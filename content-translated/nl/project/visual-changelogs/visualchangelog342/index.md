---
HasBanner: false
draft: false
releaseDate: '2025-02-21'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.42
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.42{#changelog342 }
![](images/projects/b5beabaeef257557086b43ccdceffed3c78d8676.png.webp)

Datum uitgave: 21-02-2025

Het project QGIS kondigt met trots de uitgave aan van QGIS 3.42. Een significante stap voorwaarts in de ontwikkeling van vrije en open georuimtelijke informatiesystemen. Deze uitgave bouwt voort op de solide funderingen van eerdere uitgaven en introduceert daarbij spannende nieuwe mogelijkheden en verbeteringen die werkstromen zullen stroomlijnen en gebruikers in hun kracht zullen zetten bij hun inspanningen op het gebied van analyses.

Opmerkelijke verbeteringen zijn geïntroduceerd voor mogelijkheden buiten het traditionele kaartframe, zoals verscheidene aspecten van 3D-kaartweergaven, plots en profielen. Alsook een nieuwe widget voor overzicht van virtuele puntenwolken voor verbeterde navigatie in complexe gegevenssets. Meer beheersmogelijkheden worden verschaft voor cartografische functionaliteit, zoals op CSS gebaseerde labeleigenschappen en uitbreidingen aan de Python API. Terwijl ook geavanceerde gegevenstypen, zoals Mazen en Puntenwolken, hun rechtmatige deel aan verbeteringen hebben gekregen.

Een nieuwe set gereedschappen voor Metadata is toegevoegd aan de Toolbox van Processing (naast verscheidene andere nieuwe aanvullingen en verbeteringen), terwijl een nieuwe mogelijkheid gebruikers de mogelijkheid geeft om pixels op rastergegevens te labelen. Gereedschappen voor lay-out zijn niet vergeten en de QGIS Pythonconsole heeft ook een nieuwe interactieve mogelijkheid voor hulp met directe integratie met bronnen voor projectdocumentatie voor een verbeterde ervaring voor de ontwikkelaars.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=v6Ejov4u7xk).

