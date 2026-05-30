---
draft: 'true'

---
# In kaart brengen met QGIS van woonomgeving en vogelsoorten in het Amurum bosreservaat in Nigeria
Het bosreservaat Amurum is gelegen nabij de stad Jos, Plateau state, Nigeria. Het werd ingesteld in samenwerking met het initiatief van de A.P. Leventis Ornithological Research Institute (APLORI) met als doel natuurbehoud, onderwijs en onderzoek. APLORI wordt gehost door het Departement van Zoölogie aan de Universiteit van Jos. Jaarlijks krijgt een groep van ongeveer acht gemotiveerde studenten vanuit geheel Nigeria een training in behoud van biologie, statistieken (met R) en vanaf 2011 ook GIS. Gedurende twee weken in december 2011 bestudeerden we de basisconcepten van GIS en pasten die met behulp van QGIS toe op verscheidene doelen voor natuurbehoud. In dit artikel beschrijven we de manier waarop we QGIS gebruikten om de woonomgevingen en de bepalingen daarvoor van het reservaat Amurum en hoe de basiskaarten van de woonomgevingen werden gebruikt om gebieden te verkrijgen teneinde efficiënt de ruimtelijke verdeling van de vogelsoorten te bepalen, inclusief de biodiversiteit.

![Trainingsgroep](./images/nigeria_jos1.jpg){.align-right}
## In kaart brengen van hoogten. schaduwen voor heuvels, hellingen en woonomgevingen
1) In kaart brengen hoogten en veredelen bodem: We downloaden (gratis) hoogtegegevens van de NASA Shuttle Radar Topographic Mission (SRTM) voor het gebied waar Amurum is gelegen. (Informatie over de globale set met hoogtegegevens kan hier worden gevonden: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) De GdalTools werden gebruikt om originele gegevenssets samen te voegen en een kleiner gebied te clippen dat het reservaat bevatte zodat de raster gegevenssets relatief klein bleven. Door middel van GPS verzamelden we hoogten op verscheidene locaties in het reservaat.
3) Over het algemeen kwamen de hoogten van de gegevenssets van SRTM goed overeen met de middels GPS verzamelde hoogten. Terreinmodellen in GDAL Tools werden gebruikt om schaduwen voor heuvels en hellingen voor het gebied te berekenen. Deze variabelen zijn belangrijk vanuit een ecologisch oogpunt omdat zij sterk zijn verbonden met het type woonomgeving.

![QGIS schermafdruk](./images/nigeria_jos2.jpg){.align-right}
4) Omdat we van plan waren een goed uitziende kaart te ontwikkelen, interpoleerden we de originele (geclipte) hoogtekaart om een kaart met hogere resolutie te verkrijgen. We gebruikten het gereedschap Warp in GDAL Tools. Door middel van het gereedschap Contour verkregen we meer vloeiende contourlijnen.
5) Coördinaten van de grenzen van het reservaat werden verkregen door langs de grenzen van het reservaat te lopen met een GPS. De waypoints en sporen die werden opgeslagen in de GPS werden gladjes geïmporteerd met behulp  van de GPS Tools. De geïmporteerde waypoints en sporen werden gebruikt om een polygoon shapefile te construeren. De sporen binnen het reservaat werden op een soortgelijke manier in kaart gebracht.
6) We waren in staat snel en precies een kaart van de woonomgevingen in Amurum te construeren met behulp van een Google satellietafbeelding die we in de werkruimte kregen ,met behulp van de plug-in Openlayers. Het reservaat heeft drie te onderscheiden typen woonomgeving: Savanne, bos in galerij-vorm en Rotsachtig buitengebied. Op basis van de satellietafbeelding gebruikten we de editor om markeringen te tekenen die de drie woonomgevingen markeerden. Het juist instellen van de opties voor snappen maakte het mogelijk niet overlappende polygonen te maken.

## In kaart brengen van de verdeling en diversiteit van vogels
De kaarten van de woonomgeving werden gebruikt om willekeurige locaties te maken. De gebieden van de verscheidene typen woonomgeving werden gebruikt om een aantal proportionele locaties, ten opzichte van het oppervalk van elk type woonomgeving te genereren (stratificatie).

![Trainingsgroep](./images/nigeria_jos3.jpg){.align-right}

De willekeurige punten in fTools werden voor dit doel gebruikt. Alle locaties werden gedurende twee ochtenden bezocht door vier groepen studenten (2 per groep), wat een totaal opleverde van 38 willekeurige locaties, verspreid door het reservaat. De gegevens van de observaties werden ingevoerd in een werkblad en geanalyseerd met behulp van R. In aanvulling daarop werd de Shannon-Wiener-diversiteitsindex berekend met behulp van R. Na het samenvoegen van het bestand met locaties en de resulterende gegevens van de observaties werd het als een CSV-bestand geëxporteerd, wat werd geladen in QGIS met behulp van het gereedschap "Tekengescheiden tekstlaag toevoegen". Op basis van de hierboven vermelde lagen werd een kaart geconstrueerd die sommige van de belangrijkste objecten in het landschap en de diversiteit van vogels in het reservaat Amurum weergaf.
## Conclusie
Over het algemeen was de cursus een groot succes. Wij - een groep studenten zonder eerdere ervaring met GIS  —— genoten heel veel van het werken met QGIS. Binnen slechts twee weken waren we in staat een uiterst nuttige kaart van het reservaat te ontwikkelen. Naast andere dingen werden bereiken van de verscheidene woonomgevingen bepaald, wat stratificatie mogelijk maakte en dus konden betere schattingen worden gemaakt van de overvloed aan verschillende soorten organismen. In principe zijn we nu in staat om beter ecologisch onderzoek uit te voeren met behulp van QGIS als een open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Auteurs
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
