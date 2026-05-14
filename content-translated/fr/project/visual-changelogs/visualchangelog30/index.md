---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.0
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.0{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

Date de publication : 23/02/2018

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Sponsors de QGIS 3.0
{{<fund type="changelog" relativeImgPath=true >}}
### Fonctionnalité : Supprimer l'extension convertisseur dxf2shp
Cette fonction est disponible dans OGR et une extension QGIS dédiée n'a plus lieu d'être pour achever cette tâche
### Fonctionnalité : Supprimer l'extension raster Oracle qui est orpheline
### Fonctionnalité : Supprimer le fournisseur TauDEM de la base de Processing
TauDEM est un ensemble d'outils assez spécifiques et il demande l'installation d'autres outils supplémentaires. Nous avons donc décidé de l'offrir en tant que fournisseur séparé, réduisant ainsi la taille du code de base et les efforts de maintenance.
### Fonctionnalité : De l'aide supplémentaire et la possibilité de configurer l'emplacement des fichiers d'aide de QGIS.
Des boutons supplémentaires d'aide pour les algorithmes et les dialogues sont ajoutés et pointent maintenant vers la documentation en ligne de QGIS.

La configuration permet d'accéder à l'aide contextuelle localisée en linge, soit sur le réseau de l'organisation, soit dans l'ordinateur local. Il est aussi possible de combiner des sources différentes d'aide.

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Déplacer les gadgets Photo, WebView et FileName vers Pièce-jointe
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### Fonctionnalité : Supprimer les fournisseurs OTB et lidartools de Processing
La nouvelle logique est de développer des fournisseurs d'extension qui soient capable de suivre le cycle d'évolution des logiciels externes.
## Interface utilisateur
### Fonctionnalité : Permet la tabulation dans les docks flottants
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### Fonctionnalité : Un contrôle plus fin du zoom avec la roue de la souris est fourni
Certains appareils de pointage / souris (particulièrement sur mac) ont des résolutions plus fines. Ils transmettent les événements de roue de souris à des fréquences plus élevées mais avec des valeurs delta plus petites. Les actions de zoom sur ces appareils n'étaient pas possible lors d'actions rapides de zoom. Cela est corrigé dans 3.0.

Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Une barre de recherche a été ajoutée au dialogue de configuration des raccourcis
Supporte la recherche par nom de l'action ou du raccourci

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Barre de localisation
La barre de localisation est une facilité de recherche rapide, toujours prête, générique et enfichable située dans le coin inférieur gauche de QGIS.

Elle permet, à présent, de rechercher le nom des algorithmes, actions et couches, mais aussi de sélectionner une entité dans la couche active courante en tapant une valeur d'attribut.

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

Cette fonctionnalité a été développée par Nyall Dawson
### Fonctionnalité : Plus d'édition en ligne non-bloquante
- dimensionnement des unités de carte
- éditeurs de mélangeur de couleurs et de rampe aléatoire limitée
- change les couleurs d'une liste directement dans le panneau de style
- change directement les couleurs et les symboles dans Composeur

directement affiché dans le panneau de style
### Fonctionnalité : Ajout d'une option pour montrer à l'utilisateur les menus de combinaisons de couleurs
Cela permet aux utilisateurs de décider si une combinaison de couleur crée par un utilisateur doit être affichée ou non dans les menus déroulants des boutons de couleur.

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

Cela est utile si vous avez des jeux communs de palettes et voulez qu'ils soient disponibles immédiatement par le menu de couleur.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Configuration de couleur pour la décoration flèche du Nord du canevas de carte
La configuration de la couleur de la décoration flèche du Nord a été ajoutée à tous les canevas de carte

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann (financement partiel).

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Basculer la visibilité des panneaux ouverts dans la fenêtre principale
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Amélioration dans l'harmonisation de l'interface utilisateur
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- Toutes les API **transparence/opacité/alpha** ont été standardisées en **setOpacity()** et **opacity()**. Les méthodes acceptent une valeur double précision entre 0 (transparent) et 1 (opaque), en cohérence avec l'API de Qt.
- Un **nouveau gadget QgsOpacityWidget** a été créé, et est maintenant utilisé partout dans l'IU pour fixer l'opacité. Cela encourage un comportement et un aspect uniformes pour les contrôles d'opacité dans l'ensemble de l'application.
- **Rotation** a été standardisée dans l'API et l'IU, de manière a toujours être appliquée dans le sens des aiguilles d'une montre. Tous les gadgets de rotation ont été mis à jour pour accepter une valeur entre -360 et +360.
- Les projets 2.x qui utilisent des rotations pour les labels et des rotations définies par l'utilisateur sont automatiquement **mis à jour** quand ils sont ouverts par 3.0
- Les API d'échelle ont été rendues cohérentes entre elles dans toute l'API QGIS. **Le mélange confus des dénominateurs d'échelle et des échelles vraies a été retiré**, maintenant, tout est fait avec des dénominateurs d'échelle. Le comportement de tous les appels de gamme d'échelle est standardisé avec un sens commun pour les échelles min/max (et la documentation explicite de l'API à cet effet)
- Tous les contrôles d'échelle utilisent maintenant les gadgets d'échelle pour la cohérence de toute l'IU.
- L'étiquetage utilise maintenant la même définition pour l'échelle min/max que le reste de l'IU, et les projets existants sont automatiquement mis à jour quand ils sont ouverts par 3.0.
- Corrections de la plupart des bogues restants liés à l'utilisation des échelles, y compris les bogues plantant les limites d'échelle basées sur des règles.

Merci aux donateurs du projet et du  PSC de QGIS pour avoir sponsorisé ce travail et lui permettre de continuer !

Cette fonctionnalité a été financée par les donateurs et sponsors de QGIS

