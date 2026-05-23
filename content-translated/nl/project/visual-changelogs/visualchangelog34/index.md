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

De eerste langetermijnuitgave (LTR) van QGIS 3. QGIS 3.4 zojuist uitgegeven. Na vijf consolidatiepuntuitgaven (3.4.5) zal het de eerdere LTR vervangen in de opslagplaatsen van de pakketten in februari 2019 (bekijk [uitgaveschema]({{< ref "resources/roadmap#release-schedule" >}})). Dit is een enorme stap voorwaarts voor het project - onze eerste Long Term Release gebaseerd op het 3.x-platform. Voor gebruikers die overkomen van de 2.18 LTR is er een enorme lijst van nieuwe mogelijkheden en wijzigingen met veel impact in de nieuwe versie van de LTR. Onthoud dat plug-ins voor 3.x niet compatibel zijn met plug-ins voor 2.x, dus bekijk uw gebruik van plug-ins zorgvuldig - en help indien mogelijk om oude plug-ins te migreren naar het nieuwe platform. Als u dat nog niet gedaan heeft, kijk eens in de logs met wijzigingen van [Versie 3.0](../visualchangelog30) en [Versie 3.2](../visualchangelog32) om het volledige bereik van de wijzigingen in de uitgave 3.4 te begrijpen.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst met donoren]({{&lt; ref &quot;/funding/donate/donors.md&quot; &gt;}}). Als u een officieel dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende lidmaatschappen]({{< ref "/funding/donate/donors.md" >}}) voor details. Ondersteuning van QGIS helpt ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van supporters wordt hieronder weergegeven - een welgemeend bedankt voor al onze ondersteuners!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

