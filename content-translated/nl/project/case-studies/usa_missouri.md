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
  <span>1 februari 2013</span>
</p>

Het Missouri Herpetological Atlas Project (MOHAP) werd geïnitieerd in 1997 als resultaat van de wens te komen tot een eenvoudig bij te werken kaart van de verdeling van amfibieën en reptielen voor Missouri (Verenigde Staten van Amerika). Een database werd opgezet om alle geldige locaties op te kunnen slaan, inclusief records die werden gepubliceerd in historische literatuurbronnen en specimens die gewaarmerkt werden verkregen vanuit musea. Vanuit de database kan een reeks kaarten worden geproduceerd die zowel de records voor plaats als ook de \"county records\" voor elke soort weergeven.

MOHAP host een website op <http://atlas.moherp.org/> die het project in detail beschrijft en een variëteit aan statische kaarten weergeeft, alle geproduceerd door QGIS.  Een atlas, gepubliceerd als een te downloaden pdf, wordt periodiek uitgegeven als een gratis publicatie in de geest van open toegang tot wetenschappelijk onderzoek (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Gepubliceerde kaarten worden gebruikt door veldbiologen, landbeheerders en anderen om de verdeling van de soorten in Missouri beter te begrijpen.

Vanaf februari 2013 bevat de database van MOHAP  31.495 items die de soorten weergeven die die worden bewaard in 34 museumcollecties en zijn vermeld in 32 historische literatuurbronnen; 5118 gedocumenteerde county records; 6884 unieke plaatsen; en 12.866 unieke combinaties van soorten / plaatsen. De herpetofauna van de staat bestaat uit 113 soorten.
## Statische kaarten genereren en exporteren 
Het proces van het maken van kaarten met QGIS begint met de gegevens die zijn opgeslagen in verschillende tabellen van PostgreSQL, ruimtelijk te gebruiken door middel van PostGIS. Omdat kaarten statisch zijn en uiteindelijk bedoeld voor ofwel het web of een afgedrukte atlas, worden zij voor elke soort automatisch gegenereerd door middle van een aangepaste Python-plug-in voor QGIS  (Figures 1,2).

<figure>
<img src="../images/usa_missouri1.png" class="align-right" alt="usa_missouri1.png" />
<figcaption>Aangepaste kaart maken en gebruikersinterface exporteren, kaarten worden gemaakt en geëxporteerd in een batchproces.</figcaption>
</figure>

De uiteindelijke kaarten voor de soorten hebben een helder en professioneel uiterlijk (Afbeelding 3). Een serie basiskaarten wordt ook gemaakt en gelabeld om de verdeling van de soorten beter te begrijpen (Afbeelding 4). Vanwege de manier waarop de kaartstijlen worden bekeerd binnen elke gegevenslaag, kunnen de lagen van de basiskaart ook met weinig inspanning worden verwerkt in een set van kaarten van soorten.

<figure>
<img src="../images/usa_missouri2.png" class="align-right" alt="usa_missouri2.png" />
<figcaption>Kaarten worden weergegeven als statische afbeeldingen.</figcaption>
</figure>

<figure>
<img src="../images/usa_missouri3.png" class="align-right" alt="usa_missouri3.png" />
<figcaption>Kaart met gelabelde Level III Ecoregion voor Missouri en omliggende staten.</figcaption>
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

Dit artikel werd bijgedragen door Brian Edmond in februari 2013. Hij is een Senior Systems Analyst in Computer Services aan de Missouri State University. Hij heeft een BS in Wildlife Biology van de University of Missouri en ontwikkelde zijn carrière in de samengevoegde zone tussen biologie en technologie.

{{<content-end >}}
