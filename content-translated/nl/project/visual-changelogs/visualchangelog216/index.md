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

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Dit is geen Long Term Release (Lange Termijn Release)**

Deze uitgave is niet bestemd als een Long Term Release (LTR). gebruikers die een versie van QGIS willen die niet wijzigt en voor tenminste 1 jaar geen oplossingen voor problemen willen, worden geadviseerd de huidige LTR-uitgave 2.14 te gebruiken (die nu, bij de uitgave van QGIS 2.16, onze officiële LTR wordt).

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Dankwoord**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 2.16.0
Elk jaar ontvangen wij ook ondersteuning van verschillende organisaties die het werk wat wij doen waarderen en die het mogelijk willen maken dat de ontwikkeling van het QGIS project vooral blijft doorgaan. Deze sponsoren, genoemd in onderstaande lijst, zijn wij zeer dankbaar! 

{{<fund type="changelog" >}}
## Algemeen
### Mogelijkheid: Objecten kopiëren in indeling GeoJSON
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Ruimtelijke bladwijzers in projectbestanden opslaan
Wanneer u een ruimtelijke bladwijzer maakt, kunt u er nu voor kiezen om de bladwijzer op te slaan in uw actieve projectbestand. Scroll door het paneel met bladwijzers om het keuzevak te zoeken om deze mogelijkheid in te schakelen.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### Mogelijkheid: Ondersteuning voor berichten van GNSS GNRMC
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Ondřej Fibich
### Mogelijkheid: Objecten van GeoJSON direct in QGIS plakken
De afhandeling van het klembord van QGIS kan nu vele aanvullende tekstindelingen parsen, inclusief eigen ondersteuning voor collecties van objecten van GeoJSON. Dit stelt u in staat om direct teksttekenreeksen van GeoJSON in QGIS te plakken en ze automatisch te hebben geconverteerd naar objecten en geometriën voor QGIS.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeteringen voor kaarttips
- De zichtbaarheid voor kaarttips wordt nu bewaard tussen sessies
- Kaarttips kunnen nu HTML-inhoud weergeven, inclusief afbeeldingen, video's en URL-koppelingen

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Mogelijkheid: Desktop MIME-pictogrammen voor bestandstypen van QGIS
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - QGIS projectbestand
- \*.qml - Bestand met instellingen voor laag
- \*.qlr - Bestand met definities voor laag
- \*.qpt - Sjabloonbestand voor printvormgeving

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## Gebruikersinterface
### Mogelijkheid: Vergrootglas kaartvenster
Een gereedschap Vergrootglas is toegevoegd aan QGIS, wat het u mogelijk maakt de kaart weer te geven in ene bepaalde schaal. Dit stelt u in staat in te zoomen op ene kaart, zonder de schaal van de kaart te wijzigen, wat het eenvoudiger maakt om nauwkeuriger de posities van labels en symbolen aan te passen. Aanvullend kan in de instellingen ene standaard vergrotingsfactor worden gedefinieerd, wat erg nuttig is voor schermen met hoge resoluties!

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Verbeteringen aan zoomen op de kaart
QGIS 2.16 brengt verbeteringen voor de manier waarop u in en uit kunt zoomen op het kaartvenster.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Bewerker voor interactieve kleurverlopen opnieuw ontworpen
De bewerker voor kleurenbalken is opnieuw bewerkt met interactieve besturingselementen voor het eenvoudiger manipuleren van kleurverlopen. Het dialoogvenster heeft nu ook een interactieve plot voor het aanpassen van stops voor het kleurverloop via de waarden van de kleuren HSV of RGB. De nieuwe mogelijkheden van de bewerker:
- slepen om stops voor kleuren te verplaatsen
- dubbelklikken om een nieuwe stop toe te voegen
- drukken op Delete zal de geselecteerde stop wissen
- drukken op pijltjestoetsen zal de geselecteerde stop verplaatsen, en ingedrukt houden van Shift tijdens het drukken op een pijltjestoets resulteert in ene grotere verplaatsing
- slepen en neerzetten van een kleur op de widget om een nieuwe stop toe te voegen

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Keuze voor de standaardweergave voor het dialoogvenster Attributen
In eerdere versies van QGIS zou het dialoogvenster Attributen altijd worden geopend in de tabelweergave. Nu heeft u de keuze om standaard altijd het dialoogvenster te openen in ofwel de tabelweergave, de formulierweergave of om de laatst gebruikte weergave te onthouden.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeteringen aan pop-ups van de kalender
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterde kleurenkiezers
De keuzemenu's voor knoppen van kleuren geven nu een kleurenwiel weer, wat het mogelijk maakt snelle aanpassingen te maken aan kleuren.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### Mogelijkheid: Celinhoud uit attributentabel kopiëren
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Verbeterde ondersteuning voor HiDPI
Gebruikers van HiDPI-schermen zullen merken dat er een verbeterde gebruikersinterface is omdat er werk is gemaakt van het opwaarderen van pictogrammen om te kunnen vertrouwen op afbeeldingen van SVG. Vanaf QGIS 2.16 zijn alle werkbalken nu compatibel met HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Verbeterd gedrag van het gereedschap Selecteren op de kaart
Het gedrag van op de kaart gebaseerde gereedschappen om te selecteren is verfijnd, met de volgende wijzigingen:

