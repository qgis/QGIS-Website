---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.0{#changelog20 }
Date de publication : 09/09/2013

{{<table-of-contents >}}
## Outils d'analyse
### Fonctionnalité: Ligne de commande de géo-traitements
Pour un accès plus rapide aux fonctionnalités de géo-traitements, lancez la ligne de commande de géo-traitement (Ctrl + Alt + M) et commencez à taper le nom de l'outil que vous cherchez. La ligne de commande vous montrera les options disponibles et les lancera pour vous. Plus besoin de chercher à travers les menus pour trouver des outils, il sont directement à portée de vos doigts.

![image1](images/processing_commander_2.png)
### Fonctionnalité : Amélioration de l'extension Carte de Chaleur
L'extension Cartes de chaleur a subit de nombreuses améliorations et optimisations rendant la création de cartes de chaleur beaucoup plus rapide. De plus, vous avez maintenant le choix dans la fonction kernel à utiliser.

![image2](images/Selection_027.png)
### Fonctionnalité: Gestion des géo-traitements
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Fonctionnalité: Modeleur graphique de géo-traitements
Une des meilleures fonctionnalités du nouveau cadre apporté par les géo-traitements est la possibilité de combiner les outils de manière graphique. En utilisant le **Modeleur graphique de Géo-traitements**, vous pouvez concevoir des analyses complexes à partie d'une séries de petits modules unitaires. Vous pouvez sauvegarder ces modèles et les utiliser en tant que briques dans des modèles plus complexes. De la puissance fabuleuse, intégrée directement dans QGIS et simple d'accès.

![image4](images/Processing_modeler_029.png)
## Options de l'application et du projet
### Fonctionnalité: Définition du projet ouvert par défaut et des modèles de projet
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Fonctionnalité: variables d'environnement système
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Fonctionnalité: Echelles définies par l'utilisateur
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Explorateur
### Fonctionnalité: Amélioration du panneau de navigation
- Les répertoires peuvent être filtrés avec des jokers ou des expressions rationnelles.
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Les icônes sont maintenant triées et regroupées par type (système de fichier, bases de données, serveurs cartographiques).
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Fournisseurs de données
### Fonctionnalité: Amélioration du fournisseur de données Raster
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Fonctionnalité : Support d'Oracle Spatial
QGIS 2.0 inclut maintenant la gestion d'Oracle Spatial.

![image10](images/oracle.png)
### Fonctionnalité: Ajout du fournisseur de données Web Coverage Service
QGIS fournit désormais un accès natif aux couches servies par Web Coverage Services. Le processus d'ajout de ces couches WCS est identique à l'ajout des couches WMS ou WFS.
### Fonctionnalité: Coupure cumulative à 2% par défaut des rasters
De nombreux produits d'image raster ont un grand nombre de valeurs aberrantes ce qui conduit à un rendu d'images un peu délavé en apparence. QGIS 2.0 introduit un contrôle plus fin sur le rendu des rasters, en ajoutant une coupure cumulative des valeurs, par défaut, entre 2% et 98% lors de la détermination de l'espace de couleur de l'image. L'image de gauche est rendue par QGIS 1.8 alors que l'image de droite est rendue par QGIS 2.0 avec les options par défaut.

![image11](images/Selection_023.png)
### Fonctionnalité: Format d'identification WMS
Il est maintenant possible de choisir le format de résultat de l'outil d'identification pour les couches WMS si plusieurs formats sont disponibles sur le serveur. Les formats gérés sont le HTML, à l'élément (CML) et en texte brut. Si le format d'élément (GML) est sélectionné, le résultat aura la même forme que pour les couches vecteur, la géométrie pourra être surlignée et l'entité disposant d'attributs et de géométrie pourra être copiée dans le presse-papier et collée dans une autre couche.

![image12](images/wms-identify.png)
### Fonctionnalité : Support du WMTS
Le client WMS de QGIS gère maintenant le protocole WMTS (Web Mapping Tile Service), incluant la sélection de sous-ensemble comme le découpage par périodes de temps. Lors de l'ajout d'une couche WMS depuis un serveur disposant de ce service, vous serez sollicité pour choisir la période de temps à afficher.

![image13](images/Selection_035.png)
## Général
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Étiquetage
### Fonctionnalité : Nouveau système d'étiquetage
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Fonctionnalité: Utilisation des expressions dans les étiquettes
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Exemples de propriétés liées:
- Police
- Taille
- Style
- Taille du tampon

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Fonctionnalité: Obsolescence de l'ancien moteur d'étiquettes
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

Les recommandations suivantes s'appliquent à l'utilisation de l'ancien moteur sous QGIS 2.0:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- L'onglet d'étiquetage désuet reste actif dans les anciens projets ouverts, si au moins une couche l'utilise, et ne disparaît pas lors de la sauvegarde du projet, même si aucune des couches utilisant l'ancien moteur n'a cette option d'activée.

L'onglet d'étiquettage désuet peut être activé/désactivé pour le projet en cours via des commandes dans la console Python:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**NOTE** : il y a de grandes chances que l'ancien système d'étiquetage soit complètement retiré dans la prochaine version stable de QGIS. Merci de migrer vos anciens projets.

![image17](images/changelog-2.0_labels-deprecated.png)
## Légende des couches
### Fonctionnalité: Options et retour visuel de la légende
- Décompte total des entités dans la couche ainsi que par symbole.
- Les couches vectorielles en mode édition sont matérialisées par un crayon rouge lorsque des modifications n'ont pas encore été validées (non enregistrées).
- La couche active est maintenant soulignée notamment pour l'indiquer lors d'une sélection de plusieurs couches.
- Cliquer dans le blanc de la liste des couches, désélectionne maintenant la sélection.
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Les groupes et les couches peuvent utiliser optionnellement une police en gras.
- Les icônes de d'aperçu des couches raster peuvent être désactivées pour les projets où le rendu est lent.

![image18](images/changelog-2.0_visual-options.png)
### Fonctionnalité: Dupliquer une couche existante
Dupliquer les couches vecteur ou raster sélectionnées depuis la légende. Revient à importer la même couche une deuxième fois, en tant que couche distincte, puis à copier/coller le style et les attributs de symobologie.

![image19](images/changelog-2.0_dup-layer_1.png)
### Fonctionnalité: Commande d'éditions multi-couches
L'utilisateur peut maintenant sélectionner plusieurs couches dans la légende et si une ou plusieurs de ces couches vecteurs sont en édition, il peut choisir de sauvegarder, de revenir en arrière ou d'annuler les changements non enregistrés. L'utilisateur peut également appliquer ces actions sur toutes les couches, indépendamment de la sélection.

![image20](images/changelog-2.0_current-edits.png)
## Composeur de Cartes
### Fonctionnalité: Éléments de carte HTML
Vous pouvez maintenant placer des éléments en html sur votre carte.

![image21](images/Composer_1_006.png)
### Fonctionnalité: Gestion du multipages
Une fenêtre de composeur peut maintenant contenir plus d'une page.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Fonctionnalité: Etiquettes du composeur basées sur des expressions
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Une étiquette avec une expression telle que:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
sera évaluée au moment de l'impression (ou à l'affichage) pour générer:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Fonctionnalité: Lignes à accrochage automatique
Avoir les éléments bien alignés sur la carte est primordial pour réaliser de belles cartes imprimées. Des lignes d'accrochage automatique ont été ajoutées pour permettre d'aligner facilement les objets entre eux, en glissant simplement un objet près d'un autre.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Fonctionnalité: Lignes d'accrochage manuel
Parfois, vous avez besoin d'aligner des objets à certains endroits du composeur. Avec les nouvelles lignes d'accrochage manuel, vous pouvez ajouter des lignes d'accrochage vous permettant d'aligner les objets. Il suffit de cliquer et glisser depuis la règle en haut ou à droite de la fenêtre pour ajouter une nouvelle ligne de repère.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Fonctionnalité : Génération de cartes en série
N'avez-vous jamais eu besoin de créer une série de cartes ? Bien sûr que si ! Le composeur dispose maintenant d'un outil pour générer des atlas. La couche utilisée pour déterminer l'emprise des cartes peut être une couche de points, lignes ou polygones et les attributs de cette couche peuvent être utilisés pour générer des zones de texte adaptées à chaque carte d'une série.

