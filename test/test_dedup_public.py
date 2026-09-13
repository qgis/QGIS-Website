# -*- coding: utf-8 -*-
"""Regression tests for scripts/dedup_public.py.

The deduplicator replaces files that are byte-identical to a base-language file
with a link to that canonical copy. It must never delete a file before the
replacement link exists, otherwise a failed link leaves the published asset
gone for good.
"""
import os
import sys

import dedup_public


def _run(public_dir, mode="symlink"):
    argv = [
        "dedup_public.py",
        "--public-dir", str(public_dir),
        "--ext", "png",
        "--mode", mode,
    ]
    old_argv = sys.argv
    sys.argv = argv
    try:
        return dedup_public.main()
    finally:
        sys.argv = old_argv


def _make_duplicate_tree(tmp_path):
    """A canonical file at the root and an identical copy under a subdir."""
    content = b"DUPLICATE-IMAGE-BYTES"
    (tmp_path / "logo.png").write_bytes(content)
    sub = tmp_path / "fr"
    sub.mkdir()
    dup = sub / "logo.png"
    dup.write_bytes(content)
    return dup, content


def test_failed_link_does_not_delete_original(tmp_path, monkeypatch):
    dup, content = _make_duplicate_tree(tmp_path)

    def boom(*args, **kwargs):
        raise OSError("simulated link failure")

    monkeypatch.setattr(dedup_public.os, "symlink", boom)

    assert _run(tmp_path) == 0
    # The duplicate must survive intact when the link could not be created.
    assert dup.is_file() and not dup.is_symlink()
    assert dup.read_bytes() == content


def test_duplicate_is_replaced_with_symlink_on_success(tmp_path):
    dup, content = _make_duplicate_tree(tmp_path)

    assert _run(tmp_path) == 0
    # On success the duplicate becomes a symlink that still resolves to the
    # original bytes, and no stale temp file is left behind.
    assert dup.is_symlink()
    assert dup.read_bytes() == content
    assert not (dup.parent / (dup.name + ".dedup-tmp")).exists()
