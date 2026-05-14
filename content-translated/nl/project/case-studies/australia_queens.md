---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS en GRASS voor het in kaart brengen van het gevaar voor bosbranden voor
  de lokale overheid
type: case-study

---
{{<content-start >}}
# QGIS en GRASS voor het in kaart brengen van het gevaar voor bosbranden voor de lokale overheid
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Introductie
De Southern Downs Regional Council (SDRC) is een kleine tot middelgrote lokale overheid in zuidoost Queensland, Australië. Het gebied van die overheid, met name het zuidelijke gedeelte, leidt onder grote bosbranden. Bosbranden zijn een echt en aanwezig probleem voor de inwoners en landeigenaren in de Southern Downs Region, en hebben geresulteerd in het verlies van levens en eigendommen.

Dit project zal de overheid en de mensen in de regio in staat stellen zich meer bewust te worden van de risico's en het mogelijk te maken beter beslissingen te nemen in de toekomst.

![](../images/australia_queens1.jpg)
## Het project
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

De GIS-kant van het project werd opgedeeld in 6 belangrijke stappen
- Beoordelen van hellingen en in kaart brengen daarvan
- Beoordelen van aspect en in kaart brengen daarvan
- Beoordelen van vegetatie en in kaart brengen daarvan
- Combineren van de scores om de mate van het gevaar voor bosbranden te identificeren
- Verificatie en kwalitatieve beoordeling in het veld
- Uiteindelijke kaarten

## Het gebruik van QGIS en GRASS
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

De plug-in QGIS GRASS werd gebruikt om 5 meter contouren van de gehele regio in GRASS te importeren die dan werden geconverteerd naar een contouren rasterkaart met behulp van r.surf.contour. Een helling- en aspectkaart werden daarna gegenereerd met behulp van r.slope.aspect vanuit de raster contourenkaart. Categorieën werden toegewezen aan de verschillende bereiken hellingen en aspecten en een score voor het gevaarrisico meegegeven. Gebieden met vegetatie werden ook verschillende scores voor gevaarrisico gegeven. Alle resulterende rasterkaarten werden daarna gecombineerd met behulp van mapcalc en een uiteindelijke score voor gevaarrisico gegeven. De risicoscores werden daarna verdeeld in drie hoofdcategorieën: hoog; medium; en laag.

Het laatste deel van het proces was verificatie in het veld door de plaatselijke brandweer. Na het proces van reviewen, werd QGIS gebruikt om de uiteindelijke kaarten voor de presentatie af te drukken.

Omdat alle opdrachten voor GRASS kunnen worden uitgevoerd vanaf de opdrachtregel, werden alle opdrachten, die nodig waren om de kaarten voor het gevaar van bosbranden te generen, opgenomen, voor documentatie-doeleinden en voor het geval dat op enig moment in de toekomst de kaarten opnieuw zouden moeten worden gegenereerd.
## Conclusie
Algemeen verschafte QGIS, samen met de plug-in GRASS, een fantastische ervaring en een fantastische uitkomst voor de lokale overheid in het maken van hun eigen kaarten voor het gevaar van bosbranden. De plug-in GRASS verschafte een zeer eenvoudige te gebruiken interface naar GRASS via QGIS. Omdat QGIS in staat is de rasterindeling voor GRASS zelf te openen, is integratie naadloos en kunnen eenvoudig kaarten gemaakt worden.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Verwijzingen
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Auteur
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Dit artikel werd bijgedragen in januari 2011 door Nathan Woodrow. Nathan is een GIS-officer bij de Southern Downs Regional Council en studeert voor een associates degree in Spatial Science aan de University of Souther Queensland

{{<content-end >}}
