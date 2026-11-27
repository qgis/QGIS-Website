---
HasBanner: false
draft: false
releaseDate: '2026-11-20'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 4.4
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 4.4{#changelog44 }
<img src="images/projects/7a3290539a5412956dd2a6f0a0775190abf5fabe.png" class="img-responsive img-rounded center-block" />

Datum uitgave: 20-11-2026

[QGIS](https://qgis.org) (<https://qgis.org>) is het populairste (open bron) desktop Geografisch InformatieSysteem (GIS) ter wereld. Het wordt gebruikt door mensen over de gehele wereld om ruimtelijke gegevens te bekijken, te bewerken, te analyseren en te delen. Het kan professioneel ogende cartografieproducten produceren en ondersteunt honderden indelingen voor ruimtelijke gegevens. QGIS is een lidproject van OSGEO, de Open Source Geospatial Foundation, die toegang tot ruimtelijke platforms democratiseert (<https://osgeo.org>).

We zijn blij om de nieuwe belangrijke uitgave van QGIS 4.4 aan te kondigen, die doorbouwt op de solide fundering van de update van de belangrijke versie 4.0 die de bron van QGIS overbracht naar het moderne raamwerk van Qt6. Deze uitgave is de kandidaat voor de Lange Termijn Uitgave (LTR) - de uiteindelijke LTR uitgave zal plaatsvinden na 4 ronden van problemen oplossen om deze uitgave te stabiliseren en gereed te maken voor nog een jaar stabiele ondersteuning door de gemeenschap van QGIS.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u deze mogelijkheden bekijken [in de video met hoogtepunten op YouTube](https://www.youtube.com/watch?v=_bGc5CPNpNs).

<div class="tile video mb-3">
  <div class="youtube" data-video-id="_bGc5CPNpNs" style="background-image: url(&quot;https://img.youtube.com/vi/_bGc5CPNpNs/maxresdefault.jpg&quot;);">
    <iframe width="100%" height="100%" src="https://www.youtube.com/embed/_bGc5CPNpNs?autoplay=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="true"></iframe>
  </div>
</div>

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten!

Als u tijd of geld wilt doneren of op een andere manier wilt bijdragen aan het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een gemeend bedankt voor al onze sponsoren!

{{<fund type="active" level="flagship" >}}

[Klik hier om al onze dragende leden te bekijken]({{< ref "/funding/membership/members.md" >}})

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<changelog-filter >}}

{{<changelog-category-start id="category-documentation" >}}
## Documentatie
{{<rich-box-start layoutClass="rounded" id="documentation-1" githubLink="https://github.com/qgis/QGIS/pull/67791" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Voeg een knop Help toe aan de attributentabel
De attributentabel heeft nu een knop voor context-Help!<br /><img src="https://github.com/user-attachments/assets/bb85b8c7-c68c-45b1-b88e-a4dd5d198c50" width="649" height="51" alt="Image" />

Dit werd mogelijk gemaakt door [Nelen & Schuurmans](https://www.nelen-schuurmans.nl)

Deze mogelijkheid werd ontwikkeld door [Ben](https://github.com/benvanbasten-ns)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-user-interface" >}}
## Gebruikersinterface
{{<rich-box-start layoutClass="rounded" id="user-interface-1" githubLink="https://github.com/qgis/QGIS/pull/67745" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ontkoppel de zichtbaarheid van de welkomstpagina bij het opstarten van de afhandeling van het project bij opstarten
De zichtbaarheid van de welkomstpagina bij het opstarten van de toepassing is nu onafhankelijk van het sjabloon en herlaadt de laatste acties voor het opstarten van het project.<br /><img src="https://github.com/user-attachments/assets/d54b052c-ac49-4616-88fd-6e695489628e" width="1048" height="1012" alt="image" /><br />Opties voor het beheren hiervan staan in het dialoogvenster Instellingen.<br /><img src="https://github.com/user-attachments/assets/7cf56256-688c-4777-b18b-cc069328a4bb" width="1876" height="1470" alt="image" />

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-symbology" >}}
## Symbologie
{{<rich-box-start layoutClass="rounded" id="symbology-1" githubLink="https://github.com/qgis/QGIS/pull/67477" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Optie "Ondoorzichtig vullen" in menu Kleur
Voor deze wijziging stond de optie "transparant vullen" altijd aan, zelfs als de vulkleur al transparant was. Met dit PR, als de kleur 100% transparant is, wordt een nieuwe optie in plaats daarvan geplaatst: "ondoorzichtig vullen". Dit maakt het snel in-/uitschakelen mogelijk, wat meer intuïtief is.<br /><img src="https://github.com/user-attachments/assets/67a25f27-b1f2-4333-bf90-b56b1dcea659" width="437" height="305" alt="image" /><br /><img src="https://github.com/user-attachments/assets/83fbea68-bbe1-42b4-8894-d036e9a33a09" width="437" height="305" alt="image" />

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="symbology-2" githubLink="https://github.com/qgis/QGIS/pull/67099" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Keuzevakken toegevoegd om snel een symboollaag in of uit te schakelen
Voegt een keuzevak toe naast de symboollaag om die snel in of uit te schakelen, in plaats van omlaag te moeten scrollen om hem uit te schakelen.

<img src="images/entries/838842d893a18c4bbdd5a5720e613c013a3800e1.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/fr/)

Deze mogelijkheid werd ontwikkeld door [Celia Buira](https://github.com/CeliaBuira)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-annotations" >}}
## Annotaties
{{<rich-box-start layoutClass="rounded" id="annotations-1" githubLink="https://github.com/qgis/QGIS/pull/67101" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Annotatie draaien (deel 3): rotatiebewuste kaartgereedschappen
Maakt de kaartgereedschappen voor annotaties bewust van het draaien van items, wat het werk voltooid dat werd afgesplitst<br />van \#66610 (na \#67035 en \#67036).<br />`QgsMapToolSelectAnnotation` tekent de geselecteerde band en de muishandvatten ervan<br />samen gedraaid met het, en `QgsMapToolModifyAnnotation` plaatst de<br />hoekhandvatten op de gedraaide hoeken en ondersteunt het aanpassen van de grootte van een item door<br />aan een ervan te slepen. Het slepen houdt de tegenoverliggende hoek gefixeerd op het scherm en<br />reconstrueert de nieuwe (op as uitgelijnde) begrenzingen voor het item vanuit de niet-gedraaide diagonaal.<br />Toepassen van het zo aanpassen van de grootte kan door `QgsAnnotationItemEditOperationSetItemBounds`<br />de toegevoegde bewerking, omdat de bestaande bewerking `MoveNode` alleen kan worden ingesteld op<br />een enkele hoek van de niet-gedraaide begrenzingen, wat niet is wat een gedraaide aanpassing van de grootte<br />produceert.<br />Testen zijn toegevoegd voor het verplaatsen van een item op een gedraaid kaartvenster, draaien van een item en<br />grootte aanpassen van een gedraaid item.

<img src="images/entries/f32b672f11cfcedd9397c1ebf0e4a8068055277f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="annotations-2" githubLink="https://github.com/qgis/QGIS/pull/66713" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ondersteuning voor tekst uitlijnen op itemtypes lijnannotatie
Maakt het plaatsen van tekst mogelijk aan het einde of midden van de lijn voor het itemtype "tekst langs lijn"-annotatie.

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-labelling" >}}
## Labelen
{{<rich-box-start layoutClass="rounded" id="labelling-1" githubLink="https://github.com/qgis/QGIS/pull/67437" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Labels renderen voor geselecteerde objecten in een zichtbare staat
Bij het renderen van labels in een geselecteerde staat, renderen we ze met een buffer in de selectiekleur van de laag. Dat maakt onmiddellijk duidelijk wanneer een label tot een geselecteerd object behoort.<br />Dat is met name nuttig als een laag is ingesteld om alleen labels weer te geven, met de null-symboolrenderer.

<img src="images/entries/bb5336507508e5e07f88a246c1f33682a7b02a34.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door LINZ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="labelling-2" githubLink="https://github.com/qgis/QGIS/pull/66815" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ondersteuning voor draaien voor horizontale labels voor lijnen
Maakt het mogelijk de draaihoek in te stellen voor labels indien ingesteld op de modus voor plaatsing "horizontaal" voor lijnen.

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-rendering" >}}
## Renderen
{{<rich-box-start layoutClass="rounded" id="rendering-1" githubLink="https://github.com/qgis/QGIS/pull/67112" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Verbeteringen hoogtebeheer
Dit maakt de hoogtefilterwidget te gebruiken zonder de projecteigenschappen te openen:<br />het hoogtebereik kan direct in de widget worden ingesteld, het wordt vanuit de lagen gevuld als<br />het project er niet een definieert, en de waarden die het weergeeft zijn ronde getallen.<br /><img src="https://github.com/user-attachments/assets/f0bddbe5-8574-45b1-a803-b0df8d989e1f" width="926" height="665" alt="image" /><br />**Menu Instellingen**<br /><img src="https://github.com/user-attachments/assets/8a75ee0a-6a30-4060-87c7-b14f78a10727" width="695" height="112" alt="image" /><br />Het menu Instellingen van Hoogtebeheer is nu een enkel paneel, soortgelijk aan<br />Tijdbeheer:
- **Limieten**: net als voor Tijdbeheer maakt een knop het mogelijk de limieten te definiëren vanuit alle projectlagen of vanuit de huidige laag.
- **Bereik**: de waarde wordt nu zelfs weergegeven als die niet vergrendeld is, een knop voor vergrendelen wordt gebruikt (of door te drukken op Enter)
- **Richting omdraaien**.

Het item *Hoogtefilter uitschakelen* blijft.<br />**Afgeronde waarden**
- Limieten die vanuit lagen worden berekend, worden afgerond: `1234.5 - 3456.7` wordt `1200 - 3500`.
- De schuifbalk snapt aan ronde waarden bij slepen, dus een schuifbalk van 0 - 1000 verplaatst in stappen van 10.
- De schuifbalk snapt ook aan de hoogten die significant voor de lagen van de kaart zijn als een van hen dichter bij is dan de afgeronde waarde, dus een handvat kan nog steeds exact geplaatst worden op het oppervlak van een laag.

**Beginwaarden**<br />Wanneer het project nog geen eigen hoogtebereik heeft, begint het beheer met het bereik<br />dat werd berekend uit de lagen van het kaartvenster, in plaats van met de willekeurige standaard 0 - 100.<br />Het hoogtebereik van een rasterlaag wordt nu berekend uit de bandstatistieken van zijn<br />hoogteoppervlak, dus rasterlagen dragen een echt bereik bij, in plaats van niets.<br />**Gerepareerd**
- Enkele vreemde waarden in de schuifbalk als de limieten waren ingesteld nadat een bereik werd vergrendeld.
- Lagen in het kaartvenster zonder eigenschappen voor hoogte worden genegeerd; dit verwijdert waarschuwingen in de berichtenbalk

**API**
- `QgsMathUtils::roundingInterval()` geeft een afgeronde interval terug die een waarde splitst in een bereik met een opgegeven aantal delen
- `QgsMathUtils::roundedRange()` vergroot een bereik tot afgeronde waarden.
- `QgsElevationUtils::calculateZRangeForLayers()` berekent het hoogtebereik uit een lijst met lagen
- `QgsElevationControllerWidget::setMapCanvas()` geeft de widget het kaartvenster waartoe het behoort. Het verschaft de laag voor het item "Huidige laag", en de lagen ervan geven de initiële limieten als het project geen hoogtebereik heeft.
- `QgsElevationControllerSettingsAction` is nu SIP_SKIP (maar het was binnen @cond PRIVATE)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="rendering-2" githubLink="https://github.com/qgis/QGIS/pull/67486" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Renderer vectorveld voor rasterlagen
Nu de code voor vectorrenderen van mazen is losgekoppeld van lagen met mazen, kunnen we eindelijk `QgsRasterVectorFieldRenderer` introduceren, een rasterrenderer die pijlen, stroomlijnen, sporen en windvanen kan tekenen, net zoals zijn tegenhanger laag met mazen!<br />Er zijn twee belangrijke modi voor het maken van vectors uit rastergegevens:<br />**1. Gebruik twee afzonderlijke banden voor componenten X en Y van vectors**<br /><img src="https://github.com/user-attachments/assets/88cc24cf-3791-4515-9fa0-ea343c9b1a05" height="200" alt="image" /><br />**2. Gebruik een enkele band met integer gecodeerde kardinale richtingen**<br />(bekijk https://github.com/qgis/QGIS/issues/67108#issuecomment-5340069908)<br />Waarden die niet overeenkomen met het coderingsschema worden genegeerd.<br /><img src="https://github.com/user-attachments/assets/5706df59-1070-49d2-9483-b7db53935a95" height="200" alt="image" /><br />Als eenmaal een modus en de vereiste banden zijn geselecteerd, wordt de rest van de gebruikersinterface gedeeld tussen de renderer Raster en Mazen.<br />**Voorbeelden:**<br />**Pijlen**<br /><img src="https://github.com/user-attachments/assets/26f9a85d-d7b4-4f1d-9a65-b4fedd230636" height="200" alt="image" /><br />**Windvanen**<br /><img src="https://github.com/user-attachments/assets/881b7a94-cd8d-40fc-b8b5-f3f26ae0d99e" height="200" alt="image" /><br />**Sporen**<br /><img src="https://github.com/user-attachments/assets/13145387-2d88-4961-9b66-cc962843cb98" height="200" alt="image" />

Dit werd mogelijk gemaakt door [Hans van der Kwast en een crowdfunding-campagne](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-3d-features" >}}
## 3D-objecten
{{<rich-box-start layoutClass="rounded" id="3d-features-1" githubLink="https://github.com/qgis/QGIS/pull/66583" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Enkele kleur toegevoegd, niet verlichten type materiaal
Dit materiaal interacteert niet met verlichting in de scène, wat resulteert in een vlakke render in een enkele kleur

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-2" githubLink="https://github.com/qgis/QGIS/pull/67135" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ondersteuning voor items afbeeldingsannotatie in 3D toegevoegd
We hebben de bestaande ondersteuning voor het weergeven van markeringen en tekstannotaties als 3D-billboards uitgebreid. Nu kunt u items van afbeeldingsannotaties ook weergeven als 3D-billboards.<br />Er is een optie om deze weer te geven als ofwel onafhankelijk van de weergave, billboards met vaste grootte (net zoals markeringen en tekst), of als perspectiefcorrecte afmetingen (bijv. zoals elk ander 3D-item waarop u in of uit kunt zoomen).<br />De grootten van de 3D-billboards worden handmatig ingesteld, wat het mogelijk maakt dat de grootte wordt ingesteld op een die passend is voor de 3D-kaart (tegengesteld aan het strikt volgen van de grootte voor 2D)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-3" githubLink="https://github.com/qgis/QGIS/pull/66981" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### 3D-symbologiewidgets: vereenvoudigd hoofdpaneel en introduceren van een geavanceerd paneel
Dit implementeert de ideeën die werden besproken in [PR 66112](https://github.com/qgis/QGIS/pull/66112):<br />De oude 3D-symbologiewidgets hadden te veel informatie en parameters. We hebben het aantal weergegeven opties verminderd en ze verplaatst naar de tab Geavanceerd. Dat werd bereikt met 3 belangrijke wijzigingen:
- de parameters voor 3D-symbologie hebben nu een knop en menu Geavanceerd om te wisselen naar de geavanceerde instellingen
- parameters voor materiaal: we geven standaard minder parameters weer in een nieuwe "compacte" stijl en geven alleen alle parameters weer op de tab Geavanceerd. Dat geldt voor lijnen, punten en polygonen.

**Puntenwidget**<br /><img src="https://github.com/user-attachments/assets/14f32b39-8b3a-4c89-b127-503d35e9af92" height="200" alt="points" /><br />**Lijnewidget**<br /><img src="https://github.com/user-attachments/assets/56703ca4-e776-4af2-bab5-ad6a9d19e5c3" height="200" alt="line" /><br />**Polygonenwidget**<br /><img src="https://github.com/user-attachments/assets/8bc76d99-074c-4d08-a843-a18bff5ab2ff" height="200" alt="polygon" /><br />**paneel Geavanceerd materiaal**<br /><img src="https://github.com/user-attachments/assets/5725c506-d63e-4398-86ab-164bf3244905" height="200" alt="polygon-advanced" /><br />**Materialen**<br />**Gooch**<br /><img src="https://github.com/user-attachments/assets/9a9581f6-343f-487f-9800-75dce65fae4f" height="200" alt="gooch" /><br />**Metaal**<br /><img src="https://github.com/user-attachments/assets/dde662b5-2bae-4c02-b9fa-7cd0e0ca38be" height="200" alt="metal" /><br />**Metaaltextuur**<br /><img src="https://github.com/user-attachments/assets/b93bd4ce-b593-419c-9f0d-d60deb67bd9d" height="200" alt="metal texture" /><br />**Phong**<br /><img src="https://github.com/user-attachments/assets/3af9cb27-a06f-493e-9a73-03ff988581ee" height="200" alt="phong" /><br />**Phongtextuur**<br /><img src="https://github.com/user-attachments/assets/3823281b-a926-4cf8-8246-e7c303db1ef2" height="200" alt="phong textured" /><br />**Enkele kleur**<br /><img src="https://github.com/user-attachments/assets/4bee6f0f-b67d-42c2-a2ef-3cd79e0c8761" height="200" alt="single color" />

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="3d-features-4" githubLink="https://github.com/qgis/QGIS/pull/66112" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ondersteuning toegevoegd voor het maken van 3D-symbologie vanuit 2D-symbology
Dit voegt een nieuw item "Vanuit 2D-symbologie" toe aan het combinatievak voor 3D-symbologie. Dit maakt het mogelijk een nieuwe 3D-symbologie te maken uit een van 2D. Als een 3D-symbologie al bestaat, wordt die vervangen door deze nieuwe 3D- symbologie. Dit kan nuttig zijn om snel 2D-regels/categorieën te repliceren of soortgelijke kleuren te hebben tussen de weergaven 2D en 3D.<br />Wanneer de huidige 2D-symbologiestijl geen 3D-equivalent heeft, is het item uitgeschakeld.<br />Als bijvoorbeeld de 2D-symbologie "Gecategoriseerd" is, maakt het een 3D-symbologie "Gecategoriseerd", kopieert elke categorie en probeert 3D-symbolen te maken, gebaseerd op de 2D.

Wanneer er geen perfecte match is tussen de 2D-symbooleigenschappen en de 3D-symbooleigenschappen, kunnen alleen eenvoudige eigenschappen worden gekopieerd:<br />\| 2D-eigenschap \| 3D-equivalent \|<br />\|-------------------\|-------------------------------------------------------------\|<br />\| Vulkleurr \| QgsMaterialSettings::setColorsFromBase(fillColor) \|<br />\| Opaciteit \| Opaciteit \|<br />\| Grootte punt \| Straal bol \|<br />\| Grootte vierkant \| Grootte kubus \|<br />\| Grootte driehoek \| Lengte kegel / topRadius / BottomRadius \|<br />\| Regelgebaseerde stijlen \| Elke 2D-regel wordt een 3D-regel met de in kaart gebrachte eigenschappen \|<br />\| gecategoriseerde stijlen \|  Elke 2D-categorie wordt een 3D-categorie met de in kaart gebrachte eigenschappen \|<br />**Gecategoriseerd**<br /><img src="https://github.com/user-attachments/assets/b9e92da6-e61b-4ac3-ae42-1eac897b27f5" height="200" alt="image" /><br />**Regelgebaseerd**<br /><img src="https://github.com/user-attachments/assets/ec827505-db52-401d-8b17-ba71d78413b5" height="200" alt="image" /><br />**Enkel symbool**<br /><img src="https://github.com/user-attachments/assets/8ee6fe47-3ed1-4932-a316-c19b744fe3a4" height="200" alt="image" />

Dit werd mogelijk gemaakt door StadtFrankfurt am Main

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://github.com/ptitjano)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-print-layouts" >}}
## Afdruklay-outs
{{<rich-box-start layoutClass="rounded" id="print-layouts-1" githubLink="https://github.com/qgis/QGIS/pull/67392" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Beheer toegevoegd over de positie van de eenheid voor de schaalbalk
In plaats van te forceren dat de eenheden altijd worden geplaatst na het laatste afstandslabel, hebben gebruikers nu een keuze om ze exact te plaatsen waar ze willen.

Opties zijn:
- Verticaal gecentreerd op de balk, voordat de balk begint
- Verticaal gecentreerd op de balk, nadat de balk eindigt
- Tekst gecentreerd op de linkerrand van de balk, boven de balk
- Horizontaal gecentreerd op de balk, boven de balk
- Tekst gecentreerd op de rechterrand van de balk, boven de balk
- Tekst gecentreerd op de linkerrand van de balk, onder de balk
- Horizontaal gecentreerd op de balk, onder de balk
- Tekst gecentreerd op de rechterrand van de balk, onder de balk
- Geplaatst voor het eerste afstandslabel
- Geplaatst na het laatste afstandslabel
- Geplaatst bovenop de balk, na de eerste balkverdeling
- Geplaatst voor elk afstandslabel (als deel van de tekst van het afstandslabel)
- Geplaatst na elk afstandslabel (als deel van de tekst van het afstandslabel)

Meerdere opties mogen worden geselecteerd, wat een volledig flexibele plaatsing van de eenheid mogelijk maakt.

<img src="images/entries/6550fd668b4b0e152e475a754923f9e3f14d3a95.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-expressions" >}}
## Expressies
{{<rich-box-start layoutClass="rounded" id="expressions-1" githubLink="https://github.com/qgis/QGIS/pull/66772" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Argument Version toegevoegd voor UUID-expressiefunctie
Standaard worden versie 4 UUID's gemaakt. Dit nieuwe argument 'version' maakt het mogelijk een andere versie UUID te maken. Ondersteunde waarden zijn 4 (huidige standaard) en 7.

<img src="images/entries/9b70f25047c670d893e11706c039858845adcfce.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="expressions-2" githubLink="https://github.com/qgis/QGIS/pull/66714" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Optionele deflectiehoeken toegevoegd om expressiefunctie uit te breiden
Indien gespecificeerd, zullen deze het begin of einde afbuigen met de gespecificeerde hoek in graden met de wijzers van de klok mee.

<img src="images/entries/d23f87740e4c95b474779dac087339923c98e7fe.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-digitising" >}}
## Digitaliseren
{{<rich-box-start layoutClass="rounded" id="digitising-1" githubLink="https://github.com/qgis/QGIS/pull/67028" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Dynamisch labelvoorbeeld weergeven tijdens bewerken van vectorobjecten
Voor gelabelde vectorlagen is een direct dynamisch voorbeeld toegevoegd van de plaatsing van het label tijdens het bewerken van geometrieën.<br />Van toepassing voor de gereedschappen Verplaatsen, Verschuiving, Schaal roteren en Vereenvoudigen (gereedschap Punten volgt nog).<br />Enkele opmerkingen:
- Er wordt geen vermijden van botsingen met obstakels of vermijden van overlappen uitgevoerd bij het weergeven hiervan (om dingen te kunnen laten uitvoeren), dus u zult een andere plaatsing krijgen als u de bewerkingen toepast als een ander label in de weg staat
- Het voorbeeld gebruikt exact dezelfde logica voor plaatsing als welke het programma voor labels gebruikt, dus alles wordt weergegeven zoals het hoort -- modi voor plaatsing, afstand, herhalingen, valschaduwen, etc.
- U zult nog steeds de huidige plaatsing van labels op de achtergrond zien (lijkt veel op nog steeds het huidige object geometrie zien)

<img src="images/entries/e556e99c1e7d3b4a28950c2c46cc11e46036a75f.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-data-management" >}}
## Gegevensbeheer
{{<rich-box-start layoutClass="rounded" id="data-management-1" githubLink="https://github.com/qgis/QGIS/pull/66462" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### GeoJSON-profielen ondersteunen (RFC7946, JSON-FG JSON-FG-PLUS bronondersteuning)
Gedeeltelijke implementatie van https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md<br />GeoJSON exporteren implementeert nu 4 afzonderlijke profielen voor:
- Legacy : QGIS standaardgedrag vanaf dit PR (d.i. ondersteunt andere CRSen dan CRS84)
- RFC7946: GeoJSON conform met RFC7946
- JSON-FG: OGC Features and Geometries JSON Part 1: core http://www.opengis.net/def/profile/OGC/0/jsonfg
- JSON-FG-PLUS: OGC Features and Geometries JSON Part 1: core http://www.opengis.net/def/profile/OGC/0/jsonfg-plus

Standaardgedrag voor bestaande exports van JSON is niet gewijzigd, maar nieuwe profielen verschaffen de mogelijkheid om `M` (metingen) en geometrieën `ZM` te exporteren<br />Dit werk is het resultaat van een collectieve inspanning van fondsen van:<br />QGIS gebruikersgroep Duitsland (QGIS-DE e.V.)<br />Gis3W<br />QTIBIA<br />Oslandia

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="data-management-2" githubLink="https://github.com/qgis/QGIS/pull/66545" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### DB Manager verwijderen
In lijn met [QEP 426](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-426-demote_dbmanager.md) is de DB Manager nu vervangen door een element Berichtenbalk dat gebruikers in kennis stelt dat ze in plaats daarvan de vervangende plug-in van de gemeenschapsuitgave zouden moeten installeren. De plug-in is verplaatst naar https://github.com/qgis/db_manager_plugin/tree/main, en is toegevoegd aan de opslagplaats voor plug-ins op [plugins.qgis.org](https://plugins.qgis.org/plugins/db_manager_community).

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-forms-and-widgets" >}}
## Formulieren en widgets
{{<rich-box-start layoutClass="rounded" id="forms-and-widgets-1" githubLink="https://github.com/qgis/QGIS/pull/67963" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Implementeren mogelijkheden van bewerken attributenformulier met QML-bewerkerwidget
Historisch gezien had de QML-bewerkerwidget de mogelijkheid om door expressies gegeven waarden weer te geven. Het had echter geen mogelijkheid om het object aan te passen dat werd bewerkt.<br />In deze nieuwe versie heeft de scène van de QML-bewerkerwidget toegang tot basisfunctionaliteiten voor attributenformulieren, alsook de mogelijkheid om te reageren op wijzigingen, zoals een bijgewerkt currentFormFeature en de bewerkbare staat van het attributenformulier.

<img src="images/entries/809c3ba2ac98fc44d543cf40a5ab0ed119fdea68.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-processing" >}}
## Processing
{{<rich-box-start layoutClass="rounded" id="processing-1" githubLink="https://github.com/qgis/QGIS/pull/67464" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Optionele "Maximale zoombereiken" voor XYZ-algoritmes
Staat gebruikers toe om sub-bereiken te specificeren van de tegels die meer detail moeten hebben (hoger zoomniveau), wat het mogelijk maakt meer tegels te maken voor gebieden met meer interesse.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-2" githubLink="https://github.com/qgis/QGIS/pull/67439" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Nieuw algoritme om XYZ-rastertegels GeoPackage te maken
Net zoals de bestaande XYZ-MBtiles/directory algoritmes, maar ondersteunt het wegschrijven van de tegels naar een gegevensset van GeoPackage rastertegels.<br />Ondersteunt ook het maken van niet-standaard (d.i. niet-webMercator) tegelset voor de GPKG en "directory tiles"-algoritmes, wat het maken van tegels met aangepaste tegelmatrixen mogelijk maakt.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-3" githubLink="https://github.com/qgis/QGIS/pull/67408" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Toestaan van webp als optie voor afbeeldingsindeling om algoritmes voor XYZ-tegels te maken
Staat het maken van tegels in de indeling webp toe.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-4" githubLink="https://github.com/qgis/QGIS/pull/67407" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Optie om lege tegels over te slaan in algoritmes van XYZ-tegels
Repareert https://github.com/qgis/QGIS/issues/35174

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-5" githubLink="https://github.com/qgis/QGIS/pull/67389" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Eigen ports toevoegen van SAGA's 'Kanalennetwerk en drainagebassins'
Twee nieuwe eigen algoritmes zijn toegevoegd die directe ports zijn van het gereedschap van SAGA 'Channel Network and Drainage Basins':
- Kanalennetwerk en drainagebassins vanuit DEM: een alles-in-een-gereedschap dat slechts een DEM als invoer vraagt
- 'Kanalennetwerk en drainagebassins vanuit meerdere invoeren': een meer efficiënte versie van het gereedschap voor wanneer de stroomrichting en de Strahler-volgordes al zijn berekend.

De uitvoer zijn vectorbassins, kanalen en splitsingen.

Dit werd mogelijk gemaakt door [Hans van der Kwast en een crowdfunding-campagne](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-6" githubLink="https://github.com/qgis/QGIS/pull/67388" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### SAGA-gereedschappen voor D8 stroomrichting, connectiviteit en Strahler-volgordes geporteerd naar eigen algoritmes van Processing
- Toegevoegd een eigen algoritme "stroomrichting", wat een directe port is van de berekening van Flow Direction vanuit het gereedschap van SAGA "Channel Network and Drainage Basins". Het is als een zelfstandig gereedschap in Processing uitgenomen om optimaal gebruik in modellen en werkwijzen van QGIS mogelijk te maken (tegengesteld aan de alles-in-een-implementatie in de equivalent van SAGA).
- Toegevoegd een eigen algoritme "Connectiviteit stroom", wat een direct port is van het gedeelte Flow Connectivity van het gereedschap van SAGA "Channel Network and Drainage Basins".
- Twee algoritmes toegevoegd voor het berekenen van de Strahler-stroomvolgordes vanuit DEM's. Deze algoritmes geven ports weer van de logica voor de berekening van Strahler vanuit het gereedschap van SAGA "Channel Network and Drainage Basins". Er zijn twee versies van het algoritme beschikbaar:
- "Strahler-volgorde vanuit DEM": de enige vereiste invoer is een DEM, waarmee het algoritme intern een raster van de stroomrichting maakt
- "Strahler-volgorde vanuit DEM en stroomrichting": vereist zowel de DEM als het vooraf berekende raster voor de stroomrichting. Deze versie is efficiënter voor scenario's waarin een raster voor de stroomrichting al is berekend.

Deze zijn allemaal als een zelfstandig gereedschap in Processing opgenomen om optimaal gebruik in modellen en werkwijzen van QGIS mogelijk te maken (tegengesteld aan de alles-in-een-implementatie in de equivalent van SAGA).

Dit werd mogelijk gemaakt door [Hans van der Kwast en een crowdfunding-campagne](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-7" githubLink="https://github.com/qgis/QGIS/pull/67352" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Gereedschap van SAGA Upslope Area geporteerd naar eigen algoritme voor Processing
Een eigen port van het gereedschap van SAGA "Upslope Area". Dit wordt in twee verschillende versies weergegeven, verfijnd om te gebruiken in QGIS:
- "Opwaarts gebied (vanaf punt)": heeft als invoer een parameter punt, wat het mogelijk maakt het opwaartse gebied te berekenen als een enkel punt
- "Opwaarts gebied (vanaf laag)": heeft als invoer een puntenlaag, die vanuit deze laag het gecombineerde bijdragende opwaartse gebied berekent voor alle locaties van doelpunten

Dit zijn BIJNA 1:1-ports van de gereedschappen van SAGA (aangepast voor optimale prestaties in de API van QGIS), met uitzondering van de methode "Multiple Maximum Downslope Gradient Based Flow Direction". De implementatie van SAGA van deze methode heeft een probleem dat erin resulteert dat alle uitvoercellen ofwel een waarde 1 of 100 hebben. Dat is hier gerepareerd, wat ervoor zorgt dat deze methode nu correct de wiskunde respecteert uit het originele paper van Qin et al (2011). (Dit werd opgemerkt door Gemini te vragen om de kwaliteitsport te vergelijken met de originele code van SAGA, en door de originele PDF-versies van de paper te vergelijken. Ik heb dat met de hand gecontroleerd tegen het originele paper en de reparatie van het probleem IS correct (en resulteert in definitief meer correcte uitvoer) -- het is zorgvuldig geannoteerd in de bron van de port voor QGIS.) Ik heb dit probleem ook ingediend bij SAGA, zodat ze dat kunnen corrigeren (Bekijk https://sourceforge.net/p/saga-gis/bugs/337/)

Dit werd mogelijk gemaakt door [Hans van der Kwast en een crowdfunding-campagne](https://www.qwast-gis.com/l/native-hydrology-tools-in-qgis-4-4/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-8" githubLink="https://github.com/qgis/QGIS/pull/67285" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Eigen gereedschappen voor SAGA's thin plate spline-interpolatie
Dit zijn direct ports van het gereedschap TPS interpolation van SAGA, gesplitst in twee afzonderlijke algoritmes voor Processing om beter overeen te komen met het gedrag van algoritmes in QGIS.<br />Het algoritme "Thin Plate Spline-interpolatie (globaal)" is een overeenkomst voor de standaardinstellingen van het gereedschap van SAGA, waar een enkele<br />globale Thin Plate Spline die tegelijkertijd passeert door alle invoerpunten wordt gebruikt voor interpolatie. Dat is alleen<br />geschikt voor gegevenssets met wat lagere aantallen punten.<br />Het algoritme "Thin Plate Spline-interpolatie (lokaal)" is een overeenkomst met de instelling om het gereedschap van SAGA te gebruiken in de lokale modus met een maximale zoekafstand. Een TPS wordt gemaakt voor elke individuele rasterpixel, gebaseerd op de dichtstbijzijnde punten binnen deze zoekafstand. Deze versie is geoptimaliseerd om te gebruiken op hele grote gegevenssets met punten.

Dit werd mogelijk gemaakt door [Hans van der Kwast en een crowdfunding-campagne](https://www.qwast-gis.com/l/crowdfunding-native-qgis-tools-for-hydrology/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-9" githubLink="https://github.com/qgis/QGIS/pull/67117" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Modelontwerper "automatisch aanvullen"
We hebben de mogelijkheid voor slepen en neerzetten uitgebreid met een mogelijkheid "automatisch aanvullen". Bij het slepen verschijnt een contextueel vak dat alleen de huidige compatibele algoritmes en parameters vermeld.<br />Dat maakt het maken van modellen sneller, gemakkelijker en minder foutgevoelig voor gebruikers.<br />Dit is heel veel geïnspireerd op dezelfde mogelijkheid in de nodebewerker van Blender en werkt ook omgekeerd om automatisch invoerparameters te selecteren.<br />**Hoe het werkt**<br />Begin met een uitgang te slepen en in plaats van die te verbinden met een andere uitgang, laat los ergens in het venster.<br />U zult door middel van een vak worden gevraagd met alleen het compatibele algoritme of de parameter met de uitgang die u sleepte.<br />Bij het toevoegen van het algoritme aan het venster zal dat verbinden met de eerste toepasselijke uitgang.<br />Bij ontkoppelen verschijnt de pop-up niet.

<img src="images/entries/50b46aecff18c5c50c048a3dd465af2b65e96aa0.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/fr/)

Deze mogelijkheid werd ontwikkeld door [Celia Buira](https://github.com/CeliaBuira)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-10" githubLink="https://github.com/qgis/QGIS/pull/66851" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Opties voor selecteren profiel toegevoegd aan qgis_process
U kunt nu qgis_process uitvoeren met een specifiek gebruikersprofiel, dezelfde opties gebruiken als QGIS Desktop. `--profile naam` laadt een bestaand benoemd profiel, en `--profiles-path pad` (of `-S`) verwijst naar de map die de map met uw `profielen` bevat. Een geplande of serverzijde uitvoering kan dan de plug-ins van Processing, scripts en instellingen die u hebt ingesteld in QGIS Desktop gebruiken, zonder het standaardprofiel te wijzigen.<br />`qgis_process` gebruikt altijd het standaardgebruikersprofiel en pad naar profielen, dus een Processing script, plug-in of instelling die in een ander profiel staat kan niet worden bereikt (#44783).<br />Dit voegt de opties voor de opdrachtregel `--profile <name>` en `--profiles-path <path>` (`-S`) toe die QGIS Desktop al weergeeft:
- `--profile` laadt een bestaand benoemd profiel uit de map met profielen.
- `--profiles-path` / `-S` stelt de map in die de map `profiles` bevat en heeft voorrang boven `QGIS_CUSTOM_CONFIG_PATH`.
- Met alleen `--profiles-path` wordt het standaardprofiel gebruikt dat in root's `profiles.ini` wordt gebruikt.
- Zonder optie profile wordt het standaardprofiel geladen door dezelfde enkele aanroep `init()`.
- Een benoemd `--profile` dat niet bestaat, wordt afgewezen (fout, exit 1) en moet eerst worden gemaakt en geconfigureerd in QGIS Desktop. Het standaardprofiel wordt op aanvraag gemaakt, dus een uitvoering zonder `--profile` heeft geen eerdere instelling nodig.

Het profiel wordt opgelost voor `QgsApplication::init()` en het laden van plug-ins, omdat het gekozen profiel bepaalt waaruit de instellingen en plug-ins moeten worden gelezen. De sneltoets `--help`/`--version` en de hoofdparser delen dezelfde afhandeling van opties, dus met een geldige waarde werkt een informatie-query nog steeds als er eerst een profieloptie komt, terwijl een ontbrekende, lege of optieachtige waarde altijd een fout is (exit 1). Een profiel waarvan de map niet kan worden gemaakt, bijvoorbeeld wanneer het pad naar het profiel niet kan worden beschreven of een normaal bestand is, faalt met reden in plaats van te worden uitgevoerd met een half afgemaakt profiel.<br />Dit hergebruikt de Desktop's optienamen van de opdrachtregel en de semantiek voor het pad `QgsUserProfileManager`. Het reproduceert niet de rest van het opstarten van Desktop: de globale instelling `core/profilesPath`, de profielmigratie van QGIS 3 naar 4 en het beleid voor interactieve selectie zijn ongewijzigd en blijven alleen voor Desktop.<br />Nieuwe uitvoerbare testen (`test_qgsprocessexecutable_pt3.py`) dekken de uitvoer voor Help het ontdekken van profiellokale scripts, per-profiel plug-in ingeschakelde-staat isolatie, profiles-path isolatie en voorrang boven `QGIS_CUSTOM_CONFIG_PATH`, het geconfigureerde standaardprofiel, de verkorte vorm `-S`, misvormde en ontbrekende waarden, de `--` argumentbegrenzing, `--version`/`--help` volgorde, afwijzen van een benoemd profiel zonder een map te maken, op-aanvraag maken van het standaardprofiel, JSON-uitvoer en paden met spaties. Ze werden lokaal uitgevoerd op Linux; de Windows en macOS werkwijzen voor verpakken werden gebouwd met `ENABLE_TESTS=OFF`, dus ze voeren deze suite niet uit.<br />Dit voegt voor de gebruiker zichtbare CLI-vlaggen toe, dus heeft het een overeenkomende bijgewerkte documentatie nodig.<br />Repareert [\#44783](https://github.com/qgis/QGIS/issues/44783)

<img src="images/entries/cec932b434ad8dfc9bcf1d29c98950cdbcb9a65b.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [秀吉](https://github.com/thc1006)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="processing-11" githubLink="https://github.com/qgis/QGIS/pull/66514" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Weergeven van functionaliteit GEOS Coverage Cleaner en een algoritme voor Processing ervoor toegevoegd
Geeft mogelijkheid weer voor opschonen van bedekking vanuit GEOS in QgsGeometry en voegt een nieuw algoritme toe aan Processing "Bedekking leegmaken" dat werkt op een imperfecte bedekking (polygonengegevensset). Maakt het schoner door overlappende gebieden te verwijderen en kleine gaten tussen polygonen te sluiten om een topologisch correcte bedekking te maken.<br />Vereist een versie van QGIS die is gebouwd met een GEOS-versie van ten minste 3.14.0.<br />Repareert https://github.com/qgis/QGIS/issues/66513.

<img src="images/entries/c368d862da4b53996c70ab2744dc52da1879290a.png" class="img-responsive img-rounded" />

Deze mogelijkheid werd ontwikkeld door [Juho Ervasti](https://github.com/JuhoErvasti)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-application-and-project-options" >}}
## Opties voor toepassing en projecten
{{<rich-box-start layoutClass="rounded" id="application-and-project-options-1" githubLink="https://github.com/qgis/QGIS/pull/67476" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Meerdere mappen afhandelen voor projectsjablonen
U mag nu meerdere mappen specificeren voor projectsjablonen. Dat maakt het bijvoorbeeld mogelijk een team te hebben met zijn eigen set projectsjablonen, plus enkele sjablonen die uit een andere gecentraliseerde map van een organisatie komen.<br />Het submenu voor het maken van een project vanuit een sjabloon is alleen beschikbaar als er ten minste een projectsjabloon in een sjabloonmap staat.<br />Een knop op de werkbalk is toegevoegd om consistent te zijn met het menu.<br />Een nieuw pictogram voor projectsjablonen is voorgesteld: <img src="https://github.com/user-attachments/assets/4e371268-1d34-494e-b0b5-c2a340ca76f5" width="33" height="33" alt="image" /><br />Het nieuwe welkomstscherm is aangepast om de mappen als secties weer te geven.

<img src="images/entries/4d462d93f23e7d7db0035cba30ad628ecbf72db2.png" class="img-responsive img-rounded" />

Dit werd mogelijk gemaakt door [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-profile-plots" >}}
## Profiel plotten
{{<rich-box-start layoutClass="rounded" id="profile-plots-1" githubLink="https://github.com/qgis/QGIS/pull/67484" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Modus "Vaste schaal" voor lay-out bereiken van hoogteprofielen
De vorige modus waar de gebruiker expliciet de min./max. afstand en hoogtebereiken instelt, is nu gelabeld als "Handmatige bereiken". Als de nieuwe optie "Vaste schalen" is geselecteerd, kan de gebruiker een expliciete schaal afzonderlijk instellen voor de afstand en de hoogteas.<br />De optie "Minimum hoogte" is nog steeds beschikbaar in modus "Vaste schalen", zodat het nog steeds mogelijk is de hoogteas te beginnen op een zinnige minimale waarde en de vaste schaal te gebruiken om de maximale hoogte voor deze as te bepalen.<br /><img src="https://github.com/user-attachments/assets/c7bfc858-9080-4d0c-9d6b-ff86f086fbba" width="367" height="174" alt="image" />

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-qgis-server" >}}
## QGIS Server
{{<rich-box-start layoutClass="rounded" id="qgis-server-1" githubLink="https://github.com/qgis/QGIS/pull/66762" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### JSON-FG en tijd weergeven in QGIS-server OAPIF
Weergeven van JSON-FG en JSON-FG-PLUS (en RFC7946) als profielen voor OGCAPI for features.<br />Geeft ook de dimensie "time" weer, zoals in de specificaties:<br />https://docs.ogc.org/is/21-045r1/21-045r1.html#time<br />https://docs.ogc.org/is/23-058r2/23-058r2.html#\_primary_temporal_information<br />Dit werk is het resultaat van een collectieve fondseninspanning van:<br />QGIS gebruikersgroep Duitsland (QGIS-DE e.V.)<br />Gis3W<br />QTIBIA<br />Oslandia

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="qgis-server-2" githubLink="https://github.com/qgis/QGIS/pull/66495" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### QEP 414 - Verscheidene verbeteringen inclusief object schema
Ter ondersteuning van de QGIS Server OAPIF implementaties van JSON-FG en FlatGeobuf-indeling vanuit [QEP 414](https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-414-server-oapif-jsonfg-flatgeobuf.md) omvatten nieuwe wijzigingen aan de OGC API:
- schema (inclusief `x-ogc-role` , `format` en `type` voor hoofdwidgets)
- references (van `RelationReference` en `ValueRelation`)
- profiles (voor references)
- volledige ondersteuning CRS in verzoeken en antwoorden (inclusief `storageCrs` en `storageCrsCoordinateEpoch` indien beschikbaar)
- ondersteuning voor extra geometriekolommen (Postgres), weergegeven als WKT (getransformeerd naar het verzochte CRS)
- codelijst voor enums en `Waardenkaart`
- nieuwe klassen voor conformiteit

Dit werd mogelijk gemaakt door [Geogirafe gebruikersgroep / OPENGIS.ch](http://opengis.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="qgis-server-3" githubLink="https://github.com/qgis/QGIS/pull/67343" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Ondersteuning voor waarde "default" voor dimensie Time in WMS GetCapabilities
Parameter `default` is een deel van de GetCapabilities-tag Dimension. Het dient om de standaardwaarde aan te geven die moet worden gebruikt als een verzoek GetMap geen waarde specificeert. Net als met vectorlagen kunt u de standaardweergave kiezen om ofwel een minimum- of een maximumwaarde te zijn, een in te stellen verwijzingswaarde, of "Alle waarden" wat de huidige situatie is als er geen standaard is opgeschreven.<br /><img src="https://github.com/user-attachments/assets/d91e42a0-a036-4a5d-b28c-f206f7814780" width="626" height="918" alt="default" /><br />**Implementatiedetail**<br />We hergebruiken WmsDimensionInfo voor groepen omdat we ons kunnen voorstellen dat we later een andere configuratie voor de dimensie van groepen krijgen en om consistent te blijven met vectorlaag. Op dit moment is het mogelijk om slechts een dimensie "TIME" voor groepen te hebben.

Dit werd mogelijk gemaakt door Ressources Naturelles Canada

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://github.com/troopa81)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-programmability" >}}
## Programmeerbaarheid
{{<rich-box-start layoutClass="rounded" id="programmability-1" githubLink="https://github.com/qgis/QGIS/pull/67314" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Algoritme van SAGA 'Raster grid cell index' geporteerd naar nieuwe QgsSortedRasterBlockIndex API
Maakt een platte index over een QgsRasterBlock, gesorteerd op celwaarden.<br />Gebaseerd op SAGA'S geïndexeerde CSG_Grid, veelgebruikt in de gereedschapskist voor terreinanalyses van SAGA.<br />Bevat nu een port van het gereedschap van SAGA "Grid Cell Index" als een eigen algoritme "Index rastercellen raster". Dit algoritme rangschikt geldige niet-Geen gegevens-rastercellen overeenkomstig hun waarde, voert een nieuw raster uit waarin elke cel zijn op 0 gebaseerde gesorteerde index (rang) bevat.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<rich-box-start layoutClass="rounded" id="programmability-2" githubLink="https://github.com/qgis/QGIS/pull/66910" >}}

{{<rich-content-start themeClass="coloring-1" >}}
### Vervallen subklassen Processing WidgetWrapper verwijderd
Implementeert Step 2 van https://github.com/qgis/QGIS-Enhancement-Proposals/blob/master/qep-427-remove-deprecated-processing-gui-api.md.<br />Plug-ins die nog steeds deze vervallen subklassen gebruikten, moeten worden aangepast naar de C++ Processing-gebruikersinterface, zoals in detail is vermeld in de QEP.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)

{{< rich-content-end >}} {{< rich-box-end >}}

{{<changelog-category-end >}}

{{<changelog-category-start id="category-notable-fixes" >}}
## Belangrijke reparaties
### Reparaties van problemen door Alessandro Pasotti (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Temporary layer icon in layer tree can be missing on Windows | [\#67531](https://github.com/qgis/QGIS/issues/67531) | [PR \#67532](https://github.com/qgis/QGIS/pull/67532) | [PR \#67556](https://github.com/qgis/QGIS/pull/67556) |
| Attempting to "Set Comment..." on a postgres view in Browser results in an error | [\#67358](https://github.com/qgis/QGIS/issues/67358) | [PR \#67528](https://github.com/qgis/QGIS/pull/67528) | Nee |
| Transaction groups: after "Save Layer Edits", layers can no longer leave edit mode by rollback ("no such savepoint") | [\#67523](https://github.com/qgis/QGIS/issues/67523) | upstream GDAL issue [\#15294](https://github.com/OSGeo/gdal/issues/15294) | N/B |
| \[sqlite\]\[gpkg\] Savepoints are not removed after a COMMIT | [\#15294](https://github.com/OSGeo/gdal/issues/15294) |  | N/B |
| \[REGRESSION\] PostgreSQL database loading is significantly slower in QGIS 4.2 than 3.44 in the browse | [\#67454](https://github.com/qgis/QGIS/issues/67454) | [PR \#67585](https://github.com/qgis/QGIS/pull/67585) | N/B |
| Postgres "Set Comment" windows on Tables and Projects should word wrap rather than horizontally scroll | [\#67357](https://github.com/qgis/QGIS/issues/67357) | [PR \#67594](https://github.com/qgis/QGIS/pull/67594) | Is het niet waard |
| PostgreSQL: not all linked styles are loaded with the layer | [\#67181](https://github.com/qgis/QGIS/issues/67181) | [PR \#67619](https://github.com/qgis/QGIS/pull/67619) | N/B |
| Label word wrap character is considered after case change | [\#67501](https://github.com/qgis/QGIS/issues/67501) | [PR \#67767](https://github.com/qgis/QGIS/pull/67767/) | in progress |
| Feature rejected by the database is regarded as saved and lost with toggling edit mode | [\#67474](https://github.com/qgis/QGIS/issues/67474) | [PR \#67792](https://github.com/qgis/QGIS/pull/67792) | NOG TE DOEN |
| GDAL provider: raster in a mixed raster/vector GeoPackage gets the vector layers' CRS (or none) with GDAL \>= 3.12 | [\#67777](https://github.com/qgis/QGIS/issues/67777) | [PR \#67783](https://github.com/qgis/QGIS/pull/67783) | N/B |
| QGIS Server WMS GetMap request hangs displaying inverted polygon layer with shapeburst fill incl. blur strength | [\#67142](https://github.com/qgis/QGIS/issues/67142) | Kan niet worden gereproduceerd, gesloten |  |
| Feature rejected by the database is regarded as saved and lost with toggling edit mode | [\#67474](https://github.com/qgis/QGIS/issues/67474) | [PR \#67792](https://github.com/qgis/QGIS/pull/67792) |  |
| Adding a new feature through attribute table on an empty layer crashes QGIS | [\#65025](https://github.com/qgis/QGIS/issues/65025) | [PR \#67816](https://github.com/qgis/QGIS/pull/67816) Achterhaald door oplossing van Nyall) |  |
| WMS GetCapabilities fails with "Decompression failed" on large capabilities documents (Qt6 decompressedSafetyCheckThreshold) | [\#66979](https://github.com/qgis/QGIS/issues/66979) | [PR \#67831](https://github.com/qgis/QGIS/pull/67831) | N/B |
| WMS GetCapabilities fails with gzip-encoded response (QGIS 4.0 / Qt6) | [\#65418](https://github.com/qgis/QGIS/issues/65418) | [PR \#67854](https://github.com/qgis/QGIS/pull/67854) | N/B |
| Color table ignored if sidecar xml with an attribute table exists in tiff images | [\#62579](https://github.com/qgis/QGIS/issues/62579) | [PR \#67875](https://github.com/qgis/QGIS/pull/67875) | N/B |
| WFS GetFeature fails with "Decompression failed" on large gzip responses (Qt6 decompressedSafetyCheckThreshold), no way to disable the check for WFS connections | [\#67970](https://github.com/qgis/QGIS/issues/67970) | [PR \#68010](https://github.com/qgis/QGIS/pull/68010) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (QCooperative)](https://www.qcooperative.net/)
### Reparaties van problemen door Julien Cabieces (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS4 customisation does not work | [\#67530](https://github.com/qgis/QGIS/issues/67530) | [PR \#67544](https://github.com/qgis/QGIS/pull/67544) | N/B |
| Raster calculator in 3.44LTR returns erraneous results | [\#67457](https://github.com/qgis/QGIS/issues/67457) | [PR \#67545](https://github.com/qgis/QGIS/pull/67545) | [PR \#67562](https://github.com/qgis/QGIS/pull/67562) |
| Status bar vanishes if UI customization is just enabled | [\#67590](https://github.com/qgis/QGIS/issues/67590) | [PR \#67660](https://github.com/qgis/QGIS/pull/67660) | N/B |
| Missing titles for customization item | Niet gerapporteerd | [PR \#67662](https://github.com/qgis/QGIS/pull/67662) | N/B |
| User Bookmarks are not migrated to QGIS 4 | [\#67583](https://github.com/qgis/QGIS/issues/67583) | [PR \#67667](https://github.com/qgis/QGIS/pull/67667) | N/B |
| QGIS 3 -\> QGIS 4 migration: QGIS starts the first time with the GUI translated to the system language instead of the custom one set | [\#65237](https://github.com/qgis/QGIS/issues/65237) | [PR \#67667](https://github.com/qgis/QGIS/pull/67667) | N/B |
| QGIS 3 -\> QGIS 4 migration: the paths stored inside QGIS3.ini are not correctly handled when transferred to QGIS4.ini | [\#65238](https://github.com/qgis/QGIS/issues/65238) | [PR \#67776](https://github.com/qgis/QGIS/pull/67776) | N/B |
| QGIS 3 -\> QGIS 4 migration: starting QGIS with --profiles-path and --profile options, QGIS3.ini is not copied to QGIS4.ini, instead a new QGIS4.ini is created | [\#65239](https://github.com/qgis/QGIS/issues/65239) | Zal niet gerepareerd worden |  |
| Fix drag'n drop in customization dialog | [\#67968](https://github.com/qgis/QGIS/issues/67968) | [PR \#67709](https://github.com/qgis/QGIS/pull/67709) | N/B |
| pluginManagerInterface().pluginMetadata() returns empty/error if Plugin Manager has never been opened | [\#67291](https://github.com/qgis/QGIS/issues/67291) | [PR \#67785](https://github.com/qgis/QGIS/pull/67785) | [PR \#67985](https://github.com/qgis/QGIS/pull/67985) |
| Adding a layout variable does not set the project dirty | [\#67261](https://github.com/qgis/QGIS/issues/67261) | [PR \#67789](https://github.com/qgis/QGIS/pull/67789) | [PR \#68004](https://github.com/qgis/QGIS/pull/68004) |
| Modifying a data defined override of a layout does not set the project dirty | [\#67262](https://github.com/qgis/QGIS/issues/67262) | [PR \#67804](https://github.com/qgis/QGIS/pull/67804) | [PR \#67984](https://github.com/qgis/QGIS/pull/67984) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Reparaties van problemen door Jean Felder (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Filtering features from a WFS layer gives an error in QGIS 4.2 | [\#67715](https://github.com/qgis/QGIS/issues/67715) | [PR \#67813](https://github.com/qgis/QGIS/pull/67813) | N/B |
| TIN Interpolation Issue with break/structure lines | [\#66429](https://github.com/qgis/QGIS/issues/66429) | [PR \#67815](https://github.com/qgis/QGIS/pull/67815) | N/B |
| Font Marker bug in Elevation Profile window | [\#65865](https://github.com/qgis/QGIS/issues/65865) | [PR \#67818](https://github.com/qgis/QGIS/pull/67818) | N/B |
| DXF exporter writes UTF-8 encoded MTEXT while declaring ANSI_949 when CP949 encoding is selected | [\#67573](https://github.com/qgis/QGIS/issues/67573) | [PR \#67827](https://github.com/qgis/QGIS/pull/67827) | N/B |
| wrong nan check in QgsBox3D::isNull | Niet gerapporteerd | [PR \#67852](https://github.com/qgis/QGIS/pull/67852) | [PR \#67876](https://github.com/qgis/QGIS/pull/67876) |
| Elevation profile not recognising rule-based symbols | [\#56035](https://github.com/qgis/QGIS/issues/56035) | [PR \#67855](https://github.com/qgis/QGIS/pull/67855) | NOG TE DOEN |
| Elevation profile with raster DEM appears shifted | [\#58236](https://github.com/qgis/QGIS/issues/58236) | [PR \#67859](https://github.com/qgis/QGIS/pull/67859) | [PR \#67883](https://github.com/qgis/QGIS/pull/67883) |
| Elevation Profile: the Appearance setting Continuous Surface does not work anymore with Vector data | [\#64302](https://github.com/qgis/QGIS/issues/64302) | [PR \#67864](https://github.com/qgis/QGIS/pull/67864) | N/B |
| Continous Surface option no longer works in QGIS 3.38.1 | [\#58393](https://github.com/qgis/QGIS/issues/58393) | Kan niet worden gereproduceerd, gesloten |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder (Oslandia)](https://oslandia.com/en/)
### Reparaties van problemen door Loïc Bartoletti (Oslandia)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix build with LazPerf and Spatialindex | unreported on github, patches from FreeBSD | [PR \#67780](https://github.com/qgis/QGIS/pull/67780) | N/B |
| Fix chamfer/fillet | [\#67344](https://github.com/qgis/QGIS/issues/67344) | [PR \#67882](https://github.com/qgis/QGIS/pull/67882) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Loïc Bartoletti (Oslandia)](https://oslandia.com/en/)
### Reparaties van problemen door Germán Carrillo (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Adapt test_core_expression to GEOS 3.15 | Niet gerapporteerd | [PR \#67592](https://github.com/qgis/QGIS/pull/67592) | N/B |
| GEOS 3.15: Splitting collections explodes the collection | [\#67478](https://github.com/qgis/QGIS/issues/67478) | [PR \#67650](https://github.com/qgis/QGIS/pull/67650) | N/B |
| \[geos\] Fix 'ZM' in QGIS-GEOS-QGIS conversions | Niet gerapporteerd | [PR \#67747](https://github.com/qgis/QGIS/pull/67747) | N/B |
| Loss of M values when splitting features | [\#40796](https://github.com/qgis/QGIS/issues/40796) | [PR \#67798](https://github.com/qgis/QGIS/pull/67798) | N/B |
| Building master fails when using dev version of GEOS | [\#67886](https://github.com/qgis/QGIS/issues/67886) | [PR \#67926](https://github.com/qgis/QGIS/pull/67926) | N/B |
| Pie Chart not working in version 3.34.9-Prizren | [\#62904](https://github.com/qgis/QGIS/issues/62904) | Is geen probleem | N/B |
| Add support for Z/M geometries in WFS Client | [\#57692](https://github.com/qgis/QGIS/issues/57692) | Al gerepareerd | N/B |
| Different default M values depending on the function | [\#27792](https://github.com/qgis/QGIS/issues/27792) | Al gerepareerd | N/B |
| Elevation Profile / QGIS 4: QgsPluginLayer do not show if other layers are visible | [\#66965](https://github.com/qgis/QGIS/issues/66965) | [PR \#67967](https://github.com/qgis/QGIS/pull/67967) | N/B |
| Count the number of features passing through the model | [\#15085](https://github.com/qgis/QGIS/issues/15085) | Al gerepareerd | N/B |
| Crash splitting a CurvePolygon in QGIS master | [\#68203](https://github.com/qgis/QGIS/issues/68203) | [PR \#68220](https://github.com/qgis/QGIS/pull/68220) | N/B |
| CurvedPolygon Merging Converts True Arcs into Segments in QGIS | [\#60961](https://github.com/qgis/QGIS/issues/60961) | Al gerepareerd | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Germán Carrillo (OPENGIS.ch)](https://opengis.ch/)
### Reparaties van problemen door Alexander Bruy (QCooperative)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Export to GeoParquet silently writes 0 features: Save-As dialog clamps COMPRESSION_LEVEL default (-1) to 0, which is invalid for the default SNAPPY codec (GDAL 3.12) | [\#66822](https://github.com/qgis/QGIS/issues/66822) | Al gerepareerd |  |
| Error and highest exectuion time of qgis:tilesxyzdirectory in QGIS 3.34.15-Prizren 'Prizren' (386f2583a69) | [\#60526](https://github.com/qgis/QGIS/issues/60526) | Al gerepareerd |  |
| Error of the raster histogram | [\#38298](https://github.com/qgis/QGIS/issues/38298) | Kan niet worden gereproduceerd, gesloten |  |
| \[Processing\] "Distance to nearest hub" (native:distancetonearesthub) fails unless both outputs are set, although both are optional | [\#67548](https://github.com/qgis/QGIS/issues/67548) | [PR \#67549](https://github.com/qgis/QGIS/pull/67549) | [PR \#67551](https://github.com/qgis/QGIS/pull/67551) |
| Concave Hull algorithm generates incorrect output | [\#54561](https://github.com/qgis/QGIS/issues/54561) | Al gerepareerd |  |
| Timezone is ignored when listing styles saved in the GeoPackage | Niet gerapporteerd | [PR \#67554](https://github.com/qgis/QGIS/pull/67554) | [PR \#67579](https://github.com/qgis/QGIS/pull/67579) |
| Duplicate styles returned when listing styles in the geopackage | Niet gerapporteerd | [PR \#67577](https://github.com/qgis/QGIS/pull/67577) | [PR \#67604](https://github.com/qgis/QGIS/pull/67604) |
| Wrong render of Help page in GDAL creation options setting | [\#47433](https://github.com/qgis/QGIS/issues/47433) | [PR \#67588](https://github.com/qgis/QGIS/pull/67588) | N/B |
| shadow in raster histogram plot area can confuse | [\#41113](https://github.com/qgis/QGIS/issues/41113) | [PR \#67614](https://github.com/qgis/QGIS/pull/67614) | N/B |
| SensorThings provider reads HTTP header settings from wrong section | Niet gerapporteerd | [PR \#67639](https://github.com/qgis/QGIS/pull/67639) | [PR \#67679](https://github.com/qgis/QGIS/pull/67679) |
| Styles stored inside a GeoPackage are not found anymore by QGIS | [\#58467](https://github.com/qgis/QGIS/issues/58467) | [PR \#67607](https://github.com/qgis/QGIS/pull/67607) | [PR \#67846](https://github.com/qgis/QGIS/pull/67846) |
| Unable to parse vector tiles XML generated in QGIS 3 | [\#65477](https://github.com/qgis/QGIS/issues/65477) | [PR \#67647](https://github.com/qgis/QGIS/pull/67647) | [PR \#67680](https://github.com/qgis/QGIS/pull/67680) |
| Updating raster single-band min/max method does not update actual min/max | [\#26593](https://github.com/qgis/QGIS/issues/26593) | [PR \#67666](https://github.com/qgis/QGIS/pull/67666) | N/B |
| qgis.testing.start_app() log output is silent since QGIS 4.0: QgsMessageLog.messageReceived(message, tag, level) is never emitted | [\#67668](https://github.com/qgis/QGIS/issues/67668) | [PR \#67670](https://github.com/qgis/QGIS/pull/67670) | N/B |
| Toolbuttons with popups are missing in overflow menus | [\#58641](https://github.com/qgis/QGIS/issues/58641) | [PR \#67690](https://github.com/qgis/QGIS/pull/67690) | N/B |
| WCS GetCoverage - Problem with GRIDORIGIN and GRIDOFFSETS with latitude/longitude CRS (EPSG:4326 and EPSG:4617) | [\#59445](https://github.com/qgis/QGIS/issues/59445) | [PR \#67760](https://github.com/qgis/QGIS/pull/67760) | [PR \#67781](https://github.com/qgis/QGIS/pull/67781) |
| drop QTEST_DISABLE_KEYPAD_NAVIGATION from tests (fix broken build on Qt 6.12) | Niet gerapporteerd | [PR \#67763](https://github.com/qgis/QGIS/pull/67763) | N/B |
| Zonal statistics only works with shapefiles | [\#46602](https://github.com/qgis/QGIS/issues/46602) | [PR \#67765](https://github.com/qgis/QGIS/pull/67765) | [PR \#67850](https://github.com/qgis/QGIS/pull/67850) |
| Deprecation warning in GPX provider | Niet gerapporteerd | [PR \#67782](https://github.com/qgis/QGIS/pull/67782) | N/B |
| WCS layers with query string will lose the query string parameter when calling the GetCoverage method | [\#52842](https://github.com/qgis/QGIS/issues/52842) | [PR \#67811](https://github.com/qgis/QGIS/pull/67811) | [PR \#67851](https://github.com/qgis/QGIS/pull/67851) |
| XYZ tiles from local files no longer works in 4.X series | [\#66518](https://github.com/qgis/QGIS/issues/66518) | [PR \#67879](https://github.com/qgis/QGIS/pull/67879) | N/B |
| Symmetric Classification in graduated symbol cant turn off | [\#65853](https://github.com/qgis/QGIS/issues/65853) | [PR \#67902](https://github.com/qgis/QGIS/pull/67902) | [PR \#67947](https://github.com/qgis/QGIS/pull/67947) |
| QGIS does not use TRANSPARENT=FALSE advertise by the WMS capabilities | [\#42951](https://github.com/qgis/QGIS/issues/42951) | Kan niet worden gereproduceerd, gesloten |  |
| Layout Charts: Only the first color ramp is used for all the series in a pie chart | [\#67159](https://github.com/qgis/QGIS/issues/67159) | [PR \#67954](https://github.com/qgis/QGIS/pull/67954) | N/B |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Alexander Bruy (QCooperative)](https://www.qcooperative.net/)
### Reparaties van problemen door Celia Buira (OPENGIS.ch)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Prevent multiple model designer window to override model changes | Niet gerapporteerd | [PR \#68000](https://github.com/qgis/QGIS/pull/68000) |  |
| View Output Layers feature from model designer doesn't work if spatial index is applied on vec. layer | [\#67743](https://github.com/qgis/QGIS/issues/67743) | [PR \#68076](https://github.com/qgis/QGIS/pull/68076) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Celia Buira (OPENGIS.ch)](http://opengis.ch/)
### Reparaties van problemen door Stefanos Natsis (Lutra Consulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Guard against writing out of bounds in array_insert | Niet gerapporteerd | [PR \#67888](https://github.com/qgis/QGIS/pull/67888) | N/B |
| Fix identifying and highlighting point cloud points in 3d views with different crs | Niet gerapporteerd | [PR \#67990](https://github.com/qgis/QGIS/pull/67990) | Nee |
| Make sure the style manager page is not first for point cloud layers | Niet gerapporteerd | [PR \#67991](https://github.com/qgis/QGIS/pull/67991) | N/B |
| Fix vpc labels when layer crs does not match map crs | Niet gerapporteerd | [PR \#68009](https://github.com/qgis/QGIS/pull/68009) | Nee |
| Fix point cloud editing when layer and map crs do not match | Niet gerapporteerd | [PR \#68015](https://github.com/qgis/QGIS/pull/68015) | Nee |
| Fix global map shading state when starting a new project | Niet gerapporteerd | [PR \#68021](https://github.com/qgis/QGIS/pull/68021) | [PR \#68047](https://github.com/qgis/QGIS/pull/68047) |
| Impossible to cancel movement of annotation items | [\#66701](https://github.com/qgis/QGIS/issues/66701) | [PR \#68028](https://github.com/qgis/QGIS/pull/68028) | N/B |
| Enable keyboard navigation in welcome screen | [\#64891](https://github.com/qgis/QGIS/issues/64891) | [PR \#68070](https://github.com/qgis/QGIS/pull/68070) | N/B |
| Hide welcome screen when new project is clicked | Niet gerapporteerd | [PR \#68071](https://github.com/qgis/QGIS/pull/68071) | N/B |
| adding layer with custom QgsRasterDataProvider crashes QGIS | [\#59284](https://github.com/qgis/QGIS/issues/59284) | [PR \#68101](https://github.com/qgis/QGIS/pull/68101) | Nee |
| Elevation Profile's layer tree: drag&drop layer appears twice | [\#64957](https://github.com/qgis/QGIS/issues/64957) | [PR \#68104](https://github.com/qgis/QGIS/pull/68104) | Nee |
| Fix out of bounds read in levenshtein implementation | Niet gerapporteerd | [PR \#68130](https://github.com/qgis/QGIS/pull/68130) | [PR \#68199](https://github.com/qgis/QGIS/pull/68199) |
| Welcome page: Unable to open a blank project when QGIS is launched with the recent project by default | [\#68121](https://github.com/qgis/QGIS/issues/68121) | [PR \#68139](https://github.com/qgis/QGIS/pull/68139) | N/B |
| Assert hit when aborting the deletion of an attribute used for sorting | [\#68157](https://github.com/qgis/QGIS/issues/68157) | [PR \#68158](https://github.com/qgis/QGIS/pull/68158) | Nee |
| Default Styles not available | [\#68160](https://github.com/qgis/QGIS/issues/68160) | [PR \#68164](https://github.com/qgis/QGIS/pull/68164) | N/B |
| Preselect http/https/ftp when adding data using protocol | Niet gerapporteerd | [PR \#68167](https://github.com/qgis/QGIS/pull/68167) | Nee |
| .slpk I3S meshes do not work with QGIS4 | [\#66100](https://github.com/qgis/QGIS/issues/66100) | [PR \#68185](https://github.com/qgis/QGIS/pull/68185) | Nee |
| Fix rendering I3S layers where i3s-scale_x/y is defined | [\#66100](https://github.com/qgis/QGIS/issues/66100) | [PR \#68187](https://github.com/qgis/QGIS/pull/68187) | Nee |
| Fix QT warning for submenu's parent | Niet gerapporteerd | [PR \#68188](https://github.com/qgis/QGIS/pull/68188) | Nee |
| CVS / delimited text file provider filter returns zero features when there is a space in the column name | [\#68189](https://github.com/qgis/QGIS/issues/68189) | [PR \#68194](https://github.com/qgis/QGIS/pull/68194) | Nee |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Reparaties van problemen door Jan Caha (Lutra Consulting)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Handle QgsInterval in expressions for PG driver | [\#62577](https://github.com/qgis/QGIS/issues/62577) | [PR \#68066](https://github.com/qgis/QGIS/pull/68066) |  |
| Do not estimate extent for TopoGeometry | [\#60593](https://github.com/qgis/QGIS/issues/60593) | [PR \#68057](https://github.com/qgis/QGIS/pull/68057) |  |
| Fix potentially long load time for schemata with QGIS projects in Browser | [\#66990](https://github.com/qgis/QGIS/issues/66990) | [PR \#68052](https://github.com/qgis/QGIS/pull/68052) |  |
| Issues in 3d editing Point Cloud Widget | Niet gerapporteerd | [PR \#68020](https://github.com/qgis/QGIS/pull/68020) |  |
| "Build virtual point cloud (VPC)" algorithm should only support VPC and VPZ | Niet gerapporteerd | [PR \#68005](https://github.com/qgis/QGIS/pull/68005) |  |
| ELSE Rule based renderer feature counts | [\#27893](https://github.com/qgis/QGIS/issues/27893) | [PR \#67989](https://github.com/qgis/QGIS/pull/67989) |  |
| Add -cwhere for gdalwarp when Clipping raster using vector layer with Feature filter | [\#67383](https://github.com/qgis/QGIS/issues/67383) | [PR \#67928](https://github.com/qgis/QGIS/pull/67928) |  |
| gdal_connection_details_from_layer() for vsiPrefix GDAL/OGR sources | [\#61144](https://github.com/qgis/QGIS/issues/61144) | [PR \#67823](https://github.com/qgis/QGIS/pull/67823) |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Jan Caha (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Reparaties van problemen door Nyall Dawson (North Road)
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.44 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix crash in labeling | [\#68210](https://github.com/qgis/QGIS/issues/68210) | [PR \#68234](https://github.com/qgis/QGIS/pull/68234) | [PR \#68247](https://github.com/qgis/QGIS/pull/68247) |
| Fixes crash when adding field to empty table via attribute table |  | [PR \#68146](https://github.com/qgis/QGIS/pull/68146) |  |
| Remove not safe postgres layer name logic |  | [PR \#68145](https://github.com/qgis/QGIS/pull/68145) |  |
| Fixes crash when pasting items in a new empty model | [\#68100](https://github.com/qgis/QGIS/issues/68100) | [PR \#68143](https://github.com/qgis/QGIS/pull/68143) |  |
| Fix crash if project is closed while new feature dialog is open |  | [PR \#68112](https://github.com/qgis/QGIS/pull/68112) |  |
| Fix overlapping widgets in 3d config dialog |  | [PR \#68111](https://github.com/qgis/QGIS/pull/68111) |  |
| \[afs\] Handle case mismatches between service level feature names and json | [\#67979](https://github.com/qgis/QGIS/issues/67979) | [PR \#67983](https://github.com/qgis/QGIS/pull/67983) |  |
| Fix failing tests - Don't update project when setting snap widget initial state from project |  | [PR \#67956](https://github.com/qgis/QGIS/pull/67956) |  |
| Prevent recursion when editing columns |  | [PR \#67949](https://github.com/qgis/QGIS/pull/67949) |  |
| Fix hang when rendering labels with huge angle values | [\#67885](https://github.com/qgis/QGIS/issues/67885) | [PR \#67913](https://github.com/qgis/QGIS/pull/67913) | [PR \#67948](https://github.com/qgis/QGIS/pull/67948) |
| Use more efficient way to handle loading old projects with font marker fix- \#67914 | [\#67901](https://github.com/qgis/QGIS/issues/67901) | [PR \#67914](https://github.com/qgis/QGIS/pull/67914) |  |
| Fix missing feature count in model after model run completes | [\#67874](https://github.com/qgis/QGIS/issues/67874) | [PR \#67896](https://github.com/qgis/QGIS/pull/67896) |  |
| Fix leak of QCompleter objects- \#67894 |  | [PR \#67894](https://github.com/qgis/QGIS/pull/67894) |  |
| Speed up like expressions |  | [PR \#67871](https://github.com/qgis/QGIS/pull/67871) |  |
| Fix leak in QgsAttributesFormLayoutModel |  | [PR \#67870](https://github.com/qgis/QGIS/pull/67870) |  |
| Speed up unaccent function, restore use in searches |  | [PR \#67868](https://github.com/qgis/QGIS/pull/67868) |  |
| Fix issues in attribute table model | [\#65025](https://github.com/qgis/QGIS/issues/65025) | [PR \#67856](https://github.com/qgis/QGIS/pull/67856) |  |
| Introduce widgets for choice of time zone, QDateTime with explicit time zone | [\#67496](https://github.com/qgis/QGIS/issues/67496) | [PR \#67820](https://github.com/qgis/QGIS/pull/67820) |  |
| Fix selective masking issues with opacity/blend modes | [\#49488](https://github.com/qgis/QGIS/issues/49488) | [PR \#67810](https://github.com/qgis/QGIS/pull/67810) |  |
| Fix some minor leaks |  | [PR \#67808](https://github.com/qgis/QGIS/pull/67808) |  |
| Fix leak in expression parsing |  | [PR \#67806](https://github.com/qgis/QGIS/pull/67806) |  |
| Massively speed up parallel rendering of expression-heavy projects | [\#67718](https://github.com/qgis/QGIS/issues/67718) | [PR \#67771](https://github.com/qgis/QGIS/pull/67771) |  |
| Fix leak of unparented objects |  | [PR \#67770](https://github.com/qgis/QGIS/pull/67770) |  |
| Fix leak of QgsVersionInfo in welcome screen |  | [PR \#67677](https://github.com/qgis/QGIS/pull/67677) |  |
| Fix leak of thread local QSettings |  | [PR \#67676](https://github.com/qgis/QGIS/pull/67676) |  |
| When changing a raster to single band psuedocolor, use default color ramp |  | [PR \#67674](https://github.com/qgis/QGIS/pull/67674) |  |
| \[mssql\] Fix handling of srid |  | [PR \#67653](https://github.com/qgis/QGIS/pull/67653) | [PR \#67673](https://github.com/qgis/QGIS/pull/67673) |
| Fix crash when grouping layout items | [\#61702](https://github.com/qgis/QGIS/issues/61702) | [PR \#67661](https://github.com/qgis/QGIS/pull/67661) |  |
| Fix crash when opening context menu on non-database browser layers |  | [PR \#67658](https://github.com/qgis/QGIS/pull/67658) |  |
| Fix parent ownership of QObject map layer children |  | [PR \#67656](https://github.com/qgis/QGIS/pull/67656) |  |
| \[mssql\] Fix loss of srid/wkbtype during initialization | [PR \#67672](https://github.com/qgis/QGIS/pull/67672) | [PR \#67654](https://github.com/qgis/QGIS/pull/67654) |  |
| Fix missing CRS info in tooltips for layers with custom CRS |  | [PR \#67652](https://github.com/qgis/QGIS/pull/67652) |  |
| Fix crash when switching between raster layers which support histograms vs not |  | [PR \#67651](https://github.com/qgis/QGIS/pull/67651) |  |
| Fix crash when changing style through layer style dock style manager |  | [PR \#67599](https://github.com/qgis/QGIS/pull/67599) |  |
| Fix docked attribute tables open side-by-side, not tabbed | [\#65633](https://github.com/qgis/QGIS/issues/65633) | [PR \#67572](https://github.com/qgis/QGIS/pull/67572) | [PR \#67644](https://github.com/qgis/QGIS/pull/67644) |
| Ensure layer IDs never become too long | [\#67164](https://github.com/qgis/QGIS/issues/67164) | [PR \#67570](https://github.com/qgis/QGIS/pull/67570) |  |
| Fix exceptions when running algorithms that output html files in batch mode |  | [PR \#67560](https://github.com/qgis/QGIS/pull/67560) | [PR \#67567](https://github.com/qgis/QGIS/pull/67567) |
| Remove non-functional pre/post execution script setting | [\#44651](https://github.com/qgis/QGIS/issues/44651) | [PR \#67559](https://github.com/qgis/QGIS/pull/67559) | [PR \#67569](https://github.com/qgis/QGIS/pull/67569) |
| Fix exporting animations in Movie mode from temporal controller |  | [PR \#67494](https://github.com/qgis/QGIS/pull/67494) |  |
| Fix QgsAbstractProcessingParameterWidgetWrapper use through PyQGIS- \#67491 | [\#67401](https://github.com/qgis/QGIS/issues/67401) | [PR \#67491](https://github.com/qgis/QGIS/pull/67491) | [PR \#67511](https://github.com/qgis/QGIS/pull/67511) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com/)

{{<changelog-category-end >}}

{{<content-end >}}
