---
HasBanner: false
draft: false
releaseDate: 09-09-2013
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
Het project SEXTANTE is geport en nu ook in QGIS ingebouwd als brononderdeel. SEXTANTE is hernoemd naar \'Processing\' en introduceert een nieuw menu in QGIS van waaruit u toegang heeft tot een rijke gereedschapskist met gereedschappen voor ruimtelijke analyses. De Toolbox van Processing bevat veel functionaliteit die verder uitgebreid kan worden doordat de Python API het toestaat om toegang te bieden tot open source-gereedschap beschikbaar in GRASS, OTB, SAGA enzovoorts en nieuwe analysetools toe te voegen. 

![image3](images/Selection_028.png)
### Mogelijkheid: Processing - Grafische modellen bouwen
Een prachtig onderdeel van het nieuwe framework Processing is de mogelijkheid om de gereedschappen grafisch te combineren. Gebruik makende van de Processing Grafische modellen bouwen kunt u complexe analyses bouwen door grafisch een aantal kleinere analysegereedschappen te combineren. Gebouwde modellen kunt u opslaan en vervolgens weer gebruiken als een analyseblokje van nog ingewikkelde modellen. De Processing Grafische modellen bouwen is een zeer krachtig geïntegreerd onderdeel in |qg| en eenvoudig te gebruiken!

![image4](images/Processing_modeler_029.png)
## Opties voor toepassing en projecten
### Mogelijkheid: Standaard opstartproject en projectsjablonen definiëren
Met QGIS 2.0 kunt u specificeren wat |qg| moet doen bij het opstarten: `Nieuw project` (als vanouds, start met een nieuw leeg project), `Meest recent` (wanneer u QGIS start zal het het laatst geopende project weer openen), `Specifiek` (altijd een specifiek project laden wanneer QGIS wordt gestart). U kunt een projectmap voor sjablonen instellen waarin u uw sjablonen voor het project kunt bewaren. Elk project dat daarin is bewaard kan gekozen worden in de lijst van sjabloonprojecten die wordt getoond als in het menu `Project --> Nieuw van sjabloon` wordt geselecteerd.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Mogelijkheid: Systeem omgevingsvariabelen
De systeem-omgevingsvariabelen kunnen nu worden bekeken en deze kunnen ook worden geconfigureerd via het dialoogvenster Opties. Dit is erg handig voor besturingssystemen zoals die op de Mac waarbij een grafische toepassing niet automatisch de omgevingsvariabelen erft van de shell-omgeving van de gebruiker. Ook handig om omgevingsvariabelen in te stellen die gebruikt worden door externe gereedschappen die o.a. gebruikt worden door de Processing Toolbox, bijv. SAGA, GRASS; en ook voor het meer uitvoer genereren voor het opsporen van fouten voor bepaalde gedeelten van de broncode.  

![image6](images/changelog-2.0_sys-env-options.png)
### Mogelijkheid: gebruikergedefinieerde zoomschalen
Een lijst van schaalniveaus kan nu worden ingesteld voor de toepassing en ook per project. De lijst van schaalniveaus zal worden weergegeven in het pop-upcombinatievak `Schaal` in de statusbalk van het hoofdvenster voor snelle toegang tot bekende schalen voor efficiënt weergeven en werken met de huidige gegevensbronnen. Gedefinieerde schaalniveaus kunnen worden geëxporteerd naar een XML bestand dat kan worden geïmporteerd in andere projecten of een andere toepassing van QGIS.

![image7](images/changelog-2.0_predefined-scales.png)
## Browser
### Mogelijkheid: Verbeteringen aan browser paneel binnen toepassing
- Mappen kunnen worden gefilterd met een wildcard (=jokerteken) of een reguliere expressie
- Nieuw `Thuis voo project` (oudermap van huidige project)
- Bekijk `Eigenschappen` van de geselecteerde map in een dialoogvenster
- Kiezen voor welke mappen `Snel scannen` moet worden uitgevoerd
- Kiezen voor `Map toevoegen` aan `Favorieten` via standaard bestandsdialoogvenster
- Nieuwe `/Volumes` op de Mac (verborgen map voor toegang tot externe opslag)
- Nieuwe groep `OWS` (samenvoeging van beschikbare verbindingen voor kaartservers)
- Een tweede browser openen (`Beeld -> Panelen -> Browser (2)`) zodat men gegevensbronnen tussen de twee browserpanelen kan slepen en neerzetten
- Iconen zijn nu ingedeeld per groepstype (bestandssysteem, databases, map servers)
- `Laageigenschappen` heeft nu een betere visuele indeling

