# -*- coding: utf-8 -*-
"""Regression tests for scripts/update_supporting_contributors.py.

This script converts Supporting Contributor XLSX responses into
``supporting.json`` plus a companion GeoJSON file. These tests pin the
deterministic parsing/transform/aggregation logic so a dependency upgrade
(pandas, requests, etc.) that changes behaviour fails loudly:

* ``parse_date`` normalises pandas ``Timestamp`` and assorted string formats
  to ISO ``YYYY-MM-DD`` (and gracefully returns ``None`` for junk/NaT).
* ``is_active_contributor`` applies the 3-year "active" threshold.
* ``parse_roles`` splits a comma list into a clean role list.
* ``generate_avatar_filename`` slugifies names into the avatar path.
* ``xlsx_to_supporting_json`` performs the full read -> filter -> transform
  -> sort -> JSON/GeoJSON aggregation, mocking ALL external I/O
  (``pandas.read_excel``, filesystem existence checks, image resize and the
  on-disk writes). No real network or disk access happens.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``, so the module
under test can be imported directly here. Importing is safe because the
module guards execution behind ``if __name__ == "__main__"``.
"""
from datetime import datetime
from pathlib import Path

import pytest

# update_supporting_contributors imports pandas, which is not yet in
# REQUIREMENTS.txt; skip this module cleanly where pandas is unavailable
# rather than erroring at collection.
pd = pytest.importorskip("pandas")

import update_supporting_contributors as mod


# ---------------------------------------------------------------------------
# parse_date
# ---------------------------------------------------------------------------
def test_parse_date_handles_timestamp_strings_and_junk():
    # pandas Timestamp -> ISO date
    assert mod.parse_date(pd.Timestamp("2021-07-04")) == "2021-07-04"
    # M/D/YY string format
    assert mod.parse_date("7/4/21") == "2021-07-04"
    # M/D/YYYY string format
    assert mod.parse_date("12/31/2020") == "2020-12-31"
    # NaT / NaN / None / empty / unparseable all collapse to None
    assert mod.parse_date(pd.NaT) is None
    assert mod.parse_date(None) is None
    assert mod.parse_date("") is None
    assert mod.parse_date("   ") is None
    assert mod.parse_date("not a date") is None


# ---------------------------------------------------------------------------
# is_active_contributor (3-year threshold boundary)
# ---------------------------------------------------------------------------
def test_is_active_contributor_threshold_boundary():
    # No end date -> still active
    assert mod.is_active_contributor("") is True
    assert mod.is_active_contributor(None) is True

    today = datetime.now()
    # Recently ended -> active
    recent = today.strftime("%Y-%m-%d")
    assert mod.is_active_contributor(recent) is True

    # Well over 3 years ago -> inactive
    old = today.replace(year=today.year - 5).strftime("%Y-%m-%d")
    assert mod.is_active_contributor(old) is False

    # Unparseable end date -> assume active (defensive default)
    assert mod.is_active_contributor("garbage") is True


# ---------------------------------------------------------------------------
# parse_roles
# ---------------------------------------------------------------------------
def test_parse_roles_splits_and_cleans():
    assert mod.parse_roles("Coding, Translation , Documentation") == [
        "Coding",
        "Translation",
        "Documentation",
    ]
    # Empty / whitespace -> empty list, stray commas dropped
    assert mod.parse_roles("") == []
    assert mod.parse_roles("   ") == []
    assert mod.parse_roles("Coding,,") == ["Coding"]
    # Single item
    assert mod.parse_roles("Outreach") == ["Outreach"]


# ---------------------------------------------------------------------------
# generate_avatar_filename
# ---------------------------------------------------------------------------
def test_generate_avatar_filename_slugifies_name():
    assert (
        mod.generate_avatar_filename("Jane M. Doe", is_org=False)
        == "/img/contributors/supporting/jane_m_doe.png"
    )
    # ASCII special characters stripped, spaces -> underscores, dots removed
    assert (
        mod.generate_avatar_filename("Acme Org! (Inc.)", is_org=True)
        == "/img/contributors/supporting/acme_org_inc.png"
    )


