---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/uruguay_mides1.png
title: استخدام QGIS في وزارة التنمية الاجتماعية في أوروغواي (MIDES)
type: case-study

---
{{<content-start >}}
# استخدام QGIS في وزارة التنمية الاجتماعية في أوروغواي (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## المقدمة
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## QGIS في قسم الجغرافيا من DINEM
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

تقديم الخدمات اللوجستية لتوثيق مثل هذا العمل الميداني باستخدام حزم إحصائية لإدارة قاعدة البيانات التي تم إنشاؤها ، إلى جانب الاستخدام المكثف لنظام المعلومات الجغرافية لتنظيم الرحلات الميدانية وبيانات البيانات الجغرافية المرتجعة.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

على الرغم من أن البرمجيات الاحتكارية قد تم تنفيذها عندما بدأت عملية العمل ، إلا أن تطوير المهام نفسها طلب منها تدريجياً تحويلها إلى برمجيات مفتوحة المصدر. بما أن العملية ككل أصبحت محوسبة بشكل أكبر - مع تضمين محرك سير العمل وقاعدة بيانات جغرافية مكانية في PostGIS - فقد شجعتنا متطلبات الترخيص والفوائد التي توفرها خيارات البرمجيات الحرة والمفتوحة المصدر (FOSS) على إجراء التغيير. وبهذه الطريقة ، عندما تم تنقيح مشروع QGIS (عدد أقل من الخلل والمزيد من الوظائف) ، تمكنا من تلبية احتياجاتنا باستخدام نظام QGIS. سمحت الأدوات المرتبطة بـ PostGIS لفريق العمل بالتنسيق السريع للمهام المطلوبة من أجل تحقيق استقرار الرحلات الميدانية اليومية ، بالإضافة إلى مهام التحليل اللاحقة على نفس العمل الميداني للبيانات الذي تم إنشاؤه ، بعد فترة وجيزة من تخفيفه وترقيمه.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## الخاتمة
أصبحت QGIS برنامجًا أساسيًا لقسم الجغرافيا في DINEM. يقدم أداءً ممتازًا للعمل مع الملفات الثقيلة والتفاعل مع PostGIS ومع محرك سير العمل الخاص بنا. وهذا يسمح لنا بالحصول على إدارة ممتازة للبيانات الجغرافية ، مما يجعل أيضًا إنتاج خرائط الأساس والرسوم البيانية المواضيعية ذات الجودة العالية.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## المؤلف
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

ريتشارد ديتوماسي - مستشار في قسم التحليل المكاني بقسم الجغرافيا (DINEM-MIDES ، أوروغواي). شهادة الدكتوراة طالب في العلوم الاجتماعية والدراسات السكانية. ماجستير في الدراسات المعاصرة في أمريكا اللاتينية. شهادة في العلوم الأنثروبولوجية.

مارتن هاهن - مستشار في قسم التحليل المكاني بقسم الجغرافيا (DINEM-MIDES ، أوروغواي). باخ. حاليا دراسة الجغرافيا.

على الرغم من حقيقة أن المقال الحالي كتبه الثلاثة المذكورين أعلاه ، هناك أكثر من مائة شخص يشاركون في العملية الموصوفة فيه ، لذلك ينتمي هذا العمل أساسًا إليهم.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
