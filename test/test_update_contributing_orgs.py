# -*- coding: utf-8 -*-
"""Regression tests for scripts/update_contributing_orgs.py.

The contributors API returns ``None`` whenever a request is non-200 or the
body is empty. These tests pin two reliability fixes:

* ``update_stats`` must skip a member with no API data and still save,
  rather than crashing the whole scheduled run with ``AttributeError``.
* ``get_commit_counts`` must pass a request timeout so a hung server cannot
  stall the job indefinitely.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``, so the module
under test can be imported directly here.
"""
import update_contributing_orgs as uco


def test_update_stats_skips_members_with_no_api_data(monkeypatch):
    config = {"repositories": {"web_sites": ["qgis/QGIS-Website"]}}
    orgs = [
        {
            "name": "Example Org",
            "members": [{"username": "octocat"}],
            "contributions": {
                "web_sites": {"commits": 999, "last_contribution": "2020-01-01"}
            },
        }
    ]
    saved = {}

    monkeypatch.setattr(
        uco, "load_json", lambda path: config if path == uco.CONFIG_PATH else orgs
    )
    monkeypatch.setattr(
        uco, "save_json", lambda path, data: saved.update({"path": path, "data": data})
    )
    # Simulate the API returning nothing for every query.
    monkeypatch.setattr(uco, "get_commit_counts", lambda *a, **k: None)

    # Must not raise AttributeError when the API yields no data.
    uco.update_stats()

    assert saved, "save_json should still be called when API data is missing"
    web_sites = saved["data"][0]["contributions"]["web_sites"]
    assert web_sites["commits"] == 0
    assert web_sites["last_contribution"] is None


def test_get_commit_counts_passes_a_timeout(monkeypatch):
    captured = {}

    class FakeResponse:
        status_code = 200

        def json(self):
            return {"commits": 5}

    def fake_get(url, params=None, timeout=None):
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr(uco.requests, "get", fake_get)

    uco.get_commit_counts("qgis/QGIS-Website", author="octocat")

    assert (
        captured["timeout"] == uco.REQUEST_TIMEOUT
    ), "requests.get must be called with the configured timeout"
