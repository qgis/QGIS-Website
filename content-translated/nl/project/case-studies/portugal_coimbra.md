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
  <span>1 juli 2014</span>
</p>

Dit praktijkvoorbeeld resulteert uit de uiteindelijke weergave van Graduate Geographic Information Systems, gedoceerd door GeoPoint. We stelden voor een landschap te bestuderen met behulp van de plug-in Landscape Ecology (LecoS) in QGIS 2.01 Dufour. De studie werd uitgevoerd in een regio van centraal Portugal, gemeente Coimbra, met een totaalgebied van 31.940 ha en heeft de geografische coördinaten 40°12\'11.84\" North, 8°24\'37.15\" West. Vanwege de nieuwe administratieve reorganisatie is deze gemeente opgedeeld in 18 delen, wat meestal stedelijke gebieden zijn (Afbeelding 1).

<figure>
<img src="../images/portugal_coimbra1.png" class="align-left" alt="portugal_coimbra1.png" />
<figcaption>Geografische locatie van de gemeente Coimbra.</figcaption>
</figure>

Het karakteriseren van het landschap werd uitgevoerd met behulp van kwantitatieve indices, ontworpen door metrische gegevens van het landschap. Deze indices werden toen gebruikt om de structurele karakteristieken van het landschap, de wijziging te documenteren en hun relatie met de aanwezigheid van verscheidene soorten of groepen van soorten te beschrijven (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). Het aantal metrische gegevens is extreem groot en kan worden berekend op het niveau van landschap, klasse en vlek (Turner et al, 2001;. Fidalgo et al, 2009.). Metrische gegevens kunnen worden berekend met behulp van Corine Land Cover, Land use (COS 90 en COS2006) of kaarten van landgebruik geproduceerd door ons. Volgens Martin Jung (2012), is de Landscape Ecology Stistics (Lecos) een module van QGIS die wordt gebruikt in metrische gegevens van landschappen te berekenen in rasterlagen. Het resultaat kan beschikbaar worden gesteld in de indeling CSV.
## Methoden
Metrische gegevens van het landschap werden berekend met behulp van de Corine Land Cover (CLC) over de jaren 1990 en 2006. Voor dit deel was het noodzakelijk om het grondgebruik te transformeren naar rasterindeling met een celgrootte van 50x50 meter. We gebruikten het gereedschap r.to.raster van de module GRASS GIS die aanwezig was in de Toolbox van Processing en het gebruikte niveau van de classificatie in CLC is het eerste. Na het transformeren berekenden we de metrische gegevens in de plug-in Landscape Ecology (LecoS) met behulp van Grafische modellen maken (Afbeelding 2).

<figure>
<img src="../images/portugal_coimbra3.png" class="align-left" alt="portugal_coimbra3.png" />
<figcaption>Metrische gegevens landschap, berekend over verschillende jaren (1990 en 2006).</figcaption>
</figure>

We berekenden het gebruik van het land, proportie van het landschap, dichtheid van randen, aantal gronddelen, grootste gebied gronddeel, kleinste gebied gronddeel , gemiddelde afstand tussen gronddelen en de effectieve grootte van de mazen (Tabel 1). Metingen van de diversiteit van het landschap werden berekend met de Shannon-index, Uniformiteit en de Simpson-index.
## Resultaten
Uit analyses van de berekende metrische gegevens van het landschap werd bekend dat er een verhoging was van de mate van menselijke verstoring en daarom een grotere fragmentatie van gebruik tussen 1990 en 2006. Het aantal gronddelen van "Forest Semi Natural gebieden" en "Agricultural gebieden" verminderde tussen 1990 en 2006 (Tabel 1). Deze metrische gegevens kunnen ons enige indicatie geven over ecologische processen die relaties tussen bevolking en woonomgeving doen verkleinen of vergroten (Viana and Aranha, 2008). Ook opmerkelijk is de gemiddelde afstand tussen de landdelen, een meting die ons in staat stelt de mate van defragmentatie van het landschap te begrijpen, de afname van de "Forest and Semi Natural"-gebieden 1990 tot en met 2006 ten koste van de vergrote "Artificial"-gebieden (Tabel 1).

<figure>
<img src="../images/portugal_coimbra2.png" class="align-left" alt="portugal_coimbra2.png" />
<figcaption>Model om metrische gegevens van het landschap te berekenen in 1990.</figcaption>
</figure>

Van 1990 tot en met 2006 nam de diversiteit toe. Het is echter bekend dat dat resultaat direct is gerelateerd aan de transfer in het landgebruik, in het bijzonder het verlies van "Agricultural"-gebieden en "Forest and Semi Natural"-gebieden. Hetzelfde gebeurde met uniformiteit.
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
