---
draft: 'true'

---
# QGIS та GRASS у картографуванні лісових пожеж
## Вступ
Регіональна рада Південного Даунс (Southern Downs Regional Council, SDRC) є невеликим органом місцевого самоврядування на південному сході Квінсленда, Австралія. Територія регіону, в основному південна її частина, страждає від великих лісових пожеж. Лісові пожежі це реальна та постійна загроза для жителів та землевласників Південного Даунсу, яка призводить до загибелі людей та втрати майна.

Цей проект дозволить раді та жителям регіону отримувати інформацію про ризики та приймати правильні рішення в майбутньому.

![](./images/australia_queens1.jpg){.align-right}
## Проект
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

Робота з QGIS в межах проекту складалась з 6 основних етапів
- оцінка крутизни схилів та її картографування
- оцінка експозиції схилів та її картографування
- оцінка стану рослинного покрову та його картографування
- розрахунок балів, що визначають величину небезпеки
- польова перевірка та якісна оцінка
- Кінцеві карти

## Використання QGIS та GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

Плаґін GRASS QGIS використовувався для імпорту 5 м горизонталей на весь регіон, які потім було зконвертовано у растрову карту за допомогою ``r.surf.contour``. Експозиція та крутизна схилів були розраховані з растрової карти модулем ``r.slope.aspect``. Значення експозиції та крутизни було розділено на діапазони, яким потім ставили у відповідність бали ризику. Насадження також отримували свою оцінку. Наприкінці всі карти було зведено за допомогою растрового калькулятора у фінальну карту. Бали ризику було розбито на три категорії: високий, середній та низький.

На фінальній стадії процесу проводилась польова перевірка силами сільських пожежних служб. Після процесу перевірки за допомогою QGIS було надруковано фінальні карти.

Оскільки всі алгоритми GRASS можуть виконуватися з командного рядка команди, необхідні для створення карти ризиків були записані з метою документування на випадок, якщо з'явиться необхідність створити нові карти в майбутньому.
## Підсумки
Загалом QGIS разом з плаґіном GRASS проявили себе дуже добре та дозволили отримати гарний результат у картографуванні лісових пожеж. Плаґін GRASS надає дуже простий інтерфейс до GRASS через QGIS. А оскільки QGIS здатна відкривати растровий формат GRASS напряму, інтеграція знаходиться на високому рівні та створювати карти дуже просто.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Посилання
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Автор
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

Nathan Woodrow надіслав цю статтю у січні 2011 р. Він є ГІС-спеціалістом регіональної ради Південного Даунса та отримує ступінь з просторових наук в університеті Південного Квінсленду.
