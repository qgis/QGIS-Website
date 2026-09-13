---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS для моніторингу тигрів (з використанням фото-пасток в тигровому заповіднику
  Намері, Ассам, Індія, округ Сонітпур)
type: case-study

---
{{<content-start >}}
# QGIS для моніторингу тигрів (з використанням фото-пасток в тигровому заповіднику Намері, Ассам, Індія, округ Сонітпур)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

На цій території зустрічаються такі види, що мають природоохоронне значення, яе королівський бенгальський тигр, індійський слон, індійський бізон; часто зустрічаються леопард, димчастий леопард, дика собака, індійський замбар, індійський мутнжак, свинячий олень, кабан та деякі інші види. Різноманітність пташиного світу NTR вражає, тут налічується близько 370 видів птахів. Заповідником керує лісовий департамент уряду Ассаму.
## Використання QGIS для підготовки досліджень за допомогою фото-пасток
З 2011 р. національна рада зі збереження тигрів Індії (National Tiger Conservation Authority, NTCA) зобов'язала всі тигрові заповідники проводити моніторинг тигрів з використанням фото-пасток. Згідного нових вказівок на кожні 100 кв. км. тигрового заповідника необхідно 25 пар камер, а інтервал збору даних становить 40-60 днів. Для успішного виконання нових інструкцій необхідно використовувати ГІС.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

У 2012 - 2013 роках ми реалізували новий протокол моніторингу тигрів у NTR за допомогою QGIS. Спочатку ми провели оцифровку кордонів NTR. Цей полігон потім було експортовано у GPS для навігації під час польових обстежень. Також було проведено польове обстеження території заповідника з метою виявлення таких ознак присутності тигрів як сліди, подряпини та екскременти. Координати виявлених ознак а також потенційні місця розміщення фото-пасток записувалися для подальшого аналізу. Після завершення польового етапу всі дані було завантажено в QGIS за допомогою плаґіна «Інструменти GPS» для подальшої обробки та визначення розташування фото-пасток. Також були підготовані shape-файли з координатами ознак наявності тигрів та потенційних місць розміщення пасток.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## Підсумки
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## Автор
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Rajendra G. Garawad надіслав цю статтю у березні 2013 р. Він є директором тигрового заповідника Намері, Ассам, Індія. Має магістерські ступені в області лісного господарства та охорони природи, а також управління земельними ресурсами.

{{<content-end >}}