![image8](images/changelog-2.0_browser.png)
## Gegevensproviders
### Mogelijkheid: Raster-gegevensprovider vernieuwd
De rastergegevensprovider is volledig op de schop gegaan. Een van de beste nieuwe functies die hieruit voortkomt, is de mogelijkheid via \'Laag -> Opslaan als\...\' elke rasterlaag op te slaan als een nieuwe laag. Tijdens het opslaan kunt u daarbij een bewerking clippen uitvoeren (knippen met masker), resamplen (andere kleurenindeling) en de laag projecteren naar een ander Coördinaten Referentie Systeem. U kunt ook een rasterlaag opslaan als een gerenderde afbeelding. Bijvoorbeeld nadat een eenbandsraster, waar een kleurenpalet is toegepast, kunt u deze gerenderde afbeelding opslaan als een RGB-rasterlaag met geoverwijzingen.

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
### Mogelijkheid: Quantum GIS is nu nog alleen bekend als \'QGIS\'
Het \'Quantum\' in \'Quantum GIS\' had eigenlijk geen bijzondere betekenis en doordat ons project twee verschillende namen kende, `Quantum GIS` en `QGIS`, veroorzaakte dat alleen maar verwarring. Als onderdeel van het verder stroomlijnen van het project is officieel besloten het woord `Quantum` niet langer meer te gebruiken. Het project gaat voortaan verder als `QGIS` (in hoofdletters). Alle code en gepubliceerd materiaal zal hierop worden aangepast.

![image14](images/qgis.png)
## Labelen
### Mogelijkheid: Nieuw systeem voor labels
Het nieuwe systeem voor labels is grondig verbouwd - het bevat nu veel nieuwe functionaliteit als achtergrondschaduwen, wegmarkeringen, veel meer datagerelateerde opties en verschillende verbeteringen voor de uitvoering. De \'oude\' manier van labels zijn we zo langzamerhand aan het verlaten, maar het is er nog wel in deze uitgave. Maar houd er rekening mee dat deze in de volgende uitgave is verdwenen. 

