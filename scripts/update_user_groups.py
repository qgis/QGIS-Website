#!/usr/bin/env python3
"""
Build the QGIS local user groups data from the file people edit.

data/user_groups/groups.json is the only file people edit. It holds one small entry
per group (name, country code, website, year, contacts, logo link). This
script turns it into everything the website needs:

* static/data/user_groups/user_groups.json, the GeoJSON the list and the
  map read, with each group's id, country name, continent, map point and logo
  filled in. It is published at /data/user_groups/user_groups.json so
  anyone can reuse it;
* data/user_groups/logos.json, the link each logo was downloaded from, so an
  unchanged logo is not downloaded again. Not published;
* data/user_groups/countries.json, the outlines of the countries that host a
  group, from Natural Earth (public domain). Hugo embeds it in the map page,
  it is not published as a file;
* static/img/user-groups/<id>.webp, each group's logo, downloaded from its
  logo link or taken from user-groups-logos/<id>.<png|jpg|gif|webp>, checked
  and re-encoded as WebP.

Usage:
    python scripts/update_user_groups.py           # build and write everything
    python scripts/update_user_groups.py --check   # validate only, write nothing

The pull request workflow runs --check. The workflow on main runs the build
and commits the result, so editors never need to run this themselves.
"""

import argparse
import hashlib
import json
import math
import os
import re
import sys
import tempfile
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

import requests

from resize_image import LogoError, fetch_image_bytes, normalize_logo

ROOT = Path(__file__).resolve().parent.parent
SOURCE_PATH = ROOT / "data" / "user_groups" / "groups.json"
GENERATED_PATH = ROOT / "static" / "data" / "user_groups" / "user_groups.json"
COUNTRIES_PATH = ROOT / "data" / "user_groups" / "countries.json"
LOGO_SOURCES_PATH = ROOT / "data" / "user_groups" / "logos.json"
STATIC_DIR = ROOT / "static"
LOGO_DIR = STATIC_DIR / "img" / "user-groups"
LOGO_PUBLIC_PATH = "img/user-groups"  # where LOGO_DIR is served, relative to the site root
UPLOAD_DIR = ROOT / "user-groups-logos"
UPLOAD_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp")

NE_COMMIT = "ca96624a56bd078437bca8184e78163e5039ad19"
NE_URL = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/"
    f"{NE_COMMIT}/geojson/ne_50m_admin_0_countries.geojson"
)
NE_SHA256 = "3e458fc036ad0a66411f2c1e6cac49c5d7bfb81cb1123bc513b22511a2b7fdeb"

CONTINENTS = {"africa", "asia", "europe", "north-america", "south-america", "oceania", "global"}

TOP_LEVEL_KEYS = {"_how_to_edit", "groups"}
REQUIRED_FIELDS = ("name", "country", "year", "contacts")
OPTIONAL_FIELDS = ("id", "website", "logo_url", "removed", "country_name")
FIRST_YEAR = 2000
MAX_TEXT = 120
MAX_URL = 500
MAX_CONTACTS = 10
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
COUNTRY_PATTERN = re.compile(r"^[A-Z]{2}$")

COUNTRIES_WARNING = {
    "generated_by": "scripts/update_user_groups.py",
    "warning": "This file is generated. Do NOT edit it by hand. Edit data/user_groups/groups.json instead.",
    "source": NE_URL,
    "licence": "Natural Earth, public domain",
}

# ~3 km at the equator: plenty for a world map, keeps the file under 300 KB.
SIMPLIFY_TOLERANCE = 0.03
COORD_DECIMALS = 3


