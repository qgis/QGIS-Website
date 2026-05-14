---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/usa_missouri1.png
title: QGIS-kaarten Historische herpetofaunal records (in Missouri, USA)
type: case-study

---
{{<content-start >}}
# QGIS-kaarten Historische herpetofaunal records (in Missouri, USA)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Statische kaarten genereren en exporteren 
Het proces van het maken van kaarten met QGIS begint met de gegevens die zijn opgeslagen in verschillende tabellen van PostgreSQL, ruimtelijk te gebruiken door middel van PostGIS. Omdat kaarten statisch zijn en uiteindelijk bedoeld voor ofwel het web of een afgedrukte atlas, worden zij voor elke soort automatisch gegenereerd door middle van een aangepaste Python-plug-in voor QGIS  (Figures 1,2).

<figure>
<img src="../images/usa_missouri1.png" class="align-right" alt="usa_missouri1.png" />
<figcaption>Custom map generation and export user interface, maps are generated and exported in a batch process.</figcaption>
</figure>

The final species maps have a clean and professional appearance (Figure 3). To better understand species\' distributions, a series of base maps are also created and labelled (Figure 4). Because of the way styles are managed within each data layer, the base map layers can also be incorporated into a set of species maps with little extra effort.

<figure>
<img src="../images/usa_missouri2.png" class="align-right" alt="usa_missouri2.png" />
<figcaption>Maps are displayed as static images.</figcaption>
</figure>

<figure>
<img src="../images/usa_missouri3.png" class="align-right" alt="usa_missouri3.png" />
<figcaption>Labelled Level III Ecoregion map for Missouri and surrounding states.</figcaption>
</figure>

## Conclusies
In het begin van het project MOHAP werden verschillende commerciële en zakelijke gereedschappen gebruikt om gegevens op te slaan en te verwerken en kaarten voor publicatie te maken. Vanaf 2007 proberen we alle aspecten van het project te verplaatsen naar open source software. QGIS, naast PHP, PostgreSQL, PostGIS, Python, en ReportLab, vormen de open source spil naar MOHAP, wat het project en alle gegevens effectief in staat stelt om te bestaan zonder de beperkingen van commerciële software.

QGIS bevat eigen ondersteuning voor PostGIS en een architectuur voor plug-ins in Python, die essentieel bleken te zijn voor het maken het geautomatiseerde kaarten en het exporteren daarvan. De uitgebreide documentatie van de API werd gebruikt, naast het kookboek voor het ontwikkelen van plug-ins om exact dat te maken wat we nodig hadden voor het automatiseren. De ondersteuning van de gemeenschap was ook zeer goed en bevat ook een enorme berg aan gedeelde gebouwde plug-ins die klaar zijn om te gebruiken.

Hoewel we QGIS op een kleine en specifieke manier gebruiken, zijn zijn mogelijkheden en uitbreidingen met behulp van Python meer dna voldoende om grotere en meer complexe projecten te tackelen.
## Auteur
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
