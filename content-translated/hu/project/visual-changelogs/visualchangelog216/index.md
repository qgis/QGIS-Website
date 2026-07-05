---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: projekt
sidebar: true
title: A QGIS 2.16 változásnaplója
type: visual-changelog

---
{{<content-start >}}
# A QGIS 2.16 változásnaplója{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Release date: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Ez nem egy hosszútávú kiadás**

Ez a kiadás nem egy hosszútávú (LTR) kiadás. Azok a felhasználók, akik egy évig nem változó, de hibajavításokat kapó QGIS verziót szeretnének, azokat az aktuális 2.14 LTR kiadás használatára biztatjuk (mely a QGIS 2.16 kiadással vált a hivatalos LTR változattá).

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Köszönet**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## QGIS 2.16.0 szponzorai
Évente kapunk támogatásokat több szervezettől is, akik méltányolják az elvégzett munkánkat és szeretnék elősegíteni a projekt fejlesztési folyamatát. A szponzorok az alábbi listában vannak, akiknek megköszönjük támogatást!

{{<fund type="changelog" >}}
## Általános
### Funkció: elemek másolása GeoJSON formátumban
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: térbeli könyvjelzők tárolása a projekt fájlokban
Ha térbeli könyvjelzőt hoz létre, most választhat, hogy a könyvjelzőt az aktív projekt fájljába tárolja. Görgesse a könyvjelzők panelt, hogy megtalálja a jelölőnégyzetet, mely engedélyezi ezt  lehetőséget.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### Funkció: GNSS GNRMC üzenetek támogatása
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Ezt a funkciót Ondřej Fibich fejlesztette
### Funkció: GeoJSON elemek közvetlen beillesztése QGIS-be
A QGIS vágólap kezelő most újabb szöveg formátumokat tud értelmezni, beleértve a GeoJSON elem gyűjtemények natív támogatását. Ez lehetővé teszi, hogy közvetlenül másoljon és beillesszen GeoJSON szövegeket  a QGIS-be és automatikusan QGIS elemekké és geometriákká konvertálja.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Térképtipp fejlesztések
- A térkép tippek láthatóságát megőrizzük a munkamenet folyamán
- A térkép tippek most már HTML tartalmat, képeket, videókat és URL linkeket jeleníthetnek meg 

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Funkció: Asztali MIME-típus ikonok a QGIS fájl típusokra
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - QGIS Projekt fájl
- \*.qml - Réteg beállítások fájl
- \*.qlr - Réteg definíciók fájl
- \*.qpt - Lap összeállítás sablon fájl

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## Felhasználói felület
### Funkció: Térképvászon nagyító
Egy nagyító eszköz lett hozzáadva a QGIS-hez, ami lehetővé teszi a térkép nagyítását egy megadott méretarányon. Ez lehetővé teszi a térkép nagyítását a méretarány megváltoztatása nélkül, könnyebbé téve a címke és szimbólum pozíciók finombeállítását. Továbbá, az alapértelmezett nagyítási értéket meg lehet adni a beállításokban, ami nagyon hasznos a nagy-felbontású kijelzőkön!

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funkció: Térkép nagyítás fejlesztések
A QGIS 2.16 fejlesztést hoz a térképvászon nagyítási, kicsinyítési módjaiban.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Újratervezett interaktív színátmenet szerkesztő
A színátmenet skála szerkesztő át lett dolgozva interaktív szabályozókkal a színátmenetek könnyebb beállításához. A párbeszédablak most más tartalmaz egy interaktív sávot a színátmenet pontjainak módosításához HSV vagy RGB szín értékek segítségével. Az új szerkesztő funkciói:
- húzás a színpontok mozgatásához
- dupla kattintás egy új színpont hozzáadásához
- delete billentyű megnyomásával lehet törölni a kiválasztott pontot
- a nyíl billentyűkkel lehet mozgatni a kiválasztott színpontot, és a shift billentyű nyomva tartásával lehet nagyobb léptékben mozgatni a pontokat
- egy szín húzásával és ejtésével a vezérlőbe lehet hozzáadni egy új színpontot

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Alapértelmezett nézet választása az attribútum párbeszédblakra
Az előző QGIS verziókban az attribútum párbeszédablak mindig tábla nézetben nyílt meg. Most, meg van a lehetőség az alapértelmezett párbeszédablak kiválasztására, ami lehet tábla, űrlap nézet vagy beállítható, hogy emlékezzen az utolsó használt nézetre.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Fejlesztések a felbukkanó naptárhoz
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Továbbfejlesztett szín kiválasztó
A színgomb legördülő menüje most egy szín kereket mutat, lehetővé téve a színek nagyon gyors beállítását.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### Funkció: Cella tartalom másolás az attribútum táblából
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funkció: Javított HiDPI támogatás
HiDPI  képernyő használók egy javított felhasználói felületet kaptak, mivel az ikonok frissített SVG formátumba kerültek. A QGIS 2.16 verzió összes eszköztára most már HiDPI-kompatibilis.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: Javított viselkedés a térkép szelekció eszközhöz
A térkép alapú szelekció eszköz viselkedése finomítva lett, a következő változásokkal:

