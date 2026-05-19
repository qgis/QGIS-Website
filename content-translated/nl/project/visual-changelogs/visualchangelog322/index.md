---
HasBanner: false
draft: false
releaseDate: 22-10-2021
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.22
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.22{#changelog322 }
![image1](images/projects/badbeb89221e014ed31e7ea07919c9e734df39b2.png)

Datum uitgave 22-10-2021

QGIS 3.22 Białowieża is aimed at celebrating the 100-year anniversary of [Białowieża National Park](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_National_Park), Poland, which was established in 1921. [Białowieża Forest](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_Forest) is one of the world's last primary woodlands, located on the border between Poland and Belarus. It is one of the few natural old-growth forests in temperate lowland Europe and has been protected for over 600 years. The outstanding value of Białowieża Forest has been acknowledged by its recognition as a [UNESCO Natural World Heritage Site](https://whc.unesco.org/en/list/33).

Białowieża Forest is named after the village Białowieża, which is located right in the middle of this woodland. It is one of the oldest settlements in the area, nowadays hosting numerous research and tourism activities. Today, there are three research institutions in the village: [Białowieża Geobotanical Station, University of Warsaw](https://bsg.bialowieza.pl/en/), [The Mammal Research Institute, Polish Academy of Sciences](https://ibs.bialowieza.pl/en/), and the [Forest Research Institute, Department of Natural Forests](https://www.ibles.pl/en/web/guest/home). Additionally, a large number of scientists from Poland and abroad travel to Białowieża in order to carry out their studies, and as such, there are also other users of QGIS in the area, as well as additional projects which contribute to the Open Data and Open Source Software ecosystems, such as the [Open Forest Data](https://openforestdata.pl/) project.

You can learn more about the project and this release of QGIS at the dedicated project website, <https://qgisbialowieza.pl>.

This feature-packed release includes a vast number of user experience enhancements and controls added to various advanced functionalities. In addition to a host of additional mesh functionality and operational improvements, QGIS Desktop now includes annotation tools and support for annotation layers, amongst much, much more. For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video at <https://youtu.be/U-RHBt6WZi8>

We willen nogmaals onze grote dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen) om deze uitgave mogelijk te maken. Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere manier betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [QGIS.ORG](https://www.qgis.org) en help een handje!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official project sustaining member, please visit our [sustaining member page]({{< ref "/funding/membership.md" >}}) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Annotaties
### Mogelijkheid: Eigenschappen en effecten van laag met Annotaties
Aanvullende eigenschappen voor lagen van annotaties bevatten nu het volgende:
- Een venster voor de eigenschappen van de laag met annotaties, dat enige basisinformatie over de laag bevat en opties om schaalbereiken, transparantie, Mengmodus en tekeneffecten voor de laag in te stellen
- An option to view the main annotation layer\'s properties via the annotation toolbar (the main annotation layer is the hidden layer which is always present above all other map layers, so it\'s impossible to open it\'s property window via the layer tree)
- Options to set an annotation layer\'s opacity/blend mode/paint effect in the layer styling dock for interactive changes

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Knopen bewerken in een item Annotatie
Het gereedschap voor het aanpassen van annotaties kan nu worden gebruikt om knopen in een item Annotatie te bewerken door te klikken boven een bestaande knoop en die te verplaatsen. De interacties van de gebruiker volgen de standaardpatronen voor QGIS als volgt:
- Klikken met links om het verplaatsen te beginnen
- Tweede keer met links klikken voor toepassen van de wijzigingen
- Met rechts klikken om te annuleren
- Een knoop selecteren en drukken op Delete zal de knoop verwijderen
- Dubbelklikken op een segment zal een knoop toevoegen

![image2](images/entries/4510afc65b63bab4ab46e0408a6c4c4207aff40f.gif)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Geselecteerde annotatie verplaatsen met de cursortoetsen
Als een item voor annotatie is geselecteerd kan het worden verplaatst door te drukken op de cursortoetsen.

Deze functionaliteit bevat de mogelijkheid om sneltoetsen voor het toetsenbord op een manier te gebruiken die hetzelfde patroon voor interactie volgt als die, welke worden gebruikt voor lay-outitems:
- `shift + cursor`: Big movement
- `alt + cursor`: 1px movement

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Gereedschap voor het maken van lijn-/ polygoon-items voor annotaties
Functies voor het maken van nieuwe lijn- en polygoon-items voor annotaties zijn toegevoegd aan de gereedschappen voor annotaties.

Deze ondersteunen dezelfde interacties als voor het tekenen van vectorobjecten, zoals snappen, traceren, cad dock, backspace om punten te verwijderen en modi voor het digitaliseren van stromen, en andere.

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Nieuw gereedschap voor tekst op punt
Voor kaartgereedschappen is een framewerk gemaakt om nieuwe items voor annotaties te maken, inclusief de mogelijkheid om nieuwe items voor annotaties voor tekst op punten te kunnen maken.

![image3](images/entries/4822b0a64c8a57a049ae15acb8c77a27709172d5.gif)

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Werkbalk Annotaties
Een nieuwe werkbalk Annotaties is toegevoegd die acties voor de volgende mogelijkheden biedt:
- Een nieuwe lege laag met annotaties maken in het huidige project.
- The \"Modify Annotations\" tool, which provides an interface for editing existing annotations.

De ondersteunde bewerkingen voor de mogelijkheid voor het aanpassen van annotaties omvatten:
- Klikken op een bestaande annotatie om die te selecteren om de eigenschappen weer te geven in het dock Laag opmaken, inclusief symbool, verwijzingsschaal, Z-index, etc.
- Met links klikken op een geselecteerd item voor annotatie om te beginnen met het te verplaatsen. Een klik met rechts of Escape annuleert de verplaatsing, waar een tweede klik met links de verplaatsing zal bevestigen.
- Drukken op de toets Delete, terwijl een annotatie is geselecteerd, zal die annotatie verwijderen

Dit werd mogelijk gemaakt door de Zwitserse QGIS gebruikersgroep.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Kaartgereedschap
### Feature: Add a \"measure bearing\" map tool
This tool behaves similarly to the existing \"measure angle\" map tool, but requires the user only to click two points on the map and displays the bearing between these points.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Gebruikersinterface
### Mogelijkheid: Schakelen tussen bewerken op meerdere geselecteerde lagen
The *toggle editing* action has been modified to support activation on all selected layers, making it easy to start and stop editing sessions across multiple layers simultaneously. Although the editing session status for all selected layers may not be the same, all selected layers will be toggled to an active or inactive state as the inverse of the current state of the currently active layer. This functionality is applied to the menu item *Layer \> Toggle Editing*, the *Toggle Editing* button on the digitizing toolbar, and the *Toggle Editing* entry in the layers context menu.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Mogelijkheid: Groepen van lagen en alle geselecteerde lagen identificeren
Whilst the identify features tool supported multiple selection modes, the \"current layer\" mode has been extended to support the selection of layer groups, and will identify features from all selected layers. Only features from visible layers within a layer group will be identified.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add a \'Show in Files\' action for all file items in browser
Opent een venster voor bestanden en selecteert direct het bestand

Also fixes the existing \"File Properties\" action so that it shows regardless of the file type, and doesn\'t show incorrectly in some circumstances.

![image4](images/entries/f80090adb3c2f85fa81b5689741afd936f8d5439.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Symbologie
### Mogelijkheid: Aangepaste eenheden voor de geometriegenerator van symboollagen
Geometriegeneratoren geven gebruikers nu een optie om te selecteren in welke eenheden zouden moeten worden gebruikt om geometrieën terug te geven, in plaats van alleen de eenheden te ondersteunen die zijn gedefinieerd in het laag-CRS. Dit is in het bijzonder nuttig in situaties waar het symbool niet is geassocieerd met een laag, zoals wanneer gebruikt in lay-outitems.

Het bijwerken biedt de volgende keuzes voor eenheden:
- Kaarteenheden (het standaard, eerdere gedrag)
- Millimeters
- Pixels
- Inches
- Punten

When millimeters, pixels, inches or points are selected, then the \@map_geometry variable will be available for use within the expression, containing the feature geometry in the specified units (relative to the map frame), whilst the \$geometry variable remains available within the expression in the layer CRS map units.

![image5](images/entries/d1c6b0c69cf9dd8247d1dc0e370d0182b550f48a.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Verwijzingsschaal voor Symbologie van vectorlagen
Een optie kan worden weergegeven die het mogelijk maakt verwijzingsschalen voor symbologieën van objecten op vectorlagen te configureren.

In de praktijk definieert dit de relevante kaartschaal waarmee de geconfigureerde grootten van symbologie en label kunnen worden verwezen naar op papier gebaseerde eenheden, zoals millimeters of punten. Deze grootten van eenheden zullen dan automatisch overeenkomstig op schaal worden gebracht, gebaseerd op de verhouding van de relevante verwijzingsschaal en de schaal van de huidige kaartweergave.

Wanneer bijvoorbeeld een lijnlaag is geconfigureerd om een 2 mm brede lijn te gebruiken met een verwijzingsschaal van 1:2000, zou het object worden gerenderd met 4 mm brede lijnen op een kaartschaal van 1:1000, of van 1 mm met een kaartschaal van 1:4000.

Dit werd mogelijk gemaakt door North Road, met dank aan SLYR

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Filteroptie Draai kleuren om voor renderen van rasters
Het is nu mogelijk de kleuren van een raster dat moet worden gerenderd om te draaien via een nieuwe optie Draai kleuren om. Dit kan handig zijn in een aantal gevallen. Bijvoorbeeld, een lichte raster basiskaart kan snel worden omgeschakeld naar een donkere basiskaart zonder de noodzaak om een nieuwe raster gegevensset te moeten maken.

![image6](images/entries/0fc6bce9e9240b7e354b84d7477439798fd64a59.gif)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Labelen
### Mogelijkheid: Eenheid specificeren voor gedefinieerde data-bepaalde rotatie voor labels
Specificeer de eenheid voor de hoek voor gedefinieerde data-bepaalde rotatie voor labels

![image](images/entries/126294292-06c91bd5-83d2-4d6f-88a2-38fa2d303c86.webp)

![Peek 2021-08-29 14-38](images/entries/131250678-52360214-31a9-4cf9-ad84-b10a4f78c431.gif)

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Mazen
### Mogelijkheid: Nieuwe laag met mazen maken
QGIS ondersteunt nu het maken van nieuwe lagen met mazen.

Het maken van mazen ondersteunt de volgende bewerkingen voor het maken:
- Nieuwe lege laag met mazen
- Nieuw frame voor mazen, gebaseerd op een bestaande laag met mazen binnen het project
- Nieuw frame voor mazen, gebaseerd op een bestaande laag met mazen uit een bestand

![image9](images/entries/8ba4033bf4f8eea7e3776db420b34d6c51358859.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Bewerken van frame van lagen met mazen
QGIS ondersteunt nu het bewerken van het frame van lagen met mazen, wat de mogelijkheid ondersteunt om te zorgen voor consistentie van mazen en de mogelijkheid verschaft om bewerkingen ongedaan te maken en opnieuw uit te voeren.

This introduces the `QgsMeshEditor` class to the QGIS Python API, which allows for performing edit operations, and the QgsTopologicalMesh class which is not exposed to the Python API but is used for ensuring that edited mesh elements remain topologically correct and perform data modifications.

![image10](images/entries/71bed70b1ced3fef5e3b8190cc613f3cb60f0fac.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Levenscyclus voor bewerken van frame van lagen met mazen
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

Bewerken van framewerk voor lagen met mazen ondersteunt nu een volledige set van functionaliteiten voor het beheren van de levenscyclus voor bewerkingen, inclusief beginnen, toepassen, terugdraaien en annuleren, soortgelijk aan vectorlagen.

![image11](images/entries/9463f4559796ff4808fcd05d1ffbec3aa6d6bae4.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Gereedschap Bewerken kaart met mazen
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools.

Het gereedschap voor het bewerken van lagen met mazen ondersteunt nu de volgende bewerkingen:
- Punten/zijden toevoegen
- Punten/zijden selecteren
- Punten/zijden verwijderen
- De waarden Z van punten wijzigen
- Punten verplaatsen
- Werken met randen
- Zijden splitsen

![image12](images/entries/ce164b754aff6438bb6db52a4d5c2eb3e103af62.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Verbeteringen aan het gevorderd bewerken van lagen met mazen
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

De gebruikersinterface van QGIS verschaft Delaunay-triangulatie en functies voor het verfijnen van zijden, die toegankelijk zijn vanuit het contextmenu in de kaart wanneer punten en/of zijden zijn geselecteerd in een laag met mazen. Deze opties kunnen worden toegewezen aan knoppen op de werkbalk Laag met mazen als meer functionaliteit is geïntroduceerd.

![mapToolrefine](images/entries/125721486-055c4cc3-5309-4455-bc5c-e00d6f349bc4.gif)

De QGIS API is ook uitgebreid om het gevorderd bewerken van lagen met mazen te ondersteunen, wat werd geïntroduceerd door een nieuwe abstracte klasse voor de interface QgsMeshAdvancedEditing. Afgeleide klassen van deze klasse kunnen worden geïmplementeerd om enig gevorderd bewerken van een laag met mazen mogelijk te maken: genereren van zijden om aan de laag met mazen toe te voegen, bepaalde bewerking op veel zijden of punten. Het gevorderd bewerken is mogelijk gemaakt door het doorgeven van een instantie van QgsMeshAdvancedEditing aan de instantie QgsmeshEditor, en het bewerken wordt toegepast net als andere bewerkingen.

Twee functies voor gevorderd bewerken zijn geïmplementeerd in deze mogelijkheid:
- Delauney triangulatie
- Zijden verfijnen

![image14](images/entries/a914bfb8a85bf2ab2232e8bfad6c3af3cdd751cb.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Bewerkbare elementen van mazen selecteren per polygoon
Gebruikers kunnen nu elementen van mazen selecteren binnen een gedigitaliseerd gebied bij het uitvoeren van bewerkingen aan lagen met mazen. Elk punt van de polygoon wordt gedigitaliseerd met een klik met links, terwijl met rechts klikken zal voltooien en de polygoon valideren om kruisende elementen van mazen (zijden en punten) te selecteren. Gebruiken van de toets Backspace zal de gebruiker toestaan het laatste punt te verwijderen, en de toets Escape maakt het voor gebruikers mogelijk terug te keren naar de normale modus voor digitaliseren.

Deze  functie ondersteunt twee modi voor gedrag met verschillende predicaten voor selecteren en wel als volgt:
- Elkaar rakende elementen (standaard), of gedeeltelijk opgenomen/kruisende elementen zullen worden geselecteerd (groen elastiek).
- Omsloten, of volledig opgenomen elementen zullen worden geselecteerd (blauw elastiek).

![image15](images/entries/6a687b260a4d3a41c432360336393ee2746997c8.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Elementen van lagen met mazen selecteren met bestaande geometrieën
Twee acties zijn toegevoegd voor het selecteren van elementen van lagen met mazen vanuit aanwezige geometrieën in bestaande vectorlagen.

Na het selecteren van geometrieën van een vectorlaag, kan de gebruiker deze gereedschappen gebruiken om elementen van lagen met mazen te selecteren met de predicaten voor rakend en omsloten.

![image16](images/entries/4a918fc1feabd7e3c68282b1b6d052c8504d6013.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Elementen van lagen met mazen met expressie selecteren 
An interface has been created for selecting mesh elements by expression during mesh editing. In addition, a contextual expression function `$face_area` has been added that returns the area of a mesh face.

![image17](images/entries/141acf32014c3ce387ff61e39cabf3e04c6d3896.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Enkel punt transformeren
Een nieuwe modus voor bewerken voor het gereedschap voor het transformeren van de laag met mazen, maakt het voor de gebruiker mogelijk om de coördinaten van één enkel geselecteerd punt te importeren.

De knop voor het gereedschap aan de rechterbovenzijde van het venster Punten van mazen transformeren schakelt deze modus en elke keer als één enkel punt is geselecteerd, zal het automatisch de beschikbare velden voor de gebruiker vullen om de coördinaten van het punt overeenkomstig aan te kunnen passen.

![image18](images/entries/2148b3024a51a218bafafbbe26f74c30692222f6.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Laag met mazen opnieuw indexeren/hernummeren
Gebruikers kunnen nu de zijden en punten van een laag met mazen opnieuw indexeren  (of hernummeren)  tijdens het bewerken. Het hernummeren is een optimalisatie van de mazen met het algoritme Cuthill-McKee.

![image19](images/entries/5da7e6705568488c08fbf7faaf311b2eca46c9da.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Mazen forceren bij polylijnen
Bij het bewerken van objecten van mazen kunnen gebruikers nu objecten transformeren door ze te forceren zich te conformeren aan een door bestaande polylijnen gedefinieerd oppervlakte, of breuklijnen, dat is, randen van zijden die worden tegengekomen moeten een van die lijnen zijn. Gebruikers kunnen geometrieën voor breuklijnen selecteren en dan de aangewezen knop gebruiken om de kruisende elementen van mazen te transformeren.

Opties die voor het transformeren worden verschaft, omvatten:
- Toevoegen van nieuwe punten als de lijnen de interne randen doorsnijden
- Interpoleren van de waarde Z van  nieuw gemaakte punten op de laag met mazen of vanuit de lijnen
- Instelling voor tolerantie voor het naar hun plek verplaatsen van bestaande punten en voorkomen dat nieuwe punten langs de lijn worden gemaakt binnen de gespecificeerde afstand

![forceByBreakLine](images/entries/132239197-096d733b-b519-4aab-9384-79724fd84331.gif)

Whilst the term \"break lines\" is typically used to refer to polylines that constrain a surface or TIN to the defined positions, these break lines are often components of the mesh itself, and additional operations would continue to constrain the surface to these lines. This functionality specifically transforms the surface in a static manner, so that future operations are not constrained to the lines used to transform the mesh elements.

![image21](images/entries/704c731583ce48d963fe9878177bc40639ae3078.webp)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Lagen met mazen met expressie transformeren
User can perform geometrical transformations on a mesh using an expression to change the vertices\' coordinates. All coordinates (X,Y,Z) of selected vertices can be calculated with an expression, allowing transformation of the mesh while the mesh is still valid.

With a valid expression, selecting the \"Preview transform\" option will calculate the new expression based mesh coordinates and identify whether the transform is valid and may be applied.

Als het voorbeeld groen is is de getransformeerde laag met mazen geldig en kan de gebruiker de transformatie toepassen. Als het voorbeeld rood is is de getransformeerde laag met mazen ongeldig en kan de gebruiker de transformatie niet toepassen.

Eenmaal toegepast hebben gebruikers de optie om de bewerking ongedaan te maken of opnieuw toe te passen.

![image22](images/entries/04937a2d9bba1e27712351f52e6b6f4d5fc0be4d.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Renderen
### Mogelijkheid: Gebruiken fysieke DPI voor kaartvenster toestaan
Een nieuwe instelling is beschikbaar gemaakt voor het correct gebruiken van de fysieke schermresolutie DPI in plaats van logische DPI, wat het mogelijk maakt symbolen gelijk te renderen op verschillende aangesloten apparaten (hoge DPI en lage DPI), en in mobiele toepassingen, zoals QField.

Deze instelling is standaard uitgeschakeld om er voor te zorgen dat symbolen niet anders op schaal worden gebracht dan dat zij in eerdere versies van QGIS waren.

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
### Mogelijkheid: Data-bepaalde doorzichtbaarheid rasterlagen
Een nieuw besturingselement wordt weergegeven dat het mogelijk maakt de doorzichtbaarheid van een raster data-bepaald te maken. Dit maakt een gevarieerde weergave van een rasterlaag mogelijk, in verschillende contexten, zoals op verschillende pagina's van een atlas, niet afhankelijk zijnde van de zichtbaarheid van een andere laag, of aangepast door variabelen voor Tijdbeheer, etc.

Additionally, a \"redraw layer only\" temporal mode for raster layers has been added, which causes a raster layer to be redrawn on each new animation frame as in the equivalent functionality for vector layers. This may be useful in many contexts, such as when the layer uses time-based expression values like the data defined renderer opacity to fade in or out a raster layer from an animation.

![image23](images/entries/881acd52afafba75698f1d7668794b80b594baef.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## Afdruklay-outs
### Mogelijkheid: Ondersteuning voor vooraf gedefinieerde schalen op punten gebaseerde Atlassen
Lay-out kaartitems hebben ondersteuning verkregen voor de modus voor vooraf gedefinieerd op schaal brengen indien beheerd door op punten gebaseerde atlassen. Dit zorgt er voor dat het juiste gedrag wordt waargenomen als objecten van Atlas multipunt geometrieën zijn met variërende enveloppe-gebieden.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Inspringen voor groepen en subgroepen van Legenda
Two new entries have been added to the \"Spacing\" section of the Legend properties:
- Inspringen van groepitems
- Inspringen van subgroepitems

Items die behoren tot groepen of subgroepen zullen naar rechts worden verschoven met de gespecificeerde hoeveelheid. Indien modelvormen voor de Legenda links van de items worden toegevoegd, zullen die ook inspringen.

![image24](images/entries/3792e9ae5124b81f1b4289cab220fdbb237851a8.webp)

This feature was developed by [Jürnjakob Dugge](https://github.com/jdugge)
## Expressies
### Feature: Mesh expression functions for vertex_as_point and vertex_z
Expressies zijn toegevoegd voor interactie met lagen met mazen, met de volgende functies die de waarde teruggeven die is gerelateerd aan het huidige punt:
- `$vertex_as_point`: returns the current vertex as a geometry point
- `$vertex_z`: returns the Z value of the current vertex.

These two functions are contextual and need to be added in a `QgsExpressionContext` with `QgsExpressionContextUtils::meshExpressionScope()` for the creation of a specific `QgsExpressionScope`.

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Expression function for \$z
The z value for the current feature in an expression context can now be retrieved using `$z`

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Expressie voor Affiene transformatie
An affine_transform function has been added to QGIS Expressions.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Mogelijkheid: Expressie voor Straight distance2d
A straight_distance2d function is now available in QGIS expressions for retrieving the direct/ Euclidean distance between the first and last vertex of a curve geometry feature.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Mogelijkheid: Expressie sinuosity  toegevoegd
Een functie sinuosity is toegevoegd aan de QGIS expressies.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: New exif() and exif_geotag() functions
Een nieuw paar functies werd toegevoegd aan de QGIS expressies om de tags EXIF te lezen vanuit afbeeldingsbestanden. De twee functies zijn:
- exif(path, tag) : this function returns the value of a given tag string for the provided image file path; when the second optional parameter isn\'t provided, the function will return a map object containing *all* exif tags and their values.
- exif_geotag(path) : this function returns a point geometry from the exif geotags containing in the provided image file path.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Digitaliseren
### Mogelijkheid: Geoptimaliseerd algoritme voor snappen aan geometrie
Snappen aan geometrie is nu verbazingwekkend snel nadat een andere ronde voor het optimaliseren van het algoritme is uitgevoerd. Kleine waarden voor afstanden voor snappen, die QGIS lang bezig hielden, is nu verleden tijd.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Naar boog converteren met gereedschap Punten
The ability to convert vertices to or from curved vertices is now supported with the Vertex tool, allowing users to convert vertices with the \"C\" and \"O\" keys.

Additionally, methods for `convertVertex()` have been introduced for the `QgsGeometry` and `QgsCompoundCurve` objects in the QGIS API.

![image25](images/entries/fcc006352c7b09e37d6d8511ecb7fe2ae6a8be50.gif)

This feature was funded by [Swiss QGIS user group](https://qgis.ch/)

This feature was developed by [Olivier Dalang](https://github.com/olivierdalang)
### Mogelijkheid: Ondersteuning voor toevoegen van Z/M aan Geavanceerd digitaliseren
De QGIS gereedschappen voor Geavanceerd digitaliseren ondersteunen nu het invoeren van door de gebruiker gedefinieerde waarden Z en M, wat het beschikbare beheren voor nieuwe gedigitaliseerde objecten, zoals componenten van 3D-netwerken, enorm verbeterd.

![image26](images/entries/287d041be909700393995e3018fba76f41e09a67.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## Gegevensbeheer
### Mogelijkheid: Ondersteuning voor slepen en neerzetten voor de bestandswidget Externe opslag
Gebruikers kunnen nu ondersteuning voor slepen en neerzetten gebruiken voor de widget voor een externe bron  als een externe opslag is gedefinieerd en op de juiste wijze is geconfigureerd.

![image27](images/entries/038bb187a174a4c491f3f2db6ef03cec5b75e43d.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Mogelijkheid: Op bestand gebaseerde grootte gegevensset en datum laatste wijziging in het dialoogvenster Laageigenschappen
The layer properties dialog\'s information panel now shows the size and last modified date of file-based datasets, removing the need to retrieve these details from a file manager. These additional details are also visible in the browser panel\'s information section. For datasets formed of more than a single file, the size will reflect the sum of all the auxiliary/ sidecar files forming the dataset.

![image28](images/entries/10c72ab958bb1e7a59f8f81afb81d33780ed0834.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Bestanden hernoemen in QGIS Browser
Een actie voor hernoemen is toegevoegd aan het submenu Beheren voor bestanden in de QGIS Browser. Als het hernoemde bestand correspondeert met een ruimtelijke gegevensset met meerdere hulp- /toegevoegde bestanden, dan zullen die overeenkomstig worden hernoemd.

Aanvullend worden gebruikers gewaarschuwd als het ebstand ene laag is die bestaat in het huidige project en worden gevraagd of zij automatisch alle paden voor de laag overeenkomstig willen bijwerken.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move GPS tools \"add gpx layer\" functionality to Data Source Manager
Functionality from the GPS tools plugin to add GPX layers has been moved to a new \"Add GPS Data\" page in the data source manager.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Projecten vanuit GPKG laden met slepen en neerzetten
In het verleden werden, met de functionaliteit slepen en neerzetten in de indeling GPKG, alleen lagen met objecten weergegeven om te worden geladen in QGIS.

QGIS zal nu projecten die zijn ingebed in een GPKG weergeven als het bestand van GPKG is toegevoegd aan het kaartvenster van QGIS met de functionaliteit slepen en neerzetten.

![image29](images/entries/3672e8bb8d50bf1593252343da8fd8ff78a46535.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ondersteuning voor externe opslag
QGIS now includes an External Storage API, in line with the proposal outlined in [QEP 196](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/196).

De implementatie omvat de volgende mogelijkheden:
- API voor Externe opslag
- Register dat alle apparaten voor externe opslag bevat
- SimpleCopy externe opslag dat de geselecteerde externe bron opslaat op een specifieke locatie op de schijf
- Ondersteuning voor WebDAV

In aanvulling daarop is een widget toegevoegd om het configureren en visualiseren van apparaten voor externe opslag en componenten mogelijk te maken. De widget voor de modus van opslag (Bestand of Map) is momenteel niet zichtbaar wanneer een externe opslag wordt geselecteerd, en instellingen voor relatieve paden zijn verborgen omdat relatieve paden niet relevant zijn voor gegevens van externe opslag.

![image30](images/entries/c16663cabec529b113bb73919141bf50bf142c9e.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Formulieren en widgets
### Mogelijkheid: Acties voor formulieren in Ontwerper Slepen en neerzetten
Acties voor lagen zijn nu zichtbaar in formulieren met de Ontwerper Slepen en Neerzetten

![image31](images/entries/d8af279071ac38fdc63fbd3980077155db39bd0f.gif)

This feature was funded by [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Legenda van laag
### Mogelijkheid: Pictogram plaatsvervanger gebruiken in Legenda voor rasterlagen
Een nieuwe mogelijkheid is toegevoegd om mogelijk te maken dat een plaatsvervangende afbeelding wordt geselecteerd die kan worden gebruikt in het item voor de Legenda van een raster- of vectorlaag. Dit is bijzonder handig in bepaalde gevallen, zoals bij het gebruiken van rasterlagen met QGIS Server, wat lange lijsten van gestapelde waarden uit verzoeken GetLegendGraphic voorkomt en in plaats daarvan een resultaat op maat teruggeeft, naast verschillende andere gevallen voor gebruik.

![image32](images/entries/f06524b9f422ee1ced55d9d79b816cabc5ea212d.webp)

This feature was funded by [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)

This feature was developed by [mhugent](https://github.com/mhugent)
## Analyse-gereedschappen
### Mogelijkheid: Functie if() toegevoegd aan Rasterberekeningen
Een lang verwachte mogelijkheid voor QGIS was om eenvoudige argumenten if() in Rasterberekeningen te ondersteunen.

Hoewel voorwaardelijke argumenten al enige tijd worden ondersteund in Rasterberekeningen, was de syntaxis en structuur van de expressies vaak uitgebreid en complex.

The raster calculator will now support simple conditional statements with the common syntax of `if ( condition , option1 , option2 )` whereby if the condition evaluates to true, the first option will be used, otherwise the second option will be used.

![image33](images/entries/c5d6968380879133ddb31ab2d0f755d6d2048402.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
### Mogelijkheid: Ondersteuning voor virtuele rasters in Rasterberekeningen
Ondersteuning voor virtuele raster-gegevensprovider is toegevoegd aan Rasterberekeningen van QGIS, wat gebruikers nu in staat stelt bewerkingen uit te voeren met Rasterberekeningen zonder een uitvoerbestand te moeten specificeren of het resulterende raster naar schijf te moeten schrijven.

This option is enabled via the UI by checking the \"Create on-the-fly raster instead of writing layer to disk\" checkbox in the raster calculator, and is also supported via the PyQgis API.

Resulterende rasterlagen kunnen worden gebruikt voor verdere analysebewerkingen en maakt door de gebruiker gespecificeerde rasternamen mogelijk. Waar geen naam wordt opgegeven voor het resulterende raster, zal die worden benoemd overeenkomstig de formule die werd gebuikt om hem te maken.

![image34](images/entries/844b2b463a26d035fe25d43d7221a24a570ac615.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
## Processing
### Mogelijkheid: Type parameter voor laag met Annotaties voor Processing
Een type parameter voor een laag met Annotaties is toegevoegd aan het framewerk Processing voor QGIS, wat een nieuw algoritme bevat voor het converteren van items van de hoofdlaag voor Annotaties naar de secundaire lagen met annotaties. Dit is nuttig voor het verplaatsen van items die zijn gemaakt in de hoofdlaag naar een secundaire laag, zodat de plaatsing van het item kan worden aangepast in de stapel lagen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Optie POST toegevoegd aan het algoritme FileDownloader voor Processing
Een keuze toegevoegd om te kiezen tussen verzoeken GET of POST bij het downloaden van een bestand met het algoritme FileDownloader van Processing.

Als de parameter POST wordt gespecificeerd, kan enkele DATA worden toegevoegd in de query.

Dit is voor vele contexten nuttig, zoals voor het verzenden van langere verzoeken aan de Overpass API met POST om gegevens van OSM te downloaden.

![image35](images/entries/89bee20177cb03e453300ae291ae879649e963ab.webp)

Dit werd mogelijk gemaakt door [3Liz](https://www.3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Feature: Add new \"Select within distance\" and \"Extract within distance\" algorithms
Nieuwe algoritmes zijn verschaft die het voor gebruikers mogelijk maken om objecten, die binnen een bepaalde afstand van objecten van een andere verwijzingslaag liggen, uit een laag te selecteren of uit te nemen.

Het controleren van de afstand is enorm geoptimaliseerd, met behulp van ruimtelijke indices, om het aantal opgehaalde objecten te beperken, en ook het automatisch afhandelen van de controle naar de server voor de database server voor lagen die de provider PostGIS gebruiken.

Aanvullend, de parameter voor de afstand mag een data-bepaalde eigenschap zijn.

Dit werd mogelijk gemaakt door QTIBIA Engineering

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Parameter Puntenwolk voor Processing
Een nieuwe parameter voor puntenwolken is toegevoegd aan het framewerk Processing van QGIS. Dit maakt het mogelijk lagen met puntenwolken in de kaartlagen te filteren en parameters voor meerdere lagen. Dit opent de deur voor eigen algoritmes voor puntenwolken en verbetert de ondersteuning voor puntenwolken voor 3e partij-providers.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Plug-in GPS importer verwijderd
De laatste van de gereedschappen voor functionaliteit voor GPS is overgebracht naar drie nieuwe algoritmes voor Processing, namelijk:
- GPS-gegevens converteren
- GPS-gegevens uploaden naar een apparaat
- GPS-gegevens vanaf een apparaat downloaden

Als resultaat daarvan is de plug-in GPS overbodig geraakt en is volledig verwijderd uit QGIS.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Algoritme Type GPX-object converteren voor Processing
Het algoritme Type GPX-object converteren is geporteerd van de gereedschappen voor GPS naar een nieuw algoritme voor Processing, dat het programma GPSBabel gebruikt om objecten GPX te converteren van het ene type naar een ander (bijv. converteren van alle objecten waypoint naar een object route).

Het is ontworpen als een  langskomende vervanging voor werkstromen die deze functionaliteit eerder gebruikten vanuit de plug-in GPS tools, maar met alle voordelen en verbeteringen die automatisch voortvloeien uit het deel uitmaken van het framewerk Processing in QGIS.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Ophogend veld met optie Modulo toegevoegd
Dit algoritme maakt het voor de  mogelijk om een kolom toe te voegen met een geheel getal dat zal worden opgehoogd vanaf START tot de grenswaarde, met de mogelijkheid voor groeperen om door te gaan met de waarde van  START volgend op de groep.

An option called \"modulo counter\" is included which will reset the counter to the starting value if the modulo value is reached. Using a value of 0 for the modulo option will disable it.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Mogelijkheid: Parameter Duration
Een hagelnieuwe parameter duration werd toegevoegd aan het framewerk Processing om het maken van aan Tijdbeheer-gerelateerde algoritmes mogelijk te maken.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Tijd-ruimte algoritme ST-DBSCAN clusteren 
QGIS 3.22 bevat een hagelnieuw tijd-ruimte algoritme ST-DBSCAN clusteren dat puntobjecten clustert, gebaseerd op een 2D-implementatie van tijd-ruimtelijk op dichtheid gebaseerd clusteren van toepassingen met ruis algoritme (ST-DBSCAN) .

Bekijk, voor meer details, de volgende papers:
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu, \"A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise\". In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
- Birant, Derya, and Alp Kut. \"ST-DBSCAN: An algorithm for clustering spatial--temporal data.\" Data & Knowledge Engineering 60.1 (2007): 208-221.
- Peca, I., Fuchs, G., Vrotsou, K., Andrienko, N. V., & Andrienko, G. L. (2012). Scalable Cluster Analysis of Spatial Events. In EuroVA@ EuroVis.

![image36](images/entries/10136b7563df169c40e2c20a96fe75b6ed93e16f.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
### Mogelijkheid: Niet eigen providers voor Processing verplaatsen naar onafhankelijke plug-ins
In line with the discussion in [QEP 226](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/226), the SAGA, GRASS, and OTB providers have been separated into independent plugins.

Dit zou problemen moeten voorkomen met het laden van de plug-in Processing in gevallen waar één van deze providers defect is. Het zal het ook eenvoudiger maken ze te converteren naar derde-partij-plug-ins in de toekomst.

De plug-ins SAGA en GRASS worden standaard ingeschakeld, wat de ervaring voor de gebruiker ongewijzigd laat. De provider OTB kan, indien nodig, worden ingeschakeld in Plug-ins beheren en installeren. Echter, het in- of uitschakelen van een van deze providers wordt nu uitgevoerd via Plug-ins beheren en installeren, net zoals voor elke andere plug-in.

Dit is voornamelijk een interne wijziging, met als enige zichtbare verandering aan de zij de van eindgebruikers, dat Plug-ins beheren en installeren wordt gebruikt om de providers SAGA, GRASS en OTB te activeren of te deactiveren.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Opties voor toepassing en projecten
### Mogelijkheid: Alle sneltoetsen voor het toetsenbord exporteren naar XML of PDF
In het verleden zou QGIS, bij het exporteren van sneltoetsen voor toetsenbord naar een bestand XM, alleen gebruiker gedefinieerde sneltoetsen exporteren. In gevallen waarin geen aangepaste sneltoetsen werden gevonden, zou een leeg bestand worden gemaakt.

Een nieuwe optie is verschaft om alle beschikbare sneltoetsen voor het toetsenbord te exporteren naar het resulterende bestand XML, of om een uitvoer als PDF te maken met een lijst van alle gedefinieerde sneltoetsen voor QGIS.

![image37](images/entries/1822a5ace82d1e8030ed3d563c07f6b9b6fc3901.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Mogelijkheid: Widget voor Configuratie voor apparaat voor GPSBabel verplaatst van GPS tools naar de algemene instellingen
De instellingen voor configuratie voor GPSBabel is verplaatst van een pagina in de vervallen plug-in GPS Tools, naar een nieuwe pagina in het dialoogvenster voor de algemene instellingen.

![image38](images/entries/d61c12a455d85b290431d5ff461de15db0afb446.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Standaard padstructuur voor nieuwe projecten instellen
QGIS Desktop ondersteunde in het verleden de definitie of een bepaald project een absolute of relatieve structuur gebruikte vanuit de project-eigenschappen. Echter, de standaard instelling voor deze functionaliteit werd altijd geconfigureerd om relatieve paden te gebruiken.

Een nieuwe instelling, onder de opties voor het programma, wordt weergegeven die het voor gebruikers mogelijk maakt om voor de standaard padstructuur in te stellen of die absolute of relatieve paden gebruikt voor nieuwe projecten. Op nagenoeg dezelfde manier als waarin de standaard projectindeling kan worden geconfigureerd om qgz of qgs te gebruiken, is dit beschikbaar gemaakt als een globale eigenschap, specifiek voor elke gebruikersprofiel.

This feature was developed by [mhugent](https://github.com/mhugent)
### Mogelijkheid: Configuratie van de max cache-grootte in instellingen voor QGIS
In the `qgis_global_settings.ini` file, it\'s possible to set the max image cache size in bytes.

De cache wordt gebruikt voor het cachen van afbeeldingen voor symbologie en lay-outs, Als afbeeldingen met hoge resolutie worden gebruikt voor het afdrukken van een lay-out, dan zou deze waarde overeenkomstig moeten worden verhoogd.

Standaardwaarde is 100 MB.

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [David Marteau](https://github.com/dmarteau)
## Browser
### Mogelijkheid: Verbeterde actie voor verwijderen van bestanden in Browser
De actie Verwijderen die wordt gebruikt in de QGIS Browser is op vele manieren verbeterd, inclusief:
- De actie is meer consistent en kan worden toegepast op items van alle typen bestanden
- Verwijderen van meerdere bestanden wordt nu ondersteund door meerder items te selecteren in de Browser wat ook een prompt voor bevestigen omvat
- Vóór het verwijderen van bestanden wordt het huidige project gescand om te zien of het een van de bestanden gebruikt. Als dat zo is, verschijnt een prompt die de gebruikers vraagt of zij het verwijderen  annuleren, of lagen geheel willen verwijderen, of lagen willen verwijderen en behouden.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Widget voor resultaten van verbindingen API
As a part of the ongoing efforts to port the table management functionalities from the DB Manager to the QGIS Browser, as detailed in [QEP 205](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/205), a new SQL dialog is available from the browser panel which provides the ability to execute queries and SQL statements for the following elements:
- DB-verbindingen
- Items Schema
- Items Tabel

De implementatie ondersteunt ook de volgende gevorderde functionaliteiten:
- Een multi-threaded implementatie voor resultaten van zowel het ophalen van API-token als voor rijen in niet-blokkerende elementen van de gebruikersinterface
- Volledig te onderbreken API
- Ondersteuning voor progressief laden van objecten in de weergave Resultaten (fetchMore API)

![image39](images/entries/a4d260146fe4267a34d9db97495df2b244f5d7ff.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Gegevensproviders
### Mogelijkheid: Transacties in provider MSSQL
Toevoeging van ondersteuning voor transacties voor de gegevensprovider MSSQL.

There are no GUI-related changes, as users can enable transactional editing as with other providers. This is done by going to the Project Properties and checking \"Automatically create transaction groups where possible\" in the Data Sources tab.

Standaard zal een uitgevoerde transactie in MSSQL de toegang tot dezelfde gegevens blokkeren voor andere cliënten. Als bijvoorbeeld één cliënt een transactie begint en een object in een tabel toevoegt of aanpast, zullen andere cliënten worden geblokkeerd indien zij proberen gegevens uit de tabel te lezen, totdat de transactie is voltooid.

There is database-level configuration option, `READ_COMMITTED_SNAPSHOT`, which is `OFF` by default.

Activeren hiervan zal het gedrag veranderen om op eenzelfde manier te functioneren als voor andere RDBMS-systemen, zoals PostgreSQL, in die zin dat transacties geen blokkade veroorzaken en ondersteuning voor de database inschakelen voor meerdere versies van gegevens. Dit is een eigenschap op het niveau van de database, geconfigureerd door de beheerder en kan niet automatisch worden ingesteld door QGIS bij het verbinden met de database, het kan echter worden geactiveerd met de volgende query:
``` sql
ALTER DATABASE my_db SET READ_COMMITTED_SNAPSHOT ON
```
In de meeste gevallen waarin transacties gewenst zijn, is het activeren van deze optie waarschijnlijk aan te bevelen om vastlopen te voorkomen in QGIS of andere cliënten.

This feature was funded by [ms.GIS](http://www.msgis.com)

Deze mogelijkheid werd ontwikkeld door [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Systeem- en interne tabellen weergave bij selecteren van sublaag
Een keuzevak is toegevoegd aan het dialoogvenster voor het selecteren van sublagen om te beheren of systeem- en interne tabellen zouden moeten worden weergegeven. Deze zal standaard uitgeschakeld zijn, maar zou nuttig kunnen zijn in gevallen waar gebruikers een bepaalde behoefte hebben om een systeemtabel in QGIS te laden om te bekijken of voor bewerkingsdoeleinden.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Automatisch metadata uit ESRI Personal Geodatabases lezen en converteren
Eerder werd dit ondersteund voor metadata van File Geodatabases en shp.xml, maar wordt nu ook ondersteund voor ESRI personal geodatabases (.mdb bestanden)

Vereist GDAL 3.4+

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Een algemene gegevens-item provider maken voor alle op bestanden gebaseerde databronnen
Deze provider gebruikt de QgsProviderRegistry::querySublayers API om automatisch toepasselijk gegevensitems voor de Browser te maken voor alle op bestanden gebaseerde bronnen, ongeacht de onderliggende provider, of dat nu mdal, gdal, ogr, pdal, of .ept is.

Dit maakt het mogelijk bronnen samen te voegen die kunnen worden afgehandeld door meerdere, verschillende  providers naar enkele container-items in de Browser, die kan worden uitgebreid om alle gerelateerde of geneste elementen weer te geven. Het komt voor vele typen bestanden, zoals bestanden van GeoPDF of KML/KMZ, vaak voor dat zij raster- en vectorlagen bevatten, of bestanden .nc waartoe toegang kan worden verkregen als laag met mazen of als raster, afhankelijk van de gegevensprovider.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
## QGIS Server
### Mogelijkheid: Meerdere MetadataUrls inschakelen
QGIS Server ondersteunde in het verleden alleen het verschaffen van één enkele metadata URL, maar zal nu het in de servicedefinitie specificeren van meerdere eindpunten voor metadata toestaan.

![image40](images/entries/8e644bb4823b8da291e1e2b2dd1ca472d3d57246.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: Versie toevoegen aan gereedschappen CLI voor QGIS Server
It\'s quite a common practice to have arguments like `-v` and `--version` for tools accessed via command line interfaces (CLIs), so new `--version` and it\'s alias `-v` have been added to identify QGIS version information for the following tools:
- qgis_process
- qgis_mapserv.fcgi
- qgis_mapserver

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
## Programmeerbaarheid
### Mogelijkheid: Scriptbare vectortegel coderen weergeven
An additional `writeSingleTile` method in `QgsVectorTileWriter` has been exposed to enable the encoding of a single vector tile to a memory buffer. This may support workflows for PyQgis and QGIS Server which include support for vector tiles.

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Mogelijkheid: Vectortegels in een ander CRS coderen en schrijven dan EPSG:3857
De QGIS API is uitgebreid voor de ondersteuning van het coderen en schrijven van vectortegels in een ander CRS dan EPSG:3857.

Onthoud dat, overeenkomstig de specificatie Mapbox Vector Tile, een Vectortegel gegevens weergeeft, gebaseerd op een vierkant bereik binnen een projectie. Een Vectortegel zou informatie moeten bevatten over zijn grenzen en zijn projectie. De bestandsindeling gaat er van uit dat de decoder de grenzen en projectie van een Vectortegel kent, voordat die wordt gedecodeert.

Dit werd mogelijk gemaakt door Ifremer

This feature was developed by [rldhont](https://github.com/rldhont)
### Mogelijkheid: Filter DistanceWithin voor QgsFeatureRequest
Een optie is toegevoegd aan QgsFeatureRequest om objecten te bevragen die binnen een bepaalde afstand van een verwijzings-geometrie liggen

Dit is mogelijk gemaakt door de nieuwe enum Qgis::SpatialFilterType die is toegevoegd om aan te geven of een verzoek geen ruimtelijk filter gebruikt, een filter BoundingBox (via setFilterRect), of het nieuwe filter DistanceWithin.

Het volgende verzoek zal bijvoorbeeld alle objecten ophalen die binnen 50 kaarteenheden van de opgegeven tekenreeks voor de lijn liggen:
``` python
QgsFeatureRequest().setDistanceWithin(QgsGeometry.fromWkt('LineString(0 0, 10 0, 12 1)'), 50)
```
Filters voor afstand binnen worden behandeld als filters voor begrenzingsvakken, in die zin dat zij onafhankelijk zijn van enig filter voor attribuut/ID (zoals object-ID's of expressies).

Provider feature iterators can potentially delegate the distance within search to the backend. So, for example, the PostgreSQL data provider could use an `ST_DWithin` query for optimal index use.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: API voor voorkeuzen waarden van combinatievak
Een API is toegevoegd om het mogelijk te maken een parameter voor een tekenreeks weer te geven als een combinatievak met vooraf ingestelde keuzes voor Processing in de gebruikersinterface.

In some circumstances, it is desirable to restrict the values available when a user is asked to enter a string parameter that should match a list of predetermined \"valid\" values, yet these values will vary installation by installation.

For example, a \"printer name\" parameter, where it may be desired that users may pick a name value from a list of printers installed on the system, but since the printer names will vary between installations, an enum parameter is not a suitable choice.

This is now supported by setting the \"value_hints\" option in the widget wrapper metadata, as demonstrated below.

Hoewel dit een mechanisme verschaft om de gebruikers te geleiden om geldige waarden tekenreeks te selecteren bij het uitvoeren van een algoritme voor Processing via de gebruikersinterface, plaats het geen beperkingen op geaccepteerde waarden voor de tekenreeksen via codes van PyQGIS of wanneer het algoritme wordt uitgevoerd op andere manieren die niet de gebruikersinterface gebruiken. Algoritmes zouden andere waarde netjes moeten afhandelen.
``` python
param = QgsProcessingParameterString( 'PRINTER_NAME', 'Printer name')
# show only printers which are available on the current system as options
# for the string input.
param.setMetadata( {'widget_wrapper': { 'value_hints': ['Inkjet printer', 'Laser printer'] } })
```
Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://github.com/nyalldawson)
### Mogelijkheid: Klasse QgsExifTools ondersteuning voor ophalen van waarden van tags
De klasse QgsExifTools kan nu individuele tags EXIF ophalen uit afbeeldingen met de functie readTag.

E.g.: `QgsExifTools.readTag('/my/photo/0997.JPG'), 'Exif.Image.DateTime')`

Bekende tags EXIF die tijdwaarden weergeven worden automatisch geconverteerd naar objecten Q{Date,Time,DateTime}. Dit maakt het werken met deze tags veel eenvoudiger en integreert goed met andere delen van de QGIS API.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](https://www.opengis.ch/)
## Belangrijke reparaties
### Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| WFS / GML parse issue, but QGIS loads GML as file fine? | [#45017](https://github.com/qgis/QGIS/issues/45017) | Is geen probleem |  |  |
| POST request to modify timestamp does not respect defined format | [#44990](https://github.com/qgis/QGIS/issues/44990) | Wordt niet gerepareerd / Is geen probleem |  |  |
| Warning message \'Cannot create temporary SpatiaLite cache\' when adding many WFS-layers | [#44971](https://github.com/qgis/QGIS/issues/44971) | Duplicaat |  |  |
| QGIS creates invalid filter for WFS GetFeature request | [#43957](https://github.com/qgis/QGIS/issues/43957) | [PR #45043](https://github.com/qgis/QGIS/pull/45043) | [PR #45053](https://github.com/qgis/QGIS/pull/45053) |  |
| WFS Layer is not rendered when requested CRS is not matching project CRS and \"Only request features overlapping the view extent\" option is set | [#44054](https://github.com/qgis/QGIS/issues/44054) | [PR #45044](https://github.com/qgis/QGIS/pull/45044) | [PR #45047](https://github.com/qgis/QGIS/pull/45047) |  |
| Adding a WFS layer with filter for non-existent attribute leads to broken layer | [#43950](https://github.com/qgis/QGIS/issues/43950) | [PR #45045](https://github.com/qgis/QGIS/pull/45045) | [PR #45052](https://github.com/qgis/QGIS/pull/45052) |  |
| New Shapefile layer silently overwrite existing files | [#44299](https://github.com/qgis/QGIS/issues/44299) | [PR #45207](https://github.com/qgis/QGIS/pull/45207) | [PR #45240](https://github.com/qgis/QGIS/pull/45240) |  |
| QGIS on linux crashes when opening many geopackages at once | [#43620](https://github.com/qgis/QGIS/issues/43620) | [PR #45211](https://github.com/qgis/QGIS/pull/45211) | Nee |  |
| Crash in QgsPointCloudLayerRenderer when closing while rendering still active | [#44144](https://github.com/qgis/QGIS/issues/44144) | [PR #45227](https://github.com/qgis/QGIS/pull/45227) | [PR #45241](https://github.com/qgis/QGIS/pull/45241) |  |
| Geoprocessing tools cause libgeos to throw SIGBUS | [#45226](https://github.com/qgis/QGIS/issues/45226) | [geos PR 481](https://github.com/libgeos/geos/pull/481) | N/B |  |
| QGIS crash after loading WMS layer via script and zooming in and out | [#44095](https://github.com/qgis/QGIS/issues/44095) | [PR #45254](https://github.com/qgis/QGIS/pull/45254) | Nee | Meestal een probleem van gebruiken |
| Integer unexpectedly large in GeoPackage | [#45178](https://github.com/qgis/QGIS/issues/45178) | Is geen probleem |  |  |
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file | [#45139](https://github.com/qgis/QGIS/issues/45139) | [GDAL PR 4552](https://github.com/OSGeo/gdal/pull/4552) | N/B |  |
| WFS connection manager: GetCapabilities document\'s URLs not being used consistently | [#45242](https://github.com/qgis/QGIS/issues/45242) | [PR #45267](https://github.com/qgis/QGIS/pull/45267) | [PR #45273](https://github.com/qgis/QGIS/pull/45273) |  |
| QGIS crashes if network connexion is lost and a raster layer is loaded | [#45293](https://github.com/qgis/QGIS/issues/45293) | [GDAL PR 4560](https://github.com/OSGeo/gdal/pull/4560) | N/B |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| Data Source Manager - ArcGIS REST Server - dialog/window closes when adding a layer | [#45050](https://github.com/qgis/QGIS/issues/45050) | [PR #45059](https://github.com/qgis/QGIS/pull/45059) | Niet beschikbaar |  |
| \"Display no data value as\" option is not available in raster layer properties | [#44949](https://github.com/qgis/QGIS/issues/44949) | [PR #45063](https://github.com/qgis/QGIS/pull/45063) | Niet kritisch |  |
| Raster layer not rendering after data-source change when combined with certain layout element | [#44929](https://github.com/qgis/QGIS/issues/44929) | [PR #45074](https://github.com/qgis/QGIS/pull/45074) | [PR #45083](https://github.com/qgis/QGIS/pull/45083) |  |
| Update selected feature ids before emitting featuresDeleted | [#44921](https://github.com/qgis/QGIS/issues/44921) | [PR #45078](https://github.com/qgis/QGIS/pull/45078) | Niet kritisch |  |
| sample() and identify() from QgsRasterDataProvider don\'t always provide the same value | [#44902](https://github.com/qgis/QGIS/issues/44902) | [PR #45086](https://github.com/qgis/QGIS/pull/45086) | [PR #45145](https://github.com/qgis/QGIS/pull/45145) |  |
| Copying objects containing multiline strings into another project does not work properly | [#44989](https://github.com/qgis/QGIS/issues/44989) | [PR #45129](https://github.com/qgis/QGIS/pull/45129) | Niet kritisch |  |
| projecting label coordinates for multiPoint geometry crashes QGIS | [#45148](https://github.com/qgis/QGIS/issues/45148) | [PR #45150](https://github.com/qgis/QGIS/pull/45150) | Nee |  |
| Copy/paste style category \"Form\" is missing some settings | [#45146](https://github.com/qgis/QGIS/issues/45146) | Maybe won\'t fix, checking with m-kuhn and 3nids |  |  |
| Adding a new point onto a memory multipoint layer kills QGIS | [#45152](https://github.com/qgis/QGIS/issues/45152) | [PR #45157](https://github.com/qgis/QGIS/pull/45157) |  |  |
| Attributes - Update All button - Creates Corrupted Fields - GeoJSON file | [#45139](https://github.com/qgis/QGIS/issues/45139) | [PR #45174](https://github.com/qgis/QGIS/pull/45174) | Nee |  |
| WMS parent layer added via QGIS Browser doesn\'t use default style | [#45192](https://github.com/qgis/QGIS/issues/45192) | [PR #45209](https://github.com/qgis/QGIS/pull/45209) | Nee |  |
| \"Display nodata as\" color widget is not automatically updated in layer styling panel | [#45132](https://github.com/qgis/QGIS/issues/45132) | [PR #45264](https://github.com/qgis/QGIS/pull/45264) | Niet beschikbaar |  |
| PostGIS error while changing attributes (field value and geometry): prepared statement \"updatefeature\" already exists | [#45100](https://github.com/qgis/QGIS/issues/45100) | [PR #45266](https://github.com/qgis/QGIS/pull/45266) | Wachtrij |  |
| Attribute Table in Layout Manager Font Style Override Doesn\'t Show Fields | [#45098](https://github.com/qgis/QGIS/issues/45098) | [PR #45269](https://github.com/qgis/QGIS/pull/45269) | Wachtrij |  |
| WFS Layer from QGIS Server is not rendered because of an issue with coordinate axis order | [#45216](https://github.com/qgis/QGIS/issues/45216) | [PR #45270](https://github.com/qgis/QGIS/pull/45270) | Niet kritisch |  |
| Not rendering with identity transform raster created with rasterio | [#45324](https://github.com/qgis/QGIS/issues/45324) | Gecontroleerd, waarschijnlijk geen probleem |  |  |
| SQL query from DB Manager is executed twice | [#45318](https://github.com/qgis/QGIS/issues/45318) | [PR #45351](https://github.com/qgis/QGIS/pull/45351) | Wachtrij |  |
| can\'t use layers where name starts with number in virtual layer | [#45347](https://github.com/qgis/QGIS/issues/45347) | [PR #45354](https://github.com/qgis/QGIS/pull/45354) | Wachtrij |  |
| Show Feature Count counts null in zero category | [#45280](https://github.com/qgis/QGIS/issues/45280) | [PR #45361](https://github.com/qgis/QGIS/pull/45361) | Wachtrij |  |
| Copying table by Drag&Drop in Browser (2) doesn\'t copy the table structure correctly | [#45286](https://github.com/qgis/QGIS/issues/45286) | [PR #45375](https://github.com/qgis/QGIS/pull/45375) | Nee |  |
| Wrong histogram plot if raster data type is byte | [#45379](https://github.com/qgis/QGIS/issues/45379) | [PR #45400](https://github.com/qgis/QGIS/pull/45400) | Wachtrij |  |
| Inconsistency regarding pattern handling for QgsServerOgcApiHandler | [#45439](https://github.com/qgis/QGIS/issues/45439) | [PR #45450](https://github.com/qgis/QGIS/pull/45450) | Wachtrij |  |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | [PR #45521](https://github.com/qgis/QGIS/pull/45521) | Wachtrij |  |
| projectsInDatabase key is not stored to xml for PostGIS connections | [#45508](https://github.com/qgis/QGIS/issues/45508) | [PR #45523](https://github.com/qgis/QGIS/pull/45523) | Wachtrij |  |
| Changing values in Form mode of attribute table doesn\'t set active the Save button | [#45527](https://github.com/qgis/QGIS/issues/45527) | [PR #45532](https://github.com/qgis/QGIS/pull/45532) | Wachtrij |  |
| Create spatialite trigger with DBManager do not work | [#45420](https://github.com/qgis/QGIS/issues/45420) | [PR #45553](https://github.com/qgis/QGIS/pull/45553) | Nee |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| QGIS 3.20 on Mac crashes when certain Qt signals are emitted | [#44182](https://github.com/qgis/QGIS/issues/44182) | [QGIS-Mac-Packager Commit bf925f311](https://github.com/qgis/QGIS-Mac-Packager/commit/bf925f3118a5d51080dfed46dddcb7cba3bbbc00) | Niet beschikbaar |  |
| Unable to view LAS files written in WGS84 (EPSG:4326) coordinates | [#44755](https://github.com/qgis/QGIS/issues/44755) | duplicate of [#41765](https://github.com/qgis/QGIS/issues/41765) |  |  |
| macOS: Symbol not found: \_\_cg_jpeg_resync_to_restart when reprojecting raster layer with GDAL warp on macOS | [#40164](https://github.com/qgis/QGIS/issues/40164) | nee | nee | Geen probleem meer met de nightly (qgis-deps-0.9) |
| Data Source Manager incorrectly identifies PostGIS raster extent on macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | [PR #45322](https://github.com/qgis/QGIS/pull/45322) | Wachtrij |  |
| icons not visible in the Layer Notes | [#44425](https://github.com/qgis/QGIS/issues/44425) | [PR #45332](https://github.com/qgis/QGIS/pull/45332) | Niet beschikbaar |  |
| unable to open any ascii FLO-2D files in Mesh Layer | niet gerapporteerd | [PR #45349](https://github.com/qgis/QGIS/pull/45349) | Niet beschikbaar |  |
| encoding issue when using GRASS processing tool on macOS | [#41870](https://github.com/qgis/QGIS/issues/41870) | [PR #45399](https://github.com/qgis/QGIS/pull/45399) | Niet kritisch - bestaat een workaround voor |  |
| Matplotlib QT backend imports not working on MacOS | [#45398](https://github.com/qgis/QGIS/issues/45398) | onderzoek |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Reparaties van problemen door Sandro Santilli
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| Make QgsGeos::prepareGeometry and QgsGeos::cacheGeos idempotent | niet gerapporteerd | [PR #45147](https://github.com/qgis/QGIS/pull/45147) |  |  |
| Add a distanceWithin method to the QgsGeometryEngine virtual class | niet gerapporteerd | [PR #45057](https://github.com/qgis/QGIS/pull/45057) |  |  |
| Allow calling testdata_pg.sh from any directory | niet gerapporteerd | [PR #45378](https://github.com/qgis/QGIS/pull/45378) |  |  |
| Make TestPyQgsPostgresProvider.testGeneratedColumns idempotent | niet gerapporteerd | [PR #45415](https://github.com/qgis/QGIS/pull/45415) |  |  |
| Improve PostgreSQL test DB setup documentation and script | niet gerapporteerd | [PR #45413](https://github.com/qgis/QGIS/pull/45413) |  |  |
| Add GEOS DistanceWithin API | [GEOS Ticket #1124](https://trac.osgeo.org/geos/ticket/1124) | [GEOS commit #ba10ba4508a](https://trac.osgeo.org/geos/changeset/ba10ba4508af887a1a78bbc632ab45d89ce3242c/git) | [GEOS Issue #472](https://github.com/libgeos/geos/issues/472) |  |
| Make Postgres provider test idempotent | [#45417](https://github.com/qgis/QGIS/issues/45417) | [PR #45418](https://github.com/qgis/QGIS/pull/45418) |  |  |
| Use GEOSDistanceWithin when available | niet gerapporteerd | [PR #45340](https://github.com/qgis/QGIS/pull/45340) |  |  |
| Reduce GEOS conversions and preparations of geometries | niet gerapporteerd | [PR #45195](https://github.com/qgis/QGIS/pull/45195) |  |  |
| More heuristics to determine whether to iterate over target source | niet gerapporteerd | [PR #45339](https://github.com/qgis/QGIS/pull/45339) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Reparaties van problemen door Loïc Bartoletti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| More const in geometry | Niet gerapporteerd / uitvoering | [PR #45217](https://github.com/qgis/QGIS/pull/45217) |  |  |
| QgsFeature::setId improve documentation with a warning | [#44898](https://github.com/qgis/QGIS/issues/44898) | [PR #45189](https://github.com/qgis/QGIS/pull/45189) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| Geometry Checker: Enlarge FeatureID | [#44250](https://github.com/qgis/QGIS/issues/44250) | [PR #45191](https://github.com/qgis/QGIS/pull/45191) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| VertexTool. Fixes move vertex on Z layer if CRS are differents (with Vincent Cloarec) | Niet gerapporteerd | [PR #45020](https://github.com/qgis/QGIS/pull/45020) | Niet naar oudere versies. Nieuwe methoden geïntroduceerd. |  |
| Fix Z/M dimension URI via DB Manager. | [#34894](https://github.com/qgis/QGIS/issues/34894) | [PR #45223](https://github.com/qgis/QGIS/pull/45223) | [PR #45304](https://github.com/qgis/QGIS/pull/45304) |  |
| \[FIX\] GeometryValidator init curve support | Niet gerapporteerd | [PR #45272](https://github.com/qgis/QGIS/pull/45272) |  |  |
| Compile fails, \'None\' is not a member of \'QgsField::ConfigurationFlags\' | [#44681](https://github.com/qgis/QGIS/issues/44681) | Wordt niet gerepareerd / Is geen probleem |  |  |
| Union fails when using a point and a polygon layer | [#44801](https://github.com/qgis/QGIS/issues/44801) | Verschil tussen GEOS 3.8 en 3.9 |  |  |
| Rings order in MultiPolygon WKT string may leave overlapping parts when deleting holes (native:deleteholes) | [#44424](https://github.com/qgis/QGIS/issues/44424) | Wordt voorlopig niet gerepareerd. We kunnen Geos gebruiken om het probleem op te lossen, maar dat zal Z/M en segmentize arc verwijderen. |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Loïc Bartoletti](https://www.oslandia.com/)
### Reparaties van problemen door Denis Rouzaud
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| Regression: trying to run the multipart to singleparts algorithm throws a python error | [#45331](https://github.com/qgis/QGIS/issues/45331) | [PR #45348](https://github.com/qgis/QGIS/pull/45348) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Denis Rouzaud](https://www.opengis.ch/)
### Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| Styles in database not working for postgres provider and non-geometric layers | [#44749](https://github.com/qgis/QGIS/issues/44749) | [PR #45075](https://github.com/qgis/QGIS/pull/45075) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| \"Layer notes\" icon is not displayed when copy-pasting a style | [#44692](https://github.com/qgis/QGIS/issues/44692) | [PR #45302](https://github.com/qgis/QGIS/pull/45302) | niet nodig |  |
| Ambiguous JSON errors | [#42832](https://github.com/qgis/QGIS/issues/42832) | Kan niet worden gereproduceerd |  |  |
| Attribute table: missing features when copying/pasting from scratch layer | [#42798](https://github.com/qgis/QGIS/issues/42798) | Can't reproduce (Closed) |  |  |
| Form view shows wrong image attachments when scrolling through features | [#42705](https://github.com/qgis/QGIS/issues/42705) | Al gerepareerd |  |  |
| Build Virtual Raster tool creates an additional layer when selecting and reordering layers | [#44270](https://github.com/qgis/QGIS/issues/44270) | [PR #45092](https://github.com/qgis/QGIS/pull/45092) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| Attachment widget options are reset when you reopen the field widget properties | [#45089](https://github.com/qgis/QGIS/issues/45089) | Duplicaat |  |  |
| Cleared feature attributes not acting like they have been cleared, and preventing saving of layer | [#39146](https://github.com/qgis/QGIS/issues/39146) | [PR #45176](https://github.com/qgis/QGIS/pull/45176) | [PR #45292](https://github.com/qgis/QGIS/pull/45292) |  |
| \[Postgres\] default value displayed instead of NULL | [#45198](https://github.com/qgis/QGIS/issues/45198) | [PR #45199](https://github.com/qgis/QGIS/pull/45199) | [PR #45291](https://github.com/qgis/QGIS/pull/45291) |  |
| a feature copy/paste sets a NULL field to its \"default value\" in a geopackage | [#44544](https://github.com/qgis/QGIS/issues/44544) | Vraag: Evalueren we de standaardwaarde voor een veld NULL bij kopiëren-plakken van objecten ? |  |  |
| QGIS expression builder can not resolve PostgreSQL text arrays correctly | [#45290](https://github.com/qgis/QGIS/issues/45290) | [PR #45321](https://github.com/qgis/QGIS/pull/45321) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Julien Cabieces](https://www.oslandia.com/)
### Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) | Opmerking |
| --- | --- | --- | --- | --- |
| Don\'t reset mesh layer styling when changing data source for layer | [#45391](https://github.com/qgis/QGIS/issues/45391) | [PR #45392](https://github.com/qgis/QGIS/pull/45392) | N/B |  |
| Fix crash when rendering clipped features and clipped shape results | [#45190](https://github.com/qgis/QGIS/issues/45190) | [Commit 6a4cdb36](https://github.com/qgis/QGIS/commit/6a4cdb36c91085c5bb1544fb02da1f83467a29d7) | [PR #45422](https://github.com/qgis/QGIS/pull/45422) |  |
| Fix crash when using map label tools with projects containing vector tile layers | [#44486](https://github.com/qgis/QGIS/issues/44486) | [PR #45311](https://github.com/qgis/QGIS/pull/45311) | [PR #45390](https://github.com/qgis/QGIS/pull/45390) |  |
| Fix symbol sizes in Meters at Scale cannot be negative | [#45298](https://github.com/qgis/QGIS/issues/45298) | [Commit 360351a](https://github.com/qgis/QGIS/commit/360351a02704c370545fb8f92c0bdafbdfa35b2e) | Niet geschikt om terug te brengen naar oudere versies |  |
| Fix overwriting default style of geopackage layers | [#42811](https://github.com/qgis/QGIS/issues/42811) | [Commit eef6939b96](https://github.com/qgis/QGIS/commit/eef6939b96407b3d050988be4a0eeb692ffc5b68) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Fix hang when rendering lines with dash patterns with all 0 values | [#41994](https://github.com/qgis/QGIS/issues/41994) | [Commit f4e2e900](https://github.com/qgis/QGIS/commit/f4e2e900eed16633ef0198f7b9a9152f395e173a) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Update default toolbar locations | niet gerapporteerd | [Commit 77be95feac](https://github.com/qgis/QGIS/commit/77be95feac7391e58f6bd487f30e09ed8ed63651) | N/B |  |
| Don\'t overwrite existing data defined property expressions when an interactive map tool is used to move/rotate/edit labels | [PR #45279](https://github.com/qgis/QGIS/pull/45279) | [Commit b30c17f0](https://github.com/qgis/QGIS/commit/b30c17f07d00850597d8bb1b2cfb1f454498b391) | N/B |  |
| Fix crash on exit with CAD dock open | niet gerapporteerd | [Commit 1fb21f69f](https://github.com/qgis/QGIS/commit/1fb21f69fede05cabb8f1d27a8ad24564ae16f3d) | N/B |  |
| Fix rule based symbology doesn\'t work for columns with \'-\' in name | [#44379](https://github.com/qgis/QGIS/issues/44379) | [Commit 51fa9840](https://github.com/qgis/QGIS/commit/51fa9840248135a7fe7ee181b7d645f3c591c9cc) | [Commit 797367dde](https://github.com/qgis/QGIS/commit/797367dde65d6ab06f39f5c4636c2127c67aa9d1) |  |
| Avoid hangs when drawing symbol icons using inappropriate sizes in map units | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45233](https://github.com/qgis/QGIS/pull/45233) | Niet geschikt om terug te brengen naar oudere versies |  |
| Fix inappropriate display of z/m values in cad dock when non-z/m layer is selected | niet gerapporteerd | [Commit 55a76d1d](https://github.com/qgis/QGIS/commit/55a76d1d867c32f52ae4bd38ed671d44aa3ae92e) | N/B |  |
| Implement more responsive cancelation of map render for maps using complex effects | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45212](https://github.com/qgis/QGIS/pull/45212) | Niet geschikt om terug te brengen naar oudere versies |  |
| Allow CAD dock to be used for geographic CRS, but only allow the x/y/z/m constraints to be set | niet gerapporteerd | [PR #45185](https://github.com/qgis/QGIS/pull/45185) | Niet geschikt om terug te brengen naar oudere versies |  |
| Fix crash when opening symbology properties of a layer set to embedded renderer which is not compatible with embedded renderers | [#45159](https://github.com/qgis/QGIS/issues/45159) | [PR #45193](https://github.com/qgis/QGIS/pull/45193) | N/B |  |
| Fix QgsMapToolCapture coordinates when associated with a non-vector layer where the layer CRS != canvas CRS | niet gerapporteerd | [PR #45183](https://github.com/qgis/QGIS/pull/45183) | N/B |  |
| Fix geometry generator rendering outside of vector layers | [#39159](https://github.com/qgis/QGIS/issues/39159) | [PR #45165](https://github.com/qgis/QGIS/pull/45165) | Niet geschikt om terug te brengen naar oudere versies |  |
| Fix color customisation is lost when configuring renderers using geometry generators | [#38377](https://github.com/qgis/QGIS/issues/38377) | [PR #45166](https://github.com/qgis/QGIS/pull/45166) | Niet geschikt om terug te brengen naar oudere versies |  |
| Fix rendering of interpolated line symbol layer outside of vector layers | [#45028](https://github.com/qgis/QGIS/issues/45028) | [PR #45164](https://github.com/qgis/QGIS/pull/45164) | N/B |  |
| Fix QgsGeometry.fromPolygonXY docs | [#45099](https://github.com/qgis/QGIS/issues/45099) | [Commit 3d599fe4](https://github.com/qgis/QGIS/commit/3d599fe4b5574e7c916133171e097163cae51e32) | N/B |  |
| Fix digitizing features using CAD dock when layer CRS != canvas CRS | niet gerapporteerd | [PR #45108](https://github.com/qgis/QGIS/pull/45108) | N/B |  |
| Fix offset background when drawing rotated text | [#44907](https://github.com/qgis/QGIS/issues/44907) | [PR #45425](https://github.com/qgis/QGIS/pull/45425) | In behandeling |  |
| Correctly escape complex source strings in processing history log | [#45403](https://github.com/qgis/QGIS/issues/45403) | [PR #45426](https://github.com/qgis/QGIS/pull/45426) | In behandeling |  |
| Fix handling of ADF files in browser | niet gerapporteerd | [PR #45393](https://github.com/qgis/QGIS/pull/45393) | Niet geschikt om terug te brengen naar oudere versies |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
