---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Utilizando ferramentas de código aberto para a caraterização de uma paisagem.
  O plug-in LecoS
type: case-study

---
{{<content-start >}}
# Utilizando ferramentas de código aberto para a caraterização de uma paisagem. O plug-in LecoS
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

A caracterização de uma paisagem é levada a cabo usando índices quantitativos designados por métricas da paisagem. Estes índices são depois utilizados para descrever as características estruturais da paisagem, para documentar a mudança ou a sua relação com a ocorrência de várias espécies ou grupo de espécies (Turner et al., 2001; Olsen et al., 2007; Fidalgo et al., 2009). O número de métricas é enorme, podendo ser calculado ao nível da paisagem, da classe e da mancha (Turner et al., 2001; Fidalgo et al., 2009). As métricas podem ser calculadas a partir da Corine Land Cover, da Carta de Ocupação do solo (COS 90 e COS2006) ou de mapas de Uso/Ocupação do solo por nós produzidas. Segundo Martin Jung (2012), o Landscape Ecology Stistics (LecoS) é um módulo do Qgis que serve para calcular métricas da paisagem em camadas raster. O resultado pode ficar disponível em formato CSV.
## Métodos
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

As métricas calculadas foram a Área de cada uso do solo (Land Cover), a Proporção que cada uso tem na paisagem (Landscape Proportion), a densidade de orlas (Edge density), Número de manchas (Number of Patches), Área da mancha maior, Área da mancha mais pequena, distância média entre manchas (Mean patch distance) e o tamanho efetivo da malha (effective meshsize) (Tabela 1). Quanto às medidas de diversidade da paisagem calculadas foram o índice de Shannon, Uniformidade e o Índice de Simpson.
## Resultados
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusões
Foi possível determinar as métricas da paisagem recorrendo ao módulo LecoS constatando-se que a área de estudo apresenta problemas de fragmentação devido ao elevado grau de antropização.
O QGIS revelou-se bastante intuitivo e muito prático no cálculo das métricas da paisagem não existindo qualquer tipo de constrangimento. É de facto uma solução robusta e viável comparativamente com os softwares proprietário. No futuro pretende-se aplicar este método a áreas que tenham problemas com espécies invasoras para estudar o seu comportamento na paisagem.
## Referências
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

Este artigo foi contribuído pelo André Duarte em Julho de 2014. Ele tem uma Licenciatura e Mestrado em Engenharia de Recursos Florestais da Escola Superior Agrária de Coimbra. é Pós-Graduado em Sistemas de Informação Geográfica pela Geopoint. Atualmente é colaborador do Grupo Portucel Soporcel.

{{<content-end >}}
