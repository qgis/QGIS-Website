---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: projektą
sidebar: true
title: QGIS 2.18 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.18 pakeitimai{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Laidos data: 2016-10-21

Tai paskutinė 2.x laida. Dabartinė ilgo laiko laida (LTR) lieka 2.14.x versija. Ši laida teikia papildomus paskutinės versijos patobulinimus. Pagrindinė veikla šiuo metu susijusi su QGIS 3.0 - kitos kartos laida - kūrimu. Planuojamas išleidimo laikas - 2018 pirmas ketvirtis.

**Ačiū**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## QGIS 2.18.0 versijos rėmėjai
Mes taipogi kasmet gauname paramą iš įvairių organizacijų, kurios dėkingos už mūsų atliekamą darbą ir nori padėti šio projekto ilgalaikiam vystymui. Šie sponsoriai išvardinti žemiau su mūsų padėkomis!

{{<fund type="changelog" relativeImgPath=true >}}
## Bendra
### Savybė: automatinės nuorodos identifikavimo rezultatuose
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Savybė: pelės ratukas virš spalvos dialogo slankiklių
QGIS 2.18 galite sukti pelės ratuką virš bet kokio slankiklio spalvos parinkimo dialoge, kad didintumėte reikšmę mažu dydžiu. Tai patogus būdas daryti mažus spalvų komponentų pakeitimus.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: pridėti savo spalvų schemas į spalvų mygtuko iškrentantį meniu
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Simbologija
### Savybė: spalvos parinkiklis dabar įsiūtas į sluoksnio stiliaus skydelį
QGIS 2.18 paspaudus spalvos mygtuką sluoksnio stiliaus skydelyje, atidaromas spalvos parinkimo dialogas tiesiai stiliaus skydelyje, o ne atskirame dialoge. Tai leidžia interaktyviai keisti spalvas iš karto matant rezultatą.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Užrašai
### Savybė: etikečių sinonimų sąrašas
Pridėta galimybė nurodyti sąrašą etikečių teksto sinonimų. Pavyzdžiui sutrumpintus gatvių pavadinimus.

Naudotojai gali eksportuoti ir importuoti sinonimų sąrašus, kad būtų paprasčiau naudoti ir dalintis.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: patobulintas linijų etikečių vietos parinkimo algoritmas
Stipriai pagerintas paralelinių etikečių režimas linijų sluoksniams. Naujas algoritmas vengia dėti etiketes virš dantytų geometrijų dalių.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: lenktos poligonų etiketės palei perimetrą
Pridėtas naujas poligonų etikečių režimas, kai lenktos etiketės braižomos ties perimetru.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Braižymas
### Savybė: rastro kaladėlių peržiūra (WMTS ir XYZ sluoksniai)
Ankstesnėse QGIS versijose naudotojai turėjo laukti, kol visos sluoksnio kaladėlės atsiunčiamos, prieš pamatant gautą žemėlapį. Dabar tai pataisyta ir kaladėlės pasirodo žemėlapio drobėje iš karto, kai tik yra atsiunčiamos, taip pagerinant naudotojo įspūdžius stipriai sumažinant laiką iki to, kai kažkas parodoma. Taipogi, anksčiau atsiųstos kaladėlės ir žemesnės ar aukštesnės rezoliucijos gali būti panaudotos peržiūros funkcionalumui tose vietose, kur dar neatsiųstos kaladėlės su tinkama rezoliucija.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Savybė: nutraukiamas rastro braižymas (WMS, WMTS, WCS ir XYZ sluoksniai)
Šis papildymas gerina naudotojo įspūdžius dirbant su rastro sluoksniais, atsiunčiamais iš nutolusių stočių. Anksčiau reikėdavo laukti, kol atsiuntimai būdavo pilnai baigiami, kad galėtumėte keisti mastelį ar pastumti žemėlapį, nes naudotojo sąsaja siuntimo metu būdavo užšaldyta. Tai dabar pataisyta, nes rastro sluoksnių braižymą galima nutraukti bet kokiu metu.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Duomenų valdymas
### Savybė: pridėtas požymis kopijuoti tik pažymėtus geoobjektus
Redagavimo neprisijungus priedas yra numatytasis priedas, kuris pateikiamas kartu su QGIS ir kuris leidžia jums dirbti neprisijungus prie nutolusio duomenų rinkinio (pvz. duomenų bazės), keisti duomenis lauke, o grįžus į kontorą sinchronizuoti duomenis. Tai praplečia darbo neprisijungus galimybes, leidusias dirbti tik su didelių sluoksnių poaibiais.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Šią savybę finansavo DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Formos ir valdikliai
### Savybė: leisti kontroliuoti konkrečių redagavimo valdiklių etiketes
Leisti valdyti konkrečių redagavimo valdiklių etiketes formoje. Pertempimo dizaineryje, dvigubas elemento paspaudimas leis valdyti, ar etiketė turėtų būti rodomą kiekvienam konkrečiam elementui.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Savybė: sąlyginis kortelė ir grupių matomumas
Pridėta nauja konfigūravimo parinktis, leidžianti rodyti arba paslėpti korteles ir grupes pertempimo dizainerio formose.

Konfigūravimas atliekamas du kartus paspaudus dizainerio medyje laukų konfigūravimo sąsajoje.

Matomumui valdyti gali būti įvesta išraiška. Išraiška bus įvertinta kiekvieną kartą, kai formoje pasikeičia reikšmės, kortelės ir grupės bus atitinkamai rodomos arba slepiamos.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Savybė: kliento pusės numatytosios laukų reikšmės
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Šią savybę finansavo DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Žemėlapio maketas
### Savybė: tikros šiaurės rodyklės
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Apdorojimas
### Savybė: taško ant paviršiaus algoritmas
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: Apdorojimo ištirpinimo algoritmui galima pateikti kelis laukus
Ištirpinimo algoritmas leidžia ištirpinti pagal daugiau nei vieną lauko reikšmę. Ankstesnėse QGIS versijose ištirpinimas geoobjektus grupuoti galėjo tik pagal vieno lauko reikšmę.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: optimizuotas apdorojimo apkarpymo algoritmas
Apdorojimo karpymo algoritmas buvo optimizuotas pagrindiniams naudojimo atvejams, dėl to stipriai pagreitėjo apkarpymo operacija. Pavyzdžiui:

**Kelių sluoksnio apkarpymas su 1 milijonu eilučių pagal 2 poligonus**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**5 milijonų adresų apkarpymas pagal 2 poligonus**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: apimties stačiakampio algoritmas
Šis naujas algoritmas skaičiuoja apimties stačiakampį (voką) kiekvienam įvesties sluoksnio geoobjektui.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: sujungtų linijų suliejimo algoritmas
Šis algoritmas sujungia visas susiliečiančias MultiLineString geometrijų dalis į vieną LineString geometriją. Jei bet kuri įvesties MultiLineString geometrijos dalis nesiliečia, galutinė geometrijas bus MultiLineString su bet kuriomis linijomis, kurias pavyko ir kurių nepavyko sulieti.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Savybė: geometrijos ribos algoritmas
Šis naujas algoritmas grąžina įvesties geometrijos kombinatorinės ribos uždarą ribą (t.y. topologinę geometrijos ribą). Pavyzdžiui poligono geometrijai tai bus riba, susidedanti iš linijų kiekvienam poligono žiedui. Linijos geometrija gaus ribą, susidedančią iš linijos pradžios ir pabaigos taškų. Šis algoritmas tinka tik poligonų ir linijų sluoksniams.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Duomenų tiekėjai
### Savybė: savas XYZ kaladėlių sluoksnių palaikymas
XYZ formato rastro kaladėlės dabar palaikomos WMS duomenų tiekėjų. Tai leidžia naudotojams naudoti bazinius žemėlapius iš kitų šaltinių, daugiau nebenaudojant trečiųjų šalių priedų, tokių kaip QuickMapServices ar OpenLayers.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Serveris
### Savybė: galimybė segmentuoti geoobjekto informacijos geometriją serveryje
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Šią savybę finansavo Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Priedai
### Savybė: DB tvarkyklė: pridėta galimybė pakeisti SQL sluoksnį
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programavimas
### Savybė: GEOS linijinio referencijavimo funkcijos prieinamumas QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Savybė: Naujos PyQGIS klasės 2.18
### Naujos bazinės klasės
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Naujos GUI klasės, perpanaudojami valdikliai
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Savybė: naujos išraiškų funkcijos
QGIS 2.18 pridėtos kelios naujos išraiškų funkcijos, įskaitant funkcijas kampo/atstumo interpoliavimui.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Šią savybę finansavo Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
