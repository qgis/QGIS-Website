---
draft: 'true'

---
# Archivio delle mappe storiche erpetologiche con QGIS (in Missouri, USA)
The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Generazione ed esportazione di mappe statiche
Il processo di creazione di mappe con QGIS inizia con i dati memorizzati in diverse tabelle spaziali PostgreSQL-PostGIS. Poiché le mappe sono statiche e destinati sia per il web che per la stampa, vengono generati automaticamente per ogni specie utilizzando un plugin Python (figure 1,2).

![Custom map generation and export user interface, maps are generated and exported in a batch process.](./images/usa_missouri1.png){.align-right}

The final species maps have a clean and professional appearance (Figure 3). To better understand species\' distributions, a series of base maps are also created and labelled (Figure 4). Because of the way styles are managed within each data layer, the base map layers can also be incorporated into a set of species maps with little extra effort.

![Maps are displayed as static images.](./images/usa_missouri2.png){.align-right}

![Labelled Level III Ecoregion map for Missouri and surrounding states.](./images/usa_missouri3.png){.align-right}
## Conclusioni
All'inizio del progetto MOHAP, sono stati usati diversi strumenti commerciali e proprietari per memorizzare ed elaborare i dati e produrre mappe per la pubblicazione. A partire dal 2007, abbiamo iniziato a spostare tutti gli aspetti del progetto di software su open source. QGIS, insieme a PHP, PostgreSQL, PostGIS, Python, e ReportLab, costituisce il perno open source per MOHAP, consentendo di fornire al progetto tutti i dati senza sconvolgimenti. 

QGIS contiene il supporto nativo per PostGIS e di una architettura a plugin Python, che era essenziale per creare la generazione di mappe automatiche e per l'esportazione. L'ampia documentazione API che è stata utilizzata dal nostro sviluppatore del plugin per creare esattamente quello che ci serviva per l'automazione. Il sostegno comunitario è anche molto buono e comprende una vasta gamma di plugin condivisi pronti per l'uso.

Anche se usiamo QGIS in un modo specifico, le sue capacità e l'estensibilità grazie a Python è più che sufficiente per affrontare i progetti più grandi e complessi.
## Autore
![Brian Edmond](./images/usa_missouriaut.jpg){.align-left height="200px"}

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.
