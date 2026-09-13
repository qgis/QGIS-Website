---
draft: 'true'

---
# Utilisation de QGIS pour la planification de réseau FTTH/GPON à cause de l'implémentation de la Stratégie numérique pour l'Europe
## Énoncé du problème
Au cours de ces dernières années beaucoup de pays de l'UE ont lancé des programmes opérationnels pour mettre en place la Stratégie numérique pour l'Europe (SNE) développé par la Commission européenne en 2010. Suivant ses recommandations tout citoyen de l'Union européenne devra, avant 2020, avoir accès à 30 Mbps de bande passante Internet et au moins la moitié d'entre eux auront une bande passante d'au moins 100 Mbps.

La Pologne est un des pays qui est en train de mettre en œuvre cette Stratégie. Grâce aux fonds de l'Union européenne beaucoup d'opérateurs locaux peuvent entrer en concurrence avec les gros fournisseurs de services télécoms en ce qui concerne les services de bande passante grande vitesse. Malheureusement, postuler pour des fonds nécessite beaucoup de travail pour écrire la bonne documentation, y compris, entre autre, la mise en place de la conception des plans conceptuels du réseau de fibre jusqu'au domicile (FTTH).

De plus, il n'y a pas encore un outil informatique basé sur un SIG qui soit disponible pour aider les bénéficiaires potentiels à la préparation de la documentation. La complexité du problème est encore plus exacerbée par le fait qu'un tel logiciel doit permettre la création de documentation en respectant les recommandations spécifiques du programme (c.-à-d. l'obligation de connecter les établissements éducatifs).

À cause de notre très grande expérience dans l'industrie des télécommunications, des entités postulant pour des fonds de l'UE nous ont demandé de créer un logiciel supportant le développement de plans conceptuels de réseau FTTH. Les produits créés par ce logiciel doivent accélérer de manière significative le processus de préparation de la demande.
## Description de la solution
À cause de sa grande popularité, de sa disponibilité immédiate, du fait qu'il soit libre et de ses très grandes capacités, il était tout naturel que QGIS soit choisi comme plateforme pour servir de base à notre solution.

Suivant les directives du Conseil FTTH européen, il est crucial de préparer en premier lieu un plan qui considère à la fois l'aspect technique (emplacement des câbles, boîtiers d'épissures, répartiteurs) et l'aspect économique (la demande) basé sur des données réelles de points d'adresse. La structure des bâtiments et la densité des bâtiments déterminent la technologie de la conception de réseau GPON (Réseau optique passif gigabit). Pour être capable de planifier la topologie du réseau de manière efficace, nous avons besoin, entre autre, de ce qui suit :
- l'accès aux données SIG ;
- l'automatisme des traitements de données SIG ;
- la mise en place d'algorithmes d'optimisation de réseau ;
- la mise en place de la réglementation de l'ingénierie des réseaux GPON.

Tous ces items ont été connectés dans une plateforme SIG. Nous décrivons ci-dessous comment nous avons réalisé le projet et quels sont les items fonctionnels qui ont été incorporés pour créer notre solution.

De manière à réaliser notre but, nous avions besoin de quelques composantes fonctionnelles autres qu'une plateforme SIG standard :
- GRASS - une gamme d'algorithmes de réseaux et de vecteurs ;
- Extensions QGIS - OpenLayer, QuickOSM, Scipy Point Clustering, WorkContextTracer (notre extension) ;
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - une base de données locale pour enregistrer les données d'entrée et de sortie.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](./images/poland_ffth/toolbox.png){.align-left}

Pour éviter de mélanger les résultats des analyses successives, nous avons fourni une extension appelée WorkContextTracer qui groupe notre travail en soit-disant contextes de travail.

![](./images/poland_ffth/workorder.png){.align-left}

