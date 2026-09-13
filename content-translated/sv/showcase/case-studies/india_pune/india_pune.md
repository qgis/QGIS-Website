---
draft: 'true'

---
# Användandet av python konsol för att förbereda offline-kartor från WMS (tile-nerladdning)
Denna studie förklarar hur man förbereder offline-kartor från WMS/WFS eller andra kartor laddade i QGIS kartvy genom att ladda hem delar med hjälp av ett script i Python console. Skriptet genererar även en mosaik av alla delar för framtida bruk.

Accessing raster/vector maps through Web Mapping Service (WMS) service is very common and efficient. It has several advantages such as security, centralized and flexible map styles. Example is Google maps, Yahoo, Bing, MODIS, Landsat, maps published by NASA, NRSC (India). The disadvantage/limitation of WMS is it works via internet or intranet. It may not be possible to get internet connection always especially in the field during survey. Also WMS works slow, compared to any offline image format such as GeoTiff, jpg, img etc.
## Användandet av QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Pythonkonsol
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. X,Y koordinat (övre vänstra och nedre högra) för den första tilen
2. Tilestorlek att ladda ner (t.ex. 0.001 X 0.001 grader)
3. Antal tiles att ladda ner (beräknad på vyns fulla utbredning och storleken på en tile)
4. Målmapp att spara utgående tiles/filer i.

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

The method has limitation that, changes in map at server end will not reflect in offline (downloaded map). In this case user will have to repeat the process and generate new offline map. Second limitation is the offline map created will be image format; it cannot be used for thematic mapping or image classification. With some extra efforts some landuse maps can be converted to vector with some data loss.
## Omfattning
The generated mosaic is pure image even if it is downloaded from thematic map (7-8 color). Using advance tool like reclassification, layer/band stacking this raster can be converted to polygon vector. WMS has several requests such as getcapabilities, getmap, getfeatureinfo etc. Using the getgeatureinfo attribute information for each polygon can be retrieved. The script can be converted to plugin so that anyone without scripting knowledge will be able to use the script.
## Slutsats
The above experiences shows that QGIS can be used at any advanced level. With basic programming skills one can write a small script or a plug-in to improve the quality of work and save time. Within QGIS, access to a repository of plug-ins developed worldwide is the best of QGIS. The PyQGIS Developer Cookbook is a great resource to write a script and raster data processing is much easy now with help of GDAL tools.
## Författare
Denna artikel skrevs i maj 2014 av Prashant Kadji, från Pune (Indien) som för tillfället arbetar som konsult för GIS APP Consultancy Services. Sedan 2009 använder han GIS & RS i NRM, skogsbruk, e-governance, programutvecklingsprojekt i delar av Indien och övriga världen.
- Contact: <kadgiprashant@gmail.com>
- Hemsida www.gisappco.com (under utveckling)
