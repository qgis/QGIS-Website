---
HasBanner: false
draft: false
releaseDate: 21-02-2020
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.12
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.12{#changelog312 }
![image1](images/projects/dbf38cfe3b603e7e0b840336d39b399a1a46e52d.png)

Datum uitgave 21-02-2020

Als u op zoekt bent naar nieuwe mogelijkheden en een ton aan opgeloste problemen, zal deze uitgave u laten glimlachen van oor tot oor! QGIS 3.12 voegt heel veel nieuwe mogelijkheden toe aan bijna elk gedeelte van QGIS. Van maskers voor labels tot een eigen PG Rasterprovider voor ongelooflijke nieuwe mogelijkheden voor lagen met mazen, en nog veel, veel meer, heeft deze uitgave iets voor iedereen. Zoals altijd herinneren we u er aan dat QGIS een open bron-project is en vragen u om, als het mogelijk is, ons werk te ondersteunen door donaties, sponsoring of bijdragen aan de documentatie van de code, website, enzovoort.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de QGIS gemeenschap hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op qgis.org en help een handje!

QGIS wordt ondersteund door donoren en sponsors. Een actuele lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze lijst met donoren. Als u een officiële sponsor voor het project zou willen worden, bekijk dan onze pagina om te sponsoren voor details. Het sponsoren van QGIS helpt ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van bugs te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeende dank u voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Kaartgereedschap
### Mogelijkheid: QgsMapLayerAction: item toegevoegd aan contextmenu voor Legenda voor actie bij selecteren
Een nieuw item voor het menu (Acties bij selecteren) is toegevoegd aan het contextmenu voor de lagenboom. Het wordt alleen weergegeven indien vereist (laag heeft een selectie en acties kunnen worden uitgevoerd op d betreffende laag).

![imageQ1](https://user-images.githubusercontent.com/127259/74035907-7f334580-49bb-11ea-8d2d-b99eaa10aa89.png)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Geef de afstand weer tussen de positie van de fix van de GPS en de huidige cursor
Als een GPS-apparaat is vebonden geeft, als de gebruiker de cursor over het kaartvenster beweegt, een livebericht op de statusbalk de afstand en richting weer van de cursor tot de positie van de GPS-fix.

Projectinstellingen voor afstand en richting worden in deze weergave gerespecteerd.

![Peek 2020-01-14 16-06](https://user-images.githubusercontent.com/1829991/72318360-cd6c6600-36e7-11ea-9f2d-9a47d8772623.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Instelling toegevoegd voor opmaken van richtingen in hoeken om weer te geven in projecten
De tab Extra - Opties - Kaartgereedschap bevat een nieuwe instelling voor de te gebruiken standaard instelling voor het weergeven van richtingen in hoeken voor nieuw gemaakte projecten. Wanneer een nieuw project wordt gemaakt, zal het deze standaard instelling erven.

Het dialoogvenster Projecteigenschappen heeft ook een nieuwe instelling voor de projectspecifieke indeling van richtingen.

The intention is that whenever angular bearings are shown in QGIS, they will be formatted using the current project\'s bearing format settings.

Bevat ook veel nieuwe aanvullingen voor de API die een stabiele, eenvoudig te vinden, plaats verschaffen voor het instellen en ophalen van instellingen, zoals de indeling voor de richting.

![Peek 2020-01-09 11-08](https://user-images.githubusercontent.com/1829991/72029046-5fcbce80-32d0-11ea-8571-0ae8fa8e3bb0.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Deselecteren van tabellen bij het toevoegen van gegevens van PostgreSQL nadat op de knop Toevoegen is geklikt.
Bij het toevoegen van gegevens van PostgreSQL in Gegevensbronnen beheren, nadat op de knop Toevoegen is gedrukt, zou QGIS eerder geselecteerde tabellen moeten deselecteren.

Dit werd mogelijk gemaakt door [Kartoza](http://kartoza.com/)

Deze mogelijkheid werd ontwikkeld door [Samweli Mwakisambwe](http://samweli.github.io/)
### Mogelijkheid: De totale afstand voor verschuiven en de richting weergeven in de statusbalk
We hebben de totale afstand voor verschuiven en de richting toegevoegd in de statusbalk gedurende bewerkingen voor verschuiven van het kaartvenster. Stelt gebruikers in staat exact te weten hoe ver (en in welke richting) ze de kaart hebben versleept.

![image5](images/entries/48c75d20d3805af3dad8c7faae3c3786a8f6fed0.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Nieuwe optie voor het instellen van de standaard bestandsindeling voor het project (qgs/qgz)
Dit voegt een nieuwe globale optie toe om de voorkeur voor bestandsindeling van het project te definiëren

![imageQ2](https://user-images.githubusercontent.com/127259/72597971-2bc75d80-390f-11ea-84af-7f2c25d5568a.png)

Dit werd mogelijk gemaakt door GEM foundation

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Dialoogvenster Ongeldige attributen gerepareerd bij kopiëren naar andere laag
Het is mogelijk objecten te kopiëren van de ene laag naar de andere. Als dezelfde velden in de doellaag staan, dan worden de attributen daarvoor genomen uit het originele object. Indien niet, wordt de standaardwaarde genomen. Anders is het nieuwe attribuut null.

Als de doellaag beperkingen heeft voor de velden, zouden aan deze nu moeten worden voldaan of opzettelijk worden genegeerd. Maar niet gewoon ongeldig worden gekopieerd zoals tot nu toe gebeurde.

Daarom worden nu de attributen gecontroleerd tegen de beperkingen. En voor alle ongeldige objecten wordt een dialoogvenster weergegeven.

![copydialog2](https://user-images.githubusercontent.com/28384354/72243171-7e410b00-35eb-11ea-8903-11bd56cd9da6.gif)

En bij het plakken van slechts één object, worden de opties gereduceerd:

![copypastesingle](https://user-images.githubusercontent.com/28384354/72243125-5ce01f00-35eb-11ea-897e-0bccdcf083d7.png)

Deze mogelijkheid werd ontwikkeld door [signedav](https://api.github.com/users/signedav)
### Mogelijkheid: Toestaan om een kaartlaag te slepen vanuit de lagenboom op een widget voor selecteren van de projectie
\...om de projectie zo in te stellen dat die overeenkomt met die laag. Gewoon een kleine tijdbesparende sneltoets!

![Peek 2019-12-20 11-27](https://user-images.githubusercontent.com/1829991/71222288-b7070080-231b-11ea-89f4-af856dece4c3.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Processing Rastercalculator: ontbrekende knoppen en valideren toegevoegd
Ontbrekende knoppen voor ABS/MIN/MAX toegevoegd en valideren van expressie.

![image10](https://user-images.githubusercontent.com/142164/68952420-1bd0b780-07c0-11ea-88d1-2ad0a8b5591e.gif)

Deze mogelijkheid werd ontwikkeld door Alessandro Pasotti
## Symbologie
### Mogelijkheid: Animatie voor vectorspoor en stroomlijnen voor laag met mazen
De vectorrenderer voor mazen kan nu stroomlijnen en deeltjes visualiseren boven de bestaande modus \"pijl\".

![image11](images/entries/5b772e74d433e766b50023cd107aad9cb1d68de6.webp)

Dit werd mogelijk gemaakt door [TUFLOW](http://www.tuflow.com)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Selectief masker
Een nieuwe geavanceerde mogelijkheid voor renderen is toegevoegd: selectief masker. Het maakt het definiëren van \'masker\'-gebieden rondom labels of puntmarkeringen mogelijk. Deze maskers zullen alleen enkele symboollagen of andere lagen eronder \"niet tekenen\", gekozen door de gebruiker.

![image12](https://user-images.githubusercontent.com/1618556/62111873-d68c8680-b2b1-11e9-8cd4-19077f99a8ff.gif)

Dit werd mogelijk gemaakt door [QGIS.CH en anderen door een campagne voor medefinanciering](https://oslandia.com/en/offre-qgis/selective-masking/)

Deze mogelijkheid werd ontwikkeld door [Hugo Mercier (Oslandia)](https://www.oslandia.com)
### Mogelijkheid: Als rotatie van decimale graden niet evalueert, terugvallen op statische waarde
De Legenda werkt uiteindelijk ook netjes met data-bepaalde rotatie. QGIS kon al  data-bepaalde rotatie toepassen op symbolen en individuele symboollagen, maar dat resulteerde in een kapotte legenda. De rotatie van symbolen (en delen van symbolen gedefinieerd op symboollagen) in de legenda kan nu worden beheerd door de standaardwaarden naast de data-bepaalde eigenschappen te wijzigen.

Het oude gedrag was om altijd terug te vallen op 0 in geval van een mislukte expressie. Wat het in sommige gevallen moeilijk maakte een juiste legenda te maken.

als u bijvoorbeeld twee symboollagen had met de volgende expressies voor hun rotatie

    "orientation"
    
en

    90 + "orientation"
    
wat twee loodrechte symboollagen zouden zijn (bijv. een rechte hoek aangeven), geroteerd op een veld voor oriëntatie.

Nu zouden in de Legenda (en voorbeeld van symbool), beide lagen worden weergegeven met een rotatie van 0, omdat er geen geassocieerd object is met een veld oriëntatie.

Het nieuwe gedrag is om terug te vallen op de statische, geconfigureerde waarden die het zeer intuïtief maken om de Legenda voor deze gevallen te configureren.

**Voor**

![Peek 2019-12-08 09-18](https://user-images.githubusercontent.com/588407/70386652-acec1600-199b-11ea-8457-f9dd54c84272.gif)

**Na**

![Peek 2019-12-08 09-16](https://user-images.githubusercontent.com/588407/70386651-acec1600-199b-11ea-8ce2-27798aec38a7.gif)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Mogelijkheid: Op dichtheid gebaseerde telling van punten voor de willekeurige markeringsvulling
Deze mogelijkheid voegt een op dichtheid gebaseerde methode voor telling van punten toe aan de nieuwe willekeurige markeringsvulling.

![image15](https://user-images.githubusercontent.com/1728657/67672096-c2881c00-f9a9-11e9-8394-d73505d05309.gif)

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
### Mogelijkheid: Willekeurig markeringsvulling type symboollaag
Deze mogelijkheid voegt een nieuw type gevulde symboollaag \"Willekeurige vulling markering\" toe. Het maakt het mogelijk objecten polygoon te laten renderen met een markeringssymbool dat is geplaatst op willekeurige locaties binnen de grenzen van de polygoon.

Opties bevatten:
- aantal te renderen markeringssymbolen voor de polygoon
- of de nabij randen van de polygoon gerenderde markeringen moeten worden geclipt op de grens van de polygoon of niet
- een optioneel willekeurig aantal zaad, om consistente plaatsing van markeringen te geven als kaarten worden ververst (staat ook willekeurige plaatsing toe om zich netjes te gedragen met QGIS server en op tegels gebaseerd renderen)

![image16](https://user-images.githubusercontent.com/1829991/66734145-51267480-eea5-11e9-9e0a-3bfeee15f976.png)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Moglijkheid: Optie toegevoegd om kleur in te stellen voor renderen van pixels Geen gegevens in rasterlagen
Maakt het mogelijk dat pixels Geen gegevens in rasters worden gekleurd met een specifieke (niet-transparante) kleur. Ontworpen om overeen te komen met de optie \"Display background value\" van ArcMap.

![image17](https://user-images.githubusercontent.com/1728657/64846100-f4c9fe00-d635-11e9-8acb-367ad2dd2915.png)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
## Labelen
### Mogelijkheid: Verwijderen aangepaste positie label toestaan
We hebben een nieuwe optie toegevoegd voor de mogelijkheid om aangepaste posities van het label te verwijderen, door te drukken op de DEL-toets, bij het verplaatsen van het label.

![image18](images/entries/e8064c56705b7a74befa85e8a34e7b7311626f0a.gif)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch)
## Diagrammen
### Mogelijkheid: Ondersteuning voor kleureffect voor renderer van diagrammen
Deze nieuwe mogelijkheid maakt het voor diagrammen mogelijk om kleureffecten te gebruiken, inclusief valschaduwen, gloed buitenzijde, etc\…

![image19](images/entries/37d0a22707eca463e5aba7c0a349b2d8029fb823.gif)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Nieuw type diagram \"gestapelde balken\"
Met deze nieuwe mogelijkheid hebben gebruikers de mogelijkheid om gestapelde balken van verschillende kleuren bovenop elkaar, verticaal of horizontaal, voor elk attribuut te maken. Ontworpen om overeen te komen met de optie voor de renderer van diagrammen \"Stacked\" die beschikbaar is in ArcGIS.

![image20](images/entries/933c25cf0cd8997e177eee809b4fa26462b6d8c2.webp)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Optie voor afstand voor balkdiagrammen voor vectorlagen
Maakt gebruiker-beheerde afstand mogelijk tussen elke balk in het diagram.

![image21](images/entries/7906ea6467d1d5ea19550ce1711fcc277df709a0.webp)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Nieuwe optie om de hoekrichting voor taartdiagrammen te beheren
Deze mogelijkheid maakt het mogelijk te beheren of gedeelten moeten worden gerenderd met de wijzers van de klok mee of tegen de wijzers van de klok in.

![image22](images/entries/c2484d36648c335d16d1e3a45ac1a132ca2baafe.webp)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
## Renderen
### Mogelijkheid: Play/Stop-knoppen voor terugspelen laag met mazen
Het is mogelijk te schakelen met de tijdframes van gegevenssets van lagen met mazen met de knoppen Play/Stop. De instelling voor terugspelen kan worden aangepast in het dialoogvenster voor de tijdinstellingen.

![image23](images/entries/4799685965addef6ca2c788d82eea77e67e2f1f3.webp)

Dit werd mogelijk gemaakt door [Lutra Consulting](http://www.lutraconsulting.co.uk)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Direct resamplen van data-bepaald op zijkanten naar punten (Laag met mazen)
Voor gegevenssets die zijn gedefinieerd op zijkanten, kan men er voor kiezen gegevens te interpoleren naar punten met de methode Gemiddelde buur. Wanneer geen methode voor interpolatie van de gegevens wordt gekozen, heeft elke pixel op een enkele zijkant één enkele waarde/kleur. Met gegevens op punten wordt het renderen van elke pixel geïnterpoleerd vanuit de waarden van de punten, wat gladdere figuren maakt.

Gebruik het paneel voor het opmaken van de contouren van de mazen om te schakelen tussen de methoden voor het interpoleren van de gegevens.

![image24](images/entries/c9c38ee8c59693b2971ab6269db22681a61002a1.webp)

Dit werd mogelijk gemaakt door [Oostenrijkse Ministerie voor landbouw, Bosbouw, Milieu en Waterbeheer](https://www.bmlfuw.gv.at)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Ondersteuning referentietijd voor Mazen 
Voor verscheidene gegevenstypen, bijvoorbeeld GRIB en NetCDF, wordt de referentietijd in het dialoogvenster voor de tijdinstellingen van QGIS vooraf gevuld vanuit de nieuwe gegevens en hoeft dus niet meer handmatig te worden ingesteld. Ook hebben we verschillende problemen opgelost gerelateerd aan het parsen van de tijd, dus zou het in QGIS 3.12 mogelijk moeten zijn uw tijden in plots/animaties op de juiste manier op te maken en weer te geven:
- Als er een geldige referentietijd wordt verschaft voor groepen in de gegevensset, wordt die referentietijd gebruikt om de tijd weer te geven (met absolute tijd).
- Als er geen referentietijd wordt verschaft, wordt de tijd weergegeven met relatieve tijd, en door de gebruiker kan een referentietijd worden ingesteld om de absolute tijd weer te geven.
- Wanneer geen referentietijd wordt verschaft wordt standaard de huidige datum + tijd ingesteld op 00:00:00.

Een drukknop is toegevoegd om, indien nodig, de met de groepen voor de gegevensset verschafte referentietijd opnieuw te laden.

Het voegt ook een nieuwe mogelijkheid toe om de gebruiker de tijdseenheid van de provider in te laten stellen met een combinatievak, als die tijdseenheid anders is dan uren.

![imageQ3](https://user-images.githubusercontent.com/7416892/70955568-bb939680-2047-11ea-9857-8aba122e43dd.png)

Dit werd mogelijk gemaakt door [TUFLOW](http://www.tuflow.com)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## 3D-objecten
### Mogelijkheid: 3D terreinrenderer voor lagen met mazen 
Het is mogelijk de laag met mazen te renderen als terrein in de 3D-weergave.

De gebruiker kan er voor kiezen deze afgevlakte driehoeken en draadmodel in/uit te schakelen. Het is mogelijk de lijndikte en lijnkleur van het draadmodel te kiezen, de verticale schaal te wijzigen en de stijl van het renderen te kiezen (unieke kleur of nuances uit het kleurverloop).

Er zijn twee items om de laag met mazen te renderen in de 3D-weergave :
- kies de mazen als het terrein in de widget voor configuratie
- activeer de 3D-weergave in de laageigenschappen.

De gebruiker kan deze instellingen kiezen:
- afgevlakte driehoeken in-/uitschakelen
- draadmodel in-/uitschakelen
- de lijndikte en de lijnkleur van het draadmodel kiezen
- de verticale schaal wijzigen
- de stijl voor het renderen kiezen : unieke kleur of nuance uit kleurverloop
- instellingen van de nuances voor het kleurverloop als voor rasterlaag

Voor nu kunnen de mazen worden gerenderd als een TIN, maar het renderen van de gegevensset wordt niet ondersteund. De infrastructuur is echter aangepast voor toekomstig werk.

![mesh3dsettings](https://user-images.githubusercontent.com/7416892/72482783-41d10300-37d5-11ea-9a21-8f906abcb14a.gif)

![image27](images/entries/f19c25acbd1eb462cdc0365d3af3f706c1b4d2fe.gif)

Dit werd mogelijk gemaakt door [TUFLOW](http://www.tuflow.com)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Gegevens van 3D-vectorlaag laden op de achtergrond + tegelen
Dit voegt ondersteuning toe voor het op de achtergrond laden van gegevens uit vectorlagen in 3D-kaartweergaven. Tot nu zouden laden (en mozaïeken) de gebruikersinterface volledig bevriezen - dat zou vele seconden kunnen duren, afhankelijk van de complexiteit van de invoergegevens.

De basis renderer voor vectorlagen en op regel gebaseerde renderer werden geconverteerd om QgsChunkedEntity te gebruiken, wat al reeds wordt gebruikt voor het renderen van terrein. Er zijn nog twee verbeteringen in aanvulling op het ontgrendelen van de gebruikersinterface:
- laadproces is multi-threaded in plaats van slechts één bron te gebruiken
- laden wordt gedaan in tegels - dus is het mogelijk de tegels met 3D-gegevens te zien verschijnen, terwijl andere gegevens nog steeds worden geladen

Er is een nieuwe optie voor configuratie op de 3D-tab van vectorlagen - het bepaalt hoe diep de quadtree zal zijn. Eén zoomniveau betekent bijvoorbeeld dat er één enkele tegel zal zijn voor de gehele laag. Drie zoomniveaus betekent dat er 16 tegels zullen zijn op het bladniveau (elk extra zoomniveau vermenigvuldigt dat met 4, dus heb ik de gebruikersinterface beperkt tot max. 8 niveaus, wat ~16K tegels geeft, wat al heel veel is).

Hoe de quadtree voor de tegels van een vectorlaag wordt gevuld: alle interne knopen van de boom zijn leeg en dus probeert de 3D-kaartscene ze onmiddellijk te vervangen door hun kinderen - dit gaat door totdat bladknopen worden bereikt. Momenteel bevatten alleen knopen op het bladniveau gegevens. Dit zou in de toekomst kunnen wijzigen als we meer strategieën uitwerken - interne knopen zouden bijvoorbeeld een klein percentage objecten van de kindknopen kunnen bevatten (dit zou ons in staat stellen iets weer te geven terwijl we heel ver zijn uitgezoomd, zonder eerst alle gegevens te moeten laden).

Voor doeleinden van debuggen is er ook een nieuwe optie voor configuratie \"Begrenzingsvakken van tegels weergeven\". Dit stelt u in staat het begrenzingsvak van elke tegel te zien (speciaal nuttig als er problemen zijn met tegels die niet worden weergegeven, terwijl dat wel zou moeten).

Dit werd mogelijk gemaakt door QGIS.org grant.

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://api.github.com/users/wonder-sk)
## Afdruklay-outs
### Mogelijkheid: Afbeeldingen slepen en neerzetten op afdruklay-outs toestaan
Deze nieuwe mogelijkheid geeft de gebruiker bijvoorbeeld de mogelijkheid om een SVG uit een bestandsverkenner op de afdruklay-out te slepen om een nieuw item Afbeelding te maken dat die SVG-afbeelding bevat.

![image28](images/entries/21b9f2fba7bf1576f794410fd238ef7553154d53.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Nieuw type item lay-out: handmatig gemaakte vaste tabellen
Dit nieuwe type item maakt het mogelijk tabellen te maken waarvan de inhoud handmatig door gebruikers wordt ingevoerd (d.i. stijl van een werkblad), zodat gebruikers volledig aangepaste tabellen kunnen maken. Ondersteunt het beheren van aangepaste inhoud van cellen, voor- en achtergrondkleuren (en binnenkort: voorkeuzen voor rij- en kolomhoogten). Een nagelnieuw dialoogvenster voor tabelontwerp is toegevoegd wat het aanpassen van deze tabellen mogelijk maakt.

![image29](images/entries/95cfa9a8c44fb0141474d80e4b3a5e7f98352e70.webp)

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Gebruiksbeheer toegevoegd voor numerieke indelingen van de schaalbalk
U heeft nu de optie om de numerieke indeling te beheren die wordt gebruikt door de schaalbalk van een lay-out.

U kunt alle eigenschappen voor de indeling beheren voor de nummers in de schaalbalken, inclusief of zij een scheidingsteken voor duizendtallen willen, decimale plaatsen, wetenschappelijke notatie, etc. Heel nuttig in het geval van het maken van kaarten voor publiek buiten de huidige locale van QGIS, of wanneer u gewoon een voorkeur heeft om de stijl af te laten wijken van de standaarden van de locale (bijv. toevoegen van scheidingsteken voor duizendtallen, terwijl de standaard die juist verbergt).

![image30](images/entries/99c97baaee3e5930bca0cb63db1391b6fd49b34f.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Toestaan dat attributentabellen van lay-out worden opgemaakt met de voor- en achtergrondkleuren van overeenkomende voorwaardelijke stijlen
Wanneer de nieuwe optie \"Kleuren voorwaardelijke stijlen toepassen op laag\" is ingeschakeld in de instellingen voor de attributentabel in de lay-out, zullen regels voor voorwaardelijke stijl, die in de laag aanwezig zijn, worden toegepast binnen de attributentabel op de lay-out (voor nu alleen nog voor- en achtergrondkleuren!).

![image31](images/entries/baded0d05539439d58e6df5a8f24157293cf8022.gif)

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Zoekvak toegevoegd aan Lay-out beheren
Maakt het mogelijk de lijst met lay-outs in een project te filteren op naam, handig als een project heel veel lay-outs heeft…!

![image32](images/entries/fb510c6c079d55dab2dd22f02c7c5355b317ac47.webp)

Deze mogelijkheid werd ontwikkeld door Nyall Dawson
## Expressies
### Mogelijkheid: Tags zoeken voor functies
Tags voor statische functies voor expressies om ze sneller op te kunnen halen. Functies zoals array_to_string worden vermeld als de gebruiker \"split\" of \"convert\" invoert of - zoals eerder - een deel van de naam van de functie.

![image33](images/entries/689a669fe84721d7574aba7e595e019a9936f0b9.gif)

Dit werd mogelijk gemaakt door [SwissTierras-Colombia](https://www.proadmintierra.info)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Mogelijkheid: Vermelden waarden verwijzingslaag
Wanneer een veld een RelationReference, ValueRelation en ValueMap is, is er de mogelijkheid om niet alleen de waarden van de huidige laag weer te geven, maar ook de mogelijke waarden in de verwijzingslaag / geconfigureerde mogelijkheden.

![image34](images/entries/394c762c41e71764d9be397b718252eddb2dbd3e.gif)

Dit werd mogelijk gemaakt door [SwissTierras-Colombia](https://www.proadmintierra.info)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Mogelijkheid: Nieuwe expressies
- `is_empty(geom)`, check if a geometry is empty (geometry that contain no coordinates)
- `is_empty_or_null(geom)`, check if a geometry is empty or NULL (does not have geometry)
- `hash`, cryptographic hashes functions using [QCryptographicHash](https://doc.qt.io/qt-5/qcryptographichash.html). Use case is the same as PgCrypto but in client side for all supported format.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Feature: New algorithm \"Rename table field\"
Neemt een invoerlaag, bestaand veld en een nieuwe naam voor het veld, en voert een nieuwe laag uit met het hernoemde geselecteerde veld.

While this result could also be achieved with the Refactor Fields algorithm, Refactor Fields isn\'t particularly model friendly. It relies on a constant, fixed table structure, and can\'t adapt to input tables with different field structures.

In tegenstelling daaraan past dit eenvoudige algoritme Veld hernoemen zich netjes aan voor het gebruik in modellen, omdat het werkt op slechts één veld en alle andere velden onberoerd laat.

![image35](images/entries/c01edc8ee51dff2b4df8f825e0dcaf27940e4aba.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Opgeslagen expressies
- Gebruikersexpressies opslaan
- Bewerker leegmaken pictogram/actie

![expression-storage-opt](https://user-images.githubusercontent.com/142164/70983414-faae0000-20b8-11ea-9f25-14b338d4c680.gif)

See also QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/135>

This feature was funded by [Salvatore Fiandaca](https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: Vermelden waarden verwijzingslaag in Expressiebouwer
Wanneer een veld een RelationReference, ValueRelation en ValueMap is, is er de mogelijkheid om niet alleen de waarden van de huidige laag weer te geven, maar ook de mogelijke waarden in de verwijzingslaag / geconfigureerde mogelijkheden.

*age* is a ValueMap, *species* is a ValueRelation and *island_id* is a RelationReference

![uniquevalues](https://user-images.githubusercontent.com/28384354/70978774-ab63d180-20b0-11ea-901b-d51d44fa8fa4.gif)

In het voorbeeld hebben we de personen:
- *George (in Cuba, twintiger, mens) Paul (in Vietnam, dertiger, mens) Ringo (in Venezuela, veertiger, kat) John (ook in Vietnam, veertiger, tafel)*
- En de items in de landenlaag zijn *USSR, Cuba, Vietnam, Burma, Venezuela, North Korea*

Deze mogelijkheid werd ontwikkeld door [signedav](https://api.github.com/users/signedav)
### Feature: Functies voor expressies toegevoegd voor converteren naar/van wkb
- `geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → a point geometry object` Returns a geometry created from a Well-Known Binary (WKB) representation.
- `geom_to_wkb( $geometry ) → binary blob containing a geometry object` Returns the Well-Known Binary (WKB) representation of a geometry as a binary blob.

Adds geom_from_wkb and geom_to_wkb, which mirror the existing geom_from_wkt/geom_to_wkt functions but for WKB representations of geometries.

Since QGIS 3.6 we\'ve had good support for binary blob values in expressions and field values, so adding these functions allows users to work with binary blob fields containing WKB representations of geometries (e.g. with a geometry generator showing the encoded geometries)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: is_valid expression
`is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → true` Returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules

Add an is_valid function to the expressions, which reuses GEOS is valid and returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules.

Deze mogelijkheid werd ontwikkeld door Pete King
### Feature: Add datetime_from_epoch (MSec from epoch) expression function
`datetime_from_epoch(1483225200000) → 2017-01-01T00:00:00` Returns a datetime whose date and time are the number of milliseconds, msecs, that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (Qt.UTC), and converted to Qt.LocalTime.

Deze mogelijkheid werd ontwikkeld door Richard Duivenvoorde
### Mogelijkheid: Functie voor expressie rotate()
`rotate($geometry, 45, make_point(4, 5)) → geometry rotated 45 degrees clockwise around the (4, 5) point` Returns a rotated version of a geometry. Calculations are in the Spatial Reference System of this geometry.

Deze mogelijkheid werd ontwikkeld door Raymond Nijssen, Nyall Dawson
### Mogelijkheid: Zaad toestaan voor functies Random
- `rand(10, 80, 1) → 30` Returns a random integer within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.
- `randf(10, 80, 1) → 19.37136508087729` Returns a random float within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.

This feature adds an optional seed parameter to rand() and randf() functions This is very useful if you want the result to be deterministic, for instance to assign random but fixed colors to features. Using color_hsb(rand(0,360,\$id),50,50) for instance yields always the same color for the same feature. We also improves the rand() function, which didn\'t work for high values (over 32000) by using Qt\'s QRandomGenerator instead of qrand (which it seems was deprecated in Qt 5.11).

Deze mogelijkheid werd ontwikkeld door olivierdalang
### Feature: Language support for format_date() and to\_{date,datetime,time}()
- `format_date('2012-05-15','d MMMM yyyy','fr') → '15 mai 2012'`
- `format_date('2012-05-15','d MMMM yyyy','it') → '15 maggio 2012'`
- `format_date('2012-05-15','d MMMM yyyy','en') → '15 May 2012'` Formats a date type or string into a custom string format. Uses Qt date/time format strings. See QDateTime::toString.

By default, those expression use the application\'s locale. The addition of an optional language parameter allows handling of dates that wouldn\'t match that default locale (say for e.g. an English system running QGIS trying to transform a French-formatted string into a date object).

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
## Digitaliseren
### Mogelijkheid: Dialoogvenster Ongeldige attributen bewerken bij kopiëren/plakken naar andere laag
Bij het kopiëren-plakken van objecten van de ene laag naar de andere, in het geval dat er beperkingen (bijv. not null) op de doellaag van kracht zijn, waaraan niet automatisch kan worden voldaan met standaardwaarden, verschijnt een dialoogvenster om de ongeldige attributen te repareren of de beperkingen met opzet te negeren.

![image38](images/entries/5bd43dd39955e37ace130038b968550c6fa260c5.gif)

This feature was funded by [Amt für Wald und Wild Zug](https://www.zg.ch/behoerden/direktion-des-innern/wald-und-wild)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Mogelijkheid: Parallelle cache voor snappen
In previous version of QGIS, the snapping index cache was built sequentially and you had to wait for all your layers to be indexed before starting edition. Thanks to the QGIS.org grant program, QGIS now builds the snapping index cache in parallel for each layer, so it speeds up the whole process. Snapping has also been relaxed, meaning that you don\'t have to wait for the cache to be complete, you can start editing and snapping information will appear as soon as they are ready.

![image39](images/entries/d77958db7175267448d9b94950532dee8b90145c.webp)

Dit werd mogelijk gemaakt door [QGIS.org](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Gegevensbeheer
### Mogelijkheid: Verbeteringen aan DXF exporteren
We hebben het proces voor het exporteren naar DXF opnieuw bewerkt. Dit maakt het proces voor exporteren meer solide en biedt nieuwe mogelijkheden.
- Stijlen van geometrieën worden geëxporteerd en blokken worden gebruikt
- De Z-coördinaten van 3D-geometrieën worden behouden
- Labels worden geëxporteerd met inachtneming van hun ankerpunten en horizontale en verticale uitlijning of instellingen voor kwadranten

The whole DXF export process has also been made ready for running in a thread. With this in place, it\'s now only one step away from being sent to the background, allow cancellation of an ongoing export process or being exposed as a processing algorithm.

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Formulieren en widgets
### Mogelijkheid: Geometrisch object maken vanuit de relatiebewerker
We added the ability to add a new feature and digitize its geometry directly from within the relation editor widget. It\'s now easier to add a geometric feature related to your currently displayed parent feature.

![image40](images/entries/fe03aefab87464e54b70569e6d05ad09a1b8fae5.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Verbeterd dialoogvenster voor selecteren van object
From the relation editor widget, you can link your currently displayed feature with existing features. The feature selection dialog allows you to choose these features. Thanks to the QWAT user group, feature selection is now shared with the canvas\' one so it is easy to find out and pick the feature you want to link. We have also added the ability to filter displayed features (selected ones, visible on map, matching an expression\...) reusing the same widgets already existing in attribute form.

![image41](images/entries/a65364e6a48857a8720643c41a3cb17461d9e16a.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: UX improvements in drag\'n\'drop form designer
The drag\'n\'drop form designer has received some nice UX improvements
- De twee lijsten (beschikbare velden en boom voor de lay-out) zijn nu gesynchroniseerd: wanneer u een item in een lijst selecteert, wordt het overeenkomende item in de andere geselecteerd.
- Verborgen dialoogvensters voor configuratie (onder dubbelklikken) zijn naar het rechterpaneel gebracht

![image42](images/entries/5f47cb6311a9bffef94128a703719d709deb995a.gif)

Dit werd mogelijk gemaakt door QGIS.org bugfixing

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
## Legenda van laag
### Mogelijkheid: Ondersteuning voor weergeven van afbeeldingen van legenda's van WMTS in de lagenboom
We hebben ondersteuning toegevoegd voor het weergeven van afbeeldingen voor de legenda van WMTS  direct in de lagenboom, zoals al het geval is voor afbeeldingen van legenda's van WMS.

Voorbeeld:

![imageQ4](https://user-images.githubusercontent.com/1298852/72462785-33351c80-37d2-11ea-98f2-ce0d5221e1f5.png)

Sample use case: <https://wmts10.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>

This feature was developed by [Sandro Mani](https://api.github.com/users/manisandro)
## Analyse-gereedschappen
### Mogelijkheid: Afgevlakt exporteren van contouren voor lagen met mazen
A new algorithm in QGIS's analysis library API to export directly contour lines and polygons is added. The method is not based on GDAL algorithms, but directly uses mesh layer triangular mesh interpolation methods. It is both fast and with smooth shapes, matching rendered images from QGIS. You can try the new processing algorithm in Crayfish processing toolbox.

![image44](images/entries/044ad55bfb4287026b4e002c46c8687093488d22.webp)

Dit werd mogelijk gemaakt door [Oostenrijkse Ministerie voor landbouw, Bosbouw, Milieu en Waterbeheer](https://www.bmlfuw.gv.at)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Ondersteuning van data-bepaalde gegevenssets in QGIS Mazencalculator
U kunt de mazencalculator gebruiken voor alle typen gegevenssets, zowel gedefinieerd op zijkanten als op punten. Aanvullend stelt het gebruikers in staat het resultaat van de mazencalculator op te slaan onder verschillende namen of indelingen. Dit maakt het bijvoorbeeld mogelijk om te werken met gegevens van FLO-2D of HEC-RAS in de QGIS mazencalculator

![image45](images/entries/044d52fe937887854583ecfdc551e73eafb94a41.webp)

Dit werd mogelijk gemaakt door [Oostenrijkse Ministerie voor landbouw, Bosbouw, Milieu en Waterbeheer](https://www.bmlfuw.gv.at)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Processing
### Mogelijkheid: Nieuwe lagen verpakken in een bestaand Geopackage
We verbeterden het bestaande algoritme voor Processing *package layers* om nieuwe lagen aan bestaande GeoPackages toe te kunnen voegen. Alles wat u dient te doen om hiervan gebruik te kunnen maken is het uitschakelen van de parameter OVERWRITE en een bestaand GeoPackage te specificeren.

![image46](images/entries/35d87f4826aad132de4a0b99ac7c775f6aa9b029.webp)

This feature was funded by [BikePlan](https://www.bikeplan.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (lineair lidmaatschap)
Het algoritme Raster onscherp maken (lineair lidmaatschap) is een eigen implementatie van een algoritme met fuzzy logica. Het transformeert een invoerraster naar een onscherp gemaakt raster en wijst daarbij waarden tussen 0 en 1 toe volgens een functie voor lineair onscherp lidmaatschap. De waarde 0 impliceert geen lidmaatschap met de gedefinieerde ingestelde onscherpte, een waarde 1 geeft volledig lidmaatschap weer. Daar tussen volgt de mate van lidmaatschap een functie voor lineair lidmaatschap.

![image47](images/entries/bfb37d710293c252dae11b67b25bdc1431f13815.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (macht lidmaatschap)
Het algoritme Raster onscherp maken (macht lidmaatschap) is een eigen implementatie van een algoritme met fuzzy logica. Het transformeert een invoerraster naar een onscherp gemaakt raster en wijst daarbij waarden tussen 0 en 1 toe volgens een functie voor macht onscherp lidmaatschap. De waarde 0 impliceert geen lidmaatschap met de gedefinieerde ingestelde onscherpte, een waarde 1 geeft volledig lidmaatschap weer. Daar tussen volgt de mate van lidmaatschap een functie voor macht lidmaatschap.

![image48](images/entries/7a81ecd4414ee39b37e575863687615c88e9a856.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (klein lidmaatschap)
The Fuzzify raster (small membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'small\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'small\' membership function. The \'small\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image49](images/entries/2bef948a7b02bd26208ca98e9ddb243d46d104a6.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (groot lidmaatschap)
The Fuzzify raster (large membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'large\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'large\' membership function.The \'large\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image50](images/entries/10963d11812664a76d4fc3fac72777c34a08c767.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (Gaussiaans lidmaatschap)
The Fuzzify raster (gaussian membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'gaussian\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'gaussian\' membership function. The gaussian function is constructed using two user-defined input values which set the midpoint of the gaussian function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image51](images/entries/58068dc6518a0df20a39df69ea4175f7b196b049.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Fuzzy logica - Raster onscherp maken (nabij lidmaatschap)
The Fuzzify raster (near membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'near\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'near\' membership function. The near function is constructed using two user-defined input values which set the midpoint of the near function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image52](images/entries/a4873da4c5e782a14caaa02f279ef92ba5bf5a38.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Feature: Algoritme Verdichten op aantal geporteerd naar C++
We ported the Densify by count algorithm to C++ in order to enhance it\'s speed when compared to the previous Python implementation. The new algorithm also exposes the count parameter as dynamic parameter so that it can be controlled by expressions or field values.

![image53](images/entries/680eb97f65d08de5541f4b1f5ac4425f45988cc2.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Algoritme Willekeurige punten in bereik geporteerd naar C++
We ported the Random points in extent algorithm to C++. This boosts it\'s speed when comparing it to the previous Python implementation. The new algorithm also exposes an advanced parameter of maximum numbers of retrys for the algorithm when searching for randomly placed points that respect a certain distance between all points.

![image54](images/entries/c452431d9a2cd9f9f76869cf98e09e18bf2a81a4.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Mogelijkheid: Algoritme Dichtheid lijn
In deze versie hebben we een eigen algoritme toegevoegd voor het bereken van de op het raster gebaseerde dichtheid van lijnen. Dit algoritme berekent de dichtheid van de lijn, gebaseerd op een zoekradius en wegingen van de lijnen binnen de zoekradius. Het algoritme werd geporteerd om meer functionaliteit in QGIS te verschaffen uit de extensie Spatial Analyst voor ArcGIS.

![image55](images/entries/b28bbe3d5129ccc5dd61585dc1a9e31383a59c6f.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Feature: New algorithm \"Repair Shapefile\"
We hebben een nieuw algoritme toegevoegd dat GDAL gebruikt om Shapefiles te repareren die een defect of ontbrekend bestand .SHX hebben.

![image56](images/entries/c3a6a174187284126ea0af289614505ab8c0c593.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add new algorithm \"Detect Dataset Changes\"
Dit algoritme vergelijkt twee vectorlagen en bepaalt welke objecten niet gewijzigd, toegevoegd of verwijderd zijn tussen de twee. Het is ontworpen voor het vergelijken van twee verschillende versies van dezelfde gegevensset.

Bij het vergelijken van objecten worden de geometrieën van de objecten uit het origineel en de revisie vergeleken tegen elkaar. Afhankelijk van de instelling Gedrag voor vergelijken van geometrie zal de vergelijking ofwel worden gemaakt door een exacte vergelijking te gebruiken (waarbij geometrieën een exacte overeenkomst met elkaar moeten hebben, inclusief de volgorde en het aantal punten) of alleen een topologische vergelijking (waarbij gebieden van geometrieën als gelijk worden beschouwd als al hun randen van componenten overlappen. Bijv. lijnen met dezelfde locaties voor punten, maar in tegengestelde richting zullen door deze methode als gelijk worden beschouwd). Als de topologische vergelijking is geselecteerd, dan zullen in de geometrieën aanwezige waarden Z of M niet worden vergeleken.

Standaard vergelijkt het algoritme alle attributen uit de originele en gereviseerde objecten. Als de parameter Attributen waarmee rekening moet worden gehouden voor overeenkomst wordt gewijzigd, dan zullen alleen de geselecteerde attributen worden vergeleken (bijv. gebruikers toestaan om een tijdstempel of veld ID, waarvan wordt verwacht dat die wijzigen tussen de revisies, te negeren).

Als objecten in de originele of gereviseerde lagen geen geassocieerde geometrie hebben, dan moet extra zorg in acht worden genomen om er voor te zorgen dat voor deze objecten een unieke set attributen is geselecteerd voor de vergelijking. Als aan deze voorwaarde niet wordt voldaan zullen waarschuwingen worden weergegeven en de resulterende uitvoer zou misleidend kunnen zijn.

Het algoritme voert drie lagen uit, één die alle objecten bevat die als ongewijzigd tussen de revisies worden beschouwd, één die objecten bevat die zijn verwijderd uit de originele laag en die niet voorkomen in de gereviseerde laag, en één die objecten bevat die zijn toegevoegd aan de gereviseerde laag, maar die niet voorkomen in de originele laag.

![image57](images/entries/e38dcea12e1198341eb9f0bd45a33ebf7eda390b.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: New mode to \"Join Attributes by Location\" to take attributes from matching feature with largest area of overlap only
This allows for easy polygon-\>polygon joins, where you expect there to be only a single matching feature and don\'t want to include features which are just touching or have just tiny sliver polygon overlaps.

![image58](images/entries/27b8e5e11deca93ffade31b86edc712ce918d179.webp)

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Eigen algoritme Affiene transformatie voor vectoren toegevoegd
Biedt de volgende voordelen boven de versies van GRASS/SAGA:
- Volledige ondersteuning voor Z-/M-waarden en afhandeling van gebogen geometrieën zonder verlies van bogen
- Werkt met alle eigen gegevenstypes, dus geen noodzaak voor transformeren van opmaak
- Ondersteunt dynamische (data-bepaalde, per object) parameters voor vertalen/op schaal brengen/roteren
- Maakt transformatie en op schaal brengen van zowel Z- als M-waarden mogelijk (indien aanwezig)
- Modus Direct bewerken wordt ondersteund

![image59](images/entries/1bfee3c2e208ecca6c235d96f83966ec808a0b1c.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: add gdal_viewshed algorithm
Expose new gdal_viewshed tool via Processing toolbox. Note: this requires GDAL \>= 3.1.

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
## Browser
### Mogelijkheid: Aanpassen van alle in de Browser weergegeven items
Add customization of the items shown in browser to the Interface Customization dialog. User can hide some of the root items in the browser panel (e.g. Favourites, PostGIS provider, MSSQL, Oracle, Volumes, \...)

![image60](images/entries/5e8e9037420b83cd44d4e1994d4119e4ae92c8aa.webp)

This feature was funded by [Limerick City and County Council](https://www.limerick.ie/council)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: HTML-bestanden in paneel Browser weergeven
Deze mogelijkheid staat toe dat bestanden .htm(l) worden weergegeven en kunnen worden geopend vanuit het paneel Browser. Deze worden vaak gebruikt om gegevensbestanden of projecten voor in kaart brengen te documenteren.

![image61](images/entries/0db8930d20ca6f2fbf5b29593afdcf59e1af8d1e.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Show \"Open Document\...\" action in browser
Door met rechts te klikken op bepaalde bestanden in de Browser is het mogelijk ze te openen met de standaard externe toepassing voor dat type bestand

Bijv. PDFs zullen openen met de standaard externe PDF-viewer.

Works with PDF, ODS, XLS(X), CSV, TXT, PNG, JPEG, TIFF, SVG (other types will likely need more work, since they aren\'t currently shown in the browser).

![image62](images/entries/447f201d2342a64912bbef1e1d0aa3ebb8963ae4.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)
### Mogelijkheid: Aanpassen van in de Browser weergegeven items toestaan
You can now customize items shown in the browser. User can decide (in the Interface Customization dialog) to hide some of the root items in the browser panel (e.g. Favourites, or POSTGIS provider, \...)

![Screenshot 2020-01-09 at 09 17 05](https://user-images.githubusercontent.com/804608/72050388-466f5600-32c1-11ea-94f5-092cc8471243.png)

Dit werd mogelijk gemaakt door Limerick City and County Council

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Mogelijkheid: Actie Vernieuwen toegevoegd aan OGC-services
U kunt nu de services van OGC in de Browser vernieuwen. Hieronder staat een voorbeeld over hoe deze functie werkt in de verbindingen WMS/WMTS:

![OGCrefreshonaction](https://user-images.githubusercontent.com/2663775/71974919-cfd04b00-3223-11ea-834d-ff016c70a8c6.gif)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
## Gegevensproviders
### Mogelijkheid: Gewijzigd pictogram WMTS laag verzamelen
Dit was een wijziging van het pictogram dat werd gebruikt voor het item voor de verzameling WMTS-lagen, een schema voor een database werd gebruikt, in plaats van een aan WMTS gerelateerd pictogram. Een algemeen pictogram voor WMS wordt nu gebruikt.

Dit werd mogelijk gemaakt door [Kartoza](http://kartoza.com/)

Deze mogelijkheid werd ontwikkeld door [Samweli Mwakisambwe](http://samweli.github.io/)
### Mogelijkheid: Toegevoegde eigenschap voor URL Metadata op de tab Metadata voor de lagen van services voor WMS / WMTS en WCS
Dit werd mogelijk gemaakt door [Kartoza](http://kartoza.com/)

Deze mogelijkheid werd ontwikkeld door [Samweli Mwakisambwe](http://samweli.github.io/)
### Mogelijkheid: Ophalen en weergeven van dimensies voor metadata voor metadata van een WMS-laag
![image65](images/entries/d058ac6b89a8d06169b06580843967ad26e1ef54.webp)

Dit werd mogelijk gemaakt door [Kartoza](http://kartoza.com/)

Deze mogelijkheid werd ontwikkeld door [Samweli Mwakisambwe](http://samweli.github.io/)
### Mogelijkheid: Actie Vernieuwen toegevoegd aan items voor OGC-services
![image66](images/entries/7ce331ee78be7f8b0693c653ecc58916d70a1a92.gif)

Dit werd mogelijk gemaakt door [Kartoza](http://kartoza.com/)

Deze mogelijkheid werd ontwikkeld door [Samweli Mwakisambwe](http://samweli.github.io/)
### Mogelijkheid: 3D gestapelde mazen
MDAL en QGIS ondersteunen nu 3D gestapelde mazen, in het bijzonder voor de indeling TUFLOW-FV. Voor deze uitgave dient u de van toepassing zijnde methode voor gemiddelde te kiezen in de interface van QGIS en dan kunt u door de gegevens bladeren, soortgelijk als voor elke andere 2D gegevensset.

![image67](images/entries/dc3d85153d9bcecdf7ebbc6433c7cb40319e00dd.webp)

Dit werd mogelijk gemaakt door [TUFLOW](http://www.tuflow.com)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Verscheidene problemen met codering van Shapefile gerepareerd
Dit repareert de (defect bij ontwerpen ervan?) afhandeling van de codering van Shapefile, wat a jaren een doorlopend probleem was in QGIS.

Bekijk de discussie op
- [#21264](https://github.com/qgis/QGIS/issues/21264)
- <http://osgeo-org.1560.x6.nabble.com/Shapefile-with-file-cpg-codepage-td5275106.html>
- <http://osgeo-org.1560.x6.nabble.com/QGIS-ignore-the-cpg-files-when-loading-shapefiles-td5348021.html>

(+ andere!)

The situation was that we had two different code paths for handling GDAL side attribute decoding OR QGIS side decoding. Unfortunately, they are both incompatible with each other, and due to GDAL API for this, we can\'t unify the two approaches. (More technical detail in the commit log message!)

Dus hebben we nu:
- always do the decoding on QGIS\' side. This allows users to manually override a shapefile\'s declared encoding because they are often incorrect!
- use a port of GDAL\'s shapefile detection logic (it\'s not exposed in GDAL API, so I had to re-implement it here) so that we default to reading shapefiles by respecting the embedded encoding information (via CPG files or DBF LDID information)
- Completely remove the confusing/broken \"Ignore shapefile encoding declaration\" option, as it\'s no longer required \-- users are ALWAYS able to manually change the encoding of shapefiles layers if needed
- Always show users the detected embedded encoding in the layer properties, instead of always showing \"UTF-8\" when the embedded encoding information is used

This should give the best of both worlds \-- a nice default behavior resulting in shapefiles being read with the correct encoding, whilst still allowing users to override this on a layer-by-layer basis as needed.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor bewerken type boog voorr Oracle
In eerdere versies van QGIS was het niet mogelijk enkele typen geometrie te bewerken die afkomstig waren uit een database van Oracle. We hebben daarom ondersteuning toegevoegd voor het bewerken van de volgende typen geometrie:
- CircularString(Z)
- CompoundCurve(Z)
- MultiCurve(Z)
- CurvePolygon(Z)
- MultiSurface(Z)

Dit werd mogelijk gemaakt door Lille Metropole

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Mogelijkheid: Ondersteuning voor rasters van MBTiles in WMS provider
Deze mogelijkheid voegt ondersteuning voor getegelde rasterkaarten van MBTiles toe aan de WMS-provider, zodat het dezelfde paden voor code gebruikt als die voor tegels van WMTS of XYZ. Hier zijn de voordelen van de benadering via de WMS-provider:
- correct op schaal brengen van tegels op schermen met hoge DPI
- beter uiterlijk indien niet naar de eigen resolutie van de tegels gezoomd. WMS-provider gebruikt afgevlakt op schaal brengen terwijl GDAL standaard Nearest neighbor gebruikt.
- map tile showing up while rendering (with GDAL it\'s blank map until everything is loaded)
- mogelijk om de widget met schuifbalk voor schaal te gebruiken
- sneller - voornamelijk een bijeffect van het laden van minder tegels op schermen met hoog DPI

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://api.github.com/users/wonder-sk)
### Mogelijkheid: Eigen PostGIS raster gegevensprovider
Dit is een implementatie van een PostGIS raster gegevensprovider in de bron van QGIS. Tegels worden gecachet in RAM-geheugen.

Dit werd mogelijk gemaakt door Christmas Holidays Inc.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: Weergeven van dimensies voor metadata voor metadata van een WMS-laag
![wms-ttimelayermetadataqgis](https://user-images.githubusercontent.com/2663775/71542497-37f77500-2978-11ea-854b-d9a9ca2d6c77.png)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
### Mogelijkheid: Andere methoden voor gemiddelden voor 3D mazen
QGIS now includes numerous methods for averaging mesh layers (see [related QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158), and for a description of the methods see [TUFLOW documentation](https://fvwiki.tuflow.com/index.php?title=Depth_Averaging_Results).
- SingleLevelAverageMethod (top)
- SingleLevelAverageMethod (bottom)
- MultiLevelsFromTopAveragingMethod
- MultiLevelsFromBottomAveragingMethod
- SigmaAveragingMethod
- DepthAveragingMethod
- HeightAveragingMethod
- ElevationAveragingMethod

![Screenshot 2019-12-19 at 13 59 47](https://user-images.githubusercontent.com/804608/71175509-068bf480-2268-11ea-9d60-adad896912e2.png)

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Mogelijkheid: OGC API - objectenrovider
This new provider is a client-side implementation of the recently adopted [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) specification, previously known as WFS3. It is integrated within the graphical user interface of the WFS provider, and leverages its core mechanisms to offer background downloading of features, using paging, and a local cache of already downloaded features for a smoother interactive use of datasets.

![image70](images/entries/d74a13f520336e0c2e44469ee4e527188e2466de.webp)

This feature was funded by [Planet](https://planet.com)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com)
## QGIS Server
### Mogelijkheid: QGIS ontwikkelingsserver toepassing
**QGIS Development HTTP Server**

Dit is een kleine onafhankelijke toepassing voor de opdrachtregel die een minimale HTTP ontwikkelingsserver voor QGIS Server implementeert.

Dit kan nuttig zijn bij het ontwikkelen en testen van projecten, modules enplug-ins voor QGIS Server, zonder een volledige webserver/FCGI stack nodig te hebben.

![qgismapserver](https://user-images.githubusercontent.com/142164/73081781-84c36280-3ec8-11ea-9285-ab4c41e3082c.gif)
``` bash
Usage: qgis\_mapserver [options] [address:port]
QGIS Development Server

Options:
-h, --help Displays this help.
-v, --version Displays version information.
-l Sets log level (default: 0)
0: INFO
1: WARNING
2: CRITICAL
-p Path to a QGIS project file (*.qgs or* .qgz),
if specified it will override the query string MAP argument
and the QGIS\_PROJECT\_FILE environment variable

Arguments:
addressAndPort Listen to address and port (default: "localhost:8000")
address and port can also be specified with the environment
variables QGIS\_SERVER\_ADDRESS and QGIS\_SERVER\_PORT
```
Voorbeeld uitvoer:

`bash QGIS Development Server listening on http://localhost:8000 CTRL+C to exit 127.0.0.1 [lun gen 20 15:16:41 2020] 5140 103ms "GET /wfs3/?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 3298 2ms "GET /wfs3/static/jsonFormatter.min.js HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1678 3ms "GET /wfs3/static/jsonFormatter.min.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1310 5ms "GET /wfs3/static/style.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:43 2020] 4285 13ms "GET /wfs3/collections?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200`

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files. Adds missing parameters to GetDxf request

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Mogelijkheid: Ondersteuning voor JSON toegevoegd aan WMS GetLegendGraphic
This feature adds support for GetLegendGraphic responses encoded as JSON. It builds on previous work by \@pblottiere, who added QgsLegendRenderer::exportLegendToJson for that exact purpose.

Bijvoorbeeld een verzoek GetLegendGraphic met FORMAT=image/png dat de afbeelding produceert

![image72](https://user-images.githubusercontent.com/76594/64876231-fbb13a80-d64e-11e9-83e5-120fb1bc0ea8.png)

zal het volgende produceren met FORMAT=application/json

De afbeelding van het pictogram is gecodeerd in base64, en direct weer te geven in een webpagina.

Deze mogelijkheid werd ontwikkeld door Éric Lemoine
## Programmeerbaarheid
### Mogelijkheid: Methoden voor digitaliseren van vormen weergeven in QgisInterface
The actions to trigger the drawing tools were not exposed in the API, if you wanted to do an action for one of these tools, you had to recreate classes. So a call of the type `qgis.utils.iface.actionCircleCenterPoint().trigger()` simplifies programmability.

Dit werd mogelijk gemaakt door de QWAT/QGEP group

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Stephen Knox
| Bug Title | URL issues (if reported) | URL PR or commit |----|----|----|----| | Allow editing of postgres JSON fields from Text Edit Widget | [#29361](https://github.com/qgis/QGIS/issues/29361) | [#30758](https://github.com/qgis/QGIS/pull/30758)

Deze mogelijkheid werd ontwikkeld door Stephen Knox
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| \"Recent\" Group do not appear when opening the \"Select by expression\" dialog | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) |
| QGISserver cannot find shp; tries to open absolute instead of relative path | [#33200](https://github.com/qgis/QGIS/issues/33200) | [PR #33925](https://github.com/qgis/QGIS/pull/33925) | riskant |
| unreported: wrong link in server WFS3 items page (too many slashes) | niet gerapporteerd | [PR #33926](https://github.com/qgis/QGIS/pull/33926) | riskant |
| Qgis scans raster tables on connection to postgis | [#33885](https://github.com/qgis/QGIS/issues/33885) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Layer Properties Information tab - formatting problems | [#33862](https://github.com/qgis/QGIS/issues/33862) | [PR #33955](https://github.com/qgis/QGIS/pull/33955) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | werkt bij mij in huidige master |  |
| QgsVectorLayer readStyle does not read scale based visibility | [#33840](https://github.com/qgis/QGIS/issues/33840) | [PR #33987](https://github.com/qgis/QGIS/pull/33987) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Categorized symbolization does not work on bigint columns in QGIS | [#33585](https://github.com/qgis/QGIS/issues/33585) | [PR #33992](https://github.com/qgis/QGIS/pull/33992) | [PR #34290](https://github.com/qgis/QGIS/pull/34290) |
| QGIS fails to apply style file to rasters | [#29427](https://github.com/qgis/QGIS/issues/29427) | geen wijziging vereist, maar wordt nog steeds onderzocht |  |
| copy / paste feature does not work correctly for MultilinestringZ | [#33977](https://github.com/qgis/QGIS/issues/33977) | werkt bij mij in huidige master |  |
| Edit Form shows and saves raw default-values from geopackage, spatialite or sqlite | [#33383](https://github.com/qgis/QGIS/issues/33383) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| Not possible to uncheck layers in Order Panel | [#33854](https://github.com/qgis/QGIS/issues/33854) | [PR #34015](https://github.com/qgis/QGIS/pull/34015) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| PostgreSQL identity column not recognized properly | [#29560](https://github.com/qgis/QGIS/issues/29560) | [PR #34017](https://github.com/qgis/QGIS/pull/34017) | [PR #34291](https://github.com/qgis/QGIS/pull/34291) |
| Spatialite provider does not recognize autoincrement PKs when table definition uses backticks | [#34085](https://github.com/qgis/QGIS/issues/34085) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| QGIS crash when I click on the button \"Manage Map Themes\" | [#33295](https://github.com/qgis/QGIS/issues/33295) | [PR #34090](https://github.com/qgis/QGIS/pull/34090) | [PR #34098](https://github.com/qgis/QGIS/pull/34098) |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | werkt bij mij in huidige master |  |
| QGIS 3.10.2 replace 0 to NULL | [#34118](https://github.com/qgis/QGIS/issues/34118) | [PR #34152](https://github.com/qgis/QGIS/pull/34152) | [PR #34292](https://github.com/qgis/QGIS/pull/34292) |
| Representation for NULL values inconsistent use/display | [#28643](https://github.com/qgis/QGIS/issues/28643) | [PR #34157](https://github.com/qgis/QGIS/pull/34157) | [PR #34293](https://github.com/qgis/QGIS/pull/34293) |
| DB Manager in 3.11 Master can\'t connect to PostGIS Enabled database | [#34132](https://github.com/qgis/QGIS/issues/34132) | [PR #34171](https://github.com/qgis/QGIS/pull/34171) | N/B |
| QGIS doesn\'t respect OGC guidelines for KVP parameters | [#34148](https://github.com/qgis/QGIS/issues/34148) | [PR #34175](https://github.com/qgis/QGIS/pull/34175) | [PR #34294](https://github.com/qgis/QGIS/pull/34294) |
| QGIS 3.10 can\'t find pkey of postgres views | [#34167](https://github.com/qgis/QGIS/issues/34167) | [PR #34179](https://github.com/qgis/QGIS/pull/34179) | [PR #34295](https://github.com/qgis/QGIS/pull/34295) |
| Duplicating a scratch layer ignores added fields | [#34134](https://github.com/qgis/QGIS/issues/34134) | [PR #34199](https://github.com/qgis/QGIS/pull/34199) | [PR #34203](https://github.com/qgis/QGIS/pull/34203) |
| QGIS master project XML is invalid | [#34218](https://github.com/qgis/QGIS/issues/34218) | [PR #34219](https://github.com/qgis/QGIS/pull/34219) | [PR #34297](https://github.com/qgis/QGIS/pull/34297) |
| Full row conditional formatting formats wrong full rows | [#34122](https://github.com/qgis/QGIS/issues/34122) | [PR #34305](https://github.com/qgis/QGIS/pull/34305) | [PR #34315](https://github.com/qgis/QGIS/pull/34315) |
| filter expression error returns true | [#34259](https://github.com/qgis/QGIS/issues/34259) | [PR #34309](https://github.com/qgis/QGIS/pull/34309) | [PR #34512](https://github.com/qgis/QGIS/pull/34512) |
| Fields are shifted when importing a layer with an FID attribute into GeoPackage | [#32927](https://github.com/qgis/QGIS/issues/32927) | [PR #32934](https://github.com/qgis/QGIS/pull/32934) | N/B |
| \"split features\" of PostGIS layers become slow since 3.6 | [#34326](https://github.com/qgis/QGIS/issues/34326) | gesloten: kan het niet reproduceren met een van de (verscheidene) verschafte gegevenssets |  |
| Cannot add/save more than 1 record/feature in a Spatialite layer/table | [#34379](https://github.com/qgis/QGIS/issues/34379) | [PR #34423](https://github.com/qgis/QGIS/pull/34423) | [PR #34513](https://github.com/qgis/QGIS/pull/34513) |
| QGIS crashes when changing \"default value\" in layer property on a point scratch layer, after editing feature | [#34404](https://github.com/qgis/QGIS/issues/34404) | [PR #34428](https://github.com/qgis/QGIS/pull/34428) | [PR #34514](https://github.com/qgis/QGIS/pull/34514) |
| Raster calculator turns one row of pixels into nodata | [#34435](https://github.com/qgis/QGIS/issues/34435) | [PR #34460](https://github.com/qgis/QGIS/pull/34460) | [PR #34511](https://github.com/qgis/QGIS/pull/34511) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| repository files modified by \'make check\' | [#25830](https://github.com/qgis/QGIS/issues/25830) |  |  |
| Runs of testsuite leaves hundreds of directories in \~/.local/share | [#34185](https://github.com/qgis/QGIS/issues/34185) | [Commit 96a7fb8](https://github.com/qgis/QGIS/commit/96a7fb8f5acf3a278919f88c7c5abc4d20b8b6c2) | N/B |
| Drop use of deprecated QgsCoordinateReferenceSystem constructor | [PR #34186](https://github.com/qgis/QGIS/pull/34186) | [Commit b4fa419](https://github.com/qgis/QGIS/commit/b4fa419f7654ea7d1bce666b99f0534c415d8634) | N/B |
| Only look for pointcloud in its installed extension schema | [#33509](https://github.com/qgis/QGIS/issues/33509) | [Commit 1f44b29](https://github.com/qgis/QGIS/commit/1f44b29933bff3b8806bba75b761dd47b6c349c8) | N/B |
| QGIS 3.10 unable to load PostGIS-table on MacOS Catalina | [#32558](https://github.com/qgis/QGIS/issues/32558) | [Commit d15ce6b](https://github.com/qgis/QGIS/commit/d15ce6b4c30f9faed8b818c575d6b729192fa064) | [Commit a06b164](https://github.com/qgis/QGIS/commit/a06b164b5465ee7a0f8509e737d7c71ea7c166db) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Sandro Santilli
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash when applying wrong filter to OAFeat layer | [#33878](https://github.com/qgis/QGIS/issues/33878) | [PR #33927](https://github.com/qgis/QGIS/pull/33927) | [PR #33958](https://github.com/qgis/QGIS/pull/33958) |
| Oracle provider: fix compiler warnings | - | [PR #33930](https://github.com/qgis/QGIS/pull/33930) | - |
| Cannot import 3D vector into Spatialite datasource (works for GPKG) | [#33883](https://github.com/qgis/QGIS/issues/33883) | [PR #33938](https://github.com/qgis/QGIS/pull/33938) | [PR #33945](https://github.com/qgis/QGIS/pull/33945) |
| \[Oracle\] Fix MultiSurface with straight polygon | - | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | niet te doen |
| Geometries stored in Oracle table fail sdo_geom.validate_geometry_with_context(..) check | [#29085](https://github.com/qgis/QGIS/issues/29085) | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | niet te doen |
| QGIS WFS / OGC API -- Features not showing list typed attributes correctly | [#33758](https://github.com/qgis/QGIS/issues/33758) | [PR #33983](https://github.com/qgis/QGIS/pull/33983) | N/B |
| Legend causing a crash | [#32913](https://github.com/qgis/QGIS/issues/32913) | [PR #34004](https://github.com/qgis/QGIS/pull/34004) | [PR #34063](https://github.com/qgis/QGIS/pull/34063) |
| Draw effects units setting doesn\'t persist | [#34089](https://github.com/qgis/QGIS/issues/34089) | [PR #34135](https://github.com/qgis/QGIS/pull/34135) | [PR #34151](https://github.com/qgis/QGIS/pull/34151) |
| Bad georeferencing of OZI .map | [#34299](https://github.com/qgis/QGIS/issues/34299) | [GDAL commit](https://github.com/OSGeo/gdal/commit/7bedf61bbb8d8c331642b44f30c083abb43f4085) | - |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Remove verbose wording on layout toolbar buttons | [#30161](https://github.com/qgis/QGIS/issues/30161) | [PR #33912](https://github.com/qgis/QGIS/pull/33912) |  |
| Unable to paste a layer in an empty project | [#26710](https://github.com/qgis/QGIS/issues/26710) | [PR #33961](https://github.com/qgis/QGIS/pull/33961) | [PR #33965](https://github.com/qgis/QGIS/pull/33965) |
| DB Manager: Create Layer dialog should be closed or cleared once the new layer is generated | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #33910](https://github.com/qgis/QGIS/pull/33910) |  |
| Two different default shortcuts for the Layer styling panel (F7 vs Ctrl+3) | [#26696](https://github.com/qgis/QGIS/issues/26696) | [PR #33984](https://github.com/qgis/QGIS/pull/33984) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Repareert compilatie op Arch Linux | Niet gerapporteerd | [PR #34110](https://github.com/qgis/QGIS/pull/34110) | [PR #34146](https://github.com/qgis/QGIS/pull/34146) |

| Move labels doesn\'t work with GPKG QGIS 3.4 | [#30408](https://github.com/qgis/QGIS/issues/30408) | Closed (works on master and 3.10) | - |

| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Feedback (works on master and 3.10) | - |

| Labels Buffer DD options do not have fields set and do not render in map canvas | [#28544](https://github.com/qgis/QGIS/issues/28544) | [PR #34153](https://github.com/qgis/QGIS/pull/34153) | risky |

| QGIS does not load embedded layers when opening projects | [#34060](https://github.com/qgis/QGIS/issues/34060) | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Embedded layers are duplicated after opening | Unreported | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Raise log level of server exception | [Discussed on qgis-developers list](https://lists.osgeo.org/pipermail/qgis-developer/2020-February/060108.html) | [PR #34256](https://github.com/qgis/QGIS/pull/34256) | [PR #34539](https://github.com/qgis/QGIS/pull/34539) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with relations | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34255](https://github.com/qgis/QGIS/pull/34255) | - |
| Crash with relations V2 | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34403](https://github.com/qgis/QGIS/pull/34403) | gereed |
| Fix map layer actions rendering in attribute table | Niet gerapporteerd | [PR #34266](https://github.com/qgis/QGIS/pull/34266) | gereed |
| DnD improvements (sync selections) | [#28570](https://github.com/qgis/QGIS/issues/28570) | [PR #34411](https://github.com/qgis/QGIS/pull/34411) | NOG TE DOEN? |
| DnD improvements (container config) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34433](https://github.com/qgis/QGIS/pull/34433) |  |
| DnD improvements (do not hide behind double click) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34479](https://github.com/qgis/QGIS/pull/34479) |  |
| disable browsing auto pan/scale in attribute table when showing visible features only | [#34486](https://github.com/qgis/QGIS/issues/34486) | [PR #34493](https://github.com/qgis/QGIS/pull/34493) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/B |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplicaat | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Gesloten (gerepareerd in 3.10 en master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | NOG TE DOEN |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Gesloten (geen probleem van QGIS) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | NOG TE DOEN |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | NOG TE DOEN |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | NOG TE DOEN |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Bertrand Rix
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/B |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplicaat | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Gesloten (gerepareerd in 3.10 en master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | NOG TE DOEN |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Gesloten (geen probleem van QGIS) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | NOG TE DOEN |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | NOG TE DOEN |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | NOG TE DOEN |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Close vertex for line when editing | [#32359](https://github.com/qgis/QGIS/issues/32359) | [PR #34217](https://github.com/qgis/QGIS/pull/34217) | [PR #34285](https://github.com/qgis/QGIS/pull/34285) |
| Fix Grass linking on FreeBSD | gerapporteerd op de mailinglijst van FreeBSD | [PR #34088](https://github.com/qgis/QGIS/pull/34088) | [PR #34238](https://github.com/qgis/QGIS/pull/34238) |
| \[Regular Shape\] Allow undo click when digitizing new features | [#25597](https://github.com/qgis/QGIS/issues/25597) | [PR #34080](https://github.com/qgis/QGIS/pull/34080) | [PR #34302](https://github.com/qgis/QGIS/pull/34302) |
| Remove Added Vertex with Add Circular String | [#29688](https://github.com/qgis/QGIS/issues/29688) | [PR #34058](https://github.com/qgis/QGIS/pull/34058) | [PR #34301](https://github.com/qgis/QGIS/pull/34301) |
| Rubberband not working correctly with \"Shapes\" digtizing in rotated map window | [#33287](https://github.com/qgis/QGIS/issues/33287) | Duplicaat |  |
| Digitizing: LineStringZ does not inherit Z-coordinates from points if line starts by snapping to a point with no Z coordinate | [#33201](https://github.com/qgis/QGIS/issues/33201) | [PR #33642](https://github.com/qgis/QGIS/pull/33642) | [PR #33951](https://github.com/qgis/QGIS/pull/33951) |
| Split feature makes QGIS 3.4.6 crash | [#33408](https://github.com/qgis/QGIS/issues/33408) | Al gerepareerd |  |
| Fix oriented minimum bounding box algorithm | [#33532](https://github.com/qgis/QGIS/issues/33532) | [PR #34334](https://github.com/qgis/QGIS/pull/34334) | [PR #34338](https://github.com/qgis/QGIS/pull/34338) |
| error with returned angle by orientedMinimumBoundingBox() | [#31371](https://github.com/qgis/QGIS/issues/31371) | Gesloten. Gebrek aan terugkoppeling |  |
| Fix build with txt2tags \>= 3.5 | direct gerapporteerd bij FreeBSD-onderhouder van QGIS | [PR #34377](https://github.com/qgis/QGIS/pull/34377) | [PR #34389](https://github.com/qgis/QGIS/pull/34389) |
| Fix identify menu when an expression is used as display name | niet gerapporteerd | [PR #34361](https://github.com/qgis/QGIS/pull/34361) | [PR #34402](https://github.com/qgis/QGIS/pull/34402) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Sebastien Peillet
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Extend line does not work in compoundCurvedZ layer | [#32080](https://github.com/qgis/QGIS/issues/32080) | [PR #34055](https://github.com/qgis/QGIS/pull/34055) |  |
| Feature attribute selection design bug | [#29542](https://github.com/qgis/QGIS/issues/29542) | [PR #34359](https://github.com/qgis/QGIS/pull/34359) |  |
| Unable to add a new feature when joining two PostGIS tables | [#33148](https://github.com/qgis/QGIS/issues/33148) | [PR #34216](https://github.com/qgis/QGIS/pull/34216) |  |
| Copy/Paste fails from one layer to another when layer has NOT NULL constraints and transaction groups are enabled | [#29603](https://github.com/qgis/QGIS/issues/29603) | Already fixed by [PR #33688](https://github.com/qgis/QGIS/pull/33688) |  |
| QGIS freezes when creating new shapefiles | [#32069](https://github.com/qgis/QGIS/issues/32069) | Al gerepareerd |  |
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) |  |
| BUG: fix invalid layer result when Oracle version is under 12 | niet gerapporteerd | [PR #34546](https://github.com/qgis/QGIS/pull/34546) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix IN/NOT IN evaluation with very long number like strings | [#34314](https://github.com/qgis/QGIS/issues/34314) | [Commit 167e0de](https://github.com/qgis/QGIS/commit/167e0de65b0106a3c19181a2c415c2b0ba0da117) | [Commit aca059a](https://github.com/qgis/QGIS/commit/aca059a82021cb05b58664d3b0f2db751b8f37df) |
| \[processing\] Define Layer Projection tool should write .prj files using ESRI WKT1 format | [#34007](https://github.com/qgis/QGIS/issues/34007) | [Commit f41dd11e](https://github.com/qgis/QGIS/commit/f41dd11e9214b4d6ca5dcc31c6612a65d134ce83) | Ingediend |
| Show \'unknown CRS\' in status bar instead of blank text when project is set to an unknown CRS | [#33458](https://github.com/qgis/QGIS/issues/33458) | [Commit c6319b2](https://github.com/qgis/QGIS/commit/c6319b263992c9d52646096d851cab6c674125ff) | Ingediend |
| Don\'t force users to make a choice in the datum transform dialog | [#34234](https://github.com/qgis/QGIS/issues/34234) | [Commit 644a552](https://github.com/qgis/QGIS/commit/644a5525ec08a77b4c703a7066c94802bbfa1036) | Ingediend |
| Fix crash when changing raster data source | [#34231](https://github.com/qgis/QGIS/issues/34231) | [Commit caf334e6](https://github.com/qgis/QGIS/commit/caf334e65b11f9ee1590f74fe395e97d92bbe699) | [Commit b4142c3](https://github.com/qgis/QGIS/commit/b4142c3832b9f14de97df08caf20a06dee12c02f) |
| Handle unit type \"m\" in custom WKT strings on proj 6 builds | [#34196](https://github.com/qgis/QGIS/issues/34196) | [Commit bb20cee](https://github.com/qgis/QGIS/commit/bb20cee00a931da46b830f0d1e9565d9863f9ba3) | [Commit 97c50f9](https://github.com/qgis/QGIS/commit/97c50f929fbbdd9b3eaef8f8bdf423f9daa3a163) |
| Show full CRS WKT for custom CRS in layer properties | [#33862](https://github.com/qgis/QGIS/issues/33862) | [Commit 19d58bda](https://github.com/qgis/QGIS/commit/19d58bda08c202b29020a3e9c485fac80350fc79) | [Commit 2908227](https://github.com/qgis/QGIS/commit/2908227f91ccfde245a0a608b50b7758b3eba8dd) |
| \[processing\] Fix modeler draws lines to wrong output when connecting green output boxes | Niet gerapporteerd | [Commit 5ae9807](https://github.com/qgis/QGIS/commit/5ae9807303e909a504288d97a2efc4cc04a62670) | [Commit 528a45d](https://github.com/qgis/QGIS/commit/528a45d7453b7cbeb44450d5c81de80c8dd66611) |
| \[processing\] Fix Points Along Geometry handling of multipart geometries | [#34022](https://github.com/qgis/QGIS/issues/34022) | [Commit 3fb18a2](https://github.com/qgis/QGIS/commit/3fb18a2260cbc432e892a4dacbae0092a775ec9d) | [Commit ac3b446](https://github.com/qgis/QGIS/commit/ac3b446aead90d5ea5cab101807859e5ce6f1b44) |
| \[processing\] Fix QStringList values are not accepted as valid values for multi-field parameters | Niet gerapporteerd | [Commit abcb8d2](https://github.com/qgis/QGIS/commit/abcb8d20c66b3c235802b10e68d6abc34736e2c5) | [Commit d421313](https://github.com/qgis/QGIS/commit/d421313f05fd0e5a6974568eccd36c4213f41f8f) |
| \[processing\] Fix some field names are rejected in modeler for non-multi field parameters | Niet gerapporteerd | [Commit 9bcd980](https://github.com/qgis/QGIS/commit/9bcd98094c015265e7e94c55f248248e56c24e51) | N/B - alleen 3.12 |
| Fix crash in server feature info | Niet gerapporteerd | [Commit b3f37fde](https://github.com/qgis/QGIS/commit/b3f37fde9bc4785aebca29e6553d6c1de715f523) | Ingediend |
| Fix overflow by assigning double max to float, invalid min | Niet gerapporteerd | [Commit 2b15e255](https://github.com/qgis/QGIS/commit/2b15e255eaf63f1d45b8e963fca7f9f9e4bf8d40) | N/B - alleen 3.12 |
| Fix crash in QgsGeometryDuplicateCheck due to heap use after free | Niet gerapporteerd | [Commit 195576e](https://github.com/qgis/QGIS/commit/195576e57f0aff064e962ce16b37533ab4924dce) | [Commit dc647bc](https://github.com/qgis/QGIS/commit/dc647bc56fb37207a75d55638926e7a2db75a8be) |
| Fix crash on destruction of QgsPointLocator, if object is destroyed while indexing is happening in the background | Niet gerapporteerd | [Commit 08adb23](https://github.com/qgis/QGIS/commit/08adb23a7ec284a2f84ecf7ac469fbe9004ab57e) | N/B - alleen 3.12 |
| Fix crashes when reading certain resampled raster files | [#33711](https://github.com/qgis/QGIS/issues/33711) | [Commit b2c5a45](https://github.com/qgis/QGIS/commit/b2c5a456fa4e9613ac33b8aaaed774ad3b7293a1) | [Commit 388277e](https://github.com/qgis/QGIS/commit/388277e642d99b93bd7f25197d6418b5dfb888bd) |
| Fix use after free in 3d point symbol | Niet gerapporteerd | [Commit df7979c](https://github.com/qgis/QGIS/commit/df7979cf94c43352cd10db97c16075b8816ec6c4) | [Commit 7204de2](https://github.com/qgis/QGIS/commit/7204de27f3305146fbd6f8e32355c365030afc31) |
| Fix leaks in geometry generator symbol layer | Niet gerapporteerd | [Commit 1610fb8](https://github.com/qgis/QGIS/commit/1610fb8766a13351bb303ee3bfd6301dbdc6648b) | [Commit 3944db4](https://github.com/qgis/QGIS/commit/3944db47dda6b08ea4b22f61c5e72d97597362b1) |
| Fix crash in rendering on proj 6 builds | [#33902](https://github.com/qgis/QGIS/issues/33902) | [Commit 8a71091](https://github.com/qgis/QGIS/commit/8a7109163a9362af2a5e0187cf2b57fc0219fe59) | [Commit f41076d](https://github.com/qgis/QGIS/commit/f41076d45f5f259c50e3ead2cac4d664be11bbfb) |
| Don\'t try to label empty geometries | [#33931](https://github.com/qgis/QGIS/issues/33931) | [Commit 1144974](https://github.com/qgis/QGIS/commit/11449743788f3fd346c01c46cff01bcf3f84edf0) | N/B - alleen 3.12 |
| Fix crashes when attempting to export reprojected raster layers | [#33801](https://github.com/qgis/QGIS/issues/33801) | [Commit bbd055c](https://github.com/qgis/QGIS/commit/bbd055ca13a3d6ee150251222d73e3b9e76d94c5) | [Commit 2fff8e1](https://github.com/qgis/QGIS/commit/2fff8e1205daffafa257b9312cc2c005b5e3017e) |
| Fix shapefile encoding issues | [#21264](https://github.com/qgis/QGIS/issues/21264) | Ingediend | Uitgesteld tot 3.10.4 |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
