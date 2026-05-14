---
draft: 'true'

---
# Console van Python gebruiken om offline kaart van WMS voor te bereiden (tegel downloader)
Dit praktijkvoorbeeld legt uit hoe offline kaarten vanuit WMS/WFS of een in het kaartvenster van QGIS geladen kaart voor te bereidden door tegels te downloaden met behulp van een script in de console van Python. Het script genereert ook een mozaïek uit de tegels voor verder gebruik.

Toegang tot raster-/vectorkaarten door middle van Web Mapping Service (WMS)-services is zeer algemeen en efficiënt. Het heeft verscheidene voordelen, zoals veiligheid, gecentraliseerde en flexibele kaartstijlen. Voorbeelden zijn Google maps, Yahoo, Bing, MODIS, Landsat, kaarten gepubliceerd door NASA, NRSC (India). Het nadeel/beperking van WMS is dat het werkt via internet of intranet. Het is misschien niet mogelijk om altijd een internetverbinding te krijgen, in het bijzonder tijdens veldonderzoek. Ook werkt WMS traag, vergeleken met andere offline indelingen voor afbeeldingen, zoals GeoTiff, jpg, img etc.
## Gebruik van QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Python-Console
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. X-,Y-coördinaten (linksboven en rechtsonder) van eerste tegel
2. Grootte van de te downloaden tegel (bijv. 0.001 X 0.001 graden)
3. Aantal te downloaden tegels (berekening gebaseerd op volledig bereik van de kaart en grootte van de tegels)
4. Map voor uitvoer om de uitvoerbestanden/-tegels op te slaan

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

De methode heeft de beperking dat wijzigingen in de kaart aan de kant van de server niet zichtbaar zullen zijn offline (gedownloade kaart). In dat geval zal de gebruiker het proces moeten herhalen en een nieuwe offline kaart moeten genereren. De tweede beperking is dat de offline gemaakte kaart in de indeling van een afbeelding is; hij kan niet worden gebruikt als thematische kaart of classificatie van de afbeelding. met enige extra inspanningen kunnen kaarten over grondgebruik worden geconverteerd naar vector met enig gegevensverlies.
## Bereik
De gegenereerde mozaïek is een pure afbeelding zelfs als hij wordt gedownload uit een thematische kaart (7-8 kleuren). Met behulp van geavanceerd gereedschap zoals opnieuw classificeren, laag/band stapelen kan dit raster worden geconverteerd naar polygoon vector. WMS heeft verschillende verzoeken zoals getCapabilities, getMap, getFeatureinfo etc. Met behulp van getFeatureInfo kan de informatie over attributen voor elke polygoon worden opgehaald. Het script kan worden geconverteerd naar plug-in zodat iedereen zonder kennis van scripten in staat zal zijn het script te gebruiken.
## Conclusie
Bovenstaande ervaringen laten zien dat QGIS kan worden gebruikt op elk gevorderd niveau. Met basale vaardigheden op het gebied van programmeren kan iedereen een klein script schrijven of een plug-in om de kwaliteit van het werk te verbeteren en tijd te besparen. In QGIS is de toegang tot een opslagplaats van wereldwijd ontwikkelde plug-ins het beste van QGIS. Het PyQGIS Developer Cookbook is een goede bron om een script te schrijven en het verwerken van rastergegevens is nu veel eenvoudiger met behulp van GDAL Tools.
## Auteurs
Dit artikel werd bijgedragen in mei 2014 door Prashant Kadgi, gevestigd in Pune (India) en momenteel werkzaam als consultant in GIS APP Consultancy Services. Sinds 2009 gebruikt hij GIS & RS in NRM, bosbouw, e-governance, projecten voor ontwikkeling van software in verschillende regio's van India en de wereld.
- Contact: <kadgiprashant@gmail.com>
- Website www.gisappco.com (under construction)
