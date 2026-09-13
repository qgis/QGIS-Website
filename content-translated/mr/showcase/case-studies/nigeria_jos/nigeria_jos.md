---
draft: 'true'

---
# नायजेरियातील अमुरम फॉरेस्ट रिझर्व वस्ती आणि एव्हीफाऊना क्यूजीआयएस सह मॅपिंग करतात
अमूरम फॉरेस्ट रिझर्व नायजेरियातील जोस, पठार राज्य शहराजवळ आहे. त्याची स्थापना ए.पी. लेव्हेंटिस ऑर्निथोलॉजिकल रिसर्च इन्स्टिट्यूट (एपीएलओआरआय) ने राष्ट्रीय संवर्धन, शिक्षण आणि संशोधनाच्या उद्देशाने केली. एपीएलओआरआय जॉस युनिव्हर्सिटीमध्ये प्राणीशास्त्र विभाग आयोजित करते. वार्षिक नायजेरियातील अंदाजे आठ अत्यंत प्रवृत्त विद्यार्थ्यांचा एक गट संवर्धन जीवशास्त्र, आकडेवारी (आर सह) आणि 2011  पर्यंत जीआयएस प्रशिक्षण प्राप्त करतो. डिसेंबर २०११ मध्ये दोन आठवड्यांच्या दरम्यान आम्ही मूलभूत जीआयएस संकल्पनांचा अभ्यास केला आणि विविध संवर्धनासाठी क्यूजीआयएस असलेल्यांना लागू केले. या लेखात आम्ही क्यूजीआयएसचा कसा उपयोग केला आहे त्याचे वर्णन करतो ज्यायोगे आम्ही निवासस्थानांचा आणि अमूरम आरक्षणाच्या निर्धारकांचा नकाशा तयार केला आणि जैवविविधतेसह एव्हीफाउनाचे स्थानिक वितरण प्रभावीपणे निर्धारित करण्याच्या उद्देशाने स्ट्रॅट प्राप्त करण्यासाठी मूलभूत निवास नकाशे कसे वापरले गेले.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## उन्नतीकरण, टेकडीची सावली, उतार आणि वस्ती
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) GdalTools मूळ डेटा संच विलीन करण्यासाठी आणि राखीव असलेल्या लहान क्षेत्राचे क्लिप करण्यासाठी वापरले गेले जेणेकरून रास्टर डेटा सेट तुलनेने लहान राहिले. जीपीएसच्या माध्यमातून आम्ही राखीव ठिकाणी विविध ठिकाणी उन्नती गोळा केली.
3) एकंदरीत, एसआरटीएम डेटा सेटची उन्नती जीपीएस-संकलित उन्नततेशी सुसंगत आहे. जीडलटूलमधील टेरिन मॉडेल्सचा उपयोग त्या भागासाठी डोंगरांच्या हॅडीज आणि उतारांची गणना करण्यासाठी केला जात असे. हे बदल पर्यावरणीय दृष्टीकोनातून महत्वाचे आहेत कारण ते वास्तव्याच्या प्रकाराशी दृढ निगडित आहेत.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) आम्ही एक सुंदर दिसणारा नकाशा विकसित करण्याचा हेतू असल्याने आम्ही उच्च रिझोल्यूशन नकाशा प्राप्त करण्यासाठी मूळ (क्लिप केलेले) उन्नत नकाशा गुंडाळला. आम्ही GdalTools मध्ये तानाचे साधन वापरले. समोच्च साधनाद्वारे आम्हाला गुळगुळीत समोच्च रेषा प्राप्त झाल्या.
5) रिझर्व्हच्या सीमेचे समन्वय जीपीएसद्वारे रिझर्व्हच्या सीमारेषावर चालत प्राप्त केले गेले. जीपीएस मध्ये संग्रहित वेपॉइंट्स आणि ट्रॅक जीपीएस साधनांचा वापर करून सहजतेने आयात केले गेले. बहुभुज आकार फाईल तयार करण्यासाठी आयात केलेले वेपॉइंट्स आणि ट्रॅक वापरले गेले. रिझर्वमधील ट्रॅक त्याच पद्धतीने मॅप केले गेले.
6) आम्ही ओपनलेयर्स प्लगइनसह कार्यक्षेत्रात सापडलेल्या Google उपग्रह प्रतिमेचा वापर करून अमुरमचे निवासस्थान नकाशा द्रुतपणे आणि तंतोतंतपणे तयार करण्यास आम्ही सक्षम होतो. रिझर्वमध्ये तीन प्रकारचे वेगळे अधिवास आहेत: सवाना, गॅलरी फॉरेस्ट आणि रॉकी आउटक्रॉप. उपग्रहाच्या प्रतिमेच्या आधारे आम्ही तीन अधिवास सीमांकन करणारे बहुभुज रेखाटण्यासाठी संपादकाचा वापर केला. स्नॅपिंग पर्याय सेट केल्याने नॉन-ओव्हरलॅपिंग बहुभुजांच्या बांधकामास योग्य परवानगी दिली.

## पक्षी वितरण आणि विविधता मॅपिंग
अधिवास नकाशे यादृच्छिक स्थाने व्युत्पन्न करण्यासाठी वापरले गेले. वस्तीच्या विविध प्रकारच्या क्षेत्राचा उपयोग प्रत्येक वस्ती प्रकार (स्तरीकरण) च्या पृष्ठभागाशी संबंधित अनेक ठिकाणी तयार करण्यासाठी केला जात असे.

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## निष्कर्ष
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## लेखक:
अबेंगो एल्मंड चियादिकोबी, yanडियन्जू टेमिडिओ एस्तेर, अकीमेन नेरियोया, अल्बर्ट मलंगले तौजे, अझी अबोक जोएल, इचुडे डॅनियल, इल्के फोलमर, नवागू चिमा जोशीया, ओनोजा जोसेफ डॅनियल, यदोक बिपलांग गोडविल
