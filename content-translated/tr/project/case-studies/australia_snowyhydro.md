---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: proje
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: Kar sınıflamasını otomatikleştirmek için işleme alet kutusunu kullanma
type: case-study

---
{{<content-start >}}
# Kar sınıflamasını otomatikleştirmek için işleme alet kutusunu kullanma
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

Snowy Hydro Limited (SHL) is a peak electricity generator based in the Snowy Mountains of New South Wales, Australia. Despite owning a variety of generation assets across the country, Snowy Hydro Limited is best known for the custodianship of an iconic piece of Australian infrastructure, the Snowy Mountains Hydro Electric Scheme.

The Snowy Mountains Hydro Electric Scheme, is made possible by seasonal snow falls in the New South Wales alpine region. Water from the spring snow melt is used to generate electricity addressing peak demand in the national electricity market, while also diverting water to the drier inland areas of South Eastern Australia for irrigation and agriculture.

Classifying snow cover over the winter months allows SHL to monitor the life cycle of the snow covered area, archive coverage areas for historical records, and provide coverage statistics to the hydrographic services team for water yield and storage forecasts.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## Artalan
Each year during the winter months (1st June to the 31st October) SHL obtains as many cloud free images as possible from the MODIS Terra (EOS AM) satellite. These images are then ingested into an algorithm known as the Normalised Difference Snow Index (NDSI), which is used to indicate areas where snow is present. While this algorithm is not unique to any one particular sensor, the MODIS instrument was chosen due to its adequate spatial resolution and daily coverage of the project area (Map 1.1 Snowy Water Catchment).
## Hedef
Bu projenin amacı NDSI akışını model olarak QGIS işleme aracında otomatikleştirmektir. İstenen çıktı karlı su tutma bünyesinde artırılmış, kilometre kare de çevirili toplam alanın tanımlanması ile beraber  karla kaplı vektör poligondur.
## Metod
NDSI algoritması oldukça basittir(Formül 1.1 de gösterilen Normalleştirilmiş Fark Kar İndeksi(NFKİ)) ve izleyen adımlar vektör formatında kaplayan karı almayı gerektirir hatta model araç işlemeye izin verir.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

This NDSI algorithm will return results between -1 and 1, with the threshold for snow typically being values greater than 0.4. An example of the NDSI output is shown below (Map 1.3 - NDSI output), alongside a natural colour image (Map 1.2 - MODIS true colour) for the 13th July 2014. As seen from these images the NDSI output is very good at discriminating snow covered areas from other land cover types and clouds. It can however misclassify portions of large water bodies as snow, caused by water having absorption characteristics in the Near Infrared part of the spectrum. This characteristic of the NDSI indicates the need to incorporate a water mask at some stage in the model.

<figure>
<img src="../images/australia_snowyhydro2.jpg" class="align-left" width="300" alt="australia_snowyhydro2.jpg" />
<figcaption>Map 1.2 - MODIS true colour</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro3.jpg" class="align-center" width="300" alt="australia_snowyhydro3.jpg" />
<figcaption>Map 1.3 - NDSI output</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro4.jpg" class="align-left" width="300" alt="australia_snowyhydro4.jpg" />
<figcaption>Map 1.4 - Recoded "Snow" vs "Non snow"</figcaption>
</figure>

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

<figure>
<img src="../images/australia_snowyhydro5.jpg" class="align-left" width="300" alt="australia_snowyhydro5.jpg" />
<figcaption>Map 1.5 - Extracted Snow</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro6.jpg" class="align-center" width="300" alt="australia_snowyhydro6.jpg" />
<figcaption>Map 1.6 - Snow inside the SWC</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro7.jpg" class="align-left" width="300" alt="australia_snowyhydro7.jpg" />
<figcaption>Map 1.7 - Final snow covered area</figcaption>
</figure>

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

<figure>
<img src="../images/australia_snowyhydro.png" class="align-center" width="600" alt="australia_snowyhydro.png" />
<figcaption>Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model</figcaption>
</figure>

## Netice/Sonuç
The QGIS processing toolbox is a powerful way to automate a workflow such as this snow classification. The model shown above successfully automates the snow classification process, and delivers a GIS dataset that can be used for visualisation and input into further statistical applications. It successfully removes subjective user error associated with previous methods used by SHL, while providing a repeatable and consistent classification tool. Some seasonal results can be viewed here.
### Yazar
Andrew Jeffrey Cooma NSW Avusturalya temelli Snowy Hydro Limited de GIS Analistidir. Wagga Wagga daki Charles Strut Üniversitesinden 2004 yılında Uzaysal Bilgi Sisteminde uzmanlaşarak mezun olmuştur. Snowy Hydro Limited deyken Cloud Seeding deneyi gibi mevcut projelere uzaysal destek sağladı ve günden güne kurumun her bölümünde çalıştı.

{{<content-end >}}
