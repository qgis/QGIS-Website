---
HasBanner: false
archived: true
date: 2010-07-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/mexico_jalisco1.jpg
title: Trabalhar com o QGIS na infraestrutura de dados espaciais em Jalisco no México
type: case-study

---
{{<content-start >}}
# Trabalhar com o QGIS na infraestrutura de dados espaciais em Jalisco no México
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2010</span>
</p>

O Instituto de Informação Territorial do Estado de Jalisco é uma organização governamental que foi fundada em 1998 para partilhar informação geográfica entre agências de governo de Jalisco no México.

<figure>
<img src="../images/mexico_jalisco1.jpg" class="align-right" alt="mexico_jalisco1.jpg" />
<figcaption>Exploring the data with its online viewer</figcaption>
</figure>

Durante anos, a instituição reuniu um conjunto de informações em diversos formatos, tais como SHP, DWG, DXF, GeoTIFF e ECW, entre outros. Portanto, o que nós queríamos era ter toda esta informação disponível, organizado e num formato comum, com o objectivo de ser capaz de fornecer e exibi-lo através da Internet.

<figure>
<img src="../images/mexico_jalisco2.jpg" class="align-right" alt="mexico_jalisco2.jpg" />
<figcaption>Connecting to the Spatial Data Infrastructure with WMS</figcaption>
</figure>

That\'s how it was developed the Sistema de Información Territorial Estatal en Línea, with the main target to build a spatial data infrastructure which allows our government agencies to share this kind of information to be included in their own projects as health, security or mobility.
## Decisão para o QGIS
I decided to use Mapserver and PostgreSQL with PostGIS extension to be able to deliver our satellite imagery, orthopothos, digital elevation models and vector information with Web Map Services, thinking that any application will consume our services. But the problem was that many of the commercial and free applications don't work with OGC standards, specially with WFS. After exploring many geographic information systems, I realized that QGIS was the only one which can connect to WMS, WCS and WFS successfully.
## Para que usamos o QGIS
Internally, we use QGIS to check the raster and vector data of the agencies before publishing it, and after its integration, we used it again to test the Web services that we've created. Also, we have done many spatial analysis with QGIS pulling the data directly from our PostgreSQL spatial database, then, we export the results as shape files.

<figure>
<img src="../images/mexico_jalisco3.jpg" class="align-right" alt="mexico_jalisco3.jpg" />
<figcaption>Connecting to the Spatial Data Infrastructure with WFS</figcaption>
</figure>

We're encouraging our users to download QGIS and link directly with our Sistema de Información Territorial Estatal en Línea, mainly because it fully supports OGC standards and has many interesting features like geoprocessing tools, which allow them to make analysis of their interest, and all this absolutely for free.
## Conclusão
This project understood as the technological component of a Spatial Data Infrastructure, has been considered as a PostGIS case study, and I have to say that working with open source in all of our system's cycle, has been satisfactory and trustworthy, the best choice that we have found to share our geographic information.
## Autor
<figure>
<img src="../images/mexico_jaliscoaut.jpg" class="align-left" height="200" alt="mexico_jaliscoaut.jpg" />
<figcaption>Carlos Ruiz</figcaption>
</figure>

This article was contributed in July 2010 by IC Carlos Ruiz. He works as project\'s coordinator at the Instituto de Información Territorial del Estado de Jalisco, Mexico.

{{<content-end >}}
