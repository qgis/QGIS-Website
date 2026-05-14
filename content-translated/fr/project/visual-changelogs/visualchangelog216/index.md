---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.16
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.16{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Release date: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Ceci n'est pas une Version Long Terme**

Cette version n'est pas désignée comme Version Long Terme (LTR). Les utilisateurs qui souhaitent avoir une version de QGIS qui ne change pas et qui bénéficie de correction d'erreurs pendant au moins 1 an sont invités à utiliser plutôt la version 2.14 (qui est à présent notre version LTR officielle avec la sortie de QGIS 2.16)

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## Sponsors de QGIS 2.16.0
Chaque année, nous recevons aussi le soutien de diverses organisations qui apprécient le travail que nous faisons et souhaiteraient faciliter l'effort de développement soutenu du projet. Ces sponsors sont listés ci-dessous avec nos remerciements !

{{<fund type="changelog" >}}
## Général
### Fonctionnalité : Copier les entités au format GeoJSON
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : stocker des signets spatiaux dans les fichiers de projet.
Si vous créez un signet spatial, vous pouvez choisir de stocker le signet dans votre fichier de projet actif. Parcourez le panneau des signets pour trouver la case à cocher qui permet cette possibilité.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### Fonctionnalité : visualisation des messages GNSS GNRMC
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Ondřej Fibich
### Fonctionnalité : Coller des entités GeoJSON directement dans QGIS
Le presse papier de QGIS peut à présent analyser différents type de format texte, dont le format natif pour les collections d'entités GeoJSON. Celà permet de coller et coller directement des chaînes de caractères GeoJSON dans QGIS afin de les convertir automatiquement en entités et géométries QGIS.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : amélioration des infobulles de carte
- Visibilité des infobulles de carte conservée à travers les sessions
- Les infobulles de cartes affichent à présent du contenu HTML, des vidéo et des liens internet

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Fonctionnalité : les types de fichiers de QGIS disposent à présent d'icônes MIME dédiées
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - fichier de projet QGIS
- \*.qml - fichier d'attributs de couche
- \*.qlr - fichier de définition de couche
- \*.qpt - fichier modèle de composeur

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## Interface utilisateur
### Fonctionnalité : Loupe de canevas de carte
Une loupe a été ajoutée à QGIS, et permet d'agrandir la carte sans changer d'échelle, ce qui permet de positionner plus facilement les étiquettes et symboles. De plus, une valeur par défaut peut être inscrite dans les paramètres de configuration, ce qui est très utile pour les écrans à grande résolution !

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Fonctionnalité : Amélioration du zoom
QGIS 2.16 offre de nouvelles façons de zoomer et dézoomer dans le canevas de carte.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Éditeur interactif de gradient remodelé
L'éditeur de rampe de gradient a été remodelé avec des contrôles interactifs pour une manipulation aisée des gradients. Maintenant, la boîte de dialogue a aussi un graphe interactif pour modifier les arrêts de gradient avec des valeurs de couleurs TSV ou RVB. Les nouvelles fonctionnalités de l'éditeur :
- faire glisser pour définir l'arrêt de couleur
- Double-cliquer pour ajouter un nouvel arrêt
- La touche Délétion efface l'arrêt sélectionné
- Les touches fléchées déplacent l'arrêt sélectionné, et en pressant la touche Shift en combinaison avec les touches fléchées le déplacement sera plus important
- Glisser et coller une couleur sur le widget pour ajouter un nouvel arrêt

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Choix de la vue par défaut pour la table attributaire
Dans les versions précédentes de QGIS, la table d'attributs s'affichait toujours de la même manière à l'ouverture (vue tabulaire). Maintenant vous avez le choix d'afficher par défaut la vue tabulaire, la vue formulaire ou se souvenir de la dernière vue utilisée. 

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Améliorations des calendriers contextuels
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Amélioration des sélecteurs de couleur
Les menus contextuels de couleur affichent maintenant une roue chromatique permettant un ajustement très rapide des couleurs.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### Fonctionnalité : Copie du contenu d'une cellule de la table attributaire
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Fonctionnalité: Amélioration du support pour HiDPI
Les utilisateurs d'écrans HiPDI noteront une amélioration de l'interface utilisateur car des efforts ont été faits pour mettre à jour les icônes au format SVG. Depuis QGIS 2.16 toutes les barres d'outils sont compatibles avec HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité : Amélioration de l'outil de sélection sur la carte
Le comportement des outils de sélection sur une carte a été amélioré grâce aux changements suivants :

Pour cliquer-et-glisser les sélections :
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Pour les sélections avec un seul clic :
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Ces modifications permettent d'aligner le comportement de ces outils sur celui rencontré dans d'autres applications et également avec le composeur.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Actualisation de la Documentation
### Fonctionnalité : Documentation de QGIS 2.14
Avec la génération automatique de tickets dans le dépôt Documentation pour chaque nouvelle fonctionnalité ajoutée à QGIS, nous sommes désormais sûrs que toutes les nouvelles fonctionnalités sont portées à la connaissance de l'équipe de documentation.

L'équipe a travaillé dur sur les tickets des trois précédentes versions de QGIS : 2.10, 2.12, 2.14 afin d'assurer une documentation à jour avec la Version Long Terme de QGIS. Cet effort porte sur près de 180 nouvelles fonctionnalités documentées en à peu près 4 mois.

Si vous pensez qu'il y a des éléments manquants dans la documentation, n'hésitez pas à ouvrir un nouveau ticket, écrire un texte court pour les décrire ou, mieux, proposer une contribution.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

L'équipe de documentation va désormais travailler sur la version stable (2.16) de QGIS.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Jetez un œil aux liens vers la 2.10, 2.12 et 2.14 pour voir l'ensemble du travail abattu par la documentation :
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

Cette fonctionnalité a été développée par Larry Shaffer
## Symbologie
### Fonctionnalité: Couche de symboles de flèche
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

En mode courbe, les nœuds de la couche linéaire sur laquelle est appliquée cette couche de symbole seront utilisés comme points de contrôle pour les arcs circulaires. Les flèches peuvent être remplies avec tous les styles de remplissages de QGIS. Des options permettent de sélectionner le type de flèche (avec une ou deux pointes, remplies ou hachurées), sa largeur (qui peut être variable) et la taille des pointes.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Nouveaux symboles dédiés à l'accessibilité et la mauvaise vision
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité: Nouveaux symboles de marqueurs simples
- demi-cercle, tiers de cercle, quartiers
- demi-triangles.
- croix remplies et hexagones.
- diamant en ellipse.

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Il est toujours possible de faire des sélections sur la couche dans le canevas et les entités sélectionnées seront affichées avec un symbole par défaut. Les entités en cours d'édition seront également affichées.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Amélioration du contrôle du rendu du remplissage de centroïde
Une option a été ajoutée pour contrôler si le marqueur doit être dessiné sur toutes les parties ou un seule partie des entités multiples.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité: Paramètre de bordure pour les symboles de police
Les symbole de marqueurs de police peuvent maintenant avoir une bordure ce qui peut améliorer leur visibilité grâce à l'ajout d'un tampon de couleur. Les caractères de polices emoji peuvent servir de marqueurs intéressants lorsqu'ils sont utilisés avec une bordure épaisse.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité: Contrôle de la jointure de bordure pour les symboles simples, d'ellipse et de police
Les utilisateurs peuvent maintenant modifier le style des jointures des bordures de symboles simples, d'ellipse et de police pour affiner leur symbologie.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité: Nouvel outil de carte pour paramétrer interactivement le décalage d'un symbole ponctuel
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Le panneau Style
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Étiquetage
### Fonctionnalité : La barre d'outils Étiquettes prend en charge l'étiquetage basé sur des règles
Dans les versions précédentes de QGIS, lorsque l'étiquetage basé sur des règles était utilisé, vous ne pouviez pas utiliser les outils interactifs d'étiquettes pour positionner et pivoter les étiquettes. C'est maintenant géré.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Cette fonctionnalité a été développée par Martin Dobias
## Diagrammes
### Fonctionnalité: La taille des diagrammes est affichée dans la légende
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Sélection des unités pour la largeur de bordure
La sélection de l'unité de la largeur des bordures est maintenant disponible. Cela permet à un diagramme avec une taille exprimée en unités de cartes de grossir ou diminuer en se basant sur une échelle de carte tout en maintenant la taille de la bordure fixe en millimètres.

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Fonctionnalité: Les diagrammes se comportent comme des étiquettes et peuvent être gérés depuis la barre d'outils
Au départ, il existait une barre d'outils Étiquettes pour:
- définir les paramètres d'étiquetage pour la couche active
- mettre en exergue les étiquettes épinglées. Les couches en édition affichent une surbrillance verte, sinon, elle est bleue.
- épingler ou non les étiquettes
- déplacer, afficher et cacher les étiquettes

Avec cette modification, un nouvel outil est ajouté à la barre d'outils Étiquettes afin de définir les propriétés des diagrammes de la couche active. En outre, chacun des outils précédemment mentionnés fonctionne avec les diagrammes aussi.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Rendu
### Fonctionnalité : Nouvelles options de simplification à la volée
L'utilisateur peut sélectionner l'algorithme à utiliser lors de la simplification côté client pour dessiner les géométries plus rapidement. Maintenant, QGIS propose trois algorithmes:
- Distance (algorithme par défaut et  la seule option disponible dans les versions précédentes de QGIS).
- SnapToGrid.
- Visvalingam.

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Fonctionnalité: Classification basée sur les quantiles pour les couches raster
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Piers Titus van der Torren
### Fonctionnalité: Moteur de rendu d'ombre porté en direct
QGIS 2.16 dispose d'un nouveau moteur de rendu raster qui créé dynamiquement un modèle d'ombre portée à partir d'un Modèle Numérique d'Élévation.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Cette fonctionnalité a été développée par Asger Skovbo Petersen et Nathan Woodrow
## Numérisation
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Extension des géométries linéaires avec l'outil de remodelage
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Cette fonctionnalité a été développée par Martin Dobias
### Fonctionnalité: Tolérance de segmentation
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Marco Hugentobler
## Gestion des données
### Fonctionnalité: Nouvelles options de configuration pour la table attributaire
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Ajout d'une nouvelle colonne dans la table attributaire permettant d'afficher les boutons destinés à déclencher les actions de la couche sur chaque entité choisie.
- Les colonnes peuvent être masquées depuis la table d'attributs (via un clic-droit sur l'en-tête du nom de champ).
- QGIS conserve maintenant la largeur des colonnes dont la taille a été modifiée.

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Fonctionnalité: Gestion des colonnes dans les formulaires de saisie
Lorsque la conception par glisser/déposer est utilisée, l'utilisateur peut indiquer sur combien de colonnes les champs doivent être distribués.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Assurez-vous d'utiliser le mode de formulaire par conception par glisser/déposer.
- Double-cliquez sur les conteneurs de groupe, tels que les onglets ou les groupes.
- Une boîte de dialogue apparaîtra où vous pourrez sélectionner le nombre de colonnes.

