---
HasBanner: false
draft: false
releaseDate: 18-02-2022
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.24
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.24{#changelog324 }
![image1](images/projects/dce49bc182a307d8b4d60cfa0ba8caede109cf69.png)

Datum uitgave 18-02-2022

In memoriam: Deze uitgave is genaamd \'Tisler\' naar een klein Noors eiland dat een favoriete plaats om te bezoeken was van Håvard Tveite, die overleed in mei 2021. Håvard was een bijzonder actief lid van de gemeenschap van QGIS, gaf waardevolle input voor de documentatie, ontwikkelde vele plug-ins, en onderhield de QGIS Resources Sharing Repository om slechts enkele van zijn bijdragen te noemen. De kaart in het welkomstscherm van QGIS 3.24 is een kaart voor oriëntatie die Håvard heeft gemaakt. Hij hield ervan om elk jaar enige tijd door te brengen op Tisler om kaarten te maken.

We willen nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://www.qgis.org) en help een handje!

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u de video met deze mogelijkheden bekijken op YouTube op <https://youtu.be/gVgR4Oxqtkk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/gVgR4Oxqtkk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende leden](https://www.qgis.org/nl/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Gebruikersinterface
### Mogelijkheid: Kaartbereiken direct ophalen vanuit lay-outkaarten en bladwijzers
Dit is een handige tijdspaarder! De widget Extent in QGIS stelt u nu in staat om direct de bereiken van kaarten op te halen en overeen te laten komen vanuit bladwijzers en lay-outs in uw project.

![image3](images/entries/2dc42086879501e4645c8f6b7bbaba0f90fa4164.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Gemakkelijker aangepaste Coördinaten ReferentieSystemen maken 
We hebben een nieuwe optie toegevoegd bij het selecteren van een CoördinatenReferentieSysteem (CRS), die u in staat stelt direct een definitie voor een aangepast CRS in te voeren (van proj- of WKT-tekenreeksen), in plaats van u te eisen dat u specifiek eerst dit aangepaste CRS toevoegt aan de database voor de projecties.

Dit is veel vriendelijker wanneer u slechts een aangepaste projectie wilt definiëren voor slechts één enkel doel, bijv. een overzichtskaart met een projectie die is ontworpen voor een specifieke latitude- en longitude-locatie.

![image4](images/entries/c0053c5fd55a77bc13f8e92bbf9d27ecd57535e4.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Symbologie
### Mogelijkheid: Markering/hash-lijn: verschuiving langs de lijn met \"percentage\" van de lijnlengte (en negatieve verschuivingen!)
U kunt nu de *verschuiving langs lijn* specificeren in het  percentage voor zowel de markerings- als de hash-lijn typen symboollagen. (Deze verschuivingen worden behandeld als percentages van de totale lijnlengte).

Aanvullend, wanneer de instelling *verschuiving langs lijn* voor een markerings- of hash-lijn symboollaag langer is dan de grootte van een **gesloten** ring, zal QGIS de verschuiving nu behandelen als doorlopend langs de ring. Bijvoorbeeld: instellen van de verschuiving op 150% resulteert er in dat de verschuiving wordt behandeld als 50% van de lengte van de gesloten ring.

Tenslotte hebben we het ook mogelijk gemaakt om een negatieve *verschuiving langs lijn* te specificeren voor een gesloten ring. Negatieve verschuivingen worden achterwaarts berekend langs de  ring.

![image5](images/entries/78402d91402744c434c0501a4fa078b686f31251.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Beheren of plaatsingen van eerste/laatste punt van toepassing zijn voor elk deel van meerdelige geometrieën
Deze nieuwe optie voor Symbologie voor de Markerings- en Hash-lijn symbooltypen stellen u in staat te beheren of de opties voor plaatsing van het eerste en laatste punt van toepassing zouden moeten zijn voor elk deel van een meerdelige lijn (of polygoon) individueel, of alleen het allereerste en allerlaatste punt in de gehele meerdelige geometrie.

![image6](images/entries/49ea4f5c6e67426b41fefcdcb38cb3625e03bd34.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie van plaatsing van Markering/hash-lijn \"op punten\" vervangen door \"op binnenste punten\"
De nieuwe modus *Op binnenste punten* plaatst de symbolen alleen op alle **binnenste** punten (d.i. alle punten, behalve het eerste of laatste punt).

Eerder plaatste de oude modus \"Punten\" symbolen zowel op het eerste als laatste punt en alle binnenste punten. Wat het nagenoeg onmogelijk maakte een lijn op te maken met een **afwijkende** markering op het eerste of laatste punt, vergeleken met de rest van de punten van de lijn. Met de nieuwe optie *Op binnenste punten* is het gemakkelijker om een stijl te maken waarbij de lijn een afwijkende markering heeft op het eerste of laatste punt vergeleken met de rest van de punten!

(Deze wijziging is netjes gepaard met de overschakeling naar keuzevakken voor de opties voor plaatsing \-- zorg ervoor om een markering op alle punten weer te geven, dat de opties voor Op eerste punt, Op laatste punt en Op binnenste punten zijn geselecteerd).

![image7](images/entries/4eaf67cc6d084f5f22f2dea6bdac9b62ab0ae25a.webp)

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Opties voor plaatsing in markerings- en hash-lijn symboollagen hebben nu keuzevakken in plaats van elkaar uitsluitende knoppen
Deze verbetering maakt het aanzienlijk eenvoudiger om markerings- (of hash) lijnen te maken met de markeringen op zowel het eerste **en** laatste punt (naast andere nuttige combinaties!)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Beheren van het gebruikte kleurmodel bij het interpoleren van kleurverlopen
Bij het renderen van een kleurverloop zorgen sommige combinaties van verlopende kleuren er voor dat het verloop modderige grijze middentonen weergeeft als de interpolatie wordt uitgevoerd met afzonderlijke kanalen rood/groen/blauw. Een alternatieve benadering is om in plaats van kleuren te interpoleren via hun nuance/saturatie/helderheid of waardekanalen. Deze benadering kan deze ontzadigde middentonen vermijden, wat resulteert in meer visueel prettige verlopen.

We maken het nu mogelijk de specificatie van de kleur in te stellen per stop in een kleurverloop met meerdere stops, om gebruikers het beheer te geven over welke techniek voor interpolatie te gebruiken. Er is ook een optie om de richting te beheren die de interpolatie zou moeten volgen voor de hue-component van een HSL/HSV-kleurspecificatie-interpolatie. Wat kan helpen bij het vermijden van ongewenste interpolatie door het gehele spectrum van de regenboog voor nuance in bepaalde omstandigheden!

Deze [video](https://user-images.githubusercontent.com/1829991/140872101-b6d7dd66-3595-4584-8e1a-0a384f5ec82d.mp4) geeft het verschil weer in middentonen van een kleurverloop, waarbij de RGB-interpolatie resulteert in modderige kleuren, terwijl de HSL/HSV-interpolatie netjes en levendig blijft.

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Miniaturen in grootte wijzigen in dialoogvenster Stijlbeheer
We hebben een nieuwe schuifbalk toegevoegd om de grootte van miniaturen, die worden weergegeven in het dialoogvenster Stijlbeheer, te beheren, omdat deze afmetingen van de miniaturen soms te klein zijn om een goede weergave van een symbool te kunnen geven!

![image8](images/entries/48ee80e3b2307562c724664ce3d59fa8ac7cf477.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: \"Lineburst\"-symbolen
We hebben een nagelnieuw type symboollaag \"Lineburst\" toegevoegd, dat een verloop rendert langs de **breedte** van een lijn (tegengesteld aan de renderer voor geïnterpoleerde lijnen, die een verloop rendert over de **lengte** van een lijn). Het is net als het type Shapeburst-vulling, maar voor lijnen!

![image9](images/entries/e205aa8113a089b9911726a45b0c198e79af0b6b.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR!](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: \"Rasterlijn\"-symbolen
We zijn superenthousiast om u dit nagelnieuwe type lijnsymbool aan te bieden dat het voor u mogelijk maakt een rasterafbeelding te renderen die de vorm van een object lijn volgt. Dit symbooltype opent een geheel nieuwe wereld aan mogelijkheden voor de symbologie van QGIS, en is speciaal nuttig bij het maken van kaarten in een handgetekende of geschilderde stijl.

Opties die beschikbaar zijn om te beheren:
- het pad van de afbeelding (inclusief data-bepaald pad)
- lijnbreedte
- doorzichtbaarheid
- stijlen voor  samenkomsten van lijnen en uiteinden

![image10](images/entries/fa66229ff4db5e654b673579cde7d58dff4cc85d.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Keuze voor gedrag van clippen voor patroonvullingen voor lijnen
U kunt nu beheren hoe lijnen in een symbool voor patroonvulling worden geclipt naar polygoon-vormen. De beschikbare opties omvatten:
- **Alleen clippen tijdens renderen**: lijnen worden gemaakt die het gehele *begrenzingsvak* van het object bedekken die dan worden geclipt tijdens het tekenen. De extremiteiten van de lijn (begin en einde) zullen niet zichtbaar zijn (dit is hetzelfde gedrag las in oudere uitgaven van QGIS).
- **Lijnen clippen vóór renderen**: lijnen worden geclipt naar de *exacte vorm* van de polygoon voorafgaande aan het renderen. De extremiteiten van de lijn (inclusief stijlen van uiteinden, symbolen voor begin/einde van markeringslijnen, etc) zullen zichtbaar zijn, en zouden soms uitgebreid kunnen worden tot buiten de polygoon (afhankelijk van de instellingen voor de lijnsymbolen).
- **Niet clippen**: er wordt in het geheel niet geclipt - de lijnen zullen het gehele begrenzingsvak van het object bedekken

![image11](images/entries/d6195c4a0b58fd7a1f076e7d74dc82d85f453fcc.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeterd renderen van vullingen van lijnpatronen
Bij het exporteren naar een vectorindeling (bijv. PDF of SVG) of wanneer een subsymbool van een lijn dynamische (data-bepaalde) eigenschappen heeft, kunnen we nu automatisch schakelen naar een lijn-per-lijn gebaseerde benadering om de vulling te renderen. (Eerder werd altijd een op een patroon van tegels gebaseerde benadering gebruikt, wat vaak resulteerde in ongewenste artefacten en zichtbare naden in het patroon).

Enkele van de vele voordelen van deze wijziging omvatten:
- Kleinere grootte voor uitvoerbestanden PDF/SVG \-- de vullingen voor lijnpatronen worden niet opgeslagen als rasterafbeeldingen in de uitvoer, dus zal de algehele bestandsgrootte vaak veel kleiner zijn
- PDF/SVG geëxporteerde bestanden zijn gemakkelijker aan te passen in externe toepassingen (zoals Inkscape of Adobe Illustrator) voor nabewerken, omdat elke individuele lijn in het patroon kan worden aangepast.
- Betere kwaliteit uitvoeren van PDF/SVG, omdat de vulling niet afhankelijk is van DPI en pixels er perfect uitziet, ongeacht hoe ver u inzoomt
- Geen zichtbare artefacten onder bepaalde hoeken, afstanden of met bepaalde stijlen van lijnsymbolen

En zelfs nog beter, het opent de deur voor een groot bereik aan nieuwe symboolstijlen, bijvoorbeeld:
- lijnpatronen waarin de individuele lijnen wijzigen van kleur/breedte/streepje/ etc.
- lijnpatronen met symbolen voor markeringslijnen op middelpunt/etc
- effecten van geometrie-generator per lijn, bijv. golvende lijnpatronen, handgetekende lijnstijlen, etc

![image12](images/entries/ddab2e2d054c9535c86e7a94c2045e9ffa2b0b48.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Rotatiehoek voor vullingen van puntpatronen
Nu kunt u een optionele rotatiehoek specificeren voor vullingen van puntpatronen, wat er voor zorgt dat het gehele puntpatroon onder die hoek valt. Dit kan extreem nuttig zijn bij het over elkaar leggen van meerdere vullingen van puntpatronen!

![image13](images/entries/f43cb7d8a69d6765a0873888cbe6cc7f17bb8c51.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Willekeurige verschuivingen van punten voor vullingen van puntpatronen
Deze (optionele) instelling maakt het mogelijk elk punt in een vulling voor puntpatronen willekeurig te verschuiven naar de maximaal gespecificeerde afstand in de X- of Y-richting. U kunt de maximale verschuiving specificeren in millimeters, punten, kaarteenheden, of zelfs eenheden van \"percentage\" (waar percentage relatief is aan de breedte of hoogte van het patroon).

U kunt een optioneel willekeurig aantal zaad instellen om te vermijden dat de symboolpatronen \"heen en weer springen\" rond vernieuwingen van de kaart. Data-bepaalde overrides worden ook ondersteund.

Het belangrijkste verschil tussen deze nieuwe instelling en het bestaande symbooltype *willekeurige markeringsvulling* is dat de willekeurige verschuiving met een puntpatroon quasi-\"normale\" plaatsing van markeringen mogelijk maakt \-- omdat de punten in het patroon effectief worden beperkt tot een raster. Dit maakt het maken van semi-willekeurige vullingen mogelijk die geen lege gebieden of overlappende markeringen hebben. (Tegengesteld aan de willekeurige markeringsvulling, die punten altijd volledig willekeurig plaatst\… wat soms resulteert in visuele clusters van punten of ongewenste lege gebieden).

![image14](images/entries/1ccd4651fd333335c687c1195322df4b49f59b6f.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Instelling Modus Coördinaten verwijzing voor lijnpatronen en puntpatroon vullingsymboollagen
Lijnpatroon en puntpatroon vullingsymboollagen hebben een nieuwe instelling Modus Coördinaten verwijzing om het verankeren van de patronen aan te kunnen passen. Praktisch gesproken maakt dit het mogelijk dat patronen netjes worden uitgelijnd over aanliggende en overlappende objecten.

![relief](https://changelog.qgis.orgimages/entries/e36d0e51676a76cf1655adc1453fd2a2e8a449b6.gif)

![image16](images/entries/afd8b9d9b32f494472a3787323764d9266f6f6ff.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Clippen van markeringen beheren voor vullingen van puntpatronen
Deze nieuwe optie geeft u beheer over hoe markeringen worden geclipt in een vulling van puntpatronen. De beschikbare opties omvatten:
- **Clippen naar vorm**: markeringen zullen worden geclipt op de grens van de vorm, dus \"afgebroken\" markeringen kunnen zichtbaar zijn (hetzelfde gedrag als in eerdere versies van QGIS)
- **Middelpunt markering binnen vorm**: markeringen zullen alleen worden getekend als hun middelpunt binnen de vorm valt, en markeringen zullen **niet** worden geclipt op de grens van de vorm
- **Markering volledig binnen vorm**: markeringen zullen alleen worden getekend als zij volledig binnen de vorm passen
- **Niet clippen**: gehele symbolen voor markering zullen worden getekend als **enig** deel van de markering binnen de vorm valt

![image17](images/entries/4fcff106088f49e8828b8dfcbaa0867c7735aa71.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Expressiefuncties voor het maken van driehoekige/vierkante/gebogen golven
We hebben enkele nieuwe expressiefuncties toegevoegd die \"golvende lijnen\" produceren langs grenzen van geometrieën. Meerdere vormen voor golven zijn beschikbaar, inclusief:
- Golf (sinusachtig)
- Driehoekig
- Vierkant

In aanvulling daarop zijn ook expressiefuncties toegevoegd voor het maken van golven op een normale manier of met willekeur.

Wanneer gebruikt met geometrie-generatoren kunnen deze expressies worden gebruikt voor enkele zeer geavanceerde cartografische effecten!

![image18](images/entries/fc0f7dd38a16926620e0d1d62cce022b9d2618e5.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Labelen
### Mogelijkheid: Eenheden \"Percentage\" voor grootte van de tekstbuffer, verschuiving van de schaduw en straal van vervagen
We maken het nu mogelijk de grootte voor de tekstbuffer, verschuiving van de schaduw en de straal voor vervagen in te stellen als een percentage van de grootte van het lettertype. Dit is gewenst omdat het het mogelijk maakt tekstindelingen te maken waarbij de componenten netjes op schaal worden gebracht als de grootte van de tekst wordt gewijzigd, in plaats van een vaste grootte voor buffer/schaduw te hebben die onafhankelijk moeten worden aangepast als de grootte van de tekst wijzigt.

![image19](images/entries/4e05a38133304694f05b0c70e73750436581f3ef.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Data-bepaalde labelposities voor geometrieën punt
U kunt nu de data-bepaalde plaatsing van labels instellen om te worden gebonden aan een veld voor een geometrie punt of expressie. (Eerdere versies van QGIS stonden alleen data-bepaalde plaatsing toe om te worden ingesteld via twee afzonderlijke numerieke velden X en Y).

Deze wijziging stelt u nu ook in staat om het gereedschap *Label verplaatsen* te gebruiken om de positie van een label, dat is gebonden aan een veld voor een geometrie punt, te wijzigen, wat er voor zorgt dat de nieuwe positie van het label wordt opgeslagen als een geometrie punt in dat attribuut.

![image20](images/entries/0d4347d53e5b2383aab0b5207dcc9dd6317faf3f.webp)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Damiano Lombardi](http://OPENGIS.ch)
### Mogelijkheid: Uitgestrekte tekst voor labels en tekstindelingen
Deze verbetering stelt u in staat uw tekst horizontaal uit te strekken of te comprimeren met een factor percentage. Het is vaak handig voor het aanpassen van de breedte van lettertypen om wat meer tekst te laten passen in labels (met mate gebruikt, dat is\… u kunt zeker het uitstrekken van lettertypen misbruiken met soms verschrikkelijke resultaten!)

**Opmerking:** Deze verbetering vereist Qt 6.3+ of KDE\'s 5.15 fork. (Op andere builds zijn de opties voor uitstrekken verborgen en kunnen ze niet worden ingesteld)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Renderen
### Mogelijkheid: Renderen van lagen als groepen
Dit is een andere spannende cartografische verbetering die een geheel nieuwe arena van symbologie en visualisatie van kaarten in QGIS!

Voorafgaand aan deze verbetering ondersteunde QGIS het groeperen van lagen in de boom met lagen als een manier voor het structureren van projecten, maar deze groepen hadden geen impact op hoe de component-lagen werden gerenderd. In QGIS 3.24 hebben we een nieuwe optie geïntroduceerd die het mogelijk maakt deze groepen lagen te \"*Renderen als groep*\", wat ervoor zorgt dat alle componentlagen worden gerenderd als één enkel vlak object gedurende het renderen van de kaart.

Deze optie is beschikbaar in het dock voor het opmaken van de laag wanneer een groep lagen is geselecteerd. Dit paneel maakt het voor u ook mogelijk het uiterlijk van de groep als één geheel te beheren, met opties voor de algehele doorzichtbaarheid van de groep, modus Samenvoegen, en effecten voor de laag!

Aanvullend, wanneer een laag is opgenomen in een groep die de nieuwe optie *Renderen als groep* heeft geactiveerd, zijn nieuwe modi voor samenvoegen beschikbaar die op \"clippen\" lijkende bewerkingen uitvoeren tijdens het renderen. Dit stelt u in staat enkele zeer krachtige resultaten te bereiken, zoals het clippen van het renderen van de inhoud van één laag met de inhoud van een tweede \"masker\"-laag!

![image21](images/entries/aa14990a802d70d0302c5441ea955248bc1dd40d.webp)

Dit werd mogelijk gemaakt door Andrew Fletcher.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor \"Lijnpatroon\" bij het converteren van laagstijlen van Mapbox GL vectortegels
Door gebruik te maken van de nagelnieuwe rasterlijn symboollaag, rendert QGIS 3.24 nu op de juiste wijze de opmaak van het Mapbox GL lijnpatroon voor nieuw toegevoegde vector tegellagen.

![image22](images/entries/8a1550b27e8d8252b4b79267b0cef1c72ff10659.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Ondersteuning voor achtergrondstijlen voor als Mapbox GL-opgemaakte vector tegellagen
We renderen nu op de juiste wijze vooraf gedefinieerde achtergrondstijlen die aanwezig zijn in als Mapbox GL-opgemaakte vector tegellagen. Dit verbeterd aanzienlijk het uiterlijk van vector tegellagen met donkere stijlen!

![image23](images/entries/38d362b08812fcb3d9129f2f8881d3bf02e77703.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## 3D-objecten
### Mogelijkheid: Respecteren van Z-volgorde bij het renderen van puntenwolken in 2D
We hebben een optie toegevoegd om puntenwolken te renderen overeenkomstig hun Z-volgorde in 2D kaartweergaven. Met de nieuwe optie *van onder naar boven* voor de volgorde ingeschakeld, zullen punten met een hogere Z-waarde lagere punten bedekken -- wat resulteert in het uiterlijk van een echte orthografische foto. Er is ook een optie voor omgekeerd sorteren (*van boven naar beneden*), waarbij de scène verschijnt als deze van onder wordt bekeken.

![image24](images/entries/7edd9bfb77f56b17d2c74c43a8ca1a8ab7456298.webp)

Dit werd mogelijk gemaakt door [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: 3D-weergaven vastzetten/losmaken
We zijn ons ervan bewust dat het gebruiken van vastgezette widgets voor 3D-kaarten onhandig kan zijn. En in veel situaties is het frustrerend deze in grootte te wijzigen en te verplaatsen, omdat zij gevoelig zijn voor opnieuw vastzetten als u hun grootte aanpast! Met QGIS 3.24 hebben we de mogelijkheid toegevoegd om naar 3D-kaarten te schakelen vanuit een vast te zetten widget. Naar een venster op het hoogste niveau (en terug naar een vast te zetten widget), zodat deze kaartweergaven nu kunnen worden beheerd, in grootte kunnen worden aangepast en verplaatst, net als een standaardvenster voor de toepassing.

![image25](images/entries/0ee88178c41fb6f57e0cc9ebe92256c58cfd9f55.gif)

Dit werd mogelijk gemaakt door [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: 3D-kaartweergaven behren
Eerder, als u een 3D-kaartweergave sloot en dan uw project opsloeg, zou de 3D-kaartweergave en al zijn instellingen verloren gaan als u dat project opnieuw zou openen. Dus hebben we in QGIS 3.24 een \"*3D-kaartweergaven beheren*\" toegevoegd die zorgt voor het luisteren, verwijderen, hernoemen en dupliceren van 3D-kaartweergaven in uw projecten!

We hebben ook een nieuw menu \"*3D-kaartweergaven*\" toegevoegd, wat al uw gemaakte 3D-kaartweergaven bevat voor eenvoudige toegang!

![image26](images/entries/4a38d45cc87a5068e3729f2d0091067178975164.webp)

Dit werd mogelijk gemaakt door [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Verbeterde navigatie voor camera
De standaardmodus voor navigatie in eerdere versies van QGIS gedroeg zich soms vreemd bij het verplaatsen, roteren of in-/uitzoomen. Veel moeite werd gestoken in verbeteringen van het beheren van de camera, dus vanaf QGIS 3.24 zou het gedrag van de navigatie van de camera meer natuurlijk aan moeten voelen en soortgelijk zijn aan andere software voor het 3D in kaart brengen.

Voor meer details, bekijk [Fixing terrain and camera issues in 3D](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/215)

Dit werd mogelijk gemaakt door QGIS.org grant (2021).

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Afdruklay-outs
### Mogelijkheid: Mogelijkheden voor renderen van volledige tekst voor lay-out tekstlabels
In oudere uitgaven van QGIS moest u terugvallen op bijzondere trucs zoals het toepassen van HTML en CSS om effecten toe te voegen zoals valschaduwen aan tekst in uw kaartlay-outs. Dat hoeft niet meer! In 3.24 stellen we u nu in staat om ook de bekende eigenschappen van de opties voor het labelen van tekst voor de lay-outs te gebruiken! Dit betekent dat u nu schaduwen, tekstbuffers, achtergronden, ruimten voor letter en woord, etc. gebruiken voor alle tekstitems in uw lay-outs.

![image27](images/entries/42e4f30b9e1adc647a7b7ef774186d8b90374a9f.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Mogelijkheid: Functie geometry_type
De nieuwe functie `geometry_type` geeft het type op het hoogste niveau terug van een geometrie (d.i. \'Punt\', \'Lijn\' of \'Polygoon\').

![image28](images/entries/503ad2cbcbf9b3ac0b46a624fe4d501dbf2db89d.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Sorteren van kruisingen bij overleggen op grootte kruising
We hebben meer verbeteringen toegevoegd aan de functie `overlay_intersects`. De wijziging voegt twee nieuwe optionele argumenten toe aan de bestaande functie:
- **return_details**: alleen geldig indien gebruikt met een expressie. Stel dit in op true om een lijst met kaarten terug te geven die (sleutelnamen tussen aanhalingstekens) de object-\'id\', het \'result\' van de expressie en de waarde \'overlap\' bevatten. De \'radius\' van de maximaal ingeschreven cirkel wordt ook teruggegeven als de doellaag een polygoon is.
- **sort_by_intersection_size**: alleen geldig indien gebruikt met een expressie. Stel dit in op true om de resultaten terug te geven, gesorteerd op de waarde van overlappen in aflopende volgorde.

![image29](images/entries/74ef8569e9142ace7235302fd562a6729821ee7e.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Geef alle namen van laagvelden weer bij het bouwen van expressies
Als een handige tijdbespaarder maken we nu een lijst van alle veldnamen van alle lagen in uw project direct beschikbaar in de Expressiebouwer. Als u dubbelklikt op een van deze veldnamen, zal die worden toegevoegd aan uw expressie als een waarde tekenreeks (`'field_name'`).

![image30](images/entries/e08ee30c934aa44f05b3037531e9502fd0d1feee.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Functie represent_attributes
Deze nieuwe functie geeft een kaart terug met de namen van alle attributen (velden) als de sleutels en de geconfigureerde weergave van de waarden als waarden. De weergegeven waarde voor de attributen is afhankelijk van het geconfigureerde type widget voor elk attribuut.

Kan worden gebruikt met nul, één of meer argumenten:
- Indien aangeroepen zonder parameters zal de functie de weergave van de attributen van het **huidige object** op de huidige laag teruggeven.
- Indien aangeroepen met alleen een parameter \'feature\' zal de functie de weergave van de attributen van het gespecificeerde object op de huidige laag teruggeven.
- Indien aangeroepen met een parameter \'layer\' en een parameter \'feature\' zal de functie de weergave van de attributen van het gespecificeerde object van de gespecificeerde laag teruggeven.

![image31](images/entries/2d81dc010346379fa47fb7f2e301f41d0b7f42fb.webp)

Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Optioneel minimum overlapgebied en cirkelstraal voor overlay_intersection
We hebben twee optionele argumenten toegevoegd aan de expressiefunctie `overlay_intersection()`:
- `min_overlap`: voor polygonen een optioneel minimumgebied in vierkante eenheden van het huidige object voor de kruising (als de kruising resulteert in meerdere polygonen zal de kruising worden teruggegeven als ten minste een van de polygonen een gebied heeft dat groter of gelijk is aan de waarde), voor lijnen een optionele minimumlengte in eenheden van het huidige object (als de kruising resulteert in meerdere lijnen zal de kruising worden teruggegeven als ten minste een van de lijnen een lengte heeft die groter of gelijk is aan de waarde)
- `min_inscribed_circle_radius`: alleen voor polygonen een optionele minimumradius in eenheden voor het huidige object voor de maximum ingeschreven cirkel van de kruising (als de kruising resulteert in meerdere polygonen zal de kruising worden teruggegeven als ten minste een van de polygonen een radius heeft voor de ingeschreven cirkel die groter of gelijk is aan de waarde). Lees meer over het onderliggende predicaat van GEOS, zoals beschreven in de functie voor PostGIS ST_MaximumInscribedCircle.

![image32](images/entries/c94c8c8c3879b90c6c0a602d8d932c505a9a6868.webp)

Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Functie map_prefix_keys
In QGIS 3.24 hebben we een nieuwe functie `map_prefix_keys` toegevoegd die een kaart en een voorvoegsel neemt. De functie geeft een kaart terug waarin alle sleutels worden voorafgegaan door het voorvoegsel.

Voorbeeld: `map_prefix_keys(map('1','one','2','two'), 'prefix-')`

geeft terug: `{ 'prefix-1': 'one', 'prefix-2': 'two' }`

![image33](images/entries/f8f2becdcaaa40fb07b3bb875928b3edcbdedcfc.webp)

Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Functies densify_by_count en densify_by_distance
Deze functionaliteit, die eerder alleen beschikbaar was via de Toolbox van Processing, is nu beschikbaar voor gebruik in expressies!

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Delen van meerdelige geometrieën onafhankelijk roteren met de expressiefunctie \"rotate\"
De nieuwe optie \"per_part\" voor de expressiefunctie \"rotate\" stelt u in staat elk deel van een meerdelige geometrie te roteren rondom het middelpunt van elk deel (in plaats van het middelpunt van de geometrie als geheel). Deze verbetering is ontworpen om te helpen met de symbologie als de functie rotate wordt gebruikt als een cartografisch gereedschap als deel van een symboollaag van een geometriegenerator.

![image34](images/entries/c70899168f010b55fedad4b28e90aab687158a80.gif)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Functie apply_dash_pattern
Deze boeiende nieuwe expressiefunctie past een patroon met streepjes toe op een geometrie,  wat een geometrie MultiLineString teruggeeft waarvan de invoergeometrie langs elke lijn (of ring) is gestreept met een lijnpatroon van streepjes.

Regels kunnen worden ingesteld om te beheren hoe het lijnpatroon wordt aangepast op de uiteinden van de lijn. Als u een regel voor het begin of einde specificeert, dan definieert de optie \"adjustment\" of zowel streepjes als gaten, of alleen grootte voor streepjes of gat worden aangepast om deze regels toe te passen.

U kunt ook een optionele verschuiving voor het patroon instellen om te specificeren hoe ver langs het patroon het resultaat zou moeten beginnen.

![image35](images/entries/ba54e83091593860e9e61425565b085ad082f5ff.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Functie scale
Deze nieuwe expressiefunctie stelt u in staat een geometrie op schaal te brengen (grootte wijzigen). Net als de functie \'rotate\' accepteert de functie een optionele puntpositie om het opschalen te beginnen. Als geen ankerpunt wordt gespecificeerd, dan wordt het opschalen begonnen vanuit het midden van het begrenzingsvak van de geometrie.

![image36](images/entries/6dd5dd5783c501d294a289cfbdabf9ce58b4c481.webp)

Dit werd mogelijk gemaakt door [North Road, met dank aan SLYR](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Filteren op meerdere attributen voor de functie get_feature
We hebben de functie `get_feature` uitgebreid zodat het mogelijk is te filteren op meerdere attributen, door het toevoegen van een optie om een array met filterwaarden door te geven aan de invoer.

Deze mogelijkheid werd ontwikkeld door [Alex](https://github.com/roya0045)
## Gegevensbeheer
### Mogelijkheid: Ondersteuning voor meervoudig bewerken voor relatiebewerker
We hebben een nieuwe modus voor meervoudig bewerken toegevoegd aan de relatiebewerker, wat het mogelijk maakt om snel kindobjecten toe te voegen aan meerdere ouderobjecten. Dit verbetert de efficiëntie voor bewerkingen van het beheren van gegevens, zoals de mogelijkheid om meerdere bomen te selecteren en een item voor onderhoud aan ze allemaal toe te voegen met één klik.

![image37](images/entries/c610c679ea1906d12ca9d4893e60796fd8a3ecab.gif)

Dit werd mogelijk gemaakt door [QGIS Model Baker](https://opengisch.github.io/QgisModelBaker)

Deze mogelijkheid werd ontwikkeld door [Damiano Lombardi, OPENGIS.ch](https://github.com/domi4484)
## Metadata en Metasearch
### Mogelijkheid: Ondersteuning voor OGC API - Records in MetaSearch
We hebben het gereedschap MetaSearch bijgewerkt om ondersteuning te verschaffen voor de [OGC API - Records](https://ogcapi.ogc.org/records) (OARec) standaard. Als deel van de evolutie van OGC API is OGC API - Records de opvolger van OGC:CSW (net als OGC API - Features dat is voor WFS, etc.).

De standaard OGC API - Records is momenteel in ontwikkeling en het huidige tijdpad voor een publieke RFC door OGC is Q1 2022. Onthoud dus dat dit nog slechts een ontwerp is van de specificatie, en dat u er rekening mee moet houden dat de specificatie in de komende maanden nog enigszins kan wijzigen. We moeten in de komende maanden nog steeds uitvinden hoe koppelingen met acties worden afgehandeld (wat een significante verbetering zou zijn, vergeleken met de werkstroom van CSW publish/find/bind).

Toevoegen van deze mogelijkheid aan QGIS is een grote winst voor gemakkelijker zoeken en zal op de lange termijn zowel gebruikers als providers helpen.

![image38](images/entries/5422b5fd0f6fce0bff486b0268a425f7498b1efc.webp)

Deze mogelijkheid werd ontwikkeld door [Tom Kralidis](https://github.com/tomkralidis)
## Formulieren en widgets
### Mogelijkheid: Acties voor indienen van formulieren met HTTP POST
In QGIS 3.24 hebben we twee nieuwe acties voor http POST toegevoegd, soortgelijk aan de bestaande actie `Open` die een verzoek http GET gebruikt.

De twee acties verschillen in de manier waarop de gegevens in het formulier worden gecodeerd:
1. application/x-www-form-urlencoded
2. multipart/form-data

In beide gevallen worden de gegevens doorgegeven aan de actie in een URL-gecodeerde URL.

Een nieuwe functie `url_encode(<map>)` wordt verschaft om een woordenboek (een kaart) te converteren naar de gecodeerde indeling.

Het antwoord van de ingediende URL wordt geopend door `QDesktopServices::openUrl()` te delegeren naar het besturingssysteem nadat de inhoud is opgeslagen in een tijdelijk bestand.

![image39](images/entries/7d4d7ec8aa1eb9c16be7e2e8dad3af8c6fc900a1.webp)

Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Nieuwe knop om de attributentabel te openen met gefilterde objecten
We hebben een nieuwe knop aan het attributenformulier toegevoegd (wanneer in modus Zoeken) die u in staat stelt een attributentabel te openen die is gefilterd om alleen de overeenkomende objecten weer te geven.

![image40](images/entries/1dfb86fa1bec6a73056c703ae49504cc2b61fb7a.gif)

Dit werd mogelijk gemaakt door ARPA Piemonte

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Analyse-gereedschappen
### Mogelijkheid: Methode Rondheid toegevoegd aan boog-polygoon
We hebben een methode \"rondheid\" toegevoegd aan ``QgsCurvePolygon``, wat het mogelijk maakt de \"rondheid\" te berekenen van een objectgebied, gebaseerd op de formule `Rondheid = (4 * pi * gebied) / Perimeter^2`.

Dit omvat ook het toevoegen van een nieuwe  expressie en een gereedschap voor Processing voor het berekenen van rondheid. Het gereedschap voor Processing maakt een nieuwe laag met de rondheid van elk object in een nieuw veld.

![image41](images/entries/0ebc31c2437a3f5595257edd778d3f2fcbca9486.webp)

Deze mogelijkheid werd ontwikkeld door `Antoine Facchini <https://github.com/Koyaani>`__
## Processing
### Mogelijkheid: Labels algoritme uitnemen
Voor 3.24 hebben we een nieuw gereedschap toegevoegd aan de QGIS Toolbox van Processing: \"Labels uitnemen\". Zoals de naam al aangeeft, neemt dit algoritme informatie van labels uit een gerenderde kaart op een specifiek bereik en schaal.

Uitgenomen informatie van labels omvat zijn positie (als geometrieën punt), de geassocieerde laagnaam en object-ID, als ook eigenschappen voor het uiterlijk van het label, zoals rotatie, tekst, uitlijning, lettertype, grootte, gewicht, etc.

Het algoritme maakt ook een standaardstijl zonder symbolen en gelabeld voor de uitvoerlaag die het mogelijk maakt om deze opgeslagen lagen te slepen en neer te zetten in projecten en het label exact te laten tekenen zoals het werd geëxporteerd.

Indien een kaartthema is gespecificeerd bij het uitnemen van labels, zullen de geëxporteerde labels overeenkomen met de zichtbaarheid en symbologie van dat thema. Indien leeggelaten, zullen de huidige zichtbare lagen van het project worden gebruikt.

![image42](images/entries/b2149ac307c233bac0cfcb25166a573c8d55d200.webp)

Dit werd mogelijk gemaakt door [TEKSI](https://www.teksi.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Optionele parameter voor bereik van de uitvoer voor het algoritme GDAL Raster Calculator
Bij het uitvoeren met GDAL 3.3 of nieuwer zal de QGIS Toolbox van Processing het algoritme GDAL Rasterberekeningen het voor u mogelijk maken een optionele parameter \"Bereik uitvoer\". Dit kan behoorlijk nuttig zijn bij het werken met grote gegevenssets, en vermijdt vaak de noodzaak om een tussenliggend geclipt raster te moeten maken, voorafgaand aan het algoritme voor de berekeningen.

![image43](images/entries/7ebbfa145decc6a81678410d53e4d96709d6b2c7.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Optionele parameter voor bereik voor het algoritme GDAL Raster op maskerlaag clippen
We hebben een optionele parameter voor het bereik toegevoegd aan het algoritme GDAL \"Raster op maskerlaag clippen\", wat handig kan zijn bij het werken met grote rastergegevenssets.

![image44](images/entries/08731bc9d93110cb048f5ac8c9256c9b7556694d.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Geschiedenis van Processing opnieuw bewerkt
QGIS 3.24 komt met een gedeeltelijke implementatie van het framework dat wordt beschreven in [QEP 130](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/130), en porteert het log van de geschiedenis van Processing naar dit framework.

Dit is een veel flexibeler benadering om de geschiedenis van Processing op te slaan, omdat het mogelijk is onbeperkte aanvullende informatie over het uitgevoerde gereedschap op te slaan (inclusief alle parameters voor de invoer, resultaten van de uitvoeren, en het volledige tekstlog ook!). Het log van de geschiedenis wordt nu opgeslagen in een database van SQLite, in plaats van het eerder gebruikte tekstbestand, wat meer efficiënte opslag/ophalen/filteren mogelijk maakt.

Het nieuwe framewerk kan potentieel worden uitgebreid tot meer dan alleen Processing - het zou ook kunnen worden gebruikt om de geschiedenis van andere bewerkingen van de gebruiker op te slaan, zoals bewerkingen aan het project, exporteren van lay-outs, etc.!

We zullen dit framework in de toekomst gebruiken om het dialoogvenster voor de geschiedenis van Processing verder uit te breiden. Voor 3.24 gebruiken we het om een aantal nuttige aanvullingen in het dialoogvenster van geschiedenis weer te geven:
- Met rechts klikken op een item in het log heeft een nieuwe optie om de parameters voor de uitvoering te kopiëren als een equivalent van de \"qgis_process\" opdracht voor de opdrachtregel. Wat u een supergemakkelijke manier geeft om opdrachten voor qgis_process te maken om uit te voeren in een CLI.
- Met rechts klikken op een item geeft ook een nieuwe optie \"Als JSON kopiëren\", die een tekenreeks voor JSON kopieert van de parameters voor de invoer en de instellingen van het algoritme.

![image45](images/entries/d20797cd802b8ecea77a8e1e1d96bf5fcc075f86.webp)

Dit werd mogelijk gemaakt door het [Research Institute for Nature and Forest](https://www.inbo.be/en), Vlaamse overheid

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Geavanceerde acties in dialoogvensters van Processing
We hebben nieuwe acties toegevoegd aan het dialoogvenster van Processing inclusief **Als opdracht voor qgis_process kopiëren**, en **Als JSON kopiëren/plakken**. Deze acties samen verzorgen:
- Het gemakkelijk kopiëren van de equivalente opdracht voor PyQGIS om het gereedschap uit te voeren met de parameters die zijn gedefinieerd in het dialoogvenster
- Het gemakkelijk maken van opdrachten voor qgis_process via de gebruikersinterface van QGIS, inclusief enkele lastige parameterwaarden zoals GeoPackage uitvoeren met specifieke lagen
- Een manier voor u verschaffen om de in het dialoogvenster gedefinieerde instellingen te kopiëren in een tekstindelling, zodat u ze gemakkelijk kunt opslaan en ze later opnieuw gebruiken door de waarden te plakken.
- Een manier voor u verschaffen om de instellingen in de indeling JSON, die wordt gebruikt door qgis_process, te kopiëren, zodat het gemakkelijker is om de verwachte indeling te zien, zelfs voor complexe parameters (zoals parameters voor TIN interpolatie).

![image46](images/entries/d372e3463624cffbf522dd16d72d17570a7c511b.webp)

Dit werd mogelijk gemaakt door het [Research Institute for Nature and Forest](https://www.inbo.be/en), Vlaamse overheid

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Exporteren van naar één enkel bestand met algoritme Lay-out van Atlas als PDF exporteren
U kunt nu een lay-out van een atlas exporteren naar één enkel (samengevoegd) PDF-bestand met het algoritme voor Processing \"Lay-out van Atlas als PDF exporteren\".

![image47](images/entries/ced24ad63c3ff2bf6d47b975a965e6a0b9b28466.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Projectmodellen worden weergegeven in het menu Project
We hebben een nieuw submenu toegevoegd aan het \"Project\", dat nu alle modellen van Processing zal vermelden die zijn opgeslagen binnen het huidige project. Dit geeft u een snelle manier om deze projectspecifieke modellen te starten, zowel in modus enkel als in modus batch!

![image48](images/entries/46c8c42ecd96ab046c3e8fcf944607621f43b2f8.webp)

Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Parameter voor bestemming puntenwolk en uitvoer toegevoegd aan Processing
We hebben de ondersteuning voor puntenwolken uitgebreid en verbeterd in Processing, namelijk door:
- Het filteren van lagen van puntenwolken te repareren in de `QgsProcessingMapLayerComboBox`-gebaseerde widget, gebruikt voor parameters
- Toevoegen van een parametertype voor de bestemming van de puntenwolk en typen uitvoer voor puntenwolken met corresponderende widgets. (Momenteel zijn deze nuttig voor 3e-partij providers en plug-ins die uitvoeren voor puntenwolken maken.)
- Weergeven van de nieuw toegevoegde parameters voor uitvoer van de puntenwolk en de bestemming aan de wrapper `algfactory`

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Ondersteuning voor arrayvelden
In QGIS 3.24 hebben van typen arrayvelden een eersteklas burger gemaakt in de Toolbox van Processing! De volgende algoritmes zijn al bijgewerkt om arrayvelden te ondersteunen:
- Algoritme Bijgewerkte velden;
- Algoritme Samenvoegen;
- Algoritme Veld aan attributentabel toevoegen;
- Algoritme Veldberekening; en
- Algoritme Geavanceerde (d.i. Python) veldberekening

Dit werd mogelijk gemaakt door [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Opties voor toepassing en projecten
### Mogelijkheid: argument qgis_process --no-python
Deze nieuwe, optionele parameter voor het gereedschap van de opdrachtregel van qgis_process stelt u in staat Processing te starten zonder ondersteuning voor Python als dat niet is vereist. Dit kan resulteren in significant verbeterde starttijden voor qgis_process startup!

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Afhandeling van \"Slechte lagen\" onderdrukken bij opstarten
We hebben ondersteuning toegevoegd voor een nieuwe vlag voor de opdrachtregel voor het uitvoerbare bestand `qgis`, die u in staat stelt het standaard dialoogvenster dat verschijnt bij het openen van een project met ontbrekende/defecte lagen uit te schakelen:

    [--skipbadlayers]       don't prompt for missing layers
    
Voorbeeld invoeren: `./qgis --skipbadlayers` of `./qgis -B`

Het gebruiksgeval hiervoor is dat gebruikers soms geautomatiseerde of andere processen na het opstarten hebben lopen en niet willen dat het opstartproces wordt onderbroken als er slechte lagen aanwezig zijn in het project. Na het opstarten zal QGIS ontbrekende lagen negeren, maar zij zullen nog wel als defect in de lagenlijst.

Deze mogelijkheid werd voorgesteld door Giuseppe Baiamonte gedurende, en werd live gecodeerd op de QGIS Open Dag van 17 december 2021.

![image49](images/entries/3b60790eb1b2f970940e9280d3eccee6a6f2b8f9.webp)

Deze mogelijkheid werd ontwikkeld door [Tim Sutton](https://github.com/timlinux)
### Mogelijkheid: Parameterwaarden voor qgis_process kunnen worden gespecificeerd als een JSON-object via stdin
We verschaffen nu een mechanisme om complexe invoerparameters voor algoritmes te ondersteunen bij het uitvoeren van het gereedschap qgis_process voor de opdrachtregel.

Om aan te geven dat parameters zullen worden gespecificeerd via stdin moet de opdracht voor qgis_process de volgende indeling volgen
``` 
qgis_process run algid -
```
(met een achterliggende `-` in plaats van de gebruikelijke lijst met argumenten).

Het JSON-object moet een sleutel \"inputs\" bevatten, wat een kaart is van de waarden van de invoerparameters.
``` 
echo "{"inputs": {\"INPUT\": \"my_shape.shp\", DISTANCE: 5}}" | qgis_process run native:buffer -
```
Aanvullend kunnen extra instellingen, zoals eenheden voor de afstand, eenheden voor het gebied, ellipsoïde en projectpad worden opgenomen in dit JSON-object:
``` 
{
    'ellipsoid': 'EPSG:7019',
    'distance_units': 'feet',
    'area_units': 'ha',
    'project_path': 'c:/temp/my_project.qgs'
    'inputs': {'DISTANCE': 5, ..... }
}
```
(Specificeren van invoerparameters via stdin houdt automatisch de uitvoerindeling \--json voor de resultaten in.)

Een grote motivatie voor deze verbetering is om een manier te verschaffen voor de qgis_process R-bibliotheken om parameters, zoals aggregates, te ondersteunen!

Dit werd mogelijk gemaakt door het [Research Institute for Nature and Forest](https://www.inbo.be/en), Vlaamse overheid

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritmes in Python-script direct uitvoeren via qgis_process
Het gereedschap qgis_process voor de opdrachtregel ondersteunt nu het direct uitvoeren van een algoritme in Python-script door het pad naar het .py-bestand te specificeren, in plaats van een algoritme-ID of pad naar een modelbestand!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Vriendelijker fouten van XYZ-rastertegels, WMS- en vectortegels
Serverfouten die optreden tijdens netwerkverzoeken voor XYZ, vectortegel of WMS worden nu direct weergegeven in het venster van QGIS via de berichtenbalk. We hebben deze foutberichten meer beschrijvend en hulpvoller gemaakt, door waar mogelijk de originele tekst van de antwoordfout op te nemen!

![image50](images/entries/006a532d89422cfe5ddb6638ae635384e4f8b8f2.gif)

Dit werd mogelijk gemaakt door [MapTiler](https://www.maptiler.com/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Toegevoegd een out-of-the-box-verbinding naar Mapzen Global Terrain-tegels
QGIS ondersteunt nu ingebouwde ondersteuning voor de indeling Terrarium DEM voor WMS/XYZ-lagen. In aanvulling daarop hebben we nu de out-of-the-box mogelijkheid om Mapzen Global Terrain Tiles, gehost op AWS, toe te voegen. U vindt de nieuwe optie MapZen in het gedeelte XYZ van het paneel Browser. Gebruikers hebben nu een direct toegankelijke globale DEM-bron voor hun projecten!! Bekijk ook <https://registry.opendata.aws/terrain-tiles/>

![image51](images/entries/68cfde8b146eb42d4e75fd089adb2fbe8e7e5012.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: HMAC SHA256 authenticatiemethode voor MapTiler
We hebben een nieuwe authenticatiemethode toegevoegd, specifiek voor MapTiler, die het voor u mogelijk maakt een token te gebruiken dat is versleuteld met HMAC-SHA256.

![image52](images/entries/3f4f8ef8eef605c25bf84e0e86420c6493e02729.webp)

Dit werd mogelijk gemaakt door [MapTiler](https://www.maptiler.com/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Sjabloonparameter {usage} voor XYZ raster- en vectortegels
Voor op XYZ-tegels gebaseerde rasterlagen en voor vectortegel-lagen, maken we het nu mogelijk om sjabloonparameters {usage} in te voegen (in aanvulling op {x}, {y}, {z}). Indien aanwezig zal deze parameter worden vervangen door de context waarin het verzoek wordt gedaan.

De mogelijke waarden voor de context zijn:
- **view** - als het verzoek komt uit 2D- of 3D-kaartvenster
- **export** - als het verzoek komt vanuit het exporteren van een laag of het exporteren van een afdruklay-out voor uitvoer met hoge kwaliteit (kaartvoorbeelden in de ontwerper van afdruklay-out worden geclassificeerd als "view")
- **unknown** - bij het voortkomen uit elke andere context, maar de bron is onbekend

Deze functionaliteit is nuttig voor cliënten van MapTiler, waar zij nodig zijn om de context te herkennen waarin tegels worden gebruikt om gebruikers daarvoor overeenkomstig de rekening te kunnen presenteren.

Dit werd mogelijk gemaakt door [MapTiler](https://www.maptiler.com/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Converteren van WMTS-/XYZ-rastertegels naar terrein (DEM)
In QGIS 3.24 hebben we de mogelijkheid geïntroduceerd om WMTS-/XYZ-rastergegevenssets te converteren naar een rasterlaag met het enkelbandstype float volgens een vooraf gedefinieerd schema voor codering.

U kunt deze optie activeren en een schema voor codering kiezen (voor nu zijn \"MapTiler Terrain RGB\" of \"Terrarium Terrain RGB\" beschikbaar) in de instellingen van de bron voor de verbinding van XYZ of in Databronnen beheren bij het toevoegen van een WMST-laag.

De geselecteerde converter zal de RGB-bronwaarden vertalen naar waarden float voor elke pixel. Na het laden zal de laag worden gepresenteerd als een enkelbands floating point rasterlaag, klaar voor het opmaken met een renderer pseudocolor of schaduw voor heuvels!

![image53](images/entries/6010ce9b5ad8a9d4bc3130b537c74a567be6df23.webp)

Dit werd mogelijk gemaakt door [MapTiler](https://www.maptiler.com/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Typen arrayvelden voor tekenlagen
U kunt nu typen arrayvelden direct toevoegen aan nieuw gemaakte tekenlagen. (Hoewel typen arrayvelden eerder al werden ondersteund door tekenlagen, was er geen manier voor gebruikers om ze toe te voegen bij het maken van een nieuwe tekenlaag.)

![image54](images/entries/57bd4059d12ad5ef94acb42989824a746de92582.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: JSON veldtypen voor nieuwe GeoPackage-lagen
We hebben ondersteuning toegevoegd voor het direct maken van velden voor JSON in nieuw gemaakte lagen van GeoPackage. (Hoewel JSON veldtypen eerder al werden ondersteund door lagen van GeoPackage, was er geen manier voor gebruikers om ze toe te voegen bij het maken van een nieuwe laag.)

![image55](images/entries/a96a3edb24bb7e7132fdb353b77ea1a1c98ed9ef.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Overschrijven door type tekengescheiden tekst en andere verbeteringen
We hebben enige liefde gegeven aan de provider voor tekengescheiden tekst in 3.24, met verscheidene verbeteringen die omvatten:

**Ondersteuning en automatische herkenning van type Booleaanse waarde**

Gegevenstypen van Booleaanse waarde zijn nu eersteklas burgers, die automatisch worden herkend als alle records in een kolom een van de volgende waarden bevatten (niet hoofdletter-gevoelig):
- t/f
- true/false
- yes/no
- 0/1

Velden met Booleaanse waarden worden nu ook herkend in een CSVT-bestand, een indeling GDAL/GeoCSV bijv.

`Integer(Boolean)`

U kunt ook aangepaste weergaven van tekenreeksen voor TRUE/FALSE toevoegen (bijvoorbeeld een gelokaliseerde waarde \"ja\"/\"nee\").

**Kolom type overschrijven**

Kolomtypes worden automatisch bepaald (door een initieel beperkte scan van het bestand voor directe terugkoppeling, gevolgd door een volledige scan van het bestand die in een afzonderlijke thread wordt uitgevoerd om de GUI niet te blokkeren en is door de gebruiker te onderbreken), de types worden in de GUI weergegeven als combinatievakken en de gebruiker kan de automatisch bepaalde types overschrijven.

**Verbeterde ondersteuning voor CSVT**.

CoordX, CoordY, Point(X/Y), WKT worden nu herkend zoals gespecificeerd in <https://giswiki.hsr.ch/GeoCSV>

![image56](images/entries/998275eaa241752a63c889c4c428948f6702d7ed.webp)

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Nieuw authenticatiemethode voor op HTTP-header gebaseerde authenticatie
Een nieuwe authenticatiemethode is beschikbaar voor netwerkverzoeken die gebruikergedefinieerde HTTP-header authenticatie ondersteunen. Meerdere aangepaste headers kunnen in deze verzoeken worden opgenomen.

Dit is nuttig in verscheidene scenario's. Zoals wanneer een WMS een API-sleutel vereist die moet worden gebruikt in een http-header waarin de sleutel voor de header `X-API-KEY` is. Die nu kan worden opgenomen in verzoeken vanuit QGIS om te authenticeren in het WMS-eindpunt.

![image57](images/entries/72f6e13c97be1a5e3e4d3aafdee9eef6d77a5bfe.webp)

Deze mogelijkheid werd ontwikkeld door [Tom C](https://github.com/Cumminsc9)
### Mogelijkheid: Secundaire PostGIS-geometriekolommen weergeven als verwezen geometrieën
Zoals besproken in [dit issue](https://github.com/qgis/QGIS/pull/45007), hebben we ondersteuning toegevoegd voor het weergeven van aanvullende geometriekolommen voor de provider Postgres als QgsReferencedGeometry. Dit maakt meer efficiënte interactie mogelijk met aanvullende geometriekolommen via de API. Bijvoorbeeld bij het plaatsen van labels kan de aanvullende geometriekolom worden gebruikt in plaats van de objectgeometrie. De velden zullen worden weergegeven als `WKT [CRS User-Friendly Identifier]` in de attributentabel.

Dit kan worden gebruikt in expressies en op de tab voor eigenschappen voor het plaatsen van labels waar u het plaatsen van de labels kunt koppelen aan de tweede geometriekolom met de eigenschap Point. In het geval dat u het al gebruikte voor labelen, zal de tweede kolom automatisch worden bijgewerkt wanneer u het gereedschap Verplaatsen gebruikt en het type kolom Geometrie is. Als het type kolom tekst is, zou u die ook als een tweede kolom kunnen gebruiken door te doen bijv.

    geom_from_wkt("my wkt string field")
    
In dat geval zal de kolom echter Alleen-lezen zijn.

Dus bijv. nu in expressies Als u een tweede geometriekolom hebt, kunt u doen:

    buffer("my_second_geom_column", 10)
    
en het zal werken.

{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### Waarschuwing
Dit wijzigt het gedrag van bestaande projecten.

{{<rich-content-end >}}

{{<rich-box-end >}}

![image58](images/entries/2f2169f6a9927916d3841b63333982a5417a3a0c.webp)

Dit werd mogelijk gemaakt door [OPENGIS.ch](https://www.opengis.ch)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn, OPENGIS.ch](https://github.com/m-kuhn)
## QGIS Server
### Mogelijkheid: Beter beheer toestaan van de stroom met antwoorden vanuit serverfilters
Nieuwe filters staan beheer toe van de aanroepketen door nieuwe filter callbacks te implementeren die het mogelijk maken een beheerswaarde terug te geven voor het stoppen met doorgaan. Dit maakt beter beheer mogelijk van gestroomde gegevens en stroom met antwoorden.
- Vervallen `bool QgsFilter::onRequestReady()`, `bool QgsFilter::onSendResponse()`, `bool QgsFilter::onResponseComplete()`
- Nieuwe methoden toegevoegd `bool QgsFilter::onRequestReady()`, `bool QgsFilter::onSendResponse()`, `bool QgsFilter::onResponseComplete()` die booleaanse waarden teruggeven voor het beheren van de gegevensstroom
- Afhandelen van stroombeheer in `QgsFilterResponseDecorator::flush()`

Deze mogelijkheid werd ontwikkeld door [David Marteau](https://github.com/dmarteau)
## Belangrijke reparaties
### Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Wrong raster projection on HIDPI screens | [#46882](https://github.com/qgis/QGIS/issues/46882) | [PR #46931](https://github.com/qgis/QGIS/pull/46931) | NOG TE DOEN |
| Data Source Manager title not translatable | [#46929](https://github.com/qgis/QGIS/issues/46929) | [PR #46932](https://github.com/qgis/QGIS/pull/46932) | NOG TE DOEN |
| QGIS 3.22 - Identical map names in print composer | [#46927](https://github.com/qgis/QGIS/issues/46927) | Werkt bij mij wel |  |
| Bold and italic attributes of labels that reinitialize | [#46896](https://github.com/qgis/QGIS/issues/46896) | Werkt bij mij wel |  |
| NameError: name \'QGISAPP\' is not defined when using stop_app() | [#46883](https://github.com/qgis/QGIS/issues/46883) | Werkt voor mij op Linux/master, misschien alleen op Windows |  |
| Virtual layer not loaded correctly after re-opening a project | [#46834](https://github.com/qgis/QGIS/issues/46834) | [PR #46938](https://github.com/qgis/QGIS/pull/46938) | NOG TE DOEN |
| QGIS crashes while calling readLayerXml() | [#46741](https://github.com/qgis/QGIS/issues/46741) | Werkt bij mij wel |  |
| Crash when changing orientation of page in layout | [#46575](https://github.com/qgis/QGIS/issues/46575) | [PR #46972](https://github.com/qgis/QGIS/pull/46972) | NOG TE DOEN |
| \"sort\" funcionality of attributes table sort numeric fields as text | [#34935](https://github.com/qgis/QGIS/issues/34935) | [PR #47035](https://github.com/qgis/QGIS/pull/47035) | NOG TE DOEN |
| OAPIF: api-key not included when requesting /collections endpoint | [#46535](https://github.com/qgis/QGIS/issues/46535) | [PR #47145](https://github.com/qgis/QGIS/pull/47145) | NOG TE DOEN |
| XML notation if missing from tooltips in vector file writer dialog | [#46508](https://github.com/qgis/QGIS/issues/46508) | [PR #47148](https://github.com/qgis/QGIS/pull/47148) | NOG TE DOEN |
| Ignore out of range option in interpolated symbol renderer creates artifacts if start value is out of range | [#46362](https://github.com/qgis/QGIS/issues/46362) | [PR #47174](https://github.com/qgis/QGIS/pull/47174) | NOG TE DOEN |
| start width \> end width is ignored when using the \"exact\" color interpolation method | [#46371](https://github.com/qgis/QGIS/issues/46371) | [PR #47195](https://github.com/qgis/QGIS/pull/47195) | NOG TE DOEN |
| QGIS Layouts: using \"Data defined override\" for HTML Source URL not working | [#34395](https://github.com/qgis/QGIS/issues/34395) | werkt bij mij (gesloten - geen bug) |  |
| (Un)force hide form in relation widget | [#47226](https://github.com/qgis/QGIS/issues/47226) | [PR #47245](https://github.com/qgis/QGIS/pull/47245) | NOG TE DOEN |
| Oauth2 authentication protocol does not honors the defined port number in redirect URL in QGIS 3.22.1 | [#46354](https://github.com/qgis/QGIS/issues/46354) | werkt bij mij (open gelaten) |  |
| HTML/String-ish QByteArray as result of expression function breaks expression preview display | [#46174](https://github.com/qgis/QGIS/issues/46174) | [PR #47229](https://github.com/qgis/QGIS/pull/47229) | NOG TE DOEN |
| Raster layer exported to GeoPackage with the character \'ß\' in the name is not immediately loaded in the project | [#45965](https://github.com/qgis/QGIS/issues/45965) | werkt bij mij (gesloten) |  |
| Layout Attribute Table sorting does not work in Print Layouts when column name has spaces | [#43744](https://github.com/qgis/QGIS/issues/43744) | [PR #47249](https://github.com/qgis/QGIS/pull/47249) | NOG TE DOEN |
| Incorrect scale range legend after applying logarithmic graduated symbology to a vector layer | [#45454](https://github.com/qgis/QGIS/issues/45454) | [PR #47259](https://github.com/qgis/QGIS/pull/47259) | Riskant? |
| fix server crash | niet gerapporteerd | [PR #47271](https://github.com/qgis/QGIS/pull/47271) | NOG TE DOEN |
| Load QGIS project from command line from a PostgreSQL project | [#47270](https://github.com/qgis/QGIS/issues/47270) | [PR #47272](https://github.com/qgis/QGIS/pull/47272) | NOG TE DOEN |
| Aggregate function with filter doesn\'t work in layout manager | [#45552](https://github.com/qgis/QGIS/issues/45552) | Werkt bij mij (gesloten) |  |
| Value map widget: \"value\"/\"description\" inconsistency when table added to print layouts | [#41798](https://github.com/qgis/QGIS/issues/41798) | [PR #47300](https://github.com/qgis/QGIS/pull/47300) | NOG TE DOEN |
| Missing entries in attributetable in layout with atlas at page break | [#44086](https://github.com/qgis/QGIS/issues/44086) | [PR #47303](https://github.com/qgis/QGIS/pull/47303) | NOG TE DOEN |
| Server OAPIF: bbox filter isn\'t working if data source CRS is not EPSG:4326/WGS84 | [#47302](https://github.com/qgis/QGIS/issues/47302) | [PR #47318](https://github.com/qgis/QGIS/pull/47318) | NOG TE DOEN |
| Drag & Drop designer control visibility by expression with field IS NOT NULL doesn\'t work if the field is configured with html | [#47363](https://github.com/qgis/QGIS/issues/47363) | [PR #47432](https://github.com/qgis/QGIS/pull/47432) | Riskant? |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| DistanceWithin algorithm failing with PostgreSQL provider | [#45352](https://github.com/qgis/QGIS/issues/45352) | [PR #46971](https://github.com/qgis/QGIS/pull/46971) | [PR #47076](https://github.com/qgis/QGIS/pull/47076) |
| GH_WORKSPACE -\> QGIS_WORKSPACE | [PR #47060](https://github.com/qgis/QGIS/pull/47060) |  |  |
| Improve documentation about running tests | [PR #47057](https://github.com/qgis/QGIS/pull/47057) |  |  |
| Use variables to set postgresql connection config in authmanager test | [PR #47059](https://github.com/qgis/QGIS/pull/47059) |  |  |
| Re-use possibly cached postgis_version from pgsql description method | [PR #47393](https://github.com/qgis/QGIS/pull/47393) | [PR #47401](https://github.com/qgis/QGIS/pull/47401) |  |
| Trust primary key of layers setup by DBManager TopoViewer plugin | [#47389](https://github.com/qgis/QGIS/issues/47389) | [PR #47390](https://github.com/qgis/QGIS/pull/47390) | [PR #47403](https://github.com/qgis/QGIS/pull/47403) |
| Improved debugging output in QgsPostgresConn class | [PR #47396](https://github.com/qgis/QGIS/pull/47396) |  |  |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS 3.21.0: preset transform required \"nehpgn.gsb\" but downloads \"nehpgn.tif\" which does not work | [#45470](https://github.com/qgis/QGIS/issues/45470) | [PR #46918](https://github.com/qgis/QGIS/pull/46918) | [PR #46952](https://github.com/qgis/QGIS/pull/46952) |
| Raster layer misaligns when bbox bigger than projected raster layer | [#34518](https://github.com/qgis/QGIS/issues/34518) | [PR #46939](https://github.com/qgis/QGIS/pull/46939) | [PR #46956](https://github.com/qgis/QGIS/pull/46956) |
| Filter for WFS layer: The \"Tables\" button is missing | [#46887](https://github.com/qgis/QGIS/issues/46887) | Is geen probleem |  |
| Something simpler than SQL to filter a WFS layer | [#46888](https://github.com/qgis/QGIS/issues/46888) | [PR #47056](https://github.com/qgis/QGIS/pull/47056) | [PR #47132](https://github.com/qgis/QGIS/pull/47132) |
| renaming/deleting columns takes a lot of time on large vectors | [#47012](https://github.com/qgis/QGIS/issues/47012) | [GDAL PR 5193](https://github.com/OSGeo/gdal/pull/5193) | [GDAL PR 5204](https://github.com/OSGeo/gdal/pull/5204) |
| Opening a Vector Geopackage in QGIS alters its file even when no changes are done by user | [#23991](https://github.com/qgis/QGIS/issues/23991) | [PR #47098](https://github.com/qgis/QGIS/pull/47098) | [PR #47301](https://github.com/qgis/QGIS/pull/47301) |
| MapInfo CRS not correctly recognized | [GDAL issue #5217](https://github.com/OSGeo/gdal/issues/5217) | [PR #47149](https://github.com/qgis/QGIS/pull/47149) | [PR #47157](https://github.com/qgis/QGIS/pull/47157) |
| Crash exporting dxf using \"Symbol layer symbology\" | [#46245](https://github.com/qgis/QGIS/issues/46245) | [PR #47277](https://github.com/qgis/QGIS/pull/47277) | [PR #47297](https://github.com/qgis/QGIS/pull/47297) |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Deze problemen werden opgelost door [Even Rouault](https://www.spatialys.com/)
### Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Trying to add GPKG from data source manager crashes QGIS master | [#46463](https://github.com/qgis/QGIS/issues/46463) | [PR #46928](https://github.com/qgis/QGIS/pull/46928) | niet relevant |
| Display name in layer properties is not automatically filled | [#28353](https://github.com/qgis/QGIS/issues/28353) | [PR #47016](https://github.com/qgis/QGIS/pull/47016) |  |
| Fixes to QgsGeometry::addPart + new test cases | niet gerapporteerd | [PR #47009](https://github.com/qgis/QGIS/pull/47009) |  |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Bugs fixed by [Denis Rouzaud](http://www.opengis.ch/)
### Deze problemen werden opgelost door Alex Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Layout picture: data-defined svg parameters should be disabled for incompatible pictures | [#26524](https://github.com/qgis/QGIS/issues/26524) | [PR #46976](https://github.com/qgis/QGIS/pull/46976) |  |
| TypeError in MetaSearch when adding WFS data | [#46135](https://github.com/qgis/QGIS/issues/46135) | [PR #46993](https://github.com/qgis/QGIS/pull/46993) | [PR #47003](https://github.com/qgis/QGIS/pull/47003) |
| Split Vector Layer algorithm does not export both null and empty values | [#38105](https://github.com/qgis/QGIS/issues/38105) | [PR #46997](https://github.com/qgis/QGIS/pull/46997) | [PR #47030](https://github.com/qgis/QGIS/pull/47030) |
| data source manager not opening with correct sub menu for point cloud datasources | [#42881](https://github.com/qgis/QGIS/issues/42881) | [PR #46998](https://github.com/qgis/QGIS/pull/46998) | [PR #47002](https://github.com/qgis/QGIS/pull/47002) |
| SLD import doesn\'t recognize html enconding in ttf font references | [#27263](https://github.com/qgis/QGIS/issues/27263) | [PR #46975](https://github.com/qgis/QGIS/pull/46975) | [PR #47040](https://github.com/qgis/QGIS/pull/47040) |
| Error opening data loader dialog from MetaSearch | [#40490](https://github.com/qgis/QGIS/issues/40490) | Werkt bij mij wel |  |
| Display name in layer properties is not automatically filled | [#28353](https://github.com/qgis/QGIS/issues/28353) | [PR #46978](https://github.com/qgis/QGIS/pull/46978) |  |
| No way to add mbtiles file-based MVT package except drag and drop | [#36449](https://github.com/qgis/QGIS/issues/36449) | [PR #47028](https://github.com/qgis/QGIS/pull/47028) | [PR #47068](https://github.com/qgis/QGIS/pull/47068) |
| \"GDAL rasterize overwrite with attribute\" does not refresh/reload output | [#45729](https://github.com/qgis/QGIS/issues/45729) | [PR #47055](https://github.com/qgis/QGIS/pull/47055) | [PR #47105](https://github.com/qgis/QGIS/pull/47105) |
| Delete Column in Matrix Parameter in Graphic Modeler not Working | [#45694](https://github.com/qgis/QGIS/issues/45694) | [PR #47064](https://github.com/qgis/QGIS/pull/47064) | [PR #47067](https://github.com/qgis/QGIS/pull/47067) |
| Wrong signature of the QgsProcessingParameterMeshDatasetGroups when exporting to Python | niet gerapporteerd | [PR #47152](https://github.com/qgis/QGIS/pull/47152) | [PR #47156](https://github.com/qgis/QGIS/pull/47156) |
| Error message when GRASS tools cannot be run is (now) wrong | [#46052](https://github.com/qgis/QGIS/issues/46052) | [PR #47163](https://github.com/qgis/QGIS/pull/47163) |  |
| \"Ignore invalid input features\" processing setting location is misleading | [#42557](https://github.com/qgis/QGIS/issues/42557) | [PR #47163](https://github.com/qgis/QGIS/pull/47163) |  |
| Inconsistent number of decimal places in Identify tool | [#27929](https://github.com/qgis/QGIS/issues/27929) | [PR #47173](https://github.com/qgis/QGIS/pull/47173) |  |
| qgis_process is not showing algorithm providers installed via a python plugin | [#41120](https://github.com/qgis/QGIS/issues/41120) | [PR #47258](https://github.com/qgis/QGIS/pull/47258) | [PR #47263](https://github.com/qgis/QGIS/pull/47263) |
| Unable to delete files .shp and .dbf using python code (removeMapLayers, deleteShapeFile) | [#39428](https://github.com/qgis/QGIS/issues/39428) | Werkt bij mij wel |  |
| QgsProcessingParameterFile extension option | [#45633](https://github.com/qgis/QGIS/issues/45633) | Is geen probleem |  |
| Make the labels \"edit rule\" widget a real dialog with buttons | [#36761](https://github.com/qgis/QGIS/issues/36761) | [PR #47305](https://github.com/qgis/QGIS/pull/47305) |  |
| Edit form python editor tabs/spaces confusion | [#46988](https://github.com/qgis/QGIS/issues/46988) | [PR #47345](https://github.com/qgis/QGIS/pull/47345) | [PR #47352](https://github.com/qgis/QGIS/pull/47352) |
| Error when making buffer from empty layer with \'Dissolve result\' option checked | [#46396](https://github.com/qgis/QGIS/issues/46396) | [PR #47348](https://github.com/qgis/QGIS/pull/47348) | [PR #47384](https://github.com/qgis/QGIS/pull/47384) |
| QGIS does not replace commas in layer names when exporting to DXF (so is incompatible with AutoCAD) | [#47381](https://github.com/qgis/QGIS/issues/47381) | [PR #47418](https://github.com/qgis/QGIS/pull/47418) | [PR #47430](https://github.com/qgis/QGIS/pull/47430) |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Deze problemen werden opgelost door Alex Bruy
### Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fixes WFS EXP_FILTER parsing in GetFeature request | [mailing list](https://www.mail-archive.com/qgis-user@lists.osgeo.org/msg50029.html) | [PR #47029](https://github.com/qgis/QGIS/pull/47029) | Te riskant |
| Fix output filename when a raster is saved in a format without extension | niet gerapporteerd | [PR #46992](https://github.com/qgis/QGIS/pull/46992) | NOG TE DOEN |
| WFS GetFeature document and exceptions | niet gerapporteerd | [PR #47198](https://github.com/qgis/QGIS/pull/47198) | NOG TE DOEN |
| Exluding a print layout in project propteries -\> server do not avoid that a GetPrint request can be done for that layout | [#46140](https://github.com/qgis/QGIS/issues/46140) | [PR #47199](https://github.com/qgis/QGIS/pull/47199) | NOG TE DOEN |
| Server: Can\'t enable WFS3 API update endpoint (PUT/PATCH) on layers without geometry | [#46119](https://github.com/qgis/QGIS/issues/46119) | Werkt bij mij wel |  |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Deze problemen werden opgelost door [Paul Blottiere](https://hytech-imaging.fr/)
### Reparaties van problemen door Matthias Kuhn
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix HTTP Post with MultiPart | [#46989](https://github.com/qgis/QGIS/issues/46989) | [PR #47006](https://github.com/qgis/QGIS/pull/47006) | niet nodig |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Bugs fixed by [Matthias Kuhn](https://www.opengis.ch/)
### Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Add .tsv extension to delimited text supported files filter | gerapporteerd on YouTube screencast | [PR #47181](https://github.com/qgis/QGIS/pull/47181) | In behandeling |
| Fix line anchor placements are reversed for labels which sit below lines | niet gerapporteerd | [PR #47181](https://github.com/qgis/QGIS/pull/47181) | [PR #47181](https://github.com/qgis/QGIS/pull/47181) |
| Fix incorrect return code from QgsProcessingModelAlgorithm::fromFile when file does not exist | niet gerapporteerd | [PR #47161](https://github.com/qgis/QGIS/pull/47161) | [PR #47162](https://github.com/qgis/QGIS/pull/47162) |
| Fix many georeferencer regressions | meerdere | niet gerapporteerd | In behandeling |
| Avoid some unwanted \"unhandled exception\" message boxes which can pop up while moving the mouse | gerapporteerd on YouTube screencast | [PR #47138](https://github.com/qgis/QGIS/pull/47138) | [PR #47154](https://github.com/qgis/QGIS/pull/47154) |
| Don\'t use custom palette in crash handler dialog, this results in unreadable text on dark themes | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47110](https://github.com/qgis/QGIS/pull/47110) | [PR #47136](https://github.com/qgis/QGIS/pull/47136) |
| Don\'t slightly colorise the icons for selected items in lists | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47133](https://github.com/qgis/QGIS/pull/47133) | niet geschikt |
| Fix python exception raised after running in-place algorithm which requires no parameters | gerapporteerd on YouTube screencast | [PR #47108](https://github.com/qgis/QGIS/pull/47108) | [PR #47130](https://github.com/qgis/QGIS/pull/47130) |
| Fix labelling shown for features out of range of temporal controller dates | [#45160](https://github.com/qgis/QGIS/issues/45160) | [PR #47119](https://github.com/qgis/QGIS/pull/47119) | [PR #47126](https://github.com/qgis/QGIS/pull/47126) |
| Fix line dependent orientation rendering of curved labels | [#45051](https://github.com/qgis/QGIS/issues/45051) | [PR #47118](https://github.com/qgis/QGIS/pull/47118) | [PR #47137](https://github.com/qgis/QGIS/pull/47137) |
| When processing is initialized in external scripts, ensure the GRASS, SAGA and OTB providers are included by default | [#45935](https://github.com/qgis/QGIS/issues/45935) | [PR #47114](https://github.com/qgis/QGIS/pull/47114) | [PR #47121](https://github.com/qgis/QGIS/pull/47121) |
| Show descriptive error when label rotation tool cannot be used because of invalid expressions | [#47091](https://github.com/qgis/QGIS/issues/47091) | [PR #47112](https://github.com/qgis/QGIS/pull/47112) | niet geschikt |
| QgsRasterDataProvider.block() returns invalid QgsRasterBlock if requested block size exceeds a certain threshold | [#47097](https://github.com/qgis/QGIS/issues/47097) | [PR #47106](https://github.com/qgis/QGIS/pull/47106) | [PR #47129](https://github.com/qgis/QGIS/pull/47129) |
| Fix missing icons for array field types | [#47078](https://github.com/qgis/QGIS/issues/47078) | [PR #47086](https://github.com/qgis/QGIS/pull/47086) | niet geschikt |
| Use correct approach to unset data defined field for label position when auxiliary column is removed | [#46403](https://github.com/qgis/QGIS/issues/46403) | [PR #47085](https://github.com/qgis/QGIS/pull/47085) | [PR #47088](https://github.com/qgis/QGIS/pull/47088) |
| Fix atlas sorting with complex field names | [#40332](https://github.com/qgis/QGIS/issues/40332) | [PR #47083](https://github.com/qgis/QGIS/pull/47083) | [PR #47103](https://github.com/qgis/QGIS/pull/47103) |
| improve field handling when converting to rule-based | [#46459](https://github.com/qgis/QGIS/issues/46459) | [PR #47081](https://github.com/qgis/QGIS/pull/47081) | [PR #47104](https://github.com/qgis/QGIS/pull/47104) |
| Fix \'Save all Styles/Save current Style\' only appears after close/reopen the layer properties window | [#46596](https://github.com/qgis/QGIS/issues/46596) | [PR #47080](https://github.com/qgis/QGIS/pull/47080) | niet geschikt |
| Fix readability of text when using dark themes | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47071](https://github.com/qgis/QGIS/pull/47071) | [PR #47074](https://github.com/qgis/QGIS/pull/47074) |
| Fix sqlite errors on startup caused by default style database import logic | niet gerapporteerd | [PR #47070](https://github.com/qgis/QGIS/pull/47070) | niet geschikt |
| Fix color widgets incorrectly change colors when mouse is hovered over widget | niet gerapporteerd | [PR #47069](https://github.com/qgis/QGIS/pull/47069) | [PR #47077](https://github.com/qgis/QGIS/pull/47077) |
| Avoid crs definition errors when closing options dialog | [#47014](https://github.com/qgis/QGIS/issues/47014) | [PR #47061](https://github.com/qgis/QGIS/pull/47061) | Niet beschikbaar |
| Fix duplicate shortcut registered warning on startup | niet gerapporteerd | [PR #46983](https://github.com/qgis/QGIS/pull/46983) | niet geschikt |
| Fix scroll wheel events get \"stuck\" when scrolling to bottom of areas | niet gerapporteerd | [PR #46958](https://github.com/qgis/QGIS/pull/46958) | [PR #46987](https://github.com/qgis/QGIS/pull/46987) |
| Flag a lot of situations where ballpark transforms are appropriate so warnings are not shown | [#45621](https://github.com/qgis/QGIS/issues/45621) | [PR #46957](https://github.com/qgis/QGIS/pull/46957) | [PR #46961](https://github.com/qgis/QGIS/pull/46961) |
| Fix crashes when saving layer styles | [#46954](https://github.com/qgis/QGIS/issues/46954) | [PR #46955](https://github.com/qgis/QGIS/pull/46955) | niet geschikt |
| Fix broken merge features tool | niet gerapporteerd | [PR #46924](https://github.com/qgis/QGIS/pull/46924) | Niet beschikbaar |
| \[mssql\] Fix provider on case-sensitive database locales | [#46907](https://github.com/qgis/QGIS/issues/46907) | [PR #46923](https://github.com/qgis/QGIS/pull/46923) | [PR #46949](https://github.com/qgis/QGIS/pull/46949) |
| \[mssql\] Fix inserting features when pk attribute name contains special chars | [#42290](https://github.com/qgis/QGIS/issues/42290) | [PR #46876](https://github.com/qgis/QGIS/pull/46876) | [PR #46903](https://github.com/qgis/QGIS/pull/46903) |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Deze problemen werden opgelost door [Nyall Dawson](https://north-road.com/)
### Bug fixes by Damiano Lombardi
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix #47089 wrong rotation point for rotate label tool preview | [#47089](https://github.com/qgis/QGIS/issues/47089) | [PR #47124](https://github.com/qgis/QGIS/pull/47124) |  |

Deze oplossingen voor problemen werden mogelijk gemaakt door [QGIS.ORG (door donaties en dragende leden)](https://qgis.org/)

Deze problemen werden opgelost door [Damiano Lombardi](https://www.opengis.ch/)

{{<content-end >}}
