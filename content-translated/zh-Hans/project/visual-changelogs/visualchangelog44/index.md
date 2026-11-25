---
HasBanner: false
draft: false
releaseDate: '2026-11-20'
section: 工程
sidebar: true
title: Changelog for QGIS 4.4
type: visual-changelog

---
{{<content-start >}}
# Changelog for QGIS 4.4{#changelog44 }
<img src="images/projects/7a3290539a5412956dd2a6f0a0775190abf5fabe.png" class="img-responsive img-rounded center-block" />

Release date: 2026-11-20

[QGIS](https://qgis.org) (<https://qgis.org>) is the world's most popular (open source) desktop Geographical Information System (GIS). It is used by people around the world to view, edit, analyse, and share spatial data. It can produce professional-grade cartography products and supports hundreds of spatial data formats. QGIS is a member project of OSGEO, the Open Source Geospatial Foundation that is democratising access to spatial platforms (<https://osgeo.org>).

We are pleased to announce the new major release of QGIS 4.4, which builds on the solid foundation of the Major Version 4.0 update that transitioned the core of QGIS onto the modern Qt6 framework. This release is the Long Term Release (LTR) Candidate - the final LTR release will happen after 4 bug-fix rounds to stabilise this release and make it ready for a further year of stable support by the QGIS Community.

For a whirlwind tour of all the new functionalities introduced in this release, you can view the [highlight reel video on YouTube](https://www.youtube.com/watch?v=_bGc5CPNpNs).

<div class="tile video mb-3">
  <div class="youtube" data-video-id="_bGc5CPNpNs" style="background-image: url(&quot;https://img.youtube.com/vi/_bGc5CPNpNs/maxresdefault.jpg&quot;);">
    <iframe width="100%" height="100%" src="https://www.youtube.com/embed/_bGc5CPNpNs?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="true"></iframe>
  </div>
</div>

QGIS is a community effort, and we would like to extend a big thank-you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund others to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release!

If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions, large or small, to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very big thank you to all of our sponsors!

{{<fund type="active" level="flagship" >}}

[Click here to see all of our sustaining members]({{< ref "/funding/membership/members.md" >}})

QGIS is free software, and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of their financial or social status - we believe that empowering people with spatial decision-making tools will result in a better society for all of humanity.

{{<changelog-filter >}}

{{<changelog-category-start id="category-documentation" >}}
## 文档
{{<rich-box-start layoutClass="rounded" id="documentation-1" githubLink="https://github.com/qgis/QGIS/pull/67791" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add a Help button to the attribute table
The attribute table now has a context help button!<br /><img src="https://github.com/user-attachments/assets/bb85b8c7-c68c-45b1-b88e-a4dd5d198c50" width="649" height="51" alt="Image" />

This feature was funded by [Nelen & Schuurmans](https://www.nelen-schuurmans.nl)

This feature was developed by [Ben](https://github.com/benvanbasten-ns)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-user-interface" >}}
## 用户界面
{{<rich-box-start layoutClass="rounded" id="user-interface-1" githubLink="https://github.com/qgis/QGIS/pull/67745" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Disassociate welcome page visibility at startup from handling of project at startup
The welcome page visibility on app launch is now independent of the template and reload last project startup actions.<br /><img src="https://github.com/user-attachments/assets/d54b052c-ac49-4616-88fd-6e695489628e" width="1048" height="1012" alt="image" /><br />You can find options to manage this in the settings dialog.<br /><img src="https://github.com/user-attachments/assets/7cf56256-688c-4777-b18b-cc069328a4bb" width="1876" height="1470" alt="image" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-symbology" >}}
## 符号化
{{<rich-box-start layoutClass="rounded" id="symbology-1" githubLink="https://github.com/qgis/QGIS/pull/67477" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### "Opaque Fill" option in color menu
Before this change, the "transparent fill" option was always on, even if the fill color was already transparent. With this PR, if the color is 100% transparent, a new option is put in place of the other: "opaque fill". This allows quickly turning on/off which is more intuitive.<br /><img src="https://github.com/user-attachments/assets/67a25f27-b1f2-4333-bf90-b56b1dcea659" width="437" height="305" alt="image" /><br /><img src="https://github.com/user-attachments/assets/83fbea68-bbe1-42b4-8894-d036e9a33a09" width="437" height="305" alt="image" />

This feature was developed by [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="symbology-2" githubLink="https://github.com/qgis/QGIS/pull/67099" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add checkboxes to quickly enable or disable a symbol layer
Adds a checkbox next to the symbol layer to quickly enable or disable it, instead of having to scroll down to disable it.

<img src="images/entries/838842d893a18c4bbdd5a5720e613c013a3800e1.png" class="img-responsive img-rounded" />

This feature was funded by [The Switzerland QGIS user group](https://www.qgis.ch/fr/)

This feature was developed by [Celia Buira](https://github.com/CeliaBuira)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-annotations" >}}
## 注记
{{<rich-box-start layoutClass="rounded" id="annotations-1" githubLink="https://github.com/qgis/QGIS/pull/67101" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Annotation rotation (part 3): rotation aware map tools
Makes the annotation map tools aware of item rotation, completing the work split<br />out of \#66610 (after \#67035 and \#67036).<br />`QgsMapToolSelectAnnotation` draws the selection band and its mouse handles<br />rotated together with the item, and `QgsMapToolModifyAnnotation` places the<br />vertex handles on the rotated corners and supports resizing a rotated item by<br />dragging one of them. The drag keeps the opposite corner fixed on screen and<br />reconstructs the new (axis aligned) item bounds from the un-rotated diagonal.<br />To apply such a resize a new `QgsAnnotationItemEditOperationSetItemBounds`<br />edit operation is added, since the existing `MoveNode` operation can only set a<br />single corner of the unrotated bounds, which is not what a rotated resize<br />produces.<br />Tests are added for moving an item on a rotated canvas, rotating an item and<br />resizing a rotated item.

<img src="images/entries/f32b672f11cfcedd9397c1ebf0e4a8068055277f.png" class="img-responsive img-rounded" />

This feature was developed by [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="annotations-2" githubLink="https://github.com/qgis/QGIS/pull/66713" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Support text alignment for text on line annotation item types
Allows for text placement at end or center of line for the "text along line" annotation item type.

此功能由 North Road 资助，感谢 SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-labelling" >}}
## 标注
{{<rich-box-start layoutClass="rounded" id="labelling-1" githubLink="https://github.com/qgis/QGIS/pull/67437" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Render labels for selected features in a visible state
When rendering labels in a selected state, we render them using a buffer in the layer's selection color. This makes it immediately clear when a label belongs to a selected feature.<br />This is especially useful when a layer is set to show labels only, with the null symbol renderer.

<img src="images/entries/bb5336507508e5e07f88a246c1f33682a7b02a34.png" class="img-responsive img-rounded" />

This feature was funded by LINZ

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="labelling-2" githubLink="https://github.com/qgis/QGIS/pull/66815" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Support rotation for line horizontal labels
Allows setting the rotation angle for labels when set to the "horizontal" line placement mode.

此功能由 North Road 资助，感谢 SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-rendering" >}}
## 渲染
{{<rich-box-start layoutClass="rounded" id="rendering-1" githubLink="https://github.com/qgis/QGIS/pull/67112" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Elevation controller improvements
This makes the elevation filter widget usable without opening the project properties:<br />the elevation range can be set directly in the widget, it is filled from the layers when<br />the project does not define one, and the values it shows are round numbers.<br /><img src="https://github.com/user-attachments/assets/f0bddbe5-8574-45b1-a803-b0df8d989e1f" width="926" height="665" alt="image" /><br />**Settings menu**<br /><img src="https://github.com/user-attachments/assets/8a75ee0a-6a30-4060-87c7-b14f78a10727" width="695" height="112" alt="image" /><br />The settings menu of the elevation controller is now a single panel, similar to the<br />temporal controller:
- **Limits**: like for the temporal controller a button allows to define the limits from all project layers or from the current layer.
- **Range**: the value is now displayed even if not locked, a lock button is now used (or pressing enter)
- **Invert direction**.

The entry *Disable Elevation Filter* stays.<br />**Round values**
- Limits calculated from layers are rounded: `1234.5 - 3456.7` becomes `1200 - 3500`.
- The slider snaps to round values while dragging, so a 0 - 1000 slider moves in steps of 10.
- The slider also snaps to the elevations which are significant for the layers of the map when one of them is closer than the round value, so a handle can still be placed exactly on a layer surface.

**Starting values**<br />When the project has no elevation range of its own, the controller starts with the range<br />calculated from the layers of the canvas, instead of the arbitrary 0 - 100 default.<br />The elevation range of a raster layer is now calculated from the band statistics of its<br />elevation surface, so raster layers contribute a real range instead of nothing.<br />**Fixes**
- Some weird values in the slider when the limits are set after a range is locked.
- Canvas layers without elevation properties are ignored, this removes warnings in the message bar

**API**
- `QgsMathUtils::roundingInterval()` returns a round interval which splits a value span into a given number of parts
- `QgsMathUtils::roundedRange()` expands a range to round values.
- `QgsElevationUtils::calculateZRangeForLayers()` calculates the elevation range of a list of layers
- `QgsElevationControllerWidget::setMapCanvas()` gives the widget the canvas it belongs to. It provides the layer for the "Current Layer" entry, and its layers give the initial limits when the project defines no elevation range.
- `QgsElevationControllerSettingsAction` is now SIP_SKIP (but it was within @cond PRIVATE)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="rendering-2" githubLink="https://github.com/qgis/QGIS/pull/67486" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Vector Field renderer for raster layers
With the mesh vector rendering code now decoupled from mesh layers, we can finally introduce `QgsRasterVectorFieldRenderer`, a raster renderer that can draw arrows, streamlines, traces and wind barbs just like its mesh layer counterpart!<br />There are two main modes for generating vectors out of raster data:<br />**1. Use two distinct bands for X and Y components of vectors**<br /><img src="https://github.com/user-attachments/assets/88cc24cf-3791-4515-9fa0-ea343c9b1a05" height="200" alt="image" /><br />**2. Use a single band with integer encoded cardinal directions**<br />(see https://github.com/qgis/QGIS/issues/67108#issuecomment-5340069908)<br />Values not matching the encoding scheme are ignored.<br /><img src="https://github.com/user-attachments/assets/5706df59-1070-49d2-9483-b7db53935a95" height="200" alt="image" /><br />Once a mode and the required bands are selected, the rest of the UI is shared between the Raster and Mesh renderer.<br />**Showcase:**<br />**Arrows**<br /><img src="https://github.com/user-attachments/assets/26f9a85d-d7b4-4f1d-9a65-b4fedd230636" height="200" alt="image" /><br />**Wind Barbs**<br /><img src="https://github.com/user-attachments/assets/881b7a94-cd8d-40fc-b8b5-f3f26ae0d99e" height="200" alt="image" /><br />**Traces**<br /><img src="https://github.com/user-attachments/assets/13145387-2d88-4961-9b66-cc962843cb98" height="200" alt="image" />

This feature was funded by [Hans van der Kwast and a crowdfunding campaign](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-3d-features" >}}
## 3D Features
{{<rich-box-start layoutClass="rounded" id="3d-features-1" githubLink="https://github.com/qgis/QGIS/pull/66583" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add single color, unlit material type
This material does not interact with lights in the scene, resulting in a single color flat render

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-2" githubLink="https://github.com/qgis/QGIS/pull/67135" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add support for picture annotation items in 3d maps
We have extended the existing support for showing marker and text annotations as 3D billboards. Now you can show picture annotation items as 3d billboards too.<br />There is an option to show these as either view independent, fixed size billboards (just like markers and text), or as perspective correct sizes (eg like any other 3d item you can zoom in or out of).<br />The sizes of the 3d billboards are set manually, allowing the size to be set to one that makes sense in the 3d map (as opposed to strictly following the 2d size)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-3" githubLink="https://github.com/qgis/QGIS/pull/66981" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### 3d symbology widgets: simplify main panel and introduce an advanced panel
This implements the ideas discussed in [PR 66112](https://github.com/qgis/QGIS/pull/66112):<br />The old 3d symbology widgets had too much information and parameters, We reduced the number of displayed options and moved them into the advanced tab. This is achieved with 3 main changes:
- the 3d symbology parameters now has an advanced button and menu to switch to advanced settings
- material parameters: we display less parameters by default with a new "compact" style and only display all parameters in the advanced tab. This is done for lines, points and polygons.

**Points widget**<br /><img src="https://github.com/user-attachments/assets/14f32b39-8b3a-4c89-b127-503d35e9af92" height="200" alt="points" /><br />**Lines widget**<br /><img src="https://github.com/user-attachments/assets/56703ca4-e776-4af2-bab5-ad6a9d19e5c3" height="200" alt="line" /><br />**Polygons widget**<br /><img src="https://github.com/user-attachments/assets/8bc76d99-074c-4d08-a843-a18bff5ab2ff" height="200" alt="polygon" /><br />**advanced material panel**<br /><img src="https://github.com/user-attachments/assets/5725c506-d63e-4398-86ab-164bf3244905" height="200" alt="polygon-advanced" /><br />**Materials**<br />**Gooch**<br /><img src="https://github.com/user-attachments/assets/9a9581f6-343f-487f-9800-75dce65fae4f" height="200" alt="gooch" /><br />**Metal**<br /><img src="https://github.com/user-attachments/assets/dde662b5-2bae-4c02-b9fa-7cd0e0ca38be" height="200" alt="metal" /><br />**Metal texture**<br /><img src="https://github.com/user-attachments/assets/b93bd4ce-b593-419c-9f0d-d60deb67bd9d" height="200" alt="metal texture" /><br />**Phong**<br /><img src="https://github.com/user-attachments/assets/3af9cb27-a06f-493e-9a73-03ff988581ee" height="200" alt="phong" /><br />**Phong texture**<br /><img src="https://github.com/user-attachments/assets/3823281b-a926-4cf8-8246-e7c303db1ef2" height="200" alt="phong textured" /><br />**Single color**<br /><img src="https://github.com/user-attachments/assets/4bee6f0f-b67d-42c2-a2ef-3cd79e0c8761" height="200" alt="single color" />

This feature was developed by [Jean Felder](https://github.com/ptitjano)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-4" githubLink="https://github.com/qgis/QGIS/pull/66112" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add support for creating 3D symbology from 2D symbology
This adds a new "From 2D Symbology" entry to the 3D symbology combo box. This allows to create a new 3D symbology from the 2D one. If a 3d symbology already exists, it is replaced by this a new 3d symbology. This can be useful to quickly replicate 2D rules/categories or have similar colors between the 2D and 3D representations.<br />If the current 2D symbology style does not have a 3D equivalent, the entry is disabled.<br />For example, if the 2D symbology is "Categorized", it creates a 3D "Categorized" symbology, copies each category and tries to create 3d symbols based on the 3D one.

As there is no perfect match between the 2D symbols properties and the 3D symbol properties, only simple properties can be copied:<br />\| 2D Property \| 3D Equivalent \|<br />\|-------------------\|-------------------------------------------------------------\|<br />\| Fill color \| QgsMaterialSettings::setColorsFromBase(fillColor) \|<br />\| Opacity \| Opacity \|<br />\| Point size \| Sphere radius \|<br />\| Square size \| Cube size \|<br />\| Triangle size \| Cone length / topRadius / BottomRadius \|<br />\| Rule-based styles \| Each 2D rule becomes a 3D rule with the mapped properties \|<br />\| categorized styles \| Each 2D category becomes a 3D category with the mapped properties \|<br />**Categorized**<br /><img src="https://github.com/user-attachments/assets/b9e92da6-e61b-4ac3-ae42-1eac897b27f5" height="200" alt="image" /><br />**Rule-based**<br /><img src="https://github.com/user-attachments/assets/ec827505-db52-401d-8b17-ba71d78413b5" height="200" alt="image" /><br />**Single symbol**<br /><img src="https://github.com/user-attachments/assets/8ee6fe47-3ed1-4932-a316-c19b744fe3a4" height="200" alt="image" />

This feature was funded by Stadt Frankfurt am Main

This feature was developed by [Jean Felder](https://github.com/ptitjano)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-print-layouts" >}}
## 打印布局
{{<rich-box-start layoutClass="rounded" id="print-layouts-1" githubLink="https://github.com/qgis/QGIS/pull/67392" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add control over layout scale bar unit position
Instead of forcing the units to always be placed after the last distance label, users now have a choice of exactly where they want them placed.

Options are:
- Vertically centered on the bar, before the bar begins
- Vertically centered on the bar, after the bar ends
- Text centered over the left edge of the bar, above the bar
- Horizontally centered on the bar, above the bar
- Text centered over the right edge of the bar, above the bar
- Text centered over the left edge of the bar, below the bar
- Horizontally centered on the bar, below the bar
- Text centered over the right edge of the bar, below the bar
- Placed before the first distance label
- Placed after the last distance label
- Placed on top of the bar, after the first bar division
- Placed before every distance label (as part of the distance label text)
- Placed after every distance label (as part of the distance label text)

Multiple options may be selected, allowing for fully flexible unit label positioning.

<img src="images/entries/6550fd668b4b0e152e475a754923f9e3f14d3a95.png" class="img-responsive img-rounded" />

This feature was funded by The QGIS Swiss User Group

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-expressions" >}}
## 表达式
{{<rich-box-start layoutClass="rounded" id="expressions-1" githubLink="https://github.com/qgis/QGIS/pull/66772" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add version argument for uuid expression function
By default version 4 uuids are created. This new 'version' argument allows specifying an alternate uuid version to create. Supported values are 4 (current default) and 7.

<img src="images/entries/9b70f25047c670d893e11706c039858845adcfce.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="expressions-2" githubLink="https://github.com/qgis/QGIS/pull/66714" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add optional deflection angles to extend expression function
When specified, these will deflect the start or end extensions by the specified angle in degrees clockwise.

<img src="images/entries/d23f87740e4c95b474779dac087339923c98e7fe.png" class="img-responsive img-rounded" />

此功能由 North Road 资助，感谢 SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-digitising" >}}
## Digitising
{{<rich-box-start layoutClass="rounded" id="digitising-1" githubLink="https://github.com/qgis/QGIS/pull/67028" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Show dynamic label preview while editing vector features
For labeled vector layers, adds an immediate dynamic preview of the placement of the label while editing geometries.<br />Applies to move, offset, rotate scale and simplify tools (vertex tool to follow).<br />Some notes:
- There's no obstacle collision avoidance or overlap avoidance performed while showing this (in order to keep things performant), so you'll get different placement when applying the edits if another label is in the way
- The preview uses the exact same placement logic as the labeling engine uses, so everything shows as it should -- placement modes, spacing, repeats, drop shadows, etc.
- You'll still see the current label placement in the background (much like you still see the current feature geometry)

<img src="images/entries/e556e99c1e7d3b4a28950c2c46cc11e46036a75f.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-data-management" >}}
## Data Management
{{<rich-box-start layoutClass="rounded" id="data-management-1" githubLink="https://github.com/qgis/QGIS/pull/66462" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### GeoJSON profiles support (RFC7946, JSON-FG JSON-FG-PLUS core support)
Partial implementation of https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md<br />GeoJSON export now implements 4 distinct profiles for:
- Legacy : QGIS default behavior since this PR (i.e. supports different CRS than CRS84)
- RFC7946: GeoJSON compliant with RFC7946
- JSON-FG: OGC Features and Geometries JSON Part 1: core http://www.opengis.net/def/profile/OGC/0/jsonfg
- JSON-FG-PLUS: OGC Features and Geometries JSON Part 1: core http://www.opengis.net/def/profile/OGC/0/jsonfg-plus

Default behavior for existing JSON exports is unchanged, but new profiles provide the ability to export `M` (measures) and `ZM` geometries<br />This work is the result of a collective funding effort from:<br />QGIS Anwendergruppe Deutschland e.V. (QGIS-DE e.V.)<br />Gis3W<br />QTIBIA<br />Oslandia

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="data-management-2" githubLink="https://github.com/qgis/QGIS/pull/66545" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Drop db manager
In line with [QEP 426](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md) the db manager has now been replaced with a message bar element notifying users that they should install the replacement community edition plugin instead. The plugin has been moved to https://github.com/qgis/db_manager_plugin/tree/main, and has been submitted to the plugin repository at [plugins.qgis.org](https://plugins.qgis.org/plugins/db_manager_community).

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-forms-and-widgets" >}}
## 对话框和控件
{{<rich-box-start layoutClass="rounded" id="forms-and-widgets-1" githubLink="https://github.com/qgis/QGIS/pull/67963" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Implement attribute form QML editor widget's editing capabilities
Historically, the QML editor widget had the ability to display expression-driven values. It however had no ability to modify the feature being edited.<br />In this new version, the QML editor widget's scene has access to basic attribute form functionalities as well as reacting to changes such as an updated currentFormFeature and the editable state of the attribute form.

<img src="images/entries/809c3ba2ac98fc44d543cf40a5ab0ed119fdea68.png" class="img-responsive img-rounded" />

This feature was funded by [QGIS User Group Switzerland](https://www.qgis.ch/)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-processing" >}}
## 数据处理
{{<rich-box-start layoutClass="rounded" id="processing-1" githubLink="https://github.com/qgis/QGIS/pull/67464" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Optional "Maximum zoom extents" for XYZ algorithms
Allows users to specify sub-extents of the tiles to have greater detail (higher zoom level), allowing for more tiles to be generated in areas of greater interest.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-2" githubLink="https://github.com/qgis/QGIS/pull/67439" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### New algorithm to create XYZ raster tiles GeoPackage
Like the existing XYZ mbtiles/directory algorithms, but supports writing the tiles to a GeoPackage raster tiles dataset.<br />Also adds support for non-default (i.e. non web mercator) tileset generation for the GPKG and directory tiles algorithms, allowing for creation of tiles with custom tile matrices.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-3" githubLink="https://github.com/qgis/QGIS/pull/67408" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Allow webp as image format option for generate XYZ tiles algorithms
Allows creating tiles in the webp format.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-4" githubLink="https://github.com/qgis/QGIS/pull/67407" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Option to skip empty tiles in xyz tile algorithms
Fixes https://github.com/qgis/QGIS/issues/35174

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-5" githubLink="https://github.com/qgis/QGIS/pull/67389" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add native ports of SAGA's 'Channel Network and Drainage Basins'
Two new native algorithms have been added which are direct ports of the SAGA 'Channel Network and Drainage Basins' tool:
- Channel network and drainage basins from DEM: an all-in-one tool that requires only a DEM as the input
- 'Channel network and drainage basins from multiple inputs': a more efficient version of the tool for when the flow direction and Strahler orders have already been calculated.

The outputs are vector basins, channels and junctions.

This feature was funded by [Hans van der Kwast and a crowdfunding campaign](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-6" githubLink="https://github.com/qgis/QGIS/pull/67388" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Port SAGA D8 flow direction, connectivity, and Strahler order tools to native processing algorithms
- Adds a native "flow direction" algorithm, which is a direct port of the Flow Direction calculation from SAGA's "Channel Network and Drainage Basins" tool. It has been extracted as a standalone tool in Processing to allow for optimal use in QGIS models and workflows (as opposed to the all-in-one implementation in the SAGA equivalent).
- Add native "flow connectivity" algorithm, which is a direct port of the Flow Connectivity part of SAGA's "Channel Network and Drainage Basins" tool.
- Add two algorithms for calculating Strahler stream orders from DEMs. These algorithms expose ports of the Strahler calculation logic from SAGA's "Channel Network and Drainage Basins" tool. There are two versions of the algorithm available:
- "Strahler order from DEM": the only input required is a DEM, where the algorithm internally creates a flow direction grid
- "Strahler order from DEM and flow direction": requires both the DEM and pre-computed flow direction raster. This version is more efficient for scenarios when a flow direction raster has already been calculated.

These have all been extracted as standalone tools in Processing to allow for optimal use in QGIS models and workflows (as opposed to the all-in-one implementation in the SAGA equivalent).

This feature was funded by [Hans van der Kwast and a crowdfunding campaign](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-7" githubLink="https://github.com/qgis/QGIS/pull/67352" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Port SAGA Upslope Area tool to native processing algorithm
Adds a native port of SAGA'S "upslope area" tool. This is exposed in two different versions, refined for use in QGIS:
- "Upslope area (from point)": has a point parameter input, allowing the upslope area to be calculated for a single point
- "Upslope area (from layer)": has a point layer input, calculating the combined upslope contributing area for all target point locations from this layer

These are ALMOST 1:1 ports of the SAGA tools (adapted for optimal performance in QGIS API), with the exception of the "Multiple Maximum Downslope Gradient Based Flow Direction" method. The SAGA implementation of this method has a bug resulting in all output cells having either a 1 or 100 value. This is fixed here, making this method now correctly respect the math from the original paper by Qin et al (2011). (This was spotted by asking Gemini to validate the quality port compared to the original SAGA code, and by comparing to the original PDF versions of the paper. I've hand checked this against the original paper and the bug fix IS correct (and results in definitely more correct outputs) -- it's carefully annotated in the QGIS port source.) I've filed this issue with SAGA too so they can correct (See https://sourceforge.net/p/saga-gis/bugs/337/)

This feature was funded by [Hans van der Kwast and a crowdfunding campaign](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-8" githubLink="https://github.com/qgis/QGIS/pull/67285" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Native SAGA's thin plate spline interpolation tools
These are a direct port of SAGA's TPS interpolation tool, split into two separate processing algorithms to better match QGIS algorithm behavior.<br />The "Thin Plate Spline interpolation (global)" algorithm is a match for the default SAGA tool settings, where a single<br />global thin plate spline passing through all input points simultaneously is used for interpolation. This is suitable<br />only for datasets with lower point counts.<br />The "Thin Plate Spline interpolation (local)" algorithm is a match for setting the SAGA tool to use the local mode with a maximum search distance. A TPS is created for each individual raster pixel based on the closest points within this search distance. This version is optimised for use on very large point datasets.

This feature was funded by [Hans van der Kwast and a crowdfunding campaign](https://www.qwast-gis.com/l/crowdfunding-native-qgis-tools-for-hydrology/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-9" githubLink="https://github.com/qgis/QGIS/pull/67117" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Model designer "autocomplete"
We have extended the drag and drop ability with an "autocomplete" feature. When dragging a contextual toolbox appears that lists only the current compatible algorithms and parameters.<br />This makes it faster to create models, easier, and less error prone for users.<br />This is heavily inspired by the same feature in Blender node editor and also works in reverse to automatically select input parameters.<br />**How it works**<br />Start to drag any socket, and instead of connecting to another socket release anywhere on the canvas.<br />You're prompted with a toolbox with only the algorithm or parameter compatible with the socket you were dragging.<br />When adding the algorithm to the canvas it will connect to the first appropriate socket<br />On unlink the popup does not appear.

<img src="images/entries/50b46aecff18c5c50c048a3dd465af2b65e96aa0.png" class="img-responsive img-rounded" />

This feature was funded by [the Switzerland QGIS user group](https://www.qgis.ch/fr/)

This feature was developed by [Celia Buira](https://github.com/CeliaBuira)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-10" githubLink="https://github.com/qgis/QGIS/pull/66851" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Add profile selection options to qgis_process
You can now run qgis_process with a specific user profile, using the same options as QGIS Desktop. `--profile name` loads an existing named profile, and `--profiles-path path` (or `-S`) points to the folder that holds your `profiles` directory. A scheduled or server-side run can then use the Processing plugins, scripts and settings you set up in QGIS Desktop, without changing the default profile.<br />`qgis_process` always used the default user profile and profiles path, so a Processing script, plugin or setting that lives in another profile cannot be reached (#44783).<br />This adds the `--profile <name>` and `--profiles-path <path>` (`-S`) command-line options that QGIS Desktop already exposes:
- `--profile` loads an existing named profile from the profiles folder.
- `--profiles-path` / `-S` sets the folder that contains the `profiles` directory, and takes precedence over `QGIS_CUSTOM_CONFIG_PATH`.
- With only `--profiles-path`, the default profile recorded in that root's `profiles.ini` is used.
- With no profile option, the default profile is loaded through the same single `init()` call.
- A named `--profile` that does not exist is rejected (error, exit 1) and must be created and configured in QGIS Desktop first. The default profile is created on demand, so a run with no `--profile` needs no prior setup.

The profile is resolved before `QgsApplication::init()` and plugin loading, because the chosen profile decides where settings and plugins are read from. The `--help`/`--version` shortcut and the main parser share the same option handling, so with a valid value an informational query still works when a profile option comes first, while a missing, empty or option-like value is always an error (exit 1). A profile whose folder cannot be created, for example when the profiles path is unwritable or is a regular file, fails with the reason rather than running on a half-created profile.<br />This reuses Desktop's command-line option names and the `QgsUserProfileManager` path semantics. It does not reproduce the rest of Desktop's startup: the global `core/profilesPath` setting, the QGIS 3 to 4 profile migration and the interactive selection policy are unchanged and remain Desktop-only.<br />New executable tests (`test_qgsprocessexecutable_pt3.py`) cover the help output, profile-local script discovery, per-profile plugin enabled-state isolation, profiles-path isolation and precedence over `QGIS_CUSTOM_CONFIG_PATH`, the configured default profile, the short `-S` form, malformed and missing values, the `--` argument boundary, `--version`/`--help` ordering, rejection of an unknown named profile without creating a directory, on-demand creation of the default profile, JSON output and paths with spaces. They were run locally on Linux; the Windows and macOS packaging workflows build with `ENABLE_TESTS=OFF`, so they do not execute this suite.<br />This adds user-visible CLI flags, so it will need a matching documentation update.<br />Fixes [\#44783](https://github.com/qgis/QGIS/issues/44783)

<img src="images/entries/cec932b434ad8dfc9bcf1d29c98950cdbcb9a65b.png" class="img-responsive img-rounded" />

This feature was developed by [秀吉](https://github.com/thc1006)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-11" githubLink="https://github.com/qgis/QGIS/pull/66514" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Expose GEOS Coverage Cleaner functionality and add a processing algorithm for it
Exposes coverage cleaning feature from GEOS in QgsGeometry, and adds a new processing algorithm "Clean coverage" which operates on an imperfect coverage (polygon dataset), and cleans it by removing overlapping areas and closing small gaps between polygons to make a topologically correct coverage.<br />Requires a QGIS version built with a GEOS version of at least 3.14.0.<br />Fixes https://github.com/qgis/QGIS/issues/66513.

<img src="images/entries/c368d862da4b53996c70ab2744dc52da1879290a.png" class="img-responsive img-rounded" />

This feature was developed by [Juho Ervasti](https://github.com/JuhoErvasti)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-application-and-project-options" >}}
## Application and Project Options
{{<rich-box-start layoutClass="rounded" id="application-and-project-options-1" githubLink="https://github.com/qgis/QGIS/pull/67476" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Handle multi-directories for project templates
You can now specify multiple directories for project templates. This allows, for instance, having a team with its set of project templates, plus some templates coming from another centralized directory from an organization.<br />The sub-menu for creating a project from a template is only available if there is at least one project template in one template directory.<br />A toolbar button has been added to be consistent with the menu.<br />A new icon for project templates is proposed: <img src="https://github.com/user-attachments/assets/4e371268-1d34-494e-b0b5-c2a340ca76f5" width="33" height="33" alt="image" /><br />The welcome screen has been adapted to show the directories as sections.

<img src="images/entries/4d462d93f23e7d7db0035cba30ad628ecbf72db2.png" class="img-responsive img-rounded" />

This feature was funded by [Agence de l'eau Seine Normandie](https://www.eau-seine-normandie.fr/)

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-profile-plots" >}}
## Profile Plots
{{<rich-box-start layoutClass="rounded" id="profile-plots-1" githubLink="https://github.com/qgis/QGIS/pull/67484" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### "Fixed scale" mode for layout elevation profile ranges
The previous mode where the user explicitly set the min/max distance and elevation ranges is now labeled as "Manual Ranges". When the new "Fixed Scales" option is selected, the user can set an explicit scale for the distance and elevation axis separately.<br />The "minimum elevation" option is still available in "Fixed Scales" mode, so that it's still possible to start the elevation axis at a sensible minimum value and use the fixed scale to determine the maximum elevation for this axis.<br /><img src="https://github.com/user-attachments/assets/c7bfc858-9080-4d0c-9d6b-ff86f086fbba" width="367" height="174" alt="image" />

This feature was funded by the QGIS Swiss User Group

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-qgis-server" >}}
## QGIS服务器
{{<rich-box-start layoutClass="rounded" id="qgis-server-1" githubLink="https://github.com/qgis/QGIS/pull/66762" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Expose JSON-FG and time to QGIS server OAPIF
Expose JSON-FG and JSON-FG-PLUS (and RFC7946) as profiles for OGCAPI for features.<br />Also expose "time" dimension as in the specifications:<br />https://docs.ogc.org/is/21-045r1/21-045r1.html#time<br />https://docs.ogc.org/is/23-058r2/23-058r2.html#\_primary_temporal_information<br />This work is the result of a collective funding effort from:<br />QGIS Anwendergruppe Deutschland e.V. (QGIS-DE e.V.)<br />Gis3W<br />QTIBIA<br />Oslandia

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="qgis-server-2" githubLink="https://github.com/qgis/QGIS/pull/66495" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### QEP 414 - Various enhancements including feature schema
In support of the QGIS Server OAPIF JSON-FG and FlatGeobuf format implementations from [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md) new changes to the OGC API include:
- schema (including `x-ogc-role` , `format` and `type` for main widgets)
- references (from `RelationReference` and `ValueRelation`)
- profiles (for references)
- full crs support in requests and responses (includes `storageCrs` and `storageCrsCoordinateEpoch` if available)
- extra geometry columns support (Postgres), exposed as WKT (transformed to the requested CRS)
- codelist for enums and `ValueMap`
- new conformance classes

This feature was funded by [Geogirafe user group / OPENGIS.ch](http://opengis.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="qgis-server-3" githubLink="https://github.com/qgis/QGIS/pull/67343" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Support "default" value for Time dimension in WMS GetCapabilities
`default` parameter is part of the Dimension GetCapabilities tag. It serves to indicate default value that will be used if a GetMap request does not specify a value. As with vector layers you can choose the default display to be either the minimum or maximum value, a reference value to be set, or "all values" which is the current situation where no default value is written.<br /><img src="https://github.com/user-attachments/assets/d91e42a0-a036-4a5d-b28c-f206f7814780" width="626" height="918" alt="default" /><br />**Implementation detail**<br />We reuse WmsDimensionInfo for group because we can imagine later having other dimension configuration for group and to stay consistent with vector layer. At the moment, it's possible to have only a "TIME" dimension for groups.

This feature was funded by Ressources Naturelles Canada

This feature was developed by [Julien Cabieces](https://github.com/troopa81)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-programmability" >}}
## Programmability
{{<rich-box-start layoutClass="rounded" id="programmability-1" githubLink="https://github.com/qgis/QGIS/pull/67314" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Port SAGA 'Raster grid cell index' algorithm to new QgsSortedRasterBlockIndex API
Creates a flat index over a QgsRasterBlock, sorted by cell values.<br />Based on SAGA'S indexed CSG_Grid, used heavily in SAGA's terrain analysis toolkit.<br />Now includes a port of SAGA's "Grid Cell Index" tool as a native "Raster grid cell index" algorithm. This algorithm ranks valid non-NoData raster grid cells according to their value, outputting a new grid where each cell contains its 0-based sorted index (rank).

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="programmability-2" githubLink="https://github.com/qgis/QGIS/pull/66910" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Remove deprecated Processing WidgetWrapper subclasses
Implements Step 2 of https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-427-remove-deprecated-processing-gui-api.md.<br />Plugins which were still using these deprecated subclasses will need to adapt to the c++ processing gui, as detailed in the QEP.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-notable-fixes" >}}
## Notable Fixes
### Bug fixes by Alessandro Pasotti (QCooperative)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Temporary layer icon in layer tree can be missing on Windows | [\#67531](https://github.com/qgis/QGIS/issues/67531) | [PR \#67532](https://github.com/qgis/QGIS/pull/67532) | [PR \#67556](https://github.com/qgis/QGIS/pull/67556) |
| Attempting to "Set Comment..." on a postgres view in Browser results in an error | [\#67358](https://github.com/qgis/QGIS/issues/67358) | [PR \#67528](https://github.com/qgis/QGIS/pull/67528) | 否 |
| Transaction groups: after "Save Layer Edits", layers can no longer leave edit mode by rollback ("no such savepoint") | [\#67523](https://github.com/qgis/QGIS/issues/67523) | upstream GDAL issue [\#15294](https://github.com/OSGeo/gdal/issues/15294) | N/A |
| \[sqlite\]\[gpkg\] Savepoints are not removed after a COMMIT | [\#15294](https://github.com/OSGeo/gdal/issues/15294) |  | N/A |
| \[REGRESSION\] PostgreSQL database loading is significantly slower in QGIS 4.2 than 3.44 in the browse | [\#67454](https://github.com/qgis/QGIS/issues/67454) | [PR \#67585](https://github.com/qgis/QGIS/pull/67585) | N/A |
| Postgres "Set Comment" windows on Tables and Projects should word wrap rather than horizontally scroll | [\#67357](https://github.com/qgis/QGIS/issues/67357) | [PR \#67594](https://github.com/qgis/QGIS/pull/67594) | Not worth it |
| PostgreSQL: not all linked styles are loaded with the layer | [\#67181](https://github.com/qgis/QGIS/issues/67181) | [PR \#67619](https://github.com/qgis/QGIS/pull/67619) | N/A |
| Label word wrap character is considered after case change | [\#67501](https://github.com/qgis/QGIS/issues/67501) | [PR \#67767](https://github.com/qgis/QGIS/pull/67767/) | in progress |
| Feature rejected by the database is regarded as saved and lost with toggling edit mode | [\#67474](https://github.com/qgis/QGIS/issues/67474) | [PR \#67792](https://github.com/qgis/QGIS/pull/67792) | TODO |
| GDAL provider: raster in a mixed raster/vector GeoPackage gets the vector layers' CRS (or none) with GDAL \>= 3.12 | [\#67777](https://github.com/qgis/QGIS/issues/67777) | [PR \#67783](https://github.com/qgis/QGIS/pull/67783) | N/A |
| QGIS Server WMS GetMap request hangs displaying inverted polygon layer with shapeburst fill incl. blur strength | [\#67142](https://github.com/qgis/QGIS/issues/67142) | Cannot reproduce, closed |  |
| Feature rejected by the database is regarded as saved and lost with toggling edit mode | [\#67474](https://github.com/qgis/QGIS/issues/67474) | [PR \#67792](https://github.com/qgis/QGIS/pull/67792) |  |
| Adding a new feature through attribute table on an empty layer crashes QGIS | [\#65025](https://github.com/qgis/QGIS/issues/65025) | [PR \#67816](https://github.com/qgis/QGIS/pull/67816) Superceeded by Nyall's solution) |  |
| WMS GetCapabilities fails with "Decompression failed" on large capabilities documents (Qt6 decompressedSafetyCheckThreshold) | [\#66979](https://github.com/qgis/QGIS/issues/66979) | [PR \#67831](https://github.com/qgis/QGIS/pull/67831) | N/A |
| WMS GetCapabilities fails with gzip-encoded response (QGIS 4.0 / Qt6) | [\#65418](https://github.com/qgis/QGIS/issues/65418) | [PR \#67854](https://github.com/qgis/QGIS/pull/67854) | N/A |
| Color table ignored if sidecar xml with an attribute table exists in tiff images | [\#62579](https://github.com/qgis/QGIS/issues/62579) | [PR \#67875](https://github.com/qgis/QGIS/pull/67875) | N/A |
| WFS GetFeature fails with "Decompression failed" on large gzip responses (Qt6 decompressedSafetyCheckThreshold), no way to disable the check for WFS connections | [\#67970](https://github.com/qgis/QGIS/issues/67970) | [PR \#68010](https://github.com/qgis/QGIS/pull/68010) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Bug fixes by Julien Cabieces (Oslandia)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS4 customisation does not work | [\#67530](https://github.com/qgis/QGIS/issues/67530) | [PR \#67544](https://github.com/qgis/QGIS/pull/67544) | N/A |
| Raster calculator in 3.44LTR returns erraneous results | [\#67457](https://github.com/qgis/QGIS/issues/67457) | [PR \#67545](https://github.com/qgis/QGIS/pull/67545) | [PR \#67562](https://github.com/qgis/QGIS/pull/67562) |
| Status bar vanishes if UI customization is just enabled | [\#67590](https://github.com/qgis/QGIS/issues/67590) | [PR \#67660](https://github.com/qgis/QGIS/pull/67660) | N/A |
| Missing titles for customization item | Unreported | [PR \#67662](https://github.com/qgis/QGIS/pull/67662) | N/A |
| User Bookmarks are not migrated to QGIS 4 | [\#67583](https://github.com/qgis/QGIS/issues/67583) | [PR \#67667](https://github.com/qgis/QGIS/pull/67667) | N/A |
| QGIS 3 -\> QGIS 4 migration: QGIS starts the first time with the GUI translated to the system language instead of the custom one set | [\#65237](https://github.com/qgis/QGIS/issues/65237) | [PR \#67667](https://github.com/qgis/QGIS/pull/67667) | N/A |
| QGIS 3 -\> QGIS 4 migration: the paths stored inside QGIS3.ini are not correctly handled when transferred to QGIS4.ini | [\#65238](https://github.com/qgis/QGIS/issues/65238) | [PR \#67776](https://github.com/qgis/QGIS/pull/67776) | N/A |
| QGIS 3 -\> QGIS 4 migration: starting QGIS with --profiles-path and --profile options, QGIS3.ini is not copied to QGIS4.ini, instead a new QGIS4.ini is created | [\#65239](https://github.com/qgis/QGIS/issues/65239) | Won't fix |  |
| Fix drag'n drop in customization dialog | [\#67968](https://github.com/qgis/QGIS/issues/67968) | [PR \#67709](https://github.com/qgis/QGIS/pull/67709) | N/A |
| pluginManagerInterface().pluginMetadata() returns empty/error if Plugin Manager has never been opened | [\#67291](https://github.com/qgis/QGIS/issues/67291) | [PR \#67785](https://github.com/qgis/QGIS/pull/67785) | [PR \#67985](https://github.com/qgis/QGIS/pull/67985) |
| Adding a layout variable does not set the project dirty | [\#67261](https://github.com/qgis/QGIS/issues/67261) | [PR \#67789](https://github.com/qgis/QGIS/pull/67789) | [PR \#68004](https://github.com/qgis/QGIS/pull/68004) |
| Modifying a data defined override of a layout does not set the project dirty | [\#67262](https://github.com/qgis/QGIS/issues/67262) | [PR \#67804](https://github.com/qgis/QGIS/pull/67804) | [PR \#67984](https://github.com/qgis/QGIS/pull/67984) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Bug fixes by Jean Felder (Oslandia)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Filtering features from a WFS layer gives an error in QGIS 4.2 | [\#67715](https://github.com/qgis/QGIS/issues/67715) | [PR \#67813](https://github.com/qgis/QGIS/pull/67813) | N/A |
| TIN Interpolation Issue with break/structure lines | [\#66429](https://github.com/qgis/QGIS/issues/66429) | [PR \#67815](https://github.com/qgis/QGIS/pull/67815) | N/A |
| Font Marker bug in Elevation Profile window | [\#65865](https://github.com/qgis/QGIS/issues/65865) | [PR \#67818](https://github.com/qgis/QGIS/pull/67818) | N/A |
| DXF exporter writes UTF-8 encoded MTEXT while declaring ANSI_949 when CP949 encoding is selected | [\#67573](https://github.com/qgis/QGIS/issues/67573) | [PR \#67827](https://github.com/qgis/QGIS/pull/67827) | N/A |
| wrong nan check in QgsBox3D::isNull | Unreported | [PR \#67852](https://github.com/qgis/QGIS/pull/67852) | [PR \#67876](https://github.com/qgis/QGIS/pull/67876) |
| Elevation profile not recognising rule-based symbols | [\#56035](https://github.com/qgis/QGIS/issues/56035) | [PR \#67855](https://github.com/qgis/QGIS/pull/67855) | TODO |
| Elevation profile with raster DEM appears shifted | [\#58236](https://github.com/qgis/QGIS/issues/58236) | [PR \#67859](https://github.com/qgis/QGIS/pull/67859) | [PR \#67883](https://github.com/qgis/QGIS/pull/67883) |
| Elevation Profile: the Appearance setting Continuous Surface does not work anymore with Vector data | [\#64302](https://github.com/qgis/QGIS/issues/64302) | [PR \#67864](https://github.com/qgis/QGIS/pull/67864) | N/A |
| Continous Surface option no longer works in QGIS 3.38.1 | [\#58393](https://github.com/qgis/QGIS/issues/58393) | Cannot reproduce, closed |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Bug fixes by Loïc Bartoletti (Oslandia)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix build with LazPerf and Spatialindex | unreported on github, patches from FreeBSD | [PR \#67780](https://github.com/qgis/QGIS/pull/67780) | N/A |
| Fix chamfer/fillet | [\#67344](https://github.com/qgis/QGIS/issues/67344) | [PR \#67882](https://github.com/qgis/QGIS/pull/67882) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Bug fixes by Germán Carrillo (OPENGIS.ch)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Adapt test_core_expression to GEOS 3.15 | Unreported | [PR \#67592](https://github.com/qgis/QGIS/pull/67592) | N/A |
| GEOS 3.15: Splitting collections explodes the collection | [\#67478](https://github.com/qgis/QGIS/issues/67478) | [PR \#67650](https://github.com/qgis/QGIS/pull/67650) | N/A |
| \[geos\] Fix 'ZM' in QGIS-GEOS-QGIS conversions | Unreported | [PR \#67747](https://github.com/qgis/QGIS/pull/67747) | N/A |
| Loss of M values when splitting features | [\#40796](https://github.com/qgis/QGIS/issues/40796) | [PR \#67798](https://github.com/qgis/QGIS/pull/67798) | N/A |
| Building master fails when using dev version of GEOS | [\#67886](https://github.com/qgis/QGIS/issues/67886) | [PR \#67926](https://github.com/qgis/QGIS/pull/67926) | N/A |
| Pie Chart not working in version 3.34.9-Prizren | [\#62904](https://github.com/qgis/QGIS/issues/62904) | Not a bug | N/A |
| Add support for Z/M geometries in WFS Client | [\#57692](https://github.com/qgis/QGIS/issues/57692) | Already fixed | N/A |
| Different default M values depending on the function | [\#27792](https://github.com/qgis/QGIS/issues/27792) | Already fixed | N/A |
| Elevation Profile / QGIS 4: QgsPluginLayer do not show if other layers are visible | [\#66965](https://github.com/qgis/QGIS/issues/66965) | [PR \#67967](https://github.com/qgis/QGIS/pull/67967) | N/A |
| Count the number of features passing through the model | [\#15085](https://github.com/qgis/QGIS/issues/15085) | Already fixed | N/A |
| Crash splitting a CurvePolygon in QGIS master | [\#68203](https://github.com/qgis/QGIS/issues/68203) | [PR \#68220](https://github.com/qgis/QGIS/pull/68220) | N/A |
| CurvedPolygon Merging Converts True Arcs into Segments in QGIS | [\#60961](https://github.com/qgis/QGIS/issues/60961) | Already fixed | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Bug fixes by Alexander Bruy (QCooperative)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Export to GeoParquet silently writes 0 features: Save-As dialog clamps COMPRESSION_LEVEL default (-1) to 0, which is invalid for the default SNAPPY codec (GDAL 3.12) | [\#66822](https://github.com/qgis/QGIS/issues/66822) | Already fixed |  |
| Error and highest exectuion time of qgis:tilesxyzdirectory in QGIS 3.34.15-Prizren 'Prizren' (386f2583a69) | [\#60526](https://github.com/qgis/QGIS/issues/60526) | Already fixed |  |
| Error of the raster histogram | [\#38298](https://github.com/qgis/QGIS/issues/38298) | Cannot reproduce, closed |  |
| \[Processing\] "Distance to nearest hub" (native:distancetonearesthub) fails unless both outputs are set, although both are optional | [\#67548](https://github.com/qgis/QGIS/issues/67548) | [PR \#67549](https://github.com/qgis/QGIS/pull/67549) | [PR \#67551](https://github.com/qgis/QGIS/pull/67551) |
| Concave Hull algorithm generates incorrect output | [\#54561](https://github.com/qgis/QGIS/issues/54561) | Already fixed |  |
| Timezone is ignored when listing styles saved in the GeoPackage | Unreported | [PR \#67554](https://github.com/qgis/QGIS/pull/67554) | [PR \#67579](https://github.com/qgis/QGIS/pull/67579) |
| Duplicate styles returned when listing styles in the geopackage | Unreported | [PR \#67577](https://github.com/qgis/QGIS/pull/67577) | [PR \#67604](https://github.com/qgis/QGIS/pull/67604) |
| Wrong render of Help page in GDAL creation options setting | [\#47433](https://github.com/qgis/QGIS/issues/47433) | [PR \#67588](https://github.com/qgis/QGIS/pull/67588) | N/A |
| shadow in raster histogram plot area can confuse | [\#41113](https://github.com/qgis/QGIS/issues/41113) | [PR \#67614](https://github.com/qgis/QGIS/pull/67614) | N/A |
| SensorThings provider reads HTTP header settings from wrong section | Unreported | [PR \#67639](https://github.com/qgis/QGIS/pull/67639) | [PR \#67679](https://github.com/qgis/QGIS/pull/67679) |
| Styles stored inside a GeoPackage are not found anymore by QGIS | [\#58467](https://github.com/qgis/QGIS/issues/58467) | [PR \#67607](https://github.com/qgis/QGIS/pull/67607) | [PR \#67846](https://github.com/qgis/QGIS/pull/67846) |
| Unable to parse vector tiles XML generated in QGIS 3 | [\#65477](https://github.com/qgis/QGIS/issues/65477) | [PR \#67647](https://github.com/qgis/QGIS/pull/67647) | [PR \#67680](https://github.com/qgis/QGIS/pull/67680) |
| Updating raster single-band min/max method does not update actual min/max | [\#26593](https://github.com/qgis/QGIS/issues/26593) | [PR \#67666](https://github.com/qgis/QGIS/pull/67666) | N/A |
| qgis.testing.start_app() log output is silent since QGIS 4.0: QgsMessageLog.messageReceived(message, tag, level) is never emitted | [\#67668](https://github.com/qgis/QGIS/issues/67668) | [PR \#67670](https://github.com/qgis/QGIS/pull/67670) | N/A |
| Toolbuttons with popups are missing in overflow menus | [\#58641](https://github.com/qgis/QGIS/issues/58641) | [PR \#67690](https://github.com/qgis/QGIS/pull/67690) | N/A |
| WCS GetCoverage - Problem with GRIDORIGIN and GRIDOFFSETS with latitude/longitude CRS (EPSG:4326 and EPSG:4617) | [\#59445](https://github.com/qgis/QGIS/issues/59445) | [PR \#67760](https://github.com/qgis/QGIS/pull/67760) | [PR \#67781](https://github.com/qgis/QGIS/pull/67781) |
| drop QTEST_DISABLE_KEYPAD_NAVIGATION from tests (fix broken build on Qt 6.12) | Unreported | [PR \#67763](https://github.com/qgis/QGIS/pull/67763) | N/A |
| Zonal statistics only works with shapefiles | [\#46602](https://github.com/qgis/QGIS/issues/46602) | [PR \#67765](https://github.com/qgis/QGIS/pull/67765) | [PR \#67850](https://github.com/qgis/QGIS/pull/67850) |
| Deprecation warning in GPX provider | Unreported | [PR \#67782](https://github.com/qgis/QGIS/pull/67782) | N/A |
| WCS layers with query string will lose the query string parameter when calling the GetCoverage method | [\#52842](https://github.com/qgis/QGIS/issues/52842) | [PR \#67811](https://github.com/qgis/QGIS/pull/67811) | [PR \#67851](https://github.com/qgis/QGIS/pull/67851) |
| XYZ tiles from local files no longer works in 4.X series | [\#66518](https://github.com/qgis/QGIS/issues/66518) | [PR \#67879](https://github.com/qgis/QGIS/pull/67879) | N/A |
| Symmetric Classification in graduated symbol cant turn off | [\#65853](https://github.com/qgis/QGIS/issues/65853) | [PR \#67902](https://github.com/qgis/QGIS/pull/67902) | [PR \#67947](https://github.com/qgis/QGIS/pull/67947) |
| QGIS does not use TRANSPARENT=FALSE advertise by the WMS capabilities | [\#42951](https://github.com/qgis/QGIS/issues/42951) | Cannot reproduce, closed |  |
| Layout Charts: Only the first color ramp is used for all the series in a pie chart | [\#67159](https://github.com/qgis/QGIS/issues/67159) | [PR \#67954](https://github.com/qgis/QGIS/pull/67954) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Bug fixes by Celia Buira (OPENGIS.ch)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Prevent multiple model designer window to override model changes | Unreported | [PR \#68000](https://github.com/qgis/QGIS/pull/68000) |  |
| View Output Layers feature from model designer doesn't work if spatial index is applied on vec. layer | [\#67743](https://github.com/qgis/QGIS/issues/67743) | [PR \#68076](https://github.com/qgis/QGIS/pull/68076) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Celia Buira (OPENGIS.ch)](http://opengis.ch/)
### Bug fixes by Stefanos Natsis (Lutra Consulting)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Guard against writing out of bounds in array_insert | Unreported | [PR \#67888](https://github.com/qgis/QGIS/pull/67888) | N/A |
| Fix identifying and highlighting point cloud points in 3d views with different crs | Unreported | [PR \#67990](https://github.com/qgis/QGIS/pull/67990) | 否 |
| Make sure the style manager page is not first for point cloud layers | Unreported | [PR \#67991](https://github.com/qgis/QGIS/pull/67991) | N/A |
| Fix vpc labels when layer crs does not match map crs | Unreported | [PR \#68009](https://github.com/qgis/QGIS/pull/68009) | 否 |
| Fix point cloud editing when layer and map crs do not match | Unreported | [PR \#68015](https://github.com/qgis/QGIS/pull/68015) | 否 |
| Fix global map shading state when starting a new project | Unreported | [PR \#68021](https://github.com/qgis/QGIS/pull/68021) | [PR \#68047](https://github.com/qgis/QGIS/pull/68047) |
| Impossible to cancel movement of annotation items | [\#66701](https://github.com/qgis/QGIS/issues/66701) | [PR \#68028](https://github.com/qgis/QGIS/pull/68028) | N/A |
| Enable keyboard navigation in welcome screen | [\#64891](https://github.com/qgis/QGIS/issues/64891) | [PR \#68070](https://github.com/qgis/QGIS/pull/68070) | N/A |
| Hide welcome screen when new project is clicked | Unreported | [PR \#68071](https://github.com/qgis/QGIS/pull/68071) | N/A |
| adding layer with custom QgsRasterDataProvider crashes QGIS | [\#59284](https://github.com/qgis/QGIS/issues/59284) | [PR \#68101](https://github.com/qgis/QGIS/pull/68101) | 否 |
| Elevation Profile's layer tree: drag&drop layer appears twice | [\#64957](https://github.com/qgis/QGIS/issues/64957) | [PR \#68104](https://github.com/qgis/QGIS/pull/68104) | 否 |
| Fix out of bounds read in levenshtein implementation | Unreported | [PR \#68130](https://github.com/qgis/QGIS/pull/68130) | [PR \#68199](https://github.com/qgis/QGIS/pull/68199) |
| Welcome page: Unable to open a blank project when QGIS is launched with the recent project by default | [\#68121](https://github.com/qgis/QGIS/issues/68121) | [PR \#68139](https://github.com/qgis/QGIS/pull/68139) | N/A |
| Assert hit when aborting the deletion of an attribute used for sorting | [\#68157](https://github.com/qgis/QGIS/issues/68157) | [PR \#68158](https://github.com/qgis/QGIS/pull/68158) | 否 |
| Default Styles not available | [\#68160](https://github.com/qgis/QGIS/issues/68160) | [PR \#68164](https://github.com/qgis/QGIS/pull/68164) | N/A |
| Preselect http/https/ftp when adding data using protocol | Unreported | [PR \#68167](https://github.com/qgis/QGIS/pull/68167) | 否 |
| .slpk I3S meshes do not work with QGIS4 | [\#66100](https://github.com/qgis/QGIS/issues/66100) | [PR \#68185](https://github.com/qgis/QGIS/pull/68185) | 否 |
| Fix rendering I3S layers where i3s-scale_x/y is defined | [\#66100](https://github.com/qgis/QGIS/issues/66100) | [PR \#68187](https://github.com/qgis/QGIS/pull/68187) | 否 |
| Fix QT warning for submenu's parent | Unreported | [PR \#68188](https://github.com/qgis/QGIS/pull/68188) | 否 |
| CVS / delimited text file provider filter returns zero features when there is a space in the column name | [\#68189](https://github.com/qgis/QGIS/issues/68189) | [PR \#68194](https://github.com/qgis/QGIS/pull/68194) | 否 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Bug fixes by Jan Caha (Lutra Consulting)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Handle QgsInterval in expressions for PG driver | [\#62577](https://github.com/qgis/QGIS/issues/62577) | [PR \#68066](https://github.com/qgis/QGIS/pull/68066) |  |
| Do not estimate extent for TopoGeometry | [\#60593](https://github.com/qgis/QGIS/issues/60593) | [PR \#68057](https://github.com/qgis/QGIS/pull/68057) |  |
| Fix potentially long load time for schemata with QGIS projects in Browser | [\#66990](https://github.com/qgis/QGIS/issues/66990) | [PR \#68052](https://github.com/qgis/QGIS/pull/68052) |  |
| Issues in 3d editing Point Cloud Widget | Unreported | [PR \#68020](https://github.com/qgis/QGIS/pull/68020) |  |
| "Build virtual point cloud (VPC)" algorithm should only support VPC and VPZ | Unreported | [PR \#68005](https://github.com/qgis/QGIS/pull/68005) |  |
| ELSE Rule based renderer feature counts | [\#27893](https://github.com/qgis/QGIS/issues/27893) | [PR \#67989](https://github.com/qgis/QGIS/pull/67989) |  |
| Add -cwhere for gdalwarp when Clipping raster using vector layer with Feature filter | [\#67383](https://github.com/qgis/QGIS/issues/67383) | [PR \#67928](https://github.com/qgis/QGIS/pull/67928) |  |
| gdal_connection_details_from_layer() for vsiPrefix GDAL/OGR sources | [\#61144](https://github.com/qgis/QGIS/issues/61144) | [PR \#67823](https://github.com/qgis/QGIS/pull/67823) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jan Caha (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Bug fixes by Nyall Dawson (North Road)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix crash in labeling | [\#68210](https://github.com/qgis/QGIS/issues/68210) | [PR \#68234](https://github.com/qgis/QGIS/pull/68234) | [PR \#68247](https://github.com/qgis/QGIS/pull/68247) |
| Fixes crash when adding field to empty table via attribute table |  | [PR \#68146](https://github.com/qgis/QGIS/pull/68146) |  |
| Remove not safe postgres layer name logic |  | [PR \#68145](https://github.com/qgis/QGIS/pull/68145) |  |
| Fixes crash when pasting items in a new empty model | [\#68100](https://github.com/qgis/QGIS/issues/68100) | [PR \#68143](https://github.com/qgis/QGIS/pull/68143) |  |
| Fix crash if project is closed while new feature dialog is open |  | [PR \#68112](https://github.com/qgis/QGIS/pull/68112) |  |
| Fix overlapping widgets in 3d config dialog |  | [PR \#68111](https://github.com/qgis/QGIS/pull/68111) |  |
| \[afs\] Handle case mismatches between service level feature names and json | [\#67979](https://github.com/qgis/QGIS/issues/67979) | [PR \#67983](https://github.com/qgis/QGIS/pull/67983) |  |
| Fix failing tests - Don't update project when setting snap widget initial state from project |  | [PR \#67956](https://github.com/qgis/QGIS/pull/67956) |  |
| Prevent recursion when editing columns |  | [PR \#67949](https://github.com/qgis/QGIS/pull/67949) |  |
| Fix hang when rendering labels with huge angle values | [\#67885](https://github.com/qgis/QGIS/issues/67885) | [PR \#67913](https://github.com/qgis/QGIS/pull/67913) | [PR \#67948](https://github.com/qgis/QGIS/pull/67948) |
| Use more efficient way to handle loading old projects with font marker fix- \#67914 | [\#67901](https://github.com/qgis/QGIS/issues/67901) | [PR \#67914](https://github.com/qgis/QGIS/pull/67914) |  |
| Fix missing feature count in model after model run completes | [\#67874](https://github.com/qgis/QGIS/issues/67874) | [PR \#67896](https://github.com/qgis/QGIS/pull/67896) |  |
| Fix leak of QCompleter objects- \#67894 |  | [PR \#67894](https://github.com/qgis/QGIS/pull/67894) |  |
| Speed up like expressions |  | [PR \#67871](https://github.com/qgis/QGIS/pull/67871) |  |
| Fix leak in QgsAttributesFormLayoutModel |  | [PR \#67870](https://github.com/qgis/QGIS/pull/67870) |  |
| Speed up unaccent function, restore use in searches |  | [PR \#67868](https://github.com/qgis/QGIS/pull/67868) |  |
| Fix issues in attribute table model | [\#65025](https://github.com/qgis/QGIS/issues/65025) | [PR \#67856](https://github.com/qgis/QGIS/pull/67856) |  |
| Introduce widgets for choice of time zone, QDateTime with explicit time zone | [\#67496](https://github.com/qgis/QGIS/issues/67496) | [PR \#67820](https://github.com/qgis/QGIS/pull/67820) |  |
| Fix selective masking issues with opacity/blend modes | [\#49488](https://github.com/qgis/QGIS/issues/49488) | [PR \#67810](https://github.com/qgis/QGIS/pull/67810) |  |
| Fix some minor leaks |  | [PR \#67808](https://github.com/qgis/QGIS/pull/67808) |  |
| Fix leak in expression parsing |  | [PR \#67806](https://github.com/qgis/QGIS/pull/67806) |  |
| Massively speed up parallel rendering of expression-heavy projects | [\#67718](https://github.com/qgis/QGIS/issues/67718) | [PR \#67771](https://github.com/qgis/QGIS/pull/67771) |  |
| Fix leak of unparented objects |  | [PR \#67770](https://github.com/qgis/QGIS/pull/67770) |  |
| Fix leak of QgsVersionInfo in welcome screen |  | [PR \#67677](https://github.com/qgis/QGIS/pull/67677) |  |
| Fix leak of thread local QSettings |  | [PR \#67676](https://github.com/qgis/QGIS/pull/67676) |  |
| When changing a raster to single band psuedocolor, use default color ramp |  | [PR \#67674](https://github.com/qgis/QGIS/pull/67674) |  |
| \[mssql\] Fix handling of srid |  | [PR \#67653](https://github.com/qgis/QGIS/pull/67653) | [PR \#67673](https://github.com/qgis/QGIS/pull/67673) |
| Fix crash when grouping layout items | [\#61702](https://github.com/qgis/QGIS/issues/61702) | [PR \#67661](https://github.com/qgis/QGIS/pull/67661) |  |
| Fix crash when opening context menu on non-database browser layers |  | [PR \#67658](https://github.com/qgis/QGIS/pull/67658) |  |
| Fix parent ownership of QObject map layer children |  | [PR \#67656](https://github.com/qgis/QGIS/pull/67656) |  |
| \[mssql\] Fix loss of srid/wkbtype during initialization | [PR \#67672](https://github.com/qgis/QGIS/pull/67672) | [PR \#67654](https://github.com/qgis/QGIS/pull/67654) |  |
| Fix missing CRS info in tooltips for layers with custom CRS |  | [PR \#67652](https://github.com/qgis/QGIS/pull/67652) |  |
| Fix crash when switching between raster layers which support histograms vs not |  | [PR \#67651](https://github.com/qgis/QGIS/pull/67651) |  |
| Fix crash when changing style through layer style dock style manager |  | [PR \#67599](https://github.com/qgis/QGIS/pull/67599) |  |
| Fix docked attribute tables open side-by-side, not tabbed | [\#65633](https://github.com/qgis/QGIS/issues/65633) | [PR \#67572](https://github.com/qgis/QGIS/pull/67572) | [PR \#67644](https://github.com/qgis/QGIS/pull/67644) |
| Ensure layer IDs never become too long | [\#67164](https://github.com/qgis/QGIS/issues/67164) | [PR \#67570](https://github.com/qgis/QGIS/pull/67570) |  |
| Fix exceptions when running algorithms that output html files in batch mode |  | [PR \#67560](https://github.com/qgis/QGIS/pull/67560) | [PR \#67567](https://github.com/qgis/QGIS/pull/67567) |
| Remove non-functional pre/post execution script setting | [\#44651](https://github.com/qgis/QGIS/issues/44651) | [PR \#67559](https://github.com/qgis/QGIS/pull/67559) | [PR \#67569](https://github.com/qgis/QGIS/pull/67569) |
| Fix exporting animations in Movie mode from temporal controller |  | [PR \#67494](https://github.com/qgis/QGIS/pull/67494) |  |
| Fix QgsAbstractProcessingParameterWidgetWrapper use through PyQGIS- \#67491 | [\#67401](https://github.com/qgis/QGIS/issues/67401) | [PR \#67491](https://github.com/qgis/QGIS/pull/67491) | [PR \#67511](https://github.com/qgis/QGIS/pull/67511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<changelog-category-end >}}

{{<content-end >}}
