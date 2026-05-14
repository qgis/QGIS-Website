---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Open source gereedschappen gebruiken voor het karakteriseren van een landschap.
  De plug-in LecosS
type: case-study

---
{{<content-start >}}
# Open source gereedschappen gebruiken voor het karakteriseren van een landschap. De plug-in LecosS
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

Het karakteriseren van het landschap werd uitgevoerd met behulp van kwantitatieve indices, ontworpen door metrische gegevens van het landschap. Deze indices werden toen gebruikt om de structurele karakteristieken van het landschap, de wijziging te documenteren en hun relatie met de aanwezigheid van verscheidene soorten of groepen van soorten te beschrijven (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). Het aantal metrische gegevens is extreem groot en kan worden berekend op het niveau van landschap, klasse en vlek (Turner et al, 2001;. Fidalgo et al, 2009.). Metrische gegevens kunnen worden berekend met behulp van Corine Land Cover, Land use (COS 90 en COS2006) of kaarten van landgebruik geproduceerd door ons. Volgens Martin Jung (2012), is de Landscape Ecology Stistics (Lecos) een module van QGIS die wordt gebruikt in metrische gegevens van landschappen te berekenen in rasterlagen. Het resultaat kan beschikbaar worden gesteld in de indeling CSV.
## Methoden
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

We berekenden het gebruik van het land, proportie van het landschap, dichtheid van randen, aantal gronddelen, grootste gebied gronddeel, kleinste gebied gronddeel , gemiddelde afstand tussen gronddelen en de effectieve grootte van de mazen (Tabel 1). Metingen van de diversiteit van het landschap werden berekend met de Shannon-index, Uniformiteit en de Simpson-index.
## Resultaten
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusie
Het was mogelijk de metrische gegevens van het landschap te bepalen met behulp van de plug-in LecoS met dien verstande dat het te bestuderen gebied fragmentatieproblemen weergeeft ten gevolge van de hoge mate van menselijke verstoring. QGIS bewees heel intuïtief en heel praktisch te zijn in het berekenen van metrische gegevens voor het landschap door de afwezigheid van enige beperking. Het is inderdaad robuust en betrouwbaar, vergeleken met de oplossingen van commerciële software. In de toekomst zijn we van plan om deze methode toe te passen op gebieden die problemen hebben met invasieve soorten om hun gedrag in het landschap te bestuderen.
## Verwijzingen
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Landscape ecology in theory and practice: pattern and process. New York.

## Auteurs
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Dit artikel werd bijgedragen in juli 2014 door André Duarte. Hij heeft een Engineering Degree in Forest Resources and Master of Forestry Resources van de Escola Superior Agrária de Coimbra. Graduate in Geographic Information Systems door Geopoint. Werkt momenteel samen met Grupo Portucel Soporcel.

{{<content-end >}}
