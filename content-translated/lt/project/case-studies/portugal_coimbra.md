---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: projektą
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Atviro kodo įrankių naudojimas charakterizuojant kraštovaizdį. LecosS priedas
type: case-study

---
{{<content-start >}}
# Atviro kodo įrankių naudojimas charakterizuojant kraštovaizdį. LecosS priedas
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

Kraštovaizdžio charakterizavimas vykdomas naudojant kraštovaizdžio metrikų nustatytais kiekybiniais rodikliais. Šie rodikliai vėliau naudojami aprašant struktūrines kraštovaizdžio charakteristikas, dokumentuojant pakeitimus ir jų ryšį su kai kurių rūšių ar rūšių grupių atsiradimu (Turner et al, 2001; Olsen et al, 2007; Fidalgo et al, 2009). Metrikų skaičius labai didelis ir gali būti skaičiuojamas kraštovaizdžio lygiui, klasei ar žymai (Turner et al, 2001;. Fidalgo et al, 2009.). Metrikos gali būti skaičiuojamos naudojant Corine Land Cover žemėnaudą (COS 90 ir COS2006) arba mūsų sukurtus žemėnaudos žemėlapius. Pasak Martin Jung (2012), kraštovaizdžio ekologijos statistika (Lecos) yra QGIS modulis, naudojamas skaičiuojant kraštovaizdžio metrikas rastro sluoksniuose. Rezultatai įrašomi CSV formatu.
## Metodai
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Mes skaičiuojame žemės padengimo plotą, kraštovaizdžio proporcijas, kampų skaičių, lopų skaičių, didžiausią lopą, mažiausią lopą, vidutinį lopo atstumą ir efektyvų tinklelio dydį (1 lentelė). Taipogi skaičiuotos kraštovaizdžio įvairovės metrikos, Shannon indeksas, vienodumas ir Simpsono indeksas.
## Rezultatai
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Išvada
Naudojant LecoS priedą pavyko nustatyti kraštovaizdžio metrikas, pastebint, kad studijos vietovė yra problematiška - fragmentuota dėl didelės žmogaus įtakos. QGIS pasirodė labai intuityvus ir labai praktiškas įrankis skaičiuojant kraštovaizdžio metrikas be jokių apribojimų. Jis tikrai greitas ir tinkamas, lyginant su komercinės programinės įrangos sprendimais. Ateityje mes planuojame naudoti šį metodą vietose, kur esama problemų su invazinėmis rūšimis, tiriant jų elgseną kraštovaizdyje.
## Šaltiniai
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Kraštovaizdžio ekologijos teorija ir praktika: šablonai ir procesas. New York'as.

## Autoriai
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Šį straipsnį 2014 liepą parašė André Duarte. Jis turi Miško resursų inžinieriaus laipsnį ir miško resursų magistrą Escola Superior Agrária de Coimbra. Geopoint Geografinių informacinių sistemų absolventas. Šiuo metu bendradarbiauja su Grupo Portucel Soporcel.

{{<content-end >}}
