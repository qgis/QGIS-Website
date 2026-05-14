---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: project
sidebar: true
title: क्यूजीआयएस 2.12 साठी चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.12 साठी चेंजलॉग{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Release date: 2015-10-23

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**धन्यवाद**

आम्ही विकसक, दस्तऐवजकार, परीक्षक आणि तेथील सर्व लोकांना त्यांचे आभार मानू इच्छितो जे आपला वेळ आणि मेहनत स्वयंसेवक करतात (किंवा लोकांना यासाठी पैसे देतात).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

शेवटी आम्ही आमच्या अधिकृत प्रायोजकांना या प्रकल्पात त्यांना देत असलेल्या अमूल्य आर्थिक मदतीबद्दल आभारी आहोत:
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

क्यूजीआयएस हे एक विनामूल्य सॉफ्टवेअर आहे आणि आपण ते वापरण्यासाठी काहीही देण्याचे बंधन नाही - खरं तर आम्ही आपली आर्थिक किंवा सामाजिक स्थिती काय आहे याची पर्वा न करता दूरदूरच्या लोकांना याचा वापर करण्यास प्रोत्साहित करू इच्छितो - आमचा विश्वास आहे की स्थानिक निर्णय घेण्याच्या साधनांसह लोकांना सक्षम बनविणे संपूर्ण मानवतेसाठी एक चांगल्या समाजाचा परिणाम.

{{<table-of-contents >}}
## सामान्य
### वैशिष्ट्य: नवीन स्वागत स्क्रीन
फक्त रिक्त, पांढरा कॅनव्हास दाखविण्याऐवजी, QGIS आता आपल्या शेवटच्या सत्रामध्ये आपण सोडलेल्या कामात जलद आणि सुलभतेने प्रवेश मिळविण्यासाठी थंबनेलसह आपल्या अलीकडील प्रकल्पांची यादी दर्शवेल.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### वैशिष्ट्य: कोड गुणवत्तेत चालू असलेल्या सुधारणा
अ‍ॅड्रेस सॅनिटायझर लायब्ररीच्या वापराद्वारे, शेकडो मेमरी गळती ओळखल्या गेल्या आहेत आणि त्या निश्चित केल्या आहेत. कव्हरसिटी स्कॅन वापरुन स्वयंचलित कोड स्कॅन संभाव्य समस्या ओळखण्यासाठी नियमितपणे वापरली जात आहेत आणि आमची क्लोरिटी दोष घनता आता 1000 ओळींच्या कोड ओळीत केवळ 0.02 दोषांवर प्रभावीपणे कमी आहे. स्वयंचलित युनिट चाचण्यांच्या लायब्ररीमध्ये देखील 2.12 दरम्यान लक्षणीय वाढ झाली आहे, परिणामी अधिक दबाव ओळखले जातील आणि त्वरित निश्चित केले गेले. 2.12 मध्ये आम्ही ओएसएक्सवर सतत चाचणी देखील जोडली, जेणेकरून प्रत्येक कमिटची चाचणी लिनक्स आणि ओएसएक्स प्लॅटफॉर्मवर युनिट टेस्ट सुटच्या विरूद्ध केली जाईल.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### वैशिष्ट्य: प्रगत सेटिंग्ज संपादक
सेटिंग्ज संवादात एक नवीन पॅनेल जोडला गेला आहे जो आपल्या प्रोफाइलमध्ये आधीपासूनच परिभाषित केलेला कोणताही पर्याय आपल्याला संपादित करू देतो. हे फक्त वापरकर्त्यांकरिता आहे कारण आपण काय करीत आहात हे पूर्णपणे न समजता या सेटिंग्ज बदलल्यास आपण QGIS मध्ये अनपेक्षित वर्तन अनुभवू शकता.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### वैशिष्ट्यः परस्पर अनन्य थर झाडाचे गट
या वैशिष्ट्यासह, आपण स्तर गट तयार करू शकता जेथे गटातील फक्त एक स्तर कधीही दिसू शकेल. लेयर ट्री व्यू कॉन्टेक्स्ट मेनूमधील गटांसाठी हे वैशिष्ट्य स्वतंत्रपणे टॉगल केले जाऊ शकते.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

** या वैशिष्ट्यासाठी वित्तपुरवठा करण्यात आला: ** टस्कनी प्रदेश (इटली) - सीता (सीआयजी: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### वैशिष्ट्य: अभिव्यक्ती विजेटमधील फील्ड मूल्यांसाठी फिल्टरींग
फील्डमधून मूल्ये वापरणारी अभिव्यक्ती तयार करताना, आपण आता फील्ड मूल्ये पूर्वावलोकन पॅनेल फिल्टर करू शकता.

** हे वैशिष्ट्य विकसित केले होते: ** साल्वाटोर लरोसा

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### वैशिष्ट्य: वापरकर्ता इंटरफेस थीम समर्थन
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### वैशिष्ट्य: 2.12 मध्ये नवीन अभिव्यक्ती कार्ये
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

भूमितीवर आधारित अधिक कार्ये समाविष्ट केली गेली आहेत, यासह:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

या व्यतिरिक्त, काही अतिशय उपयुक्त अभिव्यक्ती एक्सप्रेशन्स + प्लगइन वरून पोर्ट केले गेले आहेत, यासह:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

याव्यतिरिक्त, अभिव्यक्ती फंक्शन्ससाठी संदर्भ मदत अधिक वाचनीयतेसाठी सुधारित केली गेली आहे.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### वैशिष्ट्य: अभिव्यक्तिंमध्ये चल
आपण आता अभिव्यक्तींमध्ये वापरण्यासाठी सानुकूल चल परिभाषित करू शकता. अनुप्रयोगांचे वैश्विक स्तर, प्रकल्प पातळी, स्तर पातळी आणि रचना पातळीवर व्हेरिएबल्स परिभाषित केल्या जाऊ शकतात. सीएसएस कॅस्केडिंग नियमांप्रमाणेच व्हेरिएबल्स अधिलिखित केले जाऊ शकतात - उदा. प्रोजेक्ट लेव्हल व्हेरिएबल कोणताही अ‍ॅप्लिकेशन लेव्हल व्हेरिएबल्स सेट अधिलिखित करेल. मजकूर तार किंवा इतर सानुकूल अभिव्यक्ती तयार करण्यासाठी आपण हे चल वापरू शकता. उदाहरणार्थ संगीतकारांद्वारे या सामग्रीसह एक लेबल तयार करणेः

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

यासारखे लेबल प्रस्तुत करेल:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## विश्लेषण साधने
### वैशिष्ट्य: साधनामध्ये साधित केलेल्या फील्डमध्ये शिरोबिंदूंची संख्या जोडली
लाइन वैशिष्ट्यावरील ओळखीचे साधन वापरणे आता अतिरिक्त व्युत्पन्न गुणधर्म म्हणून वैशिष्ट्यात शिरोबिंदूंची संख्या दर्शवेल.
### वैशिष्ट्य: रास्टर संरेखन साधन
This new tool in qgis_analysis library is able to take several rasters as input and:
- त्याच सीआरएसला पुन्हा प्रोजेक्ट करा
- समान सेल आकारात पुन्हा नमुना आणि ग्रिडमध्ये ऑफसेट करा
- आवडीच्या ठिकाणी क्लिप करा
- आवश्यक असल्यास व्हॅल्यू रीकेले करा

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### वैशिष्ट्य: भूमिती परीक्षक आणि भूमिती स्नॅपर प्लगइन
भूमिती सत्यापित करण्यासाठी आणि दुरुस्त करण्यासाठी दोन नवीन प्लगइन (जे आपल्याला व्यक्तिचलितपणे प्लगइन व्यवस्थापकात सक्षम करणे आवश्यक आहे) उपलब्ध आहेत. ** भूमिती परीक्षक ** प्लगइन (चित्रात उजवीकडे) आपला वेक्टर डेटासेट बर्‍याच प्रकारच्या विविध प्रकारच्या पद्धतशीर त्रुटींसाठी तपासेल आणि दुरुस्त करेल आणि आपल्यासाठी तो सोडवण्याचा प्रयत्न करेल. त्रुटीचे निराकरण झाल्यानंतर, त्रुटीची सूची स्वयंचलितपणे अद्यतनित केली जाते जेणेकरून, उदाहरणार्थ, एखादी त्रुटी निश्चित केल्याने इतर त्रुटींचे निराकरण केले तर सर्व त्रुटी समस्या सूचीमधून काढल्या गेल्या.

** भूमिती स्नॅपर ** साधनासह आपण वापरकर्त्यास परिभाषित सहिष्णुता वापरुन एका वेक्टर लेयरच्या कडा आणि शिरोबिंदू दुसर्‍या लेयरच्या कडा आणि शिरोबिंदु संरेखित करू शकता.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## अनुप्रयोग आणि प्रकल्प पर्याय
### वैशिष्ट्य: कूटबद्ध संकेतशब्द व्यवस्थापन
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- मास्टर-संकेतशब्द-एनक्रिप्टेड प्रमाणीकरण कॉन्फिगरेशन एका एसक्यूलाईट डेटाबेसमध्ये संग्रहित आहे
- प्रमाणीकरण पद्धत प्लगइन आर्किटेक्चर (डेटा प्रदात्यांसारखे)
- मूलभूत प्रमाणीकरण पद्धत प्लगइन
- मूलभूत प्लगइन पोस्टजीआयएस आणि ओडब्ल्यूएस प्रदाता कनेक्शनसह समाकलित केले
- वर्तमान वापरकर्तानाव / संकेतशब्द सेटअपसह इनलाइन (अद्याप पूर्णपणे कार्यशील)
- एसएसएल सर्व्हर कनेक्शन कॉन्फिगरेशन (एसएसएल कनेक्शन त्रुटींसाठी अपवाद किंवा सानुकूल कॉन्फिगरेशन जतन करा)

पीकेआय प्रमाणीकरण संबंधितः
- अतिरिक्त प्रमाणपत्र प्राधिकरणे, दरम्यानचे प्रमाणपत्र जारीकर्ता आणि वैयक्तिक ओळख बंडल आयात करा
- फायरफॉक्सप्रमाणे प्रमाणपत्र घटक व्यवस्थापित करा
- पीईएम आणि पीकेसीएस # 12 डिस्कवरील बंडल आणि संचयित वैयक्तिक ओळखीसाठी प्रमाणीकरण पद्धत प्लगइन
- ओडब्ल्यूएस प्रदाता कनेक्शनसह समाकलित केलेले (पोस्टजीआयएस आणि इतर डेटाबेस जरा अधिक काम घेतील)

नेटवर्क ड्राइव्ह सेटअपसह सामायिक केलेल्या प्रोजेक्ट परिदृश्यांसाठी, आपण वापरकर्त्यांमधून सामायिक केलेली काहीतरी प्रमाणीकरण कॉन्फिगरेशन (authcfg) आयडी संपादित करू शकता.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

हँडल बॅड लेयर डायलॉगसाठी, संवाद संवादात ऑथ कॉन्फिगरेशन जोडा / संपादित करू / काढून टाका आणि डेटा स्रोत युआरआय जुळण्यासाठी अद्ययावत करू शकता. तर, सामायिक केलेल्या प्रकल्पाच्या परिस्थितीत, वापरकर्ता त्वरित योग्य लोड ऑथ कॉन्फिगरेशन जोडू शकेल (आणि सामायिक केलेल्या ऑथकएफजी आयडी नक्की काय वापरायच्या हे पहा) प्रकल्प लोड झाल्यानंतर.

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**This feature was developed by:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## ब्राउझर
### वैशिष्ट्यः ब्राउझरमधील पोस्टजीआयएस कनेक्शनमध्ये सुधारणा
क्यूजीआयएस ब्राउझर आता पोस्टजीआयएस कनेक्शनसाठी अतिरिक्त कार्यक्षमतेस समर्थन देते, ** स्कीमा तयार करणे, नाव बदलणे आणि हटविणे **, ** स्तर पुनर्नामित करणे आणि छाटण्याकरिता समर्थन ** आणि ** एका स्कीमामधून दुसर्‍या ** सारण्या कॉपी करण्यासाठी ** .

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## डेटा प्रदात्या
### वैशिष्ट्यः पोस्टजीआयएस प्रदाता सुधारणा
पोस्टजीआयएस प्रदात्यामध्ये पुढील सुधारणे करण्यात आल्या:
- पोस्टजीआयएस स्तरांसाठी नियम आधारित रेन्डररसाठी कार्यप्रदर्शन सुधारणा
- दृश्यांवरील कंपाऊंड की करीता समर्थन समाविष्ट केले

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## माहिती व्यवस्थापन
### वैशिष्ट्यः डीबीमेनेजर सुधारणा
डीबी मॅनेजर टूलमध्ये बर्‍याच सुधारणा केल्या आहेत:
- डीबी मॅनेजरमध्ये आपण केवळ मागील आवृत्तीमध्ये उपलब्ध असलेल्या शेफाईलऐवजी कोणत्याही ओजीआर समर्थित डेटा स्वरूपात आपला डेटा निर्यात करू शकता.
- ओरॅकल स्पेशियल आता डीबी मॅनेजर मध्ये समर्थीत आहे
- एका टेबलमध्ये डेटा आयात करताना आपण नवीन ** केवळ निवडलेली वैशिष्ट्ये आयात करा ** काय आयात केले जाईल ते प्रतिबंधित करण्यासाठी पर्याय वापरू शकता.
- संवादांची संख्या कमी करण्यासाठी आता नवीन क्वेरी विंडो टॅब म्हणून तयार केल्या आहेत

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### वैशिष्ट्य: विशेषता सारख्या पेशींसाठी सशर्त स्वरूपन
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### वैशिष्ट्य: विजेटमधील सापेक्ष मार्गांसाठी समर्थन
खालील संपादन विजेट प्रकारांसाठी:
- फाईलचे नाव
- छायाचित्र
- वेब दृश्य

फाइल ब्राउझरसह निवडलेला मार्ग .qgs प्रोजेक्ट फाईलच्या खाली किंवा त्याच निर्देशिकेमध्ये असल्यास, पथ संबंधित मार्गात रूपांतरित केले जातात. यामुळे मल्टीमीडिया माहितीसह QGIS प्रोजेक्टची पोर्टेबिलिटी वाढते.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## डिजिटलायझेशन
### वैशिष्ट्य: डिजिटायझिंग सुधारणा
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- दोन बिंदू आणि त्रिज्यासह गोलाकार स्ट्रिंग जोडण्यासाठी टूल
- प्रारंभ बिंदू, वक्र बिंदू आणि अंतिम बिंदूसह परिपत्रक जोडण्यासाठी साधन
- नवीन वैशिष्ट्ये रेखाटण्यास सुटू द्या
- नोड टूलचा वापर करून संपादन करताना नोड सारणी प्रदर्शित करा, आपल्याला नोड्ससाठी स्वयंचलितपणे अचूक x आणि y निर्देशांक तसेच झेड आणि एम मूल्ये प्रविष्ट करा (स्तर प्रकारानुसार)

याव्यतिरिक्त, अधिक भूमिती संपादन आणि सुधारित साधने z किंवा मीटर परिमाण असलेल्या स्तरांसह योग्यरित्या कार्य करण्यासाठी अद्यतनित केली गेली.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## लेबलिंग
### Feature: Data defined quadrant when in \"around point\" mode
जेव्हा पॉइंट लेबल अराउंड पॉइंट प्लेसमेंट मोडवर सेट केले जाते तेव्हा डेटा परिभाषित क्वाड्रंट निर्दिष्ट करणे आता शक्य आहे. उर्वरित लेबले स्वयंचलित प्लेसमेंटवर परत येण्याची परवानगी देताना हे आपल्याला एका विशिष्ट लेबलसाठी चतुर्भुज प्लेसमेंट व्यक्तिचलितपणे अधिलिखित करण्याची परवानगी देते.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### वैशिष्ट्यः बहुभुज मध्ये बसणारी फक्त लेबल काढा
बहुभुज वैशिष्ट्यांमध्ये पूर्णपणे फिट असलेली लेबले काढण्यासाठी बहुभुज स्तरांवर एक पर्याय जोडला गेला आहे.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### वैशिष्ट्य: लेबलिंग अडथळ्यांवरील प्राधान्य नियंत्रित करा
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### वैशिष्ट्यः बहुभुज थर अडथळे म्हणून कार्य कसे करतात हे नियंत्रित करण्यासाठी नवीन पर्याय
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### वैशिष्ट्य: डेटा लेबल प्राधान्यावर नियंत्रण नियंत्रित
हे वारंवार विनंती केलेले वैशिष्ट्य वापरकर्त्यांना स्वतंत्र लेबलांसाठी प्राधान्य सेट करण्याची परवानगी देते. मागील रिलीझमध्ये क्यूजीआयएसने संपूर्ण लेयरसाठी लेबल प्राधान्य सेट करण्याची परवानगी दिली परंतु लेयरमध्ये वैशिष्ट्यांचा प्राधान्य नियंत्रित करण्याचा कोणताही पर्याय नव्हता. आता, आपण लेयरमध्ये इतरांपेक्षा विशिष्ट वैशिष्ट्यांचे लेबलिंग करण्यास प्राधान्य देण्यासाठी डेटा परिभाषित अभिव्यक्ती किंवा फील्ड वापरू शकता!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### वैशिष्ट्य: केवळ अडथळ्याच्या थरांसाठी पर्याय
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### वैशिष्ट्यः नियम-आधारित लेबलिंग
लेबलेच्या प्लेसमेंट आणि स्टाईलिंगवर आणखी अधिक नियंत्रण जोडण्यासाठी आता नियमांनुसार वैशिष्ट्यांवरील लेबलांची शैली केली जाऊ शकते. नियम आधारित कार्टोग्राफिक रेंडरिंग प्रमाणेच अत्यंत लवचिक स्टाईलिंग पर्यायांना अनुमती देण्यासाठी लेबल नियमांचे नेस्ट केले जाऊ शकते. उदाहरणार्थ आपण वैशिष्ट्यीकृत आकाराच्या आधारे आपण भिन्न लेबल प्रस्तुत करू शकता (स्क्रीनशॉटमध्ये स्पष्ट केल्याप्रमाणे).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

** या वैशिष्ट्यासाठी वित्तपुरवठा करण्यात आला: ** टस्कनी प्रदेश (इटली) - सीता (सीआयजी: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## नकाशा संगीतकार
### वैशिष्ट्य: lasटलस नॅव्हिगेशन सुधारणा
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

पृष्ठाचे नाव चिन्हांच्या आणि लेबलिंग अभिव्यक्तींमध्ये देखील त्यांच्या पृष्ठाच्या नावावर आधारित अ‍ॅटलास वैशिष्ट्यांचे प्रगत स्टाईलिंग अनुमत करण्यासाठी वापरले जाऊ शकते.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### वैशिष्ट्य: ग्रिड भाष्यांकरिता सानुकूल स्वरूप
संगीतकार नकाशा ग्रीड भाष्ये आता सानुकूल स्वरूपात स्वरूपित केली जाऊ शकतात, ज्यांचे अभिव्यक्ती इंजिन वापरून मूल्यमापन केले जाते. आता आपण आपल्या नकाशेमध्ये आवश्यक असलेल्या विलक्षण ग्रिड क्रमांकन स्वरूपनाचा वापर करा!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### वैशिष्ट्य: मल्टीलाइन मजकूर हाताळणी आणि संगीतकार विशेषता सारण्यांमध्ये स्वयंचलित मजकूर लपेटणे
संगीतकार विशेषता सारण्यांमध्ये आता मल्टी लाइन तारांसाठी पूर्ण समर्थन समाविष्ट आहे. सेलमधील मजकूराच्या अनुलंब संरेखनावर नियंत्रण देखील जोडले गेले आहे, विशिष्ट वर्णांवर मजकूर गुंडाळण्यासाठी किंवा स्तंभांच्या आकारात फिट होण्यासाठी मजकूर लपेटण्यासाठी स्वयंचलितपणे गणना करणे. स्वयंचलित पंक्ती उंचीसह स्वयंचलित मजकूर रॅपिंगची अंमलबजावणी करण्यासाठी, स्तंभ रूंदी निश्चित आकारात सेट करा.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### वैशिष्ट्यः सेल पार्श्वभूमी रंगाचे प्रगत सानुकूलन
हा बदल वापरकर्त्यांना पंक्ती आणि स्तंभ, प्रथम / शेवटची पंक्ती / स्तंभ आणि संगीतकार विशेषता सारणीमध्ये शीर्षलेख पंक्तीसाठी भिन्न रंग सेट करण्याची अनुमती देतो.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### वैशिष्ट्य: सामग्रीवर फिट पृष्ठ जोडा आणि सामग्रीवर पीक निर्यात करण्यासाठी पर्याय
आवश्यक असल्यास पर्यायी अतिरिक्त मार्जिनसह रचनातील सामग्रीचे आकार बदलण्यासाठी रचना पॅनेलमध्ये एक नवीन पर्याय जोडला गेला आहे.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

हे सुलभ करण्यासाठी एक नवीन प्रतिमा निर्यात पर्याय संवाद जोडला गेला आहे, ज्यात प्रिंट रेझोल्यूशन किंवा एक्सपोर्ट केलेल्या प्रतिमेचे आकार अधिलिखित करण्यासाठी सुलभ शॉर्टकट देखील आहेत.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### वैशिष्ट्य: रास्टर प्रतिमेच्या रूपात प्रस्तुत करण्यासाठी वेक्टर स्तरांवर दबाव आणा
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### वैशिष्ट्यः नकाशा स्तरांवर आणि शैली प्रीसेटवर डेटा परिभाषित नियंत्रण
संगीतकार नकाशामध्ये दर्शविण्यासाठी नकाशा स्तर आणि शैली प्रीसेटसाठी एक नवीन डेटा परिभाषित नियंत्रण जोडला गेला आहे. नकाशा स्तरांवर डेटा परिभाषित अभिव्यक्तीचा परिणाम. | (पाईप) थर नावांची मर्यादीत यादी जी नकाशामध्ये दर्शविली जाईल किंवा शैली प्रीसेट डेटा परिभाषित अभिव्यक्तीचा परिणाम विद्यमान शैली प्रीसेटच्या नावावर असावा.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### वैशिष्ट्य: दृश्य / निर्यातीतून पृष्ठे लपविण्याचा पर्याय
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## प्लगइन्स
### वैशिष्ट्य: ग्रॉस प्लगइनचे अद्यतन
ग्रॅस 7 साठी समर्थन सक्षम करण्यासाठी ग्रास प्लगइन अद्ययावत केले गेले. क्यूजीआयएस ब्राउझर किंवा ब्राउझर पॅनेलमधून ग्रास स्तर ब्राउझ आणि लोड केले जाऊ शकतात. ग्रॉस वेक्टर डेटा क्यूजीआयएसमध्ये थेट संपादित केला जाऊ शकतो. प्रकल्पात खालील कार्य पॅकेजेस आहेत:
- प्लगिन लायब्ररी अपग्रेड आणि मल्टी व्हर्जन बिल्ड
- QGIS ब्राउझर आणि ब्राउझर पॅनेल एकत्रीकरण
- डेटा विश्लेषणास अनुमती देण्यासाठी नकाशेसेट, मॉड्यूल आणि शेलसाठी समर्थन
- वेक्टर संपादन

ग्रॅस 6 आणि ग्रॅस 7 वापरकर्त्यांसाठी आपणास आढळेल की ग्रास व क्यूजीआयएस मधील एकीकरण अधिक निर्बाध आहे. आपण क्यूजीआयएस ब्राउझर पॅनेलमध्ये थेट ग्रास स्तर तयार करू शकता, मानक क्यूजीआयएस स्टाईलिंग साधने वापरुन स्टाईल ग्रॉस वेक्टर स्तर आणि ग्रास मॅपसेटमध्ये नवीन सदिश भूमिती तयार करण्यासाठी परिचित क्यूजीआयएस डिजिटलाइझिंग साधने वापरू शकता.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## कार्यक्रमक्षमता
### Feature: Map tools moved from app-\>gui
हा बदल पायक्यूजीआयएस स्क्रिप्ट आणि पायथन प्लगइन मधून नकाशे साधनांचा पुनर्वापर करण्यास अनुमती देतो.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### वैशिष्ट्य: संपादन (स्तर) सह \ via मार्गे स्तरांचे संपादन: \ `
उदाहरणः

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
हे शेवटी आपोआप कमिटचेंजस () कॉल करेल. कोणताही अपवाद आढळल्यास ते सर्व बदल रोलबॅक करेल ().

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### वैशिष्ट्यः लेबलिंग इंजिनसाठी नवीन एपीआय (QgsLabelingEngineV2)
QgsPalLabeling अंमलबजावणीच्या तुलनेत इंजिनला अधिक लवचिक बनविण्याची कल्पना आहेः
> - इंजिनमधूनच मजकूर लेबले / आकृत्यांबरोबर अमूर्त व्यवहार
> - प्रति लेयरच्या अनेक प्रकारच्या लेबलांना अनुमती द्या
> - सानुकूल लेबल प्रदात्यांचे समर्थन करा (उदा. प्लगइनद्वारे लागू केलेले)
> - नकाशा प्रस्तुत इंजिनपासून लेबलिंग इंजिन स्वतंत्र करा
> - लेबलिंग इंजिन आणि त्याचे घटकांची स्वयं-चाचणी करणे सुलभ करा

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

** या वैशिष्ट्यासाठी वित्तपुरवठा करण्यात आला: ** टस्कनी प्रदेश (इटली) - सीता (सीआयजी: 63526840AE)
### वैशिष्ट्य: बाह्य संपादकात स्क्रिप्ट उघडा
पायथोनिस्टास आनंद करा - आता आपण कन्सोलमध्ये जोडलेले नवीन बटण वापरून आपल्या स्क्रिप्ट्स बाह्य संपादकात उघडू शकता.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### वैशिष्ट्यः पायक्जीआयजीएस प्रोग्राम्ससाठी नवीन वर्ग
एक नवीन वर्ग QgsStringUtils समाविष्ट केला गेला आहे जो PyQGIS स्क्रिप्टला 2.12 मध्ये जोडल्या गेलेल्या नवीन अस्पष्ट मॅचिंग अल्गोरिदमचा वापर करण्यास परवानगी देतो. यामध्ये दोन स्ट्रिंग दरम्यान लेव्हनश्टिन संपादन अंतर शोधण्यासाठी आणि स्ट्रिंगच्या ध्वन्यात्मक ध्वन्यात्मक प्रतिनिधित्वाची गणना करण्यासाठी कार्य समाविष्ट आहे. हे अल्गोरिदम कामगिरीसाठी अत्युत्तम केले गेले आहेत, म्हणूनच कोट्यवधी तारांमध्ये अस्पष्ट जुळणी सुरू करण्यासाठी ते तयार आहेत!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS सर्व्हर
### वैशिष्ट्यः क्यूजीआयएस सर्व्हर पायथन एपीआय
क्यूजीआयएस सर्व्हर आता प्रारंभिक (परंतु वाढणारी) एपीआय आणि पायथन बाइंडिंगसह लायब्ररी म्हणून भरलेले आहे. नवीन एपीआय सह आमच्याकडे सर्व्हर मुख्य घटक आणि सर्व्हर प्लगइनसाठी पायथन चाचण्यांचा एक संच आहे. पायथन वरून सर्व्हर चालू करणे आता जितके सोपे आहे:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### वैशिष्ट्य: डीएक्सएफ स्वरूपात getMap
आता डीएक्सएफ स्वरूपात गेटमॅप डब्ल्यूएमएस विनंतीचा निकाल प्राप्त करणे शक्य आहे. हे QGIS डेस्कटॉपमध्ये उपलब्ध असलेल्या समान वैशिष्ट्ये आणि पर्यायांना समर्थन देते. त्याच मर्यादांसह.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

स्क्रीनशॉटमध्ये आपणास डीएक्सएफ एक्सपोर्ट फंक्शनॅलिटी (क्यूजीआयएस सर्व्हर वापरणे) आणि डावीकडील उजव्या बाजूला ऑटोडस्क ट्रू व्ह्यूमध्ये पाहिले गेलेली क्यूजीआयएस वेब क्लायंट दिसते.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## प्रतीकशास्त्र
### वैशिष्ट्य: स्टाईल व्यवस्थापकाकडून लघुप्रतिमा निर्यात करा
शैली व्यवस्थापक आता आपल्याला निवडक शैली लघुप्रतिमा एसव्हीजी किंवा पीएनजी प्रतिमा म्हणून निर्यात करू देते.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### वैशिष्ट्यः नकाशा युनिट आकार वापरताना मिमी मध्ये मर्यादा घालण्यासाठी नवीन पर्याय
यापूर्वी केवळ नकाशा युनिट आकारांच्या स्केल श्रेणी मर्यादित करण्याचा पर्याय उपलब्ध होता. आता आपण मिमी मध्ये संबंधित प्रस्तुत आकार मर्यादित करणे देखील निवडू शकता.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### वैशिष्ट्य: विस्थापन प्रस्तुतकर्त्यामध्ये सुधारणा
- विस्थापन प्रस्तुतकर्त्यासाठी मिमी / पिक्सेलमध्ये सहनशीलता द्या
- रंगांसाठी पारदर्शकता सेट करण्याची परवानगी द्या
- कॉन्सेन्ट्रिक रिंग प्लेसमेंट मोड (केवळ रिंगशिवाय अधिक कॉम्पॅक्ट प्रदर्शनास अनुमती देते)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### वैशिष्ट्य: सर्व रंग रॅम्प आता संपादित केले जाऊ शकतात
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### वैशिष्ट्यः एसव्हीजी मार्कर बाह्यरेखा सुधारित हाताळणी
क्यूजीआयएस 2.12 एसव्हीजी मार्कर आणि एसव्हीजी फिल प्रतीकांमधील बाह्यरेखा हाताळण्याशी संबंधित अनेक प्रकरणांचे निराकरण करते.

क्यूजीआयएसच्या मागील आवृत्त्या सेटपेक्षा लक्षणीय लहान आकारात बाह्यरेखा प्रस्तुत करतील आणि नकाशा युनिटमध्ये बाह्यरेखा आकाराने एसव्हीजी रेखाटणे खंडित झाले.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### वैशिष्ट्य: सर्व प्रतीक आकाराच्या युनिट निवडींसाठी पर्याय म्हणून पिक्सल जोडा
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
