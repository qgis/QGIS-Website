---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: projekt
sidebar: true
title: A QGIS 2.8 változásnaplója
type: visual-changelog

---
{{<content-start >}}
# A QGIS 2.8 változásnaplója{#changelog28 }
Release date: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Hosszútávú kiadás**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

Az LTR kiadások célja, hogy egy stabil, kevésbé gyakran változó platformot biztosítson azoknak a vállalatoknak és szervezeteknek, melyek évente egynél többször nem akarnak foglalkozni a felhasználói ismeretek, az oktató anyagok, stb. frissítésével. Az LTR sikere nagyban öntől függ, a kedves felhasználóinktól - szükségünk van a támogatására a hibajavítások finanszírozásában és bizonyosodjon meg róla, hogy a támogatás nyújtó szerződésében vállalja a hibajavítások átvezetését az LTR ágon és a fejlesztési ágon is.

Ha egy LTR fontos önnek, kérjük fontolja meg a QGIS projekt közvetlen támogatását, ösztönözze a kereskedelmi szolgáltatóját, hogy az LTR-t használja a vállalati megoldás alapjául, így mindenkinek előnyös lehet a stabil platform, melyet folyamatosan javítanak és finomítanak. Ne feledje, hogy a négy hónaponkénti kiadások töretlenül folytatódnak azoknak a felhasználóknak és szervezeteknek, akik élen akarnak járni.

**Újdonságok**

A QGIS 2.8 egy különleges kiadás, mert sok nagyszerű új funkciót, gyorsításokat és fejlesztéseket tartalmaz, hogy a legnépszerűbb szabad asztali GIS-t még funkció gazdagabbá és hasznosabbá tegye.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Köszönet**

Szeretnénk megköszönni a fejlesztőknek, a dokumentáció készítőknek, tesztelőknek és a sok embernek akik önként adják az idejüket és energiájukat (vagy finanszírozza, hogy mások tegyenek így).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Végül szeretnénk megköszönni a hivatalos szponzorainknak a felbecsülhetetlen anyagi támogatást, melyet a projektnek nyújtottak:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

A QGIS szabad szoftver és semmi sem kötelezi arra, hogy fizessen használatáért. Valójában a QGIS használatára bátorítjuk az embereket, legyenek bárhol a világon, pénzügyi és társadalmi helyzettől függetlenül. Úgy hisszük azzal, hogy térbeli  döntéstámogatási eszközöket adunk az emberek kezébe, annak jobb társadalom építő ereje van az egész emberiségre nézve.

{{<table-of-contents >}}
## Általános
### Funkció: Kifejezés bevitel a léptethető mezőkbe
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Funkció: Könyvjelzők importálhatók, exportálhatók
Már lehetséges a könyvjelzők mentése / betöltése fájlból, ami megkönnyíti a megjelölt helyek megosztását és átvitelét számítógépek között.

**Ezt a funkciót fejlesztette:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Funkció: fejlesztések a kifejezésekhez
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Kifejezések "lusta" kiértékelése**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Funkció: Folyamatos tesztelő keretrendszer és minőségbiztosítási fejlesztések
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

