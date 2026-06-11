# -*- coding: utf-8 -*-
"""Regression tests for scripts/hub_images_harvest.py.

Harvesting used to clean the output directory before fetching, so a failed
fetch left it empty and dropped every previously harvested image. ``harvest()``
must fetch into a staging area and only swap it in once the fetch succeeds.
"""
import os

import pytest

import hub_images_harvest as hub


def _harvester(tmp_path):
    out = tmp_path / "hub-maps"
    out.mkdir()
    (out / "index.md").write_text("hand maintained", encoding="utf-8")
    return hub.HubHarvester("map", "https://hub.example/api/", str(out)), out


def test_failed_fetch_keeps_existing_images(tmp_path, monkeypatch):
    harvester, out = _harvester(tmp_path)
    existing = out / "old.png"
    existing.write_bytes(b"already harvested")

    def boom(*args, **kwargs):
        raise hub.requests.exceptions.RequestException("network down")

    monkeypatch.setattr(hub.requests, "get", boom)

    with pytest.raises(hub.requests.exceptions.RequestException):
        harvester.harvest()

    # A failed fetch must leave the live directory untouched.
    assert existing.is_file()
    assert existing.read_bytes() == b"already harvested"
    assert (out / "index.md").read_text(encoding="utf-8") == "hand maintained"
    assert not os.path.isdir(f"{out}.staging")


def test_successful_harvest_swaps_in_fresh_content(tmp_path, monkeypatch):
    harvester, out = _harvester(tmp_path)
    (out / "stale.png").write_bytes(b"stale")

    def fake_fetch():
        # fetch_resources writes into the staging dir (self.output_dir).
        with open(os.path.join(harvester.output_dir, "fresh.png"), "wb") as f:
            f.write(b"fresh")

    monkeypatch.setattr(harvester, "fetch_resources", fake_fetch)

    harvester.harvest()

    assert (out / "fresh.png").read_bytes() == b"fresh"
    assert not (out / "stale.png").exists()          # stale entry dropped
    assert (out / "index.md").read_text(encoding="utf-8") == "hand maintained"
    assert not os.path.isdir(f"{out}.staging")


def test_fetch_resources_passes_a_timeout(tmp_path, monkeypatch):
    harvester, _ = _harvester(tmp_path)
    calls = []

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {"results": [], "next": None}

    def fake_get(url, *args, **kwargs):
        calls.append(kwargs)
        return FakeResponse()

    monkeypatch.setattr(hub.requests, "get", fake_get)

    harvester.fetch_resources()

    assert calls and calls[0].get("timeout") == hub.REQUEST_TIMEOUT
