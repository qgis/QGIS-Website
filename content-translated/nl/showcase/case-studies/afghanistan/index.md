---
author: Edward Crowther
categories:
- Praktijkvoorbeelden
date: '2015-04-01'
description: The Danish Demining Group (DDG), the specialised mine action unit of
  the Danish Refugee Council, has been working in Afghanistan since 1999, undertaking
  humanitarian mineclearance, unexploded ordnance (UXO) disposal and mine risk education.
draft: 'true'
heroImage: ''
tags:
- humanitarian
- afghanistan
- case-study
- showcase
thumbnail: afghanistan3.jpg
title: Deense Demining Group gebruikt QGIS in Afghanistan
type: showcase/case-studies

---
{{<content-start classes="notification is-light" >}}

De Deense Demining Group (DDG), de gespecialiseerde  mijnopruimingseenheid van de Danish Refugee Council, werkt sinds 1999 in Afghanistan,  verricht humanitaire opruiming van mijnen, verwijderen van niet-geëxplodeerde objecten (unexploded ordnance (UXO)) en educatie over de risico's van mijnen. DDG Afghanistan levert humanitaire mijnopruimingsacties om levens te redden, het verhogen van het veiligheidsgevoel door educatie over de risico's en helpt bij het verwijderen van obstakels voor productief gebruik van bronnen, hetgeen helpt om het ontwikkelingspotentieel van Afghanistan te realiseren. Sinds de start van de operaties in Afghanistan heeft DDG meer dan 24.000 landmijnen verwijderd en meer dan 940.000 stukken UXO. Momenteel werkt DDG in de noordelijke provincies Balkh en Samangan, en de centrale provincies Kabul, Parwan en Panjshir.

In Afghanistan worden activiteiten voor mijnopruiming gecoördineerd door de Mine Action Coordination Centre for Afghanistan (MACCA), die georuimtelijke informatie van bekende gevaren (mijnenvelden, slagvelden, ‘spotten’ UXO-taken) verzamelen en ontleden, en deze informatie bijwerkt als het opruimen voortgaat. Nieuwe shapefiles van deze ‘gevaars-polygonen’ worden op een regelmatige basis uitgegeven door MACCA, en organisaties voor het opruimen van mijnen kunnen deze gebruiken om de situatie voor het opruimen van mijnen in hun werkgebieden in te schatten. DDG volgt het gebruik van QGIS binnen de organisatie om de dure commerciële software, die het vroeger gebruikte, te vervangen.

![Digitale hoogtemodellen stellen DDG in staat een idee te krijgen van de locatie van een mijnenveld.](afghanistan1.png)

The use of geospatial data is most useful in the planning and survey phases. In Afghanistan, security problems and rugged terrain mean that physical re-survey of known sites is not always easy. Instead, the use of a mixture of data satellite or aerial photography underlays, digitized Soviet-era topographic maps, hazard shapefiles and digital elevation models allow DDG to get an idea of the location of a minefield in relation to the terrain and surrounding natural and physical features before sending in a survey team. QGIS plugins add useful capabilities, like the ability to visualise terrain in 3D. The attached screenshot above made using the plugin Qgis2threejs shows an area just south of the Darulaman Palace in Kabul, with active minefields (along the ridgelines on the left) shown in red over a Soviet topographic raster layer combined with SRTM data. Minefields already cleared show as light green.

![Active hazardous areas shown in red. Hazardous areas already cleared show as light green.](afghanistan2.jpg)

Kabul University's campus is still contaminated with suspected hazardous areas thought to comprise of air-dropped bombs or similar ordnance. While not posing any immediate threat to students or staff, these hazards will require eventual clearance to allow future construction within an educational institution vital to Afghanistan's future development. The hazards are also notable as among the last significant remaining hazardous areas in the Kabul metropolitan area. By using QGIS to combine the hazard polygons from earlier surveys with highly accurate aerial photography provided by the USGS, discrepancies can be noted e.g. where the polygons do not match the shape of the buildings, as evident in the northwest part of the campus which can direct survey teams to places to first conduct a more accurate re-survey.

QGIS synchroniseert ook goed met gegevens die zijn verzameld tijdens veldbezoeken met behulp van draagbare Garmin GPS, wat het mogelijk maakt kaarten te maken met de locaties van mijnen die zijn gevonden en vernietigd.

Het gebruik van QGIS, naast een vernieuwde interesse in gegevensanalyse, heeft het op nieuwe manieren kijken naar beschikbare gegevens in een stroomversnelling gebracht, en, door het te combineren met andere gegevensbronnen, de activiteiten voor het opruimen van mijnen beter te plannen. Het zorgt ook voor verbetering van de bekwaamheden bij het maken van kaarten binnen de organisatie, en een mogelijkheid om de impact van hun werk beter te communiceren met internationale donoren. In een deel van de wereld waar ‘formele’ training in GIS moeilijk is te verkrijgen, wordt de collectieve natuur van samenwerken binnen de gebruikersgemeenschap van QGIS enorm gewaardeerd, omdat technische problemen vaak kunnen worden opgelost door online forums te raadplegen. In het kort: QGIS speelt een rol in het werken naar het verwijderen van landmijnen en UXO in Afghanistan.
## Koppeling
- Danish Demining Group <http://www.danishdemininggroup.dk/>

## Auteur
![Edward Crowther](afghanistan3.jpg)

Edward Crowther is Deputy Country Director bij de Deense Demining Group Afghanistan. Voorafgaand aan het werken bij DDG in Afghanistan, werkte Edward met het humanitaire agentschap voor het verwijderen van landmijnen. De HALO Trust in Angola en Sri Lanka. Hij heeft een MSc in Development Studies van de University of London’s School of Oriental and African Studies.

{{<content-end >}}
