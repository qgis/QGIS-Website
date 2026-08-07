#!/usr/bin/env python3
"""Generate data/docs_languages.json from the QGIS-Documentation Makefile.

The documentation is only built for the languages listed in the LANGUAGES
variable of the QGIS-Documentation Makefile. The website used to derive its
docs language dropdown from data/languages.json filtered by Transifex coverage
of the *website* strings, which is an unrelated signal — so the dropdown
offered languages docs.qgis.org does not serve, and omitted ones it does.

This script reads the upstream Makefile for the current LTR branch and writes
the resulting list, joined with the display names in data/languages.json, to
data/docs_languages.json for the language-select shortcode to consume.

Usage:
    python scripts/update_docs_languages.py [options]

Options:
    --conf PATH           Path to conf.json (default: data/conf.json)
    --languages PATH      Path to languages.json (default: data/languages.json)
    --output PATH         Path to write (default: data/docs_languages.json)
    --branch NAME         Override the QGIS-Documentation branch to read
    --dry-run             Print the result without writing the file
"""

import argparse
import json
import re
import sys
from pathlib import Path

import requests

MAKEFILE_URL = (
    "https://raw.githubusercontent.com/qgis/QGIS-Documentation/{branch}/Makefile"
)

# docs.qgis.org serves Simplified Chinese under a hyphen, while the Makefile
# spells it with an underscore. Every other code is used verbatim in the URL.
DOCS_CODE_OVERRIDES = {"zh_Hans": "zh-Hans", "zh_Hant": "zh-Hant"}

REQUEST_TIMEOUT = 30


class DocsLanguagesError(RuntimeError):
    """Raised when the upstream language list cannot be resolved."""


def normalize(lang: str) -> str:
    """Lower-case and treat hyphens/underscores as equivalent for lookup."""
    return lang.lower().replace("-", "_")


def parse_languages(makefile: str) -> list[str]:
    """Return the codes in the Makefile's LANGUAGES variable, upstream order."""
    match = re.search(r"^LANGUAGES\s*=\s*(.+)$", makefile, re.MULTILINE)
    if not match:
        raise DocsLanguagesError("No LANGUAGES line found in the Makefile")

    codes = match.group(1).split("#", 1)[0].split()
    if not codes:
        raise DocsLanguagesError("The LANGUAGES line in the Makefile is empty")
    return codes


def docs_code(code: str) -> str:
    """Return the code as it appears in a docs.qgis.org URL path."""
    return DOCS_CODE_OVERRIDES.get(code, code)


def load_languages(path: str | Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_entries(codes: list[str], languages: list[dict]) -> list[dict]:
    """Join upstream codes with the display names in languages.json.

    Raises if an upstream language is missing from languages.json: dropping it
    silently would re-create the very mismatch this script exists to prevent.
    """
    by_code = {normalize(e["code"]): e for e in languages if e.get("code")}

    entries = []
    missing = []
    for order, code in enumerate(codes):
        known = by_code.get(normalize(code))
        if known is None:
            missing.append(code)
            continue
        entries.append(
            {
                "code": known["code"],
                "docsCode": docs_code(code),
                "displayName": known["displayName"],
                # Sort by the master list's weight so the dropdown matches the
                # site's language ordering; unweighted entries go last, in
                # upstream order.
                "_sort": (known.get("weight", sys.maxsize), order),
            }
        )

    if missing:
        raise DocsLanguagesError(
            "These documentation languages have no entry in languages.json: "
            f"{', '.join(missing)}. Add them there first."
        )

    entries.sort(key=lambda e: e.pop("_sort"))
    return entries


def fetch_makefile(branch: str) -> str:
    url = MAKEFILE_URL.format(branch=branch)
    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conf", default=Path("data") / "conf.json")
    parser.add_argument("--languages", default=Path("data") / "languages.json")
    parser.add_argument("--output", default=Path("data") / "docs_languages.json")
    parser.add_argument(
        "--branch",
        default=None,
        help="QGIS-Documentation branch (default: release_<ltrversion>)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    branch = args.branch
    if branch is None:
        with open(args.conf, encoding="utf-8") as f:
            branch = f"release_{json.load(f)['ltrversion']}"

    try:
        entries = build_entries(
            parse_languages(fetch_makefile(branch)),
            load_languages(args.languages),
        )
    except (DocsLanguagesError, requests.RequestException) as error:
        print(f"❌ {error}", file=sys.stderr)
        return 1

    payload = json.dumps(entries, ensure_ascii=False, indent=2) + "\n"

    if args.dry_run:
        print(payload, end="")
    else:
        Path(args.output).write_text(payload, encoding="utf-8")

    print(
        f"✅ {len(entries)} documentation languages from {branch}: "
        f"{' '.join(e['docsCode'] for e in entries)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
