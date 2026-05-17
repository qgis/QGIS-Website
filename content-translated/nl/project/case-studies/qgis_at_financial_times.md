---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: project
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: Gebruiken van QGIS door het Financial Times Graphics Team
type: case-study

---
{{<content-start >}}
# Gebruiken van QGIS door het Financial Times Graphics Team
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 april 2016</span>
</p>

## Interview met Steven Bernard (Interactive Design Editor)
Steven is een Interactive Design Editor bij de Financial Times. U kunt hem vinden op [Twitter](https://twitter.com/sdbernard). Hij publiceert ook nuttige [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) voor bepaalde cartografische taken in QGIS.

**QGIS**: Steven, wat is de naam van het team waarmee u werkt bij FT? Kunt u ons wat achtergrondinformatie geven over wat uw team bij FT doet?

**Steven**: Ons team bevindt zich op dit moment in een transitieperiode, we hebben een nieuwe visualisatie-editor voor gegevens, Alan Smith OBE (eerder van de ONS) die de dingen enigszins opschud en één enkel team voor de graphics samenstelt. Traditioneel hadden we een team voor webgraphics en een team voor afdrukgraphics. Het team voor afdruk zou verantwoordelijk zijn voor alle graphics voor kranten als ook voor het maken van web-vriendelijke versies daravan. Mijn team was verantwoordelijk voor alle inhoud die allene op het web te zien was, als ook voor de nauwe samenwerking met de interactieve producers/ontwikkelaars bij het ontwerpen van interactieve graphics.

Het nieuw gevormde team zal een kruisbestuiving  van vaardigheden tussen de verschillende media mogelijk maken.

Alan heeft één enkele digitale werkstroom voor ons team geïntroduceerd, inclusief het gebruiken van d3 om een grotere woordenschat voor afbeelding te maken en het terugdringen van de benodigde tijd om visualisaties te maken.

![](../images/ft_europe_migration_balkan-route.png)

*Voorbeeld: Stroom van migranten. Route over de westelijke Balkan.*

**QGIS**: Hoeveel mensen werken er in uw team?

**Steven**: Inclusief all ontwerpers, ontwikkelaars, producers en statistici, hebben we een team van 24

**QGIS**: Wat is uw specifieke rol binnen het team?

**Steven**: We zijn een multi-disciplinaire afdeling dus ik heb niet echt een specifieke rol. Mijn rol omvat het produceren van responsieve ontwerpen voor interactieve afbeeldingen als ook het uitvoeren van ontwikkeling aan het frontend voor de wat minder gecompliceerde interactieven (bijv. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). Ik maak ook standaard aan het nieuws gerelateerde diagrammen en kaarten op dagelijkse basis. De laatste twee jaar heb ik me geconcentreerd op de ontwikkeling van hetgeen we op het gebied van cartografie bieden aan de FT. QGIS is belangrijk geweest voor de manier waarop we kaarten maken hebben gewijzigd, en in samenwerking met andere gereedschappen, zoals Blender, hebben we ons geholpen creatiever te zijn met betrekking tot de wijze waarop we kaarten benaderen.

![](../images/ft_nigeria-migration_animation.gif)

*Voorbeeld: Animatie van Dora\'s reis van Nigeria naar Sicilië - één van de elk jaar duizenden verhandelde vrouwen.*

**QGIS**: Kunt u ons iets over uzelf vertellen? Wat is uw achtergrond qua onderwijs? Wat deed u voordat u deel uitmaakte van het data visualisatie team bij FT?

![](../images/ft_gotthard-tunnel.png)

*Voorbeeld: Gotthard spoor- en wegtunnel in de Zwitserse Alpen.*

**Steven**: Ik ben van oorsprong getraind als wetenschappelijk illustrator. "Wat is dat dan?" hoor ik u vragen. Het omvat het maken van illustraties voor medische bladen, publicaties over de geschiedenis van de natuur, alles waarbij je probeert visueel informatie te verschaffen waar een foto dat niet kan. Denk aan diagrammen die het menselijk circulatiesysteem weergeven, of het weergeven van een procedure om een gebroken bot te repareren. Helaas was er niet veel werk op dat terrein toen ik de universiteit verliet en ik kwam eigenlijk direct bij mijn werk voor de FT terecht. Ik ben altijd nogal goed geweest in rekenen, wat volgens mij wel belangrijk is bij het werken met visualisaties van gegevens. Het heeft me zeker ook bij het coderen geholpen.

**QGIS**: Hoe ontdekte u QGIS?

**Steven**: Ik kwam QGIS in 2013 tegen toen we werkten aan een [project voor het in kaart brengen van de etniciteit in het Midden Oosten](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We gebruikten het om kaarten, die waren gemaakt door een professor aan de Columbia University, te voorzien van geoverwijzingen. Eerst vond ik het nogal beangstigend om het gereedschap Object toevoegen te gebruiken, waarschijnlijk omdat het in niets leek op wat ik had gebruikt in Adobe Illustrator in de 17 jaar daarvoor! Ik vond het ook frustrerend dat je dingen tweemaal moest opslaan, eenmaal bij het bewerken van het shapefile, en dan nogmaals om het project op te slaan. Dit kwam echter door onervarenheid met het programma en op het eind deed het precies wat we nodig hadden, wat het maken van shapefiles was die we dan konden toevoegen aan een basiskaart van Mapbox.

**QGIS**: Wat is de rol van QGIS binnen uw normale werkstromen?

**Steven**: QGIS maakt nu een integraal deel uit van onze werkstroom voor het maken van kaarten. Ik gebruik geen ander gereedschap voor GIS om onze kaarten te maken. Hoewel een aantal leden van ons team ook Map Publisher gebruiken, omdat ze zich beter voelen bij Adobe Illustrator. Ik zou zeggen dat ongeveer 80% van onze kaarten nu wordt gemaakt in QGIS.

![](../images/ft_blm-federal-land-map.png)

*Voorbeeld: Openbaar toegankelijk land in the VS.*

**QGIS**: Welke andere programma's gebruikt u naast QGIS en hoe combineert u deze?

**Steven**: Als het een rechttoe rechtaan kaart is wordt 95% van het werk gedaan in QGIS, waarna het wordt afgewerkt in Adobe Illustrator.

Als ik werk aan een kaart met reliëf, dan is het proces veel complexer. Ik haal DEM-bestanden op van Nasa Earth Explorer, en plaats die binnen QGIS om ze op grootte te maken. Ik doe de verkleinde DEM dan in Blender om een #D rendering te maken. Als ik een satellietoverlay gebruk voor de schaduw op de heuvels, dan download ik een afbeelding van BlueMarble vanaf Nasa en plaats die ook in Blender. De geëxporteerde rendering uit Blender wordt dan teruggeplaatst in QGIS om te dienen als achtergrondlaag. Ik pas soms, indien nodig, eerst nog wat aan in Photoshop.

Voor responsieve kaarten zoals die in de [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), gebruikte ik alle bovenstaande programma's, maar de uiteindelijke stap was het gebruiken van een openbron-script voor Adobe Illustrator, dat werd ontwikkeld door de New York Times’ Archie Tse. Dit maakt het voor mij mogelijk responsieve versies van mijn kaarten te maken die op alle apparaten werken.

Een ander programma dat nuttig is is Google My Maps wat het voor journalisten over d egehele wereld mogelijk maakt locaties op een kaart te markeren die we dan kunnen downloaden als een KMZ-bestand en die we rechtsreeks kunnen importeren in QGIS.

Het laatste programma dat ik gebruik is is Adobe After Effects omdat ik recent ben begonnen met het animeren van mijnkaarten om de gebruiker mee te nemen op reis. Zoals recent gebruikt in de serie Land Rush:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Gebruikt u andere ruimtelijke programma's of GIS naast QGIS, en zo ja, welke?

**Steven**: Voor mij alleen QGIS, maar zoals eerder gezegd gebruiken sommige van mijn collega's ook Map Publisher.

![](../images/ft_isis-air-strikes_febupdate.png)

*Voorbeeld: Aanvallen op Syrië in februari 2016.*

**QGIS**: Kunt u de sterke en zwakte punten van QGIS beschrijven met betrekking tot de taken die u moet uitvoeren?

**Steven**: Toen ik QGIS voor het eerst gebruikte, zag ik het als een programma voor specialisten, geschikt om alleen specifieke taken uit te voeren. Ik zag het echt niet als een programma voor productie. Eind 2014 woonden twee van mijn collega's een cursus voor QGIS bij die werd gegeven door Alasdair Rae aan de Sheffield University. Zij waren beide zeer enthousiast over hoe goed QGIS was, dus moest ik ook tot de conclusie komen dat het een programma was dat kon worden gebruikt om al onze kaarten te maken.

Binnen twee weken was ik er van overtuigd dat het dat ook zou kunnen. Het belangrijkste argument was de mogelijkheid tot het instellen van stijlen voor alles inclusief stijlen voor op zoomniveau voor kaarten op straatniveau.

Ik heb een systeem ingesteld waar we sets van bladen van Google hebben met kolommen voor naam, lat, long, pictogram voor markering, dikte voor lettertype, grootte voor lettertype en of de markering moet worden weergegeven of niet.

Het pictogram voor de markering is een keuzelijst die is gekoppeld aan een tabel met vLookUp die alle details voor die markering invult.

Alles wat ik hoef te doen is de CSV te downloaden, die importeren in QGIS, een stijl toe te passen en ik heb een kaart die al voor 95% klaar is.

Ik kan echter eerlijk gezegd geen zwak punt benoemen. Er zijn een aantal dingen die ik zou willen zien of zou willen doen, maar dat zie ik niet als zwak punt, maar als een ontbrekende mogelijkheid.

![](../images/ft_chinaMigration.png)

*Voorbeeld: Stedelijke aantrekkingskracht en migratie in China.*

**QGIS**: Wat zijn de concepten of mogelijkheden waarvan u het meest houdt  in QGIS?

**Steven**: er zijn talrijke mogelijkheden die ik zou willen klassificeren als levensredders! Maar primair hebben Quick OSM en Georeferencer mij zo vaak gered, die zijn absoluut essentieel als deadlines nabij zijn. Wat, bij het werken voor een nieuwsorganisatie, bijna 90% van de tijd is.

![](../images/ft_china_henanGuangdong.png)

*Voorbeeld: Stedelijke aantrekkingskracht en migratie in China. Gedetailleerde weergaven*

**QGIS**: Welke mogelijkkheid of functionaliteit mist u het meest in QGIS? Heeft u een lijst met ontbrekende mogelijkheden die u zouden helpen als zij werden geïmplementeerd?

**Steven**: Een aantal dingen die ik graag zou zien in toekomstige versies zijn\…

ondersteuning voor Bezier-bogen, dat zou in het bijzonder nuttig zijn in combinatie met Georeferencer. Ik weet dat er een plug-in voor Spline is, maar die geeft niet het volledige beheer dat een Bezier-boog zou geven.

De mogelijkheid om afbeelding in grotere grootten op te slaan. Momenteel is de enige manier waarop ik een verkleining met geo-verwijzingen van een DEM-bestand kan maken is om het in Blender te doen. maar het is beperkt tot de grootte van je scherm. Als ik een 8000 pixel DEM-bestand inQGIS kon laden zou ik in staat zijn de verkleining te exporteren in ene grotere grootte dan mijn scherm om bijvoorbeeld in een HD-video te gebruiken.

**QGIS**: Als u bepaalde mogelijkheden ontbeert in QGIS, zie u zouden kunnen helpen - zou u overwegen om QGIS zelf te verbetern (met coderen in de bron van QGIS of met plug-ins van Python), of zou u overwegen om een ontwikelaar van QGIS in te huren om de ontbrekende mogelijkheid voor u te implementeren? Of zou u in plaats daarvan zoeken naar andere programma's om dat gat te vullen?

**Steven**: Ik heb zelf absoluut niet de nodige vaardigheden om het coderen te doen, Ik kan redelijk overweg met Javascript maar zou moeite hebben met Python. Ik zou graag een ontwikkelaar inhuren om de mogelijkheden geïmplementeerd te krijgen, maar ik ga niet over het beheren van budgetten, dus zou ik andere programma's gebruiken om dit op te lossen.

![](../images/ft_us_broadband_internet_subscription.png)

*Voorbeeld: Percentage van huishoudens met een breedband internetabonnement in de VS.*

**QGIS**: Laten we het eens hebben over de gebruikerservaring - het team van QGIS is zich ervan bewust dat er verscheidene plekken in de gebruikersinterface (dialoogvensters, panelen, etc.) zijn die aanzienlijk verbeterd zouden kunnen worden. Kunt u ons vertellen waar in de gebruikersinterface u het grootste potentieel voor een verbetering van die UI ziet?

**Steven**: Ik denk dat de belangrijkste gereedschappen goed zijn zoals ze zijn; als je het eenmaal weet, is het ook wel duidelijk. Eén ding dat ik echter wel een beetje frustrerend vind, is het zoeken van een plug-in als die eenmaal is geïnstalleerd. Zij maken ofwel hun eigen menu (MMQGIS), leven onder een van de bestaande menu's (Georeferencer) of maken hun eigen pictogram (threejs). Het zou handig zijn om een venster voor plug-ins te hebben waarin alle geïnstalleerde plug-ins staan. Ook dit is geen halszaak, maar het zou eenvoudiger zijn dan het zoeken op verschillende locaties.

**QGIS**: Dank u voor uw tijd en het werk dat u doet voor het promoten en documenteren van werkstromen in QGIS!

![](../images/ft_potrait_steve_bernard.jpg)

*Portret van Steve Bernard. Interactive Design Editor bij de Financial Times.*

**Steven**: Graag gedaan, ik ben bijna evangelisch over QGIS! Daarom ook de [31 videohandleidingen](https://t.co/6aTE6G8h0T) en altijd bereid erover te vertellen.

Interviewvragen door A. Neumann en T. Sutton. April 2016.

{{<content-end >}}
