---
HasBanner: false
draft: false
releaseDate: '2020-10-23'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.16
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.16{#changelog316 }
![image1](images/projects/dbc0cef663f2f652e0961ac2ed168eb45ed2e182.png)

Datum uitgave 23-10-2020

Weer een bijzondere dag voor het project QGIS! De nieuwe uitgave met ondersteuning voor de langere termijn brengt een breed bereik aan mogelijkheden voor zowel QGIS Desktop als voor QGIS Server. Deze uitgave brengt heel veel nieuwe opties voor in kaart brengen in 3D, maken van mazen vanuit andere gegevenstypes, aanvullende gereedschappen voor ruimtelijke analyses, verbeteringen aan symbologie en gebruikersinterface, om er maar een paar te noemen! Veel gereedschappen zijn toegevoegd aan het nog steeds uitbreidende framewerk van Processing, en de browser van QGIS ondersteunt nu geavanceerde functionaliteit voor interactie met databases die eerder was gereserveerd voor de plug-in DB Manager. Dit zijn een aantal verbeteringen die in deze uitgave zijn geïntroduceerd, en gebruikers van de vorige LTS zullen een aanzienlijk aantal nieuwe beschikbare mogelijkheden zien sinds 3.10. We zijn verheugd enkele toegevoegde hoogtepunten van deze uitgave in detail hieronder weer te geven.

**Dankwoord**

We willen nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://www.qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende leden](https://www.qgis.org/nl/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Easter eggs toegevoegd voor gebruikersgroepen
Typ de woorden \"user groups\" in het huidige venster Coördinaat en zie de magie gebeuren.

![image2](images/entries/079434bceb5004b0ee2c4ad5d62edd1290c28575.webp)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Tijdbeheer
### Mogelijkheid om geanimeerde frames van Tijdbeheer te exporteren
Maakt het exporteren van geanimeerde frames van Tijdbeheer naar opvolgende afbeeldingen mogelijk, om ze later samen te voegen in een externe toepassing. Gebruikers hebben precieze controle over de grootte van de afbeelding en het kaartbereik.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Kaartgereedschap
### Ga naar locatie
We hebben een nieuw filter Ga naar locatie toegevoegd.

De invoer voor Ga naar mag de volgende tekenreeksen zijn:
- Een paar van X- en Y-coördinaten (gescheiden door een komma of spatie).
- Een voor OSM, Leaflet, of OpenLayers opgemaakte URL.
- Een URL voor Google maps.

De logica van de tekenreeks XY is als volgt:
- Als het CRS van het kaartvenster niet WGS84 is:
  - Als het coördinaat past binnen de begrenzingen van WGS84, voeg een resultaat van WGS84 toe (dit wordt gewogen om een hogere prioriteit te hebben dan het resultaat van het CRS van het kaartvenster hieronder).
  - Als het coördinaat past binnen de begrenzingen van het CRS van het kaartvenster, voeg een resultaat toe voor het CRS van het kaartvenster.
- Als het CRS van het kaartvenster WGS84 is:
  - Als het coördinaat past binnen de begrenzingen van  WGS84, voeg een resultaat voor WGS84 toe.

![image3](images/entries/acb9e856ac744d0e40d8de33c025deb075385856.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Gebruikersinterface
### Contextmenu toegevoegd aan kaartvenster 
Het kaartvenster heeft nu een contextmenu voor rechtsklikken. Standaard maakt dat het menu \"Coördinaat kopiëren\" dat werd geïntroduceerd in QGIS 3.14. De verwachting is dat deze functionaliteit zal worden uitgebreid om in de toekomst toegang te krijgen tot ruimtelijke context.

![image4](images/entries/f6e3ce9dca04583c9fa791204fe7e1a3c49c61d0.webp)

Deze mogelijkheid werd ontwikkeld door [jakimowb](https://api.github.com/users/jakimowb)
## Symbologie
### Verbeteringen voor opmaken van vectortegels
Meerder verbeteringen werden geïntroduceerd voor het bewerken van complexe opmaak van vectortegels:
- Helptips weergeven in lijsten, zodat volledige filterregels en namen kunnen worden bekeken, zonder grootte van kolommen aan te moeten passen
- Het zoomniveau van het huidige kaartvenster weergeven in de widgets
- Stelt de gebruikers in staat de lijst met stijlen te filteren om alleen de momenteel zichtbare weer te geven
- Stel het juiste zoomniveau voor het kaartvenster in bij het bewerken van symbolen, zodat voorbeelden van expressies netjes werken

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Gebruikers toestaan optioneel de URL voor de standaardstijl voor verbindingen van vectortegels te specificeren
Bij het instellen van een bronverbinding voor vectortegels is er een nieuwe optie om een URL in te voeren met een configuratie voor de stijl van MapBox GL JSON. Als men die heeft ingevoerd, zal die stijl worden toegepast, elke keer als lagen vanuit die verbinding worden toegevoegd aan QGIS.

Dit werkt ook met verbindingen naar ArcGIS Vector Tile Service die de configuratie voor de standaardstijl gebruiken die is gespecificeerd in de configuratie van de server.

![image5](images/entries/f93d5dca726eb94be82cc47479424b8fe42f5920.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Data-bepaalde verschuiving toestaan voor vulling van symboollagen
Elke vulling voor symboollaag die verschuiving van polygonen ondersteunt, inclusief standaard vullingen, vullingen voor rasterafbeeldingen, vullingen shapeburst en vullingen voor kleurverlopen, staat nu data-bepaalde verschuivingen toe

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Stijlen voor MapBox GL JSON voor lagen van vectortegels importeren 
Gebruikers kunnen nu configuratiebestanden voor stijlen van MapBox GL JSON laden bij het importeren van stijlbestanden voor lagen van vectortegels

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Optie weergeven om standaardpatronen lijn streepje te verschuiven met een vooraf ingestelde hoeveelheid
Staat het aanpassen van het positioneren van streepjes/spaties in de lijn toe, zodat de streepjes/spaties op betere posities kunnen worden geplaatst om rekening te houden met hoeken in de lijn (kan ook worden gebruikt om potentiële aanliggende grenzen van streepjespatronen \"uit te lijnen\").

De verschuiving kan worden ingesteld in verschillende eenheden, inclusief kaarteenheden, en mag ook data-bepaald zijn.

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Opties toegevoegd om dynamisch streepjespatronen aan te passen in standaard lijnsymboollagen
Opties zijn toegevoegd om het aanpassen van streepjespatronen mogelijk te maken om meer beheer voor het verbeteren van de kwaliteit van renderen van lijnsymbolen toe te staan. Deze opties omvatten:
- Streepjespatroon uitlijnen op lijnlengte: Indien geselecteerd zullen de lengtes van het streepjespatroon subtiel worden aangepast om er voor te zorgen dan wanneer een lijn wordt gerenderd, het zal eindigen met een volledige element streepje, in plaats van een element gat of een gedeeltelijk element streepje.
- Streepjespatroon op scherpe hoeken aanpassen: Indien geselecteerd past deze optie dynamisch de plaatsing van het streepjespatroon aan, zodat scherpe hoeken worden weergegeven door een volledig element streepje dat de scherpe hoek ingaat en uitkomt. Het is ontworpen om de onderliggende geometrie beter weer te geven bij het renderen van gestreepte lijnen, speciaal voor gekartelde lijnen.

De volgende afbeeldingen geven de wijziging \"Streepjespatroon uitlijnen op lijnlengte\" in actie weer, met gele lijnen die de ware begin- en eindpositie aangeven van de lijnobjecten die worden gesymboliseerd.

Voor:

![image6](images/entries/87635346-39f11c00-c782-11ea-88bc-369866d7f57a.webp)

Na:

![image7](images/entries/87635368-44131a80-c782-11ea-95d9-07fb7d00ffcf.webp)

![image8](images/entries/e1a4d82c248cdd0f04f236443897178c12574885.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### 3D-symbolen beheren door Stijlmanager
Ondersteuning is toegevoegd voor het beheren van 3D-suymbolen door de Stijlmanager van QGIS, inclusief ondersteuning voor het importeren en exporteren van bibliotheken van 3D-symbolen, en completeert het recente werk in het volledig abstract maken van 3D-symbolen en afhandeling in hun widgets.

Helaas worden er nog geen miniaturen gemaakt voor 3D-symbolen in de bibliotheek, en voorlopig wordt een generiek pictogram gebruikt voor alle 3D-symbolen. Maken van miniaturen is geen eenvoudige opgave, dus is het voorlopig uitgesteld.

Deze mogelijkheid behandelt het probleem dat wordt vermeld in [31479](https://github.com/qgis/QGIS/issues/31479).

![image9](images/entries/7e4ee802abba7dfd7ec61cdd8b3db333b7a30fae.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Labelen
### Optie toegevoegd om gebruikers toe te staan de plaatsing van labels langs objecten lijn te beheren
Een nieuw gedeelte \"Label verankeren\" in de instellingen van lijnen voor de plaatsing van labels geeft gebruikers de mogelijkheid om te specificeren of labels moeten worden geplaatst in het midden, aan het begin of einde van lijnen. In aanvulling daarop maakt het verschuiven van deze posities mogelijk (gebaseerd op het percentage van de lengte van het object), die statisch kan worden gedefinieerd of met een data-bepaalde definitie.

![image10](images/entries/f5cc643fc4eafe75053c134b245e91d2e72e33d0.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ankerpunt voor lijnlabels beheren
Een nieuwe optie wordt weergegeven die gebruikers in staat stelt te beheren of het ankerpunt voor het labelen van objecten een hint is of een strikte eis. Het resulterende gedrag van de aanpassingen omvat het volgende:
- Strikt: Labels worden alleen exact geplaatst op het ankerpunt van het label, en er zijn geen andere plaatsingen om op terug te vallen toegestaan.
- Hint voor voorkeursplaatsing: Het ankerpunt van het label wordt behandeld als een hint voor de voorkeursplaatsing van het label, maar andere plaatsingen nabij het ankerpunt zijn toegestaan.

![image11](images/entries/a6c67225ee3b55a021a395ffbf58bd05352ef6fb.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Diagrammen
### As renderen voor gestapelde staafdiagrammen
Dit voegt ondersteuning toe voor het renderen van de as voor gestapelde staafdiagrammen als een as is ingesteld. De implementatie is gebaseerd op het renderen van de as voor het diagram histogram.

Negatieve waarden worden niet juist afgehandeld door gestapelde staafdiagrammen, met of zonder het weergeven van de as.

Behandelt [Issue 34915](https://github.com/qgis/QGIS/issues/34915)

![image12](images/entries/09739c5bed021a99baec41c98b87f5335a4bf8ec.webp)

Deze mogelijkheid werd ontwikkeld door [Dan Minor](https://api.github.com/users/dminor)
## Mazen
### Vasthouden van gegevenssets met mazen in geheugen
Deze mogelijkheid introduceert de mogelijkheid in geheugen groepen voor gegevenssets voor lagen met mazen te maken. Deze groepen voor gegevenssets zijn tijdelijk en worden niet behouden als het project wordt gesloten.

Een nieuwe optie is toegevoegd aan Mazen berekenen, wat het maken van groepen voor gegevenssets in geheugen toestaat.

Deze mogelijkheid introduceert ook de mogelijkheid om deze geheugengroepen voor gegevenssets te verwijderen of op te slaan naar een bestand met het gespecificeerde stuurprogramma.

![image13](images/entries/85622744-4d9edc00-b635-11ea-91db-a02fa28e6bea.gif)

![image14](images/entries/b27519025102be3b07fc8241f0ff8f8f2f9b31c6.webp)

Dit werd mogelijk gemaakt door [Artelia Group](https://www.arteliagroup.com/en)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Meervoudig Identificeren voor lagen met mazen
Het gereedschap Identificeren is aangepast als het wordt gebruikt in lagen met mazen en geeft nu de waarde van de gegevensset weer die overeenkomt met de huidige tijd van de controller voor Tijdbeheer voor alle groepen van gegevensset. De actieve groepen van de gegevensset (scalair en eventueel vector) worden eerst weergegeven, en daarna de andere groepen van de gegevensset. Er wordt ook andere informatie weergegeven, inclusief:
- Bron waar de gegevensset is opgeslagen
- Tijdstap van de gegevensset die wordt weergegeven (mag een andere zijn dan de tijd van de controller van Tijdbeheer). Geeft niets weer als de groep van de gegevensset niet tijdelijk is
- Zwaartepunt van de corresponderende zijde
- Coördinaat van het gesnapte punt (als er een is gesnapt)
- Midden van de gesnapte rand (als er een is gesnapt)

Wanneer het kaartvenster de navigatie voor Tijdbeheer niet heeft ingeschakeld, bevatten de resultaten van Identificeren alleen informatie over de groepen van de actieve gegevensset waarvan statische gegevenssets zijn gedefinieerd in het dialoogvenster voor de eigenschappen van de mazen.

![image15](images/entries/c4974747f5bc0dcba02f30a97e68bb5edacc5f48.webp)

Dit werd mogelijk gemaakt door [Artelia Group](https://www.arteliagroup.com/en)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Virtuele groepen gegevensset voor laag met mazen
De mogelijkheid om \"virtuele\" groepen voor een gegevensset te gebruiken is geïntroduceerd voor lagen met mazen. Dit vervangt de "geheugen"-groep voor de gegevensset die wordt gebruikt in [37389](https://github.com/qgis/QGIS/pull/37389).

Met Mazen berekenen kunnen gebruikers ervoor kiezen deze \"virtuele\" groepen voor gegevenssets te maken die aan de laag zullen worden toegevoegd. Waarden worden niet in het geheugen opgeslagen, maar elke gegevensset wordt in plaats daarvan berekend als hij nodig is, met de in Mazen berekenen ingevoerde formule.

Deze virtuele groepen voor gegevenssets worden in het project opgeslagen  en kunnen worden verwijderd of opgeslagen naar een bestand om te behouden.

Onderscheid tussen vastgehouden en virtuele groepen voor gegevenssets wordt gemaakt op de tab Bron van de eigenschappen van de laag met mazen door verschillen in de kleur van de achtergrond voor elk item, als volgt aangegeven:

Vastgehouden: geel

Virtueel: paars

![image16](images/entries/86540129-a8a3bf00-bed0-11ea-94b8-bf29b5818cb8.gif)

![image17](images/entries/803983acbaec38e8df0fb4fd12d28beef7399520.webp)

Dit werd mogelijk gemaakt door [Artelia Group](https://www.arteliagroup.com/en)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Exporteren toegevoegd aan de methode QgsMesh
Een methode is toegevoegd aan het exporteren van een triangulatie naar een instance voor QgsMesh, met de mogelijkheid een laag met mazen te construeren uit een triangulatie uit bestaande punten en lijnen. Dit is de eerste stap om de mogelijkheid toe te staan een QgsMesh te verkrijgen uit andere lagen.

De klassen Triangulation en DualEdgeTriangulation werden ook hernoemd en opnieuw opgebouwd om ze meer consistent met de code van QGIS te maken.
- Een methode toegevoegd om de triangulatie naar een instance van QgsMesh te exporteren.

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://api.github.com/users/vcloarec)
### TIN-mazen maken
Lagen van TIN-mazen kunnen worden gemaakt vanuit gegevens van vectorlagen (punten en / of breuklijnen). De resulterende laag met mazen wordt geconstrueerd met een beperkte Delaunay-triangulatie. Deze laag met mazen kan worden gemaakt met de Python API of door een algoritme in de Toolbox van Processing.

![image18](images/entries/fc8a9633b87b29bba052dacd166c0735b4449c90.webp)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Renderen
### Gamma correctiefilter voor rasterlagen
Gamma correctiefilterpijp toegevoegd voor rasterlagen in aanvulling op de reeds bestaande filters voor helderheid, contrast, tint en verzadiging. Gebruikers kunnen de gamma-waarde aanpassen vanuit het dialoogvenster Laageigenschappen, met het stijlpaneel en/of nieuwe knoppen op de werkbalk Raster. Standaard gamma-waarde is 1.0 en die kan worden aangepast binnen het bereik van 0.1 tot en met 10.

Behandelt [Issue 13512](https://github.com/qgis/QGIS/issues/13512)

Voegt ook een test voor de filters voor helderheid en contrast voor renderen toe, die geen enkele test hadden, en repareert enkele waarschuwingen voor vervallen items in de Pythontest voor `QgsRasterLayer`.

![image19](images/entries/bf6076062db63bc4c789bc18d3b029c14b2ddc8e.gif)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
## 3D-objecten
### Toestaan dat 3D materiaal textuurbestanden worden ingebed in stijl/project
Enige kleine opschoning van API en code werd uitgevoerd, als ook de introductie van het gebruiken van QgsImageCache voor 3D textuurbestanden, om toe te kunnen staan dat zij worden ingebed in projecten.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Schaduw renderen
Schaduwen kunnen nu worden gerenderd in 3D-weergaven.

![image20](images/entries/ef724bf261c7740d3cc92238d71d5ecb32a190c3.webp)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### 3D-scenes exporteren 
3D-scenes kunnen nu worden geëxporteerd om te gebruiken in andere 3D-software, zoals Blender. Deze mogelijkheid voor exporteren ondersteunt meerdere aanvullende functies, inclusief vereenvoudiging van het uitvoermodel door de resolutie van de uitvoer te specificeren, optioneel het model glad maken, en het exporteren van 3D-vectorlagen.

![image21](images/entries/91c112ba42358124faec9c3427542524d6b593f9.webp)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Ondersteuning voor richtingslichten voor QGIS 3D
Richtingslichten voor QGIS 3D toegevoegd
- De gebruiker kan nu richtingslichten toevoegen aan de 3D-weergaven.
- Ik voegde een widget tab toe onder het gedeelte Lichten van het dialoogvenster 3D-configuratie.
- De gebruiker kan de richting van het licht, de kleur ervan en de intensiteit specificeren.
- Dit is slechts een duplicaat van de reeds bestaande implementatie van puntlichten, met enkele wijzigingen.
- Later kan het nuttig zijn een manier toe te voegen om de richting van het licht te visualiseren door mazen die zijn geplaatst op het standpunt van de camera. Bijvoorbeeld zoals een pijl die weergeeft hoe de zon de scène in het licht zet.

![image22](images/entries/4dcd7d7f4bcfb71d765656bfe734ec32ddcaca9c.webp)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Ondersteuning voor texturen voor vectorlaag
Ondersteuning voor texturen is toegevoegd voor QGIS 3D met de volgende nieuwe functionaliteiten:
- Gebruikers kunnen nu een afbeelding selecteren vanuit de eigenschappen voor symbolen om weer te geven op de oppervlakte van gebouwen als een diffuse kaart.
- De gebruiker kan nu ook de schaal van texturen vanuit de eigenschappen van symbolen wijzigen.

Enkele visuele problemen kunnen verschijnen bij het gebruiken van texturen. Deze problemen zijn gerelateerd aan de normalen van oppervlakten, die u misschien kunt oplossen door \"Achterzijden toevoegen\" en wat te experimenteren met inverteren van de normalen en de modus Ruimen in de eigenschappen van de symbolen.

![image23](images/entries/1c4fc6ffc1b7a28aeff9c625fb6238998dd30b67.webp)

Deze mogelijkheid werd ontwikkeld door [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Ingebedde en 3D-modellen op afstand voor 3D-puntsymbolen inschakelen
Gebruikers kunnen nu ingebedde en 3D-modellen op afstand voor 3D-puntsymbolen gebruiken.

![image24](images/entries/d4deaabbeddcf5f4784f602f19dabfac22b2d100.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Optie toegevoegd om origine van lichtbron weer te geven
Een mogelijkheid die gebruikers in staat stelt te schakelen met een zichtbare bol op de plaats van origine van de lichtbron in een 3D-scene.

Dit maakt het mogelijk lichtbronnen gemakkelijker opnieuw te positioneren en te plaatsen relatief ten opzichte van de inhoud van de scene.

Behandelt [Issue #37726](https://github.com/qgis/QGIS/issues/37726).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Verbeteringen voor behandeling van materiaal
Verdere verbeteringen voor behandelen van materiaal werd geïntroduceerd, en een schaduwmodel Gooch werd toegevoegd. Dit verbetert de QgsAbstractMaterialSettings API, door:
- Toevoegen van ondersteuning met pictogram voorgeregistreerde typen materiaal (om te gebruiken in het combinatievak voor het selecteren van materiaal).
- Ondersteuning toegevoegd voor afhandeling van verschillende technieken voor renderen aan QgsAbstractMaterialSettings. Nu kunnen klassen van materiaal aangeven welke technieken voor renderen ze ondersteunen (bijv. driehoeken, lijnen, InstancedPoints, etc.), en het materiaal wordt alleen aangeboden als het compatibel is met de gewenste techniek.
- De afhandeling van de techniek in de widget voor materiaal Gooch werd verbeterd om te vermijden dat instellingen worden getoond die geen effect hebben in een bepaalde context (bijv. verbergen van alle, behalve de keuze voor omgevingslicht, voor standaard 2D-lijnsymbolen).
- Een nieuw materiaal, \"Gooch\", werd toegevoegd. Dit materiaal geeft een CAD-stijl 3D-rendering, waarbij de schaduw niet afhankelijk is van de instelling van een toepasselijke verlichting in een scène en waarbij de 3D-details altijd zichtbaar zijn, ongeacht de keuze voor verlichting.

![image25](images/entries/b6df518d57147bfdfd207d4499363c9d4653721b.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Afdruklay-outs
### Beheer weergeven over tekstindeling en uitlijning voor individuele cellen in handmatige teksttabellen
Voegt beheer toe over instellen van de tekstindeling (bijv. vet/cursief/buffer/schaduw etc.) en uitlijnen van tekst (horizontaal en verticaal) voor de inhoud van individuele cellen in een handmatige teksttabel.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### QgsTextRenderer gebruiken om tekst van de attributentabel te renderen
Maakt het mogelijk dat het volledige bereik aan opties voor het opmaken van tekst wordt gebruikt in attributentabellen voor lay-out, inclusief buffers, schaduwen, afstand tussen woorden etc.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### QgsTextRenderer gebruiken om tekst voor het kaartraster te tekenen in lay-outs
Staat annotaties voor het raster toe die buffers, schaduwen, vormen voor de achtergrond, etc. gebruiken

![image26](images/entries/86863750-26550e00-c10f-11ea-8dd4-1b740017949e.gif)

![image27](images/entries/349efbc988ccbf3499e18ec4453b637abf893c38.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Optie weergeven voor beheer van de methode voor compressie van afbeelding naar PDF bij het exporteren van lay-outs naar PDF
Opties zijn voor compressie Met verlies, wat de standaard gebruikte JPEG-compressie is, en compressie Zonder verlies (wat in de meeste gevallen grotere bestanden maakt, maar veel meer geschikt is voor professionele afdrukuitvoeren of voor post-productie in andere producten zoals Illustrator etc.)

Het slechte nieuws is dat deze optie alleen beschikbaar is in builds die zijn gebaseerd op Qt 5.13 of later.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Instellingen voor automatisch clippen toegevoegd voor kaarten als atlas
Deze mogelijkheid stelt gebruikers in staat clippen van kaarten op items voor lay-out in te schakelen, zodat kaartlagen automatisch worden geclipt naar de grenzen van het huidige object van atlas.

Opties bestaan voor:
- Het clippen in- of uitschakelen op een per-kaart basis
- Specificeren van het type clippen:
  - \“Alleen clippen tijdens renderen\”: past een op schilderen gebaseerd clippen toe, zodat delen van vectorobjecten die buiten het object van de atlas vallen, onzichtbaar worden
  - \“Objecten clippen voor renderen\”: past het clippen toe voor het renderen van objecten, dus begrenzingen van objecten die gedeeltelijk buiten het object van atlas vallen zullen nog steeds zichtbaar zijn op de grens van het object van atlas
  - \“Kruisende objecten ongewijzigd renderen\”: rendert slechts alle objecten die kruisen met het huidige object van atlas, maar zonder hun geometrie te clippen
- Beheren of labels geforceerd zouden moeten worden geplaatst binnen het object van atlas, of dat zij buiten het object mogen worden geplaatst
- Beperken van het clippen tot een subset van de lagen in het project, zodat slechts enkele worden geclipt

![image28](images/entries/86433831-191ad680-bd3f-11ea-9289-cc6d2b3e2e11.gif)

![image29](images/entries/1f1343d09c75b0e1d131c25a79b905d7aaadbc35.webp)

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### API aan QgsMapSettings toegevoegd voor het specificeren van toe te passen regio's voor clippen bij renderen van kaarten
Dit is momenteel alleen functionaliteit voor de API, maar functionaliteit is toegevoegd die mogelijkheden aan de achterzijde verschaft om regio's te specificeren voor het clippen die mogen worden gebruikt bij bewerkingen voor het renderen van kaarten.

Hoewel primair geïntroduceerd om functionaliteit te verschaffen die het automatisch clippen van kaartelementen voor het huidige geometrie-object voor atlas in afdruklay-outs mogelijk maakt, is de API opzettelijk op een manier geïmplementeerd die zeer flexibel is. Om verscheidene gebruiksgevallen mogelijk te maken die het clippen van regio\'s vereisen gedurende bewerkingen van het renderen van kaarten.

Voor niet-vectorlagen wordt het clippen toegepast met een pad voor clippen QPainter. Voor vectorlagen geeft de API verscheidene opties weer in hoe het clippen zou moeten worden toegepast:
1. Alleen als een test \"intersects\"-stijl: Alle vectorobjecten die het pad kruisen worden gerenderd, zonder feitelijk de geometrie van het object te clippen
2. Door de geometrie van het object aan te passen en de geometrie te clippen naar een regio: Elke instelling voor lijn of omtrek voor het symbool zal worden gerenderd langs de grens van de te clippen regio. Zelfs als het object gedeeltelijk buiten deze regio valt.

of
1. Gebruiken van een pad voor clippen schilderen: Objecten worden geclipt tot de regio, maar alleen op moment van schilderen. Begrenzingen van het object die buiten de regio voor clippen vallen zullen niet zichtbaar zijn.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Maximale grootte markering voor legenda van lay-out
De mogelijkheid toegevoegd om de maximale grootte voor een markering in te voeren in de widget voor de legenda van de lay-out.

In sommige gevallen, zoals wanneer puntlagen een grootte voor een symbool gebruiken dat is gebaseerd op kaarteenheden, kunnen de markeringen voor de punten in de legenda van de lay-out behoorlijk groot worden. Deze mogelijkheid voegt een instelling toe aan de widget voor de legenda van de lay-out die het mogelijk maakt de maximale grootte van het symbool voor de markering te beperken, terwijl het automatisch bijwerken van de legenda nog steeds actief is.

Deze mogelijkheid werd ontwikkeld door [mhugent](https://api.github.com/users/mhugent)
### Cellen in handmatige teksttabellen toestaan op expressies gebaseerde inhoud te hebben
Staat individuele cellen in een handmatige teksttabel toe dat hun inhoud wordt verkregen uit een vooraf ingestelde expressie. Expressies hebben toegang tot de volledige inhoud voor de expressie van het item voor de lay-out, wat het voor cellen mogelijk maakt stijlwaarden voor metadata  of op samenvoegen gebaseerde berekeningen te berekenen en weer te geven.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Kaarten van lay-out clippen naar vorm
Nieuwe functionaliteit werd geïntroduceerd die het voor gebruikers mogelijk maakt een kaart-item te clippen naar een vorm of item polygoon vanuit hun lay-out, wat niet rechthoekige kaarten binnen de lay-out mogelijk maakt.

![image30](images/entries/88761088-c1428480-d1b1-11ea-90c0-a391d00b084d.gif)

![image31](images/entries/7179282b09e8d196251f543a9c5f059f89c701e2.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ondersteuning voor geroteerde streepjes/annotatie
Markeringen van streepjes en annotaties op een kaartframe in de afdruklay-out kunnen nu worden geroteerd, wat het mogelijk maakt ze uit te lijnen op een geroteerd kaartframe, zoals beschreven in [issue 36904](https://github.com/qgis/QGIS/issues/36904). Het werkt voor zowel geroteerde kaarten als voor opnieuw geprojecteerde rasters.

De volgende opties zijn toegevoegd:
- Streepjes:
  - Rotatie raster volgen (indien niet geselecteerd worden de streepjes getekend zoals eerder, geen rekening houdende met een hoek)
  - Streepjes uitlijnen (of streepjes een constante lengte zouden moeten hebben, of loodrecht zouden moeten worden uitgelijnd)
  - Onder hoek overslaan (een drempel voor de hoek waaronder streepjes niet worden getekend, zodat u streepjes kunt overslaan voor rasterlijnen die bijvoorbeeld te dichtbij zijn om parallel aan de kaartrand te zijn)
- Annotaties:
  - Parallel aan streepje (Naast / Horizontaal / Verticaal stijgend / Verticaal dalend)
  - Lage hoek tekenen (indien geselecteerd zullen overgeslagen streepjes van hierboven toch een annotatie krijgen)

![image32](images/entries/0da542215cefcd2e3ca120dd0381b47611734dce.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
### Expressie voor verschuiving pagina voor posities Y toegevoegd
Een expressie `layout_pageoffsets` werd toegevoegd voor afdruklay-outs die een array met Y-coördinaten teruggeven voor de bovenzijde van elke pagina in de lay-out. Dit maakt het voor gebruikers mogelijk om items dynamisch op pagina's te plaatsen in een context waarbij de grootte van pagina's zou kunnen wijzigen.

Bijvoorbeeld het instellen van een item op 2,5 mm van de bovenzijde van pagina 2 (voor de data-bepaalde positie Y van een kaart-item) : `@layout_pageoffsets[1] + 2.5`

Dit levert een tijdelijke oplossing voor [Issue 37567](https://github.com/qgis/QGIS/issues/37567).

Dit werd mogelijk gemaakt door [BikePlan](https://www.bikeplan.swiss/)

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Expressies
### Functie to_decimal() toegevoegd om DMS te converteren naar DD
Een nieuwe functie `QgsCoordinateUtils::dmsToDecimal` is toegevoegd die de functie `to_decimal` weergeeft in expressies. Dit maakt het mogelijk tekenreeksen DMS (graden/minuten/seconden) te converteren naar de indeling DD (decimale graden).

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Functie \"main_angle\" toegevoegd om de geschatte hoofdhoek van een geometrie terug te geven
Geeft de hoek terug van het georiënteerde minimum begrenzingsvak dat de waarde van de geometrie bedekt.

Nuttig voor data-bepaalde overrides in de symbologie van expressies voor labels, bijv. om labels te roteren zodat zij overeenkomen met de algehele hoek van een polygoon, en soortgelijk voor vulling lijnpatroon. ![image33](images/entries/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)

![image34](images/entries/03463ac0a8303444d94806fb2ff66d6a73c56ccb.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### refFunctions geporteerd naar de bron
Verscheidene functies voor bewerkingen van overleggen zijn toegevoegd aan het programma voor de expressies. Dit dekt de functionaliteit van de plug-in refFunctions.

![image35](images/entries/90797864-7bd92900-e311-11ea-945f-0c2ade14e801.gif)

De volgende nieuwe functies voor expressies werden geïmplementeerd:

    * overlay_intersects(layer[,expression][,filter][,limit][,cache])
    * overlay_contains(layer[,expression][,filter][,limit][,cache])
    * overlay_crosses(layer[,expression][,filter][,limit][,cache])
    * overlay_equals(layer[,expression][,filter][,limit][,cache])
    * overlay_touches(layer[,expression][,filter][,limit][,cache])
    * overlay_disjoint(layer[,expression][,filter][,limit][,cache])
    * overlay_within(layer[,expression][,filter][,limit][,cache])
    * overlay_nearest(layer[,expression][,filter][,limit][,max_distance][,cache])
    
In alle instanties wordt de ruimtelijke operator geëvalueerd tegen de andere laag. Als een expressie is opgegeven, geeft het een array met resultaten terug. Als geen expressie is opgegeven, geeft het een Booleaanse waarde terug die aangeeft of er al dan niet een overeenkomst is met tenminste één object. Objecten mogen optioneel gefilterd worden met een expressie, en kunnen optioneel beperkt worden tot een bepaald aantal.

De functie `overlay_nearest` heeft een aanvullend filter max_distance.

![image36](images/entries/d4bb059729eecfc689e001f731d59fff25225615.webp)

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Digitaliseren
### Optie toegevoegd voor berekenen van richting uit richting van reizen
Voor apparaten die foutieve berekeningen van richtingen rapporteren kan deze optie worden gebruikt om in plaats daarvan de GPS-richting te berekenen, gebaseerd op de vorige twee opgenomen locaties.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Digitaliseren en splitsen van gebogen objecten
Nieuwe functionaliteit werd geïntroduceerd die de mogelijkheid toevoegt om te schakelen tussen lineaire of cirkeltekenreeksen bij het digitaliseren of splitsen van objecten van vectorlagen.

De gebruiker kan de sneltoetscombinatie **Ctrl+Shift+G** gebruiken om te schakelen tussen lineair/cirkel.

Voor het splitsen van objecten zijn nieuwe methoden voor overladen toegevoegd aan de API. Bij het splitsen worden bogen behouden. Hiervoor wordt de boog gesegmenteerd voor het splitsen, en alle gesplitste objecten worden \"gede-segmenteerd\" na het splitsen.

Een knop werd aan de werkbalk toegevoegd om te schakelen tussen lineair/cirkel: ![image37](images/entries/88101713-6505b200-cb6c-11ea-9feb-68a4130d6f52.gif)

![image38](images/entries/86938423-6a93de80-c10e-11ea-8511-489d8b4f006f.gif)

![image39](images/entries/86938444-7089bf80-c10e-11ea-8fd0-0f419f71b52e.gif)

![image40](images/entries/8145ccfa4e659f7d8315830cecfe2b2f391b9aa4.webp)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Gegevensbeheer
### Algoritme Raster opnieuw op schaal brengen voor Processing
Voegt een algoritme toe voor het opnieuw opschalen van een raster om het bereik van rasterwaarden te wijzigen, waarbij de vorm van het histogram van het raster wordt behouden. Nuttig voor wanneer rasters uit verschillende bronnen zouden moeten worden vergeleken of samen zouden moeten worden verwerkt en hun pixelwaarden in hetzelfde bereik zouden moeten liggen. Standaard behoudt het algoritme origineel de waarde NODATA, maar er is een optie om die te overschrijven.

De volgende afbeelding geeft een histogram van een DEM weer (waardenbereik is 85-243). ![image41](images/entries/86897604-53ee8700-c110-11ea-99ae-540d38f88154.webp) En de volgende afbeelding geeft een histogram weer van dezelfde DEM die opnieuw op schaal is gebracht naar het bereik van 100-1000 ![image42](images/entries/86897671-67015700-c110-11ea-8183-e0d6bd013dbb.webp)

Behandelt [Issue 26099](https://github.com/qgis/QGIS/issues/26099).

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
## Formulieren en widgets
### Meerdere widgets voor één enkele relatie
Meerdere widgets voor relatie kunnen nu worden gemaakt voor één enkele relatie, elk met zijn eigen afzonderlijke configuratie.

Deze mogelijkheid wijzigt het gedrag van widgets voor relaties die worden gemaakt in de interface Slepen en neerzetten en verschaft een oplossing voor [Issue 37675](https://github.com/qgis/QGIS/issues/37675).

Bij het lezen van een project dat is geconfigureerd met een oudere versie van QGIS, wordt de configuratie overgenomen en geschreven naar de configuratie van de nieuwe widget. Automatisch gemaakte formulieren staan het maken van widgets voor het bewerken van relaties niet meer toe, maar als het werd geconfigureerd in een oudere versie van QGIS, zal het Formulier attributen nog steeds deze configuratie lezen.

![image44](images/entries/d3a51f9b7ea6ffa3c8c8c457e3d6278d57bcf125.gif)

Deze mogelijkheid werd ontwikkeld door [signedav](https://api.github.com/users/signedav)
### Gerelateerde objecten weergeven in boom van Identificatieresultaten 
Gebruikers zullen nu in staat zijn gerelateerde (kind)objecten te zien in het venster Identificatieresultaten bij het gebruiken van het gereedschap Identificeren. Onder elk geïdentificeerd ouderobject zullen nieuwe groepen zichtbaar zijn die gerelateerde kindobjecten bevatten, hun attributen weergeven, acties, en de gebruiker in staat stellen om direct het objectformulier voor het kindobject te openen.

Deze mogelijkheid behandelt issue [18634](https://github.com/qgis/QGIS/issues/18634).

![image45](images/entries/863b80851b995421b6f2ea455faf6b1c41211cd5.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Filterexpressies in widget Rrelatie-verwijzing
Een optie is toegevoegd om statische filterexpressies te kunnen gebruiken in de widget Relatie-verwijzing.

![image46](images/entries/8048bb8df64e31bb733eea239c527f8be631ce6f.gif)

Deze mogelijkheid werd ontwikkeld door [Ivan Ivanov](https://api.github.com/users/suricactus)
## Analyse-gereedschappen
### Tijden voor laden van profiel van project toegevoegd aan dock voor gereedschappen voor debuggen
Aanpassen van de klasse QgsRuntimeProfiler die de volgende functies uitvoert: 1. Maak het profileren thread-veilig, zodat het mogelijk is tijden vast te leggen over meerdere threads 2. Maakt verschillende \"groepen\" van profielen mogelijk 

De nieuwe API voor groepen is hier gebruikt om een opsomming weer te geven van de tijden voor het laden van het project in het dock voor debuggen, naast het bestaande profileren van QGIS voor opstarten. Het is nu mogelijk een opsomming te krijgen van de verschillende stadia van het laden van een project, om de mogelijke oorzaken van lange tijden voor het laden van projecten te identificeren.

TODO: In het merendeel van de gevallen zullen problemen met de uitvoering worden veroorzaakt door een of meerdere lagen. Het zou dus leuk zijn om de tijden voor het laden van de individuele lagen te kunnen opsommen. Voor een individuele WFS-laag zouden we dan bijvoorbeeld de tijd kunnen zien die het vergt voor de initiële \"server capabilities\" of andere query's. Voeg een groep met profieltijden toe voor het renderen van de kaart, zodat u exact kunt zien welke lagen in uw project lange tijden vragen voor het opnieuw tekenen van de kaart.

In zijn huidige vorm wordt alleen de algehele laadtijd van elke individuele laag weergegeven.

![image47](images/entries/85852208-7bca1a80-b7f3-11ea-8882-b3253622b1b6.webp)

![image48](images/entries/943a79db68aee3458cb88cacd7a69b66fda3caea.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Processing
### Tekenreeks voor Help toegevoegd aan parameters
Tekenreeksen voor Help kunnen nu worden gespecificeerd op het niveau van de parameter.

Dit zal zichtbaar zijn in de helptip, in de CLI en Python Processing API.

![image55](images/entries/2196bcb0123ced5e180ffb2b9469a65a38dcc41b.webp)

Deze mogelijkheid werd ontwikkeld door [Étienne Trimaille](https://api.github.com/users/Gustry)
### Nieuw algoritme \"Punten uitlijnen op objecten\"
Dit algoritme berekent de vereiste rotatie om puntobjecten uit te lijnen met hun dichtstbijzijnde object uit een andere referentielaag. Een nieuw veld wordt toegevoegd aan de uitvoerlaag dat wordt gevuld met de hoek (in graden, met de klok mee) naar het dichtstbijzijnde referentieobject.

Optioneel kan de symbologie van de uitvoerlaag worden ingesteld om automatisch het berekende veld voor de rotatie te gebruiken om markeringssymbolen te roteren.

Indien gewenst kan een maximale te gebruiken afstand worden ingesteld bij het uitlijnen van punten, om te vermijden dat geïsoleerde punten worden uitgelijnd op veraf gelegen objecten.

Een voorbeeld voor een gebruiksgeval is het uitlijnen van puntsymbolen van gebouwen om de dichtstbijzijnde richting van een weg te volgen door een data-bepaalde waarde voor rotatie te gebruiken die wordt gemaakt door dit algoritme.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Algoritme voor Grafische modellen bouwen voor het maken van mappen
Dit algoritme stelt modellen in staat om nieuwe bestandsmappen te maken. Nuttig voor modellen die resultaten moeten uitvoeren naar bepaalde dynamisch gemaakte paden (bijv. een map die de huidige datum bevat).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Algoritme voor Grafische modellen bouwen voor het maken van een expressievariabele voor het project
Stelt een model in staat om expressievariabelen op het niveau van het project in te stellen tijdens de uitvoering. In het bijzonder nuttig met de nieuwe [algoritmes Afdruklay-out exporteren](https://github.com/qgis/QGIS/pull/36916) om modellen toe te staan die dynamisch variabelen instellen die worden gebruikt in een lay-out, voorafgaande aan het exporteren.

Deze functionaliteit werd geporteerd vanaf <https://gis.stackexchange.com/questions/359386>

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Aan algoritmen van Processing toegevoegd om een afdruklay-out als PDF/afbeelding te exporteren.
Modellen zijn in staat om afdruklay-outs te exporteren vanuit het huidige project. Één gebruiksgeval is om gebruikers toe te staan een model in het project te maken dat een bepaalde set lay-outs vanuit het project naar bepaalde mappen exporteert, zodat zij gemakkelijk vanuit het huidige project opnieuw geëxporteerd kunnen worden in één enkele bewerking in plaats van meerdere lay-outs te moeten openen en ze een voor een te exporteren.

Aanvullend, met de nieuwe mogelijkheden om op expressies gebaseerde uitvoerbestanden in modellen te hebben, kunt u automatisch de lay-outs naar een map exporteren met de tag voor de huidige datum en dat opnemen in de geëxporteerde bestandsnamen!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Opgeslagen objecten toevoegen aan bestand van algoritme
Er is nu een eigen algoritme voor Processing om vectorobjecten op te slaan in een gegevensbestand voor een bestand in een model. Het komt met een paar geavanceerde mogelijkheden om opties voor gegevensset en laag door te geven aan GDAL.

![image56](images/entries/b238631365830b019300700cf59c3a8dd3d05a4f.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Algoritme voor exporteren van atlas van lay-out als PDF
Een nieuw algoritme voor Processing van QGIS werd toegevoegd wat het mogelijk maakt een kaartatlas naar PDF te exporteren. Dit is de PDF-variant van het recente algoritme om een atlas van lay-out te exporteren naar een afbeelding.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Nieuw algoritme \"Relatie afvlakken\"
Dit algoritme vlakt alle relaties voor een vectorlaag af, exporteert één enkele laag die één hoofdobject per gerelateerd object bevat. Dit hoofdobject bevat alle attributen voor de gerelateerde objecten.

Het is ontworpen als een snelle manier om een relatie uit een project te de-normaliseren, bijv. om exporteren naar CSV mogelijk te maken.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Algoritme voor exporteren van atlas van lay-out als afbeelding
Een nieuw eigen algoritme voor Processing werd toegevoegd om atlassen van lay-outs te exporteren als afbeeldingen.

Dit is nuttig in modellen waar gegevenssets op afstand worden verwerkt met het doel om te worden gebruikt als bedekkingslagen in atlassen.

![image57](images/entries/e4f315e60743577c9f45ad44643fd5ba9778c040.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Nieuw algoritme Celstatistieken
We hebben een algoritme voor rasteranalyse **Celstatistieken** toegevoegd. Het voert cel-gewijze statistieken uit op ene stapel rasterlagen waarbij rekening wordt gehouden met NoData. De in de huidige implementatie beschikbare functies zijn:

|
- Som
- Gemiddelde
- Mediaan
- Standaardafwijking
- Variantie
- Maximum
- Minimum
- Meerderheid (meest frequent voorkomende waarde)
- Minderheid (minst voorkomende waarde)
- Bereik (max - min)
- Variëteit (aantal unieke waarden)

![image49](images/entries/fca13f48b118ed13ebe84191a226ca0e20c37bfa.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Nieuw algoritme Gelijk aan frequentie
We hebben enkele nieuwe algoritmen voor rasters toegevoegd die werken op een lokale cel-per-cel basis in een stapels rasters. Het  algoritme Gelijk aan frequentie evalueert op een cel-per-cel basis de frequentie (aantal keer) de waarden van een invoerstapel van rasters gelijk zijn aan de waarde van een waardenraster.

![image50](images/entries/e368e10cfa5e19992176930121e0cb846c3d1ca8.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Nieuw algoritme Groter dan frequentie
We hebben enkele nieuwe algoritmen voor rasters toegevoegd die werken op een lokale cel-per-cel basis in een stapels rasters. Het algoritme Groter dan frequentie evalueert op een cel-per-cel basis de frequentie (aantal keer) de waarden van een invoerstapel van rasters groter zijn dan de waarde van een waardenraster.

![image51](images/entries/97228db861367c2875dab0533ab616bb2ac2432c.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Nieuw algoritme Kleiner dan frequentie
We hebben enkele nieuwe algoritmen voor rasters toegevoegd die werken op een lokale cel-per-cel basis in een stapels rasters. Het algoritme Kleiner dan frequentie evalueert op een cel-per-cel basis de frequentie (aantal keer) de waarden van een invoerstapel van rasters kleiner zijn dan de waarde van een waardenraster.

![image52](images/entries/114853cd3d7c245b56edea0024704c853997275c.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Nieuw algoritme Laagste positie in stapel rasters
We hebben enkele rasteranalyse-gereedschappen voor posities van waarden toegevoegd aan deze nieuwe versie van QGIS: Het algoritme *Laagste positie in stapel rasters* evalueert op een cel-per-cel basis de positie van het raster de laagste waarde in een stapel van rasters. Tellen van de positie begint met 1 en loopt tot het totale aantal invoerrasters. De volgorde van de invoerrasters is relevant voor het algoritme.

![image53](images/entries/f3383f5583c9096b1b8d1873679e1a495fac0485.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Nieuw algoritme Hoogste positie in stapel rasters
We hebben enkele rasteranalyse-gereedschappen voor posities van waarden toegevoegd aan deze nieuwe versie van QGIS: Het algoritme *Hoogste positie in stapel rasters* evalueert op een cel-per-cel basis de positie van het raster de hoogste waarde in een stapel van rasters. Tellen van de positie begint met 1 en loopt tot het totale aantal invoerrasters. De volgorde van de invoerrasters is relevant voor het algoritme.

![image54](images/entries/a730b8c1566c99bdebff09c783ae320b0c138d76.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
### Resultaten van Processing laden in groep van lagen
Gebruikers kunnen nu optioneel een naam van een groep instellen die ervoor zorgt dat de resulterende uitvoerlagen die aan het project worden toegevoegd met de optie *Uitvoerbestand openen na uitvoeren algoritme* gegroepeerd worden. Dit maakt het mogelijk dat alle uitvoer van verscheidene algoritmen van Processing wordt gegroepeerd, zodat ze gemakkelijk kunnen worden gevonden in de boom met lagen en worden verwijderd, geëxporteerd, of gemakkelijk hun zichtbaarheid kan worden geschakeld. ![image58](images/entries/414c68839518d5b658d6e6f1565f6c27e1f4336f.gif)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Algoritme Gebiedsstatistieken dat nieuw uitvoer maakt toegevoegd
Eerder, bij het berekenen van gebiedsstatistieken, werkte het algoritme altijd de originele databron bij, aanvullende velden toevoegend. Een nieuw algoritme Gebiedsstatistieken is toegevoegd dat in plaats daarvan een nieuwe uitvoer maakt. Deze functionaliteit is een implementatie van het [29504 feature request](https://github.com/qgis/QGIS/issues/29504).

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Nieuwe parameter geometrie toegevoegd
Een nieuwe `QgisProcessingParameterGeometry` toegevoegd voor het doorgeven van geometrieën als een parameter voor algoritmen van Processing.

Dit verschaft een manier om eenvoudige geometrieën door te geven aan algoritmen zonder een invoerlaag nodig te hebben.

De directe gevallen voor gebruik zijn:
- Algoritmen die geometrieën zouden moeten verwerken op een atomische manier.
- Delegatie vanuit ouderalgoritmen.
- Gebruiken met headless QGIS Processing in zelfstandige gereedschappen voor Processing.

Mogelijkheden:
- De parameter is compatibel met parameters als tekenreeks omdat het Well-Known-Text kan doorgeven als de waarde.
- De huidige interactie van de widget is minimalistisch omdat het alleen de widget voor invoeren van tekst gebruikt voor het invoeren van de waarde als WKT.

Deze mogelijkheid werd ontwikkeld door [David Marteau](https://api.github.com/users/dmarteau)
### Een interface toegevoegd om te bepalen of het veilig is om voor de toepassing om af te sluiten
Een interface voor plug-ins en scripts om aangepaste logica te registreren om te voorkomen dat de toepassing QGIS afsluit werd toegevoegd. Dit maakt het voor plug-ins mogelijk om te bepalen of het veilig is om de toepassing af te sluiten. Dit heeft het mogelijk gemaakt om plug-ins toe te staan te bepalen of er niet opgeslagen wijzigingen zijn die moeten worden opgeslagen of genegeerd vóór QGIS wordt toegestaan af te sluiten, functionaliteit die al was geïmplementeerd in de console scriptbewerker, wat gegevensverlies voorkomt door de gebruikers te laten weten dat er niet opgeslagen wijzigingen zijn in plaats van de toepassing stilletjes af te sluiten.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Opties voor toepassing en projecten
### Beschikbare GDAL vectorstuurprogramma's opsommen
Een tab *Vector Drivers* is nu beschikbaar in het venster QGIS GDAL instellingen, wat de beschikbare vectorstuurprogramma's voor GDAL vermeldt en gebruikers in staat stelt hun actieve status te schakelen. Waar verscheidene stuurprogramma's kunnen worden gebruikt voor het openen van gegevens van een specifiek type, kunnen gebruikers nu deze instellingen aanpassen om ervoor te zorgen dat het bedoelde stuurprogramma wordt gebruikt bij het importeren van specifieke typen vectorgegevens. De stuurprogramma's FileGDB en OpenFileGDB zijn bijvoorbeeld beide in staat om te worden gebruikt voor het importeren van .gdb-bestanden, maar als het gegevensbestand een versie 9.x heeft, kan de FileGDB het niet openen. In dit geval kan de gebruiker het stuurprogramma FileGDB uitschakelen en ervoor zorgen dat in plaats daarvan de gegevens worden geladen met het stuurprogramma OpenFileGDB.

Deze functionaliteit behandelt direct de beperkingen die zijn vermeld in [Issue 18738](https://github.com/qgis/QGIS/issues/18738).

![image59](images/entries/5cc48d8ea8bc276446f8eae4a1c838e0d1f91a40.webp)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### GRASS installatiemap op MacOS detecteren 
MacOS had eerder een platformspecifieke aangepaste parameter voor het instellen van Grass7Utils.GRASS_FOLDER. Dit veroorzaakte crashes voor veel gebruikers met meerdere installaties van QGIS of die enkele ongeldige instellingen voor mappen hadden. De parameter is verwijderd en een omgevingsvariabele GISBASE werd in plaats daarvan geïntroduceerd, die gewoonlijk in scripts voor GRASS wordt gebruikt als de \"root\" installatiemap, wat het gedrag nabootst dat wordt gebruikt voor het detecteren van GRASS in omgevingen van Windows. Als GISBASE niet aanwezig is (standaard), wordt een zoekactie uitgevoerd naar mappen van GRASS in `QgsApplication.prefixPath()` (indien verpakt in bundelindelingen). Indien het niet gevonden wordt, zal naar de zelfstandige instantie van GRASS worden gezocht. Het nieuwe gedrag voor GRASS is in lijn met de methodologie die wordt gebruikt voor de programma\'s van Processing voor GDAL en SAGA.

Dit lost [Issue 38595](https://github.com/qgis/QGIS/issues/38595) op.

![image60](images/entries/e59bb83513293830df8ec4dcf825247b14dacc98.webp)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Peter Petrik)](https://api.github.com/users/PeterPetrik)
## Browser
### Velden weergeven in de Browser
Eerste gedeelte van QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/171>

Geeft veldkolommen weer in de browser voor providers die de API voor verbindingen implementeren:
- PG
- GPKG
- SpatiaLite
- MSSQL

De volgende bewerkingen op velden worden ondersteund:
- Nieuw veld toevoegen
- Veld verwijderen

![image61](images/entries/87223743-a4b7e700-c37f-11ea-88a3-4b371bfadf89.gif)

![image62](images/entries/d4e761ad977a712aa1fc1fbc65d61c886e6e79fb.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
## Gegevensproviders
### Verbindingen ArcGIS Vector Tile Service
Een optie om verbindingen naar ArcGIS Vector Tile Services te maken werd toegevoegd om gebruikers in staat te stellen en gemakkelijk vectortegellagen te laden vanaf vector tegelservices van ArcGIS Server. Ook werd ondersteuning toegevoegd voor authenticatie, configuratie en aangepaste tekenreeks voor verwijzingen aan verbindingen voor vectortegels.

Deze wijziging voegt expliciet opties voor de gebruikersinterface toe voor het toevoegen en configureren van ESRI vector tegelservices. Omdat deze services het standaard vector tegelframewerk voor het ophalen van gegevens gebruiken, kunnen zij direct worden toegevoegd door een verbinding te maken met het API eindpunt VectorTileService op de ArcGIS server.

Nadat een gebruiker een laag toevoegt vanuit een VectorTileService, worden de standaard opmaak en labelen  van de server voor de laag automatisch geladen.

![image63](images/entries/e31c882fa9552ed6bd247f0092305ae8c153948a.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Vermeerderen van metadata van laag vertrouwen
De vlag trust op het niveau van het project wordt alleen gebruikt voor het lezen van het bereik van de vectorlaag vanuit XML, niet vanaf de provider.

Deze vlag was niet beschikbaar op de niveaus van de vectorlaag en de gegevensprovider. Een nieuwe vlag voor lezen van QgsMapLayer voor de vlag read van het project en een nieuwe vlag provider om de configuratie van de databron te vertrouwen.

Vertrouwen van de configuratie van de databron stelt de provider in staat om geschatte metadata te gebruiken, er voor te zorgen dat de primaire sleutel uniek is en dat het te detecteren type geometrie en SRID hetzelfde zijn als werd verzocht.

Deze mogelijkheid werd ontwikkeld door [rldhont](https://api.github.com/users/rldhont)
### Ondersteuning voor virtuele kolommen in Oracle toegevoegd
Ondersteuning voor virtuele (gegenereerde) kolommen van Oracle is toegevoegd en wordt op deze manier gedefinieerd:

`sql CREATE TABLE QGIS.GENERATED_COLUMNS ( "pk" INTEGER PRIMARY KEY, "generated_field" GENERATED ALWAYS AS ('test:' || "pk") VIRTUAL);`

**Opmerking:** Het is niet mogelijk een gegenereerde kolom te definiëren voor een veld SDO_GEOMETRY in Oracle.

Voor nu, bij het maken van een nieuw object, is het gegenereerde veld te bewerken en dat zou niet zo moeten zijn. Een nieuwe methode voor de API dient te worden toegevoegd om een veld alleen-lezen op te halen vanaf de provider, zoals besproken in [Issue 35995](https://github.com/qgis/QGIS/pull/35995#issuecomment-633055700).

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://api.github.com/users/troopa81)
### Geavanceerde opties voor importeren van gegevens toegevoegd
Nieuwe functionaliteit is geïntroduceerd die het mogelijk maakt geavanceerde parameters te specificeren bij het importeren van lagen met de gegevensprovider OGR, openen van een uitgebreid bereik van nieuwe mogelijkheden, speciaal bij het werken rondom verwachte problemen met gegevenssets.

![image64](images/entries/e1c7474d19828b39f5872b289a1e8ba994556a10-1.webp)

![image65](images/entries/4a2d99c6ef6ec12e5f63a29ad00d9ebc3cd534e2.webp)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://api.github.com/users/rouault)
## QGIS Server
### QGIS Server WFS3 API sorteren
Functionaliteit sorteren toegevoegd aan de QGIS Server WFS3 API

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Plug-in voor QGIS Server startpagina 
Een plug-in Landing Page Plugin for QGIS Server werd gemaakt, wat een C++-port is van <https://github.com/elpaso/qgis-server-landing-page-plugin>

![image66](images/entries/a2254bbef892835317a9f608afd8bd3722ee4b38.gif)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Omgevingsvariabele om GetPrint uit te schakelen en geen lay-outs te laden
Een nieuwe omgevingsvariabele `QGIS_SERVER_DISABLE_GETPRINT` werd toegevoegd aan QGIS Server die het laden van lay-outs voorkomt bij het lezen van projecten en schakelt het WMS-verzoek GetPrint uit, wat de leestijd voor projecten verbetert.

Dit werd mogelijk gemaakt door [Ifremer](https://wwz.ifremer.fr)

Deze mogelijkheid werd ontwikkeld door [3Liz](http://www.3liz.com)
### Omgevingsvariabele om metadata van lagen te vertrouwen met instellingen van server
Vertrouwen van metadata van een laag kan worden gedefinieerd op het niveau van het project. Een nieuwe vlag read voor het project werd toegevoegd die het mogelijk maakt het vertrouwen van metadata van de laag te forceren.

Voor QGIS server kan de optie voor het vertrouwen van de metadata van de laag worden overschreven met de omgevingsvariabele `QGIS_SERVER_TRUST_LAYER_METADATA`.

Dit werd mogelijk gemaakt door [Ifremer](https://wwz.ifremer.fr)

Deze mogelijkheid werd ontwikkeld door [3Liz](http://www.3liz.com)
## Belangrijke reparaties
### Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scrolling attribute table of a layer added with the \"delimted text provider\" is almost impossible | [#38068](https://github.com/qgis/QGIS/issues/38068) | [PR #38735](https://github.com/qgis/QGIS/pull/38735) | [PR #38745](https://github.com/qgis/QGIS/pull/38745) |
| support for API-keys via query for API implementing OGC API - Features | [#38436](https://github.com/qgis/QGIS/issues/38436) | [PR #38738](https://github.com/qgis/QGIS/pull/38738) | N/B |
| Custom CRS does not always switch parameters correctly from wkt to proj string | [#38689](https://github.com/qgis/QGIS/issues/38689) | Kan niet worden gereproduceerd |  |
| OGC API Features client always use limit=1000 | [#38666](https://github.com/qgis/QGIS/issues/38666) | Kan niet worden gereproduceerd |  |
| Exporting to geopackage changes field type from DATE to DATETIME | [#37857](https://github.com/qgis/QGIS/issues/37857) | Is geen probleem |  |
| CSV date field being interpreted as time type | [#38091](https://github.com/qgis/QGIS/issues/38091) | [PR #38741](https://github.com/qgis/QGIS/pull/38741) | N/B |
| Coordinate Transformation Difference between QGIS and Proj | [#38190](https://github.com/qgis/QGIS/issues/38190) | probleem van gebruik |  |
| gdal_rasterize not working when file has \'&\' symbol in name | [#38674](https://github.com/qgis/QGIS/issues/38674) | [PR #38743](https://github.com/qgis/QGIS/pull/38743) | [PR #38747](https://github.com/qgis/QGIS/pull/38747) |
| Core dump when using identify feature on a vector polygon | [#36213](https://github.com/qgis/QGIS/issues/36213) | al gerepareerd |  |
| Error of the raster histogram of QGIS 3.10.8(LTR) | [#38298](https://github.com/qgis/QGIS/issues/38298) | [PR #38769](https://github.com/qgis/QGIS/pull/38769) | NOG TE DOEN |
| \[Postgres\] Cannot edit attribute when there is no primary key | [#37917](https://github.com/qgis/QGIS/issues/37917) | is geen probleem IMHO |  |
| Switching between WMS info-output formats throws: CRITICAL QTableWidget: cannot insert an item that is already owned by another QTableWidget | [#37215](https://github.com/qgis/QGIS/issues/37215) | [PR #38770](https://github.com/qgis/QGIS/pull/38770) | [PR #38783](https://github.com/qgis/QGIS/pull/38783) |
| SaveAs Geopackage: TEXT fields are converted to TEXT(255) | [#25405](https://github.com/qgis/QGIS/issues/25405) | al gerepareerd |  |
| \"Join attributes by nearest\" tool defaults to \"None\" when using Max distance of 0 | [#38761](https://github.com/qgis/QGIS/issues/38761) | [PR #38773](https://github.com/qgis/QGIS/pull/38773) | No, not appropriate (see [PR #38778](https://github.com/qgis/QGIS/pull/38778)) |
| Lost edits in layer of same transaction group | [#38697](https://github.com/qgis/QGIS/issues/38697) | [PR #38779](https://github.com/qgis/QGIS/pull/38779) + [PR #38780](https://github.com/qgis/QGIS/pull/38780) | [PR #38824](https://github.com/qgis/QGIS/pull/38824) |
| Preview of Expression String Builder \'freezes\' if Feature id higher then available | [#38646](https://github.com/qgis/QGIS/issues/38646) | [PR #38797](https://github.com/qgis/QGIS/pull/38797) | N/B |
| VectorFileWriter/OGR provider: workaround GDAL 3.1.x bug regarding XLSX and ODS creation | niet gerapporteerd | [PR #38837](https://github.com/qgis/QGIS/pull/38837) | [PR #38853](https://github.com/qgis/QGIS/pull/38853) |
| Coordinate operation widget: avoid repeating scope and remarks | niet gerapporteerd | [PR #38847](https://github.com/qgis/QGIS/pull/38847) | N/B |
| Freeze when showing attribute table of WFS layer | [#37224](https://github.com/qgis/QGIS/issues/37224) | [PR #38952](https://github.com/qgis/QGIS/pull/38952) | [PR #38956](https://github.com/qgis/QGIS/pull/38956) |
| OGR Error when editing a kml file | [#39087](https://github.com/qgis/QGIS/issues/39087) | [GDAL Commit 72e1a4d7c96e0381d2d335857697b5f8e1668450](https://github.com/OSGeo/gdal/commit/72e1a4d7c96e0381d2d335857697b5f8e1668450) | Ook verwerkt in branch GDAL 3.1 |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Loading PostGIS layers with no specified geometry loads all features in the attribute table. | [PR #35367](https://github.com/qgis/QGIS/pull/35367) [#38565](https://github.com/qgis/QGIS/issues/38565) | Alleen voor eerdere versies | [PR #38736](https://github.com/qgis/QGIS/pull/38736) |
| Server API: current project is not settable anymore | [#38755](https://github.com/qgis/QGIS/issues/38755) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) |
| PostGIS layer saved in 3.10 project, fail to load correctly on 3.14 | [#38567](https://github.com/qgis/QGIS/issues/38567) | [PR #38763](https://github.com/qgis/QGIS/pull/38763) | N/B |
| Server WFS-T 1.1.0 wrong case for totalUpdated, totalInserted, totalDeleted | [#38558](https://github.com/qgis/QGIS/issues/38558) | [PR #38764](https://github.com/qgis/QGIS/pull/38764) | NOG TE DOEN |
| Server crashes on GetLegendGraphics when RULE does not exists. | [#38766](https://github.com/qgis/QGIS/issues/38766) | [PR #38775](https://github.com/qgis/QGIS/pull/38775) | [PR #38794](https://github.com/qgis/QGIS/pull/38794) |
| Form view gets stuck in the last shown not-NULL-value for some attributes when browsing through data | [#38552](https://github.com/qgis/QGIS/issues/38552) | [PR #38801](https://github.com/qgis/QGIS/pull/38801) | NOG TE DOEN |
| Marker line Simple marker rotation override not respecting follow line direction setting | [#38716](https://github.com/qgis/QGIS/issues/38716) | [PR #38815](https://github.com/qgis/QGIS/pull/38815) |  |
| Unable to dock the \"snapping options\" widget | [#38604](https://github.com/qgis/QGIS/issues/38604) | werkt bij mij wel |  |
| Can\'t read PG data sources when saved in version 3.10 and using service / auth combo | [#38809](https://github.com/qgis/QGIS/issues/38809) | [PR #38833](https://github.com/qgis/QGIS/pull/38833) | N/B |
| DB Manager \"cancel\" button to stop a query is not working | [#38092](https://github.com/qgis/QGIS/issues/38092) | [PR #38870](https://github.com/qgis/QGIS/pull/38870) | N/B |
| GDAL enhancement related to [#38092](https://github.com/qgis/QGIS/issues/38092) | [#38092](https://github.com/qgis/QGIS/issues/38092)2 | <https://github.com/OSGeo/gdal/pull/2953#event-3788638320> | N/B |
| Shift values issue while creating new field under DB Manager | [#38800](https://github.com/qgis/QGIS/issues/38800) | werkt bij mij wel |  |
| Problem with VUV wms | [#38924](https://github.com/qgis/QGIS/issues/38924) | werkt bij mij wel |  |
| Data Source Manager: WMS/WMTS Window not resizable | [#38903](https://github.com/qgis/QGIS/issues/38903) | werkt bij mij wel, wacht op terugkoppeling |  |
| Form tab option \"Show as group box\" won\'t save or apply | [#38539](https://github.com/qgis/QGIS/issues/38539) | werkt bij mij wel |  |
| Scale lock is ignored when panning the map | [#38953](https://github.com/qgis/QGIS/issues/38953) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/B |
| Zoom to layer overwrites locked scale bug | [#38417](https://github.com/qgis/QGIS/issues/38417) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/B |
| Repeated column names cause visualization issues in DB Manager | [#38976](https://github.com/qgis/QGIS/issues/38976) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/B |
| \"show search_path\" returns 0 rows | [#38975](https://github.com/qgis/QGIS/issues/38975) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/B |
| PG NOTIFY not accessible | [#38986](https://github.com/qgis/QGIS/issues/38986) | werkt bij mij wel |  |
| Fix PG db-manager rename schema | [#38998](https://github.com/qgis/QGIS/issues/38998) | [PR #39000](https://github.com/qgis/QGIS/pull/39000) | N/B |
| Several PG browser items UX issues | [#39001](https://github.com/qgis/QGIS/issues/39001) | [PR #39006](https://github.com/qgis/QGIS/pull/39006) | N/B |
| Virtual vector does not load correctly on Windows | [#35016](https://github.com/qgis/QGIS/issues/35016) | werkt bij mij op Windows/in huidige master |  |
| DB Manager: PostgreSQL field comments are not displayed correctly | [#38394](https://github.com/qgis/QGIS/issues/38394) | [PR #39026](https://github.com/qgis/QGIS/pull/39026) |  |
| Only first row for Postgis raster table in DB Manager preview and when adding layer to Map canvas | [#39017](https://github.com/qgis/QGIS/issues/39017) | [PR #39039](https://github.com/qgis/QGIS/pull/39039) | N/B |
| erroneous postgis query when trying to discover relations | [#39036](https://github.com/qgis/QGIS/issues/39036) |  |  |
| many additional tables that are already loaded in the project are loaded on project load because of layer dependencies | [#39025](https://github.com/qgis/QGIS/issues/39025) | [PR #39043](https://github.com/qgis/QGIS/pull/39043) | N/B |
| Partial fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39071](https://github.com/qgis/QGIS/pull/39071) | N/B |
| Allow to set precision for raster single band presudocolor classification | niet gerapporteerd | [PR #39079](https://github.com/qgis/QGIS/pull/39079) |  |
| Complete fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39088](https://github.com/qgis/QGIS/pull/39088) | Riskant |
| Failure with identifier sequence when adding feature | [#39093](https://github.com/qgis/QGIS/issues/39093) | werkt bij mij wel |  |
| Export report to PDF crashes QGIS if no layout is in edit mode | [#39086](https://github.com/qgis/QGIS/issues/39086) | [PR #39135](https://github.com/qgis/QGIS/pull/39135) | NOG TE DOEN |
| PG raster: float rasters do not show nodata values correctly in master/3.14 | [#39142](https://github.com/qgis/QGIS/issues/39142) | [#39142](https://github.com/qgis/QGIS/issues/39142) |  |
| Python API call QgsAbstractDatabaseProviderConnection::TableProperty exceptions not converted to QgsProviderConnectionException | [#39151](https://github.com/qgis/QGIS/issues/39151) | [PR #39152](https://github.com/qgis/QGIS/pull/39152) | N/B |
| DB Manager unable to show PostGIS geography column | [#37666](https://github.com/qgis/QGIS/issues/37666) | [PR #39154](https://github.com/qgis/QGIS/pull/39154) | N/B |
| setting a field to NULL via field calculator freezes qgis | [#39178](https://github.com/qgis/QGIS/issues/39178) | [PR #39257](https://github.com/qgis/QGIS/pull/39257) | NOG TE DOEN |
| Layer X: Feature has too many attributes (expecting 5, received 7) when \"Automatic Creation of Transaction Group\" is enabled | [#39230](https://github.com/qgis/QGIS/issues/39230) | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | [PR #39278](https://github.com/qgis/QGIS/pull/39278) |
| unreported crash when calling data provider\'s lastError on no errors | niet gerapporteerd | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | N/B |
| Crash digitizing a feature when transaction group is on (after save) | [#39265](https://github.com/qgis/QGIS/issues/39265) | [PR #39283](https://github.com/qgis/QGIS/pull/39283) |  |
| Transaction groups: not-current layers a set to not editable after save | [#39282](https://github.com/qgis/QGIS/issues/39282) | [PR #39286](https://github.com/qgis/QGIS/pull/39286) | niet kritisch |
| OGR decodeUri: be tolerant on layerName case | niet gerapporteerd maar heeft impact op de QGIS-Documentation | [PR #39328](https://github.com/qgis/QGIS/pull/39328) | N/B |
| Wrong extension handling in links when layer name has dots | niet gerapporteerd | [PR #39346](https://github.com/qgis/QGIS/pull/39346) | N/B |
| Passwords are URL-encoded before base64 encoding for HTTP Basic auth | [#39243](https://github.com/qgis/QGIS/issues/39243) | [PR #39347](https://github.com/qgis/QGIS/pull/39347) | [PR #39382](https://github.com/qgis/QGIS/pull/39382) |
| QGIS crash in Settings menu if NOT in english | [#39430](https://github.com/qgis/QGIS/issues/39430) | [PR #39434](https://github.com/qgis/QGIS/pull/39434) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Problem with displaying mesh and canvas rotation | [#35147](https://github.com/qgis/QGIS/issues/35147) | [PR #38795](https://github.com/qgis/QGIS/pull/38795)/files | nee, niet kritisch |
| Crash while attempting to use mesh | [#31773](https://github.com/qgis/QGIS/issues/31773) | Kan niet worden gereproduceerd |  |
| Spatial Bookmark Manager Bad Behavior and Crashing App | [#35348](https://github.com/qgis/QGIS/issues/35348) | Kan niet worden gereproduceerd |  |
| Seqmentation fault 11 on QGIS shutdown on MacOS | niet gerapporteerd | [PR #38806](https://github.com/qgis/QGIS/pull/38806) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| Crash when creating New MSSQL connexion on macOS | [#35026](https://github.com/qgis/QGIS/issues/35026) | [PR #39084](https://github.com/qgis/QGIS/pull/39084) | different packaging system\... |
| qgis_process is installed in the wrong place on MacOS | [#38447](https://github.com/qgis/QGIS/issues/38447) | [Mac Packager Commit 97b0ec974e2309e447ebb69c4117580db27af6f0](https://github.com/qgis/QGIS-Mac-Packager/commit/97b0ec974e2309e447ebb69c4117580db27af6f0) | N/B |
| Unable to run GRASS plugin on MacOS | [#32511](https://github.com/qgis/QGIS/issues/32511) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| Processing: GRASS r.drain fails on macOS: \"No module named site\", \"Raster not found\" | [#36126](https://github.com/qgis/QGIS/issues/36126) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| The Grass7 processing toolbox option dialogue should include a way to specify a path to the GRASS binary, overriding Grass7Utils.command | [#29454](https://github.com/qgis/QGIS/issues/29454) | Kan niet worden gereproduceerd |  |
| Path error GRASS plugin QGIS 3.14 | [#38595](https://github.com/qgis/QGIS/issues/38595) | [PR #38840](https://github.com/qgis/QGIS/pull/38840) | different packaging system\... |
| No Print dialog or Page Setup dialog in macOS | [#30791](https://github.com/qgis/QGIS/issues/30791) | Kan niet worden gereproduceerd |  |
| Splash Screen Persists While \'Handle Bad Layers\' Dialog is Open | [#34784](https://github.com/qgis/QGIS/issues/34784) | [PR #38842](https://github.com/qgis/QGIS/pull/38842) | niet van toepassing |
| qgis terms of license pop up bug | [#38588](https://github.com/qgis/QGIS/issues/38588) | Kan niet worden gereproduceerd |  |
| Cannot load pictures anymore in custom forms | [#30833](https://github.com/qgis/QGIS/issues/30833) | already fixed by [Mac Packager Issue #3](https://github.com/qgis/QGIS-Mac-Packager/issues/3) | niet van toepassing |
|  | [Mac Packager Issue #83](https://github.com/qgis/QGIS-Mac-Packager/issues/83) | [Mac Packager Commit 36f86759649abc4cb8f6875f6ad934070c13d56e](https://github.com/qgis/QGIS-Mac-Packager/commit/36f86759649abc4cb8f6875f6ad934070c13d56e) | different packaging system\... |
| Projections not reading in MacOS Nightly Build | [#38919](https://github.com/qgis/QGIS/issues/38919) | [PR #38922](https://github.com/qgis/QGIS/pull/38922) | different packaging system\... |
| layers in .osm format are not loading | [Mac Packager Issue #84](https://github.com/qgis/QGIS-Mac-Packager/issues/84) | Kan niet worden gereproduceerd | werkt in 3.10 |
| missing metadata python package | [Mac Packager Issue #87](https://github.com/qgis/QGIS-Mac-Packager/issues/87) | [Mac Packager Commit 7c94749579acaf059e9b6c5094c7a2cb74d17f7a](https://github.com/qgis/QGIS-Mac-Packager/commit/7c94749579acaf059e9b6c5094c7a2cb74d17f7a) | different packaging system\... |
| GeoPDF Export fails | [Mac Packager Issue #75](https://github.com/qgis/QGIS-Mac-Packager/issues/75) | werkt nu met qgis-deps-0.5.5 | different packaging system\... |
| GRASS Console not work on Mac | [#38961](https://github.com/qgis/QGIS/issues/38961) | [Mac Packager Commit bfc4ca0717de0e496d98f91e7a28e85216763ab1](https://github.com/qgis/QGIS-Mac-Packager/commit/bfc4ca0717de0e496d98f91e7a28e85216763ab1) | different packaging system\... |
| Processing Plugin Crashes QGIS on MacOS Nightly Build | [#38960](https://github.com/qgis/QGIS/issues/38960) | [PR #38973](https://github.com/qgis/QGIS/pull/38973) | different packaging system\... |
| Program crash when pasting file name | [#38939](https://github.com/qgis/QGIS/issues/38939) | Kan niet worden gereproduceerd |  |
| Wrong Python default path in QGIS server on macOS | [#29843](https://github.com/qgis/QGIS/issues/29843) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| qgis_map.fcgi on macOS doesn\'t find libraries | [#29399](https://github.com/qgis/QGIS/issues/29399) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| GRASS provider cannot get projection | [#31397](https://github.com/qgis/QGIS/issues/31397) | [Mac Packager Commit bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95](https://github.com/qgis/QGIS-Mac-Packager/commit/bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95) | different packaging system\... |
| QGIS crashing on start on Mac | [#38858](https://github.com/qgis/QGIS/issues/38858) | gebruikersprofiel corrupt | N/B |
| Browser cannot open Volumes under macOS | [#29702](https://github.com/qgis/QGIS/issues/29702) | [PR #39096](https://github.com/qgis/QGIS/pull/39096) | nee, niet kritisch |
| MetaSearch unexpected keyword argument \'auth\' | [#38074](https://github.com/qgis/QGIS/issues/38074) | kan niet worden gereproduceerd op master | different packaging system\... |
| No QGIS plugins found in /Applications/QGIS3.10.app/Contents/MacOS/../PlugIns/qgis | [#39044](https://github.com/qgis/QGIS/issues/39044) | kan niet worden gereproduceerd op master | different packaging system\... |
| Browser Panel: unable to find all the connected drives | [#24641](https://github.com/qgis/QGIS/issues/24641) | duplicate of [#29702](https://github.com/qgis/QGIS/issues/29702) for MacOS |  |
| Provider Settings for GRASS avoid to active OTB | [#39112](https://github.com/qgis/QGIS/issues/39112) | kan niet worden gereproduceerd op master |  |
| Can\'t open GeoJSON vector via HTTP protocol on Windows and macOS | [#37107](https://github.com/qgis/QGIS/issues/37107) | \"[Mac Packager Commit d06bc3ac933c75071f36937aaf8189920dccc503](https://github.com/qgis/QGIS-Mac-Packager/commit/d06bc3ac933c75071f36937aaf8189920dccc503) | different packaging system\... |
| QGIS 3.0.1 Crash - Zooming in while moving node crashes QGIS | [#26509](https://github.com/qgis/QGIS/issues/26509) | Kan niet worden gereproduceerd |  |
| Crash when switching user profiles (too early?) | [#26993](https://github.com/qgis/QGIS/issues/26993) | Kan niet worden gereproduceerd |  |
| Aborted when debugging python plugin with pdb | [#27201](https://github.com/qgis/QGIS/issues/27201) | kan niet worden gereproduceerd/ongeldig |  |
| Customization: the widget catcher can\'t select icon from a toolbar when it\'s under a group of icons | [#22967](https://github.com/qgis/QGIS/issues/22967) | [PR #39209](https://github.com/qgis/QGIS/pull/39209) | niet kritisch |
| QGIS on macOS can save file in qgz-format, but won\'t open files in qgz format | [#39204](https://github.com/qgis/QGIS/issues/39204) | Kan niet worden gereproduceerd |  |
| Mouse pointer keeps switching type | [#32947](https://github.com/qgis/QGIS/issues/32947) | waarschijnlijk een gewenste mogelijkheid, geen probleem |  |
| Aggregate function bug on macOS version | \"[#32932](https://github.com/qgis/QGIS/issues/32932) | kan niet worden gereproduceerd op master | different packaging system\... |
| Clear filter in Snapping Toolbar \> Edit advanced configuration causes crash | [#29750](https://github.com/qgis/QGIS/issues/29750) | kan niet worden gereproduceerd op master |  |
| Snapping Settings window with Night Mapping, low readability | [#29751](https://github.com/qgis/QGIS/issues/29751) | al gerepareerd |  |
| Merge raster fails in macOS | [#39213](https://github.com/qgis/QGIS/issues/39213) | kan niet worden gereproduceerd op master | different packaging system\... |
| Can\'t get info on WFS feature in MacOS nightly build | [#39223](https://github.com/qgis/QGIS/issues/39223) | [Mac Packager Commit 54872e06a43ef61bf6dae8242e121bd5cec8be11](https://github.com/qgis/QGIS-Mac-Packager/commit/54872e06a43ef61bf6dae8242e121bd5cec8be11) | different packaging system\... |
| QGIS 3.4.10 crashes - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | al gerepareerd | al gerepareerd |
| Exporting GRASS vector (save as\...) crashes QGIS | [#37508](https://github.com/qgis/QGIS/issues/37508) | [PR #39284](https://github.com/qgis/QGIS/pull/39284) | NOG TE DOEN |
| Crash when loading 3D project with DEM terrain and symbols that uses height value over the terrain | [#35483](https://github.com/qgis/QGIS/issues/35483) | [PR #39287](https://github.com/qgis/QGIS/pull/39287) | NOG TE DOEN |
| Creating 3D View from raster | [#37163](https://github.com/qgis/QGIS/issues/37163) | duplicate of [#35483](https://github.com/qgis/QGIS/issues/35483) | N/B |
| Crash when moving camera in 3D | \"[#37881](https://github.com/qgis/QGIS/issues/37881) | kan niet worden gereproduceerd op master |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Linebreak issue with editing expression of \"Title Label Decoration\" | [#37803](https://github.com/qgis/QGIS/issues/37803) | [PR #38817](https://github.com/qgis/QGIS/pull/38817) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| QGIS Server GetPrint: EXTERNAL_WMS layer on top of QGIS layer | [#35873](https://github.com/qgis/QGIS/issues/35873) | [PR #38548](https://github.com/qgis/QGIS/pull/38548) | N/B |
| Fixes OGC API Features certification | niet gerapporteerd | [PR #37622](https://github.com/qgis/QGIS/pull/37622) | N/B |
| Outdated help for labels \"data-defined\" placement group options | [#36680](https://github.com/qgis/QGIS/issues/36680) | [PR #37344](https://github.com/qgis/QGIS/pull/37344) |  |
| Server GetFeatureInfo returns 0 where is should return NULL | [#37781](https://github.com/qgis/QGIS/issues/37781) | [PR #38807](https://github.com/qgis/QGIS/pull/38807) |  |
| z function returns Nan when used with a 2d point geometry | [#37772](https://github.com/qgis/QGIS/issues/37772) | [PR #38831](https://github.com/qgis/QGIS/pull/38831) |  |
| m function returns Nan when used with a 2d point geometry | niet gerapporteerd | [PR #38831](https://github.com/qgis/QGIS/pull/38831)/commits/829ee25d431b2b3d1ea08fa8a930bb519ab2dd2f |  |
| processing.algorithmHelp from terminal (outside QGIS desktop) | [#37524](https://github.com/qgis/QGIS/issues/37524) | Kan niet worden gereproduceerd |  |
| Cache join layer in memory\" not toggling when editing join properties | [#37326](https://github.com/qgis/QGIS/issues/37326) | [PR #38838](https://github.com/qgis/QGIS/pull/38838) |  |
| Map tips should not appear for invisible features | [#37066](https://github.com/qgis/QGIS/issues/37066) | [PR #38861](https://github.com/qgis/QGIS/pull/38861) |  |
| Merge features: manual value is not respected | [#37659](https://github.com/qgis/QGIS/issues/37659) | [PR #39083](https://github.com/qgis/QGIS/pull/39083) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere](https://hytech-imaging.fr/)
### Reparaties van problemen door Matthias Kuhn
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Legend nodes overlapping each other after inserting | [#38881](https://github.com/qgis/QGIS/issues/38881) | [PR #38882](https://github.com/qgis/QGIS/pull/38882) | niet kritisch |
| Poor legend performance with complex legends | [#38890](https://github.com/qgis/QGIS/issues/38890) | [PR #38891](https://github.com/qgis/QGIS/pull/38891) | niet kritisch |
| AMS layers cannot be added when no project CRS is set | [#38892](https://github.com/qgis/QGIS/issues/38892) | [PR #38893](https://github.com/qgis/QGIS/pull/38893) | niet de bedoeling |
| Legend performance problems | [#38978](https://github.com/qgis/QGIS/issues/38978) | [PR #39066](https://github.com/qgis/QGIS/pull/39066) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://opengis.ch/)
### Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingAlgRunnerTask started inside function crashes QGIS | [#38583](https://github.com/qgis/QGIS/issues/38583) | Zal niet gerepareerd worden |  |
| Geometry generator symbol not rendered if the feature itself is not on the map canvas | [#38579](https://github.com/qgis/QGIS/issues/38579) | Terugkoppeling |  |
| Relation widget in input form tabs - NULL value filled with data in form | [#38549](https://github.com/qgis/QGIS/issues/38549) | Geen backport (te riskant) | (Closed) [#38549](https://github.com/qgis/QGIS/issues/38549) |
| Warning message: Missing layer form dependency : layer \'layerX\' requires layer \'layerY\' to be loaded | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | N/B |
| When embedding a layer, the display expression of a relation reference is not taken over | [#38422](https://github.com/qgis/QGIS/issues/38422) | Gesloten (verzoek voor toevoeging) |  |
| the keybord shortcut CTRL+C copy only the first cell, not the whole line | [#37503](https://github.com/qgis/QGIS/issues/37503) | [PR #38810](https://github.com/qgis/QGIS/pull/38810) |  |
| if shortcut is set for copy features then Ctrl+C not working anymore | [#37401](https://github.com/qgis/QGIS/issues/37401) | Duplicaat van #37503 |  |
| Organize columns not working if the table is empty | [#38653](https://github.com/qgis/QGIS/issues/38653) | Bovenliggend probleem (Qt) |  |
| Copy and paste style for forms ignores edit widget type | [#37702](https://github.com/qgis/QGIS/issues/37702) | [PR #38836](https://github.com/qgis/QGIS/pull/38836) |  |
| Keep order when drag and drop multiple widget | [#37038](https://github.com/qgis/QGIS/issues/37038) | [PR #38844](https://github.com/qgis/QGIS/pull/38844) | [PR #39239](https://github.com/qgis/QGIS/pull/39239) |
| QGIS crash removing QgsAnnotation in python | [#36098](https://github.com/qgis/QGIS/issues/36098) | Terugkoppeling |  |
| Error in SQL statement for Virtual layers may lock layers in map canvas | [#34378](https://github.com/qgis/QGIS/issues/34378) | [PR #38949](https://github.com/qgis/QGIS/pull/38949) | [PR #39023](https://github.com/qgis/QGIS/pull/39023) |
| Virtual field in virtual layer not found | [#38523](https://github.com/qgis/QGIS/issues/38523) | Terugkoppeling |  |
| Closed ID column for temporary layer is not detected when creating virtual layers using data source manager | [#34830](https://github.com/qgis/QGIS/issues/34830) | Zal niet gerepareerd worden |  |
| Boolean virtual field unusable in virtual layers | [#31798](https://github.com/qgis/QGIS/issues/31798) | [PR #38957](https://github.com/qgis/QGIS/pull/38957) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| fails to generate virtual geometry layer based on virtual wkt field | [#28265](https://github.com/qgis/QGIS/issues/28265) | Terugkoppeling |  |
| Closed virtual fields can\'t be filtered | [#28072](https://github.com/qgis/QGIS/issues/28072) | Kan niet worden gereproduceerd |  |
| Qgis crached after calculated field removed | [#26486](https://github.com/qgis/QGIS/issues/26486) | Kan niet worden gereproduceerd |  |
| sql \"order by\" does not work with the \"Add/Edit Virtual Layer\" feature | [#29043](https://github.com/qgis/QGIS/issues/29043) | Zal niet gerepareerd worden |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #39041](https://github.com/qgis/QGIS/pull/39041) |  |
| Oracle - can\'t create or a modify a connection | [#38979](https://github.com/qgis/QGIS/issues/38979) | [PR #39131](https://github.com/qgis/QGIS/pull/39131) |  |
| Test connection Oracle DB ready - OK greyed out ! | [#39116](https://github.com/qgis/QGIS/issues/39116) | Duplicaat van #38979 |  |
| Scale dependent snapping does not activate as long as it displays the scale as \"1:xxxxxx\" | [#39031](https://github.com/qgis/QGIS/issues/39031) | [PR #39133](https://github.com/qgis/QGIS/pull/39133) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://www.oslandia.com/)
### Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| correctly determine if variables are static in aggregate expression and filter, give \@parent in generic aggregates | [#33382](https://github.com/qgis/QGIS/issues/33382) | [PR #39391](https://github.com/qgis/QGIS/pull/39391) | nee |
| Freeze when using aggregate in a virtual field | [#39366](https://github.com/qgis/QGIS/issues/39366) | Zal niet gerepareerd worden |  |
| Fix SVG marker anchor calculation and improve bounds | [PR #39336](https://github.com/qgis/QGIS/pull/39336) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39421](https://github.com/qgis/QGIS/pull/39421) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39519](https://github.com/qgis/QGIS/pull/39519) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39524](https://github.com/qgis/QGIS/pull/39524) |  |  |
| Fix duplicating features | [PR #39548](https://github.com/qgis/QGIS/pull/39548) |  |  |
| fix duplication of feature being stopped at 1 level deep | [PR #39550](https://github.com/qgis/QGIS/pull/39550) |  |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Reparaties van problemen door Olivier Dalang
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Core topology fixer issues | niet gerapporteerd | [PR #39392](https://github.com/qgis/QGIS/pull/39392) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Olivier Dalang](https://www.opengis.ch/)
### Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix crash in dbmanager | [#38393](https://github.com/qgis/QGIS/issues/38393) | [Commit 8c623b268ed94ef65aa19e2271be10b75e1ef36a](https://github.com/qgis/QGIS/commit/8c623b268ed94ef65aa19e2271be10b75e1ef36a) | N/B |
| Fix GeoPDF page size issues when opened in Acrobat reader | [#33465](https://github.com/qgis/QGIS/issues/33465) | [Commit 460bf8e534eb32ccba665918a615b55a8cbccadd](https://github.com/qgis/QGIS/commit/460bf8e534eb32ccba665918a615b55a8cbccadd) | Uitgesteld om meer door gebruikers te laten testen |
| Improve default lighting of 3d scenes | niet gerapporteerd | [Commit 350bc602e0ecd0f93dc2cc90ab34ce09993a687b](https://github.com/qgis/QGIS/commit/350bc602e0ecd0f93dc2cc90ab34ce09993a687b) | N/B |
| Allow conversion of QgsFeatureStoreList results to Python objects | [#39479](https://github.com/qgis/QGIS/issues/39479) | [Commit 49c508921d7ccb59b1f1abaff4f890456cca1455](https://github.com/qgis/QGIS/commit/49c508921d7ccb59b1f1abaff4f890456cca1455) | Te riskant |
| Fix preview symbol when offsetting point symbols isn\'t shown correctly | niet gerapporteerd | [Commit 62409b92ce20a84dd92188cf42a98d7cdc0b08c3](https://github.com/qgis/QGIS/commit/62409b92ce20a84dd92188cf42a98d7cdc0b08c3) | N/B |
| Use click-click behavior for rotate and offset marker tools | niet gerapporteerd | [Commit 00a3a6b8057f96dfa6c37943427a276cd3a5065d](https://github.com/qgis/QGIS/commit/00a3a6b8057f96dfa6c37943427a276cd3a5065d) | N/B |
| Avoid massive UI hangs when a layer has complicated actions defined | niet gerapporteerd | [Commit 9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668](https://github.com/qgis/QGIS/commit/9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668) | Te riskant |
| Ensure display expression is used for map action tool, not raw feature ids | niet gerapporteerd | [Commit e304d4d7e3eae0f48f336c7eb34542be6055df5d](https://github.com/qgis/QGIS/commit/e304d4d7e3eae0f48f336c7eb34542be6055df5d) | Lage prioriteit |
| Improve UX when configuring lights in a 3d scene, fixes confusing interface | niet gerapporteerd | [Commit 3019b82100d4fc405f64cebcddf9aaae253c4293](https://github.com/qgis/QGIS/commit/3019b82100d4fc405f64cebcddf9aaae253c4293) | N/B |
| Fix features with invalid geometries cannot be selected | [#38460](https://github.com/qgis/QGIS/issues/38460) | [Commit 22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d](https://github.com/qgis/QGIS/commit/22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d) | N/B |
| Expose metadata tab for mesh layers | niet gerapporteerd | [Commit 9482b1be70f36f778f6a409847244c5ff8a6a739](https://github.com/qgis/QGIS/commit/9482b1be70f36f778f6a409847244c5ff8a6a739) | N/B |
| Fix missing text codecs on Windows installs | [#36871](https://github.com/qgis/QGIS/issues/36871) | [Commit c3ca85e60bec73056bd87c426fd71c8f578363cb](https://github.com/qgis/QGIS/commit/c3ca85e60bec73056bd87c426fd71c8f578363cb) | Te riskant |
| Don\'t force a whole layout map to be rasterised just because one vector layer has non 100% opacity | niet gerapporteerd | [Commit 2d15a4cfad6c732cf640fbb0eabd625856b643ca](https://github.com/qgis/QGIS/commit/2d15a4cfad6c732cf640fbb0eabd625856b643ca) | Te riskant |
| Ensure mesh layer properties follows same appearance as other layer types | niet gerapporteerd | [Commit 3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac](https://github.com/qgis/QGIS/commit/3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac) | N/B |
| Speed up mesh triangulation algorithm by avoiding a bunch of unnecessary QVector detachments | niet gerapporteerd | [Commit 46ef391a7acf10515a11c19b69fafa4548046448](https://github.com/qgis/QGIS/commit/46ef391a7acf10515a11c19b69fafa4548046448) | N/B |
| Don\'t allow users to set 3d terrain to mesh or DEM without selecting an elevation layer, instead show friendly warning | niet gerapporteerd | [Commit 0d9f1da846c70764fa6840309b5460f713b30e1f](https://github.com/qgis/QGIS/commit/0d9f1da846c70764fa6840309b5460f713b30e1f) | N/B |
| Avoid 3d map config dialog opening with initially out-of-sync selected pane | niet gerapporteerd | [Commit 8b6477208f3c34e228734f7c04d32625965c48ed](https://github.com/qgis/QGIS/commit/8b6477208f3c34e228734f7c04d32625965c48ed) | N/B |
| Fix menu not shown when clicking \'add\' item in style manager dialog and color ramp tab is active | niet gerapporteerd | [Commit a085ce84b81a46896c9f00ee64eccaea63dad29a](https://github.com/qgis/QGIS/commit/a085ce84b81a46896c9f00ee64eccaea63dad29a) | N/B |
| Fix trying to create new color ramp from first page in style manager dialog does nothing | niet gerapporteerd | [Commit 34fb646f7ab69f20072b4d74ebec0595054089d7](https://github.com/qgis/QGIS/commit/34fb646f7ab69f20072b4d74ebec0595054089d7) | N/B |
| \[processing\] Fix generated layers stored in geopackage always report a feature count of 0 | niet gerapporteerd | [Commit 0675d99b34ee209a09857dfcba47cb5a92f55154](https://github.com/qgis/QGIS/commit/0675d99b34ee209a09857dfcba47cb5a92f55154) | Te riskant |
| Fix Import Geotagged photos algorithm incorrectly assigns form widgets when saving the results to GPKG | niet gerapporteerd | [Commit ff336ade18f4d6b307e4ed0e98fee77ee11a157c](https://github.com/qgis/QGIS/commit/ff336ade18f4d6b307e4ed0e98fee77ee11a157c) | [PR #39563](https://github.com/qgis/QGIS/pull/39563) |
| \[processing\] Ensure driverName is passed to QgsVectorLayerExporter so that GPKG specific optimisations can be applied when saving outputs to geopackage | niet gerapporteerd | [Commit 501c63feb3887e18da35188062546186d8a767ac](https://github.com/qgis/QGIS/commit/501c63feb3887e18da35188062546186d8a767ac) | Te riskant |
| Update strings and UI regarding layer CRS override setting | [#32101](https://github.com/qgis/QGIS/issues/32101) | [Commit 06cfdd9563b15d8fbb27aee94b83d1b15773df77](https://github.com/qgis/QGIS/commit/06cfdd9563b15d8fbb27aee94b83d1b15773df77) | N/B |
| Use proper SQL code editor in filter preview widget in vector layer properties, don\'t show filter as disabled | niet gerapporteerd | [Commit 0f4270cfe600e77f09db7727bd3ba965be7acb0e](https://github.com/qgis/QGIS/commit/0f4270cfe600e77f09db7727bd3ba965be7acb0e) | N/B |
| Fix boolean literal presentation in dox/PyQGIS docs | niet gerapporteerd | [Commit 746ee315bd0a4140f6e84617d547cc89103f79aa](https://github.com/qgis/QGIS/commit/746ee315bd0a4140f6e84617d547cc89103f79aa) | N/B |
| Speed up QGIS geometry validation | niet gerapporteerd | [Commit 2a15c3b0a4a631db1b55ac7e46256fdbd89949f9](https://github.com/qgis/QGIS/commit/2a15c3b0a4a631db1b55ac7e46256fdbd89949f9) | Te riskant |
| \[processing\] Correctly discard fid field values when running algorithms with the RegeneratePrimaryKey flag in in-place mode | [#37761](https://github.com/qgis/QGIS/issues/37761), [#33816](https://github.com/qgis/QGIS/issues/33816) | [Commit db7b97705967041d4eaca7e7f69cbf49f5692aef](https://github.com/qgis/QGIS/commit/db7b97705967041d4eaca7e7f69cbf49f5692aef) | Te riskant |
| \[processing\] When reporting that a feature is invalid, also mention the layer name | [#26664](https://github.com/qgis/QGIS/issues/26664) | [Commit a53bb3d49b59a3f814d862f30202ff156f74d6bc](https://github.com/qgis/QGIS/commit/a53bb3d49b59a3f814d862f30202ff156f74d6bc) | Te riskant |
| Allow expanding xls, ods, gpx, pdf files in browser so that layer sources can be repaired for these file types | niet gerapporteerd | [Commit 252976b739527e213f5d1c8c98a345911dfeab32](https://github.com/qgis/QGIS/commit/252976b739527e213f5d1c8c98a345911dfeab32) | N/B |
| \[processing\] Fix \"Split with lines\" algorithm can get stuck in an endless loop | niet gerapporteerd | [Commit 05645b320d8547f50a308843e961e343c383036d](https://github.com/qgis/QGIS/commit/05645b320d8547f50a308843e961e343c383036d) | Te riskant |
| Don\'t show cascaded feature deletion warnings and feedback if joined deleted features came from an auxilary layer | niet gerapporteerd | [Commit 8c79b94fcc14e41d4442a018554e889f81b8e080](https://github.com/qgis/QGIS/commit/8c79b94fcc14e41d4442a018554e889f81b8e080) | N/B |
| Fix crash in undo dock when clearing project/closing QGIS | [#38157](https://github.com/qgis/QGIS/issues/38157) | [Commit d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8](https://github.com/qgis/QGIS/commit/d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8) | [Commit 5c97ff66dd90d450a1ec60583da9626c14c9c08c](https://github.com/qgis/QGIS/commit/5c97ff66dd90d450a1ec60583da9626c14c9c08c) |
| Fix copy/paste/select all shortcuts don\'t work when layer tree is selected | [#38849](https://github.com/qgis/QGIS/issues/38849) | [Commit 02d7afae3f8699e83efacc781d3266700397d8b8](https://github.com/qgis/QGIS/commit/02d7afae3f8699e83efacc781d3266700397d8b8) | N/B |
| Fix edited and new features no longer correctly show their corresponding color shading in the feature list view | niet gerapporteerd | [Commit a195b056624c2fabe231be7c0e96c3d63e052e5b](https://github.com/qgis/QGIS/commit/a195b056624c2fabe231be7c0e96c3d63e052e5b) | Te riskant/lage prioriteit |
| ALWAYS load processing plugin in qgis_process tool | [#37989](https://github.com/qgis/QGIS/issues/37989) | [Commit bc0df6d25e929a575d0821208f7d187737d80709](https://github.com/qgis/QGIS/commit/bc0df6d25e929a575d0821208f7d187737d80709) | N/B |
| Add \--json option to qgis_process tool | <https://github.com/paleolimbot/qgisprocess/issues/21> | [Commit fc8d916b8dd444b3edaee3c18ec308e74a9bb91e](https://github.com/qgis/QGIS/commit/fc8d916b8dd444b3edaee3c18ec308e74a9bb91e) | N/B |
| Ensure all code editors in QGIS follow the same appearance and behavior | niet gerapporteerd | (veel) | N/B |
| When creating a CRS from WKT and the WKT has an embedded CRS name, correctly use this to set the QgsCoordinateReferenceSystem description | niet gerapporteerd | [Commit 9a35b27630982d63101c57c3e3440dcbf1a7786f](https://github.com/qgis/QGIS/commit/9a35b27630982d63101c57c3e3440dcbf1a7786f) | Mogelijk na verder testen door gebruikers |
| Big speed up for scripts which fire off many individual feature requests to a memory provider layer | niet gerapporteerd | [Commit 1d2bb41752c51e6c9b84124a1ce1599d3d42b41c](https://github.com/qgis/QGIS/commit/1d2bb41752c51e6c9b84124a1ce1599d3d42b41c) | Te riskant |
| \[console\] Fix exception when running scripts | niet gerapporteerd | [Commit 5c8013df6129a2bc06d25a98ff20dbf27621bff5](https://github.com/qgis/QGIS/commit/5c8013df6129a2bc06d25a98ff20dbf27621bff5) | N/B |
| \[layouts\] Fix resizing multiline label items to adjust to the size of their text | niet gerapporteerd | [Commit 6829e6351e1dab18f1fa0c0443107eb7617794c7](https://github.com/qgis/QGIS/commit/6829e6351e1dab18f1fa0c0443107eb7617794c7) | Te riskant |
| Improve appearance of PyQGIS documentation for functions which return multiple values | niet gerapporteerd | [Commit 0001ec27a43cbf4c99d1525c3c5f75183e96f5c3](https://github.com/qgis/QGIS/commit/0001ec27a43cbf4c99d1525c3c5f75183e96f5c3) | N/B |
| \[processing\] Don\'t raise a generic \"something went wrong\" exception when calling processing.run(), instead use proper descriptive exception | niet gerapporteerd | [Commit 2207c30a247e5907a12185165b4bd220e255bbdc](https://github.com/qgis/QGIS/commit/2207c30a247e5907a12185165b4bd220e255bbdc) | Te riskant |
| \[processing\] Fix execution of \"Eliminate selection\" through Python | [#38808](https://github.com/qgis/QGIS/issues/38808) | [Commit ee7bea2305253fd276a69c25bb5d308942dcb190](https://github.com/qgis/QGIS/commit/ee7bea2305253fd276a69c25bb5d308942dcb190) | Te riskant |
| \[3d\] Fix crash when line feature cannot be buffered | niet gerapporteerd | [Commit f6eed85729a8cbf913155ae16df7499f688ba0fa](https://github.com/qgis/QGIS/commit/f6eed85729a8cbf913155ae16df7499f688ba0fa) | [Commit d4c963e1c2fdc497dba038896caf2b3f975240ff](https://github.com/qgis/QGIS/commit/d4c963e1c2fdc497dba038896caf2b3f975240ff) |
| Fix custom stroke patterns incorrectly scale when data defined stroke width is set | [#39201](https://github.com/qgis/QGIS/issues/39201) | [Commit 03fdc0cd7992a7883183704cd68506f32afe9ca3](https://github.com/qgis/QGIS/commit/03fdc0cd7992a7883183704cd68506f32afe9ca3) | Te riskant |
| Allow columns to be resized in datum transformation table | [#39169](https://github.com/qgis/QGIS/issues/39169) | [Commit 1cd5a3358b235f67b6b4d95331ce561e9f8cb715](https://github.com/qgis/QGIS/commit/1cd5a3358b235f67b6b4d95331ce561e9f8cb715) | N/B |
| Fix settings incorrectly show for wrong layer types in labeling dialog | [#39168](https://github.com/qgis/QGIS/issues/39168) | [Commit 2e948884c029c9f79639201943ec4bc36dba3573](https://github.com/qgis/QGIS/commit/2e948884c029c9f79639201943ec4bc36dba3573) | N/B |
| \[processing\] Fix error reporting from batch dialog | [#39197](https://github.com/qgis/QGIS/issues/39197) | [Commit 5243a8594cc39540f2c01201415633801a22ff43](https://github.com/qgis/QGIS/commit/5243a8594cc39540f2c01201415633801a22ff43) | N/B |
| \[processing\] Fix crash when renaming conditional branch in modeler | [#39053](https://github.com/qgis/QGIS/issues/39053) | [Commit ddae53b7b789467bf17b21d6f4b884e827fbd3c5](https://github.com/qgis/QGIS/commit/ddae53b7b789467bf17b21d6f4b884e827fbd3c5) | N/B |
| \[processing\] Fix crash in model designer when a child algorithm contains hidden parameters | niet gerapporteerd | [Commit f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0](https://github.com/qgis/QGIS/commit/f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0) | N/B |
| Ensure True/False are treated as Python keywords in Python code editor | niet gerapporteerd | [Commit 5f661045c078b7938550c2c9d0798664c6f65f5a](https://github.com/qgis/QGIS/commit/5f661045c078b7938550c2c9d0798664c6f65f5a) | N/B |
| Don\'t silently close QGIS with unsaved changes in the console script editors | [#38529](https://github.com/qgis/QGIS/issues/38529) | [Commit 9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9](https://github.com/qgis/QGIS/commit/9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9) | Te riskant |
| Fix dropping processing script algorithm .py file on QGIS no longer triggers the algorithm to execute | niet gerapporteerd | [Commit 64bf347d7e1d664fc674c5ca602ce6c4bedecdf9](https://github.com/qgis/QGIS/commit/64bf347d7e1d664fc674c5ca602ce6c4bedecdf9) | N/B |
| Fix message log dock causes havoc with other docks placed in the same area | [#31955](https://github.com/qgis/QGIS/issues/31955) | [Commit 384f6a1d9257a05eaa58942921c94f1dd4941cd3](https://github.com/qgis/QGIS/commit/384f6a1d9257a05eaa58942921c94f1dd4941cd3) | Te riskant |
| When restoring a custom CRS from XML, if the CRS does NOT match any of the existing user defined CRS\'s on the QGIS profile then still restore the previously saved name of the custom CRS | niet gerapporteerd | [Commit e6d316ace7031821e04ca625e35f7c2c4d57f639](https://github.com/qgis/QGIS/commit/e6d316ace7031821e04ca625e35f7c2c4d57f639) | Mogelijk na verder testen door gebruikers |
| Don\'t refer to valid but custom CRSes as \"Unknown CRS\" and instead use \"Custom CRS\" phrasing | niet gerapporteerd | [Commit d3833fd8d6c4b4f0673c4c2337044c224675185f](https://github.com/qgis/QGIS/commit/d3833fd8d6c4b4f0673c4c2337044c224675185f) | Mogelijk na verder testen door gebruikers |
| Improve performance of processing batch process dialog with a large number of files | [#38987](https://github.com/qgis/QGIS/issues/38987) | [Commit 776768eb9f4ee2a8d13909b4ced5c175a0d05b3d](https://github.com/qgis/QGIS/commit/776768eb9f4ee2a8d13909b4ced5c175a0d05b3d) | Te riskant |
| Improve behavior of CRS selector and transformation widgets | niet gerapporteerd | veel | N/B |
| \[layouts\] Use standard CRS selector widget for map grid CRS choice | [#26548](https://github.com/qgis/QGIS/issues/26548) | [Commit 4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70](https://github.com/qgis/QGIS/commit/4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70) | Te riskant |
| \[layouts\] When selecting a CRS for a map item, don\'t show misleading no crs option at the top of the dialog | niet gerapporteerd | [Commit c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad](https://github.com/qgis/QGIS/commit/c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad) | Te riskant |
| Fix \"layer has no CRS\" message incorrectly show at the top of many projection selection dialog boxes | niet gerapporteerd | [Commit c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c](https://github.com/qgis/QGIS/commit/c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c) | Te riskant |
| Fix crash when editing style and opening a project | [#38920](https://github.com/qgis/QGIS/issues/38920) | [Commit 67ec244864ca6f9290e1f35a1a0c60b4888fe686](https://github.com/qgis/QGIS/commit/67ec244864ca6f9290e1f35a1a0c60b4888fe686) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/ecf96231aefa5628539f0b63ca313ea8b20c9548 |
| Avoid qt warning when dragging a non-color object over color buttons | niet gerapporteerd | [Commit fd771bba68da84b1ce8023898b9662b5dc619693](https://github.com/qgis/QGIS/commit/fd771bba68da84b1ce8023898b9662b5dc619693) | N/B |
| Fix shift in geopdf feature positions when using geographic CRS at large scales | [#37755](https://github.com/qgis/QGIS/issues/37755) | [Commit 0b77f187ec5a14651457fd07f306cba2511fb854](https://github.com/qgis/QGIS/commit/0b77f187ec5a14651457fd07f306cba2511fb854) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/b705d29c73e81fe87e2e301c7028e5e659d80364 |
| Fix constraint metadata is duplicated after opening layer properties | [#38916](https://github.com/qgis/QGIS/issues/38916) | [Commit 6a002573c00a8a8e11443eaca28b57a8ad6de4c0](https://github.com/qgis/QGIS/commit/6a002573c00a8a8e11443eaca28b57a8ad6de4c0) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/49260b8f1f4b1ddd9a25c7160f32570221f3989e |
| Fix PDF export includes vector information outside of the area of interest | [#38878](https://github.com/qgis/QGIS/issues/38878) | [Commit f3f226aa69a19b31dd8a1b83c82319528e061cfe](https://github.com/qgis/QGIS/commit/f3f226aa69a19b31dd8a1b83c82319528e061cfe) | Te riskant |
| \[layouts\] Fix legend symbol rendering doesn\'t respect linked map scale when symbol uses map unit based sizes | [#38326](https://github.com/qgis/QGIS/issues/38326) | [Commit 426ee2120b33a8613f3e476da3c2eba0a00f65d7](https://github.com/qgis/QGIS/commit/426ee2120b33a8613f3e476da3c2eba0a00f65d7) | N/B |
| Don\'t try to write empty rendered rings/geometries to GeoPDF outputs | niet gerapporteerd | [Commit 96753cfd1b9e986841158675bda365e585c48c27](https://github.com/qgis/QGIS/commit/96753cfd1b9e986841158675bda365e585c48c27) | Mogelijk na verder testen door gebruikers |
| Correctly apply capitalization setting whenever QgsTextRenderer is used, not just in labeling | [#38898](https://github.com/qgis/QGIS/issues/38898) | [Commit e1ca83b2c24c51e7ff67a53278ffd2601c0459be](https://github.com/qgis/QGIS/commit/e1ca83b2c24c51e7ff67a53278ffd2601c0459be) | Te riskant |
| Fix qgis_process list raises exception if processing algorithm provider is activated | [#38862](https://github.com/qgis/QGIS/issues/38862) | [Commit 772181bc16820d7dd5ee8d967355dbdfde5a8efe](https://github.com/qgis/QGIS/commit/772181bc16820d7dd5ee8d967355dbdfde5a8efe) | N/B |
| Dramatic speed up for calling some frequently used methods from PyQGIS | niet gerapporteerd | [Commit d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca](https://github.com/qgis/QGIS/commit/d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca) | Te riskant |
| \[processing\] Fix certain characters show as HTML escaped in processing log | [#37934](https://github.com/qgis/QGIS/issues/37934) | [Commit 965595d25bd0a69875ba8a405d3b365bedfe2a12](https://github.com/qgis/QGIS/commit/965595d25bd0a69875ba8a405d3b365bedfe2a12) | N/B |
| Fix incorrect capitalization in title of new layout name dialog | niet gerapporteerd | [Commit 92d0ec59a1c26c4ac33d35b9e6c93344845eddca](https://github.com/qgis/QGIS/commit/92d0ec59a1c26c4ac33d35b9e6c93344845eddca) | N/B |
| Add a new capitalization option for \"Title Case\", and rename the confusing \"Capitalize First Letter\" option to Force First Letter to Capital | [#16539](https://github.com/qgis/QGIS/issues/16539) | [Commit 484ba6f979cdcaabffe823c72b35b57d1b1c7aad](https://github.com/qgis/QGIS/commit/484ba6f979cdcaabffe823c72b35b57d1b1c7aad) | N/B |
| Add a Legend category to the style selection widgets and allow legend settings to be stored and restored in QML | [#37683](https://github.com/qgis/QGIS/issues/37683) | [Commit f018252023275f95c167d7f308d05c8819d6db0b](https://github.com/qgis/QGIS/commit/f018252023275f95c167d7f308d05c8819d6db0b) | Te riskant |
| Fix \[Style\] Export \--\> Save as QGIS Layer style File should allow to select style categories (and output format) | [#29145](https://github.com/qgis/QGIS/issues/29145) | [Commit 1ad2e78735e57cef218a7470d7eec645c2f45263](https://github.com/qgis/QGIS/commit/1ad2e78735e57cef218a7470d7eec645c2f45263) | Te riskant |
| \[browser\] Correctly save expanded node state when closing QGIS | niet gerapporteerd | [Commit 2eff061bf3cdcb3f36956e43098adfcb0359b5eb](https://github.com/qgis/QGIS/commit/2eff061bf3cdcb3f36956e43098adfcb0359b5eb) | Te riskant |
| \[browser\] Gpkg and other container types can be dragged to the map to allow layers to be added from them | niet gerapporteerd | [Commit 0234d4e9e10f3fbb5732f66e00eebd038f502ab0](https://github.com/qgis/QGIS/commit/0234d4e9e10f3fbb5732f66e00eebd038f502ab0) | Te riskant |
| Don\'t prompt for CRS for annotation layers | [#38739](https://github.com/qgis/QGIS/issues/38739) | [Commit 15975c1d5191933311d81a494d87806f4e73ce57](https://github.com/qgis/QGIS/commit/15975c1d5191933311d81a494d87806f4e73ce57) | N/B |
| Fix reading saved color map file when an item\'s label contains a comma character | [#24112](https://github.com/qgis/QGIS/issues/24112) | [Commit 252149375c750d6a8f1ee281c1cc9d03de272170](https://github.com/qgis/QGIS/commit/252149375c750d6a8f1ee281c1cc9d03de272170) | Te riskant |
| Fix diagram settings are not correctly restored when loading a QML file | [#35343](https://github.com/qgis/QGIS/issues/35343) | [Commit 4668927ce432b198b3c572535ff234343c5042f5](https://github.com/qgis/QGIS/commit/4668927ce432b198b3c572535ff234343c5042f5) | Te riskant |
| Fix can no longer paste colors from text strings | niet gerapporteerd | [PR #39561](https://github.com/qgis/QGIS/pull/39561) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
