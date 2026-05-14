---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Comment QGIS a été utilisé
Au sein du processus de planification, QGIS a été utilisé pour les quatre tâches suivantes :
- Import des données existantes. Les données incluent les fonds de plans géo-référencés (\*.tif) ainsi que les fichiers Shape de polygone, de lignes et de point. Pour le gestionnaire forestier, la visualisation des données existantes (par exemple les ressources en eau, les zones de protection de la nature) est important dans le travail quotidien.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Analyse. Les superficies des différentes catégories de mesures ont été calculées. Des protections forestières ont été définies par un tampon autour de certains objets linéaires comme les voies de chemin de fer ou les routes,.
- Impression et export. Le composeur d'impression gère la création des présentations cartographiques. La carte a été exportée au format PDF et dans des fichiers images.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## Conclusion
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Perspective
Les tâches principales de la planification forestière peuvent être conduites à l'aide des outils SIG basiques mentionnés. Guaraci continuera à utiliser QGIS pour la planification forestière au niveau des propriétaires. Sur la base des expériences du présent projet, QGIS peut également être recommandé pour les concepts forestiers au niveau des autorités locales. Des projets plus larges et plus complexes avec des besoins d'analyse détaillée pourraient être mis en place en combinant QGIS et le serveur de base de données spatiale PostGIS. Les nouvelles zones d'exploitation ainsi que les réserves forestières et les zones de protection pourraient être facilement numérisées. J'ai l'espoir que les propriétaires et les gestionnaires forestiers s'intéressent de plus en plus au potentiel de QGIS, y compris pour leurs plans annuels ainsi que pour documenter leurs activités forestières.
## Auteur
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
