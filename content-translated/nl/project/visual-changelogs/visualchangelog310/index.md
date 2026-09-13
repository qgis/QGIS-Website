---
HasBanner: false
draft: false
releaseDate: '2019-10-25'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.10
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.10{#changelog310 }
![image1](images/projects/ce6ba8fc893e51ec721c9dded4dd98d11806a223.png)

Datum uitgave 25-10-2019

QGIS 3.10 brengt een uitgebreide lijst nieuwe wijzigingen en heel veel polijsten van bestaande mogelijkheden - de hoogtepunten daarvan zullen we hier proberen te behandelen. Zoals altijd herinneren we u er aan dat QGIS een open bron project is en vragen u om, als het mogelijk is, ons werk te ondersteunen door donaties, sponsoring of bijdragen aan de documentatie van de code, website, enzovoort.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de QGIS gemeenschap hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op qgis.org en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst met donoren]({{< ref "/funding/donate.md" >}}). Als u een officieel dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende lidmaatschappen]({{< ref "/funding/membership.md" >}}) voor details. Ondersteuning van QGIS helpt ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige dragende leden wordt hieronder weergegeven - een welgemeend bedankt voor al onze ondersteuners!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Kaartgereedschap
### Mogelijkheid: 3D-lijnlengten weergeven in resultaten gereedschap Objecten identificeren
Gebruiken van het gereedschap Objecten identificeren op een 3D-lijn neemt nu de 3D Cartesiaanse lengte van de lijn op in de resultaten (naast de bestaande 2D Cartesiaanse en 2D ellipsoïde lengtes).

