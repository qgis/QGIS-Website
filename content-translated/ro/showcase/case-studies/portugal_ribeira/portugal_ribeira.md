---
draft: 'true'

---
# QGIS și GRASS pentru modelarea coridoarelor ecologice pentru lupii din Portugalia de Nord
The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

![Study area in Portugal](./images/portugal_ribeira1.png){.align-right}

Ribeira de Pena este o municipalitate din districtul Vila Real, în partea de nord a Portugaliei. Această municipialitate rurală este caracterizată de agricultură, erbivore, păduri, munți, văi și faună diversă, având o densitate scăzută a populației umane, având condiții de adăpost și hrană pentru lupi. Situată într-o zonă de tranziție între condițiile aspre ale munților Trás-os-Montes și înverzitul Minho, Ribeira de Pena este una dintre municipalitățile care pot funcționa ca și coridor ecologic între zonele de nord, cu o concentrare mai mare de lupi și zonele de sud, cu concentrație mai mică.

Am început să utilizez programe GIS la cursul de biologie și, mai des, în teza mea de master. În acel moment am folosit în principal programe proprietare. După ce am terminat masteratul, nu am mai avut acces la programe proprietare.

Între timp, am intrat în noua lume Linux. Apoi mi s-a cerut să ofer ajutor unor cercetători, pentru modelarea coridoarelor ecologice pentru lupii din Ribeira de Pena, folosind GIS, deoarece nu lucraseră niciodată cu acest tip de program. Pentru că utilizam deja Linux în loc de Windows, prima mea problemă a fost software-ul pe care urma să-l utilizez. Apoi am auzit despre QGIS și am decis să-l încerc, deși părea foarte simplist și incomplet, în comparație cu ceea ce știam deja. Mi-am dat repede seama cât de greșită era concepția mea anterioară, fiind foarte entuziastă de capacitățile de analiză furnizate de QGIS, în special de integrarea cu GRASS.

Pentru a modela coridoarele ecologice, am folosit QGIS, împreună cu plugin-ul GRASS. Am folosit mai multe informații geografice, împreună cu datele despre prezența speciilor, pentru a modela coridoarele ecologice. Aici sunt unele dintre funcțiile QGIS și GRASS folosite în acest caz, pentru a numi doar câteva:
- plugin-ul de Interpolare din QGIS: pentru a crea un Model Digital al Elevației
- r.watershed din GRASS: pentru a crea fluxuri de apă pornind de la DEM
- r.grow.distance din GRASS: generează un strat raster de distanțe până la entitățile din stratul de intrare
- r.reclass din GRASS: pentru a reclasifica straturile hărții
- r.slope.aspect.slope din GRASS: pentru a calcula panta pornind de la DEM
- r.mapcalculator din GRASS: pentru a efectua unele calcule algebrice simple în hartă
- r.cost.coord din GRASS: creează o hartă raster care arată costul cumulat al mișcării între locații geografice diferite pe o hartă raster de intrare, ale cărei valori pentru categoriile celulelor reprezintă costuri
- r.drain in GRASS: Traces a flow through an elevation model on a raster map \---- the one used to create the corridors

Prin această muncă s-a obținut o hartă cu potențialele coridoarele ecologice pentru lupii din municipalitatea Ribeira de Pena. Acestea sunt zonele care urmează să fie luate în considerare de către tehnicienii consiliului municipal, atunci când planifică măsurile de conservare pentru specii. Aceste coridoare sunt de o importanță extremă, deoarece acestea pot conecta haitele de lupi rare din Vila Real, din partea de sud, cu cele din nord, care se învecinează cu cele din Peneda-Gerês și Spania. Sunt importante îndeosebi acele coridoare care traversează așezările umane, cum ar fi cătunele, orașele și drumurile dintre ele. Aceste zone trebuie considerate critice pentru conservarea lupului, luându-se măsuri de reducere a impactului uman asupra acestei specii.

![Ecological corridors and critical conservation areas for wolves in northern Portugal.](./images/portugal_ribeira2.png){.align-right width="100.0%"}
## Concluzii
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Autor
![Monica Almeida](./images/portugal_ribeiraaut.png){.align-left height="200px"}

Acest articol a fost transmis în iulie 2012 de către Monica Almeida. Ea lucrează ca biolog într-o organizație non-guvernamentală, al cărei scop este menținerea populațiilor de lupi în Portugalia.
