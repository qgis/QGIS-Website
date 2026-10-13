# -*- coding: utf-8 -*-
"""Tests for scripts/update_user_groups.py and the logo helpers it uses.

People edit data/user_groups/groups.json, often in the GitHub web editor, and a
workflow builds everything else. These tests make sure:

* the committed generated files match a fresh build of the committed source,
  so nobody edits a generated file by hand or forgets a rebuild;
* each source validation rule catches the mistake it exists for, with a
  message the editor can act on;
* ids, country names, continents and map points are derived correctly;
* a logo attached to the pull request is checked: a WebP named after a group,
  that decodes, and small enough for a card or a map pin;
* a build is idempotent.

Everything works off fixtures or committed files. No network.
"""
import copy
import io
import json
import os

import pytest
from PIL import Image

import update_user_groups as uut

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
SOURCE_PATH = os.path.join(ROOT_DIR, "data", "user_groups", "groups.json")
GENERATED_PATH = os.path.join(ROOT_DIR, "static", "data", "user_groups", "user_groups.json")
COUNTRIES_PATH = os.path.join(ROOT_DIR, "data", "user_groups", "countries.json")
COMMITTED_LOGO_DIR = os.path.join(ROOT_DIR, "static", "img", "user-groups")


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


def test_committed_generated_file_matches_a_fresh_build():
    """Fails when someone edits the generated file or forgets to rebuild."""
    source = _load(SOURCE_PATH)
    countries = _load(COUNTRIES_PATH)
    assert uut.countries_are_current(countries, uut.source_country_codes(source))
    rebuilt = uut.build_generated(source, countries, COMMITTED_LOGO_DIR)
    with open(GENERATED_PATH, encoding="utf-8") as fh:
        assert fh.read() == uut.to_json(rebuilt)


def test_committed_source_has_no_logo_url():
    """Logos are files in the pull request, not links."""
    assert all("logo_url" not in g for g in _load(SOURCE_PATH)["groups"])


def test_every_committed_logo_is_a_webp_in_use():
    generated = _load(GENERATED_PATH)
    in_use = {f["properties"]["logo"] for f in generated["features"] if f["properties"]["logo"]}
    on_disk = {f"img/user-groups/{name}" for name in os.listdir(COMMITTED_LOGO_DIR)}
    assert on_disk == in_use
    assert all(name.endswith(".webp") for name in on_disk)


def test_committed_logos_pass_the_file_check():
    assert uut.check_logo_files(_load(SOURCE_PATH), COMMITTED_LOGO_DIR) == []


def test_main_check_passes_on_committed_data(monkeypatch):
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    assert uut.main(["--check"]) == 0


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
    errors = uut.validate_source(_source(_entry(website=url)))
    assert any("the website must be a full link" in e for e in errors)


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


def test_build_generated_derives_every_field(tmp_path):
    countries, _ = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    source = _source(
        {"name": "QGIS France", "country": "FR", "year": 2017, "contacts": ["A"]},
        {"id": "qgis-us", "name": "QGIS USA", "country": "US", "year": 2017, "contacts": ["B"],
         "country_name": "USA", "removed": 2025},
        {"name": "QGIS Global", "country": None, "year": 2024, "contacts": ["C"], "website": "https://example.org/"},
    )
    logo_dir = tmp_path / "logos"
    logo_dir.mkdir()
    _webp(logo_dir / "qgis-france.webp")
    generated = uut.build_generated(source, countries, logo_dir)
    fr, us, world = (f["properties"] for f in generated["features"])

    assert fr["slug"] == "qgis-france" and fr["country_name"] == "France" and fr["continent"] == "europe"
    assert fr["active"] is True and fr["removed"] is None and fr["website"] is None
    assert fr["logo"] == "img/user-groups/qgis-france.webp" and "logo_source" not in fr
    assert generated["features"][0]["geometry"] == {"type": "Point", "coordinates": [2.552, 46.696]}

    assert us["country_name"] == "USA" and us["continent"] == "north-america"
    assert us["active"] is False and us["removed"] == 2025 and us["logo"] is None

    assert world["continent"] == "global" and world["country_name"] is None
    assert generated["features"][2]["geometry"] is None


def test_unknown_continent_is_reported(tmp_path):
    countries, _ = uut.build_countries_geojson(
        {"features": [_ne_feature("SC", "SC", "Seychelles", continent="Seven seas (open ocean)")]}, ["SC"]
    )
    generated = uut.build_generated(_source({"name": "QGIS SC", "country": "SC", "year": 2020, "contacts": ["A"]}), countries, tmp_path)
    assert uut.check_continents(generated) == ["qgis-sc: Natural Earth gives no known continent for SC."]


def test_changed_groups_lists_new_changed_and_removed(tmp_path):
    countries, _ = uut.build_countries_geojson(NATURAL_EARTH, ["FR", "US"])
    before = uut.build_generated(_source(_entry(id="a", country="FR"), _entry(id="b", country="US")), countries, tmp_path)
    after = uut.build_generated(_source(_entry(id="a", country="US"), _entry(id="c", country="FR")), countries, tmp_path)
    changes = dict(uut.changed_groups(before, after))
    assert changes["a"].startswith("changed: ") and "country" in changes["a"] and "map point" in changes["a"]
    assert changes["c"] == "new group"
    assert changes["b"] == "removed from the file"

    # A field that disappears is named too
    trimmed = copy.deepcopy(after)
    del trimmed["features"][1]["properties"]["website"]
    assert dict(uut.changed_groups(after, trimmed))["c"] == "changed: website"


