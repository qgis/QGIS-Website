---
draft: 'true'

---
# स्वित्झर्लंडमधील कॅन्टन ऑफ सोलथर्नच्या सरकारी एफओएसजीआयएस स्टॅकमधील क्यूजीआयएस
![](./images/suisse_solothurn1.png){.align-left}

सोलथर्नचा कॅंटन 250,000 सोलोथर्न नागरिकांना सेवा आणि पायाभूत सुविधा पुरवतो. 2001 मध्ये राज्य संसदेने विंडोज वरून लिनक्समध्ये स्थलांतर करण्याचा निर्णय घेतला. विनामूल्य उद्यमांना प्रोत्साहित करण्यासाठी आणि परवाना खर्च कमी करण्यासाठी प्रेरणा एका विशिष्ट विक्रेत्यापासून स्वतंत्र असणे आवश्यक होते. याचा परिणाम म्हणून केंटन ऑफ सोलोथर्नच्या जीआयएस विभागाने 3500 हून अधिक कर्मचार्‍यांच्या जीआयएस-आवश्यकता फॉसजीस रणनीतीद्वारे वितरित करण्यास सुरवात केली.

आम्ही पहिले पाऊल उचलले ते म्हणजे यूएमएन मॅप सर्व्हरची ओळख आणि एसओ! मॅप क्लायंटची निर्मिती जी सर्व 3500 कर्मचार्‍यांसाठी वेबजीआयएस क्लायंट वापरण्यास सुलभ देते. दुसरी पायरी म्हणजे शेपफिल्स वरून पोस्टजीआयएस स्थानिक डेटाबेस इंजिनमध्ये आमच्या सर्व भौगोलिक डेटाचे स्थलांतर. परिचय खूप यशस्वी झाला, परंतु डेस्कटॉप वापरण्यास सुलभ जीआयएसचा अभाव होता.

वेगवेगळ्या डेस्कटॉप जीआयएसच्या मूल्यांकनानंतर आम्ही 2006 मध्ये ईएसआरआय आर्कइन्फो आणि आर्कव्यू 3 ला बदलून जीआरएसएस च्या संयुक्त विद्यमाने क्यूजीआयएस वापरण्याचे ठरविले.

निर्णय खालील पैलूंद्वारे चालविला गेला:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- ओएसजीओ प्रकल्प-संघटना
- जीयूआय जर्मन भाषेत अनुवादित
- जर्मन भाषेत लिहिलेले दस्तऐवजीकरण
- स्वित्झर्लंडमधील सोलोथर्न जवळ एक सक्रिय विकसक (मार्को ह्यूजंटोबलर).
- आम्ही डिजिटलायझिंग आणि मॅपकॉम्पोजींग यासारख्या हरवलेल्या / उणीवांच्या वैशिष्ट्यांची अंमलबजावणी करण्यासाठी मार्को हूजेन्टोबलरला करार करू शकतो.
- पायथनसह अनुप्रयोग आणि प्लगइन विकास
- वाढणारा वापरकर्ता समुदाय
- खूप सक्रिय विकसक समुदाय
- एकाच ऑपरेटिंग सिस्टमपासून स्वातंत्र्य

## आम्ही QGIS कुठे वापरतो?
यूएमएन मॅपसर्व्हरद्वारे परस्पर संवादात्मक नकाशेच्या उलट, डेस्कटॉप जीआयएसला सोलोथर्नच्या भौगोलिक डेटावर लवचिक दृश्य द्यावे लागेल. क्यूजीआयएस डेस्कटॉप जीआयएस 50 पेक्षा जास्त वापरकर्ते त्यांच्या दैनंदिन कामासाठी वापरत आहेत. परंतु त्यातील बरेच लोक जीआयएस तज्ञ नाहीत. त्यांना अंतर्ज्ञानी वापरकर्ता इंटरफेससह भौगोलिक डेटा व्हिज्युअलायझेशन आणि / किंवा कॅप्चर करू इच्छित आहे.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

म्हणूनच डेटामध्ये डेटा मॉडेलची मानवी वाचनीय यादी आहे आणि जीआयएस-तज्ञ नसलेला वापरकर्ता आवश्यक माहिती शोधण्यासाठी हा डेटाबेस वापरण्यास सक्षम आहे.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## निष्कर्ष
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## लेखक
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

या लेखाचे योगदान मे 2009 in मध्ये डॉ. हॉर्स्ट डेस्टर यांनी दिले. तो स्वित्झर्लंडमधील कॅन्टन ऑफ सोलथर्नमधील भू-सूचना विभागातील जीआयएस समन्वयक आहे.
