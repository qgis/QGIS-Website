---
draft: 'true'

---
# QGIS en GRASS toegepast voor het bouwen van modellen voor ecologische corridors voor wolven in Noord-Portugal
The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

![Study area in Portugal](./images/portugal_ribeira1.png){.align-right}

Ribeira de Pena is een gemeente in het district Vila Real in het noorden van Portugal. Het is een landelijke gemeente, gekarakteriseerd door landbouw, grazend vee, bossen, bergen, valleien en diverse fauna, naast een lage bevolkingsdichtheid, dat beschutting en voedsel verschaft aan de wolven. Gelegen in een overgangsgebied tussen de onherbergzame en bergachtige Trás-os-Montes en de groene Minho, is Ribeira de Pena één van de gemeenten die kan werken als een ecologische corridor tussen gebieden met hogere concentraties wolven in het boorden en lagere concentraties in het zuiden.

Ik begon met het gebruiken van software voor GIS software gedurende mijn cursus biologie, en vaker gedurende mijn masterthesis. Op dat moment gebruikte ik voornamelijk merkgebonden software. Nadat ik mijn Master had voltooid, verloor ik de toegang tot de merkgebonden software.

Tegelijkertijd betrad ik de nieuwe wereld van Linux. Hierna werd ik verzocht om, met behulp van GIS, enkele onderzoekers te helpen om modellen te bouwen voor ecologische corridors voor wolven in Ribeira de Pena, omdat zij nog nooit met dit soort gereedschap hadden gewerkt. Omdat ik al Linux gebruikte in plaats van Windows, was min eerste probleem vast te stellen welke software te gebruiken. Ik hoorde over QGIS en besloot het te proberen, hoewel het zeer eenvoudig en incompleet leek te zijn, vergeleken met wat ik al kende. Ik realiseerde al snel dat ik er volledig naast zat en werd razend enthousiast door de door QGIS verschafte analytische mogelijkheden, in het bijzonder de integratie van GRASS.

We gebruikten QGIS tezamen met de plug-in GRASS om modellen te bouwen voor de ecologische corridors. We gebruikten verschillende geografische informatie naats gegevens over de aanwezigheid van de soort om modellen te bouwen voor de ecologische corridors. Hier zijn enkele functies van zowel QGIS als GRASS die in dit geval werden gebruikt, slechts om er enkele te noemen:
- plug-in Interpolatie in QGIS: om een Digital Elevation Model te maken
- r.watershed in GRASS: om waterstromen uit de DEM te maken
- r.grow.distance in GRASS: genereert een rasterkaartlaag voor afstanden tot objecten in de invoerlaag
- r.reclass in GRASS: om kaartlagen opnieuw te classificeren
- r.slope.aspect.slope in GRASS: om de helling uit de DEM te berekenen
- r.mapcalculator in GRASS: om enige eenvoudige algebra voor de kaart te berekenen
- r.cost.coord in GRASS: maakt een rasterkaart die de cumulatieve kosten weergeeft van de verplaatsing tussen verschillende geografische locaties op een invoerrasterkaart waarvan de waarden van categorieën kosten vertegenwoordigen
- r.drain in GRASS: Traces a flow through an elevation model on a raster map \---- the one used to create the corridors

Met dit werk verkregen we een kaart met de potentiële ecologische corridors voor wolven in de gemeente Ribeira de Pena. Met deze gebieden moet door technici van de gemeente rekening worden gehouden bij het plannen van maatregelen ter bescherming van de soort. Deze corridors zijn van extreem belang omdat zij de fragiele roedels wolven in Vila Real in het zuiden verbinden met die in het noorden, welke doorlopen in de veel meer stabiele van Peneda-Gerês en Spanje. Het is van bijzonder belang voor die corridors die menselijke nederzettingen, zoals kleine dorpen, steden en wegen, doorsnijden. Deze gebieden moeten geacht worden kritiek te zijn voor het behoud van de wolf, en vereisen maatregelen om de menselijke invloed op deze soort te beperken.

![Ecological corridors and critical conservation areas for wolves in northern Portugal.](./images/portugal_ribeira2.png){.align-right width="100.0%"}
## Conclusie
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Auteur
![Monica Almeida](./images/portugal_ribeiraaut.png){.align-left height="200px"}

Dit artikel werd bijgedragen in juli 2012 door Monica Almeida. Zij is een bioloog voor natuurbehoud die werkt voor een niet-gouvernementele organisatie voor het behouden van de wolf in Portugal.
