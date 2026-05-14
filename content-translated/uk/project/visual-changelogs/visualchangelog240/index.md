---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: проект
sidebar: true
title: Список змін для QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Список змін для QGIS 2.4{#changelog24 }
Release date: 2014-06-27

Список змін у QGIS 2.4.0. Основна увага у цьому випуску приділялась вдосконаленню та продуктивності --- ми реалізували багато нових можливостей, щоб зробити інтерфейс більш зручним та легким у використанні. Значна увага приділялась редактору макетів (для створення друкованих карт), щоб перетворити його на повноцінну платформу для створення красивих картографічних продуктів.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Ми хочемо подякувати всім розробникам, авторам документації, тестувальникам та іншим людям, які добровільно витрачали свій час та сили.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

І нарешті ми хочемо подякувати нашим офіційним спонсорам за їх безцінну підтримку:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Загальне
### Feature: Generate band name with NetCDF EXTRA_DIM
Формат NetCDF містить розширену інформацію про виміри, ця інформація зберігається у метаданих кожного каналу і може використовуватися для детального опису каналів. Наприклад, канали файлу NetCDF містять інформацію про температуру на певній глибині. Для користувачів набагато зручніше вибирати потрібний канал, спираючись на дані про глибину, а не за номером каналу.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Використання масштабу та зсуву для растрових даних
Деякі растрові формати зберігають дані як цілі числа з відповідним масштабом та зсувом у метаданих. Ці відомості використовуються для отримання правильних даних. QGIS тепер використовує цю інформацію та надає користувачу правильні відомості.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Панель калькулятора в таблиці атрибутів
Спеціально для тих, хто часто працює з таблицею атрибутів та створює нові поля. Панель калькулятора дозволяє швидко оновлювати значення атрибутів.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Режими попереднього перегляду карти та редактора макетів
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Файли шарів QGIS QLR
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Нові функції у редакторі виразів
У редактор виразів додано декілька нових функцій.
- обмежувальна рамка (bounds)
- bounding box width & height (bounds_width/bounds_height)
- мінімальна та максимальна координата X або Y (xmin/xmax/ymin/ymax)
- функція wordwrap, яка повертає рядок, розбитий на задане максимальне або мінімальне число символів

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Копіювання, вставка та перетягування кольорів
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Багатопотокова візуалізація
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Підписи
### Багаторазове підписування об'єктів
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Редактор макетів
### Вдосконалений елемент «зображення»
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Режим «вказані масштаби» для атласів
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Вдосконалена таблиця атрибутів
Значно покращено та вдосконалено відображення таблиць атрибутів у редакторі макетів:
- з'явилась можливість перевпорядкування стовпчиків таблиці
- реалізовано підтримку стовпчиків на основі виразів
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- вміст таблиці можна фільтрувати з використанням виразів

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Інші вдосконалення
Зроблено багато інших вдосконалень, які роблять роботу з редактором макетів більш зручною:
- можливість встановити охоплення поточної карти в якості охоплення основної карти
- підтримка експорту в SVG з розбиттям на шари
- можливість настойки стиків та кінців масштабних лінійок
- можливість настойки стиків рамок елементів

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Вдосконалений елемент HTML
Нова кнопка **[Додати фрейм]** дозволяє створювати зв'язані елементи. Вдосконалено алгоритм розбиття на сторінки.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Плагіни
### Плаґін пошуку в каталогах CSW
Плаґін MetaSearch дозволяє шукати дані у каталогах метаданих, що підтримують стандарт OGC CSW (Catalogue Service for Web).

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Символіка
### Зафарбовування контурів
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Можливість зсунути маркерну лінію
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Новий рендерер «інвертований полігон»
Новий режим зафарбовування дозволяє налаштувати стиль, який буде використовуватися для всіх об'єктів **за межами** ваших полігонів. Цей режим може використовуватися для виділення областей або створення картографічних маск.

**Примітка**: нова версія плаґіна Mask дозволяє легко створювати шари масок, підписувати об'єкти, які знаходяться у цій області та автоматично генерувати маску під час друку атласів.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Збереження стилів у базі SpatiaLite
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
