---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/italy_vicenza1.png
title: استخدام QGIS للتخطيط الحضري في بلدية مونتيشيو ماجيوري ، فيتشنزا ، إيطاليا
type: case-study

---
{{<content-start >}}
# استخدام QGIS للتخطيط الحضري في بلدية مونتيشيو ماجيوري ، فيتشنزا ، إيطاليا
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## المهمة
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

سيوضح المخطط سير العمل:

تم استرجاع كل بيانات المبنى من خلال المسح وكتبت في جدول ورقي. وبمجرد وصوله إلى المكتب ، تم إدخال البيانات في قاعدة بيانات Postgresql / Postgis عبر نموذج PHP باستخدام متصفح الويب الكنسي (Firefox ، Iceweasel أيضًا). في لحظة ثانية ، تم رسم شكل كل مبنى باستخدام QGIS وربطه بجدول المسح عبر حقل معرف المفتاح (PostgreSQL / Postgis view).

في نفس الوقت تم تصميم واجهات المباني باستخدام QCAD (LibreCAD).

يجب أن يتبع (PDR (piani di recuper قواعد صارمة تتطلب رسومًا محددة:
- الحالة الحالية
- حالة المشروع
- الاستخدام المقصود (الحاضر)
- الاستخدام المقصود (مشروع)
- نوع التدخل المقبولة

لكل خرائط موضوعية رسومية تم إنتاجها باستخدام السمة واسترجاع البيانات أثناء المسح (للحالة الحالية) والبيانات المعدلة خلال تصميم الدراسة والمزهرية.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

وأخيرا تم إنتاج تقرير توليفي عن كل مبنى باستخدام جناح libreoffice. يتكون التقرير من جدول زمني يلخص الصورة ، مستخرج رسم الخرائط الذي يحدّد المبنى في المسابقة وبيانات الحالة الحالية.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## الخاتمة
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

وأخيرًا وليس آخرًا: لقد عملنا على نظام أساسي مختلف (Windows 7 64 بت و Windows xp 32 bit و Debian server و Debian client) ولكننا لم نواجه مشكلات مستعصية على الإطلاق.
## المؤلف
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
