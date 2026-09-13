---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: project
sidebar: true
title: क्यूजीआयएस 2.4 साठी चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.4 साठी चेंजलॉग{#changelog24 }
Release date: 2014-06-27

क्यूजीआयएस 2.4.0 च्या पुढील रीलिझसाठी लॉग बदला. या प्रकाशनावर पॉलिश आणि कार्यक्षमतेवर जोर देण्यात आला आहे - आम्ही वापरकर्त्याची इंटरफेस अधिक सुसंगत आणि व्यावसायिक बनविण्यासाठी (आणि वापरण्यास सुलभतेने सुलभ) करण्यासाठी अनेक नवीन वैशिष्ट्ये, ट्वीक्स आणि संवर्धने जोडली आहेत. संगीतकाराने (प्रिंट रेडी नकाशे तयार करण्यासाठी वापरलेला) उत्तम कार्टोग्राफिक आउटपुट तयार करण्यासाठी अधिक व्यवहार्य व्यासपीठ बनविण्यासाठी त्याच्याकडे बरेच काम केले आहे.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

आम्ही विकसक, दस्तऐवजकार, परीक्षक आणि तेथील सर्व लोकांना त्यांचे आभार मानू इच्छितो जे आपला वेळ आणि मेहनत स्वयंसेवक करतात (किंवा लोकांना यासाठी पैसे देतात).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

शेवटी आम्ही आमच्या अधिकृत प्रायोजकांना या प्रकल्पात त्यांना देत असलेल्या अमूल्य आर्थिक मदतीबद्दल आभारी आहोत:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## सामान्य
### Feature: Generate band name with NetCDF EXTRA_DIM
नेटसीडीएफने अतिरिक्त आयामी माहिती दिली. ही माहिती प्रत्येक बँडवर मेटाडेटा प्रदान करते. हे मेटाडेटा प्रत्येक बँडचे नाव स्पष्ट करण्यासाठी वापरला जाऊ शकतो. उदाहरणार्थ, नेटसीडीएफ फाईलचे बँड दिलेल्या खोलीवर तापमानाचे प्रतिनिधित्व करतात. वापरकर्त्यासाठी, फक्त बँड क्रमांकाऐवजी खोली माहितीसह बँड निवडणे सोपे आहे.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### वैशिष्ट्य: रास्टर डेटावर स्केल लागू करणे आणि ऑफसेट करणे
काही रास्टर डेटासोर्समध्ये, डेटा स्केलसह इंटिजर आणि मेटाडेटामध्ये ऑफसेट म्हणून संग्रहित केला जातो. योग्य डेटा मिळविण्यासाठी स्केल आणि ऑफसेटचा वापर केला जाऊ शकतो. क्यूजीआयएस प्रयोक्तांना आख्यायिका, हिस्टोग्राम आणि ओळखीसाठी योग्य माहिती प्रदातापर लागू करतो.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### वैशिष्ट्य: विशेषता सारणीमध्ये द्रुत फील्ड फील्ड कॅल्क बार
वेक्टर विशेषता सारण्यांमधील गणना केलेल्या फील्डसह कार्य करणार्‍यांसाठी आमच्याकडे एक नवीन नवीन वैशिष्ट्य आहे. नवीन द्रुत गणना पट्टी आपल्याला विशेषता सारणीच्या स्तंभातील मूल्ये द्रुत आणि सहजतेने अद्यतनित करू देते.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### वैशिष्ट्यः संगीतकार आणि नकाशा कॅनव्हासमधील रंग पूर्वावलोकन मोड
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### वैशिष्ट्य: क्यूएलआर क्यूजीआयएस लेयर फायली
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### वैशिष्ट्य: नवीन अभिव्यक्ती कार्ये
आमच्याकडे अभिव्यक्ति बिल्डरमध्ये काही नवीन कार्ये उपलब्ध आहेत.
- बाउंडिंग बॉक्स (सीमा)
- bounding box width & height (bounds_width/bounds_height)
- मिनिट / कमाल x / y समन्वय (xmin / xmax / ymin / ymax)
- नवीन वर्ड्रॅप फंक्शन जे जास्तीत जास्त / किमान वर्णांमध्ये लपेटलेली स्ट्रिंग परत करते

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### वैशिष्ट्य: कॉपी, पेस्ट आणि ड्रॅग आणि ड्रॉप रंग
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### वैशिष्ट्य: बहु-थ्रेडेड प्रस्तुतीकरण
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## लेबलिंग
### वैशिष्ट्य: लेबल अनेक वेळा वैशिष्ट्ये
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## नकाशा संगीतकार
### वैशिष्ट्य: संगीतकार चित्र आयटममध्ये सुधारणा
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### वैशिष्ट्य: lasटलस नकाशेसाठी पूर्वनिर्धारित स्केल मोड
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### वैशिष्ट्य: संगीतकारात सुधारित विशेषता सारण्या
आम्ही आपल्या संगीतकार लेआउटमध्ये सारण्या प्रदर्शित करण्याच्या क्षमतेत बरेच सुधार केले आहेत:
- Support has been added for reordering columns within a table
- अभिव्यक्ति आधारित स्तंभांसाठी समर्थन जोडला
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- सारणी सामग्री अभिव्यक्तीद्वारे फिल्टर केली जाऊ शकते

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### वैशिष्ट्य: सामान्य संगीतकार सुधारणा
नकाशा रचना मोडमध्ये कार्य करताना जीवन सुलभ करण्यासाठी नकाशा संगीतकारात बरीच भर आहेत:
- मुख्य नकाशा कॅनव्हासमध्ये वर्तमान नकाशा आयटम प्रमाणात पाहण्यासाठी बटण जोडले
- थरांसह संगीतकार कडून एसव्हीजी प्रतिमा निर्यात करण्याची क्षमता
- स्केलबारसाठी लाइन जॉइन आणि कॅप शैली सेट करा
- आयटम फ्रेमसाठी लाइन जॉइन शैली सेट करण्यासाठी समर्थन

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### वैशिष्ट्यः एचटीएमएल फ्रेममध्ये सुधारणा
संगीतकारातील एचटीएमएल फ्रेम्स सुधारित केल्या आहेत. तेथे एक नवीन ** अ‍ॅड फ्रेम ** बटण आहे जे एकाधिक दुवा साधलेल्या फ्रेम मॅन्युअली तयार करण्यासाठी वापरला जाऊ शकतो. आम्ही आमचे पृष्ठ ब्रेक लॉजिक देखील सुधारित केले आहे जेणेकरून आपल्याला एचटीएमएल फ्रेम पृष्ठबद्ध करताना मजकूराच्या ओळीच्या मध्यभागी खंडित होणारे पृष्ठ ब्रेक मिळतील.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## प्लगइन्स
### वैशिष्ट्य: मेटासर्च कॅटलॉग क्लायंट प्लगइन
मेटासाटा हे वेब (सीएसडब्ल्यू) मानक करीता ओजीसी कॅटलॉग सेवेचे समर्थन करणारे मेटाडाटा कॅटलॉग सेवांसह संवाद साधण्यासाठी एक क्यूजीआयएस प्लगइन आहे. हे प्लगइन QGIS मधील मेटाडेटा कॅटलॉग शोधण्यासाठी एक सोपा आणि अंतर्ज्ञानी दृष्टीकोन आणि वापरकर्ता-अनुकूल इंटरफेस प्रदान करते आणि आता QGIS कोर उत्पादनासह डीफॉल्टनुसार जहाजे.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## प्रतीकशास्त्र
### वैशिष्ट्य: शेपबर्स्ट फिल शैली
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### वैशिष्ट्य: मार्कर लाइन प्लेसमेंट शिफ्ट करण्याचा पर्याय
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### वैशिष्ट्य: नवीन इन्व्हर्टेड बहुभुज प्रस्तुतकर्ता
बहुभुज वैशिष्ट्यांसाठी नवीन प्रस्तुतकर्ता समाविष्ट केले गेले आहे, ज्यामुळे आपण आपल्या बहुभुजांच्या ** बाहेर ** प्रत्येक गोष्टीची शैली बनवू शकता. हे क्षेत्र हायलाइट करण्यासाठी किंवा कार्टोग्राफिक मुखवटे तयार करण्यासाठी उपयुक्त ठरू शकते. जेव्हा नवीन शेपबर्स्ट शैली वापरली जाईल, तेव्हा आपण आता या एंट्रीसाठी प्रतिमेत दर्शविल्याप्रमाणे आउटपुट तयार करू शकता.

** टीपः ** प्लगइन मुखवटाची नवीन आवृत्ती सध्याच्या निवडीपासून सहजपणे मुखवटा स्तर तयार करण्यास, त्या भागात केवळ लेबल वैशिष्ट्ये आणि अ‍ॅटलास नकाशा निर्मितीमध्ये स्वयंचलित मुखवटा तयार करण्यास मदत करते.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### वैशिष्ट्यः स्थानिक स्तरांसह शैली जतन करणे आणि पुनर्प्राप्त करणे
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
