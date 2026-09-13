#!/usr/bin/env python3
import json
import os
import sys
import argparse
import requests
from typing import Dict, List, Tuple


def fetch_v3_stats(project_slug: str, resource_slugs: List[str], token: str, base_url: str = "https://rest.api.transifex.com") -> Dict[str, Dict]:
    """Fetch stats from Transifex API v3 for given project/resources.

    - project_slug: e.g. 'qgis-website'
    - resource_slugs: list like ['qgis-hugo-docs-md']

    Returns a dict: { language_code: { 'translated_strings': int, 'untranslated_strings': int, 'total_strings': int } }
    Values are aggregated across resources (weighted by total_strings).
    """
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.api+json",
    })

    project_id = f"o:qgis:p:{project_slug}"

    def list_resources_for_project() -> Dict[str, str]:
        slug_to_id: Dict[str, str] = {}
        url = f"{base_url}/resources?filter[project]={project_id}"
        while url:
            resp = session.get(url, timeout=60)
            if resp.status_code != 200:
                raise RuntimeError(f"Transifex API v3 error {resp.status_code} for {url}: {resp.text[:500]}")
            payload = resp.json()
            for item in payload.get("data", []):
                attributes = item.get("attributes", {})
                slug = attributes.get("slug")
                if slug:
                    slug_to_id[slug] = item.get("id")
            links = payload.get("links", {})
            url = links.get("next") or ""
        return slug_to_id

    def fetch_resource_language_stats(resource_id: str) -> List[Tuple[str, Dict[str, int]]]:
        results: List[Tuple[str, Dict[str, int]]] = []
        url = (
            f"{base_url}/resource_language_stats?filter[project]={project_id}"
            f"&filter[resource]={resource_id}"
        )
        while url:
            resp = session.get(url, timeout=60)
            if resp.status_code != 200:
                raise RuntimeError(f"Transifex API v3 error {resp.status_code} for {url}: {resp.text[:500]}")
            payload = resp.json()
            for item in payload.get("data", []):
                attributes = item.get("attributes", {})
                relationships = item.get("relationships", {})
                lang_rel = relationships.get("language", {}).get("data", {})
                lang_id = lang_rel.get("id") or ""
                # v3 attributes typically contain translated_strings/untranslated_strings/total_strings
                translated = int(attributes.get("translated_strings") or 0)
                untranslated = int(attributes.get("untranslated_strings") or 0)
                reviewed = int(attributes.get("reviewed_strings") or 0)
                total = int(attributes.get("total_strings") or (translated + untranslated))
                if lang_id.startswith("l:"):
                    lang_code = lang_id.split(":", 1)[1]
                else:
                    lang_code = lang_id or ""
                results.append((lang_code, {
                    'translated_strings': translated,
                    'untranslated_strings': untranslated,
                    'reviewed_strings': reviewed,
                    'total_strings': total,
                }))
            links = payload.get("links", {})
            url = links.get("next") or ""
        return results

    # Resolve resource IDs by slug
    slug_to_id = list_resources_for_project()
    missing = [s for s in resource_slugs if s not in slug_to_id]
    if missing:
        raise RuntimeError(f"Resources not found in project {project_slug}: {', '.join(missing)}")

    agg: Dict[str, Dict[str, int]] = {}
    for slug in resource_slugs:
        res_id = slug_to_id[slug]
        for lang_code, stats in fetch_resource_language_stats(res_id):
            cur = agg.setdefault(lang_code, {'translated_strings': 0, 'untranslated_strings': 0, 'reviewed_strings': 0, 'total_strings': 0})
            cur['translated_strings'] += stats['translated_strings']
            cur['untranslated_strings'] += stats['untranslated_strings']
            cur['reviewed_strings'] += stats['reviewed_strings']
            cur['total_strings'] += stats['total_strings']

    return agg


def to_coverage_percent(agg: Dict[str, Dict]) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for lang, stats in agg.items():
        total = int(stats.get('total_strings') or 0)
        translated = int(stats.get('translated_strings') or 0)
        if total <= 0:
            pct = 0.0
        else:
            pct = round((translated / float(total)) * 100.0, 2)
        out[lang] = pct
    return out


def main():
    parser = argparse.ArgumentParser(description='Fetch translation coverage from Transifex and write data/tx_coverage.json')
    parser.add_argument('--project', required=True, help='Transifex project slug (e.g. qgis-website)')
    parser.add_argument('--resources', required=True, help='Comma-separated list of resource slugs to aggregate (e.g. qgis-hugo-docs-md)')
    # Use TX_TOKEN (same as in i18n workflow)
    default_token = os.environ.get('TX_TOKEN') or ''
    parser.add_argument('--token', default=default_token, help='Transifex API token (v3, Bearer). Set TX_TOKEN env')
    parser.add_argument('--output', default=os.path.join('data', 'tx_coverage.json'), help='Output path')
    args = parser.parse_args()

    if not args.token:
        print('ERROR: Transifex token not provided (use --token or env TX_TOKEN).', file=sys.stderr)
        sys.exit(2)

    resources = [r.strip() for r in args.resources.split(',') if r.strip()]
    if not resources:
        print('ERROR: No resources provided.', file=sys.stderr)
        sys.exit(2)

    agg = fetch_v3_stats(args.project, resources, args.token)
    coverage = to_coverage_percent(agg)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(coverage, f, ensure_ascii=False, indent=2, sort_keys=True)
    print(f"Wrote coverage for {len(coverage)} languages → {args.output}")


if __name__ == '__main__':
    main()


