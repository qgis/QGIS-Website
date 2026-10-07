# -*- coding: utf-8 -*-
"""Tests for scripts/update_user_groups.py and the logo helpers it uses.

People edit data/user_groups/groups.json, often in the GitHub web editor, and a
workflow builds everything else. These tests make sure:

* the committed generated files match a fresh build of the committed source,
  so nobody edits a generated file by hand or forgets a rebuild;
* each source validation rule catches the mistake it exists for, with a
  message the editor can act on;
* ids, country names, continents and map points are derived correctly;
* logos are treated as hostile input: only raster images, size and pixel
  limits, no private network addresses, redirects checked hop by hop;
* a build is idempotent and only fetches logos that are new or changed.

Everything works off fixtures or committed files. No network.
"""
import copy
import io
import ipaddress
import json
import os
import socket

import pytest
from PIL import Image

import resize_image
import update_user_groups as uut
from resize_image import LogoError

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
SOURCE_PATH = os.path.join(ROOT_DIR, "data", "user_groups", "groups.json")
GENERATED_PATH = os.path.join(ROOT_DIR, "static", "data", "user_groups", "user_groups.json")
COUNTRIES_PATH = os.path.join(ROOT_DIR, "data", "user_groups", "countries.json")
LOGO_SOURCES_PATH = os.path.join(ROOT_DIR, "data", "user_groups", "logos.json")


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _entry(**overrides):
    entry = {
        "id": "qgis-ch",
        "name": "QGIS user group Switzerland",
        "country": "CH",
        "website": "https://qgis.ch/",
        "year": 2015,
        "contacts": ["François Voisard"],
        "logo_url": "https://qgis.ch/logo.png",
        "removed": None,
    }
    entry.update(overrides)
    return {k: v for k, v in entry.items() if v is not ...}


def _source(*entries):
    return {"groups": list(entries)}


def _image_bytes(fmt="PNG", size=(64, 48), frames=1):
    buffer = io.BytesIO()
    if frames > 1:
        images = [Image.new("RGB", size, (i * 40, 0, 0)) for i in range(frames)]
        images[0].save(buffer, format=fmt, save_all=True, append_images=images[1:])
    else:
        Image.new("RGBA" if fmt in ("PNG", "WEBP") else "RGB", size, (88, 150, 50)).save(buffer, format=fmt)
    return buffer.getvalue()


# ---------------------------------------------------------------------------
# Committed data
# ---------------------------------------------------------------------------
def test_committed_source_is_valid():
    assert uut.validate_source(_load(SOURCE_PATH)) == []


def test_committed_generated_files_match_a_fresh_build(tmp_path):
    """Fails when someone edits a generated file or forgets to rebuild."""
    source = _load(SOURCE_PATH)
    countries = _load(COUNTRIES_PATH)
    assert uut.countries_are_current(countries, uut.source_country_codes(source))

    # Rebuild offline: same logos on disk, nothing to download
    def no_network(url):
        raise AssertionError(f"unexpected download of {url}")

    logos, report, problems = uut.resolve_logos(
        source, _load(LOGO_SOURCES_PATH)["sources"], os.path.join(ROOT_DIR, "static", "img", "user-groups"),
        tmp_path, write=False, preview_dir=tmp_path, fetch=no_network,
    )
    assert report == [] and problems == []
    rebuilt = uut.build_generated(source, countries, logos)
    with open(GENERATED_PATH, encoding="utf-8") as fh:
        assert fh.read() == uut.to_json(rebuilt)
    with open(LOGO_SOURCES_PATH, encoding="utf-8") as fh:
        assert fh.read() == uut.to_json(uut.build_logo_sources(logos))


def test_published_geojson_has_no_logo_source():
    """Where a logo came from is internal: it stays in data/user_groups/logos.json."""
    assert all("logo_source" not in f["properties"] for f in _load(GENERATED_PATH)["features"])


def test_every_committed_logo_is_a_webp_in_use():
    generated = _load(GENERATED_PATH)
    in_use = {f["properties"]["logo"] for f in generated["features"] if f["properties"]["logo"]}
    logo_dir = os.path.join(ROOT_DIR, "static", "img", "user-groups")
    on_disk = {f"img/user-groups/{name}" for name in os.listdir(logo_dir)}
    assert on_disk == in_use
    assert all(name.endswith(".webp") for name in on_disk)


def test_main_check_passes_on_committed_data(tmp_path, monkeypatch):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    assert uut.main(["--check", "--preview-dir", str(tmp_path)]) == 0


