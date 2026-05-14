---
HasBanner: false
archived: true
date: 2012-07-01
draft: false
featured: false
section: progetto
sidebar: true
thumbnail: images/portugal_ribeira1.png
title: QGIS e GRASS per la modellazione di corridoi ecologici per i lupi nel Nord
  del Portogallo
type: case-study

---
{{<content-start >}}
# QGIS e GRASS per la modellazione di corridoi ecologici per i lupi nel Nord del Portogallo
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>July 01, 2012</span>
</p>

The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

<figure>
<img src="../images/portugal_ribeira1.png" class="align-right" alt="portugal_ribeira1.png" />
<figcaption>Study area in Portugal</figcaption>
</figure>

Ribeira de Pena è un comune nel distretto di Vila Real nel nord del Portogallo. E 'un comune rurale, caratterizzato da agricoltura, pascolo, foreste, montagne, valli e diversificata fauna e da bassa densità umana, che offre rifugio e cibo per lupi. Situato in una zona di transizione tra l'aspro e montuoso Trás-os-Montes e il verdeggiante Minho, Ribeira de Pena è uno dei comuni che possono offrire un corridoio ecologico tra le aree con una concentrazione maggiore del lupo a nord con la più bassa concentrazione nel sud.

Ho iniziato a usare il software GIS durante il mio corso di biologia, e più spesso durante la mia tesi di laurea. In quel momento ho usato principalmente il software proprietario. Dopo che ho finito la mia laurea, non ho più utilizzato il software proprietario.

Nel frattempo, sono entrato nel nuovo mondo di Linux. Dopo di che sono stato contattato per aiutare alcuni ricercatori di modellare corridoi ecologici per i lupi a Ribeira de Pena, utilizzando GIS, in quanto non hanno mai lavorato con questo tipo di software. Poiché stavo già usando Linux invece di Windows, il mio primo problema era che il software da utilizzare. Poi ho sentito parlare di QGIS e ho deciso di fare un tentativo, anche se sembrava molto riduttivo e incompleto, rispetto a ciò che già sapevo. Ho subito capito che mi sbagliavo, e sono davvero entusiasta per la capacità analitica di QGIS, specialmente con l'integrazione GRASS.

To model the ecological corridors, we used the QGIS along with the GRASS plugin. We used several geographic information along with presence data of the species to model the ecological corridors. Here are some of the functions of both QGIS and GRASS used in this case, just to name a few:
- plugin Interpolation in QGIS: to create a Digital Elevation Model
- r.watershed in GRASS: to create water streams from DEM
- r.grow.distance in GRASS: generates a raster map layer of distance to features in input layer
- r.reclass in GRASS: to reclassify map layers
- r.slope.aspect.slope in GRASS: to calculate the slope from the DEM
- r.mapcalculator in GRASS: to calculate some simple map algebra
- r.cost.coord in GRASS: creates a raster map showing the cumulative cost of moving between different geographic locations on an input raster map whose cell category values represent cost
- r.drain in GRASS: Traces a flow through an elevation model on a raster map — the one used to create the corridors

With this work we obtained a map with the potential ecological corridors for wolf in Ribeira de Pena municipality. These are areas to be considered by the city council technicians when planning conservation measures for the species. These corridors are of extreme importance because they can connect the fragile wolf packs in Vila Real in the south with those in the north, which are continuous with those from Peneda-Gerês and Spain far more stable. It is from particular importance those corridors that cross human settlements, like small villages, cities and roads. These areas must be considered critical for wolf conservation, and applied measures to reduce human impact in this species.

<figure>
<img src="../images/portugal_ribeira2.png" class="align-right" style="width:100.0%" alt="portugal_ribeira2.png" />
<figcaption>Ecological corridors and critical conservation areas for wolves in northern Portugal.</figcaption>
</figure>

## Conclusione
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Autore
<figure>
<img src="../images/portugal_ribeiraaut.png" class="align-left" height="200" alt="portugal_ribeiraaut.png" />
<figcaption>Monica Almeida</figcaption>
</figure>

Questo articolo è stato scritto nel mese di luglio del 2012 da Monica Almeida. È una biologa che lavora in un'organizzazione non governativa per la conservazione del lupo in Portogallo.

{{<content-end >}}
