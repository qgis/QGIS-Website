---
HasBanner: false
draft: false
releaseDate: '2026-07-03'
section: έργο
sidebar: true
title: Changelog for QGIS 4.2
type: visual-changelog

---
{{<content-start >}}
# Changelog for QGIS 4.2{#changelog42 }
<img src="images/projects/b7fa0af07e61fe7036f463d15cbba685c11baae2.png" class="img-responsive img-rounded center-block" />

Release date: 2026-07-03

[QGIS](https://qgis.org) (<https://qgis.org>) is the world's most popular (open source) desktop Geographical Information System (GIS). It is used by people around the world to view, edit, analyse, and share spatial data. It can produce professional-grade cartography products and supports hundreds of spatial data formats. QGIS is a member project of OSGEO, the Open Source Geospatial Foundation that is democratising access to spatial platforms (<https://osgeo.org>).

We are pleased to announce the new major release of QGIS 4.2, which builds on the solid foundation of the Major Version 4.0 update that transitioned the core of QGIS onto the modern Qt6 framework. This release also bundles loads of performance optimizations and newly introduced features, including multiple enhancements to 3D capabilities and processing tools.

For a whirlwind tour of all the new functionalities introduced in this release, you can view the [highlight reel video on YouTube](https://www.youtube.com/watch?v=5X1JKx7CXZY).

[![](https://img.youtube.com/vi/5X1JKx7CXZY/0.jpg)](https://www.youtube.com/watch?v=5X1JKx7CXZY)

QGIS is a community effort, and we would like to extend a big thank-you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund others to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release!

If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions, large or small, to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very big thank you to all of our sponsors!

QGIS is free software, and you are under no obligation to pay anything to use it - in fact, we want to encourage people far and wide to use it regardless of their financial or social status - we believe that empowering people with spatial decision-making tools will result in a better society for all of humanity.
## Breaking Changes
### Feature: Move QGIS4 settings storage location with automated migration from QGIS3
In order to prevent configuration file corruption between changes made to user settings on both QGIS3 and QGIS4 on the same system, the QGIS 4 settings are now completely siloed into a separate directory.<br />**PLEASE NOTE: This will affect automated installation scripts, profile management, and enterprise deployments.**<br />On initial startup, QGIS4 will perform a copy of user profile data from the existing QGIS3 path and clone the settings to a new QGIS4 path. Automated deployments and profile management scripts must be updated to target this new location. This resolves reported issues [\#61636](https://github.com/qgis/QGIS/issues/61636) and [\#60088](https://github.com/qgis/QGIS/issues/60088).<br />Please note:
- This is a ONE TIME ONLY migration
- The migration losslessly preserves existing settings of the LOADED USER PROFILE
- Subsequent profile changes will not sync between QGIS3 and QGIS4

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## User Interface
### Feature: Add layer menu to load and save styles
This adds **Load Style...** and **Save Style...** options directly to the layer menu under the **Styles** submenu. This will provide users with a quick way to load/save style on a layer, without the need to open another interface or menu.

<img src="images/entries/3649f31a4a1358779fd933bddce5e20161257fd9.png" class="img-responsive img-rounded" />

This feature was developed by [Jan Caha](https://github.com/JanCaha)
## Σύμβολα
### Feature: Add categorized renderer for 3D Symbols
Categorized and rule-based rendering is now available for QGIS 3D Symbology.<br />Both implementations are similar to the existing vector renderers for 2D styling, so that users have familiar controls for 3D scenes, whilst multiple API enhancements have been applied to support this powerful set of functionalities.

<img src="images/entries/c5fb95c208d6bc03a05ac923f019475a50310cb6.png" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Add physically based material with texture support
A new 3d material type for exposing the physically based material with full texture map support has been added.<br />Textures can be specified for:
- base color
- metalness
- roughness
- ambient occlusion

<img src="images/entries/ee3d3005794174302de3f65232c8cace82357987.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add trim distance start and end to Hashes/Markers line symbol layer
This extends capabilities already existing for simple line to hashes and markers line symbol layers.

<img src="images/entries/bb0088d635bc91e52e14fec777c191861410d687" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main and Oslandia

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: Add data-defined control for metal rough base, emission color
A data-defined control for metal rough base and emission color has been added, closing one of the few remaining functionality gaps between the legacy phong materials and the physically based material.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Data defined control over phong/metal rough texture scale, rotation and offset
A data-defined control has been added for control over the texture scale, rotation, and offset for 3D polygons when using either the metal rough or phong textured materials.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add optional solid emission color to metal rough material
A new, non-default, solid emission color setting has been added to the metal rough material, along with a spin box to also control the strength of the emission. Practically, this allows users to create materials that are not impacted by scene lighting.<br />The attached image shows a comparison of dark scene lighting with no emission, yellow emission at 100%, and yellow emission at 1000% to demonstrate the effect of this functionality.

<img src="images/entries/260c863c37dddb6f738615df50851b8eb06185bf.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add opacity support to metal rough materials
Physically based rendering materials now support opacity, bringing their capabilities closer to the older phong material capabilities.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add 3d material settings to style database
QGIS now includes support for managing 3d material settings in the style database (and style manager dialog).<br />Users can create presets of 3d materials and manage them alongside other style objects (e.g., allowing metadata such as tagging, favourites, etc.).

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Allow choice of up/forward axis for 3d point model symbols
Instead of always assuming the model file has been created using a z up, y forward axis convention, expose settings to allow users to manually set the forward and up axes.<br />This makes it easier to use random obj files downloaded from the internet as 3d point symbols in QGIS. Previous workarounds required manually rotating the symbol, but this prevented the reuse of rotation/scale values and data-defined expressions used by other 3d point symbols.

<img src="images/entries/70b6d2509f1fb98c8a582a95c7abe3d58c22066a.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add extra items for templated line symbol layer
Tools are now provided to create, move, rotate and delete new markers/hashes for marker/hash line symbol layer.<br />Those new markers will share the same style as the original markers, the same selected or visibly state.<br />This is the implementation of [QEP \#406](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/356).

<img src="images/entries/ab98e9fb9b4fd3111e4329ec44cf60c777761fd6" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main and Oslandia\*\*

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## 3D Features
### Feature: Generate environmental lighting from skybox
New environmental lighting effects have been added to the physically based materials when a cube map skybox is in place. Environmental lights are calculated dynamically from the skybox textures.<br />These effects use the spherical harmonic approximation for the irradiance to avoid the need for pre-calculated irradiance textures and to simplify the user experience.<br />This is only enabled when a skybox is in use (not the fixed gradient) and can be disabled if desired.

<img src="images/entries/80ed241c2adbea51749cc1d0d5d892ef17f7f6d6.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support 3D model instancing
Instancing support has been added for 3d symbols.<br />This introduces a new library, tinyobjloader: https://github.com/tinyobjloader/tinyobjloader<br />qgsobj3dutils (similar to qgsgltf3dutils) is created, which loads OBJ data into geometry, reading and creating textured material, if it exists.<br />Other changes:
- PhongTexturedMaterial now supports instancing by implementing setInstancingEnabled() like phong and gooch.
- HighlightMaterial has been refactored to remove technique from the constructor call, and it also implements setInstacingEnabled() with flags. This also fixes a bug where previously 3d models wouldn't be highlighted in 3d view when selected in 2d.

"And if you gaze long into an abyss, the abyss also gazes into you".

<img src="images/entries/71e571c0902c1d2a576fe09198e69dc0cb7d479f.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Allow control over 3d map color grading effects
New settings are exposed for tone mapping, exposure adjustment, and gamma for 3D scenes.<br />A new "Color Grading" section the in 3d map "Effects" tab allows users to control these options. This allows users to modify a scene to render in a manner that makes colors more dramatic and provides higher contrast, or use bloom effects that can make very bright emitted light display as overexposed light in a nighttime scene.

<img src="images/entries/460ceb890c6261ddc51ce3659dde777121d649e5.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Optional light bloom effects
A new physically-based light bloom effect has been added, which gives bright portions of the 3d map a realistic bloom. This helps those areas to actually look like they emit light, as opposed to just having bright colors, and can help make 3d scenes look much more dramatic.

<img src="images/entries/0c981146a38a83d08ffff1f8c49193662e5cf725.png" class="img-responsive img-rounded" />

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add multisample anti aliasing (MSAA)
A new global 3D setting is provided that toggles the use of multisample anti-aliasing in 3D maps.

<img src="images/entries/ca69a2e049f207e2a0a57f5c5d57b3420207605c.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Add gradient background to 3D scene
QGIS now supports configurable gradients as background effects in 3D map views, providing users an effective custom skybox effect without textures.

<img src="images/entries/139a726cacbde4fdffaee78e66c974efbef509c3.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: 3D Tiles: add instancing support
Support has been added for instanced meshes in 3D Tiles, allowing users to efficiently display repeated 3D objects like trees or streetlights at varying positions, rotations, and scales. This implementation abstracts away the complex structural differences between 3D Tiles 1.0 and 1.1 to provide seamless rendering.
- Supported in both 2D and 3D map views.
- 3D views utilize highly efficient GPU instanced rendering.
- Supports 3D Tiles 1.0 using the i3dm format.
- Supports 3D Tiles 1.1 via glTF GPU instancing.
- Automatically corrects tile rotations for projected coordinate systems.
- Quantized positions and oct-encoded rotations remain unsupported.
- Feature IDs are not read in this implementation.

<img src="images/entries/adb08002b421eee278c571fd52325e7e93251b69.png" class="img-responsive img-rounded" />

This feature was funded by Natural Resources Canada

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### Feature: Add implicit tiling for 3D Tiles
Support has been added for implicit tiles as specified in the 3D Tiles 1.1 standard. This feature improves the loading and parsing efficiency of massive 3D datasets by utilizing structured subdivision schemes.<br />Logic runs via a new `QgsCesiumImplicitTiling` core class, and the quadtree subdivision scheme is currently supported (with octree support possible in a future update).

<img src="images/entries/3031b5c8facbd4e11ddd450b7314d92f9684c083.png" class="img-responsive img-rounded" />

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### Feature: Add camera controls dialog to control the 3D camera in map coordinates
A new dialog is provided to control the camera looking at XYZ in 3D map CRS coordinates, as well as setting pitch and heading angles and distance from the center point.<br />The dialog gets a `Live update` button that mimics the behavior of the Layer Styling panel. When set, user-changed settings are automatically reflected in the 3D map.<br />This does not affect the values updating from the 3D map. When a user moves the camera, the values are updated in real time, regardless of the `Live update` checkbox.

<img src="images/entries/1f896ef8c6f67e8a925e31712a4c543525d8987c.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Add support for 3D composite tiles ("cmpt")
QGIS now includes support for 3D Tiles 1.0 spec [Composite Tiles](https://github.com/CesiumGS/3d-tiles/blob/main/specification/TileFormats/Composite/README.adoc#tileformats-composite-composite), which combine multiple tiles (e.g., b3dm or i3dm) into a single file. This support is included for both 2D and 3D rendering.

<img src="images/entries/7196a54d0d5835b1cefa9efd8b4143c67130d5ab.png" class="img-responsive img-rounded" />

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### Feature: Improve 3D map view "Invert vertical axis" setting.
The Y inversion setting for 3D views has been refactored into a QFlag-based configuration, assigning an independent bit for each navigation scenario (walk mode dragging, walk mode mouse captured, and terrain mode).
- Settings are globally editable via a checkbox-based combobox.
- The C++ interface for inverted Y preferences is updated.
- The Python interface remains compatible via duck-typing.

<img src="images/entries/9ae04d9318d5c9662a84821de7c113ed1f48eb66.png" class="img-responsive img-rounded" />

This feature was developed by [David Koňařík](https://github.com/dvdkon)
### Feature: 3d export stl
QGIS now supports exporting a 3D scene in the [STL](https://en.wikipedia.org/wiki/STL_(file_format)) format, in addition to the existing `OBJ` export functionality. The `STL` format is much simpler than the `OBJ` and does not handle textures.

<img src="images/entries/e0e80d41fe495959ba786ad4261a947b766ac321.png" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## Point Clouds
### Feature: Add overview-length optional parameter to build vpc algorithm
A new `--overview-length` optional parameter has been added to the build VPC algorithm

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add reading support for multi-overview VPC files
Instead of parsing overview assets by their "overview" id, they are now parsed based on their "overview" role.<br />VPC files may contain multiple overviews per asset with arbitrary ids. All assets with the "overview" role are now considered as overviews, loaded and rendered when zoomed out.<br />`QgsPointCloudLayer` and `QgsVirtualPointCloudProvider` now have an `overviews()` method returning a list of all overviews, instead of a single one.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add support for a vpc-in-zip (.vpz) virtual point cloud format
Virtual Point Cloud (VPC) files can become quite large, and the ASCII-based JSON format does not really help in keeping the size down.<br />Leveraging the new support for QGIS to read remote `.vpc` files, the need for a smaller file size is more apparent, and support for the `.vpz` format constructed from a zipped `.vpc` has been added (similar to the `.qgz` QGIS project files providing a zipped `.qgs`).

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add per layer elevation shading
QGIS now supports per-layer elevation shading specifically for point cloud layers. This feature provides finer visual control, avoiding the blending and rendering artifacts that can occur when global elevation shading is applied across the entire map scene.
- Controlled via extended GUI in 2D symbology.
- Bypasses global elevation shading artifacts entirely.
- Prevents unwanted blending of distinct map elements.

<img src="images/entries/41a69a819d5d1446c2bcf2ddfcc4319bdb3b9f39.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Support arithmetic operators on color objects in expressions
QGIS now supports modifying color objects on Point Cloud data directly within expressions, using basic arithmetic operations. This simplifies dynamic color manipulation by automatically splitting the color into its base components and applying the mathematical operation to each channel, eliminating the need for complex component extraction formulas.
- Arithmetic operations apply directly to underlying RGBA channels.
- Multiplication works with the color on either side.
- Other operations require the color on the left.
- This feature avoids complex color component extraction formulas.
- Dynamic shading based on attributes is greatly simplified.

For Example:

`@point_color * scale_linear( @NumberOfReturns, 0, 8, 0.5, 1 )`

<img src="images/entries/d215e96ce1bf086ec558dbf3587894a22cc75af1.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Modify renderer color by expression
An additional modifier has been added to the point cloud renderer that makes it possible to use expressions to for adjusting colors.<br />All point cloud attributes can be used in the expression, as well as the base color of the renderer. Users can combine the base color value with another attribute of the point, such as intensity, to produce a better result for point classification and styling.<br />For example:<br />`@point_color * (@intensity / 65535)`

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
## Print Layouts
### Feature: Add new layout chart item functionality to derive plot data and styling from the source vector layer renderer
New settings have been added to the layout chart items:
- a 'generate categories from the layer symbology' toggle to have the plot series' X axis match categories from the source vector layer's renderer
- an 'apply layer symbology colors' toggle to have the rendered charts take on the colors of the symbol attached to the vector layer's renderer

The user can either rely on a blank series to *count* the number of matching features, or can rely on a custom Y expression (a simple field or a full-fledged expression) to come up with a customized sum (say length of lines, or an attribute referring to a value that can be summed, etc.)

<img src="images/entries/ba82a958973bddc5c128c2b24c7cd249a81d737c.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add new option to clip a picture item by a shape-based item
QGIS now provides the ability to clip a layout picture item by a shape-typed item.<br />This provides a fantastic way to frame cool shapes and mask elements with images (whether dynamically driven by an atlas feature attribute or a static image source).<br />The clipping is enabled and configured inside a new section of the picture item properties panel.

<img src="images/entries/08cbd88117433df3beb02050b1e690886b7ee27b.png" class="img-responsive img-rounded" />

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Geospatial PDF layer management enhancement
New options have been added to allow Geospatial PDF Exports to follow the QGIS layer tree configuration (groups, order, names, visibility, group layers). This allows users to preserve the layer structure, including nested groups, when exporting to a Geospatial PDF. This functionality is supported in print layouts, but not in standard map rendering tasks.
- The feature requires a map without locked layers.
- Both visible and invisible project layers are exported.
- PDFs render custom orders while keeping standard tree structures.
- Feature attributes are exported for all layers or none.
- Group layers are supported as single map layers.
- Matching PDF groups handle layout item visibility directly.
- Unmatched PDF groups appear at the tree bottom.
- Mutually exclusive groups are currently not supported.

<img src="images/entries/c4c92f09dc1381fac13768b1b52a192c9ed64eb8.png" class="img-responsive img-rounded" />

This feature was funded by the city of Bern

This feature was developed by [Germap](https://github.com/gacarrillor)
## Expressions
### Feature: Add scale_cubic_bezier expression function, handle bezier-cubic interpolation when converting MapBox styles
Complements the existing scale_linear, scale_exponential functions and adds a new bezier-cubic based interpolation method. This is then used when converting MapBox styles using the "cubic-bezier" interpolation type.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add concat_ws expression function
Concatenate all but the first arguments with separators. The first parameter is used as a separator.<br />NULL arguments are ignored.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Data Management
### Feature: Adding "Field Calculator" menu item to the attribute table header
A new "Field Calculator" menu item is provided in the context menu of column headers in a vector layer's attribute table.<br />The Field Calculator window will open with "Update existing field" checkbox automatically checked and the corresponding field already selected in the combo box.<br />The action is only enabled on editable fields.

<img src="images/entries/8ade61ae18cd9ec8014958f35d175ed4e5d0ed4f.png" class="img-responsive img-rounded" />

This feature was developed by [Patrice Pineault](https://github.com/TurboGraphxBeige)
## Επεξεργασία
### Feature: Dynamically show child step feature counts as model progresses
As the model is run through the designer dialog, QGIS will now show an updated count of features flowing through the model links. To achieve this, a new flexible "badge" item that is attached to arrows was introduced.<br />Note:
- We now also show non-feature count outputs in the badges for arrows, so, e.g., the value of numeric outputs attached to another algorithm will be shown. (To avoid cluttered UI, strings are truncated.)
- Badges now inherit the midpoint color of their associated arrow lines.
- For performance reasons, the feature count updates are limited to only every 100 features.
- Since not all algorithms report dynamic feature count progress (e.g., third-party plugin-based ones won't, at least until the plugin author utilises the upgraded API for this), QGIS will always update the feature counts with their exact final counts when the whole model finishes executing. For those models, the user will see the arrow's count updated in one go at the end of the model, not as that child executes.

<img src="images/entries/e78e514a83f210185705a81bc6e1a8311bc025c0.png" class="img-responsive img-rounded" />

This feature was funded by City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add an area threshold parameter
The check holes processing tool now includes a threshold size which allows users to filter the returned results. If the hole area is higher than the provided threshold, then the hole is not considered an error.

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### Feature: Add support for the SFCGAL extend to edges parameter in medial axis algorithm
With SFCGAL 2.3, the approximate media axis algorithm has a new `extendToEdges` parameter. If this parameter is activated, the medial axis endpoints are extended to the input polygon boundary. The attached media illustrates the difference between running the medial axis algorithm with this option set to false (red) and true (green), respectively.

<img src="images/entries/d1cf8c4c5dd1ef1d172745817db02a6e2628191e.png" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main

This feature was developed by [Jean Felder](https://github.com/ptitjano)
### Feature: Add processing in user defined menu or toolbar
Users can now add a processing algorithm action to a user-defined menu or toolbar. When triggered, those actions will open a dialog to parametrize and execute the associated processing algorithm.

<img src="images/entries/5ae9ce29dd7d2e8a7b094e3f7c129171af8a6d8f" class="img-responsive img-rounded" />

This feature was funded by Stadt Frankfurt am Main and Oslandia

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Feature: Random subset algorithms ported to C++
The Processing algorithms Random extract within subsets and Random selection within subsets have been ported from Python to C++, providing enhanced performance.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Application and Project Options
### Feature: Topocentric projection
Topocentric CRS support has been added to QGIS, with a new widget provided for setting the point of origin of the projection, which is enabled when users explicitly select a Topocentric CRS option from the CRS selection menu.

<img src="images/entries/405bc086bd84189e5113544155ac4ef7d85ed836.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
## Sensors
### Feature: Add support for SensorThings 2.0, including Sensing, Sampling and Relations extensions
QGIS now includes support for layers utilising SensorThings 2.0 specifications, including the new Sensing, Sampling and Relations extensions.<br />This also exposes these choices for SensorThings 2.0-enabled services. The service version and extensions are determined dynamically when connecting to a service via the browser or data source manager.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Profile Plots
### Feature: Display elevation profile curve in 3D
QGIS now provides a "Show Profile in 3D Views" option in the profile plot settings menu, which enables the display of the elevation profile curve in 3D.<br />The curve is retrieved from the elevation profile, and Z values are set from the calculated min and max Z values of the data that fit within the curve.<br />Polygon and line rubberbands follow the cursor to display over what position in the elevation profile the user is currently hovering over.

<img src="images/entries/51b9332232c56ecf122b5d6205744c01a2371e42.png" class="img-responsive img-rounded" />

This feature was developed by [Dominik Cindric](https://github.com/ViperMiniQ)
## Εξερεύνηση
### Feature: Rework how ESRI REST services are exposed in the browser
Changes have been made to help de-clutter ESRI REST service content in the browser:
- The duplicate items for the same service exposed as both mapserver (raster) and featureserver (vector) are now hidden. Instead, only show the feature server item, and move the ability to load as a raster to the right-click context menu on the item. This mimics how ArcPro exposes these services, with the exception that it ONLY allows loading them as vectors. There's no capability to load as a raster when the service exposes the query capability.
- We no longer show the "All layers" pseudo layer for mapserver items. Instead, this functionality was moved to the right-click context menu for the map service item. This avoids cluttering up the service contents in the browser with rarely used items that don't correspond to the actual contents of the service.

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Data Providers
### Feature: Greatly speed up the FeatureServer provider for map viewing
QGIS has a significantly more performant refactored approach to fetching data using the FeatureServer Provider, which trims down the number of requests required to fetch a subset of the features within a given map extent.<br />Note that the actual TOTAL number of requests to get EVERY feature from the service doesn't change, so, for example, opening the attribute table would result in the same total number of requests.

<img src="images/entries/e3ea1f5568a403cb6c293d963c0b04351df8ea21.png" class="img-responsive img-rounded" />

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Enable parallel provider load for AFS, AMS providers, and some related fixes
QGIS has enabled parallel provider loading for the ArcGIS FeatureServer/MapServer providers, giving much faster project load times when a project contains multiple FeatureServer/MapServer layers.

This feature was funded by République et canton de Genève

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support STAC assets from other cloud optimized data types and blob stores
QGIS has added support for STAC assets from other cloud object-store providers, including Azure and Google.<br />This additionally extends support to other cloud-optimized data types beyond GeoTiff, such as. JPEG2000, TileDB, Point Clouds, and others provided they are published with an appropriate `cloud-optimized` labelled mimetype or a supported asset type declaration.

This feature was developed by [Norman Barker](https://github.com/normanb)
## QGIS Εξυπηρετητής
### Feature: Add support for HIGHLIGHT_LABELFRAME options WMS params
New parameters for WMS services allow for the configuration of frame style properties on labels, including:
- `HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINECOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINEWIDTH`
- `HIGHLIGHT_LABELFRAMESIZE`

For Example:

`&MAP0:HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR=%23FF0000`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINECOLOR=%230000FF`<br />`&MAP0:HIGHLIGHT_LABELFRAMESIZE=5`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINEWIDTH=2`

<img src="images/entries/e2ce00c7b18b3fbb012ee8e08e0def43db4959c5.png" class="img-responsive img-rounded" />

This feature was developed by [Sandro Mani](https://github.com/manisandro)
### Feature: FlatGeobuf OAPIF export plus various fixes
The FlatGeobuf export format has been added to the QGIS Server OAPIF service, implemented in line with [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md)

This feature was funded by [QGIS user group Germany (QGIS Anwendergruppe Deutschland e.V.)](https://www.qgis.de/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Programmability
### Feature: Expose concave hull of polygons functionality
QGIS now supports the Concave Hull of Polygons algorithm from GEOS, which has been exposed in PyQGIS.
1. Allows polygon (and line) feature input for the Concave Hull by Feature algorithm. Previously, a user would have to first extract vertices from the polygon to calculate the concave hull from the points, but that approach ignores the interior of the polygon.
2. Adds a dedicated "Fill gaps between polygons" algorithm:

Unlike the standard Concave Hull algorithm, a Concave Hull of Polygons is a (possibly) non-convex polygon containing all the input polygons. The computed hull fills the gaps between the polygons without intersecting their interiors. It strictly follows the outer boundaries of the input polygons, allowing you to fill gaps between them without distorting their original shapes. It is particularly useful for cases such as generalizing groups of building outlines, creating 'district' polygons around blocks, or removing gaps and joining disjoint sets of polygons.<br />See https://lin-ear-th-inking.blogspot.com/2022/05/concave-hulls-of-polygons.html?m=1 for more details

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Notable Fixes
### Feature: Bug fixes by Even Rouault (Spatialys)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| .ASC missing from Raster Extraction | [\#66319](https://github.com/qgis/QGIS/issues/66319) | [PR \#66368](https://github.com/qgis/QGIS/pull/66368) | N/A |
| \[OAPIF\] Zooming triggers download of already loaded data | [\#66358](https://github.com/qgis/QGIS/issues/66358) | Not a bug |  |
| Gdb format in QGIS will show also .gdbtable .gdbtablex not only as .gdb | [\#66279](https://github.com/qgis/QGIS/issues/66279) | Not a bug / not desirable |  |
| Expose AZURE_STORAGE_SAS_TOKEN configuration option in Browser Cloud Storage Connection | [\#66274](https://github.com/qgis/QGIS/issues/66274) | [PR \#14731](https://github.com/OSGeo/gdal/pull/14731) | N/A |
| Filtering WFS causes total failure to display layer | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) |
| \[OAPIF\]\[server\] Paging not working with format FlatGeobuf from QGIS Server | [\#66365](https://github.com/qgis/QGIS/issues/66365) | [PR \#66399](https://github.com/qgis/QGIS/pull/66399) | N/A |
| Gml to Gml- Conversion succeeded, input and output are not the same in QGIS | [\#66413](https://github.com/qgis/QGIS/issues/66413) | Not a bug |  |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | [PR \#66510](https://github.com/qgis/QGIS/pull/66510) | [PR \#66539](https://github.com/qgis/QGIS/pull/66539) |
| Raster attribute table: convert empty DateTime as string coming from GDAL to NULL value | [\#66544](https://github.com/qgis/QGIS/issues/66544) | [PR \#66547](https://github.com/qgis/QGIS/pull/66547) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/en/home/)
### Feature: Bug fixes by Denis Rouzaud (OPENGIS.ch)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsSettings + QGIS4.ini + XYZ Tile provider = crash | [\#66424](https://github.com/qgis/QGIS/issues/66424) | [PR \#66450](https://github.com/qgis/QGIS/pull/66450) | N/A |
| Cannot load VT layer from style only from the dialog (works in browser) | not reported | [PR \#66500](https://github.com/qgis/QGIS/pull/66500) | TODO |
| "fix" every entry in relation reference widget is shown in italic | not reported | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch)](http://opengis.ch/)
### Feature: Bug fixes by Alessandro Pasotti (QCooperative)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[OAPIF\] QGIS Server OGC API is detected as WFS 1.1 | [\#66362](https://github.com/qgis/QGIS/issues/66362) | [PR \#66369](https://github.com/qgis/QGIS/pull/66369) | N/A |
| \[OAPIF\] Changing feature format has no effect | [\#66359](https://github.com/qgis/QGIS/issues/66359) | [PR \#66386](https://github.com/qgis/QGIS/pull/66386) | N/A |
| represent_value not working | [\#66339](https://github.com/qgis/QGIS/issues/66339) | [PR \#66392](https://github.com/qgis/QGIS/pull/66392) | [PR \#66436](https://github.com/qgis/QGIS/pull/66436) |
| Remove &key=pk from memory layers tests | [\#66350](https://github.com/qgis/QGIS/issues/66350) | [PR \#66397](https://github.com/qgis/QGIS/pull/66397) | N/A |
| \[server\] Fix network cache settings read from environment | [\#59613](https://github.com/qgis/QGIS/issues/59613) | [PR \#66425](https://github.com/qgis/QGIS/pull/66425) | N/A |
| \[postgres\] Fix json/b bytea add feature in transaction group | [\#65323](https://github.com/qgis/QGIS/issues/65323) | [PR \#66478](https://github.com/qgis/QGIS/pull/66478) | N/A |
| Unable to load style from datasource database for non geometry layers. | [\#66341](https://github.com/qgis/QGIS/issues/66341) | [PR \#66486](https://github.com/qgis/QGIS/pull/66486) | N/A |
| \[expressions\] Fix IN operator nodes() | [\#66313](https://github.com/qgis/QGIS/issues/66313) | [PR \#66485](https://github.com/qgis/QGIS/pull/66485) | [PR \#66499](https://github.com/qgis/QGIS/pull/66499) |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | Cannot reproduce |  |
| Field calculator allowed string \* float operation and program crashed | [\#66507](https://github.com/qgis/QGIS/issues/66507) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/A |
| Calculating integer field by "id"=@row_number crashed QGIS on save action | [\#66268](https://github.com/qgis/QGIS/issues/66268) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/A |
| Crash when attempting to load OpenHistoricalMap vector tiles | [\#66466](https://github.com/qgis/QGIS/issues/66466) | [PR \#66533](https://github.com/qgis/QGIS/pull/66533) | N/A |
| Data-defined override expression on a field is not evaluated until any field in the form is edited | [\#66504](https://github.com/qgis/QGIS/issues/66504) | Cannot reproduce |  |
| Export to PostgreSQL (Available Connection) drops source table | [\#66228](https://github.com/qgis/QGIS/issues/66228) | [PR \#66536](https://github.com/qgis/QGIS/pull/66536) | [PR \#66570](https://github.com/qgis/QGIS/pull/66570) |
| Spatialite data types are not recognized correctly when creating query layers with SQL | [\#66329](https://github.com/qgis/QGIS/issues/66329) | [PR \#66538](https://github.com/qgis/QGIS/pull/66538) | N/A |
| Edit layer properties of an invalid layer (broken source) is not working | [\#66324](https://github.com/qgis/QGIS/issues/66324) | [PR \#66607](https://github.com/qgis/QGIS/pull/66607) | Not recommended |
| Qgis have problem to render GeometryCollection for Gml, other viewer like mygeodata website render ok | [\#66225](https://github.com/qgis/QGIS/issues/66225) | Διπλότυπο |  |
| 3.44.7-Solothurn Crashes on New Shapefile | [\#66220](https://github.com/qgis/QGIS/issues/66220) | [PR \#66609](https://github.com/qgis/QGIS/pull/66609) | [PR \#66648](https://github.com/qgis/QGIS/pull/66648) |
| Add inja escape() function to HTML escape values | [GHSA-cr49-pm9v-m788](https://github.com/qgis/QGIS/security/advisories/GHSA-cr49-pm9v-m788) | [PR \#66616](https://github.com/qgis/QGIS/pull/66616) | [PR \#66670](https://github.com/qgis/QGIS/pull/66670) |
| Regression with decimal values and negative number in color gradient in the layer style panel | [\#65566](https://github.com/qgis/QGIS/issues/65566) | [PR \#66619](https://github.com/qgis/QGIS/pull/66619) | [PR \#66671](https://github.com/qgis/QGIS/pull/66671) |
| QGIS Server: GetProjectSettings returns the error message "Layer(s) not valid" with two WMS layers | [\#65872](https://github.com/qgis/QGIS/issues/65872) | Cannot reproduce |  |
| raster histogram not working for raster with scale factor | [\#65920](https://github.com/qgis/QGIS/issues/65920) | [PR \#66640](https://github.com/qgis/QGIS/pull/66640) | TODO |
| Advanced Digitizing Floater is not wide enough to show whole value | [\#65171](https://github.com/qgis/QGIS/issues/65171) | [PR \#66663](https://github.com/qgis/QGIS/pull/66663) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Feature: Bug fixes by Julien Cabieces (Oslandia)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Custom Toolbar Position Loss | [\#65862](https://github.com/qgis/QGIS/issues/65862) | [PR \#66483](https://github.com/qgis/QGIS/pull/66483) | N/A |
| Export to PDF from layout changes colors | [\#42935](https://github.com/qgis/QGIS/issues/42935) | Not a bug (Was an Adobe issue IMHO) |  |
| Layout bleeding to edge outside map window | [\#49638](https://github.com/qgis/QGIS/issues/49638) | Fixed |  |
| Fix flaky test_gui_fileuploader | Unreported | [PR \#66543](https://github.com/qgis/QGIS/pull/66543) |  |
| Hidden actions from user defined toolbar are still visible. | Unreported | [PR \#66620](https://github.com/qgis/QGIS/pull/66620) |  |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [\#58303](https://github.com/qgis/QGIS/issues/58303) | [PR \#66621](https://github.com/qgis/QGIS/pull/66621) | TODO |
| Password is not removed when it's at the the end of uri | Unreported | [PR \#66625](https://github.com/qgis/QGIS/pull/66625) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Germán Carrillo (OPENGIS.ch)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Allow QGIS to access curves from OGC API provider | Unreported | [PR \#66452](https://github.com/qgis/QGIS/pull/66452) | N/A |
| Elevation profile - changing layer symbology crashes QGIS / Wrong rendering order of Elevation profile items after changing the color of a profile item / Elevation profile stops respecting layer order on layer properties change | [\#64952](https://github.com/qgis/QGIS/issues/64952), [\#62677](https://github.com/qgis/QGIS/issues/62677), [\#64806](https://github.com/qgis/QGIS/issues/64806) | [PR \#66360](https://github.com/qgis/QGIS/pull/66360) | N/A |
| QGIS crashes on registering a Custom Profile Source with 'Sync Layers to Project' active | [\#65056](https://github.com/qgis/QGIS/issues/65056) | [PR \#66455](https://github.com/qgis/QGIS/pull/66455) | N/A |
| QGIS hangs when opening raster calculator (Meu Qgis está travando ao tentar abrir a calculadora raster) | [\#66327](https://github.com/qgis/QGIS/issues/66327) | Cannot reproduce |  |
| Ensure consistency in MultiCurves: don't allow NurbsCurves | Unreported | [PR \#66676](https://github.com/qgis/QGIS/pull/66676) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by David Signer (OPENGIS.ch)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix field displayString on primitive JSON values | Unreported | [PR \#66575](https://github.com/qgis/QGIS/pull/66575) | N/A |
| Fix bad behavior on widget detection of JSON fields | [\#62377](https://github.com/qgis/QGIS/issues/62377) | [PR \#66494](https://github.com/qgis/QGIS/pull/66494) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [David Signer (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by Stefanos Natsis (Lutra Consulting)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Windows QGIS 4 installs plugin with ACL that do not include SYSTEM or Administrators | [\#66515](https://github.com/qgis/QGIS/issues/66515) | [PR \#66576](https://github.com/qgis/QGIS/pull/66576) | N/A |
| Crash when clicking on an unavailable layer in Layers panel | [\#65913](https://github.com/qgis/QGIS/issues/65913) | [PR \#66578](https://github.com/qgis/QGIS/pull/66578) | TODO |
| QGIS server OGC API: Limits and offset parameters ignored when plugin changing parameters | [\#65858](https://github.com/qgis/QGIS/issues/65858) | Fixed | [PR \#66480](https://github.com/qgis/QGIS/pull/66480) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Feature: Bug fixes by Loïc Bartoletti (Oslandia)
| Bug Title | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Unbreak QGIS with GDAL \>= 3.13 | [commit ffdb8e3](https://github.com/qgis/QGIS/commit/ffdb8e3b27035478c533f37087505e749cc15b9b) | [PR \#66615](https://github.com/qgis/QGIS/pull/66615) | N/A |
| concat() returns NULL when all arguments are NULL: it should return an empty string | [\#65808](https://github.com/qgis/QGIS/issues/65808) | [PR \#66618](https://github.com/qgis/QGIS/pull/66618) | TODO |
| Remove all the parts in a geometry creates an empty geometry instead of NULL | [\#65453](https://github.com/qgis/QGIS/issues/65453) | WIP | TODO / Not recommended ? |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)

{{<content-end >}}
