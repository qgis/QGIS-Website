---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: projekt
sidebar: true
title: A QGIS 3.0 változásnaplója
type: visual-changelog

---
{{<content-start >}}
# A QGIS 3.0 változásnaplója{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

Release date: 2018-02-23

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**Köszönet**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

A QGIS szabad szoftver és semmi sem kötelezi arra, hogy fizessen használatáért. Valójában a QGIS használatára bátorítjuk az embereket, legyenek bárhol a világon, pénzügyi és társadalmi helyzettől függetlenül. Úgy hisszük azzal, hogy térbeli  döntéstámogatási eszközöket adunk az emberek kezébe, annak jobb társadalom építő ereje van az egész emberiségre nézve.

{{<table-of-contents >}}
## QGIS 3.0.0 szponzorai
{{<fund type="changelog" relativeImgPath=true >}}
### Funkció: dxf2shp konvertáló modul eltávolítása
Ez a funkcionalitás rendelkezésre áll az OGR-ben és nincs többé szükség egy külön QGIS modulra a feladat megoldásához
### Funkció: Az elárvult oracle raszter modul eltávolítása
### Funkció: TauDEM szolgáltató eltávolítása az alap feldolgozásból
A TauDEM egészen speciális eszközök készlete, mely néhány további eszköz telepítését igényli. Így elhatároztuk, hogy külön szolgáltatóba tesszük, az alap kódbázis méretét és a karbantartási erőfeszítéseket csökkentendő.
### Funkció: Több súgó és a QGIS súgó fájlok helye konfigurálható
Több Súgó gomb az algoritmusokhoz és a párbeszédablakokhoz és most az online QGIS dokumentációra mutat.

A konfiguráció lehetővé teszi a környezetfüggő súgó elérését az online tároltból, a szervezet hálózatán vagy a helyi számítógépen. A különböző súgó forrásokat kombinálhatjuk.

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Kép, Webnézet és Fájlnév vezérlők átemelése a Csatolás vezérlőbe
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### Funkció: otb és lidartools szolgáltatók eltávolítása a feldolgozásból
Az új logika az lesz, hogy modul szolgáltatókat fejlesszünk, mely képes lesz a külső szoftver életciklusát követni.
## Felhasználói felület
### Funkció: Füles lebegő panelek
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### Funkció: Finom felbontású egér görgő nagyítás támogatása
Néhány egér/mutató eszköznek (különösen mac-en) finomabb felbontása van. Ezek az egér görgő eseményeket sűrűbben, de kisebb értékkel küldik. Ilyen eszközzel használhatatlan a gyors nagyításművelet. Ezt kijavítottuk a 3.0 verzióben

Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: gyors billentyűk párbeszédablakhoz keresés sort tettek
Támogatja a művelet név és gyors billentyű szerinti keresést

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Keresősáv
A keresősáv egy gyors, mindig készen álló, általános és bővíthető keresőeszköz a QGIS bal alsó sarkában.

Jelenleg algoritmusokat, műveleteket és rétegneveket lehet keresni, de ki is lehet választani egy elemet az éppen aktív rétegből egy attribútum érték gépelésével.

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

Ezt a funkciót Nyall Dawson fejlesztette
### Funkció: Több nem-blokkoló, folyamatos szerkesztés
- térkép egység méretezés
- color brewer és korlátozott véletlenszerű színskála szerkesztők
- a színlistában található színek folyamatos szerkesztése a stílus panelben
- az összeálításban található színek és szimbólumok folyamatos szerkesztése

most már mindig jelen van a stílus panelban
### Funkció: Opció hozzáadása a felhasználói színséma menük megjelenítéséhez
A felhasználónak lehetősége van arra, hogy az egyénileg létrehozott színsémája megjelenhessen a szín gomb legördülő menüjében.

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

Ez hasznos, ha egyszerű színkészletei vannak és közvetlenül el akarja érni azokat a szín menüben.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Szín beállítása a térképvászon észak jel dekorációjához
Szín beállitási lehetőség lett hozzáadva az összes térképvászon észak jel dekorációjához.

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

Ezt a funkciót Andreas Neumann támogatta (részleges támogatás)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: nyitott panelek láthatóságának ki-, bekapcsolása a fő ablakban
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Javított felhasználói felület egységesség
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- Az összes API **átlátszóság/átlátszatlanság/alfa** a **setOpacity()** és **opacity()** szerint szabványosítva lett. Az eljárás kettős értéket vesz föl 0 (átlátszó) és 1 (átlátszatlan) között, megőrizve a következetességet a  Qt API-val.
- Egy **új QgsOpacityWidget vezérlő** lett létrehozva, és most már bárhol használható a felhasználói felületben, ahol az átlátszatlanság beállítható. Ez biztosítja a következetes viselkedést, és az átlátszatlanság ellenőrzése mindenhol megegyezik.
- A **Forgatás** szabványosítva lett az API-ban és a Felhasználó felületben, tehát most már a forgatás mindig az óramutató járásával megegyező irányban lesz alkalmazva. Minden forgatás vezérlő frissítve lett, így -360 és 360 közötti értékeket fogadnak el.
- A 2.x verziójú projektek megadott és adatvezérelt forgatással rendelkező címkéi átláthatóan **frissítve** lesznek a 3.0 megnyitásakor.
- A méretarány API-k egységessé lettek téve a QGIS API-n keresztül. **Az összezavaró méretarány nevező és a valódi méretarány keveréke el lett távolítva**, most már minden a méretarány nevezővel működik. Az összes méretarány tartomány hívás viselkedése szabványosítva lett a min/max általános jelentéséhez (és az erre vonatkozó kifejezett API dokumentációhoz).
- Most már minden méretarány szabályozás egységesen a szabványos méretarány vezérlőt használja a felhasználói felületen keresztül
- A címkézés most már ugyanazt a meghatározást használja a min/max méretarányhoz, mint a felhasználói felület rész, és a meglévő projektek átláthatóan frissítve lesznek a 3.0 verzió megnyitásakor.
- Javítva lettek a legelterjedtebb hibák, amelyek a méretarány használathoz kapcsolódnak, beleértve azokat a hibákat, amelyek megtörték a szabály alapú méretarány korlátozásokat

Köszönet illeti meg a QGIS PSC-t és a projekt adományozókat a munka szponzorálásáért és hogy lehetővé teszik a folytatást! 

Ezt a funkciót támogatta: a QGIS Támogatói és Adományozói

