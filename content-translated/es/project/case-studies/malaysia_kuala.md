---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/malaysia_kuala1.png
title: QGIS en el Departamento Federal de Planificación de Ciudad y Campo, Malasia
  Peninsular
type: case-study

---
{{<content-start >}}
# QGIS en el Departamento Federal de Planificación de Ciudad y Campo, Malasia Peninsular
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

## Introducción
El Departamento Federal de Planificación Urbana y Rural, Malasia Peninsular (JPBD) es una agencia federal que asesora asuntos sobre planificación urbana y rural. Sin embargo, el alcance de la administración del departamento se limita a Malasia peninsular ya que Sabah y Sarawak en Malasia oriental tienen sus respectivas agencias de planificación urbana. La planificación de la ciudad y el país está en la lista concurrente en la Legislación Federal, por lo tanto, a nivel federal, JPBD asesora al Ministro de Vivienda y Gobierno Local del cual JPBD obtiene su patrocinio, así como asesora al Consejo Nacional de Planificación Física presidido por el Primer Ministro . A nivel estatal, el director estatal asesora al Comité de Planificación del Estado presidido por el Primer Ministro. A nivel local, JPBD asesora a las autoridades locales de planificación sobre cuestiones de planificación al participar en la preparación de planes de desarrollo obligatorios. En la Sede, la División del Plan Físico Nacional prepara el Plan Físico Nacional, mientras que cuatro oficinas regionales de proyectos ayudan en la preparación de los Planes de Estructura Estatal, Planes de Distrito Local y Planes de Área Especial. Como las agencias públicas se establecieron tradicionalmente en base a su especialización, el JPBD es el custodio de la información sobre el uso del suelo.
## El Proyecto
QGIS fue presentado por primera vez a la comunidad de código abierto de Malasia como una alternativa viable a SIG con licencia para agencias públicas por JPBD en la Conferencia de código abierto del gobierno de Malasia (MyGOSSCON) en 2009 y a la comunidad de SIG de Malasia en la 4ta Conferencia y Exposición Nacional de SIG (NGIS ) en 2010. JPBD ha sido tradicionalmente un usuario de SIG patentado, por lo tanto, la introducción de QGIS fue una verdadera revelación, no solo desde el punto de vista del software de código abierto (OSS), además, SIG OSS. La filosofía de código abierto era diferente, por lo que QGIS se sentía extraño, inseguro y arriesgado, no es sorprendente que la idea de usar QGIS no recibiera mucho apoyo interno, de hecho, se enfrentó a la resistencia desde la alta gerencia hasta el grupo de apoyo en 2010.

<figure>
<img src="../images/malaysia_kuala1.png" class="align-right" alt="malaysia_kuala1.png" />
<figcaption>MyGOSSCON, 2009</figcaption>
</figure>

On the opposite side, request for technical talks on QGIS came from other technical agencies which JPBD gave to the Ministry of Works and the Department of Irrigation and Drainage. Other works to promote QGIS from JPBD came in the form of newsletter articles on QGIS to the Open Source Competency Centre (OSCC) at the Prime Minister\'s Department and articles introducing QGIS to the Survey Department\'s GIS Bulletin and the Ministry of Natural Resource\'s Public Sector GeoSpatial Bulletin. In the meantime, JPBD researched on developing a slope analysis module for QGIS\'s Windows and Ubuntu version.

El estudio destacó los pros y los contras de personalizar un módulo y el alto nivel de compromiso de la administración necesario para garantizar su continuado éxito y adopción. En 2011, el JPBD comenzó a fomentar QGIS más como una herramienta analítica en lugar de una herramienta de mapeo para ser pionero en módulos inexplotados o nuevos enfoques para explotar QGIS.

El departamento finalmente promovió el paquete QGIS-GRASS en lugar de simplemente QGIS, ya que lo consideró más poderoso y útil para fines de planificación urbana, como la limpieza de errores de topología y la superación de las limitaciones con entradas estándar predeterminadas. Eso fue simplemente el comienzo.

