import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_dropdowns(page: Page, expected_dropdown_items):
    page.goto("/")

    for dropdown_item in expected_dropdown_items:
        selector = '.navbar-item > .navbar-dropdown > a[href^="{}"]'.format(
            dropdown_item["href"]
        )
        element = page.locator(selector)
        expect(element).to_contain_text(dropdown_item["title"])


def test_nav(page: Page, expected_dropdowns, expect_nav_items):

    page.goto("/")
    nav = page.locator(".navbar")
    expect(nav).to_be_visible()
    dropdown_nav_items = page.locator(".navbar-start > * > a")
    count = dropdown_nav_items.count()
    for i in range(count):
        expect(dropdown_nav_items.nth(i)).to_contain_text(
            expected_dropdowns[i]["title"]
        )
        expect(dropdown_nav_items.nth(i)).to_have_attribute(
            "href", expected_dropdowns[i]["href"]
        )

    nav_items = page.locator(".navbar-start > a")
    count = nav_items.count()
    for i in range(count):
        expect(nav_items.nth(i)).to_contain_text(expect_nav_items[i]["title"])
        expect(nav_items.nth(i)).to_have_attribute("href", expect_nav_items[i]["href"])

    nav_image = page.locator(".navbar-brand > a > img")

    expect(nav_image.nth(0)).to_be_visible()