Voor selecties van klikken-en-slepen:
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Voor selecties met één enkele klik:
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Deze wijziging brengt het gedrag van het kaartvenster in lijn met andere toepassingen voor ontwerpen en ook met het gedrag van printvormgeving.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Bijwerkingen van documentatie
### Mogelijkheid: Documentatie voor QGIS 2.14
Er is nu een automatische manier om een ticket te maken in de opslagplaats voor de documentatie voor elke nieuwe mogelijkheid in QGIS. We zijn er zeker van dat alle nieuwe mogelijkheden nu zijn opgenomen in de documentatie.

Het team voor de documentatie heeft hard gewerkt aan drie uitgaven van QGIS: 2.10, 2.12 en 2.14, dus nu is de documentatie up to date voor de huidige Long Term Release van QGIS. Dat zijn ongeveer 180 nieuwe mogelijkheden die zijn beschreven in de 4 maanden.

Als u denkt dat er nog enkele mogelijkheden ontbreken in de documentatie, mak dan een nieuw ticket aan, schrijf een korte tekst om het t ebeschrijven of, beter nog, dien een bijdrage in.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

Het team voor de documentatie zal de volgende maanden hard ana het werk gaan om de huidige stabiele uitgave (2.16) van QGIS te documenteren.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Bekijk de milestones 2.10, 2.12 en 2.14 om al het uitgevoerde werk voor de documentatie te bekijken:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

Deze mogelijkheid werd ontwikkeld door Larry Shaffer
## Symbologie
### Mogelijkheid: Symboollaag Pijlen
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

