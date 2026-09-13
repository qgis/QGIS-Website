---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Date de publication : 23/10/2015

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Remerciements**

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonctionnalité : Nouvel écran de bienvenue
Au lieu de vous présenter une carte vide, vierge, QGIS vous présentera maintenant une liste des projets les plus récents, avec des vignettes afin de faciliter et d'améliorer le choix des travaux que vous avez effectués lors de votre dernière session.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Fonctionnalité : amélioration continue de la qualité de code
Grâce à l'utilisation d'une bibliothèque de nettoyage d'adresse, des centaines de fuites de mémoires ont été identifiées et corrigées. Le scan automatisé du code avec Coverity Scan à été régulièrement effectué afin d'identifier des problèmes potentiels et notre densité de défaut par Coverity est incroyablement faible avec 0,02 défauts pour 1000 lignes de code. La bibliothèque de tests unitaires automatisés à également grossi significativement pendant le développement de la 2.12, résultant à une augmentation des corrections en amont corrigeant des régressions identifiés. Pour la version 2.12, nous avons également ajouté des tests en continu pour OSX, afin que chaque commit soit testé avec la suite des tests unitaires à la fois sur les plateformes Linux mais aussi OSX.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Fonctionnalité : Éditeur avancé de paramètres
Un nouveau menu a été ajouté aux options qui vous laisse éditer n'importe quelles options définies dans votre profile. Cela a été prévu dans le cas d'une utilisation avancée de QGIS car cela peut entraîner un comportement inattendu si vous changez ces options sans bien les comprendre.   

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Fonctionnalité : groupes de couches mutuellement exclusive
Avec cette fonctionnalité, vous pouvez créer un groupe de couche où seulement une seule couche peut être visible. 
cette fonctionnalité peut être activée pour les groupes dans la vue en arborescence des couches du menu contextuel.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Cette fonctionnalité a été financée par:** Tuscany Region (Italie) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Fonctionnalité : Filtre des valeurs de champs dans les boites d'expression
Lorsque vous créez une expression qui prend en compte les valeurs d'un champ, vous pouvez désormais filtrer cette valeur dans l'espace de prévisualisation

**Cette fonctionnalité a été développée par :** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Fonctionnalité : gestion des thèmes pour l'interface utilisateur
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Fonctionnalité : Nouvelles fonctions dans le générateur d'expressions
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Plusieurs fonctions basées sur les géométries ont été ajoutées, dont :
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

De plus, certaines fonctions utiles de l'extension expressions+ ont été intégrée dans le logiciel dont:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

de plus, l'aide contextuelle pour les fonctions a été amélioré pour une meilleure lisibilité.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Fonctionnalité : variables dans les expressions
Vous pouvez désormais définir des variables personnalisées pour des fonctions.
Ces variables peuvent être définies au niveau de l'application, du projet de la couche ou du composeur d'impression. Cela peut s'assimiler aux règles de CSS en cascade car les variables peuvent être remplacée.  Par exemple, une variable créée pour un projet va remplacer toute autres variables du niveau de l'application. Vous pouvez utiliser ces variables pour construire des chaînes de caractère ou une expression particulière. Par exemple, créer une étiquette dans le composeur avec ce contenu:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

