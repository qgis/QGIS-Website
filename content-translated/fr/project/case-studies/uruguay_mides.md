---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/uruguay_mides1.png
title: L'utilisation de QGIS au ministère du Développement Social de l'Uruguay (MIDES)
type: case-study

---
{{<content-start >}}
# L'utilisation de QGIS au ministère du Développement Social de l'Uruguay (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## Introduction
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## QGIS au Département de géographie du DINEM
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

La logistique, pour permettre le travail de terrain, comprend l'utilisation de logiciels de statistiques pour gérer la base de données générée et l'utilisation intensive de SIG pour organiser les campagnes de terrain et géo-référencer les données acquises.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

Bien que des logiciels commerciaux aient été utilisés lors du lancement du programme, le développement des tâches elles-mêmes ont graduellement fait qu'ils ont été remplacés par des logiciels open source. Comme le processus dans sa globalité devenait de plus en plus informatisé - comprenant un moteur de méthodes de travail et une base de données géospatiales PostGIS -, les exigences de licence et les avantages offerts par les différents logiciels open source et libres (FOSS) nous ont encouragé à faire le changement. De cette manière, au vu du raffinement de QGIS (moins de bogues et plus de fonctionnalités), nous avons pu répondre à nos besoin par l'utilisation de QGIS. Les outils associés à PostGIS ont permis au groupe de travail de coordonner rapidement les tâches nécessaires à la visualisation des campagnes de terrain journalières, avec les tâches subséquentes d'analyses de ces mêmes données de terrain, peu de temps après leur acquisition et numérisation.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## Conclusion
QGIS est devenu un logiciel clé pour le Département de géographie du DINEM. Il offre une performance excellente pour travailler avec de très gros fichiers et pour interagir avec PostGIS et notre moteur de méthodes de travail. Ceci nous permet d'avoir une très bonne gestion des données géographiques et permet aussi la production de cartes de base et de cartographies thématiques de qualité supérieure.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## Auteurs
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - Conseiller en analyses spatiales au Département de géographie (DINEM-MIDES, Uruguay). Étudiant en doctorat de sciences sociales, études des populations. Magistère en études contemporaines de l'Amérique latine. Diplôme en sciences anthropologiques.

Martín Hahn - Conseiller en analyses spatiales au Département de géographie (DINEM-MIDES, Uruguay). Bac. Étudiant pour un diplôme de géographie.

Bien que le présent article ait été rédigé par les trois personnes sus citées, il y a eu plus d'une centaine de personnes d'impliquées dans le processus qui y est décrit ; ce travail leur appartient donc en grande partie.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