In de modus Gebogen worden knopen, van de lijnlaag waarop deze symbollaag is gebaseerd, gebruikt als controlepunten voor cirkelbogen. Pijlen kunnen worden gevuld met elke bestaande vulstijl die wordt ondersteund door QGIS. Opties maken het ook mogelijk het type van de pijl te selecteren (met één of twee pijluitienden, gewoon of gehalveer), de breedte ervan (die variabel kan zijn) en de grootte van de pijluiteinden.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuwe toegankelijkheid en symbolen voor verminderd zicht
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Nieuwe symbolen voor eenvoudige markering
- halve cirkel, een derde, kwartcirkels
- markeringen halve driehoek
- gevulde kruis en achthoekige markeringen
- markering diamant ellips

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Selecties kunnen nog steeds worden gemaakt in de laag in het kaartvenster en geselecteerde objecten zullen worden gerenderd met een standaard symbool. Objecten die worden bewerkt zullen ook worden weergegeven.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Meer controle over het renderen van vullingen van zwaartepunten
Een optie is toegevoegd om te beheren of de markering moet worden getekend op alle delen of slechts één enkel deel van meerdelige objecten.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Instelling voor symbool van omtrek van markeringen van lettertype
Het symbool van markeringen van lettertypen mag nu een omtrek hebben, die de zichtbaarheid van dergelijke symbolen kan verbeteren door een bufferkleur voor de omtrek toe te voegen. Ingeschakelde tekens van Emoji-lettertypen kunnen dienen als leuke markeringen, indien gebruikt met een dikke omtrek.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Stijl voor join van omtrek beheren voor eenvoudige, ellips en lettertypemarkeringen
Gebruikers kunnen nu de stijl voor join van omtrek wijzigen voor eenvoudige, ellips en lettertypemarkeringen om hun symbologie fijner af te stemmen.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Nieuw kaartgereedschap voor interactief instellen van verschuiving voor puntsymbool
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Dock voor stijlen
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Labelen
### Mogelijkheid: Kaartgereedschappen voor labels werken nu met op regels gebaseerd labelen
In eerdere versies van QGIS waar op regels gebaseerd labelen werd gebruikt, kon u de kaartgereedschappen voor labels niet gebruiken om posities van labels interactief te plaatsen en te roteren. Dit wortd nu ondersteund.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
## Diagrammen
### Mogelijkheid: Legenda-items voor grootte van diagram
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Selecteren van eenheid voor breedte van omtrek
Selecteren van de eenheid voor de breedte van de omtrek is nu beschikbaar. Dit maakt het mogelijk, voor een diagram met de grootte van kaarteenheden, dat het zal vergroten en verkleinen gebaseerd op de schaal van de kaart waarbij een vaste breedte van de omtrek in millimeters wordt behouden

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Mogelijkheid: Diagrammen gedragen zich zoals labels en kunnen vanaf de werkbalk worden beheerd
Origineel was er een werkbalk voor labels die het mogelijk maakte om:
- opties voor labels van de huidige laag in te stellen
- de vastgezette labels te accentueren. Accentueren is groen op een bewerkbare laag, anders blauw.
- labels vast te zetten of los te maken
- labels te verplaatsen, weer te geven en te verbergen 

Met deze nieuwe mogelijkheid is een nieuw gereedschap beschikbaar in de werkbalk voor labels dat het mogelijk maakt eigenschappen in te stellen voor diagrammen van de huidige laag. Meer nog, elk hierboven genoemd gereedschap is nu ook volledig te gebruiken voor diagrammen.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Renderen
### Mogelijkheid: Nieuwe opties voor direct vereenvoudigen
De gebruiker kan het algoritme selecteren dat moet worden gebruikt, als de vereenvoudiging aan de lokale zijde wordt uitgevoerd, om sneller geometrieën te tekenen. QGIS verschaft nu drie algoritmen:
- Distance (standaard algoritme, en de enige beschikbare optie in eerdere versies van QGIS)
- Snappen aan raster
- Visvalingam

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Mogelijkheid: Op kwantielen gebaseerde classificatie voor rasterlagen
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Piers Titus van der Torren
### Mogelijkheid: Live renderer schaduw voor heuvels
QGIS 2.16 heeft een nieuwe renderer voor  rasters die dynamisch een model voor schaduw voor heuvels zal maken uit een Digital Elevation Model.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Deze mogelijkheid werd ontwikkeld door Asger Skovbo Petersen en Nathan Woodrow
## Digitaliseren
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Geometrieën Lijnen uitbreiden met gereedschap Objecten vervormen
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
### Mogelijkheid: Tolerantie voor segmentatie
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Marco Hugentobler
## Gegevensbeheer
### Mogelijkheid: Nieuwe opties voor configureren van de attributentabel
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Maakt het mogelijk een nieuwe kolom toe te voegen aan de attributentabel om knoppen te bevatten voor het activeren van een actie, gebaseerd op het gekozen object
- Kolommen kunnen in de attributentabel worden verborgen (via klik met rechts op de kop van de veldnaam)
- QGIS onthoudt nu de breedte van elke kolom waarvan de grootte is gewijzigd

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Mogelijkheid: Meerdere kolommen in formulieren voor attributen
Bij het gebruiken van de ontwerper Slepen en neerzetten kan een gebruiker specificeren over hoeveel velden de kolommen moeten worden verdeeld.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Zorg er voor dat u de modus voor ontwerpen van formulieren Slepen en neerzetten gebruikt
- Dubbelklik op een groep containers, zoals tabs of groepen
- een klein dialoogvenster zal verschijnen waar u het aantal kolommen kunt selecteren

