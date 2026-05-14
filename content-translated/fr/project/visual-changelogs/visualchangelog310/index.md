---
HasBanner: false
draft: false
releaseDate: '2019-10-25'
section: projet
sidebar: true
title: Modifications apportées par QGIS 3.10
type: visual-changelog

---
{{<content-start >}}
# Modifications apportées par QGIS 3.10{#changelog310 }
![image1](images/projects/ce6ba8fc893e51ec721c9dded4dd98d11806a223.png)

Release date: 2019-10-25

QGIS 3.10 apporte une longue liste de nouveaux changements et de nombreuses améliorations des fonctionnalités existantes - dont nous allons essayer de parler ici. Comme toujours, nous pouvons vous rappeler que QGIS est un projet open source et si vous le pouvez, pensez à soutenir notre travail par des dons ou des contributions à la documentation du code, au site web, etc.

**Remerciements**

Nous souhaitons remercier les développeurs, rédacteurs de documentation, testeurs et tous ceux qui ont volontairement donné du temps (ou donné de l'argent). La communauté QGIS espère que vous apprécierez cette version ! Si vous souhaitez donner un peu de votre temps, d'argent ou d'une manière d'une autre vous impliquer pour rendre QGIS encore plus génial, faites un tour sur `qgis.org <http://qgis.org>`__ et donnez nous un coup de main !

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS est un logiciel gratuit et vous n'avez aucune obligation de payer quoi que ce soit pour l'utiliser - en fait nous voulons encourager les personnes de tous horizons à l'utiliser quel que soit l'état de leurs finances ou leur statut social - nous pensons que mettre à disposition un outil géographique de prise de décisions participera à une meilleure société pour l'humanité entière.

{{<table-of-contents >}}
## Outils cartographiques
### Fonctionnalité : Longueurs de ligne 3D affichées dans l'outil d'identification
L'utilisation de l'outil d'identification sur une ligne 3D inclut maintenant la longueur cartésienne 3d de la ligne dans les résultats (en plus des longueurs cartésiennes 2D et ellipsoïdales 2D existantes).

![image2](images/entries/b1aba6e9334ee1d862bde8f66f9ae4d30d945703.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Symbologie
### Fonctionnalité : Paramètre de rééchantillonnage par défaut pour l'ajout de nouvelles couches raster
In QGIS 3.10 we\'ve added a new setting for the default resampling mode to use when for newly-added raster datasets. (This setting can be found in the rendering panel of the options dialog).

![image3](images/entries/07ae51e244cc5b1d6a971e386ea98f1314a3dfb1.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Amélioration du copier/coller des symboles
We\'re passionate about making QGIS a user-friendly cartographic tool which is a joy to work with, so we\'ve added a bunch of new shortcuts throughout the interface which allow you to copy and paste symbols from one part of QGIS to another. E.g, you can copy a symbol from a category and paste it directly onto another category, or a layout shape item, or inside the style manager dialog!

![image4](images/entries/79f8365571da7b6c60f001f388d9c02d9e8920b2.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \"Center of segment\" placement mode for marker and hash line symbol layers
We\'ve added a brand new \"Center of segment\" mode for placement of marker line or hashed lines symbols. This allows you to place markers or hash lines over the center point of individual line segments, exposing cartographic effects which were not possible before (and improving the quality of layers converted from ArcMap using the [SLYR](https://north-road.com/slyr/) tool).

![image5](images/entries/c1f50067d50b909e38b7333ad5d8d415e763801d.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Expressions plus flexibles de définition de décalage par les données attributaires 
In previous QGIS releases, only string values of the format \'x,y\' would be permitted for data-defined symbol and label offsets. We\'ve listened to user feedback that this was confusing, and in QGIS 3.10 we now allow arrays of numbers as a valid expression result for offsets. E.g. \"array(3,5)\".

![image6](images/entries/1ccab8f4328238f5275e41c3d466bf27a5d097a2.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Étiquetage
### Fonctionnalité : Créez et gérez des formats de texte et des paramètres d'étiquettes dans les styles QGIS
In QGIS 3.10 we\'ve finally implemented a long-awaited feature, allowing users to manage their own libraries of custom text formats and label settings alongside their existing symbol libraries!

Now, the Style Manager dialog can be used to manage text formats (which store the font, color, buffers, shadows, and backgrounds of text formats) and layer-wide label settings. (A \"text format\" includes just font settings and other appearance related settings, while a \"labe setting\" also includes layer-type specific settings such as label placement, priority, and rendering settings).

Text Formats and Label Settings offer all the same functionality as you\'re used to for managing symbols and color ramps within styles, including import and export to XML files, tagging, smart groups, favoriting etc\...

![image7](images/entries/bf657c21ba6deaff10ff80611a77b435e12155e5.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [North Road](http://north-road.com)
### Fonctionnalité : Symboles de marqueur comme fond d'étiquette
Alongside all the other exciting labeling improvements which we\'ve landed in 3.10, we now allow use of marker symbols as a background for labels. This allows you to use all the rich functionality available for marker symbols as a background to labels, and complements the existing shapes and SVG background choices!

![image8](images/entries/3a9fd11192cdbdaa2f139a28d63cc33e1d10c3bc.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [North Road](http://north-road.com)
### Fonctionnalité : Légendes (connecteurs) pour les étiquettes !
A common practice when placing labels on a crowded map is to use \'callouts\' - labels which are placed outside (or displaced from) their associated feature, with a line connecting the label and the feature. In QGIS 3.10, we\'ve added native support for quickly and easily creating beautiful label callouts (no more expression mangling or drawing by hand!).

We\'ve added many settings for controlling exactly how these label callouts are drawn, and naturally, you can take full advantage of the richness of QGIS line symbol support within your callouts! This includes all the existing line symbol styles, layer effects, and even support for data-defined settings!

In 3.10, we expose options for either a \"simple\" (direct line) or \"Manhattan\" (straight lines) callout styles. If you\'re interested in sponsoring additional callout styles in a future release, get in contact with the QGIS team to find out how you can make this happen!

![image9](images/entries/7bcc02d06eb7030a289e129b9bed2656d6c6fefb.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Modifier l'alignement d'étiquettes sur plusieurs lignes pour des étiquettes individuelles
We\'ve added an additional option to allow you to control multi-line alignment on a label-by-label basis. Just active the Label Properties tool and click on your map labels, and a new setting for the text alignment is now available.

![image10](images/entries/14b307efef5de1085e4c402d3e06e5dd10a64ae2.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Afficher les étiquettes non placées
If you\'ve ever been concerned about automatic label placement hiding away important labels on your map \-- this feature is for you! In QGIS 3.10 we\'ve added an option to show \"Unplaced labels\" on your map, so you can see immediately exactly what\'s been hidden from view (AKA \"see what others can\'t\")!

This new setting (which is accessed through the Labeling toolbar) will render these Unplaced Labels in a red color (but the color can be changed from the project Label Settings dialog). After identifying any missing labels in your map, we suggest you use the existing Labeling tools such as the \"move label\" or \"show/hide label\" tool to rearrange your map and make these labels visible again.

![image11](images/entries/4e53a6482dacb6e2d6d1ff2a8c4592d98f82430a.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Distance de dépassement pour les étiquettes de ligne
We understand that making a cartographic masterpiece is a demanding task, so in QGIS 3.10 we\'ve extended the capabilities of curved labels by adding a new \"overrun distance\" setting. This setting allows you to control exactly how far a curved label is allowed to extend past to ends of a line feature. Bumping up the distance will result in giving the labeling engine more flexibility in placing your labels, resulting in more labels being placed in better locations on your map! Win! The setting works for both curved and parallel label modes, and supports distances in mm/map units/pixels/etc, and data-defined distances.

![image12](images/entries/0b830e5ea769aacfd9c5bf9d8028ed278590d803.gif)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Data defined control for \"label every part of multipart features\" setting
The \"label every part\" option was one of the very few settings which couldn\'t be previously data-definable for labels. We\'ve remedied this omission in QGIS 3.10, and you can now control whether you want all parts labelled on a feature-by-feature basis!

![image13](images/entries/9db2c54c0d65bc61da8c0c46cfefcbab96c833df.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Control \"label all parts\" via the label properties tool
We aren\'t lying when we say that QGIS 3.10 is a love-letter to map labelling! Another new option we\'ve added in this version is interactive control over whether all parts of a feature should be labeled via the Label Properties tool.

![image14](images/entries/737cd2f8bc569ee9ad7df9aee02eec83b4e6facd.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Orientation verticale du texte
Avec la version 3.10, QGIS est maintenant entièrement équipé pour le rendu d'étiquettes orientées verticalement. À nos utilisateurs chinois, japonais et coréens : faites passer le mot ! :)

Vous pouvez choisir entre deux modes d'orientation verticale : un mode qui rend toujours les étiquettes verticalement, ou un mode alternatif qui choisit dynamiquement l'orientation en fonction de la rotation des étiquettes.

![image15](images/entries/e49baccdb83da1b88433e2c7718642ae4a78810d.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Contrôle du crénage des polices
Another option we\'ve added for improving the conversion of ArcMap symbology to QGIS (via [SLYR](https://north-road.com/slyr/)) is a new setting for controlling whether label fonts are kerned (or not).

![image16](images/entries/b2a650a874e263173a56d93b046df7f031eb8d6e.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Rendu
### Fonctionnalité : Rendu de couches raster en dehors de l'étendue rapportée
Depending on the server technology used, sometimes the map extent reported by raster layers may be smaller than the actual area which can be rendered (especially notably for WMS servers with symbology which takes more space than the data extent). Previous version of QGIS would crop raster layers to the reported extents, resulting in truncated symbols on the borders of these layers. Now, there\'s a new option to allow you to override this behaviour and ignore the reported extent for affected servers.

Cette fonctionnalité a été développée par Matthias Kuhn (Opengis.ch)
### Fonctionnalité : Géo-référencement des fichiers PDF et TIF lors de l'enregistrement du canevas de la carte sous forme d'image/PDF
In QGIS 3.10 we\'ve implemented support for embedded georeferencing within PDFs and TIFs when using the save \[map canvas\] as image or PDF.

![image17](images/entries/1030adf0c9c0c46ff5a38a09ae16a735bdff3684.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Nouvelle décoration d'image sur le canevas de  carte
We\'ve added a brand new decoration for the QGIS main canvas, allowing you to add a bitmap and SVG image overlay (logo, legend, etc.) to your map window.

Comme pour les autres parties de QGIS, la décoration de l'image prend en charge les paramètres de couleurs de remplissage et de contour personnalisables pour les SVG .

![image18](images/entries/41ab256b477b0baf0971b398f882a6633cd12615.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Classification par échelle logarithmique¶
Vous pouvez maintenant utiliser une technique de classification logarithmique lors de la création de classes pour le mode de rendu gradué.

![image19](images/entries/bb6303d9589972781988549283ef150700ba5863.webp)

This feature was developed by [OPENGIS.ch](https://www.opengis.ch)
## Fonctionnalités 3D
### Fonctionnalité : Outil de mesure en vue carte 3D
Now you can measure distances in 3D map views! This new tool is available in the 3D map view toolbar, and has the same workflow as the 2D measurement tool (with the same configuration settings of rubber band color, units, decimal place, etc). It also has the same behavior (left-click to add a new point, middle-click to delete the last point, and right-click to restart the measurement). This allows you to measure distances in 3d, e.g. the distance between two building's roofs or the length of a river running down a mountain. See the 3D measurement tool in action:

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
### Fonctionnalité : Rendu de l'affichage pour les points
Nous avons ajouté un nouveau style de rendu pour les couches de points. Il permet d'afficher le point avec un symbole QGIS (par ex. marqueur, SVG, etc.) qui fait toujours face à l'utilisateur et a toujours la même taille. Vous pouvez voir un exemple d'utilisation dans la vidéo.

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
### Fonctionnalité : Navigation 3D à l'écran
Dans les versions antérieures de QGIS, vous pouviez déjà naviguer dans le monde 3D en utilisant une souris et un clavier. Malheureusement, pour un nouvel utilisateur, il n'est pas facile de commencer à les utiliser ! La navigation 3D à l'écran vous aidera à naviguer dans le monde 3D. Il y a des boutons pour faire un zoom avant/arrière, incliner vers le haut/le bas, faire un panoramique vers le haut/le bas/gauche/droite, et faire pivoter la vue de la carte 3D. Cette fonction peut être activée à partir de la barre d'outils de la vue 3D de la carte. Voyez comment l'utiliser dans cette vidéo :

![image20](images/entries/570ff6f8c365a78d05bb56cfdbd8647f83aac331.webp)

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
## Mises en page de cartes
### Fonctionnalité : Disposition de droite à gauche pour les légendes
Thanks to funding from our right-to-left locale users, we\'ve added a new choice for arrangement of legend elements. These include symbols to the left OR symbols to the right of the legend text, and alignment options for groups, subgroups and item text.

Cette fonction permet de créer des légendes locales de droite à gauche. Pour rendre les choses conviviales, nous avons choisi par défaut l'alignement de de droite à gauche lors de la création de nouvelles légendes pour les utilisateur avec une locale basée sur RTL (Droite-A-Gauche).

![image21](images/entries/420b784c4fc79a09358201c8814cfe48b82dbbca.webp)

This feature was funded by [Kaplan Open Source](https://kaplanopensource.co.il/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Marge de contrôle des groupes et sous-groupes dans les légendes
If you\'re after pixel-perfect control over your legend appearance \-- this one\'s for you! QGIS 3.10 now allows you to tweak the spacing applied under group or subgroup headings.

![image22](images/entries/78263d3350afd05147928378f81dddba13961acc.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Paramètres définis par les données pour les formats texte
Since so much of QGIS\' cartographic power comes from the flexibility of data-defined symbol settings, we\'ve now allowed them to be used for text formats too! This means you can now use data defined properties wherever text formats are used, e.g. within layout scalebar text.

![image23](images/entries/69961f6faa732b683ccfb1ab539250b21ea5bd26.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \@scale_value variable
To complement the new support for data-defined settings within text formats, we added a new \@scale_value expression variable. This can be used when evaluating data defined text format properties while rendering scale bar text, and ultimately allows you to have per-label customisation of the text format inside scale bars (e.g. showing certain distance labels in bold).

![image24](images/entries/ec2940b4222b8172403b20b0f70af0588c38f0cc.gif)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : options de placement des étiquettes barre d'échelle
We\'ve extended layout scale bars with additional styling options, adding a pair of settings to refine the placement of scalebar labels. Now you can define whether labels are shown above or below the scalebar itself, as well as setting whether labels are centered in the middle of a segment or placed at its end.

![image25](images/entries/e571fc1811ccf58e007a7913600b65377e31ed41.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Simplifier les exports PDF ou SVG
Les versions précédentes du QGIS produisaient souvent d'ÉNORMES sorties PDF (ou SVG), car ces sorties comprenaient de nombreux sommets redondants qui n'étaient discernables suivant le DPI d'exportation. Maintenant, par défaut, nous appliquons une simplification lors de l'écriture de fichiers PDF ou SVG, ce qui simplifie les géométries et supprime automatiquement tous les sommets redondants (par exemple, si le DPI d'exportation est de 300 dpi, les sommets distants de moins de 1/600 pouces seront supprimés).

This new setting, \"Simplify geometries to reduce output file size\", is exposed in the SVG or PDF export settings dialogs shown when exporting a layout/atlas/report to PDF or SVG.

No more ridiculously complex and large export file size for your QGIS print layouts! Aside from the file size issues, these also cause problems when trying to load into other applications, e.g. Inkscape, which chokes on the huge number of vertices and grinds to a crawl\.... ouch!

![image26](images/entries/7eea84e316a148c6872369d3df5fb63a6bc2f043.webp)

Cette fonctionnalité a été financée par GeoPDF export group: Land Vorarlberg; Cantons of Zug, Thurgovia and Neuchâtel; Cities of Vienna and Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Amélioration des exportations en couches SVG
User feedback told us that the way we created layered SVG files in past releases was frustrating to work with. So, in QGIS 3.10, we\'ve revamped this feature and now SVG layer names will match the layer names from QGIS, making it much easier for designers to understand the contents of the document! Read more about this are related features [here](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/).

![image27](images/entries/dac35ad47f56dd24456df6d318359a0d70efeb15.webp)

Cette fonctionnalité a été financée par GeoPDF export group

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Mise en page : Indicateur de rafraichissement de carte.
In earlier QGIS releases, there was no way to tell whether a map refresh had finished inside a QGIS print layout designer window. So, we\'ve added a new indicator in the status bar which shows whenever there\'s a redraw is humming away in the background. No more user confusion!

![image28](images/entries/8c6426a723b9fdc1cead1949f3304db4763ecb9c.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Export en GeoPDF
If you export PDF\'s from QGIS now, there is an option to export it as GeoPDF. If you open this PDF with a compatible PDF viewer, you will then be able to toggle layers on and off, pan and zoom around the PDF and interactively interrogate features! Futhermore, you can re-import these GeoPDF documents back into QGIS as vector layers, and see all the features in their original locations and with their original attribute values.

GeoPDF export is available for either print layouts or map canvas exports. We\'ve added lots of flexibility to this new option, e.g. with options for controlling which layers will be exported as interactive layers. You can even choose to export multiple map themes into a single GeoPDF document, so that your readers can interactive switch between these themes! (Wow!)

Notez que l'exportation GeoPDF nécessite une compilation QGIS basée sur GDAL 3.0 ou supérieur.

Read more at [QGIS 3.10 Loves GeoPdf](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/)

![image29](images/entries/9f73cce9c3f3ff81c6b66adab654ff4e23524ae1.webp)

Cette fonctionnalité a été financée par GeoPDF export group: Land Vorarlberg; Cantons of Zug, Thurgovia and Neuchâtel; Cities of Vienna and Dornbirn; Biodiversity Information Service for Powys & Brecon Beacons National Park

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : définition de la grille
We\'ve added data defined control over layout map grids, to give you extra flexibility in the appearance and behaviour of these grids, and to allow you to create layout templates and atlases with grids which dynamically respond to map scale changes.

Now, you\'re able to set data-defined control for:
- Etat d'activation de la grille
- Intervalles x/y de la grille
- Offsets x/y de la grille
- Taille et marge du cadre de la grille
- Distance d'annotation par rapport au cadre de la grille
- Taille de croix de grille
- Epaisseur de ligne du cadre de la grille

![image30](images/entries/e219a18e997a6506314c1777c94050bf4a69cf9b.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Tailles de grille dynamiques
Just like the existing scalebar setting of the same name, this new setting allows you to set a page-size-based range for map grid intervals. The grid interval will be dynamically calculated based on the map extent and scale to pick the largest possible \"pretty\" interval which results in grid sizes inside the desired range.

Cette modification vous permet de créer des mises en page et des modèles de mise en page avec des grilles qui répondent avec élégance à une large gamme d'échelles de carte !

![image31](images/entries/245ada907ba2e14ad291dae54b93adb327b64225.webp)

Cette fonctionnalité a été financée par Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Signets spatiaux pour les cartes dans les mises en page
Another long-requested feature we\'ve implemented for QGIS 3.10 is a new button in the layout map item properties toolbar, which allows you to directly set a map item to the extent of a spatial bookmark!

![image32](images/entries/4b8ed681a38435a2f0bf299fd28f299e2873848c.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Expressions
### Fonctionnalité : Nouvelle fonction d'expression
- **attributes()**: returns a map containing all attributes from a feature, with field names as map keys. We\'ve got flexible, robust support for working with map values in expressions now, so this allows rapid conversion of all feature attributes to a map to use with these handy functions!
- New optional \"format\" parameters were added to the **to_date**, **to_datetime**, and **to_time** functions
- | **collect_geometries**: this new function collects a set of geometries into a multi-part geometry object. Geometry parts can either be specified as separate arguments to the function or (more flexibly), as an array of geometry parts. This function allows geometries to be generated using iterator based approaches, such as transforming an array generated using generate_series, e.g: | `collect_geometries( array_foreach( generate_series( 0, 330, 30), project($geometry, .2, radians(@element)) ) )` | Gives a nice radial effect of points surrounding the central feature point when used as a MultiPoint geometry generator
- A new **make_line** expression function variant which accepts an array of points. This allows creation of lines from variable numbers of points, and from sequences from aggregates/dynamically generated sequences.

## Numérisation
### Fonctionnalité : prise en charge de l'horodatage GPS
We\'ve overhauled the existing GPS based functionality in QGIS 3.10, adding new options for automatically retrieving and storing GPS timestamps alongside GPS based features.

This feature was funded by [NIWA](https://niwa.co.nz/)

This feature was developed by [Alessandro Pasotti (North Road)](http://north-road.com)
### Fonctionnalité : Exceptions d'écart autorisées
In QGIS 3.4 we introduced the ability to configure QGIS layers to run topological checks on every save operation. For 3.10, we have now added a new option to the check for \"gaps\" which allows you to actively mark some gaps as allowed. These exceptions will be saved on a separate, configurable layer. Whenever a gap is detected, you either have the possibility to fix it or to add it to the allowed exceptions with the press of a button.

![image33](images/entries/4a7b306942755ac96cfa9bc97abbfd7815d17ad4.webp)

This feature was funded by [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Gestion des données
### Fonctionnalité : Clés étrangères composites
In QGIS 3.10, we added the possibility to create layer relationships which utilise composite foreign keys. QGIS now fully supports editing parent and child features which are linked with more than one attribute. This functionality is accessed in the Project Properties -\> Relations tab.

![image34](images/entries/6b2177a5781bc2d5cdfb63f121501a734897e4a1.webp)

This feature was funded by [California Geological Survey](https://www.conservation.ca.gov/cgs)

This feature was developed by [OPENGIS.ch](https://www.opengis.ch)
### Fonctionnalité : Ajouter des dépendances de données circulaires
Avez-vous déjà eu des problèmes de capture lors de la modification d'une entité modifiée par quelqu'un d'autre (ou par un trigger de base de données) ? Les dépendances de données permettent d'actualiser le contenu des couches dépendantes lorsque les données sont modifiées. Nous avons amélioré la prise en charge des dépendances dans QGIS en permettant d'actualiser la couche modifiée elle-même, qui est une sorte de dépendance circulaire (une couche ponctuelle et une couche linéaire dépendantes l'une de l'autre par exemple). Plus besoin de capturer les fonctionnalités fantômes !

More info in the [pull request](https://github.com/qgis/QGIS/pull/30947)

![image35](images/entries/3b93e7b25eef3e3f149ba8db022e467258a74116.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Formulaires et widgets
### Fonctionnalité : Mise à jour des widgets en temps réel
Mise à jour les valeurs des widgets en temps réel lors de l'édition des champs référencés. Lorsque le widget A contient une valeur par défaut dépendant du widget B, il se met à jour dès que le widget B est édité.

![image36](images/entries/0f24e8e2746cb4b7890d015c2ae476f1f1bf96ef.webp)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
## Outils d'analyse
### Fonctionnalité : Expressions de filtre stockées pour les tables d'attributs
While previous versions of QGIS allowed you to filter attribute tables using a custom expression, these expressions were lost whenever the attribute table was closed. Now, we\'ve added the ability to store and manage your custom expression filters to the attribute table dialog. You can now build up your own personal collection of useful filters, which will always be available for re-use with a few simple mouse clicks!

![image37](images/entries/d6791d32d649fdc3b2e86aa257a33796391e13e0.webp)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Fonctionnalité : Nouveaux opérateurs pour la Calculatrice Raster
You ask, we listen: `abs` , `min` and `max` are now available in the Raster Calculator user interface!

![image38](images/entries/8a0081e087a6f9ff9180615f34bb56ea6dccc649.webp)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Traitement
### Feature: New algorithm \"Point to layer\"
Cet algorithme crée une nouvelle couche vectorielle qui contient une seule entité avec une géométrie correspondant à un point passé en paramètre. Il peut être utilisé dans les modèles pour convertir une entrée ponctuelle en une couche, qui peut ensuite être utilisée pour d'autres algorithmes qui nécessitent une entrée basée sur une couche.

![image39](images/entries/9f61759f0b8d6a61ea070a5328c4f641c582778e.webp)

Cette fonctionnalité a été développée par Olivier Dalang
### Fonctionnalité : Paramètre de modèle avancé
When creating inputs for a Processing model, you can now mark these input parameters as \"Advanced\" options. (Advanced parameters are hidden by default when users run your model through the Processing toolbox)

![image40](images/entries/d9224e26da62b092d56fd091195942d4142e9bd7.webp)

Cette fonctionnalité a été développée par by Alex Bruy
### Feature: All GDAL based algorithms now support free-form \"additional parameters\"
We added an optional \"Additional command-line parameters\" parameter to all GDAL algorithms , useful for cases when you need to pass a specific command-line argument(s) which is not exposed in the algorithm UI.

![image41](images/entries/18f42d184246ed167be10dee72f5000671d7ac01.webp)

Cette fonctionnalité a été développée par by Alex Bruy
### Fonctionnalité : Metatile pour les tuilages XYZ
Vous pouvez désormais spécifier une taille de métatile personnalisée lors de la génération de tuiles XYZ. Des valeurs plus élevées peuvent accélérer le rendu des tuiles et fournir un meilleur étiquetage (moins d'écarts sans étiquettes) au détriment de l'utilisation de plus de mémoire.

![image42](images/entries/471f15d2616ffc1531c8eef95d4d8ed87d161998.webp)

Cette fonctionnalité a été développée par Martin Dobias
### Fonctionnalité : Nouveau paramètre pour les couleurs
QGIS 3.10 apporte un nouveau type de paramètre à utiliser dans les modèles de traitement et les scripts, qui permet aux utilisateurs de choisir une valeur de couleur. Utile pour tous les modèles et algorithmes qui nécessitent une valeur de couleur en entrée !

![image43](images/entries/87cae0401b93aa308c156a615e63a71e98d25980.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Create style database from project\"
Cet algorithme extrait tous les objets de style (symboles, rampes de couleurs, formats de texte et paramètres d'étiquette) d'un projet QGIS et les stocke dans une nouvelle base de données de style au format XML qui peut ensuite être gérée et importée via la boîte de dialogue Gestionnaire de styles.

![image44](images/entries/8d6075eb1c4fc38b76f9761836048e940be408f8.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Filtre de fichier et valeurs par défaut pour les entrées de fichier et de dossier dans les modèles
For file or folder inputs in Processing models we\'ve added a new file filter setting (with some standard file formats available as an optional preset), and now allow you to set a default value for these inputs.

![image45](images/entries/94fe90f54308a81c5f031066c132e1ad5e8e6ac2.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Combine style databases\"
The new \"Combine style databases\" algorithm combines multiple QGIS style databases into a single output style database. If any symbols exist with duplicate names between the different source databases these will be renamed to have unique names in the output combined database. It\'s designed to give users an easy way to condense multiple separate style databases into a single unified database.

It works brilliantly with results generated by running the \"Create style database from project\" in a batch mode!

![image46](images/entries/479f2a711f8c4b254e72348eda3c79187d4117f2.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Générer des tuiles XYZ en utilisant plusieurs threads
L'algorithme de génération de tuiles XYZ existant a été optimisé et peut désormais générer des tuiles à l'aide de plusieurs threads de traitement.

![image47](images/entries/60aac076d447f244dd232a8e8766a109032a9540.webp)

Cette fonctionnalité a été développée par Isghj5
### Fonctionnalité :  Nouveaux algorithmes pour exporter et importer des signets vers / depuis les couches de carte
To complement the spatial bookmark overhaul in QGIS 3.10, we\'ve added new Processing algorithms which allow you to create a bunch of new bookmarks corresponding to the features from a layer, or to export existing spatial bookmark extents to a new polygon layer.

![image48](images/entries/d0471bc7ea65e476537c8828a7850a64ca9120ef.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Split features by character\"
Ce tout nouvel algorithme découpe les entités en plusieurs entités en sortie, en découpant une valeur de champ à partir d'un caractère spécifié.

Par exemple, si une couche contient des entités avec plusieurs valeurs séparées par des virgules contenues dans un seul champ, cet algorithme peut être utilisé pour répartir ces valeurs entre plusieurs entités en sortie. Les géométries et autres attributs restent inchangés dans la sortie.

De manière facultative, la chaîne de séparation peut être une expression régulière pour plus de flexibilité.

This algorithm was designed for use in models which need to process input files with multiple concatenated values in a single attribute, e.g. geocoding a table with \"address1,address2,address3\" format strings.

![image49](images/entries/a0adf902641c8ace142d9749e632e114262342cd.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Nouvel algorithme "Climb along line"
Previously available as a plugin, the \"Climb Along Line\" algorithm has been added to the out-of-the-box QGIS toolset. This algorithm calculates the accumulated height differences for lines in an input line layer, calculated using the Z values of the line vertices. A copy of the input line layer is returned with additional attributes for accumulated climb and descent, as well as the minimum and maximum Z values for each line.

![image50](images/entries/1b68212fa4a991c79f7d352b5ee3798d0e9a10a3.webp)

This feature was developed by [Håvard Tveite (NMBU) and Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Fonctionnalité : Portage de l'algorithme "Creat grid" de python en C++
Nous avons porté l'algorithme Create Grid de Python vers C ++ afin d'accélérer l'algorithme. L'algorithme fonctionne désormais beaucoup plus rapidement pour vous et est également capable de créer des grilles vectorielles régulières point | ligne | rectangle | losange | hexagone en haute résolution dans des proportions énormes (par exemple, des nations entières) dans un délai raisonnable.

![image51](images/entries/6ef35bc88e69aaf92f5f223249bf792ffd4d28d5.webp)

This feature was funded by [Clemens Raffler](https://twitter.com/root676)

This feature was developed by [Clemens Raffler](https://github.com/root676)
## Explorateur
### Fonctionnalité : Extraire les symboles des projets QGIS depuis l'explorateur
QGIS\' Browser panel just keeps getting more and more powerful! In 3.10, we\'ve added a new option when right-clicking a QGIS project within the browser: \"Extract Symbols\". Selecting this option opens a style manager dialog showing all symbols, color ramps, text formats and label settings from the selected project, allowing you to easily export the browse these symbols.

![image52](images/entries/4c9dd54203cbce44f91e85ed1ff01f1cbb4a40c5.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Général
### Fonctionnalité : Afficher les actualités sur la page d'accueil
Un flux d'actualités QGIS organisé est maintenant affiché sur la page d'accueil. Cela nous donne enfin un canal direct pour diffuser les nouvelles du projet à TOUS nos utilisateurs !
Attendez-vous à voir des nouvelles informations, conseils et événements intéressants sur QGIS !

![image53](images/entries/d3822539302bcd15ae05ef697abafaa1aa5c3ae4.webp)

Cette fonctionnalité a été financée par QGIS.org

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Unités Milliradians (définition SI) et mil (NATO)
QGIS 3.10 vous permet de mesurer des angles dans deux nouvelles unités, les unités milliradians (définition SI) et mil (NATO).

![image54](images/entries/f208b7c32bfe608a448dc2e9359de20e3e4397dd.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Filtrage des dialogues de personnalisation de l'interface
We\'ve added a new \"search\" box to the Interface Customization dialog, which allows you to filter through the widgets and easily find the widget you are trying to customize\...

![image55](images/entries/57f395b303ba963e67242e0f2cfe7104e61f2ad0.webp)

Cette fonctionnalité a été développée par DelazJ
### Fonctionnalité : Amélioration pour la correction des couches non trouvées à l'ouverture d 'un projet
Lorsqu'un chemin de couche est fixé dans un projet, QGIS 3.10 analyse automatiquement tous les autres chemins rompus et essaie de réparer automatiquement tous les autres qui pointaient également vers le même chemin de fichier cassé d'origine. Tout changement qui accélère la réparation des chemins de couches cassés est un changement bienvenu à notre avis !

![image56](images/entries/0119e6f0b3d950d613d224d7bbd53a38575b3579.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Signets spatiaux très nombreux !
We\'ve totally revamped how spatial bookmarks are exposed and managed in QGIS 3.10. Spatial Bookmarks are now shown in the browser panel, and can be regrouped into custom, categorized folders. This offers a much easier way to navigate and manage your bookmarks.

Nous avons également ajouté une toute nouvelle boîte de dialogue d'éditeur de signets, qui comprend un widget qui facilite grandement l'édition des signets.

Les signets peuvent également maintenant être glissés et déposés sur le canevas, permettant aux canevas secondaires de zoomer sur un signet particulier. Cela permet d'utiliser les signets facilement dans les projets multi-canevas, car vous pouvez les déposer sur un canevas spécifique pour zoomer.

![image57](images/entries/8329961bfa04631c5a970888f9a21bad66ddc6fa.webp)

Cette fonctionnalité a été développée par Mathieu Pellerin et Nyall Dawson
### Feature: \"Reselect Features\" action in Edit -\> Select menu
Ever spend 10 minutes painstakingly creating an interactive selection of features, only to accidentally deselect them all through an errant mouse click? If so, this feature is designed just for you! Now, you can restore a layer\'s selection following a selection clear operation via the new \"Reselect Features\" option in the Edit menu.

![image58](images/entries/e1234a3ca30866b91f64f97b83fdf0fb90838cb6.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Paralléliser la génération d'index d'accrochage
L'idée était de paralléliser pour chaque couche le snap cache computing (séquentiel pour le moment) et de le rendre non bloquant. Par conséquent, il est toujours possible d'utiliser QGIS même si le cache de capture est en cours de création. L'utilisateur peut par exemple commencer à éditer le nœud pendant que la construction du cache d'accrochage est en cours.

Cette fonctionnalité a été développée par Oslandia
### Fonctionnalité : Modèles pour les projets QGIS
QGIS 3.10 inclut la possibilité d'utiliser directement les modèles de projet à partir de la page d'accueil. De plus, vous pouvez désormais envoyer des modèles de projet à l'ensemble de votre organisation en les plaçant dans un dossier système, à côté de la possibilité déjà existante de le placer dans un dossier de profil utilisateur.

![image59](images/entries/5adaa5a973e0b232bae3a8dbab8739c8887ac70e.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Fournisseurs de données
### Fonctionnalité : Prise en charge en lecture-écriture de .shz et .shp.zip
For QGIS builds based on GDAL 3.1, you can now open and edit single-layer ZIP compressed shapefiles (.shz), or multi-layer ones (.shp.zip). Regardless of where you sit on the Shapefile vs Geopackage battle, you\'ll welcome this ability to de-clutter your folders and store shapefiles as a single file!

Cette fonctionnalité a été développée par Even Rouault
### Fonctionnalité : Authentification du fournisseur Oracle
We\'ve updated the Oracle database provider to add full support for QGIS built-in authentication system.

Cette fonctionnalité a été développée par Jürgen Fischer
### Fonctionnalité : Prise en charge améliorée des rasters PostGIS
Les couches raster PostGIS sont désormais affichées dans le panneau Explorateur et dans la boîte de dialogue Gestionnaire de sources de données, vous permettant de gérer et d'ajouter facilement ces couches à vos projets. Actuellement, seule la prise en charge de la lecture à partir de l'explorateur est prise en charge - vous ne pouvez pas faire glisser des rasters dans une base de données PostGIS à l'aide de l'explorateur.

Cette fonctionnalité a été développée par Alessandro Pasotti
### Fonctionnalité : Oracle - Prise en charge des transactions
For version 3.10, we\'ve enhanced the Oracle database provider and added support for editing layers via transactions.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : dimensions Z / M dans les couches de texte délimités
We\'ve added optional support for Z and M fields to QGIS\' delimited text provider, allowing you to create Z or M enabled layers directly from CSV files.

![image60](images/entries/bfaa5fc4c03d27e5345475172f5e7bdb20a4f6ff.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Fonctionnalité : Fournisseurs de données statiques
Un énorme travail en arrière plan que nous avons terminé pour QGIS 3.10 est une refactorisation de l'infrastructure du fournisseur. Désormais, les fournisseurs autorisent les liaisons dynamiques et statiques. C'était une condition préalable pour pouvoir créer des bibliothèques QGIS sur des plateformes qui ne prennent pas en charge la liaison dynamique (iOS), et permet aux outils basés sur QGIS comme l'application de collecte de données d'être distribuées pour les appareils iOS!

This feature was funded by [Lutra Consulting Ltd.](http://www.lutraconsulting.co.uk)

This feature was developed by [Peter Petrik, Martin Dobias](http://www.lutraconsulting.co.uk/about)
## QGIS Server
### Fonctionnalité : utilisation des SVG dans QGIS Server
Earlier QGIS server versions had rendering issues when remote SVG files were used in a project (e.g. those hosted via external http servers). We\'ve improved how QGIS Server fetches these resources, and it\'s now possible to use remote SVG paths in your layers and publish them as WMS without rendering issues in QGIS Server.

![image61](images/entries/71d731c71f864fcb542f2f7ec52c68e4c03068d3.webp)

This feature was funded by [Ifremer](https://sextant.ifremer.fr/)

This feature was developed by [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Fonctionnalité : Dimension WMS
Dans QGIS 3.10, un serveur WMS peut prendre en charge plusieurs types de dimensions telles que le temps, l'altitude ou d'autres types de dimensions. La dimension doit être définie comme le niveau de la couche et peut être utilisée par le client WMS pour filtrer les informations demandées. Le temps WMS est une élément de la dimension WMS.

![image62](images/entries/45744c5a4a4c94e1c71a91bcfa7b672333002e75.webp)

This feature was funded by [Ifremer](https://sextant.ifremer.fr/)

This feature was developed by [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Fonctionnalité : Prise en charge du serveur OAPIF (alias WFS3)
QGIS 3.10 Server is one of the very first geospatial servers which supports the new [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) standard (also known as WFS3)!

Il s'agit d'une implémentation complètement nouvelle qui fournit un service basé sur HTML et JSON pour vos développements de cartographie Web, y compris une interface WebGIS simple qui est disponible immédiatement et facilement personnalisable via un système de modèles HTML.

More information is available in the [documentation](https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/services.html#wfs3-ogc-api-features)

![image63](images/entries/81af9beefcd8522ecc0f953b2a6b9b4895e35675.webp)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Programmation
### Fonctionnalité : Nouvelle classe QgsBookmarkManager
Attachée à QgsProject et QgsApplication, cette nouvelle classe fournit une méthode stable et supportée de gestion des projets et des signets globaux (par opposition à l'ancienne approche non documentée et non stable de manipulation directe des clés de projet ou d'une base de données sqlite). Maintenant, vos plugins et scripts sont capables de lire, modifier et gérer les signets spatiaux !

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Fonctionnalité : Nouvelle API pour les fournisseurs de connexions aux bases de données
Thanks to funding from the QGIS grant program, you can now use a [new API](https://github.com/qgis/QGIS/pull/31190) aimed to manage DB connections in a unified way. The new connection API also provides a set of useful methods that can be used by plugin authors to access information about tables, schemas etc. and to run SQL arbitrary queries and get the results back into a handy Python array.

Cette fonctionnalité a été financée par QGIS

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Correctifs notables
### Fonctionnalité : Corrections de bug par Alessandro Pasotti
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Crash lors de la suppression d'éléments de mise en page. | [#31549](https://github.com/qgis/QGIS/issues/31549) |  |  |
| Erreur python avec DB manager | [#31457](https://github.com/qgis/QGIS/issues/31457) |  |  |
| QGIS 3.4.11: Cliquer sur une URL PDF dans la réponse GetFeatureInfo génère une erreur. | [#31542](https://github.com/qgis/QGIS/issues/31542) | Déjà corrigé (par moi) sur 3.8 et Master |  |
| Watch file not adding new columns | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| Perte de l'arrière-plan des étiquettes depuis un projet ou d'un style plus ancien | [#31427](https://github.com/qgis/QGIS/issues/31427) | [PR #3164](https://github.com/qgis/QGIS/pull/31647) |  |
| \"Text formats\" dialog shows modifiable buffer properties while the \"draw text buffer\" is unchecked | [#31428](https://github.com/qgis/QGIS/issues/31428) | [PR #3173](https://github.com/qgis/QGIS/pull/31734) |  |
| Symbology tab widget does not horizontally expand in the layer properties dialog extent | [#31449](https://github.com/qgis/QGIS/issues/31449) | [PR #3166](https://github.com/qgis/QGIS/pull/31665) |  |
| Watch file not adding new columns | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| Non reporté mais lié à #31452 | [PR #3168](https://github.com/qgis/QGIS/pull/31688) |  |  |
| Impossible d'ajouter un service WMS dans QGIS, la même URL fonctionne avec d'autres clients | [#31661](https://github.com/qgis/QGIS/issues/31661) |  |  |
| QGIS Serveur - Echec du téléchargement du fichier Capabilities : SSL handshake failed | [#31675](https://github.com/qgis/QGIS/issues/31675) |  |  |
| régression apparente dans la calculatrice de raster à la multiplication de valeurs conditionnelles | [#31193](https://github.com/qgis/QGIS/issues/31193) | [PR #3169](https://github.com/qgis/QGIS/pull/31690) |  |
| Actions d'exploration des GPKG cassées | [#31730](https://github.com/qgis/QGIS/issues/31730) | [PR #3173](https://github.com/qgis/QGIS/pull/31731) |  |
| Echec au redimensionnement de la fenêtre du gestionnaire de sources de données des panneaux inactifs | [#31732](https://github.com/qgis/QGIS/issues/31732) | [PR #3174](https://github.com/qgis/QGIS/pull/31741) |  |
| In place processing multipart to singleparts does not handle unique constraints | [#31634](https://github.com/qgis/QGIS/issues/31634) | [PR #3175](https://github.com/qgis/QGIS/pull/31750) | [PR #3181](https://github.com/qgis/QGIS/pull/31810) |
| Plantage à l'ajout d'une légende via python | [#31713](https://github.com/qgis/QGIS/issues/31713) |  |  |
| UI: Legend does not refresh after classifincation bounds updated | [#31643](https://github.com/qgis/QGIS/issues/31643) | Non affecté | [PR #3183](https://github.com/qgis/QGIS/pull/31834) |
| UI: PostGIS layer error message not helpful, disappears and shouldn\'t happen | [#31799](https://github.com/qgis/QGIS/issues/31799) | [PR #3184](https://github.com/qgis/QGIS/pull/31841) |  |
| Server GetLegendGraphics contextual (BBOX) fails if no WIDTH and HEIGHT are supplied | [#31846](https://github.com/qgis/QGIS/issues/31846) | [PR #3186](https://github.com/qgis/QGIS/pull/31865) | [PR #3188](https://github.com/qgis/QGIS/pull/31882) |
| extend/trim crash | [#31864](https://github.com/qgis/QGIS/issues/31864) |  |  |
| UI: any click on number of classes updown triggers twice | [#31635](https://github.com/qgis/QGIS/issues/31635) | [PR #3187](https://github.com/qgis/QGIS/pull/31871) |  |
| GPKG project is not marked dirty after it is deleted from the storage | [#30550](https://github.com/qgis/QGIS/issues/30550) | [PR #3187](https://github.com/qgis/QGIS/pull/31876) |  |
| Fix unreported issue with QVariantList to JSON conversion in QgsJsonUtils | non signalé | [PR #3192](https://github.com/qgis/QGIS/pull/31920) |  |
| Plantage lors de l'ajout d'un WMS | [#31927](https://github.com/qgis/QGIS/issues/31927) | [#31927](https://github.com/qgis/QGIS/issues/31927) | [PR #3197](https://github.com/qgis/QGIS/pull/31979) |
| Raster calculator change sign does not work when OpenCL is on | [#32023](https://github.com/qgis/QGIS/issues/32023) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Snapping map units always show \"meters even when the project is in different units | [#31961](https://github.com/qgis/QGIS/issues/31961) | [PR #3201](https://github.com/qgis/QGIS/pull/32018) |  |
| QGIS Raster Calculator outputs nodata only rasters | [#32025](https://github.com/qgis/QGIS/issues/32025) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Opening projects from PostgreSQL issue | [#32050](https://github.com/qgis/QGIS/issues/32050) | [PR #3206](https://github.com/qgis/QGIS/pull/32062) |  |
| GetLegendGraphic shows all identical symbols for content based legend | [#32020](https://github.com/qgis/QGIS/issues/32020) |  |  |
| WFS doesn\'t recognize advertised GeoJSON outputFormat string | [#32065](https://github.com/qgis/QGIS/issues/32065) | [PR #3210](https://github.com/qgis/QGIS/pull/32106) |  |
| la création d'index sur des GeoPackages échoue (QGIS 3.8.3) | [#32094](https://github.com/qgis/QGIS/issues/32094) |  |  |
| DB manager import option \"Create single-part geometries instead of multi-part\" is broken | [#32089](https://github.com/qgis/QGIS/issues/32089) | [PR #3210](https://github.com/qgis/QGIS/pull/32108) |  |
| GetLegendGraphic shows all identical symbols for content based legend | [#32020](https://github.com/qgis/QGIS/issues/32020) | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| WFS contextual legend issue when canvas CRS is different than layer\'s CRS | non signalé | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| PostGIS/geojson: Impossible de saisir des nombres négatifs dans les champs int | [#32149](https://github.com/qgis/QGIS/issues/32149) | [PR #3216](https://github.com/qgis/QGIS/pull/32161) |  |
| L'onglet Informations dans les propriétés de la couche WMS ne répond pas si un service WMS contient plusieurs couches | [#32213](https://github.com/qgis/QGIS/issues/32213) | [PR #3226](https://github.com/qgis/QGIS/pull/32269) |  |
| Data Source UI - PostgreSQL table multi-line comments make the grid table hard to read | [#32257](https://github.com/qgis/QGIS/issues/32257) | [PR #3233](https://github.com/qgis/QGIS/pull/32336) |  |
| More null pointer dereferences when plugins are off | [#32347](https://github.com/qgis/QGIS/issues/32347) | [PR #3235](https://github.com/qgis/QGIS/pull/32351) |  |
| null pointer dereferences when plugins are off | [#32338](https://github.com/qgis/QGIS/issues/32338) | [PR #3234](https://github.com/qgis/QGIS/pull/32345) |  |
| \"Merge features\" and \"merge feature attributes\" have broken numerical functions | [PR #3236](https://github.com/qgis/QGIS/pull/32360) | [PR #3236](https://github.com/qgis/QGIS/pull/32360) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Fonctionnalité : Correction de bugs par Alexander Bruy
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| GDAL scripts in Processing need quoting on attribute names | [#30878](https://github.com/qgis/QGIS/issues/30878) | [PR #3171](https://github.com/qgis/QGIS/pull/31712) | [PR #3171](https://github.com/qgis/QGIS/pull/31717) |
| Processing GDAL algorithms does not handle correctly WFS input layers | [#29663](https://github.com/qgis/QGIS/issues/29663) | [PR #3173](https://github.com/qgis/QGIS/pull/31735) |  |
| shp files in zip files files cannot be used in Processing with 3rd party providers (SAGA, GRASS\...) | [#29001](https://github.com/qgis/QGIS/issues/29001) | [PR #3174](https://github.com/qgis/QGIS/pull/31744) | [PR #3178](https://github.com/qgis/QGIS/pull/31787) |
| Not possible to toggle use selected features in the Processing layer combobox | [#30636](https://github.com/qgis/QGIS/issues/30636) | [PR #3173](https://github.com/qgis/QGIS/pull/31739) |  |
| Connect to postgis database fails in \"Layer - Add Postgis layer\" on databases with weird table names | [#27040](https://github.com/qgis/QGIS/issues/27040) | [PR #3176](https://github.com/qgis/QGIS/pull/31763) |  |
| GRASS v.build.polylines dosn\'t work in Qgis 3.4.10 | [#31037](https://github.com/qgis/QGIS/issues/31037) |  |  |
| Processing Algorithms written with the \@alg decorator don\'t get the gear icon | [#31252](https://github.com/qgis/QGIS/issues/31252) | [PR #3188](https://github.com/qgis/QGIS/pull/31887) |  |
| v.drape - no 25D export with SpatiaLite format | [#30066](https://github.com/qgis/QGIS/issues/30066) |  |  |
| Service url cannot include custom query parameters | [#26761](https://github.com/qgis/QGIS/issues/26761) |  |  |
| Processing: python error on startup | [#29535](https://github.com/qgis/QGIS/issues/29535) |  |  |
| Saving Processing\'s Package Layers algorithm\'s output to default temporary output leaves no result | [#30535](https://github.com/qgis/QGIS/issues/30535) |  |  |
| \[Georeferencer\] GDAL script does not set target SR | [#31353](https://github.com/qgis/QGIS/issues/31353) | [PR #3189](https://github.com/qgis/QGIS/pull/31898) |  |
| Processing \"Build virtual vector\" now fails in certain cases | [#29336](https://github.com/qgis/QGIS/issues/29336) | [PR #3190](https://github.com/qgis/QGIS/pull/31901) |  |
| Unreported issue with missed import in the Processing algorithms dialog | non signalé | [PR #3190](https://github.com/qgis/QGIS/pull/31902) |  |
| db manager: python error when clicking \"edit table\" if the table is a postgis raster | [#30214](https://github.com/qgis/QGIS/issues/30214) | [PR #3190](https://github.com/qgis/QGIS/pull/31904) |  |
| DB Manager: Renaming a PostGIS geometry column causes it to lose its geometry type and SRS | [#27613](https://github.com/qgis/QGIS/issues/27613) | [PR #3192](https://github.com/qgis/QGIS/pull/31929) |  |
| Georeferencer incorrectly shows last image when reopened | [#26700](https://github.com/qgis/QGIS/issues/26700) | [PR #3193](https://github.com/qgis/QGIS/pull/31932) |  |
| DB Manager: Create Layer dialog should be closed or cleared once the new layer is generated | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #3195](https://github.com/qgis/QGIS/pull/31956) |  |
| \[Vector Save As\...\] Extension is not replaced in filename when switching format | [#26054](https://github.com/qgis/QGIS/issues/26054) | [PR #3196](https://github.com/qgis/QGIS/pull/31960) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Cette fonctionnalité a été développée par Alexander Bruy
### Fonctionnalité : Correction de bugs par Peter Petrik
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Reproducible Crash: retrieving QgsHighlight instance stored as a widget property | [#30766](https://github.com/qgis/QGIS/issues/30766) | [PR #3173](https://github.com/qgis/QGIS/pull/31733) | [PR #3197](https://github.com/qgis/QGIS/pull/31977) |
| Layer styling Mesh layer does not respond to change of Color ramp (first time) | [#29188](https://github.com/qgis/QGIS/issues/29188) | [PR #3198](https://github.com/qgis/QGIS/pull/31981) |  |
| qgis crashed on close in QSortFilterProxyModel | [#31721](https://github.com/qgis/QGIS/issues/31721) |  |  |
| QGIS se fige | [#29742](https://github.com/qgis/QGIS/issues/29742) |  |  |
| Plante lorsque l'on essaie de sauvegarder un projet | [#29896](https://github.com/qgis/QGIS/issues/29896) |  |  |
| Crash on exit with advanced digitizing active | [#29143](https://github.com/qgis/QGIS/issues/29143) |  |  |
| Renaming macOS app causes authentication error | [#32163](https://github.com/qgis/QGIS/issues/32163) |  |  |
| QGIS ne s'ouvre pas après avoir fait la mise à jour vers Mac OS Catalina | [#32167](https://github.com/qgis/QGIS/issues/32167) |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Fonctionnalité : Correction de bugs par Even Rouault
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3176](https://github.com/qgis/QGIS/pull/31764) | [Commit 08bb3fe](https://github.com/qgis/QGIS/commit/08bb3fea3fc3f574755ecc0a7dc8381a9822e4cd) |
| QGIS master crash upon exit @ QgsCoordinateTransformPrivate::freeProj on Windows platform | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3184](https://github.com/qgis/QGIS/pull/31848) | [PR #3185](https://github.com/qgis/QGIS/pull/31850) |
| QGIS WFS stripping of viewparam KVP from WFS Feature Requests | [#31026](https://github.com/qgis/QGIS/issues/31026) | [PR #3176](https://github.com/qgis/QGIS/pull/31765) | [PR #3188](https://github.com/qgis/QGIS/pull/31883) |
| Crash: right click on image -\>export -\>save as-\>\"save raster layer as\" | [#30937](https://github.com/qgis/QGIS/issues/30937) | [PR #3176](https://github.com/qgis/QGIS/pull/31766) | [PR #3178](https://github.com/qgis/QGIS/pull/31780) |
| crash in discover relations for postgresql layers | [#31213](https://github.com/qgis/QGIS/issues/31213) | [PR #3176](https://github.com/qgis/QGIS/pull/31768) | [PR #3177](https://github.com/qgis/QGIS/pull/31779) |
| Exporting raster as raw data to GeoPackage fails silently | [#30644](https://github.com/qgis/QGIS/issues/30644) | [PR #3177](https://github.com/qgis/QGIS/pull/31771) | [PR #3178](https://github.com/qgis/QGIS/pull/31781) |
| QGIS crashes after deactivating a GDAL driver in use in the project | [#29212](https://github.com/qgis/QGIS/issues/29212) | [PR #3177](https://github.com/qgis/QGIS/pull/31772) | [PR #3180](https://github.com/qgis/QGIS/pull/31802) |
| Crash exporting to GS7BG format | [#31775](https://github.com/qgis/QGIS/issues/31775) | [PR #3178](https://github.com/qgis/QGIS/pull/31785) | [PR #3183](https://github.com/qgis/QGIS/pull/31836) |
| pgdump is no longer a recognized format for the GDAL/OGR convert format algorithm | [#31421](https://github.com/qgis/QGIS/issues/31421) | [PR #3181](https://github.com/qgis/QGIS/pull/31811) | not worth |
| PBF files not loading correctly | [#31062](https://github.com/qgis/QGIS/issues/31062) | [PR #3181](https://github.com/qgis/QGIS/pull/31812) | [PR #31835](https://github.com/qgis/QGIS/pull/31835) |
| Error importing cover from Geoserver WFS service | [#29844](https://github.com/qgis/QGIS/issues/29844) | [PR #31813](https://github.com/qgis/QGIS/pull/31813) | [PR #31867](https://github.com/qgis/QGIS/pull/31867) |
| Feature count from online Geojson not updated upon refresh | [#30518](https://github.com/qgis/QGIS/issues/30518) | [PR #31860](https://github.com/qgis/QGIS/pull/31860) | not worth |
| Edits in GeoJson datasources are not saved anymore | [#28580](https://github.com/qgis/QGIS/issues/28580) | GDAL <https://github.com/OSGeo/gdal/pull/1846> | Backported to GDAL 3.0 and 2.4 maintenance branches |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Fonctionnalité : Correction de bugs par Sandro Santilli
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Adding Postgis rasters from DB Manager ask for password for each add | [#31162](https://github.com/qgis/QGIS/issues/31162) |  |  |
| \[processing\] segmentizebymaxdistance puts qgis in endless CPU loop | [#31832](https://github.com/qgis/QGIS/issues/31832) | [Commit 6942b4b9](https://github.com/qgis/QGIS/commit/6942b4b93d252bc3a031db08a34f378d8d3c726d) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) |
| file INSTALL cannot find doc/api/html | [#31842](https://github.com/qgis/QGIS/issues/31842) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) | n/a |
| QGIS died on signal 11 \# at start up | [#31350](https://github.com/qgis/QGIS/issues/31350) |  |  |
| repository files modified by `make check` | [#25830](https://github.com/qgis/QGIS/issues/25830) | [PR #31980](https://github.com/qgis/QGIS/pull/31980) |  |
| CMake Error at cmake/FindGEOS.cmake:162 | [#32170](https://github.com/qgis/QGIS/issues/32170) | [Commit bc9bb888](https://github.com/qgis/QGIS/commit/bc9bb8880a3db5a05c697f5d56708757a2ce999d) | [Commit 27f13936](https://github.com/qgis/QGIS/commit/27f13936afd970d766f398584a1ea509dc15b907) |
| False success from ogr provider\'s committChanges | [#32144](https://github.com/qgis/QGIS/issues/32144) | [Commit f421dc4f](https://github.com/qgis/QGIS/commit/f421dc4f92cfc019eec9823556d3c8f3e9589d95) | [Commit 136cec24](https://github.com/qgis/QGIS/commit/136cec244111748627c59db151002fddfc5f1708) |
| TestSagaAlgorithms: line 139, in check_algorithm: \'NoneType\' object has no attribute \'checkParameterValues\' | [#32143](https://github.com/qgis/QGIS/issues/32143) | [Commit 76b39de1](https://github.com/qgis/QGIS/commit/76b39de1b85375f48d7a5d35ebe39a52224d1809) | n/a |
| PostGIS Data Loads Extemely Slow | [#26186](https://github.com/qgis/QGIS/issues/26186) | [PR #31858](https://github.com/qgis/QGIS/pull/31858) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sandro Santilli](http://strk.kbt.io/)
### Feature: Bug fixes by Matthias Kuhn
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Crash when opening symbology tab of invalid layer | [#32041](https://github.com/qgis/QGIS/issues/32041) | [#32041](https://github.com/qgis/QGIS/issues/32041) | n/a |
| PR reviews | Many :D |  |  |
| qgz are marked as temporary on windows | [#32118](https://github.com/qgis/QGIS/issues/32118) |  |  |
| Allow selecting geometry type in context | [#32121](https://github.com/qgis/QGIS/issues/32121) | [PR #32125](https://github.com/qgis/QGIS/pull/32125) | n/a |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Matthias Kuhn](https://www.opengis.ch/)
### Fonctionnalité : Correction de bugs par Paul Blottiere
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Fixes invalid schemaLocation in GetCapabilities doc | [#32085](https://github.com/qgis/QGIS/issues/32085) | [PR #32352](https://github.com/qgis/QGIS/pull/32352) |  |
| Invalid WMS GetFeatureInfo response with json info_format | [#32326](https://github.com/qgis/QGIS/issues/32326) | [PR #32386](https://github.com/qgis/QGIS/pull/32386)/files |  |
| QGIS Server SELECTION doesn\'t work with Postgres ids of type bigint or text | [#29779](https://github.com/qgis/QGIS/issues/29779) |  |  |
| Regression with opacities for the WMS GetPrint request | [#29317](https://github.com/qgis/QGIS/issues/29317) |  |  |
| Unreported regression: Invalid renderer type after loading a QML style file | unreported regression | [PR #32388](https://github.com/qgis/QGIS/pull/32388) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Cette fonctionnalité a été développée par Paul Blottiere
### Fonctionnalité: correction de bugs par Nyall Dawson
| Intitulé du bug | URL du ticket (le cas échéant) | URL PR ou commit | 3.4 backport PR ou commit |
| --- | --- | --- | --- |
| Fix crash when deleting layouts from designer window | [#32465](https://github.com/qgis/QGIS/issues/32465) | [Commit e643e7f6](https://github.com/qgis/QGIS/commit/e643e7f6abe63aff123e07a0137afdda3987d4e6) | n/a |
| Fix model to python when model has no input parameters | [Commit 6f1c42e7](https://github.com/qgis/QGIS/commit/6f1c42e7bc9fa6ddfae3bbc1304ebeb53fe6a014) | n/a |  |
| Fix string escaping when converting models to python code | [#32451](https://github.com/qgis/QGIS/issues/32451) | [Commit e3eb4f54](https://github.com/qgis/QGIS/commit/e3eb4f54abdd8c6d4f4de443e3517775e9e565e1) | n/a |
| Fix memory leak | [Commit 5be31915](https://github.com/qgis/QGIS/commit/5be319157f112a2fdbab7f03d0010d69f1e79157) | n/a |  |
| Fix potential overflow in raster renderer | [Commit 1ba8db41](https://github.com/qgis/QGIS/commit/1ba8db41b67c7c481affd5271864cc2318ce06e4) | n/a |  |
| Restore project variables early in the project read cycle | [#32382](https://github.com/qgis/QGIS/issues/32382) | [Commit d76835fe](https://github.com/qgis/QGIS/commit/d76835fec5a9217a5ea1996374d142f7319f8d08) | n/a |
| Improve docs for Join by Nearest, raise warning in log | [#32317](https://github.com/qgis/QGIS/issues/32317) | [Commit 670c81f9](https://github.com/qgis/QGIS/commit/670c81f9212ada60f56c1c70ee9d37280052622c) | n/a |
| Catch some reprojection exceptions during raster rendering | [#32301](https://github.com/qgis/QGIS/issues/32301) | [Commit 1dfc0c1e](https://github.com/qgis/QGIS/commit/1dfc0c1e4eb8be26bb7214e3978aa6d80974c221) | n/a |
| \[labeling\] Fix broken numeric formatting settings, add tests | [#32393](https://github.com/qgis/QGIS/issues/32393) | [Commit b58dd674](https://github.com/qgis/QGIS/commit/b58dd6745fabf8bccd6dbeb684b37393d5953cb7) | n/a |
| Fix uncaught transform exception when determining AFS layer bounds | non signalé | [Commit 857697dd](https://github.com/qgis/QGIS/commit/857697dd9919e80fc03e0c2059e56ce7311e9b49) | n/a |
| Fix qt warning thrown when converting a 2.18 project | non signalé | [Commit 12ad9fca](https://github.com/qgis/QGIS/commit/12ad9fca1ed5027129161ee5b5c764b8374d0b51) | n/a |
| Add option to take no action (\"Leave as an unknown CRS\") when a layer is loaded which has no CRS | #19762, #27634, #24815 (et probablement d'autres) | [Commit ffe66bff](https://github.com/qgis/QGIS/commit/ffe66bff82be16dd90cd95f13331e5be7ca2c628) | n/a |
| Don\'t force fallback to WGS84 for unknown layer CRSes | non signalé | [Commit 93741566](https://github.com/qgis/QGIS/commit/937415663f609fa7e41056aeb1176a0a145accc1) | n/a |
| Fix memory layers cannot use non-EPSG CRS codes | unreported, but likely a cause of many bugs | [Commit 2dad68f7](https://github.com/qgis/QGIS/commit/2dad68f76396a419b25fa8dad2b7b16552086740) | n/a |
| Fix crash after deleting report sections | [#31302](https://github.com/qgis/QGIS/issues/31302) | [Commit 3356460c](https://github.com/qgis/QGIS/commit/3356460ce70af15105880d135271595dccfc397c) | [Commit d3230ac0](https://github.com/qgis/QGIS/commit/d3230ac0c545604a97fa3028ca3e846bff65004c) |
| Ensure polygon rings generated for rendering are always closed | non signalé | [Commit a69e38d9](https://github.com/qgis/QGIS/commit/a69e38d9c358faea5ae4a8628add1e6721cc23e8) | n/a |
| Don\'t crash QgsTessellator when an empty polygon is added | non signalé | [Commit 761b2e77](https://github.com/qgis/QGIS/commit/761b2e778594f4051a72d02b898354f501e336fe) | n/a |
| Fix crash in topology checker plugin after a check is canceled | non signalé | [Commit 606bcd35](https://github.com/qgis/QGIS/commit/606bcd35143d09cca5b1ec45bdb5b13236e4376b) | n/a |
| Fix topology checker multipart check | [#28361](https://github.com/qgis/QGIS/issues/28361) | [Commit 5101386b](https://github.com/qgis/QGIS/commit/5101386b37fb4d180d32d31663404e3bcc647cec) | n/a |
| Fix crash on exit when topology checker dock is open with visible results | non signalé | [Commit 64375ad4](https://github.com/qgis/QGIS/commit/64375ad4d28597eb97808f64e1481915df7a676c) | n/a |
| Don\'t load print layouts when opening project browser items | via email | [Commit 9f1ce084](https://github.com/qgis/QGIS/commit/9f1ce08418db9545ed18d6711c472833f9889e1d) | n/a |
| Add QgsProject flag to avoid loading print layouts when reading a project file, avoids crashes when project is loaded in background thread | via email | [Commit d0ed3746](https://github.com/qgis/QGIS/commit/d0ed3746629ae9c9349fe2e9c75550679120026d) | n/a |
| Don\'t try to load HTML content when a layout is created in a background thread | via email | [Commit 53252496](https://github.com/qgis/QGIS/commit/532524961c0880b33e1d7ed4a3ce0805d7f0bc71) | [Commit 5fcab0e7](https://github.com/qgis/QGIS/commit/5fcab0e713a1e9ffde8b049f620d4a5cd6a81ff3) |
| Huge speed up to QgsTessellator | [Commit 577e1e96](https://github.com/qgis/QGIS/commit/577e1e962d4004f9cd11a169860e0b099216c963) | n/a |  |
| \[processing\] Ensure all objects used by the model are correctly imported | [#32004](https://github.com/qgis/QGIS/issues/32004) | [Commit e5e3fe47](https://github.com/qgis/QGIS/commit/e5e3fe473e8e6764f528b4a40095a7a047e9c357) | n/a |
| \[processing\] Avoid confusing use of expression parameter type in Random Points in Polygon algorithm | [#27640](https://github.com/qgis/QGIS/issues/27640) | [Commit 196e15a0](https://github.com/qgis/QGIS/commit/196e15a0ff974622bfa1e7dfdeb9fe8567a7f3b7) | n/a |
| \[layouts\] Update map settings variables in UI when map extent/rotation changes | [#24136](https://github.com/qgis/QGIS/issues/24136) | [Commit 86c83537](https://github.com/qgis/QGIS/commit/86c83537f9b03816ba5b8f90c8cf8a2820077441) | n/a |
| \[layouts\] Fix layout variables set programmatically do not show in GUI | [#28837](https://github.com/qgis/QGIS/issues/28837) | [Commit 1afdd935](https://github.com/qgis/QGIS/commit/1afdd935cf84cbd702093935a676672d1e349da1) | n/a |
| \[layouts\] Ensure variable panels are updated when layout or atlas properties change | [#26402](https://github.com/qgis/QGIS/issues/26402) | [Commit 2b31e03a](https://github.com/qgis/QGIS/commit/2b31e03ad0659500a733d71c10c54e17e6817c10) | n/a |
| \[layouts\] Move page background setting to a per-page option | [#25695](https://github.com/qgis/QGIS/issues/25695) | [Commit 45e847ef](https://github.com/qgis/QGIS/commit/45e847ef69b56b4c12774363e20a7a05f49e8618) | n/a |
| Optimize QgsContrastEnhancementFunction | [Commit f5c21a0f](https://github.com/qgis/QGIS/commit/f5c21a0fbd72fe840900e0ad35c4af285fbd8a79) | n/a |  |
| \[layouts\] Prevent removal of the last remaining page in a layout | via email | [Commit e6ecfdd3](https://github.com/qgis/QGIS/commit/e6ecfdd39bc2ae842c437700508899a9e1aa9dcd) | [Commit b65f23f8](https://github.com/qgis/QGIS/commit/b65f23f86b4630b4b5157400a713c36081bd56b9) |
| \[layouts\] Fix crash when exporting layout with no pages | via email | [Commit b784d698](https://github.com/qgis/QGIS/commit/b784d6982826039bd9fa35b7ecd1a362e29c0b04) | [Commit f8355cbb](https://github.com/qgis/QGIS/commit/f8355cbbbe4bdbbae9c3f1b135ed59bbc51226a2) |
| Fix conditional formatting panel high dpi issues | [Commit 1f033fe8](https://github.com/qgis/QGIS/commit/1f033fe83d63a2edb6ddc2b6d90169e3b814764e) | n/a |  |
| Fix loss of font setting when editing conditional format | [Commit 72efc1ed](https://github.com/qgis/QGIS/commit/72efc1edde693800b6604e8ec3afcc892ea5239e) | n/a |  |
| Avoid overflow in QgsImageOperation | [Commit aefbf662](https://github.com/qgis/QGIS/commit/aefbf6627256637cf455b2df409b3a4bf8171b33) | [Commit 9f4d3a87](https://github.com/qgis/QGIS/commit/9f4d3a8745b2d89faeb6a9272369eaa772e3638c) |  |
| \[processing\] Extend api for retrieving a layer in a compatible format | via 3rd party plugin bug tracker | [Commit 651c5071](https://github.com/qgis/QGIS/commit/651c5071806d6f4f4dafc800e6b0d67f043a9ef0) | n/a |
| Fix conditional styles in feature list view do not update when the layer\'s conditional styles are changed | [Commit bccd5a46](https://github.com/qgis/QGIS/commit/bccd5a46106d7c5a63b3bd8c64ad1491a60205af) | n/a |  |
| Fix broken display of conditional styles in feature list view | [Commit 5f7264d4](https://github.com/qgis/QGIS/commit/5f7264d4d18d6894c4d33017439dc517a932fd75) | n/a |  |
| Fix incorrect conditional styling applied to rows in some cases | [Commit c15c7271](https://github.com/qgis/QGIS/commit/c15c72718909f4bce2d172b819c74ec7d8d4d9b3) | n/a |  |
| Use invalid colors, not transparent colors, to indict not set colors in conditional formats, fixes incorrect colors used for conditionally styled rows | [Commit bc82cffd](https://github.com/qgis/QGIS/commit/bc82cffd85342d92435600547c220eb1eaf90257) | n/a |  |
| \"\[labeling\] When an extreme number of features are being labeled from a single layer, place additional limits on the maximum number of |  |  |  |
| labeling candidates to generate for features in this layer\" | [Commit 61bfced6](https://github.com/qgis/QGIS/commit/61bfced6a7ae109bc97a0924eae108c0e51916d5) | n/a |  |
| \[layouts\] Fix incorrect alignment of items when the align or distribute tools are used with items with a non-top-left reference point | [#31900](https://github.com/qgis/QGIS/issues/31900) | [Commit b4550dc4](https://github.com/qgis/QGIS/commit/b4550dc4c06eec23ace4cbc5c6f1f8b23c8ee14f) | n/a |
| \[processing\] Respect user set default vector output format in vector split algorithm | [Commit 90bac82f](https://github.com/qgis/QGIS/commit/90bac82f124ccb53e43bb99f5d483105bea1c967) | n/a |  |
| Fix GUI is not updated when layout atlas is set to use the default filename expression | [#20786](https://github.com/qgis/QGIS/issues/20786) | [Commit a4da849e](https://github.com/qgis/QGIS/commit/a4da849e9d190ece1b748303cc8f68333f1e0e78) | n/a |
| \[reports\] Remove useless extra set of export actions | [#26384](https://github.com/qgis/QGIS/issues/26384) | [Commit d6b41813](https://github.com/qgis/QGIS/commit/d6b4181349a274e8d34196a340f4b806403af06b) | n/a |
| \[reports\] Fix crash when print button clicked before a report section is opened | non signalé | [Commit c93fd0a4](https://github.com/qgis/QGIS/commit/c93fd0a4350ea14db9728ad17ada06e70eb9ffd6) | n/a |
| \[reports\] Reduce minimum width of report organiser dock | [#25916](https://github.com/qgis/QGIS/issues/25916) | [Commit 7c490848](https://github.com/qgis/QGIS/commit/7c4908481269f38e1b96c730542d5299903963fb) | n/a |
| \[layouts\] Add a page number selection combo box at the top of the guide manager dock | [#25700](https://github.com/qgis/QGIS/issues/25700) | [Commit 2f22aeaf](https://github.com/qgis/QGIS/commit/2f22aeaf276785867ed850f54c691a0a5b7c0aeb) | n/a |
| Show color button style \"Pick color\" and \"Chooe Color\" and symbol button menu | [#25696](https://github.com/qgis/QGIS/issues/25696) | [Commit 39cfd0f9](https://github.com/qgis/QGIS/commit/39cfd0f935bb8c6669237bc7abe6ca89c6a82a32) | n/a |
| Fix out of sync layout bounds after page removal | [#26665](https://github.com/qgis/QGIS/issues/26665) | [Commit d498eed0](https://github.com/qgis/QGIS/commit/d498eed0a5caf01b914a2c25f0c1d255d955b4a9) | n/a |
| \[layouts\] Fix odd selection behavior when keyboard modifiers are pressed when rectangular selection ends | [Commit 37b5af54](https://github.com/qgis/QGIS/commit/37b5af54d9423563d17422f5b90d6a7dbdfe0299) | n/a |  |
| Fix interaction with group members in items panel | [#26674](https://github.com/qgis/QGIS/issues/26674) | [Commit 5154240f](https://github.com/qgis/QGIS/commit/5154240fa94401952329138300dd2035e5519d5e) | n/a |
| \[layout\] Fix invalid svg exports when including metadata | [#28130](https://github.com/qgis/QGIS/issues/28130) | [Commit cc94aebc](https://github.com/qgis/QGIS/commit/cc94aebc6fa2e53adc99902b7f7ac4f87e0361db) | n/a |
| \[legends\] Fix missing symbols for inverted polygon layers when using filter by map content | [#22718](https://github.com/qgis/QGIS/issues/22718) | [Commit abc9f47c](https://github.com/qgis/QGIS/commit/abc9f47ca471540c9b0f9dd6159d3ac7f9791a3c) | n/a |
| Use a slightly larger font size in CRS details on Windows | [#31297](https://github.com/qgis/QGIS/issues/31297) | [Commit 757017c2](https://github.com/qgis/QGIS/commit/757017c2c29a0ea4b72527e4cd98e700c720022c) | n/a |
| \[processing\] Add warning when packaging a geopackage with no layers | [#31888](https://github.com/qgis/QGIS/issues/31888) | [Commit f11e6603](https://github.com/qgis/QGIS/commit/f11e6603957f69a34ad7aa9893aa144cc5020ca4) | n/a |
| \[layouts\] Fix crash when opening layout with dynamic image in html label | [#28996](https://github.com/qgis/QGIS/issues/28996) | [Commit 5db6165f](https://github.com/qgis/QGIS/commit/5db6165fb597c2db278e678953578992789fa38b) | [Commit e29865cd](https://github.com/qgis/QGIS/commit/e29865cd485c3576db27aab4cad86614f3eff2f3) |
| Expose report feature settings when an attribute table is used in an atlas | [#28441](https://github.com/qgis/QGIS/issues/28441) | [Commit 9fd17c8f](https://github.com/qgis/QGIS/commit/9fd17c8f3cce8fb5864db137da71c3cb61b44510) | n/a |
| \[layouts\] Fix attribute table ignores cell margin for top/bottom aligned text | [#31259](https://github.com/qgis/QGIS/issues/31259) | [Commit 7b356fe4](https://github.com/qgis/QGIS/commit/7b356fe4cde1b030ddfb589a22cb59229311074e) | n/a |
| Fix truncated legend symbol borders when layer has opacity set | [Commit 30e14938](https://github.com/qgis/QGIS/commit/30e149387bcccbd14f057a16cb27729c57c9a210) | n/a |  |
| Fix adding/moving legend is very slow with large projects | [#29058](https://github.com/qgis/QGIS/issues/29058) | [Commit 758ac909](https://github.com/qgis/QGIS/commit/758ac9092f9fac3f7533766f329f17832b2dcd35) | n/a |
| \[reports\] Fix predefined scale mode is incompatible with report outputs | [#29196](https://github.com/qgis/QGIS/issues/29196) | [Commit fcd21e48](https://github.com/qgis/QGIS/commit/fcd21e485068d8082bdef0a5a7393b57fe5bf3c1) | n/a |
| Ensure atlas expression evaluation has access to coverage layer scope | [#31807](https://github.com/qgis/QGIS/issues/31807) | [Commit 3de05939](https://github.com/qgis/QGIS/commit/3de059395706a225ca137b3d4a7a34b27d3cc9ae) | n/a |
| Resizing pages to content should not create empty page size if no items are present | [#29034](https://github.com/qgis/QGIS/issues/29034) | [Commit 421e68cf](https://github.com/qgis/QGIS/commit/421e68cf5ae5637001765842e257caf6becdb876) | n/a |
| Fix map rotation does not immediately restore in reports | [#31217](https://github.com/qgis/QGIS/issues/31217) | [Commit f5afebe5](https://github.com/qgis/QGIS/commit/f5afebe5dd0228ceb612a9823a80c77ccd51a1e6) | n/a |
| Do not return nan values when an assistant is used with min val == max val | [#31242](https://github.com/qgis/QGIS/issues/31242) | [Commit 97923751](https://github.com/qgis/QGIS/commit/979237515ce2921b9552a99eda071e9e9a14297a) | n/a |
| \[layouts\] Fix label items don\'t update when their opacity \< 100 | [#29079](https://github.com/qgis/QGIS/issues/29079) | [Commit f9a47738](https://github.com/qgis/QGIS/commit/f9a47738aaaec7504f912b2442195662a216b9e3) | n/a |
| Fix project load status indicator can get \"stuck\" after project load | non signalé | [Commit 40d95b69](https://github.com/qgis/QGIS/commit/40d95b69d91ade71473f5ea0182040d8398cc668) | n/a |
| Fix corrupted expressions in filter indicator tooltips | [Commit 393e623b](https://github.com/qgis/QGIS/commit/393e623ba7d278eabc4f09aeaabb92f56fa269c9) | [Commit 8e0e368f](https://github.com/qgis/QGIS/commit/8e0e368f255ba10c530afd445ecd1ab53bf266bb) |  |
| Fix cannot use GPS panel to draw features in multi polygon/line | [#29144](https://github.com/qgis/QGIS/issues/29144) | [Commit dc2b209d](https://github.com/qgis/QGIS/commit/dc2b209da3609a47b1457c0cb12417afbcb36344) | n/a |
| Fix loss of label background settings when restoring projects. | [#31427](https://github.com/qgis/QGIS/issues/31427) | [Commit aa4a8da3](https://github.com/qgis/QGIS/commit/aa4a8da3a713b6961fccce019c5e9b5778f68b23) | n/a |
| Fix crash in point displacement renderer | [Commit 7043933f](https://github.com/qgis/QGIS/commit/7043933ff2bed42df5ae3439867330e39fe60f53) | n/a |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
