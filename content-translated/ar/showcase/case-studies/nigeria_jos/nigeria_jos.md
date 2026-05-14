---
draft: 'true'

---
# موطن احتياطي الغابات في الأمورا ورسم خرائط الأفيون مع QGIS في نيجيريا
يقع محمية الغابات Amurum بالقرب من مدينة جوس ، ولاية بلاتو ، نيجيريا. وقد تم تأسيسه بالتزامن مع بدء معهد A.P. Leventis لأبحاث علم الطيور (APLORI) بغرض الحفاظ على الطبيعة والتعليم والبحث. تستضيف APLORI قسم علم الحيوان في جامعة جوس ، حيث تقوم مجموعة من حوالي ثمانية طلاب متحمسين من جميع أنحاء نيجيريا بالحصول على تدريب في علم أحياء الحفظ والإحصاءات (مع R) وكذلك في نظم المعلومات الجغرافية لعام 2011. خلال أسبوعين في ديسمبر 2011 قمنا بدراسة مفاهيم نظم المعلومات الجغرافية الأساسية وتطبيقها مع QGIS لأغراض الصيانة المختلفة. في هذه المقالة وصفنا الطريقة التي استخدمنا بها QGIS لرسم خرائط الموائل ومحددات احتياطي Amurum وكيفية استخدام خرائط الموائل الأساسية للحصول على طبقات لغرض تحديد التوزيع المكاني لل avifauna بما في ذلك التنوع البيولوجي بشكل فعال.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## رسم خريطة للارتفاع ورأس التل والمنحدر والموائل
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) تم استخدام GdalTools لدمج مجموعات البيانات الأصلية ولشبكة منطقة أصغر تحتوي على الاحتياطي بحيث تبقى مجموعات البيانات النقطية صغيرة نسبيًا. عن طريق GPS قمنا بجمع الارتفاعات في مواقع مختلفة في المحمية.
3) وبشكل عام ، كانت ارتفاعات مجموعة بيانات SRTM متوافقة بشكل جيد مع الارتفاعات التي تم جمعها عن طريق النظام العالمي لتحديد المواقع. استخدمت نماذج التضاريس في GdalTools لحساب هضاب التلال والمنحدرات للمنطقة. هذه المتغيرات مهمة من وجهة نظر بيئية لأنها ترتبط بشدة بنوع الموطن.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) بما أننا نعتزم تطوير خريطة ذات مظهر جيد ، فقد قمنا بتحويل خريطة الارتفاع الأصلية (المقطوعة) للحصول على خريطة دقة أعلى. استخدمنا أداة الاعوجاج في GdalTools. من خلال أداة الكفاف ، حصلنا على خطوط محيطية ناعمة.
5) تم الحصول على إحداثيات حدود المحمية عن طريق المشي على طول حدود المحمية مع نظام تحديد المواقع. تم استيراد نقاط الطريق والمسارات المخزنة في GPS بسلاسة باستخدام أدوات GPS. تم استخدام نقاط الطريق والمسارات المستوردة لبناء صورة مضلعة. تم تعيين المسارات داخل المحمية بطريقة مماثلة.
6) تمكنا من إنشاء خريطة موئل Amurum بسرعة ودقة باستخدام صورة القمر الصناعي من Google التي وصلنا بها إلى مساحة العمل مع المكون الإضافي Openlayers. يحتوي المحمية على ثلاثة أنواع من الموائل المميزة: سافانا وغابة غاليري وروكي بروب. على أساس صورة الأقمار الصناعية استخدمنا المحرر لرسم مضلعات ترسيم الموائل الثلاثة. سمح إعداد خيارات الالتقاط بشكل صحيح ببناء مضلعات غير متراكبة.

## رسم خرائط توزيع الطيور وتنوعها
تم استخدام خرائط الموائل لإنشاء مواقع عشوائية. استُخدمت منطقة الأنواع المختلفة من الموائل لتوليد عدد من المواقع متناسبة مع سطح كل نوع من الموائل (التقسيم الطبقي).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## الخاتمة
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## المؤلف
أبنجوي الموند Chiadikaobi ، Adeyanju Temidayo Esther ، Akiemen Nerioya ، Albert Malangale Tauje، Azi Abok Joel، Echude Daniel، Eelke Folmer، Nwaogu Chima Josiah، Onoja Joseph Daniel، Yadok Biplang Godwill
