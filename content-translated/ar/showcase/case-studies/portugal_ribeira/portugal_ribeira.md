---
draft: 'true'

---
# QGIS و GRASS لنمذجة ممرات إيكولوجية للذئاب في شمال البرتغال
The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

![Study area in Portugal](./images/portugal_ribeira1.png){.align-right}

ريبيرا دي بينا هي بلدية في منطقة فيلا ريال في شمال البرتغال. وهي بلدية ريفية ، تتميز بالزراعة ورعي الماشية والغابات والجبال والوديان والحيوانات المتنوعة ، إلى جانب الكثافة البشرية المنخفضة ، التي توفر المأوى والغذاء للذئاب. تقع ريبيرا دي بينا في منطقة انتقالية بين جبال Trás-os-Montes القاسية والجبلية و Minho الخضراء ، وهي واحدة من البلديات التي يمكن أن تعمل كممر إيكولوجي بين مناطق ذات تركيز أعلى للذئاب في الشمال مع تركيز أقل في جنوب.

بدأت باستخدام برنامج نظم المعلومات الجغرافية خلال دورة البيولوجيا الخاصة بي ، وكثيرا ما كان ذلك خلال أطروحة الماجستير. في ذلك الوقت كنت تستخدم أساسا البرمجيات الاحتكارية. بعد أن أنهيت درجة الماجستير ، فقدت الوصول إلى البرمجيات الاحتكارية.

وفي الوقت نفسه ، دخلت في عالم جديد من لينكس. بعد ذلك تم الاتصال بي لمساعدة بعض الباحثين على تصميم ممرات إيكولوجية للذئاب في ريبيرا دي بينا ، باستخدام نظام المعلومات الجغرافية ، لأنهم لم يعملوا أبدًا مع هذا النوع من البرامج. ولأنني كنت بالفعل أستخدم لينكس بدلاً من النوافذ ، كانت مشكلتي الأولى هي البرمجيات التي يجب استخدامها. ثم سمعت عن QGIS وقررت أن أجربها ، على الرغم من أنها تبدو مبسطة وغير كاملة ، بالمقارنة مع ما كنت أعرفه بالفعل. أدركت بسرعة كم كنت مخطئا ، وحصلت على حماسة فعلاً بالقدرات التحليلية التي توفرها QGIS ، خاصة مع تكامل GRASS.

لتصميم الممرات البيئية ، استخدمنا QGIS جنبا إلى جنب مع البرنامج المساعد GRASS. استخدمنا العديد من المعلومات الجغرافية إلى جانب بيانات التواجد الخاصة بالأنواع لنموذج الممرات البيئية. فيما يلي بعض وظائف كل من QGIS و GRASS المستخدمة في هذه الحالة ، على سبيل المثال لا الحصر:
- البرنامج المساعد الداخلي في QGIS: لإنشاء نموذج الارتفاعات الرقمية
- r.atershed في GRASS: لإنشاء تدفقات المياه من DEM
- r.grow.distance في GRASS: يولد طبقة خريطة المسح النقطي للميزات في طبقة المدخلات
- r.reclass في GRASS: لإعادة تصنيف طبقات الخريطة
- r.slope.aspect.slope في GRASS: لحساب الميل من DEM
- r.mapcalculator في GRASS: لحساب بعض الجبر خريطة بسيطة
- r.cost.coord في GRASS: يُنشئ خريطة نقطية تُظهر التكلفة التراكمية للتنقل بين المواقع الجغرافية المختلفة على خريطة مدخلات النقطية تمثل قيم فئة الخلايا الخاصة بها التكلفة
- r.drain in GRASS: Traces a flow through an elevation model on a raster map \---- the one used to create the corridors

مع هذا العمل حصلنا على خريطة مع الممرات البيئية المحتملة للذئب في بلدية ريبيرا دي بينا. هذه هي المجالات التي يتعين النظر فيها من قبل فنيين مجلس المدينة عند تخطيط تدابير الحفظ لهذه الأنواع. هذه الممرات ذات أهمية قصوى لأنها يمكن أن تصل بين حزم الذئب الهشة في فيلا ريال في الجنوب مع تلك الموجودة في الشمال ، والتي هي مستمرة مع تلك من بينيدا جيريس واسبانيا أكثر استقرارا بكثير. ومن الأهمية بمكان تلك الممرات التي تعبر المستوطنات البشرية ، مثل القرى الصغيرة والمدن والطرق. يجب أن تعتبر هذه المناطق حاسمة للحفاظ على الذئب ، وتطبيق تدابير للحد من تأثير الإنسان في هذا النوع.

![Ecological corridors and critical conservation areas for wolves in northern Portugal.](./images/portugal_ribeira2.png){.align-right width="100.0%"}
## الخاتمة
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## المؤلف
![Monica Almeida](./images/portugal_ribeiraaut.png){.align-left height="200px"}

ساهم هذا المقال في يوليو 2012 مونيكا ألميدا. وهي عالمة بيولوجيا الحفاظ تعمل في منظمة غير حكومية في مجال الحفاظ على الذئب في البرتغال.
