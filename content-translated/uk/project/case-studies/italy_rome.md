---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/italy_igag1.png
title: Модель QGIS Processing для спрощення первинного сейсмічного мікрозонального
  аналізу
type: case-study

---
{{<content-start >}}
# Модель QGIS Processing для спрощення первинного сейсмічного мікрозонального аналізу
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- екологічна геохімія та відновлення забруднених ґрунтів та вод;
- родовища корисних копали та переробка мінеральної сировини, включаючи очищення стічних вод;
- геоінженерія та безпека гірничих виробок;
- нещодавні геологічні зміни;
- пом'якшення наслідків стихійних лих;
- геоархеологія та археометрія;
- морська геологія;
- геоматика, ГІС-аналіх та розробка.

Вивчення первинного сейсмічного мікрозонування регіона П'єтрамонтекорвіно (Апулія, Південна Італія, розташована вздовж Центрально-Південного Апенінського хребта) --- частина проекту у співпраці з басейновим управлінням Апулії (Puglia AdB) та Департаментом геології та геофізики (DGG) університету Барі, метою якого є сейсмічне мікрозонування 63 муніципалітетів в регіоні Фоджа. Роботи проводяться за підтримки Італійського Департаменту Цивільного Захисту (DPC) та фінансуються Міжвідомчим комітетом економічного планування(CIPE n. 20/2004).
## Інструмент для вивчення первинного сейсмічного мікрозонування
Сейсмічне мікрозонування оцінює сейсмічну небезпеку на місцевому рівні шляхом визначення територій з одноріднимою сейсмічною поведінкою. Метою первинного сейсмічного мікрозонування є визначення літологічних характеристик та геометрії геологічниї блоків, що характеризують такі ділянки (мікрозони).

Аналіз пошкоджень внаслідок землетрусу часто показує зміни на місцевому рівні, які спричинені не тільки геологічними структурами, але й якістю та типом будівельних конструкцій, що призводить до різного рівня сейсмічної небезпеки.

Сейсмічне мікрозонування оцінює місцевий рівень сейсмічної небезпеки шляхом виявленя територій, що характеризуються однорідною сейсмічною поведінкою.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

Сейсмічне мікрозонування першого рівня складається з наступних тематичних карт:
1. Карта дослідження, що містить результати вивчення сейсмічного мікрозонування
2. Гео-літологічна мапа, отримана з великомасштабної геологічної та геоморфологічної мап, інтегрує наявні літологічні, статиграфічні та геотектонічні дані, пов'язані з польовими роботами
3. Мапа сейсмічного мікрозонування першого рівня (результат мікрозонування 1 рівня), визначає мікрозони трьох категорій
   - стабільні зони
   - стабільні зони, cхильні до наземної ампліфікації
   - нестабільні зони

Метою цієї роботи є створення методики обробки топографічних, геологічних, геофізичних та геотехнічних даних, необхідних для проведення сейсмічного мікрозонування першого рівня, за допомогою інструментів з відкритим кодом.

Редактор моделей, що входить до складу QGIS, був використаний для створення простої моделі. Ця модель служить для автоматизації одного з етапів підготовки карт сейсмічного мікрозонування першого рівня, а саме ідентифцікації нестабільних зон.

Модель використовує різне вільне програмне забезпечення та бібліотеки (GRASS, GDAL, QGIS), демонструючи доцільність використання QGIS в якості спрощеного та уніфікованого інтерфейсу до гетерогенних інструментів GFOSS (рис. 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

В якості вхідних параметрів модель приймає (рис. 2):
- shape-файл горизонталей з атрибутом, що містить значення висот;
- The name of the field containing elevation values;
- бажана роздільна здатність DEM та растру схилів у метрах (за замовчанням 10);
- полігональний shape-файл, з якогу будуть відібрані об'єкти, що попадають у зони з крутизною схилів більше 15 градусів;
- розміщення вихідного полігонального шару.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

Після запуску модель виконує наступні операції:
- інструмент GRASS ``v.to.rast.attribute`` конвертує значення висот горизонталей у растр вказаної роздільної здатності;
- інструмент GRASS ``r.surf.contour``генерує модель висот на основі растру, створеного на попередньому кроці;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- за допомогою ``r.mapcalculator`` визначаються області з крутизною схилів більше 15 градусів за формулою:

if(A\>15,1,null())

де A --- растр крутизни схилів, створений ``gdaldem``;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Отриманий полігональний шар містить потенційно нестабільні зони через крутизну схилів більше 15 градусів та автоматично генерується з тематичних карт, таких як карта зсувів (рис. 3) або літологічна карта.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## Підсумки
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Посилання
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Автори
Giuseppe Cosentino та Francesco Pennica (www.igag.cnr.it) надіслали цю статтю у березні 2015 р.

<figure>
<img src="../images/guiseppe_cosentino.png" class="align-left" height="200" alt="guiseppe_cosentino.png" />
<figcaption>Giuseppe Cosentino</figcaption>
</figure>

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

<figure>
<img src="../images/francesco_pennica.png" class="align-left" height="200" alt="francesco_pennica.png" />
<figcaption>Francesco Pennica</figcaption>
</figure>

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.

{{<content-end >}}
