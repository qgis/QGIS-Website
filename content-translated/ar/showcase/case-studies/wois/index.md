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
## وصف النظام
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

تتمثل الميزة الرئيسية في مربع أدوات المعالجة في القدرة على استخدام الوظائف بسلاسة من موفري خوارزمية مختلفة لمعالجة البيانات وتحليلها. ويمكن استخدام هذا لإنشاء نماذج معالجة تلقائية ، ومن خلال مكون QGIS الإضافي الذي تم تطويره خلال مشروع TIGER-NET ، إلى الجمع بين الخوارزميات من مقدمي الخدمات المختلفين إلى سلاسل معالجة تعتمد على المعالج. تم استخدام هذه الوظيفة لإنشاء مكتبة لسير عمل قياسي (مع تعليمات) لأداء مهام شائعة ولكنها معقدة تتعلق بتحليل بيانات EO داخل إدارة الموارد المائية.

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

وقد تم توضيح الاستخدام العملي والعملي لنظم WOIS لدعم الإدارة المتكاملة للموارد المائية في أفريقيا من خلال سلسلة من حالات العرض العملي الخاصة بالمستخدم والتي تغطي مجموعة واسعة من المواضيع والمنتجات الإعلامية. وتشمل هذه: جودة مياه البحيرة. مراقبة الفيضانات تدهور الأراضي وتوصيف الغطاء الأرضي ؛ خرائط الأجسام المائية والنمذجة الهيدرولوجية. حالات المظاهرة لديها عدة مراحل. أولاً ، يتم تطوير سير عمل معالجة معالجة مخصصة من طرف إلى طرف للمنتجات والتطبيقات المطلوبة. وتستخدم هذه التدفقات فيما بعد لاشتقاق المنتجات على مدى فترات زمنية وفيرة حسب طلب المستخدمين. في الخطوة الأخيرة ، يتم تقييم سير العمل (أي استقراره / أدائه وسهولة استخدامه) بالإضافة إلى نتائج المنتج في حوار وثيق مع المستخدمين.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## الخاتمة
يمثل تطوير نظام WOIS مثالاً ناجحًا لنموذج التنمية الذي يعتمد على المستخدم والتعاوني ، حيث تم تصميم الوظائف وتطويرها وتقييمها من خلال الحالات التي يحددها المستخدم من أجل إظهار التأثير الحقيقي للنظام على تحسين إدارة المياه والمياه المتكاملة خطط إدارة الموارد. وقد تم بالفعل تطبيق نظام WOIS في السلطات الأفريقية الرئيسية في أحواض الأنهار ، والعديد من الوزارات والوكالات الأفريقية ، وكذلك في المنظمات البحثية والإنسانية. ولذلك سوف يستمر في التطوير استجابة لمتطلبات المستخدم المستمرة للوظائف الجديدة والتحسينات الوظيفية وبسبب البرامج العامة والخوارزميات وتحسينات الطرق.

وسيتم التركيز بشكل خاص على ضمان دعم وتنفيذ قدرة المعالجة للنظام الساتلي Sentinel الجديد من خلال دمج أدوات الأدوات ESA Sentinel في WOIS وتطوير تدفقات عمل الإنتاج المخصصة. سيتضمن الإصدار التالي من WOIS (المقرر في النصف الثاني من شهر أبريل 2015) دمج أدوات Sentinel-1 وعدد من تدفقات العمل باستخدام مجموعة بيانات الرادار الجديدة لرصد الفيضانات ورسم خرائط الجسم المائية وما إلى ذلك. وسيؤدي هذا إلى تحويل WOIS إلى نظام كامل نظام المراقبة التشغيلية. ومن خلال توفير هذا النظام الخالي من الرخص والقابل للتمديد ، ومن خلال استمرار جهود بناء القدرات والتدريب ، يسعى المشروع إلى بناء الأساس للتمديد ، أي النشر في بلدان ومناطق أخرى في أفريقيا وخارجها.
## المراجع
- Bauer-Gottwein، P.، Jensen، I. H.، Guzinski، R.، Bredtoft، G. K. T.، Hansen، S.، & Michailovsky، C. I. (2015). التنبؤ التشغيلي بالنفايات النهرية في الأحواض سيئة القياس: دراسة حالة حوض نهر كافانغو. علم المياه وعلوم نظام الأرض ، 19 (3) ، 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C.تمكين استخدام بيانات رصد الأرض من أجل الإدارة المتكاملة للموارد المائية في أفريقيا مع نظام مراقبة ومعلومات المياه. التحكم عن بعد. 2014، 6، 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## الروابط
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### المؤلف
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