L'ordre sera première colonne, seconde colonne, nième colonne, ligne suivante, etc.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Fonctionnalité: Contrôle des attributs à exporter lors de l'enregistrement d'une couche vecteur
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

Cette fonctionnalité a été développée par Jürgen Fischer et Even Rouault
### Fonctionnalité: Vue formulaire: la colonne sur le côté est maintenant triable
Dans le mode formulaire de la table d'attributs de QGIS il existe une colonne sur le côté qui peut être utilisée pour aller directement sur une entité spécifique. Jusqu'à cette nouvelle version, cette colonne ne pouvait pas être triée. Pour effectuer le tri, il fallait retourner dans le mode table et revenir en mode formulaire. Il est maintenant possible de trier les entités selon l'attribut de pré-visualisation du panneau latéral en choisissant la fonction de tri dans le bouton contextuel au dessus de la colonne latérale.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Fonctionnalité: Contrôle de formulaire de référence de la relation: raccourci pour l'ajout de nouvelles valeurs
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Fonctionnalité : Améliorations de l'export DXF
Une fonctionnalité a été ajoutée pour permettre l'export des étiquettes basées sur des règles, pour les symboles en rotation et pour l'export des géométries en 3D.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité: Contrôles de formulaire de premier niveau dans la conception par glisser/déposer
Il est maintenant possible de placer les contrôles de formulaire directement dans le formulaire dans la conception par glisser/déposer. Un formulaire en conception par glisser/déposer peut maintenant exister sans aucun onglet à l'intérieur.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Fonctionnalité: Filtre et sélection basées sur le formulaire
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

