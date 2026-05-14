---
draft: 'true'

---
# Моделювання екологічних коридорів для вовків у Португалії з QGIS та GRASS
The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

![Study area in Portugal](./images/portugal_ribeira1.png){.align-right}

Рібейра-де-Піна --- муніципалітет в окрузі Віла-Реал на півночі Португалії. Це сільський муніципалітет, який характеризується наявністю сільського господарства, випасанням худоби, лісами, горами, долинам з різноманітною фауною та низькою густотою населення. Все це дає вовкам можливість проживання. Розміщений між суворим гірськими Траз-уж-Монтіш та зеленою Мінью, Рібейра-де-Піна може слугувати екологічним коридором між районами з високою концентрацією вовків на півночі та низькою концентрацією на півдні.

Я почала використовувати ГІС під час свого навчання, а більше ґрунтовно --- під час підготовки магістерської роботи. В той час я в основному використовувала власницьке програмне забезпечення. Після завершення навчання я втратила доступ до нього.

В той же час я відкрила для себе світ Linux. Після того, мені запропонували допомогти дослідникам змоделювати екологічні коридори для вовків у Рібейра-де-Піна з використанням ГІС, оскільки вони самі ніколи не працювали з такими програмами. Так як я вже використовувала Linux, моєю першою проблемою став пошук необхідного програмного забезпечення. Саме тоді я дізналась про QGIS та вирішила спробувати її, хоча вона й виглядала дуже примітивною та незавершеною у порівнянні з відомими мені програмами. Я дуже швидко зрозуміла, як я помилялась, та була вражена аналітичними можливостями QGIS, особливо з врахуванням інтеграції з GRASS.

Для моделювання екологічних коридорів ми використовували QGIS з плаґіном GRASS. В процесі моделювання використовувалися як просторові дані так і відомості про наявність видів у певних областях. Нижче наведено деякі види аналізів, які було виконано:
- створення цифрової моделі рельєфу за допомогою плаґіна інтерполяції
- генерація вододілів за допомогою модуля GRASS r.watershed
- розрахунок карти відстаней між об'єктами за допомогою модуля GRASS r.grow.distance
- ре-класифікація растрових даних за допомогою модуля GRASS r.reclass
- розрахунок крутизни схилів за допомогою модуля GRASS r.slope.aspect.slope
- растрова алгебра з використанням модуля GRASS r.mapcalculator
- розрахунок вартості переміщення між різними областями за допомогою модуля GRASS r.cost.coord
- r.drain in GRASS: Traces a flow through an elevation model on a raster map \---- the one used to create the corridors

У цій роботі ми отримали карту потенційних екологічних коридорів для вовків у муніципалітеті Рібейра-де-Піна. Ці області будуть враховуватися працівниками адміністрації під час планування заходів зі збереження виду. Коридори мають надзвичайну важливість, оскільки вони з'єднують розрізнені та нестабільні вовчі зграї у Віла-Реал на півдні з більш стабільними на півночі у Пенеда-Жереш та Іспанії. Особливу увагу слід звернути на те, що ці коридору перетинають людські поселення: маленькі селища, міста та дороги. Ці ділянки необхідні для збереження вовків, необхідно вжити заходів для зменшення впливу людини на них.

![Ecological corridors and critical conservation areas for wolves in northern Portugal.](./images/portugal_ribeira2.png){.align-right width="100.0%"}
## Підсумки
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Автор
![Monica Almeida](./images/portugal_ribeiraaut.png){.align-left height="200px"}

Monica Almeida надіслала цю статтю у липні 2012 р. Вона біолог та працює у недержавній установі зі збереження вовків у Португалії.
