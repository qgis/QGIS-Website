---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.10{#changelog210 }
Data lansării: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Cea mai nouă Versiune**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Mulțumiri**

Dorim să le mulțumim dezvoltatorilor, tester-ilor, autorilor documentațiilor și tuturor acelor persoane care, în mod voluntar, au consumat timp și efort (sau au finanțat alte persoane în acest scop).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

În fine, am dori să mulțumim sponsorilor noștri oficiali pentru sprijinul financiar de neprețuit, pe care l-au oferit acestui proiect:
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

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Generalități
### Funcționalitate: Parametrii de îmbinare pot fi editați
De acum, este posibil să editați parametrii îmbinării (cum ar fi prefixul sau coloanele de îmbinare), după crearea îmbinării. Înainte, pentru aceasta trebuia să ștergeți și să recreați întreaga îmbinare.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Funcționalitate: Straturile cu îmbinări pot fi filtrate
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Funcționalitate: Îmbunătățiri generale
Conform listei de mai jos, s-au adus următoarele îmbunătățiri:
- Suport pentru straturile Pointcloud în PostGIS
- Bare de instrumente și pictograme îmbunătățite din widget-urile andocabile, pentru a ocupa mai puțin ecran și pentru un aspect mai bun în OSX
- Îmbunătățiri aduse furnizorului / pluginului GRASS
- S-a adăugat suport pentru scrípturi cu caractere non-latine, în cazul etichetelor curbate
- Îmbunătățiri foarte mari și robuste aduse calculatorului raster și instrumentelor de georeferențiere
-  Îmbunătățiri aduse UI și fluxului de lucru din fereastra proprietăților pentru etichetele definite definite de date

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Funcționalitate: Gestiune îmbunătățită pentru suprascrierea potențială a proiecției proiectului
QGIS 2.10 vă va avertiza acum, la încercarea de a salva proiectul dvs., dacă data ultimei modificări dintr-un proiect încărcat s-a schimbat. Acest lucru este util în cazul în care mai mult de un utilizator, sau de o sesiune, au deschis același fișier de proiect, și ambii încearcă să salveze modificările în fișierul de proiect.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Funcționalitate: Nou motor geometric
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
## Instrumentele de analiză
### Funcționalitate: Un nou widget andocabil, pentru situații statistice
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Funcționalitate: Utilizarea funcțiilor logaritmice din calculatorul raster
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Funcționalitate: Noi funcțiuni de zonare statistică
Statisticile zonale furnizează o modalitate de a extrage valorile agregate pentru pixelii care stau la baza unui poligon. Următoarele funcțiuni noi au fost adăugate instrumentului nostru de statistici zonale:
- puteți selecta de acum statisticile pe care le doriți calculate
- au fost adăugate extra statistici (mediana, deviația standard, min, max, intervalul, minoritatea, majoritatea și varietatea)
- abilitatea de a selecta banda raster care se va utiliza la extragerea statisticilor

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Navigatorul
### Funcționalitate: Un nou widget cu proprietăți pentru navigator
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Funcționalitate: O nouă pictogramă pentru navigator
Navigatorul QGIS este o aplicație separată, independentă, care vă permite să răsfoiți și să vizualizați seturile de date GIS disponibile pentru dvs. (de la sistemul de fișiere, conexiunile bazei de date, conexiunile la serviciile web, etc.) În edițiile anterioare ale QGIS am folosit o pictogramă foarte similară cu cea a aplicației QGIS, care a fost o sursă de confuzie pentru mulți utilizatori. Pentru a reduce probabilitatea de deschidere a cererii greșite, am creat o nouă pictogramă de Navigator QGIS.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Furnizorii de Date
### Funcționalitate: Îmbunătățiri aduse Exportului DXF
Exportul DXF a fost îmbunătățit în mod continuu în ultimile trei versiuni de QGIS. Această versiune introduce un SVG îmbunătățit, conversia marcajelor simple în blocuri DXF, și repararea câtorva erori și probleme care au dus la fișiere DXF incomplete (ilizibile). În captura de ecran, puteți vedea imaginea originală din QGIS în stânga, și fișierul DXF exportat în Autodesk TrueView, în dreapta.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Această funcționalitate a fost finanțată de:** Comunitățile din Morges, Uster, Vevey și SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Funcționalitate: Expresii de filtrare pe partea de server PostGIS
În QGIS 2.10 puteți filtra acum entitățile pe partea serverului de baze de date. Doar expresiile acceptate vor fi transmise în baza de date. Expresiile care utilizează operatori sau funcții neacceptate vor fi eliminați în urma evaluării locale.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

sau

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Gestiunea datelor
### Funcționalitate: Câmpurile virtuale sunt actualizabile
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Funcționalitate: Linie de editare cu auto-completare pentru widget-ul ValueRelation
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Funcționalitate: Îmbunătățiri pentru DB Manager
Există două noi funcțiuni în DB Manager :

**Interogările încărcate sub formă de strat, nu mai au nevoie de o coloană unică, întreagă**

De acum, nu mai este necesară o coloană cu întregi unici, pentru a încărca o interogare SQL ca un strat de QGIS.  În loc, va fi folosită o valoare auto-incrementabilă.

**Integrarea unui constructor de interogări SQL**

În DB Manager o nouă fereastră vă ajută la crearea de interogări SQL, prin intermediul widget-urilor în care numele tabelei, cel al coloanei și funcțiile pot fi selectate de către utilizator. Fereastra a fost portată de la pluginul QSpatialite și lucrează pentru furnizorii PostGIS și Spatialite.

**Aceste funcționalități au fost finanțate de**: MEDDE (Ministerul francez al Dezvoltării Durabile)

**Aceste funcționalități au fost dezvoltate de**: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Funcționalitate: Înlănțuirea filtrelor pentru widgetul de referință a relațiilor
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagrame
### Funcționalitate: Îmbunătățiri aduse diagramei
Funcționalitatea diagramei din QGIS vă permite să suprapuneți mici diagrame plăcintă sau histograme peste entitățile de pe hartă. În această versiune, am adus următoarele îmbunătățiri diagramelor:
- Diagramele pot fi dezactivate fără pierderea setărilor
- Adaugarea casetei de bifare pentru a se arăta întotdeauna diagramele pentru un strat
- Interfața cu utilizatorul a diagramelor a fost refăcută, pentru a simplifica dialogul și pentru a-l face mai ușor de utilizat
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Digitizarea
### Funcționalitate: Instrument îmbunătățit de rotire a geometriei
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- puteți folosi, de acum, intrări numerice în instrumentul de rotire al hărții
- puteți folosi o casetă combinată, pentru a seta unghiurile
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Etichetare
### Feature: \"Follow point\" alignment for multiline labels
Când este setată în acest mod, alinierea textului pentru etichete este dependentă de destinația finală a etichetei în raport cu punctul. De exemplu, dacă eticheta este plasată la stânga punctului atunci eticheta va fi aliniată la dreapta, iar dacă aceasta este situată la dreapta punctului atunci eticheta va fi aliniată la stânga. Acest lucru îmbunătățește foarte mult aspectul etichetei multilinie pentru straturile de tip punct.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Compozitorul de Hărți
### Funcționalitate: S-a introdus modul de dimensionare a scării grafice în scopul încadrării într-o lățime dată
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programabilitate
### Funcționalitate: Îmbunătățiri pentru programatori
S-au adus o serie de schimbări și îmbunătățiri care vor fi de interes pentru dezvoltatori:
- Am mărit cerința minimă pentru Qt4 până la versiunea 4.8. Qt4 este una dintre principalele scule / biblioteci C++ pe care le folosim pentru a crea QGIS.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Se permite schimbarea surselor de date din stratul vectorial.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Server
### Funcționalitate: Suport pentru parametrul de toleranță din cererile WMS GetFeatureInfo
Atunci când se utilizează straturi WMS servite de QGIS Server, puteți specifica o toleranță care să indice cât de departe de originea clicului trebuie luate în considerare cererile GetFeatureInfo. Acest lucru este important pentru dispozitivele mobile, în cazul în care entitățile sunt mai greu de indicat. Înainte de această nouă caracteristică, era practic imposibil să se identifice entitățile de tip punct sau linie caracteristici pe un dispozitiv mobil, în cazul serverului QGIS. Puteți adăuga următorii parametri la solicitarile GetFeatureInfo ale dumneavoastră:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

și modificați valorile toleranței (în pixeli) pentru a se potrivi nevoilor dumneavoastră.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Simbologie
### Funcționalitate: Categorii corespunzătoare stilurilor existente
Adăugarea opțiunilor în meniul avansat de randare clasificată, pentru a stabili categoriile pentru simboluri cu un nume adecvat, din biblioteca de stiluri sau dintr-un fișier de stiluri XML.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Funcționalitate: Diverse dimensiuni pentru simboluri, folosind renderul gradat
Renderele sunt subsisteme ale QGIS care vă permit să creați reprezentări cartografice bogate, pentru datele dvs. Un render gradat prezintă simbologia în funcție de o valoare în continuă schimbare într-un strat vectorial. În versiunile anterioare de QGIS puteați modifica numai culoarea (de exemplu, prin utilizarea unei culori de-a lungul unei game de culori). În QGIS 2.10, randarea gradată a simbolurilor acceptă, de acum, să modificați dimensiunea *sau* culoarea. Pentru straturile de tip punct se poate modifica dimensiunea punctului, iar pentru linii se poate schimba lățimea liniei. Straturile de tip poligon păstrează doar capacitatea de schimbare în funcție de culoare, nefiind posibilă încă, schimbarea în funcție de dimensiunea liniei.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Funcționalitate: O nouă opțiune pentru prevenirea decupării automate a entităților după extinderea hărții
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Funcționalitate: Dimensiunea scării și rotația au fost eliminate din meniul avansat
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Funcționalitate: Proprietăți definite cu ajutorul datelor, pentru fontul marcajului
Cele mai multe proprietăți ale marcajului de tip font pot fi de acum definite cu ajutorul datelor, inclusiv dimensiunea, rotația și caracterul marcajului.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Funcționalitate: Vizualizarea și modificarea renderului gradat folosind o histogramă
O nouă filă pentru histogramă a fost adăugată la renderul gradat, ceea ce arată o histogramă interactivă a valorilor din câmpul sau expresia atribuite. Pauzele între clase pot fi deplasate sau adăugate folosindu-se histograma.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Funcționalitate: Expresii pentru dimensiune, rotație și lățimea-liniei la nivelul listei de simboluri
Dimensiunea și Rotația pot fi definite printr-o expresie pentru toate nivelurile de simboluri care compun un marcaj. Lățimea poate fi definită printr-o expresie, pentru toate simbolurile care compun o linie.

Pentru simboluri, este generată o legendă pentru diverse dimensiuni. Acest lucru permite o legendă pentru analiză multivariată, în cazul culorilor clasificate/gradate.

Un asistent, cu previzualizare, este accesibil prin intermediul butonului de definire a datelor, pentru a ajuta utilizatorul să definească expresia dimensiunii. Sunt disponibile trei metode: Flannery, Area și Radius.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Funcționalitate: Efecte în timp real pentru straturi
Efectele în timp real pentru straturi adaugă capacităților cartografice, deja extinse, ale QGIS, posibilitatea de a introduce diverse efecte în lanțul de randare. Cu aceste efecte puteți face lucruri cum ar fi plasarea unei umbre sub simbolul dvs., deformarea și forfecarea simbolului randat. Puteți aplica, de asemenea, aceste efecte unor straturi suprapuse și să stabiliți dacă efectul ar trebui să fie progresiv (adică, se aplică la starea randată în mod curent) sau discret (prin re-injectarea geometriei sursă înapoi în lanțul de randare).

**Observație**: Aceasta este o funcționalitate pentru utilizatorii avansați, și ar trebui să rețineți că folosirea excesivă a acestei caracteristici poate încetini semnificativ timpul de randare, așa că ar trebui să luați în considerare diferite profiluri de simbologie pentru stratul dvs. - unul pentru generarea de hărți de calitate și altul pentru producerea de schițe.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
