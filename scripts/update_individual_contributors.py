#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import datetime
import os

CONFIG_PATH = "data/contributors/config.json"
CONTRIBUTORS_PATH = "data/contributors/contributors.json"
GITHUB_API = "https://api.github.com"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def github_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def fetch_all_contributors(repo_name):
    # repo_url: https://github.com/org/repo
    contributors = []
    page = 1
    while True:
        url = f"{GITHUB_API}/repos/qgis/{repo_name}/contributors"
        params = {"per_page": 100, "page": page}
        resp = requests.get(url, headers=github_headers(), params=params)
        if resp.status_code != 200:
            print(f"Failed to fetch {repo_name} page {page}: {resp.status_code}")
            break
        data = resp.json()
        if not data:
            break
        contributors.extend(data)
        if len(data) < 100:
            break
        page += 1
    return contributors

def main():
    config = load_json(CONFIG_PATH)
    all_contributors = {}
    for thematic, repos in config["repositories"].items():
        if not repos:
            continue  # Ignore thematics without repositories
        for repo_name in repos:
            print(f"Fetching contributors for {repo_name} (thematic: {thematic})...")
            contributors = fetch_all_contributors(repo_name)
            for c in contributors:
                login = c.get("login")
                avatar_url = c.get("avatar_url")
                contribs = c.get("contributions", 0)
                if not login:
                    continue
                if login not in all_contributors:
                    all_contributors[login] = {
                        "login": login,
                        "avatar_url": avatar_url,
                        "total_contributions": 0,
                        "thematics": {}
                    }
                all_contributors[login]["total_contributions"] += contribs
                if thematic in all_contributors[login]["thematics"]:
                    all_contributors[login]["thematics"][thematic] += contribs
                else:
                    all_contributors[login]["thematics"][thematic] = contribs
            # Save after each repo to avoid memory saturation
            save_json(CONTRIBUTORS_PATH, list(all_contributors.values()))
    print(f"Done. Saved {len(all_contributors)} contributors to {CONTRIBUTORS_PATH}")

if __name__ == "__main__":
    main()

