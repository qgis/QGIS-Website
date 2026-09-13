---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Release date: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Soutiens pour QGIS version 3.2
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## Général
### Fonctionnalité : .qgz est maintenant le nouveau format par défaut pour un projet compressé
Le format QGZ a été introduit en format optionnel dans la version 3.0. Faire de ce format celui par défaut va grandement faciliter le chemin vers un conteneur capable d'intégrer des ressources telles que du SVG, des données hors lignes en GPKG, des palettes de couleurs, des extensions ou des scripts.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Fonctionnalité : Filtrage sur les valeurs de champs dans le constructeur de requête
Lorsque vous créez un nouveau filtre basé sur une expression dans le constructeur de requêtes, vous pouvez maintenant filtrer l'aperçu des valeurs de champs.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Fonctionnalité : Carte en plein écran avec la combinaison de touches Ctrl+Shift+Tab
En plus de Ctrl-Tab, vous pouvez maintenant faire Ctrl-Shift-Tab qui vous montrera la carte et uniquement la carte, sans barre d'outils ou bouton (et même sans le titre de la fenêtre en combinaison avec F11). C'est très utile pour présenter une carte en plein écran sur vidéo-projecteur ou grand écran, le zoom et le déplacement sur la carte sont toujours possible dans ce mode. (basé sur le travail de Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Richard Duivenvoorde
## Outils cartographiques
### Fonctionnalité : Outil de simplification peut maintenant lisser des entités
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Outil Identifier les entités avec des options supplémentaires
Grâce à de nouvelles améliorations, l'utilisateur peut maintenant utiliser des outils similaires à ceux de Sélection pour identifier de multiples entités.

Cette fonctionnalité a été financée par Leicestershire County Council et East Hampshire District Council

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Fonctionnalité : Les thèmes de cartes enregistrent maintenant l'état étendu ou réduit des couches.
Chaque thème de carte enregistrera aussi quelles couches, groupes de couches, et légendes sont développées, ainsi quand un thème de carte est sélectionné, l'état développé/replié s'appliquera dans l'arborescence des couches.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
Un nouveau visualisateur de carte peut être paramétré pour zoomer automatiquement sur la sélection. Comme présenté dans l'exemple, cela peut être utilisé en combinaison avec différents thèmes de carte.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Fonctionnalité : Choix de la méthode de simplification pour l'outil de simplification
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Ajout du raccourci "zoom sur l'entité" pour les formulaires
Un nouveau bouton "zoom sur la sélection" apparait dans le sous-formulaire d'attribut d'entité si un ou plusieurs enregistrements sont sélectionnés dans la table des entités en relation. Le bouton permet de zoomer sur tous les éléments qui ont été séléctionnés dans cette table.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité : Aires / longueurs / périmètres cartésiens dans les résultats d'identification
Dans QGIS 3.2, nous affichons maintenant les aires, longueurs et périmètres basés à la fois sur l'ellipsoïde et cartésiens dans le panneau des résultats de l'identification. Voir les deux mesures distinctes aide l'utilisateur à mieux comprendre les problèmes potentiels liés à de mauvais choix de projection ou d'ellipsoïde sur les calculs d'aires ou de distances.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Expressions
### Fonctionnalité : Nouvelle fonction d'expression
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Nouvelles variables :
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Cette fonctionnalité a été développée par Mathieu Pellerin et Nyall Dawson
### Fonctionnalité: Amélioration de l'aide du constructeur d'expression
Le constructeur d'expression permet maintenant de construire plus facilement des expressions QGIS !
- Il affiche la description pour chaque type de valeur dans une expresion et également l'intervale des valeurs attendues
- Le Ctrl+clic sur le nom d'une fonction dans le constructeur ouvre automatiquement l'aide sur cette fonction
- Il affiche également des indices sur la partie de l'expression qui contient des erreurs
- Il affiche la liste complête des messages d'erreur obtenu après avoir analysé l'expression

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Interface utilisateur
### Fonctionnalité : Panneau couches : Un indicateur est ajouté pour les couches ayant un filtre actif.
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

Cela ajoute un mini-système pour afficher des icones supplémentaire pour les couches et les groupes dans le panneau couches. Un texte d'information peut être associé à l'icone pour donner des informations supplémentaires. Lorsque l'utilisateur clique sur l'icone des actions personalisées peuvent être définies. L'idée est que cet indicateur puisse être utilisé dans le futur pour signaler différents types d'informations, par exemple :
- couche mappée avec géométrie invalide
- couche mappée avec une exception de reprojection "à la volée"
- couche mappée avec une source de donnée manquante
- couche mappée avec SCR invalide

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Fonctionnalité : Les préfixes du localisateur peuvent être personalisés
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Feature: Opening of vector and raster stored on HTTP(S), FTP, or cloud services
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Quick calculator in locator search bar
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Shortcuts for toggling panels
raccourci Ctrl+{no}

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Feature: Bookmark searching in locator
Allows search for spatial bookmarks. Double clicking a search result will zoom to the bookmark.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Cette fonctionnalité a été développée par Klavs Pihlkjær
### Feature: Close and Revert Project actions
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Nathan Woodrow et Nyall Dawson
### Fonctionnalité : Indicateur de modifications non sauvegardées dans la barre de titre
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Configurable map tips delay
Cette fonctionnalité a été développée par jdugge
### Fonctionnalités : Déplacer une couche ou un groupe en haut du panneau Couches
Déplacer la ou les couches ou groupes sélectionnés en haut du panneau Couches.

Cette fonctionnalité a été développée par Mie Winstrup
### Fonctionnalité : Bouton pour copier les résultats du panneau de statiques dans le presse-papier
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalités : Pages de paramétrage des recherches, options et propriétés du projet depuis le localisateur
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Cette fonctionnalité a été développée par Klavs Pihlkjær
### Feature: Indicators for embedded layers and groups
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Symbologie
### Fonctionnalité : Jolies couleurs pour les nouvelles couches
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Rendu
### Feature: Improved map Copyright decoration
- Expression support for the copyright text.
- Improved text formatting options, including shadows, outlines, backgrounds, etc.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : La police et la taille de la barre d'échelle de la fenêtre principale peuvent être personnalisées
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Custom SVG path and size for the north arrow decoration
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Gestion des données
### Feature: Refresh a materialized view
From the browser, with a right click on a materialized view, you can now refresh it.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Feature: Z and M support for offline editing
Offline editing now also supports layers with Z and M coordinates.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Fonctionnalité : Métadonnées pour les projets QGIS
Continuing the metadata work begun in QGIS 3.0, 3.2 now supports metadata for QGIS projects. This allows for detailed metadata to be set in project properties, including abstracts, keywords, contact details, links, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) au sein du projet ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formulaires et widgets
### Feature: Multi-column layout for multiselect value relation widget
The value relation widget with multi selection enabled now supports multiple columns. This allows better usage of horizontal screen space.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### Feature: Allow using a URL for custom attribute forms (UI file)
The UI file will be downloaded on every session on the first usage. This makes it possible to easily distribute updated UI files to clients.

