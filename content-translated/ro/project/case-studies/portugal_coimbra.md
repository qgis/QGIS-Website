---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: Utilizarea instrumentelor cu sursă deschisă pentru caracterizarea unui peisaj.
  Plugin-ul LecosS
type: case-study

---
{{<content-start >}}
# Utilizarea instrumentelor cu sursă deschisă pentru caracterizarea unui peisaj. Plugin-ul LecosS
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

Caracterizarea unui peisaj se realizează cu ajutorul indicilor cantitativi proiectați de metricile de peisaj. Acești indici sunt apoi folosiți pentru a descrie caracteristicile structurale ale peisajului, pentru a documenta modificarea și relația lor cu apariția mai multor specii sau grupuri de specii (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al., 2009). Numărul de metrici este extrem de mare și poate fi calculat la nivel de peisaj și clasă (Turner et al, 2001;. Fidalgo et al, 2009). Metricile pot fi calculate din hărțile de utilizare a terenului Corine Land Cover (COS 90 și COS2006) sau din hărțile de acoperire produse de noi. Potrivit lui Martin Jung (2012), Landscape Ecology Stistics (Lecos) este un modul de QGIS, utilizat pentru a calcula metricile de peisaj în straturile raster. Rezultatul poate fi disponibil în format CSV.
## Metodele
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Se calculează suprafața terenului de acoperit, proporția peisajului, densitatea marginilor, numărul de zone, suprafața celei mai mici zone, distanța medie între zone și dimensiunea ochiului de plasă efectivă (Tabelul 1). Prin măsurarea diversității peisajului s-a calculat indicele Shannon, uniformitatea și indicele Simpson.
## Rezultate
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Concluzii
A fost posibilă determinarea metricilor de peisaj folosind plugin-ul LecoS, remarcându-se faptul că zona de studiu prezintă probleme de fragmentare din cauza gradului ridicat de anxietate umană. QGIS s-a dovedit a fi destul de intuitiv și foarte practic în calculul metricilor de peisaj, în absența oricărei constrângeri. Este într-adevăr robust și viabil, comparativ cu soluțiile proprietare. În viitor ne-am propus să aplicăm această metodă în zonele care au probleme cu speciile invazive, pentru a le studia comportamentul în peisaj.
## Referințe
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Ecologia peisagistică în teorie și îń practică: model și proces. New York.

## Autori
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Acest articol a fost transmis în iulie 2014 de către André Duarte. El are o diplomă în Ingineria Resurselor Forestiere și un masterat în Resursele Forestiere la Școala Superioară de Agricultură din Coimbra. Absolvent în Sisteme Informatice Geografice la Geopoint. În prezent, colaborează cu Grupo Portucel Soporcel.

{{<content-end >}}
