#!/usr/bin/env python3
"""Fetch QGIS translation contributions from Transifex and merge into contributors.json.

Uses Transifex REST API v3 to create async project activity reports,
then aggregates per-user word counts and merges with existing contributor data.

Usage:
    python update_translation_contributors.py [--token TOKEN] [--output OUTPUT]

Environment variables:
    TX_TOKEN: Transifex API authentication token (required if --token not set)
"""

import argparse
import csv
import io
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

TRANSIFEX_API_URL = "https://rest.api.transifex.com"
ORG_SLUG = "qgis"

# QGIS projects on Transifex. Slugs must match the project URL slug on transifex.com.
QGIS_PROJECTS = [
    "QGIS",              # QGIS Desktop UI translations
    "qgis-documentation",  # QGIS Documentation
    "qgis-website",      # QGIS Website
]

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_OUTPUT = REPO_ROOT / "data" / "contributors" / "contributors.json"
DEFAULT_MAPPING = REPO_ROOT / "data" / "contributors" / "transifex_github_mapping.json"

POLL_INTERVAL = 5    # seconds between status polls
MAX_POLLS = 120      # max ~10 minutes wait per project
MIN_WORDS = 10       # minimum translated words to include a contributor


# ---------------------------------------------------------------------------
# Transifex API helpers
# ---------------------------------------------------------------------------

class PlanLimitationError(Exception):
    """Raised when the Transifex org plan does not support activity reports."""


def create_activity_report(session: requests.Session, project_slug: str) -> str:
    """Create an async project activity report and return the report ID."""
    project_id = f"o:{ORG_SLUG}:p:{project_slug}"
    url = f"{TRANSIFEX_API_URL}/project_activity_reports_async_downloads"
    payload = {
        "data": {
            "type": "project_activity_reports_async_downloads",
            "attributes": {
                # Request all-time activity.  Transifex requires date_from.
                "date_from": "2010-01-01",
            },
            "relationships": {
                "project": {
                    "data": {"type": "projects", "id": project_id}
                }
            },
        }
    }
    resp = session.post(url, json=payload)
    if resp.status_code == 403:
        errors = resp.json().get("errors", [])
        detail = errors[0].get("detail", "") if errors else ""
        if "plan" in detail.lower():
            raise PlanLimitationError(detail)
    resp.raise_for_status()
    return resp.json()["data"]["id"]


def poll_report(session: requests.Session, report_id: str) -> str:
    """Poll until the report is ready and return the download URL."""
    url = (
        f"{TRANSIFEX_API_URL}"
        f"/project_activity_reports_async_downloads/{report_id}"
    )
    for attempt in range(MAX_POLLS):
        resp = session.get(url)
        resp.raise_for_status()
        data = resp.json()["data"]
        status = data["attributes"].get("status", "")
        if status == "succeeded":
            return data["attributes"]["download_url"]
        if status == "failed":
            raise RuntimeError(f"Activity report {report_id} failed")
        print(
            f"    [{attempt + 1}/{MAX_POLLS}] status={status!r}, "
            f"waiting {POLL_INTERVAL}s…"
        )
        time.sleep(POLL_INTERVAL)
    raise TimeoutError(f"Activity report {report_id} did not complete in time")


def download_report_csv(session: requests.Session, download_url: str) -> list[dict]:
    """Download and parse the CSV activity report; return a list of row dicts."""
    resp = session.get(download_url)
    resp.raise_for_status()
    reader = csv.DictReader(io.StringIO(resp.text))
    return list(reader)


def _find_column(row: dict, candidates: list[str]) -> int:
    """Return the first value matched by a list of candidate column names."""
    for col in candidates:
        if col in row:
            try:
                return int(row[col] or 0)
            except (ValueError, TypeError):
                return 0
    return 0


def aggregate_word_counts(rows: list[dict]) -> dict[str, int]:
    """Aggregate translated word counts per Transifex username.

    The Transifex activity report CSV may use different column name styles
    depending on the plan and API version. We try several common patterns.
    """
    totals: dict[str, int] = defaultdict(int)
    user_col_candidates = ("user", "User", "username", "Username")
    word_col_candidates = (
        "translated_words",
        "Translated words",
        "words_added",
        "Words added",
        "wordcount",
    )
    for row in rows:
        username = None
        for col in user_col_candidates:
            if col in row and row[col].strip():
                username = row[col].strip()
                break
        if not username:
            continue
        word_count = _find_column(row, word_col_candidates)
        totals[username] += word_count
    return dict(totals)


# ---------------------------------------------------------------------------
# Data file helpers
# ---------------------------------------------------------------------------

