---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 'Sistema Informativo e di Osservazione dell''Acqua: Abilitare l''Uso di Dati
  di Osservazione della Terra per la Gestione Integrata della Risorsa Idrica in Africa'
type: case-study

---
{{<content-start >}}
# Sistema Informativo e di Osservazione dell'Acqua: Abilitare l'Uso di Dati di Osservazione della Terra per la Gestione Integrata della Risorsa Idrica in Africa
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Descrizione del sistema
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Un vantaggio chiave di Processing è la capacità di utilizzare senza problemi funzionalità di diversi fornitori di algoritmi per l'elaborazione e l'analisi dei dati. Questo può essere usato per creare modelli di elaborazione automatica e, attraverso un plugin QGIS sviluppato durante il progetto TIGER-NET, per combinare in sequenza gli algoritmi dei diversi fornitori in catene di elaborazione basate su procedure guidate. Questa funzionalità è stata utilizzata per creare una libreria di flussi di lavoro standardizzati (con istruzioni) per l'esecuzione di attività comuni ma complesse relative all'analisi dei dati EO nella gestione delle risorse idriche.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

L'uso operativo e pratico del WOIS per sostenere la gestione integrata delle risorse idriche in Africa è stato dimostrato attraverso una serie di casi dimostrativi che coprono una vasta gamma di temi. Questi includono: la qualità dell'acqua dei laghi; il monitoraggio delle inondazioni; il degrado del territorio e la caratterizzazione dei suoli; la mappatura di corpi idrici e la modellizzazione idrologica. I casi dimostrativi hanno diverse fasi. Innanzitutto vengono sviluppati flussi di lavoro personalizzati e completi per i prodotti e le applicazioni richiesti. Tali flussi di lavoro vengono successivamente utilizzati per la derivazione del prodotto su aree significative e periodi di tempo richiesti dagli utenti. Nella fase finale, i flussi di lavoro (vale a dire la loro stabilità / prestazioni e facilità d'uso) così come i risultati del prodotto sono in fase di valutazione in stretto dialogo con gli utenti.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## Conclusione
Lo sviluppo di WOIS rappresenta un esempio di successo di un modello di sviluppo collaborativo e basato sull'utente, in cui le funzionalità sono state progettate, sviluppate e valutate attraverso casi proposti dall'utente al fine di dimostrare l'impatto reale del sistema sul miglioramento della gestione dell'acqua e sui piani di gestione integrati delle risorse idriche. Il WOIS è già implementato nelle principali autorità dei bacini idrografici africani, in diversi ministeri e agenzie africani, nonché in organizzazioni di ricerca e umanitarie. Continuerà quindi a svilupparsi in risposta a continue richieste degli utenti per nuove funzionalità e miglioramenti funzionali e grazie a miglioramenti generali di software, algoritmi e metodi.

Un'attenzione particolare sarà rivolta a garantire il supporto e l'implementazione della capacità di elaborazione per il nuovo sistema satellitare Sentinel integrando gli strumenti ESA Sentinel in WOIS e sviluppando flussi di lavoro dedicati. La prossima versione di WOIS (prevista nella seconda metà di aprile 2015) includerà già Sentinel-1 e una serie di flussi di lavoro che utilizzano questo nuovo set di dati radar per il monitoraggio delle inondazioni, la mappatura del corpo idrico, ecc. Questo trasformerà WOIS in un sistema di monitoraggio pienamente operativo. Attraverso la fornitura di questo sistema con licenza libera, potente ed estensibile, e attraverso il continuo sviluppo delle capacità e degli sforzi di formazione, il progetto si sforza di costruire le basi per un'ulteriore estensione, vale a dire il lancio in altri paesi e regioni in Africa e oltre.
## Riferimenti
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Collegamenti
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autore
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
