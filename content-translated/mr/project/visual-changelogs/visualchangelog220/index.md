---
HasBanner: false
draft: false
releaseDate: '2014-02-22'
section: project
sidebar: true
title: क्यूजीआयएस 2.2 साठी चेंजलॉग
type: visual-changelog

---
{{<content-start >}}
# क्यूजीआयएस 2.2 साठी चेंजलॉग{#changelog22 }
Release date: 2014-02-22

क्यूजीआयएस 2.2.0 च्या पुढील रीलिझसाठी लॉग बदला. या प्रकाशनावर पॉलिश आणि कार्यक्षमतेवर जोर देण्यात आला आहे - आम्ही वापरकर्त्याची इंटरफेस अधिक सुसंगत आणि व्यावसायिक बनविण्यासाठी (आणि वापरण्यास सुलभतेने सुलभ) करण्यासाठी अनेक नवीन वैशिष्ट्ये, ट्वीक्स आणि संवर्धने जोडली आहेत. संगीतकाराने (प्रिंट रेडी नकाशे तयार करण्यासाठी वापरलेला) उत्तम कार्टोग्राफिक आउटपुट तयार करण्यासाठी अधिक व्यवहार्य व्यासपीठ बनविण्यासाठी त्याच्याकडे बरेच काम केले आहे.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

आम्ही विकसक, दस्तऐवजकार, परीक्षक आणि तेथील सर्व लोकांना त्यांचे आभार मानू इच्छितो जे आपला वेळ आणि मेहनत स्वयंसेवक करतात (किंवा लोकांना यासाठी पैसे देतात).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

शेवटी आम्ही आमच्या अधिकृत प्रायोजकांना या प्रकल्पात त्यांना देत असलेल्या अमूल्य आर्थिक मदतीबद्दल आभारी आहोत:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## अनुप्रयोग आणि प्रकल्प पर्याय
### वैशिष्ट्य: नॉटिकल मैल्समध्ये मोजण्यासाठी समर्थन
For you seafaring folks out there, you can now measure distances using nautical miles. To enable this, use the `Settings -> Options -> Map Tools` option panel.

