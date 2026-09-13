# -*- coding: utf-8 -*-
"""Regression tests for scripts/match_commercial_contributors.py.

save_matches divided by the number of commercial-support orgs to print a match
rate. When that data is empty or missing the count is 0, so the script crashed
with ZeroDivisionError instead of reporting 0%.
"""
import json

import match_commercial_contributors as mcc


def _cd_into_repo_layout(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data" / "commercial_support").mkdir(parents=True)


def test_zero_orgs_reports_zero_percent_without_crashing(tmp_path, monkeypatch, capsys):
    _cd_into_repo_layout(tmp_path, monkeypatch)

    mcc.save_matches({}, 0, 0)  # empty data -> total_orgs == 0

    out = capsys.readouterr().out
    assert "Match rate: 0.0%" in out
    saved = json.loads(
        (tmp_path / "data" / "commercial_support" / "contributor_matches.json").read_text()
    )
    assert saved["matches"] == {}


def test_match_rate_computed_when_orgs_present(tmp_path, monkeypatch, capsys):
    _cd_into_repo_layout(tmp_path, monkeypatch)

    matches = {"acme": {"contributor_name": "Acme Ltd", "is_active": True}}
    mcc.save_matches(matches, 4, 3)  # 1 of 4 matched

    assert "Match rate: 25.0%" in capsys.readouterr().out
