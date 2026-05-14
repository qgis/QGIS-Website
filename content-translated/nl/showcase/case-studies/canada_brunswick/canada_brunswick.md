---
draft: 'true'

---
# Fundy Footpath Trail-kaart maken met QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Het pad werd gemaakt, wordt onderhouden, en gepromoot door een groep vrijwilligers die bekend staan als de Fundy Hiking Trail Association Inc. (FHTA)(1975). Als een non-profit organisatie werft de FHTA fondsen voor zijn activiteiten door de verkoop van gidsen die een kaart van het pad bevat. In 2011 benaderde ik de FHTA om vrijwillig de officiële kaart voor het pad bij te werken. Als een vrijwilliger die een kaart maakt voor een non-profit organisatie voldoet QGIS zowel als gereedschap voor het bewerken van gegevens en voor de uiteindelijk lay-out van de kaart. Door de inspanningen van mijzelf en leden van de FHTA wordt de nieuwe officiële kaart voor het Fundy Footpath, opgenomen in de gids, van begin tot einde gemaakt met QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## Het project
Het proces voor het maken van de nieuwe kaart voor het Fundy Footpath met QGIS kan worden opgedeeld in drie verschillende delen:
- Verzamelen van gegevens.
- Bewerken en voorbereiden van de gegevens.
- Maken van de kaart

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

De volgende gereedschappen binnen QGIS werden gebruikt om specifieke taken te volbrengen bij het voorbereiden van de gegevens om te gebruiken in de uiteindelijke kaart:
- De met GPS verzamelde gegevens werden opgeschoond met behulp van de werkbalk Bewerken.
- De van NRCan en SNB verkregen vectorgegevens werden samengevoegd, bevraagd, en geclipt voor het uiteindelijk gebied van de kaart met behulp van de gereedschappen voor vectoren.
- Een komma-gescheiden bestand, verkregen van SNB, werd geïmporteerd in QGIS als een puntlaag met behulp van de plug-in Add Delimited Text Layer, de plug-in Interpolation werd gebruikt om een hoogteraster te maken dat daarna werd gebruikt om een raster met schaduw voor de heuvels en hoogte-contourenlaag te maken met de plug-in GDAL rastergereedschappen.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusie
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Links
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Auteur
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Dit artikel werd bijgedragen door Jarrett Totton in januari 2013. Jarrett is een GIS Technologist, woonachtig in Alberta, Canada.
