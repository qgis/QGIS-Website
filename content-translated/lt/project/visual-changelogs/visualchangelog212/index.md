---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: projektą
sidebar: true
title: QGIS 2.12 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.12 pakeitimai{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Release date: 2015-10-23

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Ačiū**

Norime padėkoti programuotojams, dokumentuotojams, testuotojams ir dar būriui kitų žmonių, kurie savo noru aukojo savo laiką ir pastangas (arba finansavo tuo užsiimančius žmones).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Na ir pagaliau norėtume padėkoti savo rėmėjams už neįkainojamą finansinę paramą šiam projektui:
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Bendra
### Savybė: naujas pasveikinimo ekranas
Vietoje to, kad rodytų tuščią baltą drobę, QGIS dabar rodys paskutinių projektų sąrašą su nedidelėmis iliustracijomis, kad būtų galima greitai ir paprastai grįžti į jūsų paskutinę darbo sesiją.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Savybė: pastovus kodo kokybės gerinimas
Naudojant adresavimo tvarkymo biblioteką buvo rasti ir pataisyti šimtai atminties nutekėjimų. Periodiškai naudojant automatinius Coverity Scan kodo skenavimus buvo ieškoma potencialių problemų, šiuo metu mūsų Coverity defektų tankis yra įspūdingai žemas - tik 0,02 defektai 1000 kodo eilučių. Automatinių testų biblioteka buvo stipriai padidinta kuriant 2.12 versiją, taigi dabar regresijos identifikuojamos ir pataisomos nedelsiant. 2.12 mes taipogi pridėjome pastovų testavimą OSX, kad kiekvienas kodo pakeitimas būtų tikrinamas testais tiek Linux, tiek ir OSX platformose.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Savybė: sudėtingesnis nustatymų redaktorius
Į nustatymų dialogą pridėtas skydelis, kuriame galite keisti bet kurią jūsų profilyje jau apibrėžtą parinktį. Tai skirta tik patyrusiems naudotojams, nes QGIS gali pradėti veikti neaiškiai, jei pakeisite vieną iš nustatymų nesuprasdami, ką darote.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Savybė: vienas kitą išjungiančių sluoksnių medžio grupė
Su šia savybe jūs galite sukurti sluoksnių grupę, kurioje tik vienas sluoksnis iš grupės gali būti rodomas konkrečiu metu. Šią savybę per kontekstinį meniu galima įjungti konkrečiai grupei sluoksnių medyje.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Šią savybę finansavo:** Tuscany Regionas (Italija) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Savybė: lauko reikšmių filtravimas išraiškos valdiklyje
Kuriant išraišką, kuri naudoja reikšmes iš lauko, jūs dabar galite filtruoti lauko reikšmes peržiūros skydelyje.

**Šią savybę sukūrė:** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Savybė: Naudotojo sąsajos temų palaikymas
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Savybė: Naujos 2.12 išraiškų funkcijos
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Buvo pridėta daugiau geometrijos funkcijų, tame tarpe:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

Papildomai kelios labai naudingos išraiškos buvo atkeltos iš expressions+ priedo, įskaitant:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

Taipogi kontekstinė išraiškos funkcijų pagalba buvo patobulinta geresniam skaitomumui.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Savybė: kintamieji išraiškose
Dabar galite apsibrėžti kintamuosius, kuriuos norite naudoti išraiškose. Kintamieji gali būti apibrėžti globaliame aplikacijos, projekto, sluoksnio arba maketo lygyje. Kaip ir CSS pakopinės taisyklės, kintamųjų reikšmės gali būti permušamos - pavyzdžiui projekto lygio kintamasis permuš bet kokius nustatytus aplikacijos lygio kintamuosius. Galite naudoti šiuos kintamuosius tekstinių eilučių ar savo išraiškų kūrimui. Pavyzdžiui maketo etiketės su tokiu turiniu:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

Sukurs tokį etiketės tekstą:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Analizės įrankiai
### Savybė: Į išvestinių laukų sąrašą pridėtas viršūnių skaičius identifikavimo įrankyje
Panaudojus identifikavimo įrankį linijos geoobjektui, papildomuose išvestiniuose atributuose dabar bus rodomas ir viršūnių skaičius geoobjekte.
### Savybė: Rastro lygiavimo įrankis
This new tool in qgis_analysis library is able to take several rasters as input and:
- perprojektuoti į tą patį CRS
- pertvarkyti į tokį patį celės dydį ir poslinkį tinklelyje
- apkarpyti pagal dominantį regioną
- prireikus pertvarkyti reikšmes

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Savybė: Geometrijos tikrinimo ir geometrijos pritraukimo priedai
Du nauji priedai (kuriuos jums reikės įjungti priedų tvarkyklėje) leidžia tikrinti ir taisyti geometrijas. **Geometrijos Tikrinimo** priedas (rodomas žemiau) jūsų vektoriniame duomenų rinkinyje ieškos skirtingų tipų sisteminių klaidų ir bandys jas už jus pataisyti. Pataisius klaidą, klaidų sąrašas automatiškai atnaujinamas, kad, pavyzdžiui, jei pataisius vieną klaidą išsprendžiamos kitos klaidos, visos klaidos būtų pašalinamos iš problemų sąrašo.

Su **Geometrijos pritraukimo** įrankiu jūs galite lygiuoti vieno vektorinio sluoksnio kraštus ir viršūnes su antro sluoksnio kraštais ir viršūnėmis, naudodami nurodytą toleranciją.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Programos ir projekto parinktys
### Savybė: užkoduoto slaptažodžio valdymas
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Pagrindiniu slaptažodžiu užkoduotos autentikacijos nustatymai laikomi SQLite duomenų bazėje
- Autentikacijos metodo priedų architektūra (kaip duomenų tiekėjų)
- Basic auth metodo priedas
- Bazinio autentikavimo priedas integruotas su PostGIS ir OWS tiekėjų jungtimis
- Kartu su dabartiniu naudotojo/slaptažodžio nustatymu (vis dar pilnai veikia)
- SSL serverio jungties konfigūracija (įrašyti išimtis ar savas konfigūracijas SSL jungties klaidoms)

Susiję su PKI autentikacija:
- Importuoti papildomus Sertifikatų Autoritetus - CA, tarpiniai sertifikatų išdavėjai ir asmens identiteto paketai
- Sertifikatų komponentai valdomi kaip Firefox'e
- Autentikavimo metodų priedai PEM ir PKCS#12 paketams diske arba išsaugotiems asmeniniams identitetams
- Integruota su OWS tiekėjų jungtimis (PostGIS ir kitoms duomenų bazėms prireiks šiek tiek daugiau laiko, kad pradėtų veikti)

Bendrų projektų atvejams, įskaitant tinklinių diskų atvejams, jūs galite keisti autentikavimo konfigūracijos (authcfg) ID į kažką, ką turi visi naudotojai.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Blogų sluoksnių valdymo dialoge naudotojai gali Pridėti/Keisti/Išimti autentikacijos konfigūracijas tiesiai iš dialogo ir taip atitinkamai pakeisti duomenų šaltinio URI. Taigi bendro projekto atveju naudotojas gali projekto įkėlimo metu nedelsiant pridėti reikiamą naują autentikacijos konfigūraciją (ir pamatyti koks konkrečiai bus naudojamas bendro authcfg ID).

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Šią savybę sukūrė:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Naršyklė
### Savybė: PostGIS jungčių naršyklėje patobulinimai
QGIS naršyklė dabar palaiko papildomą funkcionalumą PostGIS jungtims, įskaitant galimybę **kurti, pervadinti ir trinti schemas**, **sluoksnių pervadinimo ir kapojimo galimybę** ir **lentelių kopijavimą iš vienos schemos į kitą**.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Duomenų tiekėjai
### Savybė: PostGIS tiekėjo patobulinimai
Padaryti šie PostGIS tiekėjo patobulinimai:
- PostGIS sluoksnių taisyklėmis paremto braižymo greitaveikos patobulinimai
- pridėtas sudėtinių raktų rodiniuose palaikymas

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## Duomenų valdymas
### Savybė: DB tvarkyklės patobulinimai
DB tvarkyklės įrankyje buvo padaryti patobulinimai:
- DB tvarkyklėje dabar galite eksportuoti jūsų duomenis į bet kokį OGR palaikomą duomenų formatą, o ne į ankstesnėse versijose prieinamą vienintelį Shapefile.
- DB tvarkyklė dabar palaiko ir Oracle Spatial
- Importuojant duomenis į lentelę jūs galite naudoti naują parinktį **importuoti tik pažymėtus geoobjektus**, kad apribotumėte, kas bus importuota.
- Nauji užklausų langai dabar kuriami kaip kortelės, kad būtų mažiau dialogų

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Savybė: sąlyginis atributų lentelės langelių formatavimas
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Savybė: Santykinių kelių palaikymas valdikliuose
Šiems redagavimo valdiklių tipams:
- Failo pavadinimas
- Foto
- Žiniatinklio vaizdas

Jei failų naršyklės pagalba parinktas kelias yra tame pačiame aplanke kaip ir .qgs projekto failas arba žemiau, keliai konvertuojami į santykinius kelius. Taip QGIS projektai su prisegta multimedija tampa pernešamesni.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Skaitmeninimas
### Savybė: skaitmeninimo patobulinimai
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- įrankis apskritos linijos pridėjimui dviem taškais ir spinduliu
- įrankis apskritos linijos pridėjimui su pradžios tašku, kreivės taško ir pabaigos tašku
- leidžiamas naujų geoobjektų braižymo nutraukimas
- viršūnių lentelės rodymas redaguojant viršūnės įrankio pagalba, tai leidžia jums rankiniu būdu įvesti konkrečias x ir y koordinates viršūnėms, bei z ir m reikšmes (priklausomai nuo sluoksnio tipo)

Papildomai, daugiau geometrijos redagavimo ir keitimo įrankių buvo atnaujinti, kad teisingai dirbtų su sluoksniais, turinčiais z arba m matmenis.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Užrašai
### Feature: Data defined quadrant when in \"around point\" mode
Dabar galima nurodyti nuo duomenų priklausantį kvadrantą, kai taško etiketė pozicionuojama režime Aplink tašką. Tai leidžia rankiniu būdu keisti konkrečios etiketė pozicijos kvadrantą, tuo pačiu metu leidžiant likusias etiketes pildyti automatiškai.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Savybė: braižyti tik tas etiketes, kurios telpa poligonų viduje
Poligonų sluoksniams pridėta parinktis, leidžianti etiketes braižyti tik tada, kai jos pilnai telpa poligono geoobjekte.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Savybė: etikečių kliūčių prioriteto kontrolė
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Savybė: naujos parinktys, kontroliuojančios kaip poligonų sluoksniai veikia kaip kliūtys
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Savybė: nuo duomenų priklausanti etikečių prioriteto kontrolė
Ši dažnai prašoma savybė leidžia naudotojams nurodyti konkrečių etikečių prioritetą. Ankstesnėse QGIS laidose etikečių prioritetas būdavo nurodomas visam sluoksniui, nebuvo galimybė kontroliuoti konkrečių geoobjektų prioriteto sluoksnyje. Dabar galite naudoti nuo duomenų priklausančią išraišką arba lauką, kad keistumėte konkrečių geoobjektų prioritetą sluoksnio viduje!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Savybė: tik-kliūčių sluoksnio parinktis
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Savybė: nuo taisyklių priklausančios etiketės
Geoobjektų etikečių stilių dabar galima keisti naudojant taisykles, kad galėtumėte dar labiau kontroliuoti, kur ir kaip braižomos etiketės. Kaip ir nuo taisyklių priklausantis kartografinis braižymas, etikečių taisyklės gali būti valdomos hierarchiškomis taisyklėmis, leidžiančiomis labai lanksčiai valdyti stiliaus parinktis. Pavyzdžiui jūs galite etiketes braižyti skirtingai, priklausomai nuo geoobjekto, kuriame jos bus braižomos, dydžio (tai pavaizduota ekrano nuotraukoje).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Šią savybę finansavo:** Tuscany Regionas (Italija) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Žemėlapio maketas
### Savybė: atlaso navigacijos patobulinimai
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

Puslapio pavadinimas taip pat gali būti naudojamas simbologijoje ar etikečių išraiškose, taip suteikiant galimybę įmantresniam atlaso geoobjektų stilių nustatymui pagal jų puslapio pavadinimą.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Savybė: savas tinklelių anotacijų formatas
Maketo žemėlapio tinklelio anotacijas dabar galima formatuoti savu formatu, kuris įvertinamas naudojant išraiškų variklį. Galite panaudoti bet kokį ezoterinį tinklelio numeravimo formatą, kokio tik reikia jūsų žemėlapiui!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Savybė: kelių eilučių tekstas ir automatinis teksto perkėlimas maketo atributų lentelėse
Maketo atributų lentelės dabar pilnai palaiko kelių eilučių tekstą. Taipogi pridėtas vertikalaus lygiavimo celėje valdymas, kartu su parinktimis tekstą perkelti ties konkrečiais simboliais arba automatiškai paskaičiuoti, kad tekstas tilptų į stulpelių plotį. Norėdami įjungti automatinį teksto perkėlimą su automatiniu eilučių aukščiu, nurodykite stulpeliui fiksuotą dydį.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Savybė: sudėtingesnis langelio fono spalvos tinkinimas
Šis pakeitimas leidžia naudotojams nustatyti skirtingas spalvas besikeičiančioms eilutėms ir stulpeliams. Pirma/paskutinė eilutė/stulpelis ir antraštės eilutė maketo atributų lentelėse.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Savybė: pridėtos parinktys talpinti puslapį į turinį ir apkarpyti eksportą pagal turinį
Maketo skydelyje pridėta nauji parinktis, leidžianti keisti maketo dydį pagal jo turinį, su galimybe prireikus pridėti papildomas paraštes.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

Kad tai veiktų, buvo pridėtas naujas piešinio eksportavimo dialogas, kuriame taip pat yra patogios galimybės permušti spausdinimo rezoliuciją arba eksportuojamo piešinio matmenis.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Savybė: vektorinius sluoksnius priverstinai braižyti kaip rastrą
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Savybė: nuo duomenų priklausanti žemėlapio sluoksnių ir stilių kontrolė
Pridėtas naujas nuo duomenų priklausantis žemėlapio sluoksnių ir stilių rinkinių valdymas maketo žemėlapyje. Žemėlapio sluoksnių duomenų priklausomumo išraiška turėtų grąžinti \| (vertikaliais brūkšneliais) atskirtą sluoksnių, kurie turi būti rodomi žemėlapyje, pavadinimų sąrašą, arba stilių rinkinių išraiška turi grąžinti esamo stilių rinkinio pavadinimą.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Savybė: galimybė slėpti puslapius rodyme/eksportavime
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Priedai
### Savybė: GRASS priedo atnaujinimas
GRASS priedas buvo atnaujintas, pridedant GRASS 7 palaikymą. GRASS sluoksnius galima naršyti ir įkelti iš QGIS naršyklės arba naršymo skydelio. GRASS vektorinius duomenis galima redaguoti tiesiogiai QGIS. Projekte yra šie darbiniai paketai:
- Priedo bibliotekos atnaujinimas ir kelių versijų kūrimas
- QGIS naršyklės ir naršymo skydelio integracija
- Žemėlapių rinkinių, modulių ir duomenų analizės palaikymas
- vektorių redagavimas

Tiek GRASS 6, tiek GRASS 7 naudotojai pastebės, kad integracija tarp GRASS ir QGIS daug sklandesnė. Galite kurti GRASS sluoksnius tiesiai QGIS naršymo skydelyje, keisti GRASS vektorinių sluoksnių stilius naudodami standartines QGIS stiliaus priemones bei naudoti žinomus QGIS skaitmeninimo įrankius kurdami naujas geometrijas GRASS žemėlapių rinkinyje.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programavimas
### Feature: Map tools moved from app-\>gui
Šis pakeitimas leidžia naudoti žemėlapio įrankius iš PyQGIS scenarijų ir Python priedų.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### Savybė: Sluoksnių redagavimas naudojant \`with edit(layer):\`
Pavyzdys:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Tai pabaigoje automatiškai iškvies commitChanges(). Jei įvyks bet kokia klaida, visiems pakeitimams bus įvykdyta rollBack().

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Savybė: naujas API etikečių varikliui (QgsLabelingEngineV2)
Mintis yra padaryti variklį lankstesnį už QgsPalLabeling variantą:
> - abstraktus tekstinių etikečių / diagramų apdorojimas tiesiai iš variklio
> - leisti kelis skirtingus etikečių tipus viename sluoksnyje
> - leisti savus etikečių tiekėjus (pvz. veikiančius per priedus)
> - padaryti etikečių variklį nepriklausomą nuo žemėlapio braižymo variklio
> - supaprastinti automatinį etikečių variklio ir jo komponentų testavimą

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Šią savybę finansavo:** Tuscany Regionas (Italija) - SITA (CIG: 63526840AE)
### Savybė: atverti scenarijus išoriniame redaktoriuje
Pythoniastai džiaukitės - jūs dabar galite atidaryti savo scenarijus išoriniame redaktoriuje, naudodami naują konsolės mygtuką.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Savybė: naujos PyQGIS programų klasės
Buvo pridėta nauja klasė QgsStringUtils, kuri leidžia PyQGIS scenarijams naudoti naujus apytikslio palyginimo algoritmus, pridėtus 2.12. Tai funkcijos, ieškančios Levenshtein redagavimo atstumą tarp dviejų eilučių, soundex fonetinės išraiškos skaičiavimas ir pan. Šie algoritmai stipriai optimizuoti greitaveikai, taigi jų pagalba galite daryti apytikslį palyginimą milijonuose eilučių!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Serveris
### Savybė: QGIS serverio Python API
QGIS serveris dabar supakuotas kaip biblioteka su pradiniu (bet augančiu) API ir sąsaja su Python'u. Su nauju API turime aibę Python'o testų serverio pagrindiniams komponentams ir serverio priedams. Paleisti serverį per Python dabar labai paprasta:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Savybė: getMap dxf formatu
Dabar galima gauti GetMap WMS užklausos rezultatą DXF formatu. Palaikomos tos pačios savybės ir parinktys, kaip ir QGIS darbastalyje. Su tais pačiais apribojimais.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

Ekrano nuotraukoje matote QGIS Žiniatinklio klientą kairėje su DXF eksporto funkcionalumu (naudojant QGIS serverį) ir tą pačią apimti, rodomą Autodesk TrueView, dešinėje.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Simbologija
### Savybė: miniatiūrų eksportavimas iš stilių tvarkyklės
Stilių tvarkyklė dabar leidžia eksportuoti pažymėtas stilių miniatiūras arba kaip SVG, arba kaip PNG piešinius.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Savybė: nauja parinktis riboti dydį milimetrais, kai naudojami žemėlapio vienetų dydžiai
Anksčiau riboti mastelio intervalą buvo galima tik žemėlapio vienetais. Dabar taip pat galite pasirinkti riboti galutinio rezultato dydžiu milimetrais.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Savybė: pastumto braižymo patobulinimai
- Leisti postūmio braižymui toleranciją milimetrais/taškais
- Leisti spalvoms nustatyti permatomumą
- Koncentrinių žiedų pozicionavimo režimas (leidžia kompaktiškesnį rodymą nei vien žiedams)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Savybė: dabar galima redaguoti visas spalvų rampas
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Savybė: SVG žymeklių rėmų tvarkymo patobulinimai
QGIS 2.12 pataisyta eilė prblemų su SVG žymeklių ir SVG pildymo simbolių rėmelių valdymu.

Ankstesnėse QGIS versijose rėmeliai buvo braižomi stipriai mažesni, nei nurodyta, o SVG su rėmelio dydžiu žemėlapio vienetais braižymais buvo sugadintas.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Savybė: pridėti taškus kaip vieną iš simbologijos dydžio nurodymo vienetų
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
