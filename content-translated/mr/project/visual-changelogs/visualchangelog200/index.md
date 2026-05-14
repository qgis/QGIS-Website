---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: project
sidebar: true
title: QGIS 2.0 साठी चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.0 साठी चेंजलॉग{#changelog20 }
प्रकाशनाची तारीख : 2013-09-09

{{<table-of-contents >}}
## विश्लेषण साधने
### वैशिष्ट्य: प्रोसेसिंग कमांडर
जिओप्रोसेसिंग कार्यक्षमतेत द्रुत प्रवेशासाठी, फक्त प्रोसेसिंग कमांडर (Ctrl + Alt + M) लाँच करा आणि आपण ज्या साधनाचा शोध घेत आहात त्याचे नाव टाइप करण्यास प्रारंभ करा कमांडर आपल्याला उपलब्ध पर्याय दर्शवेल आणि त्या आपल्यासाठी त्यास लाँच करेल. मेनूद्वारे शोधणे आवश्यक नाही. साधने शोधण्यासाठी. ते आता आपल्या बोटांच्या टोकावर आहेत.

![image1](images/processing_commander_2.png)
### वैशिष्ट्यः हीटमॅप प्लगइन सुधारणा
हीटमॅप प्लगइनमध्ये असंख्य सुधारणा आणि ऑप्टिमायझेशन दिसून आले आहेत, परिणामी उष्णतेचे नकाशे अधिक वेगाने तयार झाले आहेत. याव्यतिरिक्त, तुम्हाला आता हीटमॅप तयार करण्यासाठी कोणते कर्नेल फंक्शन वापरले जाते याची निवड करता येईल.

![image2](images/Selection_027.png)
### वैशिष्ट्य: प्रक्रिया समर्थन
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### वैशिष्ट्य: प्रोसेसिंग मॉडेलर
नवीन प्रक्रिया फ्रेमवर्कची एक उत्तम वैशिष्ट्ये म्हणजे साधने ग्राफिकरित्या एकत्र करण्याची क्षमता. ** प्रोसेसिंग मॉडेलर ** वापरुन, आपण लहान एकल प्रयोजन मॉड्यूलच्या मालिकेतून जटिल विश्लेषण तयार करू शकता. आपण या मॉडेल्स जतन करू शकता आणि नंतर अद्भुत उर्जा बरोबरच QGIS मध्ये समाकलित झाली आणि वापरण्यास सुलभ आहे!

![image4](images/Processing_modeler_029.png)
## अनुप्रयोग आणि प्रकल्प पर्याय
### वैशिष्ट्य: डीफॉल्ट प्रारंभ प्रकल्प आणि प्रकल्प टेम्पलेट परिभाषित करा
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### वैशिष्ट्यः सिस्टम पर्यावरण वातावरण
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### वैशिष्ट्य: वापरकर्ता-परिभाषित झूम स्केल
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## ब्राउझर
### वैशिष्ट्यः अ‍ॅप-मधील ब्राउझर पॅनेलमधील सुधारणा
- निर्देशिका वाईल्डकार्ड किंवा रेजेक्स अभिव्यक्तीद्वारे फिल्टर केल्या जाऊ शकतात.
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
-  आयटम ग्रुप प्रकारानुसार आयकॉन आता क्रमबद्ध केले जातात (फाइलसिस्टम, डेटाबेस, नकाशा सर्व्हर)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## डेटा प्रदात्या
### वैशिष्ट्य: रास्टर डेटा प्रदाता तपासणी
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### वैशिष्ट्य: ओरॅकल स्थानिक समर्थन
QGIS 2.0 मध्ये आता ओरॅकल स्थानिक समर्थन समाविष्ट आहे.

![image10](images/oracle.png)
### वैशिष्ट्य: वेब कव्हरेज सेवा प्रदाता जोडला आहे.
QGIS आता वेब कव्हरेज सर्व्हिस लेयर्ससाठी नेटिव्ह समर्थन पुरवतो - WCS  जोडण्यासाठीची प्रक्रिया WMS लेयर किंवा WFS लेयर जोडण्याइतकीच आहे.
### वैशिष्ट्य: डिफॉल्टनुसार 2% संचयी कपात
बऱ्याच रास्टर प्रतिमांच्या उत्पादनांमध्ये मोठ्या संख्येने बाह्यघटक असतात ज्यामुळे प्रतिमांना धुतलेले स्वरूप येते. QGIS 2.0 रेस्टरच्या रेंडरिंग वर्तनावर अधिक बारीक नियंत्रण ठेवते, ज्यात प्रतिमेसाठी रंग जागा निश्चित करताना डिफॉल्टद्वारे 2% - 98% टक्के संचयी कपात वापरणे समाविष्ट आहे. डिफॉल्ट सेटिंग्जसह समान प्रतिमा सादर करताना येथे प्रतिमा QGIS 1.8 (डावीकडे) विरुद्ध QGIS 2.0 (उजवीकडे) दर्शविते.

![image11](images/Selection_023.png)
### वैशिष्ट्य:  WMS फॉर्मेट ओळखते
सर्व्हरद्वारे एकापेक्षा जास्त माहित असलेली स्वरूपे समर्थित असल्यास WMS स्तरांसाठी आयडेंटी टूल परिणामाचे स्वरुप निवडणे शक्य आहे . समर्थित स्वरूप HTML, वैशिष्ट्य (GML) आणि साधा मजकूर आहेत. जर वैशिष्ट्य  (GML)  स्वरूप निवडले गेले तर परिणाम वेक्टर थरांप्रमाणेच स्वरूपात आहे, भूमिती अधोरेखित केली जाऊ शकते आणि वैशिष्ट्ये आणि भूमितीसह वैशिष्ट्य क्लिपबोर्डवर कॉपी केले जाऊ शकते आणि दुसर्या थरावर पेस्ट केले जाऊ शकते .

![image12](images/wms-identify.png)
### वैशिष्ट्य: WMTS समर्थन
QGIS मधील WMS क्लायंट आता  WMTS  (वेब मॅपिंग टायल सर्व्हिस) चे समर्थन करतो ज्यात टाइम स्लाइससारख्या उप-डेटासेटच्या निवडीचा समावेश आहे. दुसऱ्या सर्व्हरमधून WMTS  लेअर जोडताना, आपल्याला प्रदर्शित करण्यासाठी टाइम स्लाइस निवडण्यास सांगितले जाईल.

![image13](images/Selection_035.png)
## सामान्य
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## लेबलिंग
### वैशिष्ट्य: नवीन लेबलिंग सिस्टम
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### वैशिष्ट्य: अभिव्यक्तीवर आधारित लेबल गुणधर्म
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

बंधनकारक गुणधर्मांच्या उदाहरणांमध्ये हे समाविष्ट आहेः
- फॉन्ट
- आकार आकार
- शैली
- बफर आकार

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### वैशिष्ट्यः जुने लेबलिंग इंजिन असमर्थित केले आहे 
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

QGIS 2.0 मधील जुन्या इंजिनसह कार्य करण्यासाठी खालील मार्गदर्शक तत्त्वे लागू आहेत:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- जुन्या उघडलेल्या प्रकल्पांसाठी नापसंत केलेला टॅब सक्रिय राहतो, जर कोणताही स्तर त्यांचा वापर करीत असेल आणि जुन्या लेबलिंग इंजिनला सक्षम नसलेले प्रकल्प नसलेले प्रकल्प जतन केले तरीही ते जात नाही.

पायथन कंसोल कमांडद्वारे सध्याच्या प्रकल्पासाठी लेबलिंग टॅब सक्षम / अक्षम केले जाऊ शकते, उदा.

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
** टीप **: * खूप उच्च शक्यता आहे * QGIS च्या पुढील स्थिर प्रकाशनाच्या आधी नापसंत लेबलिंग इंजिन पूर्णपणे काढून टाकले जाईल. कृपया जुने प्रकल्प स्थलांतरित करा.

![image17](images/changelog-2.0_labels-deprecated.png)
## स्तर दंतकथा
### वैशिष्ट्य: आभासी दृश्य अभिप्राय आणि पर्याय 
- प्रति चिन्हाप्रमाणेच थरातील वैशिष्ट्यांसाठी एकूण गणना
- संपादन मोडमधील वेक्टर थरांमध्ये आता एक लाल पेन्सिल आहे जी वचनबद्ध नसलेले (जतन न केलेले) संपादन दर्शविते
- बहु-स्तरीय निवडींमध्ये किंवा निवड नसताना ते दर्शविण्यासाठी, सक्रिय थर आता अधोरेखित केला आहे 
- नॉन-लिस्ट-आयटम व्हाईटस्पेसमध्ये क्लिक केल्याने आता निवड स्पष्ट होते
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- गट आणि स्तर वैकल्पिकपणे ठळक फॉन्ट शैलीमध्ये असू शकतात.
-  जेथे असे रेंडरिंग धीमे असू शकते अशा प्रकल्पांसाठी, रॅस्टर लेयर जनरेटेड प्रिव्ह्यू आयकॉन आता बंद केले जाऊ शकतात

![image18](images/changelog-2.0_visual-options.png)
### वैशिष्ट्य: विद्यमान नकाशा स्तर डुप्लिकेट करा.
नकाशा स्तरातील आख्यायिकेमध्ये निवडलेले सदिश आणि रास्टर स्तरांची नक्कल करा. समान डेटा स्त्रोत पुन्हा आयात करण्यासाठी समान, स्वतंत्र स्तर तयार करून , त्यानंतर कॉपी/पेस्ट शैली आणि प्रतीकात्मक वैशिष्ट्ये.

![image19](images/changelog-2.0_dup-layer_1.png)
### वैशिष्ट्य: मल्टी-लेयर टॉगल एडिटिंग कमांड
वापरकर्ता आता आख्यायिकेमधील एकाधिक थर निवडू शकतो आणि त्यापैकी काही संपादन मोडमध्ये वेक्टर थर असल्यास, सध्याचे वचनबद्ध संपादन जतन करणे, रोलबॅक करणे किंवा रद्द करणे निवडू शकतो . वापरकर्ता निवडीची पर्वा न करता सर्व थरांमध्ये त्या क्रिया लागू करणे देखील निवडू शकतो.

![image20](images/changelog-2.0_current-edits.png)
## नकाशा संगीतकार
### वैशिष्ट्य:  HTML नकाशा आयटम
आपण आता आपल्या नकाशावर html घटक ठेवू शकता.

![image21](images/Composer_1_006.png)
### वैशिष्ट्य: मल्टीपेज समर्थन
एकाच संगीतकार विंडोमध्ये आता एक नंतर अधिक पृष्ठ असू शकते.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
###  वैशिष्ट्य: रचनाकार लेबलमधील अभिव्यक्ती
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

अभिव्यक्ती असलेले लेबल जसे की:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
तयार करण्यासाठी मुद्रण वेळेत (आणि प्रदर्शन वेळ) मूल्यमापन केले जाईल:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### वैशिष्ट्य: ऑटो स्नॅप लाइन्स
छान छापील नकाशे तयार करण्यासाठी नकाशा आयटम छान ठेवणे कठीण आहे.ऑब्जेक्टच्या जवळ असलेल्या वस्तू ड्रॅग करून सहज रचनाकार ऑब्जेक्ट अलाइनमेंट करता यावी यासाठी ऑटो स्नॅपिंग लाईन्स जोडण्यात आल्या आहेत.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### वैशिष्ट्यः मॅन्युअल स्नॅप लाईन्स
कधीकधी आपल्याला संगीतकारावर पडद्याचे अंतर असलेल्या वस्तूंना संरेखित करण्याची आवश्यकता असते. नवीन मॅन्युअल स्नॅपिंग लाइन्ससह आपण मॅन्युअल स्नॅप रेषा जोडण्यास सक्षम आहात जे सामान्य संरेखन वापरुन ऑब्जेक्ट्स अधिक चांगल्या प्रकारे संरेखित करण्यास अनुमती देतात. नवीन मार्गदर्शक रेषा जोडण्यासाठी फक्त वरच्या किंवा बाजूच्या रुलर कडून खेचून घ्या.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### वैशिष्ट्य: नकाशा मालिका निर्मिती
नकाशा मालिका निर्मितीसाठी कधीही आवश्यक आहे? अर्थात आपल्याकडे आहे. संगीतकारात आता अ‍ॅटलास वैशिष्ट्य वापरून नकाशा मालिकेच्या निर्मितीमध्ये अंतर्भूत आहे. कव्हरेज लेयर्स पॉईंट्स, ओळी, बहुभुज असू शकतात आणि सध्याचे वैशिष्ट्य विशेषता डेटा लेबलमध्ये उपलब्ध आहे.  कव्हरेज थर बिंदू, रेषा, बहुभुज असू शकतात आणि सध्याची वैशिष्ट्य वैशिष्ट्य डेटा फ्लाय व्हॅल्यू रिप्लेसमेंटसाठी लेबलमध्ये उपलब्ध आहे.

![image26](images/Picture1.png)
### वैशिष्ट्य: नकाशा फ्रेममध्ये स्वयंचलित विहंगावलोकन समर्थन.
छोट्या विहंगावलोकन विंडोमध्ये मुख्य नकाशाच्या फ्रेमचे सध्याचे क्षेत्र दर्शविणे आवश्यक आहे . आता आपण हे करू शकता. नकाशा फ्रेममध्ये आता इतरांची व्याप्ती दर्शविण्याची क्षमता आहे आणि हलविल्यावर अद्ययावत होईल. अ‍ॅटलास जनरेशन वैशिष्ट्यासह याचा वापर करून आता रचने मध्ये कोर केल्याने काही स्लीक मॅप जनरेशन होऊ शकते.विहंगावलोकन फ्रेम शैली सामान्य नकाशा बहुभुज ऑब्जेक्टसारखीच स्टायलिंग वापरते जेणेकरून आपली सर्जनशीलता कधीही प्रतिबंधित होणार नाही.

![image27](images/Picture1_1.png)
### वैशिष्ट्य: थर मिश्रण
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### वैशिष्ट्य: HTML लेबल समर्थन
HTMLसमर्थन आपल्याला आपल्या अंतिम नकाशांवर अधिक नियंत्रण देण्यासाठी नकाशा रचनाकार लेबल आयटम जोडले गेले आहे. HTML लेबले पूर्ण css स्टाईल शीट, html आणि अगदी जावास्क्रिप्टला समर्थन करतात जर आपण त्या मार्गावर असाल तर.

![image29](images/html.png)
### वैशिष्ट्य: मल्टीकॉलॉम रचनाकार आख्यायिका
रचनाकार आख्यायिका आता एकाधिक स्तंभांना समर्थन देते. अनेक वर्ग असलेल्या एकाच थराचे अनेक स्तंभांमध्ये विभाजन करणे ऐच्छिक आहे.सिंगल प्रतीक स्तर आता सिंगल लाइन आयटम म्हणून डिफॉल्टने जोडले जातात. थर / गट शीर्षकासाठी तीन भिन्न शैली नियुक्त केल्या जाऊ शकतात: गट, उपसमूह किंवा लपलेले शीर्षक शैली आयटमच्या अनियंत्रित व्हिज्युअल ग्रुपिंगला परवानगी देते. उदाहरणार्थ, एकच चिन्ह थर एकल रेषा आयटम म्हणून किंवा थर शीर्षकासह दर्शविला जाऊ शकतो (जसे की 1.8 प्रमाणे), खालील अनेक थरांमधील चिन्हे एकाच गटात वर्गीकृत केली जाऊ शकतात (शीर्षक लपविणे) इत्यादी. लेबलमध्ये वैशिष्ट्य गणना जोडली जाऊ शकते.

![image30](images/multicolumn-legend.png)
### वैशिष्ट्य: रचनाकार व्यवस्थापनाचे नकाशे अद्ययावत करा
रचनाकार व्यवस्थापनाचे नकाशे तयार करण्यासाठी पुढील सुधारणा केल्या आहेत:
- रचनाकाराच्या नावाची आता निर्मितीवर व्याख्या केली जाऊ शकते, वैकल्पिकरित्या इतर रचनाकाराच्या नावांपासून प्रारंभ करणे
- रचनेची आता नक्कल केली जाऊ शकते 
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- मूळ प्रकल्प आता रचनाकाराच्या कार्यस्थानावरुन थेट जतन केला जाऊ शकतो
- सर्व रचनाकार व्यवस्थापन कृती आता थेट रचनाकार कार्यक्षेत्रातून उपलब्ध आहेत

![image31](images/changelog-2.0_composer-mngmnt.png)
## प्लगइन्स
### वैशिष्ट्य: सुधारित प्लगइन व्यवस्थापक
QGIS 1.x मध्ये प्लगइन्स व्यवस्थापित करणे दोन इंटरफेससह काहीसे गोंधळात टाकणारे होते - एक आधीच स्थापित प्लगइन व्यवस्थापित करण्यासाठी आणि एक एकमेव प्लगइन रिपॉझिटरीमधून पायथन प्लगइन आणण्यासाठी. QGIS 2.0 मध्ये आम्ही **एक नवीन, एकीकृत, प्लगइन व्यवस्थापक ** सादर करतो जो आपल्याला प्लगइन डाउनलोड करण्यासाठी, सक्षम करण्यासाठी / अक्षम करण्यासाठी आणि सामान्यत: व्यवस्थापित करण्यासाठी *वन स्टॉप शॉप* प्रदान करतो. आहे, आणि वापरकर्ता इंटरफेस साइड टॅबसह देखील भव्य आहे आणि चिन्हे ओळखण्यास सोपे आहे!

![image32](images/Plugin_Manager_024.png)
## कार्यक्रमक्षमता
### वैशिष्ट्य: नवीन पायथन कन्सोल
नवीन पायथन कन्सोलने आपल्याला आणखी अधिक सामर्थ्य दिले आहे. आता ऑटो कंप्लीट सपोर्ट, सिंटेक्स हायलाइटिंग, अडजस्टेबल फॉन्ट सेटिंग्ज. साइड कोड एडिटर QGIS सत्रात कोणतीही पायथन फाइल उघडण्याची आणि चालविण्याची क्षमता असलेल्या कोडच्या मोठ्या ब्लॉक्समध्ये सुलभ प्रवेश करण्यास परवानगी देतो.

![image33](images/pyconsole.png)
### वैशिष्ट्य: आणखी अभिव्यक्ती कार्ये
अभिव्यक्ती आधारित लेबले आणि चिन्ह यासारख्या गोष्टींना परवानगी देण्यासाठी QGIS च्या बाहेर एक्सप्रेशन इंजिन अधिकाधिक वापरले जात असल्याने, एक्सप्रेशन बिल्डरमध्ये आणखी बरीच फंक्शन्स जोडली गेली आहेत आणि एक्सप्रेशन बिल्डर म्हणून सर्व सुलभ आहेत. सर्व कार्यांमध्ये वापराच्या सुलभतेसाठी व्यापक मदत आणि वापर मार्गदर्शकांचा समावेश आहे.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### वैशिष्ट्य: सानुकूल अभिव्यक्ती कार्ये
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### वैशिष्ट्य: नवीन क्लीनर पायथन API
पायथन API अधिक क्लीनर, अधिक पायथॉनिक, प्रोग्रामिंग अनुभवास अनुमती देण्यासाठी सुधारित केले गेले आहे. QGIS 2.0 API, SIP V2 वापरते जे मूल्यांसह काम करताना आवश्यक असलेले अस्ताव्यस्त टूस्ट्रिंग (), टोआयएनटी () लॉजिक काढून टाकते. प्रकार आता मूळ पायथन प्रकारांमध्ये रूपांतरित केले जातात ज्यामुळे अधिक चांगले API तयार होते. अटरीब्युट्स प्रवेश आता साध्या की लुकअपचा वापर करून वैशिष्ट्यावरच केला जातो, यापुढे इंडेक्स लुकअप आणि वैशिष्ट्य नकाशे वापरले जात नाहीत.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
लेयरमधून वैशिष्ट्ये वाचण्याची पद्धत देखील सुधारली गेली आहे ज्यामुळे भविष्यातील आवृत्त्यांमध्ये मल्टीथ्रेडिंगची परवानगी मिळते.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### वैशिष्ट्य: आवृत्ती 1.एक्स रिलीजसह कोड सुसंगतता
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### वैशिष्ट्य: पायथन प्रोजेक्ट मॅक्रोस
पायथन मॉड्यूल, प्रोजेक्ट.कॅग्ज फाईलमध्ये सेव्ह केला, लोड केला जाऊ शकतो आणि पुढील प्रोजेक्ट इव्हेंटवर विशिष्ट कार्ये चालविली जाऊ शकतात:
- `openProject()`
- `saveProject()`
- `closeProject()`

मॅक्रो चालू आहेत की नाही हे अनुप्रयोग पर्यायांमध्ये कॉन्फिगर केले जाऊ शकते.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## प्रतीकशास्त्र
### वैशिष्ट्य: डेटा परिभाषित गुणधर्म
नवीन डेटा परिभाषित गुणधर्मांसह, वैशिष्ट्य विशेषतांद्वारे प्रतीक प्रकार, आकार, रंग, फिरविणे आणि बर्‍याच इतर गुणधर्मांवर नियंत्रण ठेवणे शक्य आहे.

![image39](images/datadefinedproperties2.png)
### वैशिष्ट्य: सुधारित प्रतीक स्तर व्यवस्थापन
नवीन प्रतीक थर विहंगावलोकन मध्ये एक स्पष्ट, वृक्ष-संरचित लेआउट वापरला गेला आहे जो सर्व प्रतीक स्तरांवर सहज आणि जलद प्रवेशास अनुमती देतो.

![image40](images/symbollayertree.png)
### वैशिष्ट्य: रंग परिभाषांमध्ये पारदर्शकतेसाठी समर्थन
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### वैशिष्ट्य: रास्टर लेयर्ससाठी रंग नियंत्रण
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### वैशिष्ट्य: स्तर दरम्यान कॉपी प्रतीकशास्त्र
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### वैशिष्ट्य: आपल्या डेटाबेसमध्ये शैली जतन करा
आपण डेटाबेस वेक्टर डेटा स्टोअर वापरत असल्यास आपण आता थेट शैली डेटाबेसमध्ये स्तर शैली परिभाषित करू शकता यामुळे एंटरप्राइझ किंवा मल्टी-यूजर वातावरणात शैलीकृत स्तर सामायिक करणे सोपे करते.

![image44](images/Selection_037.png)
### वैशिष्ट्य: रंग रॅम्प समर्थन
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### वैशिष्ट्यः सर्व स्तर प्रकारच्या सानुकूल डीफॉल्ट शैली सेट करा
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## वापरकर्ता इंटरफेस
### वैशिष्ट्य: नवीन चिन्ह थीम
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### वैशिष्ट्य: साइड टॅब, कोलेक्शन करण्यायोग्य गट
विविध पर्यायांना नॅव्हिगेट करणे अधिक सुलभ करण्यासाठी आणि स्क्रीन रीअल इस्टेटचा अधिक चांगला वापर करण्यासाठी आम्ही आमच्या बर्‍याच संवादांमध्ये टॅबचे लेआउट प्रमाणित केले आहे आणि कोलेप्सिबल ग्रुप बॉक्स समाविष्ट केले आहेत.

![image48](images/Selection_005.png)
### वैशिष्ट्य: मऊ सूचना
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### वैशिष्ट्य: अनुप्रयोग सानुकूल फॉन्ट आणि Qt शैली पत्रक
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

सद्य प्लॅटफॉर्मसाठी व्युत्पन्न केलेली QGIS GUI styप्लिकेशन स्टाईलशीट (पायक्यूजीआयएसमध्ये) सह सुरू केल्यावर प्रवेश करणे शक्य आहे:

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### वैशिष्ट्य: थेट रंग निवडक संवाद आणि बटणे
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### वैशिष्ट्यः एसव्हीजी भाष्ये
क्यूजीआयएस 2.0 सह आता आपण आपल्या नकाशावर एसव्हीजी भाष्ये जोडू शकता - विशिष्ट ठिकाणी पिन केलेले किंवा नकाशा कॅनव्हासच्या तुलनेत संबंधित ठिकाणी.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### वैशिष्ट्य: फॉर्म बिल्डर ड्रॅग आणि ड्रॉप करा
डेटा एंट्री फॉर्म तयार करण्यासाठी क्यूजीआयएस 2.0 एक उत्तम नवीन प्रणालीचे समर्थन करते. ड्रॅग dropन्ड ड्रॉप फॉर्म डिझायनरच्या सहाय्याने आपण एकत्रित शेतात एकत्रितपणे टॅबसह स्मार्ट लुकिंग फॉर्म तयार करू शकता.आता आपल्या वापरकर्त्यांसाठी डेटा एंट्री अनुभवावर नियंत्रण ठेवणे खूप सोपे आहे.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### वैशिष्ट्य: डीफॉल्ट क्रिया साधन
If you are a user of vector layer actions (small tasks that can run when you click on a feature), you will love the new action tool on the toolbar. With it you can select an active action and then click on your features to invoke that action.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
