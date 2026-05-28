---
HasBanner: false
draft: false
releaseDate: 20-06-2025
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.44
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.44{#changelog344 }
<img src="images/projects/3807b5d1851cc87bda040f637e1f4024bc11c58a.png" class="img-responsive img-rounded center-block" />

Datum uitgave: 20-06-2025

Het project QGIS kondigt met trots de uitgave van QGIS 3.44 aan, een gedenkwaardige uitgave die de beëindiging kenmerkt van de QGIS 3-serie. Deze uitgave arriveert in een levendig en zich nog steeds uitbreidend ecosysteem van vrije en open-bron-georuimtelijke programma's, bibliotheken en ondersteuning van de gemeenschap die gebruikers wereldwijd stimuleert. Voortbouwend op de solide funderingen van eerdere uitgaven verschaft QGIS 3.44 een stabiele en verfijnde ervaring voor alle gebruikers als het project overgaat op het moderne Qt6-framework met de aanstaande uitgave van [QGIS 4.0](https://blog.qgis.org/2025/04/17/qgis-is-moving-to-qt6-and-launching-qgis-4-0/) in oktober 2025.

Als de laatste uitgave met mogelijkheden van de tak QGIS 3.x, zorgt deze uitgave voor een betrouwbare omgeving voor bestaande werkstromen, en ontwikkelaars van plug-ins kunnen zich voorbereiden op een gladde overgang tussen uitgaven, omdat QGIS 4.0 vervallen API's zal behouden om inspanningen voor compatibiliteit te minimaliseren en het ecosysteem in staat te stellen te evolueren naast de brontoepassing.

Hoewel gefocust op stabiliteit en verfijning, bevat de uitgave nog steeds een groot aantal opmerkelijke verbeteringen die werkstromen verfijnen en gebruikers stimuleren bij hun georuimtelijke inspanningen. Dergelijke verbeteringen bevatten verfijningen aan het beheren van databases en connectiviteit, verbeterde flexibiliteit voor gegevensproviders en nieuwe projectinstellingen. Oude favorieten, zoals de Toolbox van Processing en QGIS-expressies, krijgen ook hun rechtmatige deel aan verbeteringen en cartografische mogelijkheden krijgen een oppepper met nieuwe bijwerkingen voor labelen en lay-out.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=5a02yaDKAiE).

