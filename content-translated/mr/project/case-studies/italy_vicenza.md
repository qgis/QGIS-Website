---
HasBanner: false
archived: true
date: 2012-05-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/italy_vicenza1.png
title: इटलीच्या मोंटेचिओ मॅगीगोर, विसेन्झा नगरपालिकेत शहरी नियोजनासाठी क्यूजीआयएस
  वापरणे
type: case-study

---
{{<content-start >}}
# इटलीच्या मोंटेचिओ मॅगीगोर, विसेन्झा नगरपालिकेत शहरी नियोजनासाठी क्यूजीआयएस वापरणे
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2012</span>
</p>

Montecchio Maggiore is a small town in the middle west of Vicenza (about 24.000 population). And as many other italian municipality it manages the town planning; in particular the urban planning and what we call "recovery plan" aka PDR —— Piani Di Recupero. This urbanistic tool is dedicated to the historical area in the center of the town and it requires a specific study: building state of conservation, intended use, particular historical notice via survey and restitution to produce planimetric and prospectus graphics. For this purpose it has used QGIS in addition to Postgresql/Postgis database, PHP code and Libreoffice suite, QCAD (LibreCAD).
## कार्य
<figure>
<img src="../images/italy_vicenza1.png" class="align-right" alt="italy_vicenza1.png" />
<figcaption>Workflow Schema</figcaption>
</figure>

स्कीमा वर्कफ्लो स्पष्ट करेल:

प्रत्येक इमारतीचा डेटा सर्व्हेद्वारे प्राप्त केला गेला होता आणि कागदाच्या वेळापत्रकात लिहिला गेला. एकदा कार्यालयात डेटा कॅनॉनिकल वेब ब्राउझर (फायरफॉक्स, आइसवेसल) वापरून पीएचपी फॉर्मद्वारे पोस्टग्रेसक्यूएल / पोस्टगिस डेटाबेसमध्ये टाकला गेला. दुसर्‍या क्षणी प्रत्येक इमारतीचा आकार क्यूजीआयएसने रेखाटला आणि आयडी की फील्डद्वारे (पोस्टग्रेसएसक्यूएल / पोस्टगिस व्ह्यू) सर्वेक्षण सर्वेक्षणात जोडला गेला.

त्याच वेळी इमारतींचे दर्शनी भाग क्यूसीएडी (लिब्रेकॅड) वापरून तयार केले गेले होते.

PDR (piani di recupero) ने कठोर ग्राफचे कठोर नियम पाळले पाहिजेत ज्यांना विशिष्ट ग्राफिक्स आवश्यक आहेत:
- सद्यस्थिती
- प्रकल्प राज्य
- हेतू वापर (सध्या)
- हेतू वापर (प्रकल्प)
- हस्तक्षेपाचा प्रकार दाखल

सर्व ग्राफिक थीमॅटिक नकाशे सर्वेक्षण आणि (डिझाइन फेज) दरम्यान सुधारित डेटा आणि सर्वेक्षण दरम्यान डेटा पुनर्प्राप्त गुण आणि डेटा वापरून तयार केले गेले.

Thus a photo was linked to every building facilitating the design and analisys in the gis project (using the "action" feature). The SQL tools (pgquery, postgis manager, dbmanager et al.) allowed to obtain very sophisticated query immediately viewable in the map canvas such as: volume calculation split by building intended use, standards area calculation in percentage of the total planning area and other minor queries. All useful items for the design and planning study otherwise not possible without a very strength tool like gis (and QGIS in particular).

<figure>
<img src="../images/italy_vicenza2.png" class="align-right" alt="italy_vicenza2.png" />
<figcaption>QGIS project with building data viewing</figcaption>
</figure>

शेवटी प्रत्येक इमारतीचा संश्लेषण अहवाल लिब्रोऑफिस स्वीटचा वापर करुन तयार केला गेला. या अहवालात फोटो, कार्टोग्राफीच्या अर्कचा सारांश तयार करण्यात आला आहे जो सध्याच्या राज्याच्या स्पर्धेत आणि डेटामध्ये इमारत स्थानिकीकृत करतो.

<figure>
<img src="../images/italy_vicenza3.png" class="align-right" alt="italy_vicenza3.png" />
<figcaption>QGIS print composer for final graphic layout</figcaption>
</figure>

## निष्कर्ष
The strength of QGIS is the very user friendly interface coupled with the several tools it offers. The connection with vary data formats (shape files, spatialite db, postgresql/postgis db,\...) facilitates and increases the interoperability between different worlds. And thus the freedom offered by the free software (QGIS, PHP, Libreoffice, QCAD) stimulates and open new horizons.

आणि शेवटचे परंतु कमीतकमी नाहीः आम्ही वेगवेगळ्या प्लॅटफॉर्मवर काम केले (विंडोज 7 64 बिट, विंडोज एक्सपी 32 बिट, डेबियन सर्व्हर आणि डेबियन क्लायंट) परंतु आम्हाला कधीही अकल्पनीय समस्या आल्या नाहीत.
## लेखक
<figure>
<img src="../images/italy_vicenzaaut.png" class="align-left" height="200" alt="italy_vicenzaaut.png" />
<figcaption>Flavio Rigolon</figcaption>
</figure>

This article was contributed May 2012 by Flavio Rigolon. He lives in Vicenza (Italy) and works in Montecchio Maggiore municipality as SIT manager. He has migrated almost all the gis data from proprietary to free platform (QGIS, Postgresql/Postgis, Spatialite). He is a member of GFOSS.it (Associazione Italiana per l\'Informazione Geografica Libera) since 2007 and was a member of the GFOSS.it board from 2010 to 2012.

{{<content-end >}}
