---
draft: 'true'

---
# QGIS \-\-- an interesting instrument for forestry planning concepts at local and regional level
Almost 35% of Switzerland\'s surface is covered by forests. Changing demands upon the forest and the poor financial situation of forest enterprises in Switzerland led to the development of a new forestry planning concept about fifteen years ago. This concept introduced a clear distinction between planning at the level of the authorities and planning at the level of the owners1. As a new forestry planning office, guaraci works primarily in the region of Basel (Switzerland) on both mentioned planning levels. This case study discusses the use of QGIS at the forest owner level. On this level, a simple, dynamic and compatible geographic information system is required for the establishment of a forest management plan. This plan covers about 1000 ha of forests, will be valid for about 20 years and is implemented by the local forest manager. The area is situated in the region of Basel (see google maps).
## Cum este folosit QGIS
În ansamblul procesului de planificare QGIS a fost folosit pentru următoarele patru sarcini:
- Importul datelor existente. Datele includ hărți de fundal georeferențiate (\*.tif), împreună cu fișierele shape de tip poligon, linie și punct. Pentru managerul pădurii, vizualizarea datelor tematice existente (cum ar fi resursele de apă potabilă și de suprafață, zonele naturale protejate) are o  importanță deosebită în munca sa de zi cu zi.
- Digitizing. The forestry measurements planned by the forest manager had been digitized. The QGIS digitizing tools with the advanced snapping options are very useful and user friendly. The „delimited text" plugin enabled the import of additional data tables.
- Analiza. Au fost calculate zonele pentru diferitele categorii de măsuri. Pornind de la anumite caracteristici cum ar fi liniile de tren sau drumurile, s-au determinat zonele împădurite de protecție.
- Imprimarea și exportul. Editorul de hărți s-a folosit la crearea așezării în pagină. Harta a fost exportată ca fișiere PDF și de imagine.

![Extract of the forestry measurements map](./images/suisse_basel1.jpg){.align-right}
## Concluzii
QGIS is an interesting tool for small planning offices, such as guaraci, as well as for the forest managers and owners. It can be used in a professional context and the presented output result was appreciated by all parties involved. For the mentioned tasks the present QGIS version 1.4 "Enceladus" offers all necessary GIS tools. The most important qualities of QGIS are the intuitive user interface and the compatibility with different file formats. It is an ideal tool for projects that are on one hand based on existing geographic data and on the other hand require the acquisition of new data. The user-manual is helpful and easy to understand. Both from the technical as well as the financial perspective QGIS is an interesting alternative to other GIS software.
## Perspective
Sarcinile de bază ale unui concept de planificare forestieră pot fi îndeplinite cu instrumentele GIS menționate. Guaraci va continua să utilizeze QGIS pentru planificarea forestieră la nivelul proprietarului pădurii. Pe baza experiențelor legate de proiectul prezentat, QGIS poate fi, de asemenea, recomandat pentru concepte forestiere la nivelul autorităților locale. Proiectele mai mari, și mai complexe, cu cerințele de analiză detaliată ar putea fi abordate prin combinarea QGIS cu serverul de baze de date spațiale PostGIS. Noile zone de exploatare, rezervațiile forestiere și zonele de protecție pot fi ușor digitalizate. Din fericire, proprietarii și managerii de păduri vor apela tot des la potențialul QGIS, pentru planificările anuale, precum și pentru documentarea activităților lor forestiere.
## Autor
![Raphael Häner](./images/suisse_baselaut.jpg){.align-left height="200px"}

This article was contributed in June 2010 by Raphael Häner. He is Dipl. Forst Ing. at ETH Zürich, Switzerland and founded his one-man company guaraci in 2009.