A kattintás-és-húzás szelekcióra:
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Az egy kattintásos szelekciókra:
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Ez a változás a térképi viselkedés mellett más tervező alkalmazásnál így a lap összeállítóban is használható.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Dokumentáció frissítések
### Funkció: QGIS 2.14 dokumentáció
Most már van automatikus mód a bejegyzés készítéshez minden egyes új QGIS funkcióhoz a dokumentum tárolóban, biztosak vagyunk, hogy most már az összes új funkció szerepel a dokumentációban.

A dokumentációs csapat keményen dolgozott a QGIS három kiadásán: 2.10, 2.12., 2.14, így az aktuális QGIS hosszútávú kiadás dokumentációja is naprakész. Ez 180 új funkció dokumentálást jelent 4 hónap alatt.

Hogyha gondolja, van néhány hiányzó funkció a dokumentációban, nyugodtan adjon hozzá egy új bejegyzést, írjon hozzá egy rövid vagy jobb leíró szöveget és tegye közzé.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

A dokumentációs csapat az elkövetkező hónapokban keményen fog dolgozni az aktuális kiadás (2.16) dokumentációján.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Nézze meg a 2.10, 2.12 és 2.14 számú mérföldköveket, hogy lássa az összes dokumentációs munkát, ezeket itt találja meg:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

Ezt a funkciót fejlesztette: Larry Shaffer
## Jelrendszer
### Funkció: Nyíl szimbólum réteg
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

Az íves módban, a vonal réteg csomópontjai lesznek felhasználva ellenőrző pontként a szimbólum réteg körívéhez. A nyilak háttere kitölthető bármilyen kitöltés típussal, amit a QGIS támogat. A beállítás lehetővé teszi a nyíl típusának (egyvégű vagy kétvégű, egyszerű vagy felezett) kiválasztását, szélességének (amit lehet variálni) és hegy méretének állítását.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Új megközelíthetőség és gyengén-látók szimbólumok
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: új egyszerű szimbólumok
- fél, harmad és negyed kör
- fél háromszög jelek
- kitöltött kereszt és hatszög jelek
- rombusz ellipszis jel

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Továbbra is lehet szelektálni a rétegen a térképvásznon belül, és a kiválasztott elemek egy alapértelmezett szimbólummal lesznek megjelenítve. A szerkesztés alatt álló elemek szintén mutatva lesznek.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Több beállítás a centrális pont kitöltés megjelenítéshez
A szabályozáshoz egy opció lett hozzáadva, amivel a megjelenítendő jelet be lehet állítani az összes részre, vagy egy több elemes geometria egy részére.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: Körvonal beállítás a betűkészlet jel szimbólumokra
Most már lehet körvonaluk a betűkészlet jel szimbólumoknak, ami növeli a láthatóságát ezeknek a szimbólumoknak egy körvonal övezet szín hozzáadásával. Engedélyezett Emoji betűkészlet karakterek esetén jól kinéző jeleket kaphatunk, ha vékony körvonalat használ.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: Körvonal kapcsolódás stílus állítása egyszerű, ellipszis és betűkészlet jelekre
A felhasználó most már meg tudja változtatni a körvonal kapcsolódási stílusát a egyszerű, ellipszis, és betűkészlet jeleknél a jelrendszerük finombeállításához.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: Új térkép eszköz a pont szimbólum eltolás interaktív beállítására
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Stílus dokk
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Címkézés
### Funkció: A címkézés térképi eszköz most már a szabály-alapú címkézéssel is használható
Az előző QGIS verziókban, amikor szabály-bázisú címkézés lett beállítva, akkor nem lehetett használni a címkézés térképi eszközt a címke elhelyezésének és forgatásának interaktív beállítására. Ez most már támogatva van.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Ezt a funkciót fejlesztette: Martin Dobias
## Diagramok
### Funkció: Jelmagyarázat elemek a diagram méretre
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Egység kiválasztása a körvonal vastagsághoz
A körvonal szélesség egységének kiválasztása most már elérhető. Ez lehetővé teszi egy térképi egységben méretezett diagramnak, hogy növekedjen és zsugorodjon térkép méretarány alapján, miközben megtartja a rögzített milliméter körvonal vastagságát.

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Funkció: A diagramok címkeként viselkednek és beállíthatóak az eszköztárban.
Eredetileg volt egy eszköztár a címkékre, ami lehetővé tette:
- az aktuális réteg címkéinek címkézési opcióinak beállítását
- a rögzített címkék kiemelését. A kiemelés zöld a szerkesztett rétegen, kék minden más esetben.
- a címkék rögzítését vagy felengedését
- a címkék mozgatását, mutatását és elrejtését

