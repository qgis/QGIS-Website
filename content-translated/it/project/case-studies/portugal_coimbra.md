---
HasBanner: false
archived: true
date: 2014-07-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/portugal_coimbra1.png
title: L'uso di strumenti open source per la caratterizzazione di un paesaggio. Il
  plugin LecosS
type: case-study

---
{{<content-start >}}
# L'uso di strumenti open source per la caratterizzazione di un paesaggio. Il plugin LecosS
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

La caratterizzazione del paesaggio è condotto utilizzando gli indici quantitativi di metrica del paesaggio. Tali indici sono quindi utilizzati per descrivere le caratteristiche strutturali del paesaggio, per documentare il cambiamento e la loro relazione con l'insorgenza di diverse specie o gruppo di specie (Turner et al, 2001 ;.  Olsen et al, 2007 ;.  Fidalgo et al. , 2009).  Il numero di parametri è estremamente ampia e può essere calcolato a livello del paesaggio, classe e macchia (Turner et al, 2001 ;.  Fidalgo et al, 2009. ).  Le metriche possono essere calcolate dal Corine Land Cover, uso del suolo (COS 90 e COS2006) o mappe di copertura del suolo prodotta da noi. Secondo Martin Jung (2012), Landscape Ecology Stistics (Lecos) è un modulo di Qgis utilizzato per calcolare le metriche del paesaggio nei livelli raster. Il risultato può essere disponibile in formato CSV.
## Metodi
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Landscape metrics calculated for diferent years (1990 and 2006).</figcaption>
</figure>

Si calcola l'area di copertura del suolo, proporzione del paesaggio, densità, numero di macchie, quella più grande, quella più piccola, distanza e la dimensione effettiva delle macchie (Tabella 1).  Le misure di diversità del paesaggio sono state calcolate con lo Shannon index, l'uniformità e lo Simpson index.
## Risultati
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model to calculate landscape metrics in 1990.</figcaption>
</figure>

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Conclusione
E 'stato possibile determinare le metriche di paesaggio utilizzando il plugin LecoS, notando che l'area di studio presenta problemi di frammentazione a causa l'elevato grado di disturbo antropico. Qgis ha dimostrato di essere molto intuitivo e molto pratico nel calcolo delle metriche di paesaggio in assenza di alcun vincolo. È davvero robusto e semplice rispetto alla soluzione software proprietario. In futuro abbiamo intenzione di applicare questo metodo alle aree che hanno problemi con le specie invasive per studiare il loro comportamento nel paesaggio.
## Riferimenti
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Landscape ecology in theory and practice: pattern and process. New York.

## Autori
<figure>
<img src="../images/portugal_coimbra4.png" class="align-left" alt="portugal_coimbra4.png" />
<figcaption>André Duarte</figcaption>
</figure>

Questo articolo è stato scritto nel luglio 2014 da André Duarte. Ha una laurea in ingegneria in risorse forestali e Maestro delle Risorse Forestali della Escola Superior Agraria de Coimbra. Laurea in Sistemi Informativi Territoriali da GeoPoint. Attualmente collabora con il Grupo Portucel Soporcel.

{{<content-end >}}
