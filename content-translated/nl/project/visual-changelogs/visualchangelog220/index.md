---
HasBanner: false
draft: false
releaseDate: '2014-02-22'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 2.2
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 2.2{#changelog22 }
Datum uitgave 22-02-2014

Log met wijzigingen voor de volgende uitgave van QGIS 2.2.0. De nadruk voor deze uitgave ligt meer op het oppoetsen en de uitvoering - we hebben vele nieuwe mogelijkheden, tweaks en verbeteringen toegevoegd om de gebruikersinterface meer consistent te maken en er professioneler uit te laten zien (en hopelijk eenvoudiger te gebruiken). Aan de Printvormgeving (gebruikt voor het maken van afdrukklare kaarten) is heel vele werk verricht om het een meer bruikbaar platform voor het maken van fantastische cartografische uitvoer te maken.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

We willen de ontwikkelaars, schrijvers van documentatie, testers en alle andere vele mensen bedanken die vrijwillig hun tijd en inspanningen bijdragen (of mensen ondersteunen om dat te doen).

Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn in het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

Tenslotte willen we onze officiële sponsoren bedanken voor de onschatbare financiële ondersteuning die zij aan dit project verlenen:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- ZILVEREN sponsor: [Staat Vorarlberg, Oostenrijk](http://www.vorarlberg.at/)
- BRONZEN sponsor: [www.molitec.it, Italië](http://www.molitec.it/)
- BRONZEN sponsor: [www.argusoft.de, Duitsland](http://www.argusoft.de

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Opties voor toepassing en projecten
### Mogelijkheid: Ondersteuning voor maateenheden in nautische mijlen
For you seafaring folks out there, you can now measure distances using nautical miles. To enable this, use the `Settings -> Options -> Map Tools` option panel.

![image1](images/entries/e1115ca7d43ec24fceaee93f976848583148724f.webp)
## Gegevensproviders
### Mogelijkheid; Ondersteuning voor één tot veel-relaties
This release sports the ability to define 1:n relations. The relations are defined in the project properties dialog. Once relations exist for a layer, a new user interface element in the form view (e.g. when identifying a feature and opening its form) will list the related entities. This provides a powerful way to express e.g. the inspection history on a length of pipeline or road segment. You can find out more about relations support [here](http://blog.vitu.ch/10112013-1201/qgis-relations).

![image2](images/entries/0e5e0d1b9dfafe9d64dd5b79866877980f03d099.webp)
### Mogelijkheid: Gereedschap DXF exporteren
A new tool for exporting DXF\'s has been added to the `Project` menu

![image3](images/entries/452e7692b5b8d2704b4d31067265eb71986d969f.webp)
### Mogelijkheid: Plakken als nieuwe vectorlaag
It is a common activity in a GIS to create a sub-selection and then to create a new layer from the selection. In QGIS you can already do `save selection as` to save a layer from your selection, and now offers functionality that allows you to create a new file or memory layer from whatever is in your clipboard. Simply select some features, copy them to your clipboard and then do `Edit -> Paste features as` and choose either `New vector layer` or `New memory layer` from the submenu. The best part of this new feature is that if you have some Well Known Text (WKT) features in your clipboard from another app, you can simply paste them into QGIS as a new layer now.

![image4](images/entries/636db14446809f9e284013113a7b881868591ed3.webp)
### Mogelijkheid: Afbeelding van WMS-legenda weergeven in inhoudsopgave en printvormgeving
Prior to QGIS 2.2 the WMS data provider was not able to display a legend in the table of contents\' layer list. Similarly no legend could be displayed in the map composer. QGIS 2.2 addresses both of these issues.

Clicking on the layer\'s legend will open a frame with the legend at full resolution. The legend will display contextual information based on your current scale. The WMS legend will be shown only if the WMS server has GetLegendGraphic capability. Legend resolution can be modified changing Canvas & Legend options.

![image5](images/entries/6e7cd4849824a802558c0e029f605145d5c885aa.webp)
## Digitaliseren
### Mogelijkheid: Gereedschap voor digitaliseren Ring vullen
This new tool is used to cut holes in polygons and automatically fill them with new features. If you hold down `Ctrl` when finalising the feature, the attributes will be taken from parent feature.

![image6](images/entries/a8c671765578b660cb5d33cca51efa66ecdb17a4.webp)
## Algemeen
### Mogelijkheid: Recente expressies opslaan
De Expressiebouwer zal nu de laatste 20 gebruikte reguliere expressies onthouden.

![image7](images/entries/90a6b4d181fb2dc7699402d17c1f31522c4f3409.webp)
### Mogelijkheid: WKT plakken vanaf klembord
QGIS can now paste and create a new feature based on WKT that is found in the clipboard. Simply copy some WKT and paste into a editable layer. You can also create a new layer by selecting `Edit -> Paste As -> New Memory Layer`
## Printvormgeving
### Mogelijkheid: Verbeteringen aan Zebra-kaartranden
You can now set the colours of the `Zebra` border on the map element in the map composer.

![image8](images/entries/682c36e3ac96b491e2e0a99a7ff9d94b9e0dc4e5.webp)
### Mogelijkheid: Ondersteuning voor roteren van elementen
Elk type element in de Printvormgeving kan nu worden geroteerd, inclusief de schaalbalk, tabellen en legenda. U kunt bijvoorbeeld een label in de kaart zo roteren dat deze beter op de kaart past (zoals geïllustreerd). Het aanpassen van de grootte van geroteerde elementen is ook verbeterd.

![image9](images/entries/700e0999552bc2e2bb2cef86ed14240b05f1da4e.webp)
### Mogelijkheid: Schaal voor Printvormgeving toegevoegd en verbeteringen aan liniaal
The appearance of rulers has been improved by adjusting the scale logic and by adding smaller ruler divisions, and by making vertical rulers use rotated text. There is also a new composer action for hiding/showing rulers. You can now quickly zoom to 100% page scale using the new `Zoom to 100%` tool on the toolbar. The composer window now lets you quickly switch the page scaling via a new scale combobox in the status bar. In addition a new indicator has been added to show you the precise pixel position of your cursor. The `Close` and `Help` buttons have been removed from the bottom of the composer window to give you the maximum amount of screen space for working with your compositions.

![image10](images/entries/8b148acf4ef24204b42f14ee7cec43d57c87911a.webp)
### Mogelijkheid: World-bestand genereren
In the composer you can now create georefenced maps! Simply ensure that you choose the correct map element in the `Composition tab` and then export your map as a PNG file. An accompanying world file will be written, allowing you to load your exported composition in QGIS as a raster layer.

![image11](images/entries/d5887511afbe8379f9e240c3763f6b68766cac88.webp)
### Mogelijkheid: Werken met meerdere items
Support has been added for moving and resizing multiple items simultaneously. You can now hold shift while resizing to maintain an item\'s ratio while resizing, or hold control to resize from the item\'s centre. Shortcut key also apply to moving items, so holding shift while moving an item constrains the movement to horizontal or vertical movement, and holding control temporarily disables item snapping. You can also hold shift while pressing a cursor key to shift all selected items by a larger amount.
### Mogelijkheid: Verbeteringen aan Atlas
You can now preview the individual pages of the map atlas that will be generated in composer. While in atlas preview mode you can output the current page without outputting the entire atlas. You can also tweak the map extent or scale for each feature while previewing the atlas page. Atlas map settings have been moved from the atlas panel to the map properties panel, so now more than one map can be controlled by the atlas generation. There\'s a new option to automatically centre an overview map, which comes in handy when creating atlas based maps. More context information is now available so that you can adjust your symbology based on whether the feature is the current atlas feature or not. See [this article for more info](http://nathanw.net/2013/12/02/waiting-for-qgis-22-highlighting-current-atlas-feature/).

![image12](images/entries/fe668e5f257efec81db855a91fc7d6febc221261.webp)
### Mogelijkheid: Verbeterd selecteren voor item
You can now select more then one item by clicking and dragging a box to select them, and there\'s shortcuts for adding to a selection (holding shift while dragging), subtracting from a selection (hold control while dragging) and switching to \"within\" selection mode (hold alt while dragging). Shift clicking an already selected item will remove it from the selection. There\'s also shortcuts and menu items for selecting all items, clearing a selection, and inverting a selection. It\'s also possible now to select items which are hidden below other items by control-clicking an item, or by using \"Select next item above/below\" in the new composer Edit menu.
### Mogelijkheid: Betere navigatie door lay-outs
QGIS 2.2 includes many improvements to help you navigate your compositions. You can now zoom in or out from a composition by using the mouse scroll wheel. A dedicated pan tool has been added which allows you to drag the composition around, and you can also switch immediately to pan mode by holding the space bar or the by holding the mouse scroll wheel. There\'s also a new zoom tool which allows you to precisely zoom to a specific area of your composition. You can also switch to zoom mode at any time by pressing and holding control-space and drawing a zoom region on the composition.
### Mogelijkheid: Verbeterde stijl voor pagina's en vormen
You can now control the style of the composition background using the full range of QGIS\' symbology options. It\'s now possible to export compositions with a transparent (or semi-transparent) background. Shape items (rectangles, triangles and ellipses) can also be styled using the same options as polygon map layers. You can even style the page background or shapes by using data defined settings based on the current atlas feature! There\'s also a new option for rounding the corners of rectangle shapes.
## QGIS Server
### Mogelijkheid: Ondersteuning voor WCS toegevoegd aan QGIS-server
QGIS Server ondersteunde al verschillende standaarden, inclusief Web Map Service (WMS versie 1.3.0 en 1.1.1), Web Feature Service (WFS versie 1.0.0) en Web Feature Service met Transaction (WFS-T). met deze nieuwe uitgave van QGIS, kunt u nu rasterlagen op de server plaatsen met behulp van de standaard Web Coverage Service (WCS versie 1.0.0).

![image13](images/entries/b93abbe00e7a32ffb06144ac839619ab50521e5c.webp)
## Symbologie
### Mogelijkheid: Ondersteuning voor vulling van kleurverloop
De nieuwe mogelijkheid voor vulling van kleurverloop laat u betere cartografie maken dan ooit tevoren. De mogelijkheid heeft vele opties die grote flexibiliteit verschaffen in hoe u kleurverlopen op uw objecten toepast. Deze bevatten:
- Tweekleurige of op kleurenbalk gebaseerde vullingen
- Kaart- of object-gebaseerde herkomst voor uw kleurverlopen
- Kleurverlopen die van origine uit het centrum van uw object komen
- Conische, lineaire en radiale typen kleurverlopen
- Data-gedefinieerde opties (om een expressie of tabelkolom te gebruiken) voor alle eigenschappen van kleurverloop

Read more about how to use gradient fills [here](http://nyalldawson.net/2014/01/waiting-for-qgis-2-2-gradient-fills/).

![image14](images/entries/7c4cb6c7ce981ca88b27cd2ae55bc4e503a1234f.webp)
### Mogelijkheid: Ondersteuning voor labels in lagen met palet
Rasters die een vast kleurpalet gebruiken (bijvoorbeeld een kaart voor landgebruik) kunnen nu een categorie labels krijgen toegewezen dat in de legenda van de kaart wordt weergegeven en in de legenda van de Printvormgeving.

![image15](images/entries/232d60f2aa3accb19eb4da3a08b75ad4c15d068a.webp)
### Mogelijkheid: Kleurovergangen kunnen worden omgedraaid
Een nieuwe optie is toegevoegd aan dialoogvensters voor symbologie die kleurenbalken behandelen om u toe te staan de kleurenbalk om te draaien als die gemaakt is.

![image16](images/entries/3b1e65705f751bb468cc6495267633d613edbe34.webp)
### Mogelijkheid: kopiëren en plakken in op regel gebaseerde renderer
In de Op regel gebaseerde renderer kunt u nu met rechts op een regel klikken en dan de regel kopiëren en plakken als een neiuwe regel.

![image17](images/entries/8e69ef57ed6ae838e813d798312d7d1e39913749.webp)
### Mogelijkheid: Direct generaliseren van object
QGIS 2.2 introduceert ondersteuning voor directe generalisatie van objecten. Dit kan de tijd voor het renderen  verbeteren bij het tekenen van vele complexe objecten op kleine schalen. Deze mogelijkheid kan in de instellingen voor de laag worden in- of uitgeschakeld. Er is ook een nieuwe globale instelling die generalisatie standaard inschakelt voor nieuw toegevoegde lagen. **Opmerking**: Generalisatie van objecten kan in sommige gevallen artefacten in uw gerenderde uitvoer veroorzaken. Dit kunnen versplinteringen zijn tussen polygonen en inaccuraat renderen bij het gebruiken van op verplaatsing gebaseerde symboollagen.

![image18](images/entries/baa801841f58883d93d0ea6ecb5363da963e4ee2.webp)
### Mogelijkheid: Ankerpunten kunnen worden ingesteld voor markeringslagen
When defining symbology with marker layers (e.g. a point layer symbolized with SVG markers) you can now specify what part of the image should correspond to the \'anchor point\'. For example you can indicate that the bottom-left corner of the image should coincide with the position of the feature. You can also use the `data defined properties` to have this property set at render time based on an attribute in the data table for that layer (or an arbitrary expression).

![image19](images/entries/ecac63dad2e0da0702b2fe5bc361d68f0c0c6a0f.webp)
### Mogelijkheid: Thematische kaarten gebaseerd op expressies
Thematische kaarten van Categorieën en Gradueel kunnen nu worden gemaakt met behulp van het resultaat van een expressie. In het dialoogvenster Eigenschappen voor vectorlagen, is de kiezer voor de attributen uitgebreid met een expressie bouwer U hoeft dus nu niet langer meer het attribuut voor de classificatie naar een nieuwe kolom in uw attributentabel weg te schrijven als u wilt dat het attribuut voor de classificatie een samenstelling is van meerdere velden of een formule van enige soort.

![image20](images/entries/cc5cad88da77d1868e394a115606f4b1e6ee8c29.webp)
### Mogelijkheid: Ondersteuning voor expressies in symbooldiagrammen voor grootte en attributen
You can now use an expression to define the size and attributes when using the diagramming capabilities of QGIS. For more info see the Pull Request here [Pull 1039](https://github.com/qgis/QGIS/pull/1039)

![image21](images/entries/547b5058efeca906c00ee65ee2504f2669ff52f9.webp)
### Mogelijkheid: Regel Else in Op regel gebaseerde renderer
De Op regel gebaseerde renderer ondersteunt nu een regel met ELSE die zal worden uitgevoerd als geen van de andere regels op dat niveau overeenkomt. Regels met Else kunnen worden genest, net als elke andere regel.

Een voorbeeld kan zijn:

| `type = 'water' (style grey)` | `ELSE (style red)`

![image22](images/entries/4c38bdd63e64274d22e6a57a6541920ed47bc4be.webp)
### Mogelijkheid: Ondersteuning voor stroken binnen polygonen
Ondersteuning is toegevoegd voor stroken van polygonen om te zijn beperkt tot het binnenste van de polygoon (zodat zij niet overvloeien in een naastgelegen polygoon).

More information on this feature can be found on the [second part of this article](http://nyalldawson.net/2014/01/qgis-two-neat-features-in-2-2/).

![image23](images/entries/81597f0bc2b848fe39e078a2684c57d44fbda79d.webp)
## Gebruikersinterface
### Mogelijkheid: Verbeterde dialoogvensters Eigenschappen
Van alle dialoogvensters Eigenschappen zijn hun hoofdmenu's bijgewerkt, zodat zij er netter uitzien, met een omgedraaid gekleurde zijbalk. Dit is puur cosmetisch maar zou het eenvoudiger moeten maken om te weten wat uw huidige context is in een dialoogvenster.

![image24](images/entries/9d817847f89a3ea7836f86ddff3317040543a78f.webp)
### Mogelijkheid: Verbeteringen aan dialoogvenster Expressie
We have made some tweaks to the expression dialog - power users can now hide the operator buttons. There are also now splitters between the function list and function help areas, and between the expression and function list area. See the [original pull request](https://github.com/qgis/QGIS/pull/1073) for details.

![image25](images/entries/150ae30a6d905e008131c28e4befe862f1bf8ed6.webp)
### Mogelijkheid: Nieuwe bindingen voor toetsen
We hebben de sneltoetsen voor het toetsenbord in QGIS bijgewerkt om het uitvoeren  van herhalende taken efficiënter te maken.
- `ctrl-d` - Remove selected layers in table of contents
- `>` - Select next vertex when using the node tool
- `<` - Select previous vertex when using the node tool
- `Delete` or `Backspace` - delete the selected features (you can undo these actions), or a node when using the nodetool.
- `F5` updates the canvas (instead of ctrl-r)

See also [Issue 9094](http://hub.qgis.org/issues/9094) and [Pull Request 1010](https://github.com/qgis/QGIS/pull/1010) for more details.

![image26](images/entries/e8766bfccf2da60b09acde28f5d766eb3d76cec9.webp)

{{<content-end >}}
