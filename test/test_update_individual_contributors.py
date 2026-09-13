# -*- coding: utf-8 -*-
"""Regression tests for scripts/update_individual_contributors.py.

These tests exercise the script's real parsing, aggregation, sorting and
transform logic so that a future dependency upgrade (requests, etc.) that
silently changes behaviour would be caught here.

Everything that touches the outside world is mocked:

* network -- ``requests.post`` (the GraphQL endpoint) is replaced with a fake
  that yields canned pages, so no HTTP ever happens;
* time / rate limiting -- ``time.sleep`` is patched to a no-op and the
  reset-time parser is fed deterministic strings;
* filesystem -- reads/writes go through ``tmp_path`` or are captured by
  monkeypatching ``save_contributors``.

``scripts/`` is placed on ``sys.path`` by ``test/conftest.py``, so the module
under test can be imported directly here.
"""
import json

import update_individual_contributors as mod


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def make_counter(monkeypatch, email_mappings=None):
    """Build a counter without loading the real email-mapping file."""
    monkeypatch.setattr(
        mod.GitHubContributionCounter,
        "load_email_mappings",
        lambda self: email_mappings or {},
    )
    return mod.GitHubContributionCounter(token="fake-token")


def commit(author_login=None, author_email=None, author_name=None,
           committer_login=None, committer_email=None):
    """Build a GraphQL commit node the way the API returns it."""
    def actor(login, email, name):
        node = {"name": name, "email": email}
        node["user"] = {"login": login} if login else None
        return node

    return {
        "oid": "deadbeef",
        "committedDate": "2024-01-01T00:00:00Z",
        "author": actor(author_login, author_email, author_name),
        "committer": actor(
            committer_login,
            committer_email,
            committer_login or "committer",
        ),
    }


def graphql_history_response(commits, has_next_page=False, end_cursor=None):
    """Wrap commit nodes in the nested shape get_commits_with_authors reads."""
    return {
        "data": {
            "repository": {
                "ref": {
                    "target": {
                        "history": {
                            "pageInfo": {
                                "hasNextPage": has_next_page,
                                "endCursor": end_cursor,
                            },
                            "nodes": commits,
                        }
                    }
                }
            }
        }
    }


class FakeResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def patch_no_sleep(monkeypatch):
    """Guarantee no real sleeping happens during a test."""
    monkeypatch.setattr(mod.time, "sleep", lambda *a, **k: None)


def patch_safe_rate_limit(monkeypatch):
    """check_rate_limit always reports plenty of quota (skips wait branch)."""
    monkeypatch.setattr(
        mod.GitHubContributionCounter,
        "check_rate_limit",
        lambda self: {"remaining": 5000, "limit": 5000, "resetAt": ""},
    )


# ---------------------------------------------------------------------------
# Bot / identifier helpers (pure functions)
# ---------------------------------------------------------------------------
def test_is_bot_login_matches_known_patterns(monkeypatch):
    counter = make_counter(monkeypatch)
    assert counter.is_bot_login("dependabot[bot]") is True
    assert counter.is_bot_login("github-actions") is True
    assert counter.is_bot_login("renovate") is True
    assert counter.is_bot_login("RoboBOTov") is True  # substring 'bot', case-insensitive
    # Real humans must not be flagged.
    assert counter.is_bot_login("nyalldawson") is False
    assert counter.is_bot_login("octocat") is False


def test_is_bot_email_and_clean_identifier(monkeypatch):
    counter = make_counter(monkeypatch)
    assert counter.is_bot_email("noreply@github-actions.com") is True
    assert counter.is_bot_email("bot@example.com") is True
    assert counter.is_bot_email("jane@example.com") is False

    # extract_clean_identifier strips each supported prefix.
    assert counter.extract_clean_identifier("email:jane@example.com") == "jane"
    assert counter.extract_clean_identifier("name:Jane Doe") == "Jane Doe"
    assert counter.extract_clean_identifier("no-github:bob@x.org") == "bob"
    assert counter.extract_clean_identifier("octocat") == "octocat"


