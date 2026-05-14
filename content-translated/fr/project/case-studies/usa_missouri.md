---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/usa_missouri1.png
title: Utilisation de QGIS pour cartographier des enregistrements herpétologiques
  historisés (Missouri, USA)
type: case-study

---
{{<content-start >}}
# Utilisation de QGIS pour cartographier des enregistrements herpétologiques historisés (Missouri, USA)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Création et exportation de cartes statiques
Le processus de création de cartes sous QGIS débute avec des données stockées dans plusieurs tables PostgreSQL/PostGIS. Parce que les cartes sont statiques et destinées en fin de compte au web ou à un atlas papier, elles sont générées de façon automatisée pour chaque espèce grâce à une extension python créée sur mesure (Figures 1,2).

<figure>
<img src="../images/usa_missouri1.png" class="align-right" alt="usa_missouri1.png" />
<figcaption>Custom map generation and export user interface, maps are generated and exported in a batch process.</figcaption>
</figure>

The final species maps have a clean and professional appearance (Figure 3). To better understand species\' distributions, a series of base maps are also created and labelled (Figure 4). Because of the way styles are managed within each data layer, the base map layers can also be incorporated into a set of species maps with little extra effort.

<figure>
<img src="../images/usa_missouri2.png" class="align-right" alt="usa_missouri2.png" />
<figcaption>Maps are displayed as static images.</figcaption>
</figure>

<figure>
<img src="../images/usa_missouri3.png" class="align-right" alt="usa_missouri3.png" />
<figcaption>Labelled Level III Ecoregion map for Missouri and surrounding states.</figcaption>
</figure>

## Conclusions
Au démarrage du projet MOHAP, plusieurs outils commerciaux et propriétaires étaient utilisés pour stocker et traiter les données et pour produire des cartes destinées à la publication. Dès 2007, nous avons entamé la migration de tous les aspects du projet vers du logiciel open source. QGIS, associé à PHP, PostgreSQL, PostGIS, Python et à ReportLab constitue le pivot open source de MOHAP, assurant au projet et à ses données une existence indépendante des logiciels propriétaires.

QGIS se connecte nativement à PostGIS et dispose d'une architecture axée autour de modules python, essentiels pour automatiser la création et l'export de cartes. La large documentation de l'API et le développement d'extensions ont permis de créer exactement ce dont nous avions besoin au niveau de l'automatisation. L'aide de la communauté est aussi très bonne et inclut un large panel d'extensions prêtes à l'emploi.

Bien que nous utilisions QGIS de façon assez précise et spécifique, ses possibilités et son extensibilité grâce à Python le rendent plus que suffisant pour aborder des projets plus grands et plus complexes.
## Auteur
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
