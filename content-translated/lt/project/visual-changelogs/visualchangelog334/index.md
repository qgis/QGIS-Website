---
HasBanner: false
draft: false
releaseDate: '2023-10-29'
section: projektą
sidebar: true
title: QGIS 3.34 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.34 pakeitimai{#changelog334 }
![image0](images/entries/334splash.webp)

Laidos data: 2023-10-29

Pristatome QGIS 3.34, pagrindinė QGIS projekto laida, kuri atneša esminius atviro kodo geoerdvinės duomenų analizės ir vizualizavimo programinės įrangos QGIS pakeitimus.

Šioje laidoje yra įvairūs pagerinimai esamame API, išraiškose, įrankiuose, spausdinimo išdėstymų pakeitimai, braižymo parinkčių pagerinimai tiek 2D, tiek ir 3D kontekste.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=LHFVo0edaXE>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/LHFVo0edaXE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is a community effort, and we would like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.
## Cesium 3D kaladėlės
Thanks to an ecosystem grant from the [Cesium](https://www.cesium.com/) project, QGIS now has support for loading in 3D content in the Cesium 3D Tiles format! Tiles can be loaded from either local or remote datasources (including the Cesium ion platform and the Google Earth photorealistic tiles), and are visible in both 2D and 3D map views. In 2D views users can control the appearance of tile content by styling in either their original textures or in a wireframe view of the tile geometries, and users also have control over the desired level of detail in both 3D and 2D views.

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/lvl8zVZ8glY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

This feature was developed by [Martin Dobias](https://github.com/wonder-sk) and [Nyall Dawson](https://github.com/nyalldawson)
## Žemėlapio įrankiai
### Feature: Optional enforcement of \"dot\" as decimal separator for measure tool
A new `Always use decimal point` checkbox option has been added to the Measure Tool. This option will ensure that measurements and coordinates are copied to the clipboard using a decimal point (dot) separator, even if the current locale uses a comma.

Tai leidžia kopijuoti kableliais atskirtus duomenis (csv) net tais atvejais, kai naudotojo lokalė kaip trupmeninės dalies skirtuką naudoja kablelį.

![image1](images/entries/ec6084247b2b698045a783e2b007b0e0dde90ddd.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Savybė: naudojant identifikavimo įrankį, paryškintai rodyti identifikuotus rastro pikselius
QGIS dabar rastro pikselių geoobjekto identifikavimo rezultato geometriją rodo žemėlapio drobėje. Tai atitinka dabartinę identifikavimo įrankio elgseną su vektoriniais, vektorinių kaladėlių ir taškų debesies geoobjektų tipais.

This is useful when a identifying a raster which has sections of similar colored pixels and it\'s difficult to visually determine the exact extent of a pixel.

![image2](images/entries/dc219caa150c9bbcb15aece90744f63e54ec25a1.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: rodyti identifikavimo rezultatuose paspausto taško rastro eilutę/stulpelį
Naudojant identifikavimo įrankį rastro sluoksniuose, išvestuose rezultatuose dabar bus ir identifikuojamo pikselio eilutė ir stulpelio numeris.

![image3](images/entries/0889d275dfefea4c7c7d13ebc5dc6fd237573076.webp)

This feature was developed by [Hannes & Nyall Dawson](https://github.com/kannes)
## Simbologija
### Savybė: nustatymai, leidžiantys permušti vektorinių sluoksnių pažymėjimo spalvą ir simbolį
Nauji sluoksnio braižymo nustatymai leidžia naudotojams valdyti spalvą ir simbolį, kurie bus naudojami vietoje sistemos ir projekto numatytųjų reikšmių, kai paryškinami pažymėti geoobjektai.

Šis nustatymas nurodomas kiekviename sluoksnyje ir naudingas siekiant pagerinti pažymėtų objektų matomumą naudojant konkrečiai nurodytą simbologiją.

Tai naudinga skirtinguose scenarijuose, įskaitant ir atvejus, kai:
- Sluoksnis naudoja simbolio spalvą ar stilių, kuris atitinka pažymėjimo simbologiją, ko pasekoje geoobjekto pažymėjimas nematomas
- Linijų sluoksnis naudoja ploną simbolį, o pažymėtos linijos spalva nepadaro jų pakankamai matomomis
- Sluoksniai su sudėtinga simbologija (tokia kaip rastro/gradiento pildymais/linijosmis/išdeginimais su spalvos rampa) neturi kur taikyti numatytosios spalvos. Tokiais atvejais naudotojas gali nurodyti paprastesnį simbolį, kurį reikia naudoti sluoksnyje pažymėtiems geoobjektams.

![image4](images/entries/c648e5905c6c69e7a1e7c1dc91e3a15de1c8d523.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Užrašai
### Savybė: perjungti vektorinių kaladėlių sluoksnių užrašus
Naudotojai dabar gali perjungti vektorinių kaladėlių sluoksnių užrašus naudojant vektorinių kaladėlių sluoksnių stiliaus skydelį ir sluoksnių turinio kontekstinį meniu, taip pakartojant vektorinių sluoksnių užrašų perjungimo galimybę.

This functionality is enabled by the addition of new functions to the `QgsVectorTileLayer` API by replicating the existing functionality on `QgsVectorLayer`.

![image5](images/entries/9e04c9c98886edf1d34eeb9750dc8f5c94946b51.gif)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Braižymas
### Feature: \"Sticky\" Map Decorations
Dynamic map decorations are now rendered to a transparent overlay, preventing re-rendering of decoration objects (such as title or scale bar) during navigation. The `QgsMapDecoration` now also includes `hasFixedMapPosition` to fix a decoration to a geographic location.

![image6](images/entries/00e6bc11fa3025317740f955962ef50cc1b95336.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Savybė: pridėtas žemėlapio braižymo profiliuotojas
The debugging/ development profiling tools have been extended with a new \"map render\" profile (accompanying the existing Startup and Project Load profiles).

Per šį įrankį naudotojai gali identifikuoti skaudamas vietas jų žemėlapių braižyme ir atsekti, kurie konkrečiai sluoksniai sukelia ilgus žemėlapio braižymus.

![image7](images/entries/50fd809522d42944942ca7a059807f59fdcec5d2.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add choice of two different modes for \"Refresh Layer at Interval\"
When using \"Refresh Layer at Interval\" on vector layers, previous versions of QGIS would simply redraw the layer (for animations etc.), without refreshing data from the data source.

Pridėtas naujas valdiklis, kuris leidžia naudotojams pasirinkti sluoksnio atnaujinimo parinktis pagal pageidaujamą naudojimo variantą:
- \"Reload Data\": The layer will be completely refreshed. Any cached data will be discarded and re-fetched from the provider. This mode may result in slower map refreshes.
- \"Redraw Layer Only\": This mode is useful for animations or when the layer style should be updated at regular intervals. Canvas updates are deferred in order to avoid refreshing multiple times if more than one layer has an automatic update interval set.

![image8](images/entries/e0b0d4561cf7963d9a16bef9f77ea8214fe15f7b.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## 3D savybės
### Savybė: leisti konfigūruoti GPU atminties apribojimą
Naudotojai dabar gali konfigūruoti GPU atminties apribojimą kiekvienam sluoksniui (anksčiau buvo naudojamas fiksuotas 500MB apribojimas esybei/sluoksniui)

Taipogi rodomas įspėjimas, kai riba yra pasiekiama, tai padeda suprasti problemas su didelėmis scenomis.

Šis funkcionalumas naudingas naudotojams, kurie naudoja dideles 3D scenas, kurios išsekina visus turimus GPU atminties resursus.

![image9](images/entries/161c61a6ec3ca078e4483279c54f25319bed2c20.webp)

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### Savybė: pridėtas boundingbox3d palaikymas
Additional API methods for relevant geometry classes are now available for `boundingBox3D` and `calculateBoundingBox3D`, as well as extensions to `boundingBoxIntersects` methods which will now support checking intersections between 3D bounding boxes.

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## Spausdinimo maketai
### Savybė: pažymėti kelis išdėstymo elementus
Suteiktas naujas funkcionalumas kelių elementų žymėjimui vienu metu spausdinimo išdėstymų elementų sąrašuose.

Tai taipogi pagerina naudotojų patirtį esamame kelių elementų pažymėjimo funkcionalume, kuris galimas su vizualiu parinkimu paliekant elementų pažymėjimą sinchronizuotą su elementų sąrašu.

![image10](images/entries/85d915ba102341669b4ccccab308a987b0927d68.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Savybė: išdėstymo puslapio numeris rodomas puslapio savybėse
When a layout has more than one page, the current page number will be displayed in the item properties header section using the format `page_number`/`pagecount`.

![image11](images/entries/367986f087f878b47fe1296fcd8143ef677b3430.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Savybė: automatiškai atverti eksportuotus išdėstymus
A new \"Open file after exporting\" checkbox option has been added to the export options for PDF, SVG, and Image output types. When selected this option will attempt to automatically open the output file once the export is completed.

The application used to open the file will use the configured default application on the system based on type (using `QDesktopServices::openUrl`). This feature will leverage the user settings API to remember the selection for the active user profile.

![image12](images/entries/502d122401e26d6dca10146dbdb9ccd1b01e8bd3.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Išraiškos
### Savybė: pridėta krypties išraiškos funkcija
A new `bearing` function has been added which computes the bearing angle (in radians) between two points.

Kryptis nustatoma nurodytoje CRS ir matuojama pagal laikrodžio rodyklę nurodytame elipsoide.

![image13](images/entries/a1d3176b8434f43bb248926df46c406f4b5f2625.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add \"layer_crs_ellipsoid\"
QGIS expressions now include a `layer_crs_ellipsoid` layer variable, as well as the `crs_ellipsoid` property available from the `layer_property` function. The value returned will be the ellipsoid acronym of the layer CRS.

![image14](images/entries/25fa0e9a64d6d1ea6b22e0e9b29ced356bbc96c8.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Skaitmeninimas
### Feature: Improve \"avoid overlap\" type awareness
When digitizing features with the \"avoid overlap\" option, QGIS has improved the behavior of automatically coercing the feature type and includes more meaningful messages to notify users of the automated behaviours.

Pavyzdžiui skaitmenizuojant kelių dalių poligoną vienos dalies poligonų paskirties sluoksnyje, kurio negalima įrašyti. QGIS dabar automatiškai išlaikys tik didžiausią geometrijos dalį ir pasiūlys naudotojui pasirinktinai atstatyti papildomus geoobjektus kaip vienos dalies poligonus.

This prevents the digitizing of \"sliver\" polygons and frustrations with improper feature types.

![image15](images/entries/e86392da95484a83eb7edbfd554526865d4195ff.gif)

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
## Duomenų valdymas
### Savybė: pagerintas vektorinių geoobjektų įrašymo jau esamų failų apdorojimas
Kai naudojamas algoritmas vektorinių geoobjektų įrašymui į failą, QGIS praneš naudotojams apie numatytąją jau esamų failų apdorojimo elgseną (failo perrašymą) ir suteiks galimybę parinkti iš aibės alternatyvių elgsenų (tokių kaip perrašyti sluoksnį arba pridėti naujus geoobjektus prie esamo sluoksnio)

Tai stipriai pagerina naudotojų galimybes valdyti duomenis naudojant plokščias failų duomenų saugyklas, tokias kaip geopackage, tuo pačiu minimizuojant duomenų praradimo ar nepageidaujamų šalutinių efektų riziką.

![image16](images/entries/2eaef470fbd823689e50cfd9fde3a747b888bc83.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Savybė: išlaikyti nukopijuotų geoobjektų ryšius
Naujas funkcionalumas užtikrina, kad tame pačiame sluoksnyje nukopijuoti geoobjektai ir toliau atsižvelgs į projekto ryšių stiprumą.

Kopijuojant geoobjektus tame pačiame vektoriniame sluoksnyje naudojant žemėlapį, atributų lentelę ar geoobjektų kopijavimo/perkėlimo įrankį, QGIS dabar seks bet kokius ryšius atvertame projekte ir dubliuos geoobjektus su išlaikytais ryšiais.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Analizės įrankiai
### Savybė: rastro juostos aprašymo palaikymas
QGIS dabar rastro sluoksnių simbologijos kortelėje rodys juostų aprašymus, kartu su juostų numeriu.

![image17](images/entries/5a45eb1db489ef62f677a745efcca6c07935c4e8.webp)

Šią savybę finansavo Vasara darosi vis šiltesnė ir šiltesnė.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Apdorojimas
### Savybė: glotninimo nustatymas rasto kaladėlių apdorojimo priede
A new \"Enable antialiasing\" parameter has been added to the \"Generate XYZ Tiles\" processing tool.

Ši parinktis įjungiama pagal nutylėjimą (pakartojant dabartinę elgseną), bet leidžia naudotojams išjungti žemėlapio turinio glotninimą.

![image18](images/entries/9c9b07222673e23caf2dcc73ff1db8a8f9257106.webp)

This feature was developed by [ASAI Hitoshi](https://github.com/hito-asa)
### Feature: Create Grid row_index and col_index fields
Fields for the `row_index` and `col_index` have been added to the output of the \"Create Grid\" processing algorithm. The fields are added to all outputs of type point, rectangle, and hexagon.

Laukų reikšmės yra sveiki skaičiai, kurie pradedami skaičiuoti nuo 0 ir didėja iš kairės į dešinę (stulpelių indeksas) ir iš viršaus žemyn (eilučių indeksas).

![image19](images/entries/54157595e9bf9c58b4b906ea28b3c335a737696b.webp)

This feature was developed by [Valentin Buira](https://github.com/Poulpator)
### Feature: New \'Calculate expression\' algorithm for use in models
The new \"Calculate expression\" algorithm will calculate the results of a QGIS expression and make the result available for use in other parts of the model.

Taip išvengiama poreikio naudoti tą pačią išraišką kelis kartus tame pačiame modulyje, jei to paties rezultato reikia daugiau nei kartą bei leidžia papildomus panaudojimus (tokius kaip statinės laiko žymos sukūrimas, naudojimui modelyje).

![image20](images/entries/90b9d8da0ec1f13c638525cedd360a5c65d89c1a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: pridėtas algoritmas turinio konvertavimui iš GLTF/GLB failo į standartinius vektorinio sluoksnio geoobjektus.
QGIS dabar leidžia konvertuoti GLTF ir GLB formatų 3D kaladėlių turinį į redaguojamų vektorinių geoobjektų formatus.

![image21](images/entries/6c95d6382b9e6abe72607df57dfefb8a4d9e8442.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Port SAGA \"DTM Filter (slope-based)\" tool to a native QGIS algorithm
The SAGA [DTM Filter tool](https://saga-gis.sourceforge.io/saga_tool_doc/8.1.0/grid_filter_7.html) has been ported to a native QGIS algorithm.

![image22](images/entries/740fdd036b19e5e0d2c13493d66e785fca89b46a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Programos ir projekto parinktys
### Savybė: išvalyti paskutinių naudotų projektų sąrašą
A \"Clear Recently Opened\" action is now listed at the bottom of the `Project → Open Recent` menu, which will remove every unpinned project from the menu.

An additional context menu is also available to enable the ability to remove individual projects from the recent project list, as well as \"pin\" and \"unpin\" items.

Būsena bus sinchronizuojama tarp paskutinių projektų meniu ir QGIS pasveikinimo puslapio.

![image23](images/entries/4ff4dd8614e4857810fc1b636d8700b143ec98b6.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Savybė: OAUTH2 PKCE autorizacijos kodas
An implementation of Proof Key for Code Exchange (PKCE, [RFC 7636](http://tools.ietf.org/html/rfc7636)) has been added for OAUTH2 [Authorization Code](https://oauth.net/2/grant-types/authorization-code/) flows, improving resilience to CSRF and code injection attacks.

Šią savybę finansavo Comune di Roma

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Savybė: apdorojimo numatytieji nustatymai iš QGIS konfigūracijos failo
QGIS dabar suteikia galimybę konfigūruoti QGIS apdorojimo karkaso GUI įrankių numatytąsias reikšmes naudojant parametrus, nurodytus QGIS.ini nustatymų faile.

This allows for the configuration of user-specific or organization-wide default values for certain algorithms. For example, to set the default value of the GRID_SIZE (precision) parameter on the intersection algorithm, the following configuration may be added to the `QGIS/QGIS3.ini` in the active user profile directory root:

    [Processing]
    DefaultGuiParam\native%3Aintersection\GRID_SIZE=0.01
    
Kai naudotojas su tokia konfigūracija atidarys atitinkamą įrankinę ir įvykdys algoritmą, numatytoji reikšmė bus jiems nurodyta automatiškai.

This feature was developed by [mhugent](https://github.com/mhugent)
## Profilių brėžiniai
### Savybė: pridėtas nustatymas, valdantis aukščio profilio diagramų fono spalvą
Ši parinktis (pasiekiama naujoje kortelėje Nustatymai → Parinktys → Aukštis) leidžia naudotojams nustatyti konkrečią spalvą, kurią reikia naudoti aukščio profilio fonui.

Taip diagrama gali tapti lengviau skaitoma su kai kuriais duomenų rinkiniais, pvz. taškų debesimis su RGB spalvomis, kur numatytoji fono spalva per daug panaši į taškų spalvas, kad būtų galima lengvai išskirti.

Tai pasirinktinis nustatymas, pagal nutylėjimą aukščio profiliai ir toliau naudos standartinę sistemos fono spalvą.

![image24](images/entries/e3bae5cc601894eca9775d5603cc3af6bd03c747.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Duomenų tiekėjai
### Savybė: aptikti Oracle tiekėjo ryšius
QGIS dabar palaiko automatinį Oracle duomenų tiekėjo ryšių aptikimą.

![image25](images/entries/951d7ccce5b34532595a21373d721f581938c65b.webp)

Šią savybę finansavo Métropole de Lille

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
## Priedai
### Savybė: išmesti interaktyvią konsolę iš GRASS C++ priedo
Dėl palaikymo priežasčių, GRASS C++ priedo interaktyvi konsolė bei įdėtas QTermWidget buvo išimti iš ateities laidų.

Tikimasi, kad ateityje GRASS apdorojiom priedui bus suteiktas prioritetinis vystymas ir palaikymas, ir interaktyvios GRASS komandinės eilutės palaikymas nebus QGIS kritinis funkcionalumas, bet kažkas, ką naudotojai galės valdyti išoriškai.

Further details on the specifics of this feature cleanup can be found on the feature [Pull Request](https://github.com/qgis/QGIS/pull/53597).

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Programavimas
### Savybė: funkcija vykdomo profilio modelio turinio eksportavimui tekstu
A new function has been added to allow for the export of the current runtime profiler (`QgsRuntimeProfiler`) model content as a multi-line text string.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Svarbūs pataisymai
### Savybė:Alessandro Pasotti riktų pataisymai (itOpen / qcooperative)
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| QGIS cannot connect to MySQL if user\'s password contains commas. | [#54493](https://github.com/qgis/QGIS/issues/54493) | [PR #54573](https://github.com/qgis/QGIS/pull/54573) | Ne |
| QGIS WFS server will look for .qgz file in wrong place if \"map\" is in path | [#54533](https://github.com/qgis/QGIS/issues/54533) | [PR #54639](https://github.com/qgis/QGIS/pull/54639) | [PR #54855](https://github.com/qgis/QGIS/pull/54855) |
| Raster layer transparency/opacity not stored in saved style | [#54496](https://github.com/qgis/QGIS/issues/54496) | [PR #54644](https://github.com/qgis/QGIS/pull/54644) | [PR #54854](https://github.com/qgis/QGIS/pull/54854) |
| WMS GetPrint with ATLAS_PK has incorrect layers visibility in versions \>= 3.22 | [#54475](https://github.com/qgis/QGIS/issues/54475) | [PR #54651](https://github.com/qgis/QGIS/pull/54651) | [PR #54663](https://github.com/qgis/QGIS/pull/54663) |
| Error saving edit on PostGIS geometry when table also contains geography | [#54572](https://github.com/qgis/QGIS/issues/54572) | [PR #54664](https://github.com/qgis/QGIS/pull/54664) | [PR #54714](https://github.com/qgis/QGIS/pull/54714) |
| Cant subtract or add angles since the degrees symbol has been added | [#54501](https://github.com/qgis/QGIS/issues/54501) | [PR #54687](https://github.com/qgis/QGIS/pull/54687) | N/A |
| WCS Keep Unavailable Layers | [#54702](https://github.com/qgis/QGIS/issues/54702) | [PR #54707](https://github.com/qgis/QGIS/pull/54707) | N/A |
| taxon legend from map whis atlas | [#54654](https://github.com/qgis/QGIS/issues/54654) | [PR #54692](https://github.com/qgis/QGIS/pull/54692) | N/A |
| Spinbox for colum space in legends does not allow to set values above 99.99 units | [#54682](https://github.com/qgis/QGIS/issues/54682) | [PR #54709](https://github.com/qgis/QGIS/pull/54709) | N/A |
| Geometry Error SpatiaLite Database | [#54662](https://github.com/qgis/QGIS/issues/54662) | [PR #54734](https://github.com/qgis/QGIS/pull/54734) | N/A |
| Splitting MultiLineStrings gives awkward results | [#54155](https://github.com/qgis/QGIS/issues/54155) | [PR #54744](https://github.com/qgis/QGIS/pull/54744) | [PR #54851](https://github.com/qgis/QGIS/pull/54851) |
| Open project, then layer properties, close, close project: qgis thinks something has changed | [#54741](https://github.com/qgis/QGIS/issues/54741) | [PR #54757](https://github.com/qgis/QGIS/pull/54757) | N/A |
| Width field of attribute tables in print layouts only uses locale when being edited | [#54204](https://github.com/qgis/QGIS/issues/54204) | [PR #54769](https://github.com/qgis/QGIS/pull/54769) | [PR #54781](https://github.com/qgis/QGIS/pull/54781) |
| Data Source Manger - Browser: Close and Help buttons are missing | [#54171](https://github.com/qgis/QGIS/issues/54171) | [PR #54770](https://github.com/qgis/QGIS/pull/54770) | N/A |
| 0 port in OAuth2 callback URI | [#54562](https://github.com/qgis/QGIS/issues/54562) | Cannot reproduce | N/A |
| QGIS Crashes when editing multiple features simultaneously that have a Value Relation field | [#54164](https://github.com/qgis/QGIS/issues/54164) | [PR #54889](https://github.com/qgis/QGIS/pull/54889) | PADARYTI |
| Crash when playing with duplicated legends in layout | [#52268](https://github.com/qgis/QGIS/issues/52268) | [PR #54947](https://github.com/qgis/QGIS/pull/54947) |  |
| QGIS fails to request more than one WMS-Layer | [#55042](https://github.com/qgis/QGIS/issues/55042) | [PR #55064](https://github.com/qgis/QGIS/pull/55064) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Savybė: Even Rouault (Spatialys) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| qgsgeos.cpp: fix a -Wunused-variable warning | nepranešta | [PR #54612](https://github.com/qgis/QGIS/pull/54612) | N/A |
| qgsvirtualpointcloudprovider.cpp: add a missing variable initialization | nepranešta | [PR #54613](https://github.com/qgis/QGIS/pull/54613) | N/A |
| OAPIF does not honour the view extent | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053400.html) | [PR #54617](https://github.com/qgis/QGIS/pull/54617) | [PR #54792](https://github.com/qgis/QGIS/pull/54792) |
| Does QGIS require units \"m\" for the projection coordinate variables in a netCDF/CF file? | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053413.html) | [GDAL PR 8407](https://github.com/OSGeo/gdal/pull/8407) | N/A |
| Syntactical error with the use of == instead of = for comparison in the WHERE clause | [#54608](https://github.com/qgis/QGIS/issues/54608) | Already fixed | Unable to write any additional layers to an existing FGDB |
| Add minimal CRS information to sqlite exports | [#54560](https://github.com/qgis/QGIS/issues/54560) | [PR #54630](https://github.com/qgis/QGIS/pull/54630) | [PR #54715](https://github.com/qgis/QGIS/pull/54715) |
| Complex Attributes in OGC API Feature-Items have empty content | [#54275](https://github.com/qgis/QGIS/issues/54275) | [PR #54631](https://github.com/qgis/QGIS/pull/54631) | [PR #54679](https://github.com/qgis/QGIS/pull/54679) |
| GPX Provider: missing element when importing gpx file | [#54119](https://github.com/qgis/QGIS/issues/54119) | [PR #54632](https://github.com/qgis/QGIS/pull/54632) | N/A |
| Saving edits on larger vector layers is slow | [#53043](https://github.com/qgis/QGIS/issues/53043) | [PR #54633](https://github.com/qgis/QGIS/pull/54633) | N/A |
| QgsVectorLayerSaveAsDialog: uncheck \'Add saved filed to map\' when selecting PGDump driver (refs #54548) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | Not worth it |
| Spatial filtering of multipart polygons within a shapefile dataset broken | [GDAL issue 8481](https://github.com/OSGeo/gdal/issues/8481) | Ne riktas |  |
| qgis cannot find/identify a polygon feature by clicking a newly created (multi)polygon part | [#54537](https://github.com/qgis/QGIS/issues/54537) | [PR #54761](https://github.com/qgis/QGIS/pull/54761) | [PR #54782](https://github.com/qgis/QGIS/pull/54782) |
| qgis cannot find/identify a polygon feature by clicking a newly created (multi)polygon part | [#54537](https://github.com/qgis/QGIS/issues/54537) | [GDAL PR 8483](https://github.com/OSGeo/gdal/pull/8483) | [GDAL PR 8503](https://github.com/OSGeo/gdal/pull/8503) |
| Export to spreadsheet creates an xlsx file with errors when exporting empty tables/layers | [#42945](https://github.com/qgis/QGIS/issues/42945) | [GDAL PR 8484](https://github.com/OSGeo/gdal/pull/8484) | [GDAL PR 8515](https://github.com/OSGeo/gdal/pull/8515) |
| export bbox wrong when feature crosses anti-prime-meridion (180 deg) | [#42827](https://github.com/qgis/QGIS/issues/42827) | [GDAL PR 8485](https://github.com/OSGeo/gdal/pull/8485) | Not worth it |
| QgsVectorDataProvider.changeAttributeValues() returns True even when it fails | [#54816](https://github.com/qgis/QGIS/issues/54816) | [PR #54905](https://github.com/qgis/QGIS/pull/54905) | [PR #54909](https://github.com/qgis/QGIS/pull/54909) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Savybė: Paul Blottiere (Hytech-imaging) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| Fix segfault in coordinate transform | nepranešta | [PR #54609](https://github.com/qgis/QGIS/pull/54609) | N/A |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [#54598](https://github.com/qgis/QGIS/issues/54598) | [PR #54667](https://github.com/qgis/QGIS/pull/54667) | N/A |
| Database string connection visible in the message bar/QGIS logs | [#54437](https://github.com/qgis/QGIS/issues/54437) | [PR #54650](https://github.com/qgis/QGIS/pull/54650) | N/A |
| PostGIS Connection\'s \"Session ROLE\" is not kept | [#54638](https://github.com/qgis/QGIS/issues/54638) | [PR #54681](https://github.com/qgis/QGIS/pull/54681) | N/A |
| Example files are installed by the server build, and additionally they are in a wrong place | [#54423](https://github.com/qgis/QGIS/issues/54423) | [PR #54708](https://github.com/qgis/QGIS/pull/54708) | N/A |
| Point to Path tool causes QGIS to crash | [#54686](https://github.com/qgis/QGIS/issues/54686) | [PR #54710](https://github.com/qgis/QGIS/pull/54710) | [PR #54784](https://github.com/qgis/QGIS/pull/54784) |
| qgs/qgz project does not save mesh symbology correctly | [#54384](https://github.com/qgis/QGIS/issues/54384) | [PR #54711](https://github.com/qgis/QGIS/pull/54711) | N/A |
| Endless loop if profile is drawn outside layer extent | [#54349](https://github.com/qgis/QGIS/issues/54349) | [PR #54745](https://github.com/qgis/QGIS/pull/54745) | N/A |
| Server: Can\'t enable WFS3 API update endpoint (PUT/PATCH) on layers without geometry | [#46119](https://github.com/qgis/QGIS/issues/46119) | [PR #54789](https://github.com/qgis/QGIS/pull/54789) | N/A |
| Add safe guard around -of in gdal command for batch processing | [#54122](https://github.com/qgis/QGIS/issues/54122) | [PR #54800](https://github.com/qgis/QGIS/pull/54800) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Paul Blottiere (Hytech-imaging)](https://hytech-imaging.fr/)
### Savybė: Sandro Santilli (strk) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| Have QgsRectangle null rectangle printed as EMPTY in wkt | nepranešta | [PR #54831](https://github.com/qgis/QGIS/pull/54831) | N/A |
| Fix aspect ratio computation in QgsLayoutItemMap::zoomToExtent | nepranešta | [PR #54827](https://github.com/qgis/QGIS/pull/54827) | N/A |
| Do not include a BoundingBox tag in GetFeatureInfo responses, when it is null | nepranešta | [PR #54858](https://github.com/qgis/QGIS/pull/54858) | N/A |
| Always run the spell and shell checkers if possible, print warning when not possible | nepranešta | [PR #54847](https://github.com/qgis/QGIS/pull/54847) | N/A |
| Tweak Null rectangle handling | nepranešta | [PR #54872](https://github.com/qgis/QGIS/pull/54872) | N/A |
| Run spellcheck only on changed files in prepare_commit.sh | nepranešta | [PR #54893](https://github.com/qgis/QGIS/pull/54893) | N/A |
| Fix prepare_commit.sh | nepranešta | [PR #54918](https://github.com/qgis/QGIS/pull/54918) | N/A |
| Fix extent computation in QgsSpatiaLiteProvider | nepranešta | [PR #54917](https://github.com/qgis/QGIS/pull/54917) | N/A |
| Do not force verbose build in mingw build | [#54932](https://github.com/qgis/QGIS/issues/54932) | [PR #54924](https://github.com/qgis/QGIS/pull/54924) | N/A |
| Make QgsBookmark string output more explicit about it being EMPTY | nepranešta | [PR #54923](https://github.com/qgis/QGIS/pull/54923) | N/A |
| Fix extent computation in QgsAFSProvider | nepranešta | [PR #54944](https://github.com/qgis/QGIS/pull/54944) | N/A |
| Add `tags` make target | nepranešta | [PR #54948](https://github.com/qgis/QGIS/pull/54948) | N/A |
| Handle null rectangles in QgsExtentWidget::outputExtent | nepranešta | [PR #54953](https://github.com/qgis/QGIS/pull/54953) | N/A |
| Handle null in QgsRectangle grow() and include() methods | nepranešta | [PR #54955](https://github.com/qgis/QGIS/pull/54955) | N/A |
| Add QgsRectangle::setNull(), deprecating setMinimal() | nepranešta | [PR #54934](https://github.com/qgis/QGIS/pull/54934) | N/A |
| Handle Null rectangle in QgsRectangle::buffered | nepranešta | [PR #54967](https://github.com/qgis/QGIS/pull/54967) | N/A |
| Fix extent computation in QgsVirtualLayerProvider | nepranešta | [PR #54976](https://github.com/qgis/QGIS/pull/54976) | N/A |
| Add a QgsRectangle::createNull() temporary static method | nepranešta | [PR #55008](https://github.com/qgis/QGIS/pull/55008) | N/A |
| Fix testRegisterFeatureUnprojectible - Use valid extent in testRegisterFeatureUnprojectible | nepranešta | [PR #55011](https://github.com/qgis/QGIS/pull/55011) | N/A |
| Have QgsGeometry::boundingBox return null rect for null geom | nepranešta | [PR #55012](https://github.com/qgis/QGIS/pull/55012) | N/A |
| Have QgsGeometry::fromRect(NULL RECT) return null geometry | nepranešta | [PR #54954](https://github.com/qgis/QGIS/pull/54954) | N/A |
| Stop considering Rectangle(0,0,0,0) null - while Rectangle(1,1,1,1) is not null | [#45563](https://github.com/qgis/QGIS/issues/45563) | [PR #54646](https://github.com/qgis/QGIS/pull/54646) | N/A |
| Run doxygen layout checker in prepare-commit script, when possible | nepranešta | [PR #54936](https://github.com/qgis/QGIS/pull/54936) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](http://strk.kbt.io/)
### Savybė: Jean Felder (Oslandia) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| qgs3daxissettings: Correctly read viewport ratio on a saved project | nepranešta | [PR #54870](https://github.com/qgis/QGIS/pull/54870) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Savybė: Nyall Dawson (North Road) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| Don\'t show help for algorithms which can\'t be run in qgis_process | [#54914](https://github.com/qgis/QGIS/issues/54914) | [PR #54920](https://github.com/qgis/QGIS/pull/54920) | laukiama |
| Fix crashes in layout designer | [#52079](https://github.com/qgis/QGIS/issues/52079) | [PR #54907](https://github.com/qgis/QGIS/pull/54907) | Too intrusive |
| Fix layout label adjust size to text logic | nepranešta | [PR #54896](https://github.com/qgis/QGIS/pull/54896) | laukiama |
| Fix toggling visibility of group layers resets child layer mask blend modes | [#53088](https://github.com/qgis/QGIS/issues/53088) | [PR #54897](https://github.com/qgis/QGIS/pull/54897) | N/A |
| Ensure identify highlight works for very transparent symbols | [#54830](https://github.com/qgis/QGIS/issues/54830) | [PR #54864](https://github.com/qgis/QGIS/pull/54864) | [PR #54883](https://github.com/qgis/QGIS/pull/54883) |
| Fix layout maps force rasterisation of whole layout when map item has transparency set | nepranešta | [PR #54882](https://github.com/qgis/QGIS/pull/54882) | Too intrusive |
| Fix crash in merge features dialog when a field has a unique constraint set | [#54856](https://github.com/qgis/QGIS/issues/54856) | [PR #54862](https://github.com/qgis/QGIS/pull/54862) | [PR #54878](https://github.com/qgis/QGIS/pull/54878) |
| Fix initial zoom level when opening layout designer windows | [#44421](https://github.com/qgis/QGIS/issues/44421) | [PR #54849](https://github.com/qgis/QGIS/pull/54849) | [PR #54880](https://github.com/qgis/QGIS/pull/54880) |
| Fix hang when exporting 3d maps | [#50067](https://github.com/qgis/QGIS/issues/50067) | [PR #54845](https://github.com/qgis/QGIS/pull/54845) | Too risky |
| Fix layout labels don\'t immediately react to changes when semi-transparent | nepranešta | [PR #54839](https://github.com/qgis/QGIS/pull/54839) | [PR #54863](https://github.com/qgis/QGIS/pull/54863) |
| Fix crash when opening layer properties for raster layer with broken data source | [#49176](https://github.com/qgis/QGIS/issues/49176) | [PR #54812](https://github.com/qgis/QGIS/pull/54812) | [PR #54838](https://github.com/qgis/QGIS/pull/54838) |
| Fix Execute SQL exeception | [#54833](https://github.com/qgis/QGIS/issues/54833) | [PR #54837](https://github.com/qgis/QGIS/pull/54837) | [PR #54842](https://github.com/qgis/QGIS/pull/54842) |
| Cleanup all browser layer properties dialog before exiting | [#39094](https://github.com/qgis/QGIS/issues/39094) | [PR #54808](https://github.com/qgis/QGIS/pull/54808) | [PR #54822](https://github.com/qgis/QGIS/pull/54822) |
| Avoid loss of attributes when calculating fields | [#47385](https://github.com/qgis/QGIS/issues/47385) | [PR #54815](https://github.com/qgis/QGIS/pull/54815) | [PR #54879](https://github.com/qgis/QGIS/pull/54879) |
| Fix crash when changing layers between editable/non-editable layers | [#54802](https://github.com/qgis/QGIS/issues/54802) | [PR #54813](https://github.com/qgis/QGIS/pull/54813) | N/A |
| Fix QgsField::ConfigurationFlag::None causes syntax error when starting PyQGIS | nepranešta | [PR #54809](https://github.com/qgis/QGIS/pull/54809) | N/A |
| Handle sql=\'\' or sql=\"\" as empty sql strings instead of \'\' / \"\" literals | [#53736](https://github.com/qgis/QGIS/issues/53736) | [PR #54806](https://github.com/qgis/QGIS/pull/54806) | [PR #54826](https://github.com/qgis/QGIS/pull/54826) |
| Fix crash when certain symbol pages are open in style dock and QGIS is closed or a new project opened | nepranešta | [PR #54749](https://github.com/qgis/QGIS/pull/54749) | Too intrusive |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Savybė: Julien Cabieces (Oslandia) riktų pataisymai
| Rikto pavadinimas | URL issues.qgis.org (jei pranešta) | URL Commit (Github) | 3.28 atgalinis pokytis (GitHub) |
| --- | --- | --- | --- |
| Masking with SVG symbol doesn\'t work | [#54926](https://github.com/qgis/QGIS/issues/54926) | [PR #54927](https://github.com/qgis/QGIS/pull/54927) |  |
| Bug on graduated symbology on French QGis 3.28.10 | [#54549](https://github.com/qgis/QGIS/issues/54549) | [PR #54943](https://github.com/qgis/QGIS/pull/54943) | [PR #54963](https://github.com/qgis/QGIS/pull/54963) |
| QGIS crashes when undoing moving of elements in map layout | [#52740](https://github.com/qgis/QGIS/issues/52740) | [PR #54959](https://github.com/qgis/QGIS/pull/54959) | [PR #54969](https://github.com/qgis/QGIS/pull/54969) |
| QGIS Crashes Upon Exporting Layout to PDF when Using Random Point Fill Symbology | [#54065](https://github.com/qgis/QGIS/issues/54065) | poly2tri issue <https://github.com/jhasse/poly2tri/issues/55> |  |
| Label expression with more than 32767 chars becomes invalid when switching from expression dialog back to layer properties | [#54141](https://github.com/qgis/QGIS/issues/54141) | [PR #55051](https://github.com/qgis/QGIS/pull/55051) | [PR #55052](https://github.com/qgis/QGIS/pull/55052) |
| Activating notify/listen feature crash QGIS | [#54260](https://github.com/qgis/QGIS/issues/54260) | [PR #55062](https://github.com/qgis/QGIS/pull/55062) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)

{{<content-end >}}
