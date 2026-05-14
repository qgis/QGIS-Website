---
draft: 'true'

---
# Creazione della mappa del sentiero Fundy Trail con QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Il sentiero è stato creato, mantenuto e sponsorizzato da un gruppo di volontari conosciuti come Fundy Hiking Trail Association Inc. (FHTA) (1975). Come organizzazione non-profit, il FHTA raccoglie fondi per le proprie attività attraverso la vendita di guide turistiche che comprendono una mappa del percorso. Nel 2011 mi sono offerto come volontariato del FHTA per aggiornare la mappa ufficiale del sentiero. Come volontario, fare una mappa per un'organizzazione non-profit, QGIS è ottimo come strumento per la modifica dei dati e per impostare il layout finale della mappa. Grazie agli sforzi miei e dei membri della FHTA. la nuova mappa ufficiale del Fundy Foothpath viene inclusa nella guida.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## Il Progetto
Il processo di creazione della nuova mappa Fundy Footpath con QGIS può essere suddiviso in tre parti distinte:
- Raccolta dati,
- Modifica ed impostazione dei dati,
- Produzione di mappe.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

Per preparare i dati per l'utilizzo nella mappa finale, sono stati usati i seguenti strumenti per svolgere compiti specifici:
- I dati raccolti con il GPS sono stati puliti utilizzando la barra degli strumenti di modifica.
- I dati vettoriali ottenuti da NRCan e BNS sono stati messi insieme, interrogati, e tagliati per la mappa finale utilizzando gli strumenti vettoriali.
- Un file separato da virgole (CSV) ottenuto dalla BNS è stato importato in QGIS come un layer di punti utilizzando l'apposito plugin. Il plugin di interpolazione è stato utilizzato per creare un raster di elevazione; per creare un raster di elevazione è stato usato il plugin strumenti raster GDAL strumenti.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusione
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Collegamenti
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Autore
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Questo articolo è stato scritto da Jarrett Totton nel mese di gennaio del 2013. Jarrett è un tecnologo GIS che vive in Alberta, Canada.
