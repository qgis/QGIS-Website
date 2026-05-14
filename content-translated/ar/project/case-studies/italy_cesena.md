---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS لوصف جدار تشيزينا
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

تم إنشاء جامعة ECAMPUS كجامعة على الإنترنت ومعترف بها من قبل وزارة التعليم الإيطالية والجامعة والأبحاث (MIUR) بموجب المرسوم الوزاري الصادر في 30 يناير 2006. تم تشكيلها بهدف توفير إمكانية الوصول إلى الجامعة من خلال منصة التعلم الإلكتروني الخاصة بها إلى الشباب الناس والمهنيين ورجال الأعمال والمديرين التنفيذيين والجهات الفاعلة في الأعمال والثقافة من أجل المساهمة في سوق العمل. يقع المقر الرئيسي ، المعروف أيضا باسم الحرم الجامعي الدولي في ميلانو ، أو Campus of Novedrate ، في مركز تدريب IBM السابق لشركة Novedrate (Como ، إيطاليا) ، في حرم جامعي في منطقة Brianza الخضراء الهادئة.

الجامعة لديها 5 كليات افتراضية: الهندسة ، الاقتصاد ، علم النفس ، الفنون ، القانون. الخرائط التاريخية ومشروع QGIS يميز سور المدينة بمدينة تشيزينا. يقسم شكل العقرب المركز التاريخي من المنطقة الحديثة.

تصف وثائق الخرائط التاريخية تطورها وتدميرها. يسمح برنامج QGIS بمقارنة الخرائط التاريخية المختلفة ، لأنها تسمح بنقل جميع الخرائط في نفس النظام المرجعي ، مع البرنامج المساعد للربط بالإحداثيات الجغرافية. كمرجع ، تم استخدام طبقة مفتوحة Google Satellite والطبقة المفتوحة Open Street Map لإحالة جميع الخرائط التاريخية إلى نظام المرجع EPSG: 3857 (Web Mercator أو Pseudo Mercator).

لقد كانت QGIS أداة أساسية لوضع هذه الخرائط ذات الأبعاد الجغرافية وتحليلها ومقارنتها من خلال الطبقات المتجهية أو ملفات الحواف ، والتي حفظت فيها جميع عناصر الخرائط ، مثل الطرق والمباني والحدائق والحدائق وسور المدينة والأبراج المحصنة القديمة المدينة القديمة. لقد استخدمت طبقات puntual وخطية ومضلعة. قارنت هذه الطبقات من خلال أدوات التحليل والبحث والمعالجة الجيولوجية والهندسة وإدارة البيانات (الشكل 1).

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

باستخدام هذه الأدوات ، حصلت على معلومات حول:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- التغيرات المورفولوجية لحائط المدينة ، مثل هدم أبراجها القديمة المحصنة ومدينة جيتس القديمة ؛
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

هناك الكثير من أدوات QGIS ، وقد استخدمت بعضًا منها لإنشاء:
- الروابط التي تربط كل قسم من الطبقة الخطية لجدار المدينة الحالي بالصور التي تمثل الحالة الفعلية للحفظ ؛
- خريطة تشيزينا في القرن 19 من خلال مؤلف الطباعة.
- نموذج ثلاثي الأبعاد من تشيزينا مع البرنامج المساعد qgis2threejs (الشكل 3) ؛

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## الخاتمة
تعد الخرائط التاريخية وثائق مهمة حتى إذا لم يكن من الممكن مقارنة دقتها بدقة وثيقة الخرائط الفعلية ، كما أنها تمثل أيضًا تمثيلات التواصل بالنسبة لأولئك الذين ليسوا متخصصين في التمثيل الجغرافي. كانت QGIS هي الوسيلة الوحيدة التي سمحت لي باستخدام المحتوى الرقمي للخرائط التاريخية وفقا لتمثيل فعال وذي معنى.
## فهرس ببليوغرافي
تم استخراج الخرائط التاريخية بواسطة:
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

تم استخراج المعلومات التاريخية من خلال:
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## المؤلف
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
