---
draft: 'true'

---
# استخدام وحدة تحكم بيثون لإعداد خريطة دون اتصال من WMS (تنزيل البلاط)
تشرح هذه الدراسة كيفية إعداد الخرائط دون اتصال من WMS / WFS أو أي خريطة محملة في عرض خريطة QGIS عن طريق تنزيل البلاط بمساعدة برنامج نصي في وحدة تحكم python. كما يولد skript فسيفساء من جميع البلاط لمزيد من الاستخدام.

يعتبر الوصول إلى الخرائط النقطية / الموجهة من خلال خدمة خدمة خرائط الويب (WMS) شائعًا جدًا وفعالًا. لديها العديد من المزايا مثل الأمن ، وأنماط خريطة مركزية ومرنة. مثال على ذلك خرائط جوجل ، ياهو ، بنج ، موديس ، لاندسات ، خرائط نشرتها ناسا ، إن آر سي إس (الهند). عيب / الحد من WMS هو أنه يعمل عبر الإنترنت أو الإنترانت. قد لا يكون من الممكن الحصول على اتصال بالإنترنت دائمًا على وجه الخصوص في المجال أثناء الاستبيان. كما يعمل WMS بطيئًا مقارنةً بأي تنسيق صور غير متصل بالإنترنت مثل GeoTiff و jpg و img وما إلى ذلك.
## استخدام QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## وحدة التحكم بيثون
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. X ، Y إحداثي (أعلى يسار وأسفل يمين) من البلاط الأول
2. حجم التجانب المراد تنزيله (على سبيل المثال ، 0.001 × 0.001 درجة)
3. عدد البلاطات المراد تنزيلها (محسوبة على أساس المدى الكامل للخريطة وحجم البلاط)
4. دليل الإخراج لتخزين بلاط / ملفات الإخراج

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

توجد قيود على هذه الطريقة ، حيث لن تظهر التغييرات في الخريطة عند نهاية الخادم في وضع عدم الاتصال (خريطة تم تنزيلها). في هذه الحالة ، سيتعين على المستخدم تكرار العملية وإنشاء خريطة جديدة دون اتصال بالإنترنت. القيد الثاني هو خريطة حاليا خلق سيتم تنسيق الصورة. لا يمكن استخدامه لرسم الخرائط المواضيعية أو تصنيف الصور. مع بعض الجهود الإضافية يمكن تحويل بعض خرائط الأراضي إلى متجه مع فقدان بعض البيانات.
## نطاق
الفسيفساء المتولدة هي صورة نقية حتى لو تم تنزيلها من الخريطة الموضوعية (7-8 لون). باستخدام أداة متقدمة مثل إعادة التصنيف ، يمكن تحويل هذه الطبقة النقطية إلى هذا المتجه إلى متجه مضلع. يحتوي WMS على عدة طلبات مثل getcapabilities و getmap و getfeatureinfo إلخ. يمكن استرداد معلومات سمة getgeatureinfo لكل مضلع. يمكن تحويل النص البرمجي إلى مكون إضافي بحيث يتمكن أي شخص بدون معرفة البرمجة النصية من استخدام النص البرمجي. ...
## الخاتمة
توضح التجارب السابقة أنه يمكن استخدام QGIS على أي مستوى متقدم. مع مهارات البرمجة الأساسية يمكن للمرء كتابة نص صغير أو برنامج إضافي لتحسين جودة العمل وتوفير الوقت. داخل QGIS ، الوصول إلى مستودع من المكونات الإضافية المتقدمة في جميع أنحاء العالم هو أفضل من QGIS. يعتبر PyQGIS Developer Cookbook موردًا رائعًا لكتابة برنامج نصي ، ومعالجة البيانات النقطية أصبحت سهلة الآن بمساعدة أدوات GDAL.
## المؤلف
تم تقديم هذه المقالة في مايو 2014 من قبل براشانت كادجي ، ومقرها في بيون (الهند) ، وتعمل حاليًا كمستشار في خدمات الاستشارات التطبيقية لـ GIS. منذ عام 2009 يستخدم GIS & RS في NRM ، والغابات ، والحكم الإلكتروني ، ومشاريع تطوير البرمجيات في مناطق مختلفة من الهند والعالم.
- Contact: <kadgiprashant@gmail.com>
- الموقع www.gisappco.com (تحت الإنشاء)
