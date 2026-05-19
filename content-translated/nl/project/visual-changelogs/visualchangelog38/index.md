---
HasBanner: false
draft: false
releaseDate: 21-06-2019
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.8
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.8{#changelog38 }
![image1](images/projects/403e44c7e958cff5d07a1eaf12af76ade88c564d.png)

Datum uitgave 21-06-2019

QGIS 3.8 brengt een uitgebreide lijst nieuwe wijzigingen en heel veel polijsten van bestaande mogelijkheden - de hoogtepunten daarvan zullen we hier proberen te behandelen. Zoals altijd herinneren we u er aan dat QGIS een open bron project is en vragen u om als het mogelijk is ons werk te ondersteunen door donaties, sponsoring of bijdragen aan de documentatie van de code, website, enzovoort.QGIS

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de QGIS gemeenschap hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op qgis.org en help een handje!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Kaartgereedschap
### Mogelijkheid: Cartesiaanse maateenheden forceren bij meten van afstanden/gebieden
In 3.8, we added an option to the measurement tool which forces Cartesian measurements for distance or area measurements. Previously, the measurement tools always used ellipsoidal/geodesic area and distance calculations, but there\'s occasions when this is not desirable and users require pure Cartesian calculations instead.

![image2](images/entries/e912304d18194a43111a2f054b7f1dba931985d4.webp)

This feature was funded by [Oslandia](https://oslandia.com)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com)
## Gebruikersinterface
### Mogelijkheid: Knop Opslaan naar sjabloon
While QGIS has offered support for Project Templates for many years, we enhanced this in 3.8 and made it much simpler for users to create new templates. Now, users can create a new template from their current project by selecting \"Save To -\> Templates\" from the \"Project\" menu.

![image3](images/entries/8a99e041656f5d3d1fa504636aa36b0046efe532.webp)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Feature: Improved \"Zoom to Native Resolution\" behavior
We\'ve improved the \"Zoom to Native\" action, so it now works correctly with tiled (e.g. WMTS/XYZ/ArcGIS MapServer) layers, by zooming to the closest native tile resolution. Additionally, we tweaked tile rendering so that pixel-perfect rendering occurs when the map is viewed at a native tile resolution. The result: super-crisp map renders when using tiled layer sources!

![image4](images/entries/61f13b52d685dcd67c7c9cc8dbb6daa269ed096a.webp)
### Mogelijkheid: Lagen slepen en neerzetten in widgets Kaartlagen
We ondersteunen nu, om het gebruiken van grote projecten van QGIS te verbeteren, direct slepen en neerzetten van lagen vanuit de inhoud van de projecttabel naar elk widget dat vraagt om het selecteren van een laag (bijv. algoritmes van Processing). Voor complexe projecten, lokaliseren van een laag in de inhoud van de tabel en slepen is veel gemakkelijker dan het kiezen uit het combinatievak van de vlakke widget van de lagen!

Aanvullend, voor algoritmes van Processing, kunnen lagen direct uit het paneel Browser worden gesleept voor keuzes voor lagen om in te voeren.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Mogelijkheid: Tekenreeksen met meerdere tekens voor markeringen lettertypen
While QGIS has long offered support for rendering points using font-based character markers, we\'ve enhanced this functionality in 3.8 and now offer the ability to render multi-character strings! And since we\'re always aiming to make the QGIS application interface as user-friendly and pleasant to use as possible, we also took the opportunity to tweak the UI for font markers and squash a number of frustrating GUI issues which previous versions suffered from.

![image5](images/entries/a0f55caed98366ae6eaa0e413d425259aa613b9b.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Factor  afstand label voor renderer Puntverplaatsing
Een andere aanvulling op de nieuwe mogelijkheden voor symbologie in 3.8 is een nagelnieuw besturingselement voor een factor labelafstand voor markeringen van Puntverplaatsing. Deze optie maakt het mogelijk verplaatste markeringen te plaatsen op een afstand die is gebaseerd op de diagonale grootte van de feitelijke markering, in plaats op een vaste afstand.

![image6](images/entries/7be374a464bde6d79745c1fedfc6075886f09b31.webp)

Deze mogelijkheid werd ontwikkeld door henrik
### Mogelijkheid: Symbooltype Hash-lijn
QGIS loves cartography, and we know you love making pretty maps! So we\'ve added a brand-new line symbology option for \"Hashed Lines\". This line symbol type is designed to replicate the ArcGIS Hash Line symbol layer type, and allows for a repeating line segment to be drawn over the length of a feature (with a line-sub symbol used to render each individual segment).

Alle beschikbare opties voor de bestaande symboollaag Markering zijn ook beschikbaar voor symbolen-lijnen, - bijv. eerste/laatste punt, middelpunten, regelmatige intervallen, data-bepaalde intervallen, etc. De lengte en hoek van de symbolen-lijn kan ook data-bepaalde 'override' hebben, die per lijnsegment worden geëvalueerd, wat het mogelijk maakt dat de symbolen-lijn van grootte en hoek wijzigt over de lengte van één enkel gerenderd object.

![image7](images/entries/d540197d4a5088df43cac495dc1a88b931131cfe.webp)

Deze mogelijkheid werd mogelijk gemaakt door anonymous

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Gemiddelde hoeken lijnen voor symbologie Markering en Symbolen-lijn
In previous QGIS versions, when a marker line was rendered using interval or center point place placement, the symbol angles were determined by taking the exact line orientation at the position of the symbol. This often leads to undesirable rendering effects, where little \"jaggies\" or corners in lines which occur right at the position of the symbol cause the marker to be oriented at a very different angle to what the eye expects to see.

We willen dat uw kaarten zo mooi mogelijk zijn, dus in QGIS 3.8 wordt de hoek van de markering in plaats daarvan berekend over een gespecificeerde afstand aan beide zijden van het symbool. Bijv. voor het middelen van de hoek van de lijn over 4mm betekent dat we de punten langs de lijn op 2mm van elke kant van de plaatsing van het lijnsymbool nemen, en die gebruiken in plaats van de lijnhoek voor dat symbool te berekenen. Dit heeft het effect van gladder maken (of verwijderen!) van hele kleine afwijkingen van de lijnrichting in zijn geheel, resulterend in een veel nettere visuele oriëntatie van markeringen of symbolen-lijnen.

Net als voor alle instellingen van symbolen kunnen de afstand voor het gladder maken van de gemiddelde hoek worden ingesteld in mm/pixels/kaarteenheden/etc, en ondersteunt data-bepaalde waarden. Gesloten ringen overwegen ook door te lopen langs deze gemiddelde hoeken vanuit het start-/eindpunt.

Deze optie is beschikbaar voor zowel het symbool Markering als de nieuwe typen symbolen-lijn.

![image8](images/entries/4101a09e0fa63aada9acce23092bb29e16db1114.webp)

Deze mogelijkheid werd mogelijk gemaakt door anonymous

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Instellingen voor verschuiving van symboollagen Puntpatroonvulling
To round out the new symbology options we\'ve added in 3.8, the Point Pattern Fill symbol type has a new setting allowing for offsetting the markers in the pattern by a preset (or data-defined!) amount. This opens the door for many styling possibilities which were not possible in earlier versions, and further increases our compatibility with converted ArcGIS symbol and layer styles.

![image9](images/entries/0cda10ddf2bac42e77b7cfc9ada813e4a26353a5.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Live effect Vervagen straal is nu hi-dpi vriendelijk
QGIS 3.8 brings a highly-desired fix to layer effects\' blurring radius (aka strength). In earlier QGIS versions, these blur settings did not take into account the DPI of the map render --- resulting in inaccurate effects rendering when exporting canvases/layouts at high resolutions. In 3.8, this was fixed and high-resolution map exports now match the results shown on the map canvas and are completely resolution-independent.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
## Labelen
### Mogelijkheid: Geometrie-generatoren voor labelen
This is a huge one! During the developer\'s meeting in A Coruña, Matthias Kuhn took the opportunity to implement a frequently-asked-for feature in our labeling engine: Geometry Generator support.

Just like Geometry Generators for symbols, we now allow label paths and positions to be calculated using dynamically-evaluated geometry expressions. You can take advantage of the rich support for geometry processing which QGIS\' expression engine exposes, and use this to do ALL sorts of pre-processing to your feature geometries before they are labelled. Want to place labels around the start or end point of linestring geometries? What about dynamically smoothing and simplifying the path used for labeling river features, based on the current map scale? How about buffering polygon objects inward by a percentage of their area, and then labeling around the perimeter of this shrunken area? Now, it\'s ALL possible, thanks to the power of labeling geometry generators!

![image10](images/entries/abc08ecfe2a879424b3f8e96c26b0391e342090e.webp)

This feature was funded by [QGIS user group switzerland](https://www.qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Kaartgereedschappen voor labels gebruiken nu klik-klik-gedrag
Like the other QGIS digitizing and map tools, the \"Move Label\" and \"Rotate Label\" tools now use the standard left-click-to-start edit, left-click-to-end behavior. Consistency is good!
## 3D-objecten
### Mogelijkheid: Brede lijnen en accentueren van randen van polygonen
Like all recent QGIS releases, in version 3.8 we\'ve significantly boosted QGIS\' 3D rendering capabilities. New 3D rendering features include:
- Configurable line width (in screen units) for \"simple\" 3D lines (in previous versions they were always 1px wide)
- Optioneel accentueren van randen van 3D-polygonen

![image11](images/entries/6e77320c7766d11f25893f9c2de2e7de57eab488.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: 3D-animaties exporteren
Another exciting change we\'ve introduced in QGIS 3.8 is the ability to export your 3D animations! These are exported as a series of png/jpg/\... images, which can be easily merged into .avi or other standard video files (using external tools).

![image12](images/entries/f0d7bb5632bfaa9c9feafb12e7b258c312ba66a6.webp)

This feature was funded by [Northumberland National Park Authority](https://www.northumberlandnationalpark.org.uk/)

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Terrein van online bronnen
Met deze nieuwe mogelijkheid voor versie 3.8, kunt u nu direct terreinen voor uw 3D-scenes ophalen vanaf online bronnen (bijv. tegels die worden gehost op AWS). Geen rasters meer als bronnen en het voorbereiden daarvan met DEM, eenvoudigweg deze optie inschakelen en out-of-the-box prachtige 3D-scenes bekijken!

This feature was funded by [Crowdfunding: More QGIS 3D](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Configuratie van veld voor hoek van weergave van camera
In QGIS 3.8, heeft het veld voor de weergave van de camera, waarmee 3D-scenes worden gerenderd, een nieuw te configureren veld voor instellingen van de weergave gekregen.

![image13](images/entries/13a7660953586fea69df8afea7f75dd5d457fce8.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
## Afdruklay-outs
### Mogelijkheid: Evenredige verdeling van afstand tussen items
We hebben nieuwe gereedschappen toegevoegd voor het automatisch opnieuw positioneren van items, zodat de horizontale of verticale afstand tussen de items gelijk is, om gemakkelijker uw perfecte afdruklay-out voor QGIS  te maken. Deze aanvulling rondt de bestaande opties voor het uitlijnen van items netjes af, en brengt meer van de kracht van specifieke toepassingen voor DTP direct in de ontwerper van afdruklay-out voor QGIS!

Deze mogelijkheid werd ontwikkeld door Matteo Nastasi
### Mogelijkheid: Noordpijlen maken
We\'ve listened to user feedback which indicated that the previous approach for creating north arrows within print layouts was too difficult, and consequently have added a new button in the Print Layout Designer for direct north arrow creation. This button is a shortcut to adding a picture item, setting it to a north arrow picture, and linking it with a map. The end result is identical, but it\'s much easier for new users to understand if we expose it as an explicit \"North Arrow\" item!

Even experienced users will likely appreciate the improved workflow, including automatically linking the picture rotation to a sensible default map choice (if a map is selected, it\'s used. If not, the topmost map item under the newly drawn north arrow is used. If there\'s none, the layout\'s \'reference map\' (or biggest map) is used as a fallback).

![image14](images/entries/7a0dd68c9a38f6e4b4f0177ae53978710df89ad5.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Expressies
### Mogelijkheid: Ondersteuning voor sorteren op voor functies voor samenvoegen
Omdat bepaalde expressies voor samenvoegen vereisen dat de resultaten in een bepaalde volgorde staan, maken we nu het beheren van de volgorde waarin objecten worden toegevoegd aan de samenvoeging bij het evalueren van de expressie, mogelijk.

E.g. `concatenate("Station",concatenator:=',', order_by:="Station")` will give a comma-separated list of station names in alphabetical order, rather than layer feature order.

![image15](images/entries/024918bb03f4620a2b5d32926322d0644c782bb8.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Simplified variant of \"attribute\" function
This improvement brings a second variant for the existing \"attribute\" function. The \"attribute\" function in previous QGIS releases required both a target feature and attribute name to be specified. The new version is much simpler, automatically using the current feature and only requiring an attribute name.

Bijv.

Eerder gedrag:

`attribute($currentfeature, 'name' )` -\> returns value stored in \'name\' attribute for the current feature

Verbeterd gedrag:

`attribute( 'name' )` -\> returns the value stored in \'name\' attribute for the current feature

It\'s just a faster shorthand version!

![image16](images/entries/13f09f754dea12a13b9d9aeb8606e86582e87e3f.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Punten ophalen van einde van geometerieën
We added negative index support to the point_n(), angle_at_vertex(), and distance_to_vertex() functions, allowing for retrieval of vertices counting backward from the end of a geometry.

![image17](images/entries/6eac3dcc7d9053f16733306878fb0cebf993737a.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Nieuwe functies voor expressies
As always, a new QGIS release brings a bunch of new functions for use within QGIS\' expression engine. These new functions add increased flexibility and power to the expression engine, and everywhere it\'s used throughout QGIS. This round, we\'ve added a set of new functions which make it super-easy to operate on file names and paths.

Nieuwe functies voor expressies ontwikkeld door Nyall Dawson van North Road:
- **base_file_name:** Returns the base name of the file without the directory or file suffix.
- **file_exists:** Returns true if a file exists
- **file_name:** Returns the file name from a full path
- **file_path:** Returns the directory/path from a full file path
- **file_size:** Returns a file size
- **file_suffix:** Returns a files suffix/extension
- **is_directory:** Returns true if a file path is a directory
- **is_file:** Returns true if a file path is a file

Nieuwe functies voor expressies ontwikkeld door Mathieu Pellerin van iMHere Asia:
- **array_all:** Returns true if an array contains the all values of a given array.
- **concatenate_unique:** Returns all unique strings from a field or expression joined by a delimiter.

![image18](images/entries/e83795c8c525c092fa9b68172ecdf9f713e5f15a.webp)
### Feature: New aggregation method: concatenate_unique
We added a new function `concatenate_unique()` to the expression engine (and Processing\'s \"aggregate\" algorithm) to support concatenating only unique values from a list or set of features.

![image19](images/entries/77c53d02f719feaf03e7e3d9cea8468645aa81e3.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
## Digitaliseren
### Mogelijkheid: Zwevend widget voor gevorderde invoer naast cursor
We hebben een optie toegevoegd om de huidige waarden afstand/hoek/X/Y als een zwevend venster naast de muiscursor weer te geven om de bestaande gereedschappen voor Geavanceerd digitaliseren gemakkelijker te gebruiken te maken. 

![image20](images/entries/c0703ea4a49115bfb398d174aa727c7e0fc67240.gif)

Dit werd mogelijk gemaakt door [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [Olivier Dalang and OPENGIS.ch](https://www.opengis.ch)
### Mogelijkheid: Geschakelde punten toevoegen op eindpunt
In QGIS 3.0, we added the ability to extend an existing line feature by clicking a \"+\" indicator at the start or end of line features when using the node tool. Version 3.8 extends this functionality by allowing addition of more than one vertex using the \"+\" button.

![image21](images/entries/a58caabea738a7e34529b9aeb2bb1d4cd307cf50.gif)

Dit werd mogelijk gemaakt door [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [Olivier Dalang and OPENGIS.ch](https://www.opengis.ch)
### Mogelijkheid: Verbeteringen aan bewerker voor punten
Voor deze uitgave verbeterden we de bewerker voor punten zodat het nu op de juiste wijze de *geselecteerde punten in het kaartvenster* zal koppelen aan de *punten voor handmatig bewerken van coördinaten in de tabel*.

![image22](images/entries/e518f5fc5b2decdbaba6272249cdfb3b6c2ad2fe.gif)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://www.opengis.ch)
## Formulieren en widgets
### Mogelijkheid: Bladeren door lijst met objecten toestaan
| arrows allow browsing the feature list in the attribute table in form view | the current edited feature can be highlighted and the map canvas automatically panned or zoomed
### Mogelijkheid: Widget HTML-formulier
Dankzij de genereuze bijdrage van A.R.P.A Piemonte (een van de Italiaanse regionale agentschappen voor het milieu) hebben we een nieuw widget voor een formulier ontwikkeld met HTML-body en toegang tot waarden van objecten en expressies.

![image23](images/entries/3932162893e8bb8d20d284d7a99ead2de9dac601.gif)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Aangepaste achtergrondkleur voor formulierwidgets
Dankzij de genereuze bijdrage van A.R.P.A Piemonte (een van de Italiaanse regionale agentschappen voor het milieu) hebben we u eindelijk bevrijd van de saaiheid van grijze achtergronden.

![image24](images/entries/8627ae1acd4ed30ae116e3b79679ecb5cad3241a.gif)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Door objecten in de attributentabel bladeren in formulierweergave
We\'ve added the possibility to browse through the attributes of features in a layer. This makes workflows for *asset management* a **lot** easier! You can:
1. Een filter definiëren
2. Door alle overeenkomende objecten bladeren
3. Nakijken en aanpassen

U kunt ook verschuiven en zoomen naar de geometrie van het object of het huidige object accentueren als u bladert.

(Dit vervangt de eerdere plug-in ItemBrowser met equivalente ingebouwde functionaliteit.)

![image25](images/entries/f034aaf2a173be885b5f8fca36e3b577795ad1de.webp)

This feature was funded by [regioDATA](https://www.regiodata-gmbh.de/)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://www.opengis.ch)
## Processing
### Feature: Add \"Save layer styles into GeoPackage\" option for Package Layers algorithm
QGIS loves GeoPackage, so it\'s likely no surprise that every new QGIS version brings improvements to GeoPackage handling! In 3.8, we enhanced the \"Package Layers\" Processing algorithm so that it now allows embedding the current layer styles directly into the packaged layers!

![image26](images/entries/ebabefc4ccc4b71dcffda0508834b709fddec635.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Analyse Overlappen 
Dit nieuwe algoritme voor Processing berekent het gebied en het bedekkingspercentage waarmee objecten op een invoerlaag worden overlapt door objecten uit een selectie van overleglagen. Nieuwe attributen worden toegevoegd aan de uitvoerlaag die het totale overlappende gebied aangeven en het percentage van de invoerobjecten die worden overlapt door elk van de geselecteerde overleglagen.

This is quite a common GIS task request, yet is full of traps for inexperienced users, and the amount of manual data work usually done by users to calculate these figures can often lead to mistakes and inaccurate results. We want to make spatial analysis as easy and foolproof as possible, so we\'ve added Overlap Analysis as an inbuilt tool which allows this task to be done in a single step without risk of human error.

![image27](images/entries/d265fa2b9bab9184d25244f0cd8aececb5136e66.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Afronden van waarden toestaan in Uitnemen/clippen op bereik
We\'ve added a parameter to the Processing algorithm \'Extract Layer Extent\' to round the extent bounding box coordinates to a certain interval. While rounding, the bounding box will only ever be enlarged, to ensure it will always cover the input data set. (I.e. the x and y minimum coordinates are rounded down, and x and y maximum coordinates are rounded up).

![image28](images/entries/6b783ea6f8bb83c8f45844681ed7221126be4782.webp)

Deze mogelijkheid werd ontwikkeld door Raymond Nijssen
### Mogelijkheid: Nieuwe opties voor automatisch vullen van batch Processing
In QGIS 3.8 we moved the existing \"double click column header\" to fill values down functionality to a new \"Auto fill\" button in the Processing Batch dialog, making this feature much more user-discoverable (we suspect many users had no idea this handy shortcut even existed!). In addition, we\'ve added TONS of new functionality to easily auto-populate the batch table. These include:
- File or layer parameters can now be batch populated by searching for files in a directory with a matching filename pattern (including recursive searches!). Ever needed to auto convert 100s of Shapefiles from a set of folders? Now it\'s easy to do!
- Een optie om berekende waarden uit een expressie van QGIS toe te voegen, wat het mogelijk maakt complexe op bereik gebaseerde waarden toe te voegen aan het dialoogvenster (bijv. waarden tussen 100-1000, verhogend met 50)
- A \"Calculate by Expression\" option allows for updating existing batch table cells using the results of a QGIS expression. These expressions can freely utilise other parameter values from the input batch rows, making it easy to craft the exact output file name you desire based on the other columns values in a batch row.

![image29](images/entries/e20e687223b884d70737f09130f0e9792974eed6.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: XYZ-rastertegels maken
We\'ve added a brand-new algorithm to generate raster \"XYZ\" tiles using the current QGIS project. Tile images can be saved as individual images in directory structure, or as a single file in the \"MBTiles\" format.

![image30](images/entries/b9af6c101c6c22836c4dec3b78a6ce3d6b7e1bcd.webp)

Deze mogelijkheid werd mogelijk gemaakt door Hansestadt Herford, SWK mbH, Datenbankgesellschaft mbH

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Wederopstanding van de provider OTB
QGIS 3.8 brengt de provider OTB voor Processing terug, die werd verwijderd bij de update naar QGIS 3.0. De provider werd bijgewerkt om alle nieuwigheden te gebruiken die beschikbaar zijn in Processing in QGIS 3, en is wederom out-of-the-box beschikbaar voor al uw wensen op het gebied van analyses van afbeeldingen!

(*Note that OTB is a third party dependency which must be manually installed by users. Instructions on installing OTB are available \`here \<https://gitlab.orfeo-toolbox.org/orfeotoolbox/qgis-otb-plugin#open-processing-settings\>\`\_\_*)

![image31](images/entries/77dfad7d869283213cfc54a96e5ced2ad69d259a.webp)

Deze mogelijkheid werd ontwikkeld door Rashad Kanavath
### Mogelijkheid: Variabelen voor expressies voor een model
We\'ve added a new \"Model Variables\" dock panel to the model editor, allowing you to create and set custom expression variables for use in your Processing models. These variables are available anywhere expressions are evaluated within the model, so you can use them as input parameter values for child algorithms, within data-defined dynamic parameters, etc.

The prime use case here is for models which use a constant value throughout multiple steps within the model (e.g. \@target_resolution: a target raster resolution, \@max_simplification: a simplification value for input features coming from different sources, etc). Previously, you\'d need to hunt down and replace these values in multiple places when you wanted to tweak them. By replacing them with variables in your model you only have a single place you need to edit these values when you want to adjust them!

Modelvariabelen worden opgeslagen binnen een individueel model van Processing zelf, en worden niet weergegeven buiten het dialoogvenster van Grafische modellen bouwen.

![image32](images/entries/dfd820ccdc499878a5d7c818f03cd2d586311945.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterde Grafische modellen bouwen UI
We\'ve added numerous usability improvements to the Processing Graphical Modeler, including
- De aanvulling van nuttige Helptips bij het met de muis gaan over componenten van het model
- Algoritmes en invoer verbonden aan de componenten van het model worden geaccentueerd als u met de muis over verschillende delen van het model gaat, wat het veel gemakkelijker maakt de stroom van het model te visualiseren en verbindingen binnen complexe modellen
- Typen invoerparameters worden nu weergegeven in de titel van het dialoogvenster voor definitie van de parameters
- Het gegevenstype voor numerieke parameters kan nu worden gespecificeerd, wat invoer van alleen gehele getallen mogelijk maakt voor modellen

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritmes met bekende problemen vlaggen
Standaard verbergen we nu van derde partijen algoritmes met bekende problemen in de Toolbox van Processing, wat u helpt om frustaties te vermijden (of misleidende resultaten) bij het uitvoeren van deze algoritmes. Een nieuwe instelling in het scherm voor opties van Processing maakt het mogelijk deze algoritmes weer te geven, maar zij zullen in de Toolbox worden weergegeven met een pictogram Waarschuwing. Gebruik is op eigen risico!

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Raster Booleaanse logische OF/EN algoritmes
In version 3.8 we\'ve added new algorithms which calculate the boolean OR or AND for a set of input rasters. For AND, if all of the input rasters have a non-zero value for a pixel, that pixel will be set to 1 in the output raster, otherwise it will be set to 0. For OR, if ANY of the input rasters have a non-zero value for a pixel, that pixel will be set to 1 in the output raster, else 0.

Een parameter voor een verwijzingslaag stelt u in staat een bestaande rasterlaag te specificeren als verwijzing bij het maken van het uitvoerraster. Het uitvoerraster zal hetzelfde bereik, CRS, en dimensies voor de pixels hebben als deze laag.

By default, a nodata pixel in ANY of the input layers will result in a nodata pixel in the output raster. If you check the \'Treat nodata values as false\' option, then nodata inputs will be treated the same as a 0 input value.

Deze nieuwe algoritmes zorgen voor veel eenvoudiger berekeningen in rasters voor Booleaanse logica, zonder de complexiteit van het gebruiken van Raster calculator. Zij zijn ook dynamisch op schaal te brengen voor elk aantal invoerrasters (anders dan de Raster calculator), en zijn zo dus veel meer flexibel als zij worden gebruikt in uw modellen van Processing.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuwe typen invoerparameters voor afdruklay-outs en items van afdruklay-out
By adding new parameter types for Print Layouts and Print Layout items, we\'ve opened up QGIS 3.8 to a whole new world of Processing algorithms which operate on print layouts. These new parameter types allow for creation of Processing algorithms and graphical models which prompt users to select a print layout and/or an item on the layout when run.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuw type parameter voor schalen van kaarten
We\'ve added a new parameter type specifically for map scales, QgsProcessingParameterScale. Scale values are evaluated using self.parameterAsDouble, which return the map scale denominator (matching the standard in other parts of the QGIS API).

Parameters voor de schaal worden aan de gebruikers weergegeven in het standaard QgsScaleWidget, wat het combinatievak met vooraf gedefinieerde schalen omvat en een knop voor een sneltoets die overeenkomt met de huidige schaal van de kaart. Het toevoegen van dit nieuwe type parameter stelt u in staat algoritmes en modellen voor Processing te maken die bij de uitvoering een keuze voor een schaal vereisen.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Improved \"point\" parameter handling
We improved the workflow for algorithms with a \"point\" input parameter. When picking the point coordinate from a map you can now take advantage of QGIS snapping tools, allowing you to exactly match the point parameter to a feature\'s boundary.

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New \"Print Layout Map Extent to Layer\" algorithm
Voordeel trekkend uit de nieuwe faciliteiten voor de toegang tot afdruklay-outs in Processing, hebben we een nieuw algoritme toegevoegd dat een polygoonlaag maakt die het bereik van een kaartitem van afdruklay-out omvat. De laag voor de uitvoer bevat ook handige attributen die de grootte van de kaart (in eenheden voor de lay-out), schaal en rotatie specificeren.

If you\'ve ever wanted to create an advanced overview indicator, and the inbuilt layout tools haven\'t sufficed --- this new algorithm is for you!

![image33](images/entries/a10b7ebe75528742860a666be9de2d1365de3b73.webp)

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Velden X/Y toevoegen aan laag
Dit nieuwe algoritme is een handige sneltoets voor het toevoegen van velden X en Y (of latitude/longitude) aan een puntenlaag. U kunt zelfs de waarden X/Y berekenen met een verschillend coördinaten referentiesysteem van de laag (bijv. velden latitude/longitude maken voor een laag in een geprojecteerd CRS).

![image34](images/entries/5633452beec85bb6486092463af4553c02aa6165.webp)

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \"Join attributes by nearest\" algorithm
U kunt nu koppelingen K-nearest neighbour uitvoeren vanuit de Toolbox van Processing!

QGIS 3.8 brengt een nieuw algoritme die een invoer vectorlaag neemt en een nieuwe vectorlaag maakt met aanvullende attributen in zijn attributentabel. De aanvullende attributen en hun waarden worden uit een tweede vectorlaag genomen waarbij objecten worden gekoppeld door de dichtstbijzijnde objecten uit elke laag te zoeken.

Standaard wordt alleen het enkele dichtstbijzijnde object gekoppeld, maar optioneel kan de koppeling in plaats daarvan de n-dichtstbijzijnde objecten gebruiken. Als een maximum afstand wordt gespecificeerd, dan zullen alleen objecten die dichterbij liggen dan deze afstand overeen komen.

![image35](images/entries/f78e2f7a712f8a5cc1d5e9e20b4bb378598c1180.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Algoritme Grass r.geomorphon 
The upstream GRASS team has been hard at work creating a new GRASS module for terrain analysis --- \"r.geomorphon\". In 3.8 we expose their efforts via a new Processing tool, which calculates geomorphons (terrain forms) and associated geometry using a machine learning approach.

![image36](images/entries/a0026a05eea40004dfd250cf1a2ff492fdeb1b58.webp)
### Mogelijkheid: GDAL algoritme Pansharpening 
Another third party tool which we\'ve added to the Processing toolbox in QGIS 3.8 is the GDAL pansharpening tool. Now it\'s easy to take advantage of this fast, powerful tool in your Processing analysis scripts and models.

![image37](images/entries/35c02288524968f8ea021f9a64fcd64b9ec328f9.webp)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Mogelijkheid: Parameter voor voorvoegsel nieuwe velden voor algoritmes vooroverleggen
We\'ve added overlay layer fields prefix parameter for the following algorithms:
- Algoritme Kruising
- Algoritme Kruisingen van lijnen
- Algoritme Symmetrisch verschil
- Algoritme Verenigen

Dit kan handig zijn om te voorkomen dat niet uniek benoemde velden botsen bij het samenvoegen van lagen.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
## Browser
### Mogelijkheid: Directe toegang tot werkbladen van XLSX/ODS-bestanden
QGIS 3.8 brengt zelfs nog meer kracht naar het paneel Browser en geeft nu alle werkbladen weer uit werkbladbestanden (bijv. Microsoft Excel en LibreOffice Calc-bestanden) in de boom van bestanden in de Browser.

![image38](images/entries/f311137d05c73b9ba673d6b68669b7117589dacd.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Algemeen
### Mogelijkheid: Projecten van QGIS binnen bestanden van GeoPackage
Did we already say that QGIS loves GeoPackage? Need any more proof of this? Well, in QGIS 3.8, we\'ve added to ability to store QGIS projects directly inside GeoPackage files! Now you can create a totally self-contained GeoPackage which embeds a QGIS Project AND all the data used by the project. (Let\'s see Shapefiles match that one!)

![image39](images/entries/8750f1c2e3c3919926fd2cb97488da071f7efc85.webp)

This feature was funded by [QCooperative](https://www.qcooperative.net)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Veel verbeterde afhandeling voor transformeren van coördinaten
Dankzij het onderliggende werk van de onvermoeibare teams van PROJ en GDAL ondersteunt QGIS nu heel veel verbeteringen in mogelijkheden voor geodetie en transformatie! Hoogtepunten omvatten:
- The PROJ CRS database is now used to populate QGIS\' CRS selection lists, removing the custom database we used in previous releases. This means that ALL responsibility for CRS definitions and updating these sit were they belong, upstream in the PROJ library \-- and consequently you can expect to see QGIS CRS definitions being a closer match to the official definitions, and newer CRS definitions will be added much faster than in previous releases.. This change also means we\'ll be an exact match for projection handling as all other open-source geospatial tools which have completed the port to the latest PROJ version, such as GDAL 3.0.
- We now rely entirely on PROJ\'s wonderful logic for generating the best coordinate operation to transform between CRS pairs. This means (amongst other stuff), we correctly support complex things like operations which require a \"pivot datum\", e.g. transformation to and from the GDA2020 coordinate systems.
- In plaats van de oudere benadering die QGIS gebruikte voor het transformeren van datums (onze eigen tabel blijven rondslepen of als bestanden voor verschuiven van rasters kunnen worden gebruikt), gebruiken we nu PROJ om dit te bepalen. Dit wijzigt de weergegeven gebruikersinterface aanmerkelijk als een gebruiker heeft geopteerd voor het handmatig kiezen van een uit te voeren transformatie als meerdere transformaties bestaan, en geven nu een vereenvoudigde lijst van beschikbare (en niet-beschikbare) paden weer.
- We also use PROJ\'s database to populate lists of available ellipsoids for use in distance and area calculations. This has cleaned up the ellipsoid choices considerably, and added many additional ellipsoid definitions as a result.
- De UX voor het notificeren van gebruikers voor problemen in transformaties van coördinaten is enorm verbeterd, bijv. gebruikers worden nu gewaarschuwd als een meer nauwkeurig transformatie mogelijk is, maar niet te gebruiken op hun systeem (wegens ontbrekende .GSB-bestanden voor verschuiven van rasters). Waar mogelijk presenteren we gebruikers directe links voor het downloaden van deze vereiste/gewenste bestanden voor verschuiven van rasters. De intentie hier is om er voor te zorgen dat gebruikers worden geïnformeerd als transformaties kunnen worden verbeterd, in plaats van stilletjes terug te vallen op minder nauwkeurige opties.
- Users also now have the option of placing grid shift files in a \"proj\" folder under their QGIS user profile. This change means users can install grid shift files and make them available in QGIS without requiring administrative rights.
- We\'ve also completed a project which began back in the lead-up to 3.0, which ensures that project-specific transformation pathway settings are correctly respected EVERYWHERE a coordinate transform is performed. This also means we\'re ready for the next stage in handling 4d temporal based coordinate transforms (when these start to land in 2020 and beyond).

A lot of this is only possible thanks to improvements in the underlying PROJ and GDAL libraries, which landed as a result of the GDAL \"barn raising\" effort. On the QGIS side, it was ONLY possible thanks to funding from the Australian ICSM.

This feature was funded by [ICSM](https://www.icsm.gov.au/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Gegevensproviders
### Mogelijkheid: provider Postgres: ondersteuning toegevoegd voor gemaakte kolommen voor identiteit
Deze mogelijkheid werd ontwikkeld door jef-n
### Mogelijkheid: Ondersteuning lijst tekenreeksen voor compatibele lagen
QGIS 3.8 now fully supports disk-based layers with String List fields, allowing you to take advantage of QGIS\' flexible handling of list field types with these formats.

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
### Mogelijkheid: Veel verbeterde afhandeling voor afhandeling ArcGIS MapServer
We bouden de provider ArcGIS MapServer opnieuw op en voegden significante verbeteringen door ten opzichte van eerder versies:
- Getegelde lagen worden nu progressief geladen, met onmiddellijke terugkoppeling
- We optimaliseerden de provider significant, wat resulteert in veel sneller opnieuw tekenen
- Lagen van MapServer respecteren nu correct instellingen voor authenticatie en instellingen voor verwijzingen van HTTP.
- \"Nested\" services are correctly shown in the QGIS browser panel
- Services voor ImageServer kunnen met de provider worden toegevoegd

Eindresultaat: lagen van MapServer zijn nu zo glad als zijde in QGIS!

Deze mogelijkheid werd ontwikkeld door Nyall Dawson (North Road) & Mathieu Pellerin (iMHere Asia)
### Mogelijkheid: SQL Server: afhandelen van geometrieën v2, inclusief gebogen en geometrieën Z/M
SQL Server users rejoice: QGIS now fully supports curved geometry types (and other \"version 2\" geometry fields)!

In past QGIS versions, the SQL Server provider would only handle version 1 type geometries, and could only show straight feature types. In 3.8, we\'ve added full support for version 2 geometries. This change also allows full support for Z or M enabled geometry types! Additionally, we fixed several known issues with geography field types.

This feature was developed by [Tamas Szekeres](https://github.com/szekerest)
### Mogelijkheid: WMS: Één filter definiëren voor verscheidene lagen
Soms dient u hetzelfde filter te definiëren voor elke geselecteerde laag bij het maken van een verzoek voor WMS (bijv. voor toegang tot gebruiker-specifieke gegevens). In eerdere versies van QGIS moesten we het filter definiëren in de indeling:

`&FILTER=layer1:"column1" = 'value1';layer2:"column1" = 'value1';layer3:"column1" = 'value1'`

With QGIS 3.8, we\'ve simplified this, and now allow the filter format:

`&FILTER=layer1,layer2,layer3:"column1" = 'value1'`

Deze mogelijkheid werd mogelijk gemaakt VEOLIA

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Ondersteuning voor bogen bij exporteren naar DXF
You can now export curved geometry layers to DXF format without segmentizing the features --- no more loss of curves!

![image41](images/entries/d0543abc36459754e4e3630e3703f0f1169ba7b3.webp)

Dit werd mogelijk gemaakt door [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer in samenwerking met Matthias Kuhn
## QGIS Server
### Mogelijkheid: Grootte configureren voor GetLegendGraphic mogelijk
| For this release we improved how the legend for QGIS servers handles the size of symbols which are scaled by map units. | Whenever possible, the server will determine the legend size based on the map canvas and resolution. Even more, for cases where this information is not available in the GetLegend request, it is now possible to configure a *default scale* in the project, symbols in the legend will then be drawn in the size they will have when rendered at this scale.

This feature was developed by [David Signer, OPENGIS.ch](https://www.opengis.ch)
## Plug-ins
### Mogelijkheid: Ondersteuning voor afhankelijkheden voor plug-ins
In QGIS 3.8, we\'ve introduced a long-sought-after feature for QGIS plugin developers: the ability to specify dependencies for your plugins.

To add a plugin dependancy, you can use the new metadata \"plugin_dependencies\". The format is a comma-separated list of PIP-like plugin names (with optional version). E.g:

`plugin_dependencies=GeoCoding,IPyConsole==1.9`

Het voorbeeld hierboven vereist:
- Een versie van GeoCoding
- Versie 1.9 van IPyConsole

Wanneer een plug-in wordt geïnstalleerd wordt de metadata geparset en aan de gebruiker zal een dialoogvenster worden gepresenteerd dat de afhankelijkheden vermeld. De gebruiker kan dan besluiten wet te doen met de afhankelijkheden:
- Installeren
- Upgraden/downgraden
- Niets doen

![image40](images/entries/28da67ad96ccda7a8a64b261db17bf33be4b3f69.gif)

This feature was funded by [GISCE TI](https://gisce.net/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it/)
## Programmeerbaarheid
### Mogelijkheid: Ondersteuning voor SQL-syntaxis REGEXP voor provider SpatiaLite en verbindingen voor Python
We\'ve enabled REGEX to be used with the spatialite provider. (This comes in handy when setting filters!). We\'ve also added support for this syntax via any python connections made through Qgis.utils\'s \"spatialite_connection\" API - allowing you to use REGEXP in your SQL queries from within DB Manager.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Zoeken naar Nearest Neighbour in QgsSpatialIndex
We hebben API toegevoegd om nauwkeurige zoekacties naar dichtstbijzijnde buren mogelijk te maken, gebaseerd op zoekacties QgsGeometry to QgsGeometry via QgsSpatialIndex. In eerdere versies van QGIS waren alleen zoekacties point to geometry nearest neighbour mogelijk. Maar met deze wijziging kunt u veilig en nauwkeurig QgsSpatialIndex gebruiken om de dichtstbijzijnde buren tussen elk type geometrie te bepalen.

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Raster Calculator verkeerde resultaten | [#21405](https://issues.qgis.org/issues/21405) | gerepareerd in master |  |
| QGIS server negeert volgorde van renderen bij laden van oudergroep | [#21917](https://issues.qgis.org/issues/21917) | [PR #9878](https://github.com/qgis/QGIS/pull/9878) | Gereed |
| WMS Client: GetFeatureInfo in JSON format doesn\'t display numeric attribute values | [#21735](https://issues.qgis.org/issues/21735) | [PR #9879](https://github.com/qgis/QGIS/pull/9879) | Gereed |
| Crash bij toevoegen van bestaand veld aan vectorlaag | [#22100](https://issues.qgis.org/issues/22100) |  |  |
| Prioriteit voor labelen niet uitgegrijsd als data-bepaalde instellingen zijn ingeschakeld | [#22077](https://issues.qgis.org/issues/22077) | Ongeldig |  |
| \$length return bad value | [#22105](https://issues.qgis.org/issues/22105) | werkt bij mij wel (en voor iedereen) |  |
| Relation reference widget wrong feature when \"on map identification\" | [#22071](https://issues.qgis.org/issues/22071) |  |  |
| Map composer: \"href\" HTML attribute issue in PDF output | [#22075](https://issues.qgis.org/issues/22075) | won\'t fix |  |
| Probleem bij exporteren van rasterlaag naar Geopackage | [#20848](https://issues.qgis.org/issues/20848) | [PR #10036](https://github.com/qgis/QGIS/pull/10036) | Gereed |
| Nieuw vector Shapefile POLYGON maken | [#22107](https://issues.qgis.org/issues/22107) | ongeldig |  |
| \"Export to PostgreSQL\" python error if rather schema has an uppercase letter in its name | [#22035](https://issues.qgis.org/issues/22035) | [PR #10063](https://github.com/qgis/QGIS/pull/10063) |  |
| Relation reference widget wrong feature when \"on map identification\" | [#22071](https://issues.qgis.org/issues/22071) | [PR #10047](https://github.com/qgis/QGIS/pull/10047) | Gereed |
| DB Manager importeert verkeerde gegevens | [#22033](https://issues.qgis.org/issues/22033) | [PR #10077](https://github.com/qgis/QGIS/pull/10077) | Gereed |
| QGIS crasht bij het filteren van een laag met een veld voor een bijlage | [#21775](https://issues.qgis.org/issues/21775) | Opgelost door Nyall |  |
| Raster calculator, abs() werkt niet | [#29824](https://github.com/qgis/QGIS/issues/29824) | [PR #29965](https://github.com/qgis/QGIS/pull/29965) | Gereed |
| Geldige link URL naar bestand mislukt in venster Objecten identificeren | [#29879](https://github.com/qgis/QGIS/issues/29879) | [PR #29967](https://github.com/qgis/QGIS/pull/29967) | Gereed |
| QgsProject.instance().clear() crasht QGIS als venster LayoutDesigner Window open is | [#29821](https://github.com/qgis/QGIS/issues/29821) | [PR #29968](https://github.com/qgis/QGIS/pull/29968) | Gereed |
| QGIS Server WFS DescribeFeatureType advertises double precision virtual fields as integer | [#29767](https://github.com/qgis/QGIS/issues/29767) | [PR #29970](https://github.com/qgis/QGIS/pull/29970) | Gereed |
| QGIS crahst bij exporteren van een sjabloon | [#29798](https://github.com/qgis/QGIS/issues/29798) | [PR #29981](https://github.com/qgis/QGIS/pull/29981) | Gereed |
| Exporteren van Atlas als afbeelding mislukt als de bestandsnaam van de expressie een punt bevat | [#29980](https://github.com/qgis/QGIS/issues/29980) | [PR #29983](https://github.com/qgis/QGIS/pull/29983) | Gereed |
| Knoppen om de grootte van markeringen aan te passen op de tab Digitaliseren van het dialoogvenster Algemene instellingen werken niet | [#29987](https://github.com/qgis/QGIS/issues/29987) | [PR #29991](https://github.com/qgis/QGIS/pull/29991) |  |
| Map Composer crashes QGIS when copying mixture of elements in page layout | [#29747](https://github.com/qgis/QGIS/issues/29747) | [PR #30017](https://github.com/qgis/QGIS/pull/30017) | NOG TE DOEN |
| QGIS crashes with PostgreSQL views | [#29673](https://github.com/qgis/QGIS/issues/29673) | kan het niet reproduceren en kan geen terugkoppeling vragen |  |
| Browser - \"Project home\" folder shortcut does not appear when a new project is saved | [#29919](https://github.com/qgis/QGIS/issues/29919) | [PR #30025](https://github.com/qgis/QGIS/pull/30025) | NOG TE DOEN |
| Crash when calling QgsRasterHistogram.histogramVector | [#29700](https://github.com/qgis/QGIS/issues/29700) | [PR #30033](https://github.com/qgis/QGIS/pull/30033) | Gereed |
| Do not offer to \"Import settings from Qgis2?\" if no such settings exist | [#30082](https://github.com/qgis/QGIS/issues/30082) | [PR #30092](https://github.com/qgis/QGIS/pull/30092) | Gereed |
| In gpkg, query builder prevents autogenerate of pasted feature with same fid as hidden feature | [#30062](https://github.com/qgis/QGIS/issues/30062) | [PR #30096](https://github.com/qgis/QGIS/pull/30096) | NOG TE DOEN |
| Drag and drop geopackage from filesystem into map misses vector layers, loses names for raster layers | [#30050](https://github.com/qgis/QGIS/issues/30050) | [PR #30098](https://github.com/qgis/QGIS/pull/30098) | Gereed |
| Qgis crashes when try to identify a layer with duplicated fields | [#29937](https://github.com/qgis/QGIS/issues/29937) | [PR #30100](https://github.com/qgis/QGIS/pull/30100) | NOG TE DOEN |
| label properties will not saved to project files (buffer and background) | [#29882](https://github.com/qgis/QGIS/issues/29882) | works for me on release-3_4 and master |  |
| Saving edits to a layer with JSON field throws an error | [#30131](https://github.com/qgis/QGIS/issues/30131) | [PR #30137](https://github.com/qgis/QGIS/pull/30137) | Riskant? |
| Value relation widget settings lost on import of layer definition file | [#30115](https://github.com/qgis/QGIS/issues/30115) | [PR #30151](https://github.com/qgis/QGIS/pull/30151) | Riskant? |
| Unable to add new features in QGIS for PostGIS table using sequence for gid. Data type serial: \'integer overflow\' | [#30041](https://github.com/qgis/QGIS/issues/30041) | [PR #30184](https://github.com/qgis/QGIS/pull/30184) | Gereed |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| v.net.distance - node cost column | [#22013](https://issues.qgis.org/issues/22013) | [PR #10060](https://github.com/qgis/QGIS/pull/10060) | Gereed |
| shapefile to raster conversion does not work | [#21922](https://issues.qgis.org/issues/21922) |  |  |
| GRASS r.in.lidar.info, can only choose *.txt not the intended* .las | [#21910](https://issues.qgis.org/issues/21910) | [PR #10061](https://github.com/qgis/QGIS/pull/10061) | Gereed |
| SAGA OpenCV Image Analysis | [#21746](https://issues.qgis.org/issues/21746) |  |  |
| SAGA \"saga split rgb bands\" tool is not inside any (SAGA) group of tools | [#21849](https://issues.qgis.org/issues/21849) | [PR #10062](https://github.com/qgis/QGIS/pull/10062) | Gereed |
| r.sun cannot be executed because it calls on two incompatible options | [#21637](https://issues.qgis.org/issues/21637) | [PR #10074](https://github.com/qgis/QGIS/pull/10074) | Gereed |
| i.segment (GRASS 7.4.2) only produces a Goodness Raster but no Segmented Raster | [#20646](https://issues.qgis.org/issues/20646) | werkt prima in master en 3.4 |  |
| Majority filter (SAGA) returns erroneous results if input is .tif | [#22118](https://issues.qgis.org/issues/22118) | ongeldig |  |
| Processing batch process interface: no way to go back | [#16893](https://issues.qgis.org/issues/16893) | [PR #10080](https://github.com/qgis/QGIS/pull/10080) | Gereed |
| DB Manager rename PostGIS column error | [#21425](https://issues.qgis.org/issues/21425) | [PR #10082](https://github.com/qgis/QGIS/pull/10082) | niet nodig |
| Word wrapping not working in maptips | [#21388](https://issues.qgis.org/issues/21388) | [PR #10081](https://github.com/qgis/QGIS/pull/10081) | Gereed |
| Styles stored in QML files with same name as layer no longer auto loaded | [#21691](https://issues.qgis.org/issues/21691) | [PR #14660](https://github.com/qgis/QGIS/pull/14660) | Gereed |
| QGIS 3.4.6 crashed when I tried classifying a layer | [#21693](https://issues.qgis.org/issues/21693) | [PR #29951](https://github.com/qgis/QGIS/pull/29951) | Gereed |
| Fixed table not working under User defined filter (SAGA) | [#29999](https://github.com/qgis/QGIS/issues/29999) | [PR #30001](https://github.com/qgis/QGIS/pull/30001) | Gereed |
| DB Manager Versioning: \_current view lacks primary key | [#25888](https://github.com/qgis/QGIS/issues/25888) | [PR #30045](https://github.com/qgis/QGIS/pull/30045) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alexander Bruy](https://bruy.me/)
### Mogelijkheid: Reparaties van problemen door Victor Olaya
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Processing \"iterate\" does not work anymore | [#21524](https://issues.qgis.org/issues/21524) | [PR #10078](https://github.com/qgis/QGIS/pull/10078) |  |
| parameter type error in SAGA Gaussian Filter | [#21797](https://issues.qgis.org/issues/21797) | [Commit](https://github.com/qgis/QGIS/commit/83e6dd3efe302de4749d68be23217d8dd4e667d2) |  |
| Distance matrix does not maintain data type and precision for Input Point Layer in Linear (N\*k x 3) | [#21501](https://issues.qgis.org/issues/21501) |  |  |
| Processing \"Build virtual vector\" now fails in certain cases | [#21519](https://issues.qgis.org/issues/21519) | [PR #10083](https://github.com/qgis/QGIS/pull/10083) |  |
| SAGA raster calculator loads more grids than selected when a sdat is supplied in XGRIDS | [#22131](https://issues.qgis.org/issues/22131) | [PR #10085](https://github.com/qgis/QGIS/pull/10085) |  |
| Export selected Objects generated line layer not selectable in graphical modeller | [#21705](https://issues.qgis.org/issues/21705) | [PR #10093](https://github.com/qgis/QGIS/pull/10093) |  |
| Batch processing error in r.mapcalc.simple | [#29822](https://github.com/qgis/QGIS/issues/29822) |  |  |
| Help for algorithms not visible in modeller | [#21536](https://issues.qgis.org/issues/21536) |  |  |
| Bug fixes related the batch interface, not linked to any bug report. They are regressions introduced in recent changes, that i found while working on another issue | [PR #29948](https://github.com/qgis/QGIS/pull/29948) |  |  |
|  | [PR #29950](https://github.com/qgis/QGIS/pull/29950) |  |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Victor Olaya
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| ENVI driver ignores \"geo point\" (GCP) metadata on reading | [#1528](https://github.com/OSGeo/gdal/issues/1528) | [Commit](https://github.com/rouault/gdal/commit/f2f29cd3a7708a4a9553f127b2d19b3cd72f9180) |  |
| WFS GetFeature fails on TypeNames parameter | [#21768](https://issues.qgis.org/issues/21768) | [PR #29946](https://github.com/qgis/QGIS/pull/29946) | Gereed |
| Cannot load GPX file automatically after creating it QGIS 3.4.7 QGIS 3.6.2 | [#22005](https://issues.qgis.org/issues/22005) | [PR #29947](https://github.com/qgis/QGIS/pull/29947) | Gereed |
| Cannot create temporary SpatiaLite cache | [#29819](https://github.com/qgis/QGIS/issues/29819) | [PR #29949](https://github.com/qgis/QGIS/pull/29949) | Gereed |
| PostGIS closed circle in Curved Polygon is not displayed | [#29895](https://github.com/qgis/QGIS/issues/29895) | [PR #30010](https://github.com/qgis/QGIS/pull/30010) | Gereed |
| Fix GeoJSON output of MultiPolygon/MultiSurface | [PR #30012](https://github.com/qgis/QGIS/pull/30012) | [PR #30012](https://github.com/qgis/QGIS/pull/30012) | Niet nodig |
| Multipatch features are not shown anymore | [#29376](https://github.com/qgis/QGIS/issues/29376) | [PR #30024](https://github.com/qgis/QGIS/pull/30024) | Gereed |
| Multiple issues and deadlocks with WFS | [#29258](https://github.com/qgis/QGIS/issues/29258) | [PR #30026](https://github.com/qgis/QGIS/pull/30026) | Gereed |
| WFS provider: Avoid dangling download progress dialog | [PR #30039](https://github.com/qgis/QGIS/pull/30039) | [PR #30039](https://github.com/qgis/QGIS/pull/30039) | Gereed |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| issues in embedded layers | [#29678](https://github.com/qgis/QGIS/issues/29678) | [PR #9993](https://github.com/qgis/QGIS/pull/9993) and [PR #10004](https://github.com/qgis/QGIS/pull/10004) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Editing a GeoPackage feature with spaces in the field names can crash QGIS | [#29630](https://github.com/qgis/QGIS/issues/29630) | [PR #29997](https://github.com/qgis/QGIS/pull/29997) | NOG TE DOEN |
| Crash on update pg layer | [#29814](https://github.com/qgis/QGIS/issues/29814) | Duplicaat | N/B |
| XMDF file type missing from Madiera 3.4.5 | [#29381](https://github.com/qgis/QGIS/issues/29381) | ongeldig | N/B |
| Mesh calculator: crash when \'All Selected Dataset Times\' button clicked | [#30003](https://github.com/qgis/QGIS/issues/30003) | [PR #30005](https://github.com/qgis/QGIS/pull/30005) | N/B |
| Crash when editing fields | [#29200](https://github.com/qgis/QGIS/issues/29200) | kan het niet reproduceren | N/B |
| Closing Vertex Edititor crashes the app | [#30028](https://github.com/qgis/QGIS/issues/30028) | [PR #30030](https://github.com/qgis/QGIS/pull/30030) | NOG TE DOEN |
| Detached 3D view crash \[macOS\] | [#29169](https://github.com/qgis/QGIS/issues/29169) | kan het niet reproduceren |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| No snap when selecting point of rotation | [#29706](https://github.com/qgis/QGIS/issues/29706) | Duplicaat / is geen probleem |  |
| Crashs when working with auxiliary storage label and data defined | [#30078](https://github.com/qgis/QGIS/issues/30078) | kan het niet reproduceren |  |
| Improve the advanced digitizing by angle | [#30133](https://github.com/qgis/QGIS/issues/30133) | Is geen probleem |  |
| Fix reshape for snapped point with Z | [PR #30108](https://github.com/qgis/QGIS/pull/30108) |  |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/en/)

{{<content-end >}}
