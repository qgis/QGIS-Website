---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: المشروع
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: استخدام QGIS في فريق الرسومات وقت المالية
type: case-study

---
{{<content-start >}}
# استخدام QGIS في فريق الرسومات وقت المالية
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2016</span>
</p>

## مقابلة مع ستيفن برنار (محرر التصميم التفاعلي)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

** QGIS **: ستيفن ، ما هو اسم الفريق الذي تعمل به في FT؟ هل يمكنك تزويدنا ببعض المعلومات حول ما يقوم به فريقك في FT؟

** ستيف **: فريقنا في فترة انتقالية في الوقت الحالي ، لدينا محرر جديد لتصور البيانات ، ألان سميث OBE (سابقًا لـ ONS) الذي يهز الأمور وينشئ فريق رسومات واحد. تقليديا كان لدينا فريق رسومات الويب وفريق رسومات الطباعة. سيكون فريق الطباعة مسؤولاً عن جميع الرسومات الصحفية بالإضافة إلى إنشاء نسخ متوافقة مع الويب. كان فريقي مسؤولًا عن جميع محتوى الويب فقط ، بالإضافة إلى العمل عن كثب مع المنتجين / المطورين التفاعليين في تصميم الرسومات التفاعلية.

سيسمح الفريق الذي تم تكوينه حديثًا بتبادل المهارات بين وسائل الإعلام المختلفة.

قدم آلان سير عمل رقمي واحد لفريقنا ، بما في ذلك استخدام d3 للمساعدة في إنشاء مفردات رسومات أكبر وتقليل الوقت المستغرق لإنشاء العناصر المرئية.

![](../images/ft_europe_migration_balkan-route.png)

* مثال: تدفقات المهاجرين. طريق غرب البلقان.

** QGIS **: كم عدد زملاء العمل في فريقك؟

** Steven**: بما في ذلك جميع المصممين والمطورين والمنتجين والإحصائيين لدينا فريق من 24

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](../images/ft_nigeria-migration_animation.gif)

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](../images/ft_gotthard-tunnel.png)

* مثال: سكة حديد جوتهارد ونفق الطرق في جبال الألب السويسرية. *

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

** QGIS **: كيف اكتشفت QGIS؟

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](../images/ft_blm-federal-land-map.png)

* مثال: الأراضي العامة في الولايات المتحدة. *

** QGIS **: ما هي الأدوات الأخرى التي تستخدمها بجانب QGIS وكيف يمكنك الجمع بينها؟

** ستيفن **: إذا كان مجرد خريطة لتحديد المواقع مباشرة ، يتم إجراء 95٪ من العمل في QGIS ، مع إجراء التلميع النهائي في Adobe Illustrator.

إذا قمت بعمل خريطة إغاثة ، فإن العملية أكثر تعقيدًا بكثير. سأقوم باسترجاع ملفات DEM من برنامج ناسا إيرث إكسبلورر ، وإحضارها إلى QGIS لتقسيمها إلى حجم. سوف أقوم بعد ذلك بخلع علامة DEM الممزوجة إلى خلاط لإنشاء عرض ثلاثي الأبعاد. إذا كنت أستخدم تراكب الأقمار الصناعية على hillshading ثم سأقوم بتحميل صورة BlueMarble من ناسا وتأخذ هذا إلى خلاط. يتم بعد ذلك إعادة عرض المصدر الذي تم تصديره من Blender إلى QGIS لاستخدامه كطبقة خلفية. أنا قد قرص عليه في Photoshop مسبقا إذا لزم الأمر.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

هناك أداة أخرى مفيدة هي Google My Maps التي تتيح للمراسلين في جميع أنحاء العالم وضع علامة على المواقع على الخريطة ، وبعد ذلك يمكننا تنزيلها كملف kmz واستيرادها مباشرة إلى QGIS.

الأداة الأخيرة التي أستخدمها هي Adobe After Effects حيث أنني قمت مؤخرًا بتحريك خرائطي لأخذ المستخدم في رحلة. كما هو مستخدم في سلسلة لاند راش في الآونة الأخيرة:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

