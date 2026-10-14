# -*- coding: utf-8 -*-
"""Every outbound request in the harvesters must carry a timeout.

The scripts here run unattended from scheduled workflows. ``requests`` has no
default timeout, so one stalled server holds the job open until the runner is
killed, and the data files it was meant to refresh go stale without anyone
being told.

This reads the sources rather than making any call, so it also covers the
branches an offline test suite cannot reach.
"""
import ast
import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(ROOT, "scripts")

# requests methods that open a connection.
VERBS = {"get", "post", "head", "put", "patch", "delete", "request"}


def _python_sources():
    paths = [os.path.join(ROOT, "fetch_feeds.py")]
    for name in sorted(os.listdir(SCRIPTS_DIR)):
        if name.endswith(".py"):
            paths.append(os.path.join(SCRIPTS_DIR, name))
    return [p for p in paths if os.path.isfile(p)]


def _requests_calls(tree):
    """Yield (lineno, verb) for direct ``requests.<verb>(...)`` calls.

    Calls made through a Session object are not matched; those are checked by
    the test below instead.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not isinstance(func, ast.Attribute) or func.attr not in VERBS:
            continue
        if isinstance(func.value, ast.Name) and func.value.id == "requests":
            yield node, func.attr


def _has_timeout(call):
    if any(kw.arg == "timeout" for kw in call.keywords):
        return True
    # **kwargs could carry it, so do not fail a call that forwards them.
    return any(kw.arg is None for kw in call.keywords)


@pytest.mark.parametrize("path", _python_sources(), ids=os.path.basename)
def test_requests_calls_pass_a_timeout(path):
    with open(path, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=path)

    missing = [
        f"{os.path.relpath(path, ROOT)}:{call.lineno} requests.{verb}()"
        for call, verb in _requests_calls(tree)
        if not _has_timeout(call)
    ]

    assert not missing, "outbound request with no timeout: " + ", ".join(missing)


def test_the_scan_actually_finds_calls():
    """Guard the guard: a scan that matches nothing would pass silently."""
    found = 0
    for path in _python_sources():
        with open(path, encoding="utf-8") as f:
            found += sum(1 for _ in _requests_calls(ast.parse(f.read())))

    assert found >= 10, f"only {found} requests calls seen, the matcher is too narrow"


def test_session_calls_pass_a_timeout():
    """Session.head in the link sanitizer is the one non-module call site."""
    path = os.path.join(SCRIPTS_DIR, "sanitize_commercial_supports.py")
    with open(path, encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=path)

    sessions = {
        t.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and isinstance(node.value, ast.Call)
        and isinstance(node.value.func, ast.Attribute)
        and node.value.func.attr == "Session"
        for t in node.targets
        if isinstance(t, ast.Name)
    }
    assert sessions, "no requests.Session() found, this test needs updating"

    missing = [
        f"{node.func.attr}() at line {node.lineno}"
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in VERBS
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id in sessions
        and not _has_timeout(node)
    ]

    assert not missing, "session request with no timeout: " + ", ".join(missing)
