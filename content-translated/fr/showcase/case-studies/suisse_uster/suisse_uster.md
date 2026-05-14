---
draft: 'true'

---
# QGIS et l'Infrastructure de Données Spatiales de la ville d'Uster
La ville d'Uster utilise QGIS depuis 2007. Encouragé par la décision du canton de Soleure d'utiliser QGIS pour remplacer Arcgis comme SIG bureautique, Uster a alors décidé de tenter sa chance. La ville a non seulement rejoint l'effort de développement de l'application en suggérant et en testant de nouvelles fonctionnalités mais également en finançant son développement. En retour, Uster peut utiliser une plate forme SIG et un WebSIG indépendants dont l'évolution est soutenue par une communauté d'utilisateurs et de développeurs internationale.

![](./images/suisse_uster1.png){.align-right}

Postgis/PostgreSQL est utilisé comme entrepôt de données central. Les autres bases de données et sources de données, sont dupliquées régulièrement dans PostgreSQL, en utilisant des outils comme OGR et FME. Au départ, QGIS était principalement utilisé pour la visualisation. Le premier utilisateur de QGIS a été un agriculteur qui avait besoin de mener à bien la déclaration de ses parcelles pour recevoir des subventions pour son exploitation. Puis, QGIS fut aussi proposé comme éditeur de données, plateforme de publication de cartes, ou encore pour améliorer la manipulation des objets, ou même pour le composeur d'impressions. La coordination et le parrainage de ces outils furent réalisés, en association avec d'autres utilisateurs suisses de QGIS (Soleure, Thoune et CDE (Université de Berne))  ainsi que des améliorations sur les analyses thématiques, l’étiquetage automatique, l'utilisation des attributs ou des formulaires. 

![](./images/suisse_uster2.png){.align-right}

Les services techniques de la ville utilisent également des logiciels de SIG commerciaux : Autodesk Topobase, pour la capture et l'édition des données d'infrastructure cadastrale et de gestion des eaux usées, et GE Smallworld pour la gestion des réseaux de gaz, d'eau et d'électricité. Cependant, ces systèmes experts sont utilisés par du personnel spécifiquement formé. Tous les autres projets SIG, ainsi que la visualisation des données, sont gérés avec QGIS. 

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

Aujourd'hui, QGIS est utilisé pour les projets SIG suivants :
- visualisation des données sur les eaux usées, intégration des bases de données supplémentaires, et accès direct aux protocoles d'inspection et de cameras vidéos. 
- Visualisation et édition pour les systèmes de planification urbaine, de planification environnementale, de gestion de l'hydrologie, et de gestion des eaux usées.
- visualisation des données d'inventaire souterrain (assainissement, adduction d'eau potable, gaz, électricité, et récemment réseaux de télécommunication)
- visualisation des données topographiques et cadastrales
- visualisation et édition de l'inventaire communal des sites naturels protégés
- visualisation et édition des données de planification urbaine et régionale
- visualisation et édition des données de l'infrastructure routière
- visualisation de statistiques créées directement depuis la base de donnée des habitants passés et présents
- Planification et visualisation pour l'aménagement énergétique (fourniture de gaz, chauffage à partir d'eaux usées, énergie géothermique en sous-sol, centrales de chauffage, etc.) 

Actuellement d'autres projets similaires sont développés.

![](./images/suisse_uster4.png){.align-right}

En 2007, la vitesse à laquelle Qgis serait développé, et la manière dont la communauté et le support seraient mis en place, n'apparaissaient pas encore clairement. Aujourd'hui, il est avéré que la vitesse de développement et d'amélioration de la commuanuté Qgis, dépassent nos prévisions. Le support commercial et communautaire de la part des compagnies Sourcepole et Norbit est excellent. Il y existe une communication directe avec les  dévellopeurs, sans l'intermédiaire d'un gestionnaire de produit ou d'un chef d'équipe. Les développeurs de ces deux compagnies sont également impliqués au premier chef dans le projet Qgis, et ont une excellente connaissance des bases du code.  

Les bugs sont souvent résolus quelques heures ou quelques jours après leur signalement, et les nouveaux développement sont installés dans un temps assez court. Les nouvelles fonctionnalités peuvent être testées immédiatement après leur développement, et proposées aux utilisateurs, si toutefois la qualité est assez stable poour l'utilisateur. Il n'est donc pas nécessaire d'attendre des publications officielles de nouvelles versions. On apprécie donc la liberté de pouvoir influencer le projet et d'installer le logiciel sur autant d'ordinateur que l'on souhaite, sans avoir à gérer de licences. On est donc impatient de participer à de futures collaborations avec la communauté Qgis, et notre partenaire privé, pour faire avancer le projet Qgis. 
## Auteur
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Cet article a été rédigé en Avril 2011 par le Dr. Andreas Neumann. Il est responsable SIG de la ville d'Uster, Suisse.
