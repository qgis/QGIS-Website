---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: projektą
sidebar: true
title: QGIS 2.4 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.4 pakeitimai{#changelog24 }
Laidos data: 2014-06-27

Kitos QGIS laidos 2.4.0 pakeitimai. Pagrindinis šios laidos dėmesys buvo skiriamas apdailai ir greitaveikai - pridėjome daug naujų savybių, pataisymų ir praplėtimų, kurie naudotojo sąsają daro nuoseklesne ir profesionalės išvaizdos (ir tikėkimės paprastesne naudoti). Kūrėjas (kuris naudojamas kuriant spausdinimui paruoštus žemėlapius) buvo stipriai patobulintas, kad būtų dar tinkamesnė platforma kuriant puikius kartografinius rezultatus.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Norime padėkoti programuotojams, dokumentuotojams, testuotojams ir dar būriui kitų žmonių, kurie savo noru aukojo savo laiką ir pastangas (arba finansavo tuo užsiimančius žmones).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Na ir pagaliau norėtume padėkoti savo rėmėjams už neįkainojamą finansinę paramą šiam projektui:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Bendra
### Feature: Generate band name with NetCDF EXTRA_DIM
NetCDF teikia papildomą matmens informaciją. Ši informacija teikia metaduomenis apie kiekvieną juostą. Šie metaduomenys gali būti naudojami kuriant kiekvienos juostos pavadinimą. Tarkim NetCDF failo juostos rodo temperatūrą nurodytame gylyje. Naudotojui daug paprasčiau parinkti juostą su gylio informacija, o ne su juostos numeriu.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Savybė: mastelio ir poslinkio taikymas rastro duomenims
Kai kuriuose rastro duomenų šaltiniuose duomenys saugomi kaip sveiki skaičiai, kurių mastelis ir poslinkis įrašytas į metaduomenis. Mastelis ir poslinkis gali būti naudojami reikiamų duomenų ištraukimui. QGIS pritaiko tai rastro duomenims, kad naudotojams būtų pateikta teisinga informacija legendoje, histogramoje ir identifikavime.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Savybė: greito laukų skaičiuotuvo juosta atributų lentelėje
Mes turime puikią naują savybę, kuri skirta tiems, kas naudoja vektorių atributų lentelės skaičiuojamus laukus. Nauja greito skaičiavimo juosta leidžia greitai ir paprastai atnaujinti atributų lentelės stulpelių reikšmes.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Savybė: kūrėjo ir žemėlapio drobės spalvų peržiūros režimai
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Savybė: QLR QGIS sluoksnių failai
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Savybė: naujos išraiškų funkcijos
Išraiškų kūrėjas gavo kelias naujas funkcijas.
- apimties stačiakampis (bounds)
- bounding box width & height (bounds_width/bounds_height)
- min/max x/y koordinatės (xmin/xmax/ymin/ymax)
- nauja wordwrap funkcija, kuri grąžina tekstą padalintą į maksimumą/minimumą simbolių skaičių

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Savybė: spalvų kopijavimas, įkėlimas ir pertempimas
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Savybė: paralelinis braižymas keliomis gijomis
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Užrašai
### Savybė: kelios etiketės vienam geoobjektui
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Žemėlapio maketas
### Savybė: kūrėjo piešinių elementų patobulinimai
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Savybė: iš anksto numatytų mastelių režimas atlasui
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Savybė: pagerintos kūrėjo atributų lentelės
Kūrėjo išdėstymuose patobulinta galimybė rodyti lenteles:
- Dabar jau galima pakeisti stulpelių tvarką lentelėje
- Pridėtas išraiškomis paremtų stulpelių palaikymas
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Lentelės turinį galima filtruoti naudojant išraišką

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Savybė: bendri kūrėjo patobulinimai
Žemėlapių kūrėjas buvo patobulintas, kad būtų paprasčiau dirbti kūrimo režime:
- Pridėtas mygtukas, rodantis dabartinio žemėlapio elemento apimtį pagrindinio žemėlapio drobėje
- Galimybė eksportuoti SVG piešinius iš kūrėjo su sluoksniais
- Mastelio juostoms nustatyti linijų sujungimo ir pabaigos stilių
- Elementų rėmams nustatyti linijų sujungimo ir pabaigos stilių

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Savybė: HTML rėmų patobulinimai
Patobulinti kūrėjo HTML rėmai. Atsirado naujas mygtukas **pridėti rėmą**, kurio pagalba galima sukurti kelis susietus rėmus. Taipogi patobulinta puslapių atskyrimo logika, dėl ko dabar bus mažesnė tikimybė, kad puslapiai bus atskirti vidury teksto linijų puslapiuojant HTML rėmus.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Priedai
### Savybė: MetaSearch katalogo kliento priedas
MetaSearch - tai QGIS priedas bendravimui su metaduomenų katalogo paslaugomis, palaikančiomis OGC katalogo paslaugų tinklui (CSW) standartą. Šis priedas suteikia paprastą ir intuityvią naudotojui draugišką sąsają paieškai kataloguose iš QGIS. Šis priedas dabar tiekiamas kartu su bazine QGIS komplektacija.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Simbologija
### Savybė: išdeginimo pagal formą pildymo stilius
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Savybė: parinktis pastumti žymekliu liniją
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Savybė: naujas invertuoto poligono braižymas
Poligono geoobjektams pridėtas naujas braižiklis, leidžiantis nurodyti poligono **išorės** stilių. Tai gali būti naudinga paryškinant plotus arba kuriant kartografinius šablonus. Naudojant su nauju formos deginimo stiliumi, dabar galite sukurti rezultatą kaip parodyta žemiau.

**Pastaba:** Nauja šablono priedo versija leidžia lengvai kurti šablonų sluoksnius iš dabartinio pažymėjimo, etiketės dėti tik geoobjektams nurodytuose plotuose ir kurti automatinius šablonus atlaso žemėlapio kūrime.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Savybė: stilių įrašymas ir ištraukimas Spatialite sluoksniuose
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
