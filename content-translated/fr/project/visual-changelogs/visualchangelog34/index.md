---
HasBanner: false
draft: false
releaseDate: '2018-10-26'
section: projet
sidebar: true
title: Changelog for QGIS 3.4
type: visual-changelog

---
{{<content-start >}}
# Changelog for QGIS 3.4{#changelog34 }
![image0](images/entries/splash34vs.webp)

Date de publication : 26/10/2018

The first long-term release (LTR) of QGIS 3. QGIS 3.4 just released. After five consolidation point releases (3.4.5) it will replace the previous LTR in the package repositories in February 2019 (see [release schedule]({{< ref "resources/roadmap#release-schedule" >}})). This is a giant leap forward for the project - our first Long Term Release based on the 3.x platform. For users moving over from the 2.18 LTR there is a huge list of new features and impactful changes in this new LTR version. Please bear in mind that 3.x plugins are incompatible with 2.x plugins so review your plugin usage carefully - and if possible help to migrate old plugins to the new platform. If you have not already done so, take a look at the changelogs from [Version 3.0](../visualchangelog30) and [Version 3.2](../visualchangelog32) to understand the full scope of changes in the 3.4 release.

**Remerciements**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current supporters is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

![image1](images/projects/750d7d9b7e9dbd498202c4b1288a0cbceb1cd65b.png)

