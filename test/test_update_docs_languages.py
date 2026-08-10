# -*- coding: utf-8 -*-
"""Tests for scripts/update_docs_languages.py.

The docs language dropdown on /resources/hub/ is only correct as long as this
parser mirrors the LANGUAGES line of the QGIS-Documentation Makefile, including
the casing docs.qgis.org uses in its URLs. Everything here works off fixture
text — no network.
"""
import json
import os

import pytest

import update_docs_languages as uut

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

# Verbatim from https://github.com/qgis/QGIS-Documentation/blob/release_3.44/Makefile
MAKEFILE_3_44 = """\
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
LANG            = en
# currently we are building for the following languages, if you want yours to be build: ask!
LANGUAGES       = en cs de es fr hu it ja ko lt nl pl pt_BR pt_PT ro ru sr sv ta zh_Hans
SPHINXOPTS      =
"""

# The codes docs.qgis.org actually serves, from its own language switcher.
EXPECTED_DOCS_CODES = [
    "en", "cs", "de", "es", "fr", "hu", "it", "ja", "ko", "lt",
    "nl", "pl", "pt_BR", "pt_PT", "ro", "ru", "sr", "sv", "ta", "zh-Hans",
]


def _load(name):
    with open(os.path.join(DATA_DIR, name), encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def languages():
    return _load("languages.json")


def test_parses_the_release_makefile(languages):
    entries = uut.build_entries(uut.parse_languages(MAKEFILE_3_44), languages)

    assert sorted(e["docsCode"] for e in entries) == sorted(EXPECTED_DOCS_CODES)


def test_docs_codes_keep_upstream_casing(languages):
    entries = uut.build_entries(uut.parse_languages(MAKEFILE_3_44), languages)
    by_code = {e["code"]: e["docsCode"] for e in entries}

    # The website master list lower-cases these; the docs URLs do not.
    assert by_code["pt_br"] == "pt_BR"
    assert by_code["pt_pt"] == "pt_PT"
    # ...and the Makefile's zh_Hans is served under a hyphen.
    assert by_code["zh-hans"] == "zh-Hans"


def test_entries_carry_display_names_from_the_master_list(languages):
    entries = uut.build_entries(uut.parse_languages(MAKEFILE_3_44), languages)
    known = {e["code"]: e["displayName"] for e in languages}

    assert entries, "expected a non-empty language list"
    for entry in entries:
        assert entry["displayName"] == known[entry["code"]]


def test_weighted_languages_sort_before_unweighted(languages):
    entries = uut.build_entries(uut.parse_languages(MAKEFILE_3_44), languages)
    weights = {e["code"]: e.get("weight") for e in languages}

    weighted = [e["code"] for e in entries if weights.get(e["code"]) is not None]
    assert entries[0]["code"] == "en"
    assert [e["code"] for e in entries[: len(weighted)]] == weighted


def test_trailing_comment_on_the_languages_line_is_ignored(languages):
    codes = uut.parse_languages("LANGUAGES = en de # fr is not ready yet\n")

    assert codes == ["en", "de"]


def test_unknown_upstream_language_is_an_error(languages):
    with pytest.raises(uut.DocsLanguagesError, match="xx"):
        uut.build_entries(["en", "xx"], languages)


def test_missing_languages_line_is_an_error():
    with pytest.raises(uut.DocsLanguagesError, match="No LANGUAGES line"):
        uut.parse_languages("SPHINXOPTS =\n")


def test_empty_languages_line_is_an_error():
    with pytest.raises(uut.DocsLanguagesError, match="empty"):
        uut.parse_languages("LANGUAGES =    # ask us to add yours\n")


def test_committed_data_file_matches_the_master_list(languages):
    """Guard against data/docs_languages.json drifting from languages.json."""
    docs_languages = _load("docs_languages.json")
    known = {e["code"]: e for e in languages}

    assert docs_languages, "data/docs_languages.json is empty"
    for entry in docs_languages:
        assert entry["code"] in known, f"{entry['code']} missing from languages.json"
        assert entry["displayName"] == known[entry["code"]]["displayName"]
        assert uut.normalize(entry["docsCode"]) == uut.normalize(entry["code"])
