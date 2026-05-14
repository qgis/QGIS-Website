---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: projektą
sidebar: true
title: QGIS 2.16 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.16 pakeitimai{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Laidos data: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Tai nėra ilgalaikė laida**

Ši laida nėra sukurta kaip ilgalaikė laida (LTR). Naudotojai, kurie nori tokios QGIS versijos, kuri nesikeičia ir gauna riktų pataisymus mažiausiai 1 metus, kviečiami naudoti dabartinę LTR laidą 2.14 (kuri dabar tampa mūsų oficialia LTR laida išleidus QGIS 2.16).

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Ačiū**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## QGIS 2.16.0 versijos rėmėjai
Mes taipogi kasmet gauname paramą iš įvairių organizacijų, kurios dėkingos už mūsų atliekamą darbą ir nori padėti šio projekto ilgalaikiam vystymui. Šie sponsoriai išvardinti žemiau su mūsų padėkomis!

{{<fund type="changelog" >}}
## Bendra
### Savybė: geoobjektų kopijavimas GeoJSON formatu
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: saugoti erdvines žymeles projektų failuose
Jei kuriate erdvinę žymelę, dabar galite pasirinkti ją saugoti jūsų aktyviame projekto faile. Žymelių skydelyje rasite varnelę, įjungiančią tokią galimybę.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### Savybė: GNSS GNRMC pranešimų palaikymas
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Šią savybę sukūrė Ondřej Fibich
### Savybė: įkelti GeoJSON geoobjektus tiesiai į QGIS
QGIS iškarpinės tvarkyklė dabar gali išnagrinėti daug papildomų tekstinių formatų, įskaitant ir GeoJSON geoobjektų rinkinių palaikymą. Tai leidžia tiesiai įkelti GeoJSON eilutes į QGIS, kur jos bus automatiškai verčiamos į QGIS geoobjektus.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: žemėlapio patarimų patobulinimai
- Žemėlapio patarimo matomumas dabar išsaugomas tarp sesijų
- Žemėlapio patarimai gali rodyti HTML turinį, įskaitant piešinius, video ir URL nuorodas

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Savybė: QGIS failų tipų darbastalio MIME piktogramos
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - QGIS Projekto failas
- \*.qml - Sluoksnio nustatymų failas
- \*.qlr - Sluoksnio apibrėžimo failas
- \*.qpt - Maketo šablono failas

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## Naudotojo sąsaja
### Savybė: žemėlapio drobės didinimas
Į QGIS pridėtas didinimo įrankis, kuris leidžia didinti žemėlapį nurodytame mastelyje. Tai leidžia padidinti žemėlapį nekeičiant mastelio, taip lengviau tiksliau derinti žemėlapio pozicija, užrašus ir simbolius. Papildomai, numatyta didinimo reikšmė gali būti keičiama nustatymuose, tai labai naudinga didelės raiškos ekranams.

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Savybė: žemėlapio mastelio keitimo patobulinimai
QGIS 2.16 patobulintas žemėlapio drobės mastelio keitimas.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: perdarytas interaktyvus gradiento redaktorius
Buvo perdarytas gradiento rampos redaktorius ir jo interaktyvūs valdikliai, kad būtų lengviau valdyti gradientus. Dialoge dabar yra ir interaktyvus gradiento sustojimų braižymas per spalvų HSV ar RGB reikšmes. Naujo redaktoriaus savybės:
- spalvų sustojimų tempimas ir perkėlimas
- naujo sustojimo pridėjimas dvigubu paspaudimu
- pažymėjimo sustojimo išėmimas paspaudus trynimą
- sustojimo perkėlimas rodyklėmis, greitesnis perkėlimas laikant shift rodyklių paspaudimo metu
- naujo sustojimo pridėjimas tempiant ir numetant spalvą į valdiklį

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: numatytojo atributų dialogo vaizdo pasirinkimas
Ankstesnėse QGIS versijose atributų dialogas visada atsidarydavo lentelės variantu. Dabar jūs galite pasirinkti visada atidarinėti dialogo arba lentelės vaizdu, arba atsiminti paskutinį naudotą vaizdą.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: iššokančių kalendoriukų patobulinimai
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: pagerinti spalvų parinkikliai
Iškrentantis spalvos parinkimo mygtuko meniu dabar rodo spalvų ratą, taip leidžiant labai greitai daryti spalvų pakeitimus.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### Savybė: kopijuoti atributų lentelės langelio turinį
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Savybė: pagerintas HiDPI palaikymas
HiDPI monitorių naudotojai pastebės pagerėjimą naudotojo sąsajoje, nes buvo daugiau padirbėta pagerinant piktogramas, kad jos priklausytų nuo SVG piešinių. Nuo QGIS 2.16 visos įrankinės dabar suderinamos su HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: pagerinta žemėlapio pažymėjimo įrankio elgsena
Žemėlapiu paremto pažymėjimo įrankio elgsenai atlikti tokie pakeitimai:

Paspaudimo ir tempimo žymėjimams:
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Vieno paspaudimo žymėjimams:
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Šis pokytis drobės elgseną sutapatina su kitomis dizaino programomis bei su maketuotojo elgsena.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Dokumentacijos atnaujinimai
### Savybė: QGIS 2.14 dokumentacija
Kadangi dabar yra automatinis būdas sukurti užduotį dokumentacijos repozitorijoje kiekvienai naujai QGIS savybei, mes tikri, kad visos naujos savybės dabar bus dokumentacijoje.

Dokumentacijos komanda sunkiai dirbo su trimis QGIS laidomis: 2.10, 2.12 ir 2.14, todėl dokumentacija dabar atitinka ilgo laiko QGIS laidą. Per paskutinius 4 mėnesius buvo dokumentuotos 180 naujos savybės.

Jei galvojate, kad yra kažkokių nedokumentuotų savybių, prašome pridėti pranešimą, parašykite trumpą funkciją aprašantį tekstą ir taip prisidėkite prie dokumentacijos tobulinimo.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

Dokumentacijos komanda sunkiai dirbs kitus kelis mėnesius, kad dokumentuotų dabartinę stabilią QGIS versiją (2.16).

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Žiūrėkite, kiek darbo buvo atlikta su 2.10, 2.12 ir 2.14 versijomis:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

Šią savybę sukūrė Larry Shaffer
## Simbologija
### Savybė: rodyklės simbolio sluoksnis
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

Kreivinių rodyklių režime linijinio sluoksnio viršūnės naudojamos kaip lankų kontroliniai taškai. Rodykles galima užpildyti bet kuriuo QGIS palaikomu pildymo stiliumi. Parinktys taipogi leidžia parinkti rodyklės tipą (su viena ar dviem rodyklėmis, pilną ar pusinę), jos storį (kuris gali būti kintamas) ir rodyklės dydžius.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: nauji prieinamumo ir riboto regėjimo simboliai
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: nauji paprasto žymeklio simboliai
- dalinis apskritimas, trečdalis, ketvirtadalis apskritimo
- dalinio trikampio žymekliai
- užpildyto kryžiaus ir šešiakampio žymekliai
- deimanto elipsės žymekliai

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Drobėje esančiuose sluoksniuose vis tiek galima žymėti, o pažymėti geoobjektai bus braižomi su numatytuoju simboliu. Redaguojami geoobjektai taipogi bus rodomi.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: daugiau centroido užpildymo taško braižymo valdymo
Pridėta parinktis valdyti ar žymeklis braižomas visose, ar tik vienoje kelių dalių geoobjektų dalyje.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: šriftų žymeklių simbolių kontūro nustatymas
Šrifto žymeklių simboliai dabar gali turėti kontūrą, kuris gali padidinti tokių simbolių matomumą pridedant buferio spalvą. Emoji turintys šriftai gali veikti kaip gražūs žymekliai, kai naudojami su storu kontūru.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: kontūrų sujungimo stiliaus valdymas paprastiems, elipsės ir šriftų žymekliams
Naudotojai dabar gali keisti paprastų, elipsinių ir šrifto žymeklių sujungimo stilių tinkinant simbologiją.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: naujas žemėlapio įrankis interaktyviam taško simbolio poslinkio nustatymui
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: stiliaus prisegimas
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Užrašai
### Savybė: žemėlapio užrašų įrankiai dabar veikia su nuo taisyklių priklausančiais užrašais
Ankstesnėse QGIS versijose, panaudojus nuo taisyklių priklausančius užrašus, jūs negalėdavote naudoti žemėlapio užrašų įrankių, tokių kaip interaktyvaus užrašų vietos keitimo ar pasukimo. Dabar tai jau palaikoma.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Šią savybę sukūrė Martin Dobias
## Diagramos
### Savybė: diagramos dydžio legendos įrašai
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: kontūro pločio vieneto parinkimas
Dabar galima pasirinkti kontūro pločio vienetą. Tai leidžia diagramos dydį valdyti žemėlapio vienetais, kad ji didėtų ir mažėtų priklausomai nuo žemėlapio mastelio, taip išlaikant konkretų kontūro plotį milimetrais.

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Savybė: diagramos elgiasi kaip užrašai ir gali būti valdomos iš įrankinės
Pradžioje buvo užrašų įrankinė, kuri leido:
- nustatyti dabartinio sluoksnio užrašų parinktis
- paryškinti pažymėtus užrašus. Paryškinimas žalias keičiamame sluoksnyje ir mėlynas visais kitais atvejais.
- prisegti ar atsegti užrašus
- perkelti, rodyti ir slėpti užrašus

Su šia nauja savybe atsiranda naujas įrankis užrašų įrankinėje, kuris leidžia nustatyti dabartinio sluoksnio diagramų savybes. Taipogi kiekvienas aukščiau paminėtas įrankis dabar pilnai naudojamas ir su diagramomis.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Braižymas
### Savybė: naujos momentinio paprastinimo parinktys
Naudotojas gali parinkti algoritmą, kuris bus naudojamas vietiniams paprastinimams, kad geometrijos būtų braižomos greičiau. Šiuo metu QGIS reikia tris algoritmus:
- Atstumas (numatytasis algoritmas ir vienintelis variantas, prieinamas ankstesnėse QGIS versijose)
- PritrauktiPrieTinklelio
- Visvalingam

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Savybė: rastro sluoksnių kvantile paremta klasifikacija
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Šią savybę sukūrė Piers Titus van der Torren
### Savybė: gyvas šešėliavimo braižymas
QGIS 2.16 turi naują rastro braižytoją, kuris dinamiškai sukuria šešėliavimo modelį iš skaitmeninio aukščio modelio (DEM).

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Šią savybę sukūrė Asger Skovbo Petersen and Nathan Woodrow
## Skaitmeninimas
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: tęsti linijų geometrijas naudojant formos keitimo įrankį
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Šią savybę sukūrė Martin Dobias
### Savybė: segmentavimo tolerancija
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Šią savybę sukūrė Marco Hugentobler
## Duomenų valdymas
### Savybė: naujos atributų lentelės konfigūracijos parinktys
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Galimybė pridėti naują atributų lentelės stulpelį, kuriame būtų mygtukai, paleidžiantys nuo parinkto geoobjekto priklausantį veiksmą
- Atributų lentelėje stulpelius galima paslėpti (paspaudus dešinį pelės mygtuką ant lauko pavadinimo antraštės)
- QGIS dabar atsimena bet kokių stulpelių pakeistą plotį

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Savybė: keli atributų formos stulpeliai
Naudodami tempimo ir numetimo dizainerį, galite nurodyti, į kelis stulpelius norite paskirstyti laukus.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Įsitikinkite, kad naudojate tempimo ir numetimo formos dizainerio režimą
- Du kartus spauskite ant grupės, tokios kaip kortelės ar grupės
- atsidarys mažas dialogas, kuriame galėsite parinkti stulpelių skaičių

Rikiuotė bus pirmas stulpelis, tada antras stulpelis, tada n-tasis stulpelis, tada kita eilutė ir t.t.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Savybė: eksportuojamų vektorinio sluoksnio atributų valdymas
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

Šią savybę sukūrė Jürgen Fischer, Even Rouault
### Savybė: formų vaizdas: šoninį stulpelį dabar galima rikiuoti
QGIS atributų lentelės formos režime yra šoninis stulpelis, kurį galima naudoti, jei reikia peršokti į konkretų geoobjektą. Iki šios laidos jo nebuvo galima rikiuoti. Norint rikiuoti reikėdavo peršokti į lentelės režimą ir tada atgal į formos režimą. Dabar galima rikiuoti geoobjektus pagal atributus peržiūroje tiesiogiai šoninėje juostoje paspaudus rikiavimo funkciją išraiškos iškrentančiame mygtuke virš šoninio stulpelio.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Savybė: ryšio atskaitos valdiklis: kombinacija pridėti naujas reikšmes
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Savybė: DXF eksporto patobulinimai
Pridėtas palaikymas nuo taisyklių priklausantiems užrašams, pasuktiems simboliams ir 3D geometrijų išvedimui.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Šią savybę sukūrė Jürgen Fischer
### Savybė: aukščiausio lygio valdikliai pertempimo ir numetimo dizaineryje
Dabar galima padėti valdiklius tiesiai formoje su tempimo ir numetimo dizaineriu. Todėl pertempimo dizainerio forma gali egzistuoti be jokių kortelių.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Savybė: forma paremtas parinkimas ir filtras
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

Nauji mygtukai rodomi formos apačioje arba parinkti atitinkamus geoobjektus (su parinktimis pridėti į parinkimą/išimti iš parinkimo/parinkti dabartiniame pažymėjime) arba filtruoti geoobjektus lentelėje (su parinktimis pridėti geoobjektus į dabartinį filtrą arba toliau apriboti dabartinį filtrą).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Šią savybę finansavo SIGE, City of Uster, Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: kurti GeoPackage sluoksnius
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Šią savybę sukūrė Even Rouault
### Savybė: valdiklių apribojimai
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Savybė: vienu metu keisti kelių geoobjektų atributus
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

Šiame režime atributų reikšmių pakeitimai bus taikomi visiems pažymėtiems geoobjektams. Greta kiekvieno redagavimo valdiklio atsiranda nauji valdikliai, kuriuose rodoma dabartinio mult-keitimo būsena ir galimybė atšaukti konkretaus lauko pakeitimus.

Pakeitimai daromi kaip vieno redagavimo komandose, taigi paspaudus atšaukti bus atšaukti visų pažymėtų geoobjektų pakeitimai.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Sluoksnių legenda
### Feature: New option to zoom to a layer\'s visible scale range
Sluoksniams, kurie turi nustatytą matomų mastelių aibę, ši parinktis automatiškai nustatys tokį mastelį, kuris bus artimiausias nuo esamo, bet kuriame sluoksnis yra matomas. Sąsaja papildomai leidžia sluoksnius, kurie esamame mastelyje nerodomi, legendoje išskirti pilka spalva.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Žemėlapio maketas
### Savybė: nauji poligonų ir polilinijų braižymo įrankiai
Žemėlapio maketuotojas dabar turi du naujus formos elementus, kurie paremti viršūnėmis. Naudojant juos jūs galite kelių mygtukų pagalba makete braižyti poligonus ir polilinijas.

Buvo taipogi pridėti nauji įrankiai, leidžiantis keisti viršūnes (pavyzdžiui perkelti ar išimti viršūnes) bei pridėti naujas viršūnes į esamą formą. Maketo poligono ir polilinijų elementams galima priskirti bet kokį linijų ir poligonų sluoksniams galimą stilių!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Savybė: santykinės maketo užrašų nuorodos
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Savybė: įtraukti atlaso geoobjektus į maketo HTML šaltinį kaip GeoJSON
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### Savybė: parametrizuotų svg palaikymas maketo svg piešiniuose
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: lengvesnis HTML naudojimas užrašuose
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: geopririšimo išvestys (pvz. PDF) iš maketo
QGIS 2.16 žemėlapio maketai automatiškai geopririša išvestis (kai išvesties formatas tai leidžia, pvz. TIF ar PDF).

Esama parinktis sukurti pasaulio failą buvo atskirta iš žemėlapio parinkimo geopririšimui. Nauja elgsena yra visada geopririšti išvestis ir tik tada kurti atskirą pasaulio failą, kai atitinkama parinktis yra įjungta.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: maketo žemėlapiai dabar automatiškai atsinaujina pagal rinkinius
Jei nurodyta, kad maketo žemėlapis turi sekti konkretaus stiliaus rinkinį, jis bus automatiškai atnaujintas pakeitus stilių.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Šią savybę sukūrė Martin Dobias
## Analizės įrankiai
### Savybė: vardiniai parametrai išraiškose
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

Vardinių parametrų naudojimas leidžia išaiškinti, ką kiekvienas funkcijos argumentas reiškia, o tai padeda, kai bandote suprasti išraišką vėliau!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: daugiau atstumo vienetų
Atstumo vienetų pasirinkimas buvo praplėstas su naujomis parinktimis, tokiomis kaip kilometras, jardas ir mylia. Naudojant šiuos vienetus nebereikia rankiniu būdu versti atstumus (pvz. pėdas į mylias).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: išraiškų pakeitimai
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Savybė: teksto ir datos laukų statistika
Statistinės apžvalgos prisegamas blokas dabar gali skaičiuoti agreguotą tekstinių ir datų laukų statistiką.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: rodyti kreivės taškų spindulį informacijos įrankyje
Jei spaudžiate ant kreivinės linijos naudodami informacijos įrankį, QGIS dabar informacijos įrankyje parodys ir spindulį.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Šią savybę sukūrė Marco Hugentobler
### Savybė: agregacijų palaikymas išraiškose
QGIS 2.16 pridėtas kai kurių agregacijų tipų palaikymas išraiškų variklyje. Įskaitant:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

Visais atvejais skaičiavimai įrašomi į išraiškos konteksto podėlį, taigi juos skaičiuoti reikia tik vieną kartą kiekvienam išraiškos įvertinimui.

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: fTools priedas buvo pakeistas Apdorojimo algoritmais
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Šią savybę sukūrė Alex Bruy
## Apdorojimas
### Savybė: nustatyti taškų vietas spaudžiant ant drobės
Apdorojimo parametrus, kuriuose turėtų būti įvestos taškų pozicijos, dabar galima nurodyti spaudžiant vietas žemėlapio drobėje. Anksčiau reikėdavo rankomis įvesti koordinates.

Šią savybę sukūrė Alex Bruy
### Savybė: išraiškų ir kintamųjų palaikymas
Algoritmų dialogų įvestys ir išvestys dabar palaiko QGIS išraiškas ir kintamuosius.

Šią savybę sukūrė Victor Olaya
### Savybė: iš anksto sukonfigūruoti algoritmai
Į apdorojimo įrankinę dabar galima pridėti algoritmus su iš anksto sukonfigūruotais parametrais, kaip proceso greitą paleidimą.

Šią savybę sukūrė Victor Olaya
### Savybė: kurti priedą su scenarijumi paremtu algoritmu iš įrankinės
Anksčiau vienintelis būdas sukurti QGIS priedą, kuris pridėtų naują algoritmą į apdorojimą, buvo rankomis sukurti tokį algoritmą ir sukurti naują algoritmo tiekėją. Dabar algoritmus galima rašyti kaip paprastus apdorojimo skriptus, o juos turintis priedas gali būti sukurtas tiesiai iš apdorojimo įrankinės. Tokį priedą tada galima platinti kai paprastą priedą ir jį įjungus bus praplėstas apdorojimas.

Šią savybę sukūrė Victor Olaya
### Savybė: autentifikacijos valdymo naudojimas su PostGIS susijusiuose algoritmuose
Su PostGIS susiję algoritmai dabar naudoja QGIS autentifikacijos valdymą, kad gautų prisijungimo prie PostGIS duomenų bazės informaciją.
- Jei PostGIS jungčiai buvo nurodytas autentifikacijos metodas, naudotojui reikės įvesti jo pagrindinį slaptažodį.
- Jei jungtis neturi nurodyto autentifikacijos metodo, prisijungimo duomenys bus imami iš podėlio, o jei ten jų nėra, naudotojui reikės juos nurodyti, po ko jie bus įdėti į podėlį vėlesniam naudojimui.

Su šiuo pakeitimu daugiau nebereikia jungties nustatymuose saugoti atviru tekstu įrašytų slaptažodžių, kurie būtų naudojami su PostGIS susijusiuose algoritmuose.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Savybė: galimybė rašyti į lenteles be geometrijos
OutputVector algoritmas dabar leidžia rašyti į lenteles be geometrijos.

Šiuo metu tai taikoma tik laukų perdarymo algoritmui, bet gali būti laisvai praplėsta kitiems susijusių algoritmų atributams.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Savybė: papildomi GRASS algoritmai apdorojime
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

Kai kurie testai (daugiausia rastro ir nuotraukų algoritmai) taipogi buvo įtraukti kai kuriems algoritmams, taip palengvinant riktų aptikimą ir tvarkymą.

Pastebėtina, kad GRASS7 apdorojimo algoritmai gali sukurti tik Shapefile vektorinius sluoksnius ir GeoTiff rastrus. Taipogi yra apribojimas kai kuriems GRASS7 rastro algoritmams (visiems algoritmams, kurie dirba su spalvų lentelėmis), kurie dubliuoja rastro sluoksnius į laikinus aplankus. Priklausomai nuo jūsų pradinio rastro dydžio, jums gali prireikti disko vietos, kad juos apdorotumėte.

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Duomenų tiekėjai
### Savybė: OGR duomenų rinkiniai pagal nutylėjimą atidaromi tik skaitymo režime
Leidžia vienu metu keisti Shape failus ir Tabfailus abiejuose QGIS ir MapInfo.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

Šią savybę sukūrė Even Rouault
### Savybė: pagerintas Postgres DOMAIN tipo laukų valdymas
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: leisti projekte konfigūruoti vektorinių sluoksnių tik skaitymo režimą
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Savybė: DB2 duomenų bazių palaikymas
Šią savybę sukūrė David Adler
### Savybė: Postgres materializuotų vaizdų atnaujinimas db tvarkyklėje
### Savybė: OGR FID atributo rodymas
QGIS dabar parodo OGR FID kaip pirmą atributą, kai jis turi prasmę, pvz. GPKG ir kituose duomenų bazėmis paremtuose sluoksniuose.

Šią savybę sukūrė Even Rouault
### Savybė: ArcGIS Map ir Feature REST paslaugos
QGIS dabar gali prisijungti prie ArcGIS REST paslaugų.

Jūs galite prisijungti prie ArcGIS Feature paslaugų (WFS ekvivalentas ESRI pasaulyje) ir ArcGIS Map paslaugų (WMS ekvivalentas). Tiekėjas leidžia iš šių paslaugų skaityti žemėlapius ir vektorinius sluoksnius.

Ši savybė labai patogi naudotojams, kurie nori persijungti iš ESRI GIS priemonių neprarasdami to, ką jie jau sukūrė privačiose ar viešose žemėlapių paslaugose. Jūs taipogi galite prisijungti prie viešų paslaugų, teikiamų ESRI.

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Savybė: įrašyti stilius į MS SQL ir Oracle duomenų bazes
Šią savybę sukūrė Jürgen Fischer ir Christian Frugard
### Savybė: pervadinti sluoksnių laukus
QGIS 2.16 jūs galite pervadinti Postgres, Oracle, OGR ir atminties sluoksnių laukus du kartus paspaudę ant lauko pavadinimo sluoksnio savybių lange.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: bazinis Oracle Workspace Manager palaikymas
Pridėtas Oracle Workspace Manager palaikymas naudojant Oracle tiekėją.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
### Savybė: masyvūs WFS tiekėjo patobulinimai
QGIS 2.16 perdarytas WFS tiekėjas, įskaitant
- Automatinis versijos aptikimas
- Atsisiųstų geoobjektų podėliavimas diske
- Atsisiuntimas fone ir progresyvus braižymas
- WFS 1.1 ir 2.0 palaikymas
- WFS 2.0 GetFeature puslapiavimas
- Pridėti tiekėjo testai
- WFS 2.0 jungimų palaikymas
- URI parametras su sql dalių SELECT / FROM / JOIN / WHERE / ORDER BY
- DateTime laukų valdymas
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- Papildomų/mišrių geometrijų tipų (CurvePolygon, CompoundCurve) palaikymas
- Daugiau tolerancijos ne visai pagal standartą veikiantiems WFS serveriams

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
Išraiškos generuojamos numatytosios postgresql duomenų bazės laukų reikšmės dabar rodomos geoobjekto formoje.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
Pagrindinis šio pagerinimo pranašumas yra tas, kad dabar galima kurti ir susieti įrašus susijusiose lentelėse iki jų įrašymo, nes pirminis raktas jau egzistuos įrašant geoobjektą.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## QGIS Serveris
### Savybė: paryškinimo palaikymas GetMap ir GetPrint užklausose
Šią savybę finansavo Canton of Solothurn

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Savybė: numatytoji duomenų transformacija serveryje
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Priedai
### Savybė: atnaujintas gaublio priedas
- Atnaujinta iki OsgEarth 2.8
- Perrašyta QGIS gaublio kaladėlių tvarkyklė
- Perrašyta sinchronizacijos tarp 2D ir 3D logika
- Migracija į naują geometrijos branduolį
- Kelių foninių sluoksnių palaikymas
- Meniu įtraukti į gaublio langą
- Nepriklausomas gaublio sluoksnių parinkimas
- Mathias Kuhns magistrinio darbo perkėlimas iš QGIS 2.1/OsgEarth 2.4

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Savybė: Gaublys: išsikišantys objektai
Leisti iškišti objektus į 3-ią dimensiją.

Arba fiksuota reikšme arba priklausomai nuo atributo ar išraiškos.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Savybė: API: į vektorinių sluoksnių savybes pridėti puslapiai
Galimybė pridėti papildomus puslapius į vektorinių sluoksnių savybių dialogą.

Tai leidžia su sluoksniu susijusias priedo teikiamas konfigūracijos parinktis dėti tiesiai kur joms vieta geresnei naudotojo patirčiai.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Savybė: Gaublys: vektorių palaikymas
Išsaugoti vektorinius duomenis rodant sluoksnius ant gaublio.

Šią savybę finansavo Master Thesis UZH

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Savybė: Gaublys: vertikalus DTM padidinimas
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## Programavimas
### Savybė: įtraukti valdikliai sluoksnių medyje
Tai leidžia sluoksnių savybių dialoge (legendos kortelėje) apibrėžti valdiklius, įtrauktus į sluoksnių medį konkretiems sluoksniams. Mintis yra turėti būdą greitai pasiekti kai kuriuos veiksmus, kurie dažnai naudojami su sluoksniu.

Įgyvendinimas ateina su permatomumo valdikliu, ateityje gali atsirasti daugiau standartinių valdiklių, pavyzdžiui filtravimas, parinkimas, stilius ar pan. API leidžia priedas registruoti savo valdiklius, kurie būtų naudojami skirtingais, nuo situacijos priklausančiais priedais, priskiriant savo valdiklius jų valdomiems sluoksniams.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Šią savybę sukūrė Martian Dobias
### Savybė: priedai gali pridėti puslapius į vektorinių sluoksnių savybes
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Savybė: naujos PyQGIS klasės, pridėtos 2.16 versijoje
### Naujos bazinės klasės
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) -an abstract base class for composer items which provides generic methods for nodes based shapes such as polygons or polylines
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - a composer item for polygon shapes
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) -a composer item for polyline shapes
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.htmll) -a composer undo command class for grouping / ungrouping composer items
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) -WKB reader which simplifies geometries on the fly
- [QgsAction](https://qgis.org/api/classQgsAction.html) - a utility class that encapsulates an action based on vector attributes
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - stores and manages actions associated with a layer
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) -a utility class for calculating aggregates for a field (or expression) over the features from a vector layer
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) -a container for configuration of the attribute table for a vector layer
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - a representation of the interval between two datetime values
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handles exporting QgsFeature features to GeoJSON features
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - helper utilities for working with JSON and GeoJSON conversions
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) -simple profiler for timing code paths during execution
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - utility class for parsing SQL statements
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of strings
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - a renderer for generating live hillshade models
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) -line symbol layer used for representing lines as arrows
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) -a renderer which draws no symbols for features by default, but allows for labeling and diagrams for the layer
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) -abstract base class for simple marker symbol layers. Handles creation of the symbol shapes but leaves the actual drawing of the symbols to subclasses.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) -filled marker symbol layer, consisting of a shape which is rendered using a QgsFillSymbolV2

