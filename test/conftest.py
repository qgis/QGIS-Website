# -*- coding: utf-8 -*-
"""Pytest configuration shared by the test suite.

Puts ``scripts/`` on ``sys.path`` once, before any test module is imported,
so the utility scripts can be imported directly (e.g. ``import
update_contributing_orgs``) without per-test path manipulation.
"""
import os
import sys

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "..", "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)
