#!/usr/bin/env python3

"""
Simplified GitHub contribution counter for QGIS repositories.

Usage:
    python update_individual_contributors.py --token YOUR_TOKEN

Features:
- Reads repositories from data/contributors/config.json
- Outputs to data/contributors/contributors.json
- Incremental updates: preserves existing data
- Supports commenting out repos/thematics in config
- Smart rate limiting and error handling
"""

import requests
import json
import os
import time
from datetime import datetime, timezone
from collections import defaultdict
from typing import Dict
import threading

class GitHubContributionCounter:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.api_url = "https://api.github.com/graphql"
        self.rate_limit_lock = threading.Lock()
        
        # Repository-specific date filters
        self.repo_date_filters = {
            "QGIS-Hub-Website": "2024-08-12T00:00:00Z",
            "QGIS-Certification-Website": "2025-03-19T00:00:00Z", 
            "QGIS-Changelog-Website": "2025-03-17T00:00:00Z"
        }
        
        # Load email-to-GitHub mappings
        self.email_mappings = self.load_email_mappings()

        
    def check_rate_limit(self) -> Dict:
        """Check remaining rate limit (thread-safe)."""
        with self.rate_limit_lock:
            try:
                query = """
                query {
                  rateLimit {
                    limit
                    remaining
                    resetAt
                  }
                }
                """
                response = requests.post(
                    self.api_url,
                    json={"query": query},
                    headers=self.headers,
                    timeout=30  # Add timeout
                )
                response.raise_for_status()
                data = response.json()
                if "errors" in data:
                    print(f"Rate limit check errors: {data['errors']}")
                    return {"remaining": 100, "limit": 5000, "resetAt": ""}
                return data["data"]["rateLimit"]
            except (requests.RequestException, KeyError, json.JSONDecodeError) as e:
                print(f"Rate limit check failed: {e}, assuming safe defaults")
                return {"remaining": 100, "limit": 5000, "resetAt": ""}
    
    def get_commits_with_authors(self, owner: str, repo: str, branch: str = "main") -> Dict[str, int]:
        """
        Get commits with GitHub user associations using GraphQL.
        Uses pagination to handle large repos efficiently.
        
        For commits without GitHub user association (e.g., from migrations),
        tracks by email and prefixes with 'email:' to distinguish from GitHub logins.
        """
        print(f"Fetching data for {owner}/{repo}:{branch}")
        contributions = defaultdict(int)
        excluded_bots = 0
        anonymous_commits = 0  # Track commits without GitHub accounts
        has_next_page = True
        cursor = None
        processed_commits = 0
        
        iteration_count = 0
        max_iterations = 1000  # Safety limit to prevent infinite loops
        
        while has_next_page and iteration_count < max_iterations:
            iteration_count += 1
            
            # Check rate limit less frequently (every 10 iterations or when remaining is low)
            if iteration_count % 10 == 1 or processed_commits == 0:
                rate_limit = self.check_rate_limit()
                if rate_limit["remaining"] < 50:  # Increased threshold for better performance
                    try:
                        if rate_limit["resetAt"]:
                            reset_time = time.mktime(time.strptime(rate_limit["resetAt"], "%Y-%m-%dT%H:%M:%SZ"))
                            wait_time = min(300, max(60, (reset_time - time.time()) / max(1, rate_limit["remaining"])))  # Cap at 5 minutes
                        else:
                            wait_time = 60  # Default wait
                        print(f"Rate limit low ({rate_limit['remaining']}). Waiting {wait_time:.1f}s...")
                        time.sleep(wait_time)
                    except (ValueError, OSError) as e:
                        print(f"Rate limit parsing error: {e}, waiting 60s...")
                        time.sleep(60)
            
            # Check if this repo has a date filter
            since_date = self.repo_date_filters.get(repo)
            
            if since_date:
                query = """
                query($owner: String!, $repo: String!, $branch: String!, $cursor: String, $since: GitTimestamp) {
                  repository(owner: $owner, name: $repo) {
                    ref(qualifiedName: $branch) {
                      target {
                        ... on Commit {
                          history(first: 100, after: $cursor, since: $since) {
                            pageInfo {
                              hasNextPage
                              endCursor
                            }
                            nodes {
                              oid
                              committedDate
                              author {
                                user {
                                  login
                                }
                                name
                                email
                              }
                              committer {
                                user {
                                  login
                                }
                                name
                                email
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
                """
            else:
                query = """
                query($owner: String!, $repo: String!, $branch: String!, $cursor: String) {
                  repository(owner: $owner, name: $repo) {
                    ref(qualifiedName: $branch) {
                      target {
                        ... on Commit {
                          history(first: 100, after: $cursor) {
                            pageInfo {
                              hasNextPage
                              endCursor
                            }
                            nodes {
                              oid
                              committedDate
                              author {
                                user {
                                  login
                                }
                                name
                                email
                              }
                              committer {
                                user {
                                  login
                                }
                                name
                                email
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
                """
            
            variables = {
                "owner": owner,
                "repo": repo,
                "branch": branch,
                "cursor": cursor
            }
            
            # Add date filter if specified for this repo
            if since_date:
                variables["since"] = since_date
                if cursor is None:  # Only log on first page
                    print(f"  Filtering commits since {since_date}")
            
            try:
                response = requests.post(
                    self.api_url,
                    json={"query": query, "variables": variables},
                    headers=self.headers,
                    timeout=60  # Add timeout to prevent hanging
                )
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Request failed for {owner}/{repo}:{branch}: {e}")
                break
            
            data = response.json()
            
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}")
                break
            
            history = data["data"]["repository"]["ref"]["target"]["history"]
            commits = history["nodes"]
            
            for commit in commits:
                author = commit["author"]
                committer = commit["committer"]
                
                
                # Skip if committer is a bot or no GitHub user
                if committer.get("user"):
                    committer_login = committer["user"]["login"]
                    if self.is_bot_login(committer_login):
                        excluded_bots += 1
                        continue
                else:
                    # Committer has no GitHub account - likely automated
                    if self.is_bot_email(committer.get("email", "")):
                        excluded_bots += 1
                        continue
                
                # Get author's GitHub login (this deduplicates users!)
                if author.get("user"):
                    author_login = author["user"]["login"]
                    if not self.is_bot_login(author_login):
                        contributions[author_login] += 1
                else:
                    # No GitHub account linked - use email for anonymous commits
                    author_email = author.get("email", "")
                    author_name = author.get("name", "")
                    
                    # Skip if author email looks like a bot
                    if author_email and not self.is_bot_email(author_email):
                        # Use email as identifier, prefixed to distinguish from GitHub logins
                        # Format: "email:user@example.com"
                        contributions[f"email:{author_email}"] += 1
                        anonymous_commits += 1
                    elif author_name and not any(bot in author_name.lower() for bot in ['bot', 'github-actions']):
                        # Fallback to name if no valid email (rare case)
                        contributions[f"name:{author_name}"] += 1
                        anonymous_commits += 1
            
            page_info = history["pageInfo"]
            has_next_page = page_info["hasNextPage"]
            cursor = page_info["endCursor"]
            
            processed_commits += len(commits)
            print(f"Processed {processed_commits} commits, {len(contributions)} unique contributors...")
            
            # Safety check: if no commits in this page, something might be wrong
            if len(commits) == 0:
                print("Warning: Received empty commit page, stopping pagination...")
                break
                
            # Safety check: prevent processing too many commits (likely infinite loop)
            if processed_commits > 150000:  # 150k commits should be more than enough
                print(f"Warning: Processed {processed_commits} commits, stopping to prevent infinite loop...")
                break
        
        if iteration_count >= max_iterations:
            print(f"Warning: Reached maximum iterations ({max_iterations}), stopping pagination...")
        
        result = dict(contributions)
        print(f"Total commits: {processed_commits}, Contributors: {len(result)}, Excluded bot commits: {excluded_bots}, Anonymous commits: {anonymous_commits}")
        
        return result


        
    def process_repositories(self, config_path: str, output_path: str) -> Dict[str, Dict]:
        """Process repositories from config file and update contributors data."""
        # Load config file
        if not os.path.exists(config_path):
            print(f"Config file not found: {config_path}")
            return {}
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Load existing contributors for incremental updates
        all_contributors = self.load_existing_data(output_path)
        
        # Track which thematics and repos are being processed (for cleanup)
        processed_thematics = set()
        processed_repos = set()
        
        # Process each thematic
        for thematic, repos in config["repositories"].items():
            if not repos:
                continue
            
            print(f"\nProcessing thematic: {thematic}")
            processed_thematics.add(thematic)
            
            # Reset thematic contributions for all contributors
            for login in all_contributors:
                old_contrib = all_contributors[login]["thematics"].get(thematic, 0)
                all_contributors[login]["total_contributions"] -= old_contrib
                all_contributors[login]["thematics"][thematic] = 0
            
            # Accumulate contributions across all repos in this thematic
            thematic_contributors = defaultdict(int)
            
            for repo_name in repos:
                processed_repos.add((thematic, repo_name))
                print(f"  Fetching contributors for {repo_name}...")
                
                try:
                    # Try both master and main branches
                    contributors_data = {}
                    for branch in ["master", "main"]:
                        try:
                            branch_data = self.get_commits_with_authors("qgis", repo_name, branch)
                            if branch_data:
                                contributors_data = branch_data
                                break
                        except Exception as e:
                            print(f"    Failed branch {branch}: {e}")
                            continue
                    
                    if not contributors_data:
                        print(f"    No data found for {repo_name}")
                        continue
                    
                    # Accumulate contributions for this thematic
                    repo_contributors = set()
                    for login, commit_count in contributors_data.items():
                        # Skip bot logins
                        if self.is_bot_login(login):
                            continue
                        
                        # Handle email-based contributors (from migrated commits)
                        # Support both "email:" and old "no-github:" prefixes
                        if login.startswith("email:") or login.startswith("name:") or login.startswith("no-github:"):
                            # First check manual mapping file
                            resolved_login = self.email_mappings.get(login)
                            
                            if resolved_login:
                                # Successfully resolved to GitHub account
                                repo_contributors.add(resolved_login)
                                thematic_contributors[resolved_login] += commit_count
                            else:
                                # Keep as email-based contributor
                                # Normalize to "email:" format for consistency
                                if login.startswith("no-github:"):
                                    normalized_login = "email:" + login[10:]
                                    repo_contributors.add(normalized_login)
                                    thematic_contributors[normalized_login] += commit_count
                                else:
                                    repo_contributors.add(login)
                                    thematic_contributors[login] += commit_count
                        else:
                            # Regular GitHub login
                            repo_contributors.add(login)
                            thematic_contributors[login] += commit_count
                    
                    print(f"    Processed {len(repo_contributors)} contributors")
                    
                except Exception as e:
                    print(f"    Error processing {repo_name}: {e}")
                    continue
            
            # Now update all contributors with accumulated thematic contributions
            for login, commit_count in thematic_contributors.items():
                # Get avatar URL (handle email-based contributors)
                # Support "email:", "name:", and old "no-github:" prefixes
                if login.startswith("email:") or login.startswith("name:") or login.startswith("no-github:"):
                    avatar_url = "" # No avatar for email-based contributors
                else:
                    # Regular GitHub user
                    avatar_url = self.get_user_avatar(login)
                
                # Determine if this is a GitHub account
                has_github = not (login.startswith("email:") or login.startswith("name:") or login.startswith("no-github:"))
                
                # Initialize contributor if not exists
                if login not in all_contributors:
                    contributor_data = {
                        "login": login,
                        "avatar_url": avatar_url,
                        "total_contributions": 0,
                        "thematics": {},
                        "has_github_account": has_github
                    }
                    all_contributors[login] = contributor_data
                else:
                    # Update avatar URL in case it changed
                    all_contributors[login]["avatar_url"] = avatar_url
                    # Update has_github_account if it's now a real account
                    if has_github:
                        all_contributors[login]["has_github_account"] = True
                
                # Set thematic contributions and update total
                all_contributors[login]["thematics"][thematic] = commit_count
                all_contributors[login]["total_contributions"] += commit_count
            
            print(f"  Completed thematic '{thematic}' with {len(thematic_contributors)} contributors")
            
            # Save after each thematic
            self.save_contributors(all_contributors, output_path)
        
        return all_contributors
    
    def load_email_mappings(self) -> dict:
        """Load email-to-GitHub login mappings from JSON file."""
        mapping_file = "data/contributors/email_mapping.json"
        if not os.path.exists(mapping_file):
            print(f"Warning: Email mapping file not found: {mapping_file}")
            return {}
        
        try:
            with open(mapping_file, 'r') as f:
                data = json.load(f)
                return data.get("mappings", {})
        except Exception as e:
            print(f"Warning: Could not load email mappings: {e}")
            return {}

    def get_user_avatar(self, login: str) -> str:
        """Get user avatar URL using GraphQL"""
        query = """
        query($login: String!) {
          user(login: $login) {
            avatarUrl
          }
        }
        """
        
        try:
            response = requests.post(
                self.api_url,
                json={"query": query, "variables": {"login": login}},
                headers=self.headers
            )
            
            data = response.json()
            if "errors" in data or not data.get("data", {}).get("user"):
                return f"https://github.com/{login}.png"  # Fallback URL
                
            return data["data"]["user"]["avatarUrl"]
        except:
            return f"https://github.com/{login}.png"  # Fallback URL

    def load_existing_data(self, output_file: str) -> Dict:
        """Load existing contributor data from file if it exists."""
        if not os.path.exists(output_file):
            return {}
        
        try:
            with open(output_file, 'r') as f:
                existing_data = json.load(f)
            
            # Convert back to contributors dict format for merging
            if "contributors" in existing_data and isinstance(existing_data["contributors"], list):
                contributors_dict = {}
                for contributor in existing_data["contributors"]:
                    contributors_dict[contributor["login"]] = contributor
                return contributors_dict
            return {}
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Warning: Could not load existing data from {output_file}: {e}")
            return {}
    
    def save_contributors(self, contributors: Dict, output_path: str):
        """Save contributors data to JSON file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Convert to list format and sort by contributions
        contributors_list = list(contributors.values())
        contributors_list.sort(key=lambda x: x["total_contributions"], reverse=True)
        
        # Create final result
        result = {
            "_automated_warning": {
                "generated_by": "scripts/update_individual_contributors.py",
                "warning": "This file is automatically generated. Do NOT edit manually!",
                "how_to_update": "Run 'python scripts/update_individual_contributors.py --token YOUR_TOKEN'",
                "documentation": "See CONTRIBUTING.md section: Automated Content and Manual Edit Guidelines"
            },
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_contributors": len(contributors_list),
            "contributors": contributors_list
        }
        
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    
    def extract_clean_identifier(self, login: str) -> str:
        """Extract a clean identifier from email: or name: prefixed logins."""
        if login.startswith("email:"):
            email = login[6:]  # Remove "email:" prefix
            # Extract username before @
            if "@" in email:
                return email.split("@")[0]
            return email
        elif login.startswith("name:"):
            return login[5:]  # Remove "name:" prefix
        elif login.startswith("no-github:"):
            email = login[10:]  # Remove "no-github:" prefix
            if "@" in email:
                return email.split("@")[0]
            return email
        return login
    
    
    def is_bot_login(self, login: str) -> bool:
        """Check if GitHub login is a bot."""
        bot_patterns = ['bot', 'github-actions', 'dependabot', 'renovate']
        login_lower = login.lower()
        return any(pattern in login_lower for pattern in bot_patterns) or login.endswith('[bot]')
    
    def is_bot_email(self, email: str) -> bool:
        """Check if email belongs to a bot."""
        bot_patterns = [
            'bot@',
            '[bot]',
            'github-actions',
            'dependabot',
        ]
        email_lower = email.lower()
        return any(pattern in email_lower for pattern in bot_patterns)

def main():
    """Main function - simplified to only process QGIS repositories."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Count GitHub contributions for QGIS repositories')
    parser.add_argument('--token', help='GitHub API token (optional, can use GITHUB_TOKEN env var)')
    
    args = parser.parse_args()
    
    # Get token from argument or environment variable
    token = args.token or os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GitHub token required. Use --token argument or set GITHUB_TOKEN environment variable.")
        return 1
    
    # Don't log the token value
    print("GitHub token loaded successfully")
    
    # Fixed paths
    config_path = "data/contributors/config.json"
    output_path = "data/contributors/contributors.json"
    
    # Initialize counter
    counter = GitHubContributionCounter(token)
    
    # Check rate limit
    rate_limit = counter.check_rate_limit()
    print(f"Rate limit: {rate_limit['remaining']}/{rate_limit['limit']}")
    print(f"Resets at: {rate_limit['resetAt']}\n")
    
    print("Processing QGIS repositories from config...")
    
    try:
        contributors_data = counter.process_repositories(config_path, output_path)
        
        if contributors_data:
            print(f"\nProcessing complete! Saved {len(contributors_data)} contributors to {output_path}")
            return 0
        else:
            print("No contributors found")
            return 1
    except Exception as e:
        print(f"Error during processing: {e}")
        return 1

if __name__ == "__main__":
    main()
