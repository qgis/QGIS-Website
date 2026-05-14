---
HasBanner: false
draft: false
releaseDate: '2023-06-26'
section: proyecto
sidebar: true
title: Registro de cambios de QGIS 3.32
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios de QGIS 3.32{#changelog332 }
![image1](images/projects/0316fbcb7ba30bcf1caee80daf0662a1a15d99b0.png)

Fecha de publicación: 2023-06-26

QGIS 3.32 es una importante versión del proyecto QGIS que aporta un avance significativo en tecnología geoespacial al mundo del código abierto. La comunidad de desarrolladores ha introducido varias prestaciones nuevas y mejoras para aprovechar el potencial de los datos geoespaciales.

Entre las numerosas mejoras en la calidad de vida a través de un amplio espectro de prestaciones existentes, la versión 3.32 incorpora la largamente esperada funcionalidad para el Procesamiento Nativo de Nubes de Puntos en QGIS, permitiendo a QGIS Desktop convertirse en una potente utilidad de procesamiento de datos LiDAR.

This milestone achievement is thanks in large part to the contributions of the community to the effective [crowd funding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/) which funded this development, the QGIS community and [Enhancement Proposals](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263) used for the effective governance of these contributions, the collaborative efforts of the development agencies involved, and of course the extraordinary contributions of individual developers who build these tools for the benefit of all.

Esta versión también incluye una amplia variedad de mejoras en la experiencia de los desarrolladores, ampliaciones de nuevas funcionalidades como los gráficos de perfiles y los marcos de procesamiento, y un nuevo marco para datos de sensores con el fin de integrar estrechamente QGIS con los aparatos de recogida de datos y facilitar la creación de soluciones inteligentes de nueva generación.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=ZtE1Az-zpf0>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/ZtE1Az-zpf0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is a community effort, and we would like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es software libre y no hay obligación de pagar nada por utilizarlo; de hecho, queremos animar a todo el mundo a que lo use, independientemente de su situación económica o social. Creemos que dotar a las personas de herramientas para la toma de decisiones espaciales redundará en una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Herramientas de mapa
### Prestación: Vista previa de consejos sobre mapas
Se ha añadido una ventana de previsualización de consejos cartográficos al cuadro de diálogo de propiedades de las capas ráster y vectoriales para enriquecer la experiencia de diseño de consejos cartográficos.

![image3](images/entries/9e24454517900953b1b667e670c553ac29f10d58.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Herramienta de medición de coordenadas de copia
El diálogo de medición se ha ampliado con las siguientes funciones:
- Columnas X e Y con coordenadas X e Y
- La primera fila de la tabla sólo contiene las coordenadas (no la distancia)
- Aparece un mensaje cuando la copia se ha realizado correctamente
- A `Copy all` action is provided in a context menu on the table
- Evita errores al cambiar los ajustes durante la medición

Additional settings for managing the \"Copy All\" button behavior are provided to configure aspects such as separator, or including header information.

![image4](images/entries/4eb0ded16e3b6be3c0696230eb63a7a88fab4197.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Desactivar los consejos de mapa para una capa específica
Una nueva prestación en las propiedades de las capas permite desactivar mapTips en una capa específica.

On the QGIS API, a `mapTipsEnabled` Q_PROPERTY was added to the `QgsMapLayer` class to enable this functionality.

![image5](images/entries/73c9d66fac45f948e63ead3f94be4ccddb3172b4.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Interfaz de usuario
### Prestación: Mostrar la descripción de la relación de valores al pasar el ratón por el combobox
A description tooltip is now available when hovering the cursor over the value in the relation editor widget\'s combobox.

The description tooltip matches that of the currently selected item\'s description as defined in the \'description column\' on the value relation configuration panel.

![image6](images/entries/369ecca5320fe09a8f2657463df647c5526a496c.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: acciones de acoplamiento de la vista del lienzo del mapa 2d
Se ha añadido la acción de acoplar y desacoplar vistas de lienzo de mapa 2d para que coincida con el comportamiento de las vistas de lienzo 3d.

![image7](images/entries/d6aaec94112b3787b59d1d820b0335b9ab9b2385.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir botón borrar src usados recientemente
The ability to remove \"recently used\" CRS information has been implemented in various ways, including:
- Si se pulsa la tecla Supr mientras la lista de SRC utilizados recientemente está activa, se elimina el SRC seleccionado.
- Una columna en la tabla de SRC recientes con un botón para borrar SRC individuales.
- Una acción del menú contextual para borrar lo seleccionado
- Una acción del menú contextual para borrar todos los SRC recientes que pedirá confirmación al usuario.

![image8](images/entries/564478bebbaeda3394d77001b46cb051a795c73f.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Acercamiento de la rueda de marcha atrás
Ahora existe un ajuste para invertir la dirección del zoom de la rueda del ratón (si se desplaza hacia delante, se aleja).

Este ajuste afectará a los zooms de rueda en múltiples contextos, incluyendo:
- in the map canvas (`QgsMapCanvas`)
- in the map overview (`QgsMapOverviewCanvas`)
- in the layout view (`QgsLayoutView`)
- in the layout map items when the \"move item content\" tool is active (`QgsLayoutViewToolMoveItemContent`)
- in the Elevation profile canvas (`QgsElevationProfileCanvas`)
- In the model editor graphic view (`QgsModelGraphicsView`)

![image9](images/entries/b242e0115f29586846d88d6d0cfb1d5f6f9760f0.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Rotación espacial de marcadores
Ahora es posible almacenar y aplicar la rotación de mapas en marcadores espaciales, lo que incluye un nuevo menú contextual en el panel del gestor de marcadores espaciales.

![image10](images/entries/ea7e07b0c6a753ab205dd31d20454a4006c17bba.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Notas
### Prestación: Mejoras en la herramienta de anotación
Se han introducido varias mejoras en el comportamiento de las herramientas de anotación, entre ellas:
- Impedir el cambio de tamaño de una anotación cuando el cursor no se encuentra sobre el marco
- Añadir un menú contextual (cuando se activa una herramienta de anotación) en los elementos de anotación.
- Drop the undocumented `toggleTextItemVisibilities` (toggled Text annotations visibility with Ctrl+T)
- Mejora del comportamiento de selección y redimensionamiento, incluidas mejoras en el tratamiento de anotaciones superpuestas.

![image11](images/entries/fe30ec582f3b10338c05db078429751c06c890af.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Vista previa en directo de las anotaciones
A \"live update\" checkbox in the annotation editors allows for on the fly review of rendered annotation content.

![image12](images/entries/a969c1ce6990854c84031bc4b7085b799c03f32f.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Objetos 3D
### Prestación: Herramienta de medición 3D mejorada
Se han implementado las siguientes mejoras en la herramienta de medición en escenas 3d:
- Permite medir en puntos de la nube de puntos
- Display billboard circle markers on the 3d rubber band\'s vertices
- Moving the mouse moves the rubber band\'s last vertex (although the measured results are not updated until user clicks)
- Mover la cámara no elimina las mediciones actuales
- Permite utilizar las teclas retroceso y del para deshacer (eliminar la última medición)
- Permite utilizar Esc para borrar mediciones, igualando el comportamiento de su homólogo 2d
- Renders 3d rubberbands on top of other 3d entities so they don\'t get occluded

La lógica de selección de objetos también se ha refactorizado para un mayor control, y la herramienta de identificación 3D también se ha mejorado para evitar interferencias con la navegación de la cámara, así como una corrección de errores por los que se devolvían los FID incorrectos en casos específicos.

![image13](images/entries/65d6c0b4ab0c187c6a4b1e9f2f6c6483708cfce4.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Nubes de Puntos
### Prestación: Nube de puntos nativa Proveedor de procesamiento
A new native processing provider has been provided for point cloud algorithms, in line with [QEP 263](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263).

Under the hood provider utilizes the [pdal_wrench](https://github.com/PDAL/wrench) command line tool and currently supports the following algorithms:
- Información: genera metadatos básicos de la nube de puntos (número de puntos, extensión, crs, etc.)
- Convertir formato: convierte la nube de puntos a otro formato, por ejemplo, de las a laz.
- Reproyectar: reproyectar la nube de puntos a un SRC diferente
- Fijar proyección: fijar (asignar) SRC de un archivo de nube de puntos
- Recortar: recorta la nube de puntos recortando polígono(s)
- Fusionar: fusiona varias nubes de puntos en un único archivo
- Mosaico: crea mosaicos a partir de los datos de entrada
- Reducir: crea una versión reducida de la nube de puntos.
- Límites: capa vectorial de exportación que contiene los límites de la nube de puntos
- Density: export a raster file where each cell contains number of points that are in that cell\'s area
- Exportar a ráster: exportar datos de nubes de puntos a una malla ráster 2D
- Exportar a vector: exportar los datos de la nube de puntos a una capa vectorial con puntos 3D.
- Exportar a ráster (TIN): exportar datos de nubes de puntos a una malla ráster 2D utilizando una triangulación de puntos.
- Filer: extraer subconjunto de la nube de puntos mediante expresiones PDAL

As pdal_wrench requires PDAL \>= 2.5.0, the new processing provider will be available only where the PDAL version requirement is satisfied.

![image14](images/entries/e6c8922d1f55cc29aeceb514da8253f9b5b36edf.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Generador de expresiones de nubes de puntos para Procesos
Un nuevo widget de creación de expresiones para nubes de puntos está disponible en la interfaz gráfica de usuario para crear filtros para nubes de puntos de una manera fácil y consistente con las interfaces existentes del Constructor de Expresiones de QGIS.

Within the QGIS API, the `QgsProcessingParameterExpression` parameter has been extended with the types `Qgis` and `PointCloud`. If parameter has a `PointCloud` type, it will use the point cloud expression builder widget. To maintain backward compatibility, by default an expression parameter will use the `Qgis` expression type.

The `QgsPointCloudExpression` class was also extended with a new method to convert QGIS point cloud expressions to [PDAL expressions](https://pdal.io/en/latest/stages/expression.html).

Los algoritmos PDAL existentes que utilizan filtros de expresión se han actualizado para utilizar parámetros de expresión en lugar de cadenas.

![image15](images/entries/f69a04fbddde3eee72333fab2c1af0c58582aaae.webp)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Adición de filtrado por rectángulo y expresión a los algoritmos PDAL
Añadida la opción de filtrar la nube de puntos de entrada por rectángulo (extensión) y expresión en los siguientes algoritmos PDAL:
- contorno
- recortar
- densidad
- exportar a ráster (variantes normal y TIN)
- exportar a vector
- fusionar
- adelgazar

Esto permite procesar sólo un subconjunto de puntos del archivo o archivos de entrada, sin necesidad de realizar un paso de filtrado intermedio ni de generar archivos temporales.

Para aquellos que sólo necesiten filtrar, también existe un algoritmo de Filtro independiente capaz de filtrar por extensión, por expresión o por su combinación.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Nuevo tipo de parámetro para el atributo de nube de puntos
Útil para algoritmos de nubes de puntos que implican atributos, como exportar valores de atributos específicos como ráster o filtrar nubes de puntos.

This also deprecates `parameterAsFields` API call, and `parameterAsStrings` should be used both for fields and point cloud attributes instead.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Visualización de nubes de puntos virtuales (VPC) en vistas 3D
Las nubes de puntos virtuales pueden representarse en vistas 3D. Para la gestión del rendimiento, se especifica un umbral de subíndice para que la vista renderice la entidad fragmentada de la nube de puntos sólo cuando sea apropiado y, en su lugar, renderice la región delimitadora de un subíndice concreto cuando no se cumplan los criterios del umbral.

![image16](images/entries/ec9947c41a6b8caedcf2a72bf7b61ff4f2b8b04e.gif)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Prestación: Nubes de puntos virtuales (VPC)
A new data provider is available for *Virtual Point Cloud* (VPC) files created by the [pdal_wrench](https://github.com/PDAL/wrench) utility and the *Build virtual point cloud (VPC)* tool in the newly introduced [Native point cloud Processing provider](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/263).

The VPC file is handled as a single layer in QGIS and may contain a large number of point cloud files whose indexes are lazy loaded when the canvas is zoomed in enough. An extent renderer is used for the individual indexes while their extent fits the canvas\' width and the user defined renderer is only used when zoomed in further.

A Virtual Point Cloud is a JSON container file with a `.vpc` extension, referring to other files/URLs that contain the actual point cloud data. This is a concept similar to virtual rasters (VRTs) in GDAL. The JSON content is actually a STAC API ItemCollection. See [VPC specification](https://github.com/PDAL/wrench/blob/main/vpc-spec.md) for more details.

![image17](images/entries/ec51218d00c661a9fd68dbda499f13ab56974c6a.gif)

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Diseño de impresión
### Prestación: Soporte de hipervínculos para exportaciones de etiquetas en HTML
Las etiquetas de QGIS con contenido HTML soportarán ahora la incrustación de hipervínculos funcionales en las exportaciones de diseños relevantes, como los PDF.

Esta prestación ha sido financiado por el cantón de Schaffhausen.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Soporte de filtrado de leyendas de diseño por múltiples elementos de mapa vinculados.
En lugar de limitar el filtrado de leyendas a un único mapa vinculado, este cambio permite filtrar las leyendas por varios mapas vinculados. Se ha diseñado para dar cabida al caso de uso en el que un diseño tiene varios mapas, potencialmente a diferentes escalas y mostrando diferentes extensiones, y se requiere una única leyenda que incluya todos los símbolos visibles en todos los mapas.

The UX has been designed to avoid changing the current user workflows, in that legends will still be linked to a single main map item. This map is used when determining the scale (and other map dependent properties) at which to render the legend\'s symbols. Checking the \"Only show items inside linked maps\" option will still automatically filter the legend by the content of the main linked maps. However, there\'s a new \"\...\" options button next to the \"Only show items inside linked maps\" checkbox which allows users to select also other maps from their layout to consider when determining visible items:

![image18](images/entries/3246252a68bf9e6ecbd8d54d20b477305ec8f79a.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Expresiones
### Prestación: Añadir funciones ltrim/rtrim
Permite recortar espacios u otros caracteres sólo del principio o del final de las cadenas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Digitalizando
### Prestación: Lista de valores de campo en el cuadro de diálogo de fusión de objetos espaciales
Al fusionar objetos espaciales, ahora los usuarios pueden seleccionar de una lista de valores disponibles de los objetos espaciales seleccionados, en lugar de capturar manualmente un valor manual para un campo.

![image19](images/entries/01bce8523b3c79ad48ae040c8a5d446c4aa338ae.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Prestación: Ampliación de las opciones de ángulos comunes para digitalización avanzada
Las opciones avanzadas de digitalización de ángulos comunes se han ampliado con las siguientes funcionalidades:
- Nuevos ángulos comunes para 0,1°, 0,5° y 1,0°.
- Se ha añadido una nueva opción para mostrar el ángulo común actual en el widget contextual del flotador.
- New \'N\' \'SHIFT+N\' keyboard shortcuts are available to cycle through the common angle options

![image20](images/entries/7e402e89c5fb13d41c7e1e99d9fa13b51499c571.webp)

Esta prestación ha sido financiada por ChartWorld International.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestaciones: Ajustes de flotador e información de rodamiento para digitalización avanzada
A new configuration setting for the advanced digitizing tool allows users to toggle the display of the \"floater\" contextual menu which follows the cursor during digitizing. Additional options are included for adding information to the floater panel, such as the display of bearing and azimuth information.

![image21](images/entries/1378170e362cd2b7f8ac14cbd5556b87ee593918.gif)

Esta prestación ha sido financiada por ChartWorld International.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Tabla de atributos
### Feature: Improve loading time of attribute tables with hidden fields
Mejorar el tiempo de carga de la tabla de atributos cuando hay campos virtuales ocultos y (de forma más limitada) cuando hay campos no virtuales ocultos.

Esta prestación ha sido financiada por QTIBIA Engineering y QCooperative.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Administración de datos
### Prestación: Permitir copiar un rango de celdas desde la ventana de resultados SQL
Permite seleccionar un rango de celdas para copiarlas en el portapapeles. Los resultados se copian como texto plano y html, por lo que se pueden pegar fácilmente en aplicaciones de hojas de cálculo/etc como tablas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Modificado el comportamiento del diálogo Nuevo campo y soporte de alias
When creating new fields, the \'Comment\' option is now only exposed for datasources which support editing comments (preventing QGIS from silently discarding the information).

Esto también añade soporte para establecer alias de campo dentro del nuevo diálogo de campo, y amplía los comentarios y alias de campo para los formatos OGR soportados.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir el valor DistanceUnit para pulgadas
Las pulgadas se incluyen ahora como unidades cartográficas válidas en QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Registro de la selección de la política de división en el cuadro de diálogo del formulario
A new \"field split policy\" choice item is exposed in the layer properties form dialog. That allows users to easily determine the current policy for splitting a field and change as required.

Se han facilitado las siguientes políticas:
- duplicar valores
- quitar valores
- usar valor predeterminado
- usar proporción de geometrías

![image22](images/entries/f53e5c49ba0c25415b7a5bd163cb94a1ab72ebcd.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Widgets y Formularios
### Prestación: Añadir el control sobre el estiramiento horizontal / vertical para los widgets de formulario de atributos
This functionality exposes two new \"size\" options for edit form widgets, allowing control over the horizontal and vertical stretch factors for the widget. By setting a horizontal or vertical stretch, users can control how edit widgets will relatively resize when resizing an attribute form.

For example, a user can set a higher horizontal stretch value for widgets which should \"grab\" more of the available horizontal space, such as for those widgets which are expected to have longer values. Similarly, the vertical stretch setting (available for select widget types) will control how widgets grow vertically when resizing forms, relative to the form dialog.

Juntas, estas opciones dan más control a los usuarios sobre el diseño y el tamaño exactos de sus formularios de atributos.

By default, the stretch values are set to \"Default\" which is the same as the behavior exhibited in previous versions of QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add new attribute form container type \"Row\"
Este contenedor siempre dispone los widgets hijos en una fila horizontal, donde el número de columnas viene determinado automáticamente por el número de widgets hijos.

It\'s useful for creation of compact forms, where no space will be wasted by assigning extraneous horizontal width to widgets where the expected values will always be short.

Ej: crear 3 filas con 3, 2, 1 widgets child respectivamente da como resultado el diseño:

    Attr 1: [...] Attr 2: [...] Attr 3: [...]
    Attr 4: [..........] Attr 5: [..........]
    Attr 6: [...............................]
    
Sin la opción de contenedores de filas, todas las filas horizontales tendrán el mismo número de columnas, por ejemplo:

    Attr 1: [...] Attr 2: [...] Attr 3: [...]
    Attr 4: [...] Attr 5: [...] Attr 6: [...]
    
(dejando una longitud horizontal insuficiente para los atributos 4-6), o bien

    Attr 1: [..........] Attr 2: [..........]
    Attr 2: [..........] Attr 3: [..........]
    Attr 4: [..........] Attr 5: [..........]
    Attr 6: [..........]
    
(el resultado es un espacio horizontal desperdiciado junto al atributo 6, y una fila adicional que ocupa espacio vertical)

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Procesado
### Prestación: Descarga del algoritmo de azulejos vectoriales
Se ha añadido un nuevo algoritmo de Procesos que permite la descarga de mosaicos vectoriales desde un servidor remoto. Esta funcionalidad incluye el soporte de mosaicos vectoriales para el parámetro de capa de mapa, así como un nuevo parámetro de destino de mosaicos vectoriales para los algoritmos de Procesamiento. Los archivos de formato MBTiles de salida también se pueden añadir automáticamente al lienzo después del procesamiento.

This feature was funded by [Mergin Maps](https://merginmaps.com/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Permite configurar el orden de las salidas creadas por un modelo
A new \"Reorder Output Layers\" action to the model designer menu has been added which allows model creators to set a specific order which the outputs from their model must use when loading the results into a project. This gives the model creator a means of ensuring that layers are logically ordered on the canvas when running a model, such as placing a vector layer output over a raster layer output, or a point layer over a polygon layer.

The model creator can also set an optional \"Group name\" for the outputs for automatically grouping outputs within the layer tree using a new group name or by adding them to an existing group.

![image23](images/entries/a898507ce882d4e757064429471307a3cdd0e0e9.webp)

This feature was funded by [QGIS User Group Germany](https://qgis.de/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Algoritmo de creación de archivos COPC para nubes de puntos de entrada
A new algorithm adds the \"Create COPC\" option to the PDAL provider for generating Cloud Optimized Point Clouds. The algorithm creates a COPC file for each input point cloud file and can be useful for indexing files before using them in QGIS, or when building a VPC.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Añadir herramienta de selección de inversión en la herramienta de procesamiento de campos de refactorización
Se ha añadido un nuevo botón a la interfaz de gestión de campos de la herramienta de procesamiento de campos de refactorización que permite a los usuarios invertir la selección. Esto permite una gestión más eficaz de los campos, como la eliminación masiva de campos.

This feature was added during the [QGIS Contributor Meeting 2023, s-hertogenbosch](https://github.com/qgis/QGIS/wiki/25th-Contributor-Meeting-in-'s-Hertogenbosch)

![image24](images/entries/ab43192e1204465860a221e323f478d9a1e8d2f6.gif)

This feature was funded by [camptocamp](https://camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Prestación: Compatibilidad con comentarios de campo y alias en algoritmos de procesamiento
This adds support for handling field comments and aliases in the processing \"add field to attributes table\" and \"refactor fields\" algorithms. Additionally, it ensures that field comments and aliases are copied from source layers to destination layers when present.

Si las capas de salida no admiten comentarios o alias, se mostrarán advertencias en el registro de procesamiento para informar a los usuarios de esta limitación.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Algoritmo de creación de nubes de puntos virtuales (VPC)
The new algorithm allows user to build [virtual point cloud (VPC)](https://github.com/PDAL/wrench/blob/main/vpc-spec.md) files that reference multiple existing point cloud datasets. This allows then visualization and processing of many point cloud files as a single layer in QGIS.

Additional options are available for the \"Build VPC\" Processing algorithm, which provide the following utilities for building Virtual Point Clouds:
- calcular estadísticas a partir de datos de entrada
- calcular los límites exactos a partir de los datos de entrada
- construir una nube de puntos general

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Gestión de hilos en la configuración de algoritmos
Se ha creado un nuevo y práctico ajuste de configuración del entorno para la configuración del número de hilos que debe utilizar un algoritmo cuando éste es capaz de utilizar varios núcleos, como TauDEM o PDAL.

Esta funcionalidad se ha aplicado a los algoritmos PDAL y TileXYZ.

![image25](images/entries/d5a70cd3ed4a01b2e51381907b92b05256e13cc2.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Permitir cambiar temporalmente la carpeta temporal a través del panel de configuración del algoritmo.
Los algoritmos de procesamiento individuales pueden incluir ahora una configuración de entorno para especificar una carpeta temporal personalizada que sobrescriba la ruta de archivo temporal configurada. Esto resulta útil en situaciones en las que una herramienta concreta puede utilizar mucho espacio de disco temporal y se requiere una ubicación dedicada o un disco de memoria virtual, o cuando una operación concreta requiere mejoras de rendimiento ofrecidas por un disco o ruta concretos.

![image26](images/entries/e36dd209990541e93fdf7a3170596fe0f81ec920.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Permitir que el diálogo de procesamiento anule la configuración predeterminada del contexto de procesamiento
A new \"Algorithm Settings\" action has been added to the Advanced button of the processing algorithms interface. Selecting it shows a panel which allows users to control general processing settings which apply to a **particular instance** of the algorithm execution. It\'s intended to be a place where a user can override their global processing settings on an ad-hoc basis without having to change their usual default settings.

Incluye ajustes para:
- gestión de geometría no válida (a diferencia de la configuración por parámetro existente para esto, la configuración del método de gestión aquí se aplicará a TODAS las entradas del algoritmo)
- unidades de distancia y unidades de superficie que se utilizan para medir distancias y superficies

![image27](images/entries/2039528616fa5e39d98dd01dc43899db654d3a45.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Parámetros adicionales para el algoritmo gdal2xyz
The gdal2xyz processing algorithm from the GDAL processing provider now includes parameters for `skipnodata` and `src`, and `dstnodata`.

This feature was developed by [Luke Pinner](https://github.com/lpinner)
### Feature: Add \"Keep disjoint results separate\" option to buffer algorithm
If checked, then any disjoint parts in the buffer results will be output as separate single-part features. This setting is designed to expose a similar functionality as is available for the \'dissolve\' algorithm.

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Posibilidad de establecer expresiones de filtro para fuentes vectoriales
This change adds a new \"feature filter\" option alongside the existing feature limit and invalid geometry handling options available for all vector inputs to processing layers.

Permite a los usuarios introducir una expresión para subconjuntar la capa dinámicamente al ejecutar la herramienta, evitando la necesidad de pasos separados para establecer filtros de capa o crear subconjuntos de capa.

![image28](images/entries/032c4a9555a7debad18a2fd8fb4b84a09e94eb3b.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support \*.HEIC format images in Processing \"Import Photos\" algorithm
The Import Photos algorithm now allows importing `*.heic` images with GDAL\'s HEIF image support.

This feature was developed by [Chris Shucksmith](https://github.com/shuckc)
## Opciones de Aplicación y Proyecto
### Prestación: Actualización del editor de ajustes
La interfaz de los editores de ajustes ha experimentado una importante revisión y la interfaz de ajustes avanzados presenta los siguientes cambios de cara al usuario:
- La opción de utilizar el widget de configuración antiguo o el nuevo, que se recuerda
- A \"hidden\" setting allows to bypass the warning before showing the settings tree
- Los ajustes tienen editores dedicados (cuadro de giro, casilla de verificación, botón de color, etc.)
- La modificación de los ajustes ahora sólo se ejecuta cuando se pulsa aplicar
- Los ajustes actuales aparecen en cursiva, mientras que los ajustes a los que se aplicarán los cambios aparecen en rojo.

Además, la API de configuración ha experimentado cambios significativos:
- Eliminación de la clase QgsSettingsEntryByValue, utilizando sólo el by reference
- El antiguo QgsSettingsTreeWidget ha sido renombrado a QgsSettingsTreeWidgetOld (en app)

Se han introducido nuevas clases de API:
- QgsSettingsTreeWidget y QgsSettingsTreeModel: widget de árbol + modelo para mostrar y editar la configuración
- QgsSettingsEditorWidgetWrapper (pure virtual): una clase base para crear y manejar un widget editor de configuraciones
- QgsSettingsEditorWidgetWrapperTemplate (puramente virtual): la clase base para la envoltura de ajustes declarados en C++ API (usando métodos tipados)
- Clases para editores de configuraciones: QgsSettingsStringEditorWidgetWrapper, etc.
- QgsSettingsEditorWidgetRegistry: un registro de las envolturas del editor de ajustes.

![image29](images/entries/36a2db1e6a9448a1bdd4699bbeaa79057e912535.webp)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Prestación: Selector de perfil de usuario
En versiones anteriores de QGIS, cuando se cerraba QGIS Desktop, el perfil actual se guardaba en el archivo de configuración profiles.ini, por lo que el perfil predeterminado era el perfil utilizado en la última instancia de QGIS que se había cerrado.

Una nueva prestación Política de selección de usuarios permite a los usuarios seleccionar cómo se definen los perfiles predeterminados, de acuerdo con las tres opciones siguientes:
- Último perfil: El modo heredado que sigue el comportamiento de versiones anteriores. Esto utiliza el último perfil cerrado al abrir una nueva instancia de QGIS.
- Perfil predeterminado: Defina manualmente un perfil predeterminado entre los perfiles existentes que se utilizarán siempre por defecto (sin utilizar un indicador de línea de comandos ni elegir un perfil desde la interfaz de usuario de QGIS).
- Dejar que el usuario elija al inicio

When \"Let user choose\" is selected, if there are 2 or more profiles, a selection dialog is displayed before the SplashScreen which will allow the user to choose which profile to use or to create a new profile which will be loaded automatically.

Independientemente de la política seleccionada, si sólo existe un perfil se utilizará, y si no existe ningún perfil, se creará y utilizará el perfil por defecto.

También se proporcionan iconos de perfil de usuario para que los usuarios puedan diferenciar visualmente sus perfiles activos.

![image30](images/entries/ac274c8186837f23d80df6142030a416efcdcb1e.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Gráficos de Perfil
### Prestación: Selección de unidades de distancia para perfiles de elevación
Los usuarios ahora pueden elegir entre una selección de unidades de distancia para anular la predeterminada (unidades de mapa Lona SRC) para los perfiles de elevación tanto en los perfiles de elevación interactivos (a través del botón de la barra de herramientas de configuración) como para los perfiles de elevación de diseño.

En los perfiles de disposición, existe una opción adicional que controla dónde deben colocarse los sufijos de unidad de distancia. Las siguientes opciones están disponibles para gestionar la visualización de los sufijos de unidad:
- ocultar los sufijos
- mostrar todos los valores
- mostrar el primer valor
- visualización para el último valor
- visualización tanto para el primer valor como para el último.

Note that it is currently not possible to expose unit selection for the vertical axis, as this is currently dimensionless and will require the development of vertical CRS handling in QGIS as outlined in [QEP 267](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/267).

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Exportación de perfiles de elevación
Se ha añadido un nuevo elemento a la barra de herramientas de perfiles de elevación, que incluye varias opciones para exportar perfiles de elevación.

Los trazados de perfil ahora se pueden exportar como:
- Objetos espaciales 3D: exporta la línea de perfil como secciones transversales 3D, con valores z tomados de los cortes de elevación.
- Perfil 2D: exporta el perfil como un gráfico de distancia frente a elevación (es decir, como se muestra en el widget de perfil de elevación).
- Tabla Distancia/Elevación: exporta valores de distancia vs elevación de muestra en forma de tabla.

Los resultados pueden guardarse como archivos DXF, CSV o cualquiera de los formatos espaciales vectoriales estándar grabables shapefile geopackages.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir capas a los perfiles de elevación
1. An explicit \"Add Layers\" button has been added to the elevation profile dock. This provides a user-friendly why of adding new layers to a plot - clicking it will show a filtered list of possible layers which can be added to the plot, but which currently aren\'t in the plot (i.e it will include all raster layers from the project which aren\'t marked as having elevation data). Selecting layers will cause them to automatically be marked as having elevation data and immediately added to the plot.
2. Layers can now be added to elevation plots via drag and drop from the layer tree. Unfortunately, users will have to explicitly hold the \"Ctrl\" key while dragging in order to force the copy action due to upstream library limitations.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add \"Fill Above\" mode for elevation profile drawing
The new fill above drawing mode for profile plots also includes additional options to limit the extent of \"fill above\" and \"fill below\" elevation ranges for a layer.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestaciones: Añadir la opción de bloquear la escala horizontal/vertical para que coincida con las escalas
Cuando está activada, esta opción garantiza que las escalas horizontal y vertical se mantengan siempre iguales. Por ejemplo, una pendiente de 45 grados aparecerá siempre como una pendiente de 45 grados en el perfil.

This feature was funded by [Point cloud processing and 3D data enhancements crowdfunding](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Sensores
### Prestación: Marco básico de sensores
Un marco básico de sensores proporciona un registro de tipos de sensores, un gestor de sensores y tres tipos de sensores simples basados en QIODevice, como se indica a continuación:
- Conexión TCP
- Conexión UDP
- Puerto serie

A las instancias de proyecto se les adjunta un gestor de sensores que permite a los usuarios registrar sensores dentro de sus archivos de proyecto. A diferencia de otras entradas, como un dispositivo de posicionamiento, los sensores se consideran entradas de datos mucho más específicas del proyecto. La gran ventaja de los sensores basados en proyectos es que los hace mucho más portátiles y fáciles de compartir entre usuarios.

A new `sensor_data()` function is added to the project scope which is available using expressions, that returns the latest captured sensor data values for a specific sensor name. An optional expiration (in milliseconds) parameter allows for expressions that will reject a specific sensor value is older that the provided expiration value.

![image31](images/entries/79f13eef3f01b425e4523a9dd9b0922a97712d4f.gif)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Registro de sensores IGU y widgets de configuración
Configuration widgets are provided for the TCP, UDP, and serial port sensor types which will allow users to configure, add, and remove sensors within the project properties dialog\'s sensors panel.

La implementación incluye un registro GUI de sensores para permitir fácilmente la creación de sensores python adicionales y su envío como complementos.

![image32](images/entries/59e82c99ec67a2bd1778543c7fa649a02e5fcf70.webp)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Panel de opciones del sensor dentro del cuadro de diálogo de propiedades del proyecto
Se proporciona un widget de tabla de sensores que muestra los sensores registrados dentro de un proyecto, junto con las acciones para conectar y desconectar los sensores. Se puede acceder a la tabla a través de un nuevo panel de sensores en el cuadro de diálogo de propiedades del proyecto.

![image33](images/entries/e797ad206e4fbb63387d98411d8e08c6a6fe0f47.webp)

This feature was funded by [Sevenson Environmental Services](https://sevenson.com/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Navegador
### Prestación: Establecer comentarios de campo en el navegador
When supported by providers, a new browser context menu action for fields allows for users to set/change the field\'s comments in the datasource.

Actualmente es compatible con formatos OGR con capacidades de comentario de campo como GPKG, ESRI File Geodatabase, NetCDF o Geoparquet, así como con fuentes de datos PostgreSQL.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Establecer alias de campo en el navegador
When supported by providers, a new browser context menu action for fields allows for users to set/change the field\'s alias in the datasource.

Actualmente se admite para formatos OGR con capacidades de comentario de campo como GPKG, ESRI File Geodatabase, NetCDF o Geoparquet.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Proveedores de datos
### Prestación: Carga de capas en hilos paralelos al abrir el proyecto
QGIS cargará ahora las capas soportadas en paralelo al cargar un proyecto, mejorando significativamente los tiempos de carga del proyecto en ciertos casos, como cuando un proyecto incluye numerosas capas remotas.

Para cargar una capa en un hilo de trabajo paralelo, el proveedor de datos de la capa debe soportar la carga paralela (actualmente los proveedores GDAL y PostgreSQL).

Existe un nuevo ajuste avanzado para desactivar este comportamiento cuando sea necesario.

![image34](images/entries/809438ef5d3fd9f3574891be96131f9d113562d9.webp)

This feature was funded by [KoBold Metals](https://www.koboldmetals.com/)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Prestación: Implementa el filtrado del lado del servidor utilizando la Parte 1 o la Parte 3
El proveedor de datos WFS/ OGC API for Features (OAPIF) se ha ampliado para soportar criterios de filtrado mejorados en línea con los estándares abiertos.

Entre las nuevas funcionalidades se incluyen:
- Soporte para el filtrado de las propiedades de los objetos espaciales (Prestaciones de la API OGC Parte 1 - /rec/core/fc-filters). Utiliza el punto final /api para obtener la lista de elementos consultables.
- Soporte para filtrado basado en prestaciones de la API OGC Parte 3 - CQL2-text
- Pasar el SRC seleccionado a la interfaz de usuario del generador de consultas
- Implementar una traducción de la expresión getFeature()

For the CQL2text compatibility, the server `/conformance` implementation is required to declare at least the following data:
- <http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/filter>
- <http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter>
- <http://www.opengis.net/spec/cql2/1.0/conf/cql2-text>
- <http://www.opengis.net/spec/cql2/1.0/conf/basic-cql2>

The `/collections/{collid}/queryables` endpoint is requested to get the queryable properties.

Las clases de conformidad adicionales para el filtrado avanzado incluyen los siguientes elementos:
- <http://www.opengis.net/spec/cql2/1.0/conf/advanced-comparison-operators>: for IN, BETWEEN, LIKE
- <http://www.opengis.net/spec/cql2/1.0/conf/case-insensitive-comparison>: for ILIKE
- <http://www.opengis.net/spec/cql2/1.0/conf/basic-spatial-operators>: for `intersects(geomcolumn, geomFromWkt('POINT(x y)'))` and `bbox_intersects(geomcolumn, geomFromWkt('WKT LITERAL'))`

This feature was developed by [Even Rouault](https://github.com/rouault)
### Prestación: Exponer la opción de cargar fuentes de mosaicos vectoriales desde archivos en el Gestor de fuentes de datos.
The Vector Tile tab now includes choices for selecting from a \"Service\" (the existing, connection based approach for adding vector tiles from online sources) or \"File\" (a new option which allows directly adding a data source using VTPK or MBTiles vector tile files).

![image35](images/entries/d882e2a88732692f8701f27c17fa60c6f376a29e.gif)

Esta prestación ha sido financiada por el Landesamt für Vermessung und Geoinformation, Feldkirch, Austria.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Propiedades adicionales de las baldosas vectoriales controladas por el usuario
Las fuentes de datos de mosaico vectorial admiten ahora controles definidos por el usuario para la opacidad de las capas y los modos de fusión.

Additionally, it adds the standard \"Source\" and \"Rendering\" tabs to the vector tile layer properties dialog. The Rendering tab contains the layer\'s scale based visibility (just like for other layer types), and the source tab contains the layer name, crs override and provider-specific source controls.

Los widgets de origen también son para los proveedores de mosaicos vectoriales VTPK y MBTiles, lo que permite controlar la ruta del archivo vtpk/mbtiles de origen.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestaciones: Arreglar el soporte de capas rotas para capas vectoriales de azulejos vtpk/mbtile, mostrar archivos vtpk en el navegador.
Las capas de mosaico vectorial exponen ahora todos los elementos de API necesarios para soportar el manejo y descubrimiento de capas rotas, haciendo que su comportamiento sea coherente con otros tipos de capas. Además, al implementar las modernas API de metadatos de proveedor para el proveedor VTPK, nos aseguramos de que los archivos VTPK se muestren en el panel del navegador para facilitar su descubrimiento.

Esta prestación ha sido financiada por el Landesamt für Vermessung und Geoinformation, Feldkirch, Austria.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Servidor de QGIS
### Prestación: Opciones de formato PDF para WMS GetPrint
The `FORMAT_OPTIONS` parameter in QGIS Server can now also be used to pass format options for PDF format to WMS GetPrint. This allows more control in GetPrint requests when generating GeoPDF outputs, such as Georeference or Geometry Simplification settings.

This feature was developed by [mhugent](https://github.com/mhugent)
### Prestaciones: Tamaño configurable de la caché de capacidades
The QGIS Server GetCapabilities request cache size can now be configured with the `QGIS_SERVER_CAPABILITIES_CACHE_SIZE` parameter, which uses an integer input specifying the number of requests to cache. A notice of \"Removed cached WMS capabilities document\" will be logged when all slots are taken and a cached document is dropped.

This feature was developed by [Jürgen Fischer](https://github.com/jef-n)
### Prestación: Añadir nombre para mostrar en la respuesta GetFeatureInfo
A new `WITH_DISPLAY_NAME` parameter will add the display name in the `GetFeatureInfo` response if needed, similar to the existing `WITH_MAPTIP` parameter.

This feature was funded by [3liz.com](https://3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Prestación: API OGC - Prestaciones: Añadir paginación completa para la página HTML de elementos de colección
Para facilitar la navegación por los objetos espaciales y proporcionar más información, se ha implementado y añadido a la plantilla HTML lo siguiente:
- paginación completa que muestra siempre el número total de páginas
- tamaño de página configurable mediante menú desplegable
- número de elementos coincidentes
- número de elementos devueltos
- controles de tamaño de página/paginación también en la parte inferior de la página

![image36](images/entries/2fc23a3a7f310ae6cc53ae4ff676c5a96eb8c34a.webp)

This feature was developed by [Björn Hinkeldey](https://github.com/pathmapper)
## Programabilidad
### Prestación: Mejoras en la ayuda de la consola de Python
A special `?` command has been added to the python console which displays a useful help message, identifies some key variables, and provides helper functions for improving the developer experience within QGIS Desktop.

The `_pyqgis` and `_api` helper functions will take a parameter (an instance or class), and will display the matching object page from the QGIS or Qt documentation.

![image37](images/entries/5eae659a4df942e04095e38fa5256e7c1436ae39.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Ejecutar comandos shell desde la consola de Python
La QGIS Python ConsoleMimics IPython comportamiento para ejecutar comandos del sistema.
- Run any command that works at the command-line with the syntax `!<cmd>`. The console will start a subprocess, and forward its output to the Python Console Output.
- Mientras el subproceso se está ejecutando, la entrada de la consola de Python cambia al modo STDIN y reenvía los caracteres introducidos al proceso hijo. Esto hace posible enviar confirmación cuando el programa hijo lo pida.
- Esto proporciona un fácil acceso a comandos como pip para la simple instalación y eliminación de dependencias directamente en el contexto del proyecto QGIS.
- Cuando la consola está en modo STDIN, pulsar Ctrl+C matará el subproceso.
- Affect the result of a command to a variable with the syntax `var = !cmd`

![image38](images/entries/6f4da5dd9d63b6c8e0914c4ad4e7e79ccdfea109.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Reformatear acción de código para editores de código
A \"format code\" action has been added to the Python Console Editor which allows for the automated linting/ pretty printing of code in line with the capabilities of modern code editors.

Los ajustes de configuración adicionales para esta acción incluyen:
- Formatear al guardar: si se activa, el formato se aplica justo antes de guardar el script.
- Ordenar importaciones: Ordenar las declaraciones de importación mediante isort
- Longitud máxima de línea: Controla cómo el formateador envolverá las líneas, y controla la regla del editor.

Las opciones de Formateador permiten seleccionar entre las herramientas autopep8 o black linting y proporcionan las siguientes opciones adicionales:
- Level (autopep8 only) See [Autopep8 aggressiveness level](https://pypi.org/project/autopep8/#more-advanced-usage)
- Normalice las comillas (sólo en negro): Sustituir todas las comillas simples por comillas dobles si es posible.

Las operaciones de ordenación se realizan mediante isort, que permite ordenar las sentencias de importación en tres grupos diferentes:
- standard library imports (re, os, sys, json, \...)
- third-party modules (PyQt5, pandas, dateutil, \...)
- first-party modules (qgis, processing, \...)

Estas operaciones facilitarán un desarrollo coherente en línea con las mejores prácticas del sector y mejorarán la calidad del código, su coherencia, legibilidad y eficacia operativa (especialmente cuando se combinan con sistemas de control de versiones).

![image39](images/entries/4d955fb378b92e625bbfbd84e720d680fecbd063.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Cambiar la consola Python a la ventana principal completa
Añade el mismo botón de alternancia 3d mapa lienzos y tablas de atributos para que sea súper fácil de cambiar la consola de Python a una ventana principal completa o de nuevo a un widget acoplado.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Reformatear código HTML en editores de código
Editors using the `QgsCodeEditorHTML` class will be able to use the code reformatting functionality to pretty print HTML data within QGIS. Note that this functionality will require the BeautifulSoup4 or lxml libraries to be installed within the python environment to parse the XML/ HTML data.

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Correcciones Notables
### Prestación: Corrección de errores por Even Rouault (Spatialys)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Apenas se admiten los ID GeoJSON (sólo se admite la lectura de ID de cadena). | [#53214](https://github.com/qgis/QGIS/issues/53214) | Sólo análisis - arreglo fuera de alcance | unreported - \[cleanup\] QgsOgrFeatureIterator(): remove (hopefully!) useless code in subset string case |
| \"Order by\" memory leak | [#53198](https://github.com/qgis/QGIS/issues/53198) | [PR #53266](https://github.com/qgis/QGIS/pull/53266) | N/D |
| Navegador muy lento al abrir directorio que contiene varios GDB | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53267](https://github.com/qgis/QGIS/pull/53267) | Doesn\'t build with armv7 on openSUSE Tumbleweed |
| Añadir .pgwx como posibles tipos de archivo de mundo para png georreferenciados | [#53125](https://github.com/qgis/QGIS/issues/53125) | [GDAL PR 7864](https://github.com/OSGeo/gdal/pull/7864) | N/A - Corrección GDAL |
| Error de aserción al filtrar una capa GeoParquet | [#53301](https://github.com/qgis/QGIS/issues/53301) | [GDAL PR 7882](https://github.com/OSGeo/gdal/pull/7882) | N/A - Corrección GDAL |
| Los parámetros URL dados no persisten para la conexión WFS OGC API - conexión de características | [#49154](https://github.com/qgis/QGIS/issues/49154) | intentado reproducir - demasiado complicado | Dominio de campo creado incorrectamente |
| Dominio de campo creado incorrectamente | [#52318](https://github.com/qgis/QGIS/issues/52318) | [PR #53314](https://github.com/qgis/QGIS/pull/53314) | [PR #53349](https://github.com/qgis/QGIS/pull/53349) |
| Mayor tiempo de apertura del archivo GPKG en las nuevas versiones | [#53525](https://github.com/qgis/QGIS/issues/53525) | [PR #53566](https://github.com/qgis/QGIS/pull/53566) | PORHACER. |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Prestación: Corrección de errores por Sandro Santilli (strk)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS offset line muestra etiquetas perpendiculares problema | [#53165](https://github.com/qgis/QGIS/issues/53165) | [PR #53234](https://github.com/qgis/QGIS/pull/53234) | [PR #53308](https://github.com/qgis/QGIS/pull/53308) |
| comportamiento extraño del algoritmo de buffer unilateral | [#52795](https://github.com/qgis/QGIS/issues/52795) | [geos PR 912](https://github.com/libgeos/geos/pull/912) | N/A - Corrección GEOS |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](http://strk.kbt.io/)
### Prestación: Corrección de errores por Alessandro Pasotti (itOpen / qcooperative)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| La expresión del filtro de leyenda tiene un contexto incompleto | [#53229](https://github.com/qgis/QGIS/issues/53229) | [PR #53296](https://github.com/qgis/QGIS/pull/53296) | en cola |
| LineString showing offset in CRS 3857 when using Vertex Tool and \"Clip Features to Canvas Extent\" is enabled | [#45200](https://github.com/qgis/QGIS/issues/45200) | [PR #53384](https://github.com/qgis/QGIS/pull/53384) | en cola |
| Qgis Server WMTS devuelve un WGS84BoundingBox erróneo para la capa | [#53213](https://github.com/qgis/QGIS/issues/53213) | No se ejecuta | Form not showing (randomly) values except when triggering \"Editing Mode\" |
| OGC API Features ignores \"X-Qgis-Service-Url\" header | [#53367](https://github.com/qgis/QGIS/issues/53367) | won\'t fix | Corregido el tamaño de la leyenda no se respeta al exportar un diseño |
| Ajustar a vértices aleatorios tras dividir los objetos espaciales | [#53040](https://github.com/qgis/QGIS/issues/53040) | No se ejecuta | Cartographic label placement with \"Distance Offset: From Symbol Bounds\" shows offset for MultiPoint features |
| Layers rendered as a group seem to bypass the \"Lock Layers\" option in my print composer. | [#53379](https://github.com/qgis/QGIS/issues/53379) | [PR #53428](https://github.com/qgis/QGIS/pull/53428) | en cola pero el PR sigue sin revisarse |
| Compositor de diseño de mapas - La expresión del elemento de leyenda no se muestra correctamente | [#53244](https://github.com/qgis/QGIS/issues/53244) | [PR #53434](https://github.com/qgis/QGIS/pull/53434) | no vale la pena, no es crítico |
| opacities parameter doesn\'t apply to labels in GetMap requests | [#48020](https://github.com/qgis/QGIS/issues/48020) | [PR #53438](https://github.com/qgis/QGIS/pull/53438) | en cola pero el PR sigue sin revisarse |
| The list in \"Link to existing child features\" does not help in selecting the right child features | [#53410](https://github.com/qgis/QGIS/issues/53410) | won\'t fix | La fijación de objetos en líneas no funciona con elementos de arco. |
| Attribute form widgets are not disabled when \"Editable\" state is data-defined and layer is not in edit mode | [#53031](https://github.com/qgis/QGIS/issues/53031) | [PR #53506](https://github.com/qgis/QGIS/pull/53506) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Prestación: Corrección de errores por Alex Bruy (LutraConsulting)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[Expressions\]: missing \"//\" operator help | [#52094](https://github.com/qgis/QGIS/issues/52094) | [PR #53355](https://github.com/qgis/QGIS/pull/53355) | [PR #53396](https://github.com/qgis/QGIS/pull/53396) |
| El remuestreo o reescalado de una imagen rasterizada no se puede encontrar en un elemento de menú o en la caja de herramientas de procesamiento. | [#49208](https://github.com/qgis/QGIS/issues/49208) | [PR #53356](https://github.com/qgis/QGIS/pull/53356) | Error producido al cerrar diálogos de algoritmos: RuntimeError: objeto C/C++ envuelto de tipo QgsMapToolCapture ha sido eliminado. |
| Model designer export as/run as python didn\'t catch newline in algorithm comments | [#50715](https://github.com/qgis/QGIS/issues/50715) | [PR #53358](https://github.com/qgis/QGIS/pull/53358) | [PR #53397](https://github.com/qgis/QGIS/pull/53397) |
| Add\' button for adding XYZ layer through Data Source Manager remains disabled | [#52622](https://github.com/qgis/QGIS/issues/52622) | [PR #53359](https://github.com/qgis/QGIS/pull/53359) | [PR #53404](https://github.com/qgis/QGIS/pull/53404) |
| La salida del algoritmo salta arriba a la izquierda al moverse | [#51757](https://github.com/qgis/QGIS/issues/51757) | [PR #53363](https://github.com/qgis/QGIS/pull/53363) | [PR #53402](https://github.com/qgis/QGIS/pull/53402) |
| La columna Nombre siempre muestra el alias en lugar del nombre del campo en el algoritmo de refactorización de campos. | [#53028](https://github.com/qgis/QGIS/issues/53028) | [PR #53365](https://github.com/qgis/QGIS/pull/53365) | [PR #53407](https://github.com/qgis/QGIS/pull/53407) |
| El conjunto de datos Sentinel 1 no funciona correctamente | [#52694](https://github.com/qgis/QGIS/issues/52694) | No se trata de un error, sino de una selección incorrecta del formato de datos para geometrías enormes y complejas. | Generar baldosas XYZ (MBTiles) - error al ejecutar |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alex Bruy (LutraConsulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsRasterIterator.readNextRasterPart() tiene una fuga de memoria | [#53412](https://github.com/qgis/QGIS/issues/53412) | [PR #53444](https://github.com/qgis/QGIS/pull/53444) | [PR #53445](https://github.com/qgis/QGIS/pull/53445) |
| Las opciones de algunos valores en Procesos no se guardan después de cerrar la ventana | [#53204](https://github.com/qgis/QGIS/issues/53204) | [PR #53458](https://github.com/qgis/QGIS/pull/53458) | no |
| No se puede importar la capa de Postgis vista o vista materializada, si no tiene ninguna clave primaria | [#52943](https://github.com/qgis/QGIS/issues/52943) | No es un error |  |
| Vértices no deseados al trazar | [#52935](https://github.com/qgis/QGIS/issues/52935) |  |  |
| El comprobador de topología no resalta todos los errores de solapamiento en el lienzo | [#52903](https://github.com/qgis/QGIS/issues/52903) | [PR #53470](https://github.com/qgis/QGIS/pull/53470) |  |
| No se puede introducir el tamaño del intervalo para el Intervalo fijo en el Renderizador graduado | [#52356](https://github.com/qgis/QGIS/issues/52356) | [PR #53479](https://github.com/qgis/QGIS/pull/53479) | [PR #53508](https://github.com/qgis/QGIS/pull/53508) |
| Las capas de mosaico vectorial no se recortan al marco del mapa de diseño cuando la máscara está activada. | [#52347](https://github.com/qgis/QGIS/issues/52347) | Problema de Qt upstream |  |
| Función Splitfeatures | [#52145](https://github.com/qgis/QGIS/issues/52145) | [PR #53526](https://github.com/qgis/QGIS/pull/53526) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)
### Prestación: Corrección de errores por Jean Felder (Oslandia)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| El trazado del perfil borrado se vuelve a dibujar después de activar/desactivar una capa. | [#48117](https://github.com/qgis/QGIS/issues/48117) | [PR #53468](https://github.com/qgis/QGIS/pull/53468) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Prestación: Corrección de errores por Jacky Volpes (Oslandia)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| La leyenda no se actualiza dinámicamente al utilizar un atlas | [#53442](https://github.com/qgis/QGIS/issues/53442) | Todavía WIP |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes (Oslandia)](https://oslandia.com/)
### Prestación: Corrección de errores por Nyall Dawson (North Road)
| Título del Error | Problemas de URL (Github, si se ha informado) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Muchas correcciones de regresiones en pantallas hidpi siguiendo el enfoque mejorado implementado para 3.32 | Múltiple | [PR #53556](https://github.com/qgis/QGIS/pull/53556) , [PR #53533](https://github.com/qgis/QGIS/pull/53533) , [PR #53531](https://github.com/qgis/QGIS/pull/53531) | [PR #53517](https://github.com/qgis/QGIS/pull/53517) |
| Implementar soporte adecuado para los nuevos formatos de archivo vsi añadidos en GDAL 3.7 | [PR #53515](https://github.com/qgis/QGIS/pull/53515) | NA |  |
| Almacenar credenciales postgres actualizadas en fuente de capa | [#37632](https://github.com/qgis/QGIS/issues/37632) | [PR #53465](https://github.com/qgis/QGIS/pull/53465) | NA |
| Limpieza de las conexiones de señal de iface al descargar el complemento de procesamiento | [#53455](https://github.com/qgis/QGIS/issues/53455) | [PR #53461](https://github.com/qgis/QGIS/pull/53461) | Demasiado arriesgado / poca recompensa |
| Evitar el bloqueo de la interfaz de usuario al cerrar la ventana Ejecutar SQL | No reportado | [PR #53448](https://github.com/qgis/QGIS/pull/53448) | Demasiado arriesgado |
| Limpieza de archivos de registro python faulthandler vacíos | [#50609](https://github.com/qgis/QGIS/issues/50609) | [PR #53417](https://github.com/qgis/QGIS/pull/53417) | Demasiado arriesgado |
| Corrección de un fallo al cerrar QGIS | No reportado | [PR #53414](https://github.com/qgis/QGIS/pull/53414) | [PR #53418](https://github.com/qgis/QGIS/pull/53418) |
| Limpiar correctamente los ficheros de archivo del proyecto antes de intentar borrar/reemplazar el archivo. | [#53034](https://github.com/qgis/QGIS/issues/53034) | [PR #53400](https://github.com/qgis/QGIS/pull/53400) | Demasiado arriesgado |
| Don\'t open datasets when populating browser directories to determine layer drop support | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53398](https://github.com/qgis/QGIS/pull/53398) | Aplazado |
| Corregir fallo al escribir la entrada del historial de procesamiento | No reportado | [PR #53394](https://github.com/qgis/QGIS/pull/53394) | NA |
| Corrección de un problema por el que se ignoraba la selección de SRC | [#53309](https://github.com/qgis/QGIS/issues/53309) | [PR #53393](https://github.com/qgis/QGIS/pull/53393) | Arreglar iconos de estilo borrosos en el diálogo de propiedades del proyecto en pantallas hidpi. |
| La corrección de proveedor de grass apunta a documentos de ayuda obsoletos | [#53105](https://github.com/qgis/QGIS/issues/53105) | [PR #53372](https://github.com/qgis/QGIS/pull/53372) | [PR #53375](https://github.com/qgis/QGIS/pull/53375) |
| Corrección de problemas de rotación y alineación de anotaciones de texto. | No reportado | [PR #53337](https://github.com/qgis/QGIS/pull/53337) | NA |
| Ampliar el rango de giro del índice z para las anotaciones | No reportado | [PR #53319](https://github.com/qgis/QGIS/pull/53319) | [PR #53326](https://github.com/qgis/QGIS/pull/53326) |
| Corrección de la escala incorrecta de los marcadores de fondo de texto en las anotaciones. | No reportado | [PR #53318](https://github.com/qgis/QGIS/pull/53318) | Arreglar fallo en rutas de capa de hierba no válidas |
| Marcar carpetas remotas de OneDrive como remotas, lentitud para abrir rutas en Windows | [#51710](https://github.com/qgis/QGIS/issues/51710) | [PR #53315](https://github.com/qgis/QGIS/pull/53315) | Demasiado arriesgado |
| Fix crash when creating new grass mapsets when \"set\" is pressed and no region is selected | No reportado | [PR #53293](https://github.com/qgis/QGIS/pull/53293) | [PR #53311](https://github.com/qgis/QGIS/pull/53311) |
| Corrección de los resultados de las pruebas de transformación de coordenadas personalizadas | [#52184](https://github.com/qgis/QGIS/issues/52184) | [PR #53292](https://github.com/qgis/QGIS/pull/53292) | [PR #53353](https://github.com/qgis/QGIS/pull/53353) |
| Don\'t create alpha bands for non-rotated, south up rasters | [#50879](https://github.com/qgis/QGIS/issues/50879) | [PR #53290](https://github.com/qgis/QGIS/pull/53290) | [PR #53310](https://github.com/qgis/QGIS/pull/53310) |
| Acelera enormemente el navegador cuando se ve un gran número de archivos | [#53265](https://github.com/qgis/QGIS/issues/53265) | [PR #53268](https://github.com/qgis/QGIS/pull/53268) | [PR #53299](https://github.com/qgis/QGIS/pull/53299) |
| Pasar el uso del renderizador del algoritmo de descarga de mosaicos vectoriales | [#53183](https://github.com/qgis/QGIS/issues/53183) | [PR #53258](https://github.com/qgis/QGIS/pull/53258) | NA |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)

{{<content-end >}}
