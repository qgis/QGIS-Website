# -*- coding: utf-8 -*-
"""Tests for scripts/fetch_grants.py against the Hugo blog's RSS feed.

The blog moved from WordPress to Hugo. The new feed only carries the post
summary in ``<description>``, and its slugs keep "#" and "." as percent
encoded characters. Each post becomes a front matter only file that Hugo
lists on the grants page without building a page for it.
"""
import fetch_grants

SAMPLE_FEED = b"""<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>Grant Programme on QGIS.org Blog</title>
<link>https://blog.qgis.org/category/grant-programme/</link>
<item>
<title>QGIS Grants #11: Call for Grant Proposals 2026</title>
<link>https://blog.qgis.org/2026/03/16/qgis-grants-%2311-call-for-grant-proposals-2026/</link>
<pubDate>Mon, 16 Mar 2026 10:00:00 +0000</pubDate>
<guid>https://blog.qgis.org/2026/03/16/qgis-grants-%2311-call-for-grant-proposals-2026/</guid>
<description>&lt;p&gt;Dear QGIS Community,&lt;/p&gt;
&lt;p&gt;This year&amp;#8217;s budget is &lt;strong&gt;\xe2\x82\xac40k&lt;/strong&gt;.&lt;/p&gt;</description>
</item>
<item>
<title>Untitled</title>
<link></link>
<description>&lt;p&gt;Skipped&lt;/p&gt;</description>
</item>
</channel></rss>
"""


class FakeResponse:
    content = SAMPLE_FEED

    def raise_for_status(self):
        pass


def test_slug_drops_percent_encoded_hash():
    url = "https://blog.qgis.org/2026/03/16/qgis-grants-%2311-call-for-grant-proposals-2026/"
    assert fetch_grants.slug_from_url(url) == "qgis-grants-11-call-for-grant-proposals-2026"


def test_slug_drops_dots():
    url = "https://blog.qgis.org/2024/06/14/qgis-grant-programme-2024-update-no.-2/"
    assert fetch_grants.slug_from_url(url) == "qgis-grant-programme-2024-update-no-2"


def test_description_is_cut_to_an_excerpt():
    html = "<p>" + " ".join(f"word{i}" for i in range(30)) + "</p>"
    description = fetch_grants.extract_description(html)
    assert description.endswith("word19…")
    assert len(description.split()) == fetch_grants.EXCERPT_WORDS


def test_short_description_is_kept_whole():
    html = "<p>Funded by our <a href=\"/members/\">donors</a>!</p>\n<p>Thank you.</p>"
    assert fetch_grants.extract_description(html) == "Funded by our donors! Thank you."


def test_fetch_grants_writes_front_matter_only(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch_grants, "GRANTS_FOLDER", str(tmp_path))
    monkeypatch.setattr(fetch_grants.requests, "get", lambda *a, **k: FakeResponse())

    fetch_grants.fetch_grants()

    written = sorted(p.name for p in tmp_path.iterdir())
    assert written == ["qgis-grants-11-call-for-grant-proposals-2026.md"]

    page = (tmp_path / written[0]).read_text(encoding="utf-8")
    assert 'title: "QGIS Grants #11: Call for Grant Proposals 2026"' in page
    assert 'date: "2026-03-16"' in page
    assert 'description: "Dear QGIS Community, This year’s budget is €40k."' in page
    assert 'externalLink: "https://blog.qgis.org/2026/03/16/qgis-grants-%2311-call-for-grant-proposals-2026/"' in page
    assert "build:\n  render: link\n  list: local\n---\n" in page
    assert page.endswith("---\n")
    assert "<strong>" not in page
