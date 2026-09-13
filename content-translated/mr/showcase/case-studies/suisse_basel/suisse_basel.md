---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## क्यूजीआयएस कसा वापरला गेला
संपूर्ण नियोजन प्रक्रियेमध्ये क्यूजीआयएसचा उपयोग खालील चार कार्यांसाठी केला गेला:
- विद्यमान डेटा आयात. डेटामध्ये बहुभुज, रेखा आणि बिंदू आकाराच्या फायलींसह भौगोलिक-संदर्भित पार्श्वभूमी नकाशे (shape *. Tif) समाविष्ट आहेत. वन व्यवस्थापकासाठी, त्याच्या दैनंदिन कार्यासाठी विद्यमान थीमॅटिक डेटाचे दृश्य (उदाहरणार्थ भूजल- आणि पिण्याचे पाणी स्त्रोत, निसर्ग संरक्षण झोन) महत्वाचे आहेत.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- विश्लेषण. वेगवेगळ्या मापन श्रेणीतील क्षेत्रांची गणना केली गेली होती. रेल्वे रुळ किंवा रस्ते यासारख्या विशिष्ट लाइन वैशिष्ट्यांपासून प्रारंभ करुन, संबंधित संरक्षण जंगले बफरच्या मदतीने निश्चित केल्या गेल्या.
- मुद्रण आणि निर्यात. मुद्रण संगीतकाराने नकाशा लेआउट निर्मितीस समर्थन दिले. नकाशा पीडीएफ आणि प्रतिमा फायली म्हणून निर्यात केला गेला.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## निष्कर्ष
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## परिप्रेक्ष्य
वनीकरण नियोजन संकल्पनेची मुख्य कामे नमूद केलेल्या मूलभूत जीआयएस साधनांसह कार्य करणे शक्य आहे. ग्वारसी वन मालक स्तरावर वनीकरण नियोजनासाठी क्यूजीआयएस वापरणे सुरू ठेवेल. सादर केलेल्या प्रकल्पाच्या अनुभवांच्या आधारे, स्थानिक अधिका of्यांच्या पातळीवर वनीकरण संकल्पनांसाठी क्यूजीआयएसची शिफारस देखील केली जाऊ शकते. तपशीलवार विश्लेषण आवश्यकतांसह मोठे आणि अधिक जटिल प्रकल्प पोस्टजीस स्थानिक डेटाबेस सर्व्हरसह QGIS च्या संयोजनाद्वारे हाताळले जाऊ शकतात. नवीन लॉगिंग झोन तसेच वन आरक्षण व संरक्षण झोन सहजपणे डिजिटल केले जाऊ शकतात. आशा आहे की, वन मालक आणि व्यवस्थापक त्यांच्या वार्षिक नियोजनासाठी तसेच त्यांच्या वन क्रियांच्या दस्तऐवजीकरणासाठी क्यूजीआयएसच्या संभाव्यतेचा अधिकाधिक वापर करतील.
## लेखक
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
