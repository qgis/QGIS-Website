---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
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

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 2.18.0
Elk jaar ontvangen wij ook ondersteuning van verschillende organisaties die het werk wat wij doen waarderen en die het mogelijk willen maken dat de ontwikkeling van het QGIS project vooral blijft doorgaan. Deze sponsoren, genoemd in onderstaande lijst, zijn wij zeer dankbaar! 

{{<fund type="changelog" relativeImgPath=true >}}
## Algemeen
### Mogelijkheid: Automatische links in Identificatieresultaten
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Mogelijkheid: Muiswiel boven schuifbalken dialoogvensters Kleuren
In QGIS 2.18 kunt u nu met het muiswiel scrollen over elke schuifbalk in het dialoogvenster Kleur kiezen om de waarde in kleine stapjes te verhogen. Dit is een handige sneltoets voor kleine aanpassingen aan kleurcomponenten.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Aangepaste kleurenschema's toevoegen aan het menu voor de keuzelijst met kleuren
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Mogelijkheid: Kleuren kiezen is nu ingebed in het paneel Laagstijlen
In QGIS 2.18 zorgt het klikken op een knop in het paneel Stijl van de laag er voor dat het dialoogvenster Kleur kiezen  wordt geopend binnen het paneel Stijl zelf in plaats van als een zelfstandig dialoogvenster. Dit maakt het mogelijk de kleuren interactief aan te passen met een direct voorbeeld van het resultaat.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Labelen
### Mogelijkheid: Ondersteuning voor labelen met lijst voor vervanging
Voegt de mogelijkheid toe om een lijst te specificeren met vervangende teksten om toe te passen op de tekst van het label. Bijv. afkortingen van typen straat.

Gebruikers kunnen lijsten met vervangingen ex- en importeren om hergebruik en delen eenvoudiger te maken.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterd algoritme voor plaatsen van lijnlabels
De modus parallel labelen voor lijnlagen is enorm verbeterd, met een nieuw algoritme dat het plaatsen van labels op puntige delen van geometrieën van objecten voorkomt.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Polygonen labelen met behulp van gebogen labels langs de omtrek
Dit voegt een nieuwe modus voor het labelen van polygonen toe waar de omtrek van de polygoon wordt gelabeld met behulp van gebogen labels.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Renderen
### Mogelijkheid: Voorbeeld van rastertegels (WMTS- en XYZ-lagen)
In eerdere versies van QGIS moesten gebruikers wachten tot het downloaden van alle tegels voor een laag was voltooid om de resulterende kaart te kunnen bekijken. Dit is nu verholpen en de tegels worden onmiddellijk in het kaartvenster weergegeven als zij worden gedownload, wat de ervaring van de gebruiker enorm verbeterd door het verlagen van de tijdsduur waarmee iets wordt weergegeven. Beter nog, eerder gedownloade tegels met lagere of hogere resoluties kunnen worden gebruikt voor de functionaliteit van het voorbeeld in de gebieden waar de tegels met de juiste resolutie nog niet zijn gedownload.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Mogelijkheid: Te annuleren renderen van rasters (WMS-, WMTS-, WCS- en XYZ-lagen)
Deze verbetering verhoogt de gebruikerservaring bij het werken met rasterlagen die afkomstig zijn van servers op afstand. Eerder moest men wachten tot de downloads volledig waren voltooid om opnieuw of de kaart in te kunnen zoomen of die te verplaatsen, omdat de gebruikersinterface tussentijds zou zijn bevroren. Dit is nu verholpen dor het feit dat het renderen van rasterlagen op elk moment kan worden geannuleerd.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Gegevensbeheer
### Mogelijkheid: Vlag toevoegen om alleen geselecteerde objecten te kopiëren
De Plug-in Offline bewerken is een standaard plug-in die in QGIS is ingebouwd en u in staat stelt om offline een gegevensset op afstand (bijv. uit een database), in het veld te bewerken en dan die, terug in uw kantoor, opnieuw te synchroniseren. Dit vergroot de mogelijkheden voor het offline bewerken door alleen te werken met een subset van grote lagen.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Formulieren en widgets
### Mogelijkheid: Beheren van labels voor individuele widgets Bewerken toestaan
Beheren van labels voor individuele widgets Bewerken in een formulier toestaan. In de ontwerper Slepen en neerzetten zal een dubbelklik op een item het mogelijk maken om te beheren of het label voor elk individueel item zou moeten worden weergegeven.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid: Conditionele zichtbaarheid voor tabs en groepsvakken
Dit voegt een nieuwe optie voor configureren toe om tabs en groepsvakken onder voorwaarden weer te geven of te verbergen in formulieren van de ontwerper Slepen en neerzetten.

