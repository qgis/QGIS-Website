#!/usr/bin/env bash
set -euo pipefail

# Incremental multilingual build: builds en first, then each language one-by-one.
# After each language build, identical files are replaced with links to en.
# This keeps peak disk usage low.

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT_DIR}"

PUBLIC_DIR="${PUBLIC_DIR:-public_prod}"
CONFIG_MAIN="${CONFIG_MAIN:-${ROOT_DIR}/config.toml}"
CONFIG_PROD="${CONFIG_PROD:-${ROOT_DIR}/config/config.prod.toml}"
BASE_LANG="${BASE_LANG:-en}"
BASE_IN_SUBDIR="${BASE_IN_SUBDIR:-false}"
LINK_MODE="${LINK_MODE:-symlink}" # symlink|hardlink
DEDUP_DRY_RUN="${DEDUP_DRY_RUN:-false}" # true to preview dedup actions
TMP_DIR="${TMP_DIR:-$(mktemp -d "${ROOT_DIR}/.tmp_langs.XXXXXX")}" || true

# Optional debug tracing (macOS bash 3.2 friendly)
DEBUG="${DEBUG:-0}"
case "${DEBUG}" in
  1|true|TRUE|yes|YES) set -x ;;
esac

cleanup() {
  rm -rf "${TMP_DIR}" || true
}
trap cleanup EXIT

echo "Reading languages from ${CONFIG_MAIN} ..."
lang_list_file="${TMP_DIR}/langs.txt"
# Robust extraction for macOS: use POSIX sed to capture language code
sed -nE 's/^[[:space:]]*\[languages\.([A-Za-z0-9_-]+)\][[:space:]]*$/\1/p' "${CONFIG_MAIN}" >"${lang_list_file}" || true
# Full language set from config
FULL_LANGS=()
while IFS= read -r l; do
  [[ -n "$l" ]] && FULL_LANGS+=("$l")
done <"${lang_list_file}"

if [[ ${#FULL_LANGS[@]} -eq 0 ]]; then
  echo "ERROR: No languages found in ${CONFIG_MAIN}" >&2
  exit 1
fi

# Determine iteration set: allow restricting languages via LANGS="nl,de,fr"
ITER_LANGS=()
if [[ -n "${LANGS:-}" ]]; then
  # Special keywords: all or *
  case "${LANGS}" in
    all|ALL)
      ITER_LANGS=("${FULL_LANGS[@]}")
      ;;
    *)
  oldIFS="$IFS"; IFS=','
  for f in $LANGS; do
    [[ -n "$f" ]] && ITER_LANGS+=("$f")
  done
  IFS="$oldIFS"
      ;;
  esac
else
  # Default: iterate over all languages from config
  ITER_LANGS=("${FULL_LANGS[@]}")
fi

echo "Languages (iter): ${ITER_LANGS[*]}"
echo "Base: ${BASE_LANG}  PublishDir: ${PUBLIC_DIR}  LinkMode: ${LINK_MODE}  BaseInSubdir: ${BASE_IN_SUBDIR}  DedupDryRun: ${DEDUP_DRY_RUN}"

# Compute progress counters (exclude base language)
REMAINING_LANGS=()
for l in "${ITER_LANGS[@]}"; do
  if [[ "$l" != "${BASE_LANG}" ]]; then
    REMAINING_LANGS+=("$l")
  fi
done
TOTAL_LANGS=${#REMAINING_LANGS[@]}
DONE_LANGS=0
echo "Total languages to build (excluding base): ${TOTAL_LANGS}"

have_lang() {
  local x=$1; shift
  for y in "$@"; do [[ "$x" == "$y" ]] && return 0; done
  return 1
}

write_tmp_cfg() {
  local allow=("$@")
  local tmp_cfg="$TMP_DIR/langs.toml"
  local disabled=()
  for l in "${FULL_LANGS[@]}"; do
    if ! have_lang "$l" "${allow[@]}"; then
      disabled+=("\"$l\"")
    fi
  done
  {
    echo "defaultContentLanguage = '${BASE_LANG}'"
    echo "defaultContentLanguageInSubdir = false"
    echo -n "disableLanguages = ["
    if [[ ${#disabled[@]} -gt 0 ]]; then
      (IFS=','; echo -n "${disabled[*]}")
    fi
    echo "]"
  } >"$tmp_cfg"
  if [[ "${DEBUG}" == "1" || "${DEBUG}" == "true" || "${DEBUG}" == "TRUE" ]]; then
    {
      echo "--- Generated overlay config: $tmp_cfg";
      cat "$tmp_cfg";
      echo "---";
    } >&2
  fi
  echo "$tmp_cfg"
}

build_step() {
  local clean="$1"; shift
  local cfg_tmp="$1"; shift
  echo "Running hugo (clean=${clean}) with overlay: ${cfg_tmp}"
  if [[ "$clean" == "true" ]]; then
    hugo --config "${CONFIG_MAIN},${CONFIG_PROD},${cfg_tmp}" --cleanDestinationDir --destination "${PUBLIC_DIR}"
  else
    hugo --config "${CONFIG_MAIN},${CONFIG_PROD},${cfg_tmp}" --cleanDestinationDir=false --destination "${PUBLIC_DIR}"
  fi
  if command -v du >/dev/null 2>&1; then
    echo "Current size of ${PUBLIC_DIR}:"; du -sh "${PUBLIC_DIR}" 2>/dev/null || true
  fi
}

dedup_step() {
  echo "Deduplicating ${PUBLIC_DIR} (mode=${LINK_MODE}) ..."
  python3 "${ROOT_DIR}/scripts/dedup_public.py" \
    --public-dir "${PUBLIC_DIR}" \
    --config "${CONFIG_MAIN}" \
    --base-lang "${BASE_LANG}" \
    $( [[ "${BASE_IN_SUBDIR}" == "true" ]] && echo "--base-lang-in-subdir" ) \
    --mode "${LINK_MODE}" \
    $( [[ "${DEDUP_DRY_RUN}" == "true" ]] && echo "--dry-run" )
}

# 1) Build base language only (clean)
cfg=$(write_tmp_cfg "${BASE_LANG}")
build_step true "$cfg"
echo "Base language '${BASE_LANG}' built. Progress: ${DONE_LANGS}/${TOTAL_LANGS}"

# 2) Dedup (no-op, but keeps flow consistent)
dedup_step

# 3) Build each other language incrementally and dedup after each
for lang in "${ITER_LANGS[@]}"; do
  [[ "$lang" == "$BASE_LANG" ]] && continue
  cfg=$(write_tmp_cfg "${BASE_LANG}" "$lang")
  build_step false "$cfg"
  dedup_step
  DONE_LANGS=$((DONE_LANGS + 1))
  echo "==== Completed language: $lang. Progress: ${DONE_LANGS}/${TOTAL_LANGS} ===="
done

echo "All languages built incrementally into ${PUBLIC_DIR}."


