# -*- coding: utf-8 -*-
"""Pytest configuration shared by the test suite.

Puts ``scripts/`` and the repository root on ``sys.path`` once, before any test
module is imported, so the utility scripts can be imported directly (e.g.
``import update_contributing_orgs`` or ``import fetch_feeds``) without per-test
path manipulation.
"""
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
# scripts/ lets the utility modules import by bare name; the repo root lets
# root-level scripts such as ``fetch_feeds`` import, including their
# ``from scripts.resize_image import resize_image`` dependency.
for path in (SCRIPTS_DIR, ROOT_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)
