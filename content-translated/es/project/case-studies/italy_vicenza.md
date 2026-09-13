---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Usando QGIS para planificación urbana en la municipalidad de Montecchio Maggiore,
  Vicenza, Italia
type: case-study

---
{{<content-start >}}
# Usando QGIS para planificación urbana en la municipalidad de Montecchio Maggiore, Vicenza, Italia
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## La tarea
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

Un esquema aclarará el flujo de trabajo:

Todos los datos del edificio se recopilaron a través de estudios y se escribieron en un cronograma en papel. Una vez en la oficina, los datos se introdujeron en la base de datos Postgresql / Postgis con un formulario PHP utilizando un navegador web canónico (Firefox y también Iceweasel). En segundo lugar, la forma de cada edificio se dibujó con QGIS y se vinculó a la tabla de estudios a través del campo de clave de identificación (vista PostgreSQL / Postgis).

Al mismo tiempo, las fachadas de los edificios fueron diseñados utilizando QCAD (CAD Libre).

El PDR (piani di recupero) debe seguir unas reglas estrictas que requieren gráficos específicos:
- Estado actual
- Estado del proyecto
- Uso previsto (actual)
- Uso previsto (proyecto)
- Tipo de intervención admitida

Cada mapa temático gráfico se produjo utilizando los atributos y datos recuperados durante el estudio (para el estado actual) y los datos modificados durante el estudio y la fase de diseño.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

Finálmente, se creó un informe de síntesis para cada edificio utilizando la suite Libreoffice. El informe es una lista resumida con foto, extracto cartográfico que ubica el edificio en el contexto y los datos del estado actual.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## Conclusión
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

Y para finalizar: trabajamos en diferentes plataformas (Windows 7 64 bit, Windows XP 32 bit, servidor Debian y cliente Debian) aunque nunca encontramos problemas que no puedan resolverse.
## Autor
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
