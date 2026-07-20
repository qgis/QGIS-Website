"""Regression tests for installation guide content."""

from pathlib import Path


def test_macports_qgis3_version_is_explicit():
    guide = Path("content/resources/installation-guide/index.md").read_text()

    assert "latest release of QGIS 3.x (port `qgis3`)" in guide
