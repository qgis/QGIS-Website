---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: استخدام أدوات مفتوحة المصدر لتوصيف منظر طبيعي. البرنامج المساعد LecosS
type: case-study

---
{{<content-start >}}
# استخدام أدوات مفتوحة المصدر لتوصيف منظر طبيعي. البرنامج المساعد LecosS
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

يتم إجراء توصيف منظر طبيعي باستخدام مؤشرات كمية صممتها مقاييس المناظر الطبيعية. ثم تستخدم هذه المؤشرات لوصف الخصائص الهيكلية للمناظر الطبيعية ، لتوثيق التغيير وعلاقتهم مع حدوث عدة أنواع أو مجموعة من الأنواع (تيرنر وآخرون ، 2001 ؛. Olsen وآخرون ، 2007 ؛. Fidalgo et al.، 2009). عدد المقاييس كبير للغاية ويمكن حسابه على مستوى المناظر الطبيعية ، الطبقة وصبغة (تيرنر وآخرون ، 2001 ؛. Fidalgo et al، 2009.). يمكن حساب المقاييس من غطاء أرض كورين ، واستخدام الأرض (COS 90 و COS2006) أو خرائط الغطاء الأرضي التي ننتجها. وفقًا لمارتن جانج (2012) ، فإن إيكولوجيات علم البيئة الطبيعية (Lecos) هي وحدة من نظام QGIS المستخدم لحساب مقاييس المناظر الطبيعية في الطبقات النقطية. يمكن أن تكون النتيجة متاحة بتنسيق CSV.
## أساليب
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

نحن نحسب مساحة الغطاء الأرضي ، نسبة المناظر الطبيعية ، كثافة الحواف ، عدد البقع ، أكبر منطقة التصحيح ، أصغر منطقة التصحيح ، متوسط ​​المسافة بين البقعة والحجم الشبكي الفعال (الجدول 1). تم حساب مقاييس التنوع في مؤشر Shannon و Uniformity و Simpson index.
## النتائج
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## الخاتمة
كان من الممكن تحديد مقاييس المناظر الطبيعية باستخدام البرنامج المساعد LecoS مشيرا إلى أن منطقة الدراسة تمثل مشاكل تجزئة بسبب ارتفاع درجة الاضطراب البشري. أثبتت QGIS أن تكون بديهية للغاية وعملية جدا في حساب مقاييس المناظر الطبيعية في غياب أي قيد. إنه بالفعل قوي وقابل للتطبيق مقارنة بحل البرمجيات الاحتكارية. في المستقبل نعتزم تطبيق هذه الطريقة على المناطق التي لديها مشاكل مع الأنواع الغازية لدراسة سلوكها في المشهد.
## المراجع
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner، M. G.، R. Gardner، et al. (2001). بيئة المناظر الطبيعية من الناحية النظرية والممارسة: نمط وعملية. نيويورك.

## المؤلف
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

ساهم هذا المقال يوليو 2014 من قبل أندريه دوارتي. حصل على درجة هندسية في الموارد الحرجية وماجستير في الموارد الحرجية من Escola Superior Agrária de Coimbra. تخرج في نظم المعلومات الجغرافية من قبل Geopoint. تتعاون حاليًا مع Grupo Portucel Soporcel.

{{<content-end >}}
