---
HasBanner: false
draft: false
releaseDate: '2021-06-18'
section: projektą
sidebar: true
title: QGIS 3.20 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.20 pakeitimai{#changelog320 }
![image1](images/projects/712c5f48a25ce79a413e9cc34336e05100b7f0c1.png)

Release date: 2021-06-18

QGIS 3.20 Odense features a splash screen which displays a section of [the earliest map](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object80440/en/) of Denmark's third largest city, [Odense](https://en.wikipedia.org/wiki/Odense) from 1593. The map was published by [Georg Braun](https://en.wikipedia.org/wiki/Georg_Braun) (1541-1622) in the work *Civitates orbis terrarum* (Cities of the World). Georg Braun's maps are all beautiful and were, for the period, produced at a high cartographic level. *Civitates orbis terrarum* was long the main source of maps of the world's cities, such as [Paris](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62269/en/), [London](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62684/en/), [Mexico City](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62261/en/) and [Aden](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62257/en/).

The name Odense literally means "Odin's temple", and the place may have originally been a shrine to the pagan god Odin. At the bottom left of the map you see the ruins of one of the large Viking-Age ring-shaped fortress, which were constructed in Denmark by the Danish Viking king [Harald Bluetooth](https://en.wikipedia.org/wiki/Harald_Bluetooth) (died c. 985/86). The ring fortress in Odense is called [Nonnebakken](https://odensebysmuseer.dk/nonnebakken-the-viking-ring-fortress-in-time-and-space/?lang=en).

Šioje laidoje yra daug subtilių pakeitimų ir stabilumo atnaujinimų, praplečiančių didžiulį kiekį pačių naujausių savybių, pridėtų paskutinėse QGIS versijose. Šioje laidoje taip pat yra keli duomenų valdymo patobulinimai su keliais išmaniais CRS sistemų ir projekcijų informacijos valdymo ir rodymo pakeitimais. Tarp šių CRS valdymo patobulinimų yra bendras koordinačių epochos palaikymas dinaminėse CRS sistemose ir išmanus tikslumo integralumo įspėjimas, dėl kurio QGIS 3.20 tvirtai stoja GIS duomenų valdymo praktikų didelio tikslumo sistemose vystymo smaigalyje.

Additionally, users can expect improved metadata management and handling for certain data and metadata types. Another key highlight is the native integration of the [nominatim](https://nominatim.org/) geocoding service, which will allow users to search locations and addresses using data from the OpenStreetMap project directly from the QGIS locator bar.

The QGIS Community has also seen an uptick in activity in the [QGIS HUB](https://plugins.qgis.org/), as well as the Virtual QGIS Open Days, with the [Cutting Edge Open Day](https://github.com/qgis/qgis/wiki/QHF-May-2021) showcasing a number of demonstrations which leverage rich QGIS functionality that was introduced in more recent releases.

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Bendra
### Savybė: papildomi būdai atverti atributų lenteles
Anksčiau buvusios klavišų kombinacijos atributų lentelių atidarymui su filtrais, rodančiais tik pažymėtus ar tik matomus drobėje elementus, buvo integruotos į meniu ir įrankines, taip palengvinant darbą ir pagerinant naudotojo patirtį, ypač dirbant su dideliais duomenų rinkiniais.

![image2](images/entries/571fda8da2dc36cc6032354e4249ac9f642aad02.webp)

This feature was developed by [Raymond Nijssen](https://github.com/raymondnijssen)
### Savybė: nustatyti visų atributų lentelės stulpelių dydį
The existing ability to \"Set Width\" and \"Autosize\" for columns has been extended to apply the resizing of a field to all columns.

This includes the ability to set a fixed width or to \"Autosize\" all columns. These actions are available from the attribute table header context menu which is accessible by right-clicking a field header.

![image3](images/entries/424dea8c61279f20c7f3ca5bf3cd13c21f999987.webp)

This feature was developed by [Ben Wirf](https://github.com/benwirf)
### Savybė: autentifikacijos konfigūracijų eksporto/importo palengvinimas
Starting with QGIS 3.20, users can now easily export and import authentication configurations via a pair of actions in QGIS settings\' authentication panel. Exported configurations can be password-protected to avoid sensitive information leakage.

Tai stipriai palengvina įvairių autentifikacijos konfigūracijos dalinimą tarp kelių QGIS naudotojų, ypač kai kalbame apie sudėtingesnes konfigūracijas, tokias kaip auth2.

This feature was funded by Ville d\'Yverdon-les-Bains

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Laikas
### Savybė: laiko navigacijos žingsniai
A temporal navigation step option for \"source timestamps\" has been added to the temporal controller. When selected, this causes the temporal navigation to step between all available time ranges from layers in the project. It\'s useful when a project contains layers with non-contiguous available times, such as a WMS-T service which provides images that are available at irregular dates. This option will allow users to only step between time ranges where the next available image is shown.

![image4](images/entries/09959743079b809c8969b49f5fbbffe774aeb644.gif)

Šią savybę finansavo Natural resources Canada Contract: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: pagerinti WMS-T nustatymai
WMS-T nustatymai buvo supaprastinti bei pridėti valdikliai, leidžiantys lengviau parinkti norimą laiką kai kuriems tiekėjams.

Pakeitimai buvo daromi tokiais tikslais:
- Kad būtų aiškiau, ką konkrečiai valdo kiekvienas nustatymas
- Kad būtų aiškesni ryšiai ir santykiai tarp skirtingų nuostatų
- Kad būtų akivaizdu, kurie nustatymai veikia nepriklausomai nuo to, ar sluoksnis valdomas laiko valdymu ar nustatymai susiję su statiniais WMS-T sluoksniais
- Serveriams, kurie teikia neištisinius datos-laiko diapazonus, vietoje datų diapazono rodomas iškrentantis sąrašas, todėl nebeprivaloma rankomis įvesti tinkamas datas

Nustatymų pavyzdys, kai serveris teikia galimų datų diapazoną:

![available](images/entries/5959d2a149797fdbd8108653dad86b4ba93d54a1.gif)

Nustatymų pavyzdys, kai serveris teikia tik konkrečių galimų datų-laikų sąrašą:

![datetime](images/entries/f8d2510c5cdf7241f1ed61a9bdd0211f1d6fb0f7.gif)

![image7](images/entries/f8ab8c722dde210f851f838752916bfe76147420.webp)

Šią savybę finansavo Natural resources Canada Contract: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: horizontalaus pelės ratuko laiko navigacija
Horizontal scrolling using the mouse wheel (where supported) with the cursor on the map canvas will allow users to navigate, or \"scrub\", the temporal navigation slider backwards and forwards

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Žemėlapio įrankiai
### Savybė: Nominatim Geokodavimo integracija
The Nominatim Geocoder is now natively integrated into QGIS out of the box! QGIS provides a Nominatim locator filter, as well as the \"Batch Nominatim Geocoder\" processing tool for batch geocoding locations.

*Nominatim lokatoriaus filtras*

The QGIS locator bar widget (by default, a search bar in the bottom left corner CTRL+K) now supports Nominatim geocode searches by using the prefix \'\>\'.

Users may now search for locations using the format `> search string` in the locator and will be provided with a selection of results. Selecting a search result will reposition the canvas extent on that location.

*Paketinis Nominatim geokodavimas*

In addition, a new \"Batch Nominatim Geocoder\" algorithm has been added to the QGIS processing toolbox under Vector tools, allowing users to geocode multiple locations at once.

Nominatim yra geokodavimo paslauga, kuri naudoja OpenStreetMap projekto duomenis. Naudojimo apribojimai yra - 1 užklausa per sekundę - atitinka OpenStreetMap Foundation (OSMF) naudojimo sąlygas, duomenys teikiami pagal ODbl licenciją. Papildomai, užklausose į Nominatim paslaugą gali būti ir telemetrijos informacija.

Šios puikios geokodavimo paslaugos nebūtų galima įtraukti į QGIS be OSMF dosnumo ir dalyvavimo.

![image8](images/entries/bd1b0900b9e2b2756dbc9c9aa90f8b8f34ef166e.gif)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Naudotojo sąsaja
### Savybė: apdorojimo istorijos dialogo patobulinimai
The processing\'s history dialog has had a series of user interface improvements, including regrouping of algorithms in meaningful folder structures and making use of individual algorithm icons. Searching for that algorithm you ran last week has never been as easy!

![image9](images/entries/4e8fa82827363fa9b82ed5b79c1b84f12a220465.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: žemėlapio sluoksnių piktogramos išraiškų kūrimo dialoge
The expression builder dialog now displays map layer icons next to the list of layers under the \'Map Layers\' parent group. This speeds up skipping through the list and provides additional context.

![image10](images/entries/2128b48e7c773959e0305181db1b4da9c917889d.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: SVG naršyklės filtravimas
SVG naršyklės sąsaja dabar palaiko paprastą tekstinį filtravimą, leidžiantį naudotojams filtruoti galimus SVG piešinius pagal nurodytą paieškos eilutę.

![image11](images/entries/3e4dfa0a3e25db1821ae914eeec5c34d7c125ebf.gif)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
## Simbologija
### Savybė: interpoliuotos linijos simbolio tipas vektoriniams sluoksniams
QGIS provides a new \"Interpolated Line\" symbol layer type, which results in the rendering of a color and/ or width varying line.

Šis simbolizavimas yra stipriai konfigūruojamas ir leidžia naudotojams greta įvairiausių konfigūravimo parinkčių dar ir susieti atributus ar išraiškas su kiekvienu linijos ekstremumu ar vingiu. Reikšmės interpoliuojamos per visą linijos ilgį tarp ekstremumų. Spalva konfigūruojama naudojant spalvos rampos valdiklį.

![image12](images/entries/ebfd1d989cdb0d61ab56ab5a629a82a716446666.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Savybė: apkarpyti paprastą linijos simbolį
Pridėta galimybė apkarpyti paprastos linijos simbolio pradžią ir pabaigą, tai leidžia nukirpti naudotojo nurodytą linijos atstumą nuo linijos pradžios ar pabaigos. Tai naudinga kuriant sudėtingus simbolius, kur linijos sluoksnis neturėtų persidengti su žymekliais, padėtais linijos geoobjekto pradžioje ar pabaigoje, pavyzdžiui braižant transporto maršrutus. Apkarpymo atstumas leidžia naudoti įvairius matavimo vienetus, įskaitant ir bendros linijos pločio procentą, o taipogi gali naudoti nuo duomenų priklausančius dydžius.

Pavyzdinė šio funkcionalumo panaudojimo galerija:

![image13](images/entries/f0cad8bbc2de6c44b22c4875c45ed6e24e9f4bf6.webp)

![image14](images/entries/14f48f5bcc891d1c97a8b187f53bb21c6dd6dff6.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New \"Embedded styling\" renderer with OGR feature styles support
A new \"Embedded styling\" renderer has been added which exposes OGR feature styles, allowing QGIS to automatically symbolize data from certain datatypes which have integrated style information, such as KML or TAB files.

This feature implements [QEP-209](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/209)

Palaikymas turėtų automatiškai išsiplėsti į visas GDAL tvarkykles, kurios įgyvendina OGR geoobjektų stiliaus API.

Šiuo metu palaikoma tik linijų simbolizacija, bet šiuo metu jau kuriamas taškų ir poligonų simbolizacijos palaikymas.

![image15](images/entries/44767fa890705c09d9c4b21b998807c7999ddde4.gif)

Šis funkcionalumas taipogi palaiko tiesioginį įtrauktų simbolių braižymo konvertavimą į kategorizuotą arba taisyklėmis paremtą braižymą. Tai leidžia QGIS automatiškai kurti kategorijas ar taisykles, kurios simbologiją nustato pagal atitinkamo geoobjekto ID:

![image16](images/entries/3a408fbcff1ee8d5889c3fe30c0d9d831b050698.gif)

![image17](images/entries/be73e288ed1f46860868a6ae49e7d1f8604082b9.webp)

Šią savybę finansavo QGIS Danijos naudotojų grupė

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: naujos elipsių žymeklių formos ir pabaigos stiliai
Prie elipsių žymeklių simbolizavimo pridėtos kelios naujos formos - daliniai lankai ir rodyklių ženklai, taipogi galimybė keisti pabaigos stilių tik braižymą turinčioms elipsės formoms.

![image18](images/entries/3b34a6b8ceb5cad5a423a10562511457c0c21396.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Savybė: nustatyti pabaigos stilius paprastiems žymekliams
QGIS now allows for the pen cap (or line ending) style to be set for simple marker symbol layers, which is useful for the stroke-only symbols like cross and arrowhead markers, where it\'s beneficial to allow the use of round caps instead of square caps.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: elipsės žymeklių simbolizavimo braižymo pabaigos stilius
Elipsės žymekliai dabar palaiko ir braižymo pabaigos (linijos pabaigos) braižymo stilių.

![image19](images/entries/5d01d2759751cf797586797a74beea3c9561677d.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Polygon rings \@geometry_ring_num variable
A new variable, `@geometry_ring_num`, has been added for data-defined styling when rendering polygon rings. The variable is available whenever a polygon outline is being rendered, such as a simple line or marker line. This data-defined property will be set to 0 for the exterior ring, and increment accordingly (1, 2, 3\... etc) for successive interior rings.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Užrašai
### Savybė: etikečių fono pildymo simboliai
Etikečių skydai dabar gali naudoti stačiakampių, kvadratų, apskritimų ir elipsių formų pildymo simbolius.

This extends beyond the previously available ability for these shields to utilize simple fill and stroke and grants the ability to leverage the complete symbology capabilities of QGIS for shield rendering, including the utilization of \"saved styles\".

![image20](images/entries/5698488e5fae8bdd876dfe754b56bfad0c3fd950.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Savybė: etikečių išnešimo suliejimo režimo nustatymai
Etikečių išnešimams dabar galima naudoti išmaniuosius QGIS suliejimo režimus

![image21](images/entries/4dd84f1e0b5ec295da997ffd84fb15b2cae25b13.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Savybė: susieti linijų etiketes su visa linija
In previous versions, when an anchor position for a line label was calculated, QGIS would only consider the visible extent of the feature. This affected the expected label position in some cases, and a new \"Use Entire Line\" setting allows users to configure the behavior according to their needs, so that the entire feature may be considered before label placement rather than just the portion of a feature that is currently visible.

![image22](images/entries/1a1788cc98f860e53b8ba3b1b2d7ad5b0969179f.webp)

Šią savybę finansavo Stadt Zürich

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: baliono išnešimo kampo spindulys
Balloon callout styles now support rounded corners by introducing a \"corner radius\" option, resulting in the ability to easily produce visually pleasing designs.

![image23](images/entries/9c3d5b37de37e8db7168e68229a6bb3cd02138e6.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: Baliono (kalbėjimo burbulio) išnešimai
A new \"balloon\", or speech bubble, callout style is provided for labels.

![image24](images/entries/7dcb80eacfb6e10dc6b6b05a160421a93ee78d14.webp)

Šią savybę finansavo SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: išlenktų linijų išnešimų stilius
A new \"Curved Line\" callout style has been provided for creating cartographically pleasing curved line callouts between the labels and features

Tarp parinkčių yra:
- Konkretaus išlenkimo nurodymas (pagal arba prieš laikrodžio rodyklę)
- Automatinės orientacijos parinktis, kuri nustato optimalią orientaciją kiekvienai konkrečiai etiketei
- Visoms išnešimo linijoms taikomas išlenkimo stiprumo valdymas.

![curved-callout](images/entries/fd1a05c782e4e2e487a5ed876dc6c396269b0acf.gif)

![image26](images/entries/42e4e2dd600bceda0ff426996577761d9e8b1638.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: paryškinti prisegtų išnešimų pradžios ar pabaigos taškus
When the \"show pinned labels\" option is enabled, QGIS will now also highlight any pinned callout start or end points. This allows users to immediately see which callouts points have been manually placed in relation to those that are automatically placed.

![image27](images/entries/e1de38ee6adde2a016b8d4550111ff766211f0f7.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: automatinis papildomų išnešimų laukų kūrimas
QGIS dabar automatiškai sutvarkys papildomų išnešimų laukų kūrimą, kai bus bandoma interaktyviai perkelti išnešimo pradžios ar pabaigos taškus. Taigi naudotojas galės perkelti ne tik etiketę, bet ir patį išnešimą. Naudotojams nebereikės prieš tai patiems kurti papildomų laukų.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: išnešimų pritraukimas
Interaktyviai perkeliant išnešimo liniją ir laikant paspaustą shift mygtuką, išnešimas bus pritraukiamas prie 15 laipsnių kartotinių

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: perjungti sluoksnių etikečių rodymą
Į vektorinių sluoksnių kontekstinį meniu pridėtas greitas veiksmas etikečių rodymo perjungimui. Jis leidžia greitai įjungti ar išjungti etikečių rodymą neprarandant etikečių konfigūracijos. Jei sluoksnyje niekada nebuvo konfigūruotos etiketės ir paspaudžiama ši parinktis, QGIS pabandys pritaikyti paprastą etikečių konfigūraciją naudojant reikšmes pagal nutylėjimą.

![image28](images/entries/023bb952056e1d7f41e7a06590000f17b76d6d45.gif)

Šią savybę finansavo Natural resources Canada Contract: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: nuo duomenų priklausantys išnešimų pradžios ir pabaigos taškai
Etikečių išnešimo linijų pradžios ir pabaigos taškus dabar galima valdyti duomenimis. Tai naudinga valdant kiekvieno konkretaus išnešimo linijas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: leisti interaktyviai perkelti išnešimus naudojant etiketės perkėlimo įrankį
This change allows the interactive \"Move labels\" tool to also move callout endpoints, whenever the callout has data-defined origin or destination fields set.

![image29](images/entries/8bb0e3614666059f3fe66065173f207d335d3800.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Taškų debesys
### Savybė: nutolusių duomenų aibių palaikymas (EPT)
Point cloud datasets that have been processed to [EPT format](https://entwine.io/entwine-point-tile.html) can be loaded from remote HTTP(S) servers, similar to how raster/vector tiles work. This way, it is possible to access large point cloud datasets without first having to download them as LAS/LAZ files. The EPT format is optimized for tiling and streaming, so QGIS only downloads small amounts of data necessary for display of the current view and resolution. This works in both 2D and 3D view.

If you have point cloud datasets in LAS/LAZ format, these can be converted to EPT using [Entwine](https://github.com/connormanning/entwine) or [Untwine](https://github.com/hobu/untwine) (shipped also with QGIS).

How to use: in Data Source Manager \> Point Cloud tab \> select \"Protocol\" as the source type and enter URL of the dataset (normally ending with \"ept.json\").

You can test with [USGS LiDAR data](https://usgs.entwine.io/) - just use the link from \"EPT\" column from one of the datasets. Some example endpoints include:
- [Chicago](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_IL_4County_Cook_2017_LAS_2019/ept.json)
- [Mount Baker](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_WA_MtBaker_2015_LAS_2017/ept.json)
- [Denmark](https://na-c.entwine.io/dk/ept.json)
- [Netherlands AHN2](https://na-c.entwine.io/ahn/ept.json)

By the way, every point cloud dataset that QGIS loads is first processed to EPT (look for \"ept_XXX\" sub-folder where your original data is located), so it is possible to just copy that \"ept_XXX\" folder to a HTTP(S) server and you are ready to use this feature.

![image30](images/entries/50ed450146655afb5c6ae68f0ead344cfc9eea73.webp)

This feature was funded by [Hobu](https://hobu.co/)

This feature was developed by [Belgacem Nedjima (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Spausdinimo maketai
### Feature: \"Convert to Static Text\" option
When using dynamic, or expression-based labels, users may now select the \"Convert to Static Text\" option which has been added to the dropdown menu next to \"Insert/Edit Expression...\", in the layout label properties widget.

This option will evaluate and replace any dynamic parts of a label\'s contents with their current values.

Tai leidžia naudotojui patogiai keisti dinamines etiketes į statines, kad būtų galima rankiniu būdu priderinti rezultatus pagal poreikius.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: XYZ sluoksnių peržiūros žemėlapių elementuose patobulinimas
XYZ sluoksnių peržiūra išdėstymo žemėlapio elementuose buvo pagerinta taip, kad kaladėlių mastelių lygiai atitiktų eksportuojamo išdėstymo lygius net keičiant mastelį išdėstymo kūrėjo dialoge. Naudotojai dabar gali patogiau tvarkyti jų elementų (etikečių, legendos, piešinių ir pan.) vietas pagal žemėlapio peržiūrą, kuri geriau atitinka galutinį rezultatą.

Šią savybę finansavo Kanton Zug - Amt für Raum und Verkehr (ARV)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Išraiškos
### Savybė: funkcija length3D
A \"length3D\" function has been added for returning the 3D length of a LineGeometry type geometry. This calculates the cartesian 3D length of a geometry line object. If the geometry is not a 3D line object, it returns its 2D length.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: praplėstos masyvo išraiškų funkcijos
Pridėtos šios masyvų išraiškos:
- array_count
- array_prioritize
- array_replace

Šią savybę finansavo Canton of Luzern

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
### Savybė: MIME tipo išraiškos funkcija
The new `mime_type( bytes )` expression function returns the MIME Type, or [Media type](https://en.wikipedia.org/wiki/Media_type), of an input bytes object

![image31](images/entries/c6aa4689915ec3337efac4284ed39a15e8cadddf.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Skaitmeninimas
### Savybė: suliejant parinkti atributus iš didžiausios geometrijos
Į poligonų ir linijų suliejimo įrankio patvirtinimo dialogą pridėtas mygtukas, leidžiantis parinkti atributus iš didžiausios geometrijos.

![image32](images/entries/e27a6a42f878cdfec87021d53241457aa1d8845f.webp)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Savybė: laisvo skaitmeninimo režimas
When streaming digitizing mode is active, points are automatically added following the mouse cursor movement, providing a \"freehand drawing\" type experience.

Using the \"R\" key during digitizing operations will toggle streaming digitizing and normal (or circular string) digitizing.

Veikia su įvairiais žemėlapio įrankiais, įskaitant ir naujos linijos ar poligono kūrimą, žiedo pridėjimą, dalies pridėjimą, formos keitimą, geoobjektų dalinimą, dalių dalinimą ir t.t.

![image33](images/entries/854b65b029335216c7e37c89168389f945e62fe2.gif)

Šią savybę finansavo Natural resources Canada Contract: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New \"Line Endpoints\" snapping option
Įjungus šią parinktį pritraukimo režime bus pritraukiama tik iki linijos pradžios ar pabaigos viršūnių. Pritraukiant iki poligono sluoksnio bus pritraukiama tik prie pirmos žiedo viršūnės.

Šią savybę finansavo Natural resources Canada Contract: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: pažymėti viršūnes poligonu
Naudotojai gali naudoti ALT mygtuką viršūnių žymėjimui poligonu skaitmeninimo metu.

Tai turėtų palengvinti konkrečių viršūnių žymėjimą naudojant viršūnių įrankį, mažinant poreikį kelis kartus spausti SHIFT ar CTRL funkcijas, kad prie žymėjimo būtų pridėtos ar išimtos viršūnės.

Tai taip pat sumažina poreikį įmantriai sukinėti žemėlapio drobę, taip išrikiuojant viršūnes žymėjimui. Taipogi praplečiamas redagavimo procesas, pavyzdžiui vingiuoto kelio tik vienos pusės viršūnių žymėjimas.

Ši funkcija palaiko šiuos naudojimo veiksmus:
- Alt+click naudojant viršūnių įrankį pradeda poligono skaitmeninimą.
- Kiekvienas vėliau einantis paspaudimas prideda naują viršūnę prie guminio poligono.
- Backspace/ delete pašalina paskutinę pridėtą guminę viršūnę.
- Esc cancels the polygon selection mode, as does backspace/ deleting all of the rubberband\'s vertices.
- Dešinys-paspaudimas užbaigia poligono braižymą ir pažymi visas viršūnes guminio poligono viduje.

![image34](images/entries/d4a70011e9064862c99827f5b940805dd2d45182.gif)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Duomenų valdymas
### Savybė: sluoksnių medžio įspėjimo piktograma sluoksniams su CRS netikslumais
A new \"Show CRS accuracy warnings for layers in project legend\" is provided which, when checked, will display a new warning icon identifying any layers with a CRS which is identified as having accuracy issues.

Mažo tikslumo pavyzdžiai būtų sluoksniai su dinaminiu CRS be koordinačių epochos arba CRS pagrįsti datum rinkiniu su tikslumu, kuris viršija naudotojo nurodytą ribą.

Pagal nutylėjimą ši parinktis išjungta ir sukurta naudojimui inžinerijos, BIM ir kitose pramonėse, kur metro ir mažesni netikslumai yra labai pavojingi.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė bazinis dinaminio CRS koordinačių epochos palaikymas
Basic support for the coordinate epoch of dynamic (not plate fixed) CRS has been added in line with relevant updates to [GDAL](https://github.com/OSGeo/gdal/pull/3810).

QGIS pridėjo šaltinio ar paskirties koordinačių epochos palaikymą transformuojant į arba iš dinaminio CRS.

Jei bandoma transformuoti dinaminį CRS į dinaminį CRS su skirtingomis epochomis, kas šiuo metu nepalaikoma PROJ, naudotojas gauna įspėjamąjį pranešimą apie tai, kad rezultatai gali būti neteisingi ir neturėtų būti naudojami didelio tikslumo darbuose.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: projekcijos informacijos patobulinimai
QGIS projekcijos informacijos valdymas ir rodymas buvo pagerintas įvairiais būdais, įskaitant:
- Pridėta API, leidžianti gauti PROJ veiksmo detales skirtas CRS
- The ability to show extended information about a layer\'s CRS in the layer properties info tab, including accuracy warnings
- The addition of a `@map_crs_projection` variable, for retrieving a friendly name of a map\'s projection (e.g. \"Albers Equal Area\")

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: duomenų ansamblio CRS įspėjimai
QGIS now shows a warning in the projection selection widget when a CRS based on a datum ensemble is selected, warning the user that there\'s an inherent lack of accuracy in the selected CRS.

![image35](images/entries/b99e932e308d3b6d2b3868a88f3528386adb3d1f.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: išlaikyti sluoksnio metaduomenis vektorinių failų eksportuose
A \"persist layer metadata\" checkbox has been added to the export vector file dialog. When checked, any layer metadata present in the source layer will be copied and stored in the destination file.

Šis funkcionalumas įjungtas pagal nutylėjimą ir užtikrina, kad metaduomenys tvarkingai perkeliami į naujai sukurtus elementus, kas ypač efektyvu naudojant GPKG formatą.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: sluoksnio pastabos
QGIS now supports \"layer notes\", which can be created via the \"Add Layer Notes\" action in the layer context menu.

Šios pastabos įrašomos atskirai projekto sluoksniui. Jos gali būti naudojamos kaip vieta, kur gali būti saugomi svarbūs pranešimai projekto naudotojams, tokie kaip atliktini darbai, apdorojimo ar valdymo instrukcijos arba tiesiog kaip paprasti tekstiniai metaduomenys.

Užrašų knygutės piktograma sluoksnių skydelyje rodo, kurie sluoksniai turi prisegtas pastabas. Paspaudus ant knygutės piktogramos pastabos bus atvertos redagavimui.

This feature was discussed in [QEP-206](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/206)

Šias pastabas galima kopijuoti ir įkelti naudojant tradicinius kopijavimo/įkėlimo metodus perkeliant stilius tarp QGIS sluoksnių.

Sluoksnių pastabos taip pat palaikomos ir saugomos QML (QGIS Stiliaus) ir QLR (QGIS sluoksnio aprašymo) failuose.

![image36](images/entries/250d188c3987a1247b9e3a414d5d72c9c681b0ad.webp)

Šią savybę finansavo Alta Ehf

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: automatiškai įkelti .shp.xml metaduomenis
QGIS dabar automatiškai įkels ir konvertuos ESRI metaduomenis, įrašytus į .shp.xml papildomą failą. Kai įkeliami shapefile duomenys ir greta yra šie failai, jie bus įkelti automatiškai, atitinkamai užpildant sluoksnio metaduomenis.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: automatiški versti sluoksnio duomenis iš ESRI Filegeoduombazių į QGIS sluoksnių metaduomenis
When loading data from a .gdb file, QGIS will automatically attempt to translate as much as possible of the original ESRI metadata across to the QGIS metadata, so that it\'s immediately available for use.

Šią savybę finansavo North Road / SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: skaityti laukų domenus iš duomenų rinkinių
Kai formatas palaiko įtrauktus laukų domenus (šiuo metu GPKG ir GDB), QGIS automatiškai konvertuos įtrauktus laukų domenų duomenis į atitinkamas QGIS redaktoriaus lauko konfigūracijas.

Tai reiškia, kad GPKG/GDB su užkoduotais laukų domenais automatiškai įsikels į QGIS su teisingomis reikšmių masyvų valdiklio konfigūracijomis, kad naudotojai galėtų matyti laukų aprašymus, o ne jų kodus. Laukai su diapazono (min/maks) tipo domenais taipogi bus išversti į diapazono valdiklius.

Šią savybę finansavo North Road

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: leisti įkelti GPKG sluoksnius su GEOMETRY tipu
GeoPackage supports layers with a generic \"geometry\" type, with the QGIS release 3.20 it is now possible to load them and specify the requested geometry type on load, just like with PostGIS.

![image37](images/entries/a37aab7ea49b4870a931206e88811ebabcff6546.webp)

This feature was developed by [Marco Bernasocchi (OPENGIS.ch)](https://www.opengis.ch)
### Savybė: eilučių ir skaičių sąrašo tipo laukų redagavimas neprisijungus
PostGIS naudotojų džiaugsmui: redagavimas neprisijungus tapo protingesnis - dabar galite tvarkyti eilučių ir skaičių sąrašų laukų tipus.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Formos ir valdikliai
### Savybė: konkrečiam laukui nustatomas paskutinių reikšmių perpanaudojimas kuriant naujus geoobjektus
Buvo pridėtas išplėstinis paskutinių lauke įvestų reikšmių valdymas - ar reikšmės perpanaudojamos kuriant naujus geoobjektus. Šį funkcionalumą dabar galima valdyti atskirai kiekvienam atributų laukui visuose sluoksniuose.

Istoriškai šis funkcionalumas buvo konfigūruojamas globalia parinktimi, kuri įtakojo VISŲ laukų reikšmių VISUOSE sluoksniuose atsiminimą ir perpanaudojimą QGIS sesijoje, kuriant naujus geoobjektus.

Tai leidžia detaliau naudoti formos elgseną, kai kai kurios reikšmės yra pageidaujamos perpanaudojimui, o kitas geriau ištrinti ir nustatyti į numatytąsias, priklausomai nuo išraiškos.

![image38](images/entries/73f699bdf27a1b3b35de96e7a233d12a49b585d9.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: JSON peržiūros valdiklis
Naujas valdiklis, rodantis JSON duomenis naudotojui draugišku būdu. Duomenis galima rodyti arba išskiriant sintaksę, arba medyje.

![image39](images/entries/1061561e58e1b0807158ab415f4a13b43589d824.gif)

This feature was funded by [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/)

This feature was developed by [Damiano Lombardi](http://damiano@opengis.ch)
## Sluoksnių legenda
### Feature: Vector \"label\" legend entries
QGIS dabar leidžia sluoksnio etiketėms pridėti legendos įrašus, kuriais bus rodomas vektorinių geoobjektų šrifto stilius pagal etikečių klases.

Tai leidžia rodyti legendos įrašus, leidžiančius naudotojams aiškiai identifikuoti geoobjektus pagal legendos stilių, net kai nenaudojama geoobjekto simbologija.

Control of this behavior is made accessible by adding a \"show label legend\" option to the legend tab of the vector layer properties.

![image40](images/entries/89218cecca8823903e432b9cd1a38280cc5101a9.webp)

Šią savybę finansavo Canton of Glarus

This feature was developed by [mhugent](https://github.com/mhugent)
## Apdorojimas
### Savybė: sluoksnių pakavimo algoritme pridėta parinktis įrašyti sluoksnio metaduomenis
Šis papildoma parinktis praturtina sluoksnių pakavimo algoritmą ir nukopijuos išeities sluoksnio metaduomenis į geopackage, kad jie būtų naudojami kaip numatytieji sluoksnio metaduomenys.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: rastro sluoksnių savybių algoritmas
Šis algoritmas gauna bazines rastro savybes, tokias kaip dydis taškais, taško dimensijos (žemėlapių vienetai per tašką), juostų skaičių ir „nėra duomenų“ reikšmę.

It is intended for use as a means of extracting these useful properties to use as the input values to other algorithms in a model, such as passing an existing raster\'s pixel sizes over to a GDAL raster algorithm.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: pagerintas rastravimo veiksmas su 3D palaikymu
Rastravimo (vektorių ir rastro) GDAL procesas dabar palaiko 3D duomenis, t.y. dabar leidžia naudoti geoobjekto Z reikšmę (aukštį) išdeginimo reikšmių ištraukimui.

The use of this option indicates that a burn value should be extracted from the "Z" values of the feature. Works with points and lines (linear interpolation along each segment). For polygons, it only works properly if the features are flat (i.e. contain the same Z value for all vertices)

This feature was developed by [talledodiego](https://github.com/talledodiego)
### Savybė: sluoksnių pakavimo algoritmo parinktis įrašyti pažymėtus
Sluoksnių pakavimo algoritmas buvo pakeistas, leidžiant įrašyti tik pažymėtus geoobjektus

This feature was developed by [Stefan Conrads](https://github.com/stefancon)
### Savybė: apdorojimo konteksto žurnalų lygiai
Į QgsProcessingContext buvo pridėta nauja žurnalizavimo lygio savybė

Tai leidžia algoritmams nustatyti jų išvesties žurnalizavimo lygį.

The qgis_process command line operation has been granted a \--verbose switch to enable verbose log output.

Šią savybę finansavo Natural resources Canada Contract: 3000720411

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: geometrijos pritraukimas perdarytas stipriai pagerinant greitaveiką
This development cycle saw a rework of the inner workings of QGIS\' geometry snapper algorithm, which has led to a significant speed boost. Datasets which could take over 10 minutes to process now take less than 10 seconds.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Add a last_value function to the aggregate algorithm
The aggregate processing tool now includes a `last_value` aggregation function, which is especially useful when working with input data that has meaningful ordering.

![image41](images/entries/77afe9dba20e9134db3a1c628c5eeebab275b87a.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Programos ir projekto parinktys
### Savybė: pridėta globali parinktis išjungti aplankų sekimą
Leidžia naudotojams rankiniu būdu išjungti pagal nutylėjimą aplankų sekimą naršyklėje, taip pat suteikia mechanizmą įmonių diegimuose išjungti šią potencialiai nepageidautiną veikseną.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: API XML autentifikacijos konfigūracijų eksportui ir importui
QGIS dabar teikia QGIS autentifikacijos tvarkyklės eksporto ir importo funkcijas. Šis funkcionalumas dar nepateikiamas per naudotojo sąsają. Gan dažnos sudėtingos autentifikacijos, tokios kaip OAuth2, gali būti užšifruotos ar įrašytos į paprastą tekstą, pagerinant autentifikacijos tvarkymo eigą.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Naršyklė
### Savybė: savos naršyklės aplankų piktogramų spalvos
QGIS now allows users to set a custom icon color for different folders in the browser. This effectively allows users to \"tag\" folders, which aids in the rapid navigation of complex folder structures in the browser.

![image42](images/entries/5135bb429434786f87aca3d2deeb980ce874ae44.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: OWS grupė išimta iš QGIS naršyklės
The non-functional and redundant \"OWS\" Group has been removed from the QGIS Browser panel.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## Duomenų tiekėjai
### Savybė: pridėtas OGR palaikymas integer, real ir integer64 sąrašų duomenų tipams
Prie OGR tvarkyklės pridėti papildomi sąrašų laukų tipai palaikomiems duomenims, tokiems kaip Geojson.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Savybė: vektorinių sluoksnių skaitymo galimybės išplėstos į kitus sluoksnių tipus
Whilst the ability for QGIS to access a layer\'s metadata information, such as reading the extent of a layer from the metadata, was previously restricted to vector layers, this functionality has now been extended to include various other layer types including raster, point cloud, and others.

Šią savybę finansavo Ifremer

This feature was developed by [rldhont](https://github.com/rldhont)
## QGIS Serveris
### Savybė: išorinio sluoksnio nepermatomumas
Išorinių/nutolusių sluoksnių, teikiamų per QGIS Serverį nepermatomumo valdymas

This feature was developed by [mhugent](https://github.com/mhugent)
### Savybė: konfigūruojamas paslaugos URL
Pridėtos papildomos QGIS Serverio parinktys, pagerinančios GetCapabilities atsako rezultatą, ypač be poreikio pildyti įvairius laukus QGIS Projekto konfigūracijoje. Šie atnaujinimai taip pat įjungia daug parinkčių, nustatomų per aplinkos kintamuosius arba pateikiant antraštes per šliuzą.

Buvo pridėtos šios parinktys, serveris jas atpažins tokia tvarka:
- Reikšmė apibrėžta projekte paslaugoje.
- The `<service>_SERVICE_URL` environment variable.
- The `SERVICE_URL` environment variable.
- The custom `X-Qgis-<service>-Service-Url` header.
- The custom `X-Qgis-Service-Url` header.
- Build from the standard `Forwarded` header.
- Build from the pseudo standard `X-Forwarded-Host` and `X-Forwarded-Proto` headers.
- Build from the standard `Host` header and the server protocol.
- Sukonstruota pagal serverio vardą ir serverio protokolą.

This feature was developed by [Stéphane Brunner](https://github.com/sbrunner)
## Svarbūs pataisymai
### Savybė: Even Rouault riktų pataisymai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| compiler warning in QgsMeshDatasetGroupStore::readXml() | nepranešta | [PR #43304](https://github.com/qgis/QGIS/pull/43304) | N/A |
| QGIS lūžta su GDAL 3.3 | [#43224](https://github.com/qgis/QGIS/issues/43224) | [PR #43306](https://github.com/qgis/QGIS/pull/43306) | [PR #43323](https://github.com/qgis/QGIS/pull/43323) |
| Data corrupted when deleting field in a (specific) geopackage layer | [#42768](https://github.com/qgis/QGIS/issues/42768) | [PR #43309](https://github.com/qgis/QGIS/pull/43309) | [PR #43322](https://github.com/qgis/QGIS/pull/43322) |
| PyQGIS: WMS-T layer uri without timeDimensionExtent in it crashes QGIS | [#43158](https://github.com/qgis/QGIS/issues/43158) | [PR #43310](https://github.com/qgis/QGIS/pull/43310) | [PR #43324](https://github.com/qgis/QGIS/pull/43324) |
| Data Corruption: Failed GPKG OID/FID Over-write causes value to spill into next attribute column | [#42274](https://github.com/qgis/QGIS/issues/42274) | [PR #43311](https://github.com/qgis/QGIS/pull/43311) | [PR #43360](https://github.com/qgis/QGIS/pull/43360) |
| \"Split features\" causes data loss | [#41283](https://github.com/qgis/QGIS/issues/41283) | [PR #43328](https://github.com/qgis/QGIS/pull/43328) | [PR #43340](https://github.com/qgis/QGIS/pull/43340) |
| Foreign key constraints checks are ignored on GPKG | [#34728](https://github.com/qgis/QGIS/issues/34728) | [PR #43330](https://github.com/qgis/QGIS/pull/43330) | Neaktualu |
| Strange error message from SQL Query Composer in WFS client | [#42985](https://github.com/qgis/QGIS/issues/42985) | [PR #43334](https://github.com/qgis/QGIS/pull/43334) | [PR #43341](https://github.com/qgis/QGIS/pull/43341) |
| WFS 1.1.0 ExceptionReport response handling : QGIS looks for \'exceptionCode\' but in specifications it\'s \'code\' attribute | [#42196](https://github.com/qgis/QGIS/issues/42196) | [PR #43335](https://github.com/qgis/QGIS/pull/43335) | [PR #43342](https://github.com/qgis/QGIS/pull/43342) |
| Export selection from a large WFS layer fails | [#42049](https://github.com/qgis/QGIS/issues/42049) | [PR #43336](https://github.com/qgis/QGIS/pull/43336) | [PR #43343](https://github.com/qgis/QGIS/pull/43343) |
| Long (?) WKT makes delimited text layer fail on 3.16 and 3.18 | [#43256](https://github.com/qgis/QGIS/issues/43256) | [PR #43337](https://github.com/qgis/QGIS/pull/43337) | [PR #43339](https://github.com/qgis/QGIS/pull/43339) |
| Wrong SRS when reading a Postgis layer | nepranešta | [PR #43338](https://github.com/qgis/QGIS/pull/43338) | Neaktualu |
| Mesh data in GRIB format from ERA5 | [#41809](https://github.com/qgis/QGIS/issues/41809) | [GDAL PR 3875](https://github.com/OSGeo/gdal/pull/3875) | [GDAL PR 3877](https://github.com/OSGeo/gdal/pull/3877) |
| Two OGR provider filtered layers with same source dataset don\'t restore proper feature count / extent on project reload | [#43361](https://github.com/qgis/QGIS/issues/43361) | [PR #43372](https://github.com/qgis/QGIS/pull/43372) | [PR #43394](https://github.com/qgis/QGIS/pull/43394) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/en/home/)
### Savybė: Alessandro Pasotti riktų pataisymai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Data Source Manager fails to derive exact 3D geometry type for GeometryZ PostGIS tables | [#43268](https://github.com/qgis/QGIS/issues/43268) | [PR #43326](https://github.com/qgis/QGIS/pull/43326) |  |
| Attribute table conditional formatting doesn\'t work when using \$geometry is NULL | [#43252](https://github.com/qgis/QGIS/issues/43252) | Man veikia |  |
| QgsZonalStatistics.calculateStatistics() incomplete outputs | [#43245](https://github.com/qgis/QGIS/issues/43245) | [PR #43332](https://github.com/qgis/QGIS/pull/43332) | [PR #43378](https://github.com/qgis/QGIS/pull/43378) |
| Bloga feed.qgis.org užklausa | [#43232](https://github.com/qgis/QGIS/issues/43232) | [PR #43333](https://github.com/qgis/QGIS/pull/43333) | Neaktualu |
| Server: WFS3/API Features - overlapping columns/content on data items as HTML pages | [#42269](https://github.com/qgis/QGIS/issues/42269) | [PR #43363](https://github.com/qgis/QGIS/pull/43363) | [PR #43380](https://github.com/qgis/QGIS/pull/43380) |
| Datum transformation using custom gsb grid for WMS Layer in QGIS Server does not work | [#43072](https://github.com/qgis/QGIS/issues/43072) | [PR #43365](https://github.com/qgis/QGIS/pull/43365) | Neaktualu |
| Server: fix unreported QGIS_OPTIONS_PATH not really working for proj | nepranešta | [PR #43366](https://github.com/qgis/QGIS/pull/43366) | Neaktualu |
| WFS cascade getfeatureinfo fails | [#42062](https://github.com/qgis/QGIS/issues/42062) | Man veikia |  |
| Server standalone: fix unreported project storage not supported with -p | nepranešta | [PR #43381](https://github.com/qgis/QGIS/pull/43381) | [PR #43464](https://github.com/qgis/QGIS/pull/43464) |
| QGIS Server GetPrint: HIGHLIGHT_GEOM is not printed if map layers are configured to follow a map theme | [#34178](https://github.com/qgis/QGIS/issues/34178) | [PR #43391](https://github.com/qgis/QGIS/pull/43391) | Rizikinga |
| Feature count is wrong when adding features from a table with features of mixed geometries | [#43199](https://github.com/qgis/QGIS/issues/43199) | Man veikia |  |
| Not all geometry types are found in PostGIS table with Spatial Type of Geometry | [#43186](https://github.com/qgis/QGIS/issues/43186) | [PR #43419](https://github.com/qgis/QGIS/pull/43419) | Rizikinga |
| Icon not updated when saving a scratch layer | nepranešta | [PR #43431](https://github.com/qgis/QGIS/pull/43431) | [PR #43463](https://github.com/qgis/QGIS/pull/43463) |
| Fix list of protocols in ssh custom configuration | nepranešta | [PR #43432](https://github.com/qgis/QGIS/pull/43432) | Neaktualu |
| Crash with table set to Show Visible, joins, and left open as QGIS is quit | [#43287](https://github.com/qgis/QGIS/issues/43287) | [PR #43434](https://github.com/qgis/QGIS/pull/43434) | Neaktualu |
| \"show label\" is disabled in widget designer but label keeps displaying in attribute form if you use tabs in the Drag and-Drop Designer and the field widget was placed in any tab | [#43103](https://github.com/qgis/QGIS/issues/43103) | [PR #43435](https://github.com/qgis/QGIS/pull/43435) | PADARYTI |
| Naršyklė prideda sluoksnius į projektus su tarpu priekyje | [#43129](https://github.com/qgis/QGIS/issues/43129) | [PR #43436](https://github.com/qgis/QGIS/pull/43436) | Neaktualu |
| saveStyleToDatabase() riktas įrašant daugiau nei vieną sluoksnį į GPKG | [#42988](https://github.com/qgis/QGIS/issues/42988) | Man veikia |  |
| Valdiklio parametrai nesuderinami ryšiams D&D dizaineryje | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43468](https://github.com/qgis/QGIS/pull/43468) | Neaktualu |
| Rule-based rendering sometimes doesn\'t show all results | [#43181](https://github.com/qgis/QGIS/issues/43181) | [PR #43502](https://github.com/qgis/QGIS/pull/43502) | Rizikinga |
| Pataisyta nepranešta trūkstamos rastro juostos statistika informacijos skydelyje | nepranešta | [PR #43507](https://github.com/qgis/QGIS/pull/43507) |  |
| Raster calculator does not create/store statistics for output rasters | [#42835](https://github.com/qgis/QGIS/issues/42835) | [PR #43512](https://github.com/qgis/QGIS/pull/43512) | Ne prioritetas |
| Attribute Form Value Relation Doesn\'t Respect Column Default | [#41951](https://github.com/qgis/QGIS/issues/41951) | Man veikia |  |
| Attribute table in form view can display \"ghost\" attributes | [#43477](https://github.com/qgis/QGIS/issues/43477) | [PR #43533](https://github.com/qgis/QGIS/pull/43533) | Ne prioritetas |
| PG identity default clause issue | <https://lists.osgeo.org/pipermail/qgis-user/2021-June/048983.html> | [PR #43529](https://github.com/qgis/QGIS/pull/43529) | Neaktualu |
| Pyqgis 3.18.3 klaida pridedant wms sluoksnį | [#43580](https://github.com/qgis/QGIS/issues/43580) | [PR #43581](https://github.com/qgis/QGIS/pull/43581) | PADARYTI |
| \"Reuse last entered attribute values\" slows creation of new features on large vector | [#42909](https://github.com/qgis/QGIS/issues/42909) | [PR #43584](https://github.com/qgis/QGIS/pull/43584) | PADARYTI |
| Deleting \"all other values\" breaks date based categorise symbology | [#43651](https://github.com/qgis/QGIS/issues/43651) | [GDAL PR 3978](https://github.com/OSGeo/gdal/pull/3978) |  |
| Fix documentation doctest builds | <https://github.com/qgis/QGIS-Documentation/pull/6747> | <https://github.com/qgis/QGIS-Documentation/pull/6747> | Neaktualu |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Savybė: Paul Blottiere riktų taisymai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| VERSION dabar privaloma WMS 1.3.0 getmap užklausoms | nepranešta | [PR #43459](https://github.com/qgis/QGIS/pull/43459) | [PR #43467](https://github.com/qgis/QGIS/pull/43467) |
| WMTS GetCapabilities ir ašių rikiuotė | [#34826](https://github.com/qgis/QGIS/issues/34826) | [PR #43280](https://github.com/qgis/QGIS/pull/43280) | [PR #43772](https://github.com/qgis/QGIS/pull/43772) |
| Naudoti žemiausią versiją wms derybose | [#41051](https://github.com/qgis/QGIS/issues/41051) | [PR #41376](https://github.com/qgis/QGIS/pull/41376) | Rizikinga |
| QGIS crashes adding a record to a memory (\"scratch\") layer table in some circumstances | [#42578](https://github.com/qgis/QGIS/issues/42578) | Man veikia |  |
| QGIS tyliai nesuveikia, kai papildomas sluoksnis negali būti pridėtas | nepranešta | [PR #43543](https://github.com/qgis/QGIS/pull/43543) | [PR #43773](https://github.com/qgis/QGIS/pull/43773) |
| Nepavyksta įrašyti papildomą talpyklą | [#26365](https://github.com/qgis/QGIS/issues/26365) | [PR #43560](https://github.com/qgis/QGIS/pull/43560) | Rizikinga |
| WMS GetFeatureInfo sluoksniuose su įjungtu laiku neperduoda TIME parametro | [#42141](https://github.com/qgis/QGIS/issues/42141) | [PR #43599](https://github.com/qgis/QGIS/pull/43599) | [PR #43774](https://github.com/qgis/QGIS/pull/43774) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://www.qcooperative.net/)
### Savybė: Denis Rouzaud riktų pataisymai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Valdiklio parametrai nesuderinami ryšiams D&D dizaineryje | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43479](https://github.com/qgis/QGIS/pull/43479) | neaktualu |
| Use a read-only line edit instead of combobox in relation reference doesn\'t allow to add a child from the parent | [#42813](https://github.com/qgis/QGIS/issues/42813) | [PR #43509](https://github.com/qgis/QGIS/pull/43509) | per daug rizikinga / neapsimoka |
| no open-form in all layers feature locator filter (active filter has) + show form instead of error for geometry-less layers | nepranešta | [PR #43462](https://github.com/qgis/QGIS/pull/43462) | ? |
| Nepavyksta pridėti polimorfinių ryšių | [#41959](https://github.com/qgis/QGIS/issues/41959) | [PR #43488](https://github.com/qgis/QGIS/pull/43488) | neaktualu |
| Filtro išraiška iš ryšio valdiklio atributų formose neveikia tinkamai | [#42803](https://github.com/qgis/QGIS/issues/42803) | [PR #43523](https://github.com/qgis/QGIS/pull/43523) | taip |
| fix Picture layout element does not handle properly a non-existing filepath when provided with an expression | [#42280](https://github.com/qgis/QGIS/issues/42280) | [PR #43119](https://github.com/qgis/QGIS/pull/43119) |  |
| relations bug: zoom to child button disappears | [#34477](https://github.com/qgis/QGIS/issues/34477) | Man veikia |  |
| Value Relation and Relation reference widget: Entries are sorted although the option \"Order by value\" is NOT checked | [#26468](https://github.com/qgis/QGIS/issues/26468) | neaišku, kaip šiuo metu tai pataisyti |  |
| Klaidos pridedant geoobjektą su polimorfiniu ryšiu | [#41962](https://github.com/qgis/QGIS/issues/41962) | pataisyta |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Savybė: Loïc Bartoletti riktų pataisymai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProjectionSelectionWidget::selectCrs() negali būti perrašyta su Python | [#43019](https://github.com/qgis/QGIS/issues/43019) | Man veikia. |  |
| Riktas? FindPyQt5.py | [#41913](https://github.com/qgis/QGIS/issues/41913) | [#41913](https://github.com/qgis/QGIS/issues/41913) | neaktualu |
| Nėra Geometry Checker bazinio priedo piktogramos | [#42708](https://github.com/qgis/QGIS/issues/42708) | [PR #43536](https://github.com/qgis/QGIS/pull/43536) | [PR #43549](https://github.com/qgis/QGIS/pull/43549) |
| Prašome išimti neveikiančią OWS grupę iš QGIS naršyklės | [#24841](https://github.com/qgis/QGIS/issues/24841) | [PR #43559](https://github.com/qgis/QGIS/pull/43559) | Neaktualu |
| Kūrimas su išoriniu qwtpolar nepavyksta | [#41910](https://github.com/qgis/QGIS/issues/41910) | [PR #43551](https://github.com/qgis/QGIS/pull/43551) | [PR #43583](https://github.com/qgis/QGIS/pull/43583) |
| Geometrijų tikrinimo įrankis neįrašo numatytųjų veiksmų pakeitimo | [#42489](https://github.com/qgis/QGIS/issues/42489) | [PR #43550](https://github.com/qgis/QGIS/pull/43550) | [PR #43568](https://github.com/qgis/QGIS/pull/43568) |
| Wrong error output location when using Check validity on data with certain type of 3D error | [#43582](https://github.com/qgis/QGIS/issues/43582) | [PR #43588](https://github.com/qgis/QGIS/pull/43588) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Savybė: Julien Cabieces ištaisyti riktai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Postgresql tables with intarray fields as primary key causes problems in python scripts | [#42778](https://github.com/qgis/QGIS/issues/42778) | [PR #43493](https://github.com/qgis/QGIS/pull/43493) | [PR #43510](https://github.com/qgis/QGIS/pull/43510) |
| Cannot instantiate QgsFeatureFilterModel using PyQGIS | [#42488](https://github.com/qgis/QGIS/issues/42488) | [PR #43494](https://github.com/qgis/QGIS/pull/43494) | [PR #43516](https://github.com/qgis/QGIS/pull/43516) |
| QGIS crashes by loading ui file | [#42379](https://github.com/qgis/QGIS/issues/42379) | Dirbama |  |
| QvariantList Field , nothing in attribute table when a single value is in the list | [#33108](https://github.com/qgis/QGIS/issues/33108) | [PR #43508](https://github.com/qgis/QGIS/pull/43508) | [PR #43530](https://github.com/qgis/QGIS/pull/43530) |
| Kopijuoti CRS į iškarpinę, kai kopijuojami parinkti geoobjektai | [#40117](https://github.com/qgis/QGIS/issues/40117) | [PR #43527](https://github.com/qgis/QGIS/pull/43527) | [PR #43532](https://github.com/qgis/QGIS/pull/43532) |
| Open Running (connection) Task makes it impossible to Quit QGIS | [#40001](https://github.com/qgis/QGIS/issues/40001) | [PR #43587](https://github.com/qgis/QGIS/pull/43587) |  |
| Plugin manager doesn\'t work with proxy | [#43284](https://github.com/qgis/QGIS/issues/43284) | Atsiliepimai |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #43617](https://github.com/qgis/QGIS/pull/43617) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Savybė: Peter Petrik ištaisyti riktai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Passwords cannot be saved into keychain on macOS with QGIS 3.16 | [#40541](https://github.com/qgis/QGIS/issues/40541) | atsiliepimai |  |
| buggy profile results in two instances starting | [#29379](https://github.com/qgis/QGIS/issues/29379) | nebe problema |  |
| GRASS plugin init error on macOS | [#41782](https://github.com/qgis/QGIS/issues/41782) | Man veikia. |  |
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | aiškinamasi |  |
| Crash with point clouds when zooming into 3D viewer \[Mac\] | [#41903](https://github.com/qgis/QGIS/issues/41903) | [PR #43743](https://github.com/qgis/QGIS/pull/43743) | neaktualu |
| Crash when chcking the \"Show bounding boxes\" option in 3D view settings | [#40766](https://github.com/qgis/QGIS/issues/40766) | [PR #43755](https://github.com/qgis/QGIS/pull/43755) | backport_bot |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Savybė: Nyall Dawson ištaisyti riktai
| Rikto pavadinimas | URL (jei pranešta, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix browser panel scanning on remote locations can hang QGIS | daug PR'ų |  |  |
| \[3d\] Fix rendering of curved lines using simple line renderer | nepranešta | [Commit 700390a](https://github.com/qgis/QGIS/commit/700390abff6928636de010c49746a10129c215eb) |  |
| Fix layer preview through browser panel | [#43303](https://github.com/qgis/QGIS/issues/43303) | [Commit 7bf85a0](https://github.com/qgis/QGIS/commit/7bf85a0cccc105208a0a9563396ad8ca10a38810) |  |
| \[expressions\] Fix evaluation of round(\...) where input value is a string containing a decimal number | [#36467](https://github.com/qgis/QGIS/issues/36467) | [Commit 42c2061](https://github.com/qgis/QGIS/commit/42c2061c5418bbcfa2fde8aac35486ac7fcb26b1) |  |
| Fix label masking settings get dropped for layers with \",\" or \";\" characters in the text | [#37473](https://github.com/qgis/QGIS/issues/37473) | [Commit 3d4e2f4](https://github.com/qgis/QGIS/commit/3d4e2f460f5ca04a469a2549c69b96dea889b174) |  |
| Fix orphaned symbol masking can force maps to be rasterized | nepranešta | [Commit ffc500d](https://github.com/qgis/QGIS/commit/ffc500d79de02d9f83d36a8fa40b4436079be04d) |  |
| Fix selection of features which use variables in filter rules | [#42006](https://github.com/qgis/QGIS/issues/42006) | [Commit d41c234](https://github.com/qgis/QGIS/commit/d41c2342676098e9c9991305711b9eea748bb858) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[labeling\] Default to \"from symbol bounds\" for cartographic point label placement | [#25866](https://github.com/qgis/QGIS/issues/25866) | [Commit 4ad5d36](https://github.com/qgis/QGIS/commit/4ad5d36d93df8eaf0105aed2c9918197f5bf67ef) |  |
| Fix PyQGIS QgsLineString constructor only accepts lists of QgsPoint, not QgsPointXY as indicated by the documentation | [#43200](https://github.com/qgis/QGIS/issues/43200) | [Commit 2b6c3c1](https://github.com/qgis/QGIS/commit/2b6c3c1db2cc3c8214a6c019c2c044b8bae712f2) |  |
| Fix crash when changing symbol levels through style dock | [#42671](https://github.com/qgis/QGIS/issues/42671) | [Commit f3f4c17](https://github.com/qgis/QGIS/commit/f3f4c17c5fa1d71670d505a2938da2345c683909) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Allow clearing data defined buttons which are set to non-existing fields | nepranešta | [Commit ee03ad5](https://github.com/qgis/QGIS/commit/ee03ad5991094ec975118c986075d0e830dec469) |  |
| \[processing\] Python entry in history dialog should be processing.run line, not processing.execAlgorithmDialog | nepranešta | [Commit 61ac64c](https://github.com/qgis/QGIS/commit/61ac64c5a146adc72d38eaf5ab3fe35a6f51be20) |  |
| Don\'t try to render font marker symbols in massive font sizes, avoid crash | [#42270](https://github.com/qgis/QGIS/issues/42270) | [Commit 12d1078](https://github.com/qgis/QGIS/commit/12d1078a8bc11caef7002629e6315cf50522e732) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix Qgis::MessageLevel::None is not available in PyQGIS | [#42996](https://github.com/qgis/QGIS/issues/42996) | [Commit 02266ef](https://github.com/qgis/QGIS/commit/02266ef8e66ef6613d27e7818e0e7adf0d5a3271) |  |
| Fix marker symbol bounds incorrectly include bounds of disabled symbol layers | nepranešta | [Commit ca54e8f](https://github.com/qgis/QGIS/commit/ca54e8f8520453954e06e4d91adbd375287ddadd) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix hang in rendering joined layers | [#38551](https://github.com/qgis/QGIS/issues/38551) | [Commit ca00377](https://github.com/qgis/QGIS/commit/ca00377027dc7ae6066d8ca5fc3da35ad46dd7c2) | [Commit cdbf722](https://github.com/qgis/QGIS/commit/cdbf7224f716a7272e89239895ae254d2ee31bcd) |
| \[temporal\] Fix broken animations when a non-integer interval value is used (e.g. 1.5 hours) | nepranešta | [Commit 81ec79c](https://github.com/qgis/QGIS/commit/81ec79c0e5d31f0e56413fdb01af320fbc00c564) |  |
| Fix allowing attribute selection for DXF layer name | [#42575](https://github.com/qgis/QGIS/issues/42575) | [Commit 66c6ef9](https://github.com/qgis/QGIS/commit/66c6ef96bcd4bcce4fa06cfc4ea62c87ac2898c9) |  |
| Fix papercut in rule based labeling widget where it\'s possible to uncheck BOTH the filter and else radio buttons | nepranešta | [Commit 1fcb9752](https://github.com/qgis/QGIS/commit/1fcb97522c34d319c18bab13e4ccc64d6161bbef) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix it\'s impossible to change a rule based labeling \"else\" rule back to a normal rule | nepranešta | [Commit de92ca0](https://github.com/qgis/QGIS/commit/de92ca034714452e8de139584518277092ea6c3c) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix data defined properties which bind to a field can have incorrect values when the linked field has a null value | nepranešta | [Commit 4e25c6b](https://github.com/qgis/QGIS/commit/4e25c6bcf413c8d93a09839696dbc93ae0e55f64) | [Commit 2a3bcc3](https://github.com/qgis/QGIS/commit/2a3bcc365d901c3d69270fd9c4a9a2165c2cbd31) |
| Fix broken coordinate transform when exporting features to DXF | [#43449](https://github.com/qgis/QGIS/issues/43449) | [Commit 65c02e0](https://github.com/qgis/QGIS/commit/65c02e024a767ccc57283ec29a9c1b6d6ef8003f) | [Commit 044f6a1](https://github.com/qgis/QGIS/commit/044f6a1ec2d96314805ee9ab9be73d8d25e38597) |
| \[processing\] Don\'t show model child algorithm outputs as choices for multi-layer input parameters when running a model | [#41210](https://github.com/qgis/QGIS/issues/41210) | [Commit f4477b2](https://github.com/qgis/QGIS/commit/f4477b2cc4f29553ceb8c3d2d82139bc955ffd0c) |  |
| Expand on QgsPoint/QgsPointXY documentation to clarify when each class should be used | [#43598](https://github.com/qgis/QGIS/issues/43598) | [Commit ae83444](https://github.com/qgis/QGIS/commit/ae83444c9f0c5ce8056ac7b282d6fb1dedc43ad4) |  |
| Fix crash when canceling union tool | [#43553](https://github.com/qgis/QGIS/issues/43553) | [Commit b1f50bb](https://github.com/qgis/QGIS/commit/b1f50bbc2cefe593918b73af7d2b92ffac9b764d) | [Commit 1f25ba5](https://github.com/qgis/QGIS/commit/1f25ba5dbc58bc2f2efd1d930a6104110abe1569) |
| Fix \"force layer to render as raster\" setting wasn\'t correctly copied | [#43535](https://github.com/qgis/QGIS/issues/43535) | [Commit 1313786](https://github.com/qgis/QGIS/commit/131378650ff47f35588eed04162a7e2f2c728abf) | [Commit dcd016b](https://github.com/qgis/QGIS/commit/dcd016bace01506aa283aa7e6760ebe13bfa0d73) |
| Fix massive performance regression in attribute table | nepranešta | [Commit 5fdb88b](https://github.com/qgis/QGIS/commit/5fdb88bae3e40316a489d71594f17548f7a55f00) | [Commit 4970c3a](https://github.com/qgis/QGIS/commit/4970c3a9dbc66d1b2d155e3cdd07df200ee1c14a) |
| Fix performance issue when using attribute table with \"edited or new features\" filter in place | nepranešta | [Commit af021f1](https://github.com/qgis/QGIS/commit/af021f10fb73d4850a0486527775e7fdc101ef47) |  |
| Fix invalid error message when creating expression for layout text item | [#42884](https://github.com/qgis/QGIS/issues/42884) | [Commit db74013](https://github.com/qgis/QGIS/commit/db74013c7fc5966436fc41b3d912e93367bbec23) |  |
| Clarify labels in temporal controller | nepranešta | [Commit ed346d8](https://github.com/qgis/QGIS/commit/ed346d88fd3ebdf16839fa5b750dc92731cecfb6) |  |
| Correctly redraw canvas when applying project properties changes | nepranešta | [Commit 41f9842](https://github.com/qgis/QGIS/commit/41f98420e028c251cd0619242b5c1e8d01f5d41e) | [Commit 607b44b](https://github.com/qgis/QGIS/commit/607b44b1e0175a97c103eb7c04f2450c1ff924d3) |
| Make interactive labeling tools correctly work with data defined properties which aren\'t bound to fields | nepranešta | [Commit c6bd366](https://github.com/qgis/QGIS/commit/c6bd366112f92e836dd071dd395f8b3dbf982d50) |  |
| Fix crash in labeling if label has data defined x/y set and projection error occurs transforming these coordinates | nepranešta | [Commit 8943ac7](https://github.com/qgis/QGIS/commit/8943ac76d598f96c59d59a2ed530a972f07f89a1) | [Commit 2fe68cc](https://github.com/qgis/QGIS/commit/2fe68cc2f9c776f12fb94886d9c5d660a7d2a99f) |
| \[temporal\] Fix filter generation for vector temporal layers | [#38468](https://github.com/qgis/QGIS/issues/38468) | [Commit 544708f](https://github.com/qgis/QGIS/commit/544708f4aade5c4451463e045fd23c168552ab40) |  |
| Fix formatting of exception blocks in PyQGIS docs | nepranešta | [Commit 8359281](https://github.com/qgis/QGIS/commit/835928101213484c23f46e5c91b8329102478534) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix zonal statistics does not correctly handle coordinate transforms | [#26858](https://github.com/qgis/QGIS/issues/26858) | [Commit e70cf8d](https://github.com/qgis/QGIS/commit/e70cf8da2747c13e02866bc940ce4dbb3af41815) | [Commit c82678d](https://github.com/qgis/QGIS/commit/c82678dd6136de79cd76206c9ca25b1f9e34abd2) |
| Don\'t assume that owslib \>= 0.20 is available | [#38074](https://github.com/qgis/QGIS/issues/38074) | [Commit 3cf9083](https://github.com/qgis/QGIS/commit/3cf9083743de2a72893d2efeddcfb29f3ea7130f) | [Commit eb1a55a](https://github.com/qgis/QGIS/commit/eb1a55a146d1dddb7ddf52da9c961e4c5a8cce96) |
| Fix crash in geometry checker when empty geometries are found | [#38983](https://github.com/qgis/QGIS/issues/38983) | [Commit 73a4948](https://github.com/qgis/QGIS/commit/73a49489c857ec492f62bb8ef0ec2494d93d368a) | [Commit 6938593](https://github.com/qgis/QGIS/commit/69385937d842cfa88ff65663591049ca210403b8) |
| \[temporal\] Fix incorrect frame duration in last frame in animation mode | [#40777](https://github.com/qgis/QGIS/issues/40777) | [Commit f76747b](https://github.com/qgis/QGIS/commit/f76747b8b1ffd93844767ad9b66e3601b96a98a2) |  |
| Default to a time range of the last 24 hours, in 1 hour increments, instead of a confusing \"zero length\" range | [#40868](https://github.com/qgis/QGIS/issues/40868) | [Commit 5f5a3a7](https://github.com/qgis/QGIS/commit/5f5a3a7e46fac5a4939d90f2eaf57a8b61008789) |  |
| Fix temporal fields reset if previously set to no value | [#43643](https://github.com/qgis/QGIS/issues/43643) | [Commit 9de5d25](https://github.com/qgis/QGIS/commit/9de5d2500bd358c1214b17434424d1c301444b03) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[processing\] Fix broken execution of models via browser/drag and drop | [#43698](https://github.com/qgis/QGIS/issues/43698) | [Commit cbe2678](https://github.com/qgis/QGIS/commit/cbe2678e34767f01dd3d2578261c4e55e40a00ba) | [Commit 9e0cdcb](https://github.com/qgis/QGIS/commit/9e0cdcba48de04a3fb3a6aa81276e68a0447a6fd) |
| Fix QgsDistanceArea.bearing() | nepranešta | [Commit 0b499d3](https://github.com/qgis/QGIS/commit/0b499d3a0058dbb234ce54f6329015818a9ccde7) |  |
| Don\'t restrict adding crs selections to list of recent CRSes to only a few select dialogs | nepranešta | [Commit 870945c](https://github.com/qgis/QGIS/commit/870945c476c1a429eb410af2a793644a7b1db85f) |  |
| \[processing\] Fix use of data defined parameter values when editing features in place | [#43758](https://github.com/qgis/QGIS/issues/43758) | [Commit 3ae9625](https://github.com/qgis/QGIS/commit/3ae96253de7efc5e8921e776ae91de4b9281d90c) |  |
| \[layouts\] Fix bounding rectangle for shapes doesn\'t include stroke width after loading from xml | [#43748](https://github.com/qgis/QGIS/issues/43748) | [Commit fad1800](https://github.com/qgis/QGIS/commit/fad18003b3560e6daa1c47080f5b2fe10ddef9e6) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
