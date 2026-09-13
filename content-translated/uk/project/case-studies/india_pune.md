---
HasBanner: false
archived: true
date: 2014-05-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/india_pune1.png
title: Використання консолі Python для підготовки оффлайн-карт з WMS (завантаження
  тайлів)
type: case-study

---
{{<content-start >}}
# Використання консолі Python для підготовки оффлайн-карт з WMS (завантаження тайлів)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2014</span>
</p>

Ця стаття розказує як підготувати карти WMS/WFS або будь-яку відкриту в QGIS карту для оффлайнового використання шляхом збереження тайлів за допомогою консолі Python. Сценарій також створює мозаїку тайлів для подільшого використання.

Сервіси WMS дедалі частіше використовуються для роботи з растровими та векторними даними. Серед їх переваг безпека, централізовані та гнучкі стилі. Прикладом таких сервісів є Google maps, Yahoo, Bing, MODIS, Landsat, карти NASA, NRSC (Індія). Недоліком/обмеженням WMS є необхідність підключення до інтернет. В деяких випадках, особливо під час польових робіт, підключення відсутнє. Також, у порівнянні з традиційними оффлайновими форматами (GeoTiff, JPS) WMS працює значно повільніше.
## Використання QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

<figure>
<img src="../images/india_pune1.png" class="align-left" alt="india_pune1.png" />
<figcaption>QGIS with WMS tiles</figcaption>
</figure>

## Python консоль
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. координати X, Y першого тайлу
2. бажаний розмір тайлів (наприклад, 0.001x0.001 градусів)
3. кількість тайлів, які необхідно завантажити (обчислюється з охоплення карти та розмірів тайлу)
4. каталог для запису тайлів

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

<figure>
<img src="../images/india_pune2.png" class="align-left" alt="india_pune2.png" />
<figcaption>Python script and directory where tiles are stored</figcaption>
</figure>

Недоліком методу є те, що зміні на сервері не будуть відображатися в режимі оффлайн. У цьому випадку користувач повинен згенерувати нову карту. Іншим недоліком є використання звичайного формату зображення, яке не може використовуватися для тематичного картографування бо класифікації. Хоча деякі карти землекористувань з певними зусиллями можна конвертувати у веторний формат із втратою частини даних.
## Область застосування
Отримана мозаїка є звичайним зображенням, навіть якщо вона була створена з тематичної карти (7-8 кольорів). За допомогою таких функцій як рекласифікація, об'єднання шарів/каналів цей растр можна перевести у векторний формат. WMS підтримує різні типи запитів, наприклад GetCapabilities, GetMap, GetFeatureInfo та ін. За допомогою запиту GetFeatureInfo можна отримати атрибутивну інформацію об'єктів. Цей сценарій також можна перетворити на плаґін, і таким чином для його використання додаткові знання не знадобляться.
## Підсумки
З вищенаписаного зрозуміло, що QGIS може використовуватися на просунутому рівні. За наявності базових навичок програмування можна створювати сценарії та плаґіни, які спрощують роботу. Можливість використовувати плаґіни, розроблені користувачами зі всього світу є однією з найкращих можливостей QGIS. Офіційна документація містить достатьньо інформації для розробки вкласних сценаріїв, а обробка растрових даних за допомогою GDALTools надзвичайно проста.
## Автори
Prashant Kadgi надіслав цю статтю у травні 2014 р. Він проживає в Пуне (Індія) та працює консультантом в GIS APP Consultancy Services. З 2009 він використовує ГІС та дані дистанційного зондування в NRM, лісному господарстві, електронному уряді та проектах з розробки програмного забезпечення у різних регіонах Індії та по всьому світу.
- Contact: <kadgiprashant@gmail.com>
- Сайт: www.gisappco.com (в розробці)

{{<content-end >}}
