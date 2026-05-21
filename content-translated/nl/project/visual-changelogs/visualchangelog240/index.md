---
HasBanner: false
draft: false
releaseDate: 27-06-2014
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.4{#changelog24 }
Datum uitgave 27-06-2014

Log met wijzigingen voor de volgende uitgave van QGIS 2.4.0. De nadruk voor deze uitgave ligt meer op het oppoetsen en de uitvoering - we hebben vele nieuwe mogelijkheden, tweaks en verbeteringen toegevoegd om de gebruikersinterface meer consistent te maken en er professioneler uit te laten zien (en hopelijk eenvoudiger te gebruiken). Aan de Printvormgeving (gebruikt voor het maken van afdrukklare kaarten) is heel vele werk verricht om het een meer bruikbaar platform voor het maken van fantastische cartografische uitvoer te maken.

Wanneer aan software nieuwe mogelijkheden worden toegevoegd, introduceren die de mogelijkheid tot het ontstaan van nieuwe problemen - als u in deze uitgave nieuwe problemen tegenkomt, vul dan een ticket in [op de QGIS Bug Tracker](http://hub.qgis.org).

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- GOUDEN Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- ZILVEREN sponsor: [G.A.I.A. mbH, Duitsland](http://www.gaia-mbh.de/)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de)
- BRONZEN sponsor: [www.openrunner.com, Frankrijk](http://www.openrunner.com)
- BRONZEN Sponsor: [www.eschenlaub.de, Duitsland](http://www.eschenlaub.de)

Een recente lijst van donoren die een financiële bijdrage, klein en groot, hebben gegeven aan het project kan worden bekeken op onze [lijst met donoren](https://qgis.org/nl/site/about/sponsorship.html#list-of-donors).

Als u een donatie zou willen geven of een sponsor voor het project zou willen worden, bekijk dan [onze pagina om te sponsoren](https://qgis.org/nl/site/about/sponsorship.html#sponsorship) voor de details. QGIS is gratis software en u bent niet verplicht om het te doen. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Genereer bandnaam met NetCDF EXTRA_DIM
De NetCDF verschafte extra dimensionele informatie. Deze informatie verschaft metadata over elke band. Deze metadata kan worden gebruikt om de de naam van elke band te verklaren. Bijvoorbeeld: de banden van een bestand van NetCDF geven de temperatuur op enen bepaalde diepte weer. Voor de gebruikers is het eenvoudiger een band te selecteren met informatie over de diepte, in plaats van alleen het nummer van de band.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Mogelijkheid: Schaal en verschuiving op rastergegevens toepassen
In sommige gegevensbronnen voor rasters, worden gegevens opgeslagen als integer met een schaal en een verschuiving in de metadata. De schaal en verschuiving kunnen worden gebruikt om de juiste gegevens op te halen. QGIS past dat toe op de rastergegevens om de gebruikers de juiste informatie te verschaffen voor legenda, histogram en identificatie.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Mogelijkheid: Snel veld voor veldberekening in attributentabel
We hebben een fantastische nieuwe mogelijkheid voor hen die werken met berekende velden in attributentabellen voor vectoren. De nieuwe snelle balk voor veldberekening laat u nel en eenvoudig de waarden in een kolom van de attributentabel bij te werken.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Mogelijkheid: Modi kleurvoorbeelden in Printvormgeving en kaartvenster
Een echt innovatieve mogelijkheid die is toegevoegd aan 2.4 is ondersteuning voor voorbeelden voor grijswaarden en voor kleurenblindheid. Dit stelt u in staat te visualiseren hoe mensen met kleurenblindheid uw cartografie en kaartlay-out zullen zien, of hoe uw kaart eruit zal zien als hij in grijswaarden wordt afgedrukt. U kunt [hier](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/) meer over deze mogelijkheid .

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Mogelijkheid: QLR QGIS-laagbestanden
Toegevoegde ondersteuning voor  bestanden van QGIS Layer Definition of eenvoudigweg QLR (zie <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR-bestand is een bestand dat wijst naar de gegevens, en bevat alle opmaak en andere informatie. U hoeft dan slechts dit bestand toe te voegen en het zal alle magie voor u uitvoeren. QLR maakt het eenvoudiger om dezelfde laag toe te voegen aan meerdere kaartdocumenten, erven van alle eigenschappen die worden ingesteld en werken met alle door QGIS ondersteunde lagen, uitgezonderd speciale lagen voor plug-ins.
### Mogelijkheid: Nieuwe functies voor expressies
We hebben enkele nieuwe functies beschikbaar in de Expressiebouwer.
- begrenzingsvakken (grenzen)
- begrenzingsvak breedte & hoogte (grenzen_breedte/grenzen_hoogte)
- min/max x/y coórdinaten (xmin/xmax/ymin/ymax)
- nieuwe functie tekstdoorloop die een tekenreeks teruggeeft met een maximum/minimum aantal tekens

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Mogelijkheid: Kleuren kopiëren, plakken en slepen en neerzetten
U kunt nu kleuren kopiëren, plakken en slepen en neerzetten tussen elke widget voor invoer in QGIS. Bekijk dit [artikel](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) voor meer informatie over hoe deze nieuwe mogelijkheid werkt. Hex-kleurcodes en RGB-strings kunnen ook op de kleurknoppen worden geplakt om het importeren van die kleuren van buiten QGIS mogelijk te maken.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Mogelijkheid: Multi-threaded renderen
Dit is een mogelijkheid die we eenvoudigweg niet tot zijn recht kunnen,laten komen met slechts één schermafdruk - QGIS ondersteunt nu multi-threaded renderen! Wat dit betekent is dat bij het tekenen van de kaart, QGIS het tekenwerk verdeelt over alle cores in uw CPU, wat het proces efficiënter maakt en beter laat reageren. Met **reageert beter** bedoelen we dat u niet langer hoeft te wachten met het bijwerken van de kaartweergave voordat u opnieuw kunt pannen en zoomen. De kaartweergave wordt ook meermalen bijgewerkt, wat u in staat stelt te zien of de kaart juist is gepositioneerd, vroeg in het proces van tekenen. Bekijk [dit artikel](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) voor een meer gedetailleerd overzicht van het systeem voor multithreaded renderen. U vindt in het dialoogvenster voor de instellingen van QGIS enkele opties die u in staat stellen het gedrag van het multi-threaded renderen te beheren.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Labelen
### Mogelijkheid: Objecten meerdere malen labelen
Lange lijnen (zoals contourlijnen of wegen) kunnen nu herhaald worden gelabeld met regelmatige intervallen. Men kan kiezen tussen mm en kaarteenheden voor het specificeren van de interval voor de herhaling. Op het moment van de uitgave is er nog steeds een probleem met de instelling \"Aan elkaar verbonden lijnen samenvoegen om labelduplicaten te voorkomen\".

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Printvormgeving
### Mogelijkheid: Verbeteringen aan items Afbeelding in Printvormgeving
Het item Afbeelding in Printvormgeving is nu \'Atlas-vriendelijk' - u kunt een **expressie om te definiëren welke afbeelding** te gebruiken om te worden weergegeven op elke pagina van de Atlas. U kunt nu ook de **modus Formaat wijzigen** (zoomen, clippen, uitrekken etc.) voor de afbeelding in relatie tot de grootte van zijn frame en de dimensies. U kunt ook de plaatsing van de afbeelding specificeren relatief vergeleken met het frame met behulp van het nieuwe item **Plaatsing**.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Mogelijkheid: Modus vooraf gedefinieerde schalen voor kaarten in Atlas
U kunt nu een vooraf gedefinieerde schaal definiëren voor de kaart bij het werken met items voor een Atlas. Het zal de optie \'Best passend gebruiken\' gebruiken uit de lijst van vooraf gedefinieerde schalen in de instellingen van de eigenschappen van uw project (zie Project -\> Projecteigenschappen -\> Algemeen -\> Projectschalen om deze vooraf gedefinieerde schalen te configureren).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Mogelijkheid: Verbeterde attributentabellen in Printvormgeving
We hebben een aantal verbeteringen gemaakt aan de mogelijkheid om attributentabellen weer te geven in uw lay-outs van Printvormgeving:
- Voor het opnieuw ordenen van kolommen binnen een tabel is ondersteuning toegevoegd
- Ondersteuning toegevoegd voor op expressies gebaseerde kolommen
- U kunt nu de uitlijning van individuele tabelkolommen instellen, en ook de uitlijning specificeren voor de kopcellen van de tabel
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
### Mogelijkheid: Plug-in MetaSearch Catalogue Client
MetaSearch is een plug-in voor QGIS om interactief te werken met metadata catalogus services, die de standaard OGC Catalogue Service voor het web (CSW) ondersteund. Deze plug-in verschaft een eenvoudige en intuïtieve benadering en gebruikersvriendelijke interface om catalogi voor metadata binnen QGIS te doorzoeken en is nu standaard opgenomen in het bronproduct van QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Symbologie
### Mogelijkheid: Stijl Shapeburst-vulling
We hebben een fantastische nieuwe renderer in QGIS 2.4. De renderer Shapeburst zal u in staat stellen polygonen te vullen met een kleurverloop dat zich uitstrekt van de lijnrand tot in het interieur van de polygoon. U kunt [hier](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4) meer lezen over **shapeburst**.

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Mogelijkheid: Optie om plaatsing van markeringslijnen te verplaatsen
Bij het gebruiken van een markeringslijn langs een rand van een lijn of polygoon, kunt u nu een **verschuiving** specificeren zodat de markeringslijn begint op een ingestelde afstand vanaf het begin van de lijn. Als een markeringslijn wordt ingesteld op de modus \"alleen op eerste hoekpunt\" of \"alleen op laatste hoekpunt\", dan zal deze verschuiving beheren hoe ver langs de lijn vanaf het hoekpunt de markering wordt geplaatst.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Mogelijkheid: Nieuwe renderen geïnverteerd polygoon
Een nieuwe renderer is toegevoegd voor objecten Polygoon, welke u in staat stelt alles op te maken **buiten** uw polygonen. Dit kan nuttig zijn voor het accentueren van gebieden, of voor het maken van cartografische maskers. Indien gebruikt met de nieuwe stijl Shapeburst, kunt u nu uitvoer maken zoals weergegeven in de afbeelding voor dit item.

**Opmerking:** De nieuwe versie van plug-in masker helpt om eenvoudig maskerlagen te maken uit de huidige selectie, label-objecten alleen in deze gebieden, en een automatisch masker te maken bij het genereren van een Atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Mogelijkheid: Stijlen met Spatialite-lagen opslaan en ophalen
In de vorige versie was het mogelijk om stijlen op te slaan met lagen in PostgreSQL, nu is dat ook mogelijk voor lagen van SpatiaLite. Deze functie maakt het mogelijk verschillende lagen in te bedden in een container van SpatiaLite, wat het delen van gegevens vereenvoudigt en ook hun presentatie. Een videohandleiding voor deze functionaliteit is hier <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/> te vinden

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