Configureren wordt gedaan door dubbel te klikken in de boom van de ontwerper in de interface voor het configureren van de velden.

Een expressie kan worden ingevoerd om de zichtbaarheid te beheren. De expressie zal opnieuw worden geëvalueerd elke keer als waarden in het formulier worden gewijzigd en zal de tab of groepsvak overeenkomstig worden weergegeven/verborgen.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid:  Standaard veldwaarden aan kant van de cliënt
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Printvormgeving
### Mogelijkheid: Pijlen voor Ware noorden
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Processing
### Mogelijkheid: Algoritme Punt op oppervlak
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Processing algoritme Dissolve accepteert meerdere velden
Het  algoritme Dissolve staat u nu toe om te ontbinden op meer dan één veldwaarde. In eerdere versies van QGIS kan het ontbinden alleen objecten groeperen op één enkele veldwaarde.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Geoptimaliseerd algoritme Clip voor Processing
Het algoritme Clip voor Processing is geoptimaliseerd voor veel voorkomende en in gebruik zijnde scenario's, wat resulteert in dramatische toename van snelheid voor bewerkingen van clippen. Bijvoorbeeld:

**Clippen van een laag met wegen met 1 miljoen lijnen tegen 2 polygonen**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**Clippen van een 5 miljoen puntenlaag met adressen tegen 2 polygonen**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritme voor begrenzingsvakken
Dit nieuwe algoritme berekent het begrenzingsvak (enveloppe) van elk object in de invoerlaag.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogeljkheid: Algoritme Samenvoegen verbonden lijnen
Dit algoritme voegt alle verbonden delen van geometrieën MultiLineString samen tot één enkele geometrie LineString. Als enig deel van de ingevoerde geometrieën MultiLineString niet is verbonden, zal de resulterende geometrie een MultiLineString zijn die lijnen bevat die konden worden samengevoegd en alle niet verbonden delen van lijnen.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritme Rand van geometry
Dit nieuwe algoritme geeft de sluiting weer van de gecombineerde randen van de geometrieën  van de invoer (d.i. de topologische grens van de geometrie). Bijvoorbeeld: een geometrie polygoon zal een rand hebben die bestaat uit de linestrings voor elke ring in de polygoon, en een geometrie lijn zal een rand hebben die bestaat uit de begin- en eindpunten van de lijn. Dit algoritme is alleen geldig voor polygoon- of lijnlagen.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Gegevensproviders
### Mogelijkheid: Eigen ondersteuning voor XYZ-lagen
Rastertegels in de indeling XYZ worden nu vanzelf ondersteund binnen WMS-gegevensproviders, wat gebruikers in staat stelt basiskaarten weer te geven uit andere bronnen zonder nog langer de noodzaak van plug-ins van derde partijen. zoals QuickMapServices of OpenLayer.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Server
### Mogelijkheid: De mogelijkheid voor informatie over segmenten van het object geometrie in server
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Plug-ins
### Mogelijkheid: DB Manager: Mogelijkheid toegevoegd voor bijwerken van SQL-laag
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programmeerbaarheid
### Mogelijkheid: Functie GEOS lineaire verwijzing weergeven voor QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Mogelijkheid: Nieuwe klassen voor PyQGIS in 2.18
### Nieuwe bronklassen
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Nieuwe klassen voor GUI, opnieuw te gebruiken widgets
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Mogelijkheid: Nieuwe functies voor expressies
QGIS 2.18 voegt verscheidene nieuwe functies voor expressies toe, inclusief functies voor interpolatie van hoeken/afstanden.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Dit werd mogelijk gemaakt door Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
