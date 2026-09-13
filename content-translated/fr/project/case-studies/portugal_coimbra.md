---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Utilisation d'outils open source pour la caractérisation d'un paysage. L'extension
  LecosS
type: case-study

---
{{<content-start >}}
# Utilisation d'outils open source pour la caractérisation d'un paysage. L'extension LecosS
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

La caractérisation du paysage est conduite en utilisant une analyse quantitative basé sur des mesures sur le paysage. Ces indices sont ensuite utilisés pour décrire les caractéristiques structurelles du paysage, pour documenter les changement des relations entre l’occurrence de plusieurs espèces ou groupes d'espèces  (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). Le nombre de mesures est très important et peut générer des calculs au niveau du paysage, de la classe et de la marque ((Turner et al, 2001;. Fidalgo et al, 2009.). Les mesures peuvent être calculées depuis les données Corine Land Cover, l'Occupation du territoire (COS 90 and COS2006) ou les cartes d'occupation du territoire produites en interne. Selon Martin Jung (2012), l'extension Landscape Ecology Statistics (Lecos) de QGIS peut être utilisée pour calculer des métriques de paysage dans les couches raster. Le résultat peut être exporté au format CSV.
## Méthode
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Nous avons calculé les surfaces de couverture du sol, la proportion de paysage, la densité des bordures, le nombre d’ilots, la surface du plus grand ilot, la surface du plus petit ilot, la distance moyenne entre ilots et la taille de grille effective (Table 1). Les mesures de la diversité du paysage ont été calculées par l'index de Shannon, l'index d'uniformité et l'index de Simpson.
## Résultats
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusion
Il est possible de déterminer des métriques de paysage en utilisant l’extension Lecos en relevant que l'aire d'étude présente des problèmes de fragmentation dû à un niveau élevé de perturbations apportées par l'homme. QGIS a été très intuitif et très pratique pour les calculs des métriques, le tout sans contrainte. Il est de fait assez robuste et viable comparé aux solutions propriétaires. Dans le futur, nous planifions d'appliquer cette méthode aux territoires présentant des problèmes d'espèces invasives pour étudier leur comportement sur le paysage.
## Références
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

Cet article a été rédigé en juillet 2014 par la contribution de André Duarte. Il possède un diplôme d'ingénieur en ressources forestières ainsi qu'un master dans la même matière de l'Escola Superior Agrária de Coimbra. Il est également diplômé en SIG par Geopoint . Il collabore actuellement avec le Grupo Portucel Soporcel.

{{<content-end >}}
