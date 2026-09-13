---
draft: 'true'

---
# Utilizarea consolei Python în pregătirea unei hărți offline WMS (descărcător de plăcuțe)
Acest studiu explică cum se pot pregăti hărțile offline provenite din WMS/WFS, sau orice alte hărți încărcate în QGIS, prin descărcarea pieselor cu ajutorul unui script din consola Python. Script-ul generează, de asemenea, un mozaic cu toate piesele, pentru utilizarea ulterioară. 

Accesarea hărților raster/vector prin Web Mapping Service (WMS) este foarte comună și eficientă. Aceasta are mai multe avantaje, cum ar fi securitatea și stilurile de hartă centralizate și flexibile. Exemple ar fi Google Maps, Yahoo, Bing, MODIS, Landsat, hărțile publicate de NASA, NRSC (India). Dezavantajele/limitările WMS constau în funcționarea prin internet sau intranet. Este posibil să nu aveți în continuu conexiune la internet, mai ales pe timpul achiziției datelor în teren. De asemenea, WMS funcționează lent, comparativ cu orice alt format de imagine offline, cum ar fi GeoTiff, jpg, img, etc
## Utilizare QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Consolă Python
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. Coordonatele X,Y ale primei plăcuțe (stânga sus și dreapta jos)
2. Mărimea plăcuței care va fi descărcată (de exemplu 0.001 X 0.001 grade)
3. Numărul de plăcuțe care vor fi descărcate (calculat pe întreaga suprafață a hărții și dimensiunea plăcuței)
4. Directorul de ieșire pentru a stoca plăcuțele/fișierele de ieșire

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

Metoda are limitări, deoarece schimbările în harta de pe server nu se reflectă offline (în harta descărcată). În acest caz, utilizatorul va trebui să repete procesul și să genereze noi hărți offline. A doua limitare este că harta offline creată va fi într-un format de imagine; ea nu va putea fi utilizată pentru cartografierea tematică sau clasificarea imaginilor. Cu unele eforturi suplimentare unele hărți pot fi convertite în vectori cu ceva pierderi de date.
## Domeniul de aplicare
Mozaicul este generat ca imagine pură, chiar dacă este descărcat de pe harta tematică (7-8 culori). Folosind instrumentele avansate, cum ar fi reclasificarea, stivuirea straturilor/benzilor, aceste rastere pot fi convertite într-un vector poligonal. WMS suportă mai multe cereri, cum ar fi getcapabilities, getmap, getfeatureinfo etc. Folosind atributul getgeatureinfo se pot obține informațiile pentru fiecare poligon. Script-ul poate fi convertit într-un plugin, astfel încât oricine, fără cunoștințe de scripting, va putea folosi script-ul.
## Concluzii
Experiențele de mai sus arată că QGIS poate fi folosit la orice nivel avansat. Cu minime cunoștințe de programare, se poate scrie un mic script sau un plug-in, pentru a îmbunătăți calitatea muncii și pentru a salva timp. În cadrul QGIS, accesul la un depozit de plug-in-uri dezvoltate la nivel mondial reprezintă cea mai bună parte a QGIS. Cartea de Rețete a Dezvoltatorului PyQGIS este o bună resursă pentru a scrie un script de prelucrare a datelor raster, lucru care este mult mai ușor acum, grație instrumentelor GDAL.
## Autori
Acest articol a fost transmis în mai 2014 de către Prashant Kadgi, care locuiește în Pune (India) și, în prezent, lucrează în calitate de consultant în Servicii GIS APP. Din 2009 el folosește GIS & RS în NRM, silvicultură, e-guvernare, proiecte de dezvoltare de software în diferite regiuni ale Indiei și în lume.
- Contact: <kadgiprashant@gmail.com>
- Site web www.gisappco.com (în construcție)
