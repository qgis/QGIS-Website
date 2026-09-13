---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: проект
sidebar: true
title: Список змін для QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Список змін для QGIS 2.0{#changelog20 }
Release date: 2013-09-09

{{<table-of-contents >}}
## Інструменти аналізу
### Processing Commander
Зручний інструмент для швидкого доступу до можливостей просторової обробки. Запустіть Commander (:kbd:`Ctrl + Alt + M`) та почніть набирати назву інструмента. Commander покаже наявні варіанти та запустить вказаний. Більше не треба блукати по меню в пошуках інструментів.

![image1](images/processing_commander_2.png)
### Вдосконалення плаґіна «Теплокарта»
Значно вдосконалено плаґін «Теплокарта», в результаті чого підвищилась швидкість генерації теплокарт. Крім того, з'явилась можливість вибору функції ядра для побудови теплокарти.

![image2](images/Selection_027.png)
### Інтеграція Processing
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Редактор моделей Processing
**Редактор моделей** Processing дозволяє легко та швидко створювати складні алгоритми обробки та аналізу шляхом з'єднання між собою простих блоків. Створені моделі можна зберігати та використовувати повторно, а також застосовувати в якості складових у більш складних моделях.

![image4](images/Processing_modeler_029.png)
## Програма та проекти
### Стартовий проект та шаблони проектів
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Системні змінні оточення
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Користувацькі набори масштабів
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Браузер
### Вдосконалення вбудованого оглядача
- Можливість фільтрації каталогів за маскою або регулярним виразом
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Іконки сортуються за типом елемента (файлова система, бази даних, картографічні сервіси)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Провайдери даних
### Оновлення растрового провайдера
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Підтримка Oracle Spatial
В QGIS 2.0 з'явилась підтримка Oracle Spatial.

![image10](images/oracle.png)
### Провайдер Web Coverage Service
У QGIS з'явилась підтримка шарів Web Coverage Service ---  процес додавання таких шарів нічим не відрізняється від додавання шарів WMS або WFS.
### Зріз 2% для растрів за замовчанням
Растри часто мають велику кількість викидів, що призводить до некоректного відображення. QGIS 2.0 використовує більш гнучкий та надійний алгоритм відображення растрів, включаючи використання зрізу 2% - 98% з накопиченням за замовчанням. Нижче показано відображення одного й того ж растру в QGIS 1.8 (зліва) та QGIS 2.0 (справа) з використанням налаштувань за замовчанням.

![image11](images/Selection_023.png)
### Формат результатів визначення WMS
Реалізовано можливість вибору формату відображення результатів визначення об'єктів у шарах WMS, якщо така можливість надається сервером. Підтримуються наступні формати: HTML, GML та простий текст. Якщо вибрано формат GML, результат буде таким же як і при визначенні об'єктів у векторному шарі: об'єкт на карті підсвічується, а його геометрію та атрибути можна скопіювати у буфер обміну та вставити в інший шар.

![image12](images/wms-identify.png)
### Підтримка WMTS
Клієнт WMS у QGIS тепер підтримує WMTS (Web Mapping Tile Service), включаючи вибір вкладених наборів даних, таких як часові зрізі. Під час додавання шару з серверу ви зможете вибрати який саме часовий зріз відображати.

![image13](images/Selection_035.png)
## Загальне
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Підписи
### Нова система підписування
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Параметри підписів на основі виразів
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

В якості прикладів можна навести наступні параметри, що підтримують вирази:
- Шрифт
- Розмір
- Стиль
- розмір буфера

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Стара система підписів не підтримується
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

Порядок роботи зі старою системою підписів у QGIS 2.0:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- Стара вкладка відображається для проектів, в яких хоча б один шар використовує старі підписи, і не буде схована навіть якщо проект перевести на використання нової системи.

Стару вкладку можна включити або виключити для поточного проекту за допомогою наступних команд:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**УВАГА**: *швидше за все* стара система підписів буде повністю видалена у наступному стабільному випуску QGIS. Будь ласка, оновіть свої проекти.

![image17](images/changelog-2.0_labels-deprecated.png)
## Легенда
### Нові можливості списку шарів
- Відображення кількості об'єктів шару, та кількості об'єктів кожного класу
- Векторні шари в режимі редагування позначаються червоним олівцем, якщо мають незбережені зміни
- Активний шар виділяється підкреслюванням
- Зняти вибір тепер можна клацнувши мишою по вільній частині легенди
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Імена груп та шарів можуть виділятися напівжирним
- Опціональне відключення генерації зменшених копій растрів, що в деяких випадках значно прискорює завантаження проектів

![image18](images/changelog-2.0_visual-options.png)
### Клонування шару
Можливість продублювати вибраний растровий або векторний шар у легенді. Рівнозначне повторному завантаженню шару та застосуванню до нього такого ж стилю.

![image19](images/changelog-2.0_dup-layer_1.png)
### Редагування декількох шарів
Якщо вибрано декілька шарів і хоча б один з них знаходиться в режимі редагування, можна швидко зберегти або відмінити поточні зміни. Також можна виконати ці дії для всіх шарів не залежно від наявності вибору.

![image20](images/changelog-2.0_current-edits.png)
## Редактор макетів
### Елемент HTML
З'явилась можливість розміщувати на карті елементи HTML.

![image21](images/Composer_1_006.png)
### Підтримка багатосторінкових макетів
Один макет тепер може складатися з декількох сторінок.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Вирази в підписах макету
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Підписи з виразами на зразок:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
будуть обчислені в процесі друку (або візуалізації) і відображені як:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Автоматичні направляючі
Запроваджено автоматичні направляючі для вирівнювання близько розміщених елементів макету.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Користувацькі направляючі
Іноді необхідно вирівняти елементи у певному місці макету. Нові користувацькі направляючі дозволяють додавати необхідну кількість ліній прив'язки для кращого вирівнювання елементів.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Генерація послідовностей карт
Редактор макетів тепер дозволяє генерувати послідовності карт (атласи). В якості шару-покриття можуть використовуватися точки, лінії, полігони, а атрибути поточного об'єкту можна використовувати у підписах.

![image26](images/Picture1.png)
### Підтримка оглядових карт
Необхідно показати поточну область основної карти в вікну огляду? Тепер така можливість існує. Карта може відображати межі іншої карти та буде оновлюватися при їх зміні. Використання цієї можливості разом з функцією підготовки атласів дозволяє створювати зручні карти. Рамка оглядової карти може використовувати такі ж стилі як і звичайний полігональний об'єкт, то ж ваша творчість нічим не обмежується.

![image27](images/Picture1_1.png)
### Змішування шарів
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Підтримка HTML у підписах
Підтримка HTML у підписах дає дозволяє контролювати зовнішній вигляд карт у ще більш широких межах. Підписи отримали повну підтримку CSS, HTML і навіть JavaScript.

![image29](images/html.png)
### Багатоколоночна легенда
Легенда тепер підтримує відображення у декілька стовпчиків. За необхідності можна розбивати один шару з багатьма класами на декілька стовпчиків. Шари з одним класом за замовчанням додаються як один рядок. Реалізовано три способи відображення назви шару або групи: Група, Вкладена група або Сховати. Стилі заголовків дозволяють налаштовувати групування елементів. Наприклад, шар з одним класом може відображатися одним рядком або з назвою шару (як у QGIS 1.8), символи декількох шарів можна об'єднати в групу тощо. За бажанням також можна відобразити число об'єктів.

![image30](images/multicolumn-legend.png)
### Вдосконалення в управлінні макетами
Внесено наступні зміни в управління макетами:
- Назву макета можна вказати на етапі створення, в тому числі вибравши в якості заготовки назву іншого макета
- Макети можна дублювати
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Можливість зберегти проект з вікна редактора макетів
- Всі операції з управління макетом тепер доступні у вінкі редактора макетів

![image31](images/changelog-2.0_composer-mngmnt.png)
## Плагіни
### Оновлений менеджер плаґінів
У QGIS 1.x управління плаґінами було дещо заплутаним через наявність двох інтерфейсів --- один для управління вде встановленими плаґінами та інший для їх завантаження з репозиторія. В QGIS 2.0 ми реалізували **новий, уніфікований менеджер плаґінів**, який є *єдиним місцем* для завантаження, активації/деактивації та управління плаґінами. Крім того, інтерфейс тепер виглядає набагато краще завдяки використанню бічної панелі та нових іконок!

![image32](images/Plugin_Manager_024.png)
## Програмування
### Нова консоль Python
Нова консоль Python надає значно більше можливостей: підтримка автоматичного доповнення, підсвітка синтаксису, можливість налаштування шрифтів. Вбудований редактор коду з підтримкою завантаження та запуску файлів, дозволяє легко вводити великі блоки коду.

![image33](images/pyconsole.png)
### Розширений набір виразів
Вирази використовуються у багатьох підсистемах QGIS та дозволяють створювати підписи та символи з використанням виразів. У редакторі виразів було реалізовано багато нових функцій, і всі вони мають вбудовану довідку з прикладами використання.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Користувацькі функції
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Нове Python API
Python API було перероблене, щоб зробити його використання більш зручним. API QGIS 2.0 використовує SIP v2, завдяки чому вдалось позбавитися ручної конвертації типів даних. Всі типи даних тепер автоматично конвертуються у відповідні типи даних Python.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
Вдосконалено процес зчитування об'єктів шару, що в майбутньому дозволить реалізувати багатопоточність.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Сумісність коду з серією 1.х
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Макроси проекту
Код Python, збережений у файлі проекту, може виконуватися при настанні однієї з наступних подій:
- `openProject()`
- `saveProject()`
- `closeProject()`

Необхідність запуску макросів можна налаштувати.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Символіка
### Перевизначення параметрів
Завдяки можливості перевизначення параметрів можна контролювати тип символу, його розмір, колір, повертання та інші параметри, через атрибути об'єктів.

![image39](images/datadefinedproperties2.png)
### Вдосконалення в управлінні символами
Нова область перегляду символу відображає структуру символу та надає швидкий доступ до всіх символьних шарів.

![image40](images/symbollayertree.png)
### Підтримка прозорості у діалогах вибору кольору
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Управління кольорами для растрів
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Копіювання символіки між шарами
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Збереження стилів у базі даних
Якщо ви використовуєте базу даних для збереження векторних шарів, то можете зберігати стилі у цій же базі даних. Завдяки цьому значно спрощується задача розповсюдження стилів у багатокористувацькому середовищі.

![image44](images/Selection_037.png)
### Підтримка кольорових шкал
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Стилі за замовчанням
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Графічний інтерфейс
### Нова тема іконок
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Бічні панелі та групи, що згортаються
Ми стандартизували зовнішній вигляд вкладок та почали використовувати групи елементів, що згортаються. Завдяки цьому навігація по настройкам стала більш простою, а використання площі екрана --- оптимальним.

![image48](images/Selection_005.png)
### Спливаючі повідомлення
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Користувацький шрифт і таблиці стилів Qt
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Таблицю стилів QGIS можна отримати за допомогою наступної команди:

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Нові діалоги вибору кольору
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### SVG-анотації
QGIS 2.0 дозволяє додавати на карту анотації в форматі SVG --- прив'язані до вказаної точки або з відносним положенням.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Інтерактивний редактор форм
QGIS 2.0 дозволяє створювати форми вводу даних. Завдяки редактору форм можна створити форму з вкладками та групами полів.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Інструмент дія за замовчанням
Якщо ви використовуєте «дії» векторних шарів (маленькі задачі, що виконуються, коли ви клацаєте на об'єкті), вам сподобається новий інструмент. Він дозволяє вказати дію за замовчанням та виконувати її просто клацнувши на об'єкті.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