# ---------------------------------------------------------------------------
# get_commits_with_authors: aggregation, dedup, bot exclusion, pagination
# ---------------------------------------------------------------------------
def test_get_commits_aggregates_and_excludes_bots(monkeypatch):
    counter = make_counter(monkeypatch)
    patch_no_sleep(monkeypatch)
    patch_safe_rate_limit(monkeypatch)

    commits = [
        commit(author_login="alice", committer_login="alice"),
        commit(author_login="alice", committer_login="alice"),  # dedup -> alice:2
        commit(author_login="bob", committer_login="bob"),
        # bot author login is excluded entirely
        commit(author_login="dependabot[bot]", committer_login="dependabot[bot]"),
        # bot committer also causes the commit to be skipped
        commit(author_login="carol", committer_login="github-actions[bot]"),
        # anonymous author (no GitHub user) tracked by email
        commit(author_email="anon@example.com", committer_email="anon@example.com"),
        # anonymous author whose email is a bot -> excluded
        commit(author_email="ci@github-actions.com",
               committer_email="ci@github-actions.com"),
    ]

    def fake_post(url, json=None, headers=None, timeout=None):
        return FakeResponse(graphql_history_response(commits))

    monkeypatch.setattr(mod.requests, "post", fake_post)

    result = counter.get_commits_with_authors("qgis", "QGIS-Website", "main")

    assert result["alice"] == 2
    assert result["bob"] == 1
    assert result["email:anon@example.com"] == 1
    # Bots / bot-committed / bot-email commits never appear.
    assert "dependabot[bot]" not in result
    assert "carol" not in result
    assert "email:ci@github-actions.com" not in result


def test_get_commits_falls_back_to_name_when_no_email(monkeypatch):
    counter = make_counter(monkeypatch)
    patch_no_sleep(monkeypatch)
    patch_safe_rate_limit(monkeypatch)

    commits = [
        # No GitHub user and no email -> fall back to name: identifier.
        commit(author_name="Jane Doe", committer_email="jane@example.com"),
    ]
    monkeypatch.setattr(
        mod.requests, "post",
        lambda *a, **k: FakeResponse(graphql_history_response(commits)),
    )

    result = counter.get_commits_with_authors("qgis", "QGIS-Website", "main")
    assert result == {"name:Jane Doe": 1}


def test_get_commits_paginates_across_pages(monkeypatch):
    counter = make_counter(monkeypatch)
    patch_no_sleep(monkeypatch)
    patch_safe_rate_limit(monkeypatch)

    pages = [
        graphql_history_response(
            [commit(author_login="alice", committer_login="alice")],
            has_next_page=True, end_cursor="CURSOR1",
        ),
        graphql_history_response(
            [commit(author_login="alice", committer_login="alice"),
             commit(author_login="bob", committer_login="bob")],
            has_next_page=False, end_cursor=None,
        ),
    ]
    calls = {"n": 0}

    def fake_post(url, json=None, headers=None, timeout=None):
        # The cursor from page 1 must be threaded into the page-2 request.
        if calls["n"] == 1:
            assert json["variables"]["cursor"] == "CURSOR1"
        payload = pages[calls["n"]]
        calls["n"] += 1
        return FakeResponse(payload)

    monkeypatch.setattr(mod.requests, "post", fake_post)

    result = counter.get_commits_with_authors("qgis", "QGIS-Website", "main")
    assert calls["n"] == 2, "should have fetched exactly two pages"
    assert result == {"alice": 2, "bob": 1}


def test_get_commits_returns_empty_on_graphql_errors(monkeypatch):
    counter = make_counter(monkeypatch)
    patch_no_sleep(monkeypatch)
    patch_safe_rate_limit(monkeypatch)

    monkeypatch.setattr(
        mod.requests, "post",
        lambda *a, **k: FakeResponse({"errors": [{"message": "boom"}]}),
    )

    result = counter.get_commits_with_authors("qgis", "Missing", "main")
    assert result == {}


