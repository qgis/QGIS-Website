---
HasBanner: false
draft: false
releaseDate: 17-06-2022
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.26
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.26{#changelog326 }
![image1](images/projects/916ce336f8f5939eb158506ea38290af6f1ce0f0.png)

Datum uitgave 17-06-2022

De vol met mogelijkheden verpakte uitgave van QGIS 3.26 Buenos Aires bevat een groot aantal verbeteringen tot een bereik aan geavanceerde bron-functionaliteiten. Dit omvat enorm veel verbeteringen aan de mogelijkheden voor, verbeterde gereedschappen voor puntenwolken, en de introductie van een nieuw framewerk voor profiel-plotten voor het maken van kruisende gedeelten en hoogte-profielen. Het beste van dit alles, het nieuwe framewerk voor plotten gebruikt de eigen mogelijkheden voor renderen van QGIS en komt met alle eigenschappen voor stijlen, symbologie, en door gegevens bepaalde, die we al kenden en waar we van hielden, ingebakken!

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://youtu.be/pZmrw_zR7sA>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/pZmrw_zR7sA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

The QGIS Community has also been active in various crowd-funding campaigns, [Open Day events](https://github.com/qgis/QGIS/wiki#qgis-open-day), and the growth of the [STAC Ecosystem](https://medium.com/radiant-earth-insights/stac-updates-february-2022-e02a194861e) has led to inter-agency collaboration initiatives which include outcomes such as the [STAC Browser QGIS Plugin](https://stac-utils.github.io/qgis-stac-plugin/), which make it nearly trivial to produce [Raster Mosaics](https://www.youtube.com/watch?v=se2Xd7CKhHg) from Earth Observation data using Open Source and Open Data. There is also a new [online analytics dashboard](https://blog.qgis.org/2022/06/16/qgis-userbase-analytics/) which collects information from the QGIS Feed in an attempt to show how and where QGIS is being used, providing valuable insight to developers and the QGIS community.

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Belangrijke wijzigingen
### Mogelijkheid: Ondersteuning voor DB2 verwijderd
De provider DB2 is aangemerkt als verouderd en voor een aantal uitgaven verborgen in de gebruikersinterface van QGIS. Aangezien er zich geen personen hebben gemeld voor het onderhouden van deze gegevensprovider, is die verwijderd en zal niet langer voor gebruik beschikbaar zijn in QGIS.
## Kaartgereedschap
### Mogelijkheid: Selecteren van alle objecten op hun attribuutwaarden vanuit het paneel Identificatieresultaten
De gereedschappen voor Identificatieresultaten verschaffen nu een optie, beschikbaar vanuit het contextmenu van een waarde van een attribuutveld, die het mogelijk maakt alle objecten in die laag met overeenkomende waarden snel te selecteren.

![image3](images/entries/d2f2d4bf5b05b7e21aa6ff0957ad8be8ccda082f.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Gebruikersinterface
### Mogelijkheid: Coördinaten ordenen volgens CRS
QGIS zal nu de juiste ordening van coördinaten voor het project-CRS gebruiken bij het weergeven van coördinaten in de statusbalk (en Identificatieresultaten). Een instelling is aan de projecteigenschappen toegevoegd om het voor gebruikers mogelijk te maken dit te overschrijven met, indien gewenst, een specifieke ordening van de coördinaten (x/y of y/x).

Specifiek betekent dit dat projecten in geografische CRS-sen, zoals EPSG:4326, nu coördinaten zullen weergeven in de volgorde latitude/longitude in plaats van longitude/latitude (tenzij het specifieke CRS een andere eigen volgorde heeft).

![image4](images/entries/7dada94231069c7f647d9a4a239d57506ad14bfd.gif)

Dit werd mogelijk gemaakt door SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Objecten selecteren uit op expressie gebaseerde symbolen
A \"Select Features\" action has been added to the right click context menu on legend class symbols. This allows you to rapidly select all features within a layer that match the associated symbol class in categorized, graduated, and rule based renderers.

![image5](images/entries/965a5e626ced053fd00fc33288c17330b7f920a0.gif)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Voorbeeld van waarde van expressie kopiëren naar klembord
Een nieuwe knop is toegevoegd aan de interface voor de Expressiebouwer die het mogelijk maakt de waarde van de expressie in het voorbeeldveld te kopiëren naar het klembord.

![image6](images/entries/0ecfdc2b0f6dae82ab5650f4d1d97d37df33aee4.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Mogelijkheid: Optie om paneel Statistieken te synchroniseren met de selectie van de laag
A \"Keep synchronized with TOC\" checkbox has been added to the statistics panel, which allows the statistics panel to automatically synchronize with the table of contents layer list, ensuring that the active layer is selected for the computed statistics displayed in the statistics panel.

De meest recent gedefinieerde expressie, die werd gebruikt voor het definiëren voor het berekenen van de statistieken voor een laag, zal onafhankelijk voor elke laag worden behouden.

![image7](images/entries/0075fa6cc3b8410072eeec8bb43ac4cef4c38e61.webp)

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### Mogelijkheid: Actie voor scrollwiel implementeren voor knoppen voor kleur en symbolen
Activeren van een actie voor het scrollwiel bij het over een symboollaag gaan zal nu automatisch een van de stijlattributen aanpassen, wat het meer efficiënt maakt om veel voorkomende regels voor symbologie aan te passen. Deze mogelijkheid beïnvloedt verschillende symboolstijlen op verschillende manieren, gebaseerd op welk besturingselement in de gebruikersinterface is geselecteerd.
- Voor markeringssymbolen, de grootte van de markering vergroten / verkleinen
- Voor lijnsymbolen, de breedte van de lijn vergroten / verkleinen

In aanvulling daarop zal het activeren van een actie voor het muiswiel, terwijl over een symbool voor kleur wordt gegaan, de opaciteit van de kleur vergroten / verkleinen.

![image8](images/entries/ab668355973259b389bd2623c4b1ba01b5e8f237.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Toegankelijkheid
### Mogelijkheid: Horizontaal scrollen in tabel met shift+wiel
Attributentabellen kunnen nu horizontaal gescrold worden met de toetscombinatie Shift + muiswiel, schakelend vanuit de standaard verticale bewerking voor scrollen.

This matches the behavior exposed by LibreOffice, and provides a convenient way to quickly horizontally scroll tables when a mouse doesn\'t have a dedicated horizontal scroll wheel.

![image9](images/entries/7bf2a8d0d0500149ed7b1cb5edb22b8cd6258c86.gif)

Dit werd mogelijk gemaakt door de City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Symbologie
### Feature: New \"Animated Marker\" symbol type
Een nieuw type markeringssymbool maakt het mogelijk punten te renderen met een geanimeerde markering, genomen vanuit een geanimeerde gif, webp of mng animatie. Opties zijn aanwezig voor markeringsbestand, grootte, hoek en framesnelheid.

Er zijn twee manieren waarop geanimeerde symbolen worden afgehandeld.
- Als de kaart NIET wordt beschouwd als een animatie (d.i. een gewoon project van QGIS), dan zal het te renderen frame alleen worden gebaseerd op het huidige tijdstempel.
- Als de kaart zelf wordt beschouwd als een animatie, dan zal het te renderen frame voor de geanimeerde markering worden gebaseerd op het frame voor de kaartanimatie en de framesnelheid. Dit is het geval als Tijdbeheer is ingesteld voor de modus Animatie. In dat geval volgen de geanimeerde markeringen de animatie van Tijdbeheer, bijv. pauzeren wanneer de animatie wordt gepauzeerd, doorgaan van de frames met de animatie, etc. Deze modus wordt ook toegepast bij het exporteren van een animatie vanuit Tijdbeheer en wordt gebruikt als een plug-in specifiek de framesnelheid en huidige eigenschappen voor frames instelt.

![image10](images/entries/e5330839c8c13220ccbbb2ea1c5fc556548a21be.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Toestaan dat elk symbool een geanimeerd symbool wordt
Users can now indicate that a symbol should be treated as an animated symbol, through the new \"Animation Settings\" option in the symbol widget\'s Advanced menu.

This settings panel allows users to enable animation for the symbol and set a specific frame rate at which the symbol should be redrawn. When enabled, the \@symbol_frame variable can be used in any symbol data defined property in order to animate that property.

For instance, setting the symbol\'s rotation to the following data defined expression will cause the symbol to rotate over time, with rotation speed dictated by the symbol\'s refresh rate.

    @symbol_frame % 360
    
![image11](images/entries/c5c8938147137d9264d57a56c00548cc535cdaa2.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Add a new classification method for \"Fixed interval\"
Stelt gebruikers in staat graduele afbrekingen te maken met een specifieke breedte voor de interval voor klassen (in plaats van het totale aantal klassen).

![image13](images/entries/5f4efe2866e8ba166c3948fb22946ec1ed3fa02b.gif)

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Paneel voor aangepast streepjespatroon geeft totale lengte van het patroon weer
Het paneel voor het aangepaste streepjespatroon geeft nu de totale lengte van het streepjespatroon weer, wat voor gebruikers de mogelijkheid verbeterd om de gehele patroonlengte te laten overeenkomen met grootten uit andere delen van een symbool.

![image14](images/entries/201cc3be8689d55102c675c4af0ffdf4204c2a2b.webp)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Stijlcategorieën selecteren bij het opslaan van stijlen in database
QGIS ondersteunt het opslaan van laagstijlen in de brondatabase, of in de lokale stijldatabase. QGIS verschaft dan de mogelijkheid om deze stijlen te gebruiken als standaardstijl voor een laag, of toegang te verschaffen tot die stijl via de Stijlmanager.

In eerdere uitgaven van QGIS sloeg dit proces alle beschikbare stijlcategorieën op in de database, nieuwe functionaliteit stelt gebruikers echter in staat te selecteren welke specifieke stijlcategorieën zouden moeten worden opgeslagen, wat een soortgelijk niveau van flexibiliteit voor het opslaan van stijlen in databasebronnen verschaft als eerder alleen beschikbaar was voor de stijlindelingen QML en SLD.

![image15](images/entries/0bd238b2326485fe91d8dd6f2aa8956e5534a5e3.webp)

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
## Labelen
### Mogelijkheid: Data-bepaald beheer over ankertype voor lijnen toestaan
Allows data-defined control over whether the \'hint\' or \'strict\' anchoring type is used.

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Beheren van plaatsing anker voor label relatief aan tekstpositie
Er wordt nu een besturingselement verschaft om te definiëren welk gedeelte van de tekst (begin, midden, of einde) van labels van lijnen correspondeert met de ankerpositie die is gedefinieerd in de plaatsing van het label. Dit maakt meer precieze plaatsing van labels mogelijk, overeenkomstig specifieke vereisten, zoals het uitlijnen van het einde van de tekst van een label met een specifiek punt op een object lijn.

In eerdere uitgaven van QGIS zouden labels altijd worden gecentreerd op de ankerpositie van lijnen, tenzij het een gebogen label was, dat het begin van het label gebruikte voor het bepalen van de oriëntatie van het label.

A new option for \"Follow placement\" has also been added, which means that the text anchor will depend on the placement along line setting. This control attempts to determine the appropriate alignment option automatically according to the label placement on the feature and exhibits the following behaviors:
- Voor labels die zijn verankerd nabij het begin van de lijn (0-25%), de plaatsing van het anker zal het **begin** van de tekst van het label zijn
- Voor labels die zijn verankerd nabij het einde van de lijn (75-100%), de plaatsing van het anker zal het **einde** van de tekst van het label zijn
- Voor labels die zijn verankerd tussen de 25 en 75% zal de plaatsing van het anker het **midden** van de tekst van het label zijn

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com/slyr/)
### Mogelijkheid: Interactief labels voor gebogen lijn verplaatsen langs hun lijnobjecten
Placement of curved label text can now be manipulated by using the interactive \"Move Labels\" tool.

![image16](images/entries/31ad531d280be178c752850a8860a95f2b8c3bf2.gif)

Dit werd mogelijk gemaakt door Stadt Freiburg im Breisgau

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Renderen
### Mogelijkheid: WMS-provider opnieuw samplen
Volgend op de mogelijkheid van QGIS 3.24 om WMS rastertegels te converteren naar hoogtegegevens, is QGIS verder verbeterd door verschillende methoden voor opnieuw samplen op te nemen om renderen van artefacten in WMS DEM-bronnen te verminderen, zoals pixelvorming die wordt tegengekomen bij het renderen van schaduwen voor heuvels.

![image17](images/entries/60b9ae3354e9c6e2086986aee3b0828dc738187f.gif)

This feature was funded by [Maptiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Selectief masker vectoriseren
QGIS introduced a selective masking feature in [version 3.12](https://changelog.qgis.org/en/qgis/version/3.12/#selective-masking), however the implementation relied on the rasterization of the map products and made it unsuitable for some cartographic work.

Deze lang verwachte mogelijkheid implementeert selectief maskeren op een manier die van toepassing zijnde gemaskeerde of geclipte objecten vectoriseert indien mogelijk, wat vectoruitvoer van hoge kwaliteit voor SVG en PDF-kaarten die de mogelijkheden voor maskeren van QGIS gebruiken.

This is implemented in line with [QEP 186](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/186).

![image18](images/entries/c717fac5bdd68a9f803738c77a5637fc070823e0.webp)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## 3D-objecten
### Mogelijkheid: Ondersteuning voor transparantie voor 3D Phong-materiaal
Verschaft ondersteuning voor het renderen van semitransparante objecten in 3D. Een schuifbalk voor opaciteit wordt verschaft voor de widget voor materiaal van Phong, die standaard op 100% (volledig ondoorzichtig) staat.

![image19](images/entries/38a2c9b60971a3056d2749373b2153e59eb0b3e1.webp)

This feature was funded by [Swedish QGIS user group.](https://www.qgis.se/)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: 3D-kaarten erven instellingen voor terrein van project
Wanneer een nieuwe 3D-kaart in het project wordt gemaakt,  zal de kaart standaard dezelfde instellingen voor het terrein gebruiken als welke zijn gedefinieerd voor het project. Dit maakt het gemakkelijker 3D-kaarten te maken en te verwijderen, zonder elke keer hun instellingen voor het terrein opnieuw in te moeten stellen.

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: 2D en 3D-navigatie synchroniseren
A new \"Navigation sync\" setting for 3D map frames provides the ability to automatically synchronize the 2D main map canvas extent and the 3D viewport based on various navigation options.
- Optie 1: Wanneer de camera in de 3D-weergave wordt verplaatst, zal het bereik van het kaartvenster (2D) worden ingesteld op het bekeken gebied
- Optie 2: Elke wijziging in positie in het kaartvenster (2D) zal er in resulteren dat de oriëntatie van de 3D- verschoven om bij benadering hetzelfde bereik weer te geven uit het bovenaanzicht (positie Nadir-weergave)
- Optie 3: Een trapezoïde gebied dat het gezichtsveld vanuit het kaartframe van 3D weergeeft, zal in het kaartvenster (2D) worden getekend

Acties voor het snel in- en uitschakelen van deze opties zijn ook beschikbaar.

![image20](images/entries/9438a5861c6891d7123bdba4918fd4cd9da82343.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](http://www.lutraconsulting.co.uk)
### Feature: 3D-as in 3D-kaartviewer
Een 3D as-annotatie is toegevoegd aan de 3D-kaartviewer die het voor gebruikers mogelijk maakt hun zicht beter te oriënteren met hun gegevens.

Deze verschillende aanvullingen omvatten besturingselementen en opties voor:
- Weerheven van een as voor X/Y/Z of North/East/South/West gebruiken, gebaseerd on het Coördinaten ReferentieSysteem (CRS) voor het frame
- Weergeven van een per zijde gelabelde kubus in plaats van typische pijlen voor assen

![image21](images/entries/bc7d732eed29aa4c9cd5a3888d2b80262960f41a.gif)

This feature was developed by [benoitdm-oslandia](https://github.com/benoitdm-oslandia)
## Puntenwolken
### Mogelijkheid: Triangulatie voor puntenwolken in 3D-weergaven
QGIS kan nu lagen van puntenwolken renderen in de 3D-weergave als een vast oppervlak, die wordt verkregen door 2.5D-triangulatie.

Triangulatie wordt geconfigureerd met een keuzevak in de opties voor opmaak van 3D, en opties voor configuratie staan het uitsluiten van driehoeken die, door de gebruiker gedefinieerde, drempels voor breedte of hoogte overschrijden.

Deze triangulatie is beschikbaar voor alle 3D-stijlen voor renderen van puntenwolken, inclusief unieke kleur, kleurverloop, classificatie, en RGB.

![image22](images/entries/4b103066398ae065f4e3eb1e898356fceda8ef1d.webp)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://github.com/vcloarec)
### Mogelijkheid: Ondersteuning voor Cloud Optimized Point Clouds (COPC)
QGIS verschaft nu ondersteuning voor het lezen van Cloud Optimized Point Clouds uit lokale gegevensbronnen en die op afstand.

For more information on the COPC format, visit <https://copc.io/>.

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Puntenwolken filteren
Ondersteuning voor filteren is toegevoegd voor lagen van puntenwolken, inclusief een gereedschap voor grafische query. Met filterexpressies kunnen punten van puntenwolken, in zowel 2D- als 3D-kaartvensters, voorwaardelijk worden weergegeven, gebaseerd on xyz- en/of LAS-attributen.

![image23](images/entries/a86ac2e8e5f5f1dbdc9630e2b71d4e62686362d9.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Synchroniseren van stijl voor puntenwolk
A new \"Follow 2d renderer\" style for 3D point cloud symbology allows for a point cloud layer\'s 3D symbol to be kept in sync with its 2D counterpart. Any changes to the 2D symbology will be automatically applied to the 3D symbology.

![image12](images/entries/9fde94a418b67018b72ad7d0e71c01cf9bc19afa.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
### Mogelijkheid: Verbeteringen aan renderer voor classificaties
Geclassificeerde renderer voor punten wolken is ook verbeterd:
- Alleen klassen weergeven die in de gegevensset aanwezig zijn (in plaats van een hard gecodeerde lijst) & ook niet-standaard klassen weergeven
- Percentage van punten voor elke klasse weergeven
- Werkt ook voor andere attributen (aantal teruggeven, aantal teruggegeven, bron punt en enkele andere klassen)

![image55](images/entries/74d4c97f9c4d402e928893c88f331e9.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
## Afdruklay-outs
### Mogelijkheid: Instellingen voor lettertype van de voorwaardelijke opmaak van de laag toepassen op lay-out van attributentabellen
Eerder werden alleen de instellingen voor de kleur van het lettertype en achtergrondkleur van de regels voor de voorwaardelijke opmaak toegepast op attributentabellen in lay-outs. Aanvullende instellingen voor opmaak, zoals type lettertype, vet, cursief, doorhalen, en onderstrepen worden nu uit de regels voor voorwaardelijke opmaak toegepast.

![image24](images/entries/a15e95f80ef5f86dd2de37e4e1642984db89f8a9.gif)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Data-bepaalde 'override' voor schaalbalk
Voegt data-bepaalde 'overrides' toe aan het item voor de lay-out Schaalbalk. Deze mogelijkheid is nuttig bij het maken van een atlas waarbij het object van de atlas de schaal als een veld bevat. De kaart kan door deze waarde worden aangedreven, maar niet de schaalbalk. Dit implementeert #48084, wat het mogelijk maakt eigenschappen van de schaalbalk data-aangedreven te laten worden door het object van de atlas.

![image56](images/entries/d3e680f3e4facc9078e4755045152d57f7dc680f.webp)

This feature was developed by [Ethan Snyder](https://github.com/esnyder-rve)
## Expressies
### Mogelijkheid: Operatoren Between/Not between
QGIS now includes support for SQL-like `BETWEEN` and `NOT BETWEEN` operators in expression clauses.

![image25](images/entries/01fbc5c6454d48b126daa9597332ca8e94811608.gif)

Dit werd mogelijk gemaakt door Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Statische ouder-variabele in functies aggregate voor expressies
In eerdere uitgaven van QGIS gaven expressies voor aggregate niet de parameters van het ouder-object door als statische variabelen, wat verhinderde dat die werden uitgevoerd door de gegevensprovider (bijv. PostgreSQL). Deze wijziging zal resulteren in significante verhoging van de uitvoering van een aantal expressies voor aggregate. Bijvoorbeeld in de expressie voor aggregate:

`IF(aggregate(layer:='parks',aggregate:='count', expression:= 't_id', filter:=intersects( $geometry, geometry(@parent))) < 1, 'FALSE', 'TRUE')`

The execution of the `intersects( $geometry, geometry(@parent))` filter will be performed on the data provider directly.

This feature was funded by [Amt für Geoinformation Kanton Schaffhausen](https://agi.sh.ch)

This feature was developed by [David Signer](https://github.com/signedav)
## Digitaliseren
### Mogelijkheid: Keuzevak toegevoegd om gedrag voor automatisch openen van dock van Gereedschap Punten uit te schakelen
The vertex tool dock now has a new checkbox for \"Auto-open table\", which is checked by default and retains the existing behavior.

Als een gebruiker er voor kiest om dit uit te schakelen, dan zal het gedrag voor het automatisch openen/sluiten van het dock voor de Puntenbewerker worden uitgeschakeld, wat het dock instelt als een normaal dock voor QGIS dat zich hetzelfde gedraagt als elk ander dock.

Dit is gewenst in situaties waar:
- The user is editing in a full screen session with docks hidden, and doesn\'t want the vertex editor dock to keep opening itself
- The user has a heavily customized setup of stacked/tabbed/rearranged docks, and doesn\'t want the vertex editor dock to keep appearing and disappearing and causing other docks to be rearranged

If a user has opted out of the auto-open table behavior, then the dock can be closed and won\'t show immediately when switching to the vertex tool. The dock can then be re-opened either through the standard Views - Panels menu (or by right clicking a toolbar), OR through a new \"Show Vertex Editor\" action which has been added to the dropdown menu for the vertex editor toolbar button.

![image26](images/entries/b8569c513e1dffa0fabb253e8074588d44cce5eb.gif)

Dit werd mogelijk gemaakt door SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Kaartgereedschap voor vormen geïntegreerd in de mogelijkheid Digitaliseren
De gereedschappen voor vormen zijn uitgebreid en geïntegreerd met de mogelijkheden uit de gereedschappen voor Digitaliseren, wat het mogelijk maakt de kaartgereedschappen te gebruiken voor bewerkingen van Digitaliseren.

Dit omvat ondersteuning voor digitaliseren van items zoals:
- StraightSegments
- CircularStrings
- Streaming
- Vormen

Dit resulteert in de mogelijkheid om de bewerkingen voor digitaliseren Deel toevoegen, Ring toevoegen, of enige andere bewerking voor digitaliseren te gebruiken met de gereedschappen voor vormen voor hybride bewerkingen voor digitaliseren, bijvoorbeeld de gereedschappen voor cirkeltekenreeks of rechthoek gebruiken om ringen te maken in bestaande objecten gebied.

This required significant refactoring and the porting of code from `QgsMapToolDigitizeFeature` to `QgsMapToolCapture`.

![image27](images/entries/c0a8faef50107305ea8a04e92f68f9d7518507ff.gif)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
### Mogelijkheid: Nieuwe beperkingen voor paneel Geavanceerd digitaliseren
Het paneel Geavanceerd digitaliseren bevat nu twee aanvullende zachte beperkingen (lijnen voor snappen) om het voor gebruikers mogelijk te maken posities vast te leggen, relatief ten opzichte van bestaande objecten. Deze beperkingen worden optioneel ingeschakeld en omvatten:
- **Lijn verlengen**: QGIS zal een beperking verschaffen die de verlening van een lijn traceert, gebaseerd op de oriëntatie van het segment, gedefinieerd door het geselecteerde punt
- **X/Y-punt**: QGIS zal een beperking verschaffen die loodrecht staat op een bestaand punt in verticale of horizontale oriëntatie.

![image28](images/entries/4a68cb3c6e9a4f55c5f95ca4b827405ce0aed526.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
## Gegevensbeheer
### Feature: Add a \"filter rules\" search box to vector tile renderer and labeling widgets
Gebruikers kunnen nu de zichtbare regels filteren op een gedeelte van tekenreeksen van hun label, laag of filter. Dit kan enorm helpen bij het zoeken naar regels in complexe stijlen voor vectortegels.

![image29](images/entries/1cb1d1557bac8d4552a3ef617a27e0fcf9c082ff.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Namen van door gebruiker gedefinieerde velden in export
Gebruikers kunnen nu de veldnamen in de resulterende lagen overschrijven bij het exporteren van lagen.

De interface van het dialoogvenster voor het exporteren van velden bevat de volgende wijzigingen:
- A new \"Export names\" column has been introduced to the fields table
- Een handig keuzevak wordt verschaft voor het automatisch maken van aliassen, of terug te gaan naar de originele veldnamen
- When field names are modified by the user, the checkbox will display a \"PartiallyChecked\" state indicator

![image30](images/entries/77669a9cc8355f9fae0e331a28de7ace46e730d6.gif)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
### Mogelijkheid: Vectorlagen voorzien van geoverwijzingen in Georeferencer
QGIS ondersteunt nu het maken van geoverwijzingen  in vectorlagen in het gereedschap Georeferencer. Dit maakt het mogelijk dat vectorlagen zonder ruimtelijke verwijzing interactief worden voorzien van geoverwijzingen, of dat lagen zonder verwijzingen opnieuw worden voorzien van geoverwijzingen op een soortgelijke manier als voor rastergegevens. Geoverwijzingen maken gebeurt in een taak, dus QGIS zou bereikbaar moeten blijven, zelfs met grote gegevenssets.

Based on [#41386](https://github.com/qgis/QGIS/pull/41386)

![image31](images/entries/b6e89fcd31aec118497af05f94586d2bbf6f4491.gif)

Dit werd mogelijk gemaakt door de Deense QGIS gebruikersgroep.

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Mogelijkheid voor beheren van velddomein voor Browser
Een nieuwe API is toegevoegd voor het beheren van velddomeinen via verbindingen met databases, en QGIS geeft deze functionaliteit weer in het paneel Browser.

Deze functionaliteit wordt momenteel alleen weergegeven voor GeoPackages, maar ondersteuning voor andere providers zou in de toekomst ook potentieel weergegeven kunnen worden.

Opgenomen in deze functionaliteit is de mogelijkheid om nieuwe velddomeinen te maken, als ook het instellen van het velddomein voor GeoPackage tabelvelden.

![image32](images/entries/e5f0feb4e3c4d925c98336d8938170ac9bb9fc1c.gif)

Dit werd mogelijk gemaakt door Provincie Gelderland

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Gebufferd transactioneel bewerken
Met deze modus voor bewerken worden alle bewerkbare lagen synchroon geschakeld en alle bewerkingen worden opgeslagen in een lokale bewerkingsbuffer. Opslaan van wijzigingen wordt uitgevoerd in één enkele transactie op alle lagen (per provider).

This new edit mode attempts to provide a hybrid alternative for managing the data editing approaches used in the current editing modes, local edit buffers and transactional editing, and is implemented in line with [QEP 203](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/203)

![image33](images/entries/c7c3eea32a0cf34a07a9325fd87fdefcf8afb280.webp)

Dit werd mogelijk gemaakt door Kanton Glarus

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Formulieren en widgets
### Mogelijkheid: Toegang tot verwijzing formulier in Python acties voor formulieren
The form instance, or `QgsAttributeForm` object, has now been exposed to the Python API for Drag and drop form actions.

Dit betekent dat gebruikers van QGIS nu kunnen verwijzen naar het huidige formulier en acties kunnen produceren die waarden in het formulier zelf wijzigen, zoals het herstellen van standaardwaarden of snelle acties voor het toepassen van andere door de gebruiker gedefinieerde voorkeuzen.

This implementation has been done in line with [QEP 251](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/251)

![image34](images/entries/8f71244038218dae15182ee507699de0050b405d.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Aanpassen van lettertype en kleur van labels van formulieren Slepen en neerzetten toestaan
Het lettertype en kleur van labels van formulieren en groepen of titels van tabs kunnen nu worden aangepast in de interface van de ontwerper Slepen en neerzetten.

![image35](images/entries/df03bff457eac65712cad54d0acee177526a3f13.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Groep uit formulier samenvouwen met expressie
Nieuwe opties voor configuratie zijn nu beschikbaar voor groepsvakken van formulieren van Slepen en neerzetten, die het mogelijk maken een expressie te specificeren die definieert of een groep uit het formulier zou moeten worden samengevouwen.

![image36](images/entries/d601af9dff97189a63c0c9d7125ad9d50de3ff66.webp)

Dit werd mogelijk gemaakt door ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Analyse-gereedschappen
### Feature: \"Keep disjoint features separate\" option for dissolve algorithm
A \"Keep disjoint features separate\" option has been added for the dissolve algorithm which will cause features and parts that do not overlap or touch to be exported as separate features instead of parts of a single multipart feature. This makes it much simpler to perform simple aggregation based dissolves on a single class.

![image37](images/entries/350b223b3d7b647643338f57158c2b139df11f87.webp)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Processing
### Mogelijkheid: Bericht weergeven voor gereedschap Model
Een algoritme voor het weergeven van een bericht is toegevoegd aan de gereedschappen voor modellen, dat het voor gebruikers mogelijk maakt aanvullende informatie uit te voeren in logs van modellen. Dit voorkomt het misbruiken van de algoritmes raise error/warning en verschaft meer fijnmazig beheer voor de niveaus van het loggen van modellen.

![image38](images/entries/e2433bb4fe23b076129ea4accd516e3b7939d64f.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Uitvoeren van batch-processing in stappen in taken
Individuele stappen uit het dialoogvenster voor batch-processing kunnen nu, indien mogelijk, worden uitgevoerd als een afzonderlijke taak. Hoewel individuele stappen nog steeds in reeks worden uitgevoerd in plaats van parallel, houdt dit de gebruikersinterface bereikbaar, en staat tussentijds annuleren en van de voortgang toe.

Dit werd mogelijk gemaakt door NRCan Contract#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Op achtergrond verwerken van algoritmes voor modellen
Eerder werden grafische modellen, ontworpen in Processing, gedwongen om te worden uitgevoerd op de hoofdthread, en ondersteunden geen uitvoering op de achtergrond. QGIS ondersteunt nu het uitvoeren van algoritmes voor modellen anders dan via de hoofdthread, zodat zij veilig kunnen worden uitgevoerd in taken op de achtergrond.

Dit werd mogelijk gemaakt door NRCan Contract#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Instellen Voorbeelden in Help van Grafische modellen toestaan
A new \'Examples\' section has been added to the graphical model help editor dialog, allowing users to enter their own custom examples to help explain usage of the model.

More instructive help is now shown for models in the qgis_process tool, including outputting any example help which has been set.

![image39](images/entries/64e788f716481fbb085a0ba70e8cc4f2333ad744.gif)

Dit werd mogelijk gemaakt door NRCan Contract#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Gereedschappen voor overleggen met ondersteuning voor overleggen met meerdere lagen
Adds new Intersect, Union and Difference tools which support multiple \"overlay\" inputs instead of a single overlay layer. The current workflow includes selecting the order of overlay layers used in the operation, which are used in an iterative process by using the output of an operation between two layers as an input for the same operation with the next layer.

Dit is een nuttige abstractie die in verschillende scenario's kan worden gebruikt, zoals het verwerken van modellen waarin iteratieve processen of doorlopen kunnen worden beperkt.

![image40](images/entries/419403e295be2748e89100cb31117685b151e409.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Opties voor toepassing en projecten
### Mogelijkheid: Framewerk voor eigenschappen van hoogte in project
Elevation/terrain settings are now project-level settings, which are defined through the Project Properties, Terrain tab, in line with [QEP 246](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/246) and in order to support the new elevation profile tools.

Dit framewerk verschaft de volgende opties voor het configureren van:
- **Vlak terrein** met een te configureren instelling voor de terreinhoogte
- **DEM (Rasterlaag)** met instelling voor het definiëren van de bron-rasterlaag, verticale schaal en verschuiving
- **Mazen** met instellingen voor het definiëren van de bronlaag met mazen, verticale schaal en verschuiving

![image41](images/entries/c58fa193b00b77b743b17b9ef50336f1b13d1b9f.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Optioneel opslaan van configuratie gebruikersinterface in projecten
An opt-in setting for projects has been added for \"Remember attribute table windows and docks between sessions\". If checked for a project, then any opened attribute tables will be saved into the project and immediately restored when loading that project.

Dit is ontworpen om werkstromen te verbeteren waar gebruikers een project hebben gemaakt met een bepaalde set van configuraties voor attributentabellen voor hun wensen, en het opnieuw instellen van deze attributentabellen een heel gedoe is.

![image42](images/entries/a9b8aad7c60417bb1d7a811da40af7a1b763efbe.gif)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Optioneel opslaan van status van bewerken van de laag in projecten
An opt-in setting has been added to project properties for \"Remember editable layer status between sessions\". If checked, then any layers which are editable will be remembered when saving that project and immediately made editable whenever the project is restored to make it simpler for users who are making complex, data-editing focused projects to store their configurations on a project by project basis.

![image43](images/entries/04bf91d7cd37549d0949e2d3c67be6e7a809a3a5.webp)

Dit werd mogelijk gemaakt door City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor stijldatabase project
Een nieuwe mogelijkheid stelt gebruikers in staat een lijst in te stellen van QGIS stijldatabases voor een project. Dit stelt projecten in staat te koppelen aan meerdere stijldatabases, en dan alle symbolen en entiteiten uit die databases weer te geven in de interface voor het opmaken van de laag.

De paden voor de stijl mogen verwijzen naar stijl .db-databases of exports van .xml. Wanneer een project is geladen, zullen symbool en label stijlselecties ALLE symbolen weergeven uit ALLE stijlen die zijn gekoppeld aan het project. Aanvullend heeft elk project nu een projectspecifieke stijldatabase (die naast het project wordt opgeslagen), voor het opslaan van projectspecifieke symbolen, tekstindelingen, etc.

**Deze functionaliteit vereist een bouw van QGIS die gebaseerd is op Qt 5.13 of later, en is verborgen op oudere bouwsels (bijv. op Ubuntu 20.04)**

![image44](images/entries/6172a0a8196db373e0eac8edbcbf790ae9532ba8.webp)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Toegevoegde instelling om standaard het aantal objecten weer te geven voor nieuw toegevoegde lagen
Indien ingeschakeld zal deze optie er voor zorgen dat het weergeven van het aantal objecten voor nieuw toegevoegde/gemaakte lage is ingeschakeld. Deze instelling zal standaard zijn uitgeschakeld.

![image45](images/entries/3706248ef1ca50af9877d04df93d6f3455bce9ca.webp)

Dit werd mogelijk gemaakt door SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Add a \"Skip\" option for custom environmental variables
The QGIS settings allow a particular user profile to modify the system environment variables for enhanced flexibility, in Settings \--\> Options \--\> Environment.

This functionality included options for \"Overwrite\", \"If Undefined\", \"Unset\", \"Prepend\", and \"Append\", which allowed users to perform various functions from configuring credentials to extending their PATH variables.

A new \"Skip\" option is now provided which allows users to ignore values from an existing field, without losing the stored values or having to remove them from the settings to disable them.

![image46](images/entries/31251db3a673149dcd900737dd9aada0fafb93ff.gif)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Revamped projects\' default symbols, color ramp, and text format
Deze nieuwe versie van QGIS heeft de manier waarop de standaard symbolen voor projecten worden afgehandeld opnieuw vorm gegeven, gericht op het upgraden van zijn UI/UX als ook om zich correct te gedragen in omgevingen met meerdere gebruikers. De wijzigingen omvatten:
- Projects\' default symbols and color ramps are now stored as symbology XML rather than references, improving portability and integration with external applications and services
- Een nieuwe instelling op projectniveau voor standaard tekstindeling is toegevoegd om gebruiker gedefinieerde configuratie van het standaard lettertype voor het project voor nieuw toegevoegde vectorlagen toe te staan
- The user interface has been upgraded to make use of QGIS\' symbol and color ramp buttons

![image47](images/entries/5fca0da47e4af53c46a12dcd5b68a1982afff16b.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Profiel plotten
### Mogelijkheid: Gereedschap voor plotten van hoogteprofielen
QGIS bevat nu een eigen gereedschap voor het plotten van hoogteprofielen

Het gereedschap omvat de volgende mogelijkheden:
- Support for vector, raster, mesh, and point cloud layers, based on the corresponding layer\'s elevation settings.
- Interactief profiellijnen teken met een kaartgereedschap, dat snappen, traceren, digitaliseren van stromen en bogen ondersteunt
- Uitkiezen van een bestaand object lijn om als de profiellijn te gebruiken. Wanneer dit gereedschap actief is, kunnen gebruikers klikken op elk object lijn op de kaart om een profielboog langs die lijn te maken. Indien meerdere objecten aanwezig zijn op het aangeklikte punt zal een pop-upmenu verschijnen dat gebruikers de kans geeft te kiezen uit de beschikbare objecten.
- Plots kunnen worden geëxporteerd naar PDF (als hoge kwaliteit vectorobjecten) of verschillende indelingen voor afbeeldingen
- Profielen worden gerenderd met standaard QGIS lijnsymbolen, en bevatten zo ondersteuning voor geavanceerd ontwerpen en configuratie, inclusief ondersteuning voor geometrie-generatoren en tekeneffecten.
- Meten van afstanden op de plots
- Identificeren van objecten in het plot via ofwel één enkele klik, of klik-en-sleep rechthoek. Resultaten worden weergegeven in het standaard dock Identificatieresultaten, en ondersteunen vector-, raster-, lagen met mazen, en puntenwolken.

Interactieve navigatie van het kaartvenster van het plot wordt ondersteund met de standaard sneltoetsen van QGIS voor verschuiven/zoomen, zoals:
- Middelste muisknop: Verschuiven
- Spatiebalk: Verschuiven
- Ctrl + Spatiebalk: Zoomen
- Ctrl + muiswiel: Fijn zoomen

Shortcuts are available for nudging the elevation profile curve left and right, which allows users to \"scrub\" the curve across the map frame and find the optimal profile line. The step distance is set to match the chart\'s tolerance distance, so that a single step will result in a different set of point and point cloud features shown in the chart.

Sneltoetsen voor het toetsenbord voor aanstoten zijn:
- Ctrl+Alt+,: Schrobben naar links
- Ctrl+Alt+.: Schrobben naar rechts

For more information on this awesome feature and framework, be sure to watch the [QGIS Elevation Profiles Deep Dive](https://www.youtube.com/watch?v=AknJjNPystU) presentation on YouTube.

![image48](images/entries/6c530f4bfd565313f515ae9f6a79662d1682bfc7.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Flexibele symbologie voor vectorlagen in hoogteprofielen
Vectorlagen die zijn toegevoegd aan het profieldiagram zullen standaard hun symbologie voor de laag respecteren. Een keuzevak is in de eigenschappen voor de hoogte van de laag toegevoegd om dit uit te schakelen.

Dit betekent dat vectorresultaten in diagrammen voor hoogteprofielen standaard hun objecten weergeven met hun corresponderende renderer 2D, dus aangepaste stijlen, zoals gecategoriseerde klassen, zullen standaard zichtbaar zijn in het profieldiagram.

There\'s also options to change the interpretation of the elevation profile for vector layers. By default, the elevation profile tool will use an \"individual features\" option, which samples discrete positions where the cross section profile line intersects the vector features. There\'s also a \"continuous surface\" option which will generate an interpretation of the surface by interpolating across the sample positions for enhanced visualization, such as the production of a continuous surface line from contour lines or surveyed elevation points.

Additional rendering capabilities are provided for the \"continuous surface\" interpretation option, such as a \"fill below\" symbol style. This can be easier to interpret in some cases, and helps match expected symbology conventions in certain disciplines.

![image49](images/entries/50ff18ed7962a0fbc09ca17f3b0688db6ed33bd3.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Flexibele symbologie voor plotten van profielen van puntenwolken
Lagen van puntenwolken in profieldiagrammen bevatten de volgende mogelijkheden voor symbologie:
- Weergave in een enkele kleur van punten of een instelling om de classificatie te erven en kleuren vanuit de 2D-symbologie (bijv. RGB-kleuren)
- Instelling voor het respecteren van de tolerantie voor de afstand van de profielboog
- Optie om de opaciteit te reduceren van punten  die verder van de profielboog liggen
- Automatisch verfijnen, gebaseerd op het zichtbare gebied van het plot en schaal, met een door de gebruiker te beheren maximale schermfout
- Beheer over uiterlijk van punten (kleur, grootte en vorm)

![image50](images/entries/c8cf49088468d798190f56a32c0e6c6d1cefe72f.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Uittrekken van vectorobjecten voor profieldiagrammen
Het gereedschap voor hoogteprofielen ondersteunt het uittrekken voor vectorobjecten en het verschuiven van hoogten voor het inpassen van 2D-vector in profieldiagrammen. Deze eigenschappen mogen data-bepaald zijn, en zullen ook worden gebruikt als de standaard instellingen voor verschuiving/uittrekken voor alle nieuwe 3D-polygoonsymbolen die voor die laag zijn gemaakt.

![image51](images/entries/3bfe2bcf8051167fd7729ef3c5a2a4f5249f823b.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Browser
### Mogelijkheid: Beheer contextmenu voor hernoemen groepen Favoriete plaatsen
Creating new spatial bookmarks from the browser will now default to the \"project bookmark\" category, and a new context menu option has been added for renaming of bookmark groups. The existing behavior of renaming bookmark groups using the F2 key remains unchanged.

![image52](images/entries/79d5021866775b2eb429eb60c96f697ac0c6af49.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor het direct lezen van bestanden van ESRI vectortegelpakketten (.vtpk)
ESRI vectortegelpakketten (bestanden VTPK) kunnen nu direct worden geopend als vectortegellagen via slepen en neerzetten, inclusief ondersteuning voor het vertalen van de stijl.

This feature was funded by [North Road Consulting, thanks to SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Mogelijkheid: Loggen van SQL in paneel Debuggen/Ontwikkeling
Het paneel Debuggen/ontwikkeling bevat nu ondersteuning voor het loggen van query's van SQL gemaakt door QGIS voor achterliggende gegevensproviders.

Dit verschaft een effectieve methode voor het debuggen van algoritmes en gegevensproviders, als ook het vastleggen van de argumenten voor SQL die worden gemaakt voor het uitvoeren van specifieke acties voor bepaalde providers.

Onthoud dat dit specifiek is ontworpen voor de gereedschappen voor debuggen en ontwikkeling en niet is ontworpen als vervanging voor welke mogelijkheden voor loggen op de achterliggende databasesystemen dan ook.

This has been implemented in line with [QEP 242](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/242).

![image53](images/entries/62594ee3295e3276fe9510f42e2ba54d05153ebd.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## QGIS Server
### Mogelijkheid: Alternatieve periodieke controlestrategie voor het detecteren van updates voor het project
QGIS Server verschaft nu een alternatieve strategie lastModified() voor het ongeldig maken van de interne projectcache, wat bedenkingen adresseert over de mogelijkheid van QGIS server om de cache ongeldig te maken wanneer een projectbestand is bijgewerkt op atypische bestandssystemen, zoals NFS, or wanneer het projectbestand is opgeslagen in een databasesysteem als PostgreSQL.

Een asynchrone periodieke controlestrategie met de laatste aangepaste waarde van een project wordt nu verschaft voor het controleren  op wijzigingen van de configuratie van het project.

The `QGIS_SERVER_PROJECT_CACHE_STRATEGY` environment variable may be used to configure the server caching strategy using the following values:
- `periodic` for the alternative strategy
- `filesystem` to use the file system watcher strategy
- `off` to disable internal caching completely.

`QGIS_SERVER_PROJECT_CACHE_CHECK_INTERVAL` is used for controlling the periodic strategy interval.

The `QFileSystemWatcher` strategy remains the default configuration.

This feature was funded by [3Liz](https://3liz.com)

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Mogelijkheid: Meer server parameters voor accentueren van labels toegevoegd
Nieuwe parameters zijn toegevoegd voor het beter plaatsen van geaccentueerde labels op de WMS server, inclusief:
- `HIGHLIGHT_LABELDISTANCE`: Distance between the feature and the label, defined in mm
- `HIGHLIGHT_LABELROTATION`: Label rotation, defined in degrees
- `HIGHLIGHT_LABELVALI`: Vertical alignment for placing the label directly on a point
- `HIGHLIGHT_LABELHALI`: Horizontal alignment for placing the label directly on a point

This feature was developed by [mhugent](https://github.com/mhugent)
### Mogelijkheid: Ondersteuning voor eigenschappen van Tijdbeheer voor WMS Server
Eerdere uitgaven van QGIS Server verschaften alleen ondersteuning voor de dimensies van tijd en hoogte voor vectorlagen en verschaften geen integratie met de bijgewerkte API voor eigenschappen van Tijdbeheer, verschaft door QGIS.

QGIS Server has now been extended to support the time dimension in the `GetCapabilities` response for WMS services, and accept a `TIME` query string parameter which provides capacity for temporal data filtering.

Parsen van tijd waarden zal worden uitgevoerd met de specificatie voor de implementatie die is verschaft door de OGC API - Features (OAPIF) en gebruikt de volgende structuur:

\| interval\| syntax \| \|\-\--\|\-\--\| \| interval-closed \| date-time \"/\" date-time \| \| interval-open-start \| \[\"..\"\] \"/\" date-time \| \| interval-open-end \| date-time \"/\" \[\"..\"\] \| \| interval \| interval-closed / interval-open-start / interval-open-end \| \| datetime \| date-time / interval \|

Onthoud dat dit filteren alleen van toepassing is op enkele waarden, en een lijst van instanties of bereiken wordt momenteel niet ondersteund.

To prevent conflict with existing TIME dimension stipulations on legacy projects, if a `TIME` dimension was explicitly defined for a vector layer, the temporal properties for that layer will not be activated and the explicitly set `TIME` dimension will be considered instead.

Dit werd mogelijk gemaakt door Gis3W

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Programmeerbaarheid
### Mogelijkheid: Een functie QgsScaleCalculator toegevoegd om de breedte van het kaartvenster te berekenen vanuit een opgegeven bereik, schaal en DPI
A new `calculateCanvasWidth( extent, scale )` was added to the `QgsScaleCalculator` class to derive canvas width in pixel unit when providing an extent, a scale, and a DPI.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Huidige actie voor symbool leegmaken in widget knop Symbool
Een actie instellen op null / huidige symbool leegmaken is toegevoegd om het huidige symbool leeg te maken voor een widget knop Symbool.

![image54](images/entries/e7c6ed595485dd51c3bccb87f2a31f9691ad4aae.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Belangrijke reparaties
### Reparaties van problemen door Even Rouault
| Titel probleem | URL Issues (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| WFS provider doesn\'t recognize CRS strings other than OGC URNs | [#46485](https://github.com/qgis/QGIS/issues/46485) | [PR #48550](https://github.com/qgis/QGIS/pull/48550) | N/B |
| QgsMapCanvas::showEvent access violation / QGIS crash | [#48438](https://github.com/qgis/QGIS/issues/48438) | [PR #48551](https://github.com/qgis/QGIS/pull/48551) | [PR #48558](https://github.com/qgis/QGIS/pull/48558) |
| \[GDAL provider\] Minimal support for GDT_Int64/GDT_UInt64 of GDAL 3.5.0 | (niet gerapporteerd) | [PR #48553](https://github.com/qgis/QGIS/pull/48553) |  |
| access to QgsRubberBand-methods crashes QGis | [#48471](https://github.com/qgis/QGIS/issues/48471) | [PR #48554](https://github.com/qgis/QGIS/pull/48554) | [PR #48561](https://github.com/qgis/QGIS/pull/48561) |
| annotationManager with access to canvas-items crashes QGis | [#48436](https://github.com/qgis/QGIS/issues/48436) | [PR #48554](https://github.com/qgis/QGIS/pull/48554) | [PR #48561](https://github.com/qgis/QGIS/pull/48561) |
| Can not import excel File with new version of QGIS | [#47838](https://github.com/qgis/QGIS/issues/47838) | N/B - probleem van freexl. Patch ingediend bij upstream | N/B |
| Layers added by QGIS are not correct if datasource is a collection | [#47610](https://github.com/qgis/QGIS/issues/47610) | [PR #48556](https://github.com/qgis/QGIS/pull/48556) | [PR #48572](https://github.com/qgis/QGIS/pull/48572) |
| SQLite: No Spatial Index Creation though QGIS misleadingly reports success | [#44513](https://github.com/qgis/QGIS/issues/44513) | [PR #48557](https://github.com/qgis/QGIS/pull/48557) | [PR #48565](https://github.com/qgis/QGIS/pull/48565) |
| Saving a large edited point layer takes far too long | [#46355](https://github.com/qgis/QGIS/issues/46355) | [GDAL PR 5730](https://github.com/OSGeo/gdal/pull/5730) | [GDAL PR 5753](https://github.com/OSGeo/gdal/pull/5753) |
| Non-existent but registered attribute table in GPKG is added as empty table | [#30670](https://github.com/qgis/QGIS/issues/30670) | [GDAL PR 5752](https://github.com/OSGeo/gdal/pull/5752) | Niet van toepassing |
| Accents displayed incorrectly when saving metadata to geopackage | [#47435](https://github.com/qgis/QGIS/issues/47435) | [PR #48625](https://github.com/qgis/QGIS/pull/48625) | [PR #48631](https://github.com/qgis/QGIS/pull/48631) |
| Raster tiles are clipped based on the gpkg_contents bounding box of a GeoPackage | [#45530](https://github.com/qgis/QGIS/issues/45530) | Is geen probleem |  |
| Pan-action freeze after use of middle mouse button and \'copy coordinate\' | [#48645](https://github.com/qgis/QGIS/issues/48645) | [PR #48666](https://github.com/qgis/QGIS/pull/48666) | [PR #48684](https://github.com/qgis/QGIS/pull/48684) |
| New GeoPackage layer cannot be loaded (QGIS thinks it\'s invalid but it isn\'t really) | [#48671](https://github.com/qgis/QGIS/issues/48671) | [PR #48692](https://github.com/qgis/QGIS/pull/48692) | [PR #48774](https://github.com/qgis/QGIS/pull/48774) |
| \[regression\] New filter for duplicated WFS layer is also applied on source layer | [#48465](https://github.com/qgis/QGIS/issues/48465) | [PR #48998](https://github.com/qgis/QGIS/pull/48998) | N/B |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL Issues (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| \@project_keywords are no longer tested on Rule based filters | [#48480](https://github.com/qgis/QGIS/issues/48480) | Is geen probleem |  |
| No more styles after duplicate layer and change filter in query builder in 3.22.6 | [#48467](https://github.com/qgis/QGIS/issues/48467) | Werkt bij mij op 3.24.2 en master |  |
| MSSQL Add Connection Dialog never enables OK button | [#48462](https://github.com/qgis/QGIS/issues/48462) | Werkt bij mij op master |  |
| Highlight of identified feature not displaying correctly on \"geometry generator\" marker from different CRS | [#48439](https://github.com/qgis/QGIS/issues/48439) | [PR #48579](https://github.com/qgis/QGIS/pull/48579) | NOG TE DOEN |
| Cannot past copied features as temporary scratch layer | [#48401](https://github.com/qgis/QGIS/issues/48401) | [PR #48611](https://github.com/qgis/QGIS/pull/48611) | NOG TE DOEN |
| QGIS crash by opening a form with relation content | [#48443](https://github.com/qgis/QGIS/issues/48443) | [PR #48616](https://github.com/qgis/QGIS/pull/48616) | NOG TE DOEN |
| Relation reference widget: filter expression does not work with variables | [#48190](https://github.com/qgis/QGIS/issues/48190) | [PR #48619](https://github.com/qgis/QGIS/pull/48619) | NOG TE DOEN |
| Random order of attributes in oracle feature query | [#35309](https://github.com/qgis/QGIS/issues/35309) | [PR #48668](https://github.com/qgis/QGIS/pull/48668) | nee |
| CSV datasource not converted from 3.16 to 3.22 correctly - projects not usable anymore | [#48587](https://github.com/qgis/QGIS/issues/48587) | Werkt bij mij op 3.24 en master |  |
| Documentation doctest failure | [QGIS developer mail list](https://lists.osgeo.org/pipermail/qgis-developer/2022-May/064720.html) | [QGIS Documentation PR 7581](https://github.com/qgis/QGIS-Documentation/pull/7581) | nee |
| \"Add to group\" option in sub layer window always add at top of layer tree | [#48694](https://github.com/qgis/QGIS/issues/48694) | [PR #48696](https://github.com/qgis/QGIS/pull/48696) | nee |
| Name/id of map objects in GetProjectSettings follows an order that is the inverse of the order used to add the map objects in a layout | [#46143](https://github.com/qgis/QGIS/issues/46143) | [PR #48728](https://github.com/qgis/QGIS/pull/48728) | nee |
| Aborted inserts in Postgis geometryless tables are saved anyway | [#48171](https://github.com/qgis/QGIS/issues/48171) | [PR #48741](https://github.com/qgis/QGIS/pull/48741) | nee |
| Inconsistent coordinate rounding in Raster \"Layer Properties\" | [#48767](https://github.com/qgis/QGIS/issues/48767) | [PR #48790](https://github.com/qgis/QGIS/pull/48790) | NOG TE DOEN |
| Drag and Drop Postgis-Table in QGIS Browser alters name of Geometry-Column | [#48748](https://github.com/qgis/QGIS/issues/48748) | [PR #48796](https://github.com/qgis/QGIS/pull/48796) | nee |
| Layer filter does not work on multiline strings values with linebreaks | [#47530](https://github.com/qgis/QGIS/issues/47530) | [PR #48818](https://github.com/qgis/QGIS/pull/48818) | niet nodig |
| QGIS Crashes while searching in the expression builder | [#48189](https://github.com/qgis/QGIS/issues/48189) | [PR #48856](https://github.com/qgis/QGIS/pull/48856) | [PR #48864](https://github.com/qgis/QGIS/pull/48864) |
| Server GetPrint with multiple maps following map themes apply prefixed LAYERS (map0:LAYERS) to all maps | [PR #48923](https://github.com/qgis/QGIS/pull/48923) | [PR #48923](https://github.com/qgis/QGIS/pull/48923) | NOG TE DOEN |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Deze problemen werden opgelost door Alex Bruy
| Titel probleem | URL Issues (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingParameterMultipleLayers adds an extra list element when reordering inputs | [#45634](https://github.com/qgis/QGIS/issues/45634) | Werkt bij mij op 3.24 en master |  |
| GDAL Vector to Raster (gdal_rasterize) fail to produce ESRI ASCII as output | [#39140](https://github.com/qgis/QGIS/issues/39140) | Is geen probleem |  |
| Processing: Drape / qgis:setzfromraster inconsistent NODATA behaviour | [#43650](https://github.com/qgis/QGIS/issues/43650) | Werkt bij mij op master |  |
| Algorithm output node is placed half outsize model canvas | [#48132](https://github.com/qgis/QGIS/issues/48132) | [PR #48600](https://github.com/qgis/QGIS/pull/48600) | [PR #48661](https://github.com/qgis/QGIS/pull/48661) |
| Inconsequence in CRS-names/id\'s in Copy Coordinate in MapCanvas | [#37226](https://github.com/qgis/QGIS/issues/37226) | [PR #48599](https://github.com/qgis/QGIS/pull/48599) |  |
| QGIS Batch Mode Populating Form are producing gaps between rows | [#43869](https://github.com/qgis/QGIS/issues/43869) | [PR #48601](https://github.com/qgis/QGIS/pull/48601) | [PR #48636](https://github.com/qgis/QGIS/pull/48636) |
| Processing settings dialog cleared after a search is done in Settings dialog | [#34543](https://github.com/qgis/QGIS/issues/34543) | [PR #48602](https://github.com/qgis/QGIS/pull/48602) | [PR #48633](https://github.com/qgis/QGIS/pull/48633) |
| QgsProcessingAlgorithm with FlagHideFromModeler flag is still visible in the Model Designer | [#48586](https://github.com/qgis/QGIS/issues/48586) | [PR #48603](https://github.com/qgis/QGIS/pull/48603) | [PR #48632](https://github.com/qgis/QGIS/pull/48632) |
| Batch Nominatim Geocoder output directly saved to file has no CRS | [#48385](https://github.com/qgis/QGIS/issues/48385) | [PR #48618](https://github.com/qgis/QGIS/pull/48618) | [PR #48708](https://github.com/qgis/QGIS/pull/48708) |
| Iterating over features in processing algorithm not creating correct destination folder | [#48383](https://github.com/qgis/QGIS/issues/48383) | [PR #48646](https://github.com/qgis/QGIS/pull/48646) | [PR #48657](https://github.com/qgis/QGIS/pull/48657) |
| Dragging multiple layers in processing algorithm layer selection widget crashes QGIS | [#47728](https://github.com/qgis/QGIS/issues/47728) | [PR #48649](https://github.com/qgis/QGIS/pull/48649) | [PR #48656](https://github.com/qgis/QGIS/pull/48656) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Alex Bruy](https://www.qcooperative.net/)
### Reparaties van problemen door Sandro Santilli
| Titel probleem | URL Issues (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Add simple bash script to run tests as done by CI | [QGIS QEP #244](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/244) | [PR #48617](https://github.com/qgis/QGIS/pull/48617) | Niet van toepassing |
| test_provider_eptprovider occasionally aborts | [#48778](https://github.com/qgis/QGIS/issues/48778) | [PR #48793](https://github.com/qgis/QGIS/pull/48793) | niet nodig |
| Issue with QgsVectorLayerUndoCommand class (QGIS crashes) | [#23243](https://github.com/qgis/QGIS/issues/23243) | [PR #48700](https://github.com/qgis/QGIS/pull/48700) | [PR #48934](https://github.com/qgis/QGIS/pull/48934) |
| Check that source files are not overridden | [#25830](https://github.com/qgis/QGIS/issues/25830) | [PR #48654](https://github.com/qgis/QGIS/pull/48654) | Niet van toepassing |
| TestQgsGdalProvider failures in absence of netcdf support | [#48906](https://github.com/qgis/QGIS/issues/48906) | [PR #48907](https://github.com/qgis/QGIS/pull/48907) | [PR #48926](https://github.com/qgis/QGIS/pull/48926) |
| test_core_gdalprovider modifies tests/testdata/zip/landsat_b1.zip source file | [#48846](https://github.com/qgis/QGIS/issues/48846) | [PR #48917](https://github.com/qgis/QGIS/pull/48917) | [PR #48926](https://github.com/qgis/QGIS/pull/48926) |
| Drop gpkg_metadata_reference_column_name_update trigger generated by GDAL \< 2.4.0 | N/B | [PR #48953](https://github.com/qgis/QGIS/pull/48953) | [PR #48957](https://github.com/qgis/QGIS/pull/48957) |
| Fix test analysis processing modification of source files | [#48937](https://github.com/qgis/QGIS/issues/48937) | [PR #48959](https://github.com/qgis/QGIS/pull/48959) | [PR #48961](https://github.com/qgis/QGIS/pull/48961) |
| ctest: No module named \'qgis.server\' | [#48958](https://github.com/qgis/QGIS/issues/48958) | [PR #48993](https://github.com/qgis/QGIS/pull/48993) | [PR #48999](https://github.com/qgis/QGIS/pull/48999) |
| PyQgsLocalServer test fails: AttributeError: module \'platform\' has no attribute \'dist\' | [#48962](https://github.com/qgis/QGIS/issues/48962) | [PR #48976](https://github.com/qgis/QGIS/pull/48976) | [PR #49028](https://github.com/qgis/QGIS/pull/49028) |
| Fix old GDAL triggers in geopackage files | N/B | [PR #49037](https://github.com/qgis/QGIS/pull/49037) | [PR #49039](https://github.com/qgis/QGIS/pull/49039) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Reparaties van problemen door Nyall Dawson
| Titel probleem | URL Issues (indien gerapporteerd, GitHub) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| layer_property(\..., \'path\') should work for all layer types | [#49011](https://github.com/qgis/QGIS/issues/49011) | [PR #49042](https://github.com/qgis/QGIS/pull/49042) | [PR #49046](https://github.com/qgis/QGIS/pull/49046) |
| Improve UX for virtual layer creation dialog | niet gerapporteerd | [PR #49015](https://github.com/qgis/QGIS/pull/49015) | Niet van toepassing |
| \[db manager\] Don\'t load preview layers into project | [#47159](https://github.com/qgis/QGIS/issues/47159) | [PR #49016](https://github.com/qgis/QGIS/pull/49016) | [PR #49019](https://github.com/qgis/QGIS/pull/49019) |
| Don\'t hang when an error occurs while trying to build a virtual layer | [#48908](https://github.com/qgis/QGIS/issues/48908) | [Commit 988edc8700](https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5) | Te indringend |
| Don\'t offer non-vector layer providers as options for virtual layer | [#48908](https://github.com/qgis/QGIS/issues/48908) | [Commit 988edc8700](https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5) | Te indringend |
| Fix selecting/deselecting all in offline editing dialog when some layers are in unchecked groups | [#48971](https://github.com/qgis/QGIS/issues/48971) | [PR #48985](https://github.com/qgis/QGIS/pull/48985) | [PR #49002](https://github.com/qgis/QGIS/pull/49002) |
| Fix hovering features in attribute table in dark themes selects them | [#48914](https://github.com/qgis/QGIS/issues/48914) | [PR #48986](https://github.com/qgis/QGIS/pull/48986) | [PR #49001](https://github.com/qgis/QGIS/pull/49001) |
| Fix atlas expression context is not available when rendering item overview frames | [#48963](https://github.com/qgis/QGIS/issues/48963) | [PR #48967](https://github.com/qgis/QGIS/pull/48967) | [PR #48984](https://github.com/qgis/QGIS/pull/48984) |
| Fix regression where layout attribute table conditional styles don\'t apply | [#48965](https://github.com/qgis/QGIS/issues/48965) | [PR #48968](https://github.com/qgis/QGIS/pull/48968) | [PR #48973](https://github.com/qgis/QGIS/pull/48973) |
| Review and finish open PR [PR #48314](https://github.com/qgis/QGIS/pull/48314) |  |  |  |
| Fix geometry based expression attributes for diagrams | [#47800](https://github.com/qgis/QGIS/issues/47800) | [PR #48893](https://github.com/qgis/QGIS/pull/48893) | [PR #48911](https://github.com/qgis/QGIS/pull/48911) |
| Fix loss of precision when an extent is manually entered in processing extent widgets | [#48887](https://github.com/qgis/QGIS/issues/48887) | [PR #48895](https://github.com/qgis/QGIS/pull/48895) | [PR #48910](https://github.com/qgis/QGIS/pull/48910) |
| Fix some undersized icons on hidpi displays | niet gerapporteerd | [PR #48875](https://github.com/qgis/QGIS/pull/48875) | Niet van toepassing |
| Make atlas coverage layer available to expression builder for custom grid format | [#48833](https://github.com/qgis/QGIS/issues/48833) | [PR #48839](https://github.com/qgis/QGIS/pull/48839) | [PR #48894](https://github.com/qgis/QGIS/pull/48894) |
| Fix regression where user defined default style doesn\'t apply to MapInfo TAB files | [#48667](https://github.com/qgis/QGIS/issues/48667) | [PR #48840](https://github.com/qgis/QGIS/pull/48840) | [PR #48892](https://github.com/qgis/QGIS/pull/48892) |
| Fix picking values from QgsFeatureListComboBox | [#48459](https://github.com/qgis/QGIS/issues/48459) | [PR #48841](https://github.com/qgis/QGIS/pull/48841) | [PR #48881](https://github.com/qgis/QGIS/pull/48881) |
| Fix clear values for offset along line spin boxes | niet gerapporteerd | [PR #48872](https://github.com/qgis/QGIS/pull/48872) | [PR #48878](https://github.com/qgis/QGIS/pull/48878) |
| Fix ambiguous \"show all labels\" setting and address regressions in label when this setting is misinterpreted | [#41043](https://github.com/qgis/QGIS/issues/41043) | [PR #48771](https://github.com/qgis/QGIS/pull/48771) | Te indringend |
| Main annotation layer should follow project crs unless it has items added | [#42378](https://github.com/qgis/QGIS/issues/42378) | [PR #48815](https://github.com/qgis/QGIS/pull/48815) | Te indringend |
| Fix some misleading warnings about transformations for non-earth crs | [#42378](https://github.com/qgis/QGIS/issues/42378) | [PR #48815](https://github.com/qgis/QGIS/pull/48815) | Te indringend |
| Never show the transformation selection dialog for the first layer added to a project | niet gerapporteerd | [PR #48811](https://github.com/qgis/QGIS/pull/48811) | [PR #48814](https://github.com/qgis/QGIS/pull/48814) |
| Ensure layer level expressions work correctly for diagrams | [#47800](https://github.com/qgis/QGIS/issues/47800)0 | [PR #48803](https://github.com/qgis/QGIS/pull/48803) | [PR #48813](https://github.com/qgis/QGIS/pull/48813) |
| Fix handling of WMTS sources with dimensions in browser | [#36264](https://github.com/qgis/QGIS/issues/36264) | [PR #48800](https://github.com/qgis/QGIS/pull/48800) | [PR #48812](https://github.com/qgis/QGIS/pull/48812) |
| Ensure that all units are changed when setting output unit for a symbol | [#45961](https://github.com/qgis/QGIS/issues/45961) | [PR #48786](https://github.com/qgis/QGIS/pull/48786) |  |
| Fix loss of mesh layer styling when fixing a broken path to a mesh layer | niet gerapporteerd | [PR #48765](https://github.com/qgis/QGIS/pull/48765) | [PR #48768](https://github.com/qgis/QGIS/pull/48768) |
| Show pinned label highlights also for pinned curved labels | [#48753](https://github.com/qgis/QGIS/issues/48753) | [PR #48764](https://github.com/qgis/QGIS/pull/48764) | N/B |
| Don\'t hide parts of the mesh renderer widget if the layer is invalid | niet gerapporteerd | [PR #48757](https://github.com/qgis/QGIS/pull/48757) |  |
| Add layer opacity widget in mesh layer renderer properties widget | niet gerapporteerd | [PR #48756](https://github.com/qgis/QGIS/pull/48756) |  |
| Review and finish open PR [PR #44941](https://github.com/qgis/QGIS/pull/44941) |  |  |  |
| Fix a crash when QgsProject::instance() is accessed when no QgsApplication exists | niet gerapporteerd | [PR #48721](https://github.com/qgis/QGIS/pull/48721) | N/B |
| Better approach to filtering lists by tags which works across different styles | [#48659](https://github.com/qgis/QGIS/issues/48659) | [PR #48689](https://github.com/qgis/QGIS/pull/48689) | N/B |
| Fix slow layout view when atlas is enabled with legend filter enabled | [#47033](https://github.com/qgis/QGIS/issues/47033) | [PR #48686](https://github.com/qgis/QGIS/pull/48686) | [PR #48704](https://github.com/qgis/QGIS/pull/48704) |
| Fix crash after running model from history dialog | [#40258](https://github.com/qgis/QGIS/issues/40258) | [PR #48687](https://github.com/qgis/QGIS/pull/48687) | [PR #48709](https://github.com/qgis/QGIS/pull/48709) |
| Fix crash on QGIS exit | zal waarschijnlijk een aantal geopende tickets oplossen, maar heeft bevestiging van de eindgebruiker nodig | [Commit 5b052730b5](https://github.com/qgis/QGIS/commit/5b052730b5c10f12570dd5e68fca1962f113b3f3) | Te indringend |
| Add support for map field types to memory provider, avoid data loss in models/processing | niet gerapporteerd | [PR #48638](https://github.com/qgis/QGIS/pull/48638) | Te indringend |
| Fix crash when convertng a curved geometry to curves | [#48045](https://github.com/qgis/QGIS/issues/48045) | [#48045](https://github.com/qgis/QGIS/issues/48045) | [PR #49024](https://github.com/qgis/QGIS/pull/49024) |
| Fix many memory leaks | niet gerapporteerd | [PR #48590](https://github.com/qgis/QGIS/pull/48590) | N/B |
| Fix ctrl modifier scrolling on symbol buttons | niet gerapporteerd | [PR #48581](https://github.com/qgis/QGIS/pull/48581) | N/B |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
