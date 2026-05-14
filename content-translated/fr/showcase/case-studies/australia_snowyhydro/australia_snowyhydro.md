---
draft: 'true'

---
# Utiliser la boîte à outils des traitements pour automatiser la classification de la neige
Snowy Hydro Limited (SHL) est un générateur de pic d'électricité basé dans les Montagnes Neigeuses de la Nouvelle-Galles du Sud,  en Australie. Bien que possédant plusieurs ouvrages de génération d'électricité à travers le pays, Snowy Hydro Limited est mieux connu pour son infrastructure emblématique en Australie, le schéma hydroelectrique des Montagnes Neigeuses.

Le schéma hydroélectrique des Montagnes Neigeuses, est rendu possible par des chutes de neige saisonnières dans la région alpine de Nouvelle-Galles du Sud. L'eau issue de la fonte de la neige de printemps est utilisée pour produire de l’électricité pour gérer les pics de demande sur le marché électrique national, tout en détournant également l'eau vers les zones plus sèches de l'intérieur de l'Australie du Sud-Est, pour l'irrigation et l'agriculture.

La classification de la couverture de neige au cours des mois d'hiver permet à SHL de contrôler le cycle de vie de la zone recouverte par la neige, d'archiver ces zones de couverture pour conserver des enregistrements historiques, et de fournir les statistiques de couverture à l'équipe des services hydrographiques pour la production d'eau et les prévisions de stockage.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Arrière-plan
Chaque année pendant les mois d'hiver (du 1 juin au 31 octobre), SHL acquiert autant d'images sans nuages que possible à partir du satellite MODIS Terra (EOS AM). Ces images sont alors intégrées dans un algorithme connu sous le nom l'Index Normalisé de Différence d'Enneigement (NDSI), qui est utilisé pour indiquer les zones où la neige est présente. Alors que cet algorithme n'est pas réservé à un capteur particulier, l'instrument MODIS a été choisi en raison de sa résolution spatiale adéquate et de sa couverture quotidienne de la zone du projet (Carte 1.1 du bassin versant Snowy).
## Objectif
Le but de ce projet est d'automatiser le processus NDSI sous la forme d'un modèle dans la boîte à outils des traitements de QGIS. La sortie attendue est un polygone vecteur montrant la zone enneigée à l'intérieur du bassin versant de Snowy ainsi que des attributs décrivant la surface totale recouverte, en kilomètres carrés.
## Méthode
L'algorithme NDSI reste assez simple (comme montré dans la formule 1.1. Index Normalisé de Différence d'Enneigement (NDS)) et les étapes successives pour extraire la couverture neigeuse sous forme de vecteur se prêtent à être construites dans un modèle de traitement.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

L'algorithme NDSI renverra des résultats compris entre -1 et 1 avec un seuil d'enneigement qui occupera les valeurs supérieures à 0.4. Un exemple de sortie de l'algorithme est présenté ci-dessous (Carte 1.3 Sortie NDSI) ainsi que l'image en couleur naturelle (Carte 1.2 - Image MODIS en couleurs vraies) pour la date du 13 juillet 2014. Comme vous pouvez l'observer sur les images, la sortie NDSI permet de particulièrement bien discriminer les zones enneigées des autres types de couverture ou des nuages. Néanmoins, il peut toutefois mal classer des portions de surface en eau de grande taille comme zones enneigées car l'eau a des caractéristiques d’absorption dans l'infra-rouge. Cette caractéristique de NDSI indique un besoin d'incorporer un masque sur les zones en eau dans une étape du modèle.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## Résultats/Conclusion
La boîte à outils de traitements de QGIS est un dispositif puissant pour automatiser un processus tel que la classification d'enneigement. Le modèle présenté ci-dessus automatise correctement le processus de classification d'enneigement et fournit un jeu de données SIG qui peut être visualisé et être retravaillé dans d'autres outils statistiques. Il permet de supprimer les erreurs subjectives des méthodes antérieurement utilisées par SHL tout en fournissant un outil cohérent et utilisable de manière répétitive. Voici quelques résultats selon les saisons.
### Auteur
Andrew Jeffrey est un analyse SIG au sein de Snowy Hydro Limited, basé à Cooma NSW en Australie. Il est diplômé de l'Université Charles Sturt de Wagga Wagga avec une licence en Science (Bsc) et en Système d'Information Spatiaux en 2004. Dans son travail à Snowy Hydro Limited, il a pu fournir du support géographique sur des projets d'envergure comme l'expérimentation d'ensemencement de nuages mais également, au quotidien dans l'organisation.
