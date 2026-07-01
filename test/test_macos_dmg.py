# -*- coding: utf-8 -*-
"""Regression tests for scripts/macos_dmg.py.

update-schedule.py used to build the macOS .dmg download URLs straight from the
release-schedule version, so when a version was announced before its macOS
build was uploaded the download button 404'd (issue #1000). latest_available_dmg
resolves the version against the actual S3 listing instead.
"""
import macos_dmg


def _listing(channel, names):
    """Build a minimal s3_downloads.json-shaped tree for one macos channel."""
    return {
        "tree": {
            "children": [
                {
                    "name": "macos",
                    "children": [
                        {"name": channel, "files": [{"name": n} for n in names]},
                    ],
                }
            ]
        }
    }


def test_falls_back_to_latest_available_patch_when_exact_missing():
    listing = _listing("ltr", ["qgis_ltr_final-3_44_9.dmg", "qgis_ltr_final-3_44_10.dmg"])
    # 3.44.11 announced but not uploaded yet -> use newest available 3.44.10.
    assert macos_dmg.latest_available_dmg("3.44.11", "ltr", listing) == "3.44.10"


def test_returns_exact_version_when_present():
    listing = _listing("pr", ["qgis_pr_final-4_0_2.dmg", "qgis_pr_final-4_0_3.dmg"])
    assert macos_dmg.latest_available_dmg("4.0.3", "pr", listing) == "4.0.3"


def test_returns_requested_when_series_absent():
    listing = _listing("ltr", ["qgis_ltr_final-3_40_5.dmg"])
    # Nothing for the 3.44 series at all -> unchanged (no worse than before).
    assert macos_dmg.latest_available_dmg("3.44.11", "ltr", listing) == "3.44.11"


def test_ignores_non_dmg_and_foreign_prefixes():
    listing = _listing(
        "ltr",
        [
            "qgis_ltr_final-3_44_10.dmg",
            "qgis_ltr_final-3_44_11.log",   # not a .dmg
            "QGIS-final-3_44_12.dmg",       # different prefix -> ignore
        ],
    )
    assert macos_dmg.latest_available_dmg("3.44.11", "ltr", listing) == "3.44.10"


def test_handles_date_suffixed_dmg_names():
    listing = _listing("ltr", ["qgis_ltr_final-3_22_10_20220815_145618.dmg"])
    assert macos_dmg.latest_available_dmg("3.22.11", "ltr", listing) == "3.22.10"


def test_available_dmg_versions_maps_all_dmgs():
    listing = _listing("pr", ["qgis_pr_final-4_0_3.dmg", "qgis_pr_final-4_0_2.dmg"])
    assert macos_dmg.available_dmg_versions(listing, "pr") == {
        (4, 0, 3): "4.0.3",
        (4, 0, 2): "4.0.2",
    }


def test_unparseable_version_returned_unchanged():
    listing = _listing("ltr", ["qgis_ltr_final-3_44_10.dmg"])
    assert macos_dmg.latest_available_dmg("nightly", "ltr", listing) == "nightly"
