---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: Usando QGIS para cartografiar áreas calientes de biodiversidad y servicios
  ecosistémicos (HABEaS)
type: case-study

---
{{<content-start >}}
# Usando QGIS para cartografiar áreas calientes de biodiversidad y servicios ecosistémicos (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

El principal objetivo de esta plataforma es proveer libre acceso a una amplia variedad de datos sobre diversidad y servicios ecosistémicos para la cuenca mediterránea que estaban dispersos en un número diversos de entidades públicas y privadas. En la actualidad HABEaS WebGIS cubre la parte sur de Portugal, pero par finales de 2012 / inicio de 2013 se expandirá al norte de Portugal y al cantón de Tuzla en Bosnia & Herzegovina. A largo plazo queremos expandir esta herramienta a toda la cuenca mediterránea.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

La información geográfica contenida en HABEaS también ha sido utilizada por WWF para proporcionar apoyo para identificar bosques con alto valor de conservación (High Conservation Value Forests), HCVF por sus siglas en inglés, en el sur de Portugal, lo cual es un paso obligatorio para los propietarios de las tierra que quieran recibir certificación por parte del Forest Stewardship Council (FSC).

![](../images/portugal_lisbon3.jpg)

Para determinar qué valores de conservación ocurren en cada propiedad usamos el modelador de procesos de la caja de herramientas para crear un script que interseca todas las capas de HABEaS con los límites de la propiedad. Usando la misma herramienta también fuimos capaces de crear un script que automáticamente calcula la cantidad de carbono que está actualmente almacenada en la propiedad.

![](../images/portugal_lisbon4.jpg)
## Conclusiones
QGIS es fácil de utilizar y tiene capacidades  de geoprocesamiento muy potentes. La integración con GRASS GIS y SAGA GIS a través de la caja de herramientas de procesos nos permitió realizar un gran número de complejos análisis espaciales y modelarlos como procesos usando el modelador de procesos. Fue muy fácil producir mapas de alta calidad usando el diseñador de impresión y exportarlos a formato SVG para posterior edición con Inkscape que es un editor de gráficos vectoriales de código abierto.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Autor
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias es un estudiante de doctorado en el centro de ecología aplicada (Instituto Superior de Agronomia, Universidad Técnica de Lisboa)  y consultor para el Programa Mediterráneo del World Wide Fund of Naure (WWF).

{{<content-end >}}
