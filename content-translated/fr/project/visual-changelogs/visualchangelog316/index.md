---
HasBanner: false
draft: false
releaseDate: '2020-10-23'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.16
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.16{#changelog316 }
![image1](images/projects/dbc0cef663f2f652e0961ac2ed168eb45ed2e182.png)

Release date: 2020-10-23

Encore un grand jour pour le projet QGIS ! La nouvelle version à long terme apporte un large panel de fonctionnalités nouvelles à QGIS Desktop et QGIS Server. Cette version apporte de nombreuses nouvelles options notamment pour la cartographie en 3D, la génération de données maillées à partir d'autres types de données, des outils d'analyse spatiale additionnels, des améliorations concernant la symbologie et l'interface utilisateur ! Beaucoup d'outils ont été ajoutés à la boîte à outils de traitement toujours grandissante et l'explorateur QGIS intègre maintenant des fonctionnalités d'interactions avancées avec les bases de données qui étaient au paravent réservées à DB Manager. Ils s'agit de quelque unes des nouvelles fonctionnalités introduites dans cette version et les utilisateurs de la version LTR précédente en trouveront un nombre encore plus important depuis la version 3.10. Nous avons la joie de détailler ci-dessous certains des points forts de cette nouvelle version.

**Remerciements**

We would like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait, nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous croyons que mettre à disposition un outil géographique de prise de décisions concourra à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonction cachée : ajouter la carte des groupes d'utilisateurs
Type the words \"user groups\" into the current coordinates window and watch the magic happen.

![image2](images/entries/079434bceb5004b0ee2c4ad5d62edd1290c28575.webp)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## Temporel
### Possibilité d'exporter les images des animations temporelles
Permet d'exporter des images d'animation temporelle vers des images successives, pour les assembler ultérieurement dans une application externe. Les utilisateurs ont un contrôle précis sur la taille de l'image et l'étendue de la carte.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Outils cartographiques
### Localisateur
Nous avons ajouté un nouveau filtre de localisateur goto.

L'indicateur goto prend en compte les chaînes de caractères suivantes :
- Un couple de coordonnées (séparées par une virgule ou un espace) 
- Une URL formatée par OSM, Leaflet ou OpenLayers.
- Une URL Google Maps

La logique de la chaîne XY est la suivante :
- If the canvas CRS isn\'t WGS84:
  - Si la coordonnée s'inscrit dans les limites du WGS84, ajoutez un résultat WGS84 (celui-ci est pondéré pour avoir une priorité plus élevée que le résultat du canevas CRS ci-dessous).
  - Si la coordonnée s'inscrit dans les limites du canevas CRS, ajoutez un résultat de canevas CRS.
- Si le SCR du canevas est WGS84 :
  - Si la coordonnée s'inscrit dans les limites du WGS84, ajoutez un résultat WGS84.

![image3](images/entries/acb9e856ac744d0e40d8de33c025deb075385856.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Interface utilisateur
### Ajouter un menu contextuel au canevas de carte
The map canvas now has a right-click context menu. By default, it creates the \"Copy Coordinate\" menu that was introduced with QGIS 3.14, however, it is expected that this functionality will be extended to allow many more functionalities to be accessed with spatial context in the future.

![image4](images/entries/f6e3ce9dca04583c9fa791204fe7e1a3c49c61d0.webp)

This feature was developed by [jakimowb](https://api.github.com/users/jakimowb)
## Symbologie
### Améliorations de la symbologie des tuiles vectorielles
De multiples améliorations ont été introduites pour l'édition de styles de tuiles vectorielles complexes :
- Afficher des infobulles dans les listes, afin que les règles de filtrage et les noms complets puissent être affichés sans redimensionner les colonnes
- Afficher le niveau de zoom actuel du canevas dans les widgets
- Permettre aux utilisateurs de filtrer la liste des styles pour n'afficher que ceux qui sont actuellement visibles
- Définir le niveau de zoom correct du canevas lors de l'édition des symboles, afin que les aperçus d'expression fonctionnent bien

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Permettre aux utilisateurs de spécifier facultativement l'URL pour le style par défaut sur les connexions de tuiles vectorielles
When setting up a vector tile source connection, there\'s a new option to enter a URL to a MapBox GL JSON style configuration. If one has been entered, then that style will be applied whenever the layers from the connection are added to QGIS.

Cela fonctionne également avec les connexions du service de tuiles vectorielles ArcGIS, dont le style de configuration par défaut sera celui spécifié dans la configuration du serveur.

![image5](images/entries/f93d5dca726eb94be82cc47479424b8fe42f5920.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Autoriser un décalage défini par les données pour les couches de symboles de remplissage
Toute couche de symboles de remplissage qui prend en charge les polygones de décalage, y compris les remplissages simples, les remplissages d'images raster, les remplissages de formes en rafale et les remplissages de gradients, permettent désormais des décalages définis par les données

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Importer les styles MapBox GL JSON pour les couches de tuiles vectorielles
Les utilisateurs peuvent désormais charger les fichiers de configuration de style MapBox GL JSON lors de l'importation de fichiers de style sur des couches de tuiles vectorielles

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Option d'exposition permettant de compenser les motifs de tirets de lignes simples par un montant prédéfini
Allows for tweaking the positioning of dashes/spaces in the line, so that the dashes/spaces can be placed at nicer positions to account for corners in the line (also can be used potentially to \"align\" adjacent dash pattern borders).

Le décalage peut être défini en différentes unités, y compris des unités cartographiques, et peut également être défini par des données.

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajouter des options pour modifier dynamiquement le motif des tirets dans les couches de symboles de lignes simples
Des options ont été ajoutées pour permettre la modification des motifs de tirets afin de mieux contrôler l'amélioration de la qualité de rendu des symboles de lignes. Ces options sont les suivantes :
- Alignez le motif du tiret sur la longueur de la ligne : Si cette option est cochée, la longueur des tirets sera subtilement ajustée afin de garantir que, lorsqu'une ligne est rendue, elle se termine par un élément tiret complet, au lieu d'un élément espace ou d'un élément tiret partiel.
- Tweak dash pattern at sharp corners: If checked, this option dynamically adjusts the dash pattern placement so that sharp corners are represented by a full dash element coming into and out of the sharp corner. It\'s designed to better represent the underlying geometry while rendering dashed lines, especially for jagged lines.

The following images illustrate the \"Align dash pattern to line length\" change in action, with yellow lines indicating the true start and end position of the line features being symbolised.

Avant :

![image6](images/entries/87635346-39f11c00-c782-11ea-88bc-369866d7f57a.webp)

Après :

![image7](images/entries/87635368-44131a80-c782-11ea-95d9-07fb7d00ffcf.webp)

![image8](images/entries/e1a4d82c248cdd0f04f236443897178c12574885.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Gérer les symboles 3D grâce au gestionnaire de style
Un support a été ajouté pour la gestion des symboles 3D via le gestionnaire de style QGIS, y compris un support pour l'importation et l'exportation de bibliothèques de symboles 3d, et complète le travail récent d'abstraction complète des symboles 3D et de leurs gestionnaires de widgets.

Malheureusement, il n'y a pas de vignettes générées pour les symboles 3D dans la bibliothèque, et une icône générique est utilisée pour tous les symboles 3D pour le moment. La génération de vignettes n'est pas une mince affaire, aussi a-t-elle été reportée pour le moment.

This feature addresses the issue raised in [31479](https://github.com/qgis/QGIS/issues/31479).

![image9](images/entries/7e4ee802abba7dfd7ec61cdd8b3db333b7a30fae.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Étiquetage
### Ajout d'une option permettant aux utilisateurs de contrôler l'emplacement des étiquettes le long des lignes
A new \"Label Anchoring\" section in the line placement settings for labels allows users to specify whether labels should be placed at the center, start or end of lines. In addition, it allows offsets of these positions (based on the percentage of the feature length), which may be defined statically or by using a data-defined definition.

![image10](images/entries/f5cc643fc4eafe75053c134b245e91d2e72e33d0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Point d'ancrage de contrôle pour les étiquettes de lignes
Une nouvelle option est exposée qui permet aux utilisateurs de contrôler si le point d'ancrage pour l'étiquetage des traits de ligne est une indication ou une exigence stricte. Les modifications de comportement qui en résultent sont notamment les suivantes :
- Stricte : Les étiquettes sont placées exactement sur l'ancrage de l'étiquette uniquement, et aucun autre placement de repli n'est autorisé.
- Conseil : l'ancrage de l'étiquette est considéré comme un conseil pour l'emplacement préféré de l'étiquette, mais d'autres emplacements proches du point d'ancrage sont autorisés.

![image11](images/entries/a6c67225ee3b55a021a395ffbf58bd05352ef6fb.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Diagrammes
### Axe de rendu pour diagramme à barres empilées
Cela permet de rendre l'axe sur les diagrammes à barres empilées si un axe a été défini. L'implémentation est basée sur le rendu de l'axe pour le diagramme histogramme.

Les valeurs négatives ne sont pas traitées correctement par des diagrammes à barres empilées avec ou sans affichage de l'axe.

Addresses [Issue 34915](https://github.com/qgis/QGIS/issues/34915)

![image12](images/entries/09739c5bed021a99baec41c98b87f5335a4bf8ec.webp)

This feature was developed by [Dan Minor](https://api.github.com/users/dminor)
## Mesh
### Ensembles de données maillées en mémoire avec persistance
Cette fonctionnalité permet de créer des groupes de données en mémoire pour les couches de maillage. Ces groupes de données sont temporaires et ne sont pas conservés une fois que le projet est quitté.

Une nouvelle option a été ajoutée au calculateur de maillage qui permet la création de groupes d'ensembles de données en mémoire.

Cette fonctionnalité introduit également la possibilité de supprimer ou d'enregistrer ces groupes d'ensembles de données en mémoire dans un fichier avec le pilote spécifié.

![image13](images/entries/85622744-4d9edc00-b635-11ea-91db-a02fa28e6bea.gif)

![image14](images/entries/b27519025102be3b07fc8241f0ff8f8f2f9b31c6.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Identification multiple pour la couche maillée
L'outil d'identification a été adapté lorsqu'il est utilisé sur des couches de maillage et affiche maintenant la valeur de l'ensemble de données correspondant à l'heure actuelle du contrôleur temporel pour tous les groupes d'ensembles de données. Les groupes de données actifs (scalaires et éventuellement vectoriels) sont d'abord affichés, puis les autres groupes de données. D'autres informations sont également affichées, notamment :
- Source où l'ensemble de données est stocké
- Le pas de temps de l'ensemble de données qui est affiché (peut être différent du temps du contrôleur temporel). N'affiche rien si le groupe de données n'est pas temporel
- Centroïde de la vue correspondante
- Coordonnées du sommet brisé (si un sommet est brisé)
- Centre du bord brisé (si un bord est brisé)

Lorsque la navigation temporelle n'est pas activée dans le canevas de la carte, les résultats d'identification ne contiennent que des informations sur les groupes d'ensembles de données actifs qui ont des ensembles de données statiques définis dans la boîte de dialogue des propriétés du maillage.

![image15](images/entries/c4974747f5bc0dcba02f30a97e68bb5edacc5f48.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Groupes d'ensembles de données virtuels pour la couche de maillage
The ability to use \"virtual\" data set groups has been introduced for mesh layers. This replaces the \"memory\" dataset group used in [37389](https://github.com/qgis/QGIS/pull/37389).

With the mesh calculator, users may choose to create those \"virtual\" dataset groups that will be added to the layer. Values are not stored in memory but each dataset is rather calculated when needed with the formula entered in the mesh calculator.

Ces groupes d'ensembles de données virtuels sont enregistrés dans le cadre du projet et sont supprimés ou enregistrés dans un fichier à des fins de persistance.

Les groupes d'ensembles de données persistants et virtuels sont distingués dans l'onglet source des propriétés de la couche de maillage par les changements de couleur du fond de chaque élément, indiqués comme suit :

Persistant : jaune

Virtuel : violet

![image16](images/entries/86540129-a8a3bf00-bed0-11ea-94b8-bf29b5818cb8.gif)

![image17](images/entries/803983acbaec38e8df0fb4fd12d28beef7399520.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Ajouter l'exportation à la méthode QgsMesh
Une méthode a été ajoutée pour exporter une triangulation vers une instance QgsMesh, avec la possibilité de construire une couche de maillage avec triangulation à partir de points et de lignes existants. C'est la première étape pour obtenir un QgsMesh à partir d'autres couches de la carte.

Les classes Triangulation et DualEdgeTriangulation ont également été renommées et remaniées pour les rendre plus cohérentes avec le code QGIS.
- Ajouter une méthode pour exporter la triangulation vers une instance QgsMesh.

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
### Création d'une maille TIN
Les couches de maillage TIN peuvent être créées à partir de données de couches vecteur (sommets et/ou lignes de rupture). Le maillage résultant est construit avec une triangulation à retardement contraint. Cette couche de maillage peut être créée à l'aide de l'API python ou d'un algorithme de la boîte à outils de traitement.

![image18](images/entries/fc8a9633b87b29bba052dacd166c0735b4449c90.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Rendu
### Filtre de correction gamma pour les couches raster
Ajoutez un filtre de correction gamma pour les couches raster en plus des filtres existants de luminosité, de contraste, de teinte et de saturation. Les utilisateurs peuvent ajuster la valeur gamma à partir de la boîte de dialogue des propriétés des couches, en utilisant le panneau de style et/ou les nouveaux boutons de la barre d'outils Raster. La valeur gamma par défaut est de 1,0 et peut être ajustée dans la plage de 0,1 à 10.

Addresses [Issue 13512](https://github.com/qgis/QGIS/issues/34915)

Also adds a rendering test for brightness and contrast filter which has no test at all and fixes some deprecation warnings in the Python test for `QgsRasterLayer`.

![image19](images/entries/bf6076062db63bc4c789bc18d3b029c14b2ddc8e.gif)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## Fonctionnalités 3D
### Permettre l'intégration de fichiers de texture de matériaux 3D dans le style/projet
Quelques nettoyages mineurs de l'API et du code ont été realisés, ainsi que l'introduction de l'utilisation de QgsImageCache pour les fichiers de texture 3D afin de leur permettre d'être intégrés dans les projets.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Rendu des ombres
Les ombres peuvent maintenant être rendues en vues 3D.

![image20](images/entries/ef724bf261c7740d3cc92238d71d5ecb32a190c3.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Export de vues 3D
Les scènes 3D peuvent désormais être exportées pour être utilisées dans d'autres logiciels 3D, tels que Blender. Cette fonction d'export prend en charge beaucoup de fonctions supplémentaires, notamment la simplification du modèle de sortie en spécifiant la résolution de sortie, le lissage optionnel du modèle et l'exportation de couches vecteur3D.

![image21](images/entries/91c112ba42358124faec9c3427542524d6b593f9.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Support d'éclairage directionnel pour QGIS 3D
Ajout de lumières directionnelles à QGIS 3D
- L'utilisateur peut maintenant ajouter des lumières directionnelles aux vues 3D.
- J'ai ajouté un widget sous la section "lights" du dialogue de configuration 3D.
- L'utilisateur peut spécifier la direction de la lumière, sa couleur et son intensité.
- Il s'agit simplement d'une duplication de la mise en œuvre des sources de lumière ponctuelles déjà existantes avec quelques changements.
- Later it may be useful to add a way to visualize the light direction by displaying a mesh that is positioned at camera\'s view point like an arrow that displays how the sun lights the scene for example.

![image22](images/entries/4dcd7d7f4bcfb71d765656bfe734ec32ddcaca9c.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Support de texturation pour la couche vecteur
Le support de textures a été ajouté pour QGIS 3D avec les nouvelles fonctionnalités suivantes :
- Les utilisateurs peuvent maintenant sélectionner une image à afficher sur les surfaces des bâtiments comme carte diffuse à partir des propriétés du symbole.
- L'utilisateur peut également modifier l'échelle des textures à partir des propriétés du symbole.

Some visual issues may appear when using textures. These issues relate to the normals of surfaces that you may be able to fix by checking \"add back faces\" and playing around with the invert normals and culling mode in the symbol properties.

![image23](images/entries/1c4fc6ffc1b7a28aeff9c625fb6238998dd30b67.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Activer les modèles 3D intégrés et distants pour les symboles de points 3D
Les utilisateurs peuvent désormais utiliser et intégrer des modèles 3D distants pour les symboles de points 3D.

![image24](images/entries/d4deaabbeddcf5f4784f602f19dabfac22b2d100.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Ajout d'une option permettant d'afficher l'origine des sources de lumière
Une fonction qui permet aux utilisateurs de basculer une sphère visible à l'origine de la source de lumière dans une scène 3D.

Cela permet de repositionner et de placer plus facilement les sources de lumière par rapport au contenu de la scène.

Addresses [Issue #37726](https://github.com/qgis/QGIS/issues/37726).

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Améliorations pour la gestion des matériaux
D'autres améliorations ont été apportées à la manipulation des matériaux et un modèle d'ombrage Gooch a été ajouté. Cela améliore l'API QgsAbstractMaterialSettings :
- Ajout d'un support d'icônes pour les types de matériaux enregistrés (à utiliser dans la liste déroulante de sélection des matériaux).
- Adds support for handling different rendering techniques to QgsAbstractMaterialSettings. Now material classes can indicate which rendering techniques they support (e.g. Triangles, Lines, InstancedPoints, etc.), and the material is only offered when it\'s compatible with the required technique.
- La gestion des techniques dans le widget Gooch Material a été améliorée pour éviter de montrer des paramètres qui n'ont aucun effet dans un contexte particulier (par exemple, cacher tout sauf le choix de la couleur ambiante pour les symboles de lignes 2D simples).
- A new material, \"Gooch\", was added. This material gives a CAD style 3D render, where the shading is not dependent on appropriate lighting setup in a scene and where the 3D details are always visible, regardless of the lighting choice.

![image25](images/entries/b6df518d57147bfdfd207d4499363c9d4653721b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Mises en page de cartes
### Exposer le contrôle du format et de l'alignement du texte pour les cellules individuelles dans les tables de texte manuels
Ajoute un contrôle sur le réglage du format du texte (par exemple, gras/italique/tampon/ombre, etc.) et l'alignement du texte (horizontal et vertical) pour le contenu des cellules individuelles dans un tableau de texte manuel.

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Utilisez QgsTextRenderer pour rendre le texte des tables d'attributs
Permet toute la gamme des options de formatage du texte dans les tables d'attributs de mise en page, y compris les tampons, les ombres, l'espacement des mots, etc.

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Utilisez QgsTextRenderer pour dessiner le texte de la grille de la carte dans les mises en page
Permet des annotations de grille qui utilisent des tampons, des ombres, des formes de fond, etc.

![image26](images/entries/86863750-26550e00-c10f-11ea-8dd4-1b740017949e.gif)

![image27](images/entries/349efbc988ccbf3499e18ec4453b637abf893c38.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Option d'exposition pour contrôler la méthode de compression des images PDF lors de l'exportation des mises en page vers le format PDF
Les options sont la compression avec perte, qui est la compression JPEG utilisée par défaut, et la compression sans perte (qui crée des fichiers plus volumineux dans la plupart des cas, mais est beaucoup plus adaptée aux impressions professionnelles ou à la post-production dans d'autres produits tels qu'Illustrator, etc.)

La mauvaise nouvelle est que cette option n'est disponible que dans les versions basées sur Qt 5.13 ou plus.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajouter des paramètres de découpage automatique pour les cartes de l'atlas
Cette fonction permet aux utilisateurs d'activer le découpage de la carte pour les éléments de la carte dans la mise en page afin que les cartes soient découpées à la limite de l'élément de la zone de l'atlas en cours.

Des options existent pour :
- Activation ou désactivation de la découpe par carte
- Préciser le type de découpage :
  - "Clip During Render Only": applies a painter based clip, so that portions of vector features which sit outside the atlas feature become invisible
  - "Clip Feature Before Render": applies the clip before rendering features, so borders of features which fall partially outside the atlas feature will still be visible on the boundary of the atlas feature
  - "Render Intersecting Features Unchanged": just renders all features which intersect the current atlas feature, but without clipping their geometry
- Contrôler si les étiquettes doivent être placées de force à l'intérieur de l'entité de l'atlas, ou si elles peuvent être placées à l'extérieur de l'entité
- Limiter le découpage à un sous-ensemble des couches du projet, de sorte que seules certaines soient coupées

![image28](images/entries/86433831-191ad680-bd3f-11ea-9289-cc6d2b3e2e11.gif)

![image29](images/entries/1f1343d09c75b0e1d131c25a79b905d7aaadbc35.webp)

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajout d'une API à QgsMapSettings pour spécifier les surfaces de découpage à appliquer lors du rendu des cartes
Il s'agit actuellement d'une fonctionnalité de l'API uniquement, mais des fonctionnalités ont été ajoutées qui fournissent les capacités permettant de spécifier les surfaces de découpage qui peuvent être utilisées lors des opérations de rendu de la carte.

Although primarily introduced in order to provide functionality which allows the automatic clipping of map elements to the current atlas feature geometry in print layouts, the API has been deliberately implemented in a manner that\'s very flexible to allow various use cases which require the clipping of regions during map render operations.

Pour les couches non vecteur, le découpage est appliqué par un chemin de découpage QPainter. Pour les couches vecteur, l'API expose différentes options quant à la manière dont le découpage doit être appliqué :
1. As an \"intersects\" style test only: All vector features which intersect the path are rendered, without actually clipping the feature\'s geometry
2. By modifying the feature\'s geometry and clipping the geometry to the region: Any stroke or outline settings for the symbol will be rendered along the boundary of the clipping region, even if the feature actually partially falls outside this region.

ou
1. Utilisation d'un chemin de découpage de forme : les traits sont découpés sur la surface, mais seulement au moment du dessin. Les limites de l'entité qui se trouvent en dehors de la surface de découpage ne seront pas visibles.

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Taille maximale du marqueur de la légende de mise en page
Ajoute la possibilité d'entrer la taille maximale du marqueur (en mm) dans le widget de légende de la mise en page.

Dans certains cas, par exemple lorsque les couches de points utilisent une taille de symbole basée sur des unités cartographiques, les marqueurs de points de la légende de la mise en page peuvent devenir assez gros. Cette fonction ajoute un paramètre au widget de légende de mise en page qui permet de limiter la taille maximale des symboles des marqueurs pendant que la mise à jour automatique de la légende est encore active.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
### Permettre aux cellules des tableaux d'avoir un contenu basé sur l'expression
Permet aux cellules individuelles d'un tableau de prendre leur contenu à partir d'une expression prédéfinie. Les expressions ont accès au contexte complet de l'expression de l'élément de mise en page, ce qui permet aux cellules de calculer et d'afficher des valeurs de style de métadonnées ou des calculs basés sur des agrégats.

Cette fonctionnalité a été financée par City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Découper des cartes pour les mettre en forme
Une nouvelle fonctionnalité a été introduite, qui permet aux utilisateurs de découper un élément de carte dans une forme ou un polygone à partir de leur mise en page, ce qui permet d'obtenir des cartes non rectangulaires dans la mise en page.

![image30](images/entries/88761088-c1428480-d1b1-11ea-90c0-a391d00b084d.gif)

![image31](images/entries/7179282b09e8d196251f543a9c5f059f89c701e2.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Soutien à la rotation des ticks/annotations
Tick marks and annotations on a map frame in the print composer can now be rotated, allowing them to align with a rotated map frame as described in [issue 36904](https://github.com/qgis/QGIS/issues/36904). It works for both rotated maps and reprojected grids.

Les options suivantes ont été ajoutées :
- Ticks:
  - Rotation des ticks (si elle n'est pas cochée, les ticks se dessinent comme auparavant, sans tenir compte de l'angle)
  - Alignement des ticks en rotation (si les ticks doivent avoir une longueur constante, ou être alignées orthogonalement)
  - Skip low angled ticks (an angle threshold below which ticks aren\'t drawn, so you can skip ticks for grid lines that are, for example, too close to being parallel with the map edge)
- Annotations :
  - Parallèle à la tick (à côté de / horizontal / vertical ascendant / vertical descendant)
  - Dessiner à angle faible (si coché, les ticks échappées ci-dessus seront tout de même annotées)

![image32](images/entries/0da542215cefcd2e3ca120dd0381b47611734dce.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
### Ajouter une expression de décalage de page pour les positions Y
A `layout_pageoffsets` expression was added for print layouts which returns an array of Y coordinates for the top of each page in the layout. this allows users to dynamically position items on pages in a context where page sizes may change.

For example, to set an item at 2.5mm from the top of page 2 (for the data-defined position Y of a map item) : `@layout_pageoffsets[1] + 2.5`

This constitutes a workaround for [Issue 37567](https://github.com/qgis/QGIS/issues/37567).

This feature was funded by [BikePlan](https://www.bikeplan.swiss/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Expressions
### Add to_decimal() function to convert DMS to DD
A new `QgsCoordinateUtils::dmsToDecimal` function has been added which exposes the `to_decimal` function in expressions. This allows the conversion of DMS (degree/minute/second) strings into DD (decimal degree) format.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Add \"main_angle\" function to return the estimated main angle of a geometry
Retourne l'angle de la boîte de délimitation minimale orientée qui couvre la valeur de la géométrie.

Useful for data defined overrides in the symbology of label expressions, e.g. to rotate labels to match the overall angle of a polygon, and similar for line pattern fill. ![image33](images/entries/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)

![image34](images/entries/03463ac0a8303444d94806fb2ff66d6a73c56ccb.webp)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Port réfFonctions au core
Diverses opérations de superposition ont été ajoutées au moteur d'expression. Cela couvre les fonctionnalités du plugin refFunctions.

![image35](images/entries/90797864-7bd92900-e311-11ea-945f-0c2ade14e801.gif)

The following new expression functions are implemented:

    * overlay_intersects(layer[,expression][,filter][,limit][,cache])
    * overlay_contains(layer[,expression][,filter][,limit][,cache])
    * overlay_crosses(layer[,expression][,filter][,limit][,cache])
    * overlay_equals(layer[,expression][,filter][,limit][,cache])
    * overlay_touches(layer[,expression][,filter][,limit][,cache])
    * overlay_disjoint(layer[,expression][,filter][,limit][,cache])
    * overlay_within(layer[,expression][,filter][,limit][,cache])
    * overlay_nearest(layer[,expression][,filter][,limit][,max_distance][,cache])
    
In all instances, the spatial operator is evaluated against the other layer. If an expression is provided, it returns an array of results. If no expression is provided, it returns a boolean indicating whether or not there is a match for at least one feature. Features can optionally be filtered by an expression, and optionally be limited to a certain count.

The `overlay_nearest` function has an additional max_distance filter.

![image36](images/entries/d4bb059729eecfc689e001f731d59fff25225615.webp)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Numérisation
### Ajout d'une option permettant de calculer le relèvement en fonction du sens de la marche
Pour les appareils qui signalent des mesures de relèvement erronées, cette option peut être utilisée pour calculer le relèvement GPS en se basant sur les deux emplacements enregistrés précédemment.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Numérisation et découpage des éléments courbes
Une nouvelle fonctionnalité a été introduite, qui ajoute la possibilité de passer d'une chaîne linéaire à une chaîne circulaire lors de la numérisation ou de la découpe des éléments d'une couche vecteur.

L'utilisateur peut utiliser le raccourci clavier **Ctrl+Shift+G** pour passer de linéaire à circulaire.

For splitting features, new overloading methods have been added to the API. When splitting, curves are preserved. For this, the curve is segmentized before splitting, and all the split features are \"de-segmentized\" after splitting.

A toolbar button was added to enable switching between linear/circular: ![image37](images/entries/88101713-6505b200-cb6c-11ea-9feb-68a4130d6f52.gif)

![image38](images/entries/86938423-6a93de80-c10e-11ea-8511-489d8b4f006f.gif)

![image39](images/entries/86938444-7089bf80-c10e-11ea-8fd0-0f419f71b52e.gif)

![image40](images/entries/8145ccfa4e659f7d8315830cecfe2b2f391b9aa4.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Gestion des données
### Algorithme de rééchelonnement des raster pour le traitement
Adds a rescale raster algorithm to change raster value range, whilst preserving the shape of the raster\'s histogram. Useful for when rasters from different sources should be compared or processed together and their pixel values should be in the same range. By default, the algorithm preserves the NODATA value of the input raster but there is an option to override it.

The following image displays a histogram of a DEM (value range is 85-243) ![image41](images/entries/86897604-53ee8700-c110-11ea-99ae-540d38f88154.webp) And the next image displays a histogram of same DEM rescaled to the range 100-1000 ![image42](images/entries/86897671-67015700-c110-11ea-8183-e0d6bd013dbb.webp)

Addresses [Issue 26099](https://github.com/qgis/QGIS/issues/26099).

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## Formulaires et widgets
### Plusieurs widgets pour une seule relation
Des widgets à relations multiples peuvent désormais être créés pour une seule relation, chacun ayant sa propre configuration distincte.

This feature changes the behavior of relation widgets created in the drag and drop interface and provides resolution for [Issue 37675](https://github.com/qgis/QGIS/issues/37675).

A la lecture d'un projet configuré avec d'anciennes versions de QGIS, la configuration est reprise et écrite dans la nouvelle configuration du widget. Les formulaires autogénérés ne permettent plus la configuration des widgets de l'éditeur de relations, mais s'il a été configuré dans une ancienne version de QGIS, le formulaire d'attribut lira toujours cette configuration.

![image44](images/entries/d3a51f9b7ea6ffa3c8c8c457e3d6278d57bcf125.gif)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Afficher les entités connexes dans l'arbre de résultats d'identification
Les utilisateurs pourront désormais voir les entites connexes (enfant) dans la fenêtre de résultats lorsqu'ils utiliseront l'outil d'identification. Sous chaque entité parent identifiée, de nouveaux groupes s'afficheront contenant toutes les entités enfants liées, affichant leurs attributs, leurs actions et permettant à l'utilisateur d'ouvrir directement le formulaire des entités enfants.

This feature addresses issue [18634](https://github.com/qgis/QGIS/issues/18634).

![image45](images/entries/863b80851b995421b6f2ea455faf6b1c41211cd5.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Filtrer les expressions dans le widget de référence des relations
Une option a été ajoutée pour l'expression de filtre statique à utiliser dans le widget de référence de relation.

![image46](images/entries/8048bb8df64e31bb733eea239c527f8be631ce6f.gif)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Outils d'analyse
### Ajouter les temps de profil de charge du projet au dock des outils de déboguage
Modification of the QgsRuntimeProfiler class which performs the following functions: 1. Make the profiling thread-safe, so that it\'s possible to record times across multiple threads 2. Allows different profiling \"groups\"

The new groups API is used here to expose a breakdown of project load times in the debugging dock, alongside the existing QGIS startup profiling. It\'s possible now to get a breakdown of the various stages of project load, in order to identify the causes of slow project load times.

TODO: In the majority of cases, performance problems will be caused by one or more layers, so it would be nice to further break down the individual layer load times. For example, for an individual WFS layer, we may see the time taken for the initial \"server capabilities\" or other queries. Add a group with profile times for map rendering, so you can see exactly which layers in your project are causing slow map redraw times.

Dans sa forme actuelle, seul le temps de chargement global de chaque couche individuelle est affiché.

![image47](images/entries/85852208-7bca1a80-b7f3-11ea-8882-b3253622b1b6.webp)

![image48](images/entries/943a79db68aee3458cb88cacd7a69b66fda3caea.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Traitement
### Ajouter une chaîne d'aide pour les paramètres
Les chaînes d'aide peuvent maintenant être spécifiées au niveau des paramètres.

Cela sera visible dans l'info-bulle, dans le CLI et dans l'API de traitement Python.

![image55](images/entries/2196bcb0123ced5e180ffb2b9469a65a38dcc41b.webp)

This feature was developed by [Étienne Trimaille](https://api.github.com/users/Gustry)
### New \"Align points to features\" algorithm
Cet algorithme calcule la rotation nécessaire pour aligner les éléments ponctuels avec leur élément le plus proche d'une autre couche de référence. Un nouveau champ est ajouté à la couche de sortie, qui est rempli avec l'angle (en degrés, dans le sens des aiguilles d'une montre) par rapport à l'élément de référence le plus proche.

Optionally, the output layer\'s symbology can be set to automatically use the calculated rotation field to rotate marker symbols.

Si vous le souhaitez, une distance maximale à utiliser lors de l'alignement des points peut être fixée pour éviter d'aligner des points isolés sur des éléments éloignés.

Un exemple de cas d'utilisation est l'alignement des symboles de points de construction pour suivre la direction de la route la plus proche en utilisant une valeur de rotation définie par les données générées par cet algorithme.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajout d'un algorithme de modélisation pour créer des répertoires
Cet algorithme permet aux modèles de créer de nouveaux répertoires de fichiers. Utile pour les modèles qui doivent fournir des résultats à certains chemins créés dynamiquement (par exemple un dossier contenant la date du jour).

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajout d'un algorithme de modélisation pour définir une variable d'expression de projet
Allows a model to set Project-level expression variables during execution. Especially useful with the new [Export Print Layout algorithms](https://github.com/qgis/QGIS/pull/36916) to allow models which dynamically set variables used in a layout prior to export.

This functionality was ported from <https://gis.stackexchange.com/questions/359386>

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajouter des algorithmes de traitement pour exporter une mise en page au format PDF/image
Les modèles sont capables d'exporter des mises en page du projet en cours. L'un des cas d'utilisation est de permettre aux utilisateurs de créer un modèle en cours de projet qui exporte un ensemble particulier de mises en page du projet vers certains dossiers, afin qu'ils puissent facilement réexporter le projet en cours en une seule opération au lieu de devoir ouvrir manuellement plusieurs mises en page et les exporter une par une.

De plus, grâce aux nouvelles possibilités d'avoir des fichiers de sortie basés sur des expressions dans les modèles, vous pouvez automatiquement exporter les mises en page vers un dossier avec l'étiquette de la date du jour et l'inclure dans les noms de fichiers exportés !

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Ajouter une fonction de sauvegarde à l'algorithme des fichiers
Il existe maintenant un algorithme de traitement natif pour sauvegarder les entites vecteur dans un ensemble de données de fichier au sein d'un modèle. Il est fourni avec une paire de fonctions avancées permettant de transmettre les options de l'ensemble de données et des couches au GDAL.

![image56](images/entries/b238631365830b019300700cf59c3a8dd3d05a4f.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Exporter l'atlas sous forme d'algorithme PDF
Un nouvel algorithme de traitement QGIS a été ajouté qui permet l'exportation d'un atlas cartographique en PDF. Il s'agit du pendant PDF du récent algorithme d'exportation de la mise en page de l'atlas vers l'image.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### New \"Flatten Relationship\" algorithm
Cet algorithme aplanit toutes les relations pour une couche vecteur, en exportant une seule couche contenant une entité maîtresse par entité connexe. Cette entité maîtresse contient tous les attributs des entites connexes.

It\'s designed as a quick way to de-normalize a relation from a project, e.g. to allow exporting to CSV.

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Exporter la mise en page de l'atlas sous forme d'algorithme d'image
Un nouvel algorithme de traitement natif a été ajouté pour exporter les atlas sous forme d'images.

Cela est utile dans les modèles où des ensembles de données distants sont traités dans le but d'être utilisés comme couches de couverture de l'atlas.

![image57](images/entries/e4f315e60743577c9f45ad44643fd5ba9778c040.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Nouvel algorithme de statistiques cellulaires
Nous avons ajouté un algorithme d'analyse raster de **Statistiques de la cellule**. Il effectue des statistiques par cellule sur une pile de couches raster tout en tenant compte des valeurs NoData. Les fonctions disponibles dans l'implémentation actuelle sont les suivantes :

|
- Somme
- Moyenne
- Médiane
- Écart-type
- Variance
- Maximum
- Minimum
- Majorité (valeur la plus fréquente)
- Minorité (valeur la moins fréquente)
- Plage (max - min)
- Variété (nombre de valeurs uniques)

![image49](images/entries/fca13f48b118ed13ebe84191a226ca0e20c37bfa.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Nouvel algorithme "Equal to frequency
Nous avons ajouté de nouveaux algorithmes raster qui fonctionnent sur une base locale, cellule par cellule, dans une pile de raster. L'algorithme "Equal to frequency" évalue cellule par cellule la fréquence (nombre de fois) où les valeurs d'une pile de raster en entrée sont égales à la valeur d'une valeur de raster.

![image50](images/entries/e368e10cfa5e19992176930121e0cb846c3d1ca8.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Nouvel Algorithme supérieur à la fréquence
Nous avons ajouté de nouveaux algorithmes rasters qui fonctionnent sur une base locale, cellule par cellule, dans une pile de rasters. L'algorithme "Plus que la fréquence" évalue cellule par cellule la fréquence (nombre de fois) où les valeurs d'une pile de rasters en entrée sont supérieures à la valeur d'un raster.

![image51](images/entries/97228db861367c2875dab0533ab616bb2ac2432c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nouvel algorithme "Moins que la fréquence"
We have added some new raster algorithms that operate on a local cell-by-cell basis in a raster stack. The Less than frequency algorithm evaluates on a cell-by-cell basis the frequency (number of times) the values of an input stack of rasters are less than the value of a value raster.

![image52](images/entries/114853cd3d7c245b56edea0024704c853997275c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nouvelle position la plus basse dans l'algorithme de la pile de rasters
Nous avons ajouté quelques outils d'analyse de position à valeur raster avec cette nouvelle version de QGIS : L'algorithme *Position la plus basse dans une pile de rasters* évalue, cellule par cellule, la position du raster ayant la valeur la plus basse dans une pile de rasters. Le comptage des positions commence par 1 et s'étend jusqu'au nombre total de rasters saisis. L'ordre des rasters en entrée est pertinent pour l'algorithme.

![image53](images/entries/f3383f5583c9096b1b8d1873679e1a495fac0485.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nouvelle position la plus élevée dans l'algorithme de la pile de rasters
Nous avons ajouté quelques outils d'analyse de position à valeur raster avec cette nouvelle version de QGIS : L'algorithme *Highest position in raster stack* évalue, cellule par cellule, la position du raster ayant la valeur la plus élevée dans une pile de rasters. Le décompte des positions commence par 1 et s'étend jusqu'au nombre total de rasters saisis. L'ordre des rasters en entrée est pertinent pour l'algorithme.

![image54](images/entries/a730b8c1566c99bdebff09c783ae320b0c138d76.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Charger les résultats du traitement dans le groupe de couches
Users can now optionally set a group name which ensures that the resulting output layers added to the project when using the *Open output file after running algorithm* option are grouped together. This allows all outputs from several processing algorithms to be grouped so that they may be easily located in the layer tree and be removed, exported, or have their visibility toggled easily. ![image58](images/entries/414c68839518d5b658d6e6f1565f6c27e1f4336f.gif)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Ajout d'un algorithme de statistiques zonales qui crée de nouveaux résultats
Previously, when calculating zonal statistics, the algorithm always updated the original data source, adding additional fields. A new zonal statistics algorithm has been added which creates a new output instead. This functionality is an implementation of the [29504 feature request](https://github.com/qgis/QGIS/issues/29504).

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Ajouter un paramètre de traitement de la géométrie
Added a new `QgisProcessingParameterGeometry` for passing geometries as a parameter to processing alogrithms.

Cela permet de passer des géométries simples aux algorithmes sans avoir besoin d'une couche en entrée.

Les cas d'utilisation immédiat sont :
- Des algorithmes qui pourraient avoir besoin de manipuler des géométries de manière atomique.
- Délégation des algorithmes parents.
- Utilisation avec le traitement de qgis sans tête dans des outils de traitement autonomes.

Fonctionnalités :
- Le paramètre est compatible avec les paramètres des chaînes de caractères car il peut transmettre la valeur de Well-Known-Text.
- L'interaction actuelle des widgets est minimaliste car elle utilise uniquement le widget de saisie de texte pour saisir la valeur en tant que WKT.

This feature was developed by [David Marteau](https://api.github.com/users/dmarteau)
### Ajouter une interface pour déterminer si la sortie de l'application est sûre
Une interface pour les plugins et les scripts permettant d'enregistrer une logique personnalisée pour empêcher la sortie de l'application QGIS a été ajoutée. Cela permet aux plugins de déterminer si la sortie de l'application est sûre. Cela a permis aux plugins de déterminer s'il y a des modifications non sauvegardées qui doivent être sauvegardées ou supprimées avant de permettre à QGIS de sortir. Cette fonctionnalité a déjà été mise en œuvre dans l'éditeur de scripts de la console, ce qui permet d'éviter la perte de données en avertissant les utilisateurs lorsqu'il y a des modifications non sauvegardées plutôt que de fermer silencieusement l'application.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Options de l'application et du projet
### Liste des pilotes vecteur GDAL disponibles
A *Vector Drivers* tab is now available within the QGIS GDAL Settings window, which lists all the available GDAL vector drivers and allows users to toggle their active state. Where several drivers may be used to open data of a specific type, users may now modify these settings to ensure that the intended driver is used when importing specific vector data types. For example, the FileGDB and OpenFileGDB drivers are both capable of being used to import .gdb files, but if the data file has a version of 9.x, the FileGDB won\'t be able to open it. In this instance, a user may disable the FileGDB driver and ensure that the data is loaded using the OpenFileGDB driver instead.

This functionality directly addresses the limitations outlined in [Issue 18738](https://github.com/qgis/QGIS/issues/18738).

![image59](images/entries/5cc48d8ea8bc276446f8eae4a1c838e0d1f91a40.webp)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Détecter le dossier d'installation de GRASS sur MacOS
MacOS previously had a platform-specific custom parameter setting Grass7Utils.GRASS_FOLDER. This caused crashes for many users with multiple QGIS installations or who had some invalid folder settings. The parameter has been removed and a GISBASE environment variable has been introduced instead, which is commonly used in GRASS scripts as the \"root\" installation directory, emulating the behavior used for GRASS detection in Windows environments. If GISBASE is not present (default), a search is performed for grass folders in `QgsApplication.prefixPath()` (when packaged in bundle format). If not found, the standalone GRASS instance is searched for. The new behaviour for GRASS is in-line with the methodology used for the GDAL and SAGA processing tools.

This resolves [Issue 38595](https://github.com/qgis/QGIS/issues/38595).

![image60](images/entries/e59bb83513293830df8ec4dcf825247b14dacc98.webp)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://api.github.com/users/PeterPetrik)
## Explorateur
### Exposer les champs dans le navigateur
First part of QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/171>

Expose les colonnes de champ dans le navigateur pour les fournisseurs qui mettent en œuvre l'API de connexion :
- PG
- GPKG
- Spatialite
- MSSQL

Les opérations suivantes sont soutenues sur le terrain :
- ajouter un nouveau champ
- supprimer le champ

![image61](images/entries/87223743-a4b7e700-c37f-11ea-88a3-4b371bfadf89.gif)

![image62](images/entries/d4e761ad977a712aa1fc1fbc65d61c886e6e79fb.webp)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
## Fournisseurs de données
### Connexions du service de tuiles vectorielles ArcGIS
Une option permettant de créer des connexions pour les services de tuiles vectorielles ArcGIS a été ajoutée pour permettre aux utilisateurs de charger facilement des couches de tuiles vectorielles à partir des services de tuiles vectorielles ArcGIS Server. Elle a également ajouté la prise en charge de l'authentification, de la configuration et de la chaîne de référencement personnalisée pour les connexions de tuiles vectorielles.

Ce changement ajoute des options d'interface utilisateur explicites pour l'ajout et la configuration de connexions aux services de tuiles vectorielles ESRI. Bien que ces services utilisent le cadre standard des tuiles vectorielles pour la recherche de données, ils peuvent être directement ajoutés en créant une connexion à l'aide du point d'extrémité de l'API VectorTileService sur le serveur ArcGIS.

After a user adds a layer from a VectorTileService, the server\'s default styling and labeling for the layer is automatically loaded.

![image63](images/entries/e31c882fa9552ed6bd247f0092305ae8c153948a.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Propagation des métadonnées de la couche de cnfiance
Le drapeau de confiance au niveau du projet n'est utilisé que pour lire l'étendue de la couche vecteur à partir du xml, et non du fournisseur.

This flag was not available at the vector layer and data provider level. A new QgsMapLayer reading flag to propagate the trust layer metadata for the project\'s read flag and a new provider flag to trust the datasource config.

La confiance dans la configuration de la source de données permet au fournisseur d'utiliser des métadonnées estimées, garantit que la clé primaire est unique et que le type de géométrie détectable et le SRID sont les mêmes que ceux demandés.

This feature was developed by [rldhont](https://api.github.com/users/rldhont)
### Ajouter le support des colonnes virtuelles dans Oracle
La prise en charge des colonnes Oracle virtuelles (générées) a été ajoutée et est définie de cette manière :

`sql CREATE TABLE QGIS.GENERATED_COLUMNS ( "pk" INTEGER PRIMARY KEY, "generated_field" GENERATED ALWAYS AS ('test:' || "pk") VIRTUAL);`

**Note:** It\'s not possible to define a generated column on an SDO_GEOMETRY field in Oracle.

For now, when creating a new feature, the generated field is editable and should not be. A new API method needs to be added to retrieve readonly field from the provider as discussed in [Issue 35995](https://github.com/qgis/QGIS/pull/35995#issuecomment-633055700).

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Ajouter des options avancées pour l'importation de données
Une nouvelle fonctionnalité a été introduite qui permet de spécifier des paramètres avancés lors de l'importation de couches à l'aide du fournisseur de données OGR, ce qui ouvre un vaste éventail de nouvelles possibilités, en particulier pour contourner les problèmes attendus des ensembles de données.

![image64](images/entries/e1c7474d19828b39f5872b289a1e8ba994556a10-1.webp)

![image65](images/entries/4a2d99c6ef6ec12e5f63a29ad00d9ebc3cd534e2.webp)

This feature was developed by [Even Rouault](https://api.github.com/users/rouault)
## QGIS Server
### QGIS Server WFS3 API Sorting
Ajoute une fonctionnalité de tri à l'API WFS3 de QGIS server

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Plugin de la page d'accueil de QGIS Server
A Landing Page Plugin for QGIS Server was created, which is a C++ port of <https://github.com/elpaso/qgis-server-landing-page-plugin>

![image66](images/entries/a2254bbef892835317a9f608afd8bd3722ee4b38.gif)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Variable d'environnement permettant de désactiver GetPrint et de ne pas charger les mises en page
A new `QGIS_SERVER_DISABLE_GETPRINT` environment variable was added to QGIS Server which prevents the loading of layouts when projects are read and disables the WMS GetPrint request, improving the read time of projects.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
### Variable d'environnement pour faire confiance aux métadonnées de la couche avec les paramètres du serveur
Les métadonnées de la couche de confiance peuvent être définies au niveau du projet. Un nouveau drapeau de lecture de projet a été ajouté, qui permet de forcer les métadonnées de la couche de confiance.

For QGIS server, the trust layer metadata option can be overridden with `QGIS_SERVER_TRUST_LAYER_METADATA` environment variable.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
## Correctifs notables
### Correction de bugs par Even Rouault
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Scrolling attribute table of a layer added with the \"delimted text provider\" is almost impossible | [#38068](https://github.com/qgis/QGIS/issues/38068) | [PR #38735](https://github.com/qgis/QGIS/pull/38735) | [PR #38745](https://github.com/qgis/QGIS/pull/38745) |
| Prise en charge des clés API via une requête pour l'API mettant en œuvre l'API de l'OGC - Features | [#38436](https://github.com/qgis/QGIS/issues/38436) | [PR #38738](https://github.com/qgis/QGIS/pull/38738) | N/A |
| Les CRS personnalisés ne commutent pas toujours correctement les paramètres de wkt à la chaîne proj | [#38689](https://github.com/qgis/QGIS/issues/38689) | impossible à reproduire |  |
| Le client OGC API Features utilise toujours limit=1000 | [#38666](https://github.com/qgis/QGIS/issues/38666) | impossible à reproduire |  |
| L'exportation vers le géopackage modifie le type de champ de DATE à DATETIME | [#37857](https://github.com/qgis/QGIS/issues/37857) | pas un bug |  |
| Champ de date CSV interprété comme type de temps | [#38091](https://github.com/qgis/QGIS/issues/38091) | [PR #38741](https://github.com/qgis/QGIS/pull/38741) | N/A |
| Différence de transformation des coordonnées entre QGIS et Proj | [#38190](https://github.com/qgis/QGIS/issues/38190) | problème d'utilisation |  |
| gdal_rasterize not working when file has \'&\' symbol in name | [#38674](https://github.com/qgis/QGIS/issues/38674) | [PR #38743](https://github.com/qgis/QGIS/pull/38743) | [PR #38747](https://github.com/qgis/QGIS/pull/38747) |
| Core dump when using identify feature on a vector polygon | [#36213](https://github.com/qgis/QGIS/issues/36213) | déjà corrigé |  |
| Error of the raster histogram of QGIS 3.10.8(LTR) | [#38298](https://github.com/qgis/QGIS/issues/38298) | [PR #38769](https://github.com/qgis/QGIS/pull/38769) | À faire |
| \[Postgres\] Cannot edit attribute when there is no primary key | [#37917](https://github.com/qgis/QGIS/issues/37917) | pas un bug à mon avis |  |
| Switching between WMS info-output formats throws: CRITICAL QTableWidget: cannot insert an item that is already owned by another QTableWidget | [#37215](https://github.com/qgis/QGIS/issues/37215) | [PR #38770](https://github.com/qgis/QGIS/pull/38770) | [PR #38783](https://github.com/qgis/QGIS/pull/38783) |
| SaveAs Geopackage: TEXT fields are converted to TEXT(255) | [#25405](https://github.com/qgis/QGIS/issues/25405) | déjà corrigé |  |
| \"Join attributes by nearest\" tool defaults to \"None\" when using Max distance of 0 | [#38761](https://github.com/qgis/QGIS/issues/38761) | [PR #38773](https://github.com/qgis/QGIS/pull/38773) | No, not appropriate (see [PR #38778](https://github.com/qgis/QGIS/pull/38778)) |
| Lost edits in layer of same transaction group | [#38697](https://github.com/qgis/QGIS/issues/38697) | [PR #38779](https://github.com/qgis/QGIS/pull/38779) + [PR #38780](https://github.com/qgis/QGIS/pull/38780) | [PR #38824](https://github.com/qgis/QGIS/pull/38824) |
| Preview of Expression String Builder \'freezes\' if Feature id higher then available | [#38646](https://github.com/qgis/QGIS/issues/38646) | [PR #38797](https://github.com/qgis/QGIS/pull/38797) | N/A |
| VectorFileWriter/OGR provider: workaround GDAL 3.1.x bug regarding XLSX and ODS creation | non reporté | [PR #38837](https://github.com/qgis/QGIS/pull/38837) | [PR #38853](https://github.com/qgis/QGIS/pull/38853) |
| Coordinate operation widget: avoid repeating scope and remarks | non reporté | [PR #38847](https://github.com/qgis/QGIS/pull/38847) | N/A |
| Freeze when showing attribute table of WFS layer | [#37224](https://github.com/qgis/QGIS/issues/37224) | [PR #38952](https://github.com/qgis/QGIS/pull/38952) | [PR #38956](https://github.com/qgis/QGIS/pull/38956) |
| OGR Error when editing a kml file | [#39087](https://github.com/qgis/QGIS/issues/39087) | [GDAL Commit 72e1a4d7c96e0381d2d335857697b5f8e1668450](https://github.com/OSGeo/gdal/commit/72e1a4d7c96e0381d2d335857697b5f8e1668450) | Également appliqué à la branche GDAL 3.1 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Correction de bugs par Alessandro Pasotti
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Loading PostGIS layers with no specified geometry loads all features in the attribute table. | [PR #35367](https://github.com/qgis/QGIS/pull/35367) [#38565](https://github.com/qgis/QGIS/issues/38565) | Backport only | [PR #38736](https://github.com/qgis/QGIS/pull/38736) |
| Server API: current project is not settable anymore | [#38755](https://github.com/qgis/QGIS/issues/38755) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) |
| PostGIS layer saved in 3.10 project, fail to load correctly on 3.14 | [#38567](https://github.com/qgis/QGIS/issues/38567) | [PR #38763](https://github.com/qgis/QGIS/pull/38763) | N/A |
| Server WFS-T 1.1.0 wrong case for totalUpdated, totalInserted, totalDeleted | [#38558](https://github.com/qgis/QGIS/issues/38558) | [PR #38764](https://github.com/qgis/QGIS/pull/38764) | À faire |
| Server crashes on GetLegendGraphics when RULE does not exists. | [#38766](https://github.com/qgis/QGIS/issues/38766) | [PR #38775](https://github.com/qgis/QGIS/pull/38775) | [PR #38794](https://github.com/qgis/QGIS/pull/38794) |
| Form view gets stuck in the last shown not-NULL-value for some attributes when browsing through data | [#38552](https://github.com/qgis/QGIS/issues/38552) | [PR #38801](https://github.com/qgis/QGIS/pull/38801) | À faire |
| Marker line Simple marker rotation override not respecting follow line direction setting | [#38716](https://github.com/qgis/QGIS/issues/38716) | [PR #38815](https://github.com/qgis/QGIS/pull/38815) |  |
| Unable to dock the \"snapping options\" widget | [#38604](https://github.com/qgis/QGIS/issues/38604) | fonctionne pour moi |  |
| Can\'t read PG data sources when saved in version 3.10 and using service / auth combo | [#38809](https://github.com/qgis/QGIS/issues/38809) | [PR #38833](https://github.com/qgis/QGIS/pull/38833) | N/A |
| DB Manager \"cancel\" button to stop a query is not working | [#38092](https://github.com/qgis/QGIS/issues/38092) | [PR #38870](https://github.com/qgis/QGIS/pull/38870) | N/A |
| GDAL enhancement related to [#38092](https://github.com/qgis/QGIS/issues/38092) | [#38092](https://github.com/qgis/QGIS/issues/38092)2 | <https://github.com/OSGeo/gdal/pull/2953#event-3788638320> | N/A |
| Shift values issue while creating new field under DB Manager | [#38800](https://github.com/qgis/QGIS/issues/38800) | fonctionne pour moi |  |
| Problem with VUV wms | [#38924](https://github.com/qgis/QGIS/issues/38924) | fonctionne pour moi |  |
| Data Source Manager: WMS/WMTS Window not resizable | [#38903](https://github.com/qgis/QGIS/issues/38903) | fonctionne pour moi, en attente de retours |  |
| Form tab option \"Show as group box\" won\'t save or apply | [#38539](https://github.com/qgis/QGIS/issues/38539) | fonctionne pour moi |  |
| Scale lock is ignored when panning the map | [#38953](https://github.com/qgis/QGIS/issues/38953) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/A |
| Zoom to layer overwrites locked scale bug | [#38417](https://github.com/qgis/QGIS/issues/38417) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/A |
| Repeated column names cause visualization issues in DB Manager | [#38976](https://github.com/qgis/QGIS/issues/38976) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/A |
| \"show search_path\" returns 0 rows | [#38975](https://github.com/qgis/QGIS/issues/38975) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/A |
| PG NOTIFY not accessible | [#38986](https://github.com/qgis/QGIS/issues/38986) | fonctionne pour moi |  |
| Fix PG db-manager rename schema | [#38998](https://github.com/qgis/QGIS/issues/38998) | [PR #39000](https://github.com/qgis/QGIS/pull/39000) | N/A |
| Several PG browser items UX issues | [#39001](https://github.com/qgis/QGIS/issues/39001) | [PR #39006](https://github.com/qgis/QGIS/pull/39006) | N/A |
| Virtual vector does not load correctly on Windows | [#35016](https://github.com/qgis/QGIS/issues/35016) | fonctionne pour moi sur Windows et la version master actuelle |  |
| DB Manager: PostgreSQL field comments are not displayed correctly | [#38394](https://github.com/qgis/QGIS/issues/38394) | [PR #39026](https://github.com/qgis/QGIS/pull/39026) |  |
| Only first row for Postgis raster table in DB Manager preview and when adding layer to Map canvas | [#39017](https://github.com/qgis/QGIS/issues/39017) | [PR #39039](https://github.com/qgis/QGIS/pull/39039) | N/A |
| erroneous postgis query when trying to discover relations | [#39036](https://github.com/qgis/QGIS/issues/39036) |  |  |
| many additional tables that are already loaded in the project are loaded on project load because of layer dependencies | [#39025](https://github.com/qgis/QGIS/issues/39025) | [PR #39043](https://github.com/qgis/QGIS/pull/39043) | N/A |
| Partial fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39071](https://github.com/qgis/QGIS/pull/39071) | N/A |
| Allow to set precision for raster single band presudocolor classification | non reporté | [PR #39079](https://github.com/qgis/QGIS/pull/39079) |  |
| Complete fix for : Wrong assignments of raster values to symbology Paletted/Unique values or Singleband Pseudocolor | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39088](https://github.com/qgis/QGIS/pull/39088) | Risqué |
| Failure with identifier sequence when adding feature | [#39093](https://github.com/qgis/QGIS/issues/39093) | fonctionne pour moi |  |
| Export report to PDF crashes QGIS if no layout is in edit mode | [#39086](https://github.com/qgis/QGIS/issues/39086) | [PR #39135](https://github.com/qgis/QGIS/pull/39135) | À faire |
| PG raster: float rasters do not show nodata values correctly in master/3.14 | [#39142](https://github.com/qgis/QGIS/issues/39142) | [#39142](https://github.com/qgis/QGIS/issues/39142) |  |
| Python API call QgsAbstractDatabaseProviderConnection::TableProperty exceptions not converted to QgsProviderConnectionException | [#39151](https://github.com/qgis/QGIS/issues/39151) | [PR #39152](https://github.com/qgis/QGIS/pull/39152) | N/A |
| DB Manager unable to show PostGIS geography column | [#37666](https://github.com/qgis/QGIS/issues/37666) | [PR #39154](https://github.com/qgis/QGIS/pull/39154) | N/A |
| setting a field to NULL via field calculator freezes qgis | [#39178](https://github.com/qgis/QGIS/issues/39178) | [PR #39257](https://github.com/qgis/QGIS/pull/39257) | À faire |
| Layer X: Feature has too many attributes (expecting 5, received 7) when \"Automatic Creation of Transaction Group\" is enabled | [#39230](https://github.com/qgis/QGIS/issues/39230) | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | [PR #39278](https://github.com/qgis/QGIS/pull/39278) |
| unreported crash when calling data provider\'s lastError on no errors | non reporté | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | N/A |
| Crash digitizing a feature when transaction group is on (after save) | [#39265](https://github.com/qgis/QGIS/issues/39265) | [PR #39283](https://github.com/qgis/QGIS/pull/39283) |  |
| Transaction groups: not-current layers a set to not editable after save | [#39282](https://github.com/qgis/QGIS/issues/39282) | [PR #39286](https://github.com/qgis/QGIS/pull/39286) | non critique |
| OGR decodeUri: be tolerant on layerName case | not reported but impact the QGIS-Documentation | [PR #39328](https://github.com/qgis/QGIS/pull/39328) | N/A |
| Wrong extension handling in links when layer name has dots | non reporté | [PR #39346](https://github.com/qgis/QGIS/pull/39346) | N/A |
| Passwords are URL-encoded before base64 encoding for HTTP Basic auth | [#39243](https://github.com/qgis/QGIS/issues/39243) | [PR #39347](https://github.com/qgis/QGIS/pull/39347) | [PR #39382](https://github.com/qgis/QGIS/pull/39382) |
| QGIS crash in Settings menu if NOT in english | [#39430](https://github.com/qgis/QGIS/issues/39430) | [PR #39434](https://github.com/qgis/QGIS/pull/39434) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Correction de bugs par Peter Petrik
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Problem with displaying mesh and canvas rotation | [#35147](https://github.com/qgis/QGIS/issues/35147) | [PR #38795](https://github.com/qgis/QGIS/pull/38795)/files | non, pas critique |
| Crash while attempting to use mesh | [#31773](https://github.com/qgis/QGIS/issues/31773) | impossible à reproduire |  |
| Spatial Bookmark Manager Bad Behavior and Crashing App | [#35348](https://github.com/qgis/QGIS/issues/35348) | impossible à reproduire |  |
| Seqmentation fault 11 on QGIS shutdown on MacOS | non reporté | [PR #38806](https://github.com/qgis/QGIS/pull/38806) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| Crash when creating New MSSQL connexion on macOS | [#35026](https://github.com/qgis/QGIS/issues/35026) | [PR #39084](https://github.com/qgis/QGIS/pull/39084) | different packaging system\... |
| qgis_process is installed in the wrong place on MacOS | [#38447](https://github.com/qgis/QGIS/issues/38447) | [Mac Packager Commit 97b0ec974e2309e447ebb69c4117580db27af6f0](https://github.com/qgis/QGIS-Mac-Packager/commit/97b0ec974e2309e447ebb69c4117580db27af6f0) | N/A |
| Impossible de lancer l'extension GRASS sur MacOS | [#32511](https://github.com/qgis/QGIS/issues/32511) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| Processing: GRASS r.drain fails on macOS: \"No module named site\", \"Raster not found\" | [#36126](https://github.com/qgis/QGIS/issues/36126) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| The Grass7 processing toolbox option dialogue should include a way to specify a path to the GRASS binary, overriding Grass7Utils.command | [#29454](https://github.com/qgis/QGIS/issues/29454) | impossible à reproduire |  |
| Path error GRASS plugin QGIS 3.14 | [#38595](https://github.com/qgis/QGIS/issues/38595) | [PR #38840](https://github.com/qgis/QGIS/pull/38840) | different packaging system\... |
| No Print dialog or Page Setup dialog in macOS | [#30791](https://github.com/qgis/QGIS/issues/30791) | impossible à reproduire |  |
| Splash Screen Persists While \'Handle Bad Layers\' Dialog is Open | [#34784](https://github.com/qgis/QGIS/issues/34784) | [PR #38842](https://github.com/qgis/QGIS/pull/38842) | inapproprié |
| qgis terms of license pop up bug | [#38588](https://github.com/qgis/QGIS/issues/38588) | impossible à reproduire |  |
| Cannot load pictures anymore in custom forms | [#30833](https://github.com/qgis/QGIS/issues/30833) | already fixed by [Mac Packager Issue #3](https://github.com/qgis/QGIS-Mac-Packager/issues/3) | inapproprié |
|  | [Mac Packager Issue #83](https://github.com/qgis/QGIS-Mac-Packager/issues/83) | [Mac Packager Commit 36f86759649abc4cb8f6875f6ad934070c13d56e](https://github.com/qgis/QGIS-Mac-Packager/commit/36f86759649abc4cb8f6875f6ad934070c13d56e) | different packaging system\... |
| Projections not reading in MacOS Nightly Build | [#38919](https://github.com/qgis/QGIS/issues/38919) | [PR #38922](https://github.com/qgis/QGIS/pull/38922) | different packaging system\... |
| layers in .osm format are not loading | [Mac Packager Issue #84](https://github.com/qgis/QGIS-Mac-Packager/issues/84) | impossible à reproduire | fonctionne avec la 3.10 |
| missing metadata python package | [Mac Packager Issue #87](https://github.com/qgis/QGIS-Mac-Packager/issues/87) | [Mac Packager Commit 7c94749579acaf059e9b6c5094c7a2cb74d17f7a](https://github.com/qgis/QGIS-Mac-Packager/commit/7c94749579acaf059e9b6c5094c7a2cb74d17f7a) | different packaging system\... |
| GeoPDF Export fails | [Mac Packager Issue #75](https://github.com/qgis/QGIS-Mac-Packager/issues/75) | works now with qgis-deps-0.5.5 | different packaging system\... |
| GRASS Console not work on Mac | [#38961](https://github.com/qgis/QGIS/issues/38961) | [Mac Packager Commit bfc4ca0717de0e496d98f91e7a28e85216763ab1](https://github.com/qgis/QGIS-Mac-Packager/commit/bfc4ca0717de0e496d98f91e7a28e85216763ab1) | different packaging system\... |
| Processing Plugin Crashes QGIS on MacOS Nightly Build | [#38960](https://github.com/qgis/QGIS/issues/38960) | [PR #38973](https://github.com/qgis/QGIS/pull/38973) | different packaging system\... |
| Program crash when pasting file name | [#38939](https://github.com/qgis/QGIS/issues/38939) | impossible à reproduire |  |
| Wrong Python default path in QGIS server on macOS | [#29843](https://github.com/qgis/QGIS/issues/29843) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| qgis_map.fcgi on macOS doesn\'t find libraries | [#29399](https://github.com/qgis/QGIS/issues/29399) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| GRASS provider cannot get projection | [#31397](https://github.com/qgis/QGIS/issues/31397) | [Mac Packager Commit bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95](https://github.com/qgis/QGIS-Mac-Packager/commit/bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95) | different packaging system\... |
| QGIS crashing on start on Mac | [#38858](https://github.com/qgis/QGIS/issues/38858) | corrupted user profile | N/A |
| Browser cannot open Volumes under macOS | [#29702](https://github.com/qgis/QGIS/issues/29702) | [PR #39096](https://github.com/qgis/QGIS/pull/39096) | non, pas critique |
| MetaSearch unexpected keyword argument \'auth\' | [#38074](https://github.com/qgis/QGIS/issues/38074) | impossible à reproduire sur la version master | different packaging system\... |
| No QGIS plugins found in /Applications/QGIS3.10.app/Contents/MacOS/../PlugIns/qgis | [#39044](https://github.com/qgis/QGIS/issues/39044) | impossible à reproduire sur la version master | different packaging system\... |
| Browser Panel: unable to find all the connected drives | [#24641](https://github.com/qgis/QGIS/issues/24641) | duplicate of [#29702](https://github.com/qgis/QGIS/issues/29702) for MacOS |  |
| Provider Settings for GRASS avoid to active OTB | [#39112](https://github.com/qgis/QGIS/issues/39112) | impossible à reproduire sur la version master |  |
| Can\'t open GeoJSON vector via HTTP protocol on Windows and macOS | [#37107](https://github.com/qgis/QGIS/issues/37107) | \"[Mac Packager Commit d06bc3ac933c75071f36937aaf8189920dccc503](https://github.com/qgis/QGIS-Mac-Packager/commit/d06bc3ac933c75071f36937aaf8189920dccc503) | different packaging system\... |
| QGIS 3.0.1 Crash - Zooming in while moving node crashes QGIS | [#26509](https://github.com/qgis/QGIS/issues/26509) | impossible à reproduire |  |
| Crash when switching user profiles (too early?) | [#26993](https://github.com/qgis/QGIS/issues/26993) | impossible à reproduire |  |
| Aborted when debugging python plugin with pdb | [#27201](https://github.com/qgis/QGIS/issues/27201) | impossible à reproduire / invalide |  |
| Customization: the widget catcher can\'t select icon from a toolbar when it\'s under a group of icons | [#22967](https://github.com/qgis/QGIS/issues/22967) | [PR #39209](https://github.com/qgis/QGIS/pull/39209) | non critique |
| QGIS on macOS can save file in qgz-format, but won\'t open files in qgz format | [#39204](https://github.com/qgis/QGIS/issues/39204) | impossible à reproduire |  |
| Mouse pointer keeps switching type | [#32947](https://github.com/qgis/QGIS/issues/32947) | probablement une demande de fonctionnalité, pas un bug |  |
| Aggregate function bug on macOS version | \"[#32932](https://github.com/qgis/QGIS/issues/32932) | impossible à reproduire sur la version master | different packaging system\... |
| Clear filter in Snapping Toolbar \> Edit advanced configuration causes crash | [#29750](https://github.com/qgis/QGIS/issues/29750) | impossible à reproduire sur la version master |  |
| Snapping Settings window with Night Mapping, low readability | [#29751](https://github.com/qgis/QGIS/issues/29751) | déjà corrigé |  |
| Merge raster fails in macOS | [#39213](https://github.com/qgis/QGIS/issues/39213) | impossible à reproduire sur la version master | different packaging system\... |
| Can\'t get info on WFS feature in MacOS nightly build | [#39223](https://github.com/qgis/QGIS/issues/39223) | [Mac Packager Commit 54872e06a43ef61bf6dae8242e121bd5cec8be11](https://github.com/qgis/QGIS-Mac-Packager/commit/54872e06a43ef61bf6dae8242e121bd5cec8be11) | different packaging system\... |
| Crashs de QGIS 3.4.10 - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | déjà corrigé | déjà corrigé |
| Exporting GRASS vector (save as\...) crashes QGIS | [#37508](https://github.com/qgis/QGIS/issues/37508) | [PR #39284](https://github.com/qgis/QGIS/pull/39284) | À faire |
| Crash when loading 3D project with DEM terrain and symbols that uses height value over the terrain | [#35483](https://github.com/qgis/QGIS/issues/35483) | [PR #39287](https://github.com/qgis/QGIS/pull/39287) | À faire |
| Creating 3D View from raster | [#37163](https://github.com/qgis/QGIS/issues/37163) | duplicate of [#35483](https://github.com/qgis/QGIS/issues/35483) | N/A |
| Crash when moving camera in 3D | \"[#37881](https://github.com/qgis/QGIS/issues/37881) | impossible à reproduire sur la version master |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Correction de bugs par Paul Blottiere
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Linebreak issue with editing expression of \"Title Label Decoration\" | [#37803](https://github.com/qgis/QGIS/issues/37803) | [PR #38817](https://github.com/qgis/QGIS/pull/38817) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| QGIS Server GetPrint: EXTERNAL_WMS layer on top of QGIS layer | [#35873](https://github.com/qgis/QGIS/issues/35873) | [PR #38548](https://github.com/qgis/QGIS/pull/38548) | N/A |
| Fixes OGC API Features certification | non reporté | [PR #37622](https://github.com/qgis/QGIS/pull/37622) | N/A |
| Outdated help for labels \"data-defined\" placement group options | [#36680](https://github.com/qgis/QGIS/issues/36680) | [PR #37344](https://github.com/qgis/QGIS/pull/37344) |  |
| Server GetFeatureInfo returns 0 where is should return NULL | [#37781](https://github.com/qgis/QGIS/issues/37781) | [PR #38807](https://github.com/qgis/QGIS/pull/38807) |  |
| z function returns Nan when used with a 2d point geometry | [#37772](https://github.com/qgis/QGIS/issues/37772) | [PR #38831](https://github.com/qgis/QGIS/pull/38831) |  |
| m function returns Nan when used with a 2d point geometry | non reporté | [PR #38831](https://github.com/qgis/QGIS/pull/38831)/commits/829ee25d431b2b3d1ea08fa8a930bb519ab2dd2f |  |
| processing.algorithmHelp from terminal (outside QGIS desktop) | [#37524](https://github.com/qgis/QGIS/issues/37524) | impossible à reproduire |  |
| Cache join layer in memory\" not toggling when editing join properties | [#37326](https://github.com/qgis/QGIS/issues/37326) | [PR #38838](https://github.com/qgis/QGIS/pull/38838) |  |
| Map tips should not appear for invisible features | [#37066](https://github.com/qgis/QGIS/issues/37066) | [PR #38861](https://github.com/qgis/QGIS/pull/38861) |  |
| Merge features: manual value is not respected | [#37659](https://github.com/qgis/QGIS/issues/37659) | [PR #39083](https://github.com/qgis/QGIS/pull/39083) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Correction de bugs par Matthias Kuhn
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Legend nodes overlapping each other after inserting | [#38881](https://github.com/qgis/QGIS/issues/38881) | [PR #38882](https://github.com/qgis/QGIS/pull/38882) | non critique |
| Poor legend performance with complex legends | [#38890](https://github.com/qgis/QGIS/issues/38890) | [PR #38891](https://github.com/qgis/QGIS/pull/38891) | non critique |
| AMS layers cannot be added when no project CRS is set | [#38892](https://github.com/qgis/QGIS/issues/38892) | [PR #38893](https://github.com/qgis/QGIS/pull/38893) | non prévu |
| Legend performance problems | [#38978](https://github.com/qgis/QGIS/issues/38978) | [PR #39066](https://github.com/qgis/QGIS/pull/39066) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Matthias Kuhn](https://www.opengis.ch/)
### Corrections de bug par Julien Cabieces
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingAlgRunnerTask started inside function crashes QGIS | [#38583](https://github.com/qgis/QGIS/issues/38583) | Ne sera pas corrigé |  |
| Geometry generator symbol not rendered if the feature itself is not on the map canvas | [#38579](https://github.com/qgis/QGIS/issues/38579) | Retour d'informations |  |
| Relation widget in input form tabs - NULL value filled with data in form | [#38549](https://github.com/qgis/QGIS/issues/38549) | Won't backport (too risky) | (Closed) [#38549](https://github.com/qgis/QGIS/issues/38549) |
| Warning message: Missing layer form dependency : layer \'layerX\' requires layer \'layerY\' to be loaded | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | N/A |
| When embedding a layer, the display expression of a relation reference is not taken over | [#38422](https://github.com/qgis/QGIS/issues/38422) | Closed (FeatureRequest) |  |
| the keybord shortcut CTRL+C copy only the first cell, not the whole line | [#37503](https://github.com/qgis/QGIS/issues/37503) | [PR #38810](https://github.com/qgis/QGIS/pull/38810) |  |
| if shortcut is set for copy features then Ctrl+C not working anymore | [#37401](https://github.com/qgis/QGIS/issues/37401) | Doublon de #37503 |  |
| Organize columns not working if the table is empty | [#38653](https://github.com/qgis/QGIS/issues/38653) | Upstream (Qt) |  |
| Copy and paste style for forms ignores edit widget type | [#37702](https://github.com/qgis/QGIS/issues/37702) | [PR #38836](https://github.com/qgis/QGIS/pull/38836) |  |
| Keep order when drag and drop multiple widget | [#37038](https://github.com/qgis/QGIS/issues/37038) | [PR #38844](https://github.com/qgis/QGIS/pull/38844) | [PR #39239](https://github.com/qgis/QGIS/pull/39239) |
| QGIS crash removing QgsAnnotation in python | [#36098](https://github.com/qgis/QGIS/issues/36098) | Retour d'informations |  |
| Error in SQL statement for Virtual layers may lock layers in map canvas | [#34378](https://github.com/qgis/QGIS/issues/34378) | [PR #38949](https://github.com/qgis/QGIS/pull/38949) | [PR #39023](https://github.com/qgis/QGIS/pull/39023) |
| Virtual field in virtual layer not found | [#38523](https://github.com/qgis/QGIS/issues/38523) | Retour d'informations |  |
| Closed ID column for temporary layer is not detected when creating virtual layers using data source manager | [#34830](https://github.com/qgis/QGIS/issues/34830) | Ne sera pas corrigé |  |
| Boolean virtual field unusable in virtual layers | [#31798](https://github.com/qgis/QGIS/issues/31798) | [PR #38957](https://github.com/qgis/QGIS/pull/38957) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| fails to generate virtual geometry layer based on virtual wkt field | [#28265](https://github.com/qgis/QGIS/issues/28265) | Retour d'informations |  |
| Closed virtual fields can\'t be filtered | [#28072](https://github.com/qgis/QGIS/issues/28072) | Non reproduit |  |
| Qgis crached after calculated field removed | [#26486](https://github.com/qgis/QGIS/issues/26486) | Non reproduit |  |
| sql \"order by\" does not work with the \"Add/Edit Virtual Layer\" feature | [#29043](https://github.com/qgis/QGIS/issues/29043) | Ne sera pas corrigé |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #39041](https://github.com/qgis/QGIS/pull/39041) |  |
| Oracle - can\'t create or a modify a connection | [#38979](https://github.com/qgis/QGIS/issues/38979) | [PR #39131](https://github.com/qgis/QGIS/pull/39131) |  |
| Test connection Oracle DB ready - OK greyed out ! | [#39116](https://github.com/qgis/QGIS/issues/39116) | Doublon de #38979 |  |
| Scale dependent snapping does not activate as long as it displays the scale as \"1:xxxxxx\" | [#39031](https://github.com/qgis/QGIS/issues/39031) | [PR #39133](https://github.com/qgis/QGIS/pull/39133) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Correction de bugs par Denis Rouzaud
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| correctly determine if variables are static in aggregate expression and filter, give \@parent in generic aggregates | [#33382](https://github.com/qgis/QGIS/issues/33382) | [PR #39391](https://github.com/qgis/QGIS/pull/39391) | non |
| Freeze when using aggregate in a virtual field | [#39366](https://github.com/qgis/QGIS/issues/39366) | Ne sera pas corrigé |  |
| Fix SVG marker anchor calculation and improve bounds | [PR #39336](https://github.com/qgis/QGIS/pull/39336) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39421](https://github.com/qgis/QGIS/pull/39421) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39519](https://github.com/qgis/QGIS/pull/39519) |  |  |
| Improve SVG UI + remove duplicated code | [PR #39524](https://github.com/qgis/QGIS/pull/39524) |  |  |
| Fix duplicating features | [PR #39548](https://github.com/qgis/QGIS/pull/39548) |  |  |
| fix duplication of feature being stopped at 1 level deep | [PR #39550](https://github.com/qgis/QGIS/pull/39550) |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Correction de bugs par Olivier Dalang
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Core topology fixer issues | non reporté | [PR #39392](https://github.com/qgis/QGIS/pull/39392) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Olivier Dalang](https://www.opengis.ch/)
### Correction de bugs par Nyall Dawson
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fix crash in dbmanager | [#38393](https://github.com/qgis/QGIS/issues/38393) | [Commit 8c623b268ed94ef65aa19e2271be10b75e1ef36a](https://github.com/qgis/QGIS/commit/8c623b268ed94ef65aa19e2271be10b75e1ef36a) | N/A |
| Fix GeoPDF page size issues when opened in Acrobat reader | [#33465](https://github.com/qgis/QGIS/issues/33465) | [Commit 460bf8e534eb32ccba665918a615b55a8cbccadd](https://github.com/qgis/QGIS/commit/460bf8e534eb32ccba665918a615b55a8cbccadd) | Delayed till more widespread user testing |
| Improve default lighting of 3d scenes | non reporté | [Commit 350bc602e0ecd0f93dc2cc90ab34ce09993a687b](https://github.com/qgis/QGIS/commit/350bc602e0ecd0f93dc2cc90ab34ce09993a687b) | N/A |
| Allow conversion of QgsFeatureStoreList results to Python objects | [#39479](https://github.com/qgis/QGIS/issues/39479) | [Commit 49c508921d7ccb59b1f1abaff4f890456cca1455](https://github.com/qgis/QGIS/commit/49c508921d7ccb59b1f1abaff4f890456cca1455) | Trop risqué |
| Fix preview symbol when offsetting point symbols isn\'t shown correctly | non reporté | [Commit 62409b92ce20a84dd92188cf42a98d7cdc0b08c3](https://github.com/qgis/QGIS/commit/62409b92ce20a84dd92188cf42a98d7cdc0b08c3) | N/A |
| Use click-click behavior for rotate and offset marker tools | non reporté | [Commit 00a3a6b8057f96dfa6c37943427a276cd3a5065d](https://github.com/qgis/QGIS/commit/00a3a6b8057f96dfa6c37943427a276cd3a5065d) | N/A |
| Avoid massive UI hangs when a layer has complicated actions defined | non reporté | [Commit 9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668](https://github.com/qgis/QGIS/commit/9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668) | Trop risqué |
| Ensure display expression is used for map action tool, not raw feature ids | non reporté | [Commit e304d4d7e3eae0f48f336c7eb34542be6055df5d](https://github.com/qgis/QGIS/commit/e304d4d7e3eae0f48f336c7eb34542be6055df5d) | Priorité basse |
| Improve UX when configuring lights in a 3d scene, fixes confusing interface | non reporté | [Commit 3019b82100d4fc405f64cebcddf9aaae253c4293](https://github.com/qgis/QGIS/commit/3019b82100d4fc405f64cebcddf9aaae253c4293) | N/A |
| Fix features with invalid geometries cannot be selected | [#38460](https://github.com/qgis/QGIS/issues/38460) | [Commit 22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d](https://github.com/qgis/QGIS/commit/22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d) | N/A |
| Expose metadata tab for mesh layers | non reporté | [Commit 9482b1be70f36f778f6a409847244c5ff8a6a739](https://github.com/qgis/QGIS/commit/9482b1be70f36f778f6a409847244c5ff8a6a739) | N/A |
| Fix missing text codecs on Windows installs | [#36871](https://github.com/qgis/QGIS/issues/36871) | [Commit c3ca85e60bec73056bd87c426fd71c8f578363cb](https://github.com/qgis/QGIS/commit/c3ca85e60bec73056bd87c426fd71c8f578363cb) | Trop risqué |
| Don\'t force a whole layout map to be rasterised just because one vector layer has non 100% opacity | non reporté | [Commit 2d15a4cfad6c732cf640fbb0eabd625856b643ca](https://github.com/qgis/QGIS/commit/2d15a4cfad6c732cf640fbb0eabd625856b643ca) | Trop risqué |
| Ensure mesh layer properties follows same appearance as other layer types | non reporté | [Commit 3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac](https://github.com/qgis/QGIS/commit/3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac) | N/A |
| Speed up mesh triangulation algorithm by avoiding a bunch of unnecessary QVector detachments | non reporté | [Commit 46ef391a7acf10515a11c19b69fafa4548046448](https://github.com/qgis/QGIS/commit/46ef391a7acf10515a11c19b69fafa4548046448) | N/A |
| Don\'t allow users to set 3d terrain to mesh or DEM without selecting an elevation layer, instead show friendly warning | non reporté | [Commit 0d9f1da846c70764fa6840309b5460f713b30e1f](https://github.com/qgis/QGIS/commit/0d9f1da846c70764fa6840309b5460f713b30e1f) | N/A |
| Avoid 3d map config dialog opening with initially out-of-sync selected pane | non reporté | [Commit 8b6477208f3c34e228734f7c04d32625965c48ed](https://github.com/qgis/QGIS/commit/8b6477208f3c34e228734f7c04d32625965c48ed) | N/A |
| Fix menu not shown when clicking \'add\' item in style manager dialog and color ramp tab is active | non reporté | [Commit a085ce84b81a46896c9f00ee64eccaea63dad29a](https://github.com/qgis/QGIS/commit/a085ce84b81a46896c9f00ee64eccaea63dad29a) | N/A |
| Fix trying to create new color ramp from first page in style manager dialog does nothing | non reporté | [Commit 34fb646f7ab69f20072b4d74ebec0595054089d7](https://github.com/qgis/QGIS/commit/34fb646f7ab69f20072b4d74ebec0595054089d7) | N/A |
| \[processing\] Fix generated layers stored in geopackage always report a feature count of 0 | non reporté | [Commit 0675d99b34ee209a09857dfcba47cb5a92f55154](https://github.com/qgis/QGIS/commit/0675d99b34ee209a09857dfcba47cb5a92f55154) | Trop risqué |
| Fix Import Geotagged photos algorithm incorrectly assigns form widgets when saving the results to GPKG | non reporté | [Commit ff336ade18f4d6b307e4ed0e98fee77ee11a157c](https://github.com/qgis/QGIS/commit/ff336ade18f4d6b307e4ed0e98fee77ee11a157c) | [PR #39563](https://github.com/qgis/QGIS/pull/39563) |
| \[processing\] Ensure driverName is passed to QgsVectorLayerExporter so that GPKG specific optimisations can be applied when saving outputs to geopackage | non reporté | [Commit 501c63feb3887e18da35188062546186d8a767ac](https://github.com/qgis/QGIS/commit/501c63feb3887e18da35188062546186d8a767ac) | Trop risqué |
| Update strings and UI regarding layer CRS override setting | [#32101](https://github.com/qgis/QGIS/issues/32101) | [Commit 06cfdd9563b15d8fbb27aee94b83d1b15773df77](https://github.com/qgis/QGIS/commit/06cfdd9563b15d8fbb27aee94b83d1b15773df77) | N/A |
| Use proper SQL code editor in filter preview widget in vector layer properties, don\'t show filter as disabled | non reporté | [Commit 0f4270cfe600e77f09db7727bd3ba965be7acb0e](https://github.com/qgis/QGIS/commit/0f4270cfe600e77f09db7727bd3ba965be7acb0e) | N/A |
| Fix boolean literal presentation in dox/PyQGIS docs | non reporté | [Commit 746ee315bd0a4140f6e84617d547cc89103f79aa](https://github.com/qgis/QGIS/commit/746ee315bd0a4140f6e84617d547cc89103f79aa) | N/A |
| Speed up QGIS geometry validation | non reporté | [Commit 2a15c3b0a4a631db1b55ac7e46256fdbd89949f9](https://github.com/qgis/QGIS/commit/2a15c3b0a4a631db1b55ac7e46256fdbd89949f9) | Trop risqué |
| \[processing\] Correctly discard fid field values when running algorithms with the RegeneratePrimaryKey flag in in-place mode | [#37761](https://github.com/qgis/QGIS/issues/37761), [#33816](https://github.com/qgis/QGIS/issues/33816) | [Commit db7b97705967041d4eaca7e7f69cbf49f5692aef](https://github.com/qgis/QGIS/commit/db7b97705967041d4eaca7e7f69cbf49f5692aef) | Trop risqué |
| \[processing\] When reporting that a feature is invalid, also mention the layer name | [#26664](https://github.com/qgis/QGIS/issues/26664) | [Commit a53bb3d49b59a3f814d862f30202ff156f74d6bc](https://github.com/qgis/QGIS/commit/a53bb3d49b59a3f814d862f30202ff156f74d6bc) | Trop risqué |
| Allow expanding xls, ods, gpx, pdf files in browser so that layer sources can be repaired for these file types | non reporté | [Commit 252976b739527e213f5d1c8c98a345911dfeab32](https://github.com/qgis/QGIS/commit/252976b739527e213f5d1c8c98a345911dfeab32) | N/A |
| \[processing\] Fix \"Split with lines\" algorithm can get stuck in an endless loop | non reporté | [Commit 05645b320d8547f50a308843e961e343c383036d](https://github.com/qgis/QGIS/commit/05645b320d8547f50a308843e961e343c383036d) | Trop risqué |
| Don\'t show cascaded feature deletion warnings and feedback if joined deleted features came from an auxilary layer | non reporté | [Commit 8c79b94fcc14e41d4442a018554e889f81b8e080](https://github.com/qgis/QGIS/commit/8c79b94fcc14e41d4442a018554e889f81b8e080) | N/A |
| Fix crash in undo dock when clearing project/closing QGIS | [#38157](https://github.com/qgis/QGIS/issues/38157) | [Commit d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8](https://github.com/qgis/QGIS/commit/d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8) | [Commit 5c97ff66dd90d450a1ec60583da9626c14c9c08c](https://github.com/qgis/QGIS/commit/5c97ff66dd90d450a1ec60583da9626c14c9c08c) |
| Fix copy/paste/select all shortcuts don\'t work when layer tree is selected | [#38849](https://github.com/qgis/QGIS/issues/38849) | [Commit 02d7afae3f8699e83efacc781d3266700397d8b8](https://github.com/qgis/QGIS/commit/02d7afae3f8699e83efacc781d3266700397d8b8) | N/A |
| Fix edited and new features no longer correctly show their corresponding color shading in the feature list view | non reporté | [Commit a195b056624c2fabe231be7c0e96c3d63e052e5b](https://github.com/qgis/QGIS/commit/a195b056624c2fabe231be7c0e96c3d63e052e5b) | Trop risqué / priorité faible |
| ALWAYS load processing plugin in qgis_process tool | [#37989](https://github.com/qgis/QGIS/issues/37989) | [Commit bc0df6d25e929a575d0821208f7d187737d80709](https://github.com/qgis/QGIS/commit/bc0df6d25e929a575d0821208f7d187737d80709) | N/A |
| Add \--json option to qgis_process tool | <https://github.com/paleolimbot/qgisprocess/issues/21> | [Commit fc8d916b8dd444b3edaee3c18ec308e74a9bb91e](https://github.com/qgis/QGIS/commit/fc8d916b8dd444b3edaee3c18ec308e74a9bb91e) | N/A |
| Ensure all code editors in QGIS follow the same appearance and behavior | non reporté | (many) | N/A |
| When creating a CRS from WKT and the WKT has an embedded CRS name, correctly use this to set the QgsCoordinateReferenceSystem description | non reporté | [Commit 9a35b27630982d63101c57c3e3440dcbf1a7786f](https://github.com/qgis/QGIS/commit/9a35b27630982d63101c57c3e3440dcbf1a7786f) | Possible after further user testing |
| Big speed up for scripts which fire off many individual feature requests to a memory provider layer | non reporté | [Commit 1d2bb41752c51e6c9b84124a1ce1599d3d42b41c](https://github.com/qgis/QGIS/commit/1d2bb41752c51e6c9b84124a1ce1599d3d42b41c) | Trop risqué |
| \[console\] Fix exception when running scripts | non reporté | [Commit 5c8013df6129a2bc06d25a98ff20dbf27621bff5](https://github.com/qgis/QGIS/commit/5c8013df6129a2bc06d25a98ff20dbf27621bff5) | N/A |
| \[layouts\] Fix resizing multiline label items to adjust to the size of their text | non reporté | [Commit 6829e6351e1dab18f1fa0c0443107eb7617794c7](https://github.com/qgis/QGIS/commit/6829e6351e1dab18f1fa0c0443107eb7617794c7) | Trop risqué |
| Improve appearance of PyQGIS documentation for functions which return multiple values | non reporté | [Commit 0001ec27a43cbf4c99d1525c3c5f75183e96f5c3](https://github.com/qgis/QGIS/commit/0001ec27a43cbf4c99d1525c3c5f75183e96f5c3) | N/A |
| \[processing\] Don\'t raise a generic \"something went wrong\" exception when calling processing.run(), instead use proper descriptive exception | non reporté | [Commit 2207c30a247e5907a12185165b4bd220e255bbdc](https://github.com/qgis/QGIS/commit/2207c30a247e5907a12185165b4bd220e255bbdc) | Trop risqué |
| \[processing\] Fix execution of \"Eliminate selection\" through Python | [#38808](https://github.com/qgis/QGIS/issues/38808) | [Commit ee7bea2305253fd276a69c25bb5d308942dcb190](https://github.com/qgis/QGIS/commit/ee7bea2305253fd276a69c25bb5d308942dcb190) | Trop risqué |
| \[3d\] Fix crash when line feature cannot be buffered | non reporté | [Commit f6eed85729a8cbf913155ae16df7499f688ba0fa](https://github.com/qgis/QGIS/commit/f6eed85729a8cbf913155ae16df7499f688ba0fa) | [Commit d4c963e1c2fdc497dba038896caf2b3f975240ff](https://github.com/qgis/QGIS/commit/d4c963e1c2fdc497dba038896caf2b3f975240ff) |
| Fix custom stroke patterns incorrectly scale when data defined stroke width is set | [#39201](https://github.com/qgis/QGIS/issues/39201) | [Commit 03fdc0cd7992a7883183704cd68506f32afe9ca3](https://github.com/qgis/QGIS/commit/03fdc0cd7992a7883183704cd68506f32afe9ca3) | Trop risqué |
| Allow columns to be resized in datum transformation table | [#39169](https://github.com/qgis/QGIS/issues/39169) | [Commit 1cd5a3358b235f67b6b4d95331ce561e9f8cb715](https://github.com/qgis/QGIS/commit/1cd5a3358b235f67b6b4d95331ce561e9f8cb715) | N/A |
| Fix settings incorrectly show for wrong layer types in labeling dialog | [#39168](https://github.com/qgis/QGIS/issues/39168) | [Commit 2e948884c029c9f79639201943ec4bc36dba3573](https://github.com/qgis/QGIS/commit/2e948884c029c9f79639201943ec4bc36dba3573) | N/A |
| \[processing\] Fix error reporting from batch dialog | [#39197](https://github.com/qgis/QGIS/issues/39197) | [Commit 5243a8594cc39540f2c01201415633801a22ff43](https://github.com/qgis/QGIS/commit/5243a8594cc39540f2c01201415633801a22ff43) | N/A |
| \[processing\] Fix crash when renaming conditional branch in modeler | [#39053](https://github.com/qgis/QGIS/issues/39053) | [Commit ddae53b7b789467bf17b21d6f4b884e827fbd3c5](https://github.com/qgis/QGIS/commit/ddae53b7b789467bf17b21d6f4b884e827fbd3c5) | N/A |
| \[processing\] Fix crash in model designer when a child algorithm contains hidden parameters | non reporté | [Commit f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0](https://github.com/qgis/QGIS/commit/f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0) | N/A |
| Ensure True/False are treated as Python keywords in Python code editor | non reporté | [Commit 5f661045c078b7938550c2c9d0798664c6f65f5a](https://github.com/qgis/QGIS/commit/5f661045c078b7938550c2c9d0798664c6f65f5a) | N/A |
| Don\'t silently close QGIS with unsaved changes in the console script editors | [#38529](https://github.com/qgis/QGIS/issues/38529) | [Commit 9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9](https://github.com/qgis/QGIS/commit/9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9) | Trop risqué |
| Fix dropping processing script algorithm .py file on QGIS no longer triggers the algorithm to execute | non reporté | [Commit 64bf347d7e1d664fc674c5ca602ce6c4bedecdf9](https://github.com/qgis/QGIS/commit/64bf347d7e1d664fc674c5ca602ce6c4bedecdf9) | N/A |
| Fix message log dock causes havoc with other docks placed in the same area | [#31955](https://github.com/qgis/QGIS/issues/31955) | [Commit 384f6a1d9257a05eaa58942921c94f1dd4941cd3](https://github.com/qgis/QGIS/commit/384f6a1d9257a05eaa58942921c94f1dd4941cd3) | Trop risqué |
| When restoring a custom CRS from XML, if the CRS does NOT match any of the existing user defined CRS\'s on the QGIS profile then still restore the previously saved name of the custom CRS | non reporté | [Commit e6d316ace7031821e04ca625e35f7c2c4d57f639](https://github.com/qgis/QGIS/commit/e6d316ace7031821e04ca625e35f7c2c4d57f639) | Possible after further user testing |
| Don\'t refer to valid but custom CRSes as \"Unknown CRS\" and instead use \"Custom CRS\" phrasing | non reporté | [Commit d3833fd8d6c4b4f0673c4c2337044c224675185f](https://github.com/qgis/QGIS/commit/d3833fd8d6c4b4f0673c4c2337044c224675185f) | Possible after further user testing |
| Improve performance of processing batch process dialog with a large number of files | [#38987](https://github.com/qgis/QGIS/issues/38987) | [Commit 776768eb9f4ee2a8d13909b4ced5c175a0d05b3d](https://github.com/qgis/QGIS/commit/776768eb9f4ee2a8d13909b4ced5c175a0d05b3d) | Trop risqué |
| Improve behavior of CRS selector and transformation widgets | non reporté | many | N/A |
| \[layouts\] Use standard CRS selector widget for map grid CRS choice | [#26548](https://github.com/qgis/QGIS/issues/26548) | [Commit 4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70](https://github.com/qgis/QGIS/commit/4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70) | Trop risqué |
| \[layouts\] When selecting a CRS for a map item, don\'t show misleading no crs option at the top of the dialog | non reporté | [Commit c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad](https://github.com/qgis/QGIS/commit/c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad) | Trop risqué |
| Fix \"layer has no CRS\" message incorrectly show at the top of many projection selection dialog boxes | non reporté | [Commit c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c](https://github.com/qgis/QGIS/commit/c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c) | Trop risqué |
| Fix crash when editing style and opening a project | [#38920](https://github.com/qgis/QGIS/issues/38920) | [Commit 67ec244864ca6f9290e1f35a1a0c60b4888fe686](https://github.com/qgis/QGIS/commit/67ec244864ca6f9290e1f35a1a0c60b4888fe686) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/ecf96231aefa5628539f0b63ca313ea8b20c9548 |
| Avoid qt warning when dragging a non-color object over color buttons | non reporté | [Commit fd771bba68da84b1ce8023898b9662b5dc619693](https://github.com/qgis/QGIS/commit/fd771bba68da84b1ce8023898b9662b5dc619693) | N/A |
| Fix shift in geopdf feature positions when using geographic CRS at large scales | [#37755](https://github.com/qgis/QGIS/issues/37755) | [Commit 0b77f187ec5a14651457fd07f306cba2511fb854](https://github.com/qgis/QGIS/commit/0b77f187ec5a14651457fd07f306cba2511fb854) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/b705d29c73e81fe87e2e301c7028e5e659d80364 |
| Fix constraint metadata is duplicated after opening layer properties | [#38916](https://github.com/qgis/QGIS/issues/38916) | [Commit 6a002573c00a8a8e11443eaca28b57a8ad6de4c0](https://github.com/qgis/QGIS/commit/6a002573c00a8a8e11443eaca28b57a8ad6de4c0) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/49260b8f1f4b1ddd9a25c7160f32570221f3989e |
| Fix PDF export includes vector information outside of the area of interest | [#38878](https://github.com/qgis/QGIS/issues/38878) | [Commit f3f226aa69a19b31dd8a1b83c82319528e061cfe](https://github.com/qgis/QGIS/commit/f3f226aa69a19b31dd8a1b83c82319528e061cfe) | Trop risqué |
| \[layouts\] Fix legend symbol rendering doesn\'t respect linked map scale when symbol uses map unit based sizes | [#38326](https://github.com/qgis/QGIS/issues/38326) | [Commit 426ee2120b33a8613f3e476da3c2eba0a00f65d7](https://github.com/qgis/QGIS/commit/426ee2120b33a8613f3e476da3c2eba0a00f65d7) | N/A |
| Don\'t try to write empty rendered rings/geometries to GeoPDF outputs | non reporté | [Commit 96753cfd1b9e986841158675bda365e585c48c27](https://github.com/qgis/QGIS/commit/96753cfd1b9e986841158675bda365e585c48c27) | Possible after further user testing |
| Correctly apply capitalization setting whenever QgsTextRenderer is used, not just in labeling | [#38898](https://github.com/qgis/QGIS/issues/38898) | [Commit e1ca83b2c24c51e7ff67a53278ffd2601c0459be](https://github.com/qgis/QGIS/commit/e1ca83b2c24c51e7ff67a53278ffd2601c0459be) | Trop risqué |
| Fix qgis_process list raises exception if processing algorithm provider is activated | [#38862](https://github.com/qgis/QGIS/issues/38862) | [Commit 772181bc16820d7dd5ee8d967355dbdfde5a8efe](https://github.com/qgis/QGIS/commit/772181bc16820d7dd5ee8d967355dbdfde5a8efe) | N/A |
| Dramatic speed up for calling some frequently used methods from PyQGIS | non reporté | [Commit d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca](https://github.com/qgis/QGIS/commit/d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca) | Trop risqué |
| \[processing\] Fix certain characters show as HTML escaped in processing log | [#37934](https://github.com/qgis/QGIS/issues/37934) | [Commit 965595d25bd0a69875ba8a405d3b365bedfe2a12](https://github.com/qgis/QGIS/commit/965595d25bd0a69875ba8a405d3b365bedfe2a12) | N/A |
| Fix incorrect capitalization in title of new layout name dialog | non reporté | [Commit 92d0ec59a1c26c4ac33d35b9e6c93344845eddca](https://github.com/qgis/QGIS/commit/92d0ec59a1c26c4ac33d35b9e6c93344845eddca) | N/A |
| Add a new capitalization option for \"Title Case\", and rename the confusing \"Capitalize First Letter\" option to Force First Letter to Capital | [#16539](https://github.com/qgis/QGIS/issues/16539) | [Commit 484ba6f979cdcaabffe823c72b35b57d1b1c7aad](https://github.com/qgis/QGIS/commit/484ba6f979cdcaabffe823c72b35b57d1b1c7aad) | N/A |
| Add a Legend category to the style selection widgets and allow legend settings to be stored and restored in QML | [#37683](https://github.com/qgis/QGIS/issues/37683) | [Commit f018252023275f95c167d7f308d05c8819d6db0b](https://github.com/qgis/QGIS/commit/f018252023275f95c167d7f308d05c8819d6db0b) | Trop risqué |
| Fix \[Style\] Export \--\> Save as QGIS Layer style File should allow to select style categories (and output format) | [#29145](https://github.com/qgis/QGIS/issues/29145) | [Commit 1ad2e78735e57cef218a7470d7eec645c2f45263](https://github.com/qgis/QGIS/commit/1ad2e78735e57cef218a7470d7eec645c2f45263) | Trop risqué |
| \[browser\] Correctly save expanded node state when closing QGIS | non reporté | [Commit 2eff061bf3cdcb3f36956e43098adfcb0359b5eb](https://github.com/qgis/QGIS/commit/2eff061bf3cdcb3f36956e43098adfcb0359b5eb) | Trop risqué |
| \[browser\] Gpkg and other container types can be dragged to the map to allow layers to be added from them | non reporté | [Commit 0234d4e9e10f3fbb5732f66e00eebd038f502ab0](https://github.com/qgis/QGIS/commit/0234d4e9e10f3fbb5732f66e00eebd038f502ab0) | Trop risqué |
| Don\'t prompt for CRS for annotation layers | [#38739](https://github.com/qgis/QGIS/issues/38739) | [Commit 15975c1d5191933311d81a494d87806f4e73ce57](https://github.com/qgis/QGIS/commit/15975c1d5191933311d81a494d87806f4e73ce57) | N/A |
| Fix reading saved color map file when an item\'s label contains a comma character | [#24112](https://github.com/qgis/QGIS/issues/24112) | [Commit 252149375c750d6a8f1ee281c1cc9d03de272170](https://github.com/qgis/QGIS/commit/252149375c750d6a8f1ee281c1cc9d03de272170) | Trop risqué |
| Fix diagram settings are not correctly restored when loading a QML file | [#35343](https://github.com/qgis/QGIS/issues/35343) | [Commit 4668927ce432b198b3c572535ff234343c5042f5](https://github.com/qgis/QGIS/commit/4668927ce432b198b3c572535ff234343c5042f5) | Trop risqué |
| Fix can no longer paste colors from text strings | non reporté | [PR #39561](https://github.com/qgis/QGIS/pull/39561) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
