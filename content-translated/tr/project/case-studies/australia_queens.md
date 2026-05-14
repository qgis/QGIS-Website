---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: proje
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS ve GRASS, Yerel Yönetimler Orman Yanıgını Tehlike Haritalama'da.
type: case-study

---
{{<content-start >}}
# QGIS ve GRASS, Yerel Yönetimler Orman Yanıgını Tehlike Haritalama'da.
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Giriş
Güney Downs Bölgesel Konseyi (SDRC) güney doğu Queensland, Avustralya'da bir küçük-orta ölçekli yerel yönetimdir. Meclis özellikle bölgenin güney kısmında büyük orman yangınlarından muzdarip. Orman yangınları Güney Downs Bölgesi sakinleri ve arazi sahipleri için can ve mal kaybına ve gerçek bir endişeye neden olmuştur.

Bu proje, meclisin ve bölge halkının riskin farkında olmasına ve gelecekte daha iyi kararlar vermelerine katkıda bulunacaktır.

![](../images/australia_queens1.jpg)
## Proje
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

Projenin CBS tarafı 6 ana adımla çökmüş
- Şev değerlendirme ve haritalama
- En boy değerlendirme ve haritalama
- Bitki değerlendirme ve haritalama
- Orman Yangınının ciddiyetini belirlemek için puanlar birleştirilir
- Saha doğrulama ve nitel değerlendirme
- Nihai Haritalar

## QGIS ve GRASS kullanımı
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

The QGIS GRASS plugin was used to import 5 meter contours of the whole region into GRASS which were then converted into a contour raster map using r.surf.contour. A slope and aspect map were then generated using r.slope.aspect from the raster contour map. Categories were assigned to different slope and aspect ranges and given a hazard risk sore. Vegetation areas were also given different risk scores. All the resulting raster maps were then combined using mapcalc and given a final risk hazard score. The risk scores are then divided into three main categories: high; medium; and low.

The final part of the process was field verification via the rural fire service. After the review process, QGIS was used to print the final maps for presentation.

As all GRASS commands can be run from the command line, all the commands that were needed to generate the bushfire hazard maps were recorded, for documentation purposes and for if the maps needed to be regenerated some time in the future.
## Sonuç
Overall QGIS, together with the GRASS plugin, provided a great experience and a great final outcome for the council doing their own bushfire hazard mapping. The GRASS plugin provides a very easy to use interface to GRASS through QGIS. As QGIS is able to open the GRASS raster format natively, integration is very seamless and maps can be made with ease.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referanslar
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Yazar
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Bu makale Nathan Woodrow tarafından Ocak 2011'de katkıda bulunulmuştur. Nathan, Southern Downs Bölgesel Konseyi'nde bir CBS memuru ve Souther Queensland Üniversitesi'nde Mekansal Bilim ortak derecesi okuyor

{{<content-end >}}
