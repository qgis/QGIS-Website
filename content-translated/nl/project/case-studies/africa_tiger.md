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
  <span>June 30, 2012</span>
</p>

The Water Observation and Information System (WOIS) is an open source software tool for monitoring, assessing and inventorying water resources in a cost-effective manner using Earth Observation (EO) data. The WOIS has been developed under the TIGER-NET project, which is a major component of the TIGER initiative of the European Space Agency (ESA) and whose main goal is to support the African Earth observation capacity for water resource monitoring. TIGER-NET aims to support the satellite-based assessment and monitoring of water resources from watershed to cross-border basin levels through the provision of a free and powerful software package, with associated capacity building, to African authorities.
## Omschrijving
The WOIS can be seen as a multipurpose system consisting of a spatial database, facilities for extracting and processing EO data, and integrative tools and models aimed at decision support e.g. hydrological modelling and GIS-embedded visualization and analysis tools. The WOIS is designed around QGIS, which acts as the front-end Graphical-User-Interface (GUI). QGIS was chosen as the central integrating platform, due to its clear and accessible GUI, strong development community, ease of implementing additional functionalities through Python plugins and its high level of interoperability with major GIS data formats through the use of the Geospatial Data Abstraction Library (GDAL/OGR) library.

Moreover, the integrated Processing Toolbox, formerly known as SEXTANTE, brings the ability to easily incorporate geoprocessing algorithms from various applications into QGIS. It acts as a joint repository for a wide range of algorithms, some native to QGIS and others imported from external applications, such as GRASS GIS or the Orfeo Toolbox. Support for algorithms from ESA's BEAM, NEST and Sentinel-1 Toolbox software and for setting up and executing SWAT based hydrological models was added to the Processing Toolbox during the WOIS development. The toolbox also allows for easy incorporation of custom R and Python scripts. The inputs and outputs of the Processing Toolbox algorithms can be evaluated with the QGIS capabilities of data I/O, rendering or map creation.

Een belangrijk voordeel van de Processing Toolbox is de mogelijkheid om naadloos functionaliteiten te kunnen gebruiken van verscheidene providers van algoritmen voor het verwerken van gegevens en voor analyses. Dit kan worden gebruikt voor het maken van geautomatiseerde modellen voor verwerking en, door middle van een plug-in voor QGIS die werd ontwikkeld gedurende het project TIGER-NET, om sequentieel algoritmen van verscheidene providers te combineren in op wizards gebaseerde ketens van verwerking. Deze functionaliteit werd gebruikt om een bibliotheek van gestandaardiseerde werkstromen samen te stellen (met instructies) voor het uitvoeren van veel voorkomende, maar complexe taken die zijn gerelateerd aan analyses van gegevens van EO bij het beheren van waterbronnen.

<figure>
<img src="../images/africa_tiger1.jpg" class="align-center" style="width:100.0%" alt="africa_tiger1.jpg" />
<figcaption>The WOIS graphical user interface, including the embedded workflow library (center) and wizard-based processing workflow (right)</figcaption>
</figure>

Het operationele en praktische gebruik van WOIS om geïntegreerd beheer van waterbronnen in Afrika te ondersteunen wordt gedemonstreerd via series van gebruikersspecifieke demonstraties, die een breed bereik aan thema's en informatieproducten behandelen. Deze omvatten: waterkwaliteit van meren; monitoren van stromen; degradatie van land en karakteriseren van landgebruik; in kaart brengen van wateren en hydrologische modellen maken. De demonstraties hebben verschillende stages. Eerst worden aangepaste eind-tot-eind werkstromen voor verwerking ontwikkeld voor de gewenste producten en toepassingen. Deze werkstromen worden vervolgens gebruikt voor afgeleide producten voor belangrijke gebieden en tijdperioden, zoals gewenst door de gebruikers. In de laatste stap worden zowel de werkstromen (d.i. hun stabiliteit/uitvoering en gebruiksgemak) als ook de uitkomsten van het product geëvalueerd in nauwe samenspraak met de gebrukers.

<figure>
<img src="../images/africa_tiger2.jpg" class="align-center" style="width:100.0%" alt="africa_tiger2.jpg" />
<figcaption>Sentinel-1 flood monitoring of Caprivi flood plain, Namibia.</figcaption>
</figure>

