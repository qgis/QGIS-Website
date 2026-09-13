---
draft: 'true'

---
# QGIS في كومة FOSSGIS الحكومية في كانتون سولوتورن في سويسرا
![](./images/suisse_solothurn1.png){.align-left}

توفر كانتون سولوتورن خدمات وبنية تحتية لـ250.000 من مواطني سولوتورن. في عام 2001 قرر برلمان الولاية الهجرة من ويندوز إلى لينكس. كانت الدوافع مستقلة عن بائع معين ، لتشجيع المشاريع الحرة وخفض تكاليف الترخيص. ونتيجة لذلك ، بدأ قسم نظم المعلومات الجغرافية في كانتون سولوتورن تسليم متطلبات نظام المعلومات الجغرافية لأكثر من 3500 موظف باستراتيجية FOSSGIS.

كانت الخطوة الأولى التي اتخذناها هي تقديم UMN MapServer وإنشاء عميل SO SO يقدم خدمة WebGIS سهلة الاستخدام لجميع الموظفين 3500. كانت الخطوة الثانية هي نقل جميع بياناتنا الجغرافية من ملفات أشكال إلى محرك قاعدة البيانات المكانية PostGIS. كانت المقدمة ناجحة للغاية ، ولكن كان هناك نقص في استخدام GIS لسطح المكتب.

بعد تقييم مختلف نظم المعلومات الجغرافية المكتبي ، قررنا استخدام QGIS بالتزامن مع GRASS ، لتحل محل ESRI ArcInfo و ArcView3 في عام 2006.

كان الدافع وراء القرار من الجوانب التالية:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- OSGeo مشروع التنظيم
- واجهة المستخدم الرسومية المترجمة في اللغة الألمانية
- وثائق مكتوبة باللغة الألمانية
- مطور نشط (Marco Hugentobler) بالقرب من Solothurn في سويسرا.
- يمكننا أن نتعاقد مع ماركو هيوجنتبلر لتنفيذ ميزات مفقودة / ناقصة مثل Digitizing و Mapcomposing.
- تطبيق وتطوير البرنامج المساعد مع بايثون
- تزايد مجتمع المستخدمين
- مجتمع مطور نشط للغاية
- الاستقلال من نظام تشغيل واحد

## أين نستخدم QGIS
على النقيض من الخرائط التفاعلية التي يقدمها UMN MapServer ، فإن نظام GIS المكتبي يوفر عرضًا مرنًا في البيانات الجغرافية المكانية لـ Solothurn. يستخدم نظام GGIS Desktop GIS أكثر من 50 مستخدمًا للعمل اليومي. لكن الكثيرين منهم ليسوا خبراء في نظم المعلومات الجغرافية. انهم يريدون تصور و / أو التقاط البيانات الجغرافية المكانية مع واجهة مستخدم بديهية.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

تحتوي SO! DATA على مخزون يمكن قراءته من البشر لنماذج البيانات ويمكن لمستخدم غير GIS-Expert استخدام قاعدة البيانات هذه لاكتشاف المعلومات التي يحتاجونها.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## الخاتمة
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## المؤلف
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

ساهم هذا المقال في مايو 2009 من قبل الدكتور هورست دوستر. وهو منسق نظم المعلومات الجغرافية في قسم المعلومات الجغرافية في كانتون سولوتورن ، سويسرا.