# ---------------------------------------------------------------------------
# Helpers for the full-pipeline integration tests
# ---------------------------------------------------------------------------
def _patch_pipeline(monkeypatch, df, existing=None, image_exists=True):
    """Wire up mocks for all external I/O and capture JSON writes.

    Returns a dict mapping str(output_path) -> data passed to ``json.dump``.
    """
    # No real Excel read.
    monkeypatch.setattr(mod.pd, "read_excel", lambda path: df)
    # No real image resizing.
    monkeypatch.setattr(mod, "resize_image", lambda *a, **k: None)
    # Control whether an avatar image is found on disk, and whether an
    # existing supporting.json is present (so json.load is exercised).
    def fake_exists(path):
        # The output JSON existence check happens first in the function; we
        # only want avatar images to (optionally) exist.
        spath = str(path)
        if spath.endswith("supporting.json"):
            return existing is not None
        if "img/contributors/supporting" in spath.replace("\\", "/"):
            return image_exists
        return False

    monkeypatch.setattr(mod.os.path, "exists", fake_exists)

    # Avoid touching the real filesystem when ensuring the geojson dir.
    monkeypatch.setattr(Path, "mkdir", lambda self, *a, **k: None)

    # Capture json.dump targets keyed by the file's name. We monkeypatch the
    # module's ``open`` to hand back a sentinel object carrying the path, and
    # ``json.dump`` to record (path, data) instead of writing.
    captured = {}

    class FakeFile:
        def __init__(self, path):
            self.path = path

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        # Support json.load reading existing contributors.
        def read(self):
            return ""

    def fake_open(path, mode="r", *a, **k):
        return FakeFile(str(path))

    def fake_json_dump(data, fp, *a, **k):
        captured[str(fp.path)] = data

    def fake_json_load(fp):
        return existing if existing is not None else []

    monkeypatch.setattr(mod, "open", fake_open, raising=False)
    monkeypatch.setattr(mod.json, "dump", fake_json_dump)
    monkeypatch.setattr(mod.json, "load", fake_json_load)

    return captured


def _outputs(captured):
    """Split captured writes into (supporting_json, geojson)."""
    supporting = next(v for k, v in captured.items() if k.endswith("supporting.json"))
    geojson = next(v for k, v in captured.items() if "map" in k.lower())
    return supporting, geojson


# ---------------------------------------------------------------------------
# xlsx_to_supporting_json: empty input
# ---------------------------------------------------------------------------
def test_pipeline_empty_input_writes_empty_collections(monkeypatch):
    df = pd.DataFrame(
        columns=[
            "Approved (yes/no)",
            "Individual or Organisation",
            "Name",
            "Organization Name",
            "Email Address",
        ]
    )
    captured = _patch_pipeline(monkeypatch, df)

    mod.xlsx_to_supporting_json(
        Path("in.xlsx"),
        Path("data/contributors/supporting.json"),
        Path("static/data/contributors/supporting_map.json"),
    )

    supporting, geojson = _outputs(captured)
    assert supporting == []
    assert geojson == {"type": "FeatureCollection", "features": []}


# ---------------------------------------------------------------------------
# xlsx_to_supporting_json: single approved entry, full transform + GeoJSON
# ---------------------------------------------------------------------------
def test_pipeline_single_approved_entry_full_shape(monkeypatch):
    df = pd.DataFrame(
        [
            {
                "Approved (yes/no)": "Yes",
                "Individual or Organisation": "Individual",
                "Name": "Jane Doe",
                "Organization Name": "",
                "Email Address": "jane@example.com",
                "Type of activities": "Coding, Translation",
                "Description of contribution": "Wrote lots of code",
                "Website/Profile link": "https://example.com",
                "Location - Longitude": 12.5,
                "Location - Latitude": 41.9,
                "Please enter the start date of your activities with the QGIS community": pd.Timestamp(
                    "2019-01-01"
                ),
                "Please enter the end date of your activities with the QGIS community": "",
            }
        ]
    )
    captured = _patch_pipeline(monkeypatch, df, image_exists=True)

    mod.xlsx_to_supporting_json(
        Path("in.xlsx"),
        Path("data/contributors/supporting.json"),
        Path("static/data/contributors/supporting_map.json"),
    )

    supporting, geojson = _outputs(captured)
    assert len(supporting) == 1
    entry = supporting[0]
    assert entry["name"] == "Jane Doe"
    assert entry["is_organization"] is False
    assert entry["is_active"] is True  # no end date -> active
    assert entry["avatar_img"] == "/img/contributors/supporting/jane_doe.png"
    assert entry["link"] == "https://example.com"
    assert entry["roles"] == ["Coding", "Translation"]
    assert entry["contribution_description"] == "Wrote lots of code"
    assert entry["start_date"] == "2019-01-01"
    assert entry["end_date"] is None

    # GeoJSON feature mirrors the contributor and carries the coordinates.
    assert len(geojson["features"]) == 1
    feature = geojson["features"][0]
    assert feature["type"] == "Feature"
    assert feature["geometry"] == {"type": "Point", "coordinates": [12.5, 41.9]}
    assert feature["properties"]["name"] == "Jane Doe"


