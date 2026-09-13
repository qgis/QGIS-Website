---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.18
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.18{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Release date: 2016-10-21

Il s'agit de la dernière version de la série 2.x. La version long terme (LTR) courante reste la version 2.14.x. La version 2.18.x apporte des améliorations graduelles par rapport à la version précédente. Le plus gros de nos efforts est maintenant focalisé sur le développement de la version 3.0 de QGIS qui est notre version nouvelle génération dont la distribution est prévue pour la fin du premier trimestre 2017.

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Sponsors de QGIS 2.18.0
Chaque année, nous recevons aussi le soutien de diverses organisations qui apprécient le travail que nous faisons et souhaiteraient faciliter l'effort de développement soutenu du projet. Ces sponsors sont listés ci-dessous avec nos remerciements !

{{<fund type="changelog" relativeImgPath=true >}}
## Général
### Fonctionnalité : Liens automatiques pour l’identification des résultats
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Fonctionnalité : Roulette souris sur les curseurs de la boîte de dialogue des couleurs
Avec QGIS 2.18 vous pouvez maintenant utiliser la roulette souris au-dessus des curseurs de la boîte de dialogue de la sélection des couleurs pour faire varier la valeur par de petits incréments. C'est un raccourci utile pour de petits ajustements dans les couleurs.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Ajout de jeux personnalisés de couleurs au menu déroulant du bouton des couleurs
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Fonctionnalité : Le sélecteur de couleur est maintenant contenu dans le panneau de style de couche
Avec QGIS 2.18 cliquer un bouton de couleur dans le panneau de style de couche affiche la boîte de dialogue du sélecteur de couleur dans le panneau de style lui-même au lieu d'une boîte de dialogue séparée. Ceci permet de modifier interactivement les couleurs avec pré-visualisation immédiate des résultats.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Étiquetage
### Fonctionnalité : Support pour liste de substitution pour l'étiquetage
Ajoute la possibilité de fournir une liste de substitution à effectuer dans les étiquettes de textes. Par ex. abréger les types de rues.

L'utilisateur peut exporter et importer des listes de substitution pour en faciliter leur réutilisation et leur partage.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Amélioration de l'algorithme de placement des étiquettes de ligne
Le mode d'étiquetage parallèle pour les couche de lignes a été grandement amélioré, avec un tout nouveau algorithme qui évite de placer les étiquettes sur les parties dentelées des géométries.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Étiquetage des polygones avec des étiquettes courbées le long du périmètre
Un nouveau mode d'étiquetage des polygones est ajouté dans lequel le périmètre du polygone est étiqueté avec des étiquettes courbées.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Rendu
### Fonctionnalité : Pré-visualisation des tuiles raster (couches WMTS et XYZ)
Dans les versions précédentes de QGIS, l'utilisateur devait attendre la fin du téléchargement de toutes les tuiles d'une couche pour pouvoir la visualiser. Ce n'est plus le cas maintenant, chaque tuile est affichée dès qu'elle est téléchargée, améliorant ainsi l'expérience utilisateur en diminuant significativement le temps d'attente avant affichage. De plus, les tuiles téléchargées précédemment, en plus haute ou plus faible résolution, peuvent être utilisées pour la pré-visualisation dans les zones où les tuiles ayant la bonne résolution n'ont pas encore été téléchargées.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Fonctionnalité : Le rendu des rasters peut être arrêté (couches WMS, WMTS, WCS et XYZ)
Cette amélioration augmente l'expérience utilisateur lors d'un travail sur des couches rasters provenant de serveurs à distance. Précédemment il fallait attendre la fin du téléchargement pour pouvoir zoomer ou déplacer la carte, car l'interface utilisateur était gelée en attendant. Ce n'est plus le cas maintenant car le rendu des couches rasters peut être arrêté à tout moment.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Gestion des données
### Fonctionnalité : Ajout d'un drapeau pour ne copier que les entités sélectionnées
L'extension d'édition hors-ligne est une extension de base, livrée avec QGIS et qui vous permet de modifier des jeux de données distants (ex: depuis une base de données) lorsque vous êtes hors-ligne, sur le terrain et de resynchroniser cette saisie lorsque vous êtes de retour au bureau. Cette amélioration permet d'améliorer les possibilités d'édition en mode hors-ligne pour travailler uniquement sur un sous-ensemble de couches volumineuses.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Formulaires et widgets
### Fonctionnalité : Permet le contrôle des étiquettes pour les widgets individuels d'édition
Permet de contrôler les étiquettes des contrôles de formulaire d'édition. Dans le mode de conception par glisser/déposer, un double clic sur une entrée permet de contrôler si l'étiquette doit être affichée individuellement par entrée de formulaire.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Fonctionnalité: Visibilité conditionnelle des onglets et des boîtes de groupe
Cette fonctionnalité ajoute une nouvelle option de configuration pour afficher ou masquer les onglets ou les boîtes de groupe des formulaires en mode de conception par glisser/déposer de manière conditionnelle.

La configuration est accessible via un double clic dans l'arbre de conception dans l'interface de configuration des champs.

Une expression peut être saisie pour contrôler la visibilité. L'expression sera ré-évaluée chaque fois que les valeurs du formulaire sont modifiées et l'onglet ou la boîte de groupe sera affiché/masqué de manière appropriée.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Fonctionnalité: Valeur de champ par défaut du côté client
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Composeur de Cartes
### Fonctionnalité : Vraies flèches du Nord
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Traitement
### Fonctionnalité : Algorithme de point sur une surface
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : L'algorithme de dissolution accepte des champs multiples
L'algorithme de dissolution permet maintenant une dissolution basée sur plus d'une valeur de champ. Dans les versions précédentes de QGIS une dissolution ne pouvait grouper des entités que par une seule valeur de champ.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Algorithme optimisé pour le découpage
L'algorithme de découpage a été optimisé pour les scénarios courants, conduisant à une amélioration dramatique des opérations de découpage. Par exemple :

**Découpage d'une couche de routes ayant 1 million de lignes par 2 polygones**

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

**Découpage d'une couche de points de 5 millions d'adresses par 2 polygones**

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Algorithme de cadres limites
Ce nouvel algorithme calcule le cadre limite (enveloppe) de chaque entité de la couche en entrée.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Algorithme pour combiner des lignes connectées
Cet algorithme joins toutes les parties connectées des géométries de chaîne multi-lignes, MultiLineString, en géométries de chaîne de lignes, LineString. Si des parties de la chaîne multi-lignes en entrée ne sont pas connectées, la géométrie en sortie sera une chaîne multi-lignes dans laquelle les parties pouvant être connectées seront combinées et contenant aussi les parties non-connectées.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Algorithme de limite de géométrie
Ce nouvel algorithme renvoie la limite combinatoire des géométries en entrée (c'est -à-dire l'enveloppe topologique de la géométrie). Par exemple, une géométrie de polygone aura une enveloppe constituée par les linéaires multi-segments de chaque anneau du polygone; une géométrie linéaire aura une enveloppe constituée des points de départ et d'arrivée de la ligne. Cet algorithme est valide uniquement pour les couches de polygones ou de lignes.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Fournisseurs de données
### Fonctionnalité : Support natif des couches de tuiles XYZ
Les tuiles raster au format XYZ sont maintenant supportées nativement avec les fournisseurs de données WMS, permettant d'afficher des cartes de base provenant d'autres sources sans ne plus avoir à recourir à des extensions telles que QuickMapServices ou OpenLayers.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## QGIS Server
### Fonctionnalité : Possibilité de segmenter les informations de géométrie d'une entité sur le serveur
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Extensions
### Fonctionnalité : Gestionnaire de BD : Ajout de la possibilité de mettre à jour une couche SQL
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programmation
### Fonctionnalité : Expose la fonction de référencement linéaire de GEOS pour QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Fonctionnalité : Nouvelles classes PyQGIS en 2.18
### Nouvelles classes de base
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Nouvelles classes de l'IG, widgets réutilisables
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Fonctionnalité : Nouvelle fonction d'expression
QGIS 2.18 ajoute plusieurs nouvelles fonctions dans le générateur d'expressions, y compris des fonctions pour l'interpolation d'angles/distances.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
