---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: projekt
sidebar: true
title: A QGIS 2.18 változásnaplója
type: visual-changelog

---
{{<content-start >}}
# A QGIS 2.18 változásnaplója{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Release date: 2016-10-21

Ez az utolsó kiadás a 2.x sorozatban. Az aktuális hosszú távú kiadás (LTR) a 2.14.x verzió marad. Ez a kiadás járulékos fejlesztéseket  tartalmaz az előző kiadáshoz. Most a tevékenységek többsége a QGIS 3.0 verzió  kidolgozására fókuszál, melynek kiadását 2017 első negyedév végére tervezzük.

**Köszönet**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

A QGIS szabad szoftver és semmi sem kötelezi arra, hogy fizessen használatáért. Valójában a QGIS használatára bátorítjuk az embereket, legyenek bárhol a világon, pénzügyi és társadalmi helyzettől függetlenül. Úgy hisszük azzal, hogy térbeli  döntéstámogatási eszközöket adunk az emberek kezébe, annak jobb társadalom építő ereje van az egész emberiségre nézve.

{{<table-of-contents >}}
## QGIS 2.18.0 verzió szponzorai
Évente kapunk támogatásokat több szervezettől is, akik méltányolják az elvégzett munkánkat és szeretnék elősegíteni a projekt fejlesztési folyamatát. A szponzorok az alábbi listában vannak, akiknek megköszönjük támogatást!

{{<fund type="changelog" relativeImgPath=true >}}
## Általános
### Funkció: Automatikus linkek az azonosítás eredményében
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Funkció: Egérgörgő a szín párbeszédablak csúszkák felett
A QGIS 2.18 verzióban már lehet az egérgörgőt használni a színkiválasztó párbeszédablakának csúszkáján az értékek kis léptékben történő változtatására. Könnyed használat a színalkotók részletes állítása közben.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Egyéni színséma hozzáadása a szín gomb legördülő menüjéhez
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Jelrendszer
### Funkció: A szín választót beágyaztuk a réteg stílus panelbe
Amikor a QGIS 2.18 verzióban a szín gombra kattint a réteg stílus panelen belül, akkor a stílus panelen belül fog megnyílni a szín kiválasztó párbeszédablak, ahelyett hogy külön ablakban jelenítődne meg. Ez lehetővé teszi a színek interaktív módosítását az eredmények közvetlen előnézetével.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Címkézés
### Funkció: Helyettesítő lista kezelés a címkézéshez
Lehetőség hozzáadása egy felirat szöveg listájának meghatározásához, hogy melyik címke szöveget alkalmazza. Pl., utcatípusok rövidítése.

A felhasználó importálhatja és exportálhatja a csereérték listákat, hogy könnyen újrahasználja vagy megoszthassa.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Továbbfejlesztett vonal címke elhelyezési algoritmus
A vonalrétegek párhuzamos címkézési módja jelentősen javult az új algoritmussal, ami elkerüli a címkék elhelyezését az elem geometria egyenetlen részein.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Felület címkézése íves címkék használatával a kerület mentén
Ez egy új módszert ad a felületek címkézéséhez, ahol a felület kerületén lesz címkézve íves címkék használatával.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Megjelenítés
### Funkció: Raszter csempék előnézete (WMTS és XYZ rétegek)
Az előző QGIS verzióknál, a felhasználónak meg kellett várnia, amíg a réteg összes csempéje teljesen letöltődött, hogy megnézhesse a térképeredményt. Ez most javítva lett és csempék azonnal megjelenítődnek a térképvásznon, amint letöltődtek. A felhasználói élmény javítva lett, mert nagyban csökkentve lett az az idő amíg bármi megjelenik. Továbbá az előzőleg letöltött kisebb vagy nagyobb felbontású csempék fel lesznek használva előnézet funkcióként, ott ahol a megfelelő felbontású csempék még nem töltődtek le.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Funkció: Megszakítható raszter megjelenítés (WMS, WMTS, WCS és XYZ rétegek)
Ez a lehetőség javítja a felhasználói élményt, amikor távoli kiszolgálón lévő raszter rétegekkel dolgozik. Előzőleg meg kellett várni, amíg teljesen letöltődnek, hogy a térképet nagyítani vagy mozgatni lehessen, mert a felhasználói felület ez idő alatt le volt fagyva. Ez most javítva lett a raszter rétegek megjelenítésének megszakításának lehetőségével.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Adatkezelés
### Funkció: Jel hozzáadása, csak a kiválasztott elemek másolásához
Az offline szerkesztés modul egy alapértelmezett modul, ami be van építve a QGIS-be lehetővé teszi offline a távoli adathalmazok (pl. adatbázisból) mezőinek szerkesztését és újraszinkronizálja, amikor visszatér a munkához. Ez kiterjeszti az offline szerkesztési lehetőségeket, hogy csak a nagy rétegek részhalmazaival dolgozzon.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Űrlapok és Vezérlők
### Funkció: Címkék kezelése a különböző szerkesztő vezérlőkön
Lehetővé teszi a címkék szabályozását  a különböző szerkesztő kezelőkre egy űrlapban. A húzd és ejtsd tervezőben a dupla kattintás az elemen lehetővé teszi a szabályozást, ha a címkét külön kell megjeleníteni minden egyes elemre.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funkció: Feltételes láthatóság a fülekre és csoport dobozokra
Az új konfigurációs opció hozzáadásával, feltételesen mutatható vagy elrejthetőek a fülek és csoportdobozok a húzd és ejtsd tervező űrlapokban.

