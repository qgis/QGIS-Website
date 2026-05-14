---
HasBanner: false
archived: true
date: 2015-03-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/italy_igag1.png
title: نموذج المعالجة الجغرافية QGIS لتبسيط تحليل microzonation المستوى الأول الزلزالي
type: case-study

---
{{<content-start >}}
# نموذج المعالجة الجغرافية QGIS لتبسيط تحليل microzonation المستوى الأول الزلزالي
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2015</span>
</p>

The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- الكيمياء الجيولوجية البيئية ومعالجة التربة والمياه الملوثة ؛
- الرواسب المعدنية ومعالجة المعادن ، بما في ذلك معالجة مياه الصرف ؛
- الهندسة الجيولوجية وسلامة الحفريات الصخرية ؛
- Recent geological evolution;
- تخفيف المخاطر الطبيعية ؛
- علم الآثار الجيولوجية وعلم الآثار.
- الجيولوجيا البحرية
- جيوماتكس ، تحليل وتطوير نظم المعلومات الجغرافية.

إن دراسة الزلازل الزلزالية من المستوى 1 لمنطقة Pietramontecorvino (بوليا ، جنوب إيطاليا ، الواقعة على طول سلسلة Apennine الوسطى الجنوبية) هي جزء من مشروع ، بالتعاون مع سلطة Basul of Apulia (Puglia AdB) وقسم الجيولوجيا والجيوفيزياء (DGG) من جامعة باري ، تهدف إلى microzonation الزلزالي من 63 بلديات في منطقة فوجيا. تم الترويج للنشاط من قبل وزارة الحماية المدنية الإيطالية (DPC) وتم تمويله من قبل اللجنة الوزارية للتخطيط الاقتصادي (CIPE n. 20/2004).
## أداة المعالجة الجغرافية QGIS للدراسات المرحلة الأولى من الزلازل السيزمية
تقوم عملية التكليف الزلزالي بتقييم الخطر الزلزالي على المستوى المحلي المقترح لتحديد المناطق التي تتميز بالسلوك الزلزالي المتجانس. المستوى الأول من microzoning الزلزالي لديه الغرض من تحديد الخصائص الحجرية وهندسة الوحدات الجيولوجية التي تميز هذه الأجزاء من الأراضي (المناطق الجزئية).

إن ملاحظة الأضرار الناجمة عن الزلزال غالباً ما تظهر اختلافات على المستوى المحلي لا تتسبب فقط في الهياكل الجيولوجية ولكن أيضاً بجودة ونوع المباني المختلفة ، مما يؤدي إلى مخاطر زلزالية مختلفة.

تقوم عملية التكليف الزلزالي بتقييم المخاطر الزلزالية المحلية ، من خلال تحديد المناطق التي تتميز بالسلوك الزلزالي المتجانس.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

المستوى الأول من الزلازل السيزمية يتكون من إنشاء ثلاث خرائط موضوعية:
1. خريطة المسح التي تحتوي على استطلاعات لدراسات الزلازل السيزمية
2. خريطة جيولوجية-ليطولوجية ، تم الحصول عليها من خرائط جيولوجية جيولوجية أو جيومورفولوجية مفصلة ، تضم البيانات الحالية الصخرية والطبقية والجيوتقنية المتعلقة بالمسوح.
3. خريطة المستوى 1 للزلازل الزلزالية (المنتج الرئيسي للمستوى 1 من المستوى المصغر) ، وتحديد المناطق الجزئية في ثلاث فئات من المخاطر المحلية:
   - مناطق مستقرة
   - المناطق المستقرة عرضة لتضخيم الأرض ؛
   - مناطق غير مستقرة.

يتمثل نطاق هذا العمل في المساهمة في وضع منهجية لمعالجة البيانات الطوبوغرافية والجيولوجية والجيوفيزيائية والجيولوجية التقنية التي تهدف إلى صياغة مخطط خريطة زلزالية للأرصدة السيزمية من المستوى 1، من خلال استخدام أدوات مفتوحة المصدر

