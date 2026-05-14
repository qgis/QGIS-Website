---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.8{#changelog28 }
Datum uitgave 20-02-2015

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Long Term Release**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

Het doel van LTR-uitgaven is om een stabiel en minder vaak wijzigend platform te verschaffen voor bedrijven en organisaties die zich niet meer dan eenmaal per jaar willen bezighouden met het bijscholen van gebruikers, trainingsmateriaal etc.  Het succes van de LTR hangt heel veel van u, onze geliefde gebruikers, af, we hebben uw ondersteuning nodig om ons probleemoplossingen aan te reiken en er voor zorgend dat u in uw ondersteuningscontracten met verleners van ondersteuning specificeert dat probleemoplossingen die voor u worden toegepast ook worden toegepast op de tak van de LTR als ook op onze normale takken voor ontwikkeling.

Als een LTR belangrijk voor u is, overweeg dan ook directe ondersteuning voor het project QGIS, of moedig uw zakelijke dienstverlener aan om de LTR als basis te gebruiken voor uw zakelijke oplossing zodat iedereen kan profiteren van een stabiel platform dat doorlopend wordt verbeterd en verfijnd. Onthoud dat voor gebruikers en organisaties die graag de grenzen verkennen, onze viermaandelijkse uitgaven ongewijzigd door blijven gaan.

**Nieuwe mogelijkheden**

QGIS 2.8 is ook een speciale uitgave omdat het zoveel fantastische nieuwe mogelijkheden bevat, wijzigingen en verbeteringen om het het meest populaire vrije desktop GIS te maken, zelfs meer gevuld met mogelijkheden en nuttig.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Expressies invoeren in draaivelden
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Mogelijkheid: Favoriete plaatsen kunnen worden geïmporteerd/geëxporteerd
Het is nu mogelijk om uw Favoriete plaatsen naar/vanuit een bestand op te slaan/te laden. Dit maakt het eenvoudiger om locaties van Favoriete plaatsen te delen, of ze tussen computers uit te wisselen.

**Deze mogelijkheid werd ontwikkeld door:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Mogelijkheid: Verbeteringen aan expressies
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Trage evaluatie van expressies**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Mogelijkheid: Doorlopend framework voor testen en verbeteringen in QA
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

We voeren nu ook regelmatig Coverity-scans uit op de codebasis van QGIS. Als resultaat hiervan hebben we meer dan 1000 gevlagde problemen geïdentificeerd en opgelost, inclusief lekken in het geheugen en potentiële crashes. QGIS heeft een dichtheid voor defecten van 0.01 waar het gemiddelde, voor programma's met een soortgelijke grootte, ongeveer 1.0 is.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Analyse-gereedschappen
### Mogelijkheid: Verbeteringen aan dialoogvenster Meten
Het gereedschap voor meten is verbeterd zodat u nu kunt kiezen welke eenheden in het dialoogvenster meten zouden moeten worden gebruikt. Er is ook een nieuw gedeelte informatie in het dialoogvenster dat weergeeft welke instellingen worden gebruikt gedurende de berekeningen van de metingen.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Browser
### Meer responderende browser
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Deze mogelijkheid werd ontwikkeld door:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor contextuele afbeeldingen van legenda's van WMS
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gegevensbeheer
### Mogelijkheid: Aangepast voorvoegsel voor joins
U kunt nu een aangepast voorvoegsel definiëren in het beheer van joins in het dialoogvenster Laag-eigenschappen. Bij het gebruiken van een voorvoegsel, zal de attributentabel nu namen van samengevoegde attributen weergeven met het voorvoegsel van uw voorkeur.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Mogelijkheid: Ondersteuning voor het maken van tijdelijke geheugenlagen
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Mogelijkheid: Ondersteuning voor berekeningen op geselecteerde rijen
In de attributentabel kunt u nu berekeningen doen op alleen de geselecteerde rijen dankzij de nieuwe knop die is toegevoegd op de balk Veldberekening.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Digitaliseren
### Mogelijkheid: Gereedschap Geavanceerd digitaliseren
Indien u ooit wilde dat u  in QGIS lijnen kon digitaliseren exact parallel of in rechte hoeken, lijnen zou kunnen vastzetten onder specifieke hoeken, enzovoort, nu kunt u dat! Het gereedschap Geavanceerd digitaliseren is een port van de plug-in CADinput en voegt een nieuw paneel toe aan QGIS. Het paneel wordt actief bij het vastleggen van nieuwe geometrieën of delen van geometrieén

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Mogelijkheid: Verbeterd gereedschap Vereenvoudigen
Het gereedschap vereenvoudigen is bewerkt, toegevoegd:
- ondersteuning voor opnieuw projecteren van OTF
- gebruiker kan de exacte tolerantie specificeren (niet slechts onzinnige relatieve waarde)
- tolerantie mag worden gespecificeerd in of kaarteenheden, laageenheden of pixels
- instellingen voor tolerantie worden opgeslagen in de instellingen
- meerdere objecten in één keer vereenvoudigen (sleep een rechthoek in plaats van slechts te klikken)
- ondersteuning voor meerdelige objecten
- statistieken over de reductie van het aantal punten

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Mogelijkheid: Verbeteringen voor snappen
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Legenda van laag
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen GUI Printvormgeving
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Modus Volledig scherm voor Printvormgeving**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Mogelijkheid: Verbeteringen voor raster
In de Printvormgeving heeft u nu fijnere controle over de weergave van frame en annotatie. Eerder zou, voor geroteerde kaarten of opnieuw geprojecteerde rasters, de Printvormgeving alle coördinaten voor elke zijde van de kaart tekenen. Dit resulteerde in een weergave van mix van latitude/Y- en longitude/X-coördinaten op één kant. Nu kunt u beheren of u alle coördinaten, alleen latitude of alleen longitude wilt voor elke kant van het kaartframe. Soortgelijke opties zijn ook toegevoegd voor het beheren van hoe een frame voor het kaartraster zal worden opgedeeld.

Nieuwe verticale aflopende richting voor annotaties. Deze wijziging voegt een nieuwe modus aflopende verticale richting toe voor annotaties in het kaartraster. Eerder werd alleen oplopende tekst ondersteund voor verticale annotaties.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Mogelijkheid: Marges voor items Label
- U kunt nu zowel horizontale als verticale **marges voor label**-items beheren. Eerder zou alleen één enkele instelling voor de marge gelden voor zowel de horizontale als de verticale marges. Deze wijziging maakt het voor gebruikers mogelijk verschillende horizontale en verticale marges te specificeren.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Plug-ins
### Mogelijkheid: Verbeteringen voor console Python
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Processing
### Mogelijkheid: Nieuw type parameter geometrisch predikaat
met dit nieuwe type parameter, gebruikt in de algoritmen **Select by location, Extract by location** en **Join attributes by location**, kan de gebruiker precies de te gebruiken ruimtelijke operator selecteren.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Mogelijkheid: Nieuwe algoritmen
Een aantal nieuwe algoritmen zijn toegevoegd aan het framework Processing:
-  algoritme **Regular points** (adresseert #5953)
- algoritme **Symetrical difference** (adresseert #5953)
- algoritme **Vector split** (adresseert #5953)
- algoritme **Vector grid** (adresseert #5953)
- algoritme voor berekening **Hypsometric curves**
- **Split lines with lines**
- algoritme **Refactor fields** voor manipuleren van attributen

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programmeerbaarheid
### Mogelijkheid: Functionaliteit voor opmerkingen bij expressies toegevoegd
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Mogelijkheid: Aangepaste functiebewerker voor expressies
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Mogelijkheid: Ondersteuning voor Qt5
QGIS kan nu worden gebouwd met behulp van bibliotheken voor Qt5. Onthoud dat momenteel de meeste binaries nog steeds standaard Qt4 hebben.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Mogelijkheid: Bulk-laden van ruimtelijke index
In de API hebben we ondersteuning toegevoegd voor het in bulk laden van ruimtelijke index. Dit is een veel snellere manier van het initialiseren van ene ruimtelijke index. vanuit Python is het zo eenvoudig als:

`index = QgsSpatialIndex( layer.getFeatures() )`

Uit een eenvoudige test met 50K aan punten in een geheugenlaag:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

De boom voor de index zou in theorie ook beter moeten zijn geconstrueerd en zou kunnen resulteren in snellere acties voor opzoeken.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Mogelijkheid: Alleen het geselecteerde deel van een query in SQL uitvoeren
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Server
### Mogelijkheid: Python plug-ins voor server 
Ondersteuning van Python plug-ins voor QGIS server brengt de kracht van Python naar de kant van de server, hetgeen snelle en efficiënte ontwikkeling toestaat alsmede het uitrollen van nieuwe mogelijkheden.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Mogelijkheid: Ondersteuning voor laagstijlen
- QGIS Server ondersteund nu vooraf gedefinieerde laagstijlen in verzoeken GetMap
- QGIS Server ondersteunt nu meerdere stijlen in het verzoek GetStyles (zie gedeelte Symbologie hieronder)

### Mogelijkheid: Methode DescribeLayer aan WMS toegevoegd
**profiel Styled Layer Descriptor van de Web Map Service : DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Definiëren van een gebruikergedefinieerde stijl vereist informatie over de te symboliseren objecten, of ten minste hun type object/bedekking. Omdat gebruikergedefinieerde stijlen kunnen worden toegepast op ene benoemde laag, dient er een mechanisme te zijn waarmee een cliënt de informatie voor een type object/bedekking voor een benoemde laag kan verkrijgen. Dit is een ander voorbeeld van het overbruggen van het gat tussen de concepten van WMS voor lagen en stijlen en concepten van WFS/WCS zoals type object en bedekkingslaag. Een WMS kan, optioneel, het verzoek **DescribeLayer** ondersteunen om dit mogelijk te maken.

Van de methode DescribeLayer wordt gedacht dat het een betere benadering is dan het document voor de WMS-capabilities nog meer te belasten.

Voor elke benoemde laag zou de beschrijving moeten aangeven of het inderdaad is gebaseerd op gegevens van ene object en als dat zo is zou het de WFS/WCS moeten aangeven (door een voorvoegsel URL) en de typen object/bedekking. Onthoud dat dit perfect geldig is voor een benoemde laag om niet te beschrijven te zijn op deze manier.
## Symbologie
### Mogelijkheid: Type vulling voor rasterafbeelding
Dit nieuwe type symboollaag maakt het mogelijk polygonen te vullen met een (getegelde) rasterafbeelding.

Opties omvatten (gegevens gedefinieerde) bestandsnaam, doorzicht, grootte afbeelding (in pixels, mm of kaarteenheden), modus coördinaten (object of  weergave), en rotatie.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Mogelijkheid: Live renderer Heatmap
De nieuwe renderer voor Heatmap vectorlagen maakt het mogelijk live, dynamische heatmaps voor puntlagen te maken.

Opties omvatten het specificeren van de straal voor de heatmap in pixels, mm of kaarteenheden, keuze voor ene kleurenbalk, gewogen punten op veld, en een schuifbalk voor het selecteren van een wisselwerking tussen snelheid van renderen en kwaliteit.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Mogelijkheid: Meerdere stijlen per laag
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Mogelijkheid: Meer instellingen voor gegevens-gedefinieerde symbologie
De gebruikersinterface voor instellingen van gegevens-gedefinieerde symbologie is verbeterd - de optie gegevens-gedefinieerd is verplaatst tot naast elke voor gegevens te definiëren eigenschap (in overeenstemming met andere delen van QGIS zoals de eigenschappen voor labelen). Ook zijn vele nieuwe eigenschappen voor gegevens te definiëren gemaakt voor symbologie. Deze verbetering van de gebruikersinterface verschaft ook een manier om onmiddellijk te zien of een gegevens-gedefinieerde voorrang is gedefinieerd als ook eenvoudiger toegang tot gegevens-gedefinieerde instellingen.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Mogelijkheid: exporteren DXF: exporteren van markeringssymbool verbeterd
De functionaliteit exporteren voor bestanden van DXF is verbeterd, met betere trouw van de geëxporteerde markeringssymbolen aan de originele symbologie van QGIS.
### Mogelijkheid: Roteren van kaart in kaartvenster, verbeterde rotatie in Printvormgeving
Deze uitgave omvat voorlopige ondersteuning voor het roteren in het kaartvenster. U kunt het kaartvenster roteren met behulp van het nieuwe widget voor roteren in de Statusbalk. Ondersteuning voor roteren is ook uitgebreid naar de Printvormgeving zodat  het labelen en symbologie etc. juist afhandelt.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Gebruikersinterface
### Mogelijkheid: Verbeterde/consistente selectie van projectie
Alle dialoogvensters gebruiken nu een consistent widget voor selectie van projectie, wat het snel selecteren van recent gebruikte en standaard project-/QGIS-projecties.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
