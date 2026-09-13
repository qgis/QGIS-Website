---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_cesena1.png
title: सेसेनाच्या भिंतीचे वर्णन करण्यासाठी QGIS
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

एॅकॅम्पस युनिव्हर्सिटी एक ऑनलाइन विद्यापीठ म्हणून तयार केली गेली होती आणि एमआययूआर (इटालियन शिक्षण मंत्रालय, विद्यापीठ आणि संशोधन मंत्रालय) यांनी 30 जानेवारी 2006 च्या मंत्रीमंडळानुसार मान्यता प्राप्त केली होती. तरुणांना त्यांच्या इलर्निंग प्लॅटफॉर्मद्वारे विद्यापीठामध्ये प्रवेश मिळावे या उद्देशाने ही स्थापना केली गेली. लोक, व्यावसायिक, उद्योजक, कार्यकारी आणि व्यवसाय आणि सांस्कृतिक कलाकार कामगार बाजारात योगदान देण्यासाठी. हेडक्वार्टर, ज्याला मिलान इंटरनॅशनल कॅम्पस किंवा नोव्हॅड्रेटचा कॅम्पस देखील म्हटले जाते, शांत हिरव्या ब्रायनझाच्या कॅम्पसमध्ये नोव्हिड्रेट (कोमो, इटली) च्या माजी आयबीएम प्रशिक्षण केंद्रात आहे.

अभियांत्रिकी, अर्थशास्त्र, मानसशास्त्र, कला, कायदा: विद्यापीठात 5 आभासी विद्याशाखा आहेत. ऐतिहासिक नकाशे आणि प्रश्नोत्तरी प्रकल्प सिटी वॉल सिसेना शहराचे वैशिष्ट्य आहे. त्याचा विंचू आकार ऐतिहासिक केंद्राला नव्या झोनमधून विभागतो.

ऐतिहासिक कार्टोग्राफिक दस्तऐवज त्याच्या उत्क्रांतीचे आणि तिच्या विध्वंसांचे वर्णन करतात. क्यूजीआयएस प्रोग्राम मला वेगवेगळ्या ऐतिहासिक नकाशांची तुलना करण्याची परवानगी देतो, कारण तो जिओरफरेन्सिंग प्लगइनद्वारे समान संदर्भ प्रणालीतील सर्व नकाशे हस्तांतरित करण्यास परवानगी देतो. संदर्भ म्हणून ओपन लेयर गूगल उपग्रह आणि ओपन लेअर ओपन स्ट्रीट मॅपचा संदर्भ सर्व ऐतिहासिक नकाशे संदर्भ प्रणाली ईपीएसजी: 3857 (वेब मर्केटर किंवा स्यूडो मर्केटर) कडे देण्यासाठी वापरला गेला आहे.

क्यूजीआयएस हे वेक्टोरियल लेयर किंवा शेपफिल्सद्वारे या भौगोलिक नकाशेची विस्तृत व्याख्या करणे, त्यांचे विश्लेषण करणे आणि त्यांची तुलना करण्याची मूलभूत साधने आहे, ज्यात मी रस्ते, इमारती, उद्याने आणि उद्याने, सिटी वॉल, प्राचीन तटबंदी आणि बुरुज यासारख्या नकाशाच्या सर्व घटकांचे स्मरण केले आहे. प्राचीन सिटी गेट्स. मी पंचुअल, रेखीय आणि बहुभुज स्तर वापरले. मी विश्लेषण, संशोधन, भौगोलिक प्रक्रिया, भूमिती आणि डेटा व्यवस्थापन साधने (चित्र 1) या थरांची तुलना केली.

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

हे साधन वापरुन, मला याबद्दल माहिती मिळाली:
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- सिटी वॉलचे मॉर्फोलॉजिकल बदल जसे की त्याच्या प्राचीन तटबंदीचे बुरुज आणि प्राचीन सिटी गेट्स पाडणे;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

तेथे बरेच QGIS साधने आहेत आणि मी यापैकी काही वापरण्यासाठी वापरली:
- विद्यमान सिटी वॉलच्या रेषीय लेयरच्या प्रत्येक भागास फोटोंसह जोडलेले दुवे, जे संवर्धनाची वास्तविक स्थिती दर्शवितात;
- प्रिंट संगीतकारांद्वारे 19 व्या शतकातील सेसेनाचा नकाशा;
- क्विगिस 2 थ्रीज प्लगइन (चित्र 3) असलेले सेसेनाचे 3 डी मॉडेल;

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## निष्कर्ष
ऐतिहासिक नकाशे महत्त्वाची कागदपत्रे आहेत जरी त्यातील शुद्धतेची तुलना प्रत्यक्ष कार्टोग्राफिक दस्तऐवजाच्या शुद्धतेशी केली जाऊ शकत नाही आणि जे भौगोलिक प्रतिनिधित्वाचे विशेषज्ञ नाहीत अशा लोकांसाठी ते संप्रेषणात्मक प्रतिनिधित्त्व आहेत. क्यूजीआयएस हे एकमेव साधन होते ज्यामुळे मला प्रभावी आणि अर्थपूर्ण प्रतिनिधित्त्वानुसार ऐतिहासिक नकाशांची संख्यात्मक सामग्री वापरण्याची परवानगी मिळाली.
## ग्रंथसूची निर्देशांक
ऐतिहासिक नकाशे याद्वारे काढले गेले आहेतः
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

ऐतिहासिक माहिती याद्वारे काढली गेली आहेः
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## लेखक
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
