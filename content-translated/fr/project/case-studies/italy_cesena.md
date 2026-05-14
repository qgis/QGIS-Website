---
HasBanner: false
archived: true
date: 2015-10-30
draft: false
featured: false
section: projet
sidebar: true
thumbnail: images/italy_cesena1.png
title: QGIS pour décrire le mur de Cesena
type: case-study

---
{{<content-start >}}
# QGIS to describe the Cesena\'s Wall
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>October 30, 2015</span>
</p>

L'Université ECAMPUS a été créée comme une université en-ligne et est reconnue par le MIUR (Le ministère italien de l'éducation, des université et de la recherche) par arrêté ministériel du 30 janvier 2006. Elle a été établie dans le but  de fournir aux jeunes gens, aux professionnels, aux entrepreneurs, aux cadres et aux acteurs des affaires et de la culture un accès à l'université au travers d'une plate-forme d'apprentissage en ligne pour contribuer au marché du travail. Le siège, connu sous le nom du Campus International de Milan, ou Campus de Novedrate, est situé dans l'ancien centre de formation d'IBM à Novedrate (Como, Italie), sur un campus de la tranquille et verte Brianza.

L'université a 5 facultés virtuelles : Ingénierie, Économie, Psychologie, Arts et Droit. LES CARTES HISTORIQUES ET LE PROJET QGIS Le mur de la cité caractérise la ville de Cesena. Sa forme en scorpion sépare le centre historique des zones nouvelles.

Les documents cartographiques historiques décrivent son évolution et ses destructions. Le logiciel QGIS me permet de comparer différentes cartes historiques, car il permet de transférer toutes les cartes dans le même système de référence, grâce à l'extension de géo-référencement. Les couches libres Google Satellite et Open Street Map ont été utilisées comme références pour référencer les cartes historiques dans le système de référence EPSG:3857 (Mercator Web ou Pseudo Mercator).

QGIS a été un outil fondamental pour élaborer, analyser et comparer ces cartes géo-référencées avec les couches vectorielles ou shapefiles, dans lesquelles j'ai sauvegardé tous les éléments des cartes, tels que routes, bâtiments, parcs et jardins, mur de la cité, les anciennes tours fortifiées et les anciennes portes de la cité. J'ai utilisé des couches de points, de lignes et de polygones avec les outils d'analyse, de recherche, de traitement spatial, de géométrie et de gestion des données (Fig. 1). 

<figure>
<img src="../images/italy_cesena1.png" style="width:100.0%" alt="italy_cesena1.png" />
<figcaption>Fig. 1 Concept Map of the QGIS project</figcaption>
</figure>

En utilisant cet outil, j'ai obtenu des informations sur :
- The precision of the Leonardo Da Vinci\'s topographic survey, realized in 1502, such as how many points of this survey are correct (Fig. 2);
- The Cesena Wall\'s Development from the Roman Age to the 15th Century;
- The Cesena Wall\'s Demolitions from the 19th Century to the Early 20th Century;
- Les changements morphologiques du mur de la cité, tels que la démolition de ses anciennes tours fortifiées et les anciennes portes de la cité ;
- The Cesena\'s Urban Progress from the 16th Century to the Present;

<figure>
<img src="../images/italy_cesena2.png" style="width:100.0%" alt="italy_cesena2.png" />
<figcaption>Fig. 2: Openlayer Google Satellite overlapped by the informations recorded in different layers: the present City Wall in black, the Leonardo Da Vinci's topographic survey of the City Wall in orange, the Leonardo Da Vinci's points of survey in yellow and the present ancient City Gates in red.</figcaption>
</figure>

Il y a beaucoup d'outils dans QGIS et j'en ai utilisé quelques unes pour créer :
- Liens qui connectaient chaque section de la couche linéaire du mur actuel de la cité aux photos, qui représentent l'état de conservation actuel ;
- Une carte de Cesena au 19ième siècle affichée dans le composeur d'impression ;
- Un modèle 3D de Cesena réalisé avec l'extension qgis2threejs (Fig. 3) ;

<figure>
<img src="../images/italy_cesena3.png" style="width:100.0%" alt="italy_cesena3.png" />
<figcaption>Fig. 3: The 3D model of the present City Wall and Cesena's buildings inside and outside the Wall. The ancient fortified towers and the ancient City Gates are indicated.</figcaption>
</figure>

## Conclusion
Les cartes historiques sont des documents importants même si leur précision ne peut pas être comparée à la précision du document cartographique actuel, et elles sont des représentations très parlantes même pour ceux qui ne sont pas des spécialistes en représentation géographique. QGIS était le seul moyen qui m'a permis d'utiliser le contenu numérique des cartes historiques en accord avec un représentation effective et significative.
## Index Bibliographique
Les cartes historiques on été extraites de :
- \"Costruzione, alterazione e recupero del centro storico di Cesena\", Ballardini, Cantori, Pezzi, Righetti, Tossani, Bruno Ghigi Editore, 1977
- \"La cinta muraria di Cesena\", Pino Montalti, Edizioni Panini, 1986

Les informations historiques on été extraites de :
- \"La cartografia in Italia: nuovi metodi e nuovi strumenti dal Settecento ad Oggi\", Andrea Cantile, IGM Firenze, 2007
- \"Lineamenti di storia della cartografia italiana, volume secondo, dal Seicento al Novecento\" Andrea Cantile, Geoweb, 2013
- \"I rilievi cartografici di Leonardo per Cesena ed Urbino contenuti nel manoscritto \'L\' dell\'Istituto di Francia\", Nando De Toni, G. Barbéra Editore, 1965
- \"La città da guerra\", Amelio Fara, Einaudi, 1993
- \"La cartografia dall\'antichità fino al XVIII secolo\", Carlo Monti, Maggioli Editore, 2011

## Auteur
Camilla Fabbri has a bachelor\'s degree in Civil and Environmental Engineering. She has developed her dissertation on historical cartography of the Cesena Wall using the QGIS program with the Supervisor Alessandra Borghi, who is the University Teacher of Topography and Theoretical Mechanics of the bachelor\'s degree in Civil and Environmental Engineering in the eCampus University.

{{<content-end >}}
