---
draft: 'true'

---
# Creando o Mapa da Ruta da Senda de Fundy con QGIS
![](./images/canada_brunswick1.jpg){.align-left}

The Fundy Footpath is a wilderness hiking trail located along the Fundy coast of New Brunswick, Canada. It is a charter member of the [UNESCO Fundy Biosphere Reserve](http://fundy-biosphere.ca/en/about-us/the-reserve) and affiliated with the [NB Trails Council Inc.](http://www.sentiernbtrail.com/) and the Trans Canada Trail. The Footpath takes hikers through the coastal Acadian Forest, home to the world's highest tides, old growth forests, and several rare and unique types of flora and fauna.

A ruta creouse, mantense e promóvese por un grupo de voluntarios coñecidos como a Fundy Hiking Trail Association Inc. (FHTA)(1975). Como organización sen ánimo de lucro a FHTA acada os fondos para as súas actividades a través da venda de guías que inclúen un mapa da ruta. En 2011 cheguei á FHTA como voluntario para actualizar o mapa oficial da ruta. Como voluntario crear un mapa para unha organización sen ánimo de lucro QGIS cabe a conta tanto como unha ferramenta de edición de datos como para un deseño do mapa final. A través destes esforzos propios e dos membros do FHTA o novo mapa oficial da Senda de Fundy incluído coa guía creouse dende o inicio ata o final con QGIS.

![QGIS GPS Tools Plugin for data collection](./images/canada_brunswick2.jpg){.align-right}
## O Proxecto
O proceso de crear o novo mapa da Senda de Fundy con QGIS pode descompoñerse en tres partes diferentes:
- Captura de datos.
- Edición de datos e preparación.
- Produción de mapas.

Data was collected both with handheld GPS units and from various free data sources. Trail data (e.g. trail centerline, campsite locations, and tidal crossings) was collected with a Garmin GPSMap 60CSX. This data was then transferred from the GPS and to shapefile format in QGIS using the GPS plugin. Free data in vector formats was then obtained from the [Natural Resources Canada (NRCan) CanVec](http://geogratis.cgdi.gc.ca/geogratis/en/product/search.do?id=5460AA9D-54CD-8349-C95E-1A4D03172FDF) website and from [Service New Brunswick (SNB) online](http://www.snb.ca/gdam-igec/e/2900e_1.asp).

![Creation of the footpath map in QGIS](./images/canada_brunswick3.jpg){.align-right}

Para prepara os datos para utilizar no produto do mapa final usáronse as seguintes ferramentas dentro de QGIS para completar tarefas específicas:
- Os datos capturados con GPS pasáronse a limpo empregando a barra de ferramentas de edición.
- Xuntáronse os datos vectoriais obtidos do NRCan e SNB, filtráronse e recortáronse para a área final do mapa usando ferramentas vectoriais.
- Importouse un ficheiro separado por comas obtido do SNB a QGIS como unha capa de puntos usando o plugin Engadir Capa de Texto Delimitado, o plugin Interpolación empregouse para crear un ráster de elevación que se usou para crear un ráster de sombreado e unha capa de liñas de elevación co plugin de ferramentas ráster de GDAL.

![Footpath map in the Print Composer](./images/canada_brunswick4.jpg){.align-right}

Once the data required to create the map was assembled and in a usable format the creation of the final map was started. To create the hiking map data was symbolized and labeled with the symbolization properties dialog and labeled with QGIS's very functional label engine. Once labels and symbolization were in place the map composer tool was run to create the layout. It was very easy to add useful map elements such as a custom north arrow and elevation profile in the print composer. Two layouts were created since it was to be a double-sided map. Once both layouts were created they were exported as PDF files and sent to the printers.
## Conclusión
The hiking map was printed on heavy-duty waterproof paper, folded and inserted in the back of the new edition of the Fundy Footpath Hiker's Guide Book. QGIS was the best and most functional choice for the creation of this map. Being free software the price was right for a volunteer creating a map for a non-profit organization. But the real advantage of QGIS was that it had all of the functionality and tools required to create a highly useful and detailed hiking map from start to finish. I would highly recommend QGIS to both experienced and beginning GIS users alike.

![The final Fundy Footpath map with accompanying guidebook](./images/canada_brunswick5.jpg){.align-right}
## Ligazóns
- <http://fundy-biosphere.ca/en/about-us/the-reserve>
- <http://www.sentiernbtrail.com>
- <http://www.snb.ca/gdam-igec/e/2900e_1.asp>

## Autor
![Jarrett Totton](./images/canada_brunswickaut.jpg){.align-left height="200px"}

Este artigo foi entregado por Jarrett Totton en xaneiro de 2013. Jarrett é un tecnólogo SIX que vive en Alberta, Canadá.
