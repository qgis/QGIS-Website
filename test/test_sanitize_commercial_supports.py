# -*- coding: utf-8 -*-
"""Regression tests for scripts/sanitize_commercial_supports.py.

The weekly sanitize job empties a listing's URL in the committed YAML when the
link looks broken. It used to treat transient conditions (timeouts, connection
errors, rate limiting, bot-protection responses) the same as a dead link, so a
network hiccup during the run removed working URLs from the site permanently:
the script only ever empties, it never restores.
"""
import requests

import sanitize_commercial_supports as san


class _FakeResponse:
    def __init__(self, status_code=200, url=None):
        self.status_code = status_code
        self.url = url


def _patch_head(monkeypatch, outcome):
    """Make requests.Session().head() return a response or raise an exception."""

    class FakeSession:
        max_redirects = 5

        def head(self, url, **kwargs):
            if isinstance(outcome, Exception):
                raise outcome
            if outcome.url is None:
                outcome.url = url
            return outcome

    monkeypatch.setattr(san.requests, "Session", FakeSession)


def test_connection_error_keeps_url(monkeypatch):
    _patch_head(monkeypatch, requests.exceptions.ConnectionError("reset by peer"))
    assert san.check_url_redirects("https://example.com/") is False


def test_timeout_keeps_url(monkeypatch):
    _patch_head(monkeypatch, requests.exceptions.ConnectTimeout("timed out"))
    assert san.check_url_redirects("https://example.com/") is False


def test_server_error_keeps_url(monkeypatch):
    _patch_head(monkeypatch, _FakeResponse(status_code=503))
    assert san.check_url_redirects("https://example.com/") is False


def test_rate_limit_and_bot_protection_keep_url(monkeypatch):
    for status in (401, 403, 405, 408, 429):
        _patch_head(monkeypatch, _FakeResponse(status_code=status))
        assert san.check_url_redirects("https://example.com/") is False, status


def test_not_found_empties_url(monkeypatch):
    _patch_head(monkeypatch, _FakeResponse(status_code=404))
    assert san.check_url_redirects("https://example.com/") is True


def test_cross_domain_redirect_empties_url(monkeypatch):
    _patch_head(monkeypatch, _FakeResponse(url="https://parked-domain.example/"))
    assert san.check_url_redirects("https://example.com/") is True


def test_same_domain_https_redirect_keeps_url(monkeypatch):
    _patch_head(monkeypatch, _FakeResponse(url="https://www.example.com/"))
    assert san.check_url_redirects("http://example.com/") is False


def test_blank_url_is_left_alone(monkeypatch):
    assert san.check_url_redirects("") is False
    assert san.check_url_redirects("   ") is False


def test_process_file_empties_only_flagged_urls(tmp_path, monkeypatch):
    yml = tmp_path / "others.yml"
    yml.write_text(
        "- name: Dead Org\n"
        '  url: "https://dead.example/"\n'
        "- name: Live Org\n"
        '  url: "https://live.example/"\n',
        encoding="utf-8",
    )
    monkeypatch.setattr(
        san, "check_url_redirects", lambda url: url == "https://dead.example/"
    )

    assert san.process_file(str(yml)) is True

    content = yml.read_text(encoding="utf-8")
    assert '  url: ""' in content                     # dead one emptied, indent kept
    assert '  url: "https://live.example/"' in content  # live one untouched
    assert "- name: Dead Org" in content


def test_process_file_leaves_file_untouched_when_all_urls_ok(tmp_path, monkeypatch):
    yml = tmp_path / "others.yml"
    original = '- name: Live Org\n  url: "https://live.example/"\n'
    yml.write_text(original, encoding="utf-8")
    monkeypatch.setattr(san, "check_url_redirects", lambda url: False)

    assert san.process_file(str(yml)) is False
    assert yml.read_text(encoding="utf-8") == original
