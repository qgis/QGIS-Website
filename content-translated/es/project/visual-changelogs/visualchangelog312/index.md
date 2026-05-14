---
HasBanner: false
draft: false
releaseDate: '2020-02-21'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.12
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.12{#changelog312 }
![image1](images/projects/dbf38cfe3b603e7e0b840336d39b399a1a46e52d.png)

Fecha de lanzamiento: 2020-02-21

Si buscas nuevas características y una tonelada de errores corregidos, esta versión te hará sonreir de oreja a oreja!. QGIS 3.12 añade nuevas y ricas funcionalidades para casi cada parte de QGIS. Desde mascaras de etiquetas hasta un proveedor nativo para raster de PostGis, nuevas e increíbles capacidades para capas de datos tipo malla, y mucho, mucho mas, esta versión tiene algo para todo el mundo. Como siempre, nos gustaría recordarte que QGIS es un proyecto de código abierto y si puedes, considera apoyar nuestro trabajo a través de donaciones, patrocinios o contribuciones a la documentación del código, sitio web y demás.    

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, evaluadores y a todas las personas que ofrecen su tiempo y esfuerzo (o financian a las personas para que lo hagan). Desde la comunidad QGIS, ¡esperamos que disfrutes de esta versión! Si deseas donar tiempo, dinero o involucrarse de alguna manera para hacer que QGIS sea más increíble, ¡Ve a qgis.org y echa una mano!

QGIS es sustentado por donantes y patrocinadores. Puedes ver una lista actual de donantes que han hecho contribuciones financieras grandes y pequeñas para el proyecto en nuestra lista de donantes. Si deseas convertirse en patrocinador oficial del proyecto, visita nuestra página de patrocinio para obtener más información. El patrocinio de QGIS nos ayuda a financiar nuestras reuniones de desarrolladores cada seis meses, mantener la infraestructura del proyecto y financiar los esfuerzos de corrección de bugs. A continuación se proporciona una lista completa de los patrocinadores actuales. ¡Muchas gracias a todos nuestros patrocinadores!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## Herramientas de mapa
### Funcionalidad: QgsMapLayerAction: agrega una entrada  al menú de contexto de la leyenda para acciones de selección
Una nueva entrada (Acciones sobre selección) se agrega al menú de contexto del árbol de capas. Se muestra solo cuando es requerido (la capa tiene una selección y se pueden ejecutar acciones sobre dicha capa)

![imageQ1](https://user-images.githubusercontent.com/127259/74035907-7f334580-49bb-11ea-8d2d-b99eaa10aa89.png)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: mostrar la distancia desde la osición fijada en el GPS hasta la posición actual del cursor
Cuando se conecta un dispositivo GPS, cada vez que el usuario mueve el cursor sobre el lienzo, se muestra un mensaje en la barra de estado con la distancia y el rumbo desde el cursor hasta la posición fijada del GPS

La configuración de distancia y comportamiento del proyecto se respetan.

![Peek 2020-01-14 16-06](https://user-images.githubusercontent.com/1829991/72318360-cd6c6600-36e7-11ea-9f2d-9a47d8772623.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad:: Agregar opción de proyecto para formatos de ángulos
La pestaña de configuración de herramientas de mapa contiene una nueva opción para controlar el formato predeterminado a usar para mostrar angulos de orientación en los nuevos proyectos craedos. Cada vez que un nuevo proyecto se crea, hereda esta configuración predeterminada.

El diálogo de propiedades del proyecto también tiene una nueva opción para el formato de ángulos específico del proyecto 

The intention is that whenever angular bearings are shown in QGIS, they will be formatted using the current project\'s bearing format settings.

También incluye muchas adiciones a la API  proporcionando un lugar estable y fácil para configurar y recuperar configuraciones como el formato de ángulos.

![Peek 2020-01-09 11-08](https://user-images.githubusercontent.com/1829991/72029046-5fcbce80-32d0-11ea-8571-0ae8fa8e3bb0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Interfaz de usuario
### Funcionalidad: Deseleccionar tablas cuando se agregan datos PostgreSQL después que el botón agregar es presionado.
Cuando se agrega datos PostgreSQL en el gestor de fuentes de datos; despues de presionar el botón agregar, QGIS debe deseleccionar las tablas previamente seleccionadas. 

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funcionalidad: Mostrar el angulo y la distancia total de desplazamiento en la barra de estado. 
We added the total pan distance and bearing in the status bar during canvas pan operations. Allows users to know exactly how far (and in what direction) they\'ve dragged the map.

![image5](images/entries/48c75d20d3805af3dad8c7faae3c3786a8f6fed0.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funcionalidad: nueva opción para configurar el formato de archivo predeterminado (qgs/qgz)
Esto agrega una nueva opción global para definir el formato de archivo de proyecto predeterminado. 

![imageQ2](https://user-images.githubusercontent.com/127259/72597971-2bc75d80-390f-11ea-84af-7f2c25d5568a.png)

Esta funcionalidad fue financiada por la fundación GEM

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Corrige el cuadro de diálogo de atributos inválido al copiar a otra capa
It\'s possible to copy features from one layer to another. If there are the same fields in the destination layer, then the attributes for them are taken from the original feature. If not, the default value is taken. Otherwise, the new attribute is null.

Si la capa destino tiene restricciones en los campos, estas deben respetarse ahora o ignoradas a propósito. Pero no copiar valores inválidos como solía hacer.

That\'s why now the attributes are checked against the constraints. And for all the invalid features a dialog pops up.

![copydialog2](https://user-images.githubusercontent.com/28384354/72243171-7e410b00-35eb-11ea-8903-11bd56cd9da6.gif)

Y al pegar un solo objeto, las opciones se reducen:

![copypastesingle](https://user-images.githubusercontent.com/28384354/72243125-5ce01f00-35eb-11ea-897e-0bccdcf083d7.png)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Funcionalidad: permite soltar una capa de mapa del árbol de capas en un control de selección de proyección
\...to set the projection to match that layer. Just a little timesaving shortcut!

![Peek 2019-12-20 11-27](https://user-images.githubusercontent.com/1829991/71222288-b7070080-231b-11ea-89f4-af856dece4c3.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Calculadora ráster de Procesos: agregar botones faltantes y validar
Agrega botones faltantes para ABS/MIN/MAX y valida la expresión

![image10](https://user-images.githubusercontent.com/142164/68952420-1bd0b780-07c0-11ea-88d1-2ad0a8b5591e.gif)

Esta funcionalidad fue desarrollada por Alessandro Pasotti
## Simbología
### Funcionalidad: Animación de trazas vectoriales y líneas de flujo para la capa de malla
Mesh vector renderer now can visualize streamlines and particles on top of existing \"arrow\" mode.

![image11](images/entries/5b772e74d433e766b50023cd107aad9cb1d68de6.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: enmascarado selectivo
A new advanced rendering feature has been added: selective masking. It allows the definition of \'masks\' areas around labels or point markers. These masks will \"un-draw\" only some symbol layers of other layers underneath, chosen by the user.

![image12](https://user-images.githubusercontent.com/1618556/62111873-d68c8680-b2b1-11e9-8cd4-19077f99a8ff.gif)

This feature was funded by [QGIS.CH and others through a cofunding campaign](https://oslandia.com/en/offre-qgis/selective-masking/)

This feature was developed by [Hugo Mercier (Oslandia)](https://www.oslandia.com)
### Funcionalidad: Cuando la rotación de grados decimales falla al evaluarse, recurrir a valor estático
La leyenda ya también funciona bien con la rotación definida por datos. QGIS ya podía aplicar rotación definida por datos a símbolos y capas de símbolos individuales, pero esto resultaba en una leyenda rota. La rotación de símbolos (y partes de símbolos definidas en las capas de símbolos) en la leyenda ahora se puede controlar cambiando los valores predeterminados junto a las propiedades definidas de datos.

El comportamiento anterior era volver siempre a 0 en caso de que unaexpresión fallara. Lo que dificultaba la creación de una leyenda correcta en algunos casos.

e.g. si tuviera dos capas de símbolos con las siguientes expresiones para su rotación

    "orientation"
    
Y

    90 + "orientation"
    
que serían dos capas de símbolos ortogonales (por ejemplo, indicar un ángulo recto), rotados usando un campo de orientación.

Ahora en la leyenda (y la vista previa del símbolo), ambas capas se mostrarían con una rotación de 0, porque no hay una característica asociada con un campo de orientación.

El nuevo comportamiento es recurrir a los valores estáticos configurados, lo que hace que sea muy intuitivo configurar la leyenda para estos casos.

**Antes**

![Peek 2019-12-08 09-18](https://user-images.githubusercontent.com/588407/70386652-acec1600-199b-11ea-8457-f9dd54c84272.gif)

**Después**

![Peek 2019-12-08 09-16](https://user-images.githubusercontent.com/588407/70386651-acec1600-199b-11ea-8ce2-27798aec38a7.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Prestación: Añadir conteo de puntos basado en la densidad para el relleno del marcador aleatorio
Esta prestación añade un método de recuento de puntos basado en densidad al nuevo relleno de marcador aleatorio.

![image15](https://user-images.githubusercontent.com/1728657/67672096-c2881c00-f9a9-11e9-8394-d73505d05309.gif)

Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: Relleno con marcador aleatorio de capas de tipo símbolo
This feature adds a new fill symbol layer type \"Random marker fill\". It allows polygon features to be rendered using a marker symbol placed at random locations within the polygon boundary.

Las opciones incluyen:
- número de símbolos marcadores a representar para el polígono
- si los marcadores representados cerca de los bordes de los polígonos deben cortar al límite del polígono o no
- una preselección de números aleatorios opcional, para proporcionar una ubicación consecuente de los marcadores cada vez que se actualizan los mapas (también permite que la ubicación aleatoria funcione bien con el servidor QGIS y la representación basada en mosaicos)

![image16](https://user-images.githubusercontent.com/1829991/66734145-51267480-eea5-11e9-9e0a-3bfeee15f976.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Añadir opción de establecer color de representación para pixels sin datos en capas ráster
Allows raster nodata pixels to be colored in a specific (non-transparent) color. Designed to match the \"Display background value\" option from ArcMap.

![image17](https://user-images.githubusercontent.com/1728657/64846100-f4c9fe00-d635-11e9-8acb-367ad2dd2915.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Etiquetando
### Prestación: Permitir eliminar la posición de etiqueta personalizada
Agregamos una nueva posible opción para eliminar la posición de la etiqueta personalizada presionando la tecla DEL mientras se mueve la etiqueta.

![image18](images/entries/e8064c56705b7a74befa85e8a34e7b7311626f0a.gif)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch)
## Diagramas
### Prestación: Soporte de efectos de pintura para el representador de diagramas
this new feature allows for diagrams to use paint effects, including drop shadows, outer glows, etc\...

![image19](images/entries/37d0a22707eca463e5aba7c0a349b2d8029fb823.gif)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New diagram type \"stacked bars\"
With this new feature users will have possibility to create stacks bars of varying colors for each attribute on top of each other vertically or horizontally. Designed to match the \"Stacked\" chart renderer option available in ArcGIS.

![image20](images/entries/933c25cf0cd8997e177eee809b4fa26462b6d8c2.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: opción de espaciado para diagramas de gráfico de barras para capa vectorial
Permite el espacio controlado por el usuario entre cada barra del gráfico.

![image21](images/entries/7906ea6467d1d5ea19550ce1711fcc277df709a0.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nueva opción para controlar dirección angular en diagrama de tarta
Esta prestación permite controlar si las secciones se representan en sentido horario o antihorario.

![image22](images/entries/c2484d36648c335d16d1e3a45ac1a132ca2baafe.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Representación
### Prestación: Botones Reproducir/Detener para la Reproducción de Capa de Malla
It is possible to switch the timeframes of mesh layer\'s datasets by play/stop button. The playback setting could be adjusted in the time setting dialog.

![image23](images/entries/4799685965addef6ca2c788d82eea77e67e2f1f3.webp)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
### Prestación: Remuestreo al Vuelo de Datos Definidos en Caras a Vertices (Capa de Malla)
Para los conjuntos de datos definidos en caras, se puede elegir interpolar datos a vértices con el método de promedio del vecino mas cercano. Cuando no se elige ningún método de interpolación de datos, cada píxel en una sola cara tiene un único valor/color. Con los datos sobre los vértices, la representación de cada píxel se interpola a partir de los valores de los vértices, lo que hace que las figuras sean más suaves.

Use el panel de estilo de contornos de malla para cambiar entre los métodos de interpolación de datos.

![image24](images/entries/c9c38ee8c59693b2971ab6269db22681a61002a1.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: soporte para malla de referencia temporal
Para varios tipos de conjuntos de datos, por ejemplo GRIB y NetCDF, el tiempo de referencia en el cuadro de diálogo de configuración de tiempo QGIS se rellena previamente a partir de los datos sin procesar y no es necesario configurarlo manualmente. También corregimos varios errores relacionados con el análisis temporal, por lo que en QGIS 3.12 debería ser posible formatear y mostrar su tiempo en planos/animaciones de la manera adecuada:
- Si hay una referencia temporal válida provista con grupos de conjuntos de datos, esta referencia temporal se usa para mostrar el tiempo (usando el tiempo absoluto).
- Si no se proporciona el tiempo de referencia, el tiempo se muestra utilizando el tiempo relativo y el usuario puede establecer una referencia de tiempo para mostrar el tiempo absoluto.
- Cuando no se proporciona ninguna referencia de tiempo, la predeterminada es la fecha actual + hora establecida con 00:00:00.

Se agrega un botón para recargar el tiempo de referencia proporcionado con los grupos de conjuntos de datos si es necesario.

También agrega una nueva prestación para permitir al usuario configurar la unidad de tiempo del proveedor con un cuadro combinado si esta unidad de tiempo es diferente de las horas.

![imageQ3](https://user-images.githubusercontent.com/7416892/70955568-bb939680-2047-11ea-9857-8aba122e43dd.png)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Objetos 3D
### Prestación: Renderizador de terreno de capa con malla 3D
Es posible renderizar la capa malla en la vista 3D como terreno.

El usuario puede elegir habilitar/deshabilitar triángulos suaves y estructuras alámbricas. Es posible elegir el ancho de línea y el color de línea de la estructura de alambres, cambiar la escala vertical y elegir el estilo de la representación (color único o sombreado de rampa de color).

Hay dos entradas para renderizar la capa malla en la vista 3D:
- Selecciona la malla como terreno en el control de configuración
- activar la vista 3D en las propiedades de capa.

El usuario puede elegir estos ajustes:
- activar/desactivar triángulos suavizados
- activar/desactivar estructura alámbrica
- elegir el grosor de línea y el color de la estructura alámbrica
- cambiar la escala vertical
- elegir el estilo de renderizado: color único o sombreado de rampa de color
- ajustes del sombreado de rampa de color como para una capa ráster

Por ahora, la malla puede ser renderizada como un TIN pero el renderizado de conjuntos no es soportado. Sin embargo, la infraestructura es adaptada para una futura ronda de trabajo.

![mesh3dsettings](https://user-images.githubusercontent.com/7416892/72482783-41d10300-37d5-11ea-9a21-8f906abcb14a.gif)

![image27](images/entries/f19c25acbd1eb462cdc0365d3af3f706c1b4d2fe.gif)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: Cargar capa vectorial 3D en fondo + mosaico
Esto agrega soporte para la carga en segundo plano de datos de capas vectoriales en vistas de mapa 3D. Hasta ahora, la carga (y el teselado) congelarían completamente la GUI; esto podría llevar muchos segundos dependiendo de la complejidad de los datos de entrada.

El renderizador de capa vectorial básico y el renderizador basado en reglas se convirtieron para usar QgsChunkedEntity, que ya se usa para renderizar el terreno. Hay dos mejoras más además del desbloqueo de la GUI:
- El proceso de carga es multiproceso en lugar de usar un solo núcleo
- la carga se realiza en mosaicos, por lo que es posible ver los mosaicos con datos 3D apareciendo mientras otros datos aún se están cargando

There is a new configuration option in the 3D tab of vector layers - it determines how deep the quadtree will be. For example, one zoom level means there will be a single tile for the whole layer. Three zoom levels means there will be 16 tiles at the leaf level (every extra zoom level multiplies that by 4, so I have limited GUI to max. 8 levels which gives \~16K tiles which is already a lot).

How a vector layer\'s tiling quadtree gets populated: all internal tree nodes are empty and thus the 3D map scene tries to immediately replace them with their children - this goes until leaf nodes are reached. Only nodes at the leaf level currently hold any data. This may change in the future when we introduce more elaborate strategies - for example, internal nodes may contain a small percentage of features of the child nodes (this would allow us to show something while zoomed out a lot, not requiring to load all data).

For debugging purposes, there is also a new configuration option \"show bounding boxes\". This allows you to see the bounding box of each tile (especially useful if there are some issues with tiles not showing up when they should).

Esta prestación fue financiada mediante subvenciones de QGIS.org.

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
## Diseño de impresión
### Prestación: permitir arrastrar y soltar imágenes en diseños de mapa
Esta nueva característica permite al usuario, p.ej. arrastrar un svg desde el explorador de archivos al diseño para crear un nuevo elemento de imagen que contenga esa imagen svg.

![image28](images/entries/21b9f2fba7bf1576f794410fd238ef7553154d53.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevo tipo de elemento de diseño: tablas fijas creadas manualmente
Este nuevo tipo de elemento permite la creación de tablas con contenidos ingresados manualmente por los usuarios (es decir, estilo de hoja de cálculo) para que los usuarios puedan crear tablas completamente personalizadas. Admite el control del contenido personalizado de las celdas, los colores de primer plano y de fondo (y pronto, las alturas predeterminadas de filas y columnas). Se ha agregado un nuevo cuadro de diálogo de diseño de tabla que permite la personalización de estas tablas.

![image29](images/entries/95cfa9a8c44fb0141474d80e4b3a5e7f98352e70.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Agregar control de usuario sobre los formatos numéricos de la barra de escala
Ahora tiene la opción de controlar el formato numérico utilizado por una barra de escala de diseño.

You can manage all the formatting properties for the numbers in scale bars, including whether they want a thousand separator, decimal places, scientific notation, etc. Very useful in the case of making maps for audiences outside of the current QGIS locale, or when you\'d just prefer to vary the style from the locale defaults (e.g. adding thousands separators when the locale default is to hide them).

![image30](images/entries/99c97baaee3e5930bca0cb63db1391b6fd49b34f.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Permitir que las tablas de atributos de diseño se diseñen utilizando los colores de primer plano y de fondo de estilos condicionales coincidentes
When the new \"Apply layer conditional styling colors\" option is enabled in the layout attribute table settings, any conditional styling rules present in the layer will be applied inside the layout attribute table (foreground and background colors only, for now!).

![image31](images/entries/baded0d05539439d58e6df5a8f24157293cf8022.gif)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Añadir cuadro de búsqueda al administrador de plantillas
Permite filtrar la lista de plantillas en un proyecto por nombre, útil cuando un proyecto tiene muchos diseños ..!

![image32](images/entries/fb510c6c079d55dab2dd22f02c7c5355b317ac47.webp)

Esta prestación fue desarrollada por Nyall Dawson
## Expresiones
### Prestación: Etiquetas de búsqueda para Funciones
Tags on static expression functions to make them more retrievable. Functions like array_to_string are listed when the user enters \"split\" or \"convert\" or - like before - a part of the function name.

![image33](images/entries/689a669fe84721d7574aba7e595e019a9936f0b9.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Prestación: Lista referenciada de Valores de Capa
Cuando un campo es RelationReference, ValueRelation y ValueMap, existe la posibilidad no solo de mostrar los valores de la capa actual sino también los valores posibles en la referenced layer / configured possibilities.

![image34](images/entries/394c762c41e71764d9be397b718252eddb2dbd3e.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Prestación: Nuevas expresiones
- `is_empty(geom)`, check if a geometry is empty (geometry that contain no coordinates)
- `is_empty_or_null(geom)`, check if a geometry is empty or NULL (does not have geometry)
- `hash`, cryptographic hashes functions using [QCryptographicHash](https://doc.qt.io/qt-5/qcryptographichash.html). Use case is the same as PgCrypto but in client side for all supported format.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Feature: New algorithm \"Rename table field\"
Toma una capa de entrada, un campo existente y un nuevo nombre para el campo, y genera una nueva capa con el campo seleccionado renombrado.

While this result could also be achieved with the Refactor Fields algorithm, Refactor Fields isn\'t particularly model friendly. It relies on a constant, fixed table structure, and can\'t adapt to input tables with different field structures.

Por el contrario, este algoritmo simple Rename Field se adapta muy bien para el uso del modelo, ya que opera solo en un campo y deja todos los demás campos intactos.

![image35](images/entries/c01edc8ee51dff2b4df8f825e0dcaf27940e4aba.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Expresiones almacenadas
- Almacenar expresiones de usuario
- Icono/acción limpiar editor

![expression-storage-opt](https://user-images.githubusercontent.com/142164/70983414-faae0000-20b8-11ea-9f25-14b338d4c680.gif)

See also QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/135>

This feature was funded by [Salvatore Fiandaca](https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Prestación: Lista referenciada de valores de capa en el Constructor de Expresiones
Cuando un campo es RelationReference, ValueRelation y ValueMap, existe la posibilidad no solo de mostrar los valores de la capa actual sino también los valores posibles en la referenced layer / configured possibilities.

*age* is a ValueMap, *species* is a ValueRelation and *island_id* is a RelationReference

![uniquevalues](https://user-images.githubusercontent.com/28384354/70978774-ab63d180-20b0-11ea-901b-d51d44fa8fa4.gif)

En el ejemplo tenemos las personas:
- *George (en Cuba, en sus veinte, humano) Paul (en Vietnam, en sus treinta, humano) Ringo (en Venezuela, en sus cuarenta, gato) John (también en Vietnam, en sus cuarenta, mesa)*
- Y las entradas en la capa de país son *URSS, Cuba, Vietnam, Birmania, Venezuela, Corea del Norte*

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Prestación: Añadir funciones de expresión para convertir a/desde wkb
- `geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → a point geometry object` Returns a geometry created from a Well-Known Binary (WKB) representation.
- `geom_to_wkb( $geometry ) → binary blob containing a geometry object` Returns the Well-Known Binary (WKB) representation of a geometry as a binary blob.

Adds geom_from_wkb and geom_to_wkb, which mirror the existing geom_from_wkt/geom_to_wkt functions but for WKB representations of geometries.

Since QGIS 3.6 we\'ve had good support for binary blob values in expressions and field values, so adding these functions allows users to work with binary blob fields containing WKB representations of geometries (e.g. with a geometry generator showing the encoded geometries)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: is_valid expression
`is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → true` Returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules

Add an is_valid function to the expressions, which reuses GEOS is valid and returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules.

Esta prestación fue desarrollada por Pete King
### Feature: Add datetime_from_epoch (MSec from epoch) expression function
`datetime_from_epoch(1483225200000) → 2017-01-01T00:00:00` Returns a datetime whose date and time are the number of milliseconds, msecs, that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (Qt.UTC), and converted to Qt.LocalTime.

Esta funcionalidad fue desarrollada por Richard Duivenvoorde
### Prestación: función de expresión rotate()
`rotate($geometry, 45, make_point(4, 5)) → geometry rotated 45 degrees clockwise around the (4, 5) point` Returns a rotated version of a geometry. Calculations are in the Spatial Reference System of this geometry.

Esta prestación fue desarrollada por Raymond Nijssen, Nyall Dawson
### Prestación: Posibilidad de preseleccionar funciones aleatorias
- `rand(10, 80, 1) → 30` Returns a random integer within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.
- `randf(10, 80, 1) → 19.37136508087729` Returns a random float within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.

This feature adds an optional seed parameter to rand() and randf() functions This is very useful if you want the result to be deterministic, for instance to assign random but fixed colors to features. Using color_hsb(rand(0,360,\$id),50,50) for instance yields always the same color for the same feature. We also improves the rand() function, which didn\'t work for high values (over 32000) by using Qt\'s QRandomGenerator instead of qrand (which it seems was deprecated in Qt 5.11).

Esta prestación fue desarrollada por olivierdalang
### Feature: Language support for format_date() and to\_{date,datetime,time}()
- `format_date('2012-05-15','d MMMM yyyy','fr') → '15 mai 2012'`
- `format_date('2012-05-15','d MMMM yyyy','it') → '15 maggio 2012'`
- `format_date('2012-05-15','d MMMM yyyy','en') → '15 May 2012'` Formats a date type or string into a custom string format. Uses Qt date/time format strings. See QDateTime::toString.

By default, those expression use the application\'s locale. The addition of an optional language parameter allows handling of dates that wouldn\'t match that default locale (say for e.g. an English system running QGIS trying to transform a French-formatted string into a date object).

Esta prestación fue desarrollada por Mathieu Pellerin
## Digitalizando
### Prestación: Editar Atributos Inválidos al Copiar/Pegar a otra capa
En las funciones de copiar y pegar de una capa a otra, en caso de que haya restricciones (por ejemplo, no nulas) en la capa de destino, que no se pueden cumplir automáticamente con los valores predeterminados, aparece un cuadro de diálogo para corregir los atributos no válidos o ignorar las restricciones propuestas.

![image38](images/entries/5bd43dd39955e37ace130038b968550c6fa260c5.gif)

This feature was funded by [Amt für Wald und Wild Zug](https://www.zg.ch/behoerden/direktion-des-innern/wald-und-wild)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Prestación: Ajustar paralelización de caché
In previous version of QGIS, the snapping index cache was built sequentially and you had to wait for all your layers to be indexed before starting edition. Thanks to the QGIS.org grant program, QGIS now builds the snapping index cache in parallel for each layer, so it speeds up the whole process. Snapping has also been relaxed, meaning that you don\'t have to wait for the cache to be complete, you can start editing and snapping information will appear as soon as they are ready.

![image39](images/entries/d77958db7175267448d9b94950532dee8b90145c.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Administración de datos
### Característica: Mejoras a Exportación DXF
Realizamos una renovación del proceso de exportación DXF. Esto solidifica el proceso de exportación y ofrece nuevas prestaciones.
- Estilos de geometrías son exportados y se utilizan bloques
- La coordenada Z de geometrías 3D son conservadas
- Las etiquetas se exportan con sus puntos de anclaje y se respetan los ajustes de alineación horizontal y vertical o cuadrante

The whole DXF export process has also been made ready for running in a thread. With this in place, it\'s now only one step away from being sent to the background, allow cancellation of an ongoing export process or being exposed as a processing algorithm.

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Widgets y Formularios
### Prestación: Crear entidad geométrica desde el editor de relaciones
We added the ability to add a new feature and digitize its geometry directly from within the relation editor widget. It\'s now easier to add a geometric feature related to your currently displayed parent feature.

![image40](images/entries/fe03aefab87464e54b70569e6d05ad09a1b8fae5.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Prestación: Mejorado del diálogo de selección de funciones
From the relation editor widget, you can link your currently displayed feature with existing features. The feature selection dialog allows you to choose these features. Thanks to the QWAT user group, feature selection is now shared with the canvas\' one so it is easy to find out and pick the feature you want to link. We have also added the ability to filter displayed features (selected ones, visible on map, matching an expression\...) reusing the same widgets already existing in attribute form.

![image41](images/entries/a65364e6a48857a8720643c41a3cb17461d9e16a.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: UX improvements in drag\'n\'drop form designer
The drag\'n\'drop form designer has received some nice UX improvements
- Las dos listas (campos disponibles y árbol de diseño) ahora están sincronizadas: cada vez que selecciona una entrada en una lista, el elemento coincidente se selecciona en la otra.
- Los cuadros de diálogo de configuración ocultos (bajo doble clic) se han llevado al panel derecho

![image42](images/entries/5f47cb6311a9bffef94128a703719d709deb995a.gif)

Esta prestación fue financiada por QGIS.org bugfixing

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
## Leyenda de capa
### Prestación: Soporte para mostrar gráficos de leyenda WMTS en el árbol de capas
Agregamos soporte para mostrar gráficos de leyenda WMTS directamente en el árbol de capas, como ya es el caso con los gráficos de leyenda WMS.

Ejemplo:

![imageQ4](https://user-images.githubusercontent.com/1298852/72462785-33351c80-37d2-11ea-98f2-ce0d5221e1f5.png)

Sample use case: <https://wmts10.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>

This feature was developed by [Sandro Mani](https://api.github.com/users/manisandro)
## Herramientas de análisis
### Prestación: Exportación suave de los contornos de la capa de malla
A new algorithm in QGIS's analysis library API to export directly contour lines and polygons is added. The method is not based on GDAL algorithms, but directly uses mesh layer triangular mesh interpolation methods. It is both fast and with smooth shapes, matching rendered images from QGIS. You can try the new processing algorithm in Crayfish processing toolbox.

![image44](images/entries/044ad55bfb4287026b4e002c46c8687093488d22.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: Soporte de conjuntos de datos definidos en caras en la Calculadora de Mallas de QGIS
Puede usar la calculadora de malla para todos los tipos de conjuntos de datos, ambos definidos en caras y vértices. Además, permite a los usuarios almacenar el resultado de la calculadora de mallas con un nombre o formato diferente. Esto permite, por ejemplo, trabajar con datos FLO-2D o HEC-RAS en la calculadora de malla QGIS

![image45](images/entries/044d52fe937887854583ecfdc551e73eafb94a41.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Procesado
### Prestación: Empaquetar nuevas capas en un GeoPackage existente
Mejoramos el algoritmo de procesamiento de *paquete de capas* existente para poder agregar nuevas capas a GeoPackages existentes. Todo lo que necesita hacer para hacer uso de esto es deshabilitar el parámetro OVERWRITE y especificar un GeoPackage existente.

![image46](images/entries/35d87f4826aad132de4a0b99ac7c775f6aa9b029.webp)

This feature was funded by [BikePlan](https://www.bikeplan.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Lógica Difusa - Fuzzfiy Raster (membresía lineal)
El algoritmo de ráster Fuzzify (pertenencia lineal) es una implementación nativa del algoritmo de lógica difusa. Transforma un ráster de entrada en un ráster difuso y, por lo tanto, asigna valores entre 0 y 1 después de una función de pertenencia de lógica lineal. El valor 0 implica la no pertenencia a conjunto difuso definido, un valor de 1 representa la pertenencia total. En medio, el grado de pertenencia de los valores ráster sigue una función de pertenencia lineal.

![image47](images/entries/bfb37d710293c252dae11b67b25bdc1431f13815.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Lógica Difusa - Fuzzfiy Raster (pertenencia de poder)
El algoritmo ráster Fuzzify (pertenencia de poder) es una implementación nativa de un algoritmo de lógica dispersa. Transforma un ráster de entrada en un ráster difuso y, por lo tanto, asigna valores entre 0 y 1 después de una función de pertenencia difusa de potencia. El valor 0 implica la no pertenencia a conjunto difuso definido, un valor 1 representa la pertenencia total. En medio, el grado de pertenencia de los valores ráster sigue una función de pertenencia de poder.

![image48](images/entries/7a81ecd4414ee39b37e575863687615c88e9a856.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Lógica Difusa - Fuzzfiy Raster (pertenencia pequeña)
The Fuzzify raster (small membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'small\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'small\' membership function. The \'small\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image49](images/entries/2bef948a7b02bd26208ca98e9ddb243d46d104a6.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Lógica Difusa  Fuzzfiy Raster (pertenencia grande)
The Fuzzify raster (large membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'large\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'large\' membership function.The \'large\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image50](images/entries/10963d11812664a76d4fc3fac72777c34a08c767.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Lógica Difusa - Fuzzfiy Raster (pertenencia gaussiana)
The Fuzzify raster (gaussian membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'gaussian\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'gaussian\' membership function. The gaussian function is constructed using two user-defined input values which set the midpoint of the gaussian function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image51](images/entries/58068dc6518a0df20a39df69ea4175f7b196b049.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Lógica Difusa - Fuzzfiy Raster (pertenencia cerca)
The Fuzzify raster (near membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'near\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'near\' membership function. The near function is constructed using two user-defined input values which set the midpoint of the near function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image52](images/entries/a4873da4c5e782a14caaa02f279ef92ba5bf5a38.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Densificación de Puertos por algoritmo de recuento a C++
We ported the Densify by count algorithm to C++ in order to enhance it\'s speed when compared to the previous Python implementation. The new algorithm also exposes the count parameter as dynamic parameter so that it can be controlled by expressions or field values.

![image53](images/entries/680eb97f65d08de5541f4b1f5ac4425f45988cc2.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: Puntos de Puerto Aleatorio en algoritmo de extensón a C++
We ported the Random points in extent algorithm to C++. This boosts it\'s speed when comparing it to the previous Python implementation. The new algorithm also exposes an advanced parameter of maximum numbers of retrys for the algorithm when searching for randomly placed points that respect a certain distance between all points.

![image54](images/entries/c452431d9a2cd9f9f76869cf98e09e18bf2a81a4.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Prestación: algoritmo de densidad lineal
En esta versión, agregamos un algoritmo nativo para calcular la densidad de líneas basada en ráster. Este algoritmo calcula la densidad de línea en función de un radio de búsqueda y pesos de las líneas dentro del radio de búsqueda. El algoritmo fue portado para proporcionar más funcionalidad desde la extensión ArcGIS Spatial Analyst en QGIS.

![image55](images/entries/b28bbe3d5129ccc5dd61585dc1a9e31383a59c6f.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Feature: New algorithm \"Repair Shapefile\"
Agregamos un nuevo algoritmo que usa GDAL para reparar archivos shape que tienen un archivo .SHX roto o faltante.

![image56](images/entries/c3a6a174187284126ea0af289614505ab8c0c593.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add new algorithm \"Detect Dataset Changes\"
Este algoritmo compara dos capas vectoriales, y determina que entidades no han sido cambiadas, añadidas o borradas entre las dos. Está diseñado para comparar dos versiones diferentes del mismo conjunto de datos.

Al comparar entidades, las geometrías de entidades originales y revisadas se compararán entre sí. Dependiendo de la configuración de Procedimiento de comparación de geometría, la comparación se realizará utilizando una comparación exacta (donde las geometrías deben ser una coincidencia exacta entre sí, incluido el orden y el recuento de vértices) o solo una comparación topológica (donde el área de geometrías se considera igual si todos los bordes de sus componentes se superponen (por ejemplo, las líneas con las mismas ubicaciones de vértice pero en dirección opuesta se considerarán iguales por este método). Si se selecciona la comparación topológica, no se compararán los valores z o m presentes en las geometrías.

Por defecto, el algoritmo compara todos los atributos de las características originales y revisadas. Si se cambia el parámetro Atributos a considerar para la coincidencia, solo se compararán los atributos seleccionados (por ejemplo, permitiendo a los usuarios ignorar una marca de tiempo o un campo de ID que se espera que cambie entre las revisiones).

Si alguna entidad en las capas originales o revisadas no tiene una geometría asociada, entonces se debe tener cuidado para garantizar que estas entidades tengan un conjunto único de atributos seleccionados para la comparación. Si no se cumple esta condición, se generarán advertencias y las salidas resultantes pueden ser engañosas.

El algoritmo genera tres capas, una que contiene todas las entidades que se consideran sin cambios entre las revisiones, una que contiene entidades eliminadas de la capa original que no están presentes en la capa revisada, y una que contiene entidades agregadas a la capa revisada que no están presentes en la capa original

![image57](images/entries/e38dcea12e1198341eb9f0bd45a33ebf7eda390b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: New mode to \"Join Attributes by Location\" to take attributes from matching feature with largest area of overlap only
This allows for easy polygon-\>polygon joins, where you expect there to be only a single matching feature and don\'t want to include features which are just touching or have just tiny sliver polygon overlaps.

![image58](images/entries/27b8e5e11deca93ffade31b86edc712ce918d179.webp)

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Agregar algoritmo de transformación afín nativo para vectores
Ofrece los siguientes beneficios sobre las versiones GRASS/SAGA:
- Soporte completo para valores z/m y manejo de geometrías curvas sin pérdida de curvas.
- Funciona con todos los tipos de datos nativos, sin necesidad de transformación de formato
- Admite parámetros dinámicos (datos definidos, por función) de traducción/escala/rotación
- Permite transformación y escalado de ambos valores Z y M( si están presentes)
- Soporta modo de edición in-situ

![image59](images/entries/1bfee3c2e208ecca6c235d96f83966ec808a0b1c.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: add gdal_viewshed algorithm
Expose new gdal_viewshed tool via Processing toolbox. Note: this requires GDAL \>= 3.1.

Esta funcionalidad fue desarrollada por Alexander Bruy
## Navegador
### Prestación: Personalización de los elementos mostrados en el navegador
Add customization of the items shown in browser to the Interface Customization dialog. User can hide some of the root items in the browser panel (e.g. Favourites, PostGIS provider, MSSQL, Oracle, Volumes, \...)

![image60](images/entries/5e8e9037420b83cd44d4e1994d4119e4ae92c8aa.webp)

This feature was funded by [Limerick City and County Council](https://www.limerick.ie/council)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: mostrar archivos html en el panel de navegador
Esta prestación permite mostrar y abrir archivos .htm(l) desde el panel del navegador. A menudo se usan para documentar archivos de datos o proyectos de mapeo.

![image61](images/entries/0db8930d20ca6f2fbf5b29593afdcf59e1af8d1e.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Show \"Open Document\...\" action in browser
El click derecho en ciertos archivos del navegador, permite que se abran con la aplicación externa predeterminada para ese tipo de archivo

P.Ej. Los PDF se abrirán con el visor de PDF externo predeterminado.

Works with PDF, ODS, XLS(X), CSV, TXT, PNG, JPEG, TIFF, SVG (other types will likely need more work, since they aren\'t currently shown in the browser).

![image62](images/entries/447f201d2342a64912bbef1e1d0aa3ebb8963ae4.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Permitir la personalización de los elementos mostrados en el navegador
You can now customize items shown in the browser. User can decide (in the Interface Customization dialog) to hide some of the root items in the browser panel (e.g. Favourites, or POSTGIS provider, \...)

![Screenshot 2020-01-09 at 09 17 05](https://user-images.githubusercontent.com/804608/72050388-466f5600-32c1-11ea-94f5-092cc8471243.png)

Esta prestación fue financiada por Limerick City and County Council

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Prestación: Añadir la acción refrescar a servicios OGC
Ahora puede actualizar los servicios OGC en el navegador. A continuación se muestra una captura de pantalla que muestra un ejemplo de cómo funciona esta función en conexiones WMS/WMTS:

![OGCrefreshonaction](https://user-images.githubusercontent.com/2663775/71974919-cfd04b00-3223-11ea-834d-ff016c70a8c6.gif)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
## Proveedores de datos
### Prestación: Cambiado el icono de colección de capas WMTS
Este era un cambio del icono utilizado para el elemento de colección de capas WMTS, se utilizó un esquema de base de datos en lugar de un icono relacionado con WMTS. Ahora se usa un icono general de WMS.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Prestación: Se agregó la propiedad de metadatos URL en la pestaña de metadatos de capa para los servicios WMS/WMTS y WCS
This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Prestación: Obtener y mostrar metadatos de dimensiones para metadatos de capa WMS
![image65](images/entries/d058ac6b89a8d06169b06580843967ad26e1ef54.webp)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Prestación: Se agregó acción de actualización a las entradas de servicios OGC
![image66](images/entries/7ce331ee78be7f8b0693c653ecc58916d70a1a92.gif)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Prestación: Mallas apiladas 3d
MDAL y QGIS ahora admiten mallas apiladas en 3D, particularmente para el formato TUFLOW-FV. Para esta versión, debe elegir el método de promedio apropiado en la interfaz QGIS y puede examinar los datos de manera similar a cualquier otro conjunto de datos 2D.

![image67](images/entries/dc3d85153d9bcecdf7ebbc6433c7cb40319e00dd.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: Solución de numerosos problemas de codificación de archivos shape
Esto corrige el manejo (¿roto por diseño?) de la codificación Shapefile, que ha sido un problema continuo durante años en QGIS.

Ver discusión en
- [#21264](https://github.com/qgis/QGIS/issues/21264)
- <http://osgeo-org.1560.x6.nabble.com/Shapefile-with-file-cpg-codepage-td5275106.html>
- <http://osgeo-org.1560.x6.nabble.com/QGIS-ignore-the-cpg-files-when-loading-shapefiles-td5348021.html>

(+ otros!)

The situation was that we had two different code paths for handling GDAL side attribute decoding OR QGIS side decoding. Unfortunately, they are both incompatible with each other, and due to GDAL API for this, we can\'t unify the two approaches. (More technical detail in the commit log message!)

Entonces, ahora nosotros/as:
- always do the decoding on QGIS\' side. This allows users to manually override a shapefile\'s declared encoding because they are often incorrect!
- use a port of GDAL\'s shapefile detection logic (it\'s not exposed in GDAL API, so I had to re-implement it here) so that we default to reading shapefiles by respecting the embedded encoding information (via CPG files or DBF LDID information)
- Completely remove the confusing/broken \"Ignore shapefile encoding declaration\" option, as it\'s no longer required \-- users are ALWAYS able to manually change the encoding of shapefiles layers if needed
- Always show users the detected embedded encoding in the layer properties, instead of always showing \"UTF-8\" when the embedded encoding information is used

This should give the best of both worlds \-- a nice default behavior resulting in shapefiles being read with the correct encoding, whilst still allowing users to override this on a layer-by-layer basis as needed.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: soporte de edición de tipo de curva Oracle
En versiones anteriores de QGIS, no era posible editar algunos tipos de geometría provenientes de una base de datos Oracle. Luego hemos agregado soporte de edición para los siguientes tipos de geometría:
- CircularString(Z)
- CompoundCurve(Z)
- MultiCurve(Z)
- CurvePolygon(Z)
- MultiSurface(Z)

Esta prestación fue financiada por Lille Metropole

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Prestación: Soporte de ráster MBTiles en el proveedor WMS
Esta prestación agrega compatibilidad con el mapa ráster en mosaico de MBTiles al proveedor WMS para que use las mismas rutas de código como WMTS o XYZ. Estas son las ventajas del enfoque a través del proveedor WMS:
- Escalar correctamente los mosaicos en una pantalla de alta resolución
- mejor aspecto cuando no se acerca a la resolución nativa de los mosaicos. El proveedor WMS usa una escala suave mientras que GDAL usa el vecino más cercano de forma predeterminada.
- map tile showing up while rendering (with GDAL it\'s blank map until everything is loaded)
- posibilidad usar el widget de base deslizante de escala de mosaico
- más rápido - principalmente un efecto secundario de cargar menos mosaicos en una pantalla de alta resolución

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### Prestación: Proveedor de datos ráster PostGIS nativo
Esta es una implementación de un proveedor de datos ráster PostGIS en el núcleo QGIS. Las fichas se almacenan en caché en la memoria RAM.

Esta prestación fue financiada por Christmas Holidays Inc.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Prestación: Mostrar metadatos de dimensiones en los metadatos de capa WMS
![wms-ttimelayermetadataqgis](https://user-images.githubusercontent.com/2663775/71542497-37f77500-2978-11ea-854b-d9a9ca2d6c77.png)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
### Prestación: Otros métodos promedio de malla 3d
QGIS now includes numerous methods for averaging mesh layers (see [related QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158), and for a description of the methods see [TUFLOW documentation](https://fvwiki.tuflow.com/index.php?title=Depth_Averaging_Results).
- SingleLevelAverageMethod (arriba)
- SingleLevelAverageMethod (abajo)
- MultiLevelsFromTopAveragingMethod
- MultiLevelsFromBottomAveragingMethod
- SigmaAveragingMethod
- DepthAveragingMethod
- HeightAveragingMethod
- ElevationAveragingMethod

![Screenshot 2019-12-19 at 13 59 47](https://user-images.githubusercontent.com/804608/71175509-068bf480-2268-11ea-9d60-adad896912e2.png)

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Prestación: Proveedor de funciones OGC API
This new provider is a client-side implementation of the recently adopted [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) specification, previously known as WFS3. It is integrated within the graphical user interface of the WFS provider, and leverages its core mechanisms to offer background downloading of features, using paging, and a local cache of already downloaded features for a smoother interactive use of datasets.

![image70](images/entries/d74a13f520336e0c2e44469ee4e527188e2466de.webp)

This feature was funded by [Planet](https://planet.com)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com)
## Servidor de QGIS
### Prestación: Aplicación QGIS Development Server
**QGIS Development HTTP Server**

Esta es una pequeña aplicación de línea de comandos independiente que implementa un servidor de desarrollo HTTP mínimo para QGIS Server.

Puede ser útil al desarrollar y probar proyectos, módulos y complementos de QGIS Server sin requerir una pila completa de servidor web/FCGI.

![qgismapserver](https://user-images.githubusercontent.com/142164/73081781-84c36280-3ec8-11ea-9285-ab4c41e3082c.gif)
``` bash
Usage: qgis\_mapserver [options] [address:port]
QGIS Development Server

Options:
-h, --help Displays this help.
-v, --version Displays version information.
-l Sets log level (default: 0)
0: INFO
1: WARNING
2: CRITICAL
-p Path to a QGIS project file (*.qgs or* .qgz),
if specified it will override the query string MAP argument
and the QGIS\_PROJECT\_FILE environment variable

Arguments:
addressAndPort Listen to address and port (default: "localhost:8000")
address and port can also be specified with the environment
variables QGIS\_SERVER\_ADDRESS and QGIS\_SERVER\_PORT
```
Muestra saliente:

`bash QGIS Development Server listening on http://localhost:8000 CTRL+C to exit 127.0.0.1 [lun gen 20 15:16:41 2020] 5140 103ms "GET /wfs3/?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 3298 2ms "GET /wfs3/static/jsonFormatter.min.js HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1678 3ms "GET /wfs3/static/jsonFormatter.min.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1310 5ms "GET /wfs3/static/style.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:43 2020] 4285 13ms "GET /wfs3/collections?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200`

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files. Adds missing parameters to GetDxf request

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Prestación: Agregar soporte json a WMS GetLegendGraphic
This feature adds support for GetLegendGraphic responses encoded as JSON. It builds on previous work by \@pblottiere, who added QgsLegendRenderer::exportLegendToJson for that exact purpose.

Por ejemplo, una solicitud GetLegendGraphic con FORMAT = image/png produciendo la imagen

![image72](https://user-images.githubusercontent.com/76594/64876231-fbb13a80-d64e-11e9-83e5-120fb1bc0ea8.png)

producirá lo siguiente con FORMAT=application/json

La imagen del icono está codificada en base64 y se puede visualizar directamente en una página web.

Esta prestación fue desarrollada por Éric Lemoine
## Programabilidad
### Prestación: Exponer los métodos de digitalización de formas a QgisInterface
The actions to trigger the drawing tools were not exposed in the API, if you wanted to do an action for one of these tools, you had to recreate classes. So a call of the type `qgis.utils.iface.actionCircleCenterPoint().trigger()` simplifies programmability.

Esta prestación fue fundad por QWAT/QGEP group

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Correcciones Notables
### Prestación: Correción de errores por Stephen Knox
| Bug Title | URL issues (if reported) | URL PR or commit |----|----|----|----| | Allow editing of postgres JSON fields from Text Edit Widget | [#29361](https://github.com/qgis/QGIS/issues/29361) | [#30758](https://github.com/qgis/QGIS/pull/30758)

Esta prestación fue desarrollada por Stephen Knox
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| \"Recent\" Group do not appear when opening the \"Select by expression\" dialog | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) |
| QGISserver no puede encontrar shp; intenta abrir ruta absoluta en lugar de relativa | [#33200](https://github.com/qgis/QGIS/issues/33200) | [PR #33925](https://github.com/qgis/QGIS/pull/33925) | arriesgado |
| sin informar: enlace incorrecto en la página de elementos del servidor WFS3 (demasiadas barras) | no reportado | [PR #33926](https://github.com/qgis/QGIS/pull/33926) | arriesgado |
| Qgis escanea tablas ráster en conexión a postgis | [#33885](https://github.com/qgis/QGIS/issues/33885) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Ficha Información de propiedades de capa: problemas de formato | [#33862](https://github.com/qgis/QGIS/issues/33862) | [PR #33955](https://github.com/qgis/QGIS/pull/33955) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | trabaja para mí en el maestro actual |  |
| QgsVectorLayer readStyle no lee la visibilidad basada en escala | [#33840](https://github.com/qgis/QGIS/issues/33840) | [PR #33987](https://github.com/qgis/QGIS/pull/33987) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| La simbolización en categorías no funciona en columnas bigint en QGIS | [#33585](https://github.com/qgis/QGIS/issues/33585) | [PR #33992](https://github.com/qgis/QGIS/pull/33992) | [PR #34290](https://github.com/qgis/QGIS/pull/34290) |
| QGIS no puede aplicar el estilo de archivo a los rásteres | [#29427](https://github.com/qgis/QGIS/issues/29427) | sin cambios requeridos, pero todavía en investigación |  |
| la función copiar/pegar no funciona correctamente para MultilinestringZ | [#33977](https://github.com/qgis/QGIS/issues/33977) | trabaja para mí en el maestro actual |  |
| Editar formulario muestra y guarda valores predeterminados sin procesar de geopackage, spatialite o sqlite | [#33383](https://github.com/qgis/QGIS/issues/33383) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| Imposible desmarcar capas en el Panel de orden | [#33854](https://github.com/qgis/QGIS/issues/33854) | [PR #34015](https://github.com/qgis/QGIS/pull/34015) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| La columna de identidad PostgreSQL no es reconocida correctamente | [#29560](https://github.com/qgis/QGIS/issues/29560) | [PR #34017](https://github.com/qgis/QGIS/pull/34017) | [PR #34291](https://github.com/qgis/QGIS/pull/34291) |
| El proveedor Spatialite no reconoce las PKs de incremento automático cuando la definición de la tabla usa backticks | [#34085](https://github.com/qgis/QGIS/issues/34085) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| QGIS crash when I click on the button \"Manage Map Themes\" | [#33295](https://github.com/qgis/QGIS/issues/33295) | [PR #34090](https://github.com/qgis/QGIS/pull/34090) | [PR #34098](https://github.com/qgis/QGIS/pull/34098) |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | trabaja para mí en el maestro actual |  |
| QGIS 3.10.2 reemplaza 0 por NULL | [#34118](https://github.com/qgis/QGIS/issues/34118) | [PR #34152](https://github.com/qgis/QGIS/pull/34152) | [PR #34292](https://github.com/qgis/QGIS/pull/34292) |
| Representación inconsistente para valores NULL use/display | [#28643](https://github.com/qgis/QGIS/issues/28643) | [PR #34157](https://github.com/qgis/QGIS/pull/34157) | [PR #34293](https://github.com/qgis/QGIS/pull/34293) |
| DB Manager in 3.11 Master can\'t connect to PostGIS Enabled database | [#34132](https://github.com/qgis/QGIS/issues/34132) | [PR #34171](https://github.com/qgis/QGIS/pull/34171) | N/D |
| QGIS doesn\'t respect OGC guidelines for KVP parameters | [#34148](https://github.com/qgis/QGIS/issues/34148) | [PR #34175](https://github.com/qgis/QGIS/pull/34175) | [PR #34294](https://github.com/qgis/QGIS/pull/34294) |
| QGIS 3.10 can\'t find pkey of postgres views | [#34167](https://github.com/qgis/QGIS/issues/34167) | [PR #34179](https://github.com/qgis/QGIS/pull/34179) | [PR #34295](https://github.com/qgis/QGIS/pull/34295) |
| Al duplicar una capa reutilizable ignora los campos agregados | [#34134](https://github.com/qgis/QGIS/issues/34134) | [PR #34199](https://github.com/qgis/QGIS/pull/34199) | [PR #34203](https://github.com/qgis/QGIS/pull/34203) |
| El proyecto Maestro XML de QGIS es inválido | [#34218](https://github.com/qgis/QGIS/issues/34218) | [PR #34219](https://github.com/qgis/QGIS/pull/34219) | [PR #34297](https://github.com/qgis/QGIS/pull/34297) |
| El formato condicional de la fila completa formatea las filas completas incorrectas | [#34122](https://github.com/qgis/QGIS/issues/34122) | [PR #34305](https://github.com/qgis/QGIS/pull/34305) | [PR #34315](https://github.com/qgis/QGIS/pull/34315) |
| El formato condicional de la fila completa formatea las filas completas incorrectas | [#34259](https://github.com/qgis/QGIS/issues/34259) | [PR #34309](https://github.com/qgis/QGIS/pull/34309) | [PR #34512](https://github.com/qgis/QGIS/pull/34512) |
| Los campos se desplazan al importar una capa con un atributo FID en GeoPackage | [#32927](https://github.com/qgis/QGIS/issues/32927) | [PR #32934](https://github.com/qgis/QGIS/pull/32934) | N/D |
| \"split features\" of PostGIS layers become slow since 3.6 | [#34326](https://github.com/qgis/QGIS/issues/34326) | cerrado: no se puede reproducir con ninguno de los (varios) conjuntos de datos proporcionados |  |
| No se puede agregar/guardar más de 1 registro/entidad en una capa/tabla de Spatialite | [#34379](https://github.com/qgis/QGIS/issues/34379) | [PR #34423](https://github.com/qgis/QGIS/pull/34423) | [PR #34513](https://github.com/qgis/QGIS/pull/34513) |
| QGIS crashes when changing \"default value\" in layer property on a point scratch layer, after editing feature | [#34404](https://github.com/qgis/QGIS/issues/34404) | [PR #34428](https://github.com/qgis/QGIS/pull/34428) | [PR #34514](https://github.com/qgis/QGIS/pull/34514) |
| La calculadora ráster convierte una fila de píxeles en nodata | [#34435](https://github.com/qgis/QGIS/issues/34435) | [PR #34460](https://github.com/qgis/QGIS/pull/34460) | [PR #34511](https://github.com/qgis/QGIS/pull/34511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Funcionalidad: Bugs corregidos por Sandro Santilli
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| repository files modified by \'make check\' | [#25830](https://github.com/qgis/QGIS/issues/25830) |  |  |
| Runs of testsuite leaves hundreds of directories in \~/.local/share | [#34185](https://github.com/qgis/QGIS/issues/34185) | [Commit 96a7fb8](https://github.com/qgis/QGIS/commit/96a7fb8f5acf3a278919f88c7c5abc4d20b8b6c2) | N/D |
| Descarte el uso del constructor QgsCoordinateReferenceSystem en desuso | [PR #34186](https://github.com/qgis/QGIS/pull/34186) | [Commit b4fa419](https://github.com/qgis/QGIS/commit/b4fa419f7654ea7d1bce666b99f0534c415d8634) | N/D |
| Solo buscar pointcloud en su esquema de extensión instalado | [#33509](https://github.com/qgis/QGIS/issues/33509) | [Commit 1f44b29](https://github.com/qgis/QGIS/commit/1f44b29933bff3b8806bba75b761dd47b6c349c8) | N/D |
| QGIS 3.10 incapaz de cargar PostGIS-table en MacOS Catalina | [#32558](https://github.com/qgis/QGIS/issues/32558) | [Commit d15ce6b](https://github.com/qgis/QGIS/commit/d15ce6b4c30f9faed8b818c575d6b729192fa064) | [Commit a06b164](https://github.com/qgis/QGIS/commit/a06b164b5465ee7a0f8509e737d7c71ea7c166db) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Esta prestación fue desarrollada por Sandro Santilli
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fallo al aplicar filtro erróneo o capa OAFeat | [#33878](https://github.com/qgis/QGIS/issues/33878) | [PR #33927](https://github.com/qgis/QGIS/pull/33927) | [PR #33958](https://github.com/qgis/QGIS/pull/33958) |
| Proveedor Oracle: arreglar las advertencias del compilador | - | [PR #33930](https://github.com/qgis/QGIS/pull/33930) | - |
| No se puede importar el vector 3D en la fuente de datos Spatialite (funciona para GPKG) | [#33883](https://github.com/qgis/QGIS/issues/33883) | [PR #33938](https://github.com/qgis/QGIS/pull/33938) | [PR #33945](https://github.com/qgis/QGIS/pull/33945) |
| \[Oracle\] Fix MultiSurface with straight polygon | - | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | no factible |
| Geometries stored in Oracle table fail sdo_geom.validate_geometry_with_context(..) check | [#29085](https://github.com/qgis/QGIS/issues/29085) | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | no factible |
| QGIS WFS / OGC API -- Features not showing list typed attributes correctly | [#33758](https://github.com/qgis/QGIS/issues/33758) | [PR #33983](https://github.com/qgis/QGIS/pull/33983) | N/D |
| La layenda provoca un fallo | [#32913](https://github.com/qgis/QGIS/issues/32913) | [PR #34004](https://github.com/qgis/QGIS/pull/34004) | [PR #34063](https://github.com/qgis/QGIS/pull/34063) |
| Draw effects units setting doesn\'t persist | [#34089](https://github.com/qgis/QGIS/issues/34089) | [PR #34135](https://github.com/qgis/QGIS/pull/34135) | [PR #34151](https://github.com/qgis/QGIS/pull/34151) |
| Mala georreferenciación de OZI .map | [#34299](https://github.com/qgis/QGIS/issues/34299) | [GDAL commit](https://github.com/OSGeo/gdal/commit/7bedf61bbb8d8c331642b44f30c083abb43f4085) | - |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Prestación: Corrección de Errores por Alexander Bruy
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Eliminar texto detallado en los botones de la barra de herramientas de diseño | [#30161](https://github.com/qgis/QGIS/issues/30161) | [PR #33912](https://github.com/qgis/QGIS/pull/33912) |  |
| Imposibilidad de pegar una capa en un proyecto vacío | [#26710](https://github.com/qgis/QGIS/issues/26710) | [PR #33961](https://github.com/qgis/QGIS/pull/33961) | [PR #33965](https://github.com/qgis/QGIS/pull/33965) |
| Administrador BD: Diálogo Crear capa debe cerrarse o limpiado una vez que la nueva capa es generada | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #33910](https://github.com/qgis/QGIS/pull/33910) |  |
| Dos accesos directos predeterminados diferentes para el panel de estilo de capa (F7 vs Ctrl+3) | [#26696](https://github.com/qgis/QGIS/issues/26696) | [PR #33984](https://github.com/qgis/QGIS/pull/33984) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Funcionalidad: Corrección de errores por Paul Blottiere
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Compilación de correcciones en Arch Linux | No reportado | [PR #34110](https://github.com/qgis/QGIS/pull/34110) | [PR #34146](https://github.com/qgis/QGIS/pull/34146) |

| Move labels doesn\'t work with GPKG QGIS 3.4 | [#30408](https://github.com/qgis/QGIS/issues/30408) | Closed (works on master and 3.10) | - |

| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Feedback (works on master and 3.10) | - |

| Labels Buffer DD options do not have fields set and do not render in map canvas | [#28544](https://github.com/qgis/QGIS/issues/28544) | [PR #34153](https://github.com/qgis/QGIS/pull/34153) | risky |

| QGIS does not load embedded layers when opening projects | [#34060](https://github.com/qgis/QGIS/issues/34060) | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Embedded layers are duplicated after opening | Unreported | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Raise log level of server exception | [Discussed on qgis-developers list](https://lists.osgeo.org/pipermail/qgis-developer/2020-February/060108.html) | [PR #34256](https://github.com/qgis/QGIS/pull/34256) | [PR #34539](https://github.com/qgis/QGIS/pull/34539) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Prestación: Corrección de errores por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Se cuelga con relaciones | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34255](https://github.com/qgis/QGIS/pull/34255) | - |
| Se cuelga con relaciones V2 | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34403](https://github.com/qgis/QGIS/pull/34403) | Hecho |
| Se corrigieron las acciones de renderizado de mapa de capa en la tabla de atributos | No reportado | [PR #34266](https://github.com/qgis/QGIS/pull/34266) | Hecho |
| Mejoras de DnD (selecciones de sincronización) | [#28570](https://github.com/qgis/QGIS/issues/28570) | [PR #34411](https://github.com/qgis/QGIS/pull/34411) | TODO? |
| Mejoras de DnD (configuración del contenedor) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34433](https://github.com/qgis/QGIS/pull/34433) |  |
| Mejoras del DnD (no se oculta tras doble click) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34479](https://github.com/qgis/QGIS/pull/34479) |  |
| deshabilitada la exploración panorámica/escala automática en la tabla de atributos cuando muestra solo entidades visibles | [#34486](https://github.com/qgis/QGIS/issues/34486) | [PR #34493](https://github.com/qgis/QGIS/pull/34493) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| La herramienta de ajuste y vértice no funciona con algunas capas si el ajuste se habilitó cuando se cargó | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/D |
| Ajuste no es posible en nuevo proyecto con nueva capa | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplicado | - |
| La memoria caché de Vertex Tool no se actualiza tras los cambios en las entidades de línea | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Cerrado (fijado en 3.10 y maestro) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | PORHACER. |
| setFilterExpression y Filtro QGIS devuelven resultados distintos | [#33454](https://github.com/qgis/QGIS/issues/33454) | Cerrado (no es problema de QGIS) | - |
| Bloqueo al usar vistas de Oracle con clave primaria definida como número sin precisión | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | PORHACER. |
| El cliente WCS dejó de funcionar en un servicio específico de 2.18 a 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | PORHACER. |
| Cuelgue en prueba de relación de referencia | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | PORHACER. |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Prestación: Corrección de errores por Bertrand Rix
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| La herramienta de ajuste y vértice no funciona con algunas capas si el ajuste se habilitó cuando se cargó | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/D |
| Ajuste no es posible en nuevo proyecto con nueva capa | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplicado | - |
| La memoria caché de Vertex Tool no se actualiza tras los cambios en las entidades de línea | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Cerrado (fijado en 3.10 y maestro) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | PORHACER. |
| setFilterExpression y Filtro QGIS devuelven resultados distintos | [#33454](https://github.com/qgis/QGIS/issues/33454) | Cerrado (no es problema de QGIS) | - |
| Bloqueo al usar vistas de Oracle con clave primaria definida como número sin precisión | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | PORHACER. |
| El cliente WCS dejó de funcionar en un servicio específico de 2.18 a 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | PORHACER. |
| Cuelgue en prueba de relación de referencia | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | PORHACER. |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Cerrar el vértice de la línea al editar | [#32359](https://github.com/qgis/QGIS/issues/32359) | [PR #34217](https://github.com/qgis/QGIS/pull/34217) | [PR #34285](https://github.com/qgis/QGIS/pull/34285) |
| Corregido el enlace Grass en FreeBSD | reportado en FreeBSD ML | [PR #34088](https://github.com/qgis/QGIS/pull/34088) | [PR #34238](https://github.com/qgis/QGIS/pull/34238) |
| \[Regular Shape\] Allow undo click when digitizing new features | [#25597](https://github.com/qgis/QGIS/issues/25597) | [PR #34080](https://github.com/qgis/QGIS/pull/34080) | [PR #34302](https://github.com/qgis/QGIS/pull/34302) |
| Eliminar el vértice agregado con Agregar cadena circular | [#29688](https://github.com/qgis/QGIS/issues/29688) | [PR #34058](https://github.com/qgis/QGIS/pull/34058) | [PR #34301](https://github.com/qgis/QGIS/pull/34301) |
| Rubberband not working correctly with \"Shapes\" digtizing in rotated map window | [#33287](https://github.com/qgis/QGIS/issues/33287) | Duplicado |  |
| Digitalización: LineStringZ no hereda las coordenadas Z de los puntos si la línea comienza ajustando a un punto sin coordenada Z | [#33201](https://github.com/qgis/QGIS/issues/33201) | [PR #33642](https://github.com/qgis/QGIS/pull/33642) | [PR #33951](https://github.com/qgis/QGIS/pull/33951) |
| La prestación Dividir hace que QGIS 3.4.6 se cuelgue | [#33408](https://github.com/qgis/QGIS/issues/33408) | Ya corregida |  |
| Arreglar algoritmo de cuadro de límite mínimo orientado | [#33532](https://github.com/qgis/QGIS/issues/33532) | [PR #34334](https://github.com/qgis/QGIS/pull/34334) | [PR #34338](https://github.com/qgis/QGIS/pull/34338) |
| error con ángulo devuelto por orientedMinimumBoundingBox() | [#31371](https://github.com/qgis/QGIS/issues/31371) | Cerrado. Falta de retroalimentación |  |
| Fix build with txt2tags \>= 3.5 | directamente reportado por el responsable de qgis de FreeBSD | [PR #34377](https://github.com/qgis/QGIS/pull/34377) | [PR #34389](https://github.com/qgis/QGIS/pull/34389) |
| Se corrige el menú de identificación cuando se usa una expresión como nombre a presentar | no reportado | [PR #34361](https://github.com/qgis/QGIS/pull/34361) | [PR #34402](https://github.com/qgis/QGIS/pull/34402) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Prestación: Errores corregidos por Sebastien Peillet
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Prolongar línea no funciona en compoundCurvedZ capa  | [#32080](https://github.com/qgis/QGIS/issues/32080) | [PR #34055](https://github.com/qgis/QGIS/pull/34055) |  |
| Error de diseño de selección de atributo de entidad | [#29542](https://github.com/qgis/QGIS/issues/29542) | [PR #34359](https://github.com/qgis/QGIS/pull/34359) |  |
| Incapacidad de añadir una nueva entidad al unir dos tablas PostGIS | [#33148](https://github.com/qgis/QGIS/issues/33148) | [PR #34216](https://github.com/qgis/QGIS/pull/34216) |  |
| Copiar/Pegar de una capa a otra falla cuando la capa NO tiene restricciciones NULL y los grupos de transaccion están habilitados | [#29603](https://github.com/qgis/QGIS/issues/29603) | Already fixed by [PR #33688](https://github.com/qgis/QGIS/pull/33688) |  |
| QGIS se congela al crear nuevos archivos shape | [#32069](https://github.com/qgis/QGIS/issues/32069) | Ya corregida |  |
| Oracle: las tablas se enumeran una vez para Polígonos y una vez para MultiPolygons pero ambas muestran todas las geometrías | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) |  |
| ERROR: corrige el resultado de la capa no válida cuando la versión de Oracle es inferior a 12 | no reportado | [PR #34546](https://github.com/qgis/QGIS/pull/34546) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Arreglar la evaluación IN/NOT IN con números muy largos como cadenas | [#34314](https://github.com/qgis/QGIS/issues/34314) | [Commit 167e0de](https://github.com/qgis/QGIS/commit/167e0de65b0106a3c19181a2c415c2b0ba0da117) | [Commit aca059a](https://github.com/qgis/QGIS/commit/aca059a82021cb05b58664d3b0f2db751b8f37df) |
| \[processing\] Define Layer Projection tool should write .prj files using ESRI WKT1 format | [#34007](https://github.com/qgis/QGIS/issues/34007) | [Commit f41dd11e](https://github.com/qgis/QGIS/commit/f41dd11e9214b4d6ca5dcc31c6612a65d134ce83) | Remitido |
| Show \'unknown CRS\' in status bar instead of blank text when project is set to an unknown CRS | [#33458](https://github.com/qgis/QGIS/issues/33458) | [Commit c6319b2](https://github.com/qgis/QGIS/commit/c6319b263992c9d52646096d851cab6c674125ff) | Remitido |
| Don\'t force users to make a choice in the datum transform dialog | [#34234](https://github.com/qgis/QGIS/issues/34234) | [Commit 644a552](https://github.com/qgis/QGIS/commit/644a5525ec08a77b4c703a7066c94802bbfa1036) | Remitido |
| Se reparó el bloqueo al cambiar la fuente de datos ráster | [#34231](https://github.com/qgis/QGIS/issues/34231) | [Commit caf334e6](https://github.com/qgis/QGIS/commit/caf334e65b11f9ee1590f74fe395e97d92bbe699) | [Commit b4142c3](https://github.com/qgis/QGIS/commit/b4142c3832b9f14de97df08caf20a06dee12c02f) |
| Handle unit type \"m\" in custom WKT strings on proj 6 builds | [#34196](https://github.com/qgis/QGIS/issues/34196) | [Commit bb20cee](https://github.com/qgis/QGIS/commit/bb20cee00a931da46b830f0d1e9565d9863f9ba3) | [Commit 97c50f9](https://github.com/qgis/QGIS/commit/97c50f929fbbdd9b3eaef8f8bdf423f9daa3a163) |
| Mostrar todo CRS WKT para CRS personal en propiedades de capa | [#33862](https://github.com/qgis/QGIS/issues/33862) | [Commit 19d58bda](https://github.com/qgis/QGIS/commit/19d58bda08c202b29020a3e9c485fac80350fc79) | [Commit 2908227](https://github.com/qgis/QGIS/commit/2908227f91ccfde245a0a608b50b7758b3eba8dd) |
| \[processing\] Fix modeler draws lines to wrong output when connecting green output boxes | No reportado | [Commit 5ae9807](https://github.com/qgis/QGIS/commit/5ae9807303e909a504288d97a2efc4cc04a62670) | [Commit 528a45d](https://github.com/qgis/QGIS/commit/528a45d7453b7cbeb44450d5c81de80c8dd66611) |
| \[processing\] Fix Points Along Geometry handling of multipart geometries | [#34022](https://github.com/qgis/QGIS/issues/34022) | [Commit 3fb18a2](https://github.com/qgis/QGIS/commit/3fb18a2260cbc432e892a4dacbae0092a775ec9d) | [Commit ac3b446](https://github.com/qgis/QGIS/commit/ac3b446aead90d5ea5cab101807859e5ce6f1b44) |
| \[processing\] Fix QStringList values are not accepted as valid values for multi-field parameters | No reportado | [Commit abcb8d2](https://github.com/qgis/QGIS/commit/abcb8d20c66b3c235802b10e68d6abc34736e2c5) | [Commit d421313](https://github.com/qgis/QGIS/commit/d421313f05fd0e5a6974568eccd36c4213f41f8f) |
| \[processing\] Fix some field names are rejected in modeler for non-multi field parameters | No reportado | [Commit 9bcd980](https://github.com/qgis/QGIS/commit/9bcd98094c015265e7e94c55f248248e56c24e51) | N/A - 3.12 solo |
| Arreglar bloqueo en la información de entidad del servidor | No reportado | [Commit b3f37fde](https://github.com/qgis/QGIS/commit/b3f37fde9bc4785aebca29e6553d6c1de715f523) | Remitido |
| Se corrigió el desbordamiento asignando double max a float, min inválido | No reportado | [Commit 2b15e255](https://github.com/qgis/QGIS/commit/2b15e255eaf63f1d45b8e963fca7f9f9e4bf8d40) | N/A - 3.12 solo |
| Se corrigió el bloqueo en QgsGeometryDuplicateCheck debido al uso de la pila tras la liberación | No reportado | [Commit 195576e](https://github.com/qgis/QGIS/commit/195576e57f0aff064e962ce16b37533ab4924dce) | [Commit dc647bc](https://github.com/qgis/QGIS/commit/dc647bc56fb37207a75d55638926e7a2db75a8be) |
| Se corrigió el bloqueo en la destrucción de QgsPointLocator, si el objeto se destruye mientras se realiza la indexación en segundo plano | No reportado | [Commit 08adb23](https://github.com/qgis/QGIS/commit/08adb23a7ec284a2f84ecf7ac469fbe9004ab57e) | N/A - 3.12 solo |
| Corregido el fallo al leer ciertos archivos ráster remuestreados | [#33711](https://github.com/qgis/QGIS/issues/33711) | [Commit b2c5a45](https://github.com/qgis/QGIS/commit/b2c5a456fa4e9613ac33b8aaaed774ad3b7293a1) | [Commit 388277e](https://github.com/qgis/QGIS/commit/388277e642d99b93bd7f25197d6418b5dfb888bd) |
| Arreglar uso después de liberar en punto de símbolo 3d | No reportado | [Commit df7979c](https://github.com/qgis/QGIS/commit/df7979cf94c43352cd10db97c16075b8816ec6c4) | [Commit 7204de2](https://github.com/qgis/QGIS/commit/7204de27f3305146fbd6f8e32355c365030afc31) |
| Repara fugas en la capa de símbolo del generador de geometría | No reportado | [Commit 1610fb8](https://github.com/qgis/QGIS/commit/1610fb8766a13351bb303ee3bfd6301dbdc6648b) | [Commit 3944db4](https://github.com/qgis/QGIS/commit/3944db47dda6b08ea4b22f61c5e72d97597362b1) |
| Corregido el bloqueo al renderizar en las compilaciones del proj 6 | [#33902](https://github.com/qgis/QGIS/issues/33902) | [Commit 8a71091](https://github.com/qgis/QGIS/commit/8a7109163a9362af2a5e0187cf2b57fc0219fe59) | [Commit f41076d](https://github.com/qgis/QGIS/commit/f41076d45f5f259c50e3ead2cac4d664be11bbfb) |
| Don\'t try to label empty geometries | [#33931](https://github.com/qgis/QGIS/issues/33931) | [Commit 1144974](https://github.com/qgis/QGIS/commit/11449743788f3fd346c01c46cff01bcf3f84edf0) | N/A - 3.12 solo |
| Se corrigieron bloqueos al intentar exportar capas ráster reproyectadas | [#33801](https://github.com/qgis/QGIS/issues/33801) | [Commit bbd055c](https://github.com/qgis/QGIS/commit/bbd055ca13a3d6ee150251222d73e3b9e76d94c5) | [Commit 2fff8e1](https://github.com/qgis/QGIS/commit/2fff8e1205daffafa257b9312cc2c005b5e3017e) |
| Solucionar problemas de codificación de archivos shape | [#21264](https://github.com/qgis/QGIS/issues/21264) | Remitido | Retenido 3.10.4 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
