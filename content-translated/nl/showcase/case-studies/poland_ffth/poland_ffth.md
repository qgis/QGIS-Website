---
draft: 'true'

---
# QGIS gebruiken voor FTTH/GPON netwerkplanning vanwege de implementatie van de European Digital Agenda
## Definitie van het probleem
Gedurende de laatste jaren zijn veel EU-landen operationele programma's gestart om de European Digital Agenda (EAC), ontwikkeld door de Europese Commissie in 2010, te implementeren. Overeenkomstig de richtlijnen daarvan zou tot 2020 elke burger van de Europese Unie toegang moeten hebben tot 30 Mbps internet bandbreedte en ten minste de helft van hen zou toegang moeten hebben tot een bandbreedte die niet lager is dan 100 Mbps.

Polen is één van de landen waarin de Agenda wordt geïmplementeerd. Dankzij fondsen van de Europese Unie kunnen vele lokale operators concurreren met grote telecomproviders met betrekking tot hoge-snelheid breedbanddiensten. Helaas vereist het aanvragen van fondsen heel veel werk om de juiste documentatie te maken, inclusief, naast andere dingen, de ontwikkeling van conceptuele kaarten voor gepland FTTH (Fiber To The Home)-netwerk.

Meer nog, momenteel zijn er geen op GIS gebaseerde IT-programma's beschikbaar om de potentiële voordelen bij het voorbereiden van documentatie te ondersteunen. De complexiteit van het probleem wordt zelfs nog gecompliceerder door het feit dat een dergelijke software het maken van documentatie overeenkomstig specifieke programmarichtlijnen mogelijk zou moeten maken (bijv. de verplichting om onderwijskundige instituten aan te sluiten).

Omdat we uitgebreide ervaring hebben in de telecommunicatie-industrie, hebben entiteiten die fondsen van de EU willen aanvragen ons gevraagd software te maken die het ontwikkelen van conceptuele kaarten voor FTTH-netwerk ondersteunt. Door deze software gegenereerde producten zouden het proces voor het voorbereiden van de aanvraag significant moeten versnellen.
## Beschrijving van de oplossing
Vanwege de grote populariteit, wijdverbreide beschikbaarheid, openheid van de software en immens functionele mogelijkheden, voelt het natuurlijk om QGIS te selecteren als platform dat dient als basis voor onze oplossing.

Overeenkomstig de richtlijnen van FTTH Council Europe, is het cruciaal om eerst een plan voor te bereiden dat zowel rekening houdt met het technische aspect (plaatsing van kabels, lasverbindingen, splitters) als met het economische aspect (vraag), gebaseerd op gegevens voor punten van echte adressen. De structuur van gebouwen en de dichtheid van de ontwikkeling van gebouwen bepalen de technologie van het GPON (Gigabit Passive Optical Network) netwerkontwerp. Het is nodig, om de mogelijkheid te hebben de topologie van het netwerk efficiënt te plannen, om naast andere dingen:
- toegang tot gegevens van GIS,
- automatisering van gegevensverwerking van GIS,
- toepassing van algoritmes voor netwerk optimalisatie,
- toepassen van regels voor GPON netwerken.

Al deze items werden verbonden op het platform van QGIS platform. Hieronder staat een korte beschrijving over hoe we het project hebben gerealiseerd en welke functionele items werden ingepast om één oplossing te maken.

We hadden, om ons doel te kunnen bereiken, nog een aantal functionele componenten nodig, los van het standaard platform van GIS:
- GRASS - een verzameling algoritmes voor vector en netwerk,
- QGIS plug-ins - OpenLayer, QuickOSM, Scipy Point Clustering, WorkContextTracer (onze plug-in),
- QGIS Grafische modellen bouwen – programma voor grafisch bouwen van modellen,
- SpatiaLite - een lokale database voor het opslaan van gegevens voor in- en uitvoer.

De gehele oplossing was gebaseerd op het concept van zogenaamde assistenten die, stap voor stap, het proces van het realiseren van het voorbereiden van het technische concept voor het FFTx-netwerk doorliepen. Met behulp van Grafische modellen bouwen \'geoprocessing\' maakten we modellen die alleen de benodigde invoergegevens van de verwerker nodig hadden. Algoritmische complexiteit werd in modellen ingebouwd in de vorm van een ontworpen stroom, die bestaande algoritmes van QGIS gebruikt en toegewezen scripts aanroept.

![](./images/poland_ffth/toolbox.png){.align-left}

We verschaften een plug-in, genaamd WorkContextTracer, die ons werk groepeert in zogenaamde werkcontexten, om te voorkomen dat resultaten van elkaar opvolgende analyses zich zouden vermengen.

![](./images/poland_ffth/workorder.png){.align-left}

Netwerkalgoritmes gebaseerd op de functie Graph die beschikbaar zijn in GRASS werden verrijkt door de scripts voor telecommunicatie toe te voegen. We introduceerden een concept van het vragen van clusters wat ons in staat stelde zowel K-gemiddelden als hiërarchische methoden te gebruiken om vraagpunten samen te voegen.