De volgorde zal zijn eerste kolom, tweede kolom, n-de kolom, volgende rij, etc.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Mogelijkheid: Beheren van te exporteren attributen bij het opslaan van een vectorlaag
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer, Even Rouault
### Mogelijkheid: Weergave formulieren: zijkolom nu te sorteren
In de modus Formulieren van de attributentabel van QGIS staat een zijkolom die men kan gebruiken om direct naar een specifiek object te springen. Tot aan deze uitgave was deze zijweergave niet te sorteren. Voor het sorteren moest men naar de modus tabel springen en dan weer terug naar de modus Formulieren. Nu kan men het object direct sorteren met het voorbeeld van de attributen van het object in het zijpaneel, door de sorteerfunctie te kiezen in de keuzeknop voor expressies boven de zijkolom.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Mogelijkheid: Widget voor verwijzing naar relatie: sneltoets voor toevoegen van nieuwe waarden
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Mogelijkheid: Verbeteringen voor DXF exporteren
Ondersteuning is toegevoegd voor op regels gebaseerde labels en geroteerde symbolen, en voor het uitvoeren van 3D-geometrieën.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Widgets op bovenste niveau in ontwerper Slepen en neerzetten
Het is nu mogelijk om widgets direct in het formulier te plaatsen met de ontwerper Slepen en neerzetten. Een formulier voor de ontwerper Slepen en neerzetten kan daarom bestaan zonder enige tabs erop.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Op formulier gebaseerd selecteren en filteren
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

Nieuwe knoppen verschijnen aan de onderzijde van het formulier om ofwel overeenkomende objecten te selecteren (met opties voor het toevoegen aan selectie/verwijderen uit selectie/selecteren binnen huidige selectie) of objecten in de tabel te filteren (met opties voor toevoegen van objecten aan huidige filter of het verder beperken van het huidige filter).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Deze mogelijkheid werd mogelijk gemaakt door SIGE, Stad Uster, Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Lagen voor GeoPackage maken
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mogelijkheid: Beperkingen in widgets
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Attributen van meerdere objecten tegelijkertijd bewerken
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

In deze modus zullen wijzigingen aan de waarden van attributen van toepassing zijn op alle geselecteerde objecten. Nieuwe widgets verschijnen naast elk widget voor bewerking wat het mogelijk maakte de huiidge status voor meervoudig bewerken weer te geven en voor het terugdraaien van wijzigingen op een basis van veld-naar-veld.

Wijzigingen worden gemaakt als één enkele opdracht voor bewerken, dus zal het drukken op Ongedaan maken alle wijzigingen voor alle objecten in één keer terugdraaien.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Legenda van laag
### Feature: New option to zoom to a layer\'s visible scale range
Voor lagen met een ingesteld zichtbaar schaalbereik, zal het selecteren van deze optie automatisch de schaal instellen op de dichtstbijzijnde schaal waarmee de laag zichtbaar is. Aanvullend is de interface zodanig aangepast dat lagen die buiten hun schaalbereik liggen en zijn verborgen uitgegrijsd worden weergegeven in de lagenboom.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Printvormgeving
### Mogelijkheid: Nieuwe gereedschappen voor het tekenen van polygonen en polylijnen
Twee nieuwe types van vormitems voor printvormgeving, gebaseerd op knopen, zijn nu beschikbaar in de printvormgeving. Door deze te gebruiken kunt u met een paar klikken polygonen of polylijnen in uw lay-out tekenen.

