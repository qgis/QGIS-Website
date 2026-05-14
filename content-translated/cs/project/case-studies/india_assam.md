---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS pro sledování tygrů (pomocí kamerových pastí v rezervaci Nameri Tiger
  Reserve, Assam, Indie, okres Sonitpur)
type: case-study

---
{{<content-start >}}
# QGIS pro sledování tygrů (pomocí kamerových pastí v rezervaci Nameri Tiger Reserve, Assam, Indie, okres Sonitpur)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

V této krajině jsou ochranářsky významnými druhy především tygr bengálský, slon asijský, zubr indický, levhart obecný, levhart obláčkový, pes divoký, jelen sambarský, jelen štěkající, jelen prasečí, prase divoké a několik dalších druhů. Ptačí rozmanitost NTR je také poměrně působivá a dosud bylo zjištěno více než 370 druhů ptáků. Rezervaci spravuje Assam Forest Department, Government of Assam.
## Použití QGIS při navrhování studií s kamerovými pastmi
Počínaje rokem 2011 indický Národní úřad pro ochranu tygrů (NTCA) nařídil, aby všechny tygří rezervace v zemi povinně monitorovaly tygry pomocí kamerových pastí. Podle tohoto nového protokolu bude na 100 km2 tygří rezervace instalováno 25 párů kamer a doba odběru vzorků bude 40-60 dní. Tento nový protokol monitorování tygrů se do značné míry opírá o GIS.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

V letech 2012-13 jsme tento nový protokol monitoringu tygrů v NTR zavedli pomocí QGIS. Nejprve jsme v QGIS digitalizovali hranice NTR a uložili je jako polygon. Tento hraniční polygon byl exportován do GPS pro účely navigace během terénních průzkumů. Provedli jsme rozsáhlý průzkum znaků v NTR, abychom našli důkazy přítomnosti tygrů, jako jsou pachové stopy, škrábance a trus. Byly zaznamenány GPS souřadnice tygřích stop a také vhodná místa pro umístění kamerových pastí. Po dokončení průzkumu byla data přenesena do QGIS pomocí nástrojů GPS pro další zpracování a pro finalizaci umístění kamerových pastí. Byl připraven shape soubor obsahující znaky tygrů a pravděpodobná místa umístění kamerových pastí.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Závěr
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Autor
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Do tohoto článku přispěl Rajendra G. Garawad v březnu 2013. Je terénním ředitelem tygří rezervace Nameri v indickém Ásámu. Je držitelem magisterských titulů v oborech lesnická věda a ochrana přírody a správa půdy.

{{<content-end >}}