![image1](images/projects/750d7d9b7e9dbd498202c4b1288a0cbceb1cd65b.png)

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Flatpak
QGIS is nu beschikbaar als een toepassing in Flatpak op [flathub](https://flathub.org/apps/search/qgis) Flatpak (eerder xdg-app) is een softwaregereedschap voor het uitrollen van software, beheer van pakketten en virtualisatie van toepassingen voor Linux desktop computers. Het stelt gebruikers in staat om verschillende versies van QGIS te installeren op Linux zonder dat ze opnieuw dienen te compileren of Docker te gebruiken. Het is een volledig pakket waarin alle bibliotheken zijn opgenomen, en het gebruikt zijn eigen locaties voor gebruikersprofielen. U zult dus enige schijfruimte nodig hebben en nieuwe gewoonten moeten ontwikkelen bij het werken met Flatpak, maar het is geweldig!

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
- **json_to_map**: Converteert een met JSON gecodeerde waarde tekenreeks naar een kaart (dictionary) type object
- **map_to_json**: Converteert een kaart (dictionary) type object naar een JSON gecodeerde waarde tekenreeks
- **hstore_to_map**: Converteert een waarde hstore naar een kaart (dictionary) type object
- **map_to_hstore**: Converteert een kaart (dictionary) type object naar een waarde hstore
- **array_foreach** : Loopt door een array en voert een expressie uit op elk item in de array en geeft een nieuwe array terug die elke berekende waarde bevat
- **array_filter** : Filtert een array overeenkomstig een expressie
- **raster_value**: Geeft een monsterwaarde terug uit een rasterlaag op een gespecificeerd punt
- **to_dms**: Converteert een numerieke waarde naar een als Graden, Minuten, Seconden opgemaakte tekenreeks
- **to_dm**: Converteert een numerieke waarde naar een als Graden, Minuten opgemaakte tekenreeks
- **line_substring**: Geeft het gedeelte van een lijn- (of booggeometrie) terug dat valt tussen de gespecificeerde begin- en eindafstanden (gemeten vanaf het begin van de lijn). Z- en M-waarden worden lineair geïnterpoleerd vanuit bestaande waarden.
- **generate_series(start,stop,step)**: Maakt een array die een reeks nummers bevat.

Aanvullend zijn enkele nieuwe variabelen beschikbaar gemaakt om te gebruiken binnen expressies van QGIS:
- **\@canvas_cursor_point**: Bevat een puntwaarde die de huidige positie van de muiscursor weergeeft in het huidige kaartvenster
- **\@map_layers**: Bevat een array van alle lagen die zichtbaar zijn op de kaart
- **\@map_layer_ids**: Bevat een array van alle laag-ID's voor lagen die zichtbaar zijn op de kaart

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
Vaak is het nuttig om objecten te selecteren/identificeren die worden bedekt door een bestaande polygoon. Hiervoor kunnen gebruikers de gereedschappen \"Objecten op polygoon selecteren\" en \"Objecten op polygoon identificeren\" gebruiken, maar het was nodig om de betreffende polygoon handmatig op te zoeken. Deze nieuwe mogelijkheid stelt de gebruiker in staat om met rechts op de kaart te klikken en een bestaand object polygoon uit te kiezen op die locatie vanuit het pop-upmenu - die polygoon zal worden gebruikt als invoer voor selectie of identificatie.

[![image4](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)

Dit werd mogelijk gemaakt door Leicestershire County Council

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Gebruikersinterface
### Mogelijkheid: Automatisch selecteren van geëxporteerde bestanden in bestandsbeheer
Wanneer een item op de berichtenbalk linkt naar een gemaakt bestand (bijv. na exporteren van een lay-out of kaartlaag), zal die link nu direct de map in de bestandsbrowser van het bestandssysteem openen waarin dit bestand is opgenomen EN het gemaakte bestand selecteren. Het is een superhandige sneltoets die bewerkingen aan bestanden na een export vanuit QGIS versnellen!

[![image5](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe optie \"Map openen\" voor uitgeschakelde projecten op de pagina Welkom
Deze nieuwe optie in het contextmenu, met rechts klikken, voor uitgeschakelde items op de pagina Welkom stelt gebruikers in staat om het dichtstbijzijnde bestaande pad te openen naar de originele projectlocatie in hun bestandsbeheerder, hopelijk om ze te helpen ontbrekende/verplaatste/hernoemde projecten terug te vinden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan UX voor tijdelijke tekenlagen
Tijdelijke tekenlagen in QGIS kunnen zeer handig zijn als een \"weggooi\"-laag nodig is, zoals wanneer gegevens in meerdere stappen vooraf worden verwerkt. Zij kunnen echter een valkuil zijn voor gewone gebruikers die zich misschien niet realiseren dat de inhoud van de laag permanent verloren zal gaan als het huidige project van QGIS wordt gesloten. Overeenkomstig is een nieuw pictogram ter indicatie toegevoegd dat naast tijdelijke tekenlagen in de lagenboom wordt weergegeven, wat direct duidelijk maakt welke lagen slechts tijdelijk zijn.

Het is ook veel eenvoudiger om deze tijdelijke tekenlagen over te zetten naar permanente op schijf-gebaseerde indelingen. U kunt ofwel klikken op het nieuwe pictogram voor indicatie of \"Permanent maken\" uit het contextmenu van de laag. QGIS zal dan vragen naar een locatie om de tijdelijke tekenlaag op te slaan, en vervangt deze ter plaatse (met behoud van dezelfde laag-ID, stijl, instellingen voor formulieren, etc.).

[![image6](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verbeteringen aan taakbeheer
De widget Taakbeheer van QGIS (weergegeven in de statusbalk wanneer een taak op de achtergrond wordt uitgevoerd) geeft nu een geschatte resterende tijdspanne aan en de tijd voor voltooien voor lang durende taken op de achtergrond. Deze geschatte tijd voor voltooiing wordt berekend met een eenvoudige lineaire interpolatie, gebaseerd op de voor de taak verstreken tijd en huidige voortgang. Ze stelt de gebruikers in staat te weten of ze alleen tijd hebben om een instantkoffie te maken in de kantoorkeuken, of een rondje te lopen en een echte barista een koffie te laten maken voor die lange verwerkingstaak is voltooid\…

Aanvullend gebruikt QGIS het standaardmechanisme voor voortgangsrapportage van het besturingssysteem op meer platforms en gelegenheden in QGIS 3.4. Sommige langdurende taken (die niet op de achtergrond worden uitgevoerd), zoals het exporteren van atlas geven nu hun voortgang weer via het mechanisme voor het besturingssysteem, en laten handige notificaties met betrekking tot het voltooien zien.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Hyperlinks naar lokale vector- & rastergegevenssets in het paneel Informatie
Voor lokale vector- en rastergegevenssets geeft de tab Informatie in het dialoogvenster Laageigenschappen nu hyperlinks naar het pad van de brondbestanden voor objecten weer. Bij het klikken op de hyperlink zal de bestandsnavigatie van het systeem worden geopend en automatisch de gegevensset accentueren.

[![image7](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)

Dit werd mogelijk gemaakt door [iMhere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Mogelijkheid: Verbeteringen aan stijlbeheer
Het QGIS-dialoogvenster Stijlbeheer (dat gebruikers in staat stelt hun eigen bibliotheken met symbolen en kleurverlopen in te stellen en te beheren) opent nu niet-modaal, dus het kan nu naast het hoofdvenster van QGIS worden gebruikt (net zoals het dialoogvenster Lay-outbeheer en de vensters van Afdruklay-out ontwerpen).

We hebben nu ook het voorbeeld van symbolen in het venster Laagstijl verbeterd, een schakelaar toegevoegd om te schakelen tussen een grote weergave van het pictogram en een gedetailleerde lijstweergave van symbolen. Met de muis over symbolen (en kleuren!) gaan geeft nu een groot voorbeeld van het symbool. Tenslotte hebben we symboollijsten meer hi-dpi-vriendelijk gemaakt.

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
Bij het exporteren en importeren van stijlen naar en vanuit `.qml`-bestanden is het nu mogelijk een subset van secties te selecteren. Dit maakt het mogelijk delen van een laagconfiguratie op te slaan of te herstellen, terwijl andere worden weggelaten. Het is bijvoorbeeld mogelijk om alleen de symbologie van een laag te exporteren en bij het importeren van dit QML-stijlbestand in een laag worden configuraties van de formulieren en widgets, of andere eigenschappen, niet beïnvloed. Het is ook mogelijk om alleen enkele secties van een stijl af te handelen bij het gebruiken van kopiëren/plakken.

[![image10](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)

Dit werd mogelijk gemaakt door [qwat group](http://qwat.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud (OPENGIS.ch GmbH)](https://www.opengis.ch)
## Digitaliseren
### Mogelijkheid: Verbeteringen aan GPS-tracking
QGIS 3.4 vergroot de ingebouwde ondersteuning voor GPS-tracking door toevoeging van de parameters \"acquisition interval\" en \"distance threshold\". Deze opties kunnen worden gebruikt om de cursor stationair te houden als de ontvanger onder statische condities opereert.

Dit werd mogelijk gemaakt door [Andrea Rossi](https://github.com/rossia)

Deze mogelijkheid werd ontwikkeld door [Andrea Rossi](https://github.com/rossia)
### Mogelijkheid: Meer keuzes voor hoeken in paneel Geavanceerd digitaliseren
Opties werden toegevoegd om snappen mogelijk te maken aan 5/10/15/18/22,5 graden in modus Constructie.

[![image11](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)

Dit werd mogelijk gemaakt door [lbartoletti](https://github.com/lbartoletti)

Deze mogelijkheid werd ontwikkeld door [lbartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Gereedschap Punten kan alleen op de huidige laag werken
Het nieuwe gereedschap Punten is nu veel productiever. Het kan punten verplaatsen op alle bewerkbare lagen in één keer, wat goed is om topologie over lagen heen te behouden. Echter, in veel gevallen willen veel van ons niet alle lagen in één keer bewerken. We hebben daarom een variatie van het kaartgereedschap Punten toegevoegd.

[![image12](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)

Dit werd mogelijk gemaakt door [Oslandia](https://oslandia.com)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](https://oslandia.com/en/home-en/)
### Mogelijkheid: Kaartgereedschap Omgekeerde lijnen toegvoegd
Een lang verwachte mogelijkheid ! Geen externe plug-in of algoritme meer om de richting van een lijn om te keren!

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

Dit is gebouwd bovenop de functionaliteit van de plug-in Geometry checker die werd geïmplementeerd door [Sourcepole](https://sourcepole.ch).

[![image16](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gegevensbeheer
### Mogelijkheid: Vertalen van projecten van QGIS
Net als QGIS en de plug-ins worden de projecten vertaald met het Qt vertaalproces. Dit betekent dat het de vertaling maakt overeenkomstig een Qt Compiled Translation Source File (`.qm` file). Wanneer de gebruiker een project opent, controleert QGIS of er een `.qm`-bestand aanwezig is in dezelfde map als het bestand `.qgs`, dat dezelfde naam heeft als het bestand `.qgs` en dat de taalcode als achtervoegsel heeft van de taal van de gebruiker (de taal die is geconfigureerd in de instellingen van QGIS). Om de vertaling te maken in de projectinstellingen, is er een optie het `.ts`-bestand te genereren, dat kan worden bewerkt met programma's als Qt Linguist of Transifex.

Meer informatie in [deze blogpost](https://new.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep en QGEP Project](https://www.qgis.ch/en)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch/)
### Mogelijkheid: Attributentabel kan op verzoek worden vastgezet
Een knop werd toegevoegd aan de werkbalk Attributentabel om op verzoek te kunnen schakelen tussen een modus vastgezet en modus als venster. Eerder dienden gebruikers een optie in het dialoogvenster Instellingen te wijzigen en een nieuwe tabel te openen om te kunnen schakelen tussen modi vastgezet/als venster. Maar dat is pijnlijk als u besluit *nadat* een tabel al is geopend en u wilt het vastzetten/losmaken\…!

[![image17](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuw filter voor locatie om over alle lagen te zoeken
Een nieuw filter voor locatie is toegevoegd dat gebruikers in staat stelt te zoeken over *alle* lagen in hun project, op de expressie van de weergave van de laag.

Het filter kan worden geactiveerd door het voorvoegsel \'af\' te gebruiken, of door een standaard zoekactie te maken via de opties van QGIS -\> Lokaliseren -\> Objecten in alle lagen. Expressies voor weergave worden gedefinieerd in de eigenschappen van de vectorlaag op de tab Bron. Individuele lagen kunnen worden gemarkeerd als niet te doorzoeken in het dialoogvenster Projecteigenschappen, op de tab Databronnen.

[![image18](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)

Dit werd mogelijk gemaakt door [Opengis.ch](https://www.opengis.ch/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Niet-verwijderbare (vereiste) lagen geaccentueerd in lagenboom
Een nieuw pictogram voor indicatie \"vergendeld\" wordt weergegeven voor lagen die zijn gemarkeerd als \"vereist\" in het huidige project. Dit pictogram geeft gebruikers directe terugkoppeling dat een bepaalde laag niet kan worden verwijderd uit het project.

Vereiste lagen worden geconfigureerd via het dialoogvenster Projecteigenschappen, tab Databronnen.

[![image19](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Rasterlaag aan een bestaand Geopackage toevoegen
Bij het opslaan van een rasterlaag naar een database van GeoPackage is het nu mogelijk de laag aan een bestaand bestand toe te voegen.

[![image20](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)

Dit werd mogelijk gemaakt door [Borys Jurgiel](https://github.com/borysiasty)

Deze mogelijkheid werd ontwikkeld door [Borys Jurgiel](https://github.com/borysiasty)
## Formulieren en widgets
### Mogelijkheid: Formulieren voor dieper zoeken (cascading) in QGIS widgets Waarderelatie
Nieuwe functies en logica in QGIS "widgets Waarderelatie" maken het mogelijk complexe, dynamische filters te implementeren in attributenformulieren in QGIS. De functionaliteit kan worden gebruikt om formulieren voor "dieper zoeken" te implementeren in QGIS, waar de beschikbare waarden in een veld afhankelijk zijn van andere velden:

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

Voor die expertgebruikers die regelmatig bewerkingen aan gegevens uitvoeren, wordt deze functionaliteit ook weergegeven via QGIS 3.0’s "Locatiebalk" (die balk "Typ om te lokaliseren" in de benedenhoek linksonder). Typen van 'ef' ("edit features" (objecten bewerken)) gevolgd door de naam van de overeenkomende bewerking stelt u in staat bewerkingen direct vanaf het toetsenbord uit te voeren. Bijv.
- Een aantal lijnobjecten selecteren
- Druk op Ctrl + K (activeert de locatiebalk)
- Typ "ef reverse"
- Druk op Enter – de geselecteerde lijnobjecten zullen onmiddellijk worden omgekeerd!

[![image23](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)

Dit werd mogelijk gemaakt door [Crowdfunding campaign](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com)
### Mogelijkheid: Modellen in het project opslaan
Sommige modellen van Processing zijn zo intrinsiek gekoppeld aan de logica binnen een bepaald project dat ze geen betekenis hebben (of helemaal niet werken) buiten dat project (bijv. modellen die afhankelijk zijn van de aanwezigheid van bepaalde lagen, relaties, etc.). Naar aanleiding daarvan kunnen, vanaf QGIS 3.4, modellen van Processing worden opgeslagen binnen projectbestanden van QGIS. Modellen die zijn opgeslagen binnen een project worden beschikbaar gemaakt zodra dat project wordt geopend. Dit voorkomt ook het vollopen van de "globale" modelprovider met modellen die geen zin hebben, en maakt het eenvoudiger een enkel project te delen, inclusief alle relevante modellen.

Modellen worden binnen projecten opgeslagen door te klikken op de nieuwe knop \"Model in project opslaan\" in de werkbalk van het dialoogvenster Grafische modellen maken. Modellen kunnen uit een project worden verwijderd via het contextmenu (rechtsklikken) in de Toolbox.

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
QGIS 3.4 voegt een eigen algoritme \"k-means clustering\" toe. Gebaseerd op een port van de functie van PostGIS ST_ClusterKMeans, voegt dit algoritme een nieuw cluster ID-veld toe aan een set van invoerobjecten die de cluster van het object identificeert, gebaseerd op een benadering van K-means clustering. Indien geen puntgeometrieën worden gebruikt als invoer, is het clusteren gebaseerd op het zwaartepunt van de invoergeometrieën.

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
### Mogelijkheid: Algoritme \'Raster pixels to points\'
Een nieuw algoritme \"Pixels to points\" werd toegevoegd in QGIS 3.4, wat een puntobject maakt in het midden van elke pixel. Pixels zonder gegevens worden overgeslagen.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Line substring
Dit nieuwe, veel om gevraagde, algoritme geeft het gedeelte van een lijn (of een boog) terug dat valt tussen de gespecificeerde begin- en eindafstanden (gemeten vanaf het begin van de lijn). Z- en M-waarden worden lineair geínterpoleerd vanuit bestaande waarden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme \"Punt op lijn interpoleren\"
Dit nieuwe algoritme maakt een puntgeometrie, geïnterpoleerd op een ingestelde afstand langs de lijn- (of grens van de polygoon) geometrieën. Gebogen invoergeometrieën worden volledig ondersteund. Z- of M-waarden worden lineair geïnterpoleerd, gebaseerd op bestaande waarden.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: k-neighbour concave hull
Dit werd mogelijk gemaakt door <https://qgis.org>

Deze mogelijkheid werd ontwikkeld door [Detlev Neumann, Rudi von Staden](https://qgis.org)
### Mogelijkheid: Pythonscripts die algoritmes implementeren voeren nu het algoritme uit bij slepen en neerzetten en dubbelklikken in de browser
Indien van toepassing zullen scripts nu een dialoogvenster voor algoritmes van Processing openen bij:
- Slepen en neerzetten van een script voor Python in het hoofdvenster
- Gebruik klik met rechts in het paneel Browser voor het uitvoeren van scriptactie

[![image25](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)

Dit werd mogelijk gemaakt door [iMhere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Mogelijkheid: Nieuwe herschikking GDAL\'s bandalgoritme
Een nieuw algoritme van provider GDAL \'Banden herschikken\' werd toegevoegd aan de Toolbox van processing. Het algoritme maakt het mogelijk om rasters doorlopend uit te voeren met behulp van een subset van opgegeven invoerrasterbanden, en biedt de mogelijkheid de banden opnieuw te schikken.

[![image26](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)

Dit werd mogelijk gemaakt door [iMHere Asia](https://www.imhere-asia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.imhere-asia.com/)
### Mogelijkheid: \"Vooraf berekende\" waarden voor parameters van modelalgoritmes
Een nieuwe optie is aanwezig voor alle parameters om een  \"vooraf berekende expressie\" te gebruiken. Deze expressie wordt eenmaal geëvalueerd voordat het kind-algoritme wordt uitgevoerd en gebruikt bij de uitvoering van dat algoritme.

Dit werd mogelijk gemaakt door [QGIS](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme \"Renderer Categorieën maken uit stijlen\"
Dit nieuwe algoritme stelt de renderer voor een vectorlaag in op een renderer Categorieën met behulp van overeenkomende symbolen uit een stijldatabase.

Een gespecificeerde expressie (of veldnaam) wordt gebruikt om categorieën voor de renderer te maken, waarbij QGIS een categorie maakt voor elke unieke waarde in de laag. Elke categorie komt individueel overeen met de symbolen die bestaan binnen de gespecificeerde XML-stijldatabase van QGIS. Wanneer een overeenkomende symboolnaam is gevonden, wordt het symbool van de categorie ingesteld op dit overeenkomende symbool.

De overeenkomst is standaard niet hoofdlettergevoelig, maar kan, indien gewenst, worden ingesteld op hoofdlettergevoelig. Optioneel kunnen niet-alfanumerieke tekens in zowel de waarde van de categorie als de naam van het symbool worden genegeerd bij het uitvoeren van de vergelijking. Dit maakt een hogere tolerantie mogelijk bij het vergelijken van categorieën met symbolen.

Indien gewenst kunnen ook tabellen worden uitgevoerd die lijsten bevatten van de categorieën die niet overeenkwamen met symbolen, en symbolen die niet overeenkwamen met categorieën.

[![image27](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe modus voor algoritme Snap geometries
De nieuwe modus \"Aan ankers voor knopen vastzetten (alleen enkele laag)\" zorgt ervoor dat twee punten van de vectorlayer op zijn minst op een afstand, opgegeven in een drempelwaarde, van elkaar af liggen.

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
Het lezen van types PostgreSQL JSON wordt ondersteund. gegevens van JSON kunen in de widgets worden weergegeven als \"Sleutel/Waarde\" (kaarten), als \"Lijst\" (arrays) of als tekst.

[![image33](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Ondersteuning voor ESRI tokenauthenticatie
Ondersteuning is toegevoegd aan het authenticatiesysteem van QGIS voor ESRI\'s tijdelijk token gebaseerde authenticatie. Dit maakt het mogelijk een verbinding te maken met ArcGIS Feature en Map Servers via een toegewezen tijdelijk token.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: SQL Server - Afhandeling ongeldige geometrie
Recente versies van QGIS zijn overgeschakeld naar een veiligere benadering om lagen van SQL Server te lezen, die automatisch controleren op de geldigheid voor geometrieën en geometrieën waar nodig repareren. Deze workaround is vereist om problemen te voorkomen met het ontwerp van de afhandeling van geometrieën van SQL Server, waarbij het tegenkomen van rijen met ongeldige geometrieën een verzoek stilletjes kan afbreken zonder alle objecten uit een laag. Helaas komt de workaround met een significant verlies aan uitvoering.

In QGIS 3.4 werd een nieuwe instelling toegevoegd die gebruikers in staat stelt om handmatig de afhandeling van QGIS voor ongeldige geometrieën van SQL Server uit te schakelen. Inschakelen van de instelling \"Afhandeling ongeldige geometrieën overslaan\" onder de eigenschappen van een verbinding naar een SQL Server zorgt ervoor dat QGIS al het tijdrovende verwerken van valideren van geometrieën overslaat. Plaatst echter ferm de verantwoordelijkheid, om ervoor te zorgen dat alle objecten in de database geldige geometrieën hebben, terug bij de gebruiker/beheerder van de database. **Dit is een instelling \"Gebruiken op eigen risico\". Onjuist inschakelen van deze optie kan leiden tot ontbrekende objecten en gegevensverlies.**

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
Het is nu mogelijk QGIS Server te configureren om ervoor te zorgen dat het zijn logs naar stderr wegschrijft. Dit wordt gedaan door de omgevingsvariabele QGIS_SERVER_LOG_FILE in te stellen op de speciale waarde \"stderr\".

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
Een zeer snelle statische ruimtelijke index voor 2D-punten, gebaseerd op een platte KD-boom, met behulp van <https://github.com/mourner/kdbush.hpp>

Deze index, vergeleken met QgsSpatialIndex: - ondersteunt alleen objecten met één enkel punt (geen multipunten) - is statisch (objecten kunnen na het maken niet aan de index worden toegevoegd of eruit worden verwijderd) - is veel sneller! - ondersteunt ware zoekacties \"op afstand gebaseerd\", d.i. geeft alle punten terug binnen een straal vanaf een zoekpunt

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: QgsRasterDataProvider::sample methode voor efficiëntt nemen van monsters van rasters op een bepaald punt
Dit is een alternatief voor de methode `QgsRasterDataProvider::identify`, die minder efficiënt is, maar wel krachtiger

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Nieuwe aanroep voor geometrie API om een gebogen subtekenreeks te rug te geven
Nieuwe PyQGIS API is toegevoegd om het eenvoudiger te maken een subtekenreeks te halen uit een geometrie LineString/Curve:

`QgsCurve::curveSubstring -  Geeft een nieuwe boog terug die een subtekenreeks van een boog weergeeft, vanaf een beginafstand en eindafstand.`

Indien Z- of M-waarden aanwezig zijn, zal de uitvoer Z en M worden geïnterpoleerd met behulp van de bestaande punten Z- en M-waarden. De methode handelt ook gebogen geometrieën af zonder verlies of segmentatie.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: sip Module API wijzigingen
Vanwege bovenliggende wijzigingen binnen de bibliotheek PyQt/sip library, is de aanbevolen manier om deze module te importeren gewijzigd in QGIS 3.4. Voor maximale portabiliteit, in plaats van direct aan te roepen: `import sip`, zouden plug-ins in plaats daarvan moeten gebruiken: `from qgis.PyQt import sip`. Gebruik van deze nieuwere stijl van importeren zal ervoor zorgen dat de code correct werkt in alle platforms en functioneel blijft in toekomstige versies van QGIS.
### Mogelijkheid: Python vectorgegevensproviders
Ontwikkeling van de API, een provider voor monsters en testen maken het mogelijk een vectorgegevensprovider te maken in pure Python.

[![image36](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)

Dit werd mogelijk gemaakt door Good will

Deze mogelijkheid werd ontwikkeld door Alessandro Pasotti
## 3D-objecten
### Mogelijkheid: Verbeterde navigatie
Dit zal het midden van de cameraweergave bijwerken als de camera beweegt. Hiervoor was het midden van de weergave altijd op hoogte nul, wat betekende dat met verder weg gelegen terrein vanaf hoogte nul optillen en roteren van de camera vreemd zou aanvoelen, omdat het middelpunt ver weg zou zijn.

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

Het voordeel is dat de 3D-lijnen niet hun Z-coördinaat verliezen, wat momenteel het geval is met \"gewoon\" 3D-renderen na bufferen.

Het nadeel is dat de lijnen niet breed kunnen zijn (ondersteund in Qt3D vanaf 5.10, maar zelfs dat renderen zal geen nette verbindingen/einden hebben) en alleen omgevingskleur wordt gebruikt uit het materiaal.

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
