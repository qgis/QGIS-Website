---
HasBanner: false
archived: false
date: '2025-06-08'
draft: false
featured: true
section: project
sidebar: true
thumbnail: images/portugal_trees_inventory3.webp
title: QGIS en Mergin Maps gebruiken voor het maken van stedelijke inventarisaties
  van bomen in Portugal
type: case-study

---
{{<content-start >}}
# QGIS en Mergin Maps gebruiken voor het maken van stedelijke inventarisaties van bomen in Portugal
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>8 juni 2025</span>
</p>

NaturalGIS \[<https://www.naturalgis.pt>\] is een Portugees bedrijf dat zich specialiseert in Geografische InformatieSystemen (GIS), met een bijzondere focus op technologieën van QGIS en PostGIS. Hun hoofdtaak bestaat uit het verschaffen van technische ondersteuning, training en het ontwikkelen van aangepaste GIS-oplossingen, inclusief WebGIS-platforms en plug-ins voor QGIS.

Mergin Maps \[<https://merginmaps.com>\] is een georuimtelijk gegevensplatform dat het verzamelen van gegevens uit het veld en synchroniseren met QGIS inschakelt. De hoofdtaak is het verschaffen van programma's voor offline mobiel in kaart brengen en met elkaar samenwerkende GIS-werkstromen. De service wordt breed gebruikt bij het monitoren van omgevingen, telecommunicatie, landbouw of beheren van bezittingen.

In 2021 nam de Portugese overheid een wet aan die het beheren van bomen in stedelijke gebieden regelt en van gemeenten eist dat ze een inventarisatie publiceren van alle bomen op stedelijk openbaar land. NaturalGIS gebruikt QGIS Mergin Maps om onderzoek in het veld uit te voeren om inventarisaties van bomen in stedelijke gebieden te maken in verscheidene Portugese gemeenten (bijv. Mação, Palmela, Lourinhã en Soure). De combinatie van QGIS en Mergin Maps maakt het mogelijk een aangepaste gegevensstructuur te laten voldoen aan de vereisten van de regelingen, terwijl het een eenvoudige mobiele interface voor niet-technische gebruikers verschaft om nauwkeurig onderzoeksgegevens te verzamelen.

<figure>
  <img src="../images/portugal_trees_inventory1.webp" class="align-right" alt="Simple user interface makes Mergin Maps easy to use for non-technical users" />
  <figcaption>Eenvoudige gebruikersinterface maakt Mergin Maps gemakkelijk te gebruiken voor niet-technische gebruikers</figcaption>
</figure>

## Ontwerpen van een zich aan de regels conformerend onderzoek naar bomen met QGIS
De regelgeving eist dat de volgende informatie moet worden verzameld voor elke boom die staat op land dat eigendom is van de gemeente:
- Soort of andere speciale klasse
- Afmetingen (totale hoogte, diameter, etc.)
- Geschatte leeftijd
- Gezondheidsstatus
- Geolocatie
- Redenen voor beschermde status (indien aanwezig)

Om de juiste identificatie van de bomen te bevestigen, worden ook foto's genomen van de wortels, stam, bladeren en eventueel fruit/kegels. Extra details, zoals het type bodem waar de boom in is geplant, irrigatiesysteem, grootte van het bladerdak, teken van ziekte/stress of defecten en andere informatie, wordt ook verzameld.

Het project werd ontworpen met QGIS en de gegevens werden gehost op hun eigen server met een uitrol van Mergin Maps Community Edition (CE), een versie van Mergin Maps die is gepubliceerd onder de licentie GNU AGPL-3.

De opstelling van het project gebruikte enige voorwaardelijke zichtbaarheid en widgets voor het bijvoegen van foto's. Wegens het grote aantal te verzamelen foto's voor het project, werd een mogelijkheid gebruikt in Mergin Maps die het downloaden van foto's beperkt voor elk apparaat. Om daarnaast opslag op het apparaat te beperken, werd elke dag een script uitgevoerd dat de Mergin Maps CLI-gereedschappen (Command Line Interface) gebruikte om de foto's van het project te verwijderen en ze op te slaan op een webserver. Daarna werd een link naar de foto opgeslagen in een daarvoor aangewezen veld op de onderzoekslaag, wat het mogelijk maakt een voorbeeld van de foto te bekijken in de app.

<figure>
  <img src="../images/portugal_trees_inventory2.webp" class="align-right" alt="Mobile forms were set up in QGIS project and transferred to Mergin Maps" />
  <figcaption>Mobiele formulieren werden in het project van QGIS ingesteld en overgebracht naar Mergin Maps</figcaption>
</figure>

## Verzamelen van gegevens geoptimaliseerd voor mobiel gebruik
De gegevens werden verzameld door teams van 2-4 onderzoekers in elke gemeente. Gewoonlijk konden ze, gemiddeld, gegevens verzamelen met een snelheid van ongeveer 150 bomen per dag. De voor mobiel geoptimaliseerde interface voor Mergin Maps maakte het gemakkelijk voor niet-technische gebruikers om de methoden voor het verzamelen van gegevens snel te leren.

Als de initiële inventarisatie eenmaal was verzameld door het team, konden ze een proces voor overdracht uitvoeren om het team van de lokale gemeente te trainen hoe het project in QGIS te beheren en, waar nodig, de gegevens in de app bij te werken. Gebruiken van QGIS en Mergin Maps voor dit project zorgde ervoor dat de inventarisatie van de bomen nauwkeurig kon worden verzameld binnen de daarvoor gestelde tijd.

<figure>
  <img src="../images/portugal_trees_inventory3.webp" class="align-right" alt="The QGIS project used for the inventory" />
  <figcaption>Het voor de inventarisatie gebruikte project van QGIS</figcaption>
</figure>

## Auteur
Giovanni Manghi B.Sc. in Biology, is mede-eigenaar en CTO bij NaturalGIS dat is gevestigd in Évora, Portugal.

{{<content-end >}}
