---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/uruguay_mides1.png
title: Gebruiken van QGIS bij het Ministerie van Sociale ontwikkeling in Uruguay (MIDES)
type: case-study

---
{{<content-start >}}
# Gebruiken van QGIS bij het Ministerie van Sociale ontwikkeling in Uruguay (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 maart 2016</span>
</p>

## Introductie
Het Ministerie van Sociale Ontwikkeling van Uruguay ([MIDES](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision), voor zijn acroniem in het Spaans) is verantwoordelijk voor het nationale sociale beleid. MIDES is ook verantwoordelijk voor de coördinatie -op zowel sectoraal als territoriaal niveau- articulatie, monitoren, supervisie en evaluatie van plannen, programma's en projecten, binnen het gebied van zijn competentie, gericht op de consolidatie van een progressief redistributief sociaal beleid.

De Nationale Divisie voor Evaluatie en Monitoren ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is een sectie van MIDES die overzicht houdt over het monitoren en evalueren van plannen, programma\'s, acties, apparaten en sociale projecten voor het gehele nationale territorium. DINEM produceert en beheert ook noodzakelijke informatie om zijn ontwerp en implementatie te verbeteren.

Het [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is verantwoordelijk voor het produceren, beheren en analyseren van geografische informatie,
## QGIS bij het Department of Geography van de DINEM
Vanaf de consolidatie van het Department of Geography in 2012 hebben we geprobeerd onze open bron-software in te bouwen om aan onze verplichtingen te voldoen. In het bijzonder het beheer van uitgebreid veldwerk, bestaande uit de jaarlijkse implementatie van bij benadering 40.000 bezoeken aan sociaal kwetsbare huishoudens in het gehele land. Het doel was om een nauwgezette database met geoverwijzingen van huishoudens te conformeren, om de implementatie van sociaal beleid te verbeteren. In het bijzonder werden gegevens verzameld om het bereik van monetaire overdrachtsprogramma's te verhogen ([\"Asignaciones Familiares – Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) en [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). Het toegepaste onderzoeksformulier bevatte onder meer sociale, huisvestings- en milieuaspecten.

Logistiek om het veldwerk te kunnen verwerken betrof onder meer het gebruiken van statistiekpakketten om de gegenereerde database te beheren, samen met een intensief gebruik van GIS om veldwerk te organiseren en ontvangen gegevens te voorzien van geoverwijzingen.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS aan het werk: identificeren van huizen in informele nederzettingen om veldwerk te implementeren</figcaption>
</figure>

Hoewel merksoftware was geïmplementeerd toen werd begonnen met het werkproces, vroeg de ontwikkeling van de zelfstandige taken zelf langzamerhand dat het zou worden geconverteerd naar open bron-software. Toen het gehele proces als geheel meer werd gecomputeriseerd - waaronder het inpassen van een programma voor de werkstroom en een PostGIS georuimtelijke database-, moedigden vereisten voor licenties en aangeboden opties van voordelen van vrije en open bron-software (FOSS)  ons aan de overstap te wagen. op die manier, waarbij het project van QGIS werd verfijnd (minder problemen en meer functionaliteiten), waren we in staat onze wensen uit te voeren met behulp van QGIS. Met PostGIS geassocieerde gereedschappen stelden de werkgroep in staat snel de benodigde taken voor het plannen van het dagelijkse veldwerk te coördineren, samen met opvolgende taken taken voor analyses op dezelfde bij het veldwerk gegenereerde gegevens, kort nadat het was verkregen en gedigitaliseerd.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS aan het werk: Montevideo, Uruguay’s hoofdstad en dichtstbevolkte stad, overlay met PostGIS-laag die nog te bezoeken plaatsen weergeeft (meestal bestaande uit sociaal kwetsbare huishoudens, aan de randen van de stad)</figcaption>
</figure>

In aanvulling op het informatiebeheer en implementatie van veldwerk, gebruikten we constant QGIS typische georuimtelijke gereedschappen om thematische cartografie te maken, en in taken voor ruimtelijke analyses. Dit laatste, zowel met betrekking tot de gegevens die het veldwerk genereert, als ook andere informatie van de programma's van het  ministerie, en frequent zelfs om interinstitutionele projecten te helpen. Met [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) waren we in staat interactieve kaarten te produceren, die de belangrijkste manier zijn geworden om de resultaten van dergelijke onderzoeken te communiceren. Zij maken het voor anderen binnen andere programma's en diensten mogelijk om eenvoudiger en effectiever grotere hoeveelheden informatie te beheren dan met een verzameling statische kaarten, zelfs wanneer de bronnen niet worden gebruikt om ruimtelijke gegevens te lezen.
## Conclusie
QGIS is een fundamentele software geworden voor het Department of Geography bij DINEM. Het presenteert een excellente uitvoering om te werken met grote bestanden en samen te werken met PostGIS en ons programma voor de werkstroom. Dit stelt ons in staat onze geografische gegevens excellent te beheren, wat ook geldt voor het produceren van basiskaarten en thematische cartografie van superieure kwaliteit.

Tegelijkertijd zijn de, extra mogelijkheden die ingepast kunnen worden door plug-ins voor ons van grote waarde. Bijvoorbeeld de mogelijkheid voor het exporteren van \"Leaflet\" kaartweergaven, alsook het inpassen van hoge resolutie satellietafbeeldingen direct in het GIS werkgebied via "OpenLayers" om, naast andere dingen, handmatig informatie te vectoriseren.

Deze variëteit aan opties is precies wat ons in staat stelde om de specifieke en tegelijkertijd zeer verschillende technische oplossingen te ontwikkelen die programma's en diensten de afgelopen jaren nodig hadden. Zoals in dit artikel vermeld, kunnen we stellen dat QGIS voldoet aan de nodige eisen voor gebruik in publieke administratie als desktop-GIS-software. Ook is het een hoeksteen voor dit instituut om te helpen een webkaart te maken die de bevolking veel meer informatie biedt over sociale problemen ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers gebaseerd WEB GIS ontwikkeld door de IT-divisie).
## Auteurs
Guillermo D\'Angelo - Hoofd van het Geography Department (DINEM-MIDES, Uruguay). Graad in Geografie.

Richard Detomasi - Adviseur in het Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Ph.D. student in Social Sciences, Population Studies. Magister in Contemporary Studies van Latijns-Amerika. Graad in Anthropological Sciences.

Martín Hahn - Adviseur in Spatial Analysis Section of Geography Department (DINEM-MIDES, Uruguay). Bach. momentele studerend voor een graad in Geography.

Ondanks het feit dat het huidige artikel werd geschreven door de drie hierboven vermelde personen, zijn er meer dan honderd mensen betrokken bij het daarin beschreven proces, dit werk behoort dan ook voor een groot deel aan hen toe.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
