---
HasBanner: false
draft: false
releaseDate: 21-10-2021
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.18
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.18{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Datum uitgave 21-10-2016

Dit is de laatste uitgave in de reeks 2.x. De huidige Long Term Release (LTR) blijft versie 2.14.x. Deze uitgave bevat aanvullende verbeteringen bovenop onze eerdere uitgave. De meeste activiteiten zijn momenteel gericht op de ontwikkeling van QGIS 3.0, wat onze volgende generatie uitgaven is, die staat gepland voor het einde van het eerste kwartaal van 2017.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en sponsors. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors). Als u een officiële sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 2.18.0
Elk jaar ontvangen wij ook ondersteuning van verschillende organisaties die het werk wat wij doen waarderen en die het mogelijk willen maken dat de ontwikkeling van het QGIS project vooral blijft doorgaan. Deze sponsoren, genoemd in onderstaande lijst, zijn wij zeer dankbaar! 

{{<fund type="changelog" relativeImgPath=true >}}
## Algemeen
### Mogelijkheid: Automatische links in Identificatieresultaten
Elke link `http` of `mailto` in waarden van attributen zal nu automatisch worden geconverteerd naar aan te klikken koppelingen binnen het paneel Identificatieresultaten.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Mogelijkheid: Muiswiel boven schuifbalken dialoogvensters Kleuren
In QGIS 2.18 kunt u nu met het muiswiel scrollen over elke schuifbalk in het dialoogvenster Kleur kiezen om de waarde in kleine stapjes te verhogen. Dit is een handige sneltoets voor kleine aanpassingen aan kleurcomponenten.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

