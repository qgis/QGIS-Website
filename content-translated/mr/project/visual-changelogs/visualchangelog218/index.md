---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: project
sidebar: true
title: क्यूजीआयएस 2.18 चा चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.18 चा चेंजलॉग{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Release date: 2016-10-21

2.x मालिकेतील हे शेवटचे प्रकाशन आहे. सद्य लाँग टर्म रीलिझ (एलटीआर) आवृत्ती 2.14.x. हे रीलिझ आमच्या मागील रिलीझपेक्षा वाढीव सुधारणा प्रदान करते. बहुतेक क्रियाकलाप सध्या क्यूजीआयएस of 3.0 च्या विकासाकडे केंद्रित आहेत जे 2017 next च्या पहिल्या तिमाहीत अखेरीस नियोजित आमची पुढील पिढी रिलीझ आहे.

**धन्यवाद**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

क्यूजीआयएस हे एक विनामूल्य सॉफ्टवेअर आहे आणि आपण ते वापरण्यासाठी काहीही देण्याचे बंधन नाही - खरं तर आम्ही आपली आर्थिक किंवा सामाजिक स्थिती काय आहे याची पर्वा न करता दूरदूरच्या लोकांना याचा वापर करण्यास प्रोत्साहित करू इच्छितो - आमचा विश्वास आहे की स्थानिक निर्णय घेण्याच्या साधनांसह लोकांना सक्षम बनविणे संपूर्ण मानवतेसाठी एक चांगल्या समाजाचा परिणाम.

{{<table-of-contents >}}
## क्यूजीआयएस आवृत्ती 2.18.0 साठी प्रायोजक
दरवर्षी आम्हाला आमच्याकडून केलेल्या कार्याचे कौतुक करणा various्या विविध संस्थांकडून पाठिंबा देखील मिळतो आणि प्रकल्पात जाणार्‍या सततच्या प्रयत्नांना मदत करणे आवडेल. हे प्रायोजक आमच्या आभारासह खाली सूचीबद्ध आहेत!

{{<fund type="changelog" relativeImgPath=true >}}
## सामान्य
### वैशिष्ट्य: परिणामांमध्ये स्वयंचलित दुवे
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### वैशिष्ट्य: माउस व्हील ओव्हर कलर डायलॉग स्लाइडर
क्यूजीआयएस 2.18 मध्ये आपण व्हॉल्यूम कमी प्रमाणात वाढविण्यासाठी कलर पिकर डायलॉगमधील स्लाइडर्सपैकी कुठल्याही स्लाइडरवर माउस व्हील स्क्रोल करू शकता. रंगीत घटकांना चिमटा काढण्यासाठी हा एक सोपा शॉर्टकट आहे.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: रंग बटण ड्रॉप डाऊन मेनूमध्ये सानुकूल रंग योजना जोडा
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## प्रतीकशास्त्र
### वैशिष्ट्य: रंग निवडक आता स्तर शैली पॅनेलमध्ये एम्बेड केला आहे
क्यूजीआयएस 2.18 In मध्ये लेयर स्टाईल पॅनेलमधील कलर बटणावर क्लिक केल्याने रंग निवडक संवाद स्वतंत्र संवादऐवजी स्वतः शैली पॅनेलमध्ये उघडला जाऊ शकतो. हे निकालाच्या तत्काळ पूर्वावलोकनासह रंगांच्या परस्पर संवादीकरणास अनुमती देते.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## लेबलिंग
### वैशिष्ट्य: लेबलिंगसाठी प्रतिस्थापन सूची समर्थन
लेबल मजकूरास लागू असलेल्या मजकूराची सूची निर्दिष्ट करण्याची क्षमता जोडते. उदा. रस्त्याचे प्रकार संक्षिप्त.

पुनर्वापर आणि सामायिकरण सुलभ करण्यासाठी वापरकर्ते पर्यायांच्या याद्या निर्यात आणि आयात करू शकतात.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: सुधारित लाइन लेबल प्लेसमेंट अल्गोरिदम
लाईन लेयर्ससाठी समांतर लेबलिंग मोडमध्ये मोठ्या प्रमाणात सुधारणा केली गेली आहे, एक नवीन अल्गोरिदम जो वैशिष्ट्य भूमितीच्या कडक भागांवर लेबल ठेवणे टाळतो.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

या वैशिष्ट्यास अँड्रियास न्युमन यांनी अनुदान दिले

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्यः परिघासह वक्र लेबले वापरुन बहुभुज लेबल
हे बहुभुजांच्या लेबलिंगसाठी एक नवीन मोड जोडते जेथे वक्र लेबलिंगचा वापर करून बहुभुजाच्या परिमितीचे लेबल लावले जाते.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## प्रस्तुत करणे
### वैशिष्ट्य: रास्टर टाईलचे पूर्वावलोकन (डब्ल्यूएमटीएस आणि एक्सवायझेड थर)
क्यूजीआयएसच्या मागील आवृत्त्यांमध्ये, परिणामी नकाशा पाहण्यासाठी वापरकर्त्याने स्तरातील सर्व टाइल डाउनलोड पूर्ण होईपर्यंत प्रतीक्षा करावी लागली. हे आता निश्चित केले गेले आहे आणि टाईल डाउनलोड होताच नकाशा कॅनव्हासमध्ये त्वरित दर्शविल्या जातील, जेणेकरून काहीतरी दर्शविले जात नाही तोपर्यंत वेळ कमी करून वापरकर्त्याचा अनुभव सुधारला. शिवाय, खाली किंवा उच्च रिजोल्यूशनवरून पूर्वी डाउनलोड केलेल्या फरशा ज्या भागात योग्य रिजोल्यूशनसह फरशा अद्याप डाउनलोड केलेल्या नाहीत त्या भागात पूर्वावलोकन कार्यक्षमतेसाठी वापरल्या जाऊ शकतात.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### वैशिष्ट्य: रास्टर्सचे रद्द करण्यायोग्य प्रस्तुतीकरण (डब्ल्यूएमएस, डब्ल्यूएमटीएस, डब्ल्यूसीएस आणि एक्सवायझेड स्तर)
रिमोट सर्व्हरवरून येणाster्या रास्टर लेयर्ससह कार्य करताना हे वर्धन वापरकर्त्याच्या अनुभवात सुधारते. पूर्वी एखाद्यास नकाशे पुन्हा झूम किंवा पॅन करण्यास सक्षम होण्यासाठी डाउनलोड पूर्णपणे पूर्ण होईपर्यंत प्रतीक्षा करावी लागेल, कारण दरम्यानच्या काळात वापरकर्ता इंटरफेस गोठलेला असेल. हे आता रास्टर थरांचे प्रस्तुतिकरण कधीही रद्द केले जाऊ शकते या तथ्याद्वारे निश्चित केले गेले आहे.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## माहिती व्यवस्थापन
### वैशिष्ट्य: केवळ निवडलेल्या वैशिष्ट्यांची कॉपी करण्यासाठी ध्वज जोडा
ऑफलाइन संपादन प्लगइन्स हे डीफॉल्ट प्लगइन आहे जे क्यूजीआयएस सह शिप करते आणि आपल्याला दूरस्थ डेटासेटची ऑफलाइन (उदा. एका डेटाबेसमधून) परवानगी देते, फील्डमध्ये संपादित करतात आणि नंतर आपल्या कार्यालयात परत येता तेव्हा ते पुन्हा संकालित करतात. हे केवळ मोठ्या स्तरांच्या सबसेटवर कार्य करण्यासाठी ऑफलाइन संपादन शक्यता वाढवते.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

हे वैशिष्ट्य डीबी फहरवेगडीएन्स्टी जीएमबीएचने दिले होते

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## फॉर्म आणि विजेट्स
### वैशिष्ट्यः स्वतंत्र संपादन विजेटसाठी नियंत्रित लेबलांना अनुमती द्या
फॉर्ममध्ये वैयक्तिकृत विजेट्ससाठी नियंत्रित लेबलांना अनुमती द्या. ड्रॅग अँड ड्रॉप डिझायनरमध्ये, आयटमवर डबल क्लिक करणे प्रत्येक आयटमसाठी स्वतंत्रपणे लेबल दर्शविले जावे की नाही हे नियंत्रित करण्यास अनुमती देईल.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### वैशिष्ट्य: टॅब आणि गट बॉक्ससाठी सशर्त दृश्यमानता
ड्रॅग अँड ड्रॉप डिझाइनर फॉर्ममध्ये टॅब आणि ग्रुपबॉक्स सशर्तपणे दर्शविण्यासाठी किंवा लपविण्यासाठी हे एक नवीन कॉन्फिगरेशन पर्याय जोडेल.

फील्ड कॉन्फिगरेशन इंटरफेसमधील डिझाइनर ट्रीमध्ये डबल क्लिकद्वारे कॉन्फिगरेशन केले जाते.

दृश्यमानता नियंत्रित करण्यासाठी अभिव्यक्ती प्रविष्ट केली जाऊ शकते. फॉर्म बदलल्याबद्दल आणि त्यानुसार टॅब किंवा ग्रुपबॉक्समध्ये दर्शविलेले / लपविलेले प्रत्येक मूल्यांचे अभिव्यक्तीचे पुन्हा मूल्यमापन केले जाईल.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### वैशिष्ट्य: क्लायंट साइड डीफॉल्ट फील्ड मूल्य
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

हे वैशिष्ट्य डीबी फहरवेगडीएन्स्टी जीएमबीएचने दिले होते

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## नकाशा संगीतकार
### वैशिष्ट्य: खरे उत्तर बाण
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## प्रक्रिया करीत आहे
### वैशिष्ट्य: पृष्ठभाग अल्गोरिदम वर बिंदू
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: प्रक्रिया विरघळणारे अल्गोरिदम एकाधिक फील्ड स्वीकारते
विसर्जित अल्गोरिदम आता आपल्याला एकापेक्षा जास्त फील्ड मूल्याच्या आधारावर विरघळण्याची परवानगी देतो. मागील QGIS आवृत्त्यांमध्ये विरघळणे केवळ एका फील्ड मूल्याद्वारे गट वैशिष्ट्ये समाविष्ट करू शकते.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: ऑप्टिमाइझ्ड प्रोसेसिंग क्लिप अल्गोरिदम
प्रक्रिया क्लिप अल्गोरिदम सामान्य वापर परिस्थितीसाठी ऑप्टिमाइझ केले गेले आहे, परिणामी क्लिपिंग ऑपरेशन्ससाठी नाटकीय वेग वाढविला जातो. उदाहरणार्थ:

** 2 बहुभुज विरूद्ध 1 दशलक्ष रेषांसह रस्ता थर कापणे **

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

** 2 बहुभुज विरूद्ध 5 दशलक्ष पॉईंट पत्त्याची थर कापणे **

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: बाउंडिंग बॉक्स अल्गोरिदम
हे नवीन अल्गोरिदम इनपुट लेयरमधील प्रत्येक वैशिष्ट्याच्या बाउंडिंग बॉक्स (लिफाफा) ची गणना करते.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: कनेक्ट केलेल्या ओळी अल्गोरिदम विलीन करा
हा अल्गोरिदम मल्टीलाइनस्ट्रिंग भूमितीच्या सर्व कनेक्ट भागांमध्ये एकल लाइनस्ट्रिंग भूमितीमध्ये सामील होतो. जर मल्टीलाइनस्ट्रिंग भूमिती इनपुटचा कोणताही भाग कनेक्ट केलेला नसेल तर परिणामी भूमिती एक मल्टिलाइनस्ट्रिंग असेल ज्यामध्ये कोणतीही लाइन विलीन केली जाऊ शकते आणि कोणतेही जोडलेले नसलेले रेखा भाग असतील.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### वैशिष्ट्य: भूमिती सीमा अल्गोरिदम
हे नवीन अल्गोरिदम इनपुट भूमिती (म्हणजे भूमितीच्या टोपोलॉजिकल सीमा) च्या संयोजी सीमेचे बंदी परत करते. उदाहरणार्थ, बहुभुज भूमितीमध्ये बहुभुजातील प्रत्येक अंगठीसाठी लिनेस्टिंग्जची एक सीमा असेल आणि रेखा भूमितीस रेषाच्या सुरूवातीस आणि शेवटच्या बिंदूंसह एक सीमा असेल. हे अल्गोरिदम फक्त बहुभुज किंवा रेखा स्तरांसाठी वैध आहे.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## डेटा प्रदात्या
### वैशिष्ट्य: एक्सवायझेड टाइल थरांचे मूळ समर्थन
एक्सवायझेड स्वरूपातील रास्टर फरशा आता डब्ल्यूएमएस डेटा प्रदात्यामध्ये मूळपणे समर्थित आहेत, ज्यामुळे वापरकर्त्यांना आता क्विकॅपॅप सर्व्हिसेस किंवा ओपनलायर्स सारख्या तृतीय-पक्षाच्या प्लगइनची आवश्यकता न पडता इतर स्त्रोतांकडून बेसमॅप्स प्रदर्शित करण्यास अनुमती दिली जाते.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS सर्व्हर
### वैशिष्ट्य: सर्व्हरमधील वैशिष्ट्य माहिती भूमिती एकत्रीकरण करण्याची शक्यता
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

या वैशिष्ट्यास अँड्रियास न्युमन यांनी अनुदान दिले

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## प्लगइन्स
### वैशिष्ट्य: डीबी व्यवस्थापक: एसक्यूएल लेअर अद्यतनित करण्याची क्षमता जोडा
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## कार्यक्रमक्षमता
### वैशिष्ट्यः जीओओएस रेषीय संदर्भ फंक्शन क्यूजीजीमेट्रीमध्ये उघड करा
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## वैशिष्ट्यः 2.18 मध्ये नवीन पायक्विजीआयएस वर्ग
### नवीन कोर वर्ग
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### नवीन जीयूआय वर्ग, पुन्हा वापरण्यायोग्य विजेट
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## वैशिष्ट्य: नवीन अभिव्यक्ती कार्ये
क्यूजीआयएस 2.18 अँगल / डिस्टॉन्स इंटरपोलेशनच्या फंक्शन्ससह अनेक नवीन एक्सप्रेशन फंक्शन्स समाविष्ट करते.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

या वैशिष्ट्यास अँड्रियास न्युमन यांनी अनुदान दिले

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
