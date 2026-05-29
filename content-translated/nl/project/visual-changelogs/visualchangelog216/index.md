---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.16
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.16{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Datum uitgave 08-07-2016

Dit is het log met wijzigingen voor de volgende uitgave van QGIS - versie 2.16.0 \'Nødebo\'. Het Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo was de gastheer voor de Eerste Internationale QGIS-conferentie en ontwikkelaarsbijeenkomst in mei 2015.

**Dit is geen Long Term Release (Lange Termijn Release)**

Deze uitgave is niet bestemd als een Long Term Release (LTR). gebruikers die een versie van QGIS willen die niet wijzigt en voor tenminste 1 jaar geen oplossingen voor problemen willen, worden geadviseerd de huidige LTR-uitgave 2.14 te gebruiken (die nu, bij de uitgave van QGIS 2.16, onze officiële LTR wordt).

**Nieuwe mogelijkheden in QGIS 2.16 \'Nødebo\'**

Als u upgradet vanaf QGIS 2.14 zult u vele nieuwe mogelijkheden aantreffen in deze uitgave. We bevelen u aan om de logs voor de wijzigingen van de [vorige uitgaven](https://www.qgis.org/en/site/forusers/visualchangelogs.html) te lezen omdat deze QGIS 2.16 ook alle mogelijkheden bevat die zijn gepubliceerd voor die uitgaven.

Wanneer aan software nieuwe mogelijkheden worden toegevoegd, introduceren die de mogelijkheid tot het ontstaan van nieuwe problemen - als u in deze uitgave nieuwe problemen tegenkomt, vul dan een ticket in [op de QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Uitspreken van Nødebo\...

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en sponsors. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors]. Als u een officiële sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het nemen van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid. Als u in staat bent QGIS te ondersteunen, kunt u [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 2.16.0
Elk jaar ontvangen wij ook ondersteuning van verschillende organisaties die het werk wat wij doen waarderen en die het mogelijk willen maken dat de ontwikkeling van het QGIS project vooral blijft doorgaan. Deze sponsoren, genoemd in onderstaande lijst, zijn wij zeer dankbaar! 

{{<fund type="changelog" >}}
## Algemeen
### Mogelijkheid: Objecten kopiëren in indeling GeoJSON
De eerdere instelling om WKT op te nemen bij het kopiëren van objecten is vervangen door een keuze voor het kopiëren van objecten als \"Platte tekst, alleen attributen\", \"Platte tekst, geometrie WKT\" en een nieuwe optie \"GeoJSON\". Indien ingesteld op "GeoJSON", zal het kopiëren van objecten in QGIS een GeoJSON-tekstweergave van de objecten op het klembord plaatsen om ze eenvoudig in andere toepassingen/JavaScript-code te kunnen plakken. Deze instellingen zijn te vinden onder `Extra -> Opties -> Databronnen -> Objecten kopiëren als`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Ruimtelijke bladwijzers in projectbestanden opslaan
Wanneer u een ruimtelijke bladwijzer maakt, kunt u er nu voor kiezen om de bladwijzer op te slaan in uw actieve projectbestand. Scroll door het paneel met bladwijzers om het keuzevak te zoeken om deze mogelijkheid in te schakelen.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Stéphane Brunner](http://www.camptocamp.com/)
### Mogelijkheid: Ondersteuning voor berichten van GNSS GNRMC
QGIS kan nu GLONASS satellietgegevens (\$GN\* regels) afhandelen om een meer precieze positie te verkrijgen uit externe GPS/GNSS-ontvangers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Ondřej Fibich
### Mogelijkheid: Objecten van GeoJSON direct in QGIS plakken
De afhandeling van het klembord van QGIS kan nu vele aanvullende tekstindelingen parsen, inclusief eigen ondersteuning voor collecties van objecten van GeoJSON. Dit stelt u in staat om direct teksttekenreeksen van GeoJSON in QGIS te plakken en ze automatisch te hebben geconverteerd naar objecten en geometriën voor QGIS.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeteringen voor kaarttips
- De zichtbaarheid voor kaarttips wordt nu bewaard tussen sessies
- Kaarttips kunnen nu HTML-inhoud weergeven, inclusief afbeeldingen, video's en URL-koppelingen

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [OPENGIS.ch GmbH](http://www.opengis.ch)

Deze mogelijkheid werd ontwikkeld door [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Mogelijkheid: Desktop MIME-pictogrammen voor bestandstypen van QGIS
Het is nu eenvoudiger om bestandstypen van QGIS te herkennen en er onderscheid tussen te maken in het bestandsbeheer van uw besturingssysteem. Er zijn nu desktop MIME-pictogrammen voor de volgende bestandstypen:
- \*.qgs - QGIS projectbestand
- \*.qml - Bestand met instellingen voor laag
- \*.qlr - Bestand met definities voor laag
- \*.qpt - Sjabloonbestand voor printvormgeving

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Alexandre Neto](https://gisunchained.wordpress.com/)
## Gebruikersinterface
### Mogelijkheid: Vergrootglas kaartvenster
Een gereedschap Vergrootglas is toegevoegd aan QGIS, wat het u mogelijk maakt de kaart weer te geven in ene bepaalde schaal. Dit stelt u in staat in te zoomen op ene kaart, zonder de schaal van de kaart te wijzigen, wat het eenvoudiger maakt om nauwkeuriger de posities van labels en symbolen aan te passen. Aanvullend kan in de instellingen ene standaard vergrotingsfactor worden gedefinieerd, wat erg nuttig is voor schermen met hoge resoluties!

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

Dit werd mogelijk gemaakt door  [het project QWAT](https://github.com/qwat)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Verbeteringen aan zoomen op de kaart
QGIS 2.16 brengt verbeteringen voor de manier waarop u in en uit kunt zoomen op het kaartvenster.
- Ingedrukt houden van de toets `Ctrl` bij het gebruiken van het muiswiel om in- of uit te zoomen resulteert in een fijnere zoom. Dit gedrag brengt het kaartvenster in lijn met de printvormgeving.
- Indrukken van `Ctrl++` of `Ctrl+-` voert onmiddellijk in-/uitzoomen uit op het kaartvenster
- Indien bepaalde kaartgereedschappen actief zijn, kunt u een webkaartachtige zoom uitvoeren door `Shift` ingedrukt te houden en een rechthoek te tekenen op de kaart om naar dat gebied te zoomen. Dit is ingeschakeld voor de kaartgereedschappen die geen gereedschappen voor selecteren zijn (omdat die Shift gebruiken voor het toevoegen aan de selectie), en gereedschappen voor bewerken.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Bewerker voor interactieve kleurverlopen opnieuw ontworpen
De bewerker voor kleurenbalken is opnieuw bewerkt met interactieve besturingselementen voor het eenvoudiger manipuleren van kleurverlopen. Het dialoogvenster heeft nu ook een interactieve plot voor het aanpassen van stops voor het kleurverloop via de waarden van de kleuren HSV of RGB. De nieuwe mogelijkheden van de bewerker:
- slepen om stops voor kleuren te verplaatsen
- dubbelklikken om een nieuwe stop toe te voegen
- drukken op Delete zal de geselecteerde stop wissen
- drukken op pijltjestoetsen zal de geselecteerde stop verplaatsen, en ingedrukt houden van Shift tijdens het drukken op een pijltjestoets resulteert in ene grotere verplaatsing
- slepen en neerzetten van een kleur op de widget om een nieuwe stop toe te voegen

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Keuze voor de standaardweergave voor het dialoogvenster Attributen
In eerdere versies van QGIS zou het dialoogvenster Attributen altijd worden geopend in de tabelweergave. Nu heeft u de keuze om standaard altijd het dialoogvenster te openen in ofwel de tabelweergave, de formulierweergave of om de laatst gebruikte weergave te onthouden.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeteringen aan pop-ups van de kalender
De datum van vandaag wordt nu geaccentueerd in pop-upwidgets van de kalender, wat het eenvoudiger maakt een datum te selecteren, relatief aan de huidige dag.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterde kleurenkiezers
De keuzemenu's voor knoppen van kleuren geven nu een kleurenwiel weer, wat het mogelijk maakt snelle aanpassingen te maken aan kleuren.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

Deze mogelijkheid werd ontwikkeld door [Nathan Woodrow](http://nathanw.net/)
### Mogelijkheid: Celinhoud uit attributentabel kopiëren
Een nieuw item voor het contextmenu, genaamd `Celinhoud kopiëren` is nu beschikbaar in het menu dat wordt geopend met een klik met rechts in een cel in de attributentabel. De inhoud van de cel wordt gekopieerd naar het klembord als op deze knop wordt geklikt, ongeacht het soort widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Verbeterde ondersteuning voor HiDPI
Gebruikers van HiDPI-schermen zullen merken dat er een verbeterde gebruikersinterface is omdat er werk is gemaakt van het opwaarderen van pictogrammen om te kunnen vertrouwen op afbeeldingen van SVG. Vanaf QGIS 2.16 zijn alle werkbalken nu compatibel met HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Verbeterd gedrag van het gereedschap Selecteren op de kaart
Het gedrag van op de kaart gebaseerde gereedschappen om te selecteren is verfijnd, met de volgende wijzigingen:

Voor selecties van klikken-en-slepen:
- `Shift` ingedrukt houden = aan selectie toevoegen
- `Ctrl` ingedrukt houden = uit selectie verwijderen
- `Ctrl+Shift` ingedrukt houden = met huidige selectie kruisen
- `Alt` ingedrukt houden (kan ook worden gebruikt met `Shift`/`Ctrl`) = wijzigt de modus van selectie van \"kruist met\" tot \"bevat volledig\"

Voor selecties met één enkele klik:
- `Shift` of `Ctrl` ingedrukt houden = schakelen of het object is geselecteerd (d.i. ofwel aan de huidige selectie toevoegen of uit de huidige selectie verwijderen)

Deze wijziging brengt het gedrag van het kaartvenster in lijn met andere toepassingen voor ontwerpen en ook met het gedrag van printvormgeving.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Bijwerkingen van documentatie
### Mogelijkheid: Documentatie voor QGIS 2.14
Er is nu een automatische manier om een ticket te maken in de opslagplaats voor de documentatie voor elke nieuwe mogelijkheid in QGIS. We zijn er zeker van dat alle nieuwe mogelijkheden nu zijn opgenomen in de documentatie.

Het team voor de documentatie heeft hard gewerkt aan drie uitgaven van QGIS: 2.10, 2.12 en 2.14, dus nu is de documentatie up to date voor de huidige Long Term Release van QGIS. Dat zijn ongeveer 180 nieuwe mogelijkheden die zijn beschreven in de 4 maanden.

Als u denkt dat er nog enkele mogelijkheden ontbreken in de documentatie, mak dan een nieuw ticket aan, schrijf een korte tekst om het t ebeschrijven of, beter nog, dien een bijdrage in.

Het team voor de documentatie heeft ook gewerkt aan het verbeteren van de richtlijnen voor de documentatie om het proces van bijdragen voor nieuwe schrijvers van documentatie en vertalers voor de help eenvoudiger te maken.

Het team voor de documentatie zal de volgende maanden hard ana het werk gaan om de huidige stabiele uitgave (2.16) van QGIS te documenteren.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Bekijk de milestones 2.10, 2.12 en 2.14 om al het uitgevoerde werk voor de documentatie te bekijken:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Mogelijkheid: Documentatie voor het authenticatiesysteem in de gebruikershandleiding
De mogelijkheden voor het authenticatiesysteem, dat werd geïntroduceerd in eerdere versies van QGIS (2.12 en 2.14) zijn nu volledig beschreven in de gebruikershandleiding, en zullen een grote bijdrage leveren in het begrijpen van het systeem en het gebruiken ervan.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Boundless](http://boundlessgeo.com/)

Deze mogelijkheid werd ontwikkeld door Larry Shaffer
## Symbologie
### Mogelijkheid: Symboollaag Pijlen
De symboollaag \"pijl\"  is een symboollaag die het mogelijk maakt rechte of gebogen pijlen te tekenen uit een lijnlaag.

In de modus Gebogen worden knopen, van de lijnlaag waarop deze symbollaag is gebaseerd, gebruikt als controlepunten voor cirkelbogen. Pijlen kunnen worden gevuld met elke bestaande vulstijl die wordt ondersteund door QGIS. Opties maken het ook mogelijk het type van de pijl te selecteren (met één of twee pijluitienden, gewoon of gehalveer), de breedte ervan (die variabel kan zijn) en de grootte van de pijluiteinden.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [MEEM (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr/) en Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Hugo Mercier](http://oslandia.com/)
### Mogelijkheid: Nieuw type symboollaag \"Gevulde markering\"
Een \"gevulde markering\" is soortgelijk aan de eenvoudige markeringssymboollaag, met het verschil dat het een subsymbool voor vullen gebruikt om de markering te renderen. Dit maakt het mogelijk alle bestaande QGIS-stijlen voor vullen (en omtrek) voor het renderen van markeringen te gebruiken, bijv, vullingen kleurverloop of shapeburst.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuwe toegankelijkheid en symbolen voor verminderd zicht
Aanvullende symbolen voor verminderd zicht en toegankelijkheid zijn nu beschikbaar in de collectie van SVG-symbolen van QGIS.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Nieuwe symbolen voor eenvoudige markering
- halve cirkel, een derde, kwartcirkels
- markeringen halve driehoek
- gevulde kruis en achthoekige markeringen
- markering diamant ellips

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Renderer \"Geen symbool\" 
Bij het gebruiken van de nieuwe renderer \"Geen symbool\" in QGIS 2.16 zal geen symbool worden getekend voor objecten, maar labels, diagrammen en andere delen die geen symbool zijn, worden wel weergegeven.

Selecties kunnen nog steeds worden gemaakt in de laag in het kaartvenster en geselecteerde objecten zullen worden gerenderd met een standaard symbool. Objecten die worden bewerkt zullen ook worden weergegeven.

Dit is bedoeld als een handige sneltoets voor lagen waarin u alleen de labels of diagrammen weer wilt geven, en voorkomt dat symbolen moeten worden gerenderd met volledig transparante vulling/rand om dit te bereiken. Het zou, gelet op de titel, niet erg nuttig kunnen lijken - maar in feite is het een zeer handige sneltoets!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Meer controle over het renderen van vullingen van zwaartepunten
Een optie is toegevoegd om te beheren of de markering moet worden getekend op alle delen of slechts één enkel deel van meerdelige objecten.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Instelling voor symbool van omtrek van markeringen van lettertype
Het symbool van markeringen van lettertypen mag nu een omtrek hebben, die de zichtbaarheid van dergelijke symbolen kan verbeteren door een bufferkleur voor de omtrek toe te voegen. Ingeschakelde tekens van Emoji-lettertypen kunnen dienen als leuke markeringen, indien gebruikt met een dikke omtrek.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Stijl voor join van omtrek beheren voor eenvoudige, ellips en lettertypemarkeringen
Gebruikers kunnen nu de stijl voor join van omtrek wijzigen voor eenvoudige, ellips en lettertypemarkeringen om hun symbologie fijner af te stemmen.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Nieuw kaartgereedschap voor interactief instellen van verschuiving voor puntsymbool
Maakt het mogelijk de verschuiving voor een punt in te stellen als het is gebonden aan een veld dat wordt overschreven door middel van gegevens gedefinieerde instellingen. Het veld voor de verschuiving moet een tekstveld zijn. Het kaartgereedschap om interactief de verschuiving in te stellen staat in de werkbalk `Geavanceerd digitaliseren` in de groep met pictogrammen met het gereedschap `Puntsymbolen roteren`. Bekijk de bijgevoegde animatie voor een voorbeeld. Onthoud dat bij het maken van opeenvolgende aanpassingen aan de verschuiving, u zou moeten slepen vanaf de originele puntmarkering, niet de huidige positie van het symbool zoals dat is gerenderd op de kaart.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Dock voor stijlen
Het dock voor stijlen is een nieuwe, veel efficiëntere manier om laagstijlen in QGIS te beheren. Het ondersteunt een live-voorbeeld van de stijlwijzigingen als zij worden gemaakt, volledige ondersteuning voor ongedaan maken / opnieuw en een minder afleidende werkstroom als u de cartografie voor uw kaart voorbereidt. Bekijk voor een uitgebreid overzicht van de mogelijkheden van het dock voor stijlen, [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) en [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

Deze mogelijkheid werd ontwikkeld door [Nathan Woodrow](https://nathanw.net/)
## Labelen
### Mogelijkheid: Kaartgereedschappen voor labels werken nu met op regels gebaseerd labelen
In eerdere versies van QGIS waar op regels gebaseerd labelen werd gebruikt, kon u de kaartgereedschappen voor labels niet gebruiken om posities van labels interactief te plaatsen en te roteren. Dit wortd nu ondersteund.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
## Diagrammen
### Mogelijkheid: Legenda-items voor grootte van diagram
Een nieuwe tab \"Legenda\" is toegevoegd aan de eigenschappen voor diagrammen, wat het mogelijk maakt zowel de bestaande legenda voor attributen als de nieuwe legenda voor grootte in-/uit te schakelen. De legenda voor de grootte heeft een te configureren markeringssymbool.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [ADUGA](http://www.aduga.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Selecteren van eenheid voor breedte van omtrek
Selecteren van de eenheid voor de breedte van de omtrek is nu beschikbaar. Dit maakt het mogelijk, voor een diagram met de grootte van kaarteenheden, dat het zal vergroten en verkleinen gebaseerd op de schaal van de kaart waarbij een vaste breedte van de omtrek in millimeters wordt behouden

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Diagrammen gedragen zich zoals labels en kunnen vanaf de werkbalk worden beheerd
Origineel was er een werkbalk voor labels die het mogelijk maakte om:
- opties voor labels van de huidige laag in te stellen
- de vastgezette labels te accentueren. Accentueren is groen op een bewerkbare laag, anders blauw.
- labels vast te zetten of los te maken
- labels te verplaatsen, weer te geven en te verbergen 

Met deze nieuwe mogelijkheid is een nieuw gereedschap beschikbaar in de werkbalk voor labels dat het mogelijk maakt eigenschappen in te stellen voor diagrammen van de huidige laag. Meer nog, elk hierboven genoemd gereedschap is nu ook volledig te gebruiken voor diagrammen.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Renderen
### Mogelijkheid: Nieuwe opties voor direct vereenvoudigen
De gebruiker kan het algoritme selecteren dat moet worden gebruikt, als de vereenvoudiging aan de lokale zijde wordt uitgevoerd, om sneller geometrieën te tekenen. QGIS verschaft nu drie algoritmen:
- Distance (standaard algoritme, en de enige beschikbare optie in eerdere versies van QGIS)
- Snappen aan raster
- Visvalingam

Deze wijziging verplaatst ook de lokale \"directe\" vereenvoudiging van de provider en klassen voor iteratie naar de code voor renderen. Dit vermijdt gevallen waarin de vereenvoudiging de opgehaalde geometrie, verkregen van vectorgegevensproviders, wijzigt, wat mogelijk op regel gebaseerde en op andere expressies gebaseerde symbologie beïnvloedt. Dit is belangrijk als u expressies heeft die de geometrie van een object gebruiken (bijv. bij berekening van een gebied) - we willen er zeker van zijn dat de berekeningen worden uitgevoerd op de originele geometrie, niet op de vereenvoudigde.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Mogelijkheid: Op kwantielen gebaseerde classificatie voor rasterlagen
Deze optie is te vinden in het dialoogvenster voor classificatie `modus` voor enkelbandpseudokleur-rasters.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Piers Titus van der Torren
### Mogelijkheid: Live renderer schaduw voor heuvels
QGIS 2.16 heeft een nieuwe renderer voor  rasters die dynamisch een model voor schaduw voor heuvels zal maken uit een Digital Elevation Model.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Deze mogelijkheid werd ontwikkeld door Asger Skovbo Petersen en Nathan Woodrow
## Digitaliseren
### Mogelijkheid: \"Herhalende\" modus Vastzetten voor beperkingen
Indien ingeschakeld, worden herhaald vastgezette niet automatisch geschoond als een nieuw punt wordt toegevoegd. Ze zijn handig wanneer dezelfde beperking herhaald moet worden voor meerdere punten (bijv. toevoegen van punten die altijd 50 meter van elkaar af liggen). Deze functionaliteit is beschikbaar in het `paneel Geavanceerd digitaliseren`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Geometrieën Lijnen uitbreiden met gereedschap Objecten vervormen
Het gereedschap Objecten vervormen stelt u nu in staat om lijnen uit te breiden, door het vervormen te beginnen bij het start- of eindpunt van een lijn.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
### Mogelijkheid: Tolerantie voor segmentatie
Ondersteuning werd toegevoegd om de tolerantie voor segmentatie in te stellen (maximale hoek of maximaal verschil). Deze instelling beheert de manier waarop cirkelbogen worden gerenderd. Hoe kleiner de maximale hoek (in graden) of het maximale verschil (in kaarteenheden), des te meer de rechte lijnsegmenten zullen worden gebruikt bij het renderen. U vindt deze optie in `Extra -> Opties -> Rendering -> Segmentatie van boog`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Marco Hugentobler
## Gegevensbeheer
### Mogelijkheid: Nieuwe opties voor configureren van de attributentabel
- Maakt het mogelijk de kolommen van de attributentabel opnieuw te ordenen (via klik met rechts op de kop van de veldnaam \--\> dialoogvenster \"Kolommen beheren\"; slepen en neerzetten om opnieuw te ordenen)
- Maakt het mogelijk een nieuwe kolom toe te voegen aan de attributentabel om knoppen te bevatten voor het activeren van een actie, gebaseerd op het gekozen object
- Kolommen kunnen in de attributentabel worden verborgen (via klik met rechts op de kop van de veldnaam)
- QGIS onthoudt nu de breedte van elke kolom waarvan de grootte is gewijzigd

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/) en [MEEM (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr/)

Deze mogelijkheid werd ontwikkeld door [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) en [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid: Meerdere kolommen in formulieren voor attributen
Bij het gebruiken van de ontwerper Slepen en neerzetten kan een gebruiker specificeren over hoeveel velden de kolommen moeten worden verdeeld.

Inschakelen van meerdere kolommen op de tab \"Velden\" van de laageigenschappen:
- Zorg er voor dat u de modus voor ontwerpen van formulieren Slepen en neerzetten gebruikt
- Dubbelklik op een groep containers, zoals tabs of groepen
- een klein dialoogvenster zal verschijnen waar u het aantal kolommen kunt selecteren

De volgorde zal zijn eerste kolom, tweede kolom, n-de kolom, volgende rij, etc.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://opengis.ch/)
### Mogelijkheid: Beheren van te exporteren attributen bij het opslaan van een vectorlaag
Keuzevakken zijn toegevoegd, zodat u kunt selecteren welke attributen u wilt opnemen bij het exporteren, en ook heeft u nu de optie om \"weergegeven\" waarden weg te schrijven in plaats van ruwe waarden. Deze optie is nuttig voor lagen met relaties, waar u liever een letterlijke waarde zou zien opgenomen dan een numerieke identificatie.

Afhankelijk van de indeling wordt de \"weergegeven waarde\" standaard ingeschakeld, bijv. bij exporteren naar de indelingen voor werkbladen (ODF, XLSX, CSV/Tekst).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

Dit werd gedeeltelijk mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer, Even Rouault
### Mogelijkheid: Weergave formulieren: zijkolom nu te sorteren
In de modus Formulieren van de attributentabel van QGIS staat een zijkolom die men kan gebruiken om direct naar een specifiek object te springen. Tot aan deze uitgave was deze zijweergave niet te sorteren. Voor het sorteren moest men naar de modus tabel springen en dan weer terug naar de modus Formulieren. Nu kan men het object direct sorteren met het voorbeeld van de attributen van het object in het zijpaneel, door de sorteerfunctie te kiezen in de keuzeknop voor expressies boven de zijkolom.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Mogelijkheid: Widget voor verwijzing naar relatie: sneltoets voor toevoegen van nieuwe waarden
De widget voor verwijzingen naar relaties werd uitgebreid om de gerelateerde lijsten met waarden sneller te kunnen uitbreiden. Als het keuzevak \"Toevoegen van nieuwe objecten toestaan\" is ingeschakeld in de eigenschappen voor de widget (toegankelijk via de tab \"Velden\" in de laageigenschappen), zal rechts naast de widget een groene knop verschijnen. Na het drukken op de knop \"Plus\", zal het dialoogvenster van de gerelateerde tabel worden geopend in de modus \"nieuw record\" waar men een aanvullend item kan toevoegen.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Mogelijkheid: Verbeteringen voor DXF exporteren
Ondersteuning is toegevoegd voor op regels gebaseerde labels en geroteerde symbolen, en voor het uitvoeren van 3D-geometrieën.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Widgets op bovenste niveau in ontwerper Slepen en neerzetten
Het is nu mogelijk om widgets direct in het formulier te plaatsen met de ontwerper Slepen en neerzetten. Een formulier voor de ontwerper Slepen en neerzetten kan daarom bestaan zonder enige tabs erop.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Op formulier gebaseerd selecteren en filteren
In QGIS 2.16 werd een nieuwe modus toegevoegd aan de mogelijkheden voor het zoeken en filteren van objecten in het dialoogvenster van de attributentabel. Indien geactiveerd (met behulp van een knop op de werkbalk of door `CTRL+F` in te drukken), zal het dialoogvenster schakelen naar de formulierweergave en zullen alle widgets worden vervangen door hun variant voor de wrapper van het zoekwidget.

Naast elke widget staat een gereedschapsknop met opties voor het beheren van het gedrag voor zoeken/filteren voor dat veld, bijv. \"is gelijk aan\", \"is niet gelijk aan\", \"is null\", \"groter dan\", etc., met de weergegeven opties die overeenkomen voor het overeenkomstige veld en type widget.

Nieuwe knoppen verschijnen aan de onderzijde van het formulier om ofwel overeenkomende objecten te selecteren (met opties voor het toevoegen aan selectie/verwijderen uit selectie/selecteren binnen huidige selectie) of objecten in de tabel te filteren (met opties voor toevoegen van objecten aan huidige filter of het verder beperken van het huidige filter).

U krijgt ook toegang tot deze modus met de nieuwe optie \"Op waarde selecteren\", of door te drukken op F3 met een laag geselecteerd.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Deze mogelijkheid werd mogelijk gemaakt door SIGE, Stad Uster, Morges

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Lagen voor GeoPackage maken
De indeling [GeoPackage](http://www.geopackage.org) is een open standaard voor georuimtelijke gegevens die op uw radar zou moeten zijn als vervanging voor de indeling ESRI Shapefile. Het verbetert vele tekortkomingen van de indeling Shapefile, inclusief beperkingen in het aantal en de breedte van velden. In QGIS 2.16 is het nu eenvoudig om een nieuwe GeoPackage te maken, omdat het is geïntegreerd in de werkbalk `Laag` en het menu `Kaartlagen -> Laag maken`.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mogelijkheid: Beperkingen in widgets
In eerdere versies van QGIS was er geen manier om de geldigheid van waarden te controleren die werden ingevoerd door een gebruiker voor attributen van een object. Nu kan een gebruiker een beperking voor elke widget instellen in het formulier van de attributen voor een laag. Beperkingen worden gemaakt met behulp van expressies voor QGIS, bijv. `"min_population" > 50000`. Een keuzevak \"Niet Null\" is ook beschikbaar om aan te geven dat voor dat veld een waarde moet worden ingevuld. Aanvullend kan een beschrijvende tekst worden toegevoegd om de gebruiker nuttige terugkoppeling te geven als een beperking mislukt.

Beperkingen worden direct geëvalueerd terwijl een gebruiker het object aanpast. Een helptip is beschikbaar voor elk veld dat een beperking heeft, die de expressie van de beperking weergeeft, het resultaat van de evaluatie en een beschrijving van de beperking. Een berichtenbalk zal ook aan de bovenzijde van het formulier worden weergegeven en velden vermelden die niet voldoen aan de criteria van de beperking.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [het project QWAT](https://github.com/qwat) en het [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) en [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Attributen van meerdere objecten tegelijkertijd bewerken
Deze wijziging maakt het mogelijk attributen van meerdere objecten tegelijkertijd te bewerken. Het wordt ingeschakeld als het dialoogvenster van de attributentabel in de \"modus Formulier\" staat, via een nieuwe knop \"Meervoudige bewerkingen\" op de werkbalk. Er is ook een sneltoets om meerdere objecten tegelijkertijd te bewerken door middel van `Bewerken -> Attributen van geselecteerde objecten aanpassen`.

In deze modus zullen wijzigingen aan de waarden van attributen van toepassing zijn op alle geselecteerde objecten. Nieuwe widgets verschijnen naast elk widget voor bewerking wat het mogelijk maakte de huiidge status voor meervoudig bewerken weer te geven en voor het terugdraaien van wijzigingen op een basis van veld-naar-veld.

Wijzigingen worden gemaakt als één enkele opdracht voor bewerken, dus zal het drukken op Ongedaan maken alle wijzigingen voor alle objecten in één keer terugdraaien.

Modus Meervoudig bewerken is alleen beschikbaar voor automatisch gegenereerde en formulier van Slepen en neerzetten - het wordt niet ondersteund in aangepaste formulieren voor de UI.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

Dit werd mogelijk gemaakt door [Kanton Basel Stadt](http://www.geo.bs.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Legenda van laag
### Mogelijkheid: Nieuwe optie om te zoomen naar het zichtbare schaalbereik van een laag
Voor lagen met een ingesteld zichtbaar schaalbereik, zal het selecteren van deze optie automatisch de schaal instellen op de dichtstbijzijnde schaal waarmee de laag zichtbaar is. Aanvullend is de interface zodanig aangepast dat lagen die buiten hun schaalbereik liggen en zijn verborgen uitgegrijsd worden weergegeven in de lagenboom.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Printvormgeving
### Mogelijkheid: Nieuwe gereedschappen voor het tekenen van polygonen en polylijnen
Twee nieuwe types van vormitems voor printvormgeving, gebaseerd op knopen, zijn nu beschikbaar in de printvormgeving. Door deze te gebruiken kunt u met een paar klikken polygonen of polylijnen in uw lay-out tekenen.

Nieuwe gereedschappen zijn ook toegevoegd aan om het mogelijk te maken knopen te bewerken (d.i. knopen verplaatsen of verwijderen) en ook om nieuwe knopen aan een bestaande vorm toe te voegen. items polygoon en polylijn in Printvormgeving kunnen ook worden opgemaakt met behulp van alle beschikbare symboolstijlen voor lijn- en polygoonlagen!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Relatieve links in labels van Printvormgeving
Nu mogen labels en HTML-vakken relatieve URL\'s bevatten. Als er geen basis-URL is, zal het projectbestand worden gebruikt als basis-URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Ingebedde objecten voor atlas in HTML-bron in Printvormgeving als GeoJSON
Deze wijziging maakt het huidige object Atlas (en aanvullend alle attributen van gerelateerde kindobjecten) beschikbaar voor de bron van een HTML-item in Printvormgeving, wat het voor het item mogelijk maakt om dynamisch zijn gerenderde HTML aan te passen als antwoord op de eigenschappen van het object. Een voorbeeld van het gebruik is het dynamisch vullen van een HTML-tabel met alle attributen van gerelateerde kindobjecten voor het object Atlas.

De HTML-bron moet een JavaScript functie \"setFeature(feature)\" implementeren om dit te kunnen gebruiken. Deze functie wordt aangeroepen als het object Atlas wijzigt, en het object Atlas (en alle gerelateerde attributen) wordt doorgegeven als een object GeoJSON.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com/)
### Mogelijkheid: Ondersteuning van SVG met parameters voor SVG-afbeeldingen in Printvormgeving
Deze wijziging maakt het mogelijk om kleuren van vulling en omtrek van SVG-bestanden te wijzigen, en de breedte van de omtrek door middel van het gebruiken van SVG-bestanden met parameters zoals die welke zijn opgenomen in QGIS. Voor meer details over SVG-bestanden met parameters, bekijk [dit artikel](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Eenvoudiger gebruik van HTML in labels
In QGIS 2.16, zal het basisstijlblad van labels van Printvormgeving automatisch het lettertype voor het label en de marges instellen om overeen te komen met de instellingen van het label. Dit maakt interactief kiezen van lettertype, marges en kleuren mogelijk en vermijdt de noodzaak om deze handmatig in te moeten stellen met CSS in de HTML-code van het label.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Uitvoer van geoverwijzingen (bijv PDF) vanuit Printvormgeving
In QGIS 2.16 zal de Printvormgeving automatisch geoverwijzingen uitvoeren (als de indeling van de uitvoer dat mogelijk maakt, bijv TIF en PDF).

De bestaande optie om een world file te maken is afgescheiden van de kaartselectie voor geoverwijzingen. Het nieuwe gedrag is om altijd geoverwijzingen uit te voeren, en alleen het afzonderlijke world file te maken als die optie is geselecteerd.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: kaarten van Printvormgeving worden nu automatisch bijgewerkt met voorkeuzen
Als een kaart van Printvormgeving is ingesteld om een voorkeuze-stijl te volgen, zal die automatisch, elke keer als de stijl wordt gewijzigd, worden bijgewerkt.

Een nieuwe optie is toegevoegd in de eigenschappen van Printvormgeving: \"Zichtbaarheid voorkeuze volgen\" met een combinatievak om de actieve voorkeuze te kiezen. Dit is een alternatief voor de functionaliteit \"lagen vastzetten\" (en \"laagstijlen vastzetten\") die slechts een kopie maakt van de configuratie van de voorkeuze, waar deze nieuwe optie en koppeling maakt naar de voorkeuze.

Het verschil is dat wanneer een voorkeuze wordt bijgewerkt, de kaart van printvormgeving automatisch de nieuwe configuratie zal kiezen bij het volgen van de voorkeuze, terwijl er niet wordt bijgewerkt indien de optie \"lagen vastzetten\" (en \"laagstijlen vastzetten\") wordt gebruikt.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
## Analyse-gereedschappen
### Mogelijkheid: Benoemde parameters in expressies
In QGIS 2.16 ondersteunt het programma voor expressies nu het gebruiken van benoemde parameters. Dit betekent dat u in plaats van de cryptische expressie: `clamp(1,2,3)` te schrijven, u: `clamp( min:=1, value:=2, max:=3)` kunt gebruiken. Deze wijziging maakt het ook mogelijk argumenten te wisselen, bijv: `clamp( value:=2, max:=3, min:=1)`.

Gebruiken van benoemde parameters helpt verduidelijken waar de argumenten voor een functie voor een expressie naar verwijzen, wat nuttig is als u probeert een expressie te interpreteren op een latere datum!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Meer eenheden voor afstanden
De keuze van eenheden van afstanden is uitgebreid, met nieuwe opties inclusief kilometers, yards en miles. gebruiken van deze eenheden voorkomt de noodzaak tot het handmatig converteren van afstanden (bijv. van voet naar mijlen).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Wijzigingen aan expressies
- Ondersteuning voor `date + time` = datetime-berekeningen
- Ondersteuning voor `date - date`, `time - time` en `datetime - datetime` type berekeningen die een interval teruggeven.
- Nieuwe functie `char()` voor teruggeven van een overeenkomend teken voor een waarde Unicode

### Mogelijkheid: Statistieken voor tekst- en datumvelden
Het dock voor statistische overzichten kan nu  doorlopende statistieken voor teken- en datumvelden berekenen.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Straal van boogpunt weergeven in gereedschap Info
Indien u klikt op een gebogen lijn met behulp van het gereedschap Info, zal QGIS nu de straal in het gereedschap Info weergeven.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Marco Hugentobler
### Mogelijkheid: Doorlopende ondersteuning voor expressies
QGIS 2.16 voegt ondersteuning voor verscheidene types doorlopende berekeningen toe aan het programma voor expressies. Deze omvatten:
1. Totaliseert binnen de huidige laag, bijv. `sum("passengers")` Ondersteunt subexpressies (d.i. `sum("passengers"/2)` ), groeperen op ( `sum("passengers", group_by:="line_segment")` ), en optionele filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relationele totalen, die een totaal berekenen uit alle overeenkomende kindobjecten uit een relatie, bijv. `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. Een overzichtsfunctie totaal, voor het berekenen van totalen over andere lagen. Bijv. `aggregate('rail_station_layer','sum',"passengers")`. De overzichtsfunctie totaal ondersteunt nu een optioneel filter, wat het mogelijk maakt dingen te berekenen zoals: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` voor het berekenen van het totale aantal passagiers voor de stations binnen het huidige object Atlas

In alle gevallen worden de berekeningen gecached binnen de context van de expressie, zodat zij slechts eenmaal behoeven te worden berekend voor elke set van evaluaties voor expressies.

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Plug-in fTools is vervangen door algoritmen voor Processing
fTools was een bronplug-in die voor jaren de gereedschappen verschafte voor het menu `Vector` in QGIS. Met de voortgang van het framework Processing in QGIS processing framework, begon fTools een duplicaat te worden van inspanningen, en veel van de gereedschappen werden verbeterd in hun equivalenten in Processing. De plug-in fTools is, om dit aan te pakken, verwijderd uit QGIS en de equivalente menuitems zijn toegevoegd aan het menu Vector, en verwijzen naar de gereedschappen in het framework Processing die hetzelfde resultaat opleveren.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Alex Bruy
## Processing
### Mogelijkheid: Puntlocaties instellem met een klik op de kaart
Parameters voor Processing die een puntlocatie verwachten kunnen nu wprden ingesteld door te klikken op een locatie in het kaartvenster. Eerder moesten coördinaten handmatig worden ingevoerd.

Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Mogelijkheid: Ondersteuning voor expressies en variabelen
Invoer en uitvoer in dialoogvensters van algoritmen ondersteunen nu expressies en variabelen van QGIS.

Deze mogelijkheid werd ontwikkeld door Victor Olaya
### Mogelijkheid: Vooraf geconfigureerde algoritmen
Algoritmen met vooraf gedefinieerde parameters kunnen nu worden toegevoegd aan de Toolbox van Processing, als een sneltoets voor een bepaald proces.

Deze mogelijkheid werd ontwikkeld door Victor Olaya
### Mogelijkheid: Een plug-in maken met op scripts gebaseerde algoritmen uit de Toolbox
Eerder was de enige manier om een plug-in voor QGIS te maken die nieuwe algoritmen toevoegde aan Processing om deze algoritmen handmatig te maken en een nieuwe provider voor algoritmen te maken. Nu kunnen algoritmen worden geschreven als eenvoudige scripts voor Processing, en een plug-in die ze bevat kan dicrect worden gemaakt vanuit de Toolbox van Processing.  Die plug-in kan dan worden gedistribueerd als een normale plug-in, en zal, indien geactiveerd, Processing uitbreiden.

Deze mogelijkheid werd ontwikkeld door Victor Olaya
### Mogelijkheid: Authenticatiebeheer gebruiken in PostGIS gerelateerde algoritmen
PostGIS gerelateerde algoritmen gebruiken nu authenticatiebeheer van QGIS om de inloggegevens op te halen uit de database van PostGIS.
- In het geval dat een authenticatiemethode is ingesteld voor een verbinding naar PostGIS, zal de gebruiker worden gevraagd naar zijn hoofdwachtwoord.
- In het geval dat geen authenticatiemethode voor de verbinding werd ingesteld, zullen de inloggegevens worden opgehaald uit de cache voor inloggegevens of, als die daar niet wordt gevonden, worden gevraagd aan de gebruiker en voor verder gebruik worden opgeslagen in de cache voor inloggegevens.

Hiermee is het niet langer noodzakelijk om platte wachtwoorden op te slaan in de instellingen voor verbindingen om PostGIS gerelateerde algoritmen te gebruiken.

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Ondersteuning voor het scrhijven van tabellen zonder geometrie
Het algoritme OutputVector ondersteunt nu het schrijven van tabellen zonder geometrie.

Momenteel was dit alleen toegepast voor het algoritme Refactor Fields maar kon eenvoudig worden uitgebreid naar andere op attributen gebaseerde algortimen.

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Aanvullende algoritmen voor GRASS in Processing
Voor deze uitgave bevat QGIS Processing nu elk algoritme voor [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) en [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) uit GRASS7. Nu zijn er meer dan 300 algoritmes direct voor u beschikbaar in de interface van QGIS. U heeft alle kracht van GRASS7 direct ingebracht in QGIS en u kunt algoritmen van GRASS7 mixen met alle andere algoritmes van Processing zonder een database voor GRASS7 te moeten gebruiken.

Sommige testen voor eenheden (meestal voor algoritmen voor rasters en afbeeldingen) zijn ook voor sommige algoritmen opgenomen, wat het onderkennen van problemen gemakkelijker maakt om af te handelen en te verwerken.

Onthoud dat op dit moment algoritmen van Processing  voor GRASS7 alleen Shapefile vectorlagen en rasters van GeoTiff gebruiken en produceren. Er is ook een beperking voor enkele algoritmen voor rasters van GRASS7 (alle algoritmen die kleurentabellen kunnen bewerken) die rasterlagen naar tijdelijke mappen dupliceren. Afhankelijk van de grootte van uw bronrasters, zult u waarschijnlijk ruimte op de schijf nodig hebben om ze te verwerken.

Deze mogelijkheid werd ontwikkeld door [Médéric Ribreux](https://medspx.fr)
## Gegevensproviders
### Mogelijkheid: Gegevenssets van OGR worden standaard geopend in modus Alleen-lezen
Maakt gelijktijdig bewerken van Shapefiles en Tab-bestanden in zowel QGIS als MapInfo mogelijk.

Dit werd mogelijk gemaakt door [MEDDE (Franse Ministerie voor Duurzame Ontwikkeling)](http://www.developpement-durable.gouv.fr)

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mogelijkheid: Verbeterde afhandeling van Postgres velden type DOMAIN
QGIS geeft nu het juiste type domain als typenaam voor het veld, en is in staat om op correcte wijze de lengte en precisie van typen domain te bepalen. Bekijk de PostgreSQL [documentatie](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) voor meer informatie over typen DOMAIN.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Maak modus readOnly van vectorlagen te configureren in project
Met behulp van deze optie kunt u voorkomen dat gebruikers per ongeluk lagen bewerken. Ga naar `Projecteigenschappen -> Lagen identificeren` om te configureren welke lagen als Alleen-lezen zouden moeten worden weergegeven.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://opengis.ch/)
### Mogelijkheid: Ondersteuning voor databases DB2
Deze mogelijkheid werd ontwikkeld door David Adler
### Mogelijkheid: Postgres gematerialiseerde weergaven vernieuwen in DB manager
### Mogelijkheid: Attribuut OGR FID weergeven
QGIS geeft nu het OGR FID als eerste attribuut weer  als dat van belang is, bijv. voor GPKG en andere op database gebaseerde stuurprogramma's.

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mo0gelijkheid: services voor ArcGIS Map en Feature REST
QGIS is nu in staat te verbinden met services van ArcGIS REST.

U kunt verbinden met services van ArcGIS Feature (equivalent voor WFS in de wereld van ESRI) en services van ArcGIS Map (WMS equivalent). De provider stelt u in staat kaarten en vectorlagen van deze services te lezen.

Deze mogelijkheid is bijzonder handig voor gebruikers die zouden willen wijzigen van een ESRI GIS stapel zonder iets te verliezen dat zij al hebben gebouwd in private of publieke services voor kaarten. U kunt oo vebrinden met publieke services die worden verschaft door ESRI.

Dit werd mogelijk gemaakt door [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

Deze mogelijkheid werd ontwikkeld door [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Stijlen opslaan in databases van MS SQL en Oracle
Deze mogelijkheid werd ontwikkeld door Jürgen Fischer en Christian Frugard
### Mogelijkheid: Velden hernoemen in lagen
In QGIS 2.16 kunt u nu velden henroemen in Postgres, Oracle, OGR en geheugenlagen door te dubbelklikken op de veldnaam in het venster van de Laageigenschappen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Basisondersteuning voor Oracle Workspace Manager
Ondersteuning is toegevoegd voor Oracle Workspace Manager bij het gebruiken van de Oracle Provider.

Bekijk <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

Dit werd mogelijk gemaakt door [ENEL](https://www.enel.com)

Deze mogelijkheid werd ontwikkeld door [Jürgen Fischer voor Faunalia](http://faunalia.it)
### Mogelijkheid: Enorme verbeteringen aan WFS Provider
QGIS 2.16 brengt een volledige renovatie van de WFS provider, inclusief
- Automatisch detecteren van de versie
- On-disk cachen van gedownloade objecten
- Downloaden op de achtergrond en progressief renderen
- Ondersteuning voor WFS 1.1 en 2.0
- WFS 2.0 GetFeature paging
- Testen vor provider toevoegen
- Ondersteuning voor joins in WFS 2.0
- Parameter URI met SQL met clausules SELECT / FROM / JOIN / WHERE / ORDER BY 
- DateTime-velden afhandelen
- \"Alleen objecten verzoeken die het weergavebereik overlappen\" standaard inschakelen (en de instellingen onthouden)
- Ondersteuning voor aanvullende/gemixte typen geometrie (CurvePolygon, CompoundCurve)
- Grotere tolerantie voor niet-conformerende servers voor WFS

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Land Information Nieuw-Zeeland en Kanton Zug, Zwitserland](http://www.linz.govt.nz/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Genereren van standaardwaarden in lagen van Postgres \"net op tijd\"
De gebruikte expressie om standaard waarden voor een veld in de database van Postgres worden momenteel afgedrukt op het forumlier van het object.

    nextval('serial')
    
Een nieuwe optie in de \"Projecteigenschappen\" (tab \"Databronnen\") maakt het mogelijk het formulier te evalueren voordat het wordt geopend en zal de nieuwe waarde direct in het formulier van het object afdrukken.

    23
    
Het grote voordeel van deze verbetering is dat men nu direct records van gerelateerde tabellen kan maken en koppelen zonder eerst de gegevens te moeten opslaan, omdat de primaire sleutel al aanwezig is vóórdat het object wordt opgeslagen.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Kanton Zug, Zwitserland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://opengis.ch/)
## QGIS Server
### Mogelijkheid: Ondersteuning voor met rood onderstrepen in GetMap en GetPrint
Dit werd mogelijk gemaakt door Kanton Solothurn

Deze mogelijkheid werd ontwikkeld door [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Standaard transformatie van datum voor server
U zult <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> moeten lezen voor de details

Deze mogelijkheid werd ontwikkeld door [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Plug-ins
### Mogelijkheid: Vernieuwde plug-in Globe
- Update naar OsgEarth 2.8
- Herschreven stuurprogramma voor QGIS Globe tegels
- Herschreven logica voor synchronizatie tussen 2D en 3D
- Migratie naar nieuwe kernel voor geometrie
- Ondersteuning voor meerdere achtergrondlagen
- Menu's ingebed in venster van Globe
- Onafhankelijke selectie van lagen voor Globe
- Afgeleid van het werk in de master thesis van Mathias Kuhns van QGIS 2.1/OsgEarth 2.4

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

Deze mogelijkheid werd ontwikkeld door [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Globe: Objecten vervormen
Vervormen van objecten naar de 3e dimensie mogelijk maken.

Ofwel door een vaste waarde of door een attribuut of expressie.

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: API: Pagina's toevoegen aan de eigenschappen van vectorlagen
Toevoegen van aanvullende pagina's in het dialoogvenster Eigenschappen van vectorlagen mogelijk maken.

Dit maakt het mogelijk de configuratie voor aan lagen gerelateerde opties, die worden verschaft door een plug-in, direct daar te plaatsen waar zij horen voor een betere ervaring voor de gebruiker.

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Globe: Ondersteuning voor vector
Behoud vectorgegevens bij het weergeven van lagen op globe.

Dit werd mogelijk gemaakt door Master Thesis UZH

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Globe: Verticaal overdrijven voor DTM
Omdat het soms gewoon leuk is om de grootte te overdrijven.

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](http://www.opengis.ch)
## Programmeerbaarheid
### Mogelijkheid: Ingebedde widgets in lagenboom
Dit maakt het mogelijk definities van widgets in te bedden in de lagenboom voor individuele lagen in het dialoogvenster Laageigenschappen (in de nieuwe tab Legenda). Het idee erachter is om een manier te hebben om snel toegang te krijgen tot enkele acties die vaak op een laag worden gebruikt.

De implementatie bevat widgets met transparantie, in de toekomst zouden er meer standaard widgets kunnen komen, bijv. om een filter in te stellen, selecteren, stijl of andere dingen. De API staat plug-ins toe om hun eigen widgets te registreren, die nuttig kunnen zijn voor verscheidene domeinspecifieke plug-ins om aangepaste widgets toe te wijzen aan lagen die zij beheren.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
### Mogelijkheid: Plug-ins kunnen pagina's toevoegen aan de eigenschappen van vectorlagen
Deze mogelijkheid werd ontwikkeld door [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Mogelijkheid: Nieuwe klassen voor PyQGIS in 2.16
### Nieuwe bronklassen
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) - een abstracte basisklasse voor items van Printvormgeving die algemene methodes voor op knopen gebaseerde vormen, zoals polygonen of polylijnen, verschaft 
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - een item voor Printvormgeving voor polygoonvormen
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) - een item voor Printvormgeving voor polylijnvormen
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.html) - een opdrachtklasse Ongedaan maken voor Printvormgeving voor groeperen / opheffen groeperen van items van Printvormgeving
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) - WKB-lezer die geometrieën direct vereenvoudigt
- [QgsAction](https://qgis.org/api/classQgsAction.html) - een programmaklasse die een actie, gebaseerd op attributen van een vector, bevat
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - opslaan en beheren van acties die zijn geassociaeerd met een laag
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) - een programmaklasse voor het berekenen van totalen voor een veld (of expressie) over de objecten van een vectorlaag
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) - een container voor het configureren van de attributentabel van een vectorlaag
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) - berekeningen voor overzichtsstatistieken en totalen voor een lijst datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - een weergave van de interval tussen twee waarden van datetime
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handelt exporteren van objecten QgsFeature naar objecten GeoJSON af
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - hulpprogramma's voor het werken met conversies van JSON en GeoJSON
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) - eenvoudig profiel voor het timen van codepaden gedurende de uitvoering
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - programmaklasse voor het parsen van argumenten voor SQL
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) - berekeningen voor overzochtsstatistieken en totalen voor een lijst tekenreeksen
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - een renderer voor het genereren van live modellen voor schaduwen van heuvels
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) - lijnsymboollaag gebruikt voor het weergeven van lijnen als pijlen
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) - een renderer die standaard geen symbolen tekent voor objecten, maar dat voor labels en diagrammen voor de laag wel toestaat
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) - abstracte basisklasse voor eenvoudige symbollagen voor markereringen. Handelt het maken van de symboolvormen af maar laat het echte tekenen van de symbolen over aan subklassen.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) - gevulde symboollaag voor markering, bestaande uit een vorm die is gerenderd met behulp van een QgsFillSymbolV2

### Nieuwe klassen voor GUI
#### Opnieuw te gebruiken widgets:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) - een widget voor een gereedschapsknop die wordt weergegeven naast de widgets Wijzig hulpmiddel in formulieren van attributen, en het mogelijk maakt te beheren hoe het widget zich gedraagt en interacteert met het formulier in de modus Meervoudig bewerken
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) - een widget voor een gereedschapsknop die wordt weergegeven naast de widgets Zoeken in formulieren van attributen, en het mogelijk maakt te beheren hoe het widget zich gedraagt en hoe het filteren/zoeken werkt
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) - een widget om in de lagenboom ingebedde widgets te configureren voor een bepaalde kaartlaag
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) - providerinterface om te worden geïmplementeerd om nieuwe soorten ingebedde widgets, om in de lagenboom te gebruiken, te introduceren
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -  register van widgets die kunnen worden ingebed in de weergave Lagenboom
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) - een widget dat bestaat uit zowel een widget Wijzig hulpmiddel en aanvullende widgets voor het beheren van het gedrag van het widget Wijzig hulpmiddel, afhankelijk van een aantaal mogelijk modi
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) - een combinatievak dat items weergeeft van een overeenkomend type uit een lay-out
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) - een aangepaste widget voor QGIS voor het selecteren van een kleur, inclusief opties om kleuren te selecteren via
- kleurenwiel, kleurvlakken, en een kleurenvoorbeeld
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subklasse met fijner beheer over hoe het widget wordt gesloten of geopend
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - een gebeurtenisfilter voor het kijken naar gebeurtenissen focus op een ouderobject
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) - een interactieve bewerker voor het voorbeeld van een balk voor kleurverloop en het aanpassen van de positie van stops voor kleuren in het kleurverloop
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) - een paneelwidget dat kan worden weergegeven in het dock Kaartstijl
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) - fabrieksklasse voor met maken van aangepaste pagina's voor eigenschappen van kaartlagen
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - basisklasse voor elk widget dat kan worden weergegeven als een inregelig paneel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) - widget inregelige paneelwrapper voor bestaande widgets waarvan de boom van erven niet kan worden gewijzigd, bijv. dialoogvensters
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) - een stapelwidget om panelen in de interface te beheren
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) - een klasse die een lijst van QActions en QShortcuts bevat die zijn geregistreerd, en waarvan het mogelijk is de sneltoetsen te wijzigen
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) - dit kan worden gebruikt als een normaal QTableWidgetItem met dit verschil dat een specifieke rol kan worden ingesteld voor sorteren
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) - widget renderer voor configureren van de renderer voor schaduwen van heuvels
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) - widget voor het beheren van de transparantie van een rasterlaag en gerelateerde opties
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) - widget renderer voor het configureren van symbollagen pijlen