De nouveaux boutons apparaissent en bas du formulaire pour soit sélectionner les entités correspondantes (avec les options pour ajouter à la sélection/supprimer de la sélection/sélectionner au sein de la sélection courante), soit filtrer les entités dans la table (avec les options pour ajouter les entités au filtre courant ou restreindre davantage le filtre courant).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Cette fonctionnalité a été financée par SIGE, la Ville d'Uster, Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Création de couches GeoPackage
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité: Contraintes dans les contrôles de formulaire
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Fonctionnalité: Mise à jour d'attributs de plusieurs entités simultanément
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

Dans ce mode, les modifications des valeurs d'attributs sont appliquées uniquement aux entités sélectionnées. De nouveaux contrôles apparaissent à côté de chaque contrôle de formulaire permettant l'affichage de l'état de mise à jour multiple et l'annulation des changements champ par champ.

Les changements sont réalisés par une seule commande de mise à jour et appuyer sur annuler annulera les changements sur toutes les entités en une seule fois.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Légende des couches
### Feature: New option to zoom to a layer\'s visible scale range
Pour les couches disposant d'une visibilité sur plage d'échelle, sélectionner cette option modifiera l'échelle courante sur l'échelle la plus proche à laquelle la couche sera visible. De plus l'interface a été affinée de manière à ce que les couches qui sont en dehors de leur plage visible et masquée sont affichées en grisé dans l'arbre des couches.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Composeur de Cartes
### Fonctionnalité: Nouveaux outils de dessin de polygones et de polylignes
Deux nouveaux éléments de formes, basées sur des nœuds, sont maintenant disponibles dans le composeur. En utilisant ces formes, vous pouvez dessiner des polygones, des polylignes au sein de votre composition en quelques clics.

