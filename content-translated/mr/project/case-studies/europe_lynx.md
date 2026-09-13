---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/europe_lynx1.png
title: दक्षिणी कार्पेथियन्समध्ये लिंक्सचे अधिवास विश्लेषण
type: case-study

---
{{<content-start >}}
# दक्षिणी कार्पेथियन्समध्ये लिंक्सचे अधिवास विश्लेषण
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

ओपन सोर्स डेटाच्या आधारे विद्यार्थ्यांसाठी वन्यजीव अधिवास मॉडेलिंगच्या मूलभूत आकलनास प्रोत्साहन देण्यासाठी केस स्टडी.
## परिचय
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## कार्यपद्धती
सर्व गोळा केलेल्या डेटावर क्यूजीआयएस २.6 आणि २.8 सह प्रक्रिया केली गेली, जी ईटीआरएस / S / ईटीआरएस-एलईईए मध्ये प्रक्षेपित केली गेली आणि ईयू मानकांच्या पूर्ततेसाठी इन्स्पायर निर्देशानुसार संग्रहित केली. एकूणच ** वेट्सची वेगळी इंडेक्स ** परिभाषित केली गेली आणि सर्व इनपुट डेटावर लागू केली.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

** वर्कफ्लो वर्णन **
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

* टीप: लँड कव्हरचे वर्ग शक्य लिंक्सच्या घटना आणि मानवी क्रियाकलापानुसार गटबद्ध केले गेले. तांत्रिकदृष्ट्या जुन्या मूळचे असले तरीही, वन सुधारण दर्शविण्यासाठी आणि स्थानिक डेटा सेटमध्ये सामील होण्याचे सामान्य उदाहरण म्हणून वन कव्हर मूल्यांशी संबंधित माहिती एकत्रित केली गेली.
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
```
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
```
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
```
* टीपः हंटर Accessक्सेसीबीलिटी मॉडेल रस्त्यांपर्यंत आणखी अंतर आणि भागाच्या उताराद्वारे शिकारीच्या क्षेत्रात जाण्याची कमी होण्याची शक्यता दर्शविते.

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## निष्कर्ष
अंतिम आउटपुट (आकृती 3) पाहता, प्रथम संभाव्य अधिवास विश्लेषण विश्लेषण यशस्वी झाल्याचे दिसून आले, परंतु मुख्य म्हणजे मूलभूत मॉडेलिंग स्वतः सुरुवातीच्या अपेक्षेपेक्षा कमी कठीण असल्याचे दिसून आले. शिकारीच्या प्रवेशयोग्यतेसाठी सब-मॉडेल जोडण्याच्या आमच्या निवडीमुळे आम्हाला अधिवास जोखमीच्या मूल्यांकनासंदर्भात आणखी एक परिमाण लागू करण्याची परवानगी मिळाली, जी आधीपासूनच अस्तित्वात असलेल्या परिस्थितीत सहजपणे बसविली जाऊ शकते आणि उदा. पायाभूत सुविधा तथापि, काही महत्वाच्या अधिवास माहिती, जसे की वन रचना (आमची सर्वोच्च अधिवास अनुकूलता) उपलब्ध डेटा सेट्सद्वारे मिळू शकत नाही आणि जटिल प्रजातींच्या वर्तनासह एकत्रितपणे, परिणामी मूलभूत आणि अपूर्ण म्हणून समजले जाणे आवश्यक आहे. या टप्प्यावर अंमलबजावणी न केलेले अतिरिक्त घटक म्हणजे रस्ते मृत्यू, भूप्रदेश आणि उदासीनता आणि तपशीलवार शिकार घटना.

त्याच्या मुक्त स्त्रोताशिवाय, विनामूल्य उपलब्ध वर्ण, क्यूजीआयएस सॉफ्टवेअर अलिकडच्या वर्षांत मोठ्या घडामोडींचा विषय बनला आहे. आम्ही अनुभवी वापरकर्त्यांसाठीदेखील विविध जीआरएएसएस आणि सागा साधनांचा वापर करण्यास अनुमती देऊन टूल बॉक्सच्या समाकलनासह खूप सकारात्मक अनुभव प्राप्त केला आहे. वेगवेगळ्या आवृत्त्या दरम्यान वारंवार बदलत असूनही सुसंगततेची समस्या उद्भवली नाही आणि डेटा सेटसह अंतर्ज्ञानाने कार्य करताना प्रशासकीय निर्बंधांच्या सामान्य अनुपस्थितीचा एक चांगला फायदा होऊ शकतो. आम्ही विशेषत: समाकलित केलेल्या मॉडेल बिल्डरच्या बाबतीत पुढील सुधारणा पहात आहोत.
## संदर्भ
- कॅक्सेंस्की, पी., चैपरॉन, जी., व्हॉन अव्रक्स, एम., ह्युबर, डी., Andन्ड्रॉन, एच. आणि लिन्नेल, जे. (डिसेंबर २०१२): युरोपमधील मोठ्या मांसाहारी लोकांची स्थिती, व्यवस्थापन आणि वितरण. दस्तऐवज युरोपियन कमिशन.
- स्काॅड, एस., रेविला, ई., वाईगँड, टी., नॉवर, एफ., कॅक्सेंस्की, पी., ब्रेटिनमोसर, यू. स्टॅनिसा, सी. आणि ट्रेपल, एल. (२००२): यूरेशियन लिंक्सच्या पुनर्प्रक्रियेसाठी मध्य युरोपियन लँडस्केप्सच्या उपयुक्ततेचे मूल्यांकन करणे. अनुच्छेद जर्नल ऑफ अप्लाइड इकोलॉजी.
- साल्वाटोरी, व्ही. (2004): कार्पेथियन पर्वतांमध्ये मोठ्या मांसाहारी संवर्धनाचे क्षेत्र. पीएचडी थीसिस.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- बुट्रोस, डी. (मार्च २००२): यूरेशियन लिंक्स (लिंक्स लिंक्स) डेन साइट्सचे वैशिष्ट्यीकरण आणि योग्यतेचे मूल्यांकन. कोरा अहवाल क्रमांक 12 ई, डिप्लोमा थीसिस.

### लेखक:
इंटरनेशनल फॉरेस्ट इकोसिस्टम मॅनेजमेंट बी.एस.सी., Gनी गिनील्के अनुक्रमे जर्मन वनीकरण आणि हेन्री हिल्टेनन हे मिक्केली युनिव्हर्सिटी ऑफ liedप्लाइडची एक्सचेंजची विद्यार्थीनी आहे. विज्ञान, फिनलँड. प्रो.मुंड हे २०१० पासून एच.एन.ई. इबर्सवाल्डे येथे जीआयएस आणि रिमोट सेन्सिंगचे व्याख्यान देत आहेत आणि या प्रकल्पाला मार्गदर्शन व तांत्रिक सहाय्य देत आहेत.

अधिक माहितीसाठी कृपया लुका.एह्रमिंजर (at) hnee.de, डेविड.विंजर (at) hnee.de, किंवा प्रोफेसर Dr.Jan- पीटर मुंड: जन-पीटर.मंड (येथे) hnee.de वर अधिक माहितीसाठी संपर्क साधा.

{{<content-end >}}