Rendszeresen végzünk "Coverity Scan" vizsgálatot a QGIS kódbázison. Ennek eredményeképpen több, mint 1000 megjelölt problémát azonosítottunk és javítottunk, mint pl. a memória szivárgás és potenciális összeomlások. A QGIS hibasűrűsége 0.01, míg az átlagos, hasonló  méretű programoké körülbelül 1.0.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Elemző eszközök
### Funkció: mérés párbeszédablak fejlesztések
A mérőeszközt továbbfejlesztettük, így már kiválasztható a mértékegység a párbeszédablakban. A párbeszédablaknak van egy információs része is, ami mutatja a mérés közben érvényes beállításokat.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Böngésző
### Reszponzívabb böngésző
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Ezt a funkciót fejlesztette:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Adatszolgáltatók
### Funkció: WMS jelkulcsi grafikák környezetérzékeny támogatása
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Adatkezelés
### Funkció: Egyedi előtag kapcsolásokhoz (join)
Megadhat egy egyedi előtagot a kapcsolások kezelőjében a rétegtulajdonságok párbeszédablakban. Ha előtagot használ, az attribútum tábla a kapcsolt attribútumokat a beállított előtaggal mutatja.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Funkció: Ideiglenesen, memóriában létező rétegek készítésének támogatása
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Funkció: Kiválasztott sorokon számítások végzésének támogatása
Az attribútum táblában végezhet számításokat a kiválasztott sorokon a mező-számológép eszköztáron elhelyezett új gomb segítségével.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Digitalizálás
### Funkció: Fejlett digitalizáló eszközök
Ha párhuzamos, merőleges, meghatározott szögű szakaszokat stb. szeretne digitalizálni, most már lehet QGIS-ben! A fejett digitalizáló eszközök a CADinput modul portolásával jöttek létre és egy új panelre kerültek QGIS-ben. A panel aktívvá válik, mikor új geometriát, vagy geometria részeket szerkesztünk.

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Funkció: javított egyszerűsítés eszköz
Az egyszerűsítő eszközt átírtuk. Új funkciói:
- azonnali újravetítési támogatás
- felhasználó megadhatja a pontos toleranciát (nem csak egy nem sokat mondó relatív értéket)
- a toleranciát térkép-i, réteg-, vagy pixel mértékegységben adhatjuk meg
- a tolerancia beállítások az egyéb beállításokkal mentődnek
- több elem együttes egyszerűsítése (húzzon téglalapot klikkelés helyett)
- több részből álló elemek támogatása
- statisztika a töréspontok számának csökkenéséről

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Funkció: Illesztés fejlesztések
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Réteg jelmagyarázat
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Térkép összeállítás
### Funkció:  Lapösszeállítő felhasználói felület fejlesztések
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Teljes képernyős mód a lapösszeállítóban**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Funkció: Rács fejlesztése
A lapösszeállítóban finomabban vezérelhető a keret és a feliratok megjelenítése. Korábban, elforgatott térképek, vagy újravetített rácsok esetén a lapösszeállító minden koordinátát a térkép minden oldalára felírt. Ennek eredménye kevert szélesség/y és hosszúság/x koordináta megírás volt egy-egy oldalon. Most kiválasztható, hogy minden koordinátát szeretne, csak szélességit, vagy csak hosszúságit megírni a térképkeret oldalaira. Hasonló opciók elérhetők a térképrács keret felosztására is.

