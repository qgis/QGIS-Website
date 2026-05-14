---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/india_assam1.png
title: वाघांच्या देखरेखीसाठी क्यूजीआयएस (आसाम, भारत सोनीतपूर जिल्हा, नामेरी व्याघ्र
  प्रकल्पात कॅमेरा सापळे वापरुन)
type: case-study

---
{{<content-start >}}
# वाघांच्या देखरेखीसाठी क्यूजीआयएस (आसाम, भारत सोनीतपूर जिल्हा, नामेरी व्याघ्र प्रकल्पात कॅमेरा सापळे वापरुन)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2013</span>
</p>

Nameri Tiger Reserve (NTR) is one of the 3 tiger reserves of Assam and it is situated in the northern part of Sonitpur District of Assam along the foothills of Eastern Himalayas. Spread over an area of 344 sq km, NTR boasts rich diversity of flora and fauna. The core area of the reserve which constitutes the "Nameri National Park" is bound by River Jia-Bhoreli on the west and River Bor-Dikorai in the east. To the north of the Nameri lies the Pakke Tiger Reserve of Arunachal Pradesh.

![](../images/india_assam1.png)

या लँडस्केपमध्ये रॉयल बंगाल टायगर, एशियन एलिफंट, इंडियन बायसन, कॉमन बिबट्या, क्लाउड बिबट्या, वन्य कुत्री, सांबर हरण, भुंकणारे हरण, हॉग हरण, वन्य डुक्कर आणि इतर अनेक प्रजाती या संरक्षणाचे महत्त्व आहेत. एनटीआर पक्षी विविधता देखील प्रभावी आहे आणि आतापर्यंत 370 पक्षी प्रजाती ओळखले गेले आहेत. हे राखीव आसाम वन विभाग, आसाम सरकारकडून व्यवस्थापित केले जाते.
## कॅमेरा ट्रॅप अभ्यासाच्या डिझाइनसाठी क्यूजीआयएसचा अर्ज
सन 2011 पासून सुरू करण्यात आलेल्या राष्ट्रीय व्याघ्र संवर्धन प्राधिकरणाने (एनटीसीए) देशातील सर्व व्याघ्र प्रकल्पांना कॅमेरा सापळ्यांचा वापर करून वाघांवर नजर ठेवणे बंधनकारक केले आहे. या नवीन प्रोटोकॉलअंतर्गत 100 चौरस किलोमीटर व्याघ्र प्रकल्पासाठी 25 जोड्या कॅमेरे बसविण्यात येणार असून नमुना घेण्याचा कालावधी 40-60 दिवसांचा आहे. हा नवीन वाघ मॉनिटरींग प्रोटोकॉल जीआयएसवर जास्त अवलंबून आहे.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Picture of a male tiger that was captured in one of the camera traps</figcaption>
</figure>

2012-13 मध्ये आम्ही क्यूजीआयएस वापरून एनटीआरमध्ये वाघांचे हे नवीन निरीक्षण प्रोटोकॉल लागू केले. सुरूवातीस, आम्ही क्यूजीआयएस मध्ये एनटीआर सीमा डिजिटल केली आणि बहुभुज म्हणून जतन केली. फील्ड सर्वेक्षण दरम्यान नेव्हिगेशन हेतूसाठी ही सीमा बहुभुज जीपीएसमध्ये निर्यात केली गेली. वाघांच्या अस्तित्वाचे पुग्मार्क, स्क्रॅच मार्क्स आणि स्कॅट्सच्या पुराव्यांकरिता आम्ही एनटीआरमध्ये विस्तृत साइन सर्वेक्षण केले. वाघाच्या चिन्हाचे जीपीएस समन्वय तसेच कॅमेर्‍याच्या सापळ्यांसाठी योग्य ठिकाणी रेकॉर्ड केली गेली. सर्वेक्षण पूर्ण झाल्यानंतर डेटा पुढील प्रक्रियेसाठी आणि कॅमेरा ट्रॅपच्या स्थानांना अंतिम रूप देण्यासाठी जीपीएस साधनांचा वापर करुन क्यूजीआयएसकडे हस्तांतरित केला गेला. वाघाची चिन्हे आणि संभाव्य कॅमेरा सापळा स्थान असलेली आकार फाईल तयार केली गेली.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Block wise distribution of camera trap locations and assigning camera traps to different forest camps by using voronoi polygons &amp; hub distance.</figcaption>
</figure>

Next we prepared 4 sq km grid layer using mmqgis plugin. The shape file containing results of sign survey was overlaid on the 4 sq grid to visualise the distribution of camera traps in NTR. Distance matrix option under vector analysis tools was quite handy for determining the inter camera distance. Camera locations having less than 1.8 km inter distance were removed to comply with the monitoring protocol. Due to lack of sufficient cameras to monitor the entire reserve area in one go, we decided to divide the reserve area into 2 blocks of 100 sq km each. Boundaries of these blocks were digitised and saved as separate shape files for both the blocks. Using RGB composition plugin, a false color composite of the reserve was created and the sign survey shape file overlaid to assess the habitat types used by the tiger. During the study period, the camera traps have to be monitored intensively by the field staff. To ensure smooth functioning of monitoring process, we used Voronoi polygon feature of Geometry tools and hub distance of mmqgis plugin for planning logistic requirements. The geographic coordinates of camera traps are required for estimating the tiger density and occupancy modelling of other species. These coordinate details were easily generated from camera trap shape files by using the "Export/ add geometry columns" feature of vector Geometry tools.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Survey grids with tiger presence</figcaption>
</figure>

## निष्कर्ष
For the first time in the history of this small tiger reserve of North East India, it was possible to monitor tigers by using camera traps mainly because of QGIS. Results of this monitoring exercise indicate the presence of 8-15 tigers in this landscape. In addition to the tigers, several elusive species have also been photographically documented. Apart from tiger monitoring, we are also using QGIS for activities such as planning habitat management works, revising patrolling schedules, and designing maps for visitors. The user-friendly interface, rich features, in-depth documentation, on-line support and the free/open source philosophy are the few qualities of QGIS that made us to select it over other proprietary software. We believe that QGIS has great potential for empowering individuals/institutions/ involved in conserving endangered wildlife in the developing world by offering GIS technology at little or no cost.
## लेखक
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

या लेखाचे योगदान मार्च 2013. मध्ये राजेंद्र जी. गरवड यांनी केले. ते आसाम, भारत मधील नामरी व्याघ्र प्रकल्पातील फील्ड डायरेक्टर आहेत. त्यांच्याकडे वनीकरण विज्ञान आणि संवर्धन आणि भूमी व्यवस्थापन विषयात मास्टर डिग्री आहे.

{{<content-end >}}