De nouveaux outils ont également été ajoutés pour permettre l'édition directe des nœuds (déplacer ou supprimer les nœuds) et également pour ajouter de nouveaux nœuds à des formes existantes. Les éléments de polygones et de polylignes du composeur peuvent également être stylés en utilisant les styles de symboles disponibles pour les couches vecteurs de polygones et de lignes !

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Fonctionnalité: Liens relatifs dans les étiquettes du composeur
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Fonctionnalité: Incorporer les entités d'atlas dans le source HTML du composeur au format GeoJSON
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### Fonctionnalité: Gestion des SVG paramétrés pour les images SVG du composeur
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Utilisation plus simple du HTML dans les étiquettes
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Sorties géoréférencées du composeur (ex: PDF)
Dans QGIS 2.16, le composeur géo-référence automatiquement ses sorties (lorsque le format de sortie le permet, ex: TIF et PDF).

L'option existante de créer un fichier world a été séparée de la sélection du géo-référencement de la carte. Le nouveau comportement par défaut est de toujours géo-référencer les exports et de créer un fichier world séparé uniquement si l'option correspondante est cochée.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Les cartes de composeur se mettent automatiquement à jour en fonction des réglages
Lorsqu'une carte de composeur est paramétrée pour suivre un réglage, elle sera automatiquement mise à jour lorsque le style sera modifié.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Cette fonctionnalité a été développée par Martin Dobias
## Outils d'analyse
### Fonctionnalité: Paramètres nommés dans les expressions
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

Utiliser des paramètres nommés aide à clarifier à quoi se réfèrent les arguments d'une fonction d'expression, ce qui est utile lorsque vous essaierez d'interpreter une expression ultérieurement.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Ajout de nouvelles unités de distance
Le choix des unités de distance a été élargi avec de nouvelles options incluant les kilomètres, les yards et les miles. Utiliser ces unités évite de réaliser des conversions manuelles de distance (ex: pieds vers des miles).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Modifications dans les expressions
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Fonctionnalité: Statistiques pour les champs chaînes de caractères et dates
Le panneau du résumé statistique peut maintenant calculer des statistiques agrégées pour les champs de dates et de chaînes de caractères.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Affichage du rayon de point de courbure dans les outils d'information
Si vous cliquez sur une ligne courbe en utilisant l'outil d'information, QGIS affichera le rayon dans l'information.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Marco Hugentobler
### Fonctionnalité: Agrégats pour les expressions
QGIS 2.16 prend en compte plusieurs types d'agrégats dans le moteur d'expression. Il inclut:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

Dans tous les cas, les calculs sont mis en cache dans le contexte de l'expression de manière à ce qu'ils ne soient calculés qu'une seule fois lors des évaluations des expressions.

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: l'extension fTool a été remplacée par les géotraitements Processing
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par by Alex Bruy
## Traitement
### Fonctionnalité: Renseigner des emplacements de points en cliquant dans le canevas de carte
Les paramètres dans Processing qui demandent un emplacement de point peuvent maintenant être renseignés en cliquant sur une position dans le canevas de carte. Auparavant, les coordonnées devaient être renseignées manuellement.

Cette fonctionnalité a été développée par by Alex Bruy
### Fonctionnalité: Gestion des expressions et des variables
Les entrées et sorties de boîtes de dialogue des algorithmes prennent maintenant en compte les expressions et les variables.

Cette fonctionnalité a été développée par Victor Olaya
### Fonctionnalité: Algorithmes pré-configurés
Des algorithmes avec des paramètres pré-configurés peuvent maintenant être ajoutés à la boîte d'outils Processing, sous forme de raccourci vers un processus donné.

