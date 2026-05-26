#!/usr/bin/env bash
# -*- mode: python -*-
# This polyglot trick lets us run inside nix develop automatically
''':'
exec nix --extra-experimental-features "nix-command flakes" develop --command python3 "$0" "$@"
'''

"""
OSGeo Content Harvester
=======================

Crawls osgeo.org via its sitemap, converts HTML content to Hugo-compatible
markdown, and upserts it into the local content/ directory.

Features:
  - Sitemap-based discovery (page-sitemap.xml)
  - HTML-to-markdown conversion via html2text
  - Front matter generation (title, description, aliases)
  - Ignore list for pages with custom local content
  - Semantic text comparison (ignores markup differences)
  - Summary table showing operation per page

Usage:
  python3 scripts/harvest_osgeo.py [--dry-run] [--verbose]
"""

import argparse
import difflib
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

import html2text
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SITE_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = SITE_ROOT / "content"
IGNORE_LIST_FILE = SITE_ROOT / "scripts" / "harvest_ignore.json"
SITEMAP_INDEX_URL = "https://www.osgeo.org/sitemap.xml"
PAGE_SITEMAP_URL = "https://www.osgeo.org/page-sitemap.xml"
BASE_URL = "https://www.osgeo.org"
REQUEST_DELAY = 0.5  # seconds between requests, be polite

# Default ignore list - pages where local content takes precedence
DEFAULT_IGNORE = [
    "/",                    # Landing page - custom hero
    "/search/",             # Local search implementation
    "/demo/",               # Demo pages
    "/demo-2/",
    "/site-survey/",
    "/archive-templates/",  # WordPress archive templates
    "/archive-templates/foundation-news/",
    "/archive-templates/community-news/",
    "/archive-templates/partners/",
    "/archive-templates/projects/",
    "/archive-templates/resources/",
    "/archive-templates/events/",
    "/archive-templates/local-chapters/",
    "/archive-templates/sponsors/",
    "/archive-templates/service-providers/",
    "/archive-templates/geo-for-all-labs/",
]

console = Console()


# ---------------------------------------------------------------------------
# Ignore list management
# ---------------------------------------------------------------------------

def load_ignore_list() -> list[str]:
    """Load the ignore list from JSON file, creating with defaults if missing."""
    if IGNORE_LIST_FILE.exists():
        with open(IGNORE_LIST_FILE) as f:
            return json.load(f)
    # Create default
    IGNORE_LIST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(IGNORE_LIST_FILE, "w") as f:
        json.dump(DEFAULT_IGNORE, f, indent=2)
    return DEFAULT_IGNORE


def is_ignored(path: str, ignore_list: list[str]) -> bool:
    """Check if a URL path is in the ignore list."""
    # Normalize: ensure trailing slash
    normalized = path.rstrip("/") + "/" if path != "/" else "/"
    for pattern in ignore_list:
        p = pattern.rstrip("/") + "/" if pattern != "/" else "/"
        if normalized == p:
            return True
        # Also match prefix for archive-templates etc.
        if normalized.startswith(p) and p.endswith("/"):
            for ig in ignore_list:
                ig_norm = ig.rstrip("/") + "/" if ig != "/" else "/"
                if normalized == ig_norm:
                    return True
    return False


# ---------------------------------------------------------------------------
# URL / path mapping
# ---------------------------------------------------------------------------

def url_to_content_path(url: str) -> Path:
    """Map an osgeo.org URL to a local content/ file path."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        return CONTENT_DIR / "_index.md"

    # Map to Hugo content structure
    parts = path.split("/")

    # Check if this maps to an _index.md (section page) or a leaf page
    # If the path has children in our content dir, it's a section
    candidate_dir = CONTENT_DIR / path
    if candidate_dir.is_dir():
        return candidate_dir / "_index.md"

    # Check if parent dir exists as a section
    parent_dir = CONTENT_DIR / "/".join(parts[:-1]) if len(parts) > 1 else CONTENT_DIR
    if parent_dir.is_dir():
        # Leaf page inside existing section
        leaf_dir = CONTENT_DIR / path
        return leaf_dir / "index.md"

    # Create as a new section/leaf
    # If it looks like a section (no file extension, could have children)
    return CONTENT_DIR / path / "_index.md"


# ---------------------------------------------------------------------------
# HTML fetching and parsing
# ---------------------------------------------------------------------------

def fetch_page(url: str) -> tuple[str, str, str]:
    """Fetch a page and extract title, description, and main content HTML.

    Returns (title, description, content_html).
    """
    resp = requests.get(url, timeout=30, headers={
        "User-Agent": "OSGeo-Hugo-Harvester/1.0 (content sync)"
    })
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")

    # Title
    title = ""
    og_title = soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"]
    elif soup.title:
        title = soup.title.string or ""
        # Strip " - OSGeo" suffix
        title = re.sub(r"\s*[-|]\s*OSGeo.*$", "", title).strip()

    # Description
    description = ""
    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        description = meta_desc["content"]

    # Main content - WordPress uses .entry-content or article
    content_el = (
        soup.find("div", class_="entry-content")
        or soup.find("article")
        or soup.find("main")
        or soup.find("div", id="content")
    )

    content_html = ""
    if content_el:
        # Remove nav, footer, sidebar elements from content
        for tag in content_el.find_all(["nav", "aside", "footer", "script", "style"]):
            tag.decompose()
        # Remove WordPress-specific cruft
        for tag in content_el.find_all("div", class_=re.compile(r"sharedaddy|jp-relatedposts|post-navigation")):
            tag.decompose()
        content_html = str(content_el)

    return title, description, content_html


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean markdown."""
    converter = html2text.HTML2Text()
    converter.body_width = 0  # No wrapping
    converter.protect_links = True
    converter.wrap_links = False
    converter.unicode_snob = True
    converter.skip_internal_links = False
    converter.inline_links = True
    converter.ignore_images = False
    converter.ignore_emphasis = False

    md = converter.handle(html)

    # Clean up excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip()


