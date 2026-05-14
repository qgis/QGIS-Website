---
draft: 'true'

---
# Utilisation de QGIS dans la pile de logiciels FOSSGIS du gouvernement du Canton de Soleure en Suisse
![](./images/suisse_solothurn1.png){.align-left}

Le Canton de Soleure fournit des services et une infrastructure à 250 000 citoyens. En 2001, le Parlement d’État a décidé de migrer de Windows vers Linux. Les motivations étaient de devenir indépendant vis à vis d'un éditeur en particulier, d'encourager la libre entreprise et de réduire les coûts de licence. Le département SO!GIS du Canton de Soleure a ainsi commencé à répondre aux besoins en SIG de plus de 3 500 employés via une stratégie FOSSGIS.

La première étape a consisté à mettre en service un serveur UMN MapServer ainsi qu'à créer le client SO!Map offrant un client SIG Web simple à utiliser pour l'ensemble des 3 500 employés. La deuxième a consisté à migrer de toute les données spatiales depuis le format Shapefile vers une base de données spatiale PostGIS. Le démarrage a été un succès, mais il manquait un logiciel SIG bureautique convivial.

Après une évaluation des différentes solutions existantes de logiciels SIG bureautiques, nous avons décider d'utiliser QGIS combiné à GRASS en remplacement d'ArcInfo d'ESRI  et d'Arcview 3 en 2006.

La décision a été motivée par les aspects suivants :
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Organisation du projet OSGeo
- Interface traduite en allemand
- Documentation rédigée en allemand
- Un développeur actif (Marco Hugentobler) près de Soleure en Suisse.
- Nous pouvions passer commande auprès de Marco Hugentobler pour l’implémentation des fonctionnalités manquantes comme la numérisation et la mise en page.
- Développement d'application et d'extension en Python
- Une communauté d'utilisateurs qui s'agrandit
- Une communauté de développeurs très active
- Indépendance vis-à-vis d'un système d'exploitation

## Notre utilisation de QGIS
Contrairement aux cartes interactives affichées par UMN Mapserver, le logiciel SIG bureautique devait offrir une vision flexible des données spatiales de Soleure. Le SIG bureautique QGIS est utilisé tous les jours par plus de 50 utilisateurs. Mais beaucoup d'entre eux ne sont pas des experts en SIG. Ils veulent juste visualiser et/ou saisir de la donnée spatiale avec une interface utilisateur intuitive.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA contient un inventaire facile à lire de tous les modèles de données et les utilisateurs non-experts en SIG sont capables ainsi de lire la base de donnée pour découvrir l'information dont ils ont besoin.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusion
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Auteur
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

Cet article a été rédigé en mai 2009 par le Dr. Horst Düster, coordinateur SIG au Departement of Geoinformation du Canton de Soleure en Suisse.
