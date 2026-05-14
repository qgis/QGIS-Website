---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.0{#changelog20 }
Datum uitgave 09-09-2013

{{<table-of-contents >}}
## Analyse-gereedschappen
### Mogelijkheid: Processing - Commando's
Start, voor snelle toegang tot de functionaliteit geoproccessing, de Processing Commando's (Ctrl + Alt + M) en begin met het typen van de naam van het  gereedschap waar u naar op zoek bent. Commando's toont de beschikbare opties en zal deze voor u opstarten. Het is niet langer meer nodig om te zoeken via verschillende menu's om de tools te vinden. Ze zitten direct onder uw vingertoppen.

![image1](images/processing_commander_2.png)
### Mogelijkheid: Verbeteringen plug-in Heatmap
De plug-in Heatmap is op een aantal punten verbeterd en geoptimaliseerd zodat de heatmaps (hittekaarten) sneller kunnen worden gemaakt. Aanvullend kunt u nu kiezen welke kernel-functie gebruikt moet worden om de heatmap aan te maken.

![image2](images/Selection_027.png)
### Mogelijkheid: Ondersteuning voor Processing
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Mogelijkheid: Processing - Grafische modellen bouwen
Een prachtig onderdeel van het nieuwe framework Processing is de mogelijkheid om de gereedschappen grafisch te combineren. Gebruik makende van de Processing Grafische modellen bouwen kunt u complexe analyses bouwen door grafisch een aantal kleinere analysegereedschappen te combineren. Gebouwde modellen kunt u opslaan en vervolgens weer gebruiken als een analyseblokje van nog ingewikkelde modellen. De Processing Grafische modellen bouwen is een zeer krachtig geïntegreerd onderdeel in |qg| en eenvoudig te gebruiken!

![image4](images/Processing_modeler_029.png)
## Opties voor toepassing en projecten
### Mogelijkheid: Standaard opstartproject en projectsjablonen definiëren
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Mogelijkheid: Systeem omgevingsvariabelen
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Mogelijkheid: gebruikergedefinieerde zoomschalen
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Browser
### Mogelijkheid: Verbeteringen aan browser paneel binnen toepassing
- Mappen kunnen worden gefilterd met een wildcard (=jokerteken) of een reguliere expressie
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Iconen zijn nu ingedeeld per groepstype (bestandssysteem, databases, map servers)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Gegevensproviders
### Mogelijkheid: Raster-gegevensprovider vernieuwd
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Mogelijkheid: Ondersteuning voor Oracle Spatial
QGIS 2.0 bevat nu ondersteuning voor Oracle Spatial.

![image10](images/oracle.png)
### Mogelijkheid: Provider voor Web Coverage Service toegevoegd
QGIS ondersteunt nu standaard ook lagen van Web Coverage Service - het toevoegen van een WCS gebeurt op gelijke wijze als voor een laag van WMS of WFS.
### Mogelijkheid: Raster standaard 2% cumulatief afgesneden
Veel rasterafbeeldingen hebben een groot aantal uitschieters die zorgen voor een vage weergave. QGIS 2.0 introduceert een meer precieze controle over het gedrag bij renderen/tekenen van een raster, waarbij alleen de kleuren die standaard vallen in het cumulatieve kleurenspectrum tussen de 2% - 98% procent worden meegenomen en die daardoor zorgen voor een meer heldere weergave. De hier weergegeven afbeelding geeft QGIS 1.8 (links) weer versus QGIS 2.0 (rechts) bij het renderen van dezelfde afbeelding met standaard instellingen.

![image11](images/Selection_023.png)
### Mogelijkheid: Indeling identificatie WMS 
Het is nu mogelijk om het gereedschap Objecten identificeren te gebruiken voor lagen van WMS als meerdere bekende indelingen worden ondersteund door de server. De ondersteunde indelingen zijn HTML, objecten (GML) en tekst. Wanneer de indeling objecten (GML) is geselecteerd wordt het resultaat weergegeven in dezelfde vorm als vectorlagen, de geometrie kan worden geaccentueerd en de objecten, inclusief attribuutwaarden en geometrie, kunnen gekopieerd worden naar het klembord en geplakt worden in een andere laag. 

![image12](images/wms-identify.png)
### Mogelijkheid: Ondersteuning voor WMTS
De WMS-cliënt in QGIS ondersteunt WMTS (Web Mapping Tile Service) waarbij de selectie van sub-gegevenssets ook wordt ondersteund zoals welk gedeelten van tijd getoond moet worden. Bij het toevoegen van een WMS-laag vanaf een daartoe geschikte server zult u worden gevraagd om het gedeelte van de tijd te selecteren dat weergegeven moet worden.

![image13](images/Selection_035.png)
## Algemeen
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Labelen
### Mogelijkheid: Nieuw systeem voor labels
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Mogelijkheid: Op expressie gebaseerd labeleigenschappen
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Voorbeelden van gebonden eigenschappen omvatten:
- Lettertype
- Grootte
- Stijl
- Grootte van buffer

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Mogelijkheid: Oude systeem voor labels vervallen
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

De volgende richtlijnen voor het werken met de oude mogelijkheid gelden in QGIS 2.0:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- De vervallen tab blijft echter actief voor projecten opgeslagen in een oudere versie waarin een vectorlaag deze oudere manier van labelen nog gebruikt en gaat ook niet weg wanneer het project wordt opgeslagen zonder lagen die de oude manier van labelen hebben ingeschakeld.

De vervallen tab voor labels kan worden in-/uitgeschakeld voor het huidige project, via Python consoleopdrachten, bijv.:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**OPMERKING**: Er is een *grote kans* dat de oudere manier van labels snel zal worden verwijderd, voorafgaande aan de volgende stabiele versie van |qg|. Migreer derhalve de oudere projecten.

![image17](images/changelog-2.0_labels-deprecated.png)
## Legenda van laag
### Mogelijkheid: Legenda visuele info en opties
- Totaal aantallen objecten in een laag en ook per symbool
- Vectorlagen in mode bewerken, hebben nu een rood potlood om aan te geven dat er nog niet opgeslagen wijzigingen aanwezig zijn.
- De actieve laag wordt nu onderlijnd zodat deze is aangegeven zelfs wanneer er meerdere lagen zijn geselecteerd of geen laag is geselecteerd
- Door te klikken in de witruimte van de legenda van niet-lijst onderdelen wordt de selectie ongedaan gemaakt
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Groepen en lagen kunnen nu optioneel in een vet lettertype worden weergegeven
- Voor Rasterlagen gemaakte voorbeeldpictogrammen kunnen nu uitgezet worden, omdat het tekenen daarvan vertragend kan werken

![image18](images/changelog-2.0_visual-options.png)
### Mogelijkheid: Bestaande kaartlaag dupliceren
Geselecteerde vector- en rasterlaag in de kaartlegenda dupliceren. Vergelijkbaar met het nogmaals inlezen van dezelfde kaart, als een afzonderlijke laag, maar daarbij worden dan ook de stijl en attributen voor symbologie mee gekopieerd.

![image19](images/changelog-2.0_dup-layer_1.png)
### Mogelijkheid: Meerdere lagen schakelopdrachten voor bewerken
Een gebruiker kan nu meerdere lagen selecteren in de legenda en, als er een aantal daarvan in de modus Bewerken staan, kiezen om wijzigingen op te slaan, terug te draaien of nog niet opgeslagen wijzigingen ongedaan maken. De gebruiker kan er ook voor kiezen om deze acties over alle lagen uit te voeren, ongeacht de selectie.

![image20](images/changelog-2.0_current-edits.png)
## Printvormgeving
### Mogelijkheid: HTML-items
U kunt nu HTML-elementen op uw kaart plaatsen.

![image21](images/Composer_1_006.png)
### Mogelijkheid: Ondersteuning voor meerdere pagina's
Één venster van Printvormgeving kan nu meer dan één pagina bevatten.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Mogelijkheid: Expressies in labels Printvormgeving
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Een label met een expressie als:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
zal bij afdrukken (en weergeven) worden geëvalueerd om te genereren:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Mogelijkheid: Automatisch snappen aan lijnen
Kaartonderdelen goed uitgelijnd te krijgen is essentieel voor het afdrukken van mooie kaarten. Lijnen om automatisch aan te snappen zijn toegevoegd om het mogelijk te maken objecten voor de lay-out beter uit te lijnen door een object dicht naar een ander object te slepen.  

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Mogelijkheid: Handmatig snappen aan lijnen
Soms is het nodig om objecten op een bepaalde afstand uit te lijnen in de Printvormgeving. Met het nieuwe handmatige snappen aan lijnen kunt u handmatig snaplijnen toevoegen die een betere gelijke uitlijning van objecten mogelijk maakt. Sleep eenvoudig van de bovenkant of van de liniaal aan de zijkant een nieuwe snaplijn in de kaart. 

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Mogelijkheid: Serie kaarten genereren
Ooit een serie kaarten in één keer moeten genereren? Natuurlijk heeft u dat al eens gedaan. De Printvormgeving bevat nu het generen van een serie kaarten waarbij gebruik wordt gemaakt van de functionaliteit Atlas. De af te drukken gebiedslagen kunnen punten, lijnen, polygoonvlakken zijn en de actieve object gegevens van attributen zijn beschikbaar in labels die dynamisch door een waarde vervangen kunnen worden.

![image26](images/Picture1.png)
### Mogelijkheid: Ondersteuning voor automatische overzichtskaarten in kaartframe
Behoefte om te laten zien waar het getoonde gebied van de hoofdkaart zich bevindt in een kleinere overzichtskaart. Het kaartframe heeft nu de mogelijkheid om een ander bereik te selecteren waarbij dit automatisch wordt bijgewerkt bij verplaatsing. Indien gebruikt in combinatie met Atlas-generatie, wat eveneens een standaard onderdeel is geworden van de Printvormgeving kunt u erg mooie kaarten maken. De mogelijke stijlen die gebruikt kunnen worden voor het maken van het frame van de overzichtskaart zijn dezelfde als voor een normaal polygoon object, dus uw creatitviteit wordt nooit beperkt. 

![image27](images/Picture1_1.png)
### Mogelijkheid: Laag mengen
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Mogelijkheid: Ondersteuning voor HTML in labels
HTML-ondersteuning is toegevoegd voor labels in Printvormgeving voor nog meer controle over de uiteindelijke kaart. De HTML ondersteuning voor labels bevat het gebruik van CSS-stylesheets, HTML en zelfs het gebruik van Javascript.

![image29](images/html.png)
### Mogelijkheid: Meerdere kolommen voor legenda van Printvormgeving
De legenda in de Printvormgeving ondersteunt nu het gebruik van een legenda die is opgebouwd uit meerdere kolommen. Opsplitsen van een enkele laag, die bestaat uit veel klassen is optioneel. Enkele symboollagen worden standaard als item van één regel toegevoegd. Drie verschillende stijlen kunnen worden toegevoegd aan een laag/groep titel: Groep, Subgroep of Verborgen. Met de titels voor de legenda kunnen kaartonderdelen in de legenda onderverdeeld worden in groepen. Een laag met een enkel symbool kan getoond worden als een labelitem bestaand uit 1 regel of met een een laagtitel (zoals in 1.8), vervolgens kunnen volgende lagen gegroepeerd worden tot één enkele groep (door het verbergen van de titels etc.) Een telling van het aantal kaartobjecten kan toegevoegd worden aan de titel.

![image30](images/multicolumn-legend.png)
### Mogelijkheid: Beheer van Printvormgeving bijgewerkt
De volgende verbeteringen zijn gemaakt aan het beheer van Printvormgeving:
- De naam van Printvormgeving kan nu worden gegeven bij het aanmaken ervan, waarbij optioneel gekozen kan worden uit andere namen voor Printvormgeving
- Lay-outs kunnen nu worden gedupliceerd
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Het ouder-project kan direct worden opgeslagen vanuit de werkruimte van Printvormgeving
- Alle beheersacties voor printvormgeving zijn direct beschikbaar vanuit de werkruimte van Printvormgeving

![image31](images/changelog-2.0_composer-mngmnt.png)
## Plug-ins
### Mogelijkheid: Vernieuwd beheer plug-ins
In |qg| 1.x was het beheren van plug-ins enigszins verwarrend door het gebruik van twee menu's. Één menu voor het beheren van geïnstalleerde plug-ins en één voor het ophalen van nieuwe plug-ins uit de opslagplaats van plug-ins. In |qg| 2.0 is er één samengevoegde plug-in manager waarmee je het volledige beheer voor plug-ins kunt doen; zoeken, downloaden, in-/uitschakelen. En daarnaast ziet de gebruikersinterface er super uit met zij-tabbladen en eenvoudig te herkennen pictogrammen!

![image32](images/Plugin_Manager_024.png)
## Programmeerbaarheid
### Mogelijkheid: Nieuwe console voor Python
De nieuwe console  voor Python geeft u nog meer controle. Deze heeft nu de functie Automatisch aanvullen, markering voor syntaxis en het lettertype kan worden aangepast. Er is ook een codebewerker toegevoegd waarmee grotere stukken code voor Python kunnen worden geschreven en bestanden van Python kunnen worden geladen en gestart in de sessie van |qg|. 

![image33](images/pyconsole.png)
### Mogelijkheid: Nog meer functies voor expressies
De expressie engine wordt op steeds meer plekken in |qg| beschikbaar, waarmee bijvoorbeeld labels kunnen worden opgebouwd met gebruik van reguliere expressies,  waarbij de expressiebouwer een belangrijk hulpmiddel is. Voor alle functies  voor expressies zijn uitvoerige helpteksten  en gebruiksaanwijzingen beschikbaar.  

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Mogelijkheid: Aangepaste functies voor expressies
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Mogelijkheid: Nieuwe opgeruimde Python API
De Python API is aangepast zodat deze nog meer overeenkomt met standaarden voor Python die zorgen voor een betere beleving van het programmeren in Python. |qg| 2.0 gebruikt SIP V2  die onder andere voor zorgt dat er minder conversies van waarden nodig zijn met functies zoals toString(), toInt(). Typen worden nu direct geconverteerd naar standaardtypen voor Python die zorgen voor een prettigere API. Het opvragen van veldwaarden kan nu bijvoorbeeld gebeuren op het object zelf met een eenvoudige sleutelwaarde waar dat voorheen een stuk lastiger was waarbij indexen en attributen maps moesten worden gebruikt.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
De manier waarop objecten uit een laag worden gelezen is ook verbeterd, wat multithreading in de toekomstige versies mogelijk maakt.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Feature: Compatibiliteit code met uitgaven versie 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Mogelijkheid: Python projectmacro's
Een module voor Python, die mee wordt opgeslagen in een project.qgs bestand, kan worden geladen en kan functies bevatten die worden gestart tijdens de volgende project events:
- `openProject()`
- `saveProject()`
- `closeProject()`

Of de macro's moeten worden uitgevoerd kan worden ingesteld via de opties voor de toepassing.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Symbologie
### Mogelijkheid: Data-bepaalde eigenschappen
Met de nieuwe data-gedefinieerde eigenschappen, is het mogelijk om symbooltype, grootte, kleur, rotatie en veel andere eigenschappen in te stellen via de attributen van de objecten.

![image39](images/datadefinedproperties2.png)
### Mogelijkheid: Beheer symboollagen verbeterd
Het nieuwe overzicht van symboollagen gebruikt een duidelijke boomstructuur die eenvoudige en snelle toegang geeft tot alle symboollagen. 

![image40](images/symbollayertree.png)
### Mogelijkheid: Ondersteuning voor transparantie in kleurdefinities
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Mogelijkheid: Kleurbeheer voor rasterlagen
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Mogelijkheid: Symbologie tussen lagen kopiëren
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Mogelijkheid: Stijl in uw database opslaan
Als u vectorgegevens opslaat in een database, dan kan nu ook de stijldefinitie van de laag direct mee worden opgeslagen. Dit maakt het eenvoudig om lagen met de gegeven stijl te delen binnen een ondernemings-omgeving of met meerdere gebruikers.

![image44](images/Selection_037.png)
### Mogelijkheid: Ondersteuning voor kleurovergangen
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Mogelijkheid: Standaard stijlen instellen voor alle typen lagen
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Gebruikersinterface
### Mogelijkheid: Nieuw thema pictogram
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Mogelijkheid: Zij-tabs, in te klappen groepen
We hebben de lay-out van tabbladen gestandaardiseerd en de inklapbare groepen geïntroduceerd in veel van onze dialogen om het navigeren door de verschillende opties makkelijker te maken en ook beter gebruik te maken van het scherm. 

![image48](images/Selection_005.png)
### Mogelijkheid: Zachte mededelingen
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Mogelijkheid: Aangepast lettertype voor applicatie en Qt-stylesheet
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Toegang tot het gegenereerde QGIS GUI-toepassing stylesheet voor het huidige platform kan worden verkregen nadat het is opgestart (in PyQGIS):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Mogelijkheid: Live dialoogvensters voor kleurkeuze en knoppen
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Mogelijkheid: SVG-annotaties
Met |qg| 2.0 kunt u nu SVG-labels toevoegen aan de kaart - ofwel plaatsgebonden of op een relatieve positie in het kaartvenster.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Mogelijkheid: Formulieren bouwen met slepen en neerzetten
QGIS 2.0 ondersteunt ene fantastisch nieuw systeem voor het maken van formulieren voor invoer van gegevens. Met de formulierontwerper die kan slepen en neerzetten kunt u goed uitziende formulieren maken met tabs om algemene velden te groeperen. Het is nu veel eenvoudiger om de ervaring va het invoeren van gegevens door uw gebruikers te beheren.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Mogelijkheid: Gereedschap Standaardactie
Als u een gebruiker bent van acties op vectorlagen (kleine taken die kunnen worden uitgevoerd als u op ene object klikt), zult u blij zijn met het nieuwe gereedschap Actie op de werkbalk. Daarmee kunt u een actieve actie selecteren en dan op uw objecten klikken om die actie uit te voeren.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
