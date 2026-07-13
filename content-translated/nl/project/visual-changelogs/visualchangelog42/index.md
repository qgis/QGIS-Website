---
HasBanner: false
draft: false
releaseDate: '2026-07-03'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 4.2
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 4.2{#changelog42 }
<img src="images/projects/b7fa0af07e61fe7036f463d15cbba685c11baae2.png" class="img-responsive img-rounded center-block" />

Datum uitgave: 03-07-2026

[QGIS](https://qgis.org) (<https://qgis.org>) is het populairste (open bron) desktop Geografisch InformatieSysteem (GIS) ter wereld. Het wordt gebruikt door mensen over de gehele wereld om ruimtelijke gegevens te bekijken, te bewerken, te analyseren en te delen. Het kan professioneel ogende cartografieproducten produceren en ondersteunt honderden indelingen voor ruimtelijke gegevens. QGIS is een lidproject van OSGEO, de Open Source Geospatial Foundation, die toegang tot ruimtelijke platforms democratiseert (<https://osgeo.org>).

We zijn blij om de nieuwe belangrijke uitgave van QGIS 4.2 aan te kondigen, die doorbouwt op de solide fundering van de update van de belangrijke versie 4.0 die de bron van QGIS overbracht naar het moderne framewerk van Qt6. Deze uitgave bundelt ook heel veel verbeteringen in de uitvoering en nieuw geïntroduceerde mogelijkheden, inclusief meerdere verbeteringen voor de mogelijkheden van 3D en de gereedschappen van Processing.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=5X1JKx7CXZY).

[![](https://img.youtube.com/vi/5X1JKx7CXZY/0.jpg)](https://www.youtube.com/watch?v=5X1JKx7CXZY)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten!

Als u tijd of geld wilt doneren of op een andere manier wilt bijdragen aan het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Belangrijke wijzigingen
### Mogelijkheid: Verplaatsen naar de locatie van opslag voor instellingen van QGIS4 met geautomatiseerde migratie vanuit QGIS3
Om corruptie in het configuratiebestand tussen wijzigingen die zijn gemaakt in zowel QGIS3 als in QGIS4 op hetzelfde systeem te voorkomen, worden de instellingen voor QGIS 4 nu volledig geïsoleerd in een afzonderlijke map.<br />**ONTHOUD: Dit heeft invloed op geautomatiseerde scripts voor installeren, profielbeheer en uitrollen in zakelijke omgevingen.**<br />Bij de eerste keer opstarten zal QGIS4 een kopie uitvoeren van de gegevens van het gebruikersprofiel vanuit het bestaande pad voor QGIS3 en de instellingen klonen naar een nieuw pad voor QGIS4. Geautomatiseerde uitrollen en scripts voor profielbeheer moeten worden bijgewerkt om te verwijzen naar die nieuwe locatie. Dat lost de problemen op van [\#61636](https://github.com/qgis/QGIS/issues/61636) en [\#60088](https://github.com/qgis/QGIS/issues/60088).<br />Onthoud goed:
- Dit is een EENMALIGE migratie
- De migratie behoudt de instellingen van het GELADEN GEBRUIKERSPROFIEL, zonder verlies
- Volgende wijzigingen in de profielen zullen niet worden gesynchroniseerd tussen QGIS3 en QGIS4

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Laden en opslaan van stijlen toegevoegd aan laagmenu
Dit voegt de opties **Stijl laden…** en **Stijl opslaan…** direct toe aan het laagmenu onder het submenu **Stijlen**. Dat zal gebruikers een snelle manier geven om stijl voor een laag te laden/op te slaan, zonder de noodzaak om een andere interface of menu te openen.

<img src="images/entries/3649f31a4a1358779fd933bddce5e20161257fd9.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Symbologie
### Mogelijkheid: Renderer Categorieën voor 3D-symbolen toegevoegd
Renderers Categorieën en Op regel-gebaseerd zijn nu beschikbaar voor QGIS 3D-symbologie.<br />Beide implementaties zijn soortgelijk aan de bestaande vectorrenderers voor 2D-stijlen, zodat gebruikers bekende besturingselementen hebben voor 3D-scenes, terwijl meerdere verbeteringen in de API zijn doorgevoerd om deze set krachtige functionaliteiten te ondersteunen.

<img src="images/entries/c5fb95c208d6bc03a05ac923f019475a50310cb6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Fysiek gebaseerd metaal met ondersteuning voor textuur toegevoegd
Een nieuw materiaaltype 3D voor het weergeven van op fysiek gebaseerd materiaal met volledige kaartondersteuning voor textuur is toegevoegd.<br />Texturen kunnen worden gespecificeerd voor:
- basiskleur
- metaalheid
- ruwheid
- ingesloten omgeving

<img src="images/entries/ee3d3005794174302de3f65232c8cace82357987.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Afstand verkleinen toegevoegd voor begin en eind voor gestreepte lijn- en markeringssymboollagen
Dit breidt de reeds bestaande mogelijkheden voor eenvoudige lijnen uit naar gestreepte lijnen- en markeringslijnsymboollagen.

<img src="images/entries/bb0088d635bc91e52e14fec777c191861410d687" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Data-bepaald beheer toegevoegd voor basis ruwheid metaal, emissiekleur
Een data-bepaald besturingselement voor de basis voor de ruwheid van metaal en de emissiekleur is toegevoegd. Dit sluit een van de weinige resterende gaten in de functionaliteit tussen de verouderde materialen Phong en het op fysiek gebaseerd materiaal.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Data-bepaald beheer toegevoegd voor Phong/ruwheid metaal textuurschaal, rotatie en verschuiving
Een data-bepaald besturingselement is toegevoegd voor beheer over de schaal van de textuur, rotatie en verschuiving voor 3D-polygonen, bij het gebruiken van ofwel de materialen van ruw metaal of Phong met textuur.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optionele effen emissiekleur toegevoegd voor metaal ruw materiaal
Een nieuwe, niet-standaardinstelling voor een effen emissiekleur is toegevoegd aan het metaal ruw materiaal, naast een draaiknop om ook de sterkte van de emissie te beheren. Praktisch stelt dit gebruikers in staat materialen te maken die niet worden beïnvloed door belichting van de scène.<br />De aangehechte afbeelding geeft een vergelijking weer tussen een donkere scènebelichting zonder emissie, gele emissie op 100% en gele emissie op 1000% om het het effect van deze functionaliteit te demonstreren.

<img src="images/entries/260c863c37dddb6f738615df50851b8eb06185bf.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor doorzichtbaarheid toegevoegd voor materialen ruw metaal
Op fysiek gebaseerde materialen voor renderen ondersteunen nu doorzichtbaarheid, wat hun mogelijkheden dichter bij de mogelijkheden voor het materiaal van Phong brengt.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Instellingen voor materiaal 3D toegevoegd aan stijldatabase
QGIS bevat nu ondersteuning voor het beheren van instellingen voor materiaal 3D in de stijldatabase (en het dialoogvenster Stijl beheren).<br />Gebruikers kunnen voorkeuzen van 3D-materialen maken en ze beheren naast andere stijlobjecten (bijv. toestaan van metadata, zoals taggen, favorieten, etc.).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Keuzemogelijkheid voor as omhoog/naar voren voor 3D-puntmodelsymbolen
In plaats van er altijd vanuit te gaan dat het modelbestand is gemaakt met een conventie voor de as van Z omhoog en Y naar voren, geef instellingen weer om gebruikers in staat te stellen om handmatig de assen naar voren en omhoog in te stellen. Dat maakt het gemakkelijker om willekeurige obj-bestanden, gedownload vanaf het internet, te gebruiken als 3D-puntsymbolen in QGIS. Eerdere workarounds vereisten het handmatig draaien van het symbool, maar dat verhinderde het opnieuw gebruiken van de waarden rotatie/schaal en data-bepaalde expressies die werden gebruikt door andere 3D-puntsymbolen.

<img src="images/entries/70b6d2509f1fb98c8a582a95c7abe3d58c22066a.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Extra items toegevoegd voor sjabloon van lijnsymboollaag
Gereedschappen worden nu verschaft om nieuwe markeringen/streepjes voor markerings-/gestreepte lijn-symboollaag te maken, te verplaatsen, te draaien en te verwijderen.<br />Deze nieuwe markeringen zullen dezelfde stijl delen als de originele markeringen, dezelfde geselecteerde of zichtbare status.<br />Dit is de implementatie van [QEP \#406](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/356).

<img src="images/entries/ab98e9fb9b4fd3111e4329ec44cf60c777761fd6" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia\*\*

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## 3D-objecten
### Mogelijkheid: Omgevingslicht maken vanauit skybox
Nieuwe effecten voor omgevingslicht zijn toegevoegd aan de op fysiek gebaseerde materialen als een kubus kaart-skybox aanwezig is. Omgevingslicht wordt dynamisch berekend vanuit de texturen van de skybox.<br />Deze effecten gebruiken de bolvormige harmonische schatting voor de straling om de noodzaak voor vooraf berekende texturen van straling te vermijden en om de gebruikerservaring te vereenvoudigen.<br />Dit is alleen ingeschakeld als een skybox wordt gebruikt (niet het vaste kleurverloop) en kan, indien gewenst, worden uitgeschakeld.

<img src="images/entries/80ed241c2adbea51749cc1d0d5d892ef17f7f6d6.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning instancing 3D-model
Ondersteuning voor instancing is toegevoegd voor 3D- symbolen.<br />Dit introduceert een nieuwe bibliotheek, tinyobjloader: https://github.com/tinyobjloader/tinyobjloader<br />qgsobj3dutils (soortgelijk aan qgsgltf3dutils) is gemaakt, die gegevens van OBJ laadt in geometrie, leest en maakt materiaal met textuur, als dat bestaat.<br />Andere wijzigingen:
- PhongTexturedMaterial ondersteunt nu instancing door het implementeren van setInstancingEnabled() zoals voor Phong en Gooch.
- HighlightMaterial is opnieuw bewerkt om techniek uit de aanroep voor het maken te verwijderen, en het implementeert setInstacingEnabled() met vlaggen. Dit repareert ook een probleem waar eerder 3D-modellen niet werden geaccentueerd in weergave 3D indien geselecteerd in 2D.

"En als je maar lang genoeg in een afgrond staart, staart de afgrond ook in jou".

<img src="images/entries/71e571c0902c1d2a576fe09198e69dc0cb7d479f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Toestaan van beheer over effecten voor graderen van 3D-kaartkleuren
Nieuwe instellingen worden weergegeven voor toonmappen, aanpassen van weergave en gamma voor 3D-scènes.<br />Een nieuw gedeelte "Kleurgradering" op de 3D-kaarttab "Effecten" stelt gebruikers in staat deze opties te beheren. Dit stelt gebruikers in staat om een scène aan te passen om te renderen op een manier die kleuren dramatischer maakt en verschaft hoger contrast, of gloeieffecten te gebruiken die heel helder uitgestraald licht weergeven als overbelicht licht in een nachtscène.

<img src="images/entries/460ceb890c6261ddc51ce3659dde777121d649e5.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optionele gloeieffecten voor licht
Een nieuw op fysiek gebaseerd gloeieffect voor licht is toegevoegd, wat heldere delen van de 3D-kaart een realistische gloed geven. Dat helpt om die gebieden er feitelijk uit te laten zien alsof ze licht uitstralen, tegengesteld aan het feit dat ze slechts heldere kleuren hebben, en kunnen helpen om 3D-scènes er veel dramatischer uit te laten zien.

<img src="images/entries/0c981146a38a83d08ffff1f8c49193662e5cf725.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Multisample anti-aliasing (MSAA) toegevoegd
Een nieuwe globale 3D-instelling wordt verschaft die schakelt met het gebruiken van multisample anti-aliasing in 3D-kaarten.

<img src="images/entries/ca69a2e049f207e2a0a57f5c5d57b3420207605c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Kleurverloop achtergrond toegevoegd aan 3D-scène
QGIS ondersteunt nu te configureren kleurverlopen als achtergrondeffecten in 3D-kaartweergaven, wat gebruikers een effectief aangepast skyboxeffect zonder texturen verschaft.

<img src="images/entries/139a726cacbde4fdffaee78e66c974efbef509c3.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
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

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Feature: Add implicit tiling for 3D Tiles
Support has been added for implicit tiles as specified in the 3D Tiles 1.1 standard. This feature improves the loading and parsing efficiency of massive 3D datasets by utilizing structured subdivision schemes.<br />Logic runs via a new `QgsCesiumImplicitTiling` core class, and the quadtree subdivision scheme is currently supported (with octree support possible in a future update).

<img src="images/entries/3031b5c8facbd4e11ddd450b7314d92f9684c083.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Feature: Add camera controls dialog to control the 3D camera in map coordinates
A new dialog is provided to control the camera looking at XYZ in 3D map CRS coordinates, as well as setting pitch and heading angles and distance from the center point.<br />The dialog gets a `Live update` button that mimics the behavior of the Layer Styling panel. When set, user-changed settings are automatically reflected in the 3D map.<br />This does not affect the values updating from the 3D map. When a user moves the camera, the values are updated in real time, regardless of the `Live update` checkbox.

<img src="images/entries/1f896ef8c6f67e8a925e31712a4c543525d8987c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Add support for 3D composite tiles ("cmpt")
QGIS now includes support for 3D Tiles 1.0 spec [Composite Tiles](https://github.com/CesiumGS/3d-tiles/blob/main/specification/TileFormats/Composite/README.adoc#tileformats-composite-composite), which combine multiple tiles (e.g., b3dm or i3dm) into a single file. This support is included for both 2D and 3D rendering.

<img src="images/entries/7196a54d0d5835b1cefa9efd8b4143c67130d5ab.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Feature: Improve 3D map view "Invert vertical axis" setting.
The Y inversion setting for 3D views has been refactored into a QFlag-based configuration, assigning an independent bit for each navigation scenario (walk mode dragging, walk mode mouse captured, and terrain mode).
- Settings are globally editable via a checkbox-based combobox.
- The C++ interface for inverted Y preferences is updated.
- The Python interface remains compatible via duck-typing.

<img src="images/entries/9ae04d9318d5c9662a84821de7c113ed1f48eb66.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [David Koňařík](https://github.com/dvdkon)
### Feature: 3d export stl
QGIS now supports exporting a 3D scene in the [STL](https://en.wikipedia.org/wiki/STL_(file_format)) format, in addition to the existing `OBJ` export functionality. The `STL` format is much simpler than the `OBJ` and does not handle textures.

<img src="images/entries/e0e80d41fe495959ba786ad4261a947b766ac321.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Puntenwolken
### Feature: Add overview-length optional parameter to build vpc algorithm
A new `--overview-length` optional parameter has been added to the build VPC algorithm

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add reading support for multi-overview VPC files
Instead of parsing overview assets by their "overview" id, they are now parsed based on their "overview" role.<br />VPC files may contain multiple overviews per asset with arbitrary ids. All assets with the "overview" role are now considered as overviews, loaded and rendered when zoomed out.<br />`QgsPointCloudLayer` and `QgsVirtualPointCloudProvider` now have an `overviews()` method returning a list of all overviews, instead of a single one.

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add support for a vpc-in-zip (.vpz) virtual point cloud format
Virtual Point Cloud (VPC) files can become quite large, and the ASCII-based JSON format does not really help in keeping the size down.<br />Leveraging the new support for QGIS to read remote `.vpc` files, the need for a smaller file size is more apparent, and support for the `.vpz` format constructed from a zipped `.vpc` has been added (similar to the `.qgz` QGIS project files providing a zipped `.qgs`).

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add per layer elevation shading
QGIS now supports per-layer elevation shading specifically for point cloud layers. This feature provides finer visual control, avoiding the blending and rendering artifacts that can occur when global elevation shading is applied across the entire map scene.
- Controlled via extended GUI in 2D symbology.
- Bypasses global elevation shading artifacts entirely.
- Prevents unwanted blending of distinct map elements.

<img src="images/entries/41a69a819d5d1446c2bcf2ddfcc4319bdb3b9f39.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
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

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Feature: Modify renderer color by expression
An additional modifier has been added to the point cloud renderer that makes it possible to use expressions to for adjusting colors.<br />All point cloud attributes can be used in the expression, as well as the base color of the renderer. Users can combine the base color value with another attribute of the point, such as intensity, to produce a better result for point classification and styling.<br />For example:<br />`@point_color * (@intensity / 65535)`

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Afdruklay-outs
### Feature: Add new layout chart item functionality to derive plot data and styling from the source vector layer renderer
New settings have been added to the layout chart items:
- a 'generate categories from the layer symbology' toggle to have the plot series' X axis match categories from the source vector layer's renderer
- an 'apply layer symbology colors' toggle to have the rendered charts take on the colors of the symbol attached to the vector layer's renderer

The user can either rely on a blank series to *count* the number of matching features, or can rely on a custom Y expression (a simple field or a full-fledged expression) to come up with a customized sum (say length of lines, or an attribute referring to a value that can be summed, etc.)

<img src="images/entries/ba82a958973bddc5c128c2b24c7cd249a81d737c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add new option to clip a picture item by a shape-based item
QGIS now provides the ability to clip a layout picture item by a shape-typed item.<br />This provides a fantastic way to frame cool shapes and mask elements with images (whether dynamically driven by an atlas feature attribute or a static image source).<br />The clipping is enabled and configured inside a new section of the picture item properties panel.

<img src="images/entries/08cbd88117433df3beb02050b1e690886b7ee27b.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
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

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
## Expressies
### Feature: Add scale_cubic_bezier expression function, handle bezier-cubic interpolation when converting MapBox styles
Complements the existing scale_linear, scale_exponential functions and adds a new bezier-cubic based interpolation method. This is then used when converting MapBox styles using the "cubic-bezier" interpolation type.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add concat_ws expression function
Concatenate all but the first arguments with separators. The first parameter is used as a separator.<br />NULL arguments are ignored.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensbeheer
### Feature: Adding "Field Calculator" menu item to the attribute table header
A new "Field Calculator" menu item is provided in the context menu of column headers in a vector layer's attribute table.<br />The Field Calculator window will open with "Update existing field" checkbox automatically checked and the corresponding field already selected in the combo box.<br />The action is only enabled on editable fields.

<img src="images/entries/8ade61ae18cd9ec8014958f35d175ed4e5d0ed4f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Patrice Pineault](https://github.com/TurboGraphxBeige)
## Processing
### Feature: Dynamically show child step feature counts as model progresses
As the model is run through the designer dialog, QGIS will now show an updated count of features flowing through the model links. To achieve this, a new flexible "badge" item that is attached to arrows was introduced.<br />Note:
- We now also show non-feature count outputs in the badges for arrows, so, e.g., the value of numeric outputs attached to another algorithm will be shown. (To avoid cluttered UI, strings are truncated.)
- Badges now inherit the midpoint color of their associated arrow lines.
- For performance reasons, the feature count updates are limited to only every 100 features.
- Since not all algorithms report dynamic feature count progress (e.g., third-party plugin-based ones won't, at least until the plugin author utilises the upgraded API for this), QGIS will always update the feature counts with their exact final counts when the whole model finishes executing. For those models, the user will see the arrow's count updated in one go at the end of the model, not as that child executes.

<img src="images/entries/e78e514a83f210185705a81bc6e1a8311bc025c0.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add an area threshold parameter
The check holes processing tool now includes a threshold size which allows users to filter the returned results. If the hole area is higher than the provided threshold, then the hole is not considered an error.

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
### Feature: Add support for the SFCGAL extend to edges parameter in medial axis algorithm
With SFCGAL 2.3, the approximate media axis algorithm has a new `extendToEdges` parameter. If this parameter is activated, the medial axis endpoints are extended to the input polygon boundary. The attached media illustrates the difference between running the medial axis algorithm with this option set to false (red) and true (green), respectively.

<img src="images/entries/d1cf8c4c5dd1ef1d172745817db02a6e2628191e.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Feature: Add processing in user defined menu or toolbar
Users can now add a processing algorithm action to a user-defined menu or toolbar. When triggered, those actions will open a dialog to parametrize and execute the associated processing algorithm.

<img src="images/entries/5ae9ce29dd7d2e8a7b094e3f7c129171af8a6d8f" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Feature: Random subset algorithms ported to C++
The Processing algorithms Random extract within subsets and Random selection within subsets have been ported from Python to C++, providing enhanced performance.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
## Opties voor toepassing en projecten
### Feature: Topocentric projection
Topocentric CRS support has been added to QGIS, with a new widget provided for setting the point of origin of the projection, which is enabled when users explicitly select a Topocentric CRS option from the CRS selection menu.

<img src="images/entries/405bc086bd84189e5113544155ac4ef7d85ed836.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Sensoren
### Feature: Add support for SensorThings 2.0, including Sensing, Sampling and Relations extensions
QGIS now includes support for layers utilising SensorThings 2.0 specifications, including the new Sensing, Sampling and Relations extensions.<br />This also exposes these choices for SensorThings 2.0-enabled services. The service version and extensions are determined dynamically when connecting to a service via the browser or data source manager.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Profiel plotten
### Feature: Display elevation profile curve in 3D
QGIS now provides a "Show Profile in 3D Views" option in the profile plot settings menu, which enables the display of the elevation profile curve in 3D.<br />The curve is retrieved from the elevation profile, and Z values are set from the calculated min and max Z values of the data that fit within the curve.<br />Polygon and line rubberbands follow the cursor to display over what position in the elevation profile the user is currently hovering over.

<img src="images/entries/51b9332232c56ecf122b5d6205744c01a2371e42.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Browser
### Feature: Rework how ESRI REST services are exposed in the browser
Changes have been made to help de-clutter ESRI REST service content in the browser:
- The duplicate items for the same service exposed as both mapserver (raster) and featureserver (vector) are now hidden. Instead, only show the feature server item, and move the ability to load as a raster to the right-click context menu on the item. This mimics how ArcPro exposes these services, with the exception that it ONLY allows loading them as vectors. There's no capability to load as a raster when the service exposes the query capability.
- We no longer show the "All layers" pseudo layer for mapserver items. Instead, this functionality was moved to the right-click context menu for the map service item. This avoids cluttering up the service contents in the browser with rarely used items that don't correspond to the actual contents of the service.

This feature was funded by République et canton de Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Feature: Greatly speed up the FeatureServer provider for map viewing
QGIS has a significantly more performant refactored approach to fetching data using the FeatureServer Provider, which trims down the number of requests required to fetch a subset of the features within a given map extent.<br />Note that the actual TOTAL number of requests to get EVERY feature from the service doesn't change, so, for example, opening the attribute table would result in the same total number of requests.

<img src="images/entries/e3ea1f5568a403cb6c293d963c0b04351df8ea21.png" class="img-responsive img-rounded" />

This feature was funded by République et canton de Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Enable parallel provider load for AFS, AMS providers, and some related fixes
QGIS has enabled parallel provider loading for the ArcGIS FeatureServer/MapServer providers, giving much faster project load times when a project contains multiple FeatureServer/MapServer layers.

This feature was funded by République et canton de Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support STAC assets from other cloud optimized data types and blob stores
QGIS has added support for STAC assets from other cloud object-store providers, including Azure and Google.<br />This additionally extends support to other cloud-optimized data types beyond GeoTiff, such as. JPEG2000, TileDB, Point Clouds, and others provided they are published with an appropriate `cloud-optimized` labelled mimetype or a supported asset type declaration.

This feature was developed by [Norman Barker](https://github.com/normanb)
## QGIS Server
### Feature: Add support for HIGHLIGHT_LABELFRAME options WMS params
New parameters for WMS services allow for the configuration of frame style properties on labels, including:
- `HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINECOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINEWIDTH`
- `HIGHLIGHT_LABELFRAMESIZE`

For Example:

`&MAP0:HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR=%23FF0000`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINECOLOR=%230000FF`<br />`&MAP0:HIGHLIGHT_LABELFRAMESIZE=5`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINEWIDTH=2`

<img src="images/entries/e2ce00c7b18b3fbb012ee8e08e0def43db4959c5.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Sandro Mani](https://github.com/manisandro)
### Feature: FlatGeobuf OAPIF export plus various fixes
The FlatGeobuf export format has been added to the QGIS Server OAPIF service, implemented in line with [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md)

This feature was funded by [QGIS user group Germany (QGIS Anwendergruppe Deutschland e.V.)](https://www.qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Programmeerbaarheid
### Feature: Expose concave hull of polygons functionality
QGIS now supports the Concave Hull of Polygons algorithm from GEOS, which has been exposed in PyQGIS.
1. Allows polygon (and line) feature input for the Concave Hull by Feature algorithm. Previously, a user would have to first extract vertices from the polygon to calculate the concave hull from the points, but that approach ignores the interior of the polygon.
2. Adds a dedicated "Fill gaps between polygons" algorithm:

Unlike the standard Concave Hull algorithm, a Concave Hull of Polygons is a (possibly) non-convex polygon containing all the input polygons. The computed hull fills the gaps between the polygons without intersecting their interiors. It strictly follows the outer boundaries of the input polygons, allowing you to fill gaps between them without distorting their original shapes. It is particularly useful for cases such as generalizing groups of building outlines, creating 'district' polygons around blocks, or removing gaps and joining disjoint sets of polygons.<br />See https://lin-ear-th-inking.blogspot.com/2022/05/concave-hulls-of-polygons.html?m=1 for more details

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| .ASC missing from Raster Extraction | [\#66319](https://github.com/qgis/QGIS/issues/66319) | [PR \#66368](https://github.com/qgis/QGIS/pull/66368) | N/B |
| \[OAPIF\] Zooming triggers download of already loaded data | [\#66358](https://github.com/qgis/QGIS/issues/66358) | Is geen probleem |  |
| Gdb format in QGIS will show also .gdbtable .gdbtablex not only as .gdb | [\#66279](https://github.com/qgis/QGIS/issues/66279) | Not a bug / not desirable |  |
| Expose AZURE_STORAGE_SAS_TOKEN configuration option in Browser Cloud Storage Connection | [\#66274](https://github.com/qgis/QGIS/issues/66274) | [PR \#14731](https://github.com/OSGeo/gdal/pull/14731) | N/B |
| Filtering WFS causes total failure to display layer | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) |
| \[OAPIF\]\[server\] Paging not working with format FlatGeobuf from QGIS Server | [\#66365](https://github.com/qgis/QGIS/issues/66365) | [PR \#66399](https://github.com/qgis/QGIS/pull/66399) | N/B |
| Gml to Gml- Conversion succeeded, input and output are not the same in QGIS | [\#66413](https://github.com/qgis/QGIS/issues/66413) | Is geen probleem |  |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | [PR \#66510](https://github.com/qgis/QGIS/pull/66510) | [PR \#66539](https://github.com/qgis/QGIS/pull/66539) |
| Raster attribute table: convert empty DateTime as string coming from GDAL to NULL value | [\#66544](https://github.com/qgis/QGIS/issues/66544) | [PR \#66547](https://github.com/qgis/QGIS/pull/66547) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/en/home/)
### Feature: Bug fixes by Denis Rouzaud (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsSettings + QGIS4.ini + XYZ Tile provider = crash | [\#66424](https://github.com/qgis/QGIS/issues/66424) | [PR \#66450](https://github.com/qgis/QGIS/pull/66450) | N/B |
| Cannot load VT layer from style only from the dialog (works in browser) | niet gerapporteerd | [PR \#66500](https://github.com/qgis/QGIS/pull/66500) | NOG TE DOEN |
| "fix" every entry in relation reference widget is shown in italic | niet gerapporteerd | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch)](http://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[OAPIF\] QGIS Server OGC API is detected as WFS 1.1 | [\#66362](https://github.com/qgis/QGIS/issues/66362) | [PR \#66369](https://github.com/qgis/QGIS/pull/66369) | N/B |
| \[OAPIF\] Changing feature format has no effect | [\#66359](https://github.com/qgis/QGIS/issues/66359) | [PR \#66386](https://github.com/qgis/QGIS/pull/66386) | N/B |
| represent_value not working | [\#66339](https://github.com/qgis/QGIS/issues/66339) | [PR \#66392](https://github.com/qgis/QGIS/pull/66392) | [PR \#66436](https://github.com/qgis/QGIS/pull/66436) |
| Remove &key=pk from memory layers tests | [\#66350](https://github.com/qgis/QGIS/issues/66350) | [PR \#66397](https://github.com/qgis/QGIS/pull/66397) | N/B |
| \[server\] Fix network cache settings read from environment | [\#59613](https://github.com/qgis/QGIS/issues/59613) | [PR \#66425](https://github.com/qgis/QGIS/pull/66425) | N/B |
| \[postgres\] Fix json/b bytea add feature in transaction group | [\#65323](https://github.com/qgis/QGIS/issues/65323) | [PR \#66478](https://github.com/qgis/QGIS/pull/66478) | N/B |
| Unable to load style from datasource database for non geometry layers. | [\#66341](https://github.com/qgis/QGIS/issues/66341) | [PR \#66486](https://github.com/qgis/QGIS/pull/66486) | N/B |
| \[expressions\] Fix IN operator nodes() | [\#66313](https://github.com/qgis/QGIS/issues/66313) | [PR \#66485](https://github.com/qgis/QGIS/pull/66485) | [PR \#66499](https://github.com/qgis/QGIS/pull/66499) |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | Kan niet worden gereproduceerd |  |
| Field calculator allowed string \* float operation and program crashed | [\#66507](https://github.com/qgis/QGIS/issues/66507) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/B |
| Calculating integer field by "id"=@row_number crashed QGIS on save action | [\#66268](https://github.com/qgis/QGIS/issues/66268) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/B |
| Crash when attempting to load OpenHistoricalMap vector tiles | [\#66466](https://github.com/qgis/QGIS/issues/66466) | [PR \#66533](https://github.com/qgis/QGIS/pull/66533) | N/B |
| Data-defined override expression on a field is not evaluated until any field in the form is edited | [\#66504](https://github.com/qgis/QGIS/issues/66504) | Kan niet worden gereproduceerd |  |
| Export to PostgreSQL (Available Connection) drops source table | [\#66228](https://github.com/qgis/QGIS/issues/66228) | [PR \#66536](https://github.com/qgis/QGIS/pull/66536) | [PR \#66570](https://github.com/qgis/QGIS/pull/66570) |
| Spatialite data types are not recognized correctly when creating query layers with SQL | [\#66329](https://github.com/qgis/QGIS/issues/66329) | [PR \#66538](https://github.com/qgis/QGIS/pull/66538) | N/B |
| Edit layer properties of an invalid layer (broken source) is not working | [\#66324](https://github.com/qgis/QGIS/issues/66324) | [PR \#66607](https://github.com/qgis/QGIS/pull/66607) | Niet aanbevolen |
| Qgis have problem to render GeometryCollection for Gml, other viewer like mygeodata website render ok | [\#66225](https://github.com/qgis/QGIS/issues/66225) | Duplicaat |  |
| 3.44.7-Solothurn Crashes on New Shapefile | [\#66220](https://github.com/qgis/QGIS/issues/66220) | [PR \#66609](https://github.com/qgis/QGIS/pull/66609) | [PR \#66648](https://github.com/qgis/QGIS/pull/66648) |
| Add inja escape() function to HTML escape values | [GHSA-cr49-pm9v-m788](https://github.com/qgis/QGIS/security/advisories/GHSA-cr49-pm9v-m788) | [PR \#66616](https://github.com/qgis/QGIS/pull/66616) | [PR \#66670](https://github.com/qgis/QGIS/pull/66670) |
| Regression with decimal values and negative number in color gradient in the layer style panel | [\#65566](https://github.com/qgis/QGIS/issues/65566) | [PR \#66619](https://github.com/qgis/QGIS/pull/66619) | [PR \#66671](https://github.com/qgis/QGIS/pull/66671) |
| QGIS Server: GetProjectSettings returns the error message "Layer(s) not valid" with two WMS layers | [\#65872](https://github.com/qgis/QGIS/issues/65872) | Kan niet worden gereproduceerd |  |
| raster histogram not working for raster with scale factor | [\#65920](https://github.com/qgis/QGIS/issues/65920) | [PR \#66640](https://github.com/qgis/QGIS/pull/66640) | NOG TE DOEN |
| Advanced Digitizing Floater is not wide enough to show whole value | [\#65171](https://github.com/qgis/QGIS/issues/65171) | [PR \#66663](https://github.com/qgis/QGIS/pull/66663) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Custom Toolbar Position Loss | [\#65862](https://github.com/qgis/QGIS/issues/65862) | [PR \#66483](https://github.com/qgis/QGIS/pull/66483) | N/B |
| Export to PDF from layout changes colors | [\#42935](https://github.com/qgis/QGIS/issues/42935) | Not a bug (Was an Adobe issue IMHO) |  |
| Layout bleeding to edge outside map window | [\#49638](https://github.com/qgis/QGIS/issues/49638) | Vast |  |
| Fix flaky test_gui_fileuploader | Niet gerapporteerd | [PR \#66543](https://github.com/qgis/QGIS/pull/66543) |  |
| Hidden actions from user defined toolbar are still visible. | Niet gerapporteerd | [PR \#66620](https://github.com/qgis/QGIS/pull/66620) |  |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [\#58303](https://github.com/qgis/QGIS/issues/58303) | [PR \#66621](https://github.com/qgis/QGIS/pull/66621) | NOG TE DOEN |
| Password is not removed when it's at the the end of uri | Niet gerapporteerd | [PR \#66625](https://github.com/qgis/QGIS/pull/66625) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: Bug fixes by Germán Carrillo (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Allow QGIS to access curves from OGC API provider | Niet gerapporteerd | [PR \#66452](https://github.com/qgis/QGIS/pull/66452) | N/B |
| Elevation profile - changing layer symbology crashes QGIS / Wrong rendering order of Elevation profile items after changing the color of a profile item / Elevation profile stops respecting layer order on layer properties change | [\#64952](https://github.com/qgis/QGIS/issues/64952), [\#62677](https://github.com/qgis/QGIS/issues/62677), [\#64806](https://github.com/qgis/QGIS/issues/64806) | [PR \#66360](https://github.com/qgis/QGIS/pull/66360) | N/B |
| QGIS crashes on registering a Custom Profile Source with 'Sync Layers to Project' active | [\#65056](https://github.com/qgis/QGIS/issues/65056) | [PR \#66455](https://github.com/qgis/QGIS/pull/66455) | N/B |
| QGIS hangs when opening raster calculator (Meu Qgis está travando ao tentar abrir a calculadora raster) | [\#66327](https://github.com/qgis/QGIS/issues/66327) | Kan niet worden gereproduceerd |  |
| Ensure consistency in MultiCurves: don't allow NurbsCurves | Niet gerapporteerd | [PR \#66676](https://github.com/qgis/QGIS/pull/66676) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by David Signer (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix field displayString on primitive JSON values | Niet gerapporteerd | [PR \#66575](https://github.com/qgis/QGIS/pull/66575) | N/B |
| Fix bad behavior on widget detection of JSON fields | [\#62377](https://github.com/qgis/QGIS/issues/62377) | [PR \#66494](https://github.com/qgis/QGIS/pull/66494) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [David Signer (OPENGIS.ch)](https://opengis.ch/)
### Feature: Bug fixes by Stefanos Natsis (Lutra Consulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Windows QGIS 4 installs plugin with ACL that do not include SYSTEM or Administrators | [\#66515](https://github.com/qgis/QGIS/issues/66515) | [PR \#66576](https://github.com/qgis/QGIS/pull/66576) | N/B |
| Crash when clicking on an unavailable layer in Layers panel | [\#65913](https://github.com/qgis/QGIS/issues/65913) | [PR \#66578](https://github.com/qgis/QGIS/pull/66578) | NOG TE DOEN |
| QGIS server OGC API: Limits and offset parameters ignored when plugin changing parameters | [\#65858](https://github.com/qgis/QGIS/issues/65858) | Vast | [PR \#66480](https://github.com/qgis/QGIS/pull/66480) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Unbreak QGIS with GDAL \>= 3.13 | [commit ffdb8e3](https://github.com/qgis/QGIS/commit/ffdb8e3b27035478c533f37087505e749cc15b9b) | [PR \#66615](https://github.com/qgis/QGIS/pull/66615) | N/B |
| concat() returns NULL when all arguments are NULL: it should return an empty string | [\#65808](https://github.com/qgis/QGIS/issues/65808) | [PR \#66618](https://github.com/qgis/QGIS/pull/66618) | NOG TE DOEN |
| Remove all the parts in a geometry creates an empty geometry instead of NULL | [\#65453](https://github.com/qgis/QGIS/issues/65453) | WIP | TODO / Not recommended ? |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)

{{<content-end >}}
