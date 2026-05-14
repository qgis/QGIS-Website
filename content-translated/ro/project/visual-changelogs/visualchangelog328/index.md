---
HasBanner: false
draft: false
releaseDate: '2022-10-21'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 3.28
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 3.28{#changelog328 }
![image1](images/projects/19a3cf4af4fcad7ecec62560b72067b903097054.png)

Data lansării: 2022-10-21

QGIS 3.28 Firenze introduces various feature updates, UX modifications, usability enhancements, and improved integration with various proprietary services and data backends. It is also set to introduce the long-awaited features provided by previous releases into the long-term support release, as outlined in the [QGIS Roadmap](https://www.qgis.org/en/site/getinvolved/development/roadmap.html).

Ecranul introductiv prezintă o extraordinară hartă rară a Florenței, din anul 1847, publicată de italianul Giuseppe Molini. Această hartă, magnific gravată, a fost proiectată inițial în 1731 de către arhitectul florentin Ferdinando Ruggieri. Orientată spre sud, harta acoperă vechiul centru fortificat al Florenței, dispus pe ambele maluri ale râului Arno. În colțul din dreapta sus se află simbolul crinului florentin. Deși tipărită în 1847, harta a fost pregătită în stilul secolului al XVII-lea, prin gravură pe cupru cu ajutorul unei hârtii groase. În 1874, Florența se afla în pragul transformării politice. La un an de la producerea acestei hărți, Marele Duce, răspunzând demonstrațiilor politice din toată Florența, a elaborat prima constituție din Toscana.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://youtu.be/IEkOhQezQMk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/IEkOhQezQMk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea lor financiară sau socială - noi având convingerea că prin aducerea deciziei spațială la îndemâna utilizatorilor vom obține o societate mai bună.

{{<table-of-contents >}}
## Modificări de Compatibilitate
### Funcționalitate: S-a renunțat la compatibilitatea, la nivel de simbologie, pentru proiectele dezvoltate în QGIS 3.16 sau în versiuni mai vechi
Versiunile anterioare ale QGIS introduc cantități semnificative de obiecte de compatibilitate în structura XML a fișierelor proiectelor, pentru a menține compatibilitatea la nivel de simbologie și pentru a permite deschiderea fișierelor proiectelor în QGIS 3.16 și în versiunile mai vechi. Această compatibilitate a fost eliminată, optimizându-se semnificativ structura fișierelor proiect.
## Facilități Temporale
### Funcționalitate: Disponibilitate de management temporal în straturile WMTS care conțin dimensiunea TIME
This enhancement exposes any WMTS \"time\" dimensions for use in the temporal framework, including allowing these layers to be animated and controlled via the temporal controller.

When we do detect a time dimension on a WMTS layer, we no longer expose this in the same way as other non-time dimensions. The browser panel does not show the dimension values, and adding the layer via Data Source Manager no longer prompts the user to pick from the available time values. Instead, these layers are indicated with a new \"time capable raster layer\" icon, and are added to a project without the user specifying a time value.

Just like a WMS(T) layer, when a time-dimension enabled WMTS layer is added to the project, it will default to the \"automatic\" temporal mode, meaning that the layer will follow the temporal controller\'s current time range by default. A user can then opt to show a specific static time value for the layer through the layer\'s Temporal properties page, by unchecking \"Dynamic Temporal Control\" and picking a specific available time range from the \"Predefined date\" option.

Acest lucru ar trebui să unifice experiențele utilizatorului, astfel încât, utilizarea straturilor WMTS cu dimensiunea temporală activată să fie identică cu utilizarea straturilor WMS(T).

![image3](images/entries/8f0a6c8e4850886732633ab76d5873dffd7746c4.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Instrumente De Cartografiere
### Funcționalitate: Este permisă selectarea entităților din straturile de plăcuțe vectoriale
A fost adăugat suport pentru selectarea entităților din straturile de plăcuțe vectoriale, ceea ce permite utilizatorilor să utilizeze instrumentele standard la selectarea interactivă a entităților din aceste surse.

Când într-un strat de plăcuțe vectoriale există o selecție, atunci un utilizator poate:
- Să copieze entitățile și să le insereze în straturile existente sau într-un strat temporar
- Use other (non-editing) tools which operate on selections, such as \"zoom to selected features\"/\"pan to selected features\"

Selecțiile pot fi făcute cu ajutorul oricăruia dintre instrumentele de selecție interactive bazate pe hărți, de ex.: selectarea după un dreptunghi, selectarea liberă, după un poligon sau după o rază. De asemenea, sunt valabile toate comenzile rapide care se aplică la adăugarea/scăderea/intersectarea selecțiilor vectoriale.

Selectarea entităților se realizează utilizând nivelul de zoom al plăcuței de pe canevas pânzei, entitățile selectate la acest nivel de zoom persistând, chiar dacă utilizatorul schimbă scara la un alt nivel de zoom al plăcuțelor vectoriale. Aceasta înseamnă că un utilizator poate mări și selecta o entitate mică/detaliată, apoi o poate micșora, văzând în continuare entitatea selectată pe hartă.

Această funcționalitate a fost finanțată de Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Interfața cu Utilizatorul
### Funcționalitate: Fereastră bazată exclusiv pe UX pentru managerul surselor de date
The data source manager dialog is now ALWAYS non modal, and options to set it as such have been removed. The dialog now functions just like other \"manager\" type windows in QGIS, such as the style manager or layout manager.

Managerul sursei de date va fi tratat, în schimb, ca și propria fereastră, care este adusă în prim-plan ori de câte ori este apăsat butonul Managerului Surselor de Date.

![image4](images/entries/9bbc312e9b1362ae660a9719c910ab209d3e8a55.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Funcționalitate: S-a adăugat acțiunea de Afișare în Tabela de Atribute în meniul contextual al simbolurilor clasificate dintr-o legendă
A new \"Show in Attribute Table\" action has been added to the right-click context menu of legend class symbols in the table of contents. This allows users to open the attribute table with a filter applied to match only the features relevant to a particular symbol group. This provides a significant performance improvement for certain datasets, such as large vector layers loaded from a remote source.

![image5](images/entries/8b43481bcab479b040b0a5ac5400ddc89c77dd0a.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Funcționalitate: S-a adăugat o setare pentru a omite valorile NULL din rezultatele identificării
The \"Identify Features\" utility now provides the capability to hide NULL values from the returned results

![image6](images/entries/f0c7217db5f0104999a3d87c2229010dcc62cb50.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Simbologie
### Funcționalitate: Este permis controlul asupra marcajului locației GPS
A fost introdusă o nouă pagină cu opțiuni generale GPS, care include setări pentru controlul marcajului utilizat pentru locația GPS curentă, oferindu-i și posibilitatea de a fi rotit pentru a se potrivi cu direcția GPS.

![image7](images/entries/411b2d3b0f1b180857eda6d4e0c73144f1aeee57.gif)

Această funcționalitate a fost finanțată de Tiwi Resources, Bush Heritage, Australian Wildlife Conservancy

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Funcționalitate: S-au adăugat noi forme pentru marcajele poligonale
Simbolurile pentru tipul de marcaj poligonal includ de acum următoarele forme suplimentare:
- Pentagon
- Hexagon
- Octogon
- O Treime de Cerc
- Un Sfert de Cerc
- Stea

![image8](images/entries/3e749b405f10a24f95665cd0ad3e1ea0f199811b.webp)

Această funcționalitate a fost finanțată de North Road

This feature was developed by [ZayneTomlins](https://github.com/ZayneTomlins)
## Etichetare
### Funcționalitate: La etichetarea prin intermediul codului HTML s-a introdus suport pentru stilul, dimensiunea și familia fonturilor
S-a adăugat suport pentru taguri de formatare HTML suplimentare, disponibile în cadrul etichetării (și oriunde se mai procesează textul).

Din tagurile permise enumerăm:
- familia fontului
- mărimea fontului
- îngroșare
- înclinare

![image9](images/entries/b49f780e98b4276b76cf3022b34da26dd4ed9d1f.webp)

Această funcționalitate a fost finanțată de Grupul Utilizatorilor Elvețieni de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Funcționalitate: S-a adăugat opțiunea de utilizare a unităților absolute pentru înălțimea liniei
Anterior, înălțimea liniei era setată în multipli ai distanței dintre liniile textului, însă, de acum este posibilă utilizarea unităților absolute pentru înălțimea liniei (lucru util atunci când se utilizează dimensiuni mixte de text în cadrul unui singur document).

![image10](images/entries/b413c593933bc197886a97919ae015880e119aa7.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Suprafața poliedrică
### Funcționalitate: S-a adăugat opțiunea de reîncărcare a proprietăților temporale ale straturilor cu suprafețe poliedrice
An \"Always take reference time from data source\" option has been added for mesh layers that when checked, will ensure that the reference time is reloaded from the data source, and each time the layer is reloaded or the project reopened the time properties will be updated from the file automatically.

In previous releases, when a mesh layer file had a reference time and time extent that changed, the time layer properties would not be updated when the projector layer are reloaded, and the user would be required to manually navigate to the \"Reload from provider\" feature in the temporal tab of the layer properties.

![image11](images/entries/8bf480abed6701e5535110f8069ba1f63ecf2de4.gif)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
## Funcționalități 3D
### Funcționalitate: Efectul de Ocluzie Ambientală 3D
Un nou efect de ocluzie ambientală este disponibil pentru randarea datelor în vizualizări 3D, îmbunătățind astfel percepția  profunzimii datelor în 3D. Acesta este un efect de post-procesare și, în scopul obținerii unor rezultate destul de interesante, poate fi chiar combinat cu iluminarea eye dome (EDL). O definiție simplificată excesiv a efectului spune că entitățile care nu sunt vizibile pentru cameră sunt folosite pentru a textura și a întuneca elementele învecinate, cu avantajul îmbunătățirii contrastului, definiției și diferențierii.

În meniul de configurare a vizualizărilor 3D s-a introdus un nou element pentru controlul stării de ocluzie ambientală. De asemenea, au apărut parametri suplimentari în secțiunea de configurare avansată, care oferă un control fin asupra:
- Razei: pragul distanței până la care se calculează ocluzia ambientală
- Intensității: puterea efectului (valorile mai mari fac lucrurile mai întunecate)
- Pragului ocluziei: numărul de puncte învecinate care trebuie să fie ocluse pentru ca efectul să apară (valorile mai mici de 50% vor întuneca ieșirea, dar, probabil, vor oferi un interval mai larg de ocluzie)

![image12](images/entries/996b020346252bc10d87279d9e0cac766802c1d4.webp)

This feature was developed by [Martin Dobias & Belgacem Nedjima](https://github.com/wonder-sk)
## Nori de Puncte
### Funcționalitate: Exportare Straturi cu Nori de Puncte
De acum, straturile cu nori de puncte acceptă exportarea în formate vectoriale sau specifice norilor de puncte, cu filtrare opțională.

Formatele acceptate includ:
- Strat temporar (strat de memorie)
- GeoPackage
- Fișier shape
- DXF
- LAZ (requires build WITH_PDAL)
- Fișiere LAS necomprimate

Operațiunile de export acceptă:
- Filtrarea după extindere
- Filtrarea după Intervalul Z
- Limitarea numărului de puncte exportate
- Filtrarea spațială după stratul poligonal

În plus, sunt acceptate definirea și reproiectarea CRS-ului de ieșire.

![image13](images/entries/9b7102f1bbd9286c16285a43158904395e56c4bc.webp)

Această funcționalitate a fost finanțată de Ținutul Vorarlberg și Grupul Utilizatorilor Elvețieni de QGIS

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Funcționalitate: Iluminare Eye Dome pentru norii de puncte  de pe canevasul hărții 2D
Efectul de iluminare Eye Dome este disponibil, de acum, pentru norii de puncte din renderele 2D

![image14](images/entries/99c16bf2efe3bdcf020a41ad088e29ec7437573e.webp)

This feature was developed by [Nedjima Belgacem](https://github.com/NEDJIMAbelgacem)
## Compoziții Cartografice
### Feature: Add FORCE_RASTER and IMAGE_COMPRESSION parameters to PDF algorithms
The `FORCE_RASTER` and `IMAGE_COMPRESSION` parameters have been added to the various \"Export print layout as PDF\" algorithms, including support for Atlas and multifile exports.

`FORCE_RASTER` is mutually exclusive with and takes precedence over the `FORCE_VECTOR` parameter.

![image15](images/entries/06cc045f6a69f9caaacde8f8b3ead9e89f02af22.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Expresii
### Funcționalitate: S-a adăugat un nou stil pentru variabilele  care fac referire la entitatea curentă în cadrul funcțiilor
Variabilele de stil nou au fost adăugate pentru referențierea entității curente și a atributelor sale în expresii.

Noile variabilele introduse sunt:
- `@feature`: a replacement for \$currentfeature, contains the current feature
- `@id`: a replacement for \$id, contains the current feature id
- `@geometry`: a replacement for \$geometry, contains the current feature geometry

This is a step towards eventually deprecating the older `$` style functions, and providing a more consistent approach to expressions instead of an unpredictable mix of `@`/`$`.

Funcțiile mai vechi și referințele variabilelor vor continua să funcționeze (și probabil vor continua să funcționeze pe termen nelimitat, pentru a asigura compatibilitatea cu proiectele mai vechi). De asemenea, vor continua (deocamdată) să fie expuse în UI, pentru evitarea confuziilor.

![image16](images/entries/b9666dee9322ba767162310e6958503e639d1148.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add new shared_paths function
A new `shared_paths` function has been added which returns a collection containing paths shared by the two input geometries. Those going in the same direction are in the first element of the collection, and those going in the opposite direction are in the second element. The paths themselves are given in the direction of the first geometry.

![image17](images/entries/f02946a8f1e45527366c30e6d0ea5a4947c7f86a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Make_valid and geom_to_array functions
Au fost adăugate funcții suplimentare pentru:
- `make_valid`: Repair broken input geometries and returns the corrected geometries
- `geometries_to_array`: This converts a geometry collection into an array for easier handling and iteration

![image18](images/entries/bc2bbd8d26e2ebb4fd7dc02f0ce7ec6460f3a3bc.webp)

This feature was developed by [Alex](https://github.com/roya0045)
### Funcționalitate: Funcția Anvelopă Concavă
A new `concave_hull` function is now available in QGIS expressions (GEOS 3.11+)

![image19](images/entries/e434b7356dc93f9c43fa3142c7f8f914a4aa5615.webp)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Funcționalitate: Solicitare confirmare la momentul renunțării la modificările expresiei
A new confirmation dialog is now safeguarding users against accidentally discarding their unapplied changes in expression editor dialogs. This safeguard is used in the Expression String Builder, the Expression Dialog (Epsilon icon, e. g. for Geometry Generators or for Pre-calculated Values in the model builder) and the Expression Based Filter (Attribute Table -\> Advanced filter expression).

![image36](images/entries/cebe844ae2c28045a8b6e2e89cb2b40cdbbd38c6.webp)

This feature was funded by [WhereGroup GmbH](https://wheregroup.com/)

This feature was developed by [Johannes Kröger](https://github.com/kannes)
## Gestiunea Datelor
### Funcționalitate: Cerere confirmare la momentul ștergerii entităților
Pentru a reduce și mai mult riscurile de ștergere accidentală a entităților, în mod implicit, un nou dialog de confirmare apare atunci când utilizatorii efectuează activități care ar putea șterge înregistrări, cum ar fi utilizarea tastei DEL sau anumite acțiuni din bara de instrumente. În plus, numărul de entități este inclus în mesajul ferestrei de dialog (fiind, de asemenea, afișat în bara de titlu), ceea ce face ca avertismentul să fie mai clar pentru utilizatori.

In previous releases, similar confirmation prompts would only be displayed when some features fell out of the extent of the map canvas, or the deletion triggered the removal of child relation features. The new behavior is for the prompt to be enabled by default and disabled by using the \"Don\'t show this message again\" checkbox.

![image20](images/entries/677952561ec24d417a74cf46842a6c52aec49587.webp)

This feature was funded by [QGIS user group Switzerland](https://www.qgis.ch/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Metadate și Metacăutare
### Funcționalitate: Căutarea și stocarea furnizorului de date pentru metadatele stratului
Implementation of elements from the [QEP #250 \"Database metadata storage\"](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/250) initiative have been completed and this functionality includes the creation of a new layer metadata API and GUI components.

Următorii furnizori/formate de date sunt pot stoca și gestiona metadatele stratului în QGIS:
- GPKG (deja implementat, tocmai s-a inclus în noul API)
- Postgres
- Postgres Raster

În plus, o nouă filă de căutare a metadatelor stratului este disponibilă în managerul sursei de date, iar o căutare interactivă a metadatelor stratului este disponibilă prin intermediul locatorului QGIS.

![image21](images/entries/17fc26636b3c1fe423ec8f715e69365495519add.webp)

Această funcționalitate a fost finanțată de ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Procesare
### Funcționalitate: Suport pentru precizie fixă în anumite instrumente de procesare
A new advanced parameter is available for some processing tools which allows the use of the [fixed precision](https://blog.cleverelephant.ca/2020/12/waiting-postgis-31-3.html#fixed-precision-overlay) parameter provided by GEOS \>= 3.9.0. This parameter is listed under advanced parameters as \"Grid Size\" and is currently supported in the following tools:
- Suprapunere
- Intersecție
- Diferență
- Diferență Simetrică
- Unificare

![image22](images/entries/b2ef315dc1013852d3316023c62af5ff06626e93.webp)

Această funcționalitate a fost finanțată de Orange Telecom FR

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: Improved \"Make Valid\" Algorithms
QGIS poate folosi de acum metodele mai noi, rafinate GEOS 3.10+, pentru validarea și repararea entităților cu geometrie.

![image23](images/entries/4b320e5bad078f1a0eb23fe958d86e330b08c10e.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Funcționalitate: Opțiune implicită de afișare a numărului de entități pentru ieșirile vectoriale ale procesării
A new `Show feature count for output vector layers` setting is available (but disabled by default for performance reasons), which will automatically enable the \"show feature count\" option on output layers loaded from QGIS processing. This is able to give users a first glimpse of what to expect as an output from a Processing algorithm.

![image24](images/entries/e804b2accbcf155f4db2ea4024bd89ed5883097f.webp)

This feature was developed by [Germap](https://github.com/gacarrillor)
### Funcționalitate: S-a adăugat opțiunea de export a relațiilor în algoritmul de împachetare a straturilor
The \"Package Layers\" processing tool now supports optionally following project relations and exporting related tables following the hierarchy both upstream and downstream, whilst also taking selected features into account.

![image25](images/entries/26076b13de92a8ac2a1fea1511e03776c1aeae13.webp)

Această funcționalitate a fost finanțată de ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add \"Offset\" parameter to \"Drape\" algorithms
Adds the \"Offset\" parameter to the \"Drape (set Z value from raster)\" and \"Set M value from raster\" algorithms. The \"Offset\" value is algebraically added to the band values after applying the \"Scale factor\".

![image26](images/entries/78e9cb5b82c872604fc3616c2c7b3772e7d26bef.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Opțiunile Aplicației și ale Proiectului
### Funcționalitate: Setări de afișare a coordonatelor modificate ale proiectului și ale azimutului
Opțiunile de afișare a coordonatelor și azimutului din setările proiectului au fost actualizate în conformitate cu următoarele:
- Unități de hartă (comportamentul este similar cu cel din versiunile anterioare)
- Map Geographic (modified behavior)
- Custom Projection Units (new type)

The legacy Geographic (Latitude/ Longitude) option would display values in the map CRS coordinates *if* the CRS was geographic, otherwise, it would transform coordinates to a hard-coded WGS84 CRS value.

The updated Map Geographic (degrees) option, which supersedes the legacy approach, will display values in the map CRS coordinates *if* the CRS is geographic, however in instances where it is not, the internal `QgsCoordinateReferenceSystem::toGeographicCrs()` API will be used to transform the coordinates into the map CRS\' associated geographic CRS. This is helpful in various contexts, such as when analyzing non-earth celestial bodies.

The Custom Projection Units type is a new addition that defaults to WGS84 and allows users to set any CRS they desire as display coordinates.

![image27](images/entries/7af6704f72373fec3c1e9c212366fd3d8cfa0218.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add support for \"user\" fonts, and automatic downloading of freely licensed fonts
A new \"Fonts\" panel has been added to the settings dialog, which provides support for the following functionalities:
- The ability for users to populate a list of automatic font replacements to apply when loading projects or styles, allowing better support for projects and styles to be used across different operating systems (e.g. replace \"Arial\" with \"Helvetica\").
- Users can now place TTF or OTF fonts in the \"fonts\" subfolder of their user profile. These fonts will automatically be loaded at QGIS startup time. This provides a way for users to use fonts without requiring them to be installed on an operating system level, which is often blocked in enterprise environments. The Fonts setting panel lists all installed user fonts and allows users to manage (i.e. remove) previously installed user fonts
- An API is provided for other tools, such as plugins and other clients, to specify additional user font folders which should be scanned during QGIS startup
- Automatic downloading of missing fonts is now supported in certain circumstances. If a user opens a project or style, or they try to load a vector tile layer that references fonts that aren\'t currently available, then a hard-coded list of freely licensed fonts to download via URL is consulted to determine whether it\'s possible to automatically download the font to the user font directory (and notify the user of the font license). A setting to opt out of this behavior is provided in the Fonts panel if so desired.

![image28](images/entries/77e17395ccb70e466ad4c5a80675ad0ff8ec070e.gif)

Această funcționalitate a fost finanțată de Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Navigatorul
### Feature: Implement relationship discovery for OGR layers, and show relationships in browser
The Project Properties → Relations → Discover Relations feature is now able to support OGR layers that support relationships, such GeoPackage (via the related tables extension) and ESRI FileGeodatabases.

The QGIS Browser Panel now includes the ability to show detailed relationship information for these data sources.

![image29](images/entries/11c3f493eff806b4eccbf9af27c96894ea3223a3.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Modified UX for Geopackage and ESRI File Geodatabase creation
A \"New ESRI File Geodatabase\" action has been added to the QGIS Browser right-click context menu on directories, and a new \"vacuum\" action is available for GDB files. (requires GDAL 3.6+)

Additionally, creating a new Geopackage from the same menu will now immediately create an empty GPKG, rather than the legacy behavior of opening a table creation dialog by default (and requiring table creation or users to input dummy data).

<https://user-images.githubusercontent.com/1829991/178902332-0e112e73-0140-45b9-84bf-fc7875cb7b98.gif>

![image30](images/entries/7a0e8f73e24aa061244e30d6bf1b8154e5eebce4.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Allow drag and drop of vector layers to non-GPKG OGR database datasets
QGIS now allows drag and drop of vector layers between OGR database datasets that are not stored in GPKG format, for instance, the dragging of a layer onto a GDB to import that dataset into the geodatabase

![image31](images/entries/c1c17d31db79a4beaab864daf13257e6e7ed0ba0.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Expose field domain management for non-gpkg OGR sources
Navigatorul QGIS acceptă de acum funcționalități mai avansate pentru bazele de date OGR care nu au formatul GPKG, inclusiv capabilități de gestionare a domeniilor câmpurilor (creare și listare de domenii) și crearea tabelelor. Aceasta înseamnă că, prin intermediul interfeței QGIS Browser, utilizatorii pot gestiona domeniile câmpurilor și pot crea noile tabele într-o bază de date ESRI FileGeodatabase existentă.

![image32](images/entries/cc1f815593c28352dffaad020061004db91f8ded.webp)

Această funcționalitate a fost finanțată de Provincie Gelderland

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Furnizorii de Date
### Feature: Define session role for PostgreSQL connections
A `session_role` setting can now be specified for PostgreSQL connections to set the user identifier of the active SQL session. Permissions checking for SQL commands are then carried out with the associated named role.

This is highly useful in instances where it is desirable to automatically give ownership of new objects (Tables/ Views/ Functions etc.) to the `session_role` group, and share ownership and the associated rights with all members of the `session_role` group.

The specified `session_role` must be a role that the current session user is a member of, or if the session user is a superuser, any role can be selected.

This feature was funded by [3liz](https://3liz.com/)

This feature was developed by [rldhont](https://github.com/rldhont)
### Feature: Automatically add related tables when adding layers from GDAL datasets with embedded relationship information
For GDAL data formats with embedded relationship information, whenever a table is added QGIS is now able to discover relationships and immediately add all the related tables to the current project (if they don\'t already exist). Additionally, when adding these related layers QGIS will automatically configure the corresponding QGIS relationships.

This works for all formats which support the GDAL relationship API, which include:
- Geopackage (via the related tables extension)
- ESRI FileGDB/ OpenFileGDB
- ESRI Personal Geodatabase
- Formatele SQLite/ Spatialite.

Această funcționalitate a fost finanțată de Universitatea din Uppsala

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add subset string (filter) support for arcgis REST layers
This can **greatly** improve the performance on large layers!

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Abstract database provider for renaming fields
A `QgsAbstractDatabaseProviderConnection` interface has been added for supporting renaming fields, and implemented for OGR connections along with the ability to rename existing fields for supported database connections via the QGIS Browser interface.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: WFS performing binary spatial operations in expressions on server
QGIS used to be able to perform the expression filters of binary spatial operations on the server when the geometry was provided as WKT or in the GML format. This change converts the geometry from being a static variable in the expression to an OGC filter. The WFS URL is then created by combining a bounding box rectangle, layer filter, and the filtering expression.

A feature request computes the expression in advance to find out if it can be performed on the server, then it\'s stored in `QgsBackgroundCachedSharedData` where a new download is triggered.

When a filter request is not a pure binary spatial operation, it will not be evaluated on the server.

Această funcționalitate a fost finanțată de Cantonul Schaffhausen

This feature was developed by [signedav](https://github.com/signedav)
### Feature: Editing ArcGIS REST Layers
QGIS now supports the editing of ArcGIS feature server layers, such as those hosted on ArcGIS online. Assuming the user has appropriate permissions granted for editing a layer, it will unlock the ability to use the native QGIS tools to edit that layer. These changes include support for the following operations:
- Deleting features
- Adding new features
- Curved geometries (only supported for enterprise ArcGIS server, as [ArcGIS online currently has no support for curves](https://support.esri.com/en/technical-article/000014684))
- Modifying existing features
- Modifying attributes (creating fields, deleting fields, creating attribute indexes)

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Load raster sublayers from vector tile styles automatically
When loading a new vector tile source into a project, if the associated MapBox GL style includes any raster sublayers, then also load those into the project with converted styles.

Fixes <https://github.com/qgis/QGIS/issues/46593>

![Peek 2022-06-20 12-31](https://user-images.githubusercontent.com/1829991/174514930-77887a1d-4679-49a2-9ff0-7c360bc0fc01.gif)

Această funcționalitate a fost finanțată de Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add WMS layers individually
In previous releases, the selection of layers from WMS Servers would be loaded into QGIS as a single project layer. This new functionality provides an optional checkbox to load each of the selected WMS layers into QGIS as distinct project layers.

![image34](images/entries/2685710315d58fc03e1557e3381a41fdd8eb5a02.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Feature: Save projects to Oracle Database Provider
QGIS now supports saving projects to Oracle databases.

![image35](images/entries/6a575714dfc905211f3518a4f5f3803c32e8afa9.webp)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## QGIS Server
### Feature: QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS settings variable
This new feature allows specifying extra tokens which may be used for a WMS FILTER definition. The current list of accepted tokens is rather small and this setting will allow system administrators to easily enlarge the list of allowed tokens.

Această funcționalitate a fost finanțată de Zweckverband Grevesmühlen

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Open layers in a read only mode with QGIS Server
A new `QGIS_SERVER_FORCE_READONLY_LAYERS` environment variable to force QGIS Server to open layers in read-only mode.

This includes various underlying API changes to support read-only configuration for data provider construction, project structure, and layer properties.

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [rldhont](https://github.com/rldhont)
## Plugin-urile
### Feature: Changes to plugin automatic updates behaviour
This change moves the old `app/plugin_installer/checkOnStart` setting key to a new `plugins/automatically-check-for-updates` key, and switches the default value to enable automatic checks.

This is designed to switch all existing QGIS users to the new default behavior of checking for plugin updates at startup (at a maximum of once every 3 days).

It is intended to offer a better QGIS experience to our users, by proactively informing all users when plugins should be updated, ensuring that ALL users are more likely to upgrade plugins and get the bug fixes for plugins promptly.

**Enterprise users who have customised this setting in their deployments will need to adapt their scripts for the new setting key.**

Additionally, the option to control the number of days between plugin startup checks has been removed and is hardcoded at 3 days.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Programabilitate
### Feature: Add temporal handling to maps in QGIS Quick
A new implementation has been added to allow the Canvas and Map Settings in [QGIS Quick](https://api.qgis.org/api/qgsquick.html) to handle temporal functionality.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Addition of py-args command line parameter
When running QGIS from the command line with the `--code` parameter, a new `--py-args` utility allows the passing of arguments to the python interpreter.

Arguments between `--py-args` and `--` are passed to the python interpreter and ignored by QGIS, so for example, when using the following command:

    qgis --code /home/user/example.py --py-args --specialScriptArguments "arg1" 'arg2' -- layer1 layer2
    
The `example.py` script will have `--specialScriptArguments`, `arg1`, and `arg2` passed as system arguments to the python interpreter, whilst `layer1` and `layer2` will be handled by QGIS normally and loaded as map layers

Această funcționalitate a fost finanțată de Oficiul de Stat pentru Topografie și Geoinformații din Vorarlberg

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Corecții Importante
### Funcționalitate: Corecții efectuate de Alessandro Pasotti
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GetPrint request of Atlas Template doesn\'t respect Project scales | [#49900](https://github.com/qgis/QGIS/issues/49900) | [PR #50199](https://github.com/qgis/QGIS/pull/50199) | [PR #50214](https://github.com/qgis/QGIS/pull/50214) |
| Attribute Table Integer entries not showing due to window size | [#50181](https://github.com/qgis/QGIS/issues/50181) | [PR #50201](https://github.com/qgis/QGIS/pull/50201) | Nerecomandat |
| WFS3 collections field name/displayName mix in request/response | [#49399](https://github.com/qgis/QGIS/issues/49399) | [PR #50203](https://github.com/qgis/QGIS/pull/50203) | Nerecomandat |
| QGIS Server WMS GetFeatureInfo does not evaluate represent_value expression in maptip | [#30719](https://github.com/qgis/QGIS/issues/30719) | [PR #50216](https://github.com/qgis/QGIS/pull/50216) | [PR #50223](https://github.com/qgis/QGIS/pull/50223) |
| \"evaluate default value on providers side\" block insert on table in the schema with autoincrement | [#50168](https://github.com/qgis/QGIS/issues/50168) | [PR #50230](https://github.com/qgis/QGIS/pull/50230) | [PR #50333](https://github.com/qgis/QGIS/pull/50333) |
| QGIS not responding when entering page size using custom width or height fields | [#50104](https://github.com/qgis/QGIS/issues/50104) | Nu se poate reproduce |  |
| \"Add Directory\...\" inputs files from previous selected directory at first instance, then the corret. | [#50055](https://github.com/qgis/QGIS/issues/50055) | [PR #50232](https://github.com/qgis/QGIS/pull/50232) | [PR #50241](https://github.com/qgis/QGIS/pull/50241) |
| Layer style panel and Layer panel do not show same visibility settings for layer style | [#49998](https://github.com/qgis/QGIS/issues/49998) | Nu se poate reproduce |  |
| Crash while opening Options dialog after switching locale | [#50239](https://github.com/qgis/QGIS/issues/50239)9 | [PR #50263](https://github.com/qgis/QGIS/pull/50263) | Nu este necesar |
| eroare API de conexiuni MSSQL neraportată | Neraportată | [PR #50194](https://github.com/qgis/QGIS/pull/50194) | [PR #50454](https://github.com/qgis/QGIS/pull/50454) |
| Identify and select tools don\'t work with geometry-based query layers | [#50242](https://github.com/qgis/QGIS/issues/50242) | Nu se poate reproduce |  |
| Problemă cu reîncărcarea fișierului SLD în QGIS | [#50152](https://github.com/qgis/QGIS/issues/50152) | [PR #50266](https://github.com/qgis/QGIS/pull/50266) | queued |
| Algoritm splitwithlines cu execuție infinită, neraportat  | Neraportată | [PR #50279](https://github.com/qgis/QGIS/pull/50279) | Nerecomandat |
| Processing algorithm \"Split with lines\" does not split polygon | [#50227](https://github.com/qgis/QGIS/issues/50227) | Nu este o eroare |  |
| Expression do not split string in multiple lines | [#49666](https://github.com/qgis/QGIS/issues/49666) | [PR #50295](https://github.com/qgis/QGIS/pull/50295) | [PR #50455](https://github.com/qgis/QGIS/pull/50455) |
| Problem with exportation of complex SLD | [#42348](https://github.com/qgis/QGIS/issues/42348) | [PR #50342](https://github.com/qgis/QGIS/pull/50342) | [PR #50354](https://github.com/qgis/QGIS/pull/50354) |
| Wrong interpretation of SLD color opacity | [#44657](https://github.com/qgis/QGIS/issues/44657) | Nu este o eroare |  |
| Wrong label size for SLD export/import | [#35561](https://github.com/qgis/QGIS/issues/35561) | [PR #50347](https://github.com/qgis/QGIS/pull/50347) | Nu este necesar |
| Exporting SLD doesnt include fill-opacity | [#33376](https://github.com/qgis/QGIS/issues/33376) | [PR #50349](https://github.com/qgis/QGIS/pull/50349) | [PR #50436](https://github.com/qgis/QGIS/pull/50436) |
| SpatiaLite - Added feature vanishes, attribute dialog does not show required fields | [#50523](https://github.com/qgis/QGIS/issues/50523) | [PR #50573](https://github.com/qgis/QGIS/pull/50573) | queued |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Funcționalitate: Corecții efectuate de Even Rouault
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Not appropriate |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Nu este necesar |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Neraportată | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Not appropriate |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Neraportată | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Nu este necesar |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328)Bug Title |
| \-- | \-- | \-- | \-- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Not appropriate |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Nu este necesar |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Neraportată | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Not appropriate |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Neraportată | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Nu este necesar |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Funcționalitate: Corecții efectuate de Julien Cabieces
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS not retrieving sequence from postgis in 3.26 | [#49463](https://github.com/qgis/QGIS/issues/49463) | [PR #50247](https://github.com/qgis/QGIS/pull/50247) | no need to bp |
| SVG is not rendered for SVG Marker symbol | [#50208](https://github.com/qgis/QGIS/issues/50208) | Nu se poate rezolva, problemă de Qt |  |
| If \"estimated metadata\" option is checked, feature count for tables/postgis do not work | [#46790](https://github.com/qgis/QGIS/issues/46790) | [PR #50256](https://github.com/qgis/QGIS/pull/50256) | [PR #50425](https://github.com/qgis/QGIS/pull/50425) |
| Variable raster image source in composer not working | [#47981](https://github.com/qgis/QGIS/issues/47981) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Print Layout Picture Box reverting to SVG | [#38031](https://github.com/qgis/QGIS/issues/38031) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Layout picture can not change SVG image to Raster image | [#37804](https://github.com/qgis/QGIS/issues/37804) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| QgsOptionsPageWidget - helpKey and helpSearchPath are not working | [#49421](https://github.com/qgis/QGIS/issues/49421) | [PR #50282](https://github.com/qgis/QGIS/pull/50282) | [PR #50330](https://github.com/qgis/QGIS/pull/50330) |
| Freeze when opening WFS attribute table from HTTPS server with SSL exception | [#42615](https://github.com/qgis/QGIS/issues/42615) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | no bp |
| News feed not loading when using MSI installer | [#49097](https://github.com/qgis/QGIS/issues/49097) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | no bp |
| .ci/run_tests.sh: test_core_networkaccessmanager (Timeout) | [#50234](https://github.com/qgis/QGIS/issues/50234) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) |  |
| SVG Symbol on newer version of QGIS (3.22.7/8/10 tested) make the software lag a lot (and not on 3.4 version). | [#49818](https://github.com/qgis/QGIS/issues/49818) | Feedback, not sure it's a bug |  |
| Empty Options drop-down menu in Query Logger tab | [#50403](https://github.com/qgis/QGIS/issues/50403) | [PR #50527](https://github.com/qgis/QGIS/pull/50527) | no bp |
| Build fails with WITH_POSTGRESQL=OFF | [#50075](https://github.com/qgis/QGIS/issues/50075) | Feedback |  |
| Build fails with WITH_GSL=OFF | [#50076](https://github.com/qgis/QGIS/issues/50076) | [PR #50555](https://github.com/qgis/QGIS/pull/50555) |  |
| QGIS master exports out of bounds in layout | [#48624](https://github.com/qgis/QGIS/issues/48624) | Nu se poate rezolva, problemă de Qt |  |
| Layout bleeding to edge outside map window | [#49638](https://github.com/qgis/QGIS/issues/49638) | Nu se poate rezolva, problemă de Qt |  |
| Freeze with virtual field on \$area used as parameter in sum | [#49589](https://github.com/qgis/QGIS/issues/49589) | [PR #50533](https://github.com/qgis/QGIS/pull/50533) | [PR #50565](https://github.com/qgis/QGIS/pull/50565) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Funcționalitate: Corecții efectuate de Paul Blottiere
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server WFS 1.1.0 GetFeature response - properties with xsi:nil=\"true\" | [#45243](https://github.com/qgis/QGIS/issues/45243) | [PR #50495](https://github.com/qgis/QGIS/pull/50495) |  |
| Cannot move labels | [#47542](https://github.com/qgis/QGIS/issues/47542) | Nu se poate reproduce |  |
| Auxiliary storage and removed layers | [#44667](https://github.com/qgis/QGIS/issues/44667) | [PR #50479](https://github.com/qgis/QGIS/pull/50479) | Nerecomandat |
| OPACITIES parameter not handled with Vector Tile layer in GetMap/GetPrint | [#50364](https://github.com/qgis/QGIS/issues/50364) | [PR #50374](https://github.com/qgis/QGIS/pull/50374) | [PR #50539](https://github.com/qgis/QGIS/pull/50539) |
| Fixes log messages when a job error is not related to a specific layer | Neraportată | [PR #50372](https://github.com/qgis/QGIS/pull/50372) | Nu este necesar |
| Labels: Data defined override of \"Show Label\" always wants the auxiliary storage option | [#47993](https://github.com/qgis/QGIS/issues/47993) | [PR #50496](https://github.com/qgis/QGIS/pull/50496) | [PR #50538](https://github.com/qgis/QGIS/pull/50538) |
| Auxiliary storage rotation or offset fields for symbols are visible by default while labels are not | [#28548](https://github.com/qgis/QGIS/issues/28548) | [PR #50498](https://github.com/qgis/QGIS/pull/50498) |  |
| Improve selection of PostGIS raster overviews | Neraportată | [PR #50554](https://github.com/qgis/QGIS/pull/50554) | [PR #50575](https://github.com/qgis/QGIS/pull/50575) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Funcționalitate: Corecții efectuate de Sandro Santilli
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with offline-editing-core-plugin converting to offline project layer with empty polygon | [#50466](https://github.com/qgis/QGIS/issues/50466) | [PR #50577](https://github.com/qgis/QGIS/pull/50577) |  |
| Cleanup temporary python test config path when requested | [#48884](https://github.com/qgis/QGIS/issues/48884) | [PR #50608](https://github.com/qgis/QGIS/pull/50608) |  |
| Include type name in message about unsupported qfield validations | Neraportată | [PR #50589](https://github.com/qgis/QGIS/pull/50589) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Funcționalitate: Corecții efectuate de Nyall Dawson
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix regression in column break calculations in legends | [#42672](https://github.com/qgis/QGIS/issues/42672) | [PR #50597](https://github.com/qgis/QGIS/pull/50597) | Not suitable \-- too risky |
| Fix tracing fails when layer crs differs from map crs | [#49247](https://github.com/qgis/QGIS/issues/49247) | [PR #50612](https://github.com/qgis/QGIS/pull/50612) | Nu este necesar |
| Show only available CRS in WMS layer selection widget | [#45918](https://github.com/qgis/QGIS/issues/45918) | [PR #50572](https://github.com/qgis/QGIS/pull/50572) | Nu este necesar |
| Fix some overlay algorithms output multipoint geometries but output layer is single point, causing insertion errors | [#49456](https://github.com/qgis/QGIS/issues/49456) | [PR #50567](https://github.com/qgis/QGIS/pull/50567) | [PR #50641](https://github.com/qgis/QGIS/pull/50641) |
| Fix missing information in crash reports on Windows | [#50472](https://github.com/qgis/QGIS/issues/50472) | [PR #50595](https://github.com/qgis/QGIS/pull/50595) | Nu este necesar |
| Fix regression where attribute table dialogs do not open as proper top level windows with their own taskbar entries | [#49286](https://github.com/qgis/QGIS/issues/49286) | [PR #50594](https://github.com/qgis/QGIS/pull/50594) | Nu este necesar |
| \[georeferencer\] Fix options ignored when \"create world file only\" is active | [#49331](https://github.com/qgis/QGIS/issues/49331) | [PR #50566](https://github.com/qgis/QGIS/pull/50566) | Nu este necesar |
| Ensure identify tool uses correct labels for x/y values when coordinate axis order for project is y/x | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Nu este necesar |
| Ensure coordinate display in status bar updates immediately when related settings change, and update the tooltip to match the actual values displayed in the widget | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Nu este necesar |
| Fix rendering of linestrings with nan z values | [#50510](https://github.com/qgis/QGIS/issues/50510) | [PR #50549](https://github.com/qgis/QGIS/pull/50549) | Nu este necesar |
| Fix broken logic in clearing python console history | Neraportată | [PR #50504](https://github.com/qgis/QGIS/pull/50504) | [PR #50515](https://github.com/qgis/QGIS/pull/50515) |
| Fix QgsFileWidget does not reactivate widget\'s window after selecting a file/folder via the browse button on mac | Neraportată | [PR #50501](https://github.com/qgis/QGIS/pull/50501) | [PR #50502](https://github.com/qgis/QGIS/pull/50502) |
| Fix code folding not shown for non-python code editor classes | Neraportată | [PR #50492](https://github.com/qgis/QGIS/pull/50492) |  |
| Fix leak in GEOS geometry library use | Neraportată | [PR #50379](https://github.com/qgis/QGIS/pull/50379) |  |
| Fix raster contour renderer ignores opacity setting | [#41663](https://github.com/qgis/QGIS/issues/41663) | [PR #50382](https://github.com/qgis/QGIS/pull/50382) | Not suitable \-- too risky |
| Fix truncation of recent project list removes too many items, raises a warning | Neraportată | [PR #50394](https://github.com/qgis/QGIS/pull/50394) | [PR #50397](https://github.com/qgis/QGIS/pull/50397) |
| Fix dizzy easter egg | [#50345](https://github.com/qgis/QGIS/issues/50345) | [PR #50380](https://github.com/qgis/QGIS/pull/50380) | Nu este necesar |
| Fix point pattern fill sometimes ignores symbol opacity setting | [#48031](https://github.com/qgis/QGIS/issues/48031) | [PR #50384](https://github.com/qgis/QGIS/pull/50384) | Not suitable \-- too risky |
| Fix broken path in svg raises Qt warnings while rendering | Neraportată | [PR #50383](https://github.com/qgis/QGIS/pull/50383) |  |
| Ensure correct expression context is used when generating symbol preview icons | [#49106](https://github.com/qgis/QGIS/issues/49106) | [PR #50393](https://github.com/qgis/QGIS/pull/50393) | Not suitable \-- too risky |
| \[spatialite\] Fix corrupted default attribute values when fields are loaded using gaiaVectorLayer | Raportare privată | [PR #50360](https://github.com/qgis/QGIS/pull/50360) | [PR #50361](https://github.com/qgis/QGIS/pull/50361) |
| Fix handling of vector tiles when zoom level 0 is not available | [#47934](https://github.com/qgis/QGIS/issues/47934) | [PR #50337](https://github.com/qgis/QGIS/pull/50337) | Nu este necesar |
| Fix drag and drop of files to georeferencer window | [#49175](https://github.com/qgis/QGIS/issues/49175) | [PR #50338](https://github.com/qgis/QGIS/pull/50338) | Nu este necesar |
| Never try to handle base parameter type values as map layers in QgsProcessingParameterDefinition::valueAs\* methods | [#48598](https://github.com/qgis/QGIS/issues/48598) | [PR #50327](https://github.com/qgis/QGIS/pull/50327) | Nu este necesar |
| Avoid a redundant calculation of visible layer extent in overview canvas | Neraportată | [PR #50329](https://github.com/qgis/QGIS/pull/50329) | [PR #50336](https://github.com/qgis/QGIS/pull/50336) |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Nu este adecvat |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Nu este adecvat |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Funcționalitate: Corecții efectuate de Loïc Bartoletti
| Titlul Erorii | URL issues.qgis.org (dacă a fost raportată) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix \"Add Ring\" tool doesn\'t consider all the overlapping features | [#23113](https://github.com/qgis/QGIS/issues/23113) | [#50447](https://github.com/qgis/QGIS/pull/50447) | Not suitable - add new methods |
| Fix wkbType cast from OGR 25D Type | [#50218](https://github.com/qgis/QGIS/issues/50218) | [#50233](https://github.com/qgis/QGIS/pull/50233) | [#50251](https://github.com/qgis/QGIS/pull/50251) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)

{{<content-end >}}