Ezzel az új funkcióval, egy új eszköz érhető el a címkézés eszköztárban lehetővé téve az aktuális réteg diagramtulajdonságainak beállítását. Továbbá minden egyes fent említett eszköz teljes mértékben használható a diagramokkal is.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Megjelenítés
### Funkció: Új beállítások a röptében egyszerűsítéshez
A felhasználó ki tudja választani a használandó algoritmust amikor a helyi-oldali egyszerűsítést futtat a geometriák gyorsabb megjelenítésére. A QGIS most már három algoritmust szolgáltat:
- Távolság (alapértelmezett algoritmus, és az egyetlen elérhető lehetőség az előző QGIS kiadásokban)
- SnapToGrid
- Visvalingam

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Funkció: Kvantilis alapú osztályozás a raszter rétegekre
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Ezt a funkciót Piers Titus van der Torren fejlesztette
### Funkció: Domborzat árnyékolás azonnali megjelenítése
A QGIS 2.16 egy új raszter megjelenítővel rendelkezik, mely dinamikusan hozza létre a domborzat árnyékolást a digitális magasság modellből.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Ezt a funkciót  Asger Skovbo Petersen és Nathan Woodrow fejlesztette
## Digitalizálás
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Törtvonal geometria bővítése az elem módosítás eszközzel
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Ezt a funkciót fejlesztette: Martin Dobias
### Funkció: Szegmentáció tolerancia
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Ezt a funkciót Marco Hugentobler fejlesztette
## Adatkezelés
### Funkció: Új attribútum tábla konfiguráció beállítások
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Lehetővé teszi egy új oszlop hozzáadását az attribútum táblához, ami tartalmazza a kiválasztott elemhez tartozó művelet indító gombokat. 
- Oszlopok elrejthetők az attribútumtáblából (jobb gomb kattintással a mezőnévre a fejlécben )
- QGIS megjegyzi az átméretezett oszlopok szélességét

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funkció: Több oszlop az attribútum űrlapban
A húzd és ejtsd tervező használatakor, a felhasználó meg tudja határozni, hogy mennyi mezőoszlopot kell kitölteni.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Győződjön meg, hogy a húzd és ejtsd tervező űrlapmódot használja
- Kattintson duplán a tárolók csoportosításához, mint fül vagy csoport
- egy kis párbeszédablak fog megjelenni, ahol beállítható az oszlopok száma

Első oszlop, második oszlop, n-ik oszlop, következő sor stb. lesz a sorrend

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Funkció: Az exportálni kívánt attribútumok szabályozása egy vektor réteg mentése során
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

Ezt a funkciót fejlesztette Jürgen Fischer, Even Rouault
### Funkció: Űrlap nézet: az oszlop oldal most már rendezhető
A QGIS attribútum táblájának űrlap módjában van egy oszlop oldal, ahol közvetlenül lehet egy meghatározott elemre ugrani. Eddig a kiadásig ez az oldal nézet volt rendezhető. A rendezéshez át kellett ugrani a tábla módba, majd vissza az űrlap módba. Most már közvetlenül lehet az elemeket rendezni az elem attribútum előnézettel az oldalsávon, kiválasztva egy rendezés függvényt az oszlop oldal felett lévő kifejezések legördülő gombján.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Funkció: Kapcsolat hivatkozás vezérlő: gyorsbillentyű az új értékek hozzáadására
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Funkció: DXF export fejlesztések
Támogatva lett a szabály bázisú címkézés, az elforgatott szimbólum és az output 3D geometria is.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Ezt a funkciót Jürgen Fischer fejlesztette
### Funkció: Felső szintű vezérlők a húzd és ejtsd tervezőben
Most már lehetséges a vezérlők közvetlen áthelyezése az űrlapon a húzd és ejtsd tervezővel. A húzd és ejtsd tervező űrlap következésképpen létezhet fül nélkül is.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Funkció: Űrlap alapú kiválasztás és szűrés
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

