---
author: Radoslaw Guzinski
categories:
- Case studies
date: '2015-04-01'
description: Enabling the Use of Earth Observation Data for Integrated Water Resource
  Management in Africa
draft: 'true'
heroImage: ''
tags:
- water
- case-study
- showcase
thumbnail: wois.png
title: Water Observation and Information System
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Description du système
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Un avantage clé de la Boîte à outils de Traitement est la capacité d'homogéneisation de l'utilisation des fonctionnalités de fournisseurs d'algorithme différents pour le traitement de données et l'analyse. Ceci peut être utilisé pour créer des modèles de traitement automatiques et, au travers d'un plug-in QGIS développé pendant le projet TIGER-NET, pour combiner par étapes des algorithmes de différents fournisseurs dans des chaînes de traitement assistées. Cette fonctionnalité a été utilisée pour créer une bibliothèque de gestion de commandes normalisées (avec des instructions) pour exécuter des tâches communes mais complexes liées à l'analyse de données EO en matière de gestion de la ressource en eau.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

L'utilisation opérationnelle et pratique du WOIS pour soutenir la gestion de la ressource en eau intégrée en Afrique a été démontrée via une série de cas précis de démonstration, couvrant une vaste gamme de thèmes et de produits de l'information. Ceux-ci incluent : qualité de l'eau de lac; surveillance d'inondation; la dégradation des sols et la caractérisation de l'occupation des sols; la cartographie des plans d'eau et la modélisation hydrologique. Les cas de démonstration ont plusieurs étapes. D'abord, les workflows personnalisés de traitement sont développés pour les produits et applications demandées. Ces workflows sont par la suite utilisés pour la dérivation de produit sur des zonesreprésentatives et des périodes demandées par les utilisateurs. Dans une étape finale, les workflows (c'est-à-dire leur stabilité/performance et facilité d'emploi) aussi bien que les résultats produits sont évalués d'un commun accord avec les utilisateurs.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Conclusion
Le développement du WOIS représente un exemple réussi d'un modèle de développement axé sur l'utilisateur et l'aspect collaboratif, où les fonctionnalités ont été conçues, développées et évaluées par des cas concrets d'utilisateur, afin de démontrer l'impact réel d'un système amélioré et de plans de gestion de la ressource en eau. Le WOIS est déjà mis en œuvre dans des autorités de gestion de bassins fluviaux majeurs en Afrique, plusieurs ministères africains et agences nationales, aussi bien que dans la Recherche et au sein d'organisations humanitaires. Il continuera donc à se développer en réponse aux exigences régulières d'utilisateurs pour de nouvelles fonctionnalités et en réponse aux améliorations fonctionnelles du logiciel en général, de l'algorithme et des améliorations méthodologiques.

Un soin particulier sera d' assurer le support et l'implémentation de la capacité de traitement pour le nouveau système de satellite Sentinel en intégrant les progiciels de l'ESA dans WOIS et et en développant des workflows de production dédiés. La prochaine sortie de WOIS (censée être dans la deuxième moitié d'avril 2015) incorporera déjà la Boite à outils Sentinel-1 et un certain nombre de workflows utilisant ce nouvel ensemble de données de radar pour la surveillances d'inondations, la cartographie des plans d'eau, etc. Ceci placera WOIS dans un système de contrôle entièrement opérationnel. Par la fourniture d'un licence libre, d'un système puissant et extensible, et au travers d'efforts de création et de formation, le projet tente de jetter les bases d'une diffusion à d'autres pays, d'autres régions en Afrique et au-delà.
## Références
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Liens
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Auteur
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
