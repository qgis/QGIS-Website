---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS لرصد النمور (باستخدام كاميرات الفخاخ في Nameri Tiger Reserve، Assam، India
  Sonitpur District)
type: case-study

---
{{<content-start >}}
# QGIS لرصد النمور (باستخدام كاميرات الفخاخ في Nameri Tiger Reserve، Assam، India Sonitpur District)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

داخل هذا المشهد ، الأنواع الرئيسية لأهمية الحفظ هي نمور البنغال الملكي ، الفيل الآسيوي ، البيسون الهندي ، النمر الشائع ، النمر الغائم ، الكلب البري ، سمبار الغزلان ، الغزلان النباح ، الغزلان خنزير ، الخنزير البري والعديد من الأنواع الأخرى. كما أن تنوع الطيور في NTR مثير للإعجاب للغاية وقد تم تحديد أكثر من 370 نوعًا من الطيور حتى الآن. تتم إدارة الاحتياطي من قبل إدارة الغابات في ولاية آسام ، حكومة ولاية أسام.
## تطبيق QGIS لتصميم دراسة فخ الكاميرا
بدءا من عام 2011 ، جعلت الهيئة الوطنية للحماية من النمر (NTCA) في الهند من الإلزامي لجميع احتياطيات النمر في البلاد مراقبة النمور باستخدام مصائد الكاميرا. وبموجب هذا البروتوكول الجديد ، سيتم تركيب 25 زوج من الكاميرات لمدة 100 كيلومتر مربع من احتياطي النمور وفترة أخذ العينات تتراوح بين 40-60 يومًا. يعتمد بروتوكول مراقبة النمر الجديد هذا بشكل كبير على نظام المعلومات الجغرافية.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

خلال الفترة 2012-13، قمنا بتنفيذ هذا البروتوكول الجديد لمراقبة النمر في NTR باستخدام QGIS. بادئ ذي بدء ، قمنا برقمنة حدود NTR في QGIS وحفظناها كمضلع. تم تصدير هذا المضلع إلى نظام تحديد المواقع لغرض الملاحة خلال المسوحات الميدانية. أجرينا مسحا واسع النطاق في NTR للأدلة على وجود النمر مثل هذه الخدوش وعلامات الخدش والقصاصات. تم تسجيل إحداثيات GPS من علامات النمر وكذلك المواقع المناسبة للمصائد الكاميرا. بعد الانتهاء من المسح ، تم نقل البيانات إلى QGIS باستخدام أدوات GPS لمزيد من المعالجة ولوضع اللمسات الأخيرة على مواقع مصائد الكاميرا. تم إعداد ملف شكل يحتوي على علامات النمر ومواقع اعتراض الكاميرا المحتملة.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## الخاتمة
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## المؤلف
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

ساهم في هذا المقال راجيندرا ج. جرادود في مارس 2013. وهو المدير الميداني لمحمية ناميري تايجر ، آسام ، الهند. وهو حاصل على درجة الماجستير في علوم الغابات والحفظ وإدارة الأراضي.

{{<content-end >}}