#### Opnieuw te gebruiken dialoogvensters:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) - dialoogvenster voor beheren (verbergen en herordenen) van kolommen in de attributentabel
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) - dialoogvenster om gebruikers sneltoetsen te laten configureren die zijn opgenomen in een QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) - dialoogvenster om parameters in te stellen om een nieuwe laag voor GeoPackage te maken
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) - algemene widgetklasse voor vermelden van lagen die beschikbaar zijn in een service op afstand

## Belangrijke reparaties
### Mogelijkheid: Programma van QGIS voor oplossen van problemen tegen betaling
We hebben nogmaals een ronde uitgevoerd van het oplossen van problemen tegen betaling (met dank aan onze sponsors en donoren!). Hier volgt ene overzicht van het werk van de ontwikkelaars die hebben deelgenomen:
### Nyall Dawson
Hier is de volledige lijst (gesorteerd op prioriteit):
- Opgelost: Gebroken projectieve transformatie in Georeferencer (#14551 - severe)
- Opgelost: Mislukken van selecteren van objecten op radius (#14748 - severe)
- Opgelost:  Onjuiste berekening van gebied voor polygoon (#14675 - severe, although very unlikely to occur. Unit tests added to cover this edge case)
- Opgelost: Lay-out widget dock (#15011 - severe)
- Opgelost:  crash in symboollaag pijl (unreported)
- Opgelost:  crash bij maken van ongeldige join (unreported)
- Opgelost:  SVG's met parameters niet weergegeven voor pijlitems van Printvormgeving (#14997 - high)
- Classificaties op samengevoegde velden zou alleen waarden moeten overwegen die overeenkomen met objecten op de laag (#9051 - high)
- Altijd vergelijking voor tekenreeksen gebruiken in expressies voor velden tekenreeks (#13204 - high)
- Opgelost:  home dir wordt toegevoegd als standaard pad voor SVG en sjabloon (#14662, #14652, #14883 - high)
- Opgelost: crash bij gebruiken van geïnverteerde polygonen met renderer Heatmap (#14968 - high)
- Waarden van rastersymbologie opslaan met volledige precisie (#14950 - normal)
- Acties worden niet ingeschakeld bij het laden van een laag met standaard stijl (#13910 - normal)
- Verwijderen van tekst \"attributentabel\" uit titel van dialoogvenster (#14959 - normal)
- Opgelost: kan opvang voor aangepast widget niet deactiveren (#9732 - normal)
- Opgelost:  hoogte/breedte van kop symboollaag pijl omgedraaid (#15002 - normal)
- Opgelost:  joins worden niet opnieuw gemaakt bij laden van project met slechte lagen (#10500 - normal)
- Ongeldige cache voor join als laag werd aangepast (#11140 - normal)
- Juist ondersteunen van joins bij gebruiken van virtuele velden (#14820 - normal)
- Opgelost:  virtuele velden die afhankelijk zijn van andere virtuele velden mogen in bepaalde omstandigheden niet worden berekend (#14939 - normal)
- Opgelost:  op regsls gebaseerde labels niet weergegeven bij het gebruiken van functies van expressies in Python (#14985 - normal)
- Automatisch vernieuwen als niveaus van symbolen werden gewijzigd in dock Stijl (#14861 - normal)
- Opgelost:  Knop van dock Stijl niet gesynchroniseerd met de status van het dock (#14862 - normal)
- Opgelost:  problemen bij renderen van SVG met tekst (#14644, #14794 - normal)
- Er voor zorgen dat de met de knop Gegevensgedefinieerd weergegeven velden altijd up to date zijn (#14809 - normal)
- Opgelost: kan geen sneltoets voor inzoomen instellen (#14958 - normal)
- Opgelost: geïinverteerde polygonen en renderer voor plaatsing staan geen klikken met rechts toe op items in Legenda (#14966 - normal)
- Opgelost: geïnverteerde polygoon & renderer voor plaatsing geven geen kleurenwiel weer in menu Legenda (#14967 - normal)
- Ontbrekende proxies toevoegen voor gedrag bij kiezen in Legenda voor subrenderers voor geïnverteerde polygoon en renderers plaatsing (unreported)
- Opgelost: samengevoegde attributen kunnen niet worden gebruikt in filterexpressies (#13176 - low)
- Type WKB weergeven inmetadata van vectorlaag (unreported)
- Ontbrekende tekenreksen voor capabilities toevoegen aan metadata van laag (unreported)
- Opgelost: debug ruis bij gebruiken van 25D geometrielagen (unreported)
- Opgelost:  sommige widgets van de statusbalk konden niet worden verborgen via aanpassingen (unreported)
- Stijlwidget live maken van toepassen van onthouden van instellingen (unreported)
- Geen berichten voor beperkingen weergeven als formulier in modus Zoeken staat (unreported)
- Schuifbalken weergeven voor attributenformulier als identificatieresultaten (unreported)
- Knop Toepassen van Stijldock altijd ingeschakeld maken (unreported)
- Opgelost: enkele ontbrekende automatische bijwerkingen van Stijldock (unreported)

Ik heb ook een groot aantal oplossingen voor problemen uit de fork van Sourcepole doorgevoerd.
### Even Rouault
Hier zijn de tickets die hij heeft behandeld gedurende de hem toegewezen tijd voor het oplossen van problemen voor QGIS 2.16.

**Severe/High:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS-client verbroken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: probleem bij sorteren van attributentabel met qgis-rel-dev (regressie vanuit 2.14.X)
- <https://issues.qgis.org/issues/15064>: QGIS crashes in OGR-lagen met wkbUnknown25D, wkbUnknownM/Z/ZM laag type geometrie
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hangt bij renderen van de kaart
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash bij verwijderen van laatste segment van een compoundcurve

**Normal**
- <https://issues.qgis.org/issues/14965>: WFS-provider kopieert objecten bij in- en uitzoomen
- <https://issues.qgis.org/issues/14928>: WMS request zonder BBOX
- <https://issues.qgis.org/issues/14999>: SpatiaLite provider ondersteunt geen alfanumerieke primaire sleutels (terug ingevoerd in 2.14)
- <http://hub.qgis.org/issues/15061>: Kan geen WFSlaag toevoegen
- <https://issues.qgis.org/issues/15065>: Mislukte detectie van type geometrie onder bepaalde voorwaarden
- <https://issues.qgis.org/issues/15066>: OGR: OGR: Soms sublagen gedetecteerd indien niet relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export maakt ongeldig bestand
- <https://issues.qgis.org/issues/15081>: Onmogelijk om geometrie van object op te schonen uit een shapefile
- unreported \[Geometry\] Opgelost: verscheidene problemen gerelateerd aan importeren van Wkb/Wkt

**Andere:**
- <https://issues.qgis.org/issues/14981>: Importeren van Shapefile naar Geopackage-database in DB-Manager mislukt (analyse)
- <https://issues.qgis.org/issues/15011>: paneel Browser panel is niet te gebruiken (bisection & analyse)
- <https://issues.qgis.org/issues/14909>: regressie: QGIS crasht bij sluiten van gedockte attributentabel (analyse)
- <https://issues.qgis.org/issues/13353>: QGIS en GDAL 2.0.0 (closed: geen verdere actie nodig)
- <https://issues.qgis.org/issues/15053>: WMS met EPSG:31255 wordt verschoven (datum=hermannskogel) (analyse. waarschijnlijk gedateerde versie van Proj.4)

### Sandro Santilli
- <http://hub.qgis.org/issues/14262>: Overloop in primaire sleutel met negatieve waarden; kan bewerkingen niet opslaan
- <http://hub.qgis.org/issues/12228>: Vastloper bij parallel renderen
- <http://hub.qgis.org/issues/11371>: Printvormgeving: groeperen + verplaatsen + groeperen opheffen + ongedaan maken = crash 
- <http://hub.qgis.org/issues/14976>: Bestanden in opslagplaats aangepast door \"make check\"
- <http://hub.qgis.org/issues/13635>: Verschillende afhandeling van ongeldige geometrieën tussen LTR en de versie master
- <http://hub.qgis.org/issues/13952>: QGIS gereedschap Knoop veroorzaakt willekeurig snappen aan een ander object

### Martin Dobias
- Digitaliseren: \"Object vereenvoudigen\" zou geen dialoogvenster moeten openen als niet op een object wordt geklikt
- Digitaliseren: hoe gereedschap \"Object vereenvoudigen\" of \"Object roteren\" te verlaten is niet duidelijk genoeg
- Eén weg ontbreekt bij Vectorlaag toevoegen!
- Automatisch traceren mislukt bij Cirkelbogen in geometrieën
- WMS werkt niet in master a625eeb (2.15.0-80)
- Python fout in verwerken van vooraf gedefinieerde algoritmen
- GPS neemt geen geometriepunt op, maar alleen waarden voor attributen\...
- Stijldock: paneel transparantie (globale transparantie, transparante pixel, etc.) werkt niet voor renderer van schaduwen voor heuvels
- Stijldock: knop Terug & broodkruimels ontbreken als een op regels gebaseerde regel wordt bewerkt
- Opgelost:  Ongedaan maken/opnieuw voor op regels gebaseerde renderer/labels in dock voor opmaken
- Opgelost:  bijwerkingen van widget Ongedaan maken in paneel Opmaken
- Stijldock: herstellen van de waarde globale transparantie voor de renderer van schaduwen van heuvels na wijzigen van instellingen voor symbologie
- Stijldock: waarden van opties voor renderen van rasterlaag niet juist hersteld

### Matthias Kuhn
- Stabiliteit van QgsMapLayerRegistry verbeteren
- Processing: algoritme Difference: negeert niet standaard ongeldige geometrieën
- Opgelost:  Enkele problemen voor compatibiliteit voor Python 3
- Gewerkt aan opnieuw inschakelen van testen voor OSX (samengevoegd na uitgave van 2.16)
- API documentatie
- startup.py wordt twee keer uitgevoerd
- reparaties UX:
  - Attributentabel: altijd sequentiele nummers voor kolomkoppen weergeven
  - Widget Relatieverwijzing : Formulierknop alleen inschakelen als een object is ingesteld
  - Object-ID in helptip van attributentabel weergeven
  - Initiële focus widget in dialoogvenster inloggegevens
  - Standaard timeout voor items van berichtenbalk
  - Status van knop\" in  dialoogvenster voor selecteren van bron van Postgis toevoegen
- Ontbrekende kopbestanden toevoegen
- Crash bij afsluiten
- Netwerk map voor cache
- Objectformulier verborgen achter hoofdvenster op Windows
- Offline bewerken: Respecteer relatieve paden
- Offline bewerken: gewijzigde attributen komen in het verkeerde object terecht
- Offline bewerken: Niet crashen met rasterlagen
- Relatieformulier groeit oneindig
- Opgelost:  crash bij laden van stijl in laageigenschappen
- Opgelost:  crash bij sluiten van vastgezette attributentabel
- Opgelost: standaard foutief geconfigureerd pad voor GPSBabel
- Juiste aantal objecten weergeven bij regel die geometrie vereist
- Opgelost:  crash bij gebruiken van renderer 2.5D met niet compatibele laag

{{<content-end >}}
