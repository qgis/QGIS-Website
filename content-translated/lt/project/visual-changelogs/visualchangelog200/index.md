---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: projektą
sidebar: true
title: QGIS 2.0 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.0 pakeitimai{#changelog20 }
Laidos data: 2013-09-09

{{<table-of-contents >}}
## Analizės įrankiai
### Savybė: Apdorojimo vadovas
Greitam priėjimui prie geoapdorojimo funkcionalumo, tiesiog paleiskite apdorojimo vadovą (Ctrl + Alt + M) ir pradėkite rašyti jūsų ieškomo įrankio pavadinimą. Vadovas rodys visas galimas parinktis ir galės jas paleisti. Daugiau nereikia ieškoti meniu, norint rasti įrankius. Dabar jie visai šalia.

![image1](images/processing_commander_2.png)
### Savybė: intensyvumo žemėlapio priedo patobulinimai
Intensyvumo žemėlapio priedas buvo stipriai patobulintas ir optimizuotas, dėl ko intensyvumo žemėlapiai kuriami greičiau. Papildomai dabar galite parinkti, kuri bazinė funkcija naudojama kuriant intensyvumo žemėlapį.

![image2](images/Selection_027.png)
### Savybė: apdorojimo palaikymas
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Savybė: apdorojimo modeliuotojas
Viena iš puikių naujo apdorojimo karkaso savybių yra galimybė kombinuoti įrankius grafiškai. Naudodami **Apdorojimo modeliuotoją** jūs galite sukurti sudėtingą analizę iš eilės kelių mažų vienos užduoties modulių. Jūs galite įrašyti šiuos modelius ir tada naudoti juos kaip komponentus dar sudėtingesniuose modeliuose. Nepakartojama jėga integruota tiesiai į QGIS ir ją labai paprasta naudoti!

![image4](images/Processing_modeler_029.png)
## Programos ir projekto parinktys
### Savybė: numatyto pradinio projekto ir projekto šablono nustatymas
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Savybė: sistemos aplinkos kintamieji
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Savybė: naudotojo nurodyti masteliai
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Naršyklė
### Savybė: aplikacijos vidinės naršyklės skydelio patobulinimai
- Aplankus galima filtruoti šablonu arba reguliariomis išraiškomis
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Piktogramos nuo šiol rikiuojamos pagal elementų grupių tipus (failų sistemos, duombazės, žemėlapių serveriai)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Duomenų tiekėjai
### Savybė: rastro duomenų tiekėjo pertvarkymas
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Savybė: Oracle Spatial palaikymas
QGIS 2.0 dabar palaiko Oracle Spatial.

![image10](images/oracle.png)
### Savybė: pridėtas tinklo padengimo paslaugos WCS tiekėjas
QGIS dabar be papildomų priedų palaiko tinklo padengimo paslaugų sluoksnius - WCS pridėjimo procesas panašus į WMS ar WFS sluoksnio pridėjimą.
### Savybė: numatytas rastro 2% nukirpimas
Daug rastro nuotraukų produktų turi didelį skaičių išskirčių, dėl ko nuotraukos atrodo išplaukusios. QGIS 2.0 leidžia daug tiksliau valdyti rastrų paišymo elgseną, įskaitant ir numatytą 2% - 98% kumuliacinį nukirpimą, kai sprendžiama dėl nuotraukoje naudojamų spalvų. Ši nuotrauka rodo QGIS 1.8 (kairėje) ir QGIS 2.0 (dešinėje) tos pačios nuotraukos braižymą su numatytais nustatymais.

![image11](images/Selection_023.png)
### Savybė: WMS identifikavimo formatas
Dabar galima pasirinkti WMS sluoksnių identifikavimo rezultato formatą, jei stotis palaiko daugiau nei vieną žinomą formatą. Palaikomi formatai, tokie kaip HTML, geoobjekto (GML) ir paprasto teksto. Parinkus geoobjekto (GML) formatą, rezultatai bus tokioje pačioje formoje, kaip ir vektoriniai sluoksniai, geometrija gali būti pažymėta ir geoobjektas, įskaitant atributus, ir geometrija gali būti nukopijuota į iškarpinę ir įkelta į kitą sluoksnį.

![image12](images/wms-identify.png)
### Savybė: WMTS palaikymas
QGIS WMS klientas dabar palaiko ir WMTS (Web Mapping Tile Service), įskaitant ir duomenų poaibių, tokių kaip laiko pjūvių, parinkimą. Pridedant WMS sluoksnį iš suderinamos stoties, jūsų paprašys parinkti, kurį laiko pjūvį rodyti.

![image13](images/Selection_035.png)
## Bendra
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Užrašai
### Savybė: nauja žymėjimo sistema
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Savybė: nuo išraiškų priklausančios žymų savybės
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Prijungiamų savybių pavyzdžiai:
- Šriftas
- Dydis
- Stilius
- Buferio dydis

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Savybė: senas žymų mechanizmas išimamas
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

QGIS 2.0 seną žymų mechanizmą galima naudoti taip:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- Senoji kortelė lieka aktyvi seniems projektams, jei kuris nors sluoksnis ją naudoja. Kortelė nedingsta ne įrašius projektą be sluoksnių, kurie naudojo seną žymėjimo mechanizmą.

Seną žymėjimo kortelę galima įjungti/išjungti einamajam projektui per Python'o konsolę tokiomis komandomis:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**PASTABA**: *labai tikėtina*, kad senas žymėjimo mechanizmas bus pilnai pašalintas iki kitos stabilios QGIS versijos išleidimo. Prašome migruoti senus projektus.

![image17](images/changelog-2.0_labels-deprecated.png)
## Sluoksnių legenda
### Savybė: legendos vizualiai pateikiama informacija ir parinktys
- Geoobjektų skaičius sluoksnyje, įskaitant pasidalinimą pagal simbolį
- Vektoriniai sluoksniai, esantys redagavimo režime, turintys nepatvirtintų (neįrašytų) pakeitimų, vaizduojami su raudonu pieštuku
- Aktyvus sluoksnis dabar pabrauktas, kad būtų matomas kelių sluoksnių pažymėjime arba kai nėra jokio pažymėjimo
- Paspaudus tuščioje vietoje be elementų, pažymėjimas panaikinamas
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Grupės ir sluoksniai gali pasirinktinai būti rodomos riebiu šriftu
- Rastro sluoksnio sugeneruotos peržiūros piktogramos gali būti išjungtos projektuose, kuriuose toks paišymas yra lėtas

![image18](images/changelog-2.0_visual-options.png)
### Savybė: egzistuojančio žemėlapio sluoksnio kopijavimas
Kopijuokite parinktą vektorinį ar rastro sluoksnį žemėlapio legendoje. Tai panašu į to paties duomenų šaltinio importavimą kaip kitą sluoksnį ir stiliaus bei simbologijos atributų perkopijavimą.

![image19](images/changelog-2.0_dup-layer_1.png)
### Savybė: kelių sluoksnių redagavimo perjungimo komandos
Naudotojas dabar gali legendoje parinkti daugiau nei vieną sluoksnį ir jei kažkurie iš pažymėtų sluoksnių yra redagavimo režime - parinkti juos įrašyti, atstatyti arba nutraukti dabartinius nepatvirtintus pakeitimus. Taipogi galite nurodyti pritaikyti šiuos veiksmus visiems sluoksniams, nepriklausomai nuo pažymėjimo.

![image20](images/changelog-2.0_current-edits.png)
## Žemėlapio maketas
### Savybė: HTML žemėlapio elementai
Dabar į žemėlapį įtraukti ir html elementus.

![image21](images/Composer_1_006.png)
### Savybė: kelių puslapių palaikymas
Viename kūrėjo lange dabar gali būti daugiau nei vienas puslapis.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Savybė: išraiškos kūrėjo žymose
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Žymelė su išraiška, tokia kaip:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
bus įvertinta spausdinimo metu (ir rodymo metu), kad sugeneruotų:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Savybė: automatinis pritraukimas prie linijų
Gražiai lygiuoti žemėlapio elementai būtini kuriant gražius spausdinamus žemėlapius. Automatinės lygiavimo linijos pridėtos tam, kad leistų kūrėjo objektus gražiai lygiuoti tiesiog pertempiant objektus arčiau vieną prie kito.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Savybė: rankinio lygiavimo linijos
Kartais jūs norite sulygiuoti kūrėjo objektus. Su naujomis rankinio lygiavimo linijomis jūs galite pridėti rankinių lygiavimo linijų, kurių pagalba galėsite lygiuoti objektus pagal savo poreikius. Tiesiog tempkite iš viršaus arba šono liniuotės, kad sukurtumėte naują lygiavimo liniją.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Savybė: žemėlapių serijos generavimas
Ar jums kada nors reikėjo sukurti žemėlapių seriją? Aišku reikėjo. Kūrėjas dabar leidžia be papildomų priedų kurti žemėlapių serijas naudojant atlaso savybę. Padengimo sluoksniai gali būti taškai, linijos, poligonai, o dabartinio geoobjekto atributų duomenys prieinami žymose dinamiškam reikšmių pakeitimui.

![image26](images/Picture1.png)
### Savybė: automatinis peržiūros palaikymas žemėlapio rėme
Norite parodyti šiuo metu rodomą žemėlapio dalį mažesniame peržiūros lange? Dabar jau galite tai padaryti. Žemėlapio rėmas jau gali rodyti kito rėmo apimtis ir atsinaujinti po pajudinimo. Naudojant tai su atlaso generavimo savybe leidžia sukurti labai elegantišką žemėlapį. Peržiūros rėmo stilius naudoja tokį patį stilių kūrimo mechanizmą kaip ir normalus žemėlapio poligonas, taigi jūsų kūrybiškumas nebus ribojamas.

![image27](images/Picture1_1.png)
### Savybė: sluoksnių suliejimas
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Savybė: HTML etikečių palaikymas
Žemėlapio kūrėjo etiketės elementui pridėtas HTML palaikymas, leidžiantis dar labiau valdyti jūsų sukurtus žemėlapius. HTML etiketės pilnai palaiko css stilius, html ir net javascript, jei jums to reikia.

![image29](images/html.png)
### Savybė: kelių stulpelių kūrėjo sutartiniai ženklai
Kūrėjo sutartiniai ženklai dabar palaiko kelis stulpelius. Vieno sluoksnio su daugeliu klasių dalinimas į kelis stulpelius nėra privalomas. Vieno simbolio sluoksniai pagal nutylėjimą pridedami kaip vienos eilutės elementai. Sluoksnio/grupės pavadinimui galima priskirti vieną iš trijų stilių: grupė, pogrupis ir paslėptas. Pavadinimo stiliai leidžia vizualiai grupuoti elementus. Pavyzdžiui vieno simbolio sluoksnį galima rodyti kaip vienos eilutės elementą arba su sluoksnio pavadinimu (taip kaip 1.8 versijoje), simboliai iš kelių kitų sluoksnių gali būti grupuojami į vieną grupę (paslepiant pavadinimus) ir pan. Prie etikečių galima pridėti ir geoobjektų skaičių.

![image30](images/multicolumn-legend.png)
### Savybė: žemėlapio kūrėjo valdymo atnaujinimai
Žemėlapio kūrėjo valdymo patobulinimai:
- Kūrėjo pavadinimą dabar galima nurodyti kuriant, galima pasirinkti ir pradėti su kitais kūrėjų pavadinimais
- Galima kurti kūrėjų kopijas
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Tėvinį projektą dabar galima įrašyti tiesiai iš kūrėjo darbo erdvės
- Visi kūrėjo valdymo veiksmai prieinami tiesiai iš kūrėjo darbo erdvės

![image31](images/changelog-2.0_composer-mngmnt.png)
## Priedai
### Savybė: perdarytas priedų valdymas
QGIS 1.x priedų valdymas buvo sudėtingas, nes buvo dvi naudotojų sąsajos - viena skirta jau įdiegtų priedų valdymui, o kita - naujų python'o priedų atsiuntimui iš vienos vienintelės repozitorijos. QGIS 2.0 pristatytas **naujas, suvienytas priedų valdymas**, kurio pagalba *vienoje vietoje* galima atsisiųsti, įjungti/išjungti ir bendrai valdyti jūsų priedus. Ir beje, naudotojo sąsaja žavinga su šoninėmis kortelėmis ir lengvai atpažįstamomis piktogramomis!

![image32](images/Plugin_Manager_024.png)
## Programavimas
### Savybė: nauja python'o konsolė
Nauja Python'o konsolė suteikia dar daugiau jėgos. Dabar jau yra autoužbaigimas, sintaksės ryškinimas, keičiami šriftų nustatymai. Krašto kodo redaktorius leidžia lengviau įvesti didesnius kodo blokus su galimybe atverti ir paleisti bet kokį Python'o failą QGIS sesijoje.

![image33](images/pyconsole.png)
### Savybė: dar daugiau išraiškų funkcijų
Kadangi išraiškų variklis vis daugiau naudojamas QGIS, leidžiant tokius dalykus kaip išraiškomis valdomos etiketės ir simboliai, vis daugiau funkcijų pridedama į išraiškų kūrėją ir visos jos matomos išraiškų kūrėjų. Lengvesniam naudojimui visos funkcijos turi išsamią pagalbą ir naudojimo patarimus.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Savybė: savos išraiškų funkcijos
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Savybė: naujas švaresnis Python'o API
Python'o API buvo perdarytas, kad būtų švaresnis, su labiau „pitonišku“ programavimo jausmu. QGIS 2.0 API naudoja SIP V2, kuri pašalina nepatogią toString(), toInt() logiką, kurios anksčiau reikėjo dirbant su reikšmėmis. Tipai dabar konvertuojami į savus Python tipus, dėl ko API pasidarė daug malonesnis. Prieiga prie atributų dabar daroma pačiame geoobjekte naudojant paprastą paiešką pagal raktą, nebėra daugiau paieškų per indeksą ir atributų žemėlapių.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
Taipogi pagerintas geoobjektų skaitymas iš sluoksnio, kas leis ateities versijose dirbti keliomis gijomis.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Savybė: kodo suderinamumas su 1.x versijomis
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Savybė: Pythono projekto makro
Pythono modulis, įrašytas į projekto .qgs failą, gali būti įkeltas ir konkrečios funkcijos gali būti paleistos po šių projekto įvykių:
- `openProject()`
- `saveProject()`
- `closeProject()`

Ar makro bus vykdomi galima konfigūruoti programos parinktyse.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Simbologija
### Savybė: nuo duomenų priklausančios savybės
Naudojant naujas, nuo duomenų priklausančias savybes, galima valdyti simbolių tipą, dydį, spalvą, pasukimą ir daug kitų savybių per geoobjekto atributus.

![image39](images/datadefinedproperties2.png)
### Savybė: pagerintas simbolių sluoksnio valdymas
Nauja simbolių sluoksnio apžiūra naudoja švaresnį, medžio struktūros išdėstymą, kuris leidžia lengvesnę ir greitesnę prieigą prie simbolių sluoksnių.

![image40](images/symbollayertree.png)
### Savybė: permatomumo palaikymas spalvų apibrėžimuose
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Savybė: rastro sluoksnių spalvų kontrolė
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Savybė: kopijuoti vieno sluoksnio simbologiją į kitą sluoksnį
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Savybė: įrašyti stilių į jūsų duomenų bazę
Jei naudojate duomenų bazę vektorinių duomenų saugojimui, galite įrašyti sluoksnio stilių apibrėžimus tiesiai į duomenų bazę. Taip bus paprasčiau dalintis sluoksniais su stiliais didelių kompanijų ar kelių naudotojų aplinkose.

![image44](images/Selection_037.png)
### Savybė: spalvų rampos palaikymas
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Savybė: nustatykite savus numatytuosius stilius visiems sluoksnių tipams
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Naudotojo sąsaja
### Savybė: nauja piktogramų tema
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Savybė: šoninės kortelės, sutraukiamos grupės
Mes standartizavome kortelių išdėstymą ir įvedėme sutraukiamas grupes į daugumą mūsų dialogų, kad naršymas tarp skirtingų parinkčių būtų paprastesnis ir leistų geriau išnaudoti ekrano plotą.

![image48](images/Selection_005.png)
### Savybė: „minkšti“ pranešimai
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Savybė: programos savas šriftas ir Qt stiliai
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Sukurtas QGIS GUI programos stilius dabartinei platformai prieinamas po paleidimo (PyQGIS pagalba):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Savybė: „gyvi“ spalvų parinkimo dialogai ir mygtukai
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Savybė: SVG anotacijos
QGIS 2.0 dabar jau galima į žemėlapį įdėti SVG anotacijas - arba prisegtas prie konkrečios vietos, arba nuo žemėlapio drobės priklausančioje vietoje.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Savybė: pertempkite iš kūrėjo
QGIS 2.0 turi naują puikią duomenų įrašų kūrimo formų sistemą. Pertempimu iš formų dizainerio jūs galite sukurti gudriai atrodančias formas su kortelėmis, grupuojančiomis bendrus laukus. Dabar daug paprasčiau valdyti jūsų naudotojų duomenų įvedimą.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Savybė: numatyto veiksmo įrankis
Jei naudojate vektorinio sluoksnio veiksmus (mažas užduotis, kurios gali būti vykdomos paspaudus ant geoobjekto), jums patiks naujas veiksmo mygtukas įrankinėje. Jo pagalba galite parinkti aktyvų veiksmą ir tada spausti ant geoobjektų, kad vykdytumėte parinktą veiksmą.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
