---
draft: 'true'

---
# QGIS ورسم خرائط مخاطر حرائق الغابات في البرتغال
لقد تضررت البرتغال من حرائق الغابات الكبيرة التي تسببت في خسائر فادحة ، ليس فقط من الناحية البيئية ، ولكن أيضا خسائر اقتصادية واجتماعية. لمواجهة هذا الخطر ، قررت الحكومة البرتغالية ، من خلال الهيئة القومية للغابات (AFN) ، قبل بضع سنوات ، إنشاء مكاتب فنية مخصصة للحكومات المحلية ، والتي ، من بين مهارات أخرى ، يجب إعداد خطط البلدية لحماية الغابات من الغابات والاستجابة التشغيلية .

In order to support the elaboration of these documents, the AFN provided technical guides with a methodology for calculating and mapping the Forest Fire Hazard and Risk. Moreover, tutorials have been offered to follow this methodology, using Proprietary Software. However, the acquisition and licensing costs of that software are unaffordable for most of the smaller local administrations and so, it was decided to create and make available a guide with a methodology for developing Hazard and Risk cartography using only Free and Open Source Software \[<http://goo.gl/TSv2E>\].

تم اقتراح استخدام مجموعة البرامج التالية: مكتبات QGIS و GRASS GIS و gvSIG و GDAL / OGR. يصف هذا الدليل جميع مهام المعالجة الجيولوجية اللازمة لوضع خطط لحماية الغابات من الحرائق والاستجابة التشغيلية ، وفقًا لمنهجية AFN. تم تطوير جزء كبير من المهام باستخدام QGIS ، وتم تطوير التحليل المكاني في نموذج البيانات النقطية باستخدام GRASS. تم استخدام gvSIG لتحليل الشبكة ، مع ملحق تحليل الشبكة ، واستخدمت مكتبات GDAL / OGR للتحويلات بين الأنظمة المرجعية المنسقة.

بعد مجموعة واسعة من الاختبارات للمنهجية ، وثلاث سنوات من التطبيق الفعلي في إعداد الخطة التشغيلية لبلدية Pinhel ، يمكن القول أن البدائل المقترحة تسمح باستبدال ، مع العديد من المزايا ، البرمجيات الاحتكارية التي عادة ما تكون تستخدم لتنفيذ هذه المهمة. يظهر إثبات صحة النتائج أنه على الرغم من البساطة النسبية للنموذج المفاهيمي ، فإن قدرته التنبؤية جيدة إلى حد كبير ، وأن تطبيق النموذج في برامج المصدر المفتوح لا يتدخل سلبًا في النتائج ، بل على العكس تمامًا.
> ![](./images/portugal_pinhel1.jpg){.align-right}

![Forest Fire Hazard and Risk Maps of Pinhel, implemented with Open Source Software.](./images/portugal_pinhel2.jpg){.align-right}

في المرحلة الثانية ، تمت محاولة تسريع هذه العملية ، باستخدام نماذج لإنشاء سير عمل يقوم بمجموعة كبيرة من المهام ، دون تدخل بشري. تتكون هذه المرحلة الثانية بشكل أساسي في أتمتة الإجراء بأكمله الموضح في الدليل العملي والذي نتج عن المرحلة الأولى. قد تعني هذه الأتمتة تخفيض ساعات عديدة من العمل المكثف من جانب الفني الذي ينوي إنتاج خطط الدفاع عن الغابات سنويًا ، لبضع دقائق فقط ، حيث يتدخل التدخل البشري في اختيار بيانات الإدخال والإشارة إلى المكان الذي نعتزم الحفاظ على بيانات الإخراج.

![Interface of the Sextante Model to calculate the Probability of the Forest Fire Hazard.](./images/portugal_pinhel3.png){.align-right}

In furtherance of this second phase, we used the Python version of Sextante software, that works integrated into QGIS and adds a broad set of independent applications (GRASS GIS, SAGA GIS, OTB, R, GDAL/OGR, Pymorph, LASTools, Python scrips, etc..) in a single interface, providing a huge geoprocessing toolbox to QGIS users. Besides the integration of these applications in QGIS, Sextante has a tool for creating models, taking advantage of the modules offered by any of those softwares which aggregates. So, we\'ve created a model to automate the process of producing Forest Fire Hazard and Risk maps, using GRASS, SAGA, fTools and MMQGIS tools.

![Part of the model developed for automation of the production of cartography for Forest Fire Hazard and Risk.](./images/portugal_pinhel4.png){.align-right}

The results obtained so far are very promising, as already can be automatically achieved the creation of the Hazard and Risk Maps \[2\]. Taking into account that the Python version of Sextante is still very recent and is in heavy construction, there are some problems that must be corrected so that the models may be completed, which certainly will happen very soon, given the momentum that Sextante project presents. As future work, we intend to apply, also automatically, the symbology to the results as well as provide the final layouts in QGIS Composer, ready for export and/or print. Upon completion of the second phase and the realization of a sufficient set of tests that can validate the results obtained, it is our intention to provide the model free and openly.
## الخاتمة
أثبتت البدائل أنها ذات جودة هائلة ، مما يسمح لجميع العمليات الموصى بها في الأدلة الفنية لهيئة الغابات القومية ، بأكثر من طريقة ، بكفاءة أكثر من البرامج الاحتكارية. من حيث سهولة الاستخدام ، لوحظ أن هذا النوع من البرامج ليس ، بأي حال ، أكثر تعقيدًا من البرمجيات الاحتكارية ، ولا يتطلب سوى معرفة تقنية أكثر للنماذج والخوارزميات التي يتم تنفيذها والتي تسمح ، مع ذلك ، بدرجة أعلى من الحرية. ، مما يجعل من الممكن استكشاف وصقل النماذج لكل حالة معينة. يتم دمج عملية إنتاج مخاطر حرائق الغابات ومخاطرها باستخدام برامج المصدر المفتوح بشكل حصري ، بعد عدة سنوات من الاختبار والتطبيق في بلدية بينيل.

إن حقيقة أن البرامج مفتوحة المصدر تعتمد على المعايير وتدعم معظم تنسيقات البيانات المفتوحة ، تسمح بإمكانية التشغيل الكامل بين البرامج ، مما يسمح للمستخدم باختيار الأنسب في كل لحظة. على الرغم من أن اقتراحنا يشير إلى مجموعة محددة من البرامج ، فلا شيء يمنع استبداله بأي من البدائل الموجودة في مجموعة واسعة من المقترحات الخاصة بالبرمجيات الحرة والمفتوحة المصدر من أجل Geospatial. ومع ذلك ، تقدم QGIS نفسها بشكل متزايد على أنها حل FOSS4G الأكثر اكتمالا واستقرارا وسهولة الاستخدام ، ومشروعه أكثر ديناميكية ، مع تصحيح سريع للحشرات ومع التنفيذ اليومي تقريبا للمكونات الإضافية الجديدة التي تضيف وظائف محددة إلى أكثر مجالات الأنشطة تنوعا .
## المؤلف
![Pedro Venâncio](./images/portugal_pinhelaut.png){.align-left height="200px"}

بيدرو فينانيسيو في الجيولوجيا ، دراسات عليا في البرمجيات الحرة و ماجستير. في نظم المعلومات الجغرافية. كان باحثًا في مركز الجيوفيزياء بجامعة كويمبرا ، في المختبر الوطني للهندسة المدنية وهو حاليًا مسؤول عن خدمة رسم الخرائط ونظم المعلومات الجغرافية في بلدية بينيل.
