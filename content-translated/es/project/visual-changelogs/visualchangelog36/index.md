---
HasBanner: false
draft: false
releaseDate: '2019-02-22'
section: proyecto
sidebar: true
title: registro de cambios para QGIS 3.6
type: visual-changelog

---
{{<content-start >}}
# registro de cambios para QGIS 3.6{#changelog36 }
![image1](images/projects/f335c2ee37b714ad6eec143246d947f09a5ff2f1.png)

Fecha de lanzamiento: 2019-02-22

¡El mejor lanzamiento de QGIS! QGIS 3.6 trae una lista masiva de nuevos cambios, cuyos aspectos más destacados trataremos de cubrir aquí. Como siempre, podemos recordarle que QGIS es un proyecto de código abierto y, si puede, considere apoyar nuestro trabajo a través de donaciones, patrocinios o contribuciones a la documentación del código, el sitio web, etc.

Gracias

Nos gustaría agradecer a los desarrolladores, documentadores, testers y a toda la gente ahí fuera que dedica su tiempo y esfuerzos (o financia a personas para que lo hacen). ¡Desde la comunidad de QGIS esperamos que disfrutes de este nuevo lanzamiento! Si deseas donar tiempo, dinero o participar de cualquier otra forma para hacer QGIS más impresionante, ¡por favor ve a qgis.org y echa una mano!

QGIS es sustentado por donantes y patrocinadores. Puedes ver una lista actual de donantes que han hecho contribuciones financieras grandes y pequeñas para el proyecto en nuestra lista de donantes. Si deseas convertirse en patrocinador oficial del proyecto, visita nuestra página de patrocinio para obtener más información. El patrocinio de QGIS nos ayuda a financiar nuestras reuniones de desarrolladores cada seis meses, mantener la infraestructura del proyecto y financiar los esfuerzos de corrección de bugs. A continuación se proporciona una lista completa de los patrocinadores actuales. ¡Muchas gracias a todos nuestros patrocinadores!

{{<fund type="active" >}}

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Herramientas de mapa
### Prestación: decoración de la etiqueta de título
Se ha agregado un nuevo decorador para permitir a los usuarios agregar rápidamente un título a sus lienzos. El decorador presenta una barra de fondo con color y opacidad personalizables.

