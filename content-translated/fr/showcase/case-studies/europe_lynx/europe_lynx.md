---
draft: 'true'

---
# Analyse de l'habitat du Lynx dans le sud des Carpates
Une étude de cas pour que les étudiants acquièrent les connaissances de base sur la modélisation des habitats des faunes sauvages en se basant sur des données Open Source.
## Introduction
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Méthodologie
Toutes les données acquises ont été traitées avec QGIS 2.6 et 2.8, projetées en ETRS89 / ETRS-LAEA et stockées selon la directive INSPIRE pour adhérer aux normes de l'UE. Un **index discret des poids** global a été défini et appliqué à toutes les données.

![Figure 1: Workflow - Lynx habitat expert model](./images/europe_lynx1.png)

**Description de l'organigramme**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Note : les classes de couverture des sols ont été groupées par présence possible de lynx et activité humaine. Bien que techniquement d'origine ancienne, les informations liées aux valeurs de couverture forestière ont été intégrées de manière à indiquer l'amélioration de l'habitat et comme un exemple général de combinaison de sets de données spatiales* 
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
    
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```

```
    .
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
    
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
    
*Note : Le modèle d'Accessibilité du Chasseur devrait indiquer la possibilité décroissante que les chasseurs ont d'accéder à la zone en fonction de la distance croissante aux routes et de l'augmentation de la pente*

![Figure 2, 3 and 4](./images/europe_lynx2.png)
## Conclusion
En observant le résultat final (Figure 3), l'analyse de l'habitat potentiel apparaît comme un succès et plus important, la modélisation de base n'a pas été aussi difficile qu'escomptée initialement. Notre choix d'ajouter un sous-modèle pour l'accessibilité des chasseurs nous a permit d'implémenter une autre dimension dans la gestion de l'évaluation de l'habitat. Cette dernière peut être intégrée dans le scénario existant et utilisée pour déterminer les besoins de protection selon différents aspects somme le développement des infrastructures. Néanmoins, des données d'habitat cruciales telles que la structure forestière (qui a la meilleure adaptation d'habitat) ne peuvent pas être déterminées selon les jeux de données disponibles ainsi qu'en combinant les comportements complexes des espèces. Ce résultat doit être interprété comme étant un résultat simple et incomplet. Les facteurs supplémentaires non couverts à ce stade sont la mortalité due aux routes, la difficulté de parcours du terrain ainsi que la population précise de proies potentielles.

Au delà de son caractère de logiciel libre et gratuit, QGIS a été sujet à un important développement ces dernières années. Nous avons un retour positif sur l'intégration de la boîte à outils, permettant l'utilisation de nombreux outils GRASS ou SAGA, même pour les utilisateurs inexpérimentés. Aucune erreur de compatibilité n'a été rencontrée malgré l'utilisation de nombreux versions différentes. L'absence de restrictions administratives est un avantage avéré lorsqu'on travaille de manière intuitive avec des jeux de données. Nous sommes impatients de voir les prochaines améliorations notamment en ce qui concerne le modeleur graphique intégré.
## Références
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Auteurs
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe et David Winger sont des étudiants de maîtrise en Gestion Internationale des Écosystèmes Forestiers, Anne Gnilke travaille chez German Forestry et Henri Hiltunen est  un étudiant en échange de l'Université des Sciences Appliquées de Mikkeli, Finlande. Prof. Mund enseigne les SIG et la Télédétection à HNE Eberswalde depuis 2010 et a fourni conseils et soutien technique pour ce projet.

Veuillez contacter Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, ou Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de pour de plus amples informations.
