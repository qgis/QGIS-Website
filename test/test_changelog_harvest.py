# -*- coding: utf-8 -*-
"""Tests for the sustaining members block added by scripts/changelog_harvest.py.

Changelogs 3.34 to 4.2 were harvested without a members list after the
"current sponsors is provided below" paragraph, so the harvester now inserts
the flagship list and a link to every sustaining member.
"""
import changelog_harvest as ch

insert = ch.ChangelogHarvester.insert_sustaining_members

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