Nieuwe gereedschappen zijn ook toegevoegd aan om het mogelijk te maken knopen te bewerken (d.i. knopen verplaatsen of verwijderen) en ook om nieuwe knopen aan een bestaande vorm toe te voegen. items polygoon en polylijn in Printvormgeving kunnen ook worden opgemaakt met behulp van alle beschikbare symboolstijlen voor lijn- en polygoonlagen!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Mogelijkheid: Relatieve links in labels van Printvormgeving
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Ingebedde objecten voor atlas in HTML-bron in Printvormgeving als GeoJSON
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### Mogelijkheid: Ondersteuning van SVG met parameters voor SVG-afbeeldingen in Printvormgeving
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Eenvoudiger gebruik van HTML in labels
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Uitvoer van geoverwijzingen (bijv PDF) vanuit Printvormgeving
In QGIS 2.16 zal de Printvormgeving automatisch geoverwijzingen uitvoeren (als de indeling van de uitvoer dat mogelijk maakt, bijv TIF en PDF).

De bestaande optie om een world file te maken is afgescheiden van de kaartselectie voor geoverwijzingen. Het nieuwe gedrag is om altijd geoverwijzingen uit te voeren, en alleen het afzonderlijke world file te maken als die optie is geselecteerd.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: kaarten van Printvormgeving worden nu automatisch bijgewerkt met voorkeuzen
Als een kaart van Printvormgeving is ingesteld om een voorkeuze-stijl te volgen, zal die automatisch, elke keer als de stijl wordt gewijzigd, worden bijgewerkt.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
## Analyse-gereedschappen
### Mogelijkheid: Benoemde parameters in expressies
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

Gebruiken van benoemde parameters helpt verduidelijken waar de argumenten voor een functie voor een expressie naar verwijzen, wat nuttig is als u probeert een expressie te interpreteren op een latere datum!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Meer eenheden voor afstanden
De keuze van eenheden van afstanden is uitgebreid, met nieuwe opties inclusief kilometers, yards en miles. gebruiken van deze eenheden voorkomt de noodzaak tot het handmatig converteren van afstanden (bijv. van voet naar mijlen).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Wijzigingen aan expressies
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Mogelijkheid: Statistieken voor tekst- en datumvelden
Het dock voor statistische overzichten kan nu  doorlopende statistieken voor teken- en datumvelden berekenen.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Straal van boogpunt weergeven in gereedschap Info
Indien u klikt op een gebogen lijn met behulp van het gereedschap Info, zal QGIS nu de straal in het gereedschap Info weergeven.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Marco Hugentobler
### Mogelijkheid: Doorlopende ondersteuning voor expressies
QGIS 2.16 voegt ondersteuning voor verscheidene types doorlopende berekeningen toe aan het programma voor expressies. Deze omvatten:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

In alle gevallen worden de berekeningen gecached binnen de context van de expressie, zodat zij slechts eenmaal behoeven te worden berekend voor elke set van evaluaties voor expressies.

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Plug-in fTools is vervangen door algoritmen voor Processing
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

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

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Ondersteuning voor het scrhijven van tabellen zonder geometrie
Het algoritme OutputVector ondersteunt nu het schrijven van tabellen zonder geometrie.

Momenteel was dit alleen toegepast voor het algoritme Refactor Fields maar kon eenvoudig worden uitgebreid naar andere op attributen gebaseerde algortimen.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Mogelijkheid: Aanvullende algoritmen voor GRASS in Processing
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

Sommige testen voor eenheden (meestal voor algoritmen voor rasters en afbeeldingen) zijn ook voor sommige algoritmen opgenomen, wat het onderkennen van problemen gemakkelijker maakt om af te handelen en te verwerken.

