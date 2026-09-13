---
draft: 'true'

---
# Створення карти стежки Фанді в QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

Стежку створили, підтримують та рекламують волонтери, відомі як Fundy Hiking Trail Association Inc. (FHTA, 1975). Як некомерційна організація FHTA забезпечує себе шляхом збору коштів та продаж путівників, що включають в себе карту стежки. В 2011 р. я запропонував FHTA свої послуги з оновлення офіційної карти стежки. Для мене, як добровольця, що створює карту для некомерційної організації, QGIS відповідає всім вимогам. Завдяки моїм зусиллям та зусиллям членів FHTA нову офіційна карта стежки Фанді було від початку до кінця створено в QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## Проект
Процес створення нової карти стежки Фанді в QGIS можна розбити на три частини:
- збір даних
- редагування та підготовка даних
- підготовка карти

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

В процесі підготовки карти використовувались наступні інструменти QGIS для вирішення різних задач:
- редагування зібраних даних за допомогою інструментів оцифровки
- Векторні шари, завантажені з сайтів NRCan та SNB були оброблені за допомогою плаґіна fTools
- Текстові файли, завантажені з сайту SNB були імпортовані в QGIS, за допомогою плаґіна інтерполяції створено карту висот, яка в свою чергу була використана для створення світло-тіньової відмивки та шару горизонталей засобами GDALTools.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Підсумки
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Посилання
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Автор
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Jarrett Totton надіслав цю статтю у січні 2013 р. Він працює ГІС-спеціалістом та проживає в Альберті, Канада.
