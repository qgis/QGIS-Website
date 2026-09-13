---
HasBanner: false
archived: true
date: 2011-04-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/suisse_uster1.png
title: استخدام QGIS في البنية التحتية Geodata لمدينة Uster
type: case-study

---
{{<content-start >}}
# استخدام QGIS في البنية التحتية Geodata لمدينة Uster
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2011</span>
</p>

كانت مدينة أوستر تستخدم نظام QGIS منذ عام 2007. شجعها قرار Kanton of Solothurn على استخدام QGIS كبديل لنظام GIS المكتبي لـ ArcView ، قرر Uster أيضًا تجربته. وانضمت المدينة إلى الجهود الرامية إلى مواصلة تطوير تطبيق QGIS ، من خلال اقتراح واختبار الميزات الجديدة ودعم التطوير المالي. في المقابل ، يتلقى أوستر نظامًا متنقلًا يتطور بشكل سريع ومنظم سطح المكتب GIS و WebGIS مدعومًا من قِبل منتدى عالمي للمستخدمين والتنمية.

![](../images/suisse_uster1.png)

يستخدم Postgis / PostgreSQL كمستودع جغرافي مركزي. يتم نسخ قواعد البيانات ومصادر البيانات الأخرى إلى PostgreSQL في فترة زمنية منتظمة ، باستخدام أدوات مثل OGR و FME. في البداية ، تم استخدام QGIS بشكل أساسي كمشاهد. كان أول مستخدم لـ QGIS مزارعًا لديه مهمة الإشراف على الإعلانات الصادرة عن المزارعين المحليين لتلقي الإعانات الزراعية. في وقت لاحق ، تم تقديم QGIS أيضًا كمحرر للبيانات ومنصة لنشر الخرائط ، بالإضافة إلى تحسينات أدوات التعديل وملحن الطباعة. بالتعاون مع مستخدمين سويسريين آخرين في QGIS (Solothurn، Thun and CDE (University of Berne)) ، نقوم بتنسيق ورعاية التحسينات لهذه الأدوات ، إلى جانب بعض التحسينات في ترميز البيانات ، وضع العلامات الآلي ، معالجة السمات والنماذج.

![](../images/suisse_uster2.png)

كما تستخدم إدارة المدينة برمجيات نظم المعلومات الجغرافية التجارية: Autodesk Topobase ، لالتقاط وتحرير بيانات البنية التحتية للمساحة ومياه الصرف الصحي ، و GE Smallworld لإدارة شبكات الغاز والمياه والكهرباء. ومع ذلك ، فهذه أنظمة خبيرة يستخدمها موظفون مدربون خصيصًا. يتم التعامل مع جميع مشاريع نظم المعلومات الجغرافية الأخرى وعرض جميع البيانات من قبل QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](../images/suisse_uster3.png)

اليوم ، يتم استخدام QGIS لمشاريع GIS التالية:
- عرض بيانات المياه العادمة ، وتكامل قواعد البيانات الإضافية والوصول المباشر إلى مقاطع الفيديو للقناة وبروتوكولات التفتيش
- عرض وتحرير للمراقبة والتخطيط البيئي والحضري لمياه الصرف وأنظمة الهيدرولوجيا (الألمانية: Genereller Entwässerungsplan)
- عرض البيانات المساحية الأرضية (شبكات المياه العادمة والمياه والغاز والكهرباء ، والاتصالات السلكية واللاسلكية في وقت لاحق) (الألمانية: Leitungskataster)
- عرض بيانات المسح والمسح
- عرض وتحرير المخزون الطائفي للمواقع الطبيعية المحمية
- عرض وتحرير بيانات التخطيط الحضري والإقليمي
- عرض وتحرير بيانات البنية التحتية للطرق
- عرض الإحصاءات الناتجة مباشرة من قاعدة بيانات السكان الحاليين والسابقين
- التخطيط والتصور لتخطيط الطاقة (مناطق إمدادات الغاز ، والاستخدام الحراري من المياه المستعملة ، والطاقة الحرارية الأرضية القريبة من السطح ، ومحطات تسخين الكتلة ، وما إلى ذلك)

وهناك مشاريع إضافية أخرى قيد التطوير.

![](../images/suisse_uster4.png)

في عام 2007 ، لم يكن واضحًا تمامًا في أي وتيرة سيتم تطوير نظام QGIS وطريقة تطوير الدعم المجتمعي والتجاري. اليوم يمكن القول أن سرعة التطوير والتحسينات التي قام بها مجتمع QGIS تجاوزت توقعاتنا. الدعم المجتمعي والتجاري من الشركات Sourcepole و Norbit ممتاز. هناك اتصال مباشر مع المطورين دون أن يحميهم فريق إدارة المنتج أو المبيعات. مطورو هاتين الشركتين هم أيضا مطورين رئيسيين لمشروع QGIS ولديهم معرفة ممتازة بقواعد الكود.

غالباً ما يتم إصلاح الخلل في غضون ساعات أو أيام بعد الإبلاغ ويتم تنفيذ التطورات الجديدة في إطار زمني قصير. يمكن اختبار الميزات الجديدة فورًا بعد التطوير ونشرها للمستخدمين عندما تكون الجودة جيدة بما يكفي للمستخدم النهائي. ليست هناك حاجة لانتظار إصدارات البرامج الرسمية. نحن نتمتع بحرية التمكن من التأثير على المشروع وتثبيت البرنامج على العديد من أجهزة الكمبيوتر التي نفضلها دون الحاجة إلى التعامل مع إدارة الترخيص. ونحن نتطلع إلى تعاون مستقبلي مع مجتمع QGIS ومع مؤيدينا التجاريين من أجل تطوير مشروع QGIS.
## المؤلف
<figure>
<img src="../images/suisse_usteraut.jpg" class="align-left" height="200" alt="suisse_usteraut.jpg" />
<figcaption>Andreas Neumann</figcaption>
</figure>

ساهم هذا المقال في أبريل 2011 من قبل الدكتور أندرياس نيومان. وهو منسق نظم المعلومات الجغرافية في مدينة أوستر ، سويسرا.

{{<content-end >}}
