---
draft: 'true'

---
# Crearea cu ajutorul QGIS a căii de acces pentru traseul Fundy
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Traseul a fost creat, menținut și promovat de un grup de voluntari, cunoscut sub numele de Asociația Traseului Turistic Fundy Inc. (FHTA)(1975). Ca și organizație non-profit, FHTA strânge fonduri pentru activitățile sale prin vânzarea de ghiduri, acestea incluzând și o hartă a traseului. În 2011 am abordat FHTA, oferindu-mă ca voluntar la actualizarea hărții traseului oficial. La elaborarea unei hărți pentru o organizație non-profit, QGIS s-a potrivit perfect, atât ca instrument de editare a datelor cât și pentru aspectul final al hărții. Prin eforturile depuse de mine și de membrii FHTA, noua hartă oficială a traseului Fundy, inclusă în ghid, a fost creată de la început până la sfârșit cu QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## Proiectul
Procesul de creare a noii harta trotuare Fundy cu QGIS poate fi împărțit în trei părți diferite:
- Colectarea datelor.
- Editarea și pregătirea datelor .
- Producția hărții.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

Pentru a pregăti datele pentru utilizare în producerea hărții finale, următoarele instrumente din QGIS au fost utilizate pentru a îndeplini sarcini specifice:
- Datele culese cu GPS-ul au fost curățate cu ajutorul barei de instrumente de editare.
- Datele vectoriale obținute de la NRCan și SNB au fost unite, interogate, și cartografiate cu ajutorul instrumentelor vectoriale.
- Un fișier de valori separate prin virgulă obținut de la SNB a fost importat în QGIS ca strat de tip punct folosind plugin-ul Add Delimited Text Layer, pluginul de interpolare a fost folosit pentru a crea un raster de elevație, care a fost apoi utilizat pentru a crea un raster cu umbriri, iar stratul curbelor izometrice s-a realizat cu plugin-ul instrumentelor raster GDAL.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Concluzii
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Legături
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Autor
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Acest articol a fost transmis de către Jarrett Totton în ianuarie 2013. Jarrett este un tehnolog GIS care trăiește în Alberta, Canada.
