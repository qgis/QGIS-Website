---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Data lansării: 2015-10-23

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Mulțumiri**

Dorim să le mulțumim dezvoltatorilor, tester-ilor, autorilor documentațiilor și tuturor acelor persoane care, în mod voluntar, au consumat timp și efort (sau au finanțat alte persoane în acest scop).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

În fine, am dori să mulțumim sponsorilor noștri oficiali pentru sprijinul financiar de neprețuit, pe care l-au oferit acestui proiect:
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

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Generalități
### Funcționalitate: Un nou ecran de întâmpinare
În loc de a afișa un simplu canevas alb, QGIS vă va prezenta de acum o listă a proiectelor cele mai recente, însoțite de miniaturi, pentru a face rapidă și ușoară revenirea la activitatea efectuată în ultima sesiune.

**Această funcționalitate a fost dezvoltată de:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Funcționalitate: Îmbunătățiri aduse calității codului
Prin utilizarea bibliotecii de curățare a adreselor, sute de pierderi de memorie au fost identificate și remediate. S-a utilizat în mod regulat Coverity Scan la scanarea automată a codului, în scopul identificării potențialelor probleme, iar densitatea Coverity a defectelor noastre este acum impresionant de scăzută, fiind de numai 0.02 defecte la 1000 de linii de cod. De asemenea, biblioteca unității de teste automate a crescut semnificativ pe durata dezvoltării 2.12, având ca rezultat identificarea și remedierea imediată a mai multor regresii. În 2.12 am adăugat, de asemenea testarea continuă pe OSX, astfel încât fiecare actualizare de cod este testată cu ajutorul unității de testare, atât pe platforma Linux, cât și pe OSX.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Funcționalitate: Editor de setări avansat
Un nou panou a fost adăugat în dialogul setărilor, permițându-vă să editați oricare dintre opțiunile deja definite în profilul dvs. Acest lucru este destinat doar utilizatorilor avansați, deoarece ați putea experimenta un comportament neașteptat din partea QGIS, dacă modificați aceste setări fără a înțelege pe deplin ceea ce faceți.

**Această funcționalitate a fost dezvoltată de:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Funcționalitate: Grupuri cu Excludere Reciprocă în Arborele Straturilor
Cu această funcționalitate puteți crea grupuri de straturi, în care doar un singur strat să poată fi vizibil la un moment dat. Funcționalitatea poate fi aplicată individual grupurilor din arborele cu straturi, care apare la accesarea meniului contextual.

**Această funcționalitate a fost dezvoltată de:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Această funcționalitate a fost finanțată de:** Regiunea Toscana (Italia) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Funcționalitate: Filtrarea valorilor din câmpuri, în widget-ul de expresii
La crearea unei expresii care utilizează valori dintr-un câmp, puteți filtra de acum panoul de previzualizare a valorilor câmpului.

**Această funcționalitate a fost dezvoltată de:** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Funcționalitate: Suport pentru Interfețe cu Utilizatorul personalizabile
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**Această funcționalitate a fost dezvoltată de:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Funcționalitate: Noi funcții pentru expresii în 2.12
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Au fost adăugate mai multe funcții care lucrează cu geometria, dintre care amintim:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

În plus, unele expresii foarte utile au fost portate din plugin-ul expressions++, incluzând:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

În plus, ajutorul context pentru funcțiile expresiilor a fost îmbunătățit, pentru o mai bună lizibilitate.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Funcționalitate: Variabile în expresii
Puteți defini de acum variabile personalizate pentru utilizarea în expresii. Variabilele pot fi definite la nivelul global al aplicației, la nivel de proiect, la nivelul stratului și la nivelul compoziției. Similar regulilor CSS, variabilele pot fi suprascrise - de exemplu, o variabilă la nivel de proiect va rescrie orice variabilă setată la nivel de aplicație. Puteți folosi aceste variabile pentru a construi șiruri de text sau alte expresii personalizate. De exemplu, în compozitor crearea unei etichete cu acest conținut:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

Va produce o etichetă care arată în felul următor:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Instrumentele de analiză
### Funcționalitate: Numărul de vertecși este adăugat la câmpurile derivate, în instrumentul de identificare
Folosind instrumentul de identificare pe o entitate de tip linie, veți observa de acum și numărul de vertecși ai entității, ca un atribut suplimentar derivat.
### Funcționalitate: Instrument pentru alinierea rasterelor
This new tool in qgis_analysis library is able to take several rasters as input and:
- să le reproiecteze în același CRS
- să le reeșantioneze la aceeași dimensiune de celulă și offset de grilă
- să decupeze regiunea de interes
- să rescaleze valorile atunci când este necesar

