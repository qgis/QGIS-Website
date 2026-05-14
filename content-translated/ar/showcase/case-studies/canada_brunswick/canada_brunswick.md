---
draft: 'true'

---
# إنشاء خريطة مسار ممر فاوندي مع QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

تم إنشاء المسار ، والحفاظ عليه ، والترويج له من قبل مجموعة من المتطوعين المعروفة باسم Fundy Hiking Trail Association Inc. (FHTA) (1975). كمنظمة غير ربحية ، تجمع منظمة FHTA الأموال لأنشطتها من خلال بيع أدلة إرشادية تتضمن خريطة درب. في عام 2011 ، اتصلت بمنظمة FHTA للتطوع لتحديث خريطة المسار الرسمي. كمتطوع إنشاء خريطة لمنظمة غير ربحية QGIS تناسب الفاتورة كأداة لتحرير البيانات والتخطيط النهائي للخريطة. من خلال الجهود التي بذلتها أنا وأعضاء جمعية "FHTA" ، تم إنشاء الخريطة الرسمية الجديدة لممشى "فوندي فوت" المتضمنة في الدليل من البداية إلى النهاية مع QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## المشروع
يمكن تقسيم عملية إنشاء خريطة Fundy Footpath الجديدة مع QGIS إلى ثلاثة أجزاء مختلفة:
- جمع البيانات.
- تحرير البيانات والتحضير.
- إنتاج الخرائط.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

لإعداد البيانات للاستخدام في المنتج النهائي للخريطة ، تم استخدام الأدوات التالية داخل QGIS لإنجاز مهام محددة:
- تم تنظيف البيانات التي تم جمعها باستخدام نظام تحديد المواقع العالمي باستخدام شريط أدوات التحرير.
- تم دمج بيانات المتجه التي تم الحصول عليها من NRCan و SNB معًا ، وتم الاستعلام عنها ، وتم قصها لمنطقة الخريطة النهائية باستخدام أدوات المتجه.
- تم استيراد ملف مفصول بفواصل تم الحصول عليه من SNB إلى QGIS كطبقة نقطية باستخدام إضافة Add Layim Text Layer ، تم استخدام ملحق Interpolation لإنشاء خطوط المسح النقطية التي تم استخدامها بعد ذلك لإنشاء خطوط المسح النقطي وطبقة كفاف الارتفاع مع GDAL أدوات النقطية المساعد.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## الخاتمة
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## الروابط
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## المؤلف
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

ساهم في هذه المقالة  Jarrett Totton في يناير 2013. جاريت هو تقني نظم المعلومات الجغرافية يعيش في ألبرتا ، كندا.
