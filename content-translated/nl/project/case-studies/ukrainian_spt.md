---
HasBanner: false
archived: true
date: 2022-12-31
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/ukraine_spt1.png
title: Oekraïens open initiatief voor het maken van gereedschappen voor ruimtelijke
  planning in de omgeving van QGIS
type: case-study

---
{{<content-start >}}
# Oekraïens open initiatief voor het maken van gereedschappen voor ruimtelijke planning in de omgeving van QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>31 december 2022</span>
</p>

## Introductie
Opgericht in 2018 is Julie\'s Data een Oekraïens consultancy-agentschap dat open-sourceoplossingen levert om breed openbaar te gebruiken. We focussen voornamelijk op strategische milieubeoordelingen met GIS, stedelijke planning, maken en onderwijzen van QGIS-cursussen en uitvoeren van het hieronder beschreven project voor crowdsourcing.

Door de laatste jaren te hebben gewerkt met lokale gemeenschappen, heeft Julie\'s Data een concept gevormd voor het oplossen van een bijzonder aantal publieke administratieve problemen, gedicteerd door het gebrek aan moderne programma's voor het beheren van geogegevens. Een dergelijk probleem is het gebrek aan legale lokale georuimtelijke gegevens van hoge kwaliteit en toegankelijk vanuit kadasters die gemeenschappen in staat stellen om zich te laten zien op de wereldinvesteringskaart en ze in staat stellen een gezond klimaat te scheppen voor voorstellen voor een duurzame ontwikkeling.

In februari 2022, twee dagen voor de Russische agressie op volledige schaal, adopteerde de Oekraïense overheid een decreet dat de verplichte structuur voor databases voor ruimtelijke planning definieerde - de primaire bron voor het vullen en uitvoeren van kadastrale systemen.

In lijn met zijn open source-houding lanceerde Julie\'s Data (<https://juliesdata.com/>) begin juni een initiatief voor crowdsourcing dat is gericht op het implementeren van de bovenstaande structuur met open source-programma\'s en riep iedereen op om mee te doen bij het ontwikkelen van programma\'s voor toepassen van GIS voor ruimtelijk plannen met QGIS.
## Programma\'s voor ruimtelijk plannen tot leven brengen
Het initiatief ontving significante terugkoppeling van de gemeenschap - meer dan 100 aanvragen van mensen die wilden meedoen, uit verschillende regio\'s van Oekraïne, inclusief de regio\'s Kherson, Zaporizhzhia, Kharkiv, Chernihiv, Kyiv, Lviv, Ivano-Frankivsk, Poltava en Vinnytsia.

Als resultaat daarvan werd een groep van 62 deelnemers met verscheidene specialiteiten gevormd - architecten, geodesisten, landmeters, cartografen, GIS-specialisten, ecologen, wetenschappers, vertegenwoordigers van lokale overheden, en anderen. De deelnemers stellen zich tot doel programma's voor ruimtelijk plannen van hoge kwaliteit te maken (SPT voor het gemak). Dit is gebaseerd op de goedgekeurde structuur voor de geodatabase, zodat elke geïnteresseerde persoon ze vrij kan gebruiken en zonder onnodige operationele kosten voor het oplossen van hun taken - in professionele stedelijke planning, wetenschappelijk, in het onderwijs, of voor publieke activiteiten. Daarom werd besloten de toekomstige SPT te distribueren onder de termen van de licentie CC BY-SA.

Voor de implementatie van SPT werd QGIS gekozen, omdat het voldoet aan twee belangrijke eisen van de deelnemers: ten eerste - om ervoor te zorgen dat elke deelnemer de mogelijkheid heeft zonder obstakels te kunnen werken, en ten tweede - om iedereen de mogelijkheid te geven het ontwikkelde SPT te gebruiken zonder onnodige barrières en kosten. De meeste deelnemers gebruikten QGIS tijdens het project voor het eerst en begonnen ook QGIS in hun professionele werk te gebruiken.

De groep van het initiatief werd gecoördineerd door zijn organisatoren, met regelmatige bijeenkomsten waar taken, voorstellen, vragen en problemen, die tijdens het werk naar voren kwamen, werden besproken. De meeste communicatie was in de messenger chat, waar constructieve discussies tussen de deelnemers werden gehouden om de waarheid te vinden.