Cette fonctionnalité a été développée par Victor Olaya
### Fonctionnalité: Créer une extension avec des algorithmes basés sur des scripts depuis la boîte à outils.
Auparavant, le seul moyen de créer une extension QGIS qui ajoutait de nouveaux algorithmes à Processing était de développer manuellement ces algorithmes et de créer un nouveau fournisseur d'algorithme. Maintenant, les algorithmes peuvent être écrits comme de simples scripts Processing et une extension les contenant peut être créée directement depuis la Boîte à outils des Traitements. Cette extension peut ensuite être distribuée sous forme d'extension classique et elle ser ajoutée dans Processing lorsqu'elle sera active.

Cette fonctionnalité a été développée par Victor Olaya
### Fonctionnalité: Utilisation du gestionnaire d'authentification pour les algorithmes utilisant des données PostGIS
Les algorithmes utilisant des sources de données PostGIS utilisent maintenant le gestionnaire d'authentification QGIS pour récupérer les éléments d'authentification pour se connecter à la base de données.
- Lorsqu'une méthode d'authentification a été paramétrée pour la connexion PostGIS, l'utilisateur devra renseigner son mot de passe principal.
- Dans le cas où aucune méthode d'authentification n'a été paramétrée pour la connexion, les éléments d'authentification seront récupérés dans le cache ou, s'ils ne sont pas trouvés, ils seront demandés à l'utilisateur et mis dans le cache d'authentification.

Ainsi, il n'est plus nécessaire d'enregistrer les mots de passe en clair dans les paramètres de connexion pour pouvoir utiliser des algorithmes sur des données PostGIS.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Fonctionnalité: Gestion de l'écriture dans des tables sans géométrie
Les sorties de type OutputVector des algorithmes gère l'écriture dans des tables sans géométrie.

Pour l'instant, la modification n'a été portée que pour l'algorithme Refactoriser les champs mais elle peut être facilement étendue à d'autres algorithmes qui gèrent des attributs.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Fonctionnalité: Ajout de nouveaux algorithmes GRASS au menu Traitement
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

