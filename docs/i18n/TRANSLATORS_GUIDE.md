# Translator's Guide for QGIS Website

## ⚠️ Important: DO NOT Translate Technical Content

When translating content for the QGIS website, please **DO NOT** translate the following technical elements:

### 1. Hugo Shortcodes (Tags)

Shortcodes are special markup that Hugo uses to generate website features. They are enclosed in `{{< >}}` or `{{% %}}`.

**❌ WRONG:**
```markdown
{{< край на колоната >}}  <!-- Bulgarian translation of "column-end" -->
{{< fin de colonne >}}     <!-- French translation of "column-end" -->
```

**✅ CORRECT:**
```markdown
{{< column-end >}}        <!-- Always keep in English -->
```

### 2. File Paths in Links

File paths inside `ref` shortcodes must remain in English:

**❌ WRONG:**
```markdown
{{< ref "общност/групи.md" >}}        <!-- Translated path -->
{{< ref "communauté/groupes.md" >}}   <!-- Translated path -->
```

**✅ CORRECT:**
```markdown
{{< ref "community/groups.md" >}}     <!-- Always keep in English -->
```

### 3. Shortcode Parameter Values

Technical parameter values must remain in English:

**❌ WRONG:**
```markdown
{{< hub-images showcase="карта" columns="галерия" >}}
{{< column-start class="заоблена" >}}
```

**✅ CORRECT:**
```markdown
{{< hub-images showcase="map" columns="gallery" >}}
{{< column-start class="rounded" >}}
```

### 4. URL Segments and Links

When you see URL paths or technical identifiers, keep them in English:

**❌ WRONG:**
```markdown
{{< button link="общност/групи" text="Потребителски групи" >}}
```

**✅ CORRECT:**
```markdown
{{< button link="community/groups" text="Потребителски групи" >}}
```

Only translate the `text` parameter!

### 5. Hugo Template Variables

Hugo uses pipe notation `|variable|` for dynamic content like version numbers. These variable names must NEVER be translated:

**❌ WRONG:**
```markdown
QGIS |алтернативна версія|      <!-- Ukrainian: "alternative version" -->
QGIS |versión ltr|              <!-- Spanish variation -->
```

**✅ CORRECT:**
```markdown
QGIS |ltrversion|               <!-- Variable name stays in English -->
```

Common Hugo variables you'll see:
- `|version|` - Current QGIS version
- `|ltrversion|` - Long-term release version
- `|nextversion|` - Next upcoming version

**✅ You CAN translate the text AROUND these variables:**
```markdown
English:    QGIS |ltrversion|
Bulgarian:  QGIS |ltrversion|         (keep "QGIS" or translate if needed)
Spanish:    QGIS |ltrversion|         (keep "QGIS" or translate if needed)
```

The key rule: **Text between pipes (|...|) is a variable name - never translate it!**

## What SHOULD Be Translated

Translate:
- ✅ Regular text and paragraphs
- ✅ Headings and titles
- ✅ Button text (the `text` parameter value)
- ✅ Alt text for images
- ✅ Link text that appears to users
- ✅ Descriptions and instructions

## Examples

### Example 1: User Groups Link

**English Source:**
```markdown
See [User Groups]({{< ref "community/groups.md" >}}) to read more.
```

**✅ Correct Bulgarian Translation:**
```markdown
Вижте [Потребителски групи]({{< ref "community/groups.md" >}}) за да прочетете повече.
```

Note: Only "User Groups" and "to read more" are translated. The file path stays in English.

### Example 2: Button with Link

**English Source:**
```markdown
{{< button class="is-primary1" link="community/groups" text="User groups 🇩🇪 🇫🇷 🇪🇸" >}}
```

**✅ Correct Bulgarian Translation:**
```markdown
{{< button class="is-primary1" link="community/groups" text="Потребителски групи 🇩🇪 🇫🇷 🇪🇸" >}}
```

Note: Only the `text` value is translated. Everything else (shortcode name, class, link path) remains in English.

### Example 3: Image Gallery

**English Source:**
```markdown
{{< hub-images showcase="map" quantity="4" columns="gallery" >}}
```

**✅ Correct Translation (ANY language):**
```markdown
{{< hub-images showcase="map" quantity="4" columns="gallery" >}}
```

Note: This entire shortcode stays the same in ALL languages - nothing should be translated!

### Example 4: Tab Labels with Hugo Variables

**English Source:**
```markdown
{{<tabs tab1="QGIS |ltrversion|" tab2="QGIS testing (>|version|)" tab3="Archived releases" >}}
```

**✅ Correct Bulgarian Translation:**
```markdown
{{<tabs tab1="QGIS |ltrversion|" tab2="QGIS тестване (>|version|)" tab3="Архивирани издания" >}}
```

**❌ WRONG Bulgarian Translation:**
```markdown
{{<tabs tab1="QGIS |алтернативна версия|" tab2="QGIS тестване (>|версия|)" tab3="Архивирани издания" >}}
```

Note: You can translate "QGIS testing" → "QGIS тестване" and "Archived releases" → "Архивирани издания", but the pipe-delimited variables (`|ltrversion|`, `|version|`) must stay exactly as they are!

## Why This Matters

When technical content gets translated:
- 🚫 The website build fails
- 🚫 Links stop working
- 🚫 Images don't display
- 🚫 Layout breaks

Our automated system will fix some of these issues, but it's better to avoid them in the first place!

## Questions?

If you're unsure whether something should be translated:
- **If it looks like code or a file path** → Don't translate it
- **If it's inside `{{< >}}` brackets** → Usually don't translate it (except `text` and similar display values)
- **If users will see it on the website** → Translate it

When in doubt, ask the translation coordinators or check the English source to see what's meant for display vs. technical markup.

Thank you for helping make QGIS accessible to speakers of your language! 🌍
