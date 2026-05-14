---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: projektą
sidebar: true
title: QGIS 3.0 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.0 pakeitimai{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

Laidos data: 2018-02-23

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**Ačiū**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## QGIS 3.0 versijos rėmėjai
{{<fund type="changelog" relativeImgPath=true >}}
### Savybė: Pašalintas dxf2shp konvertavimo priedas
Funkcionalumą teikia OGR, todėl nebereikia QGIS priedo, atliekančio tokią užduotį.
### Savybė: pašalintas nebeprižiūrimas oracle rastro priedas
### Savybė: TauDEM tiekėjas pašalintas iš Apdorojimo pagrindo
TauDEM yra gan specifinis įrankių rinkinys, reikalaujantis papildomų įrankių diegimo. Taigi nusprendėme paversti jį atskiru tiekėjo, taip sumažindami kodo dydį ir supaprastindami palaikymą.
### Savybė: daugiau pagalbos ir galimybė konfigūruoti QGIS pagalbos failų vietą
Pridėta daugiau pagalbos mygtukų algoritmams ir dialogams, ir jie rodo į internete esančią QGIS dokumentaciją.

Konfigūracija leidžia pasiekti kontekstinę pagalbą internete, organizacijos tinkle arba vietiniame kompiuteryje. Taip pat galima sujungti kelis pagalbos šaltinius.

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: Foto, TinkloPeržiūros ir FailoPavadinimo valdikliai migruoti į priedus
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### Savybė: iš apdorojimo išimti otb ir libartools tiekėjai
Nauja logika yra kurti priedų tiekėjus, galinčius sekti išorinį programinė įrangos gyvenimo ciklą.
## Naudotojo sąsaja
### Savybė: įjungti priklijuojami skydeliai su kortelėmis 
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### Savybė: tikslesnės raiškos mastelio keitimas pele
Kai kurie pelės įrenginiai (pavyzdžiui makuose) turi tikslesnes raiškas. Jie siunčia pelės ratuko įvykius aukštu dažniu, bet su mažesnėmis pokyčio reikšmėmis. Keičiant mastelį tokiais įrenginiais buvo nepanaudojamas greito mastelio keitimo veiksmams. Tai pataisyta 3.0 versijoje.

Šią savybę sukūrė Matthias Kuhn
### Savybė: paieškos juosta klavišų kombinacijų dialoge
Palaiko paiešką pagal veiksmo pavadinimą ir klavišų kombinaciją

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: atradimo juosta
Atradimo juosta yra greitas, visada paruoštas, bendras ir papildomas paieškos funkcionalumas kairėje apatinėje QGIS dalyje.

Šiuo metu jis gali ieškoti algoritmų, veiksmų, sluoksnių pavadinimų, o taip pat pažymėti geoobjektą dabar aktyviame sluoksnyje parašius atributo reikšmę.

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

Šią savybė sukūrė Nyall Dawson
### Savybė: daugiau neblokuojančio, keitimo vietoje
- žemėlapio vienetų mastelis
- spalvų kūrėjas ir ribotai atsitiktinių ramų keitimas
- spalvų keitimas spalvų sąraše vietoje ir stiliaus skydelyje
- spalvų ir simbolių keitimas vietoje makete

dabar rodoma vietoje stiliaus skydelyje
### Savybė: pridėti parinktį rodyti naudotojo spalvų schemų meniu
Tai leidžia naudotojams nurodyti, ar naudotojo sukurta spalvų schema turi būti rodoma spalvų mygtuko iškrentančiuose meniu.

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

Tai patogu, jei jūs turite kelias bendras paletes ir norite, kas jos būtų akimirksniu prieinamos per spalvų meniu.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: galimybė keisti žemėlapio drobės šiaurės rodyklės dekoracijų spalvą
Spalvų nustatymai buvo pridėti visiems žemėlapio drobės šiaurės rodyklės dekoracijoms.

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann (dalinis finansavimas)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: keisti atvertų skydelių matomumą pagrindiniame lange
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: pagerintas naudotojo sąsajos pastovumas
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- Visi API, susiję su **permatomumas/nepermatomumas/alpha**, buvo standartizuoti į **setOpacity()** ir **opacity()**. Medotai priima double reikšmę tarp 0 (permatomas) ir 1 (nepermatomas), palaikant suderinamumą su Qt API.
- Buvo sukurtas **naujas valdiklis QgsOpacityWidget**, kuris dabar naudojamas visur, kur tik nurodomas nepermatomumas. Taip užtikrinama tokia pati elgsena ir išvaizda.
- **Pasukimas** buvo standartizuotas API ir naudotojo sąsajoje, taigi dabar pasukimas yra visada pagal laikrodžio rodyklę. Visi pasukimo valdikliai buvo atnaujinti, kad priimtu reikšmes nuo -360 iki 360.
- 2.x Projektai su etiketėmis naudojančiomis pasukimą ir nuo duomenų priklausomą pasukimą dabar automatiškai **atnaujinami** atidarant 3.0
- Mastelio API sutapanti visame QGIS. **Klaidinantis mišinys mastelių denominatorių ir tikrų mastelių buvo pašalintas**, viskas dabar veikia su mastelių denominatoriais. Visų mastelių intervalų elgsena standartizuota su bendra reikšmę min/max masteliams (ir išskirtine api dokumentacija apie tai)
- Visi mastelių valdikliai dabar naudoja standartinį mastelių valdiklį pastovumui visoje naudotojo sąsajoje
- Etiketės dabar naudoja tą patį min/maks mastelio nurodymą kaip ir kiti elementai, o esami projektai automatiškai atnaujinami atidarant 3.0.
- Pataisyti beveik visi riktai, susiję su mastelių naudojimu, įskaitant riktus, laužančius nuo taisyklių priklausančius mastelių apribojimus

Ačiū QGIS PSC ir projekto donorams už šio darbo finansavimą ir leidimą jam įvykti!

Šią savybę finansavo QGIS rėmėjai ir donorai

This feature was developed by [Nyall Dawson](https://north-road.com)
### Savybė: atverti sluoksnius vienoje grupėje
Jei bandote atverti daug posluoksnių, dabar galite atidaryti visus juos toje pačioje legendos grupėje.

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## 3D savybės
### Savybė: 3D žemėlapis ir paviršiaus generavimas
QGIS atsirado naujas savas 3D žemėlapio rodinys! 3D žemėlapio rodinys rodo 2D žemėlapį (braižomą pagal projekto sluoksnius) ant paviršiaus. Pagal nutylėjimą paviršius yra plokščias, bet galima naudoti rastro sluoksnį su skaitmeniniu aukščio modelių, kaip aukščio duomenų šaltinį.

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- tempiant pelę nuspaudus vidurinį pelės mygtuką
- laikant Shift ir tempiant pelę nuspaudus kairį mygtuką
- laikant Shift ir naudojant mygtukus aukštyn/žemyn/kairėn/dešinėn

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Savybė: žemėlapio sluoksnių 3D braižymas
Su pradine konfigūracija žemėlapio sluoksniai braižomi 2D žemėlapyje ant paviršiaus. bet galima geriau išnaudoti 3D pasaulį sukonfigūravus 3D braižiklį kai kuriems žemėlapio sluoksniams. 3D braižikliai duomenis gali braižyti kaip tikrus 3D objektus - tai šiuo metu palaikoma vektoriniams sluoksniams (visi geometrijų tipai - taškai, linijos ir poligonai). Taip galima daug geriau vizualizuoti, pavyzdžiui:
- poligonai su pastatų pagrindu gali būti iškelti (galbūt su nuo duomenų priklausančiu aukščiu), kad gautume 3D vaizdą
- taškai su medžių taškinėmis pozicijomis gali būti braižomi kaip trimačiai medžių simboliai (paprastos geometrinės formos arba 3D modeliai įkeliami iš palaikomo formato failo)

Norėdami sukonfigūruoti 3D braižiklius, naudokite sluoksnio stiliaus valdiklį arba vektorinio sluoksnio savybių dialogą - ten yra nauja kortelė 3D braižiklių konfigūravimui.

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Išraiškos
### Savybė: nauji išraiškų kintamieji
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
Grąžina dabartinę QGIS naudojamą lokalę. Pagal nutylėjimą, tai dabartinė sistemos lokalė. Jei naudotojas įjungia lokalės permušimą QGIS nustatymuose, tai bus grąžinama naudotojo nurodyta lokalė.

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: nauji išraiškų kintamieji žemėlapio nustatymams
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujos išraiškų funkcijos
**Atlaso išraiškos**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**Suvestinės išraiškos**
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

**Masyvų išraiškos**

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

**Spalvų išraiškos**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**Datos ir laiko išraiškos**
- **epoch(date)**: Grąžina intervalą milisekundėmis tarp unix epochos ir nurodytos datos reikšmės.

**Bendros išraiškos**
- **env(name)**: Gauna aplinkos kintamąjį ir grąžina jo turinį kaip tekstą. Jei kintamasis nerastas, bus grąžintas NULL.
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

**Geometrijos išraiškos**
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
- **simplify(geometry, tolerance)**: Supaprastina geometriją išimant viršūnes naudojant atstumo slenkstį (pvz. Douglas Peucker algoritmas). Algoritmas išsaugo didelius geometrijų nukrypimus ir sumažina viršūnių skaičių beveik tiesiuose segmentuose.
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

**Sluoksnio savybė**
- **crs_description** returns the CRS description of the layer.

**Žemėlapio išraiškos**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**Žemėlapio sluoksniai**

Nauja grupė, kurioje yra sąrašas pasiekiamų dabartinio projekto žemėlapio sluoksnių. Grąžina vidinius žemėlapio id. Naudojama daugelyje kitų išraiškų funkcijų, kurios turi nuorodas į žemėlapio sluoksnius.

**Matematinės išraiškos**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**Operatoriai**
- **\~:** Performs a regular expression match on a string value.

**Įrašų ir atributų išraiškos**

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- **uuid()**: Kiekvienai eilutei generuoja universaliai unikalų identifikatorių (UUID) naudojant Qt QUuid::createUuid metodą. Kiekvienas UUID yra 38 simbolių ilgio.

**Ryšiai**

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**Nebenaudojama**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**Pakeitimai**
- **substr()** funkcijos pakeitimai
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- **strpos()** dabar pasikliauja paprasto teksto paieška tekste
- **regexp_match()** now returns pos of a matching regular expression

Šią savybę kūrė keli programuotojai
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
Arba numatytoji atributo reikšmė skaitmeninant geoobjektus:

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

Funkcija priima vieną argumentą, id elemento kompozicijos viduje, o grąžina žemėlapį iš kintamųjų pavadinimo su reikšme tam elementui. Tai leidžia jums daryti tokius dalykus, kaip įterpti tekstą į etiketę ištraukiant savybes iš kito elemento kompozicijoje, pvz

Į etiketę įterpti žemėlapio mastelį:

`map_get( item_variables( 'map'),'map_scale')`

Įterpti į etiketę žemėlapio x koordinatę:

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Dokumentacija
### Savybė: apdorojimo algoritmų patobulinimai
Apdorojimų algoritmai buvo peržiūrėti ir dokumentuoti. Paspaudus Pagalbos mygtuką bus atverta QGIS svetainė ir bus rodomas algoritmo aprašymas su išplėsta dokumentacija ir pavyzdžiais.

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

Šią savybė finansavo QGIS Grant Proposal

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## Simbologija
### Savybė: nuo duomenų priklausantis simbolių sluoksnio matomumas
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: įrašyti ir atstatyti spalvų rampą, naudojamą vienos juostos pseudospalvų braižymui
Šią savybę sukūrė Alexander Bruy
### Savybė: prie simbolių vienetų sąrašo pridėti taškai ir coliai
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas spalvų rampos mygtuko valdiklis
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: stilių tvarkymo perdarymas ir atnaujinimas
Stilių valdymas buvo stipriai pagerintas. Tarp naujovių yra:
- Pridėta nauja parankinių grupavimo sistema, kuri yra numatytoji sąrašo valdikliui
- Simbolių sąrašo valdiklyje parinkta žyma / išmani grupė išlieka perjungiant sluoksnius (ir tarp sesijų)
- Simbolių sąrašo valdiklis atnaujins žymą / išmanią grupę, kai naudotojai prideda / pervadina / išima kategorijas
- Naudotojai dabar gali tiesiogiai žymėti bei pridėti į parankinius simbolius, įrašydami juos į duomenų bazę
- Stilių valdymo supaprastinimui, grupės buvo išimtos ir pilnai pakeistos žymomis
- Žymos integruotos į importavimo/eksportavimo naudotojo sąsają

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: spalvos ir permatomumo nustatymo keliems elementams rastro braižyme palaikymas
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: spalvos mygtuko iškrentančiame meniu rodyti alfa slankiklį
Leidžia greitai taisyti spalvos alfą

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pseudospalvų braižytojo palaikymas rastro tempimo įrankinės veiksmuose
Šią savybę sukūrė Mathieu Pellerin
### Savybė: permatomumo palaikymas paletės braižyme
QGIS 3.0 jau galima keisti permatomumo reikšmę unikalioms reikšmėms paletės braižyme.

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: rastro automatinis ištempimas atnaujinant drobę
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

Šią savybę sukūrė Even Rouault
### Savybė: anotacijų turinio paraščių kontrolė
Leidžia nustatyti kairę/viršutinę/dešinę/apatinę anotacijos turinio paraštes.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: galima keisti anotacijų stilių naudojant simbolinius užpildymus
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

Taip pat braižymo efektus ir nuo duomenų priklausančius simbolių parametrus.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: taškų spiečiaus braižymas
Naujas simbolių braižymas, grupuojantis greta esančius taškus į vieną grupę, braižoma žymeklio simboliu. Pasirinktinai, etiketė rodo į vieną simbolį sugrupuotį geoobjektų skaičių.

Taipogi taško pastūmimo braižymas buvo patobulintas, konkrečiau:
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- konkretūs taškai dabar teisingai rodomi jų pačių pažymėjimo būsenoje
- daug kodo sutvarkymo + dokumentavimas.

Programuotojams: QgsPointDisplacementRenderer buvo padalintas į naują grynai virtualią QgsPointDistanceRenderere bazinę klasę, kuri apdoroja spiečių aptikimą ir taškų grupavimą. Naujas spiečiaus braižymas perpanaudoja bazinę klasę, kad išvengtų kodo dubliavimo.

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann, Qtibia Engineering (Tudor Barascu), Karl-Magnus Jönsson, Geonesia (Nicolas Ponzo) ir keli papildomi anoniminiai rėmėjai, kurių dosnus įnašas taip pat labai vertinamas!

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### Savybė: nauji QGIS 3.0 žemėlapio spalvinimo algoritmai
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

Šią savybė sukūrė Nyall Dawson
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: leidžia laikinai išjungti simbolinius sluoksnius
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: paprastas diskretinių rastrų spalvinimas
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

Unikalių reikšmių skaičiavimas vykdomas foninėje gijoje, kad naudotojo sąsaja neužstrigtų dideliems (ar nutolusiems) rastro sluoksniams. Papildomai naudotojai gali rankiniu būdu pridėti konkrečias klases pagal poreikį bei keisti susietas taško reikšmes bet kokiai esamai klasei. Taip pat galima vienu metu ištrinti kelias klases bei keisti spalvą, permatomumą ar etiketes kelioms klasėms iš karto.

Spalvų paletės gali būti įkeliamos iš tekstinio failo su ESRI clr/GDAL/GRASS palaikomais spalvų lentelių formatais. Spalvų paletės gali būti įrašomos į tekstinį failą dalinimuisi.

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Užrašai
### Savybė: etikečių šrifto dydį galima nurodyti mm/taškais
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: savų etikečių įrankinė dabar visada įjungta
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## Diagramos
### Savybė: nuo duomenų priklausančios savybės
Į diagramas pridėta daugiau nuo duomenų priklausančių savybių:
- Atstumas
- Prioritetas
- ZIndeksas
- YraKliūtis
- Rodyti
- VisadaRodyti
- Diagramos pradžios kampas

Šią savybę finansavo QGIS Grant Program

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Braižymas
### Savybė: gyvų sluoksnių palaikymas
QGIS 3.0 palaiko gyvus sluoksnius. Šie sluoksniai automatiškai perbraižomi gražiu, nemirgančiu būdu kas jūsų nurodytą intervalą. Gyvi sluoksniai puikiai tinka sekti pastoviai kintančius duomenis, tokius kaip mašinų parkas ar pulkas paukščių, kurių telemetrijos duomenis jūs turite.

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

Šią savybę sukūrė Kartoza & North Road
### Savybė: iššaukti sluoksnio atnaujinimą arba sluoksnio veiksmus per PostgreSQL NOTIFY signalą
Sekant gyvų sluoksnių efektus, tai leidžia iškviesti veiksmus ar sluoksnio atnaujinimą QGIS'e tik kai duomenų bazė pranešą QGIS'ui, kad jis turėtų kažką daryti. Taip bus naudojama mažiau resursų atnaujinant kas intervalą ir naudodami šią savybę jūs galite net parašyti pokalbių aplikaciją QGIS'e :)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### Savybė: etikečių dėliojimo rezultatą dėti į podėlį, kad būtų išvengta bereikalingo drobės perpaišymo atnaujinant
Šis pakeitimas leidžia po žemėlapio braižymo įrašyti į piešinio podėlį etikečių dėliojimo rezultatus. Jei podėlio piešinys gali būti iš naujo panaudotas kitam braižymui, jis ir bus panaudotas, taip vengiant nereikalingų visų sluoksnių, dalyvaujančių etikečių problemoje, perbraižymo. Tai reiškia, kad **drobės atsinaujimas dėl pakeitimų bet kuriame sluoksnyje BE ETIKEČIŲ yra daug greitesnis**. (Pakeitus sluoksnį, kuris yra etikečių braižymo uždavinio dalis, vis tiek reikia visus sluoksnius perbraižyti iš naujo)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: tinklelio braižiklis taškų pastūmimui
Tinklelio braižiklis taškų pastūmimui

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## Skaitmeninimas
### Savybė: viršūnių intervalo žymėjimas taško įrankyje
Ši savybė leidžia pažymėti vieno geoobjekto **viršūnių intervalą**.

Aktyvuoti šią savybę galima paspaudus **Shift+R** - po to reikia paspausti pirmą ir paskutinį tašką geoobjekte - tai pažymės visas viršūnes tarp jų.

Intervalo žymėjimą galima nutraukti bet kuriuo metu dešiniu arba Esc klavišo paspaudimu.

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Savybė: pridėta numatytosios Z reikšmės parinktis
Geopaketų/Shape failų kūrimas: dabar su parinktimi turėti Z reikšmes

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Lisovenko / Paul Blottiere
### Savybė: geoobjekto perkėlimas dabar laimi dėl išmanesniojo skaitmeninimo
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

Šią savybę sukūrė Denis Rouzaud
### Savybė: geoobjekto kopijavimo/perkėlimo funkcionalumas pridėtas į žemėlapio geoobjekto perkėlimo įrankį
Tai leidžia vienu veiksmu kurti geoobjekto kopiją ir juos perkelti

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

Šią savybę sukūrė Denis Rouzaud
### Savybė: braižymas su poslinkiu
Dabar galite naudoti skaitmeninimo įrankį su poslinkiu, kaip parodyta šioje iliustracijoje.

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### Savybė: Viršūnės įrankio perdarymas
Taško įrankis (pervadintas į viršūnės įrankį) buvo visiškai perdarytas, kad taptų lankstesnis. Keli svarbesni pakeitimai yra:
1. Naudotojams nebereikia iš pradžių pažymėti geoobjektą, o tik tada keisti jo viršūnes antru žingsniu. Įrankis dabar gali dirbti iš karto su keliais geoobjektais tuo pačiu metu. Todėl daug lengviau pažymėti kelių geoobjektų viršūnes ir perkelti arba ištrinti jas vienu metu. Jei yra poreikis apriboti žymėjimą tik vienu geoobjektu, tai galima padaryti iš pradžių pažymėjus geoobjektus žymėjimo įrankiu - tokiu atveju viršūnių įrankis dirbs tik su pažymėtų geoobjektų viršūnėmis.
2. Vietoje darbo tik su dabar pažymėtu sluoksniu, įrankis gali dirbti su visais sluoksniais, kurie yra redagavimo režime. Perkėlimas geoobjektų, kurie logiškai priklauso vienas kitam, bet yra skirtinguose sluoksniuose pasidarė daug paprastesnis. Visgi, dabartinis sluoksnis suprantamas, jei yra keli pasirinkimai parenkant viršūnes.
3. Geoobjektai ir jų viršūnės paryškinamos kai naudotojas užveda pelės žymeklį virš jų, taip duodant vizualią informaciją.
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. lengviau tiksliai padėti viršūnes (nes nereikia visą laiką naudoti jėgos spaudžiant pelės mygtuką)
6. viršūnes neperkeliamos netyčia
7. galima atšaukti veiksmą
8. galima pastumti žemėlapį spaudžiant tarpą perkeliant tašką

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Savybė: viršūnės įrankis: vidurio žymekliai viršūnių pridėjimui
Patobulintas viršūnių įrankis dabar taipogi rodo papildomus žymeklius geoobjektų linijų viduryje. Paspaudus tokį žymeklį pridedama nauja viršūnė. Dabartinis viršūnių pridėjimo būdas du kartus spaudžiant segmentus išsaugotas.

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Savybė: viršūnių įrankis: tęsti liniją
Keičiant linijų geometrijas su viršūnių įrankiu, perkėlus pelę link pirmos ar paskutinės viršūnės bus rodomas papildomas žymeklis šalia paskutinio taško. Spaudžiant šį žymeklį bus pridėta viršūnė geometrijos pabaigoje.

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Savybė: viršūnių įrankis: išmaniojo skaitmeninimo įrankinės palaikymas
Išmaniojo skaitmeninimo skydelis dabar dirba ir su viršūnių įrankiu - galima įvesti naujos arba esamos viršūnės koordinates taip kaip ir kituose skaitmeninimo žemėlapio įrankiuose.

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Duomenų valdymas
### Savybė: paslinkti iki dabartinio geoobjekto atributų lentelėje
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

Šią savybę sukūrė Marco Hugentobler
### Savybė: CRS-apimties žemėlapis projekto savybėse
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### Savybė: pagalbinės saugyklos palaikymas
Vektorinių sluoksnių savybės atsirado nauja kortelė, skirta papildomos saugyklos valdymui:

Nuo duomenų priklausančiame meniu atsirado nauja parinktis - „Laikyti duomenis projekte“. Ji leidžia lengvai valdyti papildomus savybės duomenis:

Pagalbiniai duomenys saugomi sqlite duomenų bazėje ir valdomi OGR duomenų tiekėjo pagalba (o ne spatialine tiekėjo), kad duomenų bazės failai būtų kiek galima mažesnis. Šis duombazės failas (su praplėtimu *.qgd*) įrašomas arba šalia projekto failą, arba įtraukiamas tiesiai į naują *.qgz* formatą.

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### Savybė: metaduomenų pertvarkymas
Pertvarkyta QGIS metaduomenų sistema. QGIS 3.0 buvo pridėta mūsų pačių vidinė, formalizuota metaduomenų schema, kuri yra nepriklauso nuo QGIS projekto failo formato. Pridėtos naujos API galimybės skaityti ir rašyti sluoksnių metaduomenis. Mes atskyrėme metaduomenų rodyma nuo redagavimo ir pridėjome naują metaduomenų redagavimo įrankį. Metaduomenys šiuo metu įrašomi į projekto failą. Taipogi gali būti įrašyti kaip XML failas šalia failais paremtų sluoksnių arba vietinėje sqlite duombazėje nutolusiems sluoksniams (pvz. PostGIS).

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### Savybė: jungtinis duomenų šaltinių valdymo dialogas
Vienas jungtinis dialogas, skirtas visų duomenų sluoksnių valdymui ir sluoksnių įkėlimui.

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

Šią savybę finansavo Boundless

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Savybė: išimtas OSM atsiuntimo įrankis
Mes išėmėme OSM atsiuntimo įrankį, buvusį 2.x QGIS versijose. Mes siūlome naudoti priedą QuickOSM, kuris paruoštas QGIS 3.0.
## Formos ir valdikliai
### Savybė: leisti kontroliuoti konkrečių redagavimo valdiklių etiketes
Pernešimo ir numetimo dizaineryje, du kartus paspaudus ant elemento leidžiama nurodyti, ar etiketė turi būti rodoma kiekvienam konkrečiam elementui.

Šią savybę sukūrė Matthias Kuhn
### Savybė: leisti konfigūruoti geoobjektų susiejimo/atsiejimo mygtukus ryšių redaktoriaus valdiklyje
Šią savybę sukūrė Matthias Kuhn
### Savybė: sąlyginis kortelių ir grupių rodymas
Tai prideda naują konfigūravimo parinktį pagal sąlygas rodyti ar slėpti korteles ir grupes pernešimo ir numetimo dizainerio formose. Konfigūravimas daromas du kartus paspaudus dizainerio medyje laukų konfigūravimo sąsajoje. Galima įvesti išraišką, kontroliuojančią matomumą. Išraiška bus įvertinta kiekvieną kartą pasikeitus formos reikšmėms ir kortelė arba grupė bus atitinkamai parodoma arba paslepiama.

Šią savybę sukūrė Matthias Kuhn
### Savybė: išmasnesni numatytieji redagavimo valdikliai su juos parenkančiais priedais
Dabar valdikliai gali teikti įvertinimą, kaip gerai jie galėtų valdyti lauko tipą. Dėl to gaunami geresni numatytieji valdikliai.

Papildomai gali būti pridėti priedai parinkti valdiklio tipą funkcijoje arba išorinėje informacijoje. Vienas iš jų naudoja PostgreSQL lentelę, leidžiančią nustatyti valdiklio tipą ir konfigūraciją, naudojamą kiekvienam laukui.

Automatiškai parinkti RelationReference valdiklius išoriniams raktams.

Šią savybę sukūrė Patrick Valsecchi
### Savybė: laukų apribojimai gali būti įjungti arba išjungti
Neįjungti apribojimai tik parodo naudotojui įspėjimą, bet nedraudžia įrašyti geoobjekto. Įjungti apribojimai blokuoja nevalidžių geoobjektų įrašymą. Taigi dabar turime minkštus įspėjimus! Bet kokie apribojimai, aptikti pas tiekėją, visada įjungti.

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

Šią savybę finansavo OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pridėti sluoksnių apimties veiksmai
Atributų lentelėje dabar yra naujas mygtukas, kviečiantis veiksmus, kurie dabar priklauso nuo konkrečių geoobjektų, o ne nuo sluoksnio. Paprastai jie vykdo veiksmus, priklausančius nuo geoobjektų arba pažymėjimo.

Šią savybę sukūrė Matthias Kuhn
### Savybė: rodyti lauko reikšmes automatiniame pabaigimo formos filtro režime
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: parinkimo dialoge pridėtos klavišų kombinacijos priartinimui prie geoobjekto ir geoobjektų mirksėjimui.
Leidžia labai greitai naviguoti ir identifikuoti geoobjektus, kurie atitinka formoje nurodytą kriterijų

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: parinkimo formos skaitiniams laukams pridėtas tarp/ne tarp filtras
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Sluoksnių legenda
### Savybė: nepažymėtų sluoksnių paslėpimo veiksmas
Leidžia greitai paslėpti visus nepažymėtus sluoksnius. Tai patogu, kai turite didelį projektą ir norite greitai paslėpti visus sluoksnius išskyrus kelis

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: grupių viduje esančių sluoksnių matomumo ergonomijos keitimas
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- Nebėra pusiau įjungtos grupės būsenos
- **Ctrl-paspaudimas** nepažymėtai grupei pažymės grupę ir visus jos vaikus.
- Paspaudus nepažymėtą sluoksnį bus pažymėtas sluoksnis ir visi jo tėvai.
- Ctrl-paspaudus pažymėta grupę bus nužymėta grupė ir visi jos vaikai.
- Ctrl-paspaudus pažymėtą sluoksnį bus nužymėtas sluoksnis ir visi jo tėvai.
- Šiuos veiksmus rasite medžio dorinio kontekstiniame meniu.
- Nematomi sluoksniai, kadangi jie ar jų tėvai yra išjungti yra rodomi pilkai.

Šią savybę sukūrė Even Rouault
## Žemėlapio maketas
### Savybė: maketo lentelės tinklelio horizontalių ir vertikalių linijų braižymo valdymas
Dabar galima nepriklausomai valdyti horizontalių ir maketo lentelių elementų vertikalių linijų braižymą. Toks lankstumas išplečia šio elemento stilizavimo galimybes.

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: pertempkite qpt į QGIS, kad sukurtumėte naują maketą pagal šabloną
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: maketo legendos elementų etikečių tarpų tarp linijų keitimas
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: leisti keisti CRS žemėlapio elementams
Tai leidžia skirtis žemėlapio elementų ir kitų drobės/projektų elementų CRS būti skirtingoms. Taip pat leidžia skirtingiems žemėlapio elementams turėti skirtingas CRS, pavyzdžiui perdengiantis žemėlapis gali turėti kitą CRS nei pagrindinis žemėlapis.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: laikant shift braižant poliliniją/poligoną, apribojami linijų kampai
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: daugiau nuo duomenų priklausančių valdiklių
Elementas **rėmas** ir **fono spalvos** Nuo duomenų priklausančios **svg spalvos ir kontūro storis maketo piešinio elementams** (Ypač naudinga, kai piešinukas rodo šiaurės rodyklę!) Nuo duomenų priklausantys **legendos antraštė ir stulpelių skaičius** Nuo duomenų priklausančios **mastelio spalvos ir plotis**

Šią savybę finansavo QGIS Grant Program

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: žemėlapio maketo pertvarkymas
Tai svarbus maketų tvarkymo QGIS kodo pertvarkymas.

Svarbiausi pakeitimai:
- Nauja QgsLayoutManager klasė, kuri naudojama maketų saugojimui ir serializavimui/deserializavimui. QgsLayoutManager prijungtas prie QgsProject. Tai leidžia baziniam kodui prieiti prie maketų, prisegtų prie projekto. Visas maketų apdorojimas perkeltas iš app į bazę, dėl ko daug lengviau serveriui (ir kitiems ne nuo app priklausantiems projektams. QField/roam?) prieiti prie projekto maketų be trapaus xml nagrinėjimo.
- Maketo langai kuriami pagal poreikį ir sunaikinami uždarant. Dėl to nebelieka sunkaus reikalavimo kurti maketo langus ir valdiklius kiekvienam maketo elementui įkeliant projektus. **Tau buvo pagrindinė priežastis, kodėl projektų su maketais įkėlimas buvo toks lėtas**. Dabar maketo langai kuriami tik kai langas atidaromas ir naikinami uždarius langą. Maketo elementų konfigūravimo valdikliai taip pat kuriami pagal poreikį (kai elementas parenkamas), o ne sukuriant visus valdiklius iš anksto.
- Šalutinis maketo lango naikinimo uždarius pliusas yra tai, kad **mums nebereikia kentėti nuo Qt rikto**, kuris blokavo plaukiojančių skydelių naudojimą moaketų languose. Dabar elementas/kompozicija/skydeliai gali plaukioti! Daug gražesnis pilno ekrano veikimas su kompozicijomis kelių vaizduoklių variantuose.
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- Daug kodo valymo ir išėmimo

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

Šią savybę finansavo Swiss QGIS User Group ir daug daugiau!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Analizės įrankiai
### Savybė: rastro unikalių reikšmių skaičiavimas apdorojimui
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## Apdorojimas
### Savybė: naujas linijų pastūmimo algoritmas
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas vienpusių buferių algoritmas
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pridėtas paprastinimo metodo pasirinkimas
Šis pakeitimas leidžia pasirinkti, kurio metodo pagalba paprastinamos geometrijos: atstumo pagrindu (Douglas Peucker), ploto pagrindu (Visvalingam) ar pritraukimo prie gardelės principu.

Visvaligam paprastai reiškia kartografiškai labiau tenkinantį paprastinimo rezultatą, lyginant su atstumu paremtu metodu.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: išvesties geometrijų tipų palaikymas modeliuose
Modelio vaikinių algoritmų įvestis dabar filtruojama tik tiems, kurie generuoja tinkamus geometrijos tipus kito vaikinio algoritmo įvesčiai.

Šią savybę sukūrė Alexander Bruy
### Savybė: kampo riba glotninimo algoritme
Pridėta QgsGeometry::smooth parinktis neglotninti segmentų, trumpesnių nei konkreti riba arba stačių kampų, su kampu viršijančių ribą

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: geresnis Z/M dimensijų palaikymas ir kreivinės geometrijos
Dabar daug daugiau algoritmų supranta Z/M reikšmes ir neišmeta šios informacijos bei papildomai daug algoritmų teisingai palaiko kreivines geometrijas be priverstinio tokių geometrijų segmentavimo.
### Savybė: į apdorojimą pridėti rastro analizės algoritmai
Šie algoritmai buvo pridėti į apdorojimą iš rastro analizės priedo:
- Aspektas
- Nuolydis
- Atsparumas
- Šešėliavimas
- Reljefas

Dabar šiuos algoritmus galima naudoti scenarijuose, modeliuose ir paketiniame apdorojime.

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: naujas konkrečių viršūnių ištraukimo algoritmas
Šis algoritmas leidžia ištraukti konkrečias geometrijų viršūnes. Pvz. jūs galite ištraukti pirmą ar paskutinę geometrijos viršūnę.

Algoritmas priima kableliais atskirtą viršūnių pozicijų sąrašą ištraukimui, pvz. 0 = pirma viršūnė, 1 = antra viršūnė ir t.t. Neigiamos pozicijos gali būti naudojamos viršūnių skaičiavimui nuo pabaigos. Pvz. -1 = paskutinė viršūnė, 2 = priešpaskutinė viršūnė.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: duoti prieigą įrankinėje prie zonų statistikos iš Zonų statistikos priedo
Šią savybę sukūrė Alexander Bruy
### Savybė: pridėtas spatialite SQL vykdymo algoritmas
Šią savybę sukūrė Mathieu Pellerin
### Savybė: naujas linijų pratęsimo algoritmas
Leidžia pratęsti linijas nurodytu atstumu linijos pradžioje arba pabaigoje

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas ištraukimo pagal išraišką algoritmas
Filtruoja įvesties sluoksnį pagal išraišką

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pridėtas importavimo į spatialite algoritmas
Šią savybę sukūrė Mathieu Pellerin
### Savybė: interpoliacijos algoritmai
Suteikiama prieiga įrankinėje prie IDW ir TIN interpoliacijos iš Interpoliacijos priedo

Interpoliacijos priedas dėl to buvo išimtas

Šią savybę sukūrė Alexander Bruy
### Savybė: naujas geometrijos skaičiavimo pagal išraišką algoritmas
Šis algoritmas atnaujina esamas geometrijas (arba sukuria naujas geometrijas) įvesties geoobjektams naudojant QGIS išraišką. Tai leidžia sudėtingas geometrijos modifikacijas, kurios gali naudoti visą QGIS išraiškų variklio lankstumą keičiant ir kuriant geometrijas išvesties geoobjektams.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pritraukti geometrijas prie sluoksnio algoritmo
Geometrijos pritraukimo priedas buvo perkeltas į apdorojimą

Geometrijų pritraukimo algoritmas leidžia pritraukti prie kitų sluoksnių tipų, palaiko taškų/linijų sluoksnius

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas įvesties tipas išraiškoms
Tai prideda naują įvesties tipą išraiškos įvestims. Išraiškos įvestys gali būti susietos su tėviniu sluoksniu, kad kūrėjas rodytų teisingus laukus ir sluoksnių kintamuosius.

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: SplitWithLines
Algoritmas SplitLinesWithLines pervadintas į SplitWithLines. Kaip įvestis priimamas ir poligonas. Padalinimui naudojamos tik pažymėtos linijos (jei apdorojimas nustatytas naudoti tik pažymėjimą). Problemų žurnalo pranešimai, jei bandant dalinti multigeometrijas įvyko klaidų. Atnaujinta pagalba.

Šią savybę sukūrė Bernhard Ströbl
### Savybė: neprieinamumo poliaus algoritmas
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: ištraukti pagal atributą dabar gali ištraukti pagal null/notnull reikšmes
Pridėtas filtro palaikymas, kur atributo reikšmė gali būti null arba not null

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: atributų indekso kūrimo algoritmas
Leidžia kurti indeksą pagal sluoksnio atributą, kad būtų greitesnis filtravimas

Palaikymas priklauso nuo to, koks yra naudojamas sluoksnio duomenų tiekėjas

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
Paprasčiausiai išima bet kokias geometrijas iš įvesties sluoksnio ir grąžina geoobjektus tik su atributais

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

Vienas jungtinis algoritmas leidžia lankstesnius modelius, kur lauko tipas gali būti nežinomas iš anksto.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: intensyvumo priedas perkeltas į apdorojimo algoritmą
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas geometrijų ortogonalizavimo algoritmas
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: tinklo analizės algoritmai
Į apdorojimą pridėti trumpiausio kelio ir aptarnavimo zonos algoritmai

taipogi leidžiama skaičiuoti trumpiausią kelią iš taško į visus taškus sluoksnyje, arba iš visų taškų sluoksnyje į galutinį tašką. Ir kurti aptarnavimo zonas visiems taškams sluoksnyje.

Dėl šio pakeitimo buvo pašalintas kelių grafo priedas.

Šią savybę sukūrė Alexander Bruy
### Savybė: eksportuoti apdorojimo modelius kaip PDF/SVG
Greta apdorojimo modelių eksportavimo kaip bitmap piešiniai, dabar galima eksportuoti į nuo rezoliucijos nepriklausomus PDF ir SVG. Tai leidžia gauti didelės raiškos modelių eksportą, kuris gali būti įtrauktas į publikuojamus mokslinius darbus ir knygas.

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: naujas lentelių išvalymo algoritmas
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
Šią savybę sukūrė Victor Olaya
### Savybė: netinkamų geometrijų tvarkymo algoritmas, naudojantis savo makeValid() variantą
Šią savybę sukūrė Alexander Bruy
### Savybė: prie scenarijų ir modelių gavimo dialogo pridėta paieška
Šią savybę sukūrė Alexander Bruy
### Savybė: bendrinis centroido algoritmas
Perdarytas centroido algoritmas, apdorojantis nepoligonų sluoksnius

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pagerintas viršūnių ištraukimo algoritmas
Viršūnių ištraukimo algoritmas dabar įrašo viršūnių indeksą, atstumą linijoje ir kampą viršūnėje

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: naujas taškų vertimo (perkėlimo) algoritmas
Leidžia pastumti geometrijas x/y postūmiu

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pagerintas apdorojimo modeliuotojo langas
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: naujas unikalių rastro reikšmių ataskaitos algoritmas
Pridėtas naujas algoritmas, grąžinantis kiekvienos unikalios nurodyto rastro sluoksnio reikšmės skaičių ir plotą.

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: TauDEM tiekėjas pašalintas iš Apdorojimo pagrindo
Mes išėmėme TauDEM tiekėją iš apdorojimo.

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### Savybė: atsisiųsti failą iš apdorojimo
Atsisiųsti failą iš apdorojimo. Užklausa nutolusiam API, norint gauti geojson

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Savybė: optimizuotų taškų palei geometriją algoritmas
Taipogi palaiko poligono geometrijas, moka apdoroti null geometrijas, įrašo kiekvieno taško pradinį linijos kampą šalia atstumo.

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: rikiavimo pagal išraišką algoritmas
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programos ir projekto parinktys
### Savybė: naujas suspausto projekto formatas .qgz
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Savybė: pridėtas naudotojų profilių palaikymas
Visi naudotojo nustatymai/priedai ir t.t. dabar įkeliami į atitinkamos platformos programos duomenų vietą, o ne .qgis3/2. Nustatymai ir priedai kiekviename profilyje dabar izoliuoti vienas nuo kito.

Tai leidžia turėti skirtingus paleidimo nustatymus priklausomai nuo naudotojo poreikių, pvz. testavimo, gamybinės veiklos, demonstravimo ir pan.

Profilio meniu leidžia persijungti tarp profilių bei kurti naujus.

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## Naršyklė
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
Leidžia paprastai laikyti jūsų laikinus sluoksnius PostGIS'e

Šią savybę sukūrė Martin Dobias
### Savybė: pašalinta atskira QGIS naršyklės programa
Mes išėmėme atskirą QGIS naršyklės programą, kuri būdavo teikiama kartu su QGIS 2.x. Šios aplikacijos naudotojai beveik nenaudojo, o ją reikėjo papildomai prižiūrėti, ko mes nebenorime daryti nuo 3.0 versijos.
## Duomenų tiekėjai
### Feature: New unified \'add layer\' dialog
Dabar galite naudoti vieną dialogą, kad pridėtumėte didžiulę įvairovę duomenų formatų į QGIS.

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Savybė: GeoPackage
- apdorojimas pagal nutylėjimą naudoja pkg
- įrašyti kaip pagal nutylėjimą rašo pkg
- naujo sluoksnio kūrimas pagal nutylėjimą naudoja pkg
- naršyklės pertempimas ir numetimas importuoja sluoksnius

Šią savybę sukūrė Alessandro Pasotti
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
Šią savybė sukūrė Nyall Dawson
### Savybė: Z/M geometrijų palaikymas gpkg, spatialite ir atminties sluoksnių tiekėjuose
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

Šią savybę sukūrė Mathieu Pellerin, Alexander Bury, Paul Blottiere
### Savybė: unikalių ir ne-null apribojimų valdymas
Automatinis unikalių ir ne-null apribojimų aptikimas tiekėjo pusėje įgyvendintas postgres, spatialite, ogr tiekėjams

Kliento pusės unikalūs ir ne-null apribojimai gali būti nurodyti QGIS.

Unikalumo apribojimas įjungiamas atributų formoje

Šią savybę finansavo OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: GeoNode integracija
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

Jei GeoNode naudoja QGIS Serverį, o ne GeoServerį, jūs galite kopijuoti ir įkelti stilius iš serverio ir pritaikyti juos savo vietiniame sluoksnyje, kad jūsų WFS sluoksnis būtų braižomas lygiai taip pat, kaip jis braižomas serveryje (kaip parodyta šiame animuotame GIF).

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### Savybė: aptikti spatialite tiekėjo numatytasias reikšmes
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: kurti spatialite tiekėjo atributų indeksą
Leidžia kurti spatialite sluoksnių atributų indeksą

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: pridėtas masyvų palaikymas
Palaiko postgres, spatialite

Šią savybę sukūrė Patrick Valsecchi
### Savybė: PostGIS duomenų tiekėjo HStore palaikymas
### Savybė: PostgreSQL ryšių auto-aptikimas
Šią savybę sukūrė Patrick Valsecchi
### Savybė: duomenų priklausomybės tarp sluoksnių
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

Šią savybę sukūrė Hugo Mercier
### Savybė: dxf eksportas: perprojektavimo palaikymas
Šią savybę sukūrė Juergen E. Fischer
### Savybė: įkelti/įrašyti GPKG ir Spatialite stilių duomenų bazėje
Šią savybę sukūrė Even Rouault
### Savybė: pagerintas numatytųjų dalykų apdorojimas
Pagerintas numatytųjų dalykų apdorojimas (įskaitant tiekėjo numatytąsias sąlygas, QGIS išraiškų numatytąsias reikšmes) ir automatinis unikalių reikšmių apribojimų apdorojimas sluoksniuose

Visi laukai su unikalių reikšmių apribojimu garantuotai turės reikšmę, kuri bus unikali.

Tai taip pat reiškia, kad po kai kurių keitimo veiksmų (pvz. kopijavimo-įkėlimo, geoobjektų padalinimo ir pan.) kur reikia, atributų reikšmės bus pakeistos į numatytąsias.

Šią savybę finansavo Canton of Zug and the QGEP project

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## QGIS Serveris
### Savybė: QGIS serverio pertvarkymas
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

Prieš metus, mažiukas trolis iš Šveicarijos paskambino varpeliu apie stiprų poreikį meilei serverio kodui. Iš tiesų, API buvo užrakinta kelių senų QGIS serverio metodų. Jei trumpai, QGIS serveris po kelis kartus savaip nagrinėdavo qgs projekto failą ir sukurdavo priklausomybes į tą QGIS dalį, kurią norėjome išmesti.

Kadangi atiduoti serverio kodą kitiems nebuvo tinkamas variantas, teko jį perdaryti. Susiję dalyviai nusprendė įsitraukti į kodo sprintą Lyon'e, Prancūzijoje, pasidalinti savo vizija, planuoti darbus ir galų gale padėti įvykti štai kam:

Aukšto lygio perrašymas

Visos paslaugos (WMS GetMap, WFS GetFeature, GetLegendGraphics, WCS, GetPrint ir pan.)

Naujos savybės
- Kelių gijų braižymas, kaip ir darbastalyje
- Nauja parinktis pasitikėti sluoksnio metaduomenimis, taip pagreitinant projekto įkėlimą
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- Pilnas Python bindings palaikymas serverio API
- Serverio paslaugos - priedai kaip tiekėjai

Gilūs, sudėtingi ir nedėkingi uždaviniai
- Išimti visus singleton kvietimus
- Nutraukti visi ryšiai su su senu QGIS projekto failo tyrėju
- Mažinti priklausomybes su GUI biblioteka. Kadangi žemėlapio braižymui reikalingi šriftai, visiškai jų pašalinti nebuvo galima.

Infrastruktūros užduotys
- Sukurti OGC suderinamumo platformą ir integruoti ją į pastovaus integravimo platformą. Atitikimo ataskaitos dabar publikuojamos tests.qgis.org
- Add unit tests \... and again more unit tests
- Patikrinti QGIS serverio saugumo spragas (SQL įterpimus ir kitas piktybines atakas)
- Pradėti profiliuoti ir matuoti greitaveiką. Šiam darbui dar reikia meilės - ir finansavimo - kad būtų pasiektas

Pristatyta FOSS4G-EU birželį

Šią savybę finansavo QGIS.ORG rėmėjai
### Savybė: galimybė segmentuoti geoobjekto informacijos geometriją serveryje
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## Priedai
### Savybė: patikimo statusas atimtas iš Priedų tvarkyklės
<https://github.com/qgis/QGIS/pull/5272>
### Savybė: keitimas neprisijungus: pridėkite požymį, kad būtų kopijuojami tik pažymėti geoobjektai
Tai praplečia redagavimo neprisijungus galimybes dirbti tik su didelių sluoksnių poaibiu

Šią savybę finansavo DB Fahrwegdienste GmbH

Šią savybę sukūrė Matthias Kuhn
### Savybė: GDAL įrankiai perkelti į apdorojimą
GDALTools priedas buvo išimtas.

Visos funkcijos, kurios anksčiau buvo GDALTools priede, buvo perkeltos į QGIS apdorojimo karkasą, leidžiant naudoti šiuos įrankius ir scenarijus, modelius ir vykdyti juos paketiniame režime. Papildomai mes atnaujinome algoritmus naujais parametrais, panaudojom paskutines GDAL versijas ir pagerinome bendrą UI/UX parodydami kai kuriuos išmanesnius parametrus, kaip sukūrimo parinktys, NODATA reikšmių nustatymus ir pan.

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: leisti diegti priedus iš vietinių ZIP paketų
Dabar lengviau įdiegti priedus rankiniu būdu, nereikia išpakuoti naudotojo profilio aplanke rankomis.

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

Šią savybę sukūrė Alexander Bruy
### Savybė: priedai gali teikti savo pagalbą išraiškų lange
Priedai, teikiantis išraiškas, gali pridėti savo pagalbą, parašyta HTML eilutėmis.

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programavimas
### Savybė: geometrijos klasės atnaujinimai
Stipriai perdarytos QGIS geometrijos klasės. Senos klasės pervadintos (pagal apačioje pateiktą lentelę). Naujos geometrijos klasės tinkamai išsaugos Z ir M atributus, jei tokie bus.

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

Tau pagaliau sugrąžina tvarkingus pavadinimus į geometrijos API
### Pervadinimai
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

Šią savybę sukūrė Matthias, Nyall ir kiti
### Savybė: užduočių tvarktojas
Pridėtas karkasas foninių užduočių kūrimui, su kuriais sąveikaujama per centrinę tvarkyklę

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

Pridėtas paprastas python metodas QgsTask.fromFunction užduočių sukūrimui iš funkcijos nekuriant QgsTask poklasių

Priklausančių užduočių palaikymas

Nutraukus užduotį, nutraukiamos ir visos nuo jos priklausančios užduotys.

Į užduočių tvarkyklę pridėtas priklausomų sluoksnių valdymas

Jei užduotis turi priklausomus sluoksnius, kurie tuoj bus pervadinti, užduotis automatiškai nutraukiama

QgsTasks gali turėti použduočių

Dabar QgsTask gali turėti použduočių QgsTasks aibę, kviečiant QgsTask::addSubTask. Použduotys gali turėti savo priklausomas užduotis.

Použduotys nematomos naudotojams, naudotojai mato tik bendrą progresą ir tėvinės užduoties būseną.

Tai leidžia kurti užduotis, kurios pačios sukurtos iš daug mažesnių komponentų. Užduočių tvarkyklė vis dar apdoros použduočių paleidimą ir planavimą, taigi použduotys gali būti vykdomos paraleliai (jei jų priklausomybės tai leidžia).

Použduotys pačios gali turėti savo použduotis.

Šis pakeitimas skirtas tam, kad apdorojimo algoritmų ir modelio algoritmų koncepcija būtų verčiama tiesiai į užduočių tvarkyklės architektūrą.

Šią savybę finansavo QGIS Grant Program

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
QgsDataItem įgyvendinimas gali teikti hasDragEnables(), mimeUri() ir QgsCustomDropHandle įgyvendinimus, kad būtų dirbama su savo elementų numetimu.

Šią savybę sukūrė Martin Dobias

{{<content-end >}}