![image2](images/entries/b1aba6e9334ee1d862bde8f66f9ae4d30d945703.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Mogelijkheid: Standaard instelling van resamplen voor nieuw toegevoegde rasterlagen
In QGIS 3.10 hebben we een nieuwe instelling toegevoegd voor de te gebruiken standaardmodus voor resamplen voor nieuw toegevoegde rastergegevenssets. (Deze instelling is te vinden in het paneel Renderen van het dialoogvenster Opties).

![image3](images/entries/07ae51e244cc5b1d6a971e386ea98f1314a3dfb1.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Verbeterd kopiëren/plakken van symbolen
We zijn echt van plan om van QGIS een gebruikersvriendelijk cartografisch gereedschap te maken dat een plezier is om mee te werken, dus hebben we veel nieuwe sneltoetsen toegevoegd, door de gehele interface, die u in staat stellen symbolen van het ene gedeelte van QGIS naar een ander te kopiëren en te plakken. U kunt bijvoorbeeld een symbool kopiëren uit een categorie en dat direct plakken in een andere categorie, of een item Vorm voor lay-out, of in het dialoogvenster van Stijlmanager!

![image4](images/entries/79f8365571da7b6c60f001f388d9c02d9e8920b2.webp)

Dit werd mogelijk gemaakt door [SMEC/SJ](https://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Modus voor plaatsing \"Midden van segment\" voor markerings- en gestreepte lijn-symboollagen
We hebben een nagelnieuwe modus \"Midden van segment\" toegevoegd voor het plaatsen van symbolen van markeringslijnen of gestreepte lijnen. Dit stelt u in staat markeringen of gestreepte lijnen te maken boven het middelpunt van individuele lijnsegmenten, wat cartografische effecten laat zien die eerder niet mogelijk waren (en de kwaliteit van vanuit ArcMap geconverteerde lagen met behulp van het gereedschap [SLYR](https://north-road.com/slyr/) verbetert).

![image5](images/entries/c1f50067d50b909e38b7333ad5d8d415e763801d.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Meer flexibele Data-bepaalde expressies voor verschuivingen
In eerdere uitgaven van QGIS waren alleen waarden tekenreeks in de indeling \'X,Y\' toegestaan voor verschuivingen voor data-bepaalde symbolen en labels. We hebben geluisterd naar de terugkoppeling van onze gebruikers dat dit verwarrend was en in QGIS 3.10 staan we nu arrays van getallen toe als een geldig resultaat voor de expressie voor verschuivingen. Bijv. \"array(3,5)\".

![image6](images/entries/1ccab8f4328238f5275e41c3d466bf27a5d097a2.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Labelen
### Mogelijkheid: Tekstindelingen en instellingen voor labels in stijlen voor QGIS maken en beheren
In QGIS 3.10 hebben we eindelijk een langverwachte mogelijkheid geïmplementeerd, die het voor gebruikers mogelijk maakt hun eigen bibliotheken met aangepaste tekstindelingen en instellingen voor labels te beheren, naast hun bestaande symboolbibliotheken!

Nu kan het dialoogvenster Stijlmanager worden gebruikt om tekstindelingen (die het lettertype, kleur, buffers, schaduwen, en achtergronden van tekstindelingen opslaan) en laag-brede instellingen voor labels te beheren. (Een \"tekstindeling\" bevat slechts instellingen voor lettertype en andere aan het uiterlijke gerelateerde instellingen, terwijl een \"instelling voor een label\" ook de voor het type laag specifieke instellingen, zoals plaatsing van labels, prioriteit, en instellingen voor renderen bevat).

Tekstindelingen en Instellingen voor labels bieden dezelfde functionaliteit als die welke u gewend was voor het beheren van symbolen en kleurverlopen in stijlen, inclusief het importeren en exporteren naar XML-bestanden, taggen, slimme groepen, favorieten etc\…

![image7](images/entries/bf657c21ba6deaff10ff80611a77b435e12155e5.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [North Road](http://north-road.com)
### Mogelijkheid: Markeringssymbolen als achtergrond voor labels
Naast alle andere opwindende verbeteringen voor labelen die we hebben doorgevoerd in 3.10, staan we nu het gebruiken van symbolen voor markeringen als een achtergrond voor labels toe. Dit stelt u in staat alle rijke beschikbare functionaliteit voor symbolen van markeringen te gebruiken als achtergrond voor labels, en vult de bestaande keuzes voor vormen en SVG-achtergronden aan!

![image8](images/entries/3a9fd11192cdbdaa2f139a28d63cc33e1d10c3bc.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [North Road](http://north-road.com)
### Mogelijkheid: Tekstballonnen label!
Een veelvoorkomend gebruik bij het plaatsen van labels op een volle kaart is om \'tekstballonen\' te gebruiken – labels die worden geplaatst buiten (of verplaatst van) hun geassocieerde object, met een lijn die het label verbindt aan het object. In QGIS 3.10 hebben we eigen ondersteuning toegevoegd voor het snel en gemakkelijk maken van mooie tekstballonnen voor labels (niet meer het verhaspelen van expressies of met de hand tekenen!).

We hebben veel instellingen toegevoegd voor het exact beheren van hoe deze tekstballonnen voor labels moeten worden getekend, en natuurlijk kunt u volledig voordeel halen uit de rijkheid van QGIS voor ondersteuning van lijnsymbolen in uw tekstballonnen! Dit omvat alle bestaande stijlen voor lijnsymbolen, laageffecten, en zelfs ondersteuning voor data-bepaalde instellingen!

In 3.10 maken we opties beschikbaar voor ofwel een \"doorgetrokken\" (directe lijn) of \"Manhattan\" (rechte lijnen) stijl voor tekstballonnen. Als u geïnteresseerd bent in het sponsoren van aanvullende stijlen voor tekstballonnen in een toekomstige uitgave, neem dan contact op met het team van QGIS om uit te zoeken hoe u dit kunt laten gebeuren!

![image9](images/entries/7bcc02d06eb7030a289e129b9bed2656d6c6fefb.webp)

Dit werd mogelijk gemaakt door [SMEC/SJ](https://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Uitlijning label over meerdere regels voor individuele labels wijzigen
We hebben een aanvullende optie toegevoegd om het u mogelijk te maken de uitlijning over meerdere regels op een basis per-label te beheren. Activeer gewoon het gereedschap Labeleigenschappen en klik op uw kaartlabels, en een nieuwe instelling voor uitlijning van de tekst is nu beschikbaar.

![image10](images/entries/14b307efef5de1085e4c402d3e06e5dd10a64ae2.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Niet geplaatste labels weergeven
Als u ooit bezorgd was over het feit dat automatisch plaatsen van labels belangrijke labels op uw kaart zou verbergen \-- dan is deze mogelijkheid voor u! In QGIS 3.10 hebben we een optie toegevoegd om \"Niet geplaatste labels\" weer te geven op uw kaart. U kunt dus onmiddellijk exact zien wat in de weergave is verborgen (ALIAS \"zien wat anderen niet kunnen zien\")!

Deze nieuwe instelling (waar u toegang toe krijgt via de werkbalk Labelen) zal deze Niet geplaatste labels renderen in een rode kleur (maar de kleur kan worden gewijzigd in het dialoogvenster Instellingen voor labels van het project). Na het identificeren van ontbrekende labels in uw kaart, raden we aan de bestaande gereedschappen voor Labelen, zoals de gereedschappen \"Label verplaatsen\" of \"Labels weergeven/verbergen\" te gebruiken om uw kaart opnieuw te schikken en deze labels opnieuw zichtbaar te maken.

![image11](images/entries/4e53a6482dacb6e2d6d1ff2a8c4592d98f82430a.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Afstand overschrijden voor lijnlabels
We begrijpen dat het maken van een cartografisch meesterwerk een veeleisende taak is, dus hebben we in QGIS 3.10 de mogelijkheden voor gebogen labels uitgebreid door een nieuwe instelling \"Afstand overschrijding\". Deze instelling stelt u in staat exact te beheren hoe ver een gebogen label zich mag uitstrekken tot voorbij de einden van een object lijn. Opvoeren van de afstand zal resulteren in het meer flexibiliteit geven aan het programma voor labelen voor het plaatsen van uw labels, wat ertoe zal leiden dat meer labels op betere locaties op uw kaart zullen worden geplaatst! Winst! De instelling werkt voor zowel de modi voor labels Gebogen als Parallel, en ondersteunt afstanden in mm/kaarteenheden/pixels/etc., en data-bepaalde afstanden.

![image12](images/entries/0b830e5ea769aacfd9c5bf9d8028ed278590d803.gif)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Data-bepaald besturingselement voor instelling \"Elk deel van een samengesteld object labelen\"
De optie \"Elk deel van een samengesteld object labelen\" was een van de weinige instellingen die eerder niet data-bepaald was voor labels. We hebben deze ontbrekende mogelijkheid verholpen in QGIS 3.10, en u kunt nu beheren of u alle delen gelabeld wilt hebben op een object-per-objectbasis!

![image13](images/entries/9db2c54c0d65bc61da8c0c46cfefcbab96c833df.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: \"Alle delen labelen\" beheren via het gereedschap Labeleigenschappen
We liegen niet als we zeggen dat QGIS 3.10 een liefdesbrief is voor het labelen van een kaart! Een andere nieuwe optie die we in deze versie hebben toegevoegd, is interactief beheer over het feit of alle delen van een object zouden moeten worden gelabeld via het gereedschap Labeleigenschappen.

![image14](images/entries/737cd2f8bc569ee9ad7df9aee02eec83b4e6facd.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verticale tekstrichting
Vanaf 3.10 is QGIS nu volledig uitgerust om verticaal georiënteerde labels te renderen Voor onze Chinese, Japanse en Koreaanse gebruikers: zegt het voort! :)

U kunt kiezen uit twee modi voor verticale oriëntatie: een die altijd labels verticaal rendert, of een alternatieve modus die dynamisch de richting uitzoekt, gebaseerd op de rotatie van het label.

![image15](images/entries/e49baccdb83da1b88433e2c7718642ae4a78810d.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Kerning van lettertype beheren
Een andere optie die we hebben toegevoegd voor het verbeteren van de conversie van symbologie van ArcMap naar QGIS (via [SLYR](https://north-road.com/slyr/)) is een nieuwe instelling voor het beheren of lettertypen moeten worden gespatieerd (of niet).

![image16](images/entries/b2a650a874e263173a56d93b046df7f031eb8d6e.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Renderen
### Mogelijkheid: Rasterlagen buiten het gerapporteerde bereik renderen 
Afhankelijk van de gebruikte technologie voor de server zou het door rasterlagen gerapporteerde kaartbereik soms kleiner kunnen zijn dan het feitelijke gebied dat kan worden gerenderd (valt speciaal op bij WMS-servers met symbologie die meer ruimte inneemt dan het gegevensbereik). Eerdere versies van QGIS zouden rasterlagen bijknippen tot de gerapporteerde bereiken, wat zou resulteren in afgebroken symbolen aan de randen van deze lagen. Nu is er een nieuwe optie die u toestaat dit gedrag te overschrijven en het gerapporteerde bereik voor getroffen servers te negeren.

Deze mogelijkheid werd ontwikkeld door Matthias Kuhn (Opengis.ch)
### Mogelijkheid: PDF's en TIF's voorzien van geoverwijzingen bij opslaan van het kaartvenster als afbeelding/PDF
In QGIS 3.10 hebben we ondersteuning geïmplementeerd voor ingebedde geoverwijzingen binnen PDF\'s en TIF\'s bij het gebruiken van het opgeslagen \[kaartvenster\] als afbeelding of PDF.

![image17](images/entries/1030adf0c9c0c46ff5a38a09ae16a735bdff3684.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Nieuwe decoratie voor afbeelding kaartvenster
We hebben een nagelnieuwe decoratie toegevoegd voor het kaartvenster van QGIS, die het u mogelijk maakt een bitmap en SVG-afbeelding overleg (logo, legenda, etc.) toe te voegen aan uw kaartvenster.

Net als met andere delen van QGIS ondersteunt de decoratie afbeelding aan te passen vulling- en omtrekkleuren voor parameter-ingeschakelde SVG's.

![image18](images/entries/41ab256b477b0baf0971b398f882a6633cd12615.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Classificatie voor logaritmische schaal
U kunt nu een techniek voor een classificatie, gebaseerd op logaritme, gebruiken bij het maken van bereiken voor de renderer Gradueel.

![image19](images/entries/bb6303d9589972781988549283ef150700ba5863.webp)

Deze mogelijkheid werd ontwikkeld door [OPENGIS.ch](https://www.opengis.ch)
## 3D-objecten
### Mogelijkheid: Gereedschap Meten in 3D-kaartweergave
Nu kunt u afstanden meten in 3D-kaartweergaven! Dit nieuwe gereedschap is beschikbaar in de werkbalk 3D-kaartweergave en heeft dezelfde werkstroom als het gereedschap Meten voor 2D (met dezelfde instellingen voor configuratie van kleuren voor elastiek, eenheden, decimale plaatsen, etc.). Het heeft ook hetzelfde gedrag (links-klikken voor toevoegen van een nieuw punt, middel-klikken om het laatste punt te verwijderen en rechts-klikken om het meten opnieuw te beginnen). Dit stelt u in staat afstanden te meten in 3D, bijv. de afstand tussen de daken van twee gebouwen of de lengte van een rivier die afdaalt langs een berg. Bekijk het gereedschap 3D Meten in actie:

Dit werd mogelijk gemaakt door [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

Deze mogelijkheid werd ontwikkeld door [Ismail Sunni](http://ismailsunni.id)
### Mogelijkheid: Renderen Billboard voor punten
We hebben een nieuw soort stijl voor renderen toegevoegd voor puntlagen. Het stelt u in staat het punt weer te geven met een symbool van QGIS (bijv. markering, SVG, etc) dat altijd gericht is op de gebruiker en altijd dezelfde grootte heeft. U kunt een voorbeeld van het gebruik zien in de video.

Dit werd mogelijk gemaakt door [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

Deze mogelijkheid werd ontwikkeld door [Ismail Sunni](http://ismailsunni.id)
### Mogelijkheid: 3D-navigatie op scherm
In eerdere versies van QGIS kon u al door de 3D-wereld navigeren met een muis en het toetsenbord. Helaas is het voor een nieuwe gebruiker niet zo eenvoudig om ze te gebruiken! 3D navigeren op scherm zal helpen bij het navigeren in de 3D-wereld. Er zijn knoppen om in/uit te zoomen, op/neer kantelen, verschuiven op/neer/links/rechts, en roteren van de 3D-kaartweergave. Deze mogelijkheid kan worden geactiveerd in de werkbalk 3D-kaartweergave Bekijk hoe het te gebruiken in deze video:

![image20](images/entries/570ff6f8c365a78d05bb56cfdbd8647f83aac331.webp)

Dit werd mogelijk gemaakt door [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

Deze mogelijkheid werd ontwikkeld door [Ismail Sunni](http://ismailsunni.id)
## Afdruklay-outs
### Mogelijkheid: Schikking van rechts naar links voor legenda's
Dankzij de giften van onze van rechts naar links locale-gebruikers hebben we een nieuwe keuze toegevoegd voor het schikken van elementen van de legenda. Dit omvat symbolen links OF symbolen rechts van de tekst van de legenda, en opties voor uitlijnen voor groepen, subgroepen en items tekst.

Deze mogelijkheid maakt het mogelijk gebruikersvriendelijke legenda's van rechts naar links te maken. We maken deze stijl voor uitlijning van rechts naar links zelfs de standaard bij het maken van nieuwe legenda's onder op RTL gebaseerde locale om dingen gebruikersvriendelijker te maken.

![image21](images/entries/420b784c4fc79a09358201c8814cfe48b82dbbca.webp)

Dit werd mogelijk gemaakt door [Kaplan Open Source](https://kaplanopensource.co.il/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Marge beheren onder koppen van groepen en subgroepen van legenda
Als u uit bent op pixel-perfect beheer over het uiterlijk van uw legenda \-- dan is deze voor u! QGIS 3.10 stelt u nu in staat de afstand aan te passen die wordt toegepast onder koppen van groepen of subgroepen.

![image22](images/entries/78263d3350afd05147928378f81dddba13961acc.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Data-bepaalde instellingen in tekstindelingen
Omdat zoveel van de cartografische kracht van QGIS voortkomt uit de flexibiliteit van data-bepaalde instellingen voor symbolen, hebben we het nu mogelijk gemaakt ze ook te gebruiken voor tekstindelingen! Dat betekent dat u nu data-bepaalde eigenschappen kunt gebruiken, overal waar tekstindelingen worden gebruikt, bijv. binnen tekst van de lay-out voor de schaalbalk.

![image23](images/entries/69961f6faa732b683ccfb1ab539250b21ea5bd26.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Variabele @scale_value
Als aanvulling op de nieuwe ondersteuning voor data-bepaalde instellingen binnen tekstindelingen, hebben we een nieuwe variabele voor een expressie @scale_value toegevoegd. Deze kan worden gebruikt bij het evalueren van eigenschappen van data-bepaalde tekstindelingen tijdens het renderen van de tekst voor de schaalbalk, en stelt u uiteindelijk in staat om aanpassingen per-label van de tekst binnen schaalbalken te hebben (bijv. bepaalde labels voor afstanden vet weergeven).

![image24](images/entries/ec2940b4222b8172403b20b0f70af0588c38f0cc.gif)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Opties voor plaatsen van label Schaalbalk
We hebben de lay-out van schaalbalken uitgebreid met aanvullende opties voor opmaken, en een paar instellingen toegevoegd om het plaatsen van labels voor de schaalbalk te verfijnen. Nu kunt u definiëren of labels boven of onder de schaalbalk zelf moeten worden weergegeven, alsook instellen of labels moeten worden gecentreerd in het midden van een segment of aan het eind ervan geplaatst moeten worden.

![image25](images/entries/e571fc1811ccf58e007a7913600b65377e31ed41.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Vereenvoudigen van exporteren van PDF of SVG
Eerdere versies van QGIS maakten vaak ENORME uitvoer voor PDF (of SVG), omdat deze uitvoer veel overbodige punten bevatten die niet herkenbaar waren als anders voor de DPI van de export. Nu passen we, standaard, een vereenvoudiging toe bij het schrijven naar PDF- of SVG-bestanden, wat er voor zorgt dat geometrieën worden vereenvoudigd en aanwezige overbodige punten automatisch worden verwijderd (bijv. als de DPI voor het exporteren 300 dpi is, zullen punten die minder dan 1/600 inch verschillen van elkaar worden verwijderd).

Deze nieuwe instelling, \"Geometrieën vereenvoudigen om de bestandsgrootten te verkleinen\", is zichtbaar in de dialoogvensters voor instellingen voor het exporteren als SVG of PDF, weergegeven wanneer een lay-out/Atlas/rapport wordt geëxporteerd naar PDF of SVG.

Geen belachelijk complexe en grote bestandsgrootte na exporteren voor uw afdruklay-outs van QGIS! Naast de problemen met de bestandsgrootten, veroorzaken zij ook problemen bij het proberen te laden in andere toepassingen, bijv. Inkscape dat zich verslikt in het enorme aantal punten en uiteindelijk nog slechts voortkruipt\…. ouch!

![image26](images/entries/7eea84e316a148c6872369d3df5fb63a6bc2f043.webp)

Dit werd mogelijk gemaakt door de GeoPDF export group: Land Vorarlberg; Kantons van Zug, Thurgovia en Neuchâtel; Steden Wenen en Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Verbeterde exports SVG-lagen
Terugkoppeling van gebruikers leerde ons dat de manier waarop we in eerdere uitgaven gelaagde SVG-bestanden maakten, frustrerend was om mee te werken. In QGIS 3.10 hebben we dus deze mogelijkheid opnieuw opgebouwd en nu zullen de laagnamen van de SVG overeenkomen met de laagnamen uit QGIS, wat het voor ontwerpers veel gemakkelijker maakt de inhoud van het document te begrijpen! Lees meer hierover en gerelateerde mogelijkheden [hier](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/).

![image27](images/entries/dac35ad47f56dd24456df6d318359a0d70efeb15.webp)

Dit werd mogelijk gemaakt door de GeoPDF export group

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Indicatie voor opnieuw tekenen kaartlay-out
In eerdere uitgaven van QGIS was er geen manier om aan te geven of het vernieuwen van de kaart was voltooid binnen een venster van QGIS-afdruklay-out ontwerpen. We hebben dus een nieuwe indicator in de Statusbalk toegevoegd die weergeeft of het opnieuw tekenen nog nazoemt op de achtergrond. Geen verwarring meer voor de gebruiker!

![image28](images/entries/8c6426a723b9fdc1cead1949f3304db4763ecb9c.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: GeoPDF exporteren
Wanneer u nu pdf\'s exporteert vanuit QGIS, is er een optie om het als GeoPDF te exporteren. Als u deze pdf opent met een compatibele pdf-lezer, zult u in staat zijn lagen in en uit te schakelen, te verplaatsen en te zoomen in de pdf en interactief objecten kunnen bevragen! Verder kunt u deze documenten van GeoPDF terug importeren in QGIS als vectorlagen, en alle objecten zien op hun originele locaties en met hun originele waarden voor attributen.

Exporteren naar GeoPDF is beschikbaar voor zowel afdruklay-outs als voor het kaartvenster. We hebben heel veel flexibiliteit voor deze nieuwe optie toegevoegd, bijv. met opties voor het beheren van welke lagen als interactieve lagen zullen worden geëxporteerd. U kunt er zelfs voor kiezen om meerdere kaartthema's naar een enkel document van GeoPDF te exporteren, zodat uw lezers interactief kunnen schakelen tussen deze thema's! (Wow!)

Onthoud dat exporteren naar GeoPDF een versie van QGIS vereist die is gebaseerd op GDAL 3.0 of later.

Lees meer op [QGIS 3.10 Loves GeoPdf](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/)

![image29](images/entries/9f73cce9c3f3ff81c6b66adab654ff4e23524ae1.webp)

Dit werd mogelijk gemaakt door de GeoPDF export group: Land Vorarlberg; Kantons van Zug, Thurgovia en Neuchâtel; Steden Wenen en Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Data-bepaald beheer rastereigenschappen
We hebben data-bepaald beheer voor kaartrasters van lay-outs toegevoegd, om u extra flexibiliteit te geven voor het uiterlijk en gedrag van deze rasters, en om het voor u mogelijk te maken sjablonen voor lay-outs en Atlassen te maken met rasters die dynamisch reageren op wijzigingen in de schaal van de kaart.

Nu bent u in staat data-bepaald beheer in te stellen voor:
- status raster ingeschakeld
- X/Y-intervallen voor raster
- X/Y-verschuivingen voor rasters
- framegrootte en marge voor rasters
- afstanden voor annotatie vanaf het frame voor het raster
- kruisgrootte van het raster
- lijndikte voor frame van het raster

![image30](images/entries/e219a18e997a6506314c1777c94050bf4a69cf9b.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Dynamische grootten segment rasters
Net als de bestaande instelling voor de schaalbalk met dezelfde naam, stelt deze nieuwe instelling u in staat een op de paginagrootte gebaseerd bereik in te stellen voor intervallen van het kaartraster. De interval voor het raster zal dynamisch worden berekend, gebaseerd op het kaartbereik, en op schaal worden gebracht voor de grootst mogelijke \"prettige\" interval die resulteert in rastergrootten binnen het gewenste bereik.

Deze wijziging maakt het voor u mogelijk lay-outs en sjablonen voor lay-outs te maken met rasters die elegant reageren voor een groot bereik aan schalen voor de kaart!

![image31](images/entries/245ada907ba2e14ad291dae54b93adb327b64225.webp)

Dit werd mogelijk gemaakt door Andreas Neumann

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Favoriete plaatsen voor lay-outkaarten
Een andere langverzochte mogelijkheid die we hebben geïmplementeerd voor QGIS 3.10 is een nieuwe knop op de werkbalk Item-eigenschappen voor een kaartitem in Lay-out, die u in staat stelt direct een kaartitem in te stellen voor een Favoriete plaats!

![image32](images/entries/4b8ed681a38435a2f0bf299fd28f299e2873848c.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Expressies
### Mogelijkheid: Nieuwe functies voor expressies
- **attributes()**: geeft een kaart terug die alle attributen van een object bevat, met veldnamen als kaartsleutels. We hebben nu flexibele, robuuste ondersteuning voor het werken met waarden van de kaart in expressies, dus dit maakt een snelle conversie van attributen van een object naar een te gebruiken kaart mogelijk met deze handige functies!
- Nieuwe optionele parameters \"format\" werden toegevoegd aan de functies **to_date**, **to_datetime**, en**to_time**
- **collect_geometries**: deze nieuwe functie verzamelt een set geometrieën in een object geometrie met meerdere delen. Delen van de geometrie kunnen ofwel worden gespecificeerd als afzonderlijke argumenten voor de functie of (meer flexibel) als een array met delen van de geometrie. Deze functie maakt het mogelijk dat geometrieën worden gemaakt met op iteratie gebaseerde benaderingen, zoals transformeren van een gemaakte array met behulp van generate_series, bijv: | `collect_geometries( array_foreach( generate_series( 0, 330, 30), project($geometry, .2, radians(@element)) ) )` | Geeft een mooi radiaal effect van punten die het centrale objectpunt omringen als dat wordt gebruikt als een MultiPoint geometriegenerator
- Een nieuwe  functievariant voor expressie **make_line** die een array van punten accepteert. Dit maakt het mogelijk lijnen te maken uit een variabel aantal punten, en uit reeksen van samengevoegde/dynamisch gemaakte reeksen.

## Digitaliseren
### Mogelijkheid: Ondersteuning voor GPS-tijdstempel
We hebben de bestaande op GPS gebaseerde functionaliteit in QGIS 3.10 vernieuwd, en nieuwe opties toegevoegd voor het automatisch ophalen en opslaan van GPS-tijdstempels naast op GPS gebaseerde objecten.

Dit werd mogelijk gemaakt door [NIWA](https://niwa.co.nz/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (North Road)](http://north-road.com)
### Mogelijkheid: toegestane uitzonderingen gat
In QGIS 3.4 introduceerden we de mogelijkheid om lagen van QGIS te configureren om topologische controles uit te voeren bij elke bewerking Opslaan. Voor 3.10 hebben we nu een nieuwe optie toegevoegd om te controleren op \"gaten\" wat u in staat stelt om actief enkele gaten te markeren als toegestaan. Deze uitzonderingen zullen worden opgeslagen op een afzonderlijk te configureren laag. Wanneer een gat wordt gedetecteerd, heeft u ofwel de mogelijkheid om het te repareren of om het toe te voegen aan de toegestane uitzonderingen, met één druk op de knop.

![image33](images/entries/4a7b306942755ac96cfa9bc97abbfd7815d17ad4.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gegevensbeheer
### Mogelijkheid: Foreign Keys samenstellen
In QGIS 3.10 hebben we de mogelijkheid toegevoegd om relaties voor lagen te maken die samengestelde foreign keys gebruiken. QGIS ondersteunt nu volledig het bewerken van ouder- en kindobjecten die zijn gekoppeld met meer dan één attribuut. Deze functionaliteit is toegankelijk in de Projecteigenschappen -\> tab Relaties.

![image34](images/entries/6b2177a5781bc2d5cdfb63f121501a734897e4a1.webp)

Dit werd mogelijk gemaakt door [California Geological Survey](https://www.conservation.ca.gov/cgs)

Deze mogelijkheid werd ontwikkeld door [OPENGIS.ch](https://www.opengis.ch)
### Mogelijkheid: Afhankelijkheden voor circulaire gegevens toevoegen
Ooit problemen gehad met snappen bij het bewerken van een object dat door iemand anders was aangepast (of een nare trigger van de database)? Afhankelijkheden voor gegevens maken het vernieuwen van de inhoud van afhankelijke lagen mogelijk als de gegevens worden gewijzigd. We verbeterden de ondersteuning voor afhankelijkheden in QGIS door het vernieuwen van de aangepaste laag zelf toe te staan, wat een soort circulaire afhankelijkheid is (een puntenlaag en een lijnenlaag bijvoorbeeld die van elkaar afhankelijk zijn). Geen snappen meer aan spook-objecten!

Meer informatie in het [pull request](https://github.com/qgis/QGIS/pull/30947)

![image35](images/entries/3b93e7b25eef3e3f149ba8db022e467258a74116.webp)

Dit werd mogelijk gemaakt door [QGIS.org](https://qgis.org)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Formulieren en widgets
### Mogelijkheid: Afhankelijke widgets real-time bijwerken
Werkt waarden van widgets bij in real time tijdens het bewerken van de verwezen velden. Wanneer widget A een standaard waarde bevat die afhankelijk is van widget B, wordt die bijgewerkt zodra widget B wordt bewerkt.

![image36](images/entries/0f24e8e2746cb4b7890d015c2ae476f1f1bf96ef.webp)

Dit werd mogelijk gemaakt door [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](http://www.opengis.ch)
## Analyse-gereedschappen
### Mogelijkheid: Opgeslagen filterexpressies voor attributentabellen
Waar eerdere versies van QGIS u in staat stelden attributentabellen te filteren met een aangepaste expressie, gingen deze expressies verloren als de attributentabel werd gesloten. Nu hebben we de mogelijkheid toegevoegd om uw aangepaste filterexpressies voor het dialoogvenster Attributentabel op te slaan en te beheren. U kunt nu uw eigen persoonlijke verzameling van nuttige filters opbouwen, die met enkele muisklikken altijd weer beschikbaar zijn om opnieuw te gebruiken!

![image37](images/entries/d6791d32d649fdc3b2e86aa257a33796391e13e0.webp)

Dit werd mogelijk gemaakt door [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

Deze mogelijkheid werd ontwikkeld door [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Mogelijkheid: Nieuwe bewerkingen voor Rasterberekeningen
U vraagt, we luisteren: `abs` , `min` en `max` zijn nu beschikbaar in de gebruikersinterface van Rasterberekeningen!

![image38](images/entries/8a0081e087a6f9ff9180615f34bb56ea6dccc649.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.qcooperative.net)
## Processing
### Mogelijkheid: Nieuw algoritme \"Laag uit punt maken\"
Dit algoritme maakt een nieuwe vectorlaag, die één enkel object bevat, waarvan de geometrie overeenkomt met een parameter voor een punt. Het kan in modellen worden gebruikt om een punt naar een laag te converteren die kan worden gebruikt voor andere algoritmen die een op een laag gebaseerde invoer vereisen.

![image39](images/entries/9f61759f0b8d6a61ea070a5328c4f641c582778e.webp)

Deze mogelijkheid werd ontwikkeld door Olivier Dalang
### Mogelijkheid: Gevorderde parameters model
Bij het maken van invoer voor een model van Processing kunt u nu deze parameters voor de invoer markeren als opties \"Geavanceerd\". (Geavanceerde parameters zijn standaard verborgen als gebruikers uw model uitvoeren via Toolbox van Processing)

![image40](images/entries/d9224e26da62b092d56fd091195942d4142e9bd7.webp)

Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Mogelijkheid: Alle op GDAL gebaseerde algoritmes ondersteunen nu vrije-vorm \"aanvullende parameters\"
We voegden een optionele parameter \"Aanvullende parameters opdrachtregel\" toe aan alle algoritmes van GDAL. Nuttig voor gevallen waarin u een specifiek argument(en) voor de opdrachtregel moet doorgeven die niet wordt weergegeven in de UI van het algoritme.

![image41](images/entries/18f42d184246ed167be10dee72f5000671d7ac01.webp)

Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Mogelijkheid: Grootte metatile voor XYZ-tegels
U kunt nu een aangepaste grootte instellen voor metatile bij het maken van XYZ-tegels. Grotere waarden zouden het renderen van tegels kunnen versnellen en beter labelen kunnen verschaffen (minder gaten zonder labels) ten koste van het gebruiken van meer geheugen.

![image42](images/entries/471f15d2616ffc1531c8eef95d4d8ed87d161998.webp)

Deze mogelijkheid werd ontwikkeld door Martin Dobias
### Mogelijkheid: Nieuw type parameter voor kleuren
QGIS 3.10 brengt een nieuw type parameter om te gebruiken in modellen en scripts van Processing, die het voor gebruikers mogelijk maken een kleurwaarde te kiezen. Nuttig voor modellen en algoritmes die een kleurwaarde als invoer vereisen!

![image43](images/entries/87cae0401b93aa308c156a615e63a71e98d25980.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuw algoritme \"Stijldatabase maken uit project\"
Dit algoritme neemt alle stijlobjecten (inclusief symbolen, kleurverlopen, tekstindelingen en instellingen voor labels) uit een project van QGIS uit en slaat ze op in een nieuwe XML-stijldatabase, die kan worden beheerd en geïmporteerd via het dialoogvenster Stijlmanager.

![image44](images/entries/8d6075eb1c4fc38b76f9761836048e940be408f8.webp)

Dit werd mogelijk gemaakt door [SMEC/SJ](https://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Bestandsfilter en standaard waarden voor invoer van bestand en map in modellen
Voor invoer van bestanden en mappen in modellen van Processing hebben we een nieuwe instelling voor bestandsfilters toegevoegd (met enkele standaard bestandsindelingen beschikbaar als optionele voorkeuze), en maakt het u mogelijk een standaard waarde voor deze invoer in te stellen.

![image45](images/entries/94fe90f54308a81c5f031066c132e1ad5e8e6ac2.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuw algoritme \"Stijldatabases combineren\"
Het nieuwe algoritme \"Stijldatabases combineren\" combineert meerdere stijldatabases van QGIS tot een enkele stijldatabase. Als er symbolen bestaan met dezelfde namen tussen de verschillende brondatabases, zullen deze worden hernoemd, zodat ze unieke namen hebben in de gecombineerde database van de uitvoer. Het is ontworpen om gebruikers een gemakkelijke manier te geven om meerdere afzonderlijke stijldatabases samen te voegen tot een enkele geünificeerde database.

Het werkt briljant met gemaakte resultaten door het uitvoeren van het algoritme \"Stijldatabase maken uit project\" in een batchmodus!

![image46](images/entries/479f2a711f8c4b254e72348eda3c79187d4117f2.webp)

Dit werd mogelijk gemaakt door [SMEC/SJ](https://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: XYZ-tegels maken met meerdere threads
Het  bestaande algoritme XYZ-tegels maken is geoptimaliseerd en kan nu tegels maken met behulp van meerdere threads voor verwerking.

![image47](images/entries/60aac076d447f244dd232a8e8766a109032a9540.webp)

Deze mogelijkheid werd ontwikkeld door Isghj5
### Mogelijkheid: Nieuwe algoritmes voor exporteren en importeren van Favoriete plaatsen naar/uit kaartlagen
We hebben, om de vernieuwing van de Favoriete plaatsen in QGIS 3.10 aan te vullen, nieuwe algoritmes voor Processing toegevoegd die u in staat stellen een aantal nieuwe Favoriete plaatsen te maken, overeenkomstig de objecten van een laag, of om bereiken van bestaande Favoriete plaatsen te exporteren naar een nieuwe polygoonlaag.

![image48](images/entries/d0471bc7ea65e476537c8828a7850a64ca9120ef.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuw algoritme \"Objecten splitsen op teken\"
Dit nagelnieuwe algoritme splitst objecten in meerdere uitvoerobjecten door een veldwaarde te splitsen op een gespecificeerd teken.

Als bijvoorbeeld een laag meerdere kommagescheiden waarden bevat, die zijn opgenomen in een enkel veld, kan dit algoritme worden gebruikt om die waarden in meerdere uitvoerobjecten te splitsen. Geometrieën en andere attributen blijven in de uitvoer ongewijzigd.

Optioneel mag de tekenreeks voor het scheiden een reguliere expressie zijn voor toegevoegde flexibiliteit.

Dit algoritme werd ontworpen om te gebruiken in modellen die invoerbestanden moeten verwerken met meerdere samengevoegde waarden in een attribuut, bijv. geocoderen van een tabel met tekenreeksen in de indeling \"address1,address2,address3\".

![image49](images/entries/a0adf902641c8ace142d9749e632e114262342cd.webp)

Dit werd mogelijk gemaakt door [SMEC/SJ](https://www.smec.com/en_au)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuw algoritme Klimmen langs lijn
Eerder beschikbaar als een plug-in, is het algoritme \"Klimmen langs lijn\" toegevoegd aan de out-of-the-box-gereedschapsset van QGIS. Dit algoritme berekent de geaccumuleerde hoogteverschillen voor lijnen in een invoerlijnenlaag, berekend met behulp van de Z-waarden van de lijnpunten. Een kopie van de invoerlijnenlaag wordt teruggegeven met aanvullende attributen voor geaccumuleerde klim en afdaling, alsook de minimum- en maximum Z-waarden voor elke lijn.

![image50](images/entries/1b68212fa4a991c79f7d352b5ee3798d0e9a10a3.webp)

Deze mogelijkheid werd ontwikkeld door [Håvard Tveite (NMBU) en Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Mogelijkheid: Algoritme Grid maken geporteerd naar C++
We hebben het algoritme Grid maken geporteerd van Python naar C++ om het algoritme te versnellen. Het algoritme wordt nu veel sneller voor u uitgevoerd en is ook in staat punt\|lijn\|rechthoek\|diamant\|hexagoon-regelmatige vectorrasters te maken in hoge resolutie voor grote bereiken (bijv. hele landen) binnen een redelijke tijdspanne.

![image51](images/entries/6ef35bc88e69aaf92f5f223249bf792ffd4d28d5.webp)

Dit werd mogelijk gemaakt door [Clemens Raffler](https://twitter.com/root676)

Deze mogelijkheid werd ontwikkeld door [Clemens Raffler](https://github.com/root676)
## Browser
### Mogelijkheid: Symbolen uit projecten van QGIS uitnemen binnen de browser
Het paneel Browser van QGIS wordt steeds krachtiger en krachtiger! In 3.10 hebben we een nieuwe optie toegevoegd bij het met rechts klikken op een project van QGIS binnen de browser: \"Symbolen uitnemen\". Selecteren van deze optie opent een dialoogvenster voor Stijlmanager dat alle symbolen, kleurverlopen, tekstindelingen en instellingen voor labels uit het geselecteerde project weergeeft, wat u in staat stelt deze symbolen eenvoudig vanuit de Browser te exporteren.

![image52](images/entries/4c9dd54203cbce44f91e85ed1ff01f1cbb4a40c5.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
## Algemeen
### Mogelijkheid: Nieuwsitems weergeven op welkomstpagina
Een gecureerde nieuwsfeed van QGIS wordt nu weergegeven op de Welkomstpagina. Dit geeft ons eindelijk een direct kanaal om nieuw s over het project door te zetten naar AL onze gebruikers! Verwacht maar dat er veel interessant(e) nieuws, tips, en gebeurtenissen van QGIS uw kant op komen!

![image53](images/entries/d3822539302bcd15ae05ef697abafaa1aa5c3ae4.webp)

Dit werd mogelijk gemaakt door QGIS.org

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Milliradialen (SI-definitie) en mil (NATO) eenheden
QGIS 3.10 stelt u in staat hoeken in twee nieuwe eenheden te meten, milliradialen (SI-definitie) en mil (NATO) eenheden.

![image54](images/entries/f208b7c32bfe608a448dc2e9359de20e3e4397dd.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Filteren dialoogvenster Aanpassen van de interface
We hebben een nieuw \"zoek\"-vak toegevoegd aan het dialoogvenster voor het aanpassen van de interface, dat u in staat stelt door de widgets te filteren en gemakkelijk de widget te zoeken die u probeert aan te passen\…

![image55](images/entries/57f395b303ba963e67242e0f2cfe7104e61f2ad0.webp)

Deze mogelijkheid werd ontwikkeld door DelazJ
### Mogelijkheid: Verbeterd automatisch repareren verbroken lagen
Wanneer een laagpad wordt gerepareerd in een project, zal QGIS 3.10 automatisch door alleen andere verbroken paden scannen en proberen elke automatisch te repareren die ook naar hetzelfde originele verbroken bestandspad wezen. Elke wijziging die het repareren van verbroken laagpaden versnelt is in onze ogen een welkome wijziging!

![image56](images/entries/0119e6f0b3d950d613d224d7bbd53a38575b3579.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Favoriete plaatsen super opgeladen!
We hebben totaal vernieuwd hoe Favoriete plaatsen worden weergegeven en beheerd in QGIS 3.10. Favoriete plaatsen worden nu weergegeven in het paneel Browser, en kunnen opnieuw worden gegroepeerd in aangepaste, gecategoriseerde mappen. Dit biedt een veel gemakkelijkere manier om door uw Favoriete plaatsen te navigeren en ze te beheren.

We hebben ook een nagelnieuw dialoogvenster voor het bewerken van Favoriete plaatsen, dat als mogelijkheid een widget voor het bereik heeft dat het bewerken van Favoriete plaatsen fantastisch faciliteert.

Favoriete plaatsen kunnen nu ook worden gesleept en neergezet op kaartvensters, wat het voor secundaire kaartvensters mogelijk maakt naar een bepaalde Favoriete plaats te zoomen. Dit maakt het mogelijk dat favoriete plaatsen netjes meespelen in projecten met meerdere kaartvensters, omdat u ze in een specifiek kaartvenster neer kunt zetten om te zoomen.

![image57](images/entries/8329961bfa04631c5a970888f9a21bad66ddc6fa.webp)

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin, Nyall Dawson
### Mogelijkheid: Actie \"Objecten opnieuw selecteren\" in menu Bewerken -\> Selecteren
Ooit 10 minuten gespendeerd aan het nauwkeurig maken van een interactieve selectie van objecten, alleen maar om ze per ongeluk te deselecteren met een foute muisklik? Indien ja, dan is deze mogelijkheid speciaal voor u ontworpen! Nu kunt u een selectie op een laag herstellen die volgt op een bewerking leegmaken, via de nieuwe optie \"Objecten opnieuw selecteren\" in het menu Bewerken.

![image58](images/entries/e1234a3ca30866b91f64f97b83fdf0fb90838cb6.webp)

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Parallelliseren bouwen index snappen
Het idee was om voor elke laag het berekenen van de snapcache (sequentieel op dit moment) te parallelliseren en niet-blokkerend te maken. Als consequentie is het nog steeds mogelijk QGIS te gebruiken zelfs als de snapcache momenteel wordt opgebouwd. Gebruiker kan bijvoorbeeld beginnen met het bewerken van een knoop, terwijl het bouwen van de snapcache nog voortduurt.

Deze mogelijkheid werd ontwikkeld door Oslandia
### Mogelijkheid: Sjablonen voor projecten van QGIS
QGIS 3.10 bevat de mogelijkheid om sjablonen voor het project direct te gebruiken vanaf de Welkomstpagina. Aanvullend kunt u nu sjablonen voor ene project verzenden naar uw gehele organisatie door ze te plaatsen in een systeemmap, naast de reeds bestaande mogelijkheid om ze in de map van ene gebruikersprofiel te plaatsen.

![image59](images/entries/5adaa5a973e0b232bae3a8dbab8739c8887ac70e.webp)

Dit werd mogelijk gemaakt door [het project QGIS](https://www.qgis.org)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor lezen-schrijven voor .shz en .shp.zip
Voor versies van QGIS gebaseerd op GDAL 3.1 kunt u nu enkele-laag ZIP gecomprimeerde shapefiles (.shz), of met meerdere lagen (.shp.zip) openen en bewerken. Ongeacht waar u zich bevindt in de strijd tussen Shapefile vs Geopackage, u zult deze mogelijkheid tot het opruimen van uw mappen verwelkomen en shapefiles als een enkel bestand opslaan!

Deze mogelijkheid werd ontwikkeld door Even Rouault
### Mogelijkheid: Authenticatie voor provider Oracle
We hebben de Oracle databaseprovider bijgewerkt door volledige ondersteuning voor het in QGIS ingebouwde systeem voor authenticatie toe te voegen.

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Verbeterde ondersteuning voor PostGIS raster
PostGIS rasterlagen worden nu weergegeven in het paneel Browser en in het dialoogvenster Databronnen beheren, wat het voor u gemakkelijker maakt deze lagen te beheren en toe te voegen aan uw projecten. Momenteel wordt alleen ondersteuning voor lezen vanuit de Browser ondersteund - u kunt geen rasters in een database van PostGIS slepen met de Browser.

Deze mogelijkheid werd ontwikkeld door Alessandro Pasotti
### Mogelijkheid: Oracle - Database ondersteuning voor transactie
Voor versie 3.10 hebben we de Oracle-databaseprovider opgewaardeerd en ondersteuning toegevoegd voor het bewerken van lagen via transacties.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Dimensies Z/M in lagen Tekengescheiden tekst
We hebben optionele ondersteuning voor velden Z en M toegevoegd voor QGIS tekengescheiden tekstprovider, wat het voor u mogelijk maakt Z- of M-ingeschakelde lagen direct te maken vanuit CSV-bestanden.

![image60](images/entries/bfaa5fc4c03d27e5345475172f5e7bdb20a4f6ff.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Statische gegevensproviders
Één taak vanachter de schermen die we hebben voltooid voor QGIS 3.10 is het opnieuw opbouwen van de infrastructuur voor providers. Nu staan providers zowel dynamisch als statisch koppelen toe. Dit was een vereiste om bibliotheken voor QGIS te kunnen bouwen voor platformen die dynamisch koppelen niet toestaan (iOS), en het mogelijk maken voor op QGIS gebaseerde gereedschappen, zoals de app Input data collection, om te worden gedistribueerd voor op iOS gebaseerde apparaten!

Dit werd mogelijk gemaakt door [Lutra Consulting Ltd.](http://www.lutraconsulting.co.uk)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik, Martin Dobias](http://www.lutraconsulting.co.uk/about)
## QGIS Server
### Mogelijkheid: SVG gebruiken in QGIS Server
Eerdere versies van QGIS Server hadden problemen bij het renderen als SVG-bestanden op afstand werden gebruikt in een project (bijv. die welke werden gehost via externe http-servers). We hebben verbeterd hoe QGIS Server deze bronnen ophaalt, en het is nu mogelijk om SVG-paden op afstand in uw lagen te gebruiken en ze als WMS te publiceren zonder problemen bij het renderen in QGIS Server.

![image61](images/entries/71d731c71f864fcb542f2f7ec52c68e4c03068d3.webp)

Dit werd mogelijk gemaakt door [Ifremer](https://sextant.ifremer.fr/)

Deze mogelijkheid werd ontwikkeld door [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Mogelijkheid: WMS dimensie
In QGIS 3.10 kan een WMS-server ondersteuning bieden voor verscheidene typen dimensies, zoals tijd, hoogte of andere typen dimensies. De dimensie moet worden gedefinieerd als het niveau van de laag en kan worden gebruikt door de cliënt van WMS om gevraagde informatie te filteren. WMS Time is deel van de WMS Dimensie.

![image62](images/entries/45744c5a4a4c94e1c71a91bcfa7b672333002e75.webp)

Dit werd mogelijk gemaakt door [Ifremer](https://sextant.ifremer.fr/)

Deze mogelijkheid werd ontwikkeld door [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Mogelijkheid: Server OAPIF (alias WFS3) ondersteuning
QGIS 3.10 Server is een van de eerste georuimtelijke servers die de nieuwe [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) standaard ondersteunt (ook wel bekend als WFS3)!

Dit is een volledig nieuwe implementatie die een op HTML en JSON gebaseerde service verschaft voor uw ontwikkelingen voor webkaarten, inclusief een eenvoudige interface WebGIS die out of the box beschikbaar is en eenvoudig is aan te passen via een systeem met sjablonen in HTML.

Meer informatie is beschikbaar in de [documentatie](https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/services.html#wfs3-ogc-api-features)

![image63](images/entries/81af9beefcd8522ecc0f953b2a6b9b4895e35675.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.qcooperative.net)
## Programmeerbaarheid
### Mogelijkheid: Nieuwe klasse QgsBookmarkManager
Verbonden met QgsProject en QgsApplication verschaft deze nieuwe klasse een stabiele, ondersteunde methode voor het beheren van project en globale Favoriete plaatsen (vs de oude niet gedocumenteerde, niet stabiele benadering van het direct bewerken van projectsleutels of een database van SQLite). Nu zijn uw plug-ins en scripts in staat Favoriete plaatsen te lezen, aan te passen en te beheren!

Dit werd mogelijk gemaakt door [North Road](http://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](http://north-road.com)
### Mogelijkheid: Nieuwe API voor verbindingen naar database van providers
Dankzij de fondsen uit het programma van QGIS voor giften kunt u nu een [nieuwe API](https://github.com/qgis/QGIS/pull/31190) gebruiken, die tot doel heeft om verbindingen naar een DB op een uniforme manier te beheren. De nieuwe API voor verbindingen verschaft ook een set nuttige methoden die kunnen worden gebruikt door auteurs van plug-ins om toegang te krijgen tot informatie over tabellen, schema's etc. en om willekeurige query's van SQL uit te voeren en de resultaten terug te krijgen in een handige array voor Python.

Dit werd mogelijk gemaakt door QGIS 

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.qcooperative.net)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Crash when deleting print layout items | [#31549](https://github.com/qgis/QGIS/issues/31549) |  |  |
| DB manager python error | [#31457](https://github.com/qgis/QGIS/issues/31457) |  |  |
| QGIS 3.4.11: Clicking a PDF URL in GetFeatureInfo response generates error | [#31542](https://github.com/qgis/QGIS/issues/31542) | Al  gerepareerd (door mij) in 3.8 en Master |  |
| Watch file not adding new columns | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| Loss of labels background from older project/style | [#31427](https://github.com/qgis/QGIS/issues/31427) | [PR #3164](https://github.com/qgis/QGIS/pull/31647) |  |
| \"Text formats\" dialog shows modifiable buffer properties while the \"draw text buffer\" is unchecked | [#31428](https://github.com/qgis/QGIS/issues/31428) | [PR #3173](https://github.com/qgis/QGIS/pull/31734) |  |
| Symbology tab widget does not horizontally expand in the layer properties dialog extent | [#31449](https://github.com/qgis/QGIS/issues/31449) | [PR #3166](https://github.com/qgis/QGIS/pull/31665) |  |
| Watch file not adding new columns | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| Unreported but related to #31452 | [PR #3168](https://github.com/qgis/QGIS/pull/31688) |  |  |
| Unable to add WMS service in QGIS, same URL works in other clients | [#31661](https://github.com/qgis/QGIS/issues/31661) |  |  |
| QGIS Server - Download of capabilities failed: SSL handshake failed | [#31675](https://github.com/qgis/QGIS/issues/31675) |  |  |
| apparent regression in raster calculator multiplying conditionals | [#31193](https://github.com/qgis/QGIS/issues/31193) | [PR #3169](https://github.com/qgis/QGIS/pull/31690) |  |
| Broken GPKG browser actions | [#31730](https://github.com/qgis/QGIS/issues/31730) | [PR #3173](https://github.com/qgis/QGIS/pull/31731) |  |
| Resizing the data source manager dialog fails to resize unfocused panels | [#31732](https://github.com/qgis/QGIS/issues/31732) | [PR #3174](https://github.com/qgis/QGIS/pull/31741) |  |
| In place processing multipart to singleparts does not handle unique constraints | [#31634](https://github.com/qgis/QGIS/issues/31634) | [PR #3175](https://github.com/qgis/QGIS/pull/31750) | [PR #3181](https://github.com/qgis/QGIS/pull/31810) |
| crash when adding legend via python | [#31713](https://github.com/qgis/QGIS/issues/31713) |  |  |
| UI: Legend does not refresh after classifincation bounds updated | [#31643](https://github.com/qgis/QGIS/issues/31643) | Geen invloed | [PR #3183](https://github.com/qgis/QGIS/pull/31834) |
| UI: PostGIS layer error message not helpful, disappears and shouldn\'t happen | [#31799](https://github.com/qgis/QGIS/issues/31799) | [PR #3184](https://github.com/qgis/QGIS/pull/31841) |  |
| Server GetLegendGraphics contextual (BBOX) fails if no WIDTH and HEIGHT are supplied | [#31846](https://github.com/qgis/QGIS/issues/31846) | [PR #3186](https://github.com/qgis/QGIS/pull/31865) | [PR #3188](https://github.com/qgis/QGIS/pull/31882) |
| extend/trim crash | [#31864](https://github.com/qgis/QGIS/issues/31864) |  |  |
| UI: any click on number of classes updown triggers twice | [#31635](https://github.com/qgis/QGIS/issues/31635) | [PR #3187](https://github.com/qgis/QGIS/pull/31871) |  |
| GPKG project is not marked dirty after it is deleted from the storage | [#30550](https://github.com/qgis/QGIS/issues/30550) | [PR #3187](https://github.com/qgis/QGIS/pull/31876) |  |
| Fix unreported issue with QVariantList to JSON conversion in QgsJsonUtils | niet gerapporteerd | [PR #3192](https://github.com/qgis/QGIS/pull/31920) |  |
| Crash on adding WMS | [#31927](https://github.com/qgis/QGIS/issues/31927) | [#31927](https://github.com/qgis/QGIS/issues/31927) | [PR #3197](https://github.com/qgis/QGIS/pull/31979) |
| Raster calculator change sign does not work when OpenCL is on | [#32023](https://github.com/qgis/QGIS/issues/32023) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Snapping map units always show \"meters even when the project is in different units | [#31961](https://github.com/qgis/QGIS/issues/31961) | [PR #3201](https://github.com/qgis/QGIS/pull/32018) |  |
| QGIS Raster Calculator outputs nodata only rasters | [#32025](https://github.com/qgis/QGIS/issues/32025) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Opening projects from PostgreSQL issue | [#32050](https://github.com/qgis/QGIS/issues/32050) | [PR #3206](https://github.com/qgis/QGIS/pull/32062) |  |
| GetLegendGraphic shows all identical symbols for content based legend | [#32020](https://github.com/qgis/QGIS/issues/32020) |  |  |
| WFS doesn\'t recognize advertised GeoJSON outputFormat string | [#32065](https://github.com/qgis/QGIS/issues/32065) | [PR #3210](https://github.com/qgis/QGIS/pull/32106) |  |
| creating indexes on geopackage failes (QGIS 3.8.3) | [#32094](https://github.com/qgis/QGIS/issues/32094) |  |  |
| DB manager import option \"Create single-part geometries instead of multi-part\" is broken | [#32089](https://github.com/qgis/QGIS/issues/32089) | [PR #3210](https://github.com/qgis/QGIS/pull/32108) |  |
| GetLegendGraphic shows all identical symbols for content based legend | [#32020](https://github.com/qgis/QGIS/issues/32020) | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| WFS contextual legend issue when canvas CRS is different than layer\'s CRS | niet gerapporteerd | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| PostGIS/geojson: Cannot input negative numbers in int fields | [#32149](https://github.com/qgis/QGIS/issues/32149) | [PR #3216](https://github.com/qgis/QGIS/pull/32161) |  |
| Information tab in WMS layer properties is unresponsive if a WMS service contains many layers | [#32213](https://github.com/qgis/QGIS/issues/32213) | [PR #3226](https://github.com/qgis/QGIS/pull/32269) |  |
| Data Source UI - PostgreSQL table multi-line comments make the grid table hard to read | [#32257](https://github.com/qgis/QGIS/issues/32257) | [PR #3233](https://github.com/qgis/QGIS/pull/32336) |  |
| More null pointer dereferences when plugins are off | [#32347](https://github.com/qgis/QGIS/issues/32347) | [PR #3235](https://github.com/qgis/QGIS/pull/32351) |  |
| null pointer dereferences when plugins are off | [#32338](https://github.com/qgis/QGIS/issues/32338) | [PR #3234](https://github.com/qgis/QGIS/pull/32345) |  |
| \"Merge features\" and \"merge feature attributes\" have broken numerical functions | [PR #3236](https://github.com/qgis/QGIS/pull/32360) | [PR #3236](https://github.com/qgis/QGIS/pull/32360) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://www.itopen.it/)
### Mogelijkheid: Reparaties van problemen door Alexander Bruy
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| GDAL scripts in Processing need quoting on attribute names | [#30878](https://github.com/qgis/QGIS/issues/30878) | [PR #3171](https://github.com/qgis/QGIS/pull/31712) | [PR #3171](https://github.com/qgis/QGIS/pull/31717) |
| Processing GDAL algorithms does not handle correctly WFS input layers | [#29663](https://github.com/qgis/QGIS/issues/29663) | [PR #3173](https://github.com/qgis/QGIS/pull/31735) |  |
| shp files in zip files files cannot be used in Processing with 3rd party providers (SAGA, GRASS\...) | [#29001](https://github.com/qgis/QGIS/issues/29001) | [PR #3174](https://github.com/qgis/QGIS/pull/31744) | [PR #3178](https://github.com/qgis/QGIS/pull/31787) |
| Not possible to toggle use selected features in the Processing layer combobox | [#30636](https://github.com/qgis/QGIS/issues/30636) | [PR #3173](https://github.com/qgis/QGIS/pull/31739) |  |
| Connect to postgis database fails in \"Layer - Add Postgis layer\" on databases with weird table names | [#27040](https://github.com/qgis/QGIS/issues/27040) | [PR #3176](https://github.com/qgis/QGIS/pull/31763) |  |
| GRASS v.build.polylines dosn\'t work in Qgis 3.4.10 | [#31037](https://github.com/qgis/QGIS/issues/31037) |  |  |
| Processing Algorithms written with the \@alg decorator don\'t get the gear icon | [#31252](https://github.com/qgis/QGIS/issues/31252) | [PR #3188](https://github.com/qgis/QGIS/pull/31887) |  |
| v.drape - no 25D export with SpatiaLite format | [#30066](https://github.com/qgis/QGIS/issues/30066) |  |  |
| Service url cannot include custom query parameters | [#26761](https://github.com/qgis/QGIS/issues/26761) |  |  |
| Processing: python error on startup | [#29535](https://github.com/qgis/QGIS/issues/29535) |  |  |
| Saving Processing\'s Package Layers algorithm\'s output to default temporary output leaves no result | [#30535](https://github.com/qgis/QGIS/issues/30535) |  |  |
| \[Georeferencer\] GDAL script does not set target SR | [#31353](https://github.com/qgis/QGIS/issues/31353) | [PR #3189](https://github.com/qgis/QGIS/pull/31898) |  |
| Processing \"Build virtual vector\" now fails in certain cases | [#29336](https://github.com/qgis/QGIS/issues/29336) | [PR #3190](https://github.com/qgis/QGIS/pull/31901) |  |
| Unreported issue with missed import in the Processing algorithms dialog | niet gerapporteerd | [PR #3190](https://github.com/qgis/QGIS/pull/31902) |  |
| db manager: python error when clicking \"edit table\" if the table is a postgis raster | [#30214](https://github.com/qgis/QGIS/issues/30214) | [PR #3190](https://github.com/qgis/QGIS/pull/31904) |  |
| DB Manager: Renaming a PostGIS geometry column causes it to lose its geometry type and SRS | [#27613](https://github.com/qgis/QGIS/issues/27613) | [PR #3192](https://github.com/qgis/QGIS/pull/31929) |  |
| Georeferencer incorrectly shows last image when reopened | [#26700](https://github.com/qgis/QGIS/issues/26700) | [PR #3193](https://github.com/qgis/QGIS/pull/31932) |  |
| DB Manager: Create Layer dialog should be closed or cleared once the new layer is generated | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #3195](https://github.com/qgis/QGIS/pull/31956) |  |
| \[Vector Save As\...\] Extension is not replaced in filename when switching format | [#26054](https://github.com/qgis/QGIS/issues/26054) | [PR #3196](https://github.com/qgis/QGIS/pull/31960) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Alexander Bruy
### Mogelijkheid: Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Reproducible Crash: retrieving QgsHighlight instance stored as a widget property | [#30766](https://github.com/qgis/QGIS/issues/30766) | [PR #3173](https://github.com/qgis/QGIS/pull/31733) | [PR #3197](https://github.com/qgis/QGIS/pull/31977) |
| Layer styling Mesh layer does not respond to change of Color ramp (first time) | [#29188](https://github.com/qgis/QGIS/issues/29188) | [PR #3198](https://github.com/qgis/QGIS/pull/31981) |  |
| qgis crashed on close in QSortFilterProxyModel | [#31721](https://github.com/qgis/QGIS/issues/31721) |  |  |
| QGIS freezes | [#29742](https://github.com/qgis/QGIS/issues/29742) |  |  |
| Crash when trying to save a project | [#29896](https://github.com/qgis/QGIS/issues/29896) |  |  |
| Crash on exit with advanced digitizing active | [#29143](https://github.com/qgis/QGIS/issues/29143) |  |  |
| Renaming macOS app causes authentication error | [#32163](https://github.com/qgis/QGIS/issues/32163) |  |  |
| QGIS cannot be opened after updating to Mac OS Catalina | [#32167](https://github.com/qgis/QGIS/issues/32167) |  |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3176](https://github.com/qgis/QGIS/pull/31764) | [Commit 08bb3fe](https://github.com/qgis/QGIS/commit/08bb3fea3fc3f574755ecc0a7dc8381a9822e4cd) |
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3184](https://github.com/qgis/QGIS/pull/31848) | [PR #3185](https://github.com/qgis/QGIS/pull/31850) |
| QGIS WFS stripping of viewparam KVP from WFS Feature Requests | [#31026](https://github.com/qgis/QGIS/issues/31026) | [PR #3176](https://github.com/qgis/QGIS/pull/31765) | [PR #3188](https://github.com/qgis/QGIS/pull/31883) |
| Crash: right click on image -\>export -\>save as-\>\"save raster layer as\" | [#30937](https://github.com/qgis/QGIS/issues/30937) | [PR #3176](https://github.com/qgis/QGIS/pull/31766) | [PR #3178](https://github.com/qgis/QGIS/pull/31780) |
| crash in discover relations for postgresql layers | [#31213](https://github.com/qgis/QGIS/issues/31213) | [PR #3176](https://github.com/qgis/QGIS/pull/31768) | [PR #3177](https://github.com/qgis/QGIS/pull/31779) |
| Exporting raster as raw data to GeoPackage fails silently | [#30644](https://github.com/qgis/QGIS/issues/30644) | [PR #3177](https://github.com/qgis/QGIS/pull/31771) | [PR #3178](https://github.com/qgis/QGIS/pull/31781) |
| QGIS crashes after deactivating a GDAL driver in use in the project | [#29212](https://github.com/qgis/QGIS/issues/29212) | [PR #3177](https://github.com/qgis/QGIS/pull/31772) | [PR #3180](https://github.com/qgis/QGIS/pull/31802) |
| Crash exporting to GS7BG format | [#31775](https://github.com/qgis/QGIS/issues/31775) | [PR #3178](https://github.com/qgis/QGIS/pull/31785) | [PR #3183](https://github.com/qgis/QGIS/pull/31836) |
| pgdump is no longer a recognized format for the GDAL/OGR convert format algorithm | [#31421](https://github.com/qgis/QGIS/issues/31421) | [PR #3181](https://github.com/qgis/QGIS/pull/31811) | is het niet waard |
| PBF files not loading correctly | [#31062](https://github.com/qgis/QGIS/issues/31062) | [PR #3181](https://github.com/qgis/QGIS/pull/31812) | [PR #31835](https://github.com/qgis/QGIS/pull/31835) |
| Error importing cover from Geoserver WFS service | [#29844](https://github.com/qgis/QGIS/issues/29844) | [PR #31813](https://github.com/qgis/QGIS/pull/31813) | [PR #31867](https://github.com/qgis/QGIS/pull/31867) |
| Feature count from online Geojson not updated upon refresh | [#30518](https://github.com/qgis/QGIS/issues/30518) | [PR #31860](https://github.com/qgis/QGIS/pull/31860) | is het niet waard |
| Edits in GeoJson datasources are not saved anymore | [#28580](https://github.com/qgis/QGIS/issues/28580) | GDAL <https://github.com/OSGeo/gdal/pull/1846> | Gebackport naar GDAL 3.0 en 2.4 onderhoudstakken |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Adding Postgis rasters from DB Manager ask for password for each add | [#31162](https://github.com/qgis/QGIS/issues/31162) |  |  |
| \[processing\] segmentizebymaxdistance puts qgis in endless CPU loop | [#31832](https://github.com/qgis/QGIS/issues/31832) | [Commit 6942b4b9](https://github.com/qgis/QGIS/commit/6942b4b93d252bc3a031db08a34f378d8d3c726d) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) |
| file INSTALL cannot find doc/api/html | [#31842](https://github.com/qgis/QGIS/issues/31842) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) | Niet beschikbaar |
| QGIS died on signal 11 \# at start up | [#31350](https://github.com/qgis/QGIS/issues/31350) |  |  |
| repository files modified by `make check` | [#25830](https://github.com/qgis/QGIS/issues/25830) | [PR #31980](https://github.com/qgis/QGIS/pull/31980) |  |
| CMake Error at cmake/FindGEOS.cmake:162 | [#32170](https://github.com/qgis/QGIS/issues/32170) | [Commit bc9bb888](https://github.com/qgis/QGIS/commit/bc9bb8880a3db5a05c697f5d56708757a2ce999d) | [Commit 27f13936](https://github.com/qgis/QGIS/commit/27f13936afd970d766f398584a1ea509dc15b907) |
| False success from ogr provider\'s committChanges | [#32144](https://github.com/qgis/QGIS/issues/32144) | [Commit f421dc4f](https://github.com/qgis/QGIS/commit/f421dc4f92cfc019eec9823556d3c8f3e9589d95) | [Commit 136cec24](https://github.com/qgis/QGIS/commit/136cec244111748627c59db151002fddfc5f1708) |
| TestSagaAlgorithms: line 139, in check_algorithm: \'NoneType\' object has no attribute \'checkParameterValues\' | [#32143](https://github.com/qgis/QGIS/issues/32143) | [Commit 76b39de1](https://github.com/qgis/QGIS/commit/76b39de1b85375f48d7a5d35ebe39a52224d1809) | Niet beschikbaar |
| PostGIS Data Loads Extemely Slow | [#26186](https://github.com/qgis/QGIS/issues/26186) | [PR #31858](https://github.com/qgis/QGIS/pull/31858) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Sandro Santilli](http://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Matthias Kuhn
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Crash when opening symbology tab of invalid layer | [#32041](https://github.com/qgis/QGIS/issues/32041) | [#32041](https://github.com/qgis/QGIS/issues/32041) | Niet beschikbaar |
| PR reviews | Vele :D |  |  |
| qgz are marked as temporary on windows | [#32118](https://github.com/qgis/QGIS/issues/32118) |  |  |
| Allow selecting geometry type in context | [#32121](https://github.com/qgis/QGIS/issues/32121) | [PR #32125](https://github.com/qgis/QGIS/pull/32125) | Niet beschikbaar |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://opengis.ch/)
### Mogelijkheid: Reparaties van problemen door Paul Blottiere
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Fixes invalid schemaLocation in GetCapabilities doc | [#32085](https://github.com/qgis/QGIS/issues/32085) | [PR #32352](https://github.com/qgis/QGIS/pull/32352) |  |
| Invalid WMS GetFeatureInfo response with json info_format | [#32326](https://github.com/qgis/QGIS/issues/32326) | [PR #32386](https://github.com/qgis/QGIS/pull/32386)/files |  |
| QGIS Server SELECTION doesn\'t work with Postgres ids of type bigint or text | [#29779](https://github.com/qgis/QGIS/issues/29779) |  |  |
| Regression with opacities for the WMS GetPrint request | [#29317](https://github.com/qgis/QGIS/issues/29317) |  |  |
| Unreported regression: Invalid renderer type after loading a QML style file | niet gerapporteerde regressie | [PR #32388](https://github.com/qgis/QGIS/pull/32388) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door Paul Blottiere
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues  (indien gerapporteerd) | URL PR of commit | 3.4 backport PR of commit |
| --- | --- | --- | --- |
| Fix crash when deleting layouts from designer window | [#32465](https://github.com/qgis/QGIS/issues/32465) | [Commit e643e7f6](https://github.com/qgis/QGIS/commit/e643e7f6abe63aff123e07a0137afdda3987d4e6) | Niet beschikbaar |
| Fix model to python when model has no input parameters | [Commit 6f1c42e7](https://github.com/qgis/QGIS/commit/6f1c42e7bc9fa6ddfae3bbc1304ebeb53fe6a014) | Niet beschikbaar |  |
| Fix string escaping when converting models to python code | [#32451](https://github.com/qgis/QGIS/issues/32451) | [Commit e3eb4f54](https://github.com/qgis/QGIS/commit/e3eb4f54abdd8c6d4f4de443e3517775e9e565e1) | Niet beschikbaar |
| Fix memory leak | [Commit 5be31915](https://github.com/qgis/QGIS/commit/5be319157f112a2fdbab7f03d0010d69f1e79157) | Niet beschikbaar |  |
| Fix potential overflow in raster renderer | [Commit 1ba8db41](https://github.com/qgis/QGIS/commit/1ba8db41b67c7c481affd5271864cc2318ce06e4) | Niet beschikbaar |  |
| Restore project variables early in the project read cycle | [#32382](https://github.com/qgis/QGIS/issues/32382) | [Commit d76835fe](https://github.com/qgis/QGIS/commit/d76835fec5a9217a5ea1996374d142f7319f8d08) | Niet beschikbaar |
| Improve docs for Join by Nearest, raise warning in log | [#32317](https://github.com/qgis/QGIS/issues/32317) | [Commit 670c81f9](https://github.com/qgis/QGIS/commit/670c81f9212ada60f56c1c70ee9d37280052622c) | Niet beschikbaar |
| Catch some reprojection exceptions during raster rendering | [#32301](https://github.com/qgis/QGIS/issues/32301) | [Commit 1dfc0c1e](https://github.com/qgis/QGIS/commit/1dfc0c1e4eb8be26bb7214e3978aa6d80974c221) | Niet beschikbaar |
| \[labeling\] Fix broken numeric formatting settings, add tests | [#32393](https://github.com/qgis/QGIS/issues/32393) | [Commit b58dd674](https://github.com/qgis/QGIS/commit/b58dd6745fabf8bccd6dbeb684b37393d5953cb7) | Niet beschikbaar |
| Fix uncaught transform exception when determining AFS layer bounds | niet gerapporteerd | [Commit 857697dd](https://github.com/qgis/QGIS/commit/857697dd9919e80fc03e0c2059e56ce7311e9b49) | Niet beschikbaar |
| Fix qt warning thrown when converting a 2.18 project | niet gerapporteerd | [Commit 12ad9fca](https://github.com/qgis/QGIS/commit/12ad9fca1ed5027129161ee5b5c764b8374d0b51) | Niet beschikbaar |
| Add option to take no action (\"Leave as an unknown CRS\") when a layer is loaded which has no CRS | #19762, #27634, #24815 (en waarschijnlijk nog enkele andere) | [Commit ffe66bff](https://github.com/qgis/QGIS/commit/ffe66bff82be16dd90cd95f13331e5be7ca2c628) | Niet beschikbaar |
| Don\'t force fallback to WGS84 for unknown layer CRSes | niet gerapporteerd | [Commit 93741566](https://github.com/qgis/QGIS/commit/937415663f609fa7e41056aeb1176a0a145accc1) | Niet beschikbaar |
| Fix memory layers cannot use non-EPSG CRS codes | niet gerapporteerd, maar waarschijnlijk oorzaak voor veel problemen | [Commit 2dad68f7](https://github.com/qgis/QGIS/commit/2dad68f76396a419b25fa8dad2b7b16552086740) | Niet beschikbaar |
| Fix crash after deleting report sections | [#31302](https://github.com/qgis/QGIS/issues/31302) | [Commit 3356460c](https://github.com/qgis/QGIS/commit/3356460ce70af15105880d135271595dccfc397c) | [Commit d3230ac0](https://github.com/qgis/QGIS/commit/d3230ac0c545604a97fa3028ca3e846bff65004c) |
| Ensure polygon rings generated for rendering are always closed | niet gerapporteerd | [Commit a69e38d9](https://github.com/qgis/QGIS/commit/a69e38d9c358faea5ae4a8628add1e6721cc23e8) | Niet beschikbaar |
| Don\'t crash QgsTessellator when an empty polygon is added | niet gerapporteerd | [Commit 761b2e77](https://github.com/qgis/QGIS/commit/761b2e778594f4051a72d02b898354f501e336fe) | Niet beschikbaar |
| Fix crash in topology checker plugin after a check is canceled | niet gerapporteerd | [Commit 606bcd35](https://github.com/qgis/QGIS/commit/606bcd35143d09cca5b1ec45bdb5b13236e4376b) | Niet beschikbaar |
| Fix topology checker multipart check | [#28361](https://github.com/qgis/QGIS/issues/28361) | [Commit 5101386b](https://github.com/qgis/QGIS/commit/5101386b37fb4d180d32d31663404e3bcc647cec) | Niet beschikbaar |
| Fix crash on exit when topology checker dock is open with visible results | niet gerapporteerd | [Commit 64375ad4](https://github.com/qgis/QGIS/commit/64375ad4d28597eb97808f64e1481915df7a676c) | Niet beschikbaar |
| Don\'t load print layouts when opening project browser items | via e-mail | [Commit 9f1ce084](https://github.com/qgis/QGIS/commit/9f1ce08418db9545ed18d6711c472833f9889e1d) | Niet beschikbaar |
| Add QgsProject flag to avoid loading print layouts when reading a project file, avoids crashes when project is loaded in background thread | via e-mail | [Commit d0ed3746](https://github.com/qgis/QGIS/commit/d0ed3746629ae9c9349fe2e9c75550679120026d) | Niet beschikbaar |
| Don\'t try to load HTML content when a layout is created in a background thread | via e-mail | [Commit 53252496](https://github.com/qgis/QGIS/commit/532524961c0880b33e1d7ed4a3ce0805d7f0bc71) | [Commit 5fcab0e7](https://github.com/qgis/QGIS/commit/5fcab0e713a1e9ffde8b049f620d4a5cd6a81ff3) |
| Huge speed up to QgsTessellator | [Commit 577e1e96](https://github.com/qgis/QGIS/commit/577e1e962d4004f9cd11a169860e0b099216c963) | Niet beschikbaar |  |
| \[processing\] Ensure all objects used by the model are correctly imported | [#32004](https://github.com/qgis/QGIS/issues/32004) | [Commit e5e3fe47](https://github.com/qgis/QGIS/commit/e5e3fe473e8e6764f528b4a40095a7a047e9c357) | Niet beschikbaar |
| \[processing\] Avoid confusing use of expression parameter type in Random Points in Polygon algorithm | [#27640](https://github.com/qgis/QGIS/issues/27640) | [Commit 196e15a0](https://github.com/qgis/QGIS/commit/196e15a0ff974622bfa1e7dfdeb9fe8567a7f3b7) | Niet beschikbaar |
| \[layouts\] Update map settings variables in UI when map extent/rotation changes | [#24136](https://github.com/qgis/QGIS/issues/24136) | [Commit 86c83537](https://github.com/qgis/QGIS/commit/86c83537f9b03816ba5b8f90c8cf8a2820077441) | Niet beschikbaar |
| \[layouts\] Fix layout variables set programmatically do not show in GUI | [#28837](https://github.com/qgis/QGIS/issues/28837) | [Commit 1afdd935](https://github.com/qgis/QGIS/commit/1afdd935cf84cbd702093935a676672d1e349da1) | Niet beschikbaar |
| \[layouts\] Ensure variable panels are updated when layout or atlas properties change | [#26402](https://github.com/qgis/QGIS/issues/26402) | [Commit 2b31e03a](https://github.com/qgis/QGIS/commit/2b31e03ad0659500a733d71c10c54e17e6817c10) | Niet beschikbaar |
| \[layouts\] Move page background setting to a per-page option | [#25695](https://github.com/qgis/QGIS/issues/25695) | [Commit 45e847ef](https://github.com/qgis/QGIS/commit/45e847ef69b56b4c12774363e20a7a05f49e8618) | Niet beschikbaar |
| Optimize QgsContrastEnhancementFunction | [Commit f5c21a0f](https://github.com/qgis/QGIS/commit/f5c21a0fbd72fe840900e0ad35c4af285fbd8a79) | Niet beschikbaar |  |
| \[layouts\] Prevent removal of the last remaining page in a layout | via e-mail | [Commit e6ecfdd3](https://github.com/qgis/QGIS/commit/e6ecfdd39bc2ae842c437700508899a9e1aa9dcd) | [Commit b65f23f8](https://github.com/qgis/QGIS/commit/b65f23f86b4630b4b5157400a713c36081bd56b9) |
| \[layouts\] Fix crash when exporting layout with no pages | via e-mail | [Commit b784d698](https://github.com/qgis/QGIS/commit/b784d6982826039bd9fa35b7ecd1a362e29c0b04) | [Commit f8355cbb](https://github.com/qgis/QGIS/commit/f8355cbbbe4bdbbae9c3f1b135ed59bbc51226a2) |
| Fix conditional formatting panel high dpi issues | [Commit 1f033fe8](https://github.com/qgis/QGIS/commit/1f033fe83d63a2edb6ddc2b6d90169e3b814764e) | Niet beschikbaar |  |
| Fix loss of font setting when editing conditional format | [Commit 72efc1ed](https://github.com/qgis/QGIS/commit/72efc1edde693800b6604e8ec3afcc892ea5239e) | Niet beschikbaar |  |
| Avoid overflow in QgsImageOperation | [Commit aefbf662](https://github.com/qgis/QGIS/commit/aefbf6627256637cf455b2df409b3a4bf8171b33) | [Commit 9f4d3a87](https://github.com/qgis/QGIS/commit/9f4d3a8745b2d89faeb6a9272369eaa772e3638c) |  |
| \[processing\] Extend api for retrieving a layer in a compatible format | via 3e partij plug-in bugtracker | [Commit 651c5071](https://github.com/qgis/QGIS/commit/651c5071806d6f4f4dafc800e6b0d67f043a9ef0) | Niet beschikbaar |
| Fix conditional styles in feature list view do not update when the layer\'s conditional styles are changed | [Commit bccd5a46](https://github.com/qgis/QGIS/commit/bccd5a46106d7c5a63b3bd8c64ad1491a60205af) | Niet beschikbaar |  |
| Fix broken display of conditional styles in feature list view | [Commit 5f7264d4](https://github.com/qgis/QGIS/commit/5f7264d4d18d6894c4d33017439dc517a932fd75) | Niet beschikbaar |  |
| Fix incorrect conditional styling applied to rows in some cases | [Commit c15c7271](https://github.com/qgis/QGIS/commit/c15c72718909f4bce2d172b819c74ec7d8d4d9b3) | Niet beschikbaar |  |
| Use invalid colors, not transparent colors, to indict not set colors in conditional formats, fixes incorrect colors used for conditionally styled rows | [Commit bc82cffd](https://github.com/qgis/QGIS/commit/bc82cffd85342d92435600547c220eb1eaf90257) | Niet beschikbaar |  |
| \"\[labeling\] When an extreme number of features are being labeled from a single layer, place additional limits on the maximum number of |  |  |  |
| labeling candidates to generate for features in this layer\" | [Commit 61bfced6](https://github.com/qgis/QGIS/commit/61bfced6a7ae109bc97a0924eae108c0e51916d5) | Niet beschikbaar |  |
| \[layouts\] Fix incorrect alignment of items when the align or distribute tools are used with items with a non-top-left reference point | [#31900](https://github.com/qgis/QGIS/issues/31900) | [Commit b4550dc4](https://github.com/qgis/QGIS/commit/b4550dc4c06eec23ace4cbc5c6f1f8b23c8ee14f) | Niet beschikbaar |
| \[processing\] Respect user set default vector output format in vector split algorithm | [Commit 90bac82f](https://github.com/qgis/QGIS/commit/90bac82f124ccb53e43bb99f5d483105bea1c967) | Niet beschikbaar |  |
| Fix GUI is not updated when layout atlas is set to use the default filename expression | [#20786](https://github.com/qgis/QGIS/issues/20786) | [Commit a4da849e](https://github.com/qgis/QGIS/commit/a4da849e9d190ece1b748303cc8f68333f1e0e78) | Niet beschikbaar |
| \[reports\] Remove useless extra set of export actions | [#26384](https://github.com/qgis/QGIS/issues/26384) | [Commit d6b41813](https://github.com/qgis/QGIS/commit/d6b4181349a274e8d34196a340f4b806403af06b) | Niet beschikbaar |
| \[reports\] Fix crash when print button clicked before a report section is opened | niet gerapporteerd | [Commit c93fd0a4](https://github.com/qgis/QGIS/commit/c93fd0a4350ea14db9728ad17ada06e70eb9ffd6) | Niet beschikbaar |
| \[reports\] Reduce minimum width of report organiser dock | [#25916](https://github.com/qgis/QGIS/issues/25916) | [Commit 7c490848](https://github.com/qgis/QGIS/commit/7c4908481269f38e1b96c730542d5299903963fb) | Niet beschikbaar |
| \[layouts\] Add a page number selection combo box at the top of the guide manager dock | [#25700](https://github.com/qgis/QGIS/issues/25700) | [Commit 2f22aeaf](https://github.com/qgis/QGIS/commit/2f22aeaf276785867ed850f54c691a0a5b7c0aeb) | Niet beschikbaar |
| Show color button style \"Pick color\" and \"Chooe Color\" and symbol button menu | [#25696](https://github.com/qgis/QGIS/issues/25696) | [Commit 39cfd0f9](https://github.com/qgis/QGIS/commit/39cfd0f935bb8c6669237bc7abe6ca89c6a82a32) | Niet beschikbaar |
| Fix out of sync layout bounds after page removal | [#26665](https://github.com/qgis/QGIS/issues/26665) | [Commit d498eed0](https://github.com/qgis/QGIS/commit/d498eed0a5caf01b914a2c25f0c1d255d955b4a9) | Niet beschikbaar |
| \[layouts\] Fix odd selection behavior when keyboard modifiers are pressed when rectangular selection ends | [Commit 37b5af54](https://github.com/qgis/QGIS/commit/37b5af54d9423563d17422f5b90d6a7dbdfe0299) | Niet beschikbaar |  |
| Fix interaction with group members in items panel | [#26674](https://github.com/qgis/QGIS/issues/26674) | [Commit 5154240f](https://github.com/qgis/QGIS/commit/5154240fa94401952329138300dd2035e5519d5e) | Niet beschikbaar |
| \[layout\] Fix invalid svg exports when including metadata | [#28130](https://github.com/qgis/QGIS/issues/28130) | [Commit cc94aebc](https://github.com/qgis/QGIS/commit/cc94aebc6fa2e53adc99902b7f7ac4f87e0361db) | Niet beschikbaar |
| \[legends\] Fix missing symbols for inverted polygon layers when using filter by map content | [#22718](https://github.com/qgis/QGIS/issues/22718) | [Commit abc9f47c](https://github.com/qgis/QGIS/commit/abc9f47ca471540c9b0f9dd6159d3ac7f9791a3c) | Niet beschikbaar |
| Use a slightly larger font size in CRS details on Windows | [#31297](https://github.com/qgis/QGIS/issues/31297) | [Commit 757017c2](https://github.com/qgis/QGIS/commit/757017c2c29a0ea4b72527e4cd98e700c720022c) | Niet beschikbaar |
| \[processing\] Add warning when packaging a geopackage with no layers | [#31888](https://github.com/qgis/QGIS/issues/31888) | [Commit f11e6603](https://github.com/qgis/QGIS/commit/f11e6603957f69a34ad7aa9893aa144cc5020ca4) | Niet beschikbaar |
| \[layouts\] Fix crash when opening layout with dynamic image in html label | [#28996](https://github.com/qgis/QGIS/issues/28996) | [Commit 5db6165f](https://github.com/qgis/QGIS/commit/5db6165fb597c2db278e678953578992789fa38b) | [Commit e29865cd](https://github.com/qgis/QGIS/commit/e29865cd485c3576db27aab4cad86614f3eff2f3) |
| Expose report feature settings when an attribute table is used in an atlas | [#28441](https://github.com/qgis/QGIS/issues/28441) | [Commit 9fd17c8f](https://github.com/qgis/QGIS/commit/9fd17c8f3cce8fb5864db137da71c3cb61b44510) | Niet beschikbaar |
| \[layouts\] Fix attribute table ignores cell margin for top/bottom aligned text | [#31259](https://github.com/qgis/QGIS/issues/31259) | [Commit 7b356fe4](https://github.com/qgis/QGIS/commit/7b356fe4cde1b030ddfb589a22cb59229311074e) | Niet beschikbaar |
| Fix truncated legend symbol borders when layer has opacity set | [Commit 30e14938](https://github.com/qgis/QGIS/commit/30e149387bcccbd14f057a16cb27729c57c9a210) | Niet beschikbaar |  |
| Fix adding/moving legend is very slow with large projects | [#29058](https://github.com/qgis/QGIS/issues/29058) | [Commit 758ac909](https://github.com/qgis/QGIS/commit/758ac9092f9fac3f7533766f329f17832b2dcd35) | Niet beschikbaar |
| \[reports\] Fix predefined scale mode is incompatible with report outputs | [#29196](https://github.com/qgis/QGIS/issues/29196) | [Commit fcd21e48](https://github.com/qgis/QGIS/commit/fcd21e485068d8082bdef0a5a7393b57fe5bf3c1) | Niet beschikbaar |
| Ensure atlas expression evaluation has access to coverage layer scope | [#31807](https://github.com/qgis/QGIS/issues/31807) | [Commit 3de05939](https://github.com/qgis/QGIS/commit/3de059395706a225ca137b3d4a7a34b27d3cc9ae) | Niet beschikbaar |
| Resizing pages to content should not create empty page size if no items are present | [#29034](https://github.com/qgis/QGIS/issues/29034) | [Commit 421e68cf](https://github.com/qgis/QGIS/commit/421e68cf5ae5637001765842e257caf6becdb876) | Niet beschikbaar |
| Fix map rotation does not immediately restore in reports | [#31217](https://github.com/qgis/QGIS/issues/31217) | [Commit f5afebe5](https://github.com/qgis/QGIS/commit/f5afebe5dd0228ceb612a9823a80c77ccd51a1e6) | Niet beschikbaar |
| Do not return nan values when an assistant is used with min val == max val | [#31242](https://github.com/qgis/QGIS/issues/31242) | [Commit 97923751](https://github.com/qgis/QGIS/commit/979237515ce2921b9552a99eda071e9e9a14297a) | Niet beschikbaar |
| \[layouts\] Fix label items don\'t update when their opacity \< 100 | [#29079](https://github.com/qgis/QGIS/issues/29079) | [Commit f9a47738](https://github.com/qgis/QGIS/commit/f9a47738aaaec7504f912b2442195662a216b9e3) | Niet beschikbaar |
| Fix project load status indicator can get \"stuck\" after project load | niet gerapporteerd | [Commit 40d95b69](https://github.com/qgis/QGIS/commit/40d95b69d91ade71473f5ea0182040d8398cc668) | Niet beschikbaar |
| Fix corrupted expressions in filter indicator tooltips | [Commit 393e623b](https://github.com/qgis/QGIS/commit/393e623ba7d278eabc4f09aeaabb92f56fa269c9) | [Commit 8e0e368f](https://github.com/qgis/QGIS/commit/8e0e368f255ba10c530afd445ecd1ab53bf266bb) |  |
| Fix cannot use GPS panel to draw features in multi polygon/line | [#29144](https://github.com/qgis/QGIS/issues/29144) | [Commit dc2b209d](https://github.com/qgis/QGIS/commit/dc2b209da3609a47b1457c0cb12417afbcb36344) | Niet beschikbaar |
| Fix loss of label background settings when restoring projects. | [#31427](https://github.com/qgis/QGIS/issues/31427) | [Commit aa4a8da3](https://github.com/qgis/QGIS/commit/aa4a8da3a713b6961fccce019c5e9b5778f68b23) | Niet beschikbaar |
| Fix crash in point displacement renderer | [Commit 7043933f](https://github.com/qgis/QGIS/commit/7043933ff2bed42df5ae3439867330e39fe60f53) | Niet beschikbaar |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