Új gombok jelennek meg az űrlap alján az egyező elemek kiválasztására (hozzáadás a szelekcióhoz/eltávolítás a szelekcióból/kiválasztás az aktuális szelekcióban lehetőséggel) vagy az elemek szűrésére a táblában (lehetőségekkel, mint az elemek hozzáadása az aktuális szűrőhöz, vagy további korlátozás hozzáadása az aktuális szűrőhöz).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

A funkciót támogatta: SIGE, City of Uster, Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: GeoPackage rétegek létrehozása
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette: Even Rouault
### Funkció: Korlátozások a vezérlőkön
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funkció: Attribútumok szerkesztése több elemre párhuzamosan 
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

Ebben a módban, az attribútum érték változások alkalmazva lesznek az összes kiválasztott elemre. Az új vezérlők megjelennek minden egyes szerkesztő vezérlő mellett, lehetővé téve az aktuális csoportos szerkesztés állapotmegjelenítését és a változtatások visszaállítását mezőnkénti alapon.

A változások egyszeri szerkesztési parancsként működnek, így a mégse gomb egyszeri megnyomásával vissza lehet állítani az attribútum változásokat az összes kiválasztott elemre.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Réteg jelmagyarázat
### Feature: New option to zoom to a layer\'s visible scale range
A rétegek látható méret tartományának beállítására, az opció kiválasztásával automatikusan be lesz állítva a méretarány a legközelebbi méretre, ahol a réteg még látható. Továbbá, a felület finomítva lett, úgy, hogy azok a rétegek, melyek kívül esnek a mérettartományon és rejtve maradnak, szürkével lesznek megjelenítve a rétegfában.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Térkép összeállítás
### Funkció: Új eszköz a felületek és törtvonalak rajzolására
A lap összeállításban most már további két csomópont alapú alakzat érhető el. Ezeket használva, csak néhány kattintással hozzá lehet adni egy felületet vagy törtvonalakat az összeállításhoz.

Új eszköz is lett hozzáadva, ami lehetővé teszi a csomópontok szerkesztését (azaz csomópontok mozgatása vagy eltávolítása) és új csomópontok is hozzáadhatóak a már létező alakzathoz. Az összeállításban lévő felület vagy törtvonal elem testreszabható, az összes szimbólumstílussal, ami elérhető a vonal és felület rétegekhez!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funkció: Relatív hivatkozások az összeállítás címkékben
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Funkció: Atlasz elemek beágyazva az összeállítás HTML forrásba, GeoJSON-ként
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### Funkció: Paraméterezett SVG támogatás az összeállítás SVG képeire
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: HTML könnyebb használata a címkékben
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Georeferált eredmények (pl. PDF) a lap összeállításból
A QGIS 2.16 verzióban a térkép összeállító automatikusan georeferálja az eredményeket (amikor az eredmény formátum lehetővé teszi, pl. TIF és PDF).

A világ fájl létrehozásához meglévő beállítás el lett különítve a térkép kiválasztásból georeferálásra. Ez az új viselkedés mindig georeferálja az eredményeket, és csak akkor hoz létre külön világ fájlt, ha az a beállítás engedélyezve van.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: A térkép összeállítások most már automatikusan frissülnek a készletekkel
Amikor egy térkép összeállítás be van állítva a stílus készlet követésére, automatikusan frissülni fog, amikor a stílus megváltozik.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Ezt a funkciót fejlesztette: Martin Dobias
## Elemző eszközök
### Funkció: Névvel bíró paraméterek a kifejezésekben
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

A névvel bíró paraméterek segítségével tisztázható, hogy mit jelentenek a kifejezés függvény utalásai, ami hasznos, ha egy kifejezést egy később időpontban próbál meg értelmezni!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Több távolság mértékegység
A távolság mértékegység választási lehetőségek kibővültek új elemekkel, mint a kilométer, yard, és a mérföld. Ezeket használva megelőzhető, hogy a távolságokat manuális kelljen átalakítani (pl. lábból mérföldbe).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Változások a kifejezésekhez
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Funkció: Statisztika szöveg és dátum mezőkre
A statisztikai összegzés dokk most már halmazosított statisztikákat számít a szöveges és dátum mezőkre.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: A görbepont sugarának megjelenítése az azonosítás eszközben
Amikor rákattint egy íves vonalra az azonosítás eszközzel, akkor a QGIS automatikusan megjeleníti a sugárt az azonosítási eredményekben.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Ezt a funkciót Marco Hugentobler fejlesztette
### Funkció: Halmazok támogatása a kifejezésekre
A QGIS 2.16 támogatást ad számos halmaz típusra a kifejezés kiértékelőhöz. Ezeket tartalmazza:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

