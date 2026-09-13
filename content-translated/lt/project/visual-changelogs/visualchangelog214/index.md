---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: projektą
sidebar: true
title: QGIS 2.14 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.14 pakeitimai{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Laidos data: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Ilgalaikė laida**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

LTR laidų tikslas - teikti stabilias ir mažiau besikeičiančias platformas, skirtas didelėms įmonėms ir organizacijoms, kurios nenori rūpintis naudotojų žinių atnaujinimu, mokymo medžiaga ir pan. daugiau nei kartą per metus. LTR sėkmė labiausiai priklauso nuo jūsų - mūsų mylimų naudotojų - mums reikia jūsų palaikymo, kad padėtumėte finansuoti klaidų taisymą ir užtikrinti, kad jūsų palaikymo kontraktuose nurodyta, kad bet kokie klaidų ištaisymai įkeliami ne tik į vystymo, bet ir į LTR šaką.

Jei LTR jums svarbi, prašome apsvarstykite tiesioginį QGIS projekto palaikymą arba įtikinkite savo komercinio palaikymo tiekėją naudoti LTR kaip jūsų įmonės pagrindą, kad visi galėtų pelnytis iš stabilios platformos, kuri pastoviai tobulinama ir atnaujinama. Pastaba kad naudotojams ir įmonėms, kurios mėgsta gyventi priešakyje, ir toliau bus teikiamos mūsų kas keturis mėnesius kuriamos laidos.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Ačiū**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Dabartiniai QGIS rėmėjai
{{<fund type="changelog" >}}
## Bendra
### Savybė: pakeista strpos funkcijos veiksena
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Ankstesnių QGIS versijų projektų failus reikės pakeisti, atsižvelgiant į šį pakeitimą.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Šią savybę sukūrė Jürgen Fischer
### Savybė: priartinti geoobjektą naudojant dešinį paspaudimą atributų lentelėje
Dabar galite priartinti bet kokį geoobjektą iš atributų lentelės (nereikia iš pradžių pažymėti) paspaudę dešinį pelės mygtuką ir parinkę geoobjekto priartinimą.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Savybė: greičio ir atminties naudojimo patobulinimai
- **Pažymėtų geoobjektų įrašymas** iš didelio sluoksnio dabar daug greitesnis
- Tik pažymėtų geoobjektų keitimas **laukų skaičiuotuve** yra greitesnis
- **Greitesnis priartinimas** prie pažymėjimo dideliuose sluoksniuose
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **Kategorijų filtravimas kategorizuotame braižyme** (pavyzdžiui rodant tik kai kurias kategorijas, kitas išmetus) yra daug greitesnis, nes dabar tik atitinkantys geoobjektai ištraukiami iš duomenų tiekėjo
- Didelis **atminties naudojimo sumažinimas** atidarant didelius vektorinius sluoksnius

### Savybė: daugiau išraiškų kintamųjų
Braižymo metu bus galima naudoti naujus kintamuosius:
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Šie naudingi, norint pritaikyti skirtingus stilius skirtingoms kelių dalių geoobjektų dalims:
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

Taipogi pridėti kintamieji, susiję su operacinės sistemos aplinka:
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann (su OS ir naudotoju susiję kintamieji)

Šią savybę sukūrė Nyall Dawson, Matthias Kuhn
### Savybė: geresnis žemėlapių elementų pozicionavimo valdymas
QGIS 2.14 gavo geresnį šiaurės rodyklių, mastelio juostų ir autorinių teisių pozicionavimo žemėlapio drobėje valdymą. Dabar galite tiksliai nurodyti šių elementų poziciją naudojant įvairius vienetus (įskaitant milimetrus, taškus arba procentus).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Savybė: mokama riktų taisymo programa
Prieš kiekvieną laidą, mes vykdomą apmokamą riktų taisymo programą, kurios metu mokame programuotojams, kad jie ištaisytų kiek galima daugiau riktų. Mes nusprendėme pradėti informuoti apie šią programą pakeitimų ataskaitoje. Pastebėtina, kad sąrašas **nėra pilnas**.
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
- Nyall Dawson: Blogas serverio pusės filtravimas OGR, Oracle ir Spatialite sluoksniams
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: Pataisyti problemas su braižymo keitimu į nuo taisyklių priklausantį braižymą
- Nyall Dawson: Pataisyti kategorizuoto braižymo klaidą, kai pakeitimai neįrašomi į išeities simbolį
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: Sutvarkyti laiko reikšmių valdymą atributuose
- Nyall Dawson: Dialogo kortelių rikiuotės pataisymai
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Teisingai apdoroti LongLong laukus atributų suliejimo dialoge
- Nyall Dawson: Sutvarkyti netinkamą skaičiavimo detalių rodymą matavimo įrankio dialoge (buvo netinkamas ir netikslus daugumai CRS/vienetų kombinacijų)
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
Laukų skaičiuotuvą dabar galima naudoti geoobjekto geometrijos atnaujinimui naudojant geometrinės išraiškos rezultatą. Tai patogus būdas atlikti greitus veiksmus, tokius kaip pridėti buferį grupei pažymėtų geoobjektų. Kartu su visomis naujomis 2.14 versijoje pridėtomis geometrijos funkcijomis taip labai patogu valdyti jūsų geometrijas!

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: Naujos 2.14 išraiškų funkcijos
2.14 versijoje buvo pridėta daug naujų išraiškų funkcijų:
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

Kiti patobulinimai:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Analizės įrankiai
### Savybė: daugiau statistikos ir atributų suliejimo įrankis
Naudojant atributų reikšmių ar geoobjektų suliejimo įrankį, yra papildoma suminė statistika, kurią galima naudoti nustatant gaunamas atributų reikšmes. Tarp tokių funkcijų yra Q1, Q3, tarp-kvartilinių diapazonų, daugumos ir mažumos reikšmės, unikalių reikšmių skaičius bei kitos.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: z/m reikšmės rodomos naudojant identifikavimo įrankį
Identifikavimo įrankis dabar gali rodyti bet kurią z ar m reikšmę, kuri yra identifikuojamuose geoobjektuose. Jei geoobjektas yra linijas ar poligonas, įrankis rodys viršūnės numerį ir x/y/z/m viršūnės, esančios arčiausiai identifikavimo taško. Identifikavimo įrankis dabar taipogi rodo rinkinių dalių skaičių ir dalies numerį.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: suvienytas atstumo ir ploto vienetų bei koordinačių formatų valdymas
QGIS 2.14 skirtingų parinkčių, susijusių su atstumo ir ploto vienetais bei koordinačių rodymu buvo suvienyti, supaprastinti ir perkelti į projekto parinktis. Šis pakeitimas suteikia tokius privalumus:
- Projekto savybėse nurodytas koordinačių formatas naudojimas visur, kur naudotojui rodomos koordinatės, įskaitant identifikavimo įrankio rezultatus bei būsenos juostą.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- Pridėti papildomi ploto vienetai, įskaitant kvadratinius jardus, akrus, hektarus ir kitus.
- Į kampų matavimo įrankį pridėti papildomi kampų vienetai, įskaitant apsisukimus, lanko minutes bei sekundes ir pan.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Šią savybę finansavo QGIS riktų taisymo programa

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Naršyklė
### Savybė: naršyklės patobulinimai
QGIS naršyklė yra failų sistemos, OGC paslaugų ir duomenų bazių jungčių skydelis, leidžiantis jums paprastai įtempti ir numesti bet kokį sluoksnį iš aukščiau paminėtų šaltinių į jūsų žemėlapio drobę (arba į DB tvarkyklės langą). Šioje laidoje pridėtos dvi naujovės:
- **Naršymo skydelyje galima pasirinktinai paslėpti kelius** - tai naudinga norint išvengti šaltinių sąrašo užteršimo, leidžiant fokusuotis į reikiamus aplankus.
- **Įkelti projektus tiesiai iš naršyklės** - dabar galite įtempti ir numest visą projektą į QGIS žemėlapio drobę ir jis bus įkeltas.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Šią savybę sukūrė Nathan Woodrow
## Duomenų tiekėjai
### Savybė: WMS galimybių įrašymas į podėlį
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Šią savybę sukūrė Jürgen Fischer
### Savybė: išplėstas kreivių geometrijos palaikymas
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: geresnis laiko ir datoslaiko laukų valdymas
QGIS 2.14 pagerinos laiko ir datoslaiko laukų tipų valdymą, įskaitant:
- Teisingai valdomi PostgreSQL timestamp laukai
- Išraiškų variklis dabar pilnai palaiko laiko laukus
- Išraiškos kūrėjas dabar rodo peržiūroje skaičiavimo rezultatus datos, laiko, datoslaio ir intervalų skaičiavimams
- Laiko laukai pilnai palaikomi vektoriniuose failų sluoksniuose (priklausomai nuo failo formato), PostgreSQL, MS SQL Server ir laikinuose juodraštiniuose sluoksniuose
- Įrašant sluoksnius į vektorinius failus bus išlaikomi laiko laukai, jei jie palaikomi vektorinio sluoksnio formato (pvz. MapInfo .tab failuose)

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Šią savybę sukūrė Jürgen Fischer, Nyall Dawson
### Savybė: atskirto teksto tiekėjo Z/M palaikymas
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: postgres redagavimo transakcijų grupės
Transakciniam redagavimui pridėta nauja parinktis.

Įjungus šią parinktį
- Visi tos pačios duomenų bazės sluoksniai įdedami į transakcijos grupę
- Kai pirmas grupės sluoksnis pakeičiamas, visiems kitiems taipogi įjungiamas redagavimo režimas
- Pakeitus sluoksnį, visi pakeitimai iš karto siunčiami į duomenų bazę, taip leidžiant iš karto pritaikyti trigerius ir apribojimus
- Patvirtinant vieno transakcijų grupės sluoksnio pakeitimus, patvirtinami visi sluoksniai (patvirtinama duomenų bazės transakcija)
- Kai vieno transakcijų grupės sluoksnio pakeitimai atšaukiami, atšaukiami visų sluoksnių pakeitimai (atšaukiama duomenų bazės transakcija)

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Šiuo metu tai įgyvendinta tik postgres duomenų bazei.

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Savybė: Postgres tiekėjo PKI autentifikacija
QGIS 2.12 versijos pridėta Autentifikacijos tvarkyklės galimybė buvo praplėsta į PostGIS tiekėją. Tai leidžia jungtis prie Postgres naudojant bazinę ar PKI autentifikaciją su prisijungimo duomenimis, saugomais QGIS konfigūracijoje. Nauja Postgres tiekėjo autentifikaciją taipogi galima naudoti ir DB tvarkyklėje.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Šią savybę sukūrė Luigi Pirelli
### Savybė: virtualūs sluoksniai
Dinamines SQL užklausas dabar galima naudoti bet kokio tipo vektoriniams sluoksniams, kurios QGIS gali įkelti, net jei sluoksnio formatas nepalaiko SQL užklausų!

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

Palaikomas SQL dialektas yra SQLite su Spatialite funkcijomis. Užklausose taipogi galima naudoti QGIS išraiškų funkcijas. Užklausoje galima pasiekti bet kokio tipo vektorinius sluoksnius, įskaitant kelis sluoksnius iš skirtingų duomenų tiekėjų darant jungtis.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Savybė: daugiau GDAL ir OGR tiekėjų failų parinkimo failų plėtinių
Vektorinių ir rastro failų skaitymui QGIS naudoja GDAL/OGR bibliotekas. Tai reiškia, kad beveik bet kokį failo formatą, kurį gali atidaryti GDAL ar OGR, galima atidaryti ir tiesiai QGIS. Iki šiandien kai kurie failų plėtiniai nebuvo pridėti į GDAL ar OGR failų parinkimą, dėl to naudotojai tikėjo, kad QGIS negalėjo atverti ar apdoroti tokių failų formatų. Siekiant sumažinti šią problemą, kai kurie nauji plėtiniai buvo pridėti į GDAL ir OGR failų parinkimo filtrus:

**Vektoriniams failams:**
- .thf EDIGEO Prancūzijos kadastro formatas
- .ods OpenDocument LibreOffice skaičiuoklės formatas
- .xls Microsoft Excel formatas
- .xlsx Microsoft Excel OpenXML formatas
- .xml NAS - ALKIS formatas
- .map WAsP formatas
- .pix PCIDSK formatas
- .gtm ir.gtz GPSTrackMaker formatas
- .vfk VFK formatas
- .osm ir .pbf OpenStreetMap formatas
- .sua SUA formatas
- .txt OpenAir formatas
- .xml Planetary Data Systems TABLE formatas
- .htf Hidrografinio perdavimo formatas
- .svg SVG formatas
- .gen ARCGEN
- .sxf Storage ir eXchange formatai
- .pdf Geoerdvinio PDF vektorinis formatas
- .sgy ir .segy SEG-Y formatas
- .seg, .seg1, .sp1, .uko, .ukooa SEGUKOOA formatas
- .ovf VRT vektorinio failo formatas
- .kmz suspaustas KML (KMZ) formatas
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 SQLite/Spatialite formatas
- .sl3 SQLite erdvinis (FDO) formatas
- CouchDB Spatial (per URL)

**Rastro failams:**
- .ovr vrt rastro failų formatas

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Šis metodas sumažins skaičių geometrijos viršūnių, kurias QGIS turi atsisiųsti iš serverio, tai pagerins braižymo greitį ir sutaupys pralaidumą tarp QGIS ir PostgreSQL serverio.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## Duomenų valdymas
### Savybė: SPIT priedo pašalinimas
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Šią savybę sukūrė Nathan Woodrow
### Savybė: DXF eksportas: galimybė naudoti pavadinimą vietoje vardo kaip DXF sluoksnio vardą aplikacijoje ir serveryje
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Šią savybę sukūrė Jürgen Fischer
### Savybė: Geometrijos tipą galima permušti vektoriaus įrašymo dialoge
Taip paprasčiau daryti tokius dalykus kaip įrašyti geometrijos neturinčias lenteles SU geometrijos tipu, kad geometrijas vėliau būtų galima pridėti rankiniu būdu. Anksčiau tai buvo įmanoma padaryti tik su QGIS naudojant netikrus sujungimus ir kitus apėjimus.

Papildomai pridėtos parinktys priverstinai nurodyti išvesties failui būti multi tipo ar įtraukti z-dimensiją.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: vektoriniai sujungimai dabar įrašomi į QLR sluoksnių apibrėžimų failus
### Savybė: išorinių resursų valdiklis
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- Jūs galite apibrėžti ir nustatyti **santykinio kelio saugojimą**. Santykinio kelio saugojimas leis jums įrašyti tik dalį kelio, einantį po numatytojo kelio (jei numatytasis kelias įvestas) arba dabartinio projekto kelio. Tai ypač naudinga, kai norite įrašyti ilgus kelius į riboto dydžio atributus (pavyzdžiui Shape failų teksto atributus, kurie riboti 254 simboliais), arba kai kuriate tik nuo savęs priklausantį projektą su duomenų failų archyvu paruoštu platinimui.
- Kita nauja savybė, palengvinanti valdiklio naudojimą, yra tai, kad **failų kelius dabar galima rodyti kaip nuorodas**. Paspaudus nuorodą QGIS atvers susietą failą. Jūs galite konfigūruoti šią parinktį, kad būtų rodomas pilnas arba tik failo pavadinimas. Failas bus atidarytas naudojant numatytąjį failo valdymą priklausomai nuo formato nustatymų jūsų operacinėje sistemoje.
- Taipogi galite **naudoti URL vietoje failo kelio**. Valdiklis interpretuos jį kaip URL ir jūs galėsite atverti susijusį puslapį tiesiai jūsų numatytoje naršyklėje.
- Jūs galite pasirinkti **saugoti aplanko kelią vietoje failo kelio**.
- Šiame valdiklyje yra ir **integruota dokumentų žiūryklė**. Jūs galite ją naudoti, jei norite tiesiai QGIS rodyti nuotraukas ar puslapius. Integruotos žiūryklės failų parinkiklis geriau veiks dėl visų šių paminėtų savybių.

Daugiau informacijos apie konfigūravimo parinktis galite rasti konfigūracijos dialogo patarimuose, rodomuose užvedus pelę ant atitinkamo elemento.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Šią savybę sukūrė**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Savybė: N:M ryšių redagavimas
Pridėta galimybė tvarkyti duomenis normalizuotuose reliacinėse duomenų bazėse N:M (daug su daug) ryšiuose. Ryšių redaktoriaus formoje įrankiai pridėti, trinti, susieti ir nebesusieti veikia ir susiejant lenteles, jei ryšys vizualizuotas kaip N:M ryšys.

Konfigūruojama laukų kortelėje, kur prie ryšio galima parinkti antrą ryšį (jei yra tinkamas ryšys, atsižvelgiant į antrą ryšį susiejimo lentelėje).

**Apribojimai:**

QGIS nėra duomenų bazių valdymo sistema.

Daroma prielaida apie duomenų bazės sistemą. Tiksliau:
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Šią savybę finansavo République et canton de Neuchâtel, Ville de Pully, Ville de Vevey

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Skaitmeninimas
### Savybė: Konfigūruojama gumelės spalva
Dabar galite nurodyti gumelės, kuri naudojam skaitmeninant, plotį ir spalvą.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Savybė: sekimo skaitmeninimo įrankis
Naujas sekimo skaitmeninimo įrankis yra išmanus skaitmeninimo įrankis, kuris leidžia jums skaitmenizuoti geoobjektus viename sluoksnyje sekant kito sluoksnio geoobjektus.

Sekimo įrankis:
- uses Dijkstra's shortest path algorithm to find traceable routes
- gali sekti maršrutus per kelis skirtingus geoobjektus
- gali būti naudojamas su Sudėtingesniu skaitmenizavimo įrankiu (pvz. keičiant formą)
- gali būti įjungtas ir išjungtas paspaudus **T** skaitmeninimo metu
- yra greitas ir paprastas naudoti

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Šią savybę finansavo: The Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Užrašai
### Feature: \"Cartographic\" placement mode for point labels
Šis vietos nustatymo režimas taškų užrašų kandidatus kuria pagal idealias kartografines vietos taisykles, t.y. užrašų vietos prioritetizuojamos tokia seka:
- viršuje dešinėje
- viršuje kairėje
- apačioje dešinėje
- apačioje kairėje
- per vidurį dešinėje
- per vidurį kairėje
- viršuje, šiek tiek dešiniau
- apačioje, šiek tiek kairiau

(pagal Krygier ir Wood (2011) ir kitų kartografijos ekspertų darbų gaires)

Vietos prioritetą taipogi galima nurodyti ir konkrečiam geoobjektui naudojant nuo duomenų priklausantį prioritetizuotų pozicijų sąrašą. Tai taipogi leidžia naudoti tik kai kurias pozicijas, pavyzdžiui kranto objektams jūs galite neleisti užrašus dėti virš žemės.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: užrašo atstumo nuo simbolio ribų taikymas
Įjungus šį nustatymą, užrašo atstumas skaičiuojamas nuo braižomo taško simbolio kraštų, o ne paties taško. Tai ypač naudinga, kai simbolio dydis kinta, t.y. kai jis nustatomas priklausomai nuo duomenų ar kai naudojami skirtingi simboliai kategorizuotame braižyme.

Pastebėtina, kad šis nustatymas galimas tik naujame kartografiniame taško užrašo pozicijos režime.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: užrašų braižymo rikiuotės valdymas
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

Papildomai buvo pakeista logika, kad jei 2 užrašai turi tą patį z-indeksą, tai:
- jei jie yra iš to paties sluoksnio, mažesnis užrašas visada bus braižomas virš didesniojo
- jei jie yra iš skirtingų sluoksnių, tai užrašai bus braižomi tokia pačia tvarka kaip ir sluoksniai (t.y. bus atsižvelgiama į legendoje nurodytą rikiuotę)

Diagramoms taipogi galima nurodyti z-indeksą (bet ne nuo duomenų priklausantį), kad būtų valdoma užrašų ir diagramų rikiuotė.

Pastebėtina, kad tai *NEleidžia* braižyti užrašų po kitų sluoksnių geoobjektais, tik valdo užrašų braižymo ant jūsų žemėlapio rikiuotę.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: taškinių geoobjektų užrašų kliūtimi laikomas realus braižomas simbolis
Anksčiau užrašų kandidatų kliūtimis buvo laikomi tik patys taškiniai geoobjektai. Jei taškui buvo naudojamas didelis ar pasislinkęs simbolis, tai užrašams buvo leidžiama dengti šį simbolį nesukeliant jokios kliūties kainos.

Dabar nustatant ar užrašas kertasi su taškiniu geoobjektu, tikrinamas realus braižomo simbolio dydis ir poslinkis. Rezultate QGIS dabar dauguma atveju vengia braižyti užrašus virš taškų simbolių.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Šią savybę finansavo City of Uster

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Sluoksnių legenda
### Savybė: įkelti stilių keliems pažymėtiems sluoksniams ar visiems legendos grupės sluoksniams
Ši savybė prideda galimybę įkelti vieno sluoksnio stilių sluoksnių grupei ar pažymėtiems sluoksniams.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Šią savybę sukūrė Salvatore Larosa
### Savybė: filtruoti legendą pagal išraišką
Dabar galima filtruoti legendos elementus naudojant išraišką. Funkcionalumas sukurtas galvojant apie taisyklėmis paremto ir kategorizuoto simbolizavimo filtravimą.

Legendos filtravimas galimas pagrindinės aplikacijos legendoje bei QGIS maketuotojo legendos komponente.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Žemėlapio maketas
### Savybė: naujos galimybės filtruoti legendos elementus
Pristatytos dvi naujos legendos elementų filtravimo parinktys.

Pirmoj - filtravimas išraiška - leidžia naudotojams nustatyti išraišką, skirtą legendoje rodomų geoobjektų filtravimui. Legendoje bus rodomi tik atitinkančių geoobjektų simboliai.

Antroji filtro parinktis leidžia maketo legendos filtre įtraukti tik elementus, kurie yra dabartinio atlaso poligone.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Savybė: papildomi maketo šablonų keliai
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Šią savybę sukūrė Nathan Woodrow
### Savybė: galimybė tvarkyklėje parinkti kelis maketus
Maketu tvarkyklė gavo galimybę valdyti kelis maketus vienu metu. Dabar jūs galite atidaryti ar ištrinti kelis maketus iš karto, laikydami Ctrl mygtuką kol pažymite sąraše kelis maketus.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Priedai
### Savybė: autentifikacijos sistemos palaikymas priedų tvarkyklėje
Naujos autentifikacijos sistemos palaikymas pridėtas į priedų tvarkyklę. Tai leidžia naudotojams taikyti autentifikacijos konfigūracijas jungtims į priedų repozitorijas, o sistemos administratoriams sukurti autentifikuotas prieigas prie priedų repozitorijų ir/arba priedų paketų atsiuntimo.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Šią savybę sukūrė Larry Shaffer
## Apdorojimas
### Savybė: nauji 2.14 algoritmai
#### QGIS geo algoritmai:
- Glotninti: linijų ar poligonų sluoksnių glotninimas.
- Apsukti linijos kryptį.

#### GDAL/OGR geo algoritmai:
- gdal2tiles: sukuria aplanką su TMS kaladėlėmis, KM ir paprasta žiniatinklio žiūrykle.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Savybė: Unit testai ir kokybės užtikrinimas
Apdorojimo modulio ilgalaikio stabilumo garantavimui buvo pridėtas naujas testavimo karkasas.

Apdorojimo geo algoritmai vykdomi po kiekvieno pakeitimo, kuris kliudo QGIS išeities kodą, o rezultatai lyginami su kontroline duomenų aibe, taip garantuojant teisingą elgseną. Tai leidžia nedelsiant gauti informaciją apie galimas regresijas.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Savybė: pagerinta įrankinė
Supaprastina naudotojo sąsaja buvo išimta, o pridėta nauja ir labiau draugiška naudotojui tiekėjų valdymo sistema.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Šią savybę sukūrė Víctor Olaya
### Savybė: paketinius darbus dabar galima įrašyti ir vėliau atstatyti naudojant paketinio darbo sąsają
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Savybė: informatyvesnis algoritmų dialogas
Greta algoritmo parametrų rodomas ir trumpas aprašymas, taip palengvinant algoritmo tikslo supratimą.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Savybė: GRASS7 v.net moduliai
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

v.net algoritmai dažnai naudoja vektorinį linijų sluoksnį (tinklui) ir taškų sluoksnį, kuriame yra viršūnės, kurias norite naudoti skaičiavimuose. Kad išvengtumėte problemų, įsitikinkite, kad tinklui naudojate tikrą linijų grafo sluoksnį (kraštinės turi būti sujungtos viršūnėse be tarpų tarp jų). Taipogi galite naudoti bet kokį tinklo sluoksnio atributą kainos skaičiavimui (atributo turinys naudojamas skaičiuojant kelionės kraštine kainą).

Žemiau pateikta greita skirtingų į apdorojimą pridėtų algoritmų santrauka:
- v.net.alloc: paima potinklius iš artimiausių centrų.
- v.net.allpairs: skaičiuoja trumpiausią kelią tarp visų tinklo taškų porų.
- v.net.arcs: sukuria lankus iš taškų failo.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: skaičiuoja kiekvienos tinklo viršūnės laipsnį, centriškumą, tarpiškumą, artumą ir eigen vektoriaus centriškumą.
- v.net.components: skaičiuoja stipriai ir silpnai sujungtus tinklo komponentus.
- v.net.connect: sujungia taškus (viršūnes) su artimiausiu tinklo lanku (ir, jei reikia, prideda kraštines).
- v.net.connectivity: skaičiuoja viršūnių jungumą tarp dviejų tinklo viršūnių aibių.
- v.net.distance: skaičiuoja trumpiausią kelią tinklu tarp dviejų viršūnių aibių.
- v.net.flow: Skaičiuoja maksimalų srautą tarp dviejų tinklo viršūnių aibių.
- v.net.iso: skaičiuoja tinklo izochronių žemėlapį pagal viršūnių aibę.
- v.net.nodes: ištraukia tinklo/grafo sluoksnio viršūnes.
- v.net.nreports: praneša informaciją apie viršūnes.
- v.net.path: randa trumpiausią kelią tinkle tarp dviejų viršūnių.
- v.net.report: praneša informaciją apie tinklo kraštines.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: vykdo matomumo grafo konstrukciją.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programavimas
### Savybė: išraiškų funkcijų redaktoriaus perkūrimas
Su automatiniu įrašymu

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Savybė: python inicializacijos kodas įrašomas į projektą
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Savybė: naujos QgisFeatureRequest filtravimo ir rikiavimo parinktys
QgsFeatureRequest dabar leidžia nurodyti maksimalų grąžinamų geoobjektų skaičių. Dauguma atveju šis apribojimas perduodamas tiekėjui, o tai leidžia stipriai pagerinti greitaveiką, nes reikia grąžinti tik poaibį geoobjektų.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Savybė: python savo geoobjekto kodo galimybės
Pridėta daugiau galimybių Pythono kodo savam geoobjektui:
- įkelti iš failo (su failų parinkimo valdikliu)
- įkelti iš aplinkos (pvz. priedo ar Python init funkcijos)
- tiesiogiai įvesti kodą įvesties valdiklyje (nauja parinktis)

Konfigūracijos parinktys, įskaitant savo python kodą įvestą dialoge ir įrašytą projekte bei kaip stiliaus QML nustatymai, kurie gali būti eksportuojami/atstatomi iš DB.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Savybė: naujos 2.14 PyQGIS klasės
### Naujos bazinės klasės
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

### Naujos GUI klasės
#### Perpanaudojami valdikliai
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

#### Perpanaudojami dialogai:
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGIS Serveris
### Savybė: WFS GetFeature užklausos parametras STARTINDEX
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Savybė: GetLegendGraphic užklausos parametras showFeatureCount
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Šiai savybei reikia netikro X server.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Savybė: parinktis vengti liekanų braižymą kaladėlių kraštuose
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Savybė: konfigūracijos tikrinimas projekto savybėse
Siekiant padėti sukonfigūruoti projektą QGIS Serveriui, projekto savybėse pridėtas naujas konfigūracijos tikrinimas.

Tikrinamos tokios klaidos:
- OWS vardų pasikartojimai ar trumpi pavadinimai
- netinkami OWS vardai
- trūkstamos vektorinių sluoksnių koduotės

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Savybė: WMS INSPIRE galimybės
Projekto savybėse naudotojas gali:
- aktyvuoti INSPIRE galimybes
- parinkti paslaugos kalbą iš 24 ES oficialių kalbų + 5 regioninių kalbų
- parinkti paslaugos metaduomenų scenarijų ir nurodyti jo parametrus

WMS 1.3.0 galimybės atspindi INSPIRE konfigūraciją.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Savybė: pridėti trumpą pavadinimą sluoksniams, grupėms ir projektui
Keli elementai turi tiek **Pavadinimą**, tiek ir **Antraštę**. Pavadinimas yra tekstinė eilutė, kuri naudojama bendravimui tarp mašinų, o antraštė yra rodoma žmonėms. Pavyzdžiui duomenų aibė gali turėti aprašomąją antraštę *Maksimali atmosferinė temperatūra* ir būti užregistruota su trumpu vardu *ATMAX*.

Naudotojai jau gali nurodyti sluoksnių ir projektų antraštes. OpenGeospatial Web Services, OWS (WMS, WFS, WCS), pavadinimas paremtas sluoksnio medyje naudojamu pavadinimu. Šis pavadinimas labiau skirtas žmonėms, nei bendravimui tarp mašinų.

Pridedant galimybę naudotojams nurodyti vardą kaip trumpą teksto eilutę, skirtą bendravimui tarp mašinų, ši savybė prideda:
- trumpo vardo lauką sluoksnio savybėse
- WMS duomenų dialogą sluoksnio medžio grupėse (trumpas pavadinimas, antraštė, aprašymas)
- trumpo vardo laukas projekto savybėse
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- TreeName elementas įdėtas į fullProjectSettings

Jei sluoksniams, grupėms ir projektui nurodytas trumpas vardas, jis naudojamas QGIS Serverio kaip sluoksnio pavadinimas.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Simbologija
### Savybė: dydžio padėjėjas kintančiam linijos pločiui
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Savybė: SVG spalvų parametrų permatomumo palaikymas
Nesupakuotuose SVG reikia pridėti:

`fill-opacity="param(fill-opacity)"`

and

`stroke-opacity="param(outline-opacity)"`

kad įjungtumėte permatomumo palaikymą.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: lengvas simbolinių sluoksnių dubliavimas
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: 2.5D braižymas
Tai prideda konfigūracijos sąsają ir braižymą, leidžianti paprastai sudėti visas dalis, kurių reikia norint gauti 2.5D efektą.

Jis leidžia konfigūruoti dalį stiliaus ir skirtas kurti lengvai naudojamus nustatymus.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Šią savybę sukūrė**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Šią savybę finansavo**:
- Regional Council of Picardy
- ADUGA
- Ville de Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Savybė: leisti apibrėžti geoobjektų braižymo rikiavimą
Kai reikia geoobjektus braižyti kažkokia konkrečia rikiuote, tai galima padaryti naudojant išraišką.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

Tai taipogi leidžia valdyti ar rikiuojama didėjančia ar mažėjančia tvarka bei ar NULL turi būti priekyje ar pabaigoje.

Jei įmanoma, užklausa bus nusiųsta į duomenų bazę (priklauso nuo išraiškos sudėtingumo bei nuo sluoksnio tiekėjo). Jei užklausos į duomenų bazę nusiųsti neįmanoma, rikiavimas bus vykdomas lokalioje mašinoje.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

Tai taipogi veikia ir priedams:

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Savybė: geometrijos generatoriaus simboliai
Geometrijos generatoriaus simboliai leidžia naudoti išraiškų variklį modifikuojant geometriją prieš braižymą ar net sukuriant naujas geometrijas braižant priklausomai nuo geoobjekto atributų.

Tai gali naudoti įvairiausias erdvines operacijas, tokias kaip buferį, vertimą, susikirtimą ar išsikišimą su parametrais, priklausančiais nuo atributų ir tik braižymui, nekeičiant pačių duomenų šaltinyje.
### Pavyzdžiai
#### Versti geometriją
Naudojama 2.5D braižymo metu stogui

    translate( $geometry, 10, 10 )
    
#### Pildymo stilius poligono kontūrui
Tai sukuria poligoną, kuris reprezentuoja pradinio poligono kontūrą (Pavyzdinė nuotrauka)

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
Skirtingi simbolių sluoksniai galit turėti skirtingus geometrijos generatorius, tai leidžia rodyti skirtingas geometrijos versijas tuo pačiu metu. 2.5D braižymas yra šito pavyzdys.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Šią savybę finansavo Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Naudotojo sąsaja
### Savybė: atributų lentelę galima atnaujinti
Atributų lentelėje pridėta galimybė iš naujo įkelti atributus.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Savybė: legendos kontekstiniame meniu tiesiogiai nurodyti braižymo ir klasės simbolio spalvą
Rodo meniu spalvų rato valdiklį, kuris leidžia jums interaktyviai keisti simbolio spalvą net neatidarant jokio dialogo!

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: keisti legendos simbolius tiesiai sluoksnių medyje
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Savybė: rodyti/slėpti visus legendos elementus per kontekstinį meniu
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