Certains tests unitaire (principalement pour les algorithmes de raster et d'imagerie) ont également été inclus pour certains algorithmes, rendant la détection de bugs plus simple à gérer et à traiter.

Veuillez toutefois noter que pour le moment les algorithmes de GRASS7 dans Processing peuvent uniquement utiliser et produire des couches vecteurs au format Shapefile et des rasters GeoTiff. Il existe également une limite pour certains algorithmes rasters qui dupliquent les couches raster dans des répertoires temporaires (tous les algorithmes qui manipulent des tables de couleur). En fonction de la taille des sources rasters, vous aurez probablement besoin d'un grand espace disque pour les gérer.

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Fournisseurs de données
### Fonctionnalité: Les jeux de données OGR sont ouverts en mode lecture seule par défaut
Cela permet l'édition concurrentielle des fichiers Shape et Tab en même temps dans QGIS et MapInfo.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité: Amélioration de la prise en compte des champs de type DOMAIN dans PostgreSQL
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Configuration du mode lecture seule des couches vecteurs dans le projet
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Fonctionnalité: Gestion des bases de données DB2
Cette fonctionnalité a été développée par David Adler
### Fonctionnalité: Rafraîchissement des vues matérialisées PostgreSQL dans DB Manager
### Fonctionnalité: Affichage de l'attribut OGR FID
QGIS expose maintenant le FID d'OGR comme premier attribut lorsque celui-ci a une utilité, comme par exemple pour les pilotes GPKG et les bases de données.

Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité: Services ArcGIS REST Map et Feature
QGIS est maintenant capable de se connecter aux services ArcGIS REST.

Vous pouvez vous connecter aux services ArcGIS Feature (un équivalent WFS dans le monde ESRI) et aux services ArcGIS Map (équivalent WMS). Le fournisseur de données permet la lecture des cartes et des couches vecteurs depuis ces services.

Cette fonctionnalité est très intéressante pour les utilisateur qui souhaiteraient basculer d'une plate-forme SIG ESRI sans perdre leur travail hébergé sur des services de carte publics ou privés. Vous pouvez également vous connecter aux services publics fournis par ESRI.

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Fonctionnalité: Enregistrement des styles dans les bases de données MS SQL et Oracle
Cette fonctionnalité a été développée par Jürgen Fischer et Christian Frugard
### Fonctionnalité: Renommer les champs dans les couches
Dans QGIS 2.16, vous pouvez maintenant renommer les champs dans les couches PostgreSQL, Oracle, OGR et celles en mémoire en double-cliquant sur le nom du champ dans la fenêtre des propriétés de la couche.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité: Gestion basique du gestionnaire Oracle Workspace
La gestion du gestionnaire Oracle Manager a été ajoutée lorsque vous utilisez le fournisseur Oracle.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
### Fonctionnalité: Améliorations massives du fournisseur WFS
QGIS 2.16 embarque une revue complète du fournisseur WFS qui inclue:
- Auto-détection de la version.
- Mise en cache sur disque des entités téléchargées.
- Téléchargement en tâche de fond et rendu progressif.
- Support du WFS 1.1 et 2.0
- Pagination des requêtes WFS 2.0 GetFeature.
- Ajout de tests unitaires sur le fournisseur.
- Prise en charge des jointures pour le WFS 2.0
- Paramètre URI avec sql pour les clauses SELECT / FROM / JOIN / WHERE / ORDER BY.
- Gestion des champs de date.
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- Gestion de types géométriques additionnels/mixtes (CurvePolygon, CompoundCurve).
- Meilleure tolérance des serveurs WFS non-conformes.

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
L'expression utilisée pour générer les valeurs par défaut pour un champ d'une base de données PostgreSQL est actuellement affichée dans le formulaire de l'entité.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
L'avantage apporté par cette amélioration est qu'il est maintenant possible de créer directement et de relier des enregistrements entre tables liées avant d'enregistrer les données en premier car la clef primaire est déjà présente avant que l'entité ne soit enregistrée.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## QGIS Server
### Fonctionnalité: Gestion de l'entourage en rouge dans les requêtes GetMap et GetPrint
Cette fonctionnalité a été financée par Canton of Solothurn

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Fonctionnalité: Transformations géodésiques par défaut pour le serveur
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Extensions
### Fonctionnalité: Amélioration de l'extension Globe.
- Mise à jour vers OsgEarth 2.8.
- Refonte du pilote de tuile de QGIS Globe.
- Refonte de la logique de synchronisation entre la 2D et la 3D.
- Migration vers un nouveau noyau géométrique.
- Gestion de plusieurs couches d'arrière-plan.
- Menus intégrés dans la fenêtre Globe.
- Couche de sélection indépendante pour l'extension.
- Report du travail de la thèse de Mathias Kuhn issue de QGIS 2.1/OsgEarth 2.4.

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Fonctionnalité: Globe: extruder les objets
Permettre l'extrusion d'objets en 3D.

Soit par une valeur fixe, soit par un attribut ou une expression.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Fonctionnalité: API: Ajout de pages pour les propriétés des couches vecteur
Permet l'ajout de pages supplémentaires à la boîte de dialogue des propriétés des couches vecteurs.

Cela permet d'ajouter des options de configuration de couche fournies par une extension pour faciliter l'identification de leur provenance et d'améliorer l'expérience utilisateur.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Fonctionnalité: Globle: gestion des vecteurs
Lors de l'affichage des couches sur le globe, les données vecteur sont préservées.

Cette fonctionnalité a été financée par Master Thesis UZH

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Fonctionnalité: Globle: Exagération verticale pour les MNT.
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## Programmation
### Fonctionnalité: Contrôles intégrés dans l'arbre des couches
Cette fonctionnalité permet de définir des contrôles intégrés dans l'arbre des couches, couche par couche, depuis la boîte de dialogue des propriétés de la couche (dans le nouvel onglet Légende). L'idée est de disposer d'un accès rapide à certaines action qui sont souvent utilisées sur une couche.

Cette implémentation livre uniquement pour le moment un contrôle de transparence. A l'avenir, d'autres contrôles devraient apparaître, comme par exemple pour paramétrer des filtres, de la sélection, du style ou d'autres éléments. L'API permet aux extensions d'enregistrer leurs propres contrôles qui peuvent être utilisés dans de nombreux domaines métiers sur des couches spécifiques.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Martin Dobias
### Fonctionnalités: Les extensions peuvent ajouter des pages dans les propriétés des couches vecteur
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Fonctionnalité : Nouvelles classes PyQGIS 2.16
### Nouvelles classes de base
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) -an abstract base class for composer items which provides generic methods for nodes based shapes such as polygons or polylines
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - a composer item for polygon shapes
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) -a composer item for polyline shapes
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.htmll) -a composer undo command class for grouping / ungrouping composer items
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) -WKB reader which simplifies geometries on the fly
- [QgsAction](https://qgis.org/api/classQgsAction.html) - a utility class that encapsulates an action based on vector attributes
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - stores and manages actions associated with a layer
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) -a utility class for calculating aggregates for a field (or expression) over the features from a vector layer
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) -a container for configuration of the attribute table for a vector layer
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - a representation of the interval between two datetime values
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handles exporting QgsFeature features to GeoJSON features
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - helper utilities for working with JSON and GeoJSON conversions
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) -simple profiler for timing code paths during execution
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - utility class for parsing SQL statements
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of strings
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - a renderer for generating live hillshade models
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) -line symbol layer used for representing lines as arrows
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) -a renderer which draws no symbols for features by default, but allows for labeling and diagrams for the layer
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) -abstract base class for simple marker symbol layers. Handles creation of the symbol shapes but leaves the actual drawing of the symbols to subclasses.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) -filled marker symbol layer, consisting of a shape which is rendered using a QgsFillSymbolV2