# ---------------------------------------------------------------------------
# Source validation
# ---------------------------------------------------------------------------
def test_minimal_entry_is_valid():
    entry = {"name": "QGIS Kenya", "country": "KE", "year": 2017, "contacts": ["Benard Mitto"]}
    assert uut.validate_source(_source(entry)) == []


@pytest.mark.parametrize("source", [None, [], {}, {"groups": {}}, {"groups": "x"}])
def test_rejects_a_file_without_a_groups_list(source):
    assert uut.validate_source(source) == ['The file must contain a "groups" list.']


def test_rejects_unknown_top_level_fields_and_empty_list():
    errors = uut.validate_source({"groups": [], "extra": 1})
    assert 'Unknown top level field "extra".' in errors
    assert 'The "groups" list is empty.' in errors


def test_rejects_unknown_and_missing_fields():
    entry = _entry(**{"logo-url": "x", "contacts": ...})
    errors = uut.validate_source(_source(entry))
    assert any('unknown field "logo-url"' in e for e in errors)
    assert any('"contacts" field is missing' in e for e in errors)


def test_rejects_a_group_that_is_not_an_object():
    assert any("between { and }" in e for e in uut.validate_source(_source("QGIS Kenya")))


@pytest.mark.parametrize("country", ["ch", "CHE", "C", 41, ""])
def test_rejects_bad_country_code(country):
    errors = uut.validate_source(_source(_entry(country=country)))
    assert any("two letter code in capitals" in e for e in errors)


def test_worldwide_group_has_no_country():
    assert uut.validate_source(_source(_entry(id="global", country=None))) == []


@pytest.mark.parametrize("year", ["2015", 1999, 2027, True, 2015.0])
def test_rejects_bad_year(year):
    errors = uut.validate_source(_source(_entry(year=year)), this_year=2026)
    assert any("the year must be a number" in e for e in errors)


@pytest.mark.parametrize("contacts", ["Someone", [], ["  "], ["x" * 121], ["a"] * 11])
def test_rejects_bad_contacts(contacts):
    errors = uut.validate_source(_source(_entry(contacts=contacts)))
    assert any("contacts must be a list" in e for e in errors)


@pytest.mark.parametrize("url", ["qgis.ch", "javascript:alert(1)", "ftp://qgis.ch", "https://", "https://u:p@qgis.ch/", "https://x/" + "a" * 600])
def test_rejects_bad_links(url):
    errors = uut.validate_source(_source(_entry(website=url, logo_url=url)))
    assert any("the website must be a full link" in e for e in errors)
    assert any("the logo url must be a full link" in e for e in errors)


def test_removed_year_rules():
    assert uut.validate_source(_source(_entry(removed=2020)), this_year=2026) == []
    assert any("cannot stop before" in e for e in uut.validate_source(_source(_entry(removed=2010)), this_year=2026))
    assert any("removed must be the year" in e for e in uut.validate_source(_source(_entry(removed="2020")), this_year=2026))
    assert any("removed must be the year" in e for e in uut.validate_source(_source(_entry(removed=2030)), this_year=2026))


@pytest.mark.parametrize("gid", ["QGIS-CH", "qgis ch", "qgis--ch", "-qgis", "qgis_ch", 5])
def test_rejects_badly_formed_id(gid):
    errors = uut.validate_source(_source(_entry(id=gid)))
    assert any("the id may only use" in e for e in errors)


def test_rejects_duplicate_ids_including_derived_ones():
    errors = uut.validate_source(_source(_entry(), _entry()))
    assert any('the id "qgis-ch" is already used' in e for e in errors)

    first = {"name": "QGIS México", "country": "MX", "year": 2017, "contacts": ["A"]}
    second = {"name": "QGIS Mexico", "country": "MX", "year": 2020, "contacts": ["B"]}
    errors = uut.validate_source(_source(first, second))
    assert any('the id "qgis-mexico" is already used' in e for e in errors)


def test_rejects_name_without_usable_id():
    entry = {"name": "日本", "country": "JP", "year": 2016, "contacts": ["A"]}
    assert any("add an id" in e for e in uut.validate_source(_source(entry)))


def test_messages_name_the_group():
    errors = uut.validate_source(_source(_entry(), _entry(id="x", name="QGIS Kenya", year="x")))
    assert errors and all(e.startswith("Group 2 (QGIS Kenya)") for e in errors)


