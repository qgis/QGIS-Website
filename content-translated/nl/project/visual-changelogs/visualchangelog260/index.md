---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.6{#changelog26 }
Datum uitgave 31-10-2014

Log met wijzigingen voor de volgende uitgave van QGIS 2.6.0. We hebben vele nieuwe mogelijkheden, aanpassingen en verbeteringen toegevoegd om de meest populaire gratis desktop GIS nog nuttiger en voller met mogelijkheden te maken.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- ZILVEREN sponsor: [Sourcepole AG, Zwitserland](http://www.sourcepole.com/)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- BRONZEN sponsor: [Lutra Consulting, VK](http://www.lutraconsulting.co.uk/)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de
- BRONZEN sponsor: [www.openrunner.com, Frankrijk](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: bestandsnaam van project in eigenschappen
U kunt nu het volledige pad en de bestandsnaam voor een project van QGIS zien in het dialoogvenster Eigenschappen.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Mogelijkheid: Verwijderen van laatste punt tijdens meten met toetsen Del/Backspace
Als u nu gebieden en afstanden meet kunt u ongewenste punten vanuit uw meetlijn verwijderen met behulp van de toetsen Delete of Backspace.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Mogelijkheid: gerelateerd object in het kaartvenster selecteren vanuit het widget relatieverwijzing
### Mogelijkheid: Wijzig-hulpmiddelen
We hebben een aantal verbeteringen gemaakt aan de Wijzig-hulpmiddelen:
- nieuw Wijzig-hulpmiddel voor datum/tijd in staat om Null-datums in te stellen
- filteren lijn wijzigen
- Juiste afhandeling van NULL-waarden voor Wijzig-hulpmiddelen
- Fotowidget behoudt waarde NULL
- Webwidget behoudt waarde NULL
- Attributentabel kan onderscheid maken tussen 0 en NULL
- Ondersteuning voor achtervoegsel toegevoegd aan widget Bereik

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Mogelijkheid: Gebruik optioneel slechts een subset van velden van de samengevoegde laag
U kunt nu slechts een subset gebruiken van gerelateerde velden bij het maken van een vectorjoin.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Mogelijkheid: Expressieveld (virtuele velden)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Mogelijkheid: Acties kunnen nu een geassocieerd pictogram hebben
Bij het maken van een aangepaste actie voor een vectorlaag kunt u nu ook een pictogram definiëren dat moet worden gebruikt voor de actie.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Mogelijkheid: Aanvullende  typen en opties voor expressies
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Mogelijkheid: Klassen binnen renderers Gradueel en Categorieën kunnen worden geschakeld
U kunt er nu voor kiezen bepaalde klassen in de renderers Gradueel en Categorieën uit te schakelen, zonder ze echt te verwijderen.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Mogelijkheid: Verbeteringen voor legenda
De tweede fase van de vernieuwing van de legenda / inhoudsopgave is voltooid. Dit omvat:
- API schoongemaakt (voor ontwikkelaars)
- Zichtbaarheid van groepen van kaartlagen in de boom van lagen. Deze nieuwe knop op de werkbalk maakt het mogelijk snel te wisselen tussen groepen lagen die zichtbaar zouden moeten zijn.
- Mogelijkheid om groepen lagen te beheren vanaf de werkbalk voor de Legenda
- De nieuwe filteroptie voor de Legenda op de werkbalk Legenda zal items van de legenda verwijderen voor klassen die niet in het huidige weergavebereik staan. Dit is een fantastische verbetering omdat het er voor zorgt dat uw inhoud van de kaartlegenda geen items bevat die momenteel niet in de kaartweergave staan. Het is beschikbaar in de legenda voor de hoofdkaart en in Printvormgeving en voor WMS-lagen.
- Legenda's van Op regel gebaseerde renderer kunnen nu worden weergegeven in een pseudo-boom

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Gegevensproviders
### Mogelijkheid: Verbeteringen voor DXF exporteren
- Weergave als boom en selectie van attributen voor toewijzen aan laag in het dialoogvenster
- Arcering en vulkleur kunnen worden ingesteld voor polygonen.
- Door het gebruik van MTEXT in plaats van TEXT bij het exporteren kunnen nu ook lettertype, -vorm en -dikte worden opgegeven.
- support for RGB colors when there\'s no exact color match
- De ondersteunde versie van DXF indeling is verhoogd naar AutoCAD 2000 DXF (R15) in plaats van R12.
- R18 testmethoden verwijderen

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Printvormgeving
### Mogelijkheid: Beheer over verbergen van items van Printvormgeving voor afdrukken/exporteren
We hebben een keuzevak en een data-gedefinieerde knop toegevoegd voor het beheren of een item moet worden uitgesloten van exporteren/afdrukken vanuit Printvormgeving. Als het item niet is geselecteerd zal het alleen gedurende ontwerptijd zichtbaar zijn.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Mogelijkheid: Beheer over afdrukken van pagina's voor lege frames in Printvormgeving
Voor tabel- of HTMLframes beheert een keuzevak nu of de betreffende pagina zou moeten worden geëxporteerd als het frame leeg is.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Mogelijkheid: Item boompaneel
Het item boompaneel in Printvormgeving maakt het mogelijk items te selecteren, items te verbergen/weer te geven, de status vastzetten van items te schakelen en dubbelklikken voor bewerken van het item-ID. U kunt ook slepen en neerzetten om items in een andere volgorde te zeten.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Mogelijkheid: Meer controle over uiterlijk van items pijl/lijn in Printvormgeving
- Lijnen kunnen worden opgemakt met behulp van het dialoogvenster Lijnsymboolstijl
- Vulling voor kleur rand pijlpunt en randen kunnen door de gebruiker worden gedefinieerd
- Breedte voor rand pijlpunt kan door de gebruiker worden gedefinieerd

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Mogelijkheid: Data-gedefinieerd beheer van items voor Printvormgeving
Veel eigenschappen van items in Printvormgeving kunnen nu worden beheerd met behulp van het binden van gegevens. Deze omvatten:
- Transparantie en mengmodus.
- Rotatie item.
- Schaal van de kaart, bereiken en rotatie.
- Marge van Atlas-object.
- Itemgrootte en positie.
- Paginagrootte, oriëntatie en aantal pagina's.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Mogelijkheid: Afbeeldingen van Printvormgeving kunnen worden gespecificeerd als URL's op afstand
Items van afbeeldingen in printvormgeving ondersteunen nu URL's op afstand als bron voor een afbeelding. Deze bron mag ook data-gedefinieerd zijn.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Mogelijkheid: Verbeteringen Tabel van Printvormgeving
- U kunt nu kleuren voor lettertypen van tabelkop en inhoud instellen.
- Tabellen kunnen nu worden gesplitst over meerdere frames, wat het mogelijk maakt hun inhoud te verdelen over kolommen of over verschillende pagina's.
- Optie toegevoegd voor het weergeven van koppen in eerste frame, alle frames, of geen frames.
- Handmatig beheren van kolombreedten toestaan.
- Nieuwe opties voor tabelbron, inclusief huidig atlas-object en kind-objecten uit een relatie.
- Keuze voor gedrag van lege tabellen, inclusief het verbergen van de gehele tabel, lege cellen weergeven, of het weergeven van een ingesteld bericht in de tabeltekst.
- Een keuzevak toegevoegd om tabelobjecten te filteren tot die welke het huidige atlas-object kruisen.
- Keuzevak toegevoegd voor het verwijderen van duplicaat-rijen uit de tabel.

Onthoud dat tabellen in bestaande projecten niet automatisch worden bijgewerkt naar de nieuwe indeling van tabellen die deze mogelijkheden ondersteunen, en tabellen moeten worden ingelezen in een lay-out om de nieuwe instellingen te laten verschijnen.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Mogelijkheid: Verbeteringen van Printvormgeving
De Printvormgeving (gebruikt om af te drukken lay-outs voor kaarten voor te bereiden) heeft een aantal verbeteringen ondergaan in QGIS 2.6.
- U kunt de tweede vulkleur wijzigen voor schaalbalken
- Ingedrukt houden van Shift bij het tekenen van items lijn/pijl beperkt het tekenen tot horizontaal, verticaal of hoeken van 45 graden
- Ingedrukt houden van Shift tijdens tekenen van andere nieuwe items beperkt ze tot vierkanten, ingedrukt houden van Alt zorgt er voor dat het item vanuit het midden wordt getekend
- Klikken met rechts zet niet langer items vast/maakt ze los, dit wordt nu afgehandeld door het nieuwe paneel Items. Vastgezette items kunnen niet langer worden geselecteerd vanuit het venster van printvormgeving, wat interactie met items eronder mogelijk maakt.
- Ingedrukt houden van Alt bij het drukken op pijltjestoetsen resulteert in een verplaatsing van het item met 1px
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Mogelijkheid: Verbeterd snappen voor item
Drempels voor snappen worden nu ingesteld in pixels, wat het mogelijk maakt nauwkeuriger te verplaatsen en items van grootte te wijzigen indien ingezoomd op een lay-out. Items binnen een groep worden niet langer gebruikt voor automatisch snappen aan lijnen.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Mogelijkheid: Meerdere overzichtskaarten voor een kaartitem
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Mogelijkheid: Verbeteringen voor HTML-items
Er zijn een aantal nuttige nieuwe nieuwe opties voor het item HTML in Printvormgeving:
- Optie voor handmatige invoer van de bron voor de HTML
- QGIS-expressies binnen HTML-bron kunnen worden geëvalueerd, voorafgaande aan het renderen van de inhoud van de HTML
- Data-gedefinieerde URL voor HTML-bron
- Mogelijkheid voor het maken van een gebruiker-stylesheet om voorrang te hebben over stijlen van HTML

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Mogelijkheid: Verbeteringen van raster van Printvormgeving
- U kunt nu meerdere rasters met verschillende eigenschappen gebruiken.
- U kunt opnieuw geprojecteerde rasters en Lat/Long-rasters mixen.
- U kunt standaard QGIS symbologie rasterlijnen etc. gebruiken.
- Er is een nieuwe rasterstijl voor alleen frame/annotaties. Selecteren van deze stijl zorgt er voor dat alleen het frame en annotaties worden getekend, zonder rasterlijnen of andere markeringen op de kaart.
- er zijn nu opties voor het beheren van aan welke kant van een kaartitem het frame zal worden getekend.
- Er zijn nieuwe stijlen voor stippels voor frames, met opties voor stippels binnen, stippels buiten en zowel binnen als buiten.
- We hebben verbeteringen aangebracht aan raster-annotaties, inclusief mvele nieuwe indelingen voor annotaties.
- Raster-annotaties gebruiken de typografische juiste symbolen voor aanhalingsteken en dubbel aanhalingsteken voor raster-annotaties.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Processing
### Mogelijkheid: Online collectie van modellen en scripts
Modellen en scripts kunnen worden gedownload vanuit de online collectie en direct worden geïnstalleerd vanuit de interface van Processing. De collectie zal worden uitgebreid met nieuwe scripts en modellen die worden verschaft door gebruikers van Processing.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Mogelijkheid: Nieuwe implementatie Grafische modellen bouwen
Grafische modellen bouwen is opnieuw geschreven, en verschaft nu extra functionaliteit zoals het toestaan van geneste modellen zonder beperking voor diepte. Modellen worden nu opgeslagen als JSON-bestanden. Achterwaartse compatibiliteit is behouden, dus alle modellen kunnen nog steeds worden gebruikt. U kunt nu ook items slepen  en neerzetten vanuit de invoeren en algoritmen op de weergave van Grafische modellen bouwen.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programmeerbaarheid
### Mogelijkheid: API-wijzigingen voor widgets van QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Server
### Mogelijkheid: Verbeteringen voor het zoeken met verzoek GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Mogelijkheid: Een instelling voor precisie toegevoegd voor geometrie-attributen van GetFeatureInfo
## Symbologie
### Mogelijkheid: Betere keuze willekeurige kleur
We hebben het algoritme voor de willekeurig kleuren voor de renderer Classificatie verbeterd zodat de gegenereerde kleuren meer visueel van elkaar verschillen.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Mogelijkheid: Verbeteringen aan de gebruikersinterface voor Symbologie
- Waar mogelijk worden eigenschappen van de symboollaag behouden bij het wijzigen van het type symboollaag.
- Een knop bewerken toegevoegd voor shapeburst en kleurverlopen.
- Automatisch bijwerken van label en grenzen van naburige bereiken.
- Klassen worden automatisch geconverteerd van klassen Categorieën en Gradueel bij het overschakelen naar de Op regel gebaseerde renderer.
- Eenheden en aantal decimale plaatsen toegevoegd aan de labels voor de renderer Gradueel.
- Verbeterde reactie bij wijzigingen in kleurenbalk, geïnverteerde kleurenbalk, en andere opties in de GUI.
- Symbool behouden bij schakelen tussen Enkel, Gradueel, Categorieën, en andere renderers.
- Labelen verbeterd van de rekenmodus StdDev.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Gebruikersinterface
### Mogelijkheid: Codebewerker met accentueren van syntaxis
Voor scriptbewerkers van Python, expressiebouwer, venster Filteren, Printvormgeving HTML en bewerkers voor CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Mogelijkheid: Kleurpaletten
U kunt nu uw eigen aangepaste kleurpaletten definiëren om te gebruiken in QGIS.
- Aangepast gebruiker globaal kleurpalet (in dialoogvenster Opties).
- Kleurpalet per project (in dialoogvenster Projecteigenschappen).
- Kleuren worden weergegeven in menu's met kleurknoppen en een nieuw dialoogvenster Kleurkiezer.
- U kunt kleuren im-/exporteren naar een paletbestand GPL.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Mogelijkheid: Nieuw dialoogvenster Kleurkiezer
Er is een nieuw aangepast QGIS dialoogvenster Kleurkiezer. Mogelijkheden omvatten:
: - Schuifbalken voor helderheid, saturatie, waarde, rode, groene, blauwe kleurcomponenten.
  - Schuifbalk Alfa.
  - Optie om HTML-kleurcodes te kopiëren/plakken (in een variëteit aan indelingen).
  - Voorbeeld kleur voor/na, met voorbeeld Alfa.
  - Interactieve widget 2D kleurenbalk.
  - Widget Hue wiel/driehoek.
  - bewerkbare kleurpaletten, inclusief de mogelijkheid om nieuwe palletten te maken en im-/exporteren van kleuren naar een paletbestand GPL.
  - Live kleurensampler met de optie om over een ingestelde radius te samplen (afhankelijk van ondersteuning besturingssysteem).
  - Ondersteunt interactie met andere apps via slepen en neerzetten van kleuren (afhankelijk van ondersteuning besturingssysteem).
  - Optie om het dialoogvenster uit te schakelen en in plaats daarvan het eigen dialoogvenster voor de keuze te gebruiken.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Mogelijkheid: Gereedschap Eén object selecteren samengevoegd met Met rechthoek selecteren
We hebben het gereedschap Eén object selecteren samengevoegd met met het gereedschap met rechthoek selecteren. Als u één enkel object wilt selecteren, schakel dan het gereedschap met rechthoek selecteren in en klik één maal op een object (in plaats van een rechthoek te tekenen).

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Mogelijkheid: Gedrag Laag aan kaartvenster toevoegen
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Mogelijkheid: Grootte pictogram 48 en 64 toegevoegd
Voor hen die QGIS gebruiken op aanraak-apparaten (of als u gewoon grote hoekige pictogrammen leuk vindt), kunnen nu de pictogrammen instellen tot een grootte van 64 x 64 pixels.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Mogelijkheid: Nieuwe knoppen kleuren
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Mogelijkheid: Contextmenu voor Gereedschap objecten identificeren
Bij het gebruiken van het gereedschap Objecten identificeren kunt u nu ,met rechts klikken op het kaartvenster om het gereedschap Objecten identificeren te gebruiken in de modus Context. In het menu dat verschijnt kunt u definiëren welke typen objecten u wilt identificeren (allemaal als u dat wilt).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
