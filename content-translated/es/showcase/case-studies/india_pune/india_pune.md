---
draft: 'true'

---
# Uso de la consola de Python para preparar mapas sin conexión desde WMS (tile downloader)
El estudio explica cómo preparar mapas fuera de línea a partir de WMS/WFS o cualquier mapa cargado en la vista de mapa QGIS descargando teselas con la ayuda de un script en la consola python. El script también genera un mosaico de todas las teselas for uso posterior.

El acceso a mapas ráster/vectoriales a través del servicio del Servicio de Mapas Web (WMS) es muy común y eficiente. Tiene varias ventajas como seguridad, estilos de mapas centralizados y flexibles. Ejemplo de ello son los mapas de Google, Yahoo, Bing, MODIS, Landsat, mapas publicados por la NASA, NRSC (India). La desventaja/limitación de WMS es que funciona a través de Internet o intranet. Puede que no siempre sea posible obtener conexión a Internet, especialmente en el campo durante el levantamiento o encuesta. Además, WMS funciona de forma lenta, en comparación con cualquier formato de imagen sin conexión, como GeoTiff, jpg, img, etc.
## Uso de QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Consola de Python
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. Coordenada X, Y (superior izquierda e inferior derecha) del primer tile
2. Tamaño del tile para ser descargado (ejemplo 0.001 X 0.001 grados)
3. Número de tiles para descargar (calculado con base en la extensión completa del mapa y el tamaño del tile)
4. Directorio de salida para almacenar las tejas/archivos de salida

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

El método tiene la limitación de que los cambios en el mapa en el servidor no se reflejarán fuera de línea ( en el mapa descargado). En este caso, el usuario tendrá que repetir el proceso y generar un nuevo mapa sin conexión. La segunda limitación es que el mapa sin conexión creado será en formato de imagen; no se puede utilizar para mapeo temático o clasificación de imágenes. Con algunos esfuerzos adicionales, algunos mapas de usos del territorio se pueden convertir en vectoriales con cierta pérdida de datos.
## Alcance
El mosaico generado es una imagen pura incluso si se descarga de un mapa temático (7-8 colores). Usando una herramienta avanzada como la reclasificación o el apilamiento de capas/bandas, este ráster puede convertirse en un vectorial de polígonos. WMS tiene varias peticiones, como getcapabilities, getmap, getfeatureinfo, etc. Usando  getfeatureinfo se puede recuperar la información de atributos para cada polígono. La secuencia de comandos se puede convertir en un complemento de modo que cualquier persona sin conocimientos de scripting pueda utilizarla.
## Conclusión
Las siguientes experiencias muestran como QGIS pueden ser usadas a cualquier nivel. Con aptitudes básicas de programación se pueden escribir pequeñas rutinas o complementos para ahorrar tiempo y mejorar la calidad de trabajo. Dentro de QGIS, es posible acceder al repositorio de complementos desarrollados en todo el mundo. El PyQGIS Developer Cookbook (En Inglés) es un excelente recurso para escribir rutinas y con las herramientas de GDAL ahora es mucho más fácil procesar datos ráster.
## Autores
Este artículo fue aportado en mayo de 2014 por Prashant Kadgi, radicado en Pune (India) y quien trabaja actualmente como consultor en GIS APP Consultancy Services. Desde 2009, utiliza GIS & RS en proyectos de desarrollo de software, gestión de recursos naturales, silvicultura, gobierno electrónico, en diferentes regiones de la India y el mundo.
- Contact: <kadgiprashant@gmail.com>
- Sitio web www.gisappco.com (en construcción)