Az összes esetben a számítások gyorsítótárazva vannak a kifejezés tartalmon belül, ezért ezeket csak egyszer szükséges kiszámítani a kifejezés kiértékelés minden egyes beállítására.

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Az fTools modult a Feldolgozás algoritmusok helyettesítik
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Ezt a funkciót fejlesztette Alex Bruy
## Feldolgozás
### Funkció: Pont helyzet beállítása a vászonra történt kattintással
A pont helyzetre váró Feldolgozás paraméterek most már beállíthatóak a térképvászon egy pontjára történt kattintással. Előzőleg, a koordinátákat kézzel kellett megadni.

Ezt a funkciót fejlesztette Alex Bruy
### Funkció: Támogatás a kifejezésekre és változókra
Az inputok és outputok az algoritmus párbeszédablakokban most már támogatják a QGIS kifejezéseket és változókat.

Ezt a funkciót fejlesztette: Victor Olaya
### Funkció: Előre konfigurált algoritmusok
Az előre konfigurált paraméterekkel rendelkező algoritmusok most már hozzáadhatóak a Feldolgozás eszköztárhoz, mint egy gyorsbillentyűt a megadott műveletre.

Ezt a funkciót fejlesztette: Victor Olaya
### Funkció: Egy modul létrehozása szkript-alapú algoritmusokkal az eszköztárból
Előzőleg, egy QGIS modul létrehozásának az egyetlen módja - ami új algoritmust adott a Feldolgozáshoz - az algoritmusok kézi fejlesztése és új algoritmus szolgáltató létrehozása volt. Most az algoritmusok megírhatóak egyszerű Feldolgozás szkriptként, és az azokat tartalmazó modult közvetlenül létre lehet hozni a a Feldolgozás eszköztárból. Ez a modul ezután szabályos modulként jeleníthető meg, és kibővíti a Feldolgozást, amikor aktív.

Ezt a funkciót fejlesztette: Victor Olaya
### Funkció: Hitelesítés kezelő használata a PostGIS kapcsolt algoritmusokban
A PostGIS kapcsolt algoritmusok most már használják a QGIS hitelesítés kezelőjét a PostGIS adatbázisokra lekért hitelesítési adatokhoz.
- Abban az esetben, ha van egy hitelesítési eljárás beállítva a PostGIS kapcsolaton, a felhasználó meg lesz kérdezve a mester jelszaváért.
- Abban az esetben, ha nincs hitelesítési eljárás beállítva a kapcsolatra, akkor a hitelesítési adatok a hitelesítési adatok gyorsítótárából lesznek kivéve, ha itt nem találhatóak, akkor a felhasználótól megkérdezi és eltárolja azokat a hitelesítési adatok gyorsítótárába a későbbi használatra.

Ezzel, többé nem szükséges eltárolni egyértelmű jelszavakat a kapcsolat beállításokban a PostGIS kapcsolt algoritmusok használatához.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Funkció: Támogatás a geometria nélküli táblák írására
Az OutputVector algoritmus most már támogatja a geometria nélküli táblák írását.

Jelenleg ez csak a Mezők újrakonfigurálása algoritmusra van alkalmazva, de könnyedén kiterjeszthető más attribútumokhoz kapcsolódó algoritmusokhoz is.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Funkció: További GRASS algoritmusok a feldolgozásban
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

Néhány egység tesztet (főleg raszter és kép algoritmusra) is tartalmaz egyes algoritmusokra, ami a hibajelzést könnyebben kezelhetővé és feldolgozhatóvá teszi.

Fontos megjegyezni, hogy jelenleg a GRASS7 Feldolgozás algoritmusok csak Shapefile vektor rétegeket és GeoTiff rasztereket készítenek és használnak. Továbbá néhány GRASS7 raszter algoritmus (az összes algoritmus, ami színtáblát kezel) is korlátozva van, amelyek megkettőzik raszter rétegeket az ideiglenes könyvtárba. A forrás raszter méretétől függően lehetséges, hogy ezek kezelése további lemezterületet igényel.

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Adatszolgáltatók
### Funkció: Az OGR adathalmazok alapértelmezetten írásvédett módban lesznek megnyitva
Lehetővé teszi a Shape fájlok és a Tab fájlok egyidejű szerkesztését a QGIS & MapInfoban.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

