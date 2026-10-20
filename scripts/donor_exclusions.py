#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Donor exclusion list.

Some donors ask not to be listed publicly. Their names are kept out of the
repository and provided through the EXCLUDED_DONORS environment variable
(a GitHub Actions repository variable), one name per line.

The donor sync scripts use is_excluded() to skip these names, and running
this module directly purges them from data/donors.json:

$ python scripts/donor_exclusions.py

Names are compared case-insensitively after the same cleanup the sync
scripts apply (trimmed, trailing dots or commas removed).
"""

import json
import os
import re

ENV_VAR = "EXCLUDED_DONORS"


def normalize_name(name):
    # Same cleanup as format_name() in the sync scripts, compared caseless
    return re.sub(r'[.,]+$', '', name.strip()).casefold()


def load_excluded_donors(env_value=None):
    """Return the set of normalized names to exclude."""
    if env_value is None:
        env_value = os.getenv(ENV_VAR, "")
    return {
        normalize_name(line)
        for line in env_value.splitlines()
        if normalize_name(line)
    }


def is_excluded(name, excluded=None):
    if excluded is None:
        excluded = load_excluded_donors()
    return normalize_name(name) in excluded


def purge_excluded_donors(donors_json_file, excluded=None):
    """Remove excluded names from the donors JSON file.

    Returns the number of entries removed. Names are never printed so they
    don't end up in public CI logs.
    """
    if excluded is None:
        excluded = load_excluded_donors()
    if not excluded:
        return 0

    try:
        with open(donors_json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return 0

    donors = data.get("donors", [])
    kept = [d for d in donors if normalize_name(d) not in excluded]
    removed = len(donors) - len(kept)
    if removed:
        data["donors"] = kept
        with open(donors_json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return removed


if __name__ == "__main__":
    count = purge_excluded_donors('data/donors.json')
    print(f"Removed {count} excluded donor(s) from the list.")
