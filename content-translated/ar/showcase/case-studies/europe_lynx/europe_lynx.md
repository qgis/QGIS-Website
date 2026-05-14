---
draft: 'true'

---
# تحليل الموائل الوشق في الكاربات الجنوبية
دراسة حالة لتعزيز الفهم الأساسي لنمذجة موائل الحياة البرية للطلاب استنادًا إلى بيانات مفتوحة المصدر.
## المقدمة
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## المنهجية
تمت معالجة جميع البيانات التي تم جمعها مع QGIS 2.6 و 2.8 ، مسقطة في ETRS89 / ETRS-LAEA وتخزينها وفقا لتوجيه INSPIRE لتلبية معايير الاتحاد الأوروبي. تم تعريف وتطبيق فهرس منفصل للأوزان ** بشكل عام على جميع بيانات المدخلات.

![Figure 1: Workflow - Lynx habitat expert model](./images/europe_lynx1.png)

** وصف سير العمل **
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

* ملاحظة: تم تصنيف الطبقات غطاء الأرض من الممكن حدوث الوشق والنشاط البشري. على الرغم من أنه من الناحية التقنية من أصل قديم ، فقد تم دمج المعلومات المتعلقة بقيم الغطاء الحراجي للإشارة إلى تحسين الموائل وكمثال عام للانضمام إلى مجموعات البيانات المكانية *
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
    
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```

```
    .
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
    
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
    
* ملاحظة: يشير نموذج إمكانية الوصول إلى هانتر إلى انخفاض احتمال دخول الصيادين إلى المنطقة عن طريق المزيد من المسافة إلى الطرق وزيادة ميلها *

![Figure 2, 3 and 4](./images/europe_lynx2.png)
## الخاتمة
بالنظر إلى الناتج النهائي (الشكل 3) ، بدا أن تحليل الموطن المحتمل الأول كان ناجحًا ، ولكن الأهم من ذلك أن النماذج الأساسية نفسها تبين أنها أقل صعوبة مما كان متوقعًا في البداية. وقد أتاح لنا اختيارنا لإضافة نموذج فرعي يتيح لنا الوصول إلى الصيادين تنفيذ بُعد آخر من حيث تقييم مخاطر الموائل ، والذي يمكن دمجه ببساطة في السيناريو القائم حاليًا واستخدامه لتحديد ضرورات الحماية في جوانب مثل. تطوير البنية التحتية. ومع ذلك ، فإن بعض المعلومات الحيوية للموائل ، مثل هيكلية الغابات (أعلى ملاءمة للموئل) لا يمكن اشتقاقها من خلال مجموعات البيانات المتاحة وبالاقتران مع سلوك الأنواع المعقدة ، يجب بالتالي فهم النتيجة على أنها أساسية وغير كاملة. هناك عوامل إضافية لم يتم تنفيذها في هذه المرحلة تتمثل في الوفيات على الطرق ، وخشونة التضاريس الأرضية ، وحدوث فريسة مفصلة.

إلى جانب مصدرها المفتوح ، الشخصية المجانية المتاحة ، كان برنامج QGIS موضوعًا للتطورات الرئيسية في السنوات الأخيرة. لقد حققنا تجربة إيجابية للغاية مع تكامل صندوق الأدوات ، مما سمح باستخدام أدوات GRASS و SAGA المختلفة ، حتى للمستخدمين غير المتمرسين. لم تحدث مشكلات توافق على الرغم من التغيير المتكرر بين الإصدارات المختلفة والغياب العام للقيود الإدارية يمكن أن يكون ميزة قوية عند العمل بشكل بديهي مع مجموعات البيانات. نحن نتطلع إلى رؤية المزيد من التحسينات ، خاصة فيما يتعلق ببناء النماذج المتكاملة.
## المراجع
- Kaczensky، P.، Chapron، G.، von Avrx، M.، Huber، D.، Andrén، H. & Linnell، J. (December 2012): Status، management and distribution of large carnivores in Europe. وثيقة المفوضية الأوروبية.
- Schadt، S.، Revilla، E.، Wiegand، T.، Knauer، F.، Kaczensky، P.، Breitenmoser، U.، Bufka، L.، Cerveny، J.، Koubek، P.، Huber، T.، Stanisa، C. & Trepl، L. (2002): تقييم مدى ملاءمة المناظر الطبيعية في أوروبا الوسطى لإعادة تقديم الوشق الأوروبي الآسيوي. مجلة علم الايكولوجيا التطبيقية.
- Salvatori، V. (2004): Conservation areas for large can carvivores in the Carpathian Mountains. رسالة الدكتوراه.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros، D. (March 2002): توصيف وتقييم ملاءمة
 oras eurasian lynx (Lynx lynx) den sites. تقرير KORA رقم 12e ، أطروحة الدبلومة.

### المؤلف
أنجيلا ديشتي ولوكا إهرمنغر وسيلفانا جارسيا ترافيسي رييس وتوبياس هوب وديفيد وينجر طالبان في الفصل الرابع من برنامج الدراسة الدولي للغابات في إدارة الأنظمة البيئية ، آن غنيلك على التوالي الغابات الألمانية وهنري هيلتينن طالب تبادل من جامعة ميكيلي التطبيقية العلوم ، فنلندا. يحاضر الأستاذ موند في نظم المعلومات الجغرافية والاستشعار عن بعد في HNE Eberswalde منذ عام 2010 وقدم التوجيه والدعم الفني للمشروع.

يرجى الاتصال بـ Luca.Ehrminger (at) hnee.de، David.Winger (at) hnee.de، or Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund (at) hnee.de لمزيد من المعلومات.
