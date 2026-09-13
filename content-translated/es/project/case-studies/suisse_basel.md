---
HasBanner: false
archived: true
date: 2010-06-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/suisse_basel1.jpg
title: QGIS —— an interesting instrument for forestry planning concepts at local and
  regional level
type: case-study

---
{{<content-start >}}
# QGIS —— an interesting instrument for forestry planning concepts at local and regional level
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>June 01, 2010</span>
</p>

Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Como se utilizó QGIS
Dentro del proceso completo de planificación se usó QGIS para las siguientes cuatro tareas:
- Importación de datos existentes. Los datos incluyen mapas de fondo geo-referenciados (\*.tif) junto con archivos de formas poligonales, líneales y puntuales. Para el administrador forestal, la visualización de los datos temáticos existentes (por ejemplo, recursos de agua subterránea y potable, zonas de protección de la naturaleza) son importantes para su trabajo diario.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Análisis. Se calcularon las áreas de las diferentes categorías de medición. A partir de ciertas características lineales, como vías de tren o carreteras, la protección de los bosques correspondientes se determinó con la ayuda de un buffer.
- Imprimir y exportar. El compositor de impresión respaldó la creación del diseño del mapa. El mapa se exportó como PDF y archivos de imagen.

<figure>
<img src="../images/suisse_basel1.jpg" class="align-right" alt="suisse_basel1.jpg" />
<figcaption>Extract of the forestry measurements map</figcaption>
</figure>

## Conclusión
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Perspectiva
Las tareas centrales de una planificación forestal conceptual pueden resolverse con las herramientas SIG básicas mencionadas. Guaraci continuará usando QGIS para la planificación forestal a nivel del propietario del bosque. En base a las experiencias con el proyecto presentado, QGIS también se puede recomendar para conceptos forestales a nivel de las autoridades locales. Los proyectos más grandes y complejos con requisitos de análisis detallados podrían manejarse mediante la combinación de QGIS con el servidor de base de datos espacial Postgis. Se pueden digitalizar fácilmente nuevas zonas de tala, así como reservas forestales y zonas de protección. Con suerte, los propietarios y administradores forestales utilizarán cada vez más el potencial de QGIS también para su planificación anual, así como la documentación de sus actividades forestales.
## Autor
<figure>
<img src="../images/suisse_baselaut.jpg" class="align-left" height="200" alt="suisse_baselaut.jpg" />
<figcaption>Raphael Häner</figcaption>
</figure>

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.

{{<content-end >}}
