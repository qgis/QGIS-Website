# -*- coding: utf-8 -*-
"""Regression tests for scripts/update_payrexx_donors.py.

These tests pin the deterministic, importable transforms of the Payrexx donor
management script so a dependency upgrade (requests, etc.) that quietly changes
behaviour breaks the build instead of silently corrupting ``data/donors.json``.

All external I/O is mocked:

* Real network calls are never made -- the only function that touches the
  network (``get_donors``) is not exercised; ``requests`` is only imported.
* File reads/writes are redirected to ``tmp_path`` so the real read -> dedup ->
  sort -> ``json.dump`` round trip runs against a throwaway file.

A known cross-script inconsistency is documented here: ``remove_donor`` writes
``data/donors.json`` with ``indent=2`` while ``update_donors`` (both in this
script and in scripts/update_donors.py) writes it with ``indent=4``. The
``test_remove_donor_*`` tests pin the indent each write path currently uses so a
future change is caught.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``, so the module
under test can be imported directly here. The ``if __name__ == "__main__"``
guard means this import does not run any network code.
"""
import json

import update_payrexx_donors as mod


def _write_donors(path, donors):
    """Write a donors JSON file the way the script expects to read it."""
    path.write_text(
        json.dumps({"donors": donors}, ensure_ascii=False), encoding="utf-8"
    )


def _read_donors(path):
    return json.loads(path.read_text(encoding="utf-8"))["donors"]


def test_format_name_normalizes_case_and_trailing_punctuation():
    # ALL CAPS -> title case, surrounding whitespace stripped.
    assert mod.format_name("  JOHN DOE  ") == "John Doe"
    # Trailing dots/commas removed (one or many), inner punctuation kept.
    assert mod.format_name("Jane Smith.") == "Jane Smith"
    assert mod.format_name("Acme Corp,,.") == "Acme Corp"
    # Already-correct names are left effectively unchanged.
    assert mod.format_name("Maria Garcia") == "Maria Garcia"


def test_update_donors_adds_formats_and_sorts(tmp_path):
    donors_file = tmp_path / "donors.json"
    _write_donors(donors_file, ["Zoe Adams", "Anna Bell"])

    # Raw input is ALL CAPS with a trailing dot -> must be normalized on add.
    mod.update_donors("CHARLIE BROWN.", str(donors_file))

    donors = _read_donors(donors_file)
    assert donors == ["Anna Bell", "Charlie Brown", "Zoe Adams"]


def test_update_donors_is_idempotent_for_duplicates(tmp_path):
    donors_file = tmp_path / "donors.json"
    _write_donors(donors_file, ["Charlie Brown"])

    # Adding the same donor again (after formatting) must not duplicate it.
    mod.update_donors("charlie brown", str(donors_file))

    assert _read_donors(donors_file) == ["Charlie Brown"]


def test_update_donors_creates_file_when_missing(tmp_path):
    # FileNotFoundError path: start from an empty list and create the file.
    donors_file = tmp_path / "missing.json"
    assert not donors_file.exists()

    mod.update_donors("Solo Donor", str(donors_file))

    assert donors_file.exists()
    assert _read_donors(donors_file) == ["Solo Donor"]


def test_update_donors_writes_indent_4_and_unescaped_unicode(tmp_path):
    # Pins this write path's format: indent=4 and ensure_ascii=False.
    donors_file = tmp_path / "donors.json"
    _write_donors(donors_file, [])

    mod.update_donors("Renée Dupont", str(donors_file))

    text = donors_file.read_text(encoding="utf-8")
    # Non-ASCII char must survive verbatim (ensure_ascii=False).
    assert "Renée Dupont" in text
    assert "\\u" not in text
    # indent=4 -> donor entries are indented by 8 spaces (2 nesting levels).
    assert '\n        "Renée Dupont"' in text


def test_remove_donor_removes_match_and_pins_indent_2(tmp_path):
    # KNOWN INCONSISTENCY: remove_donor writes with indent=2, whereas
    # update_donors (here and in scripts/update_donors.py) uses indent=4.
    donors_file = tmp_path / "donors.json"
    _write_donors(donors_file, ["Anna Bell", "Charlie Brown"])

    # Formatting is applied before matching: "ANNA BELL." -> "Anna Bell".
    mod.remove_donor("ANNA BELL.", str(donors_file))

    assert _read_donors(donors_file) == ["Charlie Brown"]

    text = donors_file.read_text(encoding="utf-8")
    # indent=2 -> remaining donor entry is indented by 4 spaces.
    assert '\n    "Charlie Brown"' in text
    # Guard the inconsistency: this write path is NOT indent=4 (8 spaces).
    assert '\n        "Charlie Brown"' not in text


def test_remove_donor_no_match_rewrites_unchanged_list(tmp_path):
    # Edge case: removing an absent donor leaves the list intact but still
    # rewrites the file (with indent=2).
    donors_file = tmp_path / "donors.json"
    _write_donors(donors_file, ["Anna Bell"])

    mod.remove_donor("Nobody Here", str(donors_file))

    assert _read_donors(donors_file) == ["Anna Bell"]


def test_remove_donor_missing_file_does_not_write(tmp_path):
    # FileNotFoundError path: print and return without creating the file.
    donors_file = tmp_path / "missing.json"

    mod.remove_donor("Anyone", str(donors_file))

    assert not donors_file.exists()


def test_generate_api_signature_is_deterministic_hmac():
    # Pure HMAC-SHA256 + base64; pins the exact auth signature so a hashlib/
    # base64 behaviour change is caught. Computed independently of the module.
    import base64
    import hashlib
    import hmac

    query_string = "limit=100&offset=0"
    secret = "test-secret"

    expected = base64.b64encode(
        hmac.new(
            secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).digest()
    ).decode("utf-8")

    assert mod.generate_api_signature(query_string, secret) == expected
