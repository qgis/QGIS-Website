---
HasBanner: false
draft: false
releaseDate: 18-06-2021
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.20
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.20{#changelog320 }
![image1](images/projects/712c5f48a25ce79a413e9cc34336e05100b7f0c1.png)

Datum uitgave 18-06-2021

QGIS 3.20 Odense heeft een welkomstscherm dat een gedeelte weergeeft van [de vroegste kaart](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object80440/en/) van Denemarken, de op twee na grootste stad, [Odense](https://en.wikipedia.org/wiki/Odense) uit 1593. De kaart werd gepubliceerd door [Georg Braun](https://en.wikipedia.org/wiki/Georg_Braun) (1541-1622) in het werk *Civitates orbis terrarum* (Steden van de wereld). Georg Braun’s kaarten zijn allemaal prachtig en waren, voor die periode, geproduceerd op een hoog cartografisch niveau. *Civitates orbis terrarum* was lange tijd de belangrijkste bron voor kaarten van steden van de wereld, zoals [Parijs](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62269/en/), [Londen](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62684/en/), [Mexico Stad](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62261/en/) en [Aden](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62257/en/).

De naam Odense betekent letterlijk \“Odins tempel\”, en de plaats zou oorspronkelijk een altaar zijn geweest voor de heidense god Odin. Aan de linkeronderzijde van de kaart ziet u de ruïnes van een groot ringvormig fort uit de Vikingtijd, dat in Denemarken werd geconstrueerd door de Deense Vikingkoning [Harald Bluetooth](https://en.wikipedia.org/wiki/Harald_Bluetooth) (gestorven in c. 985/86). Het ringvormige fort in Odense is genaamd [Nonnebakken](https://odensebysmuseer.dk/nonnebakken-the-viking-ring-fortress-in-time-and-space/?lang=en).

Deze uitgave introduceert een schat aan subtiele wijzigingen en bijwerkingen voor de stabiliteit, die de meest nieuwste mogelijkheden, die werden geïntroduceerd in recente uitgaven van QGIS, versterken. Opgenomen in deze uitgave zijn heel veel verbeteringen voor het beheren van gegevens, met enkele geavanceerde wijzigingen voor het beheer en weergeven van CRS-systemen en informatie voor projecties. Naast deze verbeteringen voor het beheer van CRS plaatsen de basisondersteuning voor de epoch van coördinaten voor dynamische CRS-systemen en integriteitswaarschuwingen voor geavanceerde nauwkeurigheid, QGIS 3.20 ferm aan de leidende zijde van praktijken voor GIS en het beheren van gegevens voor systemen met hoge nauwkeurigheid.

Aanvullend kunnen gebruikers verbeterd beheer van metadata en afhandeling voor bepaalde gegevens en typen metadata verwachten. Een ander noemenswaardig punt is de eigen integratie van de geocoderingsservice [Nominatim](https://nominatim.org/), die het voor gebruikers mogelijk maakt locaties en adressen te zoeken met gegevens uit het project OpenStreetMap, direct vanuit de Locatiebalk van QGIS.

De gemeenschap van QGIS heeft ook een stijging gezien van de activiteiten in de [QGIS HUB](https://plugins.qgis.org/). Alsook bij de Virtuele QGIS Open Dagen, met de [Cutting Edge Open Dag](https://github.com/qgis/qgis/wiki/QHF-May-2021) die een aantal demonstraties liet zien van hoogwaardige functionaliteit voor QGIS die werd geïntroduceerd in meer recente uitgaven.

We willen nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://www.qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende leden](https://www.qgis.org/nl/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Aanvullende opties voor openen van attributentabellen
De eerder beschikbare sneltoetsen voor het openen van attributentabellen, met filters om alleen de geselecteerde items of in het kaartvenster zichtbare items, weer te geven, zijn geïntegreerd in de werkbalk Menu om hun gebruiksgemak te faciliteren en de ervaring van de gebruiker te verbeteren, speciaal bij het werken met grote gegevenssets.

![image2](images/entries/571fda8da2dc36cc6032354e4249ac9f642aad02.webp)

Deze mogelijkheid werd ontwikkeld door [Raymond Nijssen](https://github.com/raymondnijssen)
### Mogelijkheid: Grootte instellen voor alle kolommen in de attributentabel
De bestaande mogelijkheden voor \"Breedte instellen\" en \"Autom. grootte\" voor kolommen zijn uitgebreid voor het aanpassen van de grootte voor een veld voor alle kolommen.

Dit omvat ook de mogelijkheid om een vaste breedte in te stellen of om \"Automatische grootte\" voor alle kolommen toe te passen. Deze acties zijn beschikbaar in het contextmenu van de kop in de attributentabel, dat toegankelijk is door met rechts te klikken op de kop van een veld.

![image3](images/entries/424dea8c61279f20c7f3ca5bf3cd13c21f999987.webp)

Deze mogelijkheid werd ontwikkeld door [Ben Wirf](https://github.com/benwirf)
### Mogelijkheid: Configuraties voor authenticatie im-/exporteren gemakkelijker gemaakt
Vanaf QGIS 3.20 kunnen gebruikers nu configuraties voor authenticatie gemakkelijker exporteren en importeren via een paar acties in het paneel voor instellingen voor authenticatie van QGIS. Geëxporteerde configuraties kunnen met een wachtwoord worden beveiligd om het lekken van gevoelige informatie te vermijden.

Dit vergroot enorm het gemak voor het delen van verscheidene configuraties voor authenticatie over meerdere gebruikers van QGIS, speciaal als het aankomt op meer complexe methoden voor configuratie, zoals Oauth2.

Dit werd mogelijk gemaakt door Ville d\'Yverdon-les-Bains

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Tijdbeheer
### Mogelijkheid: Stappen navigatie Tijdbeheer
Een optie voor stappen voor navigatie in Tijdbeheer voor \"bron tijdstempels\" is toegevoegd aan het beheer van Tijdbeheer. Indien geselecteerd, zorgt dit ervoor dat de navigatie voor Tijdbeheer door alle beschikbare tijdsperioden in lagen van het project stapt. Dit is nuttig als een project lagen bevat met niet-doorlopende beschikbare tijden, zoals een service voor WMS-T die afbeeldingen verschaft die beschikbaar zijn op onregelmatige datums. Deze optie maakt het voor gebruikers mogelijk alleen door tijdsbereiken te stappen waarvoor de volgende beschikbare afbeelding wordt weergegeven.

![image4](images/entries/09959743079b809c8969b49f5fbbffe774aeb644.gif)

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720707

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeterde instellingen voor WMS-T
Instellingen voor WMS-T werden vereenvoudigd en besturingselementen werden geïntroduceerd om het gemakkelijker te maken om voor sommige providers de gewenste tijd te selecteren.

Wijzigingen werden gemaakt om de volgende doelen te bereiken:
- Duidelijker maken wat elk van de besturingselementen van de instellingen exact doet
- De interactie en relaties tussen de verschillende instellingen helderder maken
- Duidelijk maken welke instellingen van toepassing zijn, ongeacht of de laag wordt beheerd door het beheer van Tijdbeheer of de instellingen alleen relateren aan statische lagen van WMS-T
- Voor servers die een niet-doorlopende set van items voor datum-tijd weergeven, wordt, in plaats van een bereik van datums, een combinatievak verschaft dat het handmatig invoeren van geldige datums vervangt

Voorbeeld van instellingen voor een server die een bereik aan beschikbare datums weergeeft:

![available](images/entries/5959d2a149797fdbd8108653dad86b4ba93d54a1.gif)

Voorbeeld van instellingen voor een server die alleen een lijst van beschikbare items datetime weergeeft:

![datetime](images/entries/f8d2510c5cdf7241f1ed61a9bdd0211f1d6fb0f7.gif)

![image7](images/entries/f8ab8c722dde210f851f838752916bfe76147420.webp)

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720707

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Horizontaal navigeren Tijdbeheer met muiswiel
Horizontaal scrollen met het muiswiel (indien ondersteund) met de cursor in het kaartvenster stelt gebruikers in staat te navigeren, of \"te schrobben\", de schuifbalk voor navigatie in Tijdbeheer naar achteren en voorwaarts

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Kaartgereedschap
### Mogelijkheid: Integratie Nominatim geocodering
De Nominatim Geocoder is nu standaard op eigen wijze geïntegreerd in QGIS! QGIS verschaft een Nominatim locatiefilter, als ook het gereedschap voor Processing \"Bulk geocodering Nominatim\" voor het in batch geocoderen van locaties.

*Nominatim locatiefilter*

De widget Locatiebalk in QGIS (standaard, een zoekbalk in de linkerbenedenhoek CTRL+K) ondersteunt nu zoekacties voor geocode van Nominatim door het voorvoegsel \'\>\' te gebruiken.

Gebruikers kunnen nu zoeken naar locaties met de indeling `> zoektekst` in de Locatiebalk en er zal een selectie van resultaten worden gegeven. Selecteren van een zoekresultaat zal het bereik van het kaartvenster plaatsen op die locatie.

*Bulk geocodering Nominatim*

In aanvulling daarop is een nieuw algoritme \"Bulk geocodering Nominatim\" toegevoegd aan de Toolbox van Processing in QGIS, onder Vector algemeen, wat gebruikers in staat stelt meerdere locaties in één keer te geocoderen.

Nominatim is een service voor geocodering die gegevens gebruikt van het project OpenStreetMap. Beperkingen voor gebruike en limieten - 1 query per seconde - pas het toe in lijn met de beleidsregels voor gebruik van de OpenStreetMap Foundation (OSMF), en de gegevens worden verschaft onder de termen van de licentie ODbl. Aanvullend, query's naar de service van Nominatim mogen informatie voor telemetrie bevatten.

Standaard opnemen van deze fantastische service voor geocodering zou niet mogelijk zijn geweest zonder de generositeit en deelname van de OSMF.

![image8](images/entries/bd1b0900b9e2b2756dbc9c9aa90f8b8f34ef166e.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Gebruikersinterface
### Mogelijkheid: Verbeteringen aan dialoogvenster Geschiedenis van Processing
Het dialoogvenster Geschiedenis van Processing heeft een reeks verbeteringen aan de gebruikersinterface ondergaan, inclusief het opnieuw groeperen van algoritmes in structuren van betekenisvolle mappen en gebruik makend van pictogrammen van individuele algoritmes. Zoeken naar een algoritme dat u vorige week hebt uitgevoerd was nog nooit zo gemakkelijk!

![image9](images/entries/4e8fa82827363fa9b82ed5b79c1b84f12a220465.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Pictogrammen voor kaartlagen in het dialoogvenster Expressiebouwer
Het dialoogvenster Expressiebouwer geeft nu pictogrammen voor kaartlagen weer naast de lijst met lagen onder de oudergroep \'Lagen\'. Dit versnelt het zoeken in de lijst en verschaft aanvullende context.

![image10](images/entries/2128b48e7c773959e0305181db1b4da9c917889d.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: SVG browser filteren
De SVG browser-interface ondersteunt nu filteren gebaseerd op eenvoudige tekst, wat het voor gebruikers mogelijk maakt de beschikbare SVG-afbeeldingen te filteren, gebaseerd op een opgegeven zoektekst.

![image11](images/entries/3e4dfa0a3e25db1821ae914eeec5c34d7c125ebf.gif)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
## Symbologie
### Mogelijkheid: Geïnterpoleerde lijn type symboollaag voor vectorlagen
QGIS verschaft een nieuw type symboollaag \"Geïnterpoleerde lijn\", wat resulteert in het renderen van een in kleur en/of breedte variërende lijn.

Dit symbool is in grote mate te configureren en geeft gebruikers de mogelijkheid om attributen of expressies te associëren met elk uiteinde van de lijn of boog, naast andere opties voor configuratie. Waarden worden geïnterpoleerd langs de lijn tussen uiteinden. Kleur wordt geconfigureerd met een widget voor kleurverloop.

![image12](images/entries/ebfd1d989cdb0d61ab56ab5a629a82a716446666.gif)

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://github.com/vcloarec)
### Mogelijkheid: Het enkele lijnsymbool afbreken
Een optie om het begin en einde van enkele lijnsymbolen af te breken werd toegevoegd, wat het bij het renderen van de lijn mogelijk maakt de eerste en laatste gedeelten van een lijn op een door de gebruiker gedefinieerde afstand af te breken. Dit is nuttig bij het maken van complexe symbolen waar een lijnlaag geen lagen met markeringssymbolen, die zijn geplaatst op begin- of eindposities van een object lijn, zou moeten overlappen, zoals bij routes voor transport. De afstand voor het afbreken ondersteunt een bereik aan eenheden, inclusief een percentage van de gehele lengte van de lijn en mag ook worden geconfigureerd als een data-bepaalde eigenschap.

Een voorbeeld voor het gebruik van deze functionaliteit:

![image13](images/entries/f0cad8bbc2de6c44b22c4875c45ed6e24e9f4bf6.webp)

![image14](images/entries/14f48f5bcc891d1c97a8b187f53bb21c6dd6dff6.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe renderer \"Ingebedde symbolen\" met ondersteuning voor stijlen voor OGR-objecten
Een nieuwe renderer \"Ingebedde symbolen\" is toegevoegd om stijlen van OGR-objecten weer te geven, wat het voor QGIS mogelijk maakt om automatisch gegevens van bepaalde gegevenstypen te symboliseren die geïntegreerde stijlinformatie hebben, zoals KML- of TAB-bestanden.

Deze mogelijkheid implementeert [QEP-209](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/209)

Ondersteuning zou automatisch moeten zijn uitgebreid naar alle stuurprogramma's voor GDAL die de API voor stijl van OGR-objecten implementeren.

Momenteel wordt alleen conversie van lijnsymbolen ondersteund, maar ondersteuning voor punt- en polygoonsymbolen is in ontwikkeling.

![image15](images/entries/44767fa890705c09d9c4b21b998807c7999ddde4.gif)

Deze functionaliteit ondersteunt ook de directe conversie van renderers Ingebedde symbolen naar renderers Categorieën of Regel-gebaseerd. Dit stelt QGIS in staat om automatisch categorieën of regels te maken die symbologie definieert die is gebaseerd op de relevante object-ID's:

![image16](images/entries/3a408fbcff1ee8d5889c3fe30c0d9d831b050698.gif)

![image17](images/entries/be73e288ed1f46860868a6ae49e7d1f8604082b9.webp)

Deze mogelijkheid werd mogelijk gemaakt door de QGIS Denmark gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe vormen en eindstijlen voor ellipsmarkeringen
Verscheidene nieuwe vormen - semi-boog en pijltekens - werden toegevoegd aan de symboollagen voor ellipsmarkeringen, als ook een instelling om de eindstijl aan te passen voor ellipsvormen met alleen lijnen.

![image18](images/entries/3b34a6b8ceb5cad5a423a10562511457c0c21396.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Eindstijl instellen voor eenvoudige markeringen
QGIS maakt het nu mogelijk om de afgeronde eindstijl (of lijnuiteinde) in te stellen voor eenvoudige markering-symboollagen, wat nuttig is voor de alleen-lijn-symbolen zoals kruis- en pijlmarkeringen, waar het een voordeel heeft ronde uiteinden te gebruiken in plaats van vierkante uiteinden.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Afgeronde eindstijl instellen voor ellipsmarkering-symboollagen
Ellipsmarkeringen bevatten nu ook ondersteuning voor het aanpassen van de afgeronde eindstijlen (lijnuiteinden)

![image19](images/entries/5d01d2759751cf797586797a74beea3c9561677d.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Variabele voor polygoonringen \@geometry_ring_num
Een nieuwe variabele, `@geometry_ring_num`, is toegevoegd voor data-bepaalde opmaak bij het renderen van polygoonringen. De variabele is altijd bereikbaar als een omtrek van een polygoon wordt gerenderd, zoals een enkele lijn of markeringslijn. Deze data-bepaalde eigenschap zal op 0 worden ingesteld voor de buitenste ring, en overeenkomstig verhoogd worden (1, 2, 3\… etc) voor opeenvolgende binnenste ringen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Labelen
### Mogelijkheid: Vulsymbolen voor achtergronden van labels
Achtergronden voor labels kunnen nu vulsymbolen gebruiken voor de vormen rechthoek, vierkant, cirkel en ellips.

Dit breidt de reeds eerder aanwezige mogelijkheid voor deze achtergronden uit om eenvoudige vulling en lijnen te gebruiken. En geeft tevens de mogelijkheid om de volledige mogelijkheden voor symbologie in QGIS voor het renderen van achtergronden te verhogen, inclusief het gebruiken van \"opgeslagen stijlen\".

![image20](images/entries/5698488e5fae8bdd876dfe754b56bfad0c3fd950.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Instellingen voor Meng-modus voor label Tekstballonnen
Labels Tekstballonnen mogen nu verhoogd worden met de geavanceerde meng-modi van QGIS

![image21](images/entries/4dd84f1e0b5ec295da997ffd84fb15b2cae25b13.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Lijnlabels verankeren aan gehele lijn
In eerdere versies, wanneer een ankerpositie voor een lijnlabel werd berekend, zou QGIS alleen rekening houden met het zichtbare bereik van het object. Dit beïnvloedde in sommige gevallen de verwachte labelpositie en een nieuwe instelling \"Gehele lijn gebruiken\" stelt gebruikers in staat het gedrag te configureren. Overeenkomstig hun wensen, zodat rekening wordt gehouden met het gehele object voor het plaatsen van het label, in plaats van slechts met het gedeelte van het object dat momenteel zichtbaar is.

![image22](images/entries/1a1788cc98f860e53b8ba3b1b2d7ad5b0969179f.webp)

Dit werd mogelijk gemaakt door Stadt Zürich

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Radius hoek tekstballon
Stijlen voor tekstballonnen ondersteunen nu afgeronde hoeken door de introductie van een optie \"Radius hoek\", die resulteert in de mogelijkheid om gemakkelijk visueel aantrekkelijke ontwerpen te maken.

![image23](images/entries/9c3d5b37de37e8db7168e68229a6bb3cd02138e6.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Tekstballonnen (speech bubble)
Een nieuwe \"tekstballon\", of speech bubble-stijl voor labels wordt verschaft.

![image24](images/entries/7dcb80eacfb6e10dc6b6b05a160421a93ee78d14.webp)

Dit werd mogelijk gemaakt door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Tekstballon stijl Gebogen lijn
Een nieuwe stijl voor tekstballonnen \"Gebogen lijn\" is toegevoegd voor het maken van cartografisch aantrekkelijke tekstballonnen met gebogen lijnen tussen de labels en objecten

Opties bevatten:
- Selecteren van een specifieke richting voor de boog (met de klok mee of tegen de klok in)
- Optie voor automatische oriëntatie die de optimale oriëntatie bepaalt voor elk individueel label
- Beheer over de hoeveelheid buiging die wordt toegepast op de lijnen van de tekstballon.

![curved-callout](images/entries/fd1a05c782e4e2e487a5ed876dc6c396269b0acf.gif)

![image26](images/entries/42e4e2dd600bceda0ff426996577761d9e8b1638.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Begin- of eindpunten vastgezette tekstballon accentueren
Wanneer de optie \"Vastgezette labels weergeven\" is ingeschakeld, zal QGIS nu ook begin- of eindpunten van vastgezette tekstballonnen accentueren. Dit maakt het voor gebruikers mogelijk onmiddellijk te zien welke punten voor tekstballonnen handmatig zijn neergezet in relatie tot die welke automatisch zijn geplaatst.

![image27](images/entries/e1de38ee6adde2a016b8d4550111ff766211f0f7.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch maken van hulpvelden voor tekstbalonnen
QGIS beheert nu automatisch het maken van hulpvelden voor tekstballonnen bij het proberen om interactief een begin- of eindpunt van een tekstballon te verplaatsen, waardoor de ervaring voor de gebruiker voor het verplaatsen van een tekstballon exact hetzelfde gedrag geeft als bij het verplaatsen van een label, hiermee voorkomend dat het systeem gebruikers dwingt om vooraf hulpvelden te moeten maken.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Snappen van tekstballon
Bij het interactief verplaatsen van een lijn van een tekstballon, zal het ingedrukt houden van de Shift-toets er voor zorgen dat de tekstballon wordt gesnapt aan hoeken met verhogende stappen van 15 graden

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Sneltoets voor schakelen labellagen
Een actie met een sneltoets om het labelen te schakelen is toegevoegd aan het contextmenu van vectorlagen in de laagpanelen. Dit maakt het voor labels mogelijk om snel in- of uitgeschakeld te worden, zonder de configuratie voor het label te verliezen. Als een laag nooit is geconfigureerd voor labels en de actie wordt geselecteerd, zal QGIS proberen een eenvoudige configuratie voor labelen toe te passen op de laag met standaard parameters.

![image28](images/entries/023bb952056e1d7f41e7a06590000f17b76d6d45.gif)

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720707

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Data-bepaalde begin- en eindpunten tekstballon
Lijnen voor tekstballonnen mogen nu data-bepaalde begin- en eindpunten hebben, nuttig voor het handmatig beheren van de exacte plaatsing voor individuele lijnen voor tekstballonnen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Interactief verplaatsen van tekstballonnen met het gereedschap Label verplaatsen toestaan
Deze wijziging stelt het interactieve gereedschap \"Label verplaatsen\" in staat ook eindpunten van tekstballonnen te verplaatsen, wanneer de tekstballon een data-bepaald veld voor origine of doel heeft ingesteld.

![image29](images/entries/8bb0e3614666059f3fe66065173f207d335d3800.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Puntenwolken
### Mogelijkheid: Ondersteuning voor gegevenssets op afstand (EPT)
Gegevenssets voor puntwolken die zijn verwerkt naar [indeling EPT](https://entwine.io/entwine-point-tile.html) kunnen worden geladen vanaf http(s)-servers op afstand, soortgelijk aan de werkwijze voor raster-/vectortegels. Op deze manier is het mogelijk toegang te verkrijgen tot zeer grote gegevenssets voor puntwolken zonder ze eerst als LAS/LAZ-bestanden te moeten downloaden. De indeling EPT is geoptimaliseerd voor tegels en streamen, dus downloadt QGIS alleen kleine hoeveelheden gegevens die nodig zijn voor het weergeven van de huidige weergave en resolutie. Dit werkt in zowel weergave 2D als 3D.

Wanneer u gegevenssets voor puntwolken in de indeling LAS/LAZ hebt, kunnen deze worden geconverteerd naar EPT met behulp van [Entwine](https://github.com/connormanning/entwine) of [Untwine](https://github.com/hobu/untwine) (ook verschaft met QGIS).

Hoe te gebruiken: in Databronnen beheren \> tab Puntenwolk \> selecteer \"Protocol\" als het type bron en voer de URL van de gegevensset in (normaal gesproken eindigend met \"ept.json\").

U kunt het testen met [USGS LiDAR data](https://usgs.entwine.io/) - gebruik eenvoudigweg de link uit de kolom \"EPT\" van een van de gegevenssets. Sommige eindpunten voor de voorbeelden omvatten:
- [Chicago](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_IL_4County_Cook_2017_LAS_2019/ept.json)
- [Mount Baker](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_WA_MtBaker_2015_LAS_2017/ept.json)
- [Denemarken](https://na-c.entwine.io/dk/ept.json)
- [Nederland AHN2](https://na-c.entwine.io/ahn/ept.json)

O ja, elke gegevensset voor puntwolken die QGIS laadt wordt eerst verwerkt naar EPT (zoek naar de submap \"ept_XXX\" waar uw originele gegevens zich bevinden), dus is het mogelijk om alleen die map \"ept_XXX\" te kopiëren naar een http(s)-server en u bent klaar om deze mogelijkheid te gebruiken.

![image30](images/entries/50ed450146655afb5c6ae68f0ead344cfc9eea73.webp)

Dit werd mogelijk gemaakt door [Hobu](https://hobu.co/)

Deze mogelijkheid werd ontwikkeld door [Belgacem Nedjima (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Afdruklay-outs
### Mogelijkheid: Optie \"Naar statische tekst converteren\"
Bij het gebruiken van dynamische of op expressie-gebaseerde labels kunnen gebruikers nu de optie \"Naar statische tekst converteren\" selecteren die is toegevoegd aan het keuzemenu naast \"Expressie invoegen/bewerken…\", in de widget voor eigenschappen van de lay-out voor het label.

Deze optie zal dynamische delen van de inhoud van een label evalueren en vervangen door hun huidige waarden.

Dit geeft een gemakkelijke manier om dynamische labels te wijzigen naar statische, zodat gebruikers, indien nodig, de resultaten handmatig aan kunnen passen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeteringen aan voorbeeldweergave lagen XYZ in kaartitems
Afhandelen van lagen XYZ, die als voorbeeld worden weergegeven in kaartitems van de lay-out, is verbeterd om er voor te zorgen dat hun zoomniveaus voor de tegels overeenkomen met die van de geëxporteerde lay-out tijdens het in-/uitzoomen in het dialoogvenster voor het ontwerpen van de lay-out. Gebruikers kunnen nu gemakkelijker de plaatsing van hun items verfijnen (labels, legenda, afbeeldingen, etc.) tegen een kaartvoorbeeld dat overeenkomt met de bedoelde uitvoer.

Dit werd mogelijk gemaakt door Kanton Zug - Amt für Raum und Verkehr (ARV)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Expressies
### Mogelijkheid: Functie length3D
Een functie \"length3D\" is toegevoegd voor het teruggeven van de 3D-lengte van een type geometrie LineGeometry. Deze berekent de Cartesiaanse 3D-lengte van een geometrie-lijnobject. Als de geometrie geen 3D-lijnobject is, geeft het de 2D-lengte terug.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Uitgebreide arrayfuncties voor expressies
De volgende expressies voor arrays werden toegevoegd:
- array_count
- array_prioritize
- array_replace

Dit werd mogelijk gemaakt door Canton of Luzern

Deze mogelijkheid werd ontwikkeld door [Damiano Lombardi](https://github.com/domi4484)
### Mogelijkheid: Type MIME functie voor expressie
De nieuwe `mime_type( bytes )` functie voor expressie geeft het Type MIME, of [Media type](https://en.wikipedia.org/wiki/Media_type), van een ingevoerd bytes-object terug

![image31](images/entries/c6aa4689915ec3337efac4284ed39a15e8cadddf.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Digitaliseren
### Mogelijkheid: Attributen van de grootste geometrie bij samenvoegen selecteren
Een knop om attributen van de grootste geometrie te selecteren is toegevoegd aan het dialoogvenster voor bevestiging bij het gebruiken van de bewerkingsgereedschappen voor samenvoegen van objecten voor polygoon- en lijnlagen.

![image32](images/entries/e27a6a42f878cdfec87021d53241457aa1d8845f.webp)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Stromende modus Digitaliseren
Als de modus voor stromend digitaliseren actief is, worden punten automatisch toegevoegd, de verplaatsing van de muiscursor volgend, wat een \"vrije hand tekenen\" type ervaring geeft.

Gebruiken van de \"R\"-toets tijdens bewerkingen voor digitaliseren zal schakelen tussen stromend digitaliseren en normaal (of cirkelvormige reeksen) digitaliseren.

Werkt met meerdere kaartgereedschappen, inclusief het maken van nieuwe lijn- of polygoonobjecten, ring toevoegen, deel toevoegen, opnieuw vormen, objecten splitsen, delen splitsen, en meer.

![image33](images/entries/854b65b029335216c7e37c89168389f945e62fe2.gif)

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720707

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe optie snappen aan \"Lijn eindpunten\"
Indien ingeschakeld snapt deze modus voor snappen alleen aan het begin- of eindpunt van lijnen. Bij snappen op een polygonenlaag zal alleen aan het eerste punt in ringen worden gesnapt.

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720707

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Punten per polygoon selecteren
Gebruikers kunnen nu de ALT-toets gebruiken om tijdens digitaliseren punten per polygoon te selecteren.

Dit zou de gebruikerservaring voor het selecteren van specifieke punten met het gereedschap Punten moeten verbeteren, en verkleint de noodzaak voor het meerdere malen gebruiken van de functies SHIFT of CTRL om punten aan/uit de huidige selectie toe te voegen en te verwijderen.

Dit vermindert ook de noodzaak om het kaartvenster creatief te moeten draaien om punten uit te lijnen voor het selecteren, en verschaft een verbeterd bewerkingsproces, zoals bij het selecteren van de punten van slechts één zijde langs een gebogen weg.

Deze functie ondersteunt de volgende bewerkingen voor gebruik:
- Alt+klik met gereedschap Punten voor beginnen van digitaliseren van een polygoon.
- Elke volgende klik voegt een nieuw punt toe aan de polygoon van elastiek.
- Backspace/ delete verwijdert het laatste toegevoegde punt aan het elastiek.
- Esc annuleert de modus voor selecteren van de polygoon, net als backspace/delete voor alle punten van het elastiek.
- Klik met rechts voltooid het digitaliseren van de polygoon en selecteert alle punten binnen de polygoon van elastiek.

![image34](images/entries/d4a70011e9064862c99827f5b940805dd2d45182.gif)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
## Gegevensbeheer
### Mogelijkheid: Waarschuwingspictogram voor boom van lagen voor lagen met onnauwkeurigheden voor CRS
Een nieuwe optie \"Waarschuwingen voor nauwkeurigheid CRS voor lagen weergeven in legenda van project\" is verschaft die, indien geselecteerd, een nieuw waarschuwingspictogram zal weergeven dat lagen identificeert met een CRS dat is geïdentificeerd met problemen voor nauwkeurigheid.

Voorbeelden van laag-nauwkeurige lagen zouden die kunnen bevatten met een dynamisch CRS zonder beschikbare epoche voor coördinaten, of een CRS dat is gebaseerd op een datum-ensemble met een nauwkeurigheid die de door de gebruiker ingestelde grenswaarde overschrijdt.

Deze optie is standaard uitgeschakeld, en ontworpen voor gebruik door ingenieurs, BIM, en andere industrieën waar onnauwkeurigheden op het niveau van meter/submeter erg gevaarlijk zijn.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Basisondersteuning voor dynamische epoche voor CRS-coördinaten
Basisondersteuning voor de epoche van coördinaten voor dynamisch (niet plaatvast) CRS is toegevoegd in lijn met de relevante bijwerkingen aan [GDAL](https://github.com/OSGeo/gdal/pull/3810).

QGIS heeft ondersteuning toegevoegd voor het respecteren van de bron- of doel-epoche van de coördinaten bij het transformeren naar of vanuit een dynamisch CRS.

Als een dynamisch CRS naar een transformatie naar dynamisch CRS met verschillende epochen wordt geprobeerd, wat momenteel niet wordt ondersteund door PROJ, zal een waarschuwingsbericht voor de gebruiker worden weergegeven die hem in kennis stelt van het feit dat de resultaten misleidend kunnen zijn en niet zouden moeten worden gebruikt voor werk waar een hoge mate van nauwkeurigheid is vereist.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeteringen aan projectinformatie
Verscheidene verbeteringen zijn gemaakt aan de afhandeling en weergave van projectinformatie in QGIS, inclusief:
- De toevoeging van een API om bewerkingsdetails voor PROJ voor CRS-en op te halen
- De mogelijkheid om uitgebreide informatie weer te geven over het CRS van een laag op de tab voor informatie over de laageigenschappen, inclusief waarschuwingen voor nauwkeurigheid
- De toevoeging van een variabele `@map_crs_projection`, voor het ophalen van een vriendelijke naam voor de projectie van een kaart (bijv. \"Albers Equal Area\")

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Waarschuwingen voor CRS datum-ensemble
QGIS geeft nu een waarschuwing weer in de widget voor het selecteren van de projectie als een CRS wordt geselecteerd dat is gebaseerd op een datum-ensemble, die de gebruiker waarschuwt dat er een ingewortelde onnauwkeurigheid in het geselecteerde CRS bestaat.

![image35](images/entries/b99e932e308d3b6d2b3868a88f3528386adb3d1f.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Metadata van lagen behouden in export van vectorbestanden
Een keuzevak \"Metadata laag vasthouden\" is toegevoegd aan het dialoogvenster voor het exporteren van vectorbestanden. Indien geselecteerd zal metadata van de laag, die aanwezig is in de bronlaag, worden gekopieerd en opgeslagen in het doelbestand.

Deze functionaliteit is standaard ingeschakeld en zorgt ervoor dat de metadata op de juiste wijze wordt overgebracht naar de nieuw gemaakte items, wat in het bijzonder effectief is bij het gebruiken van de indeling GPKG.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Opmerkingen voor lagen
QGIS ondersteunt nu \"opmerkingen voor lagen\", die kunnen worden gemaakt met de actie \"Opmerkingen laag toevoegen\" in het contextmenu van de laag.

Deze opmerkingen worden per laag, per project opgeslagen. Zij kunnen worden gebruikt als een plaats om belangrijke berichten voor gebruikers van het project op te slaan, zoals Nog te doen-lijsten, verwerkings- of beheersinstructies, of elke andere normale op tekst gebaseerde metadata.

Een pictogram met een kladblok in het paneel Lagen identificeert lagen die deze opmerkingen als bijlage hebben. Klikken op het pictogram kladblok opent de opmerking om die te bewerken.

Deze mogelijkheid werd besproken in [QEP-206](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/206)

Deze opmerkingen kunnen worden gekopieerd en geplakt met de normale methodologie voor kopiëren/plakken voor het overbrengen van stijlen tussen lagen in QGIS.

Opmerkingen voor lagen worden ook ondersteund door en opgeslagen in QML- (QGIS Style) en QLR- (QGIS Layer Definition) bestanden.

![image36](images/entries/250d188c3987a1247b9e3a414d5d72c9c681b0ad.webp)

Dit werd mogelijk gemaakt door Alta Ehf

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch laden van metadata uit .shp.xml
QGIS zal nu automatisch ESRI-metadata laden en converteren die is opgeslagen in een bijbestand .shp.xml. Waar gegevens uit shapefile worden geladen en deze ebstanden voor metadata zijn aanwezig, zullen zij automatisch worden geladen, waarbij de beschikbare metadata  voor de laag overeenkomstig wordt gevuld.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch gegevens van laag vertalen van ESRI Filegeodatabases naar QGIS metadata voor de laag
Bij het laden van gegevens uit een bestand .gdb zal QGIS automatisch proberen zoveel mogelijk te vertalen van de originele ESRI-metadata ten opzichte van de metadata voor QGIS, zodat het voor onmiddellijk gebruik gereed is.

Dit werd mogelijk gemaakt door North Road / SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Domeinen voor velden lezen uit gegevenssets
Voor indelingen die de ingebedde definitie voor velddomeinen ondersteunen (momenteel GPKG en GDB), converteert QGIS automatisch het ingebedde velddomein naar de equivalente configuratie voor de bewerker van QGIS voor het veld.

Dit betekent dat GPKG/GDB met gecodeerde velddomeinen automatisch zullen worden geladen in QGIS met hun juiste configuratie voor de widget Waardenkaart intact, zodat gebruikers beschrijvingen voor veldwaarden zien in plaats van ruwe codes. Velden met een domein van het type bereik (min/max) zullen ook worden vertaald naar de widget Bereik voor het veld.

Dit werd mogelijk gemaakt door North Road

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Laden van lagen GPKG met type GEOMETRY toestaan
GeoPackage ondersteunt lagen met een algemeen type "geometry". Met de uitgave QGIS 3.20 is het nu mogelijk om ze te laden en het gevraagde type geometrie te specificeren bij het laden, net als met PostGIS.

![image37](images/entries/a37aab7ea49b4870a931206e88811ebabcff6546.webp)

Deze mogelijkheid werd ontwikkeld door [Marco Bernasocchi (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Ondersteuning voor offline bewerken voor veldtypen lijst tekenreeks en lijst nummer
PostGIS-gebruikers verheugt u: offline bewerken werd enigszins slimmer en kan nu veldtypen lijst tekenreeks en lijst nummer afhandelen.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Formulieren en widgets
### Mogelijkheid: Per-veld gebruiken van laatste waarden voor nieuw gemaakte objecten
Uitgebreider beheer is verschaft voor wanneer de laatst ingevoerde waarden voor velden opnieuw gebruikt zouden moeten worden bij het maken van nieuwe objecten, zodat deze functionaliteit nu onafhankelijk kan worden beheerd voor elk individueel attributenveld voor elke laag.

Historisch werd deze functionaliteit geconfigureerd met een globale optie die er voor zorgde dat ALLE veldwaarden voor ALLE lagen zouden worden onthouden en opnieuw worden gebruikt gedurende een sessie van QGIS bij het maken van nieuwe objecten.

Dit maakt fijner beheer over het gedrag van formulieren mogelijk, waar van sommige waarden gewenst wordt dat zij opnieuw kunnen worden gebruikt, maar andere zouden moeten worden opgeschoond of worden ingesteld op ene standaard waarde. gebaseerd op een expressie.

![image38](images/entries/73f699bdf27a1b3b35de96e7a233d12a49b585d9.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Widget weergave JSON
Nieuw weergavewidget om gegevens van JSON op een gebruiksvriendelijke manier weer te geven. Gegevens kunnen worden weergegeven als geaccentueerde tekst in syntaxis of als een boom.

![image39](images/entries/1061561e58e1b0807158ab415f4a13b43589d824.gif)

Dit werd mogelijk gemaakt doo [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/)

Deze mogelijkheid werd ontwikkeld door [Damiano Lombardi](http://damiano@opengis.ch)
## Legenda van laag
### Mogelijkheid: Legenda-items \"label\" voor vector
QGIS ondersteunt nu het toevoegen van legenda-items voor laaglabels, die de stijl voor het lettertype en klassen voor labelen voor vectorobjecten zullen weergeven.

Dit verschaft een legenda-item dat het voor gebruikers mogelijk maakt om expliciet objecten op de stijl van het label te identificeren, zelfs als er geen symbologie voor objecten wordt gebruikt.

Beheer van dit gedrag is toegankelijk gemaakt door een optie \"Labellegenda weergeven\" toe te voegen aan de tab Legenda van de laageigenschappen voor vector.

![image40](images/entries/89218cecca8823903e432b9cd1a38280cc5101a9.webp)

Dit werd mogelijk gemaakt door Canton of Glarus

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
## Processing
### Mogelijkheid: Optie toegevoegd om metadata voor laag op te slaan in algoritme Pakketlagen
Deze aanvullende optie verrijkt het algoritme Pakketlagen en zal de metadata voor de bronlaag kopiëren in het geopackage, zodat het als standaard metadata zal worden gebruikt voor de laag.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme Rasterlaag eigenschappen
Dit algoritme haalt basiseigenschappen voor de rasterlaag op, zoals de grootte in pixels, dimensies van pixels (kaarteenheden per pixel), aantal banden, en waarden Geen gegevens.

Het is bedoeld voor gebruik om deze nuttige eigenschappen uit te nemen om te gebruiken als de invoerwaarden voor andere algoritmes in een model, zoals het doorgeven van bestaande pixelgrootten van rasters naar een GDAL rasteralgoritme.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeterde bewerking rasteriseren met #D-ondersteuning
Het GDAL-proces rasteriseren (vector naar raster) ondersteunt nu 3D-gegevens, in zoverre dat het nu de mogelijkheid bevat om de waarde Z (hoogte) van een object te gebruiken om brandwaarden uit te nemen.

Het gebruiken van deze optie geeft aan dat een brandwaarde zou moeten worden uitgenomen uit de waarden "Z" van het object. Werkt met punten en lijnen (lineaire interpolatie langs elk segment). Voor polygonen werkt het alleen correct als de objecten plat zijn (d.i. dezelfde waarde Z bevatten voor alle punten)

Deze mogelijkheid werd ontwikkeld door [talledodiego](https://github.com/talledodiego)
### Mogelijkheid: Optie Alleen geselecteerde objecten opslaan voor algoritme Pakketlagen
Het algoritme Pakketlagen werd aangepast met ondersteuning voor het alleen opslaan van geselecteerde objecten

Deze mogelijkheid werd ontwikkeld door [Stefan Conrads](https://github.com/stefancon)
### Feature: Logniveaus voor context Processing
Een nieuwe eigenschap log level is toegevoegd aan QgsProcessingContext

Dit maakt het voor algoritmes mogelijk om hun uitvoer te verfijnen, gebaseerd op het logniveau.

De bewerking voor de opdrachtregel qgis_process heeft een schakelaar \--verbose gekregen om verbose uitvoer voor het log te kunnen maken.

Dit werd mogelijk gemaakt door Natural resources Canada Contract: 3000720411

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Opnieuw bewerken van snappen aan geometrie biedt een grote snelheidswinst
Deze ontwikkelingscyclus zag een nieuwe bewerking van de interne werking van QGIS\' algoritme geometrieën snappen, wat heeft geleid tot een significante snelheidswinst. Gegevenssets die meer dan 10 minuten konden duren om te verwerken, duren nu minder dan 10 seconden.

Dit werd mogelijk gemaakt door [SwissTierras Colombia](https://www.swisstierrascolombia.com)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Functie last_value toegevoegd aan het algoritme Samenvoegen
Het gereedschap voor Processing Samenvoegen bevat nu een functie voor samenvoegen `last_value`, die in het bijzonder nuttig is bij het werken met invoergegevens die een betekenisvolle volgorde hebben.

![image41](images/entries/77afe9dba20e9134db3a1c628c5eeebab275b87a.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Opties voor toepassing en projecten
### Mogelijkheid: Globale optie om monitoren van mappen uit te schakelen
Geeft gebruikers de mogelijkheid om handmatig standaard het monitoren van mappen in de browser uit te schakelen, en verschaft ook een mechanisme voor installaties voor bedrijven om dit potentieel ongewenst gedrag uit te schakelen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: API's voor exporteren en importeren van XML configuraties voor authenticatie
QGIS verschaft nu functies voor exporteren en importeren naar het QGIS authenticatiebeheer. Deze functionaliteit wordt nog niet weergegeven in de gebruikersinterface. Complexe configuraties voor authenticatie met veel opties, zoals OAuth2, kunnen optioneel worden versleuteld of worden opgeslagen in platte tekst om het beheren van werkstromen met authenticatie te verbeteren.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Browser
### Mogelijkheid: Aangepaste kleuren voor pictogrammen van mappen in browser
QGIS geeft gebruikers nu de mogelijkheid om een aangepaste kleur voor pictogrammen voor verschillende mappen in de browser in te stellen. Dit maakt het voor gebruikers effectief mogelijk om mappen te \"taggen\", wat helpt bij een snellere navigatie van complexe mapstructuren in de browser.

![image42](images/entries/5135bb429434786f87aca3d2deeb980ce874ae44.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Groep OWS verwijderd uit de QGIS Browser
De niet-functionele en overbodige groep \"OWS\" is verwijderd uit het paneel van QGIS Browser.

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor lijsten van gegevenstypen integer, real en integer64 in OGR toegevoegd
Aanvullende lijsten voor veldtypen zijn toegevoegd aan het stuurprogramma voor OGR voor ondersteunde gegevenstypen, zoals Geojson.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Mogelijkheid voor lezen van vectorlaag uitgebreid naar ander typen lagen
Waar de mogelijkheid voor QGIS om toegang te verkrijgen tot informatie over metadata in een laag, zoals het lezen van het bereik van een laag vanuit de metadata, eerder was beperkt tot vectorlagen, is deze functionaliteit nu uitgebreid om ook verscheidene andere typen lagen te omvatten, inclusief raster, puntenwolk, en andere.

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
## QGIS Server
### Mogelijkheid: Externe doorzichtbaarheid laag
Ondersteuning voor beheren van doorzichtbaarheid voor externe / op afstand lagen die worden geserveerd door QGIS Server

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Mogelijkheid: Te configureren Service URL
Aanvullende opties zijn toegevoegd aan QGIS Server om het antwoord GetCapabilities met betrekking tot de resultaten te verbeteren, speciaal zonder de noodzaak om verscheidene velden te voltooien in de configuratie voor het project van QGIS. Deze bijwerkingen schakelen ook veel andere opties in die kunnen worden ingesteld met een omgevingsvariabele, of door headers uit een proxy op te geven.

De volgende opties zijn toegevoegd en zullen door de server in de volgende volgorde worden opgelost:
- Waar de gedefinieerd in het project per service.
- De omgevingsvariabele `<service>_SERVICE_URL`.
- De omgevingsvariabele `SERVICE_URL`.
- De aangepaste header `X-Qgis-<service>-Service-Url`.
- De aangepaste header `X-Qgis--Service-Url`.
- Gebouwd vanuit de standaard header `Forwarded`.
- Gebouwd uit de pseudo-standaardheaders `X-Forwarded-Host` en `X-Forwarded-Proto`.
- Gebouwd vanuit de standaard header `Host` en het serverprotocol.
- Gebouwd uit de servernaam en het serverprotocol.

Deze mogelijkheid werd ontwikkeld door [Stéphane Brunner](https://github.com/sbrunner)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| compiler warning in QgsMeshDatasetGroupStore::readXml() | niet gerapporteerd | [PR #43304](https://github.com/qgis/QGIS/pull/43304) | N/B |
| QGIS Crashes with GDAL 3.3 | [#43224](https://github.com/qgis/QGIS/issues/43224) | [PR #43306](https://github.com/qgis/QGIS/pull/43306) | [PR #43323](https://github.com/qgis/QGIS/pull/43323) |
| Data corrupted when deleting field in a (specific) geopackage layer | [#42768](https://github.com/qgis/QGIS/issues/42768) | [PR #43309](https://github.com/qgis/QGIS/pull/43309) | [PR #43322](https://github.com/qgis/QGIS/pull/43322) |
| PyQGIS: WMS-T layer uri without timeDimensionExtent in it crashes QGIS | [#43158](https://github.com/qgis/QGIS/issues/43158) | [PR #43310](https://github.com/qgis/QGIS/pull/43310) | [PR #43324](https://github.com/qgis/QGIS/pull/43324) |
| Data Corruption: Failed GPKG OID/FID Over-write causes value to spill into next attribute column | [#42274](https://github.com/qgis/QGIS/issues/42274) | [PR #43311](https://github.com/qgis/QGIS/pull/43311) | [PR #43360](https://github.com/qgis/QGIS/pull/43360) |
| \"Split features\" causes data loss | [#41283](https://github.com/qgis/QGIS/issues/41283) | [PR #43328](https://github.com/qgis/QGIS/pull/43328) | [PR #43340](https://github.com/qgis/QGIS/pull/43340) |
| Foreign key constraints checks are ignored on GPKG | [#34728](https://github.com/qgis/QGIS/issues/34728) | [PR #43330](https://github.com/qgis/QGIS/pull/43330) | Niet van toepassing |
| Strange error message from SQL Query Composer in WFS client | [#42985](https://github.com/qgis/QGIS/issues/42985) | [PR #43334](https://github.com/qgis/QGIS/pull/43334) | [PR #43341](https://github.com/qgis/QGIS/pull/43341) |
| WFS 1.1.0 ExceptionReport response handling : QGIS looks for \'exceptionCode\' but in specifications it\'s \'code\' attribute | [#42196](https://github.com/qgis/QGIS/issues/42196) | [PR #43335](https://github.com/qgis/QGIS/pull/43335) | [PR #43342](https://github.com/qgis/QGIS/pull/43342) |
| Export selection from a large WFS layer fails | [#42049](https://github.com/qgis/QGIS/issues/42049) | [PR #43336](https://github.com/qgis/QGIS/pull/43336) | [PR #43343](https://github.com/qgis/QGIS/pull/43343) |
| Long (?) WKT makes delimited text layer fail on 3.16 and 3.18 | [#43256](https://github.com/qgis/QGIS/issues/43256) | [PR #43337](https://github.com/qgis/QGIS/pull/43337) | [PR #43339](https://github.com/qgis/QGIS/pull/43339) |
| Wrong SRS when reading a Postgis layer | niet gerapporteerd | [PR #43338](https://github.com/qgis/QGIS/pull/43338) | Niet van toepassing |
| Mesh data in GRIB format from ERA5 | [#41809](https://github.com/qgis/QGIS/issues/41809) | [GDAL PR 3875](https://github.com/OSGeo/gdal/pull/3875) | [GDAL PR 3877](https://github.com/OSGeo/gdal/pull/3877) |
| Two OGR provider filtered layers with same source dataset don\'t restore proper feature count / extent on project reload | [#43361](https://github.com/qgis/QGIS/issues/43361) | [PR #43372](https://github.com/qgis/QGIS/pull/43372) | [PR #43394](https://github.com/qgis/QGIS/pull/43394) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/en/home/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Data Source Manager fails to derive exact 3D geometry type for GeometryZ PostGIS tables | [#43268](https://github.com/qgis/QGIS/issues/43268) | [PR #43326](https://github.com/qgis/QGIS/pull/43326) |  |
| Attribute table conditional formatting doesn\'t work when using \$geometry is NULL | [#43252](https://github.com/qgis/QGIS/issues/43252) | Werkt bij mij wel |  |
| QgsZonalStatistics.calculateStatistics() incomplete outputs | [#43245](https://github.com/qgis/QGIS/issues/43245) | [PR #43332](https://github.com/qgis/QGIS/pull/43332) | [PR #43378](https://github.com/qgis/QGIS/pull/43378) |
| Bad Request on feed.qgis.org | [#43232](https://github.com/qgis/QGIS/issues/43232) | [PR #43333](https://github.com/qgis/QGIS/pull/43333) | Niet relevant |
| Server: WFS3/API Features - overlapping columns/content on data items as HTML pages | [#42269](https://github.com/qgis/QGIS/issues/42269) | [PR #43363](https://github.com/qgis/QGIS/pull/43363) | [PR #43380](https://github.com/qgis/QGIS/pull/43380) |
| Datum transformation using custom gsb grid for WMS Layer in QGIS Server does not work | [#43072](https://github.com/qgis/QGIS/issues/43072) | [PR #43365](https://github.com/qgis/QGIS/pull/43365) | Niet relevant |
| Server: fix unreported QGIS_OPTIONS_PATH not really working for proj | niet gerapporteerd | [PR #43366](https://github.com/qgis/QGIS/pull/43366) | Niet van toepassing |
| WFS cascade getfeatureinfo fails | [#42062](https://github.com/qgis/QGIS/issues/42062) | Werkt bij mij wel |  |
| Server standalone: fix unreported project storage not supported with -p | niet gerapporteerd | [PR #43381](https://github.com/qgis/QGIS/pull/43381) | [PR #43464](https://github.com/qgis/QGIS/pull/43464) |
| QGIS Server GetPrint: HIGHLIGHT_GEOM is not printed if map layers are configured to follow a map theme | [#34178](https://github.com/qgis/QGIS/issues/34178) | [PR #43391](https://github.com/qgis/QGIS/pull/43391) | Riskant |
| Feature count is wrong when adding features from a table with features of mixed geometries | [#43199](https://github.com/qgis/QGIS/issues/43199) | Werkt bij mij wel |  |
| Not all geometry types are found in PostGIS table with Spatial Type of Geometry | [#43186](https://github.com/qgis/QGIS/issues/43186) | [PR #43419](https://github.com/qgis/QGIS/pull/43419) | Riskant |
| Icon not updated when saving a scratch layer | niet gerapporteerd | [PR #43431](https://github.com/qgis/QGIS/pull/43431) | [PR #43463](https://github.com/qgis/QGIS/pull/43463) |
| Fix list of protocols in ssh custom configuration | niet gerapporteerd | [PR #43432](https://github.com/qgis/QGIS/pull/43432) | Niet van toepassing |
| Crash with table set to Show Visible, joins, and left open as QGIS is quit | [#43287](https://github.com/qgis/QGIS/issues/43287) | [PR #43434](https://github.com/qgis/QGIS/pull/43434) | Niet van toepassing |
| \"show label\" is disabled in widget designer but label keeps displaying in attribute form if you use tabs in the Drag and-Drop Designer and the field widget was placed in any tab | [#43103](https://github.com/qgis/QGIS/issues/43103) | [PR #43435](https://github.com/qgis/QGIS/pull/43435) | NOG TE DOEN |
| Browser adds layers to projects with a leading space | [#43129](https://github.com/qgis/QGIS/issues/43129) | [PR #43436](https://github.com/qgis/QGIS/pull/43436) | Niet van toepassing |
| saveStyleToDatabase() bug when saving more than one layer to a GPKG | [#42988](https://github.com/qgis/QGIS/issues/42988) | Werkt bij mij wel |  |
| Widget parameters not persistent for relations in D&D designer | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43468](https://github.com/qgis/QGIS/pull/43468) | Niet van toepassing |
| Rule-based rendering sometimes doesn\'t show all results | [#43181](https://github.com/qgis/QGIS/issues/43181) | [PR #43502](https://github.com/qgis/QGIS/pull/43502) | Riskant |
| Fix unreported missing raster band stats in info panel | niet gerapporteerd | [PR #43507](https://github.com/qgis/QGIS/pull/43507) |  |
| Raster calculator does not create/store statistics for output rasters | [#42835](https://github.com/qgis/QGIS/issues/42835) | [PR #43512](https://github.com/qgis/QGIS/pull/43512) | Geen prioriteit |
| Attribute Form Value Relation Doesn\'t Respect Column Default | [#41951](https://github.com/qgis/QGIS/issues/41951) | Werkt bij mij wel |  |
| Attribute table in form view can display \"ghost\" attributes | [#43477](https://github.com/qgis/QGIS/issues/43477) | [PR #43533](https://github.com/qgis/QGIS/pull/43533) | Geen prioriteit |
| PG identity default clause issue | <https://lists.osgeo.org/pipermail/qgis-user/2021-June/048983.html> | [PR #43529](https://github.com/qgis/QGIS/pull/43529) | Niet van toepassing |
| Pyqgis 3.18.3 error when adding wms layer | [#43580](https://github.com/qgis/QGIS/issues/43580) | [PR #43581](https://github.com/qgis/QGIS/pull/43581) | NOG TE DOEN |
| \"Reuse last entered attribute values\" slows creation of new features on large vector | [#42909](https://github.com/qgis/QGIS/issues/42909) | [PR #43584](https://github.com/qgis/QGIS/pull/43584) | NOG TE DOEN |
| Deleting \"all other values\" breaks date based categorise symbology | [#43651](https://github.com/qgis/QGIS/issues/43651) | [GDAL PR 3978](https://github.com/OSGeo/gdal/pull/3978) |  |
| Fix documentation doctest builds | <https://github.com/qgis/QGIS-Documentation/pull/6747> | <https://github.com/qgis/QGIS-Documentation/pull/6747> | Niet relevant |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| VERSION is now mandatory in WMS 1.3.0 for getmap requests | niet gerapporteerd | [PR #43459](https://github.com/qgis/QGIS/pull/43459) | [PR #43467](https://github.com/qgis/QGIS/pull/43467) |
| WMTS GetCapabilities and axis order | [#34826](https://github.com/qgis/QGIS/issues/34826) | [PR #43280](https://github.com/qgis/QGIS/pull/43280) | [PR #43772](https://github.com/qgis/QGIS/pull/43772) |
| Use the lowest version in wms negotiation | [#41051](https://github.com/qgis/QGIS/issues/41051) | [PR #41376](https://github.com/qgis/QGIS/pull/41376) | Riskant |
| QGIS crashes adding a record to a memory (\"scratch\") layer table in some circumstances | [#42578](https://github.com/qgis/QGIS/issues/42578) | Werkt bij mij wel |  |
| QGIS fails silently when an auxiliary layer cannot be created | niet gerapporteerd | [PR #43543](https://github.com/qgis/QGIS/pull/43543) | [PR #43773](https://github.com/qgis/QGIS/pull/43773) |
| Niet mogelijk hulpmiddel voor opslaan op te slaan | [#26365](https://github.com/qgis/QGIS/issues/26365) | [PR #43560](https://github.com/qgis/QGIS/pull/43560) | Riskant |
| WMS GetFeatureInfo on time enabled layer does not pass TIME parameter | [#42141](https://github.com/qgis/QGIS/issues/42141) | [PR #43599](https://github.com/qgis/QGIS/pull/43599) | [PR #43774](https://github.com/qgis/QGIS/pull/43774) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Widget parameters not persistent for relations in D&D designer | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43479](https://github.com/qgis/QGIS/pull/43479) | niet relevant |
| Use a read-only line edit instead of combobox in relation reference doesn\'t allow to add a child from the parent | [#42813](https://github.com/qgis/QGIS/issues/42813) | [PR #43509](https://github.com/qgis/QGIS/pull/43509) | te riskant / is het niet waard |
| no open-form in all layers feature locator filter (active filter has) + show form instead of error for geometry-less layers | niet gerapporteerd | [PR #43462](https://github.com/qgis/QGIS/pull/43462) | ? |
| Cannot add a polymorphic relations | [#41959](https://github.com/qgis/QGIS/issues/41959) | [PR #43488](https://github.com/qgis/QGIS/pull/43488) | niet relevant |
| Filter expression from relation reference widget on attributes form, not working properly | [#42803](https://github.com/qgis/QGIS/issues/42803) | [PR #43523](https://github.com/qgis/QGIS/pull/43523) | ja |
| fix Picture layout element does not handle properly a non-existing filepath when provided with an expression | [#42280](https://github.com/qgis/QGIS/issues/42280) | [PR #43119](https://github.com/qgis/QGIS/pull/43119) |  |
| relations bug: zoom to child button disappears | [#34477](https://github.com/qgis/QGIS/issues/34477) | Werkt bij mij wel |  |
| Value Relation and Relation reference widget: Entries are sorted although the option \"Order by value\" is NOT checked | [#26468](https://github.com/qgis/QGIS/issues/26468) | voor nu niet zeker hoe dit op te lossen |  |
| Errors while adding a feature with a polymorphic relation | [#41962](https://github.com/qgis/QGIS/issues/41962) | gerepareerd |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProjectionSelectionWidget::selectCrs() cannot be overwritten in Python | [#43019](https://github.com/qgis/QGIS/issues/43019) | Werkt bij mij wel. |  |
| A bug? in FindPyQt5.py | [#41913](https://github.com/qgis/QGIS/issues/41913) | [#41913](https://github.com/qgis/QGIS/issues/41913) | niet relevant |
| Missing incon of Geometry Checker core plugin | [#42708](https://github.com/qgis/QGIS/issues/42708) | [PR #43536](https://github.com/qgis/QGIS/pull/43536) | [PR #43549](https://github.com/qgis/QGIS/pull/43549) |
| Please reomve the not functional OWS group from the QGIS browser | [#24841](https://github.com/qgis/QGIS/issues/24841) | [PR #43559](https://github.com/qgis/QGIS/pull/43559) | Niet van toepassing |
| Build fails with external qwtpolar | [#41910](https://github.com/qgis/QGIS/issues/41910) | [PR #43551](https://github.com/qgis/QGIS/pull/43551) | [PR #43583](https://github.com/qgis/QGIS/pull/43583) |
| Check geometries tool does not save default action changes | [#42489](https://github.com/qgis/QGIS/issues/42489) | [PR #43550](https://github.com/qgis/QGIS/pull/43550) | [PR #43568](https://github.com/qgis/QGIS/pull/43568) |
| Wrong error output location when using Check validity on data with certain type of 3D error | [#43582](https://github.com/qgis/QGIS/issues/43582) | [PR #43588](https://github.com/qgis/QGIS/pull/43588) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Postgresql tables with intarray fields as primary key causes problems in python scripts | [#42778](https://github.com/qgis/QGIS/issues/42778) | [PR #43493](https://github.com/qgis/QGIS/pull/43493) | [PR #43510](https://github.com/qgis/QGIS/pull/43510) |
| Cannot instantiate QgsFeatureFilterModel using PyQGIS | [#42488](https://github.com/qgis/QGIS/issues/42488) | [PR #43494](https://github.com/qgis/QGIS/pull/43494) | [PR #43516](https://github.com/qgis/QGIS/pull/43516) |
| QGIS crashes by loading ui file | [#42379](https://github.com/qgis/QGIS/issues/42379) | Werkt |  |
| QvariantList Field , nothing in attribute table when a single value is in the list | [#33108](https://github.com/qgis/QGIS/issues/33108) | [PR #43508](https://github.com/qgis/QGIS/pull/43508) | [PR #43530](https://github.com/qgis/QGIS/pull/43530) |
| Copy CRS to clipboard when copying selected features | [#40117](https://github.com/qgis/QGIS/issues/40117) | [PR #43527](https://github.com/qgis/QGIS/pull/43527) | [PR #43532](https://github.com/qgis/QGIS/pull/43532) |
| Open Running (connection) Task makes it impossible to Quit QGIS | [#40001](https://github.com/qgis/QGIS/issues/40001) | [PR #43587](https://github.com/qgis/QGIS/pull/43587) |  |
| Plugin manager doesn\'t work with proxy | [#43284](https://github.com/qgis/QGIS/issues/43284) | Terugkoppeling |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #43617](https://github.com/qgis/QGIS/pull/43617) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Peter Petrik
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Passwords cannot be saved into keychain on macOS with QGIS 3.16 | [#40541](https://github.com/qgis/QGIS/issues/40541) | Terugkoppeling |  |
| buggy profile results in two instances starting | [#29379](https://github.com/qgis/QGIS/issues/29379) | geen probleem meer |  |
| GRASS plugin init error on macOS | [#41782](https://github.com/qgis/QGIS/issues/41782) | Werkt bij mij wel. |  |
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | onderzoek |  |
| Crash with point clouds when zooming into 3D viewer \[Mac\] | [#41903](https://github.com/qgis/QGIS/issues/41903) | [PR #43743](https://github.com/qgis/QGIS/pull/43743) | niet relevant |
| Crash when chcking the \"Show bounding boxes\" option in 3D view settings | [#40766](https://github.com/qgis/QGIS/issues/40766) | [PR #43755](https://github.com/qgis/QGIS/pull/43755) | backport_bot |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix browser panel scanning on remote locations can hang QGIS | veel PR's |  |  |
| \[3d\] Fix rendering of curved lines using simple line renderer | niet gerapporteerd | [Commit 700390a](https://github.com/qgis/QGIS/commit/700390abff6928636de010c49746a10129c215eb) |  |
| Fix layer preview through browser panel | [#43303](https://github.com/qgis/QGIS/issues/43303) | [Commit 7bf85a0](https://github.com/qgis/QGIS/commit/7bf85a0cccc105208a0a9563396ad8ca10a38810) |  |
| \[expressions\] Fix evaluation of round(\...) where input value is a string containing a decimal number | [#36467](https://github.com/qgis/QGIS/issues/36467) | [Commit 42c2061](https://github.com/qgis/QGIS/commit/42c2061c5418bbcfa2fde8aac35486ac7fcb26b1) |  |
| Fix label masking settings get dropped for layers with \",\" or \";\" characters in the text | [#37473](https://github.com/qgis/QGIS/issues/37473) | [Commit 3d4e2f4](https://github.com/qgis/QGIS/commit/3d4e2f460f5ca04a469a2549c69b96dea889b174) |  |
| Fix orphaned symbol masking can force maps to be rasterized | niet gerapporteerd | [Commit ffc500d](https://github.com/qgis/QGIS/commit/ffc500d79de02d9f83d36a8fa40b4436079be04d) |  |
| Fix selection of features which use variables in filter rules | [#42006](https://github.com/qgis/QGIS/issues/42006) | [Commit d41c234](https://github.com/qgis/QGIS/commit/d41c2342676098e9c9991305711b9eea748bb858) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[labeling\] Default to \"from symbol bounds\" for cartographic point label placement | [#25866](https://github.com/qgis/QGIS/issues/25866) | [Commit 4ad5d36](https://github.com/qgis/QGIS/commit/4ad5d36d93df8eaf0105aed2c9918197f5bf67ef) |  |
| Fix PyQGIS QgsLineString constructor only accepts lists of QgsPoint, not QgsPointXY as indicated by the documentation | [#43200](https://github.com/qgis/QGIS/issues/43200) | [Commit 2b6c3c1](https://github.com/qgis/QGIS/commit/2b6c3c1db2cc3c8214a6c019c2c044b8bae712f2) |  |
| Fix crash when changing symbol levels through style dock | [#42671](https://github.com/qgis/QGIS/issues/42671) | [Commit f3f4c17](https://github.com/qgis/QGIS/commit/f3f4c17c5fa1d71670d505a2938da2345c683909) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Allow clearing data defined buttons which are set to non-existing fields | niet gerapporteerd | [Commit ee03ad5](https://github.com/qgis/QGIS/commit/ee03ad5991094ec975118c986075d0e830dec469) |  |
| \[processing\] Python entry in history dialog should be processing.run line, not processing.execAlgorithmDialog | niet gerapporteerd | [Commit 61ac64c](https://github.com/qgis/QGIS/commit/61ac64c5a146adc72d38eaf5ab3fe35a6f51be20) |  |
| Don\'t try to render font marker symbols in massive font sizes, avoid crash | [#42270](https://github.com/qgis/QGIS/issues/42270) | [Commit 12d1078](https://github.com/qgis/QGIS/commit/12d1078a8bc11caef7002629e6315cf50522e732) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix Qgis::MessageLevel::None is not available in PyQGIS | [#42996](https://github.com/qgis/QGIS/issues/42996) | [Commit 02266ef](https://github.com/qgis/QGIS/commit/02266ef8e66ef6613d27e7818e0e7adf0d5a3271) |  |
| Fix marker symbol bounds incorrectly include bounds of disabled symbol layers | niet gerapporteerd | [Commit ca54e8f](https://github.com/qgis/QGIS/commit/ca54e8f8520453954e06e4d91adbd375287ddadd) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix hang in rendering joined layers | [#38551](https://github.com/qgis/QGIS/issues/38551) | [Commit ca00377](https://github.com/qgis/QGIS/commit/ca00377027dc7ae6066d8ca5fc3da35ad46dd7c2) | [Commit cdbf722](https://github.com/qgis/QGIS/commit/cdbf7224f716a7272e89239895ae254d2ee31bcd) |
| \[temporal\] Fix broken animations when a non-integer interval value is used (e.g. 1.5 hours) | niet gerapporteerd | [Commit 81ec79c](https://github.com/qgis/QGIS/commit/81ec79c0e5d31f0e56413fdb01af320fbc00c564) |  |
| Fix allowing attribute selection for DXF layer name | [#42575](https://github.com/qgis/QGIS/issues/42575) | [Commit 66c6ef9](https://github.com/qgis/QGIS/commit/66c6ef96bcd4bcce4fa06cfc4ea62c87ac2898c9) |  |
| Fix papercut in rule based labeling widget where it\'s possible to uncheck BOTH the filter and else radio buttons | niet gerapporteerd | [Commit 1fcb9752](https://github.com/qgis/QGIS/commit/1fcb97522c34d319c18bab13e4ccc64d6161bbef) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix it\'s impossible to change a rule based labeling \"else\" rule back to a normal rule | niet gerapporteerd | [Commit de92ca0](https://github.com/qgis/QGIS/commit/de92ca034714452e8de139584518277092ea6c3c) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix data defined properties which bind to a field can have incorrect values when the linked field has a null value | niet gerapporteerd | [Commit 4e25c6b](https://github.com/qgis/QGIS/commit/4e25c6bcf413c8d93a09839696dbc93ae0e55f64) | [Commit 2a3bcc3](https://github.com/qgis/QGIS/commit/2a3bcc365d901c3d69270fd9c4a9a2165c2cbd31) |
| Fix broken coordinate transform when exporting features to DXF | [#43449](https://github.com/qgis/QGIS/issues/43449) | [Commit 65c02e0](https://github.com/qgis/QGIS/commit/65c02e024a767ccc57283ec29a9c1b6d6ef8003f) | [Commit 044f6a1](https://github.com/qgis/QGIS/commit/044f6a1ec2d96314805ee9ab9be73d8d25e38597) |
| \[processing\] Don\'t show model child algorithm outputs as choices for multi-layer input parameters when running a model | [#41210](https://github.com/qgis/QGIS/issues/41210) | [Commit f4477b2](https://github.com/qgis/QGIS/commit/f4477b2cc4f29553ceb8c3d2d82139bc955ffd0c) |  |
| Expand on QgsPoint/QgsPointXY documentation to clarify when each class should be used | [#43598](https://github.com/qgis/QGIS/issues/43598) | [Commit ae83444](https://github.com/qgis/QGIS/commit/ae83444c9f0c5ce8056ac7b282d6fb1dedc43ad4) |  |
| Fix crash when canceling union tool | [#43553](https://github.com/qgis/QGIS/issues/43553) | [Commit b1f50bb](https://github.com/qgis/QGIS/commit/b1f50bbc2cefe593918b73af7d2b92ffac9b764d) | [Commit 1f25ba5](https://github.com/qgis/QGIS/commit/1f25ba5dbc58bc2f2efd1d930a6104110abe1569) |
| Fix \"force layer to render as raster\" setting wasn\'t correctly copied | [#43535](https://github.com/qgis/QGIS/issues/43535) | [Commit 1313786](https://github.com/qgis/QGIS/commit/131378650ff47f35588eed04162a7e2f2c728abf) | [Commit dcd016b](https://github.com/qgis/QGIS/commit/dcd016bace01506aa283aa7e6760ebe13bfa0d73) |
| Fix massive performance regression in attribute table | niet gerapporteerd | [Commit 5fdb88b](https://github.com/qgis/QGIS/commit/5fdb88bae3e40316a489d71594f17548f7a55f00) | [Commit 4970c3a](https://github.com/qgis/QGIS/commit/4970c3a9dbc66d1b2d155e3cdd07df200ee1c14a) |
| Fix performance issue when using attribute table with \"edited or new features\" filter in place | niet gerapporteerd | [Commit af021f1](https://github.com/qgis/QGIS/commit/af021f10fb73d4850a0486527775e7fdc101ef47) |  |
| Fix invalid error message when creating expression for layout text item | [#42884](https://github.com/qgis/QGIS/issues/42884) | [Commit db74013](https://github.com/qgis/QGIS/commit/db74013c7fc5966436fc41b3d912e93367bbec23) |  |
| Clarify labels in temporal controller | niet gerapporteerd | [Commit ed346d8](https://github.com/qgis/QGIS/commit/ed346d88fd3ebdf16839fa5b750dc92731cecfb6) |  |
| Correctly redraw canvas when applying project properties changes | niet gerapporteerd | [Commit 41f9842](https://github.com/qgis/QGIS/commit/41f98420e028c251cd0619242b5c1e8d01f5d41e) | [Commit 607b44b](https://github.com/qgis/QGIS/commit/607b44b1e0175a97c103eb7c04f2450c1ff924d3) |
| Make interactive labeling tools correctly work with data defined properties which aren\'t bound to fields | niet gerapporteerd | [Commit c6bd366](https://github.com/qgis/QGIS/commit/c6bd366112f92e836dd071dd395f8b3dbf982d50) |  |
| Fix crash in labeling if label has data defined x/y set and projection error occurs transforming these coordinates | niet gerapporteerd | [Commit 8943ac7](https://github.com/qgis/QGIS/commit/8943ac76d598f96c59d59a2ed530a972f07f89a1) | [Commit 2fe68cc](https://github.com/qgis/QGIS/commit/2fe68cc2f9c776f12fb94886d9c5d660a7d2a99f) |
| \[temporal\] Fix filter generation for vector temporal layers | [#38468](https://github.com/qgis/QGIS/issues/38468) | [Commit 544708f](https://github.com/qgis/QGIS/commit/544708f4aade5c4451463e045fd23c168552ab40) |  |
| Fix formatting of exception blocks in PyQGIS docs | niet gerapporteerd | [Commit 8359281](https://github.com/qgis/QGIS/commit/835928101213484c23f46e5c91b8329102478534) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix zonal statistics does not correctly handle coordinate transforms | [#26858](https://github.com/qgis/QGIS/issues/26858) | [Commit e70cf8d](https://github.com/qgis/QGIS/commit/e70cf8da2747c13e02866bc940ce4dbb3af41815) | [Commit c82678d](https://github.com/qgis/QGIS/commit/c82678dd6136de79cd76206c9ca25b1f9e34abd2) |
| Don\'t assume that owslib \>= 0.20 is available | [#38074](https://github.com/qgis/QGIS/issues/38074) | [Commit 3cf9083](https://github.com/qgis/QGIS/commit/3cf9083743de2a72893d2efeddcfb29f3ea7130f) | [Commit eb1a55a](https://github.com/qgis/QGIS/commit/eb1a55a146d1dddb7ddf52da9c961e4c5a8cce96) |
| Fix crash in geometry checker when empty geometries are found | [#38983](https://github.com/qgis/QGIS/issues/38983) | [Commit 73a4948](https://github.com/qgis/QGIS/commit/73a49489c857ec492f62bb8ef0ec2494d93d368a) | [Commit 6938593](https://github.com/qgis/QGIS/commit/69385937d842cfa88ff65663591049ca210403b8) |
| \[temporal\] Fix incorrect frame duration in last frame in animation mode | [#40777](https://github.com/qgis/QGIS/issues/40777) | [Commit f76747b](https://github.com/qgis/QGIS/commit/f76747b8b1ffd93844767ad9b66e3601b96a98a2) |  |
| Default to a time range of the last 24 hours, in 1 hour increments, instead of a confusing \"zero length\" range | [#40868](https://github.com/qgis/QGIS/issues/40868) | [Commit 5f5a3a7](https://github.com/qgis/QGIS/commit/5f5a3a7e46fac5a4939d90f2eaf57a8b61008789) |  |
| Fix temporal fields reset if previously set to no value | [#43643](https://github.com/qgis/QGIS/issues/43643) | [Commit 9de5d25](https://github.com/qgis/QGIS/commit/9de5d2500bd358c1214b17434424d1c301444b03) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[processing\] Fix broken execution of models via browser/drag and drop | [#43698](https://github.com/qgis/QGIS/issues/43698) | [Commit cbe2678](https://github.com/qgis/QGIS/commit/cbe2678e34767f01dd3d2578261c4e55e40a00ba) | [Commit 9e0cdcb](https://github.com/qgis/QGIS/commit/9e0cdcba48de04a3fb3a6aa81276e68a0447a6fd) |
| Fix QgsDistanceArea.bearing() | niet gerapporteerd | [Commit 0b499d3](https://github.com/qgis/QGIS/commit/0b499d3a0058dbb234ce54f6329015818a9ccde7) |  |
| Don\'t restrict adding crs selections to list of recent CRSes to only a few select dialogs | niet gerapporteerd | [Commit 870945c](https://github.com/qgis/QGIS/commit/870945c476c1a429eb410af2a793644a7b1db85f) |  |
| \[processing\] Fix use of data defined parameter values when editing features in place | [#43758](https://github.com/qgis/QGIS/issues/43758) | [Commit 3ae9625](https://github.com/qgis/QGIS/commit/3ae96253de7efc5e8921e776ae91de4b9281d90c) |  |
| \[layouts\] Fix bounding rectangle for shapes doesn\'t include stroke width after loading from xml | [#43748](https://github.com/qgis/QGIS/issues/43748) | [Commit fad1800](https://github.com/qgis/QGIS/commit/fad18003b3560e6daa1c47080f5b2fe10ddef9e6) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
