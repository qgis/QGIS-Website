---
HasBanner: false
draft: false
releaseDate: '2026-07-03'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 4.2
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 4.2{#changelog42 }
<img src="images/projects/b7fa0af07e61fe7036f463d15cbba685c11baae2.png" class="img-responsive img-rounded center-block" />

Datum uitgave: 03-07-2026

[QGIS](https://qgis.org) (<https://qgis.org>) is het populairste (open bron) desktop Geografisch InformatieSysteem (GIS) ter wereld. Het wordt gebruikt door mensen over de gehele wereld om ruimtelijke gegevens te bekijken, te bewerken, te analyseren en te delen. Het kan professioneel ogende cartografieproducten produceren en ondersteunt honderden indelingen voor ruimtelijke gegevens. QGIS is een lidproject van OSGEO, de Open Source Geospatial Foundation, die toegang tot ruimtelijke platforms democratiseert (<https://osgeo.org>).

We zijn blij om de nieuwe belangrijke uitgave van QGIS 4.2 aan te kondigen, die doorbouwt op de solide fundering van de update van de belangrijke versie 4.0 die de bron van QGIS overbracht naar het moderne framewerk van Qt6. Deze uitgave bundelt ook heel veel verbeteringen in de uitvoering en nieuw geïntroduceerde mogelijkheden, inclusief meerdere verbeteringen voor de mogelijkheden van 3D en de gereedschappen van Processing.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=5X1JKx7CXZY).

[![](https://img.youtube.com/vi/5X1JKx7CXZY/0.jpg)](https://www.youtube.com/watch?v=5X1JKx7CXZY)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten!

Als u tijd of geld wilt doneren of op een andere manier wilt bijdragen aan het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Belangrijke wijzigingen
### Mogelijkheid: Verplaatsen naar de locatie van opslag voor instellingen van QGIS4 met geautomatiseerde migratie vanuit QGIS3
Om corruptie in het configuratiebestand tussen wijzigingen die zijn gemaakt in zowel QGIS3 als in QGIS4 op hetzelfde systeem te voorkomen, worden de instellingen voor QGIS 4 nu volledig geïsoleerd in een afzonderlijke map.<br />**ONTHOUD: Dit heeft invloed op geautomatiseerde scripts voor installeren, profielbeheer en uitrollen in zakelijke omgevingen.**<br />Bij de eerste keer opstarten zal QGIS4 een kopie uitvoeren van de gegevens van het gebruikersprofiel vanuit het bestaande pad voor QGIS3 en de instellingen klonen naar een nieuw pad voor QGIS4. Geautomatiseerde uitrollen en scripts voor profielbeheer moeten worden bijgewerkt om te verwijzen naar die nieuwe locatie. Dat lost de problemen op van [\#61636](https://github.com/qgis/QGIS/issues/61636) en [\#60088](https://github.com/qgis/QGIS/issues/60088).<br />Onthoud goed:
- Dit is een EENMALIGE migratie
- De migratie behoudt de instellingen van het GELADEN GEBRUIKERSPROFIEL, zonder verlies
- Volgende wijzigingen in de profielen zullen niet worden gesynchroniseerd tussen QGIS3 en QGIS4

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Laden en opslaan van stijlen toegevoegd aan laagmenu
Dit voegt de opties **Stijl laden…** en **Stijl opslaan…** direct toe aan het laagmenu onder het submenu **Stijlen**. Dat zal gebruikers een snelle manier geven om stijl voor een laag te laden/op te slaan, zonder de noodzaak om een andere interface of menu te openen.

<img src="images/entries/3649f31a4a1358779fd933bddce5e20161257fd9.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Symbologie
### Mogelijkheid: Renderer Categorieën voor 3D-symbolen toegevoegd
Renderers Categorieën en Op regel-gebaseerd zijn nu beschikbaar voor QGIS 3D-symbologie.<br />Beide implementaties zijn soortgelijk aan de bestaande vectorrenderers voor 2D-stijlen, zodat gebruikers bekende besturingselementen hebben voor 3D-scenes, terwijl meerdere verbeteringen in de API zijn doorgevoerd om deze set krachtige functionaliteiten te ondersteunen.

<img src="images/entries/c5fb95c208d6bc03a05ac923f019475a50310cb6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Fysiek gebaseerd metaal met ondersteuning voor textuur toegevoegd
Een nieuw materiaaltype 3D voor het weergeven van op fysiek gebaseerd materiaal met volledige kaartondersteuning voor textuur is toegevoegd.<br />Texturen kunnen worden gespecificeerd voor:
- basiskleur
- metaalheid
- ruwheid
- ingesloten omgeving

<img src="images/entries/ee3d3005794174302de3f65232c8cace82357987.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Afstand verkleinen toegevoegd voor begin en eind voor gestreepte lijn- en markeringssymboollagen
Dit breidt de reeds bestaande mogelijkheden voor eenvoudige lijnen uit naar gestreepte lijnen- en markeringslijnsymboollagen.

<img src="images/entries/bb0088d635bc91e52e14fec777c191861410d687" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Data-bepaald beheer toegevoegd voor basis ruwheid metaal, emissiekleur
Een data-bepaald besturingselement voor de basis voor de ruwheid van metaal en de emissiekleur is toegevoegd. Dit sluit een van de weinige resterende gaten in de functionaliteit tussen de verouderde materialen Phong en het op fysiek gebaseerd materiaal.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Data-bepaald beheer toegevoegd voor Phong/ruwheid metaal textuurschaal, rotatie en verschuiving
Een data-bepaald besturingselement is toegevoegd voor beheer over de schaal van de textuur, rotatie en verschuiving voor 3D-polygonen, bij het gebruiken van ofwel de materialen van ruw metaal of Phong met textuur.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optionele effen emissiekleur toegevoegd voor metaal ruw materiaal
Een nieuwe, niet-standaardinstelling voor een effen emissiekleur is toegevoegd aan het metaal ruw materiaal, naast een draaiknop om ook de sterkte van de emissie te beheren. Praktisch stelt dit gebruikers in staat materialen te maken die niet worden beïnvloed door belichting van de scène.<br />De aangehechte afbeelding geeft een vergelijking weer tussen een donkere scènebelichting zonder emissie, gele emissie op 100% en gele emissie op 1000% om het het effect van deze functionaliteit te demonstreren.

<img src="images/entries/260c863c37dddb6f738615df50851b8eb06185bf.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor doorzichtbaarheid toegevoegd voor materialen ruw metaal
Op fysiek gebaseerde materialen voor renderen ondersteunen nu doorzichtbaarheid, wat hun mogelijkheden dichter bij de mogelijkheden voor het materiaal van Phong brengt.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Instellingen voor materiaal 3D toegevoegd aan stijldatabase
QGIS bevat nu ondersteuning voor het beheren van instellingen voor materiaal 3D in de stijldatabase (en het dialoogvenster Stijl beheren).<br />Gebruikers kunnen voorkeuzen van 3D-materialen maken en ze beheren naast andere stijlobjecten (bijv. toestaan van metadata, zoals taggen, favorieten, etc.).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Keuzemogelijkheid voor as omhoog/naar voren voor 3D-puntmodelsymbolen
In plaats van er altijd vanuit te gaan dat het modelbestand is gemaakt met een conventie voor de as van Z omhoog en Y naar voren, geef instellingen weer om gebruikers in staat te stellen om handmatig de assen naar voren en omhoog in te stellen. Dat maakt het gemakkelijker om willekeurige obj-bestanden, gedownload vanaf het internet, te gebruiken als 3D-puntsymbolen in QGIS. Eerdere workarounds vereisten het handmatig draaien van het symbool, maar dat verhinderde het opnieuw gebruiken van de waarden rotatie/schaal en data-bepaalde expressies die werden gebruikt door andere 3D-puntsymbolen.

<img src="images/entries/70b6d2509f1fb98c8a582a95c7abe3d58c22066a.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Extra items toegevoegd voor sjabloon van lijnsymboollaag
Gereedschappen worden nu verschaft om nieuwe markeringen/streepjes voor markerings-/gestreepte lijn-symboollaag te maken, te verplaatsen, te draaien en te verwijderen.<br />Deze nieuwe markeringen zullen dezelfde stijl delen als de originele markeringen, dezelfde geselecteerde of zichtbare status.<br />Dit is de implementatie van [QEP \#406](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/356).

<img src="images/entries/ab98e9fb9b4fd3111e4329ec44cf60c777761fd6" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia\*\*

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## 3D-objecten
### Mogelijkheid: Omgevingslicht maken vanauit skybox
Nieuwe effecten voor omgevingslicht zijn toegevoegd aan de op fysiek gebaseerde materialen als een kubus kaart-skybox aanwezig is. Omgevingslicht wordt dynamisch berekend vanuit de texturen van de skybox.<br />Deze effecten gebruiken de bolvormige harmonische schatting voor de straling om de noodzaak voor vooraf berekende texturen van straling te vermijden en om de gebruikerservaring te vereenvoudigen.<br />Dit is alleen ingeschakeld als een skybox wordt gebruikt (niet het vaste kleurverloop) en kan, indien gewenst, worden uitgeschakeld.

<img src="images/entries/80ed241c2adbea51749cc1d0d5d892ef17f7f6d6.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning instancing 3D-model
Ondersteuning voor instancing is toegevoegd voor 3D- symbolen.<br />Dit introduceert een nieuwe bibliotheek, tinyobjloader: https://github.com/tinyobjloader/tinyobjloader<br />qgsobj3dutils (soortgelijk aan qgsgltf3dutils) is gemaakt, die gegevens van OBJ laadt in geometrie, leest en maakt materiaal met textuur, als dat bestaat.<br />Andere wijzigingen:
- PhongTexturedMaterial ondersteunt nu instancing door het implementeren van setInstancingEnabled() zoals voor Phong en Gooch.
- HighlightMaterial is opnieuw bewerkt om techniek uit de aanroep voor het maken te verwijderen, en het implementeert setInstacingEnabled() met vlaggen. Dit repareert ook een probleem waar eerder 3D-modellen niet werden geaccentueerd in weergave 3D indien geselecteerd in 2D.

"En als je maar lang genoeg in een afgrond staart, staart de afgrond ook in jou".

<img src="images/entries/71e571c0902c1d2a576fe09198e69dc0cb7d479f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Toestaan van beheer over effecten voor graderen van 3D-kaartkleuren
Nieuwe instellingen worden weergegeven voor toonmappen, aanpassen van weergave en gamma voor 3D-scènes.<br />Een nieuw gedeelte "Kleurgradering" op de 3D-kaarttab "Effecten" stelt gebruikers in staat deze opties te beheren. Dit stelt gebruikers in staat om een scène aan te passen om te renderen op een manier die kleuren dramatischer maakt en verschaft hoger contrast, of gloeieffecten te gebruiken die heel helder uitgestraald licht weergeven als overbelicht licht in een nachtscène.

<img src="images/entries/460ceb890c6261ddc51ce3659dde777121d649e5.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optionele gloeieffecten voor licht
Een nieuw op fysiek gebaseerd gloeieffect voor licht is toegevoegd, wat heldere delen van de 3D-kaart een realistische gloed geeft. Dat helpt om die gebieden er feitelijk uit te laten zien alsof ze licht uitstralen, tegengesteld aan het feit dat ze slechts heldere kleuren hebben, en kunnen helpen om 3D-scènes er veel dramatischer uit te laten zien.

<img src="images/entries/0c981146a38a83d08ffff1f8c49193662e5cf725.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Multisample anti-aliasing (MSAA) toegevoegd
Een nieuwe globale 3D-instelling wordt verschaft die schakelt met het gebruiken van multisample anti-aliasing in 3D-kaarten.

<img src="images/entries/ca69a2e049f207e2a0a57f5c5d57b3420207605c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Kleurverloop achtergrond toegevoegd aan 3D-scène
QGIS ondersteunt nu te configureren kleurverlopen als achtergrondeffecten in 3D-kaartweergaven, wat gebruikers een effectief aangepast skyboxeffect zonder texturen verschaft.

<img src="images/entries/139a726cacbde4fdffaee78e66c974efbef509c3.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: 3D-tegels: ondersteuning voor instancing toegevoegd
Ondersteuning is toegevoegd voor instancing van mazen in 3D-tegels, wat gebruikers in staat stelt om efficiënt herhalende 3D-objecten weer te geven, zoals bomen of straatlantaarns, op variërende posities, rotaties en schalen. Deze implementatie poetst de complexe structurele verschillen weg tussen 3D Tiles 1.0 en 1.1 om naadloos renderen te verschaffen.
- Ondersteund in zowel kaartweergave 2D als 3D.
- 3D-weergaven gebruiken hoog efficiënt GPU-geïnstancieerd renderen.
- Ondersteunt 3D Tiles 1.0 die de indeling i3dm gebruikt.
- Ondersteunt 3D Tiles 1.1 via glTF GPU-instancing.
- Corrigeert automatisch tegelrotaties voor geprojecteerde coördinatensystemen.
- Gekwantiseerde posities en oct-gecodeerde rotaties blijven niet ondersteund.
- Object-ID's worden in deze implementatie niet gelezen.

<img src="images/entries/adb08002b421eee278c571fd52325e7e93251b69.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Natural Resources Canada

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Mogelijkheid: Impliciete tegels toegevoegd voor 3D-tegels 
Ondersteuning is toegevoegd voor impliciete tegels zoals gespecificeerd in de 3D Tiles 1.1-standaard. Deze mogelijkheid verbetert het laden en efficiënt parsen van massieve 3D-gegevenssets door gestructureerde subschema's voor onderverdeling te gebruiken.<br />Logica wordt uitgevoerd via een nieuwe bronklasse `QgsCesiumImplicitTiling`, en het quadtree schema voor onderverdeling wordt momenteel ondersteund (met mogelijke ondersteuning voor octree in een toekomstige uitgave).

<img src="images/entries/3031b5c8facbd4e11ddd450b7314d92f9684c083.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Mogelijkheid: Dialoogvenster camerabesturingselementen toegevoegd om de 3D-camera in kaartcoördinaten te kunnen beheren
Een nieuw dialoogvenster wordt verschaft om de camera te beheren die zoekt naar XYZ in 3D-kaart CRS-coördinaten, alsook het instellen van tekenreedte en hoeken voor koppen en afstand vanaf het middelpunt.<br />Het dialoogvenster krijgt een knop `Live bijwerken` die het gedrag nabootst van het paneel Laag opmaken. Indien ingesteld worden door de gebruiker gewijzigde instellingen automatisch weergegeven in de 3D-kaart.<br />Dat beïnvloedt niet het bijwerken van de waarden vanuit de 3D-kaart. Wanneer een gebruiker de camera verplaatst, worden de waarden direct bijgewerkt, ongeacht het keuzevak `Live bijwerken`.

<img src="images/entries/1f896ef8c6f67e8a925e31712a4c543525d8987c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Ondersteuning toegevoegd voor 3D-composiettegels ("cmpt")
QGIS bevat nu ondersteuning voor de 3D Tiles 1.0 specificatie [Composite Tiles](https://github.com/CesiumGS/3d-tiles/blob/main/specification/TileFormats/Composite/README.adoc#tileformats-composite-composite), die meerdere tegels (bijv. b3dm of i3dm) combineert tot een enkel bestand. Deze ondersteuning is opgenomen voor zowel renderen in 2D als in 3D.

<img src="images/entries/7196a54d0d5835b1cefa9efd8b4143c67130d5ab.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://github.com/wonder-sk)
### Mogelijkheid: Verbeterde instelling 3D-kaartweergave "Verticale as inverteren".
De instelling voor inverteren van Y voor 3D-weergaven is opnieuw bewerkt naar een configuratie op basis van een QFlag, dat een onafhankelijk bit toewijst voor elk scenario voor navigeren (bij draaien (tijdens slepen), bij draaien (muis vastgelegd) en bij draaien over terrein).
- Instellingen zijn globaal te bewerken via een op een keuzevak gebaseerd combinatievak.
- De C++-interface voor geïnverteerde voorkeuren voor Y is bijgewerkt.
- De Python-interface blijft compatibel via duck-typing.

<img src="images/entries/9ae04d9318d5c9662a84821de7c113ed1f48eb66.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [David Koňařík](https://github.com/dvdkon)
### Mogelijkheid: 3D exporteren STL
QGIS ondersteunt nu het exporteren van een 3D-scène in de indeling [STL](https://en.wikipedia.org/wiki/STL_(file_format)), in aanvulling op de bestaande exportfunctionaliteit `OBJ`. De indeling `STL` is veel eenvoudiger dan die van `OBJ` en hoeft geen texturen af te handelen.

<img src="images/entries/e0e80d41fe495959ba786ad4261a947b766ac321.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Puntenwolken
### Mogelijkheid: Optionele parameter overview-length toegevoegd aan algoritme VPC bouwen
Een nieuwe optionele parameter `--overview-length` is toegevoegd aan het algoritme Virtuele puntenwolk (VPC) bouwen

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Ondersteuning toegevoegd voor lezen van multi-overview VPC-bestanden
In plaats van het parsen van delen van overzichten op hun ID "overview", worden ze nu geparset, gebaseerd op hun rol "overview".<br />VPC -bestanden kunnen meerdere overzichten per deel bevatten met willekeurige ID's. Alle delen met de rol "overview" worden nu beschouwd als overzichten, geladen en gerenderd indien uitgezoomd.<br />`QgsPointCloudLayer` en `QgsVirtualPointCloudProvider` hebben nu een methode `overviews()` die een lijst met alle overzichten teruggeeft, in plaats van een enkele.

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Ondersteuning toegevoegd voor een virtuele puntenwolkindeling VPC-in-ZIP (.vpz)
Virtuele Puntenwolk (VPC)-bestanden kunnen behoorlijk groot worden, en de op  ASCII-gebaseerde indeling JSON helpt niet echt om de grootte beperkt te houden.<br />Opwaarderen van de nieuwe ondersteuning voor QGIS om `.vpc`-bestanden op afstand te lezen, de noodzaak voor een kleinere bestandsgrootte is duidelijker, en ondersteuning voor de indeling `.vpz`, geconstrueerd uit een gezipte `.vpc` is toegevoegd (soortgelijk aan de QGIS projectbestanden `.qgz` die een gezipte `.qgs` verschaffen).

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Per laag schaduw voor hoogte toegevoegd
QGIS ondersteunt nu per-laag schaduw voor hoogte, specifiek voor puntenwolklagen. Deze mogelijkheid verschaft fijner visueel beheer, en vermijdt het mengen en renderen van artefacten die kunnen verschijnen als globale schaduw voor hoogte wordt toegepast over de gehele kaartscène.
- Beheerd via uitgebreide gebruikersinterface in 2D-symbologie.
- Omzeilt artefacten van globale schaduw voor hoogte helemaal.
- Voorkomt ongewenst mengen van afzonderlijke kaartelementen.

<img src="images/entries/41a69a819d5d1446c2bcf2ddfcc4319bdb3b9f39.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Ondersteuning voor rekenkundige operatoren voor kleurobjecten in expressies
QGIS ondersteunt nu direct het aanpassen van kleurobjecten in gegevens van puntenwolken binnen expressies, met rekenkundige basisbewerkingen. Dat vereenvoudigt het dynamisch manipuleren van kleuren door automatisch die kleur op te splitsen in zijn basiscomponenten en de wiskundige bewerking toe te passen op elk kanaal, wat de noodzaak elimineert voor complexe formules voor het uitnemen van componenten.
- Rekenkundige bewerkingen direct toepassen op onderliggende kanalen RGBA.
- Vermenivuldigen werkt met de kleur aan beide zijden.
- Andere bewerkingen vereisen de kleur aan de linkerkant.
- Deze mogelijkheid vermijdt complexe formules voor het uitnemen van kleurcomponenten.
- Dynamische schaduw, gebaseerd op attributen, is enorm vereenvoudigd.

Bijvoorbeeld:

`@point_color * scale_linear( @NumberOfReturns, 0, 8, 0.5, 1 )`

<img src="images/entries/d215e96ce1bf086ec558dbf3587894a22cc75af1.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
### Mogelijkheid: Kleur voor renderen aanpassen met expressie
Een aanvullende aanpassing is toegevoegd aan de renderer voor puntewolken die het mogelijk maakt expressies te gebruiken voor het aanpassen van kleuren.<br />Alle attributen van puntenwolken mogen in de expressie worden gebruikt, alsook de basiskleur van de renderer. Gebruikers kunnen de waarde van de basiskleur combineren met een ander attribuut van het punt, zoals intensity, om een beter resultaat te produceren voor classificeren van punten en opmaak.<br />Bijvoorbeeld:<br />`@point_color * (@intensity / 65535)`

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Afdruklay-outs
### Mogelijkheid: Nieuwe functionaliteit voor lay-outitem Diagram toegevoegd om gegevens voor plot en opmaak af te leiden uit de renderer voor de bronvectorlaag
Nieuwe instellingen zijn toegevoegd aan het lay-outitem Diagram
- een keuzevak 'Categorieën maken uit laagsymbologie' om de serie voor X in het plot overeen te laten komen met de categorieën van de renderer voor de bronvectorlaag
- een keuzevak 'Kleuren laagsymbologie toepassen' om de gerenderde diagrammen de kleuren te laten overnemen van het symbool dat is verbonden met de renderer van de vectorlaag

De gebruiker kan ofwel kiezen voor een blanco serie om het aantal overeenkomende objecten te *tellen*, of kan ervoor kiezen om een aangepaste expressie voor Y te maken (een eenvoudige expressie voor een veld of een heel complexe expressie) om te komen tot een aangepaste som (zeg de lengte van lijnen of een attribuut dat verwijst naar een waarde die kan worden opgeteld, etc.)

<img src="images/entries/ba82a958973bddc5c128c2b24c7cd249a81d737c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Nieuwe optie toegevoegd om een item Afbeelding bij te snijden naar een op een vorm gebaseerd item
QGIS verschaft nu de mogelijkheid om een item Afbeelding in een lay-out te clippen naar een op een vorm gebaseerd item.<br />Dat geeft een fantastische manier om mooie vormen en maskerelementen te framen met afbeeldingen (of dynamisch gedreven door een attribuut van een object van atlas of een statische afbeeldingsbron).<br />Het clippen wordt ingeschakeld en geconfigureerd binnen een nieuw gedeelte van het paneel Eigenschappen voor items Afbeelding.

<img src="images/entries/08cbd88117433df3beb02050b1e690886b7ee27b.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Verbetering voor georuimtelijk beheer PDF-laag
Nieuwe opties zijn toegevoegd om ervoor te zorgen dat exporteren naar georuimtelijk PDF de configuratie voor de boomstructuur van de lagen van QGIS volgt (groepen, volgorde, namen, zichtbaarheid, groepslagen). Dat maakt het voor gebruikers mogelijk de laagstructuur te behouden, inclusief geneste groepen, bij het exporteren naar een georuimtelijke PDF. Deze functionaliteit wordt ondersteund in afdruklay-outs, maar niet in standaardtaken voor het renderen van kaarten.
- De mogelijkheid vereist een kaart zonder vergrendelde lagen.
- Zowel zichtbare als onzichtbare projectlagen worden geëxporteerd.
- PDF's renderen aangepaste volgorden, waarbij de standaard boomstructuur wordt behouden.
- Attributen van objecten worden geëxporteerd voor alle lagen of niet.
- Groepslagen worden ondersteund als enkele kaartlagen.
- Overeenkomende groepen PDF handelen de zichtbaarheid van lay-outitems direct af.
- Niet-overeenkomende PDF-groepen verschijnen aan de onderzijde van de boom.
- Elkaar uitsluitende groepen worden momenteel niet ondersteund.

<img src="images/entries/c4c92f09dc1381fac13768b1b52a192c9ed64eb8.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door de stad Bern

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
## Expressies
### Mogelijkheid: Toegevoegde expressiefunctie scale_cubic_bezier, afhandelen interpolatie bezier-cubic bij het converteren van stijlen van MapBox
Complementeert de bestaande functies scale_linear, scale_exponential en voegt een nieuwe methode voor op bezier-cubic gebaseerde interpolatie toe. Dat wordt dan gebruikt bij het converteren van stijlen van MapBox met het interpolatietype "cubic-bezier".

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Expressiefunctie concat_ws toegevoegd
Voegt alle, behalve het eerste, argumenten met scheidingstekens samen. De eerste parameter wordt als een scheidingsteken gebruikt.<br />Argumenten NULL worden genegeerd.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensbeheer
### Mogelijkheid: Menu-item "Veldberekening openen" toegevoegd aan de kop van de attributentabel
Een nieuw menu-item "Veldberekening openen" wordt verschaft in het contextmenu van kolomkoppen in de attributentabel van een vectorlaag.<br />Het venster Veldberekening zal openen met het keuzevak "Bestaande velden vernieuwen" automatisch geselecteerd en het corresponderende veld al geselecteerd in het combinatievak.<br />De actie wordt alleen ingeschakeld voor bewerkbare velden.

<img src="images/entries/8ade61ae18cd9ec8014958f35d175ed4e5d0ed4f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Patrice Pineault](https://github.com/TurboGraphxBeige)
## Processing
### Mogelijkheid: Dynamische objecttellingen van kindstap weergeven als het model voortgaat
Als het model wordt uitgevoerd met het dialoogvenster Modelontwerper, zal QGIS nu een bijgewerkte telling weergeven van objecten die door de links van het model stromen. Een nieuw flexibel item "badge" dat is verbonden aan pijlen werd geïntroduceerd om dit te bereiken.<br />Opmerking:
- We geven nu ook uitvoer voor tellingen van niet-objecten weer in de badges voor pijlen, dus, bijv. de waarde van numerieke uitvoer, die is verbonden met een ander algoritme, wordt weergegeven. (Tekenreeksen worden afgebroken om een rommelige gebruikersinterface te voormijden.)
- Badges erven nu de middelste kleur van hun geassocieerde pijllijnen.
- Om redenen van uitvoering zijn de bijwerkingen voor de telling van objecten beperkt tot slechts elke 100 objecten.
- Omdat niet alle algoritmes de voortgang van dynamisch tellen van objecten rapporteren (bijv. die welke zijn gebaseerd op plug-ins van derde partijen doen dat niet, ten minste niet totdat de auteur van de plug-in hiervoor de opgewaardeerde API gebruikt), zal QGIS altijd de tellingen van objecten bijwerken met hun exacte uiteindelijke telling als het model de uitvoering voltooid. Voor die modellen zal de gebruiker de telling van de pijlen in één keer zien bijgewerkt aan het einde van het model, niet als dat kind wordt uitgevoerd.

<img src="images/entries/e78e514a83f210185705a81bc6e1a8311bc025c0.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Een parameter voor een drempel voor een gebied toegevoegd
Het gereedschap voor Processing voor het controleren van gaten bevat nu een drempelgrootte die het voor gebruikers mogelijk maakt de teruggegeven resultaten te filteren. Als het gehele gebied groter is dan de opgegeven drempelwaarde, dan wordt het gat niet als een fout beschouwd.

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
### Mogelijkheid: Ondersteuning toegevoegd voor SFCGAL  parameter extendToEdges in het algoritme voor schatten van de mediale as
Met SFCGAL 2.3 heeft het algoritme voor het schatten van de mediale as een nieuwe parameter `extendToEdges`. Als deze parameter is geactiveerd, worden de eindpunten van de mediale as uitgebreid tot de grens van de invoerpolygoon. De bijgevoegde afbeelding illustreert het verschil voor het uitvoeren van het algoritme voor het schatten van de mediale as met deze optie respectievelijk ingesteld op false (rood) en true (groen).

<img src="images/entries/d1cf8c4c5dd1ef1d172745817db02a6e2628191e.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Processing in een door de gebruiker gedefinieerd menu of werkbalk toevoegen
Gebruikers kunnen nu een actie voor een algoritme van processing toevoegen aan een door de gebruiker aangepast menu of werkbalk. Indien geactiveerd, zullen deze acties een dialoogvenster openen voor het invullen van de parameters en het geassocieerde algoritme voor Processing uitvoeren.

<img src="images/entries/5ae9ce29dd7d2e8a7b094e3f7c129171af8a6d8f" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stadt Frankfurt am Main en Oslandia

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Subset van algoritmes Willekeurig geporteerd naar C++
De Processing algoritmes Willekeurig uitnemen binnen subsets en Willekeurige selectie binnen subsets zijn geporteerd van Python naar C++, wat een betere uitvoering geeft.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
## Opties voor toepassing en projecten
### Mogelijkheid: Topocentrische projectie
Topocentrische ondersteuning voor CRS is toegevoegd aan QGIS, met een nieuwe widget die wordt verschaft voor het instellen van een punt van oorsprong van de projectie, die wordt ingeschakeld als gebruikers expliciet een optie voor een Topocentrisch CRS selecteren in het selectiemenu van het CRS.

<img src="images/entries/405bc086bd84189e5113544155ac4ef7d85ed836.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Sensoren
### Mogelijkheid: Ondersteuning toegevoegd voor SensorThings 2.0, inclusief de uitbreidingen Sensing, Sampling en Relations
QGIS bevat nu ondersteuning voor lagen die specificaties voor SensorThings 2.0 gebruiken, inclusief de nieuwe uitbreidingen Sensing, Sampling en Relations.<br />Dit geeft deze keuzes ook weer voor services die zijn ingeschakeld voor SensorThings 2.0. De versie van de service en de uitbreidingen worden dynamisch bepaald tijdens het verbinden met een service via de Browser of Databronnen beheren.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Profiel plotten
### Mogelijkheid: Profielboog hoogte weergeven in 3D
QGIS verschaft nu een optie "Profiel in 3D-weergaven weergeven" in het menu voor de instellingen van het profielplot, wat het inschakelen van het weergeven van de profielboog voor de hoogte in 3D mogelijk maakt.<br />De boog wordt opgehaald uit het hoogteprofiel en waarden Z worden ingesteld vanuit de berekende minimale en maximale waarden van de gegevens die passen binnen de boog.<br />Polygoon- en lijn-elastieken volgen de cursor om weer te geven over welke positie in het hoogteprofiel de gebruiker momenteel beweegt.

<img src="images/entries/51b9332232c56ecf122b5d6205744c01a2371e42.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric](https://github.com/ViperMiniQ)
## Browser
### Mogelijkheid: Opnieuw bewerkt hoe services van ESRI REST worden weergegeven in de Browser
Wijzigingen zijn gemaakt om de inhoud van de service ESRI REST minder rommelig te maken in de Browser:
- De duplicate items voor dezelfde service die worden weergegeven als zowel kaartserver (raster) als objectenserver (vector) worden nu verborgen. In plaats daarvan wordt alleen het item van de objectenserver weergegeven en is de mogelijkheid voor het laden als een raster verplaatst naar het rechtermuisklikcontextmenu in het item. Dit bootst na hoe ArcPro deze services weergeeft, met de uitzondering dat het ALLEEN toestaat dat ze als vectors worden geladen. Er is geen mogelijkheid om te laden als een raster als de service de mogelijkheid query weergeeft.
- We geven niet langer een pseudolaag "Alle lagen" weer voor items van de kaartserver. In plaats daarvan werd deze functionaliteit verplaatst naar het rechtermuisklikcontextmenu voor het item van de kaartservice. Dat vermijdt het dichtslibben van de inhoud voor de service in de Browser met zelden gebruikte items die niet corresponderen met de feitelijke inhoud van de service.

Dit werd mogelijk gemaakt door Republiek en Kanton Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Enorme versnelling voor de provider FeatureServer voor het bekijken van kaarten
QGIS heeft een significant krachtiger opnieuw uitgewerkte benadering gebruikt voor het ophalen van gegevens voor de provider FeatureServer, wat het aantal vereiste verzoeken terugdringt om een subset op te halen van de objecten in een bepaald kaartbereik.<br />Onthoud dat het feitelijke TOTALE aantal verzoeken om ELK object uit de service op te halen niet wijzigt, dus, bijvoorbeeld, openen van de attributentabel zou resulteren in hetzelfde totale aantal verzoeken.

<img src="images/entries/e3ea1f5568a403cb6c293d963c0b04351df8ea21.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Republiek en Kanton Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Parallel laden vanaf provider inschakelen voor providers AFS, AMS en enkele gerelateerde reparaties
QGIS heeft parallel laden vanaf provider ingeschakeld voor de providers ArcGIS FeatureServer/MapServer, wat veel snellere opstarttijden geeft om een project te laden als een project meerdere lagen van FeatureServer/MapServer bevat.

Dit werd mogelijk gemaakt door Republiek en Kanton Genève

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor onderdelen van STAC uit andere voor de cloud geoptimaliseerde gegevenstypen en opslag voor blobs
QGIS heeft ondersteuning toegevoegd voor onderdelen van STAC uit andere voor opslagproviders voor de cloud, inclusief Azure en Google.<br />Dit breidt de ondersteuning, naast GeoTiff, aanvullend uit naar andere voor de cloud geoptimaliseerde gegevenstypen. Zoals JPEG2000, TileDB, Point Clouds, en andere, vooropgesteld dat ze zijn gepubliceerd met een toepasselijk gelabeld mimetype `cloud-optimized` of een ondersteunde declaratie voor het type onderdeel.

Deze mogelijkheid werd ontwikkeld door [Norman Barker](https://github.com/normanb)
## QGIS Server
### Mogelijkheid: Ondersteuning toegevoegd voor opties van WMS parameters HIGHLIGHT_LABELFRAME
Nieuwe parameters voor services van WMS maken het mogelijk eigenschappen voor framestijlen voor labels te configureren, inclusief:
- `HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINECOLOR`
- `HIGHLIGHT_LABELFRAMEOUTLINEWIDTH`
- `HIGHLIGHT_LABELFRAMESIZE`

Bijvoorbeeld:

`&MAP0:HIGHLIGHT_LABELFRAMEBACKGROUNDCOLOR=%23FF0000`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINECOLOR=%230000FF`<br />`&MAP0:HIGHLIGHT_LABELFRAMESIZE=5`<br />`&MAP0:HIGHLIGHT_LABELFRAMEOUTLINEWIDTH=2`

<img src="images/entries/e2ce00c7b18b3fbb012ee8e08e0def43db4959c5.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Sandro Mani](https://github.com/manisandro)
### Mogelijkheid: FlatGeobuf OAPIF exporteren plus verscheidene reparaties
De indeling voor exporteren FlatGeobuf is toegevoegd aan de QGIS Server OAPIF-service, geïmplementeerd in lijn met [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md)

Dit werd mogelijk gemaakt door [QGIS gebruikersgroep Duitsland (QGIS Anwendergruppe Deutschland e.V.)](https://www.qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Programmeerbaarheid
### Mogelijkheid: Functionaliteit voor het weergeven van de holle schil van polygonen
QGIS ondersteunt nu het algoritme Concave Hull of Polygons van GEOS dat werd weergegeven in PyQGIS.
1. Maakt invoer van polygoon- (en lijn-) objecten mogelijk voor het algoritme Concave Hull by Feature. Eerder zou een gebruiker eerst de punten moeten uitnemen uit de polygoon om de holle schil vanuit de punten te berekenen, maar die benadering negeert het interieur van de polygoon.
2. Voegt een toegewezen algoritme "Gaten tussen polygonen vullen" toe:

Anders dan het standaardalgoritme Holle schil is Gaten tussen polygonen vullen een (mogelijk) niet holle polygoon die alle invoerpolygonen bevat. De berekende schil vult de gaten tussen de polygonen zonder hun interieuren te kruisen. Het volgt strikt de buitengrenzen van de invoerpolygonen, en stelt u in staat de gaten tussen hen te vullen zonder hun originele vormen te vervormen. Het is in het bijzonder nuttig voor gevallen zoals het generaliseren van groepen omtrekken van gebouwen, maken van 'district'-polygonen rondom blokken, of het verwijderen van gaten en het verbinden van losse sets polygonen. Bekijk https://lin-ear-th-inking.blogspot.com/2022/05/concave-hulls-of-polygons.html?m=1 voor meer details

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| .ASC missing from Raster Extraction | [\#66319](https://github.com/qgis/QGIS/issues/66319) | [PR \#66368](https://github.com/qgis/QGIS/pull/66368) | N/B |
| \[OAPIF\] Zooming triggers download of already loaded data | [\#66358](https://github.com/qgis/QGIS/issues/66358) | Is geen probleem |  |
| Gdb format in QGIS will show also .gdbtable .gdbtablex not only as .gdb | [\#66279](https://github.com/qgis/QGIS/issues/66279) | Geen bug / niet gewenst |  |
| Expose AZURE_STORAGE_SAS_TOKEN configuration option in Browser Cloud Storage Connection | [\#66274](https://github.com/qgis/QGIS/issues/66274) | [PR \#14731](https://github.com/OSGeo/gdal/pull/14731) | N/B |
| Filtering WFS causes total failure to display layer | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) | [PR \#66373](https://github.com/qgis/QGIS/pull/66373) |
| \[OAPIF\]\[server\] Paging not working with format FlatGeobuf from QGIS Server | [\#66365](https://github.com/qgis/QGIS/issues/66365) | [PR \#66399](https://github.com/qgis/QGIS/pull/66399) | N/B |
| Gml to Gml- Conversion succeeded, input and output are not the same in QGIS | [\#66413](https://github.com/qgis/QGIS/issues/66413) | Is geen probleem |  |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | [PR \#66510](https://github.com/qgis/QGIS/pull/66510) | [PR \#66539](https://github.com/qgis/QGIS/pull/66539) |
| Raster attribute table: convert empty DateTime as string coming from GDAL to NULL value | [\#66544](https://github.com/qgis/QGIS/issues/66544) | [PR \#66547](https://github.com/qgis/QGIS/pull/66547) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/en/home/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsSettings + QGIS4.ini + XYZ Tile provider = crash | [\#66424](https://github.com/qgis/QGIS/issues/66424) | [PR \#66450](https://github.com/qgis/QGIS/pull/66450) | N/B |
| Cannot load VT layer from style only from the dialog (works in browser) | niet gerapporteerd | [PR \#66500](https://github.com/qgis/QGIS/pull/66500) | NOG TE DOEN |
| "fix" every entry in relation reference widget is shown in italic | niet gerapporteerd | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud (OPENGIS.ch)](http://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[OAPIF\] QGIS Server OGC API is detected as WFS 1.1 | [\#66362](https://github.com/qgis/QGIS/issues/66362) | [PR \#66369](https://github.com/qgis/QGIS/pull/66369) | N/B |
| \[OAPIF\] Changing feature format has no effect | [\#66359](https://github.com/qgis/QGIS/issues/66359) | [PR \#66386](https://github.com/qgis/QGIS/pull/66386) | N/B |
| represent_value not working | [\#66339](https://github.com/qgis/QGIS/issues/66339) | [PR \#66392](https://github.com/qgis/QGIS/pull/66392) | [PR \#66436](https://github.com/qgis/QGIS/pull/66436) |
| Remove &key=pk from memory layers tests | [\#66350](https://github.com/qgis/QGIS/issues/66350) | [PR \#66397](https://github.com/qgis/QGIS/pull/66397) | N/B |
| \[server\] Fix network cache settings read from environment | [\#59613](https://github.com/qgis/QGIS/issues/59613) | [PR \#66425](https://github.com/qgis/QGIS/pull/66425) | N/B |
| \[postgres\] Fix json/b bytea add feature in transaction group | [\#65323](https://github.com/qgis/QGIS/issues/65323) | [PR \#66478](https://github.com/qgis/QGIS/pull/66478) | N/B |
| Unable to load style from datasource database for non geometry layers. | [\#66341](https://github.com/qgis/QGIS/issues/66341) | [PR \#66486](https://github.com/qgis/QGIS/pull/66486) | N/B |
| \[expressions\] Fix IN operator nodes() | [\#66313](https://github.com/qgis/QGIS/issues/66313) | [PR \#66485](https://github.com/qgis/QGIS/pull/66485) | [PR \#66499](https://github.com/qgis/QGIS/pull/66499) |
| No timeout for vsicurl layers when loading a project | [\#66496](https://github.com/qgis/QGIS/issues/66496) | Kan niet worden gereproduceerd |  |
| Field calculator allowed string \* float operation and program crashed | [\#66507](https://github.com/qgis/QGIS/issues/66507) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/B |
| Calculating integer field by "id"=@row_number crashed QGIS on save action | [\#66268](https://github.com/qgis/QGIS/issues/66268) | [PR \#66508](https://github.com/qgis/QGIS/pull/66508) | N/B |
| Crash when attempting to load OpenHistoricalMap vector tiles | [\#66466](https://github.com/qgis/QGIS/issues/66466) | [PR \#66533](https://github.com/qgis/QGIS/pull/66533) | N/B |
| Data-defined override expression on a field is not evaluated until any field in the form is edited | [\#66504](https://github.com/qgis/QGIS/issues/66504) | Kan niet worden gereproduceerd |  |
| Export to PostgreSQL (Available Connection) drops source table | [\#66228](https://github.com/qgis/QGIS/issues/66228) | [PR \#66536](https://github.com/qgis/QGIS/pull/66536) | [PR \#66570](https://github.com/qgis/QGIS/pull/66570) |
| Spatialite data types are not recognized correctly when creating query layers with SQL | [\#66329](https://github.com/qgis/QGIS/issues/66329) | [PR \#66538](https://github.com/qgis/QGIS/pull/66538) | N/B |
| Edit layer properties of an invalid layer (broken source) is not working | [\#66324](https://github.com/qgis/QGIS/issues/66324) | [PR \#66607](https://github.com/qgis/QGIS/pull/66607) | Niet aanbevolen |
| Qgis have problem to render GeometryCollection for Gml, other viewer like mygeodata website render ok | [\#66225](https://github.com/qgis/QGIS/issues/66225) | Duplicaat |  |
| 3.44.7-Solothurn Crashes on New Shapefile | [\#66220](https://github.com/qgis/QGIS/issues/66220) | [PR \#66609](https://github.com/qgis/QGIS/pull/66609) | [PR \#66648](https://github.com/qgis/QGIS/pull/66648) |
| Add inja escape() function to HTML escape values | [GHSA-cr49-pm9v-m788](https://github.com/qgis/QGIS/security/advisories/GHSA-cr49-pm9v-m788) | [PR \#66616](https://github.com/qgis/QGIS/pull/66616) | [PR \#66670](https://github.com/qgis/QGIS/pull/66670) |
| Regression with decimal values and negative number in color gradient in the layer style panel | [\#65566](https://github.com/qgis/QGIS/issues/65566) | [PR \#66619](https://github.com/qgis/QGIS/pull/66619) | [PR \#66671](https://github.com/qgis/QGIS/pull/66671) |
| QGIS Server: GetProjectSettings returns the error message "Layer(s) not valid" with two WMS layers | [\#65872](https://github.com/qgis/QGIS/issues/65872) | Kan niet worden gereproduceerd |  |
| raster histogram not working for raster with scale factor | [\#65920](https://github.com/qgis/QGIS/issues/65920) | [PR \#66640](https://github.com/qgis/QGIS/pull/66640) | NOG TE DOEN |
| Advanced Digitizing Floater is not wide enough to show whole value | [\#65171](https://github.com/qgis/QGIS/issues/65171) | [PR \#66663](https://github.com/qgis/QGIS/pull/66663) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Custom Toolbar Position Loss | [\#65862](https://github.com/qgis/QGIS/issues/65862) | [PR \#66483](https://github.com/qgis/QGIS/pull/66483) | N/B |
| Export to PDF from layout changes colors | [\#42935](https://github.com/qgis/QGIS/issues/42935) | Geen probleem (Was naar mijn mening een probleem van Adobe) |  |
| Layout bleeding to edge outside map window | [\#49638](https://github.com/qgis/QGIS/issues/49638) | Gerepareerd |  |
| Fix flaky test_gui_fileuploader | Niet gerapporteerd | [PR \#66543](https://github.com/qgis/QGIS/pull/66543) |  |
| Hidden actions from user defined toolbar are still visible. | Niet gerapporteerd | [PR \#66620](https://github.com/qgis/QGIS/pull/66620) |  |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [\#58303](https://github.com/qgis/QGIS/issues/58303) | [PR \#66621](https://github.com/qgis/QGIS/pull/66621) | NOG TE DOEN |
| Password is not removed when it's at the the end of uri | Niet gerapporteerd | [PR \#66625](https://github.com/qgis/QGIS/pull/66625) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Germán Carrillo (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Allow QGIS to access curves from OGC API provider | Niet gerapporteerd | [PR \#66452](https://github.com/qgis/QGIS/pull/66452) | N/B |
| Elevation profile - changing layer symbology crashes QGIS / Wrong rendering order of Elevation profile items after changing the color of a profile item / Elevation profile stops respecting layer order on layer properties change | [\#64952](https://github.com/qgis/QGIS/issues/64952), [\#62677](https://github.com/qgis/QGIS/issues/62677), [\#64806](https://github.com/qgis/QGIS/issues/64806) | [PR \#66360](https://github.com/qgis/QGIS/pull/66360) | N/B |
| QGIS crashes on registering a Custom Profile Source with 'Sync Layers to Project' active | [\#65056](https://github.com/qgis/QGIS/issues/65056) | [PR \#66455](https://github.com/qgis/QGIS/pull/66455) | N/B |
| QGIS hangs when opening raster calculator (Meu Qgis está travando ao tentar abrir a calculadora raster) | [\#66327](https://github.com/qgis/QGIS/issues/66327) | Kan niet worden gereproduceerd |  |
| Ensure consistency in MultiCurves: don't allow NurbsCurves | Niet gerapporteerd | [PR \#66676](https://github.com/qgis/QGIS/pull/66676) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door David Signer (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix field displayString on primitive JSON values | Niet gerapporteerd | [PR \#66575](https://github.com/qgis/QGIS/pull/66575) | N/B |
| Fix bad behavior on widget detection of JSON fields | [\#62377](https://github.com/qgis/QGIS/issues/62377) | [PR \#66494](https://github.com/qgis/QGIS/pull/66494) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://opengis.ch)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis (Lutra Consulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Windows QGIS 4 installs plugin with ACL that do not include SYSTEM or Administrators | [\#66515](https://github.com/qgis/QGIS/issues/66515) | [PR \#66576](https://github.com/qgis/QGIS/pull/66576) | N/B |
| Crash when clicking on an unavailable layer in Layers panel | [\#65913](https://github.com/qgis/QGIS/issues/65913) | [PR \#66578](https://github.com/qgis/QGIS/pull/66578) | NOG TE DOEN |
| QGIS server OGC API: Limits and offset parameters ignored when plugin changing parameters | [\#65858](https://github.com/qgis/QGIS/issues/65858) | Gerepareerd | [PR \#66480](https://github.com/qgis/QGIS/pull/66480) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Unbreak QGIS with GDAL \>= 3.13 | [commit ffdb8e3](https://github.com/qgis/QGIS/commit/ffdb8e3b27035478c533f37087505e749cc15b9b) | [PR \#66615](https://github.com/qgis/QGIS/pull/66615) | N/B |
| concat() returns NULL when all arguments are NULL: it should return an empty string | [\#65808](https://github.com/qgis/QGIS/issues/65808) | [PR \#66618](https://github.com/qgis/QGIS/pull/66618) | NOG TE DOEN |
| Remove all the parts in a geometry creates an empty geometry instead of NULL | [\#65453](https://github.com/qgis/QGIS/issues/65453) | Werk nog gaande | NOG TE DOEN / Niet aanbevolen? |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Deleted last series still visible in chart | [\#63466](https://github.com/qgis/QGIS/issues/63466) | Kan niet worden gereproduceerd |  |
| Grey out "Use only features intersecting atlas features" for layout chart item if no atlas is activated | [\#65612](https://github.com/qgis/QGIS/issues/65612) | [PR \#66283](https://github.com/qgis/QGIS/pull/66283) | N/B |
| DB Manager | [\#59470](https://github.com/qgis/QGIS/issues/59470) | Kan niet worden gereproduceerd |  |
| "Generate elevation profile image" algorithm doesn't propose image formats for output file | [\#64915](https://github.com/qgis/QGIS/issues/64915) | [PR \#66286](https://github.com/qgis/QGIS/pull/66286) | [PR \#66445](https://github.com/qgis/QGIS/pull/66445) |
| Ubuntu 23.04 \| /usr/lib/qgis/plugins/libplugin_grass8.so \| lib not loadable | [\#55159](https://github.com/qgis/QGIS/issues/55159) | Geen probleem/terugkoppeling |  |
| Returned result of layer_property (layer, 'type') is dependent of UI language | [\#65009](https://github.com/qgis/QGIS/issues/65009) | [PR \#66300](https://github.com/qgis/QGIS/pull/66300) | [PR \#66446](https://github.com/qgis/QGIS/pull/66446) |
| Advanced digitizing floater should not allow editing every fields | [\#65173](https://github.com/qgis/QGIS/issues/65173) | [PR \#66303](https://github.com/qgis/QGIS/pull/66303) | [PR \#66447](https://github.com/qgis/QGIS/pull/66447) |
| Join attributes by location (summary) count returns Null | [\#40108](https://github.com/qgis/QGIS/issues/40108) | [PR \#66322](https://github.com/qgis/QGIS/pull/66322) | [PR \#66448](https://github.com/qgis/QGIS/pull/66448) |
| Qt6 porting: use size_t for qHash() return | [\#44351](https://github.com/qgis/QGIS/issues/44351) | [PR \#66477](https://github.com/qgis/QGIS/pull/66477) | N/B |
| Image source file chooser does not start in the program symbol library folder (Windows) | [\#37308](https://github.com/qgis/QGIS/issues/37308) | [PR \#66342](https://github.com/qgis/QGIS/pull/66342) | [PR \#66449](https://github.com/qgis/QGIS/pull/66449) |
| TestQgsProcessingAlgsPt2::exportMeshOnGrid() | [\#48605](https://github.com/qgis/QGIS/issues/48605) | Kan niet worden gereproduceerd |  |
| TestQgsProcessingAlgs::convertGpsData() fails | [\#45588](https://github.com/qgis/QGIS/issues/45588) | Kan niet worden gereproduceerd/Is geen probleem |  |
| gdal:merge parameter OPTIONS not shown with execAlgorithmDialog | [\#66396](https://github.com/qgis/QGIS/issues/66396) | Is geen probleem |  |
| projects/anonymize_saved_projects doesn't seem to be available in the new settings tree | [\#65844](https://github.com/qgis/QGIS/issues/65844) | Is geen probleem |  |
| bug for .Shp namefile | [\#62655](https://github.com/qgis/QGIS/issues/62655) | Is geen probleem |  |
| Build virtual point cloud (VPC): dialog adds .las extension for output | [\#61934](https://github.com/qgis/QGIS/issues/61934) | Kan niet worden gereproduceerd |  |
| QGIS claims to be able to open all .jpg file (on Lubuntu) | [\#60911](https://github.com/qgis/QGIS/issues/60911) | [PR \#66472](https://github.com/qgis/QGIS/pull/66472) |  |
| QGIS wants to open all .json files, including ones unrelated to any geodata | [\#61215](https://github.com/qgis/QGIS/issues/61215) | Kan niet worden gereproduceerd |  |
| Matrix distance does not output right fields when using N x T matrix type | [\#29165](https://github.com/qgis/QGIS/issues/29165) | [PR \#66101](https://github.com/qgis/QGIS/pull/66101) |  |
| Distance Matrix returns wrong record/result when using Linear Distance Matrix with k=1 | [\#45493](https://github.com/qgis/QGIS/issues/45493) | [PR \#66101](https://github.com/qgis/QGIS/pull/66101) |  |
| QLR files not associated with QGIS | [\#56844](https://github.com/qgis/QGIS/issues/56844) | Kan niet worden gereproduceerd |  |
| TestQgsDatumTransformDialog fails | [\#48883](https://github.com/qgis/QGIS/issues/48883) | Kan niet worden gereproduceerd |  |
| TestProcessingGui::testDatabaseSchemaWrapper() Caught unhandled exception | [\#48885](https://github.com/qgis/QGIS/issues/48885) | Kan niet worden gereproduceerd |  |
| Layout arrow item has start marker in wrong direction | [\#59078](https://github.com/qgis/QGIS/issues/59078) | [PR \#66558](https://github.com/qgis/QGIS/pull/66558) |  |
| User Defined CRS gets lost | [\#57806](https://github.com/qgis/QGIS/issues/57806) | [PR \#66572](https://github.com/qgis/QGIS/pull/66572) |  |
| Raster Tools - Generate XYZ Tiles (Directory) always creates 0 tiles | [\#60069](https://github.com/qgis/QGIS/issues/60069) | Is geen probleem |  |
| Error in counting tiles in each levels in Generate XYZ tiles (Directory) | [\#62157](https://github.com/qgis/QGIS/issues/62157) | [PR \#66606](https://github.com/qgis/QGIS/pull/66606) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix deadlock when rendering annotation layers | Niet gerapporteerd | [PR \#66712](https://github.com/qgis/QGIS/pull/66712) | [PR \#66742](https://github.com/qgis/QGIS/pull/66742) |
| Fix crashes in QgsFeatureListComboBox if layer is unloaded | Niet gerapporteerd | [PR \#66697](https://github.com/qgis/QGIS/pull/66697) | [PR \#66708](https://github.com/qgis/QGIS/pull/66708) |
| Every entry in relation reference widget is shown in italic | Niet gerapporteerd | [PR \#66649](https://github.com/qgis/QGIS/pull/66649) | Niet van toepassing |
| Fix buggy processing relief colors widget | Niet gerapporteerd | [PR \#66602](https://github.com/qgis/QGIS/pull/66602) | Niet van toepassing |
| Fix QgsImageCache lossy conversion of images | Niet gerapporteerd | [PR \#66585](https://github.com/qgis/QGIS/pull/66585) | Niet van toepassing |
| Fix crash when setting 3d skybox to non-square textures | [\#66560](https://github.com/qgis/QGIS/issues/66560) | [PR \#66580](https://github.com/qgis/QGIS/pull/66580) | N/B |
| Fix intermittent failure of GRASS raster tests | Niet gerapporteerd | [PR \#66546](https://github.com/qgis/QGIS/pull/66546) | N/B |
| Fix symbology sizing issues on hidpi displays | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66531](https://github.com/qgis/QGIS/pull/66531) | Niet van toepassing |
| Fix symbology sizing issues on hidpi displays | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66530](https://github.com/qgis/QGIS/pull/66530) | Niet van toepassing |
| Fix broken color wheel widget on devices with pixel ratios | [\#55349](https://github.com/qgis/QGIS/issues/55349) | [PR \#66529](https://github.com/qgis/QGIS/pull/66529) | Niet van toepassing |
| Use correct lossless method to store metal rough colors | Niet gerapporteerd | [PR \#66521](https://github.com/qgis/QGIS/pull/66521) | N/B |
| Ensure color picker opens inline for 3d settings in style dock | Niet gerapporteerd | [PR \#66520](https://github.com/qgis/QGIS/pull/66520) | Niet van toepassing |
| Fix misalignment of spin boxes in color dialog | Niet gerapporteerd | [PR \#66498](https://github.com/qgis/QGIS/pull/66498) | Niet van toepassing |
| Use unlit material instead of phong material when more appropriate | Niet gerapporteerd | [PR \#66490](https://github.com/qgis/QGIS/pull/66490) | Niet van toepassing |
| Loosen the maximum number of grid ticks to draw | [\#45113](https://github.com/qgis/QGIS/issues/45113) | [PR \#66403](https://github.com/qgis/QGIS/pull/66403) | Niet van toepassing |
| Fixes malformed HTML metadata for postgres layers | Gerapporteerd op mailinglijst | [PR \#66402](https://github.com/qgis/QGIS/pull/66402) | N/B - alleen QT 6 |
| Fix slow count of features for filtered SQL server layers | [\#64894](https://github.com/qgis/QGIS/issues/64894) | [PR \#66401](https://github.com/qgis/QGIS/pull/66401) | Niet van toepassing |
| Partially fix slow expression builder widget construction times | Niet gerapporteerd | [PR \#66385](https://github.com/qgis/QGIS/pull/66385) | Niet van toepassing |
| Use correct default font for legend text on symbol | Related to [\#63431](https://github.com/qgis/QGIS/issues/63431) | [PR \#66384](https://github.com/qgis/QGIS/pull/66384) | Niet van toepassing |
| Don't show missing font warnings for MS Shell Dlg font | [\#63431](https://github.com/qgis/QGIS/issues/63431) | [PR \#66383](https://github.com/qgis/QGIS/pull/66383) | Niet van toepassing |
| Add explicit bool operator for QgsLayerTreeNode | [\#65755](https://github.com/qgis/QGIS/issues/65755) | [PR \#66381](https://github.com/qgis/QGIS/pull/66381) | alleen QGIS 4 |
| WMS Ensure we store deduced CRS in provider/layer sources | Niet gerapporteerd | [PR \#66379](https://github.com/qgis/QGIS/pull/66379) | Niet van toepassing |
| Fix maximum word wrap for legend title/group/subgroup text | [\#66281](https://github.com/qgis/QGIS/issues/66281) | [PR \#66338](https://github.com/qgis/QGIS/pull/66338) |  |
| Fix model is zoomed right out when opening model designer | Niet gerapporteerd | [PR \#66335](https://github.com/qgis/QGIS/pull/66335) | alleen QGIS 4 |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
