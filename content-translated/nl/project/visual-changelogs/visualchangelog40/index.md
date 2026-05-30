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

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt and Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Objecten in een array langs een lijn kopiëren
Een nieuw kaartgereedschap stelt gebruikers in staat om objecten in een array te kopiëren langs een lijn en is beschikbaar voor typen geometrie polygoon/lijn/punt geometry types.

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

Dit werd mogelijk gemaakt door [free time, inspired by :)](https://github.com/qgis/QGIS/pull/64495)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Gebruikergedefinieerde werkbalk en menu maken
QGIS staat gebruikers nu toe om gebruikergedefinieerde menu's en werkbalken te maken om krachtige opties voor aanpassingen te verschaffen.<br />Dit implementeert [QEP \#343](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-343-customized-toolbars-and-menus.md).

<img src="images/entries/553f1a2b5712a2f02d6a5a038197c1baefe6c012" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt and Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Attributentabel dubbelklik zoom
Gebruikers kunnen nu dubbelklikken op een item in de attributentabel om direct een object te selecteren en naar het geselecteerde object te zoomen.

<img src="images/entries/50fa542fa614721b36cac2efce700c9800a33c59.gif" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nass](https://github.com/lanckmann)
## Symbologie
### Mogelijkheid: Kopiëren/plakken van alle stijlen uit ene laag naar een andere toestaan
Wanneer een laag meerdere stijlen heeft, bevat het contextmenu van de boom met lagen nu een nieuwe actie "Alle stijlen kopiëren". Activeren hiervan zal de definitie van ALLE stijlen van de lagen naar het klembord kopiëren.<br />Gebruikers kunnen het contextmenu op een andere laag openen en de nieuwe mogelijkheid "Alle stijlen gebruiken" om kopieën van ALLE stijlen van de originele laag naar het doel te plakken. Dit verwijdert de noodzaak om handmatig door de bestaande stijlen in de originele laag te gaan, en de stijleen een voor een te plakken.

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
- selecteren van annotationitem(s), met de aanpassingstoets Shift om te schakelen voor het selecteren van aanvullende item(s)
- muis- en toetsenbordverplaatsing van geselecteerde item(s)
- verwijderen van geselecteerde item(s)
- afmetingen wijzigen van geselecteerde item(s) met de handvatten voor de muis
- draaien van geselecteerde item(s) met de handvatten voor de muis

<img src="images/entries/db55791d9e7c92428f8165d661bc264fd09ae61c.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Mogelijkheid: Tekstannotaties weergeven in 3D-kaartweergaven
Wanneer een annotatielaag is ingesteld om te renderen als 3D-plakborden, rendert het ook tekstannotaties als plakborden.<br />Voor tekstannotaties lijn/rechthoek wordt het plakbord geplaatst in het midden van de lijn/rechthoek. Gebruikers kunnen de gebruikte tekstindeling voor het 3D-plakbord. De originele indeling 2D-annotatietekst wordt genegeerd, wat gebruikers in staat stelt<br />een leesbare/meer toepasselijke tekstindeling te ontwerpen voor alleen de 3D-tekst.

<img src="images/entries/ce930ee001993bd8bd7ecf0477aac6e5e9436da1.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Ondersteuning voor renderen van markeringen voor Annotatielaag als 3D-aanplakborden
Een nieuwe optie voor het weergeven van annotatielagen in 3D-kaarten is toegevoegd. Vanuit de eigenschappen voor de annotatielaag, tab 3D, kunnen gebruikers de laag instellen om te renderen als 3D-aanplakborden. Indien geactiveerd, worden alle MARKERINGEN van de laag weergegeven als zwevende symbolen aanplakbord bovenop de 3D-kaart (lijnen en polygonen van de laag worden genegeerd).<br />⁣ Gebruikers hebben beheer over het klemmen van het terrein en verschuiving voor de aanplakborden, en of al dan niet  lijnen voor "tekstballonnen" zouden moeten worden weergegeven (verticale lijnen die verbinden met het aanplakbord op de corresponderende locatie op het terreinoppervlak).

<img src="images/entries/a74b316080040084674f70ed22492ad06da3c5be.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Labelen
### Mogelijkheid: Optie toegevoegd voor negeren witruimte bij detecteren labelbotsingen
Deze nieuwe optie (dia ALLEEN beschikbaar is voor modi voor het plaatsen van gebogen labels) beheert hoe QGIS witruimte behandelt (d.i. spaties of tabs) in labeltekst bij het bepalen of twee labels botsen (of wanneer een label botst met een obstakelobject). Het bestaande (en standaard) gedrag is dat spaties hetzelfde worden behandeld als tekens tekst en een label mag geen spaties overlappen op een ander label.<br /> Als de nieuwe optie "Witruimte label negeren bij detecteren botsingen" is geselecteerd, dan zal witruimte in de tekst worden genegeerd bij het controleren van overlappende labels (of labels die botsen met obstakels).<br /> Dit is nuttig bij het labelen van objecten op lange lijnen, als de woordruimte groot is en het gewenst is om tekst of andere objecten toe te staan de labelruimten op te vullen. (Bijv. bij labelen van rivieren of wegen). De instelling mag data-bepaalde zijn, functionaliteit inschakelen die wordt aangedreven door geavanceerde expressies, zoals het toestaan alleen te worden ingeschakeld voor objecten van voldoende lengte, etc.

<img src="images/entries/25ba4e122bd28db3d8cbf57717e1b4576dc790a5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Mogelijkheid: Labelen meerdelige geometrie opnieuw bewerkt
Het bestaande keuzevak voor “Label every part of multi-part features” is opnieuw bewerkt om een combinatievak te gebruiken om de keuzes voor opties voor afhandelen van meerdere delen weer te geven.<br />De beschikbare opties zijn:
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
Gebruikers kunnen nu een keuzemenu gebruiken onder Bronnen masker bij het configureren van het masker voor een laag en selecteren uit een aantal voorkeuzen om maskers efficiënt toe te passen zonder complex beheer. Dit is speciaal handig voor grote projecten als veel verschillende lagen naar dezelfde set bronnen voor maskers moeten verwijzen. Zoals wanneer veel lagen zijn gemaskeerd met dezelfde set afzonderlijk gelabelde lagen.<br />De standaardwaarde is "aangepast", wat de bestaande ad-hoc per-laag-configuratie herhaalt. Gebruikers zijn echter in staat waar nodig sets voor selectieve maskers te maken, te hernoemen of te verwijderen, en alle wijzigingen aan de geselecteerde bronnen voor een voorkeuze zullen automatisch de wijzigingen toepassen op ALLE aan de voorkeuze gekoppelde lagen.

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
- **Synchroniseren met zichtbare lagen**: Deze optie zal rekening houden met lagen die momenteel zichtbaar zijn in de kaart die is gekoppeld aan het item voor de legenda (of hoofdboom van de lagen, als geen kaart is gekoppeld aan de legenda). Wanneer deze modus actief is, zullen alle wijzigingen aan de set met lagen die zichtbaar is in de kaart ervoor zorgen dat de lagen van de legenda overeen zullen komen met deze set zichtbare lagen. Onthoud dat deze modus verschilt van de bestaande optie "Alleen items in gekoppelde laag weergeven", omdat de modus "Synchroniseren met zichtbare lagen" helemaal geen rekening houdt met de bereikingen van de gekoppelde kaart - als een laag is geselecteerd en zichtbaar is voor de kaart, dan zal die worden weergegeven in de legenda. Ongeacht of alle objecten van de laag al dan niet buiten het zichtbare laagbereik vallen. Net als met de optie "Synchroniseren met alle projectlagen" worden eventuele wijzigingen aan de namen of andere aan de legenda gerelateerde instellingen in de hoofdboom van de lagen automatisch doorgevoerd in de legenda van de afdruklay-out.
- **Handmatig**: Alle inhoud voor de legenda kan handmatig door de gebruiker worden beheerd, en er zal geen automatisch synchroniseren worden toegepast op welke laag dan ook. Dit is hetzelfde gedrag als momenteel gebeurt in QGIS als de optie "Live bijwerken" niet is geselecteerd.

De vroegere bewerking "Alles bijwerken" voor legenda's is gewijzigd naar een nieuwe functie "Herstellen", die de configuratie van de legenda terug zal zetten naar de geselecteerde modus.<br />Deze wijziging bevat een nieuwe globale instelling die is toegevoegd aan de pagina Opties - Lay-out. Dat geeft gebruikers de kans om de standaardmodus voor nieuw gemaakte legenda's te beheren. Standaard zal
QGIS de modus "Synchroniseren met zichtbare lagen" gebruiken om een betere ervaring out-of-the-box te geven voor gebruikers met grote projecten; gebruikers kunnen echter het eerdere standaardgedrag herstellen door deze instelling overeenkomstig te wijzigen.

<img src="images/entries/3b47cf11887bdd0717b6cef55fdcb5f7b7ac0c13.gif" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Deense QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add data-defined control over layout map grid annotation visibility, and additional expression variables for grids
This allows for PER-ANNOTATION control over the map grid text visibility. i.e., it allows for individual grid annotations to be selectively hidden or shown. The `@grid_axis` and `@grid_number` expression variables are available for use in the expression. New expression variables have also been introduced, making it easy to do things like hide the first/last grid annotations selectively:
- @grid_count: Totale aantal zichtbare rasterlijnen voor de huidige as van het raster.
- @grid_index: De index van de momenteel getekende rasterlijn (beginnend met 1 voor de eerste rasterlijn). De index is specifiek voor de huidige as van het raster.

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Allow for atlas geometries to reshape the frame of map items
A new clip frame function has been added that, when enabled, reshapes layout map items frames to match the (polygon) geometry of the current atlas feature. This allows flexible clipping and masking in atlas items, especially where canvas background color is an integral part of the rendering (e.g., vector tile base maps).

<img src="images/entries/6cadd40d1ebfa64b6190c75334df0340c00a4d93.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Feature: Brand new pie chart plot type
A new pie chart has been added to the available plot types in QGIS and its layout designer.

<img src="images/entries/ae30dae66281636965dbff50915b96b6ecbabacc.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Feature: Print Layout Charts Implementation
A new layout chart item has been added, which allows users to leverage chart rendering into their print and atlas layouts. Chart configurations are defined using an extensive set of properties provided in the properties panel and a number of sub-panels.<br />The chart item builds visualizations from data series of X and Y values, which are derived from a source layer that is configured through the item properties' data source group. Each series is defined using expressions to evaluate the X and Y values, as well as the possibility to filter the source layer, with each property configured via a subpanel. Iteration through the source layer can be ordered, which will be taken into account by the bar/line charts.

<img src="images/entries/65b7cdfcb7c7595f007a1911e51894e3cfab80dc.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Feature: Add an atlas option to limit coverage layer rendering to the current feature only
A new atlas option was added to limit rendering of features on the coverage layer to the current feature only, allowing the dynamic exclusion of other features without requiring complex expressions using the active atlas feature.

<img src="images/entries/7f1b58c91bf273f63b125dc5fe30327ae18068ed.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Feature: Add set extent to layer item in the map item's toolbar menu
A new menu action has been added to the toolbar for layout maps that allows users to quickly set a given map item's extent to match the extent of a spatial layer in the project.

<img src="images/entries/e4ba1fa83ed9a5601b434666eb8952eb270b970e" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
### Feature: Brand new layout item rotation handles
Rotation handles have been added for selected layout item(s), allowing users to tweak item rotation and perfect their layouts.

<img src="images/entries/eaed49778b763c98749a2d37a9e4654602911616.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Stad Frankfurt – Stadtplanungsamt

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://opengis.ch)
## Expressies
### Feature: Add "equals" geometry function
A new `equals(geometry1, geometry2)` geometry function has been added, which will test the equality of two geometries (in the same manner as `overlay_equals`).

<img src="images/entries/8bd21615869e1defb47183b43aa131ecb2dbab17.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add expression functions for working with magnetic models
New expressions for handling magnetic model details are now available, including::
- @grid_index: Geeft de daling van een magnetisch veld op een punt aan, in graden Oost of Noord
- magnetic_inclination: Geeft de stijging van een magnetisch veld op een punt aan, in graden naar beneden vergeleken met horizontaal
- magnetic_declination_rate_of_change: Geeft de mate van wijzigen van de daling van een magnetisch veld op een punt aan, in graden per jaar
- magnetic_inclination_rate_of_change: Geeft de mate van wijzigen van de stijging van een magnetisch veld op een punt aan, in graden per jaar

Dit is heel nuttig voor metadata in afdruklay-outs en

<img src="images/entries/54affd11032e735eee18b4ef94d8f654a8d7acf8.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add extract_degrees, extract_minutes, extract_seconds functions
These functions are designed to make it easy to customise the display of a degree-based grid annotation, by allowing easy extraction of the individual components of the decimal degree value for individual formatting (e.g., displaying the degrees in bold)
- extract_degrees: Extracts the integer number of degrees from a decimal degrees value. The minutes and seconds components are ignored. The extracted degrees values will be truncated towards zero (not rounded).
- extract_minutes: Extracts the integer number of minutes from a decimal degrees value. The degrees and seconds components are ignored. The extracted minutes values will be truncated towards zero (not rounded), and will always be a positive value.
- Neemt het integer getal voor minuten uit een decimale waarde voor graden uit. De componenten graden en minuten worden genegeerd. De uitgenomen waarden voor seconden zullen altijd een positieve waarde zijn.

<img src="images/entries/afca4fe52738eae1b242ae2720e0bbbb97f119fe.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [LINZ](https://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add unaccent function based on PostgreSQL unaccent
A new unaccent method is provided that removes accents (diacritic signs) from lexemes, e.g `unaccent( "ï" )`.

<img src="images/entries/1d59428a063df21c5d83676b45e83771e56f5aca.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Tudor Barascu](https://github.com/tudorbarascu)
### Feature: Add substr_count expression
The new `substr_count` expression simply allows users to count the occurrences of a substring within a string.

<img src="images/entries/09cbb9e54d4b4326ced2b4bdcf8c93736960af0a.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Tudor Barascu](https://github.com/tudorbarascu)
### Feature: Add some timezone related expression functions
Adds some functions for working with timezones in expressions:
- `timezone_from_id`: Maakt een object tijdzone uit een tekenreeks ID (uit de database voor tijdzones van IANA).
- `timezone_id`: Geeft de tekenreeks van de ID voor een object tijdzone terug, gebruikt ID's uit de database voor tijdzones van IANA.
- `get_timezone`: Geeft het object tijdzone terug dat is geassocieerd met een waarde datetime.
- `convert_timezone`: Converteert een object datetime naar een andere tijdzone.
- `set_timezone`: Stelt het object voor de tijdzone in die is geassocieerd met een waarde datetime, zonder de componenten datum of tijd te wijzigen. Deze functie kan worden gebruikt om de tijdzone voor een datetime te wijzigen.

<img src="images/entries/67fe7d4aa19caa1698e52c9d27e2dd954b809bb9.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Digitaliseren
### Mogelijkheid: Kaartgereedschap Bézier
New GUI controls for part digitization using NURBS curves are provided by adding the "poly-bézier" / "freeform" curve mode, which uses anchors and handles to control curve shape in a manner similar to many graphic design tools.<br />Users can click and drag ot add a point with handles, and reset handles on a point using `alt+click`.

<img src="images/entries/584c6a12ea7a79081fa1fce9f86d9c7d80ecf31c.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt and Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: Add area and total length/perimeter CAD dock floater values
New floater values are provided on the advanced digitizing CAD Tools interface, providing the option to show area and total length/perimeter values using Cartesian or Ellipsoidal calculations based on user selection (note that CAD tools uses Cartesian coordinates for digitization, which may result in differences between the displayed ellipsoidal values).

<img src="images/entries/03e5d6b7b5c5ad9449f6abcb73c3dc21706b5ec5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense QGIS gebruikersgroep](https://qgis.dk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add Maptool to handle chamfer and fillet of polygons
A new digitizing Maptool allows users to chamfer or fillet polygons.

<img src="images/entries/58ace0c2995032999b366d0171a78857e687d3c4.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt and Oslandia](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Gegevensbeheer
### Feature: Enhanced COG support for raster exports
The Raster Exports and Save dialogs now support explicit options to specify that the output should be exported with Cloud Optimized GeoTiff optimization, with additional COG-specific pyramid features, including improvements for:
- progress reporting
- error handling
- pyramid generation operations

Note that this requires GDAL \>= 3.13.0

<img src="images/entries/60cec0aa212eb189e7749c242ba1ca49423ca845.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Copy raw attribute values
QGIS now makes the raw (original) attribute values visible and copyable in both Attribute tables and the Identify Result interface.<br />In previous versions, data values were copied only in their "represented" form, i.e., the values that are evaluated by locale settings, expressions, or display values (e.g, foreign key values).<br />The new "Copy Raw Cell Content" option, available from the context menu, will copy literal values from the source data to the clipboard.

<img src="images/entries/cbc449f46c49440ac88d7f89a36e490d4d1deb20.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ct. Solothurn

Deze mogelijkheid werd ontwikkeld door [signedav](https://github.com/signedav)
### Feature: Allow storing Comments in QGIS Projects stored in PostgreSQL
QGIS projects stored in PostgreSQL can now include comments with additional information, which is displayed in the browser using a Tooltip.

<img src="images/entries/fa9f5d8b4ba7be7475799d104df2c4e96cc26f71.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Allow named layers as temporary output
This functionality allows the user to name a temporary output layer that is the result of a processing algorithm. The fact that the layer is temporary is identifiable by the temporary icon (memory chip) displayed before the user defined layer name.

<img src="images/entries/3fec097dc50545f03ab62e3cff5688b719d23916" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door QGIS Deense gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Possibility to change the layer name in the layer panel when saving a scratch layer
When saving a scratch layer as a permanent layer with a new name (a different file name than the name in the layer panel), a message bar is shown. In this message bar, the user can choose to automatically change the name in the layer panel to the new layer name.<br />This message bar is only shown if the layer is saved with a new name, and currently, this only works for some filetypes (it works for geopackages but not for shapefiles).

<img src="images/entries/f4d0c0c524eed26129c8c59c406018085e071220" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door QGIS Deense gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Suggest a file name when exporting layer or group as layer definition file
When saving a layer or a layer group as a layer definition file (.qlr), the filename field was left empty by default. QGIS now populates the name of the layer or group as a suggestion for the filename to reduce friction for style exports.

Deze mogelijkheid werd ontwikkeld door [pgipper](https://github.com/pgipper)
## Formulieren en widgets
### Feature: Add the ability to preview the attributes form within the vector layer properties dialog
QGIS now provides the ability to preview an attributes form while configuring it within the vector layer properties dialog.

<img src="images/entries/c0bb362e1f57600a820c2d185f77993abbd48318.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Refine reuse of last value and introduce remembrance toggle
QGIS Attribute Forms now include an enhanced user experience for handling the reuse of "last captured" values in forms. A pin icon on forms will give users visual feedback on whether a field's value will be remembered and reused, and provide an active toggle to control whether it should continue to be reused. Additional enhancements to the form configuration allow session-level reuse policies to be set, the default behavior for reuse policies (enabled/disabled), and the ability to disable reuse policies across all fields in a layer.

<img src="images/entries/b06e53bc63de8ea4643beb74c69781076b613d07.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door DB Fahrwegdienste GmbH

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Legenda van laag
### Feature: Add control over whether layers are included in automatic print layout legends
A new setting has been added in the layer properties legend tab (for vector, raster, mesh, and point cloud layers) for "Include automatically in print layout legend items". This setting is checked by default. Users must uncheck to exclude that layer from print layout legends.<br />This has also been added to the legend page for mesh and point cloud layers, with the generic setting for controlling embedded legend widgets.

<img src="images/entries/798344535f33fdaf2047bfbd3070def6d28bb6fb.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense QGIS gebruikersgroep](https://qgis.dk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Custom Elevation Profile Sources
QGIS now includes more powerful interactive behaviors for Elevation Profiles, including changing the layer visibility and rendering order on related canvases and linking the project layer tree to the profile plot sources.<br />This functionality is enabled by the introduction of the `QgsLayerTreeCustomNode` class, which enables the representation of application objects (other than layers and groups) in QGIS layer trees.

<img src="images/entries/8218225f95e403fe8e543f34b0427561371265b6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
## Processing
### Feature: Native polygon orientation algorithms
New algorithms for **Force polygons clockwise** (`native:forcecw`) and **Force polygons counter-clockwise** (`native:forceccw`) have been added to processing algorithms.<br />Force polygons clockwise replicates the existing "Force right-hand-rule" operation, and forces polygon geometries to respect the convention where the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.<br />Force polygons counter-clockwise performs the inverse, and forces polygon geometries to respect the convention where the exterior ring is oriented in a counter-clockwise direction and the interior rings in a clockwise direction.

<img src="images/entries/a0c4136c269a5cd474bdc29e15c26831baa8706f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Configure model components using an inline panel instead of modal dialogs
A new configuration panel has been added, docked to the right-hand side of the Processing model designer, which allows editing of model components without the modal dialogs, and replicating the user experience from the Layer Styling Panel. This improves the UX for model editing and prevents model configuration modals from blocking user interaction with other QGIS elements while model components are being edited. Users can still access the dialogs when double-clicking an item.

<img src="images/entries/c6368e5609a680adf719ca6cd1a95739278db0d2.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [City of Canning](https://www.canning.wa.gov.au/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add network analysis validation algorithms
Two new algorithms useful for validating networks have been added:
- Netwerk valideren
- Extract network endpoints

**Validate network**<br />This algorithm analyzes a network vector layer to identify data and topology errors that may affect network analysis tools (like shortest path). Optional checks include:
1. Validating the 'Direction' field to ensure all direction field values in the input layer match the configured forward/backward/both values. Errors will be reported if the direction field value is non-null and does not match one of the configured values.
2. Checking node-to-node separation. This check identifies nodes from the network graph that are closer to other nodes than the specified tolerance distance. This often indicates missed snaps or short segments in the input layer. In the case that a node violates this condition with multiple other nodes, only the closest violation will be reported.
3. Checking node-to-segment separation: This check identifies nodes that are closer to a line segment (e.g. a graph edge) than the specified tolerance distance, without being connected to it. In the case that a node violates this condition with multiple other edges, only the closest violation will be reported.

Two layers are output by this algorithm:
1. An output containing features from the original network layer that failed the direction validation checks.
2. An output representing the problematic node locations with an 'error' field explaining the error. This is a line layer, where the output features join the problematic node to the node or segment that failed the tolerance checks.

**Extract network endpoints**<br />This algorithm extracts the endpoints (nodes) from a network line layer. Two definitions are available for identifying endpoints:
1. Nodes with only all incoming or all outgoing edges: Identifies 'Source' or 'Sink' nodes based on the direction of flow. These are nodes where flow can start (only outgoing) or stop (only incoming).
2. Nodes connected to a single edge: Identifies topological 'dead-ends' or 'dangles', regardless of directionality. This checks if the node is connected to only one other distinct node.

<img src="images/entries/a26779141bcb3e43adeea67400b4666419f3a17f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [City of Canning](https://www.canning.wa.gov.au/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add feature preserving raster smoothing algorithm
This is a port of the Whitebox tool's equivalent algorithm, implementing the logic described in Lindsay, John et al (2019): LiDAR DEM Smoothing and the Preservation of Drainage Features.<br />It is effective at removing surface roughness from DEM) without significantly altering sharp features such as breaks-in-slope, stream banks, or terrace scarps.<br />This makes it superior to standard low-pass filters (e.g., mean, median, Gaussian) or resampling, which often blur distinct topographic features.<br />The algorithm works in three steps:
1. Calculating surface normal 3D vectors for each grid cell.
2. Smoothing the normal vector field using a filter that applies more weight to neighbors with similar surface normals (preserving edges).
3. Iteratively updating the elevations in the DEM to match the smoothed normal field.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add native raster gaussian blur algorithm
Allows applying a gaussian blur to a raster layer

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add native total curvature algorithm from the terrain analysis library
Adds the Total curvature algorithm to Processing. The total curvature filter has existed in the terrain analysis library for years, but it was never exposed in the GUI. It is now exposed to the Processing framework alongside the existing terrain analysis filters.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Expose NODATA and raster creation options for outputs in the terrain analysis tools
Expose output NODATA and raster creation options in the native raster terrain analysis tools (slope, aspect, hillshade, ruggedness index).

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add Dataset Identification GDAL Processing Algorithm
A new Data Identification algorithm allows for the automated extraction of metadata using GDAL.<br />This algorithm requires GDAL \>= 3.13.0, as it uses the new capabilities of [gdal dataset identify](https://gdal.org/en/stable/programs/gdal_dataset_identify.html).

<img src="images/entries/76dfc1189b899bedaa208692766fc765ccb76175.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Add a way to specify the raster format in processing algorithm outputs
This feature allows specifying the output format for rasters using GDAL configuration flags, primarily for enforcing Cloud Optimized GeoTiff outputs.<br />In previous versions, the output format was based on file format extension, which breaks for COG since both GDAL GTiff and COG drivers use the extension of `.tif/.tiff`. Users can now explicitly specify `-of COG` to enforce COG exports.

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Show the feature count flowing through a model inside the model designer
The long-requested ability to show the number of features flowing through the model has been added. The number of features is attached to the link going in and out between the algorithms, and it only applies to vector layers. The display of the feature count can be disabled using the "Show Feature Count" option in the view menu.<br />Note: To be able to display the feature count, the model needs to be run first at least once.

<img src="images/entries/468164c721e2407abaf86e0629d35377741dc2a6.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
### Feature: support max-triangle-edge-length in PDAL Export to raster (TIN) algorithm
Support for max-triangle-edge-length parameter has been added to the PDAL Export to raster (TIN) algorithm, so that triangles where the edge length is bigger than the specified threshold can be ignored.<br />This feature needs PDAL \>= 2.6.0 and wrench \>=1.2.2.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Model designer update
The QGIS Model Designer has had a significant update applied to the way in which it handles the input and output values between nodes to provide visual feedback in much more meaningful ways.<br />Individual parameters for node configuration are now exposed, and the connections between values from tools and variables are connected to nodes at the specific parameters where they are input and output accordingly.<br />Parameter Values are color-coded by data type (including generic data types like integer and string, but also complex QGIS-specific types such as vector and raster layers), allowing for enhanced visual indexing and traceability of data operations as they flow through the model.

<img src="images/entries/92bf8916e1ddc8d0e44b31f130d2029ac93b438f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Géo2France](https://www.geo2france.fr/portal/public/overview)

Deze mogelijkheid werd ontwikkeld door [Jonathan Lurie](https://github.com/jonathanlurie)
### Feature: Allow Reproject Layer algorithm to transform Z coordinates
An optional bool parameter to the *Reproject layer* algorithm has been added that allows for the transformation of Z coordinates.

<img src="images/entries/b93161af43e09fc6189680f8f8b323b86555d499.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add algorithm to create Cloud Optimized GeoTiffs from directory source
A new algorithm for Create Cloud Optimized GeoTIFF has been added that allows the creation of COGs for a set of input raster files provided in a dedicated folder and uses GDAL to perform a bulk conversion of the input files.

<img src="images/entries/7a822b6086fbf156b8f3528499f78a5d83eb7b29.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Add SFCGAL approximate medial axis processing algorithm
A new processing algorithm to approximate medial axis has been added which is based on the newly integrated SFCGAL backend.<br />The Approximate Medial Axis algorithm generates a simplified skeleton of a shape by approximating its medial axis. The output is a collection of lines that follow the central structure of the shape. The result is a thin, stable set of curves that capture the main topology while ignoring noise. This algorithm ignores the Z dimensions. If the geometry is 3D, the approximate medial axis will be calculated from its 2D projection.

<img src="images/entries/0804299923000a846f55b0b8fb0b50e19e3893d5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Feature: Scale and Resolution settings for WMS extraction
QGIS now enables Raster Extraction algorithms to work with WMSs requested at a given scale, so that scale-dependent rendering (symbology/labeling) is preserved in the output raster.<br />The improved algorithms are `Clip raster by extent` and `Clip raster by mask layer`.<br />A new advanced options panel is provided on WMS layers when used as a source in these algorithms, which provides options for:
- **Reference scale**: The scale at which the WMS raster should be requested/rendered.
- **Service resolution**: The resolution (in DPI) used by the server to render the WMS raster (by default 96 dpi).<br />These changes were enabled by the introduction of the `QgsProcessingRasterLayerDefinition` and `QgsWmsUtils` classes.

<img src="images/entries/532bbcaddf65f8d815ecdddd48ed71b067cdb855.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Germap](https://opengis.ch)
### Feature: Add duplicate features output layer parameter to Delete duplicate geometries Algorithm
This feature extends the "Delete duplicate geometries" processing algorithm so that the identified duplicate features that are deleted can be extracted and saved as a distinct file for further analysis.

<img src="images/entries/85ee1e8469a32c107d2bfc08ec468915399689a7.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add algorithms to filter parts by length/area
These new algorithms, "Remove parts by length" and "Remove parts by area", filter out parts of geometries from a vector layer by checking their area or length against a minimum size parameter.<br />If the input geometry is a multipart geometry, then the parts will be filtered by their individual sizes. If no parts match the required minimum size, then the feature will be skipped and omitted from the output layer. If the input geometry is a singlepart geometry, then the feature will be skipped if the geometry's size is below the required size and omitted from the output layer. Attributes are not modified.

<img src="images/entries/a3a539941a16aa0765fd05436e4e7228e3864553.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Add optional destination CRS for Package Layers algorithm
Allows for layers to be transformed into a specific output CRS, if set.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Package Layers algorithm - only export features intersecting a given extent
An optional parameter for `Extent` has been added to the Package Layers algorithm, allowing users to only export features that intersect a given extent from all the selected layers. If none of the features of a specific selected layer intersect the given extent, the layer will still be created and will be empty in the output GeoPackage.

<img src="images/entries/33644c3a135003c6e8df79e9eda8878004b6ea28" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Germap](https://github.com/gacarrillor)
### Feature: Unlimited model canvas size in the model designer
Previous versions of the QGIS model designer had a fixed canvas size of 4000 x 4000, and new models were started at the top left of the canvas, which could lead to frustration when elements went out of bounds. The QGIS model builder will now dynamically manage the scroll area and enable a much smoother user experience.

<img src="images/entries/6347778c8c50b9fa330e4985d19b980c2c8b676f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Hauts-de-France region

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
## Opties voor toepassing en projecten
### Feature: OAuth2 auto refresh
QGIS now includes an auto-refresh mechanism for OAuth2 connections.<br />A cache cleanup to stop the auto refresh is triggered periodically, and when a layer is removed from the project. This is required to avoid unnecessary, endless refreshing of unused tokens.

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Project trust for embedded code enhancement
QGIS now includes a project-level "trust" mechanism that grants or denies execution of embedded Python code within projects. This is implemented in line with the [Trusted Projects and Folders QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-336-trusted-projects-and-folders.md).<br />As established in the QEP, the embedded code types covered are:
- macros;
- expression functions;
- actions; and
- attribute form init code

This gives users the ability to allow for granular code execution at the project level instead of global settings limited only by user profile configuration.<br />QGIS will provide users with a project trust dialog to offer the user generic information on what features to allow as well as preview code accordingly. Global settings are provided to allow or deny execution of features at project and path levels.

<img src="images/entries/8325ef4b8268626c5af3c9699370dbeb6faedcd4.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Elevation Profile Manager
QGIS now links the app handling of elevation profiles to a new project-level elevation profile manager. Now, elevation profiles stored in the project can be reopened after opening a project, and changes made to the profile will be stored in the project.<br />There is also a fully functional elevation profile manager dialog, which is able to display/rename/remove elevation profiles from the project.

Dit werd mogelijk gemaakt door [Erftverband](https://www.erftverband.eu/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Project/layer metadata localization support
Translation support has been added for some key project and layer metadata values to QGIS' project translation system. This enhancement ensures that project translation can use the relevant metadata values for layout items such as labels, map canvas decorations, etc.<br />*This is funded through an ongoing effort to add support for localized/translated projects into QField*

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add project setting to enable HTML GetFeatureInfo maptip-only mode
A new project setting for QGIS Server is provided to enable HTML GetFeatureInfo maptip-only mode.<br />[This allows QGIS Server to use the WMS vendor parameter](https://docs.qgis.org/3.40/en/docs/server_manual/services/wms.html#with-maptip) `WITH_MAPTIP=HTML_FI_ONLY_MAPTIP` and use only the maptip for the HTML GetFeatureInfo response.

<img src="images/entries/5cefab81d09c5bf0e1b757238d74940a2c9d9c55" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
## Profiel plotten
### Feature: Add option to sync elevation profile layers with project layers
This new option is available from an elevation profile's settings menu as "Synchronize Layers to Project". It is unchecked by default, but when checked, the elevation profile's layers will always exactly match the project's main canvas layer structure, including groups and layer orders.<br />Groups cannot be created in the elevation profile. Any changes made to the main project's layer tree will immediately be reflected in the elevation profile's layer setup.

Dit werd mogelijk gemaakt door [Lutra](https://www.lutraconsulting.co.uk/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
### Feature: Render point cloud as a continuous elevation line
QGIS profile plots now include the ability for the elevation profile of a point cloud layer to be displayed as a continuous elevation line instead of individual points, allowing point clouds to be rendered similarly to vector or raster layers. Users can adjust the tolerance setting to improve results when too few points are present within the view, without triangulating the entire layer

<img src="images/entries/ab52589956629cc34cb09bef22e63478a65a96bf.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Deense Agency for Climate Data](https://www.klimadatastyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Dominik Cindric (Lutra Consulting)](https://github.com/ViperMiniQ)
### Feature: Show distance:elevation scale ratio in profile settings menu
A new widget has been added for the displaying of the current distance:elevation scale ratio for elevation profile plots. The widget can also be used to set a specific ratio. If the "lock" option is enabled for the plot, then this scale ratio will be used instead of the default 1:1 ratio when zooming and navigating the plot.

<img src="images/entries/a4300b20ef89e4ad71f70a114af7438e4eff9cfb" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Erftverband](https://www.erftverband.eu/)

Deze mogelijkheid werd ontwikkeld door [North Road](https://north-road.com/)
## Browser
### Feature: Move multiple tables in Database to another Schema
Allow multiple tables to be moved into the specified schema at once.

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Browser DB Table Comment
The QGIS Browser now includes the option to directly edit **Table comment** for databases that support this functionality.

<img src="images/entries/84b05ee5021e434fc16c6bc60bb1695584de7ecb.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Add create or delete Spatial Index to the Manage menu in Browser
A new context menu option has been added to **create** or **delete** Spatial Indexes on providers that support it.

<img src="images/entries/797d36c2dd01a3e0120c3835d360861033d5b516.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Gegevensproviders
### Feature: Add support for GML as a feature format for OAPIF
The OGC API for Features source configuration now includes support for GML outputs. Users may select it in the combo box in the "Modify WFS Connection" dialog if the server exposes it as a feature format.<br />Several scenarios are supported:
- Sources can be accessed with or without an XML schema available (through a rel=describedby link). As with WFS, the XML schema can be examined with the QGIS simple schema parser, or with GDAL GMLAS one, depending on the selected "Feature mode".
- Features can be retrieved with or without a bulk download link available (provided through a rel=enclosure link)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Allow OAPIF users to select an alternate format than GeoJSON with which to download features
Feature Services served from OGC API for Features sources that honour the `outputFormat` parameter in connection URIs should support additional output formats for retrieving features (e.g., FlatGeoBuf, GeoJSON, etc.). This allows users to select feature retrieval options other than GeoJSON from sources that support it for improved performance, compatibility, or extensibility according to their needs.<br />In the service connection dialog, users can use the new combo box to select their preferred output format. In addition, a new global setting for configuring "lastFeatureFormatEncoding" allows the previously defined value as the default for new connections.

<img src="images/entries/3f0add13c921416314030ca3f9ff12118dd288b2.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Allow update and delete for Field Domains in GPKG
New menu items allow users to update and delete Field Domains on GPKG data sources. Requires GDAL \>= 3.12

<img src="images/entries/3e5c8b252b192ecd9022ac7a0a638307c46bc52f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Save and import QGIS projects to PostgreSQL via Browser
QGIS now natively supports the ability to save the current QGIS project to a PostgreSQL database, as well as import QGIS projects from a folder into a PostgreSQL database.<br />Two new menu entries for PostgreSQL connections are added:
- One for saving the currently opened QGIS project directly to the schema.
- The second item allows batch import of QGIS projects to the schema. Project names are checked for name collisions, and autoincrementing suffix values (e.g. `_1`, `_2`, etc.) are added if the project name already exists in the schema.

<img src="images/entries/b139e1711b8d62c9064db1df0e8bce5b242cea96.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Add Layer Properties info to PostgreSQL provider
QGIS includes additional information in the **Layer Properties** for PostgreSQL layers, including:
- Privileges for the user regarding the table
- Estimation of rows
- Information about spatial indexes

<img src="images/entries/37e33067b2665adbfd5202b1825df30a71b1ce37.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Add auth method for Planetary computer
A new auth method is provided for use with the Microsoft Planetary Computer STAC catalog. The planetary computer requires using SAS sign tokens to access most assets' data, something that was implemented on the old STAC plugin but was missing from the core STAC implementation.<br />There are two modes for the new auth method:
- One is for the Open version of Planetary Computer, performing the SAS signing for assets
- The second is for Planetary Computer Pro GeoCatalogs, where, in addition to the SAS signing of assets, an OAuth2 authentication is also required<br />The new auth method can be used with STAC connections, or applied directly to individual gdal or point cloud layers whose data source is on the planetary computer. When a layer is added from a STAC catalog or directly using the data source manager, the `authcfg` will be appended to its URI so QGIS will use that config for the network requests. Authcfg encoding/decoding was also added to point cloud layers.

<img src="images/entries/0ed79ce1c54933c720853f364cdd505ea4292261.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Microsoft

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://github.com/uclaros)
### Feature: QGIS Project Versioning in PostgreSQL
For QGIS Projects that leverage the functionality to be stored directly in PostgreSQL, automatic version control can be enabled, which allows users to save, load, edit, and restore historic copies of their project. The process is mostly handled by a function and a trigger operation in the PostgreSQL Database, and multiple new menu items and dialogs have been provided to allow users granular control over the version management process.

<img src="images/entries/e6362175a8d1662e590efecd2b1e48f62ec79c51.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Store connections available and default image format
Stores in the settings the preferred format for a WMS connection.

Allows to detect the formats actually advertized by the server and stores them in the settings for future use.

<img src="images/entries/9736fdc6bcb34c3bbdf6d85cf3d9eaa567176313.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## QGIS Server
### Feature: Try to reload invalid project layers
In QGIS Server, there is an option to ignore bad layers; however, layers identified as bad may become available later on, such as a failed network service that recovers (web server/ database, etc.).<br />QGIS Server therefore has a new option for `QGIS_SERVER_RETRY_BAD_LAYERS`. If this option is set to true, the server checks upon each request if the bad layers are available again. If a layer is available, it is marked as valid and will be used by the server.

Dit werd mogelijk gemaakt door Stadtwerke München (SWM)

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Feature: Implement GetFeatureInfo for mesh layers
QGIS Server now provides responses for GetFeatureInfo requests on Mesh Layers.

<img src="images/entries/fd8d94bd934381d9c5670b78bba29159ddcfcf93.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Jorge Gustavo Rocha](https://github.com/jgrocha)
### Feature: OAPIF URL root path configuration option
Make the OAPIF service root path configurable through a new server setting<br />QGIS_SERVER_API_WFS3_ROOT_PATH

Change the default from “/wfs3” to “/ogcapi”.

Dit werd mogelijk gemaakt door [QGIS-DE - Anwendergruppe Deutschland e.V.](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Programmeerbaarheid
### Feature: Add support for area3D to QgsGeometry
The QgsGeometry Class is extended to include `area3D`, which is the 3-dimensional surface area of the geometry.
- For a Point or a LineString, it is always equal to 0.
- For a Polygon, it is equal to the 3D area of the exterior ring minus the 3d area of the interior rings.
- For a Polyhedral and a TIN, it is equal to the sum of the 3d areas of all its patches.
- For a GeometryCollection, it is equal to the sum of the 3d areas of all its geometries.

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Feature: Add support for 3d points in pointsAreCollinear method of QgsGeometryutils
Previous versions of the `QgsGeometryUtilsBase::pointsAreCollinear` method only worked for 2D points; it has now been extended to support 2D and 3D points and calls the corresponding `QgsGeometryUtilsBase` function. A new `QgsGeometryUtilsBase::points3DAreCollinear` has also been introduced, which works for 3D points.

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
### Feature: Implement QgsVectorLayer.as_geopandas()
The PyQgis API now provides a method to natively convert QgsVectorLayer objects to Geopandas dataframes, including the attributes. Note that this requires the GeoPandas library as a dependency in the QGIS Environment.

<img src="images/entries/cf6f4588f8da7d899a519e10117847b68fcbe292.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Feature: Expose 3D map tools to PyQgis API
Users can now create custom map tools to interact with the 3D map canvas using the `Qgs3DMapTool` base class.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Expose 3D map canvas cross section mode to PyQgis API
The 3D *Cross section tool* functionality is now exposed to the PyQgis API. One can now easily create and apply the four clipping planes to a 3D map view using Python and a 3D view's map coordinates.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: Refactor ray casting and expose to PyQgis API
The duplicated `Ray3D` class has been removed in favor of `QgsRay3D`, which has had missing methods added accordingly. The exposure of `Qgs3DMapCanvas::castRay()` to the PyQgis API will effectively allow Python plugins to perform ray casting in 3D map canvases and manage the resulting hits.

Dit werd mogelijk gemaakt door [SIGNON Deutschland GmbH](https://signon-group.com/en)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Feature: TemplatedLineSymbolLayer to enable blank areas implementation
The QGIS API was extended to support the implementation of blank area operations in line with [QEP \#345](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/345).

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Feature: Port Hub distance algorithm to C++
The Processing Hub distance algorithm has been ported from Python to C++.<br />This algorithm replaces Distance to nearest hub (points) and Distance to nearest hub (line to hub) algorithms as it produces two optional outputs as these two algorithms. The original algorithms are marked as deprecated.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add support for SFCGAL library
Native support for SFCGAL, an advanced geometric computations library, has been added to QGIS in line with [QEP \#340](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/340).<br />This feature adds two primary additional classes to the QGIS API:
- QgsSfcgalEngine: Exposes SFCGAL C API to QGIS. Also adds memory and error management.
- QgsSfcgalGeometry: Keeps a handle to SFCGAL geometry representation to reduce geometry conversion between QGIS and SFCGAL<br />Developed with support from:
- CEA/DAM
- CP4SC/France Relance/European Union
- Stadt Frankfurt am Main
- Oslandia
- OPENGIS.ch

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server won't render VRT in WMS requests | [\#64733](https://github.com/qgis/QGIS/issues/64733) | Not a bug: local issue with setting the environment |  |
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
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | Cannot reproduce (again) |  |
| QGIS Server Layer(s) not valid Exception with multiple projects using same WMS Layer | [\#62608](https://github.com/qgis/QGIS/issues/62608) | Kan niet worden gereproduceerd |  |
| Adjusting min/max cumulative count cuts for rasters in layer styling panel | [\#63075](https://github.com/qgis/QGIS/issues/63075) | Cannot reproduce (feedback) |  |
| Refresh layer at interval has no effect after loading project | [\#63007](https://github.com/qgis/QGIS/issues/63007) | [PR \#63389](https://github.com/qgis/QGIS/pull/63389) |  |
| Browser not showing CurvePolygons in LTR or Latest |  | [PR \#63404](https://github.com/qgis/QGIS/pull/63404) |  |
| Copy one style category and paste it collectively to multiple layers removes the settings of the other style categories | [\#63167](https://github.com/qgis/QGIS/issues/63167) | [PR \#63408](https://github.com/qgis/QGIS/pull/63408) |  |
| Value relation widget does excessive calls to PostGIS database | [\#63410](https://github.com/qgis/QGIS/issues/63410) | [PR \#63418](https://github.com/qgis/QGIS/pull/63418) |  |
| Adding a network file vector layer ends with a lot of server calls for the same data | [\#63407](https://github.com/qgis/QGIS/issues/63407) | Cannot reproduce (feedback) |  |
| Sld export error with expression based labels | [\#63402](https://github.com/qgis/QGIS/issues/63402) | [PR \#63419](https://github.com/qgis/QGIS/pull/63419) |  |
| Selective pasting style does not change the ‘Automatically insert into print layout legend elements’ setting in raster layers | [\#63346](https://github.com/qgis/QGIS/issues/63346) | [PR \#63430](https://github.com/qgis/QGIS/pull/63430) |  |
| Value Relation with current_value() not updating when changes made outside of the attribute form | [\#63448](https://github.com/qgis/QGIS/issues/63448) | [PR \#63468](https://github.com/qgis/QGIS/pull/63468) |  |
| @current_feature VS @feature | [\#63488](https://github.com/qgis/QGIS/issues/63488) | Not a code bug (maybe documentation) |  |
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
| Problème lecture shapefile | [\#63787](https://github.com/qgis/QGIS/issues/63787) | [PR \#4599](https://github.com/OSGeo/PROJ/pull/4599) | N/A (PROJ fix) |
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
### Feature: Bug Fixes by Denis Rouzaud (OPENGIS)
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
| Plugin manager shows changelog of current version, even for upgradable plugins | [\#64792](https://github.com/qgis/QGIS/issues/64792) | tbd |  |
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
