---
draft: 'true'

---
# Créer la carte des sentiers de Fundy avec QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Le chemin a été créé, est entretenu et développé par un groupe de bénévoles connu sous le nom de l'association Fundy Hiking Trail Association Inc., (FHTA) (1975). En tant qu'association à but non lucratif la FHTA lève des fonds pour ses activités à travers la vente de guides incluant des cartes des sentiers. En 2011, j'ai contacté la FHTA pour être bénévole afin de mettre à jour la carte officielle du chemin. En tant que bénévole réalisant une carte pour une association à but non lucratif QGIS a été parfait tant sur le plan de l'édition les données que pour la réalisation finale de la carte. Grâce à mes efforts ainsi qu'aux membres de la FHTA la nouvelle carte du Fundy Footpath incluse dans le guide a été créé de A à Z avec QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## Le Projet
Le processus de création de la nouvelle carte des sentiers avec QGIS peut-être divisé en 3 parties différentes:
- La collecte des données.
- L'édition et la préparation des données.
- La production de cartes.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

Pour préparer les données en vue de l'utilisation dans la carte finale, les outils suivants de QGIS ont été utilisés pour accomplir  différentes taches :
- Les données collectées par GPS ont été nettoyées en utilisant la barre d'outils édition.
- Les données vectorielles obtenues de NRCan et SNB ont été fusionnées, requêtées et découpées avec les outils vectoriels pour la carte finale.
- Un fichier texte délimité provenant de SNB a été importé dans QGIS en couche de point en utilisant l'extension d'Ajout de texte délimité. L'extension d'Interpolation a été utilisée pour créer un raster d'altitude ensuite utilisé pour créer un raster d'ombrage et des courbes de niveau avec les outils raster de GDAL.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusion
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Liens
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Auteur
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Cet article est une contribution de Jarrett Totton en Janvier 2013. Jarrett est technicien SIG en Alberta au Canada.