![image2](images/entries/400e617d8059eddcd1228f3ce6861d6087f65794.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Posicionamiento centrado superior/inferior para elementos de decoración
Los derechos de autor del lienzo del mapa y las decoraciones de títulos recién agregadas ahora pueden centrarse en la parte superior o inferior de la vista del mapa.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Correciones y mejoras de la herramienta vértices correciones y mejoras
Nota: Todos los elementos mencionados anteriormente han sido respaldados a LTR así que también aparecerán en QGIS 3.4.5.
### Select (\"lock\") feature before editing
In QGIS 2.18 you always had to select a feature first before editing it. In QGIS 3 there was no such thing - editing would be done on any feature any time. Now we are making the selection of feature (\"lock\") available again - using **right click**.

En versiones anteriores de QGIS 3, hacer clic con el botón derecho en una función abriría un pequeño menú emergente que ofrecería la visualización del editor de vértices. **Ahora, al hacer clic derecho en una función, se mostrará inmediatamente el editor de vértices y se deshabilitará la edición de cualquier otra entidad.**

When a feature is \"locked\", it can be again unlocked by clicking on it or by clicking on an empty area - this will bring us back to the default mode when multiple features can be edited.

**Cuando hay varias entidades en la ubicación del mouse, se repetirán los clics con el botón derecho sobre ellas**, con cada clic con el botón derecho se retendrá una entidad diferente. Finalmente, cuando se hayan ofrecido todas las entidades, no se bloqueará ninguna entidad y los clics con el botón derecho del mouse comenzarán nuevamente el ciclo.

The locking is possible when clicking a feature\'s vertex, edge or interior (for polygons).
### Añadir nuevo vértice sin moverlo
Ahora es posible usar **Shift + doble clic para agregar un nuevo vértice sin colocarlo en una nueva ubicación**. A veces esto es útil cuando los usuarios desean agregar vértices adicionales en los segmentos existentes.
### \"Current layer\" mode is now the default
From the two modes of vertex tool, \"all layers\" used to be the default one. But from the user feedback that seemed like less common case and users prefer to have \"current layer\" as the default.

This feature was funded by [German QGIS user group](http://qgis.de/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Recortar/Extender
A diferencia de varios programas, la herramienta le permite modificar líneas(múltiples)  y polígonos(múltiples). Además, no es necesariamente el final de las líneas lo que concierne; Cualquier segmento de una geometría puede ser modificado. Por otro lado esto puede conducir a geometrías no válidas, es responsabilidad del usuario.

La herramienta le pide que seleccione un límite (un segmento) hasta el que se extenderá o cortará otro segmento. A diferencia de la herramienta de nodo, se realiza una verificación para modificar solo la capa que se está editando.

Cuando ambos segmentos están en 3D, la herramienta realiza una interpolación en el segmento límite para devolver la Z.

En el caso de un recorte, debe seleccionar la parte que será recortada clickando en ella.

This feature was funded by [Mairie de Megève](https://www.megeve.fr/)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Prestación: Rectángulo desde 3 puntos(proyectado)
Ya existe un método para hacer un rectángulo de 3 puntos donde el rectángulo toma una longitud entre el primer y el segundo punto y la segunda longitud es igual a la distancia entre el tercer y el segundo punto.

Este nuevo método permite crear un rectángulo de 3 puntos donde la segunda longitud es la distancia entre el punto y el punto proyectado perpendicularmente en el segmento (o su extensión).

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Prestación: Herramienta identificar para capas de malla
La herramienta de identificación ahora funciona en la capa de malla. Muestra el valor de los componentes escalares y vectoriales de la malla en el momento actual.

![image3](images/entries/62a172172d717af1b5399af4006db1ee0e82c7f5.png.400x300_q85_crop.webp)

Esta prestación fue fundada por Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Expresiones
### Prestación: Nuevas funciones de expresión
- `force_rhr`: forces polygons to follow the right hand rule, in which the area that is bounded by a polygon is to the right of the boundary. In particular, the exterior ring is oriented in a clockwise direction and the interior rings in a counter-clockwise direction.
- `decode_uri`: takes a layer parameter and an optional uri part parameter. It will return details about the data source of the layer. The available details depend on the data provider. If called with only a layer parameter, a map will be returned with all the available information. If the part is also specified, only the value for the requested part will be extracted from the map.
- `path` has been added as an option for the `layer_property` expression function
- `array_sort`: sorts an array of elements
- `nullif`
- sqlite_fetch_and_increment
- `make_rectangle_3points`: Make a rectangle from 3 points. There is two options for make the rectangle by the distance or a projection. Option distance: Second distance is equal to the distance between 2nd and 3rd point. Option projected: Second distance is equal to the distance of the perpendicular projection of the 3rd point on the segment or its extension.
- `make_square`: Creates a square from a diagonal.
- from_json
- to_json

### Prestación: Corchetes para acceder fácilmente a los elementos del conjunto de mapas
Permite expresiones como:
- array(1,2,3)\[0\] -\> 1
- array(1,2,3)\[2\] -\> 3
- array(1,2,3)\[-1\] -\> 3 (Python style, negative indices count from end of array)
- array(1,2,3)\[-3\] -\> 1
- map(\'a\',1,\'b\',2)\[\'a\'\] -\> 1
- map(\'a\',1,\'b\',2)\[\'b\'\] -\> 2

Esta herramienta fue desarrollada por Nyall Dawson, Matthias Kuhn
### Prestación: Nuevas variables de mapas de expresión
- \@map_crs_description: name of the coordinate reference system of the map.
- \@map_crs_acronym: acronym of the coordinate reference system of the map.
- \@map_ellipsoid_acr: acronym of the ellipsoid of the coordinate reference system of the map.
- \@map_crs_proj4: Proj4 definition of the coordinate reference system.
- \@map_crs_wkt: WKT definition of the coordinate reference system.

Esta herramienta fue desarrollada por Alexis Roy-Lizotte
### Prestación: Nueva función try() para capturar errores
La nueva función try() intenta una expresión y devuelve su valor si está libre de errores. Si la expresión devuelve un error, se devolverá un valor alternativo cuando se proporcione; de lo contrario, la función devolverá null.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## Interfaz de usuario
### Feature: A new grayscale theme: \"Blend of Gray\"
A brand new UI theme has made its way into QGIS named \"Blend of Gray\". In addition, hundreds of fixes, tweaks, and refinements were applied to the preexisting \"Night Mapping\" theme.

![image4](images/entries/32e743ea5bf84c96b86ea31160b1677b6362eacf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Selección y edición de multilíneas en el editor de código/expresión
Si mantiene presionada la tecla Ctrl mientras selecciona las expresiones QGIS y los editores de secuencias de comandos de Python, puede seleccionar un bloque de texto de varias líneas, que puede editarse de una sola vez.

This feature was developed by [Nyall Dawson ()](https://north-road.com)
## Simbología
### Prestación: Mejor manejo de librerías de estilo de .XML
El panel del navegador ahora muestra bibliotecas xml de estilos de QGIS, y estos archivos también se pueden arrastrar y soltar en una ventana QGIS. Esto abre un cuadro de diálogo que permite a los usuarios explorar la biblioteca de estilos e importar estilos desde la biblioteca a su instalación QGIS.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Opcionálmente forzar la regla de la mano derecha durante el renderizado de símbolo poligonal
This new option, available under the \"Advanced\" button for fill symbols, allows forcing rendered polygons to follow the standard \"right hand rule\" for ring orientation (where exterior ring is clockwise, and interior rings are all counter-clockwise).

La corrección de orientación se aplica solo al renderizar, y la geometría de la entidad original no cambia.

Esto permite la creación de símbolos de relleno con una apariencia consistente, independientemente del conjunto de datos que se representa y la orientación del anillo de entidades individuales.

Esta prestación fue fundada por el Grupo de Usuarios de Alemania de QGIS

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Opción para lineas simples de solo renderizar el círculo exterior o el interior
This new option is shown whenever a simple line symbol or marker line symbol is used as part of a fill symbol for rendering polygons. The default behavior is to render both interior and exterior rings, but this new setting allows users to set the symbol layer to render only for the exterior ring OR only for interior rings. This allows for symbolisation which wasn\'t directly possible before, such as a marker line with markers for interior rings angled toward the interior of the polygon.

Esta prestación fue fundada por el Grupo de Usuarios de Alemania de QGIS

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: marcador de imagen ráster
Se agregó un nuevo tipo de simbología de marcador de imagen ráster a QGIS que permite a los usuarios usar un ráster, es decir, un mapa de bits, un archivo de imagen para mostrar como marcador. La simbología del marcador de imagen ráster permite la personalización de ancho, alto, relación de imagen, rotación y opacidad.

Utilizando una fuente de imagen definida por datos, esta nueva simbología es un excelente método para mostrar imágenes georreferenciadas en un lienzo de mapa.

![image5](images/entries/511ac83d3b841be6ae81db5f5d0f319e07e9656e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: El relleno de ráster puede tener imágenes configuradas en URL remotas o imágenes incrustadas
Al igual que el marcador SVG y de imagen ráster, el relleno de ráster ahora se puede configurar para usar URL de HTTP o tener archivos directamente incrustados dentro del símbolo.

Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: Usar valores de representación para renderizadores clasificados
When a field is configured with a value relation, value map or other \"representable value\" and the field is used as the source for a classification renderer, the represented values will be taken to label the categories.

Esta prestación fue desarrollada por Matthias Kuhn
### Prestación: Opción de mezclar categorías en renderizador clasificado
Este cambio permite a los usuarios seleccionar varias categorías existentes y agruparlas en una sola categoría, que se aplica a cualquiera de los valores de la selección.

Esto permite un estilo más sencillo de capas con una gran cantidad de categorías, donde es posible agrupar numerosas categorías distintas en un conjunto de categorías más pequeño y manejable que se aplica a múltiples valores.

La opción está disponible en el menú contextual del botón derecho en la vista de lista de categorías, siempre que se seleccionen varias categorías.

![image6](images/entries/159eb5270ab436adbbddba1c92799d8621a0b8e5.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mostrar colores del proyecto en botones de colores vinculados a datos definidos
This adds a new \"Project Colors\" section in data defined buttons which are linked to a color value. The color menu contains all colors defined as part of the current project\'s Project Color Scheme (which is defined through project properties).

Cuando se selecciona un color de proyecto desde el botón, la propiedad se vincula a ese color. Seguirá automáticamente cualquier cambio futuro en el color cuando se realice a través de las propiedades del proyecto.

This allows users to define common colors for a project once, and then \"bind\" symbol, label, layout, etc colors to these preset colors. The link is live, so you change it once, and the change is reflected EVERYWHERE. Sure beats updating a color 100 times when it\'s use has been scattered throughout a project\'s symbols, labels, etc\...

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Diálogo de administrador de estilos mejorado
El diálogo del administrador de estilos ha visto numerosas mejoras:
- A new \"list view\" mode has been added
- An \"all\" tab has been added, which shows all matching symbols (regardless of the symbol type)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Exportar SLD para estilos ráster
QGIS is now able to export raster styling to sld, for example to be used in Geoserver. See: <https://docs.geoserver.org/latest/en/user/styling/qgis/index.html#exporting-raster-symbology>

![image7](images/entries/7ab383dfaa0a0dbc9651168a56f44e2275b8c2df.png.400x300_q85_crop.webp)

Esta prestación fue fundada por OSGeo UK, GeoServer PSC, Brad Hards

This feature was developed by [Luigi Pirelli and GeoSolutions](https://www.geo-solutions.it/)
## Digitalizando
### Prestación: Mejoras de georreferenciadores
- añadir dX, dY y residuales en Puntos GCP
- Añadir opción para guardar automáticamente puntos GCP en la ruta modificada por ráster

![image8](images/entries/2d6278e2e65be30ceb12ff30f26d34dae6196e42.png.400x300_q85_crop.webp)

This feature was developed by [Faneva Andriamiadantsoa](https://github.com/Fanevanjanahary)
### Prestación: Nueva opción para evitar minimizar el georreferenciador al agregar puntos
Los usuarios ahora pueden optar por evitar la minimización automática de la ventana del georeferenciador que se produce al agregar nuevos puntos de control desde el lienzo del mapa. Este comportamiento puede ser molesto en configuraciones de monitores múltiples donde puede ser deseable tener ambas ventanas visibles al agregar puntos.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Administración de datos
### Prestación: Opción de comentario en db manager
This feature was developed by [Corentin Falcone (SIRS)](https://www.sirs-fr.com/sirs/fr/)
## Widgets y Formularios
### Prestación: Nuevo widget de formulario para campos binarios (blob)
Este widget está disponible solo para campos binarios (y es el widget predeterminado utilizado para campos binarios). Ofrece una etiqueta que muestra si el campo de blob está vacío o no, y si no está vacío muestra el tamaño del contenido (en bytes / kb / etc.).

Un botón de menú desplegable permite a los usuarios guardar el contenido binario actual del campo en un archivo en disco, borrar el contenido de un campo del blob o incrustar contenido binario seleccionando un archivo de su sistema.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Compositor de Mapa
### Prestación: Mejoras en la rejilla del marco
Users can now set a margin for the grid frames in layout map items. Additionally, new \"Zebra (Nautical)\" and \"Line border (Nautical)\" frame styles have been added, which show nautical-style blocks in the grid corners when a margin is set for the grid.

Esta herramienta fue desarrollada por konst
### Prestación: Manejo mejorado de la exportación de texto y etiquetas
Al exportar un diseño de impresión a formatos PDF o SVG, los usuarios ahora pueden elegir cómo exportar el texto y las etiquetas dentro de ese diseño. Las opciones disponibles son convertir todo el texto para contornos/curvas (el valor predeterminado anterior) o dejar texto y etiquetas como objetos de texto.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mejoras en el etiquetado de Mapa
Se han realizado varias mejoras con respecto a cómo se representan las etiquetas dentro de los elementos en el diseño del mapa.
- A new setting allows per-map control of how close labels are permitted to be placed to the map item\'s edges. Sizes can be set using mm/inches/pixels/etc, and data defined label margins are allowed.
- Una nueva configuración permite el control en el mapa de si las etiquetas parciales son visibles en el mapa. Este valor predeterminado es desactivado (a diferencia de la configuración del lienzo, que por defecto está activado para un nuevo proyecto), ya que los diseños siempre deben tener la configuración predeterminada que produce los resultados cartográficos de mayor calidad.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Reconstrucción de accesos directos de extensión/escala de elementos de mapa
Los botones para configurar los elementos del mapa de diseño para que coincidan con la vista del mapa actual (y viceversa) se han movido a una nueva barra de herramientas en las ventanas de propiedades de elementos del mapa.

New actions have also been added to set the map item\'s scale to match the main canvas scale, and to set the main canvas scale to match the selected layout map\'s scale. These mirror the existing settings for setting the extent from the canvas and pushing the extent TO the canvas.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Layout items can \"block\" map labels
This feature allows other layout items (such as scalebars, north arrows, inset maps, etc) to be marked as \"blockers\" for the map labels in a map item. This prevents any map labels from being placed under those items - causing the labeling engine to either try alternative placement for these labels (or discarding them altogether).

This allows for more cartographically pleasing maps \-- placing labels under other items can make them hard to read, yet without this new setting it\'s non-trivial to get QGIS to avoid placing the labels in these obscured areas.

The blocking items are set through a map item\'s properties, under the label settings panel. The setting is per-map item, so you can have a scalebar block the labels for one map in your layout and not others (if you so desire!)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Advertencias en exportaciones
Cuando exportamos diseños de impresión, QGIS ahora verifica automáticamente el diseño para errores comunes y advierte a los usuarios cuando se encuentran:
- Barras de escala no enlazadas a un elemento del mapa
- Elementos de imagen con rutas rotas o desaparecidas, o enlazadas a archivos de imagen ilegibles
- Las vistas generales de mapas ya no están vinculadas a un elemento de mapa válido

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Control sobre la posición de apilamiento de las extensiones de vista general del mapa
QGIS allows overview extents to be drawn below map labels (the new default), but in 3.6 choices have been added for drawing them below all map layers, or above/below a specific map layer. This allows users to control exactly where in the map item\'s layer stack the overview will be placed, e.g. allowing them to draw a overview extent below some feature layers such as roads whilst drawing it above other background layers.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Nuevas variables de expresión para elementos de leyenda
Se han añadido nuevas variables de expresión para usar en expresiones de datos definidos en elementos de diseño de leyenda, incluyendo:
- \@legend_title
- \@legend_column_count
- \@legend_split_layers
- \@legend_wrap_string
- \@legend_filter_by_map
- \@legend_filter_out_atlas

If the legend is linked to a map, then expressions used in that legend will also have access to the linked variables, including \@map_scale, \@map_extent, etc.

Además, los símbolos representados como parte de una leyenda ahora usan el contexto de expresión disponible completo para la leyenda. Esto significa que los símbolos tendrán acceso a variables como la función de atlas actual.

Esta herramienta fue desarrollada por Alexis Roy-Lizotte
### Prestación: Expresiones dentro de texto de elementos de leyenda
This feature allows for expressions to be embedded directly inside legend item text (e.g. group, subgroup and item text). The expressions are evaluated at render time, with full knowledge of the legend\'s expression context (so can utilise variables from the layout/layout item/etc)

There\'s no UI for this yet (that will come in 3.8), but expressions are entered using the standard \[% 1 + 2 %\] format.

p.Ej. un texto de elemento de leyenda

    My layer (rendered at 1:[% @map_scale %])
    
Mostrará una salida como

    My layer (rendered at 1:1000)
    
This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Herramientas de análisis
### Prestación: Aceleración de Hardware para calculadora de ráster
La aceleración de OpenCl está ahora disponible por defecto para operaciones de la calculadora de ráster.

Esta prestación fue fundada por Alessandro Pasotti - ItOpen

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: Calculadora de malla
Similar a la calculadora ráster, la calculadora de malla funciona en capas de malla. Además de las funciones generales, la calculadora de malla también proporciona funciones de agregado de tiempo. Por ejemplo, si tiene un netcdf con temperatura diaria durante un mes, puede calcular la temperatura promedio de todo el mes para cada celda. La salida se puede filtrar por intervalo de tiempo o extensión espacial.

Esta prestación fue fundada por Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Procesado
### Feature: New algorithm \"Remove duplicates by attribute\"
Permite la eliminación de entidades duplicadas, identificadas usando los valores de uno o más valores de campo de las características de entrada. Opcionalmente, cualquier entidad descartada (duplicada) se puede guardar en un sumidero separado.

![image9](images/entries/ae0544826b7d16479b2e48ba97f1f530c80bbd42.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Descomponer el algoritmo HStore
This algorithm creates a copy of an input layer and adds a new field for every unique key found in a HStore type field. For instance, a HStore field is often present in an OSM dataset (\"other_tags\").

![image10](images/entries/304c29f7cc6d26aa823001b67a46744deec3c2dd.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Prestación: Forzar la regla de la mano derecha
Este nuevo algoritmo obliga a las geometrías de polígonos a respetar la Regla de la mano derecha, en la que el área delimitada por un polígono está a la derecha del límite. En particular, el anillo exterior está orientado en sentido horario y el interior gira en sentido antihorario.

![image11](images/entries/16db7b4b5931c9d96eba053701641defc6f52290.png.400x300_q85_crop.webp)

Esta prestación fue fundada por el Grupo de Usuarios de Alemania de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Algoritmo de extracción de campo binario
Este nuevo algoritmo permite a los usuarios a extraer campos binarios a archivos.

![image12](images/entries/6715290eac02e216394b3f24045da0b982069c7d.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Cortar líneas por el algoritmo de máxima longitud
Este algoritmo toma una capa de entrada (multi) línea (o curva) y divide cada entidad en varias partes de modo que ninguna parte sea más larga que la longitud máxima especificada.

Admite la propiedad de longitud máxima definida por datos y la operación de edición in situ.

![image13](images/entries/13c8c2fedfa76ff8decbc4d7e6d683d01bab1126.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Nyall Dawson, Nathan Woodrow
### Prestación: Nuevo tipo de parámetro para configuración de autenticación
Se ha agregado un nuevo tipo de parámetro para procesar algoritmos, QgsProcessingParameterAuthConfig, que permite la selección de las configuraciones de autenticación disponibles (y la creación de otras nuevas).

It allows creation of processing algorithm which can fully take advantage of QGIS\' mature authentication handling, avoiding the need to use insecure string parameters for users to input sensitive logon credentials.

Los parámetros QgsProcessingParameterAuthConfig se evalúan utilizando QgsProcessingAlgorithm.parameterAsString(), que devuelve el ID de configuración de autenticación seleccionado.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: opciones de remuestreo y formato en el algoritmo gdaladdo
Esta prestación fue desarrollada por Alex Bruy
### Prestación: Algoritmo de estadísticas zonales de ráster
This algorithm calculates statistics for a raster layer\'s values, categorized by zones defined in another raster layer.

![image14](images/entries/014272dcac2a228f8d8cc7a1587ac9b07865bc1f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Algoritmos de extracción de valores Z y M
Estos algoritmos permiten a los usuarios convertir valores Z o M presentes en entidades de geometrías a atributos en la capa.

Por defecto, se extrae el valor z/m del primer vértice de la entidad, pero opcionalmente las estadísticas se pueden calcular en TODOS los valores z/m de la geometría (por ejemplo, calcular la media/min/max/suma/etc. de los valores z).

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: División en línea geodésica con algoritmo antimeridiano
Este algoritmo divide una línea en múltiples segmentos geodésicos, siempre que la línea cruza el antimeridiano (± 180 grados de longitud). La división en el antimeridiano ayuda a la visualización de las líneas en algunas proyecciones. La geometría devuelta siempre será una geometría de varias partes.

Siempre que los segmentos de línea en la geometría de entrada crucen el antimeridiano, se dividirán en dos segmentos, y la latitud del punto de ruptura se determinará utilizando una línea geodésica que conecta los puntos a cada lado de este segmento. Se utilizará la configuración actual del elipsoide del proyecto al calcular este punto de interrupción.

Si la geometría de entrada contiene valores M o Z, estos se interpolarán linealmente para los nuevos vértices creados en el antimeridiano.

También soporta el modo de edición in-situ.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Geodesic mode for \"Join by Lines (Hub lines)\" algorithm
Esto permite la creación opcional de líneas geodésicas, que representan la distancia más corta entre los puntos basándose en el elipsoide.

Cuando se utiliza el modo geodésico, es posible dividir las líneas creadas en el antimeridiano (± 180 grados de longitud), lo que puede mejorar la representación de las líneas. Además, se puede especificar la distancia entre vértices. Una distancia menor da como resultado una línea más densa y precisa.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Algoritmo de volumen de superficie ráster
El volumen de la superficie ráster SAGA se ha portado a un algoritmo QGIS nativo. La versión SAGA de este algoritmo es de uso limitado en QGIS, porque el volumen calculado está incrustado solo en la salida del terminal SAGA. Esto evita que se guarde en un archivo o se reutilice dentro de un modelo como entrada para un paso posterior del modelo. En consecuencia, el algoritmo se ha transferido a un algoritmo nativo QGIS C++. El algoritmo duplica el algoritmo SAGA 1:1, pero genera el volumen (y el área) en un informe HTML o en una tabla de vectores. Además, las salidas se exportan como salidas numéricas del algoritmo, lo que permite su reutilización dentro de los modelos.

![image15](images/entries/e0a8089ec0653cf5628636354ec80ef317e68565.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Modelo recuperado a la funcionalidad de script Python
La capacidad 2.x de convertir directamente un modelo de procesamiento en un script Python equivalente se ha recuperado y actualizado para la API de procesamiento 3.x.

![image16](images/entries/42b342e04b54d5e106ba1051b210d83af8712dd8.png.400x300_q85_crop.webp)

This feature was funded by [Solspec](http://solspec.io)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Opciones de Aplicación y Proyecto
### Prestación: Eliminar la configuración de la pestaña Avanzado en opciones
This change adds a new right click menu to the settings shown in the \"Advanced\" tab in the settings dialog, which allows users to remove that setting (or group of settings).

![image17](images/entries/6b012542ef9ca282ba6f9087758f85d818dd5ec9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Navegador
### Feature: Add \"export to file\" options for raster and vector layers within the browser
Permite la exportación directa de estos archivos (p.ej. a un formato diferente, crs, etc) sin tener que cargarlos primero en un proyecto.

![image18](images/entries/d939594c84d7aa186fe5f18f46ed7ad0c89d8c67.png.400x300_q85_crop.webp)

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Propiedades nativas de archivo/carpeta
You can now right click on a file or folder within the browser, and select \"File Properties\" or \"Directory Properties\" to open the native file/folder properties dialog for that entry. This allows rapid access to operating system file or folder properties, such as file permissions and sharing options.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Previsualización de capas y atributos
QGIS 3.6 brings back the functionality from the old 2.18 standalone \"browser\" application to preview layers and their attributes. This functionality has been moved to the inbuilt browser panel, and is available by right-clicking on a layer and selecting \"properties\" (or by clicking the \"enable properties widget\" button in the browser toolbar).

![image19](images/entries/5058aa9a701e417271b0cbf0869669177a7f0fe4.png.400x300_q85_crop.webp)

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Explorar archivos de proyecto QGS/QGZ en el navegador
Las versiones anteriores de QGIS mostrarían los archivos de proyecto QGS / QGZ en el navegador, lo que les permitiría abrirse como el nuevo proyecto activo. En QGIS 3.6 esta funcionalidad se ha ampliado, y los archivos de proyecto ahora se pueden explorar directamente DENTRO del navegador. Los proyectos ahora son elementos expandibles, y expandirlos muestra la estructura completa del proyecto de grupos y capas. Cualquier capa se puede arrastrar y soltar al proyecto actual.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Crear directamente Geopaquetes y Shapefiles
Right clicking a directory in the browser panel now shows a \"New\" menu, containing items for creating a new Geopackage, Shapefile, or subdirectory under the selected directory.

![image20](images/entries/2bc8475b95a8413285b3c88a9a070f02f43cf5b9.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Abrir Terminal en la ruta
Se ha agregado una nueva entrada al menú contextual para los elementos del directorio del panel del navegador para abrir una nueva ventana de terminal en ese directorio.

En Windows, este nuevo terminal hereda el entorno QGIS, por lo que los comandos GDAL y los scripts Python que utilizan los comandos PyQGIS funcionan sin necesidad de una configuración adicional del entorno.

¡Los hackers de la terminal se regocijan!

![image21](images/entries/623ef55ae3918f72faa7ec796bbac01bf5063464.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## General
### Feature: Improved \"missing layer\" handling on project load
![image22](images/entries/8e3fbce280478d8e88cab7e24b489b783c83fc13.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it)
### Prestación: Ajuste opcional para desabilitar comprobación de versión
A new setting, \"allowVersionCheck\" has been added to the QGIS configuration ini file. If set to true (the default), users may control whether the version check is enabled or disabled through the QGIS settings dialog. When this setting is set to false, no version checking will be performed AND users will NOT have an option to enable this check in the settings dialog.

Esta configuración está diseñada para su uso en instalaciones empresariales donde la gestión de versiones de QGIS se maneja de forma centralizada.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Añadir una acción Toggle a elementos de leyenda de capa vectorial
![image23](images/entries/f3b822b5591367b7d246fbdd5173763a1633b9ec.png.400x300_q85_crop.webp)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
## Proveedores de datos
### Prestación: Información de servicio Open para capas de ArcGIS Feature Server
Las capas de ArcGIS Feature Server tienen una nueva opción de menú de clic derecho en el panel del navegador, lo que permite a los usuarios abrir directamente la página web de información del servicio para la capa seleccionada.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: soporte de BLOB binario para proveedores OGR
En lugar de convertir campos binarios en cadenas truncadas, estos valores ahora se pueden recuperar como su contenido binario original. Esto permite que los complementos y los scripts utilicen campos binarios, como extraer sus contenidos.

Adicionálmente, se pueden crear nuevos campos binarios para fuentes de datos compatibles.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: marcador de imagen y soporte de relleno de imagen de ArcGIS Feature Server
Al cargar una capa de Feature Server con marcador de imagen o simbología de relleno de imagen, QGIS convertirá automáticamente el marcador de imagen ESRI y los símbolos de relleno y los usará como el estilo predeterminado para la capa.

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

Esta herramienta fue desarrollada por Nyall Dawson, Matthias Kuhn
### Prestación: soporte de etiquetado de ArcGIS Feature Server
Cuando una capa de Feature Server tiene un etiquetado definido por el servidor, esta configuración de etiquetado se usará automáticamente de forma predeterminada al cargar la capa en QGIS.

Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: soporte de campo boleano y binario para capas de memoria
Memory (\"Temporary scratch\") layers can now use binary and boolean (true/false) field types.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Soporte de JSON para GeoPackage
Soporte para JSON permite almacenar datos estructurados dentro de un campo sencillo en archivos GeoPackage.

Los datos que se guardan como JSON se pueden representar y editar en
- Widgets ValueRelation con permiso de selección múltiple activada
- KeyValue widgets
- Listado de Widgets
- or the [QML widget which also supports visualizing JSON data](https://www.opengis.ch/2018/11/13/visualize-postgres-json-data-in-qml-widgets/)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Esta prestación fue desarrollada por David Signer (OPENGIS.ch)
### Prestación: proveedor Postgres: guardar clave de selección primaria
When a view loaded from Data Source Managers\'s PostgreSQL tab you can select the key columns of the view (by default the first column is used, which can be wrong). This commit stores that selection in the settings, so that it doesn\'t have to be reselected on subsequent loads. This stored selection is also used when adding the loading from the browser.

Esta prestación fue desarrollada por Jürgen Fischer
### Prestación: soporte de valor único de múltiples campos de ArcGIS Feature Server
QGIS ahora puede mostrar una capa de Feature Server con una configuración de renderizador de múltiples campos de valor único.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## Servidor de QGIS
### Feature: Possibility to set ATLAS_PK in GetPrint request to print atlas sheet(s)
El nuevo parámetro GetPrint acepta la(s) clave(s) primaria(s) para las que se deben imprimir las hojas de atlas, separadas por comas,

Tal solicitud se vería así:

    https://yourserver.name/path/to/qgisproject?SERVICE=WMS&REQUEST=GetPrint
    &TEMPLATE=A4&FORMAT=pdf&ATLAS_PK=1,3,7
    
One can also provide an asterisk (\*) for ATLAS_PK to request all features of an atlas. To protect the server against requesting too many features, it is possible to restrict it to a defined maximum of features that can be requested at one time (see attached screenshot).

Como los clientes pueden no saber qué plantilla tiene un atlas y qué atributo(s) son la clave(s)  principal(es)  de la capa de cobertura, esta nueva característica también agrega esta información a la respuesta GetProjectSettings del servicio WMS.

![image24](images/entries/6a4648e447531099dfd8d5e113c2a79c8420df06.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, Amt für Geoinformation](https://geo.zg.ch/)

Esta prestación fue desarrollada por Marco Hugentobler
### Prestación: Configuración de matrices de teselas WMTS
En QGIS Server 3.4, se agregó la API WMTS en la que se calculan las matrices de mosaicos, excepto EPSG: 3857 y EPSG: 4326.

Este cambio agrega la capacidad de seleccionar las matrices de teselas para usar con el proyecto y configurar la esquina superior izquierda y el último nivel de la matriz de teselas. En el caso de EPSG: 3857 y EPSG: 4326, el usuario solo puede elegir el último nivel de las matrices de teselas.

Esta prestación fue fundada por Ifremer

Esta prestación fue desarrollada por 3liz
### Prestación: Añadir formato JSON a petición GetFeatureInfo para WMS
Thanks to this new feature, the FORMAT parameter of GetFeatureInfo for the WMS service may take \'application/json\' or \'application/geo+json\' values. In this case, the document returned by the server looks something like this:

    {"type": "FeatureCollection",
        "features":[
        {
           "type":"Feature",
           "id":"testlayer",
           "geometry":
           {"type": "Point", "coordinates": [913204.9128, 5606011.4565]},
           "properties":{
               "id":3,
               "name":"three",
               "utf8nameè":"three"
           }
        }]
    }
    
This feature was funded by [Veolia](https://www.veolia.com)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Plugins
### Prestación: DB Manager: botones añadidos para cargar y guardar un archivo SQL externo
Los nuevos botones permiten al usuario cargar y guardar la solicitud en un archivo SQL externo

![image25](images/entries/7d8fbe3054bd3d8b311d26d9343a20041f3fb809.png.400x300_q85_crop.webp)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Programabilidad
### Prestación: Nueva clase QgsExifTools
Contains utilities for retrieving the geotag from images and for setting an image\'s geotag.

Trabajar con geoetiquetas (¡antes de esta clase!) es súper molesto y complicado, y se basa en herramientas de análisis de línea de comandos o en bibliotecas Python no estándar que no están disponibles en todas partes, y a menudo es muy difícil para los usuarios en ciertas plataformas instalarse y operar correctamente

Con esta clase, tenemos métodos estables para obtener/configurar geoetiquetas que están disponibles universalmente y pueden ser utilizados de forma segura por complementos y scripts.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Iterar sobre partes de una QgsGeometry
This new PyQGIS API allows easy iteration over all the parts of a geometry, regardless of the geometry\'s type. E.g.

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
      print(part.asWkt())
    
    geometry = QgsGeometry.fromWkt( 'LineString( 0 0, 10 10 )' )
    for part in geometry.parts():
      print(part.asWkt())
    
Hay dos iteradores disponibles. QgsGeometry.parts() proporciona un iterador no constante, permitiendo que las partes se modifiquen en su lugar:

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.parts():
       part.transform(ct)
    
For a const iteration, calling .const_parts() gives a const iterator, which cannot edit the parts but avoids a potentially expensive QgsGeometry detach and clone

    geometry = QgsGeometry.fromWkt( 'MultiPoint( 0 0, 1 1, 2 2)' )
    for part in geometry.const_parts():
       print(part.x())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mejorada la API QgsLineString PyQGIS
Se han hecho algunas agradables adiciones a la API QgsLineString.
- len(QgsCurve) devuelve el número de puntos de una curva
- Localiza IndexErrors al llamara a pointN, xAt, yAt, zAt, mAt, setXAt, setYAt, setMAt, setZAt with indices de vértice inválidos
- Add \[\] getter for retrieving specific vertices, eg. ls\[0\] returns QgsPoint(\...)
- Add \[\] setter for setting specific (existing) vertices, e.g. ls\[1\] = QgsPoint(1,2)
- Add del support for removing vertices, e.g. del ls\[1\] removes the second vertex

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mejoras de API de PyQGIS Geometry Collection
La API de PyQGIS para trabajar con colecciones de geometrías ha sido mejorada:
- Llamar a removeGeometry con un índice no válido ahora generará un IndexError
- Calling collection\[0\] will return the first geometry in the collection, collection\[1\] the second, etc. And negative indices return from the end of the collection, so collection\[-1\] returns the last geometry in the collection.
- Geometries can be deleted by calling `del collection[1]` (deletes the second geometry from the collection). Also supports negative indices to count from the end of the collection.

Además, ahora puede iterar fácilmente sobre las geometrías en la colección, permitiendo este tipo de código:

    gc = QgsGeometryCollection()
    gc.fromWkt('GeometryCollection( Point(1 2), Point(11 12), LineString(33 34, 44 45))')
    for part in gc:
      print(part.asWkt())
    
This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Easier Processing algorithm creation via \@alg decorator
Permite lo siguiente para definir secuencias de comandos de procesamiento sin la necesidad de implementar una clase personalizada:

importar alg desde qgis.processing

| \@alg(name=\"test2\", label=\"test 2\", group=\"test\", groupid=\"test\") | \@alg.input(type=alg.STRING, name=\"IN1\", label=\"In string\") | \@alg.input(type=str, name=\"IN2\", label=\"In string 1\", optional=True) | \@alg.input(type=str, name=\"IN3\", label=\"In string 2\") | \@alg.input(type=alg.SINK, name=\"SINK\", label=\"Sink it!\") | \@alg.output(type=str, name=\"OUT\", label=\"WAT\") | \@alg.output(type=alg.MAPLAYER, name=\"OUT2\", label=\"WAT\") | \@alg.output(type=alg.VECTOR_LAYER, name=\"VECTOR_LAYER\", label=\"WAT\") | def testalg(instance, parms, context, feedback, inputs): | \"\"\" | This is a test function that does stuff | \"\"\" | feedback.pushInfo(\"We got these inputs!!\") | feedback.pushInfo(inputs\[\'IN1\'\]) | feedback.pushInfo(inputs\[\'IN2\'\]) | feedback.pushInfo(inputs\[\'IN3\'\]) | return { | \"OUT2\": \"wat\" | }

Esta prestación fue desarrollada por Nathan Woodrow
### Prestación: Bloqueando peticiones de red (no asíncronas)
Se ha agregado la nueva API PyQGIS para realizar con seguridad solicitudes de bloqueo. Es seguro para subprocesos y tiene soporte completo para el proxy QGIS y la configuración de autenticación.

    reply = QgsNetworkAccessManager.blockingGet(...)
    reply = QgsNetworkAccessManager.blockingPut(...)
    
Esta API debe usarse siempre que se requiera una solicitud de bloqueo de red. A diferencia de las implementaciones que dependen de QApplication::processEvents() o la creación de un QEventLoop, esta clase es completamente segura para subprocesos y se puede usar en el subproceso principal o en los subprocesos en segundo plano sin problemas.

Los redireccionamientos son manejados automáticamente por la clase.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Verificaciones de validez personalizadas en exportaciones de diseño
See <https://north-road.com/2019/01/14/on-custom-layout-checks-in-qgis-3-6-and-how-they-can-do-your-work-for-you/>

This feature was funded by [SMEC/SJ](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: API para calcular líneas Geodésicas
La nueva API PyQGIS para el cálculo de líneas geodésicas (la distancia más corta en un elipsoide) se ha agregado a QgsDistanceArea, que utiliza la biblioteca geográfica hecha para los cálculos geodésicos.
- QgsDistanceArea.geodesicLine : calcula la línea geodésica entre dos puntos
- QgsDistanceArea.latitudeGeodesicCrossesAntimeridian calcula la latitud a la cual la línea geodésica que une dos puntos cruza el antimeridiano
- QgsDistanceArea.splitGeometryAtAntimeridian: divide una cadena de líneas (múltiple) en el antimeridiano, utilizando líneas geodésicas para calcular el punto exacto en el que se produce la división en el antimeridiano

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Nueva clase QgsQuadrilateral
QgsRectangle no propone el soporte de orientación o Z, ya que su papel es para la extensión. Se crea una nueva clase llamada QgsQuadrilateral para administrar polígonos de 4 vértices. Por el momento, solo hay rectángulos, pero será posible agregar las otras formas más adelante.

Esta refactorización simplifica las herramientas de mapa y le permite utilizar la clase QgsQuadrilateral en otras herramientas.

Además, permitirá una mejor gestión de la Z para rectángulos a partir de 3 puntos. Hoy se usa la primera Z, ahora los puntos tendrán su Z y la cuarta se proyectará al vuelo.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Objetos 3D
### Prestación: Sombreado del terreno
This adds new options for user to choose how the terrain should be rendered: - shading disabled - color of terrain is determined only from map texture - shading enabled - color of terrain is determined using Phong\'s shading model, taking into account map texture, terrain normal vector, scene light(s) and terrain material\'s ambient+specular colors and shininess

Opcionalmente, los terrenos se pueden sombrear utilizando un tema de mapa preestablecido.

Esta prestación fue desarrollada por Martin Dobias (Lutra Consulting)
### Prestación: Configuración de luces en escenas de mapa 3D
Esta prestación agrega una sección para definir luces puntuales en escenas 3D. Se admiten hasta 8 luces (limitación por implementación de materiales). Para cada luz se puede establecer la posición, intensidad, color y atenuación.

Esta prestación fue desarrollada por Martin Dobias (Lutra Consulting)
### Prestación: Renderizador 3D basado en reglas
![image26](images/entries/0825fbe986d774f7f2d5a0bdfdbc2487453ef49c.png.400x300_q85_crop.webp)

Esta prestación fue fundada por la comunidad QGIS

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Prestación: Soporte para capa de malla(caras) en 3D
Con esta prestación, podrá usar capa de malla en una escena 3D,

![image27](images/entries/82a388b33e8fb96df43fb32b9bc5ef013be0459c.jpg.400x300_q85_crop.webp)

Esta prestación fue fundada por Lutra Consulting

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server: WFS issue using the EXP_FILTER parameter | [#20927](https://issues.qgis.org/issues/20927) | [PR #8924](https://github.com/qgis/QGIS/pull/8924) | Hecho |
| La respuesta GetFeatureInfo está vacía para la tabla de relaciones hijo en QGIS Server 3 | [#20801](https://issues.qgis.org/issues/20801) | No se puede reproducir con 3.5 |  |
| QGIS Server WFS DescribeFeatureType no responde al parámetro TYPENAME | [#20198](https://issues.qgis.org/issues/20198) | [PR #8948](https://github.com/qgis/QGIS/pull/8948) | Hecho |
| QGIS Server 3.4 can\'t reset numeric field using WFS Update | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Hecho |
| El proveedor WFS muestra campos numéricos NULL con 0 en lugar de NULL | [#20961](https://issues.qgis.org/issues/20961) | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Hecho |
| El título del proyecto OWS en las propiedades del proyecto no se puede establecer como blanco/vacío | no reportado | [PR #8958](https://github.com/qgis/QGIS/pull/8958) | Hecho |
| Relación de valor de formulario basada en capa WFS | [#21077](https://issues.qgis.org/issues/21077) | [PR #8970](https://github.com/qgis/QGIS/pull/8970) | Hecho |
| Posiciones de los botones en el cuadro de diálogo Administrador de estilos de base de datos | [#21068](https://issues.qgis.org/issues/21068) | [PR #8971](https://github.com/qgis/QGIS/pull/8971) | Hecho |
| la calculadora ráster en el procesamiento no funciona con el ráster Aspect | [#21011](https://issues.qgis.org/issues/21011) | No se puede reproducir con 3.5 |  |
| Error al abrir la página KML de red: ¡la descarga de rango no es compatible con este servidor! | [#21091](https://issues.qgis.org/issues/21091) | [PR #8985](https://github.com/qgis/QGIS/pull/8985) | Hecho |
| Can\'t add a virtual field or update a existing field of a WFS layer using the field calculator | [#21086](https://issues.qgis.org/issues/21086) | [PR #8990](https://github.com/qgis/QGIS/pull/8990) | Hecho |
| Abrir shapefiles en ZIP resulta en fuente de datos no válida | [#21097](https://issues.qgis.org/issues/21097) | No se puede reproducir con 3.5 |  |
| spatialite, edit table in dbmanager is broken in master Fault: no such table: pg_description | [#21151](https://issues.qgis.org/issues/21151) | [PR #9086](https://github.com/qgis/QGIS/pull/9086) | N/D |
| La capa de texto delimitado guarda la ruta absoluta cuando se proyecta en modo de ruta relativa | [#21150](https://issues.qgis.org/issues/21150) | [PR #9099](https://github.com/qgis/QGIS/pull/9099) | Hecho |
| field calculator doesn\'t load values for gpkg containing blank spaces or n dash (hypen) in field names | [#21100](https://issues.qgis.org/issues/21100) | [PR #9071](https://github.com/qgis/QGIS/pull/9071) | Hecho |
| Can\'t open feature form when when the primary key of Spatialite layer is created in text type | [#21176](https://issues.qgis.org/issues/21176) | [PR \#](https://issues.qgis.org/projects/qgis/repository/revisions/7f61dc495491752fd26c7f3bad56adc1f8950e3f) | No (diferido) |
| Geopackage layer rename in DB Manager does not update f_table_name values in the layer_styles table or the Triggers | [#21227](https://issues.qgis.org/issues/21227) | [PR #9164](https://github.com/qgis/QGIS/pull/9164) | No es posible porque se basa en la nueva función de cambio de nombre implementada en el navegador |
| Layer Properties \> Load Style \> From database \> \'Other styles \...\' \> Description column contains Name text, should contain Description text (it is a geopackage layer) | [#21254](https://issues.qgis.org/issues/21254) | [PR #9170](https://github.com/qgis/QGIS/pull/9170) | Hecho |
| Los comentarios en la consulta SQL en DB Manager interrumpen la consulta | [#21271](https://issues.qgis.org/issues/21271) | [PR #9180](https://github.com/qgis/QGIS/pull/9180) | N/D |
| Error con múltiples elementos Else en estilo basado en reglas | [#21281](https://issues.qgis.org/issues/21281) | [PR #9181](https://github.com/qgis/QGIS/pull/9181) | Hecho |
| GetFeatureInfo no envía Geometry cuando se configura en el proyecto | [#21172](https://issues.qgis.org/issues/21172) | No se puede reproducir con 3.5 | N/D |
| Geometry Checker se bloquea | [#21259](https://issues.qgis.org/issues/21259) | [PR #9191](https://github.com/qgis/QGIS/pull/9191) | Hecho |
| QGIS se bloquea cuando createInstance() usa un constructor incorrecto en una subclase QgsProcessingAlgorithm | [#21270](https://issues.qgis.org/issues/21270) | [PR #9193](https://github.com/qgis/QGIS/pull/9193) | Hecho |
| pegar entidades es muy lento | [#21305](https://issues.qgis.org/issues/21305) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (diferido) |
| Los formularios de atributos ya no muestran mensajes de restricciones | [#21266](https://issues.qgis.org/issues/21266) | Cerrado como inválido después de varias pruebas y algunas conversaciones con Giovanni Manghi | N/D |
| El proveedor de OGR devuelve un conjunto vacío para GPKG uniqueValues(0) | [#21311](https://issues.qgis.org/issues/21311) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (diferido) |
| \"default value\" is not applied when pasting features | [#21304](https://issues.qgis.org/issues/21304) | [PR #9203](https://github.com/qgis/QGIS/pull/9203) | No (diferido) |
| Postgis muy notablemente ralentizado al abrir la tabla de atributos si la tabla tiene una gran cantidad de columnas | [#21303](https://issues.qgis.org/issues/21303) | [PR #9219](https://github.com/qgis/QGIS/pull/9219) | No (diferido) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Prestación: Corrección de Errores por Alexander Bruy
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| gdal buildvrt falta un parámetro importante | [#20586](https://issues.qgis.org/issues/20586) | [PR #8927](https://github.com/qgis/QGIS/pull/8927) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| gdal:warpreproject missing old \'extra\' param | [#20721](https://issues.qgis.org/issues/20721) | [PR #8930](https://github.com/qgis/QGIS/pull/8930) | [PR #8944](https://github.com/qgis/QGIS/pull/8944) |
| Puntos dentro de polígonos | [#20798](https://issues.qgis.org/issues/20798) | No se puede reproducir con 3.5 |  |
| La interpolación IDW en la capa de puntos csv no funciona | [#20490](https://issues.qgis.org/issues/20490) | [PR #8942](https://github.com/qgis/QGIS/pull/8942) | [PR #8947](https://github.com/qgis/QGIS/pull/8947) |
| \[Processing\] Field calculator algorithm does not use the selected layer as default layer input | [#19686](https://issues.qgis.org/issues/19686) | [PR #8945](https://github.com/qgis/QGIS/pull/8945) | [PR #8949](https://github.com/qgis/QGIS/pull/8949) |
| v.surf.rst NO FUNCIONA EN QGIS 3.2.0 BONN | [#19472](https://issues.qgis.org/issues/19472) | [PR #8959](https://github.com/qgis/QGIS/pull/8959) | [Direct commit](https://github.com/qgis/QGIS/commit/c2465fc4a66425c296ffedb491d220a3db8ba453) |
| Clasificación SVM, SupportVectorMachineClassification (OpenCV) -Vector Field | [#20796](https://issues.qgis.org/issues/20796) | [PR #8960](https://github.com/qgis/QGIS/pull/8960) | [Direct commit](https://github.com/qgis/QGIS/commit/e0a8de477b04a6aa355d934c25ba37257bc63584) |
| El algoritmo de disolución GDAL/OGR no funciona correctamente con capas de punto/multipunto | [#20025](https://issues.qgis.org/issues/20025) | [PR #8972](https://github.com/qgis/QGIS/pull/8972) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Herramienta Build Vector Virtual: el archivo creado no se carga correctamente | [#14374](https://issues.qgis.org/issues/14374) | No se puede reproducir con 3.5 |  |
| \"Convert map to raster\" algorithm does not export with transparent background despite the option | [#19866](https://issues.qgis.org/issues/19866) | [PR #8965](https://github.com/qgis/QGIS/pull/8965) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| \[GUI\] Disable edit tools when no layer is selected/available nor selected layer is in edit mode | [#18141](https://issues.qgis.org/issues/18141) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| \"Add Rectangle From 3 Points\" is enabled on a new project | [#20333](https://issues.qgis.org/issues/20333) | [Direct commit](https://github.com/qgis/QGIS/commit/ab3adc663c37b3da589cf6bae56d733fcbc4feb3) | [Direct commit](https://github.com/qgis/QGIS/commit/38051a95afc190d3c65ca243fd505fb2a14b1622) |
| v.buffer processing algorithm fails when using option \"Name of column to use for buffer distances\". | [#19377](https://issues.qgis.org/issues/19377) | [PR #8973](https://github.com/qgis/QGIS/pull/8973) | [PR #8981](https://github.com/qgis/QGIS/pull/8981) |
| Problema con las URL a excluir de la configuración de red | [#20933](https://issues.qgis.org/issues/20933) | [PR #8995](https://github.com/qgis/QGIS/pull/8995) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Decimales truncados en el tamaño de píxel del conjunto de datos ráster | [#21023](https://issues.qgis.org/issues/21023) | [PR #8996](https://github.com/qgis/QGIS/pull/8996) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Las propiedades de etiquetas y estilo de capa incorporadas se pueden modificar dentro del panel estilo de capa | [#16339](https://issues.qgis.org/issues/16339) | [PR #9006](https://github.com/qgis/QGIS/pull/9006) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| processing: \"default output vector layer extension\" not respected by some tools | [#20557](https://issues.qgis.org/issues/20557) | [PR #8997](https://github.com/qgis/QGIS/pull/8997) | [PR #9022](https://github.com/qgis/QGIS/pull/9022) |
| Imposible parar ejecución del algoritmo GDAL | [#20441](https://issues.qgis.org/issues/20441) | [PR #9026](https://github.com/qgis/QGIS/pull/9026) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Agregar la opción para controlar las características de exportación sin categorías en el procesamiento de algoritmos GRASS | no reportado | [PR #9003](https://github.com/qgis/QGIS/pull/9003) | [PR #9043](https://github.com/qgis/QGIS/pull/9043) |
| Procesamiento: las herramientas v.net(GRASS) devuelven salidas vacías | [#19904](https://issues.qgis.org/issues/19904) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| v.net.salesman secuencia de salida HTML | [#21142](https://issues.qgis.org/issues/21142) | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| Los algoritmos v.net.report y v.net.nreport fallaron | no reportado | [PR #9046](https://github.com/qgis/QGIS/pull/9046) | [PR #9058](https://github.com/qgis/QGIS/pull/9058) |
| No se puede añadir WCS - solicitud errónea de WCS | [#21045](https://issues.qgis.org/issues/21045) | [PR #9005](https://github.com/qgis/QGIS/pull/9005) | [PR #9098](https://github.com/qgis/QGIS/pull/9098) |
| Las solicitudes de la API GeoNode requieren un análisis más fuerte de versiones menores | [#21093](https://issues.qgis.org/issues/21093) | [PR #9117](https://github.com/qgis/QGIS/pull/9117) | [PR #9141](https://github.com/qgis/QGIS/pull/9141) |
| Casillas de verificación + Configuración de indicadores en Python en Ubuntu | [#20910](https://issues.qgis.org/issues/20910) | No se puede reproducir con 3.5 |  |
| SAGA openCV y herramientas de procesamiento | [#19540](https://issues.qgis.org/issues/19540) | No se puede reproducir con 3.5 |  |
| Error al copiar registros entre tablas | [#21154](https://issues.qgis.org/issues/21154) | [PR #9065](https://github.com/qgis/QGIS/pull/9065) | [PR #9185](https://github.com/qgis/QGIS/pull/9185) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Solución de errores por Jürgen Fischer
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Attribute table will not allow letter \'N\' to be entered | [#21019](https://issues.qgis.org/issues/21019) | [Direct commit](https://github.com/qgis/QGIS/commit/99904f1f5e7b86a92f3ff50132fd89750fe858e7) | [Direct commit](https://github.com/qgis/QGIS/commit/3d4c6c4e3f3f270d46a419787eb20bd02f8e16d3) |
| Edición de la vista espacial de Oracle en QGIS | [#20109](https://issues.qgis.org/issues/20109) | [Direct commit](https://github.com/qgis/QGIS/commit/855b3b4e26377647de5c5f9d38485f9f00bc9257) | [Direct commit](https://github.com/qgis/QGIS/commit/1b6329c3c03a07e46d9b1c53ccd7bc3b42b3b247) |
| Falta la codificación CP949 (coreana) en el menú Exportar proyecto a DXF | [#20838](https://issues.qgis.org/issues/20838) | [Direct commit](https://github.com/qgis/QGIS/commit/4e74c8b5480ac28aabc3c0b3eba2609d1a762e8a) | [Direct commit](https://github.com/qgis/QGIS/commit/c7a6b773f2a557b4f2082d0ef114edcd043def74) |
| Compatibilidad con GeoPackage Raster WEBP | [#21083](https://issues.qgis.org/issues/21083) |  |  |
| Grass algorithms doesn\'t work from Processing Toolbox level (grass-7.7.svn folder problem) | [#21114](https://issues.qgis.org/issues/21114) | [Direct commit](https://github.com/qgis/QGIS/commit/febbc4f0b9e6f1e1c74c18bcb117148d6587ff87) | [Direct commit](https://github.com/qgis/QGIS/commit/3221b1c83fc00d4f292b2b767a27e4bfcef0f88b) |
| Solucionar ayuda substr | [#21192](https://issues.qgis.org/issues/21192) | [Direct commit](https://github.com/qgis/QGIS/commit/2bed7ab0018696dba76d2c8053d22633a271486e) | [Direct commit](https://github.com/qgis/QGIS/commit/eb8e36c27dad5413936218893393031e7d0a9915) |
| \[OSGeo4W\] introduce with spatialindex 1.9 | Solución en spatialindex | [Direct commit](https://github.com/qgis/QGIS/commit/29d44964529defd0aac94c89e747eee095a89f3a) | [Direct commit](https://github.com/qgis/QGIS/commit/af723c4942427fdce5b935560abd242c5c90ef0a) |
| osgeo4w: fix b6293f23c8c | [#21210](https://issues.qgis.org/issues/21210) | [Direct commit](https://github.com/qgis/QGIS/commit/eea4eda6a35f1a06f84f198249b51b169144c46f) |  |
| Expandir ZipItem en primer plano | [#21268](https://issues.qgis.org/issues/21268) | [Direct commit](https://github.com/qgis/QGIS/commit/407adc761ebe224a2d72df65551cdcf2addf1735) |  |
| importar dwg: capturar la mala interpretación de spline | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/3aa2d9ff9bc673a6c11456524bb7bfb6532556a7) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| importación dwg: admite codificación dxf | [#15999](https://issues.qgis.org/issues/15999) | [Direct commit](https://github.com/qgis/QGIS/commit/e1562a7f1339952be186e924bf96241ce2d826bd) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| importación dwg: forzar polilínea y continuidad de sombreado/anillo | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/b8c727f1d293b64d80c6d1cf29107e0477af3d42) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| Importación dwg/dxf: corrección de ángulo y manejo de alineación de textos(m) | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/92e7faab665d1853191227c8aeb6c13a04c43537) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| importación dwg: solucionar excepción | [#21177](https://issues.qgis.org/issues/21177) | [Direct commit](https://github.com/qgis/QGIS/commit/355deb5905861f263ae7bb03d2bc6fcea4ce5096) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| importación dwg: admite bloques anidados | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/d84c34e0b0ca3586543604a600f939c9024ca99a) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| Importación dwg: maneja la interpretación de sombreado incorrecta | [#20392](https://issues.qgis.org/issues/20392) | [Direct commit](https://github.com/qgis/QGIS/commit/fd15c3e5b6253c2898dd23dd561121ac1874396c) | [Direct commit](https://github.com/qgis/QGIS/commit/3a0f7363087bce639f4429d9099dac48a708ac69) |
| dxf export: arregla la escala de svg | no en redmine | [Direct commit](https://github.com/qgis/QGIS/commit/4b55dbef0b60349c74e40d9fd0109f33bca19510) | [Direct commit](https://github.com/qgis/QGIS/commit/23c01de492546e119d5c1c98f97694f470dbd817) |
| dxf export: reparar la salida de polilíneas 3d cerradas | [#20242](https://issues.qgis.org/issues/20242) | [Direct commit](https://github.com/qgis/QGIS/commit/56ec47328b9e24951b51c00144221c95f88c6c83) | [Direct commit](https://github.com/qgis/QGIS/commit/db823175cf5c89bc066621e34a8d922c2f80eb87) |
| dxf export: don\'t label invisible features | [#19604](https://issues.qgis.org/issues/19604) | [Direct commit](https://github.com/qgis/QGIS/commit/c389fad1ad0396cf9914dedc8d2e9a9c303cd8f8) | [Direct commit](https://github.com/qgis/QGIS/commit/87c9e18e5677d0d6e2c43d7ecb36afab84ff31fb) |
| admite ancho de polilínea y ancho de línea genérico | [#21330](https://issues.qgis.org/issues/21330) | [Direct commit](https://github.com/qgis/QGIS/commit/6bf2d9d4500977c65630add31bb2246f063e20e8) | [Direct commit](https://github.com/qgis/QGIS/commit/c10969e562eda37c0cb78d3ec6db4c1cd68b1106) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Jürgen Fischer](https://www.norbit.de/)
### Prestación: Corrección de Errores por Peter Petrik
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fallo al agregar un campo existente a la capa vectorial | [#18954](https://issues.qgis.org/issues/18954) | [PR #8982](https://github.com/qgis/QGIS/pull/8982) | [PR #9042](https://github.com/qgis/QGIS/pull/9042) |
| Colour bars in colour chooser UI are rendered with interleaved stripes \[MAC\] | [#15984](https://issues.qgis.org/issues/15984) | [PR #9009](https://github.com/qgis/QGIS/pull/9009) | [PR #9020](https://github.com/qgis/QGIS/pull/9020) |
| Imposible cambiar el nombre de un estilo de capa desde el Panel de estilo | [#17652](https://issues.qgis.org/issues/17652) | [PR #9021](https://github.com/qgis/QGIS/pull/9021) | [PR #9041](https://github.com/qgis/QGIS/pull/9041) |
| Las tablas ods no se cargan correctamente en QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | upstream: <https://github.com/OSGeo/gdal/issues/1243> |  |
| QGIS 3.4.2 falla en QgsApplication.initQgis() en Mac | [#20712](https://issues.qgis.org/issues/20712) | No se puede reproducir con 3.5 |  |
| QGIS se congela en MacOS 10.14 cuando se inicia desde Launch Services (funciona bien cuando se inicia desde la terminal) | [#20381](https://issues.qgis.org/issues/20381) | causado por Qt 5.11 utilizado en el paquete oficial de MacOS. Los paquetes deben recrearse con Qt 5.12 |  |
| Geotiff flotante de 32 bits que se muestra en negro. trabajaba en 2.18 y 3.0 - no funciona 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [PR #9035](https://github.com/qgis/QGIS/pull/9035) | [PR #9056](https://github.com/qgis/QGIS/pull/9056) |
| error de Python al ejecutar herramientas GRASS 7.6 en el procesamiento en Mac OS | [#21269](https://issues.qgis.org/issues/21269) | problema en el paquete oficial de MacOS, solución/solución sugerida en el comentario |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Bloqueo reproducible de QGis 3.4 mientras está inactivo | [#20581](https://issues.qgis.org/issues/20581) | [PR #8988](https://github.com/qgis/QGIS/pull/8988) and [PR #9019](https://github.com/qgis/QGIS/pull/9019) | [PR #9027](https://github.com/qgis/QGIS/pull/9027) and [direct commit](https://github.com/qgis/QGIS/commit/9ea7f1efa44c47d4070a1623b18059014e658017) |
| crash at processing\....qgis:snapgeometries | [#18497](https://issues.qgis.org/issues/18497) | [PR #8966](https://github.com/qgis/QGIS/pull/8966) | [PR #9010](https://github.com/qgis/QGIS/pull/9010) |
| QgsExternalResourceWidgetWrapper Falló | [#20140](https://issues.qgis.org/issues/20140) | Duplicado |  |
| Fallo en edición vectorial (que tiene el 4326 CRS) se reproyecta en CRS 3857 | [#19579](https://issues.qgis.org/issues/19579) | [proposed a libspatialindex PR](https://github.com/libspatialindex/libspatialindex/pull/126) |  |
| La adición de nuevas prestaciones en postgis falla con la ventana emergente de la ventana de atributos | [#20523](https://issues.qgis.org/issues/20523) | Trabaja para mí |  |
| Can\'t remove a constraint set on a field once saved | [#20516](https://issues.qgis.org/issues/20516) | [PR #9032](https://github.com/qgis/QGIS/pull/9032) | [PR #9229](https://github.com/qgis/QGIS/pull/9229) |
| QGIS 3.5 no carga o guarda matrices multidimensionales correctamente desde capas PostGIS | [#20872](https://issues.qgis.org/issues/20872) | [PR #9048](https://github.com/qgis/QGIS/pull/9048) | PORHACER. |
| Problema de actualización de la tabla de atributos al eliminar entidades del shapefile | [#18421](https://issues.qgis.org/issues/18421) | [PR #9152](https://github.com/qgis/QGIS/pull/9152) | [PR #9214](https://github.com/qgis/QGIS/pull/9214) |
| QgsVectorLayer del problema de spaceidite featureid | [#20633](https://issues.qgis.org/issues/20633) | Funciona en 3.5 y ramas 3.4 (no en 3.4.4) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Snapping tooltip doesn\'t works when Advanced Digitizing tool is activate | [#18441](https://issues.qgis.org/issues/18441) | No se puede reproducir con 3.5 |  |
| Borrar ajustes antiguos para marcadores de vértices | [#17366](https://issues.qgis.org/issues/17366) | Funciona según lo previsto |  |
| Opciones de ajuste en metros redondeados a enteros | [#20829](https://issues.qgis.org/issues/20829) | [PR #9168](https://github.com/qgis/QGIS/pull/9168) |  |
| Agregar la posibilidad de devolver un shp si ogr no se compila con gpkg | no reportado | [PR #9037](https://github.com/qgis/QGIS/pull/9037) |  |
| Corregir qgsRound para números negativos | [#20861](https://issues.qgis.org/issues/20861) | [PR #9030](https://github.com/qgis/QGIS/pull/9030) and [PR #9025](https://github.com/qgis/QGIS/pull/9025) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)
### Prestación: Corrección de Errores por Victor Olaya
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| algoritmo create grid: problema de punto de referencia para calcular coordenadas Y | [#20966](https://issues.qgis.org/issues/20966) | [Direct commit](https://github.com/qgis/QGIS/commit/e3516ab1b46137db36f3b7dbf4e4f2ee2df1eb70) |  |
| Error en el modelador de Procesamiento | [#20609](https://issues.qgis.org/issues/20609) | Ya no es un problema. No puede reproducir. El reporte ha sido cerrado por el informador original |  |
| No permitir la entrada de archivos para tablas o capas vectoriales si hay campos dependientes | [#21055](https://issues.qgis.org/issues/21055) | [Direct commit](https://github.com/qgis/QGIS/commit/6eaa511eed775ce36328a3e1465c32dfb82507aa) |  |
| Desactivar/desinstalar un complemento provoca un error de Python al intentar editar un modelo de procesamiento | [#19607](https://issues.qgis.org/issues/19607) | [PR #8957](https://github.com/qgis/QGIS/pull/8957) |  |
| El selector de base de datos Postgis para salidas falla listando esquemas de la base de datos seleccionada | [#21099](https://issues.qgis.org/issues/21099) | [PR #9004](https://github.com/qgis/QGIS/pull/9004) |  |
| Regresión: las salidas de los modelos de procesamiento no tienen asignados los estilos especificados | [#20573](https://issues.qgis.org/issues/20573) | [Direct commit](https://github.com/qgis/QGIS/commit/eb47288fac06692748c7017f6f125a1fc66e9561) |  |
| QGIS3: SagaUtils.py falla cuando el comando contiene caracteres no latinos | [#18617](https://issues.qgis.org/issues/18617) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] Wrong management of locale in output result path | [#19351](https://issues.qgis.org/issues/19351) | [PR #8968](https://github.com/qgis/QGIS/pull/8968) |  |
| \[processing\] SAGA algorithms cannot produce non-shp output | [#21089](https://issues.qgis.org/issues/21089) | [PR #9002](https://github.com/qgis/QGIS/pull/9002) |  |
| El selector de extensión muestra capas sin componente espacial (tablas sin geometría) | [#21129](https://issues.qgis.org/issues/21129) | [PR #9034](https://github.com/qgis/QGIS/pull/9034) (updated by Nyall in [PR #9038](https://github.com/qgis/QGIS/pull/9038)) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Esta prestación fue desarrollada por Victor Olaya
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Geotiff flotante de 32 bits que se muestra en negro. trabajaba en 2.18 y 3.0 - no funciona 3.4 | [#20493](https://issues.qgis.org/issues/20493) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/e261b7ff4fa15e762f7f3a73ff3dbc965181d991) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/0a3d241f96e83b86073efc86b51376c7cd5f6e4f) | - |
| Las tablas ods no se cargan correctamente en QGIS 3.4 | [#20588](https://issues.qgis.org/issues/20588) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/ee6278f8dd1be7064db87be87fe31fa8943730ec) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/4e84cd44868e3b91def41057b7adf28767b4c273) | - |
| attributes in attribute table don\'t match attribute in identify results/labels with WFS layer | [#20865](https://issues.qgis.org/issues/20865) | [PR #9105](https://github.com/qgis/QGIS/pull/9105) | [PR #9113](https://github.com/qgis/QGIS/pull/9113) |
| Error en la carga de KML | [#20173](https://issues.qgis.org/issues/20173) | [GDAL master commit](https://github.com/OSGeo/gdal/commit/467b088edd18f90744bccac9ff6d83a6a5d92d93) and [GDAL 2.4 in](https://github.com/OSGeo/gdal/commit/ec4bd32cd591b672274383f7c06da1d58a2a3500) | - |
| Zoom a la capa no responde a WFS filtrados | [#20742](https://issues.qgis.org/issues/20742) | [PR #9118](https://github.com/qgis/QGIS/pull/9118) | [Direct commit](https://github.com/qgis/QGIS/commit/8834ec78207c091175cb0f48b518b6d2988f337d) |
| Tiempo de procesamiento para GeoJSON 10 veces mas lento en 3.4 | [#21085](https://issues.qgis.org/issues/21085) | [GDAL master commmit](https://github.com/OSGeo/gdal/commit/bd668db37eb6f176226ebbe7efe34cfac86a3cf6a) and [GDAL 2.4 commit](https://github.com/OSGeo/gdal/commit/d6c38adfa28f75da0630f3e3ac26dbb501fc361e) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Prestación: Corrección de Errores por Martin Dobias
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[vertex tool\] Fix issue with hidden layers being editable | [#18434](https://issues.qgis.org/issues/18434) | [PR #8992](https://github.com/qgis/QGIS/pull/8992) | [Direct commit](https://github.com/qgis/QGIS/commit/2ad47198c446a1f541dca195439bb432da0dce6a) |
| \[vertex tool\] Fix vertex addition to polygon\'s first segment | [#20774](https://issues.qgis.org/issues/20774) | [PR #9024](https://github.com/qgis/QGIS/pull/9024) | [Direct commit](https://github.com/qgis/QGIS/commit/4423caff0994de64185fcc7b3acb5058ca047c14) |
| \[vertex tool\] Misleading message when deleting all nodes of a ring or a part | [#17754](https://issues.qgis.org/issues/17754) | ¡no arreglado! necesita una solución bastante complicada de hacer |  |
| \[vertex tool\] Improvements to the right-click behavior to pick locked feature | N/D | [PR #9052](https://github.com/qgis/QGIS/pull/9052) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] right-click to loop through editable features | N/D | [PR #9087](https://github.com/qgis/QGIS/pull/9087) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] misc small UX improvements | N/D | [PR #9116](https://github.com/qgis/QGIS/pull/9116) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] two more UX fixes | N/D | [PR #9130](https://github.com/qgis/QGIS/pull/9130) | [PR #9161](https://github.com/qgis/QGIS/pull/9161) |
| \[vertex tool\] Few more UX improvements | [#21283](https://issues.qgis.org/issues/21283) | [PR #9222](https://github.com/qgis/QGIS/pull/9222) | [PR #9227](https://github.com/qgis/QGIS/pull/9227) |

This feature was funded by [QGIS user group Germany](https://www.qgis.de/)

This feature was developed by [Martin Dobias](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[postgis\] Fix creation of new Z/M enabled, curved geometry type layers | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/07746dbc0e5b34e31e85e944fc6f53113721a696) | [Direct commit](https://github.com/qgis/QGIS/commit/a61abe5bb3b4c1b633f2f76b69a7f274abeb33d3) |
| \[categorized\] Fix blank layers when using categorized renderer | [#21188](https://issues.qgis.org/issues/21188) | [Direct commit](https://github.com/qgis/QGIS/commit/7714bfbfbe6acec1c193365a173c822cb72c4361) | N/D |
| Corregir mensaje de origen de datos no válido siempre se muestra después de arrastrar y soltar capas vectoriales a la ventana QGIS | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/a1d8d9ae5d8ff5130e3ccd179617b1e9c0bf4062) | N/D |
| \[processing\] Buffer algorithm should always export multipolygon layers | [#21191](https://issues.qgis.org/issues/21191) | [Direct commit](https://github.com/qgis/QGIS/commit/f22f182bcfd7b7f5b5d8f782f3df08ee9d705115) | [Direct commit](https://github.com/qgis/QGIS/commit/f4866402f7ecf759598e652d5d640dd1fdc48c50) |
| \[processing\]\[gdal\] Fix polygonize field name is ignored | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/06d5b996bfc37f2877ecbf708af608952420ed45) | [Direct commit](https://github.com/qgis/QGIS/commit/ae21d07d4b082ede7b56941aaa1ce57fad8cdb9a) |
| \[processing\] Allow matrix parameters to be correctly set for model child algorithms | [#20914](https://issues.qgis.org/issues/20914) | [Direct commit](https://github.com/qgis/QGIS/commit/eeff02fc14b96a6d3f95ac2122d1d82654dcf268) | [Direct commit](https://github.com/qgis/QGIS/commit/d5900557bdb25f4e285638bf1de85f43430ba15d) |
| \[processing\]\[gdal\] Ensure that GDAL algs output the CORRECT generated filename for outputs | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/c93775f6b177ab2f64bd347c9a6f78896cee78dd) | [Direct commit](https://github.com/qgis/QGIS/commit/93c135f97cad06a1ff703ae1839397f14cb82b3d) |
| \[processing\]\[gdal\] Fix incorrect definition of gdal_warp extra_param parameter | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/f54f5a4fe70792f4d7ea376e28edad88c4d35d4a) | N/D |
| Permitir el cálculo exacto del tamaño de los símbolos con variadas unidades de capas | [#21143](https://issues.qgis.org/issues/21143) | [Direct commit](https://github.com/qgis/QGIS/commit/867e39947b3f24d0b7714cd44e28126b61769340) | [Direct commit](https://github.com/qgis/QGIS/commit/33987fa5505ebc4cb9d83c195c49e5938f7c1f73) |
| Se corrige el bloqueo cuando se solicitan las credenciales de WMS | [#20826](https://issues.qgis.org/issues/20826) | [Direct commit](https://github.com/qgis/QGIS/commit/c9e761649820f8444a41da5e18850061b207c09c) | [Direct commit](https://github.com/qgis/QGIS/commit/ad6e1566a70d4f1a9d959a4de9f18bcae9dbd566) |
| Solucionados diversos bloqueos/bloqueos en las solicitudes de red, especialmente cuando se producen errores de SSL o tiempos de espera | Múltiple | Múltiple | N/A \-- too intrusive |
| \[processing\]\[saga\] Fix definition of Multiple regression points/grids alg | [#21146](https://issues.qgis.org/issues/21146) | [Direct commit](https://github.com/qgis/QGIS/commit/4f8e2317d796881f942bbc6bdcbe60f3470f48fe) | [Direct commit](https://github.com/qgis/QGIS/commit/1916a7fd7ae4a3d5bb767bde76f3042dfd0a7474) |
| \[processing\] do not show geometryless layers in extent selector | [#21129](https://issues.qgis.org/issues/21129) | [Direct commit](https://github.com/qgis/QGIS/commit/5bfec27938ff95cd65c1cf5b88cc13ce26ca1d5d) | [Direct commit](https://github.com/qgis/QGIS/commit/06ee13263d842ea0d7e188107cb9033893b6c75f) |
| \[layouts\] Add checkbox to disable raster tiling for PDF/SVG exports | [#19500](https://issues.qgis.org/issues/19500) | [Direct commit](https://github.com/qgis/QGIS/commit/60b8d05278cd8133e1c06108ba875960d56e90e5) | N/A \-- too intrusive |
| Corregir cadenas vacías en proxy excluye resultados de lista en proxy skippe\\d para TODOS los hosts | [#20213](https://issues.qgis.org/issues/20213) | [Direct commit](https://github.com/qgis/QGIS/commit/cf1cf0fe455a42edf6db4ab9fa07c1ad641b16cb) | [Direct commit](https://github.com/qgis/QGIS/commit/34625110327c5bec4969c2a42cfa8c210bd3b630) |
| Evitar que el proyecto se marque como sucio tan pronto como se abre | N/D | [Direct commit](https://github.com/qgis/QGIS/commit/394e5d8d76480c1235c49e46d52f5f4a277cf824) | N/D |
| Corregir la pérdida del proyecto al guardar en formato QGZ y la ruta contiene caracteres no ascii | [#19567](https://issues.qgis.org/issues/19567) | [Direct commit](https://github.com/qgis/QGIS/commit/7d7462c33334a501167813d720fb2589d3c579ec) | [Direct commit](https://github.com/qgis/QGIS/commit/bfef851b1ca98a2c45117a2b1f911f7f1b7155b1) |
| Corregida la evaluación de las propiedades definidas por datos para los subsímbolos de los subsímbolos | [#18384](https://issues.qgis.org/issues/18384) | [Direct commit](https://github.com/qgis/QGIS/commit/9cf2ff31d86e6b7671aaca137a60a7b7a975ef62) | [Direct commit](https://github.com/qgis/QGIS/commit/7e25cea7e939248c8816d2739ccd44a31c606f11) |
| Fix shortest path algorithm can \"shortcut\" when using network in geographic coordinates | [#20997](https://issues.qgis.org/issues/20997) | [Direct commit](https://github.com/qgis/QGIS/commit/e75a88825665e7bb43c6c3cd1b2c22037cd29784) | [Direct commit](https://github.com/qgis/QGIS/commit/a3428e5f92b8b98cc753de0e9366f36e7ecc018e) |
| Corregido que la tarea de carga del proyecto nunca se completa cuando el proyecto tiene capas incrustadas | [#21012](https://issues.qgis.org/issues/21012) | [Direct commit](https://github.com/qgis/QGIS/commit/7ad4b05112af0c35bd9a8e0526e8823a6b695335) | [Direct commit](https://github.com/qgis/QGIS/commit/6584fb295aed03c3167d056e1bac59a808a1abb5) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Prestación: Corrección de errores por hugo Mercier
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Qgis 3.4.1 se bloquea al acceder a métodos de función | [#20752](https://issues.qgis.org/issues/20752) | Cerrado |  |
| Solicitud de tamaño incorrecto con un ráster georreferenciado | [#8272](https://issues.qgis.org/issues/8272) | Can\'t reproduce anymore in 3.5 |  |
| Postgresql: SAVEPOINTS vacío | http://issues.qgis.org/issues/17535 | no aplicable nunca más |  |
| El widget de rango no respeta el valor predeterminado en una columna no nula | [#20831](https://issues.qgis.org/issues/20831) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) and [PR #9033](https://github.com/qgis/QGIS/pull/9033) |  |
| El widget de rango proporciona un valor NULL en la tabla de atributos/formulario | [#21125](https://issues.qgis.org/issues/21125) | [PR #9033](https://github.com/qgis/QGIS/pull/9033) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| QGIS 3.4.1 modificación avanzada y bloque snap de QGIS | [#20568](https://issues.qgis.org/issues/20568) | Cerrado |  |
| Los marcadores de vértice no se muestran correctamente para las funciones MultiPolygon | [#19909](https://issues.qgis.org/issues/19909) | [PR #9036](https://github.com/qgis/QGIS/pull/9036) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |
| Controles en cascada en formularios | [#11264](https://issues.qgis.org/issues/11264) | triaje, cerrado |  |
| \$length incorrect in expressions | [#19355](https://issues.qgis.org/issues/19355) | [PR #9063](https://github.com/qgis/QGIS/pull/9063) | [PR #9192](https://github.com/qgis/QGIS/pull/9192) |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Hugo Mercier](https://oslandia.com/)

{{<content-end >}}
