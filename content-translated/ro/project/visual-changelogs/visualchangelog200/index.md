---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.0{#changelog20 }
Data lansării: 2013-09-09

{{<table-of-contents >}}
## Instrumentele de analiză
### Funcționalitate: Linia comenzilor de procesare
Pentru un acces rapid la funcționalitățile de geoprocesare, puteți lansa doar linia comenzilor de procesare (Ctrl + Alt + M) și să începeți să tastați numele instrumentului pe care îl cautați. Vi se vor prezenta opțiunile disponibile, gata pentru a fi lansate. Nu mai este nevoie să căutați printre meniuri pentru a găsi instrumentele. Acum le aveți la îndemână.

![image1](images/processing_commander_2.png)
### Funcționalitate:  Îmbunătățiri aduse Plugin-ului Heatmap
Pluginul Heatmap a înregistrat numeroase îmbunătățiri și optimizări, având ca rezultat crearea mult mai rapidă a hărților calorice. În plus, aveți acum posibilitatea de a alege funcția de bază care să genereze harta.

![image2](images/Selection_027.png)
### Funcționalitate: Suport pentru Processing
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Funcționalitate: Modelatorul de Procese
Una din marile funcționalități ale noului cadru de procesare este abilitatea de a combina grafic instrumentele. Utilizând **Modelatorul de procese**, puteți alcătui analize complexe pornind de la o serie de mici module, dedicate, fiecare, unui singur scop. Puteți salva aceste modele și apoi să le utilizați ca blocuri în modele mai complexe. O putere incredibilă, integrată chiar în QGIS, și foarte ușor de folosit!

![image4](images/Processing_modeler_029.png)
## Opțiunile Aplicației și ale Proiectului
### Funcționalitate: Definirea proiectului de pornire implicit și a șabloanelor de proiect
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Funcționalitate: Variabilele de mediu ale sistemului
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Funcționalitate: Scări de mărire definite de utilizator
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Navigatorul
### Funcționalitate: Îmbunătățiri aduse panoului navigatorului
- Directoarele se pot filtra cu ajutorul metacaracterelor sau a expresiilor regulate
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Posibilitate de sortare a pictogramelor după tipul grupului de elemente (sistem de fișiere, baze de date, servere de hărți)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Furnizorii de Date
### Funcționalitate: Revizuirea Furnizorului de Date Raster
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Funcționalitate: Suport pentru Oracle Spatial
QGIS 2.0 include de acum suport pentru Oracle Spatial.

![image10](images/oracle.png)
### Funcționalitate: S-a adăugat furnizorul de servicii Web Coverage
QGIS oferă acum suport nativ pentru straturi Web Coverage Service - procesul de adăugare WCS fiind similar cu adăugarea straturilor WMS sau WFS.
### Funcționalitate: Reducere cumulativă cu 2% a rasterelor, în mod implicit
Multe produse de tip raster au un număr mare de aberații care au ca rezultat imagini cu aspect spălăcit. QGIS 2.0 intoduce un control mult mai fin asupra comportamentului de randare a rasterelor, inclusiv prin folosirea unui procentaj de reducere cumulativă, în mod implicit de 2%, ajungând până la 98%, atunci când se determină spațiul de culoare pentru imagine. Imaginile de mai jos prezintă o comparație între aici QGIS 1.8 (stânga) și QGIS 2.0 (dreapta), randând aceeași imagine cu setările implicite.

![image11](images/Selection_023.png)
### Funcționalitate: Format de identificare WMS
De acum este posibilă selectarea formatului rezultatului, pentru instrumentul de identificare al straturilor WMS, atunci când sunt suportate de către server mai multe formate cunoscute. Formatele suportate sunt HTML, entitate (GML) și text simplu. Dacă este selectat formatul entitate (GML), rezultatul este în aceeași formă ca cel pentru straturile vectoriale, geometria putând fi evidențiată, iar entitatea, cu tot cu atribute și cu geometrie, poate fi copiată în clipboard și lipită unui alt strat.

![image12](images/wms-identify.png)
### Funcționalitate: Suport WMTS
Clientul WMS din QGIS suportă acum WMTS (Web Mapping Tile Service), inclusiv selectarea sub-seturilor de date, cum ar fi feliile temporale. Când adăugați un strat WMS de la un server compatibil, vi se va solicita să selectați felia temporală ce urmează a fi afișată.

![image13](images/Selection_035.png)
## Generalități
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Etichetare
### Funcționalitate: Noul sistem de etichetare
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Funcționalitate: Expresii bazate pe proprietățile etichetelor
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Exemple de proprietăți atașabile:
- Font
- Dimensiuni
- Stil
- Dimensiunea zonei tampon

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Funcționalitate: Utilizarea vechiul motor de etichetare este dezaprobată
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

În QGIS 2.0 sunt valabile următoarele reguli pentru lucrul cu vechiul motor:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- Fila elementelor dezaprobate rămâne activă pentru proiectele mai vechi deschise, dacă cel puțin unul dintre straturi le folosește, și nu dispare nici dacă salvați proiectul.

Fila de etichetelor dezaprobate poate fi activată/dezactivată pentru proiectul curent, prin comenzi introduse în consola Python, cum ar fi:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**OBSERVAȚIE**: Există o *probabilitate foarte mare* ca motorul de etichetare perimat să fie eliminat complet, înainte de următoarea versiune stabilă a QGIS. Vă rugăm să migrați vechile proiecte.

![image17](images/changelog-2.0_labels-deprecated.png)
## Legenda stratului
### Funcționalitate: Răspunsul vizual al legendei și opțiunile acesteia
- Număr total de entități dintr-un strat, precum și per simbol
- În dreptul straturilor vectoriale aflate în modul de editare, există acum un creion roșu care indică modificările netransmise (nesalvate)
- Stratul activ este acum subliniat, pentru a indica existența unei selecții multi-strat sau lipsa oricărei selecții
- Efectuarea unui clic pe spațiu alb, care nu face parte dintr-o listă, elimină o selecție existentă
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- În mod opțional, grupurile și straturile pot avea denumirea scrisă îngroșat
- De acum, generarea pictogramele de previzualizare ale straturilor raster poate fi acum oprită, pentru proiecte în care randarea acestora se face lent

![image18](images/changelog-2.0_visual-options.png)
### Funcționalitate: Duplicarea unui strat de hartă existent
Este posibilă duplicarea straturilor vectoriale și raster, selectate în legenda straturilor hărții. Similar cu importarea încă o dată a aceleiași surse de date, ca strat separat, apoi copierea/lipirea stilului și simbologiei atributelor.

![image19](images/changelog-2.0_dup-layer_1.png)
### Funcționalitate: Comenzi de editare pentru multi-straturi
Utilizatorul poate selecta de acum mai multe straturi în legendă, iar în cazul în care oricare dintre aceste straturi vectoriale se află în modul de editare, poate salva, reface sau anula modificările curente. Utilizatorul poate alege, de asemenea, să efectueze aceste acțiuni în toate straturile, indiferent de selecție.

![image20](images/changelog-2.0_current-edits.png)
## Compozitorul de Hărți
### Funcționalitate: Elemente HTML pentru hărți 
De acum puteți introduce elemente HTML în hărțile dvs.

![image21](images/Composer_1_006.png)
### Funcționalitate: Suport pentru pagini multiple
De acum, o fereastră de compozitor singulară poate conține mai mult de o singură pagină.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Funcționalitate: Expresii în etichetele compozitorului
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

O etichetă cu o expresie, cum ar fi:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
va fi evaluată la momentul imprimării (și în timpul afișării) pentru a genera:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Funcționalitate: Traiectorii pentru auto-aliniere
Pentru a avea hărți aspectuoase, este vital ca elementele conținute să fie frumos aliniate. În acest sens, au fost adăugate linii care permit alinierea ușoară a obiectelor prin simpla glisare a obiectelor.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Funcționalitate: Traiectorii pentru aliniere, adăugate manual
Uneori este nevoie să aliniați obiectele în compozitor la o anumită distanță. Cu noile traiectorii manuale, pentru aliniere, veți putea alinia mai bine obiectele. Pur și simplu, trageți de rigla superioară sau de cea laterală, pentru a adăuga noi linii de ghidare.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Funcționalitate: Generarea seriilor de hărți
A trebuit vreodată să generați o serie de hărți? Cu siguranță. De acum, compozitorul include un generator de serii de hărți, care utilizează funcțiile atlasului. Straturile pot fi puncte, linii, poligoane, iar valorile actualelor atribute ale entităților sunt disponibile pentru afișare, cu ajutorul etichetelor.

![image26](images/Picture1.png)
### Funcționalitate: Suport pentru previzualizarea automată în cadrul hărții
A trebuit vreodată să afișați înteaga hartă într-o fereastră de ansamblu, mai mică? Acum se poate. Harta cadru are acum posibilitatea de a afișa vederi de ansamblu, care se vor actualiza atunci când sunt deplasate. Această facilitate, alături de funcțiile de generare de bază a atlasului din compozitor, oferă posibilitatea creării unor hărți deosebite. Stilul cadrului de vizualizare utilizează aceleași modalități de stilizare ca orice hartă poligonală obișnuită, așa că nu veți întâlni restricții de creativitate.

![image27](images/Picture1_1.png)
### Funcționalitate: Amestecarea straturilor
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Funcționalitate: Suport pentru etichete HTML
Suportul pentru HTML a fost adăugat etichetelor din compozitor, pentru a vă oferi un control mai mare asupra hărți finale. Etichetele HTML suportă pe deplin css, html și chiar javascript, dacă vă pasionează.

![image29](images/html.png)
### Funcționalitate: Legendă multicoloană, în compozitor
Legenda compozitorul suportă de acum coloane multiple. Divizarea unui strat, cu multe clase, în mai multe coloane este opțională. Straturile cu un singur simbol, sunt de acum adăugate, în mod implicit, ca elemente cu o singură linie. Trei stiluri diferite pot fi atribuite titlului stratului/grupului: Grup, Subgrup sau Ascuns. Stilurile titlurilor permit gruparea elemente în mod vizual, arbitrar. De exemplu, un strat cu un singur simbol poate fi afișat ca element cu o singură linie sau ca titlu de strat (ca în 1.8), simbolurile următoarelor straturi multiple putând fi grupate într-un singur grup (ascunzând titlurile) etc. Numărul de entități poate fi, de asemenea, adăugat etichetelor.

![image30](images/multicolumn-legend.png)
### Funcționalitate: Gestionare mai bună a hărților din compozitor
Următoarele îmbunătățiri au fost aduse gestionării hărților din compozitor:
- De acum, numele compozitorului poate fi definit la creare, fiind opțională alegerea de a porni de la alt compozitor
- Compozitoarele se pot duplica
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Proiectul părinte poate fi acum salvat direct din spațiul de lucru al compozitorului
- Toate acțiunile de gestiune sunt accesibile direct din spațiul de lucru al compozitorului

![image31](images/changelog-2.0_composer-mngmnt.png)
## Plugin-urile
### Funcționalitate: Manager de plugin-uri revitalizat
În QGIS 1.x gestionarea plugin-urilor a fost, oarecum, confuză, datorită celor două interfețe - una pentru gestionarea plugin-urilor deja instalate, iar cealaltă pentru obținerea plugin-urilor python dintr-un depozit dedicat. În QGIS 2.0 introducem **un nou manager de plugin-uri, unificat**, care oferă *o singură oprire* pentru descărcarea, activarea/dezactivarea și, în general, gestionarea plugin-urilor dvs. De asemenea, interfața cu utilizatorul devine superbă, datorită panourilor laterale și pictogramelor ușor de recunoscut!

![image32](images/Plugin_Manager_024.png)
## Programabilitate
### Funcționalitate: O Nouă Consolă Python
Noua consolă Python vă oferă și mai multă putere. De acum, suportă auto-completare, evidențierea sintaxei, setări pentru reglarea fontului. Editorul de cod lateral permite introducerea mai ușoară a blocurilor de cod de mari dimensiuni, având abilitatea de a deschide și rula orice fișier Python, în sesiunea QGIS.

![image33](images/pyconsole.png)
### Funcționalitate: Mult mai multe funcții, în cadrul expresiilor
Motorul de expresii fiind folosit din ce în ce mai mult în QGIS, pentru a permite lucruri de genul etichetelor pe bază de expresie și simbol, din ce în ce mai multe funcții au fost adăugate, toate fiind accesibile în constructorul de expresii. Funcțiile sunt însoțite de descriere și ghiduri de utilizare complete, ceea ce sporește ușurința de utilizare.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Funcționalitate: Expresii cu funcții personalizate
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Funcționalitate: Un nou API Python, mai clar
API-ul Python a fost restructurat pentru a permite un stil de lucru mult mai orientat către Python. API-ul QGIS 2.0 folosește SIP V2 care elimină logica întortocheată a funcțiilor toString(), toInt(), de care era nevoie în lucrul cu valori. De acum, tipurile sunt transformate în tipuri Python native, având ca rezultat un API mult mai frumos. Accesul la atribute se face chiar pe entitate, cu ajutorul unei simple chei de căutare, fără căutarea într-un index și în hărțile de atribute.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
De asemenea, a fost îmbunătățit modul în care sunt citite entitățile dintr-un strat, ceea ce permite execuţia multifilară, în versiunile viitoare.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Funcționalitate: Un cod compatibil cu cel al versiunilor 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Funcționalitate: Proiecte macro, în Python
Un modul Python, salvat într-un fișier project.qgs, poate fi încărcat și să aibă funcții specifice de rulare, pentru următoarele evenimente ale proiectului:
- `openProject()`
- `saveProject()`
- `closeProject()`

Chiar dacă rulează, un macro poate fi configurat în opțiunile aplicației.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Simbologie
### Funcționalitate: Proprietăți definite cu ajutorul datelor
Cu ajutorul noilor proprietăți definite cu ajutorul datelor, este posibilă controlarea tipului simbolului, mărimea, culoarea, rotirea, și multe alte proprietăți ale entităților.

![image39](images/datadefinedproperties2.png)
### Funcționalitate: Management îmbunătățit pentru straturile simbolurilor
Noul aspect al straturilor din care este compus un simbol este mai clar, fiind structurat sub forma unui arbore, permițând accesul ușor și rapid la straturi.

![image40](images/symbollayertree.png)
### Funcționalitate: Suport pentru transparență, în cadrul definițiilor de culoare
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Funcționalitate: Controlul culorii, în cazul straturilor raster
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Funcționalitate: Copiere simbologie între straturi
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Funcționalitate: Salvarea stilurilor în baza de date
Dacă utilizați o bază de date pentru stocarea datelor vectoriale, puteți stoca acum definițiile pentru stilurile straturilor direct în baza de date. Acest lucru ușurează partajarea stilurilor pentru straturi, într-un mediu multi-utilizator, sau într-o întreprindere.

![image44](images/Selection_037.png)
### Funcționalitate: Suport pentru gamele de culori
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Funcționalitate: Setarea stilurilor implicite, personalizate, pentru toate tipurile de straturi
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Interfața cu Utilizatorul
### Funcționalitate: O nouă temă pentru pictograme
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Funcționalitate: File laterale, grupuri retractabile
S-a standardizat aspectul filelor și s-au introdus grupurile de casete expandabile în multe dintre ferestrele de dialog, pentru a face mai ușoară setarea diferitelor opțiuni și pentru a utiliza mai bine ecranul.

![image48](images/Selection_005.png)
### Funcționalitate: Notificări discrete
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Funcționalitate: Font personalizat pentru aplicație și foaie de stil Qt: 
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Foaia de stil a interfeței aplicației, generată pentru platforma curentă, poate fi accesată după lansare (în PyQGIS):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Funcționalitate: Butoane și ferestre de alegere live a culorii
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Funcționalitate: Adnotări SVG
De acum, în QGIS 2.0 puteți adăuga adnotări SVG la harta dvs. - fie poziționându-le într-un loc specific, fie într-o poziție relativă pe suportul hărții.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Funcționalitate: Drag and drop în constructorul de formulare
QGIS 2.0 etalează un nou sistem, deosebit, pentru crearea formularelor de introducere a datelor. Cu ajutorul designer-ului drag and drop, puteți crea formulare care arată elegant, având file dedicate grupării câmpurilor comune. De acum, introducerea datelor este mult mai ușor de controlat.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Funcționalitate: Instrument de acțiuni implicite
Dacă folosiți acțiuni în straturile vectoriale (sarcini mici, care pot rula atunci când faceți clic pe o entitate), vă va plăcea noul instrument pentru acțiuni, din bara de instrumente. Cu aceasta puteți selecta o acțiune activă, după care să faceți clic pe entități pentru invocarea acțiunii.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
