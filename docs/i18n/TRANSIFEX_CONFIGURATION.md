# Transifex Configuration Guide for QGIS Website

This guide explains how to configure Transifex to prevent translators from accidentally translating technical content like shortcodes, file paths, and parameter values.

## Problem

Translators sometimes translate technical content that should remain in English:
- Shortcode names: `{{< column-end >}}` → `{{< край на колоната >}}`
- File paths: `"community/groups.md"` → `"общност/групи.md"`
- Parameter values: `showcase="map"` → `showcase="карта"`

This breaks the website build and requires manual fixes.

## Solution: Transifex Placeholder Protection

Transifex can be configured to lock certain patterns so they appear as non-editable placeholders to translators.

## Steps to Configure

### 1. Access Project Settings

1. Go to https://www.transifex.com/qgis/qgis-website/
2. Click **Settings** (gear icon)
3. Navigate to **Checks & Settings**

### 2. Enable Placeholder Detection

Find the **Placeholder Pattern** section and enable it.

### 3. Add Protection Patterns

Add these regex patterns to protect technical content:

#### Pattern 1: Protect All Shortcodes
```regex
\{\{<[^>]+>\}\}
```
This protects entire shortcodes like `{{< ref "path/to/file.md" >}}`.

#### Pattern 2: Protect Specific File Paths (Alternative)
```regex
\{\{<\s*ref\s+"[^"]+"\s*>\}\}
```
This specifically protects `ref` shortcodes with file paths.

#### Pattern 3: Protect URLs and Paths in Links
```regex
link="[^"]+"
```
This protects the `link` parameter in buttons and other shortcodes.

#### Pattern 4: Protect Hugo Template Variables
```regex
\|[a-zA-Z][a-zA-Z0-9_]*\|
```
This protects Hugo template variables like `|ltrversion|`, `|version|` that appear in tab labels and other dynamic content.

### 4. Configure ICU Placeholders (Advanced)

For better control, you can use ICU message format. This requires pre-processing the `.pot` file before pushing to Transifex.

Example transformation:
```
Before: See [User Groups]({{< ref "community/groups.md" >}})
After:  See {user_groups_link_start}User Groups{user_groups_link_end}
```

This requires adding scripts to convert placeholders before `txpush` and after `txpull`.

## Current Protection: Sanitize Script

We currently have a **sanitize script** that runs after pulling translations from Transifex. This catches and fixes most issues automatically:

- **Location**: `scripts/i18n/sanitize_shortcodes.py`
- **When it runs**: Automatically after `make txpull`
- **What it fixes**:
  - Translated shortcode names
  - Translated file paths in `ref` shortcodes
  - Translated parameter values (showcase, columns, class, etc.)
  - Translated Hugo template variables like `|ltrversion|`, `|version|`
  - **NEW**: Malformed shortcode syntax (e.g., `{{<ref.` → `{{< ref`)

## Hugo Template Variables

Hugo uses pipe notation for template variables: `|variable|`. These appear in tab labels and other content:

```markdown
{{<tabs tab1="QGIS |ltrversion|" tab2="QGIS testing (>|version|)" >}}
```

**Important**: The pipe-delimited content (e.g., `|ltrversion|`) is a variable name and must NOT be translated. The text around it ("QGIS", "testing") can be translated.

Example:
- ❌ Wrong: `tab1="QGIS |альтернативна версія|"` (variable translated to Ukrainian)
- ✅ Correct: `tab1="QGIS |ltrversion|"` (variable kept, "QGIS" can stay or be translated)

The sanitize script automatically restores these variables if they were translated.

## Recommended Approach

Use a **layered defense strategy**:

1. **Prevention (Transifex configuration)** - Primary defense
   - Configure placeholder patterns (as described above)
   - Provide translator guidelines (link to TRANSLATORS_GUIDE.md)

2. **Detection (Sanitize script)** - Safety net
   - Automatically fixes issues that slip through
   - Already implemented and working

3. **Education (Documentation)**
   - TRANSLATORS_GUIDE.md for translators
   - Regular reminders to translation teams
   - Examples in Transifex comments

## Testing the Configuration

After configuring Transifex:

1. Push a test file with shortcodes to Transifex:
   ```bash
   make txpush
   ```

2. Check in Transifex web interface:
   - Shortcodes should appear as locked placeholders
   - Translators should not be able to edit them

3. If shortcodes are still editable:
   - Review regex patterns
   - Check that placeholder detection is enabled
   - Contact Transifex support if needed

## Sharing Guidelines with Translators

Add a note to your Transifex project's **Instructions for Translators**:

```
⚠️ IMPORTANT: Technical Content Protection

When translating, please DO NOT modify content within {{< >}} brackets.
These are Hugo shortcodes and must remain exactly as shown in English.

Examples of what NOT to translate:
- {{< column-end >}} - Keep as-is
- {{< ref "community/groups.md" >}} - Keep file paths in English
- showcase="map" - Keep technical parameter values in English

Only translate the visible text that users will see on the website.

Full guidelines: https://github.com/qgis/QGIS-Website/blob/main/TRANSLATORS_GUIDE.md
```

## Additional Resources

- [Transifex Placeholders Documentation](https://help.transifex.com/en/articles/6241233-placeholders)
- [ICU Message Format](https://unicode-org.github.io/icu/userguide/format_parse/messages/)
- [QGIS Translation Guidelines](./TRANSLATORS_GUIDE.md)

## Support

If you encounter issues with Transifex configuration:
- QGIS Documentation Team: via mailing list
- Transifex Support: https://www.transifex.com/support/

## Monitoring

Regularly check the output of the sanitize script to see what's being fixed:

```bash
make txpull
# Look for output like:
# "Fixed 5 corrupted shortcode name(s) across 3 file(s)."
```

If you see many fixes, it means the Transifex configuration needs improvement.
