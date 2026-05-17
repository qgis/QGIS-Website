---
HasBanner: false
archived: true
date: 2012-06-30
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/africa_tiger1.jpg
title: 'Water Observatie en Informatie Systemen: Inschakelen van het gebruiken van
  Earth Observation Data voor geïntegreerd beheer van waterbronnen in Afrika'
type: case-study

---
{{<content-start >}}
# Water Observatie en Informatie Systemen: Inschakelen van het gebruiken van Earth Observation Data voor geïntegreerd beheer van waterbronnen in Afrika
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>30 juni 2012</span>
</p>

Het Water Observation and Information System (WOIS) is een gereedschap van open source software voor het monitoren, beoordelen en inventariseren van waterbronnen op een kosteneffectieve manier met behulp van gegevens van Earth Observation (EO). Het WOIS is ontwikkeld onder het project TIGER-NET, wat een belangrijke component is van het initiatief TIGER van het European Space Agency (ESA) en waarvan het belangrijkste doel is om de capaciteit van de Afrikaanse Earth observation voor het monitoren van waterbronnen te ondersteunen. TIGER-NET heeft tot doel de op satelliet gebaseerde beoordeling en het monitoren van waterbronnen te ondersteunen, van waterberging tot grensoverschrijdende niveaus van bassins door middel van het verschaffen van een gratis en krachtig softwarepakket, met geassocieerde capaciteitsopbouw, aan Afrikaanse  autoriteiten.
## Omschrijving
Het WOIS kan worden gezien als een systeem voor meerdere doelen, bestaande uit een ruimtelijke  database, faciliteiten voor het uitnemen en verwerken van gegevens van EO, en geïntegreerde gereedschappen en modellen die geacht worden ondersteuning te bieden bij het nemen van beslissingen, bijv.. hydrologische modellen maken en in GIS ingebedde gereedschappen voor visualisatie en analyses. Het WOIS is ontworpen rondom QGIS, wat optreedt als de Graphical-User-Interface (GUI) aan de voorzijde.  QGIS werd gekozen als het centrale platform voor integratie, vanwege zijn heldere en toegankelijke GUI, een sterke gemeenschap van ontwikkelaars, het gemakkelijk kunnen implementeren van aanvullende functionaliteiten door middel van plug-ins in Python en zijn hoge mate van interoperabiliteit met belangrijke indelingen van GIS-gegevens door het gebruiken van de bibliotheek Geospatial Data Abstraction Library (GDAL/OGR).

Meer dan dat geeft de geïntegreerde Processing Toolbox, vroeger bekend als SEXTANTE, de mogelijkheid om eenvoudig algoritmen voor geo-verwerking vanuit verschillende toepassingen in te brengen in QGIS. Het treedt op als een gezamenlijke opslagplaats voor een breed bereik aan algoritmen, enkele eigen van QGIS en andere geïmporteerd vanuit externe toepassingen, zoals GRASS GIS of de Orfeo Toolbox. Ondersteuning voor algoritmen van ESA’s BEAM, NEST en Sentinel-1 Toolbox software en voor het instellen en uitvoeren van op SWAT gebaseerde hydrologische modellen werd toegevoegd aan de Processing Toolbox gedurende de ontwikkeling van WOIS. De Toolbox maakt het ook mogelijk op eenvoudige wijze aangepaste scripts voor R en Python toe te voegen. De invoer en uitvoer van de algoritmen van Processing Toolbox kunnen worden geëvalueerd met de mogelijkheden van QGIS voor gegevens I/O, renderen of het maken van kaarten.

Een belangrijk voordeel van de Processing Toolbox is de mogelijkheid om naadloos functionaliteiten te kunnen gebruiken van verscheidene providers van algoritmen voor het verwerken van gegevens en voor analyses. Dit kan worden gebruikt voor het maken van geautomatiseerde modellen voor verwerking en, door middle van een plug-in voor QGIS die werd ontwikkeld gedurende het project TIGER-NET, om sequentieel algoritmen van verscheidene providers te combineren in op wizards gebaseerde ketens van verwerking. Deze functionaliteit werd gebruikt om een bibliotheek van gestandaardiseerde werkstromen samen te stellen (met instructies) voor het uitvoeren van veel voorkomende, maar complexe taken die zijn gerelateerd aan analyses van gegevens van EO bij het beheren van waterbronnen.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>De WOIS grafische gebruikersinterface, inclusief de ingebedde bibliotheek voor werkstroom (midden) en op assistenten gebaseerde werkstroom voor Processing (rechts)</figcaption>
</figure>

