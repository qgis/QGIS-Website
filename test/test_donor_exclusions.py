# -*- coding: utf-8 -*-
"""Tests for scripts/donor_exclusions.py (EXCLUDED_DONORS secret handling).

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``.
"""
import json

import donor_exclusions as de


def _write_json(path, obj):
    path.write_text(json.dumps(obj), encoding="utf-8")


def test_load_parses_one_name_per_line_and_ignores_blanks():
    excluded = de.load_excluded_donors("John Doe\n\n  jane SMITH.  \r\n")
    assert excluded == {"john doe", "jane smith"}


def test_load_reads_env_var(monkeypatch):
    monkeypatch.setenv("EXCLUDED_DONORS", "Alice")
    assert de.load_excluded_donors() == {"alice"}


def test_load_empty_when_env_var_unset(monkeypatch):
    monkeypatch.delenv("EXCLUDED_DONORS", raising=False)
    assert de.load_excluded_donors() == set()


def test_is_excluded_is_case_and_punctuation_insensitive():
    excluded = de.load_excluded_donors("John Doe")
    assert de.is_excluded("JOHN DOE,", excluded)
    assert not de.is_excluded("John Doerr", excluded)


def test_purge_removes_only_excluded_names(tmp_path):
    f = tmp_path / "donors.json"
    _write_json(f, {"donors": ["Alice", "John Doe", "Zoe"]})

    removed = de.purge_excluded_donors(str(f), de.load_excluded_donors("john doe"))

    assert removed == 1
    assert json.loads(f.read_text())["donors"] == ["Alice", "Zoe"]


def test_purge_does_not_rewrite_file_when_nothing_excluded(tmp_path):
    f = tmp_path / "donors.json"
    f.write_text('{"donors": ["Alice"]}', encoding="utf-8")

    assert de.purge_excluded_donors(str(f), set()) == 0
    assert f.read_text() == '{"donors": ["Alice"]}'


def test_purge_missing_file_is_noop(tmp_path):
    assert de.purge_excluded_donors(str(tmp_path / "nope.json"), {"bob"}) == 0
