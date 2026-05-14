---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: المشروع
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: استخدام QGIS لتعيين مناطق Hotspot للتنوع البيولوجي وخدمات النظام الإيكولوجي
  (HABEaS)
type: case-study

---
{{<content-start >}}
# استخدام QGIS لتعيين مناطق Hotspot للتنوع البيولوجي وخدمات النظام الإيكولوجي (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

الهدف الرئيسي من هذا المنبر هو توفير الوصول الحر إلى مجموعة واسعة من البيانات حول التنوع البيولوجي وخدمات النظام الإيكولوجي لحوض البحر المتوسط ​​التي كانت مبعثرة في عدد من الكيانات العامة والخاصة. تغطي HABEaS WebGIS حاليًا جنوب البرتغال ، ولكن بحلول نهاية عام 2012 / بداية عام 2013 سيتم توسيعها إلى شمال البرتغال وكذلك إلى كانتون Tuzla في البوسنة والهرسك. على المدى الطويل ، نريد توسيع هذه الأداة إلى حوض البحر الأبيض المتوسط ​​بأكمله.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

كما استخدمت WWF المعلومات الجغرافية الواردة في HABEaS لتقديم الدعم لتحديد الغابات ذات القيمة المرتفعة للغابات (HCVF) في جنوب البرتغال ، وهي خطوة إلزامية لمالكي الأراضي الذين يريدون أن تحصل الغابات على مجلس الإشراف على الغابات (FSC)شهادة.

![](../images/portugal_lisbon3.jpg)

لتحديد قيم الحفظ التي تحدث في كل خاصية ، استخدمنا SEXTANTE Modeller لإنشاء برنامج نصي يتقاطع مع جميع طبقات HABEaS مع حدود الخاصية. باستخدام الأداة نفسها ، تمكنا أيضًا من إنشاء برنامج نصي يقوم تلقائيًا بحساب كمية الكربون المخزنة حاليًا في كل موقع.

![](../images/portugal_lisbon4.jpg)
## الخاتمة
إن نظام QGIS سهل الاستخدام ولديه إمكانات قوية للغاية في مجال المعالجة الجيولوجية. سمح لنا دمج أدوات GRASS GIS و SAGA GIS من خلال أدوات SEXTANTE بإجراء عدد من التحليلات المكانية المعقدة وربطها باستخدام SEXTANTE Modeler. كما كان من السهل جدًا إنتاج خرائط عالية الجودة باستخدام "مطبوعات الطباعة" الجديدة وتصديرها بتنسيق SVG لمزيد من التعديل باستخدام Inkscape الذي يعد محرر رسومات متجه قوي المصدر المفتوح.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## المؤلف
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

فيليبي دياس طالب دكتوراة في مركز علم البيئة التطبيقي (Instituto Superior de Agronomia، Techinical University of Lisbon) ومستشار لبرنامج البحر المتوسط ​​العالمي للصندوق العالمي للطبيعة (WWF).

{{<content-end >}}