# ---------------------------------------------------------------------------
# Rate-limit reset-time parsing + wait calculation
# ---------------------------------------------------------------------------
def test_rate_limit_low_parses_reset_time_and_waits(monkeypatch):
    """When quota is low the script parses resetAt and sleeps a bounded time."""
    counter = make_counter(monkeypatch)

    # First check returns a low remaining with a parseable resetAt; subsequent
    # checks (none expected) would also be low, but we stop after one page.
    monkeypatch.setattr(
        mod.GitHubContributionCounter,
        "check_rate_limit",
        lambda self: {
            "remaining": 10,
            "limit": 5000,
            "resetAt": "2024-01-01T00:05:00Z",
        },
    )
    # Pin "now" so the wait computation is deterministic; reset is 60s ahead.
    reset_epoch = mod.time.mktime(
        mod.time.strptime("2024-01-01T00:05:00Z", "%Y-%m-%dT%H:%M:%SZ")
    )
    monkeypatch.setattr(mod.time, "time", lambda: reset_epoch - 60)

    slept = []
    monkeypatch.setattr(mod.time, "sleep", lambda s: slept.append(s))

    monkeypatch.setattr(
        mod.requests, "post",
        lambda *a, **k: FakeResponse(graphql_history_response(
            [commit(author_login="alice", committer_login="alice")]
        )),
    )

    result = counter.get_commits_with_authors("qgis", "QGIS-Website", "main")

    assert result == {"alice": 1}
    assert len(slept) == 1, "exactly one rate-limit wait expected"
    # wait = min(300, max(60, (reset-now)/remaining)) -> max(60, 60/10)=60.
    assert slept[0] == 60


# ---------------------------------------------------------------------------
# process_repositories: thematic aggregation, totals, email mapping, reset
# ---------------------------------------------------------------------------
def test_process_repositories_aggregates_thematics_and_totals(monkeypatch, tmp_path):
    config = {
        "repositories": {
            "core": ["QGIS"],
            "web_sites": ["QGIS-Website"],
            "empty": [],  # commented-out / empty thematic must be skipped
        }
    }
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(config))
    output_path = str(tmp_path / "contributors.json")

    # Map an anonymous email contributor onto a real GitHub login.
    counter = make_counter(
        monkeypatch, email_mappings={"email:anon@example.com": "alice"}
    )

    # Per-repo commit counts keyed by repo name.
    per_repo = {
        "QGIS": {"alice": 5, "bob": 3, "dependabot[bot]": 99},
        "QGIS-Website": {"alice": 2, "email:anon@example.com": 4},
    }

    def fake_commits(self, owner, repo, branch="main"):
        # Return data only for the "main" branch; master yields nothing.
        if branch == "main":
            return dict(per_repo[repo])
        return {}

    monkeypatch.setattr(
        mod.GitHubContributionCounter, "get_commits_with_authors", fake_commits
    )
    monkeypatch.setattr(
        mod.GitHubContributionCounter,
        "get_user_avatar",
        lambda self, login: f"https://avatars/{login}.png",
    )
    # Nothing on disk yet; avoid touching the filesystem during saves.
    monkeypatch.setattr(
        mod.GitHubContributionCounter, "load_existing_data", lambda self, p: {}
    )
    monkeypatch.setattr(
        mod.GitHubContributionCounter, "save_contributors", lambda self, c, p: None
    )

    result = counter.process_repositories(str(config_path), output_path)

    # alice: 5 (core) + 2 + 4 (web_sites, anon mapped onto her) = 11 total.
    assert result["alice"]["thematics"]["core"] == 5
    assert result["alice"]["thematics"]["web_sites"] == 6
    assert result["alice"]["total_contributions"] == 11
    assert result["alice"]["has_github_account"] is True
    assert result["alice"]["avatar_url"] == "https://avatars/alice.png"

    # bob only contributed to core; other thematics are zero-filled.
    assert result["bob"]["thematics"] == {"core": 3, "web_sites": 0}
    assert result["bob"]["total_contributions"] == 3

    # Bot was filtered out everywhere.
    assert "dependabot[bot]" not in result
    # The mapped email identifier should not survive as its own contributor.
    assert "email:anon@example.com" not in result
    # Empty thematic produced no key.
    assert all("empty" not in c["thematics"] for c in result.values())


def test_process_repositories_keeps_unmapped_email_contributor(monkeypatch, tmp_path):
    config = {"repositories": {"web_sites": ["QGIS-Website"]}}
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(config))

    counter = make_counter(monkeypatch, email_mappings={})

    monkeypatch.setattr(
        mod.GitHubContributionCounter,
        "get_commits_with_authors",
        lambda self, owner, repo, branch="main": (
            {"no-github:legacy@example.com": 7} if branch == "main" else {}
        ),
    )
    monkeypatch.setattr(
        mod.GitHubContributionCounter, "load_existing_data", lambda self, p: {}
    )
    monkeypatch.setattr(
        mod.GitHubContributionCounter, "save_contributors", lambda self, c, p: None
    )

    result = counter.process_repositories(str(config_path), str(tmp_path / "out.json"))

    # Old "no-github:" prefix is normalized to "email:" and kept (no avatar).
    assert "email:legacy@example.com" in result
    entry = result["email:legacy@example.com"]
    assert entry["has_github_account"] is False
    assert entry["avatar_url"] == ""
    assert entry["total_contributions"] == 7


