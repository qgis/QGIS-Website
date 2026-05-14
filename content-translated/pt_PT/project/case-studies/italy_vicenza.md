---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Usar o QGIS para o planeamento urbanístico no município de Montecchio Maggiore,
  Vicenza, Itália.
type: case-study

---
{{<content-start >}}
# Usar o QGIS para o planeamento urbanístico no município de Montecchio Maggiore, Vicenza, Itália.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## A tarefa
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

O esquema irá clarificar o fluxo de trabalho:

Toda a informação dos edifícios foi recuperado através de levantamento e escrita numa agenda. Uma vez no escritório, os dados foram introduzidos para a base de dados Postgresql/Postgis através uma um formulário PHP usando um navegador de internet (Firefox e também o Iceweasel). Num segundo momento a shapefile de cada edifício foi desenhada com o QGIS e ligada à tabela de levantamento através da chave de campo id (vista PostgreSQL/Postgis) 

Ao mesmo tempo as fachadas dos edifícios foram projetadas usando o QCAD (LibreCAD).

O PDR (plano de recuperação) deve seguir regras restritas para adquirir gráficos específicos:
- Estado atual
- Estado do Projeto
- utilização pretendida (presente)
- utilização pretendida (projeto)
- Tipo de intervenção admitida

Para cada mapa gráfico temático nós produzimos usando o atributo e data de recolha durante o levantamento (para o presente estado) e a data modificada durante o estudo na fase de design.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

Finalmente um relatório sintetizado para cada edifício foi produzido usando a ferramenta de produtividade LibreOffice. O relatório consiste no sumário da tarefa com fotografia, extrato da cartografia que está localizada no edifício em concurso e a data do seu atual estado.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## Conclusões
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

Por último mas não menos importante: nós trabalhamos em diferentes plataformas (Windows 7 de 64 bits, o Windows XP de 32 bits, o servidor Debian e cliente Debian), mas nunca encontrámos problemas intransponíveis.
## Sobre o autor:
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
