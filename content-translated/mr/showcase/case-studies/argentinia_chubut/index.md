---
author: 'Prof. Alberto Vázquez & Mauro Novara '
categories:
- Case studies
date: '2011-09-01'
description: 'In our region, Argentinean Patagonia, we have very few references about
  the application of GIS in High School for the construction of geographical knowledge
  as a mean to face territorial and environmental issues. '
draft: 'true'
heroImage: ''
tags:
- education
- argentina
- case-study
- showcase
thumbnail: argentinia_thumbnail.png
title: 'QGIS at high school: the urban green spaces in Rada Tilly coastal town, Chubut
  province, Argentina'
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}
## परिचय
आमच्या प्रदेशातील, अर्जेंटिनियन पॅटागोनियामध्ये, प्रादेशिक आणि पर्यावरणविषयक समस्यांना सामोरे जाण्यासाठी आम्ही भौगोलिक ज्ञानाच्या बांधकामासाठी हायस्कूलमधील जीआयएसच्या अर्ज बद्दल फार थोड्या संदर्भांत आहोत. QGIS द्वारे विश्लेषित केलेल्या राडा टिली किनारपट्टी शहरातील शहरी हिरव्या स्थानांच्या बाबतीत, अॅकॅबिल लिंकनच्या 12 व्या श्रेणीतील विद्यार्थ्यांना भौगोलिक कारणांसंबंधीचे विस्तृत स्वरूपातील एक महत्त्वाचे प्रबोधन असलेल्या एका शैक्षणिक कार्यक्रमाची कार्यप्रणाली प्रदर्शित करण्यास प्रवृत्त होते. 

We started by the observation (inventory), digitizing the cadastral blocks and the green areas (tree´s canopy) using Google Earth satellite images. As a conceptual framework, we lectured about cartographic design, satellite images reading and interpretation, and specially, location analysis to contrast the situation (in m^2^) of the urban green spaces by inhabitant in Rada Villa coastal town, with values suggested by the World Health Organization, WHO (a minimum of 9 m^2^ of green areas, by person, in urban areas).
## प्रकल्पा बद्दल
अनुभव मुख्य उद्देश अनुकूल आणि अवकाशासंबंधीचे माहिती व्यवस्थापन वाढविण्यासाठी, आणि निर्णय प्रक्रिया करण्यासाठी एक आधार प्रदान करण्यासाठी साधन म्हणून जी.आय.एस. ची अंमलबजावणी मध्ये, 12 ग्रेड विद्यार्थ्यांना व्याख्यान करण्यात आली.

** विशिष्ट उद्दिष्टे: **
- Student´s appropriation of a local issue (the Rada Tilly´s green areas related the 9 m^2^ by inhabitant proposed by WHO) from a geographical perspective through GIS tools.
- एक तांत्रिक साधन म्हणून जी.आय.एस. ची वापर सामाजिक अवकाशासंबंधीचे गृहीतप्रमेय सत्यापित करण्यासाठी.
- FOSS QGIS वापरून स्थानिक डेटाचे कॅप्चर, प्रोसेसिंग, स्टोरेज, विश्लेषण, पुनर्प्राप्ती आणि अद्ययावत करण्याची व्यवहार्यता तपासणे.

** पद्धती: **

आम्ही खालील पद्धतीचा सुरू ठेवण्यासाठी प्रकल्प निर्माण करण्यासाठी:
- प्रत्यक्ष व सैद्धांतिक व्याख्याने; प्रामुख्याने QGIS वापर आणि शहरी हिरव्या मोकळी जागा व त्याच्या प्रादेशिक परिणाम फायदे बद्दल.
- कॅर्तोग्रफिक  मॉडेलिंग, सदिश स्तर व्याख्या, जीआयएस डाटाबेसमध्ये विकास.
- फील्ड काम (झाडं डेटा रेकॉर्ड आणि जीपीएस स्थाने).
- एक गूगल  पृथ्वी (GeoEye) प्रतिमा वापरून शहरी कॅदास्त्राल  गट आणिट्रीस  द्वारावरील चैत्य कमानी, च्या वेक्टर अंकनीकरणाची. कॅदास्त्राल  ब्लॉक रक्कम रहिवासी विचार करण्यासाठी, आम्ही प्लॉट 4 रहिवासी सरासरी मूल्य नियुक्त केले आहे.
- विषयासंबंधीचा नकाशे माध्यमातून परिणाम सादरीकरण.

