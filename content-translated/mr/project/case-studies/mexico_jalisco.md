---
HasBanner: false
archived: true
date: 2010-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/mexico_jalisco1.jpg
title: मेक्सिकोमधील जॅलिसकोच्या अवकाशासंबंधी डेटाच्या पायाभूत सुविधांमध्ये क्यूजीआयएस
  बरोबर काम करणे
type: case-study

---
{{<content-start >}}
# मेक्सिकोमधील जॅलिसकोच्या अवकाशासंबंधी डेटाच्या पायाभूत सुविधांमध्ये क्यूजीआयएस बरोबर काम करणे
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2010</span>
</p>

इन्स्टिट्युटो डी इन्फॉर्मेशन टेरिटोरियल डेल एस्टॅडो डे जालिस्को ही एक सरकारी संस्था आहे जी मेक्सिकोमधील जॅलिस्कोच्या सरकारी एजन्सींमध्ये भौगोलिक माहिती सामायिक करण्यासाठी 1998 मध्ये स्थापन केली गेली.

<figure>
<img src="../images/mexico_jalisco1.jpg" class="align-right" alt="mexico_jalisco1.jpg" />
<figcaption>Exploring the data with its online viewer</figcaption>
</figure>

वर्षानुवर्षे संस्थेने एसएचपी, डीडब्ल्यूजी, डीएक्सएफ, जिओटीआयएफएफ आणि ईसीडब्ल्यू अशा अनेक स्वरूपात बरीच माहिती जमा केली आहे. तर, आम्हाला जे हवे होते ते इंटरनेटवर उपलब्ध करुन देण्यात आणि प्रदर्शित करण्याच्या उद्देशाने ही सर्व माहिती उपलब्ध, संयोजित आणि सामान्य स्वरूपात असणे आवश्यक आहे.

<figure>
<img src="../images/mexico_jalisco2.jpg" class="align-right" alt="mexico_jalisco2.jpg" />
<figcaption>Connecting to the Spatial Data Infrastructure with WMS</figcaption>
</figure>

That\'s how it was developed the Sistema de Información Territorial Estatal en Línea, with the main target to build a spatial data infrastructure which allows our government agencies to share this kind of information to be included in their own projects as health, security or mobility.
## QGIS साठी निर्णय
I decided to use Mapserver and PostgreSQL with PostGIS extension to be able to deliver our satellite imagery, orthopothos, digital elevation models and vector information with Web Map Services, thinking that any application will consume our services. But the problem was that many of the commercial and free applications don't work with OGC standards, specially with WFS. After exploring many geographic information systems, I realized that QGIS was the only one which can connect to WMS, WCS and WFS successfully.
## आम्ही कशासाठी QGIS वापरतो
Internally, we use QGIS to check the raster and vector data of the agencies before publishing it, and after its integration, we used it again to test the Web services that we've created. Also, we have done many spatial analysis with QGIS pulling the data directly from our PostgreSQL spatial database, then, we export the results as shape files.

<figure>
<img src="../images/mexico_jalisco3.jpg" class="align-right" alt="mexico_jalisco3.jpg" />
<figcaption>Connecting to the Spatial Data Infrastructure with WFS</figcaption>
</figure>

We're encouraging our users to download QGIS and link directly with our Sistema de Información Territorial Estatal en Línea, mainly because it fully supports OGC standards and has many interesting features like geoprocessing tools, which allow them to make analysis of their interest, and all this absolutely for free.
## निष्कर्ष
This project understood as the technological component of a Spatial Data Infrastructure, has been considered as a PostGIS case study, and I have to say that working with open source in all of our system's cycle, has been satisfactory and trustworthy, the best choice that we have found to share our geographic information.
## लेखक
<figure>
<img src="../images/mexico_jaliscoaut.jpg" class="align-left" height="200" alt="mexico_jaliscoaut.jpg" />
<figcaption>Carlos Ruiz</figcaption>
</figure>

This article was contributed in July 2010 by IC Carlos Ruiz. He works as project\'s coordinator at the Instituto de Información Territorial del Estado de Jalisco, Mexico.

{{<content-end >}}
