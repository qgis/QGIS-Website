---
HasBanner: false
draft: false
releaseDate: '2021-10-22'
section: projektą
sidebar: true
title: QGIS 3.22 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.22 pakeitimai{#changelog322 }
![image1](images/projects/badbeb89221e014ed31e7ea07919c9e734df39b2.png)

Release date: 2021-10-22

QGIS 3.22 Białowieża is aimed at celebrating the 100-year anniversary of [Białowieża National Park](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_National_Park), Poland, which was established in 1921. [Białowieża Forest](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_Forest) is one of the world's last primary woodlands, located on the border between Poland and Belarus. It is one of the few natural old-growth forests in temperate lowland Europe and has been protected for over 600 years. The outstanding value of Białowieża Forest has been acknowledged by its recognition as a [UNESCO Natural World Heritage Site](https://whc.unesco.org/en/list/33).

Białowieża Forest is named after the village Białowieża, which is located right in the middle of this woodland. It is one of the oldest settlements in the area, nowadays hosting numerous research and tourism activities. Today, there are three research institutions in the village: [Białowieża Geobotanical Station, University of Warsaw](https://bsg.bialowieza.pl/en/), [The Mammal Research Institute, Polish Academy of Sciences](https://ibs.bialowieza.pl/en/), and the [Forest Research Institute, Department of Natural Forests](https://www.ibles.pl/en/web/guest/home). Additionally, a large number of scientists from Poland and abroad travel to Białowieża in order to carry out their studies, and as such, there are also other users of QGIS in the area, as well as additional projects which contribute to the Open Data and Open Source Software ecosystems, such as the [Open Forest Data](https://openforestdata.pl/) project.

You can learn more about the project and this release of QGIS at the dedicated project website, <https://qgisbialowieza.pl>.

This feature-packed release includes a vast number of user experience enhancements and controls added to various advanced functionalities. In addition to a host of additional mesh functionality and operational improvements, QGIS Desktop now includes annotation tools and support for annotation layers, amongst much, much more. For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video at <https://youtu.be/U-RHBt6WZi8>

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official project sustaining member, please visit our [sustaining member page]({{< ref "/funding/membership.md" >}}) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Anotacijos
### Savybė: Anotacijų sluoksnio savybės ir efektai
Pridėtos papildomos anotacijų sluoksnio savybės:
- Anotacijų sluoksnio savybių langas, kuriame yra pagrindinė informacija apie sluoksnį ir sluoksnio mastelių diapazonų, permatomumo, suliejimo režimo bei paišymo efektų parinktys.
- An option to view the main annotation layer\'s properties via the annotation toolbar (the main annotation layer is the hidden layer which is always present above all other map layers, so it\'s impossible to open it\'s property window via the layer tree)
- Options to set an annotation layer\'s opacity/blend mode/paint effect in the layer styling dock for interactive changes

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: keisti anotacijos elemento taškus
Anotacijų keitimo įrankis dabar gali keisti anotacijos elemento taškus, paspaudus ant esamo taško ir jį perkeliant. Naudotojo veiksmai seka standartinę QGIS veikseną:
- Kairys paspaudimas perkėlimo pradžiai
- Antras kairys paspaudimas pakeitimų pritaikymui
- Dešinys paspaudimas nutraukimui
- Taško pažymėjimas ir delete paspaudimas ištrins tašką
- Dvigubas paspaudimas ant segmento pridės naują tašką

![image2](images/entries/4510afc65b63bab4ab46e0408a6c4c4207aff40f.gif)

Šią savybę finansavo Swiss QGIS naudotojų grupė.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: perkelti pažymėtą anotaciją rodyklių mygtukais
Kai anotacijos elementas pažymėtas, jį galima perkelti spaudžiant rodyklių mygtukus.

Šis funkcionalumas taipogi leidžia naudoti klavišų kombinacijas taip pat, kaip jos naudojamos su kompozicijos elementais:
- `shift + cursor`: Big movement
- `alt + cursor`: 1px movement

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: įrankiai kurti linijos/poligono anotacijos elementus
Į anotacijų įrankinę pridėti įrankiai, leidžiantys kurti naujus linijų ir poligonų anotacijos elementus.

Jie palaiko tokius pačius veiksmus kaip ir vektorinių geoobjektų braižymas: pritraukimą, sekimą, viršūnių naikinimą spaudžiant backspace mygtuką, kreivių ir ištisinio skaitmeninimo režimus ir pan.

Šią savybę finansavo QGIS Swiss naudotojų grupė

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: naujas taško teksto įrankis
Sukurtas karkasas žemėlapio įrankiams, skirtiems kurti naujus anotacijų elementus, įskaitant ir galimybę kurti naują taško teksto anotacijos elementą.

![image3](images/entries/4822b0a64c8a57a049ae15acb8c77a27709172d5.gif)

Šią savybę finansavo Swiss QGIS naudotojų grupė

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: anotacijų įrankinė
Pridėta nauja anotacijų įrankinė, leidžianti atlikti šiuos veiksmus:
- Kurti naują tuščią šio projekto anotacijų sluoksnį.
- The \"Modify Annotations\" tool, which provides an interface for editing existing annotations.

Leidžiami anotacijos geoobjektų keitimo veiksmai:
- Paspaudus ant esamos anotacijos, ji pažymima sluoksnio stiliaus valdiklyje rodoma jos informacija, įskaitant simbolizaciją, atskaitos mastelį, z-indeksą ir pan.
- Paspaudus kairįjį mygtuką ant anotacijos elemento, jį galima perkelti. Dešinys paspaudimas arba Esc nutraukia perkėlimą, o antras kairys paspaudimas patvirtina perkėlimą.
- Spauskite delete mygtuką pažymėjus anotaciją, jei norite ją ištrinti

Šią savybę finansavo Swiss QGIS naudotojų grupė

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Žemėlapio įrankiai
### Feature: Add a \"measure bearing\" map tool
This tool behaves similarly to the existing \"measure angle\" map tool, but requires the user only to click two points on the map and displays the bearing between these points.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Naudotojo sąsaja
### Savybė: perjungti redagavimą iš karto keliems pažymėtiems sluoksniams
The *toggle editing* action has been modified to support activation on all selected layers, making it easy to start and stop editing sessions across multiple layers simultaneously. Although the editing session status for all selected layers may not be the same, all selected layers will be toggled to an active or inactive state as the inverse of the current state of the currently active layer. This functionality is applied to the menu item *Layer \> Toggle Editing*, the *Toggle Editing* button on the digitizing toolbar, and the *Toggle Editing* entry in the layers context menu.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Savybė: identifikuoti sluoksnių grupes ir visus pažymėtus sluoksnius
Whilst the identify features tool supported multiple selection modes, the \"current layer\" mode has been extended to support the selection of layer groups, and will identify features from all selected layers. Only features from visible layers within a layer group will be identified.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add a \'Show in Files\' action for all file items in browser
Atidaro failų naršyklės langą ir pažymi nurodytą failą

Also fixes the existing \"File Properties\" action so that it shows regardless of the file type, and doesn\'t show incorrectly in some circumstances.

![image4](images/entries/f80090adb3c2f85fa81b5689741afd936f8d5439.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Simbologija
### Savybė: savi vienetai geometrijos generatoriaus simbolių sluoksniams
Geometrijos generatoriai dabar leidžia naudotojams parinkti, kurie vienetai turi būti naudojami grąžinant geometrijas, o ne tiesiog naudoti sluoksnio CRS. Tai ypač naudinga situacijose, kai simboliai nesusiję su sluoksniu, pavyzdžiui kai jie naudojami išdėstymo elementuose.

Pakeitimas suteikia šiuos vienetų pasirinkimus:
- Žemėlapio vienetai (numatytoji parinktis, ankstesnė elgsena)
- Milimetrai
- Taškai (pikseliai)
- Coliai
- Taškai

When millimeters, pixels, inches or points are selected, then the \@map_geometry variable will be available for use within the expression, containing the feature geometry in the specified units (relative to the map frame), whilst the \$geometry variable remains available within the expression in the layer CRS map units.

![image5](images/entries/d1c6b0c69cf9dd8247d1dc0e370d0182b550f48a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: vektorinių sluoksnių simbologijos atskaitos mastelis
Pridėta parinktis, leidžianti konfigūruoti vektorinių sluoksnių geoobjektų simbologijos atskaitos mastelius.

Praktiškai tai apibrėžia žemėlapio mastelį, apibrėžtą su popieriumi susijusiais vienetais, tokiais kaip milimetrai ar taškai, kuris bus naudojamas simbologijai ir etikečių užrašams. Šie vienetų dydžiai bus automatiškai keičiami priklausomai nuo dabartinio žemėlapio rodinio mastelio santykio su nurodytu sluoksnio atskaitos masteliu.

Pavyzdžiui, jei turime linijų sluoksnį, kuris sukonfigūruotas naudoti 2mm pločio liniją naudojant atskaitos mastelį 1:2000. Geoobjektas bus braižomas su 4mm pločio linijomis, kai žemėlapio mastelis bus 1:10000, ir 1mm. kai žemėlapio mastelis bus 1:4000.

Šią savybę finansavo North Road, ačiū SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: spalvų invertavimo filtras rastro braižymui
Dabar galima invertuoti braižomo rastro spalvas, naudojant naują spalvų invertavimo parinktį. Kai kuriais atvejais tai gali būti naudinga. Pavyzdžiui šviesus rastro žemėlapis gali būti greitai paverstas į tamsų žemėlapio pagrindą be poreikio kurti ar rasti naują rastro rinkinį.

![image6](images/entries/0fc6bce9e9240b7e354b84d7477439798fd64a59.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Užrašai
### Savybė: nuo duomenų priklausančio etikečių pasukimo vienetų nustatymas
Nurodykite kampo vienetus, kurie bus naudojami nuo duomenų priklausančiam etikečių pasukimui

![image](images/entries/126294292-06c91bd5-83d2-4d6f-88a2-38fa2d303c86.webp)

![Peek 2021-08-29 14-38](images/entries/131250678-52360214-31a9-4cf9-ad84-b10a4f78c431.gif)

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Tinklelis
### Savybė: naujo tinklelio sluoksnio kūrimas
QGIS dabar leidžia kurti naujus tinklelio sluoksnius.

Tinklelio kūrimas leidžia šiuos kūrimo formatus:
- Naujas tuščias tinklelio sluoksnis
- Naujas tinklelio karkasas, paremtas esamu šio projekto tinkleliu
- Naujas tinklelio karkasas, paremtas esamu tinkleliu iš failo

![image9](images/entries/8ba4033bf4f8eea7e3776db420b34d6c51358859.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio karkaso redagavimas
QGIS dabar leidžia redaguoti tinklelio karkasą, tai leidžia užtikrinti tinklelio tvarkingumą ir leidžia atšaukti ir vėl pakartoti veiksmus.

This introduces the `QgsMeshEditor` class to the QGIS Python API, which allows for performing edit operations, and the QgsTopologicalMesh class which is not exposed to the Python API but is used for ensuring that edited mesh elements remain topologically correct and perform data modifications.

![image10](images/entries/71bed70b1ced3fef5e3b8190cc613f3cb60f0fac.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio karkaso keitimo ciklas
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

Tinklelio karkaso redagavime dabar galima atlikti visus veiksmus, reikalingus redagavimo ciklui, įskaitant pradėti, įrašyti, atšaukti, nutraukti, panašiai, kaip ir vektoriniams sluoksniams.

![image11](images/entries/9463f4559796ff4808fcd05d1ffbec3aa6d6bae4.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio žemėlapio redagavimo įrankis
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools.

Tinklelio redagavimo įrankiai dabar palaiko šiuos veiksmus:
- Pridėti viršūnes/paviršius
- Pažymėti viršūnes/paviršius
- Pašalinti viršūnes/paviršius
- Keisti viršūnių Z reikšmes
- Perkelti viršūnes
- Sąveika su kraštinėmis
- Dalinti paviršius

![image12](images/entries/ce164b754aff6438bb6db52a4d5c2eb3e103af62.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: išmanaus tinklelio redagavimo pagerinimai
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

QGIS naudotojo sąsaja leidžia delaunay trianguliaciją ir plokštumų tvarkymo funkcijas, kurios prieinamos iš kontekstinio meniu, rodomo tinklelio sluoksnyje pažymėjus viršūnes ir/arba paviršius. Tikėtina, kad šios parinktys migruos į tinklelio įrankinę, kai bus pridėta dar daugiau funkcionalumo.

![mapToolrefine](images/entries/125721486-055c4cc3-5309-4455-bc5c-e00d6f349bc4.gif)

QGIS API taip pat praplėstas, pridedant išmaniojo tinklelių redagavimo funkcionalumą į naują abstrakčią klasę QgsMeshAdvancedEditing. Gali būti kuriamos klasės, paveldėtos iš šios, norint vykdyti išmanų tinklelio redagavimą: paviršių kūrimą ar atlikti kitus veiksmus su paviršiais bei viršūnėmis. Išmanus redagavimas vykdomas perduodant QgsMeshAdvancedEditing egzempliorių QgsmeshEditor egzemplioriui ir tada taikant redagavimo veiksmus.

Įgyvendintos dvi išmaniojo redagavimo funkcijos:
- Delaunay trianguliacija
- Paviršių tvarkymas

![image14](images/entries/a914bfb8a85bf2ab2232e8bfad6c3af3cdd751cb.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: pažymėti redaguojamus tinklelio elementus poligonu
Naudotojai gali žymėti suskaitmeninto ploto tinklelio elementus, kai vykdo tinklelio redagavimą. Kiekviena poligono viršūnė skaitmeninama naudojant kairįjį paspaudimą, o dešinys paspaudimas pabaigs ir patikrins poligoną susikertančių tinklelio elementų pažymėjimui (paviršių ir viršūnių). Naudojant backspace mygtuką galima pašalinti paskutinę viršūnę, o Esc mygtukas leidžia naudotojams grįžti į normalaus skaitmeninimo režimą.

Ši funkcija palaiko du veiklos modelius su skirtingais žymėjimo predikatais:
- Liečiantys elementai (numatytoji) arba dalinai įtraukti/susikertantys elementai bus pažymėti (žalia gumelė).
- Vidiniai arba pilnai įtraukti elementai bus pažymėti (mėlyna gumelė).

![image15](images/entries/6a687b260a4d3a41c432360336393ee2746997c8.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: žymėti tinklelio elementus esamomis geometrijomis
Tinklelio elementų žymėjimui pagal esamas vektorinių sluoksnių geometrijas buvo pridėti du veiksmai.

Pažymėjus vektorinio sluoksnio geometrijas, naudotojas gali naudoti šiuos įrankius, kad pažymėtų tinklelio elementus lietimo ar pilno įtraukimo predikatais.

![image16](images/entries/4a918fc1feabd7e3c68282b1b6d052c8504d6013.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio elementų parinkimas naudojant išraišką
An interface has been created for selecting mesh elements by expression during mesh editing. In addition, a contextual expression function `$face_area` has been added that returns the area of a mesh face.

![image17](images/entries/141acf32014c3ce387ff61e39cabf3e04c6d3896.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: transformuoti vieną viršūnę
Naujas tinklelio transformavimo įrankio režimas leidžia naudotojui importuoti vienos pažymėtos viršūnės koordinates.

Tinklelio viršūnių transformavimo lango įrankinės viršuje dešinėje esantis mygtukas perjungia šį režimą. Kiekvieną kartą pažymėjus vieną viršūnę ji automatiškai užpildys laukus, kuriais naudotojas gali atitinkamai keisti viršūnės koordinates.

![image18](images/entries/2148b3024a51a218bafafbbe26f74c30692222f6.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: perindeksuoti/perskaičiuoti tinklelio sluoksnį
Naudotojai dabar gali perindeksuoti (ar pernumeruoti) tinklelio sluoksnio viršūnes ir paviršius redagavimo metu. Pernumeravimas - tai tinklelio optimizavimas Cuthill-McKee algoritmu.

![image19](images/entries/5da7e6705568488c08fbf7faaf311b2eca46c9da.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio pritraukimas prie polilinijų
Redaguojant tinklelio geoobjektus, naudotojai dabar gali transformuoti geoobjektus, priversdami juos sutapti su paviršiumi, apibrėžtu esamomis polilnijomis arba lūžio linijomis. Paviršiai priverčiami sekti lūžio linijas, t.y. paviršių kraštinės privalo būtų ant šių linijų. Naudotojai gali pasirinkti lūžio linijos geometrijas ir tada naudoti tam skirtą mygtuką, kad transformuotų susikertančius tinklelio elementus.

Transformacijai teikiamos parinktys:
- Pridėti naują viršūnę, kai linijos kerta vidinius kampus
- Interpoliuoti naujai pridėtos viršūnės Z reikšmę pagal tinklelį arba iš linijų
- Tolerancija stumiant esamas viršūnes į vietą ir vengiant naujų viršūnių kūrimo palei liniją nustatytu atstumu

![forceByBreakLine](images/entries/132239197-096d733b-b519-4aab-9384-79724fd84331.gif)

Whilst the term \"break lines\" is typically used to refer to polylines that constrain a surface or TIN to the defined positions, these break lines are often components of the mesh itself, and additional operations would continue to constrain the surface to these lines. This functionality specifically transforms the surface in a static manner, so that future operations are not constrained to the lines used to transform the mesh elements.

![image21](images/entries/704c731583ce48d963fe9878177bc40639ae3078.webp)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: tinklelio transformacija naudojant išraišką
User can perform geometrical transformations on a mesh using an expression to change the vertices\' coordinates. All coordinates (X,Y,Z) of selected vertices can be calculated with an expression, allowing transformation of the mesh while the mesh is still valid.

With a valid expression, selecting the \"Preview transform\" option will calculate the new expression based mesh coordinates and identify whether the transform is valid and may be applied.

Jei peržiūra yra žalia, transformuotas tinklelis yra tinkamas ir naudotojas gali pritaikyti transformaciją. Jei peržiūra raudona, tinklelio transformacija netinkama ir naudotojas negali pritaikyti transformacijos.

Pritaikius transformaciją, naudotojas turi galimybę atšaukti ar iš naujo atlikti veiksmą.

![image22](images/entries/04937a2d9bba1e27712351f52e6b6f4d5fc0be4d.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Braižymas
### Savybė: leisti žemėlapio drobei naudoti fizinį DPI
Pridėtas naujas nustatymas, leidžiantis teisingai nurodyti fizinį ekrano DPI vietoje loginio DPI, taip leidžiant tokį patį simbolių braižymą skirtinguose prijungtuose įrenginiuose (aukšto ir žemo dpi), bei mobiliose aplikacijose, tokiose kaip QField.

Šis nustatymas pagal nutylėjimą išjungtas, kad simbolių dydis nebūtų kitoks nei ankstesnėse QGIS versijose.

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
### Savybė: nuo duomenų priklausantis rastro sluoksnio permatomumas
Pridėtas naujas valdiklis, leidžiantis rastro permatomumą valdyti pagal duomenis. Tai leidžia įvairesnį rastro sluoksnio vaizdavimą skirtinguose kontekstuose, pavyzdžiui skirtinguose atlaso lapuose, priklausomai nuo kitų sluoksnių matomumo arba laikinų kintamųjų reikšmių.

Additionally, a \"redraw layer only\" temporal mode for raster layers has been added, which causes a raster layer to be redrawn on each new animation frame as in the equivalent functionality for vector layers. This may be useful in many contexts, such as when the layer uses time-based expression values like the data defined renderer opacity to fade in or out a raster layer from an animation.

![image23](images/entries/881acd52afafba75698f1d7668794b80b594baef.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Spausdinimo maketai
### Savybė: iš anksto numatytų mastelių palaikymas taškais paremtuose atlasuose
Žemėlapio išdėstymų elementai gali naudoti iš anksto numatytus mastelius taškais paremtuose atlasuose. Tai užtikrina teisingą veikseną, kai atlaso geoobjektai yra kelių taškų tipo su kintančiomis aprėptimis.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: legendų grupių ir pogrupių atitraukimas
Two new entries have been added to the \"Spacing\" section of the Legend properties:
- Grupės elementų atitraukimas
- Pogrupio elementų atitraukimas

Elementai, priklausantys grupėms ar pogrupiams bus patraukti dešinėn nurodytu atstumu. Kai legendų formos pridėtos įrašų kairėje, jie taipogi bus patraukti.

![image24](images/entries/3792e9ae5124b81f1b4289cab220fdbb237851a8.webp)

This feature was developed by [Jürnjakob Dugge](https://github.com/jdugge)
## Išraiškos
### Feature: Mesh expression functions for vertex_as_point and vertex_z
Sąveikai su tinklelių sluoksniais pridėtos išraiškos su šiomis funkcijomis, grąžinančiomis reikšmę, susijusią su dabartine viršūne:
- `$vertex_as_point`: returns the current vertex as a geometry point
- `$vertex_z`: returns the Z value of the current vertex.

These two functions are contextual and need to be added in a `QgsExpressionContext` with `QgsExpressionContextUtils::meshExpressionScope()` for the creation of a specific `QgsExpressionScope`.

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Expression function for \$z
The z value for the current feature in an expression context can now be retrieved using `$z`

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Savybė: afininės transformacijos išraiška
An affine_transform function has been added to QGIS Expressions.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Savybė: tiesinio atstumo išraiška
A straight_distance2d function is now available in QGIS expressions for retrieving the direct/ Euclidean distance between the first and last vertex of a curve geometry feature.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Savybė: pridėta vingiuotumo išraišką
Prie QGIS išraiškų pridėta vingiuotumo funkcija.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: New exif() and exif_geotag() functions
Pridėta pora naujų funkcijų, leidžiančių skaityti nuotraukų failų exif žymas. Šios dvi funkcijos yra:
- exif(path, tag) : this function returns the value of a given tag string for the provided image file path; when the second optional parameter isn\'t provided, the function will return a map object containing *all* exif tags and their values.
- exif_geotag(path) : this function returns a point geometry from the exif geotags containing in the provided image file path.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Skaitmeninimas
### Savybė: geometrijos pritraukimo algoritmo optimizacija
Geometrijos pritraukimas dabar veikia akimirksniu, po to kai buvo atlikti papildomi optimizacijos darbai. Trumpo atstumo pritraukimai, užšaldantys QGIS, liko praeityje.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: keisti į kreivę su viršūnių įrankiu
The ability to convert vertices to or from curved vertices is now supported with the Vertex tool, allowing users to convert vertices with the \"C\" and \"O\" keys.

Additionally, methods for `convertVertex()` have been introduced for the `QgsGeometry` and `QgsCompoundCurve` objects in the QGIS API.

![image25](images/entries/fcc006352c7b09e37d6d8511ecb7fe2ae6a8be50.gif)

This feature was funded by [Swiss QGIS user group](https://qgis.ch/)

This feature was developed by [Olivier Dalang](https://github.com/olivierdalang)
### Savybė: išmanusis skaitmeninimas dabar palaiko Z/M
QGIS išmanaus skaitmeninimo įrankiai dabar leidžia įvesti naudotojo Z ir M reikšmes, tai stipriai pagerina naujai skaitmeninamų geoobjektų valdymą, ypač kuriant 3D tinklo komponentus.

![image26](images/entries/287d041be909700393995e3018fba76f41e09a67.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## Duomenų valdymas
### Savybė: išorinės failų laikmenos valdiklio nutempimo palaikymas
Naudotojai dabar gali naudoti tempimą ir numetimą išorinių resursų valdiklyje, kai išorinis valdiklis atitinkamai sukonfigūruotas.

![image27](images/entries/038bb187a174a4c491f3f2db6ef03cec5b75e43d.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Savybė: failais paremtų duomenų rinkinių dydis ir paskutinio pakeitimo data sluoksnio savybių dialoge
The layer properties dialog\'s information panel now shows the size and last modified date of file-based datasets, removing the need to retrieve these details from a file manager. These additional details are also visible in the browser panel\'s information section. For datasets formed of more than a single file, the size will reflect the sum of all the auxiliary/ sidecar files forming the dataset.

![image28](images/entries/10c72ab958bb1e7a59f8f81afb81d33780ed0834.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: failų pervadinimas QGIS naršyklėje
QGIS naršyklėje pridėtas failų pervadinimo veiksmas. Jei failas yra iš kelių failų duomenų rinkinio, tai jie irgi bus atitinkamai pakeisti.

Naudotojai taipogi įspėjami, jei failas yra sluoksnis esamame projekte ir paklausiama, ar jie nori automatiškai atnaujinti ir sluoksnio kelius.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move GPS tools \"add gpx layer\" functionality to Data Source Manager
Functionality from the GPS tools plugin to add GPX layers has been moved to a new \"Add GPS Data\" page in the data source manager.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: projektų įkėlimas iš GPKG naudojant tempimą
Istoriškai, naudojant tempimo ir numetimo funkcionalumą su GPKG formatu, tik geoobjektų sluoksnius buvo galima įkelti į QGIS.

Dabar QGIS rodys projektus, įtrauktus į GPKG, kai GPKG failas pridedamas į QGIS drobę naudojant tempimo ir numetimo funkcionalumą.

![image29](images/entries/3672e8bb8d50bf1593252343da8fd8ff78a46535.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: išorinės saugyklos palaikymas
QGIS now includes an External Storage API, in line with the proposal outlined in [QEP 196](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/196).

Įgyvendintos šios savybės:
- Išorinės saugyklos API
- Registras, kuriame yra visos išorinės saugyklos
- SimpleCopy išorinė saugykla, kurioje laikomi parinkti išoriniai resursai konkrečioje disko vietoje.
- WebDAV palaikymas

Taipogi pridėtas valdiklis, leidžiantis išorinių saugyklų ir jų komponentų konfigūravimą ir vizualizavimą. Saugojimo metodo (failas ar aplankas) valdiklis šiuo metu nematomas, kai parenkama išorinė saugykla, o santykinio kelio nustatymai yra paslėpti, nes santykiniai keliai neaktualūs išoriškai saugomiems duomenims.

![image30](images/entries/c16663cabec529b113bb73919141bf50bf142c9e.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Formos ir valdikliai
### Savybė: formos veiksmų tempimas ir numetimas
Sluoksnių veiksmai dabar galimi formose, naudojant tempimą ir numetimą

![image31](images/entries/d8af279071ac38fdc63fbd3980077155db39bd0f.gif)

This feature was funded by [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Sluoksnių legenda
### Savybė: naudoti savo piktogramą rastro sluoksnių legendai
Pridėta nauja savybė, leidžianti parinkti piešinį, kuris bus naudojamas rastro ir vektorių sluoksnių legendoje. Tai labai naudinga tais atvejais, kai QGIS serveryje naudojami rastro sluoksniui, taip išvengiant ilgų reikšmių palečių GetLegendGraphic užklausose, vietoje to grąžinant specialiai parinktus rezultatus.

![image32](images/entries/f06524b9f422ee1ced55d9d79b816cabc5ea212d.webp)

This feature was funded by [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)

This feature was developed by [mhugent](https://github.com/mhugent)
## Analizės įrankiai
### Savybė: prie rastro skaičiuotuvo pridėta funkcija if()
Seniai laukta QGIS funkcija yra paprastų if() sakinių palaikymas rastro skaičiuotuve.

Nors sąlyginiai sakiniai buvo palaikomi jau kurį laiką, jų sintaksė ir struktūra dažnai buvo sudėtinga.

The raster calculator will now support simple conditional statements with the common syntax of `if ( condition , option1 , option2 )` whereby if the condition evaluates to true, the first option will be used, otherwise the second option will be used.

![image33](images/entries/c5d6968380879133ddb31ab2d0f755d6d2048402.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
### Savybė: rastro skaičiuotuvas palaiko virtualų rastrą
QGIS rastro skaičiuotuvui pridėtas funkcionalumas, palaikantis virtualaus rastro duomenų tiekėjo palaikymą. Tai leidžia naudotojams vykdyti rastro veiksmus nenurodant išvesties failo ir neįrašant rezultato į diską.

This option is enabled via the UI by checking the \"Create on-the-fly raster instead of writing layer to disk\" checkbox in the raster calculator, and is also supported via the PyQgis API.

Gautus rastro sluoksnius galima naudoti tolimesniems analizės veiksmams ir leisti naudotojo nurodytus rastro vardus. Jei gaunamam rastrui pavadinimas nenurodomas, jis bus pavadintas pagal formulę, naudotą jo sukūrimui.

![image34](images/entries/844b2b463a26d035fe25d43d7221a24a570ac615.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
## Apdorojimas
### Savybė: anotacijų sluoksnio parametro tipas apdorojimui
Į QGIS Apdorojimo karkasą pridėtas anotacijų sluoksnių parametro tipas, įskaitant naują algoritmą, skirtą perkelti elementus tarp pagrindinio anotacijų sluoksnio ir antrinių anotacijos sluoksnių. Tai naudinga norint perkelti elementus, sukurtus pagrindiniame sluoksnyje į antrinį sluoksnį, kad galima būtų keisti elementų poziciją sluoksnių krūvoje.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: prie Failų atsisiuntimo apdorojimo algoritmo pridėta POST parinktis
Leisti pasirinkti tarp GET ir POST užklausų, kai failai atsiunčiami naudojant Failų atsiuntimo apdorojimo įrankį.

Parinkus POST parametrą, į užklausą galima pridėti papildomų DATA.

Tai naudinga daugelyje situacijų, pavyzdžiui siunčiant ilgesnes užklausas į Overpass API naudojant POST, norint atsisiųsti OSM duomenis.

![image35](images/entries/89bee20177cb03e453300ae291ae879649e963ab.webp)

This feature was funded by [3Liz](https://www.3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Feature: Add new \"Select within distance\" and \"Extract within distance\" algorithms
Pateikti nauji algoritmai, kurie leidžia naudotojams pažymėti ar ištraukti iš vieno sluoksnio geoobjektus, esančius atitinkamu atstumu nuo geoobjektų kitame sluoksnyje.

The distance checking is heavily optimized, using spatial indices to restrict the number of features retrieved, and also automatically handling off the check to the database server for layers using the PostGIS provider.

Atstumo parametras gali priklausyti ir nuo duomenų.

Šią savybę finansavo QTIBIA Engineering

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: taškų debesies parametras apdorojimui
Prie QGIS Apdorojimo karkaso pridėtas naujas taškų debesies parametras. Tai leidžia filtruoti taškų debesų sluoksnius žemėlapio sluoksnių parametruose. Taip atveriamos durys taškų debesų algoritmams ir pagerina taškų debesų palaikymą trečių šalių tiekėjams.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Savybė: išimtas GPS importavimo priedas
Paskutinis GPS įrankių funkcionalumas buvo perkeltas į tris naujus apdorojimo algoritmus, t.y.:
- Keisti GPS duomenis
- %kelti GPS duomenis į įrenginį
- Atsisiųsti GPS duomenis iš įrenginio

Šito pasekoje, GPS importavimo priedas pasidarė nebereikalingas ir todėl buvo galutinai išimtas iš QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: GPX geoobjektų tipo keitimo apdorojimo algoritmas
GPX geoobjekto tipo keitimo įrankis buvo perkeltas iš GPS įrankių į naują apdorojimo algoritmą, kuris naudoja GPSBabel įrankį GPX geoobjektų tipų keitimui (pvz. keičiant visus taškų geoobjektus į maršruto geoobjektą).

Jis sukurtas kaip pilnas pakaitalas funkcionalumui, kurį anksčiau teikdavo GPS įrankių priedas, bet su visais QGIS Apdorojimo karkaso pagerinimais.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: pridėtas didėjantis laukas su modulio parinktimi
Šis algoritmas leidžia naudotojui pridėti stulpelį su sveiku skaičiumi, kuris didėja nuo START iki nurodytos ribos, su grupavimo galimybe, tęsiant reikšmes ties START, einančiu po grupės.

An option called \"modulo counter\" is included which will reset the counter to the starting value if the modulo value is reached. Using a value of 0 for the modulo option will disable it.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Savybė: trukmės parametras
Į apdorojimo karkasą buvo pridėtas visiškai naujas trukmės parametras. Jis leidžia kurti nuo laiko priklausančius algoritmus.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: erdvinis laiko ST-DBSCAN spiečiaus algoritmas
QGIS 3.22 turi naują erdvinį laiko ST-DBSCAN spiečiaus algoritmą, kuris surenka taškinius geoobjektus pagal 2D tankiu paremtą spiečiaus skaičiavimą su triukšmo (ST-DBSCAN) algoritmu.

Daugiau informacijos rasite šiuose straipsniuose:
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu, \"A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise\". In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
- Birant, Derya, and Alp Kut. \"ST-DBSCAN: An algorithm for clustering spatial--temporal data.\" Data & Knowledge Engineering 60.1 (2007): 208-221.
- Peca, I., Fuchs, G., Vrotsou, K., Andrienko, N. V., & Andrienko, G. L. (2012). Scalable Cluster Analysis of Spatial Events. In EuroVA@ EuroVis.

![image36](images/entries/10136b7563df169c40e2c20a96fe75b6ed93e16f.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: ne vidiniai apdorojimo tiekėjai perkelti į nepriklausomus priedus
In line with the discussion in [QEP 226](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/226), the SAGA, GRASS, and OTB providers have been separated into independent plugins.

Taip turėtų būti išvengta problemų įkeliant Apdorojimo priedus tais atvejais, kai bet kuris iš šių tiekėjų yra sugedęs. Taipogi bus paprasčiau keisti juos į trečių šalių priedus ateityje.

SAGA ir GRASS priedai įjungti pagal nutylėjimą, todėl naudotojo sąsaja nesikeičia. OTB tiekėją, jei reikia, galima įjungti per Priedų tvarkyklę. Kaip bebūtų, visų šitų tiekėjų įjungimas ir išjungimas dabar vykdomas per Priedų tvarkyklę, kaip su bet kuriais kitais priedais.

Tai didžiąja dalimi vidinis pakeitimas, vienintelė matoma dalis yra ta, kad Priedų tvarkyklė naudojama SAGA, GRASS ir OTB tiekėjų įjungimui ir išjungimui.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Programos ir projekto parinktys
### Savybė: eksportuoti visas klavišų kombinacijas į XML ar PDF
Istoriškai, kai klavišų kombinacijos būdavo eksportuojamos į XML failą, QGIS eksportuodavo tik naudotojų sukurtas kombinacijas. Tais atvejais, kai nėra savų kombinacijų, būdavo kuriamas tuščias failas.

Dabar pridėta nauja eksporto parinktis, leidžianti eksportuoti visas esamas klavišų kombinacijas į XML failą, arba kurti PDF išvestį su visomis apibrėžtomis QGIS klavišų kombinacijomis.

![image37](images/entries/1822a5ace82d1e8030ed3d563c07f6b9b6fc3901.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Savybė: GPS Įrankių GPSbabel įrenginių konfigūracijos valdiklis perkeltas į globalius nustatymus
GPS babel konfigūracijos nustatymai buvo perkelti iš nustatymų puslapio nebeaktualiame GPS Įrankių priede į naują pagrindinių nustatymų dialogo puslapį.

![image38](images/entries/d61c12a455d85b290431d5ff461de15db0afb446.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: numatytoji kelių struktūra naujuose projektuose
QGIS Desktop istoriškai palaikė galimybę nurodyti projekto savybėse, ar konkretus projektas naudoja absoliučius, ar santykinius kelius. Numatytoji šio nustatymo parinktis visada buvo naudoti santykinius kelius.

Dabar pridėtas naujas nustatymas, leidžiantis nurodyti numatytąją kelių saugojimo parinktį naujiems projektams. Tai daroma tokiu pačiu būdu, kaip ir konfigūracija, ar projekto formatas turi būti qgz ar qgs. Tai saugoma globaliuose nustatymuose ir taikoma konkretaus naudotojo profiliui.

This feature was developed by [mhugent](https://github.com/mhugent)
### Savybė: maksimalaus podėlio dydžio valdymas QGIS nustatymuose
In the `qgis_global_settings.ini` file, it\'s possible to set the max image cache size in bytes.

Podėlis naudojamas sluoksnio piešinių simboogijos podėliavimui. Jei spausdinimo kompozicijoje naudojami aukštos rezoliucijos piešiniai, ši reikšmė turi būti atitinkamai padidinta.

Numatytoji reikšmė yra 100mb.

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [David Marteau](https://github.com/dmarteau)
## Naršyklė
### Savybė: pagerintas naršyklės failų trynimo veiksmas
The delete action used from the QGIS browser has been improved in various ways, including:
- Veiksmas taikomas visiems failų tipams
- Dabar palaikomas kelių failų trynimas pažymėjus kelis failus, prieš tai parodomas patvirtinimo klausimas
- Prieš trinant failus patikrinama, ar dabartiniame projekte nėra naudojamas nei vienas iš trinamų failų. Jei naudojamas, parodomas pranešimas, klausiantis naudotojų, ar nori nutraukti trynimą, išimti sluoksnius, ar ištrinti failą, bet palikti sluoksnius.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: Jungčių API rezultatų valdiklis
As a part of the ongoing efforts to port the table management functionalities from the DB Manager to the QGIS Browser, as detailed in [QEP 205](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/205), a new SQL dialog is available from the browser panel which provides the ability to execute queries and SQL statements for the following elements:
- DB jungtims
- Schemos elementams
- Lentelių elementams

Įgyvendinimas taipogi suteikia šį sudėtingesnį funkcionalumą:
- Kelių gijų įgyvendinimą tiek API žetonų gavimui, tiek rezultatų eilučių traukimui neblokuojant GUI veiksmų
- Pilnai pertraukiama API
- Palaiko progresyvų geoobjektų įkėlimą rezultatų vaizde (fetchMore API)

![image39](images/entries/a4d260146fe4267a34d9db97495df2b244f5d7ff.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Duomenų tiekėjai
### Savybė: MSSQL tiekėjo transakcijos
MSSQL duomenų tiekėjas dabar palaiko transakcijas.

There are no GUI-related changes, as users can enable transactional editing as with other providers. This is done by going to the Project Properties and checking \"Automatically create transaction groups where possible\" in the Data Sources tab.

Pagal nutylėjimą MSSQL transakcijos blokuoja kitų klientų prieigą prie tų pačių duomenų. Pavyzdžiui jei vienas klientas pradeda transakciją ir prideda ar pakeičia geoobjektą lentelėje, kiti klientai negalės perskaityti jokių duomenų iš lentelės, kol ši transakcija nebus pabaigta.

There is database-level configuration option, `READ_COMMITTED_SNAPSHOT`, which is `OFF` by default.

Įjungus šią parinktį elgsena bus panaši į kitų panašių RDBMS sistemų, tokių kaip PostgreSQL, t.y. transakcijos neblokuos ir leis duombazei turėti kelias tų pačių duomenų versijas. Tai duomenų bazės lygio parinktis, kurią konfigūruoja administratorius ir QGIS jos negali uždėti automatiškai, prisijungiant prie duomenų bazės. Bet ją galima įjungti tokia užklausa:
``` sql
ALTER DATABASE my_db SET READ_COMMITTED_SNAPSHOT ON
```
Dauguma atveju, kai reikia transakcijų, šios parinkties įjungimas rekomenduojamas, kad būtų išvengta QGIS ar kitų klientų užšaldymo.

This feature was funded by [ms.GIS](http://www.msgis.com)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Savybė: rodyti sistemines ir vidines lenteles posluoksnių parinkime
Posluoksnių parinkimo dialoge pridėta varnelė, nurodanti ar reikia rodyti sistemines ir vidines lenteles. Pagal nutylėjimą ši parinktis bus išjungta, bet gali būti naudinga ją įjungti, kai naudotojams dėl kažkokių priežasčių reikia įkelti sisteminę lentelę į QGIS peržiūrai ar naudojimui.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: automatiškai skaityti ir keisti metaduomenis iš ESRI Asmeninių Geoduombazių
Anksčiau tai buvo palaikoma Failų Geoduombazėse ir shp.xml metaduomenims, o dabar tai palaikoma ir ESRI asmeninėms geoduombazėms (.mdb failams)

Reikalauja GDAL 3.4+

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: bendras duomenų elementų tiekėjas visiems failais paremtiems duomenų šaltiniams
Šis tiekėjas naudoja QgsProviderRegistry::querySublayers API automatiniam naršyklės duomenų elementų kūrimui visiems failais paremtiems šaltiniams, nepriklausomai nuo to, koks yra tiekėjas, ar tai mdal, gdal, ogr, pdal ar ept.

Tai leidžia jungti šaltinius, kurie gali būti valdomi skirtingų tiekėjų, į vieną elementų rinkinį naršyklėje, kuris gali būti išplėstas visų elementų rodymui. Daugumai failų tipų, tokių kaip GeoPDF ar KML/KMZ, įprasta turėti rastro ir vektorinius sluoksnius arba .nc failams, kurie gali būti prieinami kaip tinklelis arba rastras, priklausomai nuo duomenų tiekėjo.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## QGIS Serveris
### Savybė: Keli Metaduomenų Url
QGIS Serveris istoriškai palaikė vieną metaduomenų URL, o dabar galima bus turėti kelis metaduomenų prieigos taškus, kurie bus nurodomi paslaugos apibrėžime.

![image40](images/entries/8e644bb4823b8da291e1e2b2dd1ca472d3d57246.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Savybė: prie QGIS Serverio CLI įrankių pridėta versija
It\'s quite a common practice to have arguments like `-v` and `--version` for tools accessed via command line interfaces (CLIs), so new `--version` and it\'s alias `-v` have been added to identify QGIS version information for the following tools:
- qgis_process
- qgis_mapserv.fcgi
- qgis_mapserver

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
## Programavimas
### Savybė: vektorinių kaladėlių kūrimą galima naudoti scenarijuose
An additional `writeSingleTile` method in `QgsVectorTileWriter` has been exposed to enable the encoding of a single vector tile to a memory buffer. This may support workflows for PyQgis and QGIS Server which include support for vector tiles.

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Savybė: kurti ir rašyti vektorines kaladėles naudojant CRS, kitokį nei EPSG:3857
QGIS API buvo praplėstas, leidžiant kurti ir rašyti vektorines kaladėles kitomis CRS nei EPSG:3857.

Pastebėtina, kad pagal Mapbox Vektorinių Kaladėlių specifikaciją, Vektorinė kaladėlė reprezentuoja duomenis kvadratinėje projekcijos erdvėje. Vektorinėje kaladėlėje turi būti informacija apie jos apimtį ir projekciją. Failo formatas numato, kad atkoduojanti pusė žino Vektorinės kaladėlės apimtis ir projekciją iki jos atkodavimo.

Šią savybę finansavo Ifremer

This feature was developed by [rldhont](https://github.com/rldhont)
### Savybė: QgsFeatureRequest filtras DistanceWithin
Prie QgsFeatureRequest pridėta parinktis prašyti geoobjektų, esančių nurodytu atstumu nuo atskaitos geometrijos

Tai įmanoma dėl naujo Qgis::SpatialFilterType, kuris pridėtas nurodyti, ar užklausa nenaudoja jokio erdvinio filtro, naudoja BoundingBox filtrą (per setFilterRect), ar naują filtrą DistanceWithin.

Pavyzdžiui žemiau pateikta užklausa ištrauks visus geoobjektus, esančius 50 žemėlapio vienetų nuo pateiktos linijų sekos:
``` python
QgsFeatureRequest().setDistanceWithin(QgsGeometry.fromWkt('LineString(0 0, 10 0, 12 1)'), 50)
```
Filtrų atstumai traktuojami kaip aprėpties stačiakampių filtrai, taigi jie nepriklausomi nuo bet kokių atributų/id filtrų (tokių kaip geoobjektų ir ar išraiškų).

Provider feature iterators can potentially delegate the distance within search to the backend. So, for example, the PostgreSQL data provider could use an `ST_DWithin` query for optimal index use.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: API iškrentančio sąrašo reikšmėms
Pridėtas API, leidžiantis tekstinį parametrą apdorojimo GUI įrankiuose rodyti kaip iškrentantį sąrašą su iš anksto nurodytomis parinktimis.

In some circumstances, it is desirable to restrict the values available when a user is asked to enter a string parameter that should match a list of predetermined \"valid\" values, yet these values will vary installation by installation.

For example, a \"printer name\" parameter, where it may be desired that users may pick a name value from a list of printers installed on the system, but since the printer names will vary between installations, an enum parameter is not a suitable choice.

This is now supported by setting the \"value_hints\" option in the widget wrapper metadata, as demonstrated below.

Nors tai teikia mechanizmą, leidžianti naudotojams pasirinkti tik teisingas tekstines reikšmes paleidžiant apdorojimo algoritmą per GUI, ji neriboja reikšmių, kurias priima PyQGIS kodas, kai algoritmas paleidžiamas kitokiomis priemonėmis, kurios nenaudoja naudotojo sąsajos. Algoritmai turėtų grakščiai apdoroti ir kitokias reikšmes.
``` python
param = QgsProcessingParameterString( 'PRINTER_NAME', 'Printer name')
# show only printers which are available on the current system as options
# for the string input.
param.setMetadata( {'widget_wrapper': { 'value_hints': ['Inkjet printer', 'Laser printer'] } })
```
This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: QgsExifTools klasė palaiko žymų reikšmių ištraukimą
QgsExifTools klasė dabar gali gauti individualias exif žymas iš piešinių naudojant readTag funkciją.

E.g.: `QgsExifTools.readTag('/my/photo/0997.JPG'), 'Exif.Image.DateTime')`

Žinomos egix žymos rodančios laiko reikšmes automatiškai konvertuojamos į Q{Date,Time,DateTime} objektus. Taip dirbti su šiomis žymomis daug paprasčiau ir gerai integruojasi su kitomis QGIS API dalimis.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Svarbūs pataisymai
### Even Rouault klaidų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| WFS / GML nagrinėjimo problema, bet QGIS įkelia GML kaip failą be problemų? | [#45017](https://github.com/qgis/QGIS/issues/45017) | Ne riktas |  |  |
| POST užklausa laiko žymos modifikavimui neatsižvelgia į apibrėžtą formatą | [#44990](https://github.com/qgis/QGIS/issues/44990) | Netaisysim / ne riktas |  |  |
| Warning message \'Cannot create temporary SpatiaLite cache\' when adding many WFS-layers | [#44971](https://github.com/qgis/QGIS/issues/44971) | Dublis |  |  |
| QGIS sukuria netinkamą WFS GetFeature užklausos filtrą | [#43957](https://github.com/qgis/QGIS/issues/43957) | [PR #45043](https://github.com/qgis/QGIS/pull/45043) | [PR #45053](https://github.com/qgis/QGIS/pull/45053) |  |
| WFS Layer is not rendered when requested CRS is not matching project CRS and \"Only request features overlapping the view extent\" option is set | [#44054](https://github.com/qgis/QGIS/issues/44054) | [PR #45044](https://github.com/qgis/QGIS/pull/45044) | [PR #45047](https://github.com/qgis/QGIS/pull/45047) |  |
| Pridėjus WFS sluoksnį su filtru neegzistuojančiam atributui reiškia neveikiantį sluoksnį | [#43950](https://github.com/qgis/QGIS/issues/43950) | [PR #45045](https://github.com/qgis/QGIS/pull/45045) | [PR #45052](https://github.com/qgis/QGIS/pull/45052) |  |
| Naujas Shapefile sluoksnis tyliai perrašo esamus failus | [#44299](https://github.com/qgis/QGIS/issues/44299) | [PR #45207](https://github.com/qgis/QGIS/pull/45207) | [PR #45240](https://github.com/qgis/QGIS/pull/45240) |  |
| QGIS linux lūžta atidarant daug geopackage vienu metu | [#43620](https://github.com/qgis/QGIS/issues/43620) | [PR #45211](https://github.com/qgis/QGIS/pull/45211) | Ne |  |
| QgsPointCloudLayerRenderer lūžimas uždarant kol dar vyksta braižymas | [#44144](https://github.com/qgis/QGIS/issues/44144) | [PR #45227](https://github.com/qgis/QGIS/pull/45227) | [PR #45241](https://github.com/qgis/QGIS/pull/45241) |  |
| Geoapdorojimo įrankiai priverčia libgeos mesti SIGBUS | [#45226](https://github.com/qgis/QGIS/issues/45226) | [geos PR 481](https://github.com/libgeos/geos/pull/481) | N/A |  |
| QGIS lūžta po WMS įkėlimo per skriptą ir mastelio pakeitimo | [#44095](https://github.com/qgis/QGIS/issues/44095) | [PR #45254](https://github.com/qgis/QGIS/pull/45254) | Ne | Labiau naudojimo problema |
| Netikėtai didelis skaičius GeoPackage | [#45178](https://github.com/qgis/QGIS/issues/45178) | Ne riktas |  |  |
| Atributai - Mygtukas atnaujinti viską - Sukuria netinkamus laukus - GeoJSON faile | [#45139](https://github.com/qgis/QGIS/issues/45139) | [GDAL PR 4552](https://github.com/OSGeo/gdal/pull/4552) | N/A |  |
| WFS connection manager: GetCapabilities document\'s URLs not being used consistently | [#45242](https://github.com/qgis/QGIS/issues/45242) | [PR #45267](https://github.com/qgis/QGIS/pull/45267) | [PR #45273](https://github.com/qgis/QGIS/pull/45273) |  |
| QGIS lūžta, jei tinklo jungtis prarandama ir rastro sluoksnis įkeltas | [#45293](https://github.com/qgis/QGIS/issues/45293) | [GDAL PR 4560](https://github.com/OSGeo/gdal/pull/4560) | N/A |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Alessandro Pasotti riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Duomenų šaltinių tvarkyklė - ArcGIS REST Server - dialogas/langas užsidaro pridedant sluoksnį | [#45050](https://github.com/qgis/QGIS/issues/45050) | [PR #45059](https://github.com/qgis/QGIS/pull/45059) | nėra |  |
| \"Display no data value as\" option is not available in raster layer properties | [#44949](https://github.com/qgis/QGIS/issues/44949) | [PR #45063](https://github.com/qgis/QGIS/pull/45063) | Ne kritinis |  |
| Rastro sluoksnis nebraižomas po duomenų šaltinio pakeitimo, kai tai daroma kartu su kai kuriais išdėstymo elementais | [#44929](https://github.com/qgis/QGIS/issues/44929) | [PR #45074](https://github.com/qgis/QGIS/pull/45074) | [PR #45083](https://github.com/qgis/QGIS/pull/45083) |  |
| Atnaujinti pažymėto geoobjekto id prieš skleidžiant featuresDeleted | [#44921](https://github.com/qgis/QGIS/issues/44921) | [PR #45078](https://github.com/qgis/QGIS/pull/45078) | Ne kritinis |  |
| sample() and identify() from QgsRasterDataProvider don\'t always provide the same value | [#44902](https://github.com/qgis/QGIS/issues/44902) | [PR #45086](https://github.com/qgis/QGIS/pull/45086) | [PR #45145](https://github.com/qgis/QGIS/pull/45145) |  |
| Neteisingai veikia objektų su kelių eilučių tekstu kopijavimas į kitą projektą | [#44989](https://github.com/qgis/QGIS/issues/44989) | [PR #45129](https://github.com/qgis/QGIS/pull/45129) | Ne kritinis |  |
| projektuojant etiketės koordinates kelių taškų geometrijoms nulaužia QGIS | [#45148](https://github.com/qgis/QGIS/issues/45148) | [PR #45150](https://github.com/qgis/QGIS/pull/45150) | Ne |  |
| Copy/paste style category \"Form\" is missing some settings | [#45146](https://github.com/qgis/QGIS/issues/45146) | Maybe won\'t fix, checking with m-kuhn and 3nids |  |  |
| Pridėjus naują tašką į atminties kelių taškų sluoksnį užmušamas QGIS | [#45152](https://github.com/qgis/QGIS/issues/45152) | [PR #45157](https://github.com/qgis/QGIS/pull/45157) |  |  |
| Atributai - Mygtukas atnaujinti viską - Sukuria netinkamus laukus - GeoJSON faile | [#45139](https://github.com/qgis/QGIS/issues/45139) | [PR #45174](https://github.com/qgis/QGIS/pull/45174) | Ne |  |
| WMS parent layer added via QGIS Browser doesn\'t use default style | [#45192](https://github.com/qgis/QGIS/issues/45192) | [PR #45209](https://github.com/qgis/QGIS/pull/45209) | Ne |  |
| \"Display nodata as\" color widget is not automatically updated in layer styling panel | [#45132](https://github.com/qgis/QGIS/issues/45132) | [PR #45264](https://github.com/qgis/QGIS/pull/45264) | nėra |  |
| PostGIS error while changing attributes (field value and geometry): prepared statement \"updatefeature\" already exists | [#45100](https://github.com/qgis/QGIS/issues/45100) | [PR #45266](https://github.com/qgis/QGIS/pull/45266) | eilėje |  |
| Attribute Table in Layout Manager Font Style Override Doesn\'t Show Fields | [#45098](https://github.com/qgis/QGIS/issues/45098) | [PR #45269](https://github.com/qgis/QGIS/pull/45269) | eilėje |  |
| QGIS Serverio WFS sluoksnis nebraižomas dėl problemų su koordinačių ašių rikiuote | [#45216](https://github.com/qgis/QGIS/issues/45216) | [PR #45270](https://github.com/qgis/QGIS/pull/45270) | Ne kritinis |  |
| Nebraižoma su identiteto transformacijos rastru sukurtu su rasterio | [#45324](https://github.com/qgis/QGIS/issues/45324) | Patikrinta, tikriausiai ne riktas |  |  |
| DB Tvarkyklės SQL užklausa vykdoma du kartus | [#45318](https://github.com/qgis/QGIS/issues/45318) | [PR #45351](https://github.com/qgis/QGIS/pull/45351) | eilėje |  |
| can\'t use layers where name starts with number in virtual layer | [#45347](https://github.com/qgis/QGIS/issues/45347) | [PR #45354](https://github.com/qgis/QGIS/pull/45354) | eilėje |  |
| Nulinėje kategorijoje geoobjektų skaičių rodyti kaip null | [#45280](https://github.com/qgis/QGIS/issues/45280) | [PR #45361](https://github.com/qgis/QGIS/pull/45361) | eilėje |  |
| Copying table by Drag&Drop in Browser (2) doesn\'t copy the table structure correctly | [#45286](https://github.com/qgis/QGIS/issues/45286) | [PR #45375](https://github.com/qgis/QGIS/pull/45375) | Ne |  |
| Neteisingas histogramos braižymas, kai rastro duomenų tipas yra baitas | [#45379](https://github.com/qgis/QGIS/issues/45379) | [PR #45400](https://github.com/qgis/QGIS/pull/45400) | eilėje |  |
| Nestandartinis šablono naudojimas su QgsServerOgcApiHandler | [#45439](https://github.com/qgis/QGIS/issues/45439) | [PR #45450](https://github.com/qgis/QGIS/pull/45450) | eilėje |  |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | [PR #45521](https://github.com/qgis/QGIS/pull/45521) | eilėje |  |
| projectsInDatabase raktas nesaugomas xml'e PostGIS jungtims | [#45508](https://github.com/qgis/QGIS/issues/45508) | [PR #45523](https://github.com/qgis/QGIS/pull/45523) | eilėje |  |
| Changing values in Form mode of attribute table doesn\'t set active the Save button | [#45527](https://github.com/qgis/QGIS/issues/45527) | [PR #45532](https://github.com/qgis/QGIS/pull/45532) | eilėje |  |
| Su DBManager nepavyksta sukurti spatialite trigerio | [#45420](https://github.com/qgis/QGIS/issues/45420) | [PR #45553](https://github.com/qgis/QGIS/pull/45553) | Ne |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Peter Petrik riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| QGIS 3.20 Mac lūžta išsiuntus kai kuriuos Qt signalus | [#44182](https://github.com/qgis/QGIS/issues/44182) | [QGIS-Mac-Packager Commit bf925f311](https://github.com/qgis/QGIS-Mac-Packager/commit/bf925f3118a5d51080dfed46dddcb7cba3bbbc00) | nėra |  |
| Negalima peržiūrėti LAS failų, įrašytų su WGS84 (EPSG:4326) koordinatėmis | [#44755](https://github.com/qgis/QGIS/issues/44755) | duplicate of [#41765](https://github.com/qgis/QGIS/issues/41765) |  |  |
| macOS: Symbol not found: \_\_cg_jpeg_resync_to_restart when reprojecting raster layer with GDAL warp on macOS | [#40164](https://github.com/qgis/QGIS/issues/40164) | ne | ne | Daugiau ne problema su (qgis-deps-0.9) |
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | [PR #45322](https://github.com/qgis/QGIS/pull/45322) | eilėje |  |
| piktogramos nesimato sluoksnių pastabose | [#44425](https://github.com/qgis/QGIS/issues/44425) | [PR #45332](https://github.com/qgis/QGIS/pull/45332) | nėra |  |
| negalima atverti jokio ascii FLO-2D failo Tinklelio sluoksnyje | nepranešta | [PR #45349](https://github.com/qgis/QGIS/pull/45349) | nėra |  |
| kodavimo problema naudojant GRASS apdorojimo įrankį macOS | [#41870](https://github.com/qgis/QGIS/issues/41870) | [PR #45399](https://github.com/qgis/QGIS/pull/45399) | Nekritiniai - yra apėjimai |  |
| Matplotlib QT importai neveikia MacOS | [#45398](https://github.com/qgis/QGIS/issues/45398) | aiškinamasi |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Sandro Santilli riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Padaryti QgsGeos::prepareGeometry ir QgsGeos::cacheGeos idempotentiniais | nepranešta | [PR #45147](https://github.com/qgis/QGIS/pull/45147) |  |  |
| Pridėti metodą distanceWithin į virtualią klasę QgsGeometryEngine | nepranešta | [PR #45057](https://github.com/qgis/QGIS/pull/45057) |  |  |
| Allow calling testdata_pg.sh from any directory | nepranešta | [PR #45378](https://github.com/qgis/QGIS/pull/45378) |  |  |
| Padaryti TestPyQgsPostgresProvider.testGeneratedColumns idempotentiniu | nepranešta | [PR #45415](https://github.com/qgis/QGIS/pull/45415) |  |  |
| Pagerinti PostgreSQL test DB sukūrimo dokumentaciją ir skriptą | nepranešta | [PR #45413](https://github.com/qgis/QGIS/pull/45413) |  |  |
| Pridėti GEOS DistanceWithin API | [GEOS Ticket #1124](https://trac.osgeo.org/geos/ticket/1124) | [GEOS commit #ba10ba4508a](https://trac.osgeo.org/geos/changeset/ba10ba4508af887a1a78bbc632ab45d89ce3242c/git) | [GEOS Issue #472](https://github.com/libgeos/geos/issues/472) |  |
| Padaryti Postgres tiekėjo testą idempotentiniu | [#45417](https://github.com/qgis/QGIS/issues/45417) | [PR #45418](https://github.com/qgis/QGIS/pull/45418) |  |  |
| Kai galima, naudoti GEOSDistanceWithin | nepranešta | [PR #45340](https://github.com/qgis/QGIS/pull/45340) |  |  |
| Sumažinti GEOS geometrijų keitimus ir paruošimus | nepranešta | [PR #45195](https://github.com/qgis/QGIS/pull/45195) |  |  |
| Daugiau heuristikos nustatant, ar iteruoti per paskirties šaltinį | nepranešta | [PR #45339](https://github.com/qgis/QGIS/pull/45339) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Loïc Bartoletti riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Daugiau const geometrijoje | Nepranešta / greitaveika | [PR #45217](https://github.com/qgis/QGIS/pull/45217) |  |  |
| QgsFeature::setId pagerinti dokumentaciją įspėjimu | [#44898](https://github.com/qgis/QGIS/issues/44898) | [PR #45189](https://github.com/qgis/QGIS/pull/45189) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| Geometrijos tikrinimas: Padidinti GeoobjektoID | [#44250](https://github.com/qgis/QGIS/issues/44250) | [PR #45191](https://github.com/qgis/QGIS/pull/45191) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| VertexTool. Fixes move vertex on Z layer if CRS are differents (with Vincent Cloarec) | Nepranešta | [PR #45020](https://github.com/qgis/QGIS/pull/45020) | Not backported. Introduce new methods. |  |
| Fix Z/M dimension URI via DB Manager. | [#34894](https://github.com/qgis/QGIS/issues/34894) | [PR #45223](https://github.com/qgis/QGIS/pull/45223) | [PR #45304](https://github.com/qgis/QGIS/pull/45304) |  |
| \[FIX\] GeometryValidator init curve support | Nepranešta | [PR #45272](https://github.com/qgis/QGIS/pull/45272) |  |  |
| Compile fails, \'None\' is not a member of \'QgsField::ConfigurationFlags\' | [#44681](https://github.com/qgis/QGIS/issues/44681) | Netaisysim / ne riktas |  |  |
| Union fails when using a point and a polygon layer | [#44801](https://github.com/qgis/QGIS/issues/44801) | Skirtumas tarp GEOS 3.8 ir 3.9 |  |  |
| Rings order in MultiPolygon WKT string may leave overlapping parts when deleting holes (native:deleteholes) | [#44424](https://github.com/qgis/QGIS/issues/44424) | Wontfix for now. We can use Geos to fix the issue, but will remove Z/M and segmentize arc. |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Loïc Bartoletti](https://www.oslandia.com/)
### Denis Rouzaud ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Regression: trying to run the multipart to singleparts algorithm throws a python error | [#45331](https://github.com/qgis/QGIS/issues/45331) | [PR #45348](https://github.com/qgis/QGIS/pull/45348) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Denis Rouzaud](https://www.opengis.ch/)
### Julien Cabieces ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Styles in database not working for postgres provider and non-geometric layers | [#44749](https://github.com/qgis/QGIS/issues/44749) | [PR #45075](https://github.com/qgis/QGIS/pull/45075) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| \"Layer notes\" icon is not displayed when copy-pasting a style | [#44692](https://github.com/qgis/QGIS/issues/44692) | [PR #45302](https://github.com/qgis/QGIS/pull/45302) | nereikia |  |
| Neaiškios JSON klaidos | [#42832](https://github.com/qgis/QGIS/issues/42832) | Nepavyksta pakartoti |  |  |
| Attribute table: missing features when copying/pasting from scratch layer | [#42798](https://github.com/qgis/QGIS/issues/42798) | Can't reproduce (Closed) |  |  |
| Form view shows wrong image attachments when scrolling through features | [#42705](https://github.com/qgis/QGIS/issues/42705) | Already fixed |  |  |
| Build Virtual Raster tool creates an additional layer when selecting and reordering layers | [#44270](https://github.com/qgis/QGIS/issues/44270) | [PR #45092](https://github.com/qgis/QGIS/pull/45092) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| Attachment widget options are reset when you reopen the field widget properties | [#45089](https://github.com/qgis/QGIS/issues/45089) | Dublis |  |  |
| Cleared feature attributes not acting like they have been cleared, and preventing saving of layer | [#39146](https://github.com/qgis/QGIS/issues/39146) | [PR #45176](https://github.com/qgis/QGIS/pull/45176) | [PR #45292](https://github.com/qgis/QGIS/pull/45292) |  |
| \[Postgres\] default value displayed instead of NULL | [#45198](https://github.com/qgis/QGIS/issues/45198) | [PR #45199](https://github.com/qgis/QGIS/pull/45199) | [PR #45291](https://github.com/qgis/QGIS/pull/45291) |  |
| a feature copy/paste sets a NULL field to its \"default value\" in a geopackage | [#44544](https://github.com/qgis/QGIS/issues/44544) | Question: Do we evaluate default value on NULL field when copy-pasting feature ? |  |  |
| QGIS expression builder can not resolve PostgreSQL text arrays correctly | [#45290](https://github.com/qgis/QGIS/issues/45290) | [PR #45321](https://github.com/qgis/QGIS/pull/45321) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Julien Cabieces](https://www.oslandia.com/)
### Nyall Dawson ištaisyti riktai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.16 backport commit (GitHub) | Pastaba |
| --- | --- | --- | --- | --- |
| Don\'t reset mesh layer styling when changing data source for layer | [#45391](https://github.com/qgis/QGIS/issues/45391) | [PR #45392](https://github.com/qgis/QGIS/pull/45392) | N/A |  |
| Fix crash when rendering clipped features and clipped shape results | [#45190](https://github.com/qgis/QGIS/issues/45190) | [Commit 6a4cdb36](https://github.com/qgis/QGIS/commit/6a4cdb36c91085c5bb1544fb02da1f83467a29d7) | [PR #45422](https://github.com/qgis/QGIS/pull/45422) |  |
| Fix crash when using map label tools with projects containing vector tile layers | [#44486](https://github.com/qgis/QGIS/issues/44486) | [PR #45311](https://github.com/qgis/QGIS/pull/45311) | [PR #45390](https://github.com/qgis/QGIS/pull/45390) |  |
| Fix symbol sizes in Meters at Scale cannot be negative | [#45298](https://github.com/qgis/QGIS/issues/45298) | [Commit 360351a](https://github.com/qgis/QGIS/commit/360351a02704c370545fb8f92c0bdafbdfa35b2e) | Not suitable for backport |  |
| Fix overwriting default style of geopackage layers | [#42811](https://github.com/qgis/QGIS/issues/42811) | [Commit eef6939b96](https://github.com/qgis/QGIS/commit/eef6939b96407b3d050988be4a0eeb692ffc5b68) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Fix hang when rendering lines with dash patterns with all 0 values | [#41994](https://github.com/qgis/QGIS/issues/41994) | [Commit f4e2e900](https://github.com/qgis/QGIS/commit/f4e2e900eed16633ef0198f7b9a9152f395e173a) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Update default toolbar locations | nepranešta | [Commit 77be95feac](https://github.com/qgis/QGIS/commit/77be95feac7391e58f6bd487f30e09ed8ed63651) | N/A |  |
| Don\'t overwrite existing data defined property expressions when an interactive map tool is used to move/rotate/edit labels | [PR #45279](https://github.com/qgis/QGIS/pull/45279) | [Commit b30c17f0](https://github.com/qgis/QGIS/commit/b30c17f07d00850597d8bb1b2cfb1f454498b391) | N/A |  |
| Fix crash on exit with CAD dock open | nepranešta | [Commit 1fb21f69f](https://github.com/qgis/QGIS/commit/1fb21f69fede05cabb8f1d27a8ad24564ae16f3d) | N/A |  |
| Fix rule based symbology doesn\'t work for columns with \'-\' in name | [#44379](https://github.com/qgis/QGIS/issues/44379) | [Commit 51fa9840](https://github.com/qgis/QGIS/commit/51fa9840248135a7fe7ee181b7d645f3c591c9cc) | [Commit 797367dde](https://github.com/qgis/QGIS/commit/797367dde65d6ab06f39f5c4636c2127c67aa9d1) |  |
| Avoid hangs when drawing symbol icons using inappropriate sizes in map units | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45233](https://github.com/qgis/QGIS/pull/45233) | Not suitable for backport |  |
| Fix inappropriate display of z/m values in cad dock when non-z/m layer is selected | nepranešta | [Commit 55a76d1d](https://github.com/qgis/QGIS/commit/55a76d1d867c32f52ae4bd38ed671d44aa3ae92e) | N/A |  |
| Implement more responsive cancelation of map render for maps using complex effects | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45212](https://github.com/qgis/QGIS/pull/45212) | Not suitable for backport |  |
| Allow CAD dock to be used for geographic CRS, but only allow the x/y/z/m constraints to be set | nepranešta | [PR #45185](https://github.com/qgis/QGIS/pull/45185) | Not suitable for backport |  |
| Fix crash when opening symbology properties of a layer set to embedded renderer which is not compatible with embedded renderers | [#45159](https://github.com/qgis/QGIS/issues/45159) | [PR #45193](https://github.com/qgis/QGIS/pull/45193) | N/A |  |
| Fix QgsMapToolCapture coordinates when associated with a non-vector layer where the layer CRS != canvas CRS | nepranešta | [PR #45183](https://github.com/qgis/QGIS/pull/45183) | N/A |  |
| Fix geometry generator rendering outside of vector layers | [#39159](https://github.com/qgis/QGIS/issues/39159) | [PR #45165](https://github.com/qgis/QGIS/pull/45165) | Not suitable for backport |  |
| Fix color customisation is lost when configuring renderers using geometry generators | [#38377](https://github.com/qgis/QGIS/issues/38377) | [PR #45166](https://github.com/qgis/QGIS/pull/45166) | Not suitable for backport |  |
| Fix rendering of interpolated line symbol layer outside of vector layers | [#45028](https://github.com/qgis/QGIS/issues/45028) | [PR #45164](https://github.com/qgis/QGIS/pull/45164) | N/A |  |
| Fix QgsGeometry.fromPolygonXY docs | [#45099](https://github.com/qgis/QGIS/issues/45099) | [Commit 3d599fe4](https://github.com/qgis/QGIS/commit/3d599fe4b5574e7c916133171e097163cae51e32) | N/A |  |
| Fix digitizing features using CAD dock when layer CRS != canvas CRS | nepranešta | [PR #45108](https://github.com/qgis/QGIS/pull/45108) | N/A |  |
| Fix offset background when drawing rotated text | [#44907](https://github.com/qgis/QGIS/issues/44907) | [PR #45425](https://github.com/qgis/QGIS/pull/45425) | laukiama |  |
| Correctly escape complex source strings in processing history log | [#45403](https://github.com/qgis/QGIS/issues/45403) | [PR #45426](https://github.com/qgis/QGIS/pull/45426) | laukiama |  |
| Fix handling of ADF files in browser | nepranešta | [PR #45393](https://github.com/qgis/QGIS/pull/45393) | Not suitable for backport |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
