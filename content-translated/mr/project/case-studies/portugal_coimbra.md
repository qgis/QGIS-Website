---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: लँडस्केपच्या वैशिष्ट्यासाठी ओपन सोर्स साधने वापरणे. लेकोस प्लगइन
type: case-study

---
{{<content-start >}}
# लँडस्केपच्या वैशिष्ट्यासाठी ओपन सोर्स साधने वापरणे. लेकोस प्लगइन
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2014</span>
</p>

This case study results from the final draft of the Graduate Geographic Information Systems taught by GeoPoint. We proposed to study a landscape using Landscape Ecology plugin (LecoS) in QGIS 2.01 Dufour. The study was conduted in a region of central Portugal, Municipality of Coimbra, with an total area of 31940ha and it has geographic coordinates 40°12\'11.84\" North, 8°24\'37.15\" West. Because the new administrative reorganization this municipality are divided into 18 parishes, which are mostly urban areas (Figure 1).

<figure>
<img src="../images/portugal_coimbra1.png" class="align-left" alt="portugal_coimbra1.png" />
<figcaption>Geographic location of the municipality of Coimbra.</figcaption>
</figure>

लँडस्केपचे वैशिष्ट्य लँडस्केप मेट्रिक्सद्वारे डिझाइन केलेले परिमाणात्मक निर्देशांकांचा वापर करून केले जाते. हे निर्देशक नंतर लँडस्केपच्या स्ट्रक्चरल वैशिष्ट्यांचे वर्णन करण्यासाठी, अनेक प्रजाती किंवा प्रजातींच्या घटनेशी संबंधित बदल आणि त्यांचे संबंध दस्तऐवजीकरण करण्यासाठी वापरले जातात (टर्नर एट अल, 2001; ऑल्सेन एट अल, 2007;. फिडाल्गो एट अल., 2009). मेट्रिक्सची संख्या अत्यंत मोठी आहे आणि लँडस्केप पातळी, वर्ग आणि डाग (टर्नर एट अल, 2001;. फिडाल्गो एट अल, 2007.) वर मोजली जाऊ शकते. मेट्रिक्सची गणना कोरीन लँड कव्हर, लँड यूज (सीओएस 90 आणि सीओएस2006) किंवा आमच्याद्वारे उत्पादित लँड कव्हरच्या नकाशातून करता येते. मार्टिन जंग (2012) च्या मते, लँडस्केप इकोलॉजी स्टॅटिस्टिक्ज (लेकोस) क्यूजीआयएसचे मॉड्यूल आहे जे रास्टर थरांमध्ये लँडस्केप मेट्रिकची गणना करण्यासाठी वापरला जातो. परिणाम सीएसव्ही स्वरूपात उपलब्ध होऊ शकतो.
## पद्धती
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

आम्ही जमीन आच्छादन क्षेत्र, लँडस्केप प्रमाण, धार घनता, पॅचेसची संख्या, सर्वात मोठे पॅच क्षेत्र, सर्वात लहान पॅच क्षेत्र, सरासरी पॅच अंतर आणि प्रभावी जाळीआकार (तक्ता 1) मोजतो. लँडस्केपच्या विविधतेचे मोजमाप शॅनन निर्देशांक, एकरूपता आणि सिम्पसन निर्देशांक म्हणून मोजले गेले.
## निकाल
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## निष्कर्ष
लेकोस प्लगइनचा वापर करून लँडस्केप मेट्रिक्स निश्चित करणे शक्य झाले आहे हे लक्षात घेता की मानवी अस्थिरतेची उच्च पातळी असल्यामुळे अभ्यासाचे क्षेत्र खंडित होण्याची समस्या दर्शविते. कोणत्याही अडचणी नसतानाही लँडस्केप मेट्रिक्सच्या मोजणीत QGIS हे अत्यंत अंतर्ज्ञानी आणि अत्यंत व्यावहारिक असल्याचे सिद्ध झाले. मालकी सॉफ्टवेअर सोल्यूशनच्या तुलनेत हे खरोखर एक मजबूत आणि व्यवहार्य आहे. भविष्यात लँडस्केपमध्ये आक्रमक प्रजातींच्या त्यांच्या वर्तणुकीचा अभ्यास करण्यासाठी समस्या असलेल्या भागात ही पद्धत लागू करण्याचा आमचा मानस आहे.
## संदर्भ
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- टर्नर, एम.जी., आर. गार्डनर, एट अल. (2001)। सिद्धांत आणि व्यवहारातील लँडस्केप इकोलॉजी: पॅटर्न आणि प्रक्रिया. न्यूयॉर्क।

## लेखक:
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

या लेखाचे योगदान आंद्रे दुआर्टे यांनी जुलै 2014 मध्ये केले होते. त्यांनी एस्कोला सुपीरियर अग्रारिया डी कोइम्ब्रा येथून वन संसाधनांमध्ये अभियांत्रिकी पदवी आणि मास्टर ऑफ फॉरेस्ट्री रिसोर्सेस ची पदवी घेतली आहे. जिओपॉईंटद्वारे भौगोलिक माहिती प्रणालीमध्ये पदवीधर. सध्या ग्रुपो पोर्टुसेल सोपोर्सेलसोबत सहकार्य करत आहे.

{{<content-end >}}
