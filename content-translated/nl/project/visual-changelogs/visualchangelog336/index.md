---
HasBanner: false
draft: false
releaseDate: 23-02-2024
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.36
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.36{#changelog336 }
![](images/projects/fc93f461b927dd4960936f3391cf00321f9552cc.png)

Datum uitgave: 23-02-2024

Het project QGIS gaat door met het verleggen van grenzen van open-bron georuimtelijke technologie, zoals weer blijkt uit de uitgave van QGIS 3.36. Het project gaat door met het gebruikers in staat stellen nog betere ruimtelijke beslissingen te nemen met nieuwe mogelijkheden en verbeteringen, en introduceert een nieuwe brongegevensprovider voor OGC SensorThings API databronnen.

Over de naam van onze uitgave: Windsor and Maidenhead borough council was een van de eerste lokale autoriteiten in het VK om over te gaan op QGIS (met versie 1.8!) in 2010/11. Het was in Windsor and Maidenhead dat Simon Miles en Matt Travis de VK QGIS-gebruikersgroep begonnen. Het was zelfs de gastheer van de eerste bijeenkomst van de VK QGIS gebruikersgroep ooit. Windsor and Maidenhead heeft ook veel financieel bijgedragen aan vele QGIS plug-ins en was ook Bronzen sponsor.

Naast de fantastische nieuwe mogelijkheden die aan deze uitgave zijn toegevoegd, is er een nieuwe "Movie Mode" voor Tijdbeheer die het maken van geanimeerde kaarten mogelijk maakt. Deze uitgave brengt ook nieuwe mogelijkheden voor kaarttips (op Desktop en Server) en verbeteringen aan de steeds groeiende collectie 3D-functionaliteiten, die gebruikers de mogelijkheden geven voordeel te halen uit gevorderde gegevenstypen, zoals Mazen, Puntenwolken en 3D-tegels.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=q7O819lFKc4)