![image15](images/Layer_labeling_settings_003_1.png)
### Mogelijkheid: Op expressie gebaseerd labeleigenschappen
De volledige kracht van de normale labels en regelexpressies kunnen nu ook voor labeleigenschappen worden gebruikt. Bijna elke eigenschap kan nu worden ingesteld met een expressie of een veldwaarde, zodat u meer controle heeft over het resultaat van het label. Expressies kunnen verwijzen naar een veld (bijv. de lettergrootte afhankelijk maken van de waarde van het veld \'lettertype\') of kunnen een veel complexere logica bevatten.

Voorbeelden van gebonden eigenschappen omvatten:
- Lettertype
- Grootte
- Stijl
- Grootte van buffer

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Mogelijkheid: Oude systeem voor labels vervallen
Gebruik van de oudere manier van labelen, zoals beschikbaar in QGIS \<= 1.8  wordt afgeraden (komt te vervallen), maar is nog niet verwijderd. Het bestaat nog, zodat gebruikers de mogelijkheid hebben om hun projecten bij te werken, waarbij de oudere manier van labelen wordt vervangen door de nieuwe manier.

De volgende richtlijnen voor het werken met de oude mogelijkheid gelden in QGIS 2.0:
- De tab Labels wordt niet langer getoond in het menu Eigenschappen voor vectorlagen, wanneer het een nieuw project betreft of een ouder, geopend project waarbij de oudere manier van labelen niet is gebruikt.
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
- `Klikken met rechts` wordt nu hetzelfde behandeld als `klikken met links`, voorheen voor het starten van het contextuele snelmenu, zodat met één muisklik hetzelfde kan worden bereikt als voorheen met twee muisklikken
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
Het label in Printvormgeving in 1.8 was nogal beperkt en alleen \$CURRENT\_DATE kon worden gebruikt. In 2.0 is volledige ondersteuning voor expressies toegevoegd, waarmee men veel meer controle heeft gekregen over de te plaatsen labels. 

Een label met een expressie als:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
zal bij afdrukken (en weergeven) worden geëvalueerd om te genereren:

    This was printed on: 06.09.2013
    
Als Atlas-generatie is ingeschakeld, zullen de waarden van attributen van de huidige actieve objecten ook toegankelijk zijn in de expressies, wat dingen mogelijk maakt als:

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
Het mengen van lagen maakt het mogelijk om lagen te combineren op nieuwe, verrassende manieren. In de oudere versies kon je lagen transparant maken, maar nu kun je kiezen uit veel geavanceerdere manieren zoals \"multiply\", \"darken only\" en nog veel meer.

Mengen kan worden gebruikt in de normale kaartweergave, maar ook in Printvormgeving. Bekijk, voor een korte handleiding over hoe mengen te gebruiken om het meeste uit de achtergrond te halen, [\"Vintage map design using QGIS"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

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
- `Nieuw uit sjabloon` en van `Specifiek` (in Lay-out beheren) maakt een printvormgeving vanuit een reeds opgeslagen sjabloon
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
Wanneer de expressie-engine niet die functie heeft die u nodig hebt, kan er een nieuwe functie worden toegevoegd via een plug-in, met behulp van een eenvoudige Python API.

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
Omdat dit een major release betreft, is de API niet volledig compatibel met de voorgaande versies 1.x. In de meeste gevallen is het porten van de code vrij eenvoudig - u kunt om te beginnen [deze handleiding](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) gebruiken als start. Ga naar de developer mailinglijst als u meer hulp nodig hebt.

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
Op de meeste plaatsen in QGIS waar je kleuren kunt kiezen, kun je nu ook het alfakanaal instellen (waarmee je de mate van transparantie kunt instellen). Dit draagt bij aan het maken van kaarten die er erg goed uitzien, waarbij u ook gegevens kunt verbergen waarvan u niet wilt dat die zichtbaar zijn voor gebruikers.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Mogelijkheid: Kleurbeheer voor rasterlagen
QGIS 2.0 geeft u meer controle over hoe de rasterlagen eruit komen te zien. U hebt nu de volledige controle over lichtsterkte, contrast en verzadiging van kleuren van rasterlagen. Er zijn ook opties die rasters kunnen tonen in grijstinten of in een bepaalde kleur.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Mogelijkheid: Symbologie tussen lagen kopiëren
Het is nu erg simpel geworden om de symbologie van de ene naar een andere laag te kopiëren. Wanneer u werkt met meerdere gelijksoortige lagen, kunt u `met rechts klikken` op een laag, de optie `Stijl kopiëren` kiezen en deze, via `met rechts klikken`, in een andere laag overbrengen met de optie `Stijl plakken`. 

![image43](images/Selection_034.png)
### Mogelijkheid: Stijl in uw database opslaan
Als u vectorgegevens opslaat in een database, dan kan nu ook de stijldefinitie van de laag direct mee worden opgeslagen. Dit maakt het eenvoudig om lagen met de gegeven stijl te delen binnen een ondernemings-omgeving of met meerdere gebruikers.

![image44](images/Selection_037.png)
### Mogelijkheid: Ondersteuning voor kleurovergangen
Kleurovergangen zijn nu beschikbaar op veel plaatsen onder QGIS instellingen voor symbologie, en QGIS komt met een rijke set aan kleurovergangen. U kunt ook uw eigen kleurovergang ontwerpen en veel cpt-city thema's voor [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) zijn nu \'out of the box\' toegevoegd in QGIS. De kleurovergangen ondersteunen ook transparantie!

![image45](images/Selection_038.png)
### Mogelijkheid: Standaard stijlen instellen voor alle typen lagen
Nu laat QGIS u beheren hoe nieuwe lagen zullen worden getekend als zij geen bestaande stijl `.qml` hebben gedefinieerd. U kunt ook de standaardtransparantie die moet worden toegekend aan nieuwe lagen instellen en of symbolen willekeurige kleuren toegekend moeten krijgen.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Gebruikersinterface
### Mogelijkheid: Nieuw thema pictogram
We hebben ons thema voor pictogrammen bijgewerkt om het thema \'GIS\' te gebruiken, zodat de gebruikersinterface van QGIS een meer consistent en professioneler uiterlijk heeft gekregen.

![image47](images/Selection_001_1.png)
### Mogelijkheid: Zij-tabs, in te klappen groepen
We hebben de lay-out van tabbladen gestandaardiseerd en de inklapbare groepen geïntroduceerd in veel van onze dialogen om het navigeren door de verschillende opties makkelijker te maken en ook beter gebruik te maken van het scherm. 

![image48](images/Selection_005.png)
### Mogelijkheid: Zachte mededelingen
In veel gevallen willen we een mededeling doen, maar we willen niet dat dit uw werkzaamheden onderbreekt. Met het nieuwe systeem voor mededelingen kan QGIS belangrijke informatie via een gele berichtenbalk, die zich boven het kaartvenster bevindt, tonen. Maar zo'n mededeling zal uw werkzaamheden niet onderbreken wanneer u ergens anders mee bezig bent. Ontwikkelaars kunnen ook mededelingen maken die getoond worden (bijvoorbeeld vanuit de plug-in) via onze Python-API. 

![image49](images/Selection_030.png)
### Mogelijkheid: Aangepast lettertype voor applicatie en Qt-stylesheet
Het systeemlettertype voor de gebruikersinterface van de toepassing kan nu worden ingesteld. Elke plug-in voor C++ of Python die een kind is van de QGIS GUI-toepassing of die het GUI-stylesheet van de toepassing heeft gekopieerd/toegepast, kan de stijl erven. Dit is erg handig, zodat de GUI kan worden aangepast voor de verschillende platformen en wanneer aangepaste QGIS Qt-widgets worden gebruikt, zoals de `QgsCollapsibleGroupBox`.

Toegang tot het gegenereerde QGIS GUI-toepassing stylesheet voor het huidige platform kan worden verkregen nadat het is opgestart (in PyQGIS):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Mogelijkheid: Live dialoogvensters voor kleurkeuze en knoppen
Elke knop voor het kiezen van kleuren van de toepassing is bijgewerkt, zodat direct zichtbaar wordt wat er is gewijzigd of wanneer de huidige kleur een transparante, of \'alfa\'-component heeft. De kleurenkeuze opent nu standaard met de nieuwe kleurenknoppen zoals ingesteld voor het besturingssysteem. Als de gebruiker de optie `Gebruik directe kleurenkeuzedialogen bijwerken` selecteert onder `Opties -> Algemeen -> Applicatie` dan zal elke wijziging in de kleurenkeuze direct zichtbaar zijn in de kleurenknoppen en elk object dat wordt bewerkt waar toepasbaar.

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