Ezt a funkciót fejlesztette: Even Rouault
### Funkció: Fejlesztve lett a Postgres DOMAIN típus mezők kezelése
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: A vektor rétegek írásvédett módba tehetőek a projekt beállításokban
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Funkció: DB2 adatbázis támogatás
Ezt a funkciót fejlesztette: David Adler
### Funkció: Postgres megvalósított nézetek frissítése az adatbázis kezelőben
### Funkció: Látható az OGR FID attribútum
A QGIS az OGR FID-et elsődleges attribútumként jeleníti meg, ha ez jelentőségteljes, pl. GPKG és egyéb adatbázis alapú meghajtók esetén.

Ezt a funkciót fejlesztette: Even Rouault
### Funkció: ArcGIS Map és Feature REST szolgáltatások
A QGIS most már képes ArcGIS REST szolgáltatáshoz kapcsolódni.

Kapcsolódhat az ArcGIS Feature szolgáltatásokhoz (a WFS megfelelője az ESRI világban) és az ArcGIS Map szolgáltatásokhoz (a WMS megfelelője). A szolgáltató lehetővé teszi a térképek és vektor rétegek olvasását ezekről a szolgáltatásokból.

Ez a funkció nagyon kényelmes azoknak a felhasználóknak, akik szeretnének váltani egy ESRI GIS veremről anélkül, hogy elveszítenének valamit, amit már magáncélú vagy nyilvános térkép szolgáltatásokra építettek. Az ESRI által nyújtott nyilvános szolgáltatásokhoz is csatlakozhat.

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Funkció: Stílusok mentése MS SQL és Oracle adatbázisokba
Ezt a funkciót fejlesztette Jürgen Fischer és Christian Frugard
### Funkció: réteg mezők átnevezése 
A QGIS 2.16 verzióban átnevezhetőek a mezők a Postgres, Oracle, OGR és az ideiglenes rétegekben. Ezt a réteg tulajdonságok ablakban, a mező nevén dupla kattintással lehet megtenni.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funkció: Alapszintű támogatás az Oracle Munkaterület Kezelőre
Támogatás lett hozzáadva az Oracle Munkaterület Kezelőhöz, ha Oracle szolgáltatót használ.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
### Funkció: Nagy fejlesztések a WFS szolgáltatóhoz
A QGIS 2.16 verzió nagy mértékű javítást hozott a WFS szolgáltatóra, beleértve
- Verzió automatikus detektálása
- A letöltött elemek gyorsítótárazása a lemezen
- Letöltés a háttérben és progresszív megjelenítés
- WFS 1.1 és 2.0 támogatás
- WFS 2.0 GetFeature lapozás
- Szolgáltató tesztek hozzáadása
- Támogatás a WFS 2.0 csatlakozásokra
- URI paraméter sql-el SELECT / FROM / JOIN / WHERE / ORDER BY kikötésekkel
- DateTime mezők kezelése
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- További/vegyes geometria típusok támogatása (CurvePolygon, CompoundCurve)
- Több tolerancia a nem megfelelő WFS szerverek számára

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
A kifejezés a mezők alapértelmezett értékeinek generálására használható a Postgres adatbázisokon ahogyan aktuálisan megjelenik az elem űrlapon.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
A fő előnye ennek a fejlesztésnek, hogy most már közvetlenül létrehozhatóak és hivatkozhatóak a kapcsolt táblák rekordjai, mielőtt az adatokat elmentené, mert az elsődleges kulcs már megjelenítődik az elem mentése előtt.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## QGIS Szerver
### Funkció: Változásátvezetés támogatás a GetMap és a GetPrint-ben
A funkciót támogatta  Canton of Solothurn

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Funkció: Alapértelmezett dátum átalakítás szerverre
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Bővítmények
### Funkció: Frissített földgömb modul
- Frissítés OsgEarth 2.8-ra
- Átírva a QGIS Földgömb csempe meghajtó
- Átírva a szinkronizációs logika a 2D és 3D között
- Áttérés új geometriai magra
- Több háttérréteg támogatása
- A menük beágyazva a Földgömb ablakba
- Független rétegkijelölések a Földgömbre
- Mathias Kuhns mester tézis munkájának portja a QGIS 2.1/OsgEarth 2.4-ből

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Funkció: Földgömb: Objektumok kihúzása
Lehetővé teszi az objektumok kihúzását a 3. dimenzióba

Ez történhet rögzített értékkel, egy attribútummal vagy egy kifejezéssel.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Funkció: API: Lapok hozzáadása a vektor réteg tulajdonságokhoz
Lehetővé teszi további lapok hozzáadását a vektor réteg tulajdonságok párbeszédablakához.

