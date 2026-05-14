---
author: Radoslaw Guzinski
categories:
- Case studies
date: '2015-04-01'
description: Enabling the Use of Earth Observation Data for Integrated Water Resource
  Management in Africa
draft: 'true'
heroImage: ''
tags:
- water
- case-study
- showcase
thumbnail: wois.png
title: Water Observation and Information System
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## सिस्टम वर्णन
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

प्रोसेसिंग साधनपॅकचा मुख्य फायदा म्हणजे डेटा प्रोसेसिंग व विश्लेषणासाठी वेगळ्या अल्गोरिदम प्रदात्यांकडून कार्यशीलता अखंडपणे वापरण्याची क्षमता आहे. हे स्वयंचलित प्रसंस्करण मॉडेल तयार करण्यासाठी वापरले जाऊ शकते आणि, TIGER-NET प्रकल्पात विकसित झालेल्या QGIS प्लगइनद्वारे, विविध प्रदात्यांपासून अल्गोरिदम एकत्रित करून विझार्ड-आधारित प्रोसेसिंग चेन्स मध्ये एकत्रित केले जाऊ शकते. जल संसाधन व्यवस्थापन अंतर्गत ईओ डेटा विश्लेषणाशी संबंधित सामान्य परंतु गुंतागुंतीच्या कामे करण्यासाठी हे कार्यक्षमता मानक वर्कफ्लोची एक लायब्ररी तयार करण्यासाठी वापरली गेली होती (सूचनांसह).

![The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)](africa_tiger1.jpg)

आफ्रिकेतील एकात्मिक जलसंवर्धन व्यवस्थापनास चालना देण्यासाठी डब्ल्यूओआयएसचा परिचालनात्मक आणि व्यावहारिक वापर, विविध प्रकारचे थीम आणि माहिती उत्पादनांसह वापरकर्त्याच्या विशिष्ट प्रदर्शनांचे प्रकरणांद्वारे प्रदर्शित केले गेले आहे. यामध्ये: तलावाच्या पाण्याची गुणवत्ता; पूर संधारण; जमिनीचा अवनत व जमीन व्यापाराचे लक्षण वर्णन; जलमित्र मंडळे आणि हायड्रॉलिक मॉडेलिंग. प्रदर्शन प्रकरणांमध्ये कित्येक स्तर आहेत. प्रथम, विनंती केलेले उत्पादने आणि अनुप्रयोगांसाठी सानुकूल केलेले अंतिम-टू-एन्ड प्रोसेसिंग वर्कफ्लो विकसित केले आहेत. वापरकर्त्यांनी विनंती केल्याप्रमाणे महत्त्वपूर्ण क्षेत्रे आणि कालावधी यानुसार उत्पादन वर्धित करिता त्या वर्कफ्लोचा वापर केला जातो. अंतिम चरणात, कार्यप्रवाह (उदा. त्यांचे स्थिरता / कार्यक्षमता आणि वापरात सोपी) तसेच उत्पादन निष्कर्ष वापरकर्त्यांसह जवळच्या संवादामध्ये मूल्यांकन केले जात आहेत.

![Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.](africa_tiger2.jpg)
## निष्कर्ष
WOIS चा विकास वापरकर्ता-चालित आणि सहयोगी विकास मॉडेलचे एक यशस्वी उदाहरण दर्शवितो, जेथे कार्यक्षमतेची रचना, विकसित आणि वापरकर्ता-नियुक्त प्रकरणांद्वारे मूल्यमापन केले गेले आहे जेणेकरुन पाणी व्यवस्थापन आणि एकात्मिक पाणी वाढविण्यावर प्रणालीचा वास्तविक परिणाम प्रदर्शित करण्यासाठी. संसाधन व्यवस्थापन योजना. WOIS आधीच प्रमुख आफ्रिकन नदी खोरे प्राधिकरण, अनेक आफ्रिकन मंत्रालये आणि एजन्सी तसेच संशोधन आणि मानवतावादी संस्थांमध्ये लागू केले आहे. त्यामुळे नवीन कार्यक्षमता आणि कार्यात्मक सुधारणांसाठी आणि सामान्य सॉफ्टवेअर, अल्गोरिदम आणि पद्धती सुधारणांमुळे सतत वापरकर्त्याच्या आवश्यकतांच्या प्रतिसादात ते विकसित होत राहील.

ESA सेंटिनेल टूलबॉक्सेस WOIS मध्ये समाकलित करून आणि समर्पित उत्पादन कार्यप्रवाह विकसित करून नवीन सेंटिनेल उपग्रह प्रणालीसाठी प्रक्रिया क्षमतेचे समर्थन आणि अंमलबजावणी सुनिश्चित करण्यावर विशेष लक्ष केंद्रित केले जाईल. WOIS चे पुढील प्रकाशन (एप्रिल 2015 च्या दुसऱ्या सहामाहीत) आधीच सेंटिनेल-1 टूलबॉक्स आणि पूर निरीक्षण, वॉटर बॉडी मॅपिंग इत्यादीसाठी या नवीन रडार डेटासेटचा वापर करणारे अनेक वर्कफ्लो समाविष्ट करेल. हे WOIS ला पूर्णपणे-कार्यरत मॉनिटरिंग सिस्टममध्ये बदलेल. या परवाना-मुक्त, शक्तिशाली आणि विस्तारित प्रणालीच्या तरतुदीद्वारे आणि सतत क्षमता निर्माण आणि प्रशिक्षण प्रयत्नांद्वारे, प्रकल्प विस्तारासाठी आधार तयार करण्यासाठी भरभराट करतो, उदा. आफ्रिका आणि त्यापलीकडे इतर देश आणि प्रदेशांमध्ये रोल-आउट करा.
## संदर्भ
- बॉयर-गॉटवेन, पी., जेन्सेन, आय. एच., गुझिंस्की, आर., ब्रेडॉफ्ट, जी. के. टी., हॅन्सन, एस., आणि मिचेलोव्हस्की, सी आय. (2015). कविंगो नदीच्या बेसिन केस स्टडी: खराब गॉजड बेसिन मध्ये अंदाजानुसार नदीचे निर्वाह. हायड्रोलॉजी अॅण्ड अर्थ सिस्टम सायन्सेस, 19(3), 1469 -1485.
- गुझिंस्की, आर .; कास, एस .; ह्यूबर, एस .; बॉयर-गॉटवेन, पी .; जेन्सेन, आय. एच .; नाइमी, वी .; दुबोकोवा, एम .; वाली, ए .; टॉटरप , सी. पाणी निरीक्षण आणि माहिती प्रणालीसह आफ्रिकेतील एकत्रित जल संसाधन व्यवस्थापनासाठी पृथ्वीवरील अवलोकन डेटा वापर सक्षम करणे. रिमोट सेन्स. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## दुवे
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### लेखक
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