![image26](images/Picture1.png)
### Fonctionnalité: Gestion de l'aperçu automatique dans le cadre de carte
Vous avez besoin d'afficher l'étendue actuelle de votre carte dans une fenêtre d'aperçu plus petite ? Vous pouvez maintenant le faire. Le cadre de carte permet maintenant de montrer l'emprise d'un autre et il sera mis à jour lors d'un déplacement. Utiliser cette fonctionnalité avec la génération d'atlas permet de générer de plus belles cartes. Le cadre d'aperçu utilise le même type de style que les objets de cartes normaux de manière à ne pas brider votre créativité.

![image27](images/Picture1_1.png)
### Fonctionnalité: Mélange de couches
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Fonctionnalité: Gestion des étiquettes HTML
Le support HTML a été ajouté aux étiquettes du composeur de cartes afin de vous offrir plus de contrôle sur vos cartes finales. Les étiquettes HTML gèrent pleinement les feuilles de style css, html, et même javascript si c'est ce qui vous enchante.

![image29](images/html.png)
### Fonctionnalité: Légende multi-colonne du composeur 
La légende du composeur d'impression gère maintenant les colonnes multiples. La division d'une couche de plusieurs classes en multiples colonnes est optionnelle. Les couches de symbole simple sont maintenant ajoutées en tant qu'élément à une seule ligne. Trois styles différents peuvent être affectés au titre de groupe ou à la couche: Groupe, Sous-Groupe ou Caché. Les styles du titre permettent de grouper arbitrairement de manière visuelle les objets. Par exemple, une couche simple symbole peut être affichée en tant qu'objet sur une simple ligne ou avec le titre de la couche (comme en version 1.8), les symboles de plusieurs couches qui se suivent peuvent être regroupés dans un seul groupe (en cachant les titres), etc. Le décompte des entités peut être ajouté aux étiquettes de la légende.

