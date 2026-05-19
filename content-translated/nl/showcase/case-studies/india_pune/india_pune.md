---
draft: 'true'

---
# Console van Python gebruiken om offline kaart van WMS voor te bereiden (tegel downloader)
Dit praktijkvoorbeeld legt uit hoe offline kaarten vanuit WMS/WFS of een in het kaartvenster van QGIS geladen kaart voor te bereiden door tegels te downloaden met behulp van een script in de console van Python. Het script genereert ook een mozaïek uit de tegels voor verder gebruik.

Toegang tot raster-/vectorkaarten door middle van Web Mapping Service (WMS)-services is zeer algemeen en efficiënt. Het heeft verscheidene voordelen, zoals veiligheid, gecentraliseerde en flexibele kaartstijlen. Voorbeelden zijn Google maps, Yahoo, Bing, MODIS, Landsat, kaarten gepubliceerd door NASA, NRSC (India). Het nadeel/beperking van WMS is dat het werkt via internet of intranet. Het is misschien niet mogelijk om altijd een internetverbinding te krijgen, in het bijzonder tijdens veldonderzoek. Ook werkt WMS traag, vergeleken met andere offline indelingen voor afbeeldingen, zoals GeoTiff, jpg, img etc.
## Gebruik van QGIS
QGIS verschaft een gereedschap om verbinding te maken met/toegang te krijgen tot elke WMS-service. De verbinding met WMS is gebaseerd op een eenvoudige URL en als de verbinding eenmaal is gemaakt, is de kaart te zien in het kaartvenster van QGIS. Als we de kaart van het zichtbare bereik vanuit het kaartvenster van QGIS willen opslaan als jpg (Bestand > Als afbeelding opslaan) maakt het een wereldbestand dat de informatie over de geografische coördinaten van een bepaalde regio bevat. Bijv. sample.jpg is de kaart en sample.jpgw bevat de coördinaten. Dat betekent dat de gedownloade afbeelding is voorzien van geoverwijzingen. We kunnen handmatig tegels in rasterindeling downloaden en later offline gebruiken. Handmatig downloaden is mogelijk als het gebied heel klein is of als afbeeldingen met een lage resolutie voldoende zijn.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Python-Console
Een kort script werd geschreven in de "Python Console" met beschikbare hulp van QGIS officiële website in het PyQGIS Developer Cookbook. Het script bestaat in de basis uit 4 componenten, en wel als volgt,
1. X-,Y-coördinaten (linksboven en rechtsonder) van eerste tegel
2. Grootte van de te downloaden tegel (bijv. 0.001 X 0.001 graden)
3. Aantal te downloaden tegels (berekening gebaseerd op volledig bereik van de kaart en grootte van de tegels)
4. Map voor uitvoer om de uitvoerbestanden/-tegels op te slaan

Het script werkt met twee eenvoudige FOR-loops die eerst het bereik van de kaart in het kaartvenster van QGIS definiëren en over de rijen/kolommen worden uitgevoerd. Als het kaartbereik is ingesteld, wordt de kaart geladen in QGIS. De vertraging van 3 seconden (afhankelijk van de internetverbinding) werd geïntroduceerd voor het opslaan van de kaart als jpg in de door de gebruiker gedefinieerde map. Als het script wordt uitgevoerd, kunnen alle in de map gemaakte tegels direct worden geladen in QGIS of wordt een enkel mozaïek voorbereid via Raster \> Diversen \> Samenvoegen of Virtueel raster bouwen (Catalogus). Beide gereedschappen genereren mozaïeken, maar het basisverschil is dat Samenvoegen een afbeelding maakt die onafhankelijk is van de tegels, terwijl Virtueel raster een koppeling genereert in alle individuele tegels (tegels zijn vereist).

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
