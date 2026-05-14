---
draft: 'true'

---
# Uso della console python per preparare mappe offline da WMS (scaricatore di mattonelle)
Questo studio spiega come preparare le mappe offline da sorgenti WMS/WFS o qualsiasi mappa caricata in QGIS, scaricando le tile con l'aiuto di uno script in python. Lo script genera anche un mosaico di tutte le piastrelle.

L'accesso vettoriale e raster tramite Web Map Service (WMS) è un servizio molto comune ed efficace. Essa ha diversi vantaggi, come la sicurezza, stili di mappa flessibili centralizzati. Un esempio sono le mappe Google maps, Yahoo, Bing, MODIS, Landsat, le carte pubblicate dalla NASA, NRSC (India). Lo svantaggio/limitazione di WMS è che funziona via internet o intranet. Potrebbe non essere possibile ottenere una connessione internet, specialmente sul campo durante i sondaggi. Anche il WMS è lento rispetto a qualsiasi formato di immagine non in linea come GeoTiff, jpg, img ecc.
## Uso di QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Console python
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. X,Y coordinate (superiore sinistro inferiore e destro) della prima piastrella
2. Dimensione della piastrella da scaircare (es 0.001 X 0.001 gradi)
3. Numero di piastrelle da scaricare (calcolata in base all'estensione della mappa e alla dimensione della piastrella)
4. Cartella di destinazione dove memorizzare le piastrelle

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

Il metodo ha limitazioni: i cambiamenti nella mappa lato server non si rifletteranno nelle mappe offline.  In questo caso l'utente dovrà ripetere la procedura e generare nuovi offline mappa. La seconda limitazione è che la mappa offline creata sarà in formato immagine e non può essere utilizzata per la creazione di mappe tematiche o per la classificazione delle immagini. Con alcuni sforzi supplementari, alcune mappe possono essere convertiti in immagini vettoriali con qualche perdita di dati.
## Obiettivo
Il mosaico è una pura immagine anche se è scaricato dalla mappa tematica (7-8 colore).  Con uno strumento avanzato, come riclassificazione, analisi strato/banda, questo raster può essere convertito in vettore poligono. Il WMS ha diverse richieste come getcapabilities, getmap getfeatureinfo, ecc. Utilizzando il getgeatureinfo possono essere recuperati gli attributi per ogni poligono. Lo script può essere convertito in plugin, in modo tale che chiunque senza conoscenze di scripting possa essere in grado di utilizzare lo script.
## Conclusione
Queste esperienze dimostrano che QGIS può essere utilizzata a qualsiasi livello avanzato. Con competenze di programmazione si può scrivere un piccolo script o un plug-in per migliorare la qualità del lavoro e risparmiare tempo. In QGIS, l'accesso a un repository di plug-in sviluppati a livello mondiale, è il lato migliore di QGIS. Il PyQGIS Developer Cookbook è una grande risorsa per scrivere uno script e elaborazione dati raster è molto più facile ora con l'aiuto di strumenti GDAL.
## Autori
Questo articolo è stato scritto nel maggio 2014 da Prashant Kadgi, a Pune (India) e lavora attualmente come consulente in servizi di consulenza GIS. Dal 2009 lavora con GIS & RS in NRM, forestali, e-governance, progetti di sviluppo software, in diverse regioni dell'India e del mondo.
- Contact: <kadgiprashant@gmail.com>
- Sito web www.gisappco.com (in costruzione)