![image30](images/multicolumn-legend.png)
### Fonctionnalité: Mises à jour du gestionnaire de composition
Les améliorations suivantes ont été réalisées sur le gestionnaire de composition :
- Le nom d'un composeur de carte peut maintenant être défini au moment de sa création, en choisissant optionnellement d'utiliser le nom d'une autre composition.
- Il est désormais possible de dupliquer le composeur
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- Le projet peut maintenant être enregistré depuis l'espace de travail du composeur
- Toutes les actions de gestion du composeur sont désormais directement accessibles depuis l'espace de travail du composeur

![image31](images/changelog-2.0_composer-mngmnt.png)
## Extensions
### Fonctionnalité : Gestionnaire d'extensions réorganisé
Dans QGIS 1.x, la gestion des extensions était un peu confuse avec deux interfaces, une pour gérer les extensions déjà installées et l'autre pour récupérer les extensions Python depuis le dépôt des extensions. Dans QGIS 2.0, nous avons introduit **un nouveau gestionnaire unifié d'extensions** qui fournit *une seul point* pour télécharger, activer/désactiver et gérer de manière générales vos extensions. L'interface utilisateur est appréciable avec ses deux onglets et ses icônes facilement reconnaissables.

![image32](images/Plugin_Manager_024.png)
## Programmation
### Fonctionnalité : Nouvelle Console Python
La nouvelle console Python vous donne encore plus de puissance à l'aide de la complétion automatique, de la coloration syntaxique et des polices ajustables. L'éditeur de code permet l'intégration de gros blocs de code par la possibilité d'ouvrir et de lancer des fichiers Python dans la session QGIS.

