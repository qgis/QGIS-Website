---
HasBanner: false
draft: false
releaseDate: '2022-10-21'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.28
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.28{#changelog328 }
![image1](images/projects/19a3cf4af4fcad7ecec62560b72067b903097054.png)

Datum uitgave 21-10-2022

QGIS 3.28 Firenze introduceert verscheidene updates voor mogelijkheden, aanpassingen van de gebruikerservaringen, verbeteringen voor gebruik, en verbeterde integratie met verschillende merkgebonden services en backends voor gegevens. Het is ook ingesteld om de langverwachte mogelijkheden te introduceren, die worden verschaft door eerdere uitgaven, in de uitgave long-term support release, zoals omschreven in de [QGIS Roadmap](https://www.qgis.org/en/site/getinvolved/development/roadmap.html).

Het welkomstscherm geeft een bijzondere en buitengewone kaart van 1847 van Firenze, of Florence, Italië door Giuseppe Molini weer. Deze schitterende gegraveerde kaart werd origineel getekend in 1731 door de Florentijnse architect Ferdinando Ruggieri. Georiënteerd op het zuiden, bedekt de kaart het oude ommuurde centrum van Florence zoals dat werd uitgebreid aan beide zijden van de rivier de Arno. Het kwadrant rechtsboven geeft het symbool van de lelie van Florence weer. Hoewel afgedrukt in 1847, is deze kaart voorbereid in de stijl van de 17e eeuw door graveren op koperen platen op dik uitgevoerd papier. Firenze in 1847 stond op het punt van een politieke transformatie. Eén jaar na de productie van deze bijzondere kaart gaf de Groothertog van Toscane, als antwoord op de politieke demonstraties in Florence, Toscane zijn eerste grondwet.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u de video met deze mogelijkheden bekijken op YouTube op <https://youtu.be/IEkOhQezQMk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/IEkOhQezQMk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We willen nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze pagina voor dragende leden voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Belangrijke wijzigingen
### Mogelijkheid: Vervallen achterwaartse compatibiliteit voor symbologie in project met QGIS 3.16 en ouder
Eerdere uitgaven van QGIS zouden significante hoeveelheden compatibiliteits-objecten schrijven naar de XML-structuur van projectbestanden om achterwaartse compatibiliteit te behouden voor symbologieën om er voor te zorgen dat projectbestanden kunnen worden geopend met QGIS 3.16 en ouder. Deze compatibiliteit is verwijderd uit toekomstige uitgaven, wat een significante optimalisatie voor de structuur van projectbestanden verschaft.
## Tijdbeheer
### Mogelijkheid: Ondersteuning voor Tijdbeheer toegevoegd voor WMTS-lagen met dimensie TIME
Deze verbetering geeft elke dimensie van \"time\" in WMTS weer om te gebruiken in het framework Tijdbeheer, inclusief de mogelijkheid om de lagen te animeren en te beheren via Tijdbeheer.

Wanneer we een dimensie tijd in een WMTS-laag detecteren, laten we die niet langer zien op dezelfde manier als andere niet-tijddimensies. Het paneel Browser geeft niet de waarden van de dimensies weer, en het toevoegen van de laag via Databron beheren vraagt de gebruiker niet langer om te kiezen tussen de beschikbare tijdwaarden. In plaats daarvan worden deze lagen aangegeven met een nieuw pictogram \"Rasterlaag met mogelijke tijd\", en worden ze toegevoegd aan een project zonder dat de gebruiker een tijdwaarde moet specificeren.

Net als met een WMS(T)-laag, wanneer een WMTS-laag met een ingeschakelde tijdsdimensie wordt toegevoegd aan het project, zal deze standaard gaan naar de modus van Tijdbeheer \"Automatisch\", wat betekent dat de laag standaard het huidige tijdsbereik van Tijdbeheer zal volgen. Een gebruiker kan dan aangeven om een specifieke statische tijdwaarde voor de laag weer te geven via de pagina Eigenschappen Tijdbeheer van de laag, door \"Dynamisch Tijdbeheer\" te deselecteren en een specifiek beschikbaar tijdbereik te kiezen uit de optie \"Vooraf gedefinieerde datum\".

Dit zou de gebruikerservaring moeten unificeren zodat het gebruiken van WMTS tijd-ingeschakelde lagen essentieel identiek is aan het gebruiken van WMS(T)-lagen.

![image3](images/entries/8f0a6c8e4850886732633ab76d5873dffd7746c4.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Kaartgereedschap
### Mogelijkheid: Selecteren van objecten vector-tegellagen toestaan
Ondersteuning voor het selecteren van objecten uit vectortegellagen is toegevoegd, wat het voor gebruikers mogelijk maakt de standaard, op kaarten gebaseerde, gereedschappen voor selecteren te gebruiken om interactief objecten uit deze bronnen te selecteren.

Een gebruiker kan, als een vecttortegellaag een selectie heeft:
- De objecten kopiëren en ze plakken in andere lagen, of ze plakken in een geheugenlaag
- Andere (niet om te bewerken) gereedschappen gebruiken die werken op selecties, zoals \"Zoom naar geselecteerde objecten\"/\"Verschuif naar geselecteerde objecten\"

Selecties kunnen worden gemaakt met behulp van elke van de interactieve op kaarten gebaseerde gereedschappen voor selecteren, bijv. selecteren op rechthoek, vrije hand, polygoon, of straal. Alle sneltoetsen die van toepassing zijn voor selecties van vectors voor toevoegen/aftrekken/kruisen van selecties zijn ook te gebruiken.

Selecteren van objecten wordt uitgevoerd met behulp van het tegel-zoomniveau van het kaartvenster, en dan worden de objecten, die op dit zoomniveau zijn geselecteerd, behouden, zelfs als de gebruiker de schaal van de kaart wijzigt naar een andere zoomniveau voor de vectortegel. Dit betekent dan een gebruiker kan inzoomen en een klein/gedetailleerd object kan selecteren, dan uitzoomen en nog steeds het object op de kaart zien.

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Exclusief venster, gebaseerd op gebruikerservaringen voor Databronnen beheren
Het dialoogvenster Databronnen beheren is nu ALTIJD niet- modaal, en opties om het als zodanig in te stellen zijn verwijderd. Het dialoogvenster functioneert net als andere typen vensters voor \"beheren\" in QGIS, zoals de Stijlmanager of Lay-out beheren.

Databronnen beheren zal in plaats daarvan worden behandeld als zijn eigen venster, dat op de voorgrond wordt geplaatst als op de knop Databronnen beheren wordt gedrukt.

![image4](images/entries/9bbc312e9b1362ae660a9719c910ab209d3e8a55.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Actie Weergeven in attributentabel toegevoegd aan het menu voor rechtsklikken van symbolen van klassen voor Legenda's
Een nieuwe actie \"Weergeven in attributentabel\" is toegevoegd aan het contextmenu voor rechtsklikken voor symbolen van klassen van legenda's in de inhoudsopgave. Dit maakt het voor gebruikers mogelijk de attributentabel te openen met een filter dat wordt toegepast om alleen de objecten die relevant zijn voor een bepaalde groep symbolen overeen te laten komen. Dit verschaft een significante verbetering in de uitvoering voor bepaalde gegevenssets, zoals grote vectorlagen, geladen vanaf een bron op afstand.

![image5](images/entries/8b43481bcab479b040b0a5ac5400ddc89c77dd0a.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Instelling toegevoegd om waarden NULL te verbergen in Identificatieresultaten
De mogelijkheid \"Objecten identificeren\" verschaft nu de mogelijkheid om waarden NULL te verbergen in de teruggegeven resultaten

![image6](images/entries/f0c7217db5f0104999a3d87c2229010dcc62cb50.gif)

Dit werd mogelijk gemaakt door [Camptocamp](https://www.camptocamp.com/)

Deze mogelijkheid werd ontwikkeld door [Ismail Sunni](https://github.com/ismailsunni)
## Symbologie
### Mogelijkheid: Toestaan van beheer over GPS-locatiemarkering
Een nieuwe algemene pagina voor opties voor GPS is geïntroduceerd die nieuwe instellingen bevat voor het beheren van het markeringssymbool dat wordt gebruikt voor de huidige GPS-locatie, en of dit symbool zou moeten worden geroteerd zodat het overeen komt met de GPS-richting.

![image7](images/entries/411b2d3b0f1b180857eda6d4e0c73144f1aeee57.gif)

Dit werd mogelijk gemaakt door Tiwi Resources, Bush Heritage, Australian Wildlife Conservancy

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe vormen voor ellips-markeringen toegevoegd
De symboolstijlen voor het type ellipsmarkering bevatten nu aanvullende typen vormen voor:
- Pentagon
- Hexagon
- Octagon
- 1/3-cirkel
- Kwartcirkel
- Ster

![image8](images/entries/3e749b405f10a24f95665cd0ad3e1ea0f199811b.webp)

Dit werd mogelijk gemaakt door North Road

Deze mogelijkheid werd ontwikkeld door [ZayneTomlins](https://github.com/ZayneTomlins)
## Labelen
### Mogelijkheid Ondersteuning toegevoegd voor HTML-vet/cursief/lettergrootte en type lettertype voor labelen
Ondersteuning voor aanvullende tags voor opmaak in HTM zijn toegevoegd om te gebruiken bij labelen (en overal elders waar de tekstrenderer wordt gebruikt).

Onderetunde tags omvatten specifiek:
- lettertype familie
- lettergrootte
- vet
- cursief

![image9](images/entries/b49f780e98b4276b76cf3022b34da26dd4ed9d1f.webp)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie toegevoegd om absolute eenheden te gebruiken voor regelhoogte
Eerder werd de regelhoogte altijd ingesteld in meervouden van de regelafstand van de tekst. Het is nu echter mogelijk om absolute eenheden te gebruiken voor de regelhoogte (nuttig in contexten waarin gemixte tekstgrootten worden gebruikt binnen één enkel document).

![image10](images/entries/b413c593933bc197886a97919ae015880e119aa7.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Mazen
### Mogelijkheid: Optie toegevoegd om tijdelijke eigenschappen van lagen met mazen opnieuw te laden
Een optie \"Verwijzingstijd altijd nemen uit databron\" is toegevoegd voor lagen met mazen die, indien geselecteerd, ervoor zal zorgen dat de verwijzingstijd opnieuw wordt geladen vanuit de databron. En elke keer als de laag opnieuw wordt geladen of het project opnieuw wordt geopend, worden de eigenschappen van de tijd automatisch vanuit het bestand bijgewerkt.

In eerdere uitgaven, wanneer een laag met mazen een verwijzingstijd en tijdbereik had die wijzigde, zouden de eigenschappen voor de laag met de tijd niet worden bijgewerkt wanneer de projectielagen opnieuw werden geladen. En zou de gebruiker handmatig moeten navigeren naar de mogelijkheid \"Opnieuw laden vanaf provider\" op de tab Tijdbeheer van de Laag-eigenschappen.

![image11](images/entries/8bf480abed6701e5535110f8069ba1f63ecf2de4.gif)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://github.com/vcloarec)
## 3D-objecten
### Mogelijkheid:  3D-effect omgeving opnemen
Een nieuw effect voor het opnemen van de omgeving is beschikbaar voor het renderen van gegevens in 3D-weergaven, wat nuttig is voor het verbeteren van de perceptie van diepte van de gegevens in 3D. Dit is een nabewerkings-effect en het kan zelfs worden gecombineerd met eye dome lighting (EDL) voor bijzonder interessante resultaten. Een oversimplificatie van het effect is dat objecten die niet zichtbaar zijn voor de camera worden gebruikt nabijgelegen elementen te voorzien van textuur en donkerder te maken, met het voordeel van het verbeteren van contrast, definitie van het object en differentiatie.

Er is een nieuw item voor het beheren van de status van Ingesloten omgeving weergeven in het configuratiemenu voor 3D-weergaven, al ook extra parameters in het gedeelte Geavanceerd van het dialoogvenster voor configuratie voor het beheren van het fijn afstemmen:
- Straal De drempel voor de afstand van het berekenen van de Ingesloten omgeving
- Intensiteit: De sterkte die het effect zou moeten hebben (hogere waarden maken dingen donkerder)
- Drempel insluiting: Aantal nabijgelegen punten die moeten worden ingesloten om het effect weer te geven (waarden lager dan 50% zullen de uitvoer donkerder maken, maar mogelijk een groter bereik van insluiting geven)

![image12](images/entries/996b020346252bc10d87279d9e0cac766802c1d4.webp)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias & Belgacem Nedjima](https://github.com/wonder-sk)
## Puntenwolken
### Mogelijkheid: Exporteren van lagen van puntenwolken
Lagen van puntenwolken ondersteunen nu dat zij worden geëxporteerd naar indelingen voor vector of gegevens voor puntenwolken, met optioneel filteren.

Ondersteunde indelingen omvatten:
- Tijdelijke tekenlaag (geheugenlaag)
- GeoPackage
- Shapefile
- DXF
- LAZ (vereist bouwen met WITH_PDAL)
- Niet-gecomprimeerde LAS-bestanden

Bewerkingen voor exporteren ondersteunen filteren op:
- Bereik
- Filteren op bereik Z
- Beperken van het aantal te exporteren punten
- Ruimtelijk filteren op polygoonlaag

Aanvullend worden ook de definitie van het CRS voor uitvoer en opnieuw projecteren ondersteund.

![image13](images/entries/9b7102f1bbd9286c16285a43158904395e56c4bc.webp)

Dit werd mogelijk gemaakt door de Staat Vorarlberg en de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Eye Dome Lighting voor puntenwolken in 2D-kaartvenster
Het effect Eye dome lighting (EDL) is nu beschikbaar voor puntenwolken in 2D-renderers

![image14](images/entries/99c16bf2efe3bdcf020a41ad088e29ec7437573e.webp)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem](https://github.com/NEDJIMAbelgacem)
## Afdruklay-outs
### Mogelijkheid: Toegevoegd parameters FORCE_RASTER en IMAGE_COMPRESSION aan algoritmes voor PDF
De parameters `FORCE_RASTER` en `IMAGE_COMPRESSION` zijn toegevoegd aan de verschillende algoritmes \"Afdruklay-out als PDF exporteren\", inclusief ondersteuning voor Atlas en exporteren naar meerdere bestanden.

`FORCE_RASTER` sluit de parameter `FORCE_VECTOR` uit en heeft voorrang boven die parameter.

![image15](images/entries/06cc045f6a69f9caaacde8f8b3ead9e89f02af22.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Expressies
### Mogelijkheid: Nieuw formulier voor variabelen van huidige functie van expressies van het huidige object toegevoegd
Dit nieuwe stijl formulier voor variabelen is toegevoegd voor het verwijzen naar het huidige object en de attributen ervan in expressies.

De nieuw geïntroduceerde variabelen zijn:
- `@feature`: een vervanging voor \$currentfeature, bevat het huidige object
- `@id`: een vervanging voor \$id, bevat het huidige object-ID
- `@geometry`: een vervanging voor \$geometry, bevat de geometrie van het huidige object

Dit is een stap naar het eventueel laten vervallen van de functies in de oudere stijl `$`, en het verschaffen van een meer consistente benadering tot expressies, in plaats van een onvoorspelbare mix van `@`/`$`.

Oudere functies en verwijzingen naar variabelen zullen blijven werken (en zullen waarschijnlijk oneindig blijven werken in verband met de compatibiliteit met oudere projecten). Zij zullen ook (voorlopig) worden weergegeven in de gebruikersinterface om verwarring voor de gebruikers te voorkomen.

![image16](images/entries/b9666dee9322ba767162310e6958503e639d1148.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe functie shared_paths toegevoegd
Een nieuwe functie `shared_paths`  is toegevoegd die een verzameling teruggeeft met paden die worden gedeeld door de twee geometrieën voor de invoer. Die welke in dezelfde richting gaan staan in het eerste element van de verzameling, die welke in de tegengestelde richting gaan staan in het tweede element. De paden zelf worden gegeven in de richting van de eerste geometrie.

![image17](images/entries/f02946a8f1e45527366c30e6d0ea5a4947c7f86a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Functies make_valid en geom_to_array 
Aanvullende functies zijn toegevoegd voor:
- `make_valid`: Herstel defecte invoergeometrieën en geef de gecorrigeerde geometrieën terug
- `geometries_to_array`: Dit converteert een verzameling geometrieën naar een array voor eenvoudigere afhandeling en doorloop

![image18](images/entries/bc2bbd8d26e2ebb4fd7dc02f0ce7ec6460f3a3bc.webp)

Deze mogelijkheid werd ontwikkeld door [Alex](https://github.com/roya0045)
### Mogelijkheid: Functie Holle schil
Een nieuwe functie `concave_hull` is nu beschikbaar in expressies voor QGIS (GEOS 3.11+)

![image19](images/entries/e434b7356dc93f9c43fa3142c7f8f914a4aa5615.webp)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Vragen naar bevestiging bij annuleren van wijzigingen in expressies
Een nieuw dialoogvenster voor bevestiging beschermt gebruikers nu tegen het per ongeluk annuleren van hun nog niet toegepaste wijzigingen in dialoogvensters van de Expressiebewerker. Deze bescherming wordt gebruikt in de Expressie-tekenreeksbouwer, het dialoogvenster Expressie (pictogram Ypsilon, bijv. voor Geometrie-generatoren of voor Vooraf berekende waarden in Modellen bouwen) en het op Expressie gebaseerde filter (Attributentabel -\> Geavanceerde filterexpressie).

![image36](images/entries/cebe844ae2c28045a8b6e2e89cb2b40cdbbd38c6.webp)

Dit werd mogelijk gemaakt door [WhereGroup GmbH](https://wheregroup.com/)

Deze mogelijkheid werd ontwikkeld door [Johannes Kröger](https://github.com/kannes)
## Gegevensbeheer
### Mogelijkheid: Vragen naar bevestiging bij verwijderen van objecten
Een nieuw dialoogvenster voor bevestiging verschijnt als gebruikers proberen een actie uit te voeren die records zou verwijderen, zoals het gebruiken van de toets DEL of acties op werkbalken om het risico van per ongeluk verwijderde objecten nog verder te beperken. Aanvullend is de telling van het aantal objecten nu opgenomen in het bericht van het dialoogvenster zelf (en wordt ook nog steeds weergegeven in de titelbalk), wat het totale aantal verwijderde objecten duidelijker maakt voor de gebruikers.

In eerdere uitgaven zouden soortgelijke prompts voor bevestiging alleen worden weergegeven als sommige objecten buiten het bereik van het kaartvenster vielen, of het verwijderen activeerde het verwijderen van objecten van kindrelaties. Het nieuwe gedrag is dat de prompt standaard is ingeschakeld en kan worden uitgeschakeld met het keuzevak \"Dit bericht niet opnieuw weergeven\".

![image20](images/entries/677952561ec24d417a74cf46842a6c52aec49587.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Metadata en Metasearch
### Mogelijkheid: Zoeken en opslaan van metadata van de gegevensprovider van de laag
Implementatie van elementen van de [QEP #250 \"Database metadata storage\"](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/250) Het initiatief is voltooid en deze functionaliteit omvat het maken van een nieuwe API voor metadata voor de laag en componenten voor de GUI.

De volgende gegevensproviders/indelingen worden ondersteund voor het opslaan en beheren van metatdata van de laag in QGIS:
- GPKG (was al geïmplementeerd, ik verpakte hem slechts in de nieuwe API)
- Postgres
- Postgres Raster

In aanvulling daarop is een tab Zoeken voor metadata van de laag beschikbaar in Databronnen beheren, en een interactieve zoekactie voor metadata van de laag beschikbaar met de Locatiebalk van QGIS.

![image21](images/entries/17fc26636b3c1fe423ec8f715e69365495519add.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Processing
### Mogelijkheid: Ondersteuning voor vaste precisie voor gereedschap van Processing voor selecteren
Een nieuwe geavanceerde parameter is beschikbaar voor enkele gereedschappen van Processing die het mogelijk maakt om de parameter [fixed precision](https://blog.cleverelephant.ca/2020/12/waiting-postgis-31-3.html#fixed-precision-overlay) te gebruiken, die wordt verschaft door GEOS \>= 3.9.0. Deze parameter is vermeld onder Geavanceerde parameters als \"Grid Size\" en wordt momenteel ondersteund in de volgende gereedschappen:
- Overlapping
- Kruising
- Verschil
- Symmetrisch verschil
- Verenigen

![image22](images/entries/b2ef315dc1013852d3316023c62af5ff06626e93.webp)

Dit werd mogelijk gemaakt door Orange Telecom FR

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Verbeterde algortimes \"Make Valid\"
QGIS kan nu de nieuwere verfijnde methoden voor GEOS 3.10+ gebruiken voor valideren en repareren van objecten geometrie.

![image23](images/entries/4b320e5bad078f1a0eb23fe958d86e330b08c10e.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Standaard optie om de telling voor vectoruitvoer vanuit Processing weer te geven
Een nieuwe instelling `Telling van objecten weergeven voor uitvoer vectorlagen` is beschikbaar (maar standaard uitgeschakeld om redenen van uitvoering), die automatisch de optie \"Telling objecten weergeven\" zal weergeven op uitvoerlagen die worden geladen vanuit QGIS Processing. Dit is een mogelijkheid om gebruikers een eerste glimp te geven van wat te verwachten als een uitvoer van een algoritme van Processing.

![image24](images/entries/e804b2accbcf155f4db2ea4024bd89ed5883097f.webp)

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
### Mogelijkheid: Optie voor het exporteren van relaties naar het algoritme voor verpakken van lagen
Het gereedschap \"Pakketlagen\" ondersteunt nu optioneel de volgende project-relaties nn het exporteren van gerelateerde tabellen, die die hiërarchie zowel naar boven als naar beneden volgen, terwijl ook rekening wordt gehouden met geselecteerde objecten.

![image25](images/entries/26076b13de92a8ac2a1fea1511e03776c1aeae13.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Parameter \"Verspringing\" toegevoegd aan algoritmes \"Drape\"
Voegt de parameter \"Verspringing\" toe aan de algoritmes \"Drape (Z-waarde instellen vanuit raster)\" en \"Z-waarde instellen vanuit raster\". De waarde \"Verspringing\" is algebraïsch toegevoegd aan de bandwaarden na het toepassen van de \"Schaalfactor\".

![image26](images/entries/78e9cb5b82c872604fc3616c2c7b3772e7d26bef.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Opties voor toepassing en projecten
### Mogelijkheid: Aangepaste instellingen projectcoördinaat en weergave van richting
De opties voor Weergave Coördinaat en richting in de projecteigenschappen zijn bijgewerkt in lijn met het volgende:
- Kaarteenheden (gedrag is hetzelfde als in eerdere uitgaven)
- Geografische kaart (aangepast gedrag)
- Eenheden aangepaste projecties (nieuw type)

De oudere optie Geografische kaart (Latitude/ Longitude) zou waarden weergeven in de coördinaten van het CRS, *als* het CRS geografisch was, anders zou het waarden transformeren naar een hard-gecodeerde waarde in CRS WGS84.

De bijgewerkte optie Kaarteenheden (graden), die de oudere benadering vervangt, zal waarde weergeven in de coördinaten van het kaart-CRS, *als* het CRS geografisch is. Echter, in gevallen waarin dat niet het geval is, zal de interne API `QgsCoordinateReferenceSystem::toGeographicCrs()` worden gebruikt om de coördinaten te transformeren naar de met het kaart-CRS geassocieerde geografische CRS. Dit is in verscheidene contexten nuttig, zoals bij het analyseren van niet-aardse hemellichamen.

Het type Eenheden aangepaste projecties is een nieuwe aanvulling die standaard terugvalt op WGS84 en gebruikers in staat stelt elke CRS dat zij willen in te stellen om de coördinaten weer te geven.

![image27](images/entries/7af6704f72373fec3c1e9c212366fd3d8cfa0218.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Ondersteuning toegevoegd voor lettertypen van \"gebruikers\", en automatisch downloaden van vrije gelicenseerde lettertypen
Een nieuw paneel \"Lettertypen\" is toegevoegd aan het dialoogvenster Instellingen dat ondersteuning verschaft voor de volgende functionaliteiten:
- De mogelijkheid voor gebruikers om een lijst te vullen met automatisch te vervangen lettertypen om toe te passen bij het laden van projecten of stijlen. Wat betere ondersteuning voor projecten en stijlen mogelijk maakt als ze worden gebruikt over verschillende besturingssystemen (bijv. vervang \"Arial\" door \"Helvetica\").
- Gebruikers kunnen nu lettertypen TTF of OTF plaatsen in de submap \"fonts\" van hun gebruikersprofiel. Deze lettertypen zullen automatisch worden geladen bij het opstarten van QGIS. Dit verschaft een manier voor gebruikers om lettertypen te gebruiken zonder dat ze moeten zijn geïnstalleerd op het niveau van het besturingssysteem, wat vaak is geblokkeerd in zakelijke netwerken. Het paneel Instellingen lettertypen vermeldt alle geïnstalleerde lettertypen van de gebruiker en stelt gebruikers in staat ze te beheren (d.i. verwijderen van) eerder geïnstalleerde lettertypen van de gebruiker
- Een API wordt verschaft voor andere gereedschappen, zoals plug-ins en andere cliënten, om aanvullende mappen voor lettertypen van gebruikers te specificeren, die zouden moeten worden gescand bij het opstarten van QGIS
- Automatisch downloaden van ontbrekende lettertypen wordt nu in bepaalde omstandigheden ondersteund. Als een gebruiker een project of stijl opent, of zij proberen een vectortegel-laag te laden die naar lettertypen verwijst die momenteel niet beschikbaar zijn, dan wordt een hardgecodeerde lijst van vrij gelicenseerde lettertypen, die kunnen worden gedownload via URL, geconsulteerd. Om te bepalen of het mogelijk is om het lettertype automatisch te downloaden naar de map voor de lettertypen van de gebruiker (en de gebruiker te notificeren over de licentie van het lettertype). Een instelling om dit gedrag uit te kunnen schakelen wordt, indien gewenst, verschaft in het paneel Lettertypen.

![image28](images/entries/77e17395ccb70e466ad4c5a80675ad0ff8ec070e.gif)

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Browser
### Mogelijkheid: Implementeren van het ontdekken van relaties voor lagen van OGR, en relatens weergeven in browser
De mogelijkheid Project Eigenschappen → Relaties → Relaties ontdekken is nu in staat lagen van OGR te ondersteunen die relaties ondersteunen, zoals GeoPackage (via de uitbreiding van de gerelateerde tabellen) en ESRI FileGeodatabases.

Het paneel QGIS Browser bevat nu de mogelijkheid om gedetailleerde informatie voor de relaties van deze databronnen weer te geven.

![image29](images/entries/11c3f493eff806b4eccbf9af27c96894ea3223a3.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aangepaste UX voor het maken van Geopackage en ESRI File Geodatabase
Een actie \"Nieuwe ESRI File Geodatabase\" is toegevoegd aan het contextmenu met rechtsklikken van de QGIS Browser voor mappen, en een nieuwe actie \"vacuum\" is beschikbaar voor bestanden van GDB files. (vereist GDAL 3.6+)

Aanvullend zal het maken van een nieuwe Geopackage vanuit hetzelfde menu nu onmiddellijk een lege GPKG maken, in plaats van het oudere standaard gedrag van het openen van een dialoogvenster voor het maken van een tabel (en het maken van een tabel te vereisen of gebruikers dummy gegevens in te laten voeren).

<https://user-images.githubusercontent.com/1829991/178902332-0e112e73-0140-45b9-84bf-fc7875cb7b98.gif>

![image30](images/entries/7a0e8f73e24aa061244e30d6bf1b8154e5eebce4.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Toestaan van verslepen van vectorlagen naar niet-GPKG OGR database-gegevenssets
QGIS staat nu het slepen en neerzetten van vectorlagen toe tussen OGR-database-gegevenssets die niet zijn opgeslagen in de indeling GPKG. Bijvoorbeeld het slepen van een laag op een GDB om die gegevensset te importeren in de geodatabase

![image31](images/entries/c1c17d31db79a4beaab864daf13257e6e7ed0ba0.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Beheren van velddomein weergeven voor niet-gpkg OGR-bronnen
De QGIS Browser ondersteunt nu meer geavanceerde functionaliteiten voor databases van OGR die niet in de indeling GPKG zijn, inclusief mogelijkheden voor het Beheren van velddomeinen (maken en vermelden van domeinen) en het maken van tabellen. Dit betekent dat gebruikers velddomeinen kunnen beheren en nieuwe tabellen kunnen maken in een bestaande ESRI FileGeodatabase-database vanuit de interface van QGIS Browser.

![image32](images/entries/cc1f815593c28352dffaad020061004db91f8ded.webp)

Dit werd mogelijk gemaakt door Provincie Gelderland

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Rol voor sessie definiëren voor verbindingen van PostgreSQL
Een instelling `session_role` kan nu worden gespecificeerd voor verbindingen voor PostgreSQL om de identificatie van de gebruiker van de actieve SQL-sessie in te stellen. Rechten voor controles van de opdrachten voor SQL worden dan uitgevoerd met de geassocieerde benoemde rol.

Dit is in het bijzonder heel nuttig in gevallen waar het gewenst is om automatisch eigenaarschap te geven voor nieuwe objecten (Tabellen/ Views/ Functies etc.) aan de groep `session_role`, en het eigenaarschap en de geassocieerde rechten te delen met alle leden van de groep `session_role`.

De gespecificeerde `session_role` moet een rol zijn waarvan de huidige gebruiker lid is, of als de gebruiker van de sessie een superuser is, mag elke rol worden geselecteerd.

Dit werd mogelijk gemaakt door [3liz](https://3liz.com/)

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
### Mogelijkheid: Automatisch gerelateerde tabellen toevoegen bij het toevoegen van lagen uit GDAL-gegevenssets met ingebedde informatie over elaties
Voor gegevensindelingen van GDAL met ingebedde informatie over relaties, is QGIS nu in staat, elke keer als een tabel wordt toegevoegd, om relaties te ontdekken en onmiddellijk alle gerelateerde tabellen toe te voegen aan het huidige project (als zij nog niet bestaan). Aanvullend zal QGIS, bij het toevoegen van deze gerelateerde lagen, automatisch de corresponderende relaties voor QGIS configureren.

Dit werkt voor alle indelingen die de API voor relaties van GDAL ondersteunt, die omvat:
- Geopackage (via de uitbreiding van de gerelateerde tabellen)
- ESRI FileGDB/ OpenFileGDB
- ESRI Personal Geodatabase
- SQLite/ Spatialite-indelingen.

Deze mogelijkheid werd mogelijk gemaakt door de Universiteit van Uppsala

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning toegevoegd voor subset string-(filter) voor Arcgis REST-lagen
Dit kan de uitvoering op grote lagen **enorm** verbeteren!

Dit werd mogelijk gemaakt door [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Abstracte database-provider voor hernoemen van velden
Een interface `QgsAbstractDatabaseProviderConnection` is toegevoegd voor de ondersteuning van het hernoemen van velden, en geïmplementeerd voor verbindingen van OGR, naast de mogelijkheid om bestaande velden voor ondersteunde verbindingen te hernoemen via de interface van QGIS Browser.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: WFS uitvoeren van binaire ruimtelijke bewerkingen in expressies op de server
QGIS was in staat om de expressie-filters voor binaire ruimtelijk bewerkingen op de server uit te voeren als de geometrie werd opgegeven als WKT of in de indeling GML. Deze wijziging converteert de geometrie van een statische variabele in de expressie tot een filter voor OGC. De URL voor WFS wordt dan gemaakt door het combineren van een rechthoek van een begrenzingsvak, een filter voor de laag en de filter-expressie.

Een verzoek voor een object berekent voorafgaand de expressie om na te gaan of die kan worden uitgevoerd op de server. Dan wordt het opgeslagen in `QgsBackgroundCachedSharedData` waar een nieuwe download wordt geactiveerd.

Wanneer een filter-verzoek geen puur binair ruimtelijke bewerking is, zal het niet worden geëvalueerd op de server.

Dit werd mogelijk gemaakt door Kanton Schaffhausen

Deze mogelijkheid werd ontwikkeld door [signedav](https://github.com/signedav)
### Mogelijkheid: Bewerken van lagen van ArcGIS REST
QGIS ondersteunt nu het bewerken van lagen van ArcGIS feature server, zoals die welke door ArcGIS online worden gehost. Er van uitgaande dat de gebruiker de toepasselijke rechten zijn toegewezen voor het bewerken van een laag, zal het de mogelijkheid ontgrendelen om de eigen gereedschappen van QGIS om die laag te bewerken. Deze wijzigingen omvatten ondersteuning voor de volgende bewerkingen:
- Objecten verwijderen
- Nieuwe objecten toevoegen
- Gebogen geometrieën (alleen ondersteund voor enterprise ArcGIS server, omdat [ArcGIS online momenteel geen ondersteuning heeft voor bogen](https://support.esri.com/en/technical-article/000014684))
- Bestaande objecten bewerken
- Attributen aanpassen (velden maken, velden verwijderen, indexen voor attributen maken)

Dit werd mogelijk gemaakt door [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch raster sublagen laden uit vectortegelstijlen
Bij het laden van een nieuwe bron voor vectortegels in een project, als de geassocieerde stijl van MapBox GL al enige raster sublaag bevat, laad deze dan ook in het project met geconverteerde stijlen.

Repareert <https://github.com/qgis/QGIS/issues/46593>

![Peek 2022-06-20 12-31](https://user-images.githubusercontent.com/1829991/174514930-77887a1d-4679-49a2-9ff0-7c360bc0fc01.gif)

Dit werd mogelijk gemaakt door Toitū Te Whenua Land Information New Zealand

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Individuele WMS-lagen toevoegen
In eerdere uitgaven zou de selectie van lagen uit WMS Servers in QGIS worden geladen als één enkele projectlaag. Deze nieuwe functionaliteit verschaft een optioneel keuzevak om elke van de geselecteerde WMS-lagenyers in QGIS te laden als afzonderlijke projectlagen.

![image34](images/entries/2685710315d58fc03e1557e3381a41fdd8eb5a02.gif)

Dit werd mogelijk gemaakt door [Camptocamp](https://www.camptocamp.com/)

Deze mogelijkheid werd ontwikkeld door [Ismail Sunni](https://github.com/ismailsunni)
### Mogelijkheid: Projecten opslaan naar Oracle Database Provider
QGIS ondersteunt nu het opslaan van projecten naar Oracle databases.

![image35](images/entries/6a575714dfc905211f3518a4f5f3803c32e8afa9.webp)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## QGIS Server
### Mogelijkheid: Instellingen variabele QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS
Deze nieuwe mogelijkheid makt het mogelijk extra tokens te specificeren die zouden kunnen worden gebruikt voor een definitie van een WMS FILTER. De huidige lijst van geaccepteerde tokens is nogal klein en deze instelling stelt systeembeheerders in staat  de lijst van toegestane tokens eenvoudig uit te breiden.

Deze mogelijkheid werd mogelijk gemaakt door Zweckverband Grevesmühlen

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Lagen openen in modus Alleen lezen met QGIS Server
Een nieuwe omgevingsvariabele `QGIS_SERVER_FORCE_READONLY_LAYERS` om QGIS Server te forceren lagen te openen in modus Alleen-lezen.

Dit omvat verscheidene onderliggen wijzigingen aan de API om configuratie voor Alleen-lezen te ondersteunen voor constructie van de gegevensprovider, structuur van het project, en eigenschappen van de laag.

Dit werd mogelijk gemaakt door [Ifremer](https://wwz.ifremer.fr/)

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
## Plug-ins
### Mogelijkheid: Wijzigingen aan het gedrag voor het automatisch bijwerken van plug-ins
Deze wijziging verplaatst de oude sleutel voor de instelling `app/plugin_installer/checkOnStart` naar een nieuwe sleutel `plugins/automatically-check-for-updates`, en schakelt de standaardwaarde naar het inschakelen van automatische controles.

Dit is ontworpen om alle bestaande gebruikers van QGIS te laten overschakelen naar het nieuwe gedrag voor het controleren van updates voor plug-ins bij het opstarten (tot een maximum van één maal elke 3 dagen).

Het is bedoeld om een betere ervaring met QGIS aan onze gebruikers te bieden, door alle gebruikers proactief te informeren wanneer plug-ins zouden moeten worden bijgewerkt, er voor zorgende dat ALLE gebruikers waarschijnlijk plug-ins upgraden en de reparaties voor problemen met plug-ins direct verkrijgen.

**Zakelijke gebruikers die deze instelling hebben aangepast in hun systemen zullen hun scripts moeten aanpassen naar de nieuwe sleutel voor de instelling.**

Aanvullend is de optie om het aantal dagen te beheren tussen de controles voor plug-ins bij opstarten verwijderd en is hard gecodeerd op 3 dagen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Programmeerbaarheid
### Mogelijkheid: AfhandelingTijdbeheer van kaarten in QGIS Quick toegevoegd
Een nieuwe implementatie is toegevoegd om de Instellingen voor kaartvenster en kaart in [QGIS Quick](https://api.qgis.org/api/qgsquick.html) toe te staan om de functionaliteit Tijdbeheer af te handelen.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Aanvulling van de parameter voor de opdrachtregel py-args
Bij het uitvoeren van QGIS vanaf de opdrachtregel met de parameter `--code`, maakt een nieuwe mogelijkheid `--py-args` het doorgeven van argumenten aan de interpreter van Python mogelijk. 

Argumenten tussen `--py-args` en `--` worden doorgegeven aan de interpreter van Python en genegeerd door QGIS, dus bij bijvoorbeeld het gebruiken van de volgende opdracht:

    qgis --code /home/user/example.py --py-args --specialScriptArguments "arg1" 'arg2' -- layer1 layer2
    
Zal aan het script `example.py` de `--specialScriptArguments`, `arg1`, en `arg2` doorgeven als systeemargumenten aan de interpreter van Python, terwijl `layer1` en `layer2` normaal door QGIS worden afgehandeld en geladen als kaartlagen

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation Vorarlberg

Deze mogelijkheid werd ontwikkeld door [Damiano Lombardi](https://github.com/domi4484)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GetPrint request of Atlas Template doesn\'t respect Project scales | [#49900](https://github.com/qgis/QGIS/issues/49900) | [PR #50199](https://github.com/qgis/QGIS/pull/50199) | [PR #50214](https://github.com/qgis/QGIS/pull/50214) |
| Attribute Table Integer entries not showing due to window size | [#50181](https://github.com/qgis/QGIS/issues/50181) | [PR #50201](https://github.com/qgis/QGIS/pull/50201) | Niet aanbevolen |
| WFS3 collections field name/displayName mix in request/response | [#49399](https://github.com/qgis/QGIS/issues/49399) | [PR #50203](https://github.com/qgis/QGIS/pull/50203) | Niet aanbevolen |
| QGIS Server WMS GetFeatureInfo does not evaluate represent_value expression in maptip | [#30719](https://github.com/qgis/QGIS/issues/30719) | [PR #50216](https://github.com/qgis/QGIS/pull/50216) | [PR #50223](https://github.com/qgis/QGIS/pull/50223) |
| \"evaluate default value on providers side\" block insert on table in the schema with autoincrement | [#50168](https://github.com/qgis/QGIS/issues/50168) | [PR #50230](https://github.com/qgis/QGIS/pull/50230) | [PR #50333](https://github.com/qgis/QGIS/pull/50333) |
| QGIS not responding when entering page size using custom width or height fields | [#50104](https://github.com/qgis/QGIS/issues/50104) | Kan niet worden gereproduceerd |  |
| \"Add Directory\...\" inputs files from previous selected directory at first instance, then the corret. | [#50055](https://github.com/qgis/QGIS/issues/50055) | [PR #50232](https://github.com/qgis/QGIS/pull/50232) | [PR #50241](https://github.com/qgis/QGIS/pull/50241) |
| Layer style panel and Layer panel do not show same visibility settings for layer style | [#49998](https://github.com/qgis/QGIS/issues/49998) | Kan niet worden gereproduceerd |  |
| Crash while opening Options dialog after switching locale | [#50239](https://github.com/qgis/QGIS/issues/50239)9 | [PR #50263](https://github.com/qgis/QGIS/pull/50263) | Niet nodig |
| unreported MSSQL connections API error | Niet gerapporteerd | [PR #50194](https://github.com/qgis/QGIS/pull/50194) | [PR #50454](https://github.com/qgis/QGIS/pull/50454) |
| Identify and select tools don\'t work with geometry-based query layers | [#50242](https://github.com/qgis/QGIS/issues/50242) | Kan niet worden gereproduceerd |  |
| Problem with Reloading SLD file in QGIS | [#50152](https://github.com/qgis/QGIS/issues/50152) | [PR #50266](https://github.com/qgis/QGIS/pull/50266) | Wachtrij |
| Unreported endless alg splitwithlines | Niet gerapporteerd | [PR #50279](https://github.com/qgis/QGIS/pull/50279) | Niet aanbevolen |
| Processing algorithm \"Split with lines\" does not split polygon | [#50227](https://github.com/qgis/QGIS/issues/50227) | Is geen probleem |  |
| Expression do not split string in multiple lines | [#49666](https://github.com/qgis/QGIS/issues/49666) | [PR #50295](https://github.com/qgis/QGIS/pull/50295) | [PR #50455](https://github.com/qgis/QGIS/pull/50455) |
| Problem with exportation of complex SLD | [#42348](https://github.com/qgis/QGIS/issues/42348) | [PR #50342](https://github.com/qgis/QGIS/pull/50342) | [PR #50354](https://github.com/qgis/QGIS/pull/50354) |
| Wrong interpretation of SLD color opacity | [#44657](https://github.com/qgis/QGIS/issues/44657) | Is geen probleem |  |
| Wrong label size for SLD export/import | [#35561](https://github.com/qgis/QGIS/issues/35561) | [PR #50347](https://github.com/qgis/QGIS/pull/50347) | Niet nodig |
| Exporting SLD doesnt include fill-opacity | [#33376](https://github.com/qgis/QGIS/issues/33376) | [PR #50349](https://github.com/qgis/QGIS/pull/50349) | [PR #50436](https://github.com/qgis/QGIS/pull/50436) |
| SpatiaLite - Added feature vanishes, attribute dialog does not show required fields | [#50523](https://github.com/qgis/QGIS/issues/50523) | [PR #50573](https://github.com/qgis/QGIS/pull/50573) | Wachtrij |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Niet van toepassing |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Niet nodig |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Niet gerapporteerd | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Niet van toepassing |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Niet gerapporteerd | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Niet nodig |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328)Bug Title |
| \-- | \-- | \-- | \-- |
| GML import is missing one feature without geometry | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | Niet van toepassing |
| WFS/QgsOapifProvider does not take the pageSize from the dialog into account | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | Niet nodig |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: missing namespace prefix on geometry and attribute elements in FILTER for WFS GetFeature reques | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | Niet gerapporteerd | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| WFS client shows wrong CRS | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignores field inherited from parent feature type in WFS 2.0 services | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | Niet van toepassing |
| Loading and displaying CADRG/NITF data is slower than it used to be | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | Niet gerapporteerd | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | Niet nodig |
| QGIS 3.24.1 (Windows) destroys my VRT raster mosaic | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS not retrieving sequence from postgis in 3.26 | [#49463](https://github.com/qgis/QGIS/issues/49463) | [PR #50247](https://github.com/qgis/QGIS/pull/50247) | niet noodzakelijk to bp |
| SVG is not rendered for SVG Marker symbol | [#50208](https://github.com/qgis/QGIS/issues/50208) | Kan niet gerepareerd worden, Probleem van Qt |  |
| If \"estimated metadata\" option is checked, feature count for tables/postgis do not work | [#46790](https://github.com/qgis/QGIS/issues/46790) | [PR #50256](https://github.com/qgis/QGIS/pull/50256) | [PR #50425](https://github.com/qgis/QGIS/pull/50425) |
| Variable raster image source in composer not working | [#47981](https://github.com/qgis/QGIS/issues/47981) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Print Layout Picture Box reverting to SVG | [#38031](https://github.com/qgis/QGIS/issues/38031) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Layout picture can not change SVG image to Raster image | [#37804](https://github.com/qgis/QGIS/issues/37804) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| QgsOptionsPageWidget - helpKey and helpSearchPath are not working | [#49421](https://github.com/qgis/QGIS/issues/49421) | [PR #50282](https://github.com/qgis/QGIS/pull/50282) | [PR #50330](https://github.com/qgis/QGIS/pull/50330) |
| Freeze when opening WFS attribute table from HTTPS server with SSL exception | [#42615](https://github.com/qgis/QGIS/issues/42615) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | geen bp |
| News feed not loading when using MSI installer | [#49097](https://github.com/qgis/QGIS/issues/49097) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | geen bp |
| .ci/run_tests.sh: test_core_networkaccessmanager (Timeout) | [#50234](https://github.com/qgis/QGIS/issues/50234) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) |  |
| SVG Symbol on newer version of QGIS (3.22.7/8/10 tested) make the software lag a lot (and not on 3.4 version). | [#49818](https://github.com/qgis/QGIS/issues/49818) | Feedback, not sure it's a bug |  |
| Empty Options drop-down menu in Query Logger tab | [#50403](https://github.com/qgis/QGIS/issues/50403) | [PR #50527](https://github.com/qgis/QGIS/pull/50527) | geen bp |
| Build fails with WITH_POSTGRESQL=OFF | [#50075](https://github.com/qgis/QGIS/issues/50075) | Terugkoppeling |  |
| Build fails with WITH_GSL=OFF | [#50076](https://github.com/qgis/QGIS/issues/50076) | [PR #50555](https://github.com/qgis/QGIS/pull/50555) |  |
| QGIS master exports out of bounds in layout | [#48624](https://github.com/qgis/QGIS/issues/48624) | Kan niet gerepareerd worden, Probleem van Qt |  |
| Layout bleeding to edge outside map window | [#49638](https://github.com/qgis/QGIS/issues/49638) | Kan niet gerepareerd worden, Probleem van Qt |  |
| Freeze with virtual field on \$area used as parameter in sum | [#49589](https://github.com/qgis/QGIS/issues/49589) | [PR #50533](https://github.com/qgis/QGIS/pull/50533) | [PR #50565](https://github.com/qgis/QGIS/pull/50565) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server WFS 1.1.0 GetFeature response - properties with xsi:nil=\"true\" | [#45243](https://github.com/qgis/QGIS/issues/45243) | [PR #50495](https://github.com/qgis/QGIS/pull/50495) |  |
| Cannot move labels | [#47542](https://github.com/qgis/QGIS/issues/47542) | Kan niet worden gereproduceerd |  |
| Auxiliary storage and removed layers | [#44667](https://github.com/qgis/QGIS/issues/44667) | [PR #50479](https://github.com/qgis/QGIS/pull/50479) | Niet aanbevolen |
| OPACITIES parameter not handled with Vector Tile layer in GetMap/GetPrint | [#50364](https://github.com/qgis/QGIS/issues/50364) | [PR #50374](https://github.com/qgis/QGIS/pull/50374) | [PR #50539](https://github.com/qgis/QGIS/pull/50539) |
| Fixes log messages when a job error is not related to a specific layer | Niet gerapporteerd | [PR #50372](https://github.com/qgis/QGIS/pull/50372) | Niet nodig |
| Labels: Data defined override of \"Show Label\" always wants the auxiliary storage option | [#47993](https://github.com/qgis/QGIS/issues/47993) | [PR #50496](https://github.com/qgis/QGIS/pull/50496) | [PR #50538](https://github.com/qgis/QGIS/pull/50538) |
| Auxiliary storage rotation or offset fields for symbols are visible by default while labels are not | [#28548](https://github.com/qgis/QGIS/issues/28548) | [PR #50498](https://github.com/qgis/QGIS/pull/50498) |  |
| Improve selection of PostGIS raster overviews | Niet gerapporteerd | [PR #50554](https://github.com/qgis/QGIS/pull/50554) | [PR #50575](https://github.com/qgis/QGIS/pull/50575) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere](https://hytech-imaging.fr/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with offline-editing-core-plugin converting to offline project layer with empty polygon | [#50466](https://github.com/qgis/QGIS/issues/50466) | [PR #50577](https://github.com/qgis/QGIS/pull/50577) |  |
| Cleanup temporary python test config path when requested | [#48884](https://github.com/qgis/QGIS/issues/48884) | [PR #50608](https://github.com/qgis/QGIS/pull/50608) |  |
| Include type name in message about unsupported qfield validations | Niet gerapporteerd | [PR #50589](https://github.com/qgis/QGIS/pull/50589) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Sandro Santilli (strk)](https://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix regression in column break calculations in legends | [#42672](https://github.com/qgis/QGIS/issues/42672) | [PR #50597](https://github.com/qgis/QGIS/pull/50597) | Niet geschikt \-- Te riskant |
| Fix tracing fails when layer crs differs from map crs | [#49247](https://github.com/qgis/QGIS/issues/49247) | [PR #50612](https://github.com/qgis/QGIS/pull/50612) | Niet vereist |
| Show only available CRS in WMS layer selection widget | [#45918](https://github.com/qgis/QGIS/issues/45918) | [PR #50572](https://github.com/qgis/QGIS/pull/50572) | Niet vereist |
| Fix some overlay algorithms output multipoint geometries but output layer is single point, causing insertion errors | [#49456](https://github.com/qgis/QGIS/issues/49456) | [PR #50567](https://github.com/qgis/QGIS/pull/50567) | [PR #50641](https://github.com/qgis/QGIS/pull/50641) |
| Fix missing information in crash reports on Windows | [#50472](https://github.com/qgis/QGIS/issues/50472) | [PR #50595](https://github.com/qgis/QGIS/pull/50595) | Niet vereist |
| Fix regression where attribute table dialogs do not open as proper top level windows with their own taskbar entries | [#49286](https://github.com/qgis/QGIS/issues/49286) | [PR #50594](https://github.com/qgis/QGIS/pull/50594) | Niet vereist |
| \[georeferencer\] Fix options ignored when \"create world file only\" is active | [#49331](https://github.com/qgis/QGIS/issues/49331) | [PR #50566](https://github.com/qgis/QGIS/pull/50566) | Niet vereist |
| Ensure identify tool uses correct labels for x/y values when coordinate axis order for project is y/x | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Niet vereist |
| Ensure coordinate display in status bar updates immediately when related settings change, and update the tooltip to match the actual values displayed in the widget | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | Niet vereist |
| Fix rendering of linestrings with nan z values | [#50510](https://github.com/qgis/QGIS/issues/50510) | [PR #50549](https://github.com/qgis/QGIS/pull/50549) | Niet vereist |
| Fix broken logic in clearing python console history | Niet gerapporteerd | [PR #50504](https://github.com/qgis/QGIS/pull/50504) | [PR #50515](https://github.com/qgis/QGIS/pull/50515) |
| Fix QgsFileWidget does not reactivate widget\'s window after selecting a file/folder via the browse button on mac | Niet gerapporteerd | [PR #50501](https://github.com/qgis/QGIS/pull/50501) | [PR #50502](https://github.com/qgis/QGIS/pull/50502) |
| Fix code folding not shown for non-python code editor classes | Niet gerapporteerd | [PR #50492](https://github.com/qgis/QGIS/pull/50492) |  |
| Fix leak in GEOS geometry library use | Niet gerapporteerd | [PR #50379](https://github.com/qgis/QGIS/pull/50379) |  |
| Fix raster contour renderer ignores opacity setting | [#41663](https://github.com/qgis/QGIS/issues/41663) | [PR #50382](https://github.com/qgis/QGIS/pull/50382) | Niet geschikt \-- Te riskant |
| Fix truncation of recent project list removes too many items, raises a warning | Niet gerapporteerd | [PR #50394](https://github.com/qgis/QGIS/pull/50394) | [PR #50397](https://github.com/qgis/QGIS/pull/50397) |
| Fix dizzy easter egg | [#50345](https://github.com/qgis/QGIS/issues/50345) | [PR #50380](https://github.com/qgis/QGIS/pull/50380) | Niet vereist |
| Fix point pattern fill sometimes ignores symbol opacity setting | [#48031](https://github.com/qgis/QGIS/issues/48031) | [PR #50384](https://github.com/qgis/QGIS/pull/50384) | Niet geschikt \-- Te riskant |
| Fix broken path in svg raises Qt warnings while rendering | Niet gerapporteerd | [PR #50383](https://github.com/qgis/QGIS/pull/50383) |  |
| Ensure correct expression context is used when generating symbol preview icons | [#49106](https://github.com/qgis/QGIS/issues/49106) | [PR #50393](https://github.com/qgis/QGIS/pull/50393) | Niet geschikt \-- Te riskant |
| \[spatialite\] Fix corrupted default attribute values when fields are loaded using gaiaVectorLayer | Privé gerapporteerd | [PR #50360](https://github.com/qgis/QGIS/pull/50360) | [PR #50361](https://github.com/qgis/QGIS/pull/50361) |
| Fix handling of vector tiles when zoom level 0 is not available | [#47934](https://github.com/qgis/QGIS/issues/47934) | [PR #50337](https://github.com/qgis/QGIS/pull/50337) | Niet vereist |
| Fix drag and drop of files to georeferencer window | [#49175](https://github.com/qgis/QGIS/issues/49175) | [PR #50338](https://github.com/qgis/QGIS/pull/50338) | Niet vereist |
| Never try to handle base parameter type values as map layers in QgsProcessingParameterDefinition::valueAs\* methods | [#48598](https://github.com/qgis/QGIS/issues/48598) | [PR #50327](https://github.com/qgis/QGIS/pull/50327) | Niet vereist |
| Avoid a redundant calculation of visible layer extent in overview canvas | Niet gerapporteerd | [PR #50329](https://github.com/qgis/QGIS/pull/50329) | [PR #50336](https://github.com/qgis/QGIS/pull/50336) |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Niet geschikt |
| Show standard Rendering tab in point cloud layer properties, add missing scale range widget to mesh layer properties | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | Niet geschikt |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix \"Add Ring\" tool doesn\'t consider all the overlapping features | [#23113](https://github.com/qgis/QGIS/issues/23113) | [#50447](https://github.com/qgis/QGIS/pull/50447) | Niet geschiky - voegy nieuwe methoden toe |
| Fix wkbType cast from OGR 25D Type | [#50218](https://github.com/qgis/QGIS/issues/50218) | [#50233](https://github.com/qgis/QGIS/pull/50233) | [#50251](https://github.com/qgis/QGIS/pull/50251) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://oslandia.com/)

{{<content-end >}}
