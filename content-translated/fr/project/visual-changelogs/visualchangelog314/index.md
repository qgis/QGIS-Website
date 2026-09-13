---
HasBanner: false
draft: false
releaseDate: '2020-06-19'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.14
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.14{#changelog314 }
![image1](images/splash.jpeg)

Release date: 2020-06-19

Another awesome release in the trail of great QGIS releases we have made across 18 years of development. This release is so jam-packed with new features and improvements big and small, it is hard to know where to start. Some of the marquee features include vector tile support, huge advances in mdal / mesh support, native support for temporal data in WMS-T, PG Raster, vector providers, and mesh layers. Users focussed on cartography and digitising haven\'t been left out either, with many new options for you!

**Remerciements**

We would like to thank the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait, nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous croyons que mettre à disposition un outil géographique de prise de décisions concourra à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonctionnalite : Nouveaux paramètres de police pour les annotations de décoration de la grille
Annotations for the map canvas\' grid decoration are now fully customizable including font color, buffer, etc.

![image8](images/entries/14b7cf800ef293ac3ea3f00d12a30022876e713c.webp)

Cette fonctionnalité a été financée par iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Temporel
### Fonctionnalite : Réglage cumulatif de la plage temporelle dans le contrôleur temporel
Ajoute un paramètre dans le contrôleur temporel pour régler la plage temporelle de l'animation sur cumulative. Cela signifie que toutes les images d'animation auront la même date et heure de début mais des dates et heures de fin différentes.

This is useful is you wish to accumulate data in your temporal visualisation instead of showing a \'moving time window\' across your data.

![image2](images/entries/90da13821bfde46aa6d9d951fb9a31bf27d85656.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Feature: Add a new \"Redraw Layer Only\" mode for temporal vector layers
Dans ce mode, la couche sera automatiquement redessinée chaque fois que la plage temporelle sera modifiée, mais aucun filtrage temporel ne sera appliqué aux entités.

Cette configuration est utile lorsque la couche a des paramètres de symbologie qui varient en fonction de la portée temporelle. Par exemple, lorsqu'une couche utilise des expressions de rendu basées sur des règles dépendantes du temps ou des expressions de symbologie définies par les données.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité: Ajouter un support de base pour la manipulation temporelle des couches vectorielles
Cela permet d'exposer certaines capacités temporelles natives de base pour les couches vectorielles :
- Plage de temps statique pour la couche (pour correspondre aux possibilités de la couche raster), cela définit une seule plage de temps statique qui s'applique à l'ensemble de la couche. Toutes les entités de la couche seront affichées chaque fois que le temps du canevas chevauche l'intervalle de temps de la couche
- \"Single field with DateTime\": Allows selection of a single Date or DateTime field from the layer. Features will be shown whenever this field value is within the canvas time range
- \"Separate Fields for Start and End Date/Time\": Allows selection of start and end Date/DateTime fields from the layer. Features will be shown whenever the time interval calculated from these fields overlaps the canvas time range

We should consider extending this in future, e.g. to add modes like \"start time + fixed duration\", \"start time + duration from field\", \"start and end time via expressions\", etc.

Quelques limites/inefficacités connues :
- Actuellement, seuls les champs Date/DateHeure peuvent être utilisés. Cela a été fait pour simplifier le traitement des formats et éviter de devoir se soucier des champs de chaîne avec différents formats de date et d'heure. À l'avenir, nous devrions permettre la sélection des champs de chaîne et permettre aux utilisateurs de saisir une chaîne de format DateTime personnalisée
- Unlike the Time Manager plugin approach, the approach taken here is to rely completely on QGIS expressions and feature requests to do the filtering (Time Manager uses layer filter strings and attempts to set a native SQL filter syntax so that filtering is done on the backend). This is intentional because it provides a unified filter approach regardless of the provider used (i.e. we don\'t need to worry about the different SQL syntaxes used natively by the different providers). The beauty of feature request expression compilation **should** mean that the QGIS expressions are magically turned into native backend queries, BUUUUUUUUUUUT\... because we lack QGIS expression support for DateTime literals, we currently rely on the \"to_datetime\" expression function and coerce everything through strings. None of the expression compilers handle this function, so currently \*all\* filtering is done on the QGIS side. We need to add functions for optimised DateTime literal creation and then ensure that the different compilers correctly map these literals across to the backend filter syntax to allow all the filtering work to be done on the database side\...

Ainsi, actuellement, les performances sont bien moins bonnes avec les grandes couches qu'avec le Time Manager (et l'ensemble des entites exposées est plus petit, par exemple pas de traitement d'interpolation) mais l'avantage est que nous pouvons utiliser le cadre temporel natif et avoir des couches vectorielles animées à côté des couches maille et raster !

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Support de l'API temporelle de Postgres raster
Ajout de l'intégration des capacités temporelles pour les rasters Postgres.

![image3](images/entries/78421839-37e3d100-765b-11ea-83e5-e7e3e519155e.webp)

![image4](images/entries/a8347da9570ae597bc17e23236e4eb4d57efb1d1.gif)

Cette fonctionnalité a été financée par ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Fonctionnalite : Paramètres temporels du projet QGIS
Cette fonction ajoute une fonctionnalité de paramétrage de la durée du projet.

You will be able to set the project temporal range either by using manual input or by calculating it from the current project\'s temporal layers. The latter can be done by clicking the provided \"Calculate from Layers\" button.

Cette implémentation ouvre la voie à l'ajout d'une fonction d'animation pour les couches temporelles dans QGIS.

Here\'s an example of setting the project temporal range. ![image5](images/entries/74980472-93f2ed00-5441-11ea-8765-f35d1f69b144.gif)

Prior discussions about QGIS temporal support can be found [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/161) and [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/128).

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Fonctionnalite : Prise en charge des contraintes temporelles des couches WMS-T
Cette fonctionnalité ajoute la possibilité de contraindre les couches WMS-T (WMS Temporal) à l'intérieur de QGIS. Vous pourrez limiter la plage de dates et d'heures pour n'importe quelle couche temporelle des fournisseurs de WMS-T.

Cette implémentation permet à l'utilisateur de spécifier la plage DateHeure requise sur la couche à partir de l'onglet source dans le dialogue des propriétés de la couche.

Below is an example of the workflow. ![image6](images/entries/74638436-ee0f5c00-517c-11ea-938e-cec23c61ba29.gif)

**Note:** *Pour les demandes de point instantané dans le temps, la spécification d'une plage avec une date et une heure de début et de fin égales entraînera l'utilisation de la date et de l'heure spécifiées et non d'une plage.*

![image7](images/entries/b86eea9111e33e6aea345b0e0759de48eaceade9.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Fonctionnalité : API temporelle
Cette fonctionnalité fournit une implémentation API pour le support temporel dans QGIS.

You can find the API for Python by searching for \'Temporal\' in the python docs ([link](https://qgis.org/pyqgis/master/search.html?q=Temporal&check_keywords=yes&area=default)).

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
## Outils cartographiques
### Fonctionnalité : outils Identifier pour les couches de tuiles vectorielles QGIS.
L'outil d'identification des cartes est maintenant capable d'inspecter les attributs des entités dans les tuiles vectorielles.

![image9](images/entries/79157425-d3501100-7dd4-11ea-8395-5c8ff1dce449.webp)

This feature was funded by [Many funders](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Affichage d'un menu à côté des boutons de widgets d'échelle, pour permettre de mettre le widget directement à l'échelle à partir d'une carte de mise en page imprimée
Un scénario dit mille mots :

![image10](images/entries/78198825-34bada80-74cd-11ea-803a-90afea085b38.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add tool button to \"Deselect Features from the Current Active layer\"
![image11](images/entries/76692569-26616780-6661-11ea-9071-fd4c712860db.gif)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Interface utilisateur
### Fonctionnalité : Permet le glisser-déposer d'une couche sur plusieurs instances QGIS
![image12](images/entries/77666018-b5834f00-6f80-11ea-971e-c6d7d996d37d.gif)

This feature was funded by [QGIS Swiss user group](https://www.qgis.ch)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalite : Ouvrez les tables d'attribut sous forme d'onglets
If the option \"Open new attribute tables as dock windows\" is active, new attribute tables will be opened as tabs on top of existing attribute tables.

![image13](images/entries/80049561-d8017d00-84d8-11ea-826e-d7092ac7a5c6.gif)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## Symbologie
### Fonctionnalite : Rendu des contours de la couche de trame
Ce nouveau moteur de rendu dessine des lignes de contour qui sont calculées à la volée à partir de la bande de trame source. Il est possible de définir l'intervalle des courbes de niveau et le symbole utilisé pour le dessin.

In addition there is support for \"index contours\" - contour lines with higher intervals, typically drawn with a wider line symbol.

If we generate contour lines on input raster blocks with the same size as our output raster block, the generated lines would contain too much detail. This detail can be reduced by the \"downscale\" factor - this will request lower resolution of the source raster.

![image14](images/entries/77861880-17111b00-7218-11ea-95ba-410c97830b93.webp)

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### Fonctionnalite : Ajout d'une unité de taille en pourcentage pour la symbologie des marqueurs d'images tramées et des couches de remplissage tramées.
According to the [Feature Request](https://github.com/qgis/QGIS/issues/30057) this patch adds a new percentage (of original image size) value for size units of **Raster Image Marker** and **Raster fill** (by [nirvn](https://github.com/qgis/QGIS/pull/34869#issuecomment-595090465) suggestion) layers.

Par exemple, une couche contient des images raster de différentes tailles et de différents ratios :

![image15](images/entries/77845535-6e3fcd00-71d1-11ea-8760-b477e75f7a3a.webp) ![image16](images/entries/77845539-726bea80-71d1-11ea-9512-0a8e6cde7b3c.webp)

Si nous utilisons un marqueur d'image Raster existant **unité de taille**, le calque ressemblera à ceci :

![image17](images/entries/77846711-bfec5580-71d9-11ea-9afe-a52af9b2784e.webp)

ou comme ça :

![image18](images/entries/77846764-1eb1cf00-71da-11ea-9d6d-f468708ea726.webp)

La nouvelle valeur de **pourcentage** des unités de taille est destinée à régler ce problème.

Both unit tests \"qgis_rasterfilltest\" and \"qgis_rastermarkertest\" were rewritten with a set of new control images for testing the proposed **percentage** value of size units.

This feature was developed by [beketata](https://api.github.com/users/beketata)
### Fonctionnalite : Ajout d'une propriété définie par des données à la famille/au style de police pour les marqueurs de police
Data-defined properties were added for the font markers\' font family and the brand new font style properties. This can come in handy for a number of scenarios, including multilingual context where a data-defined property can avoid duplicating datasets.

![image19](images/entries/1ded1a8bbec9eeebafad96b7616e963847961e14.webp)

Cette fonctionnalité a été financée par iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Fonctionnalite : Nouvelle définition du style de police pour les marqueurs de police
Grâce à ce tout nouveau paramètre de style de police, les utilisateurs peuvent choisir un style non par défaut parmi des familles de polices qui n'étaient pas disponibles auparavant.

![image20](images/entries/e387c3745d49a36116908dffc1126befae7d1b1f.webp)

Cette fonctionnalité a été financée par iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Étiquetage
### Fonctionnalite : Respecter les couleurs HTML dans les étiquettes
Lorsqu'elle est activée, cette option traite le contenu de l'étiquette comme du HTML, et toutes les options de formatage html liées à la couleur du fond seront respectées dans l'étiquette rendue.

Note: ONLY HTML COLOR TAGS ARE RESPECTED. This is NOT a bug, rather this feature has been designed as a \"test of the waters\" with HTML formatting in labels, and accordingly only formatting options which do not alter the font shape were considered.

Le côté positif est qu'il fonctionne correctement avec TOUS les autres paramètres des étiquettes, y compris les ombres, les tampons, les étiquettes courbes, etc !

Maintenant, quelques jolies photos :

![image21](images/entries/81377287-84359b80-9148-11ea-95f4-9d7917d62cf9.webp)

![image22](images/entries/81377294-88fa4f80-9148-11ea-9036-2a597b064bbc.webp)

This feature was funded by [geoProRegio AG](http://www.geoproregio.ch)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Placement automatique des étiquettes en dehors des polygones
Cette fonction ajoute la possibilité de placer automatiquement des étiquettes en dehors des polygones.

Cette situation est exposée de plusieurs façons :
1. A new placement mode which always places polygon labels for the layer outside the features: ![image23](images/entries/80680381-faf7e680-8b01-11ea-8612-b0f543bfd943.webp) ![image24](images/entries/80680391-00553100-8b02-11ea-8e56-21b57964f765.webp)
2. When using other polygon placement modes, a new checkbox \"Allow placing labels outside of polygons\" can be checked to allow labels to be placed outside when it isn\'t possible to place them inside the polygon: ![image25](images/entries/80680478-30043900-8b02-11ea-8bd5-3325fc0a5021.webp) ![image26](images/entries/80680488-37c3dd80-8b02-11ea-98bb-e0882e6ab9ab.webp)

The \"allow placing labels outside\" checkbox can be data defined, allowing users to either allow outside labels, prevent outside labels, or force outside labels on a feature-by-feature basis.

The placement algorithm is based on a modification of Rylov & Reimer (2016) \"*A practical algorithm for the external annotation of area features*\". While Rylov & Reimer propose a horizontal sweep-line based approach for selection of candidate label points, in practice I found that this delivered inferior results (and was slower) then just traversing the exterior ring of the polygon and generating candidate point at regular intervals (especially for narrow, nearly horizontal polygons).

As shown in the islands screenshot above, the outside placement mode works as expected with the \"Follow label placement\" multiline alignment mode.

This feature was funded by [Swiss QGIS user group](https://www.qgis.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Couche de tuiles vectorielles - partie 4 (étiquetage)
Poursuite des travaux sur la mise en œuvre de la couche de tuiles vectorielles.

This adds labeling support for vector tile layers. So far this is just working on qgis_core\... GUI support will come next. Labeling uses the same concepts as the rendering of vector tiles: we have a list of labeling styles, each one is defined by sub-layer name, geometry type, filter expression, zoom range and of course label style configuration (QgsPalLayerSettings).

Note there is a \"chicken-and-egg problem\" with labeling: For vector tiles, we create QgsFields for a sub-layer based on fields that renderer and labeling request, but with labeling it was impossible to get required fields if they were not already available in the expression context (hence some small additions to QgsProperty, QgsPropertyCollection, QgsPalLayerSettings to be able to get required field names by not preparing internal expressions at the same time).

![image27](images/entries/78723460-bf676380-792b-11ea-9cab-a6732e20033a.webp)

An example how to set the above labeling in Python console:

    s = QgsVectorTileBasicLabelingStyle()
    s.setLayerName("place")
    s.setGeometryType(QgsWkbTypes.PointGeometry)
    s.setFilterExpression("rank = 1 AND class = 'country'")
    ls=QgsPalLayerSettings()
    ls.drawLabels=True
    ls.fieldName="name"
    ls.placement = QgsPalLayerSettings.OverPoint s.setLabelSettings(ls)
    labeling = QgsVectorTileBasicLabeling()
    labeling.setStyles([s])
    iface.activeLayer().setLabeling(labeling)
    
This feature was funded by [Many funders](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Ajout d'un contrôle sur le point d'ancrage de l'appel sur l'étiquette
Cela permet aux utilisateurs de contrôler l'endroit où un message doit se joindre au texte de l'étiquette (auparavant, vous ne pouviez contrôler que l'endroit où le message se joindrait à la géométrie de l'élément correspondant).

Les choix comprennent :
- Point le plus proche (comportement antérieur)
- Centroïde étiquette  
- Des coins fixes : En haut à gauche/en haut à droite/en bas à gauche/en bas à droite/etc

Un contrôle défini par les données sur l'ancrage de l'étiquette est également possible.

Aide à remédier à la laideur de certains appels !

Résultat précédent (mode point le plus proche) :

![image28](images/entries/76173692-5a660400-61ed-11ea-87dd-74a4db5cf0ce.webp)

With new \"centroid\" placement:

![image29](images/entries/76173706-6d78d400-61ed-11ea-89c1-ce4e2477dfef.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Mesh
### Fonctionnalite : Utiliser uniquement le groupe de données spécifié
Cette fonction permet à l'utilisateur de choisir les groupes d'ensembles de données qui sont utilisés. Cela peut être fait dans le dialogue des propriétés de la couche de maillage dans l'onglet source.

Une nouvelle vue arborescente affiche tous les groupes d'ensembles de données disponibles du fournisseur de données. Les groupes de données peuvent être vérifiés/dévérifiés et renommés.

Ce widget propose également des boutons permettant de charger des groupes de données supplémentaires à partir de fichiers, de développer/réduire l'arborescence, de vérifier/décocher tous les éléments et de réinitialiser les valeurs par défaut du fournisseur (pour l'instant, seul le nom original).

Seul le groupe d'ensembles de données coché sera affiché dans le widget d'ensemble de données actif dans les paramètres du moteur de rendu.

![image30](images/entries/81516813-3a46e400-9307-11ea-9621-a27d5a8c86f2.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Réglages de couleurs scalaires en fonction de la classification
Grâce à cette fonction, MDAL lit les valeurs scalaires classées dans l'ensemble de données. Lorsque les valeurs sont classées, les paramètres de rendu scalaire par défaut comportent le nuanceur de rampe de couleurs et les étiquettes définies en fonction des valeurs classées.

![image31](images/entries/81480226-42fbc500-91f6-11ea-91fd-3d430693d551.webp)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Des éléments de maillage à accrocher
Ajoute à l'API une méthode permettant d'accrocher des éléments de maillage.

La méthode retourne la position du point de rupture sur l'élément de maille le plus proche :
- Pour un vertex, la position d'accrochage est la position du vertex
- Pour un bord, la position d'enclenchement est le point projeté sur le bord, ou l'extrémité du bord si elle se trouve à l'extérieur du bord
- Pour un visage, la position derupture est le centroïde du visage

La position retournée est en coordonnées cartographiques.

![image32](images/entries/f11b278c71fecee8445ff29077bfddef543b564d.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionalite : Largeur de maille 1D/couleur variable
Cette fonctionnalité offre une nouvelle façon de rendre un maillage 1D avec des largeurs de bord qui peuvent varier en fonction de la valeur. Désormais, la largeur et la couleur varient en fonction de la valeur des bords ou des sommets.

L'utilisateur peut définir la valeur min/max et la largeur min/max pour définir le rendu.

Pour la couleur, l'utilisateur peut définir un nuanceur de rampe de couleur (comme pour le maillage 2D et le raster).

Pour ce nouveau rendu, de nouvelles classes génériques sont introduites qui pourraient être utilisées en dehors du cadre du maillage.

![image33](images/entries/80013358-bb475400-849c-11ea-95c8-71b04382a927.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Prise en charge des maillages multiples (depuis MDAL 0.5.91)
En plus de la mise à jour vers MDAL 0.5.91, cette fonctionnalité permet de charger plusieurs maillages à partir d'un seul fichier.

Le fichier est analysé et un dialogue de sous-couche est lancé en utilisant la même logique que pour les couches vectorielles ou raster.

![image34](images/entries/78789841-b1413380-797b-11ea-9c7b-f31cb9756809.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Connecter la couche de maillage au cadre temporel  QGIS
![image35](images/entries/77872855-31e29000-7216-11ea-80fb-82e351dbb4a2.gif)
#### Gestion du temps dans la couche de maillage
Le temps dans une couche de maillage est défini par :
- Un temps de référence fourni par les données, le projet ou l'utilisateur
- Chaque ensemble de données est associé à des temps relatifs
- L'étendue temporelle est définie par la première et la dernière fois de tous les ensembles de données

```
    Reference time :          AT
    Dataset 1 time            o---RT------RT-----RT-----------RT
    Dataset 2 time            o-------RT------RT--------RT
    Dataset 3 time            o--------------------------RT-------RT------RT
    Time extent of layer      o----<---------------------------------------->

    -  AT : absolute time (QDateTime)
    -  RT : relative time (qint64)
```
La classe **QgsMeshDataprovidertemporalCapabilities** stocke le temps de référence fourni par les données et tous les temps relatifs de l'ensemble de données. Cette classe a la capacité de renvoyer l'index de l'ensemble de données à partir d'un index de groupe d'ensembles de données et d'un temps relatif depuis le temps de référence. Le temps de référence (qui peut être différent du temps de référence du fournisseur) et l'étendue temporelle absolue sont stockés dans la classe **QgsMeshTemporalProperties**.

The temporal settings in the properties widget are only the reference time and the provider time unit: ![image36](images/entries/77871643-bf23e580-7212-11ea-9b92-82c906c19c22.webp)

Le temps de référence par défaut de la couche est défini par (trié par priorité) :
- Du fournisseur de données si elles sont définies dans les données
- Du projet s'il est défini
- De la date actuelle à l'heure 00h00

L'utilisateur peut le modifier s'il le souhaite.
#### Principe de rendu
The 2D and 3D renderers access the active dataset index from the layer with the time range stored in the `QgsContextRenderer` and in the `Qgs3DMapSettings` : Relative time is calculated as the difference between the time range of `QgsContextRenderer` and the reference time stored by `QgsMeshTemporalProperties`. The dataset index comes from the `QgsMeshDataproviderTemporalCapabilities` that maps the relative time with dataset index.

Les données sont apportées par le fournisseur avec l'index de l'ensemble de données.
#### Ensemble de données statiques
There is also the option to set a static dataset, that is to choose a dataset that will be rendered independently of the QGIS time controller. To do that the user can check the check box at the bottom of the temporal page of the properties widget: ![image37](images/entries/77871772-20e44f80-7213-11ea-8988-a51ec78c1320.webp) For now, as it was simpler to implement and allows the required dataset to be chosen directly, the user can independently choose scalar dataset and vector dataset from combo boxes with the time associated for each dataset (relative time for data without reference time). If required, a unique time could be implemented but that could lead to inconsistent results with non synchronous datasets. The static dataset settings are in the temporal page but can be easily put in the source page if wanted.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Rééchantillonnage des valeurs des sommets vers les valeurs faciales
Le rééchantillonnage est disponible pour les ensembles de données définis sur les faces, par exemple la valeur sur les sommets est calculée à partir des valeurs sur les faces.

Cette fonction met en œuvre le rééchantillonnage des valeurs sur les sommets aux valeurs sur les faces en utilisant la méthode de la moyenne du voisin.

The default method is set to \"none\" for resampling from vertices to faces and to \"neighbor average\" for resampling from faces to vertices. Then the default rendering is always smooth. ![image38](images/entries/77320848-acc41c00-6ce7-11ea-85af-2bff553ecbb5.gif)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fontionnalite : Jeu de données de vecteurs de maillage coloré avec nuanceur de rampe de couleur
Cette fonction permet à l'utilisateur de colorer le jeu de données vectorielles de la couche de maillage (flèche, lignes de courant, traces) avec le nuanceur de rampe de couleurs en fonction de l'amplitude du vecteur.

![image39](images/entries/77156534-ed1c6380-6a75-11ea-8b97-a13d3ea27ede.webp)

![image40](images/entries/77156669-2c4ab480-6a76-11ea-9209-d0144fbfc3f0.webp)

![image41](images/entries/77156736-5bf9bc80-6a76-11ea-827b-bb55ce52b814.webp)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Sauvegarder le style pour la couche de mailles
Cette fonctionnalité ajoute la possibilité d'enregistrer un style de couche de maillage dans un fichier qml, tel qu'il est utilisé pour les couches vectorielles et raster.

The feature also refactors the raster and vector layer properties menu style. ![image42](images/entries/76421493-1fdda200-637a-11ea-9e4b-71a596b18dd9.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : rendu des mailles 1D
Update to [MDAL 0.5.90](https://github.com/lutraconsulting/MDAL/releases/tag/0.5.90)

Initial implementation of [Support of 1D elements in Mesh Layers](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/164)

Les mailles 1D sont constituées de sommets et d'arêtes. Une arête relie deux sommets et peut comporter des données (scalaires ou vecteurs) qui lui sont affectées. Le réseau de maillage 1D peut, par exemple, être utilisé pour la modélisation d'un système de drainage urbain.

There are new options to display 1D mesh (edges) in the mesh frame tab ![image43](images/entries/75885078-2aea7c80-5e26-11ea-8435-eef74afce7b7.webp)

Pour les données sur le maillage 1D (bords ou sommets), il existe également de nouvelles options dans l'onglet "Contours"

![image44](images/entries/75885122-3b9af280-5e26-11ea-96a3-f4a4e48c040e.webp)

Notez que toutes les fonctionnalités disponibles pour les maillages 2D ne sont pas disponibles, notamment
- Soutien au calculateur de mailles pour les mailles 1D
- Rendu 3D des maillages 1D
- Identifier et tracer les graphiques (sera ajouté plus tard dans le PR suivant)

Certaines fonctions ne sont pas nécessaires pour les mailles 1D, notamment
- Exportation des contours des mailles

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Fonctionnalite : Simplification des mailles
Comme une couche de maillage peut comporter des millions de triangles, le rendu peut être très lent, d'autant plus que tous les triangles sont affichés dans la vue même lorsque les triangles sont trop petits pour être vus.

Pour ces situations, cette fonction offre une option permettant de simplifier le maillage. La simplification conduit à un ou plusieurs maillages simplifiés qui représentent des niveaux de détail. Lors du rendu du maillage, le niveau de détail approprié est choisi pour fournir un rendu adéquat en fonction de la vue.

Un nouvel onglet dans le widget des propriétés de la couche de maillage permet à l'utilisateur de modifier les paramètres :
- Le facteur de réduction est utilisé pour simplifier un maillage ; le nombre de triangles pour chaque niveau de détail est approximativement égal au nombre de triangles du niveau de détail précédent, divisé par le facteur de réduction
- Résolution maximale du maillage : il s'agit de la taille moyenne (en pixels) des triangles qui peuvent être affichés ; si la taille moyenne du maillage est inférieure à cette valeur, un maillage avec un niveau de détail inférieur est affiché, c'est-à-dire un maillage avec une taille moyenne juste supérieure à la résolution maximale du maillage.

![image45](images/entries/74750757-9e936380-5242-11ea-98cf-a0e3e6694831.webp)

This feature allows the speeding up of rendering as shown in these tables (result in milliseconds) : ![image46](images/entries/74750903-d69aa680-5242-11ea-9be3-0af7b2beacaf.webp)

Demo GIF Before: ![image47](images/entries/74751034-0cd82600-5243-11ea-8a02-de78a337f299.gif)

After: ![image48](images/entries/74751042-12357080-5243-11ea-80cb-2a3217d03a78.gif)

This feature was funded by [BMT](https://www.bmt.org/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Fonctionnalités 3D
### Fonctionnalite : Flèches pour le rendu des ensembles de données de la couche de maillage 3D
Cette fonctionnalité ajoute une option permettant d'afficher des flèches sur une entité 3D d'un ensemble de données de la couche de maillage, en fonction de l'ensemble de données vectorielles.

Le jeu de données utilisé pour le rendu des flèches est celui qui a été choisi pour le rendu des vecteurs en 2D.

De la même manière, la couleur des flèches est définie dans les paramètres de rendu 2D pour l'ensemble des données vectorielles.

Dans les paramètres 3D, l'utilisateur peut définir l'espacement des flèches et si la taille est fixe ou mise à l'échelle en fonction de la magnitude.

This spacing setting also defines the maximum size of arrows because arrows can\'t overlap. ![image49](images/entries/76225819-6a80e200-61f3-11ea-88da-43e70c358530.webp)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Mises en page de cartes
### Fonctionnalite : Paramètres temporels pour les éléments de la  mise en page
Cette fonctionnalité ajoute une section repliable au widget d'élément de carte de présentation qui permet aux utilisateurs d'activer et de définir une plage temporelle à utiliser lors du rendu du contenu de la carte.

La date et l'heure de début et de fin peuvent être définies par des données, ce qui est pratique lorsqu'elles sont utilisées avec les fonctions de l'atlas.

![image50](images/entries/265d07738c1cec8a398ce5503330a520f98d4526.gif)

Cette fonctionnalité a été financée par iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Fonctionnalite : Permet de trier la table d'attributs par champ non répertorié dans le tableau
Au lieu d'utiliser le même modèle de données pour les colonnes d'affichage et de tri, deux modèles de données sont désormais utilisés. Ils utilisent la même API / classe de base car ils sont très similaires.

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalite : Exposer le contrôle sur le comportement de division des légendes des couches, couche par couche
This allows users to manually override the legend\'s default setting for \"split layers\" on a layer-by-layer basis, by double clicking a layer in the layout legend panel and choosing whether that layer:
- Suit le paramètre de légende par défaut pour le fractionnement
- Can ALWAYS be split over multiple columns (regardless of the legend\'s setting)

ou
- Can NEVER be split over multiple columns (regardless of the legend\'s setting)

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permet la personnalisation des symboles de division et de subdivision par rapport au symbole horizontal de la barre d'échelle à cocher
Permet de styliser les symboles de division et de subdivision d'une manière différente par rapport au symbole de ligne horizontale dans une barre d'échelle 

Parrainé par  SLYR

Builds off the hard work done by \@agiudiceandrea!

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permet de remplacer le symbole par défaut d'un nœud de légende
This allows users to (optionally) customise the symbol appearance for a legend node, e.g. to tweak the colors or symbol sizes to better provide a \"representative\" patch symbol compared with how those corresponding features actually appear on the map.

It\'s useful for exaggerating symbol widths, or for manually tweaking the colors of semi-transparent symbols so that the colors represent the actual appearance of the symbols when rendered on top of the map content. Or to tweak the marker interval/offset in marker lines so that the markers are nicely spaced in the legend patch.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permettre de placer des coupures de colonne manuelles dans les légendes
Ajoute la possibilité, lors de la configuration d'un élément de légende, de placer un saut de colonne avant l'élément, ce qui fait qu'il est placé dans une nouvelle colonne.

This allows user control over the column content, for cases when the automatic column generation doesn\'t result in the desired results.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout de subdivisions dans les segments de droite de la barre d'échelle
Ajoute la possibilité de créer des subdivisions pour les segments inclus dans la partie droite de la barre d'échelle.

Line Ticks Up ![image51](images/entries/80860629-47116b00-8c69-11ea-83d8-61f27cb77e68.webp)

Line Ticks Middle ![image52](images/entries/80860663-6c9e7480-8c69-11ea-94a3-8d0e8544867d.webp)

Line Ticks Down ![image53](images/entries/80860675-7b852700-8c69-11ea-984d-584eff1e3c95.webp)

Scalebar item properties - Segments groupbox ![image54](images/entries/81009703-653bbe80-8e55-11ea-9286-4850b32edb23.webp)

Le comportement lié aux segments du côté gauche de la barre d'échelle est inchangé.

This feature was developed by [Andrea Giudiceandrea](https://api.github.com/users/agiudiceandrea)
### Fonctionnalite : Permet de modifier la taille des patchs de la légende
Permet aux utilisateurs d'ignorer la taille du patch de symbole pour les nœuds de légende individuels, en double-cliquant sur le nœud

Width and height can be individually overridden, with the node falling back to the default width or height when the override isn\'t set.

Sponsored by SLYR ![image55](images/entries/80325577-0edce780-8879-11ea-82bd-8f323a4c68ab.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permet de contrôler l'espacement horizontal avant les groupes/sous-groupes/symboles de la légende
Gives flexibility to allow \"nesting\" legend groups/subgroups/symbols and much greater control over legend item placement.

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Gérer les formes des patchs de légende grâce au gestionnaire de style
Cette mise à jour finalise le récent travail de personnalisation des formes de patchs de légendes, en ajoutant la prise en charge des formes de patchs de légendes personnalisées au gestionnaire de style !

Maintenant, il ne nous reste plus qu'à expédier un très bel ensemble de formes de patchs par défaut !

![image56](images/entries/79927419-0c4a4e80-8483-11ea-9b87-7ed8b393d349.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permet de configurer les formes des patchs de légende en double-cliquant sur les éléments de la légende
Permet aux utilisateurs de définir des formes de patchs de légende personnalisés pour des objets en entrant une chaîne WKT représentant la géométrie du patch.

Parrainé par  SLYR

![image57](images/entries/79714030-ea31be80-8312-11ea-8b6f-f40e3eea04b1.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Possibilité de coller des images directement dans les mises en page
Intègre l'image collée dans la mise en page.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite: Permettre aux marqueurs de synchroniser leur rotation avec les cartes
Cela permet de créer des flèches du nord à partir de symboles de marqueurs, exposant les mêmes options que celles qui existent pour les éléments d'image faisant office de flèches du nord.

Lorsqu'un marqueur agit comme une flèche du nord, la rotation de la carte est AJOUTÉE à toute rotation de symbole de marqueur existante (par exemple, si vous devez faire pivoter le marqueur triangulaire de 90 % pour le faire pointer vers le haut, il fonctionnera toujours bien en mode flèche du nord !)

![image58](images/entries/78468312-2c2b0400-775a-11ea-926e-2acf7ec15aa4.webp)

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Dossier : Nouveau type pour les symboles de marqueurs
Permet de placer des symboles de marqueurs directement sur les mises en page, par exemple pour placer manuellement des marqueurs sur un élément de carte ou pour créer des légendes personnalisées avancées.

Auparavant, vous deviez pirater le support de ces derniers, par exemple en dessinant des rectangles à l'aide de symboles de remplissage centroïdes. Il est beaucoup plus agréable d'avoir un type dédié pour cela, ce qui permet des options de personnalisation plus spécifiques (bientôt !)

Parrainé par  SLYR

![image59](images/entries/78419618-c885d580-768a-11ea-959a-8459e19e05df.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout d'un contenu d'importation à partir du presse-papiers pour les éléments de table fixes
A new import content from clipboard feature has been added to QGIS\' table editor to enable quicker layout fixed table item editing and creation.

![image60](images/entries/e7f2b64e48b0726bc03e2d4fa9424feabde1808d.gif)

Cette fonctionnalité a été financée par iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Feature: Add numeric formatter \"fraction\" style
This style represents decimal numbers as vulgar fractions, e.g. \"3/4\" instead of 0.75.

Options include using Unicode superscript and subscript characters for nicer typography, e.g. ¹⁷/₂₃ (this is the default mode, disabling this option uses the \"17/23\" format). An option also exists for using dedicated unicode characters for specific fractions (where a unicode character exists), e.g. ½ or ¾.

Ultimately this allows for creation of scalebars with fractional representations of distances, e.g. 0 \-\-\-\-- ½ \-\-\-\-- 1 km (instead of 0 \-\-\-\-\-- 0.5 \-\-\-\-\-- 1km)

Parrainé par  SLYR

![image61](images/entries/77267662-0c71f580-6cef-11ea-9956-917e1d6ef496.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"stepped line\" and \"hollow\" scalebar styles
Ajoute deux nouveaux styles de barres d'échelle (qui sont disponibles dans ArcMap, mais auparavant impossibles à reproduire dans QGIS)

Style de ligne en escalier :

![image62](images/entries/77247015-c1b59680-6c78-11ea-92a9-7bbb2ba8638a.webp)

Hollow (aka \"South African\") style:

![image63](images/entries/77247024-dc880b00-6c78-11ea-827a-344645cec248.webp)

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permet de définir le style de ligne de la barre d'échelle à l'aide de symboles de ligne QGIS standard
Au lieu des réglages précédents des styles de couleur/largeur/capuchon des lignes de la barre d'échelle, nous exposons maintenant l'option comme symbole de ligne complète pour un style plus avancé.

Egalement quelques nettoyages de code.

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite: Retravailler l'image 
Adds an explicit choice between SVG or raster image sources, which allows us to clean up the configuration panel for layout pictures by hiding options which don\'t apply to a certain picture source. Also permits us to:
- Réutiliser le widget standard d'arbre de sélection SVG, qui charge les images dans un fil de discussion en arrière-plan
- Utilise le SVG standard et l'édition de ligne du sélecteur d'images, qui permet le glisser-déposer d'images et expose des options pour intégrer des images et établir des liens avec des sources en ligne

En fin de compte, cela est motivé par le désir de permettre aux utilisateurs d'intégrer des images dans les mises en page et les modèles de présentation

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Rendre le CRS contrôlable par une variable
Cela rend le CRS de la carte contrôlable par une variable.

![image64](images/entries/74844265-348ac500-52fb-11ea-9198-78f4f9022ac1.webp)

Related to #34547

This feature was developed by [Alex](https://api.github.com/users/roya0045)
## Expressions
### Fonctionnalité: Nouvelles expressions
- `ascii`
- `make_interval` Allows direct construction of interval values from years/months/weeks/days/hours/minutes/second values, without having to construct a string representation of the interval first
- `maptip`
- `layer_property('distance_units')`
- `display_expression`
- `eval_template`
- `make_date`
- `make_time`
- `make_datetime`
- `close_line`
- `is_multipart`
- geometry Z and M minimum and maximum
- `@frame_number`
- `@frame_rate`
- `@frame_duration`
- `@map_start_time` Start of the map\'s temporal time range (as a datetime value)
- `@map_end_time` End of the map\'s temporal time range (as a datetime value)
- `@map_interval:` Duration of the map\'s temporal time range (as an interval value)
- `@animation_start_time`
- `@animation_end_time`

Cette fonctionnalité a été développée par Etienne Trimaille, Jan Caha, Julien Monticolo, Nyall Dawson
### Fonctionnalite : Navigateur d'entites pour la prévisualisation dans le générateur d'expressions
This adds a feature browser to the expression builder so one can browse features to see the result of the expression ![image65](images/entries/80604352-e6e4b400-8a31-11ea-8f3b-8c864e124c78.webp)

A new widget is added: `QgsFeaturePickerWidget`. For the moment, it\'s a simple combobox (but inherits widget so we can add a map picker button later on). It behaves the same way than the one in the relation reference widget (an editable combobox).

It relies on the same base model (`QgsFeatureFilterModel`). A new abstract class `QgsFeaturePickerModelBase` regroups the logic of the, and the new model is called `QgsFeaturePickerModel`. Basically the `QgsFeaturePickerModel` used the feature id to identify the features while `QgsFeatureFilterModel` use a list of attributes (the foreign keys of a relation). It declutters a bit the former model which was quite\...cluttered.

As a side note, I tried to use templates for `QgsFeaturePickerModelBase`, but since templates cannot be mixed with Q_OBJECT, the alternatives sounded like the code would be less readable.

Des tests ont été ajoutés.

Sponsored by the **QGIS Swiss User Group**!

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalite : Possibilité de supprimer des fonctions personnalisées
Ajout d'un bouton de suppression dans l'onglet Éditeur de fonctions du dialogue de création d'expression pour permettre la suppression des fonctions utilisateur de QGIS sans avoir besoin de naviguer dans le répertoire du profil utilisateur.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Ajout de la possibilité de modifier, d'importer et d'exporter des expressions d'utilisateurs
A new button is added that allows editing of saved expressions. It is only active when a user expression is selected in the expressions tree. When pressed, it opens a window that allows the currently selected user expression to be edited. Changing the label of the expression makes a copy of the currently existing one. [Demo](https://imgur.com/w3UEOoR)

**Import/Export**

A new button with a menu is added, that allows the import/export of user expressions to/from a JSON file. Clicking on either of the menu entries opens a file selector dialog for the expressions JSON file source/destination. In the case of label conflicts, an additional dialog asks how to proceed - either to overwrite or to skip the current expression. [Import/Export Demo](https://imgur.com/0eiaFfu)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Numérisation
### Fonctionnalite : Mode dédié d'évitement des intersections et des chevauchements géométriques
Cette version de QGIS est dotée d'un nouveau mode dédié permettant d'éviter les intersections et les chevauchements géométriques lors de la numérisation d'éléments.

| The three available modes are:

|

Autoriser les intersections/recouvrements

|

Éviter les intersections/recouvrements sur la couche active

|

Éviter les intersections/recouvrements sur la liste des couches définie par l'utilisateur.

|

The third mode\'s layers list is setup by the user via the advanced snapping configuration widgets.

![image66](images/entries/caa646295d6f1cf6297864810637e9f8ceddc102.webp)

This feature was funded by [OpenGIS.ch](http://www.opengis.ch/)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Fonctionnalité : Nouveaux modes d'accrochage : Centroïde et milieu d'un segment (midpoint)
This feature is aimed at improving [snapping modes in QGIS](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/107) by getting closer to the experience of CAD tools.

Il ajoute deux nouveaux modes. L'accrochage sur le centre d'une géométrie (centroïde) et le milieu d'un segment.

Pour permettre la sélection de ces nouveaux modes, plusieurs modes d'accrochage peuvent être sélectionnés en même temps.

![image67](images/entries/71798125-35201280-3051-11ea-959d-a5897ca3391a.webp)

L'ordre de préférence pour l'accrochage est le suivant : - Sommet, intersection - Milieu - Centroïde - Bord - Surface

![image68](images/entries/71799417-7e726100-3055-11ea-8e07-3792dbc741c2.gif)

Sponsored by: Qwat group / Ville de Lausanne ( \@ponceta \@dsavary ) / Oslandia and some spare time

This feature was developed by [lbartoletti](https://api.github.com/users/lbartoletti)
### Fonctionnalite : Le passage à l'élément actuellement numérisé
Le snapping peut désormais également prendre en charge le snapping de l'élément en cours de numérisation. Cette option est activée/désactivée par un nouveau bouton dans la barre d'outils d'accrochage.

This enables some really nice CAD-like editing abilities, such as closing features at a 90° angle or precisely aligning segments inside a feature. It\'s very efficient once one is accustomed to using the alt+a shortcut to lock the angle.

![image69](images/entries/81065380-a37bc100-8edb-11ea-8aed-6fd52d843a26.gif)

Cette fonctionnalité a été financée par Kanton Solothurn et Land Vorarlberg

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Fonctionnalite : Le traçage prend désormais en charge les géométries courbes
L'outil de traçage crée maintenant des géométries courbes lorsqu'on travaille sur une couche qui supporte des géométries courbes.

![image70](images/entries/79769829-e3b04080-832c-11ea-9029-981e3a3ecf1b.gif)

Le support est encore expérimental, cette fonctionnalité doit donc être activée dans les options de numérisation.

Cette fonctionnalité a été financée par ecoptima et Planteam

This feature was developed by [Olivier Dalang (OPENGIS.ch)](https://api.github.com/users/olivierdalang)
## Formulaires et widgets
### Fonctionnalite Permettre l'édition des liens dans le widget de fichier
Dans un formulaire, les liens peuvent maintenant être édités dans le widget fichier (lorsque le widget n'est pas en lecture seule).

![image71](images/entries/81038564-bcb64a80-8ea6-11ea-8289-46340dee9a88.gif)

Sponsored by the QGIS Swiss user group

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalite : Étiquettes à expression contrôlée (alias)
Cette nouvelle fonctionnalité permet d'évaluer les étiquettes de formulaire (alias) dans le contexte du formulaire.

![image72](images/entries/78998144-46912300-7b48-11ea-9fbf-232d11fbeff6.webp)

![image73](images/entries/78904645-26486200-7a7d-11ea-84b0-b9e96c0c9797.gif)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalite : Ajouter une description au widget de relation de valeur
Ajoute une option permettant d'ajouter une description à chaque valeur dans un widget de valeur de relation. La description apparaîtra sous forme d'info-bulle

Veuillez excuser les différentes langues dans la vidéo de démonstration.

![image74](images/entries/76538031-f195ba80-647e-11ea-9a41-271576e315bc.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Fonctionnalite : Nouveau widget de nom de table de base de données
Un nouveau widget a été ajouté à QGIS pour sélectionner une nouvelle table à partir d'une connexion DB existante :

![image75](images/entries/76504669-70233580-6448-11ea-9194-173ae0d344ce.gif)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Fonctionnalite : Obtenir les valeurs actuelles des formulaires parents dans les formulaires enfants
This feature adds the option of using current values from the \"parent\" form in filter expressions (for now only in value-relation widgets: to be used in drill-down filters).

A new \"parentForm\" scope was added as well as a new set of functions and variables to access the parent from within an embedded child form. The new functions and variables were modelled on the existing \"current_value\", \"current_feature\" etc.

The new functions and variables are also available when the parent form is opened from a new (unsaved, unbuffered) feature, making it easier to create drill-down filters based on the parent\'s values when adding children from an unsaved parent form.
### Exemple
![image76](images/entries/75692656-28f9af80-5ca6-11ea-8dd6-9a4bf454f5b7.gif)
### Nouvelles fonctions et variables
![image77](images/entries/75693398-2ba8d480-5ca7-11ea-8be0-9643f8841c89.webp) ![image78](images/entries/75693402-2cda0180-5ca7-11ea-9d65-f0c00e26180e.webp) ![image79](images/entries/75693404-2d729800-5ca7-11ea-889d-5aa73bc131ce.webp)

Financée par: **ARPA Piemonte**

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalite : Widget relationnel : ajout d'une case à cocher pour cacher le bouton de sauvegarde des modifications de l'enfant
Cela est très utile pour les formulaires intégrés.

Financée par: **ARPA Piemonte**

![image80](images/entries/75524592-82e04800-5a0e-11ea-9333-461a0d02a1c0.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalite : La force du widget relationnel supprime les popups
Ajoute une option à la configuration du widget de relation pour supprimer le popup de formulaire ouvert lorsque de nouvelles fonctionnalités sont ajoutées dans un contexte de formulaire intégré.

Cette option a priorité sur l'option au niveau du formulaire (ce qui pourrait encore être le comportement souhaité lorsque le formulaire est utilisé comme un formulaire autonome).

![image81](images/entries/75249972-9786cb00-57d7-11ea-8100-3426d32831db.webp)

Note : l'étiquette finale est **Force hide form on add feature**

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
## Légende des couches
### Fonctionnalite : Ajout du déplacement vers le bas dans le menu contextuel de l'arborescence des couches
Le déplacement des couches sur les grands projets a été facilité par l'option *Move to top*, mais il fallait toujours déplacer manuellement les cartes de base vers le bas de la liste des couches, une tâche encombrante dans les grands arbres de couches. Cette fonctionnalité ajoute une option *Move to bottom* au menu contextuel de l'arbre des calques qui fonctionne de la même manière que Move to top.

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Feature: Make Add Group button act as Group Selected if selected layers \>= 2
When there is more than one layer selected and the user presses the *Add Group* button, create a new group and put the selected layers in it too! ![image82](images/entries/76710403-f624d200-670f-11ea-9a41-13420c7940e3.gif)

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Fonctionnalite : Permet de renommer le thème actuel de la carte
Cela ajoute la possibilité de renommer un thème de carte à partir du menu déroulant des thèmes de carte.

![image83](images/entries/78195435-e29f9800-747f-11ea-95d2-604be58cf229-1.gif)

This feature was developed by [Harrissou Sant-anna](https://api.github.com/users/DelazJ)
### Feature: Turn on/off ALL selected layers with \"Space\" button
Toggles the visibility of the currently selected layers or groups using the space button: ![image84](images/entries/77874799-cff64a80-7256-11ea-974b-c4084d1e01ae.gif)

This feature was developed by [Ivan Ivanov](https://github.com/suricactus)
## Outils d'analyse
### Fonctionnalité : Logger réseau - fonctionnalités supplémentaires
Ajoute des outils plus utiles pour le logger de réseau :
- Copier l'URL
- Copier la demande en tant que JSON
- Enregistrer le log dans un fichier (après avoir averti les utilisateurs que le log peut contenir des informations sensibles et doit être traité de manière confidentielle)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Outil intégré de log du réseau
This tool, which is available from the new F12 \"dev tools\" panel, is a native port of \@rduivenvoorde\'s network logger plugin.

Il affiche une liste des demandes de réseau en cours et terminées, ainsi que toute une série de détails utiles comme l'état des demandes et des réponses, les en-têtes, les erreurs, les erreurs de configuration SSL, les délais d'attente, l'état du cache, etc.

Il possède également de nombreuses fonctionnalités utiles, telles que la possibilité de filtrer les demandes par sous-chaîne d'URL et par statut, et vous pouvez cliquer avec le bouton droit de la souris sur les demandes pour ouvrir l'URL dans un navigateur ou les copier sous forme de commande cURL.

Pourquoi voulons-nous que ce soit un outil natif plutôt qu'un plugin ? Eh bien :
- It\'s extremely useful, so is nice to have available out-of-the-box
- En le déplaçant vers c++, nous pouvons démarrer le processus de journalisation beaucoup plus tôt. Cela permet au journal d'inclure des informations supplémentaires, telles que les demandes déclenchées par d'autres plugins qui se produisent avant que le plugin d'enregistrement du réseau n'ait été chargé (ainsi que d'autres demandes intégrées, par exemple le fil d'actualité)
- La performance a été une lutte constante avec le plugin Python. Bien qu'il s'agisse d'un port 1:1 aussi proche que possible, les problèmes de performances ont tous été résolus comme par magie. Les classes ont des opérations de liste très intensives, ce qui est probablement la cause des mauvaises performances sous Python.

![image85](images/entries/77712469-95ef3380-701f-11ea-8fec-3eded258b4e9.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Nyall Dawson (for Kartoza)](https://api.github.com/users/nyalldawson)
## Traitement
### Fonctionnalité : Collection d'algorithmes de génération de trames raster aléatoires
Avec cette fonctionnalité, nous avons ajouté une grande collection d'algorithmes de génération de trames raster aléatoires. Ces algorithmes sont capables de produire des trames aléatoires suivant des distributions de nombres aléatoires spécifiques. Les distributions suivantes sont disponibles :
1. Créer une couche raster aléatoire (distribution binomiale)
2. Créer une couche raster aléatoire (distribution exponentielle)
3. Créer une couche raster aléatoire (distribution gamma)
4. Créer une couche raster aléatoire (distribution binomiale négative)
5. Créer une couche raster aléatoire (distribution normale)
6. Créer une couche raster aléatoire (distribution poisson)
7. Créer une couche raster aléatoire (distribution uniforme)

![image86](images/entries/6304472935d29f8292cf24c7cb0198e95a4de137.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Fonctionnalité : Couche de tuiles vectorielles - partie 8 (writer Processing)
Cette fonctionnalité ajoute l'intégration du traitement pour l'écriture des tuiles vectorielles. Il s'agit juste d'un contournement de la classe QgsVectorTileWriter existante.

Nouveaux algorithmes dans la boîte à outils :

![image87](images/entries/81117303-224a1b80-8f27-11ea-851d-f4271ce66ed3.webp)

Algorithm\'s parameters for XYZ:

![image88](images/entries/81117371-4279da80-8f27-11ea-9d8b-bbe1c78d9bf1.webp)

Algorithm\'s parameters for MBTiles:

![image89](images/entries/81117466-6ccb9800-8f27-11ea-85e7-9c9a1df87920.webp)

Liste des couches en entrée :

![image90](images/entries/81117708-d6e43d00-8f27-11ea-866a-0c3bdbd97291.webp)

Détails de la couche d'entrée :

![image91](images/entries/81117621-ae5c4300-8f27-11ea-993b-782d7de4a10e.webp)

This feature was funded by [QGIS Community](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Fonctionnalite : Nouvel algorithme de modélisation pour la création de branches conditionnelles
Cet algorithme permet aux utilisateurs de définir plusieurs conditions (via des expressions qgis), qui font que la branche correspondante du modèle est exécutée ou ignorée selon le résultat de l'évaluation de l'expression.

![image92](images/entries/79409609-b6d4f400-7fe1-11ea-8f7a-f42542f3fbfe.gif)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : permettre de réorganiser les entrées du modèle
Instead of forcing a quasi-random ordering of inputs for models, this feature exposes a new \"Reorder Model Inputs\" option in the model designer which allows users control over the exact order of inputs to show users for their model.

No more illogical ordering like showing a field choice before the layer choice it\'s based on!

Sponsored by NaturalGIS

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Reporter la validation du modèle
Instead of forcing all child algorithms to be immediately valid and have all parameters correctly filled, this feature defers model validation until run time or when a new \"Validate model\" action is triggered.

A common frustration with the QGIS model designer is that it constantly forces models to be valid, even work-in-progress models. This means it's impossible to add a component to a model and only partially populate its settings --- you have to fill in everything upfront. If you realise mid way through this that you need to make a change somewhere else in your model, it's impossible to do without canceling and losing all the settings you've already configured.

Cette modification permet de reporter la validation du modèle jusqu'au moment de l'exécution. Les modèles peuvent être temporairement invalides (par exemple, si les composants de l'algorithme ne sont que partiellement configurés). Les valeurs requises manquantes peuvent maintenant être complétées ultérieurement, sans perdre les paramètres existants. Si un modèle non valide est exécuté, l'utilisateur reçoit un avertissement descriptif l'informant des modifications qu'il doit apporter pour terminer la configuration du modèle.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout de la prise en charge de différents types de données raster dans l'algorithme de création de couches raster constantes
With this feature we added a new advanced **OUTPUT_TYPE** parameter for the *Create constant raster layer* algorithm. Via this parameter, you can now specify an output data type for your constant raster layers.
- Byte
- Integer16
- Unsigned Integer16
- Integer32
- Unsigned Integer32
- Float32 
- Float 64

![image93](images/entries/b7b0b73f7d48104cb49f33ed2d453a70d188cbd6.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Fonctionnalite : Ajout de l'algorithme Round raster
Grâce à ce nouvel algorithme de traitement, nous permettons aux QGIS **d'arrondir les valeurs Raster**.

La principale fonctionnalité de l'algorithme est soit l'arrondi standard vers le haut/le bas/le plus proche des valeurs des cellules à virgule flottante, soit l'arrondi aux puissances d'une base *n* spécifiée par l'utilisateur. L'algorithme peut être utilisé avec des rasterr de tous types (même des raster d'octets/entiers lorsqu'il est arrondi à des puissances de n) et produit le même type de données draster. Un arrondi standard en virgule flottante d'une trame d'entier la copiera et provoquera un avertissement.

L'exemple montre un raster sortie arrondie à des multiples de 10

![image94](images/entries/650983141141fc954abc96f79e5255e4634c5051.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Fonctionnalite : Permet de copier/couper/coller les composants du modèle
Cette fentité permet aux utilisateurs de copier et de coller les composants d'un modèle, à la fois dans le même modèle et entre différents modèles

![image95](images/entries/78641463-a099aa80-78f4-11ea-8c0b-c6b6b72f0e7d.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Permet d'ajouter les résultats du traitement aux couches existantes
When appending results, users are given a field mapping panel choice to allow them to manually set how fields are mapped to the destination layer\'s fields:

![image96](images/entries/78631098-b9976100-78de-11ea-8f18-f7c7473e0945.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Permettre la création de boîtes de groupe dans les modèles
Ajoute les fonctions suivantes au concepteur de modèles :
- La possibilité de personnaliser la couleur des commentaires individuels dans un modèle
- Allow creation of \"Group Boxes\" in models, which are a visual indicator of logically linked model components (e.g. \'Data Preparation Steps\', \'NDVI Calculation Steps\', \... etc). Users can customise the color and title for group boxes.
- Permet de naviguer directement vers les boîtes de groupe à partir du menu Affichage, ce qui facilite la navigation dans les modèles complexes.

![image97](images/entries/78090538-bba87e00-740d-11ea-9476-144163d8f1ca.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Traitement : affichage des valeurs d'entrée et de sortie pour les enfants après avoir fait passer le modèle par le concepteur
Une image explique mieux cela ! Après avoir lancé l'algorithme dans le concepteur, vous voyez maintenant les valeurs calculées pour les entrées et les sorties de chaque algorithme enfant :

![image98](images/entries/77991113-5d749000-7366-11ea-986c-652f6e2229e7.webp)

This is very useful for debugging models \-- you can see a much clearer visual picture of the flow of values through the model.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"Save Log to File\" algorithm for models
This algorithm saves the contents of the execution log (right up to the point in the model at which the \'save log\' algorithm executes) to a file.

Il peut être utilisé pour stocker automatiquement le journal de débogage lors de l'exécution des modèles pour référence ultérieure et transparence.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : permet d'exécuter des algorithmes directement sur des bases de données (et d'autres sources qui ne sont pas dans disque) sans avoir à les charger dans les projets au préalable
Ce changement permet aux utilisateurs de naviguer directement vers des sources de couches non basées sur disque pour toute entrée de source de fonction de traitement. Il permet de prendre ces entrées directement dans les couches postgres, sql server, oracle, wfs, afs, etc. sans avoir à les charger au préalable dans un projet !

Nous tirons pleinement parti du navigateur QGIS pour l'activer :

![image99](images/entries/77508685-fca50d80-6eb6-11ea-8190-a447847f55d9.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Exposez les options avancées de traitement des intrants par source d'entité
Cette fonction expose les options avancées par source, telles que :
- La possibilité de limiter le nombre d'entités lues à partir de la source. (Utile dans le développement de modèles, vous pouvez facilement tester des modèles d'exécution en utilisant un petit sous-ensemble d'une couche d'entrée)
- The ability to override on a per-input basis the global processing option for how to handle invalid geometries. Now you can safely leave the default processing setting at the conservative \"Stop algorithm execution when a geometry is invalid\" setting while easily temporarily overriding this for one particular input!

![image100](images/entries/77395930-64dbec80-6dee-11ea-9590-b7fadcd242c1.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Permettre l'accrochage à la grille pour les modèles dans le designer 
This update implements two \"snapping\" features in the Processing model designer:
1. Users can enable a new \"Enable Snapping\" option from the view menu, which will cause all component moving or resizing operations to automatically snap to grids
2. After selecting some components, users can select Edit -\> Snap Selected Components to Grid to manually snap just those selected components.

Additionally, I\'ve added a helpful \"select all\" action for quickly selecting all components in a model.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"filter by geometry type\" and \"filter by layer type\" algorithms to processing
Cette mise à jour ajoute deux nouveaux algorithmes au traitement :
- \"Filter by geometry type\": This algorithm filters features by their geometry type. Incoming features will be directed to different outputs based on whether they have a point, line or polygon geometry. It allows for model creation which responds to different input layer geometry types by applying different logic depending on the input geometry type.
- \"Filter by layer type\": This algorithm allows conditional model branching based on an input layer type. For instance, it allows a model to adapt to the actual layer type of a generic \"map layer\" parameter input, and decide which branch of the model to run as a result.

It also adds in the required API to allow algorithms to \"prune\" model branches based on their calculated results. For example, a model which returns the new *FlagPruneModelBranchesBasedOnAlgorithmResults* flag will cause any remaining parts of the model which are dependent on the outputs of that algorithm to be entirely skipped IF the algorithm does not return that particular output. (This is a prerequisite component for a future generic \"conditional branching by expression\" algorithm, and also used by \"filter by layer type\" to control the model flow based on the input layer type)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: \"Remove Null Geometries\" algorithm can also remove EMPTY geometries
Empty geometries do not contain coordinates. Thus, like *null* geometries, empty geometries are not spatial data in a strict sense. To make it easier for users to clean a vector layer, the *Remove Null Gometries* algorithm now has an \"**Also remove empty geometries**\" option.

![image101](images/entries/76703713-81b34a00-66a1-11ea-9818-ebf771885206.webp)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Fonctionnalite : Ajout d'une gestion multi-sélection au concepteur du modèle, redimensionnement interactif
Ajoute :
- La possibilité de sélectionner plusieurs éléments à la fois dans le concepteur du modèle
- La possibilité de redimensionner des item individuels ou multiples
- La possibilité de supprimer plusieurs éléments sélectionnés
- Improved model designer \"tool\" interaction, following the layout designer approach (e.g. alt + space = zoom drag mode, and selection tools follow their counterparts in layouts so shift+selection adds to selection, ctrl+selection removes, etc)
- Les éléments sélectionnés peuvent être déplacés à l'aide des touches de curseur

Refs NRCan Contract#3000707093

Here\'s how it looks in action (with a particular ugly looking test model I use!)

![image102](images/entries/76388083-f9d4f380-63b3-11ea-8f06-97249e85ac2e.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Ajout d'un support d'annulation/rétablissement au concepteur de modèles
Rend les utilisateurs de QGIS plus indulgents !

Refs NRCan Contract#3000707093

Works just like you\'d expect:

![image103](images/entries/76176510-c8fe8e00-61fc-11ea-90e1-91cbeadcbd4f.gif)

Notez que nous sauvegardons toute la définition du modèle dans la pile d'annulation, et pas seulement les modifications des composants affectés.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Mémoriser les valeurs des paramètres entre les exécution du concepteur de modèles.
Lors de la conception d'un modèle, les utilisateurs devront généralement l'exécuter plusieurs fois, car ils doivent en modifier la structure.

This change causes the parameters used when running the model from the designer to be remembered and saved into the model, so that each time you run the model from the designer you don\'t have to re-set all the input parameter values to the desired test ones.

Rend la conception itérative de modèles tellement plus facile !

Sponsored by Alta Ehf

Also includes a partial port of the model designer dialog from Python to c++, because c++ \>\> Python.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Commentaires dans les modèles de traitement
Cela permet aux utilisateurs de créer des commentaires attachés aux composants du modèle (entrées, algorithmes ou sorties). Les commentaires sont affichés liés au composant associé, et peuvent être librement déplacés dans le modèle.

![image104](images/entries/75851342-26799000-5e35-11ea-8895-a310f01b3823.gif)

Financée par Fisel + König

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Nouvel outil de console autonome pour l'exécution d'algorithmes de traitement
This new qgis_process tool allows users to run processing algorithms (both built-in, and those provided by plugins) directly from the console.

En cours d'exécution :
- `qgis_process list` will output a complete list of all available algorithms, grouped by provider.
- `qgis_process plugins` lists available and activated plugins which advertise the hasProcessingProvider metadata option (only these plugins are loaded by the tool)
- `qgis_process help algid` outputs the help and input descriptions for the specified algorithm, e.g. `qgis_process help native:centroids`

`qgis_process run`: runs an algorithm. Parameters are specified by a `--param=value` syntax. E.g.

    qgis_process run native:centroids --INPUT="my_shapefile.shp" --OUTPUT="centroids.kml"
    
ou

    qgis_process run native:buffer --INPUT=/home/me/my.shp --DISTANCE=20 --OUTPUT=/home/me/buffered.shp
    
Pendant l'exécution d'un algorithme, une barre de rétroaction textuelle s'affiche, et l'opération peut être annulée via CTRL+C

Sponsored by the Swedish User Group

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Nouveau type de paramètre pour les valeurs de date-heure (ou date, ou heure)
Ajout d'un nouveau type de paramètre QgsProcessingParameterDateTime pour le traitement des valeurs de date/date/heure.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout d'algorithmes permettant de déclencher des avertissements et des exceptions aux modèles
Ces algorithmes déclenchent soit un avertissement personnalisé dans le journal de traitement, soit une exception qui entraîne l'arrêt de l'exécution du modèle.

An optional condition expression can be specified to control whether or not the warning/exception is raised, allowing logic like \"if the output layer from another algorithm contains more than 10 features, then abort the model execution\".

Sponsored by Fisel + König

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout de l'algorithme de remplissage des cellules NoData
Dans la nouvelle version de QGIS, nous introduisons un nouvel algorithme de traitement pour remplir les cellules NoData dans un ensemble de données matricielles avec une entrée numérique constante.

L'algorithme analyse un ensemble de données raster d'entrée pour détecter les cellules NoData et les remplit avec la valeur de remplissage définie par l'utilisateur. Ce faisant, l'algorithme respecte le type de données  raster d'entrée de sorte que, par exemple, les nombres à virgule flottante seront traités de manière appropriée pour une trame entière. L'ensemble de données résultant ne contiendra aucune cellule NoData.

![image105](images/entries/6cbf249116a09b4d342729da1e09060b9f0ec52f.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Fonctionnalite : Diverses corrections pour le traitement
- Finaliser le travail sur le support des paramètres de portée dans les algorithmes GRASS ;
- Correction de l'algorithme des séries R brisées
- Corrections mineures de r.rescale et r.rescale.eq
- Correction pour l'outil de rasterisation
- GRASS GIS tests cleanup

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Feature: Show \"template layer\" field constraints in the \"Refactor Fields\" algorithm interface
Lorsque vous migrez des données, il est important d'être conscient des contraintes sur les couches cibles (aussi appelées modèles).

The \"Refactor Fields\" algorithm now highlights constraints, and even lets you know more about them via tool-tips.

![image106](images/entries/75100644-6079a500-559e-11ea-91b6-f99fa05451de.webp)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Fonctionnalite : Nouvel algorithme de conversion en courbes
Nous avons ajouté un nouvel algorithme pour convertir les géométries segmentées en géométries courbes.

L'algorithme considère que les points successifs représentent une courbe s'ils sont espacés uniformément et dans une tolérance.

![image107](images/entries/c747d86081f3862d9d4bbb2ab067103daceab724.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Options de l'application et du projet
### Feature: Add \@layers, \@layer_ids project scope variables
Add \@layers, \@layer_ids project scope variables which contain lists of map layers and map layers ids for all layers from the current project

This mimics the existing \@map_layers, \@map_layer_ids, but unlike the \@map variants these return ALL project layers, not just those associated with the current context\'s map settings.

Parrainé par  SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Fournisseurs de données
### Fonctionnalite : Permet d'ajouter des attributs dans la boîte de dialogue New scratch Layer
Allows the user to add attributes directly in the New Scratch Layer dialog making it more consistent with other dialogs like New Shapefile/Geopackage. ![image108](images/entries/81394331-76711d80-912a-11ea-8b86-4f2789adff08.webp)

Il est toujours possible de créer une switch layer sans aucun attribut en n'ajoutant aucun champ à la liste.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Permet de créer des tables DBF sans géométrie à partir du dialogue New Shapefile
Allow creating \"plain\" DBF files without associated geometries from the New Shapefile dialog.

![image109](images/entries/81068877-be553200-8ee9-11ea-9a06-a4d30e773cf6.webp)

Creating DBF tables can be useful in some cases and having to use third-party tools for this instead of doing it from within QGIS is inconvenient. This also makes the New Shapefile dialog more consistent with the New Geopackage dialog, which already allows \"geometryless\" tables to be created.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalité : Permet de filtrer la liste des WM(T)S dans le dialogue source
Ajouter la possibilité de filtrer entre les listes de WMS ou WMTS à partir du dialogue source

WMS ![image110](images/entries/80964825-d0fc3800-8e11-11ea-9961-34edb623458c.webp)

WMTS ![image111](images/entries/80964191-b4abcb80-8e10-11ea-8b80-395dbb37b45c.webp)

Sponsored by the QGIS Swiss user group

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Fonctionnalite : Ajout de tuiles vectorielles dans le dialogue du gestionnaire de sources de données et dans le menu Couche
Ajout d'un nouvel onglet au dialogue du gestionnaire de sources de données permettant à l'utilisateur de gérer/ajouter des connexions de tuiles vectorielles, y compris importation/exportation. Ajoute également une entrée correspondante dans le menu Couche.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Importation/exportation pour les connexions ArcGIS Map et FeatureServer
Ajout de la fonctionnalité d'import/export manquée pour les connexions ArcGIS MapServer et FeatureServer.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Ajout de tuiles XYZ dans le dialogue du gestionnaire de sources de données et dans le menu Couche
Ajout d'un nouvel onglet au dialogue du gestionnaire de sources de données permettant de gérer/ajouter des connexions XYZ. Ajoute également l'entrée correspondante au menu Couches.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Groupe de transactions spatialite
Implémentation des transactions pour le fournisseur natif de SpatiaLite.

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalite : Permet de sauvegarder les résultats directement dans d'autres formats de base de données (et d'autres trucs sympas)
Cette mise à jour permet aux utilisateurs d'enregistrer les traitements des sorties vecteurs directement dans d'autres formats de base de données.

Auparavant, les résultats ne pouvaient être écrits directement dans les bases de données de postgres. Avec ce changement, cette fonctionnalité a été rendue plus flexible et permet désormais d'écrire directement dans n'importe quel fournisseur de base de données qui met en œuvre l'API de connexion (actuellement postgres, geopackage, spatialite et sql server)

En fin de compte, cela expose la nouvelle possibilité de sauvegarder directement les sorties vers des bases de données SQL Server ou Spatialite (à côté des options GPKG+Postgres précédentes qui existaient déjà)

(As soon as oracle, db2, \... have the connections API implemented we\'ll instantly gain direct write support for those too!)

We do this via a nice inline version of the new \"new database table name\" widget.

![image112](images/entries/77608752-dab89300-6f69-11ea-9c48-eefca7a4d199.gif)

Il y a aussi d'autres choses intéressantes :
- Vous pouvez maintenant glisser et déposer des fichiers ou des dossiers depuis l'explorateur ou le navigateur qgis vers les paramètres de sortie afin d'écraser facilement ces fichiers (ou de les enregistrer dans le dossier), en faisant correspondre le comportement possible avec les entrées
- You can actually write scripts which output direct to ANY qgis data provider (including oracle and db2)\... it\'s just that these don\'t get exposed in the UI because they don\'t yet support the connections API

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Ajout d'un type de paramètre dédié pour les connexions aux bases de données
Permet de faire une sélection parmi les connexions de base de données enregistrées pour un type de fournisseur de base de données spécifique (le fournisseur doit mettre en œuvre l'API de connexions).

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : PG : exposer les foreign table
Expose les foreign tables étrangères au navigateur et au dialogue de sélection de la source de données.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Fonctionnalite :  exposer un filtre sur des données raster dans l'application (PG)
Cette modification devrait être la dernière du fournisseur de données raster PostG et expose les options de filtrage définies :
- Le filtre peut être défini dans le dialogue de la source de données (comme pour les couches vecteur)
- Filter can be set from the legend tree\'s context menu (as for vector layers)
- Le moteur de rendu, l'étendue et les statistiques min/max sont également mis à jour lorsque le filtre change
- De nouveaux tests pour un nouveau comportement

![image113](images/entries/75894983-49a43f80-5e35-11ea-95a8-a86276b39bbc.gif)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Fonctionnalite : Postgres : enregistrer les entités dans des tables avec les champs générés
Permet de mettre à jour/insérer des entités dans les tables PostgreSQL avec les champs générés. Les colonnes générées sur une entité est supportée à partir PostgreSQL 12, qui permet de générer des valeurs de colonne à partir d'autres colonnes de la même table ; cela remplace la création de triggers pour, par exemple, remplir et maintenir automatiquement à jour une colonne de centroïdes ou de surfaces pour les polygones de la colonne géométrique principale.

This feature was developed by [José de Paula Rodrigues N. Assis](https://api.github.com/users/espinafre)
### Fonctionnalite : Prise en charge des types de champs Date et DateTime ajoutée aux fournisseurs de Spatialite et de Delimited Text
Les fournisseurs Spatialite et Delimited Text prennent désormais en charge les types de champs Date et DateTime.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## QGIS Server
### Feature: Add QGIS_SERVER_IGNORE_BAD_LAYERS config option
Permet d'outrepasser le comportement par défaut dans le cas de mauvaises couches (ce qui a pour effet d'invalider l'ensemble du projet).

Lorsqu'il est réglé sur VRAI, les mauvaises couches sont ignorées et le reste du projet devient disponible.

This feature was funded by [Geoinformatikbüro Dassau GmbH](https://www.gbd-consult.de/home.html)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Feature: Server project settings, add \'expanded\' attribute
In addition to the \'visible\' and \'mutuallyExclusive\' attribute, this update adds \'expanded\' to the GetProjectSettings response of the server. The update allows a web client to see which layer tree elements are expanded / collapsed and to then present them the same way in the web map layer list.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files.

Ajoute les paramètres manquants à la requête GetDxf.

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Fonctionnalite : Validateur de projet WMS
Le validateur du serveur QGIS a été revu. Cet outil est utile lorsque vous souhaitez publier un projet QGIS en utilisant le protocole WMS.

Pour les programmeurs, le validateur est maintenant aussi appelable depuis PyQGIS, donc les plugins peuvent maintenant l'utiliser aussi.

This feature was funded by [3Liz](https://www.3liz.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Fonctionnalite : Webp
> WebP est un format d'image moderne qui offre une compression supérieure sans perte et avec perte pour les images sur le web. WebP crée des images plus petites et plus riches qui rendent le web plus rapide.
> 
> Les images WebP sans perte sont 26 % plus petites que les PNG. Les images WebP avec perte sont 25-34% plus petites que les images JPEG comparables à indice de qualité SSIM équivalent.

Source: <https://developers.google.com/speed/webp>

Avec webp, le serveur QGIS prend désormais en charge un format qui permet de réduire la taille des fichiers pour une qualité identique et même d'assurer la transparence.

This feature was funded by [OPENGIS.ch](https://www.opengis.ch)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Extensions
### Feature: Allow plugins to register custom \"Project Open\" handlers
These allow plugins to extend the \"Open Project\" dialog by adding in support for new file filters, which appear in the formats drop down list alongside the existing \"QGS Projects\" entry.

Les gestionnaires d'ouverture de projet personnalisés ont alors la chance de charger les fichiers de projet.

Cela permet aux plugins d'étendre le support QGIS en ajoutant un support intégré pour l'ouverture de projets à partir de formats non QGS/QGZ, par exemple en permettant aux utilisateurs d'ouvrir des documents ArcGIS MXD ou des espaces de travail MapInfo WOR directement à partir du dialogue d'ouverture de projet.

Ces projets non natifs sont également ajoutés à la liste des projets récents et à l'écran d'accueil, ce qui leur donne une expérience vraiment de premier ordre au sein de QGIS.

Parrainé par  SLYR

![image114](images/entries/78514331-1833e080-77f4-11ea-9c8d-a5e9ead7dc1a.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Permettre aux utilisateurs d'installer des plugins stables ou expérimentaux
Cette mise à jour améliore le gestionnaire de plugin en permettant aux utilisateurs de choisir entre l'installation de la version stable ou de la version expérimentale d'un plugin.

Cela permet d'avoir des pré-livraisons de plugins dans le dépôt pour que les utilisateurs puissent les tester, tout en leur permettant de revenir facilement à des versions stables, sans avoir à décocher l'option globale *activer l'expérimentation*.

This change makes no difference for users who haven\'t checked the *enable experimental* option.

![image115](images/entries/75906887-b1638600-5e47-11ea-98c6-06fb664ab177.webp)

This feature was funded by [Swiss QGIS User Group](https://www.qgis.ch/)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
## Programmation
### Fonctionnalite : Support pour l'ajout de widgets du dock sous forme d'onglets : addTabifyDockWidget()
Les widgets du dock sont parfaits pour afficher des interfaces complexes qui étendent les fonctionnalités du QGIS.

Désormais, les développeurs du noyau et des plugins ont la possibilité de tabuler leurs widgets de dock en plus de ceux qui existent déjà. Ils peuvent même choisir sur quel widget ils veulent que leur propre widget apparaisse.

![image116](images/entries/80051225-4b0cf280-84dd-11ea-9016-84a4303f230f.gif)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Fonctionnalite : portage des paramètres de sortie du port vers la nouvelle API
Porte les enveloppes des paramètres de sortie (sinks, vector, raster, fichiers et dossiers de destination) vers la nouvelle API c++ pour le dialogue et le modeleur.

Cela permet une série de nouvelles possibilités, notamment :
- Models with static outputs for child algorithms, e.g. always saving a child algorithm\'s output to a geopackage or postgres layer
- Models with expression based output values for child algorithms, e.g. generating an automatic file name based on today\'s date and saving outputs to that file

![image117](images/entries/78028688-bbbf6400-73a2-11ea-9b7f-a7d81133d321.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Porter les derniers paramètres d'entrée restants vers la nouvelle API
Cette mise à jour porte le paramètre d'entrée Raster Band et le paramètre d'entrée Multi Layer sur la nouvelle API C++.

Les avantages comprennent :
- Listes de bandes/couches basées sur l'expression dans les modèles
- Listes en ligne (non bloquantes) pour les paramètres de multi-sélection (champs, bandes, listes de couches, énumérations)
- Réorganisation des entrées pour les paramètres multicouches dans les modèles, afin de définir des ordres de couches spécifiques

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalité : Porter des paramètres de source, de raster, de vecteur et de couche de maillage dans la nouvelle API
It\'s now possible to use expression-based layer sources in processing models.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Couche de tuiles vectorielles - partie 1
Il s'agit du travail initial sur le support des couches de tuiles vectorielles.

![image118](images/entries/77539757-2d2e7c80-6ea2-11ea-9098-c6c0924f9d59.webp) (The red lines are not rendering artifacts, they are drawn intentionally to show tile borders.)
### Résumé
So far this only includes changes to the qgis_core library.

Principaux ajouts à l'API publique :
- QgsVectorTileLayer - la principale classe de couches cartographiques
- QgsVectorTileRenderer - classe de base pour les implémentations de classe de rendu pour les tuiles vectorielles
- QgsVectorTileBasicRenderer - implémentation du moteur de rendu par défaut

Nouvelles classes privées (peuvent être ajoutées à l'API publique si nécessaire) :
- QgsVectorTileLoader - gère l'extraction des tuiles du réseau / mbtiles
- QgsVectorTileMVTDecoder - gère le décodage des données brutes des tuiles en fonction des entités
- QgsVectorTileLayerRenderer - s'occupe du rendu global (extraction + décodage + dessin)
- QgsVectorTileUtils - diverses fonctions utiles

Quelques nouvelles classes qui peuvent être partagées par les tuiles vectorielles et rasters :
- QgsTileXYZ - position d'une tuile dans l'ensemble de la matric des tuiles (niveau de zoom, colonne, ligne)
- QgsTileRange - sélection rectangulaire dans une matrice de tuiles (colonne et ligne de début/fin)
- QgsTileMatrix - description d'une matrice de tuiles (étendue de la carte, niveau de zoom, échelle, nombre de lignes/colonnes)

(également QgsTileMatrixSet à ajouter ultérieurement lorsque nous prendrons en charge d'autres ensembles de matrices de tuiles que GoogleCRS84Quad)
### Test
You can load a vector tile layer from Python console, e.g.:

    ds = QgsDataSourceUri() ds.setParam("type","xyz")
    ds.setParam("url", "https://api.maptiler.com/tiles/v3/{z}/{x}/{y}.pbf?key=YOUR_FREE_API_KEY") 
    uri = bytes(ds.encodedUri()).decode('utf-8')
    vtl = QgsVectorTileLayer(uri, "Vector Tiles Test")
    QgsProject.instance().addMapLayer(vtl)
    
It is also possible to load vector tiles from a local MBTiles file - for \"type\" use \"mbtiles\" and for \"url\" use a local path (e.g. \"/home/martin/x.mbtiles\").

Il n'y a actuellement aucun soutien pour l'étiquetage.
### Merci
Huge thanks to all funders who have contributed to the crowdfunding and made this possible - <https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors>

This feature was funded by [QGIS Community](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk)
### Fonctionnalite : Paramètre d'étendue du traitement des ports pour la nouvelle api, nombreuses autres améliorations
Cette mise à jour porte finalement le paramètre extent sur la nouvelle api c++, mais en cours de route :
- Refactors the existing gui widget \"QgsExtentGroupBox\" to move the guts out to \"QgsExtentWidget\" (allowing it to be used in places where a group box is inappropriate/looks bad). It also adds a new \"condensed\" mode for the widget, because the default appearance is very space heavy.
- Le nouveau widget de paramètres utilise ce QgsExtentWidget commun, de sorte que nous supprimons tout le code dupliqué qui était auparavant utilisé par l'ancien wrapper python
- Permet de glisser et de déposer les couches de la carte du projet depuis l'arbre des couches vers un QgsExtentWidget afin de définir automatiquement l'étendue à faire correspondre
- Permet l'annulation facultative du QgsExtentWidget
- Allows QgsGeometry values to be set for extent parameter values. This is done to aid use of extent parameters with the \"precalculated value\" mode in models \-- you can now use all the expression geometry functions to calculate a geometry and the bounding box of this is used for the parameter value in the child algorithm

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Interface et API pour des outils de développement/débogage unifiés
Adds interface hooks to allow plugins (and c++) to register \"development/debugging\" tools

Ces outils apparaissent dans un nouveau dock "Outils de développement/débogage" et offrent une manipulation et une place unifiées pour ces outils dans l'interface utilisateur.

L'intention ici est que les outils de développement/débogage spécialisés soient déplacés vers cette interface commune, par exemple
- Loggeur réseau
- Inspecteur de variables locales en Python
- Outils de débogage au démarrage
- Layer load and rendering time debugging tools \... ?

Here\'s an example demo showing a \"Python locals\" dev tool:

![image119](images/entries/77492080-55f74780-6e8b-11ea-9141-1b96c42c29eb.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Fonctionnalite : Support des types de données pour QgsProcessingParameterMapLayer
Allow the definition of accepted layer types for `QgsProcessingParameterMapLayer`. This is useful when an algorithm can work with different layer types (for example, points and rasters) and avoids duplication of the same algorithm with different inputs.

Il s'agit d'une amélioration de l'API qui n'est pas visible pour la grande majorité des utilisateurs.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Fonctionnalite : Ajout de types de paramètres de traitement pour le schéma de la base de données et le nom de la table
Remplace les anciens wrappers ad-hoc de widgets Python postgis par des paramètres de première classe en c++ pour les schémas et les tables, avec des wrappers construits à partir de l'api des connexions de base.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Correctifs notables
### Fonctionnalité : Corrections de bug par Alessandro Pasotti
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Getfeatureinfo ne montre pas les éléments de référence de la relation sous  QGIS server | [#36549](https://github.com/qgis/QGIS/issues/36549) | Il s'est avéré qu'il s'agissait d'une demande d'amelioration | N/A |
| OGR provider QgsOgrProvider::changeAttributeValues returns true on errors | [#36583](https://github.com/qgis/QGIS/issues/36583) | [PR #36620](https://github.com/qgis/QGIS/pull/36620) | N/A |
| GPKG transaction groups are stored with empty second pair of the key | [#36525](https://github.com/qgis/QGIS/issues/36525) | [PR #36660](https://github.com/qgis/QGIS/pull/36660) | [PR #37157](https://github.com/qgis/QGIS/pull/37157) |
| Symbology using relations does not propagate in QGIS Server | [#36614](https://github.com/qgis/QGIS/issues/36614) | impossible à reproduire | N/A |
| \"Loading PostGIS raster with QGIS 3.12.3 crashes\" | [#36689](https://github.com/qgis/QGIS/issues/36689) | [PR #36702](https://github.com/qgis/QGIS/pull/36702) | not relevant |
| GetFeatureInfo Fid value is different between application/json and application/vnd.ogc.gml | [#36262](https://github.com/qgis/QGIS/issues/36262) | [PR #36733](https://github.com/qgis/QGIS/pull/36733) | [PR #37158](https://github.com/qgis/QGIS/pull/37158) |
| GPKG (and spatialite) DB-level unique constraints are not supported by OGR (and spatialite) provider | [#36468](https://github.com/qgis/QGIS/issues/36468) | [PR #36802](https://github.com/qgis/QGIS/pull/36802) | N/A |
| no value in the attribute form if value missing in the value map | [#32756](https://github.com/qgis/QGIS/issues/32756) | [PR #36804](https://github.com/qgis/QGIS/pull/36804) | N/A |
| Le Gestionnaire BD n'affiche plus les résultats d'une requête | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36823](https://github.com/qgis/QGIS/pull/36823) | N/A |
| Le Gestionnaire BD n'affiche plus les résultats d'une requête | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36831](https://github.com/qgis/QGIS/pull/36831) | N/A |
| GPKG browser drag&drop not working | non signalé | [PR #36972](https://github.com/qgis/QGIS/pull/36972) | [PR #37159](https://github.com/qgis/QGIS/pull/37159) |
| Impossible de sauvegarder un projet dans le geopackage | [#36832](https://github.com/qgis/QGIS/issues/36832) | [PR #36980](https://github.com/qgis/QGIS/pull/36980) | N/A |
| It is possible to store text into a numeric field, while it shouldn\'t be, using the Date/Time edit widget | [#36715](https://github.com/qgis/QGIS/issues/36715) | [#36715](https://github.com/qgis/QGIS/issues/36715) | N/A |
| Feature creation very slow when using joins | [#36167](https://github.com/qgis/QGIS/issues/36167) | [PR #36866](https://github.com/qgis/QGIS/pull/36866), [PR #36963](https://github.com/qgis/QGIS/pull/36963) | N/A |
| QGIS Server: la requête WFS n'utilise pas SrsName sur la géométrie | [#36398](https://github.com/qgis/QGIS/issues/36398) | [PR #36926](https://github.com/qgis/QGIS/pull/36926), [PR #37071](https://github.com/qgis/QGIS/pull/37071) | non critique |
| Unable to delete a stored geopackage connection from browser | [#36930](https://github.com/qgis/QGIS/issues/36930) | [PR #36937](https://github.com/qgis/QGIS/pull/36937) | [PR #37166](https://github.com/qgis/QGIS/pull/37166) |
| Constraints: unique constraint not correctly evaluated when 0 | [#36962](https://github.com/qgis/QGIS/issues/36962) | [PR #36967](https://github.com/qgis/QGIS/pull/36967) | N/A |
| PyQgis: OriginJoin fields arte not present into QgsLayerVector QgsFields container for GeoPackage layers | [#36977](https://github.com/qgis/QGIS/issues/36977) | non reproductible | N/A |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | not reproducible/in progress | N/A |
| Removal of unused \'allowMethod\' from qgisservice/qgisserverapi | [#36163](https://github.com/qgis/QGIS/issues/36163) | [PR #36997](https://github.com/qgis/QGIS/pull/36997) | N/A |
| Omogenize window title | [#35761](https://github.com/qgis/QGIS/issues/35761) | [PR #36998](https://github.com/qgis/QGIS/pull/36998) | N/A |
| Labeling: data-defined alignment grey-out activation issue | [#37003](https://github.com/qgis/QGIS/issues/37003) | [PR #37006](https://github.com/qgis/QGIS/pull/37006) | [PR #37167](https://github.com/qgis/QGIS/pull/37167) |
| QGIS reports \"no layers\" in GeoPackage when geopackage directory is write protected | [#36574](https://github.com/qgis/QGIS/issues/36574) | [PR #37018](https://github.com/qgis/QGIS/pull/37018) | not critical (UX only) |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | won\'t fix | N/A |
| Postgis Timestamps from query in DB Manager displayed as \`PyQT5.QTCore.QDateTime(2020, 3, 17 | [#35140](https://github.com/qgis/QGIS/issues/35140) | [PR #37042](https://github.com/qgis/QGIS/pull/37042) | N/A |
| Wrong image preview and image preview size in form | [#33682](https://github.com/qgis/QGIS/issues/33682) | [PR #37093](https://github.com/qgis/QGIS/pull/37093) | [PR #37168](https://github.com/qgis/QGIS/pull/37168) |
| can\'t change value in vertex editor if \"locale\" settings use commas as decimal separator | [#29682](https://github.com/qgis/QGIS/issues/29682) | [PR #37135](https://github.com/qgis/QGIS/pull/37135) | [PR #37169](https://github.com/qgis/QGIS/pull/37169) |
| Identifying a WMS layer with format \"feature\" crashes QGIS | [#29443](https://github.com/qgis/QGIS/issues/29443) | [PR #37171](https://github.com/qgis/QGIS/pull/37171) | [PR #37210](https://github.com/qgis/QGIS/pull/37210) |
| Attempting to create a new feature in Spatialite with transaction group and NOT NULL constraint fails | [#37236](https://github.com/qgis/QGIS/issues/37236) | won\'t fix | N/A |
| Using \"Add feature\" to create feature and child feature with transaction group causes foreign key error | [#37222](https://github.com/qgis/QGIS/issues/37222) | [PR #37249](https://github.com/qgis/QGIS/pull/37249) | non critique |
| Vectorlayer from spatialite missing features and inconsistent feature count | [#29264](https://github.com/qgis/QGIS/issues/29264) | [PR #37277](https://github.com/qgis/QGIS/pull/37277) | À faire |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Fonctionnalité : Correction de bugs par Loïc Bartoletti
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fix error when vector layer has Z | [#32016](https://github.com/qgis/QGIS/issues/32016) | [PR #36553](https://github.com/qgis/QGIS/pull/36553) | [PR #36595](https://github.com/qgis/QGIS/pull/36595) |
| Fix rectangle from 3 points | [#35043](https://github.com/qgis/QGIS/issues/35043), [#35671](https://github.com/qgis/QGIS/issues/35671) | [PR #36523](https://github.com/qgis/QGIS/pull/36523) | [PR #36560](https://github.com/qgis/QGIS/pull/36560) |
| Allow to search qmlplugindump in different paths | N/A | [PR #36513](https://github.com/qgis/QGIS/pull/36513) | N/A |
| Fix the absence of words in the advanced configuration widget | [PR #35643](https://github.com/qgis/QGIS/pull/35643)#issuecomment-610215386 | [PR #36511](https://github.com/qgis/QGIS/pull/36511) | N/A |
| Fix interpolation on split geometry | [PR #36514](https://github.com/qgis/QGIS/pull/36514) | [#33489](https://github.com/qgis/QGIS/issues/33489) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Even Rouault
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Wrong interpretation of EPSG code from a PRJ file in QGIS-dev (proj v7.1.0) | [#36111](https://github.com/qgis/QGIS/issues/36111) | [PROJ PR 2240](https://github.com/OSGeo/PROJ/pull/2240) | N/A: PROJ issue |
| QGIS crashes when adding file to geopackage -\> layer -\> field(BLOB) | [#30210](https://github.com/qgis/QGIS/issues/30210) | [PR #36722](https://github.com/qgis/QGIS/pull/36722) | [PR #36737](https://github.com/qgis/QGIS/pull/36737) |
| Bad error message on WFS connection fail | [#29866](https://github.com/qgis/QGIS/issues/29866) | [PR #36717](https://github.com/qgis/QGIS/pull/36717) | [PR #36735](https://github.com/qgis/QGIS/pull/36735) |
| QGIS crashes during map re-rendering after CRS switch | [#29672](https://github.com/qgis/QGIS/issues/29672) | impossible à reproduire | N/A |
| QGIS crashes when \"open directory\" is selected from the recent projects contextual menu | [#31630](https://github.com/qgis/QGIS/issues/31630) | [PR #36738](https://github.com/qgis/QGIS/pull/36738) | [PR #36755](https://github.com/qgis/QGIS/pull/36755) |
| Problem reprojecting rasters in 54019 and 54042 CRSs | [#35512](https://github.com/qgis/QGIS/issues/35512) | [PROJ PR 2243](https://github.com/OSGeo/PROJ/pull/2243) | N/A: PROJ issue |
| WFS Provider WARNING - Cannot create temporary SpatiaLite cache when using flatpak install | [#36545](https://github.com/qgis/QGIS/issues/36545) | [PR #36745](https://github.com/qgis/QGIS/pull/36745) | N/A |
| WFS Transaction operation using GetCapabilities URI | [#34307](https://github.com/qgis/QGIS/issues/34307) | [PR #36746](https://github.com/qgis/QGIS/pull/36746) | N/A |
| QGis 3.10.2 crashes when displaying two PostGIS raster layers | [#34456](https://github.com/qgis/QGIS/issues/34456) | - | N/A |
| Crashs de QGIS 3.4.10 - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | déjà corrigé sur master | [PR #36751](https://github.com/qgis/QGIS/pull/36751) |
| WMS provider expects SERVICE=WMTS keyword in uppercase to detect WMTS | [#36659](https://github.com/qgis/QGIS/issues/36659) | [PR #36752](https://github.com/qgis/QGIS/pull/36752) | [PR #36766](https://github.com/qgis/QGIS/pull/36766) |
| WCS DescribeCoverage response origin always empty | [#36504](https://github.com/qgis/QGIS/issues/36504) | [PR #36754](https://github.com/qgis/QGIS/pull/36754) | [PR #36781](https://github.com/qgis/QGIS/pull/36781) |
| Extent wrong if layer contains point at 0,0 | [#33823](https://github.com/qgis/QGIS/issues/33823) | Ce n'est pas un bug de QGIS. Corrigé dans GDAL 3.1 | N/A |
| Projection not recognised from Mapinfo converstion | [#34471](https://github.com/qgis/QGIS/issues/34471) | [PR #36758](https://github.com/qgis/QGIS/pull/36758) | [PR #36783](https://github.com/qgis/QGIS/pull/36783) |
| QGIS crashes/freezes when adding a large CSV file as delimited text layer | [#36392](https://github.com/qgis/QGIS/issues/36392) | [PR #36778](https://github.com/qgis/QGIS/pull/36778) | [PR #36810](https://github.com/qgis/QGIS/pull/36810) |
| QGIS 3.12 unknown CRS or Select Transformation | [#36837](https://github.com/qgis/QGIS/issues/36837) | [GDAL Commit 68133b8](https://github.com/OSGeo/gdal/commit/68133b8b6f724a581a5dcb19fbdcd657ddbd6c4c) | [GDAL Commit 6ae7f60](https://github.com/OSGeo/gdal/commit/6ae7f60a5914a2f16b8b1a94758f10e6621e4aca) |
| BIGTIFF error is not obvious in processing log | [#36867](https://github.com/qgis/QGIS/issues/36867) | [GDAL Commit cfc8e61](https://github.com/OSGeo/gdal/commit/cfc8e613ad86dd4b00604dd64df239916ccda135) | [GDAL Commit fb88e3c](https://github.com/OSGeo/gdal/commit/fb88e3ca5c8905fbcaab79e96a2bfc1c36f72d08) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Fonctionnalité : Correction de bugs par Paul Blottiere
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fix segfault when adding a layer | [Mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2020-June/061421.html) | [PR #36910](https://github.com/qgis/QGIS/pull/36910) | N/A |
| Fix signal connection | Problème non reporté | [PR #35836](https://github.com/qgis/QGIS/pull/35836) | N/A |
| Update the API to export a legend in JSON | Unreported binding issue | [PR #36370](https://github.com/qgis/QGIS/pull/36370) | N/A |
| Core dump if vector tile layer (file) becomes unavailable | [#36821](https://github.com/qgis/QGIS/issues/36821) | impossible à reproduire | N/A |
| Crash on project open when mapcanvas extents = nan | [#35899](https://github.com/qgis/QGIS/issues/35899) | impossible à reproduire | N/A |
| Using some functions in raster calulator crashes QGIS | [#35583](https://github.com/qgis/QGIS/issues/35583) | [PR #37273](https://github.com/qgis/QGIS/pull/37273) | N/A |
| Stockage auxiliaire non utilisable dans une couche non éditable | [#30376](https://github.com/qgis/QGIS/issues/30376) | Déjà corrigé. Fermé. | N/A |
| Fix compilation with GCC 10, Qt/PyQt 5.15.0 and SIP 4.19.23 | [#37072](https://github.com/qgis/QGIS/issues/37072) | [PR #37116](https://github.com/qgis/QGIS/pull/37116) | [PR #37250](https://github.com/qgis/QGIS/pull/37250) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Fonctionnalité : correction de bug par Julien Cabieces
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Reproducible crash using QgsMapCanvas.items() with Oracle layers | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #36240](https://github.com/qgis/QGIS/pull/36240) | [PR #36246](https://github.com/qgis/QGIS/pull/36246) |
| Line breaks are ignored in the user expression help panel | [#36191](https://github.com/qgis/QGIS/issues/36191) | [PR #36249](https://github.com/qgis/QGIS/pull/36249) | [PR #36387](https://github.com/qgis/QGIS/pull/36387) |
| \"Edit user expression\" does not allow to rename the user expression | [#36192](https://github.com/qgis/QGIS/issues/36192) | [PR #36349](https://github.com/qgis/QGIS/pull/36349) | N/A |
| Cannot change labels of raster symbology classes | [#36172](https://github.com/qgis/QGIS/issues/36172) | [PR #36376](https://github.com/qgis/QGIS/pull/36376) | [PR #36533](https://github.com/qgis/QGIS/pull/36533) |
| Crash lorsque la couche est indisponible | [#33300](https://github.com/qgis/QGIS/issues/33300) | Ne peut pas se reproduire | N/A |
| Select by expression returns erroneous results with integer field division for shapefiles | [#35449](https://github.com/qgis/QGIS/issues/35449) | [PR #2531](https://github.com/OSGeo/gdal/pull/2531) | N/A |
| Using concat(field1, field2) concatenates 0 instead of empty string (\'\') if any of the fields is NULL | [#36112](https://github.com/qgis/QGIS/issues/36112) | [PR #36521](https://github.com/qgis/QGIS/pull/36521) | [PR #36529](https://github.com/qgis/QGIS/pull/36529) |
| Stuck at Recent Project window when opening blank file in 3.10.3 | [#34809](https://github.com/qgis/QGIS/issues/34809) | Ne peut pas se reproduire | N/A |
| QGIS crashes on getting items of mapCanvas scene if features are identified | [#34457](https://github.com/qgis/QGIS/issues/34457) | [PR #36439](https://github.com/qgis/QGIS/pull/36439) | [PR #36450](https://github.com/qgis/QGIS/pull/36450) |
| sorting on a column that has a value relation is inconsistent | [#36114](https://github.com/qgis/QGIS/issues/36114) | [PR #36776](https://github.com/qgis/QGIS/pull/36776) | [PR #36887](https://github.com/qgis/QGIS/pull/36887) |
| Missing points (depending on canvas scale) in virtual layer based on sqlite file | [#36054](https://github.com/qgis/QGIS/issues/36054) | [PR #36792](https://github.com/qgis/QGIS/pull/36792) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| Project is modified as soon as you move cursor on canvas | [#36796](https://github.com/qgis/QGIS/issues/36796) | [PR #36797](https://github.com/qgis/QGIS/pull/36797) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| Set filter applied to wrong \"version\" of table when multiple geometry types | [#34982](https://github.com/qgis/QGIS/issues/34982) | [PR #36801](https://github.com/qgis/QGIS/pull/36801)[PR #36718](https://github.com/qgis/QGIS/pull/36718) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Bertrand Rix
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Vertex tool override global snapping parameters | [#36229](https://github.com/qgis/QGIS/issues/36229) | [PR #36231](https://github.com/qgis/QGIS/pull/36231) | N/A |
| QGIS crashes with QgsGeometry method on empty collection | [#36142](https://github.com/qgis/QGIS/issues/36142) | [PR #36351](https://github.com/qgis/QGIS/pull/36351) | N/A |
| Selective masking: phantom lines on dark background | [#34650](https://github.com/qgis/QGIS/issues/34650) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/A |
| Selective masking: issue with mask opacity | [#34947](https://github.com/qgis/QGIS/issues/34947) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Sebastien Peillet
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| \[Oracle\]Error on save geometries because wrong default values #34482 | [#34482](https://github.com/qgis/QGIS/issues/34482) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/A |
| Invalid query for default value of date column of an oracle layer | [#32401](https://github.com/qgis/QGIS/issues/32401) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/A |
| Fields missing in Visibility by expression for a group in drag/drop form | [#35196](https://github.com/qgis/QGIS/issues/35196) | [PR #36824](https://github.com/qgis/QGIS/pull/36824) | N/A |
| Project custom scales are displayed with scientific notation | [#36859](https://github.com/qgis/QGIS/issues/36859) | [PR #36860](https://github.com/qgis/QGIS/pull/36860) | N/A |
| Oracle : tables are listed once for Polygons and once for MultiPolygons but both show all geometries | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) | N/A |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | [PR #37136](https://github.com/qgis/QGIS/pull/37136) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Fonctionnalité : Correction de bugs par Alexander Bruy
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Copy of truncated variable copies truncated text, not original | [#30641](https://github.com/qgis/QGIS/issues/30641) | [PR #36554](https://github.com/qgis/QGIS/pull/36554) | [PR #36576](https://github.com/qgis/QGIS/pull/36576) |
| Turning Multi edit mode off does not go back to table view | [#25099](https://github.com/qgis/QGIS/issues/25099) | [PR #36541](https://github.com/qgis/QGIS/pull/36541) | [PR #36630](https://github.com/qgis/QGIS/pull/36630) |
| GRASS processing: missing parameter name | [#36520](https://github.com/qgis/QGIS/issues/36520) | [PR #36644](https://github.com/qgis/QGIS/pull/36644) | [PR #36690](https://github.com/qgis/QGIS/pull/36690) |
| Fix redirection of the stdout results to temporary files in GRASS Processing algorithms | non signalé | [PR #36618](https://github.com/qgis/QGIS/pull/36618) | [PR #36684](https://github.com/qgis/QGIS/pull/36684) |
| Correction de l'algorithme GRASS r.tileset | non signalé | [PR #36645](https://github.com/qgis/QGIS/pull/36645) | [PR #36695](https://github.com/qgis/QGIS/pull/36695) |
| QgsRasterTerrainAnalysisPlugin: check QgsRelief::processRaster() returned value | [#17452](https://github.com/qgis/QGIS/issues/17452) | [PR #36731](https://github.com/qgis/QGIS/pull/36731) | [PR #36740](https://github.com/qgis/QGIS/pull/36740) |
| Histogram for graduated style in layer properties disappears when the layer properties window is too small | [#25197](https://github.com/qgis/QGIS/issues/25197) | [PR #36732](https://github.com/qgis/QGIS/pull/36732) | [PR #36749](https://github.com/qgis/QGIS/pull/36749) |
| Exporting image with atlas option \"Save World file\" lead to incorrect world file naming (text after dot is missing) | [#34523](https://github.com/qgis/QGIS/issues/34523) | [PR #36742](https://github.com/qgis/QGIS/pull/36742) | [PR #36748](https://github.com/qgis/QGIS/pull/36748) |
| \"Reloading QGIS\" from the crash report dialog fails to reopen the project | [#25532](https://github.com/qgis/QGIS/issues/25532) | [PR #36736](https://github.com/qgis/QGIS/pull/36736) | [PR #36750](https://github.com/qgis/QGIS/pull/36750) |
| Exporting raster style to SLD only works when output file has .sld suffix | [#35944](https://github.com/qgis/QGIS/issues/35944) | [PR #36774](https://github.com/qgis/QGIS/pull/36774) | [PR #36795](https://github.com/qgis/QGIS/pull/36795) |
| \[Style Manager\] Missing Favorites category in the \"select by group\" dialog from \"Export symbols\" | [#27315](https://github.com/qgis/QGIS/issues/27315) | [PR #36793](https://github.com/qgis/QGIS/pull/36793) | non critique |
| TIN Interpolation - output raster format and size issues | [#31970](https://github.com/qgis/QGIS/issues/31970) | [PR #36822](https://github.com/qgis/QGIS/pull/36822) | [PR #36844](https://github.com/qgis/QGIS/pull/36844) |
| Layer panel: \"Edit Symbol\" does nothing if no symbol defined for a rule (in rule-based rendering) | [#23048](https://github.com/qgis/QGIS/issues/23048) | [PR #36954](https://github.com/qgis/QGIS/pull/36954) | non critique |
| Attributes shift in the Service area algorithm results | non signalé | [PR #37074](https://github.com/qgis/QGIS/pull/37074), [PR #37097](https://github.com/qgis/QGIS/pull/37097) | N/A |
| Processing testing framework does not apply rounding to values casted to numbers | non signalé | [PR #37234](https://github.com/qgis/QGIS/pull/37234) | N/A |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité: correction de bugs par Nyall Dawson
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| Fix leak in mesh 3d renderer | non signalé | [Commit 4b5a63d](https://github.com/qgis/QGIS/commit/4b5a63d11b7ea5baf6931c8abf86e132c706c1be) | N/A |
| Fix hang when rendering symbol previews using Meters in Map Unit sizes | [#28690](https://github.com/qgis/QGIS/issues/28690) | [Commit 7c6286f](https://github.com/qgis/QGIS/commit/7c6286f8dfb7cc24e5b06c9ab950d9dd55fac517) | No \-- too intrusive |
| Fix font in CSS code editor | non signalé | [Commit 63cb42c](https://github.com/qgis/QGIS/commit/63cb42c298ef5ab732274bce205e49171b797ae4) | non critique |
| Fix rendering of geometry generator expressions which return geometry collection results | [#35356](https://github.com/qgis/QGIS/issues/35356) | [Commit be281c49](https://github.com/qgis/QGIS/commit/be281c49b7932a1d0d0e3cb4dce7af17f5b201a9) | No \-- too intrusive |
| \[processing\] Correctly expose date time inputs (and a bunch of others) as inputs for in-model expressions | [#37219](https://github.com/qgis/QGIS/issues/37219) | [Commit 281356a](https://github.com/qgis/QGIS/commit/281356aa4e951db5cd2782b53a7261c7343c4ca7) | N/A |
| Fix all Qt 5.14 deprecation warnings | non signalé | [Commit 3717adc](https://github.com/qgis/QGIS/commit/3717adcef6315f4b9a0089bfc2393cede937b644) | No \-- too intrusive |
| \[symbology\] When rendering a multipart geometry, ensure that geometry generator symbol is only rendered once, instead of once per part | [#23730](https://github.com/qgis/QGIS/issues/23730) | [Commit d98fe9f](https://github.com/qgis/QGIS/commit/d98fe9f989f3b0677282acdf2ba99f4aa4fa08cc) | No \-- too intrusive |
| \[layout\] Make \"show feature count\" button apply to all selected indexes | [#37194](https://github.com/qgis/QGIS/issues/37194) | [Commit 671cebc](https://github.com/qgis/QGIS/commit/671cebcf817e2b6fc17ce0307edf7fa377b665d3) | No \-- too intrusive |
| Fix for container \"show as group box\" setting is lost when closing layer properties dialog | [#37205](https://github.com/qgis/QGIS/issues/37205) | [Commit 803f507](https://github.com/qgis/QGIS/commit/803f507d45f99534dbc03ab5300e6137da36cd59) | N/A |
| Use even more forceful language to dissuade users from creating custom projections using Proj strings | [#37204](https://github.com/qgis/QGIS/issues/37204) | [Commit 7ec4968](https://github.com/qgis/QGIS/commit/7ec4968aa9dcb2107b00c1caaeb6ae575498bc3c) | No \-- string change |
| Use \"markers\" terminology consistently in centroid fill widget | [#37106](https://github.com/qgis/QGIS/issues/37106) | [Commit 2596b6b](https://github.com/qgis/QGIS/commit/2596b6be858a17533d1e16fca8ff8afc5d222564) | No \-- string change |
| Fixes to numbered list handling in dox/PyQGIS API | non signalé | [Commit 74400c7](https://github.com/qgis/QGIS/commit/74400c7ff88d563dad74dad41860f9b603214973) | Non |
| Fix cross references in PyQGIS docs | non signalé | [Commit 81a9db9](https://github.com/qgis/QGIS/commit/81a9db9f57706cba9b11e4372dd1bf50fcd7bc6a) | Non |
| \[layouts\] Fix attribute table sort order combined with feature filter results in empty tables | [#36341](https://github.com/qgis/QGIS/issues/36341) | [Commit 24897ab](https://github.com/qgis/QGIS/commit/24897ab86a7f11be196d8d705fa3307b05e0e53d) | N/A |
| Fix callout rendering to rotated labels | [#36681](https://github.com/qgis/QGIS/issues/36681) | [Commit 2bb4aad](https://github.com/qgis/QGIS/commit/2bb4aad8c9b7238bd6ff6dc9a90a28c8625e859e) | N/A |
| Fix grass output handling in Processing models | [#36379](https://github.com/qgis/QGIS/issues/36379) | [Commit ef19911](https://github.com/qgis/QGIS/commit/ef19911f1132dc5720a4068f059a0322d7511e2b) |  |
| Fix vector datasets incorrectly simplify to rectangles in some CRS views | [#36898](https://github.com/qgis/QGIS/issues/36898) | [Commit 47fba10](https://github.com/qgis/QGIS/commit/47fba106dd9d057e6691dcca392efacbe31ad9ff) | No \-- too intrusive |
| Fix list item formatting in PyQGIS docs | non signalé | [Commit 84ec481](https://github.com/qgis/QGIS/commit/84ec481aa8f3d3bb487272122414c765e77a2ea2) | N/A |
| \[processing\] Fix manual entry of extent values in widget | [#36787](https://github.com/qgis/QGIS/issues/36787) | [Commit ccc34c7](https://github.com/qgis/QGIS/commit/ccc34c76e714e5f6f87d2a329ca048896eb4c87f) | N/A |
| \[decorations\] Use a proper ellipsoidal length calculation when calculating the size of the scalebar decoration | [#28407](https://github.com/qgis/QGIS/issues/28407) | [Commit af19cea](https://github.com/qgis/QGIS/commit/af19cea5acc90a6cc19d116dd35739059d0c5f83) | [PR 36718 Commit a91309d](https://github.com/qgis/QGIS/pull/36718/commits/a91309ddbc0a430dc3bbcf48070bc565296ac551) |
| Fix collecting Triangle geometry types after tesselation | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit df46fba](https://github.com/qgis/QGIS/commit/df46fba33823415b8310c986795f8c51550a0fa6) | No \-- too intrusive |
| Fix writing triangle geometry type via QgsVectorFileWriter fails | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit e0c03f9](https://github.com/qgis/QGIS/commit/e0c03f9f0848490f358876ae5be6973961700bc9) | No \-- too intrusive |
| Fix degradation in Tesselation results | [#37077](https://github.com/qgis/QGIS/issues/37077) | [Commit 61e7a5f](https://github.com/qgis/QGIS/commit/61e7a5fc90154bd4d35fea7d6cbd413ce61fa02e) | N/A |
| Fix layer subset string is ignored when OGR refuses to accept a compiled feature request expression | [#37073](https://github.com/qgis/QGIS/issues/37073) | [Commit b5b4221](https://github.com/qgis/QGIS/commit/b5b42218af5cbfca82f3b0a4d5a521e3d330f550) | [PR 36718 Commit f486cf6](https://github.com/qgis/QGIS/pull/36718/commits/f486cf6e6dadb2d0690f167620c90f4efddb3c4a) |
| \[legends\] Fix corrupted data defined legend rendering in layout designer | [#36765](https://github.com/qgis/QGIS/issues/36765) | [Commit 8d00ae8](https://github.com/qgis/QGIS/commit/8d00ae8638a09cb9a4c9ecd5d1fec3b352050cdd) | No \-- too intrusive |
| Avoid some QGIS startup warnings | non signalé | [Commit 013f682](https://github.com/qgis/QGIS/commit/013f682bd3c6addd163a78d3776c578ae37377c6) | N/A |
| Place 3d tab in vector properties at the correct position | [#35010](https://github.com/qgis/QGIS/issues/35010) | [Commit ce9f5194](https://github.com/qgis/QGIS/commit/ce9f519468d46bb6fe6dd0bc68efd7d58129be68) | N/A |
| Fix 3d tab is not activated when reopening vector layer properties | [#35011](https://github.com/qgis/QGIS/issues/35011) | [Commit 3c0ecbf](https://github.com/qgis/QGIS/commit/3c0ecbfd79e1924cd01143324cdc26fe4a68f748) | N/A |
| \[labeling\] Fix incorrect label placement after moving an \'unplaced\' label | non signalé | [Commit cbfb7f4](https://github.com/qgis/QGIS/commit/cbfb7f4ce25e10aab5f7b8cee147afb801042704) | [PR 36718 Commit 9189dec](https://github.com/qgis/QGIS/pull/36718/commits/9189dec7633b2eb6a1075bb35c2f90f6b90ba63a) |
| Don\'t block creation of new geopackages in vector save as dialog | non signalé | [Commit 8ccd127](https://github.com/qgis/QGIS/commit/8ccd127f4d8bf66fb04b6484147ed116acf66d91) | N/A |
| \[browser\] Refine refreshConnections method to avoid triggering a full refresh of ALL browser content | [#37007](https://github.com/qgis/QGIS/issues/37007) | [Commit a9d6b04](https://github.com/qgis/QGIS/commit/a9d6b04f776b80acd1a97f48c7ed10e3599618b6) | No \-- too intrusive |
| \[3d\] When showing edges, data defined polygon height was not accounted for | non signalé | [Commit e516231](https://github.com/qgis/QGIS/commit/e516231bb2854405ea78a0cec40ad96295e9f8c6) | N/A |
| Fixes for \"Show all\" labeling mode | non signalé | [Commit 2b91bd0](https://github.com/qgis/QGIS/commit/2b91bd0cafff66f14ceb49b104bf2f2cc6ae714d) | N/A |
| \[3d\] Fix reprojection of features shows no features | [#34824](https://github.com/qgis/QGIS/issues/34824) | [Commit 62bd026](https://github.com/qgis/QGIS/commit/62bd0267439a65f94a5cd9cb886bbb4e4780cdf0) | N/A |
| \[processing\] Add metadata setting for file destination parameters to avoid file overwrite confirmation prompt | [#37011](https://github.com/qgis/QGIS/issues/37011) | [Commit e81af2c](https://github.com/qgis/QGIS/commit/e81af2c9e10dc2a2e220c815cb9e531f7dba838d) | N/A |
| Avoid incorrectly antialiasing rendering of certain objects (such as map labels) when not wanted | [#36964](https://github.com/qgis/QGIS/issues/36964) | [Commit bab83844](https://github.com/qgis/QGIS/commit/bab838444cb55fc479d2f3dfa3b19d8ce80e73af) | No \-- too intrusive |
| Ensure that fields required by marker symbol backgrounds for labels are fetched when rendering | [#36944](https://github.com/qgis/QGIS/issues/36944) | [Commit 8fb8e45](https://github.com/qgis/QGIS/commit/8fb8e45d516611f09bf28e3832c3c6214f16c4a2) | No \-- too intrusive |
| \"Fix \"\"zoom\"\" and \"\"flash\"\" features buttons have no effect when opening filter mode in attribute form\" | [#34506](https://github.com/qgis/QGIS/issues/34506) | [Commit 6b2795](https://github.com/qgis/QGIS/commit/6b27958948db2c88ae72b0b9ff99fc8aa8522bf2) | N/A |
| Avoid corrupted project thumbnail images in some circumstances | non signalé | [Commit f404e6e](https://github.com/qgis/QGIS/commit/f404e6e162df954ffb200d550b6c32375b7270c1) | N/A |
| Auto focus search box when opening \"add layer to legend\" dialog | [#36905](https://github.com/qgis/QGIS/issues/36905) | [Commit 019e494](https://github.com/qgis/QGIS/commit/019e494f1d61851ea192900a2cc9cce460d1ea73) | non critique |
| \[processing\] Set correct output layer type for Point to Layer algorithm | [#36941](https://github.com/qgis/QGIS/issues/36941) | [Commit 7ee85cd](https://github.com/qgis/QGIS/commit/7ee85cd93cb5e0b623feaad2ef1ce9ea8f654bac) | N/A |
| \"Limit scope of Ctrl+C shortcut for copy features to canvas and for python console to console widget\" | [#27035](https://github.com/qgis/QGIS/issues/27035) (many others too) | [Commit 873716c](https://github.com/qgis/QGIS/commit/873716c6fa17298868060a6517205ad7bea78a72) | No \-- too intrusive |
| Remember layout designer window positions | [#36907](https://github.com/qgis/QGIS/issues/36907) | [Commit 97d31d0](https://github.com/qgis/QGIS/commit/97d31d025fe2264afadcf6afcb3eb6ebcfe9e91d) | non critique |
| Fix crash when zooming in too far to labels | [#36346](https://github.com/qgis/QGIS/issues/36346) | [Commit 3aa5e56](https://github.com/qgis/QGIS/commit/3aa5e56d3c3dbb61f2a28c4874593aa401957ed3) | [Commit a22635b](https://github.com/qgis/QGIS/commit/a22635bb64ae6d2a46715bd1208463e22b6080ae) |
| \[processing\] Allow parent layer to be specified for field mapping inputs in models | [#26493](https://github.com/qgis/QGIS/issues/26493) | [Commit b8d4a39](https://github.com/qgis/QGIS/commit/b8d4a39b58465f93f45ed886e77411c194f44132) | No \-- too intrusive |
| Fix placement of message bar \'clear all\' menu arrow on hidpi screens | non signalé | [Commit 8a9975b](https://github.com/qgis/QGIS/commit/8a9975b4ff6b7a8a79bef05230db28754500fa40) | non critique |
| Always refresh plugin repositories when manually triggered by user | [#34351](https://github.com/qgis/QGIS/issues/34351) | [Commit 98603b7](https://github.com/qgis/QGIS/commit/98603b78660e05334c7b34ea3722533164f9553b) | [PR 36718 Commit 0fcf6dc](https://github.com/qgis/QGIS/pull/36718/commits/0fcf6dc08289fb549c9bace24a70ed4a50bdd959) |
| \[3d\] Expose 3d algorithms provider to Python | [#36661](https://github.com/qgis/QGIS/issues/36661) | [Commit 1f835df](https://github.com/qgis/QGIS/commit/1f835dfa9af51204ea1182df7bf722d84b223645) | No \-- too intrusive |
| \[symbology\] Don\'t force rasterized output when exporting point pattern fills | [#16100](https://github.com/qgis/QGIS/issues/16100) | [Commit 23396b7c](https://github.com/qgis/QGIS/commit/23396b7c864d00fc164db8c80d704a1ffc430ac1) | No \-- too intrusive |
| \[layouts\] Don\'t refresh the map canvas multiple times during atlas exports | [#30144](https://github.com/qgis/QGIS/issues/30144) | [Commit 57519e9](https://github.com/qgis/QGIS/commit/57519e9faa95fbfe6196134d9128caee48cb4b84) | non critique |
| \[processing\] Fix double-evaluation of warp output parameter | [#30095](https://github.com/qgis/QGIS/issues/30095) | [Commit adeca2f](https://github.com/qgis/QGIS/commit/adeca2f586203913ae3702531b32579ed4c14344) |  |
| Fix incorrect warning message when turning off atlas preview | non signalé | [Commit 3b0af960](https://github.com/qgis/QGIS/commit/3b0af960dd90af15cbe32e2fd7642408031e70f5) | N/A |
| Speed up message bar operations when many messages are shown | [#29698](https://github.com/qgis/QGIS/issues/29698) | [Commit 5dd29f0](https://github.com/qgis/QGIS/commit/5dd29f065e57fde532a21ae1bc9311aef9378455) | No \-- too intrusive |
| Fix oriented minimum bounding box calculation is wrong in some cases | [#36632](https://github.com/qgis/QGIS/issues/36632) | [Commit 97d0988](https://github.com/qgis/QGIS/commit/97d098884a7889346739d61bd9048e9dcf942d11) | [PR 36718 Commit 68c6a0e](https://github.com/qgis/QGIS/pull/36718/commits/68c6a0e31dc58fa23621e872739df9efded6e6b7) |
| Ensure symbol opacity is always ignored for selections | [#27859](https://github.com/qgis/QGIS/issues/27859) | [Commit 4de6a53](https://github.com/qgis/QGIS/commit/4de6a53235a6f7bd657c60d4f4d7160ed371d9df) | [PR 36718 Commit 99eb710](https://github.com/qgis/QGIS/pull/36718/commits/99eb710f89be0c6adc9acfdd888e366e6f2b796f) |
| Fix random sort order of symbols in Symbol Export dialog | [#20572](https://github.com/qgis/QGIS/issues/20572) | [Commit 987310f](https://github.com/qgis/QGIS/commit/987310fe90de2b21deb5c2564eb051e1d72548b2) | [PR 36718 Commit bfa6058](https://github.com/qgis/QGIS/pull/36718/commits/bfa60586e10735a6b670cd349dd8b9efd2ab2762) |
| Allow clearing heatmap weighting field | [#20256](https://github.com/qgis/QGIS/issues/20256) | [Commit 3961fa2](https://github.com/qgis/QGIS/commit/3961fa26f53e411c5c83b50e006df739ebda4c3e) | [PR 36718 Commit d2600d6](https://github.com/qgis/QGIS/pull/36718/commits/d2600d6d2cb765cb0641347ac342a74f663e4ba5) |
| Flag SAGA \'Merge Layers\' algorithm as having known issues | [#36375](https://github.com/qgis/QGIS/issues/36375) | [Commit f676c821](https://github.com/qgis/QGIS/commit/f676c821d9d9ff2d6e509d881ba2ea1853a34051) | N/A |
| Workaround odd upstream Qt issue where a painter with a semi-transparent brush with no solid pattern incorrectly applies the brush opacity to the pen when exporting to printer devices | [#36580](https://github.com/qgis/QGIS/issues/36580) | [Commit 38c8218](https://github.com/qgis/QGIS/commit/38c82187a65d8b4833f2c633a69a4d937a8725eb) | [PR 36718 Commit a562b67](https://github.com/qgis/QGIS/pull/36718/commits/a562b678438d26c1f80486fdfff422d70c8c6329) |
| Improve plugin watchdog message and UX | non signalé | [Commit 150b373](https://github.com/qgis/QGIS/commit/150b373c7ae61c0548ab0803f9b30a36b15e7ab4) | No \-- too intrusive |
| \"\[layouts\] Warn when previewing an atlas and a feature with no geometry is encountered, when one or more maps are set to be driven by atlas feature\" | [#36556](https://github.com/qgis/QGIS/issues/36556) | [Commit 6ce84d2](https://github.com/qgis/QGIS/commit/6ce84d2c347f49c9aae0c1953e2b2529228db430) | No \-- too intrusive |
| Avoid proj \'object is not a concatenated operation\' warnings | non signalé | [Commit 6baa209](https://github.com/qgis/QGIS/commit/6baa209285f452e5996537b1b0f1b5d924d5c59b) |  |
| \"Fix memory layers lose CRS definition if it does not have an authority associated with it\" | [#36241](https://github.com/qgis/QGIS/issues/36241) | [Commit e23a49a](https://github.com/qgis/QGIS/commit/e23a49a6b858cad9373c3bfb9ad66525622ce9ee) | [PR 36718 Commit c9350eb](https://github.com/qgis/QGIS/pull/36718/commits/c9350eb7439a29ac8ff3734cd7866f2403e3646e) |
| Implement spatial index detection for OGR provider | [#30530](https://github.com/qgis/QGIS/issues/30530) | [Commit f20801a](https://github.com/qgis/QGIS/commit/f20801a8bb3f23576e5e0d2abc6d3229e5044200) | [PR 36718 Commit 536906e](https://github.com/qgis/QGIS/pull/36718/commits/536906ec6375b70d88767e58a08550369a25d1a0) |
| Fix incorrect dialog title for raster layer properties | [#35510](https://github.com/qgis/QGIS/issues/35510) | [Commit 2099261](https://github.com/qgis/QGIS/commit/2099261230f82c5cd4439538e38754947c8f6bd6) | [PR 36718 Commit e809f48](https://github.com/qgis/QGIS/pull/36718/commits/e809f48cb9aaf03dfe8671c2d885f99b4a91922b) |
| Don\'t try to identify CRSes created just for ellipsoid definitions | non signalé | [Commit 15b318b](https://github.com/qgis/QGIS/commit/15b318b50de9131ed1dd6bbf73ae5eb7572579a7) | No \-- too intrusive |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Fonctionnalité : Correction de bugs par Denis Rouzaud
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| allow sorting attribute table by field not listed in the table | [#25671](https://github.com/qgis/QGIS/issues/25671) | [PR #36236](https://github.com/qgis/QGIS/pull/36236) | N/A |
| fix layer tree dependencies (showinf symbols and main layer) | non signalé | [PR #37000](https://github.com/qgis/QGIS/pull/37000) | N/A |
| fix Expression editor: syntax check fails if table is empty | [#37100](https://github.com/qgis/QGIS/issues/37100) | [PR #37137](https://github.com/qgis/QGIS/pull/37137) | N/A |
| fix setting of feature in expression preview widget | [#37214](https://github.com/qgis/QGIS/issues/37214) | [PR #37221](https://github.com/qgis/QGIS/pull/37221) | N/A |
| Freeze when showing attribute table of WFS layer | [#37224](https://github.com/qgis/QGIS/issues/37224) | pas encore corrigé | N/A |
| Lookups in tables with more than 100 entries show wrong value in Relation Reference form parts | [#37266](https://github.com/qgis/QGIS/issues/37266) | [PR #37280](https://github.com/qgis/QGIS/pull/37280) | [PR #37286](https://github.com/qgis/QGIS/pull/37286) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Feature: Bug fixes by Audun Ellertsen
| Intitulé du bug | URL du ticket (le cas échéant) | URL du commit (Github) | Commit sur la 3.10 - backport (GitHub) |
| --- | --- | --- | --- |
| SpatiaLite support for importing layers with binary fields | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36744](https://github.com/qgis/QGIS/pull/36744) | N/A |
| PostGIS support for importing layers with binary fields | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36708](https://github.com/qgis/QGIS/pull/36708) | [PR #36720](https://github.com/qgis/QGIS/pull/36720) |

This feature was funded by [Kongsberg Digital](https://www.kongsberg.com/digital/)

This feature was developed by [Audun Ellertsen](https://github.com/audun/)

{{<content-end >}}