# ---------------------------------------------------------------------------
# Source file: validation and ids
# ---------------------------------------------------------------------------
def slugify(text):
    """'QGIS México' -> 'qgis-mexico'."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def group_id(entry):
    name = entry.get("name")
    return entry.get("id") or slugify(name if isinstance(name, str) else "")


def _label(entry, index):
    name = entry.get("name") if isinstance(entry, dict) else None
    return f"Group {index + 1} ({name})" if isinstance(name, str) and name.strip() else f"Group {index + 1}"


def _valid_url(value):
    if not isinstance(value, str) or len(value) > MAX_URL:
        return False
    parts = urlsplit(value)
    return parts.scheme in ("http", "https") and bool(parts.netloc) and not (parts.username or parts.password)


def _short_text(value):
    return isinstance(value, str) and value.strip() != "" and len(value) <= MAX_TEXT


def validate_source(source, this_year=None):
    """Return a list of problems, each written for the person editing the file."""
    this_year = this_year or date.today().year
    if not isinstance(source, dict) or not isinstance(source.get("groups"), list):
        return ['The file must contain a "groups" list.']
    errors = [f'Unknown top level field "{key}".' for key in sorted(set(source) - TOP_LEVEL_KEYS)]
    if not source["groups"]:
        errors.append('The "groups" list is empty.')

    seen = {}
    for index, entry in enumerate(source["groups"]):
        label = _label(entry, index)
        if not isinstance(entry, dict):
            errors.append(f"{label}: each group must be written between {{ and }}.")
            continue

        unknown = sorted(set(entry) - set(REQUIRED_FIELDS) - set(OPTIONAL_FIELDS))
        for key in unknown:
            errors.append(f'{label}: unknown field "{key}". Check the spelling.')
        missing = [key for key in REQUIRED_FIELDS if key not in entry]
        for key in missing:
            errors.append(f'{label}: the "{key}" field is missing.')

        if "name" in entry and not _short_text(entry["name"]):
            errors.append(f"{label}: the name must be text of at most {MAX_TEXT} characters.")

        if "id" in entry and not (isinstance(entry["id"], str) and ID_PATTERN.match(entry["id"]) and len(entry["id"]) <= 60):
            errors.append(f'{label}: the id may only use lower case letters, digits and single hyphens, for example "qgis-kenya".')

        if "country" in entry:
            country = entry["country"]
            if country is not None and not (isinstance(country, str) and COUNTRY_PATTERN.match(country)):
                errors.append(f'{label}: the country must be a two letter code in capitals, for example "KE", or null for a worldwide group.')

        if "country_name" in entry and not _short_text(entry["country_name"]):
            errors.append(f"{label}: the country name must be text of at most {MAX_TEXT} characters.")

        year = entry.get("year")
        if "year" in entry and not (isinstance(year, int) and not isinstance(year, bool) and FIRST_YEAR <= year <= this_year):
            errors.append(f"{label}: the year must be a number between {FIRST_YEAR} and {this_year}, without quotes.")

        if "contacts" in entry:
            contacts = entry["contacts"]
            if not (isinstance(contacts, list) and 1 <= len(contacts) <= MAX_CONTACTS and all(_short_text(c) for c in contacts)):
                errors.append(f'{label}: contacts must be a list of one to {MAX_CONTACTS} names, for example ["Ana Silva"].')

        for key in ("website", "logo_url"):
            if entry.get(key) is not None and not _valid_url(entry[key]):
                errors.append(f"{label}: the {key.replace('_', ' ')} must be a full link starting with https:// or http://.")

        removed = entry.get("removed")
        if removed is not None:
            if not (isinstance(removed, int) and not isinstance(removed, bool) and FIRST_YEAR <= removed <= this_year):
                errors.append(f"{label}: removed must be the year the group stopped, or null.")
            elif isinstance(year, int) and removed < year:
                errors.append(f"{label}: the group cannot stop before the year it started.")

        if "name" in entry or "id" in entry:
            gid = group_id(entry)
            if not gid:
                errors.append(f"{label}: add an id, because the name gives no usable one.")
            elif gid in seen:
                errors.append(f'{label}: the id "{gid}" is already used by {seen[gid]}. Add a different "id".')
            else:
                seen[gid] = label
    return errors


def source_country_codes(source):
    return sorted({g["country"] for g in source["groups"] if g.get("country")})


# ---------------------------------------------------------------------------
# Geometry
# ---------------------------------------------------------------------------
def _perpendicular_distance(point, start, end):
    if start == end:
        return math.dist(point, start)
    (x, y), (x1, y1), (x2, y2) = point, start, end
    return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.dist(start, end)


def simplify_line(points, tolerance):
    """Douglas Peucker simplification (iterative, no recursion limit)."""
    if len(points) < 3:
        return list(points)
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        first, last = stack.pop()
        max_dist, index = 0.0, None
        for i in range(first + 1, last):
            dist = _perpendicular_distance(points[i], points[first], points[last])
            if dist > max_dist:
                max_dist, index = dist, i
        if index is not None and max_dist > tolerance:
            keep[index] = True
            stack.append((first, index))
            stack.append((index, last))
    return [p for p, k in zip(points, keep) if k]


def simplify_ring(ring, tolerance, decimals=COORD_DECIMALS):
    """Simplify a closed ring. Returns None when it collapses below a triangle."""
    simplified = simplify_line([tuple(p[:2]) for p in ring], tolerance)
    rounded = []
    for x, y in simplified:
        point = [round(x, decimals), round(y, decimals)]
        if not rounded or rounded[-1] != point:
            rounded.append(point)
    if rounded[0] != rounded[-1]:
        rounded.append(rounded[0])
    return rounded if len(rounded) >= 4 else None


def simplify_geometry(geometry, tolerance=SIMPLIFY_TOLERANCE):
    """Simplify a Polygon or MultiPolygon. Always returns a MultiPolygon."""
    if geometry["type"] == "Polygon":
        polygons = [geometry["coordinates"]]
    elif geometry["type"] == "MultiPolygon":
        polygons = geometry["coordinates"]
    else:
        raise ValueError(f"unsupported geometry type {geometry['type']}")

    out = []
    for polygon in polygons:
        outer = simplify_ring(polygon[0], tolerance)
        if outer is None:
            continue  # islands smaller than the tolerance disappear
        holes = [h for h in (simplify_ring(r, tolerance) for r in polygon[1:]) if h]
        out.append([outer, *holes])
    return {"type": "MultiPolygon", "coordinates": out}


# ---------------------------------------------------------------------------
# Natural Earth: outlines, names, continents, label points
# ---------------------------------------------------------------------------
def select_countries(natural_earth, codes):
    """Map each ISO code to its Natural Earth feature.

    An exact ISO_A2 match wins. ISO_A2_EH is the fallback because Natural
    Earth sets ISO_A2 to -99 for France, Norway and Kosovo, and reuses
    ISO_A2_EH for overseas territories (Australia's islands, for example).
    """
    by_iso, by_iso_eh = {}, {}
    for feature in natural_earth["features"]:
        props = feature["properties"]
        by_iso.setdefault(props.get("ISO_A2"), feature)
        by_iso_eh.setdefault(props.get("ISO_A2_EH"), feature)
    selected, missing = {}, []
    for code in codes:
        feature = by_iso.get(code) or by_iso_eh.get(code)
        if feature is None:
            missing.append(code)
        else:
            selected[code] = feature
    return selected, missing


def label_point(ne_feature, decimals=COORD_DECIMALS):
    """Natural Earth's label point: on the surface of the main landmass.

    Unlike a centroid it never falls in the sea or on an overseas territory.
    """
    props = ne_feature["properties"]
    return [round(props["LABEL_X"], decimals), round(props["LABEL_Y"], decimals)]


def continent_slug(ne_continent):
    return (ne_continent or "").lower().replace(" ", "-")


def build_countries_geojson(natural_earth, codes, tolerance=SIMPLIFY_TOLERANCE):
    selected, missing = select_countries(natural_earth, codes)
    features = [
        {
            "type": "Feature",
            "properties": {
                "iso_a2": code,
                "name": feature["properties"].get("NAME_LONG") or feature["properties"].get("NAME"),
                "continent": continent_slug(feature["properties"].get("CONTINENT")),
                "label": label_point(feature),
            },
            "geometry": simplify_geometry(feature["geometry"], tolerance),
        }
        for code, feature in sorted(selected.items())
    ]
    collection = {
        "type": "FeatureCollection",
        "_automated_warning": dict(COUNTRIES_WARNING),
        "features": features,
    }
    return collection, missing


def countries_are_current(countries, codes):
    """True when the outlines file holds exactly these countries, with every
    derived field and the current header."""
    if not countries or countries.get("_automated_warning") != COUNTRIES_WARNING:
        return False
    props = [f["properties"] for f in countries.get("features", [])]
    if any(not {"iso_a2", "name", "continent", "label"} <= set(p) for p in props):
        return False
    return sorted(p["iso_a2"] for p in props) == codes


def load_natural_earth(source=None):
    if source:
        raw = Path(source).read_bytes()
    else:
        response = requests.get(NE_URL, timeout=60)
        response.raise_for_status()
        raw = response.content
        digest = hashlib.sha256(raw).hexdigest()
        if digest != NE_SHA256:
            raise ValueError(f"Natural Earth checksum mismatch: {digest}")
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Logos
# ---------------------------------------------------------------------------
def find_upload(gid, upload_dir):
    for ext in UPLOAD_EXTENSIONS:
        for candidate in (Path(upload_dir) / f"{gid}{ext}", Path(upload_dir) / f"{gid}{ext.upper()}"):
            if candidate.is_file():
                return candidate
    return None


def resolve_logos(source, previous_sources, logo_dir, upload_dir, write, preview_dir=None, fetch=None):
    """Work out each group's logo.

    Order: an uploaded file, then the logo link (downloaded only when it is
    new or changed), then the logo already on disk. With write=False nothing
    in the repository changes: new logos go to preview_dir instead.

    previous_sources maps each id to the link its logo on disk came from.

    Returns (logos, report, problems):
      logos    {id: {"logo": path under static/ or None, "logo_source": url or None}}
      report   [(id, status)] for logos that were added or changed
      problems [(id, message)] for logos that could not be used
    """
    fetch = fetch or fetch_image_bytes
    logo_dir, upload_dir = Path(logo_dir), Path(upload_dir)
    previous_sources = previous_sources or {}
    logos, report, problems = {}, [], []
    if not write:
        preview_dir = Path(preview_dir or tempfile.mkdtemp(prefix="user-group-logos-"))

    for entry in source["groups"]:
        gid = group_id(entry)
        final = logo_dir / f"{gid}.webp"
        target = final if write else preview_dir / f"{gid}.webp"
        logo_rel = f"{LOGO_PUBLIC_PATH}/{gid}.webp"
        url = entry.get("logo_url")
        prev_url = previous_sources.get(gid)
        kept = {"logo": logo_rel, "logo_source": prev_url} if final.is_file() else {"logo": None, "logo_source": None}

        upload = find_upload(gid, upload_dir)
        if upload:
            try:
                normalize_logo(upload.read_bytes(), target)
                logos[gid] = {"logo": logo_rel, "logo_source": None}
                report.append((gid, f"uploaded file {upload.name} converted"))
                if write:
                    upload.unlink()
            except LogoError as error:
                problems.append((gid, f"{upload.name}: {error}"))
                logos[gid] = kept
            continue

        if url and not (final.is_file() and prev_url == url):
            try:
                normalize_logo(fetch(url), target)
                logos[gid] = {"logo": logo_rel, "logo_source": url}
                report.append((gid, "logo downloaded and converted"))
            except LogoError as error:
                problems.append((gid, str(error)))
                logos[gid] = kept
            continue

        logos[gid] = kept
    return logos, report, problems


def unmatched_uploads(source, upload_dir):
    """Files in the upload folder that no group will pick up."""
    ids = {group_id(g) for g in source["groups"]}
    problems = []
    for path in sorted(Path(upload_dir).glob("*")):
        if not path.is_file() or path.name == "README.md":
            continue
        if path.suffix.lower() not in UPLOAD_EXTENSIONS:
            problems.append((path.name, "only PNG, JPEG, GIF or WebP files can be uploaded."))
        elif path.stem not in ids:
            problems.append((path.name, "no group has this id. Name the file after the group's id, for example qgis-kenya.png."))
    return problems


def remove_orphan_logos(source, logo_dir):
    """Delete logos of groups that are no longer in the file."""
    ids = {group_id(g) for g in source["groups"]}
    removed = []
    for path in sorted(Path(logo_dir).glob("*.webp")):
        if path.stem not in ids:
            path.unlink()
            removed.append(path.name)
    return removed


# ---------------------------------------------------------------------------
# Generated GeoJSON
# ---------------------------------------------------------------------------
def build_generated(source, countries, logos):
    by_code = {f["properties"]["iso_a2"]: f["properties"] for f in countries["features"]}
    features = []
    for entry in source["groups"]:
        gid = group_id(entry)
        code = entry.get("country")
        country = by_code.get(code, {}) if code else {}
        logo = logos.get(gid, {"logo": None})
        features.append({
            "type": "Feature",
            "properties": {
                "slug": gid,
                "name": entry["name"],
                "country": code,
                "country_name": entry.get("country_name") or country.get("name"),
                "continent": country.get("continent") if code else "global",
                "website": entry.get("website"),
                "year": entry["year"],
                "contacts": entry["contacts"],
                "active": entry.get("removed") is None,
                "removed": entry.get("removed"),
                "logo": logo["logo"],
            },
            "geometry": {"type": "Point", "coordinates": country["label"]} if code else None,
        })
    return {
        "type": "FeatureCollection",
        "name": "qgis_user_groups",
        "_automated_warning": {
            "generated_by": "scripts/update_user_groups.py",
            "warning": "This file is generated. Do NOT edit it by hand. Edit data/user_groups/groups.json instead.",
        },
        "features": features,
    }


def build_logo_sources(logos):
    """The link each logo on disk came from, keyed by id. Uploads have none."""
    return {
        "_automated_warning": {
            "generated_by": "scripts/update_user_groups.py",
            "warning": "This file is generated. Do NOT edit it by hand. It records the link each logo was downloaded from, so unchanged logos are not downloaded again.",
        },
        "sources": {gid: logo["logo_source"] for gid, logo in sorted(logos.items()) if logo.get("logo_source")},
    }


def check_continents(generated):
    return [
        f'{f["properties"]["slug"]}: Natural Earth gives no known continent for {f["properties"]["country"]}.'
        for f in generated["features"]
        if f["properties"]["continent"] not in CONTINENTS
    ]


def to_json(data, compact=False):
    if compact:
        return json.dumps(data, separators=(",", ":")) + "\n"
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def changed_groups(previous, generated):
    """[(id, what)] describing the difference between two generated files."""
    before = {f["properties"]["slug"]: f for f in (previous or {}).get("features", [])}
    after = {f["properties"]["slug"]: f for f in generated["features"]}
    changes = []
    for gid in after:
        if gid not in before:
            changes.append((gid, "new group"))
        elif before[gid] != after[gid]:
            old, new = before[gid]["properties"], after[gid]["properties"]
            fields = sorted(k for k in set(old) | set(new) if old.get(k) != new.get(k))
            if before[gid].get("geometry") != after[gid].get("geometry"):
                fields.append("map point")
            changes.append((gid, "changed: " + ", ".join(fields)))
    changes += [(gid, "removed from the file") for gid in before if gid not in after]
    return changes


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def _logo_column(gid, logo_report, logo_problems, generated):
    if gid in dict(logo_problems):
        return "not used, see above"
    if gid in dict(logo_report):
        return dict(logo_report)[gid]
    props = next((f["properties"] for f in (generated or {}).get("features", []) if f["properties"]["slug"] == gid), {})
    return "unchanged" if props.get("logo") else "none, the QGIS logo is shown"


def write_report(title, errors, changes, logo_report, logo_problems, summary_path=None, generated=None):
    """Print a report, and write it as Markdown to the GitHub job summary."""
    lines = [f"## {title}", ""]
    if errors:
        lines += ["**Please fix these problems in `data/user_groups/groups.json`:**", ""]
        lines += [f"- {e}" for e in errors] + [""]
    if logo_problems:
        lines += ["**These logos could not be used:**", ""]
        lines += [f"- `{gid}`: {message}" for gid, message in logo_problems] + [""]
    if changes or logo_report:
        lines += ["| Group | Change | Logo |", "|---|---|---|"]
        ids = list(dict.fromkeys([gid for gid, _ in changes] + [gid for gid, _ in logo_report]))
        what = dict(changes)
        for gid in ids:
            logo = _logo_column(gid, logo_report, logo_problems, generated)
            lines.append(f"| `{gid}` | {what.get(gid, 'logo only')} | {logo} |")
        lines.append("")
    if not (errors or logo_problems or changes or logo_report):
        lines += ["Nothing to change.", ""]
    text = "\n".join(lines)
    print(text)
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(text + "\n")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        for gid, message in logo_problems:
            print(f"::warning title=User group logo ({gid})::{message}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _load_json(path):
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else None


def _write_if_changed(path, text):
    path = Path(path)
    if path.is_file() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="validate and test the logos, write nothing")
    parser.add_argument("--preview-dir", help="with --check, save converted logos here for review")
    parser.add_argument("--source", help="local Natural Earth GeoJSON instead of downloading it")
    parser.add_argument("--groups", default=str(SOURCE_PATH), help=argparse.SUPPRESS)
    parser.add_argument("--generated", default=str(GENERATED_PATH), help=argparse.SUPPRESS)
    parser.add_argument("--countries", default=str(COUNTRIES_PATH), help=argparse.SUPPRESS)
    parser.add_argument("--logo-sources", default=str(LOGO_SOURCES_PATH), help=argparse.SUPPRESS)
    parser.add_argument("--logo-dir", default=str(LOGO_DIR), help=argparse.SUPPRESS)
    parser.add_argument("--upload-dir", default=str(UPLOAD_DIR), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    title = "User groups check" if args.check else "User groups build"

    try:
        source = json.loads(Path(args.groups).read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        write_report(title, [f"The file is not valid JSON near line {error.lineno}, column {error.colno}: {error.msg}. "
                             "A missing comma or quote is the usual cause."], [], [], [], summary)
        return 1
    errors = validate_source(source)
    if errors:
        write_report(title, errors, [], [], [], summary)
        return 1

    codes = source_country_codes(source)
    countries = _load_json(args.countries)
    rebuild_countries = not countries_are_current(countries, codes)
    if rebuild_countries:
        countries, missing = build_countries_geojson(load_natural_earth(args.source), codes)
        if missing:
            write_report(title, [f'No country has the code "{code}". Use a two letter ISO 3166 code.' for code in missing],
                         [], [], [], summary)
            return 1

    previous = _load_json(args.generated)
    previous_sources = (_load_json(args.logo_sources) or {}).get("sources", {})
    logos, logo_report, logo_problems = resolve_logos(
        source, previous_sources, args.logo_dir, args.upload_dir,
        write=not args.check, preview_dir=args.preview_dir,
    )
    logo_problems += unmatched_uploads(source, args.upload_dir)
    generated = build_generated(source, countries, logos)
    errors = check_continents(generated)
    changes = changed_groups(previous, generated)
    write_report(title, errors, changes, logo_report, logo_problems, summary, generated)
    if errors:
        return 1
    if args.check:
        return 1 if logo_problems else 0

    if rebuild_countries:
        Path(args.countries).parent.mkdir(parents=True, exist_ok=True)
        Path(args.countries).write_text(to_json(countries, compact=True), encoding="utf-8")
        print(f"Wrote {len(countries['features'])} country outlines to {args.countries}")
    if _write_if_changed(args.generated, to_json(generated)):
        print(f"Wrote {len(generated['features'])} groups to {args.generated}")
    _write_if_changed(args.logo_sources, to_json(build_logo_sources(logos)))
    for name in remove_orphan_logos(source, args.logo_dir):
        print(f"Removed the logo {name}, its group is no longer in the file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