## Conclusie
De ontwikkeling van WOIS vertegenwoordigt een succesvol voorbeeld van een door gebruikers gedreven en samenwerking ontwikkelingsmodel, waar functionaliteiten zijn ontworpen, ontwikkeld en geëvalueerd door middel van op gebruikers afgestemde gevallen om de echte impact van het systeem voor het verbeteren van het waterbeheer en plannen voor geïntegreerd beheer van waterbonnen te demonstreren. WOIS is al geïmplementeerd bij autoriteiten van belangrijke Afrikaanse rivierbassins, verscheidene Afrikaanse ministeries en agentschappen, als ook bij humanitaire organisaties en voor onderzoeksorganisaties. Het zal daarom blijven ontwikkelen in antwoord op voortdurende wensen van gebruikers voor nieuwe functionaliteiten en functionele verbeteringen en wegens verbeteringen aan de algemene software, algoritmen en methodes.

Speciale aandacht zal liggen op het verzekeren van de ondersteuning en implementatie van de capaciteit voor verwerking voor het nieuwe Sentinel satellietsysteem door het integreren van de toolboxen voor ESA Sentinel in WOIS en het ontwikkelen van toegepaste werkstromen voor productie. De volgende uitgave van WOIS (verwacht in de tweede helft van april 2015) zal al de Toolbox Sentinel-1 bevatten en een aantal werkstromen die deze nieuwe radar-gegevensset gebruiken voor het monitoren van stromen, het in kaart brengen van wateren, etc. Dit zal WOIS omtoveren naar een volledig operationeel systeem voor monitoren. Door middel van het beschikbaar stellen van dit licentie-vrije, krachtige en uitgebreide systeem, en door het doorlopend uitbouwen van de capaciteit en inspanningen voor trainingen, neigt het project de basis te leggen voor een extensie, d.i. uitrol naar andere landen en regio's in Afrika en daarbuiten.
## Verwijzingen
- Bauer-Gottwein, P., Jensen, I. H., Guzinski, R., Bredtoft, G. K. T., Hansen, S., & Michailovsky, C. I. (2015). Operational river discharge forecasting in poorly gauged basins: the Kavango River basin case study. Hydrology and Earth System Sciences, 19(3), 1469-1485.
- Guzinski, R.; Kass, S.; Huber, S.; Bauer-Gottwein, P.; Jensen, I.H.; Naeimi, V.; Doubkova, M.; Walli, A.; Tottrup, C. Enabling the Use of Earth Observation Data for Integrated Water Resource Management in Africa with the Water Observation and Information System. Remote Sens. 2014, 6, 7819-7839.
- Walli, A., Tottrup, C., Naeimi, V., Bauer-Gottwein, P., Bila, M., Mufeti, P., Tumbulto, J.W., Rajah, C., Moloele, L.S. & Koetz, B. "TIGER-NET---Enabling an earth observation capacity for integrated water resource management in Africa," presented at the ESA Living Planet Symp., Edinburgh, U.K., Sep. 11--13, 2013.

## Links
- More information about the WOIS software and the TIGER-NET project can be found on the project's website: www.tiger-net.org
- More information about ESA's TIGER initiative can be found on the initiative's website: <http://www.tiger.esa.int/> WOIS is available for download (after registration) from the TIGER website (<http://www.tiger.esa.int/page_eoservices_wois.php>) with source code of the developed plugins, scripts, models and workflows available from the project's GitHub page (<https://github.com/TIGER-NET>)
- More information about the new Sentinel satellites can be found on ESA's website: <http://www.esa.int/Our_Activities/Observing_the_Earth/Copernicus/Overview4>

### Auteur
This article was contributed by Radoslaw Guzinski (WOIS software developer) with contributions from the TIGER-NET technical teams at DHI-GRAS (www.dhi-gras.com), GeoVille (www.geoville.com), the technical universities in Vienna (<http://rs.geo.tuwien.ac.at/>) and Copenhagen (<http://www.env.dtu.dk/>) as well as the European Space Agency ( www.esa.int).

{{<content-end >}}
