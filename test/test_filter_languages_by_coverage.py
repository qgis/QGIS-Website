# -*- coding: utf-8 -*-
"""Regression tests for scripts/i18n/filter_languages_by_coverage.py.

The tx-coverage workflow runs this script daily and commits the result, so the
config it writes has to stay on Hugo's current keys (``locale`` and the
``sites.matrix`` mount sub-table) and it has to keep recognising the blocks it
owns. A mount block now contains a ``[module.mounts.sites.matrix]`` header of
its own, which a naive "block ends at the next [" rule would treat as the start
of something else, leaving demoted languages mounted forever.
"""
import importlib.util
import os

import pytest

_SCRIPT = os.path.join(
    os.path.dirname(__file__), "..", "scripts", "i18n",
    "filter_languages_by_coverage.py",
)
_spec = importlib.util.spec_from_file_location("filter_languages_by_coverage", _SCRIPT)
flbc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(flbc)


def _mounts(lang):
    return (
        '  [[module.mounts]]\n'
        f'    source = "content-translated/{lang}"\n'
        '    target = "content"\n'
        '    [module.mounts.sites.matrix]\n'
        f'      languages = ["{lang}"]\n'
        '  [[module.mounts]]\n'
        '    source = "content"\n'
        '    target = "content"\n'
        '    [module.mounts.sites.matrix]\n'
        f'      languages = ["{lang}"]\n'
    )


def _config(langs=("en", "nl")):
    """A config.toml in the shape the site uses after the Hugo key migration."""
    head = "baseURL = 'https://qgis.org/'\nlocale = 'en-us'\n\n  [languages]\n"
    for lang in langs:
        head += (
            f'    [languages.{lang}]\n'
            f'    locale = "{lang}"\n'
            '    weight = 2\n'
            f'    contentDir = "content-translated/{lang}"\n\n'
        )
    body = "[module]\n"
    for lang in langs:
        body += _mounts(lang)
    return head + body


def _sync(text, coverage, threshold=35.0, all_langs=("en", "nl", "de")):
    return flbc.sync_config(text, dict(coverage), threshold, list(all_langs))


def test_demoted_language_loses_its_language_block_and_both_mounts():
    """The teeth: a mount block owns a sub-table, so it must still be found."""
    text, kept, added, removed = _sync(_config(), {"en": 100.0, "nl": 10.0})

    assert removed == ["nl"]
    assert kept == ["en"]
    assert "[languages.nl]" not in text
    assert "content-translated/nl" not in text
    assert text.count("[[module.mounts]]") == 2, "en's two mounts should survive"
    assert text.count('languages = ["nl"]') == 0


def test_promoted_language_is_written_with_current_hugo_keys():
    text, _kept, added, _removed = _sync(_config(), {"en": 100.0, "nl": 90.0, "de": 80.0})

    assert added == ["de"]
    assert 'locale = "de"' in text
    assert '[module.mounts.sites.matrix]\n      languages = ["de"]' in text
    assert "languageCode" not in text, "deprecated in Hugo 0.158"
    assert 'lang = "de"' not in text, "deprecated in Hugo 0.153"


def test_a_promote_and_demote_in_one_run_leaves_a_consistent_config():
    text, kept, added, removed = _sync(_config(), {"en": 100.0, "nl": 5.0, "de": 80.0})

    assert added == ["de"] and removed == ["nl"] and kept == ["de", "en"]
    assert text.count("[[module.mounts]]") == 4, "two languages, two mounts each"
    assert "content-translated/nl" not in text
    assert "content-translated/de" in text


def test_always_included_language_survives_zero_coverage():
    text, kept, _added, removed = _sync(_config(), {"en": 0.0, "nl": 0.0})

    assert kept == ["en"] and removed == ["nl"]
    assert "[languages.en]" in text


def test_legacy_lang_key_is_still_recognised_for_removal():
    """A hand-edited config on the old syntax must not go uncleaned."""
    legacy = (
        "  [languages]\n"
        '    [languages.en]\n    locale = "en"\n\n'
        '    [languages.nl]\n    locale = "nl"\n\n'
        "[module]\n"
        "  [[module.mounts]]\n"
        '    source = "content-translated/nl"\n'
        '    target = "content"\n'
        '    lang = "nl"\n'
    )
    text, _kept, _added, removed = _sync(legacy, {"en": 100.0, "nl": 1.0})

    assert removed == ["nl"]
    assert "content-translated/nl" not in text


def test_written_config_is_parseable_and_mounts_match_languages():
    try:
        import tomllib
    except ModuleNotFoundError:  # Python 3.10
        tomllib = pytest.importorskip("tomli")

    text, kept, _added, _removed = _sync(_config(), {"en": 100.0, "nl": 90.0, "de": 80.0})
    parsed = tomllib.loads(text)

    assert sorted(parsed["languages"]) == sorted(kept)
    mounted = {
        m["sites"]["matrix"]["languages"][0]
        for m in parsed["module"]["mounts"]
    }
    assert mounted == set(kept)
