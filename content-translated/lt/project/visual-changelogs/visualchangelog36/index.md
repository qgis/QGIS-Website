---
HasBanner: false
draft: false
releaseDate: '2019-02-22'
section: projektą
sidebar: true
title: QGIS 3.6 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.6 pakeitimai{#changelog36 }
![image1](images/projects/f335c2ee37b714ad6eec143246d947f09a5ff2f1.png)

Laidos data: 2019-02-22

Geriausia visų laikų QGIS laida! Su QGIS 3.6 ateina didžiulis skaičius naujų pakeitimų - apie svarbiausius iš kurių parašysime čia. Kaip visada, mes primename, kad QGIS yra atviro kodo projektas, jei galite, apsvarstykite galimybę mus paremti per įnašus, rėmimą ar pagalbą dokumentuojant kodą, svetainę ir pan.

Padėkos

Mes norėtume padėkoti vystytojams, dokumentacijos rašytojams, testuotojams ir visiems kitiems, kurie savanoriškai skyrė laiką ir pastangas (arba skyrė lėšų, kad tai būtų padaryta). QGIS bendruomenė tikisi, kad jums patiks ši laida! Jei norite skirti laiko, pinigų ar kitaip prisidėti prie to, kad QGIS būtų dar puikesnis, prašome užsukti į qgis.org ir padėti!

QGIS palaiko rėmėjai. Dabartinių rėmėjų, daugiau ar mažiau prisidėjusių finansiškai prie projekto, sąrašą rasite :ref:`rėmėjų sąraše. Jei norėtumėte tapti oficialiu projekto rėmėju, prašome apsilankyti :ref:`mūsų rėmėjų puslapyje, kur rasite daugiau informacijos. QGIS parama leidžia mums finansuoti šešis mėnesinius vystytojų susitikimus, palaikyti projekto infrastruktūrą ir finansuoti klaidų taisymo pastangas. Pilną rėmėjų sąrašą rasite žemiau - mūsų pačios didžiausios padėkos visiems mūsų rėmėjams!

{{<fund type="active" >}}

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Žemėlapio įrankiai
### Savybė: Pavadinimo etiketės dekoracija
Pridėta nauja dekoracija, leidžianti naudotojams greitai pridėti antraštę į drobę. Dekoracijoje yra fono juosta su keičiama spalva ir permatomumu.

![image2](images/entries/400e617d8059eddcd1228f3ce6861d6087f65794.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: dekoracijos elementų centravimas viršuje/apačioje
Žemėlapio drobės autorių teisių ir naujai sukurta antraštės dekoracija dabar gali būti centruojama žemėlapio rodinio viršuje arba apačioje.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: viršūnės įrankio pataisymai ir patobulinimai
Pastaba: visi žemiau išvardinti punktai buvo įdiegti ir į LTR, taigi jie pasirodys ir 3.4.5.
### Select (\"lock\") feature before editing
In QGIS 2.18 you always had to select a feature first before editing it. In QGIS 3 there was no such thing - editing would be done on any feature any time. Now we are making the selection of feature (\"lock\") available again - using **right click**.

Ankstesnėse QGIS 3 versijose dešinys paspaudimas ant geoobjekto iššaukdavo nedidelį iššokantį meniu, kuris siūlydavo rodyti viršūnių redaktorių. **Dabar dešinys paspaudimas ant geoobjekto iš karto parodys viršūnių redaktorių ir išjungs bet kurių kitų geoobjektų redagavimą.**

When a feature is \"locked\", it can be again unlocked by clicking on it or by clicking on an empty area - this will bring us back to the default mode when multiple features can be edited.

**Kai pelės pozicijoje yra keli geoobjektai, pakartotinis dešinio mygtuko paspaudimas apeis juos ratu** - su kiekvienu dešiniu paspaudimu bus užrakintas kitas geoobjektas. Galiausiai, kai visi geoobjektai bus pasiūlyti, nebus užrakintas joks geoobjektas, o tada ciklas prasidės iš naujo.

The locking is possible when clicking a feature\'s vertex, edge or interior (for polygons).
### Naujos viršūnės pridėjimas jos neperkeliant
Dabar galima naudoti **Shift + dvigubą paspaudimą, kad pridėtumėte naują viršūnę nepastūmę jos į naują vietą**. Kartais tai naudinga, kai naudotojai nori pridėti papildomas viršūnes ant esamų segmentų.
### \"Current layer\" mode is now the default
From the two modes of vertex tool, \"all layers\" used to be the default one. But from the user feedback that seemed like less common case and users prefer to have \"current layer\" as the default.

This feature was funded by [German QGIS user group](http://qgis.de/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Savybė: trumpinti/išplėsti
Priešingai nei kitoje programinėje įrangoje, įrankis leidžia jums keisti (multi)linijas IR (multi)poligonus. Dar daugiau, keisti galima ne tik linijų pabaigas, o bet kurią geometrijos vietą. Kitavertus dėl to gali atsirasti netinkamos geometrijos, o tai yra naudotojo atsakomybė.

Įrankis prašo jūsų parinkti ribą (segmentą), nuo kurios kitas segmentas bus praplečiamas ar trumpinamas. Priešingai nei viršūnės įrankyje, vykdomas tikrinimas, kad būtų keičiamas tik redaguojamas sluoksnis.

Kai abu segmentai yra 3D, įrankis vykdo ribojimo segmento interpoliaciją, kad grąžintų Z.

Trumpinimo atveju jums reikia paspaudimu parinkti dalį, kuri bus sutrumpinta.

This feature was funded by [Mairie de Megève](https://www.megeve.fr/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Savybė: stačiakampis pagal 3 taškus (projektuotas)
Jau yra metodas stačiakampio kūrimui pagal 3 taškus, kur stačiakampis ima atstumą tarp pirmo ir antro taško, o antras ilgis yra lygus atstumui tarp 3io ir 2o taško.

Šis naujas metodas leidžia kurti stačiakampį pagal 3 taškus, kur antras ilgis yra atstumas tarp taško, ir taško projektuoto statmenai segmente (arba jo praplėtime).

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Savybė: identifikavimo įrankis tinklelio sluoksniams
Identifikavimo įrankis dabar veikia ir tinklelio sluoksnyje. Jis rodo reikšmę tinklelio skaliaro ir vektoriaus komponentų reikšmes dabartiniu metu.

![image3](images/entries/62a172172d717af1b5399af4006db1ee0e82c7f5.png.400x300_q85_crop.webp)

Šią savybę finansavo Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Išraiškos
### Savybė: naujos išraiškų funkcijos
- `force_rhr`: forces polygons to follow the right hand rule, in which the area that is bounded by a polygon is to the right of the boundary. In particular, the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.
- `decode_uri`: takes a layer parameter and an optional uri part parameter. It will return details about the data source of the layer. The available details depend on the data provider. If called with only a layer parameter, a map will be returned with all the available information. If the part is also specified, only the value for the requested part will be extracted from the map.
- `path` has been added as an option for the `layer_property` expression function
- `array_sort`: sorts an array of elements
- `nullif`
- sqlite_fetch_and_increment
- `make_rectangle_3points`: Make a rectangle from 3 points. There is two options for make the rectangle by the distance or a projection. Option distance: Second distance is equal to the distance between 2nd and 3rd point. Option projected: Second distance is equal to the distance of the perpendicular projection of the 3rd point on the segment or its extension.
- `make_square`: Creates a square from a diagonal.
- from_json
- to_json

### Savybė: laužtiniai skliaustai lengvam priėjimui prie masyvo elementų
Leidžiamos tokios išraiškos:
- array(1,2,3)\[0\] -\> 1
- array(1,2,3)\[2\] -\> 3
- array(1,2,3)\[-1\] -\> 3 (Python style, negative indices count from end of array)
- array(1,2,3)\[-3\] -\> 1
- map(\'a\',1,\'b\',2)\[\'a\'\] -\> 1
- map(\'a\',1,\'b\',2)\[\'b\'\] -\> 2

Šią savybę sukūrė Nyall Dawson, Mathieu Pellerin
### Savybė: nauji masyvų išraiškų kintamieji
- \@map_crs_description: name of the coordinate reference system of the map.
- \@map_crs_acronym: acronym of the coordinate reference system of the map.
- \@map_ellipsoid_acr: acronym of the ellipsoid of the coordinate reference system of the map.
- \@map_crs_proj4: Proj4 definition of the coordinate reference system.
- \@map_crs_wkt: WKT definition of the coordinate reference system.

Šią savybę sukūrė Alexis Roy-Lizotte
### Savybė: nauja try() funkcija klaidų gaudymui
Nauja try() funkcija bando išraišką ir grąžina jos reikšmę jei neįvyko klaida. Jei išraiška grąžina klaidą, grąžinama alternatyvi reikšmė, jei ji pateikta, jei ne - grąžinamas null.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## Naudotojo sąsaja
### Feature: A new grayscale theme: \"Blend of Gray\"
A brand new UI theme has made its way into QGIS named \"Blend of Gray\". In addition, hundreds of fixes, tweaks, and refinements were applied to the preexisting \"Night Mapping\" theme.

![image4](images/entries/32e743ea5bf84c96b86ea31160b1677b6362eacf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: kelių eilučių pažymėjimas ir redagavimas kodo/išraiškų redaktoriuose
Laikant ctrl kol žymima QGIS išraiškų ir Python skriptų redaktoriuose leidžia pažymėti kelių eilučių teksto bloką, kuris gali būti keičiamas vienu metu.

This feature was developed by [Nyall Dawson ()](https://north-road.com)
## Simbologija
### Savybė: geresnis .XML stiliaus bibliotekų valdymas
Naršyklės skydelis dabar rodo QGIS stiliaus xml bibliotekas ir šiuos failus galima tempti ir numesti į QGIS langą. Taip atveriamas dialogas, leidžiantis naudotojams tyrinėti stiliaus biblioteką, importuoti stilius iš bibliotekos į QGIS.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: pasirinktinai priversti naudoti dešinės rankos taisyklę poligono simbolių braižymui
This new option, available under the \"Advanced\" button for fill symbols, allows forcing rendered polygons to follow the standard \"right hand rule\" for ring orientation (where exterior ring is clockwise, and interior rings are all counter-clockwise).

Orientacija pataisoma tik braižant, pradinė geoobjekto geometrija nekeičiama.

Tai leidžia kurti pildymo simbolius su pastovia išvaizda, nepriklausomai nuo to, kokią geoobjektų orientaciją turi braižomas duomenų rinkinys.

Šią savybę finansavo QGIS Vokietijos naudotojų grupė

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: parinktis paprastoms ir žymeklių linijoms braižyti tik išorinį arba tik vidinį žiedą.
This new option is shown whenever a simple line symbol or marker line symbol is used as part of a fill symbol for rendering polygons. The default behavior is to render both interior and exterior rings, but this new setting allows users to set the symbol layer to render only for the exterior ring OR only for interior rings. This allows for symbolisation which wasn\'t directly possible before, such as a marker line with markers for interior rings angled toward the interior of the polygon.

Šią savybę finansavo QGIS Vokietijos naudotojų grupė

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: rastro vaizdo žymeklis
QGIS pridėtas naujas rastro vaizdo žymeklio simbologijos tipas, leidžiantis naudotojams naudoti rastrą, t.y. piešinio failą kaip žymeklį. Rastro vaizdo žymeklio simbologija leidžia keisti plotį, aukštį, dydį, pasukimą ir permatomumą. 

Naudojant nuo duomenų priklausomą vaizdo šaltinį, ši nauja simbologija leidžia puikiai rodyti geopririštas nuotraukas žemėlapio drobėje.

![image5](images/entries/511ac83d3b841be6ae81db5f5d0f319e07e9656e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: rastro pildymas gali naudoti vaizdus iš nutolusio URL arba įterptus vaizdus
Kaip ir SVG, rastro vaizdo žymekliai, rastro pildymas dabar gali naudoti HTTP URL arba failus įdėti tiesiai į simbolį.

Šią savybę sukūrė Mathieu Pellerin
### Savybė: naudoti reprezentacijos reikšmes klasifikuotiems braižymams
When a field is configured with a value relation, value map or other \"representable value\" and the field is used as the source for a classification renderer, the represented values will be taken to label the categories.

Šią savybę sukūrė Matthias Kuhn
### Savybė: galimybė sulieti kategorijas kategorizuotame braižyme
Šis pakeitimas leidžia naudotojams pažymėti kelias esamas kategorijas ir sugrupuoti jas į vieną kategoriją, kuri taikoma bet kuriai iš pažymėjimo reikšmių.

Taip paprasčiau kurti sluoksnių stilius turint daug kategorijų, kur galima grupuoti daug atskirų kategorijų į mažesnę, geriau valdomą aibe kategorijų, kurioms taikomos kelios reikšmės.

Ši parinktis prieinama iš kontekstinio meniu, paspaudus dešinį pelės mygtuką kategorijų rodinyje, kai pažymėtos kelios kategorijos.

![image6](images/entries/159eb5270ab436adbbddba1c92799d8621a0b8e5.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: rodyti projekto spalvas su spalvomis susijusiuose priklausymo nuo duomenų mygtukuose
This adds a new \"Project Colors\" section in data defined buttons which are linked to a color value. The color menu contains all colors defined as part of the current project\'s Project Color Scheme (which is defined through project properties).

Kai projekto spalva parenkama per mygtuką, savybė susiejama su spalva. Ji automatiškai seks visus spalvos pakeitimus projekto nustatymuose.

This allows users to define common colors for a project once, and then \"bind\" symbol, label, layout, etc colors to these preset colors. The link is live, so you change it once, and the change is reflected EVERYWHERE. Sure beats updating a color 100 times when it\'s use has been scattered throughout a project\'s symbols, labels, etc\...

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: stiliaus tvarkyklės dialogo patobulinimai
Stiliaus tvarkyklės dialoge atlikti tokie patobulinimai:
- A new \"list view\" mode has been added
- An \"all\" tab has been added, which shows all matching symbols (regardless of the symbol type)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: SLD eksportas rastro stiliams
QGIS is now able to export raster styling to sld, for example to be used in Geoserver. See: <https://docs.geoserver.org/latest/en/user/styling/qgis/index.html#exporting-raster-symbology>

![image7](images/entries/7ab383dfaa0a0dbc9651168a56f44e2275b8c2df.png.400x300_q85_crop.webp)

Šią savybę finansavo OSGeo UK, GeoServer PSC, Brad Hards

This feature was developed by [Luigi Pirelli and GeoSolutions](https://www.geo-solutions.it/)
## Skaitmeninimas
### Savybė: geo-koordinavimo patobulinimai
- prie GCP taškų pridėti dX, dY ir likučiai
- pridėta parinktis automatiškai įrašyti GCP taškus į rastro-modifikuotą kelią

![image8](images/entries/2d6278e2e65be30ceb12ff30f26d34dae6196e42.png.400x300_q85_crop.webp)

This feature was developed by [Faneva Andriamiadantsoa](https://github.com/Fanevanjanahary)
### Savybė: nauja parinktis vengti geo-koordinavimo minimizavimo pridedant taškus
Naudotojai dabar gali pasirinkti vengti automatinio geo-koordinavimo lango minimizavimo, kuris įvyksta pridedant naujus kontrolinius taškus į žemėlapio drobę. Ši elgsena gali nepatikti turint kelis vaizduoklius, kur norima turėti abu langus matomus pridedant taškus.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Duomenų valdymas
### Savybė: DB tvarkytojo komentarų parinktis
This feature was developed by [Corentin Falcone (SIRS)](https://www.sirs-fr.com/sirs/fr/)
## Formos ir valdikliai
### Savybė: naujas formų valdiklis dvejetainiams (blob) laukams
Šis valdiklis tinka tik dvejetainiams laukams (ir yra numatytasis dvejetainių laukų valdiklis). Jis leidžia rodyti etiketėmis rodyti, ar blob tušias, ar ne, ir jei netuščias - rodyti turinio dydį (baitais/kb/ir pan.).

Iškrentančio meniu mygtukas leidžia naudotojams įrašyti dabartinį dvejetainį lauko turinį į failą diske, išvalyti blob lauko turinį arba įterpti dvejetainį turinį parenkant failą iš sistemos.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Žemėlapio maketas
### Savybė: tinklelio rėmo patobulinimai
Users can now set a margin for the grid frames in layout map items. Additionally, new \"Zebra (Nautical)\" and \"Line border (Nautical)\" frame styles have been added, which show nautical-style blocks in the grid corners when a margin is set for the grid.

Šią savybę sukūrė konst
### Savybė: patobulintas teksto ir etikečių eksportas
Eksportuojant spausdinimo išdėstymą į PDF ar SVG formatus, naudotojai dabar turi galimybę pasirinkti, kaip eksportuojamas išdėstymo tekstas ir etiketės. Galimi variantai yra konvertuoti visą tekstą į kontūrus/kreives (ankstesnė numatytoji parinktis) arba palikti tekstus ir etiketes kaip tekstinius objektus.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: žemėlapio etikečių patobulinimai
Padaryti keli etikečių braižymo tarp žemėlapio išdėstymo elementų patobulinimai.
- A new setting allows per-map control of how close labels are permitted to be placed to the map item\'s edges. Sizes can be set using mm/inches/pixels/etc, and data defined label margins are allowed.
- Naujas nustatymas leidžia žemėlapio kontekste valdyti, ar dalinės etiketės matomos žemėlapyje. Numatytoji parinktis yra nerodyti (priešingai nei drobės nustatymuose, kur numatytoji naujo projekto reikšmė yra rodyti), nes išdėstymai pagal nutylėjimą visada turėtų kurti aukščiausios kokybės kartografinį rezultatą.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: perdarytos elementų apimties/mastelio klavišų kombinacijos
Mygtukai, pritaikantys išdėstymo žemėlapio elementus taip, kad jie atitiktų dabartinį žemėlapio rodinį (ir atvirkščiai) buvo perkelti aukščiau į naują įrankinę žemėlapio elementų savybių languose.

New actions have also been added to set the map item\'s scale to match the main canvas scale, and to set the main canvas scale to match the selected layout map\'s scale. These mirror the existing settings for setting the extent from the canvas and pushing the extent TO the canvas.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Layout items can \"block\" map labels
This feature allows other layout items (such as scalebars, north arrows, inset maps, etc) to be marked as \"blockers\" for the map labels in a map item. This prevents any map labels from being placed under those items - causing the labeling engine to either try alternative placement for these labels (or discarding them altogether).

This allows for more cartographically pleasing maps \-- placing labels under other items can make them hard to read, yet without this new setting it\'s non-trivial to get QGIS to avoid placing the labels in these obscured areas.

The blocking items are set through a map item\'s properties, under the label settings panel. The setting is per-map item, so you can have a scalebar block the labels for one map in your layout and not others (if you so desire!)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: įspėjimai eksportuojant
Eksportuojant spausdinimo išdėstymus, QGIS dabar automatiškai patikrina, ar išdėstyme nėra populiarių klaidų ir įspėja naudotojus, jei jos randamos.
- Masteliai nesusieti su žemėlapio elementu
- Piešinio elementai sugadinti arba trūksta kelių, arba susieti su neperskaitomais piešinių failais
- Žemėlapio peržiūros daugiau nebesusietos su tinkamu žemėlapio elementu

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: žemėlapio peržiūros apimčių pozicijos kontrolė
QGIS allows overview extents to be drawn below map labels (the new default), but in 3.6 choices have been added for drawing them below all map layers, or above/below a specific map layer. This allows users to control exactly where in the map item\'s layer stack the overview will be placed, e.g. allowing them to draw a overview extent below some feature layers such as roads whilst drawing it above other background layers.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: nauji išraiškų kintamieji legendos elementams
Pridėti nauji išraiškų kintamieji, kuriuos galima naudoti nuo duomenų priklausančiose išraiškose išdėstymo legendos elementams:
- \@legend_title
- \@legend_column_count
- \@legend_split_layers
- \@legend_wrap_string
- \@legend_filter_by_map
- \@legend_filter_out_atlas

If the legend is linked to a map, then expressions used in that legend will also have access to the linked variables, including \@map_scale, \@map_extent, etc.

Taipogi simboliai, kurie braižomi kaip legendos dalis, dabar naudoja visą prieinama legendų išraiškų kontekstą. Tai reiškia, kad simboliai turi prieiga prie kintamųjų, tokių kaip dabartinis atlaso geoobjektas.

Šią savybę sukūrė Alexis Roy-Lizotte
### Savybė: išraiškos legendos elemento teksto viduje
This feature allows for expressions to be embedded directly inside legend item text (e.g. group, subgroup and item text). The expressions are evaluated at render time, with full knowledge of the legend\'s expression context (so can utilise variables from the layout/layout item/etc)

There\'s no UI for this yet (that will come in 3.8), but expressions are entered using the standard \[% 1 + 2 %\] format.

Pavyzdžiui legendos elemento tekstas

    My layer (rendered at 1:[% @map_scale %])
    
bus rodomas kaip

    My layer (rendered at 1:1000)
    
This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Analizės įrankiai
### Savybė: rastro skaičiuotuvo aparatinis greitinimas
Rastro skaičiuotuvo veiksmams dabar pagal nutylėjimą prieinamas OpenCL greitinimas.

Šią savybę finansavo Alessandro Pasotti - ItOpen

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Savybė: tinklelio skaičiuotuvas
Panašiai rastro skaičiuotuvui, tinklelio skaičiuotuvas veikia su tinklelio sluoksniais. Be bendrų funkcijų tinklelio skaičiuotuvas taipogi turi laiko agregavimo funkcijas. Pavyzdžiui, jei turite netcdf su kasdieninėmis temperatūromis per mėnesį, jūs galite suskaičiuoti vidutinę temperatūra visam mėnesiui kiekvienoje celėje. Išvestį galima filtruoti pagal laiką ar erdvinę apimtį.

Šią savybę finansavo Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Apdorojimas
### Feature: New algorithm \"Remove duplicates by attribute\"
Leidžia išimti pasikartojančius geoobjektus, identifikuojamus naudojant reikšmes vieno (ar daugiau) laukų reikšmių iš įvesties geoobjektų. Pasirinktinai visi išmesti (pasikartojantys) geoobjektai gali būti įrašyti į atskirą vietą.

![image9](images/entries/ae0544826b7d16479b2e48ba97f1f530c80bbd42.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: HStore išskleidimo algoritmas
This algorithm creates a copy of an input layer and adds a new field for every unique key found in a HStore type field. For instance, a HStore field is often present in an OSM dataset (\"other_tags\").

![image10](images/entries/304c29f7cc6d26aa823001b67a46744deec3c2dd.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Savybė: priverstinė dešinės rankos taisyklė
Šis naujas algoritmas priverčia poligonų geometriją paklusti dešinės rankos taisyklei, kuri nurodo, kad plotą apibrėžiantis poligonas yra ribos dešinėje. Taigi išorinis žiedas orientuojamas pagal laikrodžio rodyklę, o vidiniai žiedai - prieš laikrodžio rodyklę.

![image11](images/entries/16db7b4b5931c9d96eba053701641defc6f52290.png.400x300_q85_crop.webp)

Šią savybę finansavo QGIS Vokietijos naudotojų grupė

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: dvejetainio lauko ištraukimo algoritmas
Šis naujas algoritmas leidžia naudotojams ištraukti dvejetainių laukų turinį į failus.

![image12](images/entries/6715290eac02e216394b3f24045da0b982069c7d.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: linijų dalinimo pagal maksimalų ilgį algoritmas
Šis algoritmas ima įvesties (multi)linijų (arba kreivių) sluoksnį ir padalina kiekvieną geoobjektą į kelias dalis taip, kad nei viena jų nebūtų ilgesnė nei nurodytas maksimalus ilgis.

Palaiko nuo duomenų priklausančia maksimalaus ilgio savybę ir redagavimo vietoje veiksmą.

![image13](images/entries/13c8c2fedfa76ff8decbc4d7e6d683d01bab1126.png.400x300_q85_crop.webp)

Šią savybę sukūrė Nyall Dawson, Nathan Woodrow
### Savybė: naujas parametro tipas autentikacijos konfigūracijai
Buvo pridėtas naujas parametro tipas apdorojimo algoritmams, QgsProcessingParameterAuthConfig, kuris leidžia pasirinkti iš galimų autentikacijos konfigūracijų (ir kurti naujas).

It allows creation of processing algorithm which can fully take advantage of QGIS\' mature authentication handling, avoiding the need to use insecure string parameters for users to input sensitive logon credentials.

QgsProcessingParameterAuthConfig parametrai įvertinami naudojant QgsProcessingAlgorithm.parameterAsString(), kuris grąžina pažymėtos konfigūracijos ID.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: perrinkimo ir formatavimo parinktys gdaladdo algoritme
Šią savybę sukūrė Alex Bruy
### Savybė: rastro zoninė statistikos algoritmas
This algorithm calculates statistics for a raster layer\'s values, categorized by zones defined in another raster layer.

![image14](images/entries/014272dcac2a228f8d8cc7a1587ac9b07865bc1f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: Z ir M reikšmių ištraukimo algoritmai
Šie algoritmai leidžia naudotojams konvertuoti geoobjektuose esančias z ar m reikšmes į sluoksnio atributus.

Pagal nutylėjimą ištraukiamos z/m reikšmės iš pirmos geoobjekto viršūnės, bet pasirinktinai statistika gali būti skaičiuojama pagal VISAS geometrijos z/m reikšmes (pvz. skaičiuojant vidutines/min/maks/sumines/kitas z reikšmes).

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: geodezinio linijos dalinimo ties antimeridianu algoritmas
Šis algoritmas dalina liniją į kelis geodezinius segmentus, kai linija kerta antimeridianą (±180 laipsnių ilgumos). Dalinimas ties antimeridianu padeda vaizduoti linijas kai kuriose projekcijose. Grąžinama geometrija visada bus kelių dalių geometrija.

Kai įvesties geometrijos segmentai kerta antimeridianą, jie bus padalinti į du segmentus, kurių platuma kirtimo tašku bus nustatoma naudojant geodezines linijas, jungiančias taškus abiejose šio segmento pusėse. Dabartinis projekto elipsoido nustatymas bus naudojamas skaičiuojant šį kirtimo tašką.

Jei įvesties geometrijoje yra M ar Z reikšmės, jos bus tiesiškai interpoliuotos naujai sukurtoms viršūnėms antimeridiane.

Taipogi palaiko keitimą vietoje.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Geodesic mode for \"Join by Lines (Hub lines)\" algorithm
Tai leidžia pasirinktinai kurti geodezines linijas, kurios reprezentuoja trumpiausią atstumą tarp taškų pagal elipsoidą.

Kai naudojamas geodezinis režimas, galima dalinti sukurtas linijas ties antimeridianu (±180 laipsnių ilgumos), o tai gali pagerinti linijų braižymą. Taipogi gali būti nurodomas atstumas tarp viršūnių. Mažesnis atstumas reiškia tankesnę, tikslesnę liniją.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: rastro paviršiaus apimties algoritmas
SAGA rastro paviršiaus apimties skaičiavimas buvo perkeltas į QGIS algoritmus. Šio algoritmo SAGA versija buvo ribota QGIS'e, nes paskaičiuota apimtis buvo matoma tik SAGA terminalo išvestyje. Dėl to nebuvo galima jos įrašyti į failą arba panaudoti modelyje kaip įvestį kitame žingsnyje. Taipogi algoritmas buvo perkeltas į vidinį QGIS c++ algoritmą. Algoritmas atkartoja SAGA algoritmą 1:1, bet išveda apimtį (ir plotą) arba į HTML ataskaitą, arba į vektorinę lentelę. Papildomai išvestys gali būti eksportuojamos į skaitmeninius formatus iš algoritmo, leidžiant juos pakartotinai panaudoti modeliuose.

![image15](images/entries/e0a8089ec0653cf5628636354ec80ef317e68565.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: atgaivintas modelio į Pythono scenarijų funkcionalumas
2.x galimybė tiesiogiai konvertuoti apdorojimo modelį į atitinkamą Python skriptą buvo atgaivinta ir atnaujinta 3.x apdorojimo API.

![image16](images/entries/42b342e04b54d5e106ba1051b210d83af8712dd8.png.400x300_q85_crop.webp)

This feature was funded by [Solspec](http://solspec.io)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Programos ir projekto parinktys
### Savybė: trinti nustatymus iš parinkčių kortelės „Sudėtingesni“
This change adds a new right click menu to the settings shown in the \"Advanced\" tab in the settings dialog, which allows users to remove that setting (or group of settings).

![image17](images/entries/6b012542ef9ca282ba6f9087758f85d818dd5ec9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Naršyklė
### Feature: Add \"export to file\" options for raster and vector layers within the browser
Leidžia tiesiogiai eksportuoti šiuos failus (pvz. į kitą formatą, crs ir pan.) be poreikio juos iš pradžių įkelti į projektą.

![image18](images/entries/d939594c84d7aa186fe5f18f46ed7ad0c89d8c67.png.400x300_q85_crop.webp)

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: savos failo/aplanko savybės
You can now right click on a file or folder within the browser, and select \"File Properties\" or \"Directory Properties\" to open the native file/folder properties dialog for that entry. This allows rapid access to operating system file or folder properties, such as file permissions and sharing options.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: sluoksnių ir atributų peržiūra
QGIS 3.6 brings back the functionality from the old 2.18 standalone \"browser\" application to preview layers and their attributes. This functionality has been moved to the inbuilt browser panel, and is available by right-clicking on a layer and selecting \"properties\" (or by clicking the \"enable properties widget\" button in the browser toolbar).

![image19](images/entries/5058aa9a701e417271b0cbf0869669177a7f0fe4.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: tirti naršyklėje QGS/QGZ projekto failus
Senesnės QGIS versijos QGS/QGZ projekto failus rodė naršyklėje, leido juos atidaryti kaip naujus aktyvius projektus. QGIS 3.6 šis funkcionalumas buvo išplėstas, dabar projekto failus galima tirti tiesiai naršyklės VIDUJE. Projektai dabar yra išskleidžiami elementai, kurios išskleidus matoma visa projekto grupių ir sluoksnių struktūra. Bet kurį sluoksnį dabar galima tempti ir numesti į dabartinį projektą.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: tiesiogiai kurkite Geopackage ir Shape failus
Right clicking a directory in the browser panel now shows a \"New\" menu, containing items for creating a new Geopackage, Shapefile, or subdirectory under the selected directory.

![image20](images/entries/2bc8475b95a8413285b3c88a9a070f02f43cf5b9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: atverti terminalą kelyje
Naršyklės skydelio aplankams pridėtas naujas kontekstinis meniu, kuris atidaro naują terminalo langą pažymėtame aplanke.

Windows šis terminalas paveldi QGIS aplinką, taigi GDAL komandos ir Python scenarijai, kurie naudoja PyQGIS komandas, veikia be jokių papildomų nustatymų.

Džiūgaukite, terminalo programišiai!

![image21](images/entries/623ef55ae3918f72faa7ec796bbac01bf5063464.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Bendra
### Feature: Improved \"missing layer\" handling on project load
![image22](images/entries/8e3fbce280478d8e88cab7e24b489b783c83fc13.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it)
### Savybė: pasirinktinis nustatymas versijos tikrinimo išjungimui
A new setting, \"allowVersionCheck\" has been added to the QGIS configuration ini file. If set to true (the default), users may control whether the version check is enabled or disabled through the QGIS settings dialog. When this setting is set to false, no version checking will be performed AND users will NOT have an option to enable this check in the settings dialog.

Šis nustatymas skirtas naudojimui didelėse įmonėse, kur QGIS versijos tvarkomos centralizuotai.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: vektorinio sluoksnio legendos elementams pridėtas perjungimo veiksmas
![image23](images/entries/f3b822b5591367b7d246fbdd5173763a1633b9ec.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
## Duomenų tiekėjai
### Savybė: ArcGIS Feature Server sluoksnių atvira paslaugos info
ArcGIS Feature Server sluoksniai turi naują dešinio mygtuko paspaudimo parinktį naršyklės skydelyje, kuri leidžia tiesiogiai atverti parinkto sluoksnio paslaugos informacijos puslapį.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: OGR tiekėjų dvejetainio blob palaikymas
Vietoje to, kad kapoti dvejetainius laukus į eilutes, šios reikšmės dabar ištraukiamos kaip jų pradinis dvejetainis turinys. Tai leidžia priedams ir scenarijams naudoti dvejetainius laukus, pavyzdžiui ištraukti jų turinį.

Be to, nauji dvejetainiai laukai gali būti kuriami suderinamuose duomenų šaltiniuose.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: ArcGIS Feature Server piešinio žymeklio ir piešinio pildymo palaikymas
Įkeliant Feature Server sluoksnį su piešinio žymekliais ar piešinio pildymo simbologija, QGIS automatiškai konvertuos ESRI piešinio žymeklio ir pildymo simbolius ir naudos juos kaip sluoksnio stilių pagal nutylėjimą.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Šią savybę sukūrė Nyall Dawson, Mathieu Pellerin
### Savybė: ArcGIS Feature Server etikečių palaikymas
Kai Feature Server sluoksnis turi serveryje nurodytas etiketes, šie etikečių nustatymai bus automatiškai naudojami įkeliant sluoksnį į QGIS.

Šią savybę sukūrė Mathieu Pellerin
### Savybė: loginių ir dvejetainių laukų palaikymas atminties sluoksniuose
Memory (\"Temporary scratch\") layers can now use binary and boolean (true/false) field types.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: GeoPackage JSON palaikymas
JSON palaikymas leidžia laikyti struktūrinius duomenis viename GeoPackage failo lauke.

Duomenys, kurie saugomi kaip JSON, gali būti reprezentuojami ir keičiami
- ValueRelation valdikliuose įjungus leidimą žymėti kelis
- KeyValue valdikliuose
- Sąrašo widgets
- or the [QML widget which also supports visualizing JSON data](https://www.opengis.ch/2018/11/13/visualize-postgres-json-data-in-qml-widgets/)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Šią savybę sukūrė David Signer (OPENGIS.ch)
### Savybė: Postgres tiekėjas: įrašyti pirminio rakto pasirinkimą
When a view loaded from Data Source Managers\'s PostgreSQL tab you can select the key columns of the view (by default the first column is used, which can be wrong). This commit stores that selection in the settings, so that it doesn\'t have to be reselected on subsequent loads. This stored selection is also used when adding the loading from the browser.

Šią savybę sukūrė Jürgen Fischer
### Savybė: ArcGIS Feature Server kelių laukų unikalių reikšmių palaikymas
QGIS dabar gali rodyti braižymo nustatymus Feature Serverio sluoksnio, turinčio kelių laukų unikalias reikšmes.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## QGIS Serveris
### Feature: Possibility to set ATLAS_PK in GetPrint request to print atlas sheet(s)
Naujas GetPrint parametras priima pirminį raktą(us), nurodantį, atskyrus kableliais, kuriuos atlaso lapus reikia spausdinti.

Tokia užklausa atrodys daugmaž taip:

    https://yourserver.name/path/to/qgisproject?SERVICE=WMS&REQUEST=GetPrint
    &TEMPLATE=A4&FORMAT=pdf&ATLAS_PK=1,3,7
    
One can also provide an asterisk (\*) for ATLAS_PK to request all features of an atlas. To protect the server against requesting too many features, it is possible to restrict it to a defined maximum of features that can be requested at one time (see attached screenshot).

Kadangi klientai gali nežinoti, kuris šablonas turi atlasą ir kurie atributai yra padengimo sluoksnio pirminiai raktai, ši nauja savybė taipogi prideda šią informaciją į WMS paslaugos GetProjectSetting atsakymą.

![image24](images/entries/6a4648e447531099dfd8d5e113c2a79c8420df06.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Šią savybę sukūrė Marco Hugentobler
### Savybė: WMTS kaladėlių matricų konfigūracija
QGIS Serveryje 3.4 buvo pridėtas WMTS API, kuris skaičiuoja kaladėlių matricas, bet ne EPSG:3857  ir EPSG:4326.

Šis pakeitimas prideda galimybę parinkti kaladėlių matricas, kurios bus naudojamos projekte ir sukonfigūruoti viršutinį dešinį kampą ir paskutinį kaladėlių matricos lygį. EPSG:3857 ir EPSG:4326 naudotojas gali pasirinkti tik paskutinį kaladėlių matricos lygį.

Šią savybę finansavo Ifremer

Šią savybę sukūrė 3liz
### Savybė: Prie WMS GetFeatureInfo užklausos pridėtas JSON formatas
Thanks to this new feature, the FORMAT parameter of GetFeatureInfo for the WMS service may take \'application/json\' or \'application/geo+json\' values. In this case, the document returned by the server looks something like this:

    {"type": "FeatureCollection",
        "features":[
        {
           "type":"Feature",
           "id":"testlayer",
           "geometry":
           {"type": "Point", "coordinates": [913204.9128, 5606011.4565]},
           "properties":{
               "id":3,
               "name":"three",
               "utf8nameè":"three"
           }
        }]
    }
    
This feature was funded by [Veolia](https://www.veolia.com)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Priedai
### Savybė: DB tvarkyklė. Pridėti mygtukai išorinio SQL failo įkėlimui ir įrašymui
Nauji mygtukai leidžia naudotojui įkelti ir įrašyti užklausą išoriniame SQL faile.

![image25](images/entries/7d8fbe3054bd3d8b311d26d9343a20041f3fb809.png.400x300_q85_crop.webp)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Programavimas
### Savybė: nauja klasė QgsExifTools
Contains utilities for retrieving the geotag from images and for setting an image\'s geotag.

Darbas su geo žymomis (iki šios klasės) buvo super-varginantis ir nestabilus bei remdavosi arba komandinės eilutės įrankių naudojimu, arba priklausomybe nuo nestandartinių Python bibliotekų, kurios ne visur buvo prieinamos ir naudotojams dažnai buvo sunku kai kuriose platformose teisingai įdiegti reikiamas priemones.

Su šia klase mes turime stabilius geo žymų ištraukimo/nustatymo metodus, kurie universaliai prieinami ir gali būti saugiai naudojami prieduose ir scenarijuose.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: iteruoti per QgsGeometrijos dalis
This new PyQGIS API allows easy iteration over all the parts of a geometry, regardless of the geometry\'s type. E.g.

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
      print(part.asWkt())
    
    geometry = QgsGeometry.fromWkt( 'LineString( 0 0, 10 10 )' )
    for part in geometry.parts():
      print(part.asWkt())
    
Galimi du iteratoriai. QgsGeometry.parts() teikia ne-const iteratorių, leidžianti vietoje keisti dalis:

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
       part.transform(ct)
    
For a const iteration, calling .const_parts() gives a const iterator, which cannot edit the parts but avoids a potentially expensive QgsGeometry detach and clone

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.const_parts():
       print(part.x())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: patobulintas QgsLineString PyQGIS API
QgsLineString API gavo kelis gražius priedus:
- len(QgsCurve) grąžina taškų skaičių kreivėje
- kviečiant pointN, xAt, yAt, zAt, mAt, setXAt, setYAt, setMAt, setZAt su netinkamu viršūnių indeksu keliama IndexErrors
- Add \[\] getter for retrieving specific vertices, eg. ls\[0\] returns QgsPoint(\...)
- Add \[\] setter for setting specific (existing) vertices, e.g. ls\[1\] = QgsPoint(1,2)
- Add del support for removing vertices, e.g. del ls\[1\] removes the second vertex

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: PyQGIS geometrijų rinkinių API patobulinimai
Patobulinta PyQGIS API darbui su geometrijų rinkiniais:
- removeGeometry kvietimas su netinkamu indeksu dabar kels IndexError
- Calling collection\[0\] will return the first geometry in the collection, collection\[1\] the second, etc. And negative indices return from the end of the collection, so collection\[-1\] returns the last geometry in the collection.
- Geometries can be deleted by calling `del collection[1]` (deletes the second geometry from the collection). Also supports negative indices to count from the end of the collection.

Taipogi dabar galite lengvai iteruoti per rinkinio geometrijas pavyzdžiui tokiu kodu:

    gc = QgsGeometryCollection()
    gc.fromWkt('GeometryCollection( Point(1 2), Point(11 12), LineString(33 34, 44 45))')
    for part in gc:
      print(part.asWkt())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Easier Processing algorithm creation via \@alg decorator
Leidžia taip apibrėžti apdorojimo scenarijus neaprašant savo klasės:

iš qgis.processing import algoritmo

| \@alg(name=\"test2\", label=\"test 2\", group=\"test\", groupid=\"test\") | \@alg.input(type=alg.STRING, name=\"IN1\", label=\"In string\") | \@alg.input(type=str, name=\"IN2\", label=\"In string 1\", optional=True) | \@alg.input(type=str, name=\"IN3\", label=\"In string 2\") | \@alg.input(type=alg.SINK, name=\"SINK\", label=\"Sink it!\") | \@alg.output(type=str, name=\"OUT\", label=\"WAT\") | \@alg.output(type=alg.MAPLAYER, name=\"OUT2\", label=\"WAT\") | \@alg.output(type=alg.VECTOR_LAYER, name=\"VECTOR_LAYER\", label=\"WAT\") | def testalg(instance, parms, context, feedback, inputs): | \"\"\" | This is a test function that does stuff | \"\"\" | feedback.pushInfo(\"We got these inputs!!\") | feedback.pushInfo(inputs\[\'IN1\'\]) | feedback.pushInfo(inputs\[\'IN2\'\]) | feedback.pushInfo(inputs\[\'IN3\'\]) | return { | \"OUT2\": \"wat\" | }

Šią savybę sukūrė Nathan Woodrow
### Savybė: (ne-asinchroninių) tinklo užklausų blokavimas
Pridėta nauja PyQGIS API SAUGIAM užklausų blokavimui. Ji saugi gijose ir turi pilną QGIS šliuzo bei autentikacijos nustatymų palaikymą.

    reply = QgsNetworkAccessManager.blockingGet(...)
    reply = QgsNetworkAccessManager.blockingPut(...)
    
Ši API turi būti naudojama kai reikia blokuoti tinklo užklausą. Priešingai nei įgyvendinimai, kurie remiasi QApplication::processEvents() kuriant QEnvelopLoop, ši klasė visiškai saugiai gali būti naudojama arba pagrindinėje arba foninėje gijose.

Klasė automatiškai apdoroja peradresavimus.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: savi tinkamumo tikrinimai eksportuojant sluoksnius
See <https://north-road.com/2019/01/14/on-custom-layout-checks-in-qgis-3-6-and-how-they-can-do-your-work-for-you/>

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: Geodezinių linijų skaičiavimo API
Prie QgsDistanceArea pridėta nauja PyQGIS API, skirta geodezinių linijų (trumpiausiam atstumui elipsoide) skaičiavimui. Geodeziniams skaičiavimams ji naudoja išvystytą biblioteką geographiclib.
- QgsDistanceArea.geodesicLine : skaičiuoja geodezinį atstumą tarp dviejų taškų
- QgsDistanceArea.latitudeGeodesicCrossesAntimeridian skaičiuoja platumą, kurioje geodezinė du taškus jungianti linija kerta antimeridianą
- QgsDistanceArea.splitGeometryAtAntimeridian : dalina (multi)linestring antimeridiane naudojant geodezines linijas skaičiuojant tikslų tašką, kuriame vyksta dalinimas

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: nauja klasė QgsQuadrilateral
QgsRectangle nesuteikia orientacijos ar Z palaikymo, nes ji skirta apimtims. Buvo sukurta nauja klasė QgsQuadrilateral, skirta 4 viršūnių poligonų valdymui. Šiuo metu yra tik stačiakampiai, bet greitai bus galima pridėti ir kitokias formas.

Šis patobulinimas supaprastina žemėlapio įrankius ir leidžia jums naudoti QgsQuadrilateral klasę kituose įrankiuose.

Jis taipogi leidžia geriau valdyti stačiakampių Z pagal 3 taškus. Šiandien naudojamas pirmas Z, dabar taškai turės savo Z ir 4as bus projektuojamas plokštumoje.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## 3D savybės
### Savybė: paviršiaus šešėliavimas
This adds new options for user to choose how the terrain should be rendered: - shading disabled - color of terrain is determined only from map texture - shading enabled - color of terrain is determined using Phong\'s shading model, taking into account map texture, terrain normal vector, scene light(s) and terrain material\'s ambient+specular colors and shininess

Pasirinktinai paviršių galima šešėliuoti naudojant išankstinę žemėlapio temą.

Šią savybę sukūrė Martin Dobias (Lutra Consulting)
### Savybė: 3D žemėlapio scenų šviesų konfigūravimas
Ši savybė prideda skiltį, skirtą taškinių šviesų šaltinių 3D scenose nustatymui. Palaikoma iki 8 šviesų (ribojama dėl medžiagų įgyvendinimo). Kiekvienam šviesos šaltiniui galima nurodyti poziciją, intensyvumą, spalvą ir slopinimą.

Šią savybę sukūrė Martin Dobias (Lutra Consulting)
### Savybė: taisyklėmis paremtas 3D braižymas
![image26](images/entries/0825fbe986d774f7f2d5a0bdfdbc2487453ef49c.png.400x300_q85_crop.webp)

Šią savybę finansavo QGIS bendruomenė

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Savybė: tinklelio sluoksnio palaikymas (plokštumų) 3D palaikymas
Su šia savybe jūs galite naudoti tinklelio sluoksnius 3D scenoje.

![image27](images/entries/82a388b33e8fb96df43fb32b9bc5ef013be0459c.jpg.400x300_q85_crop.webp)

Šią savybę finansavo Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Svarbūs pataisymai
### Savybė: Alessandro Pasotti riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server: WFS issue using the EXP_FILTER parameter | [#20927](https://issues.qgis.org/issues/20927) | [PR #8924](https://github.com/qgis/QGIS/pull/8924) | Atlikta |
| GetFeatureInfo response empty for child relation table in QGIS Server 3 | [#20801](https://issues.qgis.org/issues/20801) | Nepakartojamas su 3.5 |  |
| QGIS Server WFS DescribeFeatureType not following TYPENAME parameter | [#20198](https://issues.qgis.org/issues/20198) | [PR #8948](https://github.com/qgis/QGIS/pull/8948) | Atlikta |
| QGIS Server 3.4 can\'t reset numeric field using WFS Update | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Atlikta |
| WFS provider shows numeric NULL fields with 0 instead of NULL | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Atlikta |
| OWS project title in project properties cannot be set to blank/empty | nepranešta | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Atlikta |
| Form Value relation based on WFS layer | [#21077](https://issues.qgis.org/issues/21077) | [PR #8970](https://github.com/qgis/QGIS/pull/8970) | Atlikta |
| Button positions in Database styles manager dialog | [#21068](https://issues.qgis.org/issues/21068) | [PR #8971](https://github.com/qgis/QGIS/pull/8971) | Atlikta |
| raster calculator in processing does not work with Aspect raster | [#21011](https://issues.qgis.org/issues/21011) | Nepakartojamas su 3.5 |  |
| Error opening network KML page: Range downloading not supported by this server! | [#21091](https://issues.qgis.org/issues/21091) | [PR #8985](https://github.com/qgis/QGIS/pull/8985) | Atlikta |
| Can\'t add a virtual field or update a existing field of a WFS layer using the field calculator | [#21086](https://issues.qgis.org/issues/21086) | [PR #8990](https://github.com/qgis/QGIS/pull/8990) | Atlikta |
| Opening shapefiles in ZIP gives Invalid Datasource | [#21097](https://issues.qgis.org/issues/21097) | Nepakartojamas su 3.5 |  |
| spatialite, edit table in dbmanager is broken in master Fault: no such table: pg_description | [#21151](https://issues.qgis.org/issues/21151) | [PR #9086](https://github.com/qgis/QGIS/pull/9086) | N/A |
| Delimitedtext layer saves absolute path when project in relative path mode | [#21150](https://issues.qgis.org/issues/21150) | [PR #9099](https://github.com/qgis/QGIS/pull/9099) | Atlikta |
| field calculator doesn\'t load values for gpkg containing blank spaces or n dash (hypen) in field names | [#21100](https://issues.qgis.org/issues/21100) | [PR #9071](https://github.com/qgis/QGIS/pull/9071) | Atlikta |
| Can\'t open feature form when when the primary key of Spatialite layer is created in text type | [#21176](https://issues.qgis.org/issues/21176) | [PR \#](https://issues.qgis.org/projects/qgis/repository/revisions/7f61dc495491752fd26c7f3bad56adc1f8950e3f) | No (deferred) |
| Geopackage layer rename in DB Manager does not update f_table_name values in the layer_styles table or the Triggers | [#21227](https://issues.qgis.org/issues/21227) | [PR #9164](https://github.com/qgis/QGIS/pull/9164) | Not possible because it relies on the new rename feature implemented in browser |
| Layer Properties \> Load Style \> From database \> \'Other styles \...\' \> Description column contains Name text, should contain Description text (it is a geopackage layer) | [#21254](https://issues.qgis.org/issues/21254) | [PR #9170](https://github.com/qgis/QGIS/pull/9170) | Atlikta |
| Komentarai DB tvarkyklės SQL užklausoje sulaužo užklausą | [#21271](https://issues.qgis.org/issues/21271) | [PR #9180](https://github.com/qgis/QGIS/pull/9180) | N/A |
| Riktas su keliais Else elementais nuo taisyklių priklausomame stiliuje | [#21281](https://issues.qgis.org/issues/21281) | [PR #9181](https://github.com/qgis/QGIS/pull/9181) | Atlikta |
| GetFeatureInfo nesiunčia geometrijos kai nurodytas projekte | [#21172](https://issues.qgis.org/issues/21172) | Nepakartojamas su 3.5 | N/A |
| Geometrijos tikrinimo lūžimai | [#21259](https://issues.qgis.org/issues/21259) | [PR #9191](https://github.com/qgis/QGIS/pull/9191) | Atlikta |
| QGIS lūžta, kai createInstance() naudoja netinkamą konstruktorių QgsProcessingAlgorithm subklasėje | [#21270](https://issues.qgis.org/issues/21270) | [PR #9193](https://github.com/qgis/QGIS/pull/9193) | Atlikta |
| geoobjektų įkėlimas labai lėtas | [#21305](https://issues.qgis.org/issues/21305) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| Atributų formos nerodo daugiau apribojimų pranešimų | [#21266](https://issues.qgis.org/issues/21266) | Uždaryta kaip netinkamas po keleto testų ir kelių pokalbių su Giovanni Manghi | N/A |
| OGR tiekėjas grąžina tuščią aibę GPKG uniqueValues(0) | [#21311](https://issues.qgis.org/issues/21311) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| \"default value\" is not applied when pasting features | [#21304](https://issues.qgis.org/issues/21304) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (deferred) |
| Postgis žymiai sulėtėja atidarant atributų lentelę, jei lentelė turi daug stulpelių | [#21303](https://issues.qgis.org/issues/21303) | [PR #9219](https://github.com/qgis/QGIS/pull/9219) | No (deferred) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Savybė: Alexander Bruy riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| gdal buildvrt trūksta svarbaus parametro | [#20586](https://issues.qgis.org/issues/20586) | [PR #8927](https://github.com/qgis/QGIS/pull/8927) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| gdal:warpreproject missing old \'extra\' param | [#20721](https://issues.qgis.org/issues/20721) | [PR #8930](https://github.com/qgis/QGIS/pull/8930) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| Taškai poligonuose | [#20798](https://issues.qgis.org/issues/20798) | Nepakartojamas su 3.5 |  |
| Neveikia IDW interpoliacija csv taškų sluoksnyje | [#20490](https://issues.qgis.org/issues/20490) | [PR #8942](https://github.com/qgis/QGIS/pull/8942) | [PR #8947](https://github.com/qgis/QGIS/pull/8947) |
| \[Processing\] Field calculator algorithm does not use the selected layer as default layer input | [#19686](https://issues.qgis.org/issues/19686) | [PR #8945](https://github.com/qgis/QGIS/pull/8945) | [PR #8949](https://github.com/qgis/QGIS/pull/8949) |
| v.surf.rst NEVEIKIA QGIS 3.2.0 BONN | [#19472](https://issues.qgis.org/issues/19472) | [PR #8959](https://github.com/qgis/QGIS/pull/8959) | [Direct commit](https://github.com/qgis/QGIS/commit/c2465fc4a66425c296ffedb491d220a3db8ba453) |
| SVM Classification, SupportVectorMachineClassification(OpenCV)-Vector Field | [#20796](https://issues.qgis.org/issues/20796) | [PR #8960](https://github.com/qgis/QGIS/pull/8960) | [Direct commit](https://github.com/qgis/QGIS/commit/e0a8de477b04a6aa355d934c25ba37257bc63584) |
| GDAL/OGR Dissolve algoritmas neteisingai dirba su point/multipoint sluoksniais | [#20025](https://issues.qgis.org/issues/20025) | [PR #8972](https://github.com/qgis/QGIS/pull/8972) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Virtualaus vektoriaus kūrimo įrankis: sukurtas failas neįsikelia | [#14374](https://issues.qgis.org/issues/14374) | Nepakartojamas su 3.5 |  |
| \"Convert map to raster\" algorithm does not export with transparent background despite the option | [#19866](https://issues.qgis.org/issues/19866) | [PR #8965](https://github.com/qgis/QGIS/pull/8965) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| \[GUI\] Disable edit tools when no layer is selected/available nor selected layer is in edit mode | [#18141](https://issues.qgis.org/issues/18141) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| \"Add Rectangle From 3 Points\" is enabled on a new project | [#20333](https://issues.qgis.org/issues/20333) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| v.buffer processing algorithm fails when using option \"Name of column to use for buffer distances\". | [#19377](https://issues.qgis.org/issues/19377) | [PR #8973](https://github.com/qgis/QGIS/pull/8973) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Problema su iš tinklo nustatymų išimamais URL | [#20933](https://issues.qgis.org/issues/20933) | [PR #8995](https://github.com/qgis/QGIS/pull/8995) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Rastro duomenų pikselio dydžio nustatymuose nukerpami skaičiai po kablelio | [#21023](https://issues.qgis.org/issues/21023) | [PR #8996](https://github.com/qgis/QGIS/pull/8996) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
|  Įtrauktus sluoksnių stilius ir etikečių savybes galima keisti sluoksnio stiliaus skydelyje | [#16339](https://issues.qgis.org/issues/16339) | [PR #9006](https://github.com/qgis/QGIS/pull/9006) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| processing: \"default output vector layer extension\" not respected by some tools | [#20557](https://issues.qgis.org/issues/20557) | [PR #8997](https://github.com/qgis/QGIS/pull/8997) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Negalima sustabdyti GDAL algoritmo vykdymo | [#20441](https://issues.qgis.org/issues/20441) | [PR #9026](https://github.com/qgis/QGIS/pull/9026) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Pridėta parinktis valdyti eksportuojamus geoobjektus GRASS algoritmuose be kategorijų | nepranešta | [PR #9003](https://github.com/qgis/QGIS/pull/9003) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Apdorojimas: v.net įrankiai (GRASS) grąžina tuščius rezultatus | [#19904](https://issues.qgis.org/issues/19904) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.salesman sekos HTML išvestis | [#21142](https://issues.qgis.org/issues/21142) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.report ir v.net.nreport algoritmai nesuveikia | nepranešta | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| Nepavyksta pridėti WCS - bloga WCS užklausa | [#21045](https://issues.qgis.org/issues/21045) | [PR #9005](https://github.com/qgis/QGIS/pull/9005) | [PR #9098](https://github.com/qgis/QGIS/pull/9098) |
| GeoNode API užklausoms reikia geresnio mažosios versijos nagrinėjimo | [#21093](https://issues.qgis.org/issues/21093) | [PR #9117](https://github.com/qgis/QGIS/pull/9117) | [PR #9141](https://github.com/qgis/QGIS/pull/9141) |
| Varnelės + Nustatymų vėliavėlės Python'e Ubuntu | [#20910](https://issues.qgis.org/issues/20910) | Nepakartojamas su 3.5 |  |
| SAGA openCV ir apdorojimo įrankiai | [#19540](https://issues.qgis.org/issues/19540) | Nepakartojamas su 3.5 |  |
| Klaida kopijuojant įrašus tarp lentelių | [#21154](https://issues.qgis.org/issues/21154) | [PR #9065](https://github.com/qgis/QGIS/pull/9065) | [PR #9185](https://github.com/qgis/QGIS/pull/9185) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Šią savybę sukūrė Alexander Bruy
### Savybė: Jürgen Fischer ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Attribute table will not allow letter \'N\' to be entered | [#21019](https://issues.qgis.org/issues/21019) | [Direct commit](https://github.com/qgis/QGIS/commit/99904f1f5e7b86a92f3ff50132fd89750fe858e7) | [Direct commit](https://github.com/qgis/QGIS/commit/3d4c6c4e3f3f270d46a419787eb20bd02f8e16d3) |
| Oracle Spatial rodinio redagavimas QGIS'e | [#20109](https://issues.qgis.org/issues/20109) | [Direct commit](https://github.com/qgis/QGIS/commit/855b3b4e26377647de5c5f9d38485f9f00bc9257) | [Direct commit](https://github.com/qgis/QGIS/commit/1b6329c3c03a07e46d9b1c53ccd7bc3b42b3b247) |
| Projekto eksportavimo į DXF meniu trūksta CP949 (Korean) koduotės | [#20838](https://issues.qgis.org/issues/20838) | [Direct commit](https://github.com/qgis/QGIS/commit/4e74c8b5480ac28aabc3c0b3eba2609d1a762e8a) | [Direct commit](https://github.com/qgis/QGIS/commit/c7a6b773f2a557b4f2082d0ef114edcd043def74) |
| GeoPackage rastro WEBP palaikymas | [#21083](https://issues.qgis.org/issues/21083) |  |  |
| Grass algorithms doesn\'t work from Processing Toolbox level (grass-7.7.svn folder problem) | [#21114](https://issues.qgis.org/issues/21114) | [Direct commit](https://github.com/qgis/QGIS/commit/febbc4f0b9e6f1e1c74c18bcb117148d6587ff87) | [Direct commit](https://github.com/qgis/QGIS/commit/3221b1c83fc00d4f292b2b767a27e4bfcef0f88b) |
| Pataisyti substr pagalbą | [#21192](https://issues.qgis.org/issues/21192) | [Direct commit](https://github.com/qgis/QGIS/commit/2bed7ab0018696dba76d2c8053d22633a271486e) | [Direct commit](https://github.com/qgis/QGIS/commit/eb8e36c27dad5413936218893393031e7d0a9915) |
| \[OSGeo4W\] introduce with spatialindex 1.9 | fix in spatialindex | [Direct commit](https://github.com/qgis/QGIS/commit/29d44964529defd0aac94c89e747eee095a89f3a) | [Direct commit](https://github.com/qgis/QGIS/commit/af723c4942427fdce5b935560abd242c5c90ef0a) |
| osgeo4w: fix b6293f23c8c | [#21210](https://issues.qgis.org/issues/21210) | [Direct commit](https://github.com/qgis/QGIS/commit/eea4eda6a35f1a06f84f198249b51b169144c46f) |  |
| Expand ZipItem in foreground | [#21268](https://issues.qgis.org/issues/21268) | [Direct commit](https://github.com/qgis/QGIS/commit/407adc761ebe224a2d72df65551cdcf2addf1735) |  |
| dwg import: catch spline misinterpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/3aa2d9ff9bc673a6c11456524bb7bfb6532556a7) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support dxf encoding | [#15999](https://issues.qgis.org/issues/15999) | [Direct commit](https://github.com/qgis/QGIS/commit/e1562a7f1339952be186e924bf96241ce2d826bd) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: force polyline and hatch/ring continuity | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/b8c727f1d293b64d80c6d1cf29107e0477af3d42) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg/dxf import: fix angle and alignment handing of (m)texts | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/92e7faab665d1853191227c8aeb6c13a04c43537) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: fix exception | [#21177](https://issues.qgis.org/issues/21177) | [Direct commit](https://github.com/qgis/QGIS/commit/355deb5905861f263ae7bb03d2bc6fcea4ce5096) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support nested blocks | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/d84c34e0b0ca3586543604a600f939c9024ca99a) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: handle wrong hatch interpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/fd15c3e5b6253c2898dd23dd561121ac1874396c) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dxf export: fix svg scaling | not on redmine | [Direct commit](https://github.com/qgis/QGIS/commit/4b55dbef0b60349c74e40d9fd0109f33bca19510) | [Direct commit](https://github.com/qgis/QGIS/commit/23c01de492546e119d5c1c98f97694f470dbd817) |
| dxf export: fix output of closed 3d polylines | [#20242](https://issues.qgis.org/issues/20242) | [Direct commit](https://github.com/qgis/QGIS/commit/56ec47328b9e24951b51c00144221c95f88c6c83) | [Direct commit](https://github.com/qgis/QGIS/commit/db823175cf5c89bc066621e34a8d922c2f80eb87) |
| dxf export: don\'t label invisible features | [#19604](https://issues.qgis.org/issues/19604) | [Direct commit](https://github.com/qgis/QGIS/commit/c389fad1ad0396cf9914dedc8d2e9a9c303cd8f8) | [Direct commit](https://github.com/qgis/QGIS/commit/87c9e18e5677d0d6e2c43d7ecb36afab84ff31fb) |
| support polyline width and generic line width | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/6bf2d9d4500977c65630add31bb2246f063e20e8) | [Direct commit](https://github.com/qgis/QGIS/commit/c10969e562eda37c0cb78d3ec6db4c1cd68b1106) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Jürgen Fischer](https://www.norbit.de/)
### Savybė: Peter Petrik ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash when adding existing field to vectorlayer | [#18954](https://issues.qgis.org/issues/18954) | [PR #8982](https://github.com/qgis/QGIS/pull/8982) | [PR #9042](https://github.com/qgis/QGIS/pull/9042) |
| Colour bars in colour chooser UI are rendered with interleaved stripes \[MAC\] | [#15984](https://issues.qgis.org/issues/15984) | [PR #9009](https://github.com/qgis/QGIS/pull/9009) | [PR #9020](https://github.com/qgis/QGIS/pull/9020) |
| Impossible to rename a layer style from the Styling Panel | [#17652](https://issues.qgis.org/issues/17652) | [PR #9021](https://github.com/qgis/QGIS/pull/9021) | [PR #9041](https://github.com/qgis/QGIS/pull/9041) |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | upstream: <https://github.com/OSGeo/gdal/issues/1243> |  |
| QGIS 3.4.2 crush at QgsApplication.initQgis() on Mac | [#20712](https://issues.qgis.org/issues/20712) | Nepakartojamas su 3.5 |  |
| QGIS freezes on MacOS 10.14 when launched from Launch Services (works ok when launched from terminal) | [#20381](https://issues.qgis.org/issues/20381) | caused by Qt 5.11 used in official MacOS package. Packages must be recreated with Qt 5.12 |  |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [PR #9035](https://github.com/qgis/QGIS/pull/9035) | [PR #9056](https://github.com/qgis/QGIS/pull/9056) |
| python error when running GRASS 7.6 tools in processing on mac OS | [#21269](https://issues.qgis.org/issues/21269) | problem in official MacOS package, workaround/fix suggested in the comment |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Savybė: Julien Cabieces ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGis 3.4 reproducible crash while in idle state | [#20581](https://issues.qgis.org/issues/20581) | [PR #8988](https://github.com/qgis/QGIS/pull/8988) and [PR #9019](https://github.com/qgis/QGIS/pull/9019) | [PR #9027](https://github.com/qgis/QGIS/pull/9027) and [direct commit](https://github.com/qgis/QGIS/commit/9ea7f1efa44c47d4070a1623b18059014e658017) |
| crash at processing\....qgis:snapgeometries | [#18497](https://issues.qgis.org/issues/18497) | [PR #8966](https://github.com/qgis/QGIS/pull/8966) | [PR #9010](https://github.com/qgis/QGIS/pull/9010) |
| QgsExternalResourceWidgetWrapper crashes | [#20140](https://issues.qgis.org/issues/20140) | Dublis |  |
| Crash on vector edit (that has the 4326 CRS) is reprojected in CRS 3857 | [#19579](https://issues.qgis.org/issues/19579) | [proposed a libspatialindex PR](https://github.com/libspatialindex/libspatialindex/pull/126) |  |
| Adding new features in postgis fails with attribute window popup | [#20523](https://issues.qgis.org/issues/20523) | Man veikia |  |
| Can\'t remove a constraint set on a field once saved | [#20516](https://issues.qgis.org/issues/20516) | [PR #9032](https://github.com/qgis/QGIS/pull/9032) | [PR #9229](https://github.com/qgis/QGIS/pull/9229) |
| QGIS 3.5 not loading or saving multi-dimensional arrays properly from PostGIS layers | [#20872](https://issues.qgis.org/issues/20872) | [PR #9048](https://github.com/qgis/QGIS/pull/9048) | PADARYTI |
| Attribute Table refresh issue when deleting features from shapefile | [#18421](https://issues.qgis.org/issues/18421) | [PR #9152](https://github.com/qgis/QGIS/pull/9152) | [PR #9214](https://github.com/qgis/QGIS/pull/9214) |
| QgsVectorLayer from spatialite featureid problem | [#20633](https://issues.qgis.org/issues/20633) | Works in 3.5 and 3.4 branch (not in 3.4.4) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Savybė: Loïc Bartoletti riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping tooltip doesn\'t works when Advanced Digitizing tool is activate | [#18441](https://issues.qgis.org/issues/18441) | Nepakartojamas su 3.5 |  |
| Remove old settings for vertex markers | [#17366](https://issues.qgis.org/issues/17366) | Works as intended |  |
| Snapping options in meters rounded to integers | [#20829](https://issues.qgis.org/issues/20829) | [PR #9168](https://github.com/qgis/QGIS/pull/9168) |  |
| Add the possibility to return a shp if ogr is not compiled with gpkg | nepranešta | [PR #9037](https://github.com/qgis/QGIS/pull/9037) |  |
| fix qgsRound for negative numbers | [#20861](https://issues.qgis.org/issues/20861) | [PR #9030](https://github.com/qgis/QGIS/pull/9030) and [PR #9025](https://github.com/qgis/QGIS/pull/9025) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)
### Savybė: Victor Olaya ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| algorithm create grid: reference point problem for calculating Y coordinates | [#20966](https://issues.qgis.org/issues/20966) | [Direct commit](https://github.com/qgis/QGIS/commit/e3516ab1b46137db36f3b7dbf4e4f2ee2df1eb70) |  |
| Error in Processing modeller | [#20609](https://issues.qgis.org/issues/20609) | Not an issue anymore. Cannot reproduce. Ticket has been closed by original reporter |  |
| Do not allow file input for tables or vctor layers if there are dependent fields | [#21055](https://issues.qgis.org/issues/21055) | [Direct commit](https://github.com/qgis/QGIS/commit/6eaa511eed775ce36328a3e1465c32dfb82507aa) |  |
| Deactivating/uninstalling plugin causes Python error when trying to edit a Processing model | [#19607](https://issues.qgis.org/issues/19607) | [PR #8957](https://github.com/qgis/QGIS/pull/8957) |  |
| Postgis DB selector for outputs fails to list schemas in selected DB | [#21099](https://issues.qgis.org/issues/21099) | [PR #9004](https://github.com/qgis/QGIS/pull/9004) |  |
| Regression: outputs of processing models are not assigned the specified styles | [#20573](https://issues.qgis.org/issues/20573) | [Direct commit](https://github.com/qgis/QGIS/commit/eb47288fac06692748c7017f6f125a1fc66e9561) |  |
| QGIS3: SagaUtils.py fails when comman contains non-latin characters | [#18617](https://issues.qgis.org/issues/18617) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] Wrong management of locale in output result path | [#19351](https://issues.qgis.org/issues/19351) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] SAGA algorithms cannot produce non-shp output | [#21089](https://issues.qgis.org/issues/21089) | [PR #9002](https://github.com/qgis/QGIS/pull/9002) |  |
| Extent selector shows layers with no spatial component (geometryless tables) | [#21129](https://issues.qgis.org/issues/21129) | [PR #9034](https://github.com/qgis/QGIS/pull/9034) (updated by Nyall in [PR #9038](https://github.com/qgis/QGIS/pull/9038)) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Šią savybę sukūrė Victor Olaya
### Savybė: Even Rouault riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/e261b7ff4fa15e762f7f3a73ff3dbc965181d991) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/0a3d241f96e83b86073efc86b51376c7cd5f6e4f) | - |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/ee6278f8dd1be7064db87be87fe31fa8943730ec) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/4e84cd44868e3b91def41057b7adf28767b4c273) | - |
| attributes in attribute table don\'t match attribute in identify results/labels with WFS layer | [#20865](https://issues.qgis.org/issues/20865) | [PR #9105](https://github.com/qgis/QGIS/pull/9105) | [PR #9113](https://github.com/qgis/QGIS/pull/9113) |
| KML loading bug | [#20173](https://issues.qgis.org/issues/20173) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/467b088edd18f90744bccac9ff6d83a6a5d92d93) and [GDAL 2.4 in](https://github.com/OSGeo/gdal/commit/ec4bd32cd591b672274383f7c06da1d58a2a3500) | - |
| Zoom to Layer does not respond to filtered WFS | [#20742](https://issues.qgis.org/issues/20742) | [PR #9118](https://github.com/qgis/QGIS/pull/9118) | [Direct commit](https://github.com/qgis/QGIS/commit/8834ec78207c091175cb0f48b518b6d2988f337d) |
| Processing time for GeoJSON 10 times slower in 3.4 | [#21085](https://issues.qgis.org/issues/21085) | [GDAL master commmit](https://github.com/OSGeo/gdal/commit/bd668db37eb6f176226ebbe7efe34cfac86a3cf6a) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/d6c38adfa28f75da0630f3e3ac26dbb501fc361e) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Savybė: Martin Dobias ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[vertex tool\] Fix issue with hidden layers being editable | [#18434](https://issues.qgis.org/issues/18434) | [PR #8992](https://github.com/qgis/QGIS/pull/8992) | [Direct commit](https://github.com/qgis/QGIS/commit/2ad47198c446a1f541dca195439bb432da0dce6a) |
| \[vertex tool\] Fix vertex addition to polygon\'s first segment | [#20774](https://issues.qgis.org/issues/20774) | [PR #9024](https://github.com/qgis/QGIS/pull/9024) | [Direct commit](https://github.com/qgis/QGIS/commit/4423caff0994de64185fcc7b3acb5058ca047c14) |
| \[vertex tool\] Misleading message when deleting all nodes of a ring or a part | [#17754](https://issues.qgis.org/issues/17754) | not fixed! needs quite involved fix to make |  |
| \[vertex tool\] Improvements to the right-click behavior to pick locked feature | N/A | [PR #9052](https://github.com/qgis/QGIS/pull/9052) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] right-click to loop through editable features | N/A | [PR #9087](https://github.com/qgis/QGIS/pull/9087) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] misc small UX improvements | N/A | [PR #9116](https://github.com/qgis/QGIS/pull/9116) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] two more UX fixes | N/A | [PR #9130](https://github.com/qgis/QGIS/pull/9130) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] Few more UX improvements | [#21283](https://issues.qgis.org/issues/21283) | [PR #9222](https://github.com/qgis/QGIS/pull/9222) | [PR #9227](https://github.com/qgis/QGIS/pull/9227) |

This feature was funded by [QGIS user group Germany](https://www.qgis.de/)

This feature was developed by [Martin Dobias](https://www.lutraconsulting.co.uk/)
### Savybė: Nyall Dawson ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[postgis\] Fix creation of new Z/M enabled, curved geometry type layers | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/07746dbc0e5b34e31e85e944fc6f53113721a696) | [Direct commit](https://github.com/qgis/QGIS/commit/a61abe5bb3b4c1b633f2f76b69a7f274abeb33d3) |
| \[categorized\] Fix blank layers when using categorized renderer | [#21188](https://issues.qgis.org/issues/21188) | [Direct commit](https://github.com/qgis/QGIS/commit/7714bfbfbe6acec1c193365a173c822cb72c4361) | N/A |
| Fix invalid data source message is always shown after dragging and dropping vector layers to QGIS window | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/a1d8d9ae5d8ff5130e3ccd179617b1e9c0bf4062) | N/A |
| \[processing\] Buffer algorithm should always export multipolygon layers | [#21191](https://issues.qgis.org/issues/21191) | [Direct commit](https://github.com/qgis/QGIS/commit/f22f182bcfd7b7f5b5d8f782f3df08ee9d705115) | [Direct commit](https://github.com/qgis/QGIS/commit/f4866402f7ecf759598e652d5d640dd1fdc48c50) |
| \[processing\]\[gdal\] Fix polygonize field name is ignored | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/06d5b996bfc37f2877ecbf708af608952420ed45) | [Direct commit](https://github.com/qgis/QGIS/commit/ae21d07d4b082ede7b56941aaa1ce57fad8cdb9a) |
| \[processing\] Allow matrix parameters to be correctly set for model child algorithms | [#20914](https://issues.qgis.org/issues/20914) | [Direct commit](https://github.com/qgis/QGIS/commit/eeff02fc14b96a6d3f95ac2122d1d82654dcf268) | [Direct commit](https://github.com/qgis/QGIS/commit/d5900557bdb25f4e285638bf1de85f43430ba15d) |
| \[processing\]\[gdal\] Ensure that GDAL algs output the CORRECT generated filename for outputs | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/c93775f6b177ab2f64bd347c9a6f78896cee78dd) | [Direct commit](https://github.com/qgis/QGIS/commit/93c135f97cad06a1ff703ae1839397f14cb82b3d) |
| \[processing\]\[gdal\] Fix incorrect definition of gdal_warp extra_param parameter | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/f54f5a4fe70792f4d7ea376e28edad88c4d35d4a) | N/A |
| Allow for exact calculation of symbol sizes with mixed layer units | [#21143](https://issues.qgis.org/issues/21143) | [Direct commit](https://github.com/qgis/QGIS/commit/867e39947b3f24d0b7714cd44e28126b61769340) | [Direct commit](https://github.com/qgis/QGIS/commit/33987fa5505ebc4cb9d83c195c49e5938f7c1f73) |
| Fix hang when WMS credentials requested | [#20826](https://issues.qgis.org/issues/20826) | [Direct commit](https://github.com/qgis/QGIS/commit/c9e761649820f8444a41da5e18850061b207c09c) | [Direct commit](https://github.com/qgis/QGIS/commit/ad6e1566a70d4f1a9d959a4de9f18bcae9dbd566) |
| Fix misc deadlocks/crashes in network requests, especially when SSL errors or timeouts occur | Multiple | Multiple | N/A \-- too intrusive |
| \[processing\]\[saga\] Fix definition of Multiple regression points/grids alg | [#21146](https://issues.qgis.org/issues/21146) | [Direct commit](https://github.com/qgis/QGIS/commit/4f8e2317d796881f942bbc6bdcbe60f3470f48fe) | [Direct commit](https://github.com/qgis/QGIS/commit/1916a7fd7ae4a3d5bb767bde76f3042dfd0a7474) |
| \[processing\] do not show geometryless layers in extent selector | [#21129](https://issues.qgis.org/issues/21129) | [Direct commit](https://github.com/qgis/QGIS/commit/5bfec27938ff95cd65c1cf5b88cc13ce26ca1d5d) | [Direct commit](https://github.com/qgis/QGIS/commit/06ee13263d842ea0d7e188107cb9033893b6c75f) |
| \[layouts\] Add checkbox to disable raster tiling for PDF/SVG exports | [#19500](https://issues.qgis.org/issues/19500) | [Direct commit](https://github.com/qgis/QGIS/commit/60b8d05278cd8133e1c06108ba875960d56e90e5) | N/A \-- too intrusive |
| Fix empty strings in proxy exclude list results in proxy being skippe\\d for ALL hosts | [#20213](https://issues.qgis.org/issues/20213) | [Direct commit](https://github.com/qgis/QGIS/commit/cf1cf0fe455a42edf6db4ab9fa07c1ad641b16cb) | [Direct commit](https://github.com/qgis/QGIS/commit/34625110327c5bec4969c2a42cfa8c210bd3b630) |
| Avoid project being marked dirty as soon as its opened | N/A | [Direct commit](https://github.com/qgis/QGIS/commit/394e5d8d76480c1235c49e46d52f5f4a277cf824) | N/A |
| Fix loss of project when saving to QGZ format and path contains non-ascii chars | [#19567](https://issues.qgis.org/issues/19567) | [Direct commit](https://github.com/qgis/QGIS/commit/7d7462c33334a501167813d720fb2589d3c579ec) | [Direct commit](https://github.com/qgis/QGIS/commit/bfef851b1ca98a2c45117a2b1f911f7f1b7155b1) |
| Fix evaluation of data defined properties for subsymbols of subsymbols | [#18384](https://issues.qgis.org/issues/18384) | [Direct commit](https://github.com/qgis/QGIS/commit/9cf2ff31d86e6b7671aaca137a60a7b7a975ef62) | [Direct commit](https://github.com/qgis/QGIS/commit/7e25cea7e939248c8816d2739ccd44a31c606f11) |
| Fix shortest path algorithm can \"shortcut\" when using network in geographic coordinates | [#20997](https://issues.qgis.org/issues/20997) | [Direct commit](https://github.com/qgis/QGIS/commit/e75a88825665e7bb43c6c3cd1b2c22037cd29784) | [Direct commit](https://github.com/qgis/QGIS/commit/a3428e5f92b8b98cc753de0e9366f36e7ecc018e) |
| Fix project loading task never completes when project has embedded layers | [#21012](https://issues.qgis.org/issues/21012) | [Direct commit](https://github.com/qgis/QGIS/commit/7ad4b05112af0c35bd9a8e0526e8823a6b695335) | [Direct commit](https://github.com/qgis/QGIS/commit/6584fb295aed03c3167d056e1bac59a808a1abb5) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Savybė: Hugo Mercier riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis 3.4.1 crashes when accessing methods of feature | [#20752](https://issues.qgis.org/issues/20752) | closed |  |
| Bad size request with a georeferenced raster | [#8272](https://issues.qgis.org/issues/8272) | Can\'t reproduce anymore in 3.5 |  |
| Postgresql: empty SAVEPOINTS | http://issues.qgis.org/issues/17535 | not applicable anymore |  |
| Range widget does not honor default value on not null column | [#20831](https://issues.qgis.org/issues/20831) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) and [PR #9033](https://github.com/qgis/QGIS/pull/9033) |  |
| Range widget gives NULL value in Attributes Form/Table | [#21125](https://issues.qgis.org/issues/21125) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| QGIS 3.4.1 advanced modification and snap block QGIS | [#20568](https://issues.qgis.org/issues/20568) | closed |  |
| Vertex markers not displayed properly for MultiPolygon features | [#19909](https://issues.qgis.org/issues/19909) | [PR #9036](https://github.com/qgis/QGIS/pull/9036) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| Cascading controls in forms | [#11264](https://issues.qgis.org/issues/11264) | triage, closed |  |
| \$length incorrect in expressions | [#19355](https://issues.qgis.org/issues/19355) | [PR #9063](https://github.com/qgis/QGIS/pull/9063) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Hugo Mercier](https://oslandia.com/)

{{<content-end >}}
