---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS et GRASS pour la cartographie des risques de feu de brousse a l'échelle
  locale
type: case-study

---
{{<content-start >}}
# QGIS et GRASS pour la cartographie des risques de feu de brousse a l'échelle locale
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Introduction
Le conseil régional des Southern Downs (SDRC) est une administration locale de taille intermédiaire située dans le sud-est du Queensland en Australie. L'aire de compétence du conseil, principalement la zone sud, souffre de nombreux feux de brousse. Les feux de brousse sont un réel problème pour les résidents et les propriétaires de la région du Southern Downs et ils ont entraînés des morts et des atteintes aux mobilier.

Ce projet permettra au conseil et aux gens de la région d'être plus au courant des risques et de prendre de meilleures décisions à l'avenir.

![](../images/australia_queens1.jpg)
## Le Projet
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

Le côté SIG du projet a été divisé en 6 grandes étapes.
- Evaluation de la pente et cartographie
- Evaluation de l'aspect et cartographie
- Evaluation de la végétation et cartographie
- Combinaison des résultats pour identifier le niveau de risque d'incendie de brousse
- Vérification sur le terrain et évaluation qualité
- Cartes finales

## L'utilisation de QGIS et GRASS
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

L'extension QGIS GRASS a été utilisé pour importer des courbes de niveau d'une résolution de 5 mètres dans GRASS. Ces courbes ont été converties dans une couche raster en utilisant r.surf.contour. Des cartes de pente et d'aspect ont été ensuite générées en utilisant r.slope.aspect à partir du raster des courbes de niveau. Des catégories ont été attribuées à différentes plages de pentes et d'aspect et un niveau de risque a été calculé. Les surfaces en végétation ont également reçu des niveaux de risque. Les cartes résultantes ont été combinées en utilisant mapcalc pour donner un niveau de risque final. Ces niveaux ont été ensuite divisés en trois catégories: haut, moyen et faible.

La partie finale du processus a été la vérification sur le terrain via le service rural d'incendie. Après la revue du processus, QGIS a été utilisé pour imprimer des cartes de présentation.

Toutes les commandes de GRASS peuvent être lancées depuis la ligne de commande, toutes les commandes nécessaire pour générer les cartes de risque de feu de brousse ont été enregistrées à des fins de documentation et en cas de besoin de générer à nouveau les cartes à l'avenir.
## Conclusion
Au final, l'utilisation de QGIS combiné à l'extension GRASS a été une bonne expérience avec l'intérêt pour le conseil de réaliser sa cartographie de risque incendie en régie. L'extension GRASS fournit une interface vers GRASS qui est facile à utiliser, à travers QGIS. Etant donné que QGIS est capable d'ouvrir nativement les rasters au format GRASS, l'intégration s'est déroulé assez naturellement et les cartes ont pu être facilement réalisées.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Références
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Auteur
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Cet article a été publié en janvier 2011 par Nathan Woodrow. Nathan est un agent SIG au conseil régional des Southern Downs (SDRC) et il effectue des études en alternance à l'univertisé des sciences spatiales du Southern Queensland.

{{<content-end >}}
