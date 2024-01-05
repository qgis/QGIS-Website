import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_homepage_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/home.png", full_page=True)

def test_homepage_has_logo(page: Page):
    page.goto("/")
    logo = page.locator(".navbar-item").first
    expect(logo).to_be_visible()

def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Web Site"

def test_homepage_banner_title(page: Page):
    page.goto("/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("About")

def test_homepage_banner_subtitle(page: Page):
    page.goto("/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("Welcome to the world’s most popular open source geospatial data management and analysis suite.")