**Această funcționalitate a fost dezvoltată de:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**Această funcționalitate a fost finanțată de:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Funcționalitate: Plugin-urile de Verificare a Geometriei și de Acroșare a Geometriei
Două plugin-uri noi (pe care trebuie să le activați manual în managerul de plugin-uri) sunt disponibile pentru validarea și corectarea geometriei. Plugin-ul **Verificator de Geometrie** (foto dreapta) va verifica și corecta setul dvs. vectorial de date, pentru diverse tipuri de erori sistematice, și va încerca să le rezolve în locul dvs. După rezolvarea unei erori, lista erorilor se actualizează automat, astfel încât, dacă, de exemplu, remedierea unei erori rezolvă, de asemenea, alte erori, toate erorile vor fi eliminate din lista problemelor.

Cu ajutorul instrumentului de **Acroșare Geometrie**, puteți alinia marginile și vertecșii unui strat vectorial față de marginile și vertecșii celui de-al doilea strat, folosind o toleranță definită de utilizator.

**Această funcționalitate a fost dezvoltată de:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**Această funcționalitate a fost finanțată de:** [Cantonul Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Opțiunile Aplicației și ale Proiectului
### Funcționalitate: Managementul parolelor criptate
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Configurații de autentificare parolă-master-criptată, stocate într-o bază de date SQLite
- Arhitectură de plugin pentru metoda de autentificare (similară furnizorilor de date) 
- Basic auth method plugin
- Plugin de bază integrat cu PostGIS, și conexiunile furnizorului OWS 
- Instalare pe baza numelui de utilizator/parolei curente (pe deplin funcțională)
- Configurații de conectare la server SSL (cu salvarea excepțiilor sau a configurărilor personalizate pentru erorile de conexiune SSL)

Legat de autentificarea PKI:
- Importare Autorități de Certificare suplimentare, emitenți intermediari de certificare, și pachete personale de identitate
- Gestiune a componentelor certificatelor, similară cu cea din Firefox
- Plugin-uri dedicate metodelor de autentificare pentru pachete PEM și PKCS12 și pentru identități personale stocate pe disc
- Integrare cu conexiuni către furnizor OWS (pentru PostGIS și alte baze de date mai este de lucru)

Pentru scenariul proiectelor partajate, inclusiv instalarea de pe o unitate de rețea, puteți seta ID-ul configurației de autentificare (authcfg) la ceva care este partajat între utilizatori.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Pentru dialogul de Gestiune a Straturilor Defecte, utilizatorii pot Aadăuga/Edita/Elimina configurările de autentificare, și să actualizeze URI-ul sursei de date pentru a se potrivi. Deci, în scenariul unui proiect partajat, utilizatorul ar putea adăuga imediat o nouă configurare de autentificare corespunzătoare (și să vadă exact care este ID-ul authcfg partajat, pentru a-l utiliza) la încărcarea proiectului.

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Această funcționalitate a fost dezvoltată de:** Larry Shaffer

**Această funcționalitate a fost finanțată de:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Navigatorul
### Funcționalitate: Îmbunătățiri aduse conexiunilor PostGIS din navigator
Navigatorul QGIS suportă de acum funcționalități suplimentare pentru conexiuni PostGIS, inclusiv capacitatea de a **crea, redenumi și șterge scheme**, **suport pentru redenumire și trunchiere straturi** și **copiere tabele dintr-o schemă în alta**.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Furnizorii de Date
### Funcționalitate: Îmbunătățiri aduse furnizorului PostGIS
Următoarele îmbunătățiri au fost aduse furnizorului PostGIS:
- îmbunătățiri de performanță pentru renderele bazate pe reguli, în cazul straturilor PostGIS
- s-a adăugat suport pentru chei compuse, în cadrul vederilor

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## Gestiunea datelor
### Funcționalitate: Îmbunătățiri în DBManager
S-au adus o serie de îmbunătățiri instrumentului DB Manger:
- În DB Manager, puteți exporta de acum datele dvs. pentru orice format de date acceptat de OGR, în loc de fișier shape, care a fost singurul disponibil în versiunea anterioară.
- Oracle Spatial este de acum acceptat în DBManager
- La importarea datelor într-o tabelă, puteți utiliza noua opțiune **importă doar entitățile selectate**, pentru a restricționa ceea ce se importă.
- De acum, ferestrele noilor interogări sunt create sub formă de file, pentru a reduce numărul ferestrelor de dialog

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Funcționalitate: Formatări condiționale pentru celulele tabelelor cu atribute
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**Această funcționalitate a fost dezvoltată de:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Funcționalitate: Suport pentru căile relative ale widget-urilor
Pentru următoarele tipuri de widget-uri de editare:
- Nume de Fișier
- Foto
- Vizualizare Web 

În cazul în care calea este selectată cu exploratorul de fișiere se află în același director cu al fișierului proiectului .qgs, atunci ea va fi convertită în căi relative. Acest lucru crește portabilitatea unui proiect QGIS care are atașate informații multimedia.

**Această funcționalitate a fost dezvoltată de:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**Această funcționalitate a fost finanțată de:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Digitizarea
### Funcționalitate: Îmbunătățiri aduse digitizării
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- instrument de adăugare a unui șir circular, cu două puncte și o rază
- instrument pentru a adăuga șiruri circulare cu un punct de pornire, unul pe curbă și unul final
- posibilitate de anulare a desenării unor noi entități
- afișarea unui tabel pentru nod, la editarea cu ajutorul instrumentului nod, care vă permite să introduceți manual coordonate exacte x și y pentru noduri, precum și valorile z și m (în funcție de tipul stratului)

În plus, multe dintre instrumentele de editare și de modificare a geometriei au fost actualizate, pentru a funcționa corect cu straturile care conțin z sau m dimensiuni.

**Această funcționalitate a fost dezvoltată de:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**Această funcționalitate a fost finanțată de:** [Cantonul Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Etichetare
### Feature: Data defined quadrant when in \"around point\" mode
De acum, este posibilă specificarea unui cvadrant definit cu ajutorul datelor, atunci când o etichetă de tip punct este setată la modul de plasare În Jurul Punctului. Acest lucru vă permite să suprascrieți manual plasarea cvadrantului pentru o etichetă specifică, permițând în același timp etichetelor rămase să beneficieze de plasare automată.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Funcționalitate: Desenarea doar a etichetelor care se potrivesc în interiorul poligoanelor
Straturilor poligoanelor li s-a adăugat opțiunea de desenare a etichetelor care se încadrează complet în entitățile poligonale.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Funcționalitate: Prioritate de control a obstacolelor de etichetare
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Funcționalitate: Noi opțiuni pentru controlul modului în care straturile poligonale pot acționa ca obstacole
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Funcționalitate: Control definit cu ajutorul datelor, pentru prioritatea etichetelor
Această caracteristică, solicitată adesea, permite utilizatorilor setarea priorității pentru etichetele individuale. În versiunile anterioare, QGIS a permis stabilirea priorității etichetei pentru un strat întreg, dar nu a existat nici o opțiune de a controla prioritatea entităților dintr-un strat. Acum, puteți folosi o expresie definită cu ajutorul datelor sau a unui câmp, pentru a prioritiza etichetarea anumitor entități înaintea altora, în cadrul unui strat!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Funcționalitate: Opțiuni doar pentru straturile obstacol
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Funcționalitate: Etichetare bazată pe reguli
Etichetele de pe entități pot fi de acum stilizate folosind reguli, pentru a adăuga chiar și mai mult control asupra plasării și stilizării etichetelor. Similar cu randarea cartografică bazată pe reguli, regulile de etichetare pot fi imbricate pentru a permite opțiuni de stilizare extrem de flexibile. De exemplu, puteți randa etichetele diferit, în funcție de dimensiunea entităților în care vor fi incluse (așa cum este ilustrat în captura de ecran).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**Această funcționalitate a fost dezvoltată de:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Această funcționalitate a fost finanțată de:** Regiunea Toscana (Italia) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Compozitorul de Hărți
### Funcționalitate: Îmbunătățiri aduse navigării prin Atlas
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

Numele paginii poate fi, de asemenea, utilizat în cadrul expresiilor de simbolizare și de etichetare, pentru a permite o stilizare avansată a entităților Atlasului.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Funcționalitate: Format personalizat pentru adnotările grilelor
Adnotările din grila hărții din Compozitor pot fi de acum stilizate în formate personalizate, care sunt evaluate cu ajutorul motorului de expresii. De acum puteți utiliza orice format de numerotare pe care îl necesită grila hărții!

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Funcționalitate: Manipulare și împachetare automată a textului multiliniilor în tabelele de atribute ale compozitorului
Tabela de atribute din compozitor include de acum suport complet pentru șirurile de caractere extinse pe linii multiple. De asemenea, a fost  adăugat controlul asupra alinierii verticale a textului dintr-o celulă, împreună cu opțiuni pentru încadrarea textului într-un anumit număr de caractere, sau pentru calcularea în mod automat a încadrării textului pentru a se potrivi cu dimensiunea coloanelor. Pentru a forța aranjarea automată a textului la înălțimea rândului, setați lățimea coloanei la o dimensiune fixă.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

**Această funcționalitate a fost finanțată de:** [Orașul Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Funcționalitate: Personalizare avansată a culorii de fundal din celule
Această modificare permite utilizatorilor să stabilească diferite culori pentru rânduri și coloane alternative, pentru primele/ultimele rânduri/coloane, din tabela de atribute a compozitorului.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

**Această funcționalitate a fost finanțată de:** [Orașul Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Funcționalitate: S-a adăugat o opțiune de potrivire a conținutului la pagină, și opțiuni de decupare a exporturilor după conținut
O nouă opțiune a fost adăugată în panoul compoziției, pentru a redimensiona o compoziție față de conținutul său, cu margini suplimentare, opționale, dacă este necesar.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

A fost adăugat un nou dialog cu opțiuni de export pentru a facilita exportul imaginilor, care include, de asemenea, comenzi rapide la îndemână, pentru a suprascrie rezoluția de imprimare sau dimensiunile imaginii exportate.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Funcționalitate: Forțarea randării straturilor vectoriale ca imagini raster
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Funcționalitate: Control definit cu ajutorul datelor, pentru straturile hărții și pentru presetările stilului
Un nou control definit cu ajutorul datelor a fost adăugat pentru straturile hartă, alături de presetări de stil pentru a le arăta în harta compozitorului. Expresiile definite cu ajutorul datelor din straturile hărții, ar trebui să prezinte pe hartă o listă cu nume de straturi delimitate de caracterul \| (țeavă), sau expresiile definite cu ajutorul datelor, pentru stilul prestabilit, ar trebui să genereze numele unui stil existent, presetat.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

**Această funcționalitate a fost finanțată de:** [Orașul Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Funcționalitate: Opțiune de a ascunde paginile din vizualizare/export
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)
## Plugin-urile
### Funcționalitate: Actualizare plugin GRASS
Plugin-ul GRASS a fost actualizat pentru versiunea 7. Straturile GRASS pot fi accesat și încărcate din navigatorul QGIS sau din panoul  navigatorului. Datele vectoriale GRASS pot fi editate direct în QGIS. Proiectul conține următoarele pachete de lucru:
- Actualizarea bibliotecii de plugin-uri și compilarea multi versiune
- Navigatorul QGIS și integrarea panoului navigatorului
- Suport pentru seturile de hărți, module și linia de comandă, pentru a permite analiza datelor
- editarea vectorială

Atât utilizatorii GRASS 6, cât și utilizatorii GRASS 7, vor descoperi că integrarea QGIS cu GRASS este plăcută. Puteți crea straturi GRASS direct din panoul Navigatorului QGIS, sau să stilizați straturile vectoriale GRASS cu ajutorul instrumentelor standard QGIS de stilizare, sau a celor de digitizare, la crearea noilor geometrii vectoriale într-un set de hărți GRASS.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**Această funcționalitate a fost dezvoltată de:** [Radim Blazek](http://www.gissula.eu/)

**Această funcționalitate a fost finanțată prin:** Multifinanțare, a se vedea [pagina proiectului](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programabilitate
### Feature: Map tools moved from app-\>gui
Această modificare permite reutilizarea instrumentelor hărții din cadrul scrípturilor PyQGIS și al plugin-urilor Python.

**Această funcționalitate a fost dezvoltată de:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**Această funcționalitate a fost finanțată de:** [SIGE](http://www.sige.ch/)
### Funcționalitate: Editare straturi prin intermediul \`with edit(layer):\`
Exemplu:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Aceasta va apela în mod automat commitChanges() la final. Dacă nu apare nici o excepție, modificările vor suferi un rollBack() 

**Această funcționalitate a fost dezvoltată de:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Funcționalitate: Un nou API pentru motorul de etichetare (QgsLabelingEngineV2)
Ideea este de a face motorul mai flexibil, comparativ cu implementarea QgsPalLabeling:
> - abstractizarea utilizării a etichetelor cu text / diagramelor, față de motor în sine
> - acceptarea tipurilor multiple de etichete pentru fiecare strat
> - acceptarea furnizorilor personalizați de etichete (cum ar fi cei implementați de plugin-uri)
> - facerea motorului de etichetare independent de motorul de randare al hărții
> - ușurarea auto-testării motorului de etichetare și a componentelor sale

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**Această funcționalitate a fost dezvoltată de:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Această funcționalitate a fost finanțată de:** Regiunea Toscana (Italia) - SITA (CIG: 63526840AE)
### Funcționalitate: Deschidere scrípturi într-un editor extern
Programatorii care preferă Python se vor bucura - scrípturile se pot deschide de acum într-un editor extern, folosind butonul nou adăugat în consolă.

**Această funcționalitate a fost dezvoltată de:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Funcționalitate: Noi clase pentru programele PyQGIS
O nouă clasă QgsStringUtils a fost adăugată, ceea ce permite scrípturilor PyQGIS să utilizeze noii algoritmi de potrivire fuzzy adăugați în 2.12. Acestea includ funcțiile pentru găsirea distanței de editare Levenshtein dintre două șiruri și pentru calcularea reprezentării fonetică, soundex, a unui șir. Performanța acestor algoritmi a fost bine optimizată, astfel încât aceștia să fie gata pentru a începe potrivirea fuzzy pentru milioane de șiruri de caractere!

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Server
### Funcționalitate: API Python pentru Serverul QGIS
QGIS Server este împachetat de acum ca o bibliotecă, având un API incipient (dar în creștere) și legături Python. Cu noul API avem un set de teste Python pentru componenta principală a serverului și pentru plugin-urile serverului. Invocarea serverului din Python are loc astfel:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Funcționalitate: getMap în format dxf
Acum este posibilă preluarea rezultatului unei cereri GetMap WMS în format DXF. Aceasta susține aceleași caracteristici și opțiuni ca și cele disponibile în aplicația QGIS. Cu aceleași limitări.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

În captura de ecran veți vedea Clientul Web QGIS în partea stângă, cu funcționalitatea exportului DXF (utilizarea serverului QGIS), și aceeași extindere privită în Autodesk TrueView, în dreapta.

**Această funcționalitate a fost dezvoltată de:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**Această funcționalitate a fost finanțată de:** [Orașul Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Simbologie
### Funcționalitate: Export de miniaturi din managerul de stiluri
Managerul de stiluri vă permite de acum exportarea de miniaturi pentru stilul selectat, fie ca SVG, fie ca imagini PNG.

**Această funcționalitate a fost dezvoltată de:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Funcționalitate: O nouă opțiune pentru a limita dimensiunea, în mm, la utilizarea unităților de mărime ale hărții
Anterior, era disponibilă numai posibilitatea de a limita gama scărilor, pentru dimensiunile unităților de hartă. Acum puteți alege, de asemenea, să limitați dimensiunea de randare corespunzătoare la mm.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Funcționalitate:  Îmbunătățiri aduse renderului de deplasare
- Permite o toleranță în mm/pixeli pentru renderul de deplasare
- Permite setarea transparenței pentru culori
- Modul de plasare al inelelor concentrice (permite o afișare mai compactă, numai cu inele)

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Funcționalitate: Toate gamele de culori pot fi de acum editate
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Funcționalitate: Gestionare îmbunătățită a contururilor simbolurilor SVG
QGIS 2.12 remediază o serie de aspecte legate de manipularea contururilor din simbolurile SVG și de umplerea acestora.

Versiunile anterioare ale QGIS ar fi făcut conturul la o dimensiune mult mai mică decât ar fi trebuit, iar desenarea în unități de hartă a SVG-urilor cu dimensiuni reduse ar fi fost defectuoasă.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Funcționalitate: S-au adăugat pixelii ca opțiune pentru toate unitățile de mărime pentru simbologie
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**Această funcționalitate a fost dezvoltată de:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