# ---------------------------------------------------------------------------
# xlsx_to_supporting_json: filtering, missing image skip, sorting
# ---------------------------------------------------------------------------
def test_pipeline_filters_rejects_skips_missing_image_and_sorts(monkeypatch):
    df = pd.DataFrame(
        [
            # Approved, newer start date -> should sort AFTER the 2015 entry.
            {
                "Approved (yes/no)": "yes",
                "Individual or Organisation": "Organisation",
                "Name": "",
                "Organization Name": "Beta Org",
                "Email Address": "beta@example.com",
                "Type of activities": "Funding",
                "Description of contribution": "Sponsorship",
                "Website/Profile link": "",
                "Location - Longitude": "",
                "Location - Latitude": "",
                "Please enter the start date of your activities with the QGIS community": "1/1/20",
                "Please enter the end date of your activities with the QGIS community": "",
            },
            # Approved, older start date -> should sort FIRST.
            {
                "Approved (yes/no)": "Yes",
                "Individual or Organisation": "Individual",
                "Name": "Alpha Person",
                "Organization Name": "",
                "Email Address": "alpha@example.com",
                "Type of activities": "Coding",
                "Description of contribution": "Early contributor",
                "Website/Profile link": "",
                "Location - Longitude": "",
                "Location - Latitude": "",
                "Please enter the start date of your activities with the QGIS community": "1/1/15",
                "Please enter the end date of your activities with the QGIS community": "",
            },
            # Rejected -> excluded from output entirely.
            {
                "Approved (yes/no)": "No",
                "Individual or Organisation": "Individual",
                "Name": "Rejected Ron",
                "Organization Name": "",
                "Email Address": "ron@example.com",
                "Type of activities": "Coding",
                "Description of contribution": "Nope",
                "Website/Profile link": "",
                "Location - Longitude": "",
                "Location - Latitude": "",
                "Please enter the start date of your activities with the QGIS community": "1/1/18",
                "Please enter the end date of your activities with the QGIS community": "",
            },
            # No name -> skipped silently.
            {
                "Approved (yes/no)": "Yes",
                "Individual or Organisation": "Individual",
                "Name": "",
                "Organization Name": "",
                "Email Address": "ghost@example.com",
                "Type of activities": "Coding",
                "Description of contribution": "",
                "Website/Profile link": "",
                "Location - Longitude": "",
                "Location - Latitude": "",
                "Please enter the start date of your activities with the QGIS community": "1/1/10",
                "Please enter the end date of your activities with the QGIS community": "",
            },
        ]
    )
    captured = _patch_pipeline(monkeypatch, df, image_exists=True)

    mod.xlsx_to_supporting_json(
        Path("in.xlsx"),
        Path("data/contributors/supporting.json"),
        Path("static/data/contributors/supporting_map.json"),
    )

    supporting, geojson = _outputs(captured)
    names = [c["name"] for c in supporting]
    # Rejected + no-name entries excluded; only the two approved remain.
    assert names == ["Alpha Person", "Beta Org"]  # sorted by start_date asc
    # Org name fallback was used and org flag set.
    beta = supporting[1]
    assert beta["is_organization"] is True
    assert beta["start_date"] == "2020-01-01"
    # No coordinates supplied -> no GeoJSON features.
    assert geojson["features"] == []


# ---------------------------------------------------------------------------
# xlsx_to_supporting_json: approved entry whose avatar image is missing
# ---------------------------------------------------------------------------
def test_pipeline_skips_approved_entry_without_image(monkeypatch):
    df = pd.DataFrame(
        [
            {
                "Approved (yes/no)": "Yes",
                "Individual or Organisation": "Individual",
                "Name": "No Image Person",
                "Organization Name": "",
                "Email Address": "noimg@example.com",
                "Type of activities": "Coding",
                "Description of contribution": "Has no avatar",
                "Website/Profile link": "",
                "Location - Longitude": 1.0,
                "Location - Latitude": 2.0,
                "Please enter the start date of your activities with the QGIS community": "1/1/22",
                "Please enter the end date of your activities with the QGIS community": "",
            }
        ]
    )
    # image_exists=False -> the entry should be skipped, leaving empty output.
    captured = _patch_pipeline(monkeypatch, df, image_exists=False)

    mod.xlsx_to_supporting_json(
        Path("in.xlsx"),
        Path("data/contributors/supporting.json"),
        Path("static/data/contributors/supporting_map.json"),
    )

    supporting, geojson = _outputs(captured)
    assert supporting == []
    # Even though coordinates were present, the skipped entry adds no feature.
    assert geojson["features"] == []
