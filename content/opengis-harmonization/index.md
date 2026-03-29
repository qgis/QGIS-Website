---
type: "page"
title: "OpenGIS Harmonization"
subtitle: "Coordinating the org.opengis Java Package"
description: "An OSGeo initiative addressing the coordination of the org.opengis Java package among OSGeo, OGC, and Apache Foundation stakeholders."
draft: false
heroSize: "is-medium"
HeroImage: "/img/banners/banner2.png"
HasBanner: true
---

{{< box-start class="is-light2 p-5 mb-6" >}}
This OSGeo initiative addresses the coordination of the **org.opengis** Java package among OSGeo, OGC, and Apache Foundation stakeholders.
{{< box-end >}}

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-circle-info"></i>
<span>Background</span>
</div>
<h2 class="section-title">Core Purpose</h2>
</div>

The GeoTools project participated early in GeoAPI development. The OGC has now published GeoAPI v3 and requested exclusive use of the org.opengis package, requiring a coordinated response.

---

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-bullseye"></i>
<span>Goals</span>
</div>
<h2 class="section-title">Initiative Goals</h2>
</div>

Four primary outcomes are targeted:

{{< columns-start >}}

{{< column-start class="is-6" >}}

{{< rich-box-start icon="fa-solid fa-code" >}}
### 1. Refactor GeoTools

Refactor GeoTools' use of org.opengis interfaces to remove dependency on the contested namespace.
{{< rich-box-end >}}

{{< rich-box-start icon="fa-solid fa-trash" >}}
### 2. Remove Unused Interfaces

Remove unused interfaces lacking sustained investment, notably the Geometry interfaces.
{{< rich-box-end >}}

{{< column-end >}}

{{< column-start class="is-6" >}}

{{< rich-box-start icon="fa-solid fa-rotate-left" >}}
### 3. Rollback Design Changes

Rollback certain design changes made for GeoAPI adoption that no longer serve the project.
{{< rich-box-end >}}

{{< rich-box-start icon="fa-solid fa-file-code" >}}
### 4. Migration Scripts

Provide migration scripts for downstream projects to reduce disruption from API changes.
{{< rich-box-end >}}

{{< column-end >}}

{{< columns-end >}}

---

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-calendar"></i>
<span>Schedule</span>
</div>
<h2 class="section-title">Timeline</h2>
</div>

| Date | Event |
|------|-------|
| **April 2023** | Open Standards and Open Source Software Code Sprint for initiative promotion |
| **June 2023** | FOSS4G Code Sprint for design and planning |
| **August 2023** | Bolsena Code Sprint focused on GeoTools refactoring |
| **September 2023** | GeoTools 30.0 release with API changes |

---

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-diagram-project"></i>
<span>Impact</span>
</div>
<h2 class="section-title">Affected Projects</h2>
</div>

Multiple downstream projects require updates as a result of this initiative:

{{< columns-start >}}

{{< column-start class="is-4" >}}

- GeoServer
- GeoNetwork
- GeoWebCache
- GeoMajas

{{< column-end >}}

{{< column-start class="is-4" >}}

- GeoMesa
- GeoWave
- GeoTrellis

{{< column-end >}}

{{< column-start class="is-4" >}}

- And many more projects across Maven repositories

{{< column-end >}}

{{< columns-end >}}

---

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-heart"></i>
<span>Support</span>
</div>
<h2 class="section-title">Sponsorship</h2>
</div>

The initiative receives partial funding through the OSGeo 2023 Budget as a priority activity. Additional sponsorship is welcome to complete the cross-project collaboration effort.

[Become a Sponsor &rarr;](/sponsors/)

---

{{< box-start class="cta-section my-6" >}}

<div class="section-header">
<div class="section-header-badge">
<i class="fa-solid fa-hand-point-right"></i>
<span>Action</span>
</div>
<h2 class="section-title has-text-white">Related Projects</h2>
</div>

{{< button-bar
    button1-text="View GeoTools"
    button1-link="/projects/geotools/"
    button1-class="button is-white is-large"
    button2-text="All Projects"
    button2-link="/projects/"
    button2-class="button is-outlined is-white is-large"
>}}

{{< box-end >}}
