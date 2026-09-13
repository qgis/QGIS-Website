---
HasBanner: false
draft: false
releaseDate: '2020-02-21'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.12
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.12{#changelog312 }
![image1](images/projects/dbf38cfe3b603e7e0b840336d39b399a1a46e52d.png)

Release date: 2020-02-21

Si vous souhaitez de nouvelles fonctionnalités, une tonne de correction de bogues, cette version va pleinement vous satisfaire. QGIS 3.12 ajoute de nouvelles possibilités sur presque toutes les parties du logiciel. Depuis les masques d'étiquettes, en passant par le support natif de PG Raster jusqu'aux nouvelles fonctionnalités pour les couches de maillage et encore beaucoup d'autres fonctionnalités. Cette version propose des nouveautés pour chacun des utilisateurs. Comme toujours, nous vous rappelons que QGIS est un projet open source et que si vous le pouvez, n'hésitez pas à encourager notre travail par des dons, du sponsoring ou des contributions à la documentation du code, du site internet, etc.

**Remerciements**

Nous souhaitons remercier les développeurs, rédacteurs de documentation, testeurs et tous ceux qui ont volontairement donné du temps (ou donné de l'argent). La communauté QGIS espère que vous apprécierez cette version ! Si vous souhaitez donner un peu de votre temps, d'argent ou vous impliquer d'une autre manière pour rendre QGIS encore plus génial, faites un tour sur `qgis.org <http://qgis.org>`__ et donnez nous un coup de main !

QGIS est soutenu par des donateurs et des sponsors. La liste actuelle des donateurs, que leurs contributions financières au projet soient petites ou grandes, est disponible sur notre `liste des donateurs <http://qgis.org/en/site/about/sponsorship.html#list-of-donors>`__. Si vous souhaitez devenir un sponsor officiel du projet, veuillez visiter  `notre page de sponsoring <http://qgis.org/en/site/about/sponsorship.html#sponsorship>`__ pour les détails. Sponsoriser QGIS nous aide à financer nos rencontres développeurs semestrielles, maintenir l'infrastructure du projet et financer nos efforts de correction de bogues. La liste complète des sponsors actuels est fournie ci-dessous - un grand merci à tous nos sponsors !

{{<fund type="active" >}}

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait, nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous croyons que mettre à disposition un outil géographique de prise de décisions concourra à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Outils cartographiques
### Fonctionnalité : QgsMapLayerAction: ajout de l'entrée action sur la sélection dans le menu contextuel de légende
Une nouvelle entrée (Actions sur la séléction) est ajouté dans le menu contextuel des couches. Cette entrée est visible uniquement si une sélection est active sur la couche et que des actions peuvent être réalisées sur la couche concernée.

![imageQ1](https://user-images.githubusercontent.com/127259/74035907-7f334580-49bb-11ea-8d2d-b99eaa10aa89.png)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalité : Indique la distance entre la position du curseur actuelle et la celle déterminée par GPS.
Quand un équipement GPS est connecté, dès que l'utilisateur déplace son curseur sur le canevas, la barre de statut indique la distance et l'azimut depuis la position déterminée par le GPS vers la localisation du curseur.

Les paramètres de définition de distance et d'angle du projet sont utilisés pour cela.

![Peek 2020-01-14 16-06](https://user-images.githubusercontent.com/1829991/72318360-cd6c6600-36e7-11ea-9f2d-9a47d8772623.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: ajout paramétrage du format d'affichage des directions aux projets
L'onglet Outils cartographiques des Options des Préférences comporte un nouveau paramètre qui contrôle le format d'affichage par défaut des directions pour le nouveaux projets.
Tout nouveau projet héritera de ce paramètre par défaut.

La boite de dialogue Propriété du projet comporte également un nouveau paramètre de format d'affichage des directions spécifique au projet.

The intention is that whenever angular bearings are shown in QGIS, they will be formatted using the current project\'s bearing format settings.

Comprend également de nombreux ajouts intéressants dans l'API qui offrent un emplacment stable et facile à découvrir pour définir et récupérer des paramètres tels que le format des directions. 

![Peek 2020-01-09 11-08](https://user-images.githubusercontent.com/1829991/72029046-5fcbce80-32d0-11ea-8571-0ae8fa8e3bb0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Interface utilisateur
### Fonctionnalité : Déselection des tables suite à l'appui sur le bouton d'ajout de données PostgreSQL.
Lors de l'ajout de données PostgreSQL depuis le gestionnaire des sources de données, l'appui sur le bouton d'ajout de couche retire les couches de la sélection.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Fonctionnalité: affichage de la distance et la direction du déplacement dans la carte (pan) dans la barre d'état
We added the total pan distance and bearing in the status bar during canvas pan operations. Allows users to know exactly how far (and in what direction) they\'ve dragged the map.

![image5](images/entries/48c75d20d3805af3dad8c7faae3c3786a8f6fed0.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Une nouvelle option permet de définir le format de projet (qgs/qgz) par défaut 
Cela ajoute une nouvelle option globale pour définir le format de projet préféré

![imageQ2](https://user-images.githubusercontent.com/127259/72597971-2bc75d80-390f-11ea-84af-7f2c25d5568a.png)

Cette fonctionnalité a été financée par la Fondation GEM

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalité: Correction du dialogue des attributs invalides lors de la copie dans une autre couche
It\'s possible to copy features from one layer to another. If there are the same fields in the destination layer, then the attributes for them are taken from the original feature. If not, the default value is taken. Otherwise, the new attribute is null.

Si la couche de destination a des contraintes définies sur les attributs, l'utilisateur doit choisir une valeur autorisée ou rejeter ces valeurs. Auparavant, les valeurs étaient copiées telles quelles et invalides.

That\'s why now the attributes are checked against the constraints. And for all the invalid features a dialog pops up.

![copydialog2](https://user-images.githubusercontent.com/28384354/72243171-7e410b00-35eb-11ea-8903-11bd56cd9da6.gif)

Si un seul objet est collé, les options sont plus simples:

![copypastesingle](https://user-images.githubusercontent.com/28384354/72243125-5ce01f00-35eb-11ea-897e-0bccdcf083d7.png)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Fonctionnalité: Il est possible de glisser-déposer une couche vers le widget de choix de projection
\...to set the projection to match that layer. Just a little timesaving shortcut!

![Peek 2019-12-20 11-27](https://user-images.githubusercontent.com/1829991/71222288-b7070080-231b-11ea-89f4-af856dece4c3.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Algorithme Calculatrice raster : ajout de boutons manquants et de la validation d'expression 
Ajout des boutons pour ABS/MIN/MAX et la validation de l'expression

![image10](https://user-images.githubusercontent.com/142164/68952420-1bd0b780-07c0-11ea-88d1-2ad0a8b5591e.gif)

Cette fonctionnalité a été développée par Alessandro Pasotti
## Symbologie
### Fonctionnalité: animation de trace vectorielle et lignes de flux pour les couche de maillage
Mesh vector renderer now can visualize streamlines and particles on top of existing \"arrow\" mode.

![image11](images/entries/5b772e74d433e766b50023cd107aad9cb1d68de6.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: Masquage sélectif
A new advanced rendering feature has been added: selective masking. It allows the definition of \'masks\' areas around labels or point markers. These masks will \"un-draw\" only some symbol layers of other layers underneath, chosen by the user.

![image12](https://user-images.githubusercontent.com/1618556/62111873-d68c8680-b2b1-11e9-8cd4-19077f99a8ff.gif)

This feature was funded by [QGIS.CH and others through a cofunding campaign](https://oslandia.com/en/offre-qgis/selective-masking/)

This feature was developed by [Hugo Mercier (Oslandia)](https://www.oslandia.com)
### Fonctionnalité: lorsque la rotation des degrés décimaux ne parvient pas à être évaluée, retour à la valeur statique
La légende fonctionne enfin parfaitement avec la rotation définie par les données. QGIS pouvait déjà appliquer une rotation définie par les données aux symboles et aux couches de symboles individuels, mais cela a entraîné une légende cassée. La rotation des symboles (et des parties de symboles définies sur les couches de symboles) sur la légende peut désormais être contrôlée en modifiant les valeurs par défaut à côté des propriétés définies par les données.

L'ancien comportement consistait à toujours revenir à 0 en cas d'échec d'une expression. Ce qui a rendu difficile la création d'une légende appropriée dans certains cas.

par exemple. si vous aviez deux couches de symboles avec les expressions suivantes pour leur rotation

    "orientation"
    
et

    90 + "orientation"
    
qui serait deux couches de symboles orthogonaux (par exemple dénoter un angle droit), tournées par un champ d'orientation.

Désormais, dans la légende (et l'aperçu du symbole), les deux couches seraient affichées avec une rotation de 0, car il n'y a pas d'entité associée à une orientation de champ.

Le nouveau comportement consiste à revenir aux valeurs statiques et configurées, ce qui rend très intuitif la configuration de la légende pour ces cas.

**Avant**

![Peek 2019-12-08 09-18](https://user-images.githubusercontent.com/588407/70386652-acec1600-199b-11ea-8457-f9dd54c84272.gif)

**Après**

![Peek 2019-12-08 09-16](https://user-images.githubusercontent.com/588407/70386651-acec1600-199b-11ea-8ce2-27798aec38a7.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Fonctionnalité: ajouter un nombre de points basé sur la densité pour le remplissage de marqueur aléatoire
Cette fonction ajoute une méthode de comptage de points basée sur la densité au nouveau remplissage de marqueur aléatoire.

![image15](https://user-images.githubusercontent.com/1728657/67672096-c2881c00-f9a9-11e9-8394-d73505d05309.gif)

Cette fonctionnalité a été développée par Mathieu Pellerin
### Fonctionnalité: Type de couche de symbole de remplissage de marqueur aléatoire
This feature adds a new fill symbol layer type \"Random marker fill\". It allows polygon features to be rendered using a marker symbol placed at random locations within the polygon boundary.

Les options incluent :
- nombre de symboles de marqueur à rendre pour le polygone
- si les marqueurs rendus près des bords des polygones doivent être coupés ou non à la limite du polygone
- un nombre aléatoire facultatif , pour donner un placement cohérent des marqueurs chaque fois que les cartes sont actualisées (permet également un placement aléatoire pour jouer avec QGIS server et le rendu basé sur les tuiles)

![image16](https://user-images.githubusercontent.com/1829991/66734145-51267480-eea5-11e9-9e0a-3bfeee15f976.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Ajouter une option pour définir la couleur de rendu des pixels nodata dans les couches raster
Allows raster nodata pixels to be colored in a specific (non-transparent) color. Designed to match the \"Display background value\" option from ArcMap.

![image17](https://user-images.githubusercontent.com/1728657/64846100-f4c9fe00-d635-11e9-8acb-367ad2dd2915.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Étiquetage
### Fonctionnalité: Permet de supprimer la position d'étiquette personnalisée
Nous avons ajouté une nouvelle option de possibilité pour pouvoir supprimer la position d'étiquette personnalisée en appuyant sur la touche DEL lors du déplacement de l'étiquette.

![image18](images/entries/e8064c56705b7a74befa85e8a34e7b7311626f0a.gif)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch)
## Diagrammes
### Fonctionnalité: Prise en charge des effets de peinture pour le rendu de diagramme
this new feature allows for diagrams to use paint effects, including drop shadows, outer glows, etc\...

![image19](images/entries/37d0a22707eca463e5aba7c0a349b2d8029fb823.gif)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New diagram type \"stacked bars\"
With this new feature users will have possibility to create stacks bars of varying colors for each attribute on top of each other vertically or horizontally. Designed to match the \"Stacked\" chart renderer option available in ArcGIS.

![image20](images/entries/933c25cf0cd8997e177eee809b4fa26462b6d8c2.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: option d'espacement pour les diagrammes à barres pour les couches vectorielles
Permet un espacement contrôlé par l'utilisateur entre chaque barre du graphique.

![image21](images/entries/7906ea6467d1d5ea19550ce1711fcc277df709a0.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Nouvelle option pour contrôler la direction angulaire du diagramme circulaire
Cette fonction permet de contrôler si les sections sont rendues dans le sens horaire ou antihoraire.

![image22](images/entries/c2484d36648c335d16d1e3a45ac1a132ca2baafe.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Rendu
### Fonctionnalité: Boutons Play / Stop pour la lecture de la couche de maillage
It is possible to switch the timeframes of mesh layer\'s datasets by play/stop button. The playback setting could be adjusted in the time setting dialog.

![image23](images/entries/4799685965addef6ca2c788d82eea77e67e2f1f3.webp)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
### Fonctionnalité: à la volée, rééchantillonnage des données définies sur les faces aux sommets (couche de maillage)
Pour les jeux de données définis sur les faces, on peut choisir d'interpoler les données aux sommets avec la méthode neighbour average. Lorsqu'aucune méthode d'interpolation des données n'est choisie, chaque pixel sur une seule face a une seule valeur / couleur. Avec les données sur les sommets, le rendu de chaque pixel est interpolé à partir des valeurs sur les sommets, ce qui rend les figures plus lisses.

Utilisez le panneau de style Contours de maillage pour basculer entre les méthodes d'interpolation des données.

![image24](images/entries/c9c38ee8c59693b2971ab6269db22681a61002a1.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: Prise en charge du temps de référence du maillage
Pour différents types d'ensembles de données, par exemple GRIB et NetCDF, l'heure de référence dans la boîte de dialogue des paramètres d'heure QGIS est préremplie à partir des données brutes et n'a pas besoin d'être définie manuellement. Nous avons également corrigé divers bugs liés à l'analyse temporelle, donc dans QGIS 3.12, il devrait être possible de formater et d'afficher votre temps dans des tracés / animations de la manière appropriée:
- S'il existe une référence temporelle valide fournie avec des groupes d'ensembles de données, cette référence temporelle est utilisée pour afficher l'heure (en utilisant le temps absolu).
- S'il n'y a pas de temps de référence fourni, le temps est affiché en utilisant le temps relatif, et une référence de temps peut être réglée par l'utilisateur pour afficher le temps absolu.
- Lorsqu'aucune référence d'heure n'est fournie, la valeur par défaut est la date et l'heure actuelles définies avec 00:00:00.

Un bouton est ajouté pour recharger le temps de référence fourni avec les groupes de jeux de données si nécessaire.

Il ajoute également une nouvelle fonctionnalité pour permettre à l'utilisateur de définir l'unité de temps du fournisseur avec une zone de liste déroulante si cette unité de temps est différente des heures.

![imageQ3](https://user-images.githubusercontent.com/7416892/70955568-bb939680-2047-11ea-9857-8aba122e43dd.png)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Fonctionnalités 3D
### Fonctionnalité: rendu de terrain de couche de maille 3D
Il est possible de rendre la couche de maillage dans la vue 3D en tant que terrain.

L'utilisateur peut choisir d'activer / désactiver les triangles lisses et le filaire. Il est possible de choisir la largeur de ligne et la couleur de ligne du filaire, de changer l'échelle verticale et de choisir le style de rendu (couleur unique ou dégradé de rampe de couleur).

Il existe deux entrées pour rendre la couche de maillage dans la vue 3D:
- choisissez le maillage comme terrain dans le widget de configuration
- activez la vue 3D dans les propriétés de la couche.

L'utilisateur peut choisir ces paramètres:
- activer / désactiver les triangles lisses
- activer / désactiver le filaire
- choisissez la largeur de trait et la couleur de trait du filaire
- changer l'échelle verticale
- choisissez le style du rendu: couleur unique ou dégradé de rampe de couleur
- définit l'ombrage de la rampe de couleur comme pour la couche raster

Pour l'instant, le maillage peut être rendu sous forme de TIN mais le jeu de données de rendu n'est pas pris en charge. Cependant, l'infrastructure est adaptée pour une future série de travaux.

![mesh3dsettings](https://user-images.githubusercontent.com/7416892/72482783-41d10300-37d5-11ea-9a21-8f906abcb14a.gif)

![image27](images/entries/f19c25acbd1eb462cdc0365d3af3f706c1b4d2fe.gif)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: chargez les données de couche vectorielle 3D en arrière-plan + mosaïque
Cela ajoute la prise en charge du chargement en arrière-plan des données des couches vectorielles dans les vues de carte 3D. Jusqu'à présent, le chargement gelait complètement l'interface graphique - cela pouvait prendre plusieurs secondes selon la complexité des données d'entrée.

Le rendu de couche vectorielle et le rendu basé sur des règles ont été convertis pour utiliser QgsChunkedEntity qui est déjà utilisé pour le rendu du terrain. Il y a deux autres améliorations en plus du déverrouillage de l'interface graphique:
- le processus de chargement est multithread au lieu d'utiliser un seul noyau
- le chargement se fait en tuiles - il est donc possible de voir les tuiles avec des données 3D apparaissant pendant que d'autres données sont encore en cours de chargement

There is a new configuration option in the 3D tab of vector layers - it determines how deep the quadtree will be. For example, one zoom level means there will be a single tile for the whole layer. Three zoom levels means there will be 16 tiles at the leaf level (every extra zoom level multiplies that by 4, so I have limited GUI to max. 8 levels which gives \~16K tiles which is already a lot).

How a vector layer\'s tiling quadtree gets populated: all internal tree nodes are empty and thus the 3D map scene tries to immediately replace them with their children - this goes until leaf nodes are reached. Only nodes at the leaf level currently hold any data. This may change in the future when we introduce more elaborate strategies - for example, internal nodes may contain a small percentage of features of the child nodes (this would allow us to show something while zoomed out a lot, not requiring to load all data).

For debugging purposes, there is also a new configuration option \"show bounding boxes\". This allows you to see the bounding box of each tile (especially useful if there are some issues with tiles not showing up when they should).

Cette fonctionnalité a été financée par la subvention QGIS.org.

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
## Mises en page de cartes
### Fonctionnalité: Autorisez le glisser-déposer des images sur les composeurs de carte
Cette nouvelle fonctionnalité permet à l'utilisateur par exemple de faire glisser un svg depuis un explorateur de fichiers sur la mise en page pour créer un nouvel élément image contenant cette image svg.

![image28](images/entries/21b9f2fba7bf1576f794410fd238ef7553154d53.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: nouveau type d'élément dans le composeur: tables fixes créées manuellement
Ce nouveau type d'élément permet la création de tableaux dont le contenu est entré manuellement par les utilisateurs (c'est-à-dire de style tableur) afin que les utilisateurs puissent créer des tableaux entièrement personnalisés. Prend en charge le contrôle du contenu des cellules personnalisées, des couleurs de premier plan et d'arrière-plan (et bientôt, des hauteurs de ligne et de colonne prédéfinies). Une toute nouvelle boîte de dialogue de conception de table a été ajoutée qui permet de personnaliser ces tables.

![image29](images/entries/95cfa9a8c44fb0141474d80e4b3a5e7f98352e70.webp)

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Ajoutez un contrôle utilisateur sur les formats numériques de la barre d'échelle
Vous avez maintenant la possibilité de contrôler le format numérique utilisé par une barre d'échelle de mise en page.

You can manage all the formatting properties for the numbers in scale bars, including whether they want a thousand separator, decimal places, scientific notation, etc. Very useful in the case of making maps for audiences outside of the current QGIS locale, or when you\'d just prefer to vary the style from the locale defaults (e.g. adding thousands separators when the locale default is to hide them).

![image30](images/entries/99c97baaee3e5930bca0cb63db1391b6fd49b34f.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: permet de styliser les table d'attributs de mise en page en utilisant les couleurs de premier plan et d'arrière-plan des styles conditionnels correspondants
When the new \"Apply layer conditional styling colors\" option is enabled in the layout attribute table settings, any conditional styling rules present in the layer will be applied inside the layout attribute table (foreground and background colors only, for now!).

![image31](images/entries/baded0d05539439d58e6df5a8f24157293cf8022.gif)

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Ajouter un champ de recherche au gestionnaire de mise en page
Permet de filtrer la liste des mises en page dans un projet par nom, pratique quand un projet a plusieurs mises en page ..!

![image32](images/entries/fb510c6c079d55dab2dd22f02c7c5355b317ac47.webp)

Cette fonctionnalité a été développée par Nyall Dawson
## Expressions
### Fonctionnalité: Rechercher des balises pour les fonctions
Tags on static expression functions to make them more retrievable. Functions like array_to_string are listed when the user enters \"split\" or \"convert\" or - like before - a part of the function name.

![image33](images/entries/689a669fe84721d7574aba7e595e019a9936f0b9.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Fonctionnalité: Liste des valeurs de couche référencées
Lorsqu'un champ est une RelationReference, ValueRelation et ValueMap, il y a la possibilité non seulement d'afficher les valeurs de la couche actuelle mais également les valeurs possibles dans la couche référencée / les possibilités configurées.

![image34](images/entries/394c762c41e71764d9be397b718252eddb2dbd3e.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Fonctionnalité: Nouvelles expressions
- `is_empty(geom)`, check if a geometry is empty (geometry that contain no coordinates)
- `is_empty_or_null(geom)`, check if a geometry is empty or NULL (does not have geometry)
- `hash`, cryptographic hashes functions using [QCryptographicHash](https://doc.qt.io/qt-5/qcryptographichash.html). Use case is the same as PgCrypto but in client side for all supported format.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Feature: New algorithm \"Rename table field\"
Prend une couche en entrée, un champ existant et un nouveau nom pour le champ, et sort une nouvelle couche avec le champ sélectionné renommé.

While this result could also be achieved with the Refactor Fields algorithm, Refactor Fields isn\'t particularly model friendly. It relies on a constant, fixed table structure, and can\'t adapt to input tables with different field structures.

En revanche, ce simple algorithme Renommer le champ s'adapte parfaitement à l'utilisation du modèle, car il fonctionne sur un seul champ et ne modifie pas tous les autres champs.

![image35](images/entries/c01edc8ee51dff2b4df8f825e0dcaf27940e4aba.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Expressions stockées
- Stocker les expressions utilisateur
- Effacer l'icône / l'action de l'éditeur

![expression-storage-opt](https://user-images.githubusercontent.com/142164/70983414-faae0000-20b8-11ea-9f25-14b338d4c680.gif)

See also QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/135>

This feature was funded by [Salvatore Fiandaca](https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Fonctionnalité: répertorier les valeurs de couche référencées dans Expression Builder
Lorsqu'un champ est une RelationReference, ValueRelation et ValueMap, il y a la possibilité non seulement d'afficher les valeurs de la couche actuelle mais également les valeurs possibles dans la couche référencée / les possibilités configurées.

*age* is a ValueMap, *species* is a ValueRelation and *island_id* is a RelationReference

![uniquevalues](https://user-images.githubusercontent.com/28384354/70978774-ab63d180-20b0-11ea-901b-d51d44fa8fa4.gif)

Dans l'exemple, nous avons les personnes:
- *George (à Cuba, dans la vingtaine, humain) Paul (au Vietnam, dans la trentaine, humain) Ringo (au Venezuela, dans la quarantaine, chat) John (au Vietnam aussi, dans la quarantaine, table)*
- Et les entrées dans la couche pays sont *URSS, Cuba, Vietnam, Birmanie, Venezuela, Corée du Nord*

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Fonctionnalité: Ajouter des fonctions d'expression pour la conversion vers / depuis wkb
- `geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → a point geometry object` Returns a geometry created from a Well-Known Binary (WKB) representation.
- `geom_to_wkb( $geometry ) → binary blob containing a geometry object` Returns the Well-Known Binary (WKB) representation of a geometry as a binary blob.

Adds geom_from_wkb and geom_to_wkb, which mirror the existing geom_from_wkt/geom_to_wkt functions but for WKB representations of geometries.

Since QGIS 3.6 we\'ve had good support for binary blob values in expressions and field values, so adding these functions allows users to work with binary blob fields containing WKB representations of geometries (e.g. with a geometry generator showing the encoded geometries)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: is_valid expression
`is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → true` Returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules

Add an is_valid function to the expressions, which reuses GEOS is valid and returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules.

Cette fonctionnalité a été développée by Pete King
### Feature: Add datetime_from_epoch (MSec from epoch) expression function
`datetime_from_epoch(1483225200000) → 2017-01-01T00:00:00` Returns a datetime whose date and time are the number of milliseconds, msecs, that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (Qt.UTC), and converted to Qt.LocalTime.

Cette fonctionnalité a été développée par Richard Duivenvoorde
### Fonctionnalité: fonction rotate()
`rotate($geometry, 45, make_point(4, 5)) → geometry rotated 45 degrees clockwise around the (4, 5) point` Returns a rotated version of a geometry. Calculations are in the Spatial Reference System of this geometry.

Cette fonctionnalité a été développée by Raymond Nijssen, Nyall Dawson
### Fonctionnalité: permet de generer des fonctions aléatoires
- `rand(10, 80, 1) → 30` Returns a random integer within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.
- `randf(10, 80, 1) → 19.37136508087729` Returns a random float within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.

This feature adds an optional seed parameter to rand() and randf() functions This is very useful if you want the result to be deterministic, for instance to assign random but fixed colors to features. Using color_hsb(rand(0,360,\$id),50,50) for instance yields always the same color for the same feature. We also improves the rand() function, which didn\'t work for high values (over 32000) by using Qt\'s QRandomGenerator instead of qrand (which it seems was deprecated in Qt 5.11).

Cette fonctionnalité a été développée par olivierdalang
### Feature: Language support for format_date() and to\_{date,datetime,time}()
- `format_date('2012-05-15','d MMMM yyyy','fr') → '15 mai 2012'`
- `format_date('2012-05-15','d MMMM yyyy','it') → '15 maggio 2012'`
- `format_date('2012-05-15','d MMMM yyyy','en') → '15 May 2012'` Formats a date type or string into a custom string format. Uses Qt date/time format strings. See QDateTime::toString.

By default, those expression use the application\'s locale. The addition of an optional language parameter allows handling of dates that wouldn\'t match that default locale (say for e.g. an English system running QGIS trying to transform a French-formatted string into a date object).

Cette fonctionnalité a été développée par Mathieu Pellerin
## Numérisation
### Fonctionnalité: Modifier les attributs non valides lors du copier / coller dans une autre couche
Sur les fonctionnalités de copier-coller d'une couche à une autre, dans le cas où il y a des contraintes (par exemple non nulles) sur la couche de destination, qui ne peuvent pas être remplies automatiquement par les valeurs par défaut, une boîte de dialogue apparaît pour corriger les attributs non valides ou ignorer volontairement les contraintes .

![image38](images/entries/5bd43dd39955e37ace130038b968550c6fa260c5.gif)

This feature was funded by [Amt für Wald und Wild Zug](https://www.zg.ch/behoerden/direktion-des-innern/wald-und-wild)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Fonctionnalité: Accrochage de la parallélisation du cache
In previous version of QGIS, the snapping index cache was built sequentially and you had to wait for all your layers to be indexed before starting edition. Thanks to the QGIS.org grant program, QGIS now builds the snapping index cache in parallel for each layer, so it speeds up the whole process. Snapping has also been relaxed, meaning that you don\'t have to wait for the cache to be complete, you can start editing and snapping information will appear as soon as they are ready.

![image39](images/entries/d77958db7175267448d9b94950532dee8b90145c.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Gestion des données
### Fonctionnalité: Améliorations de l'exportation DXF
Nous avons fait une refonte du processus d'exportation DXF. Cela solidifie le processus d'exportation et offre de nouvelles fonctionnalités.
- Les styles de géométries sont exportés et des blocs sont utilisés
- Les coordonnées Z des géométries 3D sont préservées
- Labels are exported with their anchor points and horizontal and vertical alignment or quadrant settings respected

The whole DXF export process has also been made ready for running in a thread. With this in place, it\'s now only one step away from being sent to the background, allow cancellation of an ongoing export process or being exposed as a processing algorithm.

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Formulaires et widgets
### Fonctionnalité: créer une entite géométrique à partir de l'éditeur de relations
We added the ability to add a new feature and digitize its geometry directly from within the relation editor widget. It\'s now easier to add a geometric feature related to your currently displayed parent feature.

![image40](images/entries/fe03aefab87464e54b70569e6d05ad09a1b8fae5.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Fonctionnalité: améliorer la boîte de dialogue de sélection des entites
From the relation editor widget, you can link your currently displayed feature with existing features. The feature selection dialog allows you to choose these features. Thanks to the QWAT user group, feature selection is now shared with the canvas\' one so it is easy to find out and pick the feature you want to link. We have also added the ability to filter displayed features (selected ones, visible on map, matching an expression\...) reusing the same widgets already existing in attribute form.

![image41](images/entries/a65364e6a48857a8720643c41a3cb17461d9e16a.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: UX improvements in drag\'n\'drop form designer
The drag\'n\'drop form designer has received some nice UX improvements
- Les deux listes (champs disponibles et arborescence) sont désormais synchronisées: chaque fois que vous sélectionnez une entrée dans une liste, l'élément correspondant est sélectionné dans l'autre.
- Les boîtes de dialogue de configuration cachées (sous double-clic) ont été placées dans le panneau de droite

![image42](images/entries/5f47cb6311a9bffef94128a703719d709deb995a.gif)

Cette fonctionnalité a été financée par QGIS.org bugfixing

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
## Légende des couches
### Fonctionnalité: Prise en charge de l'affichage des graphiques de légende WMTS dans l'arborescence des couches
Nous avons ajouté la prise en charge de l'affichage des graphiques de légende WMTS directement dans l'arborescence des couches, comme c'est déjà le cas avec les graphiques de légende WMS.

Exemple :

![imageQ4](https://user-images.githubusercontent.com/1298852/72462785-33351c80-37d2-11ea-98f2-ce0d5221e1f5.png)

Sample use case: <https://wmts10.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>

This feature was developed by [Sandro Mani](https://api.github.com/users/manisandro)
## Outils d'analyse
### Fonctionnalité: exportation fluide des contours à partir de la couche de maillage
A new algorithm in QGIS's analysis library API to export directly contour lines and polygons is added. The method is not based on GDAL algorithms, but directly uses mesh layer triangular mesh interpolation methods. It is both fast and with smooth shapes, matching rendered images from QGIS. You can try the new processing algorithm in Crayfish processing toolbox.

![image44](images/entries/044ad55bfb4287026b4e002c46c8687093488d22.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: Prise en charge des ensembles de données définis sur les faces dans QGIS Mesh Calculator
Vous pouvez utiliser la calculatrice de maillage pour tous les types de jeux de données, définis sur les faces et les sommets. De plus, il permet aux utilisateurs de stocker le résultat de la calculatrice de maillage sous un nom ou un format différent. Cela permet par exemple de travailler avec des données FLO-2D ou HEC-RAS dans la calculatrice de maillage QGIS

![image45](images/entries/044d52fe937887854583ecfdc551e73eafb94a41.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Traitement
### Fonctionnalité: empaqueter de nouvelles couches dans le GeoPackage existant
Nous avons amélioré l'algorithme de traitement *des couches de package* existant pour pouvoir ajouter de nouvelles couches aux GeoPackages existants. Pour cela, il vous suffit de désactiver le paramètre OVERWRITE et de spécifier un GeoPackage existant.

![image46](images/entries/35d87f4826aad132de4a0b99ac7c775f6aa9b029.webp)

This feature was funded by [BikePlan](https://www.bikeplan.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité: Logique floue - Fuzzfiy Raster (appartenance linéaire)
L'algorithme de raster Fuzzify (appartenance linéaire) est une implémentation native d'un algorithme de logique floue. Il transforme un raster en entrée en un raster flou et affecte ainsi des valeurs comprises entre 0 et 1 suivant une fonction d'appartenance floue linéaire. La valeur de 0 n'implique aucune appartenance à l'ensemble flou défini, une valeur de 1 représente l'appartenance complète. Entre les deux, le degré d'appartenance des valeurs raster suit une fonction d'appartenance linéaire.

![image47](images/entries/bfb37d710293c252dae11b67b25bdc1431f13815.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Logique floue - Fuzzfiy Raster (power membership)
L'algorithme de raster Fuzzify (power membership) est une implémentation native d'un algorithme de logique floue. Il transforme un raster en entrée en un raster flou et affecte ainsi des valeurs comprises entre 0 et 1 à la suite d'une fonction d'appartenance floue de puissance. La valeur de 0 n'implique aucune appartenance à l'ensemble flou défini, une valeur de 1 représente l'appartenance complète. Entre les deux, le degré d'appartenance des valeurs raster suit une fonction d'appartenance au pouvoir.

![image48](images/entries/7a81ecd4414ee39b37e575863687615c88e9a856.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Logique floue - Fuzzfiy Raster (small membership)
The Fuzzify raster (small membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'small\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'small\' membership function. The \'small\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image49](images/entries/2bef948a7b02bd26208ca98e9ddb243d46d104a6.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Logique floue - Fuzzfiy Raster (large membership)
The Fuzzify raster (large membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'large\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'large\' membership function.The \'large\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image50](images/entries/10963d11812664a76d4fc3fac72777c34a08c767.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Logique floue - Fuzzfiy Raster (gaussian membership)
The Fuzzify raster (gaussian membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'gaussian\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'gaussian\' membership function. The gaussian function is constructed using two user-defined input values which set the midpoint of the gaussian function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image51](images/entries/58068dc6518a0df20a39df69ea4175f7b196b049.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Fuzzy Logic - Fuzzfiy Raster (near membership)
The Fuzzify raster (near membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'near\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'near\' membership function. The near function is constructed using two user-defined input values which set the midpoint of the near function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image52](images/entries/a4873da4c5e782a14caaa02f279ef92ba5bf5a38.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: algotithme Port Densify by count en C ++
We ported the Densify by count algorithm to C++ in order to enhance it\'s speed when compared to the previous Python implementation. The new algorithm also exposes the count parameter as dynamic parameter so that it can be controlled by expressions or field values.

![image53](images/entries/680eb97f65d08de5541f4b1f5ac4425f45988cc2.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Porter des points aléatoires dans l'algorithme d'extension en C ++
We ported the Random points in extent algorithm to C++. This boosts it\'s speed when comparing it to the previous Python implementation. The new algorithm also exposes an advanced parameter of maximum numbers of retrys for the algorithm when searching for randomly placed points that respect a certain distance between all points.

![image54](images/entries/c452431d9a2cd9f9f76869cf98e09e18bf2a81a4.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Fonctionnalité: Algorithme de densité de ligne
Dans cette version, nous avons ajouté un algorithme natif pour calculer la densité de lignes basée sur le raster. Cet algorithme calcule la densité de ligne en fonction d'un rayon de recherche et des poids des lignes à l'intérieur du rayon de recherche. L'algorithme a été porté pour fournir plus de fonctionnalités de l'extension ArcGIS Spatial Analyst dans QGIS.

![image55](images/entries/b28bbe3d5129ccc5dd61585dc1a9e31383a59c6f.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Feature: New algorithm \"Repair Shapefile\"
Nous avons ajouté un nouvel algorithme qui utilise GDAL pour réparer les fichiers de formes qui ont un fichier .SHX cassé ou manquant.

![image56](images/entries/c3a6a174187284126ea0af289614505ab8c0c593.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add new algorithm \"Detect Dataset Changes\"
Cet algorithme compare deux couches vectorielles et détermine quelles entités sont inchangées, ajoutées ou supprimées entre les deux. Il est conçu pour comparer deux versions différentes du même ensemble de données.

Lors de la comparaison d'entités, les géométries d'entités originales et révisées seront comparées les unes aux autres. Selon le paramètre Comportement de comparaison de géométrie, la comparaison sera effectuée à l'aide d'une comparaison exacte (où les géométries doivent correspondre exactement les unes aux autres, y compris l'ordre et le nombre de sommets) ou à une comparaison topologique uniquement (où la zone des géométries est-elle considérée comme égale si toutes les arêtes de leurs composants se chevauchent. Par exemple, les lignes ayant les mêmes emplacements de sommet mais la direction opposée seront considérées comme égales par cette méthode). Si la comparaison topologique est sélectionnée, les valeurs z ou m présentes dans les géométries ne seront pas comparées.

Par défaut, l'algorithme compare tous les attributs des entites d'origine et révisées. Si le paramètre Attributs à considérer pour la correspondance est modifié, seuls les attributs sélectionnés seront comparés (par exemple, permettant aux utilisateurs d'ignorer un horodatage ou un champ ID qui devrait changer entre les révisions).

Si aucune entité des couches d'origine ou révisée n'a de géométrie associée, il faut veiller à ce que ces entités possèdent un ensemble unique d'attributs sélectionnés pour comparaison. Si cette condition n'est pas remplie, des avertissements seront émis et les sorties résultantes peuvent être trompeuses.

L'algorithme génère trois couches, une contenant toutes les entites considérées comme inchangées entre les révisions, une contenant les entites supprimées de la couche d'origine qui ne sont pas présentes dans la couche révisée et une contenant des entites s'ajoutant à la couche révisée qui ne sont pas présentes. dans la couche d'origine.

![image57](images/entries/e38dcea12e1198341eb9f0bd45a33ebf7eda390b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: New mode to \"Join Attributes by Location\" to take attributes from matching feature with largest area of overlap only
This allows for easy polygon-\>polygon joins, where you expect there to be only a single matching feature and don\'t want to include features which are just touching or have just tiny sliver polygon overlaps.

![image58](images/entries/27b8e5e11deca93ffade31b86edc712ce918d179.webp)

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Ajouter un algorithme de transformation affine native pour les vecteurs
Offre les avantages suivants par rapport aux versions GRASS/ SAGA :
- Prise en charge complète des valeurs z / m et gestion des géométries courbes sans perte de courbes
- Fonctionne avec tous les types de données natifs, pas besoin de transformation de format
- Prise en charge des paramètres dynamiques (données définies, par entite) de traduction / mise à l'échelle / rotation
- Permet la transformation et la mise à l'échelle des valeurs Z et M (si présentes)
- Prend en charge le mode d'édition sur place

![image59](images/entries/1bfee3c2e208ecca6c235d96f83966ec808a0b1c.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: add gdal_viewshed algorithm
Expose new gdal_viewshed tool via Processing toolbox. Note: this requires GDAL \>= 3.1.

Cette fonctionnalité a été développée par Alexander Bruy
## Explorateur
### Fonctionnalité: Personnalisation des éléments affichés dans le navigateur
Add customization of the items shown in browser to the Interface Customization dialog. User can hide some of the root items in the browser panel (e.g. Favourites, PostGIS provider, MSSQL, Oracle, Volumes, \...)

![image60](images/entries/5e8e9037420b83cd44d4e1994d4119e4ae92c8aa.webp)

This feature was funded by [Limerick City and County Council](https://www.limerick.ie/council)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: Afficher les fichiers html dans le panneau du navigateur
Cette fonctionnalité permet d'afficher et d'ouvrir les fichiers .htm (l) à partir du panneau du navigateur. Ils sont souvent utilisés pour documenter des fichiers de données ou des projets de mappage.

![image61](images/entries/0db8930d20ca6f2fbf5b29593afdcf59e1af8d1e.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Show \"Open Document\...\" action in browser
Lorsque vous cliquez avec le bouton droit sur certains fichiers dans le navigateur, ils pourront être ouverts avec l'application externe par défaut pour ce type de fichier

Par exemple. Les fichiers PDF s'ouvriront avec la visionneuse PDF externe par défaut.

Works with PDF, ODS, XLS(X), CSV, TXT, PNG, JPEG, TIFF, SVG (other types will likely need more work, since they aren\'t currently shown in the browser).

![image62](images/entries/447f201d2342a64912bbef1e1d0aa3ebb8963ae4.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Autoriser la personnalisation des éléments affichés dans le navigateur
You can now customize items shown in the browser. User can decide (in the Interface Customization dialog) to hide some of the root items in the browser panel (e.g. Favourites, or POSTGIS provider, \...)

![Screenshot 2020-01-09 at 09 17 05](https://user-images.githubusercontent.com/804608/72050388-466f5600-32c1-11ea-94f5-092cc8471243.png)

Cette fonctionnalité a été financée par Limerick City and County Council

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Fonctionnalité: Ajouter une action d'actualisation des services OGC
Vous pouvez maintenant actualiser les services OGC dans le navigateur. Ci-dessous, une capture d'écran montrant un exemple de fonctionnement de cette fonction dans les connexions WMS / WMTS:

![OGCrefreshonaction](https://user-images.githubusercontent.com/2663775/71974919-cfd04b00-3223-11ea-834d-ff016c70a8c6.gif)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
## Fournisseurs de données
### Fonctionnalité: icône de collection de couches WMTS modifiée
Il s'agissait d'un changement de l'icône utilisée pour l'élément de collection de couches WMTS, un schéma de base de données a été utilisé à la place d'une icône liée à WMTS. Une icône WMS générale est maintenant utilisée.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Fonctionnalité: Ajout de la propriété URL de métadonnées dans l'onglet de métadonnées de couche pour les services WMS / WMTS et WCS
This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Fonctionnalité: Récupérer et afficher les métadonnées des dimensions pour une métadonnée de couche WMS
![image65](images/entries/d058ac6b89a8d06169b06580843967ad26e1ef54.webp)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Fonctionnalité: Ajout d'une action de rafraîchissement aux entrées des services OGC
![image66](images/entries/7ce331ee78be7f8b0693c653ecc58916d70a1a92.gif)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Fonctionnalité: mailles empilées 3D
MDAL et QGIS prennent désormais en charge les maillages empilés 3D, en particulier pour le format TUFLOW-FV. Pour cette version, vous devez choisir la méthode de calcul de moyenne appropriée dans l'interface QGIS et vous pouvez parcourir les données de manière similaire à tout autre ensemble de données 2D.

![image67](images/entries/dc3d85153d9bcecdf7ebbc6433c7cb40319e00dd.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité: correction de nombreux problèmes d'encodage de fichiers de formes
Cela corrige la gestion (cassée par la conception?) De l'encodage Shapefile, qui est un problème récurrent depuis des années dans QGIS.

Voir discussion à
- [#21264](https://github.com/qgis/QGIS/issues/21264)
- <http://osgeo-org.1560.x6.nabble.com/Shapefile-with-file-cpg-codepage-td5275106.html>
- <http://osgeo-org.1560.x6.nabble.com/QGIS-ignore-the-cpg-files-when-loading-shapefiles-td5348021.html>

(+ d'autres !)

The situation was that we had two different code paths for handling GDAL side attribute decoding OR QGIS side decoding. Unfortunately, they are both incompatible with each other, and due to GDAL API for this, we can\'t unify the two approaches. (More technical detail in the commit log message!)

Alors maintenant, nous :
- always do the decoding on QGIS\' side. This allows users to manually override a shapefile\'s declared encoding because they are often incorrect!
- use a port of GDAL\'s shapefile detection logic (it\'s not exposed in GDAL API, so I had to re-implement it here) so that we default to reading shapefiles by respecting the embedded encoding information (via CPG files or DBF LDID information)
- Completely remove the confusing/broken \"Ignore shapefile encoding declaration\" option, as it\'s no longer required \-- users are ALWAYS able to manually change the encoding of shapefiles layers if needed
- Always show users the detected embedded encoding in the layer properties, instead of always showing \"UTF-8\" when the embedded encoding information is used

This should give the best of both worlds \-- a nice default behavior resulting in shapefiles being read with the correct encoding, whilst still allowing users to override this on a layer-by-layer basis as needed.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Prise en charge de l'édition de type de courbe Oracle
Dans les versions antérieures de QGIS, il n'était pas possible de modifier certains types de géométrie provenant d'une base de données Oracle. Nous avons ensuite ajouté le support d'édition pour les types de géométrie suivants:
- CircularString(Z)
- CompoundCurve(Z)
- MultiCurve(Z)
- CurvePolygon(Z)
- MultiSurface(Z)

Cette fonctionnalité a été financée par Lille Métropole

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Fonctionnalité: Prise en charge du raster MBTiles dans le fournisseur WMS
Cette fonctionnalité ajoute la prise en charge de la carte raster en mosaïque MBTiles au fournisseur WMS afin qu'il utilise les mêmes chemins de code comme les tuiles WMTS ou XYZ. Voici les avantages de l'approche via le fournisseur WMS:
- mise à l'échelle correcte des tuiles sur un affichage haute résolution
- mieux regarder sans zoomer sur la résolution native des tuiles. Le fournisseur WMS utilise une mise à l'échelle fluide tandis que GDAL utilise le voisin le plus proche par défaut.
- map tile showing up while rendering (with GDAL it\'s blank map until everything is loaded)
- possibilité d'utiliser un widget curseur à l'échelle de tuiles
- plus rapide - principalement un effet secondaire du chargement de moins de tuiles sur un affichage haute résolution

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### Fonctionnalité: fournisseur de données raster PostGIS natif
Il s'agit d'une implémentation d'un fournisseur de données raster PostGIS dans QGIS core. Les tuiles sont mises en cache dans la mémoire RAM.

Cette fonctionnalité a été financée par Christmas Holidays Inc.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Fonctionnalité: Afficher les métadonnées des dimensions sur les métadonnées de la couche WMS
![wms-ttimelayermetadataqgis](https://user-images.githubusercontent.com/2663775/71542497-37f77500-2978-11ea-854b-d9a9ca2d6c77.png)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
### Fonctionnalité: Autres méthodes moyennes maillage 3d
QGIS now includes numerous methods for averaging mesh layers (see [related QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158), and for a description of the methods see [TUFLOW documentation](https://fvwiki.tuflow.com/index.php?title=Depth_Averaging_Results).
- SingleLevelAverageMethod (top)
- SingleLevelAverageMethod (bottom)
- MultiLevelsFromTopAveragingMethod
- MultiLevelsFromBottomAveragingMethod
- SigmaAveragingMethod
- DepthAveragingMethod
- HeightAveragingMethod
- ElevationAveragingMethod

![Screenshot 2019-12-19 at 13 59 47](https://user-images.githubusercontent.com/804608/71175509-068bf480-2268-11ea-9d60-adad896912e2.png)

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Fonctionnalité: API OGC - Fournisseur de fonctionnalités
This new provider is a client-side implementation of the recently adopted [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) specification, previously known as WFS3. It is integrated within the graphical user interface of the WFS provider, and leverages its core mechanisms to offer background downloading of features, using paging, and a local cache of already downloaded features for a smoother interactive use of datasets.

![image70](images/entries/d74a13f520336e0c2e44469ee4e527188e2466de.webp)

This feature was funded by [Planet](https://planet.com)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com)
## QGIS Server
### Fonctionnalité: QGIS Development Server Application
**QGIS Development HTTP Server**

Il s'agit d'une petite application de ligne de commande indépendante qui implémente un serveur de développement HTTP minimal pour QGIS Server.

Il peut être utile lors du développement et du test de projets, modules et plugins QGIS Server sans nécessiter une pile complète de serveur Web / FCGI.

![qgismapserver](https://user-images.githubusercontent.com/142164/73081781-84c36280-3ec8-11ea-9285-ab4c41e3082c.gif)
``` bash
Usage: qgis\_mapserver [options] [address:port]
QGIS Development Server

Options:
-h, --help Displays this help.
-v, --version Displays version information.
-l Sets log level (default: 0)
0: INFO
1: WARNING
2: CRITICAL
-p Path to a QGIS project file (*.qgs or* .qgz),
if specified it will override the query string MAP argument
and the QGIS\_PROJECT\_FILE environment variable

Arguments:
addressAndPort Listen to address and port (default: "localhost:8000")
address and port can also be specified with the environment
variables QGIS\_SERVER\_ADDRESS and QGIS\_SERVER\_PORT
```
Exemple de sortie :

`bash QGIS Development Server listening on http://localhost:8000 CTRL+C to exit 127.0.0.1 [lun gen 20 15:16:41 2020] 5140 103ms "GET /wfs3/?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 3298 2ms "GET /wfs3/static/jsonFormatter.min.js HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1678 3ms "GET /wfs3/static/jsonFormatter.min.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1310 5ms "GET /wfs3/static/style.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:43 2020] 4285 13ms "GET /wfs3/collections?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200`

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files. Adds missing parameters to GetDxf request

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Fonctionnalité: ajouter la prise en charge json à WMS GetLegendGraphic
This feature adds support for GetLegendGraphic responses encoded as JSON. It builds on previous work by \@pblottiere, who added QgsLegendRenderer::exportLegendToJson for that exact purpose.

Par exemple, une requête GetLegendGraphic avec FORMAT=image/png produisant l'image

![image72](https://user-images.githubusercontent.com/76594/64876231-fbb13a80-d64e-11e9-83e5-120fb1bc0ea8.png)

produira ce qui suit avec FORMAT=application/json.

L'image de l'icône est codée en base64 et directement affichable dans une page Web.

Cette fonctionnalité a été développée par Éric Lemoine
## Programmation
### Fonctionnalité: Expose les méthodes de numérisation de formes à QgisInterface
The actions to trigger the drawing tools were not exposed in the API, if you wanted to do an action for one of these tools, you had to recreate classes. So a call of the type `qgis.utils.iface.actionCircleCenterPoint().trigger()` simplifies programmability.

Cette fonctionnalité a été financée par QWAT/QGEP group

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Correctifs notables
### Fonctionnalité: Correction de bugs par Stephen Knox
| Bug Title | URL issues (if reported) | URL PR or commit |----|----|----|----| | Allow editing of postgres JSON fields from Text Edit Widget | [#29361](https://github.com/qgis/QGIS/issues/29361) | [#30758](https://github.com/qgis/QGIS/pull/30758)

Cette fonctionnalité a été développée par Stephen Knox
### Fonctionnalité : Corrections de bug par Alessandro Pasotti
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| \"Recent\" Group do not appear when opening the \"Select by expression\" dialog | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) |
| Le serveur QGIS ne trouve pas de shp ; il essaie d'ouvrir un chemin absolu plutôt que relatif | [#33200](https://github.com/qgis/QGIS/issues/33200) | [PR #33925](https://github.com/qgis/QGIS/pull/33925) | critique |
| non signalé : mauvais lien dans la page des éléments WFS3 du serveur (trop de barres obliques) | non signalé | [PR #33926](https://github.com/qgis/QGIS/pull/33926) | critique |
| Qgis scanne les tables raster lors de la connexion à postgis | [#33885](https://github.com/qgis/QGIS/issues/33885) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Layer Properties Information tab - formatting problems | [#33862](https://github.com/qgis/QGIS/issues/33862) | [PR #33955](https://github.com/qgis/QGIS/pull/33955) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | fonctionne pour moi dans la version actuelle master |  |
| QgsVectorLayer readStyle ne lit pas la visibilité basée sur l'échelle | [#33840](https://github.com/qgis/QGIS/issues/33840) | [PR #33987](https://github.com/qgis/QGIS/pull/33987) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Categorized symbolization does not work on bigint columns in QGIS | [#33585](https://github.com/qgis/QGIS/issues/33585) | [PR #33992](https://github.com/qgis/QGIS/pull/33992) | [PR #34290](https://github.com/qgis/QGIS/pull/34290) |
| QGIS n'applique pas le fichier de style sur les couches raster | [#29427](https://github.com/qgis/QGIS/issues/29427) | Aucun changement n'est nécessaire mais l'étude se poursuit |  |
| Le copier / coller d'entité avec une géométrie de type multiligneZ ne fonctionne pas correctement | [#33977](https://github.com/qgis/QGIS/issues/33977) | fonctionne pour moi dans la version actuelle master |  |
| Edit Form shows and saves raw default-values from geopackage, spatialite or sqlite | [#33383](https://github.com/qgis/QGIS/issues/33383) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| Impossible de décocher les couches dans le panneau Ordre des couches | [#33854](https://github.com/qgis/QGIS/issues/33854) | [PR #34015](https://github.com/qgis/QGIS/pull/34015) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| PostgreSQL identity column not recognized properly | [#29560](https://github.com/qgis/QGIS/issues/29560) | [PR #34017](https://github.com/qgis/QGIS/pull/34017) | [PR #34291](https://github.com/qgis/QGIS/pull/34291) |
| Spatialite provider does not recognize autoincrement PKs when table definition uses backticks | [#34085](https://github.com/qgis/QGIS/issues/34085) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| QGIS crash when I click on the button \"Manage Map Themes\" | [#33295](https://github.com/qgis/QGIS/issues/33295) | [PR #34090](https://github.com/qgis/QGIS/pull/34090) | [PR #34098](https://github.com/qgis/QGIS/pull/34098) |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | fonctionne pour moi dans la version actuelle master |  |
| QGIS 3.10.2 remplace 0 par NULL | [#34118](https://github.com/qgis/QGIS/issues/34118) | [PR #34152](https://github.com/qgis/QGIS/pull/34152) | [PR #34292](https://github.com/qgis/QGIS/pull/34292) |
| Representation for NULL values inconsistent use/display | [#28643](https://github.com/qgis/QGIS/issues/28643) | [PR #34157](https://github.com/qgis/QGIS/pull/34157) | [PR #34293](https://github.com/qgis/QGIS/pull/34293) |
| DB Manager in 3.11 Master can\'t connect to PostGIS Enabled database | [#34132](https://github.com/qgis/QGIS/issues/34132) | [PR #34171](https://github.com/qgis/QGIS/pull/34171) | N/A |
| QGIS doesn\'t respect OGC guidelines for KVP parameters | [#34148](https://github.com/qgis/QGIS/issues/34148) | [PR #34175](https://github.com/qgis/QGIS/pull/34175) | [PR #34294](https://github.com/qgis/QGIS/pull/34294) |
| QGIS 3.10 can\'t find pkey of postgres views | [#34167](https://github.com/qgis/QGIS/issues/34167) | [PR #34179](https://github.com/qgis/QGIS/pull/34179) | [PR #34295](https://github.com/qgis/QGIS/pull/34295) |
| Duplicating a scratch layer ignores added fields | [#34134](https://github.com/qgis/QGIS/issues/34134) | [PR #34199](https://github.com/qgis/QGIS/pull/34199) | [PR #34203](https://github.com/qgis/QGIS/pull/34203) |
| Le fichier XML d'un projet QGIS est invalide | [#34218](https://github.com/qgis/QGIS/issues/34218) | [PR #34219](https://github.com/qgis/QGIS/pull/34219) | [PR #34297](https://github.com/qgis/QGIS/pull/34297) |
| Full row conditional formatting formats wrong full rows | [#34122](https://github.com/qgis/QGIS/issues/34122) | [PR #34305](https://github.com/qgis/QGIS/pull/34305) | [PR #34315](https://github.com/qgis/QGIS/pull/34315) |
| l'erreur d'expression du filtre renvoie vrai | [#34259](https://github.com/qgis/QGIS/issues/34259) | [PR #34309](https://github.com/qgis/QGIS/pull/34309) | [PR #34512](https://github.com/qgis/QGIS/pull/34512) |
| Fields are shifted when importing a layer with an FID attribute into GeoPackage | [#32927](https://github.com/qgis/QGIS/issues/32927) | [PR #32934](https://github.com/qgis/QGIS/pull/32934) | N/A |
| \"split features\" of PostGIS layers become slow since 3.6 | [#34326](https://github.com/qgis/QGIS/issues/34326) | closed: cannot reproduce with any of the (several) provided datasets |  |
| Cannot add/save more than 1 record/feature in a Spatialite layer/table | [#34379](https://github.com/qgis/QGIS/issues/34379) | [PR #34423](https://github.com/qgis/QGIS/pull/34423) | [PR #34513](https://github.com/qgis/QGIS/pull/34513) |
| QGIS crashes when changing \"default value\" in layer property on a point scratch layer, after editing feature | [#34404](https://github.com/qgis/QGIS/issues/34404) | [PR #34428](https://github.com/qgis/QGIS/pull/34428) | [PR #34514](https://github.com/qgis/QGIS/pull/34514) |
| La calculatrice raster transforme une ligne de pixels en nodata | [#34435](https://github.com/qgis/QGIS/issues/34435) | [PR #34460](https://github.com/qgis/QGIS/pull/34460) | [PR #34511](https://github.com/qgis/QGIS/pull/34511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Fonctionnalité : Correction de bugs par Sandro Santilli
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| repository files modified by \'make check\' | [#25830](https://github.com/qgis/QGIS/issues/25830) |  |  |
| Runs of testsuite leaves hundreds of directories in \~/.local/share | [#34185](https://github.com/qgis/QGIS/issues/34185) | [Commit 96a7fb8](https://github.com/qgis/QGIS/commit/96a7fb8f5acf3a278919f88c7c5abc4d20b8b6c2) | N/A |
| Drop use of deprecated QgsCoordinateReferenceSystem constructor | [PR #34186](https://github.com/qgis/QGIS/pull/34186) | [Commit b4fa419](https://github.com/qgis/QGIS/commit/b4fa419f7654ea7d1bce666b99f0534c415d8634) | N/A |
| Only look for pointcloud in its installed extension schema | [#33509](https://github.com/qgis/QGIS/issues/33509) | [Commit 1f44b29](https://github.com/qgis/QGIS/commit/1f44b29933bff3b8806bba75b761dd47b6c349c8) | N/A |
| QGIS 3.10 unable to load PostGIS-table on MacOS Catalina | [#32558](https://github.com/qgis/QGIS/issues/32558) | [Commit d15ce6b](https://github.com/qgis/QGIS/commit/d15ce6b4c30f9faed8b818c575d6b729192fa064) | [Commit a06b164](https://github.com/qgis/QGIS/commit/a06b164b5465ee7a0f8509e737d7c71ea7c166db) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Cette fonctionnalité a été développée par Sandro Santilli
### Fonctionnalité : Correction de bugs par Even Rouault
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Crash lors de l'application d'un mauvais filtre sur la couche OAFeat | [#33878](https://github.com/qgis/QGIS/issues/33878) | [PR #33927](https://github.com/qgis/QGIS/pull/33927) | [PR #33958](https://github.com/qgis/QGIS/pull/33958) |
| Fournisseur Oracle : correction des avertissements du compilateur | - | [PR #33930](https://github.com/qgis/QGIS/pull/33930) | - |
| Impossible d'importer un vecteur 3D dans Spatialite (fonctionne pour les fichiers GPKG) | [#33883](https://github.com/qgis/QGIS/issues/33883) | [PR #33938](https://github.com/qgis/QGIS/pull/33938) | [PR #33945](https://github.com/qgis/QGIS/pull/33945) |
| \[Oracle\] Fix MultiSurface with straight polygon | - | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | pas faisable |
| Geometries stored in Oracle table fail sdo_geom.validate_geometry_with_context(..) check | [#29085](https://github.com/qgis/QGIS/issues/29085) | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | pas faisable |
| QGIS WFS / OGC API -- Features not showing list typed attributes correctly | [#33758](https://github.com/qgis/QGIS/issues/33758) | [PR #33983](https://github.com/qgis/QGIS/pull/33983) | N/A |
| La légende entraîne un crash | [#32913](https://github.com/qgis/QGIS/issues/32913) | [PR #34004](https://github.com/qgis/QGIS/pull/34004) | [PR #34063](https://github.com/qgis/QGIS/pull/34063) |
| Draw effects units setting doesn\'t persist | [#34089](https://github.com/qgis/QGIS/issues/34089) | [PR #34135](https://github.com/qgis/QGIS/pull/34135) | [PR #34151](https://github.com/qgis/QGIS/pull/34151) |
| Mauvais géoréférencement des fichiers .map OZI | [#34299](https://github.com/qgis/QGIS/issues/34299) | [GDAL commit](https://github.com/OSGeo/gdal/commit/7bedf61bbb8d8c331642b44f30c083abb43f4085) | - |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Fonctionnalité : Correction de bugs par Alexander Bruy
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Remove verbose wording on layout toolbar buttons | [#30161](https://github.com/qgis/QGIS/issues/30161) | [PR #33912](https://github.com/qgis/QGIS/pull/33912) |  |
| Impossible de coller une couche dans un projet vide | [#26710](https://github.com/qgis/QGIS/issues/26710) | [PR #33961](https://github.com/qgis/QGIS/pull/33961) | [PR #33965](https://github.com/qgis/QGIS/pull/33965) |
| DB Manager: Create Layer dialog should be closed or cleared once the new layer is generated | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #33910](https://github.com/qgis/QGIS/pull/33910) |  |
| Deux raccourcis différents pour ouvrir le panneau Style de Couche (F7 vs Ctrl+3) | [#26696](https://github.com/qgis/QGIS/issues/26696) | [PR #33984](https://github.com/qgis/QGIS/pull/33984) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Correction de bugs par Paul Blottiere
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fixes compilation on Arch Linux | non signalé | [PR #34110](https://github.com/qgis/QGIS/pull/34110) | [PR #34146](https://github.com/qgis/QGIS/pull/34146) |

| Move labels doesn\'t work with GPKG QGIS 3.4 | [#30408](https://github.com/qgis/QGIS/issues/30408) | Closed (works on master and 3.10) | - |

| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Feedback (works on master and 3.10) | - |

| Labels Buffer DD options do not have fields set and do not render in map canvas | [#28544](https://github.com/qgis/QGIS/issues/28544) | [PR #34153](https://github.com/qgis/QGIS/pull/34153) | risky |

| QGIS does not load embedded layers when opening projects | [#34060](https://github.com/qgis/QGIS/issues/34060) | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Embedded layers are duplicated after opening | Unreported | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Raise log level of server exception | [Discussed on qgis-developers list](https://lists.osgeo.org/pipermail/qgis-developer/2020-February/060108.html) | [PR #34256](https://github.com/qgis/QGIS/pull/34256) | [PR #34539](https://github.com/qgis/QGIS/pull/34539) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Fonctionnalité : Correction de bugs par Denis Rouzaud
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Crash avec les relations | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34255](https://github.com/qgis/QGIS/pull/34255) | - |
| Crash avec les relations V2 | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34403](https://github.com/qgis/QGIS/pull/34403) | fait |
| Fix map layer actions rendering in attribute table | non signalé | [PR #34266](https://github.com/qgis/QGIS/pull/34266) | fait |
| DnD improvements (sync selections) | [#28570](https://github.com/qgis/QGIS/issues/28570) | [PR #34411](https://github.com/qgis/QGIS/pull/34411) | À faire ? |
| DnD improvements (container config) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34433](https://github.com/qgis/QGIS/pull/34433) |  |
| DnD improvements (do not hide behind double click) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34479](https://github.com/qgis/QGIS/pull/34479) |  |
| disable browsing auto pan/scale in attribute table when showing visible features only | [#34486](https://github.com/qgis/QGIS/issues/34486) | [PR #34493](https://github.com/qgis/QGIS/pull/34493) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Fonctionnalité : correction de bug par Julien Cabieces
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | Doublon | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Fermé (Corrigé pour la version 3.10 et master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | À faire |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Fermé (pas un problème de QGIS) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | À faire |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | À faire |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | À faire |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Bertrand Rix
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Snapping and vertex tool not working with some layers if snapping was enabled when loaded | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Snapping not possible in new project with new layer | [#32969](https://github.com/qgis/QGIS/issues/32969) | Doublon | - |
| Vertex Tool cache not refreshing after changes to line features | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Fermé (Corrigé pour la version 3.10 et master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | À faire |
| setFilterExpression and QGIS Filter output different results | [#33454](https://github.com/qgis/QGIS/issues/33454) | Fermé (pas un problème de QGIS) | - |
| Crash while using Oracle views with primary key defined as number without precision | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | À faire |
| WCS client stopped working on a specific service from 2.18 to 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | À faire |
| Crash in relation reference test | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | À faire |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Loïc Bartoletti
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fermer le sommet de la ligne lors de l'édition | [#32359](https://github.com/qgis/QGIS/issues/32359) | [PR #34217](https://github.com/qgis/QGIS/pull/34217) | [PR #34285](https://github.com/qgis/QGIS/pull/34285) |
| Correction des liens Grass sur FreeBSD | Signalé sur FreeBSD ML | [PR #34088](https://github.com/qgis/QGIS/pull/34088) | [PR #34238](https://github.com/qgis/QGIS/pull/34238) |
| \[Regular Shape\] Allow undo click when digitizing new features | [#25597](https://github.com/qgis/QGIS/issues/25597) | [PR #34080](https://github.com/qgis/QGIS/pull/34080) | [PR #34302](https://github.com/qgis/QGIS/pull/34302) |
| Remove Added Vertex with Add Circular String | [#29688](https://github.com/qgis/QGIS/issues/29688) | [PR #34058](https://github.com/qgis/QGIS/pull/34058) | [PR #34301](https://github.com/qgis/QGIS/pull/34301) |
| Rubberband not working correctly with \"Shapes\" digtizing in rotated map window | [#33287](https://github.com/qgis/QGIS/issues/33287) | Doublon |  |
| Digitizing: LineStringZ does not inherit Z-coordinates from points if line starts by snapping to a point with no Z coordinate | [#33201](https://github.com/qgis/QGIS/issues/33201) | [PR #33642](https://github.com/qgis/QGIS/pull/33642) | [PR #33951](https://github.com/qgis/QGIS/pull/33951) |
| Split feature makes QGIS 3.4.6 crash | [#33408](https://github.com/qgis/QGIS/issues/33408) | Déjà corrigé |  |
| Fix oriented minimum bounding box algorithm | [#33532](https://github.com/qgis/QGIS/issues/33532) | [PR #34334](https://github.com/qgis/QGIS/pull/34334) | [PR #34338](https://github.com/qgis/QGIS/pull/34338) |
| error with returned angle by orientedMinimumBoundingBox() | [#31371](https://github.com/qgis/QGIS/issues/31371) | Fermé. Manque de retour |  |
| Fix build with txt2tags \>= 3.5 | directly reported by FreeBSD qgis maintainer | [PR #34377](https://github.com/qgis/QGIS/pull/34377) | [PR #34389](https://github.com/qgis/QGIS/pull/34389) |
| Fix identify menu when an expression is used as display name | non signalé | [PR #34361](https://github.com/qgis/QGIS/pull/34361) | [PR #34402](https://github.com/qgis/QGIS/pull/34402) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Sebastien Peillet
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Extend line does not work in compoundCurvedZ layer | [#32080](https://github.com/qgis/QGIS/issues/32080) | [PR #34055](https://github.com/qgis/QGIS/pull/34055) |  |
| Feature attribute selection design bug | [#29542](https://github.com/qgis/QGIS/issues/29542) | [PR #34359](https://github.com/qgis/QGIS/pull/34359) |  |
| Unable to add a new feature when joining two PostGIS tables | [#33148](https://github.com/qgis/QGIS/issues/33148) | [PR #34216](https://github.com/qgis/QGIS/pull/34216) |  |
| Copy/Paste fails from one layer to another when layer has NOT NULL constraints and transaction groups are enabled | [#29603](https://github.com/qgis/QGIS/issues/29603) | Already fixed by [PR #33688](https://github.com/qgis/QGIS/pull/33688) |  |
| QGIS se fige à la création de nouveaux shapefiles | [#32069](https://github.com/qgis/QGIS/issues/32069) | Déjà corrigé |  |
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) |  |
| BUG : correction d'un résultat de couche invalide lorsque la version d'Oracle est inférieure à 12 | non signalé | [PR #34546](https://github.com/qgis/QGIS/pull/34546) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Fonctionnalité: correction de bugs par Nyall Dawson
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fix IN/NOT IN evaluation with very long number like strings | [#34314](https://github.com/qgis/QGIS/issues/34314) | [Commit 167e0de](https://github.com/qgis/QGIS/commit/167e0de65b0106a3c19181a2c415c2b0ba0da117) | [Commit aca059a](https://github.com/qgis/QGIS/commit/aca059a82021cb05b58664d3b0f2db751b8f37df) |
| \[processing\] Define Layer Projection tool should write .prj files using ESRI WKT1 format | [#34007](https://github.com/qgis/QGIS/issues/34007) | [Commit f41dd11e](https://github.com/qgis/QGIS/commit/f41dd11e9214b4d6ca5dcc31c6612a65d134ce83) | Soumis |
| Show \'unknown CRS\' in status bar instead of blank text when project is set to an unknown CRS | [#33458](https://github.com/qgis/QGIS/issues/33458) | [Commit c6319b2](https://github.com/qgis/QGIS/commit/c6319b263992c9d52646096d851cab6c674125ff) | Soumis |
| Don\'t force users to make a choice in the datum transform dialog | [#34234](https://github.com/qgis/QGIS/issues/34234) | [Commit 644a552](https://github.com/qgis/QGIS/commit/644a5525ec08a77b4c703a7066c94802bbfa1036) | Soumis |
| Correction d'un crash lors d'un changement de source de données raster | [#34231](https://github.com/qgis/QGIS/issues/34231) | [Commit caf334e6](https://github.com/qgis/QGIS/commit/caf334e65b11f9ee1590f74fe395e97d92bbe699) | [Commit b4142c3](https://github.com/qgis/QGIS/commit/b4142c3832b9f14de97df08caf20a06dee12c02f) |
| Handle unit type \"m\" in custom WKT strings on proj 6 builds | [#34196](https://github.com/qgis/QGIS/issues/34196) | [Commit bb20cee](https://github.com/qgis/QGIS/commit/bb20cee00a931da46b830f0d1e9565d9863f9ba3) | [Commit 97c50f9](https://github.com/qgis/QGIS/commit/97c50f929fbbdd9b3eaef8f8bdf423f9daa3a163) |
| Show full CRS WKT for custom CRS in layer properties | [#33862](https://github.com/qgis/QGIS/issues/33862) | [Commit 19d58bda](https://github.com/qgis/QGIS/commit/19d58bda08c202b29020a3e9c485fac80350fc79) | [Commit 2908227](https://github.com/qgis/QGIS/commit/2908227f91ccfde245a0a608b50b7758b3eba8dd) |
| \[processing\] Fix modeler draws lines to wrong output when connecting green output boxes | non signalé | [Commit 5ae9807](https://github.com/qgis/QGIS/commit/5ae9807303e909a504288d97a2efc4cc04a62670) | [Commit 528a45d](https://github.com/qgis/QGIS/commit/528a45d7453b7cbeb44450d5c81de80c8dd66611) |
| \[processing\] Fix Points Along Geometry handling of multipart geometries | [#34022](https://github.com/qgis/QGIS/issues/34022) | [Commit 3fb18a2](https://github.com/qgis/QGIS/commit/3fb18a2260cbc432e892a4dacbae0092a775ec9d) | [Commit ac3b446](https://github.com/qgis/QGIS/commit/ac3b446aead90d5ea5cab101807859e5ce6f1b44) |
| \[processing\] Fix QStringList values are not accepted as valid values for multi-field parameters | non signalé | [Commit abcb8d2](https://github.com/qgis/QGIS/commit/abcb8d20c66b3c235802b10e68d6abc34736e2c5) | [Commit d421313](https://github.com/qgis/QGIS/commit/d421313f05fd0e5a6974568eccd36c4213f41f8f) |
| \[processing\] Fix some field names are rejected in modeler for non-multi field parameters | non signalé | [Commit 9bcd980](https://github.com/qgis/QGIS/commit/9bcd98094c015265e7e94c55f248248e56c24e51) | N/A - Seulement 3.12 |
| Fix crash in server feature info | non signalé | [Commit b3f37fde](https://github.com/qgis/QGIS/commit/b3f37fde9bc4785aebca29e6553d6c1de715f523) | Soumis |
| Fix overflow by assigning double max to float, invalid min | non signalé | [Commit 2b15e255](https://github.com/qgis/QGIS/commit/2b15e255eaf63f1d45b8e963fca7f9f9e4bf8d40) | N/A - Seulement 3.12 |
| Fix crash in QgsGeometryDuplicateCheck due to heap use after free | non signalé | [Commit 195576e](https://github.com/qgis/QGIS/commit/195576e57f0aff064e962ce16b37533ab4924dce) | [Commit dc647bc](https://github.com/qgis/QGIS/commit/dc647bc56fb37207a75d55638926e7a2db75a8be) |
| Fix crash on destruction of QgsPointLocator, if object is destroyed while indexing is happening in the background | non signalé | [Commit 08adb23](https://github.com/qgis/QGIS/commit/08adb23a7ec284a2f84ecf7ac469fbe9004ab57e) | N/A - Seulement 3.12 |
| Fix crashes when reading certain resampled raster files | [#33711](https://github.com/qgis/QGIS/issues/33711) | [Commit b2c5a45](https://github.com/qgis/QGIS/commit/b2c5a456fa4e9613ac33b8aaaed774ad3b7293a1) | [Commit 388277e](https://github.com/qgis/QGIS/commit/388277e642d99b93bd7f25197d6418b5dfb888bd) |
| Fix use after free in 3d point symbol | non signalé | [Commit df7979c](https://github.com/qgis/QGIS/commit/df7979cf94c43352cd10db97c16075b8816ec6c4) | [Commit 7204de2](https://github.com/qgis/QGIS/commit/7204de27f3305146fbd6f8e32355c365030afc31) |
| Fix leaks in geometry generator symbol layer | non signalé | [Commit 1610fb8](https://github.com/qgis/QGIS/commit/1610fb8766a13351bb303ee3bfd6301dbdc6648b) | [Commit 3944db4](https://github.com/qgis/QGIS/commit/3944db47dda6b08ea4b22f61c5e72d97597362b1) |
| Fix crash in rendering on proj 6 builds | [#33902](https://github.com/qgis/QGIS/issues/33902) | [Commit 8a71091](https://github.com/qgis/QGIS/commit/8a7109163a9362af2a5e0187cf2b57fc0219fe59) | [Commit f41076d](https://github.com/qgis/QGIS/commit/f41076d45f5f259c50e3ead2cac4d664be11bbfb) |
| Don\'t try to label empty geometries | [#33931](https://github.com/qgis/QGIS/issues/33931) | [Commit 1144974](https://github.com/qgis/QGIS/commit/11449743788f3fd346c01c46cff01bcf3f84edf0) | N/A - Seulement 3.12 |
| Fix crashes when attempting to export reprojected raster layers | [#33801](https://github.com/qgis/QGIS/issues/33801) | [Commit bbd055c](https://github.com/qgis/QGIS/commit/bbd055ca13a3d6ee150251222d73e3b9e76d94c5) | [Commit 2fff8e1](https://github.com/qgis/QGIS/commit/2fff8e1205daffafa257b9312cc2c005b5e3017e) |
| Correction des problèmes d'encodage des shapefiles | [#21264](https://github.com/qgis/QGIS/issues/21264) | Soumis | Reporté à la 3.10.4 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