{{<table-of-contents >}}
## Général
### Fonctionnalité: Flatpak
QGIS is now available as a flatpak application on [flathub](https://flathub.org/apps/search/qgis) Flatpak (formerly xdg-app) is a software utility for software deployment, package management, and application virtualization for Linux desktop computers. It allows users to install different QGIS versions on linux without having to recompile or use Docker. It is a full package with all libraries included, and it uses its own user profile locations. So you\'ll need some disk space and new habits working with flatpak, but it rocks!

[![image28](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)

This feature was funded by [Aleix Pol](https://github.com/aleixpol)

This feature was developed by [Aleix Pol](https://github.com/aleixpol)
### Fonctionnalité : Les fichiers SVG peuvent être intégrés dans les fichiers de projet et de style
Permet aux images SVG utilisées pour la symbologie, les étiquettes, etc. d'être directement intégrées dans le fichier projet (ou de style QML, ou modèle d'impression QPT). Les SVG sont encodés comme une chaîne de caractères base64 standard.

Les symboles peuvent ensuite être extrait des fichiers projets ou symboles puis enregistrés sur le disque en tant que fichier SVG.

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Fonctionnalité : Accélération OpenCL
This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Alessandro Pasotti](https://qgis.org)
## Expressions
### Fonctionnalité : Nouvelles fonctions et variables pour les expressions
Des nouvelles fonctions ont été ajoutées pour les expressions dans QGIS 3.4. Cela inclu de nombreuses fonctions pour manipuler les tableaux et les objets cartographiques (dictionnaire).
- **json_to_map**: Converts a JSON encoded string value to a map (dictionary) type object
- **map_to_json**: Converts a map (dictionary) type object to a JSON encoded string value
- **hstore_to_map**: Converts a hstore value to a map (dictionary) type object
- **map_to_hstore**: Converts a map (dictionary) type object to a hstore value
- **array_foreach** : Loops over an array and executes an expression on each item in the array, returning a new array containing each calculated value
- **array_filter** : Filters an array according to an expression
- **raster_value**: Returns a value sampled from a raster layer at a specified point
- **to_dms**: Converts a numeric value to a Degrees, Minutes, Seconds formatted string
- **to_dm**: Converts a numeric value to a Degrees, Minutes formatted string
- **line_substring**: Returns the portion of a line (or curve) geometry which falls between the specified start and end distances (measured from the beginning of the line). Z and M values are linearly interpolated from existing values.
- **generate_series(start,stop,step)**: Creates an array containing a sequence of numbers.

En complément, de nouvelles variables peuvent être utilisées au sein des expressions QGIS :
- **\@canvas_cursor_point**: Contains a point value representing the current position of the mouse cursor within the main map canvas
- **\@map_layers**: Contains an array of all layers which are visible within the map
- **\@map_layer_ids**: Contains an array of all layer IDs for layers visible within the map

[![image2](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)

This feature was developed by [Etienne Trimaille, Matteo Ghetta, Matthias Kuhn, Mathieu Pellerin, Nyall Dawson](https://qgis.org)
### Fonctionnalité : Auto-complétion du code pour le constructeur d'expression
Autocompletion pour le code au sein de l'éditeur d'expression.
- Les variables, les noms de fonctions et les noms de champ sont proposés et insérés automatiquement lors de l'écriture d'expression.
- Les paramètres des fonctions sont affichés lors de leur complétion

[![image3](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)

This feature was funded by [OPENGIS.ch](https://www.opengis.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch/)
## Outils cartographiques
### Fonctionnalité : Identification ou sélection des entités à partir d'un polygone existant.
Often it is useful to select/identify features that are covered by an existing polygon. For this, users can use \"Select Features by Polygon\" and \"Identify Features by Polygon\" tools, but it was necessary to manually trace the polygon of interest. This new feature allows user to right click on the map and pick an existing polygon feature at that location from popup menu - that polygon will be used as input for selection or identification.

[![image4](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)

Cette fonctionnalité a été financée par Leicestershire County Council

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Interface utilisateur
### Fonctionnalité : Sélection automatique des fichiers exportés dans le gestionnaire de fichier
Whenever a message bar item links to a created file (e.g. after exporting a layout or map layer), the link will now directly open the folder containing this file within the operating system file browser AND pre-select the created file. It\'s a super-handy shortcut speeding up file operations after an export from QGIS!

[![image5](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: New \"Open Directory\" option for disabled welcome page projects
Cette nouvelle option du menu contextuel qui s'affiche en faisant un clic droit sur un projet de la page d'accueil permet aux utilisateurs d'ouvrir le répertoire existant le plus proche du fichier de projet désactivé pour aider à re-localiser le fichier qui aurait été supprimé, déplacé ou renommé.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Améliorations de l'experience utilisateur (UX) pour les couches temporaires en mémoire
Temporary Scratch Layers in QGIS can be very handy when a \"throw-away\" layer is needed, such as when pre-processing data in multiple steps. However, they can be a trap for uniformed users who may not realise that the contents of the layer will be permanently lost when the current QGIS project is closed. Accordingly, a new indicator icon has been added which shows up next to any temporary scratch layers in the layer tree, making it immediately clear which layers are temporary only.

It\'s also much easier to transition these temporary layers to permanent disk-based formats. You can either click the new indicator icon or select \"Make Permanent\" from the layer context menu. QGIS will then prompt for a location to save the temporary layer to, then replaces it in place (keeping the same layer ID, style, form settings, etc).

[![image6](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Amélioration du gestionnaire de tâches¶
The QGIS task manager widget (shown in the status bar whenever a background task is running) now shows an estimated time remaining and completion time for long-running background tasks. This Estimated Time of Arrival is calculated using a simple linear interpolation based on the task\'s elapsed time and current progress, and allows users to know whether they\'ve only got time to make an instance coffee in the office kitchen or walk round the block for a proper barista made coffee before that long processing task completes\...

Additionally, QGIS uses the standard operating system progress reporting mechanisms on more platforms and occasions in QGIS 3.4. Some long running tasks (which don\'t run in the background) such as atlas exports now show their progress via the operating system mechanism, and throw up handy completion notifications.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Hyperliens vers les fichiers de couche vecteur ou raster locaux dans l'onglet Information
For local vector and raster datasets, the Information tab within the layer properties dialog now features source file path hyperlinks. Upon clicking on the hyperlink, the system\'s file navigator will open and automatically highlight the dataset.

[![image7](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Fonctionnalité : Améliorations du Gestionnaire de styles
La boîte de dialogue QGIS Style Manager (qui permet aux utilisateurs de configurer et de gérer leurs propres bibliothèques de symboles et de rampes de couleurs) s'ouvre désormais de manière non modale, de sorte qu'elle peut désormais être utilisée à côté de la fenêtre principale de QGIS (tout comme la boîte de dialogue Layout Manager et Print Layout Designer).

We\'ve also improved the preview of symbols within the Layer Styling dock, adding a toggle to switch between a large icon view and a detailed list view of symbols. Hovering over symbols (and colors!) now shows a large preview of the symbol. Finally, we\'ve made symbol lists more hi-dpi friendly.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité : Améliorations de l'interface et des fonctionnalités du Panneau Explorateur
Des tonnes de travail ont été effectuées pour cette version afin d'améliorer l'interface utilisateur et l'expérience du panneau du navigateur, y compris les correctifs HiDPI, les améliorations du jeu de données vectorielles / raster compressées et un ensemble d'icônes actualisées.

Des fonctionnalités ont également été ajoutées, notamment la possibilité de créer un nouveau répertoire directement à partir du menu contextuel du navigateur. Le navigateur affiche également désormais une gamme d'options plus complète pour les connexions SQL Server, correspondant aux options qui étaient déjà disponibles pour d'autres connexions à la base de données.

[![image8](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)

Cette fonctionnalité a été développée par Mathieu Pellerin (iMHere Asia), Nyall Dawson (North Road)
### Fonctionnalité: Widget de dessins et graphique QML
Un nouveau type de widget de formulaire de couche vectorielle pour afficher des éléments graphiques et interactifs comme des graphiques ou des dessins techniques sur le formulaire d'attribut a été ajouté dans QGIS 3.4. Le widget arbore une configuration flexible, comprenant des exemples de modèles et la prise en charge des expressions.

[![image9](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)

This feature was funded by [QGIS Project](https://qgis.org/)

This feature was developed by [David Signer and Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Symbologie
### Fonctionnalité: Style de couche de maille
- Ajout de jeux de données à la couche maillée à partir du panneau des propriétés
- Panneaux Information et Source dans le panneau des propriétés
- Sélection de l'ensemble de données actif (propriétés ou panneau de style)
- Style des contours / scalaires (propriétés ou panneau de style)
- Style du cadre maille (propriétés ou panneau de style)
- Style des flèches vectorielles (propriétés ou panneau de style)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)
### Fonctionnalité : Classification symétrique pour le mode de rendu Gradué
This feature was funded by <https://github.com/pierreloicq>

This feature was developed by <https://github.com/pierreloicq>
### Fonctionnalité : Exportation et importation partielles des styles QML
When exporting and importing styles to and from `.qml` files it is now possible to select a subset of sections. This allows to save and restore parts of a layer configuration while omitting others. For example, it\'s possible to export only the symbology of a layer and when importing this QML style file into a layer, any configuration on the forms and widgets or other properties are unaffected. It is also possible to only handle single sections of a style when using copy/paste.

[![image10](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)

This feature was funded by [qwat group](http://qwat.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch GmbH)](https://www.opengis.ch)
## Numérisation
### Fonctionnalité : Améliorations des outils de tracking GPS
QGIS 3.4 extends the inbuilt GPS tracking support, adding \"acquisition interval\" and \"distance threshold\" parameters. These options can be used to keep the cursor stationary when the receiver is in static conditions.

This feature was funded by [Andrea Rossi](https://github.com/rossia)

This feature was developed by [Andrea Rossi](https://github.com/rossia)
### Fonctionnalité : Plus de choix de valeurs d'angles dans le panneau de Numérisation avancée
Des options ont été ajoutées pour permettre l'accrochage à 5/10/15/18 / 22,5 degrés en mode construction.

[![image11](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)

This feature was funded by [lbartoletti](https://github.com/lbartoletti)

This feature was developed by [lbartoletti](https://github.com/lbartoletti)
### Fonctionnalité : L'outil de nœuds peut fonctionner uniquement sur la couche active
The new vertex is a lot more productive now. It can move vertices of all editable layers at once, which is great to preserve cross layers topology. However in many cases, many of us don\'t want to modify all layers at once. We added a variation of the vertex map tool just for that.

[![image12](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)

This feature was funded by [Oslandia](https://oslandia.com)

This feature was developed by [Paul Blottiere (Oslandia)](https://oslandia.com/en/home-en/)
### Fonctionnalité : Ajout d'un outil pour inverser le sens des lignes
A long awaited feature ! No more external plugin or algorithm to reverse a line\'s direction!

[![image13](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Fonctionnalité : Précision des géométries
Les couches vectorielles ont une option de configuration de précision. La précision définit la précision de l'emplacement des nœuds à enregistrer. Chaque nœud de géométries nouvelles ou modifiées est accroché à une grille de cette résolution. Pendant la numérisation, la grille est montrée pour guider l'utilisateur.

[![image14](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité : Suppression automatique des sommets en double
Lors de l'ajout ou de la modification de géométries sur une couche vectorielle, QGIS peut supprimer automatiquement les nœuds en double des géométries. Cette option est configurable dans l'onglet de numérisation des couches vectorielles.

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité : Vérification de la validité des géométries
La validité de chaque géométrie nouvelle ou modifiée peut être vérifiée si cette option est activée. Cela permet de communiquer de manière transparente à un utilisateur lorsqu'il y a des géométries erronées produites par la session d'édition en cours.

[![image15](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité : Vérification de la topologie pendant l'édition
Les contrôles de topologie peuvent être activés sur une couche. Sur les géométries nouvellement ajoutées et modifiées, les vérifications de la topologie peuvent être exécutées. Les vérifications seront exécutées lors de l'enregistrement de la couche ou lors d'un clic sur le bouton de vérification de la topologie dans le panneau de validation de la géométrie.

Les vérifications suivantes sont disponibles:
- Intersections
- Recouvrements
- Sommets manquants entre polygones voisins

This builds on top of the functionality of the geometry checker plugin which was implemented by [Sourcepole](https://sourcepole.ch).

[![image16](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gestion des données
### Fonctionnalité : Traduction des projets QGIS
Like QGIS and the plugins, the projects are translated with the Qt translation process. Means, it makes the translation according to a Qt Compiled Translation Source File (`.qm` file). When the user opens a project, QGIS checks for a `.qm` file laying in the same folder like the `.qgs` file, having the same name like the `.qgs` file and having the language-code as postfix of the users language (the language configured in the QGIS settings). To create the translation, in the project settings, there is an option to generate the `.ts` file, that can edited by programs like Qt Linguist or Transifex.

More information in [this blog post](https://new.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)

This feature was funded by [QGIS Usergroup Switzerland and QGEP Project](https://www.qgis.ch/en)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch/)
### Fonctionnalité: Changer le mode d'ancrage de la table des attributs à la demande¶
A button has been added to the Attribute Table toolbar for switching between docked and window mode on demand. Previously users had to change an option in the settings dialog and open a new table in order to switch between docked/undocked mode, but that\'s painful if you decide *after* a table is already open that you\'d like to dock/undock it\...!

[![image17](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Nouveau filtre de localisation pour rechercher dans toutes les couches
A new locator filter has been added which allows users to search across *all* layers in their project, by the layer\'s display expression.

The filter can be activated by using the prefix \'af\', or by making it a default search via QGIS options -\> Locator -\> Features In All Layer. Display expressions are defined in the vector layer properties under the display tab. Individual layers can be marked as not searchable in the Project Properties dialog, under the Data Sources tab.

[![image18](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)

This feature was funded by [Opengis.ch](https://www.opengis.ch/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Fonctionnalité: Couches qui ne peuvent pas être enlevées de l'arborescence du projet QGIS (obligatoires)
A new indicator \"locked\" icon is shown for any layers marked as \"required\" within the current project. This icon gives users instant feedback that a particular layer cannot be removed from the project.

Les couches requises sont configurées via la boîte de dialogue Propriétés du projet, onglet Sources de données.

[![image19](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Fonctionnalité : Ajouter une vouche raster à un Geopackage existant
When saving a raster layer to GeoPackage database, it\'s now possible to append the layer to an existing file.

[![image20](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
## Formulaires et widgets
### Fonctionnalité: Formulaires d'exploration (en cascade) dans les widgets de relation de valeur QGIS
New functions and logic in QGIS "Value Relation Widgets", allowing the implementation of complex, dynamic filters within QGIS attribute forms. The functionality can be used to implement "drill-down" forms within QGIS, where the values available in one field depend on the values of other fields:

[![image21](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)

This feature was funded by [QGIS community through crowd-funding](https://north-road.com/drill-down-cascading-forms/)

Cette fonctionnalité a été développée par Alessandro Pasotti (avec North Road)
## Composeur de Cartes
### Fonctionnalité: Éléments de carte 3D
Cette fonctionnalité permet aux utilisateurs d'ajouter leur vue de carte 3D au composeur d'impression.

[![image22](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
## Traitement
### Feature: New \"Edit in place\" mode
Thanks to a large number of [generous backers](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/), a crowdfunded \"edit in place\" mode was added to Processing for 3.4. When a vector layer is active and editable, this mode allows users to execute suitable algorithms directly on the features from the layer, modifying their attributes and geometries in-place. All edits are added to the layer's "edit buffer", so you can easily undo and redo the changes before saving them back to the data source.

For those power users who perform frequent data edits, this functionality is also exposed via QGIS 3.0's "Locator bar" (that "type to locate" bar which sits in the bottom-left corner). Typing 'ef' ("edit features") followed by the name of the corresponding operation allows you to perform the edits directly via the keyboard. E.g.
- Sélectionnez un ensemble d'entités linéaires
- Appuyez sur :kbd:`Ctrl+K` (active le localisateur)
- Type "ef reverse"
- Press enter -- the selected line features will be reversed immediately!

[![image23](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)

This feature was funded by [Crowdfunding campaign](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/)

This feature was developed by [North Road](https://north-road.com)
### Fonctionnalité: Stocker les modèles dans le projet
Some Processing models are so intrinsically linked to the logic inside a particular project that they have no meaning (or are totally broken) outside of that project (e.g. models which rely on the presence of particular map layers, relations, etc). Accordingly, from QGIS 3.4, Processing models can be stored inside QGIS project files. Any models stored within a project are made available as soon as that project is opened. This also avoids cluttering up the \"global\" model provider with models which make no sense, and makes it easier to distribute a single project all relevant models included.

Models are stored inside projects by clicking the new \"Embed in Project\" button in the Modeler dialog toolbar. Models can be removed from a project from the model\'s right click menu in the toolbox.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Exemples de valeurs raster
Un nouvel algorithme a été ajouté pour échantillonner les valeurs des couches raster aux emplacements des points.

[![image24](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)

This feature was funded by [Faunalia](https://www.faunalia.eu)

This feature was developed by [Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Feature: New \'Raster pixels to polygons\' algorithm
Cet algorithme convertit une couche raster en une couche vectorielle, avec une entité polygonale correspondant à chaque pixel du raster et un seul champ contenant la valeur de bande du raster.

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Fonctionnalité: K Means algorithme de clustering
QGIS 3.4 adds a native \"k-means clustering\" algorithm. Based on a port of PostGIS\' ST_ClusterKMeans function, this algorithm adds a new cluster ID field to a set of input features which identifies the feature\'s cluster based on a k-means clustering approach. If non-point geometries are used as input, the clustering is based off the centroid of the input geometries.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: algorithme de clustering spatial dbscan
Ce nouvel algorithme natif implémente une approche de cluster d'analyse basée sur la densité DBSCAN optimisée pour regrouper les fonctionnalités de points 2D.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Algorithmes améliorés
Certaines améliorations diverses apportées aux algorithmes de traitement existants incluent:
- L'algorithme *Reverse line direction* fonctionne désormais avec les entrées de géométrie MultiLineString
- *Extend lines*: la prise en charge des distances de début et de fin dynamiques (définies par les données) a été ajoutée
- *Offset lines*: la prise en charge de la distance de décalage dynamique a été ajoutée
- Les algorithmes *Join by Field Value* et *Join by Location* peuvent désormais éventuellement exporter des enregistrements sans correspondance
- *Join by Field Value* signale également le nombre de fonctionnalités appariées / non appariées

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Filtrer les sommets par les algorithmes M et Filtrer les sommets par Z
Deux nouveaux algorithmes ont été ajoutés pour filtrer les sommets des lignes / polygones par leurs valeurs M ou Z. Une valeur minimale et maximale M / Z peut être entrée, et si les sommets tombent en dehors de ces plages, ils seront rejetés de la géométrie de sortie. Les valeurs de filtre minimales et maximales peuvent également être définies par les données, elles peuvent donc varier en fonction des entités.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of Translated Features\" algorithm
Ce nouvel algorithme crée des copies d'entités dans une couche, en créant plusieurs versions traduites (décalées) de l'entité. Chaque copie est déplacée d'une valeur prédéfinie sur l'axe x / y / z / m.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of offset (parallel) lines\" algorithm
Ce nouvel algorithme crée des copies des entités linéaires dans une couche, en créant plusieurs versions parallèles de chaque entité. Chaque copie est décalée d'une distance prédéfinie.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité:  Choix d'unités pour les distances qui ne sont pas en degrés / inconnues
Lorsqu'un algorithme a un paramètre de distance en mètres / pieds / etc. (c'est-à-dire des distances non géographiques), une zone de liste déroulante a été ajoutée permettant de choisir le type d'unité.

(QGIS doesn\'t (and should **never**) expose this for distances in degrees \-- it\'s up to users in this situation to choose a suitable local projection and reproject their data to match.)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Feature: \"Drape features to z/m\" algorithms
Ces deux nouveaux algorithmes peuvent définir des valeurs de sommet de géométrie z ou m sur des valeurs échantillonnées à partir d'une bande raster. Les valeurs peuvent éventuellement être mises à l'échelle en utilisant une valeur d'échelle (définissable par les données).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Raster pixels to points\" algorithm
A new \"pixels to points\" algorithm was added in QGIS 3.4, which creates a point feature at the center of every pixel. nodata pixels are skipped.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Algorithme extraction partie d'une Ligne
Ce nouvel algorithme très demandé renvoie la partie d'une ligne (ou courbe) qui se situe entre les distances de début et de fin spécifiées (mesurées depuis le début de la ligne). Les valeurs Z et M sont interpolées linéairement à partir des valeurs existantes.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Interpolate point on line\" algorithm
Ce nouvel algorithme crée une géométrie ponctuelle interpolée à une distance définie le long des géométries de ligne (ou de frontière de polygone). Les géométries d'entrée courbes sont entièrement prises en charge. Les valeurs Z ou M sont interpolées linéairement en fonction des valeurs existantes.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: k-neighbour concave hull
This feature was funded by <https://qgis.org>

This feature was developed by [Detlev Neumann, Rudi von Staden](https://qgis.org)
### Fonctionnalité: Les scripts Python qui implémentent des algorithmes exécutent désormais l'algorithme par glisser-déposer et double clic du navigateur
Le cas échéant, les scripts lanceront désormais une boîte de dialogue d'algorithme de traitement sur:
- Glisser-déposer un script Python sur la fenêtre principale
- Using the browser panel\'s right-click run script action

[![image25](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: New GDAL\'s rearrange band algorithm
A new GDAL provider \'Rearrange band\' algorithm was added to the processing toolbox. The algorithm allows to output rasters continuing a subset of a given input raster\'s bands, and offers the possibility to re-order the bands.

[![image26](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)

This feature was funded by [iMHere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: \"Precalculated\" values for model algorithm parameters
A new option is present for all parameters of using a \"precalculated expression\". This expression is evaluated once before the child algorithm is executed and used during the execution of that algorithm.

This feature was funded by [QGIS](https://qgis.org)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Categorize a layer using a style XML file\" algorithm
This new algorithm sets a vector layer\'s renderer to a categorized renderer using matching symbols from a style database.

A specified expression (or field name) is used to create categories for the renderer, with QGIS creating a category for each unique value within the layer. Each category is individually matched to the symbols which exist within the specified QGIS XML style database. Whenever a matching symbol name is found, the category\'s symbol will be set to this matched symbol.

La correspondance ne respecte pas la casse par défaut, mais peut être rendue sensible à la casse si nécessaire. Facultativement, les caractères non alphanumériques dans la valeur de la catégorie et le nom du symbole peuvent être ignorés lors de l'exécution de la correspondance. Cela permet une plus grande tolérance lors de la correspondance des catégories aux symboles.

Si vous le souhaitez, vous pouvez également générer des tableaux contenant des listes des catégories qui n'ont pas pu être mises en correspondance avec des symboles et des symboles qui n'ont pas pu être mis en correspondance avec des catégories.

[![image27](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Nouveau mode pour l'algorithme Snap geometries
The new mode \"Snap to anchor nodes (single layer only)\" makes sure that any two vertices of the vector layer are at least at distance given by the threshold value.

Cet algorithme est pratique lorsque vous effectuez des opérations de superposition de vecteur telles que l'intersection, l'union ou la différence pour éviter d'éventuelles erreurs topologiques causées par des erreurs numériques si les coordonnées sont très proches les unes des autres. Après avoir exécuté l'algorithme, certaines géométries précédemment valides peuvent devenir invalides et il peut donc être utile d'exécuter ensuite l'algorithme Vérifier geometries.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Fournisseurs de données
### Fonctionnalité: Plugin méthode authentification OAuth2
- Prend en charge le code d'authentification, les flux d'octroi implicites et les propriétaires de ressources
- Permet des connexions préconfigurées, lues à partir des emplacements par défaut
- Offre la mise en cache du jeton d'accès au-delà des redémarrages de QGIS
- Enregistrer / charger des configurations

This feature was funded by [Monsanto Company](https://monsanto.com/)

This feature was developed by [Larry Shaffer, Alessandro Pasotti](https://qgis.org)
### Fonctionnalité: Couche de maillage: nouveau support de format de couche de maillage
Les couches de maillage représentent des données sur une grille de taille variable avec des composants supplémentaires (par exemple, le temps et le vecteur). Avec l'introduction de MDAL, les utilisateurs peuvent charger les formats suivants directement dans QGIS et explorer tous les autres composants:
- GRIB
- XMDF
- Netcdf

[![image29](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Couche de maillage: ajoutez une fonction pour identifier la valeur des couches de maillage
Avec cette API, les développeurs peuvent inspecter les éléments de maillage et récupérer des valeurs dans l'espace et dans le temps. Par exemple, vous pouvez créer un tracé de série chronologique à partir de votre couche de maillage.

[![image30](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Couche de maillage: permet de choisir différents jeux de données vectorielles et scalaires
Une couche maillée contient souvent plusieurs quantités. Par exemple, un netcdf / grib peut contenir plusieurs quantités météorologiques. Chaque quantité peut également avoir plusieurs composants. Par exemple, les données de vent peuvent contenir la vitesse (scalaire) et les valeurs (grille). Avec cette option, vous pouvez superposer des scalaires et des grilles de différentes quantités. Dans l'image ci-dessous, vous pouvez voir la température (grille) et le vent (scalaire).

[![image31](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Couche de maillage: autorisez les vecteurs / flèches de rendu sur la grille définie par l'utilisateur
Les données scalaires sont générées généralement au centre / coin de chaque élément de maillage. Lors de l'affichage des données scalaires, les flèches peuvent sembler clairsemées et il est souvent impossible de voir la tendance générale. Avec cette option, les flèches peuvent être affichées sur une grille définie par l'utilisateur. Des valeurs scalaires supplémentaires seront interpolées à la volée et placées sur la grille définie par l'utilisateur.

[![image32](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Prise en charge du type JSON / JSONB
The reading of PostgreSQL JSON types is supported. JSON Data can be displayed in the widgets as \"Key/Value\" (maps), as \"List\" (arrays) or as text.

[![image33](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité: Prise en charge de l'authentification par jeton ESRI
Support has been added to QGIS\' Authentication system for ESRI\'s temporary token based authentication. This allows for connection to ArcGIS Feature and Map Servers via an allocated temporary token.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: SQL Server - Gestion de géométrie non valide
Recent versions of QGIS have switched to a safer approach to reading SQL Server layers, which automatically checks for geometry validity and repairs geometries when needed. This workaround is required to avoid issues with the design of SQL Server\'s geometry handling, where encountering any rows with invalid geometries can silently abort a request without returning all the features from a layer. Unfortunately, the workaround comes at a significant performance cost.

In QGIS 3.4 a new setting was added to allow users to manually turn off QGIS\' SQL Server invalid geometry handling. Turning on the \"Skip invalid geometry handling\" setting under a SQL Server connection\'s properties causes QGIS to skip all the expensive geometry validation processing, but firmly places the responsibility for ensuring that all features on the database have valid geometries back upon the user/database administrator. **This is a \"use at your own risk\" setting. Improperly enabling this option can lead to missing features and data loss.**

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## QGIS Server
### Fonctionnalité: Le cache du serveur peut être géré par des plugins
Par défaut, QGIS Server met uniquement en cache le document WMS GetCapabilities en mémoire. Avec l'implémentation WMTS, il est nécessaire d'avoir un moyen de mettre en cache les tuiles. Mais le gestionnaire de cache n'a pas été développé pour ne mettre en cache que les tuiles.

Le plugin du gestionnaire de cache peut être utilisé pour mettre en cache :
- Documents GetCapabilities WMS, WFS, WCS, WMTS.
- Documents WFS DescribeFeatureType
- Documents WCS DescribeCoverage
- Images WMTS GetTile
- Images WMS GetLegendGraphic

Voici une classe de gestionnaire de cache python, qui ne vérifie pas si le projet QGIS a changé:

    class PyServerCache(QgsServerCacheFilter):
    
        """ Used to have cache control """
    
        def __init__(self, server_iface):
            super(QgsServerCacheFilter, self).__init__(server_iface)
    
            self._cache_dir = os.path.join(tempfile.gettempdir(), "qgs_server_cache")
            if not os.path.exists(self._cache_dir):
                os.mkdir(self._cache_dir)
    
            self._tile_cache_dir = os.path.join(self._cache_dir, 'tiles')
            if not os.path.exists(self._tile_cache_dir):
                os.mkdir(self._tile_cache_dir)
    
        def getCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                return QByteArray()
    
            doc = QDomDocument(m.hexdigest() + ".xml")
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "r") as f:
                statusOK, errorStr, errorLine, errorColumn = doc.setContent(f.read(), True)
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            return doc.toByteArray()
    
        def setCachedDocument(self, doc, project, request, key):
            if not doc:
                print("Could not cache None document")
                return False
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "w") as f:
                f.write(doc.toString())
            return os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                os.remove(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
            return not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocuments(self, project):
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            for f in filelist:
                os.remove(os.path.join(self._cache_dir, f))
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            return len(filelist) == 0
    
        def getCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                return QByteArray()
    
            img = QImage(m.hexdigest() + ".png")
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "rb") as f:
                statusOK = img.loadFromData(f.read())
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            img.save(buff, 'PNG')
            return ba
    
        def setCachedImage(self, img, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "wb") as f:
                f.write(img)
            return os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                os.remove(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
            return not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImages(self, project):
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join(self._tile_cache_dir, f))
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            return len(filelist) == 0
    
Et la façon de l'ajouter au gestionnaire de cache de QGIS Server.

`servercache = PyServerCache(server_iface) server_iface.registerServerCache(servercache, 100)`

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### Fonctionnalité : Support du WMTS 1.0.0
QGIS Server 3.4 prend en charge la norme OGC WMTS 1.0.0

Dans les propriétés du projet QGIS, l'utilisateur peut définir:
- quelle partie du projet (tous les projets, groupes de couches ou couches) doit être publiée via la norme WMTS
- l'échelle min des tuiles

QGIS Server réutilise le SCR défini dans le WMS pour WMTS

Pour gérer le cache de tuiles, un plug-in QGIS Server avec une classe QgsServerCacheFilter doit être installé et chargé par QGIS Server.

[![image34](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### Fonctionnalité: Ajouter la possibilité de définir un min. échelle pour le flux WMTS
This feature was funded by <https://github.com/rldhont>

This feature was developed by <https://github.com/rldhont>
### Fonctionnalité: Prise en charge des journaux QGIS Server sur stderr
It\'s now possible to configure QGIS Server to make it write its logs to stderr. This is done by setting the QGIS_SERVER_LOG_FILE env var to the special value \"stderr\".

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Eric Lemoine](https://github.com/elemoine)
## Extensions
### Fonctionnalité: Prise en charge des zips chiffrés dans Plugin Manager
Plugin Manager peut désormais installer des plugins à partir de fichiers zip locaux même s'ils sont cryptés.

[![image35](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
### Fonctionnalité: Édition hors ligne de GeoPackage
Avec la fonctionnalité d'édition hors ligne, il est possible de choisir si l'exportation doit créer un fichier SpatiaLite ou GeoPackage pour une utilisation hors ligne.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
## Programmation
### F
A very fast static spatial index for 2D points based on a flat KD-tree, using <https://github.com/mourner/kdbush.hpp>

Compared to QgsSpatialIndex, this index: - supports single point features only (no multipoints) - is static (features cannot be added or removed from the index after construction) - is much faster! - supports true \"distance based\" searches, i.e. return all points within a radius from a search point

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: QgsRasterDataProvider :: méthode d'échantillonnage pour un échantillonnage efficace des rasters à un point donné
This is an alternative to the `QgsRasterDataProvider::identify` method, which is less efficient but more powerful

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Nouvel appel d'API de géométrie pour renvoyer une sous-chaîne de courbe
Une nouvelle API PyQGIS a été ajoutée pour faciliter la récupération d'une sous-chaîne à partir d'une géométrie LineString / Curve:

`QgsCurve::curveSubstring - Returns a new curve representing a substring of a curve, from a start distance and end distance.`

If z or m values are present, the output z and m will be interpolated using the existing vertices\' z or m values. The method also handles curved geometries without loss or segmentation.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Fonctionnalité: Modifications de l'API du module sip
Due to upstream changes within the PyQt/sip library, the recommended way to import this module has changed in QGIS 3.4. For maximum portability, instead of directly calling: `import sip` plugins should instead use: `from qgis.PyQt import sip` Using this newer style import will ensure that the code works correct across all platforms and remains functional in future QGIS versions.
### Fonctionnalité: Fournisseurs de données vectorielles Python
Développement de l'API, d'un exemple de fournisseur et de tests permettant la création d'un fournisseur de données vectorielles en python.

[![image36](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)

Cette fonctionnalité a été financée par bonne volonté !

Cette fonctionnalité a été développée par Alessandro Pasotti
## Fonctionnalités 3D
### Fonctionnalité: Amélioration de la navigation
This will update camera\'s view center as the camera moves around. Before the view center would be always at the zero elevation, which means that with terrain further away from zero elevation tilting and rotation of camera would feel weird due to the center point being far away.

Autoriser le déplacement de la caméra vers le haut / bas à l'aide des touches de page haut / bas

Déplacer la caméra en gardant la position avec Ctrl + touches fléchées / souris

[![image37](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Animations 3D
Vous pouvez créer une animation basée sur un ensemble d'images clés - les positions des caméras à des moments particuliers. QGIS 3D interpole ensuite les positions / rotations de la caméra entre les images clés.

Pour créer les images clés, définissez d'abord la scène de votre carte, en faisant pivoter, zoomer ou déplacer la caméra. Attribuez ensuite une heure au cadre. Il existe plusieurs méthodes d'interpolation entre les images clés.

[![image38](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martian Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Rendu simple des lignes 3D
Ce mode de rendu de ligne 3D utilisera le rendu de ligne OpenGL au lieu de réaliser un tampon les lignes en polygones et de les rendre sous forme de maillages.

The advantage is that the 3D lines do not loose their Z coordinate which is the case currently with \"ordinary\" 3D rendering after buffering.

The disadvantage is that the lines cannot be wide (supported in Qt3D only since 5.10, but even then their rendering won\'t have nice joins/caps) and only ambient color is used from the material.

[![image39](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Fonctionnalité: Outil de carte d'identification pour les vues 3D
Un nouvel outil d'identification a été introduit sur la carte 3D. À l'aide de cet outil, vous pouvez inspecter des entités de la scène 3D.

[![image40](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)

This feature was funded by [Department of Environment, Land and Infrastructure Engineering (DIATI)](https://www.faunalia.eu/en/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Fonctionnalité : API Python expérimentale
Certaines classes de QGIS 3D ont été mises à la disposition des développeurs Python. Il est désormais possible d'interroger ou de modifier les rendus 3D des couches de carte et les propriétés de lecture / écriture des symboles 3D contenus tels que les couleurs des matériaux. Veuillez noter que pour l'instant l'API est considérée comme expérimentale, elle peut donc changer dans les futures versions 3.x.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