### Nouvelles classes d'IHM
#### Contrôles réutilisables:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- une roue de teinte, des motifs de couleur et un échantillonneur de couleur.
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subclass with more fine-grained control over how the widget is closed or opened
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - an event filter for watching for focus events on a parent object
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) -an interactive editor for previewing a gradient color ramp and modifying the position of color stops along the gradient
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) -a panel widget that can be shown in the map style dock
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) -factory class for creating custom map layer property pages
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - base class for any widget that can be shown as a inline panel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) -inline panel wrapper widget for existing widgets which can\'t have the inheritance tree changed, e.g dialogs
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) -a stack widget to manage panels in the interface
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) -a class that contains a list of QActions and QShortcuts that have been registered and allows their shortcuts to be changed
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) -this can be used like a regular QTableWidgetItem with the difference that a specific role can be set to sort
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) -renderer widget for configuring the hill shade renderer
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) -widget for controlling a raster layer\'s transparency and related options
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) -renderer widget for configuring arrow symbol layers

#### Boîtes de dialogues réutilisables :
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Correctifs notables
### Fonctionnalité : Programme de financement de résolution de bogues
Nous avons procédé à une autre session rémunérée de correction de bugs (merci à nos sponsors et à nos donateurs !). Voici un résumé du travail des développeurs qui y ont participé:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- Correction de la transformation de projection non fonctionnelle (#14551 - grave).
- Correction des problèmes de sélection d'entité selon le rayon (#14748 - grave).
- Correction de calculs de surface incorrects pour les polygones (#14675 - grave, bien que peu probable. Les tests unitaires pour gérer ce cas ont été ajoutés).
- Correction de l'agencement du contrôle de panneau (#15011 - grave)
- Correction d'un plantage dans les couches de symboles de flèches (non remonté).
- Correction d'un plantage dans les jointures non valides (non remonté).
- Correction des SVG avec paramètres non affichés pour les éléments de flèches du composeur (#14997 - haut).
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Toujours utiliser des comparaisons de chaînes de caractères dans les expressions de champs texte (#13204 - haut).
- Correction du répertoire home ajouté par défaut dans le chemin par défaut pour les fichiers SVG et les modèles (#14662, #14652, #14883 - haut).
- Correction d'un plantage lors de l'utilisation de polygones inversés avec le moteur de rendu de carte de chaleur (#14968 - haut).
- Enregistrement des valeurs de symbologie de raster en précision complète (#14950 - normal).
- Les actions ne sont pas activées lors du chargement de la couche avec son style par défaut (#13910 - normal).
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- Correction de la non désactivation du capteur de contrôle personnalisé (#9732 - normal).
- Correction de la couche de symboles de flèches, largeur/hauteur de la pointe inversées (#15002 - normal).
- Correction des jointures non recréées lors du chargement d'un projet avec des couches à reprendre (#10500 - normal).
- Invalidation du cache de jointure lorsque la couche est modifiée (#11140 - normal).
- Gestion correcte des jointures utilisant des champs virtuels (#14820 - normal).
- Correction des champs virtuels qui dépendent d'autres champs virtuels qui ne sont pas calculés dans certains cas (#14939 - normal).
- Correction des étiquettes basées sur des règles non affichées lors de l'utilisation de fonctions d'expression en Python (#14985 - normal).
- Rafraîchissement automatique lors du changement des niveaux de symbole dans le panneau de style (#14861 - normal).
- Correction du bouton du panneau de style non synchronisé avec l'état du panneau (#14862 - normal).
- Correction des erreurs de rendu SVG avec texte (#14644, #14794 - normal).
- S'assurer que le bouton valeurs définies par les données des champs affichés est toujours à jour (#14809 - normal).
- Correction du raccourci pour le zoom + (#14958 - normal).
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- Ajout des fonctions mandataires pour la vérification du comportement des sous-moteurs de rendu pour les polygones inversés et de déplacement (non remonté).
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- Affichage du type WKB dans les métadonnées des couches vecteurs (non remonté).
- Ajout de chaînes manquantes des capacités dans les métadonnées d'une couche (non remonté).
- Correction du bruit de déboguage lors de l'utilisation des couches en géométrie 25D (non remonté).
- Correction de quelques contrôles de barre d'état qui ne pouvaient pas être masqué par personnalisation (non remonté).
- Conserver le paramétrage de l'action instantanée du panneau de style (non remonté).
- Don\'t show constraint messages when form is in search mode (unreported)
- Afficher les ascenseurs pour les formulaires d'attributs dans les résultats de l'identification (non remonté).
- Rendre le bouton Appliquer du panneau de style toujours activé (non remonté).
- Correction de certaines mises à jour automatiques manquantes dans le panneau de style (non remonté).

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Voici les tickets qu'il a géré pendant le temps alloué à la correction des bugs de QGIS 2.16.

**Sévère/Elevé:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normal**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Autre :**
- <https://issues.qgis.org/issues/14981>: Import of Shapefile to Geopackage-Database in DB-Manager fails (analysis)
- <https://issues.qgis.org/issues/15011>: Browser panel is unusable (bisection & analysis)
- <https://issues.qgis.org/issues/14909>: regression: QGIS crashes when closing docked attribute table (analysis)
- <https://issues.qgis.org/issues/13353>: QGIS and gdal 2.0.0 (closed: no further action needed)
- <https://issues.qgis.org/issues/15053>: WMS with EPSG:31255 is shifted (datum=hermannskogel) (analysis. probably outdated proj.4 version)

### Sandro Santilli
- <http://hub.qgis.org/issues/14262>: Overflow on primary key with negative values; cannot save edits
- <http://hub.qgis.org/issues/12228>: Deadlock from parallel rendering
- <http://hub.qgis.org/issues/11371>: Map Composer: group + move + ungroup + undo = crash
- <http://hub.qgis.org/issues/14976>: Repository files modified by \"make check\"
- <http://hub.qgis.org/issues/13635>: Different handling of invalid geometries between LTR and master version
- <http://hub.qgis.org/issues/13952>: QGIS node tool causes snapping another feature randomly

### Martin Dobias
- Digitizing: \"Simplify Feature\" should not open a dialog when no feature is clicked
- Digitizing: how to abort \"Simplify Feature\" or \"Rotate Feature\" tool is not that obvious
- Une route est manquant dans Ajouter une couche vecteur !
- Le tracé automatique échoue avec les géométries en arc circulaire.
- Le WMS ne fonctionne pas sur la branche master a625eeb (2.15.0-80).
- Erreur Python pour les algorithmes pré-configurés de Processing.
- GPS don\'t record geometry point, but only attribute values\...
- Panneau de style: le panneau de transparence (transparence globale, transparence de pixel, etc.) ne fonctionne pas pour le moteur de rendu d'ombre portée.
- Panneau de style: Bouton retour arrière et en avant manquant lorsqu'une étiquette basée sur les règles est en cours de modification.
- Correction de la fonction d'annuler/refaire pour le moteur de rendu et le moteur d'étiquettes basés sur des règles dans le panneau de style.
- Correction des mises à jour du contrôle d'annulation dans le panneau de style.
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Amélioration de la stabilité de QgsMapLayerRegistry.
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- Correction de quelques erreurs de compatibilité Python 3.
- Travail sur la ré-activation des tests unitaires sous OSX (fusionné après la publication de la version 2.16).
- Documentation de l'API
- startup.py est lancé deux fois.
- Corrections d'interface graphique:
  - Table attributaire: toujours afficher les numéros des en-têtes de colonnes séquentielles.
  - Contrôle de référence de relation: Activer le bouton de formulaire uniquement lorsqu'une entité est paramétrée.
  - Afficher l'id de l'entité dans l'info-bulle de l'attribut.
  - Focalisation initiale sur un contrôle dans la boîte de dialogue d'authentification.
  - Temps d'expiration par défaut pour les éléments de barre de messages.
  - Add button\" state in postgis source select dialog
- Installation des fichiers d'en-tête manquants.
- Plantage lors de la sortie.
- Répertoire de cache réseau.
- Formulaire d'entité masqué derrière la fenêtre principale sous Windows.
- Édition hors-ligne: respecter les chemins relatifs.
- Édition hors-ligne: les attributs modifiés aboutissent dans la mauvaise entité.
- Offline editing: Don\'t crash with raster layers
- Le formulaire de relation s'agrandit à l'infini.
- Correction d'un plantage lors du chargement d'un style dans les propriétés de la couche.
- Correction d'un plantage lors de la fermeture de la table d'attributs en mode parqué.
- Correction du chemin mal configuré par défaut pour gpsbabel.
- Afficher le décompte correct des entités dans une règle qui impose de la géométrie.
- Correction d'un plantage lors de l'utilisation du moteur de rendu 2.5.D avec une couche non compatible.

{{<content-end >}}