![image1](images/entries/e1115ca7d43ec24fceaee93f976848583148724f.webp)
## डेटा प्रदात्या
### वैशिष्ट्य: अनेक संबंध एक समर्थन
This release sports the ability to define 1:n relations. The relations are defined in the project properties dialog. Once relations exist for a layer, a new user interface element in the form view (e.g. when identifying a feature and opening its form) will list the related entities. This provides a powerful way to express e.g. the inspection history on a length of pipeline or road segment. You can find out more about relations support [here](http://blog.vitu.ch/10112013-1201/qgis-relations).

![image2](images/entries/0e5e0d1b9dfafe9d64dd5b79866877980f03d099.webp)
### वैशिष्ट्यः डीएक्सएफ निर्यात साधन
A new tool for exporting DXF\'s has been added to the `Project` menu

![image3](images/entries/452e7692b5b8d2704b4d31067265eb71986d969f.webp)
### वैशिष्ट्य: नवीन वेक्टर लेयर म्हणून पेस्ट करा
It is a common activity in a GIS to create a sub-selection and then to create a new layer from the selection. In QGIS you can already do `save selection as` to save a layer from your selection, and now offers functionality that allows you to create a new file or memory layer from whatever is in your clipboard. Simply select some features, copy them to your clipboard and then do `Edit -> Paste features as` and choose either `New vector layer` or `New memory layer` from the submenu. The best part of this new feature is that if you have some Well Known Text (WKT) features in your clipboard from another app, you can simply paste them into QGIS as a new layer now.

![image4](images/entries/636db14446809f9e284013113a7b881868591ed3.webp)
### वैशिष्ट्य: सारणी आणि संगीतकारातील डब्ल्यूएमएस लीजेंड ग्राफिक
Prior to QGIS 2.2 the WMS data provider was not able to display a legend in the table of contents\' layer list. Similarly no legend could be displayed in the map composer. QGIS 2.2 addresses both of these issues.

Clicking on the layer\'s legend will open a frame with the legend at full resolution. The legend will display contextual information based on your current scale. The WMS legend will be shown only if the WMS server has GetLegendGraphic capability. Legend resolution can be modified changing Canvas & Legend options.

![image5](images/entries/6e7cd4849824a802558c0e029f605145d5c885aa.webp)
## डिजिटलायझेशन
### वैशिष्ट्य: रिंग डिजिटलायझिंग टूल भरा
This new tool is used to cut holes in polygons and automatically fill them with new features. If you hold down `Ctrl` when finalising the feature, the attributes will be taken from parent feature.

![image6](images/entries/a8c671765578b660cb5d33cca51efa66ecdb17a4.webp)
## सामान्य
### वैशिष्ट्य: अलीकडील अभिव्यक्ती जतन केली
अभिव्यक्ति बिल्डर आता अंतिम 20 वापरलेले अभिव्यक्ती लक्षात ठेवेल.

![image7](images/entries/90a6b4d181fb2dc7699402d17c1f31522c4f3409.webp)
### वैशिष्ट्यः क्लिपबोर्डवरून डब्ल्यूकेटी पेस्ट करा
QGIS can now paste and create a new feature based on WKT that is found in the clipboard. Simply copy some WKT and paste into a editable layer. You can also create a new layer by selecting `Edit -> Paste As -> New Memory Layer`
## नकाशा संगीतकार
### वैशिष्ट्य: झेब्रा नकाशा सीमा सुधारणा
You can now set the colours of the `Zebra` border on the map element in the map composer.

![image8](images/entries/682c36e3ac96b491e2e0a99a7ff9d94b9e0dc4e5.webp)
### वैशिष्ट्य: घटक रोटेशन समर्थन
संगीतकारातील प्रत्येक प्रकारचे घटक आता फिरविले जाऊ शकतात, स्केल बार, सारण्या आणि प्रख्यात. उदाहरणार्थ आपण रचनावरील लेबल फिरवू शकता जेणेकरून ते आपल्या पृष्ठ लेआउटमध्ये अधिक चांगले बसू शकेल (सचित्र म्हणून). फिरवलेल्या घटकांचे आकार बदलणे देखील सुधारित केले आहे.

![image9](images/entries/700e0999552bc2e2bb2cef86ed14240b05f1da4e.webp)
### वैशिष्ट्य: संगीतकार प्रमाणात जोडले आणि शासक सुधारणा
The appearance of rulers has been improved by adjusting the scale logic and by adding smaller ruler divisions, and by making vertical rulers use rotated text. There is also a new composer action for hiding/showing rulers. You can now quickly zoom to 100% page scale using the new `Zoom to 100%` tool on the toolbar. The composer window now lets you quickly switch the page scaling via a new scale combobox in the status bar. In addition a new indicator has been added to show you the precise pixel position of your cursor. The `Close` and `Help` buttons have been removed from the bottom of the composer window to give you the maximum amount of screen space for working with your compositions.

![image10](images/entries/8b148acf4ef24204b42f14ee7cec43d57c87911a.webp)
### वैशिष्ट्य: जागतिक फाइल निर्मिती
In the composer you can now create georefenced maps! Simply ensure that you choose the correct map element in the `Composition tab` and then export your map as a PNG file. An accompanying world file will be written, allowing you to load your exported composition in QGIS as a raster layer.

![image11](images/entries/d5887511afbe8379f9e240c3763f6b68766cac88.webp)
### वैशिष्ट्य: एकाधिक आयटमसह कार्य करणे
Support has been added for moving and resizing multiple items simultaneously. You can now hold shift while resizing to maintain an item\'s ratio while resizing, or hold control to resize from the item\'s centre. Shortcut key also apply to moving items, so holding shift while moving an item constrains the movement to horizontal or vertical movement, and holding control temporarily disables item snapping. You can also hold shift while pressing a cursor key to shift all selected items by a larger amount.
### वैशिष्ट्य: lasटलस वर्धितता
You can now preview the individual pages of the map atlas that will be generated in composer. While in atlas preview mode you can output the current page without outputting the entire atlas. You can also tweak the map extent or scale for each feature while previewing the atlas page. Atlas map settings have been moved from the atlas panel to the map properties panel, so now more than one map can be controlled by the atlas generation. There\'s a new option to automatically centre an overview map, which comes in handy when creating atlas based maps. More context information is now available so that you can adjust your symbology based on whether the feature is the current atlas feature or not. See [this article for more info](http://nathanw.net/2013/12/02/waiting-for-qgis-22-highlighting-current-atlas-feature/).

![image12](images/entries/fe668e5f257efec81db855a91fc7d6febc221261.webp)
### वैशिष्ट्य: सुधारित आयटम निवड
You can now select more then one item by clicking and dragging a box to select them, and there\'s shortcuts for adding to a selection (holding shift while dragging), subtracting from a selection (hold control while dragging) and switching to \"within\" selection mode (hold alt while dragging). Shift clicking an already selected item will remove it from the selection. There\'s also shortcuts and menu items for selecting all items, clearing a selection, and inverting a selection. It\'s also possible now to select items which are hidden below other items by control-clicking an item, or by using \"Select next item above/below\" in the new composer Edit menu.
### वैशिष्ट्य: रचनांचे चांगले नेव्हिगेशन
QGIS 2.2 includes many improvements to help you navigate your compositions. You can now zoom in or out from a composition by using the mouse scroll wheel. A dedicated pan tool has been added which allows you to drag the composition around, and you can also switch immediately to pan mode by holding the space bar or the by holding the mouse scroll wheel. There\'s also a new zoom tool which allows you to precisely zoom to a specific area of your composition. You can also switch to zoom mode at any time by pressing and holding control-space and drawing a zoom region on the composition.
### वैशिष्ट्य: पृष्ठे आणि आकारांची सुधारित शैली
You can now control the style of the composition background using the full range of QGIS\' symbology options. It\'s now possible to export compositions with a transparent (or semi-transparent) background. Shape items (rectangles, triangles and ellipses) can also be styled using the same options as polygon map layers. You can even style the page background or shapes by using data defined settings based on the current atlas feature! There\'s also a new option for rounding the corners of rectangle shapes.
## QGIS सर्व्हर
### वैशिष्ट्यः डब्ल्यूसीएस समर्थन क्यूजीआयएस सर्व्हरमध्ये जोडला
क्यूजीआयएस-सर्व्हर आधीपासूनच मानकांचे समर्थन करते: वेब मॅप सर्व्हिस (WMS version 1.3.0 and 1.1.1) आणि वेब फीचर सर्व्हिस (WFS version 1.0.0) आणि ट्रान्झॅक्शनसह वेब फीचर सर्व्हिस (WFS-T). क्यूजीआयएसच्या या नवीन रीलीझसह, आपण आता वेब कव्हरेज सर्व्हिस (WCS version 1.0.0) मानक वापरून रास्टर थर देऊ शकता.

![image13](images/entries/b93abbe00e7a32ffb06144ac839619ab50521e5c.webp)
## प्रतीकशास्त्र
### वैशिष्ट्य: ग्रेडियंट फिल समर्थन
नवीन ग्रेडियंट फिल फीचर आपल्याला पूर्वीपेक्षा आणखी चांगले कार्टोग्राफी तयार करू देते. आपण आपल्या वैशिष्ट्यांकडे ग्रेडियंट कसे लावावे या वैशिष्ट्यात बरेच लवचिकता प्रदान करणारे असंख्य पर्याय आहेत. यात समाविष्ट:
- दोन रंग किंवा उतारावर आधारीत भरते
- आपल्या ग्रेडियंटसाठी कॅनव्हास किंवा ऑब्जेक्ट आधारित मूळ
- गुणविशेषाच्या सेन्ट्रॉइडपासून उत्पन्न होणारे ग्रेडियंट्स
- शंकूच्या आकाराचे, रेखीय आणि रेडियल ग्रेडियंट प्रकार
- सर्व ग्रेडियंट गुणधर्मांसाठी डेटा परिभाषित पर्याय (अभिव्यक्ती किंवा सारणी स्तंभ वापरण्यासाठी).

Read more about how to use gradient fills [here](http://nyalldawson.net/2014/01/waiting-for-qgis-2-2-gradient-fills/).

![image14](images/entries/7c4cb6c7ce981ca88b27cd2ae55bc4e503a1234f.webp)
### वैशिष्ट्यः पॅलेटेड रास्टरसाठी लेबल समर्थन
जे रास्टर्स निश्चित रंग पॅलेट वापरतात (उदा. लँड कव्हर मॅपसाठी ठराविक असतात) आता श्रेणीची लेबले नियुक्त केली जाऊ शकतात जी नकाशा आख्यायिकेमध्ये आणि संगीतकारांच्या आख्यायिकेमध्ये दर्शविली जातील.

![image15](images/entries/232d60f2aa3accb19eb4da3a08b75ad4c15d068a.webp)
### वैशिष्ट्य: कलर रॅम्प्स उलट करता येतील
कलर रॅम्पवर काम करणारे प्रतीकात्मक संवादांमध्ये एक नवीन पर्याय जोडला गेला आहे जे तो तयार झाल्यावर कलर रॅम्पला उलट करू देईल.

![image16](images/entries/3b1e65705f751bb468cc6495267633d613edbe34.webp)
### वैशिष्ट्यः नियम आधारित प्रस्तुतकर्त्यामध्ये कॉपी आणि पेस्ट करा
नियम आधारित प्रस्तुतकर्ता मध्ये, आपण आता नियम वर उजवे क्लिक करू शकता आणि नंतर नवीन नियम म्हणून नियम कॉपी आणि पेस्ट करू शकता.

![image17](images/entries/8e69ef57ed6ae838e813d798312d7d1e39913749.webp)
### वैशिष्ट्य: फ्लाय वैशिष्ट्य सामान्यीकरण वर
क्यूजीआयएस 2.2 मध्ये फ्लाय वैशिष्ट्य सामान्यीकरणासाठी समर्थन समाविष्ट केले आहे. छोट्या भाकरी लहान माडींवरच बरीच गुंतागुंतीची वैशिष्ट्ये रेखाटतात जेव्हा हे प्रतिसादाच्या वेळा सुधारू शकते. हे वैशिष्ट्य स्तर सेटिंग्जमध्ये सक्षम किंवा अक्षम केले जाऊ शकते. एक नवीन जागतिक सेटिंग देखील आहे जी नव्याने जोडलेल्या स्तरांसाठी डीफॉल्टनुसार सामान्यीकरण सक्षम करते. ** टीप: ** वैशिष्ट्य सामान्यीकरण काही प्रकरणांमध्ये आपल्या प्रस्तुत आउटपुटमध्ये कलाकृतींचा परिचय देऊ शकते. यामध्ये ऑफसेट आधारित प्रतीक थर वापरताना बहुभुज आणि चुकीच्या प्रस्तुतीकरणाच्या दरम्यान असलेल्या स्लीव्हर्सचा समावेश असू शकतो.

![image18](images/entries/baa801841f58883d93d0ea6ecb5363da963e4ee2.webp)
### वैशिष्ट्य: मार्कर लेयर्ससाठी अँकर पॉईंट्स सेट केले जाऊ शकतात
When defining symbology with marker layers (e.g. a point layer symbolized with SVG markers) you can now specify what part of the image should correspond to the \'anchor point\'. For example you can indicate that the bottom-left corner of the image should coincide with the position of the feature. You can also use the `data defined properties` to have this property set at render time based on an attribute in the data table for that layer (or an arbitrary expression).

![image19](images/entries/ecac63dad2e0da0702b2fe5bc361d68f0c0c6a0f.webp)
### वैशिष्ट्य: अभिव्यक्त्यांवर आधारित थीमेटिक नकाशे
वर्गीकृत आणि पदवीधर विषयासंबंधी नकाशे आता अभिव्यक्तीच्या परिणामाद्वारे तयार केले जाऊ शकतात. वेक्टर लेयर्ससाठी प्रॉपर्टीज डायलॉगमध्ये एक्सप्रेशन्स बिल्डरबरोबर एट्रिब्यूट बिल्डर निवडला गेला आहे. म्हणून आता आपल्याला वर्गीकरण गुणधर्म एकाधिक फील्डचे एकत्रित किंवा काही क्रमवारीचे सूत्र हवे असेल तर आपल्या विशेषता सारणीमध्ये नवीन स्तंभाचे वर्गीकरण गुण लिहिण्याची आवश्यकता नाही.

![image20](images/entries/cc5cad88da77d1868e394a115606f4b1e6ee8c29.webp)
### वैशिष्ट्य: आकार आणि गुणधर्मांसाठी प्रतीक रेखाचित्रात अभिव्यक्ती समर्थन
You can now use an expression to define the size and attributes when using the diagramming capabilities of QGIS. For more info see the Pull Request here [Pull 1039](https://github.com/qgis/QGIS/pull/1039)

![image21](images/entries/547b5058efeca906c00ee65ee2504f2669ff52f9.webp)
### वैशिष्ट्यः नियम आधारित प्रस्तुतकर्त्यामधील अन्य नियम
नियम आधारित प्रस्तुतकर्ता आता ईएलएसई नियमाचे समर्थन करतो जे त्या पातळीवरील सामन्यावरील अन्य नियमांपैकी काहीही नसाल्यास चालवले जाईल. इतर नियमांप्रमाणेच इतर नियमांचेही पालन केले जाऊ शकते.

एक उदाहरण असू शकते:

| `type = 'water' (style grey)` | `ELSE (style red)`

![image22](images/entries/4c38bdd63e64274d22e6a57a6541920ed47bc4be.webp)
### वैशिष्ट्यः बहुभुजांसाठी अंतर्गत स्ट्रोक समर्थन
बहुभुज स्ट्रोक बहुभुजाच्या आतील भागापुरते मर्यादित राहण्यासाठी समर्थन जोडले गेले आहे (जेणेकरून ते एखाद्या शेजारच्या बहुभुजामध्ये वाहू नये).

More information on this feature can be found on the [second part of this article](http://nyalldawson.net/2014/01/qgis-two-neat-features-in-2-2/).

![image23](images/entries/81597f0bc2b848fe39e078a2684c57d44fbda79d.webp)
## वापरकर्ता इंटरफेस
### वैशिष्ट्य: सुधारित गुणधर्म संवाद
All our properties dialogs have had their main property menus updated so they look slicker with a inverse coloured side bar. This is purely cosmetic but should make it easier to know what your current context is in a dialog.

![image24](images/entries/9d817847f89a3ea7836f86ddff3317040543a78f.webp)
### वैशिष्ट्य: अभिव्यक्ति संवाद सुधारणे
We have made some tweaks to the expression dialog - power users can now hide the operator buttons. There are also now splitters between the function list and function help areas, and between the expression and function list area. See the [original pull request](https://github.com/qgis/QGIS/pull/1073) for details.

![image25](images/entries/150ae30a6d905e008131c28e4befe862f1bf8ed6.webp)
### वैशिष्ट्य: नवीन कीबाइंडिंग्ज
पुनरावृत्ती कार्ये करणे अधिक कार्यक्षम करण्यासाठी आम्ही QGIS मधील कीबोर्ड शॉर्टकट अद्यतनित केले आहेत.
- `ctrl-d` - Remove selected layers in table of contents
- `>` - Select next vertex when using the node tool
- `<` - Select previous vertex when using the node tool
- `Delete` or `Backspace` - delete the selected features (you can undo these actions), or a node when using the nodetool.
- `F5` updates the canvas (instead of ctrl-r)

See also [Issue 9094](http://hub.qgis.org/issues/9094) and [Pull Request 1010](https://github.com/qgis/QGIS/pull/1010) for more details.

![image26](images/entries/e8766bfccf2da60b09acde28f5d766eb3d76cec9.webp)

{{<content-end >}}
