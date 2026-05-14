---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/india_assam1.png
title: 'Utilisation de QGIS pour le suivi des tigres (à l''aide de pièges photographiques
  dans la réserve de tigres de Nameri, Etat de l''Assam, District de Sonitpur, Inde) '
type: case-study

---
{{<content-start >}}
# Utilisation de QGIS pour le suivi des tigres (à l'aide de pièges photographiques dans la réserve de tigres de Nameri, Etat de l'Assam, District de Sonitpur, Inde) 
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

Dans ce paysage, les principales espèces d'importance pour la conservation sont le tigre royal du Bengale, l'éléphant d'Asie, bison indien, le léopard commune , la panthère nébuleuse, le dhole ("chien sauvage d'Asie"), le cerf Sambar, le cerf aboyeur, le cerf cochon, le sanglier et plusieurs autres espèces. La diversité des oiseaux de la réserve est également assez impressionnante et plus de 370 espèces d'oiseaux ont été identifiées à ce jour. La réserve est gérée par le Département des forêts de l'Assam, du gouvernement de l'Assam.
## Application de QGIS pour concevoir l'étude des photographies pièges
A partir de l'année 2011, l'Autorité Nationale pour la Conservation des Tigres de l'Inde (NTCA) a rendu obligatoire le suivi des tigres à l'aide de pièges photographiques pour toutes les réserves de tigres du pays . En vertu de ce nouveau protocole, 25 paires de caméras seront installées sur 100 km ² de la réserve de tigres et la période d'échantillonnage est de 40-60 jours. Ce nouveau protocole de surveillance tigre s'appuie fortement sur le SIG.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

Durant les années 2012-13, nous avons mis en place ce nouveau protocole de suivi des tigres au sein de la réserve en utilisant QGIS. Pour commencer, nous avons numérisé les limites de la réserve dans QGIS et enregistré celle-ci en tant que polygone. Ce polygone de délimitation a été exporté dans un GPS à des fins de navigation pour les enquêtes de terrain. Nous avons mené une vaste enquête dans la réserve à la recherche d'indices de présence de tigre  tels que des empreintes, des griffures et des excréments. Les coordonnées GPS des indices de présence de tigre ainsi que des emplacements appropriés pour des pièges photographiques ont été enregistrées. Après l'achèvement de l'enquête, les données ont été transférées dans QGIS, à l'aide des outils GPS, pour un traitement ultérieur et pour finaliser l'emplacement de pièges photographiques. Un fichier Shape contenant les indices de présence de tigres et les emplacements probables des pièges photographiques a été préparé.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Conclusion
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Auteur
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Cet article a été rédigé par G. Rajendra Garawad en Mars 2013. Il est le directeur de campagne de la réserve de tigres "Nameri Reserve Tiger", Assam, en Inde. Il détient un diplôme de Master en sciences forestières, de conservation et de gestion des terres.

{{<content-end >}}