A konfiguráció beállítható egy dupla kattintással a mező konfigurációs felületén a tervező fában.

Egy kifejezés adható meg a láthatóság szabályozásához. A kifejezés minden alkalommal újra kiértékelődik, amikor az érték megváltozik az űrlapban. A fül vagy csoportdoboz eszerint jelenik meg vagy tűnik el.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funkció: Ügyfél oldali alapértelmezett mező értékek
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Térkép összeállítás
### Funkció: Valós észak nyilak
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Feldolgozás
### Funkció: Pont a felületen algoritmus
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: A feldolgozás összevonás algoritmusa több mezőt is elfogad
Az összevonás algoritmus most már lehetővé teszi az összevonást több mezőérték alapján. Az előző QGIS verziókban az összevonás csak egy mezőérték alapján tudott csoportosítani.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: A feldolgozás vágás algoritmusa optimalizálva
A feldolgozás, vágás algoritmusa jelentősen optimalizálva lett az egyszerű esetek használatára, ami drámai sebességnövekedést eredményezett a vágás műveleteknél. Például:

**Egy utak réteg 1 millió vonalának vágása 2 felülettel**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**5 millió címpont vágása 2 felülettel**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Befoglaló téglalap algoritmus
Az új algoritmus kiszámítja a befoglaló téglalapot (boríték) az input réteg összes eleméből.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Kapcsolódó vonalak összevonása algoritmus
Ez az algoritmus összevonja a multivonal geometria kapcsolódó részeit egy vonal geometriába. Ha az input multivonal bármely része nem kapcsolódik össze, akkor az eredmény geometria egy multivonal lesz, ami tartalmazza az összevont és a nem kapcsolódó vonalrészeket.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Geometria határvonal algoritmus
Az új algoritmus az input geometria kombinatorikus határainak lezárását adja vissza (azaz a geometria topológiai határát). Például egy felület határa lesz a felületen belül található minden egyes gyűrű vonala és egy vonal geometriának a határa lesz a kezdő és a végpontja. Ez az algoritmus csak felület és vonal rétegekre alkalmazható.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Adatszolgáltatók
### Funkció: XYZ csempe rétegek natív támogatása
Az XYZ formátumú raszter csempék most már natívan támogatottak a WMS adatszolgáltatón belül, ami lehetővé teszi egy másik forrásból származó alaptérképek megjelenítését, egy harmadik féltől származó modul pl. QuickMapServices vagy OpenLayers használata nélkül.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Szerver
### Lehetőség: Az elem geometriájának szegmenseiről szóló információ lehetősége a kiszolgálón
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Ezt a funkciót támogatta: Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Bővítmények
### Funkció: DB kezelő: Hozzáadva az SQL rétegek frissítésének lehetősége
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programozhatóság
### Funkció: A GEOS lineáris referencia függvény kitéve a QgsGeometry-hez
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Funkció: Új PyQGIS osztályok a 2.18-ban
### Új belső osztályok
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Új GUI osztályok, Újrahasznosítható vezérlők
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Funkció: Új függvények a kifejezésekhez
A QGIS 2.18 verzióhoz számos új függvény kifejezés lett hozzáadva, többek között a szög/távolság interpoláció függvény.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Ezt a funkciót támogatta: Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
