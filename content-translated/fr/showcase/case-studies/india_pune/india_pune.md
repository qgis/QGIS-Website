---
draft: 'true'

---
# Utilisation de la console Python pour préparer une carte stockée en local depuis un service WMS (outil de téléchargement de tuile).
Cette étude explique comment préparer des cartes locales à partir de cartes WMS/WFS ou toute carte chargée dans le canevas de cartes de QGIS en téléchargeant des tuiles à l'aide d'un script qui fonctionne avec la console Python. Le script génère également une mosaïque de toutes les tuiles pour une utilisation ultérieure.

Accéder à des cartes raster ou vecteur à travers un service Web Mapping Service (WMS) est très courant et très efficace. Cela a plusieurs avantages dont la sécurité, la centralisation ainsi que des styles de carte flexibles. Par exemple, Google Maps, Yahoo, Bing, MODIS, Landsat, les cartes publiées par la NASA, NRSC (Inde). L'inconvénient/limite de WMS est que le service est fourni par Internet ou via un Intranet. Il est possible de ne pas toujours disposer d'une connexion Internet, particulièrement lors des enquêtes sur le terrain. De plus, WMS est généralement lent par rapport au travail avec des images stockées en local comme le GeoTiff, le jpeg, etc.
## Utilisation de QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Console Python
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. La coordonnée X,Y de la première tuile (coin supérieur gauche et inférieur droit).
2. La taille de la tuile à télécharger (ex: 0.001 x 0.001 degrés).
3. Le nombre de tuiles à télécharger (calculé à partir de l'emprise complete de la carte et la taille des tuiles).
4. Répertoire de sortie pour les tuiles/fichiers générés

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

La méthode a des limites notamment le fait que des changements sur le serveur ne sont pas reflétés localement. Dans ce cas, l'utilisateur doit relancer le script et générer une nouvelle carte locale. Le deuxième limitation est que la carte locale est une image et elle ne peut pas être utilisée pour des cartes thématiques ou pour une classification d'image. Avec un peu d'effort supplémentaire, quelques cartes d'occupation du sol peuvent être converties en vecteur avec des pertes de données.
## Portée
La mosaïque générée est une image même si elle a été téléchargée depuis une carte thématique (7-8 couleurs). En utilisant un outil avancé de reclassification, et l'empilement des bandes, ce raster peut être converti en vecteur polygone. WMS dispose de plusieurs modes de requêtes comme getcapabilities, getmap, getfeatureinfo, etc. En utilisant getfeatureinfo, l'information de l'attribut peut être récupérée pour chaque polygone. Le script peut être converti en extension de manière à ce que toute personne sans compétence de développement sera capable d'utiliser le script.
## Conclusion
Les expériences présentées montrent que QGIS peut être utilisé à n'importe quel niveau avancé. Avec des connaissances basiques en développement, on peut écrire un petit script ou une extension pour améliorer la qualité du travail et gagner du temps. Au sein de QGIS, l'accès au dépôt des extensions développées à travers le monde est une grande force. Le Guide de Recette des Développeurs PyQGIS est une source d'information d'intérêt pour écrire un script et la gestion des données raster est assez simple grâce à l'aide des outils GDAL.
## Auteurs
Cet article a été rédigé en mai 2014 avec la contribution de Prashant Kadgi, basé à Pune en Inde. Il travaille actuellement en tant que consultant SIG pour APP Consultancy Services. Depuis 2009 il utilise les SIG et la télédétection pour la gestion des ressources naturelles, la forêt, le e-gouvernement, les projets de développement logiciel dans différentes régions de l'Inde et du monde.
- Contact: <kadgiprashant@gmail.com>
- Site web : www.gisappco.com (en construction)
