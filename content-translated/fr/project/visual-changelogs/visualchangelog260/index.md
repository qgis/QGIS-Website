---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.6{#changelog26 }
Date de publication : 31/10/2014

Modifications apportées par la version 2.6.0 de QGIS. Nous avons ajouté beaucoup de nouvelles fonctionnalités, de corrections et d'améliorations pour rendre le plus populaire des logiciels libres SIG encore plus utile et fonctionnel.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Général
### Fonctionnalité : Nom du fichier projet dans les propriétés
Vous pouvez désormais voir le chemin complet du fichier projet dans la fenêtre des propriétés du projet.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Fonctionnalité : Supprimer le dernier point lors de mesures à l'aide des touches del/backspace
Maintenant, lorsque vous mesurez des surfaces ou des distances, vous pouvez enlever les points non désirés à l'aide des touches de suppression ou d'espacement arrière.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Fonctionnalité: sélection dans le canevas de carte de l'entité relative à partir du contrôle de formulaire "référence de la relation".
### Fonctionnalité : Outils d'édition
Nous avons réalisé de nombreuses améliorations concernant les outils d'édition :
- Nouveau contrôle de formulaire pour la date et l'heure, capable de gérer les dates vides.
- Édition de filtre de ligne
- Meilleure gestion des valeurs vides pour les contrôles de formulaire.
- Le contrôle de formulaire Photo conserve les valeurs vides.
- Le contrôle de formulaire Web conserver les valeurs vides.
- La table d'attributs peut faire le distinguo entre les valeurs 0 et NULL 
- Ajout d'un suffixe pour le contrôle de formulaire "Plage".

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Fonctionnalité : Utiliser une sélection de champs de la couche jointe
Vous pouvez maintenant utiliser juste un sous-ensemble des champs relatifs lorsque vous créez une jointure.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Fonctionnalité: Champ généré par expression (champs virtuels)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Fonctionnalité : les actions peuvent maintenant avoir un bouton associé
Lorsque vous créez une action personnalisée sur une couche vectorielle, vous pouvez maintenant définir et associer un bouton à cette action.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Fonctionnalité: Types et options d'expression additionnels
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Fonctionnalité : Les classes des rendus gradué et catégorisé peuvent être activées et désactivées.
Vous pouvez maintenant choisir de désactiver certaines classes des rendus gradué et catégorisé, sans les supprimer.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Fonctionnalité : Amélioration de la légende
La seconde phase de la refonte de la légende/table des matières est terminée. Cela inclue:
- Nettoyage de l'API (pour les développeurs)
- Visibilité des groupes de couches dans l'arbre des couches. Ce nouveau bouton de barre d'outil vous permet de changer rapidement l'état des groupes de couches qui devraient être visibles.
- Possibilité de gérer les groupes de couches depuis la barre d'outils de légende
- La nouvelle option de filtre de légende dans la barre d'outil de légende vous permettra d'enlever les éléments de légende de n'importe quelle classe non visibles dans l'étendue de la carte. Il s'agit d'une amélioration conséquente car elle permet à votre légende de ne pas afficher les entrées non visibles sur la carte. Elle est disponible dans la légende de la carte principale ainsi que dans le gestionnaire de composition ainsi que pour les couches WMS.
- Les légendes du rendu par ensemble de règles peuvent maintenant être affichées dans un pseudo-arbre.

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Fournisseurs de données
### Fonctionnalité : Améliorations de l'export DXF
- Vue en arbre et sélection des attributs dans la boîte de dialogue d'affectation des couches.
- Gestion des polygones pleins/hachurés.
- Représentation des textes en temps que MTEXT au lieu de TEXT (inclus la police, l'inclinaison et la graisse).
- support for RGB colors when there\'s no exact color match
- Utilisation du format DXF Autocad 2000 (R15) au lieu de la version R12.
- Suppression des méthodes de test pour la version R18.

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Composeur de Cartes
### Fonctionnalité : Possibilité de masquer des éléments du composeur au moment des impressions ou des exports
Nous avons rajouté une case et un bouton de définition par les données permettant de contrôler si l'élément doit être exclu des impressions / exports. Si la case est cochée, l'élément ne sera visible que dans le composeur.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Fonctionnalité: Contrôle de l'impression pour les cadres de composition vides
Pour les cadres de tableau ou HTML, une case à cocher contrôle maintenant si la page contenant ces cadres doit être exportée lorsque le cadre est vide.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Fonctionnalité : Onglet Éléments
L'onglet Élément du composeur permet de choisir d'afficher ou de cacher des éléments, de les verrouiller et, en double-cliquant sur leur nom, d'éditer leur identifiant. Vous pouvez aussi les réorganiser avec la souris par glisser-déposer.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Fonctionnalité: Plus de contrôle sur l'apparence des objets flèches/lignes dans la composition
- Les lignes peuvent être stylées par une boîte de dialogue spécifique.
- Le remplissage et la couleur de contour des pointes de flèches peuvent être définies par l'utilisateur.
- La largeur du contour des pointes de flèches peut être définie par l'utilisateur.

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Fonctionnalité: Contrôle par les données des éléments de composition
De nombreuses propriétés des éléments du composeur d'impression peuvent maintenant être contrôlées en utilisant des liens vers les données. Celà inclue:
- Transparence et mode de fusion
- Rotation de l'élément
- Échelle de carte, emprises et rotation
- La marge de l'atlas de cartes.
- Taille et position de l'élément
- Taille, orientation et nombre de pages

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Fonctionnalité: Les images du composeur d'impression peuvent être définies en tant qu'URL distantes.
Les éléments d'image dans le composeur d'impression gèrent maintenant les URLs distantes comme source de l'image. Cette source peut également être déterminée par les données.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Fonctionnalité: Améliorations des tableau du composeur d'impression.
- Vous pouvez maintenant ajouter une en-tête de tableau ainsi que modifier les couleurs des polices du contenu du tableau.
- Les tableaux peuvent maintenant être répartis sur plusieurs cadres, permettant à leur contenu d'être distribué sur plusieurs colonnes ou sur plusieurs pages différentes.
- Ajout d'une option pour afficher l'en-tête sur le premier cadre, tous les cadres ou aucun cadre.
- Permettre le contrôle manuel de la taille des colonnes.
- Nouvelles options pour la source du tableau, incluant les eléments de l'atlas actuel et les entités filles d'une relation.
- Choix du comportement pour les tableaux vides, incluant la suppression complète du tableau, montrer les cellules vides ou afficher un message pré-établi dans le corps du tableau.
- Ajout d'une case à cocher pour filtrer les entrées du tableau à celles qui intersectent l'élément actuel de l'atlas de carte.
- Ajout d'une case à cocher pour supprimer les lignes en doublons d'un tableau.

Veuillez noter que les tableaux des projets QGIS déjà existants ne sont pas automatiquement mis à jour dans le nouveau format de tableau qui gère ces fonctionnalités. Les tableaux doivent être ré-ajoutés au composeur d'impression pour que les nouveaux paramètres apparaissent.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Fonctionnalité: Amélioration du composeur d'impression
Le composeur d'impression (utilisé pour préparer des cartes à imprimer) a reçu un grand nombre d'amélioration dans QGIS 2.6.
- Vous pouvez maintenant modifier la seconde couleur de remplissage dans les barres d'échelle.
- Maintenir la touche Shift lors du tracé d'une ligne ou d'une flèche contraint le tracé à être horizontal, vertical ou incliné à 45 degrés.
- Maintenir la touche Shift lors du tracé des nouveaux éléments génère des carrés; maintenir la touche Alt impose aux éléments d'être tracés depuis le centre.
- Le clic droit ne verrouille plus les éléments du composeur. Cette action est maintenant gérée par le nouveau panneau d'éléments. Les éléments verrouillés ne peuvent plus être sélectionnés dans le canevas du composeur, permettant d'interagir avec les éléments qui sont situés dessous.
- Maintenir la touche Alt appuyée lorsqu'on appuie sur les touches de curseur entraîne un déplacement d'1 pixel des éléments.
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Fonctionnalité: Amélioration de l'accrochage des objets
Les seuils d'accrochage sont maintenant exprimés en pixels, permettant un mouvement et des modifications de taille plus fins lors du zoom dans le composeur d'impression. Les éléments au sein d'un groupe ne sont plus utilisés comme lignes d'accrochage automatique.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Fonctionnalité: Aperçus multiples pour un élément de carte
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Fonctionnalité: Amélioration des éléments HTML
Il existe de nombreuses options utiles pour les élements HTML du composeur:
- Option pour saisir manuellement une source HTML
- Les expressions QGIS à l'intérieur d'une source HTML peuvent être évaluées avant d'effectuer le rendu du contenu HTML.
- URL définie par les données pour les sources HTML.
- Possibilité de créer une feuille de style utilisateur pour remplacer les styles HTML.

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Fonctionnalité: Améliorations de la grille du composeur d'impression
- Vous pouvez maintenant disposer de plusieurs grilles avec des propriétés différentes.
- Vous pouvez mélanger les grilles re-projetées et les grilles en Latitude/Longitude.
- Vous pouvez utilisez la symbologie standard de QGIS pour les lignes de la grille.
- Il existe un nouveau style de cadre/d'annotations destiné aux grilles. Choisir ce style permet d'afficher le cadre ou les annotations sans lignes de grille ou d'autres marques sur la carte.
- Il existe maintenant des options pour contrôler sur quel côté d'un élément de carte le cadre est dessiné.
- Il existe des nouveaux styles de marqueurs pour les cadres, avec des options de marques intérieurs, extérieures ou combinant les deux.
- Nous avons apporté des améliorations sur les annotations de grille en incluant plusieurs nouveaux formats pour les annotations.
- Les annotations de grille utilisent désormais les symboles des guillemets simples et doubles pour le annotations de grille.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Traitement
### Fonctionnalité: Collection de modèles et de scripts en ligne
Les modèles et des scripts peuvent être téléchargés depuis la collection en ligne et installés directement depuis l'interface de géo-traitement. La collection sera étendue avec de nouveaux scripts et de nouveaux modèles par les utilisateurs des géo-traitements.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Fonctionnalité : Nouvelle implémentation du modeleur
Le modeleur a été ré-écrit et fournit maintenant des fonctionnalités supplémentaires comme la création de modèles imbriqués sans limite de niveau de profondeur. Les modèles sont désormais stockés dans des fichiers JSON. La compatibilité arrière est conservée de manière à ce que tous les types de modèles puissent continuer à être utilisés. Vous pouvez également glisser-déposer des éléments depuis les entrées et les algorithmes dans le modeleur graphique.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programmation
### Fonctionnalité: Changement d'API pour les contrôles QGIS
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Server
### Fonctionnalité: Améliorations dans la recherche avec les requêtes GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Fonctionnalité: Ajout d'un paramètre de précision for les attributs de géométries retournés par GetFeatureInfo
## Symbologie
### Fonctionnalité: Meilleur choix de couleur au hasard
Nous avons amélioré l'algorithme de classification de couleur au hasard de manière à ce que les couleurs générées soient plus visuellement distincte les unes des autres.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Fonctionnalité: Améliorations de l'interface utilisateur de Symbologie
- Lorsque c'est possible, les propriétés de symbole d'une couche sont conservées lors du changement du type de symbole.
- Ajout d'un bouton d'édition pour les rampes de gradient de couleur et le remplissage dégradé suivant la forme.
- Mise à jour automatique des plages de limites des étiquettes.
- Les classes du rendu par ensemble de règles sont automatiquement converties si elles étaient du type catégorisé ou gradué.
- Ajout des unités et du nombre de décimales pour les étiquettes du rendu gradué.
- Amélioration de la réactivité aux changements de rampes de couleurs ou de rampes inversées ainsi que des autres options de l'IHM.
- Conservation du symbole lorsqu'on change de type de rendu (simple, gradué, catégorisé et autres rendus).
- Amélioration de l’étiquetage pour le mode de calcul StdDev.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Interface utilisateur
### Fonctionnalité: Coloration syntaxique dans l'éditeur de code
Pour les éditeurs de script Python, le constructeur d'expression, la fenêtre de filtre, le composeur HTML et les éditeurs CSS.

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Fonctionnalité: Palettes de couleur
Vous pouvez maintenant définir vos propres palettes de couleur, utilisables dans QGIS.
- Palette générale customisée (dans la boîte de dialogue des options).
- Palette de couleurs par projet (dans la boîte de dialogue des options du projet).
- Les couleurs sont des boutons de couleur ainsi que dans le nouveau sélecteur de couleurs.
- Vous pouvez exporter ou importer des couleurs d'un fichier de palette GPL.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Fonctionnalité: Nouveau sélecteur de couleur
Il y a maintenant un nouveau sélecteur de couleur dans QGIS. Fonctionnalités incluses:
: - Jauges pour la teinte, la saturation, la valeur rouge, vert, bleu des couleurs.
  - Sélecteur de canal Alpha
  - Option pour copier/coller les codes couleurs HTML (avec plusieurs formats).
  - Aperçu de couleur avant/après avec aperçu alpha.
  - Contrôle interactif de rampe de couleur 2D.
  - Contrôle de teinte sous forme de roue/triangle.
  - Palettes de couleur modifiables, incluant la possibilité de créer des nouvelles palettes et d'importer/exporter des fichiers de palette GPL.
  - Échantillonneur de couleur dynamique avec l'option d'échantilloner sur un radiant donné (selon l'OS).
  - Gestion de l'interaction avec les autres application par glisser/déposer des couleurs (selon l'OS).
  - Option pour désactiver la boîte de dialogue et utiliser le sélectionneur natif de couleur à la place.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Fonctionnalité: Outil de sélection unique fusionné avec la sélection par rectangle
Nous avons fusionné l'outil de sélection unique avec l'outil de sélection en rectangle. Si vous voulez sélectionner une entité unique, activez simplement l'outil de sélection en rectangle et faites un seul clic (à la place de dessiner le rectangle) sur l'entité.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Fonctionnalité: Comportement d'ajout d'une couche dans le canevas de carte
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Fonctionnalité: Ajout des tailles d'icônes de 48 et 64 pixels
Pour ceux qui utilisent QGIS sur des périphériques à écrans tactiles (ou bien pour ceux qui préfèrent les icônes larges), vous pouvez maintenant utiliser des icônes jusqu'à une taille de 64x64 pixels.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Fonctionnalité: Nouveaux boutons de couleur
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Fonctionnalité: Menu contextuel de l'outil d'identification
Lorsque vous utilisez l'outil d'identification, vous pouvez maintenant cliquer sur le canevas pour utiliser le mode contextuel de cet outil. Dans le menu qui apparaît, vous pouvez définir le type d'entité que vous souhaitez identifier (ou toutes si vous le voulez).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
