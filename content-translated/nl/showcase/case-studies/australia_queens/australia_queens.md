---
draft: 'true'

---
# QGIS en GRASS voor het in kaart brengen van het gevaar voor bosbranden voor de lokale overheid
## Introductie
De Southern Downs Regional Council (SDRC) is een kleine tot middelgrote lokale overheid in zuidoost Queensland, Australië. Het gebied van die overheid, met name het zuidelijke gedeelte, leidt onder grote bosbranden. Bosbranden zijn een echt en aanwezig probleem voor de inwoners en landeigenaren in de Southern Downs Region, en hebben geresulteerd in het verlies van levens en eigendommen.

Dit project zal de overheid en de mensen in de regio in staat stellen zich meer bewust te worden van de risico's en het mogelijk te maken beter beslissingen te nemen in de toekomst.

![](./images/australia_queens1.jpg){.align-right}
## Het project
Een bosbrand is niet alleen een probleem voor SDRC maar ook voor geheel Queensland. De landelijke overheid vereist dat elke lokale overheid het gebied voor gevaar van bosbranden in hun gebied identificeert door middel van de State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. Dit soort werk zou normaal gesproken worden uitgevoerd met behulp van adviseurs, maar werd in plaats daarvan uitgevoerd door de lokale overheid zelf met behulp van een combinatie van QGIS en GRASS.

De GIS-kant van het project werd opgedeeld in 6 belangrijke stappen
- Beoordelen van hellingen en in kaart brengen daarvan
- Beoordelen van aspect en in kaart brengen daarvan
- Beoordelen van vegetatie en in kaart brengen daarvan
- Combineren van de scores om de mate van het gevaar voor bosbranden te identificeren
- Verificatie en kwalitatieve beoordeling in het veld
- Uiteindelijke kaarten

## Het gebruik van QGIS en GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, met behulp van de plug-in GRASS, werd geselecteerd omdat het de gereedschappen verschafte die de voltooiing van het werk vereiste en de interactie tussen QGIS en GRASS maakte het eenvoudig de rasterafbeeldingen te verwerken en ze op een betekenisvolle manier aan de gebruikers weer te geven. SDRC gebruikt MapInfo voor zijn belangrijkste GIS-systeem, maar de add-ons voor MapInfo waren niet zo krachtig als GRASS GIS voor het verwerken van de rasters.

De plug-in QGIS GRASS werd gebruikt om 5 meter contouren van de gehele regio in GRASS te importeren die dan werden geconverteerd naar een contouren rasterkaart met behulp van r.surf.contour. Een helling- en aspectkaart werden daarna gegenereerd met behulp van r.slope.aspect vanuit de raster contourenkaart. Categorieën werden toegewezen aan de verschillende bereiken hellingen en aspecten en een score voor het gevaarrisico meegegeven. Gebieden met vegetatie werden ook verschillende scores voor gevaarrisico gegeven. Alle resulterende rasterkaarten werden daarna gecombineerd met behulp van mapcalc en een uiteindelijke score voor gevaarrisico gegeven. De risicoscores werden daarna verdeeld in drie hoofdcategorieën: hoog; medium; en laag.

Het laatste deel van het proces was verificatie in het veld door de plaatselijke brandweer. Na het proces van reviewen, werd QGIS gebruikt om de uiteindelijke kaarten voor de presentatie af te drukken.

Omdat alle opdrachten voor GRASS kunnen worden uitgevoerd vanaf de opdrachtregel, werden alle opdrachten, die nodig waren om de kaarten voor het gevaar van bosbranden te generen, opgenomen, voor documentatie-doeleinden en voor het geval dat op enig moment in de toekomst de kaarten opnieuw zouden moeten worden gegenereerd.
## Conclusie
Algemeen verschafte QGIS, samen met de plug-in GRASS, een fantastische ervaring en een fantastische uitkomst voor de lokale overheid in het maken van hun eigen kaarten voor het gevaar van bosbranden. De plug-in GRASS verschafte een zeer eenvoudige te gebruiken interface naar GRASS via QGIS. Omdat QGIS in staat is de rasterindeling voor GRASS zelf te openen, is integratie naadloos en kunnen eenvoudig kaarten gemaakt worden.

Het project won een aanmoedigingsprijs bij de Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Verwijzingen
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Auteur
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

Dit artikel werd bijgedragen in januari 2011 door Nathan Woodrow. Nathan is een GIS-officer bij de Southern Downs Regional Council en studeert voor een associates degree in Spatial Science aan de University of Souther Queensland