Onthoud dat op dit moment algoritmen van Processing  voor GRASS7 alleen Shapefile vectorlagen en rasters van GeoTiff gebruiken en produceren. Er is ook een beperking voor enkele algoritmen voor rasters van GRASS7 (alle algoritmen die kleurentabellen kunnen bewerken) die rasterlagen naar tijdelijke mappen dupliceren. Afhankelijk van de grootte van uw bronrasters, zult u waarschijnlijk ruimte op de schijf nodig hebben om ze te verwerken.

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Gegevensproviders
### Mogelijkheid: Gegevenssets van OGR worden standaard geopend in modus Alleen-lezen
Maakt gelijktijdig bewerken van Shapefiles en Tab-bestanden in zowel QGIS als MapInfo mogelijk.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mogelijkheid: Verbeterde afhandeling van Postgres velden type DOMAIN
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Maak modus readOnly van vectorlagen te configureren in project
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
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

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Stijlen opslaan in databases van MS SQL en Oracle
Deze mogelijkheid werd ontwikkeld door Jürgen Fischer en Christian Frugard
### Mogelijkheid: Velden hernoemen in lagen
In QGIS 2.16 kunt u nu velden henroemen in Postgres, Oracle, OGR en geheugenlagen door te dubbelklikken op de veldnaam in het venster van de Laageigenschappen.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Basisondersteuning voor Oracle Workspace Manager
Ondersteuning is toegevoegd voor Oracle Workspace Manager bij het gebruiken van de Oracle Provider.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
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
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- Ondersteuning voor aanvullende/gemixte typen geometrie (CurvePolygon, CompoundCurve)
- Grotere tolerantie voor niet-conformerende servers voor WFS

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
De gebruikte expressie om standaard waarden voor een veld in de database van Postgres worden momenteel afgedrukt op het forumlier van het object.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
Het grote voordeel van deze verbetering is dat men nu direct records van gerelateerde tabellen kan maken en koppelen zonder eerst de gegevens te moeten opslaan, omdat de primaire sleutel al aanwezig is vóórdat het object wordt opgeslagen.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## QGIS Server
### Mogelijkheid: Ondersteuning voor met rood onderstrepen in GetMap en GetPrint
Dit werd mogelijk gemaakt door Kanton Solothurn

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Standaard transformatie van datum voor server
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
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

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Mogelijkheid: Globe: Objecten vervormen
Vervormen van objecten naar de 3e dimensie mogelijk maken.

Ofwel door een vaste waarde of door een attribuut of expressie.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: API: Pagina's toevoegen aan de eigenschappen van vectorlagen
Toevoegen van aanvullende pagina's in het dialoogvenster Eigenschappen van vectorlagen mogelijk maken.

Dit maakt het mogelijk de configuratie voor aan lagen gerelateerde opties, die worden verschaft door een plug-in, direct daar te plaatsen waar zij horen voor een betere ervaring voor de gebruiker.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Globe: Ondersteuning voor vector
Behoud vectorgegevens bij het weergeven van lagen op globe.

Dit werd mogelijk gemaakt door Master Thesis UZH

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Mogelijkheid: Globe: Verticaal overdrijven voor DTM
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## Programmeerbaarheid
### Mogelijkheid: Ingebedde widgets in lagenboom
Dit maakt het mogelijk definities van widgets in te bedden in de lagenboom voor individuele lagen in het dialoogvenster Laageigenschappen (in de nieuwe tab Legenda). Het idee erachter is om een manier te hebben om snel toegang te krijgen tot enkele acties die vaak op een laag worden gebruikt.