[![](https://img.youtube.com/vi/5a02yaDKAiE/0.jpg)](https://www.youtube.com/watch?v=5a02yaDKAiE)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Tijdbeheer
### Mogelijkheid:  Groepsknoop WMS-T toestaan dimensie tijd weer te geven
Een nieuwe optie om de groepsknoop van de boom van lagen de dimensie tijd weer te laten geven, die is toegevoegd aan lagen WMS-T is toegevoegd.

Een keuzevak in de groepseigenschappen van WMS maakt het mogelijk te schakelen met de berekening van deze tijdsdimensie. Indien ingeschakeld, zal het recursief de tijdsdimensie maken, gebaseerd op de tijdsdimensies van de kindlaag.

Een groep waarvan de berekening van de tijdsdimensie is uitgeschakeld, zal de tijdsdimensie van zijn kinderen niet doorgeven aan zijn ouder.

Datumbereik voor de tijdsdimensie is ook toegevoegd, in lijn met de standaarden OGC WMS en ISO8601.

<img src="images/entries/4916ef1bc94c95cbcb5b66d83e4c4093fe411693" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Vaste datum/tijd toegevoegd voor modus Tijdbeheer voor rasters
Stelt de gebruiker in staat om een vaste datum/tijd te selecteren in de eigenschappen voor Tijdbeheer van een rasterlaag, wat het mogelijk maakt dat het begin en einde van een tijdsperiode wordt afgeleid van een enkele invoerwaarde.

<img src="images/entries/d61699232fef2797a38e3fcbe18c65d889896308" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Gebruikersinterface
### Mogelijkheid: Een specifieke tab openen in het paneel Logboekmeldingen
QGIS ondersteunt nu het openen van berichten op een specifieke tab in het paneel Logboekmeldingen

Dit kan bijvoorbeeld worden gebruikt om een specifieke tab direct te openen voor een opgegeven provider of plug-in.

Dit wordt bereikt door de methode `openMessageLog` uit te breiden om de tabnaam als een parameter te accepteren. Als de opgegeven tabnaam niet wordt gevonden, zal het paneel worden weergegeven in zijn bestaande staat.

Opgenomen met deze wijziging is de uitbreiding van de methode iface, `iface.openMessageLog( tab_name )`.

Dit werd mogelijk gemaakt door [Stad Frankfurt – Stadtplanungsamt](https://www.stadtplanungsamt-frankfurt.de/about_us_5645.html)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Symbologie
### Mogelijkheid: Optie toegevoegd om niet-gebruikte categorieën te verwijderen in de widget symboolrenderer Categorieën
Een nieuwe optie is toegevoegd aan de widget symboolrenderer Categorieën om het voor de gebruikers mogelijk te maken in bulk niet-gebruikte categorieën te verwijderen.

Het gebruik van deze optie zal automatisch alle categorieën identificeren en verwijderen die niet overeenkomen in het attribuutveld of expressie die is gebruikt om de laag te categoriseren.

Dit is speciaal nuttig bij het gebruiken van een geclipte subset van gegevens die een grote set gecategoriseerde stijlen hebben geërfd.

<img src="images/entries/85eb6c595a8e44e2fd6deb1586215bc523861dfd.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Ben Wirf](https://github.com/benwirf)
## Labelen
### Mogelijkheid: Instellingen toegevoegd voor het beheren van marges rondom labels en voorkomen van duplicaatlabels
Twee nieuwe instellingen zijn geïntroduceerd voor labels van vectorlagen, namelijk:
- Marge rondom labels: Dit maakt het mogelijk een marge in te stellen rondom de labels van een laag, wat voorkomt dat alle andere labels worden geplaatst binnen deze margeafstand tot de labels van de laag.
- Duplicaatlabels voorkomen: Verwijdert labels binnen een minimale afstand voor ALLE lagen, met hoofdlettergevoleige overeenkomsten.

Dit kan worden gebruikt om het uiterlijk van de labels bij het renderen van complexe geografische situaties te verbeteren. Zoals gegevens van wegennetwerken, waar elementen zoals tweerichtingswegen, dienstwegen en andere entiteiten kunnen resulteren in veel identieke labelelementen, die dicht bij elkaar verschijnen.

<img src="images/entries/efc5a69fe9fa346ba7b2d6b9c3ec2b6d57b731d0.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## 3D-objecten
### Mogelijkheid: Gereedschap Kruisdeel
Een nieuw gereedschap is toegevoegd voor het maken van kruisdelen in een 3D-scène. De gebruiker kan een gedeelte in het 2D-kaartvenster kiezen (door te klikken op drie punten - beginpunt, eindpunt en dikte kruisdeel), dat ervoor zorgt dat de 3D-weergave alles eruit filtert wat buiten dat gebied ligt. De camera in de 3D-weergave wordt ook verplaatst om te kijken naar het gebied vanaf de zijkant.

Vergeleken met de configuratie van het bereik van de 3D-weergave, is het gereedschap Kruisdeel zowel sneller om te gebruiken (het hoeft niet de gehele scène opnieuw te laden als Kruisdeel is ingeschakeld/uitgeschakeld) en staat gedraaide rechthoekige gebieden toe.

<img src="images/entries/8034dbe7d55e297f052ef4d310beab10a56ddbb5.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Septima, Klimadatastyrelsen

Deze mogelijkheid werd ontwikkeld door [Matej Bagar](https://github.com/Withalion)
### Mogelijkheid: Weergave Globe
Er is een nieuwe modus voor 3D-scènes - weergave Globe - in aanvulling op de traditionele 3D-weergave, gebaseerd op een geprojecteerd CRS.

Elk type kaartlaag kan als 2D-textuur worden gebruikt voor de globe en 3D-renderers van getegelde scènelagen en lagen van puntenwolken worden ondersteund.

Weergave Globe gebruikt de ellipsoïde van het project om mazen voor de globe te maken. Het is zelfs mogelijk om andere hemellichamen te gebruiken, zoals Mars of de maan, als het CRS voor het project overeenkomstig is ingesteld.

Meer informatie:
- [QEP \#301 - Large scenes and globe in QGIS 3D](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301)
- [Cesium blog post](https://cesium.com/blog/2025/06/20/3d-globe-view-now-available-in-qgis/)

<img src="images/entries/b0ebe685540c3191ad07235d63e45176e9694551.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Cesium Ecosystem Grant

Deze mogelijkheid werd ontwikkeld door Lutra Consulting & North Road
### Mogelijkheid: Ondersteuning voor grote 3D-scènes
In eerdere versies van QGIS zou 3D-kaartweergave zich niet correct gedragen met scènes die groter zouden zijn dan 50-100 kilometer, wegens problemen met de numerieke precisie - de camera zou verkeerd verplaatsen (tot het punt van onbruikbaar) of objecten zouden onrustig zijn indien erop ingezoomd. Dat is nu opgelost - voor zowel lokale scènes als scènes voor Globe, zoals vermeld in [QEP 301](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/301).

Dit werd mogelijk gemaakt door Cesium Ecosystem Grant

Deze mogelijkheid werd ontwikkeld door Lutra Consulting & North Road
## Puntenwolken
### Mogelijkheid: Pdal_wrench bijgewerkt naar v1.2
Dit verschaft:
- Verbeterde ondersteuning voor virtuele puntenwolken (VPC) in algoritmes van Processing 
- De mogelijkheid om direct uit te voeren naar Cloud Optimized Point Cloud (COPC) voor verscheidene indelingen

Bekijk het [log met wijzigingen voor pdal_wrench](https://github.com/PDAL/wrench/releases/tag/v1.2) voor meer details over andere verbeteringen.

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation Vorarlberg

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Uitvoer COPC toestaan voor algoritmes van PDAL
Door de bijgewerkte afhankelijkheid pdal_wrench te verhogen, kan uitvoer voor algoritmes van PDAL nu worden gemaakt als Cloud Optimized Point Clouds

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation Vorarlberg

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Automatisch gebruiken van COPC-indexbestanden in gereedschappen van Processing
Als een bestand COPC een index beschikbaar heeft, zal QGIS nu automatisch die standaard gebruiken bij het uitvoeren van bewerkingen van Processing. Dat zal enkele bewerkingen sneller maken (bijv. clippen).

Dit werd mogelijk gemaakt door Landesamt für Vermessung und Geoinformation Vorarlberg

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Bewerken puntenwolk
Het is nu mogelijk lagen van puntenwolken te bewerken in de 3D-kaartweergaven. Gebruikers kunnen kiezen welk attribuut aan te passen, de doelwaarde en dan interactief punten selecteren die zouden moeten worden bewerkt.

er zijn verscheidene kaartgereedschappen om punten te selecteren om te bewerken:
- Met een polygoon selecteren 
- Met verfkwast selecteren
- Boven/Onder lijn selecteren

Gebruikers kunnen filteren voor te bewerken punten instellen met QGIS-expressies, zodat slechts van enkele punten hun attribuutwaarde wordt aangepast.

<div class="col-lg-8 col-md-offset-1">

<div class="iframe">

<div id="player">

</div>

<div class="player-unavailable">

# Er trad een fout op.{#changelog344 }
<div class="submessage">

<a href="https://www.youtube.com/watch?v=TRxW-g0HYjU" target="_blank">Bekijk deze video op www.youtube.com</a> of schakel JavaScript in als dat voor uw browser is uitgeschakeld.

</div>

</div>

</div>

</div>

Dit werd mogelijk gemaakt door Septima, Klimadatastyrelsen

Deze mogelijkheid werd ontwikkeld door Lutra Consulting
## Afdruklay-outs
### Mogelijkheid: Automatisch doorlopen na instelling voor legenda's van lay-out toegevoegd
De instelling Automatisch doorlopen maakt het mogelijk de tekst van de legenda automatisch te laten doorlopen na een vaste regellengte (ingesteld in millimeters).

Dit kan worden gebruikt om excessieve breedtes voor automatisch gemaakte legenda's te voorkomen.

<img src="images/entries/ec81517776eea3e38142ca38436789fbdb9e7f9a.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Mogelijkheid: Functie herhalen toegevoegd en variant omgekeerd voor tekenreeks
Nieuwe expressies omvatten:
- Een nieuwe functie 'repeat', die een tekenreeks een gespecificeerd aantal keer herhaald
- Een variant voor tekenreeks voor 'reverse' die het omdraaien van de tekenreeks mogelijk maakt

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Expressiefuncties om CRS te maken uit een  tekenreeksdefinitie en om authid van CRS te verkrijgen
Nieuwe expressiefuncties zijn toegevoegd die het beheren van coördinatenreferentiesystemen ondersteunen, namelijk:
- **crs_from_text**: Maakt een coördinatenreferentiesysteem uit een tekenreeksdefinitie. De tekenreeksdefinitie mag worden weergegeven met een CRS-code in de indeling `auth:id`, een definitie WKT of een tekenreeks voor PROJ die het CRS definieert.
- **crs_to_authid**: Geeft de tekenreeks voor identificatie van een coördinatenreferentiesysteem terug in de indeling `authority:id`, bijv. `EPSG:4326`.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
## Digitaliseren
###  Mogelijkheid: Beleid voor samenvoegen toegevoegd
Soortgelijk aan de reeds bestaande "beleidsvormen" Splitsen en Dupliceren ondersteunt QGIS nu beleid Samenvoegen, wat kan worden geconfigureerd om de initiële waarden te bepalen in het dialoogvenster Objecten samenvoegen.

Beleid kan per veld worden ingesteld in het attributenformulier van het dialoogvenster Laageigenschappen, onder het gedeelte "Beleid" van de veldconfiguratie.

Methoden voor beleid omvatten:
- Som: (Alleen numerieke velden) Som van waarden
- Gewogen geometrie: (Alleen numerieke velden) Gebruikt het gewogen gemiddelde per geometrie
- Standaardwaarde: Gebruikt de standaardwaarde die is ingesteld in QGIS
- Niet ingesteld veld: Maakt het veld leeg en gebruikt de standaardwaarde van de gegevensprovider (als die bestaat). Als er geen waarde wordt gespecificeerd, wordt de waarde uit het eerste object gebruikt (huidige standaard)
- Grootste geometrie: gebruikt de waarde van het object met de grootste geometrie (bepaald door de lengte (typen lijn), gebied (typen polygoon), aantal delen (typen multipunt))
- Minimumwaarde: (Alleen numerieke velden) Laagste waarde
- Maximumwaarde: (Alleen numerieke velden) Hoogste waarde
- Ingesteld op Null: Stelt de waarde van het veld voor het object in op NULL

<img src="images/entries/544229ddb1a9eb37b3deacd955241731f8aa4c59.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door de National Land Survey of Finland.

Deze mogelijkheid werd ontwikkeld door [Juho Ervasti](https://github.com/JuhoErvasti)
## Gegevensbeheer
### Mogelijkheid: HEIGHT_AVERAGE uit RPC gebruiken indien beschikbaar
QGIS kan nu nauwkeuriger satellietafbeeldingen positioneren, speciaal die van producten van DIMAP / Pleiades NEO.

Deze verbetering betekent dat deze typen staellietafbeeldingen zullen worden weergegeven in hun juiste geografische locatie met meer precisie, zelfs zonder aanvullende hoogtegegevens.

<img src="images/entries/6dac68ebcbe251181b8b878ca25e96bee1bf2b33" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Mogelijkheid: Aanpassen van veld toestaan bij importeren van databasetabellen
Het dialoogvenster Databasetabel importeren is uitgebreid met een nieuw gedeelte om velden te koppelen, wat de gebruiker beheer geeft over de velden in de gemaakte tabel.

Gebruikers kunnen hernoemen, het exacte type doelveld instellen en de bronexpressie aanpassen voor elk uitvoerveld.

Velden kunnen ook worden uitgesloten van importeren, of nieuwe velden worden gemaakt die niet bestaan in de brontabel.

<img src="images/entries/100dca954811ba2396b0fa2fa7edbbaec32dadb0" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optioneel bereik toevoegen, op expressie gebaseerd filter bij importeren van tabellen naar database
Wanneer een tabel via de browser wordt geïmporteerd naar een database, heeft de gebruiker nu een optie om de gekopieerde records te filteren op bereik of expressie.

<img src="images/entries/ac84f4eff2203d0b08b4577eeafa37cff09a6db1" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor opgeslagen query voor venster SQL uitvoeren
Het dialoogvenster "SQL uitvoeren" ondersteunt nu opgeslagen query's, wat de functionaliteit nabootst van Databronnen beheren in nieuwere gereedschappen voor de Browser.

Gebruikers kunnen opgeslagen query's invoegen in hun huidige query, nieuwe opgeslagen query's opslaan en query's verwijderen met een nieuwe actie op de werkbalk.

Query's kunnen worden opgeslagen in het huidige project of in het lokale gebruikersprofiel.

<img src="images/entries/b4d094f69e11aee5f1e2de7ad1ea40d3118b32fb.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: SQL-query's opslaan/laden vanuit dialoogvensters SQL uitvoeren/SQL bijwerken
Ondersteuning is toegevoegd aan de dialoogvensters SQL uitvoeren en SQL bijwerken, wat gebruikers in staat stelt om SQL-query's op te slaan en te laden naar/vanuit .sql-tekstbestanden. Dit kopieert het gedrag van de beschikbare functionaliteit in Databronnen beheren naar de op de bronbrowser gebaseerde faciliteiten voor databaseverbindingen.

De UX is ontworpen om dezelfde functionaliteit na te bootsen uit andere standaardgedeelten van QGIS, zoals de Scriptbewerker van Processing met acties op de werkbalk voor Opslaan/Laden, alsook nieuwe acties voor andere standaardbewerkingen, inclusief kopiëren, plakken, ongedaan maken en opnieuw.

<img src="images/entries/6f5e0b09c033f427fb7f9162d1b2be5a763d674c" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Toestaan dat extra token(s) van OAuth2 worden toegevoegd aan headers
Opties voor geavanceerde configuratie van OAuth2 kan nu extra tokens toevoegen die zijn verstuurd door het OAuth2-tokeneindpunt als HTTP(S)-requestheaders. Dat maakt een meer flexibele afhandeling van configuraties van OAuth mogelijk, zoals wanneer bepaalde providers OpenID-tokens toevoegen aan hun tokenantwoorden.

Deze wijziging is geïntegreerd in het beheer van inloggegevens en is beschikbaar voor alle services van OAuth2.

<img src="images/entries/2a9dadb3cfbf35b2efea8c7cd9dd4fe49ffbc292" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: (hoofd)letters van veldnaam converteren bij importeren van vectorlagen
Het dialoogvenster Vector importeren voor het migreren van vectorlagen naar databronnen ondersteunt nu de optie om automatisch alle veldnamen te transformeren naar kleine letters of hoofdletters.

<img src="images/entries/dc2c1e575d451c7bd98fb6c3b0a7cebe2800fe04" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Alleen geselecteerde objecten importeren naar databasetabel
Bij het importeren van laagobjecten in een databasetabel, maakt een nieuwe optie in het dialoogvenster het mogelijk de import te filteren op alleen de geselecteerde objecten. Deze optie is alleen beschikbaar als er een huidige selectie voor de geïmporteerde laag is.

<img src="images/entries/4a0b7ca2843d5acb9b2c3b3b2a237d6f7e55a308" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Formulieren en widgets
### Mogelijkheid: Schakelen tussen veldnamen en veldaliassen in formulieren
In lijn meth [QEP 401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md)zijn de vector Laageigenschappen geschakeld naar op model gebaseerde boomweergaven.

Dat heeft nieuwe functionaliteit ingeschakeld, inclusief de mogelijkheid om te schakelen tussen veldnamen en veldaliassen in zowel de panelen Beschikbare widgets als Formulierlay-out.

Aanvullende verbeteringen omvatten:
- Weesvelden worden geaccentueerd in de Formulierlay-out, de UX voor verbroken relaties nabootsend.
- Verbeteringen in verbroken relaties: behoud relatienamen als de relatie nog steeds beschikbaar is in relatiebeheer,

<img src="images/entries/5501d969ec51c06d6ecf49c691c484bec4d08b33.gif" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: Zoekvak toegevoegd aan Ontwerper atrributenformulier
In lijn met [QEP#401](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-401-overview-widget-types.md)bevat de Ontwerper Slepen en neerzetten nu een zoekvak om items te filteren op naam of alias, wat het veel gemakkelijker maakt om met tabellen en gegevenssets te werken die heel veel attributenvelden bevatten.

Dit filter werkt voor zowel de panelen Beschikbare widgets als voor Formulierlay-out.

<img src="images/entries/3fefddf7d32b70bf849e390847eca7904ca85ea0.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Analyse-gereedschappen
### Mogelijkheid: Invoerparameters toegevoegd aan de Toolbox in de modelontwerper
Een enkel paneel "Toolbox" is toegevoegd aan Modelontwerper, wat de objecten vanuit de panelen Invoer en Algoritme in een enkel paneel plaatst. Dat vereenvoudigt de gebruikservaring van de Modelontwerper. Geeft gebruikers de mogelijkheid om zoekfilters te gebruiken in plaats van afzonderlijke tabs voor gereedschappen van Modelontwerper te moeten beheren.

<img src="images/entries/2372c98c1724436a5d872bab22bd356ab6bae5d8.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Hauts-de-France](https://www.hautsdefrance.fr/)

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
## Processing
### Mogelijkheid: SAGA "Fill Sinks Wang & Liu" geporteerd naar eigen gereedschap
Dit veelgevraagde gereedschap leek nogal fragiel en foutgevoelig indien uitgevoerd via de plug-in SAGA voor Processing.

Een nieuw eigen gereedschap is verschaft voor een geoptimaliseerd out-of-the-box-gereedschap dat stabiel en effectief is.

Onthoud dat, omdat deze implementatie een kloon is van de implementatie van SAGA, problemen die in de bron aanwezig zijn, ook in het nieuwe eigen gereedschap zullen zitten.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Opties voor maken toegevoegd aan de gebruikersinterface van Rasterberekeningen
Opties voor het maken van een raster worden nu weergegeven in de interface van Rasterberekeningen, voor zowel het eigen dialoogvenster als in het dialoogvenster van het algoritme voor Processing.

<img src="images/entries/f95b1f5cf9163bbb300ce45564d4e1a7a0877271.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: In batch verwerken van tijdelijke uitvoer
Lagen voor tijdelijke uitvoer worden nu ondersteund in het gereedschap Batch verwerken, wat de mogelijkheid verbetert om tussenliggende databronnen te maken of experimenten meer efficiënt uit te voeren.

<img src="images/entries/6c4eab5ac90474f0d924f460586ff36b9c8df288.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Ondersteuning voor basis slepen en neerzetten in de Modelontwerper
De QGIS Modelontwerper ondersteunt nu onafhankelijke sockets die zijn verbonden met knopen van het model, die interactief kunnen worden verbonden met slepen en neerzetten.

Dat stelt gebruikers in staat om snel en gemakkelijk een uitvoer vanuit een knoop te verbinden aan een gespecificeerde invoer van een andere, zonder de individuele invoer van elke knoop te moeten configureren.

<img src="images/entries/00050aa06ae1565769944d24e26b9d938da2df6c.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Valentin Buira](https://github.com/ValentinBuira)
### Mogelijkheid: Algoritme Rang raster voor Processing
Het nieuwe algoritme "Rang raster" neemt een collectie rasters als invoer en maakt een uitvoer met celwaarden die overeenkomen met de rangorde van een lijst met celwaarden die uit de invoercollectie van de rasters komen.

Als bijvoorbeeld de lijst met invoerwaarden voor een bepaalde cel \[10,20,30,40\] is en de rang is 2, zal de uitvoerwaarde 20 zijn.

Het algoritme staat ook een negatieve indexrang toe. Gegeven dezelfde lijst met invoerwaarden, \[10,20,30,40\], en de randwaarde -2 gebruiken, zou de uitvoerwaarde 30 zijn.

Tenslotte biedt het algoritme gedrag voor het afhandelen van Geen gegevens. Standaard worden waarden Geen gegevens uitgesloten van de lijst en een opgegeven uitvoercel zal alleen worden ingesteld op Geen gegevens als de rang groter is dan de grootte van de waardenlijst. Gebruikers kunnen ook een alternatief gedrag kiezen, waar een of meer waarden Geen gegevens voor een opgegeven cel in de invoerlagen zullen resulteren in een waarde Geen gegevens voor die uitvoercel.

<img src="images/entries/8fe5df608b4c445246e6e0f4379304e062e20b88" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Opties voor toepassing en projecten
### Mogelijkheid: Projectinstelling toegevoegd voor schaalberekening, inclusief nieuwe methode "schaal op evenaar"
Een nieuwe instelling op projectniveau voor de methode voor berekening van de schaal is toegevoegd, met keuzes voor:
- aan bovenzijde van de kaart
- aan onderzijde van de kaart
- in het midden van de kaart
- horizontaal gemiddelde
- schaal op evenaar

Wijzigen van de schaal beïnvloedt heel veel systeemgedrag, inclusief:
- Nieuwe schaalbalken van lay-out zullen als standaard de berekeningsmethode van het project voor de schaal hebben
- De schaalberekeningen zullen worden aangepast, wat effecten heeft op aspecten van het project, inclusief:
  - widget voor statusbalk Kaart renderen
  - `@map_scale` en soortgelijke schaal-gerelateerde API-methoden
  - op schaal gebaseerde zichtbaarheid van lagen en symbolen
- Algoritmes van Processing die kaarten renderen, waarbij rekening wordt gehouden met de methode voor het berekenen van de schaal van het project
- Methode voor de schaal heeft effect op QGIS Server renderen van de kaart

Onthoud dat grootten van symbologie, bepaald in kaarteenheden, NIET worden beïnvloed door deze instelling.

De nieuwe "schaal op evenaar"-berekeningsmethode voor de schaal berekent altijd de schaal op de evenaar, ongeacht de feitelijke zichtbare breedtegraden in het kaartbereik. Het kan worden gebruikt om een consistente, statische schaal te verschaffen voor kaarten in geografische referentiesystemen, ongeacht de breedtegraden die fysiek zichtbaar zijn in de kaart. Onthoud dat deze methode alleen van toepassing is bij het berekenen van schalen met een op graden gebaseerd referentiesysteem.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add multiple country codes filter to Nominatim Geocoder Locator
A new optional configuration value for the Nominatim Geocoder Locator allows filtering results to one or more countries by providing a comma-separated string of the [Two-letter country codes](https://wiki.openstreetmap.org/wiki/Nominatim/Country_Codes) a user would like to restrict their results to.

<img src="images/entries/ad98e211c26bc952c65e8c84b0323c866cc293f0" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [level2](https://level2.si/)

Deze mogelijkheid werd ontwikkeld door [Uroš Preložnik](https://github.com/uprel)
## Profiel plotten
### Feature: Add support for subsections indicator
Profile plots now support the display of subsection indicators, which are rendered as vertical lines in the profile tool. This is based on outcomes from [QEP#260](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/260) and supports custom indicator symbology as well as providing subsection indicators on both the Elevation Profile view and Print Layout elements.

<img src="images/entries/4eb01abb7bde11412b39323f0dc89ac13958e050.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door BRGM

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Browser
### Feature: Port SQL Query History to Browser
The database query history panel is now displayed in the Execute SQL dialog on the browser, in line with [QEP#332](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-332-sql-query-history.md).

This adds a new top-level action to open the query history window.

<img src="images/entries/0790aa10b23a8a21663586201234bb438b88bb21.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door QGIS grant program 2025

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Improved project management for PostgreSQL stored Projects
QGIS now includes options in the browser that allow manipulating QGIS Projects stored in a PostGIS database. New functionalities include the ability to:
- Project hernoemen
- Project verwijderen
- Project dupliceren
- Move Project to Schema

<img src="images/entries/2ab1e23aae557053f6271e23db145fc791f425ee" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Show dialog when importing tables via browser and give users options to control import
A new dialog will prompt users for more comprehensive import configuration when dragging layers into data sources in the QGIS Browser, emulating functionality provided by the DB Manager Plugin for data imports.

Note that this only works when a single layer is selected, and using multiple selections will continue to execute an immediate import.

A new "Import Vector Table.." context menu item is also provided to allow importing directly from the current project layers into a target schema.

The dialog options include:
- Renaming the destination table
- Replace destination
- Set primary key
- Set geometry column
- Set destination CRS
- Set output table comment

This work entailed refactoring a number of internal architectural elements regarding the implementation of the QGIS Browser and data providers. It partly based on efforts by [@JanCaha](https://github.com/JanCaha) to port the DB Manager Postgres import functionality to the QGIS Browser.

Note that this feature does not currently support Oracle databases, due to legacy functionality leveraged by the oracle data provider.

<img src="images/entries/eedf110211aebb2acf61d89108d15ada41b616c8" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move table to another schema for PostgreSQL Provider
PostgreSQL Tables can now be moved to another schema directly in the QGIS Browser.

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Feature: Enable field rename for PostgreSQL
QGIS now supports renaming fields for PostgreSQL tables directly in the QGIS Browser interface.

Dit werd mogelijk gemaakt door Ocean Winds

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Gegevensproviders
### Feature: Add a WFS parameter for featureMode
The WFS Provider URI and UI now support a "featureMode" parameter, which supports options for :
- default (Use the server default configuration)
- SimpleFeatures (Enable simplification on returned features)
- ComplexFeatures (Disable simplification on returned features)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
### Feature: Add connection setting for restricting PostgreSQL Schema
This feature allows users to specify a single schema to limit a Postgres connection to, much like the equivalent Oracle provider setting.

When set, only tables from the matching schema will be included in the browser panel and data source select for the connection.

This can be used to limit the database work required to populate tables for a connection pointing to a large database store.

<img src="images/entries/14da725b2b420a05075ba1b09c83786bf5c839f3" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Regiodata

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add option to use POST requests for WFS connections
By default, connecting to a WFS server will be done using GET requests; however, users will now be able to switch specific WFS connections to utilize the POST HTTP method, allowing more flexibility in web service configurations.

<img src="images/entries/4a70618846a5eac6a459a0262887e3474bb1c091" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Dorset Council

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Allow SQL queries as layer sources from SQL Server
QGIS now allows loading SQL Server queries as map layers from the browser and updating the SQL for existing query layers.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## QGIS Server
### Feature: Allow configuring the server project cache size
A new `QGIS_SERVER_PROJECT_CACHE_SIZE` environment variable has been added, which allows the configuration of the QCache cost, which was previously a hardcoded value.

Deze mogelijkheid werd ontwikkeld door [Sandro Mani](https://github.com/manisandro)
### Feature: Add server properties on layer tree group
Users can now edit additional server properties on a layer tree group that will be returned in the GetCapabilities request. Available properties have been extended beyond the previous options of short name, title, and abstract to include:
- Sleutelwoorden
- Data URL (with format)
- Attribution title and URL
- URL's metadata 
- Legend URL and format (by default, one will be generated)

<img src="images/entries/41632eca99d103daf60c2d90b21ce9a543dfc53f.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Programmeerbaarheid
### Feature: Add method to convert shapely geometry to QGIS Geometry
In line with [QEP#227](This%20is%20part%20of%20https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), a new `QgsGeometry.from_shapely()` method for generating a QgsGeometry object from a shapely object has been provided to improve integration with the shapely geometry library, while keeping it an optional dependency.

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Feature: Expose QGIS GPS Tools to Python API and Plugins
The GPS tools class is now available in the PyQGIS API via a brand new `QgsAppGpsTools` class, accessed via `QgisInterface::gpsTools()`, so that plugins have more control on the QGIS GPS tracking session.

From QGIS 3.44 on, plugins can create a vector layer feature from the current GPS track, using the method `iface.gpsTools().createFeatureFromGpsTrack()`.

This also exposes additional functionalities, such as setting the GPS track line symbol by changing the corresponding setting in `QgsOptions` and updating the eventual current GPS track geometry accordingly, e.g. `iface.gpsTools().setGpsTrackLineSymbol( line_symbol )`

Dit werd mogelijk gemaakt door [de Deense Nature Agency, Naturstyrelsen](https://naturstyrelsen.dk/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| CSV Import to Geopackage ( x/y data) ignores more than 5 Mio rows | [\#60966](https://github.com/qgis/QGIS/issues/60966) | Not reproducible |  |
| OGC API: Feature Creation Request Fails When Location Header is in Lowercase | [\#61729](https://github.com/qgis/QGIS/issues/61729) | [PR \#61814](https://github.com/qgis/QGIS/pull/61814) | [PR \#61835](https://github.com/qgis/QGIS/pull/61835) |
| \[Backport 3.40\] Pick missing commits | [mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2025-May/067555.html) |  | [PR \#61843](https://github.com/qgis/QGIS/pull/61843) |
| Processing : unable to import non spatial table into PostGreSQL with OGR command with processing | [\#61655](https://github.com/qgis/QGIS/issues/61655) | [PR \#61868](https://github.com/qgis/QGIS/pull/61868) | [PR \#62023](https://github.com/qgis/QGIS/pull/62023) |
| Impossibility to save a Null value in a Interger64 field for geopackage files | [\#61787](https://github.com/qgis/QGIS/issues/61787) | can't reproduce |  |
| Error in GML handling in response to a GetFeature request in the WFS service | [\#60879](https://github.com/qgis/QGIS/issues/60879) | [PR \#61872](https://github.com/qgis/QGIS/pull/61872) | [PR \#61895](https://github.com/qgis/QGIS/pull/61895) |
| \[Tests\] Fix and unblock PyQgsLayerDefinition on QT6 |  | [PR \#61874](https://github.com/qgis/QGIS/pull/61874) | N/B |
| \[Tests\] Fix test_core_ogcutils on QT6 |  | [PR \#61876](https://github.com/qgis/QGIS/pull/61876) | N/B |
| \[Tests\] Fix PyQgsDelimitedTextProvider on QT6 |  | [PR \#61877](https://github.com/qgis/QGIS/pull/61877) | N/B |
| \[Tests\] Fix PyQgsSymbolLayerReadSld on QT6 |  | [PR \#61878](https://github.com/qgis/QGIS/pull/61878) | N/B |
| weird include paths including cmake keywords | [\#61887](https://github.com/qgis/QGIS/issues/61887) | [PR \#61894](https://github.com/qgis/QGIS/pull/61894) | N/B |
| QGIS Server GetProjectSettings doesn't output the EX_GeographicBoundingBox anymore for reverse axis projectsions | [\#61999](https://github.com/qgis/QGIS/issues/61999) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| Spilhaus not displayed complete in QGIS 3.42.1 | [\#61318](https://github.com/qgis/QGIS/issues/61318) | [PR \#62002](https://github.com/qgis/QGIS/pull/62002) | [PR \#62036](https://github.com/qgis/QGIS/pull/62036) |
| QT6 tests: fix PyQgsServerAccessControlWFSTransactional |  | [PR \#62034](https://github.com/qgis/QGIS/pull/62034) | N/B |
| OAPIF: CQL layer filter expression is not used in request | [\#60092](https://github.com/qgis/QGIS/issues/60092) | [PR \#62156](https://github.com/qgis/QGIS/pull/62156) | [PR \#62186](https://github.com/qgis/QGIS/pull/62186) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis server - Labels background get transparent based on layer transparency | [\#61801](https://github.com/qgis/QGIS/issues/61801) | Won't fix (not a bug) |  |
| Inconsistent contents in ogcapi openapi spec | [\#61848](https://github.com/qgis/QGIS/issues/61848) | [PR \#61903](https://github.com/qgis/QGIS/pull/61903) | [PR \#61922](https://github.com/qgis/QGIS/pull/61922) |
| QGIS Server does not list one layer in WMS GetCapabilities if datum transformation is used | [\#61293](https://github.com/qgis/QGIS/issues/61293) | Terugkoppeling |  |
| QGIS server 3.40.4 - Invalid cache strategy | [\#60947](https://github.com/qgis/QGIS/issues/60947) | [PR \#61907](https://github.com/qgis/QGIS/pull/61907) | N/B |
| Server LTR: OAPIF/WFS3 describe collections malfunction - empty pg layer with UTM zone SRID | [\#60686](https://github.com/qgis/QGIS/issues/60686) | can't reproduce |  |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [\#54598](https://github.com/qgis/QGIS/issues/54598) | Old issue: asked the OP and put on feedback |  |
| CGIDIR default for UNIX is wrong (bin, should be libexec/cgi-bin or at least not bin) | [\#54424](https://github.com/qgis/QGIS/issues/54424) | Old issue: asked for feedback |  |
| Performance issue on editing large PostGIS layers. | [\#61879](https://github.com/qgis/QGIS/issues/61879) | Not enough info: put on feedback and recommended to hire a consultant |  |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61912](https://github.com/qgis/QGIS/pull/61912) | Niet kritisch |
| Problems with \<NULL\> value in Value map | [\#61865](https://github.com/qgis/QGIS/issues/61865) | [PR \#61915](https://github.com/qgis/QGIS/pull/61915) | [PR \#61939](https://github.com/qgis/QGIS/pull/61939) |
| Expression constraint requires case-sensitive field names while form is open | [\#61740](https://github.com/qgis/QGIS/issues/61740) | [PR \#61928](https://github.com/qgis/QGIS/pull/61928) | [PR \#61949](https://github.com/qgis/QGIS/pull/61949) |
| JSON array attribute fields are not supported | [\#61728](https://github.com/qgis/QGIS/issues/61728) | [PR \#61938](https://github.com/qgis/QGIS/pull/61938) | Riskant |
| WMS: The parser incorrectly assumes that PositionType contains only a single space (but multiple spaces may exist) | [\#61399](https://github.com/qgis/QGIS/issues/61399) | [PR \#61963](https://github.com/qgis/QGIS/pull/61963) | [PR \#61986](https://github.com/qgis/QGIS/pull/61986) |
| Graduated classification offers date/datetime fields but does not support them | [\#61767](https://github.com/qgis/QGIS/issues/61767) | [PR \#61964](https://github.com/qgis/QGIS/pull/61964) | [PR \#61987](https://github.com/qgis/QGIS/pull/61987) |
| Advanced Digitizing: Floater not working correctly | [\#61587](https://github.com/qgis/QGIS/issues/61587) | [PR \#61979](https://github.com/qgis/QGIS/pull/61979) | [PR \#62114](https://github.com/qgis/QGIS/pull/62114) |
| QGis Server quotes html maptip | [\#61380](https://github.com/qgis/QGIS/issues/61380) | won't fix (not a bug) |  |
| Hidden coverage layer option remains active after disabling atlas generation in layout | [\#61946](https://github.com/qgis/QGIS/issues/61946) | [PR \#61993](https://github.com/qgis/QGIS/pull/61993) | [PR \#62066](https://github.com/qgis/QGIS/pull/62066) |
| Distance/area user selected unit unwanted reset in processing tools | [\#61470](https://github.com/qgis/QGIS/issues/61470) | [PR \#61997](https://github.com/qgis/QGIS/pull/61997) | [PR \#62021](https://github.com/qgis/QGIS/pull/62021) |
| PG: Can't add/update feature when numeric field with numeric default is set to default | [\#61529](https://github.com/qgis/QGIS/issues/61529) | [PR \#62010](https://github.com/qgis/QGIS/pull/62010) | Riskant |
| In Refactor Fields algorithm, field for "Source Expression" are loaded from the wrong layer when "selected features only" option is checked | [\#62019](https://github.com/qgis/QGIS/issues/62019) | [PR \#62124](https://github.com/qgis/QGIS/pull/62124) | [PR \#62235](https://github.com/qgis/QGIS/pull/62235) |
| Wrong timezone from default value when adding child feature | [\#62121](https://github.com/qgis/QGIS/issues/62121) | won't fix (not a bug) |  |
| Ellipsoidal measurement not working when the project is using a custom CRS | [\#61299](https://github.com/qgis/QGIS/issues/61299) | [PR \#62212](https://github.com/qgis/QGIS/pull/62212) | [PR \#62252](https://github.com/qgis/QGIS/pull/62252) |
| \[Processing\] "Select by Expression" doesn't works with some expressions | [\#62231](https://github.com/qgis/QGIS/issues/62231) | [PR \#62233](https://github.com/qgis/QGIS/pull/62233) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsOptions: Locale value is saved only if it is not empty | [\#52359](https://github.com/qgis/QGIS/issues/52359) | [PR \#62137](https://github.com/qgis/QGIS/pull/62137) | [PR \#62171](https://github.com/qgis/QGIS/pull/62171) |
| Extent not updated after digitizing features in a memory layer | [\#60830](https://github.com/qgis/QGIS/issues/60830) | [PR \#62159](https://github.com/qgis/QGIS/pull/62159) | [PR \#62189](https://github.com/qgis/QGIS/pull/62189) |
| Issue with the geometry combine and mergeLines | [\#61136](https://github.com/qgis/QGIS/issues/61136) | [PR \#62184](https://github.com/qgis/QGIS/pull/62184) |  |
| Atlas activation crash | [\#59610](https://github.com/qgis/QGIS/issues/59610) | [PR \#62260](https://github.com/qgis/QGIS/pull/62260) | [PR \#62288](https://github.com/qgis/QGIS/pull/62288) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Better support for SQL and virtual layers as inputs in Processing | [\#39138](https://github.com/qgis/QGIS/issues/39138) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| Using virtual layer gives error in GDAL processing algorithms | [\#59364](https://github.com/qgis/QGIS/issues/59364) | [PR \#61880](https://github.com/qgis/QGIS/pull/61880) | [PR \#61902](https://github.com/qgis/QGIS/pull/61902) |
| enable GdalAlgorithmsVectorTest on QT6 |  | [PR \#61882](https://github.com/qgis/QGIS/pull/61882) | N/B |
| fix PyQgsFloatingWidget test on Qt6 |  | [PR \#61885](https://github.com/qgis/QGIS/pull/61885) | N/B |
| fix PyQgsNetworkAccessManager test on Qt6 |  | [PR \#61886](https://github.com/qgis/QGIS/pull/61886) | N/B |
| enable QGIS algorithms tests (part 2) on Qt6 |  | [PR \#61888](https://github.com/qgis/QGIS/pull/61888) | N/B |
| Geopackage vocabulary harmonization | [\#60990](https://github.com/qgis/QGIS/issues/60990) | [PR \#61893](https://github.com/qgis/QGIS/pull/61893) | N/B |
| unbalanced QSettings.beginReadArray/endArray calls | [\#61373](https://github.com/qgis/QGIS/issues/61373) | [PR \#61904](https://github.com/qgis/QGIS/pull/61904) | [PR \#61923](https://github.com/qgis/QGIS/pull/61923) |
| Mesh styling, precision seems too small? | [\#50950](https://github.com/qgis/QGIS/issues/50950) | [PR \#61905](https://github.com/qgis/QGIS/pull/61905) | [PR \#61926](https://github.com/qgis/QGIS/pull/61926) |
| Inconsistency in PostgreSQL / PostGIS connection / layer dialog windows | [\#59886](https://github.com/qgis/QGIS/issues/59886) | [PR \#61908](https://github.com/qgis/QGIS/pull/61908) | N/B |
| Translate geometry does not create a 3D vector from 2D if deltaZ is an expression | [\#56495](https://github.com/qgis/QGIS/issues/56495) | [PR \#61906](https://github.com/qgis/QGIS/pull/61906) | [PR \#61933](https://github.com/qgis/QGIS/pull/61933) |
| After deleting the newly added XYZ layer...still exists | [\#53933](https://github.com/qgis/QGIS/issues/53933) | can't reproduce |  |
| TypeError: EnumType.**call**()... | [\#58312](https://github.com/qgis/QGIS/issues/58312) | can't reproduce |  |
| projects/anonymize\_\*\_projects doesn't affect projectMetadata.author | [\#42413](https://github.com/qgis/QGIS/issues/42413) | [PR \#61945](https://github.com/qgis/QGIS/pull/61945) | [PR \#61959](https://github.com/qgis/QGIS/pull/61959) |
| Inconsistencies in providers connection dialogs | [\#43951](https://github.com/qgis/QGIS/issues/43951) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/B |
| Source manager and WMS configuration dialog too tall | [\#60477](https://github.com/qgis/QGIS/issues/60477) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/B |
| New HTTP (WMS & friends) connection dialog too tall | [\#61867](https://github.com/qgis/QGIS/issues/61867) | [PR \#61948](https://github.com/qgis/QGIS/pull/61948) | N/B |
| duplicated objectName in the oracle dialog | niet gerapporteerd | [PR \#61944](https://github.com/qgis/QGIS/pull/61944) | N/B |
| "Save as" does not work... | [\#30130](https://github.com/qgis/QGIS/issues/30130) | [PR \#61960](https://github.com/qgis/QGIS/pull/61960) | N/B |
| Modifying project CRS...does not update coordinate CRS display | [\#61684](https://github.com/qgis/QGIS/issues/61684) | [PR \#61995](https://github.com/qgis/QGIS/pull/61995) | N/B |
| CRS selection widget not updated when project CRS changes | [\#56454](https://github.com/qgis/QGIS/issues/56454) | [PR \#61989](https://github.com/qgis/QGIS/pull/61989) | [PR \#62022](https://github.com/qgis/QGIS/pull/62022) |
| Choice for default/project styles missing... | [\#58653](https://github.com/qgis/QGIS/issues/58653) | [PR \#62012](https://github.com/qgis/QGIS/pull/62012) | N/B |
| Changing a new project's CRS does not change the annotation CRS | [\#48046](https://github.com/qgis/QGIS/issues/48046) | can't reproduce, already fixed |  |
| "editable" property misleading in JSON view | [\#47755](https://github.com/qgis/QGIS/issues/47755) | [PR \#62064](https://github.com/qgis/QGIS/pull/62064) | N/B |
| ‘Current CRS’ icon shows previous CRS | [\#53768](https://github.com/qgis/QGIS/issues/53768) | [PR \#62209](https://github.com/qgis/QGIS/pull/62209) | [PR \#62236](https://github.com/qgis/QGIS/pull/62236) |
| Crash when clicking on relation table node | [\#56481](https://github.com/qgis/QGIS/issues/56481) | can't reproduce |  |
| Documentation file grass7.txt is not up-to-date | [\#29140](https://github.com/qgis/QGIS/issues/29140) | [PR \#62210](https://github.com/qgis/QGIS/pull/62210) | N/B |
| AttributeError: 'NoneType' object has no attribute 'fields' | [\#62224](https://github.com/qgis/QGIS/issues/62224) | [PR \#62253](https://github.com/qgis/QGIS/pull/62253) | [PR \#62291](https://github.com/qgis/QGIS/pull/62291) |
| Selected field not cleared when changing layer in processing | [\#39351](https://github.com/qgis/QGIS/issues/39351) | [PR \#62241](https://github.com/qgis/QGIS/pull/62241) | [PR \#62305](https://github.com/qgis/QGIS/pull/62305) |
| pyqgis: QgsGraph | [\#56172](https://github.com/qgis/QGIS/issues/56172) | [PR \#62316](https://github.com/qgis/QGIS/pull/62316) | N/B |
| qgsidentifyresultsdialog.cpp: ‘best approach’ vs. ‘old fragile approach’ | [\#61499](https://github.com/qgis/QGIS/issues/61499) | can't reproduce |  |
| exporting to .dxf sets units to imperial inch | [\#50579](https://github.com/qgis/QGIS/issues/50579) | works for me, fixed upstream |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| STAC client connection failing | [\#62232](https://github.com/qgis/QGIS/issues/62232) | [PR \#62258](https://github.com/qgis/QGIS/pull/62258) | N/B |
| \[browser\] Inappropriate menus in Postgres connection context menu | [\#62183](https://github.com/qgis/QGIS/issues/62183) | [PR \#62270](https://github.com/qgis/QGIS/pull/62270#discussion_r2149355232) | N/B |
| QGIS master crashes when trying to use reshape features tool | [\#55859](https://github.com/qgis/QGIS/issues/55859) | [PR \#62295](https://github.com/qgis/QGIS/pull/62295) | [PR \#62326](https://github.com/qgis/QGIS/pull/62326) |
| Reshape Features can't handle resulting exclaves | [\#24884](https://github.com/qgis/QGIS/issues/24884) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Reshape tool doesn't obey 'Avoid Overlaps' when a feature is selected. | [\#61720](https://github.com/qgis/QGIS/issues/61720) | [PR \#62312](https://github.com/qgis/QGIS/pull/62312) |  |
| Fix reshaping when snapping to segment | niet gerapporteerd | [PR \#62315](https://github.com/qgis/QGIS/pull/62315) |  |
| Unhandled GEOS exception when reshaping | niet gerapporteerd | [PR \#62322](https://github.com/qgis/QGIS/pull/62322) |  |
| Reshape returns Success instead of NothingHappened | niet gerapporteerd | [PR \#62323](https://github.com/qgis/QGIS/pull/62323) | [PR \#62336](https://github.com/qgis/QGIS/pull/62336) |
| Reshape tool tries to run with a single digitized point | niet gerapporteerd | [PR \#62324](https://github.com/qgis/QGIS/pull/62324) |  |
| Fix crash when undoing first digitized point in shape map tools | niet gerapporteerd | [PR \#62335](https://github.com/qgis/QGIS/pull/62335) |  |
| Fix crashing shape tools when not enough points digitized | niet gerapporteerd | [PR \#62338](https://github.com/qgis/QGIS/pull/62338) |  |
| Crash any time I try to modify a polygon with "Enable tracing" activated. | [\#60856](https://github.com/qgis/QGIS/issues/60856) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| trace function on snap toolset causes QGIS to shutdown when initiated | [\#60978](https://github.com/qgis/QGIS/issues/60978) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Crash on vector digitizing with trace tool | [\#62163](https://github.com/qgis/QGIS/issues/62163) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| QGIS 3.40.7 Bratislava crashes every time I try to use the tracing tool to create polygons | [\#62342](https://github.com/qgis/QGIS/issues/62342) | [PR \#62345](https://github.com/qgis/QGIS/pull/62345) |  |
| Misbehavior of advanced topology settings on independant layers | Is geen probleem |  |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Germán Carrillo (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Old relations in form (after exporting layer to new file and applied old style) can't be deleted | [\#44683](https://github.com/qgis/QGIS/issues/44683) | Can't reproduce |  |
| \[Processing toolbox\] Search box (result) not updated when list of providers change | [\#26435](https://github.com/qgis/QGIS/issues/26435) | [PR \#62162](https://github.com/qgis/QGIS/pull/62162) | Nee |
| Ambiguous JSON errors | [\#42832](https://github.com/qgis/QGIS/issues/42832) | [PR \#62247](https://github.com/qgis/QGIS/pull/62247) | [PR \#62262](https://github.com/qgis/QGIS/pull/62262) |
| Disallow point layer as input to Oriented Minimum Bounding Box | [\#62126](https://github.com/qgis/QGIS/issues/62126) | [PR \#62300](https://github.com/qgis/QGIS/pull/62300) | [PR \#62330](https://github.com/qgis/QGIS/pull/62330) |
| When saving SLD to DB, make sure errors are reported to callers (like Package layers algorithm) | niet gerapporteerd | [PR \#62332](https://github.com/qgis/QGIS/pull/62332) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Mathieu Pellerin (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS fails to import sprites from OpenStreetMap vector tile styles | niet gerapporteerd | [PR \#62175](https://github.com/qgis/QGIS/pull/62175) |  |
| Menu bar not respecting set font size on qt6 build | [\#62007](https://github.com/qgis/QGIS/issues/62007) | [PR \#62086](https://github.com/qgis/QGIS/pull/62086) |  |
| QGIS Qt6 the gui to select the Profile is not well visible | [\#61557](https://github.com/qgis/QGIS/issues/61557) | [PR \#62083](https://github.com/qgis/QGIS/pull/62083) |  |
| Clip by extent prints error on console | [\#61365](https://github.com/qgis/QGIS/issues/61365) | [PR \#62075](https://github.com/qgis/QGIS/pull/62075) | [PR \#62094](https://github.com/qgis/QGIS/pull/62094) |
| QGIS freeze/is not responding, big CPU usage when setting horizontal and vertical spacing units in "point pattern fill" to "meters at scale" | [\#53550](https://github.com/qgis/QGIS/issues/53550) | [PR \#62074](https://github.com/qgis/QGIS/pull/62074) | [PR \#62106](https://github.com/qgis/QGIS/pull/62106) |
| Project translation only happening for .qgs, not .qgz | [\#61485](https://github.com/qgis/QGIS/issues/61485) | [PR \#62070](https://github.com/qgis/QGIS/pull/62070) | [PR \#62101](https://github.com/qgis/QGIS/pull/62101) |
| Stuck in pan mode when using both middle mouse and space pan in model or layout | [\#61528](https://github.com/qgis/QGIS/issues/61528) | [PR \#62069](https://github.com/qgis/QGIS/pull/62069) | [PR \#62093](https://github.com/qgis/QGIS/pull/62093) |
| Unchecking "Include Z-dimension" still includes Z when Geometry Type is Automatic | [\#61554](https://github.com/qgis/QGIS/issues/61554) | [PR \#62068](https://github.com/qgis/QGIS/pull/62068) | [PR \#62092](https://github.com/qgis/QGIS/pull/62092) |
| Label font style reverts to Regular in non_english UI (LTR, Qt5) | [\#61660](https://github.com/qgis/QGIS/issues/61660) | [PR \#62067](https://github.com/qgis/QGIS/pull/62067) | [PR \#62080](https://github.com/qgis/QGIS/pull/62080) |
| Custom shortcuts are not replacing default ones when imported from XML | [\#61717](https://github.com/qgis/QGIS/issues/61717) | [PR \#62063](https://github.com/qgis/QGIS/pull/62063) |  |
| QGIS fails to handle of source containing a relative path to the root of the server hosting the style json | niet gerapporteerd | [PR \#62062](https://github.com/qgis/QGIS/pull/62062) | [PR \#62084](https://github.com/qgis/QGIS/pull/62084) |
| Can't save layers as gpkg.zip | [\#61773](https://github.com/qgis/QGIS/issues/61773) | [PR \#62049](https://github.com/qgis/QGIS/pull/62049) | [PR \#62185](https://github.com/qgis/QGIS/pull/62185) |
| appearance input attributes box do not appear checked | [\#61994](https://github.com/qgis/QGIS/issues/61994) | [PR \#62047](https://github.com/qgis/QGIS/pull/62047) | [PR \#62056](https://github.com/qgis/QGIS/pull/62056) |
| QGIS-Locator, Behavior changed between 3.22 and 3.4x | [\#62013](https://github.com/qgis/QGIS/issues/62013) | [PR \#62043](https://github.com/qgis/QGIS/pull/62043) | [PR \#62058](https://github.com/qgis/QGIS/pull/62058) |
| Various new connection dialog spacing and size issues | niet gerapporteerd | [PR \#62041](https://github.com/qgis/QGIS/pull/62041) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin (OPENGIS)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Colours in PDF outputs appear washed out and don't render properly | [\#61674](https://github.com/qgis/QGIS/issues/61674) | [PR \#62091](https://github.com/qgis/QGIS/pull/62091) | [PR \#62107](https://github.com/qgis/QGIS/pull/62107) |
| \[Oracle\] Fix PyQgsProviderRegistry test | qt6 test failing | [PR \#62109](https://github.com/qgis/QGIS/pull/62109) | Nee |
| Model Designer - Python Converter not generating unique keys | [\#54150](https://github.com/qgis/QGIS/issues/54150) | [PR \#62261](https://github.com/qgis/QGIS/pull/62261) | [PR \#62329](https://github.com/qgis/QGIS/pull/62329) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix walk mode key handling | Niet gerapporteerd | [PR \#62331](https://github.com/qgis/QGIS/pull/62331) | N/B |
| Increase QImageReader allocation limit for qt6 builds | Niet gerapporteerd | [PR \#62320](https://github.com/qgis/QGIS/pull/62320) | N/B |
| Don't try to pass unset attributes to ArcGIS REST backends | [\#61673](https://github.com/qgis/QGIS/issues/61673) | [PR \#62061](https://github.com/qgis/QGIS/pull/62061) | [PR \#62249](https://github.com/qgis/QGIS/pull/62249) |
| Fix serious regression in boolean handling in expressions | [\#61072](https://github.com/qgis/QGIS/issues/61072) | [PR \#62217](https://github.com/qgis/QGIS/pull/62217) | [PR \#62248](https://github.com/qgis/QGIS/pull/62248) |
| Don't render effects which require rasterisation when forcing vector | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#62218](https://github.com/qgis/QGIS/pull/62218) | N/B |
| Fix categorized symbol renderer feature counts for null values | [\#52690](https://github.com/qgis/QGIS/issues/52690) | [PR \#62174](https://github.com/qgis/QGIS/pull/62174) | [PR \#62203](https://github.com/qgis/QGIS/pull/62203) |
| Try to extract only polygons from Voronoi results | [\#62158](https://github.com/qgis/QGIS/issues/62158) | [PR \#62173](https://github.com/qgis/QGIS/pull/62173) | [PR \#62194](https://github.com/qgis/QGIS/pull/62194) |
| \[processing\] Fix show feature count option, output layer ordering | [\#61146](https://github.com/qgis/QGIS/issues/61146) | [PR \#62143](https://github.com/qgis/QGIS/pull/62143) | [PR \#62172](https://github.com/qgis/QGIS/pull/62172) |
| Don't finalize string stats after every value addition | [\#62122](https://github.com/qgis/QGIS/issues/62122) | [PR \#62170](https://github.com/qgis/QGIS/pull/62170) | [PR \#62192](https://github.com/qgis/QGIS/pull/62192) |
| Fix build with SIP \>= 6.11 | [\#61951](https://github.com/qgis/QGIS/issues/61951) | [PR \#62113](https://github.com/qgis/QGIS/pull/62113) | [PR \#62142](https://github.com/qgis/QGIS/pull/62142) |
| Use protected, not private virtual methods for map tool classes | Niet gerapporteerd | [PR \#62097](https://github.com/qgis/QGIS/pull/62097) | [PR \#62112](https://github.com/qgis/QGIS/pull/62112) |
| Avoid corrupted overlapping docks when first changing from dialog to dock | Niet gerapporteerd | [PR \#62102](https://github.com/qgis/QGIS/pull/62102) | N/B |
| Fix jumpy scroll area when using mouse wheel on qt6 builds | Niet gerapporteerd | [PR \#62099](https://github.com/qgis/QGIS/pull/62099) | N/B |
| Fix comparators | [\#62045](https://github.com/qgis/QGIS/issues/62045) | [PR \#62081](https://github.com/qgis/QGIS/pull/62081) | [PR \#62118](https://github.com/qgis/QGIS/pull/62118) |
| \[processing\] Fix execution of nested models | [\#60883](https://github.com/qgis/QGIS/issues/60883) | [PR \#62079](https://github.com/qgis/QGIS/pull/62079) | [PR \#62100](https://github.com/qgis/QGIS/pull/62100) |
| Fix calculation of cost for speed strategy with null/negative values | [\#61667](https://github.com/qgis/QGIS/issues/61667) | [PR \#62044](https://github.com/qgis/QGIS/pull/62044) | [PR \#62059](https://github.com/qgis/QGIS/pull/62059) |
| Fix variables available for grid annotations missing for grid symbol | Niet gerapporteerd | [PR \#61943](https://github.com/qgis/QGIS/pull/61943) | [PR \#61957](https://github.com/qgis/QGIS/pull/61957) |
| Add new enum for rasterised rendering policy | [\#58230](https://github.com/qgis/QGIS/issues/58230) | [PR \#61942](https://github.com/qgis/QGIS/pull/61942) | N/B |
| Fix blend modes ignored when label masking is enabled | [\#43141](https://github.com/qgis/QGIS/issues/43141) | [PR \#61901](https://github.com/qgis/QGIS/pull/61901) | N/B |
| Delimited text test can be run on qt6 now | Niet gerapporteerd | [PR \#61900](https://github.com/qgis/QGIS/pull/61900) | N/B |
| Fix mesh layer labeling tests not actually run | Niet gerapporteerd | [PR \#61899](https://github.com/qgis/QGIS/pull/61899) | [PR \#61909](https://github.com/qgis/QGIS/pull/61909) |
| \[ogr\] Handle auto addition of vsizip prefix for vsicurl archives | [\#61561](https://github.com/qgis/QGIS/issues/61561) | [PR \#61854](https://github.com/qgis/QGIS/pull/61854) | [PR \#61896](https://github.com/qgis/QGIS/pull/61896) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
