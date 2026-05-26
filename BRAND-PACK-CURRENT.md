# OSGeo Brand Pack

Official brand guidelines for the Open Source Geospatial Foundation.

---

## 1. Logo

The OSGeo logo features a compass rose symbolizing geographic orientation and navigation. It was designed by **Pim Tebbens** (June 2017) and is licensed under [CC BY-ND 4.0](http://creativecommons.org/licenses/by-nd/4.0/).

### Logo Variants

| Variant | File | Usage |
|---------|------|-------|
| Primary Logo (SVG) | `static/img/osgeo/osgeo-logo.svg` | Light backgrounds |
| Primary Logo (PNG) | `static/img/osgeo/osgeo-logo-rgb.png` | Print / light backgrounds |
| White Logo (SVG) | `static/img/osgeo/osgeo-logo-white.svg` | Dark backgrounds |
| Emblem (SVG) | `static/img/osgeo/osgeo-emblem.svg` | Compact contexts (favicons, icons) |
| Emblem (PNG) | `static/img/osgeo/osgeo-emblem.png` | Compact contexts (favicons, icons) |

### Compass Decorative Elements

| Variant | File | Usage |
|---------|------|-------|
| Compass Intro | `static/img/osgeo/compass-intro.svg` | Hero section (mobile) |
| Compass Intro 768 | `static/img/osgeo/compass-intro-768.svg` | Hero section (tablet) |
| Compass Intro Wide | `static/img/osgeo/compass-intro-wide.svg` | Hero section (desktop) |
| Compass Footer | `static/img/osgeo/compass-footer.svg` | Footer decoration |

### Logo Clear Space

Minimum clear space around the logo equals the height of the "O" in "OSGeo".

### Logo Usage Rules

**Do:**
- Use official logo files only
- Maintain the original aspect ratio
- Ensure adequate clear space
- Use the white variant on dark backgrounds

**Don't:**
- Stretch or distort the logo
- Change logo colors
- Add effects, shadows, or outlines
- Place on busy or low-contrast backgrounds

---

## 2. Color Palette

### Primary Colors

| Name | Hex | Pantone | RGB | Usage |
|------|-----|---------|-----|-------|
| **OSGeo Green** | `#4DB05B` | 361 U | 77, 176, 91 | Primary brand, buttons, links, success states |
| **OSGeo Teal** | `#003A40` | 330 U | 0, 58, 64 | Headlines, text, dark backgrounds, info states |
| **White** | `#FFFFFF` | - | 255, 255, 255 | Backgrounds, reversed text |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Light Green** | `#6FCF7A` | 111, 207, 122 | Hover states, accents, complementary highlights |
| **Light Teal** | `#006670` | 0, 102, 112 | Secondary headings, mid-tone teal elements |
| **Dark Green** | `#3A8A47` | 58, 138, 71 | Pressed states, darker green accents |
| **Dark Teal** | `#001F22` | 0, 31, 34 | Deep backgrounds, near-black text |
| **Mid Green** | `#2D6E4B` | 45, 110, 75 | Complementary green, secondary text |
| **Bright Teal** | `#00858C` | 0, 133, 140 | Accent teal, interactive elements |
| **Deep Teal** | `#004D52` | 0, 77, 82 | Dark accent teal |

### Extended Palette

| Name | Hex | Usage |
|------|-----|-------|
| Soft Green | `#5DC06B` | Lighter primary variant |
| Pale Green | `#87D492` | Very light green accents |
| Cyan | `#00B8D4` | Ocean gradient accent |
| Emerald | `#10B981` | Success accent |
| Amber | `#F59E0B` | Warnings |
| Coral | `#FF6B6B` | Sunset gradient accent |

### Background Colors

| Name | Hex | Usage |
|------|-----|-------|
| Light BG 1 | `#f8faf8` | Page backgrounds |
| Light BG 2 | `#e8f5e9` | Section backgrounds, cards |
| Light BG 3 | `#c8e6c9` | Highlighted areas, badges |

### System / UI Colors

| Name | Hex | Usage |
|------|-----|-------|
| Danger / Error | `#d32f2f` | Error states, destructive actions |
| Warning | `#ffc107` | Warning states |
| Info | `#003A40` | Informational (same as Teal) |
| Success | `#4DB05B` | Success (same as Green) |
| Link | `#4DB05B` | Hyperlinks |

---

## 3. Typography

### Font Families

| Role | Font | Fallbacks | Weight |
|------|------|-----------|--------|
| **Headings** | Miriam Libre | Helvetica Neue, sans-serif | Bold (700) |
| **Body** | Sintony | Helvetica Neue, sans-serif | Regular (400) |
| **Display / Fancy** | Miriam Libre | serif | Bold (700) |

### Font Scale (Bulma-based)

| Size Token | Value | Usage |
|------------|-------|-------|
| Size 1 | `4rem` (64px) | Hero titles |
| Size 2 | `3.5rem` (56px) | Large headings |
| Size 3 | `2.2rem` (35.2px) | Section titles |
| Size 4 | `1.6rem` (25.6px) | Subsection titles |
| Size 5 | `1.2rem` (19.2px) | Body large / lead text |
| Size 6 | `1rem` (16px) | Body text, navigation |
| Size 7 | `0.75rem` (12px) | Captions, footnotes |

### Hero Title Sizing (Responsive)

```
clamp(2.5rem, 6vw, 4.5rem)  /* Standard hero */
clamp(3rem, 8vw, 7.5rem)    /* Home hero */
```

- Font weight: **800**
- Line height: **1.1 - 1.18**

---

## 4. Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | `0.25rem` (4px) | Tight inner padding |
| `--space-sm` | `0.5rem` (8px) | Small gaps |
| `--space-md` | `1rem` (16px) | Standard padding |
| `--space-lg` | `1.5rem` (24px) | Section padding |
| `--space-xl` | `2rem` (32px) | Large spacing |
| `--space-2xl` | `3rem` (48px) | Section gaps |
| `--space-3xl` | `4rem` (64px) | Large section gaps |
| `--space-4xl` | `6rem` (96px) | Hero-level spacing |

---

## 5. Border Radius

| Context | Radius |
|---------|--------|
| Default (cards, boxes) | `4px` |
| Small | `2px` |
| Large | `6px` |
| Buttons | `10px` |
| Cookie banner | `8px` |
| Badges | `14px` |
| Logo containers | `16px - 20px` |
| Pill / rounded | `9999px` |

---

## 6. Shadows

| Level | Value | Usage |
|-------|-------|-------|
| Small | `0 2px 4px rgba(0, 58, 64, 0.08)` | Subtle elevation |
| Medium | `0 4px 12px rgba(0, 58, 64, 0.12)` | Cards, dropdowns |
| Large | `0 8px 24px rgba(0, 58, 64, 0.16)` | Modals, popovers |
| XL | `0 16px 48px rgba(0, 58, 64, 0.2)` | Hero elements |
| Glow | `0 0 40px rgba(77, 176, 91, 0.3)` | Accent glow effect |

Note: Shadows use the OSGeo Teal (`#003A40`) as the base color rather than pure black, keeping the shadow tone on-brand.

---

## 7. Gradients

### Named Gradients

| Name | CSS | Usage |
|------|-----|-------|
| **Earth** | `linear-gradient(135deg, #003A40 0%, #006670 50%, #4DB05B 100%)` | Primary brand gradient |
| **Hero** | `linear-gradient(135deg, rgba(0,58,64,0.95) 0%, rgba(0,102,112,0.85) 50%, rgba(77,176,91,0.75) 100%)` | Hero overlay |
| **Ocean** | `linear-gradient(135deg, #003A40 0%, #00B8D4 50%, #4DB05B 100%)` | Accent / alternate |
| **Forest** | `linear-gradient(135deg, #001F22 0%, #2D6E4B 50%, #6FCF7A 100%)` | Dark nature theme |
| **Sunset** | `linear-gradient(135deg, #003A40 0%, #FF6B6B 50%, #F59E0B 100%)` | Warm accent |

All gradients use a 135-degree angle and three-stop structure anchored by the brand teal.

---

## 8. Component Patterns

### Buttons

```css
/* Primary button */
background: #4DB05B;
color: #FFFFFF;
border-radius: 10px;
padding: 0.75rem 1.25rem;
transition: all 0.2s ease;

/* Secondary / outline button */
background: transparent;
color: #FFFFFF;
border: 2px solid #FFFFFF;
border-radius: 10px;
```

### Cards

```css
/* Light card */
background: linear-gradient(145deg, rgba(255,255,255,0.9) 0%, rgba(248,250,248,0.95) 100%);
border-radius: 4px;
box-shadow: 0 4px 12px rgba(0, 58, 64, 0.12);

/* Dark card */
background: linear-gradient(145deg, rgba(0,58,64,0.95) 0%, rgba(0,31,34,0.98) 100%);
```

### Glass Morphism (Hero Stats)

```css
background: rgba(255, 255, 255, 0.12);
backdrop-filter: blur(8px);
border: 1px solid rgba(255, 255, 255, 0.25);
```

### Badges

```css
border-radius: 14px;
padding: 0.05rem 0.15rem;
```

---

## 9. Responsive Breakpoints

| Name | Width | Usage |
|------|-------|-------|
| Mobile | < 769px | Single column |
| Tablet | >= 769px | Two columns |
| Desktop | >= 1024px | Full layout |
| Widescreen | >= 1216px | Wide layout |
| Full HD | >= 1408px | Maximum width |

---

## 10. Animation & Motion

### Easing Functions

| Name | Value | Usage |
|------|-------|-------|
| Smooth | `cubic-bezier(0.4, 0, 0.2, 1)` | General transitions |
| Bounce | `cubic-bezier(0.68, -0.55, 0.265, 1.55)` | Playful interactions |
| Elastic | `cubic-bezier(0.175, 0.885, 0.32, 1.275)` | Springy feedback |

### Named Animations

| Name | Duration | Usage |
|------|----------|-------|
| `fadeInUp` | 0.8s | Content entrance |
| `floatLogo` | 6s infinite | Logo subtle motion |
| `aurora` | 20s infinite | Background ambient effect |
| `orbFloat` | 20s infinite | Decorative orb movement |

### Standard Transition

```css
transition: all 0.2s ease; /* 86ms Bulma standard for hover states */
```

---

## 11. Iconography

The site uses **Font Awesome** (solid and brands) for all icons. No custom icon set.

---

## 12. CSS Architecture

| File | Purpose |
|------|---------|
| `themes/hugo-bulma-blocks-theme/assets/sass/bulma.sass` | Base framework with color variables |
| `themes/hugo-bulma-blocks-theme/assets/css/osgeo-vibrant.css` | Modern theme with CSS custom properties |
| `themes/hugo-bulma-blocks-theme/assets/css/bulma-overrides.css` | Theme overrides |
| `assets/css/site-overrides.css` | Site-specific hero and component styles |
| `themes/hugo-bulma-blocks-theme/assets/css/custom.css` | Button radius and small tweaks |

---

## 13. Brand Voice

- **Tagline concept**: "Empowering Open Geospatial" / "The Open Source Geospatial Foundation"
- **Tone**: Professional, inclusive, community-driven, technically grounded
- **Language**: Clear, accessible English; avoid jargon where possible

---

## 14. Quick Reference Card

```
PRIMARY GREEN:   #4DB05B  (Pantone 361 U)
PRIMARY TEAL:    #003A40  (Pantone 330 U)
HEADING FONT:    Miriam Libre Bold
BODY FONT:       Sintony Regular
BUTTON RADIUS:   10px
BOX RADIUS:      4px
SHADOW BASE:     rgba(0, 58, 64, ...)
GRADIENT ANGLE:  135deg
CLEAR SPACE:     Height of "O" in OSGeo
```

---

## 15. Contact

For brand usage questions: [marketing@osgeo.org](mailto:marketing@osgeo.org)

Official logo pack: [OSGeo Wiki - Logo](https://wiki.osgeo.org/wiki/Logo)

---

*Copyright OSGeo Foundation. Logo licensed under CC BY-ND 4.0.*
