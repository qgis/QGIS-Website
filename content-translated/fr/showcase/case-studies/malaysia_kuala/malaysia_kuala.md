---
draft: 'true'

---
# Utilisation de QGIS au Département Fédéral de la Ville et de l'Aménagement du Territoire, Malaisie péninsulaire
## Introduction
Le Département Fédéral de la Ville et de l’Aménagement du Territoire, Malaisie péninsulaire (JPBD) est une agence fédérale qui donne des conseils en matière d'aménagement du territoire. Le territoire d'administration du département est limité à la Malaisie péninsulaire car Sabah et Sarawak dans l'est de la Malaisie disposent de leurs propres agences d'aménagement. La compétence d'aménagement du territoire est partagé au niveau de la réglementation fédérale. Ainsi, le JPBD conseille le ministère de l'habitat et du gouvernement local qui fournit un appui au JPBD et qui conseille à son tour le conseil national de la planification, géré par le premier ministre. Au niveau de l'état, le directeur d'état conseille le comité d'état de planification dirigé par le ministre en chef. Au niveau local, le JPBD conseille les autorités d'aménagement local dans la préparation des plans de développement obligatoires. Au niveau du siège, la division du plan d'aménagement national prépare le plan d'aménagement national et quatre bureaux régionaux préparent les plans de structure, les plans locaux de district et les plans des aires spéciales. Etant donné que chaque agence publique travaille traditionnellement dans sa spécialité, le  JPBD est le gardien de l'information sur l'utilisation du territoire.
## Le Projet
QGIS a été introduit dans la communauté malaisienne open source comme une alternative viable aux logiciels SIG propriétaires pour les agences publiques par le JPBD lors de la conférence Malaysian Government Open Source Conference (MyGOSSCON) en 2009 ainsi qu'à la communauté malaisienne des SIG lors de la 4ème conférence nationale sur les SIG (NGIS) en 2010. Le JPBD a été historiquement un utilisateur de SIG propriétaire et l'introduction de QGIS a permis d'ouvrir les yeux sur le point de vue des logiciels libres et également sur les SIG Open-Source. La philosophie libre de et différente de QGIS a été perçue comme étrange, peu sûre et non fiable. Sans surprise, l'idée de déployer QGIS n'a pas reçu un grand soutien interne et, dans les faits, elle a recontré de la résistance en 2010 de la direction au groupe de support.

![MyGOSSCON, 2009](./images/malaysia_kuala1.png){.align-right}

On the opposite side, request for technical talks on QGIS came from other technical agencies which JPBD gave to the Ministry of Works and the Department of Irrigation and Drainage. Other works to promote QGIS from JPBD came in the form of newsletter articles on QGIS to the Open Source Competency Centre (OSCC) at the Prime Minister\'s Department and articles introducing QGIS to the Survey Department\'s GIS Bulletin and the Ministry of Natural Resource\'s Public Sector GeoSpatial Bulletin. In the meantime, JPBD researched on developing a slope analysis module for QGIS\'s Windows and Ubuntu version.

L'étude a souligné les avantages et les inconvénients de la personnalisation de module et le haut niveau d'implication de la hiérarchie pour assurer une adoption large et un avancement continu. En 2011, le JPBD a lancé des recherches sur les outils d'analyse de QGIS plutôt que sur la partie cartographie dans le but d'avancer sur des modules inexploités et sur des nouvelles approches d'utilisation de QGIS.

Le département a finalement fait la promotion du paquet QGIS-GRASS à la place du simple paquet QGIS car il était plus puissant et utile pour les travaux liés à l'aménagement du territoire comme le nettoyage des erreurs topologiques et pour dépasser les limitations des entrées standards. Cette opération était simplement le lancement.

![Northern Project Office get QGIS training](./images/malaysia_kuala2.png){.align-right}

In order to centralize and share findings in the use of QGIS for town planning purpose which could also be use in other fields dealing with spatial analysis, an unofficial blog established by the author called "QGIS MALAYSIA" at <http://www.qgismalaysia.blogspot.com> was made to generate a QGIS community in Malaysia. External agencies seem to have more interest in QGIS than JPBD itself and upon their request, JPBD gave QGIS training to the Fire and Safety Department as well as to the Ministry of Education whom later was convinced QGIS will be their de facto GIS tool.

Hearing this, JPBD\'s Research and Development Division took the initiative and requested for QGIS training and subsequently 12 persons were trained. Word of mouth (a godsend thing, though at times, extremely detrimental) spread that QGIS was indeed user-friendly, easy to use and at par with proprietary GIS in mapping task and could take on proprietary GIS when optimized with GRASS modules.

L'intérêt dans QGIS a percé en 2012 avec le soutien de tous les directeurs de bureau d'étude et également par un gros effort de la part de la division information nationale sur l'occupation du territoire qui a propulsé QGIS dans leurs 4 bureaux d'étude, ce qui représente leur plus grand nombre d'utilisateurs SIG. A la fin de 2012, environ 320 personnes du JPBD devraient utiliser QGIS ce qui correspond à environ 90% des utilisateurs de SIG du département.

That is not all. States town planning departments have also requested QGIS training such as Perak including strong interest from poorer states like Perlis and Kelantan. If this catches on, it is anticipated that the use of QGIS may dominate states planning departments and even extend to local planning authorities, many of which are not wealthy. In the meantime, JPBD is seriously studying the use of the QGIS-PosgreSQL-PostGIS package for every planning office\'s client GIS-geodatabase server structure to serve as the foundation of JPBD\'s integrated landuse (iPLAN) network.
## Bénéfice de l'utilisation de QGIS
- Sur l'hypothèse de RM10  000  par licence propriétaire de logiciel SIG, l'utilisation de QGIS sur 320 postes contribuera à épargner au gouvernement fédéral la somme de RM3 200 000;
- Une éradication totale des versions piratées de logiciel SIG et une confiance plus accrue dans l'utilisation des logiciels open source en général et du SIG open source en particulier;
- La formation sur QGIS a été plus facile à gérer. Cela veut dire que l'apprentissage croisé entre le personnel, les divisions, les organismes publics et même les responsables de l'aménagement au niveau local qui utilisent QGIS peut être plus efficace parce que le SIG utilisé est identique;
- L'utilisation de QGIS contribue à la synergie avec une géodatabase PostgreSQL-PostGIS, que le Ministère envisage d'utiliser comme socle pour la base de données sur l'occupation du sol dans toute la Malaisie Péninsulaire.
- Il a été plus rapide d'effectuer la vérification des données et corriger les erreurs topologiques.
- Les utilisateurs deviennent plus courageux et commencent à s'aventurer dans Google Maps et d'autres sources Internet d'informations secondaires;
- La convivialité offerte par QGIS encourage les utilisateurs à être plus aventureux et explorer les nombreuses extensions disponibles pour en tirer le meilleur avantage et rendre leur tâche plus facile.
- SIG, un outil complexe qui devient un ami plutôt qu'une gêne.

## Auteur
![Abbas Abdul Wahab](./images/malaysia_kualaaut.jpg){.align-left height="200px"}

This article was contributed in January 2012 by Abbas Abdul Wahab. Abbas graduated as a town planner from Gloucestershire College of Arts & Design, United Kingdom in 1980 and has a Masters of Science in GIS & Geomatic Engineering from Putra University Malaysia in 2002. He is currently the Head of the National Landuse Information Unit at the National Landuse Information Division of the Federal Department of Town & Country Planning, Peninsular Malaysia.
