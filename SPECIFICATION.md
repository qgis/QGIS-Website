# OSGeo Hugo Website Specification

## Overview

The OSGeo Hugo Website is the official website for the Open Source Geospatial Foundation, built using Hugo static site generator with the hugo-bulma-blocks-theme. The site provides a comprehensive information architecture that funnels users from understanding OSGeo's value proposition to exploring projects and getting involved.

## Information Architecture

### User Journey Funnel

1. **Awareness** (Homepage) → Understand OSGeo's value proposition
2. **Discovery** (Projects) → Explore available software
3. **Engagement** (Community) → Find ways to connect
4. **Action** (Download/Join) → Get software or become a member

### Site Structure

```
OSGeo Website
├── Homepage (/)
│   ├── Value proposition stats (50+ projects, 300+ members, 20 years)
│   ├── Why Open Source Geospatial?
│   ├── Featured Projects
│   ├── Global Initiatives
│   ├── Community CTAs
│   └── Sponsors
│
├── Projects (/projects/)
│   ├── Desktop Applications (QGIS, GRASS, gvSIG, Marble)
│   ├── Web Mapping (GeoServer, MapServer, OpenLayers, pygeoapi, etc.)
│   ├── Geospatial Libraries (GDAL, PROJ, GEOS, GeoTools, etc.)
│   ├── Spatial Databases (PostGIS)
│   ├── Metadata Catalogs (GeoNetwork, pycsw)
│   ├── Content Management (GeoNode)
│   ├── Other (OSGeoLive)
│   └── Community Projects (/projects/community/)
│
├── About (/about/)
│   ├── Mission & Vision
│   ├── History & Milestones
│   ├── Governance (Board of Directors)
│   ├── Committees
│   ├── Legal Status
│   ├── FAQ (/about/faq/)
│   ├── Branding (/about/branding/)
│   ├── Contact (/about/contact/)
│   ├── Awards (/about/awards/)
│   │   └── Sol Katz Award
│   └── Incubation (/about/incubation/)
│
├── Initiatives (/initiatives/)
│   ├── FOSS4G Conference (/initiatives/foss4g/)
│   ├── Travel Grants (/initiatives/travel-grants/)
│   ├── Geo for All (/initiatives/geo-for-all/)
│   ├── Google Summer of Code (/initiatives/gsoc/)
│   ├── OSGeoLive (/initiatives/osgeolive/)
│   ├── Open GeoScience (/initiatives/open-geoscience/)
│   └── UN Initiative (/initiatives/un-initiative/)
│
├── Community (/community/)
│   ├── Getting Started (/community/getting-started/)
│   ├── Local Chapters (/local-chapters/)
│   ├── Mailing Lists (/community/mailing-lists/)
│   ├── Chat/IRC (/community/irc/)
│   ├── Code of Conduct (/community/code-of-conduct/)
│   ├── Service Providers (/service-providers/)
│   └── Events (/events/)
│
├── Membership (/membership/)
│   ├── Ways to Support
│   ├── Charter Membership
│   ├── Sponsorship Tiers
│   ├── Charter Members (/membership/charter-members/)
│   └── Donate (/donate/)
│
└── Sponsors (/sponsors/)
    ├── Diamond Sponsors
    ├── Gold Sponsors
    ├── Silver Sponsors
    └── Bronze Sponsors
```

## User Stories

### Visitor User Stories

1. **As a visitor**, I want to understand what OSGeo is so that I can decide if I want to participate in the community.

2. **As a visitor**, I want to browse OSGeo projects so that I can find the right open source geospatial tool for my needs.

3. **As a visitor**, I want to find local OSGeo chapters so that I can connect with my regional community.

4. **As a visitor**, I want to learn about FOSS4G conferences so that I can attend and participate.

5. **As a visitor**, I want to find ways to contribute so that I can help advance open source geospatial technology.

6. **As a visitor**, I want to donate to OSGeo so that I can support the foundation's mission.