[![](https://img.youtube.com/vi/WS9W1fo9Aso/0.jpg)](https://www.youtube.com/watch?v=WS9W1fo9Aso)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een heel groot bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Belangrijke wijzigingen
### Mogelijkheid: OTB-provider voor Processing verwijderd
**Wegens gebrek aan doorlopend onderhoud hebben we de moeilijke beslissing moeten nemen om de provider Orfeo ToolBox (OTB) voor Processing uit QGIS te verwijderen. Alle gebruikers, plug-ins of scripts die deze functionaliteit gebruikten, moeten dat overeenkomstig aanpassen.**

Gemotiveerde leden uit de gemeenschap van QGIS worden aangemoedigd een 3e partij door de gemeenschap te onderhouden plug-in te maken om ondersteuning voor OTB te herstellen.
## Tijdbeheer
### Mogelijkheid: "Modus Film" voor Tijdbeheer
We hebben een nagelnieuwe modus "Film" toegevoegd aan Tijdbeheer. Deze modus is ontworpen om het maken van geanimeerde films uit kaarten mogelijk te maken. Anders dan andere modi in Tijdbeheer wordt geen op tijd gebaseerd filteren van gegevens uitgevoerd in de modus Film.

In modus Film kunt u het totale aantal frames voor uw film instellen en de animatie frame na frame doorgaan voor dat aantal frames. Het verhoogt de instelling voor het frame van de huidige kaart (en de expressievariabele @frame_number) met elke stap. U kunt dan geanimeerde symbolen gebruiken, of uw symbologie wijzigen met de expressievariabele @frame_number, om dynamische, geanimeerde kaarten te maken.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Gebruikersinterface
### Mogelijkheid: Aangepaste laageigenschappen in de laageigenschappen van de kaart
We hebben een weergave van aangepaste laageigenschappen voor kaartlagen toegevoegd op de tab Informatie van de Laageigenschappen. Wat het voor gebruikers gemakkelijker maakt eventuele extra metadata en eigenschappen te bekijken die zijn verbonden met hun kaartlagen.

![](images/entries/393384efc22e1add7f41288a80b6e4bbd681b68d.webp)

Deze mogelijkheid werd ontwikkeld door [Jorge Alexandre Delesderrier da Silva](https://github.com/jadsilva)
### Mogelijkheid: Gemakkelijker opslaan project en afbeelding
In 3.36 hebben we QGIS wat slimmer gemaakt voor de manier waarop dat het opslaan van projecten en afbeeldingen afhandelt. Het type project (.qgz, .qgs) of afbeeldingsindeling (.png, .jpg, .tif, etc.) wordt nu (standaard) bepaald bij elke bestandsextensie die u in het dialoogvenster Opslaan intypt. Dat maakt een snellere ervaring voor de gebruiker mogelijk bij het wijzigen van de ene indeling naar een andere, omdat u niet vooraf expliciet een andere indeling hoeft in te stellen via het combinatievak voor de indeling!

![](images/entries/6585d31ab7870351c8b58c9bec57e36df50f3018.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin (OPENGIS.ch)](https://www.opengis.ch/)
## Symbologie
### Mogelijkheid: Hoogte afbeelding beheren voor rastervullingsymboollagen
We hebben een nieuwe instelling geïntroduceerd voor het symbooltype "rastervulling", die het voor u mogelijk maakt de breedte en hoogte van het vulpatroon onafhankelijk te beheren. (Eerder waren deze instellingen met elkaar verbonden). U kunt nu uitgerekte rastervullingen maken in horizontale of verticale richting, wat meer flexibiliteit geeft voor het maken van uw aangepaste symbolen.

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuw type symboollaag "gevulde lijn"
We hebben een nagelnieuw type lijnsymbool toegevoegd voor de "gevulde lijnen". Het lijkt veel op wat het oudere symbooltype "Gevulde markering" biedt voor markeringssymbolen. Deze optie zal lijnen renderen met **elk** vullingssymbool van QGIS. Dat betekent dat u nu lijnen kunt renderen die zijn gevuld met kleurverlopen, lijnarceringen, rastervullingen, en nog veel meer!

![](images/entries/5117e44fbe7ec55216b8fd1242c2721a78032dc0.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Mazen
### Mogelijkheid: Labelen van lagen met mazen
In 3.36 hebben we ondersteuning voor het labelen van lagen met mazen toegevoegd. Labels kunnen worden toegepast op punten van mazen, of zijden van mazen, en u kunt voordeel halen uit alle opties voor gevorderde opmaak en instellingen voor uiterlijk die beschikbaar zijn in het dialoogvenster Laageigenschappen en het paneel Laag opmaken. In-/uitschakelen van lagen met mazen kan ook handig worden gedaan met het contextmenu van het paneel Lagen.

![](images/entries/42674b6a42180aa567bf76ec53db917e191f4595.webp)

Dit werd mogelijk gemaakt door GÖTEBORGS STAD

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## 3D-objecten
### Mogelijkheid: Data-bepaald kleurbeheer voor eenvoudig 3D-lijn renderen
U kunt nu een data-bepaalde, dynamische kleur instellen voor 3D-lijnen die worden gerenderd met de optie "Renderen als eenvoudige 3D-lijnen". Dit is extreem nuttig voor het visualiseren van objecten lijn in 3D. Bijvoorbeeld het weergeven van ondergrondse pijpleidingen in verschillende kleuren, gebaseerd op hun classificaties.

![](images/entries/609eca4c0ebaa0b4dbf12d0dc4f4fae3fab5dc29.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeterd materiaal "Phong" en belichting
De Phong-schaduwmaker wordt gebruikt als standaardmateriaal voor het weergeven van vectorobjecten in 3D-weergaven van QGIS. Voor 3.36 is deze schaduwmaker verbeterd om de parameters ambient en shininess beter af te handelen. Aanvullend hebben we ervoor gezorgd dat exact dezelfde schaduw zal worden toegepast, ongeacht het onderliggende type geometrie (punten, lijnen of polygonen). Ook ongeacht welke data-bepaalde gedefinieerde aangepaste kleuren gebruikt worden. Dat geeft gebruikers veel beter te voorspellen en gemakkelijk te configureren materiaal voor hun 3D-weergaven.

Voor gemakkelijker configureren van beter uitziende materialen hebben we ook nieuwe besturingselementen voor het aanpassen van de bijdragen voor omgevingslicht, diffuus licht en gespiegeld licht.

![](images/entries/267232fa32fc1510a5c27c0364451699c1f415a1.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: "Fysiek gebaseerd" metaal ruw materiaal
Voor nog mooiere 3D-kaarten hebben we een nieuwe materiaalkeuze toegevoegd voor "fysiek gebaseerd renderen" (PBR) materiaal. Dit materiaal laat u de basiskleur van het oppervlak definiëren, en hoe "metaal" en "ruw" het eruit zou moeten zien. Dit materiaal is eenvoudig te configureren en er zijn goede resultaten mee te behalen. Het wordt verwacht het standaardmateriaal in een toekomstige uitgave van QGIS te worden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Definiëren van 3D-scènebereiken in 2D-kaarten
We hebben een actie voor een sneltoets toegevoegd aan de werkbalk voor de 3D-weergave, die het voor gebruikers mogelijk maakt om snel een begrensd bereik voor de scène op een 2D-kaart te zetten.

![](images/entries/41d95a9ad7be81ca3c8dd95a47674b356d625f1b.gif)

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Puntenwolken
### Mogelijkheid: Overschrijven grootte voor classificaties puntenwolken
In QGIS 3.36 kunt u nu de standaardgrootte voor punten van afzonderlijke categorieën in zowel 2D- als 3D-weergaven overschrijven.

Een nieuwe kolom "Grootte" werd toegevoegd aan de widget met categorieën, die blanco zal zijn als een categorie de standaard puntgrootte erft, maar u in staat stelt om handmatig de grootte te specificeren met numerieke invoer. Instellen van de waarde Grootte op 0 voor een categorie zal die terugzetten naar de standaard puntgrootte voor die laag.

U kunt ook het contextmenu rechtsklikken gebruiken om de puntgrootte in één keer in te stellen voor meerdere geselecteerde categorieën tegelijk.

![](images/entries/1be03fcdc04fd2f382222b9de4c41a8528090b0d.webp)

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Puntenwolken renderen als oppervlakte in 2D-kaarten
We hebben een nieuwe optie toegevoegd voor opmaken in 2D van puntenwolken voor "Renderen als oppervlakte (trianguleren)".

Indien ingeschakeld zal QGIS een directe Delaunay-triangulatie uitvoeren voor de punten in de huidige kaartweergave en de laag renderen als gevulde driehoeken, in plaats van als individuele punten. De kleur van elk punt wordt behouden en geïnterpoleerd in elke driehoek.

Globale schauw voor de kaart wordt ook ondersteund met de nieuwe optie, zodat, indien ingeschakeld, de hoogte van punten wordt behouden en een gerasteriseerde instantie van de driehoeken met geïnterpoleerde hoogten kan worden gegeven aan de hoogtekaart.

Als "Renderen als oppervlakte" is ingeschakeld, wordt de tekenvolgorde genegeerd en alle invoerpunten nemen deel aan de triangulatie.

We hebben ook een optie toegevoegd om grote driehoeken te filteren (gebaseerd op de maximumlengte van een rand van een driehoek), wat het mogelijk maakt gaten in gegevens te visualiseren, maar het 2D-renderen verschaft alleen filteren dat is gebaseerd op de horizontale lengte van driehoeken.

Bekijk zeker ook het [Pull Request](https://github.com/qgis/QGIS/pull/55332) voor de mogelijkheid op GitHub voor een voorbeeld van de nieuwe functionaliteit in verschillend emodi en contexten.

![](images/entries/cc7d5061c43b895106162fc314cbd6712ee8256c.webp)

Dit werd mogelijk gemaakt door National Resources Canada

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Sneller renderen van puntenwolk door cachen van gedecodeerde gegevensblokken
Wilt u sneller renderen van puntenwolken? Wel, QGIS ondersteunt nu het sneller renderen van puntenwolken, door een cache te gebruiken voor het opslaan van knopen die al zijn gedecodeerd.

Deze optimalisatie vermijdt het meerdere keren decomprimeren van dezelfde knopen bij verschuiven of zoomen, speciaal bij het gebruiken van gecomprimeerde databronnen, zoals LAZ-opgemaakte bestanden.

(Een vaste grootte voor de cache van 200 MB wordt gebruikt en gedeeld over alle lagen voor putenwolken en kaartvensters (2D, 3D en profielplots).)

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Behouden van metadata gedurende conversie naar COPC
Het programma Untwine (dat verantwoordelijk is voor conversies van puntenwolken naar de indeling COPC in QGIS) is bijgewerkt naar versie 1.3. Dat omvat verschillende reparaties en kleine verbeteringen. Naast de verbeteringen behoudt de conversie naar COPC nu de volgende metadata uit bestanden LAS/LAZ:
- Globale codering
- Tijd maken (jaar+dag)
- XYZ-verschuiving

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Verbeterde afhandeling van vlaggen voor classificatie
Bestanden LAS/LAZ zouden vier vlaggen voor elk punt kunnen bevatten (synthetic, key-point, withheld, overlap). In oudere uitgaven van QGIS werden die allemaal weergegeven in `ClassificationFlags` als een gecombineerde enkele waarde. Dat is niet praktisch als een gebruiker een van die vlaggen nodig heeft om te filteren of om te visualiseren.

Voor versie 3.36 hebben we die dingen opnieuw bewerkt, zodat deze vlaggen beschikbaar zijn als afzonderlijke attributen. Zowel voor visualisatie (bijv. met de renderer Classificatie) en voor filteren in expressies. In aansluiting daarop hebben we het oudere attribuut `ClassificationFlags` verwijderd.

Dit werd mogelijk gemaakt door National Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Expressies
### Mogelijkheid: Alias van minimum/maximum voor min/max voor Samenvoegen
We hebben enkele nieuwe aliassen voor argumenten toegevoegd aan de expressiefuncties voor samenvoegen, zodat "minimum" en "maximum" mogen worden gebruikt, in plaats van "min" en "max" voor deze functies.

![](images/entries/7f06f7f34b8a3fb756e8a982bb734d0439eadbdd.webp)

Deze mogelijkheid werd ontwikkeld door [Harrissou Sant-anna](https://github.com/DelazJ)
### Feature: @counter variable for array_foreach
We hebben een nieuwe variabele "@counter" toegevoegd aan de expressiefunctie `array_foreach`. Naast andere dingen laat dit u waarden combineren over meerdere arrayvelden.

Voorbeeld:

`array_foreach( "field_1", @element || ' ' || "field_2"[@counter] )`

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
### Mogelijkheid: Verbeterd invoeren expressie
Om QGIS 3.36 nog gebruiksvriendelijker te maken, hebben we het gedrag voor "Expressie invoeren/bewerken" aangepast. Nu,
- Als enige tekst is geselecteerd en uw selectie is binnen een expressie geschreven (d.i. tussen "[%" en "%]"), zal de expressiebewerker de gehele expressie selecteren
- Als geen tekst is geselecteerd en uw cursor staat in een expressie, wordt de hele expressie geselecteerd
- Anders zal de expressiebewerker openen met uw bestaande selectie.

Aanvullend hebben we een nieuwe knop "Expressie invoeren/bewerken" toegevoegd aan de tab Tonen (Kaarttips inschakelen) van de Laageigenschappen.

Dit nieuwe gedrag voor expressies bewerken is ook van toepassing op labels van Afdruklay-out, titels en decoraties Copyright, en ook op items van Annotatie.

![](images/entries/47a92c468b14da4ef7fc15ad131e52bb3ee4e477.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Gegevensbeheer
### Mogelijkheid: Selectie wisselen in het venster Kolommen beheren
We hebben een knop Selectie wisselen in het venster Kolommen beheren toegevoegd om u in staat te stellen gegevenssets met een grote hoeveelheid velden te beheren.

De nieuwe knop Selectie wisselen (alsook de knoppen Alles verbergen of Alles weergeven) zal alleen verschijnen als er meer dan 5 velden in een laag staan.

![](images/entries/d42005a9561cdc035cfa20f034b7a33fc9829522.gif)

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/Poulpator)
## Processing
### Feature: vlag --skip-loading-plugins voor qgis_process
Het programma voor de opdrachtregel `qgis_process` heeft baat bij een nieuw argument `--skip-loading-plugins`. Indien gespecificeerd kan dit resulteren in snellere uitvoertijden voor opdrachten als `qgis_process plugins`, die nu de geïnstalleerde plug-ins kan vermelden \*\*zonder\*\* ze te laden.

Dit werd mogelijk gemaakt door [Research Institute for Nature and Forest (INBO)](http://www.inbo.be/en)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Klik om uitvoerpaden te openen in logs van Processing
Een supernuttige nieuwe sneltoets die we aan 3.36 hebben toegevoegd, is dat eventuele uitvoerpaden (zoals bestand, map, of HTML-uitvoer) in het log van Processing nu aan te klikken zijn. Wat u in staat stelt om de betreffende map direct te openen en het gemaakte bestand vooraf te selecteren!

![](images/entries/52699edf93f7fb8710fe715ccc5482ac2f299c9c.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Vector bedekkingsalgoritmes
QGIS 3.36 introduceert een aantal nieuwe gereedschappen voor het werken met vectorbedekkingslagen. "Vectorbedekkingen" zijn polygonenlagen waarin verwacht wordt dat de objecten buren van elkaar zijn, zonder overlappingen of gaten, zoals lagen met administratieve grenzen. Deze nieuwe algoritmes voor Processing geven gereedschap weer voor het werken met bedekkingen, inclusief:
- **Bedekking valideren**: Dit algoritme analyseert een bedekking om plaatsen te zoeken waar niet wordt voldaan aan de aanname van exact overeenkomende randen.
- **Bedekking vereenvoudigen**: Dit algoritme past een vereenvoudiging Visvalingam–Whyatt toe op de randen van een bedekking, terwijl een geldige bedekking wordt behouden (d.i. randen zullen elkaar niet kruisen of raken na het vereenvoudigen).
- **Bedekking samenvoegen**: Dit algoritme verschaft een enorm geoptimaliseerde benadering voor het verenigen van polygonen in een bedekkingslaag, vergeleken met de standaardgereedschappen Samenvoegen.

Deze nieuwe gereedschappen zijn afhankelijk van de functionaliteit van de GEOS-bibliotheek voor afhandeling van geometrie. Onze dank gaat uit naar de onderhouders van GEOS om dit werk mogelijk te maken!

![](images/entries/c9fa268bf003676d082860bdc8f8bfe53bee66d8.webp)

<div class="col-lg-8 col-md-offset-1">

</div>

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeterd exporteren van lagen naar DXF-algoritme
We hebben een aantal nieuwe parameters geïntroduceerd voor het algoritme "Lagen naar DXF exporteren", om overeen te komen met zijn tegenhanger die niet voor Processing is:
- Een parameter Bereik om de objecten te filteren die moeten worden geëxporteerd
- Een parameter Kaartthema om de symbologie van de laag te overschrijven bij exporteren

We hebben ook enkele tekortkomingen in het algoritme gerepareerd, inclusief het overslaan van lagen waarvan geen objecten werden geëxporteerd.

![](images/entries/c151ba5e35152faf79d23401181bf21da3f46bca.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep (QGIS-CH)](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin (OPENGIS.ch)](https://www.opengis.ch/)
### Mogelijkheid: Sneller opstarten provider GRASS
We hebben de backend van de provider GRASS voor Processing opnieuw bewerkt, wat helpt de tijdsperiode voor het opstarten van deze plug-in te verkleinen (speciaal op installaties van Windows!). Dit heeft specifiek voordelen voor de gebruikers van het gereedschap `qgis_process`. Zij zullen opmerkelijk snellere uitvoeringstijden zien voor dit gereedschap.

Dit werd mogelijk gemaakt door [Research Institute for Nature and Forest (INBO)](http://www.inbo.be/en)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Sneller opstarten qgis_process
For 3.36, we've substantially improved the startup speed of the `qgis_process` command. This was done by applying a variety of optimisations inside QGIS, such as lazy loading of the authentication and style library frameworks so that these frameworks are only initialised when required, and by reworking the logic for migrating user settings between different QGIS versions to avoid unnecessary work.

Together, these improvements have reduced `qgis_process` startup times from multiple seconds to less than one second!

Dit werd mogelijk gemaakt door [Research Institute for Nature and Forest (INBO)](http://www.inbo.be/en)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Opties voor toepassing en projecten
### Feature: "localhost" option for OAuth2 Redirects
Some OAuth2 providers, like Microsoft Sharepoint, require specific redirect hosts for security reasons. They may not accept the standard "http://127.0.0.1" redirect, but instead allow only "https://127.0.0.1" or "http://localhost".

To ensure compatibility with these providers without the complexity of setting up HTTPS, we added a new option to use "localhost" as the redirect host for OAuth2 authentication.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Serial port sensor baudrate selection
For 3.36 you can now customize the connection speed (baud rate) to use for serial port sensors. Previously, this parameter was hardcoded at 9600 baud, limiting compatibility with various sensor types, such as NMEA sensors requiring 4800 baud. You can now connect to a wider array of sensors by adjusting the baud rate to meet specific requirements.

![](images/entries/5c594b33da01255f2c3b2b126ee2221ff484fc6f.webp)

Deze mogelijkheid werd ontwikkeld door [Jorge Tornero](https://github.com/jtornero)
## Browser
### Feature: Open layers with Datasource Manager from browser
We've introduced a new option in the QGIS browser context menu for "Open with Datasource Manager...". This option is available for layers which use the OGR provider (including GPKG sources), GDAL provider (raster layers), and Spatialite layers. When activated, a dialog will open on the data source tab of the layer properties, with relevant field values prepopulated to open the layer directly in QGIS, which allows you to set more comprehensive file opening options directly from the browser.

This functionality brings with it the `ConfigureFromUri` method which has been developed for the Python and C++ APIs. This method will enable source selection widgets to open and configure the data source manager directly from a data source URI, allowing the development of more sophisticated data loading options such as within plugins and when using the Change Data Source utility.

![](images/entries/b4ae363066776c62fe90d2dd926089f7a764d37f.gif)

Dit werd mogelijk gemaakt door NOAA

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Gegevensproviders
### Feature: SensorThings Data Provider
For version 3.36 we've introduced a brand new core data provider for OGC SensorThings API data sources.

The [SensorThings API](https://docs.ogc.org/is/15-078r6/15-078r6.html) is an OGC specification for Internet of Things sensors which complements existing communication protocols within the IoT ecosystem.

This functionality was developed in line with [QEP 257](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/257) and introduces new panels within the QGIS Browser, Data Source Manager, and Layer Properties Source tab for users to configure connections to SensorThings data sources.

We've taken care to ensure that SensorThings data sources are loaded in the most optimised way possible, providing an streamlined, user-friendly way to load SensorThings data into your QGIS projects. This is just the beginning though, and we've more functionality and improvements planned for access to SensorThings sources in QGIS 3.38!

![](images/entries/3802b455a5bdad53b1c7b8e9a7877b3c5988106f.webp)

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en), French PEPR OneWater - Eau Bien Commun ([https://www.onewater.fr/en](https://www.onewater.fr/en), ANR-22-PEXO-0009, onder het Future Program France 2030) en [Water4All Partnership](https://www.water4all-partnership.eu/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Support for WFS documents with complex feature schemas
We enhanced the WFS Provider to add support for complex feature schemas. The implementation exposes properties of complex WFS types as JSON content, converted from their original XML representations.

For more details, see the [QGIS Enhancement Proposal](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/277).

![](images/entries/587b31f23c77cdbd1589932f716759d3c2d3c015.webp)

Dit werd mogelijk gemaakt door [Duitse QGIS gebruikersgroep](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
## QGIS Server
### Feature: WMS GetMap in PDF Format
QGIS Server will now support responses in PDF format for GetMap requests.

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Feature: QGIS Server Properties Tab for Vector Tile Layers
The Layer Properties Dialog for Vector Tile layers will now include a section for editing the QGIS Server layer settings, providing the ability to configure layer-specific settings such as shortname, abstract, and other metadata.

![](images/entries/4dd2ce2af31695f8e917b037c7dfcaaa798dd575.webp)

Deze mogelijkheid werd ontwikkeld door [Sandro Mani](https://github.com/manisandro)
### Feature: GetLegendGraphics JSON rule
We've added a new `SHOWRULEDETAILS` parameter for WMS services, which will append a **rule** item in the legend entry. The rule describes the filter expression used on the respective layer when performing a `GetLegendGraphic` request using the JSON format option.

For example, the request:

`text GET /?SERVICE=WMS&VERSION=1.30&REQUEST=GetLegendGraphic&LAYERS=layer1&FORMAT=application/json&SHOWRULEDETAILS=1`

Will return the JSON response which includes a `rule` field when appropriate:

`json `

Dit werd mogelijk gemaakt door Kristianstadt

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add maptip for raster layer GetFeatureInfo
Maptip support was added for raster layer GetFeatureInfo responses, when requesting with parameter `WITH_MAPTIP=TRUE`. This matches the existing behavior which was in place for vector layers.

In this context, the variable `layer_cursor_point` holds the GetFeatureInfo position, so that maptips which are working in QGIS desktop are working also with QGIS Server GetFeatureInfo.

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
### Feature: WMS parameter to request only maptip for HTML feature info responses
We added a new value `HTML_FI_ONLY_MAPTIP` for the existing WMS vendor parameter `WITH_MAPTIP`.

If set, the feature info HTML response includes only the maptip, which gives full control over the HTML response using e.g. the built-in maptip editor which has a nice preview.

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
### Feature: Option to skip "name" attribute for groups in WMS GetCapabilities
We've added a new project level setting to **Skip name attribute for groups**. This is disabled by default, but enabling it allows you to exclude group names from a GetCapabilities response on a WMS request. This prevents name duplication in instances where a layer and group share the same name, whilst preserving the group element and bringing the QGIS Server capabilities more in line with the OGC WMS Specification.

Bijvoorbeeld:

`text <Layer queryable="1"> <Name>layer_name</Name> <--- this will be skipped when option is enabled <Title>Human readable name</Title>`

Deze mogelijkheid werd ontwikkeld door [Tomas Straupis](https://github.com/tomass)
## Plug-ins
### Feature: Use active layer when importing vector data with DB Manager
When importing vector data in the DB Manager core plugin, the "Input" combo box, which is populated with all the vector data in the layer tree, is now automatically set to the active layer whenever possible. This small change makes it much more user-friendly, especially when working with large and complex projects!

![](images/entries/1c69e30e80b5ef71d5dec8a3c6b4854f191f22cc.webp)

Deze mogelijkheid werd ontwikkeld door [Patrice Pineault](https://github.com/TurboGraphxBeige)
## Programmeerbaarheid
### Feature: Expose 3D views to PyQGIS
You now have the ability to create, list, and close 3D views from Python, matching the functionality of their 2D counterparts.

We refactored a number of application classes to introduce support the following `iface` methods:
- `createNewMapCanvas3D`: Creates a named 3D view instance
- `closeMapCanvas3D`: Closes a 3D view by name
- `mapCanvases3D`: List existing 3D views in the project context

Voorbeeld:

\`\`\`
> > > iface.createNewMapCanvas3D('my new 3d view') iface.mapCanvases3D() \[\] iface.closeMapCanvas3D('my new 3d view') iface.mapCanvases3D() \[\] \`\`\`
> > 
> 

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Feature: Optimised methods to convert GeoJSON geometries to QgsGeometry
We've added some highly optimised methods which allow direct construction of geometries (QgsGeometry) from raw JSON objects, instead of requiring translation through another library's geometry structures. These methods are exposed through the new API call `QgsJsonUtils.geometryFromGeoJson`.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Qt WebEngine classes can now be used by plugins
In older QGIS versions, an incompatibility between the modern Qt "WebEngine" classes and QGIS' 3D framework prevented QGIS plugins from using any WebEngine widgets. This was a significant shortcoming, as the older Qt "WebKit" widgets were very limited, slow, and did not support many modern JavaScript essentials.

In 3.36, we've reworked how QGIS 3D is initialised to remove this incompatibility. Scripts and plugins can now safely use Qt's WebEngine classes without issue!

Dit werd mogelijk gemaakt door <https://qgis.org>

Deze mogelijkheid werd ontwikkeld door QGIS.org
### Feature: Vertical and compound Coordinate Reference System support in CRS widgets
As part of the ongoing QGIS grant project for vertical CRS handling (see [QEP 267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267)), all of QGIS' coordinate reference system can now be set to show only vertical or compound CRS. This allows plugins and scripts to present users with choices of vertical CRS, ready for use in QgsCoordinateTransform objects for vertical CRS transformations.

See QgsCoordinateReferenceSystemProxyModel.Filter for the available CRS filtering options for use in these widgets.

Dit werd mogelijk gemaakt door [QGIS.org](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Python support in Qt6 builds
While version 5.15 remains the recommended Qt version for compiling QGIS, we've been hard at work adding full support for Qt 6 builds of QGIS. This is necessary in order to support modern desktop requirements, such as full compatibility with Wayland based Linux environments and for optimised Apple silicon builds.

QGIS 3.36 brings support for running Python under Qt 6 builds, and enables use of the PyQGIS library within Qt 6. This is a significant milestone in our ongoing journey towards full support for Qt 6!

Dit werd mogelijk gemaakt door [QGIS.org](https://qgis.org)
### Feature: Add meshMenu to QGIS Interface
`meshMenu` has been added to the `iface` object, giving plugins and scripts an easy way to extend the Mesh menu.

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://oslandia.com/)
### Feature: Server: onProjectReady method for filter plugins
The new `onProjectReady` method is called after the `QgsProject` instance is ready for a server request and before entering the main logic for core services.

The `onRequestReady` method is called after the `QgsRequestHandler` is ready and populated with parameters, but before the `QgsProject` instance is ready.

You can use `onProjectReady` to perform operations at the project level, like adding variables, checking vector layer categories, etc.

Dit werd mogelijk gemaakt door 3Liz

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
### Feature: Add fuzzy comparisons methods
We've added new methods for `fuzzyEquals` and `fuzzyDistanceEquals` to the QGIS geometry classes. These methods compare geometric objects with a tolerance for small variations, enhancing the precision of equality and distance calculations. They will be particularly useful in scenarios where exact matches may not be feasible or necessary.

\`\`\`python epsilon = 0.001 geom1 = QgsLineString(QgsPoint(0.0, 0.0), QgsPoint(0.001, 0.001)) geom2 = QgsLineString(QgsPoint(0.0, 0.0), QgsPoint(0.002, 0.002))

self.assertNotEqual(geom1, geom2) \# epsilon = 1e-8 here

self.assertTrue(geom1.fuzzyEqual(geom2, epsilon)) self.assertFalse(geom1.fuzzyDistanceEqual(geom2, epsilon)) \`\`\`

Dit werd mogelijk gemaakt door [QGIS.ORG (met GRANT)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://oslandia.com/)
### Feature: Measured line methods
In QGIS 3.36 we've introduced a `measuredLine` method within `Qgs(Multi)LineString`. This method builds upon the code from PostGIS behind ST\_AddMeasure.

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://oslandia.com/)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (itOpen / qcooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server WMS wrong tile boundary | [#55747](https://github.com/qgis/QGIS/issues/55747) | Works for me (awaiting feedback) |  |
| SLD: Hang when saving sld with linepattern orientation greater then 90 | [#55920](https://github.com/qgis/QGIS/issues/55920) | [PR #55928](https://github.com/qgis/QGIS/pull/55928) | [PR #55933](https://github.com/qgis/QGIS/pull/55933) |
| SLD saving ignores setting for exporting polygon fills as png tiles | [#55921](https://github.com/qgis/QGIS/issues/55921) | [PR #55928](https://github.com/qgis/QGIS/pull/55928) | [PR #55933](https://github.com/qgis/QGIS/pull/55933) |
| Drill down widget not working when parent field has the completer option activated | [#55922](https://github.com/qgis/QGIS/issues/55922) | [PR #55940](https://github.com/qgis/QGIS/pull/55940) | [PR #55951](https://github.com/qgis/QGIS/pull/55951) |
| Open Feld Calculator Crash | [#55898](https://github.com/qgis/QGIS/issues/55898) | Terugkoppeling |  |
| Secured WMS regression in 3.28 / 3.34?; service does not load but loads in earlier QGIS versions / other wms clients. | [#55984](https://github.com/qgis/QGIS/issues/55984) | Werkt bij mij wel |  |
| [QGIS Server][WMS] getLegend - Raster layers values not showed in legend | [#55651](https://github.com/qgis/QGIS/issues/55651) | [PR #56026](https://github.com/qgis/QGIS/pull/56026) | [PR #56257](https://github.com/qgis/QGIS/pull/56257) |
| Attribute table frame, with "allow url to be read as HTML format" has not expected result like hyperlink when output PDF file is maked from "GetPrint" request from QGIS Server | [#52370](https://github.com/qgis/QGIS/issues/52370) | Is geen probleem |  |
| WMS provider Cannot calculate extent error adding a WMTS layer from QGIS server | [#47349](https://github.com/qgis/QGIS/issues/47349) | Werkt bij mij wel |  |
| Raster Calculator Raster Menu - on the fly layer name gives issues | [#55890](https://github.com/qgis/QGIS/issues/55890) | [PR #56067](https://github.com/qgis/QGIS/pull/56067) | NOG TE DOEN |
| Expanding PostGIS table/schema in browser panel triggers slow inspection of all tables in schema | [#56069](https://github.com/qgis/QGIS/issues/56069) | [PR #56090](https://github.com/qgis/QGIS/pull/56090) | [PR #56385](https://github.com/qgis/QGIS/pull/56385) |
| Secured WMS regression in 3.28 / 3.34?; service does not load but loads in earlier QGIS versions | [#55984](https://github.com/qgis/QGIS/issues/55984) | Turned into a feature request after debugging |  |
| QGis crashes when digitizing with snapping | [#53956](https://github.com/qgis/QGIS/issues/53956) | [PR #56131](https://github.com/qgis/QGIS/pull/56131) | [PR #56204](https://github.com/qgis/QGIS/pull/56204) |
| Ellipse symbol size units are lost when closing the dialog | [#56236](https://github.com/qgis/QGIS/issues/56236) | [PR #56237](https://github.com/qgis/QGIS/pull/56237) | [PR #56248](https://github.com/qgis/QGIS/pull/56248) |
| QgsFields are viewed as the same despite having different QgsEditorWidgetSetup's | [#55873](https://github.com/qgis/QGIS/issues/55873) | [PR #56264](https://github.com/qgis/QGIS/pull/56264) | [PR #56272](https://github.com/qgis/QGIS/pull/56272) |
| Expression with newline and quotes in multiline comment leads to syntax error | [#55518](https://github.com/qgis/QGIS/issues/55518) | [PR #56315](https://github.com/qgis/QGIS/pull/56315) | [PR #56339](https://github.com/qgis/QGIS/pull/56339) |
| Linebreak and text vanish in HTML label | [#55532](https://github.com/qgis/QGIS/issues/55532) | [PR #56334](https://github.com/qgis/QGIS/pull/56334) | no (risky) |
| Postgres raster: sparse values of rasters are not displayed correctly | [#55784](https://github.com/qgis/QGIS/issues/55784) | [PR #56363](https://github.com/qgis/QGIS/pull/56363) | Failed with unrelated error |
| Running VACUUM via browser shows an error messages without identififiers | [#56377](https://github.com/qgis/QGIS/issues/56377) | [PR #56380](https://github.com/qgis/QGIS/pull/56380) | NOG TE DOEN |
| SHP: Fix unreported issue with spatialindex | niet gerapporteerd | [PR #56366](https://github.com/qgis/QGIS/pull/56366) | [PR #56399](https://github.com/qgis/QGIS/pull/56399) |
| WFS sublayer is missing when FeatureType is added from QGIS browser | [#56403](https://github.com/qgis/QGIS/issues/56403) | [PR #56404](https://github.com/qgis/QGIS/pull/56404) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Sort WFS layers ASC by default (and not DESC) | [#55693](https://github.com/qgis/QGIS/issues/55693) | [PR #55947](https://github.com/qgis/QGIS/pull/55947) | [PR #55953](https://github.com/qgis/QGIS/pull/55953) |
| Value Relation widget with Filter Expression makes QGIS crash in editing mode | [#55854](https://github.com/qgis/QGIS/issues/55854) | [PR #55948](https://github.com/qgis/QGIS/pull/55948) | [PR #55952](https://github.com/qgis/QGIS/pull/55952) |
| Hang/Crash when attempting to drag&drop multiple layers into gpkg | [#29510](https://github.com/qgis/QGIS/issues/29510) | [PR #55950](https://github.com/qgis/QGIS/pull/55950) | NOG TE DOEN |
| Crash on KML load | [#55963](https://github.com/qgis/QGIS/issues/55963) | [GDAL PR 9131](https://github.com/OSGeo/gdal/pull/9131) | [GDAL PR 9204](https://github.com/OSGeo/gdal/pull/9204) |
| Value Relation widget with Filter Expression makes QGIS crash in editing mode | [#55854](https://github.com/qgis/QGIS/issues/55854) | [PR #55980](https://github.com/qgis/QGIS/pull/55980) | [PR #55986](https://github.com/qgis/QGIS/pull/55986) |
| QGIS crashes when move tool is active and non-vector layer is selected | [#55492](https://github.com/qgis/QGIS/issues/55492) | [PR #55981](https://github.com/qgis/QGIS/pull/55981) | [PR #55985](https://github.com/qgis/QGIS/pull/55985) |
| Trailing slashes are silently removed from filter strings | [#55975](https://github.com/qgis/QGIS/issues/55975) | [PR #55988](https://github.com/qgis/QGIS/pull/55988) | [PR #55993](https://github.com/qgis/QGIS/pull/55993) |
| Vector layer points are not being imported/shown from MySQL datasource | [#55463](https://github.com/qgis/QGIS/issues/55463) | [GDAL PR 9152](https://github.com/OSGeo/gdal/pull/9152) | [GDAL PR 9180](https://github.com/OSGeo/gdal/pull/9180) |
| OAPIF: Adding layer with lot of vertices freezes QGIS | [#56059](https://github.com/qgis/QGIS/issues/56059) | [PR #56066](https://github.com/qgis/QGIS/pull/56066) | [PR #56095](https://github.com/qgis/QGIS/pull/56095) |
| [PostgreSQL provider] Add missing namespace escaping in SQL requests | niet gerapporteerd | [PR #56173](https://github.com/qgis/QGIS/pull/56173) | [PR #56186](https://github.com/qgis/QGIS/pull/56186) |
| Export Save features to gpkg does not keep Field Domains, but using Convert Format does | [#56184](https://github.com/qgis/QGIS/issues/56184) | [PR #56209](https://github.com/qgis/QGIS/pull/56209) | Niet van toepassing |
| QGIS crashes after making a connection to a GeoPackage | [#56203](https://github.com/qgis/QGIS/issues/56203) | [PR #56210](https://github.com/qgis/QGIS/pull/56210) | [PR #56214](https://github.com/qgis/QGIS/pull/56214) |
| Catch potential QgsCsException at various places; improve qgscoordinatetransform.h doc | niet gerapporteerd | [PR #56212](https://github.com/qgis/QGIS/pull/56212) | [PR #56244](https://github.com/qgis/QGIS/pull/56244) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Oracle database connection lists table multiple times | [#55961](https://github.com/qgis/QGIS/issues/55961) | NOG TE DOEN |  |
| Boolean discrepancy between expression editor and layer property | [#55923](https://github.com/qgis/QGIS/issues/55923) | [PR #56369](https://github.com/qgis/QGIS/pull/56369) | Nee |
| Using TypeVectorAnyGeometry in multiple input parameter not filtering non-spatial layers | [#55636](https://github.com/qgis/QGIS/issues/55636) | [PR #56453](https://github.com/qgis/QGIS/pull/56453) | [PR #56459](https://github.com/qgis/QGIS/pull/56459) |
| Remove expression evaluation in layout legend widget | [#53442](https://github.com/qgis/QGIS/issues/53442) | [PR #56372](https://github.com/qgis/QGIS/pull/56372) | Nee |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Raster band descriptions are shown twice | [#55156](https://github.com/qgis/QGIS/issues/55156) | [PR #55971](https://github.com/qgis/QGIS/pull/55971) |  |
| Bad_alloc when using Outline: Simple Line with Align dash pattern to line length | [#45432](https://github.com/qgis/QGIS/issues/45432) | [PR #55969](https://github.com/qgis/QGIS/pull/55969) | [PR #55991](https://github.com/qgis/QGIS/pull/55991) |
| DBManager uses deprecated constructor for QgsCoordinateReferenceSystem | [#54916](https://github.com/qgis/QGIS/issues/54916) | [PR #55968](https://github.com/qgis/QGIS/pull/55968) |  |
| Harmonize use of password lineedit in auth method editors | niet gerapporteerd | [PR #55970](https://github.com/qgis/QGIS/pull/55970) |  |
| [Data-defined Assistant] Symbols preview doesn't update if "Apply transform curve" checkbox is unchecked | [#24961](https://github.com/qgis/QGIS/issues/24961) | [PR #55967](https://github.com/qgis/QGIS/pull/55967) |  |
| Data defined assistant dialogs do not use the right title case for their name | [#26925](https://github.com/qgis/QGIS/issues/26925) | [PR #55967](https://github.com/qgis/QGIS/pull/55967) |  |
| Identify features tool does not display the ellipsoid units when "Map units" is chosen | [#26995](https://github.com/qgis/QGIS/issues/26995) | [PR #56003](https://github.com/qgis/QGIS/pull/56003) |  |
| (api) Use of None in QgsMeshRendererScalarSettings raises Python issues | [#51033](https://github.com/qgis/QGIS/issues/51033) | [PR #55999](https://github.com/qgis/QGIS/pull/55999) |  |
| Crash/freeze during Voronoi Analysis with large input dataset | [#37263](https://github.com/qgis/QGIS/issues/37263) | works for me (fixed in QEP #217) |  |
| Filling the Raster attribute tables tab with buttons should not be systematic in Layer Styling panel | [#55501](https://github.com/qgis/QGIS/issues/55501) | werkt bij mij wel |  |
| List of predefined scales in 2D map view does not update | [#51327](https://github.com/qgis/QGIS/issues/51327) | werkt bij mij wel |  |
| Data defined Assistant: closing the dialog without setting an expression invalidates the widget | [#24665](https://github.com/qgis/QGIS/issues/24665) | werkt bij mij wel |  |
| Harmonize point layer behavior regarding vertices extraction/filtering algorithms | [#33502](https://github.com/qgis/QGIS/issues/33502) | [PR #55996](https://github.com/qgis/QGIS/pull/55996) |  |
| Image export is truncated at 32768 pixels | [#41045](https://github.com/qgis/QGIS/issues/41045) | [PR #56054](https://github.com/qgis/QGIS/pull/56054) |  |
| Using the Assistant for Data Defined Colors incorrectly shows 'custom ramp' instead of the correct colour ramp name | [#48889](https://github.com/qgis/QGIS/issues/48889) | [PR #56057](https://github.com/qgis/QGIS/pull/56057) |  |
| Project predefined scales do not override global scales in labels and 2D map view widgets | [#51326](https://github.com/qgis/QGIS/issues/51326) | [PR #55998](https://github.com/qgis/QGIS/pull/55998) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Feature: Bug fixes by Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Select by Location - Point that is snapped along a linestring, is only being selected when using 'Disjoint' predicate | [#53826](https://github.com/qgis/QGIS/issues/53826) | Not a bug (tolerance and snapping problem) |  |
| [Topology Checker] Allow check does not have dangles on a second layer | [#52881](https://github.com/qgis/QGIS/issues/52881) | Not a bug. Marked as a feature request |  |
| DWG Import Tool default polyline layer style - thick symbol applied when "width" field is NULL | [#55512](https://github.com/qgis/QGIS/issues/55512) | [PR #56187](https://github.com/qgis/QGIS/pull/56187) | [PR #56228](https://github.com/qgis/QGIS/pull/56228) |
| Random Points in Polygons - Crash | [#55445](https://github.com/qgis/QGIS/issues/55445) | Can't reproduce |  |
| Buggy validation of closed QgsLineString | [#54022](https://github.com/qgis/QGIS/issues/54022) | [PR #56130](https://github.com/qgis/QGIS/pull/56130) | [PR #56229](https://github.com/qgis/QGIS/pull/56229) |
| TIN: Enable fromWkb/fromWkt | niet gerapporteerd | [PR #56071](https://github.com/qgis/QGIS/pull/56071) | nee |
| [OGC] Polygon: fix rings order | niet gerapporteerd | [PR #55306](https://github.com/qgis/QGIS/pull/55306) | nee |
| Unable to add layers with M (measure) geometries from PostGIS | [#55223](https://github.com/qgis/QGIS/issues/55223) | [PR #56199](https://github.com/qgis/QGIS/pull/56199) | [PR #56211](https://github.com/qgis/QGIS/pull/56211) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| [3D] disable altitude binding if altitude clamping is absolute | niet gerapporteerd | [PR #56154](https://github.com/qgis/QGIS/pull/56154) | [PR #56198](https://github.com/qgis/QGIS/pull/56198) |
| Improper cast of textual primary key during import with DB Manager | [#55856](https://github.com/qgis/QGIS/issues/55856) | [PR #56243](https://github.com/qgis/QGIS/pull/56243) | [PR #56259](https://github.com/qgis/QGIS/pull/56259) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| [Processing] "Points to path" algorithm calculates incorrect attributes values | [#55860](https://github.com/qgis/QGIS/issues/55860) | [PR #55917](https://github.com/qgis/QGIS/pull/55917) | [PR #55932](https://github.com/qgis/QGIS/pull/55932) |
| Fix GUI freezing when changing raster renderer | niet gerapporteerd | [PR #56000](https://github.com/qgis/QGIS/pull/56000) | [PR #56077](https://github.com/qgis/QGIS/pull/56077) |
| Point Cloud Property window resizing issue | [#43276](https://github.com/qgis/QGIS/issues/43276) | [PR #55976](https://github.com/qgis/QGIS/pull/55976) | [PR #56253](https://github.com/qgis/QGIS/pull/56253) |
| Dialog windows are too tall for some screens, rendering them unusable | [#32021](https://github.com/qgis/QGIS/issues/32021) | [PR #55978](https://github.com/qgis/QGIS/pull/55978) |  |
| Point Cloud renderer treats Unsigned8 data as Signed8 | [#55236](https://github.com/qgis/QGIS/issues/55236) | [PR #56159](https://github.com/qgis/QGIS/pull/56159) | [PR #56252](https://github.com/qgis/QGIS/pull/56252) |
| Duplicating a layer with pushing the ctrl-key while dragging, results in a layer that can't be renamed individually | [#28674](https://github.com/qgis/QGIS/issues/28674) | [PR #56188](https://github.com/qgis/QGIS/pull/56188) | [PR #56193](https://github.com/qgis/QGIS/pull/56193) |
| Prevent opening of Layer Properties when double-clicking on visibility checkbox in Layers Panel | [#38179](https://github.com/qgis/QGIS/issues/38179) | [PR #56190](https://github.com/qgis/QGIS/pull/56190) | [PR #56231](https://github.com/qgis/QGIS/pull/56231) |
| After angle/bearing measurement QGIS crashes | [#54773](https://github.com/qgis/QGIS/issues/54773) | [PR #56202](https://github.com/qgis/QGIS/pull/56202) | [PR #56216](https://github.com/qgis/QGIS/pull/56216) |
| Closing "Measure Bearing" or "Measure Angle" results dialog causes crash | [#46151](https://github.com/qgis/QGIS/issues/46151) | [PR #56202](https://github.com/qgis/QGIS/pull/56202) | [PR #56216](https://github.com/qgis/QGIS/pull/56216) |
| Measure angle dialog may appear off-screen | [#56192](https://github.com/qgis/QGIS/issues/56192) | [PR #56205](https://github.com/qgis/QGIS/pull/56205) | [PR #56217](https://github.com/qgis/QGIS/pull/56217) |
| Loading a remote COPC gets stuck when calculating stats and in 3D view | [#55210](https://github.com/qgis/QGIS/issues/55210) | [PR #56265](https://github.com/qgis/QGIS/pull/56265) | [PR #56278](https://github.com/qgis/QGIS/pull/56278) |
| Crash after right click during drawing shape annotations | [#56106](https://github.com/qgis/QGIS/issues/56106) | [PR #56157](https://github.com/qgis/QGIS/pull/56157) |  |
| Allow deleting geometry part of singlepart features | niet gerapporteerd | [PR #56279](https://github.com/qgis/QGIS/pull/56279) |  |
| The Settings->Options dlg no longer opens at the specific Processing options page and GPS options page | [#56381](https://github.com/qgis/QGIS/issues/56381) | [PR #56384](https://github.com/qgis/QGIS/pull/56384) | master only |
| 3d map view - point clouds classification symbology changes (check/uncheck classes) not honored | [#56109](https://github.com/qgis/QGIS/issues/56109) | [PR #56391](https://github.com/qgis/QGIS/pull/56391) | [PR #56398](https://github.com/qgis/QGIS/pull/56398) |
| Problem with Georeferencing Tool-QGIS 3.28.12 Firenze | [#55167](https://github.com/qgis/QGIS/issues/55167) | Is geen probleem |  |
| Not possible to open LAS file with very small X/Y/Z scale | [#49317](https://github.com/qgis/QGIS/issues/49317) | Fixed upstream |  |
| No error is shown when indexing and untwine crashes | [#48307](https://github.com/qgis/QGIS/issues/48307) | [Untwine PR #159](https://github.com/hobuinc/untwine/pull/159) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (LutraConsulting)](https://lutraconsulting.co.uk/)
### Feature: Bug fixes by Mathieu Pellerin
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Text in new version available message bar is poorly visible in Night mapping theme | [#56091](https://github.com/qgis/QGIS/issues/56091) | [PR #56455](https://github.com/qgis/QGIS/pull/56455) | [PR #56469](https://github.com/qgis/QGIS/pull/56469) |
| Text of title bars in database manager is poorly visible with Night Mapping theme | [#56105](https://github.com/qgis/QGIS/issues/56105) | [PR #56448](https://github.com/qgis/QGIS/pull/56448) | [PR #56474](https://github.com/qgis/QGIS/pull/56474) |
| Crash after right click during drawing shape annotations | [#56106](https://github.com/qgis/QGIS/issues/56106) | [PR #56447](https://github.com/qgis/QGIS/pull/56447) | [PR #56470](https://github.com/qgis/QGIS/pull/56470) |
| WMS source select interpretation combobox not setting proper index on empty interpretation string | [#56418](https://github.com/qgis/QGIS/pull/56418#issuecomment-1954156134) | [PR #56441](https://github.com/qgis/QGIS/pull/56441) | [PR #56473](https://github.com/qgis/QGIS/pull/56473) |
| QGIS: Snap geometries to layer - not all points are snapping | [#56424](https://github.com/qgis/QGIS/issues/56424) | [PR #56426](https://github.com/qgis/QGIS/pull/56426) | [PR #56449](https://github.com/qgis/QGIS/pull/56449) |
| Cannot delete vertices when attribute table is docked | [#56262](https://github.com/qgis/QGIS/issues/56262) | [PR #56423](https://github.com/qgis/QGIS/pull/56423) | [PR #56439](https://github.com/qgis/QGIS/pull/56439) |
| Add missing tooltip for "Custom Properties" style category | [#56362](https://github.com/qgis/QGIS/issues/56362) | [PR #56421](https://github.com/qgis/QGIS/pull/56421) | [PR #56440](https://github.com/qgis/QGIS/pull/56440) |
| Ensure that saving map [canvas] as image/PDF takes high DPI scaling factor into account | niet gerapporteerd | [PR #56400](https://github.com/qgis/QGIS/pull/56400) |  |
| MBTiles layers are valid when dataset is missing | niet gerapporteerd | [PR #56296](https://github.com/qgis/QGIS/pull/56296) | [PR #56298](https://github.com/qgis/QGIS/pull/56298) |
| The check result of constraints sometimes differs in the form and attribute table view | [#55390](https://github.com/qgis/QGIS/issues/55390) | [PR #56287](https://github.com/qgis/QGIS/pull/56287) | [PR #56318](https://github.com/qgis/QGIS/pull/56318) |
| Constraints are not behaving on range widget correctly when a field is displayed twice in a form | [#55607](https://github.com/qgis/QGIS/issues/55607) | [PR #56163](https://github.com/qgis/QGIS/pull/56163) | [PR #56254](https://github.com/qgis/QGIS/pull/56254) |
| DXF map theme style override not respected | niet gerapporteerd | [PR #56162](https://github.com/qgis/QGIS/pull/56162) | [PR #56164](https://github.com/qgis/QGIS/pull/56164) |
| Tileservers always blurry | [#55644](https://github.com/qgis/QGIS/issues/55644) | [PR #56047](https://github.com/qgis/QGIS/pull/56047) | [PR #56088](https://github.com/qgis/QGIS/pull/56088) |
| Blurry layouts in v3.32.2, not after v3.28.2 | [#54579](https://github.com/qgis/QGIS/issues/54579) | [PR #56085](https://github.com/qgis/QGIS/pull/56085) | [PR #56101](https://github.com/qgis/QGIS/pull/56101) |
| Pixelated QGIS logo in user profile selector dialog on high DPI screens | niet gerapporteerd | [PR #56053](https://github.com/qgis/QGIS/pull/56053) | [PR #56065](https://github.com/qgis/QGIS/pull/56065) |
| Pixelated overview panel rendering on high DPI screens | niet gerapporteerd | [PR #56050](https://github.com/qgis/QGIS/pull/56050) | [PR #56087](https://github.com/qgis/QGIS/pull/56087) |
| Welcome screen issues on high DPI screens | niet gerapporteerd | [PR #56048](https://github.com/qgis/QGIS/pull/56048) | [PR #56084](https://github.com/qgis/QGIS/pull/56084) |
| Merge vector layers also adds dbf files using Add Directory | [#56010](https://github.com/qgis/QGIS/issues/56010) | [PR #56020](https://github.com/qgis/QGIS/pull/56020) | [PR #56056](https://github.com/qgis/QGIS/pull/56056) |
| Composition relations: only the first relation is taken into account | [#55892](https://github.com/qgis/QGIS/issues/55892) | [PR #55944](https://github.com/qgis/QGIS/pull/55944) | [PR #56038](https://github.com/qgis/QGIS/pull/56038) |
| qgis_process errors with 'native:dissolve' if SEPARATE_DISJOINT=true and if OUTPUT is an explicit file | [#55587](https://github.com/qgis/QGIS/issues/55587) | [PR #55966](https://github.com/qgis/QGIS/pull/55966) | [PR #55982](https://github.com/qgis/QGIS/pull/55982) |
| "Delete Selected" button not working properly in a non-geometric layer | [#55618](https://github.com/qgis/QGIS/issues/55618) | [PR #55965](https://github.com/qgis/QGIS/pull/55965) | [PR #56006](https://github.com/qgis/QGIS/pull/56006) |
| UI-file-based (combo-box-containing) forms are not working in QGIS 3.34 any longer | [#55621](https://github.com/qgis/QGIS/issues/55621) | [PR #55964](https://github.com/qgis/QGIS/pull/55964) | [PR #55987](https://github.com/qgis/QGIS/pull/55987) |
| Can't change spatial bookmark storage or group by drag and drop | [#55819](https://github.com/qgis/QGIS/issues/55819) | [PR #55957](https://github.com/qgis/QGIS/pull/55957) |  |
| Print layout: cursor jumps when changing cell size of fixed table | [#50257](https://github.com/qgis/QGIS/issues/50257) | [PR #55941](https://github.com/qgis/QGIS/pull/55941) | [PR #55992](https://github.com/qgis/QGIS/pull/55992) |
| Need to close the layer properties dialog before a newly created field appears in Attribute form | [#26350](https://github.com/qgis/QGIS/issues/26350) | [PR #55938](https://github.com/qgis/QGIS/pull/55938) | too risky |
| Missing checkbox partially checked state styling for non-default themes | niet gerapporteerd | [PR #56290](https://github.com/qgis/QGIS/pull/56290) | [PR #56306](https://github.com/qgis/QGIS/pull/56306) |
| Unable to read MBTiles in paths containing multibytes | [#56023](https://github.com/qgis/QGIS/issues/56023) | [PR #56462](https://github.com/qgis/QGIS/pull/56462) |  |
| [Data Source Manager] Adding a local raster XYZ Tiles directory as layer is no longer possible | [#56371](https://github.com/qgis/QGIS/issues/56371) | [PR #56418](https://github.com/qgis/QGIS/pull/56418) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix broken coordinate transforms on qt6 builds | niet gerapporteerd | [PR #55914](https://github.com/qgis/QGIS/pull/55914) | [PR #55935](https://github.com/qgis/QGIS/pull/55935) |
| Fix crash in QgsRasterPipe when removing roles | niet gerapporteerd | [PR #55955](https://github.com/qgis/QGIS/pull/55955) | [PR #56008](https://github.com/qgis/QGIS/pull/56008) |
| Fix broken data defined override buttons in text format widget when no layer is associated | niet gerapporteerd | [PR #55989](https://github.com/qgis/QGIS/pull/55989) | N/B |
| Avoid use of pygments in metasearch | niet gerapporteerd | [PR #56160](https://github.com/qgis/QGIS/pull/56160) | N/B |
| Fixes filters applied to a duplicated AFS layer also incorrectly apply to the original layer | niet gerapporteerd | [PR #56195](https://github.com/qgis/QGIS/pull/56195) | [PR #56221](https://github.com/qgis/QGIS/pull/56221) |
| [processing] Don't try to interpret distance widget value as CRS | niet gerapporteerd | [PR #56292](https://github.com/qgis/QGIS/pull/56292) | [PR #56297](https://github.com/qgis/QGIS/pull/56297) |
| [3dtiles] Skip completely transparent primitives | [#55579](https://github.com/qgis/QGIS/issues/55579) | [PR #56303](https://github.com/qgis/QGIS/pull/56303) | [PR #56323](https://github.com/qgis/QGIS/pull/56323) |
| Fix calculation of string stats when nulls are present | niet gerapporteerd | [PR #56305](https://github.com/qgis/QGIS/pull/56305) | [PR #56322](https://github.com/qgis/QGIS/pull/56322) |
| Don't use (broken) QgsCoordinateReferenceSystem::createFromSrsId method for virtual point clouds | niet gerapporteerd | [PR #56325](https://github.com/qgis/QGIS/pull/56325) | [PR #56333](https://github.com/qgis/QGIS/pull/56333) |
| Make datetime stats range type consistent across Qt versions | niet gerapporteerd | [PR #56355](https://github.com/qgis/QGIS/pull/56355) | [PR #56437](https://github.com/qgis/QGIS/pull/56437) |
| Fix crash in QgsStringUtils::truncateMiddleOfString on qt 6 | niet gerapporteerd | [PR #56356](https://github.com/qgis/QGIS/pull/56356) | N/B |
| Fix handling of font family from HTML on Qt 6 builds | niet gerapporteerd | [PR #56358](https://github.com/qgis/QGIS/pull/56358) | [PR #56436](https://github.com/qgis/QGIS/pull/56436) |
| Missing expression scope in batch processing expression builder | [#56132](https://github.com/qgis/QGIS/issues/56132) | [PR #56411](https://github.com/qgis/QGIS/pull/56411) | [PR #56435](https://github.com/qgis/QGIS/pull/56435) |
| Fix crash when applying vector properties dialog | niet gerapporteerd | [PR #56412](https://github.com/qgis/QGIS/pull/56412) | N/B |
| Don't force calculate layer extents when saving layers | niet gerapporteerd | [PR #56433](https://github.com/qgis/QGIS/pull/56433) | [PR #56444](https://github.com/qgis/QGIS/pull/56444) |
| Don't force full calculation of layer extent when cloning layers | niet gerapporteerd | [PR #56434](https://github.com/qgis/QGIS/pull/56434) | N/B |
| Fix running plugins are not restarted after upgrading | [#56277](https://github.com/qgis/QGIS/issues/56277) | [PR #56443](https://github.com/qgis/QGIS/pull/56443) | [PR #56475](https://github.com/qgis/QGIS/pull/56475) |
| Regenerate primary keys for Split Lines by Length outputs | [#56486](https://github.com/qgis/QGIS/issues/56486) | [PR #56490](https://github.com/qgis/QGIS/pull/56490) | [PR #56494](https://github.com/qgis/QGIS/pull/56494) |
| Fix saving " and \\ to ArcGIS REST sources | [#55946](https://github.com/qgis/QGIS/issues/55946) | [PR #56492](https://github.com/qgis/QGIS/pull/56492) |  |
| Honderden reparaties aan PyQGIS voor compatibiliteit met Qt6 | N/B |  |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Martin Dobias (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| 3D Tiles dataset without textures not shaded correctly | [#55752](https://github.com/qgis/QGIS/issues/55752) | [PR #56185](https://github.com/qgis/QGIS/pull/56185) | N/B |
| Crash when creating 3D view | [#53941](https://github.com/qgis/QGIS/issues/53941) | [PR #56320](https://github.com/qgis/QGIS/pull/56320) | [PR #56330](https://github.com/qgis/QGIS/pull/56330) |
| Fix a deadlock in remote COPC handling (3D views) | niet gerapporteerd | [PR #56388](https://github.com/qgis/QGIS/pull/56388) | [PR #56419](https://github.com/qgis/QGIS/pull/56419) |
| Fix a crash in point cloud renderer when cleaning up preview painter | niet gerapporteerd | [PR #56409](https://github.com/qgis/QGIS/pull/56409) | N/B |
| Fix a deadlock with local COPC files in 2D rendering | niet gerapporteerd | [PR #56432](https://github.com/qgis/QGIS/pull/56432) | [PR #56458](https://github.com/qgis/QGIS/pull/56458) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door Martin Dobias (LutraConsulting)

{{<content-end >}}
