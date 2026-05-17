---
HasBanner: false
archived: false
date: 2015-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/china_hydro1.jpg
title: Produceren van een arcHYDRO-achtige uitvoer met QGIS
type: case-study

---
{{<content-start >}}
# Produceren van een arcHYDRO-achtige uitvoer met QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 januari 2015</span>
</p>

Ik werk voor een bedrijf voor stedelijke planning in China. Het is vaak moeilijk om de juiste milieutechnische bescherming te ontwerpen, omdat de algemene gegevensbronnen staatsgeheim zijn of zelfs niet eens bestaan. We worden regelmatig gevraagd om ontwerpen te maken zonder de juiste gegevens uit opnamen. In aanvulling daarop is er vaak niet meer tijd voor het juist opnemen. Mijn achtergrond is Stedelijke planning met als bijvak Milieuwetenschappen.

![](../images/china_hydro1.jpg)

De taak was een natuurreservaat te plannen aan de Chinese kant van de rivier Ili die 80% van het water van Lake Balkhash verschaft.  Toepassing van FOSS GIS + FOSS GIS gegevensopslag + onderwijs van FOSS GIS waren allemaal kritisch om de benodigde hydrologische en ecologische processen te reconstrueren en te modelleren voor authentieke planning van het reservaat.  Als een niet-wetenschapper zonder eerdere training of ervaring zou ik het niet hebben kunnen doen zonder alle drie.  Mijn bedrijf kon en wilde niet betalen voor GIS-software om de industriële standaard arcHYDRO te kunnen uitvoeren.

![](../images/china_hydro2.jpg)
## Het verhaal
Met enig proberen en fouten maken was ik in staat een uitvoer, die leek op arcHYDRO, uit QGIS te produceren. Beginnend met een USGS Hydrosheds DEM die werd geconverteerd naar een Regularized Spline with Tension met behulp van de functies voor GRASS in QGIS en training door Helena Mitsova. Met oppervlakte RST werd dit oppervlak geanalyseerd om de opvanggebieden en stroompaden te zoeken, en resulterende vectortopologiën werden geschoond in QGIS om het hydrologisch netwerk te genereren en ook om de attributentabellen op te bouwen.

![](../images/china_hydro3.jpg)

Dit netwerk werd gerangschikt door de extensie r.stream in GRASS om de volgorde voor stromen volgens build Hortons en Hacks te bouwen. Daarna werd een raster voor de oppervlakte van afstand tot uitvoer gegenereerd en geanalyseerd door gebiedsstatistieken om het verste punt te zoeken. Daarna r.drain in GRASS om een lijn voor tijd van concentratie (TOC) te traceren.  Tenslotte werd v.net in GRASS gebruikt om een netwerk van gietpunten, stroompaden, TOC-paden en HDMP te bouwen voor elke waterberging. In deze werkstroom was het gereedschap van QGIS Attributen per plaats van onschatbare waarde.

![](../images/china_hydro4.jpg)

Nadat het basis hydrologische netwerk was voltooid, gebruikte ik UN FAO soils database met samenvoegingen van tabellen voor het classificeren van de bodem. Daarna werden met behulp van functies voor query in QGIS de FAO-bodems geconverteerd naar USDA-bodems. Een eerder gedownload raster van USGS ETM7+ werd geclassificeerd door i.cluser en r.maxlik in GRASS naar een raster voor NLCD. Door tabellen voor hereclassificatie te gebruiken, converteerde ik het landgebruik naar het raster Manning's n-value grid voor de stroming over land. Tenslotte schreef ik een opzoektabel in r.mapcalc en voegde de rasters voor bodem en landgebruik samen naar NRCS TR-55 boognummers, gevolgd door de methodologie arcHYDRO.

![](../images/china_hydro5.jpg)

Ik voerde een statistische analyse uit op GHCN-tabellen om de mate van regenval voor terugkerende ontworpen stormen voor 1, 2,5 ,10, 50, 100 jaar te zoeken om de raster voor de neerslag te maken. Daarna downloadde ik een gratis voorbeeldraster van PRISM voor China en, uitgaande van een lineaire relatie,, converteerde gemiddelde celwaarden naar maximale celwaarden om de rasters voor maximale intensiteit van neerslag te bouwen.
## Conclusie
Ik begon uit wanhoop QGIS te gebruiken vanwege het ontbreken van arcMAP, maar nu wil ik nooit meer terug. De investering van tijd in FOSS is het waard, omdat u het mee kunt nemen naar elke baan. De combinatie van GRASS QGIS PostGIS geeft u de volledige functionaliteit van dure GIS-systemen. De verschafte online bronnen om te leren waren net zo waardevol als de eigenlijke software. Ik was in staat QGIS snel genoeg te leren om een groot project te produceren in een op snelheid gebaseerde industriële omgeving in de echte wereld.
## Auteur
<figure>
<img src="../images/china_hydro6.jpg" class="align-left" height="220" alt="china_hydro6.jpg" />
<figcaption>Robert Ward</figcaption>
</figure>

Robert Ward is een stedelijk ontwerper en GIS-analist bij Parsons Brinkerhoff, werkend op de kruising van hoogwaardige technologie en hoge kunst. Hij heeft onderwezen aan de Tongji University en Autodesk University.  Hij is geïnteresseerd in op GIS gebaseerde hydrologische & hydraulische modellen bouwen, landschap ecologie-modellen, evalueren van ecosystemen, transport-modellen en op GIS gebaseerde visualisatie van ontwerpen.

{{<content-end >}}
