import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_homepage_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/hub/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/resources-hub.png", full_page=True)

def test_resources_page_title(page: Page):
    page.goto("/hub/")
    assert page.title() == "Resources/Hub · Web Site"

def test_resources_banner_title(page: Page):
    page.goto("/hub/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("Resources/Hub")

def test_resources_banner_subtitle(page: Page):
    page.goto("/hub/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("Discover all resources to support your work with geospatial information")

