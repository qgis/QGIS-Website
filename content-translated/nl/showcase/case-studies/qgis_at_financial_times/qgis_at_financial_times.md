---
draft: 'true'

---
# Gebruiken van QGIS door het Financial Times Graphics Team
## Interview met Steven Bernard (Interactive Design Editor)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Steven, wat is de naam van het team waarmee u werkt bij FT? Kunt u ons wat achtergrondinformatie geven over wat uw team bij FT doet?

**Steven**: Ons team bevindt zich op dit moment in een transitieperiode, we hebben een nieuwe visualisatie-editor voor gegevens, Alan Smith OBE (eerder van de ONS) die de dingen enigszins opschud en één enkel team voor de graphics samenstelt. Traditioneel hadden we een team voor webgraphics en een team voor afdrukgraphics. Het team voor afdruk zou verantwoordelijk zijn voor alle graphics voor kranten als ook voor het maken van web-vriendelijke versies daravan. Mijn team was verantwoordelijk voor alle inhoud die allene op het web te zien was, als ook voor de nauwe samenwerking met de interactieve producers/ontwikkelaars bij het ontwerpen van interactieve graphics.

Het nieuw gevormde team zal een kruisbestuiving  van vaardigheden tussen de verschillende media mogelijk maken.

Alan heeft één enkele digitale werkstroom voor ons team geïntroduceerd, inclusief het gebruiken van d3 om een grotere woordenschat voor afbeelding te maken en het terugdringen van de benodigde tijd om visualisaties te maken.

![](./images/ft_europe_migration_balkan-route.png){.align-left width="100.0%"}

*Voorbeeld: Stroom van migranten. Route over de westelijke Balkan.*

**QGIS**: Hoeveel mensen werken er in uw team?

**Steven**: Inclusief all ontwerpers, ontwikkelaars, producers en statistici, hebben we een team van 24

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](./images/ft_nigeria-migration_animation.gif){.align-left width="100.0%"}

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](./images/ft_gotthard-tunnel.png){.align-left width="60.0%"}

*Voorbeeld: Gotthard spoor- en wegtunnel in de Zwitserse Alpen.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Hoe ontdekte u QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](./images/ft_blm-federal-land-map.png){.align-left width="100.0%"}

*Voorbeeld: Openbaar toegankelijk land in the VS.*

**QGIS**: Welke andere programma's gebruikt u naast QGIS en hoe combineert u deze?

**Steven**: Als het een rechttoe rechtaan kaart is wordt 95% van het werk gedaan in QGIS, waarna het wordt afgewerkt in Adobe Illustrator.

Als ik werk aan een kaart met reliëf, dan is het proces veel complexer. Ik haal DEM-bestanden op van Nasa Earth Explorer, en plaats die binnen QGIS om ze op grootte te maken. Ik doe de verkleinde DEM dan in Blender om een #D rendering te maken. Als ik een satellietoverlay gebruk voor de schaduw op de heuvels, dan download ik een afbeelding van BlueMarble vanaf Nasa en plaats die ook in Blender. De geëxporteerde rendering uit Blender wordt dan teruggeplaatst in QGIS om te dienen als achtergrondlaag. Ik pas soms, indien nodig, eerst nog wat aan in Photoshop.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Een ander programma dat nuttig is is Google My Maps wat het voor journalisten over d egehele wereld mogelijk maakt locaties op een kaart te markeren die we dan kunnen downloaden als een KMZ-bestand en die we rechtsreeks kunnen importeren in QGIS.

Het laatste programma dat ik gebruik is is Adobe After Effects omdat ik recent ben begonnen met het animeren van mijnkaarten om de gebruiker mee te nemen op reis. Zoals recent gebruikt in de serie Land Rush:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Gebruikt u andere ruimtelijke programma's of GIS naast QGIS, en zo ja, welke?

**Steven**: Voor mij alleen QGIS, maar zoals eerder gezegd gebruiken sommige van mijn collega's ook Map Publisher.

![](./images/ft_isis-air-strikes_febupdate.png){.align-left width="100.0%"}

*Voorbeeld: Aanvallen op Syrië in februari 2016.*

**QGIS**: Kunt u de sterke en zwakte punten van QGIS beschrijven met betrekking tot de taken die u moet uitvoeren?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

Binnen twee weken was ik er van overtuigd dat het dat ook zou kunnen. Het belangrijkste argument was de mogelijkheid tot het instellen van stijlen voor alles inclusief stijlen voor op zoomniveau voor kaarten op straatniveau.

Ik heb een systeem ingesteld waar we sets van bladen van Google hebben met kolommen voor naam, lat, long, pictogram voor markering, dikte voor lettertype, grootte voor lettertype en of de markering moet worden weergegeven of niet.

Het pictogram voor de markering is een keuzelijst die is gekoppeld aan een tabel met vLookUp die alle details voor die markering invult.

Alles wat is hoef te doen is de CSV te downloaden, die importeren in QGIS, een stijl toe te passen en ik heb een kaart die al voor 95% klaar is.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](./images/ft_chinaMigration.png){.align-left width="100.0%"}

*Voorbeeld: Stedelijke aantrekkingskracht en migratie in China.*

**QGIS**: Wat zijn de concepten of mogelijkheden waarvan u het meest houdt  in QGIS?

**Steven**: er zijn talrijke mogelijkheden die ik zou willen klassificeren als levensredders! Maar primair hebben Quick OSM en Georeferencer mij zo vaak gered, die zijn absoluut essentieel als deadlines nabij zijn. Wat, bij het werken voor een nieuwsorganisatie, bijna 90% van de tijd is.

![](./images/ft_china_henanGuangdong.png){.align-left width="100.0%"}

*Voorbeeld: Stedelijke aantrekkingskracht en migratie in China. Gedetailleerde weergaven*

**QGIS**: Welke mogelijkkheid of functionaliteit mist u het meest in QGIS? Heeft u een lijst met ontbrekende mogelijkheden die u zouden helpen als zij werden geïmplementeerd?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

De mogelijkheid om afbeelding in grotere grootten op te slaan. Momenteel is de enige manier waarop ik een verkleining met geo-verwijzingen van een DEM-bestand kan maken is om het in Blender te doen. maar het is beperkt tot de grootte van je scherm. Als ik een 8000 pixel DEM-bestand inQGIS kon laden zou ik in staat zijn de verkleining te exporteren in ene grotere grootte dan mijn scherm om bijvoorbeeld in een HD-video te gebruiken.

**QGIS**: Als u bepaalde mogelijkheden ontbeert in QGIS, zie u zouden kunnen helpen - zou u overwegen om QGIS zelf te verbetern (met coderen in de bron van QGIS of met plug-ins van Python), of zou u overwegen om een ontwikelaar van QGIS in te huren om de ontbrekende mogelijkheid voor u te implementeren? Of zou u in plaats daarvan zoeken naar andere programma's om dat gat te vullen?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](./images/ft_us_broadband_internet_subscription.png){.align-left width="100.0%"}

*Voorbeeld: Percentage van huishoudens met een breedband internetabonnement in de VS.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Dank u voor uw tijd en het werk dat u doet voor het promoten en documenteren van werkstromen in QGIS!

![](./images/ft_potrait_steve_bernard.jpg){.align-left width="50.0%"}

*Portret van Steve Bernard. Interactive Design Editor bij de Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Interviewvragen door A. Neumann en T. Sutton. April 2016.
