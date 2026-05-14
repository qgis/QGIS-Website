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
## Descripción del sistema
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Una ventaja clave de la caja de herramientas de procesamiento es la capacidad de utilizar a la perfección las funcionalidades de diferentes proveedores de algoritmos para el procesamiento y análisis de datos. Esto se puede utilizar para crear modelos de tratamiento automático y, a través de un plugin de QGIS desarrollado durante el proyecto TIGER-NET, para combinar secuencialmente algoritmos de los diferentes proveedores en las cadenas de procesamiento basadas en asistentes. Se utiliza esta funcionalidad para crear una biblioteca de flujos de trabajo estandarizados (con instrucciones) para realizar tareas comunes, pero complejas, relacionadas con el análisis de datos EO dentro de la gestión de los recursos hídricos.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

El uso práctico y operacional de WOIS para apoyar la gestión integrada de los recursos hídricos en África ha sido demostrado a través de una serie de casos de uso demostrativos específicos que cubren una amplio rango de temas y productos de información. Estos incluyen: calidad de agua lacustre, monitoreo de inundaciones, caracterización de la cobertura terrestre y su degradación, mapeo de cuerpos de agua y modelación hidrológica. Estos casos demostrativos tienen varias etapas. Primero, se desarrollan flujos de procesamiento de principio a fin personalizados para los productos y aplicaciones requeridos. Estos flujos son posteriormente usados para generar productos sobre áreas y periodos de tiempo significativos según lo requerido por los usuarios. En la etapa final, los flujos (por ejemplo, estabilidad/rendimiento y facilidad de uso) así como los productos resultantes son evaluados en un dialogo cercano con los usuarios.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Conclusión
El desarrollo de WOIS representa un ejemplo exitoso de desarrollo colaborativo impulsado por los usuarios, donde funcionalidades han sido diseñadas, desarrolladas y evaluadas a través de casos elegidos por lo usuarios con la intención de demostrar el impacto real del sistema para mejorar la gestión del agua y los planes de gestión integral de recursos hídricos. El WOIS ya ha sido implementado en las autoridades de algunas grandes cuencas de ríos africanos, varios ministerios y agencias africanos, así como en agencias humanitarias y de investigación. Por lo tanto continuará su desarrollo en respuesta a los requerimientos por parte de los usuarios de nuevas funcionalidades y mejoras funcionales y debido a la mejora en general, del software, los algoritmos y los métodos.

Una punto concreto en el que enfocarse será asegurar el soporte e implementación de capacidades de procesamiento para el nuevo sistema de satélites Sentinel mediante la integración de las herramientas de la ESA para Sentinel en WOIS y generando flujos de trabajo de producción dedicados. El próximo lanzamiento de WOIS (durante la segunda mitad de abril de 2015) ya incorporará las herramientas para Sentinel-1 y algunos flujos de trabajo que utilizaran los datos de este nuevo satélite radar para el monitoreo de inundaciones, el mapeo de cuerpos de agua, etc. Este convertirá a WOIS en un sistema de monitoreo completamente operacional. A través de la provisión de este sistema sin licencia, potente y extensible, y mediante esfuerzos continuados de  construcción de capacidades y capacitación, el proyecto intenta crear la base de una extensión, es decir, expandirse a otros países y regiones en África y más allá.
## Referencias
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Enlaces
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Autor
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
