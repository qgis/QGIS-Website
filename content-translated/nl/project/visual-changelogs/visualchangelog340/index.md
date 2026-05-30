---
HasBanner: false
draft: false
releaseDate: '2024-10-25'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.40
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.40{#changelog340 }
![](images/projects/83f1bc659777bc49e8e237625dfaa08f054e929c.png)

Datum uitgave: 24-10-2024

Het project QGIS is heel blij om de uitgave van QGIS 3.40 aan te kondigen. Het verfijnt de mogelijkheden op platformen, voor zowel georuimtelijke professionals als enthousiastelingen, en benadrukt de verbondenheid met zijn gebruikers met baanbrekende gereedschappen voor ruimtelijk ontdekken.

Deze uitgave bevat belangrijke stappen voor kleurbeheer, zoals beschreven in [QEP283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283). Met de introductie van ondersteuning voor CMYK-kleuren en de definitie van International Color Consortium (ICC) kleurprofielen om te gebruiken in widgets, expressies en op cartografie-georiënteerde werkstromen om te zorgen voor nauwkeurige weergave van kleuren tussen verschillende typen media.

Aanvullend heeft QGIS nu eigen integratie met [STAC](https://stacspec.org/en/) databronnen voor gemakkelijker toegang tot databronnen op afstand met de QGIS-browser. Nieuwe functionaliteit maakt het mogelijk aangepaste expressies en methoden van PyQGIS direct op te slaan binnen projectbestanden. Het verschaft gebruikers meer flexibiliteit bij het afhandelen van gegevens in hun processen. Deze functionaliteit zal ook nieuwe mogelijkheden bieden voor verbeterde automatiseringsmogelijkheden en zal zeker de productiviteit een boost geven en meer naadloze samenwerking voor teams faciliteren.

Deze uitgave bevat ook een ware rijkdom aan andere nieuwe mogelijkheden, die verbeteringen bevatten voor labelen, 3D-weergave, netwerken, attributentabellen, en nog veel meer.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=2Pk-etS1HNo).

[![](https://img.youtube.com/vi/2Pk-etS1HNo/0.jpg)](https://www.youtube.com/watch?v=2Pk-etS1HNo)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Kaartgereedschap
### Mogelijkheid: Verticale datum in laag/project respecteren in Identificatieresultaten
Wanneer een vectorlaag en het project verticale datums hebben, en ze verschillen, neem dan ook de getransformeerde waarde Z voor de geïdentificeerde objecten op in de datum van het project.

![](images/entries/2249cc72d87c0b0542213451037df8bbefbad6ba.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Verwijzingsrelaties presenteren in gereedschap Info
In eerdere uitgaven van QGIS werden alleen relaties waarnaar verwezen werd (gerelateerde objecten waarnaar het huidige object verwijst) gepresenteerd aan gebruikers bij het verkennen van een object met het gereedschap Info. Ondersteuning voor het presenteren van verwijzingsrelaties (gerelateerde objecten waarvandaan het huidige object wordt aangewezen), en ze worden nu ondersteund op een willekeurig niveau van nesten.

In aanvulling daarop zijn meerdere bijwerkingen aan de afhandeling van gerelateerde objecten in het gereedschap Objecten identificeren toegevoegd, inclusief:
- voorkomen van duplicate relatieverwijzingen
- alleen relaties laden bij het uitvouwen van een knoop (wat een 'explosie' van het laden van gerelateerde verwijzingen voorkomt)
- schakelen beheren om relatieverwijzingen in- of uit te schakelen
- een contextmenu-item voor "Object identificeren" om een genest gerelateerd object naar de bron van de context van het gereedschap Objecten identificeren te laden

![](images/entries/c9580e44b7f4f2ec945843c468b661ded749b8a5.webp)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
## Gebruikersinterface
### Mogelijkheid: Optioneel standaard de grootte van alle kolommen aanpassen bij het openen van een attributentabel
Een nieuwe optie op de tab Databronnen van het dialoogvenster Opties (geopend via het menu Extra) zal QGIS configureren om altijd de kolommen van een attributentabel aan te passen om de inhoud te laten passen wanneer die wordt geopend.

![](images/entries/eb2cc3cadf1ebb453de585e564fb0a56ff1c6ccf.gif)

Deze mogelijkheid werd ontwikkeld door [Ben Wirf](https://github.com/benwirf)
### Mogelijkheid: Dialoogvenster Acties, knop Dupliceren
Een knop Dupliceren actie is toegevoegd aan het dialoogvenster Acties in Laageigenschappen.

![](images/entries/6f0479c9233e8193625e98494da97029a6d0d30b.webp)

Deze mogelijkheid werd ontwikkeld door [Speedrace4](https://github.com/Speedrace4)
## Symbologie
### Mogelijkheid: Stijlcategorieën verschaffen voor rasterlagen
QGIS ondersteunt nu categorieën voor het kopiëren van eigenschappen en stijlen tussen rasterlagen (in plaats van eenvoudig het gebruik af te dwingen van `AllStyleCategories` zoals eerder), en bevat nu categorieën voor rastergegevens, voor:
- `Configuratie van laag`
- `Eigenschappen van Tijdbeheer`
- `Eigenschappen hoogte`
- `Kaarttips`
- `Opmerkingen`
- `Aangepaste eigenschappen`
- `Symbologie`
- `Renderen`

In aanvulling hierop worden deze stijlen ondersteund in de functionaliteiten voor importeren en exporteren van de QML/SLD-laagdefinitie- en stijlbestanden wat het beheren van rasterlagen meer consistent maakt met de gebruikservaring voor vectorlagen.

![](images/entries/0a6aeadd40690988d3560966b673045e568f86a7.webp)

Dit werd mogelijk gemaakt door het [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Dave Signer (OPENGIS.ch)](https://opengis.ch)
### Mogelijkheid: Type symboollaag "Lineaire verwijzing" toegevoegd
Dit nieuwe type symboollaag maakt het mogelijk tekstlabels langs een lijn te plaatsen met regelmatige intervallen (of op posities die overeenkomen met bestaande punten). Posities kunnen worden berekend met cartesiaanse afstanden, of geïnterpoleerd uit waarden Z/M.

Functionaliteit omvat:
- Labels kunnen worden geplaatst met vaste cartesiaanse 2D-afstanden, op regelmatige lineair geïnterpoleerde afstand die wordt berekend met de waarden Z of M in geometrieën, of op bestaande punten
- Labels kunnen de totale lopende afstand weergeven of de lineair geïnterpoleerde waarde Z/M
- Gebruikt tekstrenderer om labels te tekenen, dus het volledige bereik aan functionaliteit is beschikbaar voor de labels (inclusief buffers, schaduw, etc.)
- Gebruikt de klassen voor numerieke indeling van QGIS om getallen op te maken als tekenreeksen. Gebruikers hebben dus het volledige bereik aan opties voor aanpassingen, bijv.  voor decimale plaatsen
- Een optionele instelling "Veelvouden overslaan van". Indien ingesteld, worden labels waarvan de waarde een veelvoud van deze waarde is, overgeslagen. Dit maakt het mogelijk complexe labels voor verwijzingen te maken. Bijvoorbeeld waar een symbool twee symboollagen Lineaire verwijzing heeft, een ingesteld om elke 100 m te labelen in een klein lettertype, veelvouden van 1000 over te slaan, en een tweede ingesteld om elke 1000 m te labelen in een groot vet lettertype
- Labels worden gerenderd met een hoek die wordt berekend door de lijn te middelen, dus scherpe, dunne rafels resulteren niet in lelijk roteren van labels
- Optioneel kunnen markeringen worden geplaatst op verwezen punten op de lijn, met een volledig markeringssymbool van QGIS (dat maakt bijvoorbeeld het weergeven van een kruisarcering op het gelabelde punt mogelijk, voor een lijn in de stijl van een "liniaal")
- Data-bepaald beheer over de intervallen voor plaatsen, instellingen voor overslaan van veelvouden, zichtbaarheid van markeringen en lengte van de berekening voor gemiddelde hoek

Opmerkingen:
- Bij het gebruiken van op afstand gebaseerde plaatsing van labels, worden de afstanden alleen berekend met 2D, cartesiaanse berekeningen gebaseerd op het originele laag-CRS. Dit zou in de toekomst uitgebreid kunnen worden om opties weer te geven voor 3D cartesiaanse afstanden, of ellipsoïde afstandsberekeningen.

![](images/entries/ac3d8027aaa1dce55a600831bbe0a51d890f9206.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/de/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Interpoleren van kleurenbalk voor CMYK geïmplementeerd 
Dit werd mogelijk gemaakt door Bordeaux Métropôle

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Voorbeeld voor CMYK-kleur
Kleurvoorbeelden van CMYK-kleuren zullen de kleurwaarde weergeven met een lijst van waarden float

![](images/entries/bf96aab2e61c942bc43fbdab4f00d3f90ad5818d.webp)

Dit werd mogelijk gemaakt door Métropôle de Bordeaux

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Kleurcomponent selecteren als float
De QGIS-widget Kleur ondersteunt nu het selecteren van de kleurcomponent als een waarde float met 2 decimalen

![](images/entries/ac91b68a5cbaf6376aa12091077f7b5133d2049b.webp)

Dit werd mogelijk gemaakt door Bordeaux Métropôle

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Markeringssymbolen voor eindpunt toestaan voor stijl Tekstballon
Maakt het renderen van een markeringssymbool onder het eindpunt van de tekstballon mogelijk. Ontworpen om tekstballonnen in staat te stellen hetzelfde visuele uiterlijk te reproduceren als de oudere items van het annotatieframework.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Buffers voor markeringssymbolen
QGIS bevat nu "buffers" voor markeringssymbolen. Net als buffers voor labels hebben buffers voor markeringen een halo-effect rondom markeringssymbolen. Ontworpen om het symbool beter leesbaar te maken tegen verschillende achtergronden.

Buffers worden gedefinieerd op het niveau van een symbool (niet per symboollaag), en worden berekend en getekend met de vorm van ALLE symboollagen in de markering. Dat maakt ze supergemakkelijk te configureren, omdat hetzelfde resultaat met de hand verkrijgen heel veel kopieën van symboollagen en gekopieerde instellingen daartussen zouden vereisen!

Deze wijziging is ontworpen om een van de (zeer weinige!) grote symbologiegaten te dichten tussen ArcMap en QGIS, waar ArcMap al sinds decennia ondersteuning had voor effen kleurmarkeringen "halos".

![](images/entries/391b7def075a5dcdc026d0e625bb3f6483bc580a.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning van toleranties voor  pixelwaarden van QgsRasterTransparency
Staat toe dat pixels met kleurcomponenten net buiten de gespecificeerde waarden RGB, ook worden behandeld als transparante pixels

Nuttig voor foto's of gecomprimeerde rasters waar een bereik van kleurwaarden transparant moet worden gemaakt.

![](images/entries/73a7b62e6c22c27056a35c9d827f8ac3955f7b57.webp)

Dit werd mogelijk gemaakt door [Middle Third Geological](https://www.linkedin.com/in/deryk-forster-44a415104/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Annotaties
### Mogelijkheid: Automatisch upgraden SVG en tekstannotaties naar items van de annotatielaag bij laden project
We verbeterden de werkstroom voor deze projecten met oudere items voor annotaties. In eerdere versies van QGIS werden oudere items voor annotaties (tekst, HTML, SVG en formulier) niet geporteerd naar het nieuwe framework en hadden daarom invloed op werkstromen. In 3.40 hebben we ons gericht op de items met hogere prioriteit, tekst en SVG, dus nu is het framework bijgewerkt en is de ontbrekende functionaliteit toegevoegd. Nu, bij het laden van oude projecten, zullen alle oude SVG- en tekstannotaties automatisch worden geconverteerd (stilletjes) naar de nieuwere typen annotatieitem afbeelding en rechthoekige tekst.
- Gedurende die tijd werden verscheidene problemen opgelost en werden deze aanvullende functies toegevoegd:
- Tekstballonnen voor annotaties, inclusief tekst op punt, rechthoekige tekst en afbeeldingsannotaties.
- Markeringssymbool te tekenen als deel van de “ballon” tekstballonstijl
- Geassocieerde “zichtbaarheidslaag” voor annotaties
- Rijk widget tekstbewerken om het interactief maken van HTML-inhoud mogelijk te maken voor tekst op punt en rechthoekige tekst
- Gebruikersinterface opgeruimd

Dit werd mogelijk gemaakt door [QGIS Grant Programme 2024](https://github.com/qgis/PSC/issues/60)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning toegevoegd voor tekstballonnen voor items tekst naar punt, rechthoekige tekst en afbeelding
Maakt het mogelijk regels voor tekstballonnen te maken (of bubbeltekstballonnen) die tekst koppelen aan een locatie op de kaart. Gebruikers selecteren om een tekstballon te maken het tekstitem en slepen dan aan de centrale X-knoop naar het gewenste eindpunt van de tekstballon.

Stijlen voor tekstballonnen kunnen worden aangepast via het paneel Laag opmaken.

![](images/entries/87e3c18cbb4eb5bdb2ee4a2a690ffbb1f6ae2bde.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Optie gekoppelde laag toegevoegd voor annotatielagen
In lijn met [QEP\#269](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/269) is een nieuwe instelling "Gekoppelde laag" toegevoegd aan de renderpagina voor annotatielagen. Dat geeft gebruikers de mogelijkheid om optioneel een gekoppelde zichtbaarheidslaag voor de annotatielaag in te stellen. Indien ingesteld, zullen de annotaties alleen worden getekend als de gekoppelde laag zichtbaar is op de kaart.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Type item afbeeldingsannotatie toegevoegd
Kan SVG- of rasterafbeeldingen renderen als items in een annotatielaag. Opties zijn beschikbaar voor:
- Vergrendelen van de verhoudingen van de afbeelding
- Tekenen met een achtergrondsymbool
- Tekenen met een randsymbool
- Gekoppelde of ingebedde afbeeldingen
- Renderen met schaalafhankelijke grootten of vaste grootten

![](images/entries/14d168314617843058d4cfe38b8c15abb96114b4.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Labelen
### Mogelijkheid: Ondersteuning voor horizontale uitlijning in HTML-labels
Voor labels met meerdere regels maakt dit het gebruiken mogelijk van ofwel:
- HTML-attributen
- CSS "text-align: xxx"
- enkele HTML-tekst tags

Ondersteunt uitlijnen voor links, rechts gecentreerd en uitgevuld

Horizontaal uitlijnen kan worden gebruikt in elke context waar HTML-tekst wordt gerenderd, BEHALVE voor gebogen labels (omdat die zijn beperkt tot een regel tekst)

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Opmaak HTML-header in HTML-labels
Ondersteuning voor tags voor headers (h1/h2/…/h6) en geassocieerde opmaak in HTML-labels wordt nu ondersteund.

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor CSS voor tussenruimte tussen woorden toegevoegd in HTML-labels
Ondersteuning voor CSS voor tussenruimte tussen woorden in HTML-labels en op andere plaatsen waar HTML-tekstopmaak wordt geaccepteerd is toegevoegd aan QGIS, wat het mogelijk maakt CSS-regels te gebruiken, zoals "word-spacing: 12" om de ruimte tussen woorden in een gedeelte HTML-tekst te vergroten. De tussenruimte voor woorden wordt altijd behandeld alsof die in eenheden punt is.

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Implementatie van regels voor labelen
In lijn met [QEP\#299](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/299) is een nieuw API-framework geïmplementeerd voor het instellen van gevorderde regels voor labelen in een project, en implementeert 4 initiële typen regels:
- QgsLabelingEngineRuleMinimumDistanceLabelToFeature: voorkomt dat labels te *dichtbij* objecten uit een andere laag worden geplaatst
- QgsLabelingEngineRuleMaximumDistanceLabelToFeature: voorkomt dat labels te *ver* van objecten uit een andere laag worden geplaatst
- QgsLabelingEngineRuleMinimumDistanceLabelToLabel: voorkomt dat labels te dichtbij objecten uit een andere laag worden geplaatst
- QgsLabelingEngineRuleAvoidLabelOverlapWithFeature: voorkomt dat labels zo worden geplaatst dat ze objecten uit een andere laag overlappen 

Onthoud dat de eerste 3 regels een bouw vereisen die is gebaseerd op GEOS &gt;= 3.10, en dat ze niet beschikbaar zijn voor oudere bouwsels.

Ook is een register geïmplementeerd voor het opslaan van beschikbare klassen voor regels, en serialisatie van regels en configuratie in projecten van QGIS.

![](images/entries/f65ac82ccaa14f9017904db8badb25afc6e87bc5.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor tags img in HTML-labeltekst
Maakt het gebruik mogelijk van tags img in HTML-labelinhoud. De volgende logica wordt toegepast:
- Pad naar afbeelding wordt ingesteld via het attribuut src="xxx". Lokale, HTTP en met base64 gecodeerde paden zijn toegestaan
- Elke door QGIS te lezen afbeeldingsindeling mag worden gebruikt
- Afbeeldingsgroottes kunnen worden gespecificeerd met de attributen width="\#\#" en height="\#\#". Als width of height niet wordt gespecificeerd, dan zal die automatisch worden berekend uit de grootte van de originele afbeelding
- Als width of height zijn gespecificeerd, worden ze geacht in PUNT te zijn
- Met de instellingen voor CSS width/height wordt GEEN rekening gehouden (dit is een beperking van Qt)
- Afbeeldingen worden niet ondersteund voor gebogen tekstlabels
- Afbeeldingen worden alleen op de regel geplaatst; zwevende afbeeldingen worden niet ondersteund

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Diagrammen
### Mogelijkheid: Introduceren van gestapelde diagrammen
Gestapelde diagrammen geven een methode voor het structureren van meerdere aanliggende (horizontale of verticale) gestapelde "Subdiagrammen" voor een enkel object, wat een methode verschaft voor het maken van complexe diagramobjecten, zoals bevolkingspyramiden.

De implementatie introduceert meerdere nieuwe instellingen voor het configureren van diagram en subdiagram, en heeft het modale dialoogvenster voor instellingen van het diagram gemigreerd naar de dockwidget Laag opmaken.

![](images/entries/798c8f7ffe9acd928e7df5820212b39f22ef42fd.webp)

Dit werd mogelijk gemaakt door [Landesamt für Vermessung und Geoinformation (LVG) Vorarlberg in samenwerking met de Zwitserse QGIS gebruikersgroep.](https://vorarlberg.at/-/landesamt-fuer-vermessung-und-geoinformation-l-1)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Mazen
### Mogelijkheid: Gebruikersinterface toegevoegd voor Gekwantiseerde lagen met mazen
Nieuwe elementen voor de gebruikersinterface worden verschaft om databronnen en lagen voor Gekwantiseerde lagen met mazen in het paneel QGIS Browser te laden, alsook in Databronnen beheren.

![](images/entries/9873b9077c396a54266bed908c8b68a46e5ecd5c.webp)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [David Koňařík](https://github.com/dvdkon)
## Renderen
### Mogelijkheid: Meerdere bronnen ondersteunen voor vectortegels
De mogelijkheden voor QGIS zijn uitgebreid voor het laden van vectortegels die meerdere bronnen/URL's bevatten binnen een enkele stijldefinitie.

![](images/entries/c52b6dfb4751aed9c39b719d8d4c44c3eaec3a32.webp)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
## 3D-objecten
### Mogelijkheid: Instellingen voor verticaal CRS in vectorlaag respecteren in 3D-kaartweergaven
Met het geconfigureerde verticale CRS op het laagniveau zal rekening  gehouden in 3D-kaartweergaven, vooropgesteld dat het project een niet-geografisch 2D-CRS heeft ingesteld en dat een verticaal CRS is ingesteld.

Onthoud dat dit slechts invloed zal hebben op nieuw gemaakte 3D-kaartweergaven en momenteel wordt er geen instelling voor de gebruikers weergegeven om het CRS voor bestaande 3D-kaartweergaven aan te passen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Afstand voor clippen 3D-scène
Een nieuwe optie voor het instellen van `gl_clipistance` voor 3D-weergaven zal van toepassing zijnde objectpunten filteren die vallen buiten het opgegeven bereik, effectief de weergave bijsnijden in meerdere vlakken.

Deze instelling wordt beheerd met de methoden `enableClipping()` en `disableClipping()` op objecten `Qgs3DMapScene`.

![](images/entries/4ec6126f373e56755809edbabc74b0cd5a5ee160.webp)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Afdruklay-outs
### Mogelijkheid: Ondersteuning toegevoegd voor samenvoegen van cellen in handmatige tabellen
Staat toe dat aanliggende cellen worden samengevoegd in de lay-outitems van handmatige tabellen.

Vanuit de tabelbewerker, selecteer meerdere cellen in een rechthoekige vorm en dan, vanuit het menu Tabel, klik op "Geselecteerde cellen samenvoegen". Samengevoegde cellen kunnen van elkaar worden losgemaakt met de menuactie "Geselecteerde cellen splitsen".

![](images/entries/12309cc445c6d00d56ef0f724be0828bb3e094d0.webp)

Dit werd mogelijk gemaakt door FLYGHT7

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Geldige PDF/X-4-bestanden maken
In lijn met [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) zal QGIS een geldig bestand PDF/X-4 maken als de kleurruimte is ingesteld

Dit werd mogelijk gemaakt door Bordeaux Métropôle

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Optie toegevoegd om groepsnaam voor items van georuimtelijke PDF in te stellen
Deze nieuwe instelling, geplaatst in het gedeelte "Renderen" van het lay-outitem, stelt gebruikers in staat een optionele "groepsnaam" in te stellen om te gebruiken bij het exporteren naar georuimtelijke PDF. Indien ingesteld, zal een overeenkomende groep in de boom met lagen worden gemaakt in de geëxporteerde georuimtelijke PDF en het item zal alleen zichtbaar zijn als deze groep is geselecteerd.

Dit maakt het mogelijk dat inhoud selectief als een groep wordt weergegeven voor lezers van de georuimtelijke PDF. Het kan bijvoorbeeld extra lay-outinhoud mogelijk maken, zoals beschrijvende labels of legenda's, om alleen te worden weergegeven als lagen van de groep zichtbaar zijn. Wat exporteren naar een georuimtelijke PDF veel flexibeler maakt.

![](images/entries/a0f64c99c2a62dee9681d01dec7a39d991377a85.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Pagina-eigenschappen toegevoegd aan het hoofdmenu van Lay-out
Een menuoptie om de Pagina-eigenschappen te openen is toegevoegd aan het hoofdmenu in de interface voor Afdruklay-out.

![](images/entries/44407afcb40294680e8aad845bb2cf0060cfe034.webp)

Deze mogelijkheid werd ontwikkeld door [Vedran Stojnović](https://github.com/phidrho)
### Mogelijkheid: Optie voor methode Schalen voor schaalbalken in lay-outs
Een nieuwe optie voor het selecteren van een gebruikergedefinieerde methode voor het berekenen van de kaartschaal voor afdruklay-outs wordt verschaft. Dit geeft opties weer voor berekenen van de schaal:
- langs de onderzijde van het kaartframe
- langs het midden van het kaartframe
- langs de bovenzijde van het kaartframe
- als een gemiddelde van alle drie metingen

Standaard zullen de nieuwe schaalbalken de gemiddelde methode gebruiken (in plaats van de eerder gebruikte methode "langs onderzijde"), die beter scenario's afhandelt waarbij de schaal aan de boven- of onderzijde van de kaart niet kan worden berekend (bijv. wanneer de boven- of onderzijde van de kaart buiten geldige gebieden voor het kaart-CRS valt).

![](images/entries/ff809eacb3e8701d38d43292ae3d5694cb16076d.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Mogelijkheid: Numerieke indeling 'Gebruikerexpressie' toegevoegd
Deze numerieke indeling stelt gebruikers in staat een aangepaste expressie voor QGIS te maken om getallen op te maken. De expressie mag de variabele @value gebruiken om de op te maken waarde op te halen, en dan elke standaardfunctie voor een expressie van QGIS gebruiken om die op te maken zoals wordt gewenst.

Het kan overal worden gebruikt waar QgsNumericFormat wordt geaccepteerd, zoals lay-out van schaalbalken, hoogteplots, lay-out voor tabellen en legenda's voor kleurenbalken

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Expressies line\_interpolate\_point\_by\_m en line\_locate\_m toegevoegd
Twee nieuwe functies worden verschaft voor expressies om te werken met waarden M langs lijnen:
- `line_interpolate_point_by_m`: geeft een geometrie punt terug voor een overeenkomende waarde M, geïnterpoleerd langs een lijn die een dimensie M heeft.
- `line_locate_m`: geeft een afstand terug vanaf het begin van een lijn waar een overeenkomende waard M werd gevonden.

Deze functies zijn nuttig bij het werken met tijdgegevens (zoals een lijn die een GPS-spoor weergeeft, waar de waarde M de waarde epoch weergeeft), en kan effectief naast Tijdbeheer worden gebruikt om prachtige animaties te maken die eerder moeilijk te ontgrendelen waren.

![](images/entries/43d4feab4f7d4fb0fe167c7120b19a7cae13fc47.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Ondersteuning voor uitgebreide kleurwaarde
In lijn met [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) staan nieuwe expressiefuncties het ophalen van kleuren toe die bevatten:
- color\_rgbf
- color\_cmykf
- color\_hsvf
- color\_hslf

Deze functies verschillen van de expressiefuncties voor het ophalen van kleuren (bijv. color\_rgb) door kleurwaarden terug te geven met verschillende interne gegevenstypen. Dat verbetert de prestaties en de getrouwheid door onnodige kleurconversies te vermijden in specifieke contexten, zoals het schrijven van pdf's met eigen CMYK-kleuren die zijn afgeleid van expressiewaarden.

Dit werd mogelijk gemaakt door Bordeaux Métropôle

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Gebruikers toestaan expressiefuncties op te slaan in QGIS projectbestand
Een nieuw element `[Project Functions]` is nu beschikbaar binnen het dialoogvenster Expressiebouwer, dat QGIS in staat stelt om aangepaste gebruikergedefinieerde functies, ingebed in het projectbestand, op te slaan.

Dat verkleint de noodzaak om handmatig snippers van Pythoncode te moeten delen en ze te kopiëren naar de map voor het gebruikersprofiel of ze in het dialoogvenster Expressiebouwer te importeren.

Projectfuncties worden ontladen als een project wordt gesloten en gebruikerfuncties worden opnieuw geladen om eventueel potentieel overschrijven bij geactiveerde projectfuncties te vermijden.

Om beveiligingsredenen is de afhandeling voor het laden of niet laden van deze functies bij het opstarten van het project te configureren in de gebruikersinstellingen. Met dezelfde rationale als die welke wordt gebruikt voor het beheren van projectmacro's.

![](images/entries/fb459ca9362a65771713ed9b571b12a265e0b45d.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: Info toegevoegd over bruikbare "dialect voor expressie" in het dialoogvenster Filteren
De Querybouwer die wordt gebruikt voor het invoeren van expressies om te filteren op vectorlagen geeft nu het ondersteunde dialect voor de expressie weer.

![](images/entries/1bd0096fbd0fac4d612b2ca98bc7ef86cedac36e.webp)

Dit werd mogelijk gemaakt door WhereGroup GmbH.

Deze mogelijkheid werd ontwikkeld door [Hannes](https://github.com/kannes)
### Mogelijkheid: Functies project\_color\_object en ramp\_color\_object toegevoegd
In lijn with [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283) verschaffen nieuwe expressiefuncties ondersteuning bij het instellen van projectkleuren en kleuren voor balken met CMYK-kleurwaarden door expressies te gebruiken

Dit werd mogelijk gemaakt door Bordeaux Metropole

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Digitaliseren
### Mogelijkheid: Gereedschap voor digitaliseren kruising van cirkels toegevoegd
Een nieuw gereedschap voor Digitaliseren stelt gebruikers in staat een punt te kiezen/digitaliseren op de kruising van twee cirkels

De QGIS API is, om deze functionaliteit te kunnen ondersteunen, uitgebreid met een nieuwe klasse abstract voor het ondersteunen van soortgelijke ontwikkeling van "COGO" in de toekomst. Alsook voor het verschaffen van bindingen voor Python voor het ontwikkelen van mogelijkheden en plug-ins voor geavanceerd digitaliseren.

![](images/entries/990ee4bd78f0d0732ca02562ce953bed4c9443a8.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Visuele constructielijnen voor Geavanceerd digitaliseren
Visuele constructielijnen zijn toegevoegd aan de dockwidget Geavanceerd digitaliseren, dat doorbouwt op de bestaande constructiemodus voor CAD.

Bij het opnemen van constructielijnen zal QGIS alle stappen voor de constructie renderen als streepjeslijnen, die zichtbaar blijven zolang Geavanceerd digitaliseren is ingeschakeld. De hulplijnen kunnen snappen, wat het mogelijk maakt constructiestappen ook te beginnen halverwege een eerdere set stappen.

De constructielijnen worden opgeslagen in een vectorlaag, die wordt weergegeven door de dockwidget Geavanceerd digitaliseren, wat verdere aanpassing van de lijnen via andere toepassingsprocessen, zoals plug-ins van Python, mogelijk maakt.

![](images/entries/d77759a3bc23a050b3e8e9cc5a5d3bb5cc91dff3.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Gegevensbeheer
### Mogelijkheid: Sta instellen van inloggegevens VSI toe bij het laden van lagen van OGR/GDAL
Opties voor inloggegevens voor VSI worden nu weergegeven voor gebruikersbeheer bij het toevoegen van OGR-vector-/GDAL-rasterlagen vanuit Databronnen beheren. Dat geeft gebruikers de mogelijkheid inloggegevens te definiëren op een per-laag-basis voor lagen die worden opgehaald uit cloudservices (in plaats van een enkele set inloggegevens te gebruiken voor de gehele sessie van QGIS met een omgevingsvariabele of soortgelijke benadering).

Vereist GDAL 3.5+

![](images/entries/e824e2a5aef50de87656d6beced8ea0ae0f60e41.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Formulieren en widgets
### Mogelijkheid: Opnieuw ordenen van velden toestaan in nieuwe dialoogvensters voor vectorlagen
Bij het maken van een nieuwe vectorlaag, inclusief tijdelijke tekenlagen, shp, gpkg en SpatiaLite, zullen gebruikers nu in staat zijn de velddefinities opnieuw te ordenen.

![](images/entries/3623fff590c84705c9e75fa22c3e0cc9c537c9e0.webp)

Dit werd mogelijk gemaakt door Deense QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Metadata instelling toegevoegd om widgetwrapper, die wordt gebruikt voor een parameter, te overschrijven
Waar het mogelijk was nieuwe widgetwrappers toe te voegen voor parameters van Processing, was het niet mogelijk om de standaardwidgetwrappers te overschrijven die waren gedefinieerd voor elk type parameter.

Een nieuwe instelling voor de metadata van de parameter voor "widget\_type" is toegevoegd, die ontwikkelaars in staat stelt de standaardwidgetwrapper voor een parameter te overschrijven voor meer beheer van dialoogvensters voor de toepassing.

`param.setMetadata( } )`

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
## Processing
### Mogelijkheid: Algoritme Bestand of URL openen 
Een eenvoudig eigen algoritme is toegevoegd dat het mogelijk maakt lokale bestanden te openen met de corresponderende systeemprogramma's, of URL's in een webbrowser.

Nuttig in combinatie met het algoritme Bestand downloaden via HTTP(S) om het resulterende bestand te openen, of om resultaten weer te geven nadat modellen externe systemen activeren.

![](images/entries/2ab9a02e47e9d3dc7a0c4e1dc5f65d195244869b.webp)

Dit werd mogelijk gemaakt door het [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Dave Signer (OPENGIS.ch)](https://opengis.ch)
### Mogelijkheid: Typen parameters toegevoegd in Processing voor Area en Volume
Voegt aangewezen typen parameters voor waarden van Area en Volume toe.

Nauw gemodelleerd naar het bestaande type parameter Distance.

![](images/entries/8324f615ac89f6d617619f34f6cc37ee2ae55a2a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Bijgewerkte algoritmes "Vectorinformatie"
Het GDAL-algoritme voor Processing voor vectorinformatie is aangepast om aanvullende parameters voor de opdrachtregel te ondersteunen, en een nieuw algoritme **Vectorinformatie (JSON)** wordt verschaft. Dat zal de optie [`-json`](https://gdal.org/programs/ogrinfo.html#cmdoption-ogrinfo-json) van ogrinfo gebruiken om een JSON uitvoerbestand te maken dat de informatie over de laag of gegevensset bevat.

![](images/entries/b890a9ff0af7e1ef313c620c48150f871f1177f0.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Mogelijkheid: Toevoegen van gereedschappen van Processing aan Favorieten toestaan
Nieuwe functionaliteit voor 'Favorieten' is toegevoegd voor algoritmes van Processing. Die stelt gebruikers in staat om de door hen gekozen algoritmes statisch vast te zetten in een aangewezen gedeelte aan de bovenzijde van de Toolbox, voor gemakkelijke toegang.

![](images/entries/2108d8a4104ef9d50f44a72171274469bde1e429.webp)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Ondersteuning voor opties voor maken toegevoegd aan sommige eigen algoritmes van Processing voor rasters
Meer opties voor het maken van rasters zijn toegevoegd aan eigen algoritmes van Processing voor meer beheer over de indeling van de uitvoer (compressieniveau, maken van world file, etc.). Betrokken algoritmes omvatten:
- Celstatistieken
- Constante rasterlaag maken
- Mazen exporteren
- 'Geen gegevens' vullen
- Raster onscherp maken 
- Dichtheid lijn
- Willekeurig raster
- DTM-filter (gebaseerd op helling)
- Gelijk aan frequentie
- Raster booleaanse waarde EN/OF
- Positie in stapel van raster 
- Opnieuw classificeren
- Raster opnieuw op schaal brengen
- Rond

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Ondersteuning voor slepen-en-neerzetten voor parameters voor meerdere lagen
Maakt het mogelijk lagen te slepen en neer te zetten vanuit ofwel de QGIS Browser of bestandsverkenner in elk paneel voor parameters voor meerdere lagen. Handig als u veel lagen moet toevoegen en het eenvoudiger is een selectie te maken buiten het dialoogvenster van Processing.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Opties voor toepassing en projecten
### Mogelijkheid: Implementatie van slimme cachegrootte
QGIS heeft nu verbeterde afhandeling van zijn netwerkschijfcache door het ophogen van de logica voor de slimme cachegrootte die momenteel wordt gebruikt door moderne webbrowsers.

Dat maakt het mogelijk dat de cache dynamisch wordt aangepast, gebaseerd op beschikbare opslagruimte op de cacheschijf, en zal erin resulteren dat de meeste gebruikers standaard een hogere cachegrootte krijgen (en verbeterde netwerkprestaties), alsook laden beperken naar externe providers en XYZ-tegelservices.

Gebruikers kunnen de logica voor de slimme cachegrootte uitschakelen voor een statische cachegrootte met het bijgewerkte dialoogvenster Opties.

![](images/entries/80e1931b0152bfe035105520396a775b6f9bfbaf.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Selectiewidget voor verticaal CRS toegevoegd aan eigenschappen vectorlaag
Vectorlagen mogen nu afzonderlijke instellingen bevatten voor het configureren van een verticaal referentiesysteem.

Gedrag van de toepassing voor het definiëren van verticale referentie op een laag zal hetzelfde gedrag volgen als de projectinstellingen, namelijk:
- Als de laag een 3D-CRS heeft ingesteld, dan is de widget uitgeschakeld met een opmerking die uitleg geeft
- Als de laag een 2D-CRS heeft ingesteld, dan kan de gebruiker het toepasselijke verticale CRS selecteren

Een opmerking met uitleg wordt opgenomen die de facetten van de toepassing uitlegt, waarbij met de instellingen voor het verticale CRS rekening wordt gehouden. Naast een waarschuwing voor gebruikers om te onthouden dat plug-ins en andere gereedschappen geen rekening zouden kunnen houden met de configuratie van het verticale CRS.

![](images/entries/54fd7f19dfda59d13b32525efe28d75af4f72adc.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Widget projecteigenschappen kleurmodus
Widgets voor het configureren van projecteigenschappen zijn toegevoegd voor het beheren van kleurmodi en kleurprofielen op het projectniveau.

Bij het laden van een ICC-profiel zal QGIS consistentie afdwingen tussen het kleurmodel en de kleurruimte.

**Het deel van de widget ICC-profiel is niet zichtbaar, tenzij QGIS is gebouwd met Qt 6.8.0 of hoger**

![](images/entries/c763da512666981c58d3fe8b5dbfa5982ff53d4b.webp)

Dit werd mogelijk gemaakt door Bordeaux Métrôpole\*\*

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Profiel plotten
### Mogelijkheid: Naam hoogteprofiel wijzigen
Een menu-item "Naam hoogteprofiel wijzigen" in het submenu Opties van de widget Hoogteprofiel is toegevoegd, dat de gebruiker de mogelijkheid geeft de naam van het profielvenster te wijzigen.

![](images/entries/81d350164ce88101c33692b9665063970ce72791.webp)

Deze mogelijkheid werd ontwikkeld door [Simon](https://github.com/Simon-Lopez)
### Mogelijkheid: Zorg ervoor dat hoogteprofielen voor vectorlagen rekening houden met verticale datums voor laag/kaart
Wanneer de kaart en/of laag een verticale referentie heeft geconfigureerd (3D-CRS), zal daar binnen profielplots rekening mee worden gehouden

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Browser
### Mogelijkheid: UX toegevoegd om MVT-lagen alleen uit URL voor stijl te halen
Als een tegelvectorlaag is gemaakt met een URL voor de stijl, maar geen bron, wordt de stijl opgehaald en daaruit de bronnen uitgenomen.

Hier is een demo met een laag die twee bronnen heeft: https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json

https://github.com/user-attachments/assets/948db86c-e79f-40cd-9060-6bc84a31fc2a

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
### Mogelijkheid: Functionaliteit voor dupliceren toegevoegd aan Browser-verbindingsitems
QGIS bevat nu een actie "Verbinding dupliceren" in het contextmenu van Browser-verbindingsitems. Dat stelt gebruikers in staat snel een kopie van een verbinding te maken naar dezelfde databron, als slechts een paar details verschillen (bijvoorbeeld een andere database van PostGIS op dezelfde server).

![](images/entries/44b28c871c4d86b6f2c52b326fea88b7e8c1c24e.webp)

Dit werd mogelijk gemaakt door [NaturalGIS](https://www.naturalgis.pt/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Aanpassen van acties contextmenu "Database maken" voor GeoPackage
In eerdere versies van QGIS zou het maken van een nieuwe database van SpatiaLite met deze actie een lege database maken en een nieuwe verbinding maken naar de Browser. Als dezelfde actie wordt uitgevoerd voor GeoPackage-bestanden zou een database met een laag worden gemaakt.

Nieuwe acties voor "Database maken" en "Database en laag maken" zijn toegevoegd voor meer expliciete en consistente opties voor het maken van databases.

![](images/entries/0473ab08a8dd2cae040855020d570535088c4268.webp)

Dit werd mogelijk gemaakt door [NaturalGIS](https://www.naturalgis.pt)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Verbindingen naar providers voor cloudopslag toegevoegd aan Browser
QGIS ondersteunt nu zelf het opslaan en browsen van verbindingen voor cloudopslag binnen het paneel GIS Browser. GDAL ondersteunde en vector- en rasterdatabronnen kunnen direct vanaf cloudproviders worden geladen en alle GDAL VSI cloudafhandelingen worden ondersteund (S3, Azure, Google Drive, etc.)

Verbindingen kunnen ook worden gemaakt, aangepast, verwijderd en geëxporteerd/geïmporteerd naar/vanuit XML-bestanden.

![](images/entries/e6758adb24f9db8651516fc25ae8eac0670988bd.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Integratie van STAC 
Deel een van het implementeren van [QEP300](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/300) is voltooid, wat gebruikers in staat stelt catalogi en elementen van STAC zelf binnen QGIS af te handelen met de Browser.

Een nieuw item STAC in de Browser geeft gebruikers de mogelijkheid om te verbinden met statische catalogi en STAC API-eindpunten.

Items van STAC die voor de cloud geoptimaliseerde delen bevatten (bijv. COG, COPC, EPT) kunnen als kaartlagen worden toegevoegd met de actie slepen-en-neerzetten.

Een dialoogvenster Deel downloaden wordt in het contextmenu van STAC verschaft, wat opslaan van items naar lokale opslag mogelijk maakt.

Alle eigenschappen Catalog, Collection en Item kunnen worden bekeken met het dialoogvenster STAC Objectdetails.

![](images/entries/c6899bc85d87fc36edba1bb71c4613e4b68a6cbe.gif)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor polyhedraal oppervlak en TIN
QGIS ondersteunt nu de eenvoudige objecten `POLYHEDRALSURFACE` en `TIN` bij het introduceren van nieuwe typen geometrie voor `QgsPolyhedralSurface` en `QgsTriangulatedSurface`:
- `QgsPolyhedralSurface` erft van `QgsSurface`
- `QgsTriangulatedSurface` erft van `QgsPolyhedralSurface` als een speciaal geval dat alleen driehoeken bevat.

Deze functionaliteit verwijdert de noodzaak voor eerder gebruikte workarounds, zoals: - TIN is nu het meerdelige deel van een driehoek - Er is geen noodzaak om een polyhedraal oppervlak of een TIN te converteren naar een multipolygoon bij het importeren van deze gegevenstypen vanuit PostGIS.

Dit werd mogelijk gemaakt door CEA/DAM, CP4SC, Oslandia

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## QGIS Server
### Mogelijkheid: WFS titeldefinitie voor lagen
Geïmplementeerd naar service [\#55317](https://github.com/qgis/QGIS/issues/55317) hebben lagen nu een aanvullende eigenschap voor metadata WFS Title server om gebruikers een verschil te kunnen laten maken tussen verschillende laagcollecties voor lagen die worden geserveerd via WFS met QGIS Server.

Deze mogelijkheid werd ontwikkeld door [Jürgen Fischer](https://github.com/jef-n)
## Programmeerbaarheid
### Mogelijkheid: Uitzonderingen opgeworpen voor methoden QgsDistanceArea
Een QgsCsException wordt nu opgeworpen als er fouten optreden binnen methoden QgsDistanceArea om misleidende analyseresultaten te voorkomen en de juiste voortgang voor afhandeling over de gehele toepassing

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: QgsRasterLayer converteren naar NumPy-array
Ontwikkeld als gedeeltelijke oplossing voor [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227) bevat QGIS nu een nieuwe methode `as_numpy` voor objecten `QgsRasterLayer` in PyQGIS die een gemakkelijke conversie van een rasterlaag naar een NumPy-array mogelijk maakt. Voor verbeterde integratieprocessen en verbeterde analyses van rastergegevens met NumPy (Onthoud dat de bibliotheek NumPy een optionele afhankelijkheid is, die niet wordt meegeleverd met de toepassing QGIS).

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Mogelijkheid: QgsGeometry converteren naar Shapely en NumPy
Ontwikkeld als gedeeltelijke oplossing voor [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227) bevat QGIS nu nieuwe methoden `as_numpy` en `as_shapely` voor objecten `QgsGeometry` in PyQGIS, die een gemakkelijke conversie van een geometrie naar een (lijst met) NumPy-array(s) of Shapely-object(en) mogelijk maakt. Voor verbeterde integratieprocessen. (Onthoud dat de relevante bibliotheken optionele afhankelijkheden zijn, die niet worden meegeleverd met de toepassing QGIS).

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Export of geopackage to File Geodatabase creates fid type real causing subsequent vector conversions to fail | [#58690](https://github.com/qgis/QGIS/issues/58690) | [PR #58705](https://github.com/qgis/QGIS/pull/58705) | N/B |
| In QGIS 3.38.2 when deleting an attribute from a gdb file, all the fields in the remaining attributes get deleted as well | [#58669](https://github.com/qgis/QGIS/issues/58669) | [PR #58733](https://github.com/qgis/QGIS/pull/58733) | [PR #58769](https://github.com/qgis/QGIS/pull/58769) |
| test_provider_ogr.py: do not alter source test data, to keep 'git status' clean | Niet gerapporteerd | [PR #58734](https://github.com/qgis/QGIS/pull/58734) | N/B |
| GeoJSON: edits are not saved | [#58261](https://github.com/qgis/QGIS/issues/58261) | [GDAL PR 10794](https://github.com/OSGeo/gdal/pull/10794) | N/B |
| GeoJSON: edits are not saved | [#58261](https://github.com/qgis/QGIS/issues/58261) | [PR #58740](https://github.com/qgis/QGIS/pull/58740) | N/B |
| In Qgis 3.34.4 Saving vector Temporary Scratch Layer as GeoJSON - Newline Delimited leads to Unavailable Layer! error | [#58760](https://github.com/qgis/QGIS/issues/58760) | [PR #58768](https://github.com/qgis/QGIS/pull/58768) | [PR #58771](https://github.com/qgis/QGIS/pull/58771) |
| parquet file exported from QGIS causes crash when loaded into a project | [#58086](https://github.com/qgis/QGIS/issues/58086) | [GDAL PR 10815](https://github.com/OSGeo/gdal/pull/10815) | N/B |
| In Qgis 3.34.4 / 3.38.3 vector layer saved as KML does not allow deleting of polygon features | [#58780](https://github.com/qgis/QGIS/issues/58780) | [GDAL PR 10840](https://github.com/OSGeo/gdal/pull/10840) | N/B |
| Layer user notes only available for QgsVectorLayer when reading a project with flag QgsProject.FlagDontResolveLayers | [#58818](https://github.com/qgis/QGIS/issues/58818) | [PR #58835](https://github.com/qgis/QGIS/pull/58835) | N/B |
| QgsJsonExporter layer field with ValueMap | [#58861](https://github.com/qgis/QGIS/issues/58861) | [PR #58864](https://github.com/qgis/QGIS/pull/58864) | N/B |
| Geospatial PDF Export for Rasters does NOT work | [#58891](https://github.com/qgis/QGIS/issues/58891) | [PR #58895](https://github.com/qgis/QGIS/pull/58895) | [PR #58903](https://github.com/qgis/QGIS/pull/58903) |
| QGIS not recognizing CRS "EPSG:3301 - Estonian Coordinate System of 1997" in MapInfo mid/mif and tab formats | [#58283](https://github.com/qgis/QGIS/issues/58283) | [GDAL PR 10920](https://github.com/OSGeo/gdal/pull/10920) | N/B |
| Don't use the The Word Which Must Not Be Used | Niet gerapporteerd (nou ja, via vijandige kanalen) | [PR #59017](https://github.com/qgis/QGIS/pull/59017) | N/B |
| In Qgis 3.34.4 / 3.38.3 vector layer saved as KML does not allow deleting of polygon features | [#58780](https://github.com/qgis/QGIS/issues/58780) | [GDAL PR 10991](https://github.com/OSGeo/gdal/pull/10991) | N/B |
| [BUGFIX] [PostgreSQL] Properly take into account 'name' type | Niet gerapporteerd | [PR #59147](https://github.com/qgis/QGIS/pull/59147) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (itOpen / qcooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server filter does not work as expected for intersection filters | [#58220](https://github.com/qgis/QGIS/issues/58220) | Kan niet worden gereproduceerd |  |
| [Layout] Missing atlas layer attributes in expression "Fields and Values" group for fixed table item | [#58774](https://github.com/qgis/QGIS/issues/58774) | [PR #58778](https://github.com/qgis/QGIS/pull/58778) | Nee |
| Clearing the default value expression cannot be canceled / undone | [#58767](https://github.com/qgis/QGIS/issues/58767) | [PR #58787](https://github.com/qgis/QGIS/pull/58787) | Nee |
| PostgreSQL authentication gets back to basic if a layer is opened with "execute SQL" from QGIS explorer panel | [#58784](https://github.com/qgis/QGIS/issues/58784) | Kan niet worden gereproduceerd |  |
| QGIS Server: fixed width of 200 px of cascaded WMS layer legends | [#57422](https://github.com/qgis/QGIS/issues/57422) | [PR #58790](https://github.com/qgis/QGIS/pull/58790) | Nee |
| Random Points in Polygons behaves unexpectedly | [#58737](https://github.com/qgis/QGIS/issues/58737) | [PR #58815](https://github.com/qgis/QGIS/pull/58815) | Nee |
| When using a computed or virtual field that refers to other layers's fields having the same name, the wrong value is returned | [#49469](https://github.com/qgis/QGIS/issues/49469) | [PR #58819](https://github.com/qgis/QGIS/pull/58819) | NOG TE DOEN |
| QGIS can't search for PostGIS elsewhere than in the public schema | [#58577](https://github.com/qgis/QGIS/issues/58577) | Geen probleem (gesloten door OP) |  |
| Advanced digitizing using meters instead of ft if ft are set as default unit | [#58620](https://github.com/qgis/QGIS/issues/58620) | [PR #58844](https://github.com/qgis/QGIS/pull/58844) | Wachtrij |
| In layer Filter "lower" function not working with diacritical marks | [#58893](https://github.com/qgis/QGIS/issues/58893) | Kan niet worden gereproduceerd |  |
| Delete expression in Default value + click on another field in the attribute form manager = Crash | [#58887](https://github.com/qgis/QGIS/issues/58887) | [PR #58911](https://github.com/qgis/QGIS/pull/58911) | N/B |
| Deleting "all other values" breaks categorised symbology | [#58875](https://github.com/qgis/QGIS/issues/58875) | [PR #58916](https://github.com/qgis/QGIS/pull/58916) | Wachtrij |
| SLD, Server - Service=WMS&Request=GetStyles: LabelPlacement/Displacement malfunction | [#58862](https://github.com/qgis/QGIS/issues/58862) | [PR #58945](https://github.com/qgis/QGIS/pull/58945) | Wachtrij |
| Creating table on MSSQL sets varchar and nvarchar column lengths as 1 regardless of UI input | [#58809](https://github.com/qgis/QGIS/issues/58809) | [PR #58955](https://github.com/qgis/QGIS/pull/58955) | Wachtrij |
| Unwanted unique constraint added when exporting to geopackage, if not null constraint is applied via default style | [#58431](https://github.com/qgis/QGIS/issues/58431) | [PR #58986](https://github.com/qgis/QGIS/pull/58986) | Riskant? |
| Georeferencer is not using locale in GCP table | [#58765](https://github.com/qgis/QGIS/issues/58765) | [PR #59025](https://github.com/qgis/QGIS/pull/59025) | Wachtrij |
| Basic editing using "Automatic Transaction Groups" generates a critical error | [#58845](https://github.com/qgis/QGIS/issues/58845) | [PR #59076](https://github.com/qgis/QGIS/pull/59076) | Wachtrij |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Repeated Crash when using Reshape Feature Tool | [#57225](https://github.com/qgis/QGIS/issues/57225) | [PR #58779](https://github.com/qgis/QGIS/pull/58779) | [PR #58792](https://github.com/qgis/QGIS/pull/58792) |
| pyqt5_to_pyqt6.py fails on infinite recursion | [#58659](https://github.com/qgis/QGIS/issues/58659) | [PR #58785](https://github.com/qgis/QGIS/pull/58785) | Nee |
| Legend in map atlas anchored to bottom left or bottom right will not correctly reposition in PDF | [#37566](https://github.com/qgis/QGIS/issues/37566) (Regressie) | [PR #58798](https://github.com/qgis/QGIS/pull/58798) | [PR #58920](https://github.com/qgis/QGIS/pull/58920) |
| Calling several times waitForFinished on task would cause a deadlock | Niet gerapporteerd | [PR #58799](https://github.com/qgis/QGIS/pull/58799) | Nee |
| Debian sid Qt6 compile fails on sip build, python bindings | [#57760](https://github.com/qgis/QGIS/issues/57760) | Werkt nu met bijgewerkte Debian |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix rendering of line direction symbols in labels, cleanup label rendering code a bit | [#59107](https://github.com/qgis/QGIS/issues/59107) | [PR #59114](https://github.com/qgis/QGIS/pull/59114) | N/B |
| [gps] Be tolerant to talker IDs which don't start with 'G' | Privé gerapporteerd | [PR #59124](https://github.com/qgis/QGIS/pull/59124) | N/B |
| Fix unsafe use of QgsProject::instance from vector layer classes | Niet gerapporteerd | [PR #59118](https://github.com/qgis/QGIS/pull/59118) | Te riskant |
| When excluding tests, only exclude exact matches | Niet gerapporteerd | [PR #59116](https://github.com/qgis/QGIS/pull/59116) | N/B |
| When layout scalebar settings are invalid, show warning message | Niet gerapporteerd | [PR #59088](https://github.com/qgis/QGIS/pull/59088) | N/B |
| Many cppcheck fixes to get CI green again | Markeer alle operatoren bool als expliciet, geassocieerde reparaties | [PR #59086](https://github.com/qgis/QGIS/pull/59086) | N/B |
| Fix random crashes | [#36125](https://github.com/qgis/QGIS/issues/36125) | [PR #59080](https://github.com/qgis/QGIS/pull/59080) | [PR #59087](https://github.com/qgis/QGIS/pull/59087) |
| Optimise grid decoration rendering | Privé gerapporteerd | [PR #59044](https://github.com/qgis/QGIS/pull/59044) | N/B |
| Optimise text rendering for a common scenario | Privé gerapporteerd | [PR #59037](https://github.com/qgis/QGIS/pull/59037) | N/B |
| Don't override cursor in pin labels map tool | [#59016](https://github.com/qgis/QGIS/issues/59016) | [PR #59033](https://github.com/qgis/QGIS/pull/59033) | [PR #59035](https://github.com/qgis/QGIS/pull/59035) |
| Fix hang when searching expressions using regular expressions | [#59002](https://github.com/qgis/QGIS/issues/59002) | [PR #59019](https://github.com/qgis/QGIS/pull/59019) | N/B |
| Fix aggregate function returns incorrect results | [#58221](https://github.com/qgis/QGIS/issues/58221) | [PR #59000](https://github.com/qgis/QGIS/pull/59000) | [PR #59085](https://github.com/qgis/QGIS/pull/59085) |
| Fix slow performance with layout table filtering with atlas point geom filter | [#58274](https://github.com/qgis/QGIS/issues/58274) | [PR #58999](https://github.com/qgis/QGIS/pull/58999) | [PR #59030](https://github.com/qgis/QGIS/pull/59030) |
| Add user-friendly warnings when built without webkit and opening layouts with html items | [#58975](https://github.com/qgis/QGIS/issues/58975) | [PR #58997](https://github.com/qgis/QGIS/pull/58997) | N/B |
| Fix edit/copy/paste symbol action for layers with inverted polygon renderer | [#55426](https://github.com/qgis/QGIS/issues/55426) | [PR #58967](https://github.com/qgis/QGIS/pull/58967) | [PR #59034](https://github.com/qgis/QGIS/pull/59034) |
| Non-default blend mode should force raster render of layer | [#55629](https://github.com/qgis/QGIS/issues/55629) | [PR #58966](https://github.com/qgis/QGIS/pull/58966) | [PR #59036](https://github.com/qgis/QGIS/pull/59036) |
| Only render main annotation layer in main map canvas or docked maps | [#58766](https://github.com/qgis/QGIS/issues/58766) | [PR #58964](https://github.com/qgis/QGIS/pull/58964) | N/B |
| Regenerate primary key when making layer permanent if layer property set | [#58942](https://github.com/qgis/QGIS/issues/58942) | [PR #58954](https://github.com/qgis/QGIS/pull/58954) | N/B |
| QgsMapLayer::setDataSource don't require layer name, provider | Niet gerapporteerd | [PR #58953](https://github.com/qgis/QGIS/pull/58953) | N/B |
| Fix incompatibility between text wrapping and HTML text formatting | Niet gerapporteerd | [PR #58952](https://github.com/qgis/QGIS/pull/58952) | N/B |
| Fix use of custom object values from QGIS expressions in virtual layers | [#58644](https://github.com/qgis/QGIS/issues/58644) | [PR #58939](https://github.com/qgis/QGIS/pull/58939) | N/B |
| [processing] Fix translation of elapsed strings | [#58635](https://github.com/qgis/QGIS/issues/58635) | [PR #58928](https://github.com/qgis/QGIS/pull/58928) | N/B |
| Fix deadlock when exporting atlas with legend via PyQGIS | [#58496](https://github.com/qgis/QGIS/issues/58496) | [PR #58927](https://github.com/qgis/QGIS/pull/58927) | [PR #58969](https://github.com/qgis/QGIS/pull/58969) |
| Fix clipped render when using geometry generator symbol in layout items | [#58909](https://github.com/qgis/QGIS/issues/58909) | [PR #58926](https://github.com/qgis/QGIS/pull/58926) | N/B |
| Show warning in help for algorithms for known issues or security risk | Privé gerapporteerd | [PR #58925](https://github.com/qgis/QGIS/pull/58925) | N/B |
| [processing] Replace format for saving batch processing parameters | Privé gerapporteerd | [PR #58923](https://github.com/qgis/QGIS/pull/58923) | N/B |
| Fix missing canvas variables in some expression editors | Niet gerapporteerd | [PR #58907](https://github.com/qgis/QGIS/pull/58907) | [PR #58934](https://github.com/qgis/QGIS/pull/58934) |
| Don't restore corrupted sizes/positions when restoring layout items | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58906](https://github.com/qgis/QGIS/pull/58906) | [PR #59103](https://github.com/qgis/QGIS/pull/59103) |
| Add scale method option for layout scale bars | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58904](https://github.com/qgis/QGIS/pull/58904) | N/B |
| Avoid layout scalebar resizing to huge widths in extreme situations | [#55240](https://github.com/qgis/QGIS/issues/55240) | [PR #58794](https://github.com/qgis/QGIS/pull/58794) | N/B |
| QgsDistanceArea methods should raise QgsCsException when errors occur | Niet gerapporteerd | [PR #58795](https://github.com/qgis/QGIS/pull/58795) | N/B |
| Don't apply reset-to-zero step size logic in spin boxes when no special value text is set | Niet gerapporteerd | [PR #58836](https://github.com/qgis/QGIS/pull/58836) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| 2-Circle Point Intersection coordinate precision problem | [#59039](https://github.com/qgis/QGIS/issues/59039) | [PR #59155](https://github.com/qgis/QGIS/pull/59155) | N/B |
| Advanced Digitizing Split Tool zeroes M values in a PolyLineZ shapefile | [#49971](https://github.com/qgis/QGIS/issues/49971) | Niet repareren (probleem GEOS met M) |  |
| QGIS tools splitting curved polygons | [#57021](https://github.com/qgis/QGIS/issues/57021) | Niet repareren (probleem GEOS met ondersteuning Curve) |  |
| Incorrect winding/orientation/order of polygon's vertices in Memory layers | [#58333](https://github.com/qgis/QGIS/issues/58333) | [PR #59156](https://github.com/qgis/QGIS/pull/59156) | Te riskant? |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Layer order change does not update the 3D view | [#51291](https://github.com/qgis/QGIS/issues/51291) | [PR #59026](https://github.com/qgis/QGIS/pull/59026) | [PR #59187](https://github.com/qgis/QGIS/pull/59187) |
| Unwanted vertices when tracing | [#52935](https://github.com/qgis/QGIS/issues/52935) | [PR #59055](https://github.com/qgis/QGIS/pull/59055) | N/B |
| Extra vertices form to all layers when using tracing | [#59041](https://github.com/qgis/QGIS/issues/59041) | [PR #59055](https://github.com/qgis/QGIS/pull/59055) | N/B |
| QGIS drops extra byte fields from laz (char and unsigned char) | [#56945](https://github.com/qgis/QGIS/issues/56945) | [PR #59160](https://github.com/qgis/QGIS/pull/59160) | N/B |
| 3D view - completely flat MultiPolygonZ geometries don't show color correctly | [#52832](https://github.com/qgis/QGIS/issues/52832) | In behandeling |  |
| Adding more than 250 files or a folder with many files and the Build virtual point cloud (VPC) Tool Fails | [#58894](https://github.com/qgis/QGIS/issues/58894) | [PR #59200](https://github.com/qgis/QGIS/pull/59200) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix use of QgsReferencedGeometry in expressions | Niet gerapporteerd | [PR #59180](https://github.com/qgis/QGIS/pull/59180) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Mathieu Pellerin (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Clipping of long WKT strings for geometry parameters by using our geometry widget | Niet gerapporteerd | [PR #59209](https://github.com/qgis/QGIS/pull/59209) | N/B |
| Open Sans font installation failed | [#58988](https://github.com/qgis/QGIS/issues/58988) | [PR #59142](https://github.com/qgis/QGIS/pull/59142) | [PR #59152](https://github.com/qgis/QGIS/pull/59152) |
| Print Layout: with a rotated map, turning on Controlled by Atlas (atlasScalingMode = Auto by default) hangs Layout Manager and corrupts project file | [#58245](https://github.com/qgis/QGIS/issues/58245) | [PR #58749](https://github.com/qgis/QGIS/pull/58749) | N/B |
| Additional NoData value not stored correctly in Raster Layer Properties | [#58293](https://github.com/qgis/QGIS/issues/58293) | [PR #58748](https://github.com/qgis/QGIS/pull/58748) | [PR #58751](https://github.com/qgis/QGIS/pull/58751) |
| Do not copy a geometry column from non-geometry layers | [#58725](https://github.com/qgis/QGIS/issues/58725) | [PR #58746](https://github.com/qgis/QGIS/pull/58746) | [PR #58752](https://github.com/qgis/QGIS/pull/58752) |
| Attribute table: crash and weird behavior when a field has an empty name | [#58738](https://github.com/qgis/QGIS/issues/58738) | [PR #58745](https://github.com/qgis/QGIS/pull/58745) | [PR #58757](https://github.com/qgis/QGIS/pull/58757) |
| Bad styling of scrollbars in the plugin manager dialog | Niet gerapporteerd | [PR #58713](https://github.com/qgis/QGIS/pull/58713) | [PR #58721](https://github.com/qgis/QGIS/pull/58721) |
| "Refresh layer at interval" settings are not saved to QML | [#58656](https://github.com/qgis/QGIS/issues/58656) | [PR #58686](https://github.com/qgis/QGIS/pull/58686) | [PR #58714](https://github.com/qgis/QGIS/pull/58714) |
| Unresponsive "Add record" button in non-geometry layer editing | [#55092](https://github.com/qgis/QGIS/issues/55092) | [PR #58680](https://github.com/qgis/QGIS/pull/58680) | [PR #58710](https://github.com/qgis/QGIS/pull/58710) |
| -- | [PR \#58747](https://github.com/qgis/QGIS/pull/58747) | -- | -- |
| Algorithms having an output directory parameter fail to execute if output directory is set to "Save to temporary folder" | [#58345](https://github.com/qgis/QGIS/issues/58345) | [PR #58619](https://github.com/qgis/QGIS/pull/58619) | [PR #58626](https://github.com/qgis/QGIS/pull/58626) |
| Text in message box 'Font Install Failed' is poorly legible in Night Mapping theme | [#57290](https://github.com/qgis/QGIS/issues/57290) | [PR #58618](https://github.com/qgis/QGIS/pull/58618) | [PR #58628](https://github.com/qgis/QGIS/pull/58628) |
| Bad plugin manager's look on dark themes | Niet gerapporteerd | [PR #58606](https://github.com/qgis/QGIS/pull/58606) |  |
| Decorations are too small when exporting temporal controller images on Mac | [#58469](https://github.com/qgis/QGIS/issues/58469) | [PR #58605](https://github.com/qgis/QGIS/pull/58605) | [PR #58613](https://github.com/qgis/QGIS/pull/58613) |
| Layer with data defined symbology does not appear when QGIS opened | [#58508](https://github.com/qgis/QGIS/issues/58508) | [PR #58603](https://github.com/qgis/QGIS/pull/58603) | [PR #58615](https://github.com/qgis/QGIS/pull/58615) |
| QGIS (3.38.1) crashes when trying to show layer labels. QGIS died on signal 11. | [#58570](https://github.com/qgis/QGIS/issues/58570) | [PR #58602](https://github.com/qgis/QGIS/pull/58602) | N/B |
| Fix layout map item preview rendering of XYZ layers with known tile DPI | Niet gerapporteerd | [PR #58543](https://github.com/qgis/QGIS/pull/58543) | [PR #58566](https://github.com/qgis/QGIS/pull/58566) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin (OPENGIS)](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Remaining rubberband and plot data after clearing profile tool | [#50766](https://github.com/qgis/QGIS/issues/50766) | [PR #59181](https://github.com/qgis/QGIS/pull/59181) | N/B |
| Fix issue with vertical lines not visible in the elevation profile tool | niet gerapporteerd | [PR #58959](https://github.com/qgis/QGIS/pull/58959) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Germán Carrillo (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scale dependent visibility inconsistencies on scale interval edges (symbology, labeling, diagrams) | [#58150](https://github.com/qgis/QGIS/issues/58150) <br> [#42443](https://github.com/qgis/QGIS/issues/42443) | [PR #58968](https://github.com/qgis/QGIS/pull/58968) <br> [PR #59022](https://github.com/qgis/QGIS/pull/59022) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS)](https://opengis.ch/)

{{<content-end >}}