Het operationele en praktische gebruik van WOIS om geïntegreerd beheer van waterbronnen in Afrika te ondersteunen wordt gedemonstreerd via series van gebruikersspecifieke demonstraties, die een breed bereik aan thema's en informatieproducten behandelen. Deze omvatten: waterkwaliteit van meren; monitoren van stromen; degradatie van land en karakteriseren van landgebruik; in kaart brengen van wateren en hydrologische modellen maken. De demonstraties hebben verschillende stages. Eerst worden aangepaste eind-tot-eind werkstromen voor verwerking ontwikkeld voor de gewenste producten en toepassingen. Deze werkstromen worden vervolgens gebruikt voor afgeleide producten voor belangrijke gebieden en tijdperioden, zoals gewenst door de gebruikers. In de laatste stap worden zowel de werkstromen (d.i. hun stabiliteit/uitvoering en gebruiksgemak) als ook de uitkomsten van het product geëvalueerd in nauwe samenspraak met de gebrukers.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 monitoren stroming Caprivi uiterwaarden, Namibië.</figcaption>
</figure>

## Conclusie
De ontwikkeling van WOIS vertegenwoordigt een succesvol voorbeeld van een door gebruikers gedreven en samenwerking ontwikkelingsmodel, waar functionaliteiten zijn ontworpen, ontwikkeld en geëvalueerd door middel van op gebruikers afgestemde gevallen om de echte impact van het systeem voor het verbeteren van het waterbeheer en plannen voor geïntegreerd beheer van waterbonnen te demonstreren. WOIS is al geïmplementeerd bij autoriteiten van belangrijke Afrikaanse rivierbassins, verscheidene Afrikaanse ministeries en agentschappen, als ook bij humanitaire organisaties en voor onderzoeksorganisaties. Het zal daarom blijven ontwikkelen in antwoord op voortdurende wensen van gebruikers voor nieuwe functionaliteiten en functionele verbeteringen en wegens verbeteringen aan de algemene software, algoritmen en methodes.

Speciale aandacht zal liggen op het verzekeren van de ondersteuning en implementatie van de capaciteit voor verwerking voor het nieuwe Sentinel satellietsysteem door het integreren van de toolboxen voor ESA Sentinel in WOIS en het ontwikkelen van toegepaste werkstromen voor productie. De volgende uitgave van WOIS (verwacht in de tweede helft van april 2015) zal al de Toolbox Sentinel-1 bevatten en een aantal werkstromen die deze nieuwe radar-gegevensset gebruiken voor het monitoren van stromen, het in kaart brengen van wateren, etc. Dit zal WOIS omtoveren naar een volledig operationeel systeem voor monitoren. Door middel van het beschikbaar stellen van dit licentie-vrije, krachtige en uitgebreide systeem, en door het doorlopend uitbouwen van de capaciteit en inspanningen voor trainingen, neigt het project de basis te leggen voor een extensie, d.i. uitrol naar andere landen en regio's in Afrika en daarbuiten.
## Verwijzingen
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," gepresenteerd op het ESA Living Planet Symp., Edinburgh, U.K., 11--13 september 2013.

## Links
- Meer informatie over de software van WOIS en het project TIGER-NET kan worden gevonden op de website van het project: www.tiger-net.org
- Meer informatie over het initiatief van ESA TIGER kan worden gevonden op de website van het initiatief: <http://www.tiger.esa.int/> WOIS is beschiklbaar voor downloaden (na registreren) vanaf de website van TIGER (<http://www.tiger.esa.int/page_eoservices_wois.php>) met broncode van de ontwikkelde plug-ins, scripts, modellen en werkstromen beschikbaar vanaf de GitHub-pagina van het project (<https://github.com/TIGER-NET>)
- Meer informatie over de nieuwe satellieten van Sentinel kan worden gevonden op de website van ESA: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Auteur
Dit artikel werd bijgedragen door Radoslaw Guzinski (WOIS-softwareontwikkelaar) met bijdragen van technische teams van TIGER-NET van DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), de technische universiteiten in Wenen (<http://rs.geo.tuwien.ac.at/>) en Kopenhagen (<http://www.env.dtu.dk/>), alsook van het European Space Agency ( www.esa.int).

{{<content-end >}}
