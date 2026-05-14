---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.8{#changelog28 }
Date de publication : 20/02/2015

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Version maintenue à Long Terme**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

L'objectif des versions LTR est de fournir une plate-forme stable et moins sujette aux modifications pour les entreprises et les organisations qui ne veulent pas effectuer plus d'une mise à jour par an des installations des postes des travail utilisateur ou des supports de formation. Le succès de cette version LTR dépend fortement de vous, notre utilisateur bien-aimé. Nous avons notamment besoin de votre soutien pour nous aider à financer la correction de bogues et vous devez également vous assurer que vos contrats de support avec vos fournisseurs indiquent que toutes les corrections de bug gérées par votre contrat sont également appliqués sur la branche LTR ainsi que sur la branche de développement normal.

Si vous pensez que la version LTR est importante, merci de penser à soutenir directement le projet QGIS ou d'encourager votre fournisseur commercial d'utiliser la version LTR comme base de votre solution d'entreprise de manière à ce que tout le monde puisse bénéficier d'une plate-forme stable qui sera améliorée et affinée en continu. Pour les utilisateurs et les organisations qui souhaitent bénéficier des toutes dernières évolutions, notre cycle de publication de quatre mois restera inchangé.

**Fonctionnalités**

QGIS 2.8 est également une version spéciale car elle contient de nombreuses nouvelles fonctionnalités intéressantes, des corrections et des améliorations pour rendre QGIS, le plus populaire des logiciels libres SIG, encore plus utile et fonctionnel.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Remerciements**

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
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
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonctionnalité: Saisir des expressions dans des boîtes de saisie rapide
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Fonctionnalité : Les signets peuvent être importés/exportés.
Il est maintenant possible de sauvegarder / charger vos signets dans un fichier. Ceci rend plus simple le partage des signets de localisation, ou de les transférer entre deux ordinateurs.

**Cette fonctionnalité a été développée par :** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Fonctionnalité: Amélioration des expressions
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Évaluations rapides des expressions** 
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Fonctionnalité: Cadre de tests continus et améliorations d'assurance qualité
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

Nous effectuons également régulièrement des analyses sur la base de code QGIS à l'aide de Coverity. Nous avons ainsi identifié et corrigé plus de 1000 problèmes soulevés lors de l'analyse, incluant des fuites mémoires et des crashs potentiels. QGIS présente un taux de défaut de 0.01 alors que la moyenne des logiciels de taille comparable dispose d'un taux de 1.0 environ.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Outils d'analyse
### Fonctionnalité: Améliorations sur la boîte de dialogue de mesure
L'outil de mesure a été amélioré de manière à permettre de choisir quelle unité sera utilisé lors de son utilisation. Il existe également un nouvelle section d'information dans la boîte de dialogue qui montre quels paramètres sont utilisés lors des calculs de mesure.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Explorateur
### Navigateur plus réactif
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Cette fonctionnalité a été développé par :** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Fournisseurs de données
### Fonctionnalité: Gestion des légendes graphiques WMS contextuelles
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gestion des données
### Fonctionnalité: Préfixe personnalisé pour les jointures
Vous pouvez maintenant définir un préfixe personnalisé dans le gestionnaire de jointures dans la boîte de dialogue des propriétés de la couche. Lorsque vous utilisez un préfixe, la table d'attributs affiche les noms des attributs de la couche jointe avec votre préfixe.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Fonctionnalités: Gestion de la création de couches temporaires en mémoire
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Fonctionnalité: Gestion des calculs sur les lignes sélectionnées
Dans la table d'attributs, vous pouvez maintenant effectuer des calculs uniquement sur les lignes sélectionnées grâce à l'ajout d'un nouveau bouton de la barre de calculatrice de champ.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Numérisation
### Fonctionnalités: Outils de numérisation avancée
Sous QGIS, si vous avez toujours voulu pouvoir numériser des lignes qui soient exactement parallèles ou à angle droit, verrouiller des lignes à des angles spécifiques, vous pouvez maintenant le faire ! Les outils de numérisation avancée ont été portés depuis l'extension CADinput et ils ajoutent une nouveau panneau à QGIS. Le panneau s'active lors de la numérisation de nouvelles géométries ou de parties de géométrie.

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Fonctionnalité: Outil de simplification amélioré
L'outil de simplification a été revu, ajoutant:
- La gestion de la reprojection à la volée.
- L'utilisateur peut indiquer la tolérance exacte (et non plus une valeur relative sans lien).
- La tolérance peut être spécifiée en utilisant soit les unités de la couche, soit les unités de la couche, soit en pixels.
- Les paramètres de tolérance sont stockés dans les paramètres généraux de QGIS.
- Possibilité de simplifier plusieurs entités en une seule fois (dessiner un rectangle au lieu de faire un clic).
- Gestion des entités comportant plusieurs parties de géométrie.
- Statistiques à propos de la réduction du nombre de sommets.

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Fonctionnalité: Amélioration de l'accrochage
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Légende des couches
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Composeur de Cartes
### Fonctionnalité: Amélioration de l'interface graphique du composeur d'impression
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Mode plein-écran du composeur**.
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Fonctionnalité: Amélioration des grilles
Dans le composeur, vous avez maintenant un contrôle plus fin sur l'affichage du cadre et de ses annotations. Auparavant, les cartes en rotation ou les grilles reprojetées du composeur affichaient les coordonnées sur chaque côté de la carte. Cela résultait en un mélange de coordonnées latitude/y et longitude/x affichées sur chaque côté. Vous pouvez maintenant gérer si vous voulez afficher toutes les coordonnées, la latitude ou la longitude seulement pour chaque côté du cadre de carte. Des options identiques ont été également ajoutées pour contrôler comment sont divisées les grilles de carte.

Direction descendante verticale pour les annotations. Ce changement introduit un nouveau mode de direction descentante verticale pour les annotations de grilles de carte. Auparavant seul le texte en mode ascendant été géré pour les annotations verticales.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Fonctionnalité: Marges des éléments d'étiquette
- Vous pouvez maintenant contrôler individuellement les **marges d'étiquettes** horizontalement et verticalement. Auparavant, une seule marge s'appliquait aux marges verticales et horizontales. Cela permet aux utilisateurs d'indiquer des marges verticales et horizontales différentes.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Extensions
### Fonctionnalité : Améliorations de la console Python
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Traitement
### Fonctionnalité: Nouveau paramètre de type de prédicat géométrique
Avec ce nouveau type de paramètre, utilisé dans les algorithmes de **Sélection par localisation et Extraction par localisation** ainsi que **Jointure de attributs par localisation**, l'utilisateur peut indiquer précisément l'opérateur spatial à utiliser.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Fonctionnalité: Nouveaux algorithmes
Un certain nombre d'algorithmes a été ajouté à l'ensemble des Traitements:
- Algorithme **Points réguliers** (corrige le bogue #5953)
- Algorithme **Différence symétrique** (corrige le bogue #5953)
- Algorithme **Séparation de vecteur** (corrige le bogue #5953)
- Algorithme **Grille vecteur** (corrige le bogue #5953)
- Algorithme de calcule de **Courbes hypsométriques**.
- **Couper des lignes avec des lignes**
- Algorithme de manipulation d'attributs **Réagencement des champs**

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programmation
### Fonctionnalité: Ajouter des commentaires dans les expressions
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Fonctionnalité: Editeur de fonction d'expression personnalisée
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Fonctionnalité: Gestion de Qt5
QGIS peut maintenant être compilé en utilisant la bibliothèque Qt5. Notez qu'actuellement, la majorité des binaires utilisent encore Qt4 par défaut.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Fonctionnalité: Chargement massif d'index spatiaux
Dans l'API, nous avons ajouté la gestion du chargement massif des index spatiaux. Cela permet d'initialiser les index spatiaux de manière beaucoup plus rapide. Depuis Python, cette opération se réalise simplement:

`index = QgsSpatialIndex( layer.getFeatures() )`

Pour un simple test avec 50000 points dans une couche en mémoire:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

L'arbre d'index devrait théoriquement également être mieux construit ce qui conduit à des recherches plus rapides.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Fonctionnalité: Lancer uniquement la partie sélectionnée d'une requete SQL
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## QGIS Server
### Fonctionnalité: Extensions Python du serveur
La gestion des extensions Python pour QGIS Server amène la puissance de Python du côté serveur permettant un développement et i, déploiement rapide et efficace de nouvelles fonctionnalités.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Fonctionnalité: Gestion des styles de couche
- QGIS Server gère maintenant les styles prédéfinis lors des requêtes GetMap.
- QGIS Server gère maintenant les styles multiples des requêtes GetStyles (consultez la section sur la symbologie ci-dessous)

### Fonctionnalité: Ajout de la méthode DescribeLayer pour le service WMS
**Descripteur de couche stylée pour le service WMS: DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

Définir un style défini par l'utilisateur impose d'utiliser des informations sur les entités qui sont symbolisées ou au moins, leur type géométrique ou leur emprise. Étant donnée que les styles définis par l'utilisateur peuvent être appliqués à une couche nommée, il faut un mécanisme pour fournir au client l'information sur le type de géométrie ou l'emprise de cette couche nommée. Il s'agit d'un autre exemple de rapprochement entre les concepts WMS de couches et de styles et les concepts WFS/WCS de type d'entité et d'emprise de couche. Pour gérer cette fonctionnalité, WMS peut fournir la gestion des requêtes **DescribeLayer**.

La méthode DescribeLayer a été préférée à la surcharge supplémentaire des capacités du protocole WMS.

Pour chaque couche nommée, la description doit indiquer si elle est basée sur les données d'entité et si c'est le cas, elle doit indiquer le service WFS/WCS (par un préfixe d'URL) et les types d'entité/emprise. Notez qu'il est parfaitement autorisé qu'une couche nommée ne soit pas décrite avec cette méthode.
## Symbologie
### Fonctionnalité: Type de remplissage d'image raster
Ce nouveau type de symbole permet de remplir les polygones avec une image raster (tuilée).

Les options incluent (défini par les données) le nom de fichier, l'opacité, la taille de l'image (en pixels, mm ou unités de la carte), le mode de coordonnées (entité ou vue) et la rotation.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Fonctionnalité: Rendu temps réel de carte de chaleur
Le nouveau rendu vecteur de carte de chaleur permet la création de cartes de chaleur dynamiques en temps réel pour les couches de points.

Les options de ce rendu comprennent le rayon de carte de chaleur en pixels, en mm ou en unités de la carte, le choix de la rampe de couleur, la pondération des points selon un champ ainsi qu'une jauge pour choisir entre la vitesse de calcul et la qualité.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Fonctionnalité: Styles multiples par couche
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Fonctionnalité: Davantage de paramètres de symbologie déterminés par les données
L'interface utilisateur des paramètres de symbologie définis par les données a été améliorée, en déplaçant les options de données à côté de chaque paramètre modifiable par les données (en conservant les autres parties de QGIS comme les propriétés des étiquettes). De plus, de nouvelles propriétés sont maintenant modifiables par les données. Cette nouvelle interface utilisateur permet également de voir immédiatement si les données sont utilisées pour définir le paramètre et fournit également un accès immédiat à la définition de la donnée utilisée.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Fonctionnalité: Export DXF: amélioration de l'export du marqueur de symbole
La fonctionnalité d'export pour les fichiers DXF a été améliorée avec une plus grande fidélité pour les symboles de marqueurs exportés en utilisant la symbologie native de QGIS.
### Fonctionnalité: Rotation de la carte dans le canevas, amélioration de la rotation dans le composeur
Cette version introduit la gestion de la rotation dans le canevas de carte. Vous pouvez effectuer une rotation du canevas en utilisant l'entrée rotation dans la barre d'état. La gestion de la rotation a été également étendue au composeur de carte pour gérer correctement l'étiquettage et la symbologie.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Interface utilisateur
### Fonctionnalité: Amélioration/rationalisation de la sélection des projections
Toutes les boîtes de dialogue de sélection de projection utilisent désormais les mêmes contrôles de formulaire qui permettent de choisir rapidement une projection à partir des projections récemment utilisées ou des projections de QGIS.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
