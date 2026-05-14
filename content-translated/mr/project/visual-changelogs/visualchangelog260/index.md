---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: project
sidebar: true
title: क्यूजीआयएस 2.6 चा चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.6 चा चेंजलॉग{#changelog26 }
Release date: 2014-10-31

क्यूजीआयएस 2.6.0 च्या पुढील रीलिझसाठी लॉग बदला. आम्ही सर्वात लोकप्रिय विनामूल्य डेस्कटॉप जीआयएस आणखी अधिक वैशिष्ट्ये भरलेली आणि उपयुक्त करण्यासाठी अनेक नवीन वैशिष्ट्ये, ट्वीट्स आणि संवर्धने जोडली आहेत.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

आम्ही विकसक, दस्तऐवजकार, परीक्षक आणि तेथील सर्व लोकांना त्यांचे आभार मानू इच्छितो जे आपला वेळ आणि मेहनत स्वयंसेवक करतात (किंवा लोकांना यासाठी पैसे देतात).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

शेवटी आम्ही आमच्या अधिकृत प्रायोजकांना या प्रकल्पात त्यांना देत असलेल्या अमूल्य आर्थिक मदतीबद्दल आभारी आहोत:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

क्यूजीआयएस हे एक विनामूल्य सॉफ्टवेअर आहे आणि आपण ते वापरण्यासाठी काहीही देण्याचे बंधन नाही - खरं तर आम्ही आपली आर्थिक किंवा सामाजिक स्थिती काय आहे याची पर्वा न करता दूरदूरच्या लोकांना याचा वापर करण्यास प्रोत्साहित करू इच्छितो - आमचा विश्वास आहे की स्थानिक निर्णय घेण्याच्या साधनांसह लोकांना सक्षम बनविणे संपूर्ण मानवतेसाठी एक चांगल्या समाजाचा परिणाम.

{{<table-of-contents >}}
## सामान्य
### वैशिष्ट्य: गुणधर्मांमध्ये प्रकल्प फाइलनाव
प्रोजेक्ट गुणधर्म संवादात आपण आता QGIS प्रोजेक्ट फाईलसाठी पूर्ण मार्ग पाहू शकता.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### वैशिष्ट्य: डेल / बॅकस्पेस की द्वारे मोजताना अंतिम बिंदू काढण्याची परवानगी द्या
आता आपण क्षेत्रे आणि अंतर मोजत असताना आपण हटवा किंवा बॅकस्पेस की वापरून आपल्या मापन लाइनमधून अवांछित शिरोबिंदू काढू शकता.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### वैशिष्ट्य: कॅनव्हासवरील संबंध संदर्भ विजेटमधून संबंधित वैशिष्ट्य निवडा
### वैशिष्ट्य: संपादक विजेट
आम्ही संपादक विजेट्समध्ये बर्‍याच सुधारणा केल्या आहेत:
- तारीख / वेळ रिक्त तारखा सेट करण्यास सक्षम नवीन संपादन विजेट
- फिल्टर ओळ संपादन
- संपादन विजेटसाठी शून्य मूल्यांची योग्य हाताळणी
- फोटो विजेट शून्य मूल्य जतन करतो
- वेब विजेट शून्य मूल्य जतन करते
- विशेषता सारणी 0 आणि एनयूएलएल दरम्यान फरक करू शकते
- श्रेणी विजेटसाठी प्रत्यय समर्थन जोडा

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### वैशिष्ट्यः वैकल्पिकरित्या सामील झालेल्या स्तरातील फील्ड्सचा एक सबसेट वापरा
आपण आता वेक्टर जॉइन तयार करताना संबंधित फील्डचा फक्त एक उपसेट वापरू शकता.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### वैशिष्ट्य: अभिव्यक्ति फील्ड (आभासी फील्ड)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### वैशिष्ट्यः कृतींमध्ये आता संबंधित चिन्ह असू शकते
वेक्टर लेयरसाठी सानुकूल कृती तयार करताना, आपण आता क्रियेसाठी देखील वापरले जाण्यासाठी चिन्ह निश्चित करू शकता.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### वैशिष्ट्य: अतिरिक्त अभिव्यक्ति प्रकार आणि पर्याय
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### वैशिष्ट्य: पदवीधर आणि वर्गीकृत प्रस्तुतकर्त्यांमधील वर्ग टॉगल केले जाऊ शकतात
आपण आता प्रत्यक्षात न काढता पदवीधर आणि वर्गीकृत प्रस्तुतकर्त्यांमधील काही वर्ग अक्षम करणे निवडू शकता.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### वैशिष्ट्य: आख्यायिका सुधारणा
आख्यायिका / तक्ता सामग्रीच्या दुसर्‍या टप्प्याचे काम पूर्ण झाले आहे. यासहीत:
- API क्लीनअप (विकसकांसाठी)
- थर ट्रीमध्ये नकाशा स्तरांचे दृश्यमानता गट. हे नवीन टूलबार बटण दृश्यमान असलेल्या स्तरांच्या गटांमधील द्रुत बदलांस अनुमती देते.
- लेजेंड टूलबारवरील लेयर ग्रुप्स व्यवस्थापित करण्याची क्षमता
- दंतकथा टूलबारवरील नवीन लेजेंड फिल्टर पर्याय सध्या कोणत्याही दृश्यासाठी नसलेल्या कोणत्याही वर्गातील आख्यायिका आयटम काढेल. हे एक अद्भुत सुधारणा आहे कारण हे सुनिश्चित करते की आपल्या नकाशा आख्यायिकेमध्ये सध्या नकाशा दृश्यात नसलेल्या आयटमसाठी प्रविष्ट्या नाहीत. हे मुख्य नकाशा आख्यायिकेमध्ये आणि नकाशा संगीतकारात आणि डब्ल्यूएमएस स्तरांसाठी उपलब्ध आहे.
- नियम-आधारित प्रस्तुतकर्ता आख्यायिका आता छद्म-वृक्षात प्रदर्शित केल्या जाऊ शकतात

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## डेटा प्रदात्या
### वैशिष्ट्यः डीएक्सएफ निर्यात सुधारणा
- संवादातील लेयर असाइनमेंटसाठी ट्री व्ह्यू आणि विशेषता निवड
- समर्थन बहुभुज / हॅच
- मजकूराचे मजकूर पाठ TT ऐवजी MTEXT (फॉन्ट, तिरपे आणि वजन यासह)
- support for RGB colors when there\'s no exact color match
- आर 12 ऐवजी ऑटोकॅड 2000 डीएक्सएफ (आर 15) वापरा
- R18 चाचणी पद्धती काढा

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## नकाशा संगीतकार
### वैशिष्ट्य: प्रिंट / निर्यात पासून मुद्रित संगीतकार आयटम लपविण्यावर नियंत्रण
आयटमला संगीतकार निर्यात / प्रिंटआउटमधून वगळलेले नाही की नाही हे नियंत्रित करण्यासाठी आम्ही चेकबॉक्स आणि डेटा डिफाइन्ड बटण जोडले आहे. आयटमची तपासणी न केल्यास ते केवळ रचना डिझाइनच्या वेळीच दिसून येईल.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### वैशिष्ट्य: रिक्त संगीतकार फ्रेमसाठी पृष्ठ छपाईवर नियंत्रण ठेवा
टेबल किंवा एचटीएमएल फ्रेमसाठी, चेकबॉक्स आता फ्रेम रिक्त असताना असलेले पृष्ठ निर्यात करायचे की नाही हे नियंत्रित करते.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### वैशिष्ट्य: आयटम ट्री पॅनेल
नकाशा संगीतकारातील आयटम ट्री पॅनेल आयटमची निवड करण्यास परवानगी देतो, आयटम लपवित / दर्शवितो, आयटमची लॉक स्थिती टॉगल करतो आणि आयटम आयडी संपादित करण्यासाठी डबल-क्लिक करतो. आयटमची पुन्हा क्रमवारी लावण्यासाठी आपण ड्रॅग आणि ड्रॉप देखील वापरू शकता.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### वैशिष्ट्य: संगीतकार बाण / ओळ आयटम दिसण्यावर अधिक नियंत्रण
- रेखा चिन्ह शैली संवाद वापरुन ओळी स्टाईल केल्या जाऊ शकतात
- एरो हेड फिल आणि बाह्यरेखा रंग वापरकर्ता परिभाषित केले जाऊ शकतात
- एरो हेड बाह्यरेखा रूंदी वापरकर्ता परिभाषित केली जाऊ शकते

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### वैशिष्ट्य: संगीतकार आयटमचे डेटा परिभाषित नियंत्रण
संगीतकार आयटमचे बर्‍याच गुणधर्मांवर आता डेटा बाँडिंगचा वापर केला जाऊ शकतो. यात समाविष्ट:
- पारदर्शकता आणि मिश्रण मोड.
- आयटम फिरविणे.
- नकाशा स्केल, विस्तार आणि फिरविणे.
- Atटलस वैशिष्ट्य समास
- आयटमचा आकार आणि स्थिती.
- पृष्ठ आकार, अभिमुखता आणि पृष्ठांची संख्या.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### वैशिष्ट्य: संगीतकार प्रतिमा दूरस्थ URL म्हणून निर्दिष्ट केल्या जाऊ शकतात
नकाशाचे संगीतकार मधील चित्र आयटम आता चित्र स्त्रोत म्हणून रिमोट url चे समर्थन करतात. हा स्रोत डेटा परिभाषित देखील केला जाऊ शकतो.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### वैशिष्ट्य: संगीतकार सारणी सुधारणा
- आपण आता सारणी शीर्षलेख आणि सामग्री फॉन्ट रंग सेट करू शकता.
- सारण्या आता एकाधिक फ्रेममध्ये विभाजित केल्या जाऊ शकतात, ज्यामुळे त्यांची सामग्री स्तंभांवर किंवा भिन्न पृष्ठांवर वितरित केली जाऊ शकते.
- प्रथम फ्रेम, सर्व फ्रेम किंवा कोणत्याही फ्रेमवर पर्याय जोडलेले विकल्प दर्शविले.
- स्तंभ रूंदीच्या व्यक्तिचलित नियंत्रणास अनुमती द्या.
- सारणी स्त्रोतासाठी नवीन पर्याय, सध्याच्या lasटलस वैशिष्ट्यासह आणि नातेसंबंधातील मुलाच्या वैशिष्ट्यांसह.
- रिक्त सारण्यांसाठी वर्तनाची निवड, संपूर्ण सारणी लपविणे, रिक्त पेशी दर्शविणे किंवा टेबलच्या मुख्य भागामध्ये सेट संदेश प्रदर्शित करणे समाविष्ट आहे.
- सध्याच्या अ‍ॅटलास वैशिष्ट्यास प्रतिच्छेदन करणा those्यांना सारणी वैशिष्ट्ये फिल्टर करण्यासाठी चेकबॉक्स जोडला.
- सारणीमधून डुप्लिकेट पंक्ती काढण्यासाठी चेकबॉक्स जोडला.

लक्षात घ्या की विद्यमान प्रकल्पांमधील सारण्या या वैशिष्ट्यांचे समर्थन करणार्‍या नवीन सारणी स्वरूपात स्वयंचलितपणे अद्यतनित केलेली नाहीत आणि नवीन सेटिंग्ज दिसण्यासाठी सारण्या एखाद्या रचनावर पुन्हा जोडल्या पाहिजेत.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### वैशिष्ट्य: संगीतकार सुधारणा
नकाशाचे संगीतकार (मुद्रण करण्यायोग्य नकाशे रचना तयार करण्यासाठी वापरले गेले) क्यूजीआयएस 2.6 मध्ये बर्‍याच सुधारणा प्राप्त झाल्या आहेत.
- आपण आता स्केलबारसाठी दुय्यम भरण रंग बदलू शकता
- रेखा / बाण आयटम काढताना शिफ्ट होल्डिंग क्षैतिज, अनुलंब किंवा 45 डिग्री कोनात रेखांकन करते
- इतर नवीन वस्तू काढताना होल्ड शिफ्ट होल्ड केल्यामुळे त्यांना चौरसात रोखले जाते, Alt पकडण्यामुळे आयटम मध्यभागी ओढला जातो
- यापुढे आयटम लॉक / अनलॉक करण्यासाठी राइट क्लिक करा, हे आता नवीन आयटम पॅनेलद्वारे हाताळले आहे. लॉक केलेल्या वस्तू यापुढे संगीतकार कॅनव्हास वरून निवडल्या जाऊ शकत नाहीत ज्यामुळे त्याखालील वस्तूंशी संवाद साधता येईल.
- कर्सर की दाबताना Alt दाबून ठेवल्यास आयटमसाठी 1px चळवळ होते
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### वैशिष्ट्य: सुधारित आयटम स्नॅपिंग
स्नैपिंग थ्रेशोल्ड आता पिक्सल्समध्ये सेट केले आहेत, रचनामध्ये झूम केल्यावर बारीक हालचाल आणि वस्तूंचे आकार बदलण्यास अनुमती देते. गटामधील घटक यापुढे स्वयं स्नॅप लाइनसाठी वापरले जाणार नाहीत.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### वैशिष्ट्य: नकाशा आयटमसाठी एकाधिक विहंगावलोकन
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### वैशिष्ट्य: एचटीएमएल आयटम सुधारणा
एचटीएमएल कम्पोझर आयटमसाठी बरेच उपयोगी नवीन पर्याय आहेत:
- एचटीएमएल स्रोताच्या स्वहस्ते प्रविष्टीसाठी पर्याय
- एचटीएमएल स्त्रोतामधील QGIS अभिव्यक्त्यांचे HTML सामग्री प्रस्तुत करण्यापूर्वी मूल्यांकन केले जाऊ शकते
- HTML स्त्रोतासाठी डेटा परिभाषित URL
- HTML शैली अधिलिखित करण्यासाठी वापरकर्ता स्टाईलशीट तयार करण्यास अनुमती द्या

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### वैशिष्ट्य: संगीतकार नकाशा ग्रीड सुधारणा
- आपल्याकडे आता भिन्न गुणधर्मांसह अनेक ग्रिड्स असू शकतात.
- आपण रीप्रोजेक्ट ग्रिड्स आणि लॅट / लाँग ग्रिड्स मिसळू शकता.
- आपण मानक QGIS प्रतीकशास्त्र ग्रीड लाइन इत्यादी वापरू शकता.
- एक नवीन फ्रेम / भाष्ये आहेत केवळ ग्रीड शैली. ही शैली निवडल्यामुळे केवळ फ्रेम आणि भाष्ये रेखाटल्या जातील, नकाशावर ग्रीड लाइन किंवा इतर खुणा नसतात.
- आता नकाशा आयटमच्या कोणत्या बाजूस फ्रेम ओढली आहे हे नियंत्रित करण्याचे पर्याय आहेत.
- फ्रेम्ससाठी नवीन टिक स्टाईल आहेत ज्यात आतील टिक्स, बाह्य टिकिक्स आणि दोन्ही अंतर्गत आणि बाह्य टिक पर्याय आहेत.
- आम्ही भाष्यांकरिता बर्‍याच नवीन स्वरूपांसह, ग्रिड भाष्यांमधील सुधारणांमध्ये सुधारणा केली आहे.
- ग्रिड भाष्ये आता ग्रीड भाष्य करण्यासाठी टायपोग्राफिकरित्या योग्य प्राइम आणि डबल प्राइम प्रतीक वापरतात.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## प्रक्रिया करीत आहे
### वैशिष्ट्य: मॉडेल आणि स्क्रिप्टचे ऑनलाईन संग्रह
मॉडेल आणि स्क्रिप्ट ऑनलाइन संग्रहातून डाउनलोड केल्या जाऊ शकतात आणि थेट प्रक्रिया इंटरफेसमधून स्थापित केल्या जाऊ शकतात. प्रक्रियेच्या वापरकर्त्यांद्वारे प्रदान केलेल्या नवीन स्क्रिप्ट्स आणि मॉडेल्ससह संकलनाचा विस्तार केला जाईल.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### वैशिष्ट्यः नवीन मॉडेलर अंमलबजावणी
मॉडेलर पुन्हा लिहिले गेले आहे आणि आता खोलीची मर्यादा नसलेल्या नेस्टेड मॉडेल्सना परवानगी देण्यासारखे अतिरिक्त कार्यक्षमता प्रदान करते. मॉडेल आता JSON फायली म्हणून संग्रहित आहेत. मागची सुसंगतता ठेवली आहे, म्हणून सर्व मॉडेल्स अद्याप वापरली जाऊ शकतात. आपण आता इनपुट आणि अल्गोरिदममधून आयटम मॉडेलर ग्राफवर ड्रॅग आणि ड्रॉप देखील करू शकता.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## कार्यक्रमक्षमता
### वैशिष्ट्यः क्यूजीआयएस विजेट्ससाठी एपीआय बदल
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS सर्व्हर
### वैशिष्ट्य: गेटफिचरइन्फो विनंतीसह शोध वर्धित करणे
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### वैशिष्ट्य: GetFeatureInfo भूमिती वैशिष्ट्यांसाठी एक अचूक सेटिंग जोडा
## प्रतीकशास्त्र
### वैशिष्ट्य: उत्तम यादृच्छिक रंग निवड
आम्ही वर्गीकृत प्रस्तुतकर्त्यासाठी यादृच्छिक रंग अल्गोरिदम सुधारित केला आहे जेणेकरून व्युत्पन्न केलेले रंग एकमेकांपासून अधिक दृष्यमान असतील.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### वैशिष्ट्य: प्रतीकशास्त्र वापरकर्ता इंटरफेस सुधारणा
- जेथे शक्य असेल तेथे प्रतीक थर प्रकार बदलताना प्रतीक थरांचे गुणधर्म राखले जातात.
- शेपबर्स्ट आणि ग्रेडियंट कलर रॅम्पसाठी संपादन बटण जोडले.
- लेबल आणि शेजारील श्रेणीच्या सीमांचे स्वयंचलित अद्यतन.
- नियम आधारित रेन्डररवर स्विच करताना वर्ग श्रेणीबद्ध आणि पदवीधर वर्गातून आपोआप वर्ग बदलले जातात.
- पदवीधर प्रस्तुत लेबलांमध्ये युनिट्स आणि दशांश स्थानांची संख्या जोडली.
- कलर रॅम्प, इनव्हर्टेड कलर रॅम्प आणि जीयूआय मधील इतर पर्यायांमधील बदलांबद्दल सुधारित प्रतिसाद
- साधे, पदवीधर, वर्गीकरण केलेले आणि अन्य प्रस्तुतकर्त्यांमधील स्विच करताना प्रतीक कायम ठेवा.
- एसटीडीएव कॅल्क्युलेशन मोडचे सुधारित लेबलिंग.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## वापरकर्ता इंटरफेस
### वैशिष्ट्य: वाक्यरचना हायलाइटिंग कोड संपादक
अजगर स्क्रिप्ट संपादक, अभिव्यक्ती बिल्डर, फिल्टर विंडो, संगीतकार एचटीएमएल आणि सीएसएस संपादकांसाठी

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### वैशिष्ट्य: रंग पॅलेट
आपण आता QGIS मध्ये वापरासाठी आपल्या स्वतःच्या सानुकूल रंग पॅलेट परिभाषित करू शकता.
- सानुकूल वापरकर्ता ग्लोबल कलर पॅलेट (पर्याय संवादात).
- प्रति प्रकल्प रंग पॅलेट (प्रकल्प गुणधर्म संवादात).
- रंग बटण मेनू आणि नवीन रंग निवडक संवादात दर्शविले गेले आहेत.
- आपण जीपीएल पॅलेट फाईलवर रंग आयात / निर्यात करू शकता.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### वैशिष्ट्य: नवीन रंग निवडक संवाद
एक नवीन सानुकूल क्यूजीआयएस रंग निवडक संवाद आहे. वैशिष्ट्यांचा समावेश आहे:
: - रंगछटा, संपृक्तता, मूल्य, लाल, हिरवा, निळा रंग घटकांसाठी स्लाइडर.
  - अल्फा स्लायडर
  - एचटीएमएल रंग कोड कॉपी करण्यासाठी / पेस्ट करण्याचा पर्याय (विविध स्वरूपात).
  - अल्फा पूर्वावलोकनासह रंग पूर्वावलोकनापूर्वी / नंतर
  - परस्परसंवादी 2 डी कलर रॅम्प विजेट.
  - ह्यू व्हील / त्रिकोण विजेट.
  - जीपीएल पॅलेट फाईलमध्ये नवीन पॅलेट तयार करण्याची आणि आयात / निर्यात रंगांच्या क्षमतेसह संपादन करण्यायोग्य रंग पॅलेट.
  - सेट त्रिज्या (ओएस समर्थन अवलंबित) वर नमुना घेण्याचा पर्याय असलेला लाइव्ह कलर सॅम्पलर.
  - ड्रॅग आणि ड्रॉप ड्रॉप (ओएस समर्थन आश्रित) द्वारे इतर अ‍ॅप्‍ससह परस्परसंवादाचे समर्थन करते.
  - संवाद अक्षम करण्याचा पर्याय आणि त्याऐवजी मूळ निवडक संवाद वापरा.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### वैशिष्ट्यः सिंगल सिलेक्ट फीचर टूल आयताद्वारे निवडण्यात विलीन केले
आम्ही सिंगल सिलेक्शन टूल आयताच्या टूलमध्ये विलीन केले. आपण एकल वैशिष्ट्य निवडू इच्छित असल्यास, फक्त आयत साधन सक्षम करा आणि नंतर वैशिष्ट्य क्लिक करा (आयत ड्रॅग करण्याऐवजी) एक वैशिष्ट्य.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### वैशिष्ट्य: कॅनव्हास वर्तन नकाशावर स्तर जोडा
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### वैशिष्ट्य: चिन्ह आकार 48 आणि 64 जोडा
टच डिव्‍हाइसेसवर क्यूजीआयएस वापरणार्‍यांसाठी (किंवा आपल्याला फक्त मोठे, चंकी आयकॉन्स आवडत असतील तर), आता आपण चिन्ह 64 64 x p 64 पिक्सेल आकारात सेट करू शकता.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### वैशिष्ट्य: नवीन रंग बटणे
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### वैशिष्ट्य: साधन ओळखण्यासाठी संदर्भ मेनू
ओळख साधन वापरताना, संदर्भ मोडमधील ओळख साधन वापरण्यासाठी आपण आता कॅनव्हासवर उजवे क्लिक करू शकता. दिसणार्‍या मेनूमध्ये आपण कोणते वैशिष्ट्य प्रकार ओळखण्यास इच्छुक आहात ते निर्दिष्ट करू शकता (सर्व आपल्याला आवडत असल्यास).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
