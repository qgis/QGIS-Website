---
draft: 'true'

---
# Uso de herramientas de procesamiento para automatizar la clasificación de la nieve
Snowy Hydro Limited (SHL) es un generador de electricidad de pico ubicado en las Montañas Nevadas de Nueva Gales del Sur, Australia. A pesar de poseer una variedad de activos de generación en todo el país, Snowy Hydro Limited es mas conocida por la custodia de una pieza emblemática de la infraestructura australiana, el Esquema Hidroeléctrico de las Montañas Nevadas.

El esquema hidroeléctrico de Snowy Mountains es posible gracias a las nevadas estacionales en la región alpina de Nueva Gales del Sur. El agua de la nieve de la primavera se derrite y se utiliza para generar electricidad que atiende la demanda máxima en el mercado nacional de electricidad, al tiempo que desvía el agua hacia las zonas más secas del interior del sudeste de Australia para el riego y la agricultura.

La clasificación de la cobertura de nieve durante los meses de invierno le permite a SHL monitorear el ciclo de vida del área cubierta de nieve, registrar las áreas de cobertura de registros históricos y proporcionar estadísticas de cobertura al equipo de servicios hidrográficos para el rendimiento del agua y los pronósticos de almacenamiento.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Fondo
Cada año durante los meses de invierno (1 de Junio a 31 de octubre) el SHL obtiene tantas imágenes libres de nubes como sea posible del satélite MODIS Terra (EOS AM). Estas imágenes son entonces alimentadas a un algoritmo conocido como el Índie Normalizado de Diferencia de Nieve (NDSI), el cual es usado para indicar áreas donde la nieve está presente. Mientras que este algoritmo no es único a algún tipo de sensor en particular, el uinstrumento MODIS fue elegido debido a su adecuada resolución espacial y cobertura diaria del área del proyecto. (Mapa 1.1 Cuenca de Agua Nevada)
## Objetivo
El objetivo de este proyecto es para automatizar el flujo de trabajo del NDSI como un modelo el la caja de herramientas de procesamiento de QGIS. La salida requerida es un polígono vectorial que muestra la extensión cubierta de nieve dentro de la Captación de agua de nieve, junto a la  atribución que describe el área total cubierta en kilómetros cuadrados.
## Método
El algoritmo NDSI por si solo es muy sencillo (se muestra abajo en la Formula 1.1 - Índice de nieve de Diferencia Normalizada (NDSI)) y los pasos posteriores requeridos para extraer la cubierta de nieve en un formato vectorial también se prestan muy bien a un modelo de caja de herramientas de procesamiento.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

EL algoritmo NDSI regresa resultados entre -1 y 1, con el umbral para nieve generalmente con valores mayores a 0.4. A continuación se muestra un ejemplo de la salida NDSI (Mapa 1.3 - Salida NDSI), junto con una imagen en color natural (Mapa 1.2 - Color verdadero MODIS) para el 13 de julio de 2014. Como se ve en estas imágenes, la salida NDSI es muy buena para discriminar nieve Áreas cubiertas de otros tipos de cobertura terrestre y nubes. Sin embargo, puede clasificar erróneamente porciones de cuerpos de agua grandes como nieve, debido por el agua que tiene características de absorción en la parte del espectro de infrarrojo cercano. Esta característica del NDSI indica la necesidad de incorporar una máscara de agua en alguna etapa del modelo.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## Resultados/Conclusión
La caja de herramientas de procesamiento de QGIS es una manera poderosa de automatizar un flujo de trabajo como la clasificación de nieve. El modelo que se muestra arriba automatiza con éxito el proceso de clasificación de la nieve y entrega un conjunto de datos SIG que puede utilizarse para la visualización y la entrada en otras aplicaciones estadísticas. Elimina con éxito el error subjetivo del usuario asociado con los métodos anteriores usados por SHL, mientras proporciona una herramienta de clasificación repetible y consistente. Aquí se pueden ver algunos resultados estacionales.
### Autor
Andrew Jeffrey es un analista de SIG en Snowy Hydro Limited con sede en Cooma NSW, Australia. Se graduó de la Universidad Charles Sturt en Wagga Wagga con una Licenciatura en Ciencias (Bsc) con especialización en Sistemas de Información Espacial en 2004. Mientras que en Snowy Hydro Limited, ha podido brindar apoyo espacial a proyectos interesantes como el experimento Cloud Seeding, y el día a día de operaciones dentro de la organización.
