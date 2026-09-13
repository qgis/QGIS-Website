---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS в урядовому стеку FOSSGIS кантона Золотурн у Швейцарії
type: case-study

---
{{<content-start >}}
# QGIS в урядовому стеку FOSSGIS кантона Золотурн у Швейцарії
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

Кантон Золотурн надає послуги та забезпечує інфраструктурою 250000 мешканців. У 2001 році парламент вирішив мігрувати з Windows на Linux. Основними причинами були незалежність від конкретного постачальника, розвиток приватного підприємництва та зменшення витрат на ліцензії. В результаті відділ SO!GIS кантону Золотурн почав розробляти вимоги до ГІС з врахуванням потреб більше ніж 3500 співробітників та стратегії FOSSGIS.

Першим кроком стало впровадження UMN MapServer та розробка клієнта SO!MAP, який є простим у використанні WebGIS-клієнтом для всіх 3500 співробітників. Другим кроком став перенос всіх геопросторових даних у форматі shape-файлів у просторову базу даних PostGIS. Перші кроки були дуже успішними, але бракувало зручної у використанні настільної ГІС.

Після оцінки різних варіантів ми вирішили використовувати QGIS в поєднанні з GRASS, замінивши ними ESRI ArcInfo та ArcView3 у 2006 році.

Рішення було прийняте з огляду на наступне:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- проект OSGeo
- інтерфейс перекладено на німецьку
- документацію перекладено на німецьку
- активний розробник (Marco Hugentobler) проживає у Швейцарії поблизу Золотурну
- ми можемо укласти контракт з Marco Hugentobler щодо реалізації відсутнього функціоналу, наприклад оцифровки та підготовки друкованих карт
- розробка програм та плаґінів на Python
- співтовариство користувачів постійно зростає
- дуже активна спільнота розробників
- відсутня залежність від однієї операційної системи

## Де ми використовуємо QGIS
На відміну від інтерактивних карт, що обслуговуються UMN MapServer, настільна ГІС повинна забезпечувати гнучке відображення просторових даних Золотурну. QGIS використовується у повсякденній роботі більше ніж 50 користувачів. Вони хочуть відображати та/або обробляти просторові дані за допомогою інтуїтивно зрозумілого інтерфейсу.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA містить зрозумілу людям інформацію про модель даних, і звичайні користувачі можуть використовувати цю базу для пошуку необхідної інформації.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Підсумки
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Автор
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Dr. Horst Düster надіслав цю статтю у травні 2009 року. Він працює ГІС-координатором Департаменту геоінформатики кантону Золотурн, Швейцарія.

{{<content-end >}}
