---
HasBanner: false
draft: false
releaseDate: '2026-03-06'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 4.0
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 4.0{#changelog40 }
<img src="images/projects/388120cc4ef54e6b606481e3c2b08ba3738b5c17.png" class="img-responsive img-rounded center-block" />

Datum uitgave 06-03-2026

Het wachten is voorbij! QGIS 4.0 is hier!

[QGIS](https://qgis.org) (<https://qgis.org>) is het populairste (open bron) desktop Geografische InformatieSysteem (GIS) ter wereld. Het wordt gebruikt door mensen over de gehele wereld om ruimtelijke gegevens te bekijken, te bewerken, te analyseren en te delen. Het kan professioneel ogende cartografieproducten produceren en ondersteunt honderden indelingen voor ruimtelijke gegevens. QGIS is een lidproject van OSGEO, de Open Source Geospatial Foundation dat toegang tot ruimtelijke platforms democratiseert (<https://osgeo.org>).

Vanaf ons bescheiden begin meer dan 20 jaar geleden, wordt ons project nog steeds sterker - zowel in termen van het aanbieden van software als in termen van onze sterke, diverse en levendige gemeenschap die ondersteunt en profiteert van QGIS over de gehele wereld.

We zijn heel blij om de nieuwe belangrijke uitgave van QGIS 4.0 aan te kondigen Die de succesvolle voltooiing is van een lang geplande technische migratie, die de bron van QGIS overbracht naar het framework van Qt6.

Aan de oppervlakte zouden bestaande gebruikers kunnen verwachten te worden geconfronteerd met een GIS-ervaring die ze al hebben leren kennen en waarvan ze houden uit eerdere uitgaven van QGIS. Onder de motorkap introduceert het echter significante wijzigingen in onderhouds- en gebruiksmogelijkheden. Deze wijzigingen zorgen ervoor dat QGIS 4.0 aanvullende toegang kan ontgrendelen tot moderne bibliotheken, waarbij al lang nodige prestaties worden gebracht en verbeteringen aan beveiligingen aan de codebasis.

Voor een gladde overgang voor ons levendig ecosysteem, hebben we vervallen API's, waar mogelijk, behouden. Wat de inspanningen minimaliseert die vereist zijn voor ontwikkelaars van plug-ins om hun gereedschappen bij te werken. Sommige verouderde API's (zoals de Processing API uit QGIS 2.x) kunnen geen garantie bieden voor toekomstige ondersteuning en achterwaartse compatibiliteit gedurende de levensduur van de serie QGIS 4.x. Ontwikkelaars die bestaande plug-ins ondersteunen, kunnen er gemakkelijk voor zorgen dat hun plug-ins compatibel zijn met de nieuwe uitgave met de [compatibiliteitsgids voor Qt6](https://github.com/qgis/QGIS/wiki/Plugin-migration-to-be-compatible-with-Qt5-and-Qt6).

Terwijl de voorbereiding voor de migratie van QGIS 4.0 onderweg was, heeft de gemeenschap van ontwikkelaars meer dan 100 nieuwe mogelijkheden toegevoegd in de gehele toepassing. QGIS nog krachtiger makend, meer flexibel, veiliger en over het algemeen nog beter. Aansluitend aan de ontwikkelingen die waren geassocieerd met de codebasis, is de collega-gemeenschap van gebruikers van QGIS doorgegaan met het delen van bronnen, inclusief projecten, stijlen, scripts, en nog veel meer. Wat heeft geleid tot een fantastische periode van groei voor de, nieuw vormgegeven, [QGIS Hub](https://hub.qgis.org/) en geassocieerde sites voor de gemeenschap.

Als u meer wilt zien over onze uitgave, bekijk dan [hoe de gemeenschap de aankondiging deelt](https://youtu.be/SQJZm5Y0EKs)!

[![](https://img.youtube.com/vi/SQJZm5Y0EKs/0.jpg)](https://www.youtube.com/watch?v=SQJZm5Y0EKs)

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u de [video met hoogtepunten bekijken op YouTube](https://youtu.be/wTK1exokBA8). En voor een gedetailleerd overzicht van de nieuwe mogelijkheden en verbeteringen, bekijk het [log met wijzigingen](https://qgis.org/project/visual-changelogs/visualchangelog40/) voor deze uitgave.

[![](https://img.youtube.com/vi/wTK1exokBA8/0.jpg)](https://www.youtube.com/watch?v=wTK1exokBA8)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten!

Als u tijd of geld wilt doneren of op een andere manier wilt bijdragen aan het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Tijdbeheer
### Mogelijkheid: Nieuwe instelling voor accumuleren van pixels toegevoegd om de modus Tijdwaarden weer te geven
Een nieuwe optie voor het accumuleren van pixels is toegevoegd die beschikbaar is als de modus Tijdbeheer voor een rasterlaag is ingesteld om tijdwaarden weer te geven. Dit bootst de tegenhanger in vectorlagen na, waar objecten in de tijd kunnen accumuleren als de status van Tijdbeheer van een object wordt weergegeven door een enkel veld datum/tijd.<br />Dit is speciaal nuttig in geanimeerde navigatie in Tijdbeheer bij het combineren van vector- en rasterlagen.

<img src="images/entries/bcb3022b31756fa9b9bb2a161bdc74633e53c515.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Kaartgereedschap
### Mogelijkheid: Kaartgereedschap toegevoegd voor bewerken van blanco segmenten
Een nieuw kaartgereedschap voor het bewerken van blanco segmenten is toegevoegd. Zoals beschreven in [QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345).<br /> Het stelt gebruikers in staat om per object blanco segmenten te definiëren, gebaseerd op een lijnsymbologie uit een sjabloon, en voorkomt dat Hashes of Markeringen binnen deze segmenten worden getekend.<br /> De blanco segmenten worden opgeslagen in een data-bepaalde eigenschap (gegevensveld of veld voor hulpopslag). Dit gereedschap stelt gebruikers in staat om:
- Te klikken in de nabijheid van de lijn om een segment te beginnen, opnieuw te klikken om bewerken te beëindigen
- Een segment te selecteren en op de toets Del te drukken om het te verwijderen
- Te slepen aan het begin/einde van een reeds bestaand segment en het te verplaatsen langs de lijn om het te verkleinen/te vergroten

<img src="images/entries/05d17bd62aaa441e7756a5bf5970d4ddc90760da" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt en Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Objecten in een array langs een lijn kopiëren
Een nieuw kaartgereedschap stelt gebruikers in staat om objecten in een array te kopiëren langs een lijn en is beschikbaar voor typen geometrie polygoon/lijn/punt.

<img src="images/entries/60adf287a322741a4f92f851fcfc369b068ed097.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
## Gebruikersinterface
### Mogelijkheid: Nieuw ontwerp voor pagina Welkom
QGIS 4.0 komt met een glanzend nieuwe pagina Welkom, met een uit te breiden ontwerp voor een verbeterde gebruikservaring in lijn met [QEP 347](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/351).

<img src="images/entries/26a97dc32083858218bfe1bfd34d00af243b6bef.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Meegeleverde thema's ontgrendelen door plug-ins
Het toevoegen van nieuwe thema's die worden meegeleverd met de bron van QGIS (zoals Night Mapping en Blend of Gray) komt met hoge onderhoudskosten en beperken de creativiteit die auteurs kunnen uitoefenen, omdat ze over het algemeen neutraal, algemeen en toegankelijk moeten zijn.<br />QGIS is nu uitgebreid om deze thema's te ondersteunen vanuit de plug-ins-API, zodat de gemeenschap ook thema's en aangepaste stijlen voor de toepassing kan toepassen zonder wijzigingen aan de brontoepassing van QGIS. Wat een geheel nieuwe dimensie voor de gebruikservaring van QGIS ontgrendelt.

Dit werd mogelijk gemaakt door [wat vrije tijd, geïnspireerd op :)](https://github.com/qgis/QGIS/pull/64495)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Gebruikergedefinieerde werkbalk en menu maken
QGIS staat gebruikers nu toe om gebruikergedefinieerde menu's en werkbalken te maken om krachtige opties voor aanpassingen te verschaffen.<br />Dit implementeert [QEP \#343](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-343-customized-toolbars-and-menus.md).

<img src="images/entries/553f1a2b5712a2f02d6a5a038197c1baefe6c012" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt en Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Attributentabel dubbelklik zoom
Gebruikers kunnen nu dubbelklikken op een item in de attributentabel om direct een object te selecteren en naar het geselecteerde object te zoomen.

<img src="images/entries/50fa542fa614721b36cac2efce700c9800a33c59.gif" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nass](https://github.com/lanckmann)
## Symbologie
### Mogelijkheid: Kopiëren/plakken van alle stijlen uit een laag naar een andere toestaan
Wanneer een laag meerdere stijlen heeft, bevat het contextmenu van de boom met lagen nu een nieuwe actie "Alle stijlen kopiëren". Activeren hiervan zal de definitie van ALLE stijlen van de lagen naar het klembord kopiëren.<br />Gebruikers kunnen het contextmenu op een andere laag openen en de nieuwe mogelijkheid "Alle stijlen gebruiken" om kopieën van ALLE stijlen van de originele laag naar het doel te plakken. Dit verwijdert de noodzaak om handmatig door de bestaande stijlen in de originele laag te gaan, en de stijlen een voor een te plakken.

<img src="images/entries/76ce4e014c2eb3e29ac33b4b5708834c66961430.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Introduceren van aanvullende gegroepeerde stijlcategorieën in gebruikersinterface Kopiëren/Plakken
Nieuwe sneltoetsen voor gegroepeerde categorieën zijn toegevoegd aan het submenu voor de boom met lagen voor het kopiëren/plakken van stijlen. Dat maakt het voor gebruikers mogelijk om snel een set gegroepeerde categorieën tussen lagen te kopiëren/plakken.

<img src="images/entries/86c35bb07f30070746cfeed9bd533c786bba0df4.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Annotaties
### Mogelijkheid: Nagelnieuw gereedschap Annotaties selecteren
Als deel van de implementatie van [QEP \#344](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/344) dat zich richt op het introduceren van functionaliteiten voor het kopiëren, verplaatsen en draaien van annotatielagen, verschaft het nieuwe gereedschap voor selecteren interactieve bewerkingen voor items Annotatie, inclusief:
- selecteren van item(s) voor annotatie, met de aanpassingstoets Shift om te schakelen voor het selecteren van aanvullende item(s)
- muis- en toetsenbordverplaatsing van geselecteerde item(s)
- verwijderen van geselecteerde item(s)
- afmetingen wijzigen van geselecteerde item(s) met de handvatten voor de muis
- draaien van geselecteerde item(s) met de handvatten voor de muis

<img src="images/entries/db55791d9e7c92428f8165d661bc264fd09ae61c.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Tekstannotaties weergeven in 3D-kaartweergaven
Wanneer een annotatielaag is ingesteld om te renderen als 3D-plakborden, rendert het ook tekstannotaties als plakborden.<br />Voor tekstannotaties lijn/rechthoek wordt het plakbord geplaatst in het midden van de lijn/rechthoek. Gebruikers kunnen de gebruikte tekstindeling voor het 3D-plakbord. <br />De originele indeling 2D-annotatietekst wordt genegeerd, wat gebruikers in staat stelt een leesbare/meer toepasselijke tekstindeling te ontwerpen voor alleen de 3D-tekst.

<img src="images/entries/ce930ee001993bd8bd7ecf0477aac6e5e9436da1.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Ondersteuning voor renderen van markeringen voor Annotatielaag als 3D-aanplakborden
Een nieuwe optie voor het weergeven van annotatielagen in 3D-kaarten is toegevoegd. Vanuit de eigenschappen voor de annotatielaag, tab 3D, kunnen gebruikers de laag instellen om te renderen als 3D-aanplakborden. Indien geactiveerd, worden alle MARKERINGEN van de laag weergegeven als zwevende symbolen aanplakbord bovenop de 3D-kaart (lijnen en polygonen van de laag worden genegeerd).<br />⁣Gebruikers hebben beheer over het klemmen van het terrein en verschuiving voor de aanplakborden, en of al dan niet lijnen voor "tekstballonnen" zouden moeten worden weergegeven (verticale lijnen die verbinden met het aanplakbord op de corresponderende locatie op het terreinoppervlak).

<img src="images/entries/a74b316080040084674f70ed22492ad06da3c5be.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Labelen
### Mogelijkheid: Optie toegevoegd voor negeren witruimte bij detecteren labelbotsingen
Deze nieuwe optie (die ALLEEN beschikbaar is voor modi voor het plaatsen van gebogen labels) beheert hoe QGIS witruimte behandelt (d.i. spaties of tabs) in labeltekst bij het bepalen of twee labels botsen (of wanneer een label botst met een obstakelobject). Het bestaande (en standaard) gedrag is dat spaties hetzelfde worden behandeld als tekens tekst en een label mag geen spaties overlappen op een ander label.<br /> Als de nieuwe optie "Witruimte label negeren bij detecteren botsingen" is geselecteerd, dan zal witruimte in de tekst worden genegeerd bij het controleren van overlappende labels (of labels die botsen met obstakels).<br /> Dit is nuttig bij het labelen van objecten op lange lijnen, als de woordruimte groot is en het gewenst is om tekst of andere objecten toe te staan de labelruimten op te vullen. (Bijv. bij labelen van rivieren of wegen). De instelling mag data-bepaald zijn, functionaliteit inschakelen die wordt aangedreven door geavanceerde expressies, zoals het toestaan alleen te worden ingeschakeld voor objecten van voldoende lengte, etc.

<img src="images/entries/25ba4e122bd28db3d8cbf57717e1b4576dc790a5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Labelen meerdelige geometrie opnieuw bewerkt
Het bestaande keuzevak voor “Labelen meerdelige geometrie” is opnieuw bewerkt om een combinatievak te gebruiken om de keuzes voor opties voor afhandelen van meerdere delen weer te geven.<br />De beschikbare opties zijn:
- **Alleen grootste deel labelen**: Dit correspondeert met het huidige standaardgedrag, d.i. als de gebruiker het keuzevak "Elk deel labelen" niet heeft geselecteerd.
- **Elk deel met dezelfde tekst labelen**: Dit correspondeert met het huidige gedrag dat wordt geactiveerd als de gebruiker het keuzevak "Elk deel labelen" heeft geselecteerd.
- **Tekstregels van labels splitsen over delen**: Dit is nagelnieuw gedrag dat de labeltekst splitst over de delen van een object met een meerdelige geometrie. De labeltekst zal worden gesplitst met tekens voor een nieuwe regel, en elke regel zal afzonderlijk over de corresponderende delen van het object voor invoer van de geometrie worden geplaatst. Onthoud dat het splitsen zal gebeuren NADAT de bestaande instelling voor "Afbrekingsteken" wordt toegepast. Met elk aangepast teken voor een nieuwe regel dat de gebruiker voor die instelling heeft geconfigureerd, zal dus rekening worden gehouden bij het plaatsen van labels voor meerdelige geometrieën. Als de meerdelige geometrie niet voldoende delen bevat voor de labeltekst, dan zullen de overschrijdende regels worden genegeerd.

<img src="images/entries/69d0f632877a1a7380e957dd0b4d7321906d7005.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Modi voor plaatsing van gebogen labels
Nieuw toegevoegde "modi" voor plaatsing zijn nu beschikbaar om te gebruiken met gebogen labels, wat veel meer fijn af te stemmen beheer mogelijk maakt over hoe uw tekst is gepositioneerd bij het gebruiken van gebogen labels. In lijn met [QEP 404](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-404-curved-placement-modes.md). <br />Deze extra modi worden weergegeven als opties die zichtbaar zijn en kunnen worden ingeschakeld als een type geometrie lijnenlaag is ingesteld voor plaatsing van gebogen labels. Een data-bepaalde 'override' is beschikbaar voor de nieuwe modi voor plaatsing van gebogen labels, wat gemixt gebruik mogelijk maakt van de verschillende modi voor objecten op een enkele laag.<br />Nieuwe modi omvatten:
- **Standaard**: Bestaand gedrag, geen wijziging. Gliefen worden geplaatst op normale teken- en woordruimte langs de geometrie van de gebogen lijn.
- **Tekens op punten**: Als deze modus is geselecteerd, wordt elk individueel teken uit de labeltekst zo geplaatst dat zijn linkerpositie op de basislijn is geplaatst op een corresponderend punt van de geometrie van de gebogen lijn. Dat is: het eerste teken zal worden geplaatst aan het begin van de lijn, het tweede op het tweede punt, het derde op het derde punt, etc. Als de geometrie van de gebogen lijn niet voldoende punten bevat voor de in het tekstlabel aanwezige tekens, dan worden de overschrijdende tekens genegeerd en zullen niet worden gerenderd. Als de instelling van het label “afstand” niet nul is, dan zal het teken verticaal worden verschoven vanaf de positie van het punt met deze afstand. Tekens worden gedraaid om de hoek van het punt te volgen.
- **Tekenruimte uitrekken, passen op regel**: Indien geselecteerd, vergroot (of verkleint) deze modus de tekenruimte die wordt gebruikt voor elk label om de gehele tekst passend te maken over de feitelijke lengte van de geometrie gebogen lijn.
- **Afstand tussen woorden uitrekken**: Indien geselecteerd, vergroot (of verkleint) deze modus de woordruimte die wordt gebruikt voor elk label om de gehele tekst passend te maken over de feitelijke lengte van de geometrie gebogen lijn.

<img src="images/entries/1c0ce144f536089eabaaf9066453d60a5ae2ca01.gif" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Renderen
### Mogelijkheid: Introduceren van voorkeuzen selectieve maskers
Gebruikers kunnen nu een keuzemenu gebruiken onder Bronnen masker bij het configureren van het masker voor een laag en selecteren uit een aantal voorkeuzen om maskers efficiënt toe te passen zonder complex beheer. Dit is speciaal handig voor grote projecten als veel verschillende lagen naar dezelfde set bronnen voor maskers moeten verwijzen. Zoals wanneer veel lagen zijn gemaskeerd met dezelfde set afzonderlijk gelabelde lagen.<br />De standaardwaarde is "aangepast", wat de bestaande ad hoc per-laag-configuratie herhaalt. Gebruikers zijn echter in staat waar nodig sets voor selectieve maskers te maken, te hernoemen of te verwijderen, en alle wijzigingen aan de geselecteerde bronnen voor een voorkeuze zullen automatisch de wijzigingen toepassen op ALLE aan de voorkeuze gekoppelde lagen.

<img src="images/entries/a73331ff4395c78b8152d289d1759a55aeafd04d.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## 3D-objecten
### Mogelijkheid: Optie toegevoegd om exporteren van terrein bij exporteren van 3D-scène uit te schakelen
Een nieuwe optie om het exporteren van het terrein in- of uit te schakelen wordt verschaft in het dialoogvenster voor exporteren van 3D-scènes. Opties voor het terrein zijn altijd geactiveerd, zelfs als renderen van het terrein is uitgeschakeld. De optie `Resolutie terrein` is alleen relevant voor DTM of online terrein - het moet voor andere typen terrein worden uitgeschakeld.

<img src="images/entries/45d755c8e01bb45c2b728dd1dc59dc6afabe8856.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Accentueren geïdentificeerde objecten in 3D-weergaven
QGIS ondersteunt nu het accentueren van vectorobjecten in 3D-weergaven. De geïdentificeerde objecten polygoon worden geaccentueerd in 3D-weergaven met een semi-transparante overleg en een dikke silhouetlijn, soortgelijk aan het effect voor accentueren in het 2D-kaartvenster, met een overeenkomende kleur en transparantie. Het effect voor accentueren wordt altijd gerenderd bovenop andere entiteiten. Wanneer geaccentueerde objecten in de huidige zichtweergave overlappen, wordt een samengesteld silhouet gerenderd op de waargenomen perimeter.

<img src="images/entries/49c5a902146f5890162179a952c10a44757a8437.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros)
### Mogelijkheid: Kruisdelen: vaste tolerantie gebruiken (breedte) en lichtjes raken links/rechts
Bij het definiëren van een kruisdeel kiest de gebruiker normaal gesproken twee eindpunten, en daarna wordt met de derde muisklik de breedte (tolerantie) voor het kruisdeel gekozen. De nieuwe versie maakt het mogelijk de tolerantie te vergrendelen, zodat de gebruiker slechts twee eindpunten hoeft te kiezen, zonder elke keer de breedte (tolerantie) te moeten kiezen. Meer nog, het is mogelijk om de tolerantie van het actieve kruisdeel aan te passen door de waarde voor de tolerantie te bewerken in de gebruikersinterface.<br />3D-kaartweergaven staan nu ook het lichtjes raken van het kruisdeel links of rechts toe. Op dezelfde manier als dat de widget Hoogteprofiel dat doet (ofwel met menuknoppen of met sneltoetsen voor het toetsenbord).

<img src="images/entries/d6998552d0292c6f65ef77d8ad881abdd252e88f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Dynamische delen voor vector
In eerdere versies van QGIS werden vectorlagen in 2D-weergaven opgedeeld in delen met vaste zoomniveaus. Dit gedrag is aangepast om dynamisch de diepte van de quadtree aan te passen, en elk zoomniveau zal alleen een maximaal aantal objecten laden, beperkt door de door de gebruiker gespecificeerde waarde "Maximale aantal objecten per deel". Dat maakt het mogelijk grotere lagen te renderen zonder de noodzaak om al hun objecten te moeten laden bij uitzoomen.

<img src="images/entries/7d0ed17befd3fb5d351c9d3ea603ae1ea4741fdd.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros)
### Mogelijkheid: Vloeren renderen voor uitgerekte polygonen
3D-symbolen voor polygonen kunnen nu optioneel vloeren opnemen bij het renderen van objecten. Deze werden eerder niet opgenomen en het renderen van volumetrische gegevens als vakken zou het onderste deel weglaten.

<img src="images/entries/74053b5b39cc9e15d7175643786aa48edb459486.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Ondersteuning toegevoegd voor een 2D-kaartoverleg
Een nieuwe mogelijkheid voor 3D-kaartweergaven stelt gebruikers in staat een overleg van de 2D-kaart weer te geven, gecentreerd rondom de positie van de 3D-camera, en optioneel de afgeknotte kegel voor de camera.

<img src="images/entries/0c322a45de5780379e95e0f0d7467482e1d6661a.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Lagen Esri Scene
Een nieuwe gegevensprovider voor getegelde scènelagen is toegevoegd voor ESRI I3S (alias "scènelagen" / "scène servers"). Renderen van gegevens is beschikbaar in zowel 2D- als 3D-kaartweergaven.<br />Hoe I3S-gegevens te laden:
- vanuit ArcGIS REST-servers - via Databronnen beheren of dock Browser (eerder zouden de scènelagen niet te zien zijn, nu wel)
- open een lokaal bestand SLPK - met slepen-en-neerzetten vanuit de bestandsverkenner of het dock Browser, of Databronnen beheren (tab Scène)<br />Opmerkingen:
- ondersteunt I3S \>= 1.7
- ondersteunt laagtypen 3DObject en IntegratedMesh
- ondersteunt gegevenssets in zowel modus "globaal" (d.i. EPSG:4326) en modus "lokaal" (d.i. elk geprojecteerd CRS)

<img src="images/entries/b7a22f419d8b99a1cdf1fcbeacf768021b3afe33.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://github.com/wonder-sk)
### Mogelijkheid: Orthografische camera werkbaar gemaakt
3D-weergaven hadden al een optie om een orthografische camera te gebruiken in plaats van een camera met perspectief, maar die optie was al heel veel uitgaven defect. De ondersteuning voor de orthografische camera is nu te gebruiken, en die kan heel praktisch zijn bij het gebruiken van kruisdelen.

<img src="images/entries/9caebdb681257fd8ef96886833d26f278da61ae8.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [David Konarik (Lutra Consulting)](https://github.com/dvdkon)
## Puntenwolken
### Mogelijkheid: Verbeteringen aan algoritme Virtuele PuntenWolk (VPC) bouwen
Het algoritme Virtuele PuntenWolk (VPC) bouwen zal gebruikers waarschuwen wanneer bestanden LAS of LAZ als invoer zijn opgenomen voor een VPC (een dergelijke VPC kan niet volledig worden weergegeven in QGIS, zonder de invoerbestanden te converteren naar de indeling COPC). Het algoritme verschaft ook de optie **Individuele bestanden naar indeling COPC converteren** - dat zal automatisch alle invoerbestanden (bijv. LAS/LAZ) naar COPC's converteren, wat de VPC geschikt maakt om te worden gerenderd in 2D/3D in QGIS.

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting)](https://github.com/JanCaha)
### Mogelijkheid: Nieuw algoritme voor Processing: Puntenwolken vergelijken (M3C2)
Een nieuw algoritme voor het vergelijken van twee lagen van puntenwolken is beschikbaar.<br />Algoritme M3C2 (Multiscale Model to Model Cloud Comparison) berekent afstanden tussen twee puntenwolken langs lokaal geschatte oppervlaknormalen, in plaats van een vaste projectierichting te gebruiken. Het werkt met meerdere schalen om robuust zowel de oriëntatie van het oppervlak als de getekende afstand te kunnen inschatten. Wat het heel geschikt maakt voor het detecteren van wijzigingen in complexe 3D-oppervlakken, zoals rotshellingen of rivierbanken.<br />Opmerking: het algoritme gebruikt `filters.m3c2` uit PDAL - en het zal alleen werken als de installatie van QGIS een PDAL-versie \>2.10 meegeleverd heeft gekregen.

<img src="images/entries/d9a6459aac43a28b79857ac0c6a48870abbe1681.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting) + implementatie van PDAL door Hobu Inc.](https://github.com/JanCaha)
### Mogelijkheid: Kiezen op welk zoomniveau VPC feitelijke punten zal laten zien
Een nieuw combinatievak wordt verschaft in de eigenschappen 2D-/3D-stijl voor VPC's. Dat beheert het zoomniveau waarop QGIS zal schakelen van het renderen van tegelbereik of overzicht puntenwolk naar renderen van punten vanuit de gegevensbestanden die zijn gekoppeld aan de VPC. Dat verschaft beter en fijner beheer over de nadelen voor uitvoering en detail voor renderen van puntenwolken en geeft opties voor:
- Later
- Normaal
- Vroeger
- Veel vroeger

<img src="images/entries/a0c145b876b64361435d38986cdf8cef786d7857.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Ondersteuning voor gegevensset van Virtuele puntenwolk op afstand
QGIS is nu in staat virtuele puntenwolken te laden die worden gehost op een server op afstand. Dat verlaagt de wrijving bij het distribueren van grote gegevenssets van puntenwolken - gebruikers hoeven niet vooraf het .vpc-bestand te downloaden, omdat QGIS dat automatisch voor zijn rekening zal nemen.

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Bewerken van virtuele puntenwolken (VPC)
Het is nu mogelijk om gegevens van puntenwolken te bewerken binnen virtuele puntenwolken (VPC). Het is vereist dat de VPC en zijn gekoppelde gegevensbestanden beschikbaar zijn als lokale bestanden COPC (niet gehost op een server op afstand).

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Nieuw algoritme voor Processing: Hoogte boven grond
Het algoritme "Hoogte boven grond" berekent de verticale afstand van elk punt vanaf een geschat grondoppervlak, wat essentieel is voor het normaliseren van hoogtegegevens in variërend terrein. Dit is nuttig voor taken als het uitnemen van bouwhoogtes of schatten van hoogtes van vegetatie.<br />Het algoritme voert dezelfde puntenwolk uit, met een nieuw toegevoegd attribuut ("HeightAboveGround") met de berekende hoogte. De gebruiker kan er optioneel voor kiezen om de waarden Z van punten te vervangen door de berekende hoogte boven de grond - wat soms nuttig is voor 3D-visualisatie of verder verwerken.<br />Er zijn twee varianten van het algoritme - de basis die het grondoppervlak schat vanuit een aantal dichtbijgelegen grondpunten, de andere variant maakt een triangulatie van grondpunten en berekent daaruit de hoogte.<br />⁣ De puntenwolk voor de invoer moet enkele van de punten hebben geclassificeerd als grond (classification=2).

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting)](https://github.com/JanCaha)
### Mogelijkheid: Nieuw algoritme voor Processing: Grondpunten classificeren
Dit algoritme classificeert grondpunten met het algoritme Simple Morphological Filter (SMRF).<br />SMRF is een algoritme voor filteren van grond dat progressieve morfologische bewerkingen gebruikt uit niet-grondpunten (zoals vegetatie en gebouwen) in puntenwolken van Lidar. Het past iteratief bewerkingen toe voor het openen van verhogende venstergroottes, gecombineerd met een drempel voor de hoogte, wat het berekeningswijze gezien efficiënt en effectief maakt voor het maken van blote-aarde digitale terreinmodellen.

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting)](https://github.com/JanCaha)
### Mogelijkheid: Nieuw algoritme voor Processing: Ruis filteren
Er zijn twee nieuwe algoritmes voor het filteren van ruis uit puntenwolken (met de statistische methode of met straal).<br />Algoritmes voor het filteren van ruis identificeren en verwijderen uitschietende punten in een puntenwolk die voortkomen uit sensorfouten, reflecties van multipad of atmosferische interferentie. Ze analyseren de lokale nabijheid van elk punt en vlaggen punten die significant afwijken van hun omgevingen.

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting)](https://github.com/JanCaha)
### Mogelijkheid: Nieuw algoritme voor Processing: Puntenwolk transformeren
Het algoritme voor transformeren past vertalen, draaien en schalen toe om een puntenwolk uit te lijnen, zonder zijn vorm te wijzigen.<br />Dit wordt gewoonlijk gebruikt voor het corrigeren van systematische verschuivingen tussen waarnemingen, met behulp van bekende controlepunten of correspondenties.

Dit werd mogelijk gemaakt door [QGIS 3D for Open Source Digital Twins (crowdfunding campaign)](https://www.lutraconsulting.co.uk/crowdfunding/qgis-3d-for-open-source-digital-twins)

Deze mogelijkheid werd ontwikkeld door [Jan Caha (Lutra Consulting)](https://github.com/JanCaha)
## Afdruklay-outs
### Mogelijkheid: Besturingselement voor horizontale uitlijning voor rasterannotaties in kaarten van afdruklay-outs
In plaats van altijd rasterannotaties op kaarten van afdruklay-out links uit te lijnen, geeft een nieuw besturingselement de gebruikers de mogelijkheid om de uitlijning te kiezen. Dit is speciaal nuttig voor annotaties met meerdere regels, die er misschien niet goed uitzien als ze links worden uitgelijnd aan de linkerkant van de kaart.

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Opnieuw bewerkte afhandeling van initieel ingestelde laag en synchronisatie voor legenda's van afdruklay-out
QGIS heeft modi voor het synchroniseren van lagen geïntroduceerd voor de legenda's in afdruklay-outs, in lijn met [QEP 253](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/253).<br />⁣Dit verwijdert het bestaande keuzevak "Live bijwerken" voor legenda's van afdruklay-outs, en in plaats daarvan introduceert het een gebruiksvriendelijk combinatievak dat de modi voor het vullen van de legenda weergeeft, inclusief:
- **Synchroniseren met alle projectlagen**: Deze optie komt overeen met het huidige gedrag van het keuzevak "Automatisch synchroniseren". Indien geselecteerd, zullen alle nieuwe lagen die worden toegevoegd aan het project onmiddellijk verschijnen in de legenda, en elke aan deze lagen gemaakte wijziging zal onmiddellijk worden toegepast op de legenda.
- **Synchroniseren met zichtbare lagen**: Deze optie zal rekening houden met lagen die momenteel zichtbaar zijn in de kaart die is gekoppeld aan het item voor de legenda (of hoofdboom van de lagen, als geen kaart is gekoppeld aan de legenda). Wanneer deze modus actief is, zullen alle wijzigingen aan de set met lagen die zichtbaar is in de kaart ervoor zorgen dat de lagen van de legenda overeen zullen komen met deze set zichtbare lagen. Onthoud dat deze modus verschilt van de bestaande optie "Alleen items in gekoppelde laag weergeven", omdat de modus "Synchroniseren met zichtbare lagen" helemaal geen rekening houdt met de bereiken van de gekoppelde kaart - als een laag is geselecteerd en zichtbaar is voor de kaart, dan zal die worden weergegeven in de legenda. Ongeacht of alle objecten van de laag al dan niet buiten het zichtbare laagbereik vallen. Net als met de optie "Synchroniseren met alle projectlagen" worden eventuele wijzigingen aan de namen of andere aan de legenda gerelateerde instellingen in de hoofdboom van de lagen automatisch doorgevoerd in de legenda van de afdruklay-out.
- **Handmatig**: Alle inhoud voor de legenda kan handmatig door de gebruiker worden beheerd, en er zal geen automatisch synchroniseren worden toegepast op welke laag dan ook. Dit is hetzelfde gedrag als momenteel gebeurt in QGIS als de optie "Live bijwerken" niet is geselecteerd.

De vroegere bewerking "Alles bijwerken" voor legenda's is gewijzigd naar een nieuwe functie "Herstellen", die de configuratie van de legenda terug zal zetten naar de geselecteerde modus.<br />Deze wijziging bevat een nieuwe globale instelling die is toegevoegd aan de pagina Opties - Lay-out. Dat geeft gebruikers de kans om de standaardmodus voor nieuw gemaakte legenda's te beheren. Standaard zal
QGIS de modus "Synchroniseren met zichtbare lagen" gebruiken om een betere ervaring out-of-the-box te geven voor gebruikers met grote projecten; gebruikers kunnen echter het eerdere standaardgedrag herstellen door deze instelling overeenkomstig te wijzigen.

<img src="images/entries/3b47cf11887bdd0717b6cef55fdcb5f7b7ac0c13.gif" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Deense QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Data-bepaald beheer toegevoegd voor zichtbaarheid van annotaties in het raster van de kaart in afdruklay-out, en aanvullende expressievariabelen voor rasters
Dit maakt beheer PER-ANNOTATIE mogelijk voor de zichtbaarheid van de tekst in het kaartraster. D.i. het maakt het mogelijk individuele annotaties op het raster selectief te verbergen of weer te geven. De expressievariabelen `@grid_axis` en `@grid_number` zijn beschikbaar om in de expressie te gebruiken. Nieuwe expressievariabelen zijn ook geïntroduceerd, wat het gemakkelijk maakt om dingen te doen als het selectief verbergen van de eerste/laatste rasterannotaties:
- @grid_count: Totale aantal zichtbare rasterlijnen voor de huidige as van het raster.
- @grid_index: De index van de momenteel getekende rasterlijn (beginnend met 1 voor de eerste rasterlijn). De index is specifiek voor de huidige as van het raster.

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Toestaan dat geometrieën van atlas het frame van kaartitems opnieuw vormgeven
Een nieuwe functie voor het clippen van een frame is toegevoegd die, indien ingeschakeld, de frames van de kaartitems in de afdruklay-out opnieuw vormgeeft om overeen te komen met de (polygoon)geometrie van het huidige object van de atlas. Dat maakt flexibel clippen en maskers in items van Atlas mogelijk, speciaal waar de kleur van de achtergrond van het kaartvenster een integraal deel is van het renderen (bijv. vectortegelbasiskaarten).

<img src="images/entries/6cadd40d1ebfa64b6190c75334df0340c00a4d93.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Nagelnieuw plottype taartdiagram
Een nieuw taartdiagram is toegevoegd aan de typen voor plots in QGIS en zijn lay-outontwerper.

<img src="images/entries/ae30dae66281636965dbff50915b96b6ecbabacc.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Implementatie diagrammen afdruklay-out
Een nieuw item voor afdruklay-out is toegevoegd dat gebruikers in staat stelt het renderen van diagrammen te verhogen tot hun lay-outs voor afdrukken en Atlas. Configuraties voor diagrammen worden gedefinieerd met een uitgebreide set eigenschappen die worden verschaft in het paneel Eigenschappen en een aantal subpanelen.<br />De items voor diagrammen bouwen visualisaties vanuit gegevensseries van X- en Y-waarden, die worden afgeleid van een bronlaag die wordt gedefinieerd door de groep databron van de eigenschappen van het item. Elke serie wordt gedefinieerd met expressies om de waarden X en Y te evalueren, alsook de mogelijkheid om de bronlaag te filteren, op elke via een subpaneel geconfigureerde eigenschap. De volgorde voor iteratie door de bronlaag kan worden gewijzigd, waarmee rekening zal worden gehouden bij de diagrammen balk/lijn.

<img src="images/entries/65b7cdfcb7c7595f007a1911e51894e3cfab80dc.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Optie voor Atlas toegevoegd om het renderen van de bedekkingslaag te beperken tot alleen het huidige object
Een nieuwe optie voor Atlas werd toegevoegd om het renderen van objecten op de bedekkingslaag te beperken tot alleen het huidige object. Wat het mogelijk maakt dynamisch andere objecten uit te sluiten, zonder complexe expressies met het actieve object van Atlas te vereisen.

<img src="images/entries/7f1b58c91bf273f63b125dc5fe30327ae18068ed.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Bereik instellen voor laagitem in het menu van de werkbalk voor het kaartitem
Een nieuwe menuactie is toegevoegd aan de werkbalk voor kaarten van afdruklay-out. Wat gebruikers in staat stelt snel het bereik voor het item van een opgegeven kaart in te stellen om overeen te komen met het bereik van een ruimtelijke laag in het project.

<img src="images/entries/e4ba1fa83ed9a5601b434666eb8952eb270b970e" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Nagelnieuwe handvatten om te draaien voor items van afdruklay-out
Handvatten om te kunnen draaien zijn toegevoegd aan geselecteerde item(s) van afdruklay-out. Wat gebruikers de mogelijkheid geeft hun draaiing voor items aan te passen en hun lay-outs te perfectioneren.

<img src="images/entries/eaed49778b763c98749a2d37a9e4654602911616.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stad Frankfurt – Stadtplanungsamt

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
## Expressies
### Mogelijkheid: Geometriefunctie "equals" toegevoegd
Een nieuwe geometriefunctie `equals(geometry1, geometry2)` is toegevoegd, die de gelijkheid zal testen tussen twee geometrieën (op dezelfde manier als `overlay_equals`).

<img src="images/entries/8bd21615869e1defb47183b43aa131ecb2dbab17.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Mogelijkheid: Expressiefuncties toegevoegd voor werken met magnetische modellen
Nieuwe expressies voor het afhandelen van details van magnetische modellen zijn nu beschikbaar. Inclusief::
- @grid_index: Geeft de daling van een magnetisch veld op een punt aan, in graden Oost of Noord
- magnetic_inclination: Geeft de stijging van een magnetisch veld op een punt aan, in graden naar beneden vergeleken met horizontaal
- magnetic_declination_rate_of_change: Geeft de mate van wijzigen van de daling van een magnetisch veld op een punt aan, in graden per jaar
- magnetic_inclination_rate_of_change: Geeft de mate van wijzigen van de stijging van een magnetisch veld op een punt aan, in graden per jaar

Dit is heel nuttig voor metadata in afdruklay-outs en

<img src="images/entries/54affd11032e735eee18b4ef94d8f654a8d7acf8.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Functies extract_degrees, extract_minutes, extract_seconds toegevoegd
Deze functies zijn ontworpen om gemakkelijker de weergave te kunnen aanpassen van een op een graden gebaseerde rasterannotatie. Door het toestaan van het gemakkelijk uitnemen van de individuele componenten van de waarde van de decimale graad voor individuele opmaak (bijv. vet weergeven van de graden)
- extract_degrees: Neemt het integer getal voor graden uit een decimale waarde voor graden uit. De componenten minuten en seconden worden genegeerd. De uitgenomen waarden voor graden zullen worden afgebroken in de richting van nul (niet afgerond).
- extract_minutes: Neemt het integer getal voor minuten uit een decimale waarde voor graden uit. De componenten graden en seconden worden genegeerd. De uitgenomen waarden voor minuten zullen worden afgebroken in de richting van nul (niet afgerond), en zullen altijd een positieve waarde zijn.
- Neemt het integer getal voor minuten uit een decimale waarde voor graden uit. De componenten graden en minuten worden genegeerd. De uitgenomen waarden voor seconden zullen altijd een positieve waarde zijn.

<img src="images/entries/afca4fe52738eae1b242ae2720e0bbbb97f119fe.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Functie unaccent toegevoegd, gebaseerd op PostgreSQL unaccent
Een nieuwe methode unaccent wordt verschaft die accenten (diacriete tekens) verwijdert uit lexemen, bijv. `unaccent( "ï" )`.

<img src="images/entries/1d59428a063df21c5d83676b45e83771e56f5aca.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Tudor Barascu](https://github.com/tudorbarascu)
### Mogelijkheid: Expressie substr_count toegevoegd
De expressie new `substr_count` geeft gebruikers eenvoudigweg de gelegenheid om het aantal keer voorkomen van een subtekenreeks in een tekenreeks te tellen.

<img src="images/entries/09cbb9e54d4b4326ced2b4bdcf8c93736960af0a.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Tudor Barascu](https://github.com/tudorbarascu)
### Mogelijkheid: Enkele aan tijdzones gerelateerde expressiefuncties toegevoegd
Voegt enkele functies toe voor het werken met tijdzones in expressies:
- `timezone_from_id`: Maakt een object tijdzone uit een tekenreeks ID (uit de database voor tijdzones van IANA).
- `timezone_id`: Geeft de tekenreeks van de ID voor een object tijdzone terug. Gebruikt ID's uit de database voor tijdzones van IANA.
- `get_timezone`: Geeft het object tijdzone terug dat is geassocieerd met een waarde datetime.
- `convert_timezone`: Converteert een object datetime naar een andere tijdzone.
- `set_timezone`: Stelt het object voor de tijdzone in die is geassocieerd met een waarde datetime, zonder de componenten datum of tijd te wijzigen. Deze functie kan worden gebruikt om de tijdzone voor een datetime te wijzigen.

<img src="images/entries/67fe7d4aa19caa1698e52c9d27e2dd954b809bb9.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Digitaliseren
### Mogelijkheid: Kaartgereedschap Bézier
Nieuwe besturingselementen voor de gebruikersinterface voor het digitaliseren van delen met NURBS-curves worden verschaft door het toevoegen van de modus voor bogen "poly-bézier" / "freeform". Het gebruikt ankers en handvatten om de vorm van een boog te beheren op een manier die soortgelijk is aan veel gereedschappen voor grafisch ontwerpen.<br />Gebruikers kunnen klikken en slepen of een punt met handvatten toevoegen en handvatten op een punt herstellen met `alt+klik`.

<img src="images/entries/584c6a12ea7a79081fa1fce9f86d9c7d80ecf31c.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt en Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Waarden area en total length/perimeter voor zwevend dock CAD toegevoegd
Nieuwe waarden voor het zwevende venster worden verschaft voor de interface van Geavanceerd digitaliseren voor gereedschappen van CAD. Ze verschaffen de optie om de waarden voor area en total length/perimeter weer te geven met cartesiaanse of ellipsoïde berekeningen, gebaseerd op de selectie van de gebruiker (onthoud dat de gereedschappen voor CAD cartesiaanse coördinaten gebruiken voor digitaliseren, wat zou kunnen resulteren in verschillen tussen de weergegeven ellipsoïde waarden).

<img src="images/entries/03e5d6b7b5c5ad9449f6abcb73c3dc21706b5ec5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense QGIS gebruikersgroep](https://qgis.dk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Kaartgereedschap toegevoegd om afschuiningen en randen van polygonen af te handelen
Een nieuw kaartgereedschap voor digitaliseren stelt gebruikers in staat polygonen af te schuinen en randen te maken.

<img src="images/entries/58ace0c2995032999b366d0171a78857e687d3c4.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt en Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Gegevensbeheer
### Mogelijkheid: Verbeterde ondersteuning voor COG  voor exporteren van rasters
De dialoogvensters voor exporteren en opslaan van rasters ondersteunen nu expliciete opties om te specificeren dat de uitvoer zou moeten worden geëxporteerd met optimalisatie voor Cloud Optimized GeoTiff, met aanvullende COG-specifieke objecten piramiden, inclusief verbeteringen voor:
- voortgang rapporteren
- foutafhandeling
- bewerkingen voor maken van piramiden

Onthoud dat dit vereist GDAL \>= 3.13.0

<img src="images/entries/60cec0aa212eb189e7749c242ba1ca49423ca845.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Ruwe waarden attributen kopiëren
QGIS maakt nu de ruwe (originele) attribuutwaarden zichtbaar en te kopiëren in zowel de Attributentabellen als de interface voor Identificatieresultaten.<br />In eerdere versies werden gegevenswaarden alleen gekopieerd in hun "weergegeven" vorm, d.i. de waarden die zijn geëvalueerd door lokale instellingen, expressies of weergavewaarden (bijv. waarden voor vreemde sleutels).<br />De nieuwe optie "Ruwe waarde kopiëren", beschikbaar vanuit het contextmenu, zal de letterlijke waarden kopiëren vanuit de databron naar het klembord.

<img src="images/entries/cbc449f46c49440ac88d7f89a36e490d4d1deb20.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ct. Solothurn

Deze mogelijkheid werd ontwikkeld door [signedav](https://github.com/signedav)
### Mogelijkheid: Het opslaan van Opmerkingen voor projecten van QGIS in PostgreSQL toestaan
Projecten van QGIS die zijn opgeslagen in PostgreSQL mogen nu opmerkingen bevatten met aanvullende informatie, die met een Helptip zal worden weergegeven in de Browser.

<img src="images/entries/fa9f5d8b4ba7be7475799d104df2c4e96cc26f71.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Benoemde lagen toestaan als tijdelijke uitvoer
Deze functionaliteit stelt de gebruiker in staat een tijdelijke laag voor uitvoer, die het resultaat is van een algoritme van Processing, een naam te geven. Het feit dat de laag tijdelijk is, is te identificeren door het pictogram voor tijdelijk (geheugenchip), dat wordt weergegeven voor de door de gebruiker gedefinieerde laagnaam.

<img src="images/entries/3fec097dc50545f03ab62e3cff5688b719d23916" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door QGIS Deense gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Mogelijkheid om de laagnaam te wijzigen in het paneel Lagen bij het opslaan van een tijdelijke tekenlaag
Bij het opslaan van een tijdelijke tekenlaag als een permanente laag met een nieuwe naam (een andere bestandsnaam dan de naam in het paneel Lagen), wordt een berichtenbalk weergegeven. In deze berichtenbalk kan de gebruiker ervoor kiezen om automatisch de naam in het paneel Lagen te wijzigen naar de nieuwe laagnaam.<br />Deze berichtenbalk wordt alleen weergegeven als de laag wordt opgeslagen met een nieuwe naam, en momenteel werkt dit alleen voor bepaalde bestandstypen (het werkt voor GeoPackages, maar niet voor Shapefiles).

<img src="images/entries/f4d0c0c524eed26129c8c59c406018085e071220" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door QGIS Deense gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Stel een bestandsnaam voor bij het exporteren van een laag of groep als laagdefinitiebestand
Bij het opslaan van een laag of laaggroep als een laagdefinitiebestand (.qlr), werd het veld voor de bestandsnaam standaard leeggelaten. QGIS vult nu de naam van de laag of groep in als een suggestie voor de bestandsnaam om wrijving tussen geëxporteerde stijlen te verkleinen.

Deze mogelijkheid werd ontwikkeld door [pgipper](https://github.com/pgipper)
## Formulieren en widgets
### Mogelijkheid: De mogelijkheid toegevoegd om een voorbeeld van het attributenformulier te bekijken binnen het dialoogvenster Laageigenschappen van vector
QGIS verschaft nu de mogelijkheid om een voorbeeld van een attributenformulier te bekijken tijdens het configureren ervan in het dialoogvenster Laageigenschappen voor vector.

<img src="images/entries/c0bb362e1f57600a820c2d185f77993abbd48318.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Verfijnen van hergebruiken van de laatste waarde en introduceren van een schakelaar voor onthouden
Attributenformulieren van QGIS bevatten nu een verbeterde gebruikservaring voor de afhandeling van het opnieuw gebruiken van de "laatst vastgelegde" waarden in formulieren. Een pictogram van een pin op formulieren zal gebruikers visuele terugkoppeling geven over het feit of de waarde van een veld zal worden onthouden en opnieuw gebruikt kan worden, en verschaft een actieve schakelaar om te beheren of moet worden doorgegaan om het opnieuw te gebruiken. Aanvullende verbeteringen voor het configureren van het formulier maken het mogelijk beleid voor hergebruik in te stellen op het niveau van de sessie, het standaardgedrag voor beleid voor hergebruik (ingeschakeld/uitgeschakeld), en de mogelijkheid om beleid voor hergebruik uit te schakelen voor alle velden in een laag.

<img src="images/entries/b06e53bc63de8ea4643beb74c69781076b613d07.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door DB Fahrwegdienste GmbH

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Legenda van laag
### Mogelijkheid: Beheer toegevoegd of lagen moeten worden opgenomen in automatische legenda's van afdruklay-out
Een nieuwe instelling is toegevoegd aan de tab Legenda van de Laageigenschappen (voor vector, raster, lagen met mazen en lagen puntenwolken) voor "Automatisch opnemen in legenda-items van afdruklay-out". Deze instelling is standaard geselecteerd. Gebruikers moeten hem deselecteren om die laag uit te sluiten van legenda's voor afdruklay-out.<br />Dit is ook toegevoegd aan de pagina Legenda voor lagen met mazen en met puntenwolken, met de algemene instelling voor het beheren van ingebedde widgets Legenda.

<img src="images/entries/798344535f33fdaf2047bfbd3070def6d28bb6fb.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense QGIS gebruikersgroep](https://qgis.dk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Aangepaste bronnen Hoogteprofiel
QGIS bevat nu krachtiger interactief gedrag voor hoogteprofielen, inclusief het wijzigen van de zichtbaarheid van de laag en de volgorde van renderen in gerelateerde kaartvensters en het koppelen van de boom met lagen van het project aan de bronnen van de profielplot.<br />Deze functionaliteit wordt ingeschakeld door de introductie van de klasse `QgsLayerTreeCustomNode`, die de weergave inschakelt van objecten van de toepassing (andere dan lagen en groepen) in bomen van lagen in QGIS.

<img src="images/entries/8218225f95e403fe8e543f34b0427561371265b6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
## Processing
### Mogelijkheid: Eigen algoritmes voor oriëntatie polygonen
Nieuwe algoritmes voor **Rechterhand-regel forceren met de klok mee** (`native:forcecw`) en **Rechterhand-regel forceren tegen de klok in** (`native:forceccw`) zijn toegevoegd aan de algoritmes voor Processing.<br />Rechterhand-regel forceren met de klok mee kopieert de bestaande bewerking "Rechterhand-regel forceren" en forceert geometrieën polygoon om rekening te houden met de conventie waarin de buitenste ring is georiënteerd met de klok mee en de binnenste ringen in de richting tegen de klok in.<br />Rechterhand-regel forceren tegen de klok in voert het tegenovergestelde uit en forceert geometrieën polygoon de conventie te respecteren waarin de buitenste ring is georiënteerd in de richting tegen de klok in en de binnenste ringen in de richting met de klok mee.

<img src="images/entries/a0c4136c269a5cd474bdc29e15c26831baa8706f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Mogelijkheid: Configureren van modelcomponenten met een inregelig paneel in plaats van modale dialoogvensters
Een nieuw configuratiepaneel is toegevoegd, vastgezet aan de rechterkant van de modelontwerper van Processing dat het mogelijk maakt modelcomponenten te bewerken zonder de modale dialoogvensters en de gebruikservaring te kopiëren van het paneel Laag opmaken. Dit verbetert de gebruikservaring voor het bewerken van het model en voorkomt dat modalen voor het configureren van modellen de gebruikersinteractie blokkeren met andere elementen van QGIS terwijl modelcomponenten worden bewerkt. Gebruikers hebben nog steeds toegang tot de dialoogvensters door te dubbelklikken op een item.

<img src="images/entries/c6368e5609a680adf719ca6cd1a95739278db0d2.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [City of Canning](https://www.canning.wa.gov.au/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Algoritmes voor valideren netwerkanalyses toegevoegd
Twee nieuwe algoritmes die nuttig zijn voor het valideren van netwerken zijn toegevoegd:
- Netwerk valideren
- Eindpunten van netwerk uitnemen

**Netwerk valideren**<br />Dit algoritme analyseert een vectorlaag van een netwerk om gegevens te identificeren en topologiefouten die programma's voor analyses van het netwerk zouden kunnen beïnvloeden (zoals Kortste pad). Optionele controles omvatten:
1. Valideren van het veld 'Richting' om ervoor te zorgen dat alle veldwaarden voor de richting in de invoerlaag overeenkomen met de geconfigureerde waarden voorwaarts/achterwaarts/beide waarden. Fouten zullen worden gerapporteerd als het veld Richting niet-null is en niet overeenkomt met een van de geconfigureerde waarden.
2. Controleren van de scheiding knoop-naar-knoop. Deze controle identificeert knopen in de grafiek van het netwerk die dichter bij andere knopen liggen dan de gespecificeerde afstand voor tolerantie. Dit geeft vaak ontbrekend snappen of korte segmenten in de invoerlaag aan. In het geval dat een knoop deze voorwaarde schendt met meerdere andere knopen, zal alleen de dichtstbijzijnde schending worden gerapporteerd.
3. Controleren van scheiding knoop-naar-segment: Deze controle identificeert knopen die dichter bij een lijnsegment liggen (bijv. de rand van een grafiek) dan de gespecificeerde afstand voor tolerantie, zonder ermee verbonden te zijn. In het geval dat een knoop deze voorwaarde schendt met meerdere andere knopen, zal alleen de dichtstbijzijnde schending worden gerapporteerd.

Twee lagen worden door dit algoritme uitgevoerd:
1. Een uitvoer die objecten bevat uit de originele netwerklaag waarvoor de controles voor het valideren van de richting mislukten.
2. Een uitvoer die de locaties voor de problematische knopen weergeeft met een veld 'error' dat de fout uitlegt. Dit is een lijnenlaag waarbij de uitvoerobjecten de problematische knoop verbinden met de knoop of het segment waarvoor de controles van de tolerantie mislukten.

**Eindpunten van netwerk uitnemen**<br />Dit algoritme neemt de eindpunten (knopen) van een netwerklijnenlaag uit. Twee definities zijn beschikbaar voor het identificeren van eindpunten:
1. Knopen met alleen allemaal inkomende of allemaal uitgaande randen: Identificeert knopen 'Bron' of 'Afvoer', gebaseerd op de richting van de stroom. Dit zijn knopen waar de stroom kan beginnen (alleen uitgaand) of stoppen (alleen inkomend).
2. Knopen die zijn verbonden met een enkele rand: Identificeert topologische 'doodlopende einden' of 'hangers', ongeacht hun richting. Dit controleert of de knoop is verbonden met slechts een andere afzonderlijke knoop.

<img src="images/entries/a26779141bcb3e43adeea67400b4666419f3a17f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [City of Canning](https://www.canning.wa.gov.au/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Mogelijkheid toegevoegd voor het algoritme Behouden gladmaken raster
Dit is een port van het equivalente algoritme van het programma Whitebox. Het implementeert de logica die wordt beschreven in Lindsay, John et al (2019): LiDAR DEM Smoothing and the Preservation of Drainage Features.<br />Het is effectief in het verwijderen van ruwheid van de oppervlakte in DEM) zonder significant scherpe objecten te veranderen, zoals afbrekingen in hellingen, oevers van stromen, of kliffen van terrassen.<br />Dat maakt het superieur aan standaardfilters met een langzame doorloop (bijv. gemiddelde, mediaan, Gaussiaans) of hersamplen, wat vaak afzonderlijke topografische objecten vervaagt.<br />Het algoritme werkt in drie stappen:
1. Berekenen van oppervlak normale 3D-vectors voor elke rastercel.
2. Gladmaken van het normale vectorveld met een filter dat meer gewicht toepast op buren met normalen met een soortgelijk oppervlak (randen behouden).
3. Iteratief de hoogten in de DEM bijwerken om overeen te komen met het gladgemaakte veld voor de normale.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Eigen algoritme Gaussiaans vervagen voor raster
Maakt het mogelijk een filter Gaussiaans vervagen toe te passen op een rasterlaag

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Eigen algoritme toegevoegd voor Totale boog uit de bibliotheek voor terreinanalyse
Voegt het algoritme Totale boog toe aan Processing. Het filter Totale boog bestond al jaren in de bibliotheek voor Terreinanalyse, maar het werd nooit weergegeven in de gebruikersinterface. Het wordt nu weergegeven in het framework Processing, naast de bestaande filters voor terreinanalyse.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: GEEN GEGEVENS en opties voor maken van raster weergeven voor uitvoer in de gereedschappen voor terreinanalyse
GEEN GEGEVENS en opties voor maken raster weergeven in uitvoer voor de eigen gereedschappen voor terreinanalyses van rasters (Helling, Aspect, Schaduw voor heuvels, Ruwheidsindex).

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Algoritme voor Processing Dataset identification van GDAL toegevoegd
Een nieuw algoritme Dataset identification maakt het mogelijk automatisch metadata uit te nemen met GDAL.<br />Dit algoritme vereist GDAL \>= 3.13.0, omdat het de nieuwe mogelijkheden gebruikt van [gdal dataset identify](https://gdal.org/en/stable/programs/gdal_dataset_identify.html).

<img src="images/entries/76dfc1189b899bedaa208692766fc765ccb76175.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Een manier toegevoegd om de rasterindeling te specificeren in uitvoer van algoritmes van Processing
Deze mogelijkheid maakt het mogelijk de indeling voor de uitvoer te specificeren voor rasters met vlaggen voor configuratie van GDAL, primair voor het afdwingen van uitvoer voor Cloud Optimized GeoTiff.<br />In eerdere versies was de uitvoerindeling gebaseerd op de extensie van de bestandsindeling, die niet werkt voor COG omdat zowel stuurprogramma's voor GDAL GTiff als voor COG de extensie `.tif/.tiff` gebruiken. Gebruikers kunnen nu expliciet `-of COG` specificeren om exporteren voor COG af te dwingen.

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Stroom voor telling van objecten door een model weergeven in de Modelontwerper
De langverwachte mogelijkheid om het aantal objecten dat door het model stroomt weer te geven is toegevoegd. Het aantal objecten is verbonden met de koppeling die in en uit tussen de algoritmes gaat, en het is alleen van toepassing op vectorlagen. Het weergeven van het aantal objecten kan worden uitgeschakeld met de optie "Aantal objecten weergeven" in het menu Beeld.<br />Opmerking: Het model moet ten minste eenmaal zijn uitgevoerd, om in staat te zijn de telling voor objecten weer te geven.

<img src="images/entries/468164c721e2407abaf86e0629d35377741dc2a6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
### Mogelijkheid: Ondersteuning voor max-triangle-edge-length in PDAL-algoritme Export to raster (TIN)
Ondersteuning voor de parameter max-triangle-edge-length is toegevoegd aan het algoritme van PDAL Export to raster (TIN), zodat driehoeken, waarvan de lengte van de rand groter is dan de gespecificeerde drempel kunnen worden genegeerd.<br />Deze mogelijkheid heeft PDAL \>= 2.6.0 en wrench \>=1.2.2 nodig.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Bijgewerkte Modelontwerper
De QGIS Modelontwerper is significant bijgewerkt voor de manier waarop het de in- en uitvoerwaarden afhandelt tussen knopen om op veel betere manieren visuele terugkoppeling te geven.<br />Individuele parameters voor configuratie van knoop worden nu weergegeven en de verbindingen tussen waarden uit gereedschappen en variabelen zijn verbonden met de knopen door specifieke parameters waar ze overeenkomstig invoer en uitvoer zijn.<br />Waarden voor parameters zijn kleurgecodeerd op gegevenstype (inclusief algemene gegevenstypen als integer en string, maar ook complexe QGIS-specifieke typen, zoals vector- en rasterlagen. Wat verbeterd visueel indexeren mogelijk maakt en ook de traceerbaarheid van gegevensbewerkingen als die door het model stromen.

<img src="images/entries/92bf8916e1ddc8d0e44b31f130d2029ac93b438f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Géo2France](https://www.geo2france.fr/portal/public/overview)

Deze mogelijkheid werd ontwikkeld door [Jonathan Lurie](https://github.com/jonathanlurie)
### Mogelijkheid: Algoritme Laag opnieuw projecteren toestaan om coördinaten Z te transformeren
Een optionele parameter bool voor het algoritme *Laag opnieuw projecteren* is toegevoegd die het mogelijk maakt coördinaten Z te transformeren.

<img src="images/entries/b93161af43e09fc6189680f8f8b323b86555d499.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Algoritme toegevoegd om Cloud Optimized GeoTiffs te maken uit bronmap
Een nieuw algoritme voor het maken van Create Cloud Optimized GeoTIFF is toegevoegd. Dat maakt het mogelijk COG's te maken voor een set invoerrasterbestanden die worden verschaft in een aangewezen map. Het gebruikt GDAL om in bulk de invoerbestanden te converteren.

<img src="images/entries/7a822b6086fbf156b8f3528499f78a5d83eb7b29.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Algoritme voor Processing SFCGAL Geschatte mediale as toegevoegd
Een nieuw algoritme voor Processing voor de geschatte mediale as is toegevoegd, dat is gebaseerd op de nieuw geïntegreerde backend SFCGAL.<br />Het algoritme Geschatte mediale as genereert een vereenvoudigd skelet van een vorm door zijn mediale as te schatten. De uitvoer is een collectie lijnen die de centrale structuur van de vorm volgen. Het resultaat is een kleine, stabiele set van bogen die de belangrijkste topologie vastlegt, daarbij ruis negerend. Dit algoritme negeert de dimensie Z. Als de geometrie 3D is, zal de geschatte mediale as worden berekend vanuit zijn 2D-projectie.

<img src="images/entries/0804299923000a846f55b0b8fb0b50e19e3893d5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Instellingen Schaal en Resolutie voor uitnemen van WMS
QGIS schakelt nu de mogelijkheid in voor algoritmes Raster uitnemen om te werken met WMS'en die op een bepaalde schaal zijn opgevraagd, zodat schaalafhankelijk renderen (symbologie/labelen) in het uitvoerraster wordt behouden.<br />De verbeterde algoritmes zijn `Raster op bereik clippen` en `Raster op maskerlaag clippen`.<br />Een nieuw geavanceerd paneel met opties wordt verschaft voor lagen van WMS, als die als een bron worden gebruikt in deze algoritmes, dat opties verschaft voor:
- **Referentieschaal**: De schaal waarop de WMS-raster zou moeten worden verzocht/gerenderd.
- **Service resolutie**: De resolutie (in DPI) gebruikt door de server om de WMS-raster te renderen (standaard 96 dpi).<br />Deze wijzigingen werden ingeschakeld door het introduceren van de klassen `QgsProcessingRasterLayerDefinition` en `QgsWmsUtils`.

<img src="images/entries/532bbcaddf65f8d815ecdddd48ed71b067cdb855.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Germap](https://opengis.ch)
### Feature: Parameter voor toevoegen duplicaatobjecten aan uitvoerlaag toegevoegd in algoritme Gedupliceerde geometrieën
Deze mogelijkheid breidt het algoritme voor Processing "Gedupliceerde geometrieën" uit, zodat de geïdentificeerde duplicaatobjecten, die zijn verwijderd, kunnen worden uitgenomen en als afzonderlijk bestand kunnen worden opgeslagen voor verdere analyses.

<img src="images/entries/85ee1e8469a32c107d2bfc08ec468915399689a7.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Mogelijkheid: Algoritmes toegevoegd om delen op lengte/gebied te filteren
Deze nieuwe algoritmes, "Delen op lengte verwijderen" en "Delen op gebied verwijderen", filteren delen van geometrieën uit een vectorlaag door hun gebied of lengte te controleren tegen een parameter voor de minimale grootte.<br />Als de geometrie voor de invoer een geometrie met meerdere delen is, dan zullen de delen worden gefilterd op hun individuele oppervlakten. Als delen niet overeenkomen met de vereiste minimale grootte, dan zal het object worden overgeslagen en worden weggelaten uit de uitvoerlaag. Als de geometrie voor de invoer uit een deel bestaat, dan zal het object worden overgeslagen als de oppervlakte van de geometrie onder de vereiste grootte ligt en worden weggelaten uit de uitvoerlaag. Attributen worden niet aangepast.

<img src="images/entries/a3a539941a16aa0765fd05436e4e7228e3864553.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Optioneel doel-CRS toegevoegd voor algoritme Pakketlagen
Maakt het mogelijk dat lagen worden getransformeerd naar een specifieke uitvoer, indien ingesteld.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Algoritme Pakketlagen - alleen objecten exporteren die kruisen met een opgegeven bereik
Een optionele parameter voor `Bereik` is toegevoegd aan het algoritme Pakketlagen. Dat geeft gebruikers de mogelijkheid om alleen objecten te exporteren die kruisen met een opgegeven bereik uit alle geselecteerde lagen. Als geen van de objecten van een specifieke geselecteerde laag kruist met het opgegeven bereik, zal de laag toch worden gemaakt en zal leeg zijn in het GeoPackage van de uitvoer.

<img src="images/entries/33644c3a135003c6e8df79e9eda8878004b6ea28" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
### Mogelijkheid: Onbeperkte grootte kaartvenster model in de Modelontwerper
Eerdere versies van de modelontwerper van QGIS hadden een vaste grootte voor het kaartvenster van 4000 x 4000, en nieuwe modellen werden begonnen aan de linkerbovenkant van het kaartvenster, wat tot frustratie zou kunnen leiden als elementen buiten de grenzen terechtkwamen. De modelbouwer van QGIS zal nu dynamisch het scrollgebied beheren en een veel gladdere gebruikservaring inschakelen.

<img src="images/entries/6347778c8c50b9fa330e4985d19b980c2c8b676f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Hauts-de-France region

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
## Opties voor toepassing en projecten
### Mogelijkheid: OAuth2 automatisch vernieuwen
QGIS bevat nu een mechanisme voor automatisch vernieuwen van verbindingen voor OAuth2.<br />Een opruimactie van de cache om het automatisch vernieuwen te stoppen wordt periodiek geactiveerd, en wanneer een laag is verwijderd uit het project. Dit is vereist om onnodig, eindeloos vernieuwen van niet-gebruikte tokens te vermijden.

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Project vertrouwen voor verbetering ingebedde code
QGIS bevat nu een mechanisme voor "vertrouwen" op projectniveau dat de uitvoering van ingebedde code voor Python in projecten toestaat of verbiedt. Dit is geïmplementeerd in lijn met de [Trusted Projects and Folders QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-336-trusted-projects-and-folders.md).<br />Zoals vastgesteld in de QEP zijn de behandelde ingebedde typen voor code:
- macro's;
- expressiefuncties;
- acties; en
- init code voor attributenformulier 

Dit geeft gebruikers de mogelijkheid om het uitvoeren van code fijn af te stemmen op projectniveau, in plaats van globale instellingen die alleen worden beperkt door de configuratie van het gebruikersprofiel.<br />QGIS zal gebruikers een dialoogvenster voor vertrouwen voor het project verschaffen om de gebruiker algemene informatie te geven over welke mogelijkheden toe te staan. En ook om overeenkomstig een voorbeeld van de code te zien. Globale instellingen worden verschaft om het uitvoeren van de mogelijkheden op niveaus van project en pad toe te staan of te verbieden.

<img src="images/entries/8325ef4b8268626c5af3c9699370dbeb6faedcd4.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Hoogteprofielen beheren
QGIS koppelt nu de toepassing voor het afhandelen van hoogteprofielen aan een nieuw beheer voor hoogteprofielen op projectniveau. Nu kunnen hoogteprofielen, die zijn opgeslagen in het project, opnieuw worden geopend na het openen van een project, en wijzigingen aan het profiel zullen in het project worden opgeslagen.<br />Er is ook een volledig functioneel dialoogvenster Hoogteprofiel beheren, waarin hoogteprofielen van het project kunnen worden uitgeschakeld/hernoemd/verwijderd.

Dit werd mogelijk gemaakt door [Erftverband](https://www.erftverband.eu/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Ondersteuning voor lokaliseren metadata van project/laag
Ondersteuning voor vertalen is toegevoegd aan het vertaalsysteem voor projecten van QGIS voor enkele sleutelwaarden van metadata voor project en laag. Deze verbetering zorgt ervoor dat projectvertaling de relevante waarden voor die metadata kan gebruiken voor items van lay-out, zoals labels, decoraties voor het kaartvenster, etc.<br />*Dit is mogelijk gemaakt door de doorlopende inspanning voor het toevoegen van ondersteuning voor gelokaliseerde/vertaalde projecten in QField*

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Projectinstelling toegevoegd om de modus HTML GetFeatureInfo maptip-only in te schakelen
Een nieuwe projectinstelling voor QGIS Server wordt verschaft om de modus HTML GetFeatureInfo maptip-only mode in te schakelen.<br />[Dat maakt het voor QGIS Server mogelijk de WMS vendor-parameter te gebruiken](https://docs.qgis.org/3.40/en/docs/server_manual/services/wms.html#with-maptip) `WITH_MAPTIP=HTML_FI_ONLY_MAPTIP` en alleen de kaarttip voor het antwoord van HTML GetFeatureInfo te gebruiken.

<img src="images/entries/5cefab81d09c5bf0e1b757238d74940a2c9d9c55" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
## Profiel plotten
### Mogelijkheid: Optie toegevoegd om lagen met hoogteprofielen te synchroniseren met projectlagen
Deze nieuwe optie is beschikbaar in het menu Instellingen van een hoogteprofiel als "Lagen synchroniseren met project". Die is standaard niet geselecteerd, maar indien geselecteerd, zullen de lagen van het hoogteprofiel altijd exact overeenkomen met de structuur van de lagen in het hoofdkaartvenster van het project, inclusief groeps- en laagvolgordes.<br />Groepen kunnen niet in het hoogteprofiel worden gemaakt. Alle wijzigingen aan de hoofdboom met lagen van het project zullen onmiddellijk zichtbaar zijn in de instelling van de laag van het hoogteprofiel.

Dit werd mogelijk gemaakt door [Lutra](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Puntenwolk renderen als een doorlopende hoogtelijn
QGIS profielplots bevatten nu voor het hoogteprofiel van een laag puntenwolk de mogelijkheid om te worden weergegeven als een doorlopende hoogtelijn, in plaats van als individuele punten. Dat maakt het mogelijk dat puntenwolken soortgelijk worden gerenderd als vector- of rasterlagen. Gebruikers kunnen de instelling voor tolerantie aanpassen om resultaten te verbeteren als er te weinig punten aanwezig zijn in de weergave, zonder de gehele laag te trianguleren.

<img src="images/entries/ab52589956629cc34cb09bef22e63478a65a96bf.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Mogelijkheid: Schaalverhouding afstand:hoogte weergeven in menu voor instellingen van profiel
Een nieuwe widget is toegevoegd voor het weergeven van de huidige schaalverhouding afstand:hoogte voor plots van hoogteprofielen. De widget kan ook worden gebruikt om een specifieke verhouding in te stellen. Als de optie "vergrendelen"  voor de plot is ingeschakeld, dan zal die schaalverhouding worden gebruikt, in plaats van de standaardverhouding 1:1 bij zoomen en navigeren in de plot.

<img src="images/entries/a4300b20ef89e4ad71f70a114af7438e4eff9cfb" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Erftverband](https://www.erftverband.eu/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Browser
### Mogelijkheid: Meerdere tabellen in database verplaatsen naar een ander schema
Toestaan dat meerdere tabellen in één keer worden verplaatst naar het gespecificeerde schema.

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Opmerking voor tabel database in Browser
De QGIS Browser bevat nu de optie om direct een **Opmerking tabel** te bewerken voor databases die deze functionaliteit ondersteunen.

<img src="images/entries/84b05ee5021e434fc16c6bc60bb1695584de7ecb.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Toegevoegd Ruimtelijke index maken of verwijderen aan menu Beheren in Browser
Een nieuwe optie voor het contextmenu is toegevoegd om Ruimtelijke indexen te **maken** of te **verwijderen** voor providers die dat ondersteunen.

<img src="images/entries/797d36c2dd01a3e0120c3835d360861033d5b516.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Gegevensproviders
### Mogelijkheid: Ondersteuning toegevoegd voor GML als een objectindeling voor OAPIF
De OGC API for Features bronconfiguratie bevat nu ondersteuning voor uitvoer van GML. Gebruikers kunnen die selecteren in het combinatievak in het dialoogvenster "WFS-verbinding bewerken" als de server dat weergeeft als een objectindeling.<br />Verscheidene scenario's worden ondersteund:
- Toegang tot bronnen kan worden verkregen met of zonder een beschikbaar XML-schema (via een koppeling rel=describedby). Net als met WFS kan het XML-schema worden bestudeerd met de eenvoudige schemaparser van QGIS, of met GDAL GMLAS one, afhankelijk van de geselecteerde "Modus Object".
- Objecten kunnen worden opgehaald met of zonder een koppeling voor een beschikbare bulkdownload (verschaft door een koppeling rel=enclosure)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Gebruikers van OAPIF toestaan een andere indeling te kiezen dan GeoJSON waarmee objecten moeten worden gedownload
Feature Services die worden geserveerd vanuit bronnen voor OGC API for Features die rekening houden met de parameter `outputFormat` in verbindings-URI's zouden aanvullende indelingen voor uitvoer moeten ondersteunen voor het ophalen van objecten (bijv. FlatGeoBuf, GeoJSON, etc.). Dit stelt gebruikers in staat om andere opties voor het ophalen van objecten te selecteren dan GeoJSON, uit bronnen die dat ondersteunen voor verbeterde prestaties, compatibiliteit, of uitbreidbaarheid, overeenkomstig hun noodzaken.<br />In het dialoogvenster voor de verbinding van de service kunnen gebruikers het nieuwe combinatievak gebruiken om hun geprefereerde indeling voor de uitvoer te selecteren. In aanvulling daarop maakt een nieuwe globale instelling voor het configureren van "lastFeatureFormatEncoding" het mogelijk de eerder gedefinieerde waarde als standaard voor nieuwe verbindingen te gebruiken.

<img src="images/entries/3f0add13c921416314030ca3f9ff12118dd288b2.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Bijwerken en verwijderen van velddomeinen in GPKG toestaan
Nieuwe menu-items stellen gebruikers in staat om velddomeinen voor databronnen van GPKG bij te werken en te verwijderen. Vereist GDAL \>= 3.12

<img src="images/entries/3e5c8b252b192ecd9022ac7a0a638307c46bc52f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: QGIS-projecten opslaan en importeren in PostgreSQL via Browser
QGIS ondersteunt nu zelf de mogelijkheid om het huidige project van QGIS op te slaan naar een database van PostgreSQL, alsook het importeren van projecten van QGIS uit een map naar een database van PostgreSQL.<br />Twee nieuwe menu-items voor verbindingen van PostgreSQL zijn toegevoegd:
- Een voor het opslaan van het huidige geopende project van QGIS direct naar het schema.
- Het tweede item maakt het in batch importeren mogelijk van projecten van QGIS naar het schema. Projectnamen worden gecontroleerd op botsingen met namen, en automatisch verhogende waarden voor achtervoegsels (bijv. `_1`, `_2`, etc.) worden toegevoegd als de projectnaam al bestaat in het schema.

<img src="images/entries/b139e1711b8d62c9064db1df0e8bce5b242cea96.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Informatie Laageigenschappen toevoegen aan provider PostgreSQL
QGIS bevat aanvullende informatie in de **Laageigenschappen** voor lagen van PostgreSQL, inclusief:
- Rechten voor de gebruiker voor de tabel
- Schatting van de rijen
- Informatie over ruimtelijke indexen

<img src="images/entries/37e33067b2665adbfd5202b1825df30a71b1ce37.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Methode voor authenticatie Planetary computer toegevoegd
Een nieuwe methode voor authenticatie wordt verschaft om te gebruiken met de Microsoft Planetary Computer STAC-catalogus. De Planetary Computer vereist het gebruiken van SAS-ondertekeningstokens voor toegang tot de meeste van de gegevens voor zijn onderdelen. Iets wat was geïmplementeerd in de oude plug-in voor STAC, maar ontbrak in de bronimplementatie voor STAC.<br />Er zijn nu twee modi voor de nieuwe methode voor authenticeren:
- Een is voor de Open versie van Planetary Computer, die het ondertekenen met SAS uitvoert voor onderdelen
- De tweede is voor Planetary Computer Pro GeoCatalogs, waar, in aanvulling op het ondertekenen met SAS van onderdelen, ook een authenticatie met OAuth2 vereist is<br />De nieuwe methode voor authenticatie kan worden gebruikt met verbindingen voor STAC, of direct worden toegepast op individuele GDAL- of puntenwolklagen waarvan de databron op Planetary Computer staat. Wanneer een laag wordt toegevoegd vanuit een catalogus van STAC of direct met Databronnen beheren, zal de `authcfg` worden toegevoegd aan zijn URI, dus zal QGIS die configuratie gebruiken voor de netwerkverzoeken. Authcfg coderen/decoderen werd ook toegevoegd aan puntenwolklagen.

<img src="images/entries/0ed79ce1c54933c720853f364cdd505ea4292261.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Microsoft

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros)
### Mogelijkheid: QGIS-projectversionering in PostgreSQL
Voor projecten van QGIS die de functionaliteit verhogen om direct te worden opgeslagen in PostgreSQL, kan automatisch versiebeheer worden ingeschakeld. Dat stelt gebruikers in staat om historische kopieën van hun project op te slaan, te laden, te bewerken en te herstellen. Het proces wordt voor het grootste deel afgehandeld door een functie en een activatiebewerking in de database van PostgreSQL. Meerdere nieuwe menu-items en dialoogvensters worden verschaft om gebruikers fijn afgestemd beheer te geven over het proces voor versiebeheer.

<img src="images/entries/e6362175a8d1662e590efecd2b1e48f62ec79c51.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Beschikbare verbindingen opslaan en standaardindeling afbeeldingen
Slaat in de instellingen de geprefereerde indeling voor een verbinding van WMS op.

Maakt het mogelijk de feitelijk door de server geadverteerde indelingen te detecteren en slaat die in de instellingen op voor toekomstig gebruik.

<img src="images/entries/9736fdc6bcb34c3bbdf6d85cf3d9eaa567176313.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## QGIS Server
### Mogelijkheid: Ongeldige projectlagen proberen te herladen
In QGIS Server bestaat een optie om slechte lagen te negeren; maar lagen die zijn geïdentificeerd als slecht, zouden later toch beschikbaar kunnen komen, zoals een mislukte netwerkservice die zich herstelt (webserver/ database, etc.).<br />QGIS Server heeft daarom een nieuwe optie voor `QGIS_SERVER_RETRY_BAD_LAYERS`. Als deze optie is ingesteld op true, controleert de server bij elk verzoek of de slechts lagen opnieuw beschikbaar zijn. Als een laag beschikbaar is, wordt die gemarkeerd als geldig en zal deze door de server worden gebruikt.

Dit werd mogelijk gemaakt door Stadtwerke München (SWM)

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Mogelijkheid: Implementeren GetFeatureInfo voor lagen met mazen
QGIS Server verschaft nu antwoorden voor verzoeken GetFeatureInfo voor lagen met mazen.

<img src="images/entries/fd8d94bd934381d9c5670b78bba29159ddcfcf93.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Jorge Gustavo Rocha](https://github.com/jgrocha)
### Mogelijkheid: Optie voor configureren van bronpad voor URI van OAPIF
Maak het bronpad voor de service OAPIF te configureren met een nieuwe instelling voor de server:<br />QGIS_SERVER_API_WFS3_ROOT_PATH

Wijzig de standaard van “/wfs3” naar “/ogcapi”.

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Programmeerbaarheid
### Mogelijkheid: Ondersteuning toegevoegd voor area3D aan QgsGeometry
De klasse QgsGeometry is uitgebreid met `area3D`, wat het 3-dimensionale oppervlakgebied van de geometrie is.
- Voor een punt of een lijn is het altijd gelijk aan 0.
- Voor een polygoon is het gelijk aan het 3D-gebied van de buitenste ring minus het 3D-gebied van de binnenste ringen.
- Voor een polyhedraal en een TIN is het gelijk aan de som van de 3D-gebieden van al zijn blokken.
- Voor een GeometryCollection is het gelijk aan de som van de 3D-gebieden van al zijn geometrieën.

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid: Ondersteuning toegevoegd voor 3D-punten in de methode pointsAreCollinear van QgsGeometryutils
Eerdere versies van de methode `QgsGeometryUtilsBase::pointsAreCollinear` werkten alleen voor 2D-punten; het is nu uitgebreid om 2D- en 3D-punten te ondersteunen en roept de corresponderende functie `QgsGeometryUtilsBase` aan. Een nieuwe `QgsGeometryUtilsBase::points3DAreCollinear` is ook geïntroduceerd, die werkt voor 3D-punten.

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Mogelijkheid:  Implementatie van QgsVectorLayer.as_geopandas()
De PyQgis API verschaft nu een methode om eigen objecten QgsVectorLayer te converteren naar gegevensframes van Geopandas, inclusief de attributen. Onthoud dat dit de bibliotheek GeoPandas vereist, als een afhankelijkheid in de omgeving van QGIS.

<img src="images/entries/cf6f4588f8da7d899a519e10117847b68fcbe292.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Mogelijkheid: Weergeven 3D-kaartgereedschappen in PyQgis API
Gebruikers kunnen nu aangepaste kaartgereedschappen maken om te interacteren met het 3D-kaartvenster met de basisklasse `Qgs3DMapTool`.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Weergeven 3D-kaartvenster modus Kruisdeel in PyQgis API
De 3D-functionaliteit *Gereedschap Kruisdeel* wordt nu weergegeven in de PyQgis API. Men kan nu gemakkelijk de vier vlakken voor clippen maken en toepassen op een 3D-kaartweergave met Python en de kaartcoördinaten van een 3D-weergave.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Ray casting opnieuw vorm gegeven en weergeven in PyQgis API
De gedupliceerde klasse `Ray3D` is verwijderd ten faveure van `QgsRay3D`, waaraan de ontbrekende methoden overeenkomstig zijn toegevoegd. Het weergeven van `Qgs3DMapCanvas::castRay()` in de PyQgis API zal plug-ins van Python effectief toestaan ray casting uit te voeren in 3D-kaartvensters en de resulterende hits te beheren.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: TemplatedLineSymbolLayer om inschakelen van blanco gebieden te implementeren
De QGIS API werd uitgebreid om het implementeren van bewerkingen aan blanco gebieden te ondersteunen. In lijn met [QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345).

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Algoritme Naaf afstand geporteerd naar C++
Het algoritme voor Processing Afstand naaf is geporteerd van Python naar C++.<br />Dit algoritme vervangt de algoritmes Distance to nearest hub (points) en Distance to nearest hub (line to hub), omdat het twee optionele uitvoeringen produceert, net als die twee algoritmes. De originele algoritmes zijn gemarkeerd als vervallen.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Ondersteuning toegevoegd voor bibliotheek SFCGAL
Eigen ondersteuning voor SFCGAL, een geavanceerde geometrische bibliotheek voor berekeningen, is toegveoegd aan QGIS in lijn met [QEP \#340](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/340).<br />Deze mogelijkheid voegt twee primaire aanvullende klassen toe aan de QGIS API:
- QgsSfcgalEngine: Geeft de SFCGAL C API weer in QGIS. Voegt ook geheugen- en foutenbeheer toe.
- QgsSfcgalGeometry: Bevat een hendel voor de weergave van geometrie van SFCGAL om converteren van geometrie te beperken tussen QGIS en SFCGAL<br />Ontwikkeld met ondersteuning van:
- CEA/DAM
- CP4SC/France Relance/Europese Unie
- Stad Frankfurt am Main
- Oslandia
- OPENGIS.ch

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server won't render VRT in WMS requests | [\#64733](https://github.com/qgis/QGIS/issues/64733) | Geen bug: lokaal probleem bij instellen van de omgeving |  |
| QGIS Server ignores MAP override when QGIS_PROJECT_FILE is set | [\#64723](https://github.com/qgis/QGIS/issues/64723) | Won't fix (not a bug) |  |
| Server: landingpage webapp only functions if built with server python plugins support | [\#64556](https://github.com/qgis/QGIS/issues/64556) | [PR \#64763](https://github.com/qgis/QGIS/pull/64763) | Nee |
| Raster calculator fails when OpenCL acceleration is turned on | [\#64574](https://github.com/qgis/QGIS/issues/64574) | [PR \#64779](https://github.com/qgis/QGIS/pull/64779) | Nee |
| Singleband Gray Shader should create 32 bit values not just 16 bit | [\#64560](https://github.com/qgis/QGIS/issues/64560) | Won't fix (not a bug) |  |
| Virtual raster provider memory leak - memory not released until QGIS closed | [\#64559](https://github.com/qgis/QGIS/issues/64559) | [PR \#64785](https://github.com/qgis/QGIS/pull/64785) | NOG TE DOEN |
| \[gdal\] Consider mask bands as a normal alpha band | [\#64642](https://github.com/qgis/QGIS/issues/64642) | [PR \#64795](https://github.com/qgis/QGIS/pull/64795) |  |
| Raster Attribute Table for S-102 does not display correctly | [\#64797](https://github.com/qgis/QGIS/issues/64797) | [PR \#64811](https://github.com/qgis/QGIS/pull/64811) | NOG TE DOEN |
| Arrow symbol layer data-defined properties not using defaults for NULL |  | [PR \#64680](https://github.com/qgis/QGIS/pull/64680), [PR \#64828](https://github.com/qgis/QGIS/pull/64828) |  |
| "Reuse last entered value" not applied when using PyQGIS | [\#64655](https://github.com/qgis/QGIS/issues/64655) | Won't fix (not a bug) |  |
| SpatiaLite provider returns wrong schema for views (caches columns from underlying joined tables instead of view definition) | [\#64742](https://github.com/qgis/QGIS/issues/64742) | [PR \#64902](https://github.com/qgis/QGIS/pull/64902) | NOG TE DOEN |
| Updated Canvas gives inconsistent Min / Max values and colour ranges for a local raster vs. the same raster in postgres | [\#64917](https://github.com/qgis/QGIS/issues/64917) | [PR \#64953](https://github.com/qgis/QGIS/pull/64953) | [PR \#64998](https://github.com/qgis/QGIS/pull/64998) |
| Bands get cleared after attribute table creation fails, causing rendering issues and crashes | [\#65040](https://github.com/qgis/QGIS/issues/65040) | [PR \#65052](https://github.com/qgis/QGIS/pull/65052) |  |
| \[ogr\]\[gpkg\] Fix wrong row count when attribute filter | [\#65067](https://github.com/qgis/QGIS/issues/65067) | [PR \#65097](https://github.com/qgis/QGIS/pull/65097) | Nee |
| \[ogr\] Add OGR_L_GetAttributeFilter | [\#65067](https://github.com/qgis/QGIS/issues/65067) | [PR \#14005](https://github.com/OSGeo/gdal/pull/14005) | N/B |
| visualizing GDAL raster with band scale and offset values will introduce very large histograms into the raster | [\#59461](https://github.com/qgis/QGIS/issues/59461) | [PR \#63294](https://github.com/qgis/QGIS/pull/63294) |  |
| Rendering of PostGIS rasters ignores Transparency NoData value setting | [\#63171](https://github.com/qgis/QGIS/issues/63171) | [PR \#63258](https://github.com/qgis/QGIS/pull/63258) | Ja |
| Add additional QStringLiteral entries to SQLite utils | [\#50553](https://github.com/qgis/QGIS/issues/50553) | [PR \#63105](https://github.com/qgis/QGIS/pull/63105) |  |
| 'Fixed Interval' and 'Pretty Breaks' Graduated Renderers don't work when field has all the same values | [\#63277](https://github.com/qgis/QGIS/issues/63277) | [PR \#63298](https://github.com/qgis/QGIS/pull/63298) |  |
| Identify Features tool ignores Transparency NoData value setting on PostGIS rasters | [\#63133](https://github.com/qgis/QGIS/issues/63133) | [PR \#63321](https://github.com/qgis/QGIS/pull/63321) |  |
| Raise warning when trying to modify read-only layer with field calculator | [\#63111](https://github.com/qgis/QGIS/issues/63111) | [PR \#63337](https://github.com/qgis/QGIS/pull/63337) |  |
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | Kan niet (meer) worden gereproduceerd |  |
| QGIS Server Layer(s) not valid Exception with multiple projects using same WMS Layer | [\#62608](https://github.com/qgis/QGIS/issues/62608) | Kan niet worden gereproduceerd |  |
| Adjusting min/max cumulative count cuts for rasters in layer styling panel | [\#63075](https://github.com/qgis/QGIS/issues/63075) | Kan niet worden gereproduceerd (terugkoppeling) |  |
| Refresh layer at interval has no effect after loading project | [\#63007](https://github.com/qgis/QGIS/issues/63007) | [PR \#63389](https://github.com/qgis/QGIS/pull/63389) |  |
| Browser not showing CurvePolygons in LTR or Latest |  | [PR \#63404](https://github.com/qgis/QGIS/pull/63404) |  |
| Copy one style category and paste it collectively to multiple layers removes the settings of the other style categories | [\#63167](https://github.com/qgis/QGIS/issues/63167) | [PR \#63408](https://github.com/qgis/QGIS/pull/63408) |  |
| Value relation widget does excessive calls to PostGIS database | [\#63410](https://github.com/qgis/QGIS/issues/63410) | [PR \#63418](https://github.com/qgis/QGIS/pull/63418) |  |
| Adding a network file vector layer ends with a lot of server calls for the same data | [\#63407](https://github.com/qgis/QGIS/issues/63407) | Kan niet worden gereproduceerd (terugkoppeling) |  |
| Sld export error with expression based labels | [\#63402](https://github.com/qgis/QGIS/issues/63402) | [PR \#63419](https://github.com/qgis/QGIS/pull/63419) |  |
| Selective pasting style does not change the ‘Automatically insert into print layout legend elements’ setting in raster layers | [\#63346](https://github.com/qgis/QGIS/issues/63346) | [PR \#63430](https://github.com/qgis/QGIS/pull/63430) |  |
| Value Relation with current_value() not updating when changes made outside of the attribute form | [\#63448](https://github.com/qgis/QGIS/issues/63448) | [PR \#63468](https://github.com/qgis/QGIS/pull/63468) |  |
| @current_feature VS @feature | [\#63488](https://github.com/qgis/QGIS/issues/63488) | Geen bug in de code (misschien in documentatie) |  |
| Qgis Desktop does not honor layer order in get capabilites in external wms | [\#62918](https://github.com/qgis/QGIS/issues/62918) | [PR \#63492](https://github.com/qgis/QGIS/pull/63492) |  |
| Using "Subset filter" from the "Execute SQL" dialog is not applied | [\#62542](https://github.com/qgis/QGIS/issues/62542) | [PR \#63605](https://github.com/qgis/QGIS/pull/63605) |  |
| SQL editor allow undo after clear | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2025-October/067839.html) | [PR \#63621](https://github.com/qgis/QGIS/pull/63621) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgis/gdal garbage collection causes segfault | [\#58724](https://github.com/qgis/QGIS/issues/58724) | [PR \#64766](https://github.com/qgis/QGIS/pull/64766) | Nee |
| NetCDF with EPSG:3416 misaligned is latest qgis ltr | [\#64873](https://github.com/qgis/QGIS/issues/64873) | [PR \#13886](https://github.com/OSGeo/gdal/pull/13886) | N/B |
| Bug in QgsVectorFileWriter when providing the name of the FID field | [\#63320](https://github.com/qgis/QGIS/issues/63320) | [PR \#64878](https://github.com/qgis/QGIS/pull/64878) | [PR \#64903](https://github.com/qgis/QGIS/pull/64903) |
| QgsVectorFileWriter: fix writing NurbsCurve to OGR, by converting them to LineString | Niet gerapporteerd | [PR \#64906](https://github.com/qgis/QGIS/pull/64906) | N/B |
| Build issue on NixOS | [\#64937](https://github.com/qgis/QGIS/issues/64937) | Ongeldig |  |
| Float16 rasters do not render correctly | [\#64923](https://github.com/qgis/QGIS/issues/64923) | [PR \#64990](https://github.com/qgis/QGIS/pull/64990) | [PR \#65024](https://github.com/qgis/QGIS/pull/65024) |
| building master in pkgsrc; mostly ok! | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2026-February/068072.html) | Is geen probleem |  |
| Rasters with GCPs and overviews render incorrectly when zoomed out | [\#65011](https://github.com/qgis/QGIS/issues/65011) | [PR \#13968](https://github.com/OSGeo/gdal/pull/13968) | N/B |
| Huge Performance Regression using VRTs on Versions \> 3.40.6 | [\#63293](https://github.com/qgis/QGIS/issues/63293) | [PR \#13116](https://github.com/OSGeo/gdal/pull/13116) | N/A (GDAL fix) |
| Problème lecture shapefile | [\#63787](https://github.com/qgis/QGIS/issues/63787) | [PR \#4599](https://github.com/OSGeo/PROJ/pull/4599) | N/B (reparatie PROJ) |
| USE_PRECOMPILED_HEADERS related issue | [mail thread](https://lists.osgeo.org/pipermail/qgis-developer/2025-November/067871.html) | [PR \#63794](https://github.com/qgis/QGIS/pull/63794) | [PR \#63811](https://github.com/qgis/QGIS/pull/63811) |
| Crash trying to open a shapefile | [\#63826](https://github.com/qgis/QGIS/issues/63826) | [PR \#13350](https://github.com/OSGeo/gdal/pull/13350) | N/A (GDAL fix) |
| Replace all remaining uses of connect(,SIGNAL,,SLOT) in src/ | Niet gerapporteerd | [PR \#63832](https://github.com/qgis/QGIS/pull/63832) | N/B |
| Crash with invalid WMS/WMTS source | [\#62372](https://github.com/qgis/QGIS/issues/62372) | [PR \#63833](https://github.com/qgis/QGIS/pull/63833) | [PR \#64016](https://github.com/qgis/QGIS/pull/64016) |
| JSON column from GeoPackage is not read correctly | [\#62377](https://github.com/qgis/QGIS/issues/62377) | Kan niet langer worden gereproduceerd / waarschijnlijk al gerepareerd |  |
| Fix build warnings on Fedora | Niet gerapporteerd | [PR \#63910](https://github.com/qgis/QGIS/pull/63910) | N/B |
| Fix cppcheck missingOverride and functionConst warnings | Niet gerapporteerd | [PR \#63913](https://github.com/qgis/QGIS/pull/63913) | N/B |
| \[CI\] Port OGC tests to ubuntu:25.10 Qt6 | Niet gerapporteerd | [PR \#64135](https://github.com/qgis/QGIS/pull/64135) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| pyqt5_to_pyqt6.py: Some known incompatibilities do not lead to error exit code | [\#62559](https://github.com/qgis/QGIS/issues/62559) | [PR \#63526](https://github.com/qgis/QGIS/pull/63526) | Nee |
| \[PyQt5_to_PyQt6\] Fix all imports coming from Qt module | Niet gerapporteerd | [PR \#63565](https://github.com/qgis/QGIS/pull/63565) |  |
| QgsLayoutExporter.exportToPdf() does not have the same return value type if an iterator is passed or not | [\#62501](https://github.com/qgis/QGIS/issues/62501) | Niet repareren? |  |
| Broken themes in geospatial PDF | [\#62014](https://github.com/qgis/QGIS/issues/62014) | [PR \#63580](https://github.com/qgis/QGIS/pull/63580) | NOG TE DOEN |
| pyqt5_to_pyqt6.py produces broken syntax for imports | [\#64185](https://github.com/qgis/QGIS/issues/64185) | [PR \#64926](https://github.com/qgis/QGIS/pull/64926) | [PR \#64941](https://github.com/qgis/QGIS/pull/64941) |
| pyqt5_to_pyqt6.py does not catch "from PyQt5 import QtWidgets" etc | [\#63711](https://github.com/qgis/QGIS/issues/63711) | [PR \#64930](https://github.com/qgis/QGIS/pull/64930) | [PR \#64939](https://github.com/qgis/QGIS/pull/64939) |
| The "Session Role" function is not applied to loaded layers | [\#62930](https://github.com/qgis/QGIS/issues/62930) | Al gerepareerd |  |
| set session role not working on creation of tables and schema | [\#63866](https://github.com/qgis/QGIS/issues/63866) | Kan niet worden gereproduceerd |  |
| Layout export to GeoPDF: incorrect layers' order when a "PDF Group" is set | [\#63475](https://github.com/qgis/QGIS/issues/63475) | [PR \#64983](https://github.com/qgis/QGIS/pull/64983) | NOG TE DOEN |
| pyqt5_to_pyqt6.py: Some suggestions reference wrong class | [\#64462](https://github.com/qgis/QGIS/issues/64462) | [PR \#64989](https://github.com/qgis/QGIS/pull/64989) | NOG TE DOEN |
| \[GeoPdfExport\] Avoid map theme contaminate non-map-theme items | Direct gerapporteerd zonder issue | [PR \#65008](https://github.com/qgis/QGIS/pull/65008) | [PR \#65108](https://github.com/qgis/QGIS/pull/65108) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Attribute table forced to be dockable and non modal - Crash several times | [\#62416](https://github.com/qgis/QGIS/issues/62416) | [PR \#64954](https://github.com/qgis/QGIS/pull/64954) | [PR \#64954](https://github.com/qgis/QGIS/pull/64954) |
| \- | \- | [PR \#65055](https://github.com/qgis/QGIS/pull/65055) | ? |
| With composite foreign keys, all widgets are configured by default | [\#32048](https://github.com/qgis/QGIS/issues/32048) | [PR \#65059](https://github.com/qgis/QGIS/pull/65059) | nee |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud (OPENGIS)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Germán Carrillo (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Project functions in editor, save doesn't really save...? | [\#62752](https://github.com/qgis/QGIS/issues/62752) | [PR \#63425](https://github.com/qgis/QGIS/pull/63425) |  |
| Diagram properties related to variables and expressions are not saved | [\#62936](https://github.com/qgis/QGIS/issues/62936) | [PR \#63479](https://github.com/qgis/QGIS/pull/63479) |  |
| Crash in layer styling panel when closing a project if DD Property Assistant is open | Niet gerapporteerd | [PR \#63549](https://github.com/qgis/QGIS/pull/63549) |  |
| QGIS crashes when opening print layout | [\#64218](https://github.com/qgis/QGIS/issues/64218) | [PR \#64813](https://github.com/qgis/QGIS/pull/64813) | N/B |
| Fix custom node initialization for custom elevation profiles | [\#65058](https://github.com/qgis/QGIS/issues/65058) | [PR \#64762](https://github.com/qgis/QGIS/pull/64762) | N/B |
| Diagrams: histograms with only negative values don't render | [\#63980](https://github.com/qgis/QGIS/issues/63980) | [PR \#64992](https://github.com/qgis/QGIS/pull/64992) | [PR \#65211](https://github.com/qgis/QGIS/pull/65211) |
| Attributes Form is not the same when called via GUI or when called via PyQGIS | [\#65010](https://github.com/qgis/QGIS/issues/65010) | Is geen probleem |  |
| Layers added using a .qlr file cannot be added to an open Elevation Profile View | [\#58533](https://github.com/qgis/QGIS/issues/58533) | Al gerepareerd |  |
| Group title not updated in .qgs | [\#65085](https://github.com/qgis/QGIS/issues/65085) | Ongeldige bug, issue is gerelateerd aan een plug-in |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS)](https://opengis.ch/)
### Feature: Bug Fixes by Till Frankenbach (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Tabbing to start of custom formatted Date/Time field in attribute form not working | [\#65022](https://github.com/qgis/QGIS/issues/65022) | [PR \#65023](https://github.com/qgis/QGIS/pull/65023) |  |
| Plugin manager shows changelog of current version, even for upgradable plugins | [\#64792](https://github.com/qgis/QGIS/issues/64792) | nog te doen |  |
| QGIS does not request default style for WMS layer when in group/container | [\#63754](https://github.com/qgis/QGIS/issues/63754) | [PR \#65081](https://github.com/qgis/QGIS/pull/65081) |  |
| Several issues with a temporal WMS (only one image is displayed using the Temporal Controller) I | [\#64099](https://github.com/qgis/QGIS/issues/64099) | [PR \#64925](https://github.com/qgis/QGIS/pull/64925) |  |
| Several issues with a temporal WMS (only one image is displayed using the Temporal Controller) II | [\#64099](https://github.com/qgis/QGIS/issues/64099) | [PR \#64863](https://github.com/qgis/QGIS/pull/64863) |  |
| \[mvt\] WMS raster sources are not working | [\#61040](https://github.com/qgis/QGIS/issues/61040) | [PR \#65087](https://github.com/qgis/QGIS/pull/65087) |  |
| Add unit tests for unzip function in pyplugin installer | Gevraagd in [PR \#65051](https://github.com/qgis/QGIS/pull/65051) | [PR \#65119](https://github.com/qgis/QGIS/pull/65119) |  |
| Fix WMTS-T layers temporal capabilities resourceURL selection | [\#54043](https://github.com/qgis/QGIS/issues/54043) | [PR \#65190](https://github.com/qgis/QGIS/pull/65190) |  |
| Set selected section to the first section on focus in QgsDateTimeEdit | [\#65022](https://github.com/qgis/QGIS/issues/65022) | [PR \#65023](https://github.com/qgis/QGIS/pull/65023) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach (OPENGIS)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| 'Identify' function in a 'QgsMapToolIdentify' descendant crashes | [\#61372](https://github.com/qgis/QGIS/issues/61372) |  |  |
| VPC Virtual Point Cloud - Do not show the point cloud or really lately in Vue2D | [\#59793](https://github.com/qgis/QGIS/issues/59793) |  |  |
| Curl SSL error | [\#33](https://github.com/PDAL/wrench/issues/33) |  |  |
| VPC Virtual Point Cloud - Error when creating VPC from HTTPS/URI sources | [\#59802](https://github.com/qgis/QGIS/issues/59802) | [PR \#66](https://github.com/PDAL/wrench/pull/66) |  |
| LAS/LAZ file without CRS fails to load | [\#50438](https://github.com/qgis/QGIS/issues/50438) |  |  |
| PDAL prevents LAS/LAZ 1.4 from opening if global_encoding set as 1 | [\#51862](https://github.com/qgis/QGIS/issues/51862) |  |  |
| Fix 3d view shortcuts | Niet gerapporteerd | [PR \#63523](https://github.com/qgis/QGIS/pull/63523) |  |
| Fix zooming with right mouse button in 3D views | Niet gerapporteerd | [PR \#63537](https://github.com/qgis/QGIS/pull/63537) |  |
| Fix 3d point lights | Niet gerapporteerd | [PR \#63525](https://github.com/qgis/QGIS/pull/63525) |  |
| 3D map view does not update on layer filter changes | [\#62925](https://github.com/qgis/QGIS/issues/62925) | [PR \#63477](https://github.com/qgis/QGIS/pull/63477) | [PR \#63511](https://github.com/qgis/QGIS/pull/63511) |
| Fix 2d rendering of remote COPC files in virtual point clouds | [comment](https://github.com/qgis/QGIS/issues/59793#issuecomment-3351352812) | [PR \#63471](https://github.com/qgis/QGIS/pull/63471) |  |
| 3D Tiles in 3D View: Loading 2 tiles | [\#63340](https://github.com/qgis/QGIS/issues/63340) | [PR \#63469](https://github.com/qgis/QGIS/pull/63469) |  |
| 3.44.1 hangs after exporting 256 images of 3D animation | [\#62959](https://github.com/qgis/QGIS/issues/62959) | [PR \#63469](https://github.com/qgis/QGIS/pull/63469) |  |
| Update untwine to 1.5.1 |  | [PR \#63543](https://github.com/qgis/QGIS/pull/63543) |  |
| Update pdal_wrench to 1.2.2 from upstream |  | [PR \#63544](https://github.com/qgis/QGIS/pull/63544) |  |
| Update MDAL to 1.3.2 from upstream |  | [PR \#63546](https://github.com/qgis/QGIS/pull/63546) |  |
| \[3D\] Avoid clamping vertices to actual nodata value | Niet gerapporteerd | [PR \#64845](https://github.com/qgis/QGIS/pull/64845) |  |
| Data corruption using "Split Features" on a LineStringZ in GeoJSON | [\#63581](https://github.com/qgis/QGIS/issues/63581) | [PR \#64986](https://github.com/qgis/QGIS/pull/64986) | In behandeling |
| Changing styling of a VPC layer resets the previous styling | [\#59419](https://github.com/qgis/QGIS/issues/59419) | [PR \#64988](https://github.com/qgis/QGIS/pull/64988) | [PR \#65020](https://github.com/qgis/QGIS/pull/65020) |
| Fix sip_include.sh after pyqt5 removal | Niet gerapporteerd | [PR \#64974](https://github.com/qgis/QGIS/pull/64974) | N/B |
| Make the extent widget hold the full precision of the chosen extent | Niet gerapporteerd | [PR \#64919](https://github.com/qgis/QGIS/pull/64919) |  |
| Fix endless terrain levels generation | Niet gerapporteerd | [PR \#64875](https://github.com/qgis/QGIS/pull/64875) |  |
| Always check pointer initialized inside if initializer | Niet gerapporteerd | [PR \#64871](https://github.com/qgis/QGIS/pull/64871) |  |
| No "Style manager" tab for point clouds in Layer styling panel | [\#64789](https://github.com/qgis/QGIS/issues/64789) | [PR \#64868](https://github.com/qgis/QGIS/pull/64868) |  |
| Tidy includes in point clouds and 3d code | Niet gerapporteerd | [PR \#64820](https://github.com/qgis/QGIS/pull/64820) |  |
| Remove code for QT version \< 6.6 | Niet gerapporteerd | [PR \#64809](https://github.com/qgis/QGIS/pull/64809) |  |
| Plugin installer can leave a plugin in a broken state on failed upgrade | [\#64790](https://github.com/qgis/QGIS/issues/64790) | [PR \#64807](https://github.com/qgis/QGIS/pull/64807) | NOG TE DOEN |
| Avoid module wide QtConcurrent imports | Niet gerapporteerd | [PR \#64775](https://github.com/qgis/QGIS/pull/64775) |  |
| Avoid crash when edit-in-place layer is removed | Niet gerapporteerd | [PR \#65107](https://github.com/qgis/QGIS/pull/65107) | Topo |
| 3D Map View crashes QGIS when project uses UTM projection | [\#41171](https://github.com/qgis/QGIS/issues/41171) | Kan niet langer worden gereproduceerd |  |
| Simple lines rendered incorrectly in 3D | [\#51286](https://github.com/qgis/QGIS/issues/51286) | Kan niet langer worden gereproduceerd |  |
| Some feature are not rendered in a 3d map view when using rule based renderer | [\#47581](https://github.com/qgis/QGIS/issues/47581) | Al gerepareerd |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgs3daxis: Fix axis label visibility in qt6 | Niet gerapporteerd | [PR \#63585](https://github.com/qgis/QGIS/pull/63585) |  |
| qgs3daxis: Fix cube picking in qt6 when clicking on a label | Niet gerapporteerd | [PR \#63585](https://github.com/qgis/QGIS/pull/63585) |  |
| \[3D\] fix terrain obj export | Niet gerapporteerd | [PR \#63173](https://github.com/qgis/QGIS/pull/63173) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| PDAL processing are not exposed if QGIS is build without PDAL support | [\#63106](https://github.com/qgis/QGIS/issues/63106) | [PR \#63181](https://github.com/qgis/QGIS/pull/63181) |  |
| Georeferencer: "Trasformation Settings" window is too tall and it disappears when trying to resize it | [\#63157](https://github.com/qgis/QGIS/issues/63157) | [PR \#63192](https://github.com/qgis/QGIS/pull/63192) |  |
| Vector "Layer Properties -\> Legend" window is too tall and it disappears when trying to resize it | [\#63159](https://github.com/qgis/QGIS/issues/63159) | [PR \#63204](https://github.com/qgis/QGIS/pull/63204) | [PR \#63290](https://github.com/qgis/QGIS/pull/63290) |
| Unclear message for incompatible plugins in Plugin Manager | [\#62606](https://github.com/qgis/QGIS/issues/62606) | [PR \#63205](https://github.com/qgis/QGIS/pull/63205) |  |
| ExecuteSQL algorithm does not allow input layers without geometry | [\#63218](https://github.com/qgis/QGIS/issues/63218) | [PR \#63229](https://github.com/qgis/QGIS/pull/63229) | [PR \#63237](https://github.com/qgis/QGIS/pull/63237) |
| Import Geotagged Photos tool not reading HEIC EXIF data | [\#60853](https://github.com/qgis/QGIS/issues/60853) |  |  |
| Casting point geometry of a feature to QgsPointXY crashes Qgis 3.40 | [\#60963](https://github.com/qgis/QGIS/issues/60963) |  |  |
| qgis renders single band paletted image with valid data mask as multiband | [\#61283](https://github.com/qgis/QGIS/issues/61283) | [PR \#63254](https://github.com/qgis/QGIS/pull/63254) | [PR \#63363](https://github.com/qgis/QGIS/pull/63363) |
| "No" notification when activating "GRASS GIS Processing Provider" without GRASS installed | [\#61672](https://github.com/qgis/QGIS/issues/61672) | [PR \#63303](https://github.com/qgis/QGIS/pull/63303) |  |
| Fix handling of tiled scene and vector tile layers in Processing | Niet gerapporteerd | [PR \#63323](https://github.com/qgis/QGIS/pull/63323) | [PR \#63343](https://github.com/qgis/QGIS/pull/63343) |
| Processing "Output folder" parameter seems unreliable if left to default value | [\#61965](https://github.com/qgis/QGIS/issues/61965) | [PR \#63328](https://github.com/qgis/QGIS/pull/63328) | [PR \#63396](https://github.com/qgis/QGIS/pull/63396) |
| No layer name in "force by selected geometries" contextual menu if overlapping vector features | [\#50049](https://github.com/qgis/QGIS/issues/50049) | [PR \#63342](https://github.com/qgis/QGIS/pull/63342) |  |
| Temporary layers are invisible in canvas QGIS 3.28+ | [\#52149](https://github.com/qgis/QGIS/issues/52149) |  |  |
| QGIS GUI not displaying IAU codes in UI when in PROJ.db | [\#54514](https://github.com/qgis/QGIS/issues/54514) |  |  |
| Better control the scope of the "Run sipify" action | [\#62313](https://github.com/qgis/QGIS/issues/62313) | [PR \#63403](https://github.com/qgis/QGIS/pull/63403) |  |
| "Recent fonts" list is always empty | [\#52169](https://github.com/qgis/QGIS/issues/52169) | [PR \#63423](https://github.com/qgis/QGIS/pull/63423) | [PR \#63485](https://github.com/qgis/QGIS/pull/63485) |
| Copy-pasting a "label settings" item turns it into a "text format" item | [\#40217](https://github.com/qgis/QGIS/issues/40217) | [PR \#63440](https://github.com/qgis/QGIS/pull/63440) | [PR \#63490](https://github.com/qgis/QGIS/pull/63490) |
| Project Settings Panel - Can't Reach Dialog Buttons For Large Font Sizes | [\#58290](https://github.com/qgis/QGIS/issues/58290) |  |  |
| "Data source encoding" dropdown not shown in layer properties for delimited text layer | [\#55443](https://github.com/qgis/QGIS/issues/55443) | [PR \#63478](https://github.com/qgis/QGIS/pull/63478) | [PR \#63552](https://github.com/qgis/QGIS/pull/63552) |
| Addition of an option to select favourite tools in the processing menu | [\#56806](https://github.com/qgis/QGIS/issues/56806) |  |  |
| Undo/redo in Styling panel does not refresh canvas with labelling change | [\#60250](https://github.com/qgis/QGIS/issues/60250) | [PR \#63493](https://github.com/qgis/QGIS/pull/63493) | [PR \#63506](https://github.com/qgis/QGIS/pull/63506) |
| Check geometry (angle) does not check whether feature ID is unique | [\#61398](https://github.com/qgis/QGIS/issues/61398) | [PR \#63304](https://github.com/qgis/QGIS/pull/63304) |  |
| Building master (63a8d7b) fails on "call of overloaded (... QByteArray ...) is ambiguous" | [\#63560](https://github.com/qgis/QGIS/issues/63560) | [PR \#63574](https://github.com/qgis/QGIS/pull/63574) | [PR \#63606](https://github.com/qgis/QGIS/pull/63606) |
| Optional "Gap errors" output not really optional | [\#63614](https://github.com/qgis/QGIS/issues/63614) | [PR \#63616](https://github.com/qgis/QGIS/pull/63616) |  |
| Fix crash and wrong coordinate order in the WCS source widget | Niet gerapporteerd | [PR \#63615](https://github.com/qgis/QGIS/pull/63615) | [PR \#63632](https://github.com/qgis/QGIS/pull/63632) |
| Fix several issues with geometry check algorithms | Niet gerapporteerd | [PR \#63304](https://github.com/qgis/QGIS/pull/63304) |  |
| WCS Request fails due to wrong BBox using "Map Canvas Extent" or "Draw on Canvas" | [\#62528](https://github.com/qgis/QGIS/issues/62528) | [PR \#63542](https://github.com/qgis/QGIS/pull/63542) | NOG TE DOEN |
| wcs spatial extent uses wrong projection | [\#50432](https://github.com/qgis/QGIS/issues/50432) |  |  |
| String aggregate-related functions treat NULL and empty strings interchangeably | [\#35433](https://github.com/qgis/QGIS/issues/35433) | [PR \#63324](https://github.com/qgis/QGIS/pull/63324) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
## Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix nothing happens when zooming to very small line feature extent | Niet gerapporteerd | [PR \#65215](https://github.com/qgis/QGIS/pull/65215) | [PR \#65274](https://github.com/qgis/QGIS/pull/65274) |
| Don't immediately validate child algorithms in models | Niet gerapporteerd | [PR \#65183](https://github.com/qgis/QGIS/pull/65183) | N/B |
| \[browser\] Don't permit renaming tables which are open in the current project | Niet gerapporteerd | [PR \#65182](https://github.com/qgis/QGIS/pull/65182) | N/B |
| Extend timeout for processing executable tests | Niet gerapporteerd | [PR \#65161](https://github.com/qgis/QGIS/pull/65161) | [PR \#65224](https://github.com/qgis/QGIS/pull/65224) |
| Downgrade thread safety check to non-fatal | Niet gerapporteerd | [PR \#65148](https://github.com/qgis/QGIS/pull/65148) | N/B |
| Fix network fetching tasks triggered by rendering of map layers using raster marker symbol layer never complete | [\#65137](https://github.com/qgis/QGIS/issues/65137) | [PR \#65147](https://github.com/qgis/QGIS/pull/65147) | Te riskant, potentiële backport na 3.44.10? |
| \[server\] Fix completely broken service url setting handling | Niet gerapporteerd | [PR \#65117](https://github.com/qgis/QGIS/pull/65117) | [PR \#65226](https://github.com/qgis/QGIS/pull/65226) |
| Fix broken value range when calling deprecated setComponentValue int variant | Niet gerapporteerd | [PR \#65115](https://github.com/qgis/QGIS/pull/65115) | [PR \#65135](https://github.com/qgis/QGIS/pull/65135) |
| \[wms\] Fix regression in encode/decodeUri | Niet gerapporteerd | [PR \#65114](https://github.com/qgis/QGIS/pull/65114) | N/B |
| Fix a bunch of python tests weren't actually run on CI | Niet gerapporteerd | [PR \#65113](https://github.com/qgis/QGIS/pull/65113) |  |
| Fix assert triggered on qt6 builds | Niet gerapporteerd | [PR \#65079](https://github.com/qgis/QGIS/pull/65079) | N/B |
| \[gdal\] Fix openfilegdb raster path decoding/encoding | Niet gerapporteerd | [PR \#65078](https://github.com/qgis/QGIS/pull/65078) | [PR \#65096](https://github.com/qgis/QGIS/pull/65096) |
| Fix mdb files not shown in browser for non-windows platforms | Niet gerapporteerd | [PR \#65077](https://github.com/qgis/QGIS/pull/65077) | [PR \#65098](https://github.com/qgis/QGIS/pull/65098) |
| Fix failing dock widget test on newer Qt versions | Niet gerapporteerd | [PR \#65073](https://github.com/qgis/QGIS/pull/65073) | N/B |
| \[browser\] Prevent deletion or rename of fields when table is open in project | Niet gerapporteerd | [PR \#64958](https://github.com/qgis/QGIS/pull/64958) | Niet geschikt |
| Fix strict curved label anchoring when placement is on line | Niet gerapporteerd | [PR \#64736](https://github.com/qgis/QGIS/pull/64736) | [PR \#64801](https://github.com/qgis/QGIS/pull/64801) |
| Move to QGIS4 settings storage, add migration from QGIS3 | [\#61636](https://github.com/qgis/QGIS/issues/61636) | [PR \#64752](https://github.com/qgis/QGIS/pull/64752) | N/B |
| Ensure QString and Qt::StringLiterals namespace are present when needed | Niet gerapporteerd | [PR \#64724](https://github.com/qgis/QGIS/pull/64724) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
