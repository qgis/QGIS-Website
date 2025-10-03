#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import datetime
import os

CONFIG_PATH = "data/contributors/config.json"
ORG_PATH = "data/contributors/organizations.json"
CONTRIBUTORS_API = "https://hub.qgis.org/api/v1/contributors"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def fetch_all_repos():
    url = f"{CONTRIBUTORS_API}/fetch-all-repos"
    print(f"Fetching repositories from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_commit_counts(repo_name, author=None, since=None, until=None):
    url = f"{CONTRIBUTORS_API}/{repo_name}/commit-counts"
    params = {}
    if author:
        url += f"/{author}"
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    print(f"    Querying {url} with params {params}")
    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json():
        return response.json()
    return None

def update_stats():
    print("Loading config and organizations...")
    config = load_json(CONFIG_PATH)
    orgs = load_json(ORG_PATH)
    for org in orgs:
        print(f"Processing organization: {org['name']}")
        for thematic, repos in config["repositories"].items():
            print(f"  Thematic area: {thematic}")
            if not repos:
                print(f"    Skipping {thematic} (no repositories defined)")
                continue
            total_commits = 0
            last_date = None
            for repo_name in repos:
                for member in org.get("members", []):
                    author_names = member["author_names"]
                    from_date = member.get("from")
                    to_date = member.get("to")
                    since = from_date if from_date else None
                    until = to_date if to_date else None
                    commit_counts = get_commit_counts(repo_name, author=author_names, since=since, until=until)
                    total_commits += commit_counts.get("commits", 0)
                    member_last_date = commit_counts.get("last_commit_date")
                    if member_last_date:
                        member_last_dt = datetime.datetime.strptime(member_last_date[:19], "%Y-%m-%d %H:%M:%S")
                        if last_date is None:
                            last_date = member_last_dt
                        else:
                            last_dt = last_date if isinstance(last_date, datetime.datetime) else datetime.datetime.strptime(last_date[:19], "%Y-%m-%d %H:%M:%S")
                            if member_last_dt > last_dt:
                                last_date = member_last_dt
            # Update org stats
            if thematic in org["contributions"]:
                org["contributions"][thematic]["commits"] = total_commits
                print(last_date, '#####')
                org["contributions"][thematic]["last_contribution"] = last_date.strftime("%Y-%m-%d") if last_date else None
    print("Saving updated organizations...")
    save_json(ORG_PATH, orgs)
    print("Done.")

if __name__ == "__main__":
    fetch_all_repos()
    update_stats()

