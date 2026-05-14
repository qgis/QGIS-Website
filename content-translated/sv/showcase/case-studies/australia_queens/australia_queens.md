---
draft: 'true'

---
# QGIS och GRASS för riskkartläggning av skogsbränder i kommuner
## Introduktion
Regionfullmäktige i Southern Downs (SDRC) är ledningen till en liten till medelstor kommun i sydöstra Queensland i Australien. Kommunen, främst den södra delen, är hårt drabbat av skogsbränder. Skogsbränder innebär en påtaglig oro för invånare och markägare i regionen Southern Downs och har resulterat i förlorade människoliv och egendom.

Projektet hjälper fullmäktige och invånarna att vara mer förberedda på riskerna och låter dom fatta bättre beslut för framtiden.

![](./images/australia_queens1.jpg){.align-right}
## Projektet
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

GIS-delen av projektet var uppdelad i 6 steg
- Kartläggning och bedömning av lutningar
- Kartläggning och bedömning av läget
- Kartläggning och bedömning av vegetation
- Kombinera poäng för att identifiera allvarlig risk för skogsbrand
- Fältverifiering och kvalitativ bedömning
- Slutliga kartor

## Användningen av QGIS och GRASS
![](./images/australia_queens2.jpg){.align-right}

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

I QGIS användes insticksprogrammet för GRASS för att importera in 5 meters nivåkurvor över hela regionen som därefter konverterades till rasterkartor med hjälp av r.surf.contour. En lutnings- och synvinkelskarta skapades med r.slope.aspect utifrån rasterkartan med nivåkurvor. Kategorier tilldelades olika lutningsvinklar och synvinklar utifrån en riskbedömning. Beväxta ytor tilldelades också olika riskbedömningar. Alla rasterkartor kombinerades sedan med hjälp av mapcalc och fick en slutlig bedömning av risknivåerna. Risknivåerna delades sedan in i tre kategorier: hög; medel; och låg.

Den sista delen i processen var fältverifiering via den lokala brandorganisationen. Efter en genomgång så användes QGIS till att skriva ut de slutliga kartorna för presentation.

Eftersom alla GRASS-kommandon körs från kommandoraden så så spelades alla kommandona in för dokumentationsändamål och för att kartorna ska kunna återskapas i framtiden.
## Slutsats
QGIS, tillsammans med GRASS-insticksprogrammet, erbjöd ett bra stöd och ett gott resultat för myndighetens riskbedömning av skogsbränder. Insticksprogrammet för GRASS erbjuder ett enkelt sätt använda GRASS genom QGIS. Eftersom QGIS enkelt kan öppna GRASS rasterformat så är integrationen sömlös och kartproduktionen enkel.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referenser
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Skapare
![Nathan Woodrow](./images/australia_queensaut.jpg){.align-left height="200px"}

Denna artikel skrevs i januari 2011 av Nathan Woodrow. Nathan är en GIS-tjänsteman vid regionfullmäktige i Södra Downs och studerar till docent i Rumslig Vetenskap vid University of Southern Queensland.