De werkgroep implementeerde met succes de database in de indelingen PostgreSQL en GeoPackage en maakte formulieren voor de klassen (lagen), inclusief de regels voor integriteit van de gegevens. Deze waren goedgekeurd als vereisten voor de georuimtelijke database en werden opgesteld in QGIS. De bibliotheek met symbolen, met de op regels gebaseerde symbologie voor elke klasse (lagen), werd opgesteld in het projectbestand .qgs. Instellingen voor laagstijlen voor elke laag werden getest en opgeslagen in de georuimtelijke database van de SPT.

<figure>
<img src="../images/ukraine_spt1.png" class="align-left" alt="ukraine_spt1.png" />
<figcaption><em>Een voorbeeld uit de bibliotheek Symbolen</em></figcaption>
</figure>

Huidige ontwikkelingen van de initiatiefgroep werden gepresenteerd op 19 oktober 2022, op het open webinar \"Free tools for the urban planning documentation development. Presentation of the first stage\", dat een breed publiek van specialisten en vertegenwoordigers van gemeenschappen trok, vanuit geheel Oekraïne.

Gedurende het webinar deelden projectleden niet alleen hun ervaringen over het deelnemen aan het project, maar ook hun eigen ervaringen met het gebruiken van QGIS en hun eerste resultaten met het ontwikkelen van documentatie voor stedelijke planning, met hulp van de gemaakte programma's.

<figure>
<img src="../images/ukraine_spt2.png" class="align-left" alt="ukraine_spt2.png" />
<figcaption><em>Een voorbeeld van een stedelijk plan, gemaakt met SPT</em></figcaption>
</figure>

We begrijpen dat om een brede implementatie van GIS te kunnen laten werken, Oekraïne een solide open-sourcegemeenschap nodig heeft. Dus, naast andere deelnemers, nodigden we Anita Graser uit, die haar gedachten deelde over hoe oplossingen met open source door lokale Oostenrijkse overheden worden gebruikt en hoe ze een duurzaam geheel vormen, bestand tegen de uitdagingen van de maatschappij.

De geuite meningen op het webinar vonden hun weg naar de luisteraars, zoals bleek uit meer dan 600 aanvragen om een SPT te krijgen, van architecten, landbeheerders, vertegenwoordigers van lokale overheden, leraren aan universiteiten en wetenschappers. Iedereen kan de huidige SPT krijgen door hier een webformulier in te vullen: <https://juliesdata.com/form/zapit-na-otrimannya-bgd-mistobud>. De video-opname van het webinar is beschikbaar op YouTube (<https://youtu.be/ZRX1nI5Tkv0/>).
## Conclusies
Ons initiatief leeft voort en we nodigen iedereen uit die mee wil doen. De belangrijkste vragen voor het volgende stadium zijn de relaties tussen de klassen van de georuimtelijke database, programma\'s voor verificatie van toplogieregels, die bij wet verplicht zijn en ook om een minimale set functionaliteit voor de SPT te maken voor het effectief werken met ruimtelijke documentatie voor lokale gemeenschappen.

In deze tijden van drastische wijzigingen zien we de kwetsbaarheid van maatschappijen die zijn gebouwd op een gecentraliseerde infrastructuur voor gegevens als gemeenschappen die afhankelijk zijn van de wil van de eigenaren van de infrastructuur.

We geloven dat onze SPT een van de toegepaste programma\'s zal worden voor het in vrijheid verkennen, maken van ruimtelijke gegevens en betrokken zijn bij het nemen van politieke besluitvorming.
## Auteurs
Yuliia Maksymova, kandidaat technische wetenschappen, assistent bij het departement van geoinformatica en fotogrammetrie van KNUBA, medeoprichtster en GIS-specialist in Julie\'s Data, facebookpagina <https://www.facebook.com/profile.php?id=100006853998055>. email: <office@juliesdata.com>

Oleksii Boiko, GIS-specialist, medeoprichter van Julie\'s Data, email: <contact@juliesdata.com>.

{{<content-end >}}