def load_mapping(mapping_path: Path) -> dict[str, str]:
    """Load transifex_username → github_login mapping.

    Returns an empty dict if the file does not exist.
    """
    if not mapping_path.exists():
        return {}
    with open(mapping_path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("mappings", {})


def load_contributors(output_path: Path) -> dict[str, dict]:
    """Load contributors.json and return a dict keyed by login."""
    if not output_path.exists():
        return {}
    with open(output_path, encoding="utf-8") as fh:
        data = json.load(fh)
    return {c["login"]: c for c in data.get("contributors", [])}


def save_contributors(contributors: dict[str, dict], output_path: Path) -> None:
    """Save contributors dict to contributors.json sorted by total_contributions."""
    sorted_list = sorted(
        contributors.values(),
        key=lambda c: c.get("total_contributions", 0),
        reverse=True,
    )
    data = {
        "generated": datetime.now(tz=timezone.utc).isoformat(),
        "contributors": sorted_list,
    }
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    print(f"Saved {len(sorted_list)} contributors to {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch Transifex translation contributions and "
            "update data/contributors/contributors.json"
        )
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("TX_TOKEN"),
        help="Transifex API token (default: $TX_TOKEN env var)",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Path to contributors.json",
    )
    parser.add_argument(
        "--mapping",
        default=str(DEFAULT_MAPPING),
        help="Path to transifex_github_mapping.json",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print aggregated stats without modifying any files",
    )
    args = parser.parse_args()

    if not args.token:
        print(
            "ERROR: Transifex API token required. "
            "Set TX_TOKEN environment variable or pass --token.",
            file=sys.stderr,
        )
        sys.exit(1)

    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {args.token}",
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
    )

    output_path = Path(args.output)
    mapping_path = Path(args.mapping)

    # ------------------------------------------------------------------
    # Aggregate word counts from all QGIS Transifex projects
    # ------------------------------------------------------------------
    all_word_counts: dict[str, int] = defaultdict(int)

    plan_limited = 0
    for project_slug in QGIS_PROJECTS:
        print(f"\nProcessing Transifex project: {project_slug}")
        try:
            report_id = create_activity_report(session, project_slug)
            print(f"  Activity report created: {report_id}")
            print("  Polling for completion…")
            download_url = poll_report(session, report_id)
            print("  Downloading CSV…")
            rows = download_report_csv(session, download_url)
            word_counts = aggregate_word_counts(rows)
            total_words = sum(word_counts.values())
            print(
                f"  {len(word_counts)} contributors, "
                f"{total_words:,} total translated words"
            )
            for username, count in word_counts.items():
                all_word_counts[username] += count
        except PlanLimitationError as exc:
            print(
                f"    Detail: {exc}\n",
                file=sys.stderr,
            )
            plan_limited += 1
            continue
        except requests.HTTPError as exc:
            print(
                f"  WARNING: HTTP error for project {project_slug!r}: {exc}",
                file=sys.stderr,
            )
            continue
        except Exception as exc:  # noqa: BLE001
            print(
                f"  WARNING: Failed to fetch project {project_slug!r}: {exc}",
                file=sys.stderr,
            )
            continue

    if not all_word_counts:
        if plan_limited == len(QGIS_PROJECTS):
            print(
                "\nAll projects skipped due to Transifex plan limitation.\n"
                "No changes made. The workflow will continue without translation data.\n"
                "To enable this feature, upgrade the QGIS Transifex organization to a\n"
                "plan that includes activity reports (see https://www.transifex.com/open-source/).",
                file=sys.stderr,
            )
            sys.exit(0)
        print("\nNo translation data fetched. Exiting without changes.", file=sys.stderr)
        sys.exit(1)

    # Filter by minimum word threshold
    filtered: dict[str, int] = {
        u: c for u, c in all_word_counts.items() if c >= MIN_WORDS
    }
    print(
        f"\nAggregated {len(all_word_counts)} unique translators across all projects."
    )
    print(f"After applying minimum threshold ({MIN_WORDS} words): {len(filtered)} contributors")

    if args.dry_run:
        print("\n-- Dry run: top 20 translators --")
        for username, count in sorted(filtered.items(), key=lambda x: -x[1])[:20]:
            print(f"  {username}: {count:,} words")
        print("\nDry run complete. No files modified.")
        return

    # ------------------------------------------------------------------
    # Merge translation data into contributors.json
    # ------------------------------------------------------------------
    contributors = load_contributors(output_path)
    mapping = load_mapping(mapping_path)

    # Clear existing translations thematic for all contributors so we
    # get a clean slate on each run (prevents stale data accumulation).
    for contrib in contributors.values():
        contrib.setdefault("thematics", {}).pop("translations", None)

    # Remove previously created Transifex-only contributor entries so they
    # are fully regenerated from the latest data. We only remove entries
    # whose login starts with "tx:" — this preserves other non-GitHub
    # contributors such as those harvested with an "email:" prefix by
    # update_individual_contributors.py.
    tx_only_logins = [
        login for login in contributors if login.startswith("tx:")
    ]
    for login in tx_only_logins:
        del contributors[login]

    new_count = 0
    updated_count = 0

    for tx_username, word_count in filtered.items():
        # Attempt to map Transifex username to a known GitHub login.
        github_login = mapping.get(tx_username)

        if github_login and github_login in contributors:
            # Enrich an existing GitHub contributor with translation data.
            contributors[github_login]["thematics"]["translations"] = word_count
            updated_count += 1
        else:
            # Create a translation-only contributor entry.
            login_key = f"tx:{tx_username}"
            contributors[login_key] = {
                "login": login_key,
                "avatar_url": "",
                "total_contributions": 0,
                "thematics": {"translations": word_count},
                "has_github_account": False,
                "transifex_username": tx_username,
            }
            new_count += 1

    print(
        f"\nUpdated {updated_count} existing GitHub contributors with translation data."
    )
    print(f"Created {new_count} new translation-only contributor entries.")
    save_contributors(contributors, output_path)


if __name__ == "__main__":
    main()
