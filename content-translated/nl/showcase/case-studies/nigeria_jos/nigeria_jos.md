---
draft: 'true'

---
# In kaart brengen met QGIS van woonomgeving en vogelsoorten in het Amurum bosreservaat in Nigeria
Het bosreservaat Amurum is gelegen nabij de stad Jos, Plateau state, Nigeria. Het werd ingesteld in samenwerking met het initiatief van de A.P. Leventis Ornithological Research Institute (APLORI) met als doel natuurbehoud, onderwijs en onderzoek. APLORI wordt gehost door het Departement van Zoölogie aan de Universiteit van Jos. Jaarlijks krijgt een groep van ongeveer acht gemotiveerde studenten vanuit geheel Nigeria een training in behoud van biologie, statistieken (met R) en vanaf 2011 ook GIS. Gedurende twee weken in december 2011 bestudeerden we de basisconcepten van GIS en pasten die met behulp van QGIS toe op verscheidene doelen voor natuurbehoud. In dit artikel beschrijven we de manier waarop we QGIS gebruikten om de woonomgevingen en de bepalingen daarvoor van het reservaat Amurum en hoe de basiskaarten van de woonomgevingen werden gebruikt om gebieden te verkrijgen teneinde efficiënt de ruimtelijke verdeling van de vogelsoorten te bepalen, inclusief de biodiversiteit.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## In kaart brengen van hoogten. schaduwen voor heuvels, hellingen en woonomgevingen
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) De GdalTools werden gebruikt om originele gegevenssets samen te voegen en een kleiner gebied te clippen dat het reservaat bevatte zodat de raster gegevenssets relatief klein bleven. Door middel van GPS verzamelden we hoogten op verscheidene locaties in het reservaat.
3) Over het algemeen kwamen de hoogten van de gegevenssets van SRTM goed overeen met de middels GPS verzamelde hoogten. Terreinmodellen in GDAL Tools werden gebruikt om schaduwen voor heuvels en hellingen voor het gebied te berekenen. Deze variabelen zijn belangrijk vanuit een ecologisch oogpunt omdat zij sterk zijn verbonden met het type woonomgeving.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) Omdat we van plan waren een goed uitziende kaart te ontwikkelen, interpoleerden we de originele (geclipte) hoogtekaart om een kaart met hogere resolutie te verkrijgen. We gebruikten het gereedschap Warp in GDAL Tools. Door middel van het gereedschap Contour verkregen we meer vloeiende contourlijnen.
5) Coördinaten van de grenzen van het reservaat werden verkregen door langs de grenzen van het reservaat te lopen met een GPS. De waypoints en sporen die werden opgeslagen in de GPS werden gladjes geïmporteerd met behulp  van de GPS Tools. De geïmporteerde waypoints en sporen werden gebruikt om een polygoon shapefile te construeren. De sporen binnen het reservaat werden op een soortgelijke manier in kaart gebracht.
6) We waren in staat snel en precies een kaart van de woonomgevingen in Amurum te construeren met behulp van een Google satellietafbeelding die we in de werkruimte kregen ,met behulp van de plug-in Openlayers. Het reservaat heeft drie te onderscheiden typen woonomgeving: Savanne, bos in galerij-vorm en Rotsachtig buitengebied. Op basis van de satellietafbeelding gebruikten we de editor om markeringen te tekenen die de drie woonomgevingen markeerden. Het juist instellen van de opties voor snappen maakte het mogelijk niet overlappende polygonen te maken.

## In kaart brengen van de verdeling en diversiteit van vogels
De kaarten van de woonomgeving werden gebruikt om willekeurige locaties te maken. De gebieden van de verscheidene typen woonomgeving werden gebruikt om een aantal proportionele locaties, ten opzichte van het oppervalk van elk type woonomgeving te genereren (stratificatie).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Conclusie
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Auteurs
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