This feature was funded by [SIRS](http://www.sirs-fr.com)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Feature: Drill-down (cascading) forms
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS User Group Danois, Bo Victor Thomsen et Lene Fischer, North River Geographic

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## Légende des couches
### Feature: Optional text on top of symbols for vector layers
This feature allows users to add extra information to the symbols in the legend.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Copy&Paste Group/Layers from a QGIS project to another.
Allowing to copy and paste groups or layers between projects and profiles.

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## Composeur de Cartes
### Feature: Data defined table source for attribute table items
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(All existing table attributes (column settings) are left intact, so setting a data defined table to a layer with different fields will result in empty columns in the table.)

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Project metadata embedded in layout exports
Saving a print layout to SVG, PDF or images will now embed any project metadata in the created file. Support for different metadata elements depends on the individual export format.

Cette fonctionnalité a été financée par Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) au sein du projet ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Meilleur formatage du texte de la barre d'échelle
QGIS 3.2 allows the full range of text formatting options to be used within scalebar text, e.g. buffers, shadows, and background shapes.

Unreadable scale bar text is a thing of the past!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Traitement
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Fonctionnalité : Charger un script depuis un modèle
New option to load Processing scripts from a custom template

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Feature: Feature filter algorithm for processing models
Add a new feature filter algorithm for the processing modeler. Allows filtering features of a source based on expressions and send matching features to different outputs as final products or different algorithm pipeline for further processing.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Fonctionnalité : Histogramme zonal
Ce nouvel algorithme ajoute des champs représentant le décompte de chaque valeur unique à partir d'une couche raster contenue dans des zones définies comme des polygones.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Portage des algorithmes d'union, de différence et d'intersection en C++
QGIS native geoprocessing algorithms have been ported from Python to C++. In addition to performance boost, several bugs have been resolved with this update.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
This new Processing algorithm projects points from an input point layer by a specified distance and bearing (azimuth). It supports dynamic parameters for the distance and bearing so that the distance and bearing can be taken from field values or expressions.

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Dynamic parameter values for more algorithms
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

In 3.2 the following algorithms now support dynamic parameters:
- Supprimer les trous
- Supprimer les sommets en double
- Simplifier
- Lisser
- Accrocher à la grille
- Subdiviser
- Transect
- Translation

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Multi-ring buffer (constant distance) algorithm
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Cette fonctionnalité a été développée par by Alex Bruy
### Feature: New \"segmentize\" algorithms
In QGIS 3.2 two new algorithms for segmentizing curved geometries have been added to Processing.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Option to create points on all polygon parts
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Algorithme de rotation des entités
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalités : Importation des photos géolocalisées
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Optionally the scan can be recursive and you can create an optional table of photos which could not be read or which were missing geotags.