7. **As a visitor**, I want to see impressive statistics that demonstrate OSGeo's impact (50+ projects, 300+ members, 20 years).

8. **As a visitor**, I want to quickly understand the benefits of open source (freedom, security, flexibility).

### Member User Stories

1. **As a charter member**, I want to see information about governance so that I can participate in foundation decisions.

2. **As a potential member**, I want to understand membership requirements so that I can work toward becoming a charter member.

### Developer User Stories

1. **As a developer**, I want to find project incubation information so that I can learn how to bring my project to OSGeo.

2. **As a developer**, I want to access documentation and resources so that I can use OSGeo projects effectively.

3. **As a developer**, I want to learn about GSoC opportunities so I can participate as a student or mentor.

## Business Rules

### Branding

1. The website MUST use OSGeo's official brand colors:
   - Primary: Light Green #4DB05B (Pantone 361 U)
   - Secondary: Dark Teal #003A40 (Pantone 330 U)

2. The website MUST use OSGeo's official fonts:
   - Headers: Miriam Libre Bold
   - Body text: Sintony Regular

3. The website MUST display the official OSGeo logo in SVG format.

4. The website SHOULD use vibrant gradient treatments combining brand colors for visual impact.

### Content Structure

1. The main navigation MUST include:
   - Projects
   - Resources
   - About
   - Initiatives
   - Community
   - Membership

2. All content pages MUST be written in Markdown format.

3. The homepage MUST feature:
   - OSGeo tagline: "Your Open Source Compass"
   - Mission statement
   - Impact statistics (50+ projects, 300+ members, 20 years)
   - Featured projects with download CTAs
   - Global initiatives overview
   - Community engagement options
   - Sponsor recognition

4. The Projects page MUST categorize software by type:
   - Desktop Applications
   - Web Mapping
   - Geospatial Libraries
   - Spatial Databases
   - Metadata Catalogs
   - Content Management

### Visual Design

1. The website MUST use the "OSGeo Vibrant" CSS theme with:
   - Gradient backgrounds using earth/ocean themes
   - Glassmorphism effects for depth
   - Smooth animations for engagement
   - Accessible contrast ratios

2. Call-to-action sections MUST use gradient backgrounds with clear button hierarchy.

3. Project cards MUST display category tags with color coding:
   - Desktop: Green
   - Web: Cyan
   - Library: Teal
   - Database: Amber
   - Catalog: Purple

### Technical Requirements

1. The website MUST be built with Hugo version 0.139.0 or later.

2. The website MUST use the hugo-bulma-blocks-theme.

3. The website MUST be deployable to static hosting platforms.

4. The website MUST support responsive design for mobile devices.

5. The website MUST include the osgeo-vibrant.css theme for modern styling.

## Functional Requirements

### Navigation

| FR-NAV-01 | Main menu navigation with dropdown submenus |
|-----------|---------------------------------------------|
| FR-NAV-02 | Mobile-responsive navigation |
| FR-NAV-03 | Breadcrumb navigation on section pages |

### Content Sections

| FR-CON-01 | Homepage with hero banner, stats, and feature blocks |
|-----------|---------------------------------------------|
| FR-CON-02 | Projects listing with categorization by type |
| FR-CON-03 | About section with foundation information |
| FR-CON-04 | Community section with engagement options |
| FR-CON-05 | Initiatives section (FOSS4G, Geo for All, GSoC, OSGeoLive) |
| FR-CON-06 | Resources section with learning materials |
| FR-CON-07 | Membership information with sponsorship tiers |
| FR-CON-08 | Local chapters listing |
| FR-CON-09 | Donation page with multiple payment options |
| FR-CON-10 | Sponsors recognition with tiered display |

### Visual Components

| FR-VIS-01 | Stat counters with large numbers |
|-----------|--------------------------------|
| FR-VIS-02 | Category tags with color coding |
| FR-VIS-03 | CTA sections with gradient backgrounds |
| FR-VIS-04 | Rich boxes with icons |
| FR-VIS-05 | Sponsor tier badges |

