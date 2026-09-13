---
HasBanner: false
archived: false
date: 2015-01-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/portugal_pinhel1.jpg
title: QGIS та картографування ризиків пожеж у Португалії
type: case-study

---
{{<content-start >}}
# QGIS та картографування ризиків пожеж у Португалії
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2015</span>
</p>

Португалія страждає від лісових пожеж, які завдають значних втрат, не тільки екологічних, але й соціальних та економічних. Щоб впоратися з цим португальський уряд через Національну Лісову Адміністрацію (National Forest Authority, AFN) декілька років тому вирішив створити спеціальні технічні відділи у місцевих адміністраціях, які серед інших завдань, повинні готувати муніципальні плани з ліквідації лісових пожеж та оперативного реагування.

In order to support the elaboration of these documents, the AFN provided technical guides with a methodology for calculating and mapping the Forest Fire Hazard and Risk. Moreover, tutorials have been offered to follow this methodology, using Proprietary Software. However, the acquisition and licensing costs of that software are unaffordable for most of the smaller local administrations and so, it was decided to create and make available a guide with a methodology for developing Hazard and Risk cartography using only Free and Open Source Software \[<http://goo.gl/TSv2E>\].

Було запропоновано використовувати наступні програми: QGIS, GRASS GIS, gvSIG та бібліотеки GDAL/OGR. Цей посібник описує всі необхідні види аналізу, потрібні для підготовки планів захисту лісів та оперативного реагування відповідно до методики AFN. Більшість задач вирішується в QGIS, за просторовий аналіз растрових даних відповідає GRASS. gvSIG та його додаток Network Analysis використовуються для мережевого аналізу, а бібліотеки GDAL/OGR --- для перепроектування даних з однієї системи координат в іншу.

Після інтенсивного тестування та трирічного використання цієї методології для підготовки оперативних планів у муніципалітеті Піньел, можна сказати, що запропоновані альтернативи не тільки є повноцінною заміною але й мають певні переваги над власницьким програмним забезпеченням, яке зазвичай використовується для вирішення цієї задачі. Перевірка результатів показує, що не зважаючи на відносну простоту моделі, її здатність прогнозування знаходиться на досить високому рівні, а використання вільного програмного забезпечення не зменшує точність результатів, а навпаки підвищує.
> ![](../images/portugal_pinhel1.jpg)

<figure>
<img src="../images/portugal_pinhel2.jpg" class="align-right" alt="portugal_pinhel2.jpg" />
<figcaption>Forest Fire Hazard and Risk Maps of Pinhel, implemented with Open Source Software.</figcaption>
</figure>

На другому етапі ми спробували прискорити процес з використанням моделей, щоб розробити процес, який буде складатися з різних задач та не потребувати взаємодії з користувачем. Цей етап полягав в основному в автоматизації процедури, описаної у посібнику. Автоматизація означає зменшення кількості часу, необхідного фахівцям для виконання аналізу та підготовки річних планів захисту лісів, з годин інтенсивної роботи до лічених хвилин. При цьому втручання людини зводиться до вибору вхідних даних та розміщення результатів.

<figure>
<img src="../images/portugal_pinhel3.png" class="align-right" alt="portugal_pinhel3.png" />
<figcaption>Interface of the Sextante Model to calculate the Probability of the Forest Fire Hazard.</figcaption>
</figure>

In furtherance of this second phase, we used the Python version of Sextante software, that works integrated into QGIS and adds a broad set of independent applications (GRASS GIS, SAGA GIS, OTB, R, GDAL/OGR, Pymorph, LASTools, Python scrips, etc..) in a single interface, providing a huge geoprocessing toolbox to QGIS users. Besides the integration of these applications in QGIS, Sextante has a tool for creating models, taking advantage of the modules offered by any of those softwares which aggregates. So, we\'ve created a model to automate the process of producing Forest Fire Hazard and Risk maps, using GRASS, SAGA, fTools and MMQGIS tools.

<figure>
<img src="../images/portugal_pinhel4.png" class="align-right" alt="portugal_pinhel4.png" />
<figcaption>Part of the model developed for automation of the production of cartography for Forest Fire Hazard and Risk.</figcaption>
</figure>

The results obtained so far are very promising, as already can be automatically achieved the creation of the Hazard and Risk Maps \[2\]. Taking into account that the Python version of Sextante is still very recent and is in heavy construction, there are some problems that must be corrected so that the models may be completed, which certainly will happen very soon, given the momentum that Sextante project presents. As future work, we intend to apply, also automatically, the symbology to the results as well as provide the final layouts in QGIS Composer, ready for export and/or print. Upon completion of the second phase and the realization of a sufficient set of tests that can validate the results obtained, it is our intention to provide the model free and openly.
## Підсумки
Використання альтернативного програмного забезпечення підтвердило, його визначну якість та дозволило виконати всі рекомендації Національної Лісової Адміністрації більш ефективно у порівнянні з власницьким програмним забезпеченням. З точки зору зручності використання можемо відзначити, що це програмне забезпечення не складніше за власницьке та вимагає лише більше технічних знань під час створення моделей, що однак, тільки дає більший рівень свободи та дозволяє налаштовувати моделі для конкретних умов. Процес створення карт ризиків з використанням вільного програмного забезпечення повністю відлагоджений та використовується у муніципалітеті Піньел.

Той факт, що вільне програмне забезпечення базується на стандартах та підтримує більшість відкритих форматів даних, дозволяє прозоро замінювати окремі компоненти та вибирати найбільш зручне рішення в кожній ситуації. І хоча ми вибрали певне програмне забезпечення, ніщо не заважає замінити його на інші альтернативи. Однак, QGIS є найбільш повною та стабільною, зручною у використанні вільною ГІС програмою. Вона стрімко розвивається, помилки виправляються оперативно, практично щоденно з'являються нові плаґіни для вирішення різних задач.
## Автор
<figure>
<img src="../images/portugal_pinhelaut.png" class="align-left" height="200" alt="portugal_pinhelaut.png" />
<figcaption>Pedro Venâncio</figcaption>
</figure>

Pedro Venâncio має ступінь бакалавра з геології, аспірант вільного програмного забезпечення та магістр з географічних інформаційних систем. Був дослідником у Центрі геофізики Університету Коїмбри, в Національній лабораторії цивільного будівництва, а в даний час відповідає за картографічні сервіси та географічні інформаційні системи в муніципалітеті Піньел.

{{<content-end >}}
