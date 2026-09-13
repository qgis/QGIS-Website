---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: projektą
sidebar: true
title: QGIS 2.10 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.10 pakeitimai{#changelog210 }
Release date: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Paskutinė laida**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Ačiū**

Norime padėkoti programuotojams, dokumentuotojams, testuotojams ir dar būriui kitų žmonių, kurie savo noru aukojo savo laiką ir pastangas (arba finansavo tuo užsiimančius žmones).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Na ir pagaliau norėtume padėkoti savo rėmėjams už neįkainojamą finansinę paramą šiam projektui:
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
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
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Bendra
### Savybė: dabar galima redaguoti jungimo operacijos parametrus
Nuo šiol galima redaguoti sujungimo operacijos parametrus (tokius kaip jungimo priešdėlį ar jungiamus stulpelius) po to, kai sujungimas jau buvo sukurtas. Iki šio pakeitimo tekdavo ištrinti ir iš naujo sukurti visą sujungimą.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Savybė: sluoksnius su sujungimais jau galima filtruoti
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Savybė: bendri patobulinimai
Be kitų žemiau pateiktų elementų, buvo padaryti šie patobulinimai:
- Taškų debesies (angl. pointcloud) sluoksnių palaikymas PostGIS
- Prišliejamuose valdikliuose patobulintos piktogramų juostos ir piktogramos - jos užima mažiau vietos ekrane ir geriau atrodo OSX
- GRASS priedo / tiekėjo patobulinimai
- Nelotyniškų raidžių palaikymas išlenktose etiketėse
- Stipriai patobulinti ir greitesni rastro skaičiavimo ir geopririšimo įrankiai
- Patobulinta nuo duomenų priklausančių etikečių savybių lango sąsaja ir darbo eiga

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Savybė: pagerintas potencialių projekto failo perrašymų valdymas
QGIS 2.10 įspės, kai bandysite įrašyti projekto failą, kurio paskutinė redakcijos data pasikeitė po projekto įkėlimo. Tai naudinga, kai daugiau nei viena naudotojo sesija atidarė tą patį projekto failą ir abi sesijos bando įrašyti pakeitimus į projekto failą.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Savybė: naujas geometrijos varikliukas
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## Analizės įrankiai
### Savybė: naujas statistinės suvestinės priklijuojamas valdiklis
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Savybė: rastro skaičiuotuve naudokite logaritmines funkcijas
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Savybė: naujos zoninės statistikos savybės
Zoninė statistika leidžia ištraukti akumuliuotas reikšmes iš taškų, esančių po poligonu. Šios savybės buvo pridėtos prie mūsų zoninės statistikos įrankio:
- dabar galite parinkti, kurią statistiką reikia skaičiuoti
- pridėta papildoma statistika (vidurkis, standartinė deviacija, min, maks, diapazonas, mažuma, dauguma ir įvairovė)
- galimybė parinkti rastro juostą, naudojamą statistikos ištraukime

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Naršyklė
### Savybė: naujas naršyklės savybių valdiklis
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Savybė: nauja naršyklės piktograma
QGIS naršyklė - tai atskira nepriklausoma aplikacija, leidžianti naršyti ir peržiūrėti jums prieinamus GIS duomenų rinkinius (iš jūsų failų sistemos, duomenų bazių jungčių, žiniatinklio paslaugų ir t.t.). Ankstesnėse QGIS laidose mes naudojome nedidelę piktogramą, labai panašią į QGIS apllikacijos, dėl ko naudotojai dažnai painiodavosi. Kad sumažintumėm neteisingos aplikacijos paleidimą, mes sukūrėme naują piktogramą QGIS naršyklei.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Duomenų tiekėjai
### Savybė: DXF eksporto patobulinimai
DXF eksportas pastoviai tobulinamas paskutinėse trijose QGIS versijose. Šioje versijoje atsiranda patobulintas SVG arba paprastų žymeklių konvertavimas į DXF blokus, pataisytos kelios klaidos ir problemos, dėl kurių buvo gaunamas nepilnas (neperskaitomas) DXF failas. Nuotraukoje matote pradinį rodinį QGIS'e kairėje, o dešinėje - eksportuoto DXF vaizdą Autodesk TrueView programoje.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Šią savybę finansavo:** Morges, Uster, Vevey ir SIGE bendruomenės

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Savybė: išraiškų filtrai PostGIS tiekėjo pusėje
QGIS 2.10 leidžia filtruoti geoobjektus duomenų bazės pusėje. Tik palaikomos išraiškos bus siunčiamos į duomenų bazę. Išraiškos su nepalaikomais veiksmais arba funkcijomis bus naudojamos vietiniame įvertinime.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

arba

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Duomenų valdymas
### Savybė: virtualius laukus jau galima keisti
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Savybė: eilutės redagavimo automatinis pabaigimas skirtas ValueRelation redagavimo valdikliui
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Savybė: DB tvarkytojo patobulinimai
DB tvarkytojas turi dvi naujas savybes:

**Kuriant sluoksnį kaip užklausą nebereikia unikalaus sveiko skaičiaus stulpelio**

Daugiau nereikia unikalaus sveiko skaičiaus stulpelio, kai kuriate QGIS sluoksnį naudojant SQL užklausą. Tokiu atveju bus naudojamas automatiškai didėjanti skaičių seka.

**Integracija su SQL užklausų kūrėju**

Naujas DB tvarkytojo langas leidžia kurti SQL užklausas naudojant valdiklius, kuriuose lentelių pavadinimai, stulpelių pavadinimai ir funkcijos gali būti parenkamos. Jis atkeltas iš QSpatialite priedo ir veikia su PostGIS ir Spatialite tiekėjais.

**Šias savybes finansavo**: MEDDE (French Ministry of Sustainable Development)

**Šias savybes sukūrė**: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Savybė: filtrų susiejimas pririštų klasifikatorių valdikliui
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagramos
### Savybė: diagramų patobulinimai
QGIS diagramų funkcionalumas leidžia užkelti paprastas skritulines diagramas arba histogramas virš geoobjektų žemėlapyje. Šioje laidoje diagramų funkcionalumas gavo šiuos patobulinimus:
- Diagramas galima išjungti neprarandant nustatymų
- Pridėta parinktis visada rodyti diagramas sluoksniui
- Atnaujinta diagramų naudotojo sąsaja supaprastinant dialogą, dėl ko jis tampa draugiškesnis naudotojui
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Skaitmeninimas
### Savybė: pagerintas geometrijos pasukimo įrankis
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- pasukimo žemėlapio įrankyje dabar galima naudoti skaitmeninę įvestį
- galite naudoti iškrentančius laukus kampų nustatymui
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Užrašai
### Feature: \"Follow point\" alignment for multiline labels
Įjungus šį režimą, etikečių lygiavimas priklauso nuo galutinės etiketės pozicijos taško atžvilgiu. Pavyzdžiui jei etiketė piešiama taško dešinėje, tai etiketė bus lygiuojama pagal dešinį kraštą, o jei ji piešiama taško dešinėje - ji bus lygiuojama pagal kairįjį kraštą. tai stipriai pagerina kelių eilučių etiketes taškų sluoksniuose.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Žemėlapio maketas
### Savybė: mastelio dydžio nustatymo pagal norimą plotį režimas
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programavimas
### Savybė: patobulinimai programuotojams
Mes padarėme keletą pakeitimų ir patobulinimų, kurie bus įdomūs programuotojams:
- Padidinome minimalios Qt4 versijos reikalavimą iki 4.8. Qt4 - tai vienas pagrindinių C++ įrankių rinkinių / bibliotekų, kurios naudojamos kuriant QGIS.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Leidžiama keisti vektorinio sluoksnio duomenų šaltinį.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Serveris
### Savybė: tolerancijos parametro palaikymas WMS GetFeatureInfo užklausose
Naudojant WMS sluoksnius, kuriuos teikia QGIS Serveris, dabar galite nurodyti toleranciją kiek toli nuo paspaudimo vietos veiks GetFeatureInfo užklausos. Tai labai svarbu mobiliems įrenginiams, kur daug sunkiau tiksliai parodyti geoobjektą. Iki šios savybės, buvo beveik neįmanoma identifikuoti tašką arba linijinius geoobjektus mobiliuose įrenginiuose su QGIS serveriu. GetFeatureInfo užklausose galite pridėti šiuos parametrus:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

ir pakeisti tolerancijos reikšmes (taškais), kad jos atitiktų jūsų poreikius.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Simbologija
### Savybė: priderinti kategorijas prie turimų stilių
Kategorizuoto braižymo sudėtingesniame meniu pridėta parinktis nurodyti kategorijas simboliams, kurie atitinka pavadinimą stilių bibliotekoje arba XML stiliaus faile.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Savybė: keisti simbolių dydį naudojant graduotą braižymą
Braižytojai, tai QGIS posistemė, leidžianti kurti sudėtingas kartografines jūsų duomenų pateiktis. Graduotas braižymas keičia simbolį priklausomai nuo pastoviai besikeičiančios reikšmės vektoriniame sluoksnyje. Ankstesnėse QGIS versijose jūs galėjote keisti tik spalvą (pavyzdžiui naudodami spalvų rampą). QGIS 2.10 graduotas simbolio braižymas leidžia keisti ir dydį *arba* spalvą. Taškų sluoksniams jūs galite keisti taško dydį, linijoms jūs galite keisti linijos plotį. Poligonai tebeturi tik galimybę keisti spalvą, linijos plotis vis dar nepalaikomas.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Savybė: nauja parinktis leidžianti išvengti automatinio geoobjektų apkarpymo pagal žemėlapio plotą
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Savybė: dydis ir pasukimas buvo pašalinti iš sudėtingesnio meniu
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Savybė: nuo duomenų priklausančios šrifto žymeklio savybės
Dauguma šrifto žymeklio savybių dabar galima nustatyti pagal duomenis, įskaitant žymeklio dydį, pasukimą ir simbolį.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Savybė: vizualizuokite ir keiskite graduotą braižymą naudodami histogramą
Prie graduoto braižymo pridėta nauja histogramos kortelė, kurioje rodoma interaktyvi priskirto lauko arba išraiškos reikšmių histograma. Naudojant šią histogramą galima perkelti ar pridėti klasių ribas.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Savybė: dydžio, pasukimo ir brėžimo pločio išraiškos simbolisto lygyje
Dydis ir pasukimas gali būti nurodomos išraiška visiems simbolių lygiams, kuriantiems žymeklį. Plotį galima nurodyti išraiška visiems simboliams, kuriantiems liniją.

Simboliams legenda kuriama skirtingiems dydžiams. Tai leidžia kurti daugiavariantinės analizės legendą klasifikuojant/graduojant spalvomis.

Padėjėją su peržiūra galima rasti per duomenų priklausymo mygtuką, jo pagalba galima kurti savo dydžio išraišką. Galimi trys metodai: Flannery, Plotas ir Spindulys.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Savybė: gyvi sluoksnių efektai sluoksniams ir simboliniams sluoksniams
Gyvi sluoksnių efektai - tai dar vienas priedas prie jau didelio rinkinio QGIS kartografinių galimybių. Jie leidžia pridėti įvairius braižymo efektus į braižymo eigą. Naudojant gyvus efektus galite daryti tokius dalykus kaip pridėti šešėlius po jūsų simboliu, ištempti ir iškarpyti braižomą simbolį. Taipogi galite dėlioti šiuos efektus vieną po kitu ir nurodyti, ar efektas turi būti progresinis (t.y. pridėti save prie ligšiolinės braižymo būsenos) arba diskretinis (iš naujo pridedantis pradinę geometriją į braižymo eigą).

**Pastaba**: Šis funkcionalumas skirtas patyrusiems naudotojams ir mes norėtume pastebėti, kad per didelis jo naudojimas gali stipriai sulėtinti braižymą, taigi reikėtų pagalvoti apie skirtingų braižymo profilių naudojimą jūsų sluoksnyje - vieno galutinio aukštos kokybės žemėlapio generavimui ir kito - darbo režimui.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
