---
draft: 'true'

---
# Folosirea QGIS în marcarea zonelor de interes pentru Serviciile privind Biodiversitatea și Ecosistemul (HABEaS)
HABEaS \-\-- Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Scopul principal al acestei platforme este de a oferi acces gratuit la o mare varietate de date privind biodiversitatea și serviciile ecosistemice pentru Bazinul Mediteranean, care au fost împrăștiate pe un număr de entități publice și private. În prezent HABEaS WebGIS acoperă partea de sud a Portugaliei, dar până la sfârșitul anului 2012/începutul anului 2013 va fi extins la nord de Portugalia și, de asemenea, la cantonul Tuzla, în Bosnia și Herțegovina. Pe termen lung, dorim să extindem acest instrument pentru întregul Bazin Mediteranean.

![](./images/portugal_lisbon1.jpg){.align-right}

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](./images/portugal_lisbon2.jpg){.align-right}

Informațiile geografice cuprinse în HABEaS au fost, de asemenea, folosite de către WWF pentru a oferi sprijinul necesar identificării Pădurilor cu Valoare Ridicată de Conservare (HCVF), în partea de sud a Portugaliei, care constituie un pas obligatoriu pentru proprietarii de terenuri care doresc certificarea Forest Stewardship Council (FSC) pentru pădurile lor.

![](./images/portugal_lisbon3.jpg){.align-right}

Pentru a calcula valoarea de conservare a fiecărei proprietăți, am folosit SEXTANTE Modelator la crearea unui script care intersectează toate straturile HABEaS cu limitele de proprietate. Utilizând, de asemenea, același instrument, a fost posibilă crearea unui script pentru calcularea automată a cantității de carbon stocată, în prezent, în fiecare proprietate.

![](./images/portugal_lisbon4.jpg){.align-right}
## Concluzii
QGIS este ușor de folosit și are capacități de geoprocesare foarte puternice. Integrarea GRASS GIS și a instrumentelor SAGA GIS în caseta de instrumente SEXTANTE ne-a permis să efectuăm o serie de analize spațiale complexe și să le interconectăm folosind Modelatorul SEXTANTE. A fost, de asemenea, foarte ușoară producerea de hărți de înaltă calitate cu noul Compozitor de Hărți și exportarea lor în format SVG pentru editarea în continuare cu Inkscape, care este un puternic editor de grafică vectorială, cu sursă gratuită.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Autor
![Filipe Dias](./images/portugal_lisbonaut.jpg){.align-left height="200px"}

Filipe Dias este un doctorand la Centrul pentru Ecologie Aplicată (Institutul Superior de Agronomie, Universitatea Tehnică din Lisabona) și un consultant al Programului Mediteranean al Fondului Mondial pentru Natură (WWF).
