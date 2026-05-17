---
HasBanner: false
archived: true
date: 2013-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/canada_brunswick1.jpg
title: Fundy Footpath Trail-kaart maken met QGIS
type: case-study

---
{{<content-start >}}
# Fundy Footpath Trail-kaart maken met QGIS
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 januari 2013</span>
</p>

![](../images/canada_brunswick1.jpg)

Het Fundy Footpath  is een wandelpad in de wildernis, gesitueerd langs de kust van Fundy van New Brunswick, Canada. Het is markant lid van de [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) en verbonden aan de [NB Trails Council Inc.](http://www.sentiernbtrail.com/) en de Trans Canada Trail. Het Footpath neemt wandelaars mee langs het langs de kust gelegen Acadian Forest, thuis van de hoogste getijden, oudste groeiende wouden, en verscheidene bijzondere en unieke typen flora en fauna.

Het pad werd gemaakt, wordt onderhouden, en gepromoot door een groep vrijwilligers die bekend staan als de Fundy Hiking Trail Association Inc. (FHTA)(1975). Als een non-profit organisatie werft de FHTA fondsen voor zijn activiteiten door de verkoop van gidsen die een kaart van het pad bevat. In 2011 benaderde ik de FHTA om vrijwillig de officiële kaart voor het pad bij te werken. Als een vrijwilliger die een kaart maakt voor een non-profit organisatie voldoet QGIS zowel als gereedschap voor het bewerken van gegevens en voor de uiteindelijk lay-out van de kaart. Door de inspanningen van mijzelf en leden van de FHTA wordt de nieuwe officiële kaart voor het Fundy Footpath, opgenomen in de gids, van begin tot einde gemaakt met QGIS.

<figure>
<img src="../images/canada_brunswick2.jpg" class="align-right" alt="canada_brunswick2.jpg" />
<figcaption>QGIS Plug-in GPS Tools voor verzamelen van gegevens</figcaption>
</figure>

## Het project
Het proces voor het maken van de nieuwe kaart voor het Fundy Footpath met QGIS kan worden opgedeeld in drie verschillende delen:
- Verzamelen van gegevens.
- Bewerken en voorbereiden van de gegevens.
- Maken van de kaart

Gegevens werden verzameld met zowel draagbare GPS-apparaten als uit verschillende gratis bronnen met gegevens. Gegevens voor het pad (bijv. centrumlijn van het pad, locaties van kampeersites en oversteekplaatsen voor getijden) werden verzameld met een Garmin GPSMap 60CSX. Deze gegevens werden daarna overgebracht vanaf de GPS naar de indeling shapefile in QGIS met behulp van de GPS-plug-in. Vrije gegevens in vectorindelingen werden verkregen van de website van [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) en vanaf [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

<figure>
<img src="../images/canada_brunswick3.jpg" class="align-right" alt="canada_brunswick3.jpg" />
<figcaption>Maken van de kaart van het voetpad in QGIS</figcaption>
</figure>

De volgende gereedschappen binnen QGIS werden gebruikt om specifieke taken te volbrengen bij het voorbereiden van de gegevens om te gebruiken in de uiteindelijke kaart:
- De met GPS verzamelde gegevens werden opgeschoond met behulp van de werkbalk Bewerken.
- De van NRCan en SNB verkregen vectorgegevens werden samengevoegd, bevraagd, en geclipt voor het uiteindelijk gebied van de kaart met behulp van de gereedschappen voor vectoren.
- Een komma-gescheiden bestand, verkregen van SNB, werd geïmporteerd in QGIS als een puntlaag met behulp van de plug-in Add Delimited Text Layer, de plug-in Interpolation werd gebruikt om een hoogteraster te maken dat daarna werd gebruikt om een raster met schaduw voor de heuvels en hoogte-contourenlaag te maken met de plug-in GDAL rastergereedschappen.

<figure>
<img src="../images/canada_brunswick4.jpg" class="align-right" alt="canada_brunswick4.jpg" />
<figcaption>Kaart voetpad in de Printvormgeving</figcaption>
</figure>

Als de vereiste gegevens voor het maken van de kaart eenmaal zijn samengesteld en in een bruikbare indeling, werd het maken van de uiteindelijke kaart gestart. Gegevens werden gesymboliseerd en gelabeld met het dialoogvenster voor de eigenschappen voor symboliseren en gelabeld met QGIS’s zeer functionele labeling om de wandelkaart te maken. Toen labels en symbolisatie eenmaal op hun plaats waren, werd het gereedschap printvormgeving uitgevoerd om de lay-out te maken. Het was zeer eenvoudig om handige kaartelementen, zoals een aangepaste noordpijl en een hoogteprofiel toe te voegen in de Printvormgeving. Twee lay-outs werden gemaakt, omdat het een dubbelzijdige kaart moest worden. Toen beide lay-outs eenmaal waren gemaakt, werden ze geëxporteerd als PDF-bestanden en verzonden naar de printers.
## Conclusie
De wandelkaart werd afgedrukt op zwaar waterproof papier, gevouwen en ingevoegd aan de achterzijde van de nieuwe uitgave van het Fundy Footpath Hiker’s Guide Book. QGIS was de beste en functioneelste keuze voor het maken van deze kaart. Vanwege de gratis software was de prijs juist voor een vrijwilliger om een kaart te maken voor een non-profitorganisatie. Maar het echte voordeel van QGIS was dat het alle functionaliteiten en vereiste gereedschappen had om een goed bruikbare en gedetailleerde wandelkaart te maken van begin tot einde. Ik zou QGIS van harte aanbevelen aan zowel ervaren als beginnende gebruikers van GIS.

<figure>
<img src="../images/canada_brunswick5.jpg" class="align-right" alt="canada_brunswick5.jpg" />
<figcaption>De uiteindelijke kaart van het Fundy Footpath met bijbehorende gids</figcaption>
</figure>

## Links
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Auteur
<figure>
<img src="../images/canada_brunswickaut.jpg" class="align-left" height="200" alt="canada_brunswickaut.jpg" />
<figcaption>Jarrett Totton</figcaption>
</figure>

Dit artikel werd bijgedragen door Jarrett Totton in januari 2013. Jarrett is een GIS Technologist, woonachtig in Alberta, Canada.

{{<content-end >}}
