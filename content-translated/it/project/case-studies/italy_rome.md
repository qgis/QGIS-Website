---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/italy_igag1.png
title: Modello di geoprocessing QGIS per semplificare l'analisi di microzonazione
  sismica di primo livello
type: case-study

---
{{<content-start >}}
# Modello di geoprocessing QGIS per semplificare l'analisi di microzonazione sismica di primo livello
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Geochimica ambientale e risanamento di terreni ed acque contaminati;
- Depositi minerali e trattamento dei minerali, compreso il trattamento delle acque reflue;
- Geoingegneria e sicurezza degli scavi in roccia;
- Evoluzione geologica recente;
- Mitigazione dei pericoli naturali;
- Geoarcheologia e archeometria.
- Geologia marina
- Geomatica, analisi e sviluppo GIS.

Lo studio di microzonazione sismica di livello 1 dell'area di Pietramontecorvino (Puglia, Italia meridionale, situata lungo la catena dell'Appennino centro-meridionale) fa parte di un progetto, in collaborazione con l'Autorità di Bacino della Puglia (AdB Puglia) e il Dipartimento di Geologia e Geofisica (DGG) dell'Università di Bari, finalizzato alla microzonazione sismica di 63 Comuni dell'area di Foggia. L'attività è stata promossa dal Dipartimento della Protezione Civile (DPC) e finanziata dal Comitato Interministeriale per la Programmazione Economica (CIPE n. 20/2004).
## Strumento di geoprocessing QGIS per studi di microzonazione sismica di primo livello
La microzonazione sismica valuta la pericolosità sismica in scala locale proponendo di individuare aree di territorio caratterizzate da un comportamento sismico omogeneo. Il primo livello di microzonizzazione sismica ha lo scopo di definire le proprietà litologiche e la geometria delle unità geologiche che caratterizzano queste porzioni di territorio (microzone).

L'osservazione dei danni causati da un terremoto mostra spesso variazioni in scala locale causate non solo da strutture geologiche, ma anche da strutture edilizie di diversa qualità e tipologia, con conseguenti diversi rischi sismici.

La microzonazione sismica valuta la pericolosità sismica locale, attraverso l'individuazione di aree di territorio caratterizzate da un comportamento sismico omogeneo.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

La microzonazione sismica di primo livello consiste nella creazione di tre mappe tematiche:
1. Mappa dei rilievi contenente i rilievi per gli studi di microzonazione sismica;
2. Carta geolitologica, ottenuta da carte geologiche e geomorfologiche in scala dettagliata che integrano i dati litologici, stratigrafici e geotecnici esistenti relativi ai rilievi;
3. Mappa di microzonazione sismica di livello 1 (il prodotto principale della microzonazione di livello 1), che identifica le microzone in tre categorie di pericoli locali:
   - Zone stabili;
   - Zone stabili inclini all'amplificazione al suolo;
   - Zone instabili.

Lo scopo di questo lavoro è quello di contribuire alla creazione di una metodologia di elaborazione di dati topografici, geologici, geofisici e geotecnici finalizzati alla stesura di carte di microzonazione sismica di livello 1, attraverso l'utilizzo di strumenti open source.

Lo strumento Modellatore Grafico integrato nell'ultima versione di QGIS (2.8.1 al momento in cui scriviamo) è stato utilizzato per la creazione di un semplice modello di geoprocessing. Questo strumento è utile per automatizzare una delle analisi comunemente eseguite per la creazione di mappe di microzonazione sismica di livello 1, in particolare per identificare le zone instabili come caratteristiche dei poligoni.

Il modello si avvale di diversi software open source e librerie (GRASS, GDAL, QGIS), dimostrando l'utilità di QGIS come interfaccia semplificata e unificata per strumenti GFOSS (Geospatial Free e Open Source Software) eterogenei (Fig. 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

Il modello prende come input (Fig. 2):
- Uno shapefile di curve di livello contenente un campo con valori di elevazione;
- The name of the field containing elevation values;
- La risoluzione del raster desiderata in metri per DEM e Pendenza (predefinito 10);
- Verrà estratto uno shapefile di poligoni dal quale verranno estratte le aree di intersezione con pendenza superiore a 15 gradi;
- Il nome del vettore poligonale risultante.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Quando viene lanciato, il modello esegue le seguenti operazioni:
- Lo strumento GRASS v.to.rast.attribute converte le curve di livello in raster, prendendo come input lo shapefile del contorno, il nome del campo z e la risoluzione del raster;
- Lo strumento GRASS r.surf.contour genera il modello di elevazione prendendo come input l'output temporaneo rasterizzato del passo precedente e la risoluzione del raster;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- Lo strumento GRASS r.mapcalculator è utilizzato per generare un raster a 1 bit che identifica le aree con pendenza superiore a 15 gradi (questo valore è codificato nelle linee guida di microzonazione, e quindi è fisso), utilizzando l'espressione:

if(A\>15,1,null())

dove A è il raster temporaneo delle pendenze generato da gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Il risultato è un vettore poligonale con aree soggette ad instabilità a causa di un valore di pendenza superiore a 15 gradi, automaticamente estratto da una mappa tematica come ad esempio un vettore poligonale di frane (Fig. 3) o una mappa litologica.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Conclusioni
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Riferimenti
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autori
Questo articolo è stato realizzato nel marzo 2015 da Giuseppe Cosentino e Francesco Pennica (www.igag.cnr.it).

<figure>
<img src="../images/guiseppe_cosentino.png" class="align-left" height="200" alt="guiseppe_cosentino.png" />
<figcaption>Giuseppe Cosentino</figcaption>
</figure>

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

<figure>
<img src="../images/francesco_pennica.png" class="align-left" height="200" alt="francesco_pennica.png" />
<figcaption>Francesco Pennica</figcaption>
</figure>

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.

{{<content-end >}}
