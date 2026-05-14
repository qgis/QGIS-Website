---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.4{#changelog24 }
Datum uitgave 27-06-2014

Log met wijzigingen voor de volgende uitgave van QGIS 2.4.0. De nadruk voor deze uitgave ligt meer op het oppoetsen en de uitvoering - we hebben vele nieuwe mogelijkheden, tweaks en verbeteringen toegevoegd om de gebruikersinterface meer consistent te maken en er professioneler uit te laten zien (en hopelijk eenvoudiger te gebruiken). Aan de Printvormgeving (gebruikt voor het maken van afdrukklare kaarten) is heel vele werk verricht om het een meer bruikbaar platform voor het maken van fantastische cartografische uitvoer te maken.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Algemeen
### Feature: Generate band name with NetCDF EXTRA_DIM
De NetCDF verschafte extra dimensionele informatie. Deze informatie verschaft metadata over elke band. Deze metadata kan worden gebruikt om de de naam van elke band te verklaren. Bijvoorbeeld: de banden van een bestand van NetCDF geven de temperatuur op enen bepaalde diepte weer. Voor de gebruikers is het eenvoudiger een band te selecteren met informatie over de diepte, in plaats van alleen het nummer van de band.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Mogelijkheid: Schaal en verschuiving op rastergegevens toepassen
In sommige gegevensbronnen voor rasters, worden gegevens opgeslagen als integer met een schaal en een verschuiving in de metadata. De schaal en verschuiving kunnen worden gebruikt om de juiste gegevens op te halen. QGIS past dat toe op de rastergegevens om de gebruikers de juiste informatie te verschaffen voor legenda, histogram en identificatie.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Mogelijkheid: Snel veld voor veldberekening in attributentabel
We hebben een fantastische nieuwe mogelijkheid voor hen die werken met berekende velden in attributentabellen voor vectoren. De nieuwe snelle balk voor veldberekening laat u nel en eenvoudig de waarden in een kolom van de attributentabel bij te werken.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Mogelijkheid: Modi kleurvoorbeelden in Printvormgeving en kaartvenster
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Mogelijkheid: QLR QGIS-laagbestanden
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Mogelijkheid: Nieuwe functies voor expressies
We hebben enkele nieuwe functies beschikbaar in de Expressiebouwer.
- begrenzingsvakken (grenzen)
- bounding box width & height (bounds_width/bounds_height)
- min/max x/y coórdinaten (xmin/xmax/ymin/ymax)
- nieuwe functie tekstdoorloop die een tekenreeks teruggeeft met een maximum/minimum aantal tekens

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Mogelijkheid: Kleuren kopiëren, plakken en slepen en neerzetten
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Mogelijkheid: Multi-threaded renderen
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Labelen
### Mogelijkheid: Objecten meerdere malen labelen
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen aan items Afbeelding in Printvormgeving
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Mogelijkheid: Modus vooraf gedefinieerde schalen voor kaarten in Atlas
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Mogelijkheid: Verbeterde attributentabellen in Printvormgeving
We hebben een aantal verbeteringen gemaakt aan de mogelijkheid om attributentabellen weer te geven in uw lay-outs van Printvormgeving:
- Voor het opnieuw ordenen van kolommen binnen een tabel is ondersteuning toegevoegd
- Ondersteuning toegevoegd voor op expressies gebaseerde kolommen
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Inhoud van de tabel kan worden gefilterd door een expressie

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Mogelijkheid: Algemene verbeteringen van Printvormgeving
Er zijn een aantal toevoegingen aan Printvormgeving om het leven wat aangenamer te maken bij het werken in de modus Lay-out:
- Knop toegevoegd om het bereik van het huidige kaartitem te bekijken in het kaartvenster
- Mogelijkheid om SVG-afbeeldingen te exporteren vanuit Printvormgeving met lagen
- Lijn samenvoegen en eindstijlen voor schaalbalken instellen
- Ondersteuning voor de stijl voor het samenvoegen van lijnen voor items Frames

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Mogelijkheid: Verbeteringen aan HTML-frames
HTML-frames in de Printvormgeving zijn verbeterd. Er is een nieuwe knop **Frame toevoegen** die kan worden gebruikt om handmatig meerdere gekoppelde frames te maken. We hebben ook onze logica voor pagina-einden verbeterd wat de kans vermindert dat u pagina-einden krijgt die midden door tekstregels lopen bij het pagineren van HTML-frames.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Plug-ins
### Feature: Plug-in MetaSearch Catalogue Client
MetaSearch is een plug-in voor QGIS om interactief te werken met metadata catalogus services, die de standaard OGC Catalogue Service voor het web (CSW) ondersteund. Deze plug-in verschaft een eenvoudige en intuïtieve benadering en gebruikersvriendelijke interface om catalogi voor metadata binnen QGIS te doorzoeken en is nu standaard opgenomen in het bronproduct van QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Symbologie
### Mogelijkheid: Stijl Shapeburst-vulling
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Feature: Optie om plaatsing van markeringslijnen te verplaatsen
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Mogelijkheid: Nieuwe renderen geïnverteerd polygoon
Een nieuwe renderer is toegevoegd voor objecten Polygoon, welke u in staat stelt alles op te maken **buiten** uw polygonen. Dit kan nuttig zijn voor het accentueren van gebieden, of voor het maken van cartografische maskers. Indien gebruikt met de nieuwe stijl Shapeburst, kunt u nu uitvoer maken zoals weergegeven in de afbeelding voor dit item.

**Opmerking:** De nieuwe versie van plug-in masker helpt om eenvoudig maskerlagen te maken uit de huidige selectie, label-objecten alleen in deze gebieden, en een automatisch masker te maken bij het genereren van een Atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Mogelijkheid: Stijlen met Spatialite-lagen opslaan en ophalen
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