Ez lehetővé teszi, hogy a modul által biztosított réteggel kapcsolatos beállításokat közvetlenül át lehessen helyezni, ahol azok egy jobb felhasználói élményhez biztosítanak.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Funkció: Földgömb: Vektor támogatás
Amikor rétegeket jelenít meg a földgömbön, megőrzi a vektoradatokat.

Ezt a funkciót támogatta: Master Thesis UZH

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Funkció: Földgömb: Függőleges túlzás a DTM-re
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## Programozhatóság
### Funkció: Beágyazott vezérlők a réteg fában
Ez lehetővé teszi a réteg definíciók beágyazását a réteg fába a különböző rétegekre a réteg tulajdonságok párbeszédablakában (az új Jelmagyarázat fülön). Az elképzelés az, hogy gyorsan hozzá lehessen férni néhány művelethez, ami gyakran használatba kerül a rétegekkel.

A megvalósítás az átlátszóság vezérlővel kezdődik, a jövőben több szabványos vezérlő is érkezni fog, pl. szűrés beállítások, kiválasztás, stílus és más dolgok. Az API lehetővé teszi a modulok számára a saját vezérlőik regisztrálását is, ami hasznos lehet számos domain specifikus modulra, hogy egyéni vezérlőket hozzanak létre az általuk kezelt rétegekhez.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Ezt a funkciót Martian Dobias fejlesztette
### Funkció: A modulok oldalakat adhatnak a vektor réteg tulajdonságokhoz
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Funkció: Új PyQGIS osztályok a 2.16 verzióban
### Új belső osztályok
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

### Új GUI osztályok
#### Újra használható vezérlők:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- színárnyalat kerék, szín minták, és egy szín mintavevő
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