Dit werd mogelijk gemaakt door [Nyall Dawson (North Road)](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Aangepaste kleurenschema's toevoegen aan het menu voor de keuzelijst met kleuren
QGIS 2.18 voegt de mogelijkheid toe voor gebruikers om in te stellen of een door de gebruiker gemaakt kleurenschema zou moeten voorkomen in de knoppen van de keuzelijsten van de kleurenmenu's. Deze instelling wordt beheerd door het dialoogvenster Kleur kiezen, op de tab Lijsten. Voeg eenvoudigweg een nieuw schema toe, selecteer daarna in het menu Schema de nieuwe optie \"show in buttons\". Dit is een handige sneltoets als u sets van veelvoorkomende paletten heeft en ze direct beschikbaar wilt hebben via het menu Kleuren.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Mogelijkheid: Kleuren kiezen is nu ingebed in het paneel Laagstijlen
In QGIS 2.18 zorgt het klikken op een knop in het paneel Stijl van de laag er voor dat het dialoogvenster Kleur kiezen  wordt geopend binnen het paneel Stijl zelf in plaats van als een zelfstandig dialoogvenster. Dit maakt het mogelijk de kleuren interactief aan te passen met een direct voorbeeld van het resultaat.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Labelen
### Mogelijkheid: Ondersteuning voor labelen met lijst voor vervanging
Voegt de mogelijkheid toe om een lijst te specificeren met vervangende teksten om toe te passen op de tekst van het label. Bijv. afkortingen van typen straat.

Gebruikers kunnen lijsten met vervangingen ex- en importeren om hergebruik en delen eenvoudiger te maken.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterd algoritme voor plaatsen van lijnlabels
De modus parallel labelen voor lijnlagen is enorm verbeterd, met een nieuw algoritme dat het plaatsen van labels op puntige delen van geometrieën van objecten voorkomt.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Polygonen labelen met behulp van gebogen labels langs de omtrek
Dit voegt een nieuwe modus voor het labelen van polygonen toe waar de omtrek van de polygoon wordt gelabeld met behulp van gebogen labels.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Renderen
### Mogelijkheid: Voorbeeld van rastertegels (WMTS- en XYZ-lagen)
In eerdere versies van QGIS moesten gebruikers wachten tot het downloaden van alle tegels voor een laag was voltooid om de resulterende kaart te kunnen bekijken. Dit is nu verholpen en de tegels worden onmiddellijk in het kaartvenster weergegeven als zij worden gedownload, wat de ervaring van de gebruiker enorm verbeterd door het verlagen van de tijdsduur waarmee iets wordt weergegeven. Beter nog, eerder gedownloade tegels met lagere of hogere resoluties kunnen worden gebruikt voor de functionaliteit van het voorbeeld in de gebieden waar de tegels met de juiste resolutie nog niet zijn gedownload.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

Dit werd mogelijk gemaakt door [Land Information New Zealand](http://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Mogelijkheid: Te annuleren renderen van rasters (WMS-, WMTS-, WCS- en XYZ-lagen)
Deze verbetering verhoogt de gebruikerservaring bij het werken met rasterlagen die afkomstig zijn van servers op afstand. Eerder moest men wachten tot de downloads volledig waren voltooid om opnieuw of de kaart in te kunnen zoomen of die te verplaatsen, omdat de gebruikersinterface tussentijds zou zijn bevroren. Dit is nu verholpen dor het feit dat het renderen van rasterlagen op elk moment kan worden geannuleerd.

Dit werd mogelijk gemaakt door [Land Information New Zealand](http://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Gegevensbeheer
### Mogelijkheid: Vlag toevoegen om alleen geselecteerde objecten te kopiëren
De Plug-in Offline bewerken is een standaard plug-in die in QGIS is ingebouwd en u in staat stelt om offline een gegevensset op afstand (bijv. uit een database), in het veld te bewerken en dan die, terug in uw kantoor, opnieuw te synchroniseren. Dit vergroot de mogelijkheden voor het offline bewerken door alleen te werken met een subset van grote lagen.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door DB Fahrwegdienste GmbH

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Formulieren en widgets
### Mogelijkheid: Beheren van labels voor individuele widgets Bewerken toestaan
Beheren van labels voor individuele widgets Bewerken in een formulier toestaan. In de ontwerper Slepen en neerzetten zal een dubbelklik op een item het mogelijk maken om te beheren of het label voor elk individueel item zou moeten worden weergegeven.

In aanvulling daarop is het mogelijk te configureren of de knoppen koppelen/ontkoppelen worden weergegeven in widget Relatie-verwijzing, wat nuttig is om relaties 1:n te verbergen waar een kind niet kan bestaan zonder zijn ouders.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid: Conditionele zichtbaarheid voor tabs en groepsvakken
Dit voegt een nieuwe optie voor configureren toe om tabs en groepsvakken onder voorwaarden weer te geven of te verbergen in formulieren van de ontwerper Slepen en neerzetten.

Configureren wordt gedaan door dubbel te klikken in de boom van de ontwerper in de interface voor het configureren van de velden.

Een expressie kan worden ingevoerd om de zichtbaarheid te beheren. De expressie zal opnieuw worden geëvalueerd elke keer als waarden in het formulier worden gewijzigd en zal de tab of groepsvak overeenkomstig worden weergegeven/verborgen.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid:  Standaard veldwaarden aan kant van de cliënt
Maakt het mogelijk een expressie in te stellen voor een veld van een vectorlaag dat wordt gebruikt om de standaardwaarde van dat veld te evalueren. Expressies voor standaardwaarden kunnen eigenschappen gebruiken van het object dat bestaat op het moment van aanroepen, zoals gedigitaliseerde geometrieën. Variabelen voor de expressie kunnen ook worden gebruikt in expressies voor standaardwaarden, wat het eenvoudig maakt om bijv. de naam van een gebruiker in te voeren, de huidige datum en tijd, het pad van het project, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door DB Fahrwegdienste GmbH

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Printvormgeving
### Mogelijkheid: Pijlen voor Ware noorden
QGIS 2.18 voegt ondersteuning toe voor oriënteren van noordpijlen naar het ware noorden in de Printvormgeving. Eerder werden alle pijlen uitgelijnd aan het noorden van het raster, wat niet geschikt is voor regio's van de polen of niet-Noorden boven-projecties (zoals enkele Zuid-Afrikaanse projectiesystemen). Nu kunt u ervoor kiezen om de pijlen te oriënteren, ofwel vergeleken met het noorden van het raster of het ware noorden. Er is ook een optionele hoek voor verschuiving, die kan worden gebruikt om een convergentie voor het raster te verzorgen, zodat uw pijlen zich oriënteren op het magnetisch noorden!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door `Norwegian Polar Institute's Quantarctica project <http://quantarctica.npolar.no>`__

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Processing
### Mogelijkheid: Algoritme Punt op oppervlak
Dit nieuwe algoritme is soortgelijk aan het algoritme centroids, maar waar een zwaartepunt buiten het corresponderende object kan liggen, garandeert het algoritme \'Punt op oppervlak\' een punt te maken dat ligt binnen de corresponderende objectpolygoon (of het corresponderende object lijn voor lijnlagen raakt).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Processing algoritme Dissolve accepteert meerdere velden
Het  algoritme Dissolve staat u nu toe om te ontbinden op meer dan één veldwaarde. In eerdere versies van QGIS kan het ontbinden alleen objecten groeperen op één enkele veldwaarde.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Geoptimaliseerd algoritme Clip voor Processing
Het algoritme Clip voor Processing is geoptimaliseerd voor veel voorkomende en in gebruik zijnde scenario's, wat resulteert in dramatische toename van snelheid voor bewerkingen van clippen. Bijvoorbeeld:

**Clippen van een laag met wegen met 1 miljoen lijnen tegen 2 polygonen**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconden

**Clippen van een 5 miljoen puntenlaag met adressen tegen 2 polygonen**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconden

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritme voor begrenzingsvakken
Dit nieuwe algoritme berekent het begrenzingsvak (enveloppe) van elk object in de invoerlaag.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogeljkheid: Algoritme Samenvoegen verbonden lijnen
Dit algoritme voegt alle verbonden delen van geometrieën MultiLineString samen tot één enkele geometrie LineString. Als enig deel van de ingevoerde geometrieën MultiLineString niet is verbonden, zal de resulterende geometrie een MultiLineString zijn die lijnen bevat die konden worden samengevoegd en alle niet verbonden delen van lijnen.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritme Rand van geometry
Dit nieuwe algoritme geeft de sluiting weer van de gecombineerde randen van de geometrieën  van de invoer (d.i. de topologische grens van de geometrie). Bijvoorbeeld: een geometrie polygoon zal een rand hebben die bestaat uit de linestrings voor elke ring in de polygoon, en een geometrie lijn zal een rand hebben die bestaat uit de begin- en eindpunten van de lijn. Dit algoritme is alleen geldig voor polygoon- of lijnlagen.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Gegevensproviders
### Mogelijkheid: Eigen ondersteuning voor XYZ-lagen
Rastertegels in de indeling XYZ worden nu vanzelf ondersteund binnen WMS-gegevensproviders, wat gebruikers in staat stelt basiskaarten weer te geven uit andere bronnen zonder nog langer de noodzaak van plug-ins van derde partijen. zoals QuickMapServices of OpenLayer.

Open eenvoudigweg een browser dockwidget om verbindingen naar XYZ-lagen toe te voegen,, zoek naar een item, genaamd \"Tile Server (XYZ)\" en klik er met rechts op om een pop-upmenu te verkrijgen met de actie \"Nieuwe verbinding\". U zult worden gevraagd naar de URL, waarin `{x}`, `{y}`, `{z}` moeten worden vervangen door de feitelijke tegelnummers, overeenkomstig de huidige kaartweergave. Bijvoorbeeld: om de OpenStreetMap-basiskaart toe te voegen, kan men deze URL gebruiken: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

De gegevensprovider ondersteunt ook het coderen van XYZ-tegelnummers naar \"quadkeys\" die worden gebruikt door Bing. Gebruik eenvoudigweg `{q}` in plaats van `{x}`, `{y}` en `{z}` in de URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

Dit werd mogelijk gemaakt door [Lutra Consulting](http://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Server
### Mogelijkheid: De mogelijkheid voor informatie over segmenten van het object geometrie in server
Noodzakelijk voor geometrieën die bogen (CircularArc, CompoundCurve, CurvePolygon) bevatten, maar de webclient (bijv. QGIS Web Client) kan het weergeven van deze typen geometrie niet afhandelen.

Deze mogelijkheid kan worden ingeschakeld op de tab \"OWS server\" in het dialoogvenster \"Projecteigenschappen\".

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Plug-ins
### Mogelijkheid: DB Manager: Mogelijkheid toegevoegd voor bijwerken van SQL-laag
Met deze mogelijkheid kan de gebruiker de gegevensbron van de laag bijwerken als dat is gebaseerd op een verzoek van SQL.

Dit werd mogelijk gemaakt door [Ifremer](http://wwz.ifremer.fr)

Deze mogelijkheid werd ontwikkeld door [3Liz](http://3liz.com)
## Programmeerbaarheid
### Mogelijkheid: Functie GEOS lineaire verwijzing weergeven voor QgsGeometry
Een nieuwe functie `QgsGeometry::lineLocatePoint()` is toegevoegd voor het ophalen van de afstand langs een linestring naar de dichtstbijzijnde positie op de linestring tot een opgegeven punt.

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Mogelijkheid: Nieuwe klassen voor PyQGIS in 2.18
### Nieuwe bronklassen
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - een interface voor annotatie-items die op een kaart zijn getekend
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - een basisklasse voor objecten voor terugkoppeling om te worden gebruikt om iets te annuleren dat wordt uitgevoerd in een worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - een expressie met een aanvullende ingeschakelde vlag

### Nieuwe klassen voor GUI, opnieuw te gebruiken widgets
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - bevat een bewerkingsveld voor het invoeren van expressies samen met een knop om het dialoogvenster voor het maken van een expressie te openen. Dit widget is ontworpen om te gebruiken in contexten waar geen laagvelden beschikbaar zijn om te gebruiken in een expressie en de ruimte beperkt is.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - soortgelijk aan QTabWidget maar met aanvullende methoden om tijdelijk tabs weer te geven/te verbergen

## Mogelijkheid: Nieuwe functies voor expressies
QGIS 2.18 voegt verscheidene nieuwe functies voor expressies toe, inclusief functies voor interpolatie van hoeken/afstanden.
- `line_merge`: voegt een geometrie MultiLineString samen met verbonden LineStrings
- `boundary`: geeft een topologische rand van een geometrie terug, d.i. voor polygonen is dit een MultiLineString die de ringen van de polygoon weergeeft
- `angle_at_vertex`: geeft de gemiddelde (bisector) hoek terug voor een geometrie tot een gespecificeerde index van punten
- `distance_to_vertex`: geeft de afstand terug langs de geometrie tot een gespecificeerde index van punten.
- `line_interpolate_angle`: berekent de hoek parallel aan de geometrie op een gespecificeerde afstand langs een geometrie
- `line_interpolate_point`: geeft een punt op een lijn op  afstand terug 
- `line_locate_point`: geeft de afstand terug langs de lijn naar de dichtstbijzijnde locatie van de lijn die het dichtstbij ligt bij het gespecificeerde punt

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
