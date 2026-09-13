---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: projet
sidebar: true
title: Modifications apportées par QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 2.4{#changelog24 }
Date de publication : 27/06/2014

Liste des changements dans la version QGIS 2.4.0. Une attention particulière a été portée sur les performances et l'affinage, nous avons rajouté de nombreuses fonctionnalités et améliorations pour rendre l'interface plus cohérente et professionnelle (et nous l'espérons, plus simple à utiliser). Le composeur de cartes (utilisé pour l'impression) a été l'objet de beaucoup d'efforts pour en faire un outil plus adapté à la création de superbes sorties cartographiques.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Nous souhaitons remercier tous les développeurs, rédacteurs, testeurs et les nombreuses personnes qui ont donné volontairement de leur temps (ou financé des personnes pour le faire).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Enfin, nous souhaitons remercier nos sponsors officiels pour leurs soutiens financiers inestimables à ce projet :
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Général
### Feature: Generate band name with NetCDF EXTRA_DIM
NetCDF a fourni des informations extra-dimensionnelles. Cette information fournit des métadonnées sur chaque bande. Ces métadonnées peuvent être utilisée pour expliciter le nom de chaque bande. Par exemple, les bandes d'un fichier NetCDF représentant la température à une profondeur donnée. Pour l'utilisateur, il est plus facile de sélectionner une bande avec l'information de profondeur plutôt que d'utiliser uniquement le numéro de bande.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Fonctionnalité: Application d'une échelle et d'un décalage pour les données raster
Pour certaines sources de données raster, les données sont stockées sous forme d'entier avec une échelle et un décalage dans les métadonnées. L'échelle et le décalage peuvent être utilisés pour récupérer les bonnes valeurs. QGIS les applique aux données raster pour afficher l'information juste dans les légendes, les histogrammes et pour l'identification.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Fonctionnalité: Barre d'accès rapide de calcul de champs dans la table d'attributs
Nous avons une nouvelle fonctionnalité intéressante pour ceux qui travaillent avec les champs calculés des tables d'attributs des couches vecteur. La nouvelle barre d'accès rapide de calcul vous permet de mettre à jour des valeurs dans une colonne de la table d'attributs de manière facile et rapide.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Fonctionnalité: Modes de prévisualisation de couleur dans le canevas de cartes et le composeur
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Fonctionnalité: Fichiers de couche QLR pour QGIS
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Fonctionnalité : Nouvelle fonction d'expression
Nous avons de nouvelles fonctions disponibles dans le constructeur de requêtes
- rectangle d'emprise (bounds)
- bounding box width & height (bounds_width/bounds_height)
- coordonnées x/y min/max (xmin/xmax/ymin/ymax)
- La nouvelle fonction wordwrap renvoie une chaîne avec un retour chariot, suivant un nombre minimum ou maximum de caractères

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Fonctionnalité : Copier, coller et glisser-déposer des couleurs
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Fonctionnalité: Rendu graphique Multi-fils d'exécution
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Étiquetage
### Fonctionnalité : Étiqueter plusieurs fois une même entité
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Composeur de Cartes
### Fonctionnalité: Améliorations des éléments d'image du composeur
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Fonctionnalité: Echelles prédéfinies pour les cartes d'atlas
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Fonctionnalité: Améliorations des tables attributaires dans le composeur
Nous avons réalisé quelques améliorations sur l'affichage des tableaux dans la présentation des compositions:
- Ajout de la gestion de l'ordre des colonnes au sein du tableau
- Ajout de la gestion des colonnes basées sur une expression
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Le contenu de la table peut être filtré à l'aide d'une expression

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Fonctionnalité : Amélioration générale du composeur
Il existe quelques ajouts au composeur de cartes pour rendre la vie plus facile lorsqu'on travaille à la composition de cartes:
- Ajout d'un bouton pour visualiser l'emprise de l'élément de carte courant dans le canevas de carte.
- Possibilité d'exporter des images SVG avec des coches depuis le composeur
- Gestion du mode de jointure de ligne et du style de croisement pour les barres d'échelle
- Gestion du type de jointure de ligne pour les éléments de cadre

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Fonctionnalité: Amélioration des cadres HTML
Les cadres HTML du composeur ont été améliorés. Il existe un nouveau bouton **Ajouter un cadre** qui peut être utilisé pour créer manuellement de multiples cadres HTML liés. Nous avons également amélioré la logique de césure de page pour limiter les coupures au milieu des lignes de texte lors de la pagination des cadres HTML.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Extensions
### Fonctionnalité: Extension de client de catalogue MetaSearch
MetaSearch est une extension QGIS permettant d'interagir avec des services de catalogage de données. MetaSearch supporte le standard OGC Catalogue Service for the Web (CSW). Cette extension fournit une interface d'approche simple et intuitive pour effectuer des recherches dans les catalogues de métadonnées au sein de QGIS. Elle est maintenant fournie par défaut avec l'installation générale de QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Symbologie
### Fonctionnalité: Remplissage dégradé suivant la forme
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Fonctionnalité: Option pour décaler l'emplacement des marqueurs de ligne
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Fonctionnalité: Nouveau rendu par polygone inversé
Un nouveau rendu a été ajouté pour les éléments polygones qui permet de styler tout ce qui est à l'**extérieur** de vos polygones. Cela peut être utile pour mettre en valeur des emplacements ou pour créer des masques cartographiques. Combiné au nouveau style de remplissage dégradé selon la forme, vous pouvez maintenant produire des cartes comme celle présentée ci-après.

**Note:** La nouvelle version de l'extension mask facilite la création de couche de masque à partir de la sélection courante, permet l'étiquettage des entités présentes uniquement dans ces zones et génère automatiquement un masque dans les cartes générées par l'atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Fonctionnalité: Sauvegarder et récupérer les styles des couches Spatialite
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
