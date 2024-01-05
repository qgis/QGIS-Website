import re
from pathlib import Path
from typing import Dict, List
from playwright.sync_api import Page, expect


def test_homepage_screenshot(page: Page, screenshot_dir: Path):
    page.goto("/download/linux/")
    page.pause()
    page.screenshot(path=f"{screenshot_dir}/download-linux.png", full_page=True)


def test_download_linux_page_title(page: Page):
    page.goto("/download/linux/")
    assert page.title() == "Download · Web Site"

def test_download_linux_banner_title(page: Page):
    page.goto("/download/linux/")
    hero_title = page.locator(".hero-title")
    expect(hero_title).to_contain_text("Download")

def test_download_linux_banner_subtitle(page: Page):
    page.goto("/download/linux/")
    hero_subtitle = page.locator(".hero-subtitle")
    expect(hero_subtitle).to_contain_text("Download for Linux")
