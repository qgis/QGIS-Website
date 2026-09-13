---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: Використання Processing для автоматизавоної класифікамції снігового покрову
type: case-study

---
{{<content-start >}}
# Використання Processing для автоматизавоної класифікамції снігового покрову
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

Snowy Hydro Limited (SHL) це гірська електростанція, розташована у Сніжних Горах Нового Південного Уельсу, Австралія. Крім різноманітних генеручих активів по країні,, Snowy Hydro Limited також добре відома як охоронець традиційної австралійської інфраструктури, гідроелектричного масиву Сніжних Гір.

Гідроелектричний масив Сніжних Гір з'явився через сезонні снігопади у гірських районах Нового Південного Уельсу. Вода, що утворилась в результаті розтавання снігу навесні, використовується для генерації електроенергії, покриваючи пікові потреби національного енегретичного ринку, а також спрямовуючи воду для зрошення посушливих районів південного сходу Австралії.

Класифікація снігового покрову взимку дозволяє SHL відслідковувати життєвий цикл вкритих снігом территорій, збирати архівні дані та надавати статистику гідрографічній команді для створення прогнозів рівня води.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## Фон
Кожної зими (1 червня - 21 жовтня) SHL отримує максимально можливу кількість безхмарних знімків від супутника MODIS Terra (EOS AM). Ці знімки обробляються за допомогою алгоритма Normalised Difference Snow Index (NDSI), який використовується для виявлення територій, вкритих снігом. Оскільки цей алгоритм не прив'язаний до жодного сенсора, було обрано саме MODIS через достатню роздільну здатність та щоденне охоплення досліджуваної території (Мапа 1.1 Карта збору снагових вод).
## Мета
Метою цього проекту є автоматизація розрахунку NDSI шляхом створення моделі для Processing. Бажаним результатом є векторний шар, що відображає території, вкриті снігом, в межах області дослідження а також інформація про загальну площу цих територій.
## Метод
Алгоритм розрахунку NDSI досить простий (див. формулу 1.1), а послідовність дій, необхідних для отримання снігового покрову в векторному форматі також добре переноситься на модель Processing.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

Результат алгоритма NDSI лежить в межах від -1 до 1, а снігом є значення більші за 0.4. Приклад результату за 13 липня 2014 р. показано нижче (мапа 1.3),поряд з початковим зображенням (мапа 1.2). Як ви бачите, території, вкриті снігом, значно відрізняються від інших типів територій та хмар. Хоча можливі помилки класифікації за рахунок великих водних об'єктів, які спричиняються близькими коефіцієнтами поглинання у близькому інфрачервоному діапазоні. Тобто необхідно передбачити маскування водних об'єктів на певному етапі.

<figure>
<img src="../images/australia_snowyhydro2.jpg" class="align-left" width="300" alt="australia_snowyhydro2.jpg" />
<figcaption>Map 1.2 - MODIS true colour</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro3.jpg" class="align-center" width="300" alt="australia_snowyhydro3.jpg" />
<figcaption>Map 1.3 - NDSI output</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro4.jpg" class="align-left" width="300" alt="australia_snowyhydro4.jpg" />
<figcaption>Map 1.4 - Recoded "Snow" vs "Non snow"</figcaption>
</figure>

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

<figure>
<img src="../images/australia_snowyhydro5.jpg" class="align-left" width="300" alt="australia_snowyhydro5.jpg" />
<figcaption>Map 1.5 - Extracted Snow</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro6.jpg" class="align-center" width="300" alt="australia_snowyhydro6.jpg" />
<figcaption>Map 1.6 - Snow inside the SWC</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro7.jpg" class="align-left" width="300" alt="australia_snowyhydro7.jpg" />
<figcaption>Map 1.7 - Final snow covered area</figcaption>
</figure>

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

<figure>
<img src="../images/australia_snowyhydro.png" class="align-center" width="600" alt="australia_snowyhydro.png" />
<figcaption>Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model</figcaption>
</figure>

## Результати / Висновки
Processing є потужним інструментом автоматизації робочих процессів, таких як класифікація снігового покрову. Модель, наведена вище, успішно автоматизує класифікацію снігового покрову та створює набори даних, які можуть використовуватися для візуалізації та подальшої статистичної обробки. Також вона успішно запобігає появі помилок операторів, які мали місце при використанні SHL попередніх методів. Деякі результати можна переглянути тут.
### Автор
Andrew Jeffrey працює ГІС-аналітиком в офісі Snowy Hydro Limitedbased, в Коома NSW, Австралія. Він закінчив університет Чарльза Стурта у Вага-Вага та отримав ступін бакалавра (Bsc) геоінформаційних систем в 2004. У Snowy Hydro Limited він відповідає за підтримку наявних проектів, таких як Cloud Seeding experiment, так і щоденних робіт в організації.

{{<content-end >}}
