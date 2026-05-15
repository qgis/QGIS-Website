---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.18
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.18{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Data lansării: 2016-10-21

Aceasta este ultima versiune din seria 2.x. Versiunea cu Suport pe Termen Lung (LTR) va rămâne 2.14.x. Această versiune oferă îmbunătățiri incrementale față de cea anterioară. Cea mai mare parte a activității este concentrată, în prezent, pentru dezvoltarea QGIS 3.0, care reprezintă prima versiune din următoarea generație, planificată pentru sfârșitul trimestrului 1 din anul 2017.

**Mulțumiri**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Sponsorii versiunii QGIS 2.18.0
Anual primim, de asemenea, sprijin de la diverse organizații care ne apreciază munca pe care o depunem și care ar dori să faciliteze efortul susținut de dezvoltare a proiectului. Acești sponsori sunt enumerați mai jos, alături de mulțumirile noastre!

{{<fund type="changelog" relativeImgPath=true >}}
## Generalități
### Funcționalitate: Link-uri automate, în rezultatele instrumentului de identificare
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Funcționalitate: Deplasarea rotiței mouse-ului deasupra butoanelor de alegere a culorii
În QGIS 2.18 există posibilitatea deplasării rotiței mouse-ului deasupra oricărui buton glisant din dialogul de alegere a culorii, pentru a realiza incrementarea valorii. Această facilitate este indicată pentru modificări ale componentelor de culoare.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

Această funcționalitate a fost finanțată de [Nyall Dawson (North Road)](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: S-au adăugat scheme de culoare particularizate la meniul butonului de culoare
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Simbologie
### Funcționalitate: De acum, selectorul de culoare este încorporat în panoul de configurare a stilurilor straturilor
În QGIS 2.18, dacă efectuați un clic pe un buton de culoare din interiorul panoului cu stilurile stratului, atunci dialogul de alegere a culorii se va deschide în interiorul panoului, și nu într-o fereastră de dialog separată. Acest lucru permite modificarea interactivă a culorilor, cu previzualizarea imediată a rezultatului.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Etichetare
### Funcționalitate: Lista de substituție acceptă etichetarea
S-a adăugat capacitatea de a specifica o listă cu substituții de text, care vor fi aplicate etichetelor. De exemplu, la abrevierea tipurilor de străzi.

Utilizatorii pot exporta și importa liste de substituții pentru a ușura reutilizarea și partajarea.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Algoritm îmbunătățit de plasare pe linie a etichetei
Modul de etichetare paralelă a straturilor de tip linie a fost mult îmbunătățit, cu un nou algoritm care să evite plasarea etichetelor peste părțile zimțate ale entităților.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Andreas Neumann

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Etichetarea poligoanelor se face folosind etichete de-a lungul perimetrului
S-a adăugat un nou mod de etichetare a poligoanelor, al căror perimetru este etichetat cu ajutorul etichetării curbate.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Randare
### Funcționalitate: Previzualizarea plăcuțelor raster (WMTS și straturi XYZ)
În versiunile anterioare ale QGIS, utilizatorii trebuiau să aștepte până când descărcarea tuturor plăcuțelor unui strat se încheia, pentru a vedea harta rezultată. De acum, acest lucru a fost remediat, plăcuțele apărând pe canevas imediat ce au fost descărcate, experiența utilizatorului îmbunătățindu-se prin reducerea timpului până la afișare. Mai mult decât atât, plăcuțele descărcate anterior, cu rezoluții mai mici sau mai mari, pot fi utilizate de către funcția de previzualizare, în zonele în care  plăcuțele cu rezoluția corectă nu au fost descărcate încă.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

Această funcționalitate a fost finanțată de [Land Information New Zealand](http://www.linz.govt.nz/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Funcționalitate: Randarea rasterelor poate fi anulată (straturi WMS, WMTS, WCS și XYZ)
Această funcționalitate îmbunătățește experiența utilizatorului, atunci când se lucrează cu straturi raster care provin de la servere aflate la distanță. Anterior, trebuia să se aștepte descărcarea completă, pentru a putea mări sau deplasa iarăși harta, pentru că interfața cu utilizatorul rămânea, între timp, înghețată. De acum, acest lucru s-a remediat, randarea straturilor raster putând fi anulată în orice moment.

Această funcționalitate a fost finanțată de [Land Information New Zealand](http://www.linz.govt.nz/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Gestiunea Datelor
### Funcționalitate: S-a adăugat un fanion numai pentru entitățile selectate
Plugin-ul de editare offline este un plugin implicit din QGIS, care vă permite să lucrați offline cu un set de date aflat la distanță (ex.: dintr-o bază de date), să îl editați în teren, apoi să îl resincronizați la revenirea în birou. Acest lucru extinde offline posibilitățile de editare asupra subseturilor de straturi mari.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de DB Fahrwegdienste GmbH

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Formulare și Controale grafice
### Funcționalitate: Este permis controlul etichetelor pentru controale grafice de editare
Este permisă manevrarea etichetelor pentru controalele grafice de editare dintr-o formă. În interfața de proiectare drag and drop, un dublu clic pe un element va permite controlul în cazul în care eticheta ar trebui să afișată în mod individual, pentru fiecare element.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Cantonul Zug, GIS-Fachstelle](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funcționalitate: Vizibilitate condițională pentru file și pentru grupuri de casete
S-a adăugat o nouă opțiune de configurare pentru afișarea condiționată, sau pentru a ascunde filele și grupul de casete din interfața de proiectare drag and drop.

Configurarea se face printr-un dublu clic pe arborele din interfața de configurare a câmpurilor.

Se poate introduce o expresie pentru a controla vizibilitatea. Expresia va fi re-evaluată la fiecare schimbare a valorilor formei, iar fila și grupul de casete se afișează/ascunde în mod corespunzător.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funcționalitate: Valori implicite ale câmpurilor, pe partea de client
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de DB Fahrwegdienste GmbH

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Compozitorul de Hărți
### Funcționalitate: Săgeată pentru Nordul Adevărat
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Procesare
### Funcționalitate: Algoritmul punctului de pe o suprafață
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Algoritmul de dizolvare din Processing acceptă câmpuri multiple
Algoritmul de dizolvare acceptă, de acum, valorile din mai multe câmpuri. În versiunile de QGIS anterioare, o dizolvare putea grupa entitățile după valoarea dintr-un singur câmp.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: S-au optimizat calculele algoritmului de decupare
Algoritmul de procesare clip a fost optimizat pentru scenarii de utilizare comune, având ca rezultat creșterea dramatică a vitezei pentru operațiile de tăiere. De exemplu:

**Decuparea un strat cu drumuri, cu 1 milion de linii, în funcție de 2 poligoane**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**Decuparea unui strat de tip punct, cu 5 milioane de adrese, în funcție de 2 poligoane**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Algoritm pentru casetele de încadrare
Acest nou algoritm calculează caseta de încadrare (anvelopa) pentru fiecare element prezent în stratul de intrare.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Algoritm de îmbinare a liniilor conectate
Acest algoritm îmbină toate părțile conectate ale geometriilor MultiLineString în geometrii simple LineString. În cazul în care unele părți ale geometriilor MultiLineString de intrare nu sunt conectate, geometria rezultantă va consta într-un MultiLineString, care conține toate liniile care au putut fi îmbinate plus părțile de linie neconectate.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Algoritmul de delimitare a geometriei
Acest nou algoritm returnează limita combinatorie închisă a geometriilor de intrare (adică limita topologică a geometriei). De exemplu, limita unei geometrii poligonale va consta în șiruri de linii pentru fiecare inel din poligon, iar o geometrie liniară va avea o limită care constă din punctele de început și de sfârșit ale liniei. Acest algoritm este valabil numai pentru straturile de tip poligonal sau liniar.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Furnizorii de Date
### Funcționalitate: Suport nativ pentru plăcuțele straturilor XYZ 
Plăcuțele rasterelor în format XYZ sunt de acum acceptate de furnizorii de date WMS, care permite utilizatorilor să afișeze hărți din alte surse, fără a mai necesita plugin-uri terțe, cum ar fi QuickMapServices sau OpenLayers.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

Această funcționalitate a fost finanțată de [Lutra Consulting](http://www.lutraconsulting.co.uk/)

Această funcționalitate a fost dezvoltată de [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Server
### Funcționalitate: Posibilitate de fragmentare a informațiilor geometrice obținute de la server despre entități
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de Andreas Neumann

Această funcționalitate a fost dezvoltată de [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Plugin-urile
### Funcționalitate: DB Manager: S-a adăugat capacitatea de actualizare a Stratului SQL
With this feature the user can update the layer datasource if it\'s based on an SQL request.

Această funcționalitate a fost finanțată de [Ifremer](http://wwz.ifremer.fr)

Această funcționalitate a fost dezvoltată de [3Liz](http://3liz.com)
## Programabilitate
### Funcționalitate: Funcția de referențiere liniară GEOS este expusă la QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

Această funcționalitate a fost finanțată de [North Road](http://north-road.com)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Funcționalitate: Noi clase PyQGIS în 2.18
### Noi clase de baze
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Noi clase GUI, Controale grafice reutilizabile
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Funcționalitate: Noi funcții pentru expresii
QGIS 2.18 adaugă mai multe funcții noi pentru expresii, inclusiv funcții de interpolare a unghiului/distanței.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Această funcționalitate a fost finanțată de Andreas Neumann

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