![image33](images/pyconsole.png)
### Fonctionnalité: Encore plus de fonctions dans le générateur d'expressions
Étant donné que le moteur d'expression est utilisé de plus en plus au cœur de QGIS, de nouvelles fonctions ont été ajoutées au générateur d'expressions où elles sont toutes accessibles. Toutes les fonctions incluent une aide complète et un guide d'utilisation pour faciliter leur utilisation.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Fonctionnalité: Fonctions d'expression personnalisées
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Fonctionnalité: Nouvelle API python plus propre
L'API Python a été nettoyée pour fournir une expérience de développement plus propre et plus pythonesque. L'API QGIS2.0 utilise SIP v2 qui supprime le recours à la logique floue des fonctions toString() et toInt() qui étaient nécessaires pour travailler avec des valeurs. Les types sont maintenant convertis en types Python natifs. L'accès aux attributs est maintenant réalisé au niveau de l'entité elle-même en utilisant une recherche par clef; plus besoin de recherche par index ou par affectation d'attribut.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
La manière de lire les entités d'une couche a également été améliorée pour permettre la gestion du rendu multiple dans les futures versions.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Fonctionnalité : Compatibilité de code avec les versions 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Fonctionnalité: Macros de projet en Python
Un module Python peut être sauvegardé dans un fichier de projet .qgs, il peut être chargé et fournir des fonctions spécfiques qui seront appeler lors des évènements suivants:
- `openProject()`
- `saveProject()`
- `closeProject()`

Le fait de pouvoir lancer des macros se configure dans les options de l'application.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Symbologie
### Fonctionnalité: Propriétés définir par les données
A l'aide des propriétés définies par les données, il est possible de contrôler le type de symbole, la taille, la couleur, la rotation ainsi que beaucoup d'autres propriétés à travers les attributs des entités.

![image39](images/datadefinedproperties2.png)
### Fonctionnalité: Amélioration du gestionnaire de symboles des couches
Le nouvel aperçu des symboles de couches utilise une structure en arbre pour faciliter et améliorer l'accès à l'ensemble des calques de symboles.

![image40](images/symbollayertree.png)
### Fonctionnalité: Gestion de la transparence dans la définition des couleurs
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Fonctionnalité: Contrôle des couleurs pour les couches raster
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Fonctionnalité: Copie de la symbologie entre couches
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Fonctionnalité: Sauvegarder les styles dans votre base de données
Si vous utilisez une base de données pour stocker vos couches vecteurs, vous pouvez maintenant y stocker directement les styles de chaque couche. Cela permet de partager facilement les styles de couche au sein d'une entreprise ou d'un environnement multi-utilisateurs.

![image44](images/Selection_037.png)
### Fonctionnalité: Gestion des rampes de couleur
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Fonctionnalité: Paramétrer des styles personnalisés par défaut pour tous les types de couches
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Interface utilisateur
### Fonctionnalité: Nouveau thème d'icônes
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Fonctionnalité: Onglets latéraux et groupes repliables
Nous avons standardisé la présentation des onglets et avons introduit les groupes repliables dans la plupart de nos boîtes de dialogue afin de rendre la navigation dans les options plus facile ainsi que pour mieux exploiter la surface de l'écran.

![image48](images/Selection_005.png)
### Fonctionnalité: Notifications douces
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Fonctionnalité: Polices personnalisées et feuilles de style Qt
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

La feuille de style générée par QGIS pour l'interface graphique de l'application pour la plate-forme courante peut être accédée après le lancement de ce qui suit (en PyQGIS):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Fonctionnalité: Sélecteur de couleur dynamique et ses boutons
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Fonctionnalité : Annotations SVG
Avec QGIS 2.0 vous pouvez maintenant enregistrer des annotations SVG sur votre carte, soit en l'épinglant à un endroit défini, soit dans une position relative dans le canevas de carte.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Fonctionnalité : Constructeur de formulaire par glisser-déposer
QGIS 2.0 introduit un intéressant nouveau système pour créer des formulaire de saisie de données. Avec le designer de formulaire par glisser-déposer, vous pouvez créer des formulaires agréables à l'oeil, avec des onglets pour regrouper les champs communs ensemble. Il est maintenant beaucoup plus facile de contrôler l'expérience utilisateur de saisie de données.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Fonctionnalité: Outil d'action par défaut
Si vous utilisez les actions des couches vecteur (ou des actions simples peuvent être lancées lorsque vous cliquez sur une entité), alors vous adorerez le nouvel outil d'action. Avec ce dernier, vous pouvez sélectionner l'action active et la lancer lorsque vous cliquez sur les entités géographiques.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
