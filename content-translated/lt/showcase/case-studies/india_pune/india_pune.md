---
draft: 'true'

---
# Python'o konsolės naudojimas ruošiant be prisijungimo veikiantį žemėlapį iš WMS (kaladėlių atsiuntimas)
Ši studija paaiškina, kaip paruošti be interneto veikiantį žemėlapį iš WMS/WFS arba bet kokio žemėlapio, įkelto į QGIS rodinį, atsiunčiant kaladėles python'o konsolės scenarijumi. Scenarijus taipogi sukuria visų kaladėlių mozaiką, kurią galima naudoti vėliau.

Prieiga prie žemėlapių per Web Mapping Service (WMS) paslaugas labai populiari ir efektyvi. Jos pranašumai yra saugumas, centralizuoti ir lankstūs žemėlapių stiliai. Šių paslaugų pavyzdžiai yra Google žemėlapiai, Yahoo, Bing, MODIS, Landsat, NASA publikuojami žemėlapiai, NRSC (Indija). WMS apribojimas yra tai, kad jis veikia tik prisijungus prie interneto ar intraneto. Deja internetas ne visur pasiekiamas, ypač vykdant apžiūras lauke. Taipogi WMS yra lėtas, lyginant su kitais ne internetinių vaizdų formatais, tokiais kaip GeoTiff, jpg, img ir pan.
## QGIS naudojimas
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Python'o konsolė
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. Pirmos kaladėlės X,Y koordinatė (viršutinis kairys ir apatinis dešinys kampai)
2. Atsiunčiamos kaladėlės dydis (pvz. 0.001 X 0.001 laipsnių)
3. Atsiunčiamų kaladėlių skaičius (paskaičiuojamas pagal pilną žemėlapio apimtį ir kaladėlės dydį)
4. Išvesties aplankas, į kurį įrašomos kaladėlės/failai

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

Šio metodo apribojimas tas, kad žemėlapiui pasikeitus serveryje, pakeitimai nesimatys atsisiųstoje versijoje (be prisijungimo prie interneto). Tokiu atveju naudotojas turės pakartoti procesą` ir sukurti/atsisiųsti naują žemėlapį. Antras apribojimas - sukurtas ne internetinis žemėlapis bus piešinių formato, tai reiškia, kad jo negalima bus naudoti tematiniams žemėlapiams ar klasifikacijai. Pridėjus šiek tiek papildomų pastangų kai kuriuos žemėnaudos žemėlapius galima konvertuoti į vektorinius žemėlapius prarandant šiek tiek duomenų.
## Apimtis
Sukurta mozaika yra grynas paveikslas, net jei ji atsiųsta iš tematinio žemėlapio (7-8 spalvų). Naudojant sudėtingesnį įrankį, tokį kaip perklasifikavimas, sluoksnių/juostų sukrovimas, šį rastrą galima konvertuoti į poligonų vektorius. WMS turi kelias užklausas, tokias kaip getcapabilities, getpam, getfeatureinfo ir pan. Naudojant getfeatureinfo galima gauti kiekvieno poligono atributų informaciją. Scenarijus gali būti konvertuotas į priedą, kad net tie, kas neturi scenarijų žinių, galėtų jį naudoti.
## Išvada
Aukščiau pateiktas pavyzdys rodo, kad QGIS galima naudoti bet kokio sudėtingumo lygmenyje. Turint bazines programavimo žinias bet kas gali parašyti nedidelį scenarijų arba priedą, kuris keltų darbo kokybę ir taupytų laiką. QGIS viena geriausių pusių - priėjimas prie viso pasaulio programuotojų sukurtų priedų skirtų QGIS. PyQGIS programuotojo receptai - puiki medžiaga rašant scenarijų, o rastro duomenų apdorojimas dabar daug paprastesnis, kai naudojami GDAL įrankiai.
## Autoriai
Šį straipsnį 2014 gegužę parašė Prashant Kadgi, gyvenantis Pune (Indija) ir šiuo metu dirbantis konsultantu GIS APP Consultancy Services. Nuo 2009 jis naudoja GIS ir RS NRM, miškų, e-valdymo, programinės įrangos kūrimo projektuose skirtinguose Indijos regionuose ir likusiame pasaulyje.
- Contact: <kadgiprashant@gmail.com>
- Svetainė www.gisappco.com (kuriama)
