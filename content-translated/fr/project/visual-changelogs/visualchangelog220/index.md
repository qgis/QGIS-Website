---
HasBanner: false
draft: false
releaseDate: '2014-02-22'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.2
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.2{#changelog22 }
Date de publication : 22/02/2014

Liste des changements dans la version QGIS 2.2.0. Une attention particulière a été portée sur les performances et l'affinage, nous avons rajouté de nombreuses fonctionnalités et améliorations pour rendre l'interface plus cohérente et professionnelle (et nous l'espérons, plus simple à utiliser). Le composeur de cartes (utilisé pour l'impression de cartes) a été l'objet de beaucoup d'efforts pour en faire un outil plus adapté à créer de superbes sorties cartographiques.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Options de l'application et du projet
### Fonctionnalité: Gestion des mesures en Miles Nautiques
For you seafaring folks out there, you can now measure distances using nautical miles. To enable this, use the `Settings -> Options -> Map Tools` option panel.

![image1](images/entries/e1115ca7d43ec24fceaee93f976848583148724f.webp)
## Fournisseurs de données
### Fonctionnalité: Gestion des relations 1,n
This release sports the ability to define 1:n relations. The relations are defined in the project properties dialog. Once relations exist for a layer, a new user interface element in the form view (e.g. when identifying a feature and opening its form) will list the related entities. This provides a powerful way to express e.g. the inspection history on a length of pipeline or road segment. You can find out more about relations support [here](http://blog.vitu.ch/10112013-1201/qgis-relations).

![image2](images/entries/0e5e0d1b9dfafe9d64dd5b79866877980f03d099.webp)
### Fonctionnalité: Outil d'export DXF
A new tool for exporting DXF\'s has been added to the `Project` menu

![image3](images/entries/452e7692b5b8d2704b4d31067265eb71986d969f.webp)
### Fonctionnalité: Coller en tant que nouvelle couche vecteur
It is a common activity in a GIS to create a sub-selection and then to create a new layer from the selection. In QGIS you can already do `save selection as` to save a layer from your selection, and now offers functionality that allows you to create a new file or memory layer from whatever is in your clipboard. Simply select some features, copy them to your clipboard and then do `Edit -> Paste features as` and choose either `New vector layer` or `New memory layer` from the submenu. The best part of this new feature is that if you have some Well Known Text (WKT) features in your clipboard from another app, you can simply paste them into QGIS as a new layer now.

![image4](images/entries/636db14446809f9e284013113a7b881868591ed3.webp)
### Fonctionnalité: Légende WMS dans la liste des couches et le composeur
Prior to QGIS 2.2 the WMS data provider was not able to display a legend in the table of contents\' layer list. Similarly no legend could be displayed in the map composer. QGIS 2.2 addresses both of these issues.

Clicking on the layer\'s legend will open a frame with the legend at full resolution. The legend will display contextual information based on your current scale. The WMS legend will be shown only if the WMS server has GetLegendGraphic capability. Legend resolution can be modified changing Canvas & Legend options.

![image5](images/entries/6e7cd4849824a802558c0e029f605145d5c885aa.webp)
## Numérisation
### Fonctionnalité : Outil de numérisation "Remplir l'anneau"
This new tool is used to cut holes in polygons and automatically fill them with new features. If you hold down `Ctrl` when finalising the feature, the attributes will be taken from parent feature.

![image6](images/entries/a8c671765578b660cb5d33cca51efa66ecdb17a4.webp)
## Général
### Fonctionnalité: Sauvegarde des dernières expressions
Le constructeur d'expressions conservera en mémoire les 20 dernières expressions.

![image7](images/entries/90a6b4d181fb2dc7699402d17c1f31522c4f3409.webp)
### Fonctionnalité: Coller des données WKT depuis le presse-papier
QGIS can now paste and create a new feature based on WKT that is found in the clipboard. Simply copy some WKT and paste into a editable layer. You can also create a new layer by selecting `Edit -> Paste As -> New Memory Layer`
## Composeur de Cartes
### Fonctionnalité: Amélioration de la gestion des bordures de carte en zebra
You can now set the colours of the `Zebra` border on the map element in the map composer.

![image8](images/entries/682c36e3ac96b491e2e0a99a7ff9d94b9e0dc4e5.webp)
### Fonctionnalité: Gestion de la rotation des éléments
Chaque type d'élément du composeur peut maintenant subir une rotation, y compris les barres d'échelles, les tables et les légendes. Par exemple, vous pouvez tourner une étiquette de votre composition afin qu'elle s'intègre au mieux à votre mise en page (comme illustré). Le redimensionnement des éléments en rotation a aussi été consolidé.

![image9](images/entries/700e0999552bc2e2bb2cef86ed14240b05f1da4e.webp)
### Fonctionnalité: Ajout d'une échelle dans le composeur et amélioration des règles
The appearance of rulers has been improved by adjusting the scale logic and by adding smaller ruler divisions, and by making vertical rulers use rotated text. There is also a new composer action for hiding/showing rulers. You can now quickly zoom to 100% page scale using the new `Zoom to 100%` tool on the toolbar. The composer window now lets you quickly switch the page scaling via a new scale combobox in the status bar. In addition a new indicator has been added to show you the precise pixel position of your cursor. The `Close` and `Help` buttons have been removed from the bottom of the composer window to give you the maximum amount of screen space for working with your compositions.

![image10](images/entries/8b148acf4ef24204b42f14ee7cec43d57c87911a.webp)
### Fonctionnalité: Génération d'un fichier World
In the composer you can now create georefenced maps! Simply ensure that you choose the correct map element in the `Composition tab` and then export your map as a PNG file. An accompanying world file will be written, allowing you to load your exported composition in QGIS as a raster layer.

![image11](images/entries/d5887511afbe8379f9e240c3763f6b68766cac88.webp)
### Fonctionnalité: Travailler avec plusieurs éléments
Support has been added for moving and resizing multiple items simultaneously. You can now hold shift while resizing to maintain an item\'s ratio while resizing, or hold control to resize from the item\'s centre. Shortcut key also apply to moving items, so holding shift while moving an item constrains the movement to horizontal or vertical movement, and holding control temporarily disables item snapping. You can also hold shift while pressing a cursor key to shift all selected items by a larger amount.
### Fonctionnalité: Amélioration de l'atlas de cartes
You can now preview the individual pages of the map atlas that will be generated in composer. While in atlas preview mode you can output the current page without outputting the entire atlas. You can also tweak the map extent or scale for each feature while previewing the atlas page. Atlas map settings have been moved from the atlas panel to the map properties panel, so now more than one map can be controlled by the atlas generation. There\'s a new option to automatically centre an overview map, which comes in handy when creating atlas based maps. More context information is now available so that you can adjust your symbology based on whether the feature is the current atlas feature or not. See [this article for more info](http://nathanw.net/2013/12/02/waiting-for-qgis-22-highlighting-current-atlas-feature/).

![image12](images/entries/fe668e5f257efec81db855a91fc7d6febc221261.webp)
### Fonctionnalité: Amélioration de la sélection des objets
You can now select more then one item by clicking and dragging a box to select them, and there\'s shortcuts for adding to a selection (holding shift while dragging), subtracting from a selection (hold control while dragging) and switching to \"within\" selection mode (hold alt while dragging). Shift clicking an already selected item will remove it from the selection. There\'s also shortcuts and menu items for selecting all items, clearing a selection, and inverting a selection. It\'s also possible now to select items which are hidden below other items by control-clicking an item, or by using \"Select next item above/below\" in the new composer Edit menu.
### Fonctionnalité: Meilleure navigation dans les compositions
QGIS 2.2 includes many improvements to help you navigate your compositions. You can now zoom in or out from a composition by using the mouse scroll wheel. A dedicated pan tool has been added which allows you to drag the composition around, and you can also switch immediately to pan mode by holding the space bar or the by holding the mouse scroll wheel. There\'s also a new zoom tool which allows you to precisely zoom to a specific area of your composition. You can also switch to zoom mode at any time by pressing and holding control-space and drawing a zoom region on the composition.
### Fonctionnalité: Améliorations de style sur les pages et les formes
You can now control the style of the composition background using the full range of QGIS\' symbology options. It\'s now possible to export compositions with a transparent (or semi-transparent) background. Shape items (rectangles, triangles and ellipses) can also be styled using the same options as polygon map layers. You can even style the page background or shapes by using data defined settings based on the current atlas feature! There\'s also a new option for rounding the corners of rectangle shapes.
## QGIS Server
### Fonctionalité: Gestion du WCS par QGIS Server
QGIS-Server gère déjà les standards suivants: Web Map Service (WMS version 1.3.0 et 1.1.1), Web Feature Service (WFS version 1.0.0) et Web Feature Service with Transaction (WFS-T). Avec cette nouvelle version de QGIS, vous pouvez maintenant fournir des couches rasters utilisant le standard Web Coverage Service (WCS version 1.0.0).

![image13](images/entries/b93abbe00e7a32ffb06144ac839619ab50521e5c.webp)
## Symbologie
### Fonctionnalité: Gestion du remplissage par gradient
Le remplissage par gradient vous permet de créer de meilleures cartes qu'auparavant. Cette fonctionnalité dispose de nombreuses options permettant une grande flexibilité dans la manière d'appliquer le gradient. Cela inclut:
- Remplissage basé sur deux couleurs ou sur une rampe
- Origine du gradient basée sur le canevas de carte ou sur l'objet
- Gradient dont l'origine est le centroïde de l'élément
- Types de gradients de forme conique, linéaire et radiale
- Les propriétés du gradient peuvent être définies par les données (par des expression ou par la colonne d'une table)

Read more about how to use gradient fills [here](http://nyalldawson.net/2014/01/waiting-for-qgis-2-2-gradient-fills/).

![image14](images/entries/7c4cb6c7ce981ca88b27cd2ae55bc4e503a1234f.webp)
### Fonctionnalité: Gestion des étiquettes pour les rasters à palette de couleur
Les rasters qui utilisent une palette de couleur fixe (en particulier, les couvertures de sol) peuvent se voir attribuer des étiquettes de catégories qui seront affichées dans la légende de la carte ainsi que dans la légende du composeur.

![image15](images/entries/232d60f2aa3accb19eb4da3a08b75ad4c15d068a.webp)
### Fonctionnalité: Les rampes de couleurs peuvent être inversées
Une nouvelle option a été ajoutée à la boîte de dialogue de symbologie pour vous permettre d'inverser une rampe de couleur lors de sa création.

![image16](images/entries/3b1e65705f751bb468cc6495267633d613edbe34.webp)
### Fonctionnalité: Copier-Coller des représentations par ensemble de règles
Dans le rendu par ensemble de règles, vous pouvez maintenant effectuer un clic-droit sur une règle pour la copier et la coller en tant que nouvelle règle.

![image17](images/entries/8e69ef57ed6ae838e813d798312d7d1e39913749.webp)
### Fonctionnalité: Généralisation à la volée des éléments
QGIS 2.2 gère la simplification de la géométrie des entités à la volée. Cela permet d'améliorer la vitesse d'affichage de nombreuses entités complexes à large échelle. L'option peut être activée ou désactivée dans les propriétés des couches. Un nouveau paramètre global permet également d'activer la simplification par défaut au moment de chargement de chaque couche. **Note** : La simplification de la géométrie peut introduire des incohérences de rendu tels que des recouvrements entre polygones ou des placements imprécis lors de l'utilisation de décalage pour le rendu de couches de symboles.

![image18](images/entries/baa801841f58883d93d0ea6ecb5363da963e4ee2.webp)
### Fonctionnalité: Des points d'ancrage peuvent être paramétrés pour les couches à marqueurs
When defining symbology with marker layers (e.g. a point layer symbolized with SVG markers) you can now specify what part of the image should correspond to the \'anchor point\'. For example you can indicate that the bottom-left corner of the image should coincide with the position of the feature. You can also use the `data defined properties` to have this property set at render time based on an attribute in the data table for that layer (or an arbitrary expression).

![image19](images/entries/ecac63dad2e0da0702b2fe5bc361d68f0c0c6a0f.webp)
### Fonctionnalité: Cartes thématiques basées sur des expressions
Les cartes thématiques faites avec le rendu Catégorisé ou Gradué peuvent désormais être créées en utilisant le résultat d'une expression. Dans la fenêtre Propriétés des couches vectorielles, le sélecteur de colonne accueille un constructeur d'expression. Dès maintenant, vous n'avez plus besoin d'écrire l'attribut de la classification dans une nouvelle colonne de votre table si vous souhaitez que l'attribut de classification soit un composite de plusieurs champs, ou une formule quelconque.

![image20](images/entries/cc5cad88da77d1868e394a115606f4b1e6ee8c29.webp)
### Fonctionnalité: Gestion des expressions pour la taille et les attributs des diagrammes
You can now use an expression to define the size and attributes when using the diagramming capabilities of QGIS. For more info see the Pull Request here [Pull 1039](https://github.com/qgis/QGIS/pull/1039)

![image21](images/entries/547b5058efeca906c00ee65ee2504f2669ff52f9.webp)
### Fonctionnalité: Clause Else dans la représentation par ensemble de règles
Le rendu Ensemble de règles propose maintenant une règle Else qui sera exécutée si aucune des autres règles du même niveau n'est appliquée. Les règles Else peuvent être emboîtées comme les autres règles. 

Un exemple pourrait être :

| `type = 'water' (style grey)` | `ELSE (style red)`

![image22](images/entries/4c38bdd63e64274d22e6a57a6541920ed47bc4be.webp)
### Fonctionnalité: Gestion du contour interne des polygones
La fonction de limitation du contour du polygone à l'intérieur du polygone a été ajoutée (de manière à ce que le contour n'empiète pas sur un polygone voisin).

More information on this feature can be found on the [second part of this article](http://nyalldawson.net/2014/01/qgis-two-neat-features-in-2-2/).

![image23](images/entries/81597f0bc2b848fe39e078a2684c57d44fbda79d.webp)
## Interface utilisateur
### Fonctionnalité: Amélioration des boîtes de dialogue des propriétés
Toutes nos boîtes de dialogue de propriétés ont vu leur menus mis à jour de manière à avoir un rendu plus lisse avec une barre latérale de couleur inversée. C'est purement cosmétique mais cela permet de savoir plus facilement dans quel contexte est la boîte de dialogue.

![image24](images/entries/9d817847f89a3ea7836f86ddff3317040543a78f.webp)
### Fonctionnalité: Améliorations sur la boîte de dialogue des expressions
We have made some tweaks to the expression dialog - power users can now hide the operator buttons. There are also now splitters between the function list and function help areas, and between the expression and function list area. See the [original pull request](https://github.com/qgis/QGIS/pull/1073) for details.

![image25](images/entries/150ae30a6d905e008131c28e4befe862f1bf8ed6.webp)
### Fonctionnalité: Nouveaux raccourcis-clavier
Nous avons mis à jour les raccourcis clavier de QGIS de manière à rendre plus efficace les tâches répétitives.
- `ctrl-d` - Remove selected layers in table of contents
- `>` - Select next vertex when using the node tool
- `<` - Select previous vertex when using the node tool
- `Delete` or `Backspace` - delete the selected features (you can undo these actions), or a node when using the nodetool.
- `F5` updates the canvas (instead of ctrl-r)

See also [Issue 9094](http://hub.qgis.org/issues/9094) and [Pull Request 1010](https://github.com/qgis/QGIS/pull/1010) for more details.

![image26](images/entries/e8766bfccf2da60b09acde28f5d766eb3d76cec9.webp)

{{<content-end >}}
