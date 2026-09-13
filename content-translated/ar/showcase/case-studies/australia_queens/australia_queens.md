---
draft: 'true'

---
# QGIS و GRASS في الحكومة المحلية خريطة اطلاق النار في حرائق الغابات
## المقدمة
مجلس جنوب داونز الإقليمي (SDRC) هو حكومة محلية صغيرة إلى متوسطة الحجم في جنوب شرق كوينزلاند بأستراليا. منطقة المجلس ، خاصة الجزء الجنوبي ، تعاني من حرائق الغابات الكبرى. يعتبر بوشراير مصدر قلق حقيقي وحالي للسكان والملاك في منطقة داون داونز الجنوبية ، وقد أدى إلى خسائر في الأرواح والممتلكات.

سيتيح هذا المشروع للمجلس وشعوب المنطقة أن يكونوا أكثر وعياً بالمخاطر وأن يسمحوا باتخاذ قرارات أفضل في المستقبل.

![](./images/australia_queens1.jpg){.align-right}
## المشروع
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

تم تقسيم جانب نظام المعلومات الجغرافية لمشروع المشروع إلى 6 خطوات رئيسية
- تقييم المنحدر ورسم الخرائط
- تقييم الجوانب ورسم الخرائط
- تقييم الغطاء النباتي ورسم الخرائط
- الجمع بين الدرجات لتحديد خطورة خطورة حرائق الغابات
- التحقق الميداني والتقييم النوعي
- الخرائط النهائية

## استخدام QGIS و GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

تم استخدام البرنامج المساعد QGIS GRASS لاستيراد خطوط 5 متر من المنطقة بأكملها إلى GRASS والتي تم تحويلها بعد ذلك إلى خريطة خطوط المسح الكنتورية باستخدام r.surf.contour. تم بعد ذلك إنشاء منحدر وخريطة جانب باستخدام r.slope.aspect من خريطة الكنتورية النقطية. تم تعيين الفئات إلى مختلف نطاقات المنحدرات والأوجه وإعطاء خطر خطر قرحة. كما أعطيت مناطق الغطاء النباتي درجات مخاطر مختلفة. ثم تم دمج جميع الخرائط النقطية الناتجة باستخدام mapcalc وأعطيت درجة أخطار خطرة أخيرة. ثم يتم تقسيم درجات المخاطر إلى ثلاث فئات رئيسية: عالية ؛ متوسط؛ و منخفض.

وكان الجزء الأخير من العملية هو التحقق الميداني عن طريق خدمة الإطفاء الريفية. بعد عملية المراجعة ، تم استخدام QGIS لطباعة الخرائط النهائية للعرض.

بينما يمكن تشغيل جميع أوامر GRASS من سطر الأوامر ، تم تسجيل جميع الأوامر التي كانت مطلوبة لإنشاء خرائط خطر حرائق الغابات ، لأغراض التوثيق ولأن كانت هناك حاجة إلى إعادة إنشاء الخرائط في وقت ما في المستقبل.
## الخاتمة
وقد قدمت QGIS بشكل عام ، بالإضافة إلى البرنامج الإضافي GRASS ، تجربة رائعة ونتائج نهائية كبيرة للمجلس الذي يقوم برسم خرائط مخاطر حرائق الغابات الخاصة به. يوفر البرنامج المساعد GRASS واجهة سهلة الاستخدام للغاية للتنقل عبر QGIS. بما أن QGIS قادرة على فتح نسق GRASS النقطي أصلاً ، فإن التكامل سلس جداً ويمكن عمل الخرائط بسهولة.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## المراجع
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## المؤلف
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

ساهم هذا المقال في يناير 2011 من قبل ناثان وودرو. ناثان هو ضابط نظم المعلومات الجغرافية في المجلس الإقليمي لساو داونز ، وهو يدرس درجة الزمالة في العلوم المكانية في جامعة ساوزرن كوينزلاند.
