---
draft: 'true'

---
# QGIS gebruiken om hotspot-gebieden voor services van biodiversiteit ecosysteem (HABEaS) in kaart te brengen
HABEaS \-\-- Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Het belangrijkste doel van dit platform is om gratis toegang te verschaffen tot een brede variëteit aan gegevens van services voor biodiversiteit en ecosysteem voor het mediterrane bassin dat was verspreid over een aantal publieke en private entiteiten. Tegenwoordig bestrijkt HABEaS WebGIS het zuiden van Portugal, maar eind 2012/begin 2013 zal het zijn uitgebreid tot het noorden van Portugal en ook tot het Tuzla Canton in Bosnia & Herzegovina. Op de lange termijn willen we dit gereedschap uitbreiden tot het gehele mediterrane bassin.

![](./images/portugal_lisbon1.jpg){.align-right}

Omdat het belangrijkste doel van dit gereedschap is om vrije en eenvoudige toegang te bieden tot informatie over services voor biodiversiteit en ecosysteem, besloten we om alleen gratis en open source software te gebruiken, die iedereen kan gebruiken, ongeacht hun locatie of financiële beperkingen. De website HABEaS WebGIS wordt gehost op een server die Debian Linux uitvoert en werd ontwikkeld met Drupal CMS. PostgreSQL/PostGIS werd gebruikt om de gegevens op te slaan en QGIS werd gebruikt om de GIS, die we uit verschillende entiteiten verkregen, te verwerken en te analyseren. We gebruikten zowel de eigen gereedschappen van QGIS als gereedschappen van GRASS GIS en SAGA GIS via de plug-in van GRASS en de SEXTANTE Toolbox.

![](./images/portugal_lisbon2.jpg){.align-right}

De geografische informatie die is opgenomen in HABEaS wordt ook gebruikt door het WWF om ondersteuning te verschaffen voor het identificeren van High Conservation Value Forests (HCVF) in het zuiden van Portugal, wat een verplichte stap is voor landeigenaren die willen dat hun bossen een Forest Stewardship Council (FSC)-certificaat ontvangen.

![](./images/portugal_lisbon3.jpg){.align-right}

We gebruikten Grafische modellen bouwen van SEXTANTE om een script te maken dat alle lagen van HABEaS met de grenzen van het eigendom kruist om te bepalen welke waarden voor behoud voorkomen in elk eigendom.  Met behulp van hetzelfde gereedschap waren we ook in staat een script te maken dat automatisch de hoeveelheid koolmonoxide berekent die momenteel wordt opgeslagen in elk eigendom.

![](./images/portugal_lisbon4.jpg){.align-right}
## Conclusies
QGIS is eenvoudig te gebruiken en heeft zeer krachtige mogelijkheden voor geo-verwerking. De integratie van gereedschappen voor GRASS GIS en SAGA GIS door middle van de SEXTANTE Toolbox maakten het ons mogelijk een aantal complexe ruimtelijke analyses uit te voeren en om ze te stroomlijnen met behulp van Grafische modellen bouwen van SEXTANTE. Het was ook zeer eenvoudig om kaarten van hoge kwaliteit te maken met behulp van de nieuwe printvormgeving en ze te exporteren in de indeling SVG voor nadere bewerking met Inkscape, wat een krachtig open source bewerkingsprogramma voor vectorafbeeldingen is.

In het algemeen zijn onze ervaringen met QGIS heel positief geweest; de software draait gladjes en de gemeenschap is zeer actief en ondersteunend. Gerapporteerde problemen worden gewoonlijk snel nadat ze door gebruikers zijn gerapporteerd verholpen en ontwikkelaars van QGIS zijn altijd bereid om te luisteren naar de wensen en suggesties van "eindgebruikers".
## Auteur
![Filipe Dias](./images/portugal_lisbonaut.jpg){.align-left height="200px"}

Filipe Dias is een PhD-student aan het Center for Applied Ecology (Instituto Superior de Agronomia, Techinical University van Lissabon) en consultant van het Mediterranean Programme van het Wereld Natuur Fonds (WNF).
