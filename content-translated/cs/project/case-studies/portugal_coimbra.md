---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Použití nástrojů s otevřeným zdrojovým kódem pro charakterizaci krajiny. Zásuvný
  modul LecosS
type: case-study

---
{{<content-start >}}
# Použití nástrojů s otevřeným zdrojovým kódem pro charakterizaci krajiny. Zásuvný modul LecosS
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

Charakteristika krajiny se provádí pomocí kvantitativních ukazatelů navržených krajinnými metrikami. Tyto indexy se pak používají k popisu strukturálních charakteristik krajiny, k dokumentaci změn a jejich vztahu k výskytu několika druhů nebo skupin druhů (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). Počet metrik je mimořádně velký a lze je vypočítat na úrovni krajiny, třídy a skvrny (Turner et al, 2001;. Fidalgo et al, 2009.). Metriky lze vypočítat z Corine Land Cover, Land use (COS 90 a COS2006) nebo z námi vytvořených map Land Cover. Podle Martina Junga (2012) je Landscape Ecology Stistics (Lecos) modul QGIS, který slouží k výpočtu krajinných metrik v rastrových vrstvách. Výsledek může být k dispozici ve formátu CSV.
## Metody
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Vypočítáme plochu krajinného pokryvu, podíl krajiny, hustotu okrajů, počet políček, největší plochu políčka, nejmenší plochu políčka , střední vzdálenost políček a efektivní velikost sítě (tabulka 1). Míry diverzity krajiny byly vypočteny Shannonův index, Uniformita a Simpsonův index.
## Výsledky
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Závěr
Pomocí pluginu LecoS bylo možné určit krajinné metriky s tím, že studovaná oblast představuje problém fragmentace v důsledku vysoké míry narušení člověkem. QGIS se ukázal jako poměrně intuitivní a velmi praktický při výpočtu krajinných metrik při absenci jakéhokoli omezení. Ve srovnání s proprietárním softwarovým řešením je skutečně robustní a životaschopný. V budoucnu hodláme tuto metodu aplikovat na oblasti, které mají problémy s invazními druhy, abychom mohli studovat jejich chování v krajině.
## Reference
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Landscape ecology in theory and practice: pattern and process. New York.

## Autoři
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Do tohoto článku přispěl v červenci 2014 André Duarte. Má inženýrský titul v oboru lesních zdrojů a magisterský titul v oboru lesních zdrojů z Escola Superior Agrária de Coimbra. Absolvent oboru Geografické informační systémy společnosti Geopoint. V současné době spolupracuje s Grupo Portucel Soporcel.

{{<content-end >}}
