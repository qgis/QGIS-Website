---
draft: 'true'

---
# Modèle de géotraitement QGIS pour les études de micro-zonages sismiques de premier niveau
The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Géochimie environnementale et assainissement des eaux et sols contaminés;
- Gisements minéraux et traitement des minerais, y compris le traitement des eaux usées;
- Géoingénierie et sécurité dans l'excavation de roches;
- Evolution géologique récente;
- Prévention des risques naturels;
- Géoarchéologie et archéométrie.
- Géologie marine
- Géomatique, analyse et développement de SIG.

L'étude de micro-zonage sismique de niveau 1 du territoire de Pietramontecorvino (Apulia, Italie du sud, localisée le long de la chaîne centrale et sud des Apennins) fait partie d'un projet de micro-zonage sismique de 63 municipalités du territoire de Foggia, conduite en collaboration avec l'autorité de bassin d'Apulia (Puglia Adb) et le département de géologie et de géophysique (DDG) de l'Université de Bari. Cette activité a été mise en valeur par le département italien de la protection civile (DPC) et financée par le Comité Interministériel de Planification Economique (CIP n°20/2004).
## QGIS, outil de géotraitement pour les études de micro-zonages sismiques de premier niveau
Le micro-zonage sismique évalue le risque sismique à l'échelle locale en proposant d'identifier les portions de territoires caractérisées par un comportement sismique homogène. Le premier niveau de micro-zonage sismique a la particularité de définir les propriétés lithologiques et la géométrie des unités géologiques qui caractérisent ces portions de territoires (micro-zones).

L'observation des dommages causés par un tremblement de terre montre souvent des variations à l'échelle locale causées non seulement par les structures géologiques mais également par les différents types et qualités des constructions, résultant en différents risques sismiques.

Le micro-zonage sismique évalue le risque sismique local à travers l'identification de portions du territoire, caractérisées par un comportement sismique homogène.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

Le premier niveau de micro-zonage sismique consiste à créer trois cartes thématiques:
1. Carte de levé, incorporant les levés des études de micro-zonation sismique;
2. Carte géo-lithologique, dérivée de cartes géologiques et géomorphologiques à une échelle détaillée intégrant les données lithologiques, stratigraphiques et géotechniques liées aux levés;
3. La carte de micro-zonation sismique de niveau 1 (le produit principal de la micro-zonation de niveau 1) , identifiant les micro-zonations en trois catégories de risques locaux :
   - Zones stables;
   - Zones stables sujettes à amplification;
   - Zones instables

L'objectif de ce travail consiste à créer une méthodologie pour traiter les données topographiques, géologiques, géophysiques et géo-techniques pour pouvoir dessiner les zones sismiques de niveau 1 en utilisant des outils libres.

Le modeleur graphique intégré dans la dernière version de QGIS (2.8.1 au moment de la rédaction) a été utilisé pour la création d'un modèle de géo-traitement simple. Cet outil est très utile pour automatiser un des analyses couramment utilisée pour la création des cartes de micro-zonage sismique de niveau 1, en particulier pour identifier les zones instables sous forme de polygones.

Le modèle utilise différents outils et bibliothèques libres (GRASS, GDAL, QGIS), démontrant l'utilité de QGIS en tant qu'interface graphique simple et unifiée pour différents outils GFOSS (Geospatial Free and Open Source Software) (Fig. 1).

![(Fig. 1) Screenshot from the geoprocessing model.](./images/italy_igag1.png){.align-right}

Le modèle reçoit en entrée (Fig. 2):
- Une couche des courbes de niveau contenant un champ avec la valeur d'élévation
- The name of the field containing elevation values;
- La résolution raster souhaitée pour le MNT et les pentes (10 par défaut)
- Une fichier shapefile de polygones à partir duquel seront extraits les objets intersectant les zones de pente supérieures à 15%;
- Le nom de la couche polygone résultante.

![(Fig. 2) Model input form (left) and execution log (right).](./images/italy_igag2.png){.align-right}

Dès que lancé, le modèle produit les opérations suivantes:
- L'outil GRASS v.to.rast.attribute transforme les lignes de contours des élévations en raster, en acceptant en entrée le shapefile des contours, le nom du champ Z et la résolution du raster;
- L'outil GRASS r.surf.contour crée un modèle d'élévation en prenant en entrée la sortie raster temporaire de l'étape précédente et la résolution du raster;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- L'outil GRASS r.mapcalculator est utilisé pour générer un raster 1 bit identifiant les aires ayant une pente de plus de 15 degrés (cette valeur est codée dans les lignes de guide des microzones, et donc valeur fixe), en utilisant l'expression:

if(A\>15,1,null())

où A est le raster de pente temporaire généré par gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

Le résultat consiste en une couche de polygones où le risque d'instabilité est grand à cause d'une valeur de pente supérieure à 15 degrés. Cette information est automatiquement extraite d'une carte thématique telle que la couche des glissements de terrain (Fig. 3) ou une carte lithologique.

![(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).](./images/italy_igag3.png){.align-right}
## Conclusions
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Références
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Auteurs
Cet article est une contribution de Giuseppe Cosentino et Francesco Pennica (www.igag.cnr.it) en mars 2015.

![Giuseppe Cosentino](./images/guiseppe_cosentino.png){.align-left height="200px"}

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

![Francesco Pennica](./images/francesco_pennica.png){.align-left height="200px"}

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.
