---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.10{#changelog210 }
Datum uitgave 26-06-2015

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Laatste uitgave**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
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

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Parameters voor join kunnen nu worden bewerkt
Het is nu mogelijk om parameters voor joins (zoals een voorvoegsel voor join of kolommen die moeten worden samengevoegd) te bewerken nadat een join is gemaakt. Voorafgaand aan deze wijziging moest men de gehele join verwijderen en opnieuw maken.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Mogelijkheid: Lagen met joins kunnen nu worden gefilterd
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

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

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Mogelijkheid: Nieuwe aandrijving voor geometrie
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
## Analyse-gereedschappen
### Mogelijkheid: Nieuw vast te zetten widget voor statistisch overzicht
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Mogelijkheid: Logaritmische functies in de rasterberekeningen gebruiken
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Mogelijkheid: Nieuwe mogelijkheden gebiedsstatistieken
Gebiedsstatistieken verschaffen een manier om geaggregeerde waarden voor de pixels die onder een polygoon liggen uit te nemen. De volgende nieuwe mogelijkheden zijn toegevoegd aan ons gereedschap voor gebiedsstatistieken:
- u kunt nu selecteren welke statistieken moeten worden berekend
- extra statistieken zijn toegevoegd (mediaan, standaard afwijking, minimum, maximum, bereik, kleinste hoeveelheid, grootste hoeveelheid en variëteit)
- mogelijkheid om de rasterband te selecteren die moet worden gebruikt voor het uitnemen van de statistieken

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Browser
### Mogelijkheid: Nieuw widget voor eigenschappen van de browser
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Mogelijkheid: Nieuw pictogram voor browser
De QGIS Browser is een afzonderlijk, zelfstandige toepassing die u in staat stelt de voor u beschikbare GIS-gegevenssets te bekijken en er doorheen te bladeren (van uw bestandssysteem, databaseverbindingen, verbindingen naar webservices etc.) In eerdere uitgaven van QGIS gebruikten we een erg soortgelijk pictogram als dat van de toepassing QGIS zelf wat een bron van verwarring is geweest voor vele gebruikers. We hebben een nieuw pictogram voor QGIS Browser gemaakt om de kans op het openen van de verkeerde toepassing te verkleinen.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Gegevensproviders
### Mogelijkheid: Verbeteringen aan DXF exporteren
Het exporteren van DXF werd doorlopend verbeterd in de laatste drie versies van QGIS. Deze versie introduceert een verbeterde SVG of eenvoudige markering voor DXF blokconversie, repareert een aantal problemen die resulteerden in incomplete (onleesbare) DXF-bestanden. In de schermafdruk kunt u links de originele weergave in QGIS zien en rechts de rendering van het geëxporteerde DXF-bestand in Autodesk TrueView.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Dit werd mogelijk gemaakt door:** Gemeenschappen van Morges, Uster, Vevey en SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Mogelijkheid: Expressie-filters aan de kant van de provider voor PostGIS
In QGIS 2.10 kunt u nu objecten filteren aan de kant van de databaseserver. Alleen ondersteunde expressies zullen naar de database worden gezonden. Expressies die niet ondersteunde operatoren of functies gebruiken zullen ongemerkt terugvallen naar lokale evaluatie.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

of

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Gegevensbeheer
### Mogelijkheid: Virtuele velden kunnen nu bijgewerkt worden
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Mogelijkheid: Automatisch aanvullen in Wijzig hulpmiddel voor widget Waarde relatie bewerken
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

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
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagrammen
### Mogelijkheid: Verbeteringen aan Diagrammen
De functionaliteit Diagram in QGIS maakt het u mogelijk om kleine taartdiagrammen of histogrammen over objecten op de kaart te leggen. In deze uitgave hebben we have de volgende verbeteringen voor ondersteuning van diagrammen gemaakt:
- Diagrammen kunnen worden uitgeschakeld zonder verlies van instellingen
- Keuzevak om diagrammen altijd weer te geven voor een laag toegevoegd 
- De gebruikersinterface voor diagrammen is vernieuwd om het dialoogvenster te vereenvoudigen en het meer gebruikersvriendelijk te maken
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Digitaliseren
### Mogelijkheid: Verbeterd gereedschao voor draiien van geometrie
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- u kunt nu numerieke invoer in het gereedschap om te draaien gebruiken
- u kunt een combinatievak gebruiken om de hoeken in te stellen
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Labelen
### Feature: \"Follow point\" alignment for multiline labels
Indien ingesteld op deze modus, is de uitlijning van de tekst van labels afhankelijk van de uiteindelijke plaatsing van het label, relatief ten opzichte van het punt. Bijv, als het label links va het punt wordt geplaatst zal het label rechts worden uitgelijnd, en als het rechts van het punt wordt geplaatst dan zal het label links worden uitgelijnd. Dit verbetert de weergave van labels met meerdere regels voor puntlagen enorm.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Printvormgeving
### Mogelijkheid: Modus voor schalen van schaalbalk toegevoegd om een gewenste breedte van de schaalbalk passend te maken
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programmeerbaarheid
### Mogelijkheid: Verbeteringen voor programmeurs
We hebben een aantal wijzigingen en verbeteringen gemaakt die interessant zullen zijn voor ontwikkelaars:
- We hebben de minimale vereiste voor Qt4 verhoogd naar versie 4.8. Qt4 is een van de belangrijkste C++ gereedschappen / bibliotheken die we gebruiken om QGIS te maken.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Wijzigen van de gegevensbron voor een vectorlaag mogelijk gemaakt.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Server
### Mogelijkheid: Ondersteuning voor tolerantie-parameter in WMS GetFeatureInfo verzoeken
Bij het gebruiken van WMS-lagen, geleverd door QGIS Server, kunt u nu de tolerantie specificeren voor hoe ver van de klik-origine verzoeken GetFeatureInfo in aanmerking zouden moeten komen. Dit is belangrijk voor mobiele apparaten waar het moeilijker is om de objecten precies aan te duiden. Vóór deze nieuwe mogelijkheid was het nagenoeg onmogelijk om punt- of lijnobjecten te identificeren op een mobiel apparaat met QGISserver. U kunt de volgende parameters toevoegen aan uw verzoeken GetFeatureInfo:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

en wijzig de waarden voor tolerantie (in pixels) om aan uw behoeften te voldoen.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Symbologie
### Mogelijkheid: Categorieën moeten overeenkomen met bestaande stijlen
Opties onder menu Categorieën van de renderer toegevoegd om categorieën in te stellen op symbolen met een overeenkomende naam uit de stijlbibliotheek of een XML-stijlbestand.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Mogelijkheid: Variëren van symboolgrootten met behulp van de renderer Gradueel
Renderers zijn het subsysteem van QGIS dat u in staat stelt rijke cartografische weergaven van uw gegevens te maken. Een renderer Gradueel varieert de symbologie, gebaseerd op een doorlopend wijzigende waarde in een vectorlaag. In eerdere versies van QGIS kon u alleen de kleur laten variëren (bijv. door een kleur van een kleurenbalk te gebruiken). In QGIS 2.10 stelt de symboolrenderer Gradueel u nu in staat om de grootte *of* de kleur te variëren. Voor puntlagen kunt u de grootte van de punt variëren, voor lijnen kunt u de breedte van de lijn variëren. Polygoonlagen behouden slechts de mogelijkheid om te variëren op kleur, lijndikte wordt nog niet ondersteund.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Mogelijkheid: Nieuwe optie voor het voorkomen van het automatisch afsnijden van objecten naar het kaartbereik
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Mogelijkheid: Schalen van grootte en draaien zijn verwijderd uit het menu Geavanceerd
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Mogelijkheid: Datagedefinieerde eigenschappen voor markering lettertype
De meeste eigenschappen van de markering voor lettertype kunnen nu datagedefinieerd zijn, inclusief grootte, rotatie en teken van de markering.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Mogelijkheid: Visualiseren en aanpassen van de renderer Gradueel met behulp van een histogram
Een nieuwe tab Histogram is toegevoegd aan de renderer Graduaeel, die een interactief histogram van de waarden uit het toegewezen veld of expressie weergeeft. Klasse-afbrekingen kunnen met behulp van het histogram worden verplaatst of toegevoegd.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Mogelijkheid: Expressies voor grootte, rotatie en lijndikte op niveau van de symboollijst
Grootte en Rotatie kunnen door middle van een expressie worden gedefinieerd voor alle symboolniveaus die een markering samenstellen. Dikte kan worden gedefinieerd door een expressie voor alle symbolen die ene lijn samenstellen.

Voor symbolen wordt een legenda gegenereerd voor variërende grootten. Dit maakt een multivariate analyse van de legenda in het geval van geclassificeerde/graduele kleuren mogelijk.

Een assistent, met voorbeeld, is toegankelijk via de knop Datagedefinieerd om de gebruiker te helpen de expressie voor de grootte te definiëren. Drie methoden zijn beschikbaar: Flannery, Area en Radius.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Mogelijkheid: Live laageffecten voor lagen en symboollagen
Live lageneffecten zijn toegevoegd aan de reeds ruime cartografische mogelijkheden van QGIS door het toevoegen van de mogelijkheid om verscheidene effecten voor renderen toe te voegen aan de keten van renderen. Met live-effecten kunt u dingen doen als het plaatsen van valschaduwen onder uw symbool, schuin trekken en vervormen van het gerenderde symbool. U kunt deze effecten ook in lagen op elkaar leggen en instellen of het effect progressief zou moeten zijn (d.i. zichzelf toepassen op de gerenderde status tot nu toe) of discreet (door het opnieuw injecteren van de bron-geometrie terug in de keten van renderen).

**Opmerking**: Deze mogelijkheid is voor gevorderde gebruikers en we moeten opmerken dat het overmatig gebruiken van deze mogelijkheid de benodigde tijd voor renderen significant kan verlagen, overweeg dus om verschillende profielen voor symbologie voor uw laag te gebruiken - één voor het genereren van kaarten in productiekwaliteit en één voor de ontwerpmodus.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
