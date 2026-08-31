# -*- coding: utf-8 -*-
"""Regression tests for scripts/optimize_changelogs.py.

For an image whose name already ends in .webp (including the harvester's
name.png.webp convention), the optimizer's target filename equals the source
filename. It used to write the optimized copy over the original and then
unconditionally delete that same path, destroying the file while index.md kept
referencing it; that is how 24 of the 30 gallery images vanished from
visualchangelog342.
"""
import pytest

pytest.importorskip("PIL")
from PIL import Image

from optimize_changelogs import ChangelogOptimizer


def _make_changelog(tmp_path, images, index_lines):
    """Build a minimal changelog dir with oversized images and an index.md."""
    entries = tmp_path / "images" / "entries"
    entries.mkdir(parents=True)
    for name in images:
        fmt = "GIF" if name.endswith(".gif") else ("WEBP" if name.endswith(".webp") else "PNG")
        # 1500x900 exceeds the 1200x800 limits, so every image needs a rescale.
        Image.new("RGB", (1500, 900), (10, 120, 200)).save(entries / name, fmt)
    (tmp_path / "index.md").write_text(
        "\n".join(f"![shot](images/entries/{name})" for name in index_lines) + "\n",
        encoding="utf-8",
    )
    return ChangelogOptimizer(tmp_path), entries


def test_webp_named_image_survives_optimization(tmp_path):
    # foo.png.webp: stem is "foo.png", so the target name equals the source
    # name. The file must be optimized in place, not deleted.
    optimizer, entries = _make_changelog(
        tmp_path, ["foo.png.webp"], ["foo.png.webp"]
    )

    missing = optimizer.process()

    assert (entries / "foo.png.webp").exists()
    assert missing == 0
    index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "images/entries/foo.png.webp" in index


def test_png_is_converted_and_reference_updated(tmp_path):
    optimizer, entries = _make_changelog(tmp_path, ["bar.png"], ["bar.png"])

    missing = optimizer.process()

    assert (entries / "bar.webp").exists()
    assert not (entries / "bar.png").exists()
    assert missing == 0
    index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "images/entries/bar.webp" in index
    assert "images/entries/bar.png)" not in index


def test_small_image_is_left_alone(tmp_path):
    optimizer, entries = _make_changelog(tmp_path, [], [])
    small = entries / "small.png"
    Image.new("RGB", (400, 300), (200, 30, 30)).save(small, "PNG")
    (tmp_path / "index.md").write_text(
        "![shot](images/entries/small.png)\n", encoding="utf-8"
    )

    missing = optimizer.process()

    assert small.exists()
    assert missing == 0


def test_missing_reference_is_reported(tmp_path):
    # index.md points at an image that does not exist: process() must report
    # it instead of finishing silently.
    optimizer, _ = _make_changelog(tmp_path, [], ["ghost.webp"])

    assert optimizer.process() == 1


def test_no_stray_tmp_files_left_behind(tmp_path):
    optimizer, entries = _make_changelog(
        tmp_path, ["a.png", "b.png.webp"], ["a.png", "b.png.webp"]
    )

    optimizer.process()

    assert not list(entries.glob("*.tmp"))