This feature was developed by [Nyall Dawson](https://north-road.com)
### Fonctionnalité : Ouverture de couches dans un seul groupe
Si vous essayez de lire plusieurs sous-souches, vous pouvez maintenant toutes les ouvrir dans un même groupe, dans la légende.

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## Fonctionnalités 3D
### Fonctionnalité : Visualiseur de carte et génération de terrain en 3D
Nous avons un tout nouveau visualiseur interne de carte 3D dans QGIS ! Le visualiseur de carte 3D affiche les cartes 2D (rendues à partir des couches de projet) au-dessus du terrain. Par défaut le terrain est une surface plate, mais il est possible d'utiliser des couches raster avec un modèle numérique de terrain comme source pour les données de hauteur.

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- en glissant la souris avec le bouton du milieu pressé
- en pressant sur Shift et en glissant la souris avec le bouton gauche pressé
- en pressant sur Shift et en utilisant les touches haut/bas/gauche/droit

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Moteur de rendu 3D pour les couches
Dans la configuration par défaut, les couches sont rendues en images 2D drapées sur le terrain. Il est cependant possible d'avoir une meilleure utilisation de l'univers 3D en configurant des moteurs de rendu 3D pour certaines couches. Avec les moteurs de rendu 3D, les données peuvent être représentées en tant qu'objets 3D dans les visionneuses 3D - c'est actuellement possible avec les couches vecteurs (tout type de géométrie - point, ligne ou polygone). Une visualisation bien meilleure est ainsi possible, par exemple :
- des polygones représentant l'empreinte des bâtiments peuvent être extrudés (ayant même leur hauteur définie par des données) pour achever une impression de 3D
- des points représentant l'emplacement d'arbres peuvent être rendus avec des symboles 3D d'arbres (formes géométriques simples ou modèles 3D existants lus à partir de format de fichiers supportés)

Pour configurer les moteurs de rendu 3D, utilisez le dock de gadget de style de couche ou le dialogue de propriétés des couches vecteurs - il y a un nouvel onglet pour la configuration des moteurs de rendu 3D.

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Expressions
### Fonctionnalité : Nouvelles variables pour les expressions
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
Renvoie la localisation courante utilisée par QGIS. Par défaut c'est la localisation du système courant. Si l'utilisateur active une autre localisation dans les paramètres de QGIS alors cette dernière sera renvoyée.

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Nouvelles variables pour les expressions de paramétrage de carte
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Nouvelle fonction d'expression
**Expressions pour Atlas**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**Expressions pour agrégat** 
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

**Expressions pour tableau**

New group that contains expression functions for the creation and manipulation of arrays (also known as list data structures). The order of values within the array matters, in contrary to the \'map\' data structure, where the order of key-value pairs is irrelevant and values are identified by their keys.
- **array(value1, value2, ...)** : Returns an array containing all the values passed as parameter.
- **array_append(array, value)**: Returns an array with the given value added at the end.
- **array_cat(array1, array2, ...)**: Returns an array containing all the given arrays concatenated.
- **array_contains(array, value)**: Returns true if an array contains the given value.
- **array_distinct(array)**: Returns an array containing distinct values of the given array.
- **array_find(array, value)**: Returns the index (0 for the first one) of a value within an array. Returns -1 if the value is not found.
- **array_first(array)**: Returns the first value of an array.
- **array_get(array, index)**: Returns the Nth value (0 for the first one) of an array.
- **array_insert(array, pos, value)**: Returns an array with the given value added at the given position.
- **array_intersect(array1, array2)**: Returns true if any element of array1 exists in array2.
- **array_last(array)**: Returns the last value of an array.
- **array_length(array)**: Returns the number of elements of an array.
- **array_prepend(array, value)**: Returns an array with the given value added at the beginning.
- **array_remove_all(array, value)**: Returns an array with all the entries of the given value removed.
- **array_remove_at(array, pos)**: Returns an array with the given index removed.
- **array_reverse(array)**: Returns the given array with array values in reversed order.
- **array_slice(array, start_pos, end_pos)**: Returns a portion of the array. The slice is defined by the start_pos and end_pos arguments.
- **array_to_string(array, delimiter, empty_value)**: Concatenates array elements into a string separated by a delimiter using and optional string for empty values.
- **regexp_matches(string, regex, empty_value)**: Returns an array of all strings captured by capturing groups, in the order the groups themselves appear in the supplied regular expression against a string.
- **string_to_array(string, delimiter, empty_value)**: Splits string into an array using supplied delimiter and optional string for empty values.

**Expressions pour les couleurs**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**Expressions pour date et heure**
- **epoch(date)** : Renvoie l'intervalle en millisecondes entre l'époque UNIX et une date donnée.

**Expressions générales**
- **env(nom)** : Retourne le contenu d'une variable d'environnement en tant que chaîne de caractères. Si la variable n'est pas trouvée, NULL sera renvoyé.
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

**Expressions pour la géométrie**
- **extend(geometry, start_distance, end_distance)**: Extends linestrings by a specified amount at the start and end of the line
- **hausdorff_distance(geometry a, geometry b, densify_fraction)**: Returns the Hausdorff distance between two geometries. This is basically a measure of how similar or dissimilar 2 geometries are, with a lower distance indicating more similar geometries.
- **inclination(inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.
- **make_circle(center, radius, segment)**: Creates a circular, segmentized, polygon.
- **make_ellipse(center, semi_major_axis, semi_minor_axis, azimuth, segment)**: Creates an elliptical, segmentized, polygon.
- **make_regular_polygon(center, radius, number_sides, circle)**: Creates a regular polygon.
- **make_triangle()**: help still missing
- **minimal_circle(geometry, segment)**: Returns the minimal enclosing circle of a geometry. It represents the minimum circle that encloses all geometries within the set.
- **offset_curve(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by offsetting a linestring geometry to the side. Distances are in the Spatial Reference System of this geometry.
- **oriented_bbox(geom)**: Returns a geometry which represents the minimal oriented bounding box of an input geometry.
- **pole_of_inaccessibility(geometry, tolerance)**: Calculates the approximate pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance.
- **simplify(géométrie, tolérance)** : Simplifie une géométrie en supprimant des nœuds basé sur un seuil de distance (c'est-à-dire l'algorithme de Douglas Peucker). L'algorithme conserve les grands écarts dans les géométries et réduit le nombre de nœuds dans les segments presque droits.
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

**Propriété des couches**
- **crs_description** returns the CRS description of the layer.

**Expressions pour dictionnaire**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**Couches de carte**

Nouveau groupe contenant la liste des couches qui sont disponibles dans le projet courant. Renvoie l'identifiant interne des couches. Ils sont utilisés dans beaucoup de fonctions pour expressions qui se réfèrent aux couches.

**Expressions mathématiques**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**Opérateurs**
- **\~:** Performs a regular expression match on a string value.

**Expressions pour enregistrements et attributs**

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- **uuid()** : Génère un Identifiant universel unique (UUID) pour chaque rangée en utilisant la méthode QUuid::createUuid de Qt. Chaque UUID occupe 38 caractères.

**Relations**

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**Obsolète**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**Modifications**
- Modification de la fonction **substr()**
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- **strpos()** dépend maintenant d'une chaîne simple dans la chaîne de recherche
- **regexp_match()** now returns pos of a matching regular expression

Cette fonctionnalité a été développée par de nombreux développeurs
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
Ou une valeur par défaut pour l'attribut lors de la numérisation des entités :

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

La fonction accepte un seul argument, l'identifiant pour l'élément dans la composition, et renvoie un dictionnaire de nom de variable par valeur de cet élément. Cela vous permet de faire des choses telles qu'insérer du texte dans une étiquette à partir des propriétés d'un autre élément dans la composition, par ex.

Insérer l'échelle d'une carte dans une étiquette :

`map_get( item_variables( 'map'),'map_scale')`

Insérer la coordonnée x du centre d'une carte dans une étiquette :

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Documentation
### Fonctionnalité : amélioration des algorithmes de Processing
Les algorithmes de Processing ont été révisés et documentés. Un clic sur le bouton d'aide ouvrira le site web de QGIS et affichera la description de l'algorithme avec une documentation améliorée et des images.

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par la Proposition de subvention de QGIS

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## Symbologie
### Fonctionnalité : Visibilité des symboles de couche définie par les données
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : enregistrer et restaurer les palettes de couleurs utilisées pour les rendus en bande simple de pseudo-couleur.
Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Ajout de Points et Pouces pour les unités disponibles de symbole
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Nouveau gadget de bouton de palette de couleurs
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Le Gestionnaire de styles a été retravaillé et mis à jour
La gestion des styles a reçu une amélioration importante. Les améliorations comprennent :
- Un nouveau groupe "Marque-Pages" (favoris) a été ajouté, il est sélectionné par défaut dans la liste déroulante des symboles
- Maintenant, le mot-clé / "groupe intelligent" sélectionné dans la liste des symboles se maintient lorsque l'on change de couche (ainsi que d'une session à l'autre) 
- La liste de symboles met à jour la liste déroulante des balises / "groupe intelligent" lorsque les utilisateurs ajoutent / renomment / suppriment des catégories.
- Les utilisateurs peuvent directement mettre des balises, ainsi qu'ajouter aux favoris, les symboles tout en les enregistrant dans la base de données des styles.
- Pour simplifier la gestion des styles, les groupes ont été supprimés et entièrement remplacés par des balises
- Les balises ont été intégrées dans l'interface importation/exportation de l'utilisateur 

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Support pour la configuration des couleurs et de la transparence sur éléments multiples pour les rendus raster
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Affiche une jauge d'alpha dans le menu déroulant du bouton des couleurs
Permet de rapidement modifier l'alpha des couleurs

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Prise en charge des actions de la barre d'outils d'étirement raster pour le rendu pseudocolor
Cette fonctionnalité a été développée par Mathieu Pellerin
### Fonctionnalité : Support pour la transparence dans le moteur de rendu en palettes de couleurs
Dans QGIS 3.0, il est maintenant possible de changer la valeur de transparence pour des valeurs uniques pour le moteur de rendu en palettes de couleurs.

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Ajustement automatique des couleurs d'un raster lorsque le canevas est mis à jour
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité : Contrôle des marges du contenu des annotations
Permet de fixer les marges gauche/supérieure/inférieure/droite du contenu dans une annotation.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Les annotations peuvent être stylisées avec des styles de symboles pleins
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

Aussi, les effets de peinture et les paramètres de symboles définis par les données.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Moteur de rendu pour groupe de points
Nouveau moteur de rendu de symboles qui groupe et affiche les points proches les uns des autres en un symbole de marqueur unique. En option, une étiquette affiche le nombre d'entités qui ont été agglomérées dans le symbole.

De plus, quelques améliorations ont été faites sur le moteur de rendu de déplacement points, spécifiquement :
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- Les points individuels sont maintenant correctement affichés dans leur état de sélection propre
- Beaucoup de nettoyage de code et même de la documentation.

Pour les développeurs : QgsPointDisplacementRenderer a été séparé en une nouvelle classe de base virtuelle pure QgsPointDistanceRenderer qui s'occupe de la détection des groupes et du groupement des points. Le nouveau moteur de rendu pour groupe utilise cette classe de base pour éviter la duplication de code.

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann, Qtibia Engineering (Tudor Barascu), Karl-Magnus Jönsson, Geonesia (Nicolas Ponzo) et de nombreux supporteurs anonymes dont les contributions généreuses sont aussi très estimées ! 

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### Fonctionnalité : Nouveaux algorithmes pour la coloration de cartes dans QGIS 3.0
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Nyall Dawson
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Permet de désactiver temporairement toutes les couches de symboles
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Mise en style facile des raster à valeurs discrètes
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

Le calcul de la valeur unique est effectué dans un thread d'arrière-plan pour que l'interface utilisateur reste réactive pour les couches raster volumineuses (ou distantes). De plus, les utilisateurs peuvent ajouter manuellement de nouvelles classes individuelles selon leurs besoins et modifier la valeur de pixel associée pour toute classe existante. La suppression de plusieurs classes à la fois est également prise en charge, ainsi que la modification de la couleur, de la transparence et des étiquettes pour plusieurs classes à la fois.

Les palettes de couleurs peuvent être lues à partir d'un fichier. Les formats de table de couleurs ESRI clr/GDAL/GRASS sont supportés. Les palettes de couleurs peuvent être sauvées dans un fichier texte clr pour être partagées.

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Étiquetage
### Fonctionnalité : La taille des polices de caractères des étiquettes peut être spécifiée en mm/pixels
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : La barre d'outils de l'étiquetage personnalisé est maintenant toujours activée
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## Diagrammes
### Fonctionnalité : Propriétés définies par les données
Ajoute un support pour des propriétés définies par les données plus étoffées pour les diagrammes :
- Distance
- Priorité
- IndexZ
- EstObstacle
- Affiche
- AfficheToujours
- Angle départ diagramme

Cette fonctionnalité a été financée par le Programme de subvention de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Rendu
### Fonctionnalité : Support pour couche en direct
QGIS 3.0 supporte maintenant les couches en direct. Ces couches sont automatiquement rendues toutes les x secondes de façon claire et sans scintillement ; x étant une valeur que vous spécifiez. Les couches en direct sont utiles pour traquer des données qui changent continuellement, comme les flottes de véhicules, une volée d'oiseaux dont vous avez les données télémétriques et ainsi de suite.

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

Cette fonctionnalité a été développée par Kartoza et North Road
### Fonctionnalité : Déclenchement de la mise à jour d'une couche ou des actions de la couche à partir du signal NOTIFY de PostgreSQL
À la suite des effets de couches en direct, elle permet de déclencher des actions ou une mise à jour de la couche dans QGIS seulement lorsque la base de données demande à QGIS de faire quelque chose. Elle demande moins de ressources que la mise à jour à intervalle régulier, et vous pouvez même l'utiliser pour programmer une application chat avec QGIS :)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### Fonctionnalité : Le résultat du cache de l'étiquetage évite les retracés inutiles lors du rafraîchissement du canevas
Ce changement permet de créer une image cache des résultats de l'étiquetage après un rendu de carte. Si l'image cache peut être réutilisée pour le rendu suivant, elle le sera, évitant ainsi de retracer toutes les couches participant au problème de l'étiquetage en en donnant la solution. Essentiellement, cela veut dire que **les rafraîchissements du canevas entraînés par des modifications de couches NON-ÉTIQUETÉES sont bien plus rapides**. (Modifier une couche qui fait partie de la solution de l'étiquetage demande toujours le retracé complet de toutes les couches étiquetées)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Moteur de rendu pour grille de déplacement de points
Moteur de rendu pour grille de déplacement de points

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## Numérisation
### Fonctionnalité : Sélection d'un ensemble de sommets dans l'outil Nœud
Cette fonctionnalité permet de sélectionner un **ensemble de sommets** à partir d'une entité.

Elle peut être activée par **Shift+R** - puis il suffit de cliquer le point de départ et le point final dans l'entité - cela sélectionnera tous les sommets entre ces deux points.

La sélection d'ensemble peut être annulée à tout moment avec un clic droit ou avec la touche Esc.

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Fonctionnalité : Ajout de l'option pour une valeur Z par défaut
Création de Géopackages/Shapefiles: Maintenant avec l'option d'avoir des valeurs Z

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Lisovenko / Paul Blottiere
### Fonctionnalité : Déplacer une entité bénéficie maintenant de la Numérisation avancée
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

Cette fonctionnalité a été développée par Denis Rouzaud
### Fonctionnalité : Ajout de la fonctionnalité copier/déplacer une entité à l'outil de carte d'entité
Cela permet de dupliquer et de déplacer une entité d'un seul coup à partir de l'entité sélectionnée

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Denis Rouzaud
### Fonctionnalité : Tracé avec décalage
Vous pouvez maintenant utiliser l'outil de numérisation par tracé avec un décalage comme montré dans l'image.

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### Fonctionnalité : Réorganisation de l'outil de Sommet
L'outil de Nœud (maintenant appelé l'outil de Sommet) a été totalement réorganisé pour le rendre plus flexible. Quelques unes des modifications les plus importantes sont :
1. Au lieu de forcer l'utilisateur à sélectionner dans un premier temps une entité puis, dans un second temps, à éditer ses sommets, l'outil est maintenant capable de travailler avec plusieurs entités en même temps. Il est donc facile de sélectionner des sommets à partir d'entités différentes et de les déplacer ou de les effacer en même temps. Si on a besoin de contraindre la sélection des sommets à une ou plusieurs entités spécifiques, il est possible de d'abord les sélectionner avec l'outil de sélection - dans ce cas, l'outil de sommet ne fonctionnera que sur les entités sélectionnées.
2. Au lieu de ne travailler que sur la couche couramment sélectionnée l'outil est maintenant capable de travailler en même temps sur toutes les couches en édition. Déplacer des entités qui font parties d'un ensemble logique mais qui sont réparties sur différentes couches est maintenant bien plus facile. Cependant, la couche courante est respectée s'il y a plusieurs choix lorsque les sommets sont sélectionnés.
3. Les entités et leurs sommets sont mis en valeur lorsque l'utilisateur déplace la souris au-dessus d'eux, fournissant un meilleur retour visuel.
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. le placement des nœuds est plus précis (car il n'y a plus besoin d'appliquer une force permanente sur la souris)
6. on ne peut pas déplacer les nœuds par inadvertance
7. il est possible d'annuler l'opération
8. elle permet de se déplacer sur la carte en pressant la barre d'espace tout en déplaçant le nœud

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Outil de Sommet : ajout de sommets avec le marqueur du point du milieu
L'outil de sommet amélioré affiche maintenant des marqueurs supplémentaires au niveau du point au milieu des segments de ligne des entités. Un clic sur un tel marqueur ajoute un nouveau sommet. La méthode existante d'ajouter un sommet par clic-double a été conservée.

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Outil de Sommet : prolongement de ligne
Le déplacement de la souris vers le premier ou le dernier sommet, lors de l'édition des géométries de type ligne avec l'outil de sommet, entraîne l'affichage d'un marqueur supplémentaire tout prés du sommet terminal. Un clic sur le marqueur ajoute un sommet à la géométrie à sa place.

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Outil de Sommet : support pour le panneau de numérisation avancée
Le panneau de numérisation avancée fonctionne maintenant avec l'outil de sommet - il est possible de taper les coordonnées de nouveaux sommets ou de sommets existants dans le panneau comme cela est possible dans tout autre outil de numérisation de carte.

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Gestion des données
### Fonctionnalité : Recentrage sur l'entité courante, dans la table d'attributs
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

Cette fonctionnalité a été développée par Marco Hugentobler
### Fonctionnalité : Carte de l'emprise du SCR dans les propriétés du projet
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### Fonctionnalité : Support pour stockage auxiliaire
Un nouvel onglet est disponible dans les propriétés des couches de vecteurs pour gérer le stockage auxiliaire :

Une nouvelle action **Enregistre les données dans le projet** est disponible dans le menu des données définies fournissant une manière facile de gérer les données auxiliaires pour une propriété :

Les données auxiliaires sont enregistrées dans une base de données sqlite et gérées avec le fournisseur de données OGR (au lieu du fournisseur spatialite) pour que le ficher de base de données soit aussi compact que possible. Ce fichier de base de données (avec l'extension *.qgd*) est soit sauvé à coté du fichier de projet soit intégré dans le nouveau format *.qgz*.

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### Fonctionnalité : Réorganisation des métadonnées
Le système de métadonnées dans QGIS a été réorganisé. Pour QGIS 3.0 nous introduisons notre schéma personnel et formalisé de métadonnées qui est séparé du format de fichier du projet QGIS. Nous introduisons de nouvelles fonctionnalités dans l'API pour lire et écrire les métadonnées des couches. Nous avons séparé l'affichage des métadonnées de leur édition et avons ajouté un nouvel outil pour l'édition des métadonnées. Les métadonnées sont actuellement sauvées dans le fichier du projet. Elles peuvent aussi être sauvées dans un fichier XML accompagnant les couches basées sur des fichiers ou dans une base de données sqlite locale pour les couches non-locales (par ex. PostGIS).

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### Fonctionnalité : Boîte de dialogue unifiée pour la gestion des sources de données
Une boîte de dialogue unique et unifiée pour gérer les sources de données et charger les couches.

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

Cette fonctionnalité a été financée par Boundless

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalité : Suppression de l'outil de chargement OSM
Nous avons supprimé l'outil de chargement OSM fournit avec les versions 2.x de QGIS. Nous vous encourageons plutôt à utiliser l'extension QuickOSM qui a été portée sur QGIS 3.0.
## Formulaires et widgets
### Fonctionnalité : Permet le contrôle des étiquettes pour les widgets individuels d'édition
Dans le mode de conception par glisser-déposer, un clic-double sur un élément permettra de contrôler si l'étiquette doit être affichée individuellement pour chaque élément.

Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Permet la configuration des boutons de lien/relâche d'entité dans le gadget d'édition de relation
Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Visibilité conditionnelle des onglets et des boîtes de groupe
Elle ajoute une nouvelle option de configuration pour afficher ou masquer conditionnellement des onglets et des boîtes de groupe dans les formes du mode de conception par glisser-déposer. La configuration se fait par un clic-double dans l'arbre de conception de l'interface de configuration des champs. Une expression peut être saisie pour contrôler la visibilité. L'expression sera ré-évaluée chaque fois que les valeurs du formulaire sont modifiées et l'onglet ou la boîte de groupe sera affiché/masqué de manière appropriée.

Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Les gadgets par défaut pour l'édition sont plus intelligents et peuvent être sélectionnés par les extensions
Les gadgets peuvent maintenant fournir un score sur leur capacité de traiter le type d'un champ. Cela conduit à des gadgets par défaut bien meilleurs.

De plus, des extensions peuvent être ajoutées pour choisir le type d'un gadget en fonction d'informations externes. L'un d'eux utilisent une table dans PostgreSQL qui permet de spécifier le type de gadget et la configuration à utiliser pour chaque champ.

Sélection automatique du gadget RelationReference pour les clés étrangères.

Cette fonctionnalité a été développée par Patrick Valsecchi
### Fonctionnalité : Les contraintes de champ peuvent être imposées ou non
Les contraintes non-imposées affichent simplement un avertissement à l'utilisateur, mais ne permettent pas d'empêcher la modification de l'entité. Les contraintes imposées n'autorisent pas l'utilisateur à faire des modifications non conforme de l'entité. Nous avons donc maintenant des avertissements ! Toute contrainte détectée par un fournisseur est toujours imposée.

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Ajout d'actions portant sur la couche
Dans la table d'attributs, il y a un nouveau bouton pour déclencher des actions qui ne sont pas basées sur les entités individuelles mais sur la couche en entier. Elles effectueront normalement des actions basées sur toutes les entités ou la sélection.

Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Affiche les valeurs du champ dans la complétion automatique dans le mode de filtre de forme
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Ajout de raccourcis pour zoom sur entités et entités éclairs dans le dialogue de sélection par formulaire
Permet une navigation et une identification très rapides des entités qui correspondent au critère du formulaire

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Ajout de entre/pas entre aux champs numériques dans la sélection par forme
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Légende des couches
### Fonctionnalité : Action pour masquer les couches désélectionnées
Vous permet de masquer rapidement les couches désélectionnées. Cela est particulièrement utile pour de gros projets lorsque l'on veut rapidement masquer toutes les couches à l'exception de quelques unes

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Modification de l'ergonomie de la visibilité des couches dans des groupes
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- L'état de semi-sélection d'un groupe n'existe plus
- **Ctrl-clic** sur un groupe désélectionné le sélectionnera ainsi que tous ses descendants.
- Ctrl-Clic sur une couche désélectionnée la sélectionnera ainsi que tous ses parents.
- Ctrl-clic sur un groupe sélectionné le désélectionnera et désélectionnera tous ses descendants.
- Ctrl-clic sur une couche sélectionnée la désélectionnera et désélectionnera tous ses parents.
- Ces actions sont disponibles dans les éléments du menu contextuel du panneau de couches
- Les couches masquées soit parce qu’elles sont désélectionnées ou qu'un de leurs parent est désélectionnée sont affichées en gris.

Cette fonctionnalité a été développée par Even Rouault
## Composeur de Cartes
### Fonctionnalité : Contrôle de l'affichage des lignes horizontales et verticales de la grille des tables de Composeur
Il est maintenant possible de contrôler indépendamment le rendu des lignes horizontales et verticales des éléments des tables de Composeur. Cette nouvelle flexibilité augmente les possibilités de mise en style de cet élément directement dans QGIS.

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Dépose un qpt dans QGIS pour créer un nouveau Composeur à partir d'un gabarit
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Permet la personnalisation de l'espacement des lignes pour les étiquettes dans la légende de Composeur
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Permet le choix du SCR pour les éléments de la carte
Ceci permet au SCR des éléments d'une carte d'être différent de celui du canevas/projet. Cela permet aussi d'avoir des éléments de carte avec des SCR différents, par ex. une carte d'aperçu peut avoir un SCR différent de la carte principale.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Maintenir la touche Shift lors du tracé d'une ligne/polygone contraint les angles de ligne.
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Plus de propriétés définies par les données
Élément **cadre** et **couleurs arrière-plan**, **couleurs et épaisseur de la bordure d'un svg pour les éléments image de Composeur** (très utile lorsque l'image représente une flèche d'orientation), **titres et nombre de colonnes de la légende**, **couleurs et épaisseur des lignes de la barre d'échelle** peuvent être définis par les données

Cette fonctionnalité a été financée par le Programme de subvention de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Réorganisation du Composeur de cartes
C'est une réorganisation majeure de la manière dont les compositions sont gérées dans le code de QGIS.

Les points saillants sont :
- Une nouvelle classe QgsLayoutManager qui est utilisée pour le stockage et la sérialisation/dé-sérialisation des compositions. Un QgsLayoutManager est attaché à QgsProject. Cela permet au cœur du code d'accéder aux compositions attachées au projet. Toutes les manipulations des compositions ont été transférées de l'app au cœur, permettant au serveur (et aux autres projets qui ne sont pas basés sur app. QField/roam?) d'accéder plus facilement aux compositions du projet sans se fier sur l'analyse fragile du xml.
- Les fenêtres de Composeur sont créées à la demande et détruites à la fermeture. Cela évite la demande lourde de créer toutes les fenêtres et tous les gadgets de tous les éléments du Composeur lors le l'ouverture de projets. **C'est la raison pour laquelle les projets ayant des compositions s'ouvraient très lentement par le passé**. Maintenant, les fenêtres de Composeur ne sont créées qu'à l'ouverture de la fenêtre et sont détruites dès que la fenêtre est fermée. Les gadgets de configuration des éléments de Composeur ne sont aussi créés qu'à la demande (lorsque l'élément est sélectionné) au lieu de pré-créé tous les gadgets.
- Un avantage secondaire de détruite les fenêtres de Composeur à leur fermeture est que **nous ne souffrons plus d'un bogue de Qt** qui bloquait l'utilisation des docks flottants dans les fenêtres de Composeur. Vous pouvez maintenant flotter les panneaux élément/composition/etc ! Bien mieux pour travailler plein écran avec les compositions dans des configurations multi-écrans.
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- Beaucoup de nettoyage de code et de suppressions.

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par le groupe Suisse des utilisateurs de QGIS et beaucoup d'autres personnes.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Outils d'analyse
### Fonctionnalité : Compte des valeurs uniques d'un raster pour traitement
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## Traitement
### Fonctionnalité : Nouvel algorithme pour le décalage des lignes
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Nouvel algorithme pour créer des zones tampons unilatérales
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Ajout du choix de la méthode de simplification à simplification
Ce changement permet aux utilisateurs de choisir la méthode à utiliser lors de l'usage de l'algorithme de simplification des géométries, avec le choix entre l'algorithme existant basé sur la distance (Douglas Peucker), l'algorithme basé sur la surface (Visvalingam) et aligner sur la grille.

Visvaligam, en particulier, génère des simplifications qui sont cartographiquement plus plaisantes comparées à celles des méthodes standards basées sur la distance.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : prise en charge des types de géométrie de sortie dans les modèles
Les entrées de l'algorithme enfant du modèle sont désormais filtrées uniquement sur celles qui génèrent des types de géométrie applicables pour l'entrée d'un autre algorithme enfant

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Seuil d'angle pour un algorithme fluide
Ajouter une option à QgsGeometry::lisser pour ne pas lisser les segments plus courts qu'un certain seuil ou les angles vifs avec un angle dépassant un seuil

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Meilleure prise en charge des dimensions Z/M et des géométries courbes
Fonctionnalité : Meilleure prise en charge des dimensions Z/M et des géométries courbes
### Fonctionnalité : Algorithmes d'analyse raster ajoutés au traitement
Les algorithmes suivants ont été ajoutés au traitement à partir du plug-in Raster Analysis :
- Exposition
- Pente
- Rugosité
- Ombrage
- Relief

Ces algorithmes peuvent maintenant être utilisés dans des scripts, des modèles et pour le traitement par lot.

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Nouvel algorithme pour extraire des nœuds spécifiques
Cet algorithme vous permet d'extraire des nœuds spécifiques des géométries. Par exemple vous pouvez extraire le premier ou le dernier nœud d'une géométrie.

Cet algorithme requiert la liste des indices des nœuds à extraire séparés par des virgules, par ex. 0 = premier nœud, 1 =  deuxième nœud, etc. Des indices négatifs peuvent être utilisés pour extraire les nœuds depuis la fin de la géométrie. Par ex. -1 = dernier nœud, -2 = avant-dernier nœud, etc.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Exposez les statistiques zonales à partir du plug-in de statistiques zonales dans la boîte à outils
Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité: Ajoute un algorithme de requête SQL sur une base de données spatialite.
Cette fonctionnalité a été développée par Mathieu Pellerin
### Fonctionnalité : Nouvel algorithme pour prolonger des lignes
Permet d'étendre des géométries de lignes d'une distance déterminée en début et et fin de ligne

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Nouvel algorithme d'extraction à l'aide d'une expression
Filtre une couche en entrée à l'aide d'une expression

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Algorithme d'import dans une base de données SpatiaLite
Cette fonctionnalité a été développée par Mathieu Pellerin
### Fonctionnalité: Algorithmes d'interpolation
Intègre les algorithmes d'interpolation IDW et TIN de l'extension Interpolation dans la Boîte à outils de Traitements.

L'extension Interpolation a par conséquent été supprimée.

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Nouvel algorithme pour calculer la géométrie par expression
Cet algorithme met à jour les géométries existantes (ou crée de nouvelles géométries) pour les entités en entrée à l'aide d'une expression QGIS. Cela permet des modifications géométriques complexes qui peuvent utiliser toute la flexibilité du moteur d'expression QGIS pour manipuler et créer des géométries pour les entités de sortie.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Aligner les géométries sur l'algorithme de calque
Porter le plug-in Geometry Snapper vers le traitement

L'algorithme de géométries d'accrochage permet l'accrochage à d'autres types de calques, prend en charge les calques de points/lignes

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Nouveau type de saisie pour les expressions
Cela ajoute un nouveau type d'entrée pour les entrées d'expression. Les entrées d'expression peuvent être liées à une couche parente afin que le générateur affiche les champs et les variables de couche appropriés.

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : SplitWithLines
Renommer l'algorithme SplitLinesWithLines en SplitWithLines Accepter également le polygone en entrée Utiliser uniquement les lignes sélectionnées avec lesquelles fractionner (si le traitement est défini pour utiliser uniquement la sélection) Émettre un message de journal si vous essayez de fractionner plusieurs géométries Mettre à jour l'aide

Cette fonctionnalité a été développée par Bernhard Ströbl
### Fonctionnalité : Algorithme du pôle d'inaccessibilité
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : l'extraction par attribut peut extraire des valeurs nulles/non nulles
Ajoute la prise en charge du filtrage lorsqu'une valeur d'attribut est nulle ou non nulle

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Créer un algorithme d'index d'attributs
Permet la création d'un index sur un attribut dans une couche pour un filtrage plus rapide basé sur les attributs

La prise en charge dépend du fournisseur de données sous-jacent pour la couche

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
Supprime simplement toutes les géométries d'une couche d'entrée et renvoie les entités avec des attributs uniquement

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

Le fait d'avoir un seul algorithme unifié permet des modèles plus flexibles où un type de champ peut ne pas être connu à l'avance.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Port du plugin carte de chaleur vers l'algorithme de géo-traitements
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Nouvel algorithme pour orthogonaliser les géométries
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Algorithmes d'analyse de réseau
ajouter des algorithmes du chemin le plus court et de la zone de service aux géo-traitements 

permettent également de calculer le chemin le plus court d'un point à tous les points d'un calque, ou de tous les points d'un calque à un point final. Et créer des zones de desserte pour tous les points d'une couche.

Le plugin Roadgraph a donc été supprimé.

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité: Modèles d'exportation de géo-traitements aux formats PDF/SVG
Outre l'exportation de modèles de traitement sous forme d'images bitmap, il est désormais possible d'exporter des modèles de traitement sous forme de fichiers PDF et SVG indépendants de la résolution. Cela permet une exportation haute résolution de modèles qui peuvent être intégrés dans des articles et des livres en cours de publication.

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Nouvel algorithme pour tronquer les tables
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
Cette fonctionnalité a été développée par Victor Olaya
### Fonctionnalité : Algorithme pour corriger les géométries invalides à l'aide de l'implémentation native de makeValid()
Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Ajouter une recherche à la boîte de dialogue Obtenir des scripts et des modèles
Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Algorithme centroïde générique
Algorithme de centroïde retravaillé qui gère les couches non polygonales

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Algorithme de nœuds d'extraction amélioré
L'algorithme d'extraction de nœuds enregistre désormais l'index de nœud, la distance le long de la ligne et l'angle au nœud

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : nouvel algorithme de translation (déplacement) des points
Permet de décaler les géométries d'un déplacement x/y

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : fenêtre de modélisation de traitement améliorée
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : nouvel algorithme de rapport de valeurs uniques raster
Un nouvel algorithme a été ajouté au traitement qui renvoie le nombre et la surface de chaque valeur unique dans une couche raster donnée.

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Suppression de TauDEM de la base du module de Traitements
Nous avons retiré le fournisseur d'algorithmes TauDEM du module de Traitements.

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### Fonctionnalité : Télécharger un fichier à partir de Traitement
Téléchargez un fichier à partir de Processing. Interroger une API distante pour obtenir un geojson

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Fonctionnalité : points optimisés le long de l'algorithme de géométrie
Prend également en charge les géométries de polygones, gère les géométries nulles et enregistre l'angle de ligne d'origine avec la distance pour chaque point.

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Trier par algorithme d'expression
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Options de l'application et du projet
### Fonctionnalité : Nouveau format de fichier de projet zippé
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Fonctionnalité: Gestion de profils utilisateurs
Tous les paramètres/plugins utilisateur, etc. sont désormais chargés à partir de l'emplacement des données de l'application pour chaque plate-forme et non plus .qgis3/2. Les paramètres et les plugins de chaque profil sont désormais isolés les uns des autres.

Cela permet différentes configurations d'exécution en fonction des besoins de l'utilisateur, par exemple test, prod, démo, etc.

Le menu Profil permet de basculer entre les profils ou d'en créer de nouveaux.

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## Explorateur
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
Facilite par ex. stocker vos couches temporaires dans PostGIS

Cette fonctionnalité a été développée par Martin Dobias
### Fonctionnalité : Suppression de l'application autonome du navigateur QGIS
Nous avons supprimé l'application autonome QGIS Browser fournie avec QGIS 2.x. Cette application était peu utilisée par les utilisateurs et représentait une surcharge de maintenance que nous ne souhaitons pas continuer dans la base de code 3.0.
## Fournisseurs de données
### Feature: New unified \'add layer\' dialog
Vous pouvez maintenant utiliser une seule boîte de dialogue pour ajouter une grande variété de formats de données à QGIS.

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalité: GeoPackage
- enregistrer sous use pkg par défaut
- enregistrer sous utilise pkg par défaut
- créer une nouvelle couche en utilisant pkg par défaut
- navigateur glisser-déposer importer des couches

Cette fonctionnalité a été développée par Alessandro Pasotti
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
Cette fonctionnalité a été développée par Nyall Dawson
### Fonctionnalité : Prise en charge des géométries Z/M dans gpkg, spatialite et fournisseur de couche de mémoire
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

Cette fonctionnalité a été développée par Matthieu Pellerin, Alexander Bury, Paul Blottiere
### Fonctionnalité : Gestion des contraintes uniques et non nulles
Détection automatique des contraintes uniques et non nulles côté fournisseur implémentées pour le fournisseur postgres, spatialite, ogr

Les contraintes uniques sont appliquées sous forme d'attribut

Les contraintes uniques sont appliquées sous forme d'attribut

Cette fonctionnalité a été financée par OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité : Intégration de GeoNode
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

Si l'instance GeoNode utilise le backend de QGIS Server plutôt qu'un GeoServer, vous pouvez copier et coller des styles depuis le serveur et les appliquer à votre couche locale afin que votre couche WFS s'affiche exactement comme sur le serveur (comme indiqué dans l'animation GIF ici).

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### Fonctionnalité : Détecter les valeurs littérales par défaut pour le fournisseur spatialite
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Créer un support d'index d'attribut pour le fournisseur spatialite
Permet la création d'index d'attributs pour les couches spatialites

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Fonctionnalité: Gestion des tableaux
Pris en charge par postgres, spatialite

Cette fonctionnalité a été développée par Patrick Valsecchi
### Fonctionnalité : Prise en charge de HStore dans le fournisseur de données PostGIS
### Fonctionnalité: Détection des relations pour PostgresQL
Cette fonctionnalité a été développée par Patrick Valsecchi
### Fonctionnalité : dépendances de données entre les couches
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

Cette fonctionnalité a été développée par Hugo Mercier
### Fonctionnalité : exportation dxf : prise en charge de la reprojection
Cette fonctionnalité a été développée par Juergen E. Fischer
### Fonctionnalité : Charger/enregistrer le style dans la base de données pour GPKG et Spatialite
Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité : Amélioration de la gestion des valeurs par défaut
Améliorez la gestion des valeurs par défaut (incluant les clauses par défaut du fournisseur, les valeurs littérales par défaut et les valeurs par défaut des expressions QGIS) et gérez automatiquement les contraintes de valeur unique sur les couches

Tous les champs avec des contraintes de valeur unique auront la garantie d'avoir une valeur qui est unique au champ.

Cela signifie également qu'après certaines opérations d'édition (par exemple, copier-coller, fractionner des entités, etc.), les attributs seront désormais définis sur leur valeur par défaut, le cas échéant.

Cette fonctionnalité a été financée par le Canton de Zug et le projet QGEP

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## QGIS Server
### Fonctionnalité : Refonte de QGIS Server
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

Il y a un an, un petit troll de Suisse a sonné une cloche sur le fort besoin de base de code de serveur d'amour requise. En effet, l'API était verrouillée par certaines anciennes méthodes du serveur QGIS. En bref, le serveur QGIS réparait le fichier de projet qgs à sa manière et créait des dépendances à une partie de QGIS que nous devions supprimer.

Comme l'externalisation de la base de code du serveur n'était pas une option, nous avons donc dû la refactoriser. Les parties impliquées ont décidé de s'engager dans un sprint de code dans la ville de Lyon, en France, dédié au partage de leur vision, à la planification du travail et enfin à la réalisation de tout ce qui suit :

Refactoring de niveau supérieur

Tous les services (WMS GetMap, WFS GetFeature, GetLegendGraphics, WCS, GetPrint etc.) ont été réécrits. Certains comme WMS ont été entièrement réécrits. Bravo aux devs !

Nouvelles fonctionnalités
- Rendu multi-thread comme dans le bureau
- Rendu multi-thread comme dans le bureau
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- Liaisons Python complètes pour l'API du serveur
- Services de serveur en tant que plugins comme les fournisseurs

Tâches profondes, complexes et peu gratifiantes
- Supprimer tous les appels singleton
- Coupez toutes les dépendances à l'ancien analyseur de fichiers de projet QGIS
- Coupez toutes les dépendances à l'ancien analyseur de fichiers de projet QGIS

Tâches d'infrastructure
- Créez une plate-forme de conformité OGC et intégrez-la à une plate-forme d'intégration continue. Les rapports de conformité sont maintenant poussés vers tests.qgis.org
- Add unit tests \... and again more unit tests
- Stresser le serveur QGIS contre les failles de sécurité (injections SQL et autres attaques malveillantes)
- Commencez à profiler et à comparer les performances. Ce travail a encore besoin d'amour - et de financement - pour être réalisé

Une présentation a été donnée sur le sujet en juillet au FOSS4G-EU.

Cette fonctionnalité a été financée par les donateurs de QGIS.ORG
### Fonctionnalité : Possibilité de segmenter les informations de géométrie d'une entité sur le serveur
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## Extensions
### Fonctionnalité : Supprimer le statut de confiance du gestionnaire de plugins
<https://github.com/qgis/QGIS/pull/5272>
### Fonctionnalité : édition hors ligne : ajouter un indicateur pour copier uniquement les entités sélectionnées
Cela étend les possibilités d'édition hors ligne pour ne travailler que sur un sous-ensemble de grandes couches

Cette fonctionnalité a été financée par DB Fahrwegdienste GmbH

Cette fonctionnalité a été développée par Matthias Kuhn
### Fonctionnalité : Intégration de GDALTools au module de Traitements
L'extension GDALTools a été supprimée.

Toutes les fonctions précédemment disponibles via le plugin GDALTools ont été déplacées vers le framework de traitement QGIS, permettant d'utiliser ces outils dans des scripts, des modèles et de les exécuter dans des processus par lots. De plus, nous avons mis à jour les algorithmes avec de nouveaux paramètres, introduits dans les dernières versions de GDAL et amélioré l'interface utilisateur/UX globale en exposant certains paramètres avancés tels que les options de création, les paramètres de valeur NODATA, etc.

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : permet d'installer des extensions à partir de fichiers ZIP locaux
Il est maintenant plus facile d'installer des extensions manuellement sans avoir à les dézipper soi-même dans le répertoire utilisateur.

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Les extensions peuvent fournir une aide personnalisée dans la fenêtre Expression
Les extensions qui fournissent des expressions peuvent ajouter une aide personnalisée avec des chaînes HTML.

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programmation
### Fonctionnalité : Mises à jour de la classe géométrie
Il y a eu une mise à jour majeure des classes géométrie dans QGIS. Les vieilles classes ont été renommées (voir table ci-dessous). Les nouvelles classes géométrie préserveront correctement les attributs Z et M si présents.

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

Cela fournit finalement un état consistant de la nomination dans l'API géométrie
### Changement de nom
| QGIS 2 | QGIS 3 |
| --- | --- |
| QgsPolygon | QgsPolygonXY |
| QgsMultiPoint | QgsMultiPointXY |
| QgsMultiPolyline | QgsMultiPolylineXY |
| QgsMultiPolygon | QgsMultiPolygonXY |
| QgsPolygonV2 | QgsPolygon |
| QgsMultiPointV2 | QgsMultiPoint |
| QgsMultiPolylineV2 | QgsMultiPolyline |
| QgsMultiPolygonV2 | QgsMultiPolygon |

See also <https://github.com/qgis/QGIS/pull/5491>

Cette fonctionnalité a été développée par Matthias, Nyall et d'autres
### Fonctionnalité : Gestionnaire des tâches
Introduit un cadre pour la création de tâches en arrière-plan, avec lesquelles interagissent via un gestionnaire centralisé

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

Ajouter une méthode python simple QgsTask.fromFunction pour la création de tâches à partir d'une fonction sans avoir à créer une sous-classe QgsTask

Support pour des tâches dépendantes

L'annulation d'une tâche dont d'autres en dépendent entraîne l'annulation de toutes ces autres tâches.

Ajouter la gestion des couches dépendantes au gestionnaire de tâches

Si une tâche a des canapés dépendants qui sont sur le point d'être supprimées, la tâche sera automatiquement annulée

QgsTasks peut avoir des sous-tâches

Désormais, une QgsTask peut avoir une sous-tâche QgsTasks définie en appelant QgsTask::addSubTask. Les sous-tâches peuvent avoir leur propre ensemble de tâches dépendantes.

Les sous-tâches ne sont pas visibles pour les utilisateurs, et les utilisateurs ne voient que la progression globale et l'état de la tâche parente.

Cela permet la création de tâches qui sont elles-mêmes construites à partir de nombreuses tâches de composants plus petites. Le gestionnaire de tâches gérera toujours le lancement et la planification des sous-tâches, par exemple, les sous-tâches peuvent s'exécuter en parallèle (si leurs dépendances le permettent).

Les sous-tâches peuvent elles-mêmes avoir des sous-tâches.

Cette modification est faite pour permettre aux concepts d'algorithmes et d'algorithmes de modélisation de Processing d'être traduits directement dans l'architecture du gérant des tâches.

Cette fonctionnalité a été financée par le Programme de subvention de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
Les implémentations de QgsDataItem peuvent fournir hasDragEnabled(), mimeUri() et l'implémentation QgsCustomDropHandler pour gérer la dépose d'éléments personnalisés.

Cette fonctionnalité a été développée par Martin Dobias

{{<content-end >}}
