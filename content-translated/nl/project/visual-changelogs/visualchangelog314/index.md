---
HasBanner: false
draft: false
releaseDate: '2020-06-19'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.14
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.14{#changelog314 }
![image1](images/splash.jpeg)

Datum uitgave 19-06-2020

De volgende uitgave in het spoor van fantastische uitgaven van QGIS die we de afgelopen 18 jaar hebben ontwikkeld. Deze uitgave zit zo boordevol nieuwe mogelijkheden en verbeteringen, groot en klein dat het moeilijk is waar te beginnen. Enkele van de kenmerkende mogelijkheden omvatten ondersteuning voor vectortegels, grote voordelen in ondersteuning voor MDAL mdal / mazen, eigen ondersteuning voor tijdbeheer in WMS-T, PG Raster, vectorproviders, en lagen met mazen. Gebruikers die zich richten op cartografie en digitaliseren zijn ook niet vergeten, met heel veel nieuwe opties voor u!

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://www.qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende leden](https://www.qgis.org/nl/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Algemeen
### Mogelijkheid: Nieuwe instellingen voor lettertypen voor annotaties van Decoratie
Annotaties voor het decoreren van het raster van het kaartvenster zijn nu volledig aan te passen, inclusief kleur van het lettertype, buffer, etc.

![image8](images/entries/14b7cf800ef293ac3ea3f00d12a30022876e713c.webp)

Dit werd mogelijk gemaakt door iMHere Asia

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Tijdbeheer
### Mogelijkheid: Instellen van cumulatieve tijdsperiode in Tijdbeheer
Voegt een instelling toe aan Tijdbeheer om de tijdsperiode voor de animatie cumulatief in te stellen. Dit betekent dat alle frames voor de animatie dezelfde datum-tijd voor het begin hebben, maar verschillende datums en tijden voor het einde.

Dit is nuttig voor u als u accumulerende gegevens in uw visualisatie in Tijdbeheer wilt, in plaats van een \'verplaatsend tijdvenster\' weer te geven over uw gegevens.

![image2](images/entries/90da13821bfde46aa6d9d951fb9a31bf27d85656.gif)

Dit werd mogelijk gemaakt door [Meteorological Service of Canada](https://weather.gc.ca)

Deze mogelijkheid werd ontwikkeld door [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Mogelijkheid: Nieuwe modus \"Alleen laag opnieuw tekenen\" toegevoegd voor vectorlagen van Tijdbeheer
Indien ingesteld voor deze modus, zal de laag automatisch opnieuw worden getekend wanneer de tijdsperiode van Tijdbeheer wordt gewijzigd, maar er zal geen op tijd gebaseerd filteren worden toegepast op de objecten.

Deze configuratie is nuttig als de laag instellingen voor Symbologie heeft die variëren gebaseerd op de tijdsperiode. Wanneer het bijvoorbeeld tijdsafhankelijke expressies voor de renderer Regel-gebaseerd gebruikt of data-bepaalde expressies voor Symbologie.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor basisafhandeling van Tijdbeheer voor vectorlagen toegevoegd
Dit laat enkele basismogelijkheden voor het eigen Tijdbeheer voor vectorlagen zien:
- Statisch tijdbereik voor de laag (om overeen te komen met mogelijkheden voor rasterlagen), dit stelt één enkele statische tijdsperiode in die van toepassing is voor de gehele laag. Alle objecten van de laag zullen worden weergegeven als de tijd van het kaartvenster de tijdsperiode van de laag overlapt
- \"Enkel veld met DateTime\": Maakt selecteren van één enkel veld Date of DateTime uit de laag mogelijk. Objecten zullen worden weergegeven als de waarde van dit veld binnen de tijdsperiode van het kaartvenster ligt
- \"Afzonderlijke velden voor begin- en einddatum/-tijd\": Maakt het mogelijk velden voor begin- en einddatum/-tijd te selecteren uit de laag. Objecten zullen worden weergegeven als het berekende tijdsinterval uit deze velden de tijdsperiode van het kaartvenster overlapt

We zouden moeten overwegen dit in de toekomst uit te breiden, bijv. om modi toe te voegen voor \"begintijd + vaste duur\", \"begintijd + duur vanuit veld\", \"begin- en eindtijd via expressies\", etc.

Enkele bekend beperkingen/inefficiënties:
- Momenteel kunnen alleen velden Date/DateTime worden gebruikt. Dit is gedaan om de afhandeling van de indeling te vereenvoudigen en de noodzaak om rekening te houden met velden met tekenreeksen met andere indelingen voor DateTime te vermijden. In de toekomst zouden we het selecteren van velden met tekenreeksen mogelijk moeten maken, en gebruikers toestaan om een aangepaste tekenreeks voor de indeling DateTime in te voeren
- Anders dan de benadering met de plug-in Time Manager, berust de hier geboden benadering volledig op expressies van QGIS en verzoeken voor objecten om het filteren uit te voeren (Time Manager gebruikt tekenreeksen voor filteren van lagen en probeert een eigen syntaxis voor het SQL-filter in te stellen, zodat het filteren op de achtergrond wordt uitgevoerd). Dit is met opzet, omdat het een universele benadering voor filteren verschaft, ongeacht de gebruikte provider (d.i. we hoeven geen rekening te houden met de verschillende syntaxis voor SQL, die door de verschillende providers zelf wordt gebruikt). Het mooie van het compileren van expressies voor verzoeken voor objecten **zou** betekenen dat de expressies van QGIS magisch worden omgezet naar eigen query's op de achtergrond. MAAAAAAAAAAAR\… omdat ondersteuning voor expressies van QGIS voor letterlijke DateTime ontbreekt, kunnen we momenteel alleen vertrouwen op de functie voor de expressie "to_datetime" en alles door middel van tekenreeksen af te dwingen. Geen van de compilers voor expressies handelt deze functie af, dus momenteel wordt \*alle\* filteren uitgevoerd aan de zijde van QGIS. We dienen functies toe te voegen voor het geoptimaliseerd maken van letterlijke DateTime. En er dan voor zorgen dat de verschillende compilers deze letterlijken correct omzetten naar de syntaxis voor het filteren op de achtergrond, om het mogelijk te maken dat al het werk voor het filteren wordt uitgevoerd aan de zijde van de database\…

Dis is, momenteel, de uitvoering veel slechter met grote lagen, vergeleken met Time Manager (en de weergegeven set met objecten is kleiner, bijv. geen afhandeling voor interpolatie), maar het voordeel is dat we het eigen framewerk voor Tijdbeheer kunnen gebruiken en geanimeerde vectorlagen kunnen maken, naast lagen met mazen en rasterlagen!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor API van Tijdbeheer voor raster in PostgreSQL
Integratie van mogelijkheden voor Tijdbeheer voor rasters in PostgreSQL toegevoegd.

![image3](images/entries/78421839-37e3d100-765b-11ea-83e5-e7e3e519155e.webp)

![image4](images/entries/a8347da9570ae597bc17e23236e4eb4d57efb1d1.gif)

Dit werd mogelijk gemaakt door ARPA Piemonte

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: QGIS Projectinstellingen voor Tijdbeheer
Deze mogelijkheid voegt functionaliteit voor tijdsinstellingen voor het project toe.

U zult in staat zijn de tijdsperiode voor Tijdbeheer in te stellen, hetzij met handmatige invoer, hetzij door deze uit de huidige projectlagen voor Tijdbeheer te berekenen. Het laatste kan worden uitgevoerd door te klikken op de verschafte knop \"Uit lagen berekenen\".

Deze implementatie stelt het podium in voor het toevoegen van geanimeerde objecten voor lagen van Tijdbeheer in QGIS.

Hier is een voorbeeld voor het instellen van een tijdsperiode in een project. ![image5](images/entries/74980472-93f2ed00-5441-11ea-8765-f35d1f69b144.gif)

Eerdere discussies over ondersteuning voor Tijdbeheer in QGIS zijn [hier](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/161) en [hier](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/128) te vinden.

Dit werd mogelijk gemaakt door [Meteorological Service of Canada](https://weather.gc.ca)

Deze mogelijkheid werd ontwikkeld door [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Mogelijkheid: Ondersteuning voor beperkingen van Tijdbeheer in lagen van WMS-T
Deze mogelijkheid maakt het mogelijk om lagen WMS voor Tijdbeheer (WMS-T) binnen QGIS te beperken. U zult in staat zijn hede periode DateTime te beperken voor elke laag voor Tijdbeheer van providers van WMS-T.

Deze implementatie laat de gebruiker de vereiste periode DateTime op de laag te specificeren vanaf de tab Bron in het dialoogvenster Laageigenschappen.

Hieronder staat een voorbeeld van de werkstroom. ![image6](images/entries/74638436-ee0f5c00-517c-11ea-938e-cec23c61ba29.gif)

**Opmerking:** *Voor directe punten in tijdperioden zal het specificeren van ene periode met een gelijke begin en eind DateTime resulteren in het gebruiken van het gespecificeerde punt DateTime en geen periode.*

![image7](images/entries/b86eea9111e33e6aea345b0e0759de48eaceade9.gif)

Dit werd mogelijk gemaakt door [Meteorological Service of Canada](https://weather.gc.ca)

Deze mogelijkheid werd ontwikkeld door [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Mogelijkheid: API Tijdbeheer 
Deze mogelijkheid verschaft een implementatie van de API voor ondersteuning van Tijdbeheer in QGIS.

U kunt de API voor Python vinden door te zoeken naar \'Temporal\' in de documentatie voor Python ([link](https://qgis.org/pyqgis/master/search.html?q=Temporal&check_keywords=yes&area=default)).

Dit werd mogelijk gemaakt door [Meteorological Service of Canada](https://weather.gc.ca)

Deze mogelijkheid werd ontwikkeld door [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
## Kaartgereedschap
### Mogelijkheid: Ondersteuning voor Gereedschap Identificeren in QGIS voor lagen met vectortegels.
Het gereedschap Identificeren is nu in staat attributen van objecten in vectortegels te inspecteren.

![image9](images/entries/79157425-d3501100-7dd4-11ea-8395-5c8ff1dce449.webp)

Dit werd mogelijk gemaakt door [Vele giften](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Geef een menu weer naast de knoppen van de widget Schaal, om direct instellen van de widget op een schaal, vanuit een kaart van afdruklay-out, mogelijk te maken
Een screencast zegt meer dan duizend woorden:

![image10](images/entries/78198825-34bada80-74cd-11ea-803a-90afea085b38.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Knop \"Objecten deselecteren van huidige actieve laag\" aan gereedschap toegevoegd
![image11](images/entries/76692569-26616780-6661-11ea-9071-fd4c712860db.gif)

Deze mogelijkheid werd ontwikkeld door [Ivan Ivanov](https://api.github.com/users/suricactus)
## Gebruikersinterface
### Mogelijkheid: Slepen en neerzetten van een laag in verscheidene instanties van QGIS toestaan
![image12](images/entries/77666018-b5834f00-6f80-11ea-971e-c6d7d996d37d.gif)

Dit werd mogelijk gemaakt door [QGIS Zwitserse gebruikersgroep](https://www.qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Attributentabellen als tabs openen 
Als de optie \"Nieuwe attributentabellen als vastgezette vensters openen\" actief is, zullen nieuwe attributentabellen worden geopend als tabs, bovenop bestaande attributentabellen.

![image13](images/entries/80049561-d8017d00-84d8-11ea-826e-d7092ac7a5c6.gif)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
## Symbologie
### Mogelijkheid: Renderer voor contouren voor rasterlagen 
Deze nieuwe renderer tekent contourlijnen die direct worden berekend uit de bron-rastwerband. Het is mogelijk de interval voor de contourlijnen en het te gebruiken symbool voor het tekenen in te stellen.

In aanvulling daarop is er ondersteuning voor \"index contouren\" - contourlijnen met hogere intervallen worden gewoonlijk getekend met een breder lijnsymbool.

Als we contourlijnen op rasterblokken voor de invoer maken met dezelfde grootte als onze rasterblokken voor de uitvoer, zullen de gemaakte lijnen te veel details bevatten. Deze details kunnen worden verminderd door de factor \"Invoer verlagen\" - dit zal een lagere resolutie van het bronraster vragen.

![image14](images/entries/77861880-17111b00-7218-11ea-95ba-410c97830b93.webp)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias](https://api.github.com/users/wonder-sk)
### Mogelijkheid: Eenheid percentage voor grootte symbologie markering rasterafbeelding en vulling raster toegevoegd.
Overeenkomstig het [Feature Request](https://github.com/qgis/QGIS/issues/30057) voegt deze patch een nieuwe waarde in percentage (van de originele afbeeldingsgrootte) voor eenheden van de grootte voor lagen **Markering rasterafbeelding** en **Vulling raster** (suggestie van [nirvn](https://github.com/qgis/QGIS/pull/34869#issuecomment-595090465) ).

Een laag bevat bijvoorbeeld rasterafbeeldingen van verscheidene grootten en verhoudingen:

![image15](images/entries/77845535-6e3fcd00-71d1-11ea-8760-b477e75f7a3a.webp) ![image16](images/entries/77845539-726bea80-71d1-11ea-9512-0a8e6cde7b3c.webp)

Als we een bestaande waarde voor de **eenheid van grootte** voor de Markering rasterafbeelding gebruiken, zal de laag er zo uitzien (met een normale krokodil, maar met een grote giraffe):

![image17](images/entries/77846711-bfec5580-71d9-11ea-9afe-a52af9b2784e.webp)

of zoals dit (met een normale giraffe, maar hele kleine krokodil):

![image18](images/entries/77846764-1eb1cf00-71da-11ea-9d6d-f468708ea726.webp)

De nieuwe waarde **percentage** van de eenheid voor grootte is bedoeld om dit probleem op te lossen.

Beide eenheidstesten \"qgis_rasterfilltest\" en \"qgis_rastermarkertest\" werden herschreven met een set van nieuwe controleafbeeldingen voor het testen van de voorgestelde waarden **percentage** van eenheden voor grootte.

Deze mogelijkheid werd ontwikkeld door [beketata](https://api.github.com/users/beketata)
### Mogelijkheid: Data-bepaalde eigenschap voor familie/stijl lettertype voor markering lettertype toegevoegd
Data-bepaalde eigenschappen werden toegepast voor de familie van het lettertype voor markeringen van lettertypen en de nagelnieuwe eigenschappen voor de stijl van het lettertype. Dit kan handig zijn voor een aantal scenario's, inclusief meertalige context waar een data-bepaalde eigenschap het dupliceren van gegevenssets kan voorkomen.

![image19](images/entries/1ded1a8bbec9eeebafad96b7616e963847961e14.webp)

Dit werd mogelijk gemaakt door iMHere Asia

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Mogelijkheid: Nieuwe instelling voor stijl van lettertype voor markeringen van lettertype
Met deze nagelnieuwe instelling, die eerder niet beschikbaar was, kunnen gebruikers en niet-standaard stijl van families van lettertypen selecteren.

![image20](images/entries/e387c3745d49a36116908dffc1126befae7d1b1f.webp)

Dit werd mogelijk gemaakt door iMHere Asia

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Labelen
### Mogelijkheid: Kleuren voor HTML in labels respecteren 
Indien ingeschakeld zal deze optie de inhoud van labels als HTML behandelen, en  KLEURGERELATEERDE opties voor opmaak van HTML voor de VOORGROND zullen in het gerenderde label worden gerespecteerd.

Opmerking: ALLEEN TAGS VOOR KLEUR IN HTML WORDEN GERESPECTEERD. Dit is GEEN bug, deze mogelijkheid is meer ontworpen als een \"test van het water\" met opmaak in HTML in labels, en overeenkomstig komen alleen opties voor de opmaak die niet de vorm van het lettertype wijzigen in aanmerking.

Aan de pluskant werkt het correct met ALLE andere instellingen voor labels, inclusief schaduwen, buffers, gebogen labels, etc!

Nu enkele leuke plaatjes:

![image21](images/entries/81377287-84359b80-9148-11ea-95f4-9d7917d62cf9.webp)

![image22](images/entries/81377294-88fa4f80-9148-11ea-9036-2a597b064bbc.webp)

Dit werd mogelijk gemaakt door [geoProRegio AG](http://www.geoproregio.ch)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Automatisch plaatsen van labels buiten polygonen
Deze mogelijkheid maakt het mogelijk automatisch labels buiten objecten polygonen te plaatsen.

Dit wordt op een aantal manieren weergegeven:
1. Een nieuwe modus voor plaatsing die polygoonlabels voor de laag altijd buiten de objecten plaatst: ![image23](images/entries/80680381-faf7e680-8b01-11ea-8612-b0f543bfd943.webp) ![image24](images/entries/80680391-00553100-8b02-11ea-8e56-21b57964f765.webp)
2. Bij het gebruiken van andere modi voor het plaatsen van polygonen, kan een nieuw keuzevak \"Plaatsen labels buiten polygonen toestaan\" worden geselecteerd om toe te staan dat labels buiten worden geplaatst, als het niet mogelijk is ze binnen de polygoon te plaatsen: ![image25](images/entries/80680478-30043900-8b02-11ea-8bd5-3325fc0a5021.webp) ![image26](images/entries/80680488-37c3dd80-8b02-11ea-98bb-e0882e6ab9ab.webp)

Het keuzevak \"Plaatsen labels buiten polygonen toestaan\" mag data-bepaald zijn, wat het gebruikers in staat stelt om ofwel labels buiten toe te staan, labels buiten te voorkomen, of labels buiten te forceren, op een object-voor-objectbasis.

Het algoritme voor plaatsing is gebaseerd op een modificatie van Rylov & Reimer (2016) \"*A practical algorithm for the external annotation of area features*\". Rylov & Reimer stellen een op een horizontale veeglijn gebaseerde benadering voor het selecteren van kandidaat labelpunten voor. Ik vond in de praktijk dat dit inferieure resultaten opleverde (en trager was) dan gewoon door de buitenste ring van de polygoon te gaan en kandidaat-punten te maken op regelmatige intervallen (speciaal voor nauwe, bijna horizontale polygonen).

Zoals weergegeven in de schermafdruk met eilanden hierboven, werkt de modus voor plaatsen buiten zoals verwacht met de meerregelige modus voor uitlijnen \"Plaatsing van labels volgen\".

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Laag met vectortegels - deel 4 (labelen)
Doorgegaan met het werken aan de implementatie va lagen met vectortegels.

Dit voegt ondersteuning voor labelen voor lagen met vectortegels toe. Tot op heden werkt het alleen in qgis_core\… Ondersteuning voor GUI zal het volgende zijn. Labelen gebruikt dezelfde concepten als het renderen van vectortegels: we hebben een lijst met stijlen voor labelen, elke gedefinieerd door zijn naam voor de sublaag, type geometrie, filterexpressie, zoombereik, en natuurlijk de configuratie voor de stijl van het label (QgsPalLayerSettings).

Onthoud dat er een \"kip-en-het-ei probleem\" is met labelen: Voor vectortegels maken we QgsFields voor een sublaag, gebaseerd op velden die de renderer en labelen aanvragen. Maar met labelen was het onmogelijk om de aangevraagde velden op te halen als zij nog niet beschikbaar waren in de context van de expressie (ondanks enkele kleine aanvullingen aan QgsProperty, QgsPropertyCollection, QgsPalLayerSettings om in staat te zijn aangevraagde veldnamen op te halen door niet tegelijkertijd interne expressies voor te bereiden).

![image27](images/entries/78723460-bf676380-792b-11ea-9cab-a6732e20033a.webp)

Een voorbeeld hoe bovenstaand labelen in te stellen in de console van Python:

    s = QgsVectorTileBasicLabelingStyle()
    s.setLayerName("place")
    s.setGeometryType(QgsWkbTypes.PointGeometry)
    s.setFilterExpression("rank = 1 AND class = 'country'")
    ls=QgsPalLayerSettings()
    ls.drawLabels=True
    ls.fieldName="name"
    ls.placement = QgsPalLayerSettings.OverPoint s.setLabelSettings(ls)
    labeling = QgsVectorTileBasicLabeling()
    labeling.setStyles([s])
    iface.activeLayer().setLabeling(labeling)
    
Dit werd mogelijk gemaakt door [Vele giften](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Beheer over ankerpunt voor tekstballon op label toegevoegd
Dit geeft gebruikers beheer over waar een tekstballon met de tekst van een label zou moeten worden samengevoegd (eerder had u alleen beheer over waar de tekstballon zou worden samengevoegd met de overeenkomende geometrie van het object).

Keuzes omvatten:
- Dichtstbijzijnde punt (eerdere gedrag)
- Zwaartepunt label
- Vaste hoeken: Linksboven/rechtsboven/linksonder/rechtsonder/etc

Data-bepaald beheer over het anker voor het label is ook mogelijk.

Helpt enige lelijkheid van tekstballonnen op te lossen!

Eerder resultaat (modus Dichtsbijzijnde punt):

![image28](images/entries/76173692-5a660400-61ed-11ea-87dd-74a4db5cf0ce.webp)

Met nieuwe plaatsing \"zwaartepunt\":

![image29](images/entries/76173706-6d78d400-61ed-11ea-89c1-ce4e2477dfef.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Mazen
### Mogelijkheid: Alleen gespecificeerde groep van gegevensset gebruiken
Deze mogelijkheid stelt de gebruiker in staat de te gebruiken groepen van de gegevensset te kiezen. Dit kan worden gedaan in het dialoogvenster voor eigenschappen van de laag met mazen op de tab Bron.

Een nieuwe boomweergave geeft alle beschikbare groepen voor de gegevensset van de gegevensprovider weer. De groepen voor de gegevensset kunnen geselecteerd/gedeselecteerd en hernoemd worden.

Dit widget verschaft ook knoppen om extra groepen van gegevenssets te laden uit bestanden, om de boom uit te klappen/in te klappen, om alle items te selecteren/deselecteren en om de standaarden voor de provider te herstellen (voor nu nog alleen de originele naam).

Alleen de geselecteerde groep van de gegevensset zal worden weergegeven in de widget voor de actieve gegevensset in instellingen voor de renderer.

![image30](images/entries/81516813-3a46e400-9307-11ea-9621-a27d5a8c86f2.gif)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Scalaire instellingen voor kleuren, afhankelijk van classificatie
Met deze mogelijkheid leest MDAL geclassificeerde scalaire waarden in de gegevensset. Wanneer waarden zijn geclassificeerd, worden standaard scalaire instellingen voor renderen ingesteld voor het contrast van het kleurverloop en worden labels ingesteld overeenkomstig de geclassificeerde waarden.

![image31](images/entries/81480226-42fbc500-91f6-11ea-91fd-3d430693d551.webp)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Snappen aan elementen van mazen
Voegt een methode toe aan de API om aan elementen van mazen te snappen.

De methode geeft de positie van het gesnapte punt op het dichtstbijzijnde element van mazen terug. 
- Voor een punt is de gesnapte positie de positie van het punt
- Voor een rand is de gesnapte positie het geprojecteerde punt op de rand, of de extremiteit van de rand indien buiten de rand
- Voor een zijde is de gesnapte positie het zwaartepunt van de zijde

De teruggegeven positie is in kaartcoördinaten.

![image32](images/entries/f11b278c71fecee8445ff29077bfddef543b564d.gif)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: 1D variëren van breedte/kleur van mazen
Deze mogelijkheid verschaft een nieuwe manier om 1D-mazen te renderen met dikten van randen die kunnen variëren met hun waarden. Dus nu kunnen breedte en kleur variëren, afhankelijk van de waarde op de randen of op punten.

De gebruiker kan de min/max-waarde en min/max-breedte definiëren om het renderen in te stellen.

Voor kleur kan de gebruiker een contrast voor het kleurverloop definiëren (net zoals voor 2D-mazen en raster).

Voor dit nieuwe renderen worden nieuwe algemene klassen geïntroduceerd, die buiten het framewerk voor mazen kunnen worden gebruikt.

![image33](images/entries/80013358-bb475400-849c-11ea-95c8-71b04382a927.gif)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Ondersteuning voor meerdere lagen met mazen (vanaf MDAL 0.5.91)
In aanvulling op het bijwerken naar MDAL 0.5.91, staat deze mogelijkheid toe dat meerdere lagen met mazen worden geladen uit één bestand.

Het bestand wordt geparset en een dialoogvenster voor een sub-laag, dat dezelfde logica gebruikt als voor vector- of rasterlagen, wordt geopend.

![image34](images/entries/78789841-b1413380-797b-11ea-9c7b-f31cb9756809.gif)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Laag met mazen verbinden met QGIS framewerk Tijdbeheer
![image35](images/entries/77872855-31e29000-7216-11ea-80fb-82e351dbb4a2.gif)
#### Afhandelen van tijd in een laag met mazen
De tijd in een laag met mazen wordt gedefinieerd door :
- Een referentietijd die door de gegevens, het project of de gebruiker wordt verschaft
- Elke gegevensset wordt geassocieerd met relatieve tijden
- Tijdperiode wordt gedefinieerd door de eerste en de laatste tijd van alle gegevenssets

```
    Reference time :          AT
    Dataset 1 time            o---RT------RT-----RT-----------RT
    Dataset 2 time            o-------RT------RT--------RT
    Dataset 3 time            o--------------------------RT-------RT------RT
    Time extent of layer      o----<---------------------------------------->

    -  AT : absolute time (QDateTime)
    -  RT : relative time (qint64)
```
De klasse **QgsMeshDataprovidertemporalCapabilities** slaat de door de gegevens verschafte referentietijd en alle relatieve tijden van de gegevensset op. Deze klasse is in staat een index voor de gegevensset uit een groep voor de gegevensset terug te geven en een relatieve tijd vanaf de referentietijd. De referentietijd (die anders mag zijn dan de referentietijd van de provider) en de absolute tijdperiode worden opgeslagen in de klasse **QgsMeshTemporalProperties**

De instellingen voor Tijdbeheer in de widget Eigenschappen zijn alleen de referentietijd en de tijdseenheid van de provider: ![image36](images/entries/77871643-bf23e580-7212-11ea-9b92-82c906c19c22.webp)

De standaard referentietijd van de laag wordt ingesteld door (gesorteerd op prioriteit):
- Vanuit de gegevensprovider indien gedefinieerd in de gegevens
- Vanuit het project indien gedefinieerd
- Vanuit de huidige datum met tijd 00u00

De gebruiker kan het wijzigen als hij dat wil.
#### Principe voor renderen 
De renderers 2D en 3D hebben toegang tot de index van de actieve gegevensset vanuit de laag waarvan de tijdperiode is opgeslagen in de `QgsContextRenderer` en in de `Qgs3DMapSettings` : Relatieve tijd wordt berekend als het verschil tussen de tijdperiode van `QgsContextRenderer` en de referentietijd die is opgeslagen door `QgsMeshTemporalProperties`. De index voor de gegevensset komt uit de `QgsMeshDataproviderTemporalCapabilities`, die de relatieve tijd in kaart brengt met de index van de gegevensset.

De gegevens worden vanuit de provider gebracht met de index van de gegevensset.
#### Statische gegevensset
Er is ook de optie om een statische gegevensset in te stellen, dat is: om een gegevensset te kiezen die onafhankelijk zal worden gerenderd van QGIS Tijdbeheer. De gebruiker kan, om dat te doen, het keuzevak selecteren aan de onderzijde van de pagina voor Tijdbeheer van de widget Eigenschappen: ![image37](images/entries/77871772-20e44f80-7213-11ea-8988-a51ec78c1320.webp). Voor nu, omdat het eenvoudiger was om te implementeren en het mogelijk te maken de gegevens direct te kiezen, kan de gebruiker onafhankelijk kiezen tussen een scalaire gegevensset en een vectorgegevensset uit combinatievakken waarin de tijd voor elke gegevensset is geassocieerd (relatieve tijd voor gegevens zonder referentietijd). Indien vereist, zou een unieke tijd kunnen worden geïmplementeerd, maar dat zou kunnen leiden tot inconsistente resultaten met niet-synchrone gegevenssets. De instellingen voor de statische gegevensset staan op de pagina Tijdbeheer, maar kunnen eenvoudig worden ingevoerd in de pagina Bron, indien gewenst.

Dit werd mogelijk gemaakt door [Lutra Consulting](https://www.lutraconsulting.co.uk)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Resamplen vanuit waarden voor punten naar waarden voor zijden
Resamplen is beschikbaar voor gegevenssets die zijn gedefinieerd op zijden, bijv. de waarden voor punten wordt berekend uit waarden op zijden.

Deze mogelijkheid implementeert resamplen vanuit waarden voor punten naar waarden op zijden met behulp van de methode Neighbor average.

De standaardmethode is ingesteld op \"geen\" voor resamplen vanuit punten naar zijden en op \"neighbor average\" voor resamplen van zijden naar punten. Dan wordt het standaard renderen altijd glad. ![image38](images/entries/77320848-acc41c00-6ce7-11ea-85af-2bff553ecbb5.gif)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Vector gegevensset met mazen kleuren met contrast voor kleurverloop
Deze mogelijkheid stelt de gebruiker in staat de vector gegevensset met mazen (pijl, stroomlijnen, sporen) te kleuren met contrast van het kleurverloop, afhankelijk van de grootte van de vector.

![image39](images/entries/77156534-ed1c6380-6a75-11ea-8b97-a13d3ea27ede.webp)

![image40](images/entries/77156669-2c4ab480-6a76-11ea-9209-d0144fbfc3f0.webp)

![image41](images/entries/77156736-5bf9bc80-6a76-11ea-827b-bb55ce52b814.webp)

Dit werd mogelijk gemaakt door [Deltares](https://www.deltares.nl/en/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Stijl opslaan voor laag met mazen
Deze mogelijkheid voegt de optie toe om de stijl voor een laag met mazen op te slaan in een bestand QML, zoals die worden gebruikt voor vector- en rasterlagen.

Deze mogelijkheid past ook de stijl voor het menu Eigenschappen van raster- en vectorlagen aan.  ![image42](images/entries/76421493-1fdda200-637a-11ea-9e4b-71a596b18dd9.webp)

Dit werd mogelijk gemaakt door [Artelia Group](https://www.arteliagroup.com/en)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Renderer 1D-mazen 
Bijgewerkt naar [MDAL 0.5.90](https://github.com/lutraconsulting/MDAL/releases/tag/0.5.90)

Initiële implementatie van [Support of 1D elements in Mesh Layers](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/164)

1D-mazen bestaan uit punten en randen. Een rand verbindt twee punten en kan eraan toegewezen gegevens hebben (scalaire of vectors). Het netwerk voor 1D-mazen kan, bijvoorbeeld, worden gebruikt voor het modelleren van een stedelijk drainagesysteem.

Er zijn nieuwe opties om 1D-mazen (randen) weer te geven op de tab Mazen ![image43](images/entries/75885078-2aea7c80-5e26-11ea-8435-eef74afce7b7.webp)

Ook voor gegevens voor 1D-mazen (randen of punten) zijn er nieuwe opties op de tab Contouren

![image44](images/entries/75885122-3b9af280-5e26-11ea-96a3-f4a4e48c040e.webp)

Onthoud dat niet alle functionaliteiten, beschikbaar voor 2D-mazen, beschikbaar is, met name
- Ondersteuning voor Mazen berekenen voor 1D-mazen
- 3D-renderen van 1D-mazen
- Identificeren en plotten in Crayfish (zal later, met het volgende PR, worden toegevoegd)

Sommige functies zijn niet nodig voor 1D-mazen, speciaal
- Exporteren van contouren van mazen

Deze mogelijkheid werd ontwikkeld door [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Mogelijkheid: Mazen vereenvoudigen
Omdat een laag met mazen miljoenen driehoeken zou kunnen hebben, zou renderen heel traag kunnen zijn, speciaal als alle driehoeken worden weergegeven in de weergave, zelfs als driehoeken te klein zijn om te worden gezien.

Voor deze situaties verschaft deze mogelijkheid een optie om de mazen te vereenvoudigen. Vereenvoudiging leidt tot één of meer vereenvoudigde mazen die niveaus van detail vertegenwoordigen. Bij het renderen van de laag met mazen wordt het van toepassing zijnde niveau van detail gekozen om adequaat renderen te verschaffen, afhankelijk van de weergave.

Een nieuwe tab in de widget met eigenschappen voor de laag met mazen stelt de gebruiker in staat de instellingen te wijzigen :
- De verkleiningsfactor wordt gebruikt om mazen te vereenvoudigen; het aantal driehoeken voor elk niveau van detail is bij benadering gelijk aan het aantal driehoeken van het vorige niveau van detail, gedeeld door de verkleiningsfactor
- Maximale resolutie voor mazen: dit is de gemiddelde grootte (in pixels) van de driehoeken waarvan is toegestaan dat zij worden weergegeven; Als de gemiddelde grootte van de mazen kleiner is dan deze waarde, zullen mazen met een lager niveau van detail worden weergegeven, d.i. mazen met een gemiddelde grootte die net iets groter is dan de maximale resolutie voor mazen.

![image45](images/entries/74750757-9e936380-5242-11ea-98cf-a0e3e6694831.webp)

Deze mogelijkheid maakt het mogelijk het renderen te versnellen, zoals weergegeven in deze tabellen (resultaten in milliseconden): ![image46](images/entries/74750903-d69aa680-5242-11ea-9be3-0af7b2beacaf.webp)

Demo GIF voor: ![image47](images/entries/74751034-0cd82600-5243-11ea-8a02-de78a337f299.gif)

Na: ![image48](images/entries/74751042-12357080-5243-11ea-80cb-2a3217d03a78.gif)

Dit werd mogelijk gemaakt door [BMT](https://www.bmt.org/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## 3D-objecten
### Mogelijkheid: Pijlen voor renderen van 3D gegevensset voor laag met mazen
Deze mogelijkheid voegt een optie toe voor het weergeven van pijlen op een 3D-entiteit gegevensset voor een laag met mazen, afhankelijk van een vector gegevensset.

De gebruikte gegevensset om pijlen te renderen is die, welke is gekozen voor het renderen van vectors bij 2D-renderen.

Op dezelfde manier worden de kleuren voor de pijlen gedefinieerd in de instellingen voor 2D-renderen voor de vector gegevensset.

In instellingen voor 3D kan de gebruiker de afstand voor de pijlen definiëren en of de grootte vast is of geschaald op grootte.

Deze instelling voor afstand definieert ook de maximale grootte van de pijlen, omdat pijlen niet mogen overlappen. ![image49](images/entries/76225819-6a80e200-61f3-11ea-88da-43e70c358530.webp)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Afdruklay-outs
### Mogelijkheid: Instellingen Tijdbeheer voor lay-out kaartitems
Deze mogelijkheid voegt een in te klappen gedeelte toe aan de widget voor lay-out kaartitems, dat gebruikers in staat stelt een tijdperiode in te schakelen en in te stellen die moet worden gebruikt bij het renderen van de inhoud van de kaart.

De waarden DateTime voor begin en eind mogen data-bepaald zijn, wat handig kan zijn indien gebruikt naast objecten voor Atlas.

![image50](images/entries/265d07738c1cec8a398ce5503330a520f98d4526.gif)

Dit werd mogelijk gemaakt door iMHere Asia

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Mogelijkheid: Sorteren van de attributentabel op een veld, dat niet in de tabel vermeld is, toestaan
In plaats van hetzelfde gegevensmodel te gebruiken voor de weergegeven en gesorteerde kolommen, worden nu twee gegevensmodellen gebruikt. Zij gebruiken dezelfde API / basisklasse, omdat zij heel erg op elkaar lijken.

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Beheer weergeven over het gedrag bij het splitsen van de legenda van de laag op een laag-per-laag basis
Dit staat gebruikers toe om handmatig de standaardinstelling voor \"lagen splitsen\" voor de legenda te overschrijven op een laag-per-laag basis, door dubbel te klikken op een laag in het paneel voor de legenda van de lay-out en te kiezen of die laag:
- de standaardinstelling voor de legenda volgt bij splitsen
- ALTIJD mag worden gesplitst over meerdere kolommen (ongeacht de instelling voor de legenda)

of
- NOOIT mag worden gesplitst over meerdere kolommen (ongeacht de instelling voor de legenda)

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Aanpassen van symbolen voor delen en subdelen toestaan als afzonderlijk van horizontale symbool voor de schaalbalk
Staat opmaken van symbolen voor delen en subdelen op een andere manier, vergeleken met het horizontale lijnsymbool in een schaalbalk, toe

Gesponsord door SLYR

Gebouwd naar aanleiding van het vele werk dat werd gedaan door \@agiudiceandrea!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Overschrijven van het standaardsymbool voor de knoop van een legenda toestaan
Dit stelt gebruikers in staat om (optioneel) het uiterlijk van een symbool voor de knoop van een legenda aan te passen. Bijvoorbeeld om de kleuren of grootten van symbolen aan te passen om een beter \"representatief\" symbool te verschaffen. Vergeleken met hoe deze overeenkomende objecten in feite worden weergegeven op de kaart.

Het is nuttig voor het overdrijven van de dikte van symbolen, of voor het handmatig aanpassen van de kleuren van semitransparante symbolen, zodat de kleuren het feitelijke uiterlijk van de symbolen weergeven. Als ze worden gerenderd bovenop de inhoud van de kaart. Of om de interval/verschuiving voor markeringen in markeringslijnen aan te passen, zodat de markeringen netjes zijn uitgelijnd in de legenda.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Plaatsen van handmatige kolomeinden in legenda's toestaan
Voegt, bij het configureren van een item voor de legenda, de optie  toe om een kolomeinde te plaatsen vóór het item, wat er voor zorgt dat het wordt geplaatst in een nieuwe kolom.

Dit geeft de gebruiker beheer over de inhoud van kolommen, voor gevallen waarin het automatisch maken van kolommen niet het gewenste resultaat geeft.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Subdelen toegevoegd in streepjes rechter segmenten schaalbalk
Voegt de mogelijkheid toe om sub-delen voor segmenten te maken die zijn opgenomen in het rechter gedeelte van de schaalbalk met streepjes.

Lijnstreepjes boven ![image51](images/entries/80860629-47116b00-8c69-11ea-83d8-61f27cb77e68.webp)

Lijnstreepjes midden ![image52](images/entries/80860663-6c9e7480-8c69-11ea-94a3-8d0e8544867d.webp)

Lijnstreepjes onder ![image53](images/entries/80860675-7b852700-8c69-11ea-984d-584eff1e3c95.webp)

Eigenschappen item Schaalbalk - groepsvak Segmenten ![image54](images/entries/81009703-653bbe80-8e55-11ea-9286-4850b32edb23.webp)

Het gedrag dat is gerelateerd aan de segmenten aan de linkerkant van de schaalbalk blijft ongewijzigd.

Deze mogelijkheid werd ontwikkeld door [Andrea Giudiceandrea](https://api.github.com/users/agiudiceandrea)
### Mogelijkheid: Overschrijven van grootte van de vorm van het symbool voor legenda op een per-item basis toestaan
Geeft gebruikers de mogelijkheid om de grootte van de vorm van het symbool in de legenda, voor individuele knopen van de legenda, te overschrijven, door op de knoop dubbel te klikken

Breedte en hoogte kunnen individueel worden overschreven, waarbij de knoop terugvalt naar de standaardbreedte of -hoogte als het overschrijven niet wordt ingesteld.

Gesponsord door SLYR ![image55](images/entries/80325577-0edce780-8879-11ea-82bd-8f323a4c68ab.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Beheer toestaan over de horizontale afstand vóór groepen/sub-groepen/symbolen van de legenda 
Geeft flexibiliteit om \"nesten\" van groepen/subgroepen/symbolen van de legenda toe te staan en veel meer beheer over de plaatsing van het item Legenda.

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Modelvormen van de legenda beheren door Stijlmanager
Deze update beëindigt het werk aan het recente aanpassen van modelvormen voor de legenda, door ondersteuning voor de modelvormen van de legenda toe te voegen aan de Stijlmanager!

Nu hebben we nog slechts een leuke set van standaard modelvormen nodig om bij te voegen!!

![image56](images/entries/79927419-0c4a4e80-8483-11ea-9b87-7ed8b393d349.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Configureren van modelvormen voor de legenda, door dubbel te klikken op items Legenda, toestaan
Gebruikers toestaan om aangepaste modelvormen voor items in te stellen door een WKT-tekenreeks in te voeren die de geometrie voor de vorm weergeeft.

Gesponsord door SLYR

![image57](images/entries/79714030-ea31be80-8312-11ea-8b6f-f40e3eea04b1.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor het direct in lay-outs plakken van afbeeldingen
Bedt de geplakte afbeelding in de lay-out in.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Markeringsitems toestaan om rotatie te synchroniseren met kaarten
Dit maakt het maken van noordpijlen vanuit markeringssymbolen mogelijk, wat dezelfde opties weergeeft als die bestaan voor items Afbeelding die optreden als noordpijlen.

Wanneer een markering wordt gebruikt als noordpijl, wordt roteren voor de kaart TOEGEVOEGD aan bestaande rotatie voor de symbolen voor markering (bijv. als u de markering driehoek 90% moet roteren om hem recht overeind te laten wijzen, zal het nog steeds goed werken in de modus Noordpijl!)

![image58](images/entries/78468312-2c2b0400-775a-11ea-926e-2acf7ec15aa4.webp)

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Nieuwe type symbolen voor symbolen voor markering
Maakt het mogelijk symbolen voor markering direct in lay-outs te plaatsen, bijv. voor handmatig plaatsen van markeringen over een kaartitem of voor het maken van geavanceerde aangepaste legenda's.

Eerder moest u een hack uitvoeren om hier ondersteuning voor te krijgen, bijv. door het tekenen van rechthoeken met symbolen met vulling voor zwaartepunten. Veel beter om een aangewezen type item daarvoor te hebben, wat meer specifieke opties voor aanpassingen mogelijk maakt (binnenkort!)

Gesponsord door SLYR

![image59](images/entries/78419618-c885d580-768a-11ea-959a-8459e19e05df.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Inhoud vanaf klembord importeren voor vaste tabelitems toegevoegd
Een nieuwe mogelijkheid voor het importeren van inhoud vanaf het klembord is toegevoegd aan de tabelbewerker van QGIS om het sneller bewerken en maken van de lay-out van vaste tabelitems in te schakelen.

![image60](images/entries/e7f2b64e48b0726bc03e2d4fa9424feabde1808d.gif)

Dit werd mogelijk gemaakt door iMHere Asia

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Mogelijkheid: Numerieke opmaak stijl \"breuk\" toegevoegd
Deze stijl geeft decimale getallen weer als breuken, bijv. \"3/4\" in plaats van 0,75.

Opties omvatten het gebruiken van tekens voor Unicode superscript en subscript voor nettere typografie, bijv. ¹⁷/₂₃ (dit is de standaardmodus; uitschakelen van deze optie gebruikt de indeling \"17/23\"). Een optie bestaat ook voor het gebruiken van aangewezen tekens voor Unicode voor specifieke breuken (waar een teken Unicode voor bestaat), bijv. ½ of ¾.

Uiteindelijk maakt dit het maken van schaalbalken met weergave in breuken van afstanden mogelijk, bijv. 0 \-\-\-\-- ½ \-\-\-\-- 1 km (in plaats van 0 \-\-\-\-\-- 0,5 \-\-\-\-\-- 1km)

Gesponsord door SLYR

![image61](images/entries/77267662-0c71f580-6cef-11ea-9956-917e1d6ef496.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Stijlen \"staplijn\" en \"hol\" voor schaalbalk toegevoegd
Voegt twee nieuwe stijlen voor de schaalbalk toe (die beschikbaar zijn in ArcMap, maar eerder onmogelijk waren te reproduceren in QGIS)

Stijl Staplijn:

![image62](images/entries/77247015-c1b59680-6c78-11ea-92a9-7bbb2ba8638a.webp)

Hol (alias stijl \"Zuid-Afrikaans\"):

![image63](images/entries/77247024-dc880b00-6c78-11ea-827a-344645cec248.webp)

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Mogelijk tot instellen lijnstijl voor schaalbalk met standaard lijnsymbolen van QGIS
In plaats van de eerdere instellingen voor de lijnstijlen kleur/dikte/eind, geven we nu de optie weer als een volledig lijnsymbool voor meer geavanceerd stijlen.

Ook enig opruimwerk in de code.

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Opnieuw bewerken van de UI en gedrag voor item Afbeelding
Voegt een expliciete keuze toe tussen bronnen SVG of rasterafbeelding, die ons in staat stellen het paneel voor het configureren van afbeeldingen voor lay-out op te ruimen bij het verbergen van opties die niet van toepassing zijn voor een bepaalde afbeeldingsbron. Stelt ons ook in staat om:
- De standaard widget voor selecteren van SVG te hergebruiken, wat afbeeldingen laadt in een thread op deachtergrond
- Gebruikt de standaard tekstbewerker voor selectie van SVG en afbeeldingen, wat het slepen en neerzetten van afbeeldingen mogelijk maakt, en opties weergeeft om afbeeldingen in te bedden en te koppelen aan bronnen online

Uiteindelijk is de motivatie hiervoor de wens om gebruikers toe te staan afbeeldingen in te bedden in lay-outs en sjablonen voor lay-outs

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: CRS beheerbaar maken door een variabele
Dit maakt het CRS voor een kaart beheerbaar door een variabele.

![image64](images/entries/74844265-348ac500-52fb-11ea-9198-78f4f9022ac1.webp)

Gerelateerd aan #34547

Deze mogelijkheid werd ontwikkeld door [Alex](https://api.github.com/users/roya0045)
## Expressies
### Mogelijkheid: Nieuwe expressies
- `ascii`
- `make_interval` Maakt direct construeren van waarden voor intervallen uit waarden years/months/weeks/days/hours/minutes/second mogelijk, zonder eerst een weergave tekenreeks van het interval te moeten maken
- `maptip`
- `layer_property('distance_units')`
- `display_expression`
- `eval_template`
- `make_date`
- `make_time`
- `make_datetime`
- `close_line`
- `is_multipart`
- geometrie Z en M minimum en maximum
- `@frame_number`
- `@frame_rate`
- `@frame_duration`
- `@map_start_time` Begin van de tijdsperiode van de kaart (als een waarde datetime)
- `@map_end_time` Einde van de tijdsperiode van de kaart (als een waarde datetime)
- `@map_interval:` Duur van de tijdsperiode van de kaart (als een waarde interval)
- `@animation_start_time`
- `@animation_end_time`

Deze mogelijkheid werd ontwikkeld door Etienne Trimaille, Jan Caha, Julien Monticolo, Nyall Dawson
### Mogelijkheid: Browser voor objecten voor voorbeeld in expressiebouwer
Dit voegt een browser voor objecten toe aan de expressiebouwer, zodat iemand door objecten kan bladeren om het resultaat van de expressie te zien ![image65](images/entries/80604352-e6e4b400-8a31-11ea-8f3b-8c864e124c78.webp)

Een nieuwe widget is toegevoegd: `QgsFeaturePickerWidget`. Voor dit moment is het een eenvoudig combinatievak (maar erft widget, dus kunnen we later een knoop voor het selecteren van de kaart eraan toevoegen). Het gedraagt zich op dezelfde manier als die in de widget relatieverwijzing (een bewerkbaar combinatievak).

Het vertrouwt op hetzelfde basismodel (`QgsFeatureFilterModel`). Een nieuwe abstracte klasse `QgsFeaturePickerModelBase` hergroepeert de logica ervan en het nieuwe model is genaamd `QgsFeaturePickerModel`. In de basis gebruikt `QgsFeaturePickerModel` het object-ID om de objecten te identificeren, terwijl `QgsFeatureFilterModel` een lijst met attributen gebruikt (de vreemde sleutels van een relatie). Het ruimt het vorige model een beetje op, omdat dat nogal \…vol was.

Als een opmerking terzijde: ik probeerde sjablonen te gebruiken voor `QgsFeaturePickerModelBase`, maar omdat sjablonen niet kunnen worden gemixt met Q_OBJECT, zouden alternatieven leiden tot minder leesbare code.

Testen zijn toegevoegd.

Gesponsord door de **QGIS Zwitserse gebruikersgroep**!

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Het is mogelijk aangepaste functies te verwijderen
Voegt een knop voor verwijderen toe aan de tab Functiebewerker in het  dialoogvenster Expressiebouwer om het verwijderen van gebruikersfuncties uit QGIS mogelijk te maken, zonder naar de map voor het gebruikersprofiel te hoeven navigeren.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Bewerken, importeren en exporteren van expressies van gebruikers mogelijk gemaakt
Een nieuwe knop is toegevoegd die het bewerken van opgeslagen expressies mogelijk maakt. Die is alleen actief als een gebruikersexpressie is geselecteerd in de boom met expressies. Als erop wordt gedrukt, opent een venster dat het mogelijk maakt dat de momenteel geselecteerde gebruikersexpressie wordt bewerkt. Wijzigen van het label van de expressie maakt een kopie van de momenteel bestaande. [Demo](https://imgur.com/w3UEOoR)

**Importeren/Exporteren**

Een nieuwe knop met een menu is toegevoegd, die het mogelijk maakt gebruikersexpressies te importeren/exporteren naar/vanuit een bestand JSON. Klikken op een van de menu-items opent een dialoogvenster voor bestandsselectie voor de/het bron/doel van het bestand van JSON voor de expressies. In het geval van conflicten met het label, vraagt een aanvullend dialoogvenster hoe door te gaan - ofwel overschrijven of de huidige expressie overslaan. [Importeren/Exporteren demo](https://imgur.com/0eiaFfu)

Deze mogelijkheid werd ontwikkeld door [Ivan Ivanov](https://api.github.com/users/suricactus)
## Digitaliseren
### Mogelijkheid: Toegewezen modus Kruisen/overlappen van geometrie voorkomen
Deze versie van QGIS komt met een nieuwe modusinstelling voor het vermijden van kruisen/overlappen van geometrie, bij het digitaliseren van objecten.

| De drie beschikbare modi zijn:

|

Kruisen/overlappen toestaan

|

Kruisen/overlappen op actieve laag vermijden

|

Kruisen/overlappen op gebruikergedefinieerde lagenlijst vermijden

|

De lagenlijst voor de derde modus wordt door de gebruiker ingesteld via de widgets voor het configureren van geavanceerd snappen.

![image66](images/entries/caa646295d6f1cf6297864810637e9f8ceddc102.webp)

Dit werd mogelijk gemaakt door [OpenGIS.ch](http://www.opengis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Mogelijkheid: Nieuwe modi voor snappen: Zwaartepunt en midden van een segment (middelpunt)
Deze mogelijkheid is gericht op het verbeteren van [modi voor snappen in QGIS](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/107) door dichter bij de ervaring van CAD-programma\'s te komen.

Het voegt twee nieuwe modi toe. Snappen aan het midden van een geometrie (zwaartepunt) en het midden van een segment.

Verschillende modi voor snappen kunnen tegelijkertijd worden geselecteerd, om het selecteren van deze nieuwe modi toe te staan.

![image67](images/entries/71798125-35201280-3051-11ea-959d-a5897ca3391a.webp)

De volgorde van voorkeur voor snappen is de volgende: - Hoekpunt, Kruising - Midden - Zwaartepunt - Rand - Gebied

![image68](images/entries/71799417-7e726100-3055-11ea-8e07-3792dbc741c2.gif)

Gesponsord door: Qwat groep / Stad Lausanne ( \@ponceta \@dsavary ) / Oslandia en enige vrije tijd

Deze mogelijkheid werd ontwikkeld door [lbartoletti](https://api.github.com/users/lbartoletti)
### Mogelijkheid: Snappen aan het huidige te digitaliseren object
Snappen kan nu ook snappen aan het object dat momenteel wordt gedigitaliseerd. Deze optie wordt in-/uitgeschakeld door een nieuwe knop op de werkbalk Snappen.

Dit schakelt enkele leuke CAD-achtige mogelijkheden voor bewerken in, zoals het sluiten van objecten onder een hoek van 90° of het precies uitlijnen van segmenten binnen een object. Het is bijzonder efficiënt als men gewend is aan het gebruiken van de sneltoets Alt+A om de hoek te vergrendelen.

![image69](images/entries/81065380-a37bc100-8edb-11ea-8aed-6fd52d843a26.gif)

Dit werd mogelijk gemaakt door Kanton Solothurn en Land Vorarlberg

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Mogelijkheid: Traceren ondersteunt nu gebogen geometrieën
Het gereedschap Traceren maakt nu gebogen geometrieën bij het werken op een laag die gebogen geometrieën ondersteunt.

![image70](images/entries/79769829-e3b04080-832c-11ea-9029-981e3a3ecf1b.gif)

De ondersteuning is nog experimenteel, dus moet deze mogelijkheid worden ingeschakeld in de opties voor digitaliseren.

Dit werd mogelijk gemaakt door ecoptima en Planteam

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang (OPENGIS.ch)](https://api.github.com/users/olivierdalang)
## Formulieren en widgets
### Mogelijkheid: Bewerken van links in widget Bestand toestaan
In een formulier kunnen links nu worden bewerk de widget Bestand (als de widget niet alleen-lezen is).

![image71](images/entries/81038564-bcb64a80-8ea6-11ea-8289-46340dee9a88.gif)

Gesponsord door de QGIS Zwitserse gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Expressie-beheerde labels (aliassen)
Deze nieuwe mogelijkheid maakt het mogelijk dat labels in formulieren (aliassen) worden geëvalueerd in de context van het formulier.

![image72](images/entries/78998144-46912300-7b48-11ea-9fbf-232d11fbeff6.webp)

![image73](images/entries/78904645-26486200-7a7d-11ea-84b0-b9e96c0c9797.gif)

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Beschrijving toevoegen aan widget Waarde relatie
Voegt een optie toe voor het toevoegen van een beschrijving aan elke waarde in een widget Waarde relatie. De beschrijving zal zichtbaar zijn als helptip

Excuses voor de verschillende talen in de demonstratievideo.

![image74](images/entries/76538031-f195ba80-647e-11ea-9a41-271576e315bc.gif)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Mogelijkheid: Widget Nieuwe database tabelnaam
Een nieuw widget werd aan QGIS toegevoegd om een nieuwe tabel uit een bestaande verbinding naar een database te selecteren:

![image75](images/entries/76504669-70233580-6448-11ea-9194-173ae0d344ce.gif)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: Waarden huidige ouderformulier ophalen in kindformulieren
Deze mogelijkheid voegt de optie toe om huidige waarden uit het \"ouder\"-formulier in filterexpressies te gebruiken (voor nu alleen in widgets Waarde-relatie: te gebruiken in filters voor dieper zoeken).

Een nieuw bereik "parentForm" werd toegevoegd, alsook een nieuwe set functies en variabelen om toegang te verkrijgen tot het ouderformulier binnen een ingebed kindformulier. De nieuwe functies en variabelen werden gemodelleerd op de bestaande \"current_value\", \"current_feature\" etc.

De nieuwe functies en variabelen zijn ook beschikbaar als het ouderformulier is geopend in een nieuw (niet opgeslagen, niet gebufferd) object. Wat het gemakkelijker maakt filters voor dieper zoeken te maken, gebaseerd op de waarden van de ouder, bij het toevoegen van kinderen uit een niet opgeslagen ouderformulier.
### Voorbeeld
![image76](images/entries/75692656-28f9af80-5ca6-11ea-8dd6-9a4bf454f5b7.gif)
### Nieuwe functies en variabelen
![image77](images/entries/75693398-2ba8d480-5ca7-11ea-8be0-9643f8841c89.webp) ![image78](images/entries/75693402-2cda0180-5ca7-11ea-9d65-f0c00e26180e.webp) ![image79](images/entries/75693404-2d729800-5ca7-11ea-889d-5aa73bc131ce.webp)

Mogelijk gemaakt door: **ARPA Piemonte**

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Widget Relatie: keuzevak toegevoegd om de knop voor bewerken van kinderen te verbergen
Dit is bijzonder nuttig voor ingebedde formulieren.

Mogelijk gemaakt door: **ARPA Piemonte**

![image80](images/entries/75524592-82e04800-5a0e-11ea-9333-461a0d02a1c0.webp)

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Widget Relatie forceert onderdrukken van pop-up
Voegt een optie toe aan de configuratie van de widget Relatie om het openen van pop-up in een formulier te onderdrukken, als nieuwe objecten worden toegevoegd in de context van een ingebed formulier.

Deze optie overschrijft de optie op het niveau van het formulier (wat nog steeds het gewenste gedrag zou kunnen zijn als het formulier wordt gebruikt als een zelfstandig formulier).

![image81](images/entries/75249972-9786cb00-57d7-11ea-8100-3426d32831db.webp)

Opmerking: het uiteindelijke label is **Formulier verbergen bij toevoegen nieuw object forceren**

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
## Legenda van laag
### Mogelijkheid: Verplaats naar onderste toegevoegd aan contextmenu in weergave lagenboom
Verplaatsen van lagen in grote projecten werd al gemakkelijker gemaakt met *Verplaats naar bovenste*, maar men moest nog steeds handmatig basiskaarten verplaatsen naar de onderzijde van de lagenlijst, een bewerkelijke taak in grote lagenbomen. Deze mogelijkheid voegt een optie *Verplaats naar onderste* aan het contextmenu van de lagenboom toe dat op dezelfde manier werkt als Verplaats naar bovenste.

Deze mogelijkheid werd ontwikkeld door [uclaros](https://api.github.com/users/uclaros)
### Mogelijkheid: Knop Groep toevoegen laten acteren als Geselecteerde groeperen als geselecteerde lagen \>= 2
Wanneer er meer dan één laag is geselecteerd en de gebruiker drukt op de knop *Groep toevoegen*, maak dan een nieuwe groep en plaats daar de geselecteerde lagen ook in! ![image82](images/entries/76710403-f624d200-670f-11ea-9a41-13420c7940e3.gif)

Deze mogelijkheid werd ontwikkeld door [uclaros](https://api.github.com/users/uclaros)
### Mogelijkheid: Hernoemen van het huidige kaartthema toestaan
Dit voegt de optie toe voor het hernoemen van een kaartthema uit het keuzemenu voor de kaartthema's.

![image83](images/entries/78195435-e29f9800-747f-11ea-95d2-604be58cf229-1.gif)

Deze mogelijkheid werd ontwikkeld door [Harrissou Sant-anna](https://api.github.com/users/DelazJ)
### Mogelijkheid: ALLE geselecteerde lagen in-/uitschakelen met de knop \"Spatie\"
Schakelt de zichtbaarheid van de momenteel geselecteerde lagen of groepen met de spatiebalk: ![image84](images/entries/77874799-cff64a80-7256-11ea-974b-c4084d1e01ae.gif)

Deze mogelijkheid werd ontwikkeld door [Ivan Ivanov](https://github.com/suricactus)
## Analyse-gereedschappen
### Mogelijkheid: Netwerk loggen - meer functionaliteit
Voegt enkele nuttige gereedschappen toe aan de netwerklogger:
- URL kopiëren
- Verzoek als JSON kopiëren 
- Log naar bestand opslaan (na een belangrijke waarschuwing aan gebruikers dat het log gevoelige informatie zou kunnen bevatten en daarom als vertrouwelijk zou moeten worden behandeld)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ingebouwd gereedschap voor loggen van netwerk
Dit gereedschap, dat beschikbaar is vanuit het nieuwe F12 paneel \"Debugging/Development tools\", is een eigen bewerking van de plug-in Network logger van \@rduivenvoorde.

Het geeft een lijst weer van lopende en voltooide netwerkverzoeken, naast heel veel nuttige details, zoals status van verzoek en antwoord, headers, fouten, SSL configuratiefouten, time-outs, status van de cache, etc.

Heeft ook heel veel nuttige mogelijkheden en om op te poetsen, zoals de mogelijkheid om verzoeken te filteren op sub-tekenreeksen van URL's en status, en u kunt met rechts klikken op verzoeken om de URL in een browser te openen of ze te kopiëren als een opdracht cURL.

Waarom willen we dit als een eigen bewerking in plaats van als een plug-in? Wel:
- Het is bijzonder nuttig, dus goed om out-of-the-box beschikbaar te hebben
- Door het te verplaatsen naar C++ kunnen we het proces voor loggen veel eerder opstarten dan dat een plug-in daar de mogelijkheid voor krijgt. Dit maakt het mogelijk dat het log aanvullende informatie kan bevatten, zoals verzoeken die worden ingediend door andere plug-ins die optreden voordat de plug-in Network logger is geladen (ook andere ingebouwde verzoeken, bijv. nieuwsfeed)
- Uitvoering is een doorlopende strijd geweest met de plug-in voor Python. Hoewel dit voor zover mogelijk een 1:1 port is als maar mogelijk is, zijn de problemen met de uitvoering op magische wijze opgelost. De klassen bevatten enkele bijzonder intensieve lijstbewerkingen, wat waarschijnlijk de oorzaak is van de povere uitvoering onder Python.

![image85](images/entries/77712469-95ef3380-701f-11ea-8fec-3eded258b4e9.gif)

Dit werd mogelijk gemaakt door [Meteorological Service of Canada](https://weather.gc.ca)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (voor Kartoza)](https://api.github.com/users/nyalldawson)
## Processing
### Mogelijkheid: Collectie algoritmen voor maken van willekeurige rasters
Met deze mogelijkheid hebben we een grote collectie van algoritmen voor het maken van willekeurige rasters toegevoegd. De algoritmen zijn in staat willekeurige rasters uit te voeren die specifieke verdelingen voor willekeurige getallen volgen. De volgende verdelingen zijn beschikbaar:
1. Willekeurige rasterlaag maken (binomiale verdeling)
2. Willekeurige rasterlaag maken (exponentiële verdeling)
3. Willekeurige rasterlaag maken (gamma verdeling)
4. Willekeurige rasterlaag maken (negatieve binomiale verdeling)
5. Willekeurige rasterlaag maken (normale verdeling)
6. Willekeurige rasterlaag maken (poisson verdeling)
7. Willekeurige rasterlaag maken (uniforme verdeling)

![image86](images/entries/6304472935d29f8292cf24c7cb0198e95a4de137.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Mogelijkheid: Laag vectortegel - deel 8 (schrijven in Processing)
Deze mogelijkheid voegt integratie voor Processing toe voor het schrijven van vectortegels. Het is slechts een verpakking rondom de bestaande klasse QgsVectorTileWriter.

Nieuwe algoritmen in de Toolbox van Processing:

![image87](images/entries/81117303-224a1b80-8f27-11ea-851d-f4271ce66ed3.webp)

Parameters voor algoritme voor XYZ:

![image88](images/entries/81117371-4279da80-8f27-11ea-9d8b-bbe1c78d9bf1.webp)

Parameters voor algoritme voor MBTiles:

![image89](images/entries/81117466-6ccb9800-8f27-11ea-85e7-9c9a1df87920.webp)

Lijst met invoerlagen:

![image90](images/entries/81117708-d6e43d00-8f27-11ea-866a-0c3bdbd97291.webp)

Details Invoerlaag:

![image91](images/entries/81117621-ae5c4300-8f27-11ea-993b-782d7de4a10e.webp)

Dit werd mogelijk gemaakt door [QGIS gemeenschap](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Nieuw algoritme voor Grafische modellen maken voor het maken van voorwaardelijke aftakkingen
Dit algoritme stelt gebruikers in staat om meerdere voorwaarden in te stellen (via expressies van QGIS), die er voor zorgen dat de corresponderende tak van het grafische model wordt uitgevoerd of overgeslagen, afhankelijk van het resultaat van het evalueren van de expressie.

![image92](images/entries/79409609-b6d4f400-7fe1-11ea-8f7a-f42542f3fbfe.gif)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Opnieuw ordenen invoer voor modellen toestaan
In plaats van het forceren van een quasi-willekeurige ordening van invoer voor modellen, geeft deze mogelijkheid een nieuwe optie \"Invoer modellen opnieuw ordenen\" in de ontwerper voor Grafische modellen. Die gebruikers beheersmogelijkheden geeft over de exacte volgorde van aan gebruikers weer te geven invoer voor hun model.

Geen onlogische volgorde meer, zoals een veldkeuze weergeven voordat de laag is gekozen waarop het is gebaseerd!

Gesponsord door NaturalGIS

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Validatie model uitstellen
In plaats van te forceren dat alle kind-algoritmen onmiddellijk geldig zijn en dat alle parameters juist zijn ingevuld, stelt deze mogelijkheid het valideren van het model uit tot de feitelijke uitvoering of tot wanneer een nieuwe actie \"Model valideren\" wordt getriggerd.

Een veelvoorkomende frustratie met de QGIS ontwerper voor Grafische modellen is dat het constant forceert dat modellen geldig moeten zijn, zelfs modellen waaraan nog wordt gewerkt. Dit betekent dat het onmogelijk is een component aan een model toe te voegen en slechts gedeeltelijk de instellingen te vullen — u dient alles van tevoren in te voeren. Als u zich halverwege realiseert dat u ergens anders in uw model een wijziging moet maken, is het onmogelijk om dat te doen zonder te annuleren en alle instellingen te verliezen die u al hebt geconfigureerd.

Deze wijziging ziet er op toe dat het valideren van het model wordt uitgesteld tot de feitelijke uitvoering. Modellen mogen tijdelijk ongeldig zijn (bijv. componenten voor het algoritme hebben die slechts gedeeltelijk geconfigureerd zijn). De ontbrekende vereiste waarden kunnen nu in een later stadium worden ingevuld, zonder bestaande instellingen te verliezen. Als een niet-geldig model wordt uitgevoerd, krijgt de gebruiker een waarschuwing met een beschrijving die hen informeert over de wijzigingen die zij moeten maken om de configuratie van het model te voltooien.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning toegevoegd voor verschillende typen rastergegevens in algoritme Constante rasterlaag maken
Met deze mogelijkheid hebben we een nieuwe gevorderde parameter **OUTPUT_TYPE** voor het algoritme *Constante rasterlaag maken*. Via deze parameter kunt u nu een gegevenstype voor de uitvoer specificeren voor uw constante rasterlagen.
- Byte
- Integer16
- Unsigned Integer16
- Integer32
- Unsigned Integer32
- Float32
- Float64

![image93](images/entries/b7b0b73f7d48104cb49f33ed2d453a70d188cbd6.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Mogelijkheid: Algoritme Raster afronden
Met dit nieuwe algoritme voor Processing stellen we QGIS in staat **Rasterwaarden af te ronden**.

De belangrijkste functionaliteit van het algoritme is ofwel standaard afronden naar boven/dichtstbijjzijnde/naar beneden van floating point celwaarden of afronden naar machten van een door de gebruiker gespecificeerd basis *n*. Het algoritme kan worden gebruikt met rasters van alle typen (zelfs rasters byte/integer bij het afronden nar machten van n) en uitvoeren van hetzelfde gegevenstype raster. Een standaard floating point afronden van een integer raster zal het kopiëren en een waarschuwing geven.

Het voorbeeld geeft een uitvoerraster weer dat is afgerond naar veelvouden van 10

![image94](images/entries/650983141141fc954abc96f79e5255e4634c5051.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Mogelijkheid: Kopiëren/knippen/plakken van componenten van modellen toestaan
Deze mogelijkheid stelt gebruikers in staat componenten van modellen te kopiëren en te plakken, zowel in hetzelfde model als tussen verschillende modellen

![image95](images/entries/78641463-a099aa80-78f4-11ea-8c0b-c6b6b72f0e7d.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Toevoegen van resultaten van Processing aan bestaande lagen toestaan
Bij het toevoegen van resultaten wordt aan gebruikers een paneel met velden getoond dat hen in staat stelt in te stellen hoe velden moeten worden geplaatst in de velden van de bestaande laag:

![image96](images/entries/78631098-b9976100-78de-11ea-8f18-f7c7473e0945.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Maken van groepsvakken in modellen toestaan
Voegt de volgende functiies toe aan de ontwerper voor Grafische modellen maken:
- De mogelijkheid de kleur van individuele opmerkingen in een model aan te passen
- Maken van \"Groepsvakken\" in modellen, die een visuele indicatie zijn van logisch aan elkaar gekoppelde componenten van het model, toestaan (bijv. \'Stappen voor voorbereiden van gegevens\', \'Stappen voor berekening NDVI\', \… etc.). Gebruikers kunnen de kleur en titel voor groepsvakken aanpassen.
- Direct navigeren naar groepsvakken vanuit het menu Beeld toestaan, wat helpt bij het navigeren door complexe modellen.

![image97](images/entries/78090538-bba87e00-740d-11ea-9476-144163d8f1ca.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Processing: waarden voor invoer en uitvoer voor kinderen weergeven na uitvoeren van model in ontwerper
Een afbeelding laat dit het beste zien! Na het uitvoeren van het algoritme in de ontwerper, ziet u nu de berekende waarden voor de invoeren en uitvoer voor elke kind-algoritme:

![image98](images/entries/77991113-5d749000-7366-11ea-986c-652f6e2229e7.webp)

Dit is bijzonder nuttig voor het debuggen van modellen \-- u kunt nu een veel helderder visueel beeld zien van de waarden door het model.

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Algoritme \"Log naar bestand opslaan\" voor modellen toegevoegd
Dit algoritme slaat de inhoud van het log voor de uitvoering op (tot het punt in het model waar het algoritme \'Log opslaan\' wordt uitgevoerd) naar een bestand.

Het kan worden gebruikt om automatisch het log voor debuggen op te slaan bij het uitvoeren van modellen, voor latere verwijzing en transparantie.

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### "Mogelijkheid: Direct uitvoeren van algoritmen op databasebronnen (en andere niet-schijf) toestaan zonder ze eerst in projecten te laden
Deze wijziging stelt gebruikers in staat om direct te bladeren naar niet op schijf gebaseerde bronnen voor lagen voor het verwerken van elke broninvoer voor objecten. Het maakt het mogelijk deze invoeren direct op te halen uit lagen van PostgreSQL, SQL-server, Oracle, WFS, AFS, etc zonder ze eerst te moeten laden in een project!

We maken volledig gebruik van de mogelijkheden van de QGIS browser om dit in te schakelen:

![image99](images/entries/77508685-fca50d80-6eb6-11ea-8190-a447847f55d9.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid : Geavanceerde opties per-object-bron weergeven voor invoer van Processing
Deze optie geeft geavanceerde opties per-object-bron weer, zoals:
- De mogelijkheid om het aantal uit de bron te lezen objecten te beperken. (Nuttig bij het ontwikkelen van modellen, u kunt gemakkelijk het uitvoeren van modellen testen met een kleine subset van een invoerlaag)
- De mogelijkheid om op een per-invoer basis de globale optie voor Processing, voor hoe ongeldige geometrieën af te handelen, te overschrijven. Nu kunt u met een gerust hart de standaardinstelling voor Processing bij de conservatieve instelling \"Uitvoeren van algoritme stoppen als geometrie ongeldig is\" laten staan door deze gemakkelijk te kunnen overschrijven voor een bepaalde invoer!

![image100](images/entries/77395930-64dbec80-6dee-11ea-9590-b7fadcd242c1.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Snappen aan raster voor modellen in ontwerper inschakelen
Deze update implementeert twee mogelijkheden voor het \"snappen\" van objecten in de ontwerper voor Grafische modellen maken van Processing:
1. Gebruikers kunnen een nieuwe optie \"Snappen inschakelen\" in het menu Beeld inschakelen, wat er toe zal leiden dat alle bewerkingen, voor verplaatsen of afmeting aanpassen van componenten, automatisch zal snappen aan rasters
2. Na het selecteren van enkele componenten, kunnen gebruikers Bewerken -\> Geselecteerde componenten aan raster snappen selecteren om handmatig slechts deze geselecteerde componenten te snappen.

Aanvullend heb ik een nuttige actie \"Alles selecteren\" toegevoegd voor het snel selecteren van alle componenten in een model.

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Algoritmen \"Filteren type geometrie\" en \"Filteren op type laag\" toegevoegd aan Processing
Deze update voegt twee nieuwe algoritmen toe aan Processing:
- \"Filteren op type geometrie\": Dit algoritme filtert objecten op hun type geometrie. Inkomende objecten zullen naar verschillende uitvoer wordt verwezen, gebaseerd op het feit of zij een geometrie punt, lijn of polygoon hebben. Het maakt het maken van modellen mogelijk die reageren op verschillende typen geometrie van de invoerlaag door verschillende logica toe te passen, afhankelijk van het type geometrie voor de invoer.
- \"Filteren op type laag\": Dit algoritme maakt het mogelijk voorwaardelijke aftakkingen van modellen te maken, gebaseerd op een type invoerlaag. Het maakt het bijvoorbeeld voor een model mogelijk om het feitelijke type laag van een algemene parameter \"map layer\" voor de invoer aan te passen, en te bepalen welke tak van het model als resultaat moet worden uitgevoerd.

Het voegt ook in de vereiste API toe om algoritmen toe te staan aftakkingen van een model te \"snoeien\", gebaseerd op hun berekende resultaten. Bijvoorbeeld een model dat de nieuwe vlag *FlagPruneModelBranchesBasedOnAlgorithmResults* teruggeeft, zal ervoor zorgen dat resterende delen van het model, die afhankelijk zijn van de uitvoer van dat algoritme, geheel worden overgeslagen ALS het algoritme niet die bepaalde uitvoer teruggeeft. (Dit is een al vooraf ingevoerde component voor een toekomstig algemeen algoritme \"Voorwaardelijke aftakkingen met expressies\", en wordt ook gebruikt door \"Filteren op type laag\" om de stroom van het model te beheren, gebaseerd op het type invoerlaag)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Algoritme \"Geometrieën Null verwijderen\" kan ook LEGE geometrieën verwijderen
Lege geometrieën bevatten geen coördinaten. Dus, net als geometrieën *null*, zijn lege geometrieën in de strikte betekenis geen ruimtelijke gegevens. Het algoritme *Geometrieën Null verwijderen* heeft nu een optie \"**Ook lege geometrieën verwijderen**\", om het voor gebruikers gemakkelijker te maken een vectorlaag op te schonen.

![image101](images/entries/76703713-81b34a00-66a1-11ea-9818-ebf771885206.webp)

Dit werd mogelijk gemaakt door [SwissTierras Colombia](https://swisstierrascolombia.com/)+

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: Meervoudig selecteren afhandeling toegevoegd aan ontwerper Grafische modellen bouwen, interactief afmetingen aanpassen
Voegt toe:
- De mogelijkheid om in één keer meerdere items te selecteren in de ontwerper van Grafische modellen bouwen
- De mogelijkheid om afmetingen van individuele of meerdere items te wijzigen
- De mogelijkheid om meerdere geselecteerde items te verwijderen
- Verbeterde interactie voor \"gereedschap\" in de ontwerper van Grafische modellen bouwen, die de benadering voor de ontwerper van lay-outs volgt (bijv. alt + spatie = zoom sleepmodus, en gereedschappen voor selecteren volgen hun soortgenoten in lay-outs dus Shift+selectie voegt toe aan de selectie, Ctrl+selectie verwijdert, etc.)
- Geselecteerde items kunnen worden verplaatst met de pijltjestoetsen

Refs NRCan Contract#3000707093

Hier is hoe dat er in actie uitziet (met een bijzonder lelijk uitziend testmodel dat ik gebruik!)

![image102](images/entries/76388083-f9d4f380-63b3-11ea-8f06-97249e85ac2e.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor Ongedaan maken/Opnieuw toegevoegd aan de ontwerper voor Grafische modellen bouwen
Maakt QGIS meer vergevingsgezind voor gebruikers!

Refs NRCan Contract#3000707093

Werkt net zoals u zou verwachten:

![image103](images/entries/76176510-c8fe8e00-61fc-11ea-90e1-91cbeadcbd4f.gif)

Merk op dat we de gehele definitie van het model in de stapel Ongedaan maken opslaan, niet slechts de betrokken wijzigingen van componenten.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Waarden van parameter onthouden tussen uitvoeringen van ontwerper van Grafische modellen bouwen
Bij het ontwerpen van een model, zullen gebruikers gewoonlijk het model vele keren dienen uit te voeren als zij zijn structuur aanpassen.

Deze wijziging zorgt ervoor dat de gebruikte parameters bij het uitvoeren van het model in de ontwerper worden onthouden en opgeslagen in het model. Zodat u, elke keer als u het model in de ontwerper uitvoert, niet alle waarden voor de invoerparameters opnieuw moet instellen op die van de gewenste test.

Maakt iteratief modelontwerp ZOVEEL gemakkelijker!

Gesponsord door Alta Ehf

Bevat ook een gedeeltelijke overgang van het dialoogvenster van de ontwerper van Grafische modellen bouwen van Python naar C++, omdat C++ \>\> Python.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Opmerkingen in modellen van Processing
Dit stelt gebruikers in staat opmerkingen te maken die worden verbonden aan componenten van het model (invoeren, algoritmen of uitvoeren). Opmerkingen worden weergegeven gekoppeld aan de geassocieerde component, en kunnen vrijelijk worden verplaatst binnen het model.

![image104](images/entries/75851342-26799000-5e35-11ea-8895-a310f01b3823.gif)

Dit werd mogelijk gemaakt door Fisel + König

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Nieuw zelfstandig console-gereedschap voor het uitvoeren van algoritmen van Processing
Dit nieuwe gereedschap qgis_process stelt gebruikers in staat algoritmen van Processing uit te voeren (zowel ingebouwde als ook die worden verschaft door plug-ins) direct vanuit de console.

Uitvoeren:
- `qgis_process list` zal een volledig lijst van alle beschikbare algoritmen uitvoeren, gegroepeerd per provider.
- `qgis_process plugins` vermeldt beschikbare en geactiveerde plug-ins die de metadata optie hasProcessingProvider hebben (alleen die plug-ins worden door het gereedschap geladen)
- `qgis_process help algid` voert de Help uit en beschrijvingen voor de invoer van het gespecificeerde algoritme, bijv. `qgis_process help native:centroids`

`qgis_process run`: voert een algoritme uit. Parameters worden gespecificeerd door de syntaxis `--param=value`. Bijv.

    qgis_process run native:centroids --INPUT="my_shapefile.shp" --OUTPUT="centroids.kml"
    
of

    qgis_process run native:buffer --INPUT=/home/me/my.shp --DISTANCE=20 --OUTPUT=/home/me/buffered.shp
    
Bij het uitvoeren van een algoritme wordt een op tekst gebaseerde balk voor terugkoppeling weergegeven, en de bewerking kan worden geannuleerd met CTRL+C

Gesponsord door de Zweedse gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Nieuw type parameter voor waarden datetime (of date, of time)
Voegt een nieuw type parameter QgsProcessingParameterDateTime toe voor het afhandelen van waarden date/datetime/time.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Nieuwe algoritmes voor laten zien van waarschuwingen en uitzonderingen vanuit modellen toegevoegd
Deze algoritmen laten ofwel een aangepaste waarschuwing in het log van Processing zien OF werpt een uitzondering op die er voor zorgt dat het uitvoeren van het model wordt beëindigd.

Een optionele voorwaardelijke expressie kan worden gespecificeerd om te beheren of de waarschuwing/uitzondering wordt opgeworpen of niet, wat logica, zoals \"als de uitvoerlaag van een ander algoritme meer dan 10 objecten bevat, annuleer dan het uitvoeren van het model\", mogelijk maakt.

Gesponsord door Fisel + König

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Algoritme Cellen GeenGegevens vullen toegevoegd
In de nieuwe versie van QGIS introduceren we een nieuw algoritme voor Processing voor het vullen van cellen GeenGegevens in een raster gegevensset met een constante numerieke invoer.

Het algoritme scant een invoer raster gegevensset op cellen GeenGegevens en vult ze met het door de gebruiker gedefinieerde waarde voor vullen. Door dit te doen respecteert het algoritme het gegevenstype van het invoerraster, zodat bijv. getallen floating point zullen worden afgehandeld zoals toepasselijk is voor een raster integer. De resulterende gegevensset zal geen cellen GeenGegevens bevatten.

![image105](images/entries/6cbf249116a09b4d342729da1e09060b9f0ec52f.webp)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://api.github.com/users/root676)
### Mogelijkheid: Verscheidene reparaties voor Processing
- Voltooid werk aan ondersteuning voor parameters voor bereik in algoritmen van GRASS;
- Defecte algoritme r.series gerepareerd 
- Kleine reparaties aan r.rescale en r.rescale.eq
- Reparatie voor gereedschap Rasteriseren
- GRASS GIS testen opgeschoond

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Beperkingen voor veld \"template layer\" in de interface van het algoritme \"Refactor Fields\" weergeven
Wanneer u gegevens migreert is het belangrijk om u bewust te zijn van beperkingen op doel- (alias template) lagen.

Het algoritme \"Refactor Fields\" accentueert nu beperkingen, en laat u zelfs meer daarover te weten komen via Help-tips.

![image106](images/entries/75100644-6079a500-559e-11ea-91b6-f99fa05451de.webp)

Dit werd mogelijk gemaakt door [SwissTierras Colombia](https://swisstierrascolombia.com/)+

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: Nieuw algoritme voor converteren naar bogen
We hebben een nieuw algoritme toegevoegd voor het converteren van gesegmenteerde geometrieën naar gebogen geometrieën.

Het algoritme beschouwt opeenvolgende punten om een boog weer te geven als zij gelijkmatig zijn gespreid en binnen een tolerantie liggen.

![image107](images/entries/c747d86081f3862d9d4bbb2ab067103daceab724.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Opties voor toepassing en projecten
### Mogelijkheid: Variabelen voor bereik project \@layers, \@layer_ids toegevoegd
Variabelen voor bereik project \@layers, \@layer_ids toegevoegd die een lijst met lagen en laag-ID\'s bevatten voor alle lagen in het huidige project

Dit bootst de bestaande \@map_layers, \@map_layer_ids na, maar anders dan de varianten @map geven deze ALLE projectlagen terug. Niet slechts die welke zijn geassocieerd aan de kaartinstellingen voor de huidige context.

Gesponsord door SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Toevoegen van attributen in het dialoogvenster Nieuwe tekenlaag toestaan
Stelt de gebruiker in staat om attributen direct toe te voegen in het dialoogvenster Nieuwe tekenlaag. Wat het meer consistent maakt met andere dialoogvensters, zoals Nieuwe Shapefile/Geopackage. ![image108](images/entries/81394331-76711d80-912a-11ea-8b86-4f2789adff08.webp)

Het is nog steeds mogelijk om een tekenlaag te maken zonder attributen, door geen velden aan de lijst toe te voegen.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Maken van DBF-tabellen zonder geometrie in het dialoogvenster Nieuwe Shapefile toestaan
Staat het maken van \"gewone\" DBF-bestanden zonder geassocieerde geometrieën toe in het dialoogvenster Nieuwe Shapefile.

![image109](images/entries/81068877-be553200-8ee9-11ea-9a06-a4d30e773cf6.webp)

Het maken van DBF-tabellen kan in sommige gevallen nuttig zijn en om programma's van derde partijen te moeten gebruiken in plaats van het rechtstreeks in QGIS te doen is onhandig. Dit maakt ook het dialoogvenster Nieuwe Shapefile meer consistent met het dialoogvenster Nieuw GeoPackage, dat al toestaat dat tabellen \"zonder geometrie\" worden gemaakt.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Filteren lijst WM(T)S in dialoogvenster van bron toestaan
Voegt de mogelijkheid toe om te filteren tussen lijsten van WMS of WMTS in het dialoogvenster van de bron

WMS ![image110](images/entries/80964825-d0fc3800-8e11-11ea-9961-34edb623458c.webp)

WMTS ![image111](images/entries/80964191-b4abcb80-8e10-11ea-8b80-395dbb37b45c.webp)

Gesponsord door de QGIS Zwitserse gebruikersgroep

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Vectortegels toevoegen aan dialoogvenster Databronnen beheren en menu Lagen
Voegt een nieuwe tab toe aan het dialoogvenster Databronnen beheren, die de gebruiker in staat stelt verbindingen voor vectortegels te beheren/toe te voegen, inclusief importeren/exporteren. Voegt ook een overeenkomstig item in het menu Lagen in.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Importeren/exporteren voor verbindingen van ArcGIS Map en FeatureServer
Ontbrekende functionaliteit voor importeren/exporteren voor verbindingen naar ArcGIS MapServer en FeatureServer toegevoegd.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: XYZ-tegels toevoegen aan dialoogvenster Databronnen beheren en menu Lagen
Voegt een nieuwe tab toe aan het dialoogvenster Databronnen beheren, die de gebruiker in staat stelt verbindingen voor XYZ-tegels te beheren/toe te voegen. Voegt ook een overeenkomstig item in het menu Lagen in.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: SpatiaLite transactiegroep
Implementatie voor transacties voor de eigen provider SpatiaLite.

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Direct opslaan van uitvoeren naar meerdere indelingen voor databases toestaan (en andere leuke dingen)
Deze update stelt gebruikers in staat vector-uitvoeren van Processing direct op te slaan in indelingen voor meerdere databases.

Eerder konden uitvoeren alleen direct worden weggeschreven naar databases van PostgreSQL. Met deze wijziging is deze functionaliteit meer flexibel gemaakt en ondersteunt nu het direct wegschrijven naar elke provider van databases die de API voor verbindingen ondersteunt (momenteel PostgreSQL, Geopackage, SpatiaLite en SQL Server)

Uiteindelijk geeft dit de nieuwe mogelijkheid weer om uitvoer direct op te slaan naar databases van SQL Server of SpatiaLite (naast de eerdere opties voor GPKG+PostgreSQL die al bestaan)

(Zodra Oracle, DB2, \… de API voor de verbindingen hebben geïmplementeerd, zullen we ook daarvoor ondersteuning voor direct wegschrijven verkrijgen)

We doen dit via een leuke in-regelige versie van de nieuwe widget \"Nieuwe tabelnaam database\".

![image112](images/entries/77608752-dab89300-6f69-11ea-9c48-eefca7a4d199.gif)

Andere leuke dingen omvatten:
- U kunt nu bestanden of mappen slepen en neerzetten vanuit de bestandsbeheerder of de QGIS browser om parameters uit te voeren om deze bestanden gemakkelijker te kunnen overschrijven (of op te slaan in de map), wat overeenkomt met het mogelijke gedrag voor invoer
- U kunt in feite scripts schrijven die direct uitvoeren naar ELKE gegevensprovider van QGIS (inclusief Oracle en DB2)\… Het is slechts dat die niet worden weergegeven in de UI, omdat ze nog niet de API voor de verbindingen ondersteunen

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Aangewezen type parameter voor verbindingen van databases toegevoegd
Maakt selecteren vanuit de geregistreerde databaseverbindingen van een specifieke type database-provider mogelijk (de provider moet de API voor de verbindingen implementeren).

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: PG: weergeven vreemde tabellen
Geef vreemde tabellen weer in de browser en het dialoogvenster Databronnen selecteren.

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: PG raster geef toe te passen ingestelde filter weer
Dit zou de laatste wijziging moeten zijn voor de PostgreSQL raster gegevensprovider en geeft de ingestelde opties voor filteren weer:
- Filter kan worden ingesteld in het dialoogvenster Databronnen (net als voor vectorlagen)
- Filter kan worden ingesteld in het contextmenu voor de boom van de legenda (net als voor vectorlagen)
- De renderer, het bereik en de statistieken min/max worden ook bijgewerkt als het filter wijzigt
- Nieuwe testen voor het nieuwe gedrag

![image113](images/entries/75894983-49a43f80-5e35-11ea-95a8-a86276b39bbc.gif)

Dit werd mogelijk gemaakt door [ARPA Piemonte](http://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: PostgreSQL: sla objecten op in tabellen met gemaakte velden
Sta bijwerken/invoegen van objecten in tabellen van PostgreSQLmet gemaakte velden toe. GENERATED-kolommen is een mogelijkheid die werd geïntroduceerd in PostgreSQL 12, wat het mogelijk maakt dat kolomwaarden worden gemaakt vanuit andere kolommen uit dezelfde tabel; dit vervangt het maken van triggers om, bijvoorbeeld, automatisch een kolom met zwaartepunten of gebieden voor de polygonen in de hoofd geometriekolom te vullen en bij te houden.

Deze mogelijkheid werd ontwikkeld door [José de Paula Rodrigues N. Assis](https://api.github.com/users/espinafre)
### Mogelijkheid: Ondersteuning voor veldtypen Date en DateTime toegevoegd aan de providers SpatiaLite en Tekengescheiden tekst
De providers SpatiaLite en Tekengescheiden tekst ondersteunen nu de veldtypen Date en DateTime.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://api.github.com/users/nirvn)
## QGIS Server
### Mogelijkheid: Optie voor configuratie van QGIS_SERVER_IGNORE_BAD_LAYERS toegevoegd
Maakt het overschrijven van het standaardgedrag mogelijk in het geval van slechte lagen (om het gehele project ongeldig te maken.

Indien ingesteld op TRUE worden slechte lagen overgeslagen en het restant van het project komt beschikbaar.

Dit werd mogelijk gemaakt door [Geoinformatikbüro Dassau GmbH](https://www.gbd-consult.de/home.html)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it)
### Mogelijkheid: Server projectinstellingen, attribuut \'expanded\' toegevoegd
In aanvulling op de attributen \'visible\' en \'mutuallyExclusive\' voegt deze update \'expanded\' toe aan het antwoord GetProjectSettings van de server. De update maakt het voor een webcliënt mogelijk om te zien welke elementen van de laagboom zijn uitgeklapt / ingeklapt en om ze op dezelfde wijze te presenteren in de lagenlijst van de webkaart.

Deze mogelijkheid werd ontwikkeld door [mhugent](https://api.github.com/users/mhugent)
### Mogelijkheid: Toegevoegd DXF server export parameters NO_MTEXT en FORCE_2D
QGIS-server ondersteunt nu de nieuwe parameters `NO_MTEXT` en `FORCE_2D` om symbologie voor tekst en lijnen te beheren voor gegenereerde DXF-bestanden.

Voegt ontbrekende parameters toe aan verzoek GetDxf.

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Mogelijkheid: WMS-project validatie
De validatie voor QGIS Server is opnieuw bekeken. Dit gereedschap is nuttig als u een project van QGIS wilt publiceren met het protocol WMS.

Voor programmeurs is de validatie nu ook aan te roepen vanuit PyQGIS, dus plug-ins kunnen het nu ook gebruiken.

Dit werd mogelijk gemaakt door [3Liz](https://www.3liz.com)

Deze mogelijkheid werd ontwikkeld door [Etienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: Webp
> WebP is een moderne indeling voor afbeeldingen die superieure verliesloze en compressie met verlies verschaft voor afbeeldingen op het web. WebP maakt kleinere, rijkere afbeeldingen die het web sneller maakt.
> 
> WebP verliesloze afbeeldingen zijn 26% kleiner in grotte, vergeleken met PNG's. WebP afbeeldingen met verlies zijn 25-34% kleiner dan vergelijkbare afbeeldingen JPEG op de equivalente SSIM-kwaliteitsindex.

Bron: <https://developers.google.com/speed/webp>

Met Webp ondersteunt QGIS server nu een indeling die kleinere bestandsgrootten verschaft voor dezelfde kwaliteit en zelfs transparantie verschaft.

Dit werd mogelijk gemaakt door [OPENGIS.ch](https://www.opengis.ch)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Plug-ins
### Mogelijkheid: Plug-ins toestaan om aangepaste afhandeling voor \"Project openen\" te registreren
Deze stellen plug-ins in staat om het dialoogvenster "Project openen" uit te breiden door ondersteuning toe te voegen voor nieuwe bestandsfilters, die verschijnen in de keuzelijst voor indelingen naast het bestaande item \"QGIS projecten\".

Aangepaste afhandeling voor het openen van projecten krijgen dan de eerste kans bij het laden van projectbestanden.

Dit stelt plug-ins in staat de ondersteuning voor QGIS uit te breiden door geïntegreerde ondersteuning toe te voegen voor het openen van projecten van indelingen niet-QGS/QGZ, bijv. gebruikers toestaan documenten ArcGIS MXD of MapInfo WOR Workspaces te openen, direct vanuit het dialoogvenster Project openen.

Deze niet-eigen projecten zijn ook toegevoegd aan de lijst met recente projecten en Welkomstscherm, wat ze een echte eerste klas ervaring in QGIS geeft.

Gesponsord door SLYR

![image114](images/entries/78514331-1833e080-77f4-11ea-9c8d-a5e9ead7dc1a.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Gebruikers toestaan stabiele of experimentele plug-ins te installeren
Deze update verbeterd Plug-ins beheren en installeren door gebruikers toe te staan te kiezen tussen het installeren van de stabiele of de experimentele versie van een plug-in.

Dit maakt het mogelijk om pre-uitgaven van plug-ins in de opslagplaats voor power-users te testen, daarbij hen nog steeds gemakkelijk in staat te stellen terug te vallen op stabiele versies, zonder de globale optie *Ook de experimentele plug-ins tonen* te moeten deselecteren.

Deze wijziging maakt geen verschil voor gebruikers die de optie *Ook de experimentele plug-ins tonen* niet hebben geselecteerd.

![image115](images/entries/75906887-b1638600-5e47-11ea-98c6-06fb664ab177.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Olivier Dalang](https://api.github.com/users/olivierdalang)
## Programmeerbaarheid
### Mogelijkheid: Ondersteuning voor toevoegen van vast te zetten widgets als tabs: addTabifyDockWidget()
Vast te zetten widgets zijn fantastisch voor het weergeven van complexe interfaces die de functionaliteit van QGIS uitbreiden.

Nu hebben zowel ontwikkelaars van de bron als van plug-ins de optie om tabs te maken van hun vast te zetten widgets bovenop bestaande. Zij kunnen zelfs kiezen op welk vast te zetten widget zij hun eigen vast te zetten widget moet verschijnen.

![image116](images/entries/80051225-4b0cf280-84dd-11ea-9016-84a4303f230f.gif)

Dit werd mogelijk gemaakt door [SwissTierras Colombia](https://swisstierrascolombia.com/)+

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo](https://github.com/gacarrillor)
### Mogelijkheid: Wrappers van parameters voor uitvoer overzetten naar nieuwe API
Zet de wrappers van parameters voor uitvoer (doelen afvoeren, vector, raster, bestand en map) om naar de nieuwe C++ API voor dialoogvenster en Grafische modellen bouwen.

Dit opent een heel bereik van nieuwe mogelijkheden, inclusief:
- Modellen met statisch uitvoeren voor kind-algoritmen, bijv. altijd de uitvoer van een kind-algoritme opslaan naar een laag van GeoPackage of PostgreSQL
- Modellen met op expressies gebaseerde waarden voor uitvoer voor kind-algoritmen, bijv. maken van een automatische bestandsnaam, gebaseerd op de datum van vandaag en uitvoer opslaan naar dat bestand

![image117](images/entries/78028688-bbbf6400-73a2-11ea-9b7f-a7d81133d321.gif)

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Resterende parameters voor invoer overzetten naar nieuwe API
Deze update zet de parameters voor de invoer Rasterband  en Meerdere lagen om naar de nieuwe C++ API.

Voordelen omvatten:
- Op expressie gebaseerde band/laaglijsten in modellen
- In-regelige (niet-blokkerende) lijsten voor parameters voor meervoudige selectie (velden, banden, lagenlijsten, enums)
- Opnieuw schikken van invoer voor parameters voor meerder lagen in modellen, om specifieke laagvolgorde in te stellen

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Parameters Bron object, Raster, Vector en Laag met mazen overzetten naar nieuwe API
Het is nu mogelijk om op expressie gebaseerde laagbronnen in modellen van Processing te gebruiken.

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Laag met vectortegels - deel 1
Dit is het initiële werk voor ondersteuning van vectortegels-lagen.

![image118](images/entries/77539757-2d2e7c80-6ea2-11ea-9098-c6c0924f9d59.webp) (De rode lijnen zijn geen artefacten van het renderen; ze zijn met opzet getekend om randen van tegels weer te geven.)
### Overzicht
Tot op heden bevat dit alleen wijzigingen aan de bibliotheek qgis_core.

Belangrijke aanvullingen aan de publieke API:
- QgsVectorTileLayer - de belangrijkste klasse voor kaartlagen
- QgsVectorTileRenderer - basisklasse voor implementaties van klasse renderer voor vectortegels
- QgsVectorTileBasicRenderer - standaard implementatie renderer 

Nieuwe private klassen (kunnen worden toegevoegd aan de publieke API indien nodig):
- QgsVectorTileLoader - handelt ophalen van tegels van netwerk / MBTiles af
- QgsVectorTileMVTDecoder - handelt decoderen van ruwe tegelgegveens naar objecten af
- QgsVectorTileLayerRenderer - verzorgt het overall renderen (ophalen + decoderen + tekenen)
- QgsVectorTileUtils - verscheidene nuttige functies

Enkele nieuwe klassen die kunnen worden gedeeld door vector- en rastertegels:
- QgsTileXYZ - positie van een tegel in de matrixset (zoomniveau, kolom, rij)
- QgsTileRange - rechthoekige selectie in een tegelmatrix (begin-/eindkolom en -rij)
- QgsTileMatrix - beschrijving van een tegelmatrix (kaartbereik, zoomniveau, schaal, aantal rijen/kolommen)

(ook QgsTileMatrixSet zal later worden toegevoegd als we ook andere tegelmatrixsets dan alleen GoogleCRS84Quad ondersteunen)
### Testen
U kunt een vectortegellaag laden vanuit de console voor Python, bijv.:

    ds = QgsDataSourceUri() ds.setParam("type","xyz")
    ds.setParam("url", "https://api.maptiler.com/tiles/v3/{z}/{x}/{y}.pbf?key=YOUR_FREE_API_KEY") 
    uri = bytes(ds.encodedUri()).decode('utf-8')
    vtl = QgsVectorTileLayer(uri, "Vector Tiles Test")
    QgsProject.instance().addMapLayer(vtl)
    
Het is ook mogelijk vectortegels te laden vanuit een lokaal bestand MBTiles - gebruik \"mbtiles\" voor \"type\" en gebruik voor \"url\" een lokaal pad (bijv. \"/home/martin/x.mbtiles\").

Er is momenteel geen ondersteuning voor labelen.
### Dank u wel
Heel veel dank aan alle gulle gevers die hebben bijgedragen aan de crowdfunding en dit mogelijk hebben gemaakt - <https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors>

Dit werd mogelijk gemaakt door [QGIS gemeenschap](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Parameters voor bereik in Processing overzetten naar nieuwe API, vele andere verbetringen
Deze update zet uiteindelijk de parameter Bereik om naar de nieuwe C++ API, maar op weg daar naartoe wordt:
- De bestaande widget voor de GUI \"QgsExtentGroupBox\" opnieuw bijgewerkt om de kern daarvan te verplaatsen naar \"QgsExtentWidget\" (wat het mogelijk maakt het te gebruiken op plaatsen waar een groepsvak niet mogelijk is/er slecht uitziet). Het voegt ook een nieuwe modus \"verkleind\" voor de widget toe, omdat het standaard uiterlijk nogal veel plaats inneemt.
- De widget voor de nieuwe parameter gebruikt deze algemene QgsExtentWidget, zodat we alle duplicaatcode verwijderen die eerder werd gebruikt voor de oude wrapper van Python
- Maakt slepen en neerzetten mogelijk van projectlagen vanuit de lagenboom naar een QgsExtentWidget om het bereik automatisch in te stellen zodat het overeenkomt
- Maakt het mogelijk QgsExtentWidget optioneel null te laten zijn
- Maakt waarden QgsGeometry mogelijk die worden ingesteld voor waarden van de parameter Bereik. Dit is gedaan om te helpen bij het gebruiken van parameters bereik met de modus \"vooraf berekende waarde\" in modellen. U kunt nu alle functies voor expressies voor geometrie gebruiken om een geometrie te berekenen en het begrenzingsvak hiervan wordt gebruikt voor de waarde van de parameter in het kind-algoritme

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Interface en API voor universele gereedschappen voor ontwikkeling/debuggen
Voegt haken voor de interface toe om plug-ins (en C++) in staat te stellen gereedschappen voor \"ontwikkeling/debuggen\" te registreren

Deze gereedschappen verschijnen in een nieuw venster Gereedschap Ontwikkeling/Debuggen, en verschaft een geünificeerde afhandeling en plek voor deze gereedschappen in de UI.

De bedoeling hier is dat gespecialiseerde gereedschappen voor ontwikkeling/debuggen naar deze algemene interface zullen worden verplaatst, bijv.
- Netwerklogger
- Stijl Eerste Hulp inspectie van lokale variabelen voor Python
- Gereedschappen voor debuggen bij opstarten
- Gereedschappen voor debuggen bij Lagen laden en renderen \… ?

Hier is een voorbeelddemo die een gereedschap voor ontwikkeling van \"Python lokalen\" laat zien:

![image119](images/entries/77492080-55f74780-6e8b-11ea-9141-1b96c42c29eb.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Ondersteuning voor gegevenstype voor QgsProcessingParameterMapLayer
De definitie van geaccepteerde typen lagen voor `QgsProcessingParameterMapLayer` toestaan. Dit is nuttig als een algoritme kan werken met verschillende typen lagen (bijvoorbeeld punten en rasters) en het vermijdt het dupliceren van hetzelfde algoritme met verschillende invoer.

Dit is een verbetering in de API en is niet zichtbaar voor de grootste meerderheid van de gebruikers.

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Typen parameter voor Processing voor databaseschema en tabelnaam toegevoegd
Vervangt de eerdere ad hoc Python wrappers voor de widget PostGIS door juiste eerste klasse C++ toegewezen parameters voor schema's en tabellen, met wrappers die zijn gebouwd vanuit de bron-API voor verbindingen.

Refs NRCan Contract#3000707093

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Getfeatureinfo does not show relation reference items for QGIS Server | [#36549](https://github.com/qgis/QGIS/issues/36549) | Bleek een verzoek voor het toevoegen van mogelijkheid te zijn | N/B |
| OGR provider QgsOgrProvider::changeAttributeValues returns true on errors | [#36583](https://github.com/qgis/QGIS/issues/36583) | [PR #36620](https://github.com/qgis/QGIS/pull/36620) | N/B |
| GPKG transaction groups are stored with empty second pair of the key | [#36525](https://github.com/qgis/QGIS/issues/36525) | [PR #36660](https://github.com/qgis/QGIS/pull/36660) | [PR #37157](https://github.com/qgis/QGIS/pull/37157) |
| Symbology using relations does not propagate in QGIS Server | [#36614](https://github.com/qgis/QGIS/issues/36614) | Kan niet worden gereproduceerd | N/B |
| \"Loading PostGIS raster with QGIS 3.12.3 crashes\" | [#36689](https://github.com/qgis/QGIS/issues/36689) | [PR #36702](https://github.com/qgis/QGIS/pull/36702) | niet relevant |
| GetFeatureInfo Fid value is different between application/json and application/vnd.ogc.gml | [#36262](https://github.com/qgis/QGIS/issues/36262) | [PR #36733](https://github.com/qgis/QGIS/pull/36733) | [PR #37158](https://github.com/qgis/QGIS/pull/37158) |
| GPKG (and spatialite) DB-level unique constraints are not supported by OGR (and spatialite) provider | [#36468](https://github.com/qgis/QGIS/issues/36468) | [PR #36802](https://github.com/qgis/QGIS/pull/36802) | N/B |
| no value in the attribute form if value missing in the value map | [#32756](https://github.com/qgis/QGIS/issues/32756) | [PR #36804](https://github.com/qgis/QGIS/pull/36804) | N/B |
| DB Manager does not show anymore query results | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36823](https://github.com/qgis/QGIS/pull/36823) | N/B |
| DB Manager does not show anymore query results | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36831](https://github.com/qgis/QGIS/pull/36831) | N/B |
| GPKG browser drag&drop not working | niet gerapporteerd | [PR #36972](https://github.com/qgis/QGIS/pull/36972) | [PR #37159](https://github.com/qgis/QGIS/pull/37159) |
| it is not possible to save a project in the geopackage | [#36832](https://github.com/qgis/QGIS/issues/36832) | [PR #36980](https://github.com/qgis/QGIS/pull/36980) | N/B |
| It is possible to store text into a numeric field, while it shouldn\'t be, using the Date/Time edit widget | [#36715](https://github.com/qgis/QGIS/issues/36715) | [#36715](https://github.com/qgis/QGIS/issues/36715) | N/B |
| Feature creation very slow when using joins | [#36167](https://github.com/qgis/QGIS/issues/36167) | [PR #36866](https://github.com/qgis/QGIS/pull/36866), [PR #36963](https://github.com/qgis/QGIS/pull/36963) | N/B |
| QGIS Server: WFS Request does not use SrsName on the geometry | [#36398](https://github.com/qgis/QGIS/issues/36398) | [PR #36926](https://github.com/qgis/QGIS/pull/36926), [PR #37071](https://github.com/qgis/QGIS/pull/37071) | niet kritisch |
| Unable to delete a stored geopackage connection from browser | [#36930](https://github.com/qgis/QGIS/issues/36930) | [PR #36937](https://github.com/qgis/QGIS/pull/36937) | [PR #37166](https://github.com/qgis/QGIS/pull/37166) |
| Constraints: unique constraint not correctly evaluated when 0 | [#36962](https://github.com/qgis/QGIS/issues/36962) | [PR #36967](https://github.com/qgis/QGIS/pull/36967) | N/B |
| PyQgis: OriginJoin fields arte not present into QgsLayerVector QgsFields container for GeoPackage layers | [#36977](https://github.com/qgis/QGIS/issues/36977) | Kan niet worden gereproduceerd | N/B |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | Kan niet worden gereproduceerd/In behandeling | N/B |
| Removal of unused \'allowMethod\' from qgisservice/qgisserverapi | [#36163](https://github.com/qgis/QGIS/issues/36163) | [PR #36997](https://github.com/qgis/QGIS/pull/36997) | N/B |
| Omogenize window title | [#35761](https://github.com/qgis/QGIS/issues/35761) | [PR #36998](https://github.com/qgis/QGIS/pull/36998) | N/B |
| Labeling: data-defined alignment grey-out activation issue | [#37003](https://github.com/qgis/QGIS/issues/37003) | [PR #37006](https://github.com/qgis/QGIS/pull/37006) | [PR #37167](https://github.com/qgis/QGIS/pull/37167) |
| QGIS reports \"no layers\" in GeoPackage when geopackage directory is write protected | [#36574](https://github.com/qgis/QGIS/issues/36574) | [PR #37018](https://github.com/qgis/QGIS/pull/37018) | niet kritisch (alleen UX) |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | won\'t fix | N/B |
| Postgis Timestamps from query in DB Manager displayed as \`PyQT5.QTCore.QDateTime(2020, 3, 17 | [#35140](https://github.com/qgis/QGIS/issues/35140) | [PR #37042](https://github.com/qgis/QGIS/pull/37042) | N/B |
| Wrong image preview and image preview size in form | [#33682](https://github.com/qgis/QGIS/issues/33682) | [PR #37093](https://github.com/qgis/QGIS/pull/37093) | [PR #37168](https://github.com/qgis/QGIS/pull/37168) |
| can\'t change value in vertex editor if \"locale\" settings use commas as decimal separator | [#29682](https://github.com/qgis/QGIS/issues/29682) | [PR #37135](https://github.com/qgis/QGIS/pull/37135) | [PR #37169](https://github.com/qgis/QGIS/pull/37169) |
| Identifying a WMS layer with format \"feature\" crashes QGIS | [#29443](https://github.com/qgis/QGIS/issues/29443) | [PR #37171](https://github.com/qgis/QGIS/pull/37171) | [PR #37210](https://github.com/qgis/QGIS/pull/37210) |
| Attempting to create a new feature in Spatialite with transaction group and NOT NULL constraint fails | [#37236](https://github.com/qgis/QGIS/issues/37236) | won\'t fix | N/B |
| Using \"Add feature\" to create feature and child feature with transaction group causes foreign key error | [#37222](https://github.com/qgis/QGIS/issues/37222) | [PR #37249](https://github.com/qgis/QGIS/pull/37249) | niet kritisch |
| Vectorlayer from spatialite missing features and inconsistent feature count | [#29264](https://github.com/qgis/QGIS/issues/29264) | [PR #37277](https://github.com/qgis/QGIS/pull/37277) | NOG TE DOEN |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Mogelijkheid: Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix error when vector layer has Z | [#32016](https://github.com/qgis/QGIS/issues/32016) | [PR #36553](https://github.com/qgis/QGIS/pull/36553) | [PR #36595](https://github.com/qgis/QGIS/pull/36595) |
| Fix rectangle from 3 points | [#35043](https://github.com/qgis/QGIS/issues/35043), [#35671](https://github.com/qgis/QGIS/issues/35671) | [PR #36523](https://github.com/qgis/QGIS/pull/36523) | [PR #36560](https://github.com/qgis/QGIS/pull/36560) |
| Allow to search qmlplugindump in different paths | N/B | [PR #36513](https://github.com/qgis/QGIS/pull/36513) | N/B |
| Fix the absence of words in the advanced configuration widget | [PR #35643](https://github.com/qgis/QGIS/pull/35643)#issuecomment-610215386 | [PR #36511](https://github.com/qgis/QGIS/pull/36511) | N/B |
| Fix interpolation on split geometry | [PR #36514](https://github.com/qgis/QGIS/pull/36514) | [#33489](https://github.com/qgis/QGIS/issues/33489) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Wrong interpretation of EPSG code from a PRJ file in QGIS-dev (proj v7.1.0) | [#36111](https://github.com/qgis/QGIS/issues/36111) | [PROJ PR 2240](https://github.com/OSGeo/PROJ/pull/2240) | N/B: probleem van PROJ |
| QGIS crashes when adding file to geopackage -\> layer -\> field(BLOB) | [#30210](https://github.com/qgis/QGIS/issues/30210) | [PR #36722](https://github.com/qgis/QGIS/pull/36722) | [PR #36737](https://github.com/qgis/QGIS/pull/36737) |
| Bad error message on WFS connection fail | [#29866](https://github.com/qgis/QGIS/issues/29866) | [PR #36717](https://github.com/qgis/QGIS/pull/36717) | [PR #36735](https://github.com/qgis/QGIS/pull/36735) |
| QGIS crashes during map re-rendering after CRS switch | [#29672](https://github.com/qgis/QGIS/issues/29672) | Kan niet worden gereproduceerd | N/B |
| QGIS crashes when \"open directory\" is selected from the recent projects contextual menu | [#31630](https://github.com/qgis/QGIS/issues/31630) | [PR #36738](https://github.com/qgis/QGIS/pull/36738) | [PR #36755](https://github.com/qgis/QGIS/pull/36755) |
| Problem reprojecting rasters in 54019 and 54042 CRSs | [#35512](https://github.com/qgis/QGIS/issues/35512) | [PROJ PR 2243](https://github.com/OSGeo/PROJ/pull/2243) | N/B: probleem van PROJ |
| WFS Provider WARNING - Cannot create temporary SpatiaLite cache when using flatpak install | [#36545](https://github.com/qgis/QGIS/issues/36545) | [PR #36745](https://github.com/qgis/QGIS/pull/36745) | N/B |
| WFS Transaction operation using GetCapabilities URI | [#34307](https://github.com/qgis/QGIS/issues/34307) | [PR #36746](https://github.com/qgis/QGIS/pull/36746) | N/B |
| QGis 3.10.2 crashes when displaying two PostGIS raster layers | [#34456](https://github.com/qgis/QGIS/issues/34456) | - | N/B |
| QGIS 3.4.10 crashes - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | al gerepareerd in master | [PR #36751](https://github.com/qgis/QGIS/pull/36751) |
| WMS provider expects SERVICE=WMTS keyword in uppercase to detect WMTS | [#36659](https://github.com/qgis/QGIS/issues/36659) | [PR #36752](https://github.com/qgis/QGIS/pull/36752) | [PR #36766](https://github.com/qgis/QGIS/pull/36766) |
| WCS DescribeCoverage response origin always empty | [#36504](https://github.com/qgis/QGIS/issues/36504) | [PR #36754](https://github.com/qgis/QGIS/pull/36754) | [PR #36781](https://github.com/qgis/QGIS/pull/36781) |
| Extent wrong if layer contains point at 0,0 | [#33823](https://github.com/qgis/QGIS/issues/33823) | Geen probleem van QGIS. Gerepareerd in GDAL 3.1 | N/B |
| Projection not recognised from Mapinfo converstion | [#34471](https://github.com/qgis/QGIS/issues/34471) | [PR #36758](https://github.com/qgis/QGIS/pull/36758) | [PR #36783](https://github.com/qgis/QGIS/pull/36783) |
| QGIS crashes/freezes when adding a large CSV file as delimited text layer | [#36392](https://github.com/qgis/QGIS/issues/36392) | [PR #36778](https://github.com/qgis/QGIS/pull/36778) | [PR #36810](https://github.com/qgis/QGIS/pull/36810) |
| QGIS 3.12 unknown CRS or Select Transformation | [#36837](https://github.com/qgis/QGIS/issues/36837) | [GDAL Commit 68133b8](https://github.com/OSGeo/gdal/commit/68133b8b6f724a581a5dcb19fbdcd657ddbd6c4c) | [GDAL Commit 6ae7f60](https://github.com/OSGeo/gdal/commit/6ae7f60a5914a2f16b8b1a94758f10e6621e4aca) |
| BIGTIFF error is not obvious in processing log | [#36867](https://github.com/qgis/QGIS/issues/36867) | [GDAL Commit cfc8e61](https://github.com/OSGeo/gdal/commit/cfc8e613ad86dd4b00604dd64df239916ccda135) | [GDAL Commit fb88e3c](https://github.com/OSGeo/gdal/commit/fb88e3ca5c8905fbcaab79e96a2bfc1c36f72d08) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix segfault when adding a layer | [Mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2020-June/061421.html) | [PR #36910](https://github.com/qgis/QGIS/pull/36910) | N/B |
| Fix signal connection | Niet gerapporteerd probleem | [PR #35836](https://github.com/qgis/QGIS/pull/35836) | N/B |
| Update the API to export a legend in JSON | Niet gerapporteerd probleem binding | [PR #36370](https://github.com/qgis/QGIS/pull/36370) | N/B |
| Core dump if vector tile layer (file) becomes unavailable | [#36821](https://github.com/qgis/QGIS/issues/36821) | Kan niet worden gereproduceerd | N/B |
| Crash on project open when mapcanvas extents = nan | [#35899](https://github.com/qgis/QGIS/issues/35899) | Kan niet worden gereproduceerd | N/B |
| Using some functions in raster calulator crashes QGIS | [#35583](https://github.com/qgis/QGIS/issues/35583) | [PR #37273](https://github.com/qgis/QGIS/pull/37273) | N/B |
| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Al gerepareerd. Gesloten. | N/B |
| Fix compilation with GCC 10, Qt/PyQt 5.15.0 and SIP 4.19.23 | [#37072](https://github.com/qgis/QGIS/issues/37072) | [PR #37116](https://github.com/qgis/QGIS/pull/37116) | [PR #37250](https://github.com/qgis/QGIS/pull/37250) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Paul Blottiere](https://hytech-imaging.fr/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Reproducible crash using QgsMapCanvas.items() with Oracle layers | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #36240](https://github.com/qgis/QGIS/pull/36240) | [PR #36246](https://github.com/qgis/QGIS/pull/36246) |
| Line breaks are ignored in the user expression help panel | [#36191](https://github.com/qgis/QGIS/issues/36191) | [PR #36249](https://github.com/qgis/QGIS/pull/36249) | [PR #36387](https://github.com/qgis/QGIS/pull/36387) |
| \"Edit user expression\" does not allow to rename the user expression | [#36192](https://github.com/qgis/QGIS/issues/36192) | [PR #36349](https://github.com/qgis/QGIS/pull/36349) | N/B |
| Cannot change labels of raster symbology classes | [#36172](https://github.com/qgis/QGIS/issues/36172) | [PR #36376](https://github.com/qgis/QGIS/pull/36376) | [PR #36533](https://github.com/qgis/QGIS/pull/36533) |
| Crash when layer not available | [#33300](https://github.com/qgis/QGIS/issues/33300) | Kan niet worden gereproduceerd | N/B |
| Select by expression returns erroneous results with integer field division for shapefiles | [#35449](https://github.com/qgis/QGIS/issues/35449) | [PR #2531](https://github.com/OSGeo/gdal/pull/2531) | N/B |
| Using concat(field1, field2) concatenates 0 instead of empty string (\'\') if any of the fields is NULL | [#36112](https://github.com/qgis/QGIS/issues/36112) | [PR #36521](https://github.com/qgis/QGIS/pull/36521) | [PR #36529](https://github.com/qgis/QGIS/pull/36529) |
| Stuck at Recent Project window when opening blank file in 3.10.3 | [#34809](https://github.com/qgis/QGIS/issues/34809) | Kan niet worden gereproduceerd | N/B |
| QGIS crashes on getting items of mapCanvas scene if features are identified | [#34457](https://github.com/qgis/QGIS/issues/34457) | [PR #36439](https://github.com/qgis/QGIS/pull/36439) | [PR #36450](https://github.com/qgis/QGIS/pull/36450) |
| sorting on a column that has a value relation is inconsistent | [#36114](https://github.com/qgis/QGIS/issues/36114) | [PR #36776](https://github.com/qgis/QGIS/pull/36776) | [PR #36887](https://github.com/qgis/QGIS/pull/36887) |
| Missing points (depending on canvas scale) in virtual layer based on sqlite file | [#36054](https://github.com/qgis/QGIS/issues/36054) | [PR #36792](https://github.com/qgis/QGIS/pull/36792) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| Project is modified as soon as you move cursor on canvas | [#36796](https://github.com/qgis/QGIS/issues/36796) | [PR #36797](https://github.com/qgis/QGIS/pull/36797) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| Set filter applied to wrong \"version\" of table when multiple geometry types | [#34982](https://github.com/qgis/QGIS/issues/34982) | [PR #36801](https://github.com/qgis/QGIS/pull/36801)[PR #36718](https://github.com/qgis/QGIS/pull/36718) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Bertrand Rix
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Vertex tool override global snapping parameters | [#36229](https://github.com/qgis/QGIS/issues/36229) | [PR #36231](https://github.com/qgis/QGIS/pull/36231) | N/B |
| QGIS crashes with QgsGeometry method on empty collection | [#36142](https://github.com/qgis/QGIS/issues/36142) | [PR #36351](https://github.com/qgis/QGIS/pull/36351) | N/B |
| Selective masking: phantom lines on dark background | [#34650](https://github.com/qgis/QGIS/issues/34650) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/B |
| Selective masking: issue with mask opacity | [#34947](https://github.com/qgis/QGIS/issues/34947) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Bertrand Rix](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Sebastien Peillet
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[Oracle\]Error on save geometries because wrong default values #34482 | [#34482](https://github.com/qgis/QGIS/issues/34482) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/B |
| Invalid query for default value of date column of an oracle layer | [#32401](https://github.com/qgis/QGIS/issues/32401) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/B |
| Fields missing in Visibility by expression for a group in drag/drop form | [#35196](https://github.com/qgis/QGIS/issues/35196) | [PR #36824](https://github.com/qgis/QGIS/pull/36824) | N/B |
| Project custom scales are displayed with scientific notation | [#36859](https://github.com/qgis/QGIS/issues/36859) | [PR #36860](https://github.com/qgis/QGIS/pull/36860) | N/B |
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) | N/B |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | [PR #37136](https://github.com/qgis/QGIS/pull/37136) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Copy of truncated variable copies truncated text, not original | [#30641](https://github.com/qgis/QGIS/issues/30641) | [PR #36554](https://github.com/qgis/QGIS/pull/36554) | [PR #36576](https://github.com/qgis/QGIS/pull/36576) |
| Turning Multi edit mode off does not go back to table view | [#25099](https://github.com/qgis/QGIS/issues/25099) | [PR #36541](https://github.com/qgis/QGIS/pull/36541) | [PR #36630](https://github.com/qgis/QGIS/pull/36630) |
| GRASS processing: missing parameter name | [#36520](https://github.com/qgis/QGIS/issues/36520) | [PR #36644](https://github.com/qgis/QGIS/pull/36644) | [PR #36690](https://github.com/qgis/QGIS/pull/36690) |
| Fix redirection of the stdout results to temporary files in GRASS Processing algorithms | niet gerapporteerd | [PR #36618](https://github.com/qgis/QGIS/pull/36618) | [PR #36684](https://github.com/qgis/QGIS/pull/36684) |
| Fix GRASS r.tileset algorithm | niet gerapporteerd | [PR #36645](https://github.com/qgis/QGIS/pull/36645) | [PR #36695](https://github.com/qgis/QGIS/pull/36695) |
| QgsRasterTerrainAnalysisPlugin: check QgsRelief::processRaster() returned value | [#17452](https://github.com/qgis/QGIS/issues/17452) | [PR #36731](https://github.com/qgis/QGIS/pull/36731) | [PR #36740](https://github.com/qgis/QGIS/pull/36740) |
| Histogram for graduated style in layer properties disappears when the layer properties window is too small | [#25197](https://github.com/qgis/QGIS/issues/25197) | [PR #36732](https://github.com/qgis/QGIS/pull/36732) | [PR #36749](https://github.com/qgis/QGIS/pull/36749) |
| Exporting image with atlas option \"Save World file\" lead to incorrect world file naming (text after dot is missing) | [#34523](https://github.com/qgis/QGIS/issues/34523) | [PR #36742](https://github.com/qgis/QGIS/pull/36742) | [PR #36748](https://github.com/qgis/QGIS/pull/36748) |
| \"Reloading QGIS\" from the crash report dialog fails to reopen the project | [#25532](https://github.com/qgis/QGIS/issues/25532) | [PR #36736](https://github.com/qgis/QGIS/pull/36736) | [PR #36750](https://github.com/qgis/QGIS/pull/36750) |
| Exporting raster style to SLD only works when output file has .sld suffix | [#35944](https://github.com/qgis/QGIS/issues/35944) | [PR #36774](https://github.com/qgis/QGIS/pull/36774) | [PR #36795](https://github.com/qgis/QGIS/pull/36795) |
| \[Style Manager\] Missing Favorites category in the \"select by group\" dialog from \"Export symbols\" | [#27315](https://github.com/qgis/QGIS/issues/27315) | [PR #36793](https://github.com/qgis/QGIS/pull/36793) | niet kritisch |
| TIN Interpolation - output raster format and size issues | [#31970](https://github.com/qgis/QGIS/issues/31970) | [PR #36822](https://github.com/qgis/QGIS/pull/36822) | [PR #36844](https://github.com/qgis/QGIS/pull/36844) |
| Layer panel: \"Edit Symbol\" does nothing if no symbol defined for a rule (in rule-based rendering) | [#23048](https://github.com/qgis/QGIS/issues/23048) | [PR #36954](https://github.com/qgis/QGIS/pull/36954) | niet kritisch |
| Attributes shift in the Service area algorithm results | niet gerapporteerd | [PR #37074](https://github.com/qgis/QGIS/pull/37074), [PR #37097](https://github.com/qgis/QGIS/pull/37097) | N/B |
| Processing testing framework does not apply rounding to values casted to numbers | niet gerapporteerd | [PR #37234](https://github.com/qgis/QGIS/pull/37234) | N/B |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix leak in mesh 3d renderer | niet gerapporteerd | [Commit 4b5a63d](https://github.com/qgis/QGIS/commit/4b5a63d11b7ea5baf6931c8abf86e132c706c1be) | N/B |
| Fix hang when rendering symbol previews using Meters in Map Unit sizes | [#28690](https://github.com/qgis/QGIS/issues/28690) | [Commit 7c6286f](https://github.com/qgis/QGIS/commit/7c6286f8dfb7cc24e5b06c9ab950d9dd55fac517) | No \-- too intrusive |
| Fix font in CSS code editor | niet gerapporteerd | [Commit 63cb42c](https://github.com/qgis/QGIS/commit/63cb42c298ef5ab732274bce205e49171b797ae4) | niet kritisch |
| Fix rendering of geometry generator expressions which return geometry collection results | [#35356](https://github.com/qgis/QGIS/issues/35356) | [Commit be281c49](https://github.com/qgis/QGIS/commit/be281c49b7932a1d0d0e3cb4dce7af17f5b201a9) | No \-- too intrusive |
| \[processing\] Correctly expose date time inputs (and a bunch of others) as inputs for in-model expressions | [#37219](https://github.com/qgis/QGIS/issues/37219) | [Commit 281356a](https://github.com/qgis/QGIS/commit/281356aa4e951db5cd2782b53a7261c7343c4ca7) | N/B |
| Fix all Qt 5.14 deprecation warnings | niet gerapporteerd | [Commit 3717adc](https://github.com/qgis/QGIS/commit/3717adcef6315f4b9a0089bfc2393cede937b644) | No \-- too intrusive |
| \[symbology\] When rendering a multipart geometry, ensure that geometry generator symbol is only rendered once, instead of once per part | [#23730](https://github.com/qgis/QGIS/issues/23730) | [Commit d98fe9f](https://github.com/qgis/QGIS/commit/d98fe9f989f3b0677282acdf2ba99f4aa4fa08cc) | No \-- too intrusive |
| \[layout\] Make \"show feature count\" button apply to all selected indexes | [#37194](https://github.com/qgis/QGIS/issues/37194) | [Commit 671cebc](https://github.com/qgis/QGIS/commit/671cebcf817e2b6fc17ce0307edf7fa377b665d3) | No \-- too intrusive |
| Fix for container \"show as group box\" setting is lost when closing layer properties dialog | [#37205](https://github.com/qgis/QGIS/issues/37205) | [Commit 803f507](https://github.com/qgis/QGIS/commit/803f507d45f99534dbc03ab5300e6137da36cd59) | N/B |
| Use even more forceful language to dissuade users from creating custom projections using Proj strings | [#37204](https://github.com/qgis/QGIS/issues/37204) | [Commit 7ec4968](https://github.com/qgis/QGIS/commit/7ec4968aa9dcb2107b00c1caaeb6ae575498bc3c) | No \-- string change |
| Use \"markers\" terminology consistently in centroid fill widget | [#37106](https://github.com/qgis/QGIS/issues/37106) | [Commit 2596b6b](https://github.com/qgis/QGIS/commit/2596b6be858a17533d1e16fca8ff8afc5d222564) | No \-- string change |
| Fixes to numbered list handling in dox/PyQGIS API | niet gerapporteerd | [Commit 74400c7](https://github.com/qgis/QGIS/commit/74400c7ff88d563dad74dad41860f9b603214973) | Nee |
| Fix cross references in PyQGIS docs | niet gerapporteerd | [Commit 81a9db9](https://github.com/qgis/QGIS/commit/81a9db9f57706cba9b11e4372dd1bf50fcd7bc6a) | Nee |
| \[layouts\] Fix attribute table sort order combined with feature filter results in empty tables | [#36341](https://github.com/qgis/QGIS/issues/36341) | [Commit 24897ab](https://github.com/qgis/QGIS/commit/24897ab86a7f11be196d8d705fa3307b05e0e53d) | N/B |
| Fix callout rendering to rotated labels | [#36681](https://github.com/qgis/QGIS/issues/36681) | [Commit 2bb4aad](https://github.com/qgis/QGIS/commit/2bb4aad8c9b7238bd6ff6dc9a90a28c8625e859e) | N/B |
| Fix grass output handling in Processing models | [#36379](https://github.com/qgis/QGIS/issues/36379) | [Commit ef19911](https://github.com/qgis/QGIS/commit/ef19911f1132dc5720a4068f059a0322d7511e2b) |  |
| Fix vector datasets incorrectly simplify to rectangles in some CRS views | [#36898](https://github.com/qgis/QGIS/issues/36898) | [Commit 47fba10](https://github.com/qgis/QGIS/commit/47fba106dd9d057e6691dcca392efacbe31ad9ff) | No \-- too intrusive |
| Fix list item formatting in PyQGIS docs | niet gerapporteerd | [Commit 84ec481](https://github.com/qgis/QGIS/commit/84ec481aa8f3d3bb487272122414c765e77a2ea2) | N/B |
| \[processing\] Fix manual entry of extent values in widget | [#36787](https://github.com/qgis/QGIS/issues/36787) | [Commit ccc34c7](https://github.com/qgis/QGIS/commit/ccc34c76e714e5f6f87d2a329ca048896eb4c87f) | N/B |
| \[decorations\] Use a proper ellipsoidal length calculation when calculating the size of the scalebar decoration | [#28407](https://github.com/qgis/QGIS/issues/28407) | [Commit af19cea](https://github.com/qgis/QGIS/commit/af19cea5acc90a6cc19d116dd35739059d0c5f83) | [PR 36718 Commit a91309d](https://github.com/qgis/QGIS/pull/36718/commits/a91309ddbc0a430dc3bbcf48070bc565296ac551) |
| Fix collecting Triangle geometry types after tesselation | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit df46fba](https://github.com/qgis/QGIS/commit/df46fba33823415b8310c986795f8c51550a0fa6) | No \-- too intrusive |
| Fix writing triangle geometry type via QgsVectorFileWriter fails | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit e0c03f9](https://github.com/qgis/QGIS/commit/e0c03f9f0848490f358876ae5be6973961700bc9) | No \-- too intrusive |
| Fix degradation in Tesselation results | [#37077](https://github.com/qgis/QGIS/issues/37077) | [Commit 61e7a5f](https://github.com/qgis/QGIS/commit/61e7a5fc90154bd4d35fea7d6cbd413ce61fa02e) | N/B |
| Fix layer subset string is ignored when OGR refuses to accept a compiled feature request expression | [#37073](https://github.com/qgis/QGIS/issues/37073) | [Commit b5b4221](https://github.com/qgis/QGIS/commit/b5b42218af5cbfca82f3b0a4d5a521e3d330f550) | [PR 36718 Commit f486cf6](https://github.com/qgis/QGIS/pull/36718/commits/f486cf6e6dadb2d0690f167620c90f4efddb3c4a) |
| \[legends\] Fix corrupted data defined legend rendering in layout designer | [#36765](https://github.com/qgis/QGIS/issues/36765) | [Commit 8d00ae8](https://github.com/qgis/QGIS/commit/8d00ae8638a09cb9a4c9ecd5d1fec3b352050cdd) | No \-- too intrusive |
| Avoid some QGIS startup warnings | niet gerapporteerd | [Commit 013f682](https://github.com/qgis/QGIS/commit/013f682bd3c6addd163a78d3776c578ae37377c6) | N/B |
| Place 3d tab in vector properties at the correct position | [#35010](https://github.com/qgis/QGIS/issues/35010) | [Commit ce9f5194](https://github.com/qgis/QGIS/commit/ce9f519468d46bb6fe6dd0bc68efd7d58129be68) | N/B |
| Fix 3d tab is not activated when reopening vector layer properties | [#35011](https://github.com/qgis/QGIS/issues/35011) | [Commit 3c0ecbf](https://github.com/qgis/QGIS/commit/3c0ecbfd79e1924cd01143324cdc26fe4a68f748) | N/B |
| \[labeling\] Fix incorrect label placement after moving an \'unplaced\' label | niet gerapporteerd | [Commit cbfb7f4](https://github.com/qgis/QGIS/commit/cbfb7f4ce25e10aab5f7b8cee147afb801042704) | [PR 36718 Commit 9189dec](https://github.com/qgis/QGIS/pull/36718/commits/9189dec7633b2eb6a1075bb35c2f90f6b90ba63a) |
| Don\'t block creation of new geopackages in vector save as dialog | niet gerapporteerd | [Commit 8ccd127](https://github.com/qgis/QGIS/commit/8ccd127f4d8bf66fb04b6484147ed116acf66d91) | N/B |
| \[browser\] Refine refreshConnections method to avoid triggering a full refresh of ALL browser content | [#37007](https://github.com/qgis/QGIS/issues/37007) | [Commit a9d6b04](https://github.com/qgis/QGIS/commit/a9d6b04f776b80acd1a97f48c7ed10e3599618b6) | No \-- too intrusive |
| \[3d\] When showing edges, data defined polygon height was not accounted for | niet gerapporteerd | [Commit e516231](https://github.com/qgis/QGIS/commit/e516231bb2854405ea78a0cec40ad96295e9f8c6) | N/B |
| Fixes for \"Show all\" labeling mode | niet gerapporteerd | [Commit 2b91bd0](https://github.com/qgis/QGIS/commit/2b91bd0cafff66f14ceb49b104bf2f2cc6ae714d) | N/B |
| \[3d\] Fix reprojection of features shows no features | [#34824](https://github.com/qgis/QGIS/issues/34824) | [Commit 62bd026](https://github.com/qgis/QGIS/commit/62bd0267439a65f94a5cd9cb886bbb4e4780cdf0) | N/B |
| \[processing\] Add metadata setting for file destination parameters to avoid file overwrite confirmation prompt | [#37011](https://github.com/qgis/QGIS/issues/37011) | [Commit e81af2c](https://github.com/qgis/QGIS/commit/e81af2c9e10dc2a2e220c815cb9e531f7dba838d) | N/B |
| Avoid incorrectly antialiasing rendering of certain objects (such as map labels) when not wanted | [#36964](https://github.com/qgis/QGIS/issues/36964) | [Commit bab83844](https://github.com/qgis/QGIS/commit/bab838444cb55fc479d2f3dfa3b19d8ce80e73af) | No \-- too intrusive |
| Ensure that fields required by marker symbol backgrounds for labels are fetched when rendering | [#36944](https://github.com/qgis/QGIS/issues/36944) | [Commit 8fb8e45](https://github.com/qgis/QGIS/commit/8fb8e45d516611f09bf28e3832c3c6214f16c4a2) | No \-- too intrusive |
| \"Fix \"\"zoom\"\" and \"\"flash\"\" features buttons have no effect when opening filter mode in attribute form\" | [#34506](https://github.com/qgis/QGIS/issues/34506) | [Commit 6b2795](https://github.com/qgis/QGIS/commit/6b27958948db2c88ae72b0b9ff99fc8aa8522bf2) | N/B |
| Avoid corrupted project thumbnail images in some circumstances | niet gerapporteerd | [Commit f404e6e](https://github.com/qgis/QGIS/commit/f404e6e162df954ffb200d550b6c32375b7270c1) | N/B |
| Auto focus search box when opening \"add layer to legend\" dialog | [#36905](https://github.com/qgis/QGIS/issues/36905) | [Commit 019e494](https://github.com/qgis/QGIS/commit/019e494f1d61851ea192900a2cc9cce460d1ea73) | niet kritisch |
| \[processing\] Set correct output layer type for Point to Layer algorithm | [#36941](https://github.com/qgis/QGIS/issues/36941) | [Commit 7ee85cd](https://github.com/qgis/QGIS/commit/7ee85cd93cb5e0b623feaad2ef1ce9ea8f654bac) | N/B |
| \"Limit scope of Ctrl+C shortcut for copy features to canvas and for python console to console widget\" | [#27035](https://github.com/qgis/QGIS/issues/27035) (many others too) | [Commit 873716c](https://github.com/qgis/QGIS/commit/873716c6fa17298868060a6517205ad7bea78a72) | No \-- too intrusive |
| Remember layout designer window positions | [#36907](https://github.com/qgis/QGIS/issues/36907) | [Commit 97d31d0](https://github.com/qgis/QGIS/commit/97d31d025fe2264afadcf6afcb3eb6ebcfe9e91d) | niet kritisch |
| Fix crash when zooming in too far to labels | [#36346](https://github.com/qgis/QGIS/issues/36346) | [Commit 3aa5e56](https://github.com/qgis/QGIS/commit/3aa5e56d3c3dbb61f2a28c4874593aa401957ed3) | [Commit a22635b](https://github.com/qgis/QGIS/commit/a22635bb64ae6d2a46715bd1208463e22b6080ae) |
| \[processing\] Allow parent layer to be specified for field mapping inputs in models | [#26493](https://github.com/qgis/QGIS/issues/26493) | [Commit b8d4a39](https://github.com/qgis/QGIS/commit/b8d4a39b58465f93f45ed886e77411c194f44132) | No \-- too intrusive |
| Fix placement of message bar \'clear all\' menu arrow on hidpi screens | niet gerapporteerd | [Commit 8a9975b](https://github.com/qgis/QGIS/commit/8a9975b4ff6b7a8a79bef05230db28754500fa40) | niet kritisch |
| Always refresh plugin repositories when manually triggered by user | [#34351](https://github.com/qgis/QGIS/issues/34351) | [Commit 98603b7](https://github.com/qgis/QGIS/commit/98603b78660e05334c7b34ea3722533164f9553b) | [PR 36718 Commit 0fcf6dc](https://github.com/qgis/QGIS/pull/36718/commits/0fcf6dc08289fb549c9bace24a70ed4a50bdd959) |
| \[3d\] Expose 3d algorithms provider to Python | [#36661](https://github.com/qgis/QGIS/issues/36661) | [Commit 1f835df](https://github.com/qgis/QGIS/commit/1f835dfa9af51204ea1182df7bf722d84b223645) | No \-- too intrusive |
| \[symbology\] Don\'t force rasterized output when exporting point pattern fills | [#16100](https://github.com/qgis/QGIS/issues/16100) | [Commit 23396b7c](https://github.com/qgis/QGIS/commit/23396b7c864d00fc164db8c80d704a1ffc430ac1) | No \-- too intrusive |
| \[layouts\] Don\'t refresh the map canvas multiple times during atlas exports | [#30144](https://github.com/qgis/QGIS/issues/30144) | [Commit 57519e9](https://github.com/qgis/QGIS/commit/57519e9faa95fbfe6196134d9128caee48cb4b84) | niet kritisch |
| \[processing\] Fix double-evaluation of warp output parameter | [#30095](https://github.com/qgis/QGIS/issues/30095) | [Commit adeca2f](https://github.com/qgis/QGIS/commit/adeca2f586203913ae3702531b32579ed4c14344) |  |
| Fix incorrect warning message when turning off atlas preview | niet gerapporteerd | [Commit 3b0af960](https://github.com/qgis/QGIS/commit/3b0af960dd90af15cbe32e2fd7642408031e70f5) | N/B |
| Speed up message bar operations when many messages are shown | [#29698](https://github.com/qgis/QGIS/issues/29698) | [Commit 5dd29f0](https://github.com/qgis/QGIS/commit/5dd29f065e57fde532a21ae1bc9311aef9378455) | No \-- too intrusive |
| Fix oriented minimum bounding box calculation is wrong in some cases | [#36632](https://github.com/qgis/QGIS/issues/36632) | [Commit 97d0988](https://github.com/qgis/QGIS/commit/97d098884a7889346739d61bd9048e9dcf942d11) | [PR 36718 Commit 68c6a0e](https://github.com/qgis/QGIS/pull/36718/commits/68c6a0e31dc58fa23621e872739df9efded6e6b7) |
| Ensure symbol opacity is always ignored for selections | [#27859](https://github.com/qgis/QGIS/issues/27859) | [Commit 4de6a53](https://github.com/qgis/QGIS/commit/4de6a53235a6f7bd657c60d4f4d7160ed371d9df) | [PR 36718 Commit 99eb710](https://github.com/qgis/QGIS/pull/36718/commits/99eb710f89be0c6adc9acfdd888e366e6f2b796f) |
| Fix random sort order of symbols in Symbol Export dialog | [#20572](https://github.com/qgis/QGIS/issues/20572) | [Commit 987310f](https://github.com/qgis/QGIS/commit/987310fe90de2b21deb5c2564eb051e1d72548b2) | [PR 36718 Commit bfa6058](https://github.com/qgis/QGIS/pull/36718/commits/bfa60586e10735a6b670cd349dd8b9efd2ab2762) |
| Allow clearing heatmap weighting field | [#20256](https://github.com/qgis/QGIS/issues/20256) | [Commit 3961fa2](https://github.com/qgis/QGIS/commit/3961fa26f53e411c5c83b50e006df739ebda4c3e) | [PR 36718 Commit d2600d6](https://github.com/qgis/QGIS/pull/36718/commits/d2600d6d2cb765cb0641347ac342a74f663e4ba5) |
| Flag SAGA \'Merge Layers\' algorithm as having known issues | [#36375](https://github.com/qgis/QGIS/issues/36375) | [Commit f676c821](https://github.com/qgis/QGIS/commit/f676c821d9d9ff2d6e509d881ba2ea1853a34051) | N/B |
| Workaround odd upstream Qt issue where a painter with a semi-transparent brush with no solid pattern incorrectly applies the brush opacity to the pen when exporting to printer devices | [#36580](https://github.com/qgis/QGIS/issues/36580) | [Commit 38c8218](https://github.com/qgis/QGIS/commit/38c82187a65d8b4833f2c633a69a4d937a8725eb) | [PR 36718 Commit a562b67](https://github.com/qgis/QGIS/pull/36718/commits/a562b678438d26c1f80486fdfff422d70c8c6329) |
| Improve plugin watchdog message and UX | niet gerapporteerd | [Commit 150b373](https://github.com/qgis/QGIS/commit/150b373c7ae61c0548ab0803f9b30a36b15e7ab4) | No \-- too intrusive |
| \"\[layouts\] Warn when previewing an atlas and a feature with no geometry is encountered, when one or more maps are set to be driven by atlas feature\" | [#36556](https://github.com/qgis/QGIS/issues/36556) | [Commit 6ce84d2](https://github.com/qgis/QGIS/commit/6ce84d2c347f49c9aae0c1953e2b2529228db430) | No \-- too intrusive |
| Avoid proj \'object is not a concatenated operation\' warnings | niet gerapporteerd | [Commit 6baa209](https://github.com/qgis/QGIS/commit/6baa209285f452e5996537b1b0f1b5d924d5c59b) |  |
| \"Fix memory layers lose CRS definition if it does not have an authority associated with it\" | [#36241](https://github.com/qgis/QGIS/issues/36241) | [Commit e23a49a](https://github.com/qgis/QGIS/commit/e23a49a6b858cad9373c3bfb9ad66525622ce9ee) | [PR 36718 Commit c9350eb](https://github.com/qgis/QGIS/pull/36718/commits/c9350eb7439a29ac8ff3734cd7866f2403e3646e) |
| Implement spatial index detection for OGR provider | [#30530](https://github.com/qgis/QGIS/issues/30530) | [Commit f20801a](https://github.com/qgis/QGIS/commit/f20801a8bb3f23576e5e0d2abc6d3229e5044200) | [PR 36718 Commit 536906e](https://github.com/qgis/QGIS/pull/36718/commits/536906ec6375b70d88767e58a08550369a25d1a0) |
| Fix incorrect dialog title for raster layer properties | [#35510](https://github.com/qgis/QGIS/issues/35510) | [Commit 2099261](https://github.com/qgis/QGIS/commit/2099261230f82c5cd4439538e38754947c8f6bd6) | [PR 36718 Commit e809f48](https://github.com/qgis/QGIS/pull/36718/commits/e809f48cb9aaf03dfe8671c2d885f99b4a91922b) |
| Don\'t try to identify CRSes created just for ellipsoid definitions | niet gerapporteerd | [Commit 15b318b](https://github.com/qgis/QGIS/commit/15b318b50de9131ed1dd6bbf73ae5eb7572579a7) | No \-- too intrusive |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| allow sorting attribute table by field not listed in the table | [#25671](https://github.com/qgis/QGIS/issues/25671) | [PR #36236](https://github.com/qgis/QGIS/pull/36236) | N/B |
| fix layer tree dependencies (showinf symbols and main layer) | niet gerapporteerd | [PR #37000](https://github.com/qgis/QGIS/pull/37000) | N/B |
| fix Expression editor: syntax check fails if table is empty | [#37100](https://github.com/qgis/QGIS/issues/37100) | [PR #37137](https://github.com/qgis/QGIS/pull/37137) | N/B |
| fix setting of feature in expression preview widget | [#37214](https://github.com/qgis/QGIS/issues/37214) | [PR #37221](https://github.com/qgis/QGIS/pull/37221) | N/B |
| Freeze when showing attribute table of WFS layer | [#37224](https://github.com/qgis/QGIS/issues/37224) | nog niet gerepareerd | N/B |
| Lookups in tables with more than 100 entries show wrong value in Relation Reference form parts | [#37266](https://github.com/qgis/QGIS/issues/37266) | [PR #37280](https://github.com/qgis/QGIS/pull/37280) | [PR #37286](https://github.com/qgis/QGIS/pull/37286) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://www.opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Audun Ellertsen
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| SpatiaLite support for importing layers with binary fields | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36744](https://github.com/qgis/QGIS/pull/36744) | N/B |
| PostGIS support for importing layers with binary fields | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36708](https://github.com/qgis/QGIS/pull/36708) | [PR #36720](https://github.com/qgis/QGIS/pull/36720) |

Dit werd mogelijk gemaakt door [Kongsberg Digital](https://www.kongsberg.com/digital/)

Deze mogelijkheid werd ontwikkeld door [Audun Ellertsen](https://github.com/audun/)

{{<content-end >}}
