---
HasBanner: false
draft: false
releaseDate: 22-02-2019
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.6
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.6{#changelog36 }
![image1](images/projects/f335c2ee37b714ad6eec143246d947f09a5ff2f1.png)

Datum uitgave 22-02-2019

De grootste uitgave van QGIS ooit! QGIS 3.6 brengt een enorme lijst met nieuwe wijzigingen - de hoogtepunten daarvan zullen we hier proberen te behandelen. Zoals altijd herinneren we u er aan dat QGIS een open bron project is en vragen u om als het mogelijk is ons werk te ondersteunen door donaties, sponsoring of bijdragen aan de documentatie van de code, website, enzovoort.

Dank u wel

We willen onze dank uitspreken aan alle ontwikkelaars schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de QGIS gemeenschap hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op qgis.org en help een handje!

QGIS wordt ondersteund door donoren en sponsors. Een actuele lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze lijst met donoren. Als u een officiële sponsor voor het project zou willen worden, bekijk dan onze pagina om te sponsoren voor details. Het sponsoren van QGIS helpt ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van bugs te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeende dank u voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Kaartgereedschap
### Mogelijkheid: Titellabel-decoratie
Een nieuwe decoratie werd toegevoegd om gebruikers toe te laten snel een titel weer te geven op hun kaartvenster. De decoratie heeft een achtergrondbalk met een instelbare kleur en transparantie.

![image2](images/entries/400e617d8059eddcd1228f3ce6861d6087f65794.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Boven/onder centreren voor decoratie items
Kaartvenster copyright en de nieuw toegevoegde titellabel-decoratie kunnen nu gecentreerd worden boven- of onderaan de kaartweergave.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Gereedschap Punten reparaties en verbeteringen
Opmerking: alle hieronder vermelde items zijn ook aan de LTR toegevoegd, zodat ze ook in QGIS 3.4.5 zullen verschijnen.
### Select (\"lock\") feature before editing
In QGIS 2.18 you always had to select a feature first before editing it. In QGIS 3 there was no such thing - editing would be done on any feature any time. Now we are making the selection of feature (\"lock\") available again - using **right click**.

In eerdere versies van QGIS3, gaf rechts klikken een klein popup menu weer dat de weergave van van de punten bewerker aanbood.  **Nu wordt bij rechts klikken onmiddellijk de punten bewerker weergegeven en het bewerken van andere objecten uitgeschakeld.**

When a feature is \"locked\", it can be again unlocked by clicking on it or by clicking on an empty area - this will bring us back to the default mode when multiple features can be edited.

**Wanneer er meerdere objecten op één muislocatie staan zal herhaald met rechts klikken door die objecten gaan** - met elke rechtsklik zult u een ander object zien. Tenslotte, als alle objecten zijn aangeboden, zal geen object worden vergendeld en zal een volgende klik met rechts de doorloop opnieuw starten.

The locking is possible when clicking a feature\'s vertex, edge or interior (for polygons).
### Nieuw punt toevoegen zonder het te verplaatsen
Het is nu mogelijk om **Shift + dubbelklik te gebruiken om een nieuw punt toe te voegen zonder het op een nieuwe locatie te plaatsen**. Soms is dit handig als gebruikers een extra punten willen plaatsen op de bestaande segmenten.
### \"Current layer\" mode is now the default
From the two modes of vertex tool, \"all layers\" used to be the default one. But from the user feedback that seemed like less common case and users prefer to have \"current layer\" as the default.

This feature was funded by [German QGIS user group](http://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Verkleind/Vergroot
Anders dan in andere software stelt het gereedschap u in staat (multi)lijnen EN (multi)polygonen aan te passen. Meer nog, het is niet noodzakelijkerwijze het einde van de lijnen dat is betrokken; elk segment van een geometrie kan worden aangepast. De andere kant is dat dit kan leiden tot ongeldige geometrieën, het is de verantwoordelijkheid van de gebruiker.

Het gereedschap vraagt u een grens te kiezen (een segment) waarop een ander segment zal worden vergroot of verkleind. Anders dan het gereedschap Knoop wordt een controle uitgevoerd om alleen de laag aan te passen die wordt bewerkt.

Als beide segmenten 3D zijn, voert het gereedschap een interpolatie uit op het grenssegment om de Z terug te geven.

In het geval van verkleinen moet u het deel selecteren dat moet worden verkort door erop te klikken.

This feature was funded by [Mairie de Megève](https://www.megeve.fr/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Mogelijkheid: Rechthoek uit 3 punten (geprojecteerd)
Er is al een methode om een rechthoek uit 3 punten te maken waarbij de rechthoek een lengte krijgt van tussen het eerste en tweede punt en de tweede lengte gelijk is aan de afstand tussen het 3e en 2e punt.

Deze nieuwe methode maakt het mogelijk een rechthoek te maken uit 3 punten waarbij de tweede lengte de afstand is tussen het punt en het loodrecht geprojecteerde punt op het segment (of de uitbreiding daarvan).

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Mogelijkheid: Gereedschap Identificeren voor lagen met mazen
Het gereedschap identificarenwerkt nu op de laag met mazen. Het geeft de huidige waarde weer van scalaire en vectorcomponenten van de mazen.

![image3](images/entries/62a172172d717af1b5399af4006db1ee0e82c7f5.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Expressies
### Mogelijkheid: Nieuwe functies voor expressies
- `force_rhr`: forces polygons to follow the right hand rule, in which the area that is bounded by a polygon is to the right of the boundary. In particular, the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.
- `decode_uri`: takes a layer parameter and an optional uri part parameter. It will return details about the data source of the layer. The available details depend on the data provider. If called with only a layer parameter, a map will be returned with all the available information. If the part is also specified, only the value for the requested part will be extracted from the map.
- `path` has been added as an option for the `layer_property` expression function
- `array_sort`: sorts an array of elements
- `nullif`
- sqlite_fetch_and_increment
- `make_rectangle_3points`: Make a rectangle from 3 points. There is two options for make the rectangle by the distance or a projection. Option distance: Second distance is equal to the distance between 2nd and 3rd point. Option projected: Second distance is equal to the distance of the perpendicular projection of the 3rd point on the segment or its extension.
- `make_square`: Creates a square from a diagonal.
- from_json
- to_json

### Mogelijkheid: Vierkante haken om eenvoudig toegang te krijgen tot array-elementen van de kaart
Maakt expressies mogelijkzoals:
- array(1,2,3)\[0\] -\> 1
- array(1,2,3)\[2\] -\> 3
- array(1,2,3)\[-1\] -\> 3 (Python style, negative indices count from end of array)
- array(1,2,3)\[-3\] -\> 1
- map(\'a\',1,\'b\',2)\[\'a\'\] -\> 1
- map(\'a\',1,\'b\',2)\[\'b\'\] -\> 2

Deze mogelijkheid werd ontwikkeld door Nyall Dawson, Mathieu Pellerin
### Mogelijkheid: Nieuwe variabelen voor expressies voor kaart
- \@map_crs_description: name of the coordinate reference system of the map.
- \@map_crs_acronym: acronym of the coordinate reference system of the map.
- \@map_ellipsoid_acr: acronym of the ellipsoid of the coordinate reference system of the map.
- \@map_crs_proj4: Proj4 definition of the coordinate reference system.
- \@map_crs_wkt: WKT definition of the coordinate reference system.

Deze mogelijkheid werd ontwikkeld door  Alexis Roy-Lizotte
### Mogelijkheid: Nieuwe funtie try() om fouten te vangen
De nieuwe functie try() probeert een expressie en geeft de waarde ervan terug indien foutenvrij. Als de expressie een fout teruggeeft zal een alternatieve waarde worden teruggegeven, indien opgegeven, anders zal de functie null teruggeven.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
## Gebruikersinterface
### Feature: A new grayscale theme: \"Blend of Gray\"
A brand new UI theme has made its way into QGIS named \"Blend of Gray\". In addition, hundreds of fixes, tweaks, and refinements were applied to the preexisting \"Night Mapping\" theme.

![image4](images/entries/32e743ea5bf84c96b86ea31160b1677b6362eacf.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Meerregelige selecties en bewerken in bewerkers voor code/expressies
Indrukken van Ctrl tijdens het selecteren in de bewerkers voor expressies en Python-scripts in QGIS stelt u in staat een meerregelig blok tekst te selecteren, die in één keer kan worden bewerkt.

This feature was developed by [Nyall Dawson ()](https://north-road.com)
## Symbologie
### Mogelijkheid: Verbeterde afhandeling van stijlbibliotheken voor .XML
Het paneel Browser geeft nu stijlbibliotheken voor XML in QGIS weer en deze bestanden kunnen ook worden versleept en worden neergezet in een venster van QGIS. Dit opent een dialoogvenster dat gebruikers in staat stelt de stijlbibliotheek te verkennen en stijlen uit de bibliotheek te importeren naar hun installatie van QGIS.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Optioneel forceren van de Rechterhand-regel gedurende het renderen van symbolen voor polygonen
This new option, available under the \"Advanced\" button for fill symbols, allows forcing rendered polygons to follow the standard \"right hand rule\" for ring orientation (where exterior ring is clockwise, and interior rings are all counter-clockwise).

De reparatie voor de richting wordt alleen toegepast tijdens het renderen, en de originele geometrie van het object wordt niet gewijzigd.

Dit maakt het maken van gevulde symbolen met een consistent uiterlijk mogelijk, ongeacht de gegevensset die wordt gebruikt bij het renderen en de richting van de ringen van individuele objecten.

Deze mogelijkheid werd mogelijk gemaakt door de Duitse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Optie voor eenvoudige lijnen en markeringslijnen om alleen de buitenste ring of binnenste ringen te renderen
This new option is shown whenever a simple line symbol or marker line symbol is used as part of a fill symbol for rendering polygons. The default behavior is to render both interior and exterior rings, but this new setting allows users to set the symbol layer to render only for the exterior ring OR only for interior rings. This allows for symbolisation which wasn\'t directly possible before, such as a marker line with markers for interior rings angled toward the interior of the polygon.

Deze mogelijkheid werd mogelijk gemaakt door de Duitse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Rasterafbeelding als puntsymbool
Een nieuw type symbologie voor punten als rasterafbeeldingen werd toegevoegd aan QGIS die gebruikers in staat stelt een raster, d.i. bitmap, afbeeldingsbestand te gebruiken en weer te geven als een puntsymbool. De symbologie voor punten als rasterafbeelding staat aanpassen van de breedte, hoogte, verhoudingen van de afbeelding, rotatie, en transparantie toe.

Gebruik maken van een gegevens-gedefinieerde afbeeldingsbron maakt deze nieuwe symbologie een fantastische methode om afbeeldingen met geoverwijzingen weer te geven op een kaartvenster.

![image5](images/entries/511ac83d3b841be6ae81db5f5d0f319e07e9656e.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Vulling voor raster mag afbeeldingen hebben ingesteld naar URL's op afstand of ingebedde afbeeldingen
Net zoals de SVG en markering voor rasterafbeeldingen, kan de vulling voor rasters nu worden ingesteld om URL's naar HTTP(s) te gebruiken of bestanden direct hebben ingebed binnen het symbool zelf.

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
### Mogelijkheid: Weergavewaarden gebruiken voor geklassificeerde renderers
When a field is configured with a value relation, value map or other \"representable value\" and the field is used as the source for a classification renderer, the represented values will be taken to label the categories.

Deze mogelijkheid werd ontwikkeld door Matthias Kuhn
### Mogelijkheid: Optie om categorieën samen te voegen in renderer Categorieën
Deze wijziging stelt gebruikers in staat om meerdere bestaande categorieën te selecteren en die te groeperen naar één enkele categorie, die wordt toegepast op elke waarde in de selectie.

Dit maakt het mogelijk lagen met een groot aantal categorieën eenvoudiger op te maken, waarbij het mogelijk is meerdere afzonderlijke categorieën naar een kleinere, meer beheersbaarder set van categorieën te groeperen, die van toepassing is op meerdere waarden.

De optie is beschikbaar in het contextmenu, klik met rechts, in de lijstweergave van de categorieën, wanneer meerdere categorieën zijn geselecteerd.

![image6](images/entries/159eb5270ab436adbbddba1c92799d8621a0b8e5.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Projectkleuren weergeven in kleurgebonden data-gedefinieerde knoppen
This adds a new \"Project Colors\" section in data defined buttons which are linked to a color value. The color menu contains all colors defined as part of the current project\'s Project Color Scheme (which is defined through project properties).

Wanneer een projectkleur wordt gekozen uit de knop, wordt de eigenschap gekoppeld aan die kleur. Het zal automatisch elke toekomstige wijziging aan de kleur volgen die worden gemaakt via de Projecteigenschappen.

This allows users to define common colors for a project once, and then \"bind\" symbol, label, layout, etc colors to these preset colors. The link is live, so you change it once, and the change is reflected EVERYWHERE. Sure beats updating a color 100 times when it\'s use has been scattered throughout a project\'s symbols, labels, etc\...

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan dialoogvenster stijlbeheer
Het dialoogvenster Stijl manager heeft een aantal verbeteringen ondergaan:
- A new \"list view\" mode has been added
- An \"all\" tab has been added, which shows all matching symbols (regardless of the symbol type)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: SLD exporteren voor rasterstijlen
QGIS is now able to export raster styling to sld, for example to be used in Geoserver. See: <https://docs.geoserver.org/latest/en/user/styling/qgis/index.html#exporting-raster-symbology>

![image7](images/entries/7ab383dfaa0a0dbc9651168a56f44e2275b8c2df.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door OSGeo UK, GeoServer PSC, Brad Hards

This feature was developed by [Luigi Pirelli and GeoSolutions](https://www.geo-solutions.it/)
## Digitaliseren
### Mogelijkheid: Verbeteringen aan Georeferencer
- dX, dY en residu toegevoegd aan GCP-punten
- optie toegevoegd om automatisch GCP-punten op te slaan in het raster-aangepaste pad

![image8](images/entries/2d6278e2e65be30ceb12ff30f26d34dae6196e42.png.400x300_q85_crop.webp)

This feature was developed by [Faneva Andriamiadantsoa](https://github.com/Fanevanjanahary)
### Mogelijkheid: Nieuwe optie om minimaliseren van Georeferencer bij het toevoegen van punten te voorkomen
Gebruikers kunnen er nu voor kiezen om het automatisch minimaliseren van het venster van georeferencer, dat voorkomt bij het toevoegen van nieuw grondcontrolepunten aan het kaartvenster, te voorkomen. Dit gedrag kan irritant zijn op setups met meerdere schermen, waar het wenselijk kan zijn om beide vensters zichtbaar te hebben bij het toevoegen van punten.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Gegevensbeheer
### Mogelijkheid: Optie Opmerking in DB Manager
This feature was developed by [Corentin Falcone (SIRS)](https://www.sirs-fr.com/sirs/fr/)
## Formulieren en widgets
### Mogelijkheid: Nieuw formulierwidget voor binaire (blob)-velden
Deze widget is alleen beschikbaar voor binaire velden (en wordt als standaard widget gebruikt voor binaire velden).  Het biedt een label om aan te geven of het blob veld leeg is of niet. Als het niet leeg is, geeft het de inhoudsgrootte weer (in bytes/kb/enz.).

Een knop met keuzemenu laat gebruikers toe om de huidige binaire inhoud van het veld op te slaan naar een schijf gebaseerd bestand, de inhoud van een blob veld leeg te maken, of binaire inhoud te inbedden door een bestand te selecteren van hun systeem.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Printvormgeving
### Mogelijkheid: Grid frame verbeteringen
Users can now set a margin for the grid frames in layout map items. Additionally, new \"Zebra (Nautical)\" and \"Line border (Nautical)\" frame styles have been added, which show nautical-style blocks in the grid corners when a margin is set for the grid.

Deze mogelijkheid werd ontwikkeld door konst
### Mogelijkheid: Verbeterde behandeling van exporteren van tekst en labels
Bij het exporteren van een afdruklay-out naar PDF- of SVG- indelingen hebben gebruikers nu de keuze over hoe tekst en labels binnen die lay-out zouden moeten wordne geëxporteerd. Beschikbare opties worden geconverteerd naar allemaal tekst voor omtrekken/bogen (de eerdere standaard), of om tekst en labels als tekstobjecten te behouden.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen voor kaartlabels
Verscheidene verbeteringen zijn gemaakt met betrekking tot hoe labels worden gerenderd in kaartitems van lay-out.
- A new setting allows per-map control of how close labels are permitted to be placed to the map item\'s edges. Sizes can be set using mm/inches/pixels/etc, and data defined label margins are allowed.
- Een nieuwe instelling maakt beheer per kaart mogelijk of gedeeltelijke labels zichtbaar zijn op de kaart. Dit staat standaard uit, (anders dan de instelling voor het kaartvenster die standaard aan staat voor een nieuw project) omdat lay-outs altijd standaard de instellingen zouden moeten gebruiken die de hoogste kwaliteit cartografische uitvoer produceren.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Sneltoetsen voor bereik/schaal van kaartitems opnieuw bewerkt
De knoppen voor het instellen van kaartitems voor lay-out om overene te komen met de huidige kaartweergave (en vice versa) zijn naar boven verplaatst naar een nieuwe werkbalk in het venster voor eigenschappen van kaartitems.

New actions have also been added to set the map item\'s scale to match the main canvas scale, and to set the main canvas scale to match the selected layout map\'s scale. These mirror the existing settings for setting the extent from the canvas and pushing the extent TO the canvas.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Layout items can \"block\" map labels
This feature allows other layout items (such as scalebars, north arrows, inset maps, etc) to be marked as \"blockers\" for the map labels in a map item. This prevents any map labels from being placed under those items - causing the labeling engine to either try alternative placement for these labels (or discarding them altogether).

This allows for more cartographically pleasing maps \-- placing labels under other items can make them hard to read, yet without this new setting it\'s non-trivial to get QGIS to avoid placing the labels in these obscured areas.

The blocking items are set through a map item\'s properties, under the label settings panel. The setting is per-map item, so you can have a scalebar block the labels for one map in your layout and not others (if you so desire!)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Waarschuwingen voor exporteren
Bij het exporteren van afdruklay-outs controleert QGIS nu automatisch de lay-out op veel voorkomende fouten en waarschuwt de gebruiker als die worden gevonden:
- Schaalbalken niet gekoppeld aan een kaartitem
- Items voor afbeeldingen met verbroken of ontbrekende paden, of gekoppeld aan onleesbare afbeeldingsbestanden
- Overzichtskaarten niet langer gekoppeld aan een geldig kaartitem

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Beheer over stapelpositie van bereiken van overzichtskaarten
QGIS allows overview extents to be drawn below map labels (the new default), but in 3.6 choices have been added for drawing them below all map layers, or above/below a specific map layer. This allows users to control exactly where in the map item\'s layer stack the overview will be placed, e.g. allowing them to draw a overview extent below some feature layers such as roads whilst drawing it above other background layers.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe variabelen voor expressies voor items van de legenda
Nieuwe variabelen voor expressies zijn toegevoegd om te gebruiken in data-gedefinieerde expressies in items van de legenda van een lay-out, inclusief:
- \@legend_title
- \@legend_column_count
- \@legend_split_layers
- \@legend_wrap_string
- \@legend_filter_by_map
- \@legend_filter_out_atlas

If the legend is linked to a map, then expressions used in that legend will also have access to the linked variables, including \@map_scale, \@map_extent, etc.

Aanvullend gebruiken symbolen, gerenderd als deel van een legenda, de volledig beschikbare context van de expressie voor de legenda. Dit betekent dat de symbolen toegang hebben tot variabelen, zoals het huidige object Atlas.

Deze mogelijkheid werd ontwikkeld door  Alexis Roy-Lizotte
### Mogelijkheid: Expressies binnen tekst van een item voor legenda
This feature allows for expressions to be embedded directly inside legend item text (e.g. group, subgroup and item text). The expressions are evaluated at render time, with full knowledge of the legend\'s expression context (so can utilise variables from the layout/layout item/etc)

There\'s no UI for this yet (that will come in 3.8), but expressions are entered using the standard \[% 1 + 2 %\] format.

Bijvoorbeeld een item voor de legenda als

    My layer (rendered at 1:[% @map_scale %])
    
zal in de uitvoer worden weergegeven als

    My layer (rendered at 1:1000)
    
Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Analyse-gereedschappen
### Mogelijkheid: Hardware-acceleratie voor rasterberekeningen
Acceleratie van OpenCL is nu standaard beschikbaar voor bewerkingen van rasterberekeningen

Deze mogelijkheid werd mogelijk gemaakt door Alessandro Pasotti - ItOpen

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Mazen berekenen
Soortgelijk aan rasterberekeningen werkt Mazen berekenen op lagen met mazen. In aanvulling op de algemene functies verschaft Mazen berekenen ook functies voor het optellen van tijden. Als u bijvoorbeeld een netcdf hebt met dagelijkse temperaturen over een maand, kunt u de gemiddelde temperatuur over de gehele maand berekenen voor elke cel. De uitvoer kan worden gefilterd op tijdsduur of ruimtelijk bereik.

Dit werd mogelijk gemaakt door Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Processing
### Feature: New algorithm \"Remove duplicates by attribute\"
Maakt het verwijderen van gedupliceerde objecten mogelijk, geïdentificeerd met behulp van de waarden in één (of meer) veldwaarden van de invoerobjecten. Optioneel kunnen genegeerde (duplicaat)-objecten worden opgeslagen in een afzonderlijke afvoer.

![image9](images/entries/ae0544826b7d16479b2e48ba97f1f530c80bbd42.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Explode HStore
This algorithm creates a copy of an input layer and adds a new field for every unique key found in a HStore type field. For instance, a HStore field is often present in an OSM dataset (\"other_tags\").

![image10](images/entries/304c29f7cc6d26aa823001b67a46744deec3c2dd.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Etienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: Rechterhand-regel forceren 
Dit nieuwe algoritme forceert geometrieën polygoon om de Rechterhand-regel te respecteren, waarin het gebied dat is gebonden aan een polygoon aan de rechterkant van de grens ligt. In het bijzonder de buitenste ring is georiënteerd in de richting met de klok mee en de binnenste ringen in de richting tegen de klok in.

![image11](images/entries/16db7b4b5931c9d96eba053701641defc6f52290.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door de Duitse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Binair veld uitnemen
Dit algoritme stelt gebruikers in staat de inhoud uit binaire velden te nemen en op te slaan in bestanden.

![image12](images/entries/6715290eac02e216394b3f24045da0b982069c7d.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Lijnen splitsen op maximum lengte
Dit algoritme neemt een invoer (meerdere) lijnen- (of boog-)laag en splitst elk object in meerdere delen, waarbij elk deel niet langer is dan de gespecificeerde maximale lengte.

Ondersteunt de data-gedefinieerde eigenschap voor maximum lengte, en de bewerking voor direct bewerken.

![image13](images/entries/13c8c2fedfa76ff8decbc4d7e6d683d01bab1126.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Nyall Dawson, Nathan Woodrow
### Mogelijkheid: Nieuw type parameter voor configureren van authenticatie
Een nieuw type parameter voor algoritmes van Processing, QgsProcessingParameterAuthConfig, is toegevoegd, wat het mogelijk maakt een selectie te maken uit beschikbare configuraties voor authenticatie (en het maken van nieuwe).

It allows creation of processing algorithm which can fully take advantage of QGIS\' mature authentication handling, avoiding the need to use insecure string parameters for users to input sensitive logon credentials.

Parameters QgsProcessingParameterAuthConfig worden geëvalueerd met behulp van QgsProcessingAlgorithm.parameterAsString(), die de ID voor de geselecteerde configuratie voor de authenticatie teruggeeft.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Opties voor resamplen en indeling in het algoritme gdaladdo
Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Mogelijkheid: Algoritme Rastergebiedsstatistieken
This algorithm calculates statistics for a raster layer\'s values, categorized by zones defined in another raster layer.

![image14](images/entries/014272dcac2a228f8d8cc7a1587ac9b07865bc1f.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritmes Z-waarden uitnemen en M-waarden uitnemen 
Deze algoritmes stellen gebruikers in staat de in object-geometrieën aanwezige Z- en M-waarden te converteren naar attributen in de laag.

Standaard wordt de Z/M-waarde uit het eerste punt in het object uitgenomen, maar optionele statistieken kunnen wordne berekend voor ALLE Z-/M-waarden uit de geometrie (bijv. berekenen van gemiddelde/min/max/som/etc van Z-waarden).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Geodesische lijn gesplitst op antimeridiaan
Dit algoritme splitst een lijn in meerdere geodesische segmenten wanneer de lijn de antimeridiaan (±180 graden longitude) kruist. Splitsen op de antimeridiaan helpt de visuele weergave van de lijnen in sommige projecties. De teruggegeven geometrie zal altijd een meerdelige geometrie zijn.

Wanneer lijnsegmenten in de invoergeometrie de antimeridiaan kruisen, zullen zij worden gesplitst in twee segmenten, waarbij de latitude van het breekpunt wordt bepaald met behulp van een geodesische lijn die de punten aan beide zijden van dit segment verbindt. De huidige instelling voor de ellipsoïde van het project zal bij het berekenen van het breekpunt worden gebruikt.

Als de invoergeometrie M- of Z-waarden bevat zullen die lineair worden geïnterpoleerd voor de nieuwe punten die worden gemaakt op de antimeridiaan.

Modus Direct bewerken wordt ook ondersteund.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Geodesic mode for \"Join by Lines (Hub lines)\" algorithm
Dit maakt het mogelijk optioneel geodesische lijnen te maken, die de kortste afstand tussen de punten weergeven, gebaseerd op de ellipsoïde.

Wanneer de modus Geodesisch wortd gebruikt is het mogelijk de gemaakte lijnen te splitsen op de antimeridiaan (±180 graden longitude), wat het renderen van de lijnen kan verbeteren. Aanvullend kan de afstand tussen de punten worden gespecificeerd. Een kleinere afstand resulteert in een dichtere, meer nauwkeuriger lijn.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Rasteroppervlak volume
Het SAGA rasteroppervlak volume is geporteerd naar een eigen alforitme van QGIS. De versie van SAGA van dit algoritme is van beperkt gebruik in QGIS, omdat het berekende volume alleen is ingebed in de uitvoer voor de terminal in SAGA. Dit voorkomt dat het wordt opgeslagen naar een bestand, of opnieuw gebruikt in een model als een invoer voor een latere stap in het model. Dientengevolge is het algoritme geporteerd naar een eigen QGIS C++-algoritme. Het algoritme dupliceert het algoritme voor SAGA 1:1, maar voert het volume (en gebied) uit naar ofwel een rapport in HTML, of een vectortabel. Aanvullend wordt de uitvoer geëxporteerd als numerieke uitvoer vanuit het algoritme, wat het mogelijk maakt ze opnieuw te gebruiken in modellen.

![image15](images/entries/e0a8089ec0653cf5628636354ec80ef317e68565.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Herrezen functionaliteit model naar Python-script
De 2.x mogelijkheid voor het direct converteren van een model van Processing naar een equivalent script voor Python is nieuw leven ingeblazen en bijgewerkt voor de 3.x API van Processing.

![image16](images/entries/42b342e04b54d5e106ba1051b210d83af8712dd8.png.400x300_q85_crop.webp)

This feature was funded by [Solspec](http://solspec.io)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Opties voor toepassing en projecten
### Mogelijkheid: Verwijderen van instellingen van de tab Geavanceerd in Opties
This change adds a new right click menu to the settings shown in the \"Advanced\" tab in the settings dialog, which allows users to remove that setting (or group of settings).

![image17](images/entries/6b012542ef9ca282ba6f9087758f85d818dd5ec9.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Browser
### Feature: Add \"export to file\" options for raster and vector layers within the browser
Maakt het mogelijk deze bestanden direct te exporteren (bijv. naar een andere indeling, CRS, etc) zonder de noodzaak ze feitelijk eerst in het project te laden.

![image18](images/entries/d939594c84d7aa186fe5f18f46ed7ad0c89d8c67.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Nyall Dawson (North Road)](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Eigen eigenschappen bestand/map
You can now right click on a file or folder within the browser, and select \"File Properties\" or \"Directory Properties\" to open the native file/folder properties dialog for that entry. This allows rapid access to operating system file or folder properties, such as file permissions and sharing options.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Voorbeeld lagen en attributen
QGIS 3.6 brings back the functionality from the old 2.18 standalone \"browser\" application to preview layers and their attributes. This functionality has been moved to the inbuilt browser panel, and is available by right-clicking on a layer and selecting \"properties\" (or by clicking the \"enable properties widget\" button in the browser toolbar).

![image19](images/entries/5058aa9a701e417271b0cbf0869669177a7f0fe4.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: QGS/QGZ projectbestanden verkennen in de browser
Eerdere versies van QGIS gaven QGS/QGZ projectbestanden weer in de browser, waar ze konden worden geopend als nieuw actief project.  In QGIS 3.6 werd deze functionaliteit uitgebreid en projectbestanden kunnen nu rechtstreeks verkend worden IN de browser zelf.  Projecten zijn nu uitklapbare items en door ze uit te klappen wordt de volledige projectstructuur van groepen en lagen weergegeven.  Elke laag kan dan gesleept en neergezet worden in het huidige project.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Het rechtstreeks aanmaken van Geopackage- en Shapebestanden.
Right clicking a directory in the browser panel now shows a \"New\" menu, containing items for creating a new Geopackage, Shapefile, or subdirectory under the selected directory.

![image20](images/entries/2bc8475b95a8413285b3c88a9a070f02f43cf5b9.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Terminal openen in pad
Een nieuwe contextmenu optie werd toegevoegd voor map items in het browser paneel om een nieuw terminal venster te openen in die map.

In Windows erft deze nieuwe terminal de omgeving van QGIS over, waardoor GDAL commando's en Python scripts die PyQGIS gebruiken, werken zonder dat er nog instellingen van de omgeving aangepast moeten worden.

Terminal hackers verheug u!

![image21](images/entries/623ef55ae3918f72faa7ec796bbac01bf5063464.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Algemeen
### Feature: Improved \"missing layer\" handling on project load
![image22](images/entries/8e3fbce280478d8e88cab7e24b489b783c83fc13.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it)
### Mogelijkheid: Optionele instelling voor het uitschakelen van controle op updates
A new setting, \"allowVersionCheck\" has been added to the QGIS configuration ini file. If set to true (the default), users may control whether the version check is enabled or disabled through the QGIS settings dialog. When this setting is set to false, no version checking will be performed AND users will NOT have an option to enable this check in the settings dialog.

Deze instelling is bedoeld voor gebruik in bedrijfsinstallaties waar QGIS versiebeheer centraal geregeld wordt.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Een aan/uit actie werd toegevoegd aan vectorlaag legende items
![image23](images/entries/f3b822b5591367b7d246fbdd5173763a1633b9ec.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
## Gegevensproviders
### Mogelijkheid: Open service info voor ArcGIS Feature Server-lagen
ArcGIS Feature Server-lagen hebben een nieuw rechtsklik-menu optie in het browser paneel, dat gebruikers toelaat om de service informatie webpagina voor de geselecteerde laag rechtstreeks te openen.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Binaire blob ondersteuning voor OGR provider
In plaats van binaire velden om te zetten naar afgekorte strings, zijn deze nu op te halen als hun originele binaire inhoud.  Dit laat toe dat plugins en scripts binaire velden gebruiken, zoals hun inhoud er uit halen.

Aanvullend kunnen nieuwe binaire velden aangemaakt worden voor compatibele gegevensbronnen.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor markering afbeelding en vullen afbeelding voor ArcGIS Feature Server
Bij het laden van een laag van Feature Server met markeringen voor afbeeldingen of symbologie voor het vullen van afbeeldingen zal QGIS automatiscg de ESRI markeringen voor afbeeldingen en de symbolen voor vullen converteren en ze gebruiken als de standaard stijl voor de laag.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door Nyall Dawson, Mathieu Pellerin
### Mogelijkheid: Ondersteuning voor labelen van ArcGIS Feature Server
Wanneer een laag van Feature Server labelen heeft gedefinieerd door de server, zullen de instellingen van dat labelen automatisch standaard worden gebruikt bij het laden van de laag in QGIS.

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
### Mogelijkheid: Ondersteuning voor geheugenlagen met Booleaanse en binaire velden
Memory (\"Temporary scratch\") layers can now use binary and boolean (true/false) field types.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor JSON voor GeoPackage
Ondersteuning voor JSON maakt het mogelijk gestructureerde gegevens op te slaan binnen één enkel veld in bestanden van GeoPackage.

gegevens die zijn opgeslagen als JSON kunnen wordne weergegeven en bewerkt in
- Widgets ValueRelation die meervoudige selectie toestaan geactiveerd
- Widgets KeyValue 
- Lijstwidgets
- or the [QML widget which also supports visualizing JSON data](https://www.opengis.ch/2018/11/13/visualize-postgres-json-data-in-qml-widgets/)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door David Signer (OPENGIS.ch)
### Mogelijkheid: provider Postgres: selectie primaire sleutel opslaan
When a view loaded from Data Source Managers\'s PostgreSQL tab you can select the key columns of the view (by default the first column is used, which can be wrong). This commit stores that selection in the settings, so that it doesn\'t have to be reselected on subsequent loads. This stored selection is also used when adding the loading from the browser.

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Ondersteuning voor unieke waarden in meervoudige velden van ArcGIS Feature Server
QGIS kan nu een laag van Feature Server met een renderinstelling voor unieke waarden voor meervoudige lagen weergeven.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
## QGIS Server
### Feature: Possibility to set ATLAS_PK in GetPrint request to print atlas sheet(s)
De nieuwe parameter GetPrint accepteert de primaire sleutel(s) waarvoor bladen van atlas zouden moeten worden afgedrukt, gescheiden door komma,

Een dergelijk verzoek zou er uitzien als:

    https://yourserver.name/path/to/qgisproject?SERVICE=WMS&REQUEST=GetPrint
    &TEMPLATE=A4&FORMAT=pdf&ATLAS_PK=1,3,7
    
One can also provide an asterisk (\*) for ATLAS_PK to request all features of an atlas. To protect the server against requesting too many features, it is possible to restrict it to a defined maximum of features that can be requested at one time (see attached screenshot).

Omdat cliënten niet zouden kunnen weten welk sjabloon een atlas heeft en welk(e) attribu(u)t(en) de primaire sleutel zijn van de bedekkingslaag, voegt deze nieuwe mogelijkheid die informatie toe aan het antwoord van GetProjectSettings van de service WMS.

![image24](images/entries/6a4648e447531099dfd8d5e113c2a79c8420df06.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door Marco Hugentobler
### Mogelijkheid: Configuratie van tegelmatrixen voor WMTS
In QGIS Server 3.4, werd de WMTS API toegevoegd waarin de tegelmatrixen werden berekend, uitgezonderd voor EPSG:3857 en EPSG:4326.

Deze wijziging voegt de mogelijkheid toe om de tegelmatrixen te selecteren die moeten worden gebruikt in het project en de hoek linksboven te configureren en het laatste niveau van de tegelmatrix. In het geval van EPSG:3857 en EPSG:4326 kan de gebruiker alleen het laatste niveau van de tegelmatrixen kiezen.

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door 3liz
### Mogelijkheid: Indeling JSON toevoegen voor WMS verzoek GetFeatureInfo
Thanks to this new feature, the FORMAT parameter of GetFeatureInfo for the WMS service may take \'application/json\' or \'application/geo+json\' values. In this case, the document returned by the server looks something like this:

    {"type": "FeatureCollection",
        "features":[
        {
           "type":"Feature",
           "id":"testlayer",
           "geometry":
           {"type": "Point", "coordinates": [913204.9128, 5606011.4565]},
           "properties":{
               "id":3,
               "name":"three",
               "utf8nameè":"three"
           }
        }]
    }
    
This feature was funded by [Veolia](https://www.veolia.com)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Plug-ins
### Mogelijkheid: DB Manager: Knoppen toegevoegd om een extern bestand van SQL te laden en op te slaan
De nieuwe knoppen stellen de gebruiker in staat de query in een extern bestand van SQL te laden en op te slaan.

![image25](images/entries/7d8fbe3054bd3d8b311d26d9343a20041f3fb809.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Programmeerbaarheid
### Mogelijkheid: Nieuwe klasse QgsExifTools
Contains utilities for retrieving the geotag from images and for setting an image\'s geotag.

Werken met geotags (vóór deze klasse!) is super-vervelend en vergt veel werk en is afhankelijk van ofwel het parsen van programma's voor de opdrachtregel of afhankelijk van niet-standaard bibliotheken voor Python die niet overal beschikbaar zijn, en vaak zeer moeilijk voor gebruikers op bepaalde platformen om te installeren en goed werkend te krijgen.

Met deze klasse hebben we stabiele methoden voor ophalen/instellen van geotags, die universeel beschikbaar zijn en veilig kunnen worden gebruikt door plug-ins en scripts.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Doorlopen over een delen van een QgsGeometry
This new PyQGIS API allows easy iteration over all the parts of a geometry, regardless of the geometry\'s type. E.g.

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
      print(part.asWkt())
    
    geometry = QgsGeometry.fromWkt( 'LineString( 0 0, 10 10 )' )
    for part in geometry.parts():
      print(part.asWkt())
    
Er zijn twee mogelijkheden voor doorlopen beschikbaar. QgsGeometry.parts() geeft een non-const doorloop, die het mogelijk maakt delen direct op hun plaats aan te passen:

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
       part.transform(ct)
    
For a const iteration, calling .const_parts() gives a const iterator, which cannot edit the parts but avoids a potentially expensive QgsGeometry detach and clone

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.const_parts():
       print(part.x())
    
Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeterde QgsLineString PyQGIS API
Enkele nette aanvullingen in de API zijn gemaakt voor de QgsLineString API:
- len(QgsCurve) geeft het aantal punten terug in een boog
- IndexErrors aangeven bij aanroepen van pointN, xAt, yAt, zAt, mAt, setXAt, setYAt, setMAt, setZAt met ongeldige indices voor punten
- Add \[\] getter for retrieving specific vertices, eg. ls\[0\] returns QgsPoint(\...)
- Add \[\] setter for setting specific (existing) vertices, e.g. ls\[1\] = QgsPoint(1,2)
- Add del support for removing vertices, e.g. del ls\[1\] removes the second vertex

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan PyQGIS Geometry Collection API 
De PyQGIS API voor het werken met verzamelingen van geometrieën is verbeterd:
- Aanroepen van removeGeometry met een ongeldige index zal nu een IndexError aangeven
- Calling collection\[0\] will return the first geometry in the collection, collection\[1\] the second, etc. And negative indices return from the end of the collection, so collection\[-1\] returns the last geometry in the collection.
- Geometries can be deleted by calling `del collection[1]` (deletes the second geometry from the collection). Also supports negative indices to count from the end of the collection.

Aanvullend kunt u nu ook gemakkelijk door de geometrieën in de verzameling lopen, wat dit type code mogelijk maakt:

    gc = QgsGeometryCollection()
    gc.fromWkt('GeometryCollection( Point(1 2), Point(11 12), LineString(33 34, 44 45))')
    for part in gc:
      print(part.asWkt())
    
Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Easier Processing algorithm creation via \@alg decorator
Maakt het volgende mogelijk om scripts voor Processing te definiëren zonder de noodzaak van het implementeren van een aangepaste klasse:

from qgis.processing import alg

| \@alg(name=\"test2\", label=\"test 2\", group=\"test\", groupid=\"test\") | \@alg.input(type=alg.STRING, name=\"IN1\", label=\"In string\") | \@alg.input(type=str, name=\"IN2\", label=\"In string 1\", optional=True) | \@alg.input(type=str, name=\"IN3\", label=\"In string 2\") | \@alg.input(type=alg.SINK, name=\"SINK\", label=\"Sink it!\") | \@alg.output(type=str, name=\"OUT\", label=\"WAT\") | \@alg.output(type=alg.MAPLAYER, name=\"OUT2\", label=\"WAT\") | \@alg.output(type=alg.VECTOR_LAYER, name=\"VECTOR_LAYER\", label=\"WAT\") | def testalg(instance, parms, context, feedback, inputs): | \"\"\" | This is a test function that does stuff | \"\"\" | feedback.pushInfo(\"We got these inputs!!\") | feedback.pushInfo(inputs\[\'IN1\'\]) | feedback.pushInfo(inputs\[\'IN2\'\]) | feedback.pushInfo(inputs\[\'IN3\'\]) | return { | \"OUT2\": \"wat\" | }

Deze mogelijkheid werd ontwikkeld door Nathan Woodrow
### Mogelijkheid: Blokkeren van (niet-async) netwerkverzoeken
Nieuwe PyQGIS API is toegevoegd voor het uitvoeren van blokkeerverzoeken van SAFE. Het is thread-veilig en heeft volledige ondersteuning voor instellingen van QGIS proxy en authenticatie.

    reply = QgsNetworkAccessManager.blockingGet(...)
    reply = QgsNetworkAccessManager.blockingPut(...)
    
Deze API zou altijd moeten worden gebruikt als een blokkeerverzoek voor een netwerk vereist is. Anders dan implementaties die vertrouwen op QApplication::processEvents() of het maken van een QEventLoop, is deze klasse compleet thread-veilig en kan zonder problemen worden gebruikt op ofwel de hoofdthread of threads op de achtergrond.

Doorverwijzingen worden automatisch afgehandeld door de klasse.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Aangepaste controles voor geldigheid voor exports van lay-out
See <https://north-road.com/2019/01/14/on-custom-layout-checks-in-qgis-3-6-and-how-they-can-do-your-work-for-you/>

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: API voor berekenen van geodetische lijnen
Nieuwe PyQGIS API voor het berekenen van geodetische lijnen (kortste afstand op een ellipsoïde) is toegevoegd aan QgsDistanceArea, wat de volwassen bibliotheek geographiclib gebruikt voor geodetische berekeningen.
- QgsDistanceArea.geodesicLine : berekent de geodetische lijn tussen twee punten
- QgsDistanceArea.latitudeGeodesicCrossesAntimeridian berekent de breedtegraad waarop de geodetische lijn twee punten verbindt die de ant-meridiaan kruisen
- QgsDistanceArea.splitGeometryAtAntimeridian : splitst een (multi)linestring op de anti-meridiaan, met behulp van geodetische lijnen om het exacte punt te berekenen om te splitsen op de anti-meridiaan

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuwe klasse QgsQuadrilateral
QgsRectangle stelt niet de ondersteuning voor oriëntatie of Z voor, omdat zijn rol is voor het bereik. Een nieuwe klasse, genaamd QgsQuadrilateral, om 4 vertexpolygonen te beheren is gemaakt. Voor dit moment zijn er alleen rechthoeken maar het is mogelijk later andere vormen toe te voegen.

Deze opnieuw uitgevoerde fabricage vereenvoudigt kaartgereedschappen en stelt u in staat de klasse QgsQuadrilateral in andere gereedschappen te gebruiken.

Aanvullend daar zal het een beter beheer van de Z voor rechthoeken door 3 punten mogelijk maken. Vandaag wordt de eerste Z gebruikt, nu zullen de punten hun Z hebben en de 4e zal op de vlakte wordne geprojecteerd.

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## 3D-objecten
### Mogelijkheid: Terreinschaduw
This adds new options for user to choose how the terrain should be rendered: - shading disabled - color of terrain is determined only from map texture - shading enabled - color of terrain is determined using Phong\'s shading model, taking into account map texture, terrain normal vector, scene light(s) and terrain material\'s ambient+specular colors and shininess

Optioneel kunnen terreinen worden voorzien van schaduw uit een voorkeuze kaartthema.

Deze mogelijkheid werd ontwikkeld door Martin Dobias (Lutra Consulting)
### Mogelijkheid: Configuratie van lichten in 3D-kaartscenes
Deze mogelijkheid voegt een gedeelte toe om punten voor lichten te definiëren in 3D-scenes. Tot maximaal 8 lichten wordt ondersteund (beperking door implementatie van materiaal). Voor elk licht kan men de positie, intensiteit, kleur en demping instellen.

Deze mogelijkheid werd ontwikkeld door Martin Dobias (Lutra Consulting)
### Mogelijkheid: Op regel gebaseerde 3D-renderer
![image26](images/entries/0825fbe986d774f7f2d5a0bdfdbc2487453ef49c.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door de gemeenschap van QGIS

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Ondersteuning voor lagen met mazen (faces) in 3D
Met deze mogelijkheid kunt u uw laag met mazen gebruiken in 3D-scenes,

![image27](images/entries/82a388b33e8fb96df43fb32b9bc5ef013be0459c.jpg.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server: WFS issue using the EXP_FILTER parameter | [#20927](https://issues.qgis.org/issues/20927) | [PR #8924](https://github.com/qgis/QGIS/pull/8924) | Gereed |
| GetFeatureInfo response empty for child relation table in QGIS Server 3 | [#20801](https://issues.qgis.org/issues/20801) | Kan niet worden gereproduceerd met 3.5 |  |
| QGIS Server WFS DescribeFeatureType not following TYPENAME parameter | [#20198](https://issues.qgis.org/issues/20198) | [PR #8948](https://github.com/qgis/QGIS/pull/8948) | Gereed |
| QGIS Server 3.4 can\'t reset numeric field using WFS Update | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Gereed |
| WFS provider shows numeric NULL fields with 0 instead of NULL | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Gereed |
| OWS project title in project properties cannot be set to blank/empty | niet gerapporteerd | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Gereed |
| Form Value relation based on WFS layer | [#21077](https://issues.qgis.org/issues/21077) | [PR #8970](https://github.com/qgis/QGIS/pull/8970) | Gereed |
| Button positions in Database styles manager dialog | [#21068](https://issues.qgis.org/issues/21068) | [PR #8971](https://github.com/qgis/QGIS/pull/8971) | Gereed |
| raster calculator in processing does not work with Aspect raster | [#21011](https://issues.qgis.org/issues/21011) | Kan niet worden gereproduceerd met 3.5 |  |
| Error opening network KML page: Range downloading not supported by this server! | [#21091](https://issues.qgis.org/issues/21091) | [PR #8985](https://github.com/qgis/QGIS/pull/8985) | Gereed |
| Can\'t add a virtual field or update a existing field of a WFS layer using the field calculator | [#21086](https://issues.qgis.org/issues/21086) | [PR #8990](https://github.com/qgis/QGIS/pull/8990) | Gereed |
| Opening shapefiles in ZIP gives Invalid Datasource | [#21097](https://issues.qgis.org/issues/21097) | Kan niet worden gereproduceerd met 3.5 |  |
| spatialite, edit table in dbmanager is broken in master Fault: no such table: pg_description | [#21151](https://issues.qgis.org/issues/21151) | [PR #9086](https://github.com/qgis/QGIS/pull/9086) | N/B |
| Delimitedtext layer saves absolute path when project in relative path mode | [#21150](https://issues.qgis.org/issues/21150) | [PR #9099](https://github.com/qgis/QGIS/pull/9099) | Gereed |
| field calculator doesn\'t load values for gpkg containing blank spaces or n dash (hypen) in field names | [#21100](https://issues.qgis.org/issues/21100) | [PR #9071](https://github.com/qgis/QGIS/pull/9071) | Gereed |
| Can\'t open feature form when when the primary key of Spatialite layer is created in text type | [#21176](https://issues.qgis.org/issues/21176) | [PR \#](https://issues.qgis.org/projects/qgis/repository/revisions/7f61dc495491752fd26c7f3bad56adc1f8950e3f) | Nee (twijfelachtig) |
| Geopackage layer rename in DB Manager does not update f_table_name values in the layer_styles table or the Triggers | [#21227](https://issues.qgis.org/issues/21227) | [PR #9164](https://github.com/qgis/QGIS/pull/9164) | Niet mogelijk omdat het afhankelijk is van de nieuw geïmplementeerde mogelijkheid voor hernoemen in Browser |
| Layer Properties \> Load Style \> From database \> \'Other styles \...\' \> Description column contains Name text, should contain Description text (it is a geopackage layer) | [#21254](https://issues.qgis.org/issues/21254) | [PR #9170](https://github.com/qgis/QGIS/pull/9170) | Gereed |
| Comments in SQL query in DB Manager breaks the query | [#21271](https://issues.qgis.org/issues/21271) | [PR #9180](https://github.com/qgis/QGIS/pull/9180) | N/B |
| Bug with multiple Else items in rule-based style | [#21281](https://issues.qgis.org/issues/21281) | [PR #9181](https://github.com/qgis/QGIS/pull/9181) | Gereed |
| GetFeatureInfo not send Geometry when set into project | [#21172](https://issues.qgis.org/issues/21172) | Kan niet worden gereproduceerd met 3.5 | N/B |
| Geometry Checker Crashes | [#21259](https://issues.qgis.org/issues/21259) | [PR #9191](https://github.com/qgis/QGIS/pull/9191) | Gereed |
| QGIS crashes when createInstance() uses wrong constructor in a QgsProcessingAlgorithm subclass | [#21270](https://issues.qgis.org/issues/21270) | [PR #9193](https://github.com/qgis/QGIS/pull/9193) | Gereed |
| pasting features is very slow | [#21305](https://issues.qgis.org/issues/21305) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | Nee (twijfelachtig) |
| Attribute forms do not show anymore constraints messages | [#21266](https://issues.qgis.org/issues/21266) | Afgesloten als ongeldig na verscheidene testen en enige gesprekken met Giovanni Manghi | N/B |
| OGR provider returns an empty set for GPKG uniqueValues(0) | [#21311](https://issues.qgis.org/issues/21311) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | Nee (twijfelachtig) |
| \"default value\" is not applied when pasting features | [#21304](https://issues.qgis.org/issues/21304) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | Nee (twijfelachtig) |
| Postgis very noticeable slowdown when opening the attributes table if the table has a large number of columns | [#21303](https://issues.qgis.org/issues/21303) | [PR #9219](https://github.com/qgis/QGIS/pull/9219) | Nee (twijfelachtig) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| gdal buildvrt missing an important param | [#20586](https://issues.qgis.org/issues/20586) | [PR #8927](https://github.com/qgis/QGIS/pull/8927) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| gdal:warpreproject missing old \'extra\' param | [#20721](https://issues.qgis.org/issues/20721) | [PR #8930](https://github.com/qgis/QGIS/pull/8930) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| Points inside polygons | [#20798](https://issues.qgis.org/issues/20798) | Kan niet worden gereproduceerd met 3.5 |  |
| IDW interpolation on csv point layer not working | [#20490](https://issues.qgis.org/issues/20490) | [PR #8942](https://github.com/qgis/QGIS/pull/8942) | [PR #8947](https://github.com/qgis/QGIS/pull/8947) |
| \[Processing\] Field calculator algorithm does not use the selected layer as default layer input | [#19686](https://issues.qgis.org/issues/19686) | [PR #8945](https://github.com/qgis/QGIS/pull/8945) | [PR #8949](https://github.com/qgis/QGIS/pull/8949) |
| v.surf.rst NOT WORKING IN QGIS 3.2.0 BONN | [#19472](https://issues.qgis.org/issues/19472) | [PR #8959](https://github.com/qgis/QGIS/pull/8959) | [Direct commit](https://github.com/qgis/QGIS/commit/c2465fc4a66425c296ffedb491d220a3db8ba453) |
| SVM Classification, SupportVectorMachineClassification(OpenCV)-Vector Field | [#20796](https://issues.qgis.org/issues/20796) | [PR #8960](https://github.com/qgis/QGIS/pull/8960) | [Direct commit](https://github.com/qgis/QGIS/commit/e0a8de477b04a6aa355d934c25ba37257bc63584) |
| GDAL/OGR Dissolve algorithm not properly working with point/multipoint layers | [#20025](https://issues.qgis.org/issues/20025) | [PR #8972](https://github.com/qgis/QGIS/pull/8972) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Build Virtual Vector tool: file created fails to load correctly | [#14374](https://issues.qgis.org/issues/14374) | Kan niet worden gereproduceerd met 3.5 |  |
| \"Convert map to raster\" algorithm does not export with transparent background despite the option | [#19866](https://issues.qgis.org/issues/19866) | [PR #8965](https://github.com/qgis/QGIS/pull/8965) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| \[GUI\] Disable edit tools when no layer is selected/available nor selected layer is in edit mode | [#18141](https://issues.qgis.org/issues/18141) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| \"Add Rectangle From 3 Points\" is enabled on a new project | [#20333](https://issues.qgis.org/issues/20333) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| v.buffer processing algorithm fails when using option \"Name of column to use for buffer distances\". | [#19377](https://issues.qgis.org/issues/19377) | [PR #8973](https://github.com/qgis/QGIS/pull/8973) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Problem with URLs to exclude from network settings | [#20933](https://issues.qgis.org/issues/20933) | [PR #8995](https://github.com/qgis/QGIS/pull/8995) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Truncated decimals in raster data set pixel size | [#21023](https://issues.qgis.org/issues/21023) | [PR #8996](https://github.com/qgis/QGIS/pull/8996) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Embedded layer style and labels properties can be modified within the layer styling panel | [#16339](https://issues.qgis.org/issues/16339) | [PR #9006](https://github.com/qgis/QGIS/pull/9006) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| processing: \"default output vector layer extension\" not respected by some tools | [#20557](https://issues.qgis.org/issues/20557) | [PR #8997](https://github.com/qgis/QGIS/pull/8997) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Unable to stop executing GDAL algorithm | [#20441](https://issues.qgis.org/issues/20441) | [PR #9026](https://github.com/qgis/QGIS/pull/9026) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Add option to control export features without categories in Processing GRASS algorithms | niet gerapporteerd | [PR #9003](https://github.com/qgis/QGIS/pull/9003) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Processing: v.net tools (GRASS) return empty outputs | [#19904](https://issues.qgis.org/issues/19904) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.salesman sequence HTML output | [#21142](https://issues.qgis.org/issues/21142) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.report and v.net.nreport algorithms failed | niet gerapporteerd | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| Unable to add WCS - bad WCS Request | [#21045](https://issues.qgis.org/issues/21045) | [PR #9005](https://github.com/qgis/QGIS/pull/9005) | [PR #9098](https://github.com/qgis/QGIS/pull/9098) |
| GeoNode API requests require a stronger minor version parsing | [#21093](https://issues.qgis.org/issues/21093) | [PR #9117](https://github.com/qgis/QGIS/pull/9117) | [PR #9141](https://github.com/qgis/QGIS/pull/9141) |
| Check Boxes + Setting Flags in Python in Ubuntu | [#20910](https://issues.qgis.org/issues/20910) | Kan niet worden gereproduceerd met 3.5 |  |
| SAGA openCV and processing tools | [#19540](https://issues.qgis.org/issues/19540) | Kan niet worden gereproduceerd met 3.5 |  |
| Error copying records between tables | [#21154](https://issues.qgis.org/issues/21154) | [PR #9065](https://github.com/qgis/QGIS/pull/9065) | [PR #9185](https://github.com/qgis/QGIS/pull/9185) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Mogelijkheid: Reparaties van problemen door Jürgen Fischer
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Attribute table will not allow letter \'N\' to be entered | [#21019](https://issues.qgis.org/issues/21019) | [Direct commit](https://github.com/qgis/QGIS/commit/99904f1f5e7b86a92f3ff50132fd89750fe858e7) | [Direct commit](https://github.com/qgis/QGIS/commit/3d4c6c4e3f3f270d46a419787eb20bd02f8e16d3) |
| Editing Oracle Spatial view in QGIS | [#20109](https://issues.qgis.org/issues/20109) | [Direct commit](https://github.com/qgis/QGIS/commit/855b3b4e26377647de5c5f9d38485f9f00bc9257) | [Direct commit](https://github.com/qgis/QGIS/commit/1b6329c3c03a07e46d9b1c53ccd7bc3b42b3b247) |
| Missing CP949 (Korean) encoding at Export Project to DXF menu | [#20838](https://issues.qgis.org/issues/20838) | [Direct commit](https://github.com/qgis/QGIS/commit/4e74c8b5480ac28aabc3c0b3eba2609d1a762e8a) | [Direct commit](https://github.com/qgis/QGIS/commit/c7a6b773f2a557b4f2082d0ef114edcd043def74) |
| GeoPackage Raster WEBP support | [#21083](https://issues.qgis.org/issues/21083) |  |  |
| Grass algorithms doesn\'t work from Processing Toolbox level (grass-7.7.svn folder problem) | [#21114](https://issues.qgis.org/issues/21114) | [Direct commit](https://github.com/qgis/QGIS/commit/febbc4f0b9e6f1e1c74c18bcb117148d6587ff87) | [Direct commit](https://github.com/qgis/QGIS/commit/3221b1c83fc00d4f292b2b767a27e4bfcef0f88b) |
| Fix substr help | [#21192](https://issues.qgis.org/issues/21192) | [Direct commit](https://github.com/qgis/QGIS/commit/2bed7ab0018696dba76d2c8053d22633a271486e) | [Direct commit](https://github.com/qgis/QGIS/commit/eb8e36c27dad5413936218893393031e7d0a9915) |
| \[OSGeo4W\] introduce with spatialindex 1.9 | fix in spatialindex | [Direct commit](https://github.com/qgis/QGIS/commit/29d44964529defd0aac94c89e747eee095a89f3a) | [Direct commit](https://github.com/qgis/QGIS/commit/af723c4942427fdce5b935560abd242c5c90ef0a) |
| osgeo4w: fix b6293f23c8c | [#21210](https://issues.qgis.org/issues/21210) | [Direct commit](https://github.com/qgis/QGIS/commit/eea4eda6a35f1a06f84f198249b51b169144c46f) |  |
| Expand ZipItem in foreground | [#21268](https://issues.qgis.org/issues/21268) | [Direct commit](https://github.com/qgis/QGIS/commit/407adc761ebe224a2d72df65551cdcf2addf1735) |  |
| dwg import: catch spline misinterpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/3aa2d9ff9bc673a6c11456524bb7bfb6532556a7) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support dxf encoding | [#15999](https://issues.qgis.org/issues/15999) | [Direct commit](https://github.com/qgis/QGIS/commit/e1562a7f1339952be186e924bf96241ce2d826bd) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: force polyline and hatch/ring continuity | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/b8c727f1d293b64d80c6d1cf29107e0477af3d42) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg/dxf import: fix angle and alignment handing of (m)texts | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/92e7faab665d1853191227c8aeb6c13a04c43537) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: fix exception | [#21177](https://issues.qgis.org/issues/21177) | [Direct commit](https://github.com/qgis/QGIS/commit/355deb5905861f263ae7bb03d2bc6fcea4ce5096) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: support nested blocks | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/d84c34e0b0ca3586543604a600f939c9024ca99a) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dwg import: handle wrong hatch interpretation | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/fd15c3e5b6253c2898dd23dd561121ac1874396c) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dxf export: fix svg scaling | niet in redmine | [Direct commit](https://github.com/qgis/QGIS/commit/4b55dbef0b60349c74e40d9fd0109f33bca19510) | [Direct commit](https://github.com/qgis/QGIS/commit/23c01de492546e119d5c1c98f97694f470dbd817) |
| dxf export: fix output of closed 3d polylines | [#20242](https://issues.qgis.org/issues/20242) | [Direct commit](https://github.com/qgis/QGIS/commit/56ec47328b9e24951b51c00144221c95f88c6c83) | [Direct commit](https://github.com/qgis/QGIS/commit/db823175cf5c89bc066621e34a8d922c2f80eb87) |
| dxf export: don\'t label invisible features | [#19604](https://issues.qgis.org/issues/19604) | [Direct commit](https://github.com/qgis/QGIS/commit/c389fad1ad0396cf9914dedc8d2e9a9c303cd8f8) | [Direct commit](https://github.com/qgis/QGIS/commit/87c9e18e5677d0d6e2c43d7ecb36afab84ff31fb) |
| support polyline width and generic line width | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/6bf2d9d4500977c65630add31bb2246f063e20e8) | [Direct commit](https://github.com/qgis/QGIS/commit/c10969e562eda37c0cb78d3ec6db4c1cd68b1106) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Jürgen Fischer](https://www.norbit.de/)
### Mogelijkheid: Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash bij toevoegen van bestaand veld aan vectorlaag | [#18954](https://issues.qgis.org/issues/18954) | [PR #8982](https://github.com/qgis/QGIS/pull/8982) | [PR #9042](https://github.com/qgis/QGIS/pull/9042) |
| Colour bars in colour chooser UI are rendered with interleaved stripes \[MAC\] | [#15984](https://issues.qgis.org/issues/15984) | [PR #9009](https://github.com/qgis/QGIS/pull/9009) | [PR #9020](https://github.com/qgis/QGIS/pull/9020) |
| Impossible to rename a layer style from the Styling Panel | [#17652](https://issues.qgis.org/issues/17652) | [PR #9021](https://github.com/qgis/QGIS/pull/9021) | [PR #9041](https://github.com/qgis/QGIS/pull/9041) |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | upstream: <https://github.com/OSGeo/gdal/issues/1243> |  |
| QGIS 3.4.2 crush at QgsApplication.initQgis() on Mac | [#20712](https://issues.qgis.org/issues/20712) | Kan niet worden gereproduceerd met 3.5 |  |
| QGIS freezes on MacOS 10.14 when launched from Launch Services (works ok when launched from terminal) | [#20381](https://issues.qgis.org/issues/20381) | veroorzaakt door Qt 5.11 gebruikt in officiële MacOS-pakket. Pakketten moeten opnieuw gemaakt worden met Qt 5.12 |  |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [PR #9035](https://github.com/qgis/QGIS/pull/9035) | [PR #9056](https://github.com/qgis/QGIS/pull/9056) |
| python error when running GRASS 7.6 tools in processing on mac OS | [#21269](https://issues.qgis.org/issues/21269) | probleem in officiële MacOS-pakket, workaround/reparatie voorgesteld in opmerking |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGis 3.4 reproducible crash while in idle state | [#20581](https://issues.qgis.org/issues/20581) | [PR #8988](https://github.com/qgis/QGIS/pull/8988) and [PR #9019](https://github.com/qgis/QGIS/pull/9019) | [PR #9027](https://github.com/qgis/QGIS/pull/9027) and [direct commit](https://github.com/qgis/QGIS/commit/9ea7f1efa44c47d4070a1623b18059014e658017) |
| crash at processing\....qgis:snapgeometries | [#18497](https://issues.qgis.org/issues/18497) | [PR #8966](https://github.com/qgis/QGIS/pull/8966) | [PR #9010](https://github.com/qgis/QGIS/pull/9010) |
| QgsExternalResourceWidgetWrapper crashes | [#20140](https://issues.qgis.org/issues/20140) | Duplicaat |  |
| Crash on vector edit (that has the 4326 CRS) is reprojected in CRS 3857 | [#19579](https://issues.qgis.org/issues/19579) | [proposed a libspatialindex PR](https://github.com/libspatialindex/libspatialindex/pull/126) |  |
| Adding new features in postgis fails with attribute window popup | [#20523](https://issues.qgis.org/issues/20523) | Werkt bij mij wel |  |
| Can\'t remove a constraint set on a field once saved | [#20516](https://issues.qgis.org/issues/20516) | [PR #9032](https://github.com/qgis/QGIS/pull/9032) | [PR #9229](https://github.com/qgis/QGIS/pull/9229) |
| QGIS 3.5 not loading or saving multi-dimensional arrays properly from PostGIS layers | [#20872](https://issues.qgis.org/issues/20872) | [PR #9048](https://github.com/qgis/QGIS/pull/9048) | NOG TE DOEN |
| Attribute Table refresh issue when deleting features from shapefile | [#18421](https://issues.qgis.org/issues/18421) | [PR #9152](https://github.com/qgis/QGIS/pull/9152) | [PR #9214](https://github.com/qgis/QGIS/pull/9214) |
| QgsVectorLayer from spatialite featureid problem | [#20633](https://issues.qgis.org/issues/20633) | Werkt in 3.5 en branch 3.4 (niet in 3.4.4) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping tooltip doesn\'t works when Advanced Digitizing tool is activate | [#18441](https://issues.qgis.org/issues/18441) | Kan niet worden gereproduceerd met 3.5 |  |
| Remove old settings for vertex markers | [#17366](https://issues.qgis.org/issues/17366) | Werkt zoals bedoeld |  |
| Snapping options in meters rounded to integers | [#20829](https://issues.qgis.org/issues/20829) | [PR #9168](https://github.com/qgis/QGIS/pull/9168) |  |
| Add the possibility to return a shp if ogr is not compiled with gpkg | niet gerapporteerd | [PR #9037](https://github.com/qgis/QGIS/pull/9037) |  |
| fix qgsRound for negative numbers | [#20861](https://issues.qgis.org/issues/20861) | [PR #9030](https://github.com/qgis/QGIS/pull/9030) and [PR #9025](https://github.com/qgis/QGIS/pull/9025) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Victor Olaya
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| algorithm create grid: reference point problem for calculating Y coordinates | [#20966](https://issues.qgis.org/issues/20966) | [Direct commit](https://github.com/qgis/QGIS/commit/e3516ab1b46137db36f3b7dbf4e4f2ee2df1eb70) |  |
| Error in Processing modeller | [#20609](https://issues.qgis.org/issues/20609) | Geen probleem meer. Kan het niet reproduceren. Ticket is gesloten door de originele rapporteur |  |
| Do not allow file input for tables or vctor layers if there are dependent fields | [#21055](https://issues.qgis.org/issues/21055) | [Direct commit](https://github.com/qgis/QGIS/commit/6eaa511eed775ce36328a3e1465c32dfb82507aa) |  |
| Deactivating/uninstalling plugin causes Python error when trying to edit a Processing model | [#19607](https://issues.qgis.org/issues/19607) | [PR #8957](https://github.com/qgis/QGIS/pull/8957) |  |
| Postgis DB selector for outputs fails to list schemas in selected DB | [#21099](https://issues.qgis.org/issues/21099) | [PR #9004](https://github.com/qgis/QGIS/pull/9004) |  |
| Regression: outputs of processing models are not assigned the specified styles | [#20573](https://issues.qgis.org/issues/20573) | [Direct commit](https://github.com/qgis/QGIS/commit/eb47288fac06692748c7017f6f125a1fc66e9561) |  |
| QGIS3: SagaUtils.py fails when comman contains non-latin characters | [#18617](https://issues.qgis.org/issues/18617) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] Wrong management of locale in output result path | [#19351](https://issues.qgis.org/issues/19351) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] SAGA algorithms cannot produce non-shp output | [#21089](https://issues.qgis.org/issues/21089) | [PR #9002](https://github.com/qgis/QGIS/pull/9002) |  |
| Extent selector shows layers with no spatial component (geometryless tables) | [#21129](https://issues.qgis.org/issues/21129) | [PR #9034](https://github.com/qgis/QGIS/pull/9034) (updated by Nyall in [PR #9038](https://github.com/qgis/QGIS/pull/9038)) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Victor Olaya
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| 32 bit floating geotiff showing as black. worked in 2.18 and 3.0 - not working 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/e261b7ff4fa15e762f7f3a73ff3dbc965181d991) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/0a3d241f96e83b86073efc86b51376c7cd5f6e4f) | - |
| ods tables are not loaded correctly in QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/ee6278f8dd1be7064db87be87fe31fa8943730ec) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/4e84cd44868e3b91def41057b7adf28767b4c273) | - |
| attributes in attribute table don\'t match attribute in identify results/labels with WFS layer | [#20865](https://issues.qgis.org/issues/20865) | [PR #9105](https://github.com/qgis/QGIS/pull/9105) | [PR #9113](https://github.com/qgis/QGIS/pull/9113) |
| KML loading bug | [#20173](https://issues.qgis.org/issues/20173) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/467b088edd18f90744bccac9ff6d83a6a5d92d93) and [GDAL 2.4 in](https://github.com/OSGeo/gdal/commit/ec4bd32cd591b672274383f7c06da1d58a2a3500) | - |
| Zoom to Layer does not respond to filtered WFS | [#20742](https://issues.qgis.org/issues/20742) | [PR #9118](https://github.com/qgis/QGIS/pull/9118) | [Direct commit](https://github.com/qgis/QGIS/commit/8834ec78207c091175cb0f48b518b6d2988f337d) |
| Processing time for GeoJSON 10 times slower in 3.4 | [#21085](https://issues.qgis.org/issues/21085) | [GDAL master commmit](https://github.com/OSGeo/gdal/commit/bd668db37eb6f176226ebbe7efe34cfac86a3cf6a) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/d6c38adfa28f75da0630f3e3ac26dbb501fc361e) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Martin Dobias
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[vertex tool\] Fix issue with hidden layers being editable | [#18434](https://issues.qgis.org/issues/18434) | [PR #8992](https://github.com/qgis/QGIS/pull/8992) | [Direct commit](https://github.com/qgis/QGIS/commit/2ad47198c446a1f541dca195439bb432da0dce6a) |
| \[vertex tool\] Fix vertex addition to polygon\'s first segment | [#20774](https://issues.qgis.org/issues/20774) | [PR #9024](https://github.com/qgis/QGIS/pull/9024) | [Direct commit](https://github.com/qgis/QGIS/commit/4423caff0994de64185fcc7b3acb5058ca047c14) |
| \[vertex tool\] Misleading message when deleting all nodes of a ring or a part | [#17754](https://issues.qgis.org/issues/17754) | niet gerepareerd! vereist een behoorlijk uitgebreide te maken reparatie |  |
| \[vertex tool\] Improvements to the right-click behavior to pick locked feature | N/B | [PR #9052](https://github.com/qgis/QGIS/pull/9052) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] right-click to loop through editable features | N/B | [PR #9087](https://github.com/qgis/QGIS/pull/9087) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] misc small UX improvements | N/B | [PR #9116](https://github.com/qgis/QGIS/pull/9116) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] two more UX fixes | N/B | [PR #9130](https://github.com/qgis/QGIS/pull/9130) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] Few more UX improvements | [#21283](https://issues.qgis.org/issues/21283) | [PR #9222](https://github.com/qgis/QGIS/pull/9222) | [PR #9227](https://github.com/qgis/QGIS/pull/9227) |

This feature was funded by [QGIS user group Germany](https://www.qgis.de/)

This feature was developed by [Martin Dobias](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[postgis\] Fix creation of new Z/M enabled, curved geometry type layers | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/07746dbc0e5b34e31e85e944fc6f53113721a696) | [Direct commit](https://github.com/qgis/QGIS/commit/a61abe5bb3b4c1b633f2f76b69a7f274abeb33d3) |
| \[categorized\] Fix blank layers when using categorized renderer | [#21188](https://issues.qgis.org/issues/21188) | [Direct commit](https://github.com/qgis/QGIS/commit/7714bfbfbe6acec1c193365a173c822cb72c4361) | N/B |
| Fix invalid data source message is always shown after dragging and dropping vector layers to QGIS window | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/a1d8d9ae5d8ff5130e3ccd179617b1e9c0bf4062) | N/B |
| \[processing\] Buffer algorithm should always export multipolygon layers | [#21191](https://issues.qgis.org/issues/21191) | [Direct commit](https://github.com/qgis/QGIS/commit/f22f182bcfd7b7f5b5d8f782f3df08ee9d705115) | [Direct commit](https://github.com/qgis/QGIS/commit/f4866402f7ecf759598e652d5d640dd1fdc48c50) |
| \[processing\]\[gdal\] Fix polygonize field name is ignored | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/06d5b996bfc37f2877ecbf708af608952420ed45) | [Direct commit](https://github.com/qgis/QGIS/commit/ae21d07d4b082ede7b56941aaa1ce57fad8cdb9a) |
| \[processing\] Allow matrix parameters to be correctly set for model child algorithms | [#20914](https://issues.qgis.org/issues/20914) | [Direct commit](https://github.com/qgis/QGIS/commit/eeff02fc14b96a6d3f95ac2122d1d82654dcf268) | [Direct commit](https://github.com/qgis/QGIS/commit/d5900557bdb25f4e285638bf1de85f43430ba15d) |
| \[processing\]\[gdal\] Ensure that GDAL algs output the CORRECT generated filename for outputs | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/c93775f6b177ab2f64bd347c9a6f78896cee78dd) | [Direct commit](https://github.com/qgis/QGIS/commit/93c135f97cad06a1ff703ae1839397f14cb82b3d) |
| \[processing\]\[gdal\] Fix incorrect definition of gdal_warp extra_param parameter | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/f54f5a4fe70792f4d7ea376e28edad88c4d35d4a) | N/B |
| Allow for exact calculation of symbol sizes with mixed layer units | [#21143](https://issues.qgis.org/issues/21143) | [Direct commit](https://github.com/qgis/QGIS/commit/867e39947b3f24d0b7714cd44e28126b61769340) | [Direct commit](https://github.com/qgis/QGIS/commit/33987fa5505ebc4cb9d83c195c49e5938f7c1f73) |
| Fix hang when WMS credentials requested | [#20826](https://issues.qgis.org/issues/20826) | [Direct commit](https://github.com/qgis/QGIS/commit/c9e761649820f8444a41da5e18850061b207c09c) | [Direct commit](https://github.com/qgis/QGIS/commit/ad6e1566a70d4f1a9d959a4de9f18bcae9dbd566) |
| Fix misc deadlocks/crashes in network requests, especially when SSL errors or timeouts occur | Meerdere | Meerdere | N/A \-- too intrusive |
| \[processing\]\[saga\] Fix definition of Multiple regression points/grids alg | [#21146](https://issues.qgis.org/issues/21146) | [Direct commit](https://github.com/qgis/QGIS/commit/4f8e2317d796881f942bbc6bdcbe60f3470f48fe) | [Direct commit](https://github.com/qgis/QGIS/commit/1916a7fd7ae4a3d5bb767bde76f3042dfd0a7474) |
| \[processing\] do not show geometryless layers in extent selector | [#21129](https://issues.qgis.org/issues/21129) | [Direct commit](https://github.com/qgis/QGIS/commit/5bfec27938ff95cd65c1cf5b88cc13ce26ca1d5d) | [Direct commit](https://github.com/qgis/QGIS/commit/06ee13263d842ea0d7e188107cb9033893b6c75f) |
| \[layouts\] Add checkbox to disable raster tiling for PDF/SVG exports | [#19500](https://issues.qgis.org/issues/19500) | [Direct commit](https://github.com/qgis/QGIS/commit/60b8d05278cd8133e1c06108ba875960d56e90e5) | N/A \-- too intrusive |
| Fix empty strings in proxy exclude list results in proxy being skippe\\d for ALL hosts | [#20213](https://issues.qgis.org/issues/20213) | [Direct commit](https://github.com/qgis/QGIS/commit/cf1cf0fe455a42edf6db4ab9fa07c1ad641b16cb) | [Direct commit](https://github.com/qgis/QGIS/commit/34625110327c5bec4969c2a42cfa8c210bd3b630) |
| Avoid project being marked dirty as soon as its opened | N/B | [Direct commit](https://github.com/qgis/QGIS/commit/394e5d8d76480c1235c49e46d52f5f4a277cf824) | N/B |
| Fix loss of project when saving to QGZ format and path contains non-ascii chars | [#19567](https://issues.qgis.org/issues/19567) | [Direct commit](https://github.com/qgis/QGIS/commit/7d7462c33334a501167813d720fb2589d3c579ec) | [Direct commit](https://github.com/qgis/QGIS/commit/bfef851b1ca98a2c45117a2b1f911f7f1b7155b1) |
| Fix evaluation of data defined properties for subsymbols of subsymbols | [#18384](https://issues.qgis.org/issues/18384) | [Direct commit](https://github.com/qgis/QGIS/commit/9cf2ff31d86e6b7671aaca137a60a7b7a975ef62) | [Direct commit](https://github.com/qgis/QGIS/commit/7e25cea7e939248c8816d2739ccd44a31c606f11) |
| Fix shortest path algorithm can \"shortcut\" when using network in geographic coordinates | [#20997](https://issues.qgis.org/issues/20997) | [Direct commit](https://github.com/qgis/QGIS/commit/e75a88825665e7bb43c6c3cd1b2c22037cd29784) | [Direct commit](https://github.com/qgis/QGIS/commit/a3428e5f92b8b98cc753de0e9366f36e7ecc018e) |
| Fix project loading task never completes when project has embedded layers | [#21012](https://issues.qgis.org/issues/21012) | [Direct commit](https://github.com/qgis/QGIS/commit/7ad4b05112af0c35bd9a8e0526e8823a6b695335) | [Direct commit](https://github.com/qgis/QGIS/commit/6584fb295aed03c3167d056e1bac59a808a1abb5) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Hugo Mercier
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis 3.4.1 crashes when accessing methods of feature | [#20752](https://issues.qgis.org/issues/20752) | gesloten |  |
| Bad size request with a georeferenced raster | [#8272](https://issues.qgis.org/issues/8272) | Can\'t reproduce anymore in 3.5 |  |
| Postgresql: empty SAVEPOINTS | http://issues.qgis.org/issues/17535 | niet meer van toepassing |  |
| Range widget does not honor default value on not null column | [#20831](https://issues.qgis.org/issues/20831) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) and [PR #9033](https://github.com/qgis/QGIS/pull/9033) |  |
| Range widget gives NULL value in Attributes Form/Table | [#21125](https://issues.qgis.org/issues/21125) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| QGIS 3.4.1 advanced modification and snap block QGIS | [#20568](https://issues.qgis.org/issues/20568) | gesloten |  |
| Vertex markers not displayed properly for MultiPolygon features | [#19909](https://issues.qgis.org/issues/19909) | [PR #9036](https://github.com/qgis/QGIS/pull/9036) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| Cascading controls in forms | [#11264](https://issues.qgis.org/issues/11264) | triage, gesloten |  |
| \$length incorrect in expressions | [#19355](https://issues.qgis.org/issues/19355) | [PR #9063](https://github.com/qgis/QGIS/pull/9063) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Hugo Mercier](https://oslandia.com/)

{{<content-end >}}
