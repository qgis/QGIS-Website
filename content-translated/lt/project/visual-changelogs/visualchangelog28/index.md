---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: projektą
sidebar: true
title: QGIS 2.8 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.8 pakeitimai{#changelog28 }
Laidos data: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Ilgalaikė laida**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

LTR laidų tikslas - teikti stabilias ir mažiau besikeičiančias platformas, skirtas didelėms įmonėms ir organizacijoms, kurios nenori rūpintis naudotojų žinių atnaujinimu, mokymo medžiaga ir pan. daugiau nei kartą per metus. LTR sėkmė labiausiai priklauso nuo jūsų - mūsų mylimų naudotojų - mums reikia jūsų palaikymo, kad padėtumėte finansuoti klaidų taisymą ir užtikrinti, kad jūsų palaikymo kontraktuose nurodyta, kad bet kokie klaidų ištaisymai įkeliami ne tik į vystymo, bet ir į LTR šaką.

Jei LTR jums svarbi, prašome apsvarstykite tiesioginį QGIS projekto palaikymą arba įtikinkite savo komercinio palaikymo tiekėją naudoti LTR kaip jūsų įmonės pagrindą, kad visi galėtų pelnytis iš stabilios platformos, kuri pastoviai tobulinama ir atnaujinama. Pastaba kad naudotojams ir įmonėms, kurios mėgsta gyventi priešakyje, ir toliau bus teikiamos mūsų kas keturis mėnesius kuriamos laidos.

***Naujos savybės***

QGIS 2.8 taipogi ypatinga laida, nes joje yra tiek daug naujų puikių savybių, pataisymų ir išplėtimų, kad populiariausia atvira darbastalio GIS taptų dar funkcionalesnė ir naudingesnė.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Ačiū**

Norime padėkoti programuotojams, dokumentuotojams, testuotojams ir dar būriui kitų žmonių, kurie savo noru aukojo savo laiką ir pastangas (arba finansavo tuo užsiimančius žmones).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Na ir pagaliau norėtume padėkoti savo rėmėjams už neįkainojamą finansinę paramą šiam projektui:
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

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Bendra
### Savybė: išraiškų įvedimas į prasukiklius
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Savybė: žymeles galima importuoti ir eksportuoti
Dabar galima įrašyti ir įkelti jūsų žymeles į failą. Taip lengviau dalintis pasižymėtomis vietomis arba perkelti jas į kitą kompiuterį.

**Šią savybę sukūrė:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Savybė: išraiškų patobulinimai
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Tingus išraiškų įvertinimas**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Savybė: pastovus testavimo karkasas ir QA patobulinimai
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

Taipogi reguliariai vykdomi QGIS kodo padengimo skaičiavimai. To pasekoje mes radome ir pataisėme daugiau nei 1000 problemų, įskaitant atminties praradimą ir galimus lūžimus. QGIS defektų tankis yra 0,01, kai tuo metu vidutinis tokio tipo programų tankis yra 1,0.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Analizės įrankiai
### Savybė: matavimo dialogo patobulinimai
Patobulintame matavimo įrankyje galite parinkti, kuriuos matavimo vienetus naudoti matavimo dialoge. Taipogi dialoge yra nauja informacijos skiltis, rodanti, kokie nustatymai naudojami vykdant matavimo skaičiavimus.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Naršyklė
### Jautresnė naršyklė
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Šią savybę sukūrė:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Duomenų tiekėjai
### Savybė: kontekstinio WMS legendos vaizdo palaikymas
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Duomenų valdymas
### Savybė: keičiamas jungčių priešdėlis
Dabar sluoksnio savybių dialogo jungčių valdyme galite nurodyti savo priešdėlį. Naudojant priešdėlį, atributų lentelėje sujungti atributai bus rodomi su jūsų nurodytu priešdėliu.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Savybė: laikinų atminties sluoksnių kūrimo palaikymas
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Savybė: parinktų eilučių skaičiavimo palaikymas
Dabar laukų skaičiuotuvo įrankinėje pridėtu mygtuku atributų lentelėje skaičiavimus galite taikyti tik pažymėtoms eilutėms.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Skaitmeninimas
### Savybė: sudėtingesni skaitmeninimo įrankiai
Jei kada nors norėjote skaitmeninti linijas, kurios yra tiksliai lygiagrečios arba konkretaus kampo, užrakinti linijas ties nurodytu kampu - dabar galite tai padaryti QGIS! Sudėtingesni skaitmeninimo įrankiai - tai CAD įvesties priedo perkeltas funkcionalumas, kuriam sukurtas naujas QGIS skydelis. Skydelis aktyvuojasi įvedant naujas geometrijas arba geometrijos kelius

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Savybė: patobulintas supaprastinimo įrankis
Supaprastinimo įrankis buvo perdarytas pridedant:
- OTF perprojektavimo palaikymą
- naudotojas gali nurodyti konkrečią toleranciją (ne tik neesminę santykinę reikšmę)
- toleranciją galima nurodyti arba žemėlapio/sluoksnio vienetais, arba taškais
- tolerancijos nustatymai įrašomi į nustatymus
- supaprasti vienu metu daugiau nei vieną geoobjektą (tempkite stačiakampį, o ne spauskite)
- kelių dalių geoobjektų palaikymas
- viršūnių skaičiaus sumažinimo statistika

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Savybė: pritraukimo patobulinimai
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Sluoksnių legenda
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Žemėlapio maketas
### Savybė: kūrėjo sąsajos patobulinimai
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Kūrėjo pilno ekrano režimas**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Savybė: tinklelio patobulinimai
Kūrėjas dabar leidžia tiksliau valdyti rėmo ir anotacijos vaizdavimą. Anksčiau pasuktiems žemėlapiams ar perprojektuotiems tinkleliams kūrėjas paišydavo visas koordinates kiekvienoje žemėlapio pusėje. Gaudavosi šone rodomų derinys platumos/y ir ilgumos/x koordinačių. Dabar galite nurodyti ar norite visų koordinačių, tik platumos ar tik ilgumos kiekvienoje rėmo pusėje. Panašios parinktys pridėtos ir žemėlapio tinklelio padalinimo valdymui.

Nauja vertikali mažėjanti kryptis anotacijoms. Šis pakeitimas prideda naują mažėjantį vertikalios krypties režimą žemėlapio tinklelio anotacijoms. Anksčiau buvo vertikalioms anotacijoms buvo palaikomas tik didėjantis tekstas.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Savybė: etikečių paraštės
- Dabar galite valdyti ir vertikalias, ir horizontalias **etikečių paraštes**. Anksčiau buvo vienas nustatymas, kuris buvo taikomas ir vertikaliai, ir horizontaliai paraštei. Šis pakeitimas leidžia naudotojui nurodyti skirtingas vertikalias ir horizontalias paraštes.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Priedai
### Savybė: Python'o konsolės patobulinimai
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Apdorojimas
### Savybė: naujas geometrinio predikato parametro tipas
Naudodami šį naują parametrų tipą algoritmuose **pažymėti pagal vietą, ištraukti pagal vietą** ir **sujungti atributus pagal vietą**, naudotojas gali konkrečiai parinkti naudojamą erdvinį operatorių.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Savybė: nauji algoritmai
Į apdorojimo karkasą buvo įtraukta eilė naujų algoritmų:
- **Reguliarių taškų** algoritmas (pagal #5953)
- **Simetrinio skirtumo** algoritmas (pagal #5953)
- **Vektorių dalinimo** algoritmas (pagal #5953)
- **Vektorių tinklelio** algoritmas (pagal #5953)
- **Hypsometrinių kreivių** skaičiavimo algoritmas
- **Linijų dalinimas linijomis**
- **Laukų pertvarkymo** atributų apdorojimo algoritmas

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programavimas
### Savybė: išraiškoms pridėtas komentavimo funkcionalumas
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Savybė: savų išraiškų funkcijų redaktorius
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Savybė: Qt5 palaikymas
QGIS dabar galima sukurti naudojant Qt5 bibliotekas. Pastebėtina, kad šiuo metu dauguma dvejetainio kodo pagal nutylėjimą vis dar naudoja Qt4.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Savybė: masinis erdvinių indeksų įkėlimas
Masinio erdvinių indeksų įkėlimo funkcionalumas įtrauktas į API. Taip galima daug greičiau inicializuoti erdvinį indeksą. Iš python'o tai labai paprasta:

`index = QgsSpatialIndex( layer.getFeatures() )`

Paprastas bandymas su 50K taškų atminties sluoksnyje:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

Indekso medis teoriškai taip pat turėtų būti geriau sukurtas dėl ko turėtų pagreitėti paieška.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Savybė: vykdyti tik pažymėtą SQL užklausos dalį
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Serveris
### Savybė: serverio python'o priedai
Python'o priedų palaikymas QGIS serveryje suteikia python'o jėgą serveriui, tai leidžia greitą ir efektyvų naujų savybių kūrimą ir pateikimą.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Savybė: sluoksnio stilių palaikymas
- QGIS serveris dabar palaiko iš anksto nustatytus sluoksnių stilius GetMap užklausose
- QGIS serveris dabar palaiko kelis stilius GetStyles užklausoje (žr. simbologijos sekciją žemiau)

### Savybė: prie WMS pridėtas DescribeLayer metodas
** Web Map Service sluoksnio aprašo profilis su stiliumi: DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Apibrėžiant naudotojo stilių, reikia informacijos apie simbolizuojamus geoobjektus ar bent jau jų objekto/padengimo tipą. Kadangi naudotojo stiliai gali būti taikomi ir pavadintam sluoksniui, turi būti mechanizmas, leidžiantis klientui gauti pavadintų sluoksnių objektų/padengimo tipo informaciją. Tai dar vienas pavyzdys, kai mažinamas skirtumas tarp WMS sluoksnių ir stilių koncepcijos ir WFS/WCS koncepcijos, tokios kaip geoobjekto-tipas ir padengimo sluoksnis. Kad tai leistų, WMS gali pasirinktinai palaikyti **DescribeLayer** užklausą.

DescribeLayer metodas laikomas geresne išeitimi nei dar labiau perkrauti WMS galimybių dokumentą.

Kiekvieno pavadinto sluoksnio aprašymas turi rodyti, ar jis tikrai remiasi geoobjektų duomenimis ir jei taip, turi rodyti WFS/WCS (pagal URL priešdėlį) ir geoobjektų/padengimo tipus. Pastebėtina, kad visiškai normalu pavadintam sluoksniui nebūti aprašytu tokiu būdu.
## Simbologija
### Savybė: rastro piešinio pildymo tipas
Šis naujas simbolinio sluoksnio tipas leidžia poligonus pildyti (kaladėlėmis išdėliotu) rastro piešiniu.

Parinktyse yra (nuo duomenų priklausantis) failo pavadinimas, permatomumas, piešinio dydis (taškais, mm arba žemėlapio vienetais), koordinačių režimas (geoobjektai arba rodinys) ir pasukimas.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Savybė: gyvas intensyvumo žemėlapio braižymas
Naujas intensyvumo vektorinio sluoksnio braižiklis leidžia kurti gyvus, dinaminius intensyvumo žemėlapius taškų sluoksniams.

Parinktyse galima nurodyti intensyvumo žemėlapio radiusą taškais, mm arba žemėlapio vienetais, parinkti spalvų rampą, svorio taškus pagal lauką ir slankiklis, leidžiantis balansuoti tarp braižymo greičio ir kokybės.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Savybė: keli stiliai viename sluoksnyje
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Savybė: daugiau nuo duomenų priklausančių simbologijos nustatymų
Pagerinta nuo duomenų priklausančių simbologijos nustatymų naudotojo sąsaja - nuo duomenų priklausančios parinktys perkeltos į kiekvieną nuo duomenų priklausomą savybę (taip elgsena tampa panaši į kitas QGIS dalis, tokias kaip etikečių savybes). Taipogi daug simbologijos savybių dabar jau galima nustatyti pagal duomenis. Šis naudotojo sąsajos patobulinimas taipogi leidžia iš karto matyti, ar yra naudojamas nuo duomenų priklausomas nustatymas bei lengviau prieiti prie nuo duomenų priklausančių nustatymų.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Savybė: DXF eksportas: patobulintas žymeklių simbolių eksportas
Patobulintas DXF failų eksportavimo funkcionalumas - didesnis tikslumas tarp eksportuotų žymeklių simbolių ir pradinės QGIS simbologijos.
### Savybė: žemėlapio pasukimas drobėje, pagerintas pasukimas kūrėjyje
Šioje laidoje yra pradinis žemėlapio pasukimo drobėje palaikymas. Galite pasukti drobę naudodami naują pasukimo valdiklį būsenos juostoje. Pasukimo palaikymas taip pat išplėstas į žemėlapio kūrėją, kad jis teisingai apdorotų etiketes, simbologiją ir pan.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Naudotojo sąsaja
### Savybė: patobulintas/nuoseklus projekcijos parinkimas
Dabar visi dialogai naudoja nuoseklų projekcijos parinkimo dialogą, kuris leidžia greitai parinkti iš paskutiniu metu naudotų ir standartinių projekto/QGIS projekcijų.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
