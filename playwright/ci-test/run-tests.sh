#!/usr/bin/env bash
#
# Run the Playwright end-to-end suite against a freshly built copy of the site.
#
# Mirrors .github/workflows/playwright-e2e.yml: build with Hugo pinned to the
# test base URL, serve the output statically, run the suite, tear the server
# down again.
#
# Any arguments are passed straight through to `playwright test`, so:
#
#   ./run-tests.sh                       # headless, whole suite
#   ./run-tests.sh --ui                  # interactive UI mode
#   ./run-tests.sh tests/01-home-page.spec.ts
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PORT="${PLAYWRIGHT_TEST_PORT:-1313}"
BASE_URL="http://127.0.0.1:${PORT}"

cd "$HERE"
# shellcheck source=playwright-path.sh
source ./playwright-path.sh

if ! command -v hugo >/dev/null 2>&1; then
    echo "❌ hugo not found. Run this from 'nix develop' at the repo root." >&2
    exit 1
fi

echo "🏗️  Building the site for ${BASE_URL}"
( cd "$ROOT" && rm -f .hugo_build.lock && hugo --gc --config ./config.toml -b "$BASE_URL" --quiet )

server_pid=""
cleanup() {
    if [[ -n "$server_pid" ]] && kill -0 "$server_pid" 2>/dev/null; then
        echo "🧹 Stopping test server (pid ${server_pid})"
        kill "$server_pid" 2>/dev/null || true
        wait "$server_pid" 2>/dev/null || true
    fi
}
trap cleanup EXIT INT TERM

echo "🌐 Serving ${ROOT}/public on port ${PORT}"
( cd "$ROOT/public" && exec python3 -m http.server "$PORT" ) >/dev/null 2>&1 &
server_pid=$!

for _ in $(seq 1 30); do
    if curl -sf -o /dev/null "$BASE_URL/"; then break; fi
    sleep 0.5
done
if ! curl -sf -o /dev/null "$BASE_URL/"; then
    echo "❌ Test server did not come up on ${BASE_URL}" >&2
    exit 1
fi

echo "🎭 Running Playwright suite"
# shellcheck disable=SC2086
$PLAYWRIGHT test --project chromium "$@"
