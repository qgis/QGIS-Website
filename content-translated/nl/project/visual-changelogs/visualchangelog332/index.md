---
HasBanner: false
draft: false
releaseDate: '2023-06-26'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.32
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.32{#changelog332 }
![image1](images/projects/0316fbcb7ba30bcf1caee80daf0662a1a15d99b0.png)

Datum uitgave 26-06-2023

QGIS 3.32 is een belangrijke uitgave van het Project QGIS dat een significante stap voorwaarts brengt in georuimtelijke technologie naar de wereld van Open Source. De gemeenschap van ontwikkelaars heeft verschillende nieuwe mogelijkheden geïntroduceerd en verbeteringen doorgevoerd om het potentieel aan georuimtelijke gegevens te kunnen benutten.

Naast heel veel verbeteringen voor de kwaliteit van leven naast een breed spectrum aan bestaande mogelijkheden, brengt de uitgave 3.32 de lang verwachte functionaliteit voor eigen verwerking van puntenwolken in QGIS, wat QGIS Desktop een krachtig gereedschap voor het verwerken van gegevens van LiDAR maakt.

This milestone achievement is thanks in large part to the contributions of the community to the effective [crowd funding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/) which funded this development, the QGIS community and [Enhancement Proposals](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263) used for the effective governance of these contributions, the collaborative efforts of the development agencies involved, and of course the extraordinary contributions of individual developers who build these tools for the benefit of all.

Deze uitgave bevat ook een brede variëteit aan verbeteringen voor de ervaringen van ontwikkelaars, uitbreidingen van nieuwe functionaliteiten zoals de plots voor profielen en framewerk voor Processing, en een nieuw framewerk voor sensorgegevens om naadloos te integreren in QGIS met apparaten voor het verzamelen van gegevens en het maken van intelligente oplossingen van de volgende generatie te faciliteren.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=ZtE1Az-zpf0>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/ZtE1Az-zpf0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Kaartgereedschap
### Mogelijkheid: Voorbeeld voor kaarttips
Een venster voor een voorbeeld van kaarttips is toegevoegd aan het dialoogvenster voor eigenschappen van raster- en vectorlagen om de ervaring van het ontwerpen van kaarttips te verrijken.

![image3](images/entries/9e24454517900953b1b667e670c553ac29f10d58.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Gereedschap Meten coördinaten kopiëren
Het dialoogvenster Meten is uitgebreid met de volgende functies:
- kolommen X en Y met coördinaten X en Y
- De eerste rij in de tabel bevat alleen de coördinaten (geen afstand)
- Een bericht wordt weergegeven als het kopiëren is geslaagd
- A `Copy all` action is provided in a context menu on the table
- Voorkomt fouten bij het wijzigen van de instellingen tijdens het meten

Additional settings for managing the \"Copy All\" button behavior are provided to configure aspects such as separator, or including header information.

![image4](images/entries/4eb0ded16e3b6be3c0696230eb63a7a88fab4197.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Kaarttips uitschakelen voor een specifieke laag
Een nieuwe mogelijkheid in de laageigenschappen maakt het mogelijk kaarttips uit te schakelen voor een specifieke laag.

On the QGIS API, a `mapTipsEnabled` Q_PROPERTY was added to the `QgsMapLayer` class to enable this functionality.

![image5](images/entries/73c9d66fac45f948e63ead3f94be4ccddb3172b4.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Gebruikersinterface
### Mogelijkheid: Geef beschrijving waarde relatie weer tijdens hangen boven het combinatievak
A description tooltip is now available when hovering the cursor over the value in the relation editor widget\'s combobox.

The description tooltip matches that of the currently selected item\'s description as defined in the \'description column\' on the value relation configuration panel.

![image6](images/entries/369ecca5320fe09a8f2657463df647c5526a496c.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Acties voor vastzetten 2D-kaartvenster
De actie om weergaven van het 2D-kaartvenster vast te zetten en los te maken zijn toegevoegd om overeen te komen met het gedrag voor weergaven van 3D-kaartvensters.

![image7](images/entries/d6aaec94112b3787b59d1d820b0335b9ab9b2385.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Knop Recent gebruikte CRS leegmaken toegevoegd
The ability to remove \"recently used\" CRS information has been implemented in various ways, including:
- Drukken op de toets Del, terwijl de lijst met recent gebruikte CRS-en de focus heeft, verwijdert het geselecteerde CRS
- Een kolom in de tabel Recent CRS met een knop om individuele CRS-en leeg te maken
- Een actie contextmenu Geselecteerde leegmaken
- Een actie contextmenu Alle recente CRS-en verwijderen die de gebruiker om bevestiging zal vragen

![image8](images/entries/564478bebbaeda3394d77001b46cb051a795c73f.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Zoomen met muiswiel omdraaien
Een instelling is nu beschikbaar om de richting van het zoomen met het muiswiel om te draaien (voorwaarts scrollen zoomt uit)

Deze instelling zal het gedrag van zoomen met het muiswiel beïnvloeden in meerdere contexten, inclusief:
- in the map canvas (`QgsMapCanvas`)
- in the map overview (`QgsMapOverviewCanvas`)
- in the layout view (`QgsLayoutView`)
- in the layout map items when the \"move item content\" tool is active (`QgsLayoutViewToolMoveItemContent`)
- in the Elevation profile canvas (`QgsElevationProfileCanvas`)
- In the model editor graphic view (`QgsModelGraphicsView`)

![image9](images/entries/b242e0115f29586846d88d6d0cfb1d5f6f9760f0.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Favoriete plaatsen roteren
Roteren van de kaart kan nu worden opgeslagen en worden toegepast op Favoriete plaatsen, inclusief een nieuw contextmenu in het paneel Favoriete plaatsen beheren.

![image10](images/entries/ea7e07b0c6a753ab205dd31d20454a4006c17bba.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Annotaties
### Mogelijkheid: Verbeteringen voor gereedschap Annotaties
Een aantal verbeteringen zijn in het gedrag voor gereedschappen voor annotaties gemaakt, inclusief:
- Voorkomen van het wijzigen van de grootte van een annotatie als de cursor niet feitelijk boven het frame is
- Een contextmenu toegevoegd (wanneer een gereedschap voor annotaties wordt geactiveerd) voor items van Annotaties
- Drop the undocumented `toggleTextItemVisibilities` (toggled Text annotations visibility with Ctrl+T)
- Gedrag voor selecteren en wijzigen grootte verbeterd, inclusief verbeteringen voor afhandelen van overlappende annotaties

![image11](images/entries/fe30ec582f3b10338c05db078429751c06c890af.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Live voorbeeld voor annotaties
A \"live update\" checkbox in the annotation editors allows for on the fly review of rendered annotation content.

![image12](images/entries/a969c1ce6990854c84031bc4b7085b799c03f32f.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## 3D-objecten
### Mogelijkheid: Verbeterd gereedschap 3D-meten
De volgende verbeteringen zijn geïmplementeerd in het gereedschap Meten in 3D-scenes:
- Staat meten op puntenwolk-punten toe
- Display billboard circle markers on the 3d rubber band\'s vertices
- Moving the mouse moves the rubber band\'s last vertex (although the measured results are not updated until user clicks)
- Verplaatsen van de camera verwijdert niet de huidige metingen
- Maakt gebruiken van de toetsen Backspace en Del mogelijk om ongedaan te maken (verwijder laatste meting)
- Maakt gebruiken van Esc mogelijk om metingen leeg te maken, wat overeenkomt met het gedrag van zijn 2D tegenhanger
- Renders 3d rubberbands on top of other 3d entities so they don\'t get occluded

De logica voor het selecteren van objecten is ook opnieuw bewerkt voor meer controle, en het gereedschap 3D identificeren werd ook verbeterd om inmenging van navigatie met de camera te voorkomen, als ook een reparatie van een probleem waarbij in specifieke gevallen verkeerde FID's werden teruggegeven.

![image13](images/entries/65d6c0b4ab0c187c6a4b1e9f2f6c6483708cfce4.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Puntenwolken
### Mogelijkheid: Provider voor eigen verwerking van puntenwolken
A new native processing provider has been provided for point cloud algorithms, in line with [QEP 263](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263).

Under the hood provider utilizes the [pdal_wrench](https://github.com/PDAL/wrench) command line tool and currently supports the following algorithms:
- Informatie: voer een basis metadata uit van de puntenwolk (aantal punten, bereik, CRS, etc)
- Converteert indeling: converteer puntenwolk naar een andere indeling, bijv. las naar laz
- Projecteert opnieuw: projecteer puntenwolk opnieuw naar een ander CRS
- Projectie repareren: repareer (toewijzen) CRS van een bestand voor een puntenwolk
- Clippen: clip puntenwolk door polyg(o)on(en) te clippen
- Samenvoegen: voeg meerdere bestanden met puntenwolken samen tot één enkel.
- Tegel: maakt tegels uit invoergegevens.
- Uitdunnen: maak een verdunde versie van de puntenwolk
- Grens: exporteer vectorlaag die grenzen voor puntenwolk bevat
- Density: export a raster file where each cell contains number of points that are in that cell\'s area
- Exporteren naar raster: exporteer gegevens van puntenwolk naar een 2D-raster grid
- Exporteren naar vector: exporteer gegevens van puntenwolk naar een vectorlaag met 3D-punten
- Exporteren naar raster (met triangulatie): exporteer gegevens van puntenwolk naar een 2D-raster grid door triangulatie van punten
- Filer: neem een subset uit de puntenwolk met expressies van PDAL

As pdal_wrench requires PDAL \>= 2.5.0, the new processing provider will be available only where the PDAL version requirement is satisfied.

![image14](images/entries/e6c8922d1f55cc29aeceb514da8253f9b5b36edf.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Expressiebouwer Puntenwolk voor framewerk Processing
Een nieuw widget voor puntenwolken Expressie-bouwer is beschikbaar in de gebruikersinterface om filters te maken voor puntenwolken op een gebruikersvriendelijke manier, consistent met de bestaande interfaces voor Expressie-bouwer in QGIS.

Within the QGIS API, the `QgsProcessingParameterExpression` parameter has been extended with the types `Qgis` and `PointCloud`. If parameter has a `PointCloud` type, it will use the point cloud expression builder widget. To maintain backward compatibility, by default an expression parameter will use the `Qgis` expression type.

The `QgsPointCloudExpression` class was also extended with a new method to convert QGIS point cloud expressions to [PDAL expressions](https://pdal.io/en/latest/stages/expression.html).

Bestaande algoritmes voor PDAL die expressiefilters gebruiken zijn bijgewerkt om parameters voor expressies te gebruiken in plaats van tekenreeksen.

![image15](images/entries/f69a04fbddde3eee72333fab2c1af0c58582aaae.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Filteren op rechthoek en expressie toegevoegd aan algoritmes van PDAL
Toegevoegd de optie om invoer puntenwolken te filteren op rechthoek (bereik) en expressie in de volgende algoritmes voor PDAL:
- grens
- clip
- dichtheid
- exporteren naar raster (normaal en varianten voor TIN)
- exporteren naar vector
- samenvoegen
- uitdunnen

Dit maakt het mogelijk slechts een subset punten uit de/het invoerbestand(en) te verwerken, zonder de noodzaak om een tussenstap voor filteren uit te voeren of tijdelijke bestanden te maken.

Voor hen die alleen filteren nodig hebben is er ook een afzonderlijk algoritme Filteren, dat in staat is te filteren op ofwel bereik, met een expressie of een combinatie daarvan.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Nieuw type parameter voor attribuut puntenwolk
Nuttig voor algoritmes voor puntenwolken die attributen hebben, zoals het exporteren van specifieke attribuutwaarden als raster of filteren van puntenwolken.

This also deprecates `parameterAsFields` API call, and `parameterAsStrings` should be used both for fields and point cloud attributes instead.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Virtuele PuntenWolken (VPC) weergeven in 3D-weergave
Virtuele puntenwolken kunnen nu worden gerenderd in 3D-weergaven. Voor het beheren van de uitvoering wordt een drempel voor de sub-index gespecificeerd, zodat de weergave de opgedeelde entiteit van de puntenwolk alleen zal renderen indien van toepassing en zal in plaats daarvan de begrenzingsregio van een bepaalde sub-index renderen als niet wordt voldaan aan de criteria voor de drempel.

![image16](images/entries/ec9947c41a6b8caedcf2a72bf7b61ff4f2b8b04e.gif)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Virtuele puntenwolken (VPC)
A new data provider is available for *Virtual Point Cloud* (VPC) files created by the [pdal_wrench](https://github.com/PDAL/wrench) utility and the *Build virtual point cloud (VPC)* tool in the newly introduced [Native point cloud Processing provider](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263).

The VPC file is handled as a single layer in QGIS and may contain a large number of point cloud files whose indexes are lazy loaded when the canvas is zoomed in enough. An extent renderer is used for the individual indexes while their extent fits the canvas\' width and the user defined renderer is only used when zoomed in further.

A Virtual Point Cloud is a JSON container file with a `.vpc` extension, referring to other files/URLs that contain the actual point cloud data. This is a concept similar to virtual rasters (VRTs) in GDAL. The JSON content is actually a STAC API ItemCollection. See [VPC specification](https://github.com/PDAL/wrench/blob/main/vpc-spec.md) for more details.

![image17](images/entries/ec51218d00c661a9fd68dbda499f13ab56974c6a.gif)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Afdruklay-outs
### Mogelijkheid: Ondersteuning voor hyperlink voor met HTML ingeschakelde export van labels
Labels van QGIS die inhoud HTML bevatten zullen nu ondersteuning bieden voor het inbedden van functionele hyperlinks in relevant exporteren van lay-outs, zoals PDF's.

Dit werd mogelijk gemaakt door Kanton Schaffhausen

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Ondersteuning voor filteren van legenda's van lay-outs op meerdere gekoppelde kaartitems
In plats van het beperken van het filteren van een legenda van lay-outs tot één enkele gekoppelde kaart, maakt deze wijziging het mogelijk dat legenda's worden gefilterd, in plaats van meerdere gekoppelde kaarten. Het is ontworpen het gebruiksgeval mogelijk te maken waarbij een lay-out meerdere kaarten heeft, potentieel op verschillende schalen en die verschillende bereiken weergeven, en één enkele legenda is vereist die die alle symbolen bevat die zichtbaar zijn op alle kaarten.

The UX has been designed to avoid changing the current user workflows, in that legends will still be linked to a single main map item. This map is used when determining the scale (and other map dependent properties) at which to render the legend\'s symbols. Checking the \"Only show items inside linked maps\" option will still automatically filter the legend by the content of the main linked maps. However, there\'s a new \"\...\" options button next to the \"Only show items inside linked maps\" checkbox which allows users to select also other maps from their layout to consider when determining visible items:

![image18](images/entries/3246252a68bf9e6ecbd8d54d20b477305ec8f79a.webp)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Mogelijkheid: Functies ltrim/rtrim toegevoegd
Maakt het mogelijk spaties of andere tekens te verwijderen vanaf het begin of het einde van tekenreeksen

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Digitaliseren
### Mogelijkheid: Lijst veldwaarde in dialoogvenster Objecten samenvoegen
Bij het samenvoegen van objecten kunnen gebruikers nu uit een lijst met beschikbare waarden uit de geselecteerde objecten selecteren, in plaats van handmatig een waarde op te gevenvoor een veld.

![image19](images/entries/01bce8523b3c79ad48ae040c8a5d446c4aa338ae.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Mogelijkheid: Uitbreidingen optie Veel voorkomende hoek  voor Geavanceerd digitaliseren
De opties voor Geavanceerd digitaliseren voor veel voorkomende hoeken zijn uitgebreid met de volgende functionaliteiten:
- Nieuwe veel voorkomende hoeken voor 0.1°, 0.5° en 1.0°
- Een nieuwe optie is toegevoegd om de huidige veel voorkomende hoek weer te geven in de zwevende contextwidget
- New \'N\' \'SHIFT+N\' keyboard shortcuts are available to cycle through the common angle options

![image20](images/entries/7e402e89c5fb13d41c7e1e99d9fa13b51499c571.webp)

Dit werd mogelijk gemaakt door ChartWorld International

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Instelling voor zwevend venster en informatie over richting voor Geavanceerd digitaliseren
A new configuration setting for the advanced digitizing tool allows users to toggle the display of the \"floater\" contextual menu which follows the cursor during digitizing. Additional options are included for adding information to the floater panel, such as the display of bearing and azimuth information.

![image21](images/entries/1378170e362cd2b7f8ac14cbd5556b87ee593918.gif)

Dit werd mogelijk gemaakt door ChartWorld International

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Attributentabel
### Feature: Improve loading time of attribute tables with hidden fields
Verbeterde laadtijd van attributentabel als er verborgen virtuele velden zijn en (op een meer beperkte manier) als er verborgen niet-virtuele velden zijn.

Dit werd mogelijk gemaakt door QTIBIA Engineering and QCooperative.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Gegevensbeheer
### Mogelijkheid: Sta toe dat een bereik aan cellen wordt gekopieerd uit het venster met resultaten voor SQL
Maakt selecteren van een bereik aan cellen mogelijk om naar het klembord te kopiëren. Resultaten worden gekopieerd als zowel platte tekst als HTML, dus kan gemakkelijk als tabellen worden geplakt in werkbladen van apps/etc.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aangepast gedrag dialoogvenster Nieuw veld en ondersteuning alias
When creating new fields, the \'Comment\' option is now only exposed for datasources which support editing comments (preventing QGIS from silently discarding the information).

Dit voegt ook ondersteuning toe voor het instellen van aliassen voor velden in het dialoogvenster Nieuw veld, en breidt opmerkingen en aliassen uit voor ondersteunde indelingen voor OGR.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Waarde DistanceUnit voor inches toegevoegd
Inches zijn nu opgenomen als geldige kaarteenheden binnen QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Selectie voor beleid van splitsen van records in dialoogvenster Formulier
A new \"field split policy\" choice item is exposed in the layer properties form dialog. That allows users to easily determine the current policy for splitting a field and change as required.

De volgende beleidsregels worden verschaft:
- Duplicaat waarde
- Waarde verwijderen
- Standaardwaarde gebruiken
- Verhouding geometrieën gebruiken

![image22](images/entries/f53e5c49ba0c25415b7a5bd163cb94a1ab72ebcd.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Formulieren en widgets
### Mogelijkheid: Beheer toegevoegd voor horizontaal / verticaal uitrekken voor widgets van attribuutformulieren
This functionality exposes two new \"size\" options for edit form widgets, allowing control over the horizontal and vertical stretch factors for the widget. By setting a horizontal or vertical stretch, users can control how edit widgets will relatively resize when resizing an attribute form.

For example, a user can set a higher horizontal stretch value for widgets which should \"grab\" more of the available horizontal space, such as for those widgets which are expected to have longer values. Similarly, the vertical stretch setting (available for select widget types) will control how widgets grow vertically when resizing forms, relative to the form dialog.

Samen geven deze opties meer beheer aan gebruikers over de exacte lay-out en grootte van hun attributenformulieren.

By default, the stretch values are set to \"Default\" which is the same as the behavior exhibited in previous versions of QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add new attribute form container type \"Row\"
Deze container legt kind-widgets altijd op een horizontale rij, waarbij het aantal kolommen automatisch wordt bepaald door het aantal kind-widgets.

It\'s useful for creation of compact forms, where no space will be wasted by assigning extraneous horizontal width to widgets where the expected values will always be short.

Bijv.: maken van 3 rijen met 3, 2, 1 kind-widgets respectievelijke resultaten in de lay-out:

    Attr 1: [...] Attr 2: [...] Attr 3: [...]
    Attr 4: [..........] Attr 5: [..........]
    Attr 6: [...............................]
    
Zonder de optie van rij-containers zouden alle horizontale rijen hetzelfde aantal kolommen hebben, bijv.:

    Attr 1: [...] Attr 2: [...] Attr 3: [...]
    Attr 4: [...] Attr 5: [...] Attr 6: [...]
    
(wat onvoldoende horizontale ruimte laat voor de attributen 4-6), of

    Attr 1: [..........] Attr 2: [..........]
    Attr 2: [..........] Attr 3: [..........]
    Attr 4: [..........] Attr 5: [..........]
    Attr 6: [..........]
    
(resulterend in verspilde horizontale ruimte naast attribuut 6, en een extra rij die verticale ruimte inneemt)

Dit werd mogelijk gemaakt door NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Processing
### Mogelijkheid: Algoritme Vectortegels downloaden
Een nieuw algoritme voor Processing is toegevoegd dat het downloaden van vectortegels van een server op afstand mogelijk maakt. Deze functionaliteit bevat ondersteuning voor vectortegels voor de parameter kaartlaag, als ook een nieuwe parameter voor de bestemming van de vectortegel voor algoritmes van Processing. De uitvoer in de indeling MBTiles-bestanden kan na de verwerking ook automatisch worden toegevoegd aan het kaartvenster.

This feature was funded by [Mergin Maps](https://merginmaps.com/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Toestaan van configureren van de volgorde van uitvoer die werd gemaakt door een model
A new \"Reorder Output Layers\" action to the model designer menu has been added which allows model creators to set a specific order which the outputs from their model must use when loading the results into a project. This gives the model creator a means of ensuring that layers are logically ordered on the canvas when running a model, such as placing a vector layer output over a raster layer output, or a point layer over a polygon layer.

The model creator can also set an optional \"Group name\" for the outputs for automatically grouping outputs within the layer tree using a new group name or by adding them to an existing group.

![image23](images/entries/a898507ce882d4e757064429471307a3cdd0e0e9.webp)

This feature was funded by [QGIS User Group Germany](https://qgis.de/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme voor het maken van bestanden COPC voor invoer van puntenwolken
A new algorithm adds the \"Create COPC\" option to the PDAL provider for generating Cloud Optimized Point Clouds. The algorithm creates a COPC file for each input point cloud file and can be useful for indexing files before using them in QGIS, or when building a VPC.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Gereedschap voor Selectie omkeren voor algoritme Bijgewerkte velden van Processing
Een nieuwe knop is toegevoegd aan de interface voor het beheren van velden van het algoritme Bijgewerkte velden in Processing. Die stelt gebruikers in staat de selectie om te draaien. Dit maakt meer efficiënt beheer van velden mogelijk, zoals het inschakelen van het in bulk verwijderen van velden.

This feature was added during the [QGIS Contributor Meeting 2023, s-hertogenbosch](https://github.com/qgis/QGIS/wiki/25th-Contributor-Meeting-in-'s-Hertogenbosch)

![image24](images/entries/ab43192e1204465860a221e323f478d9a1e8d2f6.gif)

This feature was funded by [camptocamp](https://camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Mogelijkheid: Ondersteuning voor opmerkingen voor velden en aliassen in algoritmes van Processing 
This adds support for handling field comments and aliases in the processing \"add field to attributes table\" and \"refactor fields\" algorithms. Additionally, it ensures that field comments and aliases are copied from source layers to destination layers when present.

Als de uitvoerlagen geen opmerkingen/ aliassen ondersteunen dan worden gebruikersvriendelijke waarschuwingen weergegeven in het log van Processing die gebruikers in kennis stellen van de beperking.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme Virtuele PuntenWolk (VPC) bouwen
The new algorithm allows user to build [virtual point cloud (VPC)](https://github.com/PDAL/wrench/blob/main/vpc-spec.md) files that reference multiple existing point cloud datasets. This allows then visualization and processing of many point cloud files as a single layer in QGIS.

Additional options are available for the \"Build VPC\" Processing algorithm, which provide the following utilities for building Virtual Point Clouds:
- statistieken berekenen vanuit invoergegevens
- exacte grenzen berekenen vanuit invoergegevens
- een overzichts-puntenwolk bouwen

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Beheren van threads in instellingen voor algoritmes
Een handige nieuwe instelling voor de omgevingsconfiguratie is gemaakt voor het configureren van het aantal threads dat een algoritme zou meten gebruiken als een algoritme in staat is meerdere cores te gebruiken, zoals TauDEM of PDAL.

Deze functionaliteit is toegepast voor de algoritmes van PDAL en TileXYZ.

![image25](images/entries/d5a70cd3ed4a01b2e51381907b92b05256e13cc2.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Toestaan dat tijdelijke map tijdelijk wordt gewijzigd via het paneel voor de instellingen van het algoritme
Individuele algoritmes voor Processing mogen nu een omgevingsinstelling hebben om een aangepaste tijdelijke map te specificeren die het huidige geconfigureerde bestandspad overschrijft. Dit is nuttig in situaties waarbij een bepaald gereedschap heel veel tijdelijk schijfruimte gebruikt en een aangewezen locatie of geheugen schijf is vereist, of wanneer een bepaalde bewerking verbeteringen voor de uitvoering vereist die worden geboden door een bepaalde schijf of pad.

![image26](images/entries/e36dd209990541e93fdf7a3170596fe0f81ec920.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Toestaan dat dialoogvenster van Processing de standaard instellingen voor de context van Processing te overschrijven
A new \"Algorithm Settings\" action has been added to the Advanced button of the processing algorithms interface. Selecting it shows a panel which allows users to control general processing settings which apply to a **particular instance** of the algorithm execution. It\'s intended to be a place where a user can override their global processing settings on an ad-hoc basis without having to change their usual default settings.

Bevat instellingen voor:
- afhandelen van ongeldige geometrieën (Anders dan de bestaande instelling per-parameter overschrijven hiervoor, zal het instellen van de afhandelingsmethode hier van toepassing zijn op ALLE invoer voor het algoritme)
- eenheden voor afstanden en gebieden te gebruiken voor metingen van afstand/gebied

![image27](images/entries/2039528616fa5e39d98dd01dc43899db654d3a45.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aanvullende parameters voor algoritme gdal2xyz
The gdal2xyz processing algorithm from the GDAL processing provider now includes parameters for `skipnodata` and `src`, and `dstnodata`.

This feature was developed by [Luke Pinner](https://github.com/lpinner)
### Feature: Add \"Keep disjoint results separate\" option to buffer algorithm
If checked, then any disjoint parts in the buffer results will be output as separate single-part features. This setting is designed to expose a similar functionality as is available for the \'dissolve\' algorithm.

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Toestaan dat filterexpressies worden ingesteld voor vectorbronnen
This change adds a new \"feature filter\" option alongside the existing feature limit and invalid geometry handling options available for all vector inputs to processing layers.

Het stelt gebruikers in staat een expressie in te voeren om dynamisch een subset van de laag te maken bij het uitvoeren van het gereedschap, wat afzonderlijke stappen vermijdt voor het instellen van filters voor lagen of het maken van subsets van lagen.

![image28](images/entries/032c4a9555a7debad18a2fd8fb4b84a09e94eb3b.webp)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support \*.HEIC format images in Processing \"Import Photos\" algorithm
The Import Photos algorithm now allows importing `*.heic` images with GDAL\'s HEIF image support.

This feature was developed by [Chris Shucksmith](https://github.com/shuckc)
## Opties voor toepassing en projecten
### Mogelijkheid: Updates voor bewerker instellingen
De interface voor bewerkers van instellingen hebben een belangrijke opknapbeurt gekregen en de interface voor geavanceerde instellingen heeft de volgende, voor de gebruiker zichtbare, wijzigingen:
- Een keuze tussen de oude of de nieuwe widget voor instellingen, die wordt onthouden
- A \"hidden\" setting allows to bypass the warning before showing the settings tree
- Instellingen hebben toegewezen bewerkers (draaivak, keuzevak, kleurenknop, etc.)
- Het aanpassen van instellingen wordt nu alleen uitgevoerd als op de knop Toepassen wordt gedrukt
- Huidige instellingen zijn weergegeven in cursief, waar instellingen, waarop wijzigingen zullen worden toegepast, worden weergegeven in rood

In aanvulling heeft de API voor instellingen significante wijzigingen ondergaan, inclusief:
- Verwijderen van de klasse QgsSettingsEntryByValue, gebruik allee met verwijzing
- De oude QgsSettingsTreeWidget is hernoemd naar QgsSettingsTreeWidgetOld (in app)

Nieuwe klassen voor API geïntroduceerd omvatten:
- QgsSettingsTreeWidget en QgsSettingsTreeModel: boom widget + model om de instellingen weer te geven en te bewerken
- QgsSettingsEditorWidgetWrapper (puur virtueel): een basis wrapper-klasse om een widget Instellingen bewerken te maken en af te handelen
- QgsSettingsEditorWidgetWrapperTemplate (puur virtueel): de basisklasse voor de wrapper van instellingen die zijn gedeclareerd in C++ API (met typed methods)
- Klassen voor bewerkers van instellingen: QgsSettingsStringEditorWidgetWrapper, etc.
- QgsSettingsEditorWidgetRegistry: een register van de wrappers voor bewerkers van instellingen

![image29](images/entries/36a2db1e6a9448a1bdd4699bbeaa79057e912535.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Mogelijkheid: Gebruikersprofiel selecteren
In eerdere versies van QGIS, als QGIS Desktop werd gesloten, werd het huidige profiel opgeslagen in het configuratiebestand profiles.ini, dus werd het standaard profiel gebruikt in de laatste instantie van QGIS die werd gesloten.

Nieuw beleid voor het selecteren van de gebruiker stelt gebruikers in staat te selecteren hoe standaard profielen worden gedefinieerd, overeenkomend met de volgende drie opties:
- Laatste profiel: De oude modus die het gedrag van eerder versies volgt. Dit gebruikt het laatst gesloten profiel bij het openen van een nieuwe instantie van QGIS.
- Standaard profiel: Definieer handmatig een standaard profiel, naast het bestaande profiel, dat standaard altijd zal worden gebruikt (zonder een vlag voor de opdrachtregel te gebruiken of een profiel te kiezen in de gebruikersinterface van QGIS)
- Laat gebruiker kiezen bij opstarten

When \"Let user choose\" is selected, if there are 2 or more profiles, a selection dialog is displayed before the SplashScreen which will allow the user to choose which profile to use or to create a new profile which will be loaded automatically.

Ongeacht het geselecteerde beleid, als slechts een profiel bestaat, zal dat worden gebruikt, en als er geen profiel bestaat, zal het standaard profiel worden gemaakt en gebruikt.

Pictogrammen voor gebruikersprofielen worden ook verschaft om gebruikers in staat te stellen visueel onderscheid te maken tussen hun actieve profielen.

![image30](images/entries/ac274c8186837f23d80df6142030a416efcdcb1e.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Profiel plotten
### Mogelijkheid: Selecteren van eenheden voor afstand voor hoogteprofielen
Gebruikers kunnen nu kiezen uit een selectie van afstandseenheden om de standaard (kaarteenheden van het CRS van het kaartvenster) te overschrijven voor hoogteprofielen in zowel de interactieve hoogteprofielen (via de knop Instellingen van de werkbalk) en voor lay-out hoogteprofielen.

In lay-outprofielen is er een aanvullende optie die beheert of het achtervoegsel voor afstandseenheden zou moeten worden geplaatst. De volgende opties zijn beschikbaar om de weergave van de achtervoegsels voor eenheden te beheren:
- achtervoegsels verbergen
- weergeven voor alle waarden
- weergeven voor de eerste waarde
- weergeven voor de laatste waarde
- weergeven voor zowel de eerste als de laatste waarde

Note that it is currently not possible to expose unit selection for the vertical axis, as this is currently dimensionless and will require the development of vertical CRS handling in QGIS as outlined in [QEP 267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267).

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Exporteren hoogteprofielen
Een nieuw item is toegevoegd aan de werkbalk voor hoogteprofielen, dat verschillende opties bevat voor het exporteren van hoogteprofielen.

Plots van profielen kunnen nu worden geëxporteerd als:
- 3D-objecten: exporteert de profiellijn als 3D-kruisdelen, met waarden Z uit de delen van de hoogte
- 2D-profiel: exporteert het profiel als een diagram afstand vs hoogte (d.i. zoals weergegeven in de widget Hoogteprofiel)
- Tabel Afstand/Hoogte: exporteert monsterwaarden afstand vs hoogte als een tabel

De resultaten kunnen worden opgeslagen als DXF-bestanden, CSV-bestanden, of elk van de standaard weg te schrijven vectorruimtelijke indelingen, Shapefile GeoPackages.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Lagen toevoegen aan hoogteprofielen
1. An explicit \"Add Layers\" button has been added to the elevation profile dock. This provides a user-friendly why of adding new layers to a plot - clicking it will show a filtered list of possible layers which can be added to the plot, but which currently aren\'t in the plot (i.e it will include all raster layers from the project which aren\'t marked as having elevation data). Selecting layers will cause them to automatically be marked as having elevation data and immediately added to the plot.
2. Layers can now be added to elevation plots via drag and drop from the layer tree. Unfortunately, users will have to explicitly hold the \"Ctrl\" key while dragging in order to force the copy action due to upstream library limitations.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add \"Fill Above\" mode for elevation profile drawing
The new fill above drawing mode for profile plots also includes additional options to limit the extent of \"fill above\" and \"fill below\" elevation ranges for a layer.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie toegevoegd om de horizontale/ verticale schaal te vergrendelen voor overeenkomende schalen
Indien geactiveerd zorgt deze optie ervoor dat de horizontale en verticale schalen altijd gelijk blijven. Bijvoorbeeld: een helling van 45 graden zal altijd in het profiel verschijnen als een helling van 45 graden.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Sensoren
### Mogelijkheid: Bronframewerk sensoren 
Een bronframewerk voor sensoren verschaft een register voor type sensoren, een beheerder voor sensoren en drie eenvoudige op QIODevice-gebaseerde type sensoren als volgt:
- TCP socket
- UDP socket
- Seriële poort

Een beheerder voor sensoren is aangehecht aan projectinstanties die het voor gebruikers mogelijk maakt sensoren te registreren in hun projectbestanden. Anders dan met andere invoer, zoals een apparaat die een positie aangeeft, wordt van sensoren verwacht dat zij veel meer project-specifieke gegevensinvoer leveren. Het grote voordeel van op project-gebaseerde sensoren is dat het deze veel draagbaarder maakt en gemakkelijker te delen tussen gebruikers.

A new `sensor_data()` function is added to the project scope which is available using expressions, that returns the latest captured sensor data values for a specific sensor name. An optional expiration (in milliseconds) parameter allows for expressions that will reject a specific sensor value is older that the provided expiration value.

![image31](images/entries/79f13eef3f01b425e4523a9dd9b0922a97712d4f.gif)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Gebruikersinterface voor register van sensoren en configuratiewidgets
Configuration widgets are provided for the TCP, UDP, and serial port sensor types which will allow users to configure, add, and remove sensors within the project properties dialog\'s sensors panel.

De implementatie omvat een gebruikersinterface voor het register van sensoren om gemakkelijk aanvullende sensoren voor Python te maken en te verpakken als plug-ins.

![image32](images/entries/59e82c99ec67a2bd1778543c7fa649a02e5fcf70.webp)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Paneel met opties voor sensoren in het dialoogvenster voor de eigenschappen van het project
Een widget sensortabel wordt verschaft dat geregistreerde sensoren in een project weergeeft, naast acties om met sensoren te verbinden en verbindingen te verbreken. De tabel is toegankelijk via een nieuw paneel voor sensoren in het dialoogvenster voor de eigenschappen van het project.

![image33](images/entries/e797ad206e4fbb63387d98411d8e08c6a6fe0f47.webp)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Browser
### Mogelijkheid: Opmerkingen voor veld instellen in Browser
When supported by providers, a new browser context menu action for fields allows for users to set/change the field\'s comments in the datasource.

Momenteel ondersteund voor indelingen OGR met mogelijkheden voor opmerkingen in velden, zoals GPKG, ESRI File Geodatabase, NetCDF, of Geoparquet, als ook databronnen van PostgreSQL.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aliassen voor veld instellen in Browser
When supported by providers, a new browser context menu action for fields allows for users to set/change the field\'s alias in the datasource.

Momenteel ondersteund voor indelingen OGR met mogelijkheden voor opmerkingen in velden, zoals GPKG, ESRI File Geodatabase, NetCDF, of Geoparquet.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Lagen laden in parallelle threads bij openen van project
QGIS zal nu parallel ondersteunde lagen laden bij het laden van een project, wat de laadtijden van een project significant verbeterd in bepaalde omstandigheden, zoals wanneer een project enorm veel lagen op afstand bevat.

De provider van de laaggegevens moet, om een laag te laden in een parallelle thread, parallel laden ondersteunen (momenteel providers GDAL en PostgreSQL).

Een nieuwe geavanceerde instelling is beschikbaar om, indien nodig, dit gedrag uit te schakelen.

![image34](images/entries/809438ef5d3fd9f3574891be96131f9d113562d9.webp)

This feature was funded by [KoBold Metals](https://www.koboldmetals.com/)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Mogelijkheid: Implementeren van server-side filteren met Part 1 of Part 3
De gegevensprovider WFS/ OGC API for Features (OAPIF) is uitgebreid om verbeterde criteria voor filteren in lijn te brengen met open standaarden.

Nieuwe functionaliteiten omvatten:
- Ondersteuning voor filteren op eigenschappen van objecten (OGC API Features Part 1 - /rec/core/fc-filters). Dit gebruikt het eindpunt /api om een lijst van te bevragen items te verkrijgen.
- Ondersteuning voor filteren, gebaseerd op OGC API Features Part 3 - CQL2-text
- Geef geselecteerde CRS door aan de gebruikersinterface van Querybouwer
- Implementeer een vertaling expressie getFeature()

For the CQL2text compatibility, the server `/conformance` implementation is required to declare at least the following data:
- <http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter>
- <http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter>
- <http://www.opengis.net/spec/cql2/1.0/conf/cql2-text>
- <http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2>

The `/collections/{collid}/queryables` endpoint is requested to get the queryable properties.

Aanvullende klassen voor conformatie aan geavanceerd filteren omvatten de volgende items:
- <http://www.opengis.net/spec/cql2/1.0/conf/advanced-comparison-operators>: for IN, BETWEEN, LIKE
- <http://www.opengis.net/spec/cql2/1.0/conf/case-insensitive-comparison>: for ILIKE
- <http://www.opengis.net/spec/cql2/1.0/conf/basic-spatial-operators>: for `intersects(geomcolumn, geomFromWkt('POINT(x y)'))` and `bbox_intersects(geomcolumn, geomFromWkt('WKT LITERAL'))`

This feature was developed by [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Optie weergeven om bronnen voor vectortegels te laden uit bestanden in Databronnen beheren
The Vector Tile tab now includes choices for selecting from a \"Service\" (the existing, connection based approach for adding vector tiles from online sources) or \"File\" (a new option which allows directly adding a data source using VTPK or MBTiles vector tile files).

![image35](images/entries/d882e2a88732692f8701f27c17fa60c6f376a29e.gif)

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation, Feldkirch, Austria

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aanvullende gebruiker beheerde eigenschappen voor vectortegels
Databronnen voor vectortegels ondersteunen nu door de gebruiker gedefinieerd beheer voor transparantie van de laag en mengmodi.

Additionally, it adds the standard \"Source\" and \"Rendering\" tabs to the vector tile layer properties dialog. The Rendering tab contains the layer\'s scale based visibility (just like for other layer types), and the source tab contains the layer name, crs override and provider-specific source controls.

Bronwidgets zijn ook voor de providers van VTPK en MBTiles vectortegels, wat beheer mogelijk maakt voor het bron bestandspad voor vtpk/mbtiles.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Reparatie van defecte ondersteuning voor lagen vectortegels VTPK/MBTiles, VTPK-bestanden weergeven in Browser
Vectortegellagen geven nu alle vereiste API-items weer voor ondersteuning van de defecte afhandeling en opsporen van lagen, wat hun gedrag consistent maakt met andere laagtypen. Aanvullend, door implementeren van de moderne provider metadata API's voor de provider VTPK zorgen we ervoor dat bestanden VTPK worden weergegeven in het paneel Browser  om ze gemakkelijk op te sporen.

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation, Feldkirch, Austria

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## QGIS Server
### Mogelijkheid: Opties voor opmaken van PDF voor WMS GetPrint
The `FORMAT_OPTIONS` parameter in QGIS Server can now also be used to pass format options for PDF format to WMS GetPrint. This allows more control in GetPrint requests when generating GeoPDF outputs, such as Georeference or Geometry Simplification settings.

This feature was developed by [mhugent](https://github.com/mhugent)
### Mogelijkheid: Te configureren mogelijkheden grootte cache
The QGIS Server GetCapabilities request cache size can now be configured with the `QGIS_SERVER_CAPABILITIES_CACHE_SIZE` parameter, which uses an integer input specifying the number of requests to cache. A notice of \"Removed cached WMS capabilities document\" will be logged when all slots are taken and a cached document is dropped.

This feature was developed by [Jürgen Fischer](https://github.com/jef-n)
### Mogelijkheid: Weergavenaam toevoegen in antwoord GetFeatureInfo
A new `WITH_DISPLAY_NAME` parameter will add the display name in the `GetFeatureInfo` response if needed, similar to the existing `WITH_MAPTIP` parameter.

This feature was funded by [3liz.com](https://3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: OGC API - Features: Volledige paginering toegevoegd voor items collectie HTML-pagina
Om bladeren door de objecten meer gebruikersvriendelijk te maken en om meer informatie te verschaffen, werd het volgende geïmplementeerd en toegevoegd aan de sjabloon voor HTML:
- volledige paginering die altijd het aantal pagina's weergeeft
- te configureren grootte pagina via keuzelijst
- aantal overeenkomende items
- aantal teruggegeven items
- besturingselementen voor grootte pagina/paginering ook aan de onderzijde van de pagina

![image36](images/entries/2fc23a3a7f310ae6cc53ae4ff676c5a96eb8c34a.webp)

This feature was developed by [Björn Hinkeldey](https://github.com/pathmapper)
## Programmeerbaarheid
### Mogelijkheid: Verbeteringen voor Help console Python
A special `?` command has been added to the python console which displays a useful help message, identifies some key variables, and provides helper functions for improving the developer experience within QGIS Desktop.

The `_pyqgis` and `_api` helper functions will take a parameter (an instance or class), and will display the matching object page from the QGIS or Qt documentation.

![image37](images/entries/5eae659a4df942e04095e38fa5256e7c1436ae39.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Uitvoeren van shell-opdrachten vanuit de Python Console
De QGIS Python Console bootst het IPython-gedrag na om systeemopdrachten uit te kunnen voeren.
- Run any command that works at the command-line with the syntax `!<cmd>`. The console will start a subprocess, and forward its output to the Python Console Output.
- Terwijl het subproces wordt uitgevoerd, schakelt de invoer voor Python Console naar de modus STDIN en stuurt ingevoerde tekens door naar het kind-proces. Dit maakt het mogelijk bevestiging te sturen als het kind-proces daarom vraagt.
- Dit verschaft eenvoudige toegang tot de opdrachten. zoals pip, voor het eenvoudig direct installeren en verwijderen van afhankelijkheden in de context van het project van QGIS. 
- Als de Console in de modus STDIN staat, zal het drukken op Ctrl+C het sub-proces afsluiten.
- Affect the result of a command to a variable with the syntax `var = !cmd`

![image38](images/entries/6f4da5dd9d63b6c8e0914c4ad4e7e79ccdfea109.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Actie Code opnieuw opmaken voor codebewerkers
A \"format code\" action has been added to the Python Console Editor which allows for the automated linting/ pretty printing of code in line with the capabilities of modern code editors.

Aanvullende instellingen voor configuratie van deze actie omvatten:
- Opmaken bij opslaan: indien ingeschakeld wordt de opmaak toegepast net voor het opslaan van het script
- Import sorteren: Sorteer geïmporteerde argumenten met isort
- Maximale regellengte: Beheer hoe de opmaak de regels zal laten doorlopen, en beheert de liniaal van d ebewerker

De opties voor Opmaak maken een selectie mogelijk tussen de gereedschappen voor autopep8 of zwart linting en verschaffen de volgende aanvullende opties:
- Level (autopep8 only) See [Autopep8 aggressiveness level](https://pypi.org/project/autopep8/#more-advanced-usage)
- Aanhalingstekens normaliseren (alleen zwart): Vervang alle enkele aanhalingstekens, indien mogelijk, door dubbele aanhalingstekens

Bewerkingen voor sorteren worden verschaft met isort, wat het mogelijk maakt de geïmporteerde argumenten te sorteren in drie verschillende groepen:
- standard library imports (re, os, sys, json, \...)
- third-party modules (PyQt5, pandas, dateutil, \...)
- first-party modules (qgis, processing, \...)

Deze bewerkingen zullen consistente ontwikkeling faciliteren in lijn met de beste voorbeelden uit de praktijk en de kwaliteit van de code verbeteren, consistentie, leesbaarheid, en operationele efficiëntie (speciaal indien gekoppeld aan systemen voor versiebeheer).

![image39](images/entries/4d955fb378b92e625bbfbd84e720d680fecbd063.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Python console schakelen naar volledig hoofdvenster
Voegt dezelfde schakelknop toe als die voor 3D-kaartvensters en attributentabellen om het super-gemakkelijk te maken, de Python console om te schakelen naar een volledig hoofdvenster of terug naar een vastgezet widget.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: HTML-code opnieuw opmaken voor codebewerkers
Editors using the `QgsCodeEditorHTML` class will be able to use the code reformatting functionality to pretty print HTML data within QGIS. Note that this functionality will require the BeautifulSoup4 or lxml libraries to be installed within the python environment to parse the XML/ HTML data.

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| GeoJSON IDs are barely supported (only reading string IDs is supported) | [#53214](https://github.com/qgis/QGIS/issues/53214) | Alleen analyse - reparatie ligt buiten bereik | unreported - \[cleanup\] QgsOgrFeatureIterator(): remove (hopefully!) useless code in subset string case |
| \"Order by\" memory leak | [#53198](https://github.com/qgis/QGIS/issues/53198) | [PR #53266](https://github.com/qgis/QGIS/pull/53266) | N/B |
| Browser very slow when opening directory containing several GDB | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53267](https://github.com/qgis/QGIS/pull/53267) | Doesn\'t build with armv7 on openSUSE Tumbleweed |
| Add .pgwx as potential world file types for georeferenced png | [#53125](https://github.com/qgis/QGIS/issues/53125) | [GDAL PR 7864](https://github.com/OSGeo/gdal/pull/7864) | N/B - reparatie in GDAL |
| Assertion failed when filtering a GeoParquet layer | [#53301](https://github.com/qgis/QGIS/issues/53301) | [GDAL PR 7882](https://github.com/OSGeo/gdal/pull/7882) | N/B - reparatie in GDAL |
| Given URL parameters do not persist for WFS OGC API - Features connection | [#49154](https://github.com/qgis/QGIS/issues/49154) | probeerde te reproduceren - te gecompliceerd | Field domain created incorrectly |
| Field domain created incorrectly | [#52318](https://github.com/qgis/QGIS/issues/52318) | [PR #53314](https://github.com/qgis/QGIS/pull/53314) | [PR #53349](https://github.com/qgis/QGIS/pull/53349) |
| Longer opening time of GPKG file in newer versions | [#53525](https://github.com/qgis/QGIS/issues/53525) | [PR #53566](https://github.com/qgis/QGIS/pull/53566) | NOG TE DOEN |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli (strk)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS offset line shows perpendicular tags issue | [#53165](https://github.com/qgis/QGIS/issues/53165) | [PR #53234](https://github.com/qgis/QGIS/pull/53234) | [PR #53308](https://github.com/qgis/QGIS/pull/53308) |
| strange behaviour of single sided buffer algorithm | [#52795](https://github.com/qgis/QGIS/issues/52795) | [geos PR 912](https://github.com/libgeos/geos/pull/912) | N/B - reparatie in GEOS |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](http://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (itOpen / qcooperative)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Legend filter expression has an incomplete context | [#53229](https://github.com/qgis/QGIS/issues/53229) | [PR #53296](https://github.com/qgis/QGIS/pull/53296) | Wachtrij |
| LineString showing offset in CRS 3857 when using Vertex Tool and \"Clip Features to Canvas Extent\" is enabled | [#45200](https://github.com/qgis/QGIS/issues/45200) | [PR #53384](https://github.com/qgis/QGIS/pull/53384) | Wachtrij |
| Qgis Server WMTS returns wrong WGS84BoundingBox for the layer | [#53213](https://github.com/qgis/QGIS/issues/53213) | Kan niet worden gereproduceerd | Form not showing (randomly) values except when triggering \"Editing Mode\" |
| OGC API Features ignores \"X-Qgis-Service-Url\" header | [#53367](https://github.com/qgis/QGIS/issues/53367) | won\'t fix | Vaste grootte legenda wordt niet gerespecteerd bij exporteren van een lay-out |
| Snap to random vertices after splitting features | [#53040](https://github.com/qgis/QGIS/issues/53040) | Kan niet worden gereproduceerd | Cartographic label placement with \"Distance Offset: From Symbol Bounds\" shows offset for MultiPoint features |
| Layers rendered as a group seem to bypass the \"Lock Layers\" option in my print composer. | [#53379](https://github.com/qgis/QGIS/issues/53379) | [PR #53428](https://github.com/qgis/QGIS/pull/53428) | in wachtrij maar PR is nog steeds niet beoordeeld |
| Map Layout composer - Legend item expression not displaying correctly | [#53244](https://github.com/qgis/QGIS/issues/53244) | [PR #53434](https://github.com/qgis/QGIS/pull/53434) | is het niet waard, niet kritisch |
| opacities parameter doesn\'t apply to labels in GetMap requests | [#48020](https://github.com/qgis/QGIS/issues/48020) | [PR #53438](https://github.com/qgis/QGIS/pull/53438) | in wachtrij maar PR is nog steeds niet beoordeeld |
| The list in \"Link to existing child features\" does not help in selecting the right child features | [#53410](https://github.com/qgis/QGIS/issues/53410) | won\'t fix | Object Snappen aan lijnen werkt niet voor elementen boog |
| Attribute form widgets are not disabled when \"Editable\" state is data-defined and layer is not in edit mode | [#53031](https://github.com/qgis/QGIS/issues/53031) | [PR #53506](https://github.com/qgis/QGIS/pull/53506) | N/B |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Alex Bruy (LutraConsulting)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[Expressions\]: missing \"//\" operator help | [#52094](https://github.com/qgis/QGIS/issues/52094) | [PR #53355](https://github.com/qgis/QGIS/pull/53355) | [PR #53396](https://github.com/qgis/QGIS/pull/53396) |
| Resample or rescale of a raster image cannot be found in a menu item or in the processing toolbox | [#49208](https://github.com/qgis/QGIS/issues/49208) | [PR #53356](https://github.com/qgis/QGIS/pull/53356) | Fout geproduceerd door sluiten dialoogvenster algoritmes: RuntimeError: wrapped C/C++ object of type QgsMapToolCapture has been deleted |
| Model designer export as/run as python didn\'t catch newline in algorithm comments | [#50715](https://github.com/qgis/QGIS/issues/50715) | [PR #53358](https://github.com/qgis/QGIS/pull/53358) | [PR #53397](https://github.com/qgis/QGIS/pull/53397) |
| Add\' button for adding XYZ layer through Data Source Manager remains disabled | [#52622](https://github.com/qgis/QGIS/issues/52622) | [PR #53359](https://github.com/qgis/QGIS/pull/53359) | [PR #53404](https://github.com/qgis/QGIS/pull/53404) |
| Output of Algorithm jumps top left when moving | [#51757](https://github.com/qgis/QGIS/issues/51757) | [PR #53363](https://github.com/qgis/QGIS/pull/53363) | [PR #53402](https://github.com/qgis/QGIS/pull/53402) |
| Name column always shows alias instead of field name in refactor fields algorithm | [#53028](https://github.com/qgis/QGIS/issues/53028) | [PR #53365](https://github.com/qgis/QGIS/pull/53365) | [PR #53407](https://github.com/qgis/QGIS/pull/53407) |
| Sentinel 1 data set not working properly | [#52694](https://github.com/qgis/QGIS/issues/52694) | Geen probleem, verkeerde selectie van gegevensindeling voor grote en complexe geometrieën | Genereren XYZ tiles (MBTiles) - fout bij uitvoeren |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alex Bruy (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsRasterIterator.readNextRasterPart() has a memory leak | [#53412](https://github.com/qgis/QGIS/issues/53412) | [PR #53444](https://github.com/qgis/QGIS/pull/53444) | [PR #53445](https://github.com/qgis/QGIS/pull/53445) |
| Options for some values in Processing are not saved after close window | [#53204](https://github.com/qgis/QGIS/issues/53204) | [PR #53458](https://github.com/qgis/QGIS/pull/53458) | nee |
| Unable to import layer from Postgis view or materialized view , if it has no no primary key | [#52943](https://github.com/qgis/QGIS/issues/52943) | Is geen probleem |  |
| Unwanted vertices when tracing | [#52935](https://github.com/qgis/QGIS/issues/52935) |  |  |
| Topology checker does not highlight all overlap errors in the canvas | [#52903](https://github.com/qgis/QGIS/issues/52903) | [PR #53470](https://github.com/qgis/QGIS/pull/53470) |  |
| Unable to enter interval size for fixed Interval in Graduated Renderer | [#52356](https://github.com/qgis/QGIS/issues/52356) | [PR #53479](https://github.com/qgis/QGIS/pull/53479) | [PR #53508](https://github.com/qgis/QGIS/pull/53508) |
| Vector Tile Layers do not clip to layout map frame when mask enabled | [#52347](https://github.com/qgis/QGIS/issues/52347) | Probleem van Qt upstream |  |
| Splitfeatures function | [#52145](https://github.com/qgis/QGIS/issues/52145) | [PR #53526](https://github.com/qgis/QGIS/pull/53526) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Erased profile plot is redrawn after a layer toggles on/off | [#48117](https://github.com/qgis/QGIS/issues/48117) | [PR #53468](https://github.com/qgis/QGIS/pull/53468) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Legend not updating dynamically when using an atlas | [#53442](https://github.com/qgis/QGIS/issues/53442) | Nog steeds Werk In Uitvoering |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL van probleem (Github, indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Many fixes for regressions on hidpi displays following improved approach implemented for 3.32 | Meerdere | [PR #53556](https://github.com/qgis/QGIS/pull/53556) , [PR #53533](https://github.com/qgis/QGIS/pull/53533) , [PR #53531](https://github.com/qgis/QGIS/pull/53531) | [PR #53517](https://github.com/qgis/QGIS/pull/53517) |
| Implement proper support for new vsi archive formats added in GDAL 3.7 | [PR #53515](https://github.com/qgis/QGIS/pull/53515) | NB |  |
| Store updated postgres credentials in layer source | [#37632](https://github.com/qgis/QGIS/issues/37632) | [PR #53465](https://github.com/qgis/QGIS/pull/53465) | NB |
| Cleanup iface signal connections when unloading processing plugin | [#53455](https://github.com/qgis/QGIS/issues/53455) | [PR #53461](https://github.com/qgis/QGIS/pull/53461) | Te riskant / te weinig profijt |
| Avoid UI lock when closing Execute SQL window | Niet gerapporteerd | [PR #53448](https://github.com/qgis/QGIS/pull/53448) | Te riskant |
| Gracefully cleanup empty python faulthandler log files | [#50609](https://github.com/qgis/QGIS/issues/50609) | [PR #53417](https://github.com/qgis/QGIS/pull/53417) | Te riskant |
| Fix a crash on QGIS close | Niet gerapporteerd | [PR #53414](https://github.com/qgis/QGIS/pull/53414) | [PR #53418](https://github.com/qgis/QGIS/pull/53418) |
| Correctly cleanup project archive files before attempting to clear/replace archive | [#53034](https://github.com/qgis/QGIS/issues/53034) | [PR #53400](https://github.com/qgis/QGIS/pull/53400) | Te riskant |
| Don\'t open datasets when populating browser directories to determine layer drop support | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53398](https://github.com/qgis/QGIS/pull/53398) | Afgewezen |
| Fix crash when writing processing history entry | Niet gerapporteerd | [PR #53394](https://github.com/qgis/QGIS/pull/53394) | NB |
| Fix issue causing CRS selection to be ignored | [#53309](https://github.com/qgis/QGIS/issues/53309) | [PR #53393](https://github.com/qgis/QGIS/pull/53393) | Fix blurry style icons in project properties dialog on hidpi displays |
| Fix grass provider points to out of date help documents | [#53105](https://github.com/qgis/QGIS/issues/53105) | [PR #53372](https://github.com/qgis/QGIS/pull/53372) | [PR #53375](https://github.com/qgis/QGIS/pull/53375) |
| Fix point text annotation rotation, alignment issues | Niet gerapporteerd | [PR #53337](https://github.com/qgis/QGIS/pull/53337) | NB |
| Expand range of z index spin for annotations | Niet gerapporteerd | [PR #53319](https://github.com/qgis/QGIS/pull/53319) | [PR #53326](https://github.com/qgis/QGIS/pull/53326) |
| Fix incorrect scaling of text background markers in annotations | Niet gerapporteerd | [PR #53318](https://github.com/qgis/QGIS/pull/53318) | Fix crash on invalid grass layer paths |
| Flag OneDrive remote folders as remote, slow to open paths on Windows | [#51710](https://github.com/qgis/QGIS/issues/51710) | [PR #53315](https://github.com/qgis/QGIS/pull/53315) | Te riskant |
| Fix crash when creating new grass mapsets when \"set\" is pressed and no region is selected | Niet gerapporteerd | [PR #53293](https://github.com/qgis/QGIS/pull/53293) | [PR #53311](https://github.com/qgis/QGIS/pull/53311) |
| Fix custom coordinate transform test results | [#52184](https://github.com/qgis/QGIS/issues/52184) | [PR #53292](https://github.com/qgis/QGIS/pull/53292) | [PR #53353](https://github.com/qgis/QGIS/pull/53353) |
| Don\'t create alpha bands for non-rotated, south up rasters | [#50879](https://github.com/qgis/QGIS/issues/50879) | [PR #53290](https://github.com/qgis/QGIS/pull/53290) | [PR #53310](https://github.com/qgis/QGIS/pull/53310) |
| Greatly speed up browser when a large number of files are visible | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53268](https://github.com/qgis/QGIS/pull/53268) | [PR #53299](https://github.com/qgis/QGIS/pull/53299) |
| Pass renderer usage from download vector tile algorithm | [#53183](https://github.com/qgis/QGIS/issues/53183) | [PR #53258](https://github.com/qgis/QGIS/pull/53258) | NB |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
