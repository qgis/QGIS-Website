# -*- coding: utf-8 -*-
"""Regression tests for fetch_feeds.py.

The members feed serialises a single member as a dict rather than a
one-element list. Iterating that dict walked its keys and crashed, so the
funders list stopped updating whenever there was exactly one member. Network
calls must also pass a timeout so a hung host cannot stall the job.
"""
import io
import json

import fetch_feeds


class _FakeResponse:
    def __init__(self, text=None, raw=None):
        self.text = text
        self.raw = raw

    def raise_for_status(self):
        pass


def _member(slug):
    return {
        "slug": slug,
        "member_url": f"https://{slug}.example",
        "image_url": f"https://{slug}.example/logo.png",
        "title": slug.title(),
        "member_level": "small",
        "member_country": "NL",
        "start_date": "2024-01-01",
        "end_date": "2025-01-01",
    }


def _install_fakes(tmp_path, monkeypatch, item_payload):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "content" / "funders").mkdir(parents=True)
    monkeypatch.setattr(fetch_feeds, "resize_image", lambda *a, **k: None)

    calls = []

    def fake_get(url, *args, **kwargs):
        calls.append(kwargs)
        if kwargs.get("stream"):
            return _FakeResponse(raw=io.BytesIO(b"image-bytes"))
        payload = {"rss": {"channel": {"item": item_payload}}}
        return _FakeResponse(text=json.dumps(payload))

    monkeypatch.setattr(fetch_feeds.requests, "get", fake_get)
    return calls


def test_single_member_dict_is_processed(tmp_path, monkeypatch):
    # A single member arrives as a dict, not a list.
    calls = _install_fakes(tmp_path, monkeypatch, _member("acme"))

    fetch_feeds.fetch_funders("https://members.example/json/")

    md = tmp_path / "content" / "funders" / "acme.md"
    assert md.is_file()
    assert 'title: "Acme"' in md.read_text(encoding="utf-8")
    # The feed request carried a timeout.
    assert calls[0].get("timeout") == fetch_feeds.REQUEST_TIMEOUT


def test_multiple_members_list_still_works(tmp_path, monkeypatch):
    _install_fakes(tmp_path, monkeypatch, [_member("acme"), _member("globex")])

    fetch_feeds.fetch_funders("https://members.example/json/")

    funders = tmp_path / "content" / "funders"
    assert (funders / "acme.md").is_file()
    assert (funders / "globex.md").is_file()
