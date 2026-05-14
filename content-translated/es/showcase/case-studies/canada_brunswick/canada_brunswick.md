---
draft: 'true'

---
# Creación del mapa de la ruta de Fundy Footpath con QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

El sendero se creó y es mantenido y promovido por un grupo de voluntarios conocidos como el Fundy Senderismo Trail Association Inc. (FHTA) (1975). Como una organización sin fines de lucro la FHTA recauda fondos para sus actividades a través de la venta de guías que incluyen un mapa de los senderos. En 2011, me ofrecí a la FHTA como voluntario para actualizar el mapa oficial de senderismo. Como voluntario, para crear un mapa para una organización sin fines de lucro, QGIS encajaba como una herramienta para la edición de datos y para la elaboración final de los mapas. A través de mis esfuerzos y los de los miembros de la FHTA, el nuevo mapa oficial del Fundy FootPath incluido en la guía fue creado de principio a fin con QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## El Proyecto
El procedimiento para crear el nuevo mapa de Fundy Footpath mediante QGIS se puede dividir en tres partes diferentes:
- Captura de datos.
- Edición y preparación de los datos.
- Elaboración del mapa.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

Para preparar los datos para su uso en el mapa final se utilizaron las siguientes herramientas dentro de QGIS para realizar tareas específicas:
- Los datos recogidos mediante GPS fueron limpiados utilizando la barra de herramientas de edición.
- Los datos vectoriales obtenidos de NRCan y SNB fueron puestos en común, consultados y recortados al área final del mapa utilizando las herramientas vectoriales.
- Se importó a QGIS un archivo separado por comas obtenido de SNB como una capa de puntos mediante el complemento Agregar Capa de Texto Delimitado. Se utilizó el plugin de interpolación para crear un raster de elevación que posteriormente se usó para crear una capa de contorno ráster de sombreado y elevación con el complemento de herramientas raster GDAL.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusión
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Enlaces
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Autor
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Este artículo fue aportado por Jarrett Totton en enero de 2013. Jarrett es tecnológo SIG que vive en Alberta, Canadá.
