---
draft: 'true'

---
# De Processing Toolbox gebruiken om de classificatie van sneeuw te automatiseren
Snowy Hydro Limited (SHL) is een piek electriciteitsgenerator gevestigd in de Snowy Mountains van New South Wales, Australië. Ondanks het bezit van een variëteit aan generatoren door het gehele land, is Snowy Hydro Limited het meest bekend door het beheren van een iconisch stukje Australische infrastructuur, het Snowy Mountains Hydro Electric Scheme.

Het Snowy Mountains Hydro Electric Scheme, is mogelijk door seizoensgebonden sneeuwval in het berggebied van New South Wales. Water van de gesmolten lentesneeuw wordt gebruikt om elektriciteit te genereren, bestemd voor piekvragen door het nationale elektriciteitsmarkt, terwijl ook water wordt omgeleid naar gebieden in het drogere binnenland van zuidoost Australië voor irrigatie en landbouw.

Classificeren van het sneeuwdek gedurende de wintermaanden stelt SHL in staat om de levenscyclus te monitoren van het met sneeuw bedekte gebied, bedekte gebieden te archiveren voor de historie, en statistieken van bedekking te verschaffen aan de hydrografische serviceteams voor wateropbrengst en voorspellingen voor opslag.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Achtergrond
Elk jaar gedurende de wintermaanden (1 juni tot en met 31 oktober) verzamelt SHL zoveel mogelijk vrije afbeeldingen als mogelijk van de MODIS Terra (EOS AM) satelliet. Deze afbeeldingen worden dan geïmporteerd in een algoritme dat bekend is als de Normalised Difference Snow Index (NDSI), wat wordt gebruikt om aan te geven waar sneeuw aanwezig is. Hoewel dit algoritme niet uniek is voor één bepaalde sensor, werd het instrument MODIS gekozen vanwege zijn nauwkeurige ruimtelijke resolutie en dagelijks bedekking van het projectgebied (Kaart 1.1 Sneeuwwateropvang).
## Doel
Het doel van dit project is om de werkstroom voor NDSI te automatiseren als een model in de Toolbox van QGIS Processing. De vereiste uitvoer is een vectorpolygoon die het met sneeuw bedekte bereik weergeeft binnen de sneeuwwateropvang, met daarnaast de beschrijving van het totale bedekte gebied in vierkante kilometers.
## Methode
Het algoritme NDSI zelf is zeer eenvoudig (hieronder weergegeven in Formule 1.1 - Normalised Difference Snow Index (NDSI)) en de vervolgstappen die vereisen dat de bedekking met sneeuw wordt uitgenomen in een vectorindeling lenen zichzelf prima voor een model voor de Toolbox in Processing.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

Dit algoritme NDSI zal resultaten teruggeven tussen -1 en 1, waarin de drempel van sneeuw normaal gesproken ligt bij waarden groter dan 0.4. Een voorbeeld van de uitvoer van NDSI wordt hieronder weergegeven (Kaart 1.3 - uitvoer NDSI), naast een afbeelding met natuurlijke kleuren (Kaart 1.2 - MODIS ware kleuren) voor 13 juli 2014. Zoals op deze afbeeldingen kan worden gezien is de uitvoer van NDSI zeer goed in het verwijderen van met sneeuw bedekte gebieden uit andere typen landgebruik en wolken. Het kan echter gedeelten van grote waterlichamen ten onrechte classificeren als sneeuw, veroorzaakt dor het feit dat water absorptiekarakteristieken heeft in het gedeelte Bijna infrarood van het spectrum. Deze karakteristiek van de NDSI vereist, op enig moment, het gebruiken van een watermasker in het model.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

De uitvoer NDSI wordt gemaakt met behulp van een zeer eenvoudige bandkaart door gebruik te maken van de module \"r.mapcalculator\" in GRASS. Zodra het raster NDSI beschikbaar was, diende de NDSI-drempel van 0.4 te worden toegepast en dat zou resulteren in een booleaans raster dat de gebieden "Sneeuw" en "Geen sneeuw" weer zou geven. Een andere module van GRASS \"r.recode\" werd gebruikt om die classificatie te verkrijgen en produceerde het resultaat zoals hierboven weergegeven in Kaart 1.4 Opnieuw gecodeerde ‘sneeuw’ vs ‘geen sneeuw’.

Het opnieuw gecodeerde raster werd daarna geconverteerd naar een gegevensset voor een vectorpolygoon en de met sneeuw bedekte gebieden werden uitgenomen (hieronder weergegeven, Kaart 1.5 - Uitgenomen sneeuw). De met sneeuw bedekte gebieden werden hierna geclipt tot de Sneeuwwateropvang (hieronder weergegeven, Kaart 1.6 - Sneeuw binnen de SWO). Daarna werden de grote waterlichamen eruit genomen met een masker (hieronder weergegeven, Kaart 1.7 - Uiteindelijk met sneeuw bedekte gebied), en tenslotte werden de gebiedsstatistieken voor het met sneeuw bedekte gebied gegenereerd.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

De uitvoer van het model is een vectorpolygoon die het met sneeuw bedekte gebied binnen de sneeuwwateropvang weergeeft. De attributen van de polygoon omvatten het gebied dat wordt bedekt door sneeuw en het percentage van de opvang dat is bedekt. Het model in zijn geheel kan hieronder worden bekeken \"Afbeelding 1.1 - model Normalised Difference Snow Index (NDSI) Toolbox QGIS Processing\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## Resultaten/Conclusie
De Toolbox van QGIS Processing is een krachtige manier om een werkstroom te automatiseren, zoals deze classificatie van sneeuw. Het hierboven weergegeven model automatiseert met succes het proces van het classificeren van de sneeuw, en levert een GIS-gegevensset die gebruikt kan worden voor visualisatie en worden ingevoerd in volgende toepassingen voor statistieken. Het verwijdert met succes subjectieve gebruikersfouten die zijn geassocieerd met de eerder door SHL gebruikte methoden, terwijl een herhaaldelijk te gebruiken en consistent gereedschap voor classificeren wordt geleverd. Enkele seizoensresultaten kunnen hier worden bekeken.
### Auteur
Andrew Jeffrey is een GIS-analist bij Snowy Hydro Limited gevestigd in Cooma NSW, Australië. Hij promoveerde aan de Charles Sturt University in Wagga Wagga met een Bachelor of Science (Bsc) met als hoofdvak Spatial Information Systems in 2004. Gedurende zijn werk bij Snowy Hydro Limited is hij in staat geweest ruimtelijke ondersteuning te verlenen aan fantastische projecten zoals het experiment Cloud Seeding, en dagelijkse bewerkingen binnen de organisatie.
