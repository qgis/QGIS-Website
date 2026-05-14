---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.14
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.14{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Datum uitgave 26-02-2016

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Long Term Release**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

Het doel van LTR-uitgaven is om een stabiel en minder vaak wijzigend platform te verschaffen voor bedrijven en organisaties die zich niet meer dan eenmaal per jaar willen bezighouden met het bijscholen van gebruikers, trainingsmateriaal etc.  Het succes van de LTR hangt heel veel van u, onze geliefde gebruikers, af, we hebben uw ondersteuning nodig om ons probleemoplossingen aan te reiken en er voor zorgend dat u in uw ondersteuningscontracten met verleners van ondersteuning specificeert dat probleemoplossingen die voor u worden toegepast ook worden toegepast op de tak van de LTR als ook op onze normale takken voor ontwikkeling.

Als een LTR belangrijk voor u is, overweeg dan ook directe ondersteuning voor het project QGIS, of moedig uw zakelijke dienstverlener aan om de LTR als basis te gebruiken voor uw zakelijke oplossing zodat iedereen kan profiteren van een stabiel platform dat doorlopend wordt verbeterd en verfijnd. Onthoud dat voor gebruikers en organisaties die graag de grenzen verkennen, onze viermaandelijkse uitgaven ongewijzigd door blijven gaan.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Dankwoord**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Huidige sponsoren van QGIS
{{<fund type="changelog" >}}
## Algemeen
### Mogelijkheid: Gedrag gewijzigd voor functie strpos
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Projectbestanden uit eerdere versies van QGIS zullen moeten worden bijgewerkt om deze wijziging te kunnen laten zien.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Zoomen naar object met klik met rechts in attributentabel
U kunt nu naar een object zoomen vanuit de attributentabel (zonder het eerst te moeten selecteren) door met rechts te klikken en te selecteren Naar object inzoomen.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Mogelijkheid: Verbeteringen voor snelheid en geheugen
- **Een set geselecteerde objecten opslaan** uit een grote laag is nu veel sneller
- Alleen geselecteerde objecten bijwerken met behulp van het **veldberekening** is sneller
- **Sneller zoomen** naar geselecteerde in grote lagen
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **De categorieën in een renderer Categorieën filteren** (bijv. alleen enkele categorieën weergeven en andere niet selecteren) is veel sneller, omdat nu alleen de overeenkomende objecten worden opgehaald van de gegevensprovider
- Significante **reductie in het geheugen** vereist voor het openen van grote vectorlagen

### Mogelijkheid: Meer variabelen in expressies
Tijdens renderen zullen nieuwe variabelen beschikbaar zijn:
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Deze zijn nuttig om verschillende stijlen toe te passen op verschillende delen van meerdelige objecten:
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

Variabelen die een relatie hebben met de omgeving van het besturingssysteem zijn ook toegevoegd:
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

deze mogelijkheid werd mogelijk gemaakt door Andreas Neumann (de OS- en gebruikergerelateerde variabelen)

Deze mogelijkheid werd ontwikkeld door Nyall Dawson, Matthias Kuhn
### Mogelijkheid: Meer controle over plaatsing van kaartelementen
QGIS 2.14 heeft een betere controle verkregen voor het plaatsen van Noordpijlen, schaalbalken en opmerkingen voor auteursrecht in het hoofdkaartvenster. U kunt nu precies de positie van deze elementen instellen met behulp van een variëteit aan eenheden (inclusief millimeters, pixels en percentage).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Feature: Programma voor oplossen van problemen tegen betaling
Voorafgaande aan elke uitgave houden we een programma voor het oplossen van problemen tegen betaling waar we ontwikkelaars de fondsen verstrekken om zoveel mogelijk problemen op te lossen. We hebben besloten om een verantwoording van dit programma voor het oplossen van problemen tegen betaling op te nemen als deel van ons log van wijzigingen. Onthoud dat deze lijst **niet uitputtend** is.
- Sandro Santilli: [Postgis Connection freeze if you press \"Set filter\" during loading of data](http://hub.qgis.org/issues/13141)
- Sandro Santilli: [db_manager is unable to load rasters from connections with no dbname specified](http://hub.qgis.org/issues/10600)
- Sandro Santilli: [Plugin layers do not work correctly with rotation](http://hub.qgis.org/issues/11900)
- Sandro Santilli: Crash in QgsGeomColumnTypeThread stopping connection scan [#14140](http://hub.qgis.org/issues/14140) [#13806](http://hub.qgis.org/issues/13806)
- Sandro Santilli: [Crash after bulk change of attribute value in shapefile](http://hub.qgis.org/issues/11422)
- Sandro Santilli: [KMZ causes QGIS application crash (Mac)](http://hub.qgis.org/issues/13865)
- Sandro Santilli: [QGIS 2.8.1 crash opening FileGDB (openGDB-Driver)](http://hub.qgis.org/issues/12416)
- Sandro Santilli: [QGIS crashes when removing vertex of a multipart geometry](http://hub.qgis.org/issues/14188)
- Sandro Santilli: [test -V -R qgis_analyzertest segfaults](http://hub.qgis.org/issues/14176)
- Sandro Santilli: [output/bin/qgis_diagramtest segfaults](http://hub.qgis.org/issues/14212)
- Sandro Santilli: Overflow on primary key with negative values; crashes QGIS when editing [#13958](http://hub.qgis.org/issues/13958) [#14262](http://hub.qgis.org/issues/14262)
- Sandro Santilli: [PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Sandro Santilli: [TestVectorLayerJoinBuffer hangs if database is not available](http://hub.qgis.org/issues/14308)
- Nyall Dawson: [BLOCKER: Crash when opening layer properties dialog for geometryless vector layer](http://hub.qgis.org/issues/14116)
- Nyall Dawson: Broken server side filtering for OGR, Oracle and Spatialite layers
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: Fix issues with conversion of renderers to rule based renderer resulting in broken renderer
- Nyall Dawson: Fix categorised renderer does not store changes to the source symbol
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: Fix handling of time value in attributes
- Nyall Dawson: Dialog tab order fixes
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Correctly handle LongLong fields in merge attribute dialog
- Nyall Dawson: Fix misleading display of calculation details in measure tool dialog (was misleading and inaccurate for many CRS/unit combinations)
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias: raster layer drawn as garbage
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias: Slow loading of attribute table in debug mode
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias: 2.5d renderer fixes
- Martin Dobias: [HIGH: Long freeze when initializing snapping](http://hub.qgis.org/issues/12578)
- Martin Dobias: [NORMAL: Loading of data-defined from xml](http://hub.qgis.org/issues/14177)
- Martin Dobias: Fix DB manager to work with SpatiaLite \< 4.2
- Martin Dobias: [NORMAL: Crash while rendering in debug mode](http://hub.qgis.org/issues/14369)
- Martin Dobias: BLOCKER: Fix selection / identification in spatialite views [#14232](http://hub.qgis.org/issues/14232) [#14233](http://hub.qgis.org/issues/14233)
- Martin Dobias: [BLOCKER: Fix drag&drop of spatialite tables](http://hub.qgis.org/issues/14237)
- Jürgen Fischer:[Zoom to layer works incorrectly while layer editing](http://hub.qgis.org/issues/3155)
- Jürgen Fischer:[Help viewer process running in the background with no help viewer (or even QGIS) open](http://hub.qgis.org/issues/8305)
- Jürgen Fischer:[Spatialindex include path missing in some components](http://hub.qgis.org/issues/13197)
- Jürgen Fischer:[compile fails attempting to generate qgsversion.h](http://hub.qgis.org/issues/13680)
- Jürgen Fischer:[Edit widget configuration is stored twice](http://hub.qgis.org/issues/13960)
- Jürgen Fischer:[Extra space in \"IS NOT\" operator makes the expression return wrong selection](http://hub.qgis.org/issues/13938)
- Jürgen Fischer:[QGIS greadily allocates memory and crashes when editing moderately large shapefiles with the node tool](http://hub.qgis.org/issues/13963)
- Jürgen Fischer:[French reprojection use ntf_r93.gsb (IGNF:LAMBE etc ..)](http://hub.qgis.org/issues/14101)
- Jürgen Fischer:[Digitizing: \"Reuse last entered attribute values\" should not overwrite primary key column](http://hub.qgis.org/issues/14154)
- Jürgen Fischer:[Issues in Case expression description](http://hub.qgis.org/issues/14189)
- Jürgen Fischer:[shapefile vector writer: datetime field saved as date resulting in data loss of time](http://hub.qgis.org/issues/14190)
- Jürgen Fischer:[Add help for some variable functions](http://hub.qgis.org/issues/14259)
- Jürgen Fischer:[Virtual layers not working in Processing](http://hub.qgis.org/issues/14313)
- Jürgen Fischer:[layer definition file load error](http://hub.qgis.org/issues/14340)
- Jürgen Fischer:[QgsGeometry::fromWkb fails if WKB is different endian representation](http://hub.qgis.org/issues/14204)
- Jürgen Fischer:[Debian build failure.](http://hub.qgis.org/issues/14248)
- Jürgen Fischer:[PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Jürgen Fischer:[wkb access out of bounds](http://hub.qgis.org/issues/14315)
- Jürgen Fischer:[QGIS under Windows netCDF import reverses Y axis, Linux doesn\'t](http://hub.qgis.org/issues/14316) [OSGeo4W #483](https://trac.osgeo.org/osgeo4w/ticket/483)
- Jürgen Fischer:[OSGEO4W: Running offline install crashes installer](https://trac.osgeo.org/osgeo4w/ticket/105)
- Jürgen Fischer:[OSGEO4W: Dependencies are not tracking on Windows Server 2003 x64](https://trac.osgeo.org/osgeo4w/ticket/117)
- Jürgen Fischer:[OSGEO4W: installation from local package don\'t check the dependencies](https://trac.osgeo.org/osgeo4w/ticket/151)
- Jürgen Fischer:[OSGEO4W: Setup starts downloading and installing packages before showing you a list to choose from](https://trac.osgeo.org/osgeo4w/ticket/262)
- Jürgen Fischer:[OSGEO4W: Using -a for Advanced selects two options (command line install)](https://trac.osgeo.org/osgeo4w/ticket/351)
- Jürgen Fischer:[OSGEO4W: Infinite license download during quite installation of szip](https://trac.osgeo.org/osgeo4w/ticket/486)
- Jürgen Fischer:Oracle provider deadlock
- Jürgen Fischer:fix saga path setting

### Feature: Field calculator can be used to update feature\'s geometry
De Veldberekening kan u worden gebruikt om de geometrie van geometrieën van objecten bij te werken met behulp van het resultaat van een geometrische expressie. Dit is een handige sneltoets om bewerkingen, zoals het toevoegen van een buffer aan groep geselecteerde objecten, uit te voeren en samen met alle nieuw toegevoegde functies voor geometrie in 2.14 is het een zeer handige manier om uw geometrieën te manipuleren!

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Nieuwe functies voor expressies in 2.14
Vele nieuwe functies voor expressies zijn toegevoegd aan versie 2.14:
- `relate`: performs a DE-9IM geometry relation by either returning the DE-9IM representation of the relationship between two geometries, or by testing whether the DE-9IM relationship matches a specified pattern.
- the `make_point` function now accepts optional z and m values, and a new `make_point_m` function has been added for creation of PointM geometries.
- `m` and `z` functions for retrieving the m and z values from a point geometry
- new `make_line` and `make_polygon` functions, for creation of line and polygon geometries from a set of points
- `reverse`, for reversing linestrings
- `eval` function, which can evaluate a string as though it is an expression of its own
- `translate` function, for translating geometries by an x/y offset
- `darker` and `lighter` functions, which take a color argument and make it darker or lighter by a specified amount
- `radians` and `degrees`: for converting angles between radians and degrees
- `point_on_surface`: returns a point on the surface of a geometry
- `exterior_ring`: returns the exterior ring for a polygon geometry
- `is_closed`: returns true if a linestring is closed
- new geometry accessor functions: `geometry_n` (returns a specific geometry from within a collection), `interior_ring_n` (returns an interior ring from within a polygon)
- `num_geometries`: returns number of geometries inside a collection
- `num_rings`: returns number of rings in a polygon geometry object
- `num_interior_rings`: returns number of interior rings in a polygon
- `nodes_to_points`, for converting every node in a geometry to a multipoint geometry
- `segments_to_lines`, for converting every segment in a geometry to a multiline geometry
- `closest_point`: returns closest point in a geometry to a second geometry
- `shortest_line`: returns the shortest possible line joining two geometries

`nodes_to_points` and `segments_to_lines` are intended for use with geometry generator symbology, eg to allow use of m and z values for nodes/lines with data defined symbology.

Andere verbeteringen:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Analyse-gereedschappen
### Mogelijkheid: Meer statistieken beschikbaar in Gereedschap Attributen samenvoegen
Bij het gebruiken van ofwel de gereedschappen Attributenwaarden samenvoegen of Objecten samenvoegen, zijn er aanvullende overzichtsstatistieken beschikbaar die kunnen worden gebruikt om de resulterende attribuutwaarden in te stellen. Deze omvatten Q1, Q3, inter-kwartiel bereiken, waarden Meerderheid en Minderheid, en, naast andere, het anatal unieke waarden.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Waarden Z/M worden weergegeven bij het gebruiken van het gereedschap Objecten identificeren
Het gereedschap Objecten identificeren is nu in staat elke waarde Z of M weer te geven die aanwezig is in de geïdentificeerde objecten. Als het object een lijn of een polygoon is, zal het gereedschap het nummer voor de knoop weergeven en X/Y/Z/M voor de dichtstbijzijnde knoop ten opzichte van het geïdentificeerde punt. Het gereedschap Objecten identificeren geeft nu ook het aantal delen en deelnummers voor collecties weer.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Uniforme afhandeling van eenheden voor afstand en gebieden en indelingen voor coördinaten
In QGIS 2.14 zijn de afhandeling van verscheidene opties met betrekking tot eenheden voor afstand en gebieden en weergave van coördinaten geüniformeerd, vereenvoudigd en verplaatst naar Projecteigenschappen. Deze verandering biedt vele voordelen, inclusief:
- De indeling voor coördinaten, gespecificeerd in Projecteigenschappen, wordt consistent gebruikt als een coördinaat wordt weergegeven aan de gebruiker, inclusief de resultaten van het gereedschap Objecten identificeren en de weergave van de Statusbalk.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- Aanvullende eenheden voor gebied zijn toegevoegd, inclusief vierkante yards, acres, hectares en meer.
- Aanvullende eenheden voor hoeken zijn toegevoegd aan het gereedschap voor het meten van hoeken, inclusief rotaties, minuten voor boog en seconden voor boog.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door het door QGIS gesponsorde programma voor het oplossen van problemen

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Browser
### Mogelijkheid: Verbeteringen aan Browser
De QGIS Browser is een paneel voor het bestandssysteem, OGC webservices en databaseverbindingen dat u snel en eenvoudig een laag uit de hiervoor genoemde bronnen laat slepen en neerzetten in uw kaartvenster (of in het venster van DB Manager). Twee nuttige nieuwe verbeteringen werden voor deze uitgave toegevoegd:
- **Paden kunnen selectief worden verborgen in het paneel Browser** - dit is nuttig voor het opschonen van uw lijst met bronnen en om alleen te focussen op relevante mappen.
- **Projecten direct uit de Browser laden** - nu kunt u een geheel project in het kaartvenster van QGIS slepen en laten vallen het zal worden geladen.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Nathan Woodrow
## Gegevensproviders
### Feature: Cache mogelijkheden voor WMS
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Ondersteuning voor gebogen geometrie uitgebreid
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Verbeterde afhandeling van velden time en datetime
QGIS 2.14 heeft verbeterde afhandeling voor de veldtypes time en datetime, inclusief:
- PostgreSQL velden voor tijdstempels worden juist afgehandeld
- De aandrijving voor expressies heeft nu volledige ondersteuning voor velden time
- De expressiebouwer geeft nu voorbeelden van berekeningen voor date, time, datetime en interval
- Velden time worden volledig ondersteund door vector bestandslagen (afhankelijk van de bestandsindeling), PostgreSQL, MS SQL Server en tijdelijke tekenlagen
- Opslaan van lagen als vectorbestanden files zal de velden time behouden als dat wordt ondersteund door de indeling van de vectorlaag (bijv. MapInfo .tab-bestanden)

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer, Nyall Dawson
### Mogelijkheid: Ondersteuning voor Z/M in provider Tekengescheiden tekst
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Transactiegroepen voor bewerken van Postgres
Een nieuwe optie is geïntroduceerd om het bewerken van transacties mogelijk te maken.

Wanneer deze optie is ingeschakeld
- Alle lagen uit dezelfde database worden in één transactiegroep geplaatst
- Wanneer de eerste laag van een groep in de modus bewerken wordt geplaatst, worden alle andere ook automatisch in modus Bewerken geplaatst
- Wanneer een laag wordt bewerkt, worden de wijzigingen onmiddellijk naar de database gezonden, wat het mogelijk maakt triggers en beperkingen onmiddellijk toe te passen
- Wanneer één laag in een groep lagen wordt doorgevoerd, worden alle lagen doorgevoerd (databasetransactie)
- Wanneer één laag in een groep lagen wordt teruggedraaid, worden alle lagen teruggedraaid (databasetransactie)

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Dit is op dit moment alleen geïmplementeerd voor databases van Postgres

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Mogelijkheid: PKI-authenticatie voor provider Postgres
De mogelijkheid om de QGIS Authentication Manager, geïntroduceerd in 2.12, te gebruiken is uitgebreid met de provider PostGIS. Dit maakt het mogelijk te verbinden met Postgres met behulp van basis of PKI-authenticatie, met de inloggegevens opgeslagen in de configuratie van QGIS. De nieuwe authenticatie voor provider Postgres kan ook worden gebruikt in de DB manager.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Deze mogelijkheid werd ontwikkeld door Luigi Pirelli
### Mogelijkheid: Virtuele lagen
Dynamische query's voor SQL kunnen nu worden gebruikt op elke soort vectorlaag die QGIS kan laden, zelfs als de indeling van de laag zelf geen ondersteuning biedt voor query's van SQL!

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

Het ondersteunde dialect van SQL is SQLite met functies van SpatiaLite. Functies voor expressies van QGIS mogen ook in query's worden gebruikt. Elk soort vectorlaag is toegankelijk voor de query, inclusief meerdere lagen van verschillende gegevensproviders om samenvoegingen te maken.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Mogelijkheid: Meer bestandsextensies voor bestandsselectie voor providers GDAL en OGR
Voor vector- en rasterbestanden vertrouwt QGIS op de bibliotheek van GDAL/OGR. Dat betekent dat nagenoeg elke bestandsindeling die kan worden geopend door GDAL of OGR direct kan worden geopend in QGIS. Tot nu werden sommige bestandsextensies niet toegevoegd an de bestandsselectie voor GDAL of OGR, wat er in resulteerde dat gebruikers geloofden dat QGIS die bestandsindelingen niet kon openen of behandelen. Enkele nieuwe extensies zijn nu toegevoegd aan de filters voor bestandsselectie in GDAL en OGR om dit probleem te verkleinen:

**Voor vectorbestanden:**
- .thf voor indeling EDIGEO Frans kadaster
- .ods voor indeling OpenDocument Spreadsheet LibreOffice/Apache OpenOffice
- .xls voor indeling Microsoft Excel
- .xlsx voor indeling Microsoft Excel OpenXML
- .xml voor indeling NAS - ALKIS
- .map voor indeling WAsP
- .pix voor indeling PCIDSK
- .gtm en.gtz voor indeling GPSTrackMaker
- .vfk voor indeling VFK
- .osm en .pbf voor indeling OpenStreetMap
- .sua voor indeling SUA
- .txt voor indeling OpenAir
- .xml voor indeling Planetary Data Systems TABLE
- .htf voor indeling Hydrographic Transfer
- .svg voor indeling SVG
- .gen voor ARCGEN
- .sxf voor indelingen voor opslag en uitwisseling
- .pdf voor vectorindeling Geospatial PDF
- .sgy en .segy voor indeling SEG-Y
- .seg, .seg1, .sp1, .uko, .ukooa voor indeling SEGUKOOA
- .ovf voor vectorbestandsindeling VRT
- .kmz voor indeling gecomprimeerde KML (KMZ)
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 voor indeling  SQLite/SpatiaLite
- .sl3 voor indeling SQLite Spatial (FDO)
- CouchDB Spatial (via URL)

**Voor rasterbestanden:**
- .ovr voor rasterbestandsindeling vrt

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Deze methode zal het aantal knopen verminderen van de geometrieën die QGIS moet downloaden vanaf de server, wat de snelheid van het renderen zal verhogen en bandbreedte zal besparen tussen QGIS en de server van PostgreSQL.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## Gegevensbeheer
### Mogelijkheid: Plug-in SPIT verwijderd
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Nathan Woodrow
### Mogelijkheid: Exporteren als DXF: optie om titel te gebruiken in plaats van de naam als laagnaam voor DXF in toepassing en server
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Type geometrie kan worden overschreven in het dialoogvenster Vector opslaan als
Dit maakt jet mogelijk dingen te doen als het opslaan van een tabel zonder geometrie MET een type geometrie, zodat geometrieën dan handmatig kunnen worden toegevoegd aan rijen. eerder was dit alleen mogelijk in QGIS te doen door opnieuw te sorteren op dummy-samenvoegingen of andere workarounds.

Aanvullend zijn opties toegevoegd om te forceren dat het type uitvoerbestand multitype is, of een dimensie Z bevat.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Vectorsamenvoegingen worden nu opgeslagen in QLR laagdefinitie bestanden
### Mogelijkheid: Widget Externe bron
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- U kunt een **relatief pad voor opslaan** definiëren en instellen. Relatieve paden voor opslag zullen u in staat stellen allen dat deel van het pad op te slaan dat na het standaard pad is gelegen (als standaard pad is ingesteld) of het huidige pad voor het project. Dit is in het bijzonder nuttig wanneer u lange paden wilt opslaan in attributen met beperkte grootte (zoals tekstattributen voor Shapefiles die zijn beperkt tot 254 tekens), of voor het maken van zichzelf bevattende project- en gegevensbestandsarchieven voor distributie.
- Een andere nieuwe mogelijkheid om het widget gemakkelijker te gebruiken is dat **bestandspaden nu kunnen worden weergegeven als hyperlinks**. klikken op de hyperlink zal het gekoppelde bestand direct openen vanuit QGIS. U kunt deze optie configureren om het volledige pad van het bestand weer te geven of alleen de bestandsnaam. Het bestand zal worden geopend met behulp van de standaard afhandelaar voor die bestandsindeling vanuit uw besturingssysteem.
- U kunt ook **een URL gebruiken in plaats van een bestandspad**. Het widget zal het interpreteren als een URL en u zult in staat zijn de gekoppelde webpagina direct in uw standaard webbrowser te openen.
- U kunt er voor kiezen **paden naar mappen op te slaan in plaats van bestandspaden**.
- Er is een **geïntegreerde documentviewer** in dit widget. U kunt het gebruiken om afbeeldingen of webpagina's direct weer te geven in QGIS. De bestandsselectie voor de geïntegreerde viewer heeft voordeel van alle hierboven genoemde opties.

Voor meer informatie over opties voor configuratie, kunt u de helptips in het dialoogvenster voor configureren gebruiken.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Deze mogelijkheid werd ontwikkeld door**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Mogelijkheid: Bewerken relatie N:M
Dit voegt de mogelijkheid toe om gegevens te beheren in een genormaliseerde relationele database in relaties N:M (veel tot veel). Op de relatiebewerker in een formulier werken de gereedschappen om toe te voegen, te verwijderen, koppelen en koppeling verwijderen ook op de tabel om te koppelen als een relatie wordt gevisualiseerd als een relatie N:M.

Configuratie vindt plaats op de tab Velden waar op de relatie een tweede relatie kan worden gekozen (indien er een geschikte relatie is in termen van een tweede relatie op de tabel om te koppelen).

**Beperkingen:**

QGIS is geen beheerssysteem voor databases.

Het is gebaseerd op aannames vanuit het onderliggende systeem van de database. In het bijzonder:
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door Kanton Neuchâtel, stad Pully, stad Vevey

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Digitaliseren
### Mogelijkheid: Kleur van het elastiek te configureren
U kunt nu breedte en kleur voor het elastiek, dat wordt gebruikt voor Digitaliseren, instellen.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Mogelijkheid: gereedschap Traceren voor digitaliseren
Het nieuwe gereedschap Traceren is een geavanceerd gereedschap voor digitaliseren dat u in staat stelt objecten in de ene laag te digitaliseren door die objecten in een andere laag te volgen.

Het gereedschap Traceren:
- uses Dijkstra's shortest path algorithm to find traceable routes
- kan routes traceren over meerdere afzonderlijke objecten
- kan worden gebruikt met gereedschappen van geavanceerd Digitaliseren (bijv. opnieuw vormen)
- kan worden in- en uitgeschakeld door **T** in te drukken op uw toetsenbord tijdens het digitaliseren
- is snel een gemakkelijk te gebruiken

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Deze mogelijkheid werd mogelijk gemaakt door: de Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Labelen
### Feature: \"Cartographic\" placement mode for point labels
In deze plaatsingsmodus, worden kandidaten voor puntlabels gegenereerd die de ideale cartografische regels voor plaatsing volgen, bijv. plaatsing van labels wordt geprioriteerd in de volgorde:
- rechtsboven
- linksboven
- rechtsonder
- linksonder
- rechts midden
- links midden
- boven, iets naar rechts
- onder, iets naar links

(rekening houdende met de richtlijnen van Krygier en Wood (2011) en andere cartografische meesterwerken)

De prioriteit voor plaatsing kan ook worden ingesteld voor een individueel object met behulp van een gegevensgedefinieerde lijst met geprioriteerde posities. Dit maakt het mogelijk dat slechts enkele bepaalde plaatsingen kunnen worden gebruikt, dus bijv voor objecten langs de kust zou u kunnen voorkomen dat labels boven land worden geplaatst.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Afstand voor label toepassen vanaf grenzen symbool
Als deze instelling actief is, is de afstand voor het label van toepassing vanaf de grenzen van het gerenderde symbool voor een punt in plaats van voor het punt zelf. Dit is speciaal nuttig wanneer de grootte va het symbool niet vast is, bijv. als het wordt ingesteld door een gegevensgedefinieerde grootte of bij het gebruiken van verschillende symbolen in een renderer Categorieën.

Onthoud dat deze instelling alleen beschikbaar is met de nieuwe modus voor plaatsing van puntlabels Cartografisch.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Volgorde van renderen van labels beheren
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

Aanvullend is de logica aangepast zodat als 2 labels overenekomende Z-indexen hebben, dan:
- als zij van dezelfde laag zijn zal een kleiner label altijd boven een groter label worden getekend
- als zij uit verschillende lagen komen zullen zij worden getekend in dezelfde volgorde als de lagen zelf (d.i. rekening houdende met de volgorde die is ingesteld in de legenda)

Diagrammen kunnen ook hun Z-index hebben ingesteld (maar niet gegevensgedefinieerd) zodat de volgorde van labels en diagrammen kan worden beheerd.

Onthoud dat dit het *NIET* mogelijk maakt dat labels onder de objecten van andere lagen worden getekend, het beheert slechts de volgorde waarin labels bovenop uw kaart worden getekend.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Feitelijk gerenderde symbool wordt nu beschouwd als een obstakel voor labels van puntobjecten
Eerder werd alleen het puntobject zelf behandeld
als een obstakel voor kandidaat-labels. Indien een groot of verschoven symbool werd gebruikt voor het punt, dan werd labels toegestaan dit symbool te overlappen zonder de lasten van het obstakel zijn mee te wegen.

Nu wordt rekening gehouden met de feitelijke grootte en verschuiving van het gerenderde symbool bij het detecteren van of een label botst met een puntobject. Het resultaat is nu dat QGIS in meer omstandigheden het tekenen van labels over puntsymbolen vermijd.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door Stad Uster

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Legenda van laag
### Mogelijkheid: Een stijl op meerdere geselecteerde lagen plakken of op alle lagen in een groep van de legenda
Deze mogelijkheid voegt de mogelijkheid toe om de stijl van één laag te plakken op een groep lagen of op geselecteerde lagen.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Salvatore Larosa
### Mogelijkheid: Legenda filteren met expressie
Het is nu mogelijk elementen van de legenda te filteren met een expressie. Het is ontworpen met het filteren van op regel gebaseerde of gecategoriseerde symbologie in gedachte.

Het filteren van de legenda is beschikbaar in de legenda van de hoofdtoepassing, als ook voor componenten van de legenda in de QGIS Printvormgeving.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Printvormgeving
### Mogelijkheid: Nieuwe opties voor filteren van elementen van de legenda
Dit introduceert twee nieuwe opties om elementen van de legenda te filteren.

De eerste, filteren met expressie, stelt gebruikers in staat een expressie in te stellen voor het filteren van welke objecten zouden moeten worden weergegeven in de legenda. Alleen symbolen met een overeenkomend object zullen worden weergegeven in de legenda.

De tweede optie voor filteren maakt het mogelijk een legenda van Printvormgeving te filteren om alleen items te bevatten die ook zijn opgenomen binnen de huidige polygoon van Atlas.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Aanvullende paden voor sjablonen van Printvormgeving
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Nathan Woodrow
### Mogelijkheid: Meervoudige selectie van lay-outs in beheer
De Printvormgeving-manager heeft ondersteuning gekregen voor het beheren van meerdere lay-outs op hetzelfde moment. U kunt nu meerdere lay-outs tegelijkertijd openen of verwijderen met behulp van de Ctrl-toets en meerdere lay-outs uit de lijst selecteren.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Plug-ins
### Mogelijkheid: Ondersteuning voor authenticatiesysteem voor beheer plug-ins
Ondersteuning voor het nieuwe authenticatiesysteem is toegevoegd aan het beheer voor plug-ins. Dit stelt gebruikers in staat configuraties voor authenticatie toe te passen voor verbindingen met opslagplaatsen voor plug-ins, en systeembeheerders om geauthenticeerde toegang te verschaffen tot opslagplaatsen van plug-ins en/of de downloadpakketten van plug-ins.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Deze mogelijkheid werd ontwikkeld door Larry Shaffer
## Processing
### Mogelijkheid: Nieuwe algoritmes in 2.14
#### QGIS geo-algoritmes:
- Smooth: voor glad maken van lijn- of polygoonlagen.
- Omgekeerde lijnrichting.

#### GDAL/OGR geo-algoritmes:
- gdal2tiles: bouwt een map met TMS-tegels, KML's en eenvoudige webviewers.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Mogelijkheid: Q/A eenheidstesten
Een nieuw testframework is geïntroduceerd om de stabiliteit van de module processing op de lange termijn te garanderen.

Geo-algoritmes van Processing worden uitgevoerd na elke wijziging die raakt aan de broncode van QGIS en de resultaten worden vergeleken met een controle gegevensset om het juiste gedrag te garanderen. Dit geeft onmiddellijke terugkoppeling over mogelijke regressies.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Verbeterde Toolbox
De vereenvoudigde interface is verwijderd, en een nieuwe en meer gebruikersvriendelijk systeem voor het beheren van de providers is toegevoegd. De functionaliteit voor het zoeken van algoritmes zoekt nu ook in providers die niet actief zijn, en stelt voor om ze te activeren.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Deze mogelijkheid werd ontwikkeld door Víctor Olaya
### Mogelijkheid: Batchprocessen kunnen worden opgeslagen en later worden opgehaald met de interface voor Batchprocessing
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Mogelijkheid: Meer informatief dialoogvenster voor algoritmes
Een korte beschrijving wordt nu weergegeven naast de parameters van het algoritme, wat het eenvoudiger maakt het doel van het algoritme te begrijpen.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Mogelijkheid:  modules v.net voor GRASS7
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

Algoritmes v.net gebruiken vaak een lijn vectorlaag (voor het netwerk) en een puntlaag die de knopen weergeeft die u wilt gebruiken voor de berekening. Zorg er voor een ware graph lijn vectorlaag te gebruiken als de netwerklaag (randen moeten zijn verbonden met vertex zonder kruisingen tussen randen) om problemen te vermijden. U kunt ook elk attribuut voor een netwerklaag gebruiken voor berekening van de kosten (de inhoud van het attribuut wordt gebruikt om de reiskosten naar de rand te berekenen).

Hier is een snelle samenvatting van de verschillende algoritmes die zijn opgenomen in Processing:
- v.net.alloc: Kent subnetten toe voor nabijgelegen centra.
- v.net.allpairs: Berekent de kortste afstand tussen alle paren van knopen in het netwerk.
- v.net.arcs: Maakt bogen uit een bestand met punten.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: Berekent metingen voor degree, centrality, betweeness, closeness en eigenvector centrality in het netwerk.
- v.net.components: Berekent sterke en zwakke verbonden componenten in het netwerk.
- v.net.connect: Verbindt punten (knopen) met de dichtstbij gelegen boog in een netwerk (en voegt randen toe indien nodig).
- v.net.connectivity: Berekent de vertex-connectiviteit tussen twee sets van knopen in het netwerk.
- v.net.distance: Berekent de kortste afstand via het netwerk tussen twee sets van knopen.
- v.net.flow: Berekent de maximale stroom tussen twee sets van knopen in het netwerk..
- v.net.iso: Berekent de isochrone kaart van een netwerk  uit een set van knopen.
- v.net.nodes: Neemt knopen uit een netwerk/graph-laag.
- v.net.nreports: Rapporteert informatie over de knopen.
- v.net.path: Zoekt de kortste afstand via het netwerk tussen twee knopen.
- v.net.report: Rapporteert informatie over de randen van het netwerk.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: Voert grafische zichtbaarheidsconstructie uit.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programmeerbaarheid
### Mogelijkheid: Functiebewerker voor expressie opnieuw ontworpen
Met automatisch opslaan

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Mogelijkheid: Init-code voor Python opslaan in het project
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Mogelijkheid: Nieuwe opties filteren en sorteren voor QgsFeatureRequest
QgsFeatureRequest ondersteunt nu instellingen voor een maximum limiet voor het aantal terug te geven objecten. In veel gevallen wordt deze limiet doorgegeven aan de provider, resulterend in significante winst in de uitvoering wanneer slechts een bepaald aantal objecten zijn vereist.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Mogelijkheid: Opties voor aangepast objectformulier voor code van Python
Deze mogelijkheid voegt meer opties toe aan het aangepaste objectfomulier voor code van Python:
- laden uit bestand (met widget Bestandsselectie)
- laden uit omgeving (d.i. een plug-in of een Pythonfunctie init)
- direct invoeren van de code in een widget Invoer (nieuwe optie)

De opties voor configuratie, inclusief de aangepaste Python-code ingevoerd in het dialoogvenster worden opgeslagen in het project, als ook in de instellingen van QML voor de stijl en kunnen worden geëxporteerd/hersteld naar/vanuit een database.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Mogelijkheid: Nieuwe klassen voor PyQGIS in 2.14
### Nieuwe bronklassen
- [QgsAttributeEditorElement](https://qgis.org/api/classQgsAttributeEditorElement.html)
  - abstract base class for any elements of a drag and drop form
- [QgsAttributeEditorContainer](https://qgis.org/api/classQgsAttributeEditorContainer.html)
  
  \- container for attribute editors, used to group them visually in an attribute form
- [QgsAttributeEditorField](https://qgis.org/api/classQgsAttributeEditorField.html)
  - element for loading a field\'s widget onto a form
- [QgsAttributeEditorRelation](https://qgis.org/api/classQgsAttributeEditorRelation.html)
  - element for loading a relation editor widget onto a form
- [QgsEditFormConfig](https://qgis.org/api/classQgsEditFormConfig.html)
  - stores and sets configuration parameters for attribute editor forms
- [QgsFeatureFilterProvider](https://qgis.org/api/classQgsFeatureFilterProvider.html)
  
  \- provides an interface for modifying a QgsFeatureRequest in place to apply additional filters to the request
- [QgsTracer](https://qgis.org/api/classQgsTracer.html) - provides graph creation and shortest path search for vector layers
- [QgsTransactionGroup](https://qgis.org/api/classQgsTransactionGroup.html)
  - interface for grouping layers into single edit transactions
- [QgsUnitTypes](https://qgis.org/api/classQgsUnitTypes.html) -helper functions for various unit types and conversions between units (eg distance and area units)
- [QgsVirtualLayerDefinition](https://qgis.org/api/classQgsVirtualLayerDefinition.html)
  - class for manipulating the definitions of virtual layers
- [QgsVirtualLayerDefinitionUtils](https://qgis.org/api/classQgsVirtualLayerDefinitionUtils.html)
  - helper utilities for working with QgsVirtualLayerDefinition objects
- [Qgs25DRenderer](https://qgis.org/api/classQgs25DRenderer.html) -2.5D symbol renderer
- [QgsGeometryGeneratorSymbolLayerV2](https://qgis.org/api/classQgsGeometryGeneratorSymbolLayerV2.html)
  - geometry generator symbol layer
- [QgsFeatureRequest.OrderByClause](https://qgis.org/api/classQgsFeatureRequest_1_1OrderByClause.html)
  - class for specifying a field sort order for feature requests
- [QgsFeatureRequest.OrderBy](https://qgis.org/api/classQgsFeatureRequest_1_1OrderBy.html)
  - a prioritized list of order by clauses for sorting

### Nieuwe klassen voor GUI
#### Opnieuw te gebruiken widgets:
- [QgsExternalResourceWidget](https://qgis.org/api/classQgsExternalResourceWidget.html)
  
  \- widget for displaying a file path with a push button for an \"open file\" dialog, and optional display of pictures or HTML files
- [QgsFileWidget](https://qgis.org/api/classQgsFileWidget.html) -widget for selecting a file or a folder
- [QgsLegendFilterButton](https://qgis.org/api/classQgsLegendFilterButton.html)
  
  \- tool button widget that allows enabling or disabling legend filter by contents of the map
- [QgsMapCanvasTracer](https://qgis.org/api/classQgsMapCanvasTracer.html)
  
  \- an extension of QgsTracer that provides extra functionality for interacting with map canvases
- [Qgs25DRendererWidget](https://qgis.org/api/classQgs25DRendererWidget.html)
  - widget for setting properties for a 2.5D renderer
- [QgsColorWidgetAction](https://qgis.org/api/classQgsColorWidgetAction.html)
  - widget action for embedding a color picker inside a menu

#### Opnieuw te gebruiken dialoogvensters:
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGIS Server
### Mogelijkheid: parameter STARTINDEX in WFS GetFeature Request
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Mogelijkheid: showFeatureCount in GetLegendGraphic
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Deze mogelijkheid heeft een fake X server nodig.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Mogelijkheid: Optie om het renderen van onregelmatigheden aan de randen van tegels te vermijden
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Mogelijkheid: Controle van configuratie in projecteigenschappen
Een nieuwe controle voor configuratie is toegevoegd aan projecteigenschappen om te helpen bij het configureren van een project voor QGIS Server,.

De controle test op fouten als:
- duplicaatnamen of verkorte namen gebruikt als namen voor OWS
- ongeldige namen voor OWS
- ontbrekende coderingen voor vectorlagen

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Mogelijkheid: mogelijkheden voor WMS INSPIRE
In de projecteigenschappen kan de gebruiker:
- mogelijkheden voor INSPIRE activeren
- de taal voor de service selecteren, uit 24 officiële talen voor de EU + 5 regionale talen
- het scenario voor service metadata selecteren en hun parameters specificeren

De mogelijkheden voor WMS 1.3.0 sluiten aan op de configuratie van INSPIRE.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Mogelijkheid: Verkorte namen toevoegen aan lagen, groepen en project
Een aantal elementen heeft zowel een **Naam** als een **Titel**. De Naam is teksttekenreeks gebruikt voor communicatie van machine-naar-machine terwijl de Titel ten behoeve van mensen is. Een gegevensset kan bijvoorbeeld de beschrijvende Titel *Maximum Atmospheric Temperature* hebben en kan worden bevraagd met de verkorte Naam *ATMAX*.

Gebruikers zouden al een titel kunnenhebben ingesteld voor lagen en het project. OpenGeospatial Web Services, OWS (WMS, WFS, WCS), naam is gebaseerd op de gebruikte naam in de boom van lagen. Deze naam is meer een label voor mensen dan een naam voor communicatie van machine-naar-machine.

Deze mogelijkheid voegt de mogelijkheid voor gebruikers toe om Name te definiëren als een teksttekenreeks voor communicatie van machine-naar-machine:
- verkorte naam voor bewerkingselementen voor laageigenschappen
- dialoogvenster voor gegevens van WMS om de boom van lagen te groeperen (verkorte naam, titel, abstract)
- bewerkingen voor verkorte naam voor projecteigenschappen
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- element TreeName toegevoegd aan de fullProjectSettings

Als een verkorte naam is ingesteld voor lagen, groepen en project wordt die gebruikt door QGIS Server als de laagnaam.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Symbologie
### Mogelijkheid: Assistent Grootte voor variëren van de breedte van de lijn
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Mogelijkheid: Ondersteuning voor transparantie in parameters voor SVG-kleuren
Niet-gebundelde SVG's moeten toevoegen:

`fill-opacity="param(fill-opacity)"`

en

`stroke-opacity="param(outline-opacity)"`

om ondersteuning voor transparantie in te schakelen.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Gemakkelijk dupliceren van symboollagen
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Renderer 2.5D
Dit voegt een interface toe voor configuratie en renderer die het eenvoudiger maakt om alle stukken samen te voegen die vereist zijn om een 2.5D-effect te krijgen.

Het maakt het configureren van delen van de stijl en is bedoeld voor een eenvoudige-naar-eenvoudige isetup.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Deze mogelijkheid werd ontwikkeld door**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Dit werd mogelijk gemaakt door**:
- Regionale raad van Picardië
- ADUGA
- Stad Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Mogelijkheid: Toestaan van definitie van volgorde voor renderen voor objecten
Wanneer objecten zijn vereist om te worden gerenderd in een bepaalde volgorde, kan dit worden gespecificeerd door een willekeurige expressie te gebruiken.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

Het verschaft ook beheer over een oplopende of aflopende volgorde, als ook of NUL-en eerst of laatst zijn.

Indien mogelijk zal het verzoek worden verzonden naar de database (Dit is afhankelijk van de complexiteit van de expressie, als ook van de provider voor de laag). Als het niet mogelijk is om het verzoek te verzenden naar de database, zal de sortering worden uitgevoerd op de lokale machine.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

Dit is ook beschikbaar voor plug-ins:

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheden: Symbolen voor geometrie-generator
Symbolen voor geometrie-generator maken het mogelijk de aandrijving voor expressies te gebruiken voor het aanpassen van de geometrie vóór het renderen of zelfs nieuwe geometrieën te maken tijdens het renderen, gebaseerd op attributen van het object.

Dit kan  alle soorten ruimtelijke operatoren gebruiken, zoals buffer, translate, intersect of extrude met parameters gebaseerd op attributen alleen voor het renderen zonder in feite de gegevens in de bron aan te passen.
### Voorbeelden
#### Translate een geometrie
Gebruikt voor het dak van de 2.5D renderer

    translate( $geometry, 10, 10 )
    
#### Vulstijl voor de rand van de polygoon
Dit genereert een polygoon die de omtrek van de originele polygoon weergeeft (Voorbeeld afbeelding)

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
Verschillende symboollagen kunnen verschillende geometrie-generatoren bevatten, dit maakt het mogelijk om tegelijkertijd verschillende versies van een een geometrie weer te geven. De 2.5D renderer dient als voorbeeld.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Regionale raad van Picardië, ADUGA, Stad Nyon, Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Gebruikersinterface
### Mogelijkheid: Attributentabel kan worden vernieuwd
Een optie om attributen opnieuw te laden binnen de attributentabel is nu beschikbaar.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Mogelijkheid: Direct instellen kleuren renderer en klassesymbool uit contextmenu in legenda
Geeft een widget kleurenwiel weer in het menu, wat u in staat stelt interactief de kleur voor een symbool te bewerken zonder zelfs één enkel dialoogvenster te moeten openen!

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Symbolen voor de legenda direct bewerken vanuit de boom met lagen
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Mogelijkheid: Alle items voor de legenda weergeven/verbergen via het contextmenu
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
