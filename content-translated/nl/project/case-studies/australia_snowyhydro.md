---
HasBanner: false
archived: true
date: 2014-08-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/australia_snowyhydro1.jpg
title: De Processing Toolbox gebruiken om de classificatie van sneeuw te automatiseren
type: case-study

---
{{<content-start >}}
# De Processing Toolbox gebruiken om de classificatie van sneeuw te automatiseren
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>August 01, 2014</span>
</p>

Snowy Hydro Limited (SHL) is een piek electriciteitsgenerator gevestigd in de Snowy Mountains van New South Wales, Australië. Ondanks het bezit van een variëteit aan generatoren door het gehele land, is Snowy Hydro Limited het meest bekend door het beheren van een iconisch stukje Australische infrastructuur, het Snowy Mountains Hydro Electric Scheme.

Het Snowy Mountains Hydro Electric Scheme, is mogelijk door seizoensgebonden sneeuwval in het berggebied van New South Wales. Water van de gesmolten lentesneeuw wordt gebruikt om elektriciteit te genereren, bestemd voor piekvragen door het nationale elektriciteitsmarkt, terwijl ook water wordt omgeleid naar gebieden in het drogere binnenland van zuidoost Australië voor irrigatie en landbouw.

Classificeren van het sneeuwdek gedurende de wintermaanden stelt SHL in staat om de levenscyclus te monitoren van het met sneeuw bedekte gebied, bedekte gebieden te archiveren voor de historie, en statistieken van bedekking te verschaffen aan de hydrografische serviceteams voor wateropbrengst en voorspellingen voor opslag.

<figure>
<img src="../images/australia_snowyhydro1.jpg" class="align-center" height="43400" alt="images/australia_snowyhydro1.jpg" />
<figcaption>Map 1.1 Snowy Water Catchment Map</figcaption>
</figure>

## Achtergrond
Elk jaar gedurende de wintermaanden (1 juni tot en met 31 oktober) verzamelt SHL zoveel mogelijk vrije afbeeldingen als mogelijk van de MODIS Terra (EOS AM) satelliet. Deze afbeeldingen worden dan geïmporteerd in een algoritme dat bekend is als de Normalised Difference Snow Index (NDSI), wat wordt gebruikt om aan te geven waar sneeuw aanwezig is. Hoewel dit algoritme niet uniek is voor één bepaalde sensor, werd het instrument MODIS gekozen vanwege zijn nauwkeurige ruimtelijke resolutie en dagelijks bedekking van het projectgebied (Kaart 1.1 Sneeuwwateropvang).
## Doel
Het doel van dit project is om de werkstroom voor NDSI te automatiseren als een model in de Toolbox van QGIS Processing. De vereiste uitvoer is een vectorpolygoon die het met sneeuw bedekte bereik weergeeft binnen de sneeuwwateropvang, met daarnaast de beschrijving van het totale bedekte gebied in vierkante kilometers.
## Methode
Het algoritme NDSI zelf is zeer eenvoudig (hieronder weergegeven in Formule 1.1 - Normalised Difference Snow Index (NDSI)) en de vervolgstappen die vereisen dat de bedekking met sneeuw wordt uitgenomen in een vectorindeling lenen zichzelf prima voor een model voor de Toolbox in Processing.

<figure>
<img src="../images/australia_snowyhydro8.png" alt="australia_snowyhydro8.png" />
<figcaption>Formula 1.1 - Normalised Difference Snow Index (NDSI)</figcaption>
</figure>

Dit algoritme NDSI zal resultaten teruggeven tussen -1 en 1, waarin de drempel van sneeuw normaal gesproken ligt bij waarden groter dan 0.4. Een voorbeeld van de uitvoer van NDSI wordt hieronder weergegeven (Kaart 1.3 - uitvoer NDSI), naast een afbeelding met natuurlijke kleuren (Kaart 1.2 - MODIS ware kleuren) voor 13 juli 2014. Zoals op deze afbeeldingen kan worden gezien is de uitvoer van NDSI zeer goed in het verwijderen van met sneeuw bedekte gebieden uit andere typen landgebruik en wolken. Het kan echter gedeelten van grote waterlichamen ten onrechte classificeren als sneeuw, veroorzaakt dor het feit dat water absorptiekarakteristieken heeft in het gedeelte Bijna infrarood van het spectrum. Deze karakteristiek van de NDSI vereist, op enig moment, het gebruiken van een watermasker in het model.

<figure>
<img src="../images/australia_snowyhydro2.jpg" class="align-left" width="300" alt="australia_snowyhydro2.jpg" />
<figcaption>Map 1.2 - MODIS true colour</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro3.jpg" class="align-center" width="300" alt="australia_snowyhydro3.jpg" />
<figcaption>Map 1.3 - NDSI output</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro4.jpg" class="align-left" width="300" alt="australia_snowyhydro4.jpg" />
<figcaption>Map 1.4 - Recoded "Snow" vs "Non snow"</figcaption>
</figure>

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

<figure>
<img src="../images/australia_snowyhydro5.jpg" class="align-left" width="300" alt="australia_snowyhydro5.jpg" />
<figcaption>Map 1.5 - Extracted Snow</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro6.jpg" class="align-center" width="300" alt="australia_snowyhydro6.jpg" />
<figcaption>Map 1.6 - Snow inside the SWC</figcaption>
</figure>

<figure>
<img src="../images/australia_snowyhydro7.jpg" class="align-left" width="300" alt="australia_snowyhydro7.jpg" />
<figcaption>Map 1.7 - Final snow covered area</figcaption>
</figure>

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

<figure>
<img src="../images/australia_snowyhydro.png" class="align-center" width="600" alt="australia_snowyhydro.png" />
<figcaption>Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model</figcaption>
</figure>

## Resultaten/Conclusie
De Toolbox van QGIS Processing is een krachtige manier om een werkstroom te automatiseren, zoals deze classificatie van sneeuw. Het hierboven weergegeven model automatiseert met succes het proces van het classificeren van de sneeuw, en levert een GIS-gegevensset die gebruikt kan worden voor visualisatie en worden ingevoerd in volgende toepassingen voor statistieken. Het verwijdert met succes subjectieve gebruikersfouten die zijn geassocieerd met de eerder door SHL gebruikte methoden, terwijl een herhaaldelijk te gebruiken en consistent gereedschap voor classificeren wordt geleverd. Enkele seizoensresultaten kunnen hier worden bekeken.
### Auteur
Andrew Jeffrey is een GIS-analist bij Snowy Hydro Limited gevestigd in Cooma NSW, Australië. Hij promoveerde aan de Charles Sturt University in Wagga Wagga met een Bachelor of Science (Bsc) met als hoofdvak Spatial Information Systems in 2004. Gedurende zijn werk bij Snowy Hydro Limited is hij in staat geweest ruimtelijke ondersteuning te verlenen aan fantastische projecten zoals het experiment Cloud Seeding, en dagelijkse bewerkingen binnen de organisatie.

{{<content-end >}}
