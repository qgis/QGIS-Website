---
draft: 'true'

---
# प्रायोगिक आणि उपयोजित भूगोलवरील प्रयोगशाळेत प्रमुख जीआयएस सॉफ्टवेअर म्हणून क्यूजीआयएस
## परिचय
प्रयोगशाळा आणि प्रयोगित भूगोल (एलएजीएजी) वर प्रयोगशाळा म्हणजे कॉलेज ऑफ हॉटेल अँड बिझिनेस मॅनेजमेन्ट, लि. चा भाग आहे ब्र्नो, झेक प्रजासत्ताकमधील (Vysokákla obchodní a hotelová, s.r.o.) जे पर्यटन, व्यवसाय आणि हॉटेल व्यवस्थापन येथे उच्च शिक्षण देते. एलएजीजी सामाजिक-आर्थिक स्थानिक प्रक्रिया मॉडेलिंग, स्थानिक नमुने विश्लेषित करणे, परिसर आणि प्रदेशांच्या वास्तविकतेचे वर्णन आणि देखरेखीवर लक्ष केंद्रित करते.

![QGIS while modeling 3D objects (interpolation), terrain analysis](./images/czech_brno1.jpg){.align-right}

LEAG plays important role in academic research held in College of Business and Hotel Management. The need of spatial modeling requires also excellent software. The philosophy of minimum cost and maximum efficiency led to choice of open source solutions. This step resulted in using core open source SW such as LibreOffice, GIMP, Inkscape and QGIS. QGIS does not stand alone --\-- we use MapWindow, OpenJump, gvSIG, SAGA and others. But QGIS plays the major role.
## QGIS चा वापर
QGIS is the leading software and stands in current versions (because of the "experimental" character of LEAG we are using the latest unstable releases instead of LTS versions) for several reasons:
- ग्राफिकल यूजर इंटरफेस (व्यावसायिक उत्पादनांच्या जवळ)
- द्रुत विकास आणि वापरकर्ता-इच्छित वैशिष्ट्ये समाकलित करणे
- स्थिरता आणि इंटरऑपरेबिलिटी (आम्ही विंडोज आणि उबंटू लिनक्स प्लॅटफॉर्म वापरत आहोत)
- इतर (डॉ. हॉर्स्ट डस्टर यांनी लिहिलेल्या प्रकरण अभ्यासामध्ये नमूद केलेले)

स्थानिक विश्लेषण मुख्यत: मूलभूत जिओप्रोसेसींग कार्ये आणि पायथन-आधारित प्लगइन वापरुन केले जातात. अलीकडील प्रकल्प जिथे क्यूजीआयएस वापरले गेले:
- स्थानिक स्थान आणि रहिवाश्यांमध्ये मॉडेलिंगचे नमुने
- भूप्रदेश व्हिज्युअलायझेशनसाठी 3 डी मॉडेल तयार करणे (आणि पुढील टेकडी शेडिंग म्हणून वापरा)
- लघु आणि मध्यम उद्योगांचे डेटाबेस संचयित करणे, तयार करणे आणि संपादन करणे (+ पुढील व्हिज्युअलायझेशन)
- Homogenizing of free-to-use geodata and creation of "geo-data-bank" for students and researchers at College of Business and Hotel Management

क्यूजीआयएसचा उपयोग अन्य मुक्त स्त्रोत उत्पादनांच्या सहकार्याने केला जातो. उदाहरणार्थ अंतिम लेआउट बहुधा इंकस्केप किंवा जीआयएमपी (लिबर ऑफिस ड्रॉ मध्ये कमी) वापरून तयार करणे आहे. वेब-आधारित नकाशे इनकस्केप (एसव्हीजी निर्यातानंतर) वापरून संपादित करीत आहेत आणि रास्टर नकाशे जीआयएमपी वापरुन पूर्व-संपादित केले जातात.

QGIS is also great educational tool. College of Business and Hotel Management offers students subjects like "Geographical Information Systems I. and II." or "Selected chapters from geoinformatic literacy" where QGIS is used as main platform for teaching students how to use GIS and how to produce high-quality maps. Recently, the QGIS was used as main product during GIS Day held at our school on November 2010.

![Using diagrams comparing population between two censuses](./images/czech_brno2.jpg){.align-right}
## निष्कर्ष
With no cost and high efficiency the Laboratory on Experimental and Applied Geography produces high-quality analysis, maps and visualizations. Using QGIS large databases are being created and further testing of new functions are being done. Finally, one of the highest impact of using QGIS could be seen in education \-\-- QGIS is the first software, which is presented to students. During regular workshops students learn how to legally work with QGIS and how to create their own maps.
## लेखक
![Jakub Trojan](./images/czech_brnoaut.jpg){.align-left height="200px"}

या लेखाचे योगदान नोव्हेंबर २०१० मध्ये जॅकब ट्रोजन यांनी दिले होते. तो कॉलेज ऑफ बिझिनेस अँड हॉटेल मॅनेजमेंट, लि. (ब्र्नो, सीझेड) येथे शैक्षणिक संशोधक आहे जिथे त्याने प्रायोगिक आणि उपयोजित भूगोल विषयावरील प्रयोगशाळेची स्थापना केली आणि नेतृत्व केले. ते इन्स्टिट्यूट ऑफ जिओग्राफी, विज्ञान संकाय, मासारिक विद्यापीठ (ब्र्नो, सीझेड) मधील डॉक्टरेट विद्यार्थी देखील आहेत.
