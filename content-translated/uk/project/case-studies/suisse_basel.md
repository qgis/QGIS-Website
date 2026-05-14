---
HasBanner: false
archived: true
date: 2010-06-01
draft: false
featured: false
section: проект
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
## Як використовується QGIS
В процесі планування QGIS використовувалась для наступних чотирьох задач:
- Імпорт наявних даних. Ці дані складаються з прив'язаних растрових карт (:file:`*.tif`) та полігональних, лінійних і точкових shape-файлів. Візуалізація тематичних даних (наприклад, джерел питної та технічної води, захисних зон) є важливою складовою повсякденної роботи управляючого лісом.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Аналіз. Необхідно розрахувати площу різних категорій лісу. Вздовж лінійних об'єктів, таких як залізниця або дороги, визначаються відповідні захисні зони шляхом побудови буфера.
- Друк та експорт. Редактор макетів допомагає створювати друковані карти. Карти експортуються у формат PDF та графічні файли.

<figure>
<img src="../images/suisse_basel1.jpg" class="align-right" alt="suisse_basel1.jpg" />
<figcaption>Extract of the forestry measurements map</figcaption>
</figure>

## Підсумки
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Перспективи
Основні задачі планування лісного господарства можуть бути вирішені за допомогою базових інструментів QGIS. Guaraci буде і надалі використовувати QGIS для планування лісного господарства на рівні власників лісу. На основі досвіду описаного проекту QGIS також можна рекомендувати для використання на рівні органів влади. Більш об'ємні та складні проекти з детальним аналізом вимог можуть бути виконані з використанням QGIS та просторової бази даних PostGIS. Дуже легко оцифровувати нові зони лісозаготівлі, резерви та захисні зони. Сподіваємось, власники лісів та управляючі будуть частіше використовувати QGIS для щорічного планування та документування своєї активності.
## Автор
<figure>
<img src="../images/suisse_baselaut.jpg" class="align-left" height="200" alt="suisse_baselaut.jpg" />
<figcaption>Raphael Häner</figcaption>
</figure>

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.

{{<content-end >}}
