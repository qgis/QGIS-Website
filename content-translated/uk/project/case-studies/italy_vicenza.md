---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/italy_vicenza1.png
title: Використання QGIS для міського планування у муніципалітеті Монтеккьо-Маджоре,
  Віченца, Італія
type: case-study

---
{{<content-start >}}
# Використання QGIS для міського планування у муніципалітеті Монтеккьо-Маджоре, Віченца, Італія
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## Задача
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

Процес роботи показано на схемі:

Кожна будівля обстежується та на паперові носії збирається всі необхідна інформація. В офісі вся інформація вноситься у базу даних PostgreSQL/PostGIS через форму на PHP за допомогою звичайного браузера (Firefox, Iceweasel тощо). Також для кожної споруди в QGIS створюється відповідний об'єкт та зв'язується з таблицею через ключове поле.

Одночасно в QCAD (LibreCAD) створюються моделі фасадів будівель.

PDR (piani di recupero) повинен відповідати певним вимогам, для чого потрібні різні дані:
- поточний стан
- запланований стан
- використання за призначенням (поточний стан)
- використання за призначенням (заплановане)
- Тип втручання

Для кожного зображення створюються тематичні карти з використанням атрибутів та даних польових обстежень (для поточного стану) та даних, отриманих на етапі дослідження та проектування.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

Нарешті, за допомогою пакету LibreOffice створюється зведений звіт по кожній будівлі. Звіт складається з основних відомостей з фотографією, фрагмент карти з будівлею та поточними даними.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## Підсумки
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

І нарешті: ми працювали на різних платформах (Windows 7 64bi), Windows XP 32 bit, сервер та клієнт Debian) і не мали жодних проблем.
## Автор
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
