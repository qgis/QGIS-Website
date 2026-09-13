#!/usr/bin/env python3
"""Sync config.toml [languages] and [module.mounts] entries against the 35%
Transifex coverage threshold.

Uses data/languages.json as the authoritative list of all known languages.
- Adds languages that newly meet the threshold but are absent from config.toml.
- Removes languages that are present but have dropped below the threshold.

This means the script is self-contained: the tx-coverage CI workflow can call
it right after fetching fresh coverage data, and config.toml will immediately
reflect any language promotions or demotions — no hugo-gettext run required.

Usage:
    python3 scripts/i18n/filter_languages_by_coverage.py [options]

Options:
    --threshold FLOAT     Minimum coverage % to include a language (default: 35)
    --config PATH         Path to config.toml (default: config.toml)
    --coverage PATH       Path to tx_coverage.json (default: data/tx_coverage.json)
    --languages PATH      Path to languages.json (default: data/languages.json)
    --dry-run             Print what would change without writing the file
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

# These language codes are always kept regardless of coverage.
ALWAYS_INCLUDE: set[str] = {"en"}


def load_coverage(path: str) -> dict[str, float]:
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return {k: float(v) for k, v in raw.items()}


def load_all_languages(path: str) -> list[str]:
    """Return every language code listed in data/languages.json."""
    with open(path, encoding="utf-8") as f:
        entries = json.load(f)
    return [e["code"] for e in entries if e.get("code")]


def normalize(lang: str) -> str:
    """Lower-case and treat hyphens/underscores as equivalent for lookup."""
    return lang.lower().replace("-", "_")


def get_coverage(lang: str, coverage: dict[str, float]) -> float:
    """Return coverage % for a language code, 0 if not found."""
    n = normalize(lang)
    for k, v in coverage.items():
        if normalize(k) == n:
            return v
    return 0.0


# ── helpers for building config.toml snippets ────────────────────────────────

def _lang_block(lang: str) -> str:
    return (
        f"\n    [languages.{lang}]\n"
        f"    languageCode = \"{lang}\"\n"
        f"    weight = 2\n"
    )


def _mount_block(lang: str) -> str:
    return (
        f"\n  [[module.mounts]]\n"
        f"    source = \"content-translated/{lang}\"\n"
        f"    target = \"content\"\n"
        f"    lang = \"{lang}\"\n"
        f"  [[module.mounts]]\n"
        f"    source = \"content\"\n"
        f"    target = \"content\"\n"
        f"    lang = \"{lang}\"\n"
    )


# ── main transform ────────────────────────────────────────────────────────────

def sync_config(
    text: str,
    coverage: dict[str, float],
    threshold: float,
    all_langs: list[str],
) -> tuple[str, list[str], list[str], list[str]]:
    """Add and remove languages in config.toml text to match the threshold.

    Returns:
        (new_text, kept_langs, added_langs, removed_langs)
    """
    lines = text.splitlines(keepends=True)

    lang_header_re = re.compile(r"^\s*\[languages\.([A-Za-z0-9_-]+)\]")
    mount_header_re = re.compile(r"^\s*\[\[module\.mounts\]\]")
    module_section_re = re.compile(r"^\[module\]")
    section_start_re = re.compile(r"^\s*\[")

    # Languages currently present in config.toml.
    present: set[str] = {
        lang_header_re.match(l).group(1)
        for l in lines
        if lang_header_re.match(l)
    }

    # Languages to remove: present, below threshold, not always-included.
    to_remove: set[str] = {
        lang for lang in present
        if lang not in ALWAYS_INCLUDE and get_coverage(lang, coverage) < threshold
    }

    # Languages to add: in the master list, above threshold, not already present.
    to_add: list[str] = sorted(
        lang for lang in all_langs
        if lang not in present
        and lang not in ALWAYS_INCLUDE
        and get_coverage(lang, coverage) >= threshold
    )

    # ── Pass 1: remove below-threshold blocks ────────────────────────────────
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        lm = lang_header_re.match(line)
        if lm and lm.group(1) in to_remove:
            i += 1
            while i < len(lines) and not section_start_re.match(lines[i]):
                i += 1
            continue

        if mount_header_re.match(line):
            block: list[str] = [line]
            j = i + 1
            while j < len(lines) and not section_start_re.match(lines[j]):
                block.append(lines[j])
                j += 1
            lang_in_block: str | None = None
            for bl in block:
                kv = re.match(r'^\s*lang\s*=\s*"([^"]+)"', bl)
                if kv:
                    lang_in_block = kv.group(1)
                    break
            if lang_in_block and lang_in_block in to_remove:
                i = j
                continue
            result.extend(block)
            i = j
            continue

        result.append(line)
        i += 1

    if not to_add:
        kept = sorted({lang_header_re.match(l).group(1) for l in result if lang_header_re.match(l)})
        return "".join(result), kept, [], sorted(to_remove)

    # ── Pass 2: insert new language entries before [module] ──────────────────
    module_idx: int | None = None
    for idx, line in enumerate(result):
        if module_section_re.match(line):
            module_idx = idx
            break

    if module_idx is None:
        # No [module] section found — append language blocks at end of file.
        for lang in to_add:
            result.append(_lang_block(lang))
    else:
        insert_at = module_idx
        for lang in reversed(to_add):
            result.insert(insert_at, _lang_block(lang))

    # ── Pass 3: append new mount pairs at end of file ────────────────────────
    # Strip any trailing blank lines so we can add cleanly.
    while result and result[-1].strip() == "":
        result.pop()

    for lang in to_add:
        result.append(_mount_block(lang))

    kept = sorted({lang_header_re.match(l).group(1) for l in result if lang_header_re.match(l)})
    return "".join(result), kept, to_add, sorted(to_remove)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Sync config.toml languages against the Transifex coverage threshold.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument(
        "--threshold",
        type=float,
        default=35.0,
        metavar="PCT",
        help="Minimum coverage %% to include a language (default: %(default)s)",
    )
    ap.add_argument(
        "--config",
        default="config.toml",
        help="Path to config.toml (default: %(default)s)",
    )
    ap.add_argument(
        "--coverage",
        default=os.path.join("data", "tx_coverage.json"),
        help="Path to tx_coverage.json (default: %(default)s)",
    )
    ap.add_argument(
        "--languages",
        default=os.path.join("data", "languages.json"),
        help="Path to languages.json master list (default: %(default)s)",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing the file",
    )
    args = ap.parse_args()

    for p in (args.coverage, args.config, args.languages):
        if not Path(p).exists():
            print(f"ERROR: file not found: {p}", file=sys.stderr)
            sys.exit(1)

    coverage = load_coverage(args.coverage)
    all_langs = load_all_languages(args.languages)
    config_text = Path(args.config).read_text(encoding="utf-8")

    new_text, kept, added, removed = sync_config(config_text, coverage, args.threshold, all_langs)

    if added:
        print(f"Adding {len(added)} language(s) that newly meet {args.threshold}%:\n  {', '.join(added)}")
    if removed:
        print(f"Removing {len(removed)} language(s) below {args.threshold}%:\n  {', '.join(removed)}")
    if not added and not removed:
        print("No language changes (all qualifying languages already present).")

    print(f"Active languages ({len(kept)}): {', '.join(kept)}")

    if args.dry_run:
        print("(dry-run — no files written)")
        return

    Path(args.config).write_text(new_text, encoding="utf-8")
    print(f"Updated {args.config}")


if __name__ == "__main__":
    main()
