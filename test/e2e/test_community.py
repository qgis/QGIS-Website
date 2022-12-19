import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_homepage_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/community/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/community.png", full_page=True)

def test_community_page_title(page: Page):
    page.goto("/community/")
    assert page.title() == "Our Community · QGIS Web Site"

def test_community_banner_title(page: Page):
    page.goto("/community/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("Our Community")

def test_community_banner_subtitle(page: Page):
    page.goto("/community/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("Experience the world’s most vibrant community of geospatial experts and enthusiasts")

