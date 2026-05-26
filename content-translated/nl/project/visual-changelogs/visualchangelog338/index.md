---
HasBanner: false
draft: false
releaseDate: 21-06-2024
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.38
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.38{#changelog338 }
![](images/projects/77e273e90ec2f1953a8c0b5b0097a235c85f2425.png)

Datum uitgave: 21-06-2024

Het project QGIS is er trots op de uitgave aan te kondigen van QGIS 3.38 Grenoble, een kenmerkende bijwerking bruisend van verbeteringen die zijn ontworpen om gebruikers goed uit te rusten op hun reis naar ruimtelijke ontdekkingen. Deze uitgave bevat verbeterde mogelijkheden voor het filteren van gegevens en nauwe integratie van filtercriteria tussen verschillende projectelementen, uitgebreid beheer biedend aan gebruikers om ze in staat te stellen hun processen voor het verkennen van hun gegevens te verfijnen.

Verscheidene verbeteringen worden verschaft voor hoogtebeheer, inclusief het nieuwe hoogtebeheer, alsook de mogelijkheid om expliciet een verticaal CRS voor uw project te declareren. Eerdere uitgaven verwijderden actief informatie over verticaal CRS om technische redenen, zoals vermeld in [QGIS voorstel voor verbeteringen 267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267). Dit vitale aspect van ruimtelijk gegevensbeheer is nu echter opnieuw geïntroduceerd in het project QGIS.

Naast deze bronverbeteringen biedt QGIS 3.38 een rijkdom aan verbeteringen en kwaliteitsverbeteringen, inclusief verscheidene verbeteringen voor gebruik, ondersteuning voor CMYK kleuren, verbeterde zoekfunctionaliteit en nieuwe mogelijkheden voor gegevenstypen, zoals DXF, Mazen en SensorThings.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=oktjj7xBZ54).