Scripts voor Geoprocessing met gebruik van de laag voor routeren van kabels en Dijkstra-algoritme ontwikkelen een voorstel voor routering van de kabel met locaties voor optische fiberknopen.

Operators hebben ook een verbinding nodig tussen gemaakte netwerkknopen en adrespunten om de individuele kosten voor elke netwerktak in te schatten. We maakten. om deze taak te voltooien, scripts die deze bewerking uitvoert en de resultaten opslaat in de lokale database van SpatiaLite. De gegevens moesten zijn te exporteren naar een werkblad, dus gebruikten we een vrije softwarebibliotheek om aan dit vereiste te voldoen.
## Hoe gebruikers het gereedschap gebruikten om een netwerkplan FTTH/GPON te maken
De gebruiker begon zijn werk met het starten van een nieuwe werkcontext en het specificeren van een invoerlaag met adrespunten die moesten worden geanalyseerd. Met behulp van de standaard interface van QGIS kan de gebruiker aan aantal vragen voor adrespunten instellen en tenslotte de parameters verschaffen die nodig waren voor de verdere stappen van het algoritme.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

Zonder informatie te hebben over de bestaande civiele infrastructuur, werd een op de juiste manier gefilterd wegennetwerk van OpenStreet gebruikt als routelaag. Algoritmes voor Scipy werden gevoed met invoerparameters, clusterde de adrespunten naar gevraagde samenvoegingen en markeerden ze met een afzonderlijke kleur, welke kleur de toewijzing aan een bepaalde cluster weregaf.

![](./images/poland_ffth/step1.png){.align-left}

Nadat alle adrespunten waren geclusterd, initieerde de gebruiker de stappen voor het op hoog niveau plannen van het netwerk, door in eerdere stappen voorbereide lagen te verschaffen en een laag met beginpunten voor het GPON-netwerk.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Bij het voltooien van het algoritme staan in QGIS geometrieobjecten die geplande kabels en locaties voor verbindingen weergeven. Gebaseerd op de gevraagde gegevens en topologie van het netwerk, wordt aanvullende informatie opgeslagen in de database, zoals de lengte van de kabel, het profiel ervan, servicegebieden van nodes.

![](./images/poland_ffth/step4_results.png){.align-left}

In dit stadium heeft de gebruiker al alle stukken benodigde informatie om een technisch concept voor een hoog niveau FTTx-netwerk te ontwikkelen. Het laatste deel was het genereren van een werkblad met een rapport van de gegevens, die alle berekende gegevens liet zien vanuit verschillende perspectieven.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Conclusie
Dankzij het gebruiken van het platform QGIS als ook zijn mogelijkheden tot uitbreiding, konden we een vrije open bron-oplossing ontwikkelen die het voor operators van telecommunicatie mogelijk maken om de benodigde documenten voor te bereiden om een aanvraag in te dienen voor co-financiering voor het EU-programma dat de European Digital Agenda implementeert.

Door flexibele vectoralgoritmes te combineren met de scripts voor telecom ontwerpen, maakten we gebruik van het praktisch gebruik van rekenkundige algoritmes voor het oplossen van echte problemen die optreden bij het plannen van netwerken voor telecommunicatie. De gebruiker werkt met een bereik van te begrijpen gegevens (gemeenten, gebouwen, wegen) waar transformatie van deze informatie naar een rekenkundig model is verborgen voor die gebruiker.

De gebruiker kreeg veel nuttige voordelen:
- Automatische ontwikkeling van de planning voor  GPON-netwerk, gebaseerd op publiek beschikbare gegevens en regels voor het ontwerpen van technologie voor GPON.
- Mogelijkheid om het programma aan te passen met specifieke richtlijnen voor het EU-programma in een bepaald land.
- De grote nauwkeurigheid van de resultaten, corresponderend met de echte dimensies.
- Genereren van de benodigde gegevens voor het aanvragen van fondsen van de EU: kaart van het concept netwerk, rapport voor kabels en verbindingen met toewijzing van servicegebieden.
- Mogelijkheid om de constructie precies te bepalen en verminderen van de kosten voor elk deel van het netwerk met berekening van de kosten voor het aansluiten van elk adrespunt.
- Mogelijkheid om adrespunten te prioriteren van meest voordelig tot onvoordelig.
- Mogelijkheid om basale economische indicatoren te evalueren, zoals ROI, NPV.

## Nuttige links en bibliografie
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - informatie over European Digital Agenda
- <http://www.ftthcouncil.eu/> - website FTTH Council Europe 
- <https://www.scipy.org/> - website SciPy project
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - webpagina downloaden programma.

## Auteurs
De oplossing is een volledig vrij open bron-programma. Het is deel van een groter project, gebaseerd op QGIS en FreeCAD-platformen waarvan de bedoeling is dat het wordt gebruikt in de telecommunicatie-industrie.

De auteur van deze op QGIS gebaseerde oplossing is Softelnet (<https://www.softelnet.com>), een bedrijf dat software maakt en integreert voor de telecommunicatie-industrie voor meer dan 15 jaar.
