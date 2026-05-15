---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.16
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.16{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Data lansării: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Aceasta nu este o Versiune cu Suport pe Termen Lung**

Această versiune nu este desemnată ca având Suport pe Termen Lung (LTR). Utilizatorii care doresc să aibă o versiune de QGIS invariabilă, și care beneficiază de remedierea erorilor timp de cel puțin 1 an, sunt invitați să utilizeze actuala versiune LTR 2.14 (care a devenit versiunea LTR oficială, în urma lansării QGIS 2.16).

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Mulțumiri**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## Sponsorii versiunii QGIS 2.16.0
Anual primim, de asemenea, sprijin de la diverse organizații care ne apreciază munca pe care o depunem și care ar dori să faciliteze efortul susținut de dezvoltare a proiectului. Acești sponsori sunt enumerați mai jos, alături de mulțumirile noastre!

{{<fund type="changelog" >}}
## Generalități
### Funcționalitate: Copierea entităților în format GeoJSON
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Stocarea marcajelor spațiale în fișierul proiectului
De acum, la crearea unui semn de carte spațial, puteți alege stocarea sa în fișierul proiectului activ. Derulați panoul semnelor de carte pentru a găsi caseta de selectare care permite această facilitate.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Stéphane Brunner](http://www.camptocamp.com/)
### Funcționalitate: Suport pentru mesaje GNSS GNRMC
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Ondřej Fibich
### Funcționalitate: Lipirea entităților GeoJSON direct în QGIS
De acum, gestionarul memoriei QGIS poate analiza formate de text suplimentare, oferind suport nativ pentru colecții de elemente GeoJSON. Acest lucru vă permite să copiați direct și să inserați șiruri de caractere GeoJSON în QGIS, convertindu-le automat în entități și geometrii QGIS.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Îmbunătățiri aduse indiciilor pentru hărți
- Vizibilitatea unui maptip este păstrată de acum de-a lungul sesiunilor
- De acum, maptip-urile pot prezenta conținut HTML, inclusiv imagini, video și link-uri URL

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [OPENGIS.ch GmbH](http://www.opengis.ch)

Această funcționalitate a fost dezvoltată de [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Funcționalitate: Pictograme MIME pentru tipurile de fișiere QGIS
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - Fișierul proiectului QGIS
- \*.qml - Fișierul cu setările stratului
- \*.qlr - Fișierul cu definițiile stratului
- \*.qpt - Fișierul șablonului din compozitor

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Alexandre Neto](https://gisunchained.wordpress.com/)
## Interfața cu Utilizatorul
### Funcționalitate: Instrument de mărire a canevasului hărții
Un instrument de mărire a fost adăugat la QGIS, permițându-vă să măriți harta la scara dată. Acest lucru vă permite să măriți o hartă fără a modifica scara hărții, ceea ce ușurează optimizarea preciziei cu care se poziționează etichetele și simbolurile. În plus, poate fi definită o valoare de transfocare implicită, lucru foarte util pentru ecranele de înaltă rezoluție!

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

Această funcționalitate a fost finanțată de [Proiectul QWAT](https://github.com/qwat)

Această funcționalitate a fost dezvoltată de [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funcționalitate: Îmbunătățiri aduse transfocării
QGIS 2.16 aduce îmbunătățiri modului în care puteți mări sau micșora canevasul hărții.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: S-a reproiectat editorul interactiv de gradienți
Editorul gamei gradientului a fost dotat cu controale interactive, pentru manipularea mai ușoară a gradienților. De asemenea, caseta de dialog include de acum o diagramă interactivă dedicată modificării valorilor HSV sau RGB pentru culorile de stop ale gradienților. Caracteristicile noului editor:
- trageți pentru a muta opritorii de culoare
- efectuați dublu clic pentru a adăuga un nou opritor
- apăsând tasta delete se va elimina opritorul selectat
- opritorul selectat poate fi deplasat prin apăsarea tastelor cu săgeți, iar apăsarea tastei shift în același timp va avea ca rezultat o mișcare mai amplă
- glisați și aruncați o culoare pe controlul grafic, pentru a adăuga un nou opritor

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Alegerea unei vizualizări implicite pentru dialogul atributelor
În versiunile QGIS anterioare, dialogul atributelor se deschide întotdeauna cu imaginea unei tabele. De acum, aveți opțiunea de a seta ca implicită vizualizarea sub forma unui tabel, a unui formular sau redeschiderea în ultimul mod utilizat.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Îmbunătățiri aduse ferestrei calendarului
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Selector de culoare îmbunătățit
Meniurile derulante ale butonului de culoare arată de acum o roată de culoare, permițând foarte rapid ajustări ale culorilor.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

Această funcționalitate a fost dezvoltată de [Nathan Woodrow](http://nathanw.net)
### Funcționalitate: Copierea conținutului celulelor din tabelele de atribute
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funcționalitate: Suport HiDPI îmbunătățit
Utilizatorii ecranelor HiDPI vor observa o interfață cu utilizatorul îmbunătățită, atât timp cât s-a depus multă muncă pentru a utiliza pentru pictograme imaginile SVG. În QGIS 2.16 toate barele de instrumente sunt compatibile cu standardul HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Comportament îmbunătățit al instrumentului de selecție
Comportamentul instrumentelor de selecție din hartă a fost rafinat, efectuându-se următoarele modificări:

Pentru selecțiile clic-și-tragere:
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Pentru selecțiile efectuate cu un singur clic:
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Această modificare aduce comportamentul canevasului în concordanță cu alte aplicații similare și, de asemenea, cu comportamentul compozitorului.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Actualizarea Documentației
### Funcționalitate: Documentație pentru QGIS 2.14
Având, de acum, pentru fiecare nouă funcționalitate din QGIS, un mod automat de creare a unui bilet în depozitul documentației, suntem convinși că toate caracteristicile noi se vor regăsi în documentație.

Echipa documentației a lucrat din greu la trei versiuni de QGIS: 2.10, 2.12 și 2.14, în acest fel documentația fiind la zi pentru actuala versiune de QGIS cu Suport pe Termen Lung. Aproximativ 180 de caracteristici noi au fost documentate în 4 luni.

În cazul în care considerați că unele caracteristici lipsesc din documentație, nu ezitați să adăugați un nou tichet, descriind pe scurt problema sau, mai bine, făcând o cerere pentru o contribuție.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

Echipa de documentare va lucra din greu în următoarele luni pentru a documenta versiunea curentă de QGIS (2.16) stabilă.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Verificați versiunile de referință 2.10, 2.12 și 2.14 pentru a vedea toată munca de documentare care a avut loc:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Boundless](http://boundlessgeo.com/)

Această funcționalitate a fost dezvoltată de Larry Shaffer
## Simbologie
### Funcționalitate: Strat simbol de tip săgeată
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

În modul curbat, nodurile stratului de tip linie, asupra căruia este aplicat stratul simbol, sunt folosite ca puncte de control pentru arcele de cerc. Săgețile pot fi umplute cu oricare tip de umplere existent în QGIS. Opțiunile permit, de asemenea,  selectarea tipului de săgeată (cu unul sau două capete, simplă sau înjumătățită), lățimea acesteia (care poate fi variabilă) și mărimea vârfurilor.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

Această funcționalitate a fost dezvoltată de [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Noi simboluri de accesibilitate
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Noi însemne grafice simple pentru simboluri
- semicerc, o treime de cerc și un sfert de cerc
- jumătăți de triunghi
- figuri sub formă de cruce și de hexagon umplute
- figuri sub formă de elipsă și de diamant

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Selecțiile pot fi efectuate în continuare pe stratul din canevas, iar entitățile selectate vor fi randate cu un simbol implicit. Entitățile care sunt editate vor fi, de asemenea, afișate.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Mai mult control asupra randării punctul de umplere a centroidului
S-a adăugat opțiunea de control a desenării simbolului pe toate părțile sau doar pe o singură parte a entităților multiple.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Setarea unui contur pentru simbolurile care conțin caractere ale unor fonturi
Simbolurile care conțin caractere ale unor fonturi pot avea de acum un contur, ceea ce poate contribui la creșterea vizibilității lor, după ce se adaugă un tampon colorat. Caracterele de tip emoji pot avea un aspect mai plăcut, dacă se utilizează un contur îngroșat.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Control asupra stilului de îmbinare pentru însemnele grafice simple, eliptice sau de tip font
Utilizatorii pot schimba de acum stilul de îmbinare pentru figurile simple, eliptice sau de tip font, în scopul finisării simbolurilor.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Un nou instrument pentru hărți, dedicat setării interactive a punctului de decalare al simbolurilor.
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Un nou panou pentru stil
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

Această funcționalitate a fost dezvoltată de [Nathan Woodrow](https://nathanw.net/)
## Etichetare
### Funcționalitate: Instrumentele de etichetare ale hărții permit, de acum, etichetarea în funcție de reguli
În versiunile anterioare ale QGIS, atunci când avea loc etichetarea bazată pe reguli, nu se puteau folosi instrumentele de plasare și de rotire interactivă a etichetelor. Acest lucru este permis de acum.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Această funcționalitate a fost dezvoltată de Martin Dobias
## Diagrame
### Funcționalitate: Elementele din legendă permit redimensionarea diagramei
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [ADUGA](http://www.aduga.org/)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Selecția unității pentru lățimea conturului
De acum, este disponibilă selecția unității pentru lățimea conturului. Acest lucru permite alegerea unităților de hartă pentru diagrame, care vor crește și se vor micșora în funcție de scara hărții, păstrând în același timp o lățime fixă, în milimetri, a conturului.

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Mathieu Pellerin](http://imhere-asia.com/)
### Funcționalitate: Diagramele se comportă similar etichetelor, și pot fi gestionate din bara de instrumente
Inițial, a existat o bară de instrumente pentru etichete care permitea:
- setarea opțiunilor de etichetare pentru etichetele stratului curent
- evidențierea etichetelor fixate. Evidențierea este verde pe strat editabil, și albastru în caz contrar.
- blocarea și deblocarea etichetelor
- deplasarea, afișarea și ascunderea etichetelor

O dată cu această nouă caracteristică, un nou instrument este disponibil în bara instrumentelor de etichetare, care permite stabilirea proprietăților pentru diagramele stratului curent. Mai mult decât atât, fiecare instrument menționat mai sus este, de acum, pe deplin utilizabil asupra diagramelor.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Randare
### Funcționalitate: Noi opțiuni pentru simplificarea "din zbor"
Utilizatorul poate selecta algoritmul de utilizat atunci când are loc simplificarea la nivel local, pentru a desena geometriile mai repede. Acum, QGIS oferă trei algoritmi:
- Distanța (algoritm implicit, fiind singura opțiune disponibilă în versiunile anterioare de QGIS)
- SnapToGrid
- Visvalingam

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Funcționalitate: Clasificare bazată pe cuantile, în cazul straturilor raster
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Piers Titus van der Torren
### Funcționalitate: Render în tip real pentru relief
QGIS 2.16 are un nou render raster, care va crea în mod dinamic un model al reliefului, plecând de la un Model Digital al Elevației.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Această funcționalitate a fost dezvoltată de Asger Skovbo Petersen și Nathan Woodrow
## Digitizarea
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Extinderea geometriilor pentru șirurile de linii cu ajutorul instrumentului de remodelare
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Această funcționalitate a fost dezvoltată de Martin Dobias
### Funcționalitate: Toleranţa  segmentării
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Marco Hugentobler
## Gestiunea Datelor
### Funcționalitate: Noi opțiuni de configurare pentru tabelul de atribute
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Permite adăugarea unei noi coloane în tabelul de atribute, pentru a menține apăsate butoanele, în scopul declanșării unei acțiuni bazate pe entitatea aleasă
- Coloanele pot fi ascunse, în tabelul de atribute (printr-un clic dreapta pe numele câmpului)
- QGIS își amintește, de acum, lățimea coloanelor redimensionate

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/) and [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Funcționalitate: Coloane multiple în formularele cu atribute
Atunci când se utilizează proiectantul drag and drop, un utilizator poate specifica peste câte coloane trebuie să fie distribuite câmpurile.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Asigurați-vă că utilizați modul de proiectare drag and drop
- Faceți clic dublu pe controalele de tip container, cum ar fi filele sau grupurile
- o mică fereastră va apărea în cazul în care puteți selecta numărul de coloane

Ordinea va fi astfel: prima coloană, a doua coloană, coloana n, rândul următor, etc.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch/)
### Funcționalitate: Control asupra atributelor de exportat, atunci când are loc salvarea unui strat vectorial
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de Jürgen Fischer, Even Rouault
### Funcționalitate: La vizualizarea formularelor: coloana laterală este, de acum, sortabilă
În modul de vizualizare sub formă de formular a tabelului de atribute QGIS, există o coloană laterală care se poate folosi pentru a sări direct la o entitate specifică. Până la această versiune, această vedere laterală nu era sortabilă. Pentru sortare, trebuia să se treacă la modul tabelar și apoi se revenea la modul de tip formular. De acum, atributele se pot sorta în mod direct, entitate după entitate, în panoul lateral,  alegând funcția de sortare de pe butonul cu derulare verticală al expresiei de deasupra coloanei laterale.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Funcționalitate: Controlul grafic pentru referințele relațiilor: comenzi rapide pentru adăugarea noilor valori
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Funcționalitate: Îmbunătățiri aduse exportului DXF
A fost adăugat suport pentru etichetarea bazată pe reguli, pentu simboluri rotite și pentru generarea geometriilor 3D.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Jürgen Fischer
### Funcționalitate: Controale grafice la nivel de vârf în modul de proiectare drag and drop
De acum, este posibilă punerea controalelor grafice direct pe formular, prin intermediul proiectantului drag and drop. Un formular cu mod de proiectare drag and drop poate, prin urmare, să nu conțină vreo filă.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch)
### Funcționalitate: Selectare și filtrare pe bază de formular
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

Noile butoane apar în partea de jos a formularului, fie pentru selectarea entitătilor găsite (cu opțiuni de adăugare la selecție/eliminare din selecție/selectare în cadrul selecției curente) sau pentru filtrarea entităților din tabel (cu opțiuni de adăugare sau de eliminare a entităților dintr-un filtru curent).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Această funcționalitate a fost finanțată de SIGE, City of Uster, Morges

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Crearea straturilor GeoPackage
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Even Rouault
### Funcționalitate: Constrângeri asupra controalelor de editare
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Proiectul QWAT](https://github.com/qwat) and the [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funcționalitate: Modificarea simultană a atributelor pentru entitățile multiple
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

În acest mod, modificarea valorii atributelor se va aplica tuturor entităților selectate. Noi controale grafice apar lângă fiecare control de editare, permițând afișarea stării curente de multi-editare și anularea modificărilor pe bază de tipul câmp după câmp.

Modificarile sunt realizate ca o singură comandă de editare, astfel încât apăsarea butonului de refacere va anula modificările aduse atributelor, simultan pentru toate entitățile selectate.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

Această funcționalitate a fost finanțată de [Cantonul Basel Stadt](http://www.geo.bs.ch/)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
## Legenda stratului
### Feature: New option to zoom to a layer\'s visible scale range
Pentru straturile care au setat un interval de scări de vizibilitate, alegerea acestei opțiuni va seta automat scara la cea mai apropiată scară. În plus, interfața a fost optimizată, astfel încât straturile care sunt în afara intervalului de scări, fiind ascunse, sunt prezentate gri în arborele straturilor.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Compozitorul de Hărți
### Funcționalitate: Noi instrumente pentru desenarea poligoanelor și a poliliniilor
Două noi tipuri de elemente pentru compozitor, bazate pe noduri, sunt de acum disponibile în compozitorul de hărți. Cu ajutorul acestora se pot desena poligoane sau polilinii în cadrul compoziției, cu doar câteva clicuri.

Au fost, de asemenea, adăugate instrumente noi care permit editarea nodurilor (cum ar fi mutarea sau eliminarea nodurilor) și de adăugare de noduri la formele existente. De asemenea, elementele de tip poligon și polilinie din compozitor pot fi stilizate cu ajutorul tuturor stilurilor disponibile pentru straturile de tip linie și poligon!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Funcționalitate: Link-uri relative în etichetele compozitorului
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Funcționalitate: Includerea entităților atlasului în sursa compozitorului HTML ca GeoJSON
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com/)
### Funcționalitate: Suport svg parametrizat pentru imaginile svg din compozitor
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Ușurință în utilizarea etichetelor HTML
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Ieșiri georeferențiate (de exemplu, PDF) din compozitor
În QGIS 2.16 compozitorul de hărți generează automat ieșiri georeferențiate (în cazul în care formatul de ieșire, cum ar fi TIF și PDF, face posibil acest lucru).

Opțiunea existentă, de a crea un fișier world, a fost separată de selecția hărții pentru georeferențiere. Noul comportament este de a georeferenția întotdeauna ieșirile, și de a crea doar fișierul world separat, în cazul în care această opțiune este bifată.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Hărțile din compozitor se auto-actualizează pe baza unor presetări
Atunci când un compozitor de hărți este setat să urmeze un stil prestabilit, acesta va fi actualizat automat, la fiecare modificare de stil.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Această funcționalitate a fost dezvoltată de Martin Dobias
## Instrumentele de Analiză
### Funcționalitate: Parametri denumiți în expresii
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

Folosirea parametrilor denumiți ajută la clarificarea argumentelor la care se referă funcția unei expresii, ceea ce este de mare ajutor atunci când se încearcă interpretarea unei expresii la o dată ulterioară!

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Mai multe unități de distanță
Gama unităților de distanță a fost extinsă cu noi opțiuni, incluzând kilometri, yarzi și mile. Folosirea acestor unități previne nevoia de conversie manuală a distanțelor (de exemplu, din picioare în mile).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Modificări aduse expresiilor
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Funcționalitate: Statistici pentru câmpuri de tipul text sau dată
Panoul cu statistici poate prezenta, de acum, statistici cumulate pentru câmpurile text și dată.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Afișarea razei de curbură cu ajutorul instrumentul info
Dacă efectuați clic pe o linie curbă, folosind instrumentul info, QGIS va afișa raza aceteia în instrumentul info.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Marco Hugentobler
### Funcționalitate: Suport pentru agregare, în cadrul expresiilor
QGIS 2.16 adaugă suport, în motorul de expresii, pentru mai multe tipuri de agregare. Dintre acestea enumerăm:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

În toate cazurile, calculele sunt memorate în contextul expresiilor, astfel încât ele vor fi calculate o singură dată pentru fiecare set de evaluări.

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Pluginul fTools a fost înlocuit de algoritmi Processing
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Alex Bruy
## Procesare
### Funcționalitate: Setarea locațiilor pentru puncte printr-un clic pe canevas
Procesarea parametrilor așteaptă o locație de tip punct, care se poate seta, de acum, printr-un simplu clic pe canevasul hărții. În versiunile anterioare, coordonatele locației se introduceau manual.

Această funcționalitate a fost dezvoltată de Alex Bruy
### Funcționalitate: Suport pentru expresii și variabile
Intrările și ieșirile din ferestrele algoritmilor, acceptă de acum expresii și variabile QGIS.

Această funcționalitate a fost dezvoltată de Victor Olaya
### Funcționalitate: Algoritmi preconfigurați
De acum, algoritmii cu parametri preconfigurați pot fi adăugați acum în bara instrumentelor de procesare, sub formă de comandă rapidă pentru un proces dat.

Această funcționalitate a fost dezvoltată de Victor Olaya
### Funcționalitate: Crearea, din bara de instrumente, a unui plugin, cu ajutorul algoritmilor bazați pe scrípturi
Anterior, singura modalitate de a crea un plugin QGIS, care adăuga noi algoritmi în Processing, consta în dezvoltarea manuală a acestor algoritmi și în crearea unui nou furnizor de algoritm. De acum, algoritmii pot fi scriși sub formă de simplu script de procesare, iar un plugin care conține script-ul va fi creat direct din bara de instrumente Processing. Acel plugin poate fi apoi distribuit ca un plug-in obișnuit, și va extinde cadrul de procesare la momentul activării.

Această funcționalitate a fost dezvoltată de Victor Olaya
### Funcționalitate: Utilizarea managerului de autentificare din algoritmii PostGIS
De acum, algoritmii PostGIS folosesc managerul de autentificare QGIS, pentru a obține acreditările din baza de date PostGIS.
- În cazul în care a fost setată o metodă de autentificare la conexiunea PostGIS, utilizatorului i se va cere parola master.
- În cazul lipsei metodei de autentificare pentru conexiune, datele de conectare vor fi preluate din credențialele stocate sau, în cazul în care nu se găsesc acolo, vor fi cerute utilizatorului și vor fi stocate, pentru utilizarea ulterioară.

Astfel, nu mai este necesară pentru a stoca parolelor în clar, în setările conexiunii, pentru a utiliza algoritmi PostGIS.

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Funcționalitate: Suport pentru scrierea în tabelele  fără geometrie
Algoritmul OutputVector suportă, de acum, scrierea în tabelele fără geometrie.

Deocamdată, acest lucru a fost aplicat doar pentru algoritmul Refactor Fields, dar ar putea cu ușurință extins la alți algoritmi pentru atribute, înrudiți.

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Funcționalitate: Algoritmi GRASS suplimentari în cadrul de procesare
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

De asemenea, au fost incluse unele teste de unitate pentru anumiți algoritmi (mai ales pentru algoritmii raster și de imagistică), făcând detectarea erorilor mai ușor de manipulat și de procesat.

Rețineți că, deocamdată, Algoritmii de Procesare GRASS7 pot lucra numai straturi vectoriale de tip Shapefile și rastere GeoTiff. Există, de asemenea, o limită pentru unii algoritmi GRASS7 raster (toți algoritmii care manipulează tabelele de culori), care efectuează o duplicare a straturilor raster în directoare temporare. În funcție de mărimea rasterelor sursă, veți avea nevoie, probabil, de spațiu pe disc pentru a le manipula.

Această funcționalitate a fost dezvoltată de [Médéric Ribreux](https://medspx.fr)
## Furnizorii de Date
### Funcționalitate: Seturile de date OGR sunt deschise, în mod implicit, în modul doar-citire
Este permisă editarea concomitentă a fișierelor Shape și  a fișierelor Tab în QGIS & MapInfo.

Această funcționalitate a fost finanțată de [MEEM (Ministerul Francez al Dezvoltării Sustenabile)](http://www.developpement-durable.gouv.fr/)

Această funcționalitate a fost dezvoltată de Even Rouault
### Funcționalitate: Gestiune îmbunătățită a câmpurilor de tip DOMENIU din Postgres
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Modul readOnly al straturilor vectoriale este configurabil în cadrul proiectului
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch/)
### Funcționalitate: Suport pentru bazele de date DB2
Această funcționalitate a fost dezvoltată de David Adler
### Funcționalitate: În managerul bazei de date, este posibilă actualizarea vederilor Postgres materializate
### Funcționalitate: Este afișat atributul FID OGR
QGIS expune, de acum, FID-ul OGR ca prim atribut, atunci când este util, cum ar fi pentru GPKG și alte drivere pentru baze de date.

Această funcționalitate a fost dezvoltată de Even Rouault
### Funcționalitate: Servicii REST ArcGIS Map și Feature
De acum, QGIS este capabil să se conecteze la serviciile ArcGIS REST.

Vă puteți conecta la servicii ArcGIS Feature (echivalentul WFS în lumea ESRI) și la servicii ArcGIS Map (echivalentul WMS). Furnizorul permite citirea hărților și straturilor vectoriale din aceste servicii.

Această caracteristică este utilă celor care doresc să treacă - fără a pierde nimic din ceea ce s-a construit deja - de la o stivă ESRI GIS la servicii publice sau private pentru hărți. De asemenea, vă puteți conecta la serviciile publice oferite de ESRI.

Această funcționalitate a fost finanțată de [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

Această funcționalitate a fost dezvoltată de [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Funcționalitate: Salvarea stilurilor în bazele de date MS SQL și Oracle
Această funcționalitate a fost dezvoltată de Jürgen Fischer și Christian Frugard
### Funcționalitate: Redenumirea câmpurilor din straturi
În QGIS 2.16 se pot redenumi, de acum, câmpurile din Postgres, Oracle, OGR și straturile de memorie, printr-un dublu clic pe numele câmpului din fereastra de proprietăți a stratului.

Această funcționalitate a fost dezvoltată de [Nyall Dawson (North Road)](http://north-road.com)
### Funcționalitate: Suport de bază pentru Oracle Workspace Manager
A fost adăugat suport pentru Oracle Workspace Manager atunci când se utilizează Oracle Provider.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

Această funcționalitate a fost finanțată de [ENEL](https://www.enel.com)

Această funcționalitate a fost dezvoltată de [Jürgen Fischer for Faunalia](http://faunalia.it)
### Funcționalitate: Îmbunătățiri masive aduse Furnizorului WFS
QGIS 2.16 aduce o revizuire a furnizorului de WFS, incluzând
- Autodetecția versiunii
- Înmagazinarea pe disc a entităților descărcate
- Descărcarea fundalului și randarea progresivă
- Su0port pentru WFS 1.1 și 2.0 
- Paginarea WFS 2.0 GetFeature 
- Adăugarea testelor de furnizor
- Suport pentru îmbinările WFS 2.0
- Parametru URI pentru expresiile sql cu clauze SELECT / FROM / JOIN / WHERE / ORDER BY
- Gestiunea câmpurilor DateTime
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- Suport pentru tipuri de geometrie suplimentară/mixtă (CurvePolygon, CompoundCurve)
- Toleranță mai mare pentru servere WFS neconforme

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Land Information New Zealand și Cantonul Zug, Elveția](http://www.linz.govt.nz/)

Această funcționalitate a fost dezvoltată de [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
Expresia utilizată pentru a genera valori implicite, pentru un câmp din baza de date Postgres, este afișată pe formularul entității.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
Avantajul principal al acestei îmbunătățiri este că, de acum, se pot crea și lega direct înregistrările din tabelele aferente, înainte de salvarea datelor, deoarece cheia primară este prezentă deja.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Cantonul Zug, Elveția](http://geo.zg.ch/)

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch/)
## QGIS Server
### Funcționalitate: Suport pentru sublinierea cu roșu în GetMap și GetPrint
Această funcționalitate a fost finanțată de Cantonul Solothurn

Această funcționalitate a fost dezvoltată de [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Funcționalitate: Transformări de datum implicite pentru server
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

Această funcționalitate a fost dezvoltată de [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Plugin-urile
### Funcționalitate: Plugin globe actualizat
- Actualizare la OsgEarth 2.8
- Rescriere driver QGIS pentru plăcuțe globe
- Rescrierea logicii de sincronizare între 2D și 3D
- Migrare la noul nucleu geometric
- Suport pentru straturi de fundal multiple
- Meniurile încorporate în fereastra globe 
- Selecția straturilor independente pentru glob
- Muncă de portare a tezei de masterat a lui Mathias Kuhns, pentru QGIS 2.1/OsgEarth 2.4

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

Această funcționalitate a fost finanțată de [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

Această funcționalitate a fost dezvoltată de [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Funcționalitate: Globe: Extrudare obiecte 
Este permisă extrudarea obiectelor în a 3-a dimensiune.

Fie după o valoare fixă, fie ​​după un atribut sau o expresie.

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch)
### Funcționalitate: API: Adăugare pagini la proprietățile stratului vectorial
Este permisă adăugarea de pagini suplimentare în fereastra de proprietăți a stratului vectorial.

Acest lucru permite punerea configurației pentru opțiunile stratului, furnizată de un plug-in, direct în locația din care fac parte, pentru o experiență mai bună.

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch)
### Funcționalitate: Globe: Suport vectorial
Atunci când sunt afișate straturi pe glob, se vor păstra datele vectoriale.

Această facilitate a fost finanțată de Master Thesis UZH

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch)
### Funcționalitate: Globe: Exagerare verticală pentru DTM
Because sometimes it\'s just nice to exaggerate about the size.

Această funcționalitate a fost dezvoltată de [Matthias Kuhn](http://www.opengis.ch)
## Programabilitate
### Funcționalitate: Controale grafice încorporate în arborele straturilor
Acest lucru permite definirea unor controalelor grafice, pentru a fi încorporate în arborele straturilor, și care vor corespunde straturilor individuale din fereastra proprietăților stratului (utilizând noua filă a Legendei). Ideea este de a avea o cale de accesare rapidă a acțiunilor des efectuate într-un strat.

Implementarea vine cu un control grafic pentru transparență, în viitor putând exista mai multe controale standard, cum ar fi configurarea filtrării, selecției, stilului etc. API permite plugin-urilor să-și înregistreze propriile controale, care vor permite plugin-urilor pentru diverse domenii specifice să atribuie controale personalizate straturilor pe care le administrează.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Această funcționalitate a fost dezvoltată de Martin Dobias
### Funcționalitate: Plugin-urile pot adăuga pagini proprietăților stratului vectorial
Această funcționalitate a fost dezvoltată de [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Funcționalitate: Noi clase PyQGIS în 2.16
### Noi clase de baze
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

### Noi clase GUI
#### Controale grafice reutilizabile:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- paletei de nuanțe, a specimenelor de culoare, și a unui prelevator de culoare
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

#### Dialoguri reutilizabile:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Corecții Importante
### Funcționalitate: Programul de eliminare cu plată a erorilor QGIS
Am efectuat o altă rundă de remediere cu plată a erorilor (datorită sponsorilor și donatorilor noștri!). Mai jos puteți vedea un sumar al lucrărilor, pentru dezvoltatorii care au participat:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- S-a remediat transformarea proiecției din georeferențiator (#14551 - severă)
- S-a remediat selectarea eronată a entităților, în funcție de rază (#14748 - severă)
- S-a remediat calcularea incorectă a suprafeței poligoanelor (#14675 - severă, deși este foarte puțin probabil să se producă. S-au adăugat teste de unitate, pentru a acoperi acest caz rar)
- S-a remediat aspectul controlului grafic de tip panou (#15011 - severă)
- S-a remediat o eroare din stratul de tip săgeată, al simbolului (neraportată)
- S-a remediat o eroare care apărea la crearea unei relații nevalide (neraportată)
- S-a remediat o eroare care împiedica afișarea SVG-urilor parametrizate, pentru elementele de tip săgeată din compozitor (#14997 - ridicată)
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Întotdeauna se folosește comparația șirurilor în expresii, pentru câmpurile de tip șir (#13204 - ridicată)
- S-au reparat calea către șabloane și directorul de casă, fiind adăugat ca svg, în mod implicit, (#14662, #14652, #14883 - ridicate)
- S-a remediat o eroare care apărea la utilizarea poligoanelor inverse cu renderul pentru hărți calorice (#14968 - ridicată)
- Valorile simbologiei raster au fost salvate cu precizie completă (#14950 - normală)
- Acțiunile nu sunt activate, la încărcarea stratului cu stilul implicit (#13910 - normală)
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- S-a eliminat imposibilitatea de dezactivare a controlului de interceptare (#9732 - normală)
- S-a inversat ordinea dimensiunilor, lățime/înălțime, pentru vârful săgeții din straturile simbolului (#15002 - normală)
- S-au remediat îmbinările care nu sunt recreate atunci când se încarcă un proiect cu straturi defecte (#10500 - normală)
- Memorie cache invalidată atunci când stratul este modificat (#11140 - normală)
- Folosire corectă a îmbinărilor care folosesc câmpuri virtuale (#14820 - normală)
- S-au remediat câmpurile virtuale care depind de alte câmpuri virtuale, care nu puteau fi calculate în anumite circumstanțe (#14939 - normală)
- S-a corectat etichetarea pe bază de reguli, etichetele nefiind afișate atunci când se utilizează funcții cu expresii Python (#14985 - normală)
- Actualizare automată la modificarea nivelurilor simbolurilor în panoul stilului (#14861 - normală)
- S-a resincronizat starea butonlui de andocare cu starea panoului (#14862 - normală)
- S-au remediat problemele de randare a SVG-urilor cu text (#14644, #14794 - normală)
- Câmpurile prezente pe butonul de afișare definită cu ajutorul datelor sunt întotdeauna actualizate (#14809 - normală)
- S-a eliminat imposibilitatea de setare a comenzilor rapide pentru mărire (#14958 - normală)
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- S-au adăugat proxy-urile lipsă din legendă, pentru verificarea comportamentului subrenderelor de inversare și răsturnare a poligoanelor (neraportată)
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- Se arată tipul WKB în metadatele stratului vectorial (neraportat)
- S-au adăugat șirurile de capabilități lipsă, în metadatele stratului (neraportat)
- S-au eliminat informațiile parazit, provenite de la depanare, atunci când se utilizează straturi de geometrie 25D (neraportată)
- S-au remediat unele controale gafice din bara de stare, care nu au putut fi ascunse prin personalizare (neraportată)
- Controlul grafic de stilizare în timp real își amintește setările (neraportată)
- Don\'t show constraint messages when form is in search mode (unreported)
- Se arată bara de derulare pentru formularul de atribute, pe măsură ce se identifică rezultatele (neraportată)
- Butonul de Aplicare din panoul de stilizare este întotdeauna activat (neraportată)
- S-au reintrodus unele actualizări automate, care lipsesc din panoul de stil (neraportată)

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Acestea sunt biletele cu erori specifice aplicației QGIS 2.16, pentru rezolvarea cărora și-a dedicat timpul .

**Severitate/Înaltă:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Severitate/Normală**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Altele:**
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
- Un pas lipsă din Adăugare Strat Vectorial!
- Autourmărirea eșuează pentru Arcele Circulare din geometrii
- WMS nu funcționează în master a625eeb (2.15.0-80)
- Eroare Python în algoritmii de procesare preconfigurați
- GPS don\'t record geometry point, but only attribute values\...
- panoul de stilizare: panoul de transparență (transparență globală, pixel transparent, etc.) nu lucrează pentru renderul de reliefare
- panoul de stilizare: back button & breadcrumb lipsesc atunci când se editează o regulă de etichetare
- S-au remediat funcțiile de undo/redo pentru randarea/etichetarea bazată pe reguli, în panoul de stilizare
- S-au introdus actualizările controlului grafic undo din panoul de stilizare
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Îmbunătățirea stabilității QgsMapLayerRegistry
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- S-au remediat unele probleme de compatibilitate cu Python 3
- S-a lucrat la reactivarea testelor OSX (după fuzionarea cu versiunea 2.16)
- Documentația API
- startup.py se executa de două ori
- Remedieri UX:
  - Tabela de atribute: se afișează întotdeauna numerele secvențiale ale antetului coloanelor
  - Controlul grafic pentru Referințele Relațiilor: Se activează doar atunci când o entitate este setată
  - Afișarea id-ului entității în tabela de atribute a unui tooltip
  - Focusare pe primul control grafic din dialogul credențialelor
  - Durata implicită a textelor din bara de mesaje
  - Add button\" state in postgis source select dialog
- S-au instalat fișierele antet lipsă
- S-a eliminat o eroare de închidere
- Directorul de stocare în rețea
- Formularul entității ascunsă în spatele ferestrei principale, din Windows
- Editarea offline: Respectă căile relative
- Editarea offline: atributele modificate ajung în entitatea greșită
- Offline editing: Don\'t crash with raster layers
- Formularul relațiilor creștea la infinit
- S-a remediat o eroare la încărcarea stilului în proprietățile stratului
- S-a remediat o eroare la închiderea tabelei de atribute
- S-a remediat calea configurată în mod greșit către gpsbabel
- Se afișează numărul corect de entități cu reguli care necesită o geometrie
- S-a remediat o eroare la utilizarea renderului 2.5D într-un strat incompatibil

{{<content-end >}}
