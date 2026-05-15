---
draft: 'true'

---
# QGIS si GRASS folosite în studiul paleontologic din Portugalia de Vest
The Associação Leonel Trindade -- Sociedade de História Natural (ALT-SHN) is a non profit institution headquarted in Torres Vedras, Portugal, specialized in paleontology. The institution manages a large fossil collection, mainly from Upper Jurassic. One of the key issues in paleontological management is to assess spatial context of the sites from where the fossils are retrieved -- hundreds of sites representing thousands of different specimens.
## Proiectul
![](./images/portugal_torres1.jpg){.align-right}

Back in 2008, we came up with the idea of exploring GIS technologies to support the investigation and get a more holistic perspective on the heritage we were dealing. This idea boosted SIGAP Project (GIS applied to paleontology) \[2\]. The project, supported by public and private entities -- mainly the Municipalty, Digiterra.hu and the Army\'s Geographic Institute (IGeoE), aimed three goals:
- Vizită în teren cu GPS-ul diferențiat pentru a aduna coordonatele siturilor;
- Construirea unui model de risc pentru a identifica riscurile față de patrimoniul paleontologic și de a le preveni prin vizite periodice în teren;
- Construirea unei baze de date geografice pentru a gestiona toate informațiile și a începe inventarul colecției.

## Softurile folosite
QGIS a fost elementul de bază al tuturor proiectelor. Datele au fost descărcate direct în QGIS, apoi editate și manipulate pentru a atinge rezultatele dorite. Interfața GRASS furnizată de QGIS ne-a permis să efectuăm analize spațiale complexe pe rastere, pentru a obține modelul de risc de care avem nevoie pentru a ne planifica activitatea din teren și prospectările viitoare. Mai mult, ne-a permis să importăm straturi PostGIS și să le vizualizăm în QGIS.

![Vector point data editing and visualization](./images/portugal_torres2.jpg){.align-right}

The choice for QGIS was also encouraged by the multi platform support. The institution has three distinct facilities, and each of those facilities has different systems \---- we have Mac, Windows PC and Linux PC, therefore it\'s of extreme importance that we have the freedom to install the software on any machine we want so we don\'t get stuck to a particular computer.

![Paleontological Risk Map](./images/portugal_torres3.jpg){.align-right}
## Concluzii
The overall experience with QGIS can only be rated has being very good and recommendable. From our point of view, the main advantage of QGIS is that it\'s not just a GIS software --\-- it\'s a productivity suite for spatial data. It allowed us to take advantage of other powerful tools within a single work environment. From QGIS you can work with GRASS, with PostGIS, with GPS data, with webservices and with tens of useful plug-ins developed by users worldwide. The user friendly interface is also a big advantage, especially if you have to train first time users has we\'ve done. The easyness of the interface makes production of maps an everyday task and brought people closer to spatial approaches \[3\].
## Referințe
- \[1\] www.alt-shn.org (portuguese only)
- \[2\] MANO, André. (2009) -- Sistema de Informação Geográfica Aplicado à Paleontologia. Paleolusitana: Revista de Paleontologia e Paleoecologia, Torres Vedras: Alt-Sociedade de História Natural. ISSN 1647-2756, n.º 1, p. 245-250.
- \[3\] Mano, André. (2010) -- Projecto SIGAP, Trabalho de Projecto apresentado como requisito parcial para a obtenção do grau de Mestre em Ciência e Sistemas de Informação Geográfica. ISEGI -- UNL, Lisboa, 2010

## Autor
![André Mano](./images/portugal_torresaut.png){.align-left height="200px"}

This article was contributed in November 2010 by André Mano. He is responsible for the Geopraphic Department of Associação Leonel Trindade -- Sociedade de História Natural. His area of interest is focused on geotechnology applications to the fields of paleontology, archeology and cultural heritage.
