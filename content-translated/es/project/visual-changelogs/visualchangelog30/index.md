---
HasBanner: false
draft: false
releaseDate: '2018-02-23'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.0
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.0{#changelog30 }
![image1](images/projects/8c7c6c5ded71fa7284d9e31144e2c0cdb02059ee.png)

Fecha de lanzamiento: 2018-02-23

The greatest QGIS release ever! QGIS 3.0 is a huge overhaul and cleanup of our beloved Open Source GIS. QGIS 3.0 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations](http://www.qgis.org/en/site/getinvolved/donations.html?highlight=donate), [sponsorship](http://www.qgis.org/en/site/getinvolved/governance/sponsorship/sponsorship.html) or contributions to the code documentation, web site and so on.

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Patrocinadores para QGIS versión 3.0
{{<fund type="changelog" relativeImgPath=true >}}
### Característica: Eliminar el complemento convertidor dxf2shp
Esta funcionalidad está disponible en OGR y ya no es necesario un complemento QGIS dedicado para realizar esta tarea.
### Característica: Eliminar el complemento de trama oráculo huérfano
### Característica: eliminar el proveedor TauDEM del procesamiento central
TauDEM es un conjunto de herramientas bastante específico y requiere la instalación de algunas herramientas adicionales. Por lo tanto, decidimos convertirlo en un proveedor separado, reduciendo el tamaño de la base de código central y los esfuerzos de mantenimiento.
### Característica: más ayuda y posibilidad de configurar la ubicación de los archivos de ayuda de QGIS
Se agregaron más botones de Ayuda para algoritmos y cuadros de diálogo y ahora apuntan a la Documentación QGIS en línea.

La configuración permite acceder a la ayuda contextual almacenada en línea, en la red de la organización o en una computadora local. También es posible combinar diferentes fuentes de ayuda.

![image112](images/entries/7c17e43c0c6738c9588f3bef149ca7f3d8a13948.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Característica: migrar los controles Foto, VistaWeb y NombreArchivo a Adjunto
![image113](images/entries/d2e949a9804de76d196af6e58996165d01350fec.jpeg.400x300_q85_crop.webp)
### Característica: Se eliminaron los proveedores de otb y lidartools del procesamiento
La nueva lógica será desarrollar proveedores de complementos que puedan seguir el ciclo de vida del software externo.
## Interfaz de usuario
### Característica: Habilitar muelles flotantes con pestañas
For qt \> 5.6 builds, it is possible to drop several floating docks in the same floating window where they appear as tabs <https://woboq.com/blog/qdockwidget-changes-in-56.html>

![image66](images/entries/02137f3073c3f8a32bc505bd4916a8df751db79f.gif)
### Característica: Añadiendo soporte para zoom con la rueda del mouse para resolución fina
Algunos dispositivos de mouse/puntero (especialmente en Mac) tienen resoluciones más finas. Envían eventos de rueda del mouse a una frecuencia alta pero con valores delta más pequeños. Hacer zoom con dichos dispositivos era inutilizable para acciones de zoom rápido. Esto se ha solucionado en 3.0.

Esta prestación fue desarrollada por Matthias Kuhn
### Característica: añadiendo la barra de búsqueda al cuadro de diálogo Configurar accesos directos
Admite la búsqueda por nombre de acción y acceso directo

![image67](images/entries/5f9439417546fff26fe410b5a860a7680b07c53e.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Característica: barra de localización
La barra de localización es un servicio de búsqueda rápido, siempre listo, genérico y conectable en la esquina inferior izquierda de QGIS.

Actualmente es capaz de buscar algoritmos, acciones y nombres de capa, pero también puede seleccionar una característica en la capa activa actual escribiendo un valor de atributo.

It is \'easy\' extendable, so everybody can create a QgsLocatorFilter for his/her national geocoding service or other search online or database search facility.

![image68](images/entries/c5eba5f5e5a6745d1a81df88eb55f01a68fcc1ad.gif)

Esta prestación fue desarrollada por Nyall Dawson
### Característica: más edición en línea sin bloqueo
- escala de la unidad de mapa
- elaborador de color y editores de rampa aleatorios limitados
- Edición de colores en una lista de colores en línea en el panel de estilo
- edición en línea de colores y símbolos en compositor

ahora se muestra en línea en el panel de estilo
### Característica: Agregue una opción para mostrar los menús de esquemas de color del usuario
Esto agrega la capacidad para que los usuarios establezcan si un esquema de color creado por el usuario debe aparecer en los menús desplegables del botón de color.

It\'s accessed through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option.

Esto es útil si tiene conjuntos de paletas comunes y desea que estén disponibles al instante a través del menú de color.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Opción de decoración con color para la flecha de norte en la vista del mapa
Opción color ha sido añadida para decorar todas las flechas del norte para todas las vistas de mapa.

![image69](images/entries/6a3fa6fb065a02defaa42440f301847e8fbbeb75.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Feature: Improved map canvas\' save as image
The map canvas\' save as image function has been expanded and now offers users the possibility to tweak the scale, resolution, and extent on-the-fly. Extents can be restricted to a height-width ratio. A save as PDF function was also added to quickly export the map canvas into a resolution-independent PDF.

![image70](images/entries/a2adf1e9930f23fa739e68a6e2c55e1b553867b9.png.400x300_q85_crop.webp)

Esta prestación fue fundad por Andreas Neumann (fundación parcial)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: alternar la visibilidad de los paneles abiertos en la ventana principal
Accessible via: - View menu \> Toggle Panels Visibility - **Ctrl+Tab** keyboard shortcut

![image71](images/entries/68249b50c2813f4b204cb0305587b2850e7cd61e.gif)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: mejorada consistencia a la interfaz de usuario
This work sponsored by the QGIS grant program on \"adding consistency to UI controls\" is now complete and merged into master. The following tasks were done as part of this work:
- Toda la API con respecto a **transparencia/opacidad/alfa** se estandarizó a **setOpacity()** y **opacity()**. Los métodos toman un valor double entre 0 (transparente) y 1 (opaco), manteniendo la coherencia con la API Qt.
- Se creó un **nuevo widget QgsOpacityWidget**, y ahora se usa en cualquier parte a través de la interfaz de usuario donde se configura la opacidad. Esto garantiza un comportamiento constante y busca controles de opacidad en todas partes.
- **La rotación** se ha estandarizado en la API y la interfaz de usuario, por lo que ahora la rotación siempre se aplica en el sentido de las agujas del reloj. Todos los widgets de rotación se han actualizado para que acepten valores de -360 a 360.
- Los proyectos de 2.x con etiquetado mediante rotación y rotación definida por datos se **actualizan** limpiamente al abrirse en 3.0
- Las API de escala se han hecho consistentes en toda la API de QGIS. **Se ha eliminado la confusa combinación de denominadores de escala frente a escalas reales**, y ahora todo funciona en denominadores de escala. El comportamiento de todas las llamadas de rango de escala está estandarizado con un significado común para escalas mínimas/máximas (y documentación de API explícita al respecto)
- Todos los controles de escala ahora usan los widgets de escala estándar para lograr consistencia en la IU
- El etiquetado ahora usa la misma definición de escala mínima/máxima que el resto de la interfaz de usuario, y los proyectos existentes se actualizan de forma limpia al abrirse en 3.0.
- Se corrigieron los errores más importantes relacionados con el uso de la escala, incluidos los errores que rompen los límites de escala basados en normas

¡Gracias al PSC de QGIS y a los donantes del proyecto por patrocinar este trabajo permitiendo que continúe!

Esta prestación fue fundado por Patrocinadores y Donantes de QGIS

This feature was developed by [Nyall Dawson](https://north-road.com)
### Prestación: Capas abiertas en un solo grupo
Si trata de abrir muchas subcapas, ahora puede abrir todas ellas en el mismo grupo en la leyenda.

![image72](images/entries/a64155774fee81370dfb5a786cf7386bffb7a089.png.400x300_q85_crop.webp)

This feature was funded by [Kartoza](http://www.kartoza.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
## Objetos 3D
### Prestación: vista de mapa 3D y generación de terreno
¡Tenemos una nueva vista de mapa 3D nativa en QGIS! La vista de mapa en 3D muestra un mapa en 2D (renderizado desde las capas del proyecto) en la parte superior del terreno. Por defecto, el terreno es un plano plano, pero es posible utilizar capas ráster con el modelo digital de elevaciones como fuente de datos de altura.

Use menu View \> New 3D Map View to add a 3D view of the project. This will create a new dock widget with 3D map canvas. The 3D view uses the same controls like 2D map views to browse the map using mouse (drag map to move it around, mouse wheel to zoom) or keyboard arrow keys. In addition there are camera controls specific to 3D views: it is possible to rotate and tilt camera by one of the following ways:
- arrastrando el mouse con el botón central del mouse presionado
- presionando shift y arrastrando el ratón con el botón izquierdo pulsado
- presionando shift  y usando las teclas arriba/abajo/izquierda/derecha

![image121](images/entries/86e6303419d84812266eada5327e74dbc6d507a4.jpg.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Renderizadores 3D para capas de mapa
En la configuración predeterminada, las capas del mapa se representan en imágenes de mapa 2D en la parte superior del terreno. Sin embargo, es posible hacer un mejor uso del mundo 3D configurando renderizadores 3D para algunas capas de mapa. Con los renderizadores 3D, los datos se pueden mostrar en vistas 3D como verdaderos objetos 3D; esto es actualmente compatible con capas vectoriales (todos los tipos de geometría: punto, línea o polígono). Esto permite una visualización mucho mejor, por ejemplo:
- los polígonos con huellas de construcciones pueden extruirse (posiblemente con una altura definida por datos) para lograr un aspecto 3D
- los puntos con ubicaciones puntuales de arboles se pueden representar con símbolos 3D de árboles (formas geométricas simples o modelos 3D existentes cargados desde un formato de archivo compatible)

Para configurar los renderizadores 3D, use el widget de acoplamiento de estilo de capa o el cuadro de diálogo de propiedades de capa vectorial: hay una nueva pestaña para la configuración de los renderizadores 3D.

![image122](images/entries/311f1b52d068ccca9ef74f9ea1dcba259c7ed674.png.400x300_q85_crop.webp)

This feature was funded by [QGIS.ORG](https://qgis.org/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Expresiones
### Prestación: Nuevas variables de expresión
Adds `@project_crs` and `@project_crs_definition` variables for retrieving the current project CRS
### Feature: new global expression variable \@qgis_locale
Devuelve la configuración local actual utilizada por QGIS. Por defecto, esta es la configuración local actual del sistema. Si el usuario habilitó la anulación de la configuración local en QGIS, se devolverá la configuración local anulada.

![image63](images/entries/23e0bd2bc2cd560dad2d2a873e7d9ab98c532fb0.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Nuevas variables de expresión para la configuración del mapa
    - map_crs, map_crs_definition: retrieves crs details for map
    - map_units: retrieves units for map (eg 'meters','degrees')
    
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevas funciones de expresión
**Atlas expressions**
- **atlas_layerid** and **atlas_layername**: Returns layer ID and layer name of the current layer in the atlas.

**Aggregate expressions**
- **array_agg(expression, group_by, filter)**: Returns an array of aggregated values from a field or expression.

**Array expressions**

New group that contains expression functions for the creation and manipulation of arrays (also known as list data structures). The order of values within the array matters, in contrary to the \'map\' data structure, where the order of key-value pairs is irrelevant and values are identified by their keys.
- **array(value1, value2, ...)** : Returns an array containing all the values passed as parameter.
- **array_append(array, value)**: Returns an array with the given value added at the end.
- **array_cat(array1, array2, ...)**: Returns an array containing all the given arrays concatenated.
- **array_contains(array, value)**: Returns true if an array contains the given value.
- **array_distinct(array)**: Returns an array containing distinct values of the given array.
- **array_find(array, value)**: Returns the index (0 for the first one) of a value within an array. Returns -1 if the value is not found.
- **array_first(array)**: Returns the first value of an array.
- **array_get(array, index)**: Returns the Nth value (0 for the first one) of an array.
- **array_insert(array, pos, value)**: Returns an array with the given value added at the given position.
- **array_intersect(array1, array2)**: Returns true if any element of array1 exists in array2.
- **array_last(array)**: Returns the last value of an array.
- **array_length(array)**: Returns the number of elements of an array.
- **array_prepend(array, value)**: Returns an array with the given value added at the beginning.
- **array_remove_all(array, value)**: Returns an array with all the entries of the given value removed.
- **array_remove_at(array, pos)**: Returns an array with the given index removed.
- **array_reverse(array)**: Returns the given array with array values in reversed order.
- **array_slice(array, start_pos, end_pos)**: Returns a portion of the array. The slice is defined by the start_pos and end_pos arguments.
- **array_to_string(array, delimiter, empty_value)**: Concatenates array elements into a string separated by a delimiter using and optional string for empty values.
- **regexp_matches(string, regex, empty_value)**: Returns an array of all strings captured by capturing groups, in the order the groups themselves appear in the supplied regular expression against a string.
- **string_to_array(string, delimiter, empty_value)**: Splits string into an array using supplied delimiter and optional string for empty values.

**Color expressions**
- **create_ramp(map, discrete)**: Returns a gradient ramp from a map of color strings and steps.

**Date and Time expressions**
- **epoch(date)**: Devuelve el intervalo en milisegundos entre la época Unix y un valor de fecha dada.

**General expressions**
- **env(name)**: Obtiene una variable de entorno y devuelve su contenido como una cadena. Si no se encuentra la variable, se devolverá NULL.
- **raster_statistic(layer, band, property)**: Returns statistics from a raster layer. Properties: min/max/avg/range/stdev/sum
- **with_variable(name, value, node)**: This function sets a variable for any expression code that will be provided as 3rd argument. This is only useful for complicated expressions, where the same calculated value needs to be used in different places.

**Geometry expressions**
- **extend(geometry, start_distance, end_distance)**: Extends linestrings by a specified amount at the start and end of the line
- **hausdorff_distance(geometry a, geometry b, densify_fraction)**: Returns the Hausdorff distance between two geometries. This is basically a measure of how similar or dissimilar 2 geometries are, with a lower distance indicating more similar geometries.
- **inclination(inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.
- **make_circle(center, radius, segment)**: Creates a circular, segmentized, polygon.
- **make_ellipse(center, semi_major_axis, semi_minor_axis, azimuth, segment)**: Creates an elliptical, segmentized, polygon.
- **make_regular_polygon(center, radius, number_sides, circle)**: Creates a regular polygon.
- **make_triangle()**: help still missing
- **minimal_circle(geometry, segment)**: Returns the minimal enclosing circle of a geometry. It represents the minimum circle that encloses all geometries within the set.
- **offset_curve(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by offsetting a linestring geometry to the side. Distances are in the Spatial Reference System of this geometry.
- **oriented_bbox(geom)**: Returns a geometry which represents the minimal oriented bounding box of an input geometry.
- **pole_of_inaccessibility(geometry, tolerance)**: Calculates the approximate pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance.
- **simplify(geometry, tolerance)**: Simplifica una geometría eliminando nodos utilizando un umbral basado en la distancia (es decir, el algoritmo Douglas Peucker). El algoritmo conserva grandes desviaciones en las geometrías y reduce el número de vértices en segmentos casi rectos.
- **simplify_vw(geometry, tolerance)**: Simplifies a geometry by removing nodes using an area based threshold (the Visvalingam-Whyatt algorithm). The algorithm removes vertices which create small areas in geometries, e.g., narrow spikes or nearly straight segments.
- **smooth(geometry, iterations, offset, min_length, max_angle)**: Smooths a geometry by adding extra nodes which round off corners in the geometry.
- **single_sided_buffer(geometry, distance, segments, join, miter_limit)**: Returns a geometry formed by buffering out just one side of a linestring geometry. Distances are in the Spatial Reference System of this geometry.

**Layer Property**
- **crs_description** returns the CRS description of the layer.

**Map Expressions**

This group contains expression functions for the creation and manipulation of \'map\' data structures (also known as dictionary objects, key-value pairs, or associative arrays). One can assign values to given keys. The order of the key-value pairs in the map object is not relevant.
- **map(key1, value1, key2, value2, , ...)**: Returns a map containing all the keys and values passed as pair of parameters.
- **map_akeys(map)**: Returns all the keys of a map as an array.
- **map_avals(map)**: Returns all the values of a map as an array.
- **map_concat(map1, map2, ...)**: Returns a map containing all the entries of the given maps. If two maps contain the same key, the value of the second map is taken.
- **map_delete(map, key)**: Returns a map with the given key and its corresponding value deleted.
- **map_exist(map, key)**: Returns true if the given key exists in the map.
- **map_get(map, key)**: Returns the value of a map, given it\'s key.
- **map_insert(map, key, value)**: Returns a map with an added key/value.

**Map Layers**

Nuevo grupo que contiene una lista de capas de mapa disponibles en el proyecto actual. Devuelve los identificadores internos de la capa del mapa. Esto se usa en muchas otras funciones de expresión que hacen referencia a las capas del mapa.

**Math expressions**
- **inclination(point_a, point_b)**: Returns the inclination measured from the zenith (0) to the nadir (180) on point_a to point_b.

**Operators**
- **\~:** Performs a regular expression match on a string value.

**Record and Attributes Expressions**

renamed from just \"Record\"
- **get_feature_by_id(layer, feature_id)**: Returns the feature with an id on a layer.
- **is_selected(feature, layer)**: Returns if a feature is selected. If called with no parameters checks the current feature.
- **num_selected(layer)**: Returns the number of selected features on a given layer. By default works on the layer on which the expression is evaluated.
- **represent_value(value, fieldName)**: Returns the configured representafftion value for a field value. It depends on the configured widget type. Often, this is useful for \'Value Map\' widgets.
- **uuid()**: Genera un identificador único universal(UUID) para cada fila utilizando el método Qt QUuid::createUuid. Cada UUID tiene 38 caracteres de longitud.

**Relations**

New group listing all available table relations in a project. Useful for relation_aggregate functions.

**Deprecated**
- **\$scale**: old variable to get current map scale. Replaced by **maps_scale**

**Changes**
- Cambio en la función **substr()**
  - support negative start value (e.g. substr(\'hello\',-2) returns \'lo\')
  - support negative length value (e.g. substr(\'hello\',3,-1) returns \'ll\')
  - length parameter now optional, defaults to end of string (e.g. substr(\'hello world\',7) returns \'world\')
- **strpos()** ahora se basa en una cadena simple dentro de una búsqueda de cadena
- **regexp_match()** now returns pos of a matching regular expression

Esta prestación fue desarrollada por numerosos desarrolladores.
### Feature: Expose \@parent variable in aggregate functions
This makes it possible to access attributes and geometry from the parent feature when in the filter of the \"aggregate\" expression function. With this in place aggregates can be calculated per feature.

    E.g. max "measurement" for each point_station per polygon_research_area.
    
O un valor por defecto del atributo mientras digitalizamos entidades:

`aggregate(layer:='countries', aggregate:='max', expression:=\"code\", filter:=intersects( $geometry, geometry(@parent) ) )`

![image64](images/entries/7666e6f1fd7a95ec3e099c27c6bf9ef6b145c956.jpeg.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://opengis.ch)
### Feature: Item_variables expression function inside compositions
This adds a new item_variables expression function when expressions are used inside a composition context.

La función toma un solo argumento, la identificación de un elemento dentro de la composición, y devuelve un mapa del nombre de la variable al valor de ese elemento. Esto le permite hacer cosas como insertar texto en una etiqueta propiedades de otro elemento en la composición, por ejemplo

Insertar la escala del mapa en una etiqueta:

`map_get( item_variables( 'map'),'map_scale')`

Insertar coordenada central x del mapa en una etiqueta:

`x(map_get( item_variables( 'map'),'map_extent_center'))`

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Documentación
### Prestación: Mejoras de algortimos de procesamiento
Los algoritmos de procesamiento han sido revisados y documentados. Al hacer clic en el botón Ayuda, se abrirá el sitio web de QGIS y se mostrará la descripción del algoritmo con documentación e imágenes mejoradas.

![image65](images/entries/ca710bbcb3e67a83217d5894ccccfcb5103b1bf4.png.400x300_q85_crop.webp)

Esta prestación fue fundada por  Subvenciones de QGIS a Propuestas

This feature was developed by [Matteo Ghetta (Faunalia), Alexander Bruy](http://www.faunalia.eu/)
## Simbología
### Prestación: Visibilidad de capa de símbolos definida por datos
Adds a data defined override to control a symbol layer\'s visibility. Allows users to disable drawing certain symbol layers for matching features.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: guardar y restaurar rampa de color usada para renderizado de banda única pseudocolor
Esta funcionalidad fue desarrollada por Alexander Bruy
### Característica: Añadir puntos y pulgadas a las unidades de símbolos disponibles
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: Nuevo widget de botón de rampa de color
In QGIS 3.0, handling of color ramps has gotten much better via a newly introduced color ramp button widget. Improvements include: - custom color ramp settings are remembered when projects are re-opened - color ramp inversion is implemented within the widget, enabling this action across QGIS - quick access to \"favorite\" color ramps within the widget pop-up menu - interfacing with catalogs (cpt-city and ColorBrewer) is now much more pleasant

![image73](images/entries/547ffa26f79435ff28198820bb0d95dc495b4f13.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Gestión de reelaboración y actualización de estilos
La adinistración del estilo ha recibido una importante actualización. Las mejoras incluyen:
- Se agregó un nuevo sistema de agrupación favorito, que el widget de lista de símbolos predeterminado
- La etiqueta/grupo inteligente seleccionado en el widget de la lista de símbolos ahora persiste al cambiar de capa (y entre sesiones)
- El widget de la lista de símbolos actualizará el cuadro combinado etiqueta/grupo inteligente cuando los usuarios agreguen/cambien de nombre/eliminen categorías
- Los usuarios ahora pueden etiquetar directamente, así como agregar a favoritos símbolos mientras los guardan en la base de datos de estilos
- Para agilizar la administración del estilo, los grupos se han eliminado y reemplazado completamente por etiquetas
- Se han integrado las etiquetas en la interfaz de usuario import/export

![image74](images/entries/bb43cc8a048018b0f54463674ebf2d11bb0abc21.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Soporte de ajuste de color y transparencia en elementos múltiples para renderizadores raster
It is now possible to change the color and transparency for multiple values at the same time for the singleband pseudocolor and the paletted renderers. Simply select values within the values\' list and right click to have a pop-up menu appear.

![image75](images/entries/dc60a3f5fdc3a6568e8f3b9bf635066fcde9926d.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Mostrar un deslizante alfa en el menú desplegable del botón de color
Permite ajustes rápidos para el color alfa

![image76](images/entries/669437f416c6ef5c18dd87ecdfc52772e0b597c7.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: Soporte de acciones de barra de herramientas de trama ráster para el renderizador de pseudocolor
Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: Soporte de transparencia para el renderizador paletizado
QGIS 3.0, ahora es posible cambiar el valor de transparencia a valores únicos para el renderizador paletizado.

![image77](images/entries/603b73fbf8ad7db9cdb43689641eb70326c11bbf.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Auto-estiramiento del ráster al actualizar la vista de mapa
see <https://lists.osgeo.org/pipermail/qgis-developer/2016-September/044393.html> follow up to raster pseudocolor updated extent auto classification.

Esta prestación fue desarrollada por Even Rouault
### Prestación: Control sobre contenido de anotaciones marginales
Permite ajuste marginal izquierdo/superior/derecho/inferior para los contenidos dentro de una anotación.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Las anotaciones se pueden estilizar usando estilos de símbolos rellenos
This changes the rendering of annotation frames to use QGIS\' symbology engine, which means that all the existing fill styles can now be used to style annotation frames.

Tambien efectos de pintura y parámetros de símbolos definidos.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Renderizador de grupos de puntos
Nuevo procesador de símbolos que agrupa los puntos cercanos representados en un solo símbolo marcador. Opcionalmente, una etiqueta muestra el número de entidades que se han agregado en el símbolo único.

Adicionálmente, se han hecho algunas mejoras al renderizador de desplazamiento de puntos, mas específicamente:
- points are now assigned to the group which is \"nearest\" them, rather then just assigning them first group within the search distance. In some cases this was assigning features to a more distant cluster, resulting in less predictable cluster patterns
- puntos individuales se muestran ahora correctamente en su propio estado de selección
- mucha limpieza de código + documentación también.

Para desarrolladores: QgsPointDisplacementRenderer se ha dividido en una nueva clase base virtual pura QgsPointDistanceRenderer que maneja la detección de grupos y la agrupación de puntos. El nuevo renderizador de clúster reutiliza esta clase base para evitar la duplicación de código.

See the crowd [funding programme](https://north-road.com/qgis-cluster-renderer-crowdfunding/) for more details.

![image78](images/entries/a9a26b2c7154f918f8b218c2e01f3b38f599436a.png.400x300_q85_crop.webp)

Esta prestación fue fundada por  Andreas Neumann, Qtibia Engineering (Tudor Barascu), Karl-Magnus Jönsson, Geonesia (Nicolas Ponzo) & ¡numerosos patrocinadores anónimos adicionales cuyas generosas contribuciones también son muy valoradas!

This feature was developed by [Nyall Dawson](https://north-road.com/qgis-cluster-renderer-crowdfunding/)
### Prestación: NUEVOS ALGORTIMOS DE COLORACIÓN DEL MAPA EN QGIS 3.0
see <http://nyalldawson.net/2017/02/new-map-coloring-algorithms-in-qgis-3-0/>

![image79](images/entries/1a507363f0c35065d8c2751e167531b96600d700.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Nyall Dawson
### Feature: New \"preset\" colors color ramp option
Allows use of a color ramp consisting of a list of selected colors. Currently there\'s no way in QGIS to classify a renderer using some list of colors you\'ve previously selected. So you can modify the colors manually after classifying, but that\'s a pain if you\'re regularly using the same color scheme. Basically, it\'s like the color brewer color ramp options but allowing users to pick their own preset list of colors to use (Because Cynthia Brewer isn\'t the only cartographic color expert!)

![image80](images/entries/ea1e2fe7215ea888b9de00329e230f6b665610a6.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Permite desabilitar temporálmente las capas de símbolos
Adds a new checkbox at the bottom of each symbol layer\'s properties which allows you to control whether the layer is enabled or not. Disabled layers are not drawn, but are saved and can be enabled at a later stage. This makes it easier to tweak symbol appearance without having to totally delete a symbol layer.

![image81](images/entries/555204a38e13852e4717179a9981cb522244613a.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Estilizado sencillo de rasters discretos
In QGIS 3.0, the existing raster Paletted Renderer for rasters was adapted to allow for easy styling of discrete raster layers, such as landcover or boolean rasters. Now, users can select the renamed \"Paletted/Unique Values\" renderer and click the \"Add Unique Values\" button to load all unique raster values from the layer. These are automatically assigned a color using the selected color ramp.

El cálculo del valor único se realiza en un subproceso de fondo para mantener la interfaz de usuario receptiva para capas ráster grandes (o remotas). Además, los usuarios pueden agregar manualmente nuevas clases individuales como lo deseen, y editar el valor de píxel asociado para cualquier clase existente. También se admite la eliminación de varias clases a la vez, así como el cambio de color, transparencia y etiquetas para varias clases a la vez.

Las paletas de color se pueden cargar desde un archivo de texto, con formatos de tabla de colores ESRI clr/GDAL/GRASS. Las paletas de color pueden ser grabadas a un archivo de texto clr para compartirlas.

![image82](images/entries/536a7bce4d526e2d5fbeeb3189de6f60b2d79256.png.400x300_q85_crop.webp)

This feature was funded by Stéphane Henriod, Satelligence (<http://satelligence.com/>), Bird\'s Eye View (<https://www.birdseyeviewgis.com/>), other anonymous backers

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Etiquetando
### Prestación: Permite tamaño de fuente de etiquetas en mm/pixels
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Barra de herramientas personalizada esta ahora habilitada
Thanks to the awesome **auxiliary data storage** and the editable joined table, the manual label customization is now always enabled. You do not need anymore to add dedicated fields in your datasource to change labels position, rotation, or any of the possible settings for labels to activate the toolbar. **No more copy of readonly datasources and so much faster labeling !** **Be warned**, labels are **only saved along with your project file** in a .qgd sqlite database, or inside the .qgz zipped project file if you chose that format. Don\'t forget to share that .qgd file if you want to share your project file.

And for power users, the old way of having data defined fields in your datasource is still there. Just define them in the layer\'s properties as before!

![image83](images/entries/546a77b230bf9b0b28bf61bb231b78cbb6bd5b5f.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
## Diagramas
### Prestación: propiedades definibles por datos
Añade soporte para mas propiedades definibles por datos a diagramas:
- Distancia
- Prioridad
- ZIndice
- IsObstacle
- Mostrar
- MostrarSiempre
- Ángulo Inicial del Diagrama

Esta prestación fue fundada por el Programa de Subvenciones de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Representación
### Prestación: soporte de capa en vivo
QGIS 3.0 ahora admite capas en vivo. Estas capas se vuelven a representar automáticamente en un intervalo de tiempo que usted determine, de forma limpia y sin parpadeos. Las capas en vivo son excelentes para rastrear datos que cambian continuamente, como una flota de automóviles, una bandada de pájaros para los que tiene datos de telemetría, etc.

![image84](images/entries/5a9cd3df6f804b903fee30a08f7018887c1d8710.gif)

Esta prestación fue desarrollada por Kartoza & North Road
### Prestación: Activar actualización de capa o acciones de capa desde la señal NOTIFICACIÓN de PostgreSQL
Siguiendo los efectos de la capa en vivo, esto permite activar acciones o actualizar la capa en QGIS solo cuando la base de datos notifica a QGIS que debe hacer algo. Requerirá menos recursos que actualizar en intervalos, e incluso puede codificar una aplicación de chat en QGIS con ello :)

See <https://vimeo.com/236604742>

<http://oslandia.com/en/2017/10/07/refresh-your-maps-from-postgresql/>

This feature was funded by [QGIS.org Grant application](https://qgis.org)

This feature was developed by [OSLANDIA - Vincent Mora](https://github.com/vmora)
### Prestación: Resultado de etiquetado en caché para evitar redibujos innecesarios al actualizar la vista de mapa
Este cambio permite que los resultados del etiquetado se almacenen en caché en una imagen después de un renderizado de mapa. Si la imagen del resultado de la etiqueta en caché se puede reutilizar para el siguiente renderizado, lo será, evitando la necesidad de volver a dibujar todas las capas que participan en el problema de etiquetado y resolviendo la solución de etiquetado. Básicamente, esto significa que **el lienzo se actualiza como resultado de los cambios en cualquier capa NO ETIQUETADA mucho más rápido**. (Cambiar una capa que es parte de la solución de etiquetado aún requiere que todas las capas etiquetadas se vuelvan a dibujar por completo)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: renderizador de cuadrícula para desplazamiento de puntos
renderizador de cuadrícula para desplazamiento de puntos

![image85](images/entries/0247dfa555b6a80139f399b69071a2cc9bd278b3.png.400x300_q85_crop.webp)

This feature was developed by [Muhammad Yarjuna Rohmat (Kartoza)](http://www.kartoza.com)
## Digitalizando
### Prestación: Selección de una serie de vértices en la herramienta nodos
Esta prestación hace posible seleccionar una **serie de vértices** de una entidad.

Se puede activar presionando **Shift+R** - luego se necesita hacer clic en el punto inicial y final dentro de una entidad - esto seleccionará todos los vértices entre los dos.

La selección del rango se puede cancelar en cualquier momento haciendo clic con el botón derecho o presionando la tecla Esc.

For closed curves (polygons), it is possible to switch to the \"longer\" way around the ring by holding **Ctrl** while clicking the final point.

![image86](images/entries/b44524fe2864249a334cb7d21fd1a0c1d885ff15.gif)

This feature was funded by [French ministry in charge of ecology](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Prestación: Opción de añadir valor Z por defecto.
Crear Geopaquetes/Shapefiles: Ahora con la opción de tener valores Z

![image87](images/entries/80e8c78a1b38dfde5120144fac7354e800b9daff.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Alexander Lisovenko / Paul Blottiere
### Prestación: Mover entidad ahora beneficiada desde Digitalización Avanzada
Just move a feature using the new \"click - click ergonomy\" and use the advanced digitizing panel and shortcut to constraint angles, distances, exact XY.

Esta prestación fue desarrollada por Denis Rouzaud
### Prestación: Funcionalidad añadida a la prestación copiar/mover a la herramienta mover entidad de mapa
Esto permite duplicar una entidad y moverlas en un movimiento desde una entidad seleccionada

![image88](images/entries/eea327329365ad80c7fc3363ad0fb455fc9d4335.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Denis Rouzaud
### Prestación: Trazando con compensación
Ahira puede usar la herramienta de digitalización de trazado con una compensación como muestra la imagen adjunta.

![image89](images/entries/974604dc8908668c2d727e12975707560cffb493.gif)

This feature was funded by [d.b.g. Datenbankgesellschaft mbH](http://www.datenbankgesellschaft.de/)

This feature was developed by [Martin Dobias](http://www.lutraconsulting.co.uk)
### Prestación: Revisión de la herraienta Vértice
La herramienta Nodo (ahora renombrada a herramienta Vértice) ha sido sometido a una revisión completa para hacerlo más flexible. Algunos de los cambios más importantes son:
1. En lugar de exigir a los usuarios que primero seleccionen una entidad y luego editen sus vértices en un segundo paso, la herramienta ahora es capaz de trabajar con múltiples entidades al mismo tiempo. Por lo tanto, es fácil seleccionar vértices de varias entidades y moverlos o eliminarlos a la vez. Si hay necesidad de restringir la selección de vértices solo a entidad(es) específica(s), es posible seleccionar las entidades con la herramienta de selección primero -la herramienta de vértices solo funcionará con vértices de la(s) entidad(es) seleccionada(s) en ambos casos.
2. En lugar de trabajar solo con la capa seleccionada actualmente, la herramienta ahora puede trabajar con todas las capas que están en modo de edición al mismo tiempo. El traslado de entidades que lógicamente están juntas pero que se encuentran en diferentes capas se ha vuelto mucho más fácil. Aún así, la capa actual se respeta si hay múltiples elecciones al escoger vértices.
3. Las características y sus vértices se resaltan a medida que el usuario mueve el puntero del mouse sobre ellos, proporcionando una mejor respuesta visual.
4. In QGIS 2.x the vertices would be moved by clicking a vertex, dragging it with the left mouse button still pressed and finally dropping them by releasing the mouse button. This behavior has been changed to \"click-click\" approach where user first clicks a vertex to pick it, then drag it without having any mouse buttons pressed and drop it by clicking again on the final destination. The arguments for this change were the following:
5. es más fácil colocar nodos con precisión (al no tener que aplicar fuerza al botón del mouse todo el tiempo)
6. uno no mueve nodos sin percatarse
7. Es posible cancelar la operación
8. permite desplazar el mapa presionando la barra espaciadora mientras se mueve el nodo

See <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/69> for more information.

![image90](images/entries/c2761555d13be6b8a1893da2bd3240dd6343c9a6.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Herramienta Vértices: marcadores de punto medio para añadir vértices
La herramienta de vértice mejorada ahora también muestra marcadores adicionales en el punto medio de los segmentos de entidades lineales. Al hacer clic en dicho marcador, se suma un nuevo vértice. Se ha mantenido la forma existente de agregar vértices haciendo doble clic en segmentos.

![image91](images/entries/b47f105d5ea3ecf5176a8296cc386c65bce21da7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Característica: Herramienta vértice: continuar linea
Al editar geometrías de cadenas lineales con la herramienta de vértice, al mover el mouse hacia el primer o el último vértice se mostrará un marcador adicional justo al lado del punto final. Al hacer clic en el marcador, se agregará un vértice al final de la geometría.

![image92](images/entries/b355e0701d6b395d25a965cc7d31b9f8acce49d7.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Herramienta vértice: panel de soporte para digitalización avanzada
El panel de digitalización avanzada ahora trabaja con la herramienta vértices - Es posible ingresar coordenadas de vértices nuevos o existentes en el panel al igual que en otras herramientas de digitalización de mapas.

![image93](images/entries/297f18356a626066332b4c28e13ce4c94bb70166.gif)

This feature was funded by [QWAT](http://qwat.org/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Administración de datos
### Prestación: Desplazarse a la entidad actual en la tabla de atributos
![image94](images/entries/2f488f086cb64fb0394d1848b4a41f28f80a2adf.gif)

Esta prestación fue desarrollada por Marco Hugentobler
### Prestación: Mapa de la extensión del CRS en las propiedades del proyecto
![image95](images/entries/d56d5d68aff5b7f10999751041490769b79e619d.png.400x300_q85_crop.webp)
### Prestación: Soporte de almacenamiento auxiliar
Una nueva lengüeta está disponible en las propiedades de la capa vectorial para administrar el almacenamiento auxiliar :

Una nueva opción *Almacenar datos en el proyecto* está disponible en el menú de datos definidos proporcionando una forma sencilla para administrar datos auxiliares para una propiedad:

Los datos auxiliares se almacenan en una base de datos sqlite y se gestionan gracias al proveedor de datos OGR (en lugar del proveedor de espacialidad) para mantener el archivo de base de datos lo más pequeño posible. Este archivo de base de datos (con extensión *.qgd*) se guarda junto al archivo del proyecto o se incrusta directamente en el nuevo formato *.qgz*.

See the original [pull request](https://github.com/qgis/QGIS/pull/5086) and this article [which explains more](http://oslandia.com/en/2017/10/17/auxiliary-storage-support-in-qgis-3/)

![image96](images/entries/f0fded6f5276d4b7e51b11834bad3d615e2b4f2d.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere / Oslandia](http://oslandia.com/)
### Prestación: Revisión de Metadatos
El sistema de metadatos en QGIS ha sido revisado. En QGIS 3.0 presentamos nuestro propio esquema interno, formalizado de metadatos que es independiente del formato de archivo del proyecto QGIS. Introducimos nuevas capacidades de API para leer y escribir metadatos para capas. Hemos separado la visualización de metadatos de la edición y hemos agregado una nueva herramienta de edición de metadatos. Los metadatos se guardan actualmente en el archivo del proyecto. También se puede guardar como un archivo XML junto con capas basadas en archivos o en una base de datos sqlite local para capas remotas(por ejemplo, PostGIS).

you can read more about the design considerations adopted in this work by referring to the QGIS Enhancement Proposal (QEP) - [QEP-92](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/91)

Please note this is the first phase in the development of a complete and standards compliant metadata infrastructure for QGIS. We are seeking further funding to implement a more complete implementation for the metadata system - see [this document](https://docs.google.com/document/d/1twE8J345Sz1rk1z34672eqlEiL2mJT4bZbuF5oRTCoM/edit?usp=sharing) for details of future planned work packages that need funding.

The specification for the QGIS metadata schema is [here](https://github.com/qgis/QGIS/blob/master/resources/qgis-resource-metadata.xsd).

The primary funder for this work was [The WorldBank/GFDRR](https://www.gfdrr.org) with supporting funding provided by [NINA](https://www.nina.no/english).

![image97](images/entries/a26adc99ea62733e65222769095537e3be3fb29a.png.400x300_q85_crop.webp)

This feature was funded by [WorldBank/GFDRR](http://gfdrr.org)

This feature was developed by [Kartoza and collaborators](http://kartoza.com)
### Prestación: diálogo de administrador de fuente de datos unifcado
Un único cuadro de diálogo unificado para manejar la administración de la fuente de datos y la carga de capas.

![image98](images/entries/3d6a40ee709ca4f18d8532291f3cbc97997f1932.gif)

Esta prestación fue fundada por Boundless

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: Herramienta de descarga de OSM borrada
Hemos borrado la herramienta de descarga de OSM que fue proporcionada en versiones QGIS 2.x. Le recomendamos que utilice el complemento QuickOSM que se ha portado a QGIS 3.0.
## Widgets y Formularios
### Característica: Permitir controlar etiquetas para widgets de edición individual
En el diseñador de arrastrar y soltar, un doble click en un elemento permitirá controlar si la etiqueta debe mostrarse individualmente para cada elemento.

Esta prestación fue desarrollada por Matthias Kuhn
### Característica: Permitir configurar botones link/unlink entidad en el widget editor de relación
Esta prestación fue desarrollada por Matthias Kuhn
### Característica: visibilidad condicional para pestañas y cuadros de grupo
Esto agrega una nueva opción de configuración para mostrar u ocultar condicionalmente pestañas y cuadros de grupo en formularios del diseñador de arrastrar y soltar. La configuración se realiza mediante un doble clic en el árbol del diseñador en la interfaz de configuración de campos. Se puede ingresar una expresión para controlar la visibilidad. La expresión se volverá a evaluar cada vez que los valores en el formulario cambien y la pestaña o el cuadro de grupo se muestra/oculta en consecuencia.

Esta prestación fue desarrollada por Matthias Kuhn
### Carcaterística: Widgets de edición predeterminados más inteligentes con complementos para elegirlos
Ahora los widgets pueden dar una puntuación sobre qué tal podrían manejar el tipo de campo. Conduce a mejores widgets predeterminados.

Además, se pueden agregar complementos para elegir un tipo de widget en función de la información externa. Uno de ellos usa una tabla en PostgreSQL, lo que permite especificar el tipo de widget y la configuración que se utilizará para cada campo.

Elija automáticamente los widgets RelationReference para claves foráneas.

Esta característica fue desarrollada por Patrick Valsecchi
### Característica: Las restricciones de campo pueden aplicarse o no
Las restricciones no forzadas solo muestran una advertencia al usuario, pero no impiden que se confirme la función. Las restricciones impuestas impiden a los usuarios comprometer funciones no conformes. ¡Entonces ahora tenemos advertencias suaves! Cualquier restricción detectada por el proveedor siempre se aplica.

![image99](images/entries/da468dc209eb7e7da3696ee26850af6b9017312c.png.400x300_q85_crop.webp)

Esta característica fue fundada por OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: Agregar acciones de ámbito de capa
Dentro de la tabla de atributos, hay un nuevo botón para activar acciones que no se basan en características individuales, sino en toda la capa. Normalmente realizarán acciones basadas en todas las características o la selección.

Esta prestación fue desarrollada por Matthias Kuhn
### Característica: Mostrar valores de campos en el autocompletador en el modo de filtro de formulario
The autocompleter is nicely updated in the background so that the gui remains nice and responsive, even if there\'s millions of records in the associated table.

It\'s now used as a search widget for text fields, so can be seen in the browser window if you set the filter to a text field, or if you launch the form based select/filter by selecting a layer and pressing F3.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: Agregar zoom a funciones y accesos directos a funciones de flash en el cuadro de diálogo Seleccionar por formulario
Permite una navegación muy rápida e identificación de características que coinciden con los criterios del formulario

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: Añadir entre/no entre a campos numéricos en seleccionar por formulario
![image100](images/entries/4bfb34794edbff35e6336c165993278e9a515644.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Leyenda de capa
### Prestación: Acción de ocultar Capas Deseleccionadas
Le permite fácilmente esconder todas las capas deseleccionadas. Esto es muy práctico cuando tienes un proyecto extenso y quieres esconder fácilmente todo excepto un par de capas

![image101](images/entries/a8419d6027de9351afa6f8a99700509b24cc7418.png.400x300_q85_crop.webp)

This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Cambiar la ergonomía de la visibilidad de capas dentro de grupos
- Checking/unchecking a group doesn\'t change the check state of its children. A node is visible if and only if it is checked and all its parents too.
- No hay mas un estado semimarcado para un grupo
- **Ctrl-click** en un grupo no marcado, marcará el grupo y todos sus descendientes.
- Click en una capa no marcada marcará la capa y todos sus padres.
- Ctrl-click en un grupo marcado desmarcará el grupo y todos sus descendientes.
- Ctrl-click en una capa marcada desmarcará la capa y todos sus padres.
- Estas acciones están disponibles en elementos de menú contextual en la vista de árbol.
- Capas invisibles en gris porque ellas o su(s) padre(s) están desmarcadas.

Esta prestación fue desarrollada por Even Rouault
## Compositor de Mapa
### Prestación: Control sobre el dibujo de las líneas horizontales y verticales de la cuadrícula del tablero del compositor
Ahora es posible controlar independientemente la representación de líneas horizontales y verticales de los elementos del tablero del compositor. Esta flexibilidad adicional usa las posibilidades de diseño de este elemento directamente dentro de QGIS.

![image102](images/entries/ac1b2079c9e6c19747322d246d666df7e3c4ac0d.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Arrastre de qpt a QGIS para crear un nuevo compositor desde la plantilla
This feature was funded by [SMEC (Surbana Jurong)](http://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Permitir la personalización del espaciado de líneas para etiquetas de elementos de leyenda del compositor
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Permitir elección del CRS para elementos del mapa
Esto permite que el CRS para los elementos del mapa difiera del CRS del canvas/proyecto. También permite que diferentes elementos del mapa tengan diferentes CRS, por ejemplo, se puede establecer un mapa general en un CRS diferente al mapa principal.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Manteniendo shift mientras dibujamos polilineas/poligonos restringe ángulos entre líneas
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Mas controles definibles por datos
Elemento **marco** y **colores de fondo** Datos definidos **colores svg y ancho del contorno para elementos de imagen del compositor** (¡Especialmente útil cuando la imagen muestra una flecha norte!) Datos definidos **títulos de leyenda y conteo de columnas** Datos definidos **colores de barra de escala y ancho de línea**

Esta prestación fue fundada por el Programa de Subvenciones de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Revisión del compositor de mapa
Esta es una reconstrucción de como las composiciones son administradas en el código de QGIS.

Los puntos destacados son:
- Una nueva clase de QgsLayoutManager que se utiliza para almacenar y serializar/deserializar composiciones. Se adjunta un QgsLayoutManager a QgsProject. Esto permite que el código central acceda a las composiciones adjuntas a un proyecto. Todo el manejo de las composiciones se ha movido de la aplicación al núcleo, lo que facilita que el servidor (y otros proyectos no basados en aplicaciones. QField/roam?) accedan a las composiciones del proyecto sin recurrir al frágil análisis de XML.
- Las ventanas del compositor se crean bajo demanda y se destruyen al cerrar. Esto evita el gran requisito de crear todas las ventanas y widgets del compositor para cada elemento del compositor al cargar proyectos. **Era la razón principal por la que la carga de composiciones de proyectos era tan lenta anteriormente**. Ahora, las ventanas del compositor se crean solo cuando la ventana se abre y se destruye cuando se cierra la ventana. Los widgets de configuración de elementos del compositor también se crean bajo demanda(cuando se selecciona un elemento) en lugar de crear todos los widgets.
- Un beneficio adicional de destruir ventanas del compositor al cerrarlas es que **ya no sufrimos un error Qt** que bloqueó el uso de muelles flotantes en las ventanas de compositor. ¡Ahora puede hacer flotar los paneles de elementos/composición/etc. !. Mucho mejor para trabajar a pantalla completa con composiciones en configuración de monitores múltiples.
- **Reworked API for working with composers through iface**. Since composer windows don\'t exist unless they are currently open, all the iface methods for interacting with composers have been redone to make it clear that they only apply to open windows. Additionally, a simple composer interface which provides a stable API for plugins and scripts to work with composer windows has been added. Very basic for now, but in future we can extend with more hooks to allow plugins to interact with composer windows.
- Mucha limpieza y borrado de código 

More info at <https://north-road.com/qgis-layout-and-reporting-engine-campaign/>

![image103](images/entries/fa298be4fea348f58b9bd2f4bea30f2e7f1c2ee5.png.400x300_q85_crop.webp)

Esta prestación fue fundada por El Grupo de Usuarios Suizos de QGIS y muchos mas !

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Herramientas de análisis
### Característica: recuento de valores únicos de ráster para procesamiento
<http://imhere-asia.com/blog/post/qgis-raster-layer-unique-values-count>

This feature was developed by <http://imhere-asia.com/>
## Procesado
### Prestación: Nuevo algoritmo para compensar líneas
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevo algoritmo para búferes de un solo lado
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Añadir elección del método de simplificación a simplificar
Este cambio permite a los usuarios elegir qué método usar al ejecutar el algoritmo de simplificar geometrías, con opciones del algoritmo existente basado en distancia (Douglas Peucker), algoritmo basado en área (Visvalingam) y ajuste a la cuadrícula.

Visvaligam en particular generalmente resulta una simplificación cartográficamente más agradable que los métodos estándar basados en distancia.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: soporte para tipos de geometría saliente en modelos
Las entradas del algoritmo hijo modelo ahora se filtran solo a aquellas que generan tipos de geometría aplicables para la entrada a otro algoritmo hijo

Esta funcionalidad fue desarrollada por Alexander Bruy
### Característica: umbral de ángulo para algoritmo suavizado
Agrega la opción a QgsGeometry::smooth a segmentos no suaves más cortos que un cierto umbral o esquinas afiladas con un ángulo que excede un umbral

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Mejor soporte para dimensiones Z/M y geometrías curvas
Muchos más algoritmos ahora respetan los valores Z/M y no descartan esta información, y además ahora muchos algoritmos mantienen correctamente las geometrías curvas sin una segmentación forzada de estas geometrías.
### Prestación: Algoritmos de análisis ráster añadidos a Processing
Los siguientes algoritmos han sido añadidos a Processing desde el complemento de Análisis Ráster
- Aspecto
- Pendiente
- Rugosidad
- Sombreado
- Relieve

Ahora estos algoritmos pueden usarse en scripts, modelos y para procesamiento por lotes.

![image104](images/entries/f5980f4840b9c822e5a228ec03da59168cd9c5e9.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Nuevo algoritmo para extraer nodos específicos.
Este algortimo le permite extraer nodos específicos de geometrías. Por ejemplo puede extraer el primer o último nodo de la geometría.

El algoritmo acepta una lista separada por comas de indices de los nodos a extraer, p.ej 0=primer nodo, 1=segundo nodo, etc. Índices negativos pueden usarse para extraer nodos desde el final de la geometría. p.ej. -1=último nodo, -2=penúltimo nodo.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Exponer estadísticas zonales del complemento de la caja de herramientas estadísticas zonales
Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Agregue un algoritmo SQL de ejecución espacial
Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: Nuevo algortimo para extender líneas
Permite extender cadenas lineales en una distancia establecida al principio y final de la línea

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nueva extracción por expresión algorítmica
Filtra una capa de entrada por expresión

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Añadir algortimo para importar en spatialite
Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: algortimos de interpolación
Expone la interpolación IDW y TIN del complemento interpolación en la caja de herramientas

En consecuencia el complemento interpolación ha sido borrado

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Nuevo algortimo para calcular geometría por expresión
Este algoritmo actualiza geometrías existentes (o crea nuevas geometrías) para las entidades entrantes mediante el uso de una expresión QGIS. Esto permite modificaciones en geometrías complejas que pueden emplear toda la flexibilidad del motor de expresiones de QGIS para manipular y crear geometrías para entidades salientes.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Ajustar geometrías a un algortimo de capa
Portar el complemento Geometry Snapper a procesamiento

Algoritmo de ajustar geometrías permite el ajuste a otros tipos de capas, soporta capas de punto/líneas.

Snap to layer algorithm accepts a mode parameter. With a new option to prefer to snap to closest point on geometry. The old behaviour was to prefer to snap to nodes, even if a node was further from the input geometry than a segment. The new option allows you to snap geometries to the closest point, regardless of whether it\'s a node or segment.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevo tipo de entrada para expresiones
Esto añade un nuevo tipo de entrada para entradas de expresiones. Las entradas de expresiones pueden enlazarse a una capa parental de tal manera que el constructor muestra los campos correctos y variables de capa.

It\'s designed to be used when an algorithm specifically requires an expression, eg Select by Expression and Extract by Expression.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: SplitWithLines
Cambiar el nombre del algoritmo SplitLinesWithLines a SplitWithLines Acept polígono como entrada, además Usa solo las líneas seleccionadas a dividir (si el procesamiento está configurado para usar solo la selección) emitiendo un mensaje de registro si intenta dividir geometrías múltiples. Ayuda actualizada

Esta prestación fue desarrollada por Bernhard Ströbl
### Característica: algoritmo de polo de inaccesibilidad
Implements a processing algorithm to calculate the pole of inaccessibility for a surface, which is the most distant internal point from the boundary of the surface. This function uses the \'polylabel\' algorithm (Vladimir Agafonkin, 2016), which is an iterative approach guaranteed to find the true pole of inaccessibility within a specified tolerance. More precise tolerances require more iterations and will take longer to calculate.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Extraer por atributo puede extraer valores nulos/no nulos
Añade soporte para filtrar cuando el valor de un atributo es nulo o no nulo

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Crear algortimo de índice de atributos
Permite la creación de un índice en un atributo en un ¡a capa para mayor rapidez de filtrado basado en atributos

El soporte depende del proveedor de datos subyacente para la capa

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New \'drop geometries\' algorithm
Simplemente borra algunas geometrías de una capa de entrada y devuelve solo las entidades con atributos

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New universal \'basic stats for field\' algorithm
Replaces the existing \'Basic Stats for Numeric Fields\' and \'Basic Stats for String Fields\' algorithms and adds support for date/time/datetime fields.

Tener un único algoritmo unificado permite modelos más flexibles donde un tipo de campo puede no conocerse de antemano.

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Característica: algoritmo para portar complemento de mapa de color a processing
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevo algoritmo para ortogonalizar geometrías
Adds a new algorithm which tries to make angles in geometries either right angles or straight lines

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Algoritmos para análisis de red
agrega algoritmos de ruta mas corta y de área de servicio más cortos a Processing

también permite calcular la ruta más corta desde un punto a todos los puntos en una capa, o desde todos los puntos en una capa a un punto final. Y creando áreas de servicio para todos los puntos en una capa.

En consecuencia el complemento Roadgraph ha sido borrado.

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: exportar modelos de procesamiento como PDF/SVG
Además de exportar modelos de procesamiento como imágenes de mapa de bits, ahora es posible exportar modelos de procesamiento como PDF y SVG independientes de la resolución. Esto permite la exportación de alta resolución de modelos que pueden integrarse en documentos y libros a publicar.

![image105](images/entries/0ad81df99f01b91d2421263ad35fdc4430c483e0.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Nuevo algoritmo para truncar tablas
Irretrievably deletes all features from a table\... use with caution!

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Added 'invalid feature handling' option
Esta prestación fue desarrollada por Victor Olaya
### Prestación: Algoritmo para fijar geometrías inválidas usando la implementación del nativo makeValid()
Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Agregar Búsqueda al diálogo Get Scripts and Models
Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Algoritmo genérico de centroide
Algoritmo centroide reconstruido el cual manipula capas no poligonales

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Algoritmo de extracción de nodos mejorado
El algoritmo extraer nodos ahora guarda el índice de nodos, distancia a lo largo de la línea y ángulo al nodo

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Nuevo algoritmo para trasladar (mover) puntos
Permite que las geometrías sean desplazadas en un desplazamiento x/y

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Ventana del modelador de procesamiento mejorada
The processing modeler window has received a lot of attention for this release. Improvements include: - zoom controls in the window\'s toolbar - customization of inputs and algorithms panels\' location - panels can now float above the processing window

![image106](images/entries/d7d74d9113516f51289380755f1862324c83feb5.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Característica: Nuevo algoritmo de informe de valores únicos de ráster
Se agregó un nuevo algoritmo al procesamiento el cuál devuelve el recuento y el área de cada valor único dentro de una capa ráster dada.

![image107](images/entries/096af77b050265c85d7ee203c2ab4d974b8be126.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Borrado del proveedor TauDEM del núcleo de Processing
Hemos borrado el proveedor TauDEM de procesando.

![image108](images/entries/c48a25965a147b866502d10771bea3e831a4d28e.jpeg.400x300_q85_crop.webp)
### Prestación: Descargar un archivo de Processing
Descargar un archivo de Processing. Consultar una API remota para obtener un geojson

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Prestación: algoritmo Puntos optimizados a lo largo de geometría
También admite geometrías poligonales, maneja geometrías nulas y registra el ángulo de línea original junto con la distancia a cada punto.

![image109](images/entries/9b24dc337e4896a8be9b0e651e32b3dc9cb11593.png.400x300_q85_crop.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: algoritmo Sort by expression
This feature was funded by [DFAT/DMI](http://dfat.gov.au/pages/default.aspx)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Opciones de Aplicación y Proyecto
### Prestación: Nuevo formato comprimido de archivos de proyecto .qgz
A long time ago on the developper\'s mailing list, we discussed of a container storing the xml file and other ressources. This is now possible, though it remains optional. The auxiliary storage feature takes advantage of that by storing the associated .qgd sqlite database. We hope that in next versions land support for embedding other resources like SVG, color ramps, datasources, images, etc\...

![image110](images/entries/b954811defffce51a7375ae24c640e0d1dcf88da.png.400x300_q85_crop.webp)

This feature was funded by [French ministry of Ecology and Sustainable Developpement](https://www.ecologique-solidaire.gouv.fr/)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Prestación: añadir soporte para perfiles de usuario
Todos los ajustes/complementos de usuario, etc. ahora se cargan desde la ubicación de los datos de la aplicación para cada plataforma y ya no son .qgis3/2. La configuración y los complementos en cada perfil ahora están aislados unos de otros.

Esto permite diferentes configuraciones de tiempo de ejecución dependiendo de lo que el usuario necesite, por ejemplo, prueba, producción, demostración, etc.

Menú perfil permite cambiar entre perfiles o crear unos nuevos.

![image111](images/entries/82d90b2a02b84584279b5e2b75774631a0cd4a44.jpeg.400x300_q85_crop.webp)

This feature was developed by [Nathan Woodrow](https://github.com/NathanW2)
## Navegador
### Feature: Drag\'n\'drop layers from layer tree view to browser dock
Hace sencillo p.ej. almacenar sus capas temporales en PostGIS

Esta prestación fue desarrollada por Martin Dobias
### Prestación: Aplicación de navegador independiente de QGIS eliminado
Hemos eliminado la aplicación de navegador QGIS independiente que se armó en QGIS 2.x. Esta aplicación tenía una mala aceptación del usuario y representaba una sobrecarga de mantenimiento con la que no deseamos que continúe en la base del código 3.0.
## Proveedores de datos
### Feature: New unified \'add layer\' dialog
Puede ahora usar un sencillo diálogo para añadir una amplia variedad de formatos de datos a QGIS

![image114](images/entries/d81a5fba0df198b53ef60293ade556125499e5e8.png.400x300_q85_crop.webp)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: GeoPackage
- el proceso usa pkg por defecto
- guardar como usa pkg por defecto
- crear nueva capa usa pkg por defecto
- arrastrar y soltar capas a importar desde el navegador

Esta funcionalidad fue desarrollada por Alessandro Pasotti
### Feature: Support all GDAL writable raster formats for \'Save as\' dialog on raster layers
Esta prestación fue desarrollada por Nyall Dawson
### Prestación: Soporte para geometríass Z/M en gpkg, spatialite y proveedor de capa de memoria
Support for Z dimension and M values was added to QGIS\' gpkg, spatialite and memory layer provider. the option to add Z and M dimensions has also been added to the \"create new layer\" dialogs

![image115](images/entries/63c518b689c749b106944c9d48826abba90887f0.jpg.400x300_q85_crop.webp)

This feature was funded by [QWAT group, http://www.imhere-asia.com/](http://www.qwat.org)

Esta prestación fue desarrollada por Mathieu Pellerin, Alexander Bury, Paul Blottiere
### Prestación: manejo de restricciones único y no nulo
Detección automática de restricciones únicas y no nulas del lado del proveedor implementadas para postgres, spatialite, proveedor ogr

Se pueden establecer restricciones únicas y no nulas del lado del cliente dentro de QGIS.

Se aplican restricciones únicas en forma de atributo

Esta característica fue fundada por OpenGIS.ch

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Integración de GeoNode
[GeoNode](http://geonode.org) is an open source geospatial content management system that makes it easy to publish geospatial data on the web. QGIS 3.0 includes new functionality that will allow you to very easily add a GeoNode instance to the browser tree and add any layers from that site to your project as WMS, WFS or XYZ. There is no need to dig around trying to figure out WMS/WFS end points, QGIS will do everything for you. When using WMS and XYZ Tiled layers, the style of the published GeoNode layer will be used.

Si la instancia de GeoNode usa el servidor QGIS en lugar de un servidor GeoServer, puede copiar y pegar estilos desde el servidor y aplicarlos a su capa local para que su capa WFS se muestre exactamente como lo hace en el servidor (como se muestra en la animación GIF aquí).

There are also python bindings so that you can add GeoServer layers to QGIS from your plugins. If you are interested in running your own GeoNode with QGIS Server backend please see [this site](https://github.com/kartoza/kartoza-rancher-catalogue/blob/master/README.md) for details on how you can do that using docker and rancher.

![image116](images/entries/8f23a63a25a4ad14c8a35ccf52029aa8f8c96379.gif)

This feature was funded by [WorldBank/GFDRR](https://www.gfdrr.org)

This feature was developed by [Kartoza](http://kartoza.com)
### Prestación: Detectar valores literales por defecto para el proveedor spatialite
This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Crear soporte para índice de atributos para el proveedor spatialite
Permite la creación de índices de atributos para capas spatialite

This feature was funded by [North Road](https://north-road.com/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Añade soprte para matrices
Soportado por postgres, spatialite

Esta característica fue desarrollada por Patrick Valsecchi
### Prestación: Soporte para HScore en el proveedor de datos PostGIS
### Prestación: Añadir autodescubrimiento de relaciones para PostgresQL
Esta característica fue desarrollada por Patrick Valsecchi
### Prestación: Dependencias de datos entre capas
This allows to declare data dependencies between layers. A data dependency occurs when a data modification in a layer, not by direct user manipulation may modify data of other layers. This is the case for instance when geometry of a layer is updated by a database trigger after modification of another layer\'s geometry.

Esta característica fue desarrollada por Hugo Mercier
### Prestación: Exportar dxf: soporte de reproyección
Esta característica fue desarrollada por Juergen E. Fischer
### Prestación: Cargar/Guardar estilo en la database para GPKG y Spatialite
Esta prestación fue desarrollada por Even Rouault
### Prestación: Manejo mejorado de los valores predeterminados
Mejora el manejo de los valores predeterminados (incluidas cláusulas predeterminadas del proveedor, valores predeterminados literales y valores predeterminados de expresión QGIS) y manejo automático de las restricciones de valores únicos en las capas

Se garantizará que cualquier campo con restricciones de valor único tendrá un valor único para el campo

Esto también significa que después de ciertas operaciones de edición (por ejemplo, copiar y pegar, dividir características, etc.) los atributos ahora se establecerán en su valor predeterminado, si corresponde.

Esta prestación fue fundada por Canton de Zug y el proyecto QGEP

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Servidor de QGIS
### Prestación: Revisión del Servidor de QGIS
As you may know, QGIS is jumping to a new major version (yes!). Doing so was made necessary because of the need to switch to python 3, QT5, but also because we needed to break the QGIS API in several places. (<http://blog.qgis.org/2016/02/10/qgis-3-0-plans/>)

Hace un año, un pequeño troll de Suiza hizo sonar la campana sobre la fuerte necesidad de una base de código de servidor de amor requerida. De hecho, la API estaba bloqueada por algunos métodos antiguos del servidor QGIS. En resumen, el servidor QGIS estaba analizando el archivo del proyecto qgs a su manera, y creó dependencias de parte de QGIS que necesitábamos eliminar.

Como la externalización de la base del código del servidor no era una opción, tuvimos que refactorizarla. Las partes involucradas decidieron involucrarse en un sprint de código en la ciudad de Lyon, Francia, dedicado a compartir su visión, planificar el trabajo y finalmente hacer que sucediera lo siguiente:

Refactorización de nivel superior

Todos los servicios (WMS GetMap, WFS GetFeature, GetLegendGraphics, WCS, GetPrint etc..) han sido reescritos. Algunos como WMS fueron completamente reescritos. ¡Felicidades a los desarrolladores!

Nuevas características
- Representación de subprocesos múltiples como en el escritorio
- Una nueva opción para confiar en los metadatos de la capa y así acelerar la carga del proyecto
- WFS 1.1 support <https://github.com/qgis/QGIS/pull/5297>
- Enlaces completos de Python para el servidor API
- Servicios de servidor como complementos como proveedores

Tareas profundas, complejas y poco gratificantes
- Eliminar todas las llamadas individuales
- Corta todas las dependencias al antiguo analizador de archivos de proyecto QGIS
- Minimice las dependencias de la biblioteca GUI. Dado que las fuentes son necesarias para representar mapas, no fue factible eliminarlas por completo.

Tareas de infraestructura
- Crear una plataforma de conformidad de OGC e integrarla en una plataforma de integración continua. Los informes de conformidad ahora se envían a tests.qgis.org
- Add unit tests \... and again more unit tests
- Hacer hincapié en el servidor QGIS contra fugas de seguridad (inyecciones SQL y otros ataques maliciosos)
- Comenzar a perfilar y realizar actuaciones de marcado de banco. Este trabajo todavía necesita algo de amor, y fondos, para ser logrado.

Se dió una presentación en Julio en  FOSS4G-EU

Esta prestación fue fundada por Donantes de QGIS.ORG
### Prestación: Posibilidad de segmentar información de geometría en el servidor
Many web clients can\'t display circular arcs in geometries. To allow such clients to still display a feature\'s geometry (e.g. for highlighting the feature), a new per project QGIS server option was introduced (Menu \"Project\" -\> \"Project Properties\" -\> \"QGIS Server\") to segmentize the geometry before sending it to the client in a GetFeatureInfo response.

![image117](images/entries/c6e36e36b5dc6fb0f5534ef11cb773781db4bf8c.png.400x300_q85_crop.webp)

This feature was funded by [Kanton of Zug](https://geo.zg.ch/)

This feature was developed by [Marco Hugentobler](https://www.sourcepole.ch/)
## Plugins
### Prestación: Borrar estado de confiable del Administrador de Complementos
<https://github.com/qgis/QGIS/pull/5272>
### Prestación: Edición fuera de linea: Añadir bandera de solo copiar a entidades seleccionadas
Esto amplia las posibilidades de edición fuera de línea para trabajar en subconjuntos de capas grandes

Esta prestación fue fundada por DB Fahrwegdienste GmbH

Esta prestación fue desarrollada por Matthias Kuhn
### Prestación: GDALTools movida a Processing
El complemento GDALTools ha sido borrado

Todas las funciones disponibles anteriormente a través del complemento GDALTools se movieron al marco de procesamiento QGIS, lo que permite utilizar estas herramientas en scripts, modelos y ejecutarlas en procesos por lotes. Además, actualizamos los algoritmos con nuevos parámetros, introducidos en las últimas versiones de GDAL y mejoramos la UI/UX general al exponer algunos parámetros avanzados como las opciones de creación, la configuración de valores NODATA, etc.

![image118](images/entries/ee1c51737225b6dac80a044f272319534fee2832.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: permitir la instalación de complementos desde paquetes locales ZIP
Ahora es mas sencillo instalar complementos manualmente sin tener que descomprimirlos en el directorio del perfil del usuario manuálmente.

![image119](images/entries/b0311613cf73564f4dc104772abfab551c391dad.jpg.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Los complementos pueden proporcionar ayuda personalizada en la ventana Expresión
Los complementos que proporcionan expresiones pueden agregar una ayuda personalizada hecha con cadenas HTML.

![image120](images/entries/ef610ef1efd507e9bf0ee905d8f8d24a40c753e5.png.400x300_q85_crop.webp)

This feature was funded by [DFAT/DMI](http://dfat.gov.au)

This feature was developed by [Etienne Trimaille (Kartoza)](http://www.kartoza.com)
## Programabilidad
### Prestación: Actualizaciones de la clase de Geometrías
Ha habido una revisión importante de las clases de geometría en QGIS. Las antiguas clases han sido renombradas (según la tabla siguiente). Las nuevas clases de geometría conservarán debidamente los atributos Z y M si están presentes.

References [https://github.com/qgis/qgis3.0\\\_api/issues/11](https://github.com/qgis/qgis3.0\_api/issues/11)

Esto finalmente devuelve un estado consistente a la denominación en la API de geometría
### Renombramientos
| QGIS 2 | QGIS 3 |
| --- | --- |
| QgsPolygon | QgsPolygonXY |
| QgsMultiPoint | QgsMultiPointXY |
| QgsMultiPolyline | QgsMultiPolylineXY |
| QgsMultiPolygon | QgsMultiPolygonXY |
| QgsPolygonV2 | QgsPolygon |
| QgsMultiPointV2 | QgsMultiPoint |
| QgsMultiPolylineV2 | QgsMultiPolyline |
| QgsMultiPolygonV2 | QgsMultiPolygon |

See also <https://github.com/qgis/QGIS/pull/5491>

Esta prestación fue desarrollada por Matthias, Nyall y otros
### Prestación: Administrador de Tareas
Presenta un sistema para crear tareas en segundo plano, con las que interactúa a través de un administrador centralizado

Adds new classes: - QgsTask. An interface for long-running background tasks - QgsTaskManager. Handles groups of tasks - also available as a QgsApplication member for tracking application wide tasks

Agrega el método simple de Python QgsTask.fromFunction para la creación de tareas desde una función sin tener que crear una subclase de QgsTask

Soporte para tareas dependientes

Cancelando una tarea de la que dependen otras provoca que todas esas otras sean canceladas también.

Añade manejabilidad de capas dependientes al administrador de tareas

Si una tarea tiene capas dependientes las cuales van a ser borradas, la tarea será automáticamente cancelada

QgsTasks puede tener subtareas

Ahora, una QgsTask  puede tener una subtarea QgsTasks establecida llamando a QgsTask::addSubTask. Las subtareas pueden tener a su vez tareas dependientes.

Las subtareas no son visibles a los usuarios, y los usuarios solo ven el progreso global y el estador de la tarea principal.

Esto permite la creación de tareas que se construyen a partir de muchas tareas componentes más pequeñas. El administrador de tareas seguirá manejando la activación y la programación de las subtareas, por lo que, por ejemplo, las subtareas pueden ejecutarse en paralelo (si sus dependencias lo permiten).

Las subtareas pueden tener subtareas propias.

Este cambio está diseñado para permitir que el concepto de procesamiento de algoritmos y algoritmos de modelador sean traducibles directamente a la arquitectura del administrador de tareas.

Esta prestación fue fundada por el Programa de Subvenciones de QGIS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: API to allow drag\'n\'drop of custom browser items
Las implementaciones de QgsDataItem pueden proporcionar la implementación de hasDragEnabled(), mimeUri() y QgsCustomDropHandler para ayudar a colocar elementos personalizados.

Esta prestación fue desarrollada por Martin Dobias

{{<content-end >}}
