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
### Feature: Create DXF blocks for point symbols with data defined properties
Additional enhancements have been added to the capability of utilizing references within a DXF, especially for complex data-defined properties, providing much smaller DXF outputs for complex layers that include repeated point symbols.

A process of attribute hashing is utilized to optimize the performance and account for all possible attribute combinations. In instances where many combinations are unique, each block would only be used nearly once - resulting in a large output file. To manage such cases, the "Export Project to DXF" dialog now includes new configuration options to limit the number of blocks per symbol layer (-1 means no limitation). If the limit is set to an integer value, e.g. 5, then only the 5 blocks with the highest number of references are created and the other symbols are written inline.

![](images/entries/5de078fe33adb052f1177d7359432e69c84d81fa.webp)

Dit werd mogelijk gemaakt door [Stadtwerke München](http://www.swm.de)

Deze mogelijkheid werd ontwikkeld door [mhugent](https://github.com/mhugent)
### Feature: Add option 'Use only selected features' to DXF export
A new option has been added to DXF export dialogs that will allow users to export only the features active in the current selection.

By default, this setting will be set to false.

![](images/entries/28e6ac14aac9b118efadc23167f795da2bc0c19c.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Feature: Import/ Export 'DXF Export' dialog settings
Users to save and restore GUI settings for the DXF Export dialog, making it possible to export any number of configurations for improved reusability or to share them with colleagues for enhanced collaboration.

Settings are exported to an XML file which can be loaded into the DXF Export configuration interface, overwriting the existing configuration values.

![](images/entries/7f343b6a090823e6a090f4a33423cdd52fb655a8.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Formulieren en widgets
### Feature: Add CMYK support for Color Widget
CMYK color support has been added for the color widget in line with the [CMYK QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/283).

![](images/entries/b5572a60bcc06b580b55f42d2b87f6825daa5774.webp)

Dit werd mogelijk gemaakt door Métropôle de Bordeaux

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
### Feature: Add parent feature scope when adding/editing a child feature through the relation editor widget
A current\_parent\_\* scope is now provided when adding and editing child features through the attribute form's relation editor widget.

This is very useful in contexts where a captured feature or value may rely on the parent entity being captured at the same time, but as the parent feature has not yet been captured, the attributes and geometry cannot be retrieved.

Dit werd mogelijk gemaakt door [Hansestadt Herford](https://www.herford.de/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add "match contains" to autocompleter in value relation widget
Previously, the autocomplete function would match from the beginning of the string only, but a new checkbox option allows users to match contained values within the entire string.

The old behavior is still the default for autocomplete, making this setting an opt-in operation.

![](images/entries/3834e0b22600cce776ac149910fd9246bda6bd9c.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Implement value relation's grouping functionality
Grouping functionality has been added for the value relation editor widget, allowing users to regroup items into buckets of values. Users are also given the option to show the group value as a group header name in the combo box and table widgets.

![](images/entries/3ef4fa48ee89cc91babb736dd477a1db6b66bcbc.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Legenda van laag
### Feature: Show a color ramp legend for vector heatmap layers
Instead of showing no legend for these layers, QGIS will now show the color ramp as a gradient bar.

Users can control the text for the min/ max labels, the direction of the bar, and the font settings.

This update also introduced changes to the internal API for vector renderers so that renderers have the flexibility to create other types of legend nodes other than `QgsSymbolLegendNodes` and provides the opportunity for future extensions to existing renderers.

![](images/entries/06b024c9294de21d36cc6efb702c342106a6242d.webp)

Dit werd mogelijk gemaakt door Rubicon Concierge Real Estate Services

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add layer tree filter for "Show Broken Layers Only"
When checked, only layers with broken sources will be shown in the tree.

This allows users to easily find broken layers in large complex projects, where they may otherwise escape notice!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Processing
### Feature: Show more detail in history dialog
A new tree display is provided for review of processing history entries, where the root item for each entry shows the full algorithm log when clicked and the respective python or qgis\_process commands are displayed as child items.

This provides more useful information for users browsing the history, while still making all the previous information available.

![](images/entries/34df4b46463545d3d9fc20168d386ffc04d9341d.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add "Run Selected Steps" option to model designer
A new action will allow users to run only the selected steps in a model, effectively allowing users to run a subset of a model.

The initial state will be taken from any previous executions of the model through the designer, so results from previous steps in the model are available for the selected steps.

This makes it possible for a user to fix parts of a large model, without having to constantly run the entire model to test. Especially<br />useful when earlier steps in the model are time-consuming!

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add "View Output Layers" option for model child algorithms
When editing a model through the designer, a new right-click context option has been added for "View Output Layers" on any child step in the model<br />that has been run. Selecting this option will add the output layers from that step as new layers in the current QGIS project.

This action is available for all child algorithms in the model, even if the model is not configured to use the outputs from those children as model outputs. This action is also always available after running the model, even if the model itself fails (e.g. because of a misconfigured step later in the model).

This is designed as a helpful debugging action. If a user's model fails (or gives unexpected results), they will now be able to trace through the model and view the outputs for suspected problematic steps, avoiding the need to add temporary outputs to a model and re-run for testing purposes.

An additional "View Log" action has also been provided so that users can see the log for each child after the algorithm dialog has been closed down.

![](images/entries/f4357f5df60617753cb9fc215f4cce96f34139b2.webp)

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Endpoint distance threshold for network analysis
An optional end-point distance threshold parameter has been added to the network analysis tools.

The previous (and current default) behavior is that endpoints will ALWAYS be snapped to the nearest point in the network layer, regardless of how far away from the network they are, resulting in errors where points are snapped to an edge an arbitrary distance away.

The behavior of the threshold depends on the algorithm:
- For the “Service area (from layer)” tool an optional new output was added for “non-routable features”. This output will contain any features that were deemed too far from the network. All other features that are within tolerance distance to the network will be stored in the standard output from the tool.
- For the “Service area (from point)” tool an error will be raised if the point is too far from the network
- For the “Shortest path (point to point)” tool an error will be raised if either the source or destination points are too far from the network.
- For the “Shortest path (layer to point)” and “Shortest path (point to layer)” tools:
- An error will be raised if the **point** is too far from the network.
- A new optional output was added for “non-routable features”. This output will contain any features that were deemed too far from the network. All other features that are within tolerance distance to the network will be stored in the standard output from the tool.

Dit werd mogelijk gemaakt door City of Canning

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add support for pure date and time decorators
QGIS Processing previously provided support for generating and processing datetime values as an explicit datetime type, but this release will support the definition of datetime, time, and date objects as discrete data types.

Dit werd mogelijk gemaakt door Ifremer

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)
## Opties voor toepassing en projecten
### Feature: Add vertical crs option for projects
In line with [QEP \#267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267), a new vertical CRS option has been added to projects.

If the project CRS is a compound CRS, then the vertical CRS for the project will be the vertical component of the main project CRS. Otherwise, it will be the value explicitly set by the user.

Users can specify the vertical CRS through the Elevation Tab of the Project Properties.

If a compound CRS is defined as the active CRS for a project, the Vertical Reference System will infer the Vertical CRS definition. If the current project CRS is a 2D/ Horizontal CRS, then users will be able to define their own explicitly selected Vertical CRS.

This functionality does not impact rendering or feature handling and is currently a metadata property only.

The API for project objects has also been extended to support this functionality, and now includes methods for:
- crs(): The existing project method for the defined project CRS
- verticalCrs(): A new project method for fetching the Vertical Reference System
- [crs3D()](https://github.com/qgis/QGIS/pull/57107): An explicit getter for retrieving a compound reference system (combination of crs and verticalCrs)

![](images/entries/83cc370834aa045a61e3021da640753f406f4a23.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add elevation range to project properties
This setting allows users to specify the upper and lower elevation limits associated with the project in line with [QEP 201](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/201), providing an equivalent user experience for filtering elevation range as users may already be familiar with for configuring the temporal range settings within projects.

This can be specified through the Elevation tab (renamed from "Terrain") in the Project Properties and extends the API of the QgsProjectElevationProperties class.

![](images/entries/c9f0765306562047cdba7a675587d484d5a7ce51.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Sensoren
### Feature: Support feature expansion
This change allows SensorThings entities to be expanded to contain their related child feature attributes, exposing the relational SensorThings model as a traditional "flat" GIS-friendly table structure.

For example, when selecting Location entities, users can now opt to expand to "Things &gt; Datastreams &gt; Observations". This would result in multiple "stacked" point location features, one corresponding to each observation, with the attributes for each point feature containing the location, thing, datastream, and observation attributes.

This functionality is best used when combined with some extent, feature limit, or custom filter option, as this can otherwise result in very heavy requests to the backend service!

An option to limit the number of child features returned when expanding is provided. By default, a conservative amount of features will be returned to reduce the load on services and require users to explicitly "opt-in" to fetch large amounts of features.

![](images/entries/457f84d686c8c91d0fc894920ab462511226c0d2.webp)

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add support for SensorThings Multidatastreams
This adds support for the Multidatastream entity type, as implemented in the SensorThings version 1.1 "MultiDatastream extension".

While the specification mandates that MultiDatastreams have an optional polygon geometry, many servers expose different geometry types for this entity or return errors when attempting to read the geometries from MultiDatastreams. Accordingly, QGIS now exposes an option to load MultiDatastreams as geometryless layers alongside the default option to load them as polygon layers, allowing users to handle a wider range of connections.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Serial port sensor's data frame delimiter
A new data frame delimiter option has been added to the serial port sensor configuration.

In cases where multiple data frames are found in the last chunk of data pushed by the serial port, this implementation will return all data frames. Users can then use an expression to further split the returned last data value from the sensor into individual frames (e.g. using string\_to\_array).

![](images/entries/6cc5c72f2a9ff329f8a507e63e28d3771b26c0d3.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add an optional feature limit setting
Allows setting a maximum number of features to request from the service, avoiding overloading services with too many requests

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Implement subset string support for SensorThings
This allows setting custom filters on the layer, using the SensorThings filter syntax.

A custom layer filter GUI is provided for SensorThings layer filters, making it easier for users to craft valid filters using the SensorThings filter language.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Profiel plotten
### Feature: Add tolerance for lines and polygons
The elevation profile tool has been improved by adding tolerance support for lines and polygons (2D/ 3D), as illustrated using drillhole representations (from the [OpenLog plugin](https://plugins.qgis.org/plugins/openlog/)).

Without support for tolerances, any line or polygon feature is displayed in its entirety within the elevation profile plot as soon as it intersects the profile curve. By adding support for user-defined tolerances, only intersecting slices of the feature that fall within the defined region are rendered on the plot.

![](images/entries/25b1f63397246b4195891a08956b38239e78df07.gif)

Dit werd mogelijk gemaakt door CEA/DAM François Renard

Deze mogelijkheid werd ontwikkeld door [Benoit D.-M. - oslandia](https://github.com/benoitdm-oslandia)
## Gegevensproviders
### Feature: Add extent based filtering for SensorThings layers
Allows users to set an extent limit for the layer so that features are only ever loaded within this extent.

The extent can be set using the data source manager before initially adding the layer, or modified within the source tab if the layer properties.

Dit werd mogelijk gemaakt door [BRGM](https://www.brgm.fr/en) en [Water4All Partnership](https://www.water4all-partnership.eu)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Web proxy prefix support for ArcGIS URLs
A new prefix field is provided in ArcGIS settings dialogs that allows users to define the URL prefix of a web proxy used to access ArcGIS Services which will be prepended to all requests.

![](images/entries/671e0f4b015b4a575c6bb1255317f0af56a6c056.webp)

Deze mogelijkheid werd ontwikkeld door [Vytax](https://github.com/Vytax)
### Feature: Add support for fast extent estimation on SAP HANA connections
Stored extent metadata can be utilized with the new "use estimated metadata" connection, which allows for precomputed extent estimation and much faster connectivity on large tables.

Although costly aggregation functions are avoided whenever the extent is recomputed, the extent information for HANA tables is only available after a delta merge. By default, this option will leverage a fallback to the standard behavior of using aggregation functions to compute extents in cases where the data is unavailable(or has not yet been computed).

![](images/entries/cf6ffc5f71ca8d57e9f3f717bf3e960c5afb51e4.webp)

Deze mogelijkheid werd ontwikkeld door [Johannes Quast](https://github.com/jatsqi)
## QGIS Server
### Feature: Default limit for GetFeatureInfo results
A new setting allows users to set a default FEATURE\_COUNT value individually for each WMS connection, with a predefined default value of 10.

This default also works when adding WMS layers from the browser and it can be overridden for each layer when added from the datasource manager.

The default user experience has not changed when adding layers from the data source manager, so the default of 10 still applies unless it is explicitly set from the connection settings.

![](images/entries/aa3907488d32cf1e90bb04115dfacffb5cdfee21.webp)

Dit werd mogelijk gemaakt door [Duitse QGIS gebruikersgroep (QGIS Anwendergruppe Deutschland e.V.)](https://qgis.de/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add crs information in WMS GetFeatureInfo output when it differs from WGS84
GeoJSON explicitly requires the use of OGC:CRS84, but when a GetFeatureInfo request that explicitly requests a CRS that is not WGS84 is sent to a QGIS Server WMS, the output will now include the CRS definition in a manner compatible with the older [GeoJSON specification format](http://wiki.geojson.org/GeoJSON_draft_version_6#Specification) that included support for multiple Coordinate Reference Systems.

Dit werd mogelijk gemaakt door Eurométropole de Strasbourg

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)
## Programmeerbaarheid
### Feature: Add replace/ replace all functionality to QgsCodeEditorWidget
The new replace functionality allows replacing matching text. If the regex find option is enabled, then captured groups from the regular expression pattern are available for use in the replacement string using the numeric identifier of the group (e.g. via `\1`).

In addition, the processing script editor has been ported to leverage the `QgsCodeEditorWidget` class and functionalities.

![](images/entries/286b7da77b39735f963327f8c0c373a4530023fc.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Register custom elevation profile sources
We've added a new `QgsProfileSourceRegistry` class to allow both core and plugin developers to register profile sources other than map layers (e.g., based on profile web services).

These custom profile sources can generate elevation profiles that are displayed in the main Elevation Profile dock widget and as layout items.

To do so, plugins should subclass `QgsAbstractPluginSource` and pass it to the registry via `registerProfileSource()`. Likewise, plugins should unregister (most likely on their `unload()` method) their registered sources via `unregisterProfileSource()`.

Like other QGIS registries, the profile source registry is available from the `QgsApplication` object: `QgsApplication.profileSourceRegistry()`.

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
### Feature: Bug fixes by David Signer (OPENGIS)
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
