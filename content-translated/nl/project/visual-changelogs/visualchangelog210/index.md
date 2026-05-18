---
HasBanner: false
draft: false
releaseDate: 26-06-2015
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.10{#changelog210 }
Datum uitgave 26-06-2015

Dit is het log met wijzigingen voor de volgende uitgave van QGIS - versie 2.10.0 \'Pisa\' - gastheer voor de ontmoeting van de ontwikkelaars in maart 2010.

**Laatste uitgave**

Dit is de volgende uitgave in onze 4-maandelijkse serie voor uitgaven. Het geeft u vroege toegang tot de nieuwe mogelijkheden waaraan we hebben gewerkt en vertegenwoordigt de \'cutting edge\' van de ontwikkeling van QGIS. Als u werkt in een productieomgeving waar u meer conservatief wilt zijn met betrekking tot het uitrollen van nieuwe mogelijkheden voor uw gebruikers, verschaffen we ook een Lange Termijn Release (LTR) versie van QGIS. De huidige LTR is versie 2.8.2 en is beschikbaar op [download.qgis.org](http://download.qgis.org). LTR releases zullen worden ondersteund met achterwaartse oplossingen voor problemen gedurende één jaar, en zal zich in een permanente vriesfase bevinden met betrekking tot nieuwe mogelijkheden (d.i. er worden geen nieuwe mogelijkheden toegevoegd, alleen oplossingen voor problemen en triviale bijwerkingen). De in QGIS 2.10 \'Pisa\' verschafte mogelijkheden zullen worden opgenomen in de volgende LTR-release (gepland voor release in 2016). Het gebruiken van deze release verschaft u een excellente mogelijkheid om nieuwe mogelijkheden te testen die uiteindelijk zullen worden opgenomen in de volgende LTR.

**Nieuwe mogelijkheden in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 bevat vele nieuwe mogelijkheden, aanpassingen en verbeteringen om de meest populaire gratis desktop GIS nog meer gevuld met mogelijkheden en nuttiger te maken. Wanneer aan software nieuwe mogelijkheden worden toegevoegd introduceren die de mogelijkheid tot het ontstaan van nieuwe problemen - als u in deze uitgave nieuwe problemen tegenkomt, vul dan een ticket in [op de QGIS Bug Tracker](http://hub.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOUDEN sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- ZILVEREN sponsor: [Sourcepole AG, Zwitserland](http://www.sourcepole.com/)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- ZILVEREN sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- ZILVEREN Sponsor: [AGH University of Science and Technology, Krakow, Polen](http://www.agh.edu.pl/en)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de
- BRONZEN sponsor: [www.openrunner.com, Frankrijk](http://www.openrunner.com)
- BRONZEN sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Duitsland](http://www.gkg-kassel.de/)
- BRONZEN sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZEN sponsor: [Urbsol, Australië](http://www.urbsol.com.au/)
- BRONZEN sponsor: [MappingGIS, Spanje](http://www.mappinggis.com/)
- BRONZEN sponsor: [Lutra Consulting, VK](http://www.lutraconsulting.co.uk/)
- BRONZEN sponsor: [ADLARES GmbH, Duitsland](http://www.adlares.com/)
- BRONZEN sponsor: [Avioportolano Italia, Italië](http://www.avioportolano.it/)
- BRONZEN Sponsor: [GeoSynergy, Australië](http://www.geosynergy.com.au/)
- BRONZEN Sponsor: [Gaia3D, Zuid-Korea](http://www.gaia3d.com/)
- BRONZEN Sponsor: [Royal Borough of Windsor and Maidenhead, VK](http://www.rbwm.gov.uk/)
- BRONZEN Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZEN Sponsor: [Trage Wegen vzw, België](http://www.tragewegen.be/)
- BRONZEN Sponsor: [GIS-Support, Polen](http://www.gis-support.com/)
- BRONZEN Sponsor: [GIS3W, italië](http://www.gis3w.it/)
- BRONZEN Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Duitsland](http://www.gfi-gis.de/)
- BRONZEN Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Polen](http://www.wggios.agh.edu.pl/en)

Een huidige lijst van doneren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors). Als u een officiële sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Parameters voor join kunnen nu worden bewerkt
Het is nu mogelijk om parameters voor joins (zoals een voorvoegsel voor join of kolommen die moeten worden samengevoegd) te bewerken nadat een join is gemaakt. Voorafgaand aan deze wijziging moest men de gehele join verwijderen en opnieuw maken.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Mogelijkheid: Lagen met joins kunnen nu worden gefilterd
Voorafgaand aan versie 2.10 kon een laag niet worden gefilterd als die ten minste één join had. Nu is die nog steeds te filteren, maar alleen met behulp van de kolommen van de originele hoofdtabel.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Mogelijkheid: Algemene verbeteringen
Naast de vele hieronder vermelde items zijn de volgende verbeteringen aangebracht:
- Ondersteuning voor lagen van Pointcloud in PostGIS
- Verbeterde balken voor pictogrammen en pictogrammen in vast te zetten vensters om minder schermruimte in te nemen en voor verbeterd uiterlijk op OSX
- Verbeteringen aan de plug-in / provider voor GRASS
- Ondersteuning voor niet-Latijnse scripts voor gebogen labels
- Enorm verbeterde en meer robuuste gereedschappen voor rasterberekeningen en geoverwijzingen
- Verbeterde UI en werkstroom voor het venster van de eigenschappen voor gegevensgedefinieerde labels

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Mogelijkheid: Verbeterde afhandeling van potentiële overschrijvingen van projectbestanden
QGIS 2.10 zal u nu waarschuwen wanneer u een project probeert op te slaan als de laatste datum van aanpassingen van een geladen project is gewijzigd. Dit is nuttig als meer dan één gebruiker of sessie hetzelfde project hebben geopend en beide proberen wijzigingen op te slaan in het projectbestand.

**Deze mogelijkheid werd ontwikkeld door:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Mogelijkheid: Nieuwe aandrijving voor geometrie
QGIS 2.10 heeft een nieuwe aandrijving voor geometrie. Over het algemeen zult u nog niet veel verschillen zien in de gebruikersinterface, maar dit legt de fundering voor een veel uitgebreidere set van georuimtelijke mogelijkheden die we in de toekomst zullen kunnen ondersteunen. De nieuwe implementatie ondersteunt typen gebogen geometrieën (u kunt dus bijvoorbeeld een rotonde voor verkeer weergeven als een cirkel in plaats van een gesegmenteerde polygoon die is gemaakt om eruit te zien als een cirkel) en heeft ondersteuning aan de achterzijde voor waarden Z/M in geometrieën.  U zult PostGIS of een soortgelijke gegevensopslag dienen te gebruiken die in staat is gebogen lineaire geometrieën weer te geven om bogen in QGIS te gebruiken. Als u er eens mee wilt spelen, kunt u een eenvoudige oefening zoals deze proberen in uw database van PostGIS:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Voeg dan de laag `curves` toe aan uw project.

**Deze mogelijkheid werd ontwikkeld door:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [KantonSolothurn, Zwitserland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## Analyse-gereedschappen
### Mogelijkheid: Nieuw vast te zetten widget voor statistisch overzicht
Kan een overzicht van statistieken weergeven (bijv. gemiddelde, standaardafwijking, ...) voor een veld of expressie uit een vectorlaag of selectie. Dit wordt mogelijk gemaakt door middel van een nieuw vast te zetten paneel dat u kunt activeren in het menu `Weergave -> Panelen -> Statistieken`. Onthoud dat u alleen statistieken kunt genereren in **vectorlagen** die een **numerieke kolom** hebben.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Mogelijkheid: Logaritmische functies in de rasterberekeningen gebruiken
De rasterberekeningen (`Raster -> Rasterberekeningen` in het menu van QGIS) is een gereedschap dat u in staat stelt om matrixbewerkingen uit te voeren op een of meer rasterlagen. Met QGIS 2.10 kunt u nu de functies `LN` en `LOG10` in de rasterberekeningen gebruiken.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Mogelijkheid: Nieuwe mogelijkheden gebiedsstatistieken
Gebiedsstatistieken verschaffen een manier om geaggregeerde waarden voor de pixels die onder een polygoon liggen uit te nemen. De volgende nieuwe mogelijkheden zijn toegevoegd aan ons gereedschap voor gebiedsstatistieken:
- u kunt nu selecteren welke statistieken moeten worden berekend
- extra statistieken zijn toegevoegd (mediaan, standaard afwijking, minimum, maximum, bereik, kleinste hoeveelheid, grootste hoeveelheid en variëteit)
- mogelijkheid om de rasterband te selecteren die moet worden gebruikt voor het uitnemen van de statistieken

Onthoud dat gebiedsstatistieken een 'bronplug-in' is (een plug-in die is ingebouwd in uw installatie van QGIS), maar standaard is uitgeschakeld. U dient hem in te schakelen in Plug-ins beheren en installeren en dan zal een menu-item voor gebiedsstatistieken verschijnen in het menu `Raster`.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Browser
### Mogelijkheid: Nieuw widget voor eigenschappen van de browser
Bij het gebruiken van de vast te zetten panelen voor de QGIS Browser (`Weergave -> Panelen -> Browser`), kunt u nu een widget voor eigenschappen inschakelen aan de onderzijde van de boom van het bestandssysteem. Elke gegevensbron waar u op klikt, zal zijn eigenschappen laten zien in dat paneel. Dit zorgt voor het snel en handig bekijken van de basisinformatie over de gegevensset die u heeft geselecteerd. U zou het blauwe pictogram `i` aan de bovenzijde van het paneel van de browser moeten gebruiken om de weergave van eigenschappen in-/uit te schakelen.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Mogelijkheid: Nieuw pictogram voor browser
De QGIS Browser is een afzonderlijk, zelfstandige toepassing die u in staat stelt de voor u beschikbare GIS-gegevenssets te bekijken en er doorheen te bladeren (van uw bestandssysteem, databaseverbindingen, verbindingen naar webservices etc.) In eerdere uitgaven van QGIS gebruikten we een erg soortgelijk pictogram als dat van de toepassing QGIS zelf wat een bron van verwarring is geweest voor vele gebruikers. We hebben een nieuw pictogram voor QGIS Browser gemaakt om de kans op het openen van de verkeerde toepassing te verkleinen.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Gegevensproviders
### Mogelijkheid: Verbeteringen aan DXF exporteren
Het exporteren van DXF werd doorlopend verbeterd in de laatste drie versies van QGIS. Deze versie introduceert een verbeterde SVG of eenvoudige markering voor DXF blokconversie, repareert een aantal problemen die resulteerden in incomplete (onleesbare) DXF-bestanden. In de schermafdruk kunt u links de originele weergave in QGIS zien en rechts de rendering van het geëxporteerde DXF-bestand in Autodesk TrueView.

Bekijk ook [dit artikel op qgis.ch](http://www.qgis.ch/en/projects/dxf-export) dat verklaart wat wel wordt ondersteund en wat niet.

**Deze mogelijkheid werd ontwikkeld door:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Dit werd mogelijk gemaakt door:** Gemeenschappen van Morges, Uster, Vevey en SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Mogelijkheid: Expressie-filters aan de kant van de provider voor PostGIS
In QGIS 2.10 kunt u nu objecten filteren aan de kant van de databaseserver. Alleen ondersteunde expressies zullen naar de database worden gezonden. Expressies die niet ondersteunde operatoren of functies gebruiken zullen ongemerkt terugvallen naar lokale evaluatie.

U dient deze mogelijkheid in te schakelen in `Extra -> Opties -> Databronnen` om hem te kunnen gebruiken. Als uw filterexpressie te gebruiken is in PostgreSQL, zal hij automatisch worden uitgevoerd aan de zijde van de server. U kunt ook gebruikmaken van deze mogelijkheid bij het gebruiken van de Python-API, bijvoorbeeld bij het gebruiken van deze aanroepen.

`QgsFeatureRequest().setFilterExpression( expression )`

of

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Gegevensbeheer
### Mogelijkheid: Virtuele velden kunnen nu bijgewerkt worden
Voorafgaand aan versie 2.8 diende u virtuele velden te verwijderen en opnieuw te maken als u de expressie voor het berekenen van het virtuele veld wilde wijzigen. In 2.10 kunt u nu naar de tab `Velden` gaan en drukken op de kleine knop `Expressie` om de expressiebewerker te openen en de voor het virtuele veld gebruikte expressie bij te werken.

**Deze mogelijkheid werd ontwikkeld door:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**Dit werd mogelijk gemaakt door:** [Stad Uster, Zwitserland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Mogelijkheid: Automatisch aanvullen in Wijzig hulpmiddel voor widget Waarde relatie bewerken
Het widget Waarde relatie bewerken voor vectorlagen (`Laag -> Eigenschappen -> Velden -> Tekst bewerken -> Waarde relatie`) kan nu worden ingesteld op automatisch aanvullen wanneer u begint te typen in het invoervak dat het maakt op het objectformulier.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Mogelijkheid: Verbeteringen aan DB Manager
Er zijn twee nieuwe mogelijkheden in de DB Manager :

**Query als laag geen unieke kolom integer meer nodig heeft**

Een kolom met een unieke kolom integer is niet meer nodig om een query van SQL te laden als een laag voor QGIS. Een automatisch verhoogde waarde zal in plaats daarvan worden gebruikt.

**Integratie van een SQL querybouwer**

Een nieuw venster in DB Manager helpt bij het maken van query's voor SQL door middel van widgets waar namen van tabellen, kolommen en functies kunnen worden geselecteerd door de gebruiker. Dit is geporteerd vanuit de plug-in QSpatialite en werkt voor de providers  PostGIS en Spatialite.

**Dit werd mogelijk gemaakt door**: MEDDE (French Ministry of Sustainable Development)

**Deze mogelijkheden werden ontwikkeld door**: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Mogelijkheid: Keten van filters voor widget Relatieverwijzing
Men kan de widgets voor relatieverwijzing gebruiken om gekoppelde items uit andere tabellen te selecteren. Men kan ofwel grafische elementen selecteren door ze in de kaart te selecteren, als aan het gekoppelde object een geometrie is verbonden, of een element kiezen door middel van de gekoppelde ID. Faciliteren van de niet-ruimtelijke selectie is nu mogelijk door het aantal beschikbare opties te verkleinen met filters (geketend of niet). Als de filters niet geketend zijn, worden hun keuzes gecombineerd met \"AND\" om de beschikbare opties te definiëren. Als \'geketend\' is geselecteerd, wordt een modus Opzoeken voor de filters geactiveerd, zodat elk filter alleen de items weergeeft die overeenkomen met het eerdere filter. Dit is handig bij het selecteren van hiërarchische gegevens zoals Stad -\> Straat -\> Nummer.

**Deze mogelijkheid werd ontwikkeld door:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**Dit werd mogelijk gemaakt door:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagrammen
### Mogelijkheid: Verbeteringen aan Diagrammen
De functionaliteit Diagram in QGIS maakt het u mogelijk om kleine taartdiagrammen of histogrammen over objecten op de kaart te leggen. In deze uitgave hebben we have de volgende verbeteringen voor ondersteuning van diagrammen gemaakt:
- Diagrammen kunnen worden uitgeschakeld zonder verlies van instellingen
- Keuzevak om diagrammen altijd weer te geven voor een laag toegevoegd 
- De gebruikersinterface voor diagrammen is vernieuwd om het dialoogvenster te vereenvoudigen en het meer gebruikersvriendelijk te maken
- Klassen voor diagrammen worden nu weergegeven in de legenda van de laag

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Digitaliseren
### Mogelijkheid: Verbeterd gereedschao voor draiien van geometrie
Het gereedschap voor het draaien van een geometrie is een geavanceerd gereedschap voor digitaliseren dat u in staat stelt de geometrie van een object onafhankelijk te draaien. De volgende verbeteringen zijn aan het gereedschap om te draaien gemaakt:
- u kunt nu numerieke invoer in het gereedschap om te draaien gebruiken
- u kunt een combinatievak gebruiken om de hoeken in te stellen
- ondersteuning voor snappen aan hoeken toegevoegd (direct ingeschakeld bij `gebruiken van `\shift + click\`\`)
- het anker voor de draaiing wordt gedefinieerd met `CTRL+click` en niet bij het verplaatsen van de muis

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Labelen
### Mogelijkheid: Uitlijning \"Punt volgen\" voor labels met meerdere regels
Indien ingesteld op deze modus, is de uitlijning van de tekst van labels afhankelijk van de uiteindelijke plaatsing van het label, relatief ten opzichte van het punt. Bijv, als het label links va het punt wordt geplaatst zal het label rechts worden uitgelijnd, en als het rechts van het punt wordt geplaatst dan zal het label links worden uitgelijnd. Dit verbetert de weergave van labels met meerdere regels voor puntlagen enorm.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Printvormgeving
### Mogelijkheid: Modus voor schalen van schaalbalk toegevoegd om een gewenste breedte van de schaalbalk passend te maken
In eerdere versies van QGIS was het moeilijk om grafische schaalbalken te gebruiken als het bereik van de potentiële schalen te groot was. De schaalbalk zou ofwel snel te breed of te smal zijn en men moest handmatig de segmentgrootten (eenheden per segment) aanpassen na elke wijziging in de schaal. Het betekende ook dat schaalbalken niet echt gebruikt konden worden bij het in serie afdrukken van een Atlas of met QGIS Server indien de uiteindelijke schaal onbekend was. Met QGIS 2.10 kan men nu min/max-groottes voor een segmentlengte in mm instellen en QGIS zal automatisch de eenheden per segment aanpassen met behoud van ronde waarden.

Vergeet ook niet om de uitlijning van de schaalbalk in te stellen, speciaal als u wilt dat die wordt gecentreerd of rechts uitgelijnd!

**Deze mogelijkheid werd ontwikkeld door:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programmeerbaarheid
### Mogelijkheid: Verbeteringen voor programmeurs
We hebben een aantal wijzigingen en verbeteringen gemaakt die interessant zullen zijn voor ontwikkelaars:
- We hebben de minimale vereiste voor Qt4 verhoogd naar versie 4.8. Qt4 is een van de belangrijkste C++ gereedschappen / bibliotheken die we gebruiken om QGIS te maken.
- Nieuwe klasse `QgsStatisticalSummary` voor het berekenen van statistieken uit een lijst met getallen.
- Wijzigen van de gegevensbron voor een vectorlaag mogelijk gemaakt.
- Impliciet delen van de klassen: `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plug-ins kunnen nu hun eigen items maken in de widget Browser met twee nieuwe klassen: `QgsDataItemProvider` en `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Server
### Mogelijkheid: Ondersteuning voor tolerantie-parameter in WMS GetFeatureInfo verzoeken
Bij het gebruiken van WMS-lagen, geleverd door QGIS Server, kunt u nu de tolerantie specificeren voor hoe ver van de klik-origine verzoeken GetFeatureInfo in aanmerking zouden moeten komen. Dit is belangrijk voor mobiele apparaten waar het moeilijker is om de objecten precies aan te duiden. Vóór deze nieuwe mogelijkheid was het nagenoeg onmogelijk om punt- of lijnobjecten te identificeren op een mobiel apparaat met QGISserver. U kunt de volgende parameters toevoegen aan uw verzoeken GetFeatureInfo:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

en wijzig de waarden voor tolerantie (in pixels) om aan uw behoeften te voldoen.

**Deze mogelijkheid werd ontwikkeld door:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**Dit werd mogelijk gemaakt door:** [Stad Uster, Zwitserland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Symbologie
### Mogelijkheid: Categorieën moeten overeenkomen met bestaande stijlen
Opties onder menu Categorieën van de renderer toegevoegd om categorieën in te stellen op symbolen met een overeenkomende naam uit de stijlbibliotheek of een XML-stijlbestand.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Mogelijkheid: Variëren van symboolgrootten met behulp van de renderer Gradueel
Renderers zijn het subsysteem van QGIS dat u in staat stelt rijke cartografische weergaven van uw gegevens te maken. Een renderer Gradueel varieert de symbologie, gebaseerd op een doorlopend wijzigende waarde in een vectorlaag. In eerdere versies van QGIS kon u alleen de kleur laten variëren (bijv. door een kleur van een kleurenbalk te gebruiken). In QGIS 2.10 stelt de symboolrenderer Gradueel u nu in staat om de grootte *of* de kleur te variëren. Voor puntlagen kunt u de grootte van de punt variëren, voor lijnen kunt u de breedte van de lijn variëren. Polygoonlagen behouden slechts de mogelijkheid om te variëren op kleur, lijndikte wordt nog niet ondersteund.

**Deze mogelijkheid werd ontwikkeld door:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**Dit werd mogelijk gemaakt door:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Mogelijkheid: Nieuwe optie voor het voorkomen van het automatisch afsnijden van objecten naar het kaartbereik
Deze optie (geplaatst onder het menu Geavanceerd van symbolen) schakelt het automatisch afsnijden van lijnen/polygonen naar het kaartbereik uit. In sommige gevallen resulteert dit afsnijden in niet gewenste symbologie (bijv. zwaartepuntvullingen waarbij het zwaartepunt altijd het actuele zwaartepunt van het object moet zijn).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Mogelijkheid: Schalen van grootte en draaien zijn verwijderd uit het menu Geavanceerd
We hebben `Grootte schalen` en `Draaien` verwijderd uit `` `Laag -> Eigenschappen -> tab Symbologie -> menu Geavanceerd ``. U zou in plaats daarvan draaien moeten instellen op een *per-symbool laag basis* met behulp van een expressie of veld. De gebruikte expressies in oude projecten worden geconverteerd naar eigenschappen **data-bepaalde grootte en hoek**  op symboolniveau.

**Deze mogelijkheid werd ontwikkeld door:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**Dit werd mogelijk gemaakt door:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Mogelijkheid: Datagedefinieerde eigenschappen voor markering lettertype
De meeste eigenschappen van de markering voor lettertype kunnen nu datagedefinieerd zijn, inclusief grootte, rotatie en teken van de markering.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Mogelijkheid: Visualiseren en aanpassen van de renderer Gradueel met behulp van een histogram
Een nieuwe tab Histogram is toegevoegd aan de renderer Graduaeel, die een interactief histogram van de waarden uit het toegewezen veld of expressie weergeeft. Klasse-afbrekingen kunnen met behulp van het histogram worden verplaatst of toegevoegd.

**Dit werd mogelijk gemaakt door:** [ADUGA](http://www.aduga.org)

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Mogelijkheid: Expressies voor grootte, rotatie en lijndikte op niveau van de symboollijst
Grootte en Rotatie kunnen door middle van een expressie worden gedefinieerd voor alle symboolniveaus die een markering samenstellen. Dikte kan worden gedefinieerd door een expressie voor alle symbolen die ene lijn samenstellen.

Voor symbolen wordt een legenda gegenereerd voor variërende grootten. Dit maakt een multivariate analyse van de legenda in het geval van geclassificeerde/graduele kleuren mogelijk.

Een assistent, met voorbeeld, is toegankelijk via de knop Datagedefinieerd om de gebruiker te helpen de expressie voor de grootte te definiëren. Drie methoden zijn beschikbaar: Flannery, Area en Radius.

**Deze mogelijkheid werd ontwikkeld door:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**Dit werd mogelijk gemaakt door:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Mogelijkheid: Live laageffecten voor lagen en symboollagen
Live lageneffecten zijn toegevoegd aan de reeds ruime cartografische mogelijkheden van QGIS door het toevoegen van de mogelijkheid om verscheidene effecten voor renderen toe te voegen aan de keten van renderen. Met live-effecten kunt u dingen doen als het plaatsen van valschaduwen onder uw symbool, schuin trekken en vervormen van het gerenderde symbool. U kunt deze effecten ook in lagen op elkaar leggen en instellen of het effect progressief zou moeten zijn (d.i. zichzelf toepassen op de gerenderde status tot nu toe) of discreet (door het opnieuw injecteren van de bron-geometrie terug in de keten van renderen).

**Opmerking**: Deze mogelijkheid is voor gevorderde gebruikers en we moeten opmerken dat het overmatig gebruiken van deze mogelijkheid de benodigde tijd voor renderen significant kan verlagen, overweeg dus om verschillende profielen voor symbologie voor uw laag te gebruiken - één voor het genereren van kaarten in productiekwaliteit en één voor de ontwerpmodus.

**Deze mogelijkheid werd ontwikkeld door:** [Nyall Dawson](http://nyalldawson.net/)

**Dit werd mogelijk gemaakt door:** [een initiatief voor crowd-funding](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
