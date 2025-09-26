#!/usr/bin/env python3
import argparse
import hashlib
import os
import re
import sys
from pathlib import Path


def sha256_file(path: Path, buf_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        while True:
            data = f.read(buf_size)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


def parse_languages_from_config(config_path: Path) -> set[str]:
    langs: set[str] = set()
    if not config_path.exists():
        return langs
    lang_re = re.compile(r"^\s*\[languages\.([A-Za-z0-9_-]+)\]")
    with config_path.open('r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = lang_re.match(line)
            if m:
                langs.add(m.group(1).lower())
    return langs


def should_skip_dir(path: Path, base_dir: Path, language_dirs: set[str], base_lang_subdir: bool, base_lang: str) -> bool:
    if path == base_dir:
        return False
    # Skip known language top-level directories when base is root
    if not base_lang_subdir and path.parent == base_dir and path.is_dir():
        name = path.name.lower()
        if name in language_dirs:
            return True
    return False


def collect_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dp = Path(dirpath)
        for filename in filenames:
            p = dp / filename
            if p.is_symlink():
                # Leave existing symlinks as-is
                continue
            if p.is_file():
                files.append(p)
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description='Deduplicate Hugo public dir by replacing identical files across languages with links to base language files.')
    parser.add_argument('--public-dir', default='public_prod', help='Hugo publishDir to process (default: public_prod)')
    parser.add_argument('--config', default='config.toml', help='Path to main Hugo config.toml (for language detection)')
    parser.add_argument('--base-lang', default='en', help='Base language code (default: en)')
    parser.add_argument('--base-lang-in-subdir', action='store_true', help='Set if defaultContentLanguageInSubdir=true (base language under its own subdir)')
    parser.add_argument('--mode', choices=['symlink', 'hardlink'], default='symlink', help='Link mode to use for duplicates (default: symlink)')
    parser.add_argument('--ext', default='png,jpg,jpeg,webp,avif,gif,svg,bmp,tif,tiff,ico,apng,heic,mp4,webm,ogv,mov,m4v,mp3,ogg,oga,wav,flac,m4a,pdf,psd,ai,eps',
                        help='Comma-separated list of file extensions to dedupe (no dots). Use "*" to dedupe all files. Default: common media types')
    parser.add_argument('--dry-run', action='store_true', help='Only report actions without modifying files')

    args = parser.parse_args()

    public_dir = Path(args.public_dir).resolve()
    if not public_dir.exists():
        print(f"ERROR: Public dir not found: {public_dir}", file=sys.stderr)
        return 1

    config_path = Path(args.config).resolve()
    langs = parse_languages_from_config(config_path)

    # Determine base area
    base_root: Path
    if args.base_lang_in_subdir:
        base_root = public_dir / args.base_lang
        if not base_root.exists():
            print(f"ERROR: Base language subdir not found: {base_root}", file=sys.stderr)
            return 1
    else:
        base_root = public_dir

    # Build a set of language top-level directories present in public
    present_lang_dirs: set[str] = set()
    for entry in public_dir.iterdir():
        if entry.is_dir():
            name = entry.name.lower()
            if name in langs or '-' in name or '_' in name:
                present_lang_dirs.add(name)

    # Prepare extension filter
    allowed_exts: set[str] | None
    if args.ext.strip() == '*':
        allowed_exts = None
    else:
        allowed_exts = set()
        for e in args.ext.split(','):
            e = e.strip().lower()
            if not e:
                continue
            if not e.startswith('.'):
                e = '.' + e
            allowed_exts.add(e)

    def is_allowed(path: Path) -> bool:
        if allowed_exts is None:
            return True
        return path.suffix.lower() in allowed_exts

    # Pass 1: index base files
    canonical_by_hash: dict[str, Path] = {}
    base_excluded: set[Path] = set()
    if not args.base_lang_in_subdir:
        # Exclude known language directories at top-level
        for entry in public_dir.iterdir():
            if should_skip_dir(entry, public_dir, present_lang_dirs, args.base_lang_in_subdir, args.base_lang):
                base_excluded.add(entry)

    base_files: list[Path] = []
    if args.base_lang_in_subdir:
        base_files = [p for p in collect_files(base_root) if is_allowed(p)]
    else:
        for dirpath, dirnames, filenames in os.walk(public_dir):
            dp = Path(dirpath)
            # Skip language top-level dirs
            if dp in base_excluded:
                dirnames[:] = []
                continue
            for filename in filenames:
                p = dp / filename
                if p.is_symlink() or not p.is_file():
                    continue
                if is_allowed(p):
                    base_files.append(p)

    for p in base_files:
        try:
            h = sha256_file(p)
        except Exception as e:
            print(f"WARN: Failed to hash {p}: {e}")
            continue
        canonical_by_hash.setdefault(h, p)

    # Pass 2: deduplicate other files
    processed = 0
    linked = 0
    skipped_diff = 0
    for dirpath, dirnames, filenames in os.walk(public_dir):
        dp = Path(dirpath)
        for filename in filenames:
            p = dp / filename
            if p.is_symlink() or not p.is_file():
                continue
            if not is_allowed(p):
                continue
            # Skip if this is the canonical copy
            try:
                h = sha256_file(p)
            except Exception as e:
                print(f"WARN: Failed to hash {p}: {e}")
                continue
            canonical = canonical_by_hash.get(h)
            if canonical is None:
                # Not seen before; register as canonical
                canonical_by_hash[h] = p
                continue
            if canonical == p:
                continue

            # Replace with link to canonical
            rel_target = os.path.relpath(canonical, start=p.parent)
            if args.dry_run:
                print(f"DRY-RUN: replace {p} -> link to {rel_target}")
            else:
                try:
                    p.unlink()
                    if args.mode == 'symlink':
                        os.symlink(rel_target, p)
                    else:
                        os.link(canonical, p)
                    linked += 1
                except Exception as e:
                    print(f"ERROR: Failed to link {p} -> {rel_target}: {e}", file=sys.stderr)
                    # If linking fails, leave file as-is
            processed += 1

    print(f"Dedup complete. processed={processed} linked={linked} unique={len(canonical_by_hash)} base={base_root}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


