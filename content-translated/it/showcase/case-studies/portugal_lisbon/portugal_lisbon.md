---
draft: 'true'

---
# Utilizzo di QGIS per mappare aree di interesse per la biodiversità e l'ecosistema (HABEaS)
HABEaS \-\-- Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

L'obiettivo principale di questa piattaforma è quello di fornire l'accesso gratuito a una vasta gamma di dati sulla biodiversità e dei servizi ecosistemici per il bacino del Mediterraneo, che era dispersa in vari di enti pubblici e privati​​. Attualmente HABeas WebGIS copre il sud del Portogallo, ma entro la fine del 2012/primi 2013 sarà ampliato a nord del Portogallo e anche per il Cantone di Tuzla in Bosnia Erzegovina. Nel lungo periodo vogliamo estendere questo strumento per coprire l'intero bacino del Mediterraneo.

![](./images/portugal_lisbon1.jpg){.align-right}

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](./images/portugal_lisbon2.jpg){.align-right}

Le informazioni geografiche contenute in habeas sono state utilizzate anche dal WWF per fornire il supporto per l'identificazione per le foreste ad alto valore di conservazione (HCVF), nel sud del Portogallo, passaggio obbligatorio per i proprietari terrieri che vogliono ricevere la Certificazione Forest Stewardship Council (FSC).

![](./images/portugal_lisbon3.jpg){.align-right}

Per determinare i valori di conservazione per ogni proprietà, abbiamo usato SEXTANTE Modeller per creare uno script che interseca tutti habeas livelli con i confini della proprietà. Utilizzando lo stesso strumento siamo stati in grado di creare uno script che calcola automaticamente la quantità di carbonio che è attualmente memorizzato in ciascuna struttura.

![](./images/portugal_lisbon4.jpg){.align-right}
## Conclusioni
QGIS è facile da usare e ha molte funzionalità di geoprocessing potenti. L'integrazione di GRASS GIS e SAGA GIS strumenti attraverso i SEXTANTE Toolbox ci ha permesso di effettuare una serie di analisi spaziali complesse utilizzando SEXTANTE Modeler. È stato anche molto semplice produrre mappe di alta qualità con il nuovo Compositore di stampa e esportarli in formato SVG per un ulteriore editing con Inkscape che è un potente editor di grafica vettoriale open source.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Autore
![Filipe Dias](./images/portugal_lisbonaut.jpg){.align-left height="200px"}

Filipe Dias è uno studente di dottorato presso il Centro di Ecologia Applicata (Instituto Superior de Agronomia, Università tecnica di Lisbona) e consulente del Programma Mediterraneo del World Wide Fund for Nature (WWF).
