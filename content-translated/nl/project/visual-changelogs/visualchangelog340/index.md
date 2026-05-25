---
HasBanner: false
draft: false
releaseDate: 25-10-2024
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
### Feature: Add scale method option for layout scale bars
A new option for selecting a user-defined method of calculating the map scale in print layouts is provided. This exposes options for calculating scale:
- along the bottom of the map frame
- along the middle of the map frame
- along the top of the map frame
- as an average of all three measurements

By default, new scale bars will utilize the average method (instead of the previously used "along bottom" method), which will better handle scenarios where the scale at the top or bottom of the map cannot be calculated (e.g. when the top or bottom of the map falls outside valid areas for the map CRS).

![](images/entries/ff809eacb3e8701d38d43292ae3d5694cb16076d.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Feature: Add 'Custom Expression' numeric format
This numeric format allows users to craft a custom QGIS expression to format numbers. The expression can use the @value variable to retrieve the value to be formatted, and then use any standard QGIS expression function to format this as desired.

It can be used anywhere QgsNumericFormat is accepted, such as layout scalebars, elevation plots, layout tables, and color ramp legends

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add line\_interpolate\_point\_by\_m and line\_locate\_m expressions
Two new functions are provided to the expression engine to work with M values along line strings:
- `line_interpolate_point_by_m`: returns a point geometry of a matching m value interpolated along a line containing an m dimension.
- `line_locate_m`: returns a distance from the beginning of a line where a matching m value was found.

These functions are useful when working with temporal data (such as a linestring representing a GPS track, where the M value represents the epoch value), and can be used effectively alongside the temporal controller to create beautiful animations that were previously harder to unlock.

![](images/entries/43d4feab4f7d4fb0fe167c7120b19a7cae13fc47.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Extended color value support
In line with [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283), new expression functions allow for the retrieval of colors that include:
- color\_rgbf
- color\_cmykf
- color\_hsvf
- color\_hslf

These functions differ from the existing color retrieval expression functions (e.g. color\_rgb) by returning color values with different internal data types. This improves performance and fidelity by avoiding unnecessary color conversions in specific contexts, such as writing PDFs with native CMYK colors derived from expression values.

Dit werd mogelijk gemaakt door Bordeaux Métropôle

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Feature: Allow users to save expression functions in QGIS project file
A new `[Project Functions]` element is now available within the expression builder dialog, allowing QGIS to store custom user-defined functions embedded in the project file.

This reduces the need to manually share Python code snippets and copy them to the user profile directory or import them into the expression builder dialog.

Project functions are unloaded when a project is closed, and user functions are reloaded to avoid any potential overwrite by activated project functions.

For security reasons, the handling of whether to load or not load these functions on project startup is configurable in the user settings with the same rationale used for managing project macros.

![](images/entries/fb459ca9362a65771713ed9b571b12a265e0b45d.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Feature: Add info about usable "expression dialect" to filter dialog
The query builder used for entering filter expressions on vector layers now shows the supported expression dialect.

![](images/entries/1bd0096fbd0fac4d612b2ca98bc7ef86cedac36e.webp)

Dit werd mogelijk gemaakt door WhereGroup GmbH.

Deze mogelijkheid werd ontwikkeld door [Hannes](https://github.com/kannes)
### Feature: Add project\_color\_object and ramp\_color\_object functions
In line with [QEP\#283](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283), new expression functions provide support for setting project and ramp colors using CMYK color values using expressions

Dit werd mogelijk gemaakt door Bordeaux Metropole

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Digitaliseren
### Feature: Add circles intersection digitizing tool
A new advanced digitizing tool allows users to pick/ digitize a point at the intersection of two circles

To support this functionality, the QGIS API has been extended with a new abstract class for supporting similar "COGO" development in the future, as well as providing Python bindings for developing advanced digitization utilities and plugins.

![](images/entries/990ee4bd78f0d0732ca02562ce953bed4c9443a8.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Visual construction guides for advanced digitizing
Visual construction guides have been added to the advanced digitizing dock widget, which builds on the existing CAD construction mode.

When recording construction guides, QGIS will render all construction steps taken as dashed lines which will remain visible for as long as advanced digitizing is enabled. The guides are snap-able, allowing for construction steps to begin mid-way into a previous set of steps too.

The construction guides are stored in a vector layer, which is exposed through the advanced digitizing dock widget, allowing for further customization of the guides via other application processes, such as Python plugins.

![](images/entries/d77759a3bc23a050b3e8e9cc5a5d3bb5cc91dff3.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Gegevensbeheer
### Feature: Allow setting VSI credentials when loading OGR/GDAL layers
VSI credential options are now exposed for user control when adding OGR vector/GDAL raster layers from the Data Source Manager, allowing users to define credentials on a per-layer basis for layers retrieved from cloud services (rather than use a single set of credentials for an entire QGIS session using an environment variable or similar approach).

Vereist GDAL 3.5+

![](images/entries/e824e2a5aef50de87656d6beced8ea0ae0f60e41.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Formulieren en widgets
### Feature: Allow reordering fields in new vector layer dialogs
When creating a new vector layer, including scratch, shp, gpkg, and spatialite, users will now be able to reorder the field definitions.

![](images/entries/3623fff590c84705c9e75fa22c3e0cc9c537c9e0.webp)

Dit werd mogelijk gemaakt door Deense QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add metadata setting to override widget wrapper used for a parameter
While it was possible to add new widget wrappers for Processing parameters, it was not possible to override the standard widget wrappers defined for each parameter type.

A new parameter metadata setting for "widget\_type" has been added, which provides developers to override the standard widget wrapper for a parameter for more control of application dialogues.

`param.setMetadata( } )`

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
## Processing
### Feature: Open file or URL Algorithm
A simple native algorithm has been added to allow for the opening of local files using the corresponding system programs, or URLs in a web browser.

Useful in combination with the Download File Algorithm to open the resulting file, or to display results after models triggering external systems.

![](images/entries/2ab9a02e47e9d3dc7a0c4e1dc5f65d195244869b.webp)

Dit werd mogelijk gemaakt door het [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Dave Signer (OPENGIS.ch)](https://opengis.ch)
### Feature: Add processing parameter types for Area and Volume
Adds dedicated parameter types for Area and Volume values.

Modeled closely off the existing Distance parameter type.

![](images/entries/8324f615ac89f6d617619f34f6cc37ee2ae55a2a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Updated "Vector information" algorithms
The GDAL Processing algorithm for vector information has been modified to support additional command-line parameters, and a new **Vector information (JSON)** algorithm is provided that will use the [`-json`](https://gdal.org/programs/ogrinfo.html#cmdoption-ogrinfo-json) option of ogrinfo to create a JSON file output containing the layer or dataset information.

![](images/entries/b890a9ff0af7e1ef313c620c48150f871f1177f0.webp)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Allow adding Processing tools to Favorites
New 'Favorites' functionality has been added for Processing alogrithms, allowing users to statically pin their chosen algorithms to a dedicated section at the top of the toolbox for ease of access.

![](images/entries/2108d8a4104ef9d50f44a72171274469bde1e429.webp)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add creation options support to some native raster Processing algorithms
More raster creation options have been added to native Processing algorithms for more control of the output format (compression level, world file generation etc.). Affected algorithms include:
- Celstatistieken
- Constant raster
- Export mesh
- 'Geen gegevens' vullen
- Fuzzify raster
- Dichtheid lijn
- Willekeurig raster
- DTM-filter (gebaseerd op helling)
- Gelijk aan frequentie
- Raster boolean AND/OR
- Raster stack position
- Reclassify
- Rescale
- Rond

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Support drag and drop for multi-layer parameters
Allows dragging and dropping layers from either the QGIS browser or file explorer onto any multiple-layer parameter panel. Handy when you have to add many layers and it's simpler to make a selection outside of the processing dialog.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Opties voor toepassing en projecten
### Feature: Smart cache size implementation
QGIS now has improved handling of its network disk cache by leveraging smart cache size logic currently utilized by modern web browsers.

This allows the cache to dynamically resize based on available storage space on the cache disk, and will result in most users getting a larger cache size (and improved network performance) by default as well as limiting loads to external providers and XYZ tile services.

Users can disable the smart cache size logic in favor of a static cache size using the updated Options dialog.

![](images/entries/80e1931b0152bfe035105520396a775b6f9bfbaf.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add vertical CRS selection widget to vector layer properties
Vector layers can now include discrete settings for configuring the vertical reference system.

Application behavior for the definition of vertical reference on a layer will follow the same behavior as the project settings, namely:
- If the layer has a 3D CRS set, then the widget is disabled with an explanatory note
- If the layer has a 2D CRS set, then the user can select the appropriate vertical CRS

An explanatory note is included which details the facets of the application where the vertical CRS settings are respected, along with a warning for users to note that plugins and other tools may not respect the layers' vertical CRS configuration.

![](images/entries/54fd7f19dfda59d13b32525efe28d75af4f72adc.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Project color mode properties widget
Project properties configuration widgets have been added for managing color modes and color profiles at the project level.

When loading an ICC profile, QGIS will enforce consistency between the color model and color space.

**The ICC profile widget part is not visible unless QGIS is built with Qt 6.8.0 or greater**

![](images/entries/c763da512666981c58d3fe8b5dbfa5982ff53d4b.webp)

Dit werd mogelijk gemaakt door Bordeaux Métrôpole\*\*

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Profiel plotten
### Feature: Change elevation profile name
A "Change Profile Name" menu item in the Options sub-menu of the Elevation Profile widget has been added that allows the user to change the name of the profile window.

![](images/entries/81d350164ce88101c33692b9665063970ce72791.webp)

Deze mogelijkheid werd ontwikkeld door [Simon](https://github.com/Simon-Lopez)
### Feature: Ensure vector layer elevation profiles respect layer/map vert datums
When the map and/or layer has a vertical reference (3D CRS) configured it will be respected within profile plots

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Browser
### Feature: add UX to load MVT layers from style URL only
If a tile vector layer is created with a style URL but not source, the style is fetched and sources are extracted from it.

Here is a demo with a layer having two sources: https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json

https://github.com/user-attachments/assets/948db86c-e79f-40cd-9060-6bc84a31fc2a

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
### Feature: Add duplicate functionality to Browser connection items
QGIS now includes a "Duplicate connection" action in the context menu of Browser connection items. This allows users to quickly make a copy of a connection to the same data source when only a few details differ (for example, a different PostGIS database on the same server).

![](images/entries/44b28c871c4d86b6f2c52b326fea88b7e8c1c24e.webp)

Dit werd mogelijk gemaakt door [NaturalGIS](https://www.naturalgis.pt/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Adjust "Create Database" context menu actions on GeoPackage
In previous versions of QGIS, creating a new SpatiaLite database with this action would create an empty database and add a new connection to the browser, while the same action executed for GeoPackage files would generate a database with a layer.

New actions for "Create Database" and "Create Database and Layer" have been added for more explicit and consistent database creation options.

![](images/entries/0473ab08a8dd2cae040855020d570535088c4268.webp)

Dit werd mogelijk gemaakt door [NaturalGIS](https://www.naturalgis.pt)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Feature: Add connections to cloud storage providers to browser
QGIS now natively supports the storing and browsing cloud storage connections within the QGIS browser panel. GDAL supported vector and raster data sources can be loaded directly from cloud providers and all GDAL VSI cloud handlers are supported including (S3, Azure, Google Drive, etc.)

Connections can also be created, modified, removed, and exported/imported to/from XML files.

![](images/entries/e6758adb24f9db8651516fc25ae8eac0670988bd.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: STAC integration
Part one of the [QEP300](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/300) implementation has been completed, allowing users to handle STAC catalogs and elements natively within QGIS using the browser.

A new STAC entry on the browser allows users to connect to static catalogs and STAC API endpoints.

STAC Items that contain cloud-optimized assets (e.g. COG, COPC, EPT) can be added as map layers via the drag-and-drop action.

A Download Assets dialog is provided in the STAC context menu that allows saving items to local storage.

All Catalog, Collection, and Item properties can be examined using the STAC Object Details dialog.

![](images/entries/c6899bc85d87fc36edba1bb71c4613e4b68a6cbe.gif)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
## Gegevensproviders
### Feature: Support for polyhedral surface and TIN
QGIS now supports the `POLYHEDRALSURFACE` and `TIN` simple features by introducing new geometry types for `QgsPolyhedralSurface` and `QgsTriangulatedSurface`:
- `QgsPolyhedralSurface` inherits from `QgsSurface`
- `QgsTriangulatedSurface` inherits from `QgsPolyhedralSurface` as a special case which only contains triangles.

This functionality removes the need for previously used workarounds, such as: - TIN is now the multipart of a triangle - There is no need to convert a polyhedral surface or a TIN to a multipolygon when importing these data types from PostGIS.

Dit werd mogelijk gemaakt door CEA/DAM, CP4SC, Oslandia

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## QGIS Server
### Feature: WFS title definition for layers
Implemented to service [\#55317](https://github.com/qgis/QGIS/issues/55317), layers now have an additional WFS Title server metadata property to allow users to differentiate between different layer collections on layers served via WFS with QGIS Server.

Deze mogelijkheid werd ontwikkeld door [Jürgen Fischer](https://github.com/jef-n)
## Programmeerbaarheid
### Feature: Exceptions raised on QgsDistanceArea methods
A QgsCsException is now raised when errors occur within QgsDistanceArea methods to prevent misleading analysis results and properly handle error propagation throughout the application

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Convert QgsRasterLayer to NumPy Array
Developed in partial fulfillment of [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), QGIS now includes a new `as_numpy` method on `QgsRasterLayer` objects in PyQGIS which allow for the easy conversion of a raster layer to NumPy array for improved integration processes and improved analysis of raster data using NumPy (Note that the NumPy library is an optional dependency not shipped with the QGIS Application).

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Feature: Convert QgsGeometry to Shapely and NumPy
Developed in partial fulfillment of [QEP 227](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/227), QGIS now includes `as_numpy` and `as_shapely` methods on `QgsGeometry` objects in PyQGIS which allow for the easy conversion of a geometry to a (list of) NumPy array(s) or Shapely object(s) for improved integration processes (Note that the relevant libraries are optional dependencies not shipped with the QGIS Application).

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
| Debian sid Qt6 compile fails on sip build, python bindings | [#57760](https://github.com/qgis/QGIS/issues/57760) | Now working with updated debian |  |

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
### Feature: Bug fixes by Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| 2-Circle Point Intersection coordinate precision problem | [#59039](https://github.com/qgis/QGIS/issues/59039) | [PR #59155](https://github.com/qgis/QGIS/pull/59155) | N/B |
| Advanced Digitizing Split Tool zeroes M values in a PolyLineZ shapefile | [#49971](https://github.com/qgis/QGIS/issues/49971) | Do not fix (GEOS issue with M) |  |
| QGIS tools splitting curved polygons | [#57021](https://github.com/qgis/QGIS/issues/57021) | Do not fix (GEOS issue with Curve support) |  |
| Incorrect winding/orientation/order of polygon's vertices in Memory layers | [#58333](https://github.com/qgis/QGIS/issues/58333) | [PR #59156](https://github.com/qgis/QGIS/pull/59156) | Too risky? |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/)
### Feature: Bug fixes by Stefanos Natsis (LutraConsulting)
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
### Feature: Bug fixes by Mathieu Pellerin (OPENGIS)
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
### Feature: Bug fixes by Germán Carrillo (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scale dependent visibility inconsistencies on scale interval edges (symbology, labeling, diagrams) | [#58150](https://github.com/qgis/QGIS/issues/58150) <br> [#42443](https://github.com/qgis/QGIS/issues/42443) | [PR #58968](https://github.com/qgis/QGIS/pull/58968) <br> [PR #59022](https://github.com/qgis/QGIS/pull/59022) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS)](https://opengis.ch/)

{{<content-end >}}