[![](https://img.youtube.com/vi/v6Ejov4u7xk/0.jpg)](https://www.youtube.com/watch?v=v6Ejov4u7xk)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Symbologie
### Mogelijkheid: Te configureren buffer voor bereik toegevoegd voor symbolen
In eerdere versies van QGIS kwamen alleen objecten die waren geplaatst binnen het kaartbereik in aanmerking om onder bepaalde omstandigheden te worden gerenderd.

Dit zou problemen kunnen veroorzaken voor bepaalde symbologieën, speciaal bij het gebruiken van complexe geometriegeneratoren. Omdat gebruikers geen objecten zouden zien waarvan het gerenderde symbool misschien binnen het kaartvenster zou verschijnen, maar het bronobject niet.

Als bijvoorbeeld een object punt wordt gebruikt om een bufferpolygoon te maken, zoals `buffer(@geometry, 7)`, zou de buffer niet renderen als het punt niet binnen het kaartvenster zou liggen.

Een nieuwe optie voor configuratie van symbolen maakt het voor een buffer op het kaartvenster mogelijk om deze aanvullende objecten op te nemen binnen door de gebruiker gedefinieerde beperkingen en balanceert tussen prestaties en eisen voor complexe gegevensvisualisatie.

![](images/entries/bf954ba6632135c099f5e5d7f8db594e19dc01a2.png.webp)

Dit werd mogelijk gemaakt door de National Land Survey of Finland.

Deze mogelijkheid werd ontwikkeld door [Juho Ervasti](https://github.com/JuhoErvasti)
## Labelen
### Mogelijkheid: Raster labelen
QGIS staat nu toe dat rasterpixels worden gelabeld met de waarde die wordt genomen uit een rasterband. Labels worden geregistreerd bij het labelmechanisme en zullen zo deelnemen bij het oplossen van conflicten van labels en het vermijden van overlappen. Optie omvatten:
- Selecteren van band waaruit de waarden moeten worden genomen
- Gebruiken van QgsNumericFormat om de getalindeling voor de labels aan te passen
- Tekstrenderer gebruiken, ondersteunt dus buffers, schaduw, etc.
- Prioriteit label
- Schaalafhankelijke zichtbaarheid
- Optionele zichtbaarheid die afhankelijk is van de pixelgrootte, d.i. alleen weergeven als pixels &gt;4 mmin grootte zijn
- Beheer van de Z-index, modus voor vermijden van overlappen
- Optie voor weergeven van waarden die zijn hersampled over naburige pixels

![](images/entries/0ac302054a6a0e64bc140f4e7ebd403f0894a634.png.webp)

Dit werd mogelijk gemaakt door Kanton Neuchâtel

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aangepaste tabafstanden voor labels
Maakt het mogelijk een lijst met aangepaste afstanden voor tabstops op te nemen voor labels. In plaats van slechts een enkele afstand. Dit maakt verschillende drempels mogelijk om tussen afbrekingen te worden gebruikt.

![](images/entries/fb24a7593018d5732f9e3b64a68912e38d431dd3.png.webp)

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor eigenschap CSS-achtergrond in labels/tekstrenderer
QGIS ondersteunt nu de eigenschappen voor CSS background-color en background-image indien gebruikt met HTML-labels.
- Achtergronden worden ondersteund voor blokitems (bijv. `<div>`) of inline-items (bijv. `<span>`)
- Voor afbeeldingen zou de CSS moeten worden opgemaakt als background-image: url(xx). Het ondersteunt lokale bestandspaden, http-koppelingen of ingebedde inhoud van base64
- Achtergronden worden niet ondersteund voor gebogen tekst
- HTML-achtergronden worden altijd gerenderd boven elke achtergrondvorm voor het label, en onder valschaduw/buffer

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor CSS-marges voor blokelementen in HTML-labels
QGIS heeft ondersteuning toegevoegd voor eigenschappen voor CSS-margin voor blockelementen in de tekstrenderer. Specifiek:
- Dit is alleen beschikbaar voor elementen van het type block, bijv. DIV, P, H1-H6.
- Marges zijn NIET beschikbaar voor spans of andere inhoud die geen block is (wegens beperkingen van Qt)
- Marges mogen alleen worden gespecificeerd in eenheden pt units
- Marges mogen worden gespecificeerd ofwel via "margin-left: 5pt; margin-right: 10pt" etc, of "margin: 5pt 0pt 10pt 0pt"
- Negatieve marges worden ALLEEN ondersteund voor de ondermarge (wegens beperkingen van Qt)

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor CSS line-height in HTML-labels
QGIS heeft ondersteuning voor de eigenschap van CSS line-height toegevoegd in als HTML opgemaakte labels.

Ondersteunt line-height in ofwel punten of als percentage, bijv. "line-height: 40pt" of "line-height: 40%"

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Mazen
### Mogelijkheid: Instellingen renderbereik van lagen met mazen
De instelling voor de renderer van lagen met mazen bevat nu een optie voor het instellen van de limieten Min/Max voor de renderer Kleurenbalk, gebaseerd op het huidige bereik van het kaartvenster. Dat kan worden vergrendeld naar een specifieke instantie van het kaartvenster of worden gewijzigd, gebaseerd op het actieve kaartvenster, met hetzelfde gedrag voor renderen als rasterlagen.

![](images/entries/36f92b26c173dbaddf798eb572e795a1759b2b5e.webp)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Lagen met mazen bewerken met verfijning Delaunay
Bewerken van lagen met mazen bevat nu een nieuwe optie voor verfijnen met Delaunay. Bij het toevoegen van een punt aan een zijde van een maas stelt deze mogelijkheid u in staat de naburige driehoekige zijden automatisch te verfijnen. Het algoritme controleert of de randen van deze aanliggende zijden voldoen aan de voorwaarde voor Delaunay, en als dat niet zo is, spiegelt het de randen automatisch om de kwaliteit van de maas te verbeteren.

![](images/entries/80bfb4d962708d894f5ae8735a8cf19d5de14dad.gif)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Besturingselementen groep gegevensset voor laag met mazen
Lagen met mazen bieden nu meer flexibel beheer van groepen in de gegevensset. Gebruikers kunnen groepen voor de gegevensset toevoegen met dezelfde naam (echter niet vanuit dezelfde URI) aan een laag met mazen. Om verwarring te vermijden tussen deze duplicate namen zal automatisch een getal worden toegevoegd (bijv. "Originele naam\_1").

Aanvullend kunnen gebruikers nu groepen van de gegevensset verwijderen uit een laag met mazen. Echter, alleen toegevoegde groepen voor de gegevensset (niet die welke zijn geassocieerd aan het originele bronbestand voor de mazen) kunnen worden verwijderd, wat het per ongeluk verwijderen van brongegevens voorkomt.

![](images/entries/dc92e7714bf34361837b67c23cd3faf1ea5bb797.webp)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Acties voor selecteren van mazen
Twee nieuwe acties zijn toegevoegd voor het selecteren van punten in lagen met mazen, namelijk:
- selecteer geïsoleerde punten die geen deel van een zijde zijn
- selecteer alle punten uit de laag met mazen

Dit geeft gebruikers meer beheer over de selectiecriteria voor specifieke punten.

![](images/entries/537402aa2d62c6db821d0f6eea457785adfbfc86.webp)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: Modi voor toewijzen hoogte voor toegevoegde punten in lagen met mazen
Het gereedschap "Elementen voor mazen digitaliseren" heeft een aanvullend menu dat gebruikers in staat stelt te selecteren welke methode te gebruiken voor het toewijzen van waarden Z op nieuw gemaakte punten. Nieuwe opties bevatten:
- Voorkeur mazen, dan widget Z (interpoleert waarde Z uit mazen als een punt binnen de zijde van een maas ligt, anders gebruikt het de waarde van de widget Z)
- Voorkeur mazen, dan terrein (interpoleert waarde Z uit mazen als een punt binnen de zijde van een maas ligt, anders gebruikt het de terreinwaarde)
- Project Terrein (gebruikt altijd projectterrein waarde Z)
- Widget Z (gebruikt altijd waarden Z uit de widget)

Het paneel "Punten mazen transformeren" heeft ook een nieuwe knop gekregen die het mogelijk maakt dat gebruikers de waarde Z instellen voor geselecteerde punten uit afgeleide waarden, gebaseerd op de instellingen van het projectterrein.

![](images/entries/134e4b88cb478ff8c1d72fc1eb35cf873e416ab4.png.webp)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## 3D-objecten
### Mogelijkheid: Widget Debuggen voor 3D-weergaven
Een nieuw zijpaneel voor debuggen voor 3D-kaartweergaven verplaatst alle relevante instellingen voor debuggen naar een enkele locatie.

![](images/entries/b676f80f03eeac81a44dd5d95c21a1dd1d968d42.webp)

Deze mogelijkheid werd ontwikkeld door [Matej Bagar](https://github.com/Withalion)
## Puntenwolken
### Mogelijkheid: Overzichten virtuele puntenwolken in 2D
Het standaardgedrag van het renderen van virtuele puntenwolken is gewijzigd, zodat, indien aanwezig, een overzicht wordt gerenderd en als alternatief bereiken worden gerenderd bij uitzoomen. Configureren van lagen via het paneel Laag opmaken verschaft geavanceerd beheer over het gebruikergedefinieerde gedrag, wat gebruikers de mogelijkheid geeft om naadloos te schakelen tussen tussen renderen van slechts de bereiken, slechts het overzicht, of een combinatie van die twee.

![](images/entries/76df45b4beff919f1428f39e13370c5bd48facb1.png.webp)

Dit werd mogelijk gemaakt door Klimadatastyrelsen

Deze mogelijkheid werd ontwikkeld door [Matej Bagar](https://github.com/Withalion)
## Afdruklay-outs
### Mogelijkheid: Dubbelklikken op een handvat voor een lay-outlabel past dat aan om de tekst te laten passen
Dubbelklikken op een handvat zal het label automatisch zo op grootte maken dat de opgenomen tekst exact in het label past (groeien of krimpen waar nodig). De tegenoverliggende zijde van het label zal vast op zijn plaats blijven, zodat bijvoorbeeld dubbelklikken op het handvat rechtsonder ervoor zorgt dat de rechterbenedenhoek van het label verplaatst.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Actie bij bubbelklikken op lay-outitem
De QGIS API is uitgebreid om een gebeurtenis toe te voegen voor elementen van Afdruklay-out waarop dubbel wordt geklikt. Wat het mogelijk maakt dat in de toekomst meer geavanceerde functionaliteiten worden geïntroduceerd (bijv. dubbelklikken om een item te bewerken).

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Lay-out beter maken van item knoop
Bij het digitaliseren van vormen met gereedschappen van lay-out is het gedrag aangepast om beter uit te lijnen met de bestaande gebruikservaring in gereedschappen van Digitaliseren. Wat gebruikers de mogelijkheid geeft om onjuist vastgelegde punten in hun vormen te verwijderen.

![](images/entries/65a754c47bc5d678e9716fc168d3802a96b04a2e.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Paginagrootte lay-out toepassen op alle pagina's
Een nieuwe knop "Op alle pagina's toepassen" is toegevoegd aan het paneel Pagina-eigenschappen voor lay-outs met meerdere pagina's, zodat gebruikers efficiënter wijzigingen kunnen maken aan complexe eigenschappen voor lay-out.

![](images/entries/17edee9a6187866ed824fe92134f088e32327056.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Nieuwe kwaliteitsparameter voor exporteren van lay-out naar JPG
Een nieuwe kwaliteitsparameter is toegevoegd aan de opties voor exporteren naar JPEG/JPG-afbeelding in afdruklay-outs om gebruikers beter beheer over hun opties voor exporteren te geven.

![](images/entries/ddc1fa979771c938ec22dabcadefda2cd79aa96b.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Digitaliseren
### Mogelijkheid: Accentueren afbreken/uitbreiden kruisingsvlak
De opmaak en het gedrag voor de functionaliteit Afbreken/Uitbreiden is aangepast om beter te worden uitgelijnd met de gebruikservaring van de gereedschappen Geavanceerd digitaliseren, zodat grenzen van geometrieën visueel duidelijker worden weergegeven aan gebruikers.

![](images/entries/afff864bb555fcfba93b700cf4f63c7e2eb65390.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Gegevensbeheer
### Mogelijkheid: Snappen inschakelen in de Georeferencer
Het paneel Geavanceerd digitaliseren en opties voor Snappen zijn toegevoegd aan de interface Georeferencer om gebruikers beter beheer te geven over referentiepunten bij het uitlijnen van gegevenssets.

![](images/entries/5d2403406b6bf2644f6ba0d60a77364dc80b4c7b.png.webp)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
### Mogelijkheid: Verbeteringen STAC in Databronnen beheren
Doorbouwend op de mogelijkheden voor de STAC Cliënt, die werden geïntroduceerd in QGIS 3.40 als een deel van [QEP\#300](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/300), ondersteunt de QGIS STACcliënt nu aanvullende functionaliteiten inclusief:
- STAC Catalog functionaliteit voor zoeken binnen Databronnen beheren
- Geavanceerd filteren voor teruggegeven resultaten
- Weergeven of verbergen van voetafdrukken van de items van de zoekresultaten in het kaartvenster
- Accentueren van de voetafdruk van het geselecteerde item

![](images/entries/86d59b6e6bbcafcd505cc6301d26f55b295566db.webp)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
## Formulieren en widgets
### Mogelijkheid: Aanvullende opties voor sorteren voor widget Waarderelatie
De widget Waarderelatie bevat nu een aantal nieuwe opties voor sorteren, inclusief:
- omgekeerde volgorde
- volgorde op een specifiek veld

![](images/entries/ea40b733da3f998b83590ce985986cf8438fe2d7.webp)

Dit werd mogelijk gemaakt door Consorzio della Bonifica Renana

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Configuratie voor widget kopiëren en plakken bij ontwerpen van formulieren
Een contextmenu is toegevoegd aan het paneel `Beschikbare widgets` in het dialoogvenster Laageigenschappen voor vectors. Dat maakt het voor gebruikers mogelijk configuraties van widgets te kopiëren en te plakken tussen velden van dezelfde laag, tussen velden van verschillende lagen in het project van QGIS, of tussen velden uit lagen in verschillende instanties van QGIS.

![Copy and paste context menu](images/entries/copy_paste_widget_configuration.webp)

Dit werd mogelijk gemaakt door Ville de Pully (Switzerland)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Processing
### Mogelijkheid: Processing gereedschappen voor metadata
Nieuwe eigen algoritmes zijn toegevoegd aan de Toolbox van Processing voor het beter afhandelen van metadata van lagen.
- Kopieer metadata van een laag om metadata van een invoerlaag naar een doellaag te kopiëren
- Pas metadata van een laag toe om metadata voor een laag in te stellen uit een bestand QMD
- Exporteer metadata van een laag om metadata voor een laag in een bestand QMD te exporteren
- Voeg geschiedenis van metadata toe om een nieuw item voor geschiedenis toe te voegen aan bestaande items die zijn gedefinieerd voor een laag
- Werk metadata voor een laag bij om niet-lege velden van metadata uit de invoerlaag te kopiëren naar een doellaag en behoud de lege velden uit de invoer ongewijzigd in het doel
- Stel velden voor metadata in om eenvoudige velden voor metadata in te stellen (identificatie, ouderidentificatie, titel, type, codering, taal, CRS, abstract, kosten)

![](images/entries/a61da0150028588dafa6e2fb98c0f71d628bdd29.png.webp)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Op expressie gebaseerd over inhoud gaan in verspreidingsplots
Nieuwe opties voor het Processing algoritme Verspreidingsplot vectorlaag maakt het voor gebruikers mogelijk om optioneel tekst toe te voegen met expressies van QGIS die wordt weergegeven als er met de muis overheen wordt gegaan.

![](images/entries/43b93ee8f5a7632654207f5d31345ea9a66ec538.webp)

Deze mogelijkheid werd ontwikkeld door [Florian Neukirchen](https://github.com/florianneukirchen)
### Mogelijkheid: Optie toegevoegd om attributen 'laag' en 'pad' op te nemen in gereedschap Vectorlagen samenvoegen
Een nieuw keuzevak is toegevoegd aan het gereedschap voor processing Vectorlagen samenvoegen. Deze optie geeft gebruikers de mogelijkheid om ervoor te kiezen de attributen laag en pad uit de individuele invoervectorlagen op te nemen in de resulterende samengevoegde laag. Standaard is deze optie ingeschakeld om achterwaartse compatibiliteit te behouden.

Deze mogelijkheid werd ontwikkeld door [Nass](https://github.com/lanckmann)
### Mogelijkheid: Geometry Checker verplaatst naar gereedschappen van Processing
In lijn met de doelen van [QEP\#236](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/236) dat ernaar streeft om alle methoden voor verificatie/validatie van topologie op elkaar af te stemmen en te uniformeren, is de Geometry Checker nu geïntegreerd in de Toolbox van QGIS Processing.

Deze algoritmes zijn overeenkomstig toegevoegd aan de categorieën "Geometrie controleren" en "Geometrie repareren", en elk algoritme onderhoudt een consistente ervaring met een enkele invoerlaag en twee uitvoerlagen.

Voor Processing algoritmes voor controleren is de uitvoer:
- een laag van hetzelfde type als de invoerlaag met alleen foutieve geometrieën
- een puntenlaag met de locaties van de fouten en informatie (object-ID, deel en nummer punt, etc.)

Voor Processing algoritmes voor repareren is de uitvoer:
- een vaste laag van hetzelfde type als de invoerlaag, met gecorrigeerde objecten overeenkomstig de gekozen methode
- een puntenlaag met de locaties van de fouten en rapport over de reparatie (gerepareerd of niet en een bericht over het verwerkte object)

![](images/entries/f1b235d2feb5b4fe396603fc0f0bbc039f9321fd.png.webp)

Dit werd mogelijk gemaakt door QGIS (Grant OpenSource 2023) en Oslandia

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
### Mogelijkheid: Titel, astitels en logaritmische assen aan plots toegevoegd
Algoritmes voor plotten in het gedeelte "Plotten" van de gereedschappen van Processing zijn uitgebreid met nieuwe functionaliteiten.

De algoritmes Verspreidingsplot, Plot Balkenplot en Boxplot staan nu het specificeren van plottitels toe, alsook astitels als optionele parameters. Als astitels leeg zijn, wordt standaard de naam van het veld gebruikt als de astitel.

Wanneer een enkele spatie wordt ingevoerd, wordt de astitel niet weergegeven (herstelt het huidige gedrag).

Verspreidingsplots ondersteunen nu ook het gebruik van logaritmische schalen op hun assen.

![](images/entries/5c84aa9c7e5fc0f4dcf6ba72b6f721a10380777a.webp)

Deze mogelijkheid werd ontwikkeld door [Florian Neukirchen](https://github.com/florianneukirchen)
### Mogelijkheid: Algoritme Min/max rastergebied
Een nieuw algoritme is toegevoegd dat objecten punt uitneemt, corresponderend met de minimale en maximale pixelwaarden die binnen gebieden van polygonen zijn opgenomen.

De uitvoer zal een object punt bevatten voor de minimale rasterwaarde en een voor de maximale rasterwaarde voor elk individueel gebiedsobject uit een polygonenlaag.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme om min/max pixel uit raster te nemen
Een nieuw algoritme is toegevoegd dat extreme waarden (minimum en maximum) uitneemt uit een opgegeven band van de invoerrasterlaag.

De uitvoer is een vectorlaag die objecten punt bevat voor de geselecteerde extremen, op het middelpunt van de geassocieerde pixel.

Als meerdere pixels in het raster de minimale of maximale waarde delen, dan zal slechts een van deze pixels in de uitvoer worden opgenomen.

Het algoritme gebruikt een rasterdoorloop om efficiënt te blijven in grote rasters en hoeft niet het gehele raster naar het geheugen te lezen

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuw algoritme om afbeeldingen van hoogteprofielen te maken
Een nieuw algoritme voor Processing is gemaakt dat gebruikers de mogelijkheid geeft afbeeldingen van hoogteprofielen te maken. Dit kan effectief worden gebruikt binnen modellen en zal gebruikers in staat stellen om efficiënt hoogteprofielen voor meerdere bogen uit te voeren.

![](images/entries/e1ed046394798d715f1f08a00bc0233668b860b9.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Nieuw algoritme mazen: Oppervlak naar polygoon
Een nieuw algoritme voor Processing is toegevoegd voor een gegevensset met lagen met mazen die een oppervlak van de mazen exporteert naar een uitvoer-MultiPolygoon.

![](images/entries/9c057e645861d7ac5f6e83128845095e60c9cf35.webp)

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Profiel plotten
### Mogelijkheid: Introduceren van een aangepaste tolerantie voor vectorlagen
Gebruikers kunnen een aangepaste tolerantie definiëren door een eigenschap `custom tolerance` toe te voegen aan de hoogte-eigenschappen van de laag. Indien ingesteld, zal dit de globale parameter tolerantie overschrijven die is gedefinieerd in de widget Hoogteprofiel.

![](images/entries/235450d3d9a4e73de42c567c3fc7120b31b5185f.webp)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Gegevensproviders
### Mogelijkheid: SQL uitvoeren vanuit contextmenu laag
Gebruikers kunnen nu SQL direct uitvoeren op ondersteunde lagen vanuit de inhoudsopgave van het project.

![](images/entries/17dd1deefc986be713c4c6b007ed345dbde449d2.webp)

Deze mogelijkheid werd ontwikkeld door [Jürgen Fischer](https://github.com/jef-n)
### Mogelijkheid: Postgres rasterprovider - opslaan rasterstijl database
Dit PR staat opslaan van rasterstijlen in database van PostGIS toe.

Dit werd mogelijk gemaakt door Ocean Winds.

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
### Mogelijkheid: PostgreSQL/PostGIS gegevensprovider - rasteroverzichten verbergen
Voegt een optie toe aan verbinding van PostGIS om geen overzicht van tabellen uit Browser te geven. De lijst van tabellen rasteroverzicht wordt verkregen uit de view van PostGIS raster_overviews.

![](images/entries/401532722-4fab3810-07d9-453e-beb0-9efe1e397bfd.webp)

Dit werd mogelijk gemaakt door Ocean Winds.

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Plug-ins
### Databronnen beheren Tabelopmerking meerregelig
Maakt tabelopmerkingen in Databronnen beheren meerregelig (maakt van originele QLineEdit een QTextEdit). Repareert ook een klein foutje waarbij de opmerking niet goed werd bijgewerkt bij het voor de tweede keer openen van het venster "Tabeleigenschappen".

![](images/entries/395182951-bffa7117-bc19-41a6-952a-adc0ed6187ae.webp)

![](images/entries/395182959-9b082901-56a7-4465-ba46-d1c6c10b896a.webp)

Dit werd mogelijk gemaakt door Ocean Winds.

Deze mogelijkheid werd ontwikkeld door [Jan Caha](https://github.com/JanCaha)
## Programmeerbaarheid
### Mogelijkheid: Klasse QgsGeos weergeven in PyQGIS
GEOS-specifieke functionaliteit die niet wordt weergegeven door de basisklasse QgsGeometryEngine is nu direct toegankelijk via de nieuwe klasse QgsGeos.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Maak waarden Z en M toegankelijk via QgsGeometry.as\_numpy()
In eerdere versies van QGIS zou de methode `QgsGeometry.as_numpy()` alleen coördinaten teruggeven met waarden XY.

In deze uitgave is `as_numpy` anagepast, zodat de coördinaten voor geometrieën met waarden X en/of M zullen worden overeenkomstig teruggegeven als XYZ, XYM of XYZM.

Deze mogelijkheid werd ontwikkeld door [Till Frankenbach](https://github.com/merydian)
### Mogelijkheid: Python-console interactieve help
Door in de Python-console te drukken op F1 zal QGIS automatisch de pagina van de API openen die overeenkomt met:
- geselecteerde tekst, indien aanwezig OF
- woord op de positie van de muis (indien ingeschakeld in de instellingen, zie hieronder) OF
- woord op de positie van de tekstcursor

De documentatie zal worden geopend in het nieuwe gedeelte documentatie dat is toegevoegd aan het paneel voor de gereedschappen Debuggen en ontwikkelen. Zodat ontwikkelaars eenvoudig toegang hebben tot de documentatie van de API voor huidige codeobjecten, direct in de toepassing.

Aanvullende instellingen voor QGIS zijn ook toegevoegd, zodat ontwikkelaars gemakkelijker dit gedrag kunnen aanpassen, zodat het aansluit bij hun werkstroom.

![](images/entries/e5590d57719aa11a7cdefd0014fa56ea830c535c.png.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Allow additional fields in Cloud Storage Connection credentials (or maybe gdal credentials more broadly) | [#60174](https://github.com/qgis/QGIS/issues/60174) | [GDAL PR 11699](https://github.com/OSGeo/gdal/pull/11699) | N/B |
| Add geometryColumnName() method for WFS and OAPIF providers | [#60055](https://github.com/qgis/QGIS/issues/60055) | [PR #60191](https://github.com/qgis/QGIS/pull/60191) | N/B |
| OAPIF: CQL layer filter expression is not used in request | [#60092](https://github.com/qgis/QGIS/issues/60092) | Is geen probleem |  |
| Add support to export to/convert to .gpkg.zip files | [#59959](https://github.com/qgis/QGIS/issues/59959) | [PR #60202](https://github.com/qgis/QGIS/pull/60202) | N/B |
| WMS-T with Time Value YYYY | [#60264](https://github.com/qgis/QGIS/issues/60264) | [PR #60290](https://github.com/qgis/QGIS/pull/60290) | [PR #60307](https://github.com/qgis/QGIS/pull/60307) |
| GDAL Clip Raster by Layer Mask fails when given GeoPackage layer with diacritics (accents) in the name | [#59573](https://github.com/qgis/QGIS/issues/59573) | Oppervlakkig onderzocht |  |
| webconnections xml is invalid due to missing namespace prefix | [#60242](https://github.com/qgis/QGIS/issues/60242) | [PR #60293](https://github.com/qgis/QGIS/pull/60293) | [PR #60353](https://github.com/qgis/QGIS/pull/60353) |
| Unsupported Data Source' adding GDAL AWS S3 raster layers with credential options | [#60288](https://github.com/qgis/QGIS/issues/60288) | [GDAL Commit 4d2e65347ee0207328b14753ee2ea5628ced7d17](https://github.com/OSGeo/gdal/commit/4d2e65347ee0207328b14753ee2ea5628ced7d17) | N/B |
| Create shapefile layer: allow to create Bool fields | [#60324](https://github.com/qgis/QGIS/issues/60324) | [PR #60327](https://github.com/qgis/QGIS/pull/60327) | [PR #60332](https://github.com/qgis/QGIS/pull/60332) |
| [cleanup] Limit number of hardcoded strings for layer type by leveraging QgsMapLayerFactory::typeToString() | Geen | [PR #60360](https://github.com/qgis/QGIS/pull/60360) | N/B |
| Add Raster Layer: do not include credentials in layer name | [#60292](https://github.com/qgis/QGIS/issues/60292) | [PR #60380](https://github.com/qgis/QGIS/pull/60380) | [PR #60387](https://github.com/qgis/QGIS/pull/60387) |
| QgsMapLayer::publicSource(): make it redact/remove GDAL credentials | [#60292](https://github.com/qgis/QGIS/issues/60292) | [PR #60384](https://github.com/qgis/QGIS/pull/60384) | [PR #60400](https://github.com/qgis/QGIS/pull/60400) |
| QgsLayoutExporter: avoid to print the "ERROR 6: The PNG driver does not support update access to existing datasets." GDAL error message | [PR #60208](https://github.com/qgis/QGIS/pull/60208) | [GDAL PR 11708](https://github.com/OSGeo/gdal/pull/11708) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| A semicolon after a custom SQL query makes QGIS generate a broken layer | [#56993](https://github.com/qgis/QGIS/issues/56993) | [PR #60209](https://github.com/qgis/QGIS/pull/60209) | [PR #60230](https://github.com/qgis/QGIS/pull/60230) |
| QGIS Server does not respect datum transformation | [#60216](https://github.com/qgis/QGIS/issues/60216) | [PR #60239](https://github.com/qgis/QGIS/pull/60239) | [PR #60302](https://github.com/qgis/QGIS/pull/60302) |
| [OGR] Fix transactional editing for GPKG/SQLite | [PR #60198](https://github.com/qgis/QGIS/pull/60198) | [PR #60198](https://github.com/qgis/QGIS/pull/60198) | Nee |
| QGIS Server: GetFeatureInfo default tolerance can be too small for line and point features | [#59818](https://github.com/qgis/QGIS/issues/59818) | [PR #60243](https://github.com/qgis/QGIS/pull/60243) | [PR #60259](https://github.com/qgis/QGIS/pull/60259) |
| Missing Update operation for WFS layers without geometry | [#60185](https://github.com/qgis/QGIS/issues/60185) | [PR #60266](https://github.com/qgis/QGIS/pull/60266) | [PR #60271](https://github.com/qgis/QGIS/pull/60271) |
| QGIS Server OGC: Ignoring "Use attribute form settings in GetFeatureInfo response" in GML output | [#59355](https://github.com/qgis/QGIS/issues/59355) | [PR #60281](https://github.com/qgis/QGIS/pull/60281) | Nee |
| First field in attribute table gets cleared on selection when Widget Type Date/Time is set | [#60223](https://github.com/qgis/QGIS/issues/60223) | Kan niet worden gereproduceerd | Nee |
| Data Source Manager connects to all PostgreSQL connections on launch | [#60018](https://github.com/qgis/QGIS/issues/60018) | [PR #60319](https://github.com/qgis/QGIS/pull/60319) | [PR #60326](https://github.com/qgis/QGIS/pull/60326) |
| Virtual layer with JOIN on PostGIS layers not working anymore | [#60104](https://github.com/qgis/QGIS/issues/60104) | Kan niet worden gereproduceerd | Nee |
| Enabling OpenCL acceleration generates erratic behavior in raster operations | [#60077](https://github.com/qgis/QGIS/issues/60077) | [PR #60339](https://github.com/qgis/QGIS/pull/60339) | [PR #60347](https://github.com/qgis/QGIS/pull/60347) |
| QGIS Server OGC: Display name is not provided in GetFeatureInfo json/gml response | [#59353](https://github.com/qgis/QGIS/issues/59353) | [PR #60343](https://github.com/qgis/QGIS/pull/60343) | Nee |
| Source Multipolygon-geometry reads as Polygon-geometry in MapInfo TAB format | [#60396](https://github.com/qgis/QGIS/issues/60396) | [PR #60410](https://github.com/qgis/QGIS/pull/60410) | Nee |
| Geometry checker accepts invalid polygon | [#60464](https://github.com/qgis/QGIS/issues/60464) | Kan niet worden gereproduceerd | Nee |
| Labels with decimal values do not use Locale when decimal is used in a text expression | [#60440](https://github.com/qgis/QGIS/issues/60440) | Niet zeker of dit een bug is, open voor bespreking [PR #60479](https://github.com/qgis/QGIS/pull/60479) | Nee |
| New Connections to OGC Services Hang in Profiles with PostGIS Connections | [#60335](https://github.com/qgis/QGIS/issues/60335) | [PR #60495](https://github.com/qgis/QGIS/pull/60495) | NOG TE DOEN |
| [Regression] OGC-Features API requests do not send Authorization header in v3.40.3 | [#60473](https://github.com/qgis/QGIS/issues/60473) | [PR #60511](https://github.com/qgis/QGIS/pull/60511) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qt6: migration script forces Qt modules which are not covered by qgis.PyQt | [#59351](https://github.com/qgis/QGIS/issues/59351) | [PR #60280](https://github.com/qgis/QGIS/pull/60280) | [PR #60298](https://github.com/qgis/QGIS/pull/60298) |
| Unable to perform zip or export to PDF/image | [#59911](https://github.com/qgis/QGIS/issues/59911) | Is geen probleem | N/B |
| QgisVectorLayerEditUtils addTopologicalPoints causes overlaps | [#58350](https://github.com/qgis/QGIS/issues/58350) | Is geen probleem | N/B |
| QGIS should never poll a PostGIS/WMS/WFS/etc connections unless specifically asked to | [#58303](https://github.com/qgis/QGIS/issues/58303) | Kan niet worden gereproduceerd | N/B |
| Masking labels doesn't work with rule-based labeling | [#46402](https://github.com/qgis/QGIS/issues/46402) | [PR #60325](https://github.com/qgis/QGIS/pull/60325) | [PR #60458](https://github.com/qgis/QGIS/pull/60458) |
| [Clang] Remove some deprecated warnings | Niet gerapporteerd | [PR #60428](https://github.com/qgis/QGIS/pull/60428) | N/B |
| Label mask in Geopackage | [#59245](https://github.com/qgis/QGIS/issues/59245) | Kan niet worden gereproduceerd | N/B |
| QMS plugin crashes in master | [#60286](https://github.com/qgis/QGIS/issues/60286) | [PR #60363](https://github.com/qgis/QGIS/pull/60363) | N/B |
| Sip deprecated annotation makes QGIS crash | Niet gerapporteerd probleem van SIP | [SIP PR #67](https://github.com/Python-SIP/sip/pull/67) | N/B |
| Masking labels doesn't work with rule-based labeling | [#46402](https://github.com/qgis/QGIS/issues/46402) | [PR #60490](https://github.com/qgis/QGIS/pull/60490) | [PR #60509](https://github.com/qgis/QGIS/pull/60509) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Rule based symbology sorting with all fields in legend when only linked maps is ticked | [#60383](https://github.com/qgis/QGIS/issues/60383) | [PR #60536](https://github.com/qgis/QGIS/pull/60536) |  |
| Fix bad overlaps results with QgsRange objects and derivatives (int range, date range...) | niet gerapporteerd | [PR #60139](https://github.com/qgis/QGIS/pull/60139) | [PR #60532](https://github.com/qgis/QGIS/pull/60532) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix leaks in layer definition loading code | niet gerapporteerd | [PR #60650](https://github.com/qgis/QGIS/pull/60650) | In behandeling |
| Fix data-defined overrides ignored in legend text format | [#60628](https://github.com/qgis/QGIS/issues/60628) | [PR #60632](https://github.com/qgis/QGIS/pull/60632) | In behandeling |
| Fix normalising constant in quartic kernel | [#60616](https://github.com/qgis/QGIS/issues/60616) | [PR #60631](https://github.com/qgis/QGIS/pull/60631) | [PR #60633](https://github.com/qgis/QGIS/pull/60633) |
| Fix incorrect compilation of "field IN (...) or field NOT IN (...)" | niet gerapporteerd | [PR #60630](https://github.com/qgis/QGIS/pull/60630) | N/B |
| Lots of memory leak fixes | niet gerapporteerd | [PR #60629](https://github.com/qgis/QGIS/pull/60629) | [PR #60651](https://github.com/qgis/QGIS/pull/60651) |
| [stac] Port more API to use unique_ptr | niet gerapporteerd | [PR #60627](https://github.com/qgis/QGIS/pull/60627) | N/B |
| Fix slow performance of raster image marker | [#51273](https://github.com/qgis/QGIS/issues/51273) | [PR #60604](https://github.com/qgis/QGIS/pull/60604) | Te riskant |
| Fix hang when project with large number of layers has joins to same layers | [#55026](https://github.com/qgis/QGIS/issues/55026) | [PR #60577](https://github.com/qgis/QGIS/pull/60577) | In behandeling |
| Fix some app slowdown when many queries visible in network/db log panel | niet gerapporteerd | [PR #60576](https://github.com/qgis/QGIS/pull/60576) | [PR #60583](https://github.com/qgis/QGIS/pull/60583) |
| Fix render order of symbol layers for filled marker/filled line/arrow subsymbol | niet gerapporteerd | [PR #60575](https://github.com/qgis/QGIS/pull/60575) | [PR #60613](https://github.com/qgis/QGIS/pull/60613) |
| Diamond star marker shape is not closed | niet gerapporteerd | [PR #60574](https://github.com/qgis/QGIS/pull/60574) | [PR #60579](https://github.com/qgis/QGIS/pull/60579) |
| Fix artifacts when rendering filled line symbol | [#59689](https://github.com/qgis/QGIS/issues/59689) | [PR #60554](https://github.com/qgis/QGIS/pull/60554) | [PR #60578](https://github.com/qgis/QGIS/pull/60578) |
| Fix checkbox search widget wrapper for boolean field types | [#60152](https://github.com/qgis/QGIS/issues/60152) | [PR #60552](https://github.com/qgis/QGIS/pull/60552) | [PR #60558](https://github.com/qgis/QGIS/pull/60558) |
| [processing] Use matrix editor panel value if open | [#60442](https://github.com/qgis/QGIS/issues/60442) | [PR #60551](https://github.com/qgis/QGIS/pull/60551) | [PR #60556](https://github.com/qgis/QGIS/pull/60556) |
| [processing] Fix exception when algorithm has no output layers | niet gerapporteerd | [PR #60550](https://github.com/qgis/QGIS/pull/60550) | [PR #60560](https://github.com/qgis/QGIS/pull/60560) |
| Fix status bar coordinate display when project has no CRS | [#56954](https://github.com/qgis/QGIS/issues/56954) | [PR #60549](https://github.com/qgis/QGIS/pull/60549) | [PR #60561](https://github.com/qgis/QGIS/pull/60561) |
| Fixes for layers with a compound crs | [#55173](https://github.com/qgis/QGIS/issues/55173) | [PR #60548](https://github.com/qgis/QGIS/pull/60548) | [PR #60557](https://github.com/qgis/QGIS/pull/60557) |
| [oracle] Fix adding features with null attributes | niet gerapporteerd | [PR #60540](https://github.com/qgis/QGIS/pull/60540) | [PR #60566](https://github.com/qgis/QGIS/pull/60566) |
| [ams] Fix crash when layer ids are not sequential | [#60483](https://github.com/qgis/QGIS/issues/60483) | [PR #60520](https://github.com/qgis/QGIS/pull/60520) | [PR #60538](https://github.com/qgis/QGIS/pull/60538) |
| Fix pasting unsaved changes as temporary scratch layers | [#38913](https://github.com/qgis/QGIS/issues/38913) | [PR #60474](https://github.com/qgis/QGIS/pull/60474) | Te riskant |
| More descriptive expression parsing errors when a function is not found | niet gerapporteerd | [PR #60472](https://github.com/qgis/QGIS/pull/60472) | [PR #60475](https://github.com/qgis/QGIS/pull/60475) |
| Fix paint effects sometimes result in aliased rendering | niet gerapporteerd | [PR #60453](https://github.com/qgis/QGIS/pull/60453) | [PR #60468](https://github.com/qgis/QGIS/pull/60468) |
| More fixes for use of inline data for SVG content | [#60427](https://github.com/qgis/QGIS/issues/60427) | [PR #60448](https://github.com/qgis/QGIS/pull/60448) | [PR #60452](https://github.com/qgis/QGIS/pull/60452) |
| Fix potential crashes when layer tree insertion target group is deleted | niet gerapporteerd | [PR #60446](https://github.com/qgis/QGIS/pull/60446) | [PR #60449](https://github.com/qgis/QGIS/pull/60449) |
| When changing rect text annotation to fixed size mode, use current size | [#59189](https://github.com/qgis/QGIS/issues/59189) | [PR #60424](https://github.com/qgis/QGIS/pull/60424) | [PR #60451](https://github.com/qgis/QGIS/pull/60451) |
| Fix crash in text renderer when wrapping with one word + small rect | [#60256](https://github.com/qgis/QGIS/issues/60256) | [PR #60423](https://github.com/qgis/QGIS/pull/60423) | [PR #60450](https://github.com/qgis/QGIS/pull/60450) |
| [sensorthings] Offer MultiDatastreams as valid expansion targets | [#59531](https://github.com/qgis/QGIS/issues/59531) | [PR #60420](https://github.com/qgis/QGIS/pull/60420) | [PR #60426](https://github.com/qgis/QGIS/pull/60426) |
| [sensorthings] Fix provider does not work with oauth2 config method | [#60407](https://github.com/qgis/QGIS/issues/60407) | [PR #60419](https://github.com/qgis/QGIS/pull/60419) | [PR #60425](https://github.com/qgis/QGIS/pull/60425) |
| [sensorthings] only allow expansion removal from end of table | [#59532](https://github.com/qgis/QGIS/issues/59532) | [PR #60403](https://github.com/qgis/QGIS/pull/60403) | [PR #60405](https://github.com/qgis/QGIS/pull/60405) |
| [sensorthings] Remove option for basic authentication | [#59721](https://github.com/qgis/QGIS/issues/59721) | [PR #60376](https://github.com/qgis/QGIS/pull/60376) | [PR #60421](https://github.com/qgis/QGIS/pull/60421) |
| [sensorthings] Offer geometry for Datastream entities | [#59525](https://github.com/qgis/QGIS/issues/59525) | [PR #60375](https://github.com/qgis/QGIS/pull/60375) | Te riskant |
| [sensorthings] Hide proxy fields for interval fields in filter builder | [#59528](https://github.com/qgis/QGIS/issues/59528) | [PR #60374](https://github.com/qgis/QGIS/pull/60374) | [PR #60457](https://github.com/qgis/QGIS/pull/60457) |
| [sensorthings] Offer choices of non-polygon geometry types for multidatastreams | [#59719](https://github.com/qgis/QGIS/issues/59719) | [PR #60373](https://github.com/qgis/QGIS/pull/60373) | Te riskant |
| [sensorthings] Don't allow expansion back to base entity type | [#59722](https://github.com/qgis/QGIS/issues/59722) | [PR #60372](https://github.com/qgis/QGIS/pull/60372) | [PR #60398](https://github.com/qgis/QGIS/pull/60398) |
| When a layer changes from non-spatial to spatial, update canvas layers | [#59723](https://github.com/qgis/QGIS/issues/59723) | [PR #60371](https://github.com/qgis/QGIS/pull/60371) | Te riskant |
| Ensure that labeling solutions are deterministic | niet gerapporteerd | [PR #60369](https://github.com/qgis/QGIS/pull/60369) | [PR #60388](https://github.com/qgis/QGIS/pull/60388) |
| Remove an extraneous setting of layer scope for vectors | [#60112](https://github.com/qgis/QGIS/issues/60112) | [PR #60367](https://github.com/qgis/QGIS/pull/60367) | Te riskant |
| Use font button in annotation widgets instead of full text format widget | niet gerapporteerd | [PR #60354](https://github.com/qgis/QGIS/pull/60354) | [PR #60368](https://github.com/qgis/QGIS/pull/60368) |
| Fix incorrect annotation HTML shown when clicking between annotations | niet gerapporteerd | [PR #60333](https://github.com/qgis/QGIS/pull/60333) | [PR #60365](https://github.com/qgis/QGIS/pull/60365) |
| Delegate bounding box transformation to proj | [#59821](https://github.com/qgis/QGIS/issues/59821) | [PR #60331](https://github.com/qgis/QGIS/pull/60331) | [PR #60439](https://github.com/qgis/QGIS/pull/60439) |
| Fix logic in pdal indexing task relating to progress updates | niet gerapporteerd | [PR #60312](https://github.com/qgis/QGIS/pull/60312) | [PR #60315](https://github.com/qgis/QGIS/pull/60315) |
| Fix handling of multiple consecutive tabs with HTML text rendering | [#60098](https://github.com/qgis/QGIS/issues/60098) | [PR #60299](https://github.com/qgis/QGIS/pull/60299) | [PR #60422](https://github.com/qgis/QGIS/pull/60422) |
| Explicitly block initQgis, exitQgis from within application | [#60025](https://github.com/qgis/QGIS/issues/60025) | [PR #60297](https://github.com/qgis/QGIS/pull/60297) | Te riskant |
| Fix potential (unlikely) crash in concave hull algorithm | [#59778](https://github.com/qgis/QGIS/issues/59778) | [PR #60296](https://github.com/qgis/QGIS/pull/60296) |  |
| Catch transform errors in QgsWFSProvider::getCapabilities | [#60622](https://github.com/qgis/QGIS/issues/60622) | [PR #60653](https://github.com/qgis/QGIS/pull/60653) | In behandeling |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Zonal histogram unusable results if input raster has many decimal places | [#30822](https://github.com/qgis/QGIS/issues/30822) | [PR#60212](https://github.com/qgis/QGIS/pull/60212) | [PR#60234](https://github.com/qgis/QGIS/pull/60234) |
| PyQGIS / Processing: QgsProcessingParameterMapLayer doesn't respect QgsProcessing.TypeVector | [#56344](https://github.com/qgis/QGIS/issues/56344) | [PR#60213](https://github.com/qgis/QGIS/pull/60213) | [PR#60305](https://github.com/qgis/QGIS/pull/60305) |
| "Layer name" is actually layer title | [#28857](https://github.com/qgis/QGIS/issues/28857) | [PR#60215](https://github.com/qgis/QGIS/pull/60215) | nee |
| WMS layers added with the browser panel ignore image format preferences and default to PNG | [#57666](https://github.com/qgis/QGIS/issues/57666) | [PR#60221](https://github.com/qgis/QGIS/pull/60221) | [PR#60309](https://github.com/qgis/QGIS/pull/60309) |
| There seems to be an issue with the way the algorithm for merging pointclouds works in the model builder | [#57550](https://github.com/qgis/QGIS/issues/57550) | [PR#60236](https://github.com/qgis/QGIS/pull/60236) | [PR#60304](https://github.com/qgis/QGIS/pull/60304) |
| TypeError: unsupported operand type(s) for +: 'Modifier' and 'Key' | [#60063](https://github.com/qgis/QGIS/issues/60063) | [PR#60289](https://github.com/qgis/QGIS/pull/60289) | [PR#60294](https://github.com/qgis/QGIS/pull/60294) |
| "TIN interpolation" and "IDW interpolation" algs always output an ASCII grid (AAIGrid) raster regardless of the output file extension | [#56653](https://github.com/qgis/QGIS/issues/56653) | [PR#60320](https://github.com/qgis/QGIS/pull/60320) | [PR#60351](https://github.com/qgis/QGIS/pull/60351) |
| When editing a Scene connection a new Scene connection is created instead | [#57570](https://github.com/qgis/QGIS/issues/57570) | [PR#60321](https://github.com/qgis/QGIS/pull/60321) | [PR#60329](https://github.com/qgis/QGIS/pull/60329) |
| Spatialite execute SQL issues | [#53904](https://github.com/qgis/QGIS/issues/53904) | [PR#60337](https://github.com/qgis/QGIS/pull/60337) | [PR#60348](https://github.com/qgis/QGIS/pull/60348) |
| Selected sub-item of Join doesn't count for editing | [#29709](https://github.com/qgis/QGIS/issues/29709) | [PR#60338](https://github.com/qgis/QGIS/pull/60338) | [PR#60356](https://github.com/qgis/QGIS/pull/60356) |
| Export Layer(s) Information processing tool suggests unsupported Annotations layer as input | [#49010](https://github.com/qgis/QGIS/issues/49010) | [PR#60341](https://github.com/qgis/QGIS/pull/60341) | [PR#60460](https://github.com/qgis/QGIS/pull/60460) |
| Add BIGTIFF writing option to the georeferencer | [#47362](https://github.com/qgis/QGIS/issues/47362) | [PR#60344](https://github.com/qgis/QGIS/pull/60344) | nee |
| Raster resampling settings are not applied when importing a style | [#56771](https://github.com/qgis/QGIS/issues/56771) | [PR#60358](https://github.com/qgis/QGIS/pull/60358) | [PR#60377](https://github.com/qgis/QGIS/pull/60377) |
| Switching back to Box style scale bar after having switched to Hollow does not reset the fill brush | [#37413](https://github.com/qgis/QGIS/issues/37413) | [PR#60430](https://github.com/qgis/QGIS/pull/60430) | [PR#60471](https://github.com/qgis/QGIS/pull/60471) |
| Failure when writing to vector file: Path to corresponding vector file is not shown | [#49567](https://github.com/qgis/QGIS/issues/49567) | [PR#60433](https://github.com/qgis/QGIS/pull/60433) | [PR#60444](https://github.com/qgis/QGIS/pull/60444) |
| WFS GetFeature request is not using project CRS despite it is offered by WFS | [#44325](https://github.com/qgis/QGIS/issues/44325) | [PR#60476](https://github.com/qgis/QGIS/pull/60476) | [PR#60505](https://github.com/qgis/QGIS/pull/60505) |
| Fix missed import and incorrect call to getThemeIcon() | niet gerapporteerd | [PR#60480](https://github.com/qgis/QGIS/pull/60480) | [PR#60484](https://github.com/qgis/QGIS/pull/60484) |
| "CRS" variable does not work in Processing/expression calculator when defining an output name in batch mode | [#58313](https://github.com/qgis/QGIS/issues/58313) | [PR#60485](https://github.com/qgis/QGIS/pull/60485) | nee |
| [WMS] Not possible to "Ignore reported layer extents" | [#60496](https://github.com/qgis/QGIS/issues/60496) | [PR#60513](https://github.com/qgis/QGIS/pull/60513) | [PR#60529](https://github.com/qgis/QGIS/pull/60529) |
| Alias not exported with algorithm Export to spreadsheet with Value Relation widget | [#59403](https://github.com/qgis/QGIS/issues/59403) | [PR#60542](https://github.com/qgis/QGIS/pull/60542) | [PR#60544](https://github.com/qgis/QGIS/pull/60544) |
| Create "Constant Raster" image size is different compared to "Rasterize" | [#43547](https://github.com/qgis/QGIS/issues/43547) | [PR#60587](https://github.com/qgis/QGIS/pull/60587) | [PR#60608](https://github.com/qgis/QGIS/pull/60608) |
| [browser] "edit" multiple connections at once? | [#31928](https://github.com/qgis/QGIS/issues/31928) | [PR#60639](https://github.com/qgis/QGIS/pull/60639) | [PR#60648](https://github.com/qgis/QGIS/pull/60648) |
| Remove ALL references to plugin | [#56808](https://github.com/qgis/QGIS/issues/56808) | Is geen probleem |  |
| native:savefeatures unable to specify output layer | [#56517](https://github.com/qgis/QGIS/issues/56517) | Kan niet worden gereproduceerd |  |
| Processing Raster Calculator not working in Processing Graphical Modeler | [#37831](https://github.com/qgis/QGIS/issues/37831) | Kan niet worden gereproduceerd, gerepareerd in eigen algoritme |  |
| [processing] Raster calculator in embedded model can't refer to embedded model input | [#42825](https://github.com/qgis/QGIS/issues/42825) | Kan niet worden gereproduceerd, gerepareerd in eigen algoritme |  |
| Raster calculator in graphical modeler reversing layer definitions every time the program is opened | [#33338](https://github.com/qgis/QGIS/issues/33338) | Kan niet worden gereproduceerd, gerepareerd in eigen algoritme |  |
| Modeler and Raster Calculator fail to calc | [#32753](https://github.com/qgis/QGIS/issues/32753) | Kan niet worden gereproduceerd, gerepareerd in eigen algoritme |  |
| Hillshade not created when Save File As is used | [#57247](https://github.com/qgis/QGIS/issues/57247) | Is geen probleem |  |
| Customization: Tools selected with the widget catcher are kept selected even if the dialog is cancelled | [#23199](https://github.com/qgis/QGIS/issues/23199) | [PR#60643](https://github.com/qgis/QGIS/pull/60643) | [PR#60678](https://github.com/qgis/QGIS/pull/60678) |
| Disable default actions for non-spatial tables | [#57916](https://github.com/qgis/QGIS/issues/57916) | [PR#60657](https://github.com/qgis/QGIS/pull/60657) | [PR#60670](https://github.com/qgis/QGIS/pull/60670) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Mathieu Pellerin (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Algorithm postprocessing regression failing to add all but one output to the project | Niet gerapporteerd | [PR #60624](https://github.com/qgis/QGIS/pull/60624) | [PR #60626](https://github.com/qgis/QGIS/pull/60626) |
| Expression's `$id` value can overflow due to wrong int casting | Niet gerapporteerd | [PR #60521](https://github.com/qgis/QGIS/pull/60521) | - |
| Symbol selector dialog not passing on its context to its widget | [#58985](https://github.com/qgis/QGIS/issues/58985) | [PR #60482](https://github.com/qgis/QGIS/pull/60482) | [PR #60667](https://github.com/qgis/QGIS/pull/60667) |
| Missing `cluster_size` variable in expression constructor dialog for cluster symbol | [#58985](https://github.com/qgis/QGIS/issues/58985) | [#58985](https://github.com/qgis/QGIS/issues/58985) | [Commit 068e27c](https://github.com/qgis/QGIS/commit/068e27c0d30babc6582e2db511cd848ec6f0095c) |
| Annotation fixed-size units not set correctly in UI | [#59188](https://github.com/qgis/QGIS/issues/59188) | [PR #60392](https://github.com/qgis/QGIS/pull/60392) | [PR #60397](https://github.com/qgis/QGIS/pull/60397) |
| MBtiles Won't Load Zooms Higher Than 14 | [#59309](https://github.com/qgis/QGIS/issues/59309) | [PR #60391](https://github.com/qgis/QGIS/pull/60391) | [PR #60395](https://github.com/qgis/QGIS/pull/60395) |
| Docked Georeferencer does not reopen if closed | [#60382](https://github.com/qgis/QGIS/issues/60382) | [PR #60390](https://github.com/qgis/QGIS/pull/60390) | [PR #60401](https://github.com/qgis/QGIS/pull/60401) |
| Unable to reorder subdiagrams in stacked diagrams dialog | [#59505](https://github.com/qgis/QGIS/issues/59505) | [PR #60278](https://github.com/qgis/QGIS/pull/60278) | [PR #60519](https://github.com/qgis/QGIS/pull/60519) |
| Unable to save after error in Geometry Validation | [#59688](https://github.com/qgis/QGIS/issues/59688) | [PR #60263](https://github.com/qgis/QGIS/pull/60263) | [PR #60303](https://github.com/qgis/QGIS/pull/60303) |
| Barely visible icon within Python editor in grey theme | [#59772](https://github.com/qgis/QGIS/issues/59772) | [PR #60261](https://github.com/qgis/QGIS/pull/60261) | [PR #60352](https://github.com/qgis/QGIS/pull/60352) |
| Help->About window displays not up-to-date active Python plugins list after activating/deactivating or installing/uninstalling plugins | [#59779](https://github.com/qgis/QGIS/issues/59779) | [PR #60257](https://github.com/qgis/QGIS/pull/60257) | [PR #60270](https://github.com/qgis/QGIS/pull/60270) |
| QGIS' handling of network requests' redirects is broken under Qt6 | [#60235](https://github.com/qgis/QGIS/issues/60235) | [PR #60238](https://github.com/qgis/QGIS/pull/60238) | [PR #60269](https://github.com/qgis/QGIS/pull/60269) |
| Data loss for new rows if a column added after row in attribute table | [#59783](https://github.com/qgis/QGIS/issues/59783) | [PR #60226](https://github.com/qgis/QGIS/pull/60226) | [PR #60310](https://github.com/qgis/QGIS/pull/60310) |
| Non-HTML-formatted annotations have their text deleted every time a setting changes | [#59804](https://github.com/qgis/QGIS/issues/59804) | [PR #60222](https://github.com/qgis/QGIS/pull/60222) | [PR #60334](https://github.com/qgis/QGIS/pull/60334) |
| `outputCrs` is an unknown keyword argument in QgsRasterCalculator | [#59890](https://github.com/qgis/QGIS/issues/59890) | [PR #60218](https://github.com/qgis/QGIS/pull/60218) | - |
| Invalid CRS after writing in QgsRasterCalculator | [#59898](https://github.com/qgis/QGIS/issues/59898) | [PR #60214](https://github.com/qgis/QGIS/pull/60214) | [PR #60253](https://github.com/qgis/QGIS/pull/60253) |
| Data-defined expression for labels "tab distance" doesn't seem to work | [#60004](https://github.com/qgis/QGIS/issues/60004) | [PR #60211](https://github.com/qgis/QGIS/pull/60211) | Niet nodig |
| QGIS crashes due to erroneous extent / invalid CRS in XYZ creation algorithms | [#60069](https://github.com/qgis/QGIS/issues/60069) | [PR #60199](https://github.com/qgis/QGIS/pull/60199) | [PR #60220](https://github.com/qgis/QGIS/pull/60220) |
| The "Selected features only" checkbox is incorrectly disabled / enabled although the layer has / has not selected features | [#60108](https://github.com/qgis/QGIS/issues/60108) | [PR #60197](https://github.com/qgis/QGIS/pull/60197) | [PR #60306](https://github.com/qgis/QGIS/pull/60306) |
| Modeler - Feature iteration does not work | [#60131](https://github.com/qgis/QGIS/issues/60131) | [PR #60194](https://github.com/qgis/QGIS/pull/60194) | [PR #60300](https://github.com/qgis/QGIS/pull/60300) |
| Changes on form are not applied by default | [#60181](https://github.com/qgis/QGIS/issues/60181) | [PR #60192](https://github.com/qgis/QGIS/pull/60192) | [PR #60591](https://github.com/qgis/QGIS/pull/60591) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin (OPENGIS)](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis (LutraConsulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| PointCloud - Converting LAZ to COPC.LAZ: CRS information is lost in COPC.LAZ file | [#59662](https://github.com/qgis/QGIS/issues/59662) | [hobuinc/untwine PR #189](https://github.com/hobuinc/untwine/pull/189) | - |
| Losing the CRS in .copc.laz created from .laz using drag and drop | [#57983](https://github.com/qgis/QGIS/issues/57983) | [hobuinc/untwine PR #189](https://github.com/hobuinc/untwine/pull/189) | - |
| Untwine fails if path contains Swedish characters | [#57913](https://github.com/qgis/QGIS/issues/57913) | [hobuinc/untwine PR #191](https://github.com/hobuinc/untwine/pull/191) | - |
| After loading a Mesh in current master, the Layer styling panel is unusable | [#60083](https://github.com/qgis/QGIS/issues/60083) | Al gerepareerd | - |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Add a CMAKE option to completely disable Python | security@ | [PR #60463](https://github.com/qgis/QGIS/pull/60463) | - |
| Allow snapping point with different CRS | [#59792](https://github.com/qgis/QGIS/issues/59792) | [PR #60456](https://github.com/qgis/QGIS/pull/60456) | [PR #60478](https://github.com/qgis/QGIS/pull/60478) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Germán Carrillo (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.40 backport commit (GitHub) |
| --- | --- | --- | --- |
| Drag and drop of symbology classes is buggy <br> Cannot move legend items when classifying <br> Drag and drop in Point cloud classification is confusing | [#50823](https://github.com/qgis/QGIS/issues/50823) <br> [#55267](https://github.com/qgis/QGIS/issues/55267) <br> [#60559](https://github.com/qgis/QGIS/issues/60559) | [PR #60546](https://github.com/qgis/QGIS/pull/60546) | [PR #60750](https://github.com/qgis/QGIS/pull/60750) |
| (Still) Unable to reorder subdiagrams in stacked diagrams dialog | [#60596](https://github.com/qgis/QGIS/issues/60596) | [PR #60600](https://github.com/qgis/QGIS/pull/60600) | [PR #61126](https://github.com/qgis/QGIS/pull/61126) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS)](https://opengis.ch/)

{{<content-end >}}