# ---------------------------------------------------------------------------
# Logos (attached to the pull request, never generated)
# ---------------------------------------------------------------------------
def _webp(path, size=(64, 64)):
    Image.new("RGBA", size, (88, 150, 50)).save(path, format="WEBP")
    return path


@pytest.fixture
def logo_dir(tmp_path):
    d = tmp_path / "logos"
    d.mkdir()
    return d


def test_logo_for_finds_the_file_or_returns_none(logo_dir):
    assert uut.logo_for("qgis-ch", logo_dir) is None
    _webp(logo_dir / "qgis-ch.webp")
    assert uut.logo_for("qgis-ch", logo_dir) == "img/user-groups/qgis-ch.webp"


def test_a_good_logo_folder_has_no_problems(logo_dir):
    _webp(logo_dir / "qgis-ch.webp")
    assert uut.check_logo_files(_source(_entry()), logo_dir) == []


def test_only_webp_files_are_accepted(logo_dir):
    (logo_dir / "qgis-ch.png").write_bytes(b"x")
    (logo_dir / "qgis-ch.svg").write_bytes(b"<svg/>")
    problems = dict(uut.check_logo_files(_source(_entry()), logo_dir))
    assert set(problems) == {"qgis-ch.png", "qgis-ch.svg"}
    assert "WebP file named after the group" in problems["qgis-ch.png"]


def test_a_logo_for_an_unknown_group_is_reported(logo_dir):
    _webp(logo_dir / "gone.webp")
    problems = dict(uut.check_logo_files(_source(_entry()), logo_dir))
    assert "no group has this id" in problems["gone.webp"]


def test_a_damaged_logo_is_reported(logo_dir):
    (logo_dir / "qgis-ch.webp").write_bytes(b"not an image")
    problems = dict(uut.check_logo_files(_source(_entry()), logo_dir))
    assert "damaged" in problems["qgis-ch.webp"]


def test_an_oversized_logo_is_reported(logo_dir):
    _webp(logo_dir / "qgis-ch.webp", size=(900, 400))
    problems = dict(uut.check_logo_files(_source(_entry()), logo_dir))
    assert "900 by 400 pixels" in problems["qgis-ch.webp"]


def test_a_heavy_logo_is_reported(logo_dir, monkeypatch):
    _webp(logo_dir / "qgis-ch.webp")
    monkeypatch.setattr(uut, "LOGO_MAX_BYTES", 10)
    problems = dict(uut.check_logo_files(_source(_entry()), logo_dir))
    assert "Save it again" in problems["qgis-ch.webp"]


def test_orphan_logos_are_removed(logo_dir):
    for name in ("qgis-ch.webp", "gone.webp"):
        (logo_dir / name).write_bytes(b"x")
    assert uut.remove_orphan_logos(_source(_entry()), logo_dir) == ["gone.webp"]
    assert [p.name for p in logo_dir.iterdir()] == ["qgis-ch.webp"]


# ---------------------------------------------------------------------------
# Whole runs
# ---------------------------------------------------------------------------
@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """A self contained copy of the inputs and outputs."""
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    ne = tmp_path / "ne.geojson"
    ne.write_text(json.dumps(NATURAL_EARTH), encoding="utf-8")
    (tmp_path / "logos").mkdir()

    def run(source, *extra):
        (tmp_path / "groups.json").write_text(json.dumps(source), encoding="utf-8")
        return uut.main([
            *extra, "--source", str(ne), "--groups", str(tmp_path / "groups.json"),
            "--generated", str(tmp_path / "generated.json"), "--countries", str(tmp_path / "countries.json"),
            "--logo-dir", str(tmp_path / "logos"),
        ])

    run.path = tmp_path
    run.logos = tmp_path / "logos"
    return run


def _snapshot(path):
    return {p.relative_to(path).as_posix(): p.read_bytes() for p in sorted(path.rglob("*")) if p.is_file()}


def test_build_is_idempotent(workspace):
    source = _source(_entry(country="FR"), {"name": "QGIS USA", "country": "US", "year": 2017, "contacts": ["R"]})
    _webp(workspace.logos / "qgis-ch.webp")
    assert workspace(source) == 0
    first = _snapshot(workspace.path)
    assert workspace(source) == 0
    assert _snapshot(workspace.path) == first

    generated = json.loads((workspace.path / "generated.json").read_text(encoding="utf-8"))
    assert [f["properties"]["slug"] for f in generated["features"]] == ["qgis-ch", "qgis-usa"]
    logos = {f["properties"]["slug"]: f["properties"]["logo"] for f in generated["features"]}
    assert logos == {"qgis-ch": "img/user-groups/qgis-ch.webp", "qgis-usa": None}


def test_check_writes_nothing_and_fails_on_logo_problems(workspace):
    (workspace.logos / "qgis-ch.webp").write_bytes(b"not an image")
    before = _snapshot(workspace.path)
    assert workspace(_source(_entry(country="FR")), "--check") == 1
    after = _snapshot(workspace.path)
    assert {k: v for k, v in after.items() if k != "groups.json"} == {k: v for k, v in before.items() if k != "groups.json"}


def test_build_commits_data_even_when_a_logo_is_bad(workspace, monkeypatch, capsys):
    (workspace.logos / "qgis-ch.webp").write_bytes(b"not an image")
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    assert workspace(_source(_entry(country="FR"))) == 0
    assert (workspace.path / "generated.json").is_file()
    assert "::warning title=User group logo (qgis-ch.webp)::" in capsys.readouterr().out


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
