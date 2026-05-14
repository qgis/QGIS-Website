---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/india_assam1.png
title: Monitorare le tigri con QGIS (utilizzando trappole fotografiche nel Nameri
  Tiger Reserve, Assam, India Sonitpur District)
type: case-study

---
{{<content-start >}}
# Monitorare le tigri con QGIS (utilizzando trappole fotografiche nel Nameri Tiger Reserve, Assam, India Sonitpur District)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

In questo paesaggio, le principali specie di importanza per la conservazione sono la tigre reale del Bengala, l'elefante asiatico, i bisonti indiani, il leopardo comune, il leopardo nebuloso, il cane selvatico, il cervo Sambar, cervi, caprioli, cinghiali e numerose altre specie. La diversità degli uccelli di NTR è anche abbastanza impressionante e sono state identificate più di 370 specie di uccelli finora. La riserva è gestita dal Dipartimento forestale Assam, governo di Assam.
## L'applicazione di QGIS per la progettazione delle trappole fotografiche 
Dall'anno 2011, la Tiger Conservation Authority nazionale (NTCA) dell'India ha reso obbligatorio per le tutte le riserve tigre del paese il monitoraggio delle tigri utilizzando trappole fotografiche. Nell'ambito di questo nuovo protocollo, 25 coppie di telecamere verranno installate per 100 kmq di riserva tigre e il periodo di campionamento è di 40-60 giorni. Questo nuovo protocollo di monitoraggio della tigre si basa molto sul GIS.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

Durante il 2012-13, abbiamo implementato il nuovo protocollo di monitoraggio tigre in NTR utilizzando QGIS. Per iniziare, abbiamo digitalizzato il confine NTR in QGIS e salvato come poligono. Questo poligono di confine è stato esportato in GPS per scopi di navigazione durante le indagini sul campo. Abbiamo condotto una vasta indagine nel NTR per ottenere testimonianze di presenza delle tigri come impronte, graffi e escrementi. Sono state registrate le coordinate GPS dei segni delle tigri così come i luoghi adatti per mettere le trappole fotografiche. Al termine del sondaggio, i dati sono stati trasferiti su QGIS usando strumenti GPS per l'ulteriore elaborazione e l'allocazione della località per le trappole fotografiche. È stato preparato un shapefile che contiene i segni tigre e le probabili destinazioni per le trappole fotografiche.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Conclusione
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Autore
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Questo articolo è stato scritto da Rajendra G. Garawad nel mese di marzo del 2013. Egli è il direttore del campo di Nameri Tiger Reserve, Assam, India. Ha conseguito un Master in Scienze Forestali e conservazione e gestione del territorio.

{{<content-end >}}
