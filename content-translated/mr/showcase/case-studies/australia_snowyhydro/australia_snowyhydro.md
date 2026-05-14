---
draft: 'true'

---
# बर्फाचे वर्गीकरण स्वयंचलित करण्यासाठी प्रोसेसिंग टूलबॉक्स वापरणे
स्नोई हायड्रो लिमिटेड (एसएचएल) ऑस्ट्रेलियातील न्यू साउथ वेल्सच्या हिमाच्छादित पर्वत स्थित एक पीक वीज जनरेटर आहे. देशभरात विविध प्रकारच्या मालमत्तेची मालकी असला तरी, हिमाच्छादित हायड्रो लिमिटेड ऑस्ट्रेलियाच्या पायाभूत सुविधांच्या संरक्षणासाठी प्रसिद्ध आहे, स्नोई पर्वत हायड्रो इलेक्ट्रिक स्कीम.

हिमाच्छादित पर्वत हायड्रो इलेक्ट्रिक स्कीम, न्यू साऊथ वेल्स अल्पाइन भागातील मोसमी बर्फमुळे शक्य झाले आहे. स्प्रिंग हिमवृष्टीतील पाणी राष्ट्रीय वीज बाजारपेठेमध्ये वीज पुरवठ्याची मागणी, पीक आणि दक्षिण-पूर्व ऑस्ट्रेलियातील सिंचन आणि शेतीसाठी वाळवंट अंतर्देशीय भागात पाणी वळविण्यासाठी वापरली जाते.

हिवाळ्याच्या महिन्यांत बर्फ कव्हरची वर्गवारी करणे SHL हिमाच्छादित क्षेत्राचे जीवन चक्र, ऐतिहासिक नोंदींचे संग्रह क्षेत्र, आणि पाणी उपज आणि साठवण अंदाजांसाठी जलविज्ञान सेवा संघाला कव्हरेज आकडेवारी प्रदान करण्याची परवानगी देते.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## पार्श्वभूमी
हिवाळ्याच्या महिन्यांत प्रत्येक वर्षी (1 जून ते 31 ऑक्टोबर) SHL ने MOODIS Terra (EOS AM) उपग्रह पासून शक्य तितक्या ढग मुक्त प्रतिमा प्राप्त केल्या आहेत. त्यानंतर ही प्रतिमा सामान्यीकृत हिमवर्षाव निर्देशांक (एनडीएसआय) म्हणून ओळखल्या गेलेल्या एका अल्गोरिदममध्ये भरल्या जातात, ज्याचा वापर हिमवर्षाव असलेल्या ठिकाणी दर्शविण्याकरीता केला जातो. हा अल्गोरिदम कोणत्याही एका विशिष्ट सेन्सरसाठी अद्वितीय नसला तरी, MODIS इन्स्ट्रुमेंट त्याच्या पुरेसा स्थानिक रिझोल्यूशन आणि प्रकल्पाच्या क्षेत्राच्या दररोज कव्हरेज (मॅप 1.1 हिमवर्षाव पाणी संचय) यांच्यामुळे निवडण्यात आला.
## आमचे ध्येय
QGIS प्रोसेसिंग टूलबॉक्समध्ये मॉडेल म्हणून एनडीएसआय वर्कफ्लो स्वयंचलित करने हा प्रकल्पाचा उद्देश आहे. आवश्यक आऊटपुट वेक्टर बहुभुज आहे ज्यामध्ये हिमध्वल वॉटर कॅचमेंटच्या अंतरावर हिमवर्षाव असणारा भाग दर्शवितात, तसेच चौरस किलोमीटरमध्ये असलेल्या एकूण क्षेत्राचे वर्णन करतात.
## पद्धत
एनडीएसआय अल्गोरिदम स्वतः अगदी सोपे आहे (फॉर्मुला 1.1 - सामान्य फॉरेस्ट हिम इंडेक्स (एनडीएसआय) मध्ये) आणि व्हेक्टरच्या स्वरूपात हिमवृष्टी काढण्यासाठी लागणारे पुढचे पावले देखील प्रोसेसिंग टूलबॉक्स मॉडेलसाठी छानपणे स्वतः उधार देतात.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

हे NDSI अल्गोरिदम -1 आणि 1 दरम्यान निकाल देईल, विशेषत: बर्फसाठी थ्रेशोल्ड 0.4 पेक्षा जास्त असणार आहे. एनडीएसआय आउटपुटचे एक उदाहरण खाली दिलेले आहे (नकाशा 1.3 - एनडीएसआय आऊटपुट), 13 जुलै 2014 साठी नैसर्गिक रंगीत प्रतिमेसह (नकाशा 1.2 - एमडीआयएस खरे कलर). या प्रतिमांवरून पाहिल्याप्रमाणे बर्फला भेदभाव करताना एनडीएसआय आउटपुट फार चांगले आहे. इतर जमिनीच्या कव्हर प्रकार आणि ढगांचे झाकलेले भाग. हे मात्र मोठ्या प्रमाणातील बर्फाचे अंश म्हणून चुकीचे वर्गीकरण करू शकते, ज्यामुळे स्पेक्ट्रम जवळच्या इन्फ्रारेड भागात पाणी शोषून घेण्यासारखे आहे. NDSI च्या या वैशिष्ट्यपूर्ण मॉडेल मध्ये काही टप्प्यावर एक पाणी मुखवटा अंतर्भूत करण्याची आवश्यकता दर्शवितात.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## परिणाम / निष्कर्ष
QGIS प्रोसेसिंग टूलबॉक्स हा बर्फ वर्गीकरण सारख्या कार्यप्रवाह स्वयंचलित करण्यासाठी एक शक्तिशाली मार्ग आहे. वर दर्शविलेले मॉडल यशस्वीरित्या बर्फ वर्गीकरण प्रक्रियेस स्वयंचलित करते आणि जीआयएस डेटासेट वितरीत करते जे व्हिज्युअलायझेशन आणि इनपुटसाठी पुढील सांख्यिकीय अनुप्रयोगांमध्ये वापरले जाऊ शकते. पुनरावृत्तीयोग्य आणि सातत्यपूर्ण वर्गीकरण साधन प्रदान करताना हे SHL द्वारे वापरल्या जाणाऱ्या पूर्वीच्या पद्धतींसह संबंधित विषयक वापरकर्ता त्रुटी यशस्वीरित्या काढते. काही हंगामी परिणाम येथे पाहिले जाऊ शकतात.
### लेखक
अँड्र्यू जेफ्री ऑस्ट्रेलियातील कूमा एनएसडब्ल्यूमध्ये स्थित हिमाचल प्रदेश हायस्कूल लिमिटेडसह जीआयएस विश्लेषक आहे. 2004 मध्ये स्पाशील इन्फॉर्मेशन सिस्टिम्स मध्ये त्यांनी प्राध्यापक म्हणून विज्ञान (बीएससी) घेऊन वाग्गा वागामधील चार्ल्स स्टर्ट विद्यापीठातून पदवी प्राप्त केली. स्नोइ हायड्रो लिमिटेडमध्ये त्यांनी क्लाउड सीडिंग प्रयोग आणि दिवसांसारख्या रोमांचक प्रकल्पांना स्थानिक आधार प्रदान करण्यास सक्षम केले आहे. 
