---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.14
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.14{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Data lansării: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Versiunea cu Suport pe Termen Lung**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

Scopul versiunilor LTR este de a oferi o platformă stabilă și mai puțin supusă schimbărilor, pentru întreprinderi și organizații care nu doresc să se ocupe cu reactualizarea competențelor utilizatorilor, a materialelor de instruire etc., mai mult de o dată pe an. Succesul versiunilor LTR ține de voi, utilizatorii noștri dragi - avem nevoie de sprijinul vostru pentru a ajuta la finanțarea reparării erorilor, asigurându-vă, totodată, prin contractele de asistență cu furnizorii de suport tehnic, că toate erorile reparate în numele dumneavoastră vor fi aplicate atât versiunii LTR cât și celei obișnuite.

De asemenea, în cazul în care o versiune LTR este importantă pentru dvs., vă rugăm să luați în considerare susținerea în mod direct a proiectului QGIS, sau să propuneți furnizorului dumneavoastră comercial utilizarea LTR ca bază pentru soluțiile de întreprindere, astfel încât oricine să poată beneficia de o platformă stabilă,  îmbunătățită și finisată în permanență. Rețineți că pentru utilizatorii și organizațiile cărora le plac lucrurile împinse la limită, elaborarea unei noi versiuni, o dată la patru luni, va continua neabătut.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Mulțumiri**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Sponsori Actuali ai QGIS
{{<fund type="changelog" >}}
## Generalități
### Funcționalitate: Comportament schimbat al funcției strpos
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Fișierele de proiect din versiunile anterioare QGIS vor trebui să fie actualizate, pentru a reflecta această modificare.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Jürgen Fischer
### Funcționalitate: Transfocare la nivelul entității, cu ajutorul unui clic dreapta în tabelul de atribute
De acum, puteți transfoca la nivelulu oricărei entități din cadrul tabelului de atribute (fără a fi nevoie să o selectați mai întâi) făcând clic dreapta și alegând transfocare la nivelul entității.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Funcționalitate: Îmbunătățiri aduse vitezei și memoriei
- **Salvarea unui set de entități selectate** dintr-un strat foarte mare, este, de acum, mult mai rapidă
- Actualizarea doar a entităților selectate, folosind **calculatorul de câmpuri** este mai rapidă
- **Transfocare mai rapidă** asupra selecțiilor din straturile mari
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **Filtrarea categoriilor dintr-un render de categorisire** (de exemplu, prezentând doar unele categorii și debifându-le pe altele) este mult mai rapidă, deoarece acum doar entitățile potrivite sunt preluate din furnizorul de date
- **Reducere semnificativă a memoriei** necesară pentru deschiderea straturilor vectoriale de mari dimensiuni

### Funcționalitate: Mai multe variabile în cadrul expresiilor
Pe durata randării, noi variabile vor fi disponibile:
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Acestea sunt utile pentru a aplica diferite stiluri diverselor părți ale entităților multiparte:
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

Au fost, de asemenea, adăugate variabilele referitoare la mediul de operare:
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

Această facilitate a fost finanțată de Andreas Neumann (variabilele referitoare la sistemul de operare și la utilizator)

Această funcționalitate a fost dezvoltată de Nyall Dawson, Matthias Kuhn
### Funcționalitate: Mai mult control asupra plasamentului elementelor de hartă
QGIS 2.14 a dobândit un control mai bun asupra plasării pe canevas a săgeții nordului, a bării de scară și a notițelor privind drepturile de autor. De acum puteți seta cu precizie poziționarea acestor elemente, folosind diferite unități (inclusiv milimetri, pixeli și procente).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Funcționalitate: Program de plată pentru eliminarea erorilor
Înainte de fiecare lansare, vom susține un program plătit de eliminare a erorilor, în care vom finanța dezvoltatorii să curețe cât mai multe erori posibil. Am decis să inițiem inclusiv un nou raport cu privire la acest program de eliminare cu plată a defecțiunilor, ca parte a jurnalului schimbărilor. Rețineți că această listă **nu este exhaustivă**.
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
- Nyall Dawson: Filtrarea pe partea de server este nefuncțională pentru straturi OGR, Oracle și Spatialite
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: S-au remediat probleme care blocau un render, la conversia acestuia în render bazat pe reguli
- Nyall Dawson: S-a remediat un defect care împiedica renderul bazat pe categorii să stocheze modificările aduse simbolului sursei
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: S-a remediat manipularea valorii timpului în atribute
- Nyall Dawson: S-a remediat ordinea filelor dialogului
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Acum câmpurile LongLong se interpretează corect în dialogul de îmbinare a atributelor
- Nyall Dawson: S-a remediat afișarea eronată a detaliilor de calcul din dialogul instrumentului de măsurare (era înșelătoare și inexactă pentru multe combinații CRS/unitate)
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias: desenare defectuoasă a straturilor raster
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias: În modul de depanare încărcarea tabelului de atribute are loc lent
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias: S-au adus corecții la renderul 2.5d
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
- Jürgen Fischer: s-a remediat setarea căii SAGA

### Feature: Field calculator can be used to update feature\'s geometry
Calculatorul de câmpuri poate fi utilizat de acum pentru a actualiza o geometrie a unei entități utilizând rezultatul unei expresii geometrice. Aceasta este o comandă rapidă, la îndemână, pentru a face operații de genul aplicării unui tampon unui grup de entități selectate, care, alături de toate funcțiile specifice geometriilor, nou adăugate în 2.14, facilitează manipularea geometriilor dvs.!

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Noi funcții pentru expresii în 2.14
În versiunea 2.14 au fost adăugate multe funcții noi, specifice expresiilor:
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

Alte îmbunătățiri:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Instrumentele de analiză
### Funcționalitate: Mai multe statistici disponibile în instrumentul de îmbinare a atributelor
Atunci când se utilizează îmbinarea valorilor atributului sau instrumentul de îmbinare a entităților, sunt disponibile sumare cu statistici, care se pot utiliza la stabilirea valorilor pentru atributele rezultate. Printre altele, sunt incluse cuartilele Q1 și Q3, intervalele intercuartile, valorile majorității și minoritții precum și numărul de valori unice.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Valorile z/m sunt afișate atunci când se utilizează instrumentul de identificare
Instrumentul de identificare este de acum capabil să arate orice valoare z sau m prezentă în entitățile identificate. În cazul în care entitatea este de tip linie sau poligon, instrumentul va afișa numărul vertecșilor și coordonatele x/y/z/m pentru cel mai apropiat vertex față de punctul identificat. De acum, instrumentul de identificare arată, de asemenea, numărul de părți și numărul de identificare al fiecărei părți, în cazul colecțiilor.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Manipulare centralizată a unităților de distanță și de suprafață, și a formatelor pentru coordonate
În QGIS 2.14 manipularea diferitelor opțiuni referitoare la unitățile de distanță, de suprafață și de afișare a coordonatelor au fost unificate, simplificate, fiind grupate în Proprietățile Proiectului. Această modificare aduce numeroase avantaje, printre care:
- Formatul pentru coordonate, specificat în Proprietățile Proiectului, este utilizat de fiecare dată când o coordonată este afișată utilizatorului, inclusiv la prezentarea rezultatelor instrumentului de identificare și la afișarea în bara de stare.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- Au fost adăugate unități suplimentare pentru arii, incluzând yarzi pătrați, acri, hectare și multe altele.
- instrumentul de măsurare a unghiului i s-au adăugat unități unghiulare suplimentare, inclusiv rotații, minute de arc și secunde de arc.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Această facilitate a fost finanțată prin programul de eliminare a erorilor, sponsorizat de QGIS

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Navigatorul
### Funcționalitate: Îmbunătățiri aduse Navigatorului
Navigatorul QGIS constă într-un sistem de fișiere, în Servicii Web OGC și conexiuni de date, care vă permit să trageți cu ușurință orice strat din sursele menționate mai sus, iar apoi să-l fixați în canevasul hărții (sau în fereastra DB Manager). În această versiune s-au adus două noi îmbunătățiri utile:
- **Căile pot fi ascunse în mod selectiv, utilizând panoul navigatorului** - acest lucru este util pentru curățarea listei cu surse, și să vă concentrați doar pe directoarele relevante.
- **Încărcarea proiectelor direct din navigator** - acum aveți posibilitatea să glisați și să eliberați un întreg proiect în canevasul hărții QGIS, iar acesta va fi încărcat.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Nathan Woodrow
## Furnizorii de Date
### Funcționalitate: Capabilităţi de păstrare în memoria tampon a cererilor WMS
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Jürgen Fischer
### Funcționalitate: S-a extins suportul pentru geometria curbată
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Gestiune îmbunătățită pentru câmpurile de tipurile time și datetime
QGIS 2.14 dispune de o manipulare îmbunătățită a câmpurilor de tipurile time și datetime, iar în plus:
- Câmpurile de tip amprentă temporală din PostgreSQL sunt manipulate corect
- Motorul de expresii are de acum suport complet pentru câmpurile de tipul time
- Generatorul de expresii oferă de acum previzualizarea rezultatelor calculului pentru dată, oră și intervale de ore sau date
- Câmpurile time sunt pe deplin acceptate de straturile fișierelor vectoriale (în funcție de formatul de fișier), PostgreSQL, MS SQL Server și de straturile temporare stocate în memorie
- La salvarea straturilor în fișiere vectoriale se va păstra tipurile time din câmpuri, dacă acest lucru este acceptat de formatul stratului vectorial (de exemplu,  fișiere MapInfo, cu extensia .tab)

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Jürgen Fischer, Nyall Dawson
### Funcționalitate: Suport Z/M în furnizorul de text delimitat
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Grupuri de tranzacții pentru editarea Postgres: 
O nouă opțiune a fost introdusă pentru a permite editarea tranzacțională.

Atunci când această opțiune este activată
- Toate straturile din aceeași bază de date sunt incluse într-un grup de tranzacții
- În cazul în care primul strat al unui grup este pus în modul de editare, toate celelalte straturi sunt, de asemenea, puse automat în modul de editare
- Atunci când un strat este editat, modificările sunt transmise imediat în baza de date, permițând aplicarea imediată a declanșatorilor și a constrângerilor
- În urma modificărilor efectuate asupra unui strat dintr-un grup de tranzacții, se vor salva toate straturile (tranzacție la nivelul bazei de date)
- În urma refacerii modificărilor aduse unui strat dintr-un grup de tranzacții, se vor reface modificările din toate straturile (tranzacție la nivelul bazei de date)

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Acest lucru este aplicabil doar bazelor de date Postgres, la acest moment.

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Funcționalitate: Autentificare PKI pentru furnizorul Postgres
Abilitatea de a utiliza Managerul de Autentificare QGIS, introdusă în 2.12, a fost extinsă la furnizorul PostGIS. Acest lucru permite conectarea la Postgres folosind autentificarea de bază sau PKI, cu acreditările stocate în configurația QGIS. Noul furnizor de autentificarea Postgres poate fi utilizat și în DB Manager.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Această funcționalitate a fost dezvoltată de Luigi Pirelli
### Funcționalitate: Straturi virtuale
Interogările dinamice SQL pot fi acum folosite pentru orice fel de straturi vectoriale pe care le poate încărca QGIS, chiar dacă, în sine, formatul stratului nu are suport pentru interogări SQL!

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

Dialectul SQL permis este SQLite, cu funcții Spatialite. Expresiile cu funcții QGIS pot fi utilizate, de asemenea, în interogări. Orice fel de straturi vectoriale pot fi accesate în interogare, inclusiv mai multe straturi de la diferiți furnizori de date, în scopul creării de joncțiuni.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Funcționalitate: Mai multe extensii de fișiere pentru furnizorii selectorilor de fișiere  GDAL și OGR
Pentru fișierele vectoriale și raster, QGIS se bazează pe biblioteca GDAL/OGR. Aceasta înseamnă că aproape orice format de fișier care poate fi deschis de către GDAL sau OGR, poate fi deschis direct din QGIS. Până în prezent, unele extensii de fișiere nu au fost adăugate în selectorul de fișiere GDAL sau OGR și, drept urmare, există utilizatori care cred că QGIS nu poate deschide sau manipula aceste formate. Pentru a minimiza această problemă, unele extensii noi au fost adăugate în filtrele de selectare a fișierelor GDAL și OGR:

**Pentru fișierele vectoriale:**
- .thf pentru formatul franțuzesc de cadastru EDIGEO
- .ods pentru formatul Foilor de calcul de tip Open Document LibreOffice
- .xls pentru formatul MS Excel
- .xlsx pentru formatul Microsoft Excel OpenXML
- .xml pentru formatul NAS - ALKIS
- .map pentru formatul WAsP
- .pix pentru formatul PCIDSK
- .gtm și .gtz pentru formatul GPSTrackMaker
- .vfk pentru formatul VFK
- .osm și .pbf pentru formatul OpenStreetMap
- .sua pentru formatul SUA
- .txt pentru formatul OpenAir
- .xml pentru formatul Planetary Data Systems TABLE
- .htf pentru formatul Hydrographic Transfer
- .svg pentru formatul SVG
- .gen pentru formatul ARCGEN
- .sxf pentru formatul Storage and eXchange
- .pdf pentru formatul vectorial Geospatial PDF
- .sgy și .segy pentru formatul SEG-Y
- .seg, .seg1, .sp1, .uko, .ukooa pentru formatul SEGUKOOA
- .ovf pentru formatul fișierului vectorial VRT
- .kmz pentru formatul KML compresat (KMZ)
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 pentru formatele SQLite/Spatialite
- .sl3 pentru formatul SQLite Spatial (FDO)
- CouchDB Spatial (via URL)

**Pentru fIșierele raster:**
- .ovr pentru formatul de fișier raster vrt

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Această metodă va reduce numărul de noduri al geometriilor pe care QGIS trebuie să le descarce de pe server, ceea ce va crește viteza de randare și va economisi lățimea de bandă dintre QGIS și serverul PostgreSQL.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## Gestiunea datelor
### Funcționalitate: Eliminarea plugin-ului SPIT
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Nathan Woodrow
### Funcționalitate: Exportul DXF: opțiunea de a utiliza titlul în loc de nume, ca denumire a stratului DXF în aplicație și server
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Această funcționalitate a fost dezvoltată de Jürgen Fischer
### Funcționalitate: Tipul de geometrie poate fi suprascris în dialogul de salvare a vectorului
Acest lucru face posibilă efectuarea unor lucruri cum ar fi salvarea unui tabel fără geometrie CU un anumit tip de geometrie, astfel încât geometriile să poată fi apoi adăugate manual în rânduri. Anterior, acest lucru a fost posibil în QGIS doar prin recurgerea la relații false, sau la alte trucuri.

În plus, au fost adăugate opțiuni pentru a forța ca fișierul de ieșire să fie de genul multi-tip, sau să includă o dimensiune z.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Joncțiunile vectoriale sunt de acum salvate în interiorul fișierului QLR, cu definițiile stratului
### Funcționalitate: Controlul grafic al Resurselor Externe
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- Puteți defini și seta **calea relativă de stocare**. Aveți posibilitatea de a salva doar acea parte a căii care se află după calea implicită (în cazul în care calea implicită este setată), sau calea proiectului curent. Acest lucru este deosebit de util atunci când doriți să salvați căi lungi în cadrul atributelor cu dimensiuni limitate (cum ar fi atributele de text pentru fișierele shape, care sunt limitate la 254 de caractere), sau pentru crearea de proiecte și fișiere cu arhive de date de sine stătătoare, în scopul distribuirii.
- O altă caracteristică nouă care face controlul mai ușor de utilizat o constituie faptul că **de acum, căile de fișier pot fi afișate sub formă de hiperlegături**. Dacă faceți clic pe hiperlegătură, fișierul respectiv se va deschide direct din QGIS. Aveți posibilitatea să configurați această opțiune, pentru a afișa calea completă a fișierului, sau doar numele fișierului. Fișierul va fi deschis cu ajutorul aplicației implicite, pentru acel format de fișier, configurată în sistemul de operare.
- De asemenea, **puteți utiliza o adresă URL în loc de o cale de fișier**. Controlul o va interpreta ca pe o adresă URL, și va fi capabil de a deschide pagina web respectivă direct în navigatorul web implicit.
- Puteți alege să **selectaţi căile către directoare în locul căilor spre fişiere**.
- Există un **vizualizator de documente integrat** în acest control grafic. Puteți să-l utilizați pentru a afișa imagini sau pagini web direct în QGIS. Selectorul de fișiere al vizualizatorului integrat va beneficia de toate opțiunile menționate mai sus.

Pentru mai multe informații despre opțiunile de configurare, puteți utiliza baloanele cu indicații din caseta de dialog pentru configurare.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Această funcționalitate a fost dezvoltată de**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Funcționalitate: Editarea relației N:M
S-a adăugat posibilitatea de a gestiona datele dintr-o bază de date relațională, normalizată în N:M (mai multe la mai multe) relații. În editorul de relații dintr-un formular, instrumentele necesare pentru a adăuga, șterge, lega și dezlega funcționează, de asemenea, și pe tabela legată, dacă relația cu aceasta este vizualizată ca fiind de tipul N:M.

Configurarea se face în fila câmpurilor, unde pentru o relație poate fi aleasă o a doua relație (în cazul în care există una adecvată).

**Limitări:**

QGIS nu este un sistem de management al bazelor de date.

Acesta face unele presupuneri privitor la sistemul de baze de date. În special:
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Această caracteristică a fost finanțată de către Republica și Cantonul Neuchâtel, Ville de Pully, Ville de Vevey

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Digitizarea
### Funcționalitate: Culoare configurabilă pentru banda elastică
De acum, se pot seta lățimea și culoarea pentru banda elastică folosită la digitizare.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Funcționalitate: Instrument de digitizare prin urmărire
Noul instrument de digitizare prin urmărire reprezintă un instrument avansat, care permite digitizarea entităților dintr-un strat prin urmărirea conturului entităților dintr-un alt strat.

Instrumentul de urmărire:
- uses Dijkstra's shortest path algorithm to find traceable routes
- poate urmări trasee pentru multiple entități distincte
- poate fi utilizat cu instrumente Avansate de Digitizare (cum ar fi reprofilarea)
- poate fi activat și dezactivat prin apăsarea tastei **T** pe durata digitizării
- este rapid și ușor de utilizat

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Această caracteristică a fost finanțată de: The Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Etichetare
### Feature: \"Cartographic\" placement mode for point labels
În acest mod de poziționare, etichetele punctelor sunt generate după reguli ideale de plasare, cartografice, aranjarea etichetelor fiind prioritizată astfel:
- dreapta sus
- stânga sus
- dreapta jos
- stânga jos
- mijloc dreapta
- mijloc stânga
- sus, puțin spre dreapta 
- jos, puțin spre stânga

(în concordanță cu indicațiile din Krygier și Wood (2011), precum și din alte lucrări cartografice de bază)

Prioritatea destinațiilor de plasare poate fi, de asemenea, setată pentru o entitate individuală utilizând o listă de poziții definite cu ajutorul datelor. Acest lucru permite, de asemenea, utilizarea numai a unora dintre destinațiile de plasare, astfel că, în cazul unor entități care reprezintă, de exemplu, coasta marină, ați putea împiedica plasarea etichetelor deasupra solului.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Aplicarea distanței etichetei față de limitele simbolurilor
Când această setare este activă, distanța etichetei se calculează de la limitele simbolului randat pentru un punct. Este deosebit de util atunci când dimensiunea simbolului nu este fixă, cum ar fi în cazul în care dimensiunea este definită cu ajutorul datelor, sau atunci când se utilizează diferite simboluri dintr-un render organizat pe categorii.

Rețineți că această setare este disponibilă numai pentru noul mod, Cartografic, de plasare al etichetei.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Controlul ordinii de randare a etichetelor
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

In plus, logica a fost optimizată, astfel încât, dacă 2 etichete au același z-index, atunci:
- în cazul în care acestea fac parte din același strat, o etichetă mai mică va fi desenată întotdeauna deasupra unei etichete mai mare
- în cazul în care acestea fac parte din diferite straturi, etichetele vor fi desenate în aceeași ordine ca și straturile în sine (de exemplu, respectând ordinea stabilită în legendă)

Diagramelor li se poate stabili, de asemenea, propriul z-index (care nu poate fi definit, totuși, cu ajutorul datelor), astfel încât ordinea etichetelor și a diagramelor poate fi controlată.

Rețineți că acest control *NU* stabilește ca etichetele să fie desenate sub entitățile din alte straturi, ci ordinea în care sunt desenate etichetele deasupra hărții.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Simbolulul de randare actual este de acum considerat drept un obstacol pentru etichetele entităților de tip punct
Anterior, numai entitățile de tip punct erau considerate ca obstacol pentru etichete. În cazul în care pentru punct erau utilizate un simbol sau un decalaj mare, atunci etichetele erau lăsate să se suprapună peste acest simbol, fără a se lua în considerare obstacolul.

De acum, sunt luate în considerare atât dimensiunea reală, cât și decalajul simbolului randat, la momentul în care s-a detectat că o etichetă s-a ciocnit cu un element de tip punct. Drept urmare,  QGIS va evita, în mai multe circumstanțe, desenarea etichetelor peste simbolurile de tip punct.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de City of Uster

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Legenda stratului
### Funcționalitate: Se poate aplica un stil mai multor straturi selectate, sau tuturor straturilor din legenda grupului
Această facilitate adaugă posibilitatea de a aplica stilul unuia dintre straturi, unui grup de straturi sau unor straturi selectate.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Salvatore Larosa
### Funcționalitate: Filtrarea legendei după o expresie
De acum, este posibilă filtrarea elementelor de legendă după o expresie. Acest lucru a fost gândit pentru filtrarea simbologiilor bazate pe reguli sau pe categorii.

Filtrarea legendei este disponibilă în legenda aplicației principale, precum și pentru componentele de legendă ale compozitorului QGIS.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Compozitorul de Hărți
### Funcționalitate: Noi opțiuni pentru filtrarea elementelor de legendă
S-au introdus două noi opțiuni pentru filtrarea elementelor de legendă.

Prima, filtrarea după o expresie, permite utilizatorilor stabilirea unei expresii, pentru filtrarea entităților care trebuie să fie afișate în legendă. Numai simbolurile cu entitatea potrivită vor fi afișate în legendă.

A doua opțiune de filtrare permite legendei compozitorului să fie filtrată, pentru a include numai elementele care sunt conținute în poligonul atlasului curent.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Funcționalitate: Căi suplimentare pentru șabloanele compozitorului
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Nathan Woodrow
### Funcționalitate: Selecție multiplă a compozițiilor din manager
Managerul de compoziții acceptă gestionarea mai multor compoziții în același timp. De acum, puteți deschide sau șterge mai multe compoziții simultan, folosind tasta Ctrl și selectând mai multe compoziții din listă.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Plugin-urile
### Funcționalitate: Sistem de autentificare pentru managerul de plugin-uri
A fost adăugat managerului de plugin-uri suport pentru noul sistem de autentificare. Acest lucru permite utilizatorilor să aplice configurații de autentificare pentru conexiunile către depozitele de plugin-uri, iar administratorilor de sistem să creeze acces autentificat la arhivele și/sau la pachetelor descărcabile de plugin-uri.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Această funcționalitate a fost dezvoltată de Larry Shaffer
## Procesare
### Funcționalitate: Noi algoritmi în 2.14
#### Geoalgoritmi QGIS:
- Netezire: pentru netezirea stratorilor de tip poligon sau linie.
- Inversare direcţie linie.

#### Geoalgoritmi GDAL/OGR:
- gdal2tiles: construiește un director cu plăcuțe TMS, KML-uri și simple navigatoare web.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Funcționalitate: Asigurarea Calității pentru Testele de Unitate
Pentru a garanta stabilitatea pe termen lung a modulului de procesare, a fost introdus un nou cadru de testare.

Geo-algoritmii de procesare sunt rulați după fiecare schimbare adusă codului sursă QGIS, iar rezultatele sunt comparate cu un set de date de control, pentru validarea execuției corecte. În acest fel se obține un feedback imediat cu privire la posibilele regresii.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcționalitate: Îmbunătățiri aduse barei de instrumente
Interfața simplificată a fost eliminată, fiind adăugat un sistem nou, mai ușor de utilizat, pentru gestionarea furnizorilor. Algoritmul de căutare caută, de acum, și  furnizorii care nu sunt activi, sugerând activarea acestora.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Această funcționalitate a fost dezvoltată de Víctor Olaya
### Funcționalitate: Procesarea loturilor se poate salva, deschizându-se, ulterior, cu ajutorul interfeței de prelucrare a loturilor
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Funcționalitate: Dialogul algoritmilor conține mai multe informații
O scurtă descriere este afișată, de acum, împreună cu parametrii algoritmului, făcând ușor de înțeles scopul acestuia.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Funcționalitate: Module v.net GRASS7
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

Algoritmii v.net folosesc adesea un strat vectorial de tip linie (pentru rețea), și un strat de tip punct, care reprezintă nodurile pe care doriți să le utilizați în calcul. Asigurați-vă că utilizați un strat vectorial de tip linie care reprezintă un graf  (muchiile trebuie să fie conectate la vârfuri, fără intersecție între muchii) pentru a evita problemele. De asemenea, puteți utiliza orice atribut al stratului, pentru calcul costurilor (conținutul atributului este utilizat pentru a calcula costul de deplasare de-a lungul liniei).

Mai jos este prezentat un sumar al diferiților algoritmi care au fost incluși în Processing:
- v.net.alloc: Alocă subrețelele din cele mai apropiate centre.
- v.net.allpairs: Calculează cea mai scurtă cale între toate perechile de noduri din rețea
- v.net.arcs: Creează arce dintr-un fișier cu puncte.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: Calculează gradul, centralitatea, încadrarea, apropierea și centralitatea vectorului caracteristic din fiecare nod al rețelei.
- v.net.components: Calculează componentele puternic și slab conectate din rețea.
- v.netconnect: Conectează punctele (nodurile) la cele mai apropiate arce din rețea (adaugând muchii, dacă este necesar).
- v.net.connectivity: Calculează conectivitatea vertecșilor dintre două seturi cu noduri, din rețea.
- v.net.distance: Calculează cea mai scurtă cale din rețea, dintre două seturi cu noduri.
- v.net.flow: Calculează debitul maxim dintre două seturi cu noduri, ale unei rețele.
- v.net.iso: Calculează harta izocronă a rețelei, dintr-un set cu noduri.
- v.net.nodes - Extrage nodurile din rețeaua/graful unui strat.
- v.net.nreports: Oferă informații despre noduri.
- v.net.path: Găsește calea cea mai scurtă dintre două noduri ale unei rețele.
- v.net.report: Oferă informații despre liniile dintr-o rețea.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: Execută construirea grafului de vizibilitate.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programabilitate
### Funcționalitate: S-a reproiectat editorul de expresii
Cu auto salvare

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Funcționalitate: Stocarea în proiect a codului init Python
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Funcționalitate: Noi opțiuni de sortare și filtrare pentru QgsFeatureRequest
QgsFeatureRequest acceptă de acum setarea unei limite maxime pentru numărul de entități returnate. În multe cazuri, această limită este transmisă furnizorului, având ca rezultat creșterea semnificativă a performanței.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Funcționalitate: Opțiuni pentru codul Python din formularele personalizabile
Această funcționalitate adaugă mai multe opțiuni codului Python pentru formularele personalizabile 
- încărcarea din fișier (cu ajutorul controlului grafic pentru selectarea fișierelor)
- încărcarea din mediul de lucru (cum ar fi un plugin sau o funcție de inițializare Python)
- introducerea directă a codului, într-un control grafic de intrare (opțiune nouă)

Opțiunile de configurare, inclusiv codul Python personalizat, introdus în fereastra de dialog, pot fi stocate atât în proiect cât și în setările stilului QML, putând fi exportate/restaurate în/din baza de date.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Funcționalitate: Noi clase PyQGIS în 2.14
### Noi clase de baze
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

### Noi clase GUI
#### Controale grafice reutilizabile:
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

#### Dialoguri reutilizabile:
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGIS Server
### Funcționalitate: Parametrul STARTINDEX în cererea WMS GetFeature
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Funcționalitate: showFeatureCount în GetLegendGraphic
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Această caracteristică are nevoie de un server fals de X.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Funcționalitate: Opțiune de evitare a randării artefactelor, la marginile plăcuțelor
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Funcționalitate: Verificator de configurare, în Proprietățile Proiectului
Pentru a ajuta la configurarea pentru QGIS Server a unui proiect, a fost adăugat un nou verificator de configurare în proprietățile proiectului.

Verificatorul depistează următoarele erori:
- numele duplicate, sau scurte, folosite ca denumiri OWS
- nume OWS nevalide
- lipsă codificărilor pentru straturile vectoriale

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Funcționalitate: Capabilităţi WMS INSPIRE
În proprietățile proiectului, utilizatorul poate:
- să activeze capabilităţile INSPIRE
- să selecteze limba pentru serviciu, de la 24 de limbi oficiale ale UE + 5 limbi regionale
- să aleagă scenariul pentru metadatele serviciului și să specifice parametrii lor

Capabilitățile WMS 1.3.0 reflectă configurația INSPIRE.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Funcționalitate: Adăugarea unor nume scurte pentru straturi, grupuri și proiecte
O serie de elemente au atât un **Name** cât și un **Titlu**. Numele este reprezentat printr-un șir de caractere, care este utilizat pentru comunicarea de-la-mașină-la-mașină, în timp ce titlul este folosit pentru comunicarea între utilizatori. De exemplu, un set de date poate avea Titlul descriptiv *Temperatura Atmosferică Maximă* și să fie solicitat cu ajutorul Numelui abreviat *ATMAX*.

Utilizatorul poate seta deja un titlu pentru straturi și pentru proiect. Numele serviciilor Web OpenGeospatial, OWS (WMS, WFS, WCS) se bazează pe numele utilizat în arborele straturilor. Acest nume este mai mult o etichetă pentru uzul utilizatorului, nicidecum un nume pentru comunicarea de-la-mașină-la-mașină.

Pentru a adăuga utilizatorilor capacitatea de a defini Numele ca pe un șir de caractere pentru comunicarea de-la-mașină-la-mașină, această caracteristică adaugă:
- linii editabile, pentru nume scurte, în proprietățile straturilor
- fereastră de dialog pentru datele WMS în grupul care conține arborele straturilor (nume scurt, titlu, rezumat)
- linii editabile, pentru nume scurte, în proprietățile proiectului
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- un element TreeName în fullProjectSettings

În cazul în care un nume scurt a fost stabilit pentru straturi, grupuri și proiect, acesta va fi utilizat de QGIS Sever pentru numele stratului.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Simbologie
### Funcționalitate: Asistent pentru ajustarea lățimii liniei
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Funcționalitate: Suport pentru transparență în parametrii de culoare SVG
SVG-urile care nu sunt încorporate au nevoie de:

`fill-opacity="param(fill-opacity)"`

și

`stroke-opacity="param(outline-opacity)"`

pentru activarea transparenței.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Duplicarea facilă a straturilor pentru simboluri
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Render 2.5D
S-a adăugat o interfață de configurare și un render care ușurează operațiunile necesare obținerii un efect 2.5D.

Acest lucru permite configurarea unora dintre stiluri, fiind menit să creeze o configurație ușor de utilizat.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Această funcționalitate a fost dezvoltată de**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Această facilitate a fost finanțată de**:
- Consiliul Regional din Picardia
- ADUGA
- Orașul Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Funcționalitate: Este permisă definirea ordinii de randare a entităților
Atunci când este necesară randarea într-o anumită ordine a entităților, acest lucru poate fi specificat cu ajutorul unei expresii arbitrare.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

De asemenea, există control asupra ordinii crescătoare sau descrescătoare, precum și în cazul în care prima sau ultima entitate au valoarea NULL.

În cazul în care este posibil, cererea va fi trimisă bazei de date (acest lucru depinde de complexitatea expresiei și de furnizorul stratului). În cazul în care nu este posibilă transmiterea cererii către baza de date, ordonarea se va efectua pe mașina locală.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

De asemenea, este disponibilă și pentru plugin-uri:

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcționalitate: Simboluri pentru generatorul de geometrie
Simbolurile generatorului de geometrii permit utilizarea motorului de expresii pentru a modifica geometria înainte de randare, sau chiar crearea de noi geometrii în timp ce are loc randarea bazată pe atributele entităților.

Acest lucru poate fi folosit pentru a utiliza toate tipurile de operatori spațiali, cum ar fi buffer, translate, intersect sau extrude, cu parametri bazați numai pe atributele de randare, fără a modifica efectiv datele sursei.
### Exemple
#### Translația unei geometrii
Se utilizează pentru acoperiș, de către renderul 2.5D

    translate( $geometry, 10, 10 )
    
#### Stilul umplerii pentru conturul poligoanelor
Acest lucru generează un poligon care reprezintă conturul poligonului original (Imaginea exemplu)

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
Diversele straturi pentru simboluri pot conține diferite generatoare de geometrii, acest lucru permițând afișarea de versiuni diferite ale unei geometrii, în același timp. Renderul 2.5D servește drept exemplu.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Consiliul Regional Picardy, ADUGA, Orașul Nyon, Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Interfața cu Utilizatorul
### Funcționalitate: Tabela de atribute poate fi actualizată
De acum, este disponibilă opțiunea de reîncărcare a atributelor din tabelul de atribute.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Funcționalitate: Setarea directă a renderului și a clasei de culori pentru simbol, din meniul contextual al legendei,
Deschide un control grafic de tip roată de culoare direct din meniu, ceea ce vă va permite să editați interactiv culoarea unui simbol, fără a fi nevoie să deschideți măcar un singur dialog!

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Editarea simbolurilor legendei direct din arborele straturilor
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Funcționalitate: Afișarea/ascunderea tuturor elementelor din legendă, prin intermediul meniului contextual
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