def test_process_repositories_missing_config_returns_empty(monkeypatch, tmp_path):
    counter = make_counter(monkeypatch)
    missing = str(tmp_path / "does_not_exist.json")
    assert counter.process_repositories(missing, str(tmp_path / "out.json")) == {}


# ---------------------------------------------------------------------------
# save_contributors: JSON shape + sort order (round-trips through tmp_path)
# ---------------------------------------------------------------------------
def test_save_contributors_sorts_and_shapes_output(monkeypatch, tmp_path):
    counter = make_counter(monkeypatch)
    output_path = str(tmp_path / "nested" / "contributors.json")

    contributors = {
        "low": {"login": "low", "avatar_url": "", "total_contributions": 1,
                "thematics": {"core": 1}, "has_github_account": True},
        "high": {"login": "high", "avatar_url": "", "total_contributions": 50,
                 "thematics": {"core": 50}, "has_github_account": True},
        "mid": {"login": "mid", "avatar_url": "", "total_contributions": 10,
                "thematics": {"core": 10}, "has_github_account": True},
    }

    counter.save_contributors(contributors, output_path)

    with open(output_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    assert data["total_contributors"] == 3
    assert "_automated_warning" in data
    assert "generated_at" in data
    # Sorted by total_contributions descending.
    logins = [c["login"] for c in data["contributors"]]
    assert logins == ["high", "mid", "low"]


# ---------------------------------------------------------------------------
# load_existing_data: list -> dict conversion keyed by login
# ---------------------------------------------------------------------------
def test_load_existing_data_converts_list_to_dict(monkeypatch, tmp_path):
    counter = make_counter(monkeypatch)
    existing = {
        "contributors": [
            {"login": "alice", "total_contributions": 5, "thematics": {}},
            {"login": "bob", "total_contributions": 2, "thematics": {}},
        ]
    }
    path = tmp_path / "contributors.json"
    path.write_text(json.dumps(existing))

    result = counter.load_existing_data(str(path))
    assert set(result.keys()) == {"alice", "bob"}
    assert result["alice"]["total_contributions"] == 5

    # Missing file -> empty dict (no crash).
    assert counter.load_existing_data(str(tmp_path / "nope.json")) == {}


# ---------------------------------------------------------------------------
# generate_geojson: feature shape, sorting, email skip, geometry matching
# ---------------------------------------------------------------------------
def test_generate_geojson_builds_sorted_features(monkeypatch, tmp_path):
    contributors = {
        "contributors": [
            {"login": "alice", "avatar_url": "a.png", "total_contributions": 3,
             "thematics": {"core": 3}, "has_github_account": True},
            {"login": "bob", "avatar_url": "b.png", "total_contributions": 30,
             "thematics": {"core": 30}, "has_github_account": True},
            {"login": "email:anon@example.com", "avatar_url": "",
             "total_contributions": 99, "thematics": {"core": 99},
             "has_github_account": False},
        ]
    }
    contributors_path = tmp_path / "contributors.json"
    contributors_path.write_text(json.dumps(contributors))

    # Location + honorary files live at module-relative hardcoded paths; the
    # function reads them via os.path.exists, so just make those return False
    # to keep the test isolated from the repo's real data directory.
    monkeypatch.setattr(mod.os.path, "exists", lambda p: p == str(contributors_path))

    out_path = tmp_path / "out" / "map.json"
    ok = mod.generate_geojson(str(contributors_path), str(out_path))
    assert ok is True

    with open(out_path, "r", encoding="utf-8") as fh:
        geo = json.load(fh)

    assert geo["type"] == "FeatureCollection"
    logins = [f["properties"]["login"] for f in geo["features"]]
    # email-based contributor skipped; remaining sorted by contributions desc.
    assert logins == ["bob", "alice"]
    # Thematics flattened onto properties; no geometry available -> None.
    bob = geo["features"][0]
    assert bob["properties"]["core"] == 30
    assert bob["geometry"] is None


def test_generate_geojson_missing_input_returns_false(monkeypatch, tmp_path):
    monkeypatch.setattr(mod.os.path, "exists", lambda p: False)
    assert mod.generate_geojson(
        str(tmp_path / "missing.json"), str(tmp_path / "out.json")
    ) is False
