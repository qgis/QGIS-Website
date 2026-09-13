---
author: Radoslaw Guzinski
categories:
- Case studies
date: '2015-04-01'
description: Enabling the Use of Earth Observation Data for Integrated Water Resource
  Management in Africa
draft: 'true'
heroImage: ''
tags:
- water
- case-study
- showcase
thumbnail: wois.png
title: Water Observation and Information System
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Опис системи
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Основною перевагою Processing є можливість прозорого використання алгоритмів з різних джерел. Завдяки цьому можна створювати моделі та об'єднувати їх у покрокові майстри обробки, що й було зроблено в межаж проекту TIGER-NET шляхом створення плагінів. Цей функціонал було використано для створення бібліотеки стандартизованих процесів (з інструкціями) для проведення складних видів аналізу ДДЗ з метою управління водними ресурсами.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

Операційне та практичне застосування WOIS для підтримки інтегрованого управління водними ресурсами в Африці було продемонстроване у різних ситуаціях з використанням різних наборів даних та продутів на їх основі. Включаючи: якість води в озерах, моніторинг паводків, деградація земель та характеризація земельного покрову, картографування водних об'єктів та гідрологічне моделювання. Демонстрація проводилась в декілька етапів. Спочатку розроблялися робочі процеси для наявних даних. Ці процеси використовувалися для виявлення значущих областей та періодів. На фінальному етапі робочі процеси (а саме їх стабільність/швидкість роботи, простота використання тощо) оговорювались з кінцевими користувачами

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## Підсумки
Розробка WOIS є прикладом спільної розробки, яка управляється користувачами, коли необхідний функціонал проектується, розробляється та перевіряється на основі наданих користувачами даних, щоб продемонструвати реальний вплив системи управління водними ресурсами. WOIS вже впроваджено на всіх основних річкових басейнах Африки та в деяких міністерствах і агенціях, а також в дослідницьких та гуманітарних організаціях. Тому система буду продовжувати розвиватися і відповідь на запити користувачів.

Основний акцент буде зроблено на підтримку нових супутників Sentinel, шляхом інтеграції Sentinel Toolbox у WOIS та розробку спеціалізованих процесів аналізу. Наступний випуск WOIS (у першій половині квітня 2015 р.) буде підтримувати Sentinel-1 Toolbox та надавати ряд алгоритмів для обробки даних цієї нової радарної системи для моніторингу паводків, картографування водних об'єктів тощо. Таким чином WOIS перетвориться на повноцінну систему моніторингу. Завдяки використанню вільної ліцензії, потужної та модульної системи та наявності шляхів подальшого розвитку, проект має потенціал для розширення, наприклад, запровадження в інших країнах та регіонах Африки, а також за її межами.
## Посилання
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Посилання
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Автор
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