### Naujos GUI klasės
#### Perpanaudojami valdikliai
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- atspalvio ratas, spalvų paletės ir spalvų pavyzdžio imtuvas
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subclass with more fine-grained control over how the widget is closed or opened
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - an event filter for watching for focus events on a parent object
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) -an interactive editor for previewing a gradient color ramp and modifying the position of color stops along the gradient
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) -a panel widget that can be shown in the map style dock
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) -factory class for creating custom map layer property pages
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - base class for any widget that can be shown as a inline panel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) -inline panel wrapper widget for existing widgets which can\'t have the inheritance tree changed, e.g dialogs
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) -a stack widget to manage panels in the interface
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) -a class that contains a list of QActions and QShortcuts that have been registered and allows their shortcuts to be changed
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) -this can be used like a regular QTableWidgetItem with the difference that a specific role can be set to sort
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) -renderer widget for configuring the hill shade renderer
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) -widget for controlling a raster layer\'s transparency and related options
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) -renderer widget for configuring arrow symbol layers

#### Perpanaudojami dialogai:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Svarbūs pataisymai
### Savybė: QGIS mokamų riktų taisymo programa
Mes padarėme dar vieną mokamų riktų taisymo ratą (ačiū mūsų sponsoriams ir rėmėjams). Žemiau pateiktas dalyvavusių programuotojų aprašymai:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- Fix broken projective transform in georeferencer (#14551 - severe)
- Fix selecting features by radius fails (#14748 - severe)
- Fix incorrect area calculation for polygon (#14675 - severe, although very unlikely to occur. Unit tests added to cover this edge case)
- Fix dock widget layout (#15011 - severe)
- Fix crash in arrow symbol layer (unreported)
- Fix crash when creating invalid join (unreported)
- Fix parameterised SVGs not shown for composer arrow items (#14997 - high)
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Always use string comparison in expressions for string fields (#13204 - high)
- Fix home dir being added as default svg and template path (#14662, #14652, #14883 - high)
- Fix crash when using inverted polygons with heatmap renderer (#14968 - high)
- Save raster symbology values with full precision (#14950 - normal)
- Actions are not enabled when loading layer with default style (#13910 - normal)
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- Fix cannot deactivate customization widget catcher (#9732 - normal)
- Fix arrow symbol layer head width/height flipped (#15002 - normal)
- Fix joins are not recreated when loading project with bad layers (#10500 - normal)
- Invalidate join cache when layer is modified (#11140 - normal)
- Correctly support joins using virtual fields (#14820 - normal)
- Fix virtual fields which depend on other virtual fields may not be calculated in some circumstances (#14939 - normal)
- Fix rule based labels not shown when using python expression functions (#14985 - normal)
- Auto refresh when symbol levels changed in style dock (#14861 - normal)
- Fix style dock button not synced to dock state (#14862 - normal)
- Fix issues rendering SVG with text (#14644, #14794 - normal)
- Ensure data defined button displayed fields are always up to date (#14809 - normal)
- Fix cannot set shortcut for zoom in (#14958 - normal)
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- Add missing proxies for legend check behaviour to sub renderers for inverted polygon and displacement renderers (unreported)
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- Show WKB type in vector layer metadata (unreported)
- Add missing capabilities strings to layer metadata (unreported)
- Fix debug noise when using 25D geometry layers (unreported)
- Fix some status bar widgets could not be hidden via customisation (unreported)
- Make styling widget live apply remember setting (unreported)
- Don\'t show constraint messages when form is in search mode (unreported)
- Show scrollbars for attribute form as identify results (unreported)
- Make style dock Apply button always enabled (unreported)
- Fix some missing auto updates from style dock (unreported)

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Čia yra pranešimai, su kuriais jis susitvarkė per skirtą QGIS 2.16 riktų taisymo laiką.

**Rimtas/Aukštas:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normalus**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Kita:**
- <https://issues.qgis.org/issues/14981>: Import of Shapefile to Geopackage-Database in DB-Manager fails (analysis)
- <https://issues.qgis.org/issues/15011>: Browser panel is unusable (bisection & analysis)
- <https://issues.qgis.org/issues/14909>: regression: QGIS crashes when closing docked attribute table (analysis)
- <https://issues.qgis.org/issues/13353>: QGIS and gdal 2.0.0 (closed: no further action needed)
- <https://issues.qgis.org/issues/15053>: WMS with EPSG:31255 is shifted (datum=hermannskogel) (analysis. probably outdated proj.4 version)

### Sandro Santilli
- <http://hub.qgis.org/issues/14262>: Overflow on primary key with negative values; cannot save edits
- <http://hub.qgis.org/issues/12228>: Deadlock from parallel rendering
- <http://hub.qgis.org/issues/11371>: Map Composer: group + move + ungroup + undo = crash
- <http://hub.qgis.org/issues/14976>: Repository files modified by \"make check\"
- <http://hub.qgis.org/issues/13635>: Different handling of invalid geometries between LTR and master version
- <http://hub.qgis.org/issues/13952>: QGIS node tool causes snapping another feature randomly

### Martin Dobias
- Digitizing: \"Simplify Feature\" should not open a dialog when no feature is clicked
- Digitizing: how to abort \"Simplify Feature\" or \"Rotate Feature\" tool is not that obvious
- One road missing upon Add Vector Layer!
- Autotracing fails with Circular Arcs in geometries
- WMS not working on master a625eeb (2.15.0-80)
- Processing preconfigured algorithms python error
- GPS don\'t record geometry point, but only attribute values\...
- style dock: transparency panel (global transparency, transparent pixel, etc.) not working for hillshade renderer
- style dock: back button & breadcrumb missing when a rule-based label rule is being edited
- Fix undo/redo for rule-based renderer/labeling in styling dock
- Fix updates of undo widget in styling panel
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Improve QgsMapLayerRegistry stability
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- Fixed some Python 3 compatibility issues
- Work on re-enabling osx tests (merged after 2.16 release)
- API dokumentacija
- startup.py is executed twice
- UX fixes:
  - Attribute table: always show sequential column header numbers
  - Relation Reference Widget: Only enable form button when a feature is set
  - Show feature id in attribute table tooltip
  - Initial widget focus in credential dialog
  - Default timeout for message bar items
  - Add button\" state in postgis source select dialog
- Install missing header files
- Crash on exit
- Network cache directory
- Feature form hidden behind main window on Windows
- Offline editing: Respect relative paths
- Offline editing: changed attributes end up in wrong feature
- Offline editing: Don\'t crash with raster layers
- Relation form grows infinitely
- Fix crash when loading style in layer properties
- Fix crash when closing docked attribute table
- Fix default-misconfigured gpsbabel path
- Show correct feature count with rule that requires geometry
- Fix crash when using 2.5D renderer with incompatible layer

{{<content-end >}}
