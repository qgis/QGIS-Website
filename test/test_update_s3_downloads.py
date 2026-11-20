"""Regression tests for S3 download path de-duplication."""

import update_s3_downloads as mod


def _file(key, path):
    return {"key": key, "name": key.rsplit("/", 1)[-1], "path": path}


def test_windows_copy_uses_root_download_key_for_same_named_root_file():
    filename = "QGIS-OSGeo4W-4.2.3-1.msi"
    root_copy = _file(filename, "")
    windows_copy = _file(f"windows/{filename}", "windows")
    other_file = _file("windows/readme.txt", "windows")

    explorer = mod.S3FileExplorer.__new__(mod.S3FileExplorer)

    expected_windows_copy = {**windows_copy, "key": filename}
    assert explorer.deduplicate_files([root_copy, windows_copy, other_file]) == [
        expected_windows_copy,
        other_file,
    ]


def test_same_name_in_unrelated_directory_is_not_deduplicated():
    filename = "manifest.json"
    root_copy = _file(filename, "")
    macos_copy = _file(f"macOS/{filename}", "macOS")

    explorer = mod.S3FileExplorer.__new__(mod.S3FileExplorer)

    assert explorer.deduplicate_files([root_copy, macos_copy]) == [
        root_copy,
        macos_copy,
    ]