This feature was developed by [Nyall Dawson](https://north-road.com)
### Funkció: Rétegek megnyitása és betöltése egyetlen csoportba
Ha sok alréteget akár megnyitni, most már be tudja ezeket tölteni a jelmagyarázat ugyanazon csoportjába.

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## 3D funkciók
### Funkció: 3D térkép megjelenítés és terep generálás
Egy teljesen új natív 3D térképnézetünk van a QGIS-ben! A 3D-s térképnézet 2D-s térképet jelenít meg (a projekt rétegeiból) a terepen. Alapértelmezés szerint a terep egy sík sík, de egy  digitális domborzatmodellt tartalmazó raszter réteget használhatunk a magassági adatok forrásaként.

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- középső gomb nyomvatartásával húzza az egeret
- a Shift billentyű és a bal egérgomb nyomvatartásával húzza az egeret
- a Shift nyomvatartása mellett a fel/le/bal/jobb nyíl billentyűk megnyomása

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Funkció: 3D megjelenítés a térkép rétegekre
Az alapértelmezett konfigurációban a térképrétegek 2D-s térképként jelennek meg a terepen. A 3D-s világ jobb kihasználása azonban lehetséges, ha 3D-s megjelenítőket konfigurálja az egyes térképrétegekhez. 3D-s megjelenítőkkel az adatok 3D-s nézetekként valós 3D objektumokként jeleníthetők meg - ez jelenleg vektoros rétegek esetén támogatott (minden geometria típusra - pont, törtvonal vagy felület). Ez sokkal jobb megjelenítést tesz lehetővé, például:
- az épületek körvonalaival ellátott felületek (adott esetben az adatvezérelt magassággal) kihúzhatóak úgy, hogy azok 3 dimenziósnak tűnjenek
- a fák pont helyzeteivel ellátott pontokat meg lehet jeleníteni a fák 3D-s szimbólumaival is (egyszerű geometriai alakzatokat vagy meglévő 3D-s modelleket lehet betölteni a támogatott fájl formátumból)

A 3D megjelenítés beállításához a rétegstílus rögzített vezérlője vagy a vektor réteg tulajdonságok párbeszédablaka használható - itt egy új fül található a 3D megjelenítés beállításához.

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Kifejezések
### Funkció: Új kifejezés változók
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
Visszaadja a QGIS által használt aktuális terület és nyelv beállítását. Alapértelmezésnél ez a rendszer által használt terület és nyelv beállítása. Ha a felhasználó engedélyezi a területi és nyelvi beállítások felülbírálását a QGIS beállításaiban, akkor a felülbírált területi és nyelvi beállítás lesz visszaadva. 

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Új kifejezés változók a térkép beállításokhoz
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új függvények a kifejezésekhez
**Atlasz kifejezések**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**Összesítő kifejezések**
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

**Tömb kifejezések**

New group that contains expression functions for the creation and manipulation of arrays (also known as list data structures). The order of values within the array matters, in contrary to the \'map\' data structure, where the order of key-value pairs is irrelevant and values are identified by their keys.
- **array(value1, value2, ...)** : Returns an array containing all the values passed as parameter.
- **array_append(array, value)**: Returns an array with the given value added at the end.
- **array_cat(array1, array2, ...)**: Returns an array containing all the given arrays concatenated.
- **array_contains(array, value)**: Returns true if an array contains the given value.
- **array_distinct(array)**: Returns an array containing distinct values of the given array.
- **array_find(array, value)**: Returns the index (0 for the first one) of a value within an array. Returns -1 if the value is not found.
- **array_first(array)**: Returns the first value of an array.
- **array_get(array, index)**: Returns the Nth value (0 for the first one) of an array.
- **array_insert(array, pos, value)**: Returns an array with the given value added at the given position.
- **array_intersect(array1, array2)**: Returns true if any element of array1 exists in array2.
- **array_last(array)**: Returns the last value of an array.
- **array_length(array)**: Returns the number of elements of an array.
- **array_prepend(array, value)**: Returns an array with the given value added at the beginning.
- **array_remove_all(array, value)**: Returns an array with all the entries of the given value removed.
- **array_remove_at(array, pos)**: Returns an array with the given index removed.
- **array_reverse(array)**: Returns the given array with array values in reversed order.
- **array_slice(array, start_pos, end_pos)**: Returns a portion of the array. The slice is defined by the start_pos and end_pos arguments.
- **array_to_string(array, delimiter, empty_value)**: Concatenates array elements into a string separated by a delimiter using and optional string for empty values.
- **regexp_matches(string, regex, empty_value)**: Returns an array of all strings captured by capturing groups, in the order the groups themselves appear in the supplied regular expression against a string.
- **string_to_array(string, delimiter, empty_value)**: Splits string into an array using supplied delimiter and optional string for empty values.

**Szín kifejezések**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**Dátum és idő kifejezések**
- **epoch(date)**: A UNIX kezdőidő (1970.01.01. 00:00) és az adott dátum között eltelt időt adja vissza milliszekundumban.

**Általános kifejezések**
- **env(name)**: Egy környezeti változót vesz fel és a tartalmát karakterláncként adja vissza. Ha a változó nem található, akkor NULL értéket ad vissza.
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

**Geometria kifejezések**
- **extend(geometry, start_distance, end_distance)**: Extends linestrings by a specified amount at the start and end of the line
- **hausdorff_distance(geometry a, geometry b, densify_fraction)**: Returns the Hausdorff distance between two geometries. This is basically a measure of how similar or dissimilar 2 geometries are, with a lower distance indicating more similar geometries.
- **inclination(inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.
- **make_circle(center, radius, segment)**: Creates a circular, segmentized, polygon.
- **make_ellipse(center, semi_major_axis, semi_minor_axis, azimuth, segment)**: Creates an elliptical, segmentized, polygon.
- **make_regular_polygon(center, radius, number_sides, circle)**: Creates a regular polygon.
- **make_triangle()**: help still missing
- **minimal_circle(geometry, segment)**: Returns the minimal enclosing circle of a geometry. It represents the minimum circle that encloses all geometries within the set.
- **offset_curve(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by offsetting a linestring geometry to the side. Distances are in the Spatial Reference System of this geometry.
- **oriented_bbox(geom)**: Returns a geometry which represents the minimal oriented bounding box of an input geometry.
- **pole_of_inaccessibility(geometry, tolerance)**: Calculates the approximate pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance.
- **simplify(geometry, tolerance)**: Egyszerűsít egy geometriát a csomópontok eltávolításával, távolság alapú küszöb használatával (azaz Douglas Peucker algoritmus). Az algoritmus megőrzi a geometria nagy eltéréseit és csökkenti a töréspontok számát a majdnem egyenes szakaszokban.
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

**Réteg tulajdonságok**
- **crs_description** returns the CRS description of the layer.

**Térkép kifejezések**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**Térkép rétegek**

Új csoport, ami tartalmazza az aktuális projektben rendelkezésre álló térkép rétegek listáját. Visszaadja a belső térkép réteg azonosítókat. Ezt számos más kifejezés függvényben használható, amelyek a térkép rétegekre hivatkoznak.

**Matematikai kifejezések**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**Műveletek**
- **\~:** Performs a regular expression match on a string value.

**Rekord és attribútum kifejezések**

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- **uuid()**: Univerzális egyedi azonosító (UUID) generálása minden sorhoz a Qt QUuid::createUuid módszer használatával. Minden UUID 38 karakter hosszú.

**Kapcsolatok*

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**Elavult**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**Módosítások**
- Változások a **substr()** függvényben
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- **strpos()** most már egyszerű karakterláncra támaszkodik egy karakterláncban végzett keresésen belül
- **regexp_match()** now returns pos of a matching regular expression

Ezt a funkciót számos fejlesztő fejlesztette ki
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
Vagy egy alapértelmezett attribútum érték az elem digitalizálásakor:

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

A függvény egyetlen argumentumot, egy lapösszeállításban lévő elem azonosítóját veszi fel, és egy változónév-térképet ad vissza az adott elemhez tartozó értékre. Ez lehetővé teszi olyan dolgok végrehajtását, mint a szöveg beillesztése egy címkére, ami a lapösszeállítás egy másik elemének tulajdonságait tartalmazza, például

Térkép méretarányának beszúrása egy címkébe:

`map_get( item_variables( 'map'),'map_scale')`

Térkép középponti x koordinátájának beszúrása egy címkébe:

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Dokumentáció
### Funkció: Feldolgozás algoritmus fejlesztések
A feldolgozás algoritmusok felül lettek vizsgálva és dokumentálva lettek. A Súgó gombra kattintva megnyílik a QGIS honlapja, és megjeleníti az algoritmus leírását továbbfejlesztett dokumentációval és képekkel.

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: A QGIS támogatási felajánlások

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## Jelrendszer
### Funkció: Adatvezérelt szimbólum réteg láthatóság
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: színskála mentése és visszaállítása az egysávos álszínes megjelenítés használatához
Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Pont és hüvelyk hozzáadása az elérhető szimbólum egységekhez
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új színskála gomb vezérlő
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Stílus kezelés átdolgozása és frissítése
A stíluskezelés jelentős frissítést kapott. A fejlesztések a következők:
- Új kedvenc csoportosítási rendszer került hozzáadásra, ami alapértelmezettként a szimbólum lista vezérlőt használja
- A szimbólumok lista vezérlőből kiválasztott címke / intelligens csoport a rétegek (és az egyes munkamenetek) közti átváltásakor továbbra is megmarad
- A szimbólumok lista vezérlő frissíteni fogja a címkét / intelligens csoport legördülő listát, amikor a felhasználó kategóriát ad hozzá / átnevez / eltávolít
- A felhasználók mostantól közvetlenül címkézhetnek, valamint hozzáadhatnak a kedvencekhez, a szimbólumokhoz, miközben mentik ezeket a stílus adatbázisba
- A stíluskezelés korszerűsítése érdekében a csoportok el lettek távolítva és a címkékkel lettek teljesen helyettesítve
- A címkék integrálva lettek az importálás/exportálás felhasználói felületbe

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Több elem szín és átlátszóság beállításának támogatása a raszter megjelenítéséhez
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Alfa csúszka megjelenítése a szín gomb legördülő menüjében
Lehetővé teszi az alfa szín összetevő gyors finomhangolását

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Raszter széthúzás eszköztár műveletek támogatás az álszínes megjelenítéshez
Ezt a funkciót fejlesztette: Mathieu Pellerin
### Funkció: Átlátszóság támogatás a palettás megjelenítéshez
A QGIS 3.0 kiadásban most már lehetséges az egyedi értékek átlátszóság értékeinek módosítása a palettás megjelenítésnél.

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Raszter automatikus széthúzása a térképvászon frissítése során
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

Ezt a funkciót fejlesztette: Even Rouault
### Funkció: Felügyelet a felirat tartalom margó felett
Lehetővé teszi a bal/felső/jobb/alsó margók beállítását a felirat tartalmához.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: A feliratok kitölthetőek a kitöltés szimbólum stílusokkal
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

Valamint használhatóak a rajzi hatások és az adatvezérelt szimbólum paraméterek is.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Pont csoportosítás (klaszter) megjelenítés
Új szimbólum megjelenítés, ami csoportosítja a közeli pontokat egyetlen megjelenített jel szimbólumba. Választható, hogy a címkén megjelenjen azon elemek száma, melyek összesítve lettek egyetlen szimbólumba.

Továbbá, néhány fejlesztés történt a pont áthelyezés megjelenítéshez: különösképpen:
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- az egyedülálló pontok most már helyesen jelennek meg a saját kiválasztási állapotukban
- sok kód takarítás + dokumentáció is.

Fejlesztők számára: A QgsPointDisplacementRenderer egy új tiszta virtuális QgsPointDistanceRenderer alaposztályra lett osztva, ami kezeli a klaszterek felismerését és a pontok csoportosítását. Az új klaszter megjelenítő újrahasznosítja ezt az alaposztályt, hogy elkerülje a kód ismétlését.

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

Ezt a funkciót Andreas Neumann, Qtibia Engineering (Tudor Barascu), Karl-Magnus Jönsson, Geonesia (Nicolas Ponzo) és számos további névtelen támogató finanszírozta, akiknek nagylelkű hozzájárulásait is nagyra értékeljük!

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### Funkció: ÚJ TÉRKÉP SZÍNEZŐ ALGORITMUS A QGIS 3.0 KIADÁSBAN
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

Ezt a funkciót Nyall Dawson fejlesztette
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Szimbólum réteg átmeneti tiltása
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Diszkrét raszter stílus könnyed beállítása
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

Az egyedi érték számítása a háttérben történik, hogy a felhasználó felület válaszképes legyen a nagy (vagy távoli) raszteres rétegek számítása közben. Emellett a felhasználók manuálisan is hozzáadhatnak egyedi új osztályokat, és módosíthatják a hozzájuk tartozó pixel értéket bármely létező osztály esetén. Egyszerre több osztály törlése is támogatott, valamint a szín, az átlátszóság és a címkék beállítása több osztályon is módosítható egyidőben.

A színskálák betölthetőek ESRI clr/GDAL/GRASS támogatott színtábla formátumú szöveg fájlból. Megosztás céljából a színskálákat el lehet menteni clr szöveg fájlba.

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Címkézés
### Funkció: Címke betűkészletének méret beállítása mm/pixel egységekben
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Az egyéni címkézési eszköztár mostantól mindig engedélyezve van
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## Diagramok
### Funkció: Adatvezérelt tulajdonságok
Több adatvezérelt tulajdonság beállítás támogatás a diagramokhoz:
- Távolság
- Prioritás
- Z Index
- Akadály
- Megjelenítés
- Mindig látszik
- Diagram kezdő szög

Ezt a funkciót a QGIS Támogatási Program támogatta

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Megjelenítés
### Funkció: Élő réteg támogatás
A QGIS 3.0 mostantól támogatja az élő rétegeket. Ezek a rétegek újra meg lesznek jelenítve (kirajzolva) előre meghatározott időközönként tisztán és villódzásmentesen. Az élő rétegek kiválóan alkalmasak a folyamatosan változó adatok követéséhez, például gépjármű flották, madárcsapatok vonulása, amihez telemetriai adatai vannak és így tovább.

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

Ezt a funkciót fejlesztette: Kartoza & North Road
### Funkció: Réteg frissítés vagy réteg művelet indítása/leállítása PostgreSQL üzenet jel hatására
Az élő rétegek hatására ez lehetővé teszi műveletek végrehajtását vagy a réteg frissítését a QGIS-ben, de csak akkor, ha az adatbázis értesíti a QGIS-t, hogy valamit meg kell tennie. Kevesebb erőforrást igényel, mint az időközönkénti frissítés, és ezzel még kódolni is tud egy csevegő alkalmazást a QGIS-ben :)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### Funkció: Címkézési eredmények gyorsítótárazása a szükségtelen újrarajzolások elkerülésének érdekében, amikor a vászon frissül.
Ez a változás lehetővé teszi a címkézési eredmények gyorsítótárazását egy térkép megjelenítést követő képben. Ha a gyorsítótárazott címkézési eredmény képe újra felhasználható a következő megjelenítéshez, akkor fel lesz használva, elkerülve a címkézési problémában részt vevő összes réteg újrarajzolását és a megoldja címkézési  módokat. Alapvetően ez azt jelenti, hogy a **vászon frissítésekor a NEM-CÍMKÉZETT rétegek módosításai sokkal gyorsabban jelennek meg**. (Olyan rétegek módosításai, amelyek részt vesznek valamilyen címkézési megoldásban továbbra is igénylik a teljes újrarajzolást)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Rács megjelenítés a pont áthelyezéshez
Rács megjelenítés használata a pont áthelyezéshez

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## Digitalizálás
### Funkció: Tartomány a töréspont kiválasztáshoz a csomópont eszközben
Ez a funkció lehetővé teszi a **csomópont tartomány** kiválasztását egy pontból.

A funkció a ** Shift + R ** billentyű kombinációval aktiválható - utána az elem kezdő és záró pontjára kell kattintani - ez kijelöli a kettő közötti összes töréspontot.

A tartomány kijelölés bármikor törölhető jobb kattintással vagy az Esc billentyű megnyomásával.

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funkció: Alapértelmezett Z érték hozzáadási lehetőség
Geopackages/Shape fájl létrehozása: Most már beállítható, hogy Z értéket tartalmazzon

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette: Alexander Lisovenko / Paul Blottiere
### Funkció: Az elem mozgatás most már kihasználja a Bővített digitalizálás lehetőségeit
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

Ezt a funkciót fejlesztette: Denis Rouzaud
### Feature: Added functionality to copy/move feature to move feature map tool
Ez lehetővé teszi a kijelölt elem másolatának létrehozását és annak mozgatását

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette: Denis Rouzaud
### Funkció: Útvonalkövetés eltolással
Most már használhatja a követés digitalizálás eszközt eltolással, ahogyan a mellékelt képen látható.

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### Funkció: A töréspont eszköz nagyjavítása
A Csomópont eszköz (mostantól Töréspont eszközre átnevezve) egy teljes átdolgozáson esett túl a nagyobb rugalmasság érdekében. Néhány példa a legfontosabb változásokból:
1. Ahelyett, hogy a felhasználónak először ki kellene választania egy elemet, majd a második lépésben a töréspontokat szerkesztenie, az eszköz egyszerre több elemmel is képes dolgozni. Ennélfogva egyszerűen több elemből kiválaszthatja a töréspontokat, és egyszerre áthelyezheti vagy törölheti azokat. Ha szükség van arra, hogy korlátozza a meghatározott elemek töréspontjainak kiválasztását, akkor először kiválaszthatóak az elemek a kiválasztó eszközzel - ilyen esetekben a töréspont eszköz csak a kiválasztott elemek töréspontjaival dolgozik.
2. Ahelyett, hogy csak az aktuálisan kiválasztott réteggel dolgozna, az eszköz képes dolgozni minden olyan réteggel, amely egyidőben szerkesztő módban vannak. Az olyan elemek mozgatása, amelyek logikailag egymáshoz tartoznak, de különböző rétegekben találhatóak, sokkal könnyebbé váltak. Az aktuális réteget azonban figyelembe veszi, ha a töréspontok kiválasztásakor több lehetőség van.
3. A elemek és azok csúcsai ki lesznek emelve, amikor a felhasználó rájuk mozgatja az egérmutatót, így adva jobb vizuális visszajelzést.
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. könnyebb pontosan elhelyezni csomópontokat (nem kell többé erőltetni az egérgombot)
6. az egyik nem mozgatja véletlenül a csomópontokat
7. lehetőség van a művelet megszakítására
8. lehetővé teszi a térkép eltolását a szóköz billentyű megnyomásával, mialatt a csomópontot mozgatja

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Funkció: Töréspont eszköz: középpont jelölők a töréspontok hozzáadásához
A továbbfejlesztett töréspont eszköz mostantól további jelölőket jelenít meg a vonal szakaszok középpontjában. Ilyen jelölőkre kattintva új töréspontot adhat meg. Meg lett tartva a töréspontok hozzáadásának meglévő módja, vagyis a szakaszon történő dupla kattintás.

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Funkció: Töréspont eszköz: vonal folytatása
Amikor törtvonal geometriákat szerkeszt a töréspont eszközzel, és az első vagy az utolsó töréspont felé mozgatja az egeret, akkor egy extra pontot jelenít meg a végpont mellett. Ha rákattint a jelölőre, akkor új töréspontot ad hozzá a geometria végéhez.

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Funkció: Töréspont eszköz: együttműködés a bővített digitalizálás panellel
A bővített digitalizálás panel mostantól működik a töréspont eszközzel - most már meg lehet adni a panelben egy új vagy már létező töréspont koordinátáját, mint ahogyan más digitalizáló térképi eszközben.

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Adatkezelés
### Funkció: Mozgatás az aktuális elemre az attribútum táblában
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

Ezt a funkciót Marco Hugentobler fejlesztette
### Funkció: Koordináta-rendszer terjedelem térképe a projekt tulajdonságokban
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### Feature: Auxiliary Storage Support
Egy új fül érhető el a vektor réteg tulajdonságokban a segédtároló kezeléséhez:

Egy új művelet az *Adatok tárolása a projektben* az adatvezérelt menüben érhető el, amivel egyszerűen kezelheti egy adott tulajdonság segéd adatait:

A segédadatok egy sqlite adatbázisban vannak tárolva, és az OGR adatszolgáltató (a SpatiaLite szolgáltató helyett) kezeli, hogy a lehető legkisebb legyen az adatbázis fájl. Ez az adatbázis fájl (*.qgd* kiterjesztéssel) a projektfájl mellett található, vagy közvetlenül az új *.qgz* formátumban van beágyazva.

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### Funkció: Metaadatok nagyjavítása
A QGIS metaadatok rendszere teljesen át lett dolgozva. A QGIS 3.0-ban bemutatkozik a mi saját belső, megformált metaadatok sémánk, ami elkülönül a QGIS projekt fájl formátumától. Új API képességek mutatkoznak be a réteg metaadatainak olvasásához és írásához. Külön lett választotva a metatadatok megjelenítése a szerkesztéstől, és új metaadat szerkesztő eszköz lett hozzáadva. A metaadatok jelenleg a projekt fájlban kerülnek mentésre. Menthető XML fájlként is a fájl alapú rétegek mellett vagy egy helyi sqlite adatbázisban távoli rétegekhez (például PostGIS).

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### Funkció: Egységesített adatforrás kezelő párbeszédablak
Egyetlen egységes párbeszédablak az adatforrás kezelés és a rétegbetöltés kezeléséhez.

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

Ezt a funkciót támogatta: Boundless

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Funkció: OSM Letöltés eszköz eltávolítva
We have removed the OSM downloader tool that was provided in 2.x releases of QGIS. We encourage you to rather use the QuickOSM plugin which has been ported to QGIS 3.0.
## Űrlapok és Vezérlők
### Funkció: Címkék kezelése a különböző szerkesztő vezérlőkön
A Húzd és ejtsd egy elem dupla kattintása lehetővé teszi, hogy szabályozza, hogy a címke minden egyes elemhez külön-külön jelenjen meg.

Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: Lehetővé teszi az elem összekapcsolás/szétkapcsolás gombok beállítását a kapcsolat szerkesztő vezérlőn.
Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: a fülek és csoportdobozok feltételes láthatósága
Ez új beállítási lehetőséget ad a fülek és csoportdobozok feltételes megjelenítéséhez vagy elrejtéséhez a Húzd és ejtsd tervezési űrlapokon. A beállítás a mezők konfigurációs felületén dupla kattintással történik a tervező fában. A láthatóság ellenőrzésére kifejezést lehet megadni. A kifejezés minden alkalommal újra ki lesz értékelve az űrlap érték változása során, és a fül vagy a csoportdoboz ennek megfelelően lesz megjelenítve/elrejtve.

Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: Intelligensebb alapértelmezett szerkesztés vezérlők modulokkal a kiválasztásukhoz
Mostantól a vezérlők adhatnak pontszámot arról, hogy milyen jól tudnak kezelni egy mezőtípust. Ez jobb alapértelmezett vezérlőkhöz vezet.

Ezenkívül modulok is hozzáadhatók egy vezérlő típus kiválasztásához a külső információk függvényében. Egyikük egy táblát használ a PostgreSQL-ben, ami lehetővé teszi az egyes mezőkhöz használni kívánt vezérlő típus és konfiguráció megadását

Automatikusan felveszi RelationReference vezérlőt az idegen kulcsokért.

Ezt a funkciót fejlesztette: Patrick Valsecchi
### Funkció: Mező korlátozások kikényszerítése vagy csak figyelmeztetés
A nem kikényszerített korlátozások csak egy figyelmeztetést jelenítenek meg a felhasználónak, de nem akadályozzák meg az elem véglegesítését. A kikényszerített korlátozások blokkolják a felhasználót a nem megfelelő elemek véglegesítésében. Tehát most már finom figyelmeztetések vannak! A szolgáltató által észlelt korlátozások mindig kényszerítettek.

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Réteg hatáskörű műveletek hozzáadása
Az attribútum táblán belül van egy új gomb, amivel kiválaszthatja azokat az műveleteket, amelyek nem az különböző elemeken alapulnak, hanem az egész rétegre érvényesek. Általában az összes elemen vagy csak a kiválasztottakon lesznek végre hajtva a műveletek.

Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: Mezőértékek megjelenítése az űrlap szűrés mód automatikus kiegészítőjében
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: nagyítás az elemekre és elemek felvillantása gyorsbillentyűk hozzáadása a kiválasztás űrlappal párbeszédablakban
Lehetővé teszi a nagyon gyors navigációt és az elemek azonosítását, amelyek megfelelnek az űrlapban szereplő kritériumoknak

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: közötte/nincs közötte lehetőség hozzáadása a numerikus mezőkhöz a kiválasztás űrlappal párbeszédablakban
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Réteg jelmagyarázat
### Funkció: Nem kiválasztott rétegek elrejtése művelet
Lehetővé teszi az összes ki nem választott réteg gyors elrejtését. Ez nagyon hasznos, ha van egy nagy projektje, és néhány réteget kivéve mindent gyorsan el akar rejteni

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: A csoportokon belüli rétegek láthatóságának ergonómiai változása
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- Nincs többé félig engedélyezett csoport állapot
- **Ctrl-katintás** egy letiltott csoporton, engedélyezni fogja a csoportot az összes hozzá tartozó elemmel együtt.
- Kattintás egy letiltott rétegre, engedélyezni fogja a réteget az összes szülő elemmel együtt.
- Ctrl-katintás egy engedélyezett csoporton, letiltja a csoportot az összes hozzá tartozó elemmel együtt.
- Ctrl-kattintás egy engedélyezett rétegre, letiltja a réteget az összes szülő elemmel együtt.
- Ezek a műveletek elérhetőek a fa nézet környezeti menüjének elemei között.
- A nem látható rétegek, mert azok vagy a szülő elemei le vannak tiltva, szürkén jelennek meg.

Ezt a funkciót fejlesztette: Even Rouault
## Térkép összeállítás
### Funkció: Az összeállítás tábla rács vízszintes és függőleges vonalainak megjelenítés szabályozása
Mostantól lehetséges az összeállítás tábla elemek vízszintes és függőleges vonal megjelenítéseinek egymástól független beállítása. Ez a hozzáadott rugalmasság közvetlenül a QGIS-en belül teszi lehetővé az elem stílus beállítási lehetőségeit.

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: qpt behúzása a QGIS-be egy új összeállítás létrehozásához sablonból
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Sorköz testreszabásának lehetősége az összeállítás jelmagyarázat elem címkékhez 
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Koordináta-rendszer választási lehetőség a térkép elemekhez
Ez lehetővé teszi, hogy a térkép elemek koordináta-rendszere eltérjen a vászon/projekt koordináta-rendszerétől. Továbbá lehetővé teszi, hogy az egyes térkép elemek eltérő koordináta-rendszerel rendelkezzenek, pl. egy áttekintő térkép koordináta-rendszere eltérjen a fő térképtől. 

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: A shift billentyű nyomvatartásával korlátozhatóak a vonal szögek egy törtvonal/felület rajzolása közben
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Több adat-vezérelhető szabályozás
Elem **keret** és **háttérszín** Adatvezérelt **svg szín és körvonal vastagság az összeállítás kép elemeihez** (Különösen hasznos, amikor a kép egy észak nyilat ábrázol!) Adatvezérelt **jelmagyarázat cím és oszlop számítás** Adatvezérelt **léptékvonalzó szín és vonal vastagság**

Ezt a funkciót a QGIS Támogatási Program támogatta

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Térkép összeállítás nagyjavítása
Ez egy nagyobb átdolgozás a QGIS kódjában az összeállítások kezeléséhez. 

Kiemeltek:
- Egy új QgsLayoutManager osztály, amit az összeállítások tárolására és sorbarendezésére/sor szétbontására használják. A QgsLayoutManager hozzá lett csatolva a QgsProject-hez. Ez lehetővé teszi, hogy a belső magkód hozzáférjen a projekthez csatolt összeállításokhoz. Az összeállítások összes kezelése át lett téve az alkalmazásból a belső magba, könnyebbé téve a szerver (és más nem alkalmazás alapú projekt. Qfield/roam?) hozzáférését a projekt összeállításokhoz a törékeny xml értelmezés újrarendezése nélkül.
- Az összeállítás ablakok szükség esetén lesznek létrehozva és bezáráskor megsemmisülés. Ezzel elkerülhető az összes összeállítás ablak és vezérlő létrehozása minden egyes összeállítás elemhez a projekt betöltése alatt, ami nagy rendszer erőforrást igényelt. **Ez volt a fő oka az összeállításokat tartalmazó projektek lassú betöltődésének.** Mostantól az összeállítás ablakok csak szükség esetén lesznek létrehozva és bezáráskor megsemmisülnek. Az összeállítás elem konfigurációs vezérlők is csak szükség esetén lesznek létrehozva (amikor az elem ki lett választva) az összes vezérlő elő létrehozása helyett. 
- Az egyik előnye a összeállítás ablakok bezárást követő megsemmisítésének, hogy **többé nem szenvedünk egy Qt hibától**, ami blokkolta a lebegő dokkok használatát az összeállítás ablakokban. Mostantól lebeghetnek az elem/összeállítás/stb panelek! Sokkal szebb dolgozni az összeállításokkal teljes képernyőn, több monitoros rendszeren is. 
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- Rengeteg kód takarítás és eltávolítás

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: A QGIS Felhasználói Csoport, Svájc és sokan mások! 

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Elemző eszközök
### Funkció: Raszter egyedi értékek számolás a feldolgozáshoz
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## Feldolgozás
### Funkció: Új algoritmus a vonalak eltolásához
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új algoritmus az egyoldali övezetekhez
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Egyszerűsítési eljárás kiválasztásának hozzáadása az egyszerűsítésekhez
Ez a változás lehetővé teszi a felhasználónak, hogy kiválassza a használandó eljárást, amikor a geometriák egyszerűsítése algoritmust futtatja. Ez lehet a meglévő távolság alapú (Douglas Peucker) algoritmus, terület alapú (Visvalingam) algoritmus és illesztés rácshoz.

A Visvalingam különösen a kartográfiai szempontból kellemesebb egyszerűsítést eredményez a standard távolság alapú módszerek helyett.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: eredmény geometria típus támogatása a modellekben
A modell gyerek algoritmus inputok mostantól szűrésre kerülnek, azokhoz, amelyek alkalmasak egy másik gyerek algoritmus inputjára vonatkozó geometria típusok létrehozására

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Szög küszöbérték a simítás algoritmushoz
Beállítási lehetőség hozzáadása a QgsGeometry::smooth-hoz, hogy ne simítsa azokat a szakaszokat, amelyek rövidebbek egy bizonyos küszöbértéknél, vagy ne simítsa azokat az éles sarkokat, melyek szöge meghaladja a küszöbértéket.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Jobb támogatás a Z/M dimenziókhoz és az íves geometriákhoz
Sokkal több algoritmus veszi figyelembe a Z/M értékeket és nem dobja el ezt az információt, és a továbbiakban most már több algoritmus helyesen állítja elő az íves geometriákat ezen geometriák szakaszosításának kényszerítése nélkül.
### Funkció: A feldolgozáshoz adott raszter elemző algoritmusok
A következő algoritmusokat a raszter elemzés modulból adtuk a feldolgozáshoz:
- Kitettség
- Lejtőszög
- Érdesség
- Domborzat árnyékolás
- Domborzat árnyalás

Most ezek az algoritmusok használhatók szkriptekben, modellekben és kötegelt feldolgozásban.

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Új algoritmus megadott töréspontok kinyerésére
Ez az algoritmus lehetővé teszi megadott töréspontok kinyerését a geometriákból. Pl. kivehetjük az első és utolsó pontot a geometriából.

Ez az algoritmus a kiveendő töréspont indexek vesszővel elválasztott listáját várja, pl. 0 = első töréspont, 1 = második töréspont, stb. Negatív indexeket használhatunk a geometria végpontjától megadott töréspontok kivételéhez. Pl. -1 = utolsó töréspont, -2 utolsó előtti töréspont.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Expose zonal statistics from Zonal statistics plugin in toolbox
Ezt a funkciót fejlesztette Alexander Bruy
### Feature: Add a spatialite execute SQL algorithm
Ezt a funkciót fejlesztette: Mathieu Pellerin
### Funkció: Új algoritmus a vonalak meghosszabbításához
Lehetővé teszi a törtvonalak meghosszabbítását egy adott távolsággal a vonal elején és végén

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új átvétel kifejezés alapján algoritmus
Egy input réteg szűrése kifejezéssel

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add import into spatialite algorithm
Ezt a funkciót fejlesztette: Mathieu Pellerin
### Funkció: Interpolálás algoritmusok
IDW és TIN interpolálás átemelése az Interpolálás modulból az eszköztárba

Ennek eredményeként az interpolálás modul el lett távolítva

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Új algoritmus a geometriák kifejezés alapú számításához
Ez az algoritmus frissíti a létező input elemek geometriáit (vagy újakat hoz létre) QGIS kifejezések használatával. Ez lehetővé teszi az összetett geometriák módosításait, amihez használható a QGIS kifejezések motor teljes rugalmassága, az eredmény elemek geometriáinak manipulálásához és létrehozásához.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Geometriák illesztése a réteghez algoritmus
Geometriák illesztése modul átemelése a feldolgozásokba

A geometriák illesztése algoritmus lehetővé teszi az illesztést más réteg típusokhoz, támogatja a pont/vonal rétegeket

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új input típus a kifejezésekre
Ez egy új input típust ad hozzá a kifejezés inputokhoz. A kifejezés input lehet szülő réteghez csatolt, így a kifejezés építő a megfelelő mezőket és réteg változókat jeleníti meg.

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: SplitWithLines
A SplitLinesWithLines algoritmus SplitWithLines névre lett átnevezve. Felületeket is elfogad inputként. Csak a kiválasztott vonalak felosztása (ha a feldolgozásban be van állítva a Csak a kiválasztottak beállítás). Probléma jelző naplóüzenet, ha többrészű geometriákat próbál felosztani. Frissített súgó.

Ezt a funkciót fejlesztette: Bernhard Ströbl
### Feature: Pole of inaccessibility algorithm
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Az Átvétel attribútum alapján algoritmus képes átvenni null/notnull értékeket 
Támogatás hozzáadása a szűréshez, ahol egy attribútum érték null vagy notnull

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Attribútum index létrehozása algoritmus
Lehetővé teszi egy réteg attribútum indexének létrehozását a gyorsabb attribútum alapú szűrés érdekében

A támogatás a réteg alapjául szolgáló adat szolgáltatótól függ

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
Egyszerűen eltávolítja az összes geometriát egy input rétegből és az elemeket csak az attribútumokkal adja vissza

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

Mostantól egyetlen egy egységesített algoritmus van, ami sokkal rugalmasabb modelleket tesz lehetővé, ahol a mező típus nem ismert előre.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Hőtérkép modul átemelése a feldolgozás algoritmusokba
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új algoritmus a geometriák derékszögesítéséhez
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Hálózat elemzés algoritmusok
legrövidebb útvonal és szolgáltatás terület hozzáadása a Feldolgozásokhoz

továbbá lehetővé teszi a legrövidebb útvonal számítását egy pontból az összes ponthoz egy rétegben, vagy egy réteg összes pontjából egy záró ponthoz. És szolgáltatási területek létrehozása a rétegben lévő összes ponthoz.

Ennek eredményeként az Úthálózat modul el lett távolítva.

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Feldolgozás modellek exportálása PDF/SVG fájlokba
A feldolgozás modellek bittérképes képként történő exportálásán kívül most már lehetőség van a feldolgozás modellek felbontás független PDF és SVG fájlokba történő exportálására. Ez lehetővé teszi a nagy felbontású modellek exportálását, amelyek beágyazhatók a publikált papírokba és könyvekbe.

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Új algoritmus a táblák csonkításához
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
Ezt a funkciót fejlesztette: Victor Olaya
### Feature: Algorithm to fix invalid geometries using native makeValid() implementation
Ezt a funkciót fejlesztette Alexander Bruy
### Feature: Add search to Get Scripts and Models dialog
Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Általános centrális (súlypont) algoritmus 
Átdolgozott centrális algoritmus, ami kezeli a nem felület típusú rétegeket

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Improved Extract nodes algorithm
A Csomópontok átvétele algoritmus mostantól elmenti a csomópont indexet, a távolságot a vonal mentés és a szöget a csomópontnál

Ezt a funkciót támogatta: Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Új algoritmus a pontok fordításához (mozgatás)
Lehetővé teszi a geometriák x/y elmozdítással történő eltolását

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Javított feldolgozás modellező ablak
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funkció: Új raszter egyedi értékek jelentés algoritmus
Egy új algoritmus lett hozzáadva a feldolgozásokhoz, ami visszaadja az összes egyedi érték számát és területét egy megadott raszteren belül.

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Remove TauDEM provider from core Processing
Eltávolítottuk a TauDEM szolgáltatót a feldolgozásból.

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### Funkció: Fájl letöltés a Feldolgozás eszköztárból
Fájl letöltése a Feldolgozásból. Egy távoli API lekérdezése egy geojson beszerzéséhez

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Funkció: Optimalizált pontok a geometria mentén algoritmus
Felület geometriák támogatása, null geometriák kezelése, és az eredeti szög rögzítése a vonal mentén az egyes pontok távolságával együtt.

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Rendezés kifejezés alapján algoritmus
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Alkalmazás és Projekt beállításai
### Funkció: Új tömörített projekt fájl formátum .qgz
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Funkció: Támogatás hozzáadása a felhasználói profilokhoz
Az összes felhasználói beállítás/modul, stb mostantól minden platformon az alkalmazás adat helyéről lesz betöltve és többé nem a .qgis3/2 könyvtárból. Az egyes profilok beállításai és a modulok most már elkülönülnek egymástól.

Ez lehetővé tesz különböző futtatási beállításokat, attól függően, hogy a felhasználónak mire van épp szüksége, pl. teszt, munka, demó, stb

A profil menü lehetővé teszi a profilok közti váltást vagy egy új létrehozását.

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## Böngésző
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
Könnyűvé teszi pl. az ideiglenes munka rétegek tárolását PostGIS-be

Ezt a funkciót fejlesztette: Martin Dobias
### Funkció: Az önálló QGIS Böngésző alkalmazás eltávolítva
Eltávolítottuk az önálló QGIS Böngésző alkalmazást, amit a QGIS 2.x verziók szállítottak. Ez az alkalmazás rossz felhasználói észrevételeket kapott, és olyan karbantartási többletet jelentett, amit nem kívánunk tovább folytatni a 3.0-as kódbázisban.
## Adatszolgáltatók
### Feature: New unified \'add layer\' dialog
Mostantól egyetlen egy párbeszédablakot használhat a nagy változatosságú adatformátumok hozzáadásához a QGIS-be.

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Funkció: GeoPackage
- a feldolgozás alapértelmezetten a pkg-t használja
- a mentés másként alapértelmezetten a pkg-t használja
- az új réteg létrehozása alapértelmezetten a pkg-t használja
- a böngészőben húzd és ejtsd módszerrel importálhatóak a rétegek

Ezt a funkciót fejlesztette: Alessandro Pasotti
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
Ezt a funkciót Nyall Dawson fejlesztette
### Funkció: Z/M értékkel rendelkező geometriák támogatása a gpkg, spatialite és ideiglenes réteg szolgáltatókban
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

Ezt a funkciót fejlesztette: Mathieu Pellerin, Alexander Bury, Paul Blottiere
### Funkció: Egyedi és nem null érték korlátozások kezelése
A szolgáltató oldali egyedi és nem null értékű beágyazott korlátozások automatikus észlelése a postgres, spatialite, ogr szolgáltatóknál

Az ügyfél oldali egyedi és nem null értékek korlátozás beállítható a QGIS alkalmazáson belül.

Az egyedi korlátozások kényszerítettek az attribútum űrlapban

Ezt a funkciót támogatta: OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: GeoNode integráció
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

Ha a GeoNode példány inkább a QGIS kiszolgáló hátterét használja, mint a támogatott GeoServer háttér rendszerét, akkor a kiszolgálóról másolhatja és beillesztheti a stílusokat , és alkalmazhatja azokat a helyi rétegre úgy, hogy a WFS réteg pontosan úgy jelenjen meg, mint a kiszolgálón (ahogy itt, az animált GIF képen is látható).

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### Funkció: Literál alapértelmezett értékek észlelése a spatialite szolgáltatóhoz
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Attribútum index létrehozásának támogatása a spatialite szolgáltatóhoz
Lehetővé teszi az attribútum indexek létrehozását a spatialite rétegekhez

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funkció: Támogatás hozzáadása a tömbökhöz
A postgres, spatialite támogatása

Ezt a funkciót fejlesztette: Patrick Valsecchi
### Funkció: Támogatás a HStore-hoz a PostGIS adat szolgáltatóban
### Funkció: Kapcsolatok automatikus felfedezésének hozzáadása a PostgreSQL-hez
Ezt a funkciót fejlesztette: Patrick Valsecchi
### Funkció: Adat függőségek a rétegek között
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

Ezt a funkciót  Hugo Mercier fejlesztette
### Funkció: dxf exportálás: vetületváltás támogatása
Ezt a funkciót fejlesztette: Juergen E. Fischer
### Funkció: Stílus betöltése/mentése az adatbázisba GPKG és a Spatialite szolgáltatóknál
Ezt a funkciót fejlesztette: Even Rouault
### Funkció: Alapértelmezések kezelésének javítása
Az alapértelmezések kezelésének javítása (beleértve a szolgáltató alapértelmezett kikötéseket, literál alapértelmezéseket és a QGIS kifejezés alapértelmezéseket) és az egyedi értékek korlátozás automatikus kezelése a rétegeken

Bármelyik egyedi érték korlátozással bíró mező garantáltan rendelkezni fog egy értékkel, ami ebben a mezőben egyedi.

Ez azt is jelenti, hogy bizonyos szerkesztési műveletek (például a másolás-beillesztés, elemek felosztása stb.) után az attribútumok az alapértelmezett értékre lesznek állítva, ha az megfelelő.

Ezt a funkciót támogatta: Zug kanton és a QGEP projekt

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## QGIS Szerver
### Funkció: QGIS Szerver nagyjavítása
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

Egy évvel ezelőtt, egy svájci kis troll megkongatta a harangot, hogy nagy igény van a szerverhez szükséges kódbázisra. Valójában, az API-t néhány, a QGIS Szerver régi módszere lezárta. Röviden, a QGIS Szerver saját módján újraértelmezte a qgs projekt fájlt, és olyan függőségeket teremtett a QGIS egyes részeihez, amelyeket el kellett távolítanunk.

A szerver kódbázis kiszervezésére nem volt lehetőség, ezért újra kellett építeni azt. Az érintett felek úgy döntöttek Lyon városában, Franciaországban, hogy elkötelezik magukat egy kód tervezésére, megosztják elképzeléseiket, megtervezik a munkát, és végül a következőket teszik:

Magasabb szintű újjáépítés

Minden szolgáltató (WMS GetMap, WFS GetFeature, GetLegendGraphics, WCS, GetPrint stb.) át lett írva. Néhány, pl. a WMS teljesen újra lett írva. Dicsőség a fejlesztőknek!

Új tulajdonságok
- Többszálú megjelenítés, mint ahogy az asztali verzióban
- Új lehetőség a réteg metaadatok megbízhatóságához és ezáltal felgyorsul a projekt betöltés
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- Teljes python kötés a szerver API-hoz
- Szerver szolgáltatások modulokként, mint szolgáltatók

Mély, bonyolult és kényelmetlen feladatok
- Összes egyke hívás eltávolítása
- Az összes függőség kivágása a régi QGIS projekt fájl értelmezőhöz
- A GUI könyvtárhoz való függőség minimalizálása. Mivel a térképek megjelenítéséhez szükséges a betűtípus, a teljesen eltávolításuk nem volt lehetséges.

Infrastrukturális feladatok
- OGC kompatibilitási platform építése, és integrálása egy folyamatos integrációs platformhoz. A megfelelőségi jelentések mostantól a tests.qgis.org oldalra kerülnek
- Add unit tests \... and again more unit tests
- A QGIS kiszolgáló biztonsági résekre vonatkozó tesztelése (SQL behatolások és egyéb rosszindulatú támadások)
- Profilozás és teljesítményértékelés előkészítése. Ehhez a munkához még mindig szükség van némi figyelemre, és támogatásra

A FOSS4G-EU-n júliusban tartottak előadást.

Ezt a funkciót támogatták: QGIS.ORG adományozói
### Lehetőség: Az elem geometriájának szegmenseiről szóló információ lehetősége a kiszolgálón
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## Bővítmények
### Funkció: Megbízható állapot eltávolítása a Modul kezelőből
<https://github.com/qgis/QGIS/pull/5272>
### Funkció: Offline szerkesztés: Jelzés hozzáadása a csak kiválasztott elemek másolásához
Ez kibővíti az offline szerkesztési lehetőségeket, hogy a nagy rétegek  részhalmazán dolgozzon csak

Ezt a funkciót támogatta: DB Fahrwegdienste GmbH

Ezt a funkciót Matthias Kuhn fejlesztette 
### Funkció: GDAL eszközök átemelve a Feldolgozásba
GDAL eszközök modult eltávolítottuk.

A GDALTools modul által korábban elérhető összes függvény át lett helyezve a QGIS Feldolgozás keretrendszerbe, lehetővé téve ezen eszközöknek használatát szkriptekben, modellekben és azok végrehajtását kötegelt feldolgozásokban. Ezenkívül az algoritmusokat frissítettük a GDAL legújabb verzióiban bevezetett új paraméterekkel, és javítottuk a teljes UI/UX-et, néhány speciális paraméter megjelenítésével, mint például a létrehozási beállítások, a NODATA értékek beállításai stb.

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: Lehetővé tett modultelepítés helyi ZIP csomagokból
mostantól sokkal könnyebb modulokat manuálisan telepíteni anélkül, hogy először kézzel kellene kicsomagolni őket a felhasználói profil mappában.

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alexander Bruy
### Funkció: A modulok egyéni súgókat szolgáltathatnak a kifejezés ablakban
A kifejezéseket biztosító modulokhoz hozzá lehet adni egyéni súgót HTML-karakterláncokkal.

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programozhatóság
### Funkció: Geometria osztály frissítések
A QGIS-ben a geometria osztályok jelentősen át lettek dolgozva. A régi osztályok át lettek nevezve (az alábbi táblázat szerint). Az új geometria osztályok megfelelően megőrzik a Z és M attribútumokat, ha vannak.

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

Ez végül egy következetes állapotot hoz vissza a geometria API-n belüli elnevezésben
### Átnevezések
| QGIS 2 | QGIS 3 |
| --- | --- |
| QgsPolygon | QgsPolygonXY |
| QgsMultiPoint | QgsMultiPointXY |
| QgsMultiPolyline | QgsMultiPolylineXY |
| QgsMultiPolygon | QgsMultiPolygonXY |
| QgsPolygonV2 | QgsPolygon |
| QgsMultiPointV2 | QgsMultiPoint |
| QgsMultiPolylineV2 | QgsMultiPolyline |
| QgsMultiPolygonV2 | QgsMultiPolygon |

See also <https://github.com/qgis/QGIS/pull/5491>

Ezt a funkciót Matthias, Nyall és mások fejlesztették
### Funkció: Feladat kezelő
Bevezetésre került egy keretrendszer a háttér feladatok létrehozásához, amelyek egy központosított kezelőn keresztül kapcsolódnak egymáshoz

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

Egyszerű python QgsTask.fromFunction eljárás hozzáadása feladatok létrehozásához egy funkcióból anélkül, hogy QgsTask alosztályt kellene létrehozni

Támogatás függő feladatokhoz

Egy olyan feladat törlése, amelytől mások függenek az összes többi feladat törléséhez is vezet.

Függő rétegek kezelésének hozzáadása a feladatkezelőhöz

Ha egy feladat függő rétegeket tartalmaz, amelyek eltávolításra kerülnek, a feladat automatikusan törlődik

A QgsTasks alfeladatokat is tartalmazhat

Egy QgsTask-nak most már QgsTasks alfeladata is lehet a QgsTask::addSubTask hívásával. Az alfeladatok saját függő alfeladatokkal rendelkezhetnek.

Az alfeladatok nem láthatók a felhasználók számára, és a felhasználók csak a szülői feladat általános előrehaladását és állapotát látják.

Ez lehetővé teszi, hogy olyan feladatokat hozzunk létre, amelyek magukban sok kisebb feladatelemből épülnek fel. A feladatkezelő továbbra is kezelni fogja az alfeladatok megkezdését és ütemezését, így pl. az alfeladatok párhuzamosan futtathatók (ha a függőségük ezt lehetővé teszi).

Az alfeladatok maguk is rendelkezhetnek alfeladatokkal.

Ez a változás úgy van kialakítva, hogy az algoritmusok és a modellező algoritmusok feldolgozási koncepciója közvetlenül a feladatkezelő felépítésére legyen fordítható.

Ezt a funkciót a QGIS Támogatási Program támogatta

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
A QgsDataItem implementációk hasDragEnabled(), mimeUri() és QgsCustomDropHandler implementációk biztosíthatják az egyéni elemek eldobását.

Ezt a funkciót fejlesztette: Martin Dobias

{{<content-end >}}
