# Shortcode Syntax Guide for Hugo-Gettext Translation

## Problem Summary

Hugo-gettext extracts translatable content from shortcode parameters only when shortcodes meet **three requirements**:
1. Each shortcode must be in its **own markdown paragraph** — blank line before and after it
2. For paired shortcodes (using `.Inner`): the `{{< /tag >}}` closing tag must be on its own separate paragraph (blank line before it)
3. No `{{< content-start >}}`/`{{< content-end >}}` wrapper around translatable shortcodes

Spaces around `=` (`param = "value"`) are conventional in this project but are not strictly required by the parser.

## The Root Cause

Hugo-gettext uses markdown-it to parse content. The extractor (`renderer_hugo_i18n.py`) only extracts params when an inline token has **exactly one shortcode child** (`len(token.children) == 1`). If two or more shortcodes share the same paragraph, they produce multiple children and the whole paragraph is extracted as prose.

### 1. Multiple shortcodes in the same paragraph (critical)

Adjacent shortcode lines without a blank line between them form **one markdown paragraph**. The extractor sees multiple shortcode children and falls back to prose extraction.

```markdown
❌ Adjacent lines — one paragraph, two children, extracted as a blob:
{{< button text = "Click me" link = "..." >}}
{{< button text = "Read more" link = "..." >}}

✅ Blank line between them — separate paragraphs, one child each:
{{< button text = "Click me" link = "..." >}}

{{< button text = "Read more" link = "..." >}}
```

### 2. Paired/closing shortcode tags on the same line (critical)

When `{{< /block >}}` is on the same line as `>}}`, both end up in the same paragraph, giving two shortcode children. Moving the closing tag to its own paragraph (with a blank line before it) isolates each element.

```markdown
❌ Closing tag on same line — two children, extracted as blob:
{{< block title = "Mapping." subtitle = "..." >}}{{< /block >}}

✅ Closing tag on its own paragraph:
{{< block
title = "Mapping."
subtitle = "..." >}}

{{< /block >}}
```

### 3. `{{< content-start >}}` wrapper (critical)
Anything inside a `{{< content-start >}}`/`{{< content-end >}}` wrapper is treated as a single prose block.
Fix: do not place translatable shortcodes inside these wrappers.

None of these are configurable via Transifex or `config.toml` — they must be fixed in the source markdown files.

## Syntax Comparison

### ✅ CORRECT: Each shortcode in its own paragraph

```markdown
{{< button text = "Click me" link = "/page" >}}

{{< button text = "Read more" link = "/other" >}}
```

**Extraction result:**
```po
msgid "Click me"
msgid "Read more"
```

### ✅ CORRECT: Paired shortcode with closing tag in its own paragraph

```markdown
{{< block
title = "Mapping."
subtitle = "Unleash your creativity." >}}

{{< /block >}}
```

**Extraction result:**
```po
msgid "Mapping."
msgid "Unleash your creativity."
```

### ❌ INCORRECT: Adjacent shortcodes without blank lines

```markdown
{{< button text = "Click me" link = "/page" >}}
{{< button text = "Read more" link = "/other" >}}
```

**Extraction result:** Both buttons merged into one prose string.

### ❌ INCORRECT: Closing tag on the same line as `>}}`

```markdown
{{< block title = "Mapping." subtitle = "..." >}}{{< /block >}}
```

**Extraction result:** The whole construct extracted as one prose string.

### ❌ INCORRECT: Inside `content-start`/`content-end` wrapper

```markdown
{{< content-start >}}
{{< block title = "Mapping." ... >}}
{{< content-end >}}
```

**Extraction result:** All content between the wrappers merged into one string.

## Conversion Process

### Step 1: Identify Affected Files

Search for shortcodes with quoted syntax:
```bash
grep -r '{{<\s*\w\+\s\+\w\+="' content/
```

Common patterns to look for:
- `title="..."`
- `subtitle="..."`
- `text="..."`
- `class="..."`
- `link="..."`

### Step 2: Convert Each Shortcode

**Before:**
```markdown
{{< button text="Download QGIS" link="/download" class="is-primary" >}}
```

**After:**
```markdown
{{< button text = "Download QGIS" link = "/download" class = "is-primary" >}}
```

**Rules:**
1. Add space before `=`
2. Add space after `=`
3. Apply to ALL parameters in the shortcode
4. Keep quotes around values
5. Maintain multi-line formatting if present

### Step 3: Handle Multi-line Shortcodes

**Before:**
```markdown
{{< block
    title="Behind the scenes."
    subtitle="Leverage the work and experience of some the world's top geospatial experts."
    image=""
    class="is-primary5"
>}}{{< /block >}}
```

**After:**
```markdown
{{< block
    title = "Behind the scenes."
    subtitle = "Leverage the work and experience of some the world's top geospatial experts."
    image = ""
    class = "is-primary5"
>}}{{< /block >}}
```

**Important:**
- Keep the closing `>}}` on the same line as the last parameter
- Maintain indentation for readability
- Multi-line formatting is fine with correct syntax

### Step 4: Verify Changes

After conversion:
1. Run `make messages-extract` to regenerate messages.pot
2. Check that individual parameter values are extracted:
   ```bash
   grep 'msgid "Behind the scenes."' translations/en/messages.pot
   ```
3. Verify no full shortcode blocks in messages.pot:
   ```bash
   grep '{{< block title=' translations/en/messages.pot
   ```
4. Test Hugo build: `hugo server`

## Common Shortcodes That Need Conversion

### Priority 1: Content Shortcodes (User-Facing Text)

These have translatable parameters and should be converted first:

```markdown
# block shortcode
{{< block title = "..." subtitle = "..." >}}

# button shortcode  
{{< button text = "..." link = "..." >}}

# feature shortcode
{{< feature title = "..." text = "..." col-title-1 = "..." >}}

# rich-list shortcode
{{< rich-list listTitle = "..." listSubtitle = "..." >}}

# info-card shortcode
{{< info-card title = "..." description = "..." >}}

# tabs shortcode
{{< tabs tab1 = "..." tab2 = "..." tab3 = "..." >}}

# spoiler-start shortcode
{{< spoiler-start title = "..." >}}

# hero-banner shortcode
{{< hero-banner title = "..." subtitle = "..." >}}
```

### Priority 2: Layout Shortcodes (Technical Parameters Only)

These typically don't have translatable content, but should use correct syntax for consistency:

```markdown
# column-start
{{< column-start class = "is-half" >}}

# rich-box-start
{{< rich-box-start layoutClass = "has-right" mode = "html" >}}

# rich-content-start
{{< rich-content-start themeClass = "coloring-1" >}}

# box-start
{{< box-start ribbon = "Note!" ribbon-class = "is-warning" >}}
```

## Files Requiring Conversion

Based on current codebase scan:

### Content Files with Quoted Syntax

1. **content/about/index.md** - Multiple `block` shortcodes (HIGH PRIORITY)
   - 5 block shortcodes with title/subtitle parameters
   - Currently sends full blocks to translation

2. **content/funding/donate.md** - Layout shortcodes
   - Mainly `rich-box-start`, `rich-content-start`, `column-start`
   - Mostly technical parameters, lower priority

3. **content/funding/membership.md** - Layout shortcodes
   - Similar to donate.md, mostly technical

4. **Other files** - Check with grep search

### Verification Commands

```bash
# Find all shortcodes with quoted syntax in content
find content -name "*.md" -exec grep -l '{{<.*="' {} \;

# Count occurrences
grep -r '{{<\s*\w\+\s\+\w\+="' content/ | wc -l

# Check specific shortcode
grep -r '{{< block.*title=' content/
```

## Automated Conversion Script

For bulk conversion, you can use this sed command (test on a copy first!):

```bash
# Backup first
cp content/about/index.md content/about/index.md.bak

# Convert quoted syntax to shorthand (add spaces around =)
sed -i '' 's/\(\w\+\)="\([^"]*\)"/\1 = "\2"/g' content/about/index.md

# Verify changes
diff content/about/index.md.bak content/about/index.md
```

**Warning:** This is a simple regex replacement. Review changes manually before committing!

## Testing After Conversion

### 1. Extract Strings
```bash
make messages-extract
```

### 2. Check messages.pot
```bash
# Should find individual values
grep -A2 'msgid "Mapping."' translations/en/messages.pot

# Should NOT find full shortcodes
grep 'msgid.*{{< block title=' translations/en/messages.pot
```

### 3. Push to Transifex
```bash
make txpush
```

### 4. Verify on Transifex
- Log into Transifex web interface
- Check that translators see clean parameter values
- Verify no Hugo markup in strings

### 5. Build Site
```bash
hugo server
```

Check that all pages render correctly.

## Prevention: New Content Guidelines

When creating new content:

1. **Always use shorthand syntax** for shortcodes with parameters:
   ```markdown
   {{< shortcode param = "value" >}}
   ```

2. **Add to config.toml** if new translatable parameters:
   ```toml
   [i18n.shortcodes.params]
     my-shortcode = ["title", "text"]
   ```

3. **Verify extraction** after adding new shortcodes:
   ```bash
   make messages-extract
   grep "my new string" translations/en/messages.pot
   ```

## FAQ

### Q: Why does Hugo accept both syntaxes?
A: Hugo's own parser handles both. The issue is with hugo-gettext's extraction parser, which is separate.

### Q: Can we configure hugo-gettext to handle quoted syntax?
A: No, this is a parser limitation in hugo-gettext itself. The only solution is to use shorthand syntax.

### Q: Will this break existing translations?
A: No. After conversion:
- Extract new messages.pot
- Push to Transifex
- Translators will see the same strings (but cleaner)
- Existing translations will match automatically

### Q: Do I need to convert shortcodes without translatable parameters?
A: Not strictly necessary, but recommended for consistency and future-proofing.

### Q: What about shortcodes in themes?
A: Theme shortcodes don't get extracted for translation, so they can use either syntax. This only affects content files.

## Related Documentation

- [I18N.md](../../I18N.md) - Main internationalization documentation
- [TRANSLATORS_GUIDE.md](TRANSLATORS_GUIDE.md) - Guide for translators
- [TRANSIFEX_CONFIGURATION.md](TRANSIFEX_CONFIGURATION.md) - Transifex setup

## Summary Checklist

Before converting:
- [ ] Backup files
- [ ] Identify all affected files
- [ ] Understand current extraction issues

During conversion:
- [ ] Convert shortcodes to use ` = ` (spaces around equals)
- [ ] Apply to ALL parameters consistently
- [ ] Maintain multi-line formatting where used
- [ ] Keep closing `>}}` on same line as last parameter

After conversion:
- [ ] Run `make messages-extract`
- [ ] Verify individual values in messages.pot
- [ ] Test Hugo build
- [ ] Push to Transifex
- [ ] Verify cleaner strings for translators
- [ ] Commit changes

## Support

If you encounter issues during conversion:
1. Check Hugo build output for errors
2. Verify hugo-gettext extraction works: `make messages-extract`
3. Compare messages.pot before and after conversion
4. Ask on QGIS developers mailing list

---

**Last Updated:** May 2026  
**Applies to:** hugo-gettext integration with QGIS Website project