# ---------------------------------------------------------------------------
# Ids and derivation
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "name, expected",
    [
        ("QGIS México", "qgis-mexico"),
        ("Asociația Utilizatorilor QGIS", "asociatia-utilizatorilor-qgis"),
        ("QGIS  User Group (OSGeo.JP)", "qgis-user-group-osgeo-jp"),
        ("  QGIS Lëtzebuerg! ", "qgis-letzebuerg"),
    ],
)
def test_slugify(name, expected):
    assert uut.slugify(name) == expected


def test_group_id_prefers_explicit_id():
    assert uut.group_id({"id": "qgis-ch", "name": "Anything"}) == "qgis-ch"
    assert uut.group_id({"name": "QGIS Kenya"}) == "qgis-kenya"


def _ne_feature(iso, iso_eh, name, name_long=None, continent="Europe", label=(0.5, 0.5)):
    square = [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]]
    return {
        "type": "Feature",
        "properties": {
            "ISO_A2": iso,
            "ISO_A2_EH": iso_eh,
            "NAME": name,
            "NAME_LONG": name_long or name,
            "CONTINENT": continent,
            "LABEL_X": label[0],
            "LABEL_Y": label[1],
        },
        "geometry": {"type": "Polygon", "coordinates": square},
    }


NATURAL_EARTH = {
    "type": "FeatureCollection",
    "features": [
        _ne_feature("-99", "AU", "Ashmore and Cartier Is.", continent="Oceania"),
        _ne_feature("AU", "AU", "Australia", continent="Oceania"),
        _ne_feature("-99", "FR", "France", label=(2.5522751, 46.6961131)),
        _ne_feature("-99", "XK", "Kosovo"),
        _ne_feature("US", "US", "United States of America", "United States", "North America", (-97.48, 39.54)),
        _ne_feature("-99", "-99", "Somaliland", continent="Africa"),
    ],
}


def test_select_prefers_iso_a2_and_falls_back_to_eh():
    selected, missing = uut.select_countries(NATURAL_EARTH, ["AU", "FR", "XK", "ZZ"])
    assert selected["AU"]["properties"]["NAME"] == "Australia"
    assert selected["FR"]["properties"]["NAME"] == "France"
    assert selected["XK"]["properties"]["NAME"] == "Kosovo"
    assert missing == ["ZZ"]


def test_countries_carry_long_name_continent_and_label_point():
    countries, missing = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    assert missing == []
    props = {f["properties"]["iso_a2"]: f["properties"] for f in countries["features"]}
    assert props["US"] == {"iso_a2": "US", "name": "United States", "continent": "north-america", "label": [-97.48, 39.54]}
    assert props["FR"]["label"] == [2.552, 46.696]
    assert countries["features"][0]["geometry"]["type"] == "MultiPolygon"
    assert "_automated_warning" in countries


def test_countries_are_current():
    countries, _ = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    assert uut.countries_are_current(countries, ["FR", "US"])
    assert not uut.countries_are_current(countries, ["FR"])
    assert not uut.countries_are_current(countries, ["FR", "US", "XK"])
    assert not uut.countries_are_current(None, ["FR"])
    old = copy.deepcopy(countries)
    del old["features"][0]["properties"]["continent"]
    assert not uut.countries_are_current(old, ["FR", "US"])
    stale_header = copy.deepcopy(countries)
    stale_header["_automated_warning"]["warning"] = "Edit data/user_groups.json instead."
    assert not uut.countries_are_current(stale_header, ["FR", "US"])


def test_build_generated_derives_every_field():
    countries, _ = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    source = _source(
        {"name": "QGIS France", "country": "FR", "year": 2017, "contacts": ["A"]},
        {"id": "qgis-us", "name": "QGIS USA", "country": "US", "year": 2017, "contacts": ["B"],
         "country_name": "USA", "removed": 2025},
        {"name": "QGIS Global", "country": None, "year": 2024, "contacts": ["C"], "website": "https://example.org/"},
    )
    logos = {"qgis-france": {"logo": "img/user-groups/qgis-france.webp", "logo_source": "https://x/logo.png"}}
    generated = uut.build_generated(source, countries, logos)
    fr, us, world = (f["properties"] for f in generated["features"])

    assert fr["slug"] == "qgis-france" and fr["country_name"] == "France" and fr["continent"] == "europe"
    assert fr["active"] is True and fr["removed"] is None and fr["website"] is None
    assert fr["logo"] == "img/user-groups/qgis-france.webp" and "logo_source" not in fr
    assert uut.build_logo_sources(logos)["sources"] == {"qgis-france": "https://x/logo.png"}
    assert generated["features"][0]["geometry"] == {"type": "Point", "coordinates": [2.552, 46.696]}

    assert us["country_name"] == "USA" and us["continent"] == "north-america"
    assert us["active"] is False and us["removed"] == 2025 and us["logo"] is None

    assert world["continent"] == "global" and world["country_name"] is None
    assert generated["features"][2]["geometry"] is None


