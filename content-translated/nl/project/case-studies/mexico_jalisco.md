---
HasBanner: false
archived: true
date: 2010-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/mexico_jalisco1.jpg
title: Werken met QGIS in de ruimtelijke infrastructuur voor gegevens van Jalisco
  in Mexico
type: case-study

---
{{<content-start >}}
# Werken met QGIS in de ruimtelijke infrastructuur voor gegevens van Jalisco in Mexico
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 juli 2010</span>
</p>

Het Instituto de Información Territorial del Estado de Jalisco is een gouvernementele organisatie die werd opgericht in 1998 om geografische informatie te delen tussen de gouvernementele agentschappen van Jalisco in México.

<figure>
<img src="../images/mexico_jalisco1.jpg" class="align-right" alt="mexico_jalisco1.jpg" />
<figcaption>De gegevens verkennen met zijn online viewer</figcaption>
</figure>

In de loop van de jaren heeft het instituut heel veel informatie verzameld in verschillende indelingen, zoals SHP, DWG, DXF, GeoTIFF en ECW, naast andere. Wat we dus wilden was al deze informatie beschikbaar maken, georganiseerd en in een algemene indeling met als doel het ter beschikking te stellen en zichtbaar te zijn via het internet.

<figure>
<img src="../images/mexico_jalisco2.jpg" class="align-right" alt="mexico_jalisco2.jpg" />
<figcaption>Verbinden door WMS met de Spatial Data Infrastructure</figcaption>
</figure>

Dat is hoe het werd ontwikkeld als het Sistema de Información Territorial Estatal en Línea, met als hoofddoel een infrastructuur voor ruimtelijke gegevens te bouwen die het voor gouvernementele agentschappen mogelijk maakt dit soort informatie te delen om het op te nemen in hun eigen projecten voor gezondheid, veiligheid of mobiliteit.
## Keuze voor QGIS
Ik besloot om Mapserver en PostgreSQL met de extensie PostGIS te gebruiken om in staat te zijn onze satellietafbeeldingen, orthografische foto's, digitale hoogtemodellen en vectorinformatie af te leveren met Web Map Services, ervan uitgaande dat elke toepassing onze services kon verwerken. Maar het probleem was dat vele van de commerciële en gratis toepassingen niet werken met de standaarden van OGC, in het bijzonder met WFS. Na het verkennen van vele geografische informatiesystemen realiseerde ik me dat QGIS de enige was die met succes kon verbinden met WMS, WCS en WFS.
## Waar gebruiken we QGIS voor
Intern gebruiken we QGIS om de raster- en vectorgegevens van de agentschappen te controleren voordat ze worden gepubliceerd, en na de integratie, gebruikten we het opnieuw om de webservices die we hebben gemaakt te testen. Ook hebben we veel ruimtelijke analyses gedaan met QGIS, waar we de gegevens rechtstreeks uit onze ruimtelijke database van PostgreSQL haalden en dan de resultaten exporteerden als shapefiles.

<figure>
<img src="../images/mexico_jalisco2.jpg" class="align-right" alt="mexico_jalisco2.jpg" />
<figcaption>Verbinden door WFS met de Spatial Data Infrastructure</figcaption>
</figure>

We moedigen onze gebruikers aan QGIS te downloaden en direct te verbinden met ons Sistema de Información Territorial Estatal en Línea, voornamelijk omdat het de standaarden voor OGC volledig ondersteunt en veel interessante mogelijkheden heeft, zoals gereedschappen voor geoprocessing, wat hen in staat stelt analyses te maken op hun gebied van interesse, en dat allemaal gratis.
## Conclusie
Dit project, bedoeld als de technologische component van een infrastructuur voor ruimtelijke gegevens, is beschouwd als een praktijkvoorbeeld voor PostGIS, en ik moet zeggen dat het werken met open source, in de gehele cyclus van ons systeem, veel voldoening gaf en betrouwbaar was, de beste keuze die we hebben kunnen vinden om onze geografische informatie te delen.
## Auteur
<figure>
<img src="../images/mexico_jaliscoaut.jpg" class="align-left" height="200" alt="mexico_jaliscoaut.jpg" />
<figcaption>Carlos Ruiz</figcaption>
</figure>

Dit artikel werd bijgedragen in juli 2010 door IC Carlos Ruiz. Hij werkt als projectcoördinator aan het Instituto de Información Territorial del Estado van Jalisco, Mexico.

{{<content-end >}}
