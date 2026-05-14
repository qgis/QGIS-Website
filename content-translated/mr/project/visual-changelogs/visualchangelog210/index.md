---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: project
sidebar: true
title: क्यूजीआयएस 2.10 चा चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.10 चा चेंजलॉग{#changelog210 }
Release date: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

** नवीनतम प्रकाशन **

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**धन्यवाद**

आम्ही विकसक, दस्तऐवजकार, परीक्षक आणि तेथील सर्व लोकांना त्यांचे आभार मानू इच्छितो जे आपला वेळ आणि मेहनत स्वयंसेवक करतात (किंवा लोकांना यासाठी पैसे देतात).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

शेवटी आम्ही आमच्या अधिकृत प्रायोजकांना या प्रकल्पात त्यांना देत असलेल्या अमूल्य आर्थिक मदतीबद्दल आभारी आहोत:
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

क्यूजीआयएस हे एक विनामूल्य सॉफ्टवेअर आहे आणि आपण ते वापरण्यासाठी काहीही देण्याचे बंधन नाही - खरं तर आम्ही आपली आर्थिक किंवा सामाजिक स्थिती काय आहे याची पर्वा न करता दूरदूरच्या लोकांना याचा वापर करण्यास प्रोत्साहित करू इच्छितो - आमचा विश्वास आहे की स्थानिक निर्णय घेण्याच्या साधनांसह लोकांना सक्षम बनविणे संपूर्ण मानवतेसाठी एक चांगल्या समाजाचा परिणाम.

{{<table-of-contents >}}
## सामान्य
### वैशिष्ट्य: जॉइन पॅरामीटर्स आता संपादित केली जाऊ शकतात
जॉइन तयार झाल्यावर जॉइन पॅरामीटर्स (जसे की सामील होण्यासाठी उपसर्ग किंवा स्तंभांमध्ये सामील होणे) संपादित करणे आता शक्य झाले आहे. या बदलापूर्वी एखाद्यास संपूर्ण जोड हटवणे आणि पुन्हा तयार करावे लागले.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### वैशिष्ट्यः सामील होणारे स्तर आता फिल्टर केले जाऊ शकतात
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### वैशिष्ट्य: सामान्य सुधारणा
खाली सूचीबद्ध असंख्य आयटम प्रमाणेच, पुढील सुधारणाही करण्यात आल्या आहेत:
- पोस्टजीआयएस मधील पॉईंटक्लॉड स्तरांसाठी समर्थन
- कमी स्क्रीन रीअल इस्टेट व्यापण्यासाठी आणि सुधारित ओएसएक्स देखाव्यासाठी डॉक करण्यायोग्य विजेट्समधील सुधारित चिन्ह बार आणि चिन्हे
- जीआरएआरएसएस प्लगइन / प्रदात्यावर सुधारणा
- वक्र लेबलसाठी नॉन-लॅटिन स्क्रिप्टसाठी समर्थन
- मोठ्या प्रमाणात सुधारित आणि अधिक मजबूत रास्टर कॅल्क्युलेटर आणि जियोरिफरन्सर टूल्स
- डेटा परिभाषित लेबल गुणधर्म विंडोसाठी सुधारित यूआय आणि वर्कफ्लो

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### वैशिष्ट्य: संभाव्य प्रोजेक्ट फाईल अधिलिखितची सुधारित हाताळणी
लोड केलेल्या प्रकल्पाची अंतिम तारीख बदलली असल्यास आपला प्रकल्प वाचविण्याचा प्रयत्न करताना क्यूजीआयएस 2.10 आता आपल्याला चेतावणी देईल. एकापेक्षा जास्त वापरकर्त्यांकडे किंवा सत्रामध्ये समान प्रकल्प फाइल उघडल्यास आणि दोन्ही प्रकल्प फाइलमध्ये संपादने जतन करण्याचा प्रयत्न करीत असल्यास हे उपयुक्त आहे.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### वैशिष्ट्य: नवीन भूमिती इंजिन
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## विश्लेषण साधने
### वैशिष्ट्य: नवीन सांख्यिकी सारांश डॉक विजेट
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### वैशिष्ट्य: रास्टर कॅल्क्युलेटरमध्ये लॉगरिथमिक फंक्शन्स वापरा
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### वैशिष्ट्य: नवीन विभागीय आकडेवारी वैशिष्ट्ये
क्षेत्रीय आकडेवारी बहुभुज अंतर्गत असलेल्या पिक्सेलसाठी एकत्रित मूल्ये काढण्याचा मार्ग प्रदान करते. आमच्या विभागीय आकडेवारी साधनामध्ये पुढील नवीन वैशिष्ट्ये जोडली गेली आहेत:
- आपण आता कोणत्या आकडेवारीची गणना करायची ते निवडू शकता
- अतिरिक्त आकडेवारी जोडली गेली आहे (मध्यम, मानक देव, किमान, कमाल, श्रेणी, अल्पसंख्याक, बहुमत आणि विविधता)
- आकडेवारीच्या माहितीसाठी वापरण्यासाठी रास्टर बँड निवडण्याची क्षमता

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## ब्राउझर
### वैशिष्ट्य: नवीन ब्राउझर गुणधर्म विजेट
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### वैशिष्ट्य: नवीन ब्राउझर चिन्ह
क्यूजीआयएस ब्राउझर हा एक स्वतंत्र, स्वतंत्र अनुप्रयोग आहे जो आपल्याला आपल्यास उपलब्ध असलेल्या जीआयएस डेटासेट ब्राउझ करण्यास आणि पाहण्याची परवानगी देतो (आपल्या फाईल सिस्टम, डेटाबेस कनेक्शन, वेब सेवा कनेक्शन इ.) क्यूजीआयएसच्या मागील प्रकाशनात आम्ही समान प्रकारचे चिन्ह वापरले होते क्यूजीआयएस अनुप्रयोग स्वतःच जो बर्‍याच वापरकर्त्यांसाठी गोंधळ उडाला आहे. चुकीचे अनुप्रयोग उघडण्यासारखेपणा कमी करण्यासाठी आम्ही क्यूजीआयएस ब्राउझरसाठी एक नवीन प्रतीक तयार केले आहे.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## डेटा प्रदात्या
### वैशिष्ट्यः डीएक्सएफ निर्यात सुधारणा
मागील तीन क्यूजीआयएस आवृत्तीमध्ये डीएक्सएफ निर्यात निरंतर सुधारित केली गेली. ही आवृत्ती डीएक्सएफ ब्लॉक रूपांतरणात सुधारित एसव्हीजी किंवा साधे मार्करची ओळख करुन देते, काही दोष आणि समस्यांचे निराकरण करते ज्याच्या परिणामी अपूर्ण (अवाचनीय) डीएक्सएफ फायली बनल्या. स्क्रीनशॉटमध्ये आपण डावीकडे क्यूजीआयएस मधील मूळ दृश्य आणि उजवीकडे ऑटोडेस्क ट्रू व्ह्यूमध्ये निर्यात केलेल्या डीएक्सएफ फाईलचे प्रस्तुतीकरण पाहू शकता.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

** या वैशिष्ट्यासाठी वित्तपुरवठा करण्यात आला: ** मॉर्गेज, युस्टर, वेवे आणि साइन इनचे समुदाय

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### वैशिष्ट्यः पोस्टजीआयएस प्रदाता साइड एक्सप्रेशन फिल्टर
QGIS 2.10 मध्ये आपण आता डेटाबेस सर्व्हर बाजूला वैशिष्ट्ये फिल्टर करू शकता. केवळ समर्थित अभिव्यक्ती डेटाबेसवर पाठविली जातील. असमर्थित ऑपरेटर किंवा कार्ये वापरून अभिव्यक्ती स्थानिक मूल्यमापन करण्यासाठी कृपापूर्वक फॉलबॅक होतील.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

किंवा

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## माहिती व्यवस्थापन
### वैशिष्ट्यः आभासी फील्ड आता अद्ययावत करण्यायोग्य आहेत
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### वैशिष्ट्यः व्हॅल्यू रिलेशन संपादन विजेटसाठी स्वयं-परिपूर्णसह लाइन संपादन
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### वैशिष्ट्यः डीबी व्यवस्थापकात सुधारणा
डीबी व्यवस्थापकात दोन नवीन वैशिष्ट्ये आहेतः

** लेयर म्हणून क्वेरीसाठी यापुढे अद्वितीय पूर्णांक स्तंभ आवश्यक नाही **

क्यूजीआयएस लेयर म्हणून एसक्यूएल क्वेरी लोड करण्यासाठी यापुढे अद्वितीय पूर्णांक स्तंभ असलेल्या स्तंभाची आवश्यकता नाही. त्या ठिकाणी स्वयं-वर्धित मूल्य वापरले जाईल.

** एस क्यू एल क्वेरी बिल्डरचे एकत्रीकरण **

डीबी मॅनेजरमधील एक नवीन विंडो एसक्यूएल क्वेरी तयार करण्यात मदत करते विजेटच्या माध्यमातून जिथे टेबलद्वारे नावे, स्तंभ नावे आणि कार्ये वापरकर्त्याद्वारे निवडली जाऊ शकतात. हे QSpatialite प्लगइनवरून पोर्ट केले गेले आहे आणि पोस्टजीआयएस आणि स्पॅटालाइट प्रदात्यांसाठी कार्य करते.

** ही वैशिष्ट्ये ** द्वारा समर्थित: एमईडीडीई (टिकाऊ विकास मंत्रालय फ्रेंच मंत्रालय)

** ही वैशिष्ट्ये **: ह्यूगो मर्सियर / ओस्लंडिया द्वारा विकसित केली गेली

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### वैशिष्ट्य: संबंध संदर्भ विजेटसाठी फिल्टर साखळी
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## आकृत्या
### वैशिष्ट्य: आकृती सुधारणे
क्यूजीआयएस मधील आकृती कार्यक्षमता आपल्याला नकाशावरील वैशिष्ट्यांवरून लहान पाय चार्ट किंवा हिस्टोग्राम आच्छादित करण्यास परवानगी देते. या रीलिझमध्ये आम्ही आकृत्या समर्थनासाठी पुढील सुधारणा केल्या आहेत:
- सेटिंग्ज न गमावता रेखाचित्र अक्षम केले जाऊ शकतात
- लेयरसाठी नेहमीच आकृती दर्शविण्यासाठी चेकबॉक्स जोडा
- संवाद सुलभ करण्यासाठी आणि त्यास अधिक वापरकर्ता अनुकूल बनविण्यासाठी आकृती वापरकर्त्याचा संवाद रीफ्रेश केला आहे
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## डिजिटलायझेशन
### वैशिष्ट्य: सुधारित भूमिती फिरविणे साधन
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- आपण आता रोटेशन मॅप टूलमध्ये संख्यात्मक इनपुट वापरू शकता
- कोन सेट करण्यासाठी आपण कॉम्बो बॉक्स वापरू शकता
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## लेबलिंग
### Feature: \"Follow point\" alignment for multiline labels
जेव्हा या मोडवर सेट केलेले असते तेव्हा लेबलांसाठी मजकूर संरेखन बिंदूशी संबंधित लेबलच्या अंतिम स्थानावर अवलंबून असते. उदाहरणार्थ, जर लेबल बिंदूच्या डावीकडे ठेवले असेल तर लेबल उजवीकडे संरेखित केले जाईल आणि ते बिंदूच्या उजवीकडे ठेवल्यास लेबल डावीकडे संरेखित केले जाईल. हे पॉइंट लेयर्ससाठी मल्टीलाइन लेबल्सचे स्वरूप मोठ्या प्रमाणात सुधारते.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## नकाशा संगीतकार
### वैशिष्ट्यः इच्छित स्केलबार रूंदीमध्ये फिट होण्यासाठी स्केलबार आकार बदलण्याची मोड जोडा
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## कार्यक्रमक्षमता
### वैशिष्ट्य: प्रोग्रामरसाठी सुधारणा
आम्ही बर्‍याच बदल आणि सुधारणा केल्या आहेत जे विकासकांच्या हिताचे असतील:
- आम्ही क्यूटी 4 ते आवृत्ती 4.8 ची किमान आवश्यकता पूर्ण केली. क्यूटी 4 मुख्य सी ++ टूलकिट्स / लायब्ररीपैकी एक आहे जे आपण क्यूजीआयएस तयार करण्यासाठी वापरतो.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- वेक्टर लेयर डेटा स्त्रोत बदलण्याची परवानगी द्या.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS सर्व्हर
### वैशिष्ट्य: डब्ल्यूएमएस गेटफीचरइन्फो विनंत्यांमध्ये सहिष्णुता मापदंडासाठी समर्थन
क्यूजीआयएस सर्व्हरद्वारे डब्ल्यूएमएस स्तर वापरताना, आपण आता क्लिक फ्रि गेटफीचरइन्फो विनंत्या किती दूर मानल्या पाहिजेत याबद्दल सहिष्णुता निर्दिष्ट करू शकता. मोबाइल डिव्हाइससाठी हे महत्वाचे आहे जिथे वैशिष्ट्यांकडे नेणे अगदी कठीण आहे. या नवीन वैशिष्ट्यापूर्वी, क्यूजीआयएस सर्व्हरसह मोबाइल डिव्हाइसवरील पॉइंट किंवा लाइन वैशिष्ट्ये ओळखणे व्यावहारिकदृष्ट्या अशक्य होते. आपण आपल्या GetFeatureInfo विनंत्यांमध्ये खालील पॅरामीटर्स जोडू शकता:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

आणि आपल्या आवश्यकतेनुसार सहिष्णुता मूल्ये (पिक्सेलमध्ये) बदला.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## प्रतीकशास्त्र
### वैशिष्ट्य: विद्यमान शैलींमध्ये श्रेणी जोडा
स्टाईल लायब्ररी किंवा एक्सएमएल शैली फाईलमधील जुळणार्‍या नावाच्या चिन्हावर श्रेणी सेट करण्यासाठी श्रेणीबद्ध प्रस्तुत प्रगत मेनू अंतर्गत पर्याय जोडा.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### वैशिष्ट्य: पदवीधर प्रस्तुतकर्त्याचा वापर करून चिन्हांच्या आकारात बदल करा
प्रस्तुतकर्ता क्यूजीआयएसचे सबसिस्टम आहेत जे आपल्याला आपल्या डेटाची समृद्ध कार्टोग्राफिक प्रतिनिधित्व तयार करण्याची परवानगी देतात. पदवी प्राप्तकर्ता वेक्टर लेयरमधील सतत बदलणार्‍या मूल्याच्या आधारे प्रतीकशास्त्र बदलते. QGIS च्या मागील आवृत्त्यांमध्ये आपण केवळ रंग बदलू शकता (उदा. कलर रॅम्पच्या बाजूने रंग वापरुन). क्यूजीआयएस 2.10 मध्ये, पदवीधर प्रतीक प्रस्तुतकर्ता आता आपल्याला आकार * किंवा * रंग बदलू देतो. पॉइंट लेयर्ससाठी आपण पॉइंट साइज बदलू शकता, ओळींसाठी आपण लाईन रूंदी बदलू शकता. बहुभुज स्तर फक्त रंगानुसार बदलण्याची क्षमता राखून ठेवतात, रेखा रुंदी अद्याप समर्थित नाही.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### वैशिष्ट्य: नकाशा मर्यादेपर्यंत वैशिष्ट्यांचे स्वयंचलित क्लिपिंग प्रतिबंधित करण्यासाठी नवीन पर्याय
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### वैशिष्ट्य: प्रगत मेनूमधून आकारमान आणि फिरविणे काढले गेले आहे
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### वैशिष्ट्य: फॉन्ट मार्करसाठी डेटा परिभाषित गुणधर्म
फाँटर मार्करचे बहुतेक गुणधर्म आता मार्करचा आकार, फिरविणे आणि वर्ण यासह डेटा परिभाषित केला जाऊ शकतो.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### वैशिष्ट्य: हिस्टोग्राम वापरुन पदवीधर प्रस्तुतकर्ता व्हिज्युअल बनवा आणि सुधारित करा
ग्रॅज्युएटेड रेन्डररमध्ये नवीन हिस्टोग्राम टॅब जोडला गेला आहे, जो नियुक्त केलेल्या फील्ड किंवा अभिव्यक्तिमधील मूल्यांचा परस्पर हिस्टोग्राम दर्शवितो. हिस्टोग्राम वापरून वर्ग ब्रेक हलविले किंवा जोडले जाऊ शकतात.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### वैशिष्ट्य: आकार, फिरविणे आणि स्ट्रोक-रुंदीचे अभिव्यक्ति प्रतीक चिन्ह स्तरावर
आकार आणि फिरविणे मार्कर बनविणार्‍या सर्व प्रतीक स्तरावरील अभिव्यक्तीद्वारे परिभाषित केले जाऊ शकते. रेखा बनविणार्‍या सर्व चिन्हांच्या अभिव्यक्तीद्वारे रूंदीची व्याख्या केली जाऊ शकते.

किंवा चिन्हे म्हणून, विविध आकारांसाठी एक आख्यायिका व्युत्पन्न केली जाते. हे वर्गीकृत / पदवीधर रंगांच्या बाबतीत मल्टिव्हिएट विश्लेषण विश्लेषणास अनुमती देते.

वापरकर्त्याचे आकार अभिव्यक्ती परिभाषित करण्यात मदत करण्यासाठी, सहाय्यक, पूर्वावलोकनासह डेटा परिभाषित डेटाद्वारे प्रवेशयोग्य असतो. तीन पद्धती उपलब्ध आहेतः फ्लॅनेरी, क्षेत्र आणि त्रिज्या.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### वैशिष्ट्य: स्तर आणि प्रतीक स्तरांसाठी थेट स्तर प्रभाव
रेंडर चेनमध्ये विविध रेंडर इफेक्ट जोडण्याची क्षमता जोडून लाइव्ह लेयर इफेक्ट क्यूजीआयएसच्या आधीपासूनच विस्तृत कार्टोग्राफिक क्षमतांमध्ये भर घालतात. थेट प्रभावांसह आपण आपल्या चिन्हाखाली ड्रॉप सावली ठेवणे, रेखांकित चिन्हे स्क्यूइंग आणि कातरणे यासारख्या गोष्टी करू शकता. आपण हे प्रभाव एकमेकांच्या वरच्या बाजूस देखील ठेवू शकता आणि प्रभाव प्रगतीशील असावा की नाही ते सेट करू शकता (उदा. आतापर्यंत प्रस्तुत केलेल्या स्थितीवर स्वत: ला लागू करा) किंवा स्वतंत्र (स्त्रोत भूमिती पुन्हा प्रस्तुत करण्याच्या शृंखलामध्ये पुन्हा इंजेक्शन देऊन).

** टीप **: हे प्रगत वापरकर्त्यांसाठी कार्यक्षमता आहे आणि आम्ही हे लक्षात घेतले पाहिजे की या वैशिष्ट्याचा अतिवापर केल्यामुळे वेळा प्रस्तुत करणे लक्षणीय प्रमाणात कमी होऊ शकते, जेणेकरून आपण आपल्या लेयरसाठी भिन्न प्रतीकात्मक प्रोफाइल असल्याचे विचार करू शकता - उत्पादन गुणवत्तेच्या नकाशे तयार करण्यासाठी आणि ड्राफ्ट मोडसाठी एक.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
