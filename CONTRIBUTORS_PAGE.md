# QGIS Contributor & Organization Data Aggregation

Link: https://qgis.org/community/volunteers/

This document explains how data for organizations and individual contributors is collected, aggregated, and maintained in this repository. It covers:
- Data sources and config files
- Python scripts for automation
- Manual vs. automatic fields
- File structure and attribute mapping

---

## 1. Configuration: `config.json` / `config_template.yml`
- Defines **thematic areas** (e.g., documentation, qgis_core, web_sites).
- For each thematic:
  - `thresholds`: Used to compute contribution "level" (0–5) based on total activity.
  - `repositories`: List of GitHub repos to aggregate for that thematic (except for community/infrastructure, which are manual).

## 2. Organization Data: `organizations.json` / `organizations_template.yml`
- Each organization entry includes:
  - Basic metadata: `name`, `image`, `url`, `description`, etc.
  - `members`: List of GitHub usernames mapped to the org, with `from`/`to` dates for historical tracking. **Manual**.
  - `contributions`: Per-thematic stats (commits, PRs, issues, last_contribution, level).
    - For GitHub-tracked thematics (documentation, qgis_core, web_sites):
      - **Automatically aggregated** by scripts (see below).
      - `commits`: Total commits by org members in thematic repos.
      - `pull_requests`: Total PRs opened by org members.
      - `issues`: Total issues opened by org members.
      - `last_contribution`: Latest date of any commit, PR, or issue.
      - `level`: Computed from thresholds in config.
    - For community_activities and qgis_infrastructure:
      - **Manual**: `events`, `sponsorship`, `other`, `contributions`, `last_contribution`, `level`.

## 3. Individual Contributor Data: `contributors.json`
- Each contributor entry includes:
  - `login`, `avatar_url`: From GitHub API.
  - `total_contributions`: Sum of all commits, PRs, and issues across all thematics/repos. **Automatic**.
  - `thematics`: Per-thematic breakdown:
    - For each thematic:
      - `commits`: Total commits in thematic repos.
      - `pull_requests`: Total PRs in thematic repos.
      - `issues`: Total issues in thematic repos.
      - `last_contribution`: Latest date of any commit, PR, or issue in thematic repos.
    - All fields **automatically aggregated** by scripts.

## 4. Automation Scripts

### `update_individual_contributors.py`
- Reads config and iterates over all thematic repos.
- For each repo and contributor:
  - Fetches commit counts (GitHub API).
  - Uses GitHub Search API to count PRs and issues (`total_count` for accuracy).
  - Aggregates per-thematic stats for each contributor.
  - Updates `contributors.json` incrementally.
- All fields in `contributors.json` are **automatic** except for manual exclusions or overrides.

### `update_contributing_orgs.py`
- Reads config and organizations.
- For each org and thematic:
  - Iterates over all mapped members and thematic repos.
  - Aggregates commits, PRs, issues using GitHub API and Search API.
  - Computes `level` using config thresholds.
  - Updates `last_contribution` using latest commit/PR/issue date.
  - Updates `organizations.json`.
- For community/infrastructure thematics, stats are **manual**.

## 5. Manual vs. Automatic Fields

| File                  | Attribute/Section         | Manual/Automatic | Notes |
|---------------------- |--------------------------|------------------|-------|
| organizations.json    | name, image, url, desc   | Manual           | Org metadata |
| organizations.json    | members                  | Manual           | Map usernames to org |
| organizations.json    | contributions (GH areas) | Automatic        | By script |
| organizations.json    | contributions (community/infrastructure) | Manual | Events, sponsorship, etc. |
| contributors.json     | login, avatar_url        | Automatic        | From GitHub |
| contributors.json     | total_contributions      | Automatic        | By script |
| contributors.json     | thematics                | Automatic        | By script |

## 6. Data Update Workflow

1. **Edit config.json** to update repos or thresholds.
2. **Edit organizations.json** to add orgs, members, or manual stats.
3. **Run scripts** to aggregate and update stats:
   - `python scripts/update_individual_contributors.py`
   - `python scripts/update_contributing_orgs.py`
4. **Review output** in JSON files. Manual fields can be edited directly if needed.

---

For more details, see comments in each template file and script.
