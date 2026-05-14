---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: Utiliser QGIS pour cartographier les zones de services écosystémiques de la
  biodiversité (HABEaS)
type: case-study

---
{{<content-start >}}
# Utiliser QGIS pour cartographier les zones de services écosystémiques de la biodiversité (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Le but principal de cette plateforme est de fournir un accès gratuit à un grand nombre de données sur les services écosystémiques et sur la biodiversité du bassin méditerranéen, qui étaient jusqu'alors réparties entre de nombreuses structures publiques et privées.
À ce jour, le WebSIG HABEaS ne couvre que le sud du Portugal, mais à l'horizon fin 2012 / début 2013, son extension est prévue jusqu'au nord du pays ainsi qu'au canton de Tuzla en Bosnie Bosnie-Herzégovine. À terme, nous souhaitons étendre l'outil au bassin méditerranéen tout entier .

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

L'information géographique contenue dans HABEaS a également été utilisée par le WWF pour fournir des données d'identification pour le programme du High Conservation Value Forests (HCVF) du sud du Portugal qui est une étape obligatoire pour les propriétaires qui souhaitent obtenir la certification Forest Stewardship Council (FSC) pour leurs forêts.

![](../images/portugal_lisbon3.jpg)

Pour déterminer quelle valeur de conservation concerne chaque propriété, nous avons utilisé le modeleur graphique SEXTANTE pour créer un script qui intersecte toutes les couches HABEaS avec les limites de la propriété. En utilisant le même outil, nous avons été capable de créer un script qui calcule automatiquement la quantité de carbone qui est stocké dans chaque propriété.

![](../images/portugal_lisbon4.jpg)
## Conclusions
QGIS est facile à utiliser et possède de puissantes capacités de géo-traitement. L'intégration de GRASS GIS ET SAGA GIS dans la boite à outils SEXTANTE nous a permis de réaliser des analyses spatiales complexes en les combinant dans le modeleur graphique SEXTANTE. Il était aussi très facile de produire des cartes de grande qualité avec le nouveau composeur d'impression et de les exporter au format SVG pour d'ultérieurs traitements sous Inkscape, un puissant  logiciel libre d'édition d'images vectorielles.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Auteur
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias est un étudiant doctorant du Centre d’Écologie Appliquée (Instituto Superior de Agronomia, Université Technique de Lisbon) ainsi qu'un consultant pour le Programme Méditéranéen du World Wilde Fund for Nature (WWF).

{{<content-end >}}
