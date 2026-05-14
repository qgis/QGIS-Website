---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: QGIS et GRASS pour la modélisation des corridors écologiques des loups dans
  le nord du portugal
type: case-study

---
{{<content-start >}}
# QGIS et GRASS pour la modélisation des corridors écologiques des loups dans le nord du portugal
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

Ribeira de Pena est une municipalité dans le district de Vila Real, dans le nord du Portugal. Il s'agit d'une municipalité rurale, caractérisée par l'agriculture, le pâturage du bétail, des forêts, des montagnes, des vallées et une faune diversifiée, avec une faible densité humaine, qui offre un abri et de la nourriture pour les loups. Situé dans une zone de transition entre le rude et montagneux Tras-os-Montes et le verdoyant Minho, Ribeira de Pena est l'une des municipalités qui peut fonctionner comme un corridor écologique entre les zones à concentration élevée loup dans le nord avec une concentration plus faible dans le sud.

J'ai commencé à utiliser les logiciels SIG pendant mes études de biologie, et plus souvent pendant mon mémoire de master. A cette époque j'utilisais principalement des logiciels propriétaires. Après la fin de mon master, j'ai perdu l'accès aux logiciels propriétaires.

En attendant, je suis entrée dans le nouveau monde de Linux. Après ça, j'ai été contactée pour aidé des chercheurs à modéliser les corridors écologiques des loups à RIbeira de Pena, en utilisant les SIG,  puisqu'ils n'avaient jamais travaillé avec ce type de logiciel. Comme j'utilisais déjà Linux au lieu de Windows, mon premier problème fut de trouver quel logiciel utiliser. Après, j'ai entendu parler de QGIS et j'ai décidé de faire un essai, malgré qu'il me semblait très simpliste et incomplet quand je le comparais à ceux que je connaissais déjà. J'ai vite réalisé à quel point je m'étais trompée, et je fus vraiment enthousiaste aux vues des capacités analytiques de QGIS, spécialement avec l’intégration de GRASS

Pour modéliser les corridors écologiques, nous avons utilisé QGIS avec l'extension GRASS. Nous avons utilisé plusieurs informations géographiques combinées avec les données de présence des espèces pour modéliser les corridors écologiques. Voici quelques fonctions de QGIS et de GRASS que nous avons utilisées dans ce cas d'étude:
- Extension Interpolation de QGIS: pour créer un Modèle d'Elévation Numérique.
- r.watershed sous GRASS: pour créer les cours d'eau à partir du MEN.
- r.grow.distance sous GRASS: génère une couche raster de la distance aux entités de la couche d'entrée.
- r.reclass sous GRASS: pour re-classifier les couches cartographiques.
- r.slope.aspect.slope sous GRASS: pour calculer les bassins versants à partir du MEN.
- r.mapcalculator sous GRASS: pour calculer des cartes avec de l'alggèbre simple.
- r.cost.coord sous GRASS: créé une carte raster qui affiche le coût cumulé du déplacement entre plusieurs positions géographiques d'une couche raster d'entrée ou les valeurs des cellules représentent le coût.
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

Avec ce travail, nous avons obtenu une carte avec les corridors écologiques potentiels pour les populations de loups dans la municipalité de Ribeira de Pena. Il s'agit de surfaces qui peuvent être prises en compte par les techniciens de la ville lors de la planification de mesures de conservation des espèces. Ces corridors sont d'une extrême importance car il permettent de connecter la population fragile des loups de Vila Real dans le sud avec celles du nord qui sont en communication avec celles de Peneda-Gerês et de l'Espagne qui sont beaucoup plus stables. Les corridors qui croisent des installation humaines comme des petits villages, des villes, des routes sont d'une importance particulière. Ces territoires sont considérés comme critiques pour la conservation du loup et des mesures doivent y être appliquées pour réduire l'impact de l'homme sur ces espèces.

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## Conclusion
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Auteur
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

Cet article a été rédigé en Juillet 2012 par Monica Almeida. Elle est biologiste de la conservation et travaille dans une organisation non gouvernementale pour la préservation du loup au Portugal.

{{<content-end >}}
