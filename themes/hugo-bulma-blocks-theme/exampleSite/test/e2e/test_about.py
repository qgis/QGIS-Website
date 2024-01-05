import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_about_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/about/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/about.png", full_page=True)

def test_about_page_title(page: Page):
    page.goto("/about/")
    assert page.title() == "About · Web Site"

def test_about_banner_title(page: Page):
    page.goto("/about/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("About")

def test_about_banner_subtitle(page: Page):
    page.goto("/about/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("")

