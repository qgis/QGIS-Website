---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: जैवविविधता आणि इकोसिस्टम सर्व्हिसेस (एचएबीईएएस) साठी हॉटस्पॉट एरियासाठी नकाशावर
  क्यूजीआयएस वापरणे.
type: case-study

---
{{<content-start >}}
# जैवविविधता आणि इकोसिस्टम सर्व्हिसेस (एचएबीईएएस) साठी हॉटस्पॉट एरियासाठी नकाशावर क्यूजीआयएस वापरणे.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

या व्यासपीठाचे मुख्य उद्दीष्ट म्हणजे भूमध्य सागरी क्षेत्रातील अनेक सार्वजनिक आणि खाजगी संस्थांमध्ये पसरलेल्या जैवविविधता आणि इकोसिस्टम सर्व्हिसेसवरील विविध प्रकारच्या डेटामध्ये विनामूल्य प्रवेश प्रदान करणे हे आहे. 2012 च्या अखेरीस / 2013 early च्या सुरूवातीस ते पोर्तुगालच्या उत्तरेस आणि बोस्निया आणि हर्जेगोव्हिनामधील तुझला कॅन्टनमध्येही विस्तारित केले जाईल.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

पोर्तुगालच्या दक्षिणेकडील उच्च संवर्धन मूल्य वन (एचसीव्हीएफ) ओळखण्यासाठी डब्ल्यूडब्ल्यूएफ द्वारे एचएबीईएएसमध्ये समाविष्ट असलेली भौगोलिक माहिती देखील वापरली गेली आहे, ज्यांना त्यांचे वन वनविभागाची परिषद (एफएससी मिळावी अशी इच्छा आहे अशा जमीन मालकांसाठी) एक अनिवार्य पाऊल आहे.(FSC)  प्रमाणपत्र.

![](../images/portugal_lisbon3.jpg)

प्रत्येक मालमत्तेत कोणत्या संवर्धनाचे मूल्य होते हे निर्धारित करण्यासाठी आम्ही सेक्स्टंट मॉडेलरचा उपयोग स्क्रिप्ट तयार करण्यासाठी केला ज्याने मालमत्तेच्या सीमांसह सर्व HABEaS थरांना छेदले. समान साधन वापरुन आम्ही स्वयंचलितपणे कार्बनची मात्रा मोजणारी स्क्रिप्ट देखील तयार करू शकलो. ते सध्या प्रत्येक प्रॉपर्टीमध्ये संग्रहित आहे.

![](../images/portugal_lisbon4.jpg)
## निष्कर्ष
क्यूजीआयएस वापरण्यास सुलभ आहे आणि त्यात खूप शक्तिशाली भू-प्रसंस्करण क्षमता आहे ग्रॅस जीआयएस आणि सागा जीआयएस टूल्सच्या सेक्स्टंट टूलबॉक्सद्वारे एकत्रित केल्याने आम्हाला अनेक जटिल स्थानिक विश्लेषण करण्यास परवानगी दिली आणि सेक्स्टंट मॉडेलरद्वारे त्यांना पाइपलाइन काढले. नवीन मुद्रण संगीतकारांसह गुणवत्ता नकाशे आणि इंकस्केप सह पुढील संपादनासाठी त्यांना एसव्हीजी स्वरूपात निर्यात करण्यासाठी जे एक शक्तिशाली मुक्त स्रोत वेक्टर ग्राफिक्स संपादक आहे.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## लेखक
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

फिलिप डायस हा सेंटर फॉर अप्लाइड इकोलॉजी (इंस्टीट्युटो सुपीरियर डी ronग्रोनोमिया, लिस्बनच्या टेकिनिकल युनिव्हर्सिटी) मधील पीएचडी विद्यार्थी आहे आणि वर्ल्ड वाइड फंड फॉर नेचर (डब्ल्यूडब्ल्यूएफ) च्या भूमध्य प्रोग्रामचा सल्लागार आहे.

{{<content-end >}}