The algorithm automatically sets the output table to use an external resource widget to display the linked photos in the attribute form.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Algorithme pour inverser les valeurs de coordonnées x/y 
Cet algorithme permute les valeurs de coordonnées X et Y dans les géométries source. Il peut être utilisé pour réparer des géométries dont les valeurs de latitude et de longitude ont été inversées.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
This change allows users to optionally set a sort order to use when assigning values in the Add Incremental Field algorithm. Previously values were always added using the original feature order. With this change users can control the order in which features are assigned values.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Indicator for distance parameter units
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Additionally - if the unit is in degrees, a small warning icon is shown next to the parameter. The tooltip for this icon advises users to reproject data into a suitable projected local coordinate system.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Algorithm log can be saved/cleared/copied
In the algorithm execution dialog, new buttons have been added to allow users to save the current log (to text or HTML files), copy the log contents to the clipboard, and clear the log.

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Wedge buffer algorithm
This new algorithm creates wedge shaped buffers from input points.

The azimuth parameter gives the angle (in degrees) for the middle of the wedge to point. The buffer width (in degrees) is specified by the width parameter. Note that the wedge will extend to half of the angular width either side of the azimuth direction. The outer radius of the buffer is specified via outer radius, and optionally an inner radius can also be specified.

The algorithm supports dynamic parameters for azimuth, width, and radius.

The native output from this algorithm is CurvePolygon geometries, but these may be automatically segmentized to Polygons depending on the output format.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Variable width buffers
New Processing algorithms have been added to create variable width buffers, including tapered buffers (with a specified start and end diameter) and variable width buffers from line string m values.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Reclassify raster algorithms
Two new native QGIS raster reclassification algorithms have been added to Processing. These are simple to use, yet fast and stable, and work for ANY raster layer type supported by QGIS!
- Reclassify by layer: reclassifies a raster using the ranges specified via min/max/value fields from a vector table
- Reclassify by table: reclassifies a raster using a fixed table entered by users in the algorithm dialog

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Algorithme d'union sur une couche seule
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Options de l'application et du projet
### Fonctionnalité : Couches requises pour un projet
Les couches requises ne peuvent pas être supprimées d'un projet. Ceci ajoute un niveau de sécurité supplémentaire pour empêcher les utilisateurs de supprimer des couches qui leur semblent ne pas servir (par ex. utilisées dans des jointures, des relations, des expressions).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Fonctionnalité : Enregistrer et charger des projets dans une base de données PostgreSQL
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Explorateur
### Feature: Save/Load connections for XYZ Tiles
From the Browser panel, XYZ Tiles entries can be exported/imported to/from an XML file.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Feature: Project home path can be manually set
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Project home paths can also be set to relative paths, in which case they will be relative to the project saved location.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Fournisseurs de données
### Feature: Support for mesh layers
Initial work has been done to introduce mesh layers supporting display of data on structured or unstructured meshes (grids) in addition to raster and vector layers. This is still a work in progress, expected to be fully ready in QGIS 3.4. The work so far lead to creation of a new library MDAL for handling of different formats of mesh-based data and there are new APIs introduced under the hood, however the user interface is not implemented yet.

Pour plus d'informations :

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

et

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: Automatically set default style for layers for ArcGIS Feature Server layers
When layers from a Feature Server are loaded into QGIS 3.2, they will automatically have the same style applied as has been specified for that layer on the server, matching the appearance of the layer when it is loaded into ArcGIS.

Cette fonctionnalité a été financée par SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Faster Oracle queries
Certain operations are greatly sped up for Oracle layers, e.g. case-insensitive value matches for features.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Restrict table list for a Oracle database connection to a preset schema
This change allows a schema to be set in the connection properties for an Oracle database connection. If set, only tables within that schema will be scanned and listed for the connection.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Read only support for curved Oracle geometries
Previously these geometries were silently discarded.

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Extensions
### Feature: Adding query history in DB Manager
Dans la version 3.2, il est possible de stocker des requêtes SQL. L'historique des requêtes est disponible dans la Fenêtre SQL du plugin Gestionnaire de base de données.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Feature: DB Manager SQL execution in background
Cette fonctionnalité a été développée par Paul Blottiere
## Fonctionnalités 3D
### Feature: 3D Polygons: Optionally generate back faces
Sometimes datasets with 3D polygons do not have consistent ordering of vertices (clockwise vs. counter-clockwise) and that caused sub-optimal results in the 3D view: either some polygons (walls) seem to be missing if back-face culling is enabled - or some polygons are shaded incorrectly if back-face culling is disabled. With the new option **Add back faces** enabled, the tessellator will generate triangles in both directions (front and back) which greatly improves the rendering quality for such datasets.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

The image contains freely available Prague 3D buildings dataset.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
