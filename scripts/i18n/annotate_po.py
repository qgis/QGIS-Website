#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script should be run from the root repo directory:

    $ python scripts/i18n/annotate_po.py

It adds developer comments (#.) to PO/POT entries containing non-translatable tokens,
warning translators not to modify them. Supported tokens:

    - Hugo shortcodes : {{< ref ... >}}, {{< param ... >}}
    - Pipe variables  : |ltrversion|, |version|, etc.

Modifying any of these tokens could break translated content.
"""

import glob
import re
from dataclasses import dataclass
from pathlib import Path

import polib

# ---------------------------------------------------------------------------
# Token definitions
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Token:
    label: str          # human-readable name shown in the comment
    pattern: re.Pattern # compiled regex used to detect the token in a msgid


TOKENS: list[Token] = [
    Token(
        label="{{< ref ... >}}",
        pattern=re.compile(r"\{\{<\s*ref\b"),
    ),
    Token(
        label="{{< param ... >}}",
        pattern=re.compile(r"\{\{<\s*param\b"),
    ),
    Token(
        label="|ltrversion|, |version|",
        pattern=re.compile(r"\|(?:ltrversion|version)\|"),
    ),
    Token(
        label="http:// or https:// links",
        pattern=re.compile(r"https?://"),
    ),
    Token(
        label="the url in the [Markdown links](url)",
        pattern=re.compile(r"\[.*?\]\(.*?\)"),
    ),
    Token(
        label="HTML tags",
        pattern=re.compile(r"<[^>]+>"),
    ),
]

SHORTCODES_TO_REMOVE = [
    re.compile(r"^\{\{<\s*csv-table\b"),
]

CATALOG_PATTERNS: list[str] = [
    "translations/**/*.po",
    "translations/**/*.pot",
]

DO_NOT_MODIFY = "Do NOT modify"
ONLY_TRANSLATE = "Only translate actual text."

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def build_comment(found: list[Token]) -> str:
    """Build the #. comment string for a set of matched tokens."""
    if len(found) == 1:
        return f"{DO_NOT_MODIFY} the {found[0].label} part. {ONLY_TRANSLATE}"

    labels = " or ".join(t.label for t in found)
    return f"{DO_NOT_MODIFY} {labels} parts. {ONLY_TRANSLATE}"


def find_tokens(msgid: str) -> list[Token]:
    """Return all tokens whose pattern is found in msgid."""
    return [token for token in TOKENS if token.pattern.search(msgid)]


def catalog_paths() -> list[Path]:
    """Yield unique catalog paths matching CATALOG_PATTERNS."""
    seen: set[str] = set()
    paths: list[Path] = []
    for pattern in CATALOG_PATTERNS:
        for path in glob.glob(pattern, recursive=True):
            if path not in seen:
                seen.add(path)
                paths.append(Path(path))
    return paths


def is_removable(msgid: str) -> bool:
    return any(p.search(msgid) for p in SHORTCODES_TO_REMOVE)

# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def annotate_catalog(path: Path) -> bool:
    catalog = polib.pofile(str(path))
    modified = False

    original_entries = catalog.translated_entries() + catalog.untranslated_entries()
    filtered = [e for e in original_entries if not is_removable(e.msgid)]
    if len(filtered) != len(original_entries):
        catalog[:] = filtered  # ← slice assignment, not attribute assignment
        print(f"  removed {len(original_entries) - len(filtered)} entries from {path}")
        modified = True

    for entry in catalog:
        found = find_tokens(entry.msgid)
        if not found:
            continue

        comment = build_comment(found)
        if entry.comment == comment:
            continue

        entry.comment = comment
        modified = True

    if modified:
        catalog.save(str(path))
        print(f"  annotated  {path}")

    return modified


def main() -> None:
    paths = catalog_paths()
    if not paths:
        print("No PO/POT files found.")
        return

    changed = sum(annotate_catalog(p) for p in paths)
    total = len(paths)
    print(f"\n{changed}/{total} file(s) annotated.")


if __name__ == "__main__":
    main()