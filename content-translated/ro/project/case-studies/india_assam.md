---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS pentru monitorizarea tigrilor (folosind capcane foto, în Rezervația de
  Tigri Nameri, Assam, Districtul Indian Sonitpur)
type: case-study

---
{{<content-start >}}
# QGIS pentru monitorizarea tigrilor (folosind capcane foto, în Rezervația de Tigri Nameri, Assam, Districtul Indian Sonitpur)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

În acest ținut, principalele specii de importanță pentru conservare sunt tigrul regal de Bengal, elefantul asiatic, bizonul indian, leopardul comun, leopardul pătat, câinele sălbatic, cerbul de Sambar, cerbul porcin, căprioara lătrătoare, mistrețul și multe alte specii. Diversitatea păsărilor din NTR este, de asemenea, destul de impresionantă, mai mult de 370 de specii de păsări fiind identificate până în prezent. Rezervația este gestionată de Direcția Silvică a Administrației Assam.
## Aplicarea QGIS pentru proiectarea camerelor capcană ale studiului
Începând cu anul 2011, Autoritatea Națională pentru Conservarea Tigrilor (NTCA) din India a făcut obligatorie, pentru toate rezervațiile de tigri ale țării, monitorizarea cu ajutorul capcanelor foto. În cadrul acestui nou protocol, 25 de perechi de camere vor fi instalate de 100 km pătrați de rezervație, pe o perioada de eșantionare de 40-60 de zile. Acest nou protocol de monitorizare a tigrilor se bazează foarte mult pe GIS.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

În perioada 2012-13, am implementat acest nou protocol de monitorizare a tigrilor în NTR, prin utilizarea QGIS. Pentru început, am digitizat granița NTR în QGIS și am salvat-o ca poligon. Această zonă poligonală a fost exportată în GPS pentru scopuri de navigare pe perioada lucrului în teren. Am realizat o investigare extinsă a semnelor prezenței tigrilor în NTR, cum ar fi urme, zgârieturi și resturi. S-au înregistrat coordonatele GPS ale semnelor tigrilor precum și ale locațiilor potrivite pentru aparatele capcană. După finalizarea studiului, datele au fost transferate în QGIS, folosind instrumente GPS pentru prelucrare ulterioară și pentru stabilirea locațiilor capcanelor foto. A fost pregătit un fișier de tip shape care conține semne ale tigrilor și locațiile probabile ale aparatelor de fotografiat.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Concluzii
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Autor
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Acest articol a fost trimis de Rajendra G. Garawad, în martie 2013. El este Directorul Rezervației de Tigiri, Assam, India. El deține un master în Științe Silvice și Conservarea & Gestionarea terenurilor.

{{<content-end >}}
