---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: proxecto
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Empregando ferramentas de código aberto para a caracterización da paisaxe.
  O plugin LecoS
type: case-study

---
{{<content-start >}}
# Empregando ferramentas de código aberto para a caracterización da paisaxe. O plugin LecoS
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

A caracterización da paisaxe lévase a cabo empregando índices cuantitativos deseñados a través de medicións da paisaxe. Estes índices empréganse despois para describir os trazos estruturais da paisaxe, para documentar a mudanza e as súas relacións coa presenza de varias especies ou grupos de especies (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). O número de medicións é extremadamente elevada e poden calcularse ó nivel da paisaxe, de clase e de tesela (Turner et al, 2001;. Fidalgo et al, 2009.). As medicións poden calcularse dende a Cobertura do Terreo de Corine, usos do Terreo (COS 90 e COS 2006) ou mapas de cobertura do terreo producidos por nós. De acordo con Martin Jung (2012), as Estatísticas de Ecoloxía da Paisaxe (LecoS) é un módulo de QGIS empregado para calcular medicións da paisaxe en capas ráster. O resultado pode estar dispoñíbel en formato CSV.
## Métodos
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Calculamos a área de cobertura da terra, Proporción da Paisaxe, densidade de límites, número de parcelas, área coas parcelas máis grandes, área coas parcelas máis pequenas, distancia media da parcela e tamaño efectivo da grella (Táboa 1). As medidas de diversidade da paisaxe calculáronse mediante o índice de Shannon, o índice de Uniformidade e o índice de Simpson.
## Resultados
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusión
It was possible to determine the landscape metrics using the LecoS plugin noting that the study area presents problems of fragmentation due to the high degree of human disturbance. QGIS proved to be quite intuitive and very practical in the calculation of landscape metrics in the absence of any constraint. It is indeed a robust and viable compared to proprietary software solution. In the future we intend to apply this method to areas that have problems with invasive species to study their behavior in the landscape.
## Referencias
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Landscape ecology in theory and practice: pattern and process. New York.

## Autores
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Este artigo entregouse en xullo de 2014 por André Duarte. El ten un Grao en Enxeñería en Recursos Forestais e un Máster en Recursos Forestais da Escola Superior Agrária de Coimbra. Graduado en Sistemas de Información Xeográfica por Geopoint. Actualmente colabora co Grupo Portucel Soporcel.

{{<content-end >}}