qui renverra l'étiquette suivante:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Outils d'analyse
### Fonctionnalité : ajout du nombre de sommets dans un champs de l'outil "identifiez les entités"
En utilisant "identifiez les entités" sur une ligne, vous aurez désormais accès au nombre de sommets de l'entité comme attribut supplémentaire.
### Fonctionnalité : outil d'alignement des raster
This new tool in qgis_analysis library is able to take several rasters as input and:
- Reprojète vers le même SRC
- Rééchantilloner à la même taille de cellule et décalage dans la grille
- Découpe une région d'intérêt
- Rééchantillonne les valeurs lorsque cela est nécessaire

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Fonctionnalité : Extension d'aimantation et vérificateur de géométrie
Deux nouvelles extensions (que vous devez ajouter manuellement dans le gestionnaire d'extensions) sont disponibles pour valider et corriger les géométries.

L'extension **Geometry Checker** (image de droite), va vérifier et tenter de corriger des erreurs recensées dans votre jeu de données vecteur. Après résolution des erreurs, la liste des erreurs est automatiquement mise à jour. Cela permet, par exemple que si la résolution d'une erreur résout d'autres erreurs, celles-ci seront enlevées de la liste.

Avec l'outil **Géometry Snaper**, vous pouvez aligner les lignes et sommets d'un vecteur vers celles d'un autre vecteur selon une tolérance pouvant être personalisée.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Options de l'application et du projet
### Fonctionnalité : gestion des mots de passe cryptés
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Configurations d'authentification chiffrées par un mot de passe principale et stockées dans une base de données SQLite
- Architecture basée sur un mécanisme d'extension d'authentification (comme les fournisseurs de données)
- Extension d'authentification basique
- Extension d'authentification basique intégrée pour les connexions PostGIS et les fournisseurs OWS
- Configuration classique avec utilisateur/mot de passe (toujours fonctionnelle)
- Configurations pour les connexions serveurs SSL (enregistrement d'exceptions ou de configurations customisées pour les erreurs de connexion SSL)

Authentification avec une IGC:
- Import de certificats d'Autorités de Certification supplémentaires, de certificats intermédiaires et de lots de certificats d'identification personnelle
- Composants de gestion des certificats comme dans Firefox
- Extensions d'authentification pour les lots de certificats au format PEM et PKCS#12 sur disque ou dans les identités personnelles
- Intégration avec les connexions du fournisseur de données OWS (les connexions avec PostGIS et d'autres bases de données demandent encore un peu de travail)

Pour le cas de projets partagés incluant un répertoire réseau, il est possible d'éditer l'identifiant de la configuration d'authentification (authcfg) avec une référence commune à l'ensemble des utilisateurs.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Dans la boîte de dialogue de gestion des couches non trouvées, les utilisateurs peuvent directement ajouter/modifier/supprimer les configuration d'authentification et mettre à jour l'URI de la source de données correspondante. Ainsi, dans le scénario d'un projet partagé, l'utilisateur peut immédiatement ajouter une nouvelle configuration d'authentification adaptée (et voir exactement quel est l'identifiant de configuration d'authentification qui doit être utilisé) lors du chargement du projet.

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Cette fonctionnalité a été développé par:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Explorateur
### Fonctionnalité : Améliorations des connexions PostGIS dans le navigateur
Le navigateur QGIS gère maintenant la fonctionnalité supplémentaire pour les connexions PostGIS, incluant la possibilité de **créer, renommer et supprimer les schémas**, **le renommage et le vidage des couches** ainsi que la **copie de tables d'un schéma à l'autre**.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Fournisseurs de données
### Fonctionnalité : Amélioration du connecteur PostGIS
Les améliorations suivantes ont été apportées au prestataire PostGIS :
- amélioration des performances pour les rendus basés sur des ensembles de règles pour les couches PostGIS
- prise en charge des clés composées pour les vues

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## Gestion des données
### Fonctionnalité : Améliorations du gestionnaire de bases de données
De nombreuses améliorations ont été ajoutées au Gestionnaire de bases de données :
- Dans DB Manager, vous pouvez maintenant exporter vos données dans n'importe quel format géré par OGR. Auparavant seul le format Shapefile était géré.
- Oracle Spatial est maintenant géré dans le Gestionnaire de Base de données
- Lors de l'import de données dans une table, vous pouvez utiliser la nouvelle option **Importer uniquement les entités sélectionnées** pour limiter les données à récupérer.
- Afin de mieux gérer l'espace occupé par les fenêtres, les nouvelles fenêtres de requête sont affichées sous forme d'onglet.

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Fonctionnalité : Formatage conditionnel des cellules de la table attributaire
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Fonctionnalité : Support des chemins relatifs dans les widgets
Pour les types de widgets d'édition suivants:
- Nom de fichier
- Photo
- Vue Web

Si le chemin sélectionné par le sélectionneur de fichiers est situé dans le même répertoire que le fichier de projet .qgs ou dans un répertoir situé dessous, les chemins sont convertis en chemins relatifs. Cela améliore la portabilité d'un projet QGIS avec des informations multimédias embarquées.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Numérisation
### Fonctionnalité : Améliorations de la numérisation
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- outil de création de polylignes circulaires avec deux points et un rayon
- outil de création de polylignes circulaires avec un point de départ, un point de courbe et un point terminal
- Permet d'annuler le dessin d'une nouvelle entité.
- affichage d'une table des nœuds lors de l'édition avec l'outil de nœuds. Cette table vous permet de renseigner manuellement les coordonnées x et y des nœuds ainsi que les valeurs z et m (en fonction du type de couche).

De plus, la plupart des outils de modification et d'édition de géométrie ont été mis à jour pour gérer correctement les couches contenant des dimensions z ou m.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Étiquetage
### Feature: Data defined quadrant when in \"around point\" mode
Il est maintenant possible d'indiquer un quadrant via les données de la couche lorsqu'une étiquette d'un point est paramétrée avec le mode de placement "Autour du point". Cela vous permet de passer outre la position du quadrant pour une étiquette spécifique alors que les autres suivront la règle du placement automatique.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Fonctionnalité : Afficher uniquement les étiquettes qui rentrent à l'intérieur des polygones
Une nouvelle option ajoutée aux couches de polygones permet de limiter l'affichage des étiquettes à celles qui sont complètement contenues dans le polygone.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Fonctionnalité : Contrôle de la priorité des obstacles aux étiquettes
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Fonctionnalité : Nouvelles options de contrôle des couches polygones en obstacles aux étiquettes
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Fonctionnalité : Définition de la priorité de contrôle sur les étiquettes par les données
Cette fonctionnalité souvent réclamée permet aux utilisateurs de paramétrer la priorité de chaque étiquette. Dans les versions antérieures, QGIS ne permettait de paramétrer la priorité des étiquettes qu'au niveau de la couche entière mais il n'y avait aucune option pour contrôler chaque entité au sein d'une même couche. Maintenant, vous pouvez utiliser une expression définie par les données ou un champ pour prioriser l'affichage des étiquettes sur certaines entités par rapport à d'autres au sein de la même couche !

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Fonctionnalité : Option pour les couches d'obstacle
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Fonctionnalité : Étiquettes basées sur des règles
Les étiquettes des entités peuvent maintenant être stylées en utilisant des règles qui permettent plus de contrôles sur le placement et le style. De la même manière que les rendus cartographiques basés sur des ensembles de règles, les étiquettes basées sur des règles peuvent être hiérarchisées pour permettre plus de souplesse dans les options. Par exemple, vous pouvez faire un rendu différent des étiquettes selon la taille de l'entité sur lesquelles elles seront dessinées (comme illustré par la capture d'écran).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Cette fonctionnalité a été financée par:** Tuscany Region (Italie) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Composeur de Cartes
### Fonctionnalité : Amélioration de la navigation dans l'atlas de cartes
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

Le nom de page peut également être utilisé au sein des expressions de symbologie et d'étiquettes pour permettre la création de styles avancés des entités de l'atlas, en se basant sur le nom de la page.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Fonctionnalité : Format personnalisé pour les annotations de grille
Les annotations de grille du composeur peuvent maintenant être formattées en utilisant un format personnalisé qui est construit en utilisant le moteur d'expression de QGIS. Vous pouvez maintenant utiliser n'importe quel format de grille ésotérique dont vos cartes ont besoins !

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Fonctionnalité : Gestion du texte multi-lignes et du redimensionnement automatique de texte dans les tables d'attributs du composeur
Les tables d'attributs du composeur incorpore maintenant une gestion complète des chaînes de caractères sur plusieurs lignes. Le contrôle de l'alignement vertical du texte au sein d'une cellule a été ajouté ainsi que des options pour redimensionner le texte sur certains caractères ou automatiquement pour s'adapter à la taille des colonnes. Pour imposer le redimensionnement automatique du texte avec des hauteurs automatiques de ligne, paramétrez la largeur de la colonne avec une taille fixe.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Option : Personnalisation avancée de la couleur d'arrière plan d'une cellule.
Ce changement permet aux utilisateurs de paramétrer différentes couleurs pour les alternances de lignes et de colonnes, pour les premières/dernières lignes/colonnes et pour les lignes d'en-tête au sein des tables d'attributs du composeur.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Fonctionnalité : Ajout de l'option d'adaptation de la page à son contenu et des options de rognage de l'export au contenu
Une nouvelle option a été ajouté au panneau de composition pour modifier la taille de la composition à son contenu avec, en option, des marges supplémentaires si nécéssaires.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

Une nouvelle boîte de dialogue des options d'export au format image a été ajoutée pour faciliter cela. Elle inclue des raccourcis pour passer outre la résolution d'impression ou les dimensions de l'image exportée.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Fonctionnalité : Forcer le rendu en images raster des couches vecteur
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Fonctionnalité : Contrôle défini par les données sur les couches et les réglages de style
Un nouveau contrôle défini par les données a été ajouté pour les couches et les réglages de styles pour l'affichage dans un objet carte de composeur. L'expression définie par les données des couches de la carte doit produire une liste de couches délimitée par des caractères \| (pipe) qui seront affichés dans la carte; ou encore, l'expression qui gère les réglages de style doit produire le nom d'un réglage de style existant.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Fonctionnalité : Option pour masquer des pages de la vue/export
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Extensions
### Fonctionnalité : Mise à jour de l'extension GRASS
Le plugin GRASS a été mis à jour pour gérer GRASS 7. Les couches GRASS peuvent être accessibles et chargées depuis le panneau de navigation ou par QGIS Browser. Les données vecteur GRASS peuvent être éditées directement dans QGIS. Le projet contient les modules fonctionnels suivants:
- Mise à jour de la bibliothèque d'extensions et compilation multi-version
- Intégration dans QGIS Browser et dans le panneau de navigation
- Gestion des ensembles de couches, des modules et du shell pour l'analyse de données
- édition de vecteur

Pour les utilisateurs de GRASS 6 et 7, vous trouverez que l'intégration de GRASS dans QGIS est maintenant plus fluide. Vous pouvez créer des couches GRASS directement dans le panneau de QGIS Browser, vous pouvez styler les couches vecteur GRASS en utilisant les outils de style de QGIS ainsi qu'utiliser les outils de numérisation de QGIS pour créer de nouvelles géométries vectorielles dans un jeu de données GRASS.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programmation
### Feature: Map tools moved from app-\>gui
Cette modification permet de réutiliser les outils de carte depuis des scripts Python ou des extensions Python

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### Fonctionnalité : Édition de couches via \`with edit(layer):\`
Exemple :

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Ceci appellera automatiquement commitChanges() à la fin. En cas d'exception levée, toutes les modifications seront automatiquement annulées grâce à rollBack().

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Fonctionnalité : Nouvelle API du moteur d'étiquettes (QgsLabelingEngineV2)
L'idée est de rendre le moteur plus flexible comparé à QgsPalLabeling :
> - abstraction des étiquettes et des diagrammes du moteur en lui-même
> - permet de disposer de plusieurs types d'étiquettes par couche
> - gère les fournisseurs d'étiquettes personnalisés (ex: implémentés dans des extensions)
> - rend le moteur d'étiquette indépendant du moteur de rendu de la carte
> - améliore les tests automatiques du moteur d'étiquettes et de ses composants

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Cette fonctionnalité a été financée par:** Tuscany Region (Italie) - SITA (CIG: 63526840AE)
### Fonctionnalité : Ouvrir les scripts dans un éditeur externe
Pythonistas, réjouissez-vous - vous pouvez désormais ouvrir vos scripts dans un éditeur externe à l'aide du nouveau bouton ajouté à la console.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Fonctionnalité : Nouvelles classes pour les programmes PyQGIS
Une nouvelle classe QgsStringUtils a été ajoutée et elle permet aux scripts de PyQGIS d’utiliser les nouveaux algorithmes de correspondance floue ajoutés dans la version 2.12. Ces fonctions permettent de trouver la distance de Levenshtein entre deux chaînes de caractères ainsi que de calculer la représentation phonetique Soundex d'une chaîne de caractères. Ces algorithmes ont été optimisés pour la performance et vous pouvez les appliquer à des millions de chaînes de caractères !

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## QGIS Server
### Fonctionnalité : API python de QGIS Server
QGIS Server est empaqueté sous forme de bibliothèque avec une API initiale (mais en accroissement) ainsi que des liens Python. Avec la nouvelle API, nous disposons d'un jeu de tests unitaires Python pour le composant principal du serveur ainsi que pour ses extensions. Invoquer le serveur depuis Python est maintenant aussi facile que:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Fonctionnalité : getMap en format dxf
Il est maintenant possible de récupérer le résultat d'une requête GetMap sur WMS en format DXF. Il prend en charge les mêmes fonctionnalités et options disponibles sous QGIS Desktop. Avec les mêmes limitations.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

Dans la capture d'écran, vous pouvez observer le client QGIS Web sur la gauche avec l'export DXF fonctionnel (utilisant QGIS Server) et la même emprise dans Autodesk TrueView sur la droite.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Symbologie
### Fonctionnalité : Exporter des vignettes depuis le gestionnaire de style
Le gestionnaire de styles vous permet désormais d'exporter des vignettes des styles sélectionnés en format SVG ou PNG.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Fonctionnalité : Nouvelle option de limitation de la taille en mm lorsque les tailles sont définies en unités de carte
Auparavant, la seule option disponible de limite de la plage d'échelle était exprimée en unité de la carte. Vous pouvez maintenant également choisir de limiter la taille de rendu en mm.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Fonctionnalité : Améliorations du moteur de rendu de déplacement de points
- Permettre une tolérance en mm/pixels pour le moteur de rendu de déplacement
- Permettre le paramétrage de la transparence des couleurs
- Mode de placement en cercle concentrique (permet un affichage plus compact qu'avec les cercles)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Fonctionnalité : Toutes les palettes de couleurs peuvent être modifiées
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Fonctionnalité : Amélioration de la gestion des marqueurs de bordure SVG
QGIS 2.12 a corrigé un certain nombre de problèmes liés à la gestion des bordures de marqueurs SVG et des symboles de remplissage SVG

Les versions précédentes de QGIS effectuaient un rendu des bordures avec une taille significativement plus petite que celle qui était paramétrée et le dessin des bordures SVG avec des tailles exprimées en unités de carte était non fonctionnel.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Fonctionnalité : Ajout du pixel comme unité pour la taille des symboles
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
