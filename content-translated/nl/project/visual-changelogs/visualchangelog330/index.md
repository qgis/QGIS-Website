---
HasBanner: false
draft: false
releaseDate: 04-03-2023
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.30
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.30{#changelog330 }
![image1](images/projects/af9e5405a8329d7de8959238a3d499da780c1598.png)

Datum uitgave 04-03-2023

De uitgave 3.30 \'s-Hertogenbosch van het vernieuwende project QGIS introduceert een breed scala aan wijzigingen en verbeteringen uit de ontwikkelgemeenschap van QGIS.

Het welkomstscherm laat een fragment zien van de "Gemeentekaart" van \'s-Hertogenbosch uit 1867. Het maakt deel uit van een serie van 1200 kaarten van alle gemeenschappen Nederland rond die tijd, die werden gepubliceerd in een atlas voor elk van de 11 regio's. Alle kaarten werden op dezelfde grootte getekend, hoewel voor grotere gemeenten een dubbel formaat werd gebruikt en geschaald om overeen te komen met de pagina. De serie werd internationaal geprezen vanwege zijn nauwkeurigheid en volledigheid. De kaart werd getekend door Jacob Kuyper (1821-1908), de meest beroemde geograaf en cartograaf van zijn tijd in Nederland. Tekst en afbeelding voor welkomstscherm beschikbaar gesteld door [atlasandmap.com](https://atlasandmap.com)

De eigen integratie van GeoNode is ook gemigreerd naar een externe plug-in, wat de krachtige extensies voor de QGIS API voor plug-ins, geimplementeërd in recente uitgaven, ten volle benut.

Gebruikers kunnen ook nieuwe functionaliteiten en verbeteringen aan de UI verwachten, inclusief ondersteuning voor raster attributentabellen, intelligente en configureerbaar sorteren voor het laden van lagen, verbeteringen aan de mogelijkheden voor GPS, meer dynamische formulierwidgets, eigen voorbeelden van rich media voor bijlagen, betere integratie met cloud-services, extensies voor de QGIS standaarden voor metadata, en een host voor andere noemenswaardige aanvullingen.

Voor een snelle toer door alle nieuw geïntroduceerde functionaliteiten kunt u de video met deze mogelijkheden bekijken op YouTube op <https://www.youtube.com/watch?v=q7O819lFKc4>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/q7O819lFKc4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is een inspanning van de gemeenschap en we willen ook nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier bij wilt dragen in het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote of kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst van donoren](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). Als u een dragend lid voor het project zou willen worden, bekijk dan onze [pagina voor dragende leden](https://qgis.org/en/site/about/sustaining_members.html) voor de details. Sponsoren van QGIS helpen ons om fondsen te verkrijgen voor onze regelmatige ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige sponsoren wordt hieronder weergegeven - een welgemeend bedankt voor al onze sponsoren!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht hun financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Belangrijke wijzigingen
### Mogelijkheid: Vervallen achterwaartse compatibiliteit voor symbologie in project met QGIS 3.16 en ouder
Eerdere uitgaven van QGIS zouden significante hoeveelheden compatibiliteits-objecten schrijven naar de XML-structuur van projectbestanden om achterwaartse compatibiliteit te behouden voor symbologieën om er voor te zorgen dat projectbestanden kunnen worden geopend met QGIS 3.16 en ouder. Deze compatibiliteit is verwijderd uit toekomstige uitgavent.

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://github.com/3nids)
## Kaartgereedschap
### Mogelijkheid: Raster kaarttips
in eerdere uitgaven waren Kaarttips slechts alleen beschikbaar voor vectorlagen, maar nieuwe wijzigingen in de API hebben het mogelijk gemaakt om Kaarttips ook voor andere typen kaarten te implementeren.

Rasterlagen ondersteunen nu Kaarttips, en nieuwe functies voor mogelijkheden van expressies zijn toegevoegd om de bestaande mogelijkheden voor Kaarttips uit te breiden:
- `map_to_html_table`: converteert een kaart (gegevensstructuur van paren sleutel/waarde) naar een HTML-tabel
- `map_to_html_dl`: converteert een kaart (gegevensstructuur van paren sleutel/waarde) naar een definitielijst in HTML
- `raster_attributes`: maakt een kaart met de veldnamen als sleutels en de waarden van de rasterattributentabel vanuit het item van de attributentabel dat overeenkomt met de opgegeven rasterwaarde
- een nieuw bereik voor expressies \"Positie kaartlaag\" dat een variabele `@layer_cursor_point` definieert met de coördinaten van de laag (in het CRS van de laag) op de positie van de muis

![image3](images/entries/7cc33f0191d7461c103eef9eb792495d4b298dd6.webp)

Dit werd mogelijk gemaakt door NOAA OCS Hydrography

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Identificeren met verplaatsing muis, geen muisklik
Een nieuwe optie maakt het mogelijk het gereedschap Objecten identificeren te gebruiken met het verplaatsen van de muis, zonder in het kaartvenster te hoeven klikken.

Deze optie gedraagt zich bijna identiek aan de standaardoptie voor Objecten identificeren, met als verschil dat de gebruiker niet hoeft te klikken of een sneltoets hoeft te gebruiken om de actie voor identificeren uit te voeren. Dit stelt het gereedschap Objecten identificeren in staat zich soortgelijk te gedragen als de mogelijkheid voor Kaarttips, tegelijkertijd de gebruikers de voordelen van het gereedschap Objecten identificeren te geven, zoals ondersteuning voor meerdere laagtypen en afgeleide informatie.

De standaard activatie is een tijdklok van 300 milliseconden die de actie voor Objecten identificeren uitvoert, die is geïmplementeerd om problemen bij uitvoering te vermijden bij het verplaatsen van de muis.

![image4](images/entries/36bfbae2b85c46b304ea84c05ce819fd69a66d38.gif)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Gebruikersinterface
### Mogelijkheid: Op beperkingen gebaseerde functionaliteit voor attributentabellen
Nieuwe, op beperkingen gebaseerde, voorwaardelijke opmaak en mislukt filteren van objecten met beperkingen worden weergegeven in de attributentabel.

Deze functionaliteit verschaft opties voor het filteren om objecten weer te geven of te verbergen die mislukte (harde of zachte) beperkingen hebben, en introduceert een nieuw type voorwaardelijke opmaak dat werkt naast de al bestaande typen voor rijen en velden om objecten te accentueren die niet voldoen aan de beperkingen voor de laag.

![image5](images/entries/4ad89600c1e78bca863927f30581319b86afe6f1.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Aanvullend informatiepaneel en werkbalk Velden voor GPS
Het informatiepaneel voor GPS bevat nu de huidige totale lengte van het spoor, en de afstand vanaf het begin van het spoor. Deze mogelijkheden zijn ook beschikbaar als een (niet standaard ingeschakeld) optie die het mogelijk maakt ze weer te geven in de werkbalk voor het informatielabel van GPS.

Het informatiepaneel GPS bevat ook ellipsoïde hoogte in de beschikbare waarden voor GPS-informatie.

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: UX GPS Informatiepaneel en opnieuw bewerkt
Substantieel opnieuw bewerken van het informatiepaneel voor GPS is uitgevoerd om het verwerken van GPS door gebruikers in QGIS te vereenvoudigen en een meer gestroomlijnde ervaring voor GPS te verschaffen.

Eerder werd **alle** functionaliteit voor GPS op het niveau van de toepassing weergegeven door een enkele interface voor het GPS \"Informatie\"paneel. Dat de instellingen voor de verbinding van GPS bevatten, het digitaliseren van GPS, en de feitelijke weergave van informatie over GPS. Deze interface raakte verstopt en was moeilijk te gebruiken.

Functionaliteit voor GPS is nu gesplitst in afzonderlijke delen:
1. Niveau van de toepassing, zelden gewijzigde instellingen voor GPS zijn aanwezig op de tab GPS van het menu Opties in de instellingen van QGIS.
2. Een nieuwe zwevende \"werkbalk GPS\" is toegevoegd, die de meest gebruikte, aan GPS gerelateerde bewerkingen bevat.
3. De laatste actie in de werkbalk GPS opent een popup \"GPS-instellingen\", die verschillende instellingen bevat waarvan wordt verwacht dat ze tijdens een sessie kunnen worden aangepast en beter bereikbaar zijn.
4. De widget GPS-informatie is opnieuw ontworpen om alleen GPS **informatie** weer te geven. Specifiek: alleen de tabs \"Informatie\" en \"Signaal\" zijn behouden. De widget GPS-informatie bevat nog steeds een sneltoets naar de actie verbinden/verbinding verbreken, en ook een knop Instellingen die hetzelfde menu voor instellingen van GPS weergeeft als wat wordt gebruikt in de werkbalk GPS.

De klasse widget GPS informatie is nu ALLEEN verantwoordelijk voor het weergeven van de GPS-informatie in het paneel, en nieuwe toegewezen klassen zijn overeenkomstig gemaakt voor het afhandelen van digitaliseren van GPS, de nieuwe werkbalk GPS, en instellingen voor GPS.

![image6](images/entries/206ae34a728a37cae967f60887b5a7f2bbd94c0f.webp)

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Symbologie
### Mogelijkheid: Verbeterde opties voor exporteren SLD
Een nieuwe uitbreiding voor de API voor het exporteren van Styled Layer Descriptor (SLD) is ontwikkeld en parallel bestaat naast bestaande opties voor exporteren van SLD, maar aanvullende functionaliteit verschaft voor nauwkeuriger beheer van het exporteren van SLD.

Deze ontwikkeling bevat ook het exporteren van complexe polygoon laagstijlen als externe grafische symbolen die worden opgeslagen naast de geëxporteerde SLD.

![image7](images/entries/cce332a4adc8cc7a24ead53acd8924431f1085f2.webp)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Renderen
### Mogelijkheid: Globaal schaduwen voor kaartterrein
Gebruikers zijn nu in staat een globaal schaduweffect voor de kaart toe te passen, die is gebaseerd op de hoogte van *alle* actieve lagen die hoogte ondersteunen, inclusief :
- Rasterlagen (als \"Geeft oppervlakte hoogte weer\" is geselecteerd in de Laageigenschappen)
- Lagen met mazen
- Puntenwolklagen

De waarde voor de hoogte op elke bepaalde positie voor alle relevante lagen worden gecombineerd, en de overwogen hoogte wordt gekozen, afhankelijk van één van de twee door de gebruiker gedefinieerde methoden:
- De hoogste hoogte wordt overwogen
- De hoogte van de hoogste laag in de boom met lagen wordt overwogen

De implementatie van methoden voor schaduw zijn momenteel de Eye Dome Lighting en het effect van schaduw voor heuvels.

Instellingen voor schaduw worden in de volgende besturingselementen in de gebruikersinterface weergegeven:
- In Projecteigenschappen, op dezelfde tab als de instellingen voor de hoogte van het project
- In het paneel Laag opmaken, een nieuwe tab is gemaakt voor het definiëren van instellingen van globale schaduw voor het terrein

![image8](images/entries/e75c69fb42f1916ceaf4b30f589154dc47881c6f.webp)

Dit werd mogelijk gemaakt door [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

Deze mogelijkheid werd ontwikkeld door [Vincent Cloarec](https://github.com/vcloarec)
### Mogelijkheid: Ondersteuning toegevoegd voor super- en subscript voor de tekstrenderer
Tekstitems in QGIS ondersteunen nu superscript en subscript.

Dit maakt:
- componenten `<sup>superscript</sup>` / `<sub>subscript</sub>` in tekst mogelijk, waar de tekst verticaal super- of subscript wordt uitgelijnd en automatisch op de grootte van 2/3 van de grootte van het ouderlettertype zal worden gebracht. Gebruikers kunnen ook een vaste grootte voor het lettertype voor het super-/subscript instellen door de relevante regels voor CSS op te nemen in hun HTML, bijv. `<sup style="font-size:33pt">super</sup>`
- `vertical-align: super` of `vertical-align: sub` opmaakregels voor CSS in elk ander element van HTML mogelijk

![image9](images/entries/24e510e32b919b373d09e5fe8536cfc0dfd0d66e.webp)

Deze mogelijkheid werd mogelijk gemaakt door OSGEO UK

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## 3D-objecten
### Mogelijkheid: Beperken bereik 2D van 3D-scene
Het gerenderde bereik van een 3D-scene kan nu worden beperkt tot de objecten die kruisen met een door de gebruiker gespecificeerd 2D-bereik.

De manier waarop gerenderde objecten worden beperkt is afhankelijk van het laagtype van de brongegevens:
- Vlak, DEM en Online Terrain worden *geclipt* tot het gespecificeerde bereik
- Puntenwolklagen *laden alleen punten binnen* het gespecificeerde bereik
- Vectorlagen *laden alleen punten die kruisen* met het gespecificeerde bereik

Op bereik gebaseerd filteren van objecten in lagen met mazen is momenteel in ontwikkeling.

![image10](images/entries/a8135c9cfcaa91fdc540512f36cf276a2cdb4f02.webp)

Dit werd mogelijk gemaakt door [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Verbeterd beheer voor camera
Er zijn een aantal verbeteringen die de ervaring voor de gebruiker verbeteren:
- Met het bereik van de hoogte wordt rekening gehouden als \"Volledig zoomen\" wordt gebruikt (gebruikers zouden niet meer moeten eindigen \"achter\" hun scene)
- Camera verticaal verplaatsen met Ctrl + Shift + linkermuisknop
- Zoomen met muis tijdens verplaatsen met muis toestaan
- Ga door met zoomen met rechtermuisknop als de muisaanwijzer het zichtgebied verlaat

Dit werd mogelijk gemaakt door [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Afdruklay-outs
### Mogelijkheid: Beheren sneltoetsen voor afdruklay-outs
Het beheren van sneltoetsen, toegankelijk vanuit het menu Extra van de primaire interface van QGIS, stelt gebruikers in staat bestaande sneltoetsen voor het toetsenbord te configureren en bestaande te overschrijven en ondersteunt door de gebruiker gedefinieerde methoden voor het uitvoeren van Acties van QGIS.

Een soortgelijk dialoogvenster voor het configureren van sneltoetsen voor toetsenbord is nu toegevoegd aan de interface Afdruklay-out voor verbeterde productiviteit.

![image11](images/entries/ce065abd5dfe0a678e461a12e0efef92c5acaae3.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Tekstrenderer gebruiken in legenda's van lay-outs
Deze wijziging maakt het mogelijk de volledige mogelijkheden van de tekstrenderer te gebruiken voor titels, subtitels en tekst voor items in legenda's.

Het maakt het mogelijk buffers, schaduwen, beheren van afstanden van lettertypen, en andere beschikbare opties te configureren (inclusief gemixte opmaak voor HTML) die zijn toegestaan bij het gebruiken in tekstindelingen.

Dit werd mogelijk gemaakt door NIBIO

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Expressies
### Mogelijkheid: Functie Toevoegen feature_id()
Een nieuwe expressie-functie `feature_id($feature)` maakt het nu mogelijk het object-ID van een object op te halen.

De functie accepteert één argument dat een object moet zijn. Soortgelijk kan deze functie worden gebruikt met de resultaten van elke andere functie die objecten teruggeeft, zoals \"get_feature\", \"overlay\_\*\", etc.

![image12](images/entries/6536913b10d68dded9a54bc58ba003b821b100f6.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe functies is_feature_valid() en is_attribute_valid()
Nieuwe functies `is_feature_valid()` en `is_attribute_valid()` worden verschaft in expressies van QGIS. Beide functies valideren een object of attribuut, gebaseerd op de aan de velden aangehechte beperkingen voor een bepaalde vectorlaag. Dit stelt gebruikers in staat de mogelijkheid voor selecteren-met-expressie te gebruiken om objecten te lokaliseren die niet voldoen aan beperkingen. In aanvulling daarop kunnen gebruikers nu de op regel gebaseerde renderer gebruiken om visuele terugkoppeling te verschaffen, door symbologie die de status voor de geldigheid van de beperking voor gerenderde objecten aangeeft.

![image13](images/entries/f6a73012edcc84033d40e91bc6216365fd4f5ae6.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Expressiefuncties x_at, y_at, z_at, m_at toegevoegd
De beschikbare \$functies worden als vervallen beschouwd (`$x_at` en `$y_at`), en in plaats van het werken op de huidige geometrie van het object ondersteunen de functies in plaats daarvan een geometrie van een object als argumenten.

De wijzigingen voor deze expressies bevatten het maken van soortgelijke functies voor andere metingen van geometrieën. Deze nieuwe functies omvatten:
- x_at(geometry, i)
- y_at(geometry, i)
- z_at(geometry, i)
- m_at(geometry, i)

Dit werd mogelijk gemaakt door [Métropole Européenne de Lille](https://www.lillemetropole.fr/)

Deze mogelijkheid werd ontwikkeld door [Antoine Facchini](https://github.com/Koyaani)
## Gegevensbeheer
### Mogelijkheid: Bewerken veld DateTime: scheiding van indeling weergave en indeling veldwaarde
Inspanningen om het beheer van informatie voor het veld Datetime omvatten de expliciete definitie van gelokaliseerde opmaak voor het *weergeven* van velden Datetime, er voor zorgend dat het bewerken, vastleggen en opslaan van de veldwaarden zich conformeert aan internationale standaarden voor de opmaak van tijd.

Dit werd mogelijk gemaakt door [3liz](https://3liz.com)

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
### Mogelijkheid: Optie toegevoegd om direct GPS-punten en tracks te loggen naar een database van GeoPackage of SpatiaLite
Indien geactiveerd in de instellingen voor de werkbalk van GPS, zal de actie \"Log naar GeoPackage/SpatiaLite\" de gebruiker vragen een bestaand bestand GPKG of SpatiaLite te selecteren, of een nieuwe bestandsnaam in te voeren. Een tabel \"gps_points\" en \"gps_tracks\" zal in het bestand worden gemaakt met een vooraf gedefinieerde structuur.

Alle inkomende GPS-berichten zullen worden gelogd naar de laag gps_points, naast de informatie voor snelheid/richting/hoogte/nauwkeurigheid van de GPS.

Wanneer de verbinding met de GPS wordt verbroken (of QGIS wordt afgesloten), zal het gehele opgenomen GPS-spoor worden toegevoegd aan de tabel gps_tracks, naast enige berekende informatie, zoals lengte van het spoor en begin- en eindtijden.

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Een expliciete optie \"Verschuiving van UTC\" toegevoegd voor het opslaan van tijdstempels van GPS-objecten
Deze optie stelt gebruikers in staat om handmatig een gewenste verschuiving vanaf UTC in te voeren voor het opslaan van GPS tijdstempels. Dit maakt volledige flexibiliteit mogelijk voor gebruikers die rekening moeten houden met verschuivingen door zomer-/wintertijd of andere complexe problemen met tijdzones.

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor Raster-AttributenTabellen (RAT)
QGIS ondersteunt nu uitgebreid Raster-AttributenTabellen (RAT's).

Deze bijwerkingen verschaffen een nieuwe interface voor RAT's in de QGIS API, en ondersteuning wordt verschaft voor RAT's die worden beheerd door raster gegevensproviders (GDAL), als ook voor algemene bestanden voor waarde attributentabellen (VAT), vooropgesteld dat zij zijn opgeslagen in een DBF sidecar hulpbestand.

Veel van de functionaliteit van de [Python RAT Plugin](https://github.com/noaa-ocs-hydrography/qgis-raster-attribute-table-plugin) werd geporteerd in QGIS om eigen ondersteuning te verschaffen voor RAT's, en een nieuwe set bewerkingen van de gebruikersinterface biedt gebruikers de volgende geavanceerde functionaliteiten:
- **Automatisch opmaken raster**: Als een RAT beschikbaar is bij het toevoegen van een raster aan het project en informatie over de opmaak bevat, zal QGIS standaard de relevante stijlen toepassen op de rasterlaag. Automatisch laden werkt voor zowel ingebedde RAT's als voor sidecar VAT.DBF met dezelfde basisnaam van het raster.
- **RAT opnieuw classificeren**: Opnieuw classificeren van een raster kan worden uitgevoerd door een andere kolom te selecteren
- **RAT identificeren**: Waarden uit de rij van de RAT die corresponderen met de relevante pixelwaarde worden weergegeven in het kaartgereedschap Objecten identificeren
- **RAT eigenschappen**: Een nieuwe tab \"Attributentabellen\" is beschikbaar in het venster van de laageigenschappen van het raster
- **RAT bewerken**: RAT's bieden basismogelijkheden voor bewerken
- **RAT maken uit huidige classificatie**: RAT's kunnen worden gemaakt uit bestaande gepaletteerde of enkelband pseudokleur stijlen

Een galerij van deze functionaliteiten in actie is [beschikbaar op GitHub](https://github.com/qgis/QGIS/pull/50687)

![image14](images/entries/4406611cee132d2bfae92d9ba01681464f333928.gif)

Dit werd mogelijk gemaakt door NOAA OCS Hydrography

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
## Metadata en Metasearch
### Mogelijkheid: Sleuteldatums toevoegen aan metadata voor laag en project
De volgende velden zijn toegevoegd aan de standaard voor metadata van QGIS laag/project:
- Datum gemaakt
- Datum gepubliceerd
- Datum beoordeeld
- Datum vervangen

In eerdere uitgaven had metadata voor de laag geen velden voor datums, waar metadata voor het project alleen het veld Datum maken bevatte

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Formulieren en widgets
### Mogelijkheid: Ondersteuning voor attributen van audiovisuele multimedia bijlagen
Nieuwe functionaliteit introduceert ondersteuning voor multimedia voor de widget voor externe bronnen, wat het gebruikers mogelijk maakt audio en video mediabestanden af te spelen in de viewer voor bijlagen.

Deze wijziging omvat aanvullende opties voor het configureren van externe bronnen, met twee nieuwe items in het geïntegreerde combinatievak voor het type viewer. Het type video zal rekening houden met de door de gebruiker ingestelde hoogte. Als het op auto wordt gezet, zal de widget video groter worden om de beschikbare ruimte te vullen.

Deze functionaliteit omvat het ontwikkelen van het object `QgsMediaWidget` in de QGIS API voor uitgebreide ondersteuning voor multimedia.

![image15](images/entries/75fcba5750d9ce4bb1b7ad41089dd39fd11ae827.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Bewerkbare status data-bepaald voor formulierwidgets
De status van het keuzevak \"Aanpasbaar\" kan nu worden beheerd door een expressie. De expressie ondersteunt de context "form", wat betekent dat het `current_value( '<field_name>' )` kan gebruiken om dynamisch de status voor Aanpasbaar te wijzigen overeenkomstig de wijzigingen aan andere velden in het formulier.

![image16](images/entries/ce2bc7938c4c5f28d3f0d872e9045c856ef79ef1.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Scheidingsteken-widget voor slepen & neerzetten attributenformulieren
Een nieuw scheidingsteken-widget is verschaft, met de optie om een horizontale lijn te tekenen, wat gebruikers een grotere mate van beheer geeft voor hoe formulieren worden gerenderd voor eindgebruikers en functionaliteit uitbreidt voor verbeterde gebruikerservaring met thematische scheidingen en verbeterde uitlijning.

De widget rendert als een blanco ruimte in het formulier, wat een handmatige scheiding maakt tussen andere objecten van het formulier.

Als de optie \"Horizontale lijn tekenen\" is ingesteld in de configuratie, zal het de vrije ruimte vullen met een lijn op een manier die soortgelijk is aan de horizontale regel, of tag ``<hr>`` in HTML.

![image17](images/entries/72c262227fb339abd30833edc712ead25d943044.webp)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Dynamische tekstwidgets met ondersteuning voor current_value
Tekstwidgets ondersteunen nu dynamische configuratie, gebaseerd op de waarden van velden die in de context van het huidige formulier aanwezig zijn, door een functie `current_value()` te verschaffen die kan worden geëvalueerd in een object `QLabel`.

Gebruik van de expressie `current_value(  '<field_name>' )` zal het formulier evalueren en bijwerken als de waarde van het veld in het formulier wijzigt.

![image18](images/entries/6de3cc5d5a6d002fd014717e57f251ec9b0147d9.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Dynamische HTML-widgets met ondersteuning voor current_value
HTML-widgets ondersteunen nu dynamische configuratie, gebaseerd op de waarden van velden die in de context van het huidige formulier aanwezig zijn door een functie `current_value()` te verschaffen.

Gebruik van de expressie `current_value(  '<field_name>' )` zal het formulier evalueren en bijwerken als de waarde van het veld in het formulier wijzigt.

![image19](images/entries/f04157ac77cf00862595f8b75707c8126e121ce4.gif)

Dit werd mogelijk gemaakt door [Kanton Solothurn](https://geo.so.ch/)

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Meerdere selecties met filteren voor widget relatie met waarden
De widget Waarde relatie negeerde eerder de optie \"Compleet maken gebruiken\" als \"Meerdere selecties toestaan\" werd ingeschakeld. Nu werken deze twee opties samen en is er een zoekvak aanwezig aan de bovenkant van de tabel dat het filteren van waarden mogelijk maakt. Als de optie \"Compleet maken gebruiken\" niet is ingeschakeld, wordt, zoals eerder, het zoekvak niet weergegeven.

![image20](images/entries/3ec355e558ca705d17be8f21c79c613d1022630a.gif)

Dit werd mogelijk gemaakt door [QGIS Noorwegen](http://www.qgis.no/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Legenda van laag
### Mogelijkheid: Nieuwe verbeteringen volgorde van lagen
Nieuwe opties voor te configureren methoden voor het invoegen in de boom met lagen, en het automatisch sorteren van lagen die zijn toegevoegd met functies voor slepen en neerzetten, zijn nu beschikbaar in QGIS.

Het eerdere gedrag was dat QGIS altijd nieuwe lagen laadde boven de huidige actieve laag.

Nieuwe opties zijn verschaft om meer beheer, over hoe nieuwe lagen worden toegevoegd aan projecten, mogelijk te maken:
- Altijd bovenaan de boom van lagen
- Optimale index in de huidige groep van de boom van lagen

De optimale index zal proberen om lagen intelligent te ordenen op type (bijv. punten bovenop gebieden etc.) en een significant verbeterde ervaring verschaffen voor nieuwe gebruikers.

In aanvulling daarop zullen met slepen en neerzetten toegevoegde lagen worden toegevoegd aan de index van de boom van lagen op de locatie van de cursor indien losgelaten om er voor te zorgen dat de laag wordt gerenderd op ene voorspelbare en intuïtieve manier.

![image21](images/entries/a2f44bdf5df6e8b33dc71c975cbb9c01cfa4845c.webp)

Dit werd mogelijk gemaakt door [Fondsen van de Zwitserse QGIS gebruikersgroep](https://www.qgis.ch/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Processing
### Mogelijkheid: Aanvullende opties voor export van XYZ Tile bij het gebruiken van Leaflet HTML-uitvoer
Drie nieuwe optionele geavanceerde parameters zijn weergegeven voor het algoritme voor het maken van het XYZ Tile:
- Titel Leaflet HTML-uitvoer 
- Attributie Leaflet HTML-uitvoer 
- OpenStreetMap-basiskaart opnemen in Leaflet HTML-uitvoer

![image22](images/entries/a96f4972c9664c8887220b0a218103c053050e71.webp)

Deze mogelijkheid werd ontwikkeld door [Björn Hinkeldey](https://github.com/pathmapper)
### Mogelijkheid: Ondersteuning voor waarden van parameters data-bepaald bij het gebruiken van het gereedschap qgis_process
Waar vele algoritmes voor Processing waarden voor parameters data-bepaald ondersteunden, was het niet mogelijk die te specificeren bij het gebruiken van het gereedschap qgis_process (of bij het weergeven van instellingen voor het algoritme als JSON en opdrachten voor qgis_process), wat beperkingen introduceerde voor het gebruiken van QGIS in bewerkingen van Processing op de opdrachtregel.

Een nieuwe syntaxis wordt nu verschaft om het specificeren van waarden parameters data-bepaald toe te staan bij het uitvoeren van bewerkingen met qgis_process, en het kopiëren van de instellingen voor het algoritme vanuit QGIS zal nu op de juiste wijze de data-bepaalde waarden afhandelen.

Argumenten voor de opdrachtregel worden gespecificeerd met het voorvoegsel `expression:` binnen een omsloten tekenreeks, terwijl de definitie voor JSON wordt geïmplementeerd met een object expression met een typedefinitie `data_defined`. Onthoud dat speciale tekens in de expressie het toepasselijke teken voor escapen moeten gebruiken, relevant vergeleken met de context waarin ze worden gebruikt.

Kijkend naar de expressie `@variable*"field_name"*to_int('2')/100` voor de volgende voorbeelden, zou de opdracht voor de opdrachtregel moeten zijn:

    --PARAMETER='expression:@variable*"field_name"*to_int('\''2'\'')/100'
    
Terwijl de weergave in JSON zou moeten zijn:

    "inputs": {
      "PARAMETER": {
        "expression": "@variable*\"field_name\"*to_int('2')/100",
        "type": "data_defined"
      },
      "OUTPUT": "TEMPORARY_OUTPUT"
    }
    
Dit werd mogelijk gemaakt door het Research Institute for Nature and Forest, Vlaamse overheid

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuwe functie \"load_layer\"
Een nieuwe expressiefunctie `load_layer` is beschikbaar gemaakt (voorlopig alleen exclusief voor expressies van Processing), die het laden van een kaartlaag met een brontekenreeks en naam van een provider mogelijk maakt.

Het is ontworpen om het gebruik mogelijk te maken van expressie-functies die direct verwijzen naar kaartlagen (zoals de functies voor totaliseren) met een hard gecodeerd pad naar de laag.

Dit maakt het mogelijk deze functies te gebruiken buiten een project (zoals via het gereedschap qgis_process) en bewerkingen uit te voeren. Zoals het gebruiken van complexe functies voor totaliseren in het algoritme Bijgewerkte velden via de mogelijkheid van qgis_process zonder een tijdelijk project te moeten maken voor het bewerken van gegevens.

Dit werd mogelijk gemaakt door het Research Institute for Nature and Forest, Vlaamse overheid

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Gebruikersinterface toegevoegd voor definitie van bereik in GDAL Raster Calculator
De GDAL Raster Calculator heeft nu een interface voor gebruikergespecificeerde definitie van bereik, zodat de gebruikers niet langer de criteria `--extent` hoeven te specificeren in geavanceerde opties.

Deze mogelijkheid werd ontwikkeld door [Nicolas Godet](https://github.com/nicogodet)
## Opties voor toepassing en projecten
### Mogelijkheid: Optie toegevoegd voor opslaan geselecteerde component voor GPS in waarden M van geometrie
Deze nieuwe instelling, beschikbaar in het paneel voor de instellingen van GPS, stelt gebruikers in staat de optie voor het maken van geometrieën met waarden M uit de ingebouwde gereedschappen voor loggen van GPS te gebruiken. Dit is van toepassing op zowel objecten die zijn gedigitaliseerd uit logs van GPS, als van de nieuwe functionaliteit \"Loggen naar GeoPackage/SpatiaLite\".

Opties omvatten het opslaan van tijdstempels (als milliseconden vanaf epoch), grondsnelheid, hoogten, richtingen en componenten voor nauwkeurigheid als waarden M.

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: GPS-spoor doellaag maken een expliciete keuze voor de gebruiker maken, onthouden in project
In eerdere uitgaven volgde de doellaag voor nieuw gemaakte GPS-gedigitaliseerde objecten altijd de selectie van de huidige laag. Dat maakte het heel lastig projecten te ontwerpen rondom het digitaliseren van GPS, omdat, elke keer als een gebruiker begon te interacteren met het project, de vastgelegde objecten van GPS onvoorspelbaar zouden worden geplaatst in de beschikbare lagen.

De doellaag voor GPS-objecten is nu een expliciete keuze die door de gebruiker moet worden gemaakt. Een gebruiker kan deze laag instellen en dan doorgaan en interacteren met de rest van hun projectlagen en de garantie hebben dat op elke moment dat zij de acties activeren om GPS-objecten te maken, deze objecten op de juiste laag zullen worden geplaatst. De doellaag wordt opgeslagen in het huidige project, dus opnieuw openen van een eerder project zal automatisch de GPS-doellaag herstellen (wat het gemakkelijker maakt voor staf of scripts om vooraf projecten voor digitaliseren van GPS voor andere gebruikers te maken en er vertrouwen in kunnen hebben dat die in het veld juist zullen werken).

Aanvullende verbeteringen omvatten:
- GPS-doellaag wordt nu automatisch bewerkbaar gemaakt wanneer een object wordt gemaakt, en de gebruiker wordt overeenkomstig in kennis gesteld. Dit volgt de benadering die we gebruiken voor de gereedschappen voor interactief labelen en vermijdt frustratie voor de gebruiker over waarom de objecten eerder niet werden opgeslagen zonder enige notie over het waarom.
- De acties op de werkbalk GPS volgen nu meer intelligenter de status van het project, GPS, en huidige GPS-spoor, zodat acties alleen worden ingeschakeld als zij zin hebben.
- Verbeteringen aan gebruikersinterface en betere helptips

![image23](images/entries/9563911d7eeb4412cd32f237969579aa1ed6aa90.gif)

Dit werd mogelijk gemaakt door NIWA

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Profiel plotten
### Mogelijkheid: Nieuw item Hoogteprofiel voor kaartvenster voor QGIS Quick
Een nieuw item Hoogteprofiel voor het kaartvenster is beschikbaar voor [QGIS Quick](https://api.qgis.org/api/qgsquick.html), wat het mogelijk maakt de gereedschappen voor hoogteprofielen te gebruiken op andere platforms en in toepassingen van mobiel QGIS.

![image24](images/entries/f870a9112a3577742c6f8c6a98b142b23145d525.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Hoogteprofielen plotten in afdruklay-outs 
Het is nu mogelijk om plots van hoogteprofielen op te nemen in afdruklay-outs! Er is een nieuwe knop \"Hoogteprofiel toevoegen\" op de werkbalk, die initieel een lege plot zal maken. Een plot kan worden geïnitialiseerd door te klikken op de knop \"Kopiëren vanuit profiel\" in de eigenschappen van het item Hoogteprofiel - dit zal het hoogteprofiel gebruiken uit het hoofdvenster van QGIS.

Het hoogteprofiel heeft brede opties voor configureren - u kunt specificeren:
- welke lagen moeten worden opgenomen
- tolerantie voor de profielboog
- diagrambereiken (minimum en maximum afstand/hoogte)
- randen en kleuren van diagramgebied
- eigenschappen voor afstand van assen - intervallen voor labels, uiterlijk rasterlijnen, lettertypen, en meer

![image25](images/entries/ca6f01c1c76d7cff23ff8d27492734c74b8c3973.webp)

Dit werd mogelijk gemaakt door [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Browser
### Mogelijkheid: Mogelijkheden voor bewerken en maken van relatie voor gegevensset toegevoegd in Browser
Deze functionaliteit maakt het mogelijk nieuwe ingebedde definities voor relaties te maken in databasebestanden voor databases ESRI FileGeodatabases, GeoPackage, en SQLite.

Verwijderen en aanpassen van bestaande relaties wordt ook ondersteund, de beschikbare functionaliteit kan echter afhankelijk zijn van de beperkingen van de feitelijke indeling van de database.

![image26](images/entries/2e902df01faff7f71bdfe3854c5b1a38e013e8d8.gif)

Dit werd mogelijk gemaakt door Provincie Zuid-Holland

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Verwijderen van Native GeoNode Provider
De Native GeoNode Provider is verwijderd uit QGIS en is in plaats daarvan nu beschikbaar als een [plug-in](https://geonode.org/QGISGeoNodePlugin/).

Deze wijziging is vanwege de uitbreiding van de API's voor plug-ins om de noodzakelijke functionaliteiten te ondersteunen, zoals Databronnen beheren, en werd uitgevoerd in lijn met [QEP 262](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/262).

Deze mogelijkheid werd ontwikkeld door [Giovanni Allegri](https://github.com/giohappy)
### Mogelijkheid: In Databronnen beheren, gebruikers toestaan direct een laag XYZ toe te voegen zonder eerst een verbinding te moeten maken
Gebruikers mogen nu direct een laag XYZ-tegel toevoegen in Databronnen beheren, zonder eerst een nieuwe verbinding te moeten maken.

Dit staat gebruikers toe om gemakkelijk ad-hoc XYZ-lagen toe te voegen aan hun kaart, zonder hun lijsten met opgeslagen verbindingen te vervuilen.

![image27](images/entries/1e5a07f058db3b16265d94f6e535ac7c79664bcd.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: SQL loggen voor OGR Provider
Omdat GDAL nu loggen van callbacks van queries ondersteunt voor op SQLite-gebaseerde lagen, biedt QGIS deze functionaliteit aan voor het loggen van queries in de gereedschappen voor debuggen van QGIS.

Dit is beschikbaar voor op OGR-gebaseerde  gegevensbronnen van SQLite (SpatiaLite/ GPKG).

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti](https://github.com/elpaso)
### Mogelijkheid: Ondersteuning voor S3 Cloud Storage
S3 compatibele opslag in de cloud, zoals AWS S3 en MinIO, worden nu ondersteund als een methode voor toegang tot en opslaan van externe bestanden, beschikbaar gemaakt door de gebruikersinterface voor externe opslag te gebruiken in de cloud voor opslag van bijlagen.

Een nieuwe methode voor Auth in QGIS, genaamd \"AWS S3\", wordt verschaft om het verbinden met services met het protocol S3 te ondersteunen.

Dit werd mogelijk gemaakt door Métropole Grand Lyon\*\*

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://github.com/Djedouas)
### Mogelijkheid: Resolutie herkennende WMTS-lagen met automatisch opschalen
QGIS staat WMTS-lagen nu toe om rekening te houden met de schermresolutie van het apparaat, of dots per inch (DPI), en de resolutie voor de tegel op te schalen op schermen met hoog DPI.

Een nieuw combinatievak is toegevoegd in de nieuwe dialoogvensters voor WMS- en WMTS-servers voor het configureren van de WMTS-tegel pixelverhouding. Dit stelt QGIS in staat om automatisch het op- en neerschalen af te handelen van tegels die worden opgehaald van de service, gebaseerd op de gerenderde DPI.

Onthoud dat inschakelen van gladde pixmap transformatie wordt aanbevolen als het automatisch opschalen actief is

![image28](images/entries/a921de87af46b4774b94bd632e704527f840ea55.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Verwijderen niet onderhouden provider SAGA uit installaties van QGIS
Deze provider wordt niet meer onderhouden en werkt niet met nieuwere versies van SAGA. Gebruikers worden aangeraden de plug-in van 3e-partij \"Processing Saga NextGen\" in plaats daarvan te gebruiken.

Na vele jaren van discussie is het voor de ingebouwde provider tijd om te vertrekken!

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verbeterde ondersteuning voor lagen met onbekend type geometrie voor provider WFS
De provider van QGIS WFS is verbeterd om in het antwoord van het verzoek GetCapabilities te zoeken (indien WFS 2.0 wordt gebruikt) of de uitgebreide filterfuncties `IsPoint`, `IsCurve`, `IsSurface` aanwezig zijn.

Wanneer een dergelijke laag wordt toegevoegd aan het project, wordt een dialoogvenster \"Toe te voegen items selecteren\" weergegeven.

Dit stelt de gebruiker in staat om een of meerdere lagen te selecteren naast typen `NoGeometry`, `MultiPoint`, `MultiCurve`, `MultiSurface`, `GeometryCollection`.

![image32](images/entries/2068734219e240ca90b22435ca1381f3c8e4b9ef.webp)

Dit werd mogelijk gemaakt door [Duitse QGIS gebruikersgroep](https://qgis.de)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://github.com/rouault)
## QGIS Server
### Mogelijkheid: Omgevingsvariabele QGIS_APPLICATION_FULL_NAME
Deze wijziging definieert de methode `QgsApplication::applicationFullName()` voor gebruik met PostgreSQL `application_name` en QGIS Server loggen.

Voor QGIS Server mag de `QGIS_SERVER_APPLICATION_NAME` worden gespecificeerd in plaats van en zal voorrang hebben boven de instelling `QGIS_APPLICATION_FULL_NAME`.

De waarde mag ook worden gespecificeerd in de variabele `/qgis/application_full_name` in het configuratiebestand van QGIS Server.

Standaard zal deze waarde worden gedefinieerd door de waarde van `QgsApplication::applicationName()+' '+QgsApplication::platform()`.

Dit werd mogelijk gemaakt door [3liz](https://3liz.com)

Deze mogelijkheid werd ontwikkeld door [rldhont](https://github.com/rldhont)
### Mogelijkheid: Ondersteuning voor GeoJSON voor WFS DescribeFeatureType
Ondersteuning voor JSON is toegevoegd als een indeling voor de uitvoer voor verzoeken DescribeFeatureType naar de QGIS Server WFS. Hoewel er geen expliciete stipulatie bestaat in de specificaties van WFS, maakt deze functionaliteit antwoorden mogelijk die overeenkomen met andere providers van de service WFS, zoals GeoServer.

Dit werd mogelijk gemaakt door [Kristianstads kommun](https://www.kristianstad.se/)

Deze mogelijkheid werd ontwikkeld door [David Marteau](https://github.com/dmarteau)
## Plug-ins
### Mogelijkheid: Regels voor Topologie controle in-/uitschakelen en filteren
De plug-in Topology checker is verbeterd om functionaliteit te verschaffen voor het beter beheren van regels, als ook het filteren van grote sets fouten. Aanvullende verbeteringen brengen de gebruikerservaring meer in lijn met de laatste uitgaven van QGIS en maken verbetering van de productiviteit mogelijk, zoals verwijderen in bulk en uitschakelen van regels.

Het dialoogvenster van Topology checker heeft nu keuzevakken die zijn verbonden met individuele regels, die het mogelijk maken de regels in/uit te schakelen bij het uitvoeren van controles op geldigheid *zonder ze te hoeven verwijderen*. Dit vermijdt scenario's waar gebruikers geen regels willen verliezen, maar alleen zijn geïnteresseerd in het valideren van een subset.

Het Topologie controlepaneel  heeft ook een nieuw combinatievak onder zijn werkbalk om snel filteren op fouten mogelijk te maken om gebruikers te kunnen laten focussen op een specifiek type fout, hoewel het zal doorgaan met het standaard weergeven van alle typen fouten.

![image29](images/entries/52e54d9f31a12f024d3c452ecbc77fb3278c18e4.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
## Programmeerbaarheid
### Mogelijkheid: Verbeteringen QgsExifTools
Nieuwe functionaliteit is toegevoegd aan de klasse QgsExifTools, inclusief:
- De functies `readTag()` en `readTags()` ondersteunen nu Xmp-metadatatags
- Een nieuwe functie `tagImage()` kan worden gebruikt om individuele tags voor metadata toe te voegen aan een bepaalde afbeelding, die kunnen worden gebruikt in aanvulling op de al bestaande functie `geoTagImage()`

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://github.com/nirvn)
### Mogelijkheid: Updates voor automatisch aanvullen slimme haakjes voor codebewerkers
Eerdere uitgaven van QGIS bevatten een instelling `autoCloseBracket` voor de Python Console, die een aantal beperkingen in zijn gedrag had. En inclusief dat deze beperkt was tot het gebruiken binnen de Python Console en de interfaces van de Scriptbewerker.

Updates aan de instellingen voor automatisch aanvullen breiden deze functionaliteit uit naar andere interfaces voor codebewerkers, zoals de Expressiebewerker, Project Macrobewerker en de Scriptbewerker. Het gedrag van `autoCloseBracket` is ook aangepast om het gedrag van moderne IDE's na te bootsen, en een instelling `autoSurround` is toegevoegd om geselecteerde tekst te omsluiten bij het gebruiken van de volgende tekensets:
- haakjes/ gekrulde haakjes: `{}`
- vierkante/ vak haakjes: `[]`
- haakjes/ ronde haakjes: `()`
- dubbel aanhalingsteken: `"`
- enkel aanhalingsteken: `'`
- accent grave: `\``
- asterisk: `*`

Met uitzondering van de tekens accent grave en asterisk, is de functionaliteit autoCloseBracket beschikbaar bij het omsluiten van nieuwe gegevens zonder een actieve selectie van tekst.

De configuratie voor automatisch aanvullen wordt standaard ingeschakeld voor nieuwe uitgaven, maar een nieuwe interface voor instellingen wordt verschaft voor nauwkeuriger beheer door gebruikers.

![image30](images/entries/2ed531d2789b12d258d1503c8fb74e396f06e63d.webp)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Mogelijkheid: Actie \"Opmerking schakelen\" toegevoegd aan de geïntegreerde Python-console
De acties Opmerking en Opmerking uitschakelen van de ingebedde Python-bewerker zijn vervangen door een actie Opmerking schakelen, die nu ook beschikbaar is in de Script-bewerker van Processing. 

Dit brengt de gebruikerservaring voor de bewerker in lijn met andere IDE's, zoals VSCode, die de mogelijkheid voor het schakelen van opmerkingen toestaan.

De standaard sneltoets voor deze actie is ingesteld op `Ctrl+:`

De actie Opmerking schakelen is ook beschikbaar in **Project Macro** en **Expressie-bewerkers**. Dit is echter alleen beschikbaar met de sneltoets `Ctrl+:` en bevat niet de actieknop in de gebruikersinterface.

![image31](images/entries/fb255d60095471377459f1c6907df83e6f54bea4.gif)

Deze mogelijkheid werd ontwikkeld door [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Task: take into account GDT_Int8 | [#50907](https://github.com/qgis/QGIS/issues/50907) | [PR #51586](https://github.com/qgis/QGIS/pull/51586) | [PR #51602](https://github.com/qgis/QGIS/pull/51602) |
| Task: take into account GDT_Int8 | [#50907](https://github.com/qgis/QGIS/issues/50907) | [PR #51587](https://github.com/qgis/QGIS/pull/51587) | N/B |
| MultiLineString from OpenFileGDB Disappears on Zoom | [#32534](https://github.com/qgis/QGIS/issues/32534) | [GDAL PR 7137](https://github.com/OSGeo/gdal/pull/7137) |  |
| DATETIME: Wrong timezone for UTC in attribute table | [#48393](https://github.com/qgis/QGIS/issues/48393) | [PR #51625](https://github.com/qgis/QGIS/pull/51625) | [PR #51645](https://github.com/qgis/QGIS/pull/51645) |
| distutils is deprecated but still used | [#51532](https://github.com/qgis/QGIS/issues/51532) | [PR #51630](https://github.com/qgis/QGIS/pull/51630) | [PR #51644](https://github.com/qgis/QGIS/pull/51644) |
| Importing Data into a QGIS Created File Based Geodatabase | [#51435](https://github.com/qgis/QGIS/issues/51435) | <https://github.com/nyalldawson/QGIS/pull/36> | N/B |
| Importing Data into a QGIS Created File Based Geodatabase | [#51435](https://github.com/qgis/QGIS/issues/51435) | [GDAL PR 7147](https://github.com/OSGeo/gdal/pull/7147) | [GDAL PR 7176](https://github.com/OSGeo/gdal/pull/7176) |
| OGCAPI Features url of collection with dot | [#51663](https://github.com/qgis/QGIS/issues/51663) | [PR #51671](https://github.com/qgis/QGIS/pull/51671) | [PR #51987](https://github.com/qgis/QGIS/pull/51987) |
| CityGML Import not working with LoD2 files | [#51647](https://github.com/qgis/QGIS/issues/51647) | [GDAL PR 7168](https://github.com/OSGeo/gdal/pull/7168) | N/B |
| Broken layers when creating new table on GPKG created by third party | [#51721](https://github.com/qgis/QGIS/issues/51721) | [GDAL PR 7174](https://github.com/OSGeo/gdal/pull/7174) | N/B |
| \"Save Layer Edits\" after \"Add Polygon Feature\" deletes added polygons when the objects have no attributes | [#51247](https://github.com/qgis/QGIS/issues/51247) | [GDAL PR 7184](https://github.com/OSGeo/gdal/pull/7184) | [GDAL PR 7188](https://github.com/OSGeo/gdal/pull/7188) |
| gis transforming coordinates incorrectly | [#51792](https://github.com/qgis/QGIS/issues/51792) | [proj PR 3621](https://github.com/OSGeo/PROJ/pull/3621) | N/B |
| Some versions of QGIS can\'t parse mixed-dtype-columns in GeoJSON | [#51911](https://github.com/qgis/QGIS/issues/51911) | Geen: alleen onderzoek & voorlopige poging tot repareren |  |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](https://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Add Row does not work with postgres identity columns that have many characters | [#51563](https://github.com/qgis/QGIS/issues/51563) | [PR #51641](https://github.com/qgis/QGIS/pull/51641) | [PR #52059](https://github.com/qgis/QGIS/pull/52059) |
| If some layers are not identifyable, QGIS Server WMS \"GetFeatureInfo\" returns LayerNotQueryable | [#51613](https://github.com/qgis/QGIS/issues/51613) | [PR #51646](https://github.com/qgis/QGIS/pull/51646) (tests only, cannot reproduce) | N/B |
| Research and diagnosys on: Bug or new behaviour on default fields values on QGIS 3.28.X | [#51543](https://github.com/qgis/QGIS/issues/51543) | Asked feedback to the original developer of the \"feature\" |  |
| \[ogr provider\] Saving big CSV edit is very slow when the whole file has to be updated (such as adding a new field) | [#51668](https://github.com/qgis/QGIS/issues/51668) | [PR #51686](https://github.com/qgis/QGIS/pull/51686) | [PR #51700](https://github.com/qgis/QGIS/pull/51700) |
| Vector data - Graduated Symbology - Legend Format - Only use upper limit | [#51691](https://github.com/qgis/QGIS/issues/51691) | [PR #51692](https://github.com/qgis/QGIS/pull/51692) | [PR #51696](https://github.com/qgis/QGIS/pull/51696) |
| Weird interval QgsDoubleSpinbox behavior in graduated symbology with fixed interval | [#51687](https://github.com/qgis/QGIS/issues/51687) | [PR #51714](https://github.com/qgis/QGIS/pull/51714) | Nee |
| Project predefined scales are trimmed at thousand separator after project restart/reopening properties | [#51735](https://github.com/qgis/QGIS/issues/51735) | [PR #51749](https://github.com/qgis/QGIS/pull/51749) | [PR #51766](https://github.com/qgis/QGIS/pull/51766) |
| wms getLegendGraphic call the group and not the layer when many style layers add from browser | [#51759](https://github.com/qgis/QGIS/issues/51759) | [PR #51765](https://github.com/qgis/QGIS/pull/51765) | Nee |
| overlay_intersects\' does not work with WFS-layer | [#51492](https://github.com/qgis/QGIS/issues/51492) | [PR #51773](https://github.com/qgis/QGIS/pull/51773) | [PR #51793](https://github.com/qgis/QGIS/pull/51793) |
| multiedit in attribute table not working properly in version \>=3.22 | [#48077](https://github.com/qgis/QGIS/issues/48077) | [PR #51801](https://github.com/qgis/QGIS/pull/51801) | Riskant? |
| Key/Value expression constraint is not updated | [#51791](https://github.com/qgis/QGIS/issues/51791) | [PR #51804](https://github.com/qgis/QGIS/pull/51804) | [PR #51811](https://github.com/qgis/QGIS/pull/51811) |
| Float fields created in ArcGIS are converted into Real 12, 11 - Precision is too high | [#51849](https://github.com/qgis/QGIS/issues/51849) | Won\'t Fix |  |
| CSV datasource not converted from 3.16 to 3.22 correctly - projects not usable anymore | [#48587](https://github.com/qgis/QGIS/issues/48587) | [PR #51881](https://github.com/qgis/QGIS/pull/51881) | [PR #51950](https://github.com/qgis/QGIS/pull/51950) |
| Changes on geometry get discarded on save edits when layer filter is enabled (gpkg layer) | [#51934](https://github.com/qgis/QGIS/issues/51934) | Werkt bij mij wel |  |
| If a widget default value is setup as NULL then it\'s not working as it\'s overriden by database column default | [#51818](https://github.com/qgis/QGIS/issues/51818) | Won\'t Fix (probably: still debating) |  |
| Can\'t use raster Unique values symbolgogy for Integer rasters with a single value of 1 | [#51822](https://github.com/qgis/QGIS/issues/51822) | [PR #51975](https://github.com/qgis/QGIS/pull/51975) | [PR #51979](https://github.com/qgis/QGIS/pull/51979) |
| PyQGIS QgsPolygon creation crashes | [#51978](https://github.com/qgis/QGIS/issues/51978) | [PR #52004](https://github.com/qgis/QGIS/pull/52004) | NOG TE DOEN |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Area Simplify drops Z and M values | [#50742](https://github.com/qgis/QGIS/issues/50742) | [PR #51695](https://github.com/qgis/QGIS/pull/51695) | [PR #51742](https://github.com/qgis/QGIS/pull/51742) |
| NULL Value is displayed as NULL html link in the File widget | [#50892](https://github.com/qgis/QGIS/issues/50892) | [PR #51770](https://github.com/qgis/QGIS/pull/51770) | [PR #51775](https://github.com/qgis/QGIS/pull/51775) |
| Vertex Editor table shows incorrect columns in QGIS 3.28 | [#51433](https://github.com/qgis/QGIS/issues/51433) | [PR #51774](https://github.com/qgis/QGIS/pull/51774) | [PR #51986](https://github.com/qgis/QGIS/pull/51986) |
| Copying fetures to PostgreSQL layer not copying same name attribute value | [#51121](https://github.com/qgis/QGIS/issues/51121) | Won\'t Fix |  |
| Crash when switching style to point displacement from geometry generator | [#51070](https://github.com/qgis/QGIS/issues/51070) | [PR #51784](https://github.com/qgis/QGIS/pull/51784) | NOG TE DOEN |
| Fix trust parameter not saved and not read | niet gerapporteerd | [PR #51854](https://github.com/qgis/QGIS/pull/51854) | NOG TE DOEN |
| North Arrow Decoration: file selector for custom SVG does not work correctly | [#51850](https://github.com/qgis/QGIS/issues/51850) | [PR #51882](https://github.com/qgis/QGIS/pull/51882) | [PR #51949](https://github.com/qgis/QGIS/pull/51949) |
| Filter dialog for vector layers in edit state can still be opened via the filter icon in the layers menu | [#51816](https://github.com/qgis/QGIS/issues/51816) | [PR #51884](https://github.com/qgis/QGIS/pull/51884) | [PR #51990](https://github.com/qgis/QGIS/pull/51990) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Julien Cabieces](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| CI fails upon touching src/test/qgistest.h | [#51917](https://github.com/qgis/QGIS/issues/51917) |  |  |
| TestQgsTileDownloadManager::testIdleThread is unstable | [#48927](https://github.com/qgis/QGIS/issues/48927) | [PR #51916](https://github.com/qgis/QGIS/pull/51916) |  |
| Crash on exit with static `QgsCoordinateReferenceSystem` | [#51893](https://github.com/qgis/QGIS/issues/51893) | [PR #51891](https://github.com/qgis/QGIS/pull/51891) | [PR #51954](https://github.com/qgis/QGIS/pull/51954) |
| Allow to skip PostgreSQL backend dependent tests at runtime | [Discussion in PR #51891](https://github.com/qgis/QGIS/pull/51891#discussion_r1109132667) | [PR #51910](https://github.com/qgis/QGIS/pull/51910) | N/B |
| Do not discard geometry attributes having no SRID | [#49380](https://github.com/qgis/QGIS/issues/49380#issuecomment-1282913470) | [PR #51885](https://github.com/qgis/QGIS/pull/51885) | [PR #51997](https://github.com/qgis/QGIS/pull/51997) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Sandro Santilli (strk)](https://strk.kbt.io/)
### Mogelijkheid: Reparaties van problemen door Jean Felder
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| wms getcapabilities crashes on dimensional data if there are no values | niet gerapporteerd | [PR #51930](https://github.com/qgis/QGIS/pull/51930) | [PR #51933](https://github.com/qgis/QGIS/pull/51933) |
| \[3D\] Fix Y-Z inversion in point3dsymbolwidget | niet gerapporteerd | [PR #51855](https://github.com/qgis/QGIS/pull/51855) | [PR #51938](https://github.com/qgis/QGIS/pull/51938) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jean Felder](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Jacky Volpes
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Missing \"Save style\...\" icon in Layer Style Panel | [#51515](https://github.com/qgis/QGIS/issues/51515) | [PR #52037](https://github.com/qgis/QGIS/pull/52037) | Riskant? |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Jacky Volpes](https://oslandia.com/)
### Mogelijkheid: Reparaties van problemen door Stefanos Natsis
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Drag and drop point clouds from the browser add the layer twice | niet gerapporteerd | [PR #51685](https://github.com/qgis/QGIS/pull/51685) |  |
| Opening more than 16 vector layers at once causes crash | niet gerapporteerd | [PR #51782](https://github.com/qgis/QGIS/pull/51782) |  |
| Crash when try to split line by point | [#51501](https://github.com/qgis/QGIS/issues/51501) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| QGIS 3.26 crashes when performing \"split with line\". | [#50948](https://github.com/qgis/QGIS/issues/50948) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| Cannot split line geometry at vertex if the geometry has Z dimension | [#49403](https://github.com/qgis/QGIS/issues/49403) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| Current implementation of multiple-layer style paste doesn\'t work for the command menu \"Layer / Paste Style\". | [#25214](https://github.com/qgis/QGIS/issues/25214) | [PR #51799](https://github.com/qgis/QGIS/pull/51799) |  |
| Copy attribute / Copy feature attributes doesn\'t return value if value is URI | [#26899](https://github.com/qgis/QGIS/issues/26899) | [PR #51803](https://github.com/qgis/QGIS/pull/51803) |  |
| Split tool tries to split even without any digitized points | niet gerapporteerd | [PR #51831](https://github.com/qgis/QGIS/pull/51831) | [PR #51955](https://github.com/qgis/QGIS/pull/51955) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Stefanos Natsis](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix using interpolated line symbol layer for polygon outlines | Niet gerapporteerd | [PR #52030](https://github.com/qgis/QGIS/pull/52030) | [PR #52032](https://github.com/qgis/QGIS/pull/52032) |
| \[processing\] Don\'t raise uncaught exceptions when trying to generate GDAL commands for invalid layers | [#51958](https://github.com/qgis/QGIS/issues/51958) | [PR #51994](https://github.com/qgis/QGIS/pull/51994) | [PR #52001](https://github.com/qgis/QGIS/pull/52001) |
| Don\'t use scientific notation when generating gdal_translate command from georeferencer | [#51813](https://github.com/qgis/QGIS/issues/51813) | [PR #51993](https://github.com/qgis/QGIS/pull/51993) | [PR #52071](https://github.com/qgis/QGIS/pull/52071) |
| Immediately apply color ramp label precision and suffix changes when auto apply is checked | Niet gerapporteerd | [PR #51989](https://github.com/qgis/QGIS/pull/51989) | Niet van toepassing |
| \[processing\] Fix exception when setting output files in batch processing after removing rows | [#51664](https://github.com/qgis/QGIS/issues/51664) | [PR #51988](https://github.com/qgis/QGIS/pull/51988) | [PR #51998](https://github.com/qgis/QGIS/pull/51998) |
| \[processing\] Gracefully handle algorithms with no provider set | [#51971](https://github.com/qgis/QGIS/issues/51971) | [PR #51985](https://github.com/qgis/QGIS/pull/51985) | [PR #51999](https://github.com/qgis/QGIS/pull/51999) |
| Nan z values should not be clipped from rendered geometries | [#51796](https://github.com/qgis/QGIS/issues/51796) | [PR #51984](https://github.com/qgis/QGIS/pull/51984) | [PR #51996](https://github.com/qgis/QGIS/pull/51996) |
| Don\'t try to download whole COG locally in order to determine open options | Niet gerapporteerd | [PR #51982](https://github.com/qgis/QGIS/pull/51982) | Niet van toepassing |
| Fix loss of first color for lineburst symbol layers in GUI | [#51942](https://github.com/qgis/QGIS/issues/51942) | [PR #51952](https://github.com/qgis/QGIS/pull/51952) | [PR #51968](https://github.com/qgis/QGIS/pull/51968) |
| Fix inefficient vector iteration when no rule based rules match current map scale | Niet gerapporteerd | [PR #51904](https://github.com/qgis/QGIS/pull/51904) | Niet van toepassing |
| Fix logic for triggering a full model reset in attribute table after changing attributes | Niet gerapporteerd | [PR #51890](https://github.com/qgis/QGIS/pull/51890) | [PR #51892](https://github.com/qgis/QGIS/pull/51892) |
| Fix placement of perimeter labels with HTML formatting enabled | [#51829](https://github.com/qgis/QGIS/issues/51829) | [PR #51840](https://github.com/qgis/QGIS/pull/51840) | [PR #51868](https://github.com/qgis/QGIS/pull/51868) |
| Fix data loss in secondary geometry columns when displaying in attribute form | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51863](https://github.com/qgis/QGIS/pull/51863) | Niet van toepassing |
| Fix data loss when layers with secondary geometry columns are used in processing tools | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51846](https://github.com/qgis/QGIS/pull/51846) | Niet van toepassing |
| Correctly handle geometry value conversion for geometry fields | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51845](https://github.com/qgis/QGIS/pull/51845) | [PR #51859](https://github.com/qgis/QGIS/pull/51859) |
| Show an icon for geometry fields | Niet gerapporteerd | [PR #51844](https://github.com/qgis/QGIS/pull/51844) | Niet van toepassing |
| Fix geometry fields incorrectly show as \"range\" types in fields list | Niet gerapporteerd | [PR #51842](https://github.com/qgis/QGIS/pull/51842) | [PR #51860](https://github.com/qgis/QGIS/pull/51860) |
| Ensure correct crs is available for QgsMapCanvas for slots connected to extentsChanged when canvas CRS is changed | [#51833](https://github.com/qgis/QGIS/issues/51833) | [PR #51841](https://github.com/qgis/QGIS/pull/51841) | [PR #51873](https://github.com/qgis/QGIS/pull/51873) |
| Fix array_remove_all behavior when removing null values from array | [#51820](https://github.com/qgis/QGIS/issues/51820) | [PR #51838](https://github.com/qgis/QGIS/pull/51838) | [PR #51869](https://github.com/qgis/QGIS/pull/51869) |
| Use a better approach to update virtual layer queries which doesn\'t lose all the layer\'s properties | [#51118](https://github.com/qgis/QGIS/issues/51118) | [PR #51780](https://github.com/qgis/QGIS/pull/51780) | [PR #51872](https://github.com/qgis/QGIS/pull/51872) |
| \[layouts\] Use nicer number formatting for dynamic map scale labels | [#51764](https://github.com/qgis/QGIS/issues/51764) | [PR #51768](https://github.com/qgis/QGIS/pull/51768) | Niet mogelijk |
| Re-permit format_number to omit group separators | Niet gerapporteerd | [PR #51761](https://github.com/qgis/QGIS/pull/51761) | [PR #51763](https://github.com/qgis/QGIS/pull/51763) |
| Remember the collapsed state of the vector layer renderer group box | Niet gerapporteerd | [PR #51719](https://github.com/qgis/QGIS/pull/51719) | Niet van toepassing |
| When unchecking render layers as a group, ensure child layers don\'t have clipping blend modes | [#51358](https://github.com/qgis/QGIS/issues/51358) | [PR #51707](https://github.com/qgis/QGIS/pull/51707) | Te indringend |
| Fix incorrect georeferencing of images | [#51699](https://github.com/qgis/QGIS/issues/51699) | [PR #51705](https://github.com/qgis/QGIS/pull/51705) | [PR #51736](https://github.com/qgis/QGIS/pull/51736) |
| Fix crash when showing tooltips for invalid layers | Niet gerapporteerd | [PR #51703](https://github.com/qgis/QGIS/pull/51703) | [PR #51708](https://github.com/qgis/QGIS/pull/51708) |
| Fix map tips do not show for vector layers where the HTML map tip option isn\'t used | Niet gerapporteerd | [PR #51702](https://github.com/qgis/QGIS/pull/51702) | Geen invloed |
| Fix creation of GeoPDF with exported themes containing slashes | [#51480](https://github.com/qgis/QGIS/issues/51480) | [PR #51633](https://github.com/qgis/QGIS/pull/51633) | [PR #51677](https://github.com/qgis/QGIS/pull/51677) |
| Avoid redo-ing the legend symbol hit test for legend edits which won\'t affect the legend symbols visible in a map | [#51455](https://github.com/qgis/QGIS/issues/51455) | [PR #51681](https://github.com/qgis/QGIS/pull/51681) | [PR #51738](https://github.com/qgis/QGIS/pull/51738) |
| Optimise legend filter by map/expression calculations | [#51233](https://github.com/qgis/QGIS/issues/51233) | [PR #51675](https://github.com/qgis/QGIS/pull/51675) | Te riskant |
| \[georeferencer\] Fix warning about missing output file name doesn\'t show in all circumstances | Niet gerapporteerd | [PR #51673](https://github.com/qgis/QGIS/pull/51673) | [PR #51739](https://github.com/qgis/QGIS/pull/51739) |
| Ensure using \@geometry/@feature variables trigger geometry fetching in expression calculation | [#50791](https://github.com/qgis/QGIS/issues/50791) | [PR #51655](https://github.com/qgis/QGIS/pull/51655) | [PR #51678](https://github.com/qgis/QGIS/pull/51678) |
| Fix generation of raster elevation profiles for exactly horizontal/vertical lines | [#51196](https://github.com/qgis/QGIS/issues/51196) | [PR #51637](https://github.com/qgis/QGIS/pull/51637) | [PR #52072](https://github.com/qgis/QGIS/pull/52072) |
| Percent encode text values when creating/updating fields on ArcGIS feature services | [#51509](https://github.com/qgis/QGIS/issues/51509) | [PR #51636](https://github.com/qgis/QGIS/pull/51636) | [PR #51654](https://github.com/qgis/QGIS/pull/51654) |
| Fix drag and drop to GDB results in columns shifted by on | [#51435](https://github.com/qgis/QGIS/issues/51435) | [PR #51634](https://github.com/qgis/QGIS/pull/51634) | [PR #51969](https://github.com/qgis/QGIS/pull/51969) |
| Expose option for irregular time steps when exporting map animations | [#51546](https://github.com/qgis/QGIS/issues/51546) | [PR #51632](https://github.com/qgis/QGIS/pull/51632) | [PR #51638](https://github.com/qgis/QGIS/pull/51638) |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)
### Mogelijkheid: Reparaties van problemen door David Signer
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| WMS legend symbol missing for \"Meters at Scale\" symbology and projected CRS | [#50366](https://github.com/qgis/QGIS/issues/50366) | [PR #52015](https://github.com/qgis/QGIS/pull/52015) |  |
| Attribute table form view looses index when a layer depending on changed | [#43902](https://github.com/qgis/QGIS/issues/43902) | [PR #52046](https://github.com/qgis/QGIS/pull/52046) |  |
| Attribute table form view looses index when the \"yellow\" selection is changed | niet gerapporteerd | [PR #52045](https://github.com/qgis/QGIS/pull/52045) |  |
| Features in Relation Editor are not selectable anymore | niet gerapporteerd | [PR #51914](https://github.com/qgis/QGIS/pull/51914) | Geen invloed |

Dit werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://qgis.org/)

Deze mogelijkheid werd ontwikkeld door [David Signer](https://opengis.ch/)

{{<content-end >}}
