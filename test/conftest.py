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
        {"href": "/community/", "title": "Community"},
        {"href": "/guests", "title": "Guests"},
        {"href": "https://github.com/JupiterBroadcasting/", "title": "GitHub"},
        {"href": "https://jupiter.tube", "title": "Peertube"},
        {"href": "https://www.meetup.com/jupiterbroadcasting", "title": "Meetup"},
        {
            "href": "https://www.youtube.com/user/jupiterbroadcasting",
            "title": "YouTube",
        },
        {"href": "https://twitter.com/jupitersignal", "title": "Twitter"},
        {"href": "{}/community/irc".format(base_url), "title": "IRC"},
        {
            "href": "http://www.facebook.com/pages/Jupiter-Broadcasting/156241429615",
            "title": "Facebook",
        },
        {"href": "https://discord.com/invite/n49fgkp", "title": "Self-Hosted Discord"},
        {"href": "{}/community/matrix".format(base_url), "title": "Matrix"},
        {"href": "{}/community/mumble".format(base_url), "title": "Mumble"},
        {"href": "https://t.me/jupitertelegram", "title": "Telegram"},
        {"href": "/show/coder-radio", "title": "Coder Radio"},
        {"href": "/show/jupiter-extras", "title": "Jupiter EXTRAS"},
        {"href": "/show/linux-action-news", "title": "Linux Action News"},
        {"href": "/show/linux-unplugged", "title": "LINUX Unplugged"},
        {"href": "/show/office-hours", "title": "Office Hours"},
        {"href": "/show/self-hosted", "title": "Self-Hosted"},
    ]


@fixture
def expected_dropdowns() -> List[Dict[str, str]]:
    return [{"title": "Community", "href": "/community"}]


@fixture
def expect_nav_items() -> List[Dict[str, str]]:
    return [
        {"title": "Community", "href": "/community/"},
    ]

    page.goto("/")
    nav = page.locator("#mainnavigation")
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
