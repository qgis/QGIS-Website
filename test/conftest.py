from pathlib import Path
from typing import Dict, List
from pytest import fixture


@fixture
def screenshot_dir() -> Path:
    return Path("screenshots/")


@fixture
def expected_rss_feeds() -> List[
    Dict[
        str,
        str,
    ]
]:
    return [
        {
            "href": "https://changelog.qgis.org/en/qgis/past-members/rss/",
            "title": "Past Sustaining Members Feed",
        },
        {
            "href": "https://changelog.qgis.org/en/qgis/members/rss/",
            "title": "Current Sustaining Members Feed",
        },
    ]

@fixture
def expected_dropdown_items(base_url) -> List[Dict[str, str]]:
    return [
        # Note: Order is significant
        #{"href": "/download/linux/", "title": "Linux"},
        #{"href": "/download/macos/", "title": "macOS"},
        #{"href": "/download/windows/", "title": "Windows"},
        {"href": "/documentation/overview/", "title": "Documentation"},
        {"href": "/showcase/overview/", "title": "Showcase"},
        {"href": "/roadmap/roadmap/", "title": "Roadmap"},   
    ]

@fixture
def expected_dropdowns() -> List[Dict[str, str]]:
    return [{"title": "Resources", "href": ""}]

@fixture
def expect_nav_items() -> List[Dict[str, str]]:
    return [
        {"title": "About", "href": "/about/"},
    ]

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