def extract_plain_text(html: str) -> str:
    """Extract plain text from HTML for semantic comparison."""
    soup = BeautifulSoup(html, "lxml")
    # Remove script/style
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ---------------------------------------------------------------------------
# Hugo front matter
# ---------------------------------------------------------------------------

def build_front_matter(title: str, description: str, url_path: str) -> str:
    """Build Hugo front matter YAML."""
    lines = ["---"]
    lines.append(f'title: "{escape_yaml(title)}"')
    if description:
        lines.append(f'description: "{escape_yaml(description)}"')
    lines.append("draft: false")
    # Add alias from the original osgeo.org path
    alias = url_path.rstrip("/") + "/" if url_path != "/" else "/"
    lines.append(f"aliases:")
    lines.append(f"  - {alias}")
    lines.append(f'harvested_from: "{BASE_URL}{url_path}"')
    lines.append("---")
    return "\n".join(lines)


def escape_yaml(s: str) -> str:
    """Escape a string for YAML double-quoted scalar."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


# ---------------------------------------------------------------------------
# Semantic comparison
# ---------------------------------------------------------------------------

def semantic_similarity(text_a: str, text_b: str) -> float:
    """Compute semantic similarity ratio between two plain-text strings.

    Returns a float 0.0-1.0 where 1.0 means identical text.
    """
    if not text_a and not text_b:
        return 1.0
    if not text_a or not text_b:
        return 0.0
    return difflib.SequenceMatcher(None, text_a, text_b).ratio()


def extract_text_from_markdown(md: str) -> str:
    """Extract plain text from markdown (strip front matter and markup)."""
    # Remove front matter
    md = re.sub(r"^---.*?---\s*", "", md, flags=re.DOTALL)
    # Remove Hugo shortcodes
    md = re.sub(r"\{\{[<>%].*?[>%]\}\}", "", md)
    # Remove markdown links, keep text
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    # Remove images
    md = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", md)
    # Remove HTML tags
    md = re.sub(r"<[^>]+>", "", md)
    # Remove markdown formatting
    md = re.sub(r"[*_#>`~\-]", "", md)
    # Normalize whitespace
    md = re.sub(r"\s+", " ", md).strip()
    return md


# ---------------------------------------------------------------------------
# Sitemap fetching
# ---------------------------------------------------------------------------

def fetch_page_urls() -> list[str]:
    """Fetch all page URLs from the osgeo.org page sitemap."""
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    resp = requests.get(PAGE_SITEMAP_URL, timeout=15)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    urls = []
    for url_el in root.findall("s:url", ns):
        loc = url_el.find("s:loc", ns)
        if loc is not None and loc.text:
            urls.append(loc.text)
    return urls


# ---------------------------------------------------------------------------
# Main harvest logic
# ---------------------------------------------------------------------------

def harvest(dry_run: bool = False, verbose: bool = False) -> list[dict]:
    """Run the full harvest. Returns a list of result dicts for the report."""
    ignore_list = load_ignore_list()
    console.print(f"[bold]Fetching sitemap from {PAGE_SITEMAP_URL}...[/bold]")
    urls = fetch_page_urls()
    console.print(f"Found [bold]{len(urls)}[/bold] pages in sitemap")
    console.print(f"Ignore list has [bold]{len(ignore_list)}[/bold] entries")

    results = []

    for i, url in enumerate(urls):
        parsed = urlparse(url)
        url_path = parsed.path

        # Check ignore list
        if is_ignored(url_path, ignore_list):
            results.append({
                "url": url_path,
                "operation": "ignored",
                "similarity": "-",
                "detail": "In ignore list",
            })
            if verbose:
                console.print(f"  [{i+1}/{len(urls)}] SKIP (ignored): {url_path}")
            continue

        # Determine local file path
        local_path = url_to_content_path(url)

        try:
            # Fetch remote page
            if verbose:
                console.print(f"  [{i+1}/{len(urls)}] Fetching: {url_path}")
            title, description, content_html = fetch_page(url)

            if not content_html.strip():
                results.append({
                    "url": url_path,
                    "operation": "skipped",
                    "similarity": "-",
                    "detail": "No content found on page",
                })
                continue

            # Convert to markdown
            md_body = html_to_markdown(content_html)
            front_matter = build_front_matter(title, description, url_path)
            new_content = f"{front_matter}\n\n{md_body}\n"

            # Extract plain text from remote for semantic comparison
            remote_text = extract_plain_text(content_html)

            # Check if local file exists
            if local_path.exists():
                existing = local_path.read_text(encoding="utf-8")
                local_text = extract_text_from_markdown(existing)

                # Semantic similarity
                sim = semantic_similarity(remote_text, local_text)
                sim_pct = f"{sim:.1%}"

                if sim > 0.95:
                    results.append({
                        "url": url_path,
                        "operation": "no change",
                        "similarity": sim_pct,
                        "detail": f"Content matches (>95%)",
                    })
                    continue

                # Content differs - update
                if not dry_run:
                    local_path.parent.mkdir(parents=True, exist_ok=True)
                    local_path.write_text(new_content, encoding="utf-8")

                results.append({
                    "url": url_path,
                    "operation": "update" if not dry_run else "update (dry)",
                    "similarity": sim_pct,
                    "detail": f"Content differs",
                })
            else:
                # New page - insert
                remote_text_for_sim = extract_plain_text(content_html)

                if not dry_run:
                    local_path.parent.mkdir(parents=True, exist_ok=True)
                    local_path.write_text(new_content, encoding="utf-8")

                results.append({
                    "url": url_path,
                    "operation": "insert" if not dry_run else "insert (dry)",
                    "similarity": "new",
                    "detail": f"New page -> {local_path.relative_to(SITE_ROOT)}",
                })

        except requests.RequestException as e:
            results.append({
                "url": url_path,
                "operation": "error",
                "similarity": "-",
                "detail": str(e)[:60],
            })

        # Be polite
        time.sleep(REQUEST_DELAY)

    # Check for local pages that no longer exist in sitemap (potential deletes)
    remote_paths = set()
    for url in urls:
        remote_paths.add(urlparse(url).path)

    for md_file in CONTENT_DIR.rglob("*.md"):
        # Read front matter to check if it was harvested
        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue
        if "harvested_from:" not in text:
            continue  # Not a harvested file, skip

        # Extract the harvested URL
        match = re.search(r'harvested_from:\s*"([^"]+)"', text)
        if not match:
            continue
        harvested_url = match.group(1)
        harvested_path = urlparse(harvested_url).path

        if harvested_path not in remote_paths:
            results.append({
                "url": harvested_path,
                "operation": "orphaned",
                "similarity": "-",
                "detail": f"No longer in sitemap: {md_file.relative_to(SITE_ROOT)}",
            })

    return results


def print_report(results: list[dict]):
    """Print a rich table summarizing the harvest."""
    table = Table(title="OSGeo Content Harvest Report", show_lines=False)
    table.add_column("URL Path", style="cyan", max_width=50)
    table.add_column("Operation", style="bold")
    table.add_column("Similarity", justify="center")
    table.add_column("Detail", style="dim", max_width=50)

    # Sort: errors first, then inserts, updates, no change, ignored
    order = {"error": 0, "insert": 1, "insert (dry)": 1, "update": 2,
             "update (dry)": 2, "orphaned": 3, "no change": 4,
             "skipped": 5, "ignored": 6}
    results.sort(key=lambda r: order.get(r["operation"], 99))

    op_colors = {
        "insert": "green", "insert (dry)": "green",
        "update": "yellow", "update (dry)": "yellow",
        "no change": "dim", "ignored": "dim blue",
        "error": "red", "skipped": "dim", "orphaned": "red",
    }

    for r in results:
        color = op_colors.get(r["operation"], "white")
        table.add_row(
            r["url"],
            f"[{color}]{r['operation']}[/{color}]",
            r["similarity"],
            r["detail"],
        )

    console.print()
    console.print(table)

    # Summary counts
    counts = {}
    for r in results:
        op = r["operation"]
        counts[op] = counts.get(op, 0) + 1

    console.print()
    console.print("[bold]Summary:[/bold]")
    for op, count in sorted(counts.items()):
        console.print(f"  {op}: {count}")
    console.print(f"  [bold]total: {len(results)}[/bold]")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Harvest content from osgeo.org into Hugo content/")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files, just show what would happen")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show progress for each page")
    args = parser.parse_args()

    console.print("[bold green]OSGeo Content Harvester[/bold green]")
    console.print(f"Content dir: {CONTENT_DIR}")
    console.print(f"Dry run: {args.dry_run}")
    console.print()

    results = harvest(dry_run=args.dry_run, verbose=args.verbose)
    print_report(results)


if __name__ == "__main__":
    main()
