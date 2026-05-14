---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS आणि स्थानिक सरकारी बुशफायर हॅझार्ड मॅपिंग मध्ये GRASS
type: case-study

---
{{<content-start >}}
# QGIS आणि स्थानिक सरकारी बुशफायर हॅझार्ड मॅपिंग मध्ये GRASS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## परिचय
द साउथर्न डाउन्स रीजनल कौन्सिल (एसडीआरसी) दक्षिण-पूर्व क्वीन्सलॅंड, ऑस्ट्रेलियात लहान-ते-मध्यम आकाराची स्थानिक सरकार आहे. कौन्सिल प्रदेश, प्रमुख्याने दक्षिणेकडील भाग, मुख्य बुश फायर ग्रस्त हा दक्षिणेकडच्या क्षेत्रातील रहिवाशांना आणि जमीनदारांसाठी एक वास्तविक आणि वर्तमान चिंता आहे, आणि यामुळे जीवनाचे व मालमत्तेचे नुकसान झाले आहे.

हा प्रकल्प परिषद आणि क्षेत्रातील लोकांना धोका जाणून घेण्यास आणि भविष्यात चांगले निर्णय घेण्यास अनुमती देईल.

![](../images/australia_queens1.jpg)
## प्रकल्प
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

प्रकल्प प्रकल्पाची जीआयएस बाजू 6 मुख्य पायऱ्यांमध्ये मोडली गेली आहे. 
- उतार मूल्यांकन आणि मॅपिंग
- आकलन मूल्यांकन आणि मॅपिंग
- वनस्पती मूल्यांकन आणि मॅपिंग
- बुशफायरच्या धोक्याची तीव्रता ओळखण्यासाठी स्कोअर एकत्रित करणे
- फिल्ड पडताळणी आणि गुणात्मक मूल्यांकन
- अंतिम नकाशे

## QGIS आणि GRASS चा वापर
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

QGIS GRASS प्लगइनचा वापर संपूर्ण क्षेत्राच्या 5 मीटरच्या आतील आकाराच्या GRASS मध्ये आयात करण्यासाठी केला गेला होता ज्याला नंतर r.surf.contour वापरून एक समोच्च रास्टर मॅपमध्ये रूपांतरित केले गेले होते. रास्टर समोच्च नकाशावरून r.slope.aspect वापरून उतार आणि आकृती नकाशा तयार केले गेले. श्रेणींना विभिन्न उतार आणि वर्तुळाच्या श्रेणींमध्ये नियुक्त केले गेले आणि धोका जोखिम घसा दिला. वनस्पती विभागांना देखील वेगळ्या जोखीम स्कोअर देण्यात आल्या. सर्व परिणामी रास्टर नकाशे नंतर mapcalc वापरून एकत्र केले गेले आणि अंतिम धोका धोक्याचे स्कोअर दिले. त्यानंतर जोखीम गुण तीन मुख्य विभागांमध्ये विभागले जातात: उच्च; मध्यम आणि कमी.

ग्रामीण अग्निशमन सेवेद्वारे या प्रक्रीयेचा अंतीम भाग फिल्ड पडताळणी होते. पुनरावलोकन प्रक्रियेनंतर, QGIS अंतिम नकाशे मुद्रित करण्यासाठी वापरले गेले होते.

सर्व GRASS आदेश पंक्तीवरून चालवल्या जाऊ शकतात, तर सर्व आज्ञा ज्या बुश फायर हँझार्ड नकाशे निर्माण करण्यासाठी आवश्यक होते ते दस्तऐवजीकरणाच्या उद्देशाने रेकॉर्ड केले गेले होते आणि नकाशे भविष्यात काही काळ पुन्हा निर्माण करण्यासाठी आवश्यक केले गेले होते.
## निष्कर्ष
एकूणच QGIS, एकत्र GRASS प्लगइनसह, एक उत्तम अनुभव प्रदान केला आणि कौन्सिलने त्यांच्या स्वतःच्या बुशफायर इशारा मॅपिंगसाठी एक उत्तम अंतिम परिणाम दिला. GRASS प्लगइन QGIS द्वारे GRASS वर इंटरफेस वापरण्यास अतिशय सोपे आहे. QGIS नैसर्गिकपणे GRASS रास्टर स्वरुपन उघडण्यासाठी सक्षम आहे म्हणून, एकीकरण अत्यंत सहजतेने होते आणि नकाशे सहजपणे केले जाऊ शकतात.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## संदर्भ
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## लेखक
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

हा लेख जानेवारी 2011 मध्ये नेथन वुड्रोने योगदान दिला होता. नेथन दक्षिण डाउन्स प्रादेशिक परिषदेचे जीआयएस अधिकारी आहेत आणि Southern Queensland विद्यापीठ स्थानिक विज्ञान पदवी अभ्यास करीत आहेत.

{{<content-end >}}
