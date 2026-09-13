# QGIS Website – Development and Production Build Guide

This document explains how to run the site in development with minimal disk usage and how to produce optimized production builds with post-build media deduplication.

## Dev workflow (en + nl + ro)

Purpose: keep `public*` small during local development and speed up iterations.

- Dev config overlay: `config/config.dev.toml`
  - Builds English, Dutch and Romanian locally
  - Serves from memory (no massive disk writes)
  - Publishes to `public_dev` (if you force write)

Run the dev server:

```bash
hugo server --config config.toml,config/config.dev.toml
```

Notes:
- Default language is `en`, Dutch (`nl`) and Romanian (`ro`) are enabled; all other languages are disabled.
- The server keeps output in memory (`renderToDisk = false`). If you need files on disk, temporarily set it to `true`.

## Production workflow (per-language incremental with media dedup)

We avoid exploding disk usage by building languages incrementally and deduplicating only media across languages using links.

### Key scripts

- `scripts/build_prod_per_lang.sh`
  - Builds base language first, then each language one-by-one with `disableLanguages` overlay.
  - After each build step, runs `scripts/dedup_public.py` to replace identical media files with links to the base copy.
  - By default, links are symlinks. You can switch to hardlinks if your hosting platform disallows symlinks.

- `scripts/dedup_public.py`
  - Scans the publish directory, hashes files, and replaces duplicates with links to their canonical copy in the base language tree.
  - By default, it deduplicates only media file types (images, video, audio, PDFs/graphics formats). It does not touch MD/HTML/CSS/JS.
  - Flags:
    - `--mode symlink|hardlink` — link type (default: `symlink`)
    - `--ext "png,jpg,webp,pdf,..."` — custom comma-separated list of extensions; `*` to dedupe all file types.
    - `--dry-run` — report actions without touching files.

### Typical production build

Build only English + one language at a time, dedup after each step, write into `public_prod`:

```bash
# Clean any previous artifact first
rm -rf public_prod

# Build EN first (clean), then NL (incremental), dedup media via hardlinks
PUBLIC_DIR=public_prod \
LANGS=nl \
LINK_MODE=hardlink \
bash scripts/build_prod_per_lang.sh
```

Options:
- Limit to a set of languages:
```bash
LANGS=nl,de,fr bash scripts/build_prod_per_lang.sh
```
- All languages from config:
```bash
LANGS=all bash scripts/build_prod_per_lang.sh
```
- Use symlinks (default):
```bash
LINK_MODE=symlink bash scripts/build_prod_per_lang.sh
```
- If your default content language is rendered under its own subdirectory in production, set:
```bash
BASE_IN_SUBDIR=true bash scripts/build_prod_per_lang.sh
```

### Verifying deduplication

- Check that files under a non-base language (e.g., `public_prod/nl/...`) are links:
```bash
find public_prod/nl -type l | head -n 20 | xargs -I{} sh -c 'ls -l "{}"; readlink "{}"'
```
- For hardlinks, confirm identical inodes:
```bash
stat -f '%i %N' public_prod/nl/path/to/file.png public_prod/path/to/file.png
```

### Direct dedup invocation (optional)

If you built the whole site at once and only want to deduplicate media afterwards:

```bash
python3 scripts/dedup_public.py --public-dir public_prod --mode hardlink
```

Use `--dry-run` for a preview:
```bash
python3 scripts/dedup_public.py --public-dir public_prod --dry-run
```


## Troubleshooting

- The build produced all languages (huge output): ensure you passed `LANGS=...` and that the overlay config is being picked up. The script prints a summary of languages and the generated overlay.
- No links created: ensure you’re not running with `--dry-run`. If you chose `hardlink`, links will not show arrows in `ls -l`; use `stat` to check inodes.
- Dedup skipped non-media: this is expected. Pass `--ext "*"` to dedupe any file type, or provide a custom list.

---
Maintainers: see `config/config.dev.toml` for dev-only settings and `config/config.prod.toml` for production publish directory.
