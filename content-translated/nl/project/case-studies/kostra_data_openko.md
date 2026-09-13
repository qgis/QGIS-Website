---
HasBanner: false
archived: false
date: 2026-03-23
draft: false
featured: true
section: project
sidebar: true
thumbnail: images/thumbnail_openko.webp
title: Vrije KOSTRA-data op openko.de
type: case-study

---
{{<content-start >}}
# Vrije KOSTRA-data op openko.de
Dit artikel presenteert het project [openko.de](https://www.openko.de/), dat **KOSTRA-data op een gestructureerde en gebruiksvriendelijke manier, zonder kosten** verschaft. De inhoud van het platform werd grotendeels geïmplementeerd met QGIS.
## Over KOSTRA
KOSTRA (ook wel bekend als KOSTRA-DWD) is een catalogus voor zware neerslag, gepubliceerd door de Duitse Meteorologische Service ("Deutscher Wetterdienst" in Duitsland, DWD). Het acroniem staat voor *Coordinated Heavy Precipitation Regionalization and Evaluation* ("Gecoördineerde zware neerslag regionalisatie en evaluatie" ) ("Koordinierte Starkniederschlagsregionalisierung und -auswertung" in het Duits).

De catalogus bevat rastergegevens over neerslaghoogten en intensiteit, afhankelijk van de duur van de neerslag en terugkeerperiode. De gegevensset bedekt het gehele territorium van Duitsland.

Decennia lang waren gegevens van KOSTRA alleen tegen betaling beschikbaar via de DWD. Volgend op een amendement op de wet voor de DWD in 2017, werden deze gegevenssets vrij toegankelijk.

Hoewel de gegevens beschikbaar zijn, zowel zonder als met ruimtelijke referentie, is de structuur ervan niet bijzonder gebruiksvriendelijk en vereist deze gevorderde gebruikers. Goed gestructureerde PDF-tabellen die een overzicht geven van de neerslagwaarden zijn slechts tegen kosten beschikbaar, momenteel € 70 (netto) per rastercel.
## Wat is openko.de?
Vanaf 2022 heeft de website openko.de meer dan **21.000 alternatieve PDF-tabellen en kaarten** verschaft om gratis te downloaden. In aanvulling op de tabulaire gegevens bevat elke pdf een kaart die de locatie van de corresponderende rastercel weergeeft.

![Voorbeeld uittreksel van een KOSTRA PDF-tabel, inclusief een kaart](../images/screenshot_pdf_example_table_and_map.webp)

Navigeren naar de toepasselijke rastercel van KOSTRA wordt verschaft via een webkaart ([Interactieve kaart KOSTRA-DWD-2020](https://www.openko.de/kostra-dwd-2020-tabellen-kostenlos-herunterladen/)) met geïntegreerd zoeken op adres (Klik op "Interaktive Karte KOSTRA-DWD-2020" om naar de kaart te gaan).

![Selectie van rastercellen via webkaart](../images/screenshot_qgis2web_raster_selection.webp)

Het project is bijzonder goed ontvangen. De gebruikers ervan zijn over het algemeen adviesbureaus voor bouwkunde, constructiebedrijven en openbare autoriteiten die gegevens van KOSTRA nodig hebben voor het ontwerpen en verifiëren van hydraulische infrastructuur. Ook universiteiten gebruiken openko.de om studenten met gemakkelijke toegang gegevens van KOSTRA te laten gebruiken.

Het succes van het project kan ook kwantitatief worden uitgedrukt: vanaf de start in juli 2022 tot en met maart 2026, zijn meer dan **200.000 tabellen gedownload**. Tegen de kosten van € 70 per tabel (de prijs van de DWD), correspondeert dat met een **totale waarde van meer dan 14.000.000 euro**!
## Hoe openko.de werd gemaakt en de rol van QGIS
De tabellen werden gemaakt met **QGIS Printomgeving** en demonstreren hoe standaardfunctionaliteit van QGIS ruwe gegevens kan transformeren naar goed gestructureerde en visueel aantrekkelijke uitvoer.

Voor gemakkelijker verwerken in QGIS werden tabellen van neerslag eerst samengevoegd in een enkel CSV-bestand met een script van Python. Het resultaat is een gegevensset van meer dan 45 MB, **dat 351.759 rijen en meer dan 10.2 miljoen gegevensitems bevat**.

Elke rij bevat een ID voor de rastercel, wat het mogelijk maakt de gegevens overeenkomstig toe te wijzen. In de lay-out worden neerslagwaarden en informatie over onwaarschijnlijkheid gecombineerd in tabellen.

Hoewel deze benadering goed werkte met de kleinere gegevensset KOSTRA-DWD-2010, traden problemen bij de uitvoering op met KOSTRA-DWD-2020. Genereren van de **atlas** vereiste een hele hoge verwerkingstijd, omdat gegevens voor elke rastercel opnieuw moesten worden geladen. Een ruwe schatting gaf aan dat het maken van ongeveer 16.000 tabellen zo rond de 11 dagen zou gaan duren.

De oplossing was eenvoudig: de gegevensset werd gesplitst in vier delen en tabellen werden tegelijkertijd gemaakt met vier parallel draaiende instanties van QGIS. Dat verkleinde de totale verwerkingstijd tot ongeveer een dag.

Aanvullende scripts voor Python werden ontwikkeld voor:
- Het maken van HTML-opgemaakte downloadpagina's, inclusief metadata, zoals gemeenten, federale staten en postcodes
- Het uploaden van voorbeeldafbeeldingen en PDF-bestanden via de WordPress API

De webkaart werd gemaakt met de [plug-in qgis2web](https://plugins.qgis.org/plugins/qgis2web/). Het bevat slechts twee twee lagen: een topografische basiskaart en het raster voor het raster.

Downloadlinks worden systematisch gemaakt, gebaseerd op ID's van rastercellen, wat het voor elk object mogelijk maakt een directe link te bevatten naar zijn corresponderende downloadpagina. Klikken op een rastercel opent een pop-up met de juiste link die naar de downloadpagina leidt.
## Databronnen
De volgende bronnen voor open data werden gebruikt:
- Gegevens van KOSTRA vanaf de DWD:<br />https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/
- Topografische basiskaart TopPlusOpen van het Federale Agentschap voor Cartografie en Geodesie ("Bundesamt für Kartographie und Geodäsie" in het Duits):<br />https://sgx.geodatenzentrum.de/web_public/gdz/datenquellen/Datenquellen_TopPlusOpen.html

## Outlook
Een REST API ([REST API](https://www.openko.de/rest-api-kostra-dwd-2020/)) is recent ontwikkeld om toegang te verlenen tot gegevens van KOSTRA. Het is momenteel beschikbaar als een bètaversie en werkt betrouwbaar.

De officiële uitgave is gepland voor juli 2026 om samen te vallen met het vierjarig bestaan van openko.de. Deze uitgave zal deel uitmaken van een volledige herziening van de website, die, naast de bestaande uitvoer in pdf, ook **aanvullende gegevensindelingen zal introduceren**.
## Auteur
![Alexander Altnöder](../images/alexander_altnoeder.webp)

Alexander Altnöder is een bouwkunde-geoloog, gevestigd in het Roergebied, Duitsland. Hij werkt extensief met GIS en programmeren, zowel professioneel als privé.

{{<content-end >}}
