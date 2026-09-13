---
HasBanner: false
archived: true
date: 2011-12-31
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/nigeria_jos1.jpg
title: Картографування місцевості та орнітофауни в заповіднику Amurum у Нігерії
type: case-study

---
{{<content-start >}}
# Картографування місцевості та орнітофауни в заповіднику Amurum у Нігерії
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>December 31, 2011</span>
</p>

Лісовий заповідник Amurum знаходиться неподалік від міста Джос, штат Плато, Нігерія. Його було створено за поданням A.P. Leventis Ornithological Research Institute (APLORI) для задач збереження природи,навчання та наукових досліджень. APLORI створено на кафедрі зоології університету м. Джос. Щорічно група мотивованих студентів з усієї Нігерії проходить там навчання з природоохоронної біології, статистики (з використанням R), а з 2011 р. і з ГІС. Протягом двох тижнів 2011 р. ми вивчали базові поняття ГІС та вчились застосовувати ці знання для вирішення різних природоохоронних задач у QGIS. У цій статті ми опишемо як саме ми використовували QGIS для картографування території заповідника та як ці карти використовувались для визначення просторового розподілу орнітофауни та біорізноманіття.

<figure>
<img src="../images/nigeria_jos1.jpg" class="align-right" alt="nigeria_jos1.jpg" />
<figcaption>Training Group</figcaption>
</figure>

## Картографування висот та ареалів
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) За допомогою GDALTools ми об'єднали тайли, а потім обрізали растр по межі заповідника, і таким чином отримали відносно невеликий шар. За допомогою GPS було зібрано дані про висоту різних точок заповідника.
3) Загалом, дані SRTM узгоджуються з даними GPS. За допомогою GDALTools були розраховані тіньова відмивка та крутизна схилів. Ці величини є важливими, оскільки вони пов'язані з типом ареалу.

<figure>
<img src="../images/nigeria_jos2.jpg" class="align-right" alt="nigeria_jos2.jpg" />
<figcaption>QGIS screenshot</figcaption>
</figure>

4) Так як ми хотіли створити високоякісну карту, ми інтерполювали вихідну (обрізану) карту висот. Для цього ми використовували інструмент warp з набору GDALTools. А за допомогою інструменту contours ми отримали горизонталі.
5) Координати меж заповідника було отримано за допомогою GPS. Маршрутні точки та треки були завантажені з GPS за допомогою плаґіна «Інструменти GPS». З них ми створили полігональний shape-файл. Так само було отримано дороги на території заповідника.
6) Ми швидко створили карту ареалів заповідника, використовуючи в якості основи супутниковий знімок Google, який був завантажений у проект за допомогою плаґіна OpenLayers. У заповіднику можна виділити три ареали: савани, галерейний ліс та скельна порода. З супутникового знімку були оцифровані межі цих трьох ареалів. Правильне налаштування прилипання дозволило уникнути топологічних помилок.

## Розповсюдження птахів та різноманітність
На основі карти ареалів було згенеровано випадкові точки. Число точок у кожному ареалі залежало від його площі.

<figure>
<img src="../images/nigeria_jos3.jpg" class="align-right" alt="nigeria_jos3.jpg" />
<figcaption>Training Group</figcaption>
</figure>

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Підсумки
Overall, the course was a great success. We - a group of students with no previous GIS experience —— enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

<figure>
<img src="../images/nigeria_jos4.png" class="align-right" alt="nigeria_jos4.png" />
<figcaption>QGIS map: Diversity of Amurum Forest Reserve</figcaption>
</figure>

## Автори
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill

{{<content-end >}}