def test_unknown_continent_is_reported():
    countries, _ = uut.build_countries_geojson(
        {"features": [_ne_feature("SC", "SC", "Seychelles", continent="Seven seas (open ocean)")]}, ["SC"]
    )
    generated = uut.build_generated(_source({"name": "QGIS SC", "country": "SC", "year": 2020, "contacts": ["A"]}), countries, {})
    assert uut.check_continents(generated) == ["qgis-sc: Natural Earth gives no known continent for SC."]


def test_changed_groups_lists_new_changed_and_removed():
    countries, _ = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    before = uut.build_generated(_source(_entry(id="a", country="FR"), _entry(id="b", country="US")), countries, {})
    after = uut.build_generated(_source(_entry(id="a", country="US"), _entry(id="c", country="FR")), countries, {})
    changes = dict(uut.changed_groups(before, after))
    assert changes["a"].startswith("changed: ") and "country" in changes["a"] and "map point" in changes["a"]
    assert changes["c"] == "new group"
    assert changes["b"] == "removed from the file"

    # A field that disappears is named too
    trimmed = copy.deepcopy(after)
    del trimmed["features"][1]["properties"]["website"]
    assert dict(uut.changed_groups(after, trimmed))["c"] == "changed: website"


# ---------------------------------------------------------------------------
# Logo normalisation (hostile input)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("fmt", ["PNG", "JPEG", "WEBP", "GIF"])
def test_normalize_accepts_raster_formats(tmp_path, fmt):
    dest = tmp_path / "out" / "logo.webp"
    resize_image.normalize_logo(_image_bytes(fmt, size=(600, 300)), dest)
    with Image.open(dest) as img:
        assert img.format == "WEBP"
        assert img.size == (256, 128)


def test_normalize_keeps_first_frame_of_animation(tmp_path):
    dest = tmp_path / "logo.webp"
    resize_image.normalize_logo(_image_bytes("GIF", frames=3), dest)
    with Image.open(dest) as img:
        assert getattr(img, "n_frames", 1) == 1


def test_normalize_strips_metadata_and_trailing_data(tmp_path):
    buffer = io.BytesIO()
    Image.new("RGB", (64, 64), "green").save(buffer, format="JPEG", comment=b"secret")
    data = buffer.getvalue() + b"<script>alert(1)</script>"
    dest = tmp_path / "logo.webp"
    resize_image.normalize_logo(data, dest)
    raw = dest.read_bytes()
    assert b"secret" not in raw and b"<script>" not in raw


@pytest.mark.parametrize(
    "data, message",
    [
        (b'<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg"></svg>', "SVG logos are not accepted"),
        (b"<svg onload=alert(1)></svg>", "SVG logos are not accepted"),
        (b"<!DOCTYPE html><html><body>Not found</body></html>", "returns a web page"),
        (b"just some text", "not a PNG, JPEG, GIF or WebP"),
        (b"", "not a PNG, JPEG, GIF or WebP"),
    ],
)
def test_normalize_refuses_non_images(tmp_path, data, message):
    with pytest.raises(LogoError, match=message):
        resize_image.normalize_logo(data, tmp_path / "logo.webp")
    assert not (tmp_path / "logo.webp").exists()


def test_normalize_refuses_other_image_formats(tmp_path):
    buffer = io.BytesIO()
    Image.new("RGB", (64, 64)).save(buffer, format="BMP")
    with pytest.raises(LogoError, match="not a PNG, JPEG, GIF or WebP"):
        resize_image.normalize_logo(buffer.getvalue(), tmp_path / "logo.webp")