تم استخدام أداة Graphical Modeler المدمجة في أحدث إصدار من QGIS (2.8.1 اعتبارًا من الكتابة) لإنشاء نموذج بسيط للمعالجة الفيزيائية. هذه الأداة مفيدة لأتمتة واحد من التحليل الذي يتم إجراؤه عادة لإنشاء خرائط microzonation من المستوى 1 الزلزالية ، وخاصة لتحديد المناطق غير المستقرة كخصائص مضلع.

يستفيد هذا النموذج من البرامج والمكتبات المختلفة المفتوحة المصدر (GRASS و GDAL و QGIS) ، مما يدل على فائدة نظام QGIS كواجهة مبسطة وموحدة للأدوات غير المتجانسة من GFOSS (البرمجيات الحرة والمفتوحة المصدر) (الشكل 1).

<figure>
<img src="../images/italy_igag1.png" class="align-right" alt="italy_igag1.png" />
<figcaption>(Fig. 1) Screenshot from the geoprocessing model.</figcaption>
</figure>

يأخذ النموذج كمدخل (الشكل 2):
- A shapefile من خطوط الكنتورية التي تحتوي على حقل مع قيم الارتفاع ؛
- The name of the field containing elevation values;
- الدقة النقطية المطلوبة بالأمتار لـ DEM و Slope (الافتراضي 10) ؛
- سيتم استخراج صورة مضلعة من مناطق تتقاطع مع منحدر أكبر من 15 درجة.
- اسم طبقة المضلع الناتجة.

<figure>
<img src="../images/italy_igag2.png" class="align-right" alt="italy_igag2.png" />
<figcaption>(Fig. 2) Model input form (left) and execution log (right).</figcaption>
</figure>

عند البدء ، ينفذ النموذج العمليات التالية:
- تقوم أداة GRASS v.to.rast.attribute بتحويل خطوط الارتفاع الكنتورية إلى خطوط المسح ، مع أخذ شكل الكفاف ، اسم الحقل z ودرجة الدقة النقطية كمدخل ؛
- تقوم أداة GRAS r.surf.contour بتوليد نموذج الارتفاع مع الأخذ في الاعتبار الناتج المؤقت النقطي من الخطوة السابقة ودقة البيانات النقطية ؛
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- يتم استخدام r.mapcalculator أداة GRASS لإنشاء مناطق تعريف نقطية 1 بت منحدر أكبر من 15 درجة (يتم ترميز هذه القيمة في إرشادات microzonation ، وبالتالي يتم إصلاحها) ، باستخدام التعبير:

if(A\>15,1,null())

حيث A هي المنحدر المؤقت الذي تم إنشاؤه بواسطة gdaldem ؛
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

والنتيجة هي طبقة مضلع ذات مناطق عرضة لعدم الاستقرار بسبب قيمة ميل أكبر من 15 درجة ، يتم استخراجها أوتوماتيكياً من خريطة مواضيعية مثل طبقة مضلعة من الانهيارات الأرضية (الشكل 3) أو خريطة ليترولوجية.

<figure>
<img src="../images/italy_igag3.png" class="align-right" alt="italy_igag3.png" />
<figcaption>(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).</figcaption>
</figure>

## الخاتمة
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## المراجع
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## المؤلف
ساهم هذا المقال مارس 2015 من قبل جوزيبي Cosentino وفرانشيسكا بينيكا (www.igag.cnr.it).

<figure>
<img src="../images/guiseppe_cosentino.png" class="align-left" height="200" alt="guiseppe_cosentino.png" />
<figcaption>Giuseppe Cosentino</figcaption>
</figure>

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

<figure>
<img src="../images/francesco_pennica.png" class="align-left" height="200" alt="francesco_pennica.png" />
<figcaption>Francesco Pennica</figcaption>
</figure>

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.

{{<content-end >}}
