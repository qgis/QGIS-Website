---
HasBanner: false
draft: false
releaseDate: '2023-10-29'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.34
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.34{#changelog334 }
![image0](images/entries/334splash.webp)

Datum uitgave 29-10-2023

Wij brengen u QGIS 3.34, een belangrijke uitgave van het Project QGIS die significante verbeteringen brengt voor de mogelijkheden van de open-bron georuimtelijke gegevensanalyse en visualisatie-software in QGIS.

Deze uitgave omvat een variëteit aan verbeteringen aan bestaande API's, expressies en gereedschappen, aanpassingen aan afdruklay-out, en verbeteringen aan de opties voor renderen van zowel context in 2D als in 3D.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=LHFVo0edaXE>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/LHFVo0edaXE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Cesium 3D-tegels
Thanks to an ecosystem grant from the [Cesium](https://www.cesium.com/) project, QGIS now has support for loading in 3D content in the Cesium 3D Tiles format! Tiles can be loaded from either local or remote datasources (including the Cesium ion platform and the Google Earth photorealistic tiles), and are visible in both 2D and 3D map views. In 2D views users can control the appearance of tile content by styling in either their original textures or in a wireframe view of the tile geometries, and users also have control over the desired level of detail in both 3D and 2D views.

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/lvl8zVZ8glY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk) en [Nyall Dawson](https://github.com/nyalldawson)
## Kaartgereedschap
### Feature: Optional enforcement of \"dot\" as decimal separator for measure tool
A new `Always use decimal point` checkbox option has been added to the Measure Tool. This option will ensure that measurements and coordinates are copied to the clipboard using a decimal point (dot) separator, even if the current locale uses a comma.

Dit schakelt de mogelijkheid in om kommagescheiden (csv)-gegevens te kopiëren, zelfs in gevallen waar de gebruiker een komma gebruikt als het decimale scheidingsteken.

![image1](images/entries/ec6084247b2b698045a783e2b007b0e0dde90ddd.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Accent weergeven op geïdentificeerde rasterpixels bij gebruiken van gereedschap Objecten identificeren
QGIS geeft nu de geometrie van het resultaat van het geïdentificeerde object weer voor rasterpixels in het kaartvenster. Dit komt overeen met het bestaande gedrag van het gereedschap Objecten identificeren voor objecttypen vector, vectortegel, en puntenwolk.

This is useful when a identifying a raster which has sections of similar colored pixels and it\'s difficult to visually determine the exact extent of a pixel.

![image2](images/entries/dc219caa150c9bbcb15aece90744f63e54ec25a1.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Raster met rij/kolom weergeven van geklikt punt in resultaten Objecten identificeren
Bij  het gebruiken van het gereedschap Objecten identificeren op rasterlagen zullen de afgeleide resultaten nu het rij- en kolomnummer weergeven van de geïdentificeerde pixel.

![image3](images/entries/0889d275dfefea4c7c7d13ebc5dc6fd237573076.webp)

Deze mogelijkheid werd ontwikkeld door [Hannes & Nyall Dawson](https://github.com/kannes)
## Symbologie
### Mogelijkheid: Instelling voor overschrijven kleur en symbool van selectie voor vectorlagen
Nieuwe instellingen voor renderen van lagen stellen gebruikers in staat de kleur en het symbool te beheren dat zal worden gebruikt in plaats van de standaarden voor systeem of project bij het accentueren van geselecteerde objecten.

Deze instelling is gedefinieerd voor elke laag en is nuttig om de zichtbaarheid van geselecteerde objecten te verbeteren door het toepassen van een expliciet gedefinieerde symbologie.

Dit is nuttig in verscheidene scenario's, inclusief gevallen waar:
- De laag een kleur voor een symbool of stijl gebruikt die overeenkomt met de symbologie van de selectie, wat resulteert in het niet zichtbaar zijn van de selectie van objecten
- Een lijnlaag gebruikt een dun symbool, en kleuren van geselecteerde lijnen maakt ze niet zichtbaar genoeg
- Lagen met complexe symbologie (zoals raster/ kleurverloop vullingen/ lijnen/ shapeburst met een kleurenbalk) zouden geen standaardkleur voor selectie hebben toegepast. In deze scenario's kan de gebruiker nu een eenvoudiger symbool specificeren om te gebruiken voor geselecteerde objecten op de laag.

![image4](images/entries/c648e5905c6c69e7a1e7c1dc91e3a15de1c8d523.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Labelen
### Mogelijkheid: Labels schakelen voor lagen vectortegel
Gebruikers kunnen nu schakelen met labels voor lagen met vectortegels met het paneel voor opmaken van de laag met vectortegel en het contextmenu van de laag in de inhoudsopgave van het paneel Lagen, wat effectief de schakelmogelijkheden voor vectorlagen vervangt.

This functionality is enabled by the addition of new functions to the `QgsVectorTileLayer` API by replicating the existing functionality on `QgsVectorLayer`.

![image5](images/entries/9e04c9c98886edf1d34eeb9750dc8f5c94946b51.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Renderen
### Feature: \"Sticky\" Map Decorations
Dynamic map decorations are now rendered to a transparent overlay, preventing re-rendering of decoration objects (such as title or scale bar) during navigation. The `QgsMapDecoration` now also includes `hasFixedMapPosition` to fix a decoration to a geographic location.

![image6](images/entries/00e6bc11fa3025317740f955962ef50cc1b95336.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Profileren kaartrenderer toegevoegd
The debugging/ development profiling tools have been extended with a new \"map render\" profile (accompanying the existing Startup and Project Load profiles).

Met dit gereedschap zijn gebruikers in staat pijnpunten te identificeren in het renderen van hun kaart en exact te bepalen welke lagen de lange duur van het opnieuw tekenen van de kaart veroorzaken.

![image7](images/entries/50fd809522d42944942ca7a059807f59fdcec5d2.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add choice of two different modes for \"Refresh Layer at Interval\"
When using \"Refresh Layer at Interval\" on vector layers, previous versions of QGIS would simply redraw the layer (for animations etc.), without refreshing data from the data source.

Een nieuw widget is verschaft dat gebruikers in staat stelt de opties voor het bijwerken van de laag te selecteren overeenkomstig het door hen gebruikte gebruiksgeval:
- \"Reload Data\": The layer will be completely refreshed. Any cached data will be discarded and re-fetched from the provider. This mode may result in slower map refreshes.
- \"Redraw Layer Only\": This mode is useful for animations or when the layer style should be updated at regular intervals. Canvas updates are deferred in order to avoid refreshing multiple times if more than one layer has an automatic update interval set.

![image8](images/entries/e0b0d4561cf7963d9a16bef9f77ea8214fe15f7b.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## 3D-objecten
### Mogelijkheid: Configuratie van beperking geheugen GPU toestaan
Gebruikers kunnen nu de beperking van het geheugen voor de GPU configureren voor elke laag (eerder vastgezet op 500MB per entiteit/ laag)

Een waarschuwing wordt ook weergegeven als een grens wordt bereikt, wat zou moeten helpen bij het oplossen van problemen van grote scenes.

Deze functionaliteit is nuttig voor gebruikers die grote 3D-scenes gebruiken die de beschikbare geheugenbronnen van de GPU uitputten.

![image9](images/entries/161c61a6ec3ca078e4483279c54f25319bed2c20.webp)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Mogelijkheid: Ondersteuning voor boundingbox3d toegevoegd
Additional API methods for relevant geometry classes are now available for `boundingBox3D` and `calculateBoundingBox3D`, as well as extensions to `boundingBoxIntersects` methods which will now support checking intersections between 3D bounding boxes.

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Afdruklay-outs
### Mogelijkheid: Meerdere lay-outitems selecteren
Nieuwe functionaliteit wordt verschaft voor het afhandelen van het selecteren van meerdere items tegelijkertijd uit de lijst met items in afdruklay-outs.

Dit verbetert ook de gebruikerservaring van bestaande functionaliteit voor selecteren van meerdere die beschikbaar is met visuele selecties door het selecteren van het item te synchroniseren met de lijst met items.

![image10](images/entries/85d915ba102341669b4ccccab308a987b0927d68.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Nummer pagina lay-out weergegeven in Pagina-eigenschappen
When a layout has more than one page, the current page number will be displayed in the item properties header section using the format `page_number`/`pagecount`.

![image11](images/entries/367986f087f878b47fe1296fcd8143ef677b3430.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Automatisch openen van geëxporteerde lay-outs
A new \"Open file after exporting\" checkbox option has been added to the export options for PDF, SVG, and Image output types. When selected this option will attempt to automatically open the output file once the export is completed.

The application used to open the file will use the configured default application on the system based on type (using `QDesktopServices::openUrl`). This feature will leverage the user settings API to remember the selection for the active user profile.

![image12](images/entries/502d122401e26d6dca10146dbdb9ccd1b01e8bd3.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Expressies
### Mogelijkheid: Expressiefunctie voor richting toegevoegd
A new `bearing` function has been added which computes the bearing angle (in radians) between two points.

De richting wordt bepaald in het opgegeven CRS en met de klok mee gemeten in de opgegeven ellipsoïde.

![image13](images/entries/a1d3176b8434f43bb248926df46c406f4b5f2625.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add \"layer_crs_ellipsoid\"
QGIS expressions now include a `layer_crs_ellipsoid` layer variable, as well as the `crs_ellipsoid` property available from the `layer_property` function. The value returned will be the ellipsoid acronym of the layer CRS.

![image14](images/entries/25fa0e9a64d6d1ea6b22e0e9b29ced356bbc96c8.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Digitaliseren
### Feature: Improve \"avoid overlap\" type awareness
When digitizing features with the \"avoid overlap\" option, QGIS has improved the behavior of automatically coercing the feature type and includes more meaningful messages to notify users of the automated behaviours.

Een voorbeeld voor het gebruik zou kunnen zijn het digitaliseren van een meerdelige polygoon in een doellaag met eendelige polygonen, die niet kan worden opgeslagen. QGIS zal nu automatisch alleen het grootste deel van de polygoon behouden, en gebruikers vragen om optioneel de aanvullende objecten te herstellen als eendelige polygonen.

This prevents the digitizing of \"sliver\" polygons and frustrations with improper feature types.

![image15](images/entries/e86392da95484a83eb7edbfd554526865d4195ff.gif)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://github.com/m-kuhn)
## Gegevensbeheer
### Mogelijkheid: Verbeterde afhandeling van opslaan van vectorobjecten voor al eerder bestaande bestanden
Bij het gebruiken van het algoritme Vectorobjecten opslaan naar bestand zal QGIS gebruikers informeren over het standaard gedrag voor de afhandeling van al bestaande bestanden (overschrijven bestanden) en de mogelijkheid verschaffen om uit een bereik van alternatieve gedragingen te selecteren (zoals het overschrijven van ene laag of toevoegen van nieuwe objecten aan bestaande laag)

Dit verbetert enorm de mogelijkheid voor gebruikers om gegevens te beheren met opslag indeling van gegevens in platte bestanden, zoals GeoPackage, daarbij het risico van gegevensverlies of ongewenste bijeffecten minimaliserend.

![image16](images/entries/2eaef470fbd823689e50cfd9fde3a747b888bc83.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Relaties behouden voor gekopieerde objecten
Nieuwe functionaliteit zorgt ervoor dat gekopieerde objecten op dezelfde laag door zullen gaan met het respecteren van de sterkte van projectrelatie(s).

Bij het kopiëren van objecten op dezelfde vectorlaag met gereedschappen voor kaart, attributentabel, of het gereedschap Objecten kopiëren/ verplaatsen, zal QGIS nu relaties in het geopende project opsporen en objecten dupliceren met intacte relaties.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Analyse-gereedschappen
### Mogelijkheid: Ondersteuning beschrijving rasterband
QGIS zal nu beschrijvingen van banden weergeven op de tab Symbologie voor rasterlagen, in aanvulling op het bandnummer.

![image17](images/entries/5a45eb1db489ef62f677a745efcca6c07935c4e8.webp)

Dit werd mogelijk gemaakt door Summer is getting warmer and warmer.

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Processing
### Mogelijkheid: Instelling Antialias voor rastertegel plug-in voor Processing
A new \"Enable antialiasing\" parameter has been added to the \"Generate XYZ Tiles\" processing tool.

Deze optie zal standaard ingeschakeld zijn (vervangt het huidige gedrag) maar stelt gebruikers in staat de antialiasing voor kaartinhoud uit te schakelen.

![image18](images/entries/9c9b07222673e23caf2dcc73ff1db8a8f9257106.webp)

Deze mogelijkheid werd ontwikkeld door [ASAI Hitoshi](https://github.com/hito-asa)
### Feature: Create Grid row_index and col_index fields
Fields for the `row_index` and `col_index` have been added to the output of the \"Create Grid\" processing algorithm. The fields are added to all outputs of type point, rectangle, and hexagon.

Veldwaarden zijn integers waarvan de telling begint met 0 en verhoogd van links naar rechts (kolom-index) en van boven naar beneden (rij-index).

![image19](images/entries/54157595e9bf9c58b4b906ea28b3c335a737696b.webp)

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/Poulpator)
### Feature: New \'Calculate expression\' algorithm for use in models
The new \"Calculate expression\" algorithm will calculate the results of a QGIS expression and make the result available for use in other parts of the model.

Het vermijdt de noodzaak om dezelfde expressie meerdere malen te moeten gebruiken in een model als hetzelfde resultaat meer dan eens moet worden gebruikt en verschaft aanvullende gevallen voor gebruik (zoals het genereren van een statische waarde tijdstempel om in het model te kunnen gebruiken).

![image20](images/entries/90b9d8da0ec1f13c638525cedd360a5c65d89c1a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme toegevoegd om inhoud uit een bestand GLTF/GLB te converteren naar standaard objecten voor vectorlagen
QGIS maakt nu het converteren van 3D-tegelinhoud in indelingen GLTF en GLB naar bewerkbare indelingen voor vectorobjecten mogelijk.

![image21](images/entries/6c95d6382b9e6abe72607df57dfefb8a4d9e8442.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Port SAGA \"DTM Filter (slope-based)\" tool to a native QGIS algorithm
The SAGA [DTM Filter tool](https://saga-gis.sourceforge.io/saga_tool_doc/8.1.0/grid_filter_7.html) has been ported to a native QGIS algorithm.

![image22](images/entries/740fdd036b19e5e0d2c13493d66e785fca89b46a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Opties voor toepassing en projecten
### Mogelijkheid: Lijst recent geopend project leegmaken
A \"Clear Recently Opened\" action is now listed at the bottom of the `Project → Open Recent` menu, which will remove every unpinned project from the menu.

An additional context menu is also available to enable the ability to remove individual projects from the recent project list, as well as \"pin\" and \"unpin\" items.

De status zal worden gesynchroniseerd tussen het menu Recent geopende projecten en het Welkomststcherm van QGIS.

![image23](images/entries/4ff4dd8614e4857810fc1b636d8700b143ec98b6.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: OAUTH2 PKCE authorisatie-code
An implementation of Proof Key for Code Exchange (PKCE, [RFC 7636](http://tools.ietf.org/html/rfc7636)) has been added for OAUTH2 [Authorization Code](https://oauth.net/2/grant-types/authorization-code/) flows, improving resilience to CSRF and code injection attacks.

Dit werd mogelijk gemaakt door Comune di Roma

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Standaarden voor Processing instellen vanuit QGIS configuratiebestand
QGIS ondersteunt nu de mogelijkheid om de standaardwaarden voor gereedschappen van de gebruikersinterface voor het QGIS Processing framewerk te configureren met parameters die zijn gespecificeerd in het bestand voor instellingen QGIS.ini.

This allows for the configuration of user-specific or organization-wide default values for certain algorithms. For example, to set the default value of the GRID_SIZE (precision) parameter on the intersection algorithm, the following configuration may be added to the `QGIS/QGIS3.ini` in the active user profile directory root:

    [Processing]
    DefaultGuiParam\native%3Aintersection\GRID_SIZE=0.01
    
Wanneer een gebruiker met deze configuratie de relevante Toolbox opent om een algoritme uit te voeren, zal voor hem automatisch de standaardwaarde worden gespecificeerd.

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
## Profiel plotten
### Mogelijkheid: Instelling toegevoegd voor het beheren van de achtergrondkleur voor diagrammen van hoogteprofielen
Deze optie (beschikbaar op de nieuwe tab Extra → Opties → Hoogte) stelt gebruikers in staat een specifieke kleur te gebruiken als de achtergrondkleur voor hoogteprofielen.

Dit kan voor bepaalde gegevensset het diagram beter leesbaar maken, bijv. puntenwolken met RGB-kleuren, waar de achtergrondkleur heel veel lijkt op de kleuren van de punten om gemakkelijk onderscheid te kunnen maken.

Dit is een instelling opt-in, en standaard zullen de hoogteprofielen doorgaan met het gebruiken  van de standaard achtergrondkleur van het systeem.

![image24](images/entries/e3bae5cc601894eca9775d5603cc3af6bd03c747.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Relaties ontdekken voor provider Oracle
QGIS ondersteunt nu het geautomatiseerd ontdekken van relaties voor de gegevensprovider Oracle.

![image25](images/entries/951d7ccce5b34532595a21373d721f581938c65b.webp)

Dit werd mogelijk gemaakt door Métropole de Lille

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
## Plug-ins
### Mogelijkheid: Interactieve shell verwijderd uit plug-in GRASS C++
Om redenen van onderhoud is de interactieve shell voor de plug-in GRASS C++ Plugin, als ook het ingebedde QTermWidget, verwijderd uit toekomstige uitgaven.

Het ligt in de lijn der verwachting dat de plug-in GRASS Processing Plugin prioritaire ontwikkeling zal krijgen en ondersteuning voor onderhoud zal worden doorgezet, en verschaffen van een interactieve shell voor GRASS is geen kritische functionaliteit voor QGIS zelf, maar meer iets dat gebruikers zelf extern kunnen beheren.

Further details on the specifics of this feature cleanup can be found on the feature [Pull Request](https://github.com/qgis/QGIS/pull/53597).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Programmeerbaarheid
### Mogelijkheid: Functie om runtime profiler modelinhoud als tekst te exporteren
A new function has been added to allow for the export of the current runtime profiler (`QgsRuntimeProfiler`) model content as a multi-line text string.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (itOpen / qcooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS cannot connect to MySQL if user\'s password contains commas. | [#54493](https://github.com/qgis/QGIS/issues/54493) | [PR #54573](https://github.com/qgis/QGIS/pull/54573) | Nee |
| QGIS WFS server will look for .qgz file in wrong place if \"map\" is in path | [#54533](https://github.com/qgis/QGIS/issues/54533) | [PR #54639](https://github.com/qgis/QGIS/pull/54639) | [PR #54855](https://github.com/qgis/QGIS/pull/54855) |
| Raster layer transparency/opacity not stored in saved style | [#54496](https://github.com/qgis/QGIS/issues/54496) | [PR #54644](https://github.com/qgis/QGIS/pull/54644) | [PR #54854](https://github.com/qgis/QGIS/pull/54854) |
| WMS GetPrint with ATLAS_PK has incorrect layers visibility in versions \>= 3.22 | [#54475](https://github.com/qgis/QGIS/issues/54475) | [PR #54651](https://github.com/qgis/QGIS/pull/54651) | [PR #54663](https://github.com/qgis/QGIS/pull/54663) |
| Error saving edit on PostGIS geometry when table also contains geography | [#54572](https://github.com/qgis/QGIS/issues/54572) | [PR #54664](https://github.com/qgis/QGIS/pull/54664) | [PR #54714](https://github.com/qgis/QGIS/pull/54714) |
| Cant subtract or add angles since the degrees symbol has been added | [#54501](https://github.com/qgis/QGIS/issues/54501) | [PR #54687](https://github.com/qgis/QGIS/pull/54687) | N/B |
| WCS Keep Unavailable Layers | [#54702](https://github.com/qgis/QGIS/issues/54702) | [PR #54707](https://github.com/qgis/QGIS/pull/54707) | N/B |
| taxon legend from map whis atlas | [#54654](https://github.com/qgis/QGIS/issues/54654) | [PR #54692](https://github.com/qgis/QGIS/pull/54692) | N/B |
| Spinbox for colum space in legends does not allow to set values above 99.99 units | [#54682](https://github.com/qgis/QGIS/issues/54682) | [PR #54709](https://github.com/qgis/QGIS/pull/54709) | N/B |
| Geometry Error SpatiaLite Database | [#54662](https://github.com/qgis/QGIS/issues/54662) | [PR #54734](https://github.com/qgis/QGIS/pull/54734) | N/B |
| Splitting MultiLineStrings gives awkward results | [#54155](https://github.com/qgis/QGIS/issues/54155) | [PR #54744](https://github.com/qgis/QGIS/pull/54744) | [PR #54851](https://github.com/qgis/QGIS/pull/54851) |
| Open project, then layer properties, close, close project: qgis thinks something has changed | [#54741](https://github.com/qgis/QGIS/issues/54741) | [PR #54757](https://github.com/qgis/QGIS/pull/54757) | N/B |
| Width field of attribute tables in print layouts only uses locale when being edited | [#54204](https://github.com/qgis/QGIS/issues/54204) | [PR #54769](https://github.com/qgis/QGIS/pull/54769) | [PR #54781](https://github.com/qgis/QGIS/pull/54781) |
| Data Source Manger - Browser: Close and Help buttons are missing | [#54171](https://github.com/qgis/QGIS/issues/54171) | [PR #54770](https://github.com/qgis/QGIS/pull/54770) | N/B |
| 0 port in OAuth2 callback URI | [#54562](https://github.com/qgis/QGIS/issues/54562) | Kan niet worden gereproduceerd | N/B |
| QGIS Crashes when editing multiple features simultaneously that have a Value Relation field | [#54164](https://github.com/qgis/QGIS/issues/54164) | [PR #54889](https://github.com/qgis/QGIS/pull/54889) | NOG TE DOEN |
| Crash when playing with duplicated legends in layout | [#52268](https://github.com/qgis/QGIS/issues/52268) | [PR #54947](https://github.com/qgis/QGIS/pull/54947) |  |
| QGIS fails to request more than one WMS-Layer | [#55042](https://github.com/qgis/QGIS/issues/55042) | [PR #55064](https://github.com/qgis/QGIS/pull/55064) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgsgeos.cpp: fix a -Wunused-variable warning | niet gerapporteerd | [PR #54612](https://github.com/qgis/QGIS/pull/54612) | N/B |
| qgsvirtualpointcloudprovider.cpp: add a missing variable initialization | niet gerapporteerd | [PR #54613](https://github.com/qgis/QGIS/pull/54613) | N/B |
| OAPIF does not honour the view extent | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053400.html) | [PR #54617](https://github.com/qgis/QGIS/pull/54617) | [PR #54792](https://github.com/qgis/QGIS/pull/54792) |
| Does QGIS require units \"m\" for the projection coordinate variables in a netCDF/CF file? | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053413.html) | [GDAL PR 8407](https://github.com/OSGeo/gdal/pull/8407) | N/B |
| Syntactical error with the use of == instead of = for comparison in the WHERE clause | [#54608](https://github.com/qgis/QGIS/issues/54608) | Al gerepareerd | Kan geen aanvullende lagen schrijven naar een bestaande FGDB |
| Add minimal CRS information to sqlite exports | [#54560](https://github.com/qgis/QGIS/issues/54560) | [PR #54630](https://github.com/qgis/QGIS/pull/54630) | [PR #54715](https://github.com/qgis/QGIS/pull/54715) |
| Complex Attributes in OGC API Feature-Items have empty content | [#54275](https://github.com/qgis/QGIS/issues/54275) | [PR #54631](https://github.com/qgis/QGIS/pull/54631) | [PR #54679](https://github.com/qgis/QGIS/pull/54679) |
| GPX Provider: missing element when importing gpx file | [#54119](https://github.com/qgis/QGIS/issues/54119) | [PR #54632](https://github.com/qgis/QGIS/pull/54632) | N/B |
| Saving edits on larger vector layers is slow | [#53043](https://github.com/qgis/QGIS/issues/53043) | [PR #54633](https://github.com/qgis/QGIS/pull/54633) | N/B |
| QgsVectorLayerSaveAsDialog: uncheck \'Add saved filed to map\' when selecting PGDump driver (refs #54548) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | Is het niet waard |
| Spatial filtering of multipart polygons within a shapefile dataset broken | [GDAL issue 8481](https://github.com/OSGeo/gdal/issues/8481) | Is geen probleem |  |
| qgis cannot find/identify a polygon feature by clicking a newly created (multi)polygon part | [#54537](https://github.com/qgis/QGIS/issues/54537) | [PR #54761](https://github.com/qgis/QGIS/pull/54761) | [PR #54782](https://github.com/qgis/QGIS/pull/54782) |
| qgis cannot find/identify a polygon feature by clicking a newly created (multi)polygon part | [#54537](https://github.com/qgis/QGIS/issues/54537) | [GDAL PR 8483](https://github.com/OSGeo/gdal/pull/8483) | [GDAL PR 8503](https://github.com/OSGeo/gdal/pull/8503) |
| Export to spreadsheet creates an xlsx file with errors when exporting empty tables/layers | [#42945](https://github.com/qgis/QGIS/issues/42945) | [GDAL PR 8484](https://github.com/OSGeo/gdal/pull/8484) | [GDAL PR 8515](https://github.com/OSGeo/gdal/pull/8515) |
| export bbox wrong when feature crosses anti-prime-meridion (180 deg) | [#42827](https://github.com/qgis/QGIS/issues/42827) | [GDAL PR 8485](https://github.com/OSGeo/gdal/pull/8485) | Is het niet waard |
| QgsVectorDataProvider.changeAttributeValues() returns True even when it fails | [#54816](https://github.com/qgis/QGIS/issues/54816) | [PR #54905](https://github.com/qgis/QGIS/pull/54905) | [PR #54909](https://github.com/qgis/QGIS/pull/54909) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Feature: Bug fixes by Paul Blottiere (Hytech-imaging)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix segfault in coordinate transform | niet gerapporteerd | [PR #54609](https://github.com/qgis/QGIS/pull/54609) | N/B |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [#54598](https://github.com/qgis/QGIS/issues/54598) | [PR #54667](https://github.com/qgis/QGIS/pull/54667) | N/B |
| Database string connection visible in the message bar/QGIS logs | [#54437](https://github.com/qgis/QGIS/issues/54437) | [PR #54650](https://github.com/qgis/QGIS/pull/54650) | N/B |
| PostGIS Connection\'s \"Session ROLE\" is not kept | [#54638](https://github.com/qgis/QGIS/issues/54638) | [PR #54681](https://github.com/qgis/QGIS/pull/54681) | N/B |
| Example files are installed by the server build, and additionally they are in a wrong place | [#54423](https://github.com/qgis/QGIS/issues/54423) | [PR #54708](https://github.com/qgis/QGIS/pull/54708) | N/B |
| Point to Path tool causes QGIS to crash | [#54686](https://github.com/qgis/QGIS/issues/54686) | [PR #54710](https://github.com/qgis/QGIS/pull/54710) | [PR #54784](https://github.com/qgis/QGIS/pull/54784) |
| qgs/qgz project does not save mesh symbology correctly | [#54384](https://github.com/qgis/QGIS/issues/54384) | [PR #54711](https://github.com/qgis/QGIS/pull/54711) | N/B |
| Endless loop if profile is drawn outside layer extent | [#54349](https://github.com/qgis/QGIS/issues/54349) | [PR #54745](https://github.com/qgis/QGIS/pull/54745) | N/B |
| Server: Can\'t enable WFS3 API update endpoint (PUT/PATCH) on layers without geometry | [#46119](https://github.com/qgis/QGIS/issues/46119) | [PR #54789](https://github.com/qgis/QGIS/pull/54789) | N/B |
| Add safe guard around -of in gdal command for batch processing | [#54122](https://github.com/qgis/QGIS/issues/54122) | [PR #54800](https://github.com/qgis/QGIS/pull/54800) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Hytech-imaging)](https://hytech-imaging.fr/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli (strk)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Have QgsRectangle null rectangle printed as EMPTY in wkt | niet gerapporteerd | [PR #54831](https://github.com/qgis/QGIS/pull/54831) | N/B |
| Fix aspect ratio computation in QgsLayoutItemMap::zoomToExtent | niet gerapporteerd | [PR #54827](https://github.com/qgis/QGIS/pull/54827) | N/B |
| Do not include a BoundingBox tag in GetFeatureInfo responses, when it is null | niet gerapporteerd | [PR #54858](https://github.com/qgis/QGIS/pull/54858) | N/B |
| Always run the spell and shell checkers if possible, print warning when not possible | niet gerapporteerd | [PR #54847](https://github.com/qgis/QGIS/pull/54847) | N/B |
| Tweak Null rectangle handling | niet gerapporteerd | [PR #54872](https://github.com/qgis/QGIS/pull/54872) | N/B |
| Run spellcheck only on changed files in prepare_commit.sh | niet gerapporteerd | [PR #54893](https://github.com/qgis/QGIS/pull/54893) | N/B |
| Fix prepare_commit.sh | niet gerapporteerd | [PR #54918](https://github.com/qgis/QGIS/pull/54918) | N/B |
| Fix extent computation in QgsSpatiaLiteProvider | niet gerapporteerd | [PR #54917](https://github.com/qgis/QGIS/pull/54917) | N/B |
| Do not force verbose build in mingw build | [#54932](https://github.com/qgis/QGIS/issues/54932) | [PR #54924](https://github.com/qgis/QGIS/pull/54924) | N/B |
| Make QgsBookmark string output more explicit about it being EMPTY | niet gerapporteerd | [PR #54923](https://github.com/qgis/QGIS/pull/54923) | N/B |
| Fix extent computation in QgsAFSProvider | niet gerapporteerd | [PR #54944](https://github.com/qgis/QGIS/pull/54944) | N/B |
| Add `tags` make target | niet gerapporteerd | [PR #54948](https://github.com/qgis/QGIS/pull/54948) | N/B |
| Handle null rectangles in QgsExtentWidget::outputExtent | niet gerapporteerd | [PR #54953](https://github.com/qgis/QGIS/pull/54953) | N/B |
| Handle null in QgsRectangle grow() and include() methods | niet gerapporteerd | [PR #54955](https://github.com/qgis/QGIS/pull/54955) | N/B |
| Add QgsRectangle::setNull(), deprecating setMinimal() | niet gerapporteerd | [PR #54934](https://github.com/qgis/QGIS/pull/54934) | N/B |
| Handle Null rectangle in QgsRectangle::buffered | niet gerapporteerd | [PR #54967](https://github.com/qgis/QGIS/pull/54967) | N/B |
| Fix extent computation in QgsVirtualLayerProvider | niet gerapporteerd | [PR #54976](https://github.com/qgis/QGIS/pull/54976) | N/B |
| Add a QgsRectangle::createNull() temporary static method | niet gerapporteerd | [PR #55008](https://github.com/qgis/QGIS/pull/55008) | N/B |
| Fix testRegisterFeatureUnprojectible - Use valid extent in testRegisterFeatureUnprojectible | niet gerapporteerd | [PR #55011](https://github.com/qgis/QGIS/pull/55011) | N/B |
| Have QgsGeometry::boundingBox return null rect for null geom | niet gerapporteerd | [PR #55012](https://github.com/qgis/QGIS/pull/55012) | N/B |
| Have QgsGeometry::fromRect(NULL RECT) return null geometry | niet gerapporteerd | [PR #54954](https://github.com/qgis/QGIS/pull/54954) | N/B |
| Stop considering Rectangle(0,0,0,0) null - while Rectangle(1,1,1,1) is not null | [#45563](https://github.com/qgis/QGIS/issues/45563) | [PR #54646](https://github.com/qgis/QGIS/pull/54646) | N/B |
| Run doxygen layout checker in prepare-commit script, when possible | niet gerapporteerd | [PR #54936](https://github.com/qgis/QGIS/pull/54936) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Sandro Santilli (strk)](http://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgs3daxissettings: Correctly read viewport ratio on a saved project | niet gerapporteerd | [PR #54870](https://github.com/qgis/QGIS/pull/54870) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Don\'t show help for algorithms which can\'t be run in qgis_process | [#54914](https://github.com/qgis/QGIS/issues/54914) | [PR #54920](https://github.com/qgis/QGIS/pull/54920) | In behandeling |
| Fix crashes in layout designer | [#52079](https://github.com/qgis/QGIS/issues/52079) | [PR #54907](https://github.com/qgis/QGIS/pull/54907) | Te indringend |
| Fix layout label adjust size to text logic | niet gerapporteerd | [PR #54896](https://github.com/qgis/QGIS/pull/54896) | In behandeling |
| Fix toggling visibility of group layers resets child layer mask blend modes | [#53088](https://github.com/qgis/QGIS/issues/53088) | [PR #54897](https://github.com/qgis/QGIS/pull/54897) | N/B |
| Ensure identify highlight works for very transparent symbols | [#54830](https://github.com/qgis/QGIS/issues/54830) | [PR #54864](https://github.com/qgis/QGIS/pull/54864) | [PR #54883](https://github.com/qgis/QGIS/pull/54883) |
| Fix layout maps force rasterisation of whole layout when map item has transparency set | niet gerapporteerd | [PR #54882](https://github.com/qgis/QGIS/pull/54882) | Te indringend |
| Fix crash in merge features dialog when a field has a unique constraint set | [#54856](https://github.com/qgis/QGIS/issues/54856) | [PR #54862](https://github.com/qgis/QGIS/pull/54862) | [PR #54878](https://github.com/qgis/QGIS/pull/54878) |
| Fix initial zoom level when opening layout designer windows | [#44421](https://github.com/qgis/QGIS/issues/44421) | [PR #54849](https://github.com/qgis/QGIS/pull/54849) | [PR #54880](https://github.com/qgis/QGIS/pull/54880) |
| Fix hang when exporting 3d maps | [#50067](https://github.com/qgis/QGIS/issues/50067) | [PR #54845](https://github.com/qgis/QGIS/pull/54845) | Te riskant |
| Fix layout labels don\'t immediately react to changes when semi-transparent | niet gerapporteerd | [PR #54839](https://github.com/qgis/QGIS/pull/54839) | [PR #54863](https://github.com/qgis/QGIS/pull/54863) |
| Fix crash when opening layer properties for raster layer with broken data source | [#49176](https://github.com/qgis/QGIS/issues/49176) | [PR #54812](https://github.com/qgis/QGIS/pull/54812) | [PR #54838](https://github.com/qgis/QGIS/pull/54838) |
| Fix Execute SQL exeception | [#54833](https://github.com/qgis/QGIS/issues/54833) | [PR #54837](https://github.com/qgis/QGIS/pull/54837) | [PR #54842](https://github.com/qgis/QGIS/pull/54842) |
| Cleanup all browser layer properties dialog before exiting | [#39094](https://github.com/qgis/QGIS/issues/39094) | [PR #54808](https://github.com/qgis/QGIS/pull/54808) | [PR #54822](https://github.com/qgis/QGIS/pull/54822) |
| Avoid loss of attributes when calculating fields | [#47385](https://github.com/qgis/QGIS/issues/47385) | [PR #54815](https://github.com/qgis/QGIS/pull/54815) | [PR #54879](https://github.com/qgis/QGIS/pull/54879) |
| Fix crash when changing layers between editable/non-editable layers | [#54802](https://github.com/qgis/QGIS/issues/54802) | [PR #54813](https://github.com/qgis/QGIS/pull/54813) | N/B |
| Fix QgsField::ConfigurationFlag::None causes syntax error when starting PyQGIS | niet gerapporteerd | [PR #54809](https://github.com/qgis/QGIS/pull/54809) | N/B |
| Handle sql=\'\' or sql=\"\" as empty sql strings instead of \'\' / \"\" literals | [#53736](https://github.com/qgis/QGIS/issues/53736) | [PR #54806](https://github.com/qgis/QGIS/pull/54806) | [PR #54826](https://github.com/qgis/QGIS/pull/54826) |
| Fix crash when certain symbol pages are open in style dock and QGIS is closed or a new project opened | niet gerapporteerd | [PR #54749](https://github.com/qgis/QGIS/pull/54749) | Te indringend |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Masking with SVG symbol doesn\'t work | [#54926](https://github.com/qgis/QGIS/issues/54926) | [PR #54927](https://github.com/qgis/QGIS/pull/54927) |  |
| Bug on graduated symbology on French QGis 3.28.10 | [#54549](https://github.com/qgis/QGIS/issues/54549) | [PR #54943](https://github.com/qgis/QGIS/pull/54943) | [PR #54963](https://github.com/qgis/QGIS/pull/54963) |
| QGIS crashes when undoing moving of elements in map layout | [#52740](https://github.com/qgis/QGIS/issues/52740) | [PR #54959](https://github.com/qgis/QGIS/pull/54959) | [PR #54969](https://github.com/qgis/QGIS/pull/54969) |
| QGIS Crashes Upon Exporting Layout to PDF when Using Random Point Fill Symbology | [#54065](https://github.com/qgis/QGIS/issues/54065) | poly2tri issue <https://github.com/jhasse/poly2tri/issues/55> |  |
| Label expression with more than 32767 chars becomes invalid when switching from expression dialog back to layer properties | [#54141](https://github.com/qgis/QGIS/issues/54141) | [PR #55051](https://github.com/qgis/QGIS/pull/55051) | [PR #55052](https://github.com/qgis/QGIS/pull/55052) |
| Activating notify/listen feature crash QGIS | [#54260](https://github.com/qgis/QGIS/issues/54260) | [PR #55062](https://github.com/qgis/QGIS/pull/55062) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/)

{{<content-end >}}