<figure>
<img src="../images/malaysia_kuala2.png" class="align-right" alt="malaysia_kuala2.png" />
<figcaption>Northern Project Office get QGIS training</figcaption>
</figure>

In order to centralize and share findings in the use of QGIS for town planning purpose which could also be use in other fields dealing with spatial analysis, an unofficial blog established by the author called "QGIS MALAYSIA" at <http://www.qgismalaysia.blogspot.com> was made to generate a QGIS community in Malaysia. External agencies seem to have more interest in QGIS than JPBD itself and upon their request, JPBD gave QGIS training to the Fire and Safety Department as well as to the Ministry of Education whom later was convinced QGIS will be their de facto GIS tool.

Hearing this, JPBD\'s Research and Development Division took the initiative and requested for QGIS training and subsequently 12 persons were trained. Word of mouth (a godsend thing, though at times, extremely detrimental) spread that QGIS was indeed user-friendly, easy to use and at par with proprietary GIS in mapping task and could take on proprietary GIS when optimized with GRASS modules.

El interés en QGIS aumentó y, en 2012, con el apoyo de todos los directores de la oficina del proyecto, la División Nacional de Información sobre el Uso del Suelo emprendió un esfuerzo máximo que encabezó QGIS para formar a las 4 oficinas del proyecto, ya que tienen el mayor número de usuarios de SIG. A finales de 2012, se anticipa que al menos 320 empleados en todo el JPBD utilizarán QGIS, que representa aproximadamente el 90% de los usuarios de SIG en el departamento.

That is not all. States town planning departments have also requested QGIS training such as Perak including strong interest from poorer states like Perlis and Kelantan. If this catches on, it is anticipated that the use of QGIS may dominate states planning departments and even extend to local planning authorities, many of which are not wealthy. In the meantime, JPBD is seriously studying the use of the QGIS-PosgreSQL-PostGIS package for every planning office\'s client GIS-geodatabase server structure to serve as the foundation of JPBD\'s integrated landuse (iPLAN) network.
## Resultado de usar QGIS
- Suponiendo RM10,000 por la propiedad de licencia SIG, el uso de QGIS en 320 instalaciones ayudará a ahorrar RM3,200,000 al gobierno federal;
- Una erradicación total de los SIG piratas y el aumento de la confianza en el uso de OSS en general y específicamente SIG de OSS;
- El curso de QGIS ha sido más fácil de administrar. Esto significa que el aprendizaje cruzado entre personal, divisiones, las agencias públicas e incluso las autoridades locales de planificación que usan QGIS puede ser más efectivo porque el GIS utilizado es uniforme;
- El uso de QGIS ayuda a lograr la sinergia con una geodatabase PostgreSQL-PostGIS que el departamento planea usar como base de la geodatabase de uso del suelo en toda la Península de Malasia.
- Ha sido más rápido procesar verificación de datos y limpiar errores topológicos.
- Los usuarios se vuelven más valientes y comienzan a aventurarse en Google Maps y otras fuentes de información secundaria en internet;
- La facilidad de uso de QGIS alienta a los usuarios a ser más aventureros y explorar los muchos complementos disponibles para su beneficio y facilitar su tarea.
- SIG una herramienta compleja se convierte en amigo antes que un estorbo.

## Autor
<figure>
<img src="../images/malaysia_kualaaut.jpg" class="align-left" height="200" alt="malaysia_kualaaut.jpg" />
<figcaption>Abbas Abdul Wahab</figcaption>
</figure>

This article was contributed in January 2012 by Abbas Abdul Wahab. Abbas graduated as a town planner from Gloucestershire College of Arts & Design, United Kingdom in 1980 and has a Masters of Science in GIS & Geomatic Engineering from Putra University Malaysia in 2002. He is currently the Head of the National Landuse Information Unit at the National Landuse Information Division of the Federal Department of Town & Country Planning, Peninsular Malaysia.

{{<content-end >}}
