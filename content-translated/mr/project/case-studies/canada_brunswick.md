---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/canada_brunswick1.jpg
title: क्यूजीआयएस सह फंडी फुटपाथ ट्रेल नकाशा तयार करण
type: case-study

---
{{<content-start >}}
# क्यूजीआयएस सह फंडी फुटपाथ ट्रेल नकाशा तयार करण
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2013</span>
</p>

![](../images/canada_brunswick1.jpg)

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

पायवाट तयार केली गेली आहे, देखरेख केली गेली आहे आणि त्यांना फंडी हायकिंग ट्रेल असोसिएशन इंक. (एफ एच टी ए) (1975) म्हणून ओळखल्या जाणार्‍या स्वयंसेवकांच्या गटाद्वारे बढती दिली गेली. एक नानफा संस्था म्हणून एफ एच टी ए आपल्या मार्गदर्शकाच्या विक्रीतून आपल्या कामांसाठी निधी गोळा करते ज्यात मागचा नकाशा समाविष्ट आहे. २०११ मध्ये मी अधिकृत पथ नकाशा अद्यतनित करण्यासाठी स्वयंसेवा करण्यासाठी एफ एच टी ए संपर्क साधला. स्वयंसेवी म्हणून एखाद्या नफा न देणार्‍या संस्थेसाठी नकाशा तयार करणे, डेटा संपादन करण्यासाठी आणि अंतिम नकाशाच्या लेआउटसाठी दोन्ही उपकरण बिल म्हणून फिट होते. मी आणि एफ एच टी ए च्या सदस्यांच्या प्रयत्नातून मार्गदर्शक पुस्तकासह समाविष्ट असलेला फंडी फूटपाथचा नवीन अधिकृत नकाशा क्यूजीआयएससह प्रारंभ करण्यापासून तयार केला गेला.

<figure>
<img src="../images/canada_brunswick2.jpg" class="align-right" alt="canada_brunswick2.jpg" />
<figcaption>QGIS GPS Tools Plugin for data collection</figcaption>
</figure>

## प्रकल्प
क्यू जीआय एस सह नवीन कोना फूटपाथ नकाशा तयार करण्याची प्रक्रिया तीन वेगवेगळ्या भागांमध्ये मोडली जाऊ शकते:
- माहिती मिळवणे.
- डेटा संपादन आणि तयारी.
- नकाशा उत्पादन.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

<figure>
<img src="../images/canada_brunswick3.jpg" class="align-right" alt="canada_brunswick3.jpg" />
<figcaption>Creation of the footpath map in QGIS</figcaption>
</figure>

अंतिम नकाशा उत्पादनात डेटा तयार करण्यासाठी क्यूजीआयएस मधील खालील साधने विशिष्ट कामे साध्य करण्यासाठी वापरली गेली.
- अंतिम नमुना उत्पादन डेटा तयार करण्यासाठी कुजेवडे खालील साधने विशिष्ट सामर्थ्यासाठी वापरलेली सामग्री.
- एनआरसीन आणि एसएनबीकडून प्राप्त केलेला वेक्टर डेटा एकत्र विलीन केला गेला, क्वेरी केला आणि वेक्टर साधनांचा वापर करून अंतिम नकाशाच्या क्षेत्रासाठी क्लिप केला.
- एसएनबीकडून प्राप्त केलेली स्वल्पविरामाने-विभक्त केलेली फाइल क्यूजीआयएस कडे एक बिंदू स्तर म्हणून आयात केली गेली, डिलिमिटेड मजकूर स्तर जोडा रास्टर टूल्स प्लगइन.

<figure>
<img src="../images/canada_brunswick4.jpg" class="align-right" alt="canada_brunswick4.jpg" />
<figcaption>Footpath map in the Print Composer</figcaption>
</figure>

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## निष्कर्ष
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

<figure>
<img src="../images/canada_brunswick5.jpg" class="align-right" alt="canada_brunswick5.jpg" />
<figcaption>The final Fundy Footpath map with accompanying guidebook</figcaption>
</figure>

## दुवे
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## लेखक
<figure>
<img src="../images/canada_brunswickaut.jpg" class="align-left" height="200" alt="canada_brunswickaut.jpg" />
<figcaption>Jarrett Totton</figcaption>
</figure>

या लेखाचे योगदान जानेवारी 2013 in मध्ये जॅरेट टटन यांनी दिले. जॅरेट कॅनडाच्या अल्बर्टामध्ये राहणारा जीआयएस तंत्रज्ञ आहे.

{{<content-end >}}
