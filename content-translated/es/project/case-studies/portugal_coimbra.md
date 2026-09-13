---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Usando herramientas código fuente para la caracterización de un paisaje. El
  complemento LecosS
type: case-study

---
{{<content-start >}}
# Usando herramientas código fuente para la caracterización de un paisaje. El complemento LecosS
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

La caracterización de un paisaje se lleva a cabo utilizando índices cuantitativos diseñados por métricas pasisajísticas. Estos índices se utilizan para describir las características estructurales del paisaje, para documentar el cambio y su relación con la aparición de varias especies o grupos de especies (Turner et al, 2001; Olsen et al, 2007; Fidalgo et al., 2009). El número de métricas es extremadamente grande y puede calcularse a nivel de paisaje, clase y fragmento(Turner et al, 2001; Fidalgo et al, 2009.). Las métricas se pueden calcular a partir de Corine Land Cover, el uso de la tierra (COS 90 y COS2006) o los mapas de la cobertura terrestre producidos por nosotros. Según Martin Jung (2012), las Estadísticas de Ecología del Paisaje (Lecos) es un módulo de QGIS utilizado para calcular las métricas del paisaje en capas ráster. El resultado está disponible en formato CSV.
## Métodos
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Calculamos el área de cobertura del suelo, la proporción del paisaje, densidad de aristas, número de parcelas, parcela de mayor área, parcela de menor área, longitud media de parcela y tamaño efectivo de malla ( Tabla 1). Se calcularon medidas de la diversidad del paisaje según el índice de Shannon, la Uniformidad y el índice de Simpson.
## Resultados
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusión
Fue posible determinar las métricas del paisaje utilizando el complemento LecoS, señalando que el área de estudio presenta problemas de fragmentación debido al alto grado de alteración humana. QGIS demostró ser bastante intuitivo y muy práctico en el cálculo de las métricas del paisaje en ausencia de cualquier restricción. De hecho, es una solución robusta y viable en comparación con software con licencia. En el futuro, pretendemos aplicar este método a áreas que tienen problemas con especies invasoras para estudiar su comportamiento en el paisaje.
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

El artículo fue aportado en Julio de 2014 por André Duarte. Tiene un título en Ingeniería de Recursos Forestales y un Máster en Recursos Forestales de la Escuela Agraria Superior de Coimbra. Licenciado en Sistemas de Información Geográfica por Geopoint. Actualmente colabora con el Grupo Portucel Soporcel.

{{<content-end >}}
