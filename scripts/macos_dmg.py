#!/usr/bin/env python3
"""Resolve macOS .dmg download versions against the actual S3 listing.

The release schedule spreadsheet can name a version whose macOS build has not
been uploaded to S3 yet, which produces a download link that 404s (issue
#1000). These helpers look up what is actually present in the generated
data/downloads/s3_downloads.json listing and pick the newest build that really
exists for a release series, so the download button always points at a file
that can be fetched.
"""
import re

# e.g. qgis_ltr_final-3_44_10.dmg -> ("3", "44", "10"). Older files carry a
# build-date suffix (qgis_ltr_final-3_22_10_20220815_145618.dmg), so allow a
# trailing "_..." after the major_minor_patch part.
_DMG_RE = re.compile(r"^qgis_(?:ltr|pr)_final-(\d+)_(\d+)_(\d+)(?:_.*)?\.dmg$")


def _iter_channel_files(s3_listing, channel):
    """Yield the file entries under macos/<channel> in the S3 listing tree."""
    tree = s3_listing.get("tree", {})
    for macos in tree.get("children", []):
        if macos.get("name") != "macos":
            continue
        for sub in macos.get("children", []):
            if sub.get("name") == channel:
                yield from sub.get("files", [])


def available_dmg_versions(s3_listing, channel):
    """Map (major, minor, patch) -> dotted version for every .dmg in a channel.

    channel is "ltr" or "pr" (the macOS subfolders on S3).
    """
    versions = {}
    for entry in _iter_channel_files(s3_listing, channel):
        match = _DMG_RE.match(entry.get("name", ""))
        if match:
            versions[tuple(int(p) for p in match.groups())] = ".".join(match.groups())
    return versions


def latest_available_dmg(requested_version, channel, s3_listing):
    """Return the dotted version whose .dmg actually exists on S3.

    Prefer the exact requested version; if its build has not been uploaded yet,
    fall back to the newest patch available in the same major.minor series. If
    the listing has nothing for that series (or the version cannot be parsed),
    return the requested version unchanged so behaviour is no worse than before.
    """
    try:
        requested = tuple(int(p) for p in requested_version.split("."))
    except (AttributeError, ValueError):
        return requested_version

    available = available_dmg_versions(s3_listing, channel)
    if requested in available:
        return requested_version

    same_series = [v for v in available if v[:2] == requested[:2]]
    if same_series:
        return available[max(same_series)]
    return requested_version
