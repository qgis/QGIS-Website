---
draft: 'true'

---
# QGIS en GRASS toegepast voor een paleontologisch onderzoek in West-Portugal
De Associação Leonel Trindade -- Sociedade de História Natural (ALT-SHN) is een non-profitinstituut dat is gevestigd in Torres Vedras, Portugal, gespecialiseerd in paleontologie. Het instituut beheert een grote collectie fossielen, voornamelijk uit de Upper Jurassic. Een van de sleutelproblemen in paleontologisch beheer is om de ruimtelijke context te beoordelen van de plaatsen waar de fossielen zijn gevonden – honderden plaatsen die duizenden verschillende specimens vertegenwoordigen.
## Het project
![](./images/portugal_torres1.jpg){.align-right}

In 2008 kregen we het idee om GIS-technologieën te verkennen om het onderzoek te ondersteunen en een meer holistisch perspectief te krijgen op de erfenis die we behandelen. Dit idee accelereerde het project SIGAP (GIS toegepast in paleontologie) \[2\]. Het project, ondersteund door publieke en private private entiteiten -- voornamelijk de gemeente, Digiterra.hu en het Army\'s Geographic Institute (IGeoE), richtte zich op drie doelen:
- Veldonderzoek met verschillende GPS-en om coördinaten van de plaatsen te verkrijgen;
- Bouwen van een risicomodel om gevaren te identificeren met betrekking tot de paleontologische erfenis en ze aldus beschermend door regelmatig veldonderzoek;
- Bouwen van een geografische database om alle informatie af te handelen en de inventarisatie van de collectie te beginnen.

## Software die we gebruikten
QGIS was het hoofdbestanddeel van het gehele project. gegevens werden direct in QGIS geplaatst en dan bewerkt en gemanipuleerd om de gewenste uitvoer te verkrijgen. De interface van GRASS, verschaft door QGIS, maakte het voor ons mogelijk om complexe ruimtelijke analyses uit te voeren op rasters om het risicomodel te verkrijgen dat we nodig hadden om het veldwerk te plannen en toekomstige verkenningen. Daarnaast maakte het ons mogelijk lagen van PostGIS te importeren en ze te visualiseren in QGIS.

![Vector point data editing and visualization](./images/portugal_torres2.jpg){.align-right}

The choice for QGIS was also encouraged by the multi platform support. The institution has three distinct facilities, and each of those facilities has different systems \---- we have Mac, Windows PC and Linux PC, therefore it\'s of extreme importance that we have the freedom to install the software on any machine we want so we don\'t get stuck to a particular computer.

![Paleontological Risk Map](./images/portugal_torres3.jpg){.align-right}
## Conclusie
The overall experience with QGIS can only be rated has being very good and recommendable. From our point of view, the main advantage of QGIS is that it\'s not just a GIS software --\-- it\'s a productivity suite for spatial data. It allowed us to take advantage of other powerful tools within a single work environment. From QGIS you can work with GRASS, with PostGIS, with GPS data, with webservices and with tens of useful plug-ins developed by users worldwide. The user friendly interface is also a big advantage, especially if you have to train first time users has we\'ve done. The easyness of the interface makes production of maps an everyday task and brought people closer to spatial approaches \[3\].
## Verwijzingen
- \[1\] www.alt-shn.org (alleen Portugees)
- \[2\] MANO, André. (2009) -- Sistema de Informação Geográfica Aplicado à Paleontologia. Paleolusitana: Revista de Paleontologia e Paleoecologia, Torres Vedras: Alt-Sociedade de História Natural. ISSN 1647-2756, n.º 1, p. 245-250.
- \[3\] Mano, André. (2010) -- Projecto SIGAP, Trabalho de Projecto apresentado como requisito parcial para a obtenção do grau de Mestre em Ciência e Sistemas de Informação Geográfica. ISEGI -- UNL, Lisboa, 2010

## Auteur
![André Mano](./images/portugal_torresaut.png){.align-left height="200px"}

Dit artikel werd bijgedragen in november 2010 door André Mano. Hij is verantwoordelijk voor het Geopraphic Department of Associação Leonel Trindade -- Sociedade de História Natural. Zijn werkgebied is gefocust op geotechnologische toepassingen op het gebied van paleontologie, archeologie en culturele erfenis.
