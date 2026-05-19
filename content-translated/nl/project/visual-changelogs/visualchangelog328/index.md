---
HasBanner: false
draft: false
releaseDate: 21-10-2022
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.28
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.28{#changelog328 }
![image1](images/projects/19a3cf4af4fcad7ecec62560b72067b903097054.png)

Datum uitgave 21-10-2022

QGIS 3.28 Firenze introduces various feature updates, UX modifications, usability enhancements, and improved integration with various proprietary services and data backends. It is also set to introduce the long-awaited features provided by previous releases into the long-term support release, as outlined in the [QGIS Roadmap](https://www.qgis.org/en/site/getinvolved/development/roadmap.html).

Het welkomstscherm geeft een bijzondere en buitengewone kaart van 1847 van Firenze, of Florence, Italië door Giuseppe Molini weer. Deze schitterende gegraveerde kaart werd origineel getekend in 1731 door de Florentijnse architect Ferdinando Ruggieri. Georiënteerd op het zuiden, bedekt de kaart het oude ommuurde centrum van Florence zoals dat werd uitgebreid aan beide zijden van de rivier de Arno. Het kwadrant rechtsboven geeft het symbool van de lelie van Florence weer. Hoewel afgedrukt in 1847, is deze kaart voorbereid in de stijl van de 17e eeuw door graveren op koperen platen op dik uitgevoerd papier. Firenze in 1847 stond op het punt van een politieke transformatie. Eén jaar na de productie van deze bijzondere kaart gaf de Groothertog van Toscane, als antwoord op de politieke demonstraties in Florence, Toscane zijn eerste grondwet.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://youtu.be/IEkOhQezQMk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/IEkOhQezQMk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Belangrijke wijzigingen
### Mogelijkheid: Vervallen achterwaartse compatibiliteit voor symbologie in project met QGIS 3.16 en ouder
Eerdere uitgaven van QGIS zouden significante hoeveelheden compatibiliteits-objecten schrijven naar de XML-structuur van projectbestanden om achterwaartse compatibiliteit te behouden voor symbologieën om er voor te zorgen dat projectbestanden kunnen worden geopend met QGIS 3.16 en ouder. Deze compatibiliteit is verwijderd uit toekomstige uitgaven, wat een significante optimalisatie voor de structuur van projectbestanden verschaft.
## Tijdbeheer
### Mogelijkheid: Ondersteuning voor Tijdbeheer toegevoegd voor WMTS-lagen met dimensie TIME
This enhancement exposes any WMTS \"time\" dimensions for use in the temporal framework, including allowing these layers to be animated and controlled via the temporal controller.

When we do detect a time dimension on a WMTS layer, we no longer expose this in the same way as other non-time dimensions. The browser panel does not show the dimension values, and adding the layer via Data Source Manager no longer prompts the user to pick from the available time values. Instead, these layers are indicated with a new \"time capable raster layer\" icon, and are added to a project without the user specifying a time value.

Just like a WMS(T) layer, when a time-dimension enabled WMTS layer is added to the project, it will default to the \"automatic\" temporal mode, meaning that the layer will follow the temporal controller\'s current time range by default. A user can then opt to show a specific static time value for the layer through the layer\'s Temporal properties page, by unchecking \"Dynamic Temporal Control\" and picking a specific available time range from the \"Predefined date\" option.

Dit zou de gebruikerservaring moeten unificeren zodat het gebruiken van WMTS tijd-ingeschakelde lagen essentieel identiek is aan het gebruiken van WMS(T)-lagen.

![image3](images/entries/8f0a6c8e4850886732633ab76d5873dffd7746c4.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Kaartgereedschap
### Mogelijkheid: Selecteren van objecten vector-tegellagen toestaan
Ondersteuning voor het selecteren van objecten uit vectortegellagen is toegevoegd, wat het voor gebruikers mogelijk maakt de standaard, op kaarten gebaseerde, gereedschappen voor selecteren te gebruiken om interactief objecten uit deze bronnen te selecteren.

Een gebruiker kan, als een vecttortegellaag een selectie heeft:
- De objecten kopiëren en ze plakken in andere lagen, of ze plakken in een geheugenlaag
- Use other (non-editing) tools which operate on selections, such as \"zoom to selected features\"/\"pan to selected features\"

Selecties kunnen worden gemaakt met behulp van elke van de interactieve op kaarten gebaseerde gereedschappen voor selecteren, bijv. selecteren op rechthoek, vrije hand, polygoon, of straal. Alle sneltoetsen die van toepassing zijn voor selecties van vectors voor toevoegen/aftrekken/kruisen van selecties zijn ook te gebruiken.

Selecteren van objecten wordt uitgevoerd met behulp van het tegel-zoomniveau van het kaartvenster, en dan worden de objecten, die op dit zoomniveau zijn geselecteerd, behouden, zelfs als de gebruiker de schaal van de kaart wijzigt naar een andere zoomniveau voor de vectortegel. Dit betekent dan een gebruiker kan inzoomen en een klein/gedetailleerd object kan selecteren, dan uitzoomen en nog steeds het object op de kaart zien.

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Exclusief venster, gebaseerd op gebruikerservaringen voor Databronnen beheren
The data source manager dialog is now ALWAYS non modal, and options to set it as such have been removed. The dialog now functions just like other \"manager\" type windows in QGIS, such as the style manager or layout manager.

Databronnen beheren zal in plaats daarvan worden behandeld als zijn eigen venster, dat op de voorgrond wordt geplaatst als op de knop Databronnen beheren wordt gedrukt.

![image4](images/entries/9bbc312e9b1362ae660a9719c910ab209d3e8a55.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Actie Weergeven in attributentabel toegevoegd aan het menu voor rechtsklikken van symbolen van klassen voor Legenda's
A new \"Show in Attribute Table\" action has been added to the right-click context menu of legend class symbols in the table of contents. This allows users to open the attribute table with a filter applied to match only the features relevant to a particular symbol group. This provides a significant performance improvement for certain datasets, such as large vector layers loaded from a remote source.

![image5](images/entries/8b43481bcab479b040b0a5ac5400ddc89c77dd0a.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Instelling toegevoegd om waarden NULL te verbergen in Identificatieresultaten
The \"Identify Features\" utility now provides the capability to hide NULL values from the returned results

![image6](images/entries/f0c7217db5f0104999a3d87c2229010dcc62cb50.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Symbologie
### Mogelijkheid: Toestaan van beheer over GPS-locatiemarkering
Een nieuwe algemene pagina voor opties voor GPS is geïntroduceerd die nieuwe instellingen bevat voor het beheren van het markeringssymbool dat wordt gebruikt voor de huidige GPS-locatie, en of dit symbool zou moeten worden geroteerd zodat het overeen komt met de GPS-richting.

![image7](images/entries/411b2d3b0f1b180857eda6d4e0c73144f1aeee57.gif)

Dit werd mogelijk gemaakt door Tiwi Resources, Bush Heritage, Australian Wildlife Conservancy

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe vormen voor ellips-markeringen toegevoegd
De symboolstijlen voor het type ellipsmarkering bevatten nu aanvullende typen vormen voor:
- Pentagon
- Hexagon
- Octagon
- 1/3-cirkel
- Kwartcirkel
- Ster

![image8](images/entries/3e749b405f10a24f95665cd0ad3e1ea0f199811b.webp)

Dit werd mogelijk gemaakt door North Road

This feature was developed by [ZayneTomlins](https://github.com/ZayneTomlins)
## Labelen
### Mogelijkheid Ondersteuning toegevoegd voor HTML-vet/cursief/lettergrootte en type lettertype voor labelen
Ondersteuning voor aanvullende tags voor opmaak in HTM zijn toegevoegd om te gebruiken bij labelen (en overal elders waar de tekstrenderer wordt gebruikt).

Onderetunde tags omvatten specifiek:
- lettertype familie
- lettergrootte
- vet
- cursief

![image9](images/entries/b49f780e98b4276b76cf3022b34da26dd4ed9d1f.webp)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie toegevoegd om absolute eenheden te gebruiken voor regelhoogte
Eerder werd de regelhoogte altijd ingesteld in meervouden van de regelafstand van de tekst. Het is nu echter mogelijk om absolute eenheden te gebruiken voor de regelhoogte (nuttig in contexten waarin gemixte tekstgrootten worden gebruikt binnen één enkel document).

![image10](images/entries/b413c593933bc197886a97919ae015880e119aa7.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Mazen
### Mogelijkheid: Optie toegevoegd om tijdelijke eigenschappen van lagen met mazen opnieuw te laden
An \"Always take reference time from data source\" option has been added for mesh layers that when checked, will ensure that the reference time is reloaded from the data source, and each time the layer is reloaded or the project reopened the time properties will be updated from the file automatically.

In previous releases, when a mesh layer file had a reference time and time extent that changed, the time layer properties would not be updated when the projector layer are reloaded, and the user would be required to manually navigate to the \"Reload from provider\" feature in the temporal tab of the layer properties.

![image11](images/entries/8bf480abed6701e5535110f8069ba1f63ecf2de4.gif)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://github.com/vcloarec)
## 3D-objecten
### Mogelijkheid:  3D-effect omgeving opnemen
Een nieuw effect voor het opnemen van de omgeving is beschikbaar voor het renderen van gegevens in 3D-weergaven, wat nuttig is voor het verbeteren van de perceptie van diepte van de gegevens in 3D. Dit is een nabewerkings-effect en het kan zelfs worden gecombineerd met eye dome lighting (EDL) voor bijzonder interessante resultaten. Een oversimplificatie van het effect is dat objecten die niet zichtbaar zijn voor de camera worden gebruikt nabijgelegen elementen te voorzien van textuur en donkerder te maken, met het voordeel van het verbeteren van contrast, definitie van het object en differentiatie.

Er is een nieuw item voor het beheren van de status van Ingesloten omgeving weergeven in het configuratiemenu voor 3D-weergaven, al ook extra parameters in het gedeelte Geavanceerd van het dialoogvenster voor configuratie voor het beheren van het fijn afstemmen:
- Straal De drempel voor de afstand van het berekenen van de Ingesloten omgeving
- Intensiteit: De sterkte die het effect zou moeten hebben (hogere waarden maken dingen donkerder)
- Drempel insluiting: Aantal nabijgelegen punten die moeten worden ingesloten om het effect weer te geven (waarden lager dan 50% zullen de uitvoer donkerder maken, maar mogelijk een groter bereik van insluiting geven)

![image12](images/entries/996b020346252bc10d87279d9e0cac766802c1d4.webp)

This feature was developed by [Martin Dobias & Belgacem Nedjima](https://github.com/wonder-sk)
## Puntenwolken
### Mogelijkheid: Exporteren van lagen van puntenwolken
Lagen van puntenwolken ondersteunen nu dat zij worden geëxporteerd naar indelingen voor vector of gegevens voor puntenwolken, met optioneel filteren.

Ondersteunde indelingen omvatten:
- Tijdelijke tekenlaag (geheugenlaag)
- GeoPackage
- Shapefile
- DXF
- LAZ (requires build WITH_PDAL)
- Niet-gecomprimeerde LAS-bestanden

Bewerkingen voor exporteren ondersteunen filteren op:
- Bereik
- Filteren op bereik Z
- Beperken van het aantal te exporteren punten
- Ruimtelijk filteren op polygoonlaag

Aanvullend worden ook de definitie van het CRS voor uitvoer en opnieuw projecteren ondersteund.

![image13](images/entries/9b7102f1bbd9286c16285a43158904395e56c4bc.webp)

Dit werd mogelijk gemaakt door de Staat Vorarlberg en de Zwitserse QGIS gebruikersgroep.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Eye Dome Lighting voor puntenwolken in 2D-kaartvenster
Het effect Eye dome lighting (EDL) is nu beschikbaar voor puntenwolken in 2D-renderers

![image14](images/entries/99c16bf2efe3bdcf020a41ad088e29ec7437573e.webp)

This feature was developed by [Nedjima Belgacem](https://github.com/NEDJIMAbelgacem)
## Afdruklay-outs
### Feature: Add FORCE_RASTER and IMAGE_COMPRESSION parameters to PDF algorithms
The `FORCE_RASTER` and `IMAGE_COMPRESSION` parameters have been added to the various \"Export print layout as PDF\" algorithms, including support for Atlas and multifile exports.

`FORCE_RASTER` is mutually exclusive with and takes precedence over the `FORCE_VECTOR` parameter.

![image15](images/entries/06cc045f6a69f9caaacde8f8b3ead9e89f02af22.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Expressies
### Mogelijkheid: Nieuw formulier voor variabelen van huidige functie van expressies van het huidige object toegevoegd
Dit nieuwe stijl formulier voor variabelen is toegevoegd voor het verwijzen naar het huidige object en de attributen ervan in expressies.

De nieuw geïntroduceerde variabelen zijn:
- `@feature`: a replacement for \$currentfeature, contains the current feature
- `@id`: a replacement for \$id, contains the current feature id
- `@geometry`: a replacement for \$geometry, contains the current feature geometry

This is a step towards eventually deprecating the older `$` style functions, and providing a more consistent approach to expressions instead of an unpredictable mix of `@`/`$`.

Oudere functies en verwijzingen naar variabelen zullen blijven werken (en zullen waarschijnlijk oneindig blijven werken in verband met de compatibiliteit met oudere projecten). Zij zullen ook (voorlopig) worden weergegeven in de gebruikersinterface om verwarring voor de gebruikers te voorkomen.

![image16](images/entries/b9666dee9322ba767162310e6958503e639d1148.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add new shared_paths function
A new `shared_paths` function has been added which returns a collection containing paths shared by the two input geometries. Those going in the same direction are in the first element of the collection, and those going in the opposite direction are in the second element. The paths themselves are given in the direction of the first geometry.

![image17](images/entries/f02946a8f1e45527366c30e6d0ea5a4947c7f86a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Make_valid and geom_to_array functions
Aanvullende functies zijn toegevoegd voor:
- `make_valid`: Repair broken input geometries and returns the corrected geometries
- `geometries_to_array`: This converts a geometry collection into an array for easier handling and iteration

![image18](images/entries/bc2bbd8d26e2ebb4fd7dc02f0ce7ec6460f3a3bc.webp)

This feature was developed by [Alex](https://github.com/roya0045)
### Mogelijkheid: Functie Holle schil
A new `concave_hull` function is now available in QGIS expressions (GEOS 3.11+)

![image19](images/entries/e434b7356dc93f9c43fa3142c7f8f914a4aa5615.webp)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Vragen naar bevestiging bij annuleren van wijzigingen in expressies
A new confirmation dialog is now safeguarding users against accidentally discarding their unapplied changes in expression editor dialogs. This safeguard is used in the Expression String Builder, the Expression Dialog (Epsilon icon, e. g. for Geometry Generators or for Pre-calculated Values in the model builder) and the Expression Based Filter (Attribute Table -\> Advanced filter expression).

![image36](images/entries/cebe844ae2c28045a8b6e2e89cb2b40cdbbd38c6.webp)

This feature was funded by [WhereGroup GmbH](https://wheregroup.com/)

This feature was developed by [Johannes Kröger](https://github.com/kannes)
## Gegevensbeheer
### Mogelijkheid: Vragen naar bevestiging bij verwijderen van objecten
Een nieuw dialoogvenster voor bevestiging verschijnt als gebruikers proberen een actie uit te voeren die records zou verwijderen, zoals het gebruiken van de toets DEL of acties op werkbalken om het risico van per ongeluk verwijderde objecten nog verder te beperken. Aanvullend is de telling van het aantal objecten nu opgenomen in het bericht van het dialoogvenster zelf (en wordt ook nog steeds weergegeven in de titelbalk), wat het totale aantal verwijderde objecten duidelijker maakt voor de gebruikers.

In previous releases, similar confirmation prompts would only be displayed when some features fell out of the extent of the map canvas, or the deletion triggered the removal of child relation features. The new behavior is for the prompt to be enabled by default and disabled by using the \"Don\'t show this message again\" checkbox.

![image20](images/entries/677952561ec24d417a74cf46842a6c52aec49587.webp)

This feature was funded by [QGIS user group Switzerland](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Metadata en Metasearch
### Mogelijkheid: Zoeken en opslaan van metadata van de gegevensprovider van de laag
Implementation of elements from the [QEP #250 \"Database metadata storage\"](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/250) initiative have been completed and this functionality includes the creation of a new layer metadata API and GUI components.

De volgende gegevensproviders/indelingen worden ondersteund voor het opslaan en beheren van metatdata van de laag in QGIS:
- GPKG (was al geïmplementeerd, ik verpakte hem slechts in de nieuwe API)
- Postgres
- Postgres Raster

In aanvulling daarop is een tab Zoeken voor metadata van de laag beschikbaar in Databronnen beheren, en een interactieve zoekactie voor metadata van de laag beschikbaar met de Locatiebalk van QGIS.

![image21](images/entries/17fc26636b3c1fe423ec8f715e69365495519add.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Processing
### Mogelijkheid: Ondersteuning voor vaste precisie voor gereedschap van Processing voor selecteren
A new advanced parameter is available for some processing tools which allows the use of the [fixed precision](https://blog.cleverelephant.ca/2020/12/waiting-postgis-31-3.html#fixed-precision-overlay) parameter provided by GEOS \>= 3.9.0. This parameter is listed under advanced parameters as \"Grid Size\" and is currently supported in the following tools:
- Overlapping
- Kruising
- Verschil
- Symmetrisch verschil
- Verenigen

![image22](images/entries/b2ef315dc1013852d3316023c62af5ff06626e93.webp)

Dit werd mogelijk gemaakt door Orange Telecom FR

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: Improved \"Make Valid\" Algorithms
QGIS kan nu de nieuwere verfijnde methoden voor GEOS 3.10+ gebruiken voor valideren en repareren van objecten geometrie.

![image23](images/entries/4b320e5bad078f1a0eb23fe958d86e330b08c10e.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Standaard optie om de telling voor vectoruitvoer vanuit Processing weer te geven
A new `Show feature count for output vector layers` setting is available (but disabled by default for performance reasons), which will automatically enable the \"show feature count\" option on output layers loaded from QGIS processing. This is able to give users a first glimpse of what to expect as an output from a Processing algorithm.

![image24](images/entries/e804b2accbcf155f4db2ea4024bd89ed5883097f.webp)

This feature was developed by [Germap](https://github.com/gacarrillor)
### Mogelijkheid: Optie voor het exporteren van relaties naar het algoritme voor verpakken van lagen
The \"Package Layers\" processing tool now supports optionally following project relations and exporting related tables following the hierarchy both upstream and downstream, whilst also taking selected features into account.

![image25](images/entries/26076b13de92a8ac2a1fea1511e03776c1aeae13.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add \"Offset\" parameter to \"Drape\" algorithms
Adds the \"Offset\" parameter to the \"Drape (set Z value from raster)\" and \"Set M value from raster\" algorithms. The \"Offset\" value is algebraically added to the band values after applying the \"Scale factor\".

![image26](images/entries/78e9cb5b82c872604fc3616c2c7b3772e7d26bef.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Opties voor toepassing en projecten
### Mogelijkheid: Aangepaste instellingen projectcoördinaat en weergave van richting
De opties voor Weergave Coördinaat en richting in de projecteigenschappen zijn bijgewerkt in lijn met het volgende:
- Kaarteenheden (gedrag is hetzelfde als in eerdere uitgaven)
- Geografische kaart (aangepast gedrag)
- Eenheden aangepaste projecties (nieuw type)

De oudere optie Geografische kaart (Latitude/ Longitude) zou waarden weergeven in de coördinaten van het CRS, *als* het CRS geografisch was, anders zou het waarden transformeren naar een hard-gecodeerde waarde in CRS WGS84.

The updated Map Geographic (degrees) option, which supersedes the legacy approach, will display values in the map CRS coordinates *if* the CRS is geographic, however in instances where it is not, the internal `QgsCoordinateReferenceSystem::toGeographicCrs()` API will be used to transform the coordinates into the map CRS\' associated geographic CRS. This is helpful in various contexts, such as when analyzing non-earth celestial bodies.

Het type Eenheden aangepaste projecties is een nieuwe aanvulling die standaard terugvalt op WGS84 en gebruikers in staat stelt elke CRS dat zij willen in te stellen om de coördinaten weer te geven.

![image27](images/entries/7af6704f72373fec3c1e9c212366fd3d8cfa0218.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add support for \"user\" fonts, and automatic downloading of freely licensed fonts
A new \"Fonts\" panel has been added to the settings dialog, which provides support for the following functionalities:
- The ability for users to populate a list of automatic font replacements to apply when loading projects or styles, allowing better support for projects and styles to be used across different operating systems (e.g. replace \"Arial\" with \"Helvetica\").
- Users can now place TTF or OTF fonts in the \"fonts\" subfolder of their user profile. These fonts will automatically be loaded at QGIS startup time. This provides a way for users to use fonts without requiring them to be installed on an operating system level, which is often blocked in enterprise environments. The Fonts setting panel lists all installed user fonts and allows users to manage (i.e. remove) previously installed user fonts
- Een API wordt verschaft voor andere gereedschappen, zoals plug-ins en andere cliënten, om aanvullende mappen voor lettertypen van gebruikers te specificeren, die zouden moeten worden gescand bij het opstarten van QGIS
- Automatic downloading of missing fonts is now supported in certain circumstances. If a user opens a project or style, or they try to load a vector tile layer that references fonts that aren\'t currently available, then a hard-coded list of freely licensed fonts to download via URL is consulted to determine whether it\'s possible to automatically download the font to the user font directory (and notify the user of the font license). A setting to opt out of this behavior is provided in the Fonts panel if so desired.

![image28](images/entries/77e17395ccb70e466ad4c5a80675ad0ff8ec070e.gif)

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Browser
### Mogelijkheid: Implementeren van het ontdekken van relaties voor lagen van OGR, en relatens weergeven in browser
De mogelijkheid Project Eigenschappen → Relaties → Relaties ontdekken is nu in staat lagen van OGR te ondersteunen die relaties ondersteunen, zoals GeoPackage (via de uitbreiding van de gerelateerde tabellen) en ESRI FileGeodatabases.

Het paneel QGIS Browser bevat nu de mogelijkheid om gedetailleerde informatie voor de relaties van deze databronnen weer te geven.

![image29](images/entries/11c3f493eff806b4eccbf9af27c96894ea3223a3.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aangepaste UX voor het maken van Geopackage en ESRI File Geodatabase
A \"New ESRI File Geodatabase\" action has been added to the QGIS Browser right-click context menu on directories, and a new \"vacuum\" action is available for GDB files. (requires GDAL 3.6+)

Aanvullend zal het maken van een nieuwe Geopackage vanuit hetzelfde menu nu onmiddellijk een lege GPKG maken, in plaats van het oudere standaard gedrag van het openen van een dialoogvenster voor het maken van een tabel (en het maken van een tabel te vereisen of gebruikers dummy gegevens in te laten voeren).

<https://user-images.githubusercontent.com/1829991/178902332-0e112e73-0140-45b9-84bf-fc7875cb7b98.gif>

![image30](images/entries/7a0e8f73e24aa061244e30d6bf1b8154e5eebce4.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Toestaan van verslepen van vectorlagen naar niet-GPKG OGR database-gegevenssets
QGIS staat nu het slepen en neerzetten van vectorlagen toe tussen OGR-database-gegevenssets die niet zijn opgeslagen in de indeling GPKG. Bijvoorbeeld het slepen van een laag op een GDB om die gegevensset te importeren in de geodatabase

![image31](images/entries/c1c17d31db79a4beaab864daf13257e6e7ed0ba0.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Beheren van velddomein weergeven voor niet-gpkg OGR-bronnen
De QGIS Browser ondersteunt nu meer geavanceerde functionaliteiten voor databases van OGR die niet in de indeling GPKG zijn, inclusief mogelijkheden voor het Beheren van velddomeinen (maken en vermelden van domeinen) en het maken van tabellen. Dit betekent dat gebruikers velddomeinen kunnen beheren en nieuwe tabellen kunnen maken in een bestaande ESRI FileGeodatabase-database vanuit de interface van QGIS Browser.

![image32](images/entries/cc1f815593c28352dffaad020061004db91f8ded.webp)

Dit werd mogelijk gemaakt door Provincie Gelderland

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Rol voor sessie definiëren voor verbindingen van PostgreSQL
A `session_role` setting can now be specified for PostgreSQL connections to set the user identifier of the active SQL session. Permissions checking for SQL commands are then carried out with the associated named role.

This is highly useful in instances where it is desirable to automatically give ownership of new objects (Tables/ Views/ Functions etc.) to the `session_role` group, and share ownership and the associated rights with all members of the `session_role` group.

The specified `session_role` must be a role that the current session user is a member of, or if the session user is a superuser, any role can be selected.

This feature was funded by [3liz](https://3liz.com/)

This feature was developed by [rldhont](https://github.com/rldhont)
### Mogelijkheid: Automatisch gerelateerde tabellen toevoegen bij het toevoegen van lagen uit GDAL-gegevenssets met ingebedde informatie over elaties
For GDAL data formats with embedded relationship information, whenever a table is added QGIS is now able to discover relationships and immediately add all the related tables to the current project (if they don\'t already exist). Additionally, when adding these related layers QGIS will automatically configure the corresponding QGIS relationships.

Dit werkt voor alle indelingen die de API voor relaties van GDAL ondersteunt, die omvat:
- Geopackage (via de uitbreiding van de gerelateerde tabellen)
- ESRI FileGDB/ OpenFileGDB
- ESRI Personal Geodatabase
- SQLite/ Spatialite-indelingen.

Deze mogelijkheid werd mogelijk gemaakt door de Universiteit van Uppsala

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning toegevoegd voor subset string-(filter) voor Arcgis REST-lagen
Dit kan de uitvoering op grote lagen **enorm** verbeteren!

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Abstracte database-provider voor hernoemen van velden
A `QgsAbstractDatabaseProviderConnection` interface has been added for supporting renaming fields, and implemented for OGR connections along with the ability to rename existing fields for supported database connections via the QGIS Browser interface.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: WFS uitvoeren van binaire ruimtelijke bewerkingen in expressies op de server
QGIS was in staat om de expressie-filters voor binaire ruimtelijk bewerkingen op de server uit te voeren als de geometrie werd opgegeven als WKT of in de indeling GML. Deze wijziging converteert de geometrie van een statische variabele in de expressie tot een filter voor OGC. De URL voor WFS wordt dan gemaakt door het combineren van een rechthoek van een begrenzingsvak, een filter voor de laag en de filter-expressie.

A feature request computes the expression in advance to find out if it can be performed on the server, then it\'s stored in `QgsBackgroundCachedSharedData` where a new download is triggered.

Wanneer een filter-verzoek geen puur binair ruimtelijke bewerking is, zal het niet worden geëvalueerd op de server.

Dit werd mogelijk gemaakt door Kanton Schaffhausen

This feature was developed by [signedav](https://github.com/signedav)
### Mogelijkheid: Bewerken van lagen van ArcGIS REST
QGIS ondersteunt nu het bewerken van lagen van ArcGIS feature server, zoals die welke door ArcGIS online worden gehost. Er van uitgaande dat de gebruiker de toepasselijke rechten zijn toegewezen voor het bewerken van een laag, zal het de mogelijkheid ontgrendelen om de eigen gereedschappen van QGIS om die laag te bewerken. Deze wijzigingen omvatten ondersteuning voor de volgende bewerkingen:
- Objecten verwijderen
- Nieuwe objecten toevoegen
- Curved geometries (only supported for enterprise ArcGIS server, as [ArcGIS online currently has no support for curves](https://support.esri.com/en/technical-article/000014684))
- Bestaande objecten bewerken
- Attributen aanpassen (velden maken, velden verwijderen, indexen voor attributen maken)

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch raster sublagen laden uit vectortegelstijlen
Bij het laden van een nieuwe bron voor vectortegels in een project, als de geassocieerde stijl van MapBox GL al enige raster sublaag bevat, laad deze dan ook in het project met geconverteerde stijlen.

Fixes <https://github.com/qgis/QGIS/issues/46593>

![Peek 2022-06-20 12-31](https://user-images.githubusercontent.com/1829991/174514930-77887a1d-4679-49a2-9ff0-7c360bc0fc01.gif)

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Individuele WMS-lagen toevoegen
In eerdere uitgaven zou de selectie van lagen uit WMS Servers in QGIS worden geladen als één enkele projectlaag. Deze nieuwe functionaliteit verschaft een optioneel keuzevak om elke van de geselecteerde WMS-lagenyers in QGIS te laden als afzonderlijke projectlagen.

![image34](images/entries/2685710315d58fc03e1557e3381a41fdd8eb5a02.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Mogelijkheid: Projecten opslaan naar Oracle Database Provider
QGIS ondersteunt nu het opslaan van projecten naar Oracle databases.

![image35](images/entries/6a575714dfc905211f3518a4f5f3803c32e8afa9.webp)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## QGIS Server
### Feature: QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS settings variable
Deze nieuwe mogelijkheid makt het mogelijk extra tokens te specificeren die zouden kunnen worden gebruikt voor een definitie van een WMS FILTER. De huidige lijst van geaccepteerde tokens is nogal klein en deze instelling stelt systeembeheerders in staat  de lijst van toegestane tokens eenvoudig uit te breiden.

Deze mogelijkheid werd mogelijk gemaakt door Zweckverband Grevesmühlen

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Lagen openen in modus Alleen lezen met QGIS Server
A new `QGIS_SERVER_FORCE_READONLY_LAYERS` environment variable to force QGIS Server to open layers in read-only mode.

Dit omvat verscheidene onderliggen wijzigingen aan de API om configuratie voor Alleen-lezen te ondersteunen voor constructie van de gegevensprovider, structuur van het project, en eigenschappen van de laag.

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [rldhont](https://github.com/rldhont)
## Plug-ins
### Mogelijkheid: Wijzigingen aan het gedrag voor het automatisch bijwerken van plug-ins
This change moves the old `app/plugin_installer/checkOnStart` setting key to a new `plugins/automatically-check-for-updates` key, and switches the default value to enable automatic checks.

Dit is ontworpen om alle bestaande gebruikers van QGIS te laten overschakelen naar het nieuwe gedrag voor het controleren van updates voor plug-ins bij het opstarten (tot een maximum van één maal elke 3 dagen).

Het is bedoeld om een betere ervaring met QGIS aan onze gebruikers te bieden, door alle gebruikers proactief te informeren wanneer plug-ins zouden moeten worden bijgewerkt, er voor zorgende dat ALLE gebruikers waarschijnlijk plug-ins upgraden en de reparaties voor problemen met plug-ins direct verkrijgen.

**Zakelijke gebruikers die deze instelling hebben aangepast in hun systemen zullen hun scripts moeten aanpassen naar de nieuwe sleutel voor de instelling.**

Aanvullend is de optie om het aantal dagen te beheren tussen de controles voor plug-ins bij opstarten verwijderd en is hard gecodeerd op 3 dagen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Programmeerbaarheid
### Mogelijkheid: AfhandelingTijdbeheer van kaarten in QGIS Quick toegevoegd
A new implementation has been added to allow the Canvas and Map Settings in [QGIS Quick](https://api.qgis.org/api/qgsquick.html) to handle temporal functionality.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Aanvulling van de parameter voor de opdrachtregel py-args
When running QGIS from the command line with the `--code` parameter, a new `--py-args` utility allows the passing of arguments to the python interpreter.

Arguments between `--py-args` and `--` are passed to the python interpreter and ignored by QGIS, so for example, when using the following command:

    qgis --code /home/user/example.py --py-args --specialScriptArguments "arg1" 'arg2' -- layer1 layer2
    
The `example.py` script will have `--specialScriptArguments`, `arg1`, and `arg2` passed as system arguments to the python interpreter, whilst `layer1` and `layer2` will be handled by QGIS normally and loaded as map layers

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation Vorarlberg

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GetPrint request of Atlas Template doesn\'t respect Project scales | [#49900](https://github.com/qgis/QGIS/issues/49900) | [PR #50199](https://github.com/qgis/QGIS/pull/50199) | [PR #50214](https://github.com/qgis/QGIS/pull/50214) |
| Attribute Table Integer entries not showing due to window size | [#50181](https://github.com/qgis/QGIS/issues/50181) | [PR #50201](https://github.com/qgis/QGIS/pull/50201) | Niet aanbevolen |
| WFS3 collections field name/displayName mix in request/response | [#49399](https://github.com/qgis/QGIS/issues/49399) | [PR #50203](https://github.com/qgis/QGIS/pull/50203) | Niet aanbevolen |
| QGIS Server WMS GetFeatureInfo does not evaluate represent_value expression in maptip | [#30719](https://github.com/qgis/QGIS/issues/30719) | [PR #50216](https://github.com/qgis/QGIS/pull/50216) | [PR #50223](https://github.com/qgis/QGIS/pull/50223) |
| \"evaluate default value on providers side\" block insert on table in the schema with autoincrement | [#50168](https://github.com/qgis/QGIS/issues/50168) | [PR #50230](https://github.com/qgis/QGIS/pull/50230) | [PR #50333](https://github.com/qgis/QGIS/pull/50333) |
| QGIS not responding when entering page size using custom width or height fields | [#50104](https://github.com/qgis/QGIS/issues/50104) | Kan niet worden gereproduceerd |  |
| \"Add Directory\...\" inputs files from previous selected directory at first instance, then the corret. | [#50055](https://github.com/qgis/QGIS/issues/50055) | [PR #50232](https://github.com/qgis/QGIS/pull/50232) | [PR #50241](https://github.com/qgis/QGIS/pull/50241) |
| Layer style panel and Layer panel do not show same visibility settings for layer style | [#49998](https://github.com/qgis/QGIS/issues/49998) | Kan niet worden gereproduceerd |  |
| Crash while opening Options dialog after switching locale | [#50239](https://github.com/qgis/QGIS/issues/50239)9 | [PR #50263](https://github.com/qgis/QGIS/pull/50263) | Niet nodig |
| unreported MSSQL connections API error | Niet gerapporteerd | [PR #50194](https://github.com/qgis/QGIS/pull/50194) | [PR #50454](https://github.com/qgis/QGIS/pull/50454) |
| Identify and select tools don\'t work with geometry-based query layers | [#50242](https://github.com/qgis/QGIS/issues/50242) | Kan niet worden gereproduceerd |  |
| Problem with Reloading SLD file in QGIS | [#50152](https://github.com/qgis/QGIS/issues/50152) | [PR #50266](https://github.com/qgis/QGIS/pull/50266) | Wachtrij |
| Unreported endless alg splitwithlines | Niet gerapporteerd | [PR #50279](https://github.com/qgis/QGIS/pull/50279) | Niet aanbevolen |
| Processing algorithm \"Split with lines\" does not split polygon | [#50227](https://github.com/qgis/QGIS/issues/50227) | Is geen probleem |  |
| Expression do not split string in multiple lines | [#49666](https://github.com/qgis/QGIS/issues/49666) | [PR #50295](https://github.com/qgis/QGIS/pull/50295) | [PR #50455](https://github.com/qgis/QGIS/pull/50455) |
| Problem with exportation of complex SLD | [#42348](https://github.com/qgis/QGIS/issues/42348) | [PR #50342](https://github.com/qgis/QGIS/pull/50342) | [PR #50354](https://github.com/qgis/QGIS/pull/50354) |
| Wrong interpretation of SLD color opacity | [#44657](https://github.com/qgis/QGIS/issues/44657) | Is geen probleem |  |
| Wrong label size for SLD export/import | [#35561](https://github.com/qgis/QGIS/issues/35561) | [PR #50347](https://github.com/qgis/QGIS/pull/50347) | Niet nodig |
| Exporting SLD doesnt include fill-opacity | [#33376](https://github.com/qgis/QGIS/issues/33376) | [PR #50349](https://github.com/qgis/QGIS/pull/50349) | [PR #50436](https://github.com/qgis/QGIS/pull/50436) |
| SpatiaLite - Added feature vanishes, attribute dialog does not show required fields | [#50523](https://github.com/qgis/QGIS/issues/50523) | [PR #50573](https://github.com/qgis/QGIS/pull/50573) | Wachtrij |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Niet van toepassing |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Niet nodig |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Niet gerapporteerd | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Niet van toepassing |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Niet gerapporteerd | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Niet nodig |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328)Bug Title |
| \-- | \-- | \-- | \-- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Niet van toepassing |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Niet nodig |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Niet gerapporteerd | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Niet van toepassing |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Niet gerapporteerd | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Niet nodig |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS not retrieving sequence from postgis in 3.26 | [#49463](https://github.com/qgis/QGIS/issues/49463) | [PR #50247](https://github.com/qgis/QGIS/pull/50247) | niet noodzakelijk to bp |
| SVG is not rendered for SVG Marker symbol | [#50208](https://github.com/qgis/QGIS/issues/50208) | Kan niet gerepareerd worden, Probleem van Qt |  |
| If \"estimated metadata\" option is checked, feature count for tables/postgis do not work | [#46790](https://github.com/qgis/QGIS/issues/46790) | [PR #50256](https://github.com/qgis/QGIS/pull/50256) | [PR #50425](https://github.com/qgis/QGIS/pull/50425) |
| Variable raster image source in composer not working | [#47981](https://github.com/qgis/QGIS/issues/47981) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Print Layout Picture Box reverting to SVG | [#38031](https://github.com/qgis/QGIS/issues/38031) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Layout picture can not change SVG image to Raster image | [#37804](https://github.com/qgis/QGIS/issues/37804) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| QgsOptionsPageWidget - helpKey and helpSearchPath are not working | [#49421](https://github.com/qgis/QGIS/issues/49421) | [PR #50282](https://github.com/qgis/QGIS/pull/50282) | [PR #50330](https://github.com/qgis/QGIS/pull/50330) |
| Freeze when opening WFS attribute table from HTTPS server with SSL exception | [#42615](https://github.com/qgis/QGIS/issues/42615) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | geen bp |
| News feed not loading when using MSI installer | [#49097](https://github.com/qgis/QGIS/issues/49097) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | geen bp |
| .ci/run_tests.sh: test_core_networkaccessmanager (Timeout) | [#50234](https://github.com/qgis/QGIS/issues/50234) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) |  |
| SVG Symbol on newer version of QGIS (3.22.7/8/10 tested) make the software lag a lot (and not on 3.4 version). | [#49818](https://github.com/qgis/QGIS/issues/49818) | Feedback, not sure it's a bug |  |
| Empty Options drop-down menu in Query Logger tab | [#50403](https://github.com/qgis/QGIS/issues/50403) | [PR #50527](https://github.com/qgis/QGIS/pull/50527) | geen bp |
| Build fails with WITH_POSTGRESQL=OFF | [#50075](https://github.com/qgis/QGIS/issues/50075) | Terugkoppeling |  |
| Build fails with WITH_GSL=OFF | [#50076](https://github.com/qgis/QGIS/issues/50076) | [PR #50555](https://github.com/qgis/QGIS/pull/50555) |  |
| QGIS master exports out of bounds in layout | [#48624](https://github.com/qgis/QGIS/issues/48624) | Kan niet gerepareerd worden, Probleem van Qt |  |
| Layout bleeding to edge outside map window | [#49638](https://github.com/qgis/QGIS/issues/49638) | Kan niet gerepareerd worden, Probleem van Qt |  |
| Freeze with virtual field on \$area used as parameter in sum | [#49589](https://github.com/qgis/QGIS/issues/49589) | [PR #50533](https://github.com/qgis/QGIS/pull/50533) | [PR #50565](https://github.com/qgis/QGIS/pull/50565) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server WFS 1.1.0 GetFeature response - properties with xsi:nil=\"true\" | [#45243](https://github.com/qgis/QGIS/issues/45243) | [PR #50495](https://github.com/qgis/QGIS/pull/50495) |  |
| Cannot move labels | [#47542](https://github.com/qgis/QGIS/issues/47542) | Kan niet worden gereproduceerd |  |
| Auxiliary storage and removed layers | [#44667](https://github.com/qgis/QGIS/issues/44667) | [PR #50479](https://github.com/qgis/QGIS/pull/50479) | Niet aanbevolen |
| OPACITIES parameter not handled with Vector Tile layer in GetMap/GetPrint | [#50364](https://github.com/qgis/QGIS/issues/50364) | [PR #50374](https://github.com/qgis/QGIS/pull/50374) | [PR #50539](https://github.com/qgis/QGIS/pull/50539) |
| Fixes log messages when a job error is not related to a specific layer | Niet gerapporteerd | [PR #50372](https://github.com/qgis/QGIS/pull/50372) | Niet nodig |
| Labels: Data defined override of \"Show Label\" always wants the auxiliary storage option | [#47993](https://github.com/qgis/QGIS/issues/47993) | [PR #50496](https://github.com/qgis/QGIS/pull/50496) | [PR #50538](https://github.com/qgis/QGIS/pull/50538) |
| Auxiliary storage rotation or offset fields for symbols are visible by default while labels are not | [#28548](https://github.com/qgis/QGIS/issues/28548) | [PR #50498](https://github.com/qgis/QGIS/pull/50498) |  |
| Improve selection of PostGIS raster overviews | Niet gerapporteerd | [PR #50554](https://github.com/qgis/QGIS/pull/50554) | [PR #50575](https://github.com/qgis/QGIS/pull/50575) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere](https://hytech-imaging.fr/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with offline-editing-core-plugin converting to offline project layer with empty polygon | [#50466](https://github.com/qgis/QGIS/issues/50466) | [PR #50577](https://github.com/qgis/QGIS/pull/50577) |  |
| Cleanup temporary python test config path when requested | [#48884](https://github.com/qgis/QGIS/issues/48884) | [PR #50608](https://github.com/qgis/QGIS/pull/50608) |  |
| Include type name in message about unsupported qfield validations | Niet gerapporteerd | [PR #50589](https://github.com/qgis/QGIS/pull/50589) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix regression in column break calculations in legends | [#42672](https://github.com/qgis/QGIS/issues/42672) | [PR #50597](https://github.com/qgis/QGIS/pull/50597) | Not suitable \-- too risky |
| Fix tracing fails when layer crs differs from map crs | [#49247](https://github.com/qgis/QGIS/issues/49247) | [PR #50612](https://github.com/qgis/QGIS/pull/50612) | Niet vereist |
| Show only available CRS in WMS layer selection widget | [#45918](https://github.com/qgis/QGIS/issues/45918) | [PR #50572](https://github.com/qgis/QGIS/pull/50572) | Niet vereist |
| Fix some overlay algorithms output multipoint geometries but output layer is single point, causing insertion errors | [#49456](https://github.com/qgis/QGIS/issues/49456) | [PR #50567](https://github.com/qgis/QGIS/pull/50567) | [PR #50641](https://github.com/qgis/QGIS/pull/50641) |
| Fix missing information in crash reports on Windows | [#50472](https://github.com/qgis/QGIS/issues/50472) | [PR #50595](https://github.com/qgis/QGIS/pull/50595) | Niet vereist |
| Fix regression where attribute table dialogs do not open as proper top level windows with their own taskbar entries | [#49286](https://github.com/qgis/QGIS/issues/49286) | [PR #50594](https://github.com/qgis/QGIS/pull/50594) | Niet vereist |
| \[georeferencer\] Fix options ignored when \"create world file only\" is active | [#49331](https://github.com/qgis/QGIS/issues/49331) | [PR #50566](https://github.com/qgis/QGIS/pull/50566) | Niet vereist |
| Ensure identify tool uses correct labels for x/y values when coordinate axis order for project is y/x | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Niet vereist |
| Ensure coordinate display in status bar updates immediately when related settings change, and update the tooltip to match the actual values displayed in the widget | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Niet vereist |
| Fix rendering of linestrings with nan z values | [#50510](https://github.com/qgis/QGIS/issues/50510) | [PR #50549](https://github.com/qgis/QGIS/pull/50549) | Niet vereist |
| Fix broken logic in clearing python console history | Niet gerapporteerd | [PR #50504](https://github.com/qgis/QGIS/pull/50504) | [PR #50515](https://github.com/qgis/QGIS/pull/50515) |
| Fix QgsFileWidget does not reactivate widget\'s window after selecting a file/folder via the browse button on mac | Niet gerapporteerd | [PR #50501](https://github.com/qgis/QGIS/pull/50501) | [PR #50502](https://github.com/qgis/QGIS/pull/50502) |
| Fix code folding not shown for non-python code editor classes | Niet gerapporteerd | [PR #50492](https://github.com/qgis/QGIS/pull/50492) |  |
| Fix leak in GEOS geometry library use | Niet gerapporteerd | [PR #50379](https://github.com/qgis/QGIS/pull/50379) |  |
| Fix raster contour renderer ignores opacity setting | [#41663](https://github.com/qgis/QGIS/issues/41663) | [PR #50382](https://github.com/qgis/QGIS/pull/50382) | Not suitable \-- too risky |
| Fix truncation of recent project list removes too many items, raises a warning | Niet gerapporteerd | [PR #50394](https://github.com/qgis/QGIS/pull/50394) | [PR #50397](https://github.com/qgis/QGIS/pull/50397) |
| Fix dizzy easter egg | [#50345](https://github.com/qgis/QGIS/issues/50345) | [PR #50380](https://github.com/qgis/QGIS/pull/50380) | Niet vereist |
| Fix point pattern fill sometimes ignores symbol opacity setting | [#48031](https://github.com/qgis/QGIS/issues/48031) | [PR #50384](https://github.com/qgis/QGIS/pull/50384) | Not suitable \-- too risky |
| Fix broken path in svg raises Qt warnings while rendering | Niet gerapporteerd | [PR #50383](https://github.com/qgis/QGIS/pull/50383) |  |
| Ensure correct expression context is used when generating symbol preview icons | [#49106](https://github.com/qgis/QGIS/issues/49106) | [PR #50393](https://github.com/qgis/QGIS/pull/50393) | Not suitable \-- too risky |
| \[spatialite\] Fix corrupted default attribute values when fields are loaded using gaiaVectorLayer | Privé gerapporteerd | [PR #50360](https://github.com/qgis/QGIS/pull/50360) | [PR #50361](https://github.com/qgis/QGIS/pull/50361) |
| Fix handling of vector tiles when zoom level 0 is not available | [#47934](https://github.com/qgis/QGIS/issues/47934) | [PR #50337](https://github.com/qgis/QGIS/pull/50337) | Niet vereist |
| Fix drag and drop of files to georeferencer window | [#49175](https://github.com/qgis/QGIS/issues/49175) | [PR #50338](https://github.com/qgis/QGIS/pull/50338) | Niet vereist |
| Never try to handle base parameter type values as map layers in QgsProcessingParameterDefinition::valueAs\* methods | [#48598](https://github.com/qgis/QGIS/issues/48598) | [PR #50327](https://github.com/qgis/QGIS/pull/50327) | Niet vereist |
| Avoid a redundant calculation of visible layer extent in overview canvas | Niet gerapporteerd | [PR #50329](https://github.com/qgis/QGIS/pull/50329) | [PR #50336](https://github.com/qgis/QGIS/pull/50336) |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Niet geschikt |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Niet geschikt |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix \"Add Ring\" tool doesn\'t consider all the overlapping features | [#23113](https://github.com/qgis/QGIS/issues/23113) | [#50447](https://github.com/qgis/QGIS/pull/50447) | Niet geschiky - voegy nieuwe methoden toe |
| Fix wkbType cast from OGR 25D Type | [#50218](https://github.com/qgis/QGIS/issues/50218) | [#50233](https://github.com/qgis/QGIS/pull/50233) | [#50251](https://github.com/qgis/QGIS/pull/50251) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)

{{<content-end >}}
