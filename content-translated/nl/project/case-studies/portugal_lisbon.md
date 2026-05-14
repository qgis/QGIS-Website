---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: QGIS gebruiken om hotspot-gebieden voor services van biodiversiteit ecosysteem
  (HABEaS) in kaart te brengen
type: case-study

---
{{<content-start >}}
# QGIS gebruiken om hotspot-gebieden voor services van biodiversiteit ecosysteem (HABEaS) in kaart te brengen
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Het belangrijkste doel van dit platform is om gratis toegang te verschaffen tot een brede variëteit aan gegevens van services voor biodiversiteit en ecosysteem voor het mediterrane bassin dat was verspreid over een aantal publieke en private entiteiten. Tegenwoordig bestrijkt HABEaS WebGIS het zuiden van Portugal, maar eind 2012/begin 2013 zal het zijn uitgebreid tot het noorden van Portugal en ook tot het Tuzla Canton in Bosnia & Herzegovina. Op de lange termijn willen we dit gereedschap uitbreiden tot het gehele mediterrane bassin.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

De geografische informatie die is opgenomen in HABEaS wordt ook gebruikt door het WWF om ondersteuning te verschaffen voor het identificeren van High Conservation Value Forests (HCVF) in het zuiden van Portugal, wat een verplichte stap is voor landeigenaren die willen dat hun bossen een Forest Stewardship Council (FSC)-certificaat ontvangen.

![](../images/portugal_lisbon3.jpg)

We gebruikten Grafische modellen bouwen van SEXTANTE om een script te maken dat alle lagen van HABEaS met de grenzen van het eigendom kruist om te bepalen welke waarden voor behoud voorkomen in elk eigendom.  Met behulp van hetzelfde gereedschap waren we ook in staat een script te maken dat automatisch de hoeveelheid koolmonoxide berekent die momenteel wordt opgeslagen in elk eigendom.

![](../images/portugal_lisbon4.jpg)
## Conclusies
QGIS is eenvoudig te gebruiken en heeft zeer krachtige mogelijkheden voor geo-verwerking. De integratie van gereedschappen voor GRASS GIS en SAGA GIS door middle van de SEXTANTE Toolbox maakten het ons mogelijk een aantal complexe ruimtelijke analyses uit te voeren en om ze te stroomlijnen met behulp van Grafische modellen bouwen van SEXTANTE. Het was ook zeer eenvoudig om kaarten van hoge kwaliteit te maken met behulp van de nieuwe printvormgeving en ze te exporteren in de indeling SVG voor nadere bewerking met Inkscape, wat een krachtig open source bewerkingsprogramma voor vectorafbeeldingen is.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Auteur
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias is een PhD-student aan het Center for Applied Ecology (Instituto Superior de Agronomia, Techinical University van Lissabon) en consultant van het Mediterranean Programme van het Wereld Natuur Fonds (WNF).

{{<content-end >}}