[![](https://img.youtube.com/vi/oktjj7xBZ54/0.jpg)](https://www.youtube.com/watch?v=oktjj7xBZ54)

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een heel groot bedankt voor al onze sponsoren!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.
## Tijdbeheer
### Mogelijkheid: Nieuwe modus Tijdbeheer: pixelwaarde als datetime voor Tijdbeheer
Een nieuwe modus voor Tijdbeheer voor rasterlagen wordt verschaft die elke pixel als een waarde datetime interpreteert.

Bij het renderen van een rasterlaag, terwijl die modus wordt gebruikt, zullen pixels worden verborgen als ze buiten de tijdsperiode vallen die is verbonden met de rendercontext.

Voorbeelden van enkele interessante gebruiksgevallen voor Tijdbeheer omvatten:
- weergeven van landgebruik, zoals verlies van bos
- weergeven van overstroming in de tijd
- weergeven van verplaatsingskosten (bijv. GRASS' `r.walk`)

![](images/entries/e9349bf2255cb4e027d1f91460eb4fea9710c4c1.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Kaartgereedschap
### Mogelijkheid: Hoogtebeheer toegevoegd voor filteren verticale gegevens in 2D-kaarten
Een nieuw Hoogtebeheer verschaft gebruikers de mogelijkheid om verticale gegevens in 2D-kaarten te filteren. Wat de equivalente ervaring verschaft van tijdbeheer voor het afromen van hoogten in het bereik Z van gegevens in lijn met [QEP 201](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/201).

Deze mogelijkheid is toegankelijk via een nieuw submenu "Gegevens filteren" in het menu Beeld, naast nieuwe menu-items voor Tijdbeheer.

Het beheer geeft een schuifbalk weer voor het bereik aan de linkerkant van de kaart. Er is een actie voor het configureren van de instellingen van het hoogtebereik voor het project dat het beschikbare bereik in de widget bepaalt.

![](images/entries/09e8196d117fbd9dc521e59ed5e206ced16e14ab.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Z-bereik ondersteunt items voor instellen van kaartvenster / kaart
Filteren van hoogte wordt nu in kaartvensters ondersteund

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Optie toegevoegd om een vaste breedte voor hoogte voor Hoogtebeheer in te stellen
Een nieuwe optie wordt gegeven in het configuratiemenu van Hoogtebeheer, wat het mogelijk maakt een vaste breedte in te stellen voor het hoogtedeel.

Dat kan worden gebruikt als een specifieke breedte voor het hoogtebereik gewenst is, of als het bereik altijd breedte nul zou moeten hebben.

![](images/entries/89ac87d5ec596dbd04f45be17dac9532d4a120b4.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Zoekoptie toegevoegd voor zoeken dat is gebaseerd op reguliere expressies
Een nieuwe optionele modus voor regex wordt weergegeven voor gevorderde zoekopties, zoals geïmplementeerd in de bijgewerkte zoekfunctionaliteit voor de codebewerker.

![](images/entries/2ab6a0a0e6837a51cf7e50a7104359fc063ced7e.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Data-bepaalde 'override': middelklik gebruiken om het dialoogvenster Expressiebouwer te openen
## Beschrijving
De middelklik op het pictogram Data-bepaalde 'override' opent het dialoogvenster Expressiebouwer, als een handige sneltoets voor met rechts klikken op het item in het menu Bewerken.

![](images/entries/f44815b85558f76d7a6e6791370f683def53d51d.gif)

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Symbologie
### Mogelijkheid: Nieuwe renderer Enkele kleur voor rasters
Een nieuwe symbologie Enkele kleur is toegevoegd voor rasterlagen. Dit maakt het mogelijk om op een super eenvoudige en vriendelijke manier een raster te renderen in een enkele kleur.

![](images/entries/73049b50b1c9d2e2c0c22fbfdd00db58d4ffc5c0.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Ondersteuning toegevoegd voor renderen van windvanen voor vectorgegevenssets van mazen
Windvanen zijn een veelvoorkomende manier om windsterkte en -richting aan te geven op kaarten en het nieuwe type symbologie Windvanen maakt het voor gebruikers gemakkelijk om deze krachtige stijl voor visualiseren te gebruiken voor hun vectorgegevenssets met mazen.

Windvanen coderen de windsnelheid in knopen (nautische mijlen per uur). Dus gebruikers moeten expliciet de relevante gegevenseenheden selecteren voor hun gegevens om juist te worden weergegeven, of een aangepaste vermenigvuldigingsfactor gebruiken om de waarden naar knopen te converteren.

![](images/entries/1f5b158227f114192f411835adfb8dd40d0a8900.webp)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
## Labelen
### Mogelijkheid: Instelling Maximale afstand toegevoegd voor puntlabels
Een nieuwe optionele instelling is toegevoegd voor de modi voor plaatsing "Rondom punt" en "Cartografisch" om de maximale afstand van de labels vanaf het object te specificeren. Het wordt samen gebruikt met de bestaande instelling voor de afstand om een bereik met afstanden te definiëren waarop labels mogen worden geplaatst vanaf hun corresponderende objecten punt.

Dit voegt meer flexibiliteit toe aan de plaatsing voor deze lagen, wat het ultiem mogelijk maakt meer labels te plaatsen op drukke kaarten.

Wanneer de laag is ingesteld op de modus "Rondom punt", hebben labelkandidaten die dichter bij het punt liggen altijd voorrang op die welke verder weg liggen.

Als de laag is ingesteld op de modus "Cartografisch", is het standaardgedrag om ook de dichterbij gelegen labels te prioriteren. Een nieuw combinatievak maakt het voor gebruikers mogelijk de prioriteit te beheren, met een optie voor een ordening op voorkeur voor positie. Als die optie is ingesteld, hebben kandidaten op de corresponderende posities (bijv. linksboven) de voorkeur, ongeacht hoe ver ze van het punt af liggen, waarbij het labelen alleen terugvalt op alternatieve posities als er geen labels kunnen worden geplaatst tot aan de maximale labelafstand.

![](images/entries/cf8223309d9bf77cf5634a7166706e3b9841bda9.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie voor plaatsing 'Boven punt' toegevoegd voor de modus voor labelen Cartografisch
Een nieuwe optie voor het plaatsen van labels is toegevoegd voor "O" = "Boven punt" als de modus voor plaatsing is ingesteld op de modus "Cartografisch".

Wanneer de prioriteiten voor data-bepaalde plaatsing voor een object deze nieuwe optie 'O' bevatten, kan een label direct boven het corresponderende punt worden geplaatst.

![](images/entries/25c00222d0e6f17efda6784e8ce9a577275618a8.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Renderen
### Mogelijkheid: Data-bepaald beheer toegevoegd voor straal van heatmap en maximale waarde
Dit stelt gebruikers in staat de straal en het maximum in te stellen als een waarde die zin heeft voor de huidige situatie, bijv. de huidige schaal voor de kaart, huidige object van de afdrukatlas, of huidige tijdsperiode.

Dit bevat aanvullend de basiswijzigingen voor data-bepaalde eigenschappen op het niveau van de renderer voor het object, wat nuttig zou kunnen zijn voor het uitbreiden van andere klassen voor renderen van vector (bijv. punt cluster/ verplaatsing).

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Afdruklay-outs
### Mogelijkheid: Ondersteuning voor teken Tab voor QgsTextFormat en QgsTextRenderer
Een [regressie](https://github.com/qgis/QGIS/issues/56981) resulteerde erin dat QGIS tekens Tab stripte en de mogelijkheid beperkte om tekens Tab te kunnen gebruiken in bepaalde contexten, zoals het uitvoeren van uitlijnen van tekens in legenda's.

![](images/entries/b8934ab8ad907adbc628a9e168fcbd9c88af83ee.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Rasters voor printomgeving kopiëren
Een knop om het geselecteerde raster te kopiëren (dupliceren) is toegevoegd aan Printomgeving.

Dat vereenvoudigt het proces voor het maken van nieuwe rasters die slechts een paar verschillen hebben van een bestaand raster of een bestaand raster als sjabloon gebruiken.

![](images/entries/bad634a873669247fe13d334d080b0b1cb6e1363.webp)

Dit werd mogelijk gemaakt door [NaturalGIS](https://naturalgis.pt/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Optie voor filteren bereik Z voor lay-outkaarten
Een nieuwe instelling voor het kaartitem lay-out stelt gebruikers in staat een specifieke hoogte/Z-bereik in te stellen voor het filteren van 2D-lay-outkaarten, soortgelijk aan de bestaande instelling voor filters voor Tijdbeheer.

Indien ingesteld, zullen kaartlagen, die filteren van 2D-Z-bereik ondersteunen, worden gefilterd om alleen inhoud binnen dit bereik te laten zien.

Aanvullend kan het bereik voor filteren van Z data-bepaald worden, wat verschillende bereiken Z mogelijk maakt voor atlas of objecten rapporteren die zijn gebaseerd op data-bepaalde eigenschappen van het object.

![](images/entries/c7f2cc35cfaf4a101ee2be654688142fb83ac055.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Knoppen toegevoegd om de boom van de lay-outlegenda in- of uit te klappen
Nieuwe knoppen zijn toegevoegd, zodat gebruikers gemakkelijk de bomen van legenda's binnen lay-outs van Printomgeving kunnen in- of uitklappen.

![](images/entries/e3ada0021b7137123133b645093168bd483530a7.webp)

Deze mogelijkheid werd ontwikkeld door [Harrissou Sant-anna](https://github.com/DelazJ)
## Expressies
### Mogelijkheid: Variabelen @map\_z\_range reflecteren de waarden van het bereik Z van de kaart
Nieuwe variabelen voor het ophalen van de huidige waarden `@map_z_range_lower` en `@map_z_range_upper` zijn toegevoegd aan de QGIS Expressies die de waarde voor het bereik Z in het kaartvenster weergeven.

![](images/entries/ab7a53d114337665cded7fd178658144222d1962.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Gegevensbeheer
### Mogelijkheid: Beleid voor dupliceren voor velden bij het dupliceren van objecten
Bij het dupliceren van een object (en de kinderen ervan) zal nieuw beleid beschikbaar zijn voor objecten QgsField.

Dit gedrag kan worden geconfigureerd met de interface voor beleid in de definitie van het objectformulier in de laag. Echter, het actief gedefinieerde beleid zal worden geïmplementeerd op alle objecten die worden gedupliceerd met algemene kaartgereedschappen. Iedere keer als een object wordt gekopieerd (bijv. "verplaatsen en kopiëren" in digitaliseren, of kopiëren en plakken vanuit het kaartvenster of attributentabel).

Er zijn momenteel drie opties voor soorten beleid beschikbaar:
- **Waarde dupliceren** (standaardmodus): Maakt een kopie van de attribuutwaarde uit het bronobject.
- **Standaard waarde**: Niet te verwarren met de standaardmodus, de instelling Standaard waarde herstelt nieuwe objecten naar de standaard voor het objectformulier, zoals gedefinieerd in de formulierontwerper (gewoonlijk een QGIS Expressie).
- **Waarde verwijderen**: Heft instelling op en verwijdert de veldwaarde (NULL).

![](images/entries/76e7f27309a07b9bb7e61a074efa81c1340bfbed.webp)

Deze mogelijkheid werd ontwikkeld door [signedav](https://github.com/signedav)
### Mogelijkheid: Modus "Vaste tijdsperiode per band" voor Tijdbeheer voor rasters
Deze modus kan worden gebruikt als elke band in de rasterlaag is geassocieerd met een vaste tijdsperiode, bijv. bestanden NetCDF.

De gebruiker kan ofwel handmatig een tabel vullen met begin-/einddatums voor elke band in het raster of de tabel opbouwen met QGIS-expressies die waarden datetime teruggeven

![](images/entries/7075b0b60ec0f0d4e5901e4d94452fa187b9a787.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Introduceren van een vast hoogtebereik voor rasterlagen
Een nieuwe optie is geïntroduceerd om te specificeren hoe hoogte moet worden geassocieerd met rasterlagen. Het maakt het mogelijk een vast hoogtebereik in te stellen voor de laag en kan worden gebruikt als de laag een enkele vaste hoogte heeft of een bereik (schijf) met hoogtewaarden.

Gebruikers kunnen het onderste en bovenste bereik voor de hoogte voor de laag instellen, en of de grenzen voor de onderste en bovenste hoogte inclusief of exclusief zijn.

Indien ingeschakeld zal de laag alleen zichtbaar zijn in 2D-kaarten waarin filteren van hoogte actief is als het bereik van de laag is opgenomen in het bereik Z van de kaart.

![](images/entries/64a2386154517472b58a41f2551b0d8d30951770.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Introduceren van een vast hoogtebereik voor lagen met mazen
Een nieuwe modus voor een bereik met een vaste hoogte is beschikbaar voor lagen met mazen, equivalent aan de modus voor een bereik met vaste hoogte voor rasterlagen. Het verschaft een nieuwe optie om te specificeren hoe hoogte moet worden geassocieerd voor lagen met mazen. Het maakt het mogelijk een vast hoogtebereik in te stellen voor de laag en kan worden gebruikt als de laag een enkele vaste hoogte heeft of een bereik (schijf) met hoogtewaarden.

Gebruikers kunnen het onderste en bovenste bereik voor de hoogte voor de laag instellen, en of de grenzen voor de onderste en bovenste hoogte inclusief of exclusief zijn.

Indien ingeschakeld zal de laag alleen zichtbaar zijn in 2D-kaarten waarin filteren van hoogte actief is als het bereik van de laag is opgenomen in het bereik Z van de kaart.

![](images/entries/88a53a76a505418c2ed776f70fb56cd5bd85031b.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Modus "Vast hoogtebereik per band" voor rasters
In deze nieuwe modus kan elke band in het raster een vast bereik voor de hoogte aan zich hebben verbonden.

Dit is ontworpen door databronnen die aan hoogte gerelateerde gegevens weergeven in banden, bijv. een raster NetCDF met temperatuurgegevens op verschillende dieptes in de oceaan.

Bij het renderen zal de meest HOOGSTE overeenkomende band worden geselecteerd en gebruikt voor de gegevens van de laag. De configuratie voor de renderer zal ongewijzigd worden behouden, ongeacht de overeenkomende band. Gebruikers moeten dus de opties voor renderen voor de laag configureren met een representatief bereik dat de gegevens uit alle banden bedekt.

De configuratie voor de laag wordt weergegeven als een door de gebruiker te bewerken tabel met rasterbanden met onder- en bovenwaarden. Gebruikers kunnen ofwel handmatig de onder- en bovenwaarden vullen of een QGIS-expressie gebruiken om alle bandwaarden automatisch te vullen.

Definities voor waarden die zijn gebaseerd op expressies zullen gebruikers in staat stellen expressies te ontwerpen die capabel genoeg zijn om nuttige informatie uit het bestand met metadata uit te nemen. Welke anders misschien moeilijk te bewerken zou zijn, zoals de namen van de banden zelf, bijv. "Band 001: depth=-5500 (meters)".

![](images/entries/9622032fd646ac79cc63e48ed30eca1841c9993b.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Modus "Dynamisch hoogtebereik per band" voor rasters
Een nieuwe dynamische modus voor het configureren van de rasterhoogte wordt verschaft, waarin het hoogtebereik voor rasterbanden wordt berekend met een paar van QGIS-expressies voor de grenzen van de onder- en bovenwaarde van het hoogtebereik voor de laag.

In deze modus kunnen de gebruikers een QGIS-expressie specificeren voor de onder- en bovenwaarde die overeenkomt met de rasterbanden. Met variabelen zoals @band, @band\_name en @band\_description, naast de standaardwaarden, globalen en projectvariabelen voor QGIS-expressie.

Bijvoorbeeld:

    @band * 100
    
Dit kan worden gebruikt wanneer elke band een 100 m verticale schijf van gegevens weergeeft.

De expressie zal indien nodig worden geëvalueerd om het feitelijke hoogtebereik te bepalen voor elke band.

Dit verschilt van de modus "Vast hoogtebereik per band", die van gebruikers eist dat ze handmatig afzonderlijk een hoogte invoeren voor elke band, en die waarden worden dan behandeld als constanten. Die modus werkt het beste voor rasters zonder regelmatige stappen in de waarden voor de  hoogten in de band. Terwijl de dynamische modus meer geschikt is voor gegevens die regelmatige stappen voor hoogten in elke band bevatten.

![](images/entries/d40450a1bcc9d3d2d3c5565681228b1d52256b69.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Een modus voor vast hoogtebereik per groep gegevensset voor lagen met mazen toegevoegd
Aanvullende functionaliteit om een vast hoogtebereik in te stellen per groep gegevensset voor lagen met mazen bootst de nieuwe modus "Vast hoogtebereik per band" voor rasterlagen na, maar staat toe dat een groep hoogtebereik per-gegevens wordt ingesteld.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie toegevoegd om alle lijnen te exporteren met minimale breedte bij exporteren naar dxf
Een optionele instelling is toegevoegd voor het exporteren naar dxf die toestaat dat gebruikers alle lijnen wegschrijven met een minimale breedte van 0 (haarlijn).

Lijnen binnen bestanden van DXF die een breedte nul hebben, blijven normaal gesproken minimaal in de CAD, ongeacht het zoomniveau. Deze functionaliteit kan dus behoorlijk nuttig zijn voor compatibiliteit met geëxporteerde DXF's die met andere software zijn bewerkt, speciaal in gebruiksgevallen waar de hoge dichtheid van gegevens een zorg is.

![](images/entries/1c7a18b41d42049e6c6ab7538d74d69406b837bb.webp)

Dit werd mogelijk gemaakt door [Stadtwerke München](http://www.swm.de/)

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Mogelijkheid: Sta gebruikers toe de laagnamen, die zijn geëxporteerd naar DXF, te overschrijven
Het is nu mogelijk de uitvoernaam van geëxporteerde individuele lagen te overschrijven. Door nieuwe opties voor configuratie die zijn toegevoegd aan de dialoogvensters voor exporteren naar DXF voor projectexport, laagexport en het algoritme van Processing Lagen naar DXF exporteren.

![](images/entries/83f65d9f8afbd45ecc0fa6b2804a7981f6192e7e.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid DXF-blokken maken voor puntsymbolen met data-bepaalde eigenschappen
Aanvullende verbeteringen zijn toegevoegd aan de mogelijkheid van het gebruiken van verwijzingen binnen een DXF, speciaal voor complexe data-bepaalde eigenschappen, wat veel kleinere DXF-uitvoer geeft voor complexe lagen die herhaalde puntsymbolen bevatten.

Een proces van het hashen van attributen wordt gebruikt om het uitvoeren te optimaliseren en houdt rekening met alle mogelijke combinaties van attributen. In instanties waar veel combinaties uniek zijn, zou elk blok slechts bijna altijd maar één keer gebruikt worden - wat resulteert in een groot uitvoerbestand. Voor het beheren van dergelijke gevallen heeft het dialoogvenster "Project naar DXF exporteren" nu nieuwe opties voor configureren om het aantal blokken per symboollaag te beperken (-1 betekent geen beperking). Als de beperking is ingesteld op een waarde integer, bijv. 5, dan worden alleen de 5 blokken met het hoogste aantal verwijzingen gemaakt en de andere symbolen worden in de regel geschreven.

![](images/entries/5de078fe33adb052f1177d7359432e69c84d81fa.webp)

Dit werd mogelijk gemaakt door [Stadtwerke München](http://www.swm.de)

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Mogelijkheid: Optie 'Alleen geselecteerde objecten gebruiken' toegevoegd aan exporteren naar DXF
Een nieuwe optie is toegevoegd aan de dialoogvensters voor het exporteren naar DXF die gebruikers zal toestaan om alleen de actieve objecten in de huidige selectie te exporteren.

Standaard zal deze optie worden ingesteld op false.

![](images/entries/28e6ac14aac9b118efadc23167f795da2bc0c19c.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: importeren/exporteren: Instellingen dialoogvenster 'DXF exporteren' 
Gebruikers kunnen de instellingen voor de gebruikersinterface voor het dialoogvenster "DXF exporteren" opslaan en herstellen, wat het mogelijk maakt elk aantal configuraties te exporteren voor verbeterde herbruikbaarheid of om ze te delen met collega's voor uitgebreide samenwerking.

De instellingen worden geëxporteerd naar een XML-bestand dat kan worden geladen met de interface voor het configureren van DXF exporteren en overschrijft de bestaande waarden voor configuratie.

![](images/entries/7f343b6a090823e6a090f4a33423cdd52fb655a8.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Formulieren en widgets
### Mogelijkheid: Ondersteuning voor CMYK toegevoegd voor widget Kleur
Ondersteuning voor CMYK-kleuren is toegevoegd voor de widget Kleur in lijn met [CMYK QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283).

![](images/entries/b5572a60bcc06b580b55f42d2b87f6825daa5774.webp)

Dit werd mogelijk gemaakt door Métropôle de Bordeaux

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Bereik ouderobject toegevoegd bij het toevoegen/bewerken van een kindobject via de widget Relatiebewerker
Een huidig bereik current\_parent\_\* wordt nu verschaft bij het toevoegen en bewerken van kindobjecten door de widget relatiebewerker van het attributenformulier.

Dat is bijzonder nuttig in contexten waar een vastgelegd object of waarde erop kan vertrouwen dat het ouderobject tegelijkertijd zal worden vastgelegd, maar als het ouderobject nog niet vastgelegd is, kunnen de attributen en geometrie niet opgehaald worden.

Dit werd mogelijk gemaakt door [Hansestadt Herford](https://www.herford.de/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: "Overeenkomst bevat" voor automatisch aanvullen in de widget Waarderelatie
Eerder zou de functie Automatisch aanvullen alleen overeenkomen vanaf het begin van de tekenreeks, maar een nieuw optiekeuzevak stelt gebruikers in staat om opgenomen waarden overeen te laten komen met de gehele tekenreeks.

Het oude gedrag is nog steeds standaard voor automatisch aanvullen, wat deze optie een bewerking opt-in maakt.

![](images/entries/3834e0b22600cce776ac149910fd9246bda6bd9c.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Functionaliteit voor groeperen geïmplementeerd voor waarderelaties 
Functionaliteit voor groeperen is toegevoegd voor de widget Waarderealtie bewerken, wat het voor gebruikers mogelijk maakt items te hergroeperen in emmers of waarden. Gebruikers krijgen ook de optie om de groepswaarde weer te geven als naam voor de kop van de groep in het combinatievak en tabelwidgets.

![](images/entries/3ef4fa48ee89cc91babb736dd477a1db6b66bcbc.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Legenda van laag
### Mogelijkheid: legenda voor kleurenbalk weergeven voor vector heatmaplagen
In plaats van geen legenda weer te geven voor deze lagen, zal QGIS nu de kleurenbalk weergeven als een balk met kleurverloop.

Gebruikers kunnen de tekst voor labels min/ max beheren, de richting van de balk en de instellingen voor lettertypen.

Deze update introduceerde ook wijzigingen aan de interne API voor vectorrenderers, zodat renderers de flexibiliteit hebben om andere typen legenda's te maken dan `QgsSymbolLegendNodes` en verschaft de mogelijkheid voor toekomstige uitbreidingen aan bestaande renderers.

![](images/entries/06b024c9294de21d36cc6efb702c342106a6242d.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Filter voor boom van lagen toegevoegd voor "Alleen verbroken lagen"
Indien geselecteerd, zullen alleen lagen met verbroken bronnen in de boom worden weergegeven.

Dit geeft gebruikers de kans om gemakkelijk verbroken lagen te zoeken in grote complexe projecten. Die ze anders misschien niet hadden opgemerkt!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Processing
### Mogelijkheid: Meer detail weergeven in dialoogvenster Geschiedenis
Een nieuwe boomweergave wordt verschaft voor het beoordelen van items in de Geschiedenis van Processing. Waarbij het bronitem voor elk item het volledige log voor het algoritme weergeeft indien aangeklikt en de respectievelijke opdrachten voor Python of qgis\_process worden als kinditems weergegeven.

Dit verschaft meer nuttige informatie voor gebruikers die door de geschiedenis bladeren, terwijl nog steeds alle eerdere informatie beschikbaar is.

![](images/entries/34df4b46463545d3d9fc20168d386ffc04d9341d.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie "Geselecteerde stappen uitvoeren" toegevoegd in modelontwerper
Een nieuwe actie zal gebruikers in staat stellen om alleen de geselecteerde stappen in een model uit te voeren, wat het voor de gebruikers effectief mogelijk maakt een subset van een model uit te voeren.

De initiële staat zal worden genomen uit eventuele eerdere uitvoeringen van het model door de ontwerper, dus resultaten uit eerdere stappen in het model zijn beschikbaar voor de geselecteerde stappen.

Dit maakt het voor een gebruiker mogelijk om delen van een groot model te repareren, zonder constant het gehele model te moeten uitvoeren om te testen. Speciaal<br />nuttig als eerdere stappen in het model nogal wat tijd vragen!

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie "Uitvoerlagen bekijken" voor model kindalgoritmes
Bij het bewerken van een model met de ontwerper is een nieuwe optie voor rechtsklikken toegevoegd voor "Uitvoerlagen bekijken" voor elke kindstap in het model<br />dat werd uitgevoerd. Selecteren van deze optie zal de uitvoerlagen voor die stap als nieuwe lagen toevoegen aan het huidige project van QGIS.

Deze actie is beschikbaar voor alle kindalgoritmes in het model, zelfs als het model niet is geconfigureerd om de uitvoer van die kinderen te gebruiken als uitvoer voor het model. Deze actie is ook altijd beschikbaar na het uitvoeren van het model, zelfs als het model zelf faalt (bijv. wegens een foutief geconfigureerde stap later in het model).

Dit is ontworpen als een nuttige actie voor debuggen. Als het model van een gebruiker faalt (of onverwachte resultaten geeft), zullen ze nu in staat zijn door het model te traceren en de uitvoer te bekijken voor verdachte problematische stappen. Wat de noodzaak vermijdt voor het toevoegen van tijdelijke uitvoer aan een model en het opnieuw uit te voeren om te testen.

Een aanvullende actie "Log weergeven" wordt ook verschaft, zodat gebruikers het log kunnen bekijken voor elk kind nadat het dialoogvenster van het algoritme is gesloten.

![](images/entries/f4357f5df60617753cb9fc215f4cce96f34139b2.webp)

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Drempel voor afstand tot eindpunt voor netwerkanalyses
Een optionele parameter voor een drempel voor de afstand tot een eindpunt is toegevoegd aan de gereedschappen voor netwerkanalyses.

Het vorige (en huidige standaard) gedrag is dat eindpunten ALTIJD zullen worden gesnapt aan het dichtstbijzijnde punt in de netwerklaag. Ongeacht hoe ver ze van het netwerk liggen, wat resulteert in fouten waar punten worden gesnapt aan een rand die op een willekeurige afstand ligt.

Het gedrag van de drempel is afhankelijk van het algoritme:
- Voor het gereedschap “Servicegebied (vanuit laag)” is een optionele nieuwe uitvoer toegevoegd voor “niet-routeerbare objecten”. Deze uitvoer zal de objecten bevatten die te ver van het netwerk lijken te liggen. Alle andere objecten die binnen de tolerantieafstand voor het netwerk liggen, zullen worden opgeslagen in de standaarduitvoer van het gereedschap.
- Voor het gereedschap “Servicegebied (vanuit punt)” zal een fout worden opgeworpen als het punt te ver van het netwerk ligt.
- Voor het gereedschap “Kortste pad (punt naar punt)” zal een fout worden opgeworpen als ofwel de bron- of de doelpunten te ver van het netwerk liggen.
- Voor de gereedschappen “Kortste pad (laag naar punt)” en “Kortste pad (punt naar laag)”:
- Een fout zal worden opgeworpen als het **punt** te ver van het netwerk ligt.
- Een optionele nieuwe uitvoer werd toegevoegd voor “niet-routeerbare objecten”. Deze uitvoer zal de objecten bevatten die te ver van het netwerk lijken te liggen. Alle andere objecten die binnen de tolerantieafstand voor het netwerk liggen, zullen worden opgeslagen in de standaarduitvoer van het gereedschap.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning toegevoegd voor pure decoraties datum en tijd
QGIS Processing verschafte eerder ondersteuning voor het maken en verwerken van waarden datetime als een expliciet type datetime, maar deze uitgave zal de definitie van objecten datetime, time en date als afzonderlijke gegevens ondersteunen.

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Opties voor toepassing en projecten
### Mogelijkheid:  Optie verticaal CRS toegevoegd voor projecten
In lijn met [QEP \#267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267) is een nieuwe optie voor verticaal CRS toegevoegd aan projecten.

Als het project-CRS een samengesteld CRS is, dan zal het verticale CRS voor het project de verticale component zijn van het hoofd-project-CRS. Anders zal het de waarde zijn die expliciet door de gebruiker is ingesteld.

Gebruikers kunnen het verticale CRS specificeren via de tab Hoogte van de Projecteigenschappen.

Als een samengesteld CRS is gedefinieerd als het actieve CRS voor een project, zal het VerticaleReferentieSysteem de definitie voor het verticale CRS daarvan afleiden. Als het huidige project-CRS een 2D/ horizontaal CRS is, dan zullen gebruikers in staat zijn hun eigen expliciet geselecteerde verticale CRS in te stellen.

Deze functionaliteit heeft geen invloed op afhandelen van renderen of objecten en is momenteel slechts alleen een eigenschap metadata.

De API voor projectobjecten is ook uitgebreid om deze functionaliteit te ondersteunen en bevat nu methoden voor:
- crs(): De bestaande projectmethode voor het gedefinieerde project-CRS
- verticalCrs(): Een nieuwe projectmethode voor het ophalen van het VerticaalReferentieSysteem
- [crs3D()](https://github.com/qgis/QGIS/pull/57107): Een expliciete ophaler voor het ophalen van een samengesteld referentiesysteem (combinatie van crs en verticalCrs)

![](images/entries/83cc370834aa045a61e3021da640753f406f4a23.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Hoogtebereik toegevoegd aan projecteigenschappen
Deze instelling geeft gebruikers de mogelijkheid om de onder- en bovengrens voor hoogten in te stellen die zijn geassocieerd met het project. In lijn met [QEP 201](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/201) verschaft het een equivalente gebruikservaring voor het filteren van hoogtebereik als dat waar gebruikers al mee bekend zijn voor het configureren van instellingen voor Tijdbeheer binnen projecten.

Dit kan worden gespecificeerd op de tab Hoogte (hernoemd vanuit "Terrein") in de projecteigenschappen en breidt de API van de klasse QgsProjectElevationProperties uit.

![](images/entries/c9f0765306562047cdba7a675587d484d5a7ce51.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Sensoren
### Mogelijkheid: Ondersteuning uitbreiding object
Deze wijziging geeft entiteiten van SensorThings de mogelijkheid om te worden uitgebreid om de attributen van hun gerelateerde kindobjecten te bevatten, wat het relationele  model SensorThings weergeeft als een traditioneel "plat" GIS-vriendelijke tabelstructuur.

Bijvoorbeeld bij het selecteren van entiteiten Location kunnen gebruikers er nu voor kiezen om uit te breiden naar "Things &gt; Datastreams &gt; Observations". Dat zal resulteren in meerdere "gestapelde" objecten puntlocatie, een corresponderend met elke waarneming, waarbij de attributen voor elk puntobject de attributen location, thing, datastream en observation bevat.

Deze functionaliteit is het beste te gebruiken indien gecombineerd met enig bereik, object, begrenzing of aangepaste filteroptie, omdat dit anders kan resulteren in hele zware verzoeken aan de backendservice!

Een optie om het aantal terug te geven kindobjecten te beperken bij het uitbreiden wordt verschaft. Standaard zal een conservatieve hoeveelheid objecten worden teruggegeven om de lading voor de services te beperken en van gebruikers te vereisen dat ze expliciet "ervoor kiezen" om hele grote hoeveelheden objecten op te halen.

![](images/entries/457f84d686c8c91d0fc894920ab462511226c0d2.webp)

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning toegevoegd voor SensorThings Multidatastreams
Dit voegt ondersteuning toe voor het entiteitstype Multidatastream, zoals geïmplementeerd in de SensorThings versie 1.1 "MultiDatastream extension".

Terwijl de specificatie mandateert dat MultiDatastreams een optionele geometrie polygoon hebben, geven vele servers andere typen geometrie weer voor deze entiteit of geven fouten terug bij het proberen te lezen van de geometrieën uit MultiDatastreams. QGIS geeft nu overeenkomstig een optie weer om MultiDatastreams als lagen zonder geometrie te laden, naast de standaardoptie om ze als polygonenlagen te laden. Dat stelt gebruikers in staat een breder bereik aan verbindingen af te handelen.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Scheidingsteken gegevensframe seriële poort
Een nieuwe optie scheidingsteken voor gegevensframe is toegevoegd aan de configuratie van de seriële poort voor sensoren.

In gevallen waar meerdere gegevensframes worden gevonden in de laatste portie met gegevens die door de seriële poort zijn gepusht, zal deze implementatie alle gegevensframes teruggeven. Gebruikers kunnen dan een expressie gebruiken om de door de sensor teruggegeven laatste gegevenswaarde te splitsen naar individuele frames (bijv. met string\_to\_array).

![](images/entries/6cc5c72f2a9ff329f8a507e63e28d3771b26c0d3.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Een optionele instelling voor beperken van objecten toegevoegd
Maakt het mogelijk een maximaal aantal op te vragen objecten van de service in te stellen, wat het overladen van services met te veel verzoeken vermijdt

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning geïmplementeerd voor subset-tekenreeks voor SensorThings
Dat maakt het mogelijk aangepaste filters voor de laag in te stellen, met de filtersyntaxis voor SensorThings.

Een gebruikersinterface voor het aangepaste laagfilter wordt verschaft voor SensorThings-laagfilters, wat het voor gebruikers gemakkelijker maakt om geldige filters te maken met de filtertaal voor SensorThings.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Profiel plotten
### Mogelijkheid: Tolerantie voor lijnen en polygonen toegevoegd
Het gereedschap Hoogteprofiel is verbeterd door ondersteuning voor tolerantie toe te voegen voor lijnen en polygonen (2D/ 3D), zoals geïllustreerd met diepteweergaven (uit de [plug-in OpenLog](https://plugins.qgis.org/plugins/openlog/)).

Zonder ondersteuning voor toleranties wordt elk object lijn of polygoon in zijn geheel weergegeven binnen het plot van het hoogteprofiel, zodra het kruist met de profielboog. Door ondersteuning toe te voegen voor gebruikergedefinieerde toleranties, worden alleen kruisende schijven van het object die binnen het gedefinieerde gebied vallen, op de plot gerenderd.

![](images/entries/25b1f63397246b4195891a08956b38239e78df07.gif)

Dit werd mogelijk gemaakt door CEA/DAM François Renard

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Gegevensproviders
### Mogelijkheid: op bereik gebaseerd filteren toegevoegd voor lagen van SensorThings
Stelt gebruikers in staat een begrenzing voor het bereik van de laag in te stellen, zodat objecten alleen geladen worden als ze binnen dit bereik vallen.

Het bereik kan worden ingesteld met Databronnen beheren voordat de laag initieel wordt toegevoegd, of aangepast op de tab Bron van de Laageigenschappen.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor voorvoegsel webproxy voor URL's van ArcGIS
Een nieuw veld voorvoegsel wordt verschaft in de dialoogvensters voor het instellen van ArcGIS, dat het voor gebruikers mogelijk maakt het voorvoegsel voor de URL van een webproxy die wordt gebruikt voor toegang tot ArcGIS Services in te stellen, wat zal worden toegevoegd aan de voorzijde van alle verzoeken.

![](images/entries/671e0f4b015b4a575c6bb1255317f0af56a6c056.webp)

Deze mogelijkheid werd ontwikkeld door [Vytax](https://github.com/Vytax)
### Mogelijkheid: Ondersteuning toegevoegd voor het snel schatten van het bereik in verbindingen van SAP HANA
Metadata van opgeslagen bereik kan worden gebruikt met de nieuwe verbinding "Gebruik geschatte tabelstatistieken", die het mogelijk maakt een vooraf berekend bereik te schatten en een veel betere connectiviteit voor grote tabellen.

Hoewel kostbare functies voor samenvoegen worden vermeden wanneer het bereik opnieuw wordt berekend, is de informatie voor het bereik van tabellen voor HANA alleen beschikbaar na het samenvoegen van een delta. Standaard zal deze optie een terugval opleveren naar het standaardgedrag van het gebruiken van functies voor samenvoegen om bereiken te berekenen in gevallen waar de gegevens niet beschikbaar zijn (of nog niet eerder zijn berekend).

![](images/entries/cf6ffc5f71ca8d57e9f3f717bf3e960c5afb51e4.webp)

Deze mogelijkheid werd ontwikkeld door [Johannes Quast](https://github.com/jatsqi)
## QGIS Server
### Mogelijkheid: Standaardbeperking voor resultaten GetFeatureInfo
Een nieuwe instelling stelt gebruikers in staat een standaardwaarde FEATURE\_COUNT in te stellen voor elke verbinding van WMS, met een vooraf gedefinieerde standaardwaarde van 10.

Deze standaard werkt ook bij het toevoegen van lagen WMS vanuit de Browser, en kan voor elke laag worden overschreven indien toegevoegd vanuit Databronnen beheren.

De standaard gebruikservaring is niet gewijzigd bij het toevoegen van lagen vanuit databronnen beheren, dus de standaard van 10 is nog steeds van toepassing, tenzij die expliciet is ingesteld in de instellingen van de verbinding.

![](images/entries/aa3907488d32cf1e90bb04115dfacffb5cdfee21.webp)

Dit werd mogelijk gemaakt door [Duitse QGIS gebruikersgroep (QGIS Anwendergruppe Deutschland e.V.)](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Informatie over CRS toegevoegd in uitvoer van WMS GetFeatureInfo, als die anders is dan WGS84
GeoJSON vereist expliciet het gebruik van OGC:CRS84, maar als een verzoek GetFeatureInfo, dat expliciet een CRS vraagt dat geen WGS84 is, naar een QGIS Server WMS verstuurt, zal de uitvoer nu de definitie van het CRS bevatten op een manier die compatibel is met de oudere [specificatie van de indeling GeoJSON](http://wiki.geojson.org/GeoJSON_draft_version_6#Specification) die ondersteuning bevatte voor meerdere CoördinatenReferentieSystemen.

Dit werd mogelijk gemaakt door Eurométropole de Strasbourg

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Programmeerbaarheid
### Mogelijkheid: Functionaliteit vervangen/ alles vervangen toegevoegd aan QgsCodeEditorWidget
De nieuwe functionaliteit vervangen maakt het vervangen van overeenkomende tekst mogelijk. Als de optie voor zoeken van regex is ingeschakeld, dan zijn vastgelegde groepen met het patroon van de reguliere expressie beschikbaar om te gebruiken in de tekenreeks voor vervanging met de numerieke identificatie van de groep (bijv. met `\1`).

In aanvulling daarop is de scriptbewerker voor Processing geporteerd om de klasse `QgsCodeEditorWidget` en de functionaliteiten goed te gebruiken.

![](images/entries/286b7da77b39735f963327f8c0c373a4530023fc.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Aangepaste bronnen hoogteprofiel registreren
We hebben een nieuwe klasse `QgsProfileSourceRegistry` toegevoegd om zowel bron- als plug-inontwikkelaars in staat te stellen profielbronnen te registreren, anders dan die van kaartlagen (bijv. gebaseerd op profielwebservices).

Deze aangepaste profielbronnen kunnen hoogteprofielen maken die worden weergegeven in de hoofddockwidget Hoogteprofiel en als lay-outitems.

Plug-ins zouden, om dat te doen, `QgsAbstractPluginSource` moeten subklasseren en dat doorgeven aan het register via `registerProfileSource()`. Op dezelfde manier zouden plug-ins de registratie van hun geregistreerde bronnen moeten opheffen (zeer waarschijnlijk met hun methode `unload()`) met `unregisterProfileSource()`.

Net als andere registraties van QGIS is het register voor profielbronnen beschikbaar vanuit het object `QgsApplication`: `QgsApplication.profileSourceRegistry()`.

![Custom profile source example](images/entries/custom_profile_source.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault (Spatialys)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS cannot load feature classes from a .gdb with a 64bit ObjectID | [#57471](https://github.com/qgis/QGIS/issues/57471) | Probably no longer a bug with GDAL 3.9 |  |
| QGIS crashes while Export Data from a WFS-Service as DXF-File | [#57139](https://github.com/qgis/QGIS/issues/57139) | Kan niet worden gereproduceerd |  |
| WFS connection problems after QGIS Update from LTR 3.28.2 to LTR 3.34.4 | [#56931](https://github.com/qgis/QGIS/issues/56931) | Not a QGIS bug |  |
| [GML] asGml3() creates invalid GML for CurvePolygon | [#57355](https://github.com/qgis/QGIS/issues/57355) | [PR #57476](https://github.com/qgis/QGIS/pull/57476) | [PR #57485](https://github.com/qgis/QGIS/pull/57485) |
| GDAL processing provider: "FutureWarning: Neither ogr.UseExceptions() nor ogr.DontUseExceptions() has been explicitly called" warning | [#57344](https://github.com/qgis/QGIS/issues/57344) | [PR #57477](https://github.com/qgis/QGIS/pull/57477) | Niet van toepassing |
| QGIS can't create conformant geopackage files with UTC "Z" timestamps | [#57262](https://github.com/qgis/QGIS/issues/57262) | [PR #57483](https://github.com/qgis/QGIS/pull/57483) | [PR #57548](https://github.com/qgis/QGIS/pull/57548) |
| QGIS cannot load feature classes from a .gdb with a 64bit ObjectID | [#57471](https://github.com/qgis/QGIS/issues/57471) | [GDAL PR 9980](https://github.com/OSGeo/gdal/pull/9980) | N/B |
| [OAPIF] Server defined fields are not fetched when creating a new feature | [#57486](https://github.com/qgis/QGIS/issues/57486) | [PR #57547](https://github.com/qgis/QGIS/pull/57547) | [PR #57549](https://github.com/qgis/QGIS/pull/57549) |
| QGIS3.28.15:Polygon Features from ArcGIS GDB Turn into TABLE after Editing in QGIS | [#57536](https://github.com/qgis/QGIS/issues/57536) | [GDAL PR 10008](https://github.com/OSGeo/gdal/pull/10008) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti (itOpen / qcooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server GetFeatureInfo issue on WMTS layer | [#57441](https://github.com/qgis/QGIS/issues/57441) | [PR #57491](https://github.com/qgis/QGIS/pull/57491) | Wachtrij |
| Cannot connect to SQL Server on QGis 3.34.3 | [#56136](https://github.com/qgis/QGIS/issues/56136) | Kan niet worden gereproduceerd |  |
| Balloon annotations fails to adopt text formatting | [#57423](https://github.com/qgis/QGIS/issues/57423) | Kan niet worden gereproduceerd |  |
| Generate XYZ tiles' does not render labels from ArcGIS Vector Tile Service layers | [#57443](https://github.com/qgis/QGIS/issues/57443) | [PR #57517](https://github.com/qgis/QGIS/pull/57517) | Wachtrij |
| Empty space after host name in SQL server, cause inconsistent error | [#57358](https://github.com/qgis/QGIS/issues/57358) | [PR #57518](https://github.com/qgis/QGIS/pull/57518) | Wachtrij |
| GDAL/OGR processing algorithms may silently output incorrect result if an input is a vector "memory" layer with a "fid" column | [#57343](https://github.com/qgis/QGIS/issues/57343) | [PR #57522](https://github.com/qgis/QGIS/pull/57522) | Wachtrij |
| attribute table row sorting doesn't work | [#57338](https://github.com/qgis/QGIS/issues/57338) | [PR #57624](https://github.com/qgis/QGIS/pull/57624) | Wachtrij |
| Unable to edit elements in the print layout after locking an element | [#57331](https://github.com/qgis/QGIS/issues/57331) | [PR #57543](https://github.com/qgis/QGIS/pull/57543) | Wachtrij |
| QGIS 3.34 LTR not loading REST services with referers | [#57288](https://github.com/qgis/QGIS/issues/57288) | Cannot reproduce (on master) |  |
| New Postgis/Postgres connection NOT saving username/password when requested | [#57284](https://github.com/qgis/QGIS/issues/57284) | [PR #57544](https://github.com/qgis/QGIS/pull/57544) |  |
| setting labeling font size to less than 0.3 freezes qgis with meters units | [#57336](https://github.com/qgis/QGIS/issues/57336) | [PR #57560](https://github.com/qgis/QGIS/pull/57560) |  |
| Server: OAPIF/WFS3 service collection id missmatch | [#57556](https://github.com/qgis/QGIS/issues/57556) | [PR #57561](https://github.com/qgis/QGIS/pull/57561) | Wachtrij |
| [Layout manager] The wordwrap expression function fails if the legend item is set to hidden | [#57589](https://github.com/qgis/QGIS/issues/57589) | Cannot reproduce (on master) - closed by OP |  |
| [ux][layouts] Fix legend item style mutex | niet gerapporteerd | [PR #57605](https://github.com/qgis/QGIS/pull/57605) | N/B |
| Expression output won't show until you open the attribute table (PostGIS layers) | [#57578](https://github.com/qgis/QGIS/issues/57578) | Cannot reproduce (on master and 3.36) |  |
| QGIS Server wrongly positions the map objects in the output when there's more than one map | [#57631](https://github.com/qgis/QGIS/issues/57631) | Is geen probleem |  |
| Current selected feature still marked as "dirty" after save in attribute table's form view | [#57644](https://github.com/qgis/QGIS/issues/57644) | [PR #57674](https://github.com/qgis/QGIS/pull/57674) |  |
| JSON-String not read from GPKG | [#57673](https://github.com/qgis/QGIS/issues/57673) | [PR #57707](https://github.com/qgis/QGIS/pull/57707) | N/B |
| value maps ignore field length | [#57634](https://github.com/qgis/QGIS/issues/57634) | [PR #57690](https://github.com/qgis/QGIS/pull/57690) |  |
| Identify Results for raster data value does not use correct decimal separator | [#57765](https://github.com/qgis/QGIS/issues/57765) | [PR #57769](https://github.com/qgis/QGIS/pull/57769) | Wachtrij |
| Value relation dropdown issue -Dropdown list selection reverts to default value upon selecting subtype option | [#57808](https://github.com/qgis/QGIS/issues/57808) | Cannot reproduce (awaiting feedback) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door David Signer (OPENGIS)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Wrongly displayed action widget | [#33464](https://github.com/qgis/QGIS/issues/33464), [#57398](https://github.com/qgis/QGIS/issues/57398), [#56966](https://github.com/qgis/QGIS/issues/56966) | [PR #57475](https://github.com/qgis/QGIS/pull/57475) | Niet van toepassing |
| Custom properties variableNames and variableValues are cleared when more than one layer custom variable exist | [#57334](https://github.com/qgis/QGIS/issues/57334) | [PR #57490](https://github.com/qgis/QGIS/pull/57490) | Niet van toepassing |
| Default values depending on other fields are not correctly applied when field not part of form made by Drag and Drop Designer | [#57411](https://github.com/qgis/QGIS/issues/57411) | [PR #57527](https://github.com/qgis/QGIS/pull/57527) | Niet van toepassing |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS)](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli (strk)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Source-tree documentation improvements | niet gerapporteerd | [PR #57594](https://github.com/qgis/QGIS/pull/57594) |  |
| QGIS DB manager lowercase conversion is broken | [#52898](https://github.com/qgis/QGIS/issues/52898) | [PR #57645](https://github.com/qgis/QGIS/pull/57645) |  |
| "money" type (postgresql) interpreted as string | [#25529](https://github.com/qgis/QGIS/issues/25529) | [PR #57513](https://github.com/qgis/QGIS/pull/57513) |  |
| Fix podman run of container-based testing | [#57724](https://github.com/qgis/QGIS/issues/57724) | [PR #57688](https://github.com/qgis/QGIS/pull/57688) |  |
| QGIS 3.34 is not able to figure out PostgreSQL relations when there are build using compound keys | [#56420](https://github.com/qgis/QGIS/issues/56420) | [PR #57653](https://github.com/qgis/QGIS/pull/57653) | [PR #57817](https://github.com/qgis/QGIS/pull/57817) |
| Fix PostgreSQL compound key discovery | [#56420](https://github.com/qgis/QGIS/issues/56420) | [PR #57653](https://github.com/qgis/QGIS/pull/57653) | [PR #57817](https://github.com/qgis/QGIS/pull/57817) |
| Extent of data fetched from GEOGRAPHY PostGIS column can not be changed | [#30294](https://github.com/qgis/QGIS/issues/30294) | [PR #57514](https://github.com/qgis/QGIS/pull/57514) |  |
| test_core_project test fail if TMPDIR is set to anything but /tmp | [#57610](https://github.com/qgis/QGIS/issues/57610) | [PR #57606](https://github.com/qgis/QGIS/pull/57606) |  |
| Tests create directories under ~/.local/share | [#50587](https://github.com/qgis/QGIS/issues/50587) |  |  |
| Directory /tmp full of QGIS temporary files after ctest run | [#48884](https://github.com/qgis/QGIS/issues/48884) |  |  |
| test_provider_postgresprovider TestPyQgsPostgresProvider.testExtent doesn't test extent | [#57818](https://github.com/qgis/QGIS/issues/57818) | [PR #57829](https://github.com/qgis/QGIS/pull/57829) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Sandro Santilli (strk)](https://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Avoid crash on summary when error list is empty | niet gerapporteerd | [PR #57658](https://github.com/qgis/QGIS/pull/57658) | [PR #57661](https://github.com/qgis/QGIS/pull/57661) |
| Masking symbol of current layer not listed in style panel | [#57248](https://github.com/qgis/QGIS/issues/57248) | [PR #57679](https://github.com/qgis/QGIS/pull/57679) | [PR #57783](https://github.com/qgis/QGIS/pull/57783) |
| Marker Line masking not working for layout prints or PDF exports | [#57564](https://github.com/qgis/QGIS/issues/57564) | [PR #57694](https://github.com/qgis/QGIS/pull/57694) |  |
| Qgis crashes while digitising lines | [#57617](https://github.com/qgis/QGIS/issues/57617) | Kan niet worden gereproduceerd |  |
| Crash when running Topology Checker to validate corrective edits. | [#53425](https://github.com/qgis/QGIS/issues/53425) | [PR #57695](https://github.com/qgis/QGIS/pull/57695) | [PR #57712](https://github.com/qgis/QGIS/pull/57712) |
| Topology Checker crashes | [#57627](https://github.com/qgis/QGIS/issues/57627) | [PR #57695](https://github.com/qgis/QGIS/pull/57695) | [PR #57712](https://github.com/qgis/QGIS/pull/57712) |
| Debian sid Qt6 compile fails on sip build, python bindings | [#57760](https://github.com/qgis/QGIS/issues/57760) | upstream issue, wait for PyQt/sip mailing list answer |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| copy/paste feature tool sets integer/decimal fields of destination feature to 0 if the source feature fields are NULL | [#57710](https://github.com/qgis/QGIS/issues/57710) | [PR #57851](https://github.com/qgis/QGIS/pull/57851) | [PR #57855](https://github.com/qgis/QGIS/pull/57855) |
| Postgres layer with multi geometry columns fails to export | [#57757](https://github.com/qgis/QGIS/issues/57757) | Is geen probleem |  |
| Georeferencing tool: default name for export with an accent in french (_modifié) | [#55389](https://github.com/qgis/QGIS/issues/55389) | [Transifex](https://app.transifex.com/qgis/QGIS/translate/#fr/$/412589941?q=text%3A_modified) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgsabstractmaterialsettings: Handle selection in addParametersToEffect | niet gerapporteerd | [PR #57803](https://github.com/qgis/QGIS/pull/57803) | not backported |
| qgs3daxis: Fix cube face picking | niet gerapporteerd | [PR #57848](https://github.com/qgis/QGIS/pull/57848) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.34 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix bugs relating to selective masking vector exports | [#50734](https://github.com/qgis/QGIS/issues/50734) | [PR #57843](https://github.com/qgis/QGIS/pull/57843) | Te indringend |
| Fix bugs relating to selective masking vector exports | [#54788](https://github.com/qgis/QGIS/issues/54788) | [PR #57703](https://github.com/qgis/QGIS/pull/57703) | Te indringend |
| Fix bugs relating to selective masking vector exports | [PR #57623](https://github.com/qgis/QGIS/pull/57623) | Te indringend |  |
| Fix bugs relating to selective masking vector exports | [PR #57498](https://github.com/qgis/QGIS/pull/57498) | Te indringend |  |
| Pressing escape should clear current identify results | [#47984](https://github.com/qgis/QGIS/issues/47984) | [PR #57774](https://github.com/qgis/QGIS/pull/57774) | N/B |
| Fix some grass vectors incorrectly show as datasets | niet gerapporteerd | [PR #57780](https://github.com/qgis/QGIS/pull/57780) | [PR #57786](https://github.com/qgis/QGIS/pull/57786) |
| Don't try to load extent strings as layers | [#57758](https://github.com/qgis/QGIS/issues/57758) | [PR #57772](https://github.com/qgis/QGIS/pull/57772) | [PR #57787](https://github.com/qgis/QGIS/pull/57787) |
| Limit fixed interval classification to generate at most 999 classes | [PR #50290](https://github.com/qgis/QGIS/pull/50290) | [PR #57722](https://github.com/qgis/QGIS/pull/57722) | Niet van toepassing |
| Don't try to connect widget to null vector tile layers | niet gerapporteerd | [PR #57721](https://github.com/qgis/QGIS/pull/57721) | N/B |
| Don't show invalid "Style not found in database" warning when adding vector tile layers | niet gerapporteerd | [PR #57714](https://github.com/qgis/QGIS/pull/57714) | Niet van toepassing |
| Replace processing default extension setting with string based setting | [#57676](https://github.com/qgis/QGIS/issues/57676) | [PR #57702](https://github.com/qgis/QGIS/pull/57702) | Niet van toepassing |
| Fix incorrect attempts to load outputs from models to projects | [#57698](https://github.com/qgis/QGIS/issues/57698) | [PR #57701](https://github.com/qgis/QGIS/pull/57701) | [PR #57715](https://github.com/qgis/QGIS/pull/57715) |
| Fix add feature dialog does not restore position when shown modally | niet gerapporteerd | [PR #57686](https://github.com/qgis/QGIS/pull/57686) | [PR #57700](https://github.com/qgis/QGIS/pull/57700) |
| Fix python script editor "open in external editor" action | niet gerapporteerd | [PR #57682](https://github.com/qgis/QGIS/pull/57682) | Niet van toepassing |
| Fix broken prefetch capabilities for raster layers | niet gerapporteerd | [PR #57663](https://github.com/qgis/QGIS/pull/57663) | [PR #57667](https://github.com/qgis/QGIS/pull/57667) |
| Fix missing field type information in eg the horizontal header tooltips in attribute table | niet gerapporteerd | [PR #57621](https://github.com/qgis/QGIS/pull/57621) | Niet van toepassing |
| Don't try to paint to indexed image | niet gerapporteerd | [PR #57601](https://github.com/qgis/QGIS/pull/57601) |  |
| Clamp values for set_color_part function to avoid qt warnings when out of range values are specified | niet gerapporteerd | [PR #57600](https://github.com/qgis/QGIS/pull/57600) |  |
| Add some tests for rendering text with RTL markers | [PR #57586](https://github.com/qgis/QGIS/pull/57586) |  |  |
| Fix rotation based orientation when html labeling enabled | niet gerapporteerd | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Te indringend |
| Fix data defined font size is ignored when HTML labeling is active | niet gerapporteerd | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Te indringend |
| Don't set @value to line height when evaluating multi line alignment | niet gerapporteerd | [PR #57582](https://github.com/qgis/QGIS/pull/57582) | Te indringend |
| Don't try to load CRS strings as map layers | [#57494](https://github.com/qgis/QGIS/issues/57494) | [PR #57508](https://github.com/qgis/QGIS/pull/57508) | [PR #57541](https://github.com/qgis/QGIS/pull/57541) |
| Don't try to load CRS strings as map layers | [#57494](https://github.com/qgis/QGIS/issues/57494) | [PR #57576](https://github.com/qgis/QGIS/pull/57576) | [PR #57579](https://github.com/qgis/QGIS/pull/57579) |
| Fix line extension tool when layer crs != map crs | [#49267](https://github.com/qgis/QGIS/issues/49267) | [PR #57575](https://github.com/qgis/QGIS/pull/57575) |  |
| Fix incorrect buffers drawn for html label item | niet gerapporteerd | [PR #57551](https://github.com/qgis/QGIS/pull/57551) | [PR #57571](https://github.com/qgis/QGIS/pull/57571) |
| Fix label mask sizes get reset to 0 | niet gerapporteerd | [PR #57555](https://github.com/qgis/QGIS/pull/57555) | [PR #57569](https://github.com/qgis/QGIS/pull/57569) |
| Fix tab stops in legend text | [#56981](https://github.com/qgis/QGIS/issues/56981) | [PR #57554](https://github.com/qgis/QGIS/pull/57554) | N/B |
| Fix colors for new diagram categories are not randomly picked | [#56862](https://github.com/qgis/QGIS/issues/56862) | [PR #57532](https://github.com/qgis/QGIS/pull/57532) | [PR #57539](https://github.com/qgis/QGIS/pull/57539) |
| Make brush and stroke style combo box icons visible on dark themes | niet gerapporteerd | [PR #57506](https://github.com/qgis/QGIS/pull/57506) | [PR #57510](https://github.com/qgis/QGIS/pull/57510) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