** QGIS **: هل تستخدم أدوات مكانية أخرى أو GIS إلى جانب QGIS ، وإذا كانت الإجابة بنعم ، فما هي تلك؟

** ستيفن **: QGIS على طول الطريق بالنسبة لي ، ولكن كما ذكر أعلاه بعض زملائي استخدام خريطة الناشر كذلك.

![](../images/ft_isis-air-strikes_febupdate.png)

* مثال: الإضرابات على سوريا في فبراير 2016. *

** QGIS **: هل يمكنك وصف نقاط القوة والضعف في QGIS فيما يتعلق بالمهام التي عليك القيام بها؟

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

خلال أسبوعين تقريبًا ، كنت مقتنعاً بأنها ستكون قابلة للتطبيق. كانت نقطة البيع الرئيسية هي القدرة على إعداد أدلة للأسلوب لكل شيء ، بما في ذلك تصميم مستوى التكبير / التصغير للخرائط على مستوى الشارع.

لدي نظام تم إعداده بحيث يكون لدينا مجموعات من جداول Google تحتوي على أعمدة للاسم ، و lat ، و long ، و marker-icon ، و fontweight ، و fontsize ، وما إذا كنت تريد أن تكون العلامة مرئية أم لا.

رمز العلامة عبارة عن قائمة منسدلة متصلة بجدول vLookUp الذي يملأ جميع تفاصيل تلك العلامة.

كل ما علي فعله هو تنزيل ملف csv واستيراده إلى QGIS وتطبيق نمط ولدي خريطة جاهزة 95٪.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](../images/ft_chinaMigration.png)

* مثال: الجذب الحضري والهجرة داخل الصين. *

** QGIS **: ما هي المفاهيم أو الميزات التي تفضلها أكثر في QGIS؟

** ستيفن **: هناك العديد من الميزات التي أود تصنيفها كمدربات إنقاذ! ولكن في البداية ، وفر لي نظامي Quick OSM و Georeferencer الكثير من الوقت ، وهذا ضروري للغاية عندما تكون المواعيد النهائية ضيقة. والذي ، عند العمل في مؤسسة إخبارية ، يكون عادة 90٪ من الوقت.

![](../images/ft_china_henanGuangdong.png)

* مثال: الجذب الحضري والهجرة داخل الصين. مشاهدة التفاصيل. *

** QGIS **: ما هي الميزات أو الوظائف في QGIS التي تفتقد أكثر؟ هل لديك قائمة بالميزات المفقودة التي من شأنها مساعدتك كثيرًا إذا تم تنفيذها؟

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

القدرة على حفظ كصورة بأحجام ملفات أكبر. حالياً هذه هي الطريقة الوحيدة التي يمكنني بها إنشاء اقتصاص من ملف DEM يتم نقله جغرافيًا إلى Blender. لكنه يقتصر على حجم الشاشة. إذا كان لدي ملف DEM 8000 بيكسل تم تحميله في QGIS ، فأنا أود أن أتمكن من تصدير المحصول بحجم أكبر من الشاشة الخاصة بي للاستخدام في الفيديو عالي الدقة على سبيل المثال.

** QGIS **: إذا فقدت بعض الميزات في QGIS التي من شأنها مساعدتك - هل تفكر في تحسين QGIS بنفسك (مع الترميز في المكونات الأساسية QGIS أو Python) ، أو قد تفكر في استئجار مطور QGIS لتنفيذ الميزة المفقودة لـ أنت؟ أو هل ستبحث بدلاً من ذلك عن أدوات أخرى لملء هذه الفجوة؟

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](../images/ft_us_broadband_internet_subscription.png)

* مثال: النسبة المئوية للأسر ذات الاشتراك في الإنترنت ذات النطاق العريض في الولايات المتحدة. *

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

** QGIS **: شكرا لك على وقتك والعمل الذي تقوم به لتعزيز وتوثيق مهام سير العمل في QGIS!

![](../images/ft_potrait_steve_bernard.jpg)

* صورة لستيف برنارد. محرر التصميم التفاعلي في الأوقات المالية. *

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

أسئلة المقابلة بواسطة A. Neumann و T. Sutton. نيسان 2016.

{{<content-end >}}
