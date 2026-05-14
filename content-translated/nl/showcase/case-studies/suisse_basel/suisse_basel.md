---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Hoe QGIS werd gebruikt
Binnen het gehele proces van het plannen werd QGIS gebruikt voor de volgende vier taken:
- Importeren van bestaande gegevens. De gegevens bevatten kaarten met geo-verwezen achtergrondafbeeldingen (\*.tif) naast polygoon, lijn en punt shapefiles. Voor de bosbeheerder is de visualisatie van bestaande thematische gegevens (bijvoorbeeld grond- en drinkwaterbronnen, zones van natuurbescherming) belangrijk voor zijn dagelijkse werk.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Analyses. De gebieden van de verschillende categorieën van metingen zijn berekend. Beginnend vanuit bepaalde lijnobjecten, zoals treinsporen of wegen, werden overeenkomende bossen bepaald met behulp van een buffer.
- Afdrukken en exporteren. De Printvormgeving ondersteunde het maken van de lay-out voor de kaarten. De kaart werd geëxporteerd als PDF en afbeeldingsbestanden.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## Conclusie
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Perspectief
De brontaak van een concept voor het plannen van bossen kan worden uitgewerkt met de genoemde basis gereedschappen voor GIS. Guaraci zal QGIS blijven gebruiken voor het plannen van bossen op het niveau van de boseigenaar. Gebaseerd op de ervaringen van het gepresenteerde project, kan QGIS ook worden aanbevolen voor concepten voor bosbouw op het niveau van lokale autoriteiten. Grotere en meer complexe projecten met vereisten voor gedetailleerde analyses zouden kunnen worden afgehandeld door de combinatie van QGIS met de ruimtelijke database server van Postgis. Nieuwe zones voor kappen als ook bosreservaten en beschermingszones kunnen eenvoudig worden gedigitaliseerd. Hopelijk zullen boseigenaren en beheerders in toenemende mate het potentieel van QGIS gebruiken, ook voor hun jaarlijkse planning als ook voor het documenteren van hun activiteiten met betrekking tot het bos.
## Auteur
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
