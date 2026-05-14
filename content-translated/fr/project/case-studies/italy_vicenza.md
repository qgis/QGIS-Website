---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Utilisation de QGIS pour la planification urbaine de la municipalité de Montecchio
  Maggiore, Vicenza, Italie.
type: case-study

---
{{<content-start >}}
# Utilisation de QGIS pour la planification urbaine de la municipalité de Montecchio Maggiore, Vicenza, Italie.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## La tâche
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

Un schéma clarifiera le processus:

Chaque bâtiment en construction a été retrouvé via une enquête et a été notifié sur papier. Une fois au bureau, les données sont saisies dans la base de données PotsgreSQL/PostGIS via un formulaire PHP en utilisant un navigateur web standard (Firefox, Iceweasel). Dans un second temps, l'emprise de chaque bâtiment a été dessinée avec QGIS et liée à la table d'enquête via un identifiant (d'une vue PostgreSQL/PostGIS). 

En parallèle, les facades des bâtiments ont été représentées en utilisant QCAD (LibreCAD).

Le PDR (piani di recupero) doit suivre des règles strictes sur sa représentation graphique:
- État actuel
- État du projet
- Utilisation prévue (actuellement)
- Utilisation prévue (projet)
- Type d'intervention autorisée

Pour chaque représentation, des cartes thématiques ont été produites en utilisant les attributs et les données récupérées lors de l'enquête (pour l'état actuel) et des données modifiées lors de l'étude et de la phase de design.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

Finalement, un rapport de sytnhèse de chaque batiment a été produit en utilisant la suite LibreOffice. Le rapport consiste en un résumé avec une photographie, un extrait de carte qui permet de localiser le batiment dans son contexte ainsi que son état actuel.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## Conclusion
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

Enfin, nous avons travaillé sur différentes plate-formes (Windows 7 64 bits, Windows XP 32 bits, Debian sur serveur et sur client) mais nous n'avons jamais rencontré de problèmes insurmontables.
## Auteur
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
