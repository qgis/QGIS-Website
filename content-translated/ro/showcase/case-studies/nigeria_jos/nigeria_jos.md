---
draft: 'true'

---
# Cartografiere a habitatului și a avifaunei din Amurum Forest Reserve, Nigeria, cu ajutorul QGIS
Amurum Forest Reserve se află în apropiere de orașul Jos, statul Plateau, Nigeria. Înființarea sa a avut loc  în conjuncție cu o inițiativă a Institutului de Cercetare Ornitologică Leventis (APLORI), având scopuri de conservare a naturii, educație și cercetare. APLORI ține de Departamentul de Zoologie al Universității Jos. Anual, un grup de aproximativ opt studenți foarte motivați din întreaga Nigerie sunt instruiți în conservarea diversității biologice, statistică (în limbajul R) și, din 2011, în GIS. Timp de două săptămâni, în luna decembrie 2011, am studiat conceptele de bază ale GIS și cu ajutorul QGIS le-am aplicat în practică, în diverse scopuri de conservare. În acest articol vom descrie modul în care am folosit QGIS la cartografierea habitatelor și cauzele determinante ale acestora, precum și modul în care hărțile habitatelor de bază s-au folosit în scopul determinării eficiente a distribuției spațiale a avifaunei, inclusiv biodiversitatea.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## Cartografierea altitudinii, umbrire deal, pante și habitate
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) Instrumentele Gdal au fost folosite pentru a unifica seturile de date originale și pentru a decupa o zonă mai mică conținând pădurea, astfel încât seturile de date raster au rămas relativ mici. Prin intermediul GPS-ul am colectat elevațiile în diverse locații ale pădurii.
3) În general, cotele din setul de date SRTM corespund cotelor GPS-colectate. Modele ale terenului în GdalTools au fost utilizate pentru a calcula umbrele și pantele dealurilor din zonă. Aceste variabile sunt importante din punct de vedere ecologic, deoarece ele sunt puternic asociate tipului de habitat.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) Din moment ce ne-am propus să dezvoltăm o hartă aspectuoasă, am interpolat harta originalâ (decupată) a elevațiilor pentru a obține o hartă de rezoluție mai mare. Am folosit Warp Tool din GdalTools. Prin intermediul instrumentului de contur am obținut curbe mai netede.
5) Coordonatele limitelor pădurii au fost obținute mergând pe jos de-a lungul perimetrului zonei, și folosind un GPS. Punctele stocate în GPS au fost importate folosind instrumente GPS. Punctele intermediare importate au fost folosite pentru a construi un fișier shape de tip poligon. Curbele din interiorul pădurii au fost trasate într-un mod similar.
6) Am fost capabili de a construi rapid și precis o hartă a habitatului din Amurum, folosind o imagine de satelit de la Google, pe care am afișat-o în spațiul de lucru prin intermediul plugin-ului OpenLayers. Rezerva are trei tipuri de habitat distincte: savană, coridor împădurit și afloriment stâncos. Deasupra imaginii din satelit am folosit editorul pentru a desena poligoanele care delimitează cele trei habitate. Setarea opțiunilor de snapping au permis corecta construire a poligoanelor evitând suprapunerile.

## Cartografierea distribuției păsărilor și a biodiversității
Hărțile de habitat au fost utilizate pentru a genera puncte aleatorii. Zonele diferitelor tipuri de habitat au fost utilizate pentru a genera un număr de locații, proporțional cu suprafața fiecărui tip de habitat (stratificare).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Concluzii
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Autori
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