### Search

| FR-SRC-01 | Client-side search functionality |
|-----------|--------------------------------|
| FR-SRC-02 | Search results highlighting |

### Build & Deploy

| FR-BLD-01 | Hugo build with development configuration |
|-----------|------------------------------------------|
| FR-BLD-02 | Hugo build with production configuration |
| FR-BLD-03 | GitHub Pages deployment workflow |

## Non-Functional Requirements

### Performance

| NFR-PRF-01 | Page load time < 3 seconds on 3G connection |
|-----------|-------------------------------------------|
| NFR-PRF-02 | Static assets optimized for web delivery |
| NFR-PRF-03 | CSS animations GPU-accelerated |

### Accessibility

| NFR-ACC-01 | WCAG 2.1 Level AA compliance |
|-----------|------------------------------|
| NFR-ACC-02 | Semantic HTML structure |
| NFR-ACC-03 | Alt text for all images |
| NFR-ACC-04 | Focus-visible states for all interactive elements |

### Maintainability

| NFR-MNT-01 | Content managed through Markdown files |
|-----------|---------------------------------------|
| NFR-MNT-02 | Configuration through TOML files |
| NFR-MNT-03 | Theme separated from content |
| NFR-MNT-04 | CSS custom properties for theming |

## Architecture

### Technology Stack

- **Static Site Generator**: Hugo (extended version)
- **CSS Framework**: Bulma (via hugo-bulma-blocks-theme)
- **Custom CSS**: osgeo-vibrant.css for modern styling
- **Development Environment**: Nix
- **Deployment**: GitHub Pages / Static hosting

### Directory Structure

```
OSGEO-hugo/
├── config.toml           # Main configuration
├── config/               # Environment configs
├── content/              # Markdown content
│   ├── _index.md         # Homepage
│   ├── projects/         # Projects section
│   ├── about/            # About section
│   ├── initiatives/      # Initiatives section
│   ├── community/        # Community section
│   ├── membership/       # Membership section
│   └── sponsors/         # Sponsors section
├── data/                 # Data files (JSON, YAML)
├── static/               # Static assets
│   └── img/
│       ├── osgeo/        # OSGeo logos
│       ├── projects/     # Project logos
│       └── banners/      # Hero banners
├── themes/               # Hugo theme
│   └── hugo-bulma-blocks-theme/
│       └── assets/
│           └── css/
│               └── osgeo-vibrant.css  # Vibrant theme
└── layouts/              # Layout overrides
```

### Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| Primary Green | #4DB05B | Primary brand color, buttons, links |
| Green Light | #6FCF7A | Hover states, gradients |
| Green Dark | #3A8A47 | Active states |
| Dark Teal | #003A40 | Secondary color, text, headers |
| Teal Light | #006670 | Info blocks, gradients |
| Teal Dark | #001F22 | Footer, dark sections |
| Accent Cyan | #00B8D4 | Web category, accents |
| Accent Amber | #F59E0B | Database category |
| White | #ffffff | Backgrounds |
| Light Background | #f8faf8 | Section backgrounds |

### CSS Design System

The osgeo-vibrant.css theme provides:

1. **CSS Custom Properties**: Design tokens for colors, spacing, animations
2. **Gradient Backgrounds**: earth, ocean, forest, sunset themes
3. **Glassmorphism**: Semi-transparent cards with blur effects
4. **Smooth Animations**: Scroll reveals, hover effects, transitions
5. **Responsive Utilities**: Mobile-first breakpoints
6. **Component Classes**: .is-osgeo-hero, .is-osgeo-card, .is-osgeo-cta, etc.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-02-24 | Initial specification based on QGIS-Hugo template |
| 0.2.0 | 2025-02-24 | Complete redesign with vibrant theme, comprehensive information architecture, full content integration from osgeo.org |
