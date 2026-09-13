---
HasBanner: false
archived: true
date: 2011-12-31
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/nigeria_jos1.jpg
title: Cartographie de la faune aviaire et de l'habitat de la réserve forestière d'Amurum
  au Nigéria avec QGIS
type: case-study

---
{{<content-start >}}
# Cartographie de la faune aviaire et de l'habitat de la réserve forestière d'Amurum au Nigéria avec QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>December 31, 2011</span>
</p>

La réserve forestière Amurum est située près de la ville de Jos, Etat du Plateau, au Nigeria. Elle a été créée en collaboration avec l'Institut de recherche ornithologique AP Leventis  (APLORI) pour la protection de la nature, l'éducation et la recherche. APLORI est hébergé par le Département de zoologie à l'Université de Jos. Chaque année, un groupe d'environ huit étudiants motivés de tout le Nigeria reçoivent une formation en biologie de la conservation, en statistiques (avec R) et en SIG depuis 2011. Pendant deux semaines en décembre 2011, nous avons étudié les concepts de base des SIG que nous avons appliqués via QGIS à diverses fins de conservation. 

Dans cet article, nous décrivons la manière dont nous avons utilisé QGIS pour cartographier les habitats et leurs marqueurs pour la réserve Amurum, et comment les cartes de base de l'habitat ont été utilisés pour obtenir des couches dans le but de déterminer efficacement la distribution spatiale de l'avifaune, y compris la biodiversité.

<figure>
<img src="../images/nigeria_jos1.jpg" class="align-right" alt="nigeria_jos1.jpg" />
<figcaption>Training Group</figcaption>
</figure>

## Cartographie de l'élévation, ombrage, pente et habitats
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) Les GDALTools ont été utilisées pour fusionner les sets de données initiaux et pour découper des zones plus petites englobant la réserve afin de réduire la taille des données raster. Nous avons relevé par GPS des élévations en différents endroits de la réserve.
3) De manière générale, les données altimétriques SRTM correspondent bien avec les relevés d'altimétrie par GPS. Les modèles de terrain ont été utilisés afin de calculer via les GDALTools les ombrages et les pentes pour le secteur. Ces variables sont importantes d'un pioint de vue écologique car elles sont fortement associées avec le type d'habitat.

<figure>
<img src="../images/nigeria_jos2.jpg" class="align-right" alt="nigeria_jos2.jpg" />
<figcaption>QGIS screenshot</figcaption>
</figure>

4) Comme nous souhaitions créer des cartes attratives, vous avons interpolé les raster (source) d'élévation afin obtenir un raster de meilleur résolution. Nous avons utilisé l'outil warp tool des GDALTools. Ensuite, nous avons utilisé l'outil de création de contours pour obtenir des courbes de niveaux lissées.
5) Les coordonnées des limites de la réserve ont été obtenues en marchant le long de celles-ci avec un GPS. Les waypoints et les traces stockés dans le GPS ont été facilement importés via les GPS Tools puis utilisés pour construire un shapefile de polygones. Les routes à l'intérieur de la réserve ont été cartographiées de la même manière.
6) Nous avons pu construire précisément et rapidement une carte des habitats d'Amurum en utilisant les images satellites de Google que nous avons récupérées dans l'espace de travail via l'extension OpenLayers. La réserve comporte 3 types d' habitats : Savane, Forêt-Galerie, et Affleurements rocheux. Sur la base de l'image satellite, nous avons utilisé l'éditeur afin de digitaliser les polygones démarquant ces 3 habitats. Le réglage correct des options d'accrochage a permis de créer des polygones non superposés.

## Cartographier la diversité et la répartition des oiseaux
Les cartes d'habitats ont été utilisées pour créer des positions aléatoires. Les zones de différents type d'habitat ont été utilisées pour générer un nombre de positions proportionnelle à la surface de chaque type d'habitat (stratification).

<figure>
<img src="../images/nigeria_jos3.jpg" class="align-right" alt="nigeria_jos3.jpg" />
<figcaption>Training Group</figcaption>
</figure>

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Conclusion
Overall, the course was a great success. We - a group of students with no previous GIS experience —— enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

<figure>
<img src="../images/nigeria_jos4.png" class="align-right" alt="nigeria_jos4.png" />
<figcaption>QGIS map: Diversity of Amurum Forest Reserve</figcaption>
</figure>

## Auteurs
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill

{{<content-end >}}
