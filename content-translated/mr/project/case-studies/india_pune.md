---
HasBanner: false
archived: true
date: 2014-05-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/india_pune1.png
title: WMS (टाइल डाउनलोडर) वरून ऑफलाइन नकाशा तयार करण्यासाठी पायथन कन्सोलचा वापर करता
  येतो.
type: case-study

---
{{<content-start >}}
# WMS (टाइल डाउनलोडर) वरून ऑफलाइन नकाशा तयार करण्यासाठी पायथन कन्सोलचा वापर करता येतो.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2014</span>
</p>

पायथन कंसोलमधील स्क्रिप्टच्या मदतीने टाइल्स डाऊनलोड करून WMS/WFS  किंवा QGIS नकाशा दृश्यात लोड केलेला कोणताही नकाशा ऑफलाइन नकाशे कसे तयार करावे हे त्यांच्या अभ्यासात स्पष्ट केले आहे. स्क्रिप्ट पुढील वापरासाठी सर्व टाइल्सचे मोझॅक देखील तयार करते.

वेब मॅपिंग सर्व्हिस (डब्ल्यूएमएस) सेवेद्वारे रास्टर / वेक्टर नकाशांवर प्रवेश करणे खूप सामान्य आणि कार्यक्षम आहे. सुरक्षितता, केंद्रीकृत आणि लवचिक नकाशा शैली यासारखे त्याचे बरेच फायदे आहेत. गूगल नकाशे, याहू, बिंग, मोडीस, लँडसॅट, नासा, एनआरएससी (भारत) द्वारा प्रकाशित केलेले नकाशे याचे उदाहरण आहे. डब्ल्यूएमएसची गैरसोय / मर्यादा हे इंटरनेट किंवा इंट्रानेटद्वारे कार्य करते. विशेषत: सर्व्हेच्या वेळी क्षेत्रात नेहमीच इंटरनेट कनेक्शन मिळणे शक्य होणार नाही. GeoTiff, jpg, img इत्यादी कोणत्याही ऑफलाइन प्रतिमेच्या तुलनेत डब्ल्यूएमएस देखील धीमे कार्य करते.
## QGIS चा वापर
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

<figure>
<img src="../images/india_pune1.png" class="align-left" alt="india_pune1.png" />
<figcaption>QGIS with WMS tiles</figcaption>
</figure>

## पायथन कन्सोल
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. पहिल्या टायलचा X,Y समन्वय (वरचा डावा आणि खालचा उजवा)
2. डाउनलोड करण्यासाठी टाइलचा आकार (उदा. 0.001 X 0.001 अंश) इतका असतो 
3. डाउनलोड करण्यासाठी टाइलची संख्या (नकाशाच्या पूर्ण प्रमाणात आणि टाइलच्या आकारावर आधारित गणना केली आहे)
4. आउटपुट टाइल्स / फाइल्स संचयित करण्यासाठी आउटपुट निर्देशिका

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

<figure>
<img src="../images/india_pune2.png" class="align-left" alt="india_pune2.png" />
<figcaption>Python script and directory where tiles are stored</figcaption>
</figure>

या पद्धतीची मर्यादा आहे की, सर्व्हरच्या शेवटी नकाशामधील बदल ऑफलाइनमध्ये दिसून येणार नाहीत (डाउनलोड केलेला नकाशा). या प्रकरणात वापरकर्त्यास प्रक्रिया पुन्हा करावी लागेल आणि नवीन ऑफलाइन नकाशा तयार करावा लागेल. दुसरी मर्यादा हा तयार केलेला ऑफलाइन नकाशा प्रतिमा स्वरूप असेल; ते थीमॅटिक मॅपिंग किंवा प्रतिमेच्या वर्गीकरणासाठी वापरले जाऊ शकत नाही. काही अतिरिक्त प्रयत्नांनी काही डेटा गमावल्यास काही लँड्युज नकाशे वेक्टरमध्ये रूपांतरित केले जाऊ शकतात.
## व्याप्ती
तयार केलेले मोझॅक विषयगत नकाशावरून (7-8 रंग) डाऊनलोड केले असले तरी ते शुद्ध प्रतिमा आहे. पुनर्वर्गीकरणासारख्या प्रगत साधनाचा वापर करून लेयर/बँड स्टॅकिंग या रॅस्टरचे बहुभुज वेक्टरमध्ये रूपांतर करता येते. WMS कडे गेटक्षमता, गेटमॅप, गेटफिचरइन्फो अशा अनेक विनंत्या आहेत. प्रत्येक बहुभुजासाठी गेटगेचरइन्फो वैशिष्ट्य माहिती वापरून पुनर्प्राप्त केली जाऊ शकते. स्क्रिप्टप्लगइनमध्ये रुपांतरित केली जाऊ शकते जेणेकरून स्क्रिप्टिंगचे ज्ञान नसलेले कोणीही स्क्रिप्ट वापरू शकतील.
## निष्कर्ष
वरील अनुभव दर्शवितो की QGIS कोणत्याही प्रगतस्तरावर वापरला जाऊ शकतो. मूलभूत प्रोग्रामिंग कौशल्यामुळे एखादी व्यक्ती कामाची गुणवत्ता सुधारण्यासाठी आणि वेळ वाचविण्यासाठी एक छोटी स्क्रिप्ट किंवा प्लग-इन लिहू शकते.QGIS मध्ये, जगभरात विकसित केलेल्या प्लगइनच्या भांडारांमध्ये प्रवेश करणे QGIS मधील सर्वोत्कृष्ट आहे.  PyQGIS  विकसक कूकबुक एक स्क्रिप्ट लिहिण्यासाठी एक उत्तम स्त्रोत आहे आणि GDAL  साधनांच्या मदतीने रास्टर डेटा प्रोसेसिंग आता बरेच सोपे आहे.
## लेखक:
हा लेख पुणे (भारत) येथील प्रशांत कडगी यांनी मे 2014 मध्ये लिहिला असून ते सध्या GIS APP कन्सल्टन्सी सर्व्हिसेसमध्ये सल्लागार म्हणून कार्यरत आहेत. 2009 पासून ते NRM, वनीकरण, ई-गव्हर्नन्स, सॉफ्टवेअर डेव्हलपमेंट प्रकल्पांमध्ये GIS आणि RS चा वापर भारत आणि जगातील विविध प्रदेशांमध्ये करीत आहेत.
- Contact: <kadgiprashant@gmail.com>
- वेबसाइट www.gisappco.com (बांधकाम अंतर्गत)

{{<content-end >}}
