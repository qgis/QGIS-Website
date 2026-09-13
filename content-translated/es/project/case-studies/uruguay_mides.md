---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/uruguay_mides1.png
title: Uso de QGIS en el Ministerio de Desarrollo Social de Uruguay (MIDES)
type: case-study

---
{{<content-start >}}
# Uso de QGIS en el Ministerio de Desarrollo Social de Uruguay (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## Introducción
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## QGIS en el Departamento de Geografía de la DINEM.
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

La logística para viabilizar dicho trabajo de campo involucró el uso de paquetes estadísticos para administrar la base de datos generada, junto con un uso intensivo de GIS para organizar viajes de campo y datos relevados georeferenciados.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

Aunque el software propietario se implementó cuando comenzó el proceso de trabajo, el desarrollo de las tareas en sí mismo exigió gradualmente que se convirtiera a software de Código Libre. A medida que el proceso en su conjunto se volvió más informatizado (la incorporación de un motor de flujo de trabajo y una base de datos geoespaciales de PostGIS), los requisitos de licencia y los beneficios ofrecidos por las opciones de software de código abierto y Libre (FOSS) nos animaron a hacer el cambio. De esa manera, a medida que se refinaba el proyecto de QGIS (menos errores y más funcionalidades), pudimos satisfacer nuestras necesidades utilizando QGIS. Las herramientas asociadas de PostGIS permitieron al grupo de trabajo coordinar rápidamente las tareas necesarias para viabilizar los viajes de campo diarios, junto con las tareas de análisis subsiguientes en el mismo campo de datos generado, poco después de que fue relevado y digitalizado.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## Conclusión
QGIS se ha convertido en un software fundamental para el Departamento de Geografía de DINEM. Presenta un excelente rendimiento para trabajar con archivos pesados e interactuar con PostGIS y con nuestro motor de flujo de trabajo. Esto nos permite tener una excelente gestión de datos geográficos, lo que también contribuye a la producción de mapas base y cartografías temáticas de calidad superior.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## Autores
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - Asesor en la Sección de Análisis Espacial del Departamento de Geografía. (DINEM-MIDES, Uruguay). Estudiante Ph.D de Ciencias Sociales, Estudios de Población. Magister en Estudios Contemporáneos de América Latina. Licenciado en Ciencias Antropológicas.

Martín Hahn - Asesor en la Sección de Análisis Espacial del Departamento de Geografía (DINEM-MIDES, Uruguay). Soltero. Actualmente cursando el Grado de Geografía.

A pesar de que el presente artículo fue escrito por los tres mencionados anteriormente, hay más de un centenar de personas involucradas en el proceso descrito en él, por lo que este trabajo pertenece principalmente a ellos.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
