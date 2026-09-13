---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Data lansării: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Mulțumiri**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Sponsorii versiunii QGIS 3.2
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## Generalități
### Feature: New zipped project file format .qgz is now the default format
QGZ was added as an optional format in 3.0. Having this format as the default format will ease a lot the path to go to a container able to embed resources like SVG, offline data in GPKG, color ramps, plugins or scripts.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Feature: Filtering for field values in Query Builder
When creating a new expression filter in query builder, you can now filter the field values preview panel.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Salvatore Larosa](https://github.com/slarosa)
### Feature: FULL screen Map via Ctrl-Shift-Tab
Besides Ctrl-Tab you can now do Ctrl-Shift-Tab, which will show you the Map and ONLY the Map, no more toolbars or buttons (or even without Window Title, in combination with F11). Great for Full Screen Map projection via Beamer or on Big Screens. You can still zoom and pan! (Based on work of Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Richard Duivenvoorde
## Instrumente De Cartografiere
### Feature: Simplify map tool can now also smooth features
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Identify Tool with extra options
With the new improvements, user can now use similar tools to the Selection to identify multiple features.

Această facilitate a fost finanțată de Leicestershire County Council and East Hampshire District Council

Această funcționalitate a fost dezvoltată de [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Feature: Store also expanded/collapsed state of nodes in map Themes
Each map theme will also record which layers, groups and legend items are expanded, so when a map theme is selected, the expanded/collapsed states get applied in the layer tree.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
A new map view can be configured to automatically zoom to the current selection. Could be combined with different map themes as in this example.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Technology One](https://www.technologyonecorp.com/)

Această funcționalitate a fost dezvoltată de [Nathan Woodrow](https://nathanw.net/)
### Feature: Choice of simplification method for simplify map tool
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: add zoom to related feature in forms
A new button appears in the feature attribute sub form when one or more records are selected in a related table. The button zooms the map to these features if they have geometries.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Jürgen Fischer
### Feature: Cartesian areas/lengths/perimeters in identify results
In QGIS 3.2 we now show both ellipsoidal and cartesian areas, lengths and perimeters separately within the identify results panel. Seeing the two distinct measurements gives users a better understanding of potential issues in area or distance calculations caused by incorrect projection or ellipsoid choices.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Expresii
### Funcționalitate: Noi funcții pentru expresii
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Noi variabile:
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Această funcționalitate a fost dezvoltată de Mathieu Pellerin, Nyall Dawson
### Feature: More helpful expression builder
The expression builder now makes it easier to build expressions within QGIS!
- The builder now shows the description for data defined values, including the range of expected values from the expression
- Ctrl+clicking a function name in the current expression will automatically open the help for that function
- It now shows indicators for parts of expressions with errors
- It shows a complete list of error messages obtained from parsing the expression

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Technology One](https://www.technologyonecorp.com/)

Această funcționalitate a fost dezvoltată de [Nathan Woodrow](https://nathanw.net/)
## Interfața cu Utilizatorul
### Feature: Layers panel: indicators for filtered map layers
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

This adds a mini-framework for display of extra icons in layer tree views next to layer and group names. Tool tip text can be associated with indicators to give extra context for indicators. In addition, a signal gets emitted when user clicks indicators and custom actions can be defined. The idea is that indicators can be used in the future for a subtle reporting of various bits of information, for example:
- map layer with invalid geometries
- map layer with on-the-fly reprojection exceptions
- map layer has missing data source
- map layer with invalid CRS

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Allow customizing prefix of locator filters
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [QGIS User Group Elveția](https://qgis.ch)

Această funcționalitate a fost dezvoltată de [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Feature: Opening of vector and raster stored on HTTP(S), FTP, or cloud services
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Quick calculator in locator search bar
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Shortcuts for toggling panels
Ctrl+{no} shortcut

Această funcționalitate a fost finanțată de [Technology One](https://www.technologyonecorp.com/)

Această funcționalitate a fost dezvoltată de [Nathan Woodrow](https://nathanw.net/)
### Feature: Bookmark searching in locator
Allows search for spatial bookmarks. Double clicking a search result will zoom to the bookmark.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Această funcționalitate a fost dezvoltată de Klavs Pihlkjær
### Feature: Close and Revert Project actions
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Nathan Woodrow, Nyall Dawson
### Feature: Unsaved changes indicator in title bar
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Configurable map tips delay
Această funcționalitate a fost dezvoltată de jdugge
### Feature: Move layer or group to top of layer panel
Moves the selected layer(s) or group(s) to the top of the layer panel.

Această funcționalitate a fost dezvoltată de Mie Winstrup
### Feature: Copy statistics panel content to clipboard button
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Search Settings, Options, and Project Properties pages from locator
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Această funcționalitate a fost dezvoltată de Klavs Pihlkjær
### Feature: Indicators for embedded layers and groups
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Simbologie
### Feature: Nicer colors for new layers
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Randare
### Feature: Improved map Copyright decoration
- Expression support for the copyright text.
- Improved text formatting options, including shadows, outlines, backgrounds, etc.

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Main window scale bar font size and family can be customized
Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Custom SVG path and size for the north arrow decoration
Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
## Gestiunea Datelor
### Feature: Refresh a materialized view
From the browser, with a right click on a materialized view, you can now refresh it.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Etienne Trimaille](https://github.com/Gustry)
### Feature: Z and M support for offline editing
Offline editing now also supports layers with Z and M coordinates.

Această funcționalitate a fost finanțată de [Oester Messtechnik](https://messtechnik.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Feature: Metadata for QGIS projects
Continuing the metadata work begun in QGIS 3.0, 3.2 now supports metadata for QGIS projects. This allows for detailed metadata to be set in project properties, including abstracts, keywords, contact details, links, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formulare și Controale grafice
### Feature: Multi-column layout for multiselect value relation widget
The value relation widget with multi selection enabled now supports multiple columns. This allows better usage of horizontal screen space.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Grundbuch- und Vermessungsamt des Cantonul Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

Această funcționalitate a fost dezvoltată de [David Signer, OPENGIS.ch](https://opengis.ch)
### Feature: Allow using a URL for custom attribute forms (UI file)
The UI file will be downloaded on every session on the first usage. This makes it possible to easily distribute updated UI files to clients.

Această funcționalitate a fost finanțată de [SIRS](http://www.sirs-fr.com)

Această funcționalitate a fost dezvoltată de [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Feature: Drill-down (cascading) forms
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS Danish User Group, Bo Victor Thomsen și Lene Fischer, North River Geographic

Această funcționalitate a fost dezvoltată de [Alessandro Pasotti (North Road)](https://north-road.com)
## Legenda stratului
### Feature: Optional text on top of symbols for vector layers
This feature allows users to add extra information to the symbols in the legend.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Copy&Paste Group/Layers from a QGIS project to another.
Allowing to copy and paste groups or layers between projects and profiles.

Această funcționalitate a fost dezvoltată de [Salvatore Larosa](https://github.com/slarosa)
## Compozitorul de Hărți
### Feature: Data defined table source for attribute table items
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(All existing table attributes (column settings) are left intact, so setting a data defined table to a layer with different fields will result in empty columns in the table.)

Această funcționalitate a fost finanțată de [Kartoza/InaSAFE](http://kartoza.com/en/)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Project metadata embedded in layout exports
Saving a print layout to SVG, PDF or images will now embed any project metadata in the created file. Support for different metadata elements depends on the individual export format.

Această funcționalitate a fost finanțată de Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Better formatting for scalebar text
QGIS 3.2 allows the full range of text formatting options to be used within scalebar text, e.g. buffers, shadows, and background shapes.

Unreadable scale bar text is a thing of the past!

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Procesare
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Feature: Load script from template
New option to load Processing scripts from a custom template

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Feature: Feature filter algorithm for processing models
Add a new feature filter algorithm for the processing modeler. Allows filtering features of a source based on expressions and send matching features to different outputs as final products or different algorithm pipeline for further processing.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [QGIS User Group Elveția](https://qgis.ch)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Feature: Zonal histogram
This new algorithm appends fields representing counts of each unique value from a raster layer contained within zones defined as polygons.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Port Union, Difference and Intersection algorithms to C++
QGIS native geoprocessing algorithms have been ported from Python to C++. In addition to performance boost, several bugs have been resolved with this update.

Această funcționalitate a fost finanțată de [InaSAFE DFAT](https://www.dfat.gov.au/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
This new Processing algorithm projects points from an input point layer by a specified distance and bearing (azimuth). It supports dynamic parameters for the distance and bearing so that the distance and bearing can be taken from field values or expressions.

Această funcționalitate a fost finanțată de [Nyall Dawson (North Road)](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Dynamic parameter values for more algorithms
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

In 3.2 the following algorithms now support dynamic parameters:
- Ştergere goluri
- Remove Duplicate Vertices
- Simplificare
- Neted
- Snap to Grid
- Subdivizare
- Transectul
- Translație

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Multi-ring buffer (constant distance) algorithm
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Această funcționalitate a fost dezvoltată de Alex Bruy
### Feature: New \"segmentize\" algorithms
In QGIS 3.2 two new algorithms for segmentizing curved geometries have been added to Processing.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Option to create points on all polygon parts
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Rotate Features algorithm
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Import geotagged photos
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Optionally the scan can be recursive and you can create an optional table of photos which could not be read or which were missing geotags.

The algorithm automatically sets the output table to use an external resource widget to display the linked photos in the attribute form.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Swap x/y coordinate values algorithm
Acest algoritm înlocuiește valorile coordonatelor X și Y din geometria de intrare. Poate fi utilizată pentru a repara geometriile care au avut inversate, în mod accidental, valorile pentru latitudine și longitudine.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
This change allows users to optionally set a sort order to use when assigning values in the Add Incremental Field algorithm. Previously values were always added using the original feature order. With this change users can control the order in which features are assigned values.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Indicator for distance parameter units
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Additionally - if the unit is in degrees, a small warning icon is shown next to the parameter. The tooltip for this icon advises users to reproject data into a suitable projected local coordinate system.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Algorithm log can be saved/cleared/copied
In the algorithm execution dialog, new buttons have been added to allow users to save the current log (to text or HTML files), copy the log contents to the clipboard, and clear the log.

Această funcționalitate a fost finanțată de SMEC/SJ

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Wedge buffer algorithm
This new algorithm creates wedge shaped buffers from input points.

The azimuth parameter gives the angle (in degrees) for the middle of the wedge to point. The buffer width (in degrees) is specified by the width parameter. Note that the wedge will extend to half of the angular width either side of the azimuth direction. The outer radius of the buffer is specified via outer radius, and optionally an inner radius can also be specified.

The algorithm supports dynamic parameters for azimuth, width, and radius.

The native output from this algorithm is CurvePolygon geometries, but these may be automatically segmentized to Polygons depending on the output format.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Variable width buffers
New Processing algorithms have been added to create variable width buffers, including tapered buffers (with a specified start and end diameter) and variable width buffers from line string m values.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Reclassify raster algorithms
Two new native QGIS raster reclassification algorithms have been added to Processing. These are simple to use, yet fast and stable, and work for ANY raster layer type supported by QGIS!
- Reclassify by layer: reclassifies a raster using the ranges specified via min/max/value fields from a vector table
- Reclassify by table: reclassifies a raster using a fixed table entered by users in the algorithm dialog

Această funcționalitate a fost finanțată de SMEC/SJ

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Union algorithm with a single layer
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [InaSAFE DFAT](https://www.dfat.gov.au/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Opțiunile Aplicației și ale Proiectului
### Feature: Mandatory layers in project
Required layers are not allowed to be removed from the project. This adds extra safety to protect project users from removing layers they may think are not needed (e.g. used in joins, relations, expressions).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Saving and loading projects in PostgreSQL database
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

Această funcționalitate a fost finanțată de [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

Această funcționalitate a fost dezvoltată de [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Navigatorul
### Feature: Save/Load connections for XYZ Tiles
From the Browser panel, XYZ Tiles entries can be exported/imported to/from an XML file.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Salvatore Larosa](https://github.com/slarosa)
### Feature: Project home path can be manually set
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Project home paths can also be set to relative paths, in which case they will be relative to the project saved location.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de SMEC/SJ

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Furnizorii de Date
### Feature: Support for mesh layers
Initial work has been done to introduce mesh layers supporting display of data on structured or unstructured meshes (grids) in addition to raster and vector layers. This is still a work in progress, expected to be fully ready in QGIS 3.4. The work so far lead to creation of a new library MDAL for handling of different formats of mesh-based data and there are new APIs introduced under the hood, however the user interface is not implemented yet.

Pentru mai multe informații:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

și

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: Automatically set default style for layers for ArcGIS Feature Server layers
When layers from a Feature Server are loaded into QGIS 3.2, they will automatically have the same style applied as has been specified for that layer on the server, matching the appearance of the layer when it is loaded into ArcGIS.

Această funcționalitate a fost finanțată de SMEC/SJ

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Faster Oracle queries
Certain operations are greatly sped up for Oracle layers, e.g. case-insensitive value matches for features.

Această funcționalitate a fost finanțată de [North Road](https://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Restrict table list for a Oracle database connection to a preset schema
This change allows a schema to be set in the connection properties for an Oracle database connection. If set, only tables within that schema will be scanned and listed for the connection.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

Această funcționalitate a fost finanțată de [Open Spatial](http://www.openspatial.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Read only support for curved Oracle geometries
Previously these geometries were silently discarded.

Această funcționalitate a fost finanțată de [Open Spatial](http://www.openspatial.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](https://north-road.com)
## Plugin-urile
### Feature: Adding query history in DB Manager
In 3.2 it is possible to store SQL queries. The query history is available into the SQL Window tab of the DB Manager plugin.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Salvatore Larosa](https://github.com/slarosa)
### Feature: DB Manager SQL execution in background
Această funcționalitate a fost dezvoltată de Paul Blottiere
## Funcționalități 3D
### Feature: 3D Polygons: Optionally generate back faces
Sometimes datasets with 3D polygons do not have consistent ordering of vertices (clockwise vs. counter-clockwise) and that caused sub-optimal results in the 3D view: either some polygons (walls) seem to be missing if back-face culling is enabled - or some polygons are shaded incorrectly if back-face culling is disabled. With the new option **Add back faces** enabled, the tessellator will generate triangles in both directions (front and back) which greatly improves the rendering quality for such datasets.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

The image contains freely available Prague 3D buildings dataset.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
