#!/usr/bin/env python3
"""Restore corrupted Hugo shortcode names and technical content in translated .po files.

When translators translate a paragraph that contains a Hugo shortcode tag
(e.g. {{< rich-box-end >}}), the shortcode *name* can get accidentally
translated too — for example, Swedish "end" = "slut" turns
{{< rich-box-end >}} into {{< rich-box-slut >}}, which breaks Hugo builds.

Additionally, translators may translate technical content like:
- File paths in ref shortcodes: {{< ref "community/groups.md" >}}
- Parameter values: showcase="map", columns="gallery", class="rounded"
- URL segments and technical identifiers

This script:
  1. Collects all valid shortcode names from the theme's shortcodes directory.
  2. Scans every translated .po file under translations/.
  3. For each msgid/msgstr pair:
     a. Fixes shortcode names that were translated
     b. Restores file paths in ref shortcodes from msgid
     c. Restores technical parameter values (showcase, columns, class, etc.)
  4. Writes back any modified .po files using polib, which guarantees
     correct PO escaping and syntax.

Run this after 'make txpull' and before 'make messages-compile'.
It is called automatically by 'make txpull'.

Usage:
    python3 scripts/i18n/sanitize_shortcodes.py [--translations DIR] [--themes DIR] [--dry-run]
"""
import argparse
import glob
import os
import re
import sys
from pathlib import Path

try:
    import polib
