import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_homepage_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/value-proposition/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/value-proposition.png", full_page=True)

def test_value_page_title(page: Page):
    page.goto("/value-proposition/")
    assert page.title() == "QGIS Value Proposition · QGIS Web Site"

def test_value_banner_title(page: Page):
    page.goto("/value-proposition/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("QGIS Value Proposition")

def test_value_banner_subtitle(page: Page):
    page.goto("/value-proposition/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("")