def test_normalize_refuses_truncated_image(tmp_path):
    data = _image_bytes("PNG", size=(300, 300))
    with pytest.raises(LogoError, match="damaged"):
        resize_image.normalize_logo(data[: len(data) // 2], tmp_path / "logo.webp")


def test_normalize_refuses_pixel_bomb(tmp_path):
    # A tiny file whose header claims 30000 x 30000 pixels
    buffer = io.BytesIO()
    Image.new("1", (30000, 30000)).save(buffer, format="PNG")
    assert len(buffer.getvalue()) < 1_000_000
    with pytest.raises(LogoError, match="too many pixels"):
        resize_image.normalize_logo(buffer.getvalue(), tmp_path / "logo.webp")
    assert Image.MAX_IMAGE_PIXELS != resize_image.LOGO_MAX_PIXELS  # limit restored


def test_normalize_refuses_tiny_images(tmp_path):
    with pytest.raises(LogoError, match="too small"):
        resize_image.normalize_logo(_image_bytes("PNG", size=(10, 200)), tmp_path / "logo.webp")


# ---------------------------------------------------------------------------
# Logo download (hostile URLs)
# ---------------------------------------------------------------------------
class FakeResponse:
    def __init__(self, status=200, body=b"", headers=None, chunk=1024):
        self.status_code = status
        self.headers = headers or {}
        self.body = body
        self.chunk = chunk
        self.is_redirect = status in (301, 302, 303, 307, 308) and "Location" in self.headers

    def iter_content(self, size):
        for i in range(0, len(self.body), self.chunk):
            yield self.body[i:i + self.chunk]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class FakeSession:
    def __init__(self, responses):
        self.responses = dict(responses)
        self.requested = []

    def get(self, url, **kwargs):
        assert kwargs["allow_redirects"] is False and kwargs["stream"] is True and kwargs["timeout"]
        self.requested.append(url)
        return self.responses[url]


@pytest.fixture
def dns(monkeypatch):
    """Resolve hosts from a table instead of the network."""
    table = {"qgis.example": "93.184.216.34", "evil.example": "169.254.169.254", "lan.example": "192.168.1.10"}

    def getaddrinfo(host, port, *args, **kwargs):
        try:
            ip = str(ipaddress.ip_address(host))  # literal addresses resolve to themselves
        except ValueError:
            try:
                ip = table[host]
            except KeyError:
                raise socket.gaierror(host)
        family = socket.AF_INET6 if ":" in ip else socket.AF_INET
        return [(family, socket.SOCK_STREAM, 6, "", (ip, port))]

    monkeypatch.setattr(resize_image.socket, "getaddrinfo", getaddrinfo)
    return table


def test_fetch_downloads_a_public_image(dns):
    session = FakeSession({"https://qgis.example/logo.png": FakeResponse(body=b"PNGDATA")})
    assert resize_image.fetch_image_bytes("https://qgis.example/logo.png", session) == b"PNGDATA"


def test_fetch_follows_a_checked_redirect(dns):
    session = FakeSession({
        "https://qgis.example/old": FakeResponse(301, headers={"Location": "/new.png"}),
        "https://qgis.example/new.png": FakeResponse(body=b"IMG"),
    })
    assert resize_image.fetch_image_bytes("https://qgis.example/old", session) == b"IMG"
    assert session.requested == ["https://qgis.example/old", "https://qgis.example/new.png"]


@pytest.mark.parametrize("url", [
    "http://169.254.169.254/latest/meta-data/",
    "http://127.0.0.1/logo.png",
    "http://[::1]/logo.png",
    "http://10.0.0.5/logo.png",
    "http://evil.example/logo.png",
    "http://lan.example/logo.png",
])
def test_fetch_refuses_private_addresses(dns, url):
    with pytest.raises(LogoError, match="private network address"):
        resize_image.fetch_image_bytes(url, FakeSession({}))


def test_fetch_refuses_a_redirect_to_a_private_address(dns):
    session = FakeSession({
        "https://qgis.example/logo.png": FakeResponse(302, headers={"Location": "http://evil.example/latest/meta-data/"}),
    })
    with pytest.raises(LogoError, match="private network address"):
        resize_image.fetch_image_bytes("https://qgis.example/logo.png", session)
    assert session.requested == ["https://qgis.example/logo.png"]


def test_fetch_refuses_too_many_redirects(dns):
    loop = {f"https://qgis.example/{i}": FakeResponse(302, headers={"Location": f"/{i + 1}"}) for i in range(10)}
    with pytest.raises(LogoError, match="redirects too many times"):
        resize_image.fetch_image_bytes("https://qgis.example/0", FakeSession(loop))


@pytest.mark.parametrize("url, message", [
    ("file:///etc/passwd", "must start with https://"),
    ("ftp://qgis.example/logo.png", "must start with https://"),
    ("https://user:secret@qgis.example/logo.png", "user name or password"),
    ("https://unknown.example/logo.png", "could not find the website"),
])
def test_fetch_refuses_unsafe_or_unknown_urls(dns, url, message):
    with pytest.raises(LogoError, match=message):
        resize_image.fetch_image_bytes(url, FakeSession({}))


def test_fetch_stops_oversized_downloads(dns, monkeypatch):
    monkeypatch.setattr(resize_image, "LOGO_MAX_BYTES", 10_000)
    session = FakeSession({"https://qgis.example/big.png": FakeResponse(body=b"x" * 50_000)})
    with pytest.raises(LogoError, match="larger than 5 MB"):
        resize_image.fetch_image_bytes("https://qgis.example/big.png", session)


def test_fetch_reports_http_errors(dns):
    session = FakeSession({"https://qgis.example/gone.png": FakeResponse(404)})
    with pytest.raises(LogoError, match="error 404"):
        resize_image.fetch_image_bytes("https://qgis.example/gone.png", session)


# ---------------------------------------------------------------------------
# Logo resolution
# ---------------------------------------------------------------------------
@pytest.fixture
def dirs(tmp_path):
    logo_dir, upload_dir, preview_dir = tmp_path / "logos", tmp_path / "uploads", tmp_path / "preview"
    for d in (logo_dir, upload_dir):
        d.mkdir()
    return logo_dir, upload_dir, preview_dir


def _previous(gid, logo_source):
    return {gid: logo_source}


def test_new_logo_link_is_downloaded(dirs):
    logo_dir, upload_dir, _ = dirs
    fetched = []
    fetch = lambda url: fetched.append(url) or _image_bytes()
    logos, report, problems = uut.resolve_logos(_source(_entry()), None, logo_dir, upload_dir, write=True, fetch=fetch)
    assert fetched == ["https://qgis.ch/logo.png"]
    assert logos["qgis-ch"] == {"logo": "img/user-groups/qgis-ch.webp", "logo_source": "https://qgis.ch/logo.png"}
    assert report == [("qgis-ch", "logo downloaded and converted")] and problems == []
    assert (logo_dir / "qgis-ch.webp").is_file()


def test_unchanged_logo_link_is_not_downloaded_again(dirs):
    logo_dir, upload_dir, _ = dirs
    (logo_dir / "qgis-ch.webp").write_bytes(_image_bytes("WEBP"))
    def fetch(url):
        raise AssertionError("should not download")
    logos, report, _ = uut.resolve_logos(
        _source(_entry()), _previous("qgis-ch", "https://qgis.ch/logo.png"), logo_dir, upload_dir, write=True, fetch=fetch
    )
    assert logos["qgis-ch"]["logo_source"] == "https://qgis.ch/logo.png" and report == []


def test_changed_logo_link_is_downloaded_again(dirs):
    logo_dir, upload_dir, _ = dirs
    (logo_dir / "qgis-ch.webp").write_bytes(_image_bytes("WEBP"))
    logos, report, _ = uut.resolve_logos(
        _source(_entry(logo_url="https://qgis.ch/new.png")), _previous("qgis-ch", "https://qgis.ch/logo.png"),
        logo_dir, upload_dir, write=True, fetch=lambda url: _image_bytes(),
    )
    assert logos["qgis-ch"]["logo_source"] == "https://qgis.ch/new.png"
    assert report == [("qgis-ch", "logo downloaded and converted")]


def test_upload_wins_over_link_and_is_removed_after_conversion(dirs):
    logo_dir, upload_dir, _ = dirs
    (upload_dir / "qgis-ch.PNG").write_bytes(_image_bytes("PNG"))
    def fetch(url):
        raise AssertionError("should not download")
    logos, report, _ = uut.resolve_logos(_source(_entry()), None, logo_dir, upload_dir, write=True, fetch=fetch)
    assert logos["qgis-ch"] == {"logo": "img/user-groups/qgis-ch.webp", "logo_source": None}
    assert report == [("qgis-ch", "uploaded file qgis-ch.PNG converted")]
    assert (logo_dir / "qgis-ch.webp").is_file() and not any(upload_dir.iterdir())


def test_check_mode_writes_only_to_the_preview_folder(dirs):
    logo_dir, upload_dir, preview_dir = dirs
    (upload_dir / "qgis-ch.jpg").write_bytes(_image_bytes("JPEG"))
    uut.resolve_logos(_source(_entry()), None, logo_dir, upload_dir, write=False, preview_dir=preview_dir)
    assert (preview_dir / "qgis-ch.webp").is_file()
    assert not any(logo_dir.iterdir())
    assert (upload_dir / "qgis-ch.jpg").is_file()


def test_failed_download_keeps_the_previous_logo(dirs):
    logo_dir, upload_dir, _ = dirs
    (logo_dir / "qgis-ch.webp").write_bytes(_image_bytes("WEBP"))
    def fetch(url):
        raise LogoError("The logo link answered with error 404.")
    logos, report, problems = uut.resolve_logos(
        _source(_entry(logo_url="https://qgis.ch/new.png")), _previous("qgis-ch", "https://qgis.ch/logo.png"),
        logo_dir, upload_dir, write=True, fetch=fetch,
    )
    assert problems == [("qgis-ch", "The logo link answered with error 404.")]
    assert logos["qgis-ch"] == {"logo": "img/user-groups/qgis-ch.webp", "logo_source": "https://qgis.ch/logo.png"}


def test_failed_first_download_falls_back_to_no_logo(dirs):
    logo_dir, upload_dir, _ = dirs
    def fetch(url):
        raise LogoError("SVG logos are not accepted.")
    logos, _, problems = uut.resolve_logos(_source(_entry()), None, logo_dir, upload_dir, write=True, fetch=fetch)
    assert logos["qgis-ch"] == {"logo": None, "logo_source": None} and len(problems) == 1


def test_bad_upload_is_reported_and_kept_for_the_editor(dirs):
    logo_dir, upload_dir, _ = dirs
    (upload_dir / "qgis-ch.png").write_bytes(b"<svg></svg>")
    _, _, problems = uut.resolve_logos(_source(_entry()), None, logo_dir, upload_dir, write=True, fetch=lambda u: b"")
    assert problems == [("qgis-ch", "qgis-ch.png: SVG logos are not accepted. Use a PNG, JPEG, GIF or WebP image.")]


def test_group_without_link_keeps_its_existing_logo(dirs):
    logo_dir, upload_dir, _ = dirs
    (logo_dir / "qgis-ch.webp").write_bytes(_image_bytes("WEBP"))
    logos, _, _ = uut.resolve_logos(_source(_entry(logo_url=...)), None, logo_dir, upload_dir, write=True)
    assert logos["qgis-ch"]["logo"] == "img/user-groups/qgis-ch.webp"


def test_unmatched_uploads_are_reported(dirs):
    _, upload_dir, _ = dirs
    for name in ("README.md", "qgis-ch.png", "qgis-chh.png", "qgis-ch.svg"):
        (upload_dir / name).write_bytes(b"x")
    problems = dict(uut.unmatched_uploads(_source(_entry()), upload_dir))
    assert set(problems) == {"qgis-chh.png", "qgis-ch.svg"}
    assert "no group has this id" in problems["qgis-chh.png"]
    assert "only PNG, JPEG, GIF or WebP" in problems["qgis-ch.svg"]


def test_orphan_logos_are_removed(dirs):
    logo_dir, _, _ = dirs
    for name in ("qgis-ch.webp", "gone.webp"):
        (logo_dir / name).write_bytes(b"x")
    assert uut.remove_orphan_logos(_source(_entry()), logo_dir) == ["gone.webp"]
    assert [p.name for p in logo_dir.iterdir()] == ["qgis-ch.webp"]


# ---------------------------------------------------------------------------
# Whole runs
# ---------------------------------------------------------------------------
@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """A self contained copy of the inputs and outputs, with a fake network."""
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    ne = tmp_path / "ne.geojson"
    ne.write_text(json.dumps(NATURAL_EARTH), encoding="utf-8")
    (tmp_path / "logos").mkdir()
    (tmp_path / "uploads").mkdir()
    fetched = []
    monkeypatch.setattr(uut, "fetch_image_bytes", lambda url: fetched.append(url) or _image_bytes())

    def run(source, *extra):
        (tmp_path / "groups.json").write_text(json.dumps(source), encoding="utf-8")
        return uut.main([
            *extra, "--source", str(ne), "--groups", str(tmp_path / "groups.json"),
            "--generated", str(tmp_path / "generated.json"), "--countries", str(tmp_path / "countries.json"),
            "--logo-dir", str(tmp_path / "logos"), "--upload-dir", str(tmp_path / "uploads"),
            "--logo-sources", str(tmp_path / "logo_sources.json"),
        ])

    run.path = tmp_path
    run.fetched = fetched
    return run


def _snapshot(path):
    return {p.relative_to(path).as_posix(): p.read_bytes() for p in sorted(path.rglob("*")) if p.is_file()}


def test_build_is_idempotent(workspace):
    source = _source(_entry(country="FR"), {"name": "QGIS USA", "country": "US", "year": 2017, "contacts": ["R"]})
    assert workspace(source) == 0
    first = _snapshot(workspace.path)
    assert workspace(source) == 0
    assert _snapshot(workspace.path) == first
    assert workspace.fetched == ["https://qgis.ch/logo.png"]

    generated = json.loads((workspace.path / "generated.json").read_text(encoding="utf-8"))
    assert [f["properties"]["slug"] for f in generated["features"]] == ["qgis-ch", "qgis-usa"]
    assert all("logo_source" not in f["properties"] for f in generated["features"])
    # The second run skipped the download because the link was recorded here
    sources = json.loads((workspace.path / "logo_sources.json").read_text(encoding="utf-8"))
    assert sources["sources"] == {"qgis-ch": "https://qgis.ch/logo.png"}


def test_check_writes_nothing_and_fails_on_logo_problems(workspace, monkeypatch):
    def fetch(url):
        raise LogoError("SVG logos are not accepted.")
    monkeypatch.setattr(uut, "fetch_image_bytes", fetch)
    before = _snapshot(workspace.path)
    assert workspace(_source(_entry(country="FR")), "--check") == 1
    after = _snapshot(workspace.path)
    assert {k: v for k, v in after.items() if k != "groups.json"} == {k: v for k, v in before.items() if k != "groups.json"}


def test_build_commits_data_even_when_a_logo_fails(workspace, monkeypatch, capsys):
    def fetch(url):
        raise LogoError("The logo link answered with error 404.")
    monkeypatch.setattr(uut, "fetch_image_bytes", fetch)
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    assert workspace(_source(_entry(country="FR"))) == 0
    assert (workspace.path / "generated.json").is_file()
    assert "::warning title=User group logo (qgis-ch)::The logo link answered with error 404." in capsys.readouterr().out


def test_unknown_country_code_fails(workspace, capsys):
    assert workspace(_source(_entry(country="ZZ"))) == 1
    assert 'No country has the code "ZZ"' in capsys.readouterr().out
    assert not (workspace.path / "generated.json").exists()


def test_invalid_json_gives_a_readable_message(workspace, capsys):
    (workspace.path / "groups.json").write_text('{"groups": [ {"name": "x",} ]}', encoding="utf-8")
    code = uut.main(["--check", "--groups", str(workspace.path / "groups.json")])
    assert code == 1
    assert "not valid JSON near line 1" in capsys.readouterr().out


def test_report_goes_to_the_github_job_summary(workspace, monkeypatch):
    summary = workspace.path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    assert workspace(_source(_entry(country="FR", year="2015")), "--check") == 1
    text = summary.read_text(encoding="utf-8")
    assert text.startswith("## User groups check") and "the year must be a number" in text


# ---------------------------------------------------------------------------
# Simplification
# ---------------------------------------------------------------------------
def test_simplify_line_keeps_endpoints_and_drops_collinear_points():
    assert uut.simplify_line([(0, 0), (1, 0.001), (2, 0), (3, 0)], 0.01) == [(0, 0), (3, 0)]


def test_simplify_line_keeps_significant_vertex():
    line = [(0, 0), (1, 1), (2, 0)]
    assert uut.simplify_line(line, 0.1) == line


def test_simplify_ring_stays_closed_and_drops_slivers():
    ring = uut.simplify_ring([[0, 0], [1, 0], [1, 1], [0.5, 1.0001], [0, 1], [0, 0]], 0.01)
    assert ring[0] == ring[-1] and len(ring) >= 4
    assert uut.simplify_ring([[0, 0], [0.001, 0], [0.001, 0.001], [0, 0]], 0.01) is None


def test_simplify_geometry_returns_multipolygon_and_drops_tiny_islands():
    big = [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]]
    tiny = [[[20, 20], [20.001, 20], [20.001, 20.001], [20, 20]]]
    result = uut.simplify_geometry({"type": "MultiPolygon", "coordinates": [big, tiny]}, 0.01)
    assert result["type"] == "MultiPolygon" and len(result["coordinates"]) == 1
    with pytest.raises(ValueError):
        uut.simplify_geometry({"type": "Point", "coordinates": [0, 0]})
