---
HasBanner: false
draft: false
releaseDate: 20-02-2015
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.8{#changelog28 }
Datum uitgave 20-02-2015

Dit is het log met wijzigingen voor de volgende uitgave van QGIS - versie 2.8 \' Wien\'. Wien is Duits voor \'Wenen\' - gastheer voor de ontmoeting van de ontwikkelaars in november 2009 en opnieuw in maart 2014.

**Long Term Release**

Dit is een speciale uitgave omdat het is aangewezen als een \'LTR\' (Long Term Release). LTR-uitgaven zullen worden ondersteund met achterwaarts ondersteunende probleemoplossingen voor één jaar, en zullen een permanente bevriezingsfase hebben (d.i. er zullen geen nieuwe mogelijkheden worden toegevoegd, alleen probleemoplossingen en kleinere updates).

Het doel van LTR-uitgaven is om een stabiel en minder vaak wijzigend platform te verschaffen voor bedrijven en organisaties die zich niet meer dan eenmaal per jaar willen bezighouden met het bijscholen van gebruikers, trainingsmateriaal etc.  Het succes van de LTR hangt heel veel van u, onze geliefde gebruikers, af, we hebben uw ondersteuning nodig om ons probleemoplossingen aan te reiken en er voor zorgend dat u in uw ondersteuningscontracten met verleners van ondersteuning specificeert dat probleemoplossingen die voor u worden toegepast ook worden toegepast op de tak van de LTR als ook op onze normale takken voor ontwikkeling.

Als een LTR belangrijk voor u is, overweeg dan ook directe ondersteuning voor het project QGIS, of moedig uw zakelijke dienstverlener aan om de LTR als basis te gebruiken voor uw zakelijke oplossing zodat iedereen kan profiteren van een stabiel platform dat doorlopend wordt verbeterd en verfijnd. Onthoud dat voor gebruikers en organisaties die graag de grenzen verkennen, onze viermaandelijkse uitgaven ongewijzigd door blijven gaan.

**Nieuwe mogelijkheden**

QGIS 2.8 is ook een speciale uitgave omdat het zoveel fantastische nieuwe mogelijkheden bevat, wijzigingen en verbeteringen om het het meest populaire vrije desktop GIS te maken, zelfs meer gevuld met mogelijkheden en nuttig.

Wanneer aan software nieuwe mogelijkheden worden toegevoegd, introduceren die de mogelijkheid tot het ontstaan van nieuwe problemen - als u in deze uitgave nieuwe problemen tegenkomt, vul dan een ticket in [op de QGIS Bug Tracker](http://hub.qgis.org).

**Dankwoord**

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOUDEN Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- ZILVEREN sponsor: [Sourcepole AG, Zwitserland](http://www.sourcepole.com/)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- ZILVEREN sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZEN Sponsor: [GIS3W, Italië](http://www.gis3w.it/)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de
- BRONZEN sponsor: [www.openrunner.com, Frankrijk](http://www.openrunner.com)
- BRONZEN sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Duitsland](http://www.gkg-kassel.de/)
- BRONZEN sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZEN sponsor: [Urbsol, Australië](http://www.urbsol.com.au/)
- BRONZEN sponsor: [MappingGIS, Spanje](http://www.mappinggis.com/)
- BRONZEN sponsor: [Lutra Consulting, VK](http://www.lutraconsulting.co.uk/)
- BRONZEN sponsor: [ADLARES GmbH, Duitsland](http://www.adlares.com/)
- BRONZEN sponsor: [Avioportolano Italia, Italië](http://www.avioportolano.it/)
- BRONZEN Sponsor: [Faculteit voor Geologie, Geofysica en Milieubescherming, AGH, ​University of Science and Technology, Polen](http://www.wggios.agh.edu.pl/en)

Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors). Als u een officiële sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren.

Als u geniet van het gebruiken van QGIS, overweeg dan eens om een donatie te geven om het project te ondersteunen - ofwel [financieel](https://qgis.org/nl/site/getinvolved/donations.html) of van [uw tijd en vaardigheden](https://qgis.org/nl/site/getinvolved/index.html)! Tenslotte willen we even stilstaan om u aan te moedigen bij te dragen aan een [speciale campagne](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) door een van onze ontwikkelaars van QGIS om een werkende testsuite voor QGIS te krijgen. Zodat we onze processen voor het verbeteren van de kwaliteit kunnen verbeteren en u de best mogelijke uitgaven kunnen geven.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Expressies invoeren in draaivelden
Bij het bewerken van attributen in de **attributentabel of formulieren**, kunt u nu direct expressies invoeren in draaivelden, bijv. `5 * 2.5` en zij zullen automatisch worden geëvalueerd.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Mogelijkheid: Favoriete plaatsen kunnen worden geïmporteerd/geëxporteerd
Het is nu mogelijk om uw Favoriete plaatsen naar/vanuit een bestand op te slaan/te laden. Dit maakt het eenvoudiger om locaties van Favoriete plaatsen te delen, of ze tussen computers uit te wisselen.

**Deze mogelijkheid werd ontwikkeld door:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Mogelijkheid: Verbeteringen aan expressies
- **Delen van een integer produceert een double indien vereist**: Eerder zou het delen van twee integers in een expressie altijd resulteren in een waarde integer, d.i. `5 / 2 = 2`. Nu zal het resultaat, indien vereist, altijd een double zijn, dus `5 / 2 = 2.5`, wat veel meer wordt verwacht door gebruikers. Een nieuwe operator voor het delen van integer - `//` is toegevoegd om het oude gedrag na te bootsen, d.i. `5 // 2 = 2`.
- **Nieuwe functie \'if()\'**: Er is nu een nieuwe expressie `if(cond, true, false)`
- **Trage evaluatie van expressies**
- **Geometrie verkrijgen en transformeren toegevoegd**: Deze nieuwe sleutelwoorden kunnen worden gebruikt met `getFeature` voor enkele testen van geometrie zoals intersects, crosses, contains, etc.
- `geometry` - geeft de geometrie van het object terug
- `transform` - geeft de getransformeerde geometrie terug

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Mogelijkheid: Doorlopend framework voor testen en verbeteringen in QA
In onze doorlopende zoektocht naar het verbeteren van de stabiliteit en kwaliteit van QGIS, wordt elke bijdrage nu getest tegen een groeiende testsuite om regressies automatisch te identificeren. In de afbeelding rechts ziet u in de lijst met inkomende pull requests op onze pagina van GitHub, dat ze nu automatisch geannoteerd worden met een vinkje of een kruis. Gebaseerd op het feit of onze testsuite al dan niet succesvol werd uitgevoerd op [Travis.ci](https://travis-ci.org/qgis/QGIS) toen het pull request werd gemaakt of werd bijgewerkt.

We voeren nu ook regelmatig Coverity-scans uit op de codebasis van QGIS. Als resultaat hiervan hebben we meer dan 1000 gevlagde problemen geïdentificeerd en opgelost, inclusief lekken in het geheugen en potentiële crashes. QGIS heeft een dichtheid voor defecten van 0.01 waar het gemiddelde, voor programma's met een soortgelijke grootte, ongeveer 1.0 is.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Analyse-gereedschappen
### Mogelijkheid: Verbeteringen aan dialoogvenster Meten
Het gereedschap voor meten is verbeterd zodat u nu kunt kiezen welke eenheden in het dialoogvenster meten zouden moeten worden gebruikt. Er is ook een nieuw gedeelte informatie in het dialoogvenster dat weergeeft welke instellingen worden gebruikt gedurende de berekeningen van de metingen.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Browser
### Meer responderende browser
In de QGIS Browser worden items nu in hun eigen threads uitgevouwen, wat de tijd voor laden van de browser versnelt en de browser meer reagerend maakt. Navigeren door bronnen van PostGIS is nu veel sneller in de browser. De geanimeerde schermafbeelding rechts (klik op de afbeelding om de animatie te zien) geeft het laden van twee trage servers van WMS parallel weer. De status van de browser (uitbreiding boom) wordt hersteld bij opstarten.

**Deze mogelijkheid werd ontwikkeld door:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor contextuele afbeeldingen van legenda's van WMS
Als uw server van WMS contextuele legenda's ondersteunt, kunt u daar nu ook in QGIS gebruik van maken. Contextuele legenda's zijn verzoeken getLegendGraphic die alleen de relevante legenda voor uw huidige bereik van de weergave teruggeven, en dus geen items voor de legenda bevatten voor dingen die u in de huidige kaart niet kunt zien.

**Dit werd mogelijk gemaakt door:** [Regio Toscane](http://www.regione.toscana.it/)

**Deze mogelijkheid werd ontwikkeld door:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gegevensbeheer
### Mogelijkheid: Aangepast voorvoegsel voor joins
U kunt nu een aangepast voorvoegsel definiëren in het beheer van joins in het dialoogvenster Laag-eigenschappen. Bij het gebruiken van een voorvoegsel, zal de attributentabel nu namen van samengevoegde attributen weergeven met het voorvoegsel van uw voorkeur.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Mogelijkheid: Ondersteuning voor het maken van tijdelijke geheugenlagen
Deze uitgave voegt ondersteuning toe voor het maken van nieuwe tijdelijke tekenlagen binnen de bron van QGIS. Tekenlagen kunnen worden gemaakt via de menuoptie `Kaartlagen --> Laag maken --> Nieuwe tijdelijke tekenlaag`.

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

**Dit werd mogelijk gemaakt door:** [Tracks for Africa](http://tracks4africa.com/)

**Deze mogelijkheid werd ontwikkeld door:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in samenwerking met [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Mogelijkheid: Verbeteringen voor snappen
Er is een nieuwe modus voor snappen : **snappen aan alle lagen** wat het inschakelen van snappen tussen alle lagen sneller maakt. Ook is de onderliggende architectuur voor snappen in QGIS bijgewerkt, wat snappen op grotere projecten sneller maakt en de precisie waarmee snappen wordt uitgevoerd verbetert. ​Er is ook minder verwarring tussen toleranties voor snappen in kaarteenheden of laageenheden, dus de verwachte toleranties van 1 meter worden geen toleranties van 1 graad zonder dat u dat weet.

**Dit werd mogelijk gemaakt door:** [Stad Vevey, SITNyon](http://www.vevey.ch/) en [QGIS gebruikersgroep Zwitserland](http://www.qgis.ch/)

**Deze mogelijkheid werd ontwikkeld door:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Legenda van laag
### Mogelijkheid: Legenda van regelgebaseerde-renderer als een boom weergeven
Gevorderde gebruikers die gebruikmaken van het systeem van Regelgebaseerde-renderer in QGIS zullen blij zijn te zien dat de regels nu worden gepresenteerd als een boom in de Legenda. Beter nog, elke knoop in de **boom** kan individueel worden **in-/uitgeschakeld** wat grote flexibiliteit verschaft voor hoe sublagen worden gerenderd in uw kaart.

**Dit werd mogelijk gemaakt door:** [SIGE](http://www.sige.ch/)

**Deze mogelijkheid werd ontwikkeld door:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in samenwerking met [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen GUI Printvormgeving
- Menuoptie voor weergave om **begrenzingsvakken te verbergen**. Dit stelt gebruikers in staat de begrenzingsvakken van in de compositie geselecteerde items te verbergen. Het is een handige mogelijkheid voor het toestaan van interactie met items, terwijl de voorvertoning exact laat zien hoe ze eruit komen te zien wanneer de compositie wordt geëxporteerd, zonder dat grote blokken de weergave blokkeren.
- **Modus Volledig scherm voor Printvormgeving**
- Optie om **de weergave van panelen in/uit te schakelen** in Printvormgeving, beschikbaar in zowel het `menu Beeld`, met behulp van de sneltoets `F10` en door op `Tab` te drukken wanneer het kaartvenster in printvormgeving is geselecteerd. Het is nuttig voor het maximaliseren van de ruimte bij het plannen van een lay-out voor een kaart.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Mogelijkheid: Verbeteringen voor raster
In de Printvormgeving heeft u nu fijnere controle over de weergave van frame en annotatie. Eerder zou, voor geroteerde kaarten of opnieuw geprojecteerde rasters, de Printvormgeving alle coördinaten voor elke zijde van de kaart tekenen. Dit resulteerde in een weergave van mix van latitude/Y- en longitude/X-coördinaten op één kant. Nu kunt u beheren of u alle coördinaten, alleen latitude of alleen longitude wilt voor elke kant van het kaartframe. Soortgelijke opties zijn ook toegevoegd voor het beheren van hoe een frame voor het kaartraster zal worden opgedeeld.

Nieuwe verticale aflopende richting voor annotaties. Deze wijziging voegt een nieuwe modus aflopende verticale richting toe voor annotaties in het kaartraster. Eerder werd alleen oplopende tekst ondersteund voor verticale annotaties.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Mogelijkheid: Marges voor items Label
- U kunt nu zowel horizontale als verticale **marges voor label**-items beheren. Eerder zou alleen één enkele instelling voor de marge gelden voor zowel de horizontale als de verticale marges. Deze wijziging maakt het voor gebruikers mogelijk verschillende horizontale en verticale marges te specificeren.
- U kunt nu negatieve marges specificeren voor items Label, **toestaan dat tekst enigszins buiten de grenzen van het item label wordt getekend**. Dit is gewenst voor het uitlijnen van items Label met andere items terwijl een optische uitlijning van de marge voor het type label wordt toegestaan.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Plug-ins
### Mogelijkheid: Verbeteringen voor console Python
U kunt nu scripts voor Python in het venster van QGIS slepen en laten vallen en zij zullen automatisch worden uitgevoerd. We hebben ook een pictogram voor de werkbalk toegevoegd aan de werkbalk Plug-ins en een sneltoets ( `Ctrl-Alt-P` ) voor snelle toegang tot de console voor Python.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Processing
### Mogelijkheid: Nieuw type parameter geometrisch predikaat
met dit nieuwe type parameter, gebruikt in de algoritmen **Select by location, Extract by location** en **Join attributes by location**, kan de gebruiker precies de te gebruiken ruimtelijke operator selecteren.

**Dit werd mogelijk gemaakt door:** [Franse Ministerie van Ecologie, Duurzame ontwikkeling en Energie](http://www.developpement-durable.gouv.fr/)

**Deze mogelijkheid werd ontwikkeld door:** [Camptocamp](http://www.camptocamp.com)

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
Opmerkingen kunnen nu aan expressies worden toegevoegd met behulp van een SQL-stijl voorvoegsel `--`.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Mogelijkheid: Aangepaste functiebewerker voor expressies
U kunt nu aangepaste functies voor expressies definiëren in het widget Expressie. Bekijk [deze blogpost](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) voor meer details.

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
In de SQL-bewerker van DB Manager is het nu mogelijk om een deel van de SQL te accentueren en alleen dat gedeelte zal dan worden uitgevoerd als u drukt op `F5` of klikt op de knop `Uitvoeren`

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Server
### Mogelijkheid: Python plug-ins voor server 
Ondersteuning van Python plug-ins voor QGIS server brengt de kracht van Python naar de kant van de server, hetgeen snelle en efficiënte ontwikkeling toestaat alsmede het uitrollen van nieuwe mogelijkheden.

**Deze mogelijkheid werd ontwikkeld door:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
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
Het is nu mogelijk om meerdere stijlen voor ene laag in te stellen en dan eenvoudig daartussen te schakelen. Deze functionaliteit is beschikbaar in het `contextmenu Legenda --> submenu Stijlen` waar het mogelijk is stijlen toe te voegen/te verwijderen en daar snel tussen te schakelen. Sets van lagen onthouden stijlen, en verschillende stijlen kunnen ook worden toegepast op individuele kaartitems in Printvormgeving. De gedefinieerde meerdere stijlen zijn ook beschikbaar als het project wordt gebruikt via QGIS Server als een laag voor WMS. Voor meer informatie hierover, zie ook deze [blogpost](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**Dit werd mogelijk gemaakt door:** [Regio Toscane](http://www.regione.toscana.it/)

**Deze mogelijkheid werd ontwikkeld door:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Mogelijkheid: Meer instellingen voor gegevens-gedefinieerde symbologie
De gebruikersinterface voor instellingen van gegevens-gedefinieerde symbologie is verbeterd - de optie gegevens-gedefinieerd is verplaatst tot naast elke voor gegevens te definiëren eigenschap (in overeenstemming met andere delen van QGIS zoals de eigenschappen voor labelen). Ook zijn vele nieuwe eigenschappen voor gegevens te definiëren gemaakt voor symbologie. Deze verbetering van de gebruikersinterface verschaft ook een manier om onmiddellijk te zien of een gegevens-gedefinieerde voorrang is gedefinieerd als ook eenvoudiger toegang tot gegevens-gedefinieerde instellingen.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Mogelijkheid: exporteren DXF: exporteren van markeringssymbool verbeterd
De functionaliteit exporteren voor bestanden van DXF is verbeterd, met betere trouw van de geëxporteerde markeringssymbolen aan de originele symbologie van QGIS.
### Mogelijkheid: Roteren van kaart in kaartvenster, verbeterde rotatie in Printvormgeving
Deze uitgave omvat voorlopige ondersteuning voor het roteren in het kaartvenster. U kunt het kaartvenster roteren met behulp van het nieuwe widget voor roteren in de Statusbalk. Ondersteuning voor roteren is ook uitgebreid naar de Printvormgeving zodat  het labelen en symbologie etc. juist afhandelt.

**Dit werd mogelijk gemaakt door:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**Deze mogelijkheid werd ontwikkeld door:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Gebruikersinterface
### Mogelijkheid: Verbeterde/consistente selectie van projectie
Alle dialoogvensters gebruiken nu een consistent widget voor selectie van projectie, wat het snel selecteren van recent gebruikte en standaard project-/QGIS-projecties.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
