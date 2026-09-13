# -*- coding: utf-8 -*-
"""Tests for scripts/update_donors_from_file.py.

Exercises name formatting and the file-based donor update (read existing
JSON, format + dedupe + sort new names, write back) using real temp files,
so a change in the formatting/sorting/output behavior is caught.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``.
"""
import json

import update_donors_from_file as udf


def test_format_name_strips_punctuation_and_titlecases():
    assert udf.format_name("  john DOE.  ") == "John Doe"
    assert udf.format_name("JANE,") == "Jane"
    assert udf.format_name("alice") == "Alice"


def test_update_donors_formats_dedupes_and_sorts(tmp_path):
    donors_json = tmp_path / "donors.json"
    donors_json.write_text(json.dumps({"donors": ["Bob"]}), encoding="utf-8")
    names = tmp_path / "names.txt"
    names.write_text("alice\nBOB\nCAROL,\n", encoding="utf-8")

    udf.update_donors([str(names)], str(donors_json))

    data = json.loads(donors_json.read_text())
    # "BOB" -> "Bob" (already present, not duplicated); result sorted.
    assert data["donors"] == ["Alice", "Bob", "Carol"]


def test_update_donors_creates_file_when_missing(tmp_path):
    donors_json = tmp_path / "missing.json"
    names = tmp_path / "names.txt"
    names.write_text("Zoe\nAnna\n", encoding="utf-8")

    udf.update_donors([str(names)], str(donors_json))

    assert json.loads(donors_json.read_text())["donors"] == ["Anna", "Zoe"]


def test_update_donors_skips_missing_input_file(tmp_path):
    donors_json = tmp_path / "donors.json"
    donors_json.write_text(json.dumps({"donors": ["Bob"]}), encoding="utf-8")

    # A non-existent input file must be skipped, not crash the run.
    udf.update_donors([str(tmp_path / "nope.txt")], str(donors_json))

    assert json.loads(donors_json.read_text())["donors"] == ["Bob"]


def test_update_donors_writes_indent_4(tmp_path):
    donors_json = tmp_path / "donors.json"
    donors_json.write_text(json.dumps({"donors": []}), encoding="utf-8")
    names = tmp_path / "names.txt"
    names.write_text("Tim\n", encoding="utf-8")

    udf.update_donors([str(names)], str(donors_json))

    # indent=4 nests array items at 8 spaces.
    assert '\n        "Tim"' in donors_json.read_text()
