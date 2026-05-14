---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS para monitorear tigres (usando trampas cámara en la Reserva de Tigre Nameri,
  Assam, Distrito Sonitpur India)
type: case-study

---
{{<content-start >}}
# QGIS para monitorear tigres (usando trampas cámara en la Reserva de Tigre Nameri, Assam, Distrito Sonitpur India)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

En este paisaje, las principales especies importantes para la conservación son el tigre real de Bengala, el elefante asiático, el bisonte indio, el leopardo común, el perro salvaje, el ciervo Sambar, el ciervo ladrador, el ciervo porcino, el cerdo salvaje, y varias otras especies. La diversidad de aves es bastante impresionante y más de 370 especies han sido identificadas hasta ahora. La reserva es gestionada por el Assam Forest Department, Gobierno de Assam.
## Aplicación de QGIS para diseñar un estudio con cámaras trampa.
Desde el año 2011, la National Tiger Conservation Authority (NTCA) de la India ha hecho obligatorio que todas las reservas de tigre del país monitoreen los tigres usando cámaras trampa. Con este nuevo protocolo, 25 pares de cámaras serán instaladas en 100 km2 de reservas de tigres y el periodo de muestreo será de 40-60 días. Este nuevo protocolo de monitoreo de tigres depende mucho de los SIG.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

Durante 2012-13, implementamos este nuevo protocolo para el monitoreo de tigres en NTR usando QGIS. Para empezar, digitalizamos en QGIS los límites de la reserva y los guardamos como un polígono. Este polígono fue exportado a GPS con fines de navegación durante el muestreo de campo. Hicimos una campaña extensiva de monitoreo de signos en NTR para encontrar evidencias de la presencia de tigres, tales como huellas, marcas de arañazos y heces. Las coordenadas GPS de los signos así como las de ubicaciones adecuadas para la colocación de las cámaras trampa fueron registradas. Una vez completado el muestreo, los datos fueron transferidos a QGIS usando las herramientas para GPS para posterior procesamiento y para la determinación de las ubicaciones de las cámaras trampa. Se preparó una shapefile que contenía los signos y las ubicaciones probables de las cámaras.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Conclusión
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Autor
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Este artículo fue contribuido por  Rajendra G. Garawad en marzo de 2013. Él es director de campo en la Nameri Tiger Reserve, Assam, India. Tiene Masters en Ciencia Forestal y Conservación y Gestión del Territorio.

{{<content-end >}}