De implementatie bevat widgets met transparantie, in de toekomst zouden er meer standaard widgets kunnen komen, bijv. om een filter in te stellen, selecteren, stijl of andere dingen. De API staat plug-ins toe om hun eigen widgets te registreren, die nuttig kunnen zijn voor verscheidene domeinspecifieke plug-ins om aangepaste widgets toe te wijzen aan lagen die zij beheren.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
### Mogelijkheid: Plug-ins kunnen pagina's toevoegen aan de eigenschappen van vectorlagen
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Mogelijkheid: Nieuwe klassen voor PyQGIS in 2.16
### Nieuwe bronklassen
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) -an abstract base class for composer items which provides generic methods for nodes based shapes such as polygons or polylines
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - a composer item for polygon shapes
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) -a composer item for polyline shapes
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.htmll) -a composer undo command class for grouping / ungrouping composer items
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) -WKB reader which simplifies geometries on the fly
- [QgsAction](https://qgis.org/api/classQgsAction.html) - a utility class that encapsulates an action based on vector attributes
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - stores and manages actions associated with a layer
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) -a utility class for calculating aggregates for a field (or expression) over the features from a vector layer
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) -a container for configuration of the attribute table for a vector layer
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - a representation of the interval between two datetime values
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handles exporting QgsFeature features to GeoJSON features
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - helper utilities for working with JSON and GeoJSON conversions
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) -simple profiler for timing code paths during execution
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - utility class for parsing SQL statements
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of strings
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - a renderer for generating live hillshade models
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) -line symbol layer used for representing lines as arrows
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) -a renderer which draws no symbols for features by default, but allows for labeling and diagrams for the layer
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) -abstract base class for simple marker symbol layers. Handles creation of the symbol shapes but leaves the actual drawing of the symbols to subclasses.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) -filled marker symbol layer, consisting of a shape which is rendered using a QgsFillSymbolV2

### Nieuwe klassen voor GUI
#### Opnieuw te gebruiken widgets:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- kleurenwiel, kleurvlakken, en een kleurenvoorbeeld
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subclass with more fine-grained control over how the widget is closed or opened
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - an event filter for watching for focus events on a parent object
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) -an interactive editor for previewing a gradient color ramp and modifying the position of color stops along the gradient
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) -a panel widget that can be shown in the map style dock
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) -factory class for creating custom map layer property pages
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - base class for any widget that can be shown as a inline panel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) -inline panel wrapper widget for existing widgets which can\'t have the inheritance tree changed, e.g dialogs
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) -a stack widget to manage panels in the interface
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) -a class that contains a list of QActions and QShortcuts that have been registered and allows their shortcuts to be changed
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) -this can be used like a regular QTableWidgetItem with the difference that a specific role can be set to sort
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) -renderer widget for configuring the hill shade renderer
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) -widget for controlling a raster layer\'s transparency and related options
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) -renderer widget for configuring arrow symbol layers