Új függőlegesen lefelé íródó feliratok. Ez a változás egy lefelé íródó irányt ad hozzá a térképrács megírások irányaihoz. Korábban függőleges irányban csak felfelé íródó feliratokat támogattunk.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Funkció: Címke margók
- Most már vezérelheti mind a vízszintes, mind függőleges irányban a **címke margót**. Korábban egy azonos margó beállítást lehetett alkalmazni vízszintes és függőleges irányban. Ez a változtatás lehetővé teszi különböző vízszintes és függőleges margók használatát.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Bővítmények
### Funkció: Python konzol fejlesztések
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Feldolgozás
### Funkció: Új geometriai predikátum paraméter típus
Ezzel az új paraméterrel, melyet a **Hely szerinti  kiválasztás, Hely szerinti  kivágás** és a **Attribútumok kapcsolása hely szerint** algoritmusok használnak, a felhasználó pontosan beállíthatja a használandó térbeli operátort.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Funkció: Új algoritmusok
Jópár új algoritmust adtunk hozzá a feldolgozó keretrendszerhez.
- **Szabályos pontok** algoritmus (#5953-as hibát javítja)
- **Szimmetrikus különbség**  (addresses #5953)
- **Vektor darabolás** algoritmus (addresses #5953)
- **Vektor rács** algoritmus (#5953)
- **Hipszometrikus görbe** számítási algoritmus
- **Vonalak darabolása vonalakkal**
- **Refaktor mezők** attribútum kezelő algoritmus

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programozhatóság
### Funkció: megjegyzés hozzáadása a kifejezésekhez
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Funkció: Testre szabott kifejezések, függvény szerkesztő
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Funkció: Qt5 támogatás
A QGIS összeszerkeszthető a Qt5 könyvtárak használatával. Vegye figyelembe, hogy az aktuális bináris változatok alapértelmezés szerint még Qt4-el készülnek.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Funkció: Térbeli index tömeges betöltése
Az API-ban a térbeli indexek tömeges betöltéséhez adtunk támogatást. A térbeli indexek inicializálására ez egy sokkal gyorsabb módszer. Pythonból ilyen egyszerű:

`index = QgsSpatialIndex( layer.getFeatures() )`

Egy egyszerű teszt 50K ponttal egy memória rétegen:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

Az index fa elméletileg jobban felépített lehetne és ez gyorsabb kereséseket eredményezne.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Funkció: Az SQL lekérdezés szelektált részének futtatása
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Szerver
### Funkció: Szerver python modulok
A Python modulok támogatása a QGIS szerveren a Python erejét hozza a szerver oldalra, az új funkciók gyors, hatékony fejlesztését és továbbítását lehetővé téve.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Funkció: réteg stílusok támogatása
- A QGIS szerver támogatja az előre definiált réteg stílusokat a GetMap kérésekben
- A QGIS szerver most már támogatja a többszörös stílusokat GetStyles kérésekben (lásd. a lenti jelrendszer szakaszban)

### Funkció: DescribeLayer metódus hozzáadása a WMS-hez
**Styled Layer Descriptor profile of the Web Map Service : DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Defining a user-defined style requires information about the features being symbolized, or at least their feature/coverage type. Since user-defined styles can be applied to a named layer, there needs to be a mechanism by which a client can obtain feature/coverage-type information for a named layer. This is another example of bridging the gap between the WMS concepts of layers and styles and WFS/WCS concepts such as feature-type and coverage layer. To allow this, a WMS may optionally support the **DescribeLayer** request.

DescribeLayer method has been thought to be a better approach than overloading the WMS capabilities document even more.

For each named layer, the description should indicate if it is indeed based on feature data and if so it should indicate the WFS/WCS (by a URL prefix) and the feature/coverage types. Note that it is perfectly valid for a named layer not to be describable in this way.
## Jelrendszer
### Funkció: Raszter kép kitöltési típus
Ez az új szimbólum réteg típus lehetővé teszi egy felület kitöltését (csempe) raszter képpel.

Options include (data defined) file name, opacity, image size (in pixels, mm or map units), coordinate mode (feature or view), and rotation.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Funkció: élő hőtérkép rajzolás
Az új hőtérkép vektor réteg rajzoló lehetővé teszi a pont rétegekre az élő, dinamikus hótérképeket.

Options include specifying heatmap radius in pixels, mm or map units, choice of color ramp,weighting points by field, and a slider for selecting a tradeoff between render speed and quality.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Funkció: Több stílus rétegenként
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Funkció: Több adatvezérelt megjelenítési beállítások
The user interface for data defined symbology settings has been improved - moving the data defined option next to each data definable property (in keeping with other parts of QGIS such as the labeling properties). Also many new properties have been made data definable for symbology. This user interface improvement also provides a way to immediately see if a data defined override is defined as well as easier access to the data-defined settings.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Funkció: DXF export: szimbólum export tökéletesítése
The exporter functionality for DXF files has been improved, with better fidelity of exported marker symbols to the original QGIS symbology.
### Funkció: Térkép forgatás a vásznon, tökéletesített forgatás az összeállítás szerkesztőben
This release includes preliminary support for rotation in the map canvas. You can rotate the canvas using the new rotation widget in the status bar. Rotation support has been extended into the map composer too so that it correctly handles labelling and symbology, etc.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Felhasználói felület
### Funkció: Javított/konzisztens vetület kiválasztás
All dialogs now use a consistent projection selection widget, which allows for quickly selecting from recently used and standard project/QGIS projections.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