#### Újra használható párbeszédablakok:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Fontos javítások
### Funkció: QGIS fizetett hibajavítás program
A fizetett hibajavítások egy másik fordulóját (a szponzoraink és a adományozóinknak köszönhetően!) is megtettük. Itt követheti azoknak a fejlesztőknek a munka összefoglalóit, akik részt vettek:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- Javítva lett az összeomlott projektív átalakítás a georeferálóban (#14551 - súlyos)
- Javítva lett az elemek kiválasztás sugárral hiba. (#14748 - súlyos)
- Javítva lett a felületek helytelen terület számítása (#14675 - súlyos, habár nagyon ritkán fordult elő. Egység tesztek lettek hozzáadva, hogy felfedezzék ezt a kritikus esetet)
- Javítva lett a dokk vezérlő elrendezés (#15011 - súlyos)
- Javítva lett az összeomlás a nyíl szimbólum rétegekben (nem jelentett)
- Javítva lett az összeomlás, amikor érvénytelen kapcsolódás lett létrehozva (nem jelentett)
- Javítva lett, hogy a paraméterezhető SVG-k nem jelentek meg az összeállítás nyíl elemeknél (#14997 - magas)
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Mindig használja a karakterlánc összehasonlítást a kifejezésekben a karakterlánc mezőkre. (#13204 - magas)
- Javítva lett, hogy a home könyvtár lett hozzáadva az svg-k és sablonok alapértelmezett útvonalaként (#14662, #14652, #14883 - magas)
- Javítva lett az összeomlás, amikor invertált poligonok voltak használva a hőtérkép megjelenítőben (#14968 - magas)
- Raszter jelrendszer értékek mentése teljes pontosságal (#14950 - normál)
- A műveletek nem lettek engedélyezve, amikor a réteg alapértelmezett stílussal töltődött be (#13910 - normál)
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- Javítva lett, hogy nem lehetett kikapcsolni a testreszabási vezérlőt (#9732 - normál)
- Javítva lett a nyíl szimbólumréteg hegy szélesség/magasság tükrözése  (#15002 - normál)
- Javítva lett, hogy az összekapcsolások nem lettek újra létrehozva, amikor a projekt rossz rétegekkel töltődött be (#10500 - normál)
- Az összekapcsolási gyorsítótárat érvényteleníése, amikor a réteg módosult (#11140 - normál)
- Helyesen támogatja az összekapcsolásokat virtuális mezők használata esetén (#14820 - normál)
- Javítva lett, hogy bizonyos körülmények között a virtuális mezők nem voltak számíthatóak, amelyek másik virtuális mezőtől függtek (#14939 - normál) 
- Javítva lett, hogy a szabály alapú címkék nem jelentek meg, amikor python kifejezés függvénnyel volt használva (#14985 - normál)
- Automatikus frissítés, amikor a szimbólum szintek megváltoznak a stílus dokkban (#14861 - normál)
- Javítva lett, hogy a stílus dokk gomb nem volt szinkronizálva a dokk állapotához (#14862 - normál)
- Javítva lettek az SVG szöveg megjelenítési hibái (#14644, #14794 - normál)
- Biztosítva van, hogy az adatvezérelt gombon megjelenített mezők mindig frissek legyenek (#14809 - normál)
- Javítva lett, hogy a nagyítás gyorsbillentyűjét nem lehetett beállítani (#14958 - normál)
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- Hiányzó proxyk hozzáadása a jelmagyarázat ellenőrzés viselkedésre az invertált felületek és a áthelyezés megjelenítések részmegjelenítéséhez (nem jelentett)
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- WKB típus mutatása a vektor réteg metaadatban (nem jelentett)
- Hiányzó jellegzetesség karakterláncok hozzáadása a réteg metaadathoz (nem jelentett)
- Javítva lett a hibakeresési zaj, a 2.5D geometria réteg használatakor (nem jelentett)
- Javítva lett, hogy néhány állapotsor vezérlőt nem lehetett elrejteni a testreszabáson keresztül (nem jelentett)
- A stílus vezérlő folyamatosan frissülővé téve, úgy, hogy emlékezzen a beállításokra (nem jelentett)
- Don\'t show constraint messages when form is in search mode (unreported)
- Görgetősáv megjelenítése az attribútum űrlapra mint azonosítási eredmények (nem jelentett)
- A stílus dokk Alkalmaz gombja mindig engedélyezett állapotba téve (nem jelentett)
- Javítva lett néhány hiányzó automatikus frissítés a stílus dokkból (nem jelentett)

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Itt vannak a bejegyzések, amelyekkel foglalkozott a QGIS 2.16 hibajavításának ideje alatt.

**Súlyos/Magas:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normál**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Egyéb:**
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
- Egy út hiányzott a Vektor réteg hozzáadásából!
- Az automata követés nem sikerült a köríves geometriákban
- A WMS nem működött a master a625eeb verzióban (2.15.0-80)
- Python hiba az előre konfigurált Feldolgozás algoritmusban
- GPS don\'t record geometry point, but only attribute values\...
- Stílus dokk: az átlátszóság panel (globális átlátszóság, átlátszó pixel, stb.) nem működött a domborzat árnyékolás megjelenítéssel
- Stílus dokk: vissza gomb és a morzsa hiányzott, amikor egy szabály alapú címkézést lett szerkesztve
- Javítva lett a visszavonás/ismét parancs a szabály alapú megjelenítés/címkézésre a stílus dokkban
- Javítva lett a visszavonás vezérlő frissítése a stílus panelben
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Fokozva lett a QgsMapLayerRegistry stabilitása
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- Javítva lett néhány Python 3 kompatibilitási probléma
- Az OSX tesztek újbóli engedélyezésével kapcsolatos munka (a 2.16 kiadás után összevonva)
- API dokumentáció
- startup.py dupla végrehajtása
- UX javítások:
  - Attribútum tábla: mindig megjelenítette a sorozatos oszlopfejléc-számokat
  - Kapcsolat hivatkozás vezérlő: Csak akkor engedélyezte az űrlapgombot, ha egy elem be volt állítva
  - Elem azonosító mutatása az attribútum tábla eszköztippjében
  - Kezdeti vezérlő fókusz a hitelesítési párbeszédablakban
  - Alapértelmezett időtúllépés a üzenetsáv elemeire
  - Add button\" state in postgis source select dialog
- Hiányzó fejléc fájlok telepítése
- Összeomlás a kilépésnél
- Hálózat gyorsítótár könyvtár
- Elem űrlap elrejtve a főablak mögött Windowson
- Offline szerkesztés: Figyelembe veszi a relatív útvonalakat
- Offline szerkesztés: a megváltozott attribútumok rossz elemeket eredményeznek
- Offline editing: Don\'t crash with raster layers
- A kapcsolat űrlap végtelenül növekszik
- Javítva az összeomlás, amikor egy stílust tölt be a réteg tulajdonságokban
- Javítva az összeomlás, amikor egy dokkolt attribútum táblát zár be
- Javítva lett az alapértelmezésben rosszul beállított GPSBabel útvonala
- Megjeleníti a helyes elemszámot a geometriát igénylő szabály szerint
- Javítva lett az összeomlás, amikor a 2.5D megjelenítés volt használva egy nem kompatibilis réteggel

{{<content-end >}}
