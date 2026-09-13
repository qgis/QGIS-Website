---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.10{#changelog210 }
Date de publication : 26/06/2015

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Dernière version**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Remerciements**

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonctionnalité: les paramètres de jointure peuvent maintenant être édités.
Il est maintenant possible d'éditer les paramètres de jointure (tels que le préfixe de jointure ou les colonnes à joindre) après la création de la jointure. Avant ce changement, il fallait supprimer et recréer la jointure complète.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Fonctionnalité: Les couches avec jointures peuvent maintenant être filtrées.
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Fonctionnalité: Améliorations générales
Les améliorations qui sont listées ci-dessous ont été apportées à cette version:
- Gestion des couches de nuages de points de PostGIS.
- Améliorations des barres d'icônes et des icônes dans les widgets mobiles pour occuper moins d'espace sur l'écran et pour une meilleure apparence sous OSX.
- Améliorations de l'extension et du pilote de données GRASS.
- Gestion des écritures non-latin pour les étiquettes courbes (le long d'un linéaire).
- Grandes améliorations et meilleure robustesse pour la calculatrice raster et les outils de géo-référencement.
- Amélioration de l'IHM et du processus de la fenêtre des propriétés des étiquettes en ce qui concerne les paramètres définis par les données.

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Fonctionnalité: Amélioration de la gestion des écrasements des fichiers de projet
Désormais, QGIS 2.10 vous avertira lorsque vous essayerez de sauvegarder votre projet et que la date de dernière modification de celui-ci aura été modifiée. Cette fonctionnalité est très utile si plus d'un seul utilisateur ou si plus d'une session travaillent sur le même fichier et qu'ils tentent d'enregistrer leur modification.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Fonctionnalité: Nouveau moteur géométrique
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## Outils d'analyse
### Fonctionnalité: Nouveau panneau de résumé statistique
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Fonctionnalité: Utilisation des fonctions logarithmiques dans la calculatrice raster
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Fonctionnalité: Nouvelles fonctionnalités de statistiques zonales
Les statistiques zonales permettent d'extraire des valeurs agrégées de pixels compris dans un polygone. Les nouvelles fonctionnalités ont été ajoutées à cet outil:
- Vous pouvez maintenant sélectionner quelles statistiques calculer.
- De nouvelles statistiques ont été ajoutées (médiane, écart-type, min, max, plage, minorité, majorité et variation).
- Sélection de la bande raster à utiliser pour une extraction de statistiques.

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Explorateur
### Fonctionnalité: Nouveau panneau de propriétés pour le navigateur
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Fonctionnalité: Nouvelle icône pour le navigateur
Le navigateur QGIS est une application séparée et autonome qui vous permet de naviguer et de consulter les jeux de données géographiques disponibles (issus de votre système de fichiers, de connexions à des bases de données, de services web, etc.). Dans les précédentes versions de QGIS, nous utilisions une icône très semblable à celle de l'application QGIS ce qui entraînait de la confusion pour de nombreux utilisateurs. Pour réduire le désagrément d'ouvrir la mauvaise application, nous avons créé une nouvelle icône pour le navigateur QGIS.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Fournisseurs de données
### Fonctionnalité: Améliorations de l'exportation DXF
L'export DXF a été améliorée de façon continue dans les trois dernières versions de QGIS. Cette version amène une meilleure conversion par blocs du SVG ou des marqueurs simples vers le DXF; elle corrige quelques bogues et erreurs qui pouvaient créer des fichiers DXF incomplets (non lisibles). Dans la capture d'écran, vous pouvez observer la vue originale dans QGIS sur la gauche et le rendu du fichier DXF dans Autodesk TrueView sur la droite.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Cette fonctionnalité a été financée par:** Communautés de Morges, Uster, Vevey et SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Fonctionnalité: Filtres d'expression joués par le serveur PostGIS
Dans QGIS 2.10 vous pouvez maintenant filtrer les entités directement du côté du serveur de base de données. Seules les expressions gérées seront envoyées à la base de données. Les expressions qui utilisent des opérateurs non pris en compte ou des fonctions seront simplement évalués en local.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

ou

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Gestion des données
### Fonctionnalité: Les champs virtuels peuvent maintenant être mis à jour
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Fonctionnalité: Edition de ligne avec auto-complétion pour les contrôles d'édition de type ValueRelation
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Fonctionnalité: Améliorations du gestionnaire de Bases de Données
Il y a deux nouvelles fonctionnalités dans le gestionnaire de bases de données :

**Les couches provenant d'une requête ne nécessitent plus une colonne avec des entiers uniques**

Une colonne avec des entiers uniques n'est plus nécessaire pour charger une couche QGIS provenant d'une requête SQL. Une valeur auto-incrémentée sera utilisée à la place.

**Intégration d'un constructeur de requête SQL**

Une nouvelle fenêtre dans DB Manager permet de faciliter la création de requêtes SQL en utilisant des contrôles où les noms des tables, les noms des colonnes et les fonctions peuvent être sélectionnées par l'utilisateur. Elle a été portée depuis l'extension QSpatialite et fonctionne pour les pilotes PostGIS et Spatialite.

**Cette fonctionnalité a été financée par:** MEDDE (Ministère Français du Développement Durable)

**Cette fonctionnalité a été développée par :** Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Fonctionnalité: Filtres chaînés pour les contrôles de formulaire basés sur des relations
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagrammes
### Fonctionnalité: Améliorations des diagrammes
Les fonctions de diagrammes dans QGIS vous permettent d'ajouter des camemberts ou des histogrammes sur les entités de la carte. Dans cette version, nous avons apporté les changements suivants:
- Les diagrammes peuvent être désactivés sans perdre leur configuration.
- Ajout d'une case à cocher afin de toujours afficher les diagrammes d'une couche.
- L'interface utilisateur des diagrammes a été rafraîchie pour simplifier la boîte de dialogue et la rendre plus accessible à l'utilisateur.
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Numérisation
### Fonctionnalité: Amélioration de l'outil de rotation des géométries
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- Vous pouvez maintenant utiliser une entrée numérique dans l'outil de rotation.
- Vous pouvez utiliser une liste déroulante pour paramétrer les angles.
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Étiquetage
### Feature: \"Follow point\" alignment for multiline labels
Dans ce mode, l'alignement du texte des étiquettes est dépendant du placement final de l'étiquette par rapport au point. Ex: si l'étiquette est placée à gauche du point alors l'étiquette sera alignée à droite et inversement. Cela améliore l'apparence des étiquettes multi-lignes pour les couches de points.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Composeur de Cartes
### Fonctionnalité: Ajout d'un mode de dimensionnement de barre d'échelle pour tenir dans une largeur donnée
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programmation
### Fonctionnalité: Améliorations destinées aux programmeurs
Nous avons réalisé de nombreuses modifications et améliorations au profit des développeurs :
- La version minimum de Qt4 est maintenant la version 4.8. Qt4 est une des plus importantes bibliothèques C++ qui est utilisée pour créer QGIS. 
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Possibilité de changer la source de données d'une couche vecteur.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## QGIS Server
### Fonctionnalité: Gestion du paramètre de tolérance dans les requêtes WMS GetFeatureInfo
Lorsque vous utilisez des couches WMS servies par QGIS Server, vous pouvez maintenant indiquer une tolérance de distance par rapport au clic d'origine pour les requêtes GetFeatureInfo. Ceci est très important pour les appareils mobiles où il est difficile de pointer exactement une entité. Avant cette fonctionnalité, il était pratiquement impossible d'identifier un point ou une ligne sur un appareil mobile avec QGIS Server. Vous pouvez ajouter ces paramètres à vos requêtes GetFeatureInfo:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

et modifiez les valeurs de tolérance (en pixels) qui correspondent à vos besoins.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Symbologie
### Fonctionnalité: Correspondance entre les catégories et les styles
Ajout d'une option dans le menu avancé du rendu catégorisé pour définir les catégories en fonction des symboles dont le nom correspond dans la bibliothèques de style ou d'un fichier XML de style.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Fonctionnalité: Variation des tailles de symboles en utilisant le rendu gradué
Les moteurs de rendu composent le système de QGIS qui vous permet de créer des représentation cartographiques riches de vos données. Le rendu gradué fait varier la symbologie selon une valeur en constant changement dans une couche vecteur. Dans les versions précédentes de QGIS vous ne pouviez faire varier que la couleur (ex: en utilisant une couleur selon une rampe de couleur). Dans QGIS 2.10, le rendu gradué par symbole vous permet de faire varier la taille *ou* la couleur. Pour les couches de points, vous pouvez faire varier la taille du points, pour les lignes, vous pouvez faire varier la largeur de la ligne. Les couches de polygones ne peuvent faire varier que la couleur, la largeur de ligne n'est pas encore gérée.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Fonctionnalité: Nouvelle option pour empêcher le découpage automatique des entités par rapport à l'emprise de la carte
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Fonctionnalité: L'échelle de taille et de rotation ont été supprimées du menu avancé
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Fonctionnalité: Propriétés définies par les données des symboles de police
La majorité des propriétés des symboles de polices de caractères peuvent maintenant être définis par les données, y compris la taille du symbole, la rotation et le caractère.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Fonctionnalité: Visualisation et modification du rendu gradué par un histogramme
Un nouveau panneau d'histogramme a été ajouté au rendu gradué. Il permet d'afficher un histogramme interactif des valeurs du champ ou de l'expression utilisé pour le rendu. Les classes peuvent être définies ou ajoutées depuis l'histogramme.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Fonctionnalité: Expressions de taille, de rotation et d'épaisseur de ligne au niveau de la liste des symboles
La taille et la rotation peuvent être définies en utilisant une expression pour tous les niveaux de symboles qui composent un marqueur. La largeur peut être définie par une expression pour tous les symboles composants une ligne.

Pour les symboles, une légende est générée pour les tailles variables. Cela permet d'afficher une légende d'analyse multivariée dans le cas où vous utilisez des couleurs par classes ou graduation.

Un assistant avec prévisualisation est disponible au niveau du bouton de définition par les données pour aider l'utilisateur à définir l'expression de taille. Trois méthodes sont disponibles: Flannery, Surface et Rayon.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Fonctionnalité: Effets de couche pour les couches et les couches de symboles
Les effets de couche ajoutent au déjà très larges capacités cartographiques de QGIS la possibilité d'ajouter différents effets de rendu dans la chaîne de rendu. Avec ces effets, vous pouvez placer une ombre portée sous le symbole, modifiant et mettant en valeur le rendu du symbole. Vous pouvez également utiliser ces effets l'un sur l'autre et indiquer si l'effet sera progressif (ex: s'applique lui-même sur l'état du rendu) ou discret (en ré-injectant la source géométrique dans la chaîne de rendu).

**Note**: Cette fonctionnalité est réservée aux utilisateurs avancés et vous devez noter que l'abus de cette fonctionnalité peut significativement ralentir le rendu. Vous devriez utiliser plusieurs profils de symbologie pour votre couche: une pour la génération en production et l'autre pour le mode brouillon.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
