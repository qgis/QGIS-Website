---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: استخدام مربع أدوات المعالجة لأتمتة تصنيف الثلج
type: case-study

---
{{<content-start >}}
# استخدام مربع أدوات المعالجة لأتمتة تصنيف الثلج
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

ثلجي هيدرو المحدودة (SHL) هو مولد الكهرباء الذروة في الجبال الثلجية في شمال ويلز الجديدة ، أستراليا. على الرغم من امتلاك مجموعة متنوعة من أصول التوليد في جميع أنحاء البلاد ، إلا أن شركة هيدرو المحدودة ذات المياه الثلجية تشتهر باحتفاظها بقطعة بارزة من البنية التحتية الأسترالية ، وهي مخطط الطاقة الكهرمائية للجبال الثلجية.

يتم جعل مخطط الطاقة الكهرمائية للجبال الثلجية ممكنًا بسبب تساقط الثلوج الموسمية في منطقة جبال الألب في شمال ويلز الجديدة. يتم استخدام المياه المتولدة من ذوبان الثلوج الربيعي لتوليد الكهرباء التي تعالج ذروة الطلب في سوق الكهرباء الوطني ، بينما تقوم أيضًا بتحويل المياه إلى المناطق الداخلية الأكثر جفافاً في جنوب شرق أستراليا لأغراض الري والزراعة.

إن تصنيف الغطاء الثلجي خلال أشهر الشتاء يتيح لشركة SHL مراقبة دورة حياة المنطقة المغطاة بالثلوج ، ومناطق التغطية الأرشيفية للسجلات التاريخية ، وتوفير إحصاءات التغطية لفريق الخدمات الهيدروغرافية من أجل توقعات إنتاجية المياه وتخزينها.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## خلفية
في كل عام خلال أشهر الشتاء (من 1 يونيو إلى 31 أكتوبر) تحصل شركة SHL على أكبر عدد ممكن من الصور السحابية من القمر الصناعي MODIS Terra (EOS AM). يتم بعد ذلك استيعاب هذه الصور في خوارزمية تُعرف باسم مؤشر فرق الثلوج  (NDSI) ، والذي يستخدم للإشارة إلى المناطق التي يوجد بها الثلج. في حين أن هذه الخوارزمية ليست فريدة من نوعها لأي مستشعر معين ، فقد تم اختيار أداة MODIS بسبب الدقة المكانية الكافية لها والتغطية اليومية لمنطقة المشروع (خريطة 1.1 خريطة مستجمعات المياه الثلجية).
## تصويب
الهدف من هذا المشروع هو أتمتة سير عمل NDSI كنموذج في صندوق أدوات معالجة QGIS. الناتج المطلوب هو عبارة عن مضلع متجه يظهر المدى المغطى بالثلج داخل مستجمعات المياه الثلجية ، بالإضافة إلى الإسناد الذي يصف المساحة الكلية التي تغطيها الكيلومترات المربعة.
## طريقة
خوارزمية NDSI نفسها بسيطة جداً (تظهر أدناه في معادلة 1.1 - عادي مؤشر فرق الثلوج (NDSI)) والخطوات اللاحقة المطلوبة لاستخراج الغطاء الثلجي في تنسيق متجه ، تفسح المجال بشكل جيد لطراز صندوق أدوات المعالجة.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

ستعطي خوارزمية NDSI هذه نتائج بين -1 و 1 ، مع كون قيمة الحد الأدنى للثلج عادةً قيم أكبر من 0.4. يظهر مثال لخرج NDSI أدناه (خريطة 1.3 - ناتج NDSI) ، إلى جانب صورة طبيعية ملونة (خريطة 1.2 - MODIS لون حقيقي) في 13 يوليو 2014. كما يتضح من هذه الصور ، فإن خرج NDSI جيد جدًا في التمييز بين الثلج المناطق المغطاة من أنواع الغطاء الأرضي والغيوم الأخرى. ومع ذلك ، يمكن تصنيف أجزاء كبيرة من المسطحات المائية على أنها تساقط الثلوج ، بسبب المياه التي لها خصائص امتصاص في الجزء القريب من الأشعة تحت الحمراء في الطيف. تشير هذه الخاصية في NDSI إلى الحاجة إلى دمج قناع مائي في مرحلة ما في النموذج.

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

## النتائج / اختتام
يعد صندوق أدوات معالجة QGIS طريقة فعالة لأتمتة سير العمل مثل تصنيف الثلج هذا. يعمل النموذج المبين أعلاه على أتمتة عملية تصنيف الثلوج تلقائيًا ، ويقدم مجموعة بيانات GIS يمكن استخدامها للتصور والمدخلات في مزيد من التطبيقات الإحصائية. ينجح في إزالة الخطأ الذاتي للمستخدم المرتبط بالطرق السابقة المستخدمة من قبل SHL ، مع توفير أداة تصنيف متكررة ومتسقة. يمكن الاطلاع على بعض النتائج الموسمية هنا.
### المؤلف
أندرو جيفري هو محلل نظم معلومات جغرافية مع هيدرو ثلجي محدود مقرها في كوما نيو ساوث ويلز ، أستراليا. تخرج من جامعة تشارلز ستورت في Wagga Wagga مع بكالوريوس العلوم (Bsc) تخصص في أنظمة المعلومات المكانية في عام 2004. بينما كان في مجال الطاقة المائية الثلجية محدودة تمكن من تقديم الدعم المكاني للمشاريع المثيرة مثل تجربة السحب السحاب ، واليوم لعمليات اليوم داخل المنظمة.

{{<content-end >}}
