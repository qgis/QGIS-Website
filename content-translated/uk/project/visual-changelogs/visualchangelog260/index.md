---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: проект
sidebar: true
title: Список змін для QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Список змін для QGIS 2.6{#changelog26 }
Release date: 2014-10-31

Список змін у QGIS 2.6.0. Ми додали багато нових можливостей, вдосконалень та покращень щоб зробити найпопулярнішу настільну ГІС ще більш функціональною та корисною.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Ми хочемо подякувати всім розробникам, авторам документації, тестувальникам та іншим людям, які добровільно витрачали свій час та сили.

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

І нарешті ми хочемо подякувати нашим офіційним спонсорам за їх безцінну підтримку:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS є вільним програмним забезпеченням і ви не зобов’язані сплачувати її використання. Ми заохочуємо людей зі всього світу, не залежно від фінансового чи соціального статусу, використовувати її. Також ми вважаємо, що можливість використовувати інструменти для обробки просторових даних допоможе людству побудувати гарне суспільство.

{{<table-of-contents >}}
## Загальне
### Ім'я файлу проекту у діалозі настройок
Тепер повний шлях до файлу проекту QGIS відображається у діалозі настройок проекту.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Можливість видаляти останню точку під час вимірювання
Тепер під час вимірювання площі або відстані ви можете видалити непотрібні вузли за допомогою клавіш :kbd:`Del` або :kbd:`Backspace`.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Вибір пов'язаних об'єктів на карті з віджету зв'язаних таблиць
### Віджети редагування
Було вдосконалено віджети редагування:
- новий віджет редагування дати/часу з підтримкою значень NULL
- текстове поле з підтримкою фільтрації
- підтримка значень NULL у всіх віджетах
- віджет «Зображення» зберігає значення NULL
- Віджет «Веб-сторінка» зберігає значення NULL
- Таблиця атрибутів відрізняє 0 та NULL
- підтримка суфіксів у віджеті «Діапазон»

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Можливість вибору лише необхідних полів при з'єднані таблиць
Під час з’єднання таблиць можна вибрати лише необхідні поля

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Віртуальні поля
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Іконки для дій
При створені «дії» для векторного шару можна вказати іконку для цієї дії.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Додаткові типи виразів
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Відключення класів для «Градуйованого знаку» та «Унікальних значеннь»
Реалізовано можливість відключення візуалізації певних класів рендерерів «Градуйований знак» та «Унікальні значення» без їх видалення.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Вдосконалена легенда
Завершено другий етап вдосконалення легенди. Сюди входить:
- Змінено API (для розробників)
- Групи візуалізації. Нова кнопка дозволяє швидко перемикатися між наборами видимих шарів.
- Можливість управляти групами з пеналі легенди
- Нова настройка для фільтрації легенди в залежності від поточного масштабу карти. Дозволяє динамічно видаляти елементи, які відповідають об'єктам, що не відображаються на карті.
- класи рендереру «Правила» відображаються у вигляді дерева

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Провайдери даних
### Вдосконалений експорт у DXF
- вибір атрибутів у діалозі призначення шару
- підтримка зафарбовування полігонів/HATCH
- конвертація тексту в MTEXT замість TEXT (включаючи шрифт, нахил та насиченість)
- support for RGB colors when there\'s no exact color match
- замість R12 використовується формат AutoCAD 2000 DXF (R15)
- видалені тестові методи R18

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Редактор макетів
### Виключення елементів з списків експорту/друку
Ми додали перемикач для виключення елементів макета зі списків експорту/друку. Якщо перемикач активовано, відповідний елемент буде відображатися лише в режимі редагування.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Виключення пустих фреймів зі списків експорту/друку
Для таблиць та фреймів HTML з'явилась можливість виключення елементів зі списків експорту/друку, якщо вони не містять даних.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Панель елементів
Дозволяє швидко вибирати елементи, блокувати їх положення та розміри тощо. Також підтримується зміна порядку шляхом перетягування елементів у панелі.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Більше настройок для ліній та стрілок у редакторі макетів
- Для налаштування відображення ліній тепер використовуються всі можливості символіки
- Колір контуру та фону стрілки може налаштовуватися
- Товщина контуру стрілки налаштовується

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Підтримка настройок, що визначаються даними, елементами макета
Більшість параметрів елементів макета тепер може визначатися даними, включаючи:
- прозорість та режим змішування кольорів
- обертання
- масштаб карти, охоплення та обертання
- Поля об'єкту атласу.
- розмір та позицію елемента.
- розмір та орієнтацію сторінки, число сторінок.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Завантаження зображень за вказаним посиланням
Зображення в макеті тепер можуть завантажуватися не тільки з локальних файлів, а й за вказаним посиланням.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Вдосконалена таблиця атрибутів
- Реалізовано можливість вибору кольору шрифтів заголовка та вмісту таблиці.
- Таблиці автоматично розбиваються на декілька фреймів, що дозволяє розміщувати їх у колонках або на декількох сторінках.
- Можливість відображення заголовків на першому фреймі, на всіх фреймах або виводи таблицю без заголовків.
- Ручне налаштування ширини стовпчиків.
- Нові настройки джерела таблиці, включаючи поточний об'єкт атласу та дочірній об'єкт.
- Настройка поведінки пустих таблиць включаючи видалення пустої таблиці, відображення пустої таблиці або відображення повідомлення замість таблиці.
- Можливість відображення в таблиці лише об'єктів, які перетинаються з поточним об'єктом атласу.
- Можливість видалення однакових рядків з таблиці.

Слід пам'ятати, що таблиці в наявних проектах не будуть автоматично конвертуватися у новий формат, тому їх необхідно створити знову.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Вдосконалення в редакторі макетів
Редактор макетів у версії 2.6 отримав велику кількість вдосконалень.
- Тепер можна налаштовувати другий колір для масштабних лінійок
- Натискання :kbd:`Shift` під час малювання ліній/стрілок дозволяє точно створювати вертикальні, горизонтальні та з нахилом у 45 градусів лінії
- Натискання :kbd:`Shift` під час створення нових об'єктів робить їх квадратними, а натискання :kbd:`Alt` --- активує малювання від центру
- Для блокування/розблокування елементів тепер використовується панель елементів, а не права клавіша миші. Заблоковані елементи не вибираються, що значно спрощує взаємодію з іншими елементами.
- Натискання :kbd:`Alt` одночасно з клавішами управління курсором призводить до зсуву елементів на 1 піксель
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Вдосконалена прив'язка елементів
Межа прив'язки задається у пікселях, що робить переміщення та зміну розмірів елементів більш плавною. Згруповані елементи більше не використовуються для автоматичної прив'язки.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Підтримка декількох оглядових карт
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Вдосконалений елемент HTML
Елемент HTML отримав велику кількість вдосконалень:
- можливість вручну задавати вміст
- підтримка виразів QGIS всередині HTML
- Посилання для завантаження може визначатися даними
- Користувач може вказати свою таблицю стилів

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Вдосконалення сітки
- З'явилась можливість відображення декількох сіток з різними параметрами.
- Можна комбінувати географічні та зпроектовані сітки.
- Для налаштування зовнішнього вигляду сіток доступні всі можливості символіки.
- Новий тип сітки з відображенням лише анотацій.
- Нова настройка, що визначає на якій стороні карти відображати рамку.
- Нові стилі штрихів для рамки: внутрішні, зовнішні та внутрішні і зовнішні.
- Нові формати анотацій
- Для анотацій використовуються правильні символи штрихів та подвійних штрихів.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Обробка
### Онлайн репозиторій моделей та сценаріїв
З'явилась можливість завантажувати моделі та сценарії з онлайн репозиторію. Колекція поповнюється користувачами Processing.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Новий редактор моделей
Було повністю переписано редактор моделей, тепер він дозволяє створювати складні моделі без обмеження вкладеності. Моделі зберігаються у форматі JSON. Також ми подбали про підтримку моделей старого формату, тому ви зможете використовувати свої старі моделі. З'явилась підтримка перетягування алгоритмів та параметрів на робочу область з відповідних списків.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Програмування
### Змінено API віджетів QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## Сервер QGIS
### Вдосконалено пошук за допомогою запитів GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Налаштування точності відображення геометрії у результатах запитів GetFeatureInfo
## Символіка
### Кращий вибір випадкових кольорів
Ви вдосконалили алгоритм генерації випадкових кольорів, тепер вони більше відрізняються один від одного.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Вдосконалений інтерфейс символіки
- За можливості параметри символьного шару зберігаються при зміні його типу.
- Можливість редагування кольорових шкал
- Автоматичне оновлення підписів та значень сусідніх діапазонів
- Автоматична конвертація класів градуйованого та унікального знака у правила
- Можливість вказувати одиниці виміру та розрядність для підписів градуйованого знаку
- покращено швидкість реакції на зміну кольорової шкали та інших настройок
- Збереження настройок знаку при зміні рендерера
- Виправлений підпис для режиму стандартного відхилення.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Графічний інтерфейс
### Підсвітка синтаксису у редакторі коду
Для редакторів Python, виразів, фільтрів та редакторів HTML/CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Палітри кольорів
З'явилась можливість задавати власні палітри кольорів.
- Глобальна палітра кольорів
- Палітра кольорів проекту
- Кольори відображаються у вигляді кнопок вибору
- Також палітри можна імпортувати/експортувати

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Новий діалог вибору кольору
Розроблено новий діалог вибору кольорів. Серед його можливостей:
: - Повзунки для насиченості, тону, значення та червоного, синього і зеленого компонентів
  - Повзунок для налаштування прозорості
  - підтримка копіювання та вставки HTML-кодів кольору в різних форматах
  - попередній перегляд з можливістю порівняння попереднього та поточного кольору
  - Інтерактивний віджет палітри кольорів
  - Колесо/трикутник відтінків
  - Редагування палітр, включаючи можливість створення нової та імпорт/експорт
  - можливість «захвату» кольору (так звана «піпетка», доступно не для всіх ОС)
  - підтримка перетягування кольорів в/з інші програми (доступно не для всіх ОС)
  - користувач має вибір який саме діалог буде використовуватися: системний чи діалог QGIS

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Новий інструмент вибору об'єктів
Інструменти «Вибрати об’єкт» та «Вибрати об’єкти прямокутником» замінено одним універсальним інструментом.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Додавання шарів на карту за замовчанням
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Іконки розмірів 48 та 64
Для тих, хто використовує QGIS на планшетах реалізовано можливість вибору великих іконок, включно до 64х64.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Нові кнопки вибору кольорів
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Контекстне меню інструмента ідентифікації
При використанні інструмента визначення об'єктів натискання правої клавіші миші викличе контекстне меню. За допомогою меню можна вказати які саме об'єкти вас цікавлять.

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
