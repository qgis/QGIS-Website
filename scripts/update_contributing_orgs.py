#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
import datetime
import os

CONFIG_PATH = "data/contributors/config.json"
ORG_PATH = "data/contributors/organizations.json"
GITHUB_API = "https://api.github.com"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def github_headers():
    return {
        "Accept": "application/vnd.github.v3+json"
    }

def get_commit_count(repo, author=None, since=None, until=None):
    url = f"{GITHUB_API}/repos/{repo}/commits"
    headers = github_headers()
    params = {"per_page": 1}
    if author:
        params["author"] = author
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    response = requests.get(url, headers=headers, params=params)
    link = response.headers.get("Link", "")
    import re
    match = re.search(r'page=(\d+)>; rel="last"', link)
    if match:
        return int(match.group(1))
    # If no Link header, check if there is at least one commit
    if response.status_code == 200 and response.json():
        return 1
    return 0

def get_contributions(repo, username, since=None, until=None):
    print(f"    Querying {repo} for user {username}...")
    commits = get_commit_count(repo, author=username, since=since, until=until)
    prs = requests.get(
        f"{GITHUB_API}/search/issues",
        params={"q": f"repo:{repo} type:pr author:{username}"},
        headers=github_headers()
    ).json()
    issues = requests.get(
        f"{GITHUB_API}/search/issues",
        params={"q": f"repo:{repo} type:issue author:{username}"},
        headers=github_headers()
    ).json()
    print(f"      Commits: {commits}, PRs: {prs.get('total_count', 0)}, Issues: {issues.get('total_count', 0)}")
    return {
        "commits": commits,
        "pull_requests": prs.get("total_count", 0),
        "issues": issues.get("total_count", 0)
    }

def compute_level(count, thresholds):
    for i, t in enumerate(thresholds):
        if count <= t:
            return i
    return len(thresholds)

def update_stats():
    print("Loading config and organizations...")
    config = load_json(CONFIG_PATH)
    orgs = load_json(ORG_PATH)
    for org in orgs:
        print(f"Processing organization: {org['name']}")
        for thematic, thematic_cfg in config["levels"].items():
            print(f"  Thematic area: {thematic}")
            repos = thematic_cfg.get("repositories", [])
            if not repos:
                print(f"    Skipping {thematic} (no repositories defined)")
                continue
            thresholds = thematic_cfg["thresholds"]
            total_commits = total_prs = total_issues = 0
            last_date = None
            for repo_url in repos:
                repo = "/".join(repo_url.split("/")[-2:])
                for member in org.get("members", []):
                    username = member["username"]
                    from_date = member.get("from")
                    to_date = member.get("to")
                    since = f"{from_date}T00:00:00Z" if from_date else None
                    until = f"{to_date}T23:59:59Z" if to_date else None
                    contrib = get_contributions(repo, username, since=since, until=until)
                    total_commits += contrib["commits"]
                    total_prs += contrib["pull_requests"]
                    total_issues += contrib["issues"]
                    
                    # Update last_date using commit dates
                    commits_response = requests.get(
                      f"{GITHUB_API}/repos/{repo}/commits",
                      params={"author": username, "per_page": 1},
                      headers=github_headers()
                    )
                    if commits_response.status_code == 200:
                      commits_data = commits_response.json()
                      for commit in commits_data:
                        commit_date_str = commit.get("commit", {}).get("author", {}).get("date")
                        if commit_date_str:
                          commit_date = datetime.datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")
                          if last_date is None or commit_date > last_date:
                            last_date = commit_date
                    # If no commits, last_date remains None
            # Update org stats
            if thematic in org["contributions"]:
                org["contributions"][thematic]["commits"] = total_commits
                org["contributions"][thematic]["pull_requests"] = total_prs
                org["contributions"][thematic]["issues"] = total_issues
                org["contributions"][thematic]["level"] = compute_level(
                    total_commits + total_prs + total_issues, thresholds
                )
                org["contributions"][thematic]["last_contribution"] = last_date.strftime("%Y-%m-%d") if last_date else None
    print("Saving updated organizations...")
    save_json(ORG_PATH, orgs)
    print("Done.")

if __name__ == "__main__":
    update_stats()

