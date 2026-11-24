# -*- coding: utf-8 -*-
"""Tests for the Markdown post-processing in scripts/changelog_harvest.py.

Changelogs 3.34 to 4.2 were harvested without a members list after the
"current sponsors is provided below" paragraph, so the harvester now inserts
the flagship list and a link to every sustaining member. It also swaps the
highlight reel thumbnail link for an embedded YouTube player.
"""
import changelog_harvest as ch

insert = ch.ChangelogHarvester.insert_sustaining_members
embed = ch.ChangelogHarvester.embed_highlight_video

ONE_LINE = (
    "QGIS is supported by donors and sustaining members. A complete list of "
    "current sponsors is provided below - our very great thank you to all of "
    "our sponsors!\n"
    "\n"
    "QGIS is free software.\n"
)

WRAPPED = (
    "details. A complete list of current sponsors is provided below - our very big\n"
    "thank you to all of our sponsors!\n"
    "\n"
    "QGIS is free software, and you are under no obligation to pay anything\n"
)


def _expected(content: str) -> str:
    paragraph, rest = content.split("\n\n", 1)
    return paragraph + "\n\n" + ch.SUSTAINING_MEMBERS_BLOCK + rest


def test_inserts_after_one_line_paragraph() -> None:
    assert insert(ONE_LINE) == _expected(ONE_LINE)


def test_inserts_after_wrapped_paragraph() -> None:
    assert insert(WRAPPED) == _expected(WRAPPED)


def test_leaves_content_without_sponsors_paragraph(capsys) -> None:
    content = "# Changelog for QGIS 9.9\n\nNo sponsors here.\n"
    assert insert(content) == content
    assert "Warning" in capsys.readouterr().out


def test_does_not_add_a_second_block() -> None:
    once = insert(ONE_LINE)
    assert insert(once) == once


VIDEO_LINK = (
    "YouTube](https://www.youtube.com/watch?v=5X1JKx7CXZY).\n"
    "\n"
    "[![](https://img.youtube.com/vi/5X1JKx7CXZY/0.jpg)]"
    "(https://www.youtube.com/watch?v=5X1JKx7CXZY)\n"
    "\n"
    "QGIS is a community effort.\n"
)

VIDEO_PLAYER = (
    "YouTube](https://www.youtube.com/watch?v=5X1JKx7CXZY).\n"
    "\n"
    '<div class="tile video mb-3">\n'
    '  <div class="youtube" data-video-id="5X1JKx7CXZY" style="background-image: '
    'url(&quot;https://img.youtube.com/vi/5X1JKx7CXZY/maxresdefault.jpg&quot;);">\n'
    '    <iframe width="100%" height="100%" '
    'src="https://www.youtube.com/embed/5X1JKx7CXZY?autoplay=1" frameborder="0" '
    'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; '
    'picture-in-picture; web-share" allowfullscreen="true"></iframe>\n'
    "  </div>\n"
    "</div>\n"
    "\n"
    "QGIS is a community effort.\n"
)


def test_embeds_the_highlight_video() -> None:
    assert embed(VIDEO_LINK) == VIDEO_PLAYER


def test_leaves_content_without_video_link() -> None:
    content = "# Changelog for QGIS 9.9\n\nNo video for this release.\n"
    assert embed(content) == content


def test_embedding_twice_changes_nothing() -> None:
    assert embed(VIDEO_PLAYER) == VIDEO_PLAYER
