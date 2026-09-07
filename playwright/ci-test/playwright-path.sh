#!/usr/bin/env bash
#
# Resolve how to invoke Playwright and make sure the dependencies are present.
# Sets $PLAYWRIGHT for the caller to use.
#
# Two supported environments:
#
#   * nix-shell (see shell.nix) -- provides a `playwright` binary plus a
#     matching browser bundle via PLAYWRIGHT_BROWSERS_PATH.
#   * plain Node -- falls back to `npx playwright` against node_modules.
#
# Dependencies are installed with `npm ci`, which honours package-lock.json.
# Never use `npm install @playwright/test@latest` here: the client version must
# stay in step with the browser revision pinned in shell.nix.

if command -v playwright >/dev/null 2>&1; then
    PLAYWRIGHT="playwright"
else
    if ! command -v npm >/dev/null 2>&1; then
        echo "❌ Neither 'playwright' nor 'npm' is available." >&2
        echo "   Enter the dev environment first: nix-shell (in this directory)." >&2
        return 1 2>/dev/null || exit 1
    fi
    if [[ ! -d node_modules ]]; then
        echo "📦 Installing pinned npm dependencies (npm ci)"
        npm ci
    fi
    PLAYWRIGHT="npx playwright"
fi

export PLAYWRIGHT
