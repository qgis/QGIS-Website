---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.14
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.14{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Release date: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Version maintenue à Long Terme**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

L'objectif des versions LTR est de fournir une plate-forme stable et moins sujette aux modifications pour les entreprises et les organisations qui ne veulent pas effectuer plus d'une mise à jour par an des installations des postes des travail utilisateur ou des supports de formation. Le succès de cette version LTR dépend fortement de vous, notre utilisateur bien-aimé. Nous avons notamment besoin de votre soutien pour nous aider à financer la correction de bogues et vous devez également vous assurer que vos contrats de support avec vos fournisseurs indiquent que toutes les corrections de bug gérées par votre contrat sont également appliqués sur la branche LTR ainsi que sur la branche de développement normal.

Si vous pensez que la version LTR est importante, merci de penser à soutenir directement le projet QGIS ou à encourager votre fournisseur commercial pour qu'il utilise la version LTR comme base de votre solution d'entreprise de manière à ce que tout le monde puisse bénéficier d'une plate-forme stable qui sera améliorée et affinée en continu. Pour les utilisateurs et les organisations qui souhaitent bénéficier des toutes dernières évolutions, notre cycle de publication de quatre mois restera inchangé.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Sponsors actuels de QGIS
{{<fund type="changelog" >}}
## Général
### Fonctionnalité : Modification du comportement de la fonction strpos
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Les fichiers de projet des versions précédentes de QGIS doivent être mis à jour pour bénéficier de ce changement.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité : Zoom sur l'entité avec un clic-droit dans la table d'attribut
Vous pouvez maintenant zoomer sur n'importe qu'elle entité depuis la table d'attributs (sans avoir à sélectionner la ligne avant) en faisant un clic-droit et en sélectionnant Zoomer sur l'entité.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Fonctionnalité : Amélioration sur la rapidité et la mémoire
- **Sauvegarder un ensemble d'entités sélectionnées** depuis une couche volumineuse est maintenant plus rapide.
- La mise à jour des entités sélectionnées depuis la **calculatrice de champs** est plus rapide.
- **Zoom plus rapide** sur la sélection pour les couches volumineuses.
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **Filtrer les catégories dans le moteur de rendu catégorisé** (ex: afficher seulement certaines catégories et masquer d'autres) est beaucoup plus rapide car seules les entités concernées sont transmises par le fournisseur de données.
- **Réduction significative de la consommation mémoire** pour les couches vecteurs volumineuses.

### Fonctionnalité : Nouvelles variables d'expression
Lors du rendu, de nouvelles variables sont maintenant disponibles :
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Les expressions qui suivent sont utiles pour appliquer différents styles à différentes parties d'entités multi-parties :
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

Des variables relatives au système d'exploitation ont également été ajoutées :
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann (partie sur le système d'exploitation et les variables utilisateur).

Cette fonctionnalité a été développée par Nyall Dawson et Matthias Kuhn
### Fonctionnalité : Meilleur contrôle du placement des éléments de la carte
QGIS 2.14 dispose d'un contrôle plus fin sur le placement des flèches de nord, des barres d'échelle et de l'affichage du copyright dans le canevas de cartes. Vous pouvez maintenant positionner précisément ces éléments en utilisant différentes unités (incluant les millimètres, les pixels et le pourcentage).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Fonctionnalité : Programme de financement de résolution de bogues
Avant chaque publication d'une nouvelle version, nous entretenons un programme de financement de correction de bogues où nous finançons des développeurs pour clore un maximum de bogues. Nous avons décidé de d'inclure un rapport sur les bogues corrigés par ce programme dans les modifications en image. Cette liste n'est **pas exhaustive**.
- Sandro Santilli: [Postgis Connection freeze if you press \"Set filter\" during loading of data](http://hub.qgis.org/issues/13141)
- Sandro Santilli: [db_manager is unable to load rasters from connections with no dbname specified](http://hub.qgis.org/issues/10600)
- Sandro Santilli: [Plugin layers do not work correctly with rotation](http://hub.qgis.org/issues/11900)
- Sandro Santilli: Crash in QgsGeomColumnTypeThread stopping connection scan [#14140](http://hub.qgis.org/issues/14140) [#13806](http://hub.qgis.org/issues/13806)
- Sandro Santilli: [Crash after bulk change of attribute value in shapefile](http://hub.qgis.org/issues/11422)
- Sandro Santilli: [KMZ causes QGIS application crash (Mac)](http://hub.qgis.org/issues/13865)
- Sandro Santilli: [QGIS 2.8.1 crash opening FileGDB (openGDB-Driver)](http://hub.qgis.org/issues/12416)
- Sandro Santilli: [QGIS crashes when removing vertex of a multipart geometry](http://hub.qgis.org/issues/14188)
- Sandro Santilli: [test -V -R qgis_analyzertest segfaults](http://hub.qgis.org/issues/14176)
- Sandro Santilli: [output/bin/qgis_diagramtest segfaults](http://hub.qgis.org/issues/14212)
- Sandro Santilli: Overflow on primary key with negative values; crashes QGIS when editing [#13958](http://hub.qgis.org/issues/13958) [#14262](http://hub.qgis.org/issues/14262)
- Sandro Santilli: [PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Sandro Santilli: [TestVectorLayerJoinBuffer hangs if database is not available](http://hub.qgis.org/issues/14308)
- Nyall Dawson: [BLOCKER: Crash when opening layer properties dialog for geometryless vector layer](http://hub.qgis.org/issues/14116)
- Nyall Dawson: Problème de filtre côté serveur pour les couches OGR, Oracle et Spatialite.
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: Correction de problèmes lors de la conversion vers le moteur de rendu basé sur des règles, résultant dans un rendu cassé.
- Nyall Dawson: Correction du rendu catégorisé qui ne stockait pas les changements de source de symbole.
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: Correction de la gestion des valeurs de temps dans les attributs.
- Nyall Dawson: Correction de l'ordre des onglets de certaines boîtes de dialogue.
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Gestion des champs de type LongLong dans la boîte de dialogue de fusion des attributs.
- Nyall Dawson: Correction de l'affichage du détail des calculs de l'outil de mesure (affichage incorrect et non précis pour plusieurs combinaisons de SCR et d'unités).
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias : Couche raster rendue non correctement.
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias : Chargement lent de la table des attributs en mode débug.
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias : Corrections sur le moteur de rendu 2.5D.
- Martin Dobias: [HIGH: Long freeze when initializing snapping](http://hub.qgis.org/issues/12578)
- Martin Dobias: [NORMAL: Loading of data-defined from xml](http://hub.qgis.org/issues/14177)
- Martin Dobias: Fix DB manager to work with SpatiaLite \< 4.2
- Martin Dobias: [NORMAL: Crash while rendering in debug mode](http://hub.qgis.org/issues/14369)
- Martin Dobias: BLOCKER: Fix selection / identification in spatialite views [#14232](http://hub.qgis.org/issues/14232) [#14233](http://hub.qgis.org/issues/14233)
- Martin Dobias: [BLOCKER: Fix drag&drop of spatialite tables](http://hub.qgis.org/issues/14237)
- Jürgen Fischer:[Zoom to layer works incorrectly while layer editing](http://hub.qgis.org/issues/3155)
- Jürgen Fischer:[Help viewer process running in the background with no help viewer (or even QGIS) open](http://hub.qgis.org/issues/8305)
- Jürgen Fischer:[Spatialindex include path missing in some components](http://hub.qgis.org/issues/13197)
- Jürgen Fischer:[compile fails attempting to generate qgsversion.h](http://hub.qgis.org/issues/13680)
- Jürgen Fischer:[Edit widget configuration is stored twice](http://hub.qgis.org/issues/13960)
- Jürgen Fischer:[Extra space in \"IS NOT\" operator makes the expression return wrong selection](http://hub.qgis.org/issues/13938)
- Jürgen Fischer:[QGIS greadily allocates memory and crashes when editing moderately large shapefiles with the node tool](http://hub.qgis.org/issues/13963)
- Jürgen Fischer:[French reprojection use ntf_r93.gsb (IGNF:LAMBE etc ..)](http://hub.qgis.org/issues/14101)
- Jürgen Fischer:[Digitizing: \"Reuse last entered attribute values\" should not overwrite primary key column](http://hub.qgis.org/issues/14154)
- Jürgen Fischer:[Issues in Case expression description](http://hub.qgis.org/issues/14189)
- Jürgen Fischer:[shapefile vector writer: datetime field saved as date resulting in data loss of time](http://hub.qgis.org/issues/14190)
- Jürgen Fischer:[Add help for some variable functions](http://hub.qgis.org/issues/14259)
- Jürgen Fischer:[Virtual layers not working in Processing](http://hub.qgis.org/issues/14313)
- Jürgen Fischer:[layer definition file load error](http://hub.qgis.org/issues/14340)
- Jürgen Fischer:[QgsGeometry::fromWkb fails if WKB is different endian representation](http://hub.qgis.org/issues/14204)
- Jürgen Fischer:[Debian build failure.](http://hub.qgis.org/issues/14248)
- Jürgen Fischer:[PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Jürgen Fischer:[wkb access out of bounds](http://hub.qgis.org/issues/14315)
- Jürgen Fischer:[QGIS under Windows netCDF import reverses Y axis, Linux doesn\'t](http://hub.qgis.org/issues/14316) [OSGeo4W #483](https://trac.osgeo.org/osgeo4w/ticket/483)
- Jürgen Fischer:[OSGEO4W: Running offline install crashes installer](https://trac.osgeo.org/osgeo4w/ticket/105)
- Jürgen Fischer:[OSGEO4W: Dependencies are not tracking on Windows Server 2003 x64](https://trac.osgeo.org/osgeo4w/ticket/117)
- Jürgen Fischer:[OSGEO4W: installation from local package don\'t check the dependencies](https://trac.osgeo.org/osgeo4w/ticket/151)
- Jürgen Fischer:[OSGEO4W: Setup starts downloading and installing packages before showing you a list to choose from](https://trac.osgeo.org/osgeo4w/ticket/262)
- Jürgen Fischer:[OSGEO4W: Using -a for Advanced selects two options (command line install)](https://trac.osgeo.org/osgeo4w/ticket/351)
- Jürgen Fischer:[OSGEO4W: Infinite license download during quite installation of szip](https://trac.osgeo.org/osgeo4w/ticket/486)
- Jürgen Fischer: Problème sur le fournisseur de données Oracle.
- Jürgen Fischer: corrige le paramètre du chemin vers SAGA.

### Feature: Field calculator can be used to update feature\'s geometry
La calculatrice de champs peut maintenant être utilisée pour mettre à jour les géométries des entités en utilisant le résultat d'une expression géométrique. C'est très utile pour réaliser des tampons sur un groupe donné d'entités. De plus, les nouvelles fonctions géométriques de QGIS 2.14 ajoutent de nombreuses opérations de manipulation de géométries !

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Nouvelles fonctions dans le générateur d'expressions
De nouvelles fonctions d'expression ont fait leur apparition dans la version 2.14:
- `relate`: performs a DE-9IM geometry relation by either returning the DE-9IM representation of the relationship between two geometries, or by testing whether the DE-9IM relationship matches a specified pattern.
- the `make_point` function now accepts optional z and m values, and a new `make_point_m` function has been added for creation of PointM geometries.
- `m` and `z` functions for retrieving the m and z values from a point geometry
- new `make_line` and `make_polygon` functions, for creation of line and polygon geometries from a set of points
- `reverse`, for reversing linestrings
- `eval` function, which can evaluate a string as though it is an expression of its own
- `translate` function, for translating geometries by an x/y offset
- `darker` and `lighter` functions, which take a color argument and make it darker or lighter by a specified amount
- `radians` and `degrees`: for converting angles between radians and degrees
- `point_on_surface`: returns a point on the surface of a geometry
- `exterior_ring`: returns the exterior ring for a polygon geometry
- `is_closed`: returns true if a linestring is closed
- new geometry accessor functions: `geometry_n` (returns a specific geometry from within a collection), `interior_ring_n` (returns an interior ring from within a polygon)
- `num_geometries`: returns number of geometries inside a collection
- `num_rings`: returns number of rings in a polygon geometry object
- `num_interior_rings`: returns number of interior rings in a polygon
- `nodes_to_points`, for converting every node in a geometry to a multipoint geometry
- `segments_to_lines`, for converting every segment in a geometry to a multiline geometry
- `closest_point`: returns closest point in a geometry to a second geometry
- `shortest_line`: returns the shortest possible line joining two geometries

`nodes_to_points` and `segments_to_lines` are intended for use with geometry generator symbology, eg to allow use of m and z values for nodes/lines with data defined symbology.

Autres améliorations :
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Outils d'analyse
### Fonctionnalité : Nouvelles fonctions statistiques pour l'outil de fusion d'attributs
Lorsque vous utilisez l'outil de fusion d'attributs ou l'outil de fusion d'entités, il existe maintenant d'autres statistiques disponibles permettant d'affecter les résultats des valeurs d'attributs fusionnés. Ces fonctions sont, entre autres, Q1 (1er quartile), Q3 (3ème quartile), écart inter-quartiles, valeurs majoritaires et minoritaires, nombre de valeurs uniques.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : les valeurs z/m sont affichées dans l'outil d'identification
L'outil d'identification est maintenant capable d'afficher n'importe quelle valeur z ou m pour les entités identifiées. Si l'entité est une ligne ou un polygone, l'outil montrera le numéro de sommet et la valeur x/y/z/m pour le sommet le plus proche du point identifié. L'outil d'identification affiche également le nombre de parties et le numéro de partie des collections géométriques.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Gestion unifiée des unités de distance et de surface et des formats de coordonnées
Dans QGIS 2.14, la gestion des différentes options des unités de distance, de surface et d'affichage de coordonnées ont été unifiées, simplifiées et déplacées dans les propriétés du projet. Ce changement permet de nombreux avantages, dont les suivants :
- Le format des coordonnées indiqué dans les propriétés du projet sont utilisées de manière uniforme partout où une coordonnées doit être affichée, incluant l'outil d'identification et la barre d'état.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- D'autres unités de surface ont été ajoutées, comme les yards carrés, les acres, les hectares et d'autres encore.
- De nouvelles unités d'angle ont été ajoutées à l'outil de mesure des angles, incluant les rotations, les minutes et les secondes d'arc.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par le programme de sponsor de correction de bogues de QGIS.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Explorateur
### Fonctionnalité : Améliorations de l'explorateur
L'explorateur QGIS est un panneau pour l'accès aux fichiers, aux services Web OGC et pour la connexion aux bases de données qui vous permet de glisser-déposer facilement des couches depuis les sources sus-mentionnées directement dans votre canevas de carte (ou dans une fenêtre DB Manager). Deux nouvelles améliorations ont été ajoutées dans cette version:
- **Certains chemins peuvent être maintenant masqués depuis le panneau d'exploration**. Cela permet de simplifier l'affichage de vos sources de données en affichant uniquement les répertoires qui vous concernent.
- **Chargement des projets directement depuis l'explorateur**. Vous pouvez maintenant faire un glisser-déposer d'un projet complet dans le canevas de carte de QGIS et il sera chargé.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Nathan Woodrow
## Fournisseurs de données
### Fonctionnalité : Cache WMS
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité : Amélioration de la gestion des géométries courbes
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Meilleure gestion des champs de date et de temps
QGIS 2.14 améliore la gestion des champs de type date et temps, incluant:
- Les champs de date et heure PostgreSQL sont gérés correctement.
- Le moteur d'expression gère l'ensemble des types de champs de temps.
- Le constructeur d'expression affiche maintenant les pré-résultats pour les dates, les temps, les dates et heures et les intervalles.
- Les champs de temps sont complètement gérés pour les couches vecteurs fichiers (selon le format), PostgreSQL, MS SQL Server et les couches en mémoire temporaire.
- Sauvegarder des couches dans des fichiers vecteurs conserve les champs de date si le format du fichier vecteur le permet (ex: fichiers MapInfo .tab).

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Jürgen Fischer et Nyall Dawson
### Fonctionnalité : Gestion des valeurs Z/M du fournisseur de données de texte délimité
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Édition par groupes de transaction pour PostgreSQL
Une nouvelle option a été introduite pour permettre l'édition transactionnelle.

Lorsque cette option est activée:
- Toutes les couches de la même base de données sont rassemblées dans un groupe de transaction.
- Lorsque la première couche d'un groupe passe en mode édition, toutes les autres couches sont également mises en mode édition, automatiquement.
- Lorsqu'une couche est éditée, les changements sont envoyés immédiatement à la base de données, ce qui permet aux contraintes et aux déclencheurs d'être appliqués immédiatement.
- Lorsqu'une couche appartenant à un groupe de transaction est validée, toutes les couches sont alors validées (via une transaction dans la base de données)
- Lorsqu'une couche appartenant à un groupe de transaction d'un groupe de couche est remise à l'état initial, toutes les couches sont remises à leur état initial (via une transaction dans la base de données).

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Cette fonction n'est implémentée que pour les bases de données PostgreSQL pour le moment.

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Fonctionnalité : Authentification par IGC pour le fournisseur PostgreSQL
La possibilité d'utiliser le gestionnaire d'authentification de QGIS introduit dans la version 2.12 a été étendu au fournisseur de données PostgreSQL. Cela permet de se connecter à PostgreSQL en utilisant l'authentification basique ou via une IGC, où les éléments de connexion sont gérés par la configuration QGIS. Cette nouvelle authentification peut également être utilisée dans DB Manager.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Cette fonctionnalité a été développée par by Luigi Pirelli
### Fonctionnalité : Couches virtuelles
Des requêtes SQL dynamiques peuvent maintenant être utilisées sur n'importe quel type de couche vecteur que QGIS est capable d'ouvrir, même si le format de la couche ne permet pas les requêtes SQL !

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

La syntaxe SQL utilisée est celle de SQLite avec les fonctions Spatialite. Les fonctions d'expressions QGIS peuvent également être utilisées dans les requêtes. Tout type de couche vecteur peut être utilisée dans une requête, y compris les couches multiples de différents fournisseurs de données, pour réaliser des jointures.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Fonctionnalité : Plus d'extensions de fichiers pour les sélecteurs de fichiers GDAL et OGR
Pour la gestion des fichiers vecteurs et rasters, QGIS s'appuie sur la bibliothèque GDAL/OGR. Cela signifie que QGIS peut ouvrir pratiquement n'importe quel format pouvant être lu par GDAL ou OGR. Néanmoins, jusqu'à cette version, certaines extensions de ces formats de fichiers n'étaient pas présentes dans les boîtes de dialogue des sélecteurs de fichiers GDAL et d'OGR. Les utilisateurs pouvaient croire que QGIS n'était pas capable d'ouvrir ces formats. Pour minimiser ce problèmes de nouvelles extensions ont été ajoutées aux filtres des sélecteurs de fichiers de GDAL et d'OGR:

**Pour les fichiers vecteurs :**
- .thf pour le format EDIGEO du cadastre français
- .ods pour le format OpenDocument Spreadsheet de LibreOffice
- .xls pour le format Microsoft Excel
- .xlsx pour le format Microsoft Excel OpenXML
- .xml pour le format NAS - ALKIS
- .map pour le format WAsP
- .pix pour le format PCIDSK
- .gtm et .gtz pour le format GPSTrackMaker
- .vfk pour le format VFK
- .osm et .pbf pour le format OpenStreetMap
- .sua pour le format SUA
- .txt pour le format OpenAir
- .xml pour le format de table Planetary Data Systems
- .htf pour le format Hydrographic Transfer
- .svg pour le format SVG
- .gen pour le format ARCGEN
- .sxf pour le format Storage and eXchange
- .pdf pour le format vecteur PDF Géospatial
- .sgy et .segy pour le format SEG-Y
- .seg, .seg1, .sp1, .uko, .ukooa pour le format SEGUKOOA
- .ovf pour le format de fichier VRT vecteur
- .kmz pour le format KML compressé (KMZ)
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 pour le format SQLite/Spatialite
- .sl3 pour le format SQLite Spatial (FDO)
- CouchDB spatial (via une URL)

**Pour les fichiers raster:**
- .ovr pour le format des fichiers VRT raster

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Cette méthode réduit le nombre de sommets d'une géométrie renvoyée à QGIS, ce qui diminue la taille de téléchargement ainsi que le temps nécessaire pour faire le rendu et permet d'économiser de la bande passant entre QGIS et le serveur PostgreSQL.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## Gestion des données
### Fonctionnalité : Suppression de l'extension SPIT
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Nathan Woodrow
### Fonctionnalité : Export DXF : option pour utiliser le titre à la place du nom en tant que nom de la couche DXF dans l'application bureautique et serveur
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité : Le type géométrique peut être outrepassé dans la boîte de dialogue d'enregistrement des fichiers vecteurs
Cela permet d'enregistrer une table sans géométrie avec un type géométrique, de manière à ce que les géométries puissent être ajoutées aux lignes. Auparavant, on ne pouvait le faire directement dans QGIS que via des jointures complexes ou d'autres solutions de contournement.

De plus, des options ont été ajoutées pour forcer que le fichier de sortie soit de type multi-géométrie ou inclue une dimension z.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Les jointures entre vecteurs sont maintenant sauvegardées dans les fichiers QLR
### Fonctionnalité : Contrôle de formulaire Ressource Externe
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- Vous pouvez définir et paramétrer le **stockage des chemins en relatif**. Ce mode d'enregistrement vous permettra de conserver uniquement la partie du chemin présente après l'emplacement par défaut (si celui-ci est paramétré) ou après l'emplacement du fichier de projet. Cette fonctionnalité est particulièrement utile lorsque vous souhaitez enregistrer des chemins de fichiers longs dans des attributs avec une taille limitée (comme les attributs textes des fichiers Shapefiles qui sont limité à 254 caractères) ou pour héberger un ensemble fichier projet et fichiers d'archive dans un seul répertoire, pour faciliter la distribution.
- Une autre nouvelle fonctionnalité qui rend le contrôle de formulaire intéressant à utiliser est **l'affichage des chemins sous forme de liens hypertextes**. En cliquant sur le lien, vous ouvrirez directement le fichier depuis QGIS. Vous pouvez paramétrer cette option pour afficher le chemin complet ou uniquement le nom de fichier. Le fichier sera ouvert avec le logiciel par défaut pour le format du fichier, tel que configuré dans votre système d'exploitation.
- Vous pouvez également **utiliser une URL à la place d'un chemin de fichier**. Le contrôle de formulaire interprètera l'URL et vous donner la possibilité d'ouvrir le lien directement dans votre navigateur web par défaut.
- Vous pouvez choisir d'**enregistrer des noms de répertoires à la place des noms de fichiers**.
- Il existe un **visualiseur interne de documents** dans ce contrôle de formulaire. Vous pouvez l'utiliser pour afficher des images ou des pages web directement dans QGIS. Le sélecteur de fichier du visualiseur interne bénéficie de toutes les options mentionnées ci-dessus.

Pour plus d'informations sur les options de configuration, vous pouvez utiliser les info-bulles de la boîte de dialogue de configuration du contrôle de formulaire.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Cette fonctionnalité a été développée par**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Fonctionnalité : Relations N:M
Cette fonctionnalité ajoute la possibilité de gérer des données dans une base de données relationnelle avec des relations N:M (relations plusieurs à plusieurs). Au niveau des formulaires d'édition, les outils d'ajout, de suppression, de création/suppression de lien fonctionne également sur la table liée si une relation est définie comme une relation N:M.

La configuration est réalisée par l'onglet Champs où il est possible de choisir la seconde relation de la relation initiale (s'il existe une relation secondaire par rapport à la table liée).

**Limites :**

QGIS n'est pas un système de gestion de base de données.

Cette fonctionnalité repose sur le système de base de données sous-jacent. En particulier :
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par la République et le canton de Neuchâtel, la ville de Pully et la ville de Vevey.

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Numérisation
### Fonctionnalité : Couleur de numérisation paramétrable
Vous pouvez maintenant paramétrer la couleur et la largeur de numérisation.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Fonctionnalité : Outil de tracé assisté
Le nouvel outil de tracé est un outil avancé permettant de numériser des entités sur une couche à partir du tracé des entités d'une autre couche.

L'outil de tracé :
- uses Dijkstra's shortest path algorithm to find traceable routes
- Peut tracer des routes sur plusieurs entités distinctes.
- Peut être utilisé avec les outils de numérisation avancée (ex: remodeler les entités).
- Peut être activé et désactivé en pression la touche **T** lors de la numération.
- Est rapide et facile à utiliser.

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Cette fonctionnalité a été financée par: The Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Étiquetage
### Feature: \"Cartographic\" placement mode for point labels
Dans ce mode de placement, les points potentiels d'étiquettes suivent des règles de placement cartographiques idéales. Par exemple, les règles de placement sont priorisées dans l'ordre suivant :
- coin supérieur droit
- coin supérieur gauche
- coin inférieur droit
- coin inférieur gauche
- au milieu à droite
- au milieu gauche
- en haut, décalé légèrement à droite
- en haut, décalé légèrement à gauche

(respectant les règles définies par Krygier et Wood (2011) et d'autres travaux cartographiques)

La priorité de placement peut également être paramétrée pour une entité donnée en utilisant la liste des positions, définie par les données. Cela permet d'utiliser un placement pour certaines entités et pas pour les autres, exemple: les entités sur la côte peuvent empêcher les étiquettes de s'afficher sur les territoires hors d'eau.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Appliquer la distance de l'étiquette par rapport aux limites du symbole
Lorsque ce paramètre est activé, la distance de l'étiquette s'applique à partir des limites du symbole rendu pour le point, à la place du point lui-même. Ceci est particulièrement utile lorsque la taille du symbole est variable (définie par les données) ou bien lorsque différents symboles sont utilisés dans une symbologie catégorisée.

A noter que ce paramètre n'est disponible que pour le nouveau mode de placement de point d'étiquette cartographique.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Contrôle de l'ordre de rendu des étiquettes
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

De plus, la logique a été affinée pour gérer les cas où 2 étiquettes ont un index z identique:
- Si elles sont dans la même couche, une étiquette plus petite sera toujours tracée au dessus de l'étiquette plus large.
- Si elles sont issues de couches différentes, les étiquettes sont tracées dans le même ordre que les couches (pour respecter l'ordre des couches dans la légende).

Les diagrammes ont maintenant également un index z (mais non défini par les données) de manière à pouvoir gérer l'ordre des étiquettes et des diagrammes.

A noter que ce paramètre ne permet *PAS* d'autoriser le tracé des étiquettes au dessus des entités d'autres couches, il contrôle uniquement l'ordre dans lequel les étiquettes sont tracée à partir du niveau le plus haut de la carte.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Un symbole rendu est maintenant considéré comme un obstacle pour les étiquettes des entités ponctuelles
Auparavant, seule l'entité de point elle-même était traitée comme un obstacle pour les étiquettes. Si un symbole de grande taille ou un symbole décalé était utilisé pour représenter le point, les étiquettes pouvaient alors le recouvrir dans recouvrir le point.

Maintenant, la taille et le décalage du symbole rendu sont pris en compte pour la détection de la collision avec les étiquettes. QGIS évite maintenant de tracer des étiquettes sur les symboles de points avec de meilleures conditions.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par la Ville d'Uster.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Légende des couches
### Fonctionnalité : Coller un style à plusieurs couches sélectionnées ou à toutes les couches d'un groupe
Cette fonctionnalité permet de coller le style d'une couche à tout un groupe ou à l'ensemble des couches sélectionnées.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Salvatore Larosa
### Fonctionnalité : Filtre de légende par expression
Il est maintenant possible de filtrer les éléments de la légende par une expression. Cette fonctionnalité a été développée en utilisant les filtres basés sur des règles et la symbologie catégorisée.

Le filtre de légende est disponible depuis le panneau de légende ainsi que pour les éléments de légende du composeur QGIS.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Composeur de Cartes
### Fonctionnalité : Nouvelles options de filtre de légende
Cette fonctionnalité introduit deux nouvelles options au filtre de légende.

La première, le filtre par expression, permet aux utilisateurs d'utiliser une expression pour filtrer quelles seront les entités qui seront affichées dans la légende. Seuls les symboles des entités qui correspondent au filtre seront affichés dans la légende.

La seconde option de filtre permet au composeur de filtrer uniquement les éléments qui sont présents dans le polygone de l'atlas courant.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Fonctionnalité : Chemins supplémentaires pour les modèles de composition
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Cette fonctionnalité a été développée par Nathan Woodrow
### Fonctionnalité : Sélection multiple dans le gestionnaire de compositions
Le gestionnaire de composition permet de gérer plusieurs compositions en même temps. Vous pouvez maintenant ouvrir et supprimer plusieurs compositions en utilisant la touche Ctrl pour sélectionner plusieurs compositions dans la liste.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Extensions
### Fonctionnalité : Gestion du système d'authentification pour le gestionnaire d'extensions
La gestion du nouveau système d'authentification a été ajoutée au gestionnaire d'extension. Cela permet aux utilisateurs d'utiliser des configurations d'authentification pour se connecter à des dépôts d'extension. Cela permet également aux administrateurs systèmes de créer un accès authentifié à des dépôts d'extension ou à authentifier le téléchargement de certaines extensions.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Cette fonctionnalité a été développée par Larry Shaffer
## Traitement
### Fonctionnalité : Nouveaux algorithmes de la version 2.14
#### Géotraitements QGIS :
- Lisser une géométrie: permet de lisser des couches de polylignes ou de polygones.
- Inverse la direction des lignes.

#### Géoalgorithmes GDAL/OGR :
- gdal2tiles: construit un répertoire de tuiles TMS, KMLs ou incluant une simple visualisation web.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Fonctionnalité : Assurance Qualité sur les tests unitaires
Pour garantir une stabilité à long terme du module Processing (NDT: module des géotraitements), un nouveau cadre de test a été introduit.

Les géo-traitements de Processing sont exécutés après chaque changement du code source de QGIS et le résultat des tests est comparé à un jeu de données de contrôle pour garantir le fonctionnement correct de chaque traitement. Cela permet d'identifier immédiatement toute régression.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Fonctionnalité : Amélioration de la boîte à outils
L'interface simplifiée a été supprimée et un système plus orienté utilisateur a été mis en place pour mieux accéder aux algorithmes. La fonction de recherche d'algorithmes recherche également dans les fournisseurs de traitements désactivés et vous suggère de les activer.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Cette fonctionnalité a été développée par Víctor Olaya
### Fonctionnalité : Les traitements par lot peuvent être sauvegardés et ouverts ultérieurement à partir de l'interface
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Fonctionnalité : Boîte de dialogue d'algorithme plus complète
Une courte description est maintenant affichée à côté des paramètres de l'algorithme rendant plus facile la compréhension de l'action de l'algorithme.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Fonctionnalité : modules GRASS7 v.net
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

Les algorithmes v.net utilisent généralement une couche vecteur linéaire (pour le réseau) et une couche de points qui représente les nœuds sur lesquels vous souhaitez réaliser le traitement. Assurez-vous d'utiliser une couche vecteur linéaire qui soit vraiment un réseau (les segments doivent être connectés par des sommets sans intersection entre segments) pour éviter tout problème. Vous pouvez également utiliser un attribut de la couche de réseau pour définir les coûts (le contenu de l'attribut est utilisé pour calculer le coût de transport le long du segment).

Voici un résumé rapide des différents algorithmes qui ont été inclus dans Processing:
- v.net.alloc : créé des sous-réseaux à partir de nœuds centraux.
- v.net.allpairs : Calcule le chemin le plus court entre toutes les paires de nœuds sur le réseau.
- v.net.arcs : Créé des arcs à partir d'un fichier de points.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: Calcule le degré, la centralité, la proximité et la centraluté par vecteur eigen de chaque nœud du réseau.
- v.net.components : Calcule les éléments connectés de manière fortes et faibles sur le réseau.
- v.net.connect : Connecte des points (nœuds) aux arcs les plus proches du réseau (et ajoute des segments si nécessaire).
- v.net.connectivity: Calcule la connectivité des sommets entre deux jeux de nœuds sur le réseau.
- v.net.distance: Calcule le chemin le plus court par le réseau entre deux jeux de nœuds.
- v.net.flow: Calcule le flux maximal entre deux jeux de nœuds sur le réseau.
- v.net.iso: Calcule une carte isochrone du réseau à partir d'un ensemble de nœuds.
- v.net.nodes : extrait les nœuds d'une couche de réseau/graphe.
- v.net.nreports : Renvoie des informations sur les nœuds du réseau.
- v.net.path : Trouve le chemin le plus court sur le réseau entre deux nœuds.
- v.net.report : Renvoie des informations sur les segments d'un réseau.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: Calcule le graphe de visibilité.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programmation
### Fonctionnalité : Amélioration de l'éditeur de fonction d'expression
Avec sauvegarde automatique.

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Fonctionnalité : Sauvegarder le code Python d'initialisation directement dans le fichier de projet
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Fonctionnalité : Nouvelles options de filtre et de tris pour la classe QgsFeatureRequest
La classe QgsFeatureRequest gère maintenant une limite supérieure d'entités renvoyées. Dans bien des cas, cette limite est transmise au fournisseur de données, ce qui permet des gains de performances significatifs lorsque seul un certain nombre d'entités est nécessaire.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Fonctionnalité : Options de code Python pour les formulaires personnalisés
Cette fonctionnalité amène de nouvelles options pour le code Python des formulaires personnalisés :
- Chargement depuis un fichier (avec une boîte de sélection de fichier).
- Chargement depuis l'environnement (comme une extension ou une fonction d'initialisation Python).
- Directement en entrant le code dans un contrôle (nouvelle option).

Les options de configuration, incluant le code Python stocké en interne du projet ainsi que les paramètres de style QML peuvent être exportés/restaurés à partir d'une base de données.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Fonctionnalité : Nouvelles classes PyQGIS 2.14
### Nouvelles classes de base
- [QgsAttributeEditorElement](https://qgis.org/api/classQgsAttributeEditorElement.html)
  - abstract base class for any elements of a drag and drop form
- [QgsAttributeEditorContainer](https://qgis.org/api/classQgsAttributeEditorContainer.html)
  
  \- container for attribute editors, used to group them visually in an attribute form
- [QgsAttributeEditorField](https://qgis.org/api/classQgsAttributeEditorField.html)
  - element for loading a field\'s widget onto a form
- [QgsAttributeEditorRelation](https://qgis.org/api/classQgsAttributeEditorRelation.html)
  - element for loading a relation editor widget onto a form
- [QgsEditFormConfig](https://qgis.org/api/classQgsEditFormConfig.html)
  - stores and sets configuration parameters for attribute editor forms
- [QgsFeatureFilterProvider](https://qgis.org/api/classQgsFeatureFilterProvider.html)
  
  \- provides an interface for modifying a QgsFeatureRequest in place to apply additional filters to the request
- [QgsTracer](https://qgis.org/api/classQgsTracer.html) - provides graph creation and shortest path search for vector layers
- [QgsTransactionGroup](https://qgis.org/api/classQgsTransactionGroup.html)
  - interface for grouping layers into single edit transactions
- [QgsUnitTypes](https://qgis.org/api/classQgsUnitTypes.html) -helper functions for various unit types and conversions between units (eg distance and area units)
- [QgsVirtualLayerDefinition](https://qgis.org/api/classQgsVirtualLayerDefinition.html)
  - class for manipulating the definitions of virtual layers
- [QgsVirtualLayerDefinitionUtils](https://qgis.org/api/classQgsVirtualLayerDefinitionUtils.html)
  - helper utilities for working with QgsVirtualLayerDefinition objects
- [Qgs25DRenderer](https://qgis.org/api/classQgs25DRenderer.html) -2.5D symbol renderer
- [QgsGeometryGeneratorSymbolLayerV2](https://qgis.org/api/classQgsGeometryGeneratorSymbolLayerV2.html)
  - geometry generator symbol layer
- [QgsFeatureRequest.OrderByClause](https://qgis.org/api/classQgsFeatureRequest_1_1OrderByClause.html)
  - class for specifying a field sort order for feature requests
- [QgsFeatureRequest.OrderBy](https://qgis.org/api/classQgsFeatureRequest_1_1OrderBy.html)
  - a prioritized list of order by clauses for sorting

### Nouvelles classes d'IHM
#### Contrôles réutilisables:
- [QgsExternalResourceWidget](https://qgis.org/api/classQgsExternalResourceWidget.html)
  
  \- widget for displaying a file path with a push button for an \"open file\" dialog, and optional display of pictures or HTML files
- [QgsFileWidget](https://qgis.org/api/classQgsFileWidget.html) -widget for selecting a file or a folder
- [QgsLegendFilterButton](https://qgis.org/api/classQgsLegendFilterButton.html)
  
  \- tool button widget that allows enabling or disabling legend filter by contents of the map
- [QgsMapCanvasTracer](https://qgis.org/api/classQgsMapCanvasTracer.html)
  
  \- an extension of QgsTracer that provides extra functionality for interacting with map canvases
- [Qgs25DRendererWidget](https://qgis.org/api/classQgs25DRendererWidget.html)
  - widget for setting properties for a 2.5D renderer
- [QgsColorWidgetAction](https://qgis.org/api/classQgsColorWidgetAction.html)
  - widget action for embedding a color picker inside a menu

#### Boîtes de dialogues réutilisables :
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## QGIS Server
### Fonctionnalité : paramètre STARTINDEX dans la requête WFS GetFeature
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Fonctionnalité : showFeatureCount dans la classe GetLegendGraphic
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Cette fonctionnalité nécessite un serveur X.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Fonctionnalité : Option pour éviter le rendu d'artefacts aux bordures de tuiles
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Fonctionnalité : Vérificateur de configuration des propriétés de projet
Pour faciliter la configuration d'un projet pour QGIS Server, un nouveau vérificateur de configuration a été ajouté dans les propriétés du projet.

Les tests de vérification gèrent:
- Les noms dupliqués ou les alias utilisés comme des noms OWS.
- Les noms OWS invalides.
- L'encodage manquant pour les couches vecteur.

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Fonctionnalité : Fourniture de métadonnées INSPIRE WMS
Dans les propriétés du projet, l'utilisateur peut:
- Activer les métadonnées INSPIRE
- Choisir la langue du service à partir des 24 langues officielles de l'Union Européenne et 5 langues régionales.
- Choisir le scénario du service de métadonnées et indiquer leurs paramètres.

Le service WMS 1.3.0 (de QGIS Server) reflètera la configuration INSPIRE du projet.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Fonctionnalité : Ajout d'un nom court pour les couches, les groupes et le projet
Un certains nombre d'éléments disposent d'un **Nom** et d'un **Titre**. Le nom est une chaîne de caractères utilisée dans la communication de machine à machine alors que le titre est utilisé pour les êtres humains. Par exemple, un jeu de données peut avoir un titre descriptif **Température Atmosphérique Maximum** et être requêté par le nom abrégé *ATMAX*.

L'utilisateur peut déjà ajouter un titre pour les couches et le projet. Dans les services Web OpenGeoSpatial, OWS (WMS, WFS, WCS), le nom est basé sur le nom utilisé dans l'arbre des couches. Ce nom est plus une étiquette pour les humains qu'un nom de machine à machine.

Pour ajouter la possibilité aux utilisateurs de définir le Nom en tant que texte destiné aux ordinateurs, cette fonctionnalité ajoute :
- L'édition de nom court dans les propriétés de la couche.
- Boîte de dialogue WMS pour les groupes (permet de saisir le nom court du groupe, le titre et un résumé).
- L'édition de nom court dans les propriétés du projet.
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- Ajout d'un élément TreeName dans les propriétés du projet (fullProjectSettings).

Si un nom court a été utilisé pour des couches, des groupes et pour le projet, il sera utilisé par QGIS Server pour définir le nom de la couche.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Symbologie
### Fonctionnalité : Assistant de taille pour les largeurs de lignes variables
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Fonctionnalité : Gestion de la transparence dans les paramètres de couleur SVG
Les fichiers SVG non fournis par QGIS doivent disposer des attributs :

`fill-opacity="param(fill-opacity)"`

et

`stroke-opacity="param(outline-opacity)"`

pour autoriser la transparence dans le SVG.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Duplication simplifiée des couches de symbole
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Moteur de rendu 2.5D
Il ajoute une interface de configuration et un moteur de rendu pouvant générer un style composé qui produit un effet 2.5D.

Il permet de configurer le style et il a été créé pour rester simple dans son utilisation.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Cette fonctionnalité a été développée par**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Cette fonctionnalité a été financée par**:
- Conseil Régional de Picardie (France)
- ADUGA
- Ville de Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Fonctionnalité : Permettre la définition de l'ordre de rendu des entités
Lorsque les entités doivent être gérées dans un certain ordre, ce dernier peut être indiqué en utilisant une expression arbitraire.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

On peut également contrôler l'ordre ascendant ou descendant ainsi que la gestion des valeurs NULL (traitées en premier ou en dernier).

Lorsque c'est possible, la requête est envoyée à la base de données (en fonction de la complexité de l'expression ainsi que du type de fournisseur de données pour la couche). S'il n'es pas possible d'envoyer la requête directement à la base de données, le tri et l'ordre sont gérés localement.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

Elle est également disponible pour les extensions :

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Fonctionnalité : Générateur de symboles géométriques
Le générateur de symboles géométriques permet d'utiliser le moteur des expressions pour modifier la géométrie avant de faire le rendu ou bien de créer de nouvelle géométries selon les attributs des entités.

Il peut être utilisé en combinant tout type d'opérateur spatial tel que buffer, translate, intersect ou extrude avec des paramètres basés sur des attributs, simplement pour le rendu, sans modifier aucunement les données source.
### Exemples
#### Translation d'une géométrie.
Utilisé pour le toit du moteur de rendu 2.5D

    translate( $geometry, 10, 10 )
    
#### Remplissage de la bordure des polygones.
La syntaxe suivante permet de générer un polygone qui représente la bordure extérieure du polygone d'origine (voir l'image en exemple).

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
Différentes couches de symboles peuvent contenir différents générateurs géométriques permettant d'afficher différentes versions d'une même géométrie en même temps. Le moteur de rendu 2.5D est un exemple de ce genre d'utilisation.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Cette fonctionnalité a été financée par le Conseil Régional de Picardie, ADUGA, la Ville de Nyon et Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Interface utilisateur
### Fonctionnalité : La table d'attributs peut être rafraîchie
Une option permettant de recharger les attributs de la table d'attributs est maintenant disponible.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Fonctionnalité : Modification directe de la couleurs du rendu et des classes de symboles depuis le menu contextuel de légende
Affiche un contrôle de choix de couleur dans le menu, ce qui vous permet de choisir interactivement une couleur pour un symbole sans avoir à ouvrir la boîte de dialogue concernée !

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Édition directe des symboles de légende depuis l'arbre des couches
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Fonctionnalité : Afficher/Masquer tous les éléments de légende via le menu contextuel
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
