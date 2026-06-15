# -*- coding: utf-8 -*-
"""Tests for scripts/update_donors.py (Stripe donor sync).

Exercises name formatting, add/remove/sort behavior, the donors.json write
format, timestamp persistence, and the Stripe opt-in routing in
``get_donors`` — with the Stripe API and the filesystem fully mocked, so a
``stripe``/stdlib upgrade that changes behavior is caught.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``.
"""
import json

import update_donors as ud


def _write_json(path, obj):
    path.write_text(json.dumps(obj), encoding="utf-8")


def test_format_name_strips_punctuation_and_titlecases():
    assert ud.format_name("  john DOE.  ") == "John Doe"
    assert ud.format_name("JANE,") == "Jane"
    assert ud.format_name("alice smith") == "Alice Smith"


def test_update_donors_adds_formats_dedupes_and_sorts(tmp_path):
    f = tmp_path / "donors.json"
    _write_json(f, {"donors": ["Bob"]})

    ud.update_donors("alice", str(f))
    ud.update_donors("Bob", str(f))  # duplicate after format -> not re-added

    assert json.loads(f.read_text())["donors"] == ["Alice", "Bob"]


def test_update_donors_creates_file_when_missing(tmp_path):
    f = tmp_path / "missing.json"
    ud.update_donors("zoe", str(f))
    assert json.loads(f.read_text())["donors"] == ["Zoe"]


def test_update_donors_writes_indent_4(tmp_path):
    f = tmp_path / "donors.json"
    _write_json(f, {"donors": []})
    ud.update_donors("Tim", str(f))
    # indent=4 nests array items at 8 spaces.
    assert '\n        "Tim"' in f.read_text()


def test_remove_donor_removes_when_present(tmp_path):
    f = tmp_path / "donors.json"
    _write_json(f, {"donors": ["Alice", "Bob"]})
    ud.remove_donor("bob", str(f))
    assert json.loads(f.read_text())["donors"] == ["Alice"]


def test_remove_donor_missing_file_is_noop(tmp_path):
    f = tmp_path / "nope.json"
    ud.remove_donor("Bob", str(f))  # must not raise
    assert not f.exists()


def test_timestamp_roundtrip(tmp_path, monkeypatch):
    ts_file = tmp_path / "latest.txt"
    monkeypatch.setattr(ud, "TIMESTAMP_FILE", str(ts_file))

    assert ud.get_latest_timestamp() == 0  # missing file -> 0
    ud.save_latest_timestamp(1234567890)
    assert ud.get_latest_timestamp() == 1234567890


def test_get_donors_routes_opt_in_and_opt_out(monkeypatch):
    customers = {
        "data": [
            {"id": "c1", "name": "Alice", "created": 100, "metadata": {}},
            {
                "id": "c2",
                "name": "Bob",
                "created": 200,
                "metadata": {"list_as_donor": "false"},
            },
        ],
        "has_more": False,
    }
    # Fully mock Stripe so no network/credentials are needed.
    monkeypatch.setattr(ud.stripe.Customer, "list", lambda **kw: customers)
    monkeypatch.setattr(ud.stripe.checkout.Session, "list", lambda **kw: {"data": []})
    monkeypatch.setattr(ud, "get_latest_timestamp", lambda: 0)
    saved = {}
    monkeypatch.setattr(ud, "save_latest_timestamp", lambda ts: saved.update(ts=ts))

    calls = []
    monkeypatch.setattr(ud, "update_donors", lambda name, f: calls.append(("add", name)))
    monkeypatch.setattr(ud, "remove_donor", lambda name, f: calls.append(("remove", name)))

    ud.get_donors("data/donors.json", "List me as a donor")

    # Alice has no opt-out -> added; Bob opted out via metadata -> removed.
    assert ("add", "Alice") in calls
    assert ("remove", "Bob") in calls
    # Latest timestamp advances to the newest donation.
    assert saved["ts"] == 200