#### Opnieuw te gebruiken dialoogvensters:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Belangrijke reparaties
### Mogelijkheid: Programma van QGIS voor oplossen van problemen tegen betaling
We hebben nogmaals een ronde uitgevoerd van het oplossen van problemen tegen betaling (met dank aan onze sponsors en donoren!). Hier volgt ene overzicht van het werk van de ontwikkelaars die hebben deelgenomen:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- Opgelost: Gebroken projectieve transformatie in Georeferencer (#14551 - severe)
- Opgelost: Mislukken van selecteren van objecten op radius (#14748 - severe)
- Opgelost:  Onjuiste berekening van gebied voor polygoon (#14675 - severe, although very unlikely to occur. Unit tests added to cover this edge case)
- Opgelost: Lay-out widget dock (#15011 - severe)
- Opgelost:  crash in symboollaag pijl (unreported)
- Opgelost:  crash bij maken van ongeldige join (unreported)
- Opgelost:  SVG's met parameters niet weergegeven voor pijlitems van Printvormgeving (#14997 - high)
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Altijd vergelijking voor tekenreeksen gebruiken in expressies voor velden tekenreeks (#13204 - high)
- Opgelost:  home dir wordt toegevoegd als standaard pad voor SVG en sjabloon (#14662, #14652, #14883 - high)
- Opgelost: crash bij gebruiken van geïnverteerde polygonen met renderer Heatmap (#14968 - high)
- Waarden van rastersymbologie opslaan met volledige precisie (#14950 - normal)
- Acties worden niet ingeschakeld bij het laden van een laag met standaard stijl (#13910 - normal)
- Remove \"attribute table\" text from dialog title (#14959 - normal)
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
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- Ontbrekende proxies toevoegen voor gedrag bij kiezen in Legenda voor subrenderers voor geïnverteerde polygoon en renderers plaatsing (unreported)
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- Type WKB weergeven inmetadata van vectorlaag (unreported)
- Ontbrekende tekenreksen voor capabilities toevoegen aan metadata van laag (unreported)
- Opgelost: debug ruis bij gebruiken van 25D geometrielagen (unreported)
- Opgelost:  sommige widgets van de statusbalk konden niet worden verborgen via aanpassingen (unreported)
- Stijlwidget live maken van toepassen van onthouden van instellingen (unreported)
- Don\'t show constraint messages when form is in search mode (unreported)
- Schuifbalken weergeven voor attributenformulier als identificatieresultaten (unreported)
- Knop Toepassen van Stijldock altijd ingeschakeld maken (unreported)
- Opgelost: enkele ontbrekende automatische bijwerkingen van Stijldock (unreported)

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Hier zijn de tickets die hij heeft behandeld gedurende de hem toegewezen tijd voor het oplossen van problemen voor QGIS 2.16.

**Severe/High:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normal**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Andere:**
- <https://issues.qgis.org/issues/14981>: Import of Shapefile to Geopackage-Database in DB-Manager fails (analysis)
- <https://issues.qgis.org/issues/15011>: Browser panel is unusable (bisection & analysis)
- <https://issues.qgis.org/issues/14909>: regression: QGIS crashes when closing docked attribute table (analysis)
- <https://issues.qgis.org/issues/13353>: QGIS and gdal 2.0.0 (closed: no further action needed)
- <https://issues.qgis.org/issues/15053>: WMS with EPSG:31255 is shifted (datum=hermannskogel) (analysis. probably outdated proj.4 version)

### Sandro Santilli
- <http://hub.qgis.org/issues/14262>: Overflow on primary key with negative values; cannot save edits
- <http://hub.qgis.org/issues/12228>: Deadlock from parallel rendering
- <http://hub.qgis.org/issues/11371>: Map Composer: group + move + ungroup + undo = crash
- <http://hub.qgis.org/issues/14976>: Repository files modified by \"make check\"
- <http://hub.qgis.org/issues/13635>: Different handling of invalid geometries between LTR and master version
- <http://hub.qgis.org/issues/13952>: QGIS node tool causes snapping another feature randomly

### Martin Dobias
- Digitizing: \"Simplify Feature\" should not open a dialog when no feature is clicked
- Digitizing: how to abort \"Simplify Feature\" or \"Rotate Feature\" tool is not that obvious
- Eén weg ontbreekt bij Vectorlaag toevoegen!
- Automatisch traceren mislukt bij Cirkelbogen in geometrieën
- WMS werkt niet in master a625eeb (2.15.0-80)
- Python fout in verwerken van vooraf gedefinieerde algoritmen
- GPS don\'t record geometry point, but only attribute values\...
- Stijldock: paneel transparantie (globale transparantie, transparante pixel, etc.) werkt niet voor renderer van schaduwen voor heuvels
- Stijldock: knop Terug & broodkruimels ontbreken als een op regels gebaseerde regel wordt bewerkt
- Opgelost:  Ongedaan maken/opnieuw voor op regels gebaseerde renderer/labels in dock voor opmaken
- Opgelost:  bijwerkingen van widget Ongedaan maken in paneel Opmaken
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Stabiliteit van QgsMapLayerRegistry verbeteren
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
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
  - Add button\" state in postgis source select dialog
- Ontbrekende kopbestanden toevoegen
- Crash bij afsluiten
- Netwerk map voor cache
- Objectformulier verborgen achter hoofdvenster op Windows
- Offline bewerken: Respecteer relatieve paden
- Offline bewerken: gewijzigde attributen komen in het verkeerde object terecht
- Offline editing: Don\'t crash with raster layers
- Relatieformulier groeit oneindig
- Opgelost:  crash bij laden van stijl in laageigenschappen
- Opgelost:  crash bij sluiten van vastgezette attributentabel
- Opgelost: standaard foutief geconfigureerd pad voor GPSBabel
- Juiste aantal objecten weergeven bij regel die geometrie vereist
- Opgelost:  crash bij gebruiken van renderer 2.5D met niet compatibele laag

{{<content-end >}}