![Attribute table of "blocks" vector layer](argentinia_chubut1.png)
## निष्कर्ष
कॅडमॉस्ट्रल प्लॉटद्वारे 4 रहिवाश्यांच्या सरासरी मूल्याच्या प्रोजेक्शनच्या आधारे, आम्ही अंदाज केला की वर्तमान (2010) शहरी लोकसंख्या Rada Tilly सुमारे 9 .600 रहिवासी पर्यंत जाईल हे लोक 20 9 ब्लॉक्समध्ये वास्तव्य करतात आणि ते 157.6 हेक्टर जागेत आहेत. सरासरी लोकसंख्येची घनता हेक्टरच्या 61 रहिवाशांची असेल.

The total inventoried green areas grow up to 150.736 m^2^ (15 hectares). Reason why we can consider that the green area by inhabitant in the study area is 15.7 m^2^ (the WHO suggested value is 9 m^2^ of green area by inhabitant). This value proves a very favorable situation, as far as the environmental benefits, that trees offer to the inhabitants in this marine coastal town.

![Distribution of urban green spaces (green) and population density by blocks (white to brown) at Rada Tilly coastal town, Chubut Provinc, Argentina.](./images/argentinia_chubut2.png){.align-right}

प्रकल्प हायस्कूल एक शैक्षणिक व्यायाम होते, तरी आम्ही गंभीरपणे QGIS प्राप्त इंवेन्तोर्य्स  परिणाम मूल्य. विद्यार्थी साधन (QGIS) देखील विषयासंबंधीचा (शहरी हिरव्या मोकळी जागा) च्या विनियोजन दर्शविणे, सर्व शैक्षणिक आकस्मिक थंडी वाजून हुडहुडी भरणे आणि गांभीर्य सह काम आणि. पण त्यांना तसेच सहभागी शैक्षणिक कर्मचारी एक अतिशय समृद्ध अनुभव होता.

प्रकल्प अनुभवानंतर आम्ही FOSS QGIS जलद आणि कार्यक्षम स्वरूपात कॅप्चर, प्रोसेसिंग, स्टोरेज, विश्लेषण, पुनर्प्राप्ती आणि स्थानिक डेटाची अद्ययावत करण्यासाठी अत्यंत शिफारस पर्याय आहे. आमच्याकडे अशी सॉफ्टवेअरची अशी चांगली जाणीव आहे की आम्ही जीआयएस प्रोप्रायटरी सॉफ्टवेअरचा वापर करीत आहोत ज्याचा वापर आम्ही वापरत आहोत.
## लेखक:
हा लेख अर्जेटिना पासून मौरो नोवारा आणि अल्बेर्तो वश्क़ुएशz द्वारे सप्टेंबर 2011 मध्ये योगदान होते.

![Mauro Novara](argentinia_chubutaut1.png)

मौरो नोवारा  प्रादेशिक माहिती प्रणाल्या नक्कीच प्रोफेसर आहे. लेक्चरर आणि Patagonia सण जुआन Bosco, मानवता आणि सामाजिक विज्ञान अध्यापक राष्ट्रीय विद्यापीठाचे संशोधक. भूगोल विभाग. कोमोडोरो रिवाडाविया, Chubut प्रांत, अर्जेंटिना.

![Alberto Vázquez](argentinia_chubutaut2.png)

प्रा आल्बेर्तो वक़ुएश  अर्थात प्रादेशिक माहिती प्रणालीच्या पदवीधर शिक्षण सहाय्यक आहे. पाताडोनिया  सण जुआन बोस्को , मानवता आणि सामाजिक विज्ञान अध्यापक राष्ट्रीय विद्यापीठ. भूगोल विभाग. कोमोडोरो रिवाडाविया, चुबूत प्रांत, अर्जेंटिना.

{{<content-end >}}
