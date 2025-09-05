#!/usr/bin/env bash
set -euo pipefail

# Incremental multilingual build with post-build deduplication via links.
# Requirements: Python 3, scripts/dedup_public.py

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC_DIR="${PUBLIC_DIR:-public_prod}"
CONFIG_MAIN="${CONFIG_MAIN:-${ROOT_DIR}/config.toml}"
CONFIG_PROD="${CONFIG_PROD:-${ROOT_DIR}/config/config.prod.toml}"
BASE_LANG="${BASE_LANG:-en}"
BASE_IN_SUBDIR="${BASE_IN_SUBDIR:-false}"
LINK_MODE="${LINK_MODE:-symlink}" # symlink|hardlink

cd "${ROOT_DIR}"

echo "Building all languages at once into ${PUBLIC_DIR} ..."
hugo --config "${CONFIG_MAIN},${CONFIG_PROD}" --cleanDestinationDir

echo "Post-build deduplication in ${PUBLIC_DIR} ..."
python3 "${ROOT_DIR}/scripts/dedup_public.py" \
  --public-dir "${PUBLIC_DIR}" \
  --config "${CONFIG_MAIN}" \
  --base-lang "${BASE_LANG}" \
  $( [ "${BASE_IN_SUBDIR}" = "true" ] && echo "--base-lang-in-subdir" ) \
  --mode "${LINK_MODE}"

echo "Done."


