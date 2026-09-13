---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: proje
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Using QGIS for urban planning in the municipality of Montecchio Maggiore, Vicenza,
  Italy
type: case-study

---
{{<content-start >}}
# Using QGIS for urban planning in the municipality of Montecchio Maggiore, Vicenza, Italy
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## Görev
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

Bir şema iş akışını açıklığa kavuşacaktır:

Her bina verisi anket yoluyla alınır ve kağıt programına yazılır. İlk önce, ofiste verilerin kurallı bir web tarayıcısı kullanarak PHP formu aracılığıyla PostgreSQL / PostGIS veritabanına  girişi yapılır. (Firefox, Iceweasel). İkinci olarak, her binanın şekli QGIS ile çiziliir ve id anahtarı ile anket tablosuna bağlanır (PostgreSQL / PostGIS görünümü).

Aynı zamanda bina cepheleri QCAD (LibreCAD) kullanılarak dizayn edilmiştir.

PDR (piani di recupero) belirli grafikleri gerektiren sıkı kurallara uymalıdır:
- Mevcut durum
- Proje durumu
- Kullanım amacı (mevcut)
- Kullanım amacı (proje)
- Müdahale tipi başvurdu

For every graphic thematic maps were produced using the attribute and data retrieve during the survey (for the present state) and data modified during the study and design fase.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

Sonunda her bina için bir sentez raporu LibreOffice paketi kullanılarak üretilmiştir. Rapor, fotoğraf, harita, bina lokasyon verilerinin mevcut durumunun  özetini içerir.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## Sonuç
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

And last but not least: we worked on different platform (Windows 7 64 bit, Windows xp 32 bit, Debian server and Debian client) but we never encountered insurmountable problems.
## Yazar
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