except ImportError:
    print("ERROR: polib is required. Install with: pip install polib", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Hugo shortcode tag pattern — matches both {{< name ... >}} and {{% name %}}
# Operates on plain (unescaped) strings as delivered by polib.
# Updated to match Unicode characters (including Cyrillic, Chinese, etc.) for corrupted shortcodes
# ---------------------------------------------------------------------------
SHORTCODE_RE = re.compile(
    r'(\{\{(?:<|%)[ \t]*)(/?)(\w+[\w-]*)((?:[^>%]|>(?!\}\})|%(?!\}\}))*?)(>|%)(\}\})',
    re.DOTALL | re.UNICODE,
)


def get_valid_shortcodes(themes_dir: str) -> set[str]:
    """Return every shortcode name found in the theme layouts."""
    names: set[str] = set()
    pattern = os.path.join(themes_dir, '**', 'layouts', 'shortcodes', '*.html')
    for path in glob.glob(pattern, recursive=True):
        names.add(os.path.splitext(os.path.basename(path))[0])
    return names


def list_shortcodes(text: str) -> list[tuple]:
    """Return ordered list of (match_obj, slash, name) for all shortcode tags in text."""
    return [(m, m.group(2), m.group(3)) for m in SHORTCODE_RE.finditer(text)]


def restore_names(msgid: str, msgstr: str, valid: set[str]) -> tuple[str, list[str]]:
    """Fix invalid shortcode names in msgstr using positions from msgid.

    Operates on plain unescaped strings as provided by polib — no manual
    PO escaping needed here; polib handles that on save.

    Returns (new_msgstr, list_of_fixes). If no changes, new == old.
    """
    id_shortcodes = list_shortcodes(msgid)
    if not id_shortcodes:
        return msgstr, []

    result = msgstr
    fixes: list[str] = []
    offset = 0  # tracks displacement from previous in-place replacements

    for i, m in enumerate(SHORTCODE_RE.finditer(msgstr)):
        name = m.group(3)
        if name in valid:
            continue
        if i >= len(id_shortcodes):
            continue  # more shortcodes in msgstr than msgid — leave alone
        correct_name = id_shortcodes[i][2]  # Now index 2 is the name
        if correct_name == name:
            continue

        # Get the correct shortcode from msgid (includes all its params)
        id_shortcode_match = id_shortcodes[i][0]  # Now index 0 is the match object
        params_from_msgid = id_shortcode_match.group(4)  # params from source
        params_from_msgstr = m.group(4)  # params from translation
        
        # Check if params look like translated text (not key="value" syntax)
        # If params contain non-ASCII and no "=" signs, they're probably part of translated shortcode name
        has_param_syntax = '=' in params_from_msgstr
        has_non_ascii = any(ord(c) > 127 for c in params_from_msgstr)
        
        if has_non_ascii and not has_param_syntax and params_from_msgstr.strip():
            # Translated shortcode name had spaces - use params from msgid instead
            new_tag = m.group(1) + m.group(2) + correct_name + params_from_msgid + m.group(5) + m.group(6)
            fixes.append(f'{name!r} (with translated params) → {correct_name!r}')
        else:
            # Normal case - just fix the name, keep the params
            new_tag = m.group(1) + m.group(2) + correct_name + m.group(4) + m.group(5) + m.group(6)
            fixes.append(f'{name!r} → {correct_name!r}')
        
        start = m.start() + offset
        end = m.end() + offset
        result = result[:start] + new_tag + result[end:]
        offset += len(new_tag) - len(m.group(0))

    return result, fixes


def restore_technical_content(msgid: str, msgstr: str) -> tuple[str, list[str]]:
    """
    Restore technical content like file paths, parameter values, and class names
    from msgid to msgstr. This catches translated content that should remain technical.
    
    Returns (new_msgstr, list_of_fixes).
    """
    result = msgstr
    fixes: list[str] = []
    
    # Pattern for ref shortcodes with file paths
    ref_pattern = r'\{\{<\s*ref\s+"([^"]+)"\s*>\}\}'
    
    msgid_refs = [m.group(1) for m in re.finditer(ref_pattern, msgid)]
    msgstr_refs = list(re.finditer(ref_pattern, msgstr))
    
    # Restore file paths in ref shortcodes (they should never be translated)
    offset = 0
    for i, m in enumerate(msgstr_refs):
        if i >= len(msgid_refs):
            break
        translated_path = m.group(1)
        correct_path = msgid_refs[i]
        
        # Clean up corrupted paths that have Markdown link syntax embedded
        # e.g., "/funding/[donate.md](http://donate.md)" → should use correct_path
        cleaned_path = re.sub(r'/\[([^\]]+)\]\([^)]+\)', r'/\1', translated_path)
        
        # Check if path was translated or corrupted (contains non-ASCII, doesn't match, or was cleaned)
        if translated_path != correct_path or cleaned_path != translated_path:
            new_ref = '{{< ref "' + correct_path + '" >}}'
            start = m.start() + offset
            end = m.end() + offset
            result = result[:start] + new_ref + result[end:]
            offset += len(new_ref) - len(m.group(0))
            fixes.append(f'ref: "{translated_path}" → "{correct_path}"')
    
    # Pattern for shortcode parameters that should not be translated
    # These are technical values like showcase="map", columns="gallery", class="rounded"
    # Note: 'title' and 'subtitle' are user-facing content and SHOULD be translated
    # Note: 'tab1'-'tab4' are handled separately to preserve only Hugo variables (|var|)
    technical_params = {
        'showcase', 'columns', 'id', 'class', 'layoutClass', 
        'themeClass', 'link', 'icon', 'platform', 'mode'
    }
    
    # Tab parameters need special handling: preserve Hugo template variables |var|
    # but allow surrounding text to be translated
    tab_params = {'tab1', 'tab2', 'tab3', 'tab4'}
    
    # Extract shortcodes from msgid to get correct parameter values
    msgid_shortcodes = list(SHORTCODE_RE.finditer(msgid))
    msgstr_shortcodes = list(SHORTCODE_RE.finditer(result))
    
    # For each shortcode, check if technical parameters were translated
    for i, sc_msgid in enumerate(msgid_shortcodes):
        if i >= len(msgstr_shortcodes):
            break
            
        sc_msgstr = msgstr_shortcodes[i]
        
        # Only process if it's the same shortcode type
        if sc_msgid.group(3) != sc_msgstr.group(3):
            continue
        
        params_content_id = sc_msgid.group(4)
        params_content_str = sc_msgstr.group(4)
        
        # Find all parameter="value" pairs
        param_pattern = r'(\w+)="([^"]*)"'
        params_id = dict(re.findall(param_pattern, params_content_id))
        params_str = dict(re.findall(param_pattern, params_content_str))
        
        # Restore technical parameters that were translated
        for param_name in technical_params:
            if param_name in params_id and param_name in params_str:
                correct_value = params_id[param_name]
                translated_value = params_str[param_name]
                
                # Check if value was translated (contains non-ASCII or doesn't match)
                if translated_value != correct_value:
                    # Only fix if it looks like it was translated (contains non-ASCII)
                    if any(ord(c) > 127 for c in translated_value):
                        old_param = f'{param_name}="{translated_value}"'
                        new_param = f'{param_name}="{correct_value}"'
                        
                        # Replace only within this specific shortcode's parameter section
                        sc_start = sc_msgstr.start(4)
                        sc_end = sc_msgstr.end(4)
                        before = result[:sc_start]
                        sc_params = result[sc_start:sc_end]
                        after = result[sc_end:]
                        
                        if old_param in sc_params:
                            sc_params = sc_params.replace(old_param, new_param, 1)
                            result = before + sc_params + after
                            fixes.append(f'param {param_name}: "{translated_value}" → "{correct_value}"')
                            
                            # Refresh the shortcode matches after modification
                            msgstr_shortcodes = list(SHORTCODE_RE.finditer(result))
        
        # Special handling for tab parameters: preserve only Hugo template variables |var|
        for param_name in tab_params:
            if param_name in params_id and param_name in params_str:
                value_id = params_id[param_name]
                value_str = params_str[param_name]
                
                # Find all Hugo template variables (inside |...|) in the source
                pipe_pattern = r'\|[^|]+\|'
                variables_in_source = re.findall(pipe_pattern, value_id)
                
                if variables_in_source and value_id != value_str:
                    # Restore Hugo variables from source while keeping translated text
                    new_value = value_str
                    
                    # For each |variable| in source, ensure it exists in translation
                    for var in variables_in_source:
                        if var not in new_value:
                            # Variable was translated/corrupted, restore all variables from source
                            # Extract all |...| patterns from both source and translation
                            vars_in_translation = re.findall(pipe_pattern, value_str)
                            
                            # If count matches, replace each translated var with source var
                            if len(vars_in_translation) == len(variables_in_source):
                                new_value = value_str
                                for src_var, trans_var in zip(variables_in_source, vars_in_translation):
                                    if src_var != trans_var:
                                        new_value = new_value.replace(trans_var, src_var, 1)
                            else:
                                # Mismatch in variable count, restore entire value
                                new_value = value_id
                            break
                    
                    if new_value != value_str:
                        old_param = f'{param_name}="{value_str}"'
                        new_param = f'{param_name}="{new_value}"'
                        
                        # Replace within this specific shortcode's parameter section
                        sc_start = sc_msgstr.start(4)
                        sc_end = sc_msgstr.end(4)
                        before = result[:sc_start]
                        sc_params = result[sc_start:sc_end]
                        after = result[sc_end:]
                        
                        if old_param in sc_params:
                            sc_params = sc_params.replace(old_param, new_param, 1)
                            result = before + sc_params + after
                            fixes.append(f'param {param_name}: "{value_str}" → "{new_value}"')
                            
                            # Refresh the shortcode matches after modification
                            msgstr_shortcodes = list(SHORTCODE_RE.finditer(result))
    
    return result, fixes


def restore_hugo_variables(msgid: str, msgstr: str) -> tuple[str, list[str]]:
    """
    Restore Hugo template variables that were translated.
    Hugo template variables use pipe notation: |variable|, |ltrversion|, |version|
    These should NEVER be translated as they are template variable names.
    """
    result = msgstr
    fixes = []
    
    # Find all Hugo template variables in source (msgid)
    pipe_pattern = r'\|[a-zA-Z][a-zA-Z0-9_]*\|'
    variables_in_source = re.findall(pipe_pattern, msgid)
    
    if not variables_in_source:
        return result, fixes
    
    # Check each variable exists in translation
    for var in variables_in_source:
        if var not in result:
            # Variable was translated or corrupted
            # Find what it was translated to (any |...| pattern in roughly the same position)
            variables_in_translation = re.findall(r'\|[^|]+\|', result)
            
            # Try to match by position/context
            # For now, simple approach: replace first occurrence of any translated |...| with correct variable
            if variables_in_translation:
                for trans_var in variables_in_translation:
                    # Check if this translated variable doesn't exist in source
                    if trans_var not in msgid:
                        # This is likely the translated version of our variable
                        result = result.replace(trans_var, var, 1)
                        fixes.append(f'Hugo variable: "{trans_var}" → "{var}"')
                        break
    
    return result, fixes


def fix_malformed_shortcodes(msgstr: str, valid: set[str]) -> tuple[str, list[str]]:
    """
    Fix malformed shortcode syntax where punctuation or typos corrupt the shortcode structure.
    Examples:
    - {{<ref. "path" >}} → {{< ref "path" >}}
    - {{<column-start. >}} → {{< column-start >}}
    - {{<button, text="foo" >}} → {{< button text="foo" >}}
    
    Note: We fix malformed syntax regardless of whether the shortcode is in our valid set,
    because built-in Hugo shortcodes (like 'ref', 'relref', 'param') won't be in the custom
    shortcodes directory but still need syntax fixes.
    """
    result = msgstr
    fixes = []
    
    # Pattern to detect malformed shortcodes with punctuation after shortcode name
    # Matches: {{< or {{<, then shortcode name, then punctuation (., , ; :), then space or >
    malformed_pattern = r'\{\{<\s*(/?)(\w+[\w-]*)([\.,;:])\s*([^>]*?)(/?)>\}\}'
    
    for match in re.finditer(malformed_pattern, result, re.UNICODE):
        closing_slash = match.group(1)  # / for closing tags
        shortcode_name = match.group(2)
        punctuation = match.group(3)    # The offending punctuation
        params = match.group(4)         # Parameters
        self_closing = match.group(5)   # / for self-closing
        
        # Fix the malformed shortcode regardless of valid set
        # (could be built-in Hugo shortcode like 'ref' or 'param')
        old_shortcode = match.group(0)
        
        # Reconstruct with proper spacing
        space_before = '' if closing_slash else ' '
        space_after = ' ' if params.strip() else ''
        new_shortcode = f'{{{{<{space_before}{closing_slash}{shortcode_name}{space_after}{params.strip()}{self_closing} >}}}}'
        
        result = result.replace(old_shortcode, new_shortcode, 1)
        fixes.append(f'malformed shortcode: "{{{{<{closing_slash}{shortcode_name}{punctuation}" → "{{{{< {closing_slash}{shortcode_name}"')
    
    return result, fixes


def process_po_file(path: str, valid: set[str], dry_run: bool) -> int:
    """Process one .po file using polib. Returns number of shortcode names fixed."""
    try:
        po = polib.pofile(path)
    except Exception as e:
        print(f'  WARNING: could not parse {os.path.basename(path)}: {e}', file=sys.stderr)
        return 0

    total_fixes = 0
    entries_processed = 0

    for entry in po:
        # polib gives us already-unescaped strings; handles quoting on save.
        if not entry.msgid or not entry.msgstr:
            continue
        
        entries_processed += 1

        # First, fix shortcode names
        new_msgstr, name_fixes = restore_names(entry.msgid, entry.msgstr, valid)
        
        # Fix malformed shortcode syntax (e.g., {{<ref. instead of {{< ref)
        new_msgstr, syntax_fixes = fix_malformed_shortcodes(new_msgstr, valid)
        
        # Then, fix technical content (paths, parameters)
        new_msgstr, tech_fixes = restore_technical_content(entry.msgid, new_msgstr)
        
        # Finally, restore Hugo template variables that were translated
        new_msgstr, var_fixes = restore_hugo_variables(entry.msgid, new_msgstr)
        
        all_fixes = name_fixes + syntax_fixes + tech_fixes + var_fixes
        
        if not all_fixes:
            continue

        total_fixes += len(all_fixes)
        entry.msgstr = new_msgstr
        print(f'  {os.path.basename(path)}: {"; ".join(all_fixes)}')

    if total_fixes and not dry_run:
        try:
            po.save(path)
            print(f'  ✓ Saved {os.path.basename(path)} ({entries_processed} entries, {total_fixes} fixes)')
        except Exception as e:
            print(f'  ERROR: Failed to save {os.path.basename(path)}: {e}', file=sys.stderr)
            return 0

    return total_fixes


def main() -> None:
    ap = argparse.ArgumentParser(
        description='Restore corrupted Hugo shortcode names in translated .po files.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument(
        '--translations',
        default='translations',
        help='Root directory containing language subdirs with .po files (default: %(default)s)',
    )
    ap.add_argument(
        '--themes',
        default='themes',
        help='Root directory of Hugo themes (default: %(default)s)',
    )
    ap.add_argument(
        '--dry-run',
        action='store_true',
        help='Print what would change without modifying files',
    )
    args = ap.parse_args()

    themes_dir = args.themes
    translations_dir = args.translations

    if not os.path.isdir(themes_dir):
        print(f'ERROR: themes directory not found: {themes_dir}', file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(translations_dir):
        print(f'ERROR: translations directory not found: {translations_dir}', file=sys.stderr)
        sys.exit(1)

    valid = get_valid_shortcodes(themes_dir)
    if not valid:
        print('WARNING: no shortcode names found in themes — check --themes path', file=sys.stderr)

    po_files = sorted(glob.glob(os.path.join(translations_dir, '**', '*.po'), recursive=True))
    if not po_files:
        print('No .po files found — nothing to do.')
        return

    print(f'Processing {len(po_files)} .po file(s)...')
    
    total = 0
    processed_files = 0
    for po_file in po_files:
        n = process_po_file(po_file, valid, args.dry_run)
        total += n
        if n > 0:
            processed_files += 1

    if total:
        action = 'Would fix' if args.dry_run else 'Fixed'
        print(f'{action} {total} corrupted shortcode name(s) across {processed_files} file(s).')
    else:
        print('No corrupted shortcode names found.')
    
    # Validation: Check for common corrupted patterns that shouldn't be there
    if not args.dry_run and total > 0:
        print('\nValidating fixes...')
        # Only check for specific corrupted shortcode patterns, not general word occurrences
        corrupted_patterns = ['край', 'slut', 'koniec', 'конец', 'slutt', 'колона', 'параметър']
        found_issues = False
        for po_file in po_files:
            try:
                with open(po_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in corrupted_patterns:
                        # Look for actual shortcode tags: {{< pattern OR {{< pattern-something
                        # This is much more specific than the previous regex
                        shortcode_pattern = rf'\{{\{{<\s*{re.escape(pattern)}(?:\s|>|-)'
                        if re.search(shortcode_pattern, content):
                            print(f'  WARNING: Corrupted shortcode "{{{{< {pattern}" still in {os.path.basename(po_file)}', file=sys.stderr)
                            found_issues = True
                            break  # Don't spam multiple warnings for the same file
            except Exception:
                pass
        
        if found_issues:
            print('\n❌ ERROR: Validation found remaining corrupted shortcodes after sanitization!', file=sys.stderr)
            sys.exit(1)
        else:
            print('✅ Validation passed - no corrupted patterns detected')


if __name__ == '__main__':
    main()
