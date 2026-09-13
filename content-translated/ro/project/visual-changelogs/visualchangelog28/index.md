---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.8{#changelog28 }
Data lansării: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Versiunea cu Suport pe Termen Lung**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

Scopul versiunilor LTR este de a oferi o platformă stabilă și mai puțin supusă schimbărilor, pentru întreprinderi și organizații care nu doresc să se ocupe cu actualizarea competențelor utilizatorilor, a materialelor de instruire etc., mai mult de o dată pe an. Succesul versiunilor LTR ține de voi, utilizatorii noștri dragi - avem nevoie de sprijinul vostru pentru a ajuta la finanțarea reparării erorilor, totodată, asigurându-vă prin contractele de asistență cu furnizorii de suport tehnic, că toate erorile reparate în numele dumneavoastră vor fi aplicate atât versiunii LTR cât și celei obișnuite.

În cazul în care un LTR este important pentru dvs., vă rugăm să luați în considerare, de asemenea, sprijinirea în mod direct a proiectului QGIS, sau să propuneți furnizorului dumneavoastră comercial utilizarea LTR ca o bază pentru soluțiile enterprise, astfel încât oricine să poată beneficia de o platformă stabilă, care este în permanență îmbunătățită și rafinată. Rețineți că pentru utilizatorii și organizațiile cărora le plac lucrurile împinse la limită, elaborarea unei noi versiuni, o dată la patru luni, va continua neabătut.

**Noi Funcționalități**

QGIS 2.8 este, de asemenea, o versiune specială, deoarece include foarte multe caracteristici noi, reglaje și îmbunătățiri, pentru a face cel mai popular GIS desktop gratuit cât mai complet și util.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Mulțumiri**

Dorim să le mulțumim dezvoltatorilor, tester-ilor, autorilor documentațiilor și tuturor acelor persoane care, în mod voluntar, au consumat timp și efort (sau au finanțat alte persoane în acest scop).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

În fine, am dori să mulțumim sponsorilor noștri oficiali pentru sprijinul financiar de neprețuit, pe care l-au oferit acestui proiect:
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

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Generalități
### Funcționalitate: Introducerea expresiilor în casete cu incrementare
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Funcționalitate: Semnele de carte pot fi importate/exportate
Acum este posibil să salvați/încărcați marcajele într-un fișier. Acest lucru facilitează partajarea locațiilor marcate, sau transferul lor în alte calculatoare.

**Această funcționalitate a fost dezvoltată de:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Funcționalitate: Îmbunătățiri aduse expresiilor
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Evaluarea întârziată a expresiilor**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Funcționalitate: Testarea continuă a cadrului de lucru și asigurarea îmbunătățirii calității
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

De asemenea, în prezent desfășurăm cu regularitate scanări ale bazei de cod QGIS. Ca urmare a acestui fapt, am identificat și reparat peste 1000 de marcat probleme, inclusiv defecțiuni de memorie și potențiale erori. QGIS are o densitate a defectelor de 0,01, în timp  ce media pentru programele de dimensiuni similare este de aproximativ 1,0.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Instrumentele de analiză
### Funcționalitate: Îmbunătățiri aduse dialogului de măsurare
Instrumentul de măsurare a fost îmbunătățit, astfel încât de acum să puteți selecta unitățile care trebuie să fie utilizate. Există, de asemenea, o nouă secțiune de informații în fereastra de dialog, care arată ce setări sunt utilizate în timpul operațiunilor de măsurare.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Navigatorul
### Un navigator mult mai prompt
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Această funcționalitate a fost dezvoltată de:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Furnizorii de Date
### Funcționalitate: Suport pentru legendă grafică WMS contextuală 
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**Această funcționalitate a fost finanțată de:** [Regione Toscana](http://www.regione.toscana.it/)

**Această funcționalitate a fost dezvoltată de:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gestiunea datelor
### Funcționalitate: Prefix personalizat pentru joncțiuni
Puteți defini de acum un prefix personalizat în managerul de joncțiuni din fereastra de dialog a proprietăților stratului. Când se folosește un prefix, tabelul de atribute în cauză va avea numele atributelor alăturate afișat cu prefixul preferat.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Funcționalitate: Suport pentru crearea straturilor stocate temporar în memorie
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Funcționalitate: Suport pentru calcule asupra rândurilor selectate
În tabelul de atribute puteți face acum calcule pe rândurile selectate, mulțumită butonului nou adăugat în bara de calculatorului de câmpuri.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Digitizarea
### Funcționalitate: Instrumente de digitizare avansată
Dacă ați dorit vreodată să puteți digitiza în QGIS linii exact paralele sau în unghi drept, sau să fixați liniile la un unghi specific și așa mai departe, acum se poate! Instrumentele de digitizare avansate reprezintă o portare a pluginului CADinput, căruia i s-a adăugat un nou panou în QGIS. Panoul devine activ la momentul capturii de noi geometrii sau a unor părți de geometrie

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Funcționalitate: Instrument de simplificare îmbunătățit
Instrumentul de simplificare a fost revizuit, adăugându-se:
- Suport pentru reproiectarea OTF
- utilizatorul poate specifica toleranța exactă (nu doar o valoare relativă fără sens)
- toleranța poate fi specificată fie în unități ale hărții, fie în unitățile stratului sau în pixeli
- setările toleranței sunt stocate în setările generale
- simplificarea mai multor entități simultan (glisare dreptunghi în loc de efectuarea unui clic)
- suport pentru entitățile multi-parte
- statistici despre reducerea numărului de noduri

**Această funcționalitate a fost finanțată de:** [Tracks for Africa](http://tracks4africa.com/)

**Această funcționalitate a fost dezvoltată de:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Funcționalitate: Îmbunătățiri aduse acroșării
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**Această funcționalitate a fost finanțată de:** [Orașul Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Elveția](http://www.qgis.ch/)

**Această funcționalitate a fost dezvoltată de:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Legenda stratului
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**Această funcționalitate a fost finanțată de:** [SIGE](http://www.sige.ch/)

**Această funcționalitate a fost dezvoltată de:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Compozitorul de Hărți
### Funcționalitate: Îmbunătățiri aduse Interfeței Compozitorului
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- Modul de afișare a compozitorului **pe tot ecranul**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Funcționalitate: Îmbunătățiri aduse grilei
În compozitor, de acum aveți un control mai fin al cadrului de afișare și adnotare. Anterior, pentru hărți rotite sau grile reproiectate, compozitorul desena toate coordonatele pentru fiecare latură a hărții. Acest lucru a dus la un amestec de coordonate de latitudine/y și longitudine/x afișate pe margini. Acum puteți controla dacă doriți să se afișeze toate coordonatele, doar latitudinea sau numai longitudinea pentru fiecare latură a cadrului hărții. Opțiuni similare au fost, de asemenea, adăugate pentru a controla modul în care este împărțit cadrul hărții.

O nouă direcție descendentă, verticală, pentru adnotări. Această schimbare adaugă o nou mod de direcție verticală, descendentă, pentru adnotări pe grila hărții. Înainte era posibil doar textul crescător pentru adnotările verticale.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Funcționalitate: Marginea etichetelor
- De acum, puteți controla ambele **margini pentru etichete**, orizontale și verticale. Anterior, setările marginii se aplicau atât marginii orizontale cât și celei verticale. Această modificare permite utilizatorilor să specifice margini orizontale și verticale diferite.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Plugin-urile
### Funcționalitate: Îmbunătățiri aduse consolei Python
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Procesare
### Funcționalitate: Un nou tip de parametru - predicatul geometric
Cu acest nou tip de parametru, folosit în algoritmii **Selectare după locație, Extragere după locație** și **Joncțiune atribute după locație**, utilizatorul poate selecta cu precizie a operatorul spațial de utilizat.

**Această funcționalitate a fost finanțată de:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**Această funcționalitate a fost dezvoltată de:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Funcționalitate: Noi algoritmi
Au fost adăugați cadrului de procesare o serie de algoritmi noi:
- Algoritmul "Puncte regulate" (ca răspuns la #5953)
- Algoritmul "Diferență simetrică" (ca răspuns la #5953)
- Algoritmul "Divizare vectorială" (ca răspuns la #5953)
- Algoritmul "Grilă vectorială" (ca răspuns la #5953)
- Algoritmul de calculare a **Curbelor hipsometrice**
- **Divizarea liniilor cu ajutorul liniilor**
- Algoritmul de manipulare a atributelor: **Refactorizare câmpuri** 

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programabilitate
### Funcționalitate: S-a adăugat funcționalitatea de comentare în expresii
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Funcționalitate: Editor de funcții cu expresii personalizate
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Funcționalitate: Suport pentru Qt5
QGIS poate fi acum construit folosind biblioteci Qt5. Rețineți că în prezent majoritatea binarelor sunt compilate, în mod implicit, pentru Qt4.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Funcționalitate: Încărcare bulk a indexului spațial
În API s-a adăugat suport pentru încărcarea bulk a indexului spațial. Aceasta reprezintă o modalitate mai rapidă de inițializare a indexului spațial. În python se scrie pur și simplu:

`index = QgsSpatialIndex( layer.getFeatures() )`

Dintr-un test simplu cu 50K puncte într-un strat de memorie:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

Teoretic, arborele indexului ar trebui să fie, de asemenea, mai bine construit și să conducă la căutări rapide.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Funcționalitate: Se poate rula doar partea selectată a unei interogări SQL
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Server
### Funcționalitate: Plugin-uri Python pentru server
Suportul pentru plugin-uri, aduce puterea Python pe partea de server QGIS, pentru a permite dezvoltarea și implementarea de noi caracteristici rapide și eficiente.

**Această funcționalitate a fost dezvoltată de:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Funcționalitate: Suport pentru stilurile straturilor
- QGIS Server suportă de acum stiluri de straturi predefinite în cererile GetMap
- QGIS Server suportă de acum multiple stiluri de cereri GetStyles (v. secțiunea Simbologie, de mai jos)

### Funcționalitate: S-a adăugat metoda DescribeLayer în WMS
**Profil Styled Layer Descriptor pentru Web Map Service : DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Definirea unui stil personalizat de către utilizator necesită informații despre entitățile care vor fi simbolizate, sau cel puțin tipul entității/acoperirii. Deoarece stilurile definite de către utilizator pot fi aplicate unui strat denumit, trebuie să existe un mecanism prin care un client poate obține informațiile pentru acest tip de strat. Acesta este un alt exemplu de reducere a decalajului dintre conceptele de straturi si stiluri WMS și conceptele de tip de entitate și strat de acoperire specifice WFS/WCS. Pentru a permite acest lucru, un WMS poate accepta în mod opțional cererea **DescribeLayer**.

Metoda DescribeLayer a fost considerată a fi o abordare mai bună decât supraîncărcarea documentului de capabilități WMS.

Pentru fiecare strat denumit, descrierea ar trebui să indice dacă se bazează într-adevăr pe datele entității și dacă da, ar trebui să arate WFS/WCS (printr-un prefix URL) și tipul entității/acoperirii. Rețineți că este perfect valabil ca un strat denumit să nu fie descris în acest fel.
## Simbologie
### Funcționalitate: Posibilitate de umplere cu imagini raster
Acest nou tip de strat pentru simbol permite umplerea poligoanelor cu o imagine raster (sub formă de plăcuță).

Opțiunile includ numele de fișier (definit cu ajutorul datelor), opacitate, dimensiunea imaginii (în pixeli, mm sau unități de hartă), modul coordonatelor (entitate sau vizualizare), și rotația.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Funcționalitate: Render în tip real pentru hărți calorice
Noul render de hărți calorice vectoriale este dinamic, putând fi folosit în timp real pentru straturile de puncte.

Opțiunile includ specificarea razei hărții calorice în pixeli, mm sau unități de hartă, alegerea rampei de culoare, ponderarea punctelor în funcție de câmp, precum și un cursor glisant pentru stabilirea unui compromis între viteza și calitatea randării.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Funcționalitate: Stiluri multiple per strat
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**Această funcționalitate a fost finanțată de:** [Regione Toscana](http://www.regione.toscana.it/)

**Această funcționalitate a fost dezvoltată de:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Funcționalitate: Mai multe setări de simbologie definite cu ajutorul datelor
Interfața cu utilizatorul, pentru setarea simbologiei definite prin date, a fost îmbunătățită - mutând opțiunile de definire prin date imediat lângă fiecare proprietate definibilă (în conformitate cu alte părți ale QGIS, cum ar fi proprietățile de etichetare). De asemenea, multe proprietăți noi ale simbologiei au devenit definibile prin date. Această îmbunătățire a interfeței cu utilizatorul oferă, de asemenea, un mod de a vedea imediat dacă definirea prin date a unui parametru este posibilă, oferind și un acces mai ușor la aceste setări.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Funcționalitate: Export DXF - s-a îmbunătățit exportul simbolului 
Funcționalitatea de exportare a fișierelor DXF a fost îmbunătățită, crescând fidelitatea simbolurilor exportate din QGIS comparativ cu simbolurile inițiale.
### Funcționalitate: Rotirea hărții din canevas - rotație îmbunătățită în compozitor
Această versiune include suport preliminar pentru rotirea hărții de pe canevas. Puteți roti canevasul folosind noul widget de rotație din bara de stare. Suportul pentru rotire a fost extins în compozitorul de hărți, astfel încât acesta să poată gestiona în mod corect etichetarea și simbologia, etc.

**Această funcționalitate a fost finanțată de:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**Această funcționalitate a fost dezvoltată de:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Interfața cu Utilizatorul
### Funcționalitate: Selecție îmbunătățită/consistentă a proiecției
Toate dialogurile folosesc acum un widget selecție consistentă a proiecției, care permite selectarea rapidă a proiecțiilor recent utilizate și a celor standard din proiect/QGIS.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
