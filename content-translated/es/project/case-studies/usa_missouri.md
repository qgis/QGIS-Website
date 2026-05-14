---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/usa_missouri1.png
title: QGIS Mapea Registros Históricos de Herpetofauna (en Missouri, EE.UU.)
type: case-study

---
{{<content-start >}}
# QGIS Mapea Registros Históricos de Herpetofauna (en Missouri, EE.UU.)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Generar y Exportar Mapas Estáticos
El proceso de creación de mapas con QGIS comienza con los datos almacenados en varias tablas de PostgreSQL, habilitados espacialmente con PostGIS. Debido a que los mapas son estáticos y, en última instancia, están destinados a la web o a un atlas impreso, se generan automáticamente para cada especie utilizando un complemento personalizado en Python de QGIS(Figuras 1,2).

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

## Conclusiones
Al comienzo del proyecto MOHAP, se utilizaron varias herramientas comerciales y propias para almacenar, procesar datos y producir mapas para su publicación. A partir de 2007, nos propusimos trasladar todos los aspectos del proyecto al software de código abierto. QGIS, junto con PHP, PostgreSQL, PostGIS, Python y ReportLab, forma el eje de código abierto para MOHAP, lo que permite que el proyecto y todos los datos coexistan sin enredos de software privativo.

QGIS contiene soporte nativo para PostGIS y una arquitectura de complementos de Python, que fueron esenciales para crear la generación y exportación de mapas automatizados. Se utilizó la extensa documentación de la API junto con el libro de cocina del desarrollador de complementos para crear exactamente lo que necesitábamos para la automatización. El soporte de la comunidad también es muy bueno e incluye una gran variedad de complementos compartidos creados y listos para usar.

Aunque usamos QGIS de un modo breve y específico, sus capacidades y extensibilidad con Python son más que suficientes para abordar proyectos más grandes y complejos.
## Autor
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