Des algorithmes de réseau basés sur les fonctions de graphe disponibles dans GRASS ont été complémentés par l'addition de scripts de télécommunication. Nous avons introduit un concept de groupement de la demande qui permet d'utiliser à la fois les méthodes de K-means et hiérarchiques pour cumuler les points de demande.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

Les opérateurs ont aussi eu besoin de la relation entre les nœuds du réseau créé et les points d'adresse pour estimer le coût individuel de chaque branche du réseau. Pour achever cette tâche, nous avons créé des scripts qui font cette opération et enregistrent les résultats dans une base de données SpatiaLite. Les données devant être exportées vers des tableurs, nous avons donc utilisé une bibliothèque de logiciels libres pour cette tâche.
## Comment les utilisateurs ont utilisé l'outil pour créer un plan de réseau FTTH/GPON
L'utilisateur commence son travail en ouvrant un contexte de travail et en spécifiant la couche source des points d'adresse à analyser. En utilisant l'interface standard de QGIS, l'utilisateur peut ensuite définir un ensemble de points d'adresse à analyser et finalement fournir les paramètres nécessaires aux étapes suivantes de l'algorithme.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

N'ayant pas accès aux informations existantes de l'infrastructure civile, un réseau routier OpenStreet correctement filtré a été utilisé comme couche de routage. Des algorithmes Scipy avec des paramètres en entrée ont regroupé les points d'adresse en cumuls de demandes, les marquant d'une couleur distincte indiquant leur attribution à un groupement particulier.

![](./images/poland_ffth/step1.png){.align-left}

Ayant regroupés tous les points d'adresse, l'utilisateur pouvait lancer les étapes de planification du réseau de haut niveau en fournissant les couches préparées à l'étape précédente et une couche contenant un point de départ pour le réseau GPON.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](./images/poland_ffth/step4_results.png){.align-left}

À ce stade, l'utilisateur a déjà tous les éléments d'information pour créer un concept technique de réseau FTTx de haut niveau. La dernière étape est la création de la feuille de calcul du rapport sur les données montant toutes les données calculées à partir de perspectives différentes.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Conclusion
Grâce à l'utilisation de la plateforme QGIS et à ses capacités d'extension, nous avons pu développer une solution Open Source gratuite permettant aux opérateurs de télécommunication de préparer les documents nécessaires pour soumettre leur demande de cofinancement dans le programme de l'UE qui met en œuvre la Stratégie numérique pour l'Europe.

En combinant des algorithmes flexibles de vecteurs avec les scripts d'ingénierie de télécom, nous avons permis l'utilisation pratique d'algorithmes mathématiques dans la résolution de problèmes réels concernant la planification de réseaux de télécommunication. L'utilisateur opère sur un champs de données compréhensible (municipalité, bâtiment, route) alors que la transformation de cette information en modèles mathématiques n'est pas visible par l'utilisateur.

L'utilisateur obtient beaucoup de résultats utiles :
- Développement automatique de la planification du réseau GPON basé sur des données publiques et la réglementation de l'ingénierie des réseaux GPON.
- Capacité de personnaliser l'outil avec les directives du programme de l'UE dans un pays quelconque.
- La grande précision des résultats correspondant aux dimensions réelles.
- Création des données nécessaires pour la demande de fonds de l'UE : plan conceptuel de réseau, rapport sur les câbles et fermetures d'épissure avec attribution des zones de service.
- Possibilité de déterminer précisément les coûts de construction et de dépréciation de chaque section du réseau avec calcul du coût de raccordement de chaque point d'adresse.
- Possibilité de hiérarchiser les points d'adresse des plus rentables aux moins rentables.
- Possibilité d'évaluer les indicateurs économiques de base comme ROI, NPV.

## Liens utiles et bibliographie
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Auteurs
La solution est un outil Open Source entièrement gratuit. Elle fait partie d'un projet plus important basé sur les plateformes QGIS et FreeCAD et qui a pour intention d'être utilisé dans l'industrie des télécommunications.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.
