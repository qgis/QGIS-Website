---
HasBanner: false
draft: false
releaseDate: 26-10-2018
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.4
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.4{#changelog34 }
![image0](images/entries/splash34vs.webp)

Datum uitgave 26-10-2018

The first long-term release (LTR) of QGIS 3. QGIS 3.4 just released. After five consolidation point releases (3.4.5) it will replace the previous LTR in the package repositories in February 2019 (see [release schedule]({{< ref "resources/roadmap#release-schedule" >}})). This is a giant leap forward for the project - our first Long Term Release based on the 3.x platform. For users moving over from the 2.18 LTR there is a huge list of new features and impactful changes in this new LTR version. Please bear in mind that 3.x plugins are incompatible with 2.x plugins so review your plugin usage carefully - and if possible help to migrate old plugins to the new platform. If you have not already done so, take a look at the changelogs from [Version 3.0](../visualchangelog30) and [Version 3.2](../visualchangelog32) to understand the full scope of changes in the 3.4 release.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current supporters is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

![image1](images/projects/750d7d9b7e9dbd498202c4b1288a0cbceb1cd65b.png)

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Flatpak
QGIS is now available as a flatpak application on [flathub](https://flathub.org/apps/search/qgis) Flatpak (formerly xdg-app) is a software utility for software deployment, package management, and application virtualization for Linux desktop computers. It allows users to install different QGIS versions on linux without having to recompile or use Docker. It is a full package with all libraries included, and it uses its own user profile locations. So you\'ll need some disk space and new habits working with flatpak, but it rocks!

[![image28](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)

Dit werd mogelijk gemaakt door [Aleix Pol](https://github.com/aleixpol)

Deze mogelijkheid werd ontwikkeld door [Aleix Pol](https://github.com/aleixpol)
### Mogelijkheid: SVG-bestanden kunnen worden ingebed in projecten en symbolen
Maakt het mogelijk dat SVG-afbeeldingen voor symbologie, labels, etc direct worden ingebed in een projectbestand (of QML-stijl, of QPT-afdruksjabloon!) door de SVG te coderen als een standaard base64-tekenreeks.

Aanvullend kunnen ingebedde bestanden uit projecten en symbolen worden uitgenomen en terug worden opgeslagen als op schijf gebaseerde SVG-bestanden.

Dit werd mogelijk gemaakt door [SMEC/SJ](http://smec.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com)
### Mogelijkheid: Op OpenCL gebaseerde acceleratie
Dit werd mogelijk gemaakt door [QGIS.org](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://qgis.org)
## Expressies
### Mogelijkheid: Nieuwe functies en variabelen voor expressies
Vele nieuwe functies voor expressies zijn toegevoegd aan QGIS 3.4. Deze omvatten vele handige functies voor het werken met en manipuleren van array- en kaartobjecten (woordenboek).
- **json_to_map**: Converts a JSON encoded string value to a map (dictionary) type object
- **map_to_json**: Converts a map (dictionary) type object to a JSON encoded string value
- **hstore_to_map**: Converts a hstore value to a map (dictionary) type object
- **map_to_hstore**: Converts a map (dictionary) type object to a hstore value
- **array_foreach** : Loops over an array and executes an expression on each item in the array, returning a new array containing each calculated value
- **array_filter** : Filters an array according to an expression
- **raster_value**: Returns a value sampled from a raster layer at a specified point
- **to_dms**: Converts a numeric value to a Degrees, Minutes, Seconds formatted string
- **to_dm**: Converts a numeric value to a Degrees, Minutes formatted string
- **line_substring**: Returns the portion of a line (or curve) geometry which falls between the specified start and end distances (measured from the beginning of the line). Z and M values are linearly interpolated from existing values.
- **generate_series(start,stop,step)**: Creates an array containing a sequence of numbers.

Aanvullend zijn enkele nieuwe variabelen beschikbaar gemaakt om te gebruiken binnen expressies van QGIS:
- **\@canvas_cursor_point**: Contains a point value representing the current position of the mouse cursor within the main map canvas
- **\@map_layers**: Contains an array of all layers which are visible within the map
- **\@map_layer_ids**: Contains an array of all layer IDs for layers visible within the map

[![image2](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)

Deze mogelijkheid werd ontwikkeld door [Etienne Trimaille, Matteo Ghetta, Matthias Kuhn, Mathieu Pellerin, Nyall Dawson](https://qgis.org)
### Mogelijkheid: Aanvullen van code voor expressiebouwer
Automatisch aanvullen van code in de expressiebewerker.
- Variabelen, namen van functies en veldnamen worden voorgesteld en automatisch ingevoegd bij het schrijven van expressies
- Parameters voor functies worden weergegeven als zij worden ingevoerd

[![image3](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)

Dit werd mogelijk gemaakt door [OPENGIS.ch](https://www.opengis.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch/)
## Kaartgereedschap
### Mogelijkheid: Objecten identificeren of selecteren, gebaseerd op bestaande polygoon
Often it is useful to select/identify features that are covered by an existing polygon. For this, users can use \"Select Features by Polygon\" and \"Identify Features by Polygon\" tools, but it was necessary to manually trace the polygon of interest. This new feature allows user to right click on the map and pick an existing polygon feature at that location from popup menu - that polygon will be used as input for selection or identification.

[![image4](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)

Dit werd mogelijk gemaakt door Leicestershire County Council

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Gebruikersinterface
### Mogelijkheid: Automatisch selecteren van geëxporteerde bestanden in bestandsbeheer
Whenever a message bar item links to a created file (e.g. after exporting a layout or map layer), the link will now directly open the folder containing this file within the operating system file browser AND pre-select the created file. It\'s a super-handy shortcut speeding up file operations after an export from QGIS!

[![image5](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe optie \"Map openen\" voor uitgeschakelde projecten op de pagina Welkom
Deze nieuwe optie in het contextmenu, met rechts klikken, voor uitgeschakelde items op de pagina Welkom stelt gebruikers in staat om het dichtstbijzijnde bestaande pad te openen naar de originele projectlocatie in hun bestandsbeheerder, hopelijk om ze te helpen ontbrekende/verplaatste/hernoemde projecten terug te vinden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan UX voor tijdelijke tekenlagen
Temporary Scratch Layers in QGIS can be very handy when a \"throw-away\" layer is needed, such as when pre-processing data in multiple steps. However, they can be a trap for uniformed users who may not realise that the contents of the layer will be permanently lost when the current QGIS project is closed. Accordingly, a new indicator icon has been added which shows up next to any temporary scratch layers in the layer tree, making it immediately clear which layers are temporary only.

It\'s also much easier to transition these temporary layers to permanent disk-based formats. You can either click the new indicator icon or select \"Make Permanent\" from the layer context menu. QGIS will then prompt for a location to save the temporary layer to, then replaces it in place (keeping the same layer ID, style, form settings, etc).

[![image6](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan taakbeheer
The QGIS task manager widget (shown in the status bar whenever a background task is running) now shows an estimated time remaining and completion time for long-running background tasks. This Estimated Time of Arrival is calculated using a simple linear interpolation based on the task\'s elapsed time and current progress, and allows users to know whether they\'ve only got time to make an instance coffee in the office kitchen or walk round the block for a proper barista made coffee before that long processing task completes\...

Additionally, QGIS uses the standard operating system progress reporting mechanisms on more platforms and occasions in QGIS 3.4. Some long running tasks (which don\'t run in the background) such as atlas exports now show their progress via the operating system mechanism, and throw up handy completion notifications.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Hyperlinks naar lokale vector- & rastergegevenssets in het paneel Informatie
For local vector and raster datasets, the Information tab within the layer properties dialog now features source file path hyperlinks. Upon clicking on the hyperlink, the system\'s file navigator will open and automatically highlight the dataset.

[![image7](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)

Dit werd mogelijk gemaakt door [iMhere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Mogelijkheid: Verbeteringen aan stijlbeheer
Het QGIS-dialoogvenster Stijlbeheer (dat gebruikers in staat stelt hun eigen bibliotheken met symbolen en kleurverlopen in te stellen en te beheren) opent nu niet-modaal, dus het kan nu naast het hoofdvenster van QGIS worden gebruikt (net zoals het dialoogvenster Lay-outbeheer en de vensters van Afdruklay-out ontwerpen).

We\'ve also improved the preview of symbols within the Layer Styling dock, adding a toggle to switch between a large icon view and a detailed list view of symbols. Hovering over symbols (and colors!) now shows a large preview of the symbol. Finally, we\'ve made symbol lists more hi-dpi friendly.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Gepolijste interface en ervaring met browserpaneel
Tonnen werk werden voor deze uitgave uitgevoerd om de gebruikersinterface en ervaring met het browserpaneel te verbeteren, inclusief reparaties voor HiDPI, verbeteringen voor gecomprimeerde vector-/rastergegevenssets, en een vernieuwde set pictogrammen.

Ook functionaliteit werd toegevoegd, inclusief de mogelijkheid om een nieuwe map te maken direct vanuit het contextmenu van de browser. De browser geeft nu ook een meer volledig bereik van opties weer voorverbindingen naar SQL Server, waarmee deze opties overeenkomen met die welke reeds beschikbaar waren voor andere verbindingen naar databases.

[![image8](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin (iMHere Asia), Nyall Dawson (North Road)
### Mogelijkheid: Widget QML diagrammen en tekenen
Een nieuw type widget voor formulieren voor vectorlagen voor het weregeven van grafisch aantrekkelijke en interactieve items, zoals diagrammen of technische tekeningen op het formulier voor attributen is toegevoegd in QGIS 3.4. Het widget ondersteunt een flexibele configuratie, inclusief voorbeeldsjablonen en ondersteuning voor expressies.

[![image9](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)

Dit werd mogelijk gemaakt door [QGIS Project](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [David Signer and Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Symbologie
### Mogelijkheid: Stijlen van lagen met mazen
- Gegevenssets toevoegen aan lagen met mazen vanuit het paneel Eigenschappen
- Informatie- en bronpaneel in paneel Eigenschappen
- Selecteren van actieve gegevensset (paneel Eigenschappen of Stijl)
- Stijlen van contouren/scalairen (paneel Eigenschappen of Stijl)
- Stijlen van frame van mazen (paneel Eigenschappen of Stijl)
- Stijlen van vectorpijlen (paneel Eigenschappen of Stijl)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)
### Mogelijkheid: Symmetrie classificeren in renderer Gradueel
Dit werd mogelijk gemaakt door <https://github.com/pierreloicq>

Deze mogelijkheid werd ontwikkeld door <https://github.com/pierreloicq>
### Mogelijkheid: Gedeeltelijk exporteren en importeren van QML
When exporting and importing styles to and from `.qml` files it is now possible to select a subset of sections. This allows to save and restore parts of a layer configuration while omitting others. For example, it\'s possible to export only the symbology of a layer and when importing this QML style file into a layer, any configuration on the forms and widgets or other properties are unaffected. It is also possible to only handle single sections of a style when using copy/paste.

[![image10](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)

Dit werd mogelijk gemaakt door [qwat group](http://qwat.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud (OPENGIS.ch GmbH)](https://www.opengis.ch)
## Digitaliseren
### Mogelijkheid: Verbeteringen aan GPS-tracking
QGIS 3.4 extends the inbuilt GPS tracking support, adding \"acquisition interval\" and \"distance threshold\" parameters. These options can be used to keep the cursor stationary when the receiver is in static conditions.

Dit werd mogelijk gemaakt door [Andrea Rossi](https://github.com/rossia)

Deze mogelijkheid werd ontwikkeld door [Andrea Rossi](https://github.com/rossia)
### Mogelijkheid: Meer keuzes voor hoeken in paneel Geavanceerd digitaliseren
Opties werden toegevoegd om snappen mogelijk te maken aan 5/10/15/18/22,5 graden in modus Constructie.

[![image11](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)

Dit werd mogelijk gemaakt door [lbartoletti](https://github.com/lbartoletti)

Deze mogelijkheid werd ontwikkeld door [lbartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Gereedschap Punten kan alleen op de huidige laag werken
The new vertex is a lot more productive now. It can move vertices of all editable layers at once, which is great to preserve cross layers topology. However in many cases, many of us don\'t want to modify all layers at once. We added a variation of the vertex map tool just for that.

[![image12](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)

Dit werd mogelijk gemaakt door [Oslandia](https://oslandia.com)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](https://oslandia.com/en/home-en/)
### Mogelijkheid: Kaartgereedschap Omgekeerde lijnen toegvoegd
A long awaited feature ! No more external plugin or algorithm to reverse a line\'s direction!

[![image13](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)

Dit werd mogelijk gemaakt door [OSLANDIA](https://oslandia.com)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Precisie geometrie
Vectorlagen hebben een optie voor configuratie van de precisie. De precisie definieert hoe nauwkeurig de locatie van punten zou moeten worden opgeslagen. Elk punt of nieuwe of bewerkte geometrieën wordt gevangen aan een raster van deze resolutie. Tijdens het digitaliseren wordt het raster weergegeven om de gebruiker te helpen.

[![image14](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Automatisch verwijderen van gedupliceerde knopen
Bij het toevoegen of bewerken van geometrieën op een vectorlaag kan QGIS automatisch gedupliceerde knopen uit geometrieën verwijderen. Deze optie is te configureren op de tab Digitaliseren van vectorlagen.

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Controleren op geldigheid van geometrie
Elke nieuwe of bewerkte geometrie kan worden gecontroleerd op geldigheid als deze optie is geactiveerd. Dit maakt het mogelijk tranparant te communiceren naar een gebruiker als er geometrieën met fouten worden geproduceerd tijdens de huidjge sessie van bewerken.

[![image15](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Controles van topologie tijdens bewerken
Controles van topologie kunnen worden geactiveerd op een laag. Voor nieuw toegevoegde en bewerkte geometrieën kunnen controles van toplogie worden uitgevoerd. De controles zullen worden uitgevoerd als de laag wordt opgeslagen of bij het klikken op de knop voor het controleren van de topologie in het paneel voor Geldigheid van de geometrie.

De volgende controles zijn beschikbaar:
- Gaten
- Overlappingen
- Ontbrekende punten op nabijgelegen polygonen

This builds on top of the functionality of the geometry checker plugin which was implemented by [Sourcepole](https://sourcepole.ch).

[![image16](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gegevensbeheer
### Mogelijkheid: Vertalen van projecten van QGIS
Like QGIS and the plugins, the projects are translated with the Qt translation process. Means, it makes the translation according to a Qt Compiled Translation Source File (`.qm` file). When the user opens a project, QGIS checks for a `.qm` file laying in the same folder like the `.qgs` file, having the same name like the `.qgs` file and having the language-code as postfix of the users language (the language configured in the QGIS settings). To create the translation, in the project settings, there is an option to generate the `.ts` file, that can edited by programs like Qt Linguist or Transifex.

More information in [this blog post](https://new.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep en QGEP Project](https://www.qgis.ch/en)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch/)
### Mogelijkheid: Attributentabel kan op verzoek worden vastgezet
A button has been added to the Attribute Table toolbar for switching between docked and window mode on demand. Previously users had to change an option in the settings dialog and open a new table in order to switch between docked/undocked mode, but that\'s painful if you decide *after* a table is already open that you\'d like to dock/undock it\...!

[![image17](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuw filter voor locatie om over alle lagen te zoeken
A new locator filter has been added which allows users to search across *all* layers in their project, by the layer\'s display expression.

The filter can be activated by using the prefix \'af\', or by making it a default search via QGIS options -\> Locator -\> Features In All Layer. Display expressions are defined in the vector layer properties under the display tab. Individual layers can be marked as not searchable in the Project Properties dialog, under the Data Sources tab.

[![image18](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)

Dit werd mogelijk gemaakt door [Opengis.ch](https://www.opengis.ch/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Niet-verwijderbare (vereiste) lagen geaccentueerd in lagenboom
A new indicator \"locked\" icon is shown for any layers marked as \"required\" within the current project. This icon gives users instant feedback that a particular layer cannot be removed from the project.

Vereiste lagen worden geconfigureerd via het dialoogvenster Projecteigenschappen, tab Databronnen.

[![image19](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Rasterlaag aan een bestaand Geopackage toevoegen
When saving a raster layer to GeoPackage database, it\'s now possible to append the layer to an existing file.

[![image20](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)

Dit werd mogelijk gemaakt door [Borys Jurgiel](https://github.com/borysiasty)

Deze mogelijkheid werd ontwikkeld door [Borys Jurgiel](https://github.com/borysiasty)
## Formulieren en widgets
### Mogelijkheid: Formulieren voor dieper zoeken (cascading) in QGIS widgets Waarderelatie
New functions and logic in QGIS "Value Relation Widgets", allowing the implementation of complex, dynamic filters within QGIS attribute forms. The functionality can be used to implement "drill-down" forms within QGIS, where the values available in one field depend on the values of other fields:

[![image21](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)

Dit werd mogelijk gemaakt door [QGIS community through crowd-funding](https://north-road.com/drill-down-cascading-forms/)

Deze mogelijkheid werd ontwikkeld door Alessandro Pasotti (met North Road)
## Printvormgeving
### Mogelijkheid: 3D-kaartitems
Deze mogelijkheid stelt gebruikers in staat hun 3D-kaartweergave toe te voegen aan de afdruklay-out.

[![image22](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)

Dit werd mogelijk gemaakt door [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](https://www.lutraconsulting.co.uk/)
## Processing
### Mogelijkheid: Nieuwe modus \"Op plaats bewerken\"
Dankzij een groot aantal [genereuze gevers](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/), werd een door crowdfunding mogelijk gemaakte modus \"Op plaats bewerken\" toegevoegd aan Processing voor 3.4. Wanneer een vectorlaag actief is en bewerkbaar, stelt deze modus gebruikers in staat om geschikte algoritmes direct uit te voeren op de objecten van de laag, hun attributen en geometrieën op de plaats aan te passen. Alle bewerkingen worden toegevoegd aan de \“bewerkingsbuffer\” van de laag, dus u kunt de wijzigingen eenvoudig ongedaan maken en opnieuw uitvoeren voordat u ze terug opslaat in de gegevensbron.

For those power users who perform frequent data edits, this functionality is also exposed via QGIS 3.0's "Locator bar" (that "type to locate" bar which sits in the bottom-left corner). Typing 'ef' ("edit features") followed by the name of the corresponding operation allows you to perform the edits directly via the keyboard. E.g.
- Een aantal lijnobjecten selecteren
- Druk op Ctrl + K (activeert de locatiebalk)
- Type "ef reverse"
- Press enter -- the selected line features will be reversed immediately!

[![image23](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)

Dit werd mogelijk gemaakt door [Crowdfunding campaign](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com)
### Mogelijkheid: Modellen in het project opslaan
Some Processing models are so intrinsically linked to the logic inside a particular project that they have no meaning (or are totally broken) outside of that project (e.g. models which rely on the presence of particular map layers, relations, etc). Accordingly, from QGIS 3.4, Processing models can be stored inside QGIS project files. Any models stored within a project are made available as soon as that project is opened. This also avoids cluttering up the \"global\" model provider with models which make no sense, and makes it easier to distribute a single project all relevant models included.

Models are stored inside projects by clicking the new \"Embed in Project\" button in the Modeler dialog toolbar. Models can be removed from a project from the model\'s right click menu in the toolbox.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Monster rasterwaarden
Een nieuw algoritme werd toegevoegd voor monsterneming van waarden van rasterlagen op locaties van punten.

[![image24](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)

Dit werd mogelijk gemaakt door [Faunalia](https://www.faunalia.eu)

Deze mogelijkheid werd ontwikkeld door [Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Mogelijkheid: Nieuw algoritme \'Raster pixels to polygons\'
Dit algoritme converteert een rasterlaag naar een vectorlaag, met een polygoonobject dat correspondeert met elke pixel uit het raster en een enkel veld dat de bandwaarde uit het raster bevat.

Dit werd mogelijk gemaakt door [SMEC/SJ](http://smec.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com)
### Mogelijkheid: Algoritme K Means clustering
QGIS 3.4 adds a native \"k-means clustering\" algorithm. Based on a port of PostGIS\' ST_ClusterKMeans function, this algorithm adds a new cluster ID field to a set of input features which identifies the feature\'s cluster based on a k-means clustering approach. If non-point geometries are used as input, the clustering is based off the centroid of the input geometries.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Dbscan spatial clustering
Dit nieuwe eigen algoritme implementeert een geoptimaliseerde op dichtheid gebaseerde benadering DBSCAN cluster voor het clusteren van 2D puntobjecten.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeterde algoritmes
Enkele verschillende verbeteringen voor bestaande algoritmes van Processing omvatten:
- Het algoritme *Reverse line direction* werkt nu met MultiLineString geometrie-invoer
- *Extend lines*: ondersteuning voor dynamische (datagedefinieerde) begin- en eindafstanden werd toegevoegd
- *Offset lines*: ondersteuning voor dynamische afstand voor verschuiving werd toegevoegd
- De algoritmes *Join by Field Value* en *Join by Location* kunnen nu, optioneel, niet overeenkomende records exporteren
- *Join by Field Value* rapporteert ook aantallen overeenkomende/niet overeenkomende objecten

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritmes Filter Vertices by M en Filter Vertices by Z
Twee nieuwe algoritmes werden toegevoegd voor het filteren van punten lijn/polygoon op hun M- of Z-waarde. Een minimum en maximum M/Z-waarde kan worden ingevoerd, en als de punten buiten deze bereiken vallen zullen zij worden genegeerd in de uitvoergeometrie. Zowel de minimum als de maximum filterwaarde kunnen ook datagedefinieerd worden, dus kunnen zij per object variëren.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid:  Algoritme \"Array of Translated Features\"
Dit nieuwe algoritme maakt kopieën van objecten in een laag, door meerdere vertaalde (verschoven) versies van het object te maken. Elke kopie wordt verplaatst met een vooraf opgegeven hoeveelheid op de X/Y/Z/M-as.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme \"Array of offset (parallel) lines\"
Dit nieuwe algoritme maakt kopieën van lijnobjecten in een laag, door meerdere parallelle versies van elk object te maken. Elke kopie wordt verschoven met een vooraf opgegeven afstand.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Keuze voor eenheden voor geen graden/onbekende afstanden
Wanneer een algoritme een parameter afstand heeft in meters/feet/etc (d.i. niet-geografische afstanden), is een combinatievak toegevoegd voor het kiezen van het type eenheid.

(QGIS geeft dit niet weer (en zou dat ook **nooit** moeten doen) voor afstanden in graden \-- het is in deze situatie aan de gebruiker om een geschikte lokale projectie te kiezen en hun gegevens opnieuw te projecteren om overeen te komen.)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com)
### Mogelijkheid: Algoritmes \"Drape features to z/m\"
Deze twee nieuwe algoritmes kunnen Z- of M-waarden van geometriepunten instellen naar monsterwaarden die zijn genomen uit een rasterband. Waarden kunnen optioneel worden geschaald met behulp van een (datagedefinieerde) schaalwaarde.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Raster pixels to points\" algorithm
A new \"pixels to points\" algorithm was added in QGIS 3.4, which creates a point feature at the center of every pixel. nodata pixels are skipped.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Line substring
Dit nieuwe, veel om gevraagde, algoritme geeft het gedeelte van een lijn (of een boog) terug dat valt tussen de gespecificeerde begin- en eindafstanden (gemeten vanaf het begin van de lijn). Z- en M-waarden worden lineair geínterpoleerd vanuit bestaande waarden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Interpolate point on line\" algorithm
Dit nieuwe algoritme maakt een puntgeometrie, geïnterpoleerd op een ingestelde afstand langs de lijn- (of grens van de polygoon) geometrieën. Gebogen invoergeometrieën worden volledig ondersteund. Z- of M-waarden worden lineair geïnterpoleerd, gebaseerd op bestaande waarden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: k-neighbour concave hull
Dit werd mogelijk gemaakt door <https://qgis.org>

Deze mogelijkheid werd ontwikkeld door [Detlev Neumann, Rudi von Staden](https://qgis.org)
### Mogelijkheid: Pythonscripts die algoritmes implementeren voeren nu het algoritme uit bij slepen en neerzetten en dubbelklikken in de browser
Indien van toepassing zullen scripts nu een dialoogvenster voor algoritmes van Processing openen bij:
- Slepen en neerzetten van een script voor Python in het hoofdvenster
- Using the browser panel\'s right-click run script action

[![image25](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)

Dit werd mogelijk gemaakt door [iMhere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: New GDAL\'s rearrange band algorithm
A new GDAL provider \'Rearrange band\' algorithm was added to the processing toolbox. The algorithm allows to output rasters continuing a subset of a given input raster\'s bands, and offers the possibility to re-order the bands.

[![image26](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)

Dit werd mogelijk gemaakt door [iMHere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: \"Precalculated\" values for model algorithm parameters
A new option is present for all parameters of using a \"precalculated expression\". This expression is evaluated once before the child algorithm is executed and used during the execution of that algorithm.

Dit werd mogelijk gemaakt door [QGIS](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Categorize a layer using a style XML file\" algorithm
This new algorithm sets a vector layer\'s renderer to a categorized renderer using matching symbols from a style database.

A specified expression (or field name) is used to create categories for the renderer, with QGIS creating a category for each unique value within the layer. Each category is individually matched to the symbols which exist within the specified QGIS XML style database. Whenever a matching symbol name is found, the category\'s symbol will be set to this matched symbol.

De overeenkomst is standaard niet hoofdlettergevoelig, maar kan, indien gewenst, worden ingesteld op hoofdlettergevoelig. Optioneel kunnen niet-alfanumerieke tekens in zowel de waarde van de categorie als de naam van het symbool worden genegeerd bij het uitvoeren van de vergelijking. Dit maakt een hogere tolerantie mogelijk bij het vergelijken van categorieën met symbolen.

Indien gewenst kunnen ook tabellen worden uitgevoerd die lijsten bevatten van de categorieën die niet overeenkwamen met symbolen, en symbolen die niet overeenkwamen met categorieën.

[![image27](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe modus voor algoritme Snap geometries
The new mode \"Snap to anchor nodes (single layer only)\" makes sure that any two vertices of the vector layer are at least at distance given by the threshold value.

Dit algoritme is handig bij bewerkingen waarbij vectoren over elkaar worden gelegd, zoals kruisen, verenigen of verschil om mogelijke topologische fouten, veroorzaakt door numerieke fouten als coördinaten heel dicht bij elkaar liggen, te voorkomen. Na het uitvoeren van het algoritme zouden eerdere geldige geometrieën ongeldig kunnen zijn geworden en daarom kan het nuttig zijn daarna het algoritme Fix geometries uit te voeren.

Dit werd mogelijk gemaakt door [InaSAFE DFAT](https://www.dfat.gov.au/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Gegevensproviders
### Mogelijkheid: Plug-in OAuth2 authenticatiemethode
- Ondersteunt authenticatiecode, impliciete en stromen met toestemming van broneigenaar
- Maakt vooraf geconfigureede verbindingen mogelijk, gelezen vanuit standaard locaties
- Biedt cachen van toegangstoken over opnieuw opstarten van QGIS heen
- Configuraties Opslaan/laden 

Dit werd mogelijk gemaakt door [Monsanto Company](https://monsanto.com/)

Deze mogelijkheid werd ontwikkeld door [Larry Shaffer, Alessandro Pasotti](https://qgis.org)
### Mogelijkheid: Laag met mazen: Ondersteuning voor nieuwe indeling lagen met mazen
Lagen met mazen geven gegevens weer in een raster met variabele grootte met extra componenten (bijv. tijd en vector). Met de introductie van MDAL kunnen gebruikers de volgende indelingen direct in QGIS laden en alle andere componenten verkennen:
- GRIB
- XMDF
- Netcdf

[![image29](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Laag met mazen: functie toegevoegd om waarde te identificeren op lagen met mazen
Met deze API kunnen ontwikkelaars elementen van mazen inspecteren en waarden ophalen, ruimtelijk en tijdelijk. Als voorbeeld kunt u een plot van een tijdreeks maken uit uw laag met mazen.

[![image30](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Laag met mazen: mogelijk maken om verschillende vector en scalaire gegevensset te kiezen
Een laag met mazen bevat vaak diverse kwantiteiten. Een netcdf/grib kan bijvoorbeeld verscheidene meteorologische kwantiteiten bevatten. Elke kwantiteit kan ook meerdere componenten hebben. Windgegevens kunnen bijvoorbeeld snelheid (scalair) en waarden (raster) bevatten. Met deze optie kun u scalairen en rasters over elkaar leggen uit verschillende kwantiteiten. In de afbeelding hieronder ziet u temperatuur (raster) en wind (scalair).

[![image31](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Laag met mazen: mogelijk maken van renderen van vectoren/pijlen op het gebruigedefinieerde raster
Scalaire gegevens worden gewoonlijk in het midden/hoek van elk element mesh gegenereerd. Bij het weergeven van scalaire gegevens zien de pijlen er misschien dun uit en is het vaak niet mogelijk de algemene trend te zien. Met deze optie kunnen pijlen worden weergegeven op een gebruikergedefinieerd raster. Extra scalaire waarden zullen direct worden geïnterpolateerd en geplaatst op het gebruikergedefinieerde raster.

[![image32](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Ondersteuning voor type JSON/JSONB
The reading of PostgreSQL JSON types is supported. JSON Data can be displayed in the widgets as \"Key/Value\" (maps), as \"List\" (arrays) or as text.

[![image33](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Ondersteuning voor ESRI tokenauthenticatie
Support has been added to QGIS\' Authentication system for ESRI\'s temporary token based authentication. This allows for connection to ArcGIS Feature and Map Servers via an allocated temporary token.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: SQL Server - Afhandeling ongeldige geometrie
Recent versions of QGIS have switched to a safer approach to reading SQL Server layers, which automatically checks for geometry validity and repairs geometries when needed. This workaround is required to avoid issues with the design of SQL Server\'s geometry handling, where encountering any rows with invalid geometries can silently abort a request without returning all the features from a layer. Unfortunately, the workaround comes at a significant performance cost.

In QGIS 3.4 a new setting was added to allow users to manually turn off QGIS\' SQL Server invalid geometry handling. Turning on the \"Skip invalid geometry handling\" setting under a SQL Server connection\'s properties causes QGIS to skip all the expensive geometry validation processing, but firmly places the responsibility for ensuring that all features on the database have valid geometries back upon the user/database administrator. **This is a \"use at your own risk\" setting. Improperly enabling this option can lead to missing features and data loss.**

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## QGIS Server
### Mogelijkheid: Servercache kan worden beheerd door plug-ins
Standaard cacht QGIS Server alleen in geheugen documenten WMS GetCapabilities. Met implementatie van WMTS is het nodig om een manier te hebben om tegels te cachen. Maar het beheer van de cache is niet ontwikkeld om alleen tegels te cachen.

De plug-in Cache-beheer kan worden gerbuikt om te cachen:
- documenten WMS, WFS, WCS, WMTS GetCapabilities 
- documenten WFS DescribeFeatureType 
- documenten WCS DescribeCoverage 
- afbeeldingen WMTS GetTile
- afbeeldingen WMS GetLegendGraphic

Hier is een klasse Cache manager voor Python die niet verifieert of het project van QGIS is gewijzigd:

    class PyServerCache(QgsServerCacheFilter):
    
        """ Used to have cache control """
    
        def __init__(self, server_iface):
            super(QgsServerCacheFilter, self).__init__(server_iface)
    
            self._cache_dir = os.path.join(tempfile.gettempdir(), "qgs_server_cache")
            if not os.path.exists(self._cache_dir):
                os.mkdir(self._cache_dir)
    
            self._tile_cache_dir = os.path.join(self._cache_dir, 'tiles')
            if not os.path.exists(self._tile_cache_dir):
                os.mkdir(self._tile_cache_dir)
    
        def getCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                return QByteArray()
    
            doc = QDomDocument(m.hexdigest() + ".xml")
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "r") as f:
                statusOK, errorStr, errorLine, errorColumn = doc.setContent(f.read(), True)
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            return doc.toByteArray()
    
        def setCachedDocument(self, doc, project, request, key):
            if not doc:
                print("Could not cache None document")
                return False
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "w") as f:
                f.write(doc.toString())
            return os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                os.remove(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
            return not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocuments(self, project):
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            for f in filelist:
                os.remove(os.path.join(self._cache_dir, f))
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            return len(filelist) == 0
    
        def getCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                return QByteArray()
    
            img = QImage(m.hexdigest() + ".png")
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "rb") as f:
                statusOK = img.loadFromData(f.read())
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            img.save(buff, 'PNG')
            return ba
    
        def setCachedImage(self, img, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "wb") as f:
                f.write(img)
            return os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                os.remove(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
            return not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImages(self, project):
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join(self._tile_cache_dir, f))
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            return len(filelist) == 0
    
En de manier om die toe te voegen aan cache-beheer van QGIS Server.

`servercache = PyServerCache(server_iface) server_iface.registerServerCache(servercache, 100)`

Dit werd mogelijk gemaakt door [Ifremer](https://wwz.ifremer.fr/)

Deze mogelijkheid werd ontwikkeld door [3Liz](https://3liz.com)
### Mogelijkheid: Ondersteuning voor WMTS 1.0.0
QGIS Server 3.4 ondersteunt de OGC-standaard WMTS 1.0.0.

In projecteigenschappen van QGIS kan de gebruiker definiëren:
- welk delen van het project (het gehele project, groepen van lagen of lagen) moeten worden gepubliceerd volgens de standaard van WMTS
- de mininale schaal van de tegels

QGIS Server hergebruikt het in de WMS gedefinieerde CRS voor WMTS.

Een plug-in voor QGIS Server met een klasse QgsServerCacheFilter dient te worden geïnstalleerd en geladen door QGIS Server om de cache voor tegels te beheren.

[![image34](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)

Dit werd mogelijk gemaakt door [Ifremer](https://wwz.ifremer.fr/)

Deze mogelijkheid werd ontwikkeld door [3Liz](https://3liz.com)
### Mogelijkheid: Mogelijkheid toegveoegd om de minimale schaal voor WMTS te definiëren
Dit werd mogelijk gemaakt door <https://github.com/rldhont>

Deze mogelijkheid werd ontwikkeld door <https://github.com/rldhont>
### Mogelijkheid: Ondersteuning voor logs naar stderr voor QGIS Server
It\'s now possible to configure QGIS Server to make it write its logs to stderr. This is done by setting the QGIS_SERVER_LOG_FILE env var to the special value \"stderr\".

Dit werd mogelijk gemaakt door [OSLANDIA](https://oslandia.com)

Deze mogelijkheid werd ontwikkeld door [Eric Lemoine](https://github.com/elemoine)
## Plug-ins
### Mogelijkheid: Ondersteuning voor versleutelde ZIP's in Plug-ins beheren
Plug-ins beheren is nu in staat plug-ins te installeren vanuit lokale ZIP-bestanden, zelfs als die zijn versleuteld.

[![image35](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)

Dit werd mogelijk gemaakt door [Borys Jurgiel](https://github.com/borysiasty)

Deze mogelijkheid werd ontwikkeld door [Borys Jurgiel](https://github.com/borysiasty)
### Mogelijkheid: GeoPackage offline bewerken
Met de functionaliteit Offline bewerken is het  mogelijk om te selecteren of de export een SpatiaLite of een bestand voor GeoPackage moet maken voor gebruik offline.

Dit werd mogelijk gemaakt door [Oester Messtechnik](https://messtechnik.ch/)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch)
## Programmeerbaarheid
### Mogelijkheid: QgsSpatialIndexKDBush
A very fast static spatial index for 2D points based on a flat KD-tree, using <https://github.com/mourner/kdbush.hpp>

Compared to QgsSpatialIndex, this index: - supports single point features only (no multipoints) - is static (features cannot be added or removed from the index after construction) - is much faster! - supports true \"distance based\" searches, i.e. return all points within a radius from a search point

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: QgsRasterDataProvider::sample methode voor efficiëntt nemen van monsters van rasters op een bepaald punt
This is an alternative to the `QgsRasterDataProvider::identify` method, which is less efficient but more powerful

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe aanroep voor geometrie API om een gebogen subtekenreeks te rug te geven
Nieuwe PyQGIS API is toegevoegd om het eenvoudiger te maken een subtekenreeks te halen uit een geometrie LineString/Curve:

`QgsCurve::curveSubstring - Returns a new curve representing a substring of a curve, from a start distance and end distance.`

If z or m values are present, the output z and m will be interpolated using the existing vertices\' z or m values. The method also handles curved geometries without loss or segmentation.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: sip Module API wijzigingen
Due to upstream changes within the PyQt/sip library, the recommended way to import this module has changed in QGIS 3.4. For maximum portability, instead of directly calling: `import sip` plugins should instead use: `from qgis.PyQt import sip` Using this newer style import will ensure that the code works correct across all platforms and remains functional in future QGIS versions.
### Mogelijkheid: Python vectorgegevensproviders
Ontwikkeling van de API, een provider voor monsters en testen maken het mogelijk een vectorgegevensprovider te maken in pure Python.

[![image36](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)

Dit werd mogelijk gemaakt door Good will

Deze mogelijkheid werd ontwikkeld door Alessandro Pasotti
## 3D-objecten
### Mogelijkheid: Verbeterde navigatie
This will update camera\'s view center as the camera moves around. Before the view center would be always at the zero elevation, which means that with terrain further away from zero elevation tilting and rotation of camera would feel weird due to the center point being far away.

Op en neergaan van de camera mogelijk maken met behulp van de toetsen Page up/down

Camera verplaatsen met behoud van de positie met Ctrl + pijltjestoetsen / muis

[![image37](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)

Dit werd mogelijk gemaakt door [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Animatie
U kunt een animatie maken, gebaseerd op een set sleutelframes - cameraposities op bepaalde tijden. QGIS 3D interpoleert dan de cameraposities/-rotaties tussen de sleutelframes.

Stel eerst de scene van uw kaart in door roteren, zoomen of verplaatsen van de camera om de sleutelframes te maken. Wijs dan een tijd toe aan het frame. Er zijn verscheidene methoden voor interpolaties tussen sleutelframes.

[![image38](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)

Dit werd mogelijk gemaakt door [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

Deze mogelijkheid werd ontwikkeld door [Martian Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Eenvoudig renderen van 3D-lijnen
Deze modus voor 3D renderen van lijnen zal OpenGL renderen van lijnen gebruiken in plaats van het bufferen van lijnen in polygonen en ze te renderen als mazen.

The advantage is that the 3D lines do not loose their Z coordinate which is the case currently with \"ordinary\" 3D rendering after buffering.

The disadvantage is that the lines cannot be wide (supported in Qt3D only since 5.10, but even then their rendering won\'t have nice joins/caps) and only ambient color is used from the material.

[![image39](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Kaartgereedschap Identificatie voor 3D-weergaven
Een nieuw gereedschap Identificatie werd geïntroduceerd voor de 3D-kaart. Met behulp van dit gereedschap kunt u objecten inspecteren vanuit de 3D-scene.

[![image40](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)

Dit werd mogelijk gemaakt door [Department of Environment, Land and Infrastructure Engineering (DIATI)](https://www.faunalia.eu/en/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Experimentele Python API
Enkele klassen van QGIS 3D zijn beschikbaar gemaakt voor ontwikkelaars in Python. Het is nu mogelijk om 3D-renderers van lagen te bevragen of te wijzigen en eigenschappen te lezen/schrijven van opgenomen 3D-symbolen, zoals kleuren van materiaal. Onthoud dat voor nu de API wordt beschouwd als experimenteel, dus die zou kunnen wijzigen in toekomstige uitgaven van 3.x.

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
