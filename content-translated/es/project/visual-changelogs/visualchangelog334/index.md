---
HasBanner: false
draft: false
releaseDate: '2023-10-29'
section: proyecto
sidebar: true
title: Registro de cambios de QGIS 3.34
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios de QGIS 3.34{#changelog334 }
![image0](images/entries/334splash.webp)

Fecha de lanzamiento: 2023-10-29

Presentamos QGIS 3.34, una importante versión del proyecto QGIS que aporta mejoras significativas a las capacidades del software de análisis y visualización de datos geoespaciales de código abierto QGIS.

Esta versión incluye una serie de mejoras en las API, expresiones y herramientas existentes, modificaciones en el diseño de impresión y mejoras en las opciones de renderizado tanto en 2D como en 3D.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=LHFVo0edaXE>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/LHFVo0edaXE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is a community effort, and we would like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS es software libre y no hay obligación de pagar nada por utilizarlo; de hecho, queremos animar a todo el mundo a que lo use, independientemente de su situación económica o social. Creemos que dotar a las personas de herramientas para la toma de decisiones espaciales redundará en una sociedad mejor para toda la humanidad.
## Azulejos 3D Cesium
Thanks to an ecosystem grant from the [Cesium](https://www.cesium.com/) project, QGIS now has support for loading in 3D content in the Cesium 3D Tiles format! Tiles can be loaded from either local or remote datasources (including the Cesium ion platform and the Google Earth photorealistic tiles), and are visible in both 2D and 3D map views. In 2D views users can control the appearance of tile content by styling in either their original textures or in a wireframe view of the tile geometries, and users also have control over the desired level of detail in both 3D and 2D views.

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/lvl8zVZ8glY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

This feature was developed by [Martin Dobias](https://github.com/wonder-sk) and [Nyall Dawson](https://github.com/nyalldawson)
## Herramientas de mapa
### Feature: Optional enforcement of \"dot\" as decimal separator for measure tool
A new `Always use decimal point` checkbox option has been added to the Measure Tool. This option will ensure that measurements and coordinates are copied to the clipboard using a decimal point (dot) separator, even if the current locale uses a comma.

Esto permite copiar datos separados por comas (csv) incluso en casos en los que la configuración regional del usuario utiliza una coma como separador decimal.

![image1](images/entries/ec6084247b2b698045a783e2b007b0e0dde90ddd.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Mostrar un resalte en los píxeles ráster identificados al utilizar la herramienta de identificación.
QGIS muestra ahora la geometría del resultado del objeto espacial identificado para píxeles ráster en el lienzo del mapa. Esto coincide con el comportamiento existente de la herramienta de identificación con los tipos de características vectoriales, de mosaico vectorial y de nube de puntos.

This is useful when a identifying a raster which has sections of similar colored pixels and it\'s difficult to visually determine the exact extent of a pixel.

![image2](images/entries/dc219caa150c9bbcb15aece90744f63e54ec25a1.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mostrar la fila/columna de trama del punto seleccionado en los resultados de la identificación
Al utilizar la herramienta de identificación en capas ráster, los resultados derivados incluirán ahora el número de fila y columna del píxel identificado.

![image3](images/entries/0889d275dfefea4c7c7d13ebc5dc6fd237573076.webp)

This feature was developed by [Hannes & Nyall Dawson](https://github.com/kannes)
## Simbología
### Prestación: Ajustes para anular el color de selección y el símbolo de selección de las capas vectoriales
Los nuevos ajustes de representación de capas permiten a los usuarios controlar el color y el símbolo que se utilizarán en lugar de los predeterminados del sistema o del proyecto al resaltar las prestaciones seleccionadas.

Este ajuste se define para cada capa y es útil para mejorar la visibilidad de los objetos espaciales seleccionados mediante la aplicación de una simbología definida explícitamente.

Esto es útil en varios escenarios, incluyendo casos en los que:
- La capa utiliza un color o estilo de símbolo que coincide con la simbología de la selección, por lo que la selección del objeto espacial no es visible.
- Una capa de línea utiliza un símbolo fino, y colorear las líneas seleccionadas no las hace lo suficientemente visibles
- A las capas con simbología compleja (como ráster/rellenos de degradado/ líneas/ shapeburst con una rampa de color) no se les aplicaba un color de selección por defecto. En estos casos, el usuario puede especificar un símbolo más sencillo para las prestaciones seleccionadas en la capa.

![image4](images/entries/c648e5905c6c69e7a1e7c1dc91e3a15de1c8d523.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Etiquetando
### Prestación: Conmutar etiquetas para capas de mosaico vectorial
Ahora, los usuarios pueden alternar las etiquetas de las capas de mosaico vectorial mediante el panel de estilo de capas de mosaico vectorial y el menú contextual de capas del índice del panel de capas, replicando así las funciones de alternancia de etiquetas de las capas vectoriales.

This functionality is enabled by the addition of new functions to the `QgsVectorTileLayer` API by replicating the existing functionality on `QgsVectorLayer`.

![image5](images/entries/9e04c9c98886edf1d34eeb9750dc8f5c94946b51.gif)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Representación
### Feature: \"Sticky\" Map Decorations
Dynamic map decorations are now rendered to a transparent overlay, preventing re-rendering of decoration objects (such as title or scale bar) during navigation. The `QgsMapDecoration` now also includes `hasFixedMapPosition` to fix a decoration to a geographic location.

![image6](images/entries/00e6bc11fa3025317740f955962ef50cc1b95336.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Añadir perfilador de renderizado de mapas
The debugging/ development profiling tools have been extended with a new \"map render\" profile (accompanying the existing Startup and Project Load profiles).

Gracias a esta herramienta, los usuarios pueden identificar los puntos débiles en la representación de sus mapas y saber exactamente qué capas están provocando redibujos prolongados.

![image7](images/entries/50fd809522d42944942ca7a059807f59fdcec5d2.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add choice of two different modes for \"Refresh Layer at Interval\"
When using \"Refresh Layer at Interval\" on vector layers, previous versions of QGIS would simply redraw the layer (for animations etc.), without refreshing data from the data source.

Se proporciona un nuevo widget que permite a los usuarios seleccionar las opciones de actualización de capas según su caso de uso preferido:
- \"Reload Data\": The layer will be completely refreshed. Any cached data will be discarded and re-fetched from the provider. This mode may result in slower map refreshes.
- \"Redraw Layer Only\": This mode is useful for animations or when the layer style should be updated at regular intervals. Canvas updates are deferred in order to avoid refreshing multiple times if more than one layer has an automatic update interval set.

![image8](images/entries/e0b0d4561cf7963d9a16bef9f77ea8214fe15f7b.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Objetos 3D
### Prestación: Permitir la configuración del límite de memoria de la GPU
Ahora los usuarios pueden configurar el límite de memoria de la GPU en cada capa (antes estaba fijado en 500 MB por entidad/capa).

También se muestra una advertencia cuando se alcanza un límite, lo que debería ayudar en la resolución de problemas en escenas grandes.

Esta funcionalidad es útil para los usuarios que utilizan grandes escenas 3D que agotan los recursos de memoria disponibles en la GPU.

![image9](images/entries/161c61a6ec3ca078e4483279c54f25319bed2c20.webp)

This feature was developed by [Martin Dobias](https://github.com/wonder-sk)
### Prestación: Añadir soporte para boundingbox3d
Additional API methods for relevant geometry classes are now available for `boundingBox3D` and `calculateBoundingBox3D`, as well as extensions to `boundingBoxIntersects` methods which will now support checking intersections between 3D bounding boxes.

This feature was developed by [Jean Felder](https://github.com/ptitjano)
## Diseño de impresión
### Prestación: Seleccionar varios elementos de diseño
Se proporciona una nueva funcionalidad para gestionar la selección de varios elementos simultáneamente desde la lista de elementos dentro de los diseños de impresión.

Esto también mejora la experiencia del usuario de la funcionalidad existente de selección múltiple que está disponible con las selecciones visuales al mantener la selección de elementos sincronizada con la lista de elementos.

![image10](images/entries/85d915ba102341669b4ccccab308a987b0927d68.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Diseño El número de página se refleja en las propiedades de la página
When a layout has more than one page, the current page number will be displayed in the item properties header section using the format `page_number`/`pagecount`.

![image11](images/entries/367986f087f878b47fe1296fcd8143ef677b3430.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Apertura automática de diseños exportados
A new \"Open file after exporting\" checkbox option has been added to the export options for PDF, SVG, and Image output types. When selected this option will attempt to automatically open the output file once the export is completed.

The application used to open the file will use the configured default application on the system based on type (using `QDesktopServices::openUrl`). This feature will leverage the user settings API to remember the selection for the active user profile.

![image12](images/entries/502d122401e26d6dca10146dbdb9ccd1b01e8bd3.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Expresiones
### Prestación: Añadir función de expresión de rodamiento
A new `bearing` function has been added which computes the bearing angle (in radians) between two points.

El rumbo se determina en el SRC dado y se mide en el sentido de las agujas del reloj en el elipsoide dado.

![image13](images/entries/a1d3176b8434f43bb248926df46c406f4b5f2625.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Add \"layer_crs_ellipsoid\"
QGIS expressions now include a `layer_crs_ellipsoid` layer variable, as well as the `crs_ellipsoid` property available from the `layer_property` function. The value returned will be the ellipsoid acronym of the layer CRS.

![image14](images/entries/25fa0e9a64d6d1ea6b22e0e9b29ced356bbc96c8.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Digitalizando
### Feature: Improve \"avoid overlap\" type awareness
When digitizing features with the \"avoid overlap\" option, QGIS has improved the behavior of automatically coercing the feature type and includes more meaningful messages to notify users of the automated behaviours.

Un ejemplo de uso sería la digitalización de un polígono multiparte en una capa de destino de polígono de una sola parte, que no se puede guardar. QGIS ahora sólo guardará automáticamente la porción geométrica más grande, y pedirá a los usuarios que restauren opcionalmente los objetos espaciales adicionales como polígonos de una sola parte.

This prevents the digitizing of \"sliver\" polygons and frustrations with improper feature types.

![image15](images/entries/e86392da95484a83eb7edbfd554526865d4195ff.gif)

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
## Administración de datos
### Prestación: Mejora de la gestión de objetos espaciales vectoriales para archivos preexistentes
Cuando se utilice el algoritmo de guardar objetos espaciales vectoriales en un archivo, QGIS informará a los usuarios del comportamiento predeterminado para el manejo de archivos preexistentes (sobrescritura de archivos) y ofrecerá la posibilidad de seleccionar entre una serie de comportamientos alternativos (como sobrescribir la capa o añadir nuevos objetos espaciales a la capa existente).

Esto mejora en gran medida la capacidad de los usuarios para gestionar datos utilizando formatos de almacenamiento de datos de archivos planos como geopackage, al tiempo que minimiza el riesgo de pérdida de datos o efectos secundarios no deseados.

![image16](images/entries/2eaef470fbd823689e50cfd9fde3a747b888bc83.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Mantener relaciones para objetos espaciales copiados
La nueva funcionalidad garantiza que los objetos espaciales copiados dentro de la misma capa seguirán respetando la solidez de la relación o relaciones del proyecto.

Al copiar objetos espaciales dentro de la misma capa vectorial utilizando el mapa, la tabla de atributos o la herramienta copiar/mover objeto(s) espacial(es), QGIS ahora rastreará cualquier relación dentro del proyecto abierto y duplicará los objetos espaciales con las relaciones intactas.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Herramientas de análisis
### Prestación: Admite la descripción de bandas ráster
QGIS mostrará ahora las descripciones de las bandas en la pestaña de simbología de las capas ráster, además del número de banda.

![image17](images/entries/5a45eb1db489ef62f677a745efcca6c07935c4e8.webp)

Esta prestación ha sido financiada por El verano es cada vez más cálido.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Procesado
### Prestación: Configuración de antialias para el complemento de procesamiento de mosaicos ráster
A new \"Enable antialiasing\" parameter has been added to the \"Generate XYZ Tiles\" processing tool.

Esta opción estará activada por defecto (replicando el comportamiento actual) pero permitirá a los usuarios desactivar el antialiasing del contenido del mapa.

![image18](images/entries/9c9b07222673e23caf2dcc73ff1db8a8f9257106.webp)

This feature was developed by [ASAI Hitoshi](https://github.com/hito-asa)
### Feature: Create Grid row_index and col_index fields
Fields for the `row_index` and `col_index` have been added to the output of the \"Create Grid\" processing algorithm. The fields are added to all outputs of type point, rectangle, and hexagon.

Los valores de campo son números enteros cuya cuenta comienza en 0 y se incrementa de izquierda a derecha (índice de columna) y de arriba abajo (índice de fila).

![image19](images/entries/54157595e9bf9c58b4b906ea28b3c335a737696b.webp)

This feature was developed by [Valentin Buira](https://github.com/Poulpator)
### Feature: New \'Calculate expression\' algorithm for use in models
The new \"Calculate expression\" algorithm will calculate the results of a QGIS expression and make the result available for use in other parts of the model.

Evita la necesidad de utilizar la misma expresión varias veces a lo largo de un modelo si es necesario utilizar el mismo resultado más de una vez y proporciona casos de uso adicionales (como la generación de un valor de fecha y hora estático para su uso a lo largo de un modelo).

![image20](images/entries/90b9d8da0ec1f13c638525cedd360a5c65d89c1a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Se añade un algoritmo para convertir el contenido de un archivo GLTF/GLB en objetos espaciales de capa vectorial estándar.
QGIS permite ahora la conversión de contenido de teselas 3D en formatos GLTF y GLB a formatos de prestaciones vectoriales editables.

![image21](images/entries/6c95d6382b9e6abe72607df57dfefb8a4d9e8442.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Port SAGA \"DTM Filter (slope-based)\" tool to a native QGIS algorithm
The SAGA [DTM Filter tool](https://saga-gis.sourceforge.io/saga_tool_doc/8.1.0/grid_filter_7.html) has been ported to a native QGIS algorithm.

![image22](images/entries/740fdd036b19e5e0d2c13493d66e785fca89b46a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Opciones de Aplicación y Proyecto
### Prestación: Borrar la lista de proyectos abiertos recientemente
A \"Clear Recently Opened\" action is now listed at the bottom of the `Project → Open Recent` menu, which will remove every unpinned project from the menu.

An additional context menu is also available to enable the ability to remove individual projects from the recent project list, as well as \"pin\" and \"unpin\" items.

El estado se sincronizará entre el menú de proyectos recientes y la página de bienvenida de QGIS.

![image23](images/entries/4ff4dd8614e4857810fc1b636d8700b143ec98b6.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Código de autorización OAUTH2 PKCE
An implementation of Proof Key for Code Exchange (PKCE, [RFC 7636](http://tools.ietf.org/html/rfc7636)) has been added for OAUTH2 [Authorization Code](https://oauth.net/2/grant-types/authorization-code/) flows, improving resilience to CSRF and code injection attacks.

Esta prestación ha sido financiada por el Ayuntamiento de Roma.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Establecimiento de valores predeterminados de procesamiento desde el archivo de configuración de QGIS
QGIS admite ahora la capacidad de configurar los valores predeterminados de las herramientas GUI dentro del marco de procesamiento de QGIS mediante parámetros especificados en el archivo de configuración QGIS.ini.

This allows for the configuration of user-specific or organization-wide default values for certain algorithms. For example, to set the default value of the GRID_SIZE (precision) parameter on the intersection algorithm, the following configuration may be added to the `QGIS/QGIS3.ini` in the active user profile directory root:

    [Processing]
    DefaultGuiParam\native%3Aintersection\GRID_SIZE=0.01
    
Cuando un usuario con esta configuración abra la caja de herramientas correspondiente para ejecutar un algoritmo, se le especificará automáticamente el valor por defecto.

This feature was developed by [mhugent](https://github.com/mhugent)
## Gráficos de Perfil
### Prestación: Adición de un ajuste para controlar el color de fondo de los gráficos de perfiles de elevación
Esta opción (disponible en la nueva pestaña Configuración → Opciones → Elevación) permite a los usuarios establecer un color específico para utilizarlo como color de fondo en los perfiles de elevación.

Esto puede hacer que el gráfico sea más legible para ciertos conjuntos de datos, por ejemplo, nubes de puntos con coloración RGB, donde el color de fondo por defecto es demasiado similar a los colores de los puntos para ser fácilmente discernible.

Se trata de un ajuste opcional y, por defecto, los perfiles de elevación seguirán mostrándose con el color de fondo estándar del sistema.

![image24](images/entries/e3bae5cc601894eca9775d5603cc3af6bd03c747.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Proveedores de datos
### Prestación: Descubrir relaciones para el proveedor Oracle
QGIS admite ahora el descubrimiento automatizado de relaciones para el proveedor de datos Oracle.

![image25](images/entries/951d7ccce5b34532595a21373d721f581938c65b.webp)

Esta prestación fue financiada por Métropole de Lille

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
## Plugins
### Prestación: Eliminar el shell interactivo del complemento C++ de GRASS
Por razones de mantenimiento, el shell interactivo para el Complemento C++ de GRASS, así como el QTermWidget incrustado, han sido eliminados de futuras versiones.

Se espera que el complemento de procesamiento de GRASS reciba un desarrollo prioritario y soporte de mantenimiento en el futuro, y proporcionar un shell interactivo de GRASS no es una funcionalidad crítica para el propio QGIS, sino más bien algo que los usuarios pueden gestionar externamente.

Further details on the specifics of this feature cleanup can be found on the feature [Pull Request](https://github.com/qgis/QGIS/pull/53597).

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Programabilidad
### Prestación: Función para exportar como texto el contenido del modelo del perfilador en tiempo de ejecución
A new function has been added to allow for the export of the current runtime profiler (`QgsRuntimeProfiler`) model content as a multi-line text string.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti (itOpen / qcooperative)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS cannot connect to MySQL if user\'s password contains commas. | [#54493](https://github.com/qgis/QGIS/issues/54493) | [PR #54573](https://github.com/qgis/QGIS/pull/54573) | No |
| QGIS WFS server will look for .qgz file in wrong place if \"map\" is in path | [#54533](https://github.com/qgis/QGIS/issues/54533) | [PR #54639](https://github.com/qgis/QGIS/pull/54639) | [PR #54855](https://github.com/qgis/QGIS/pull/54855) |
| La transparencia/opacidad de la capa de ráster no se almacena en el estilo guardado | [#54496](https://github.com/qgis/QGIS/issues/54496) | [PR #54644](https://github.com/qgis/QGIS/pull/54644) | [PR #54854](https://github.com/qgis/QGIS/pull/54854) |
| WMS GetPrint with ATLAS_PK has incorrect layers visibility in versions \>= 3.22 | [#54475](https://github.com/qgis/QGIS/issues/54475) | [PR #54651](https://github.com/qgis/QGIS/pull/54651) | [PR #54663](https://github.com/qgis/QGIS/pull/54663) |
| Error al guardar edición en geometría PostGIS cuando la tabla también contiene geografía | [#54572](https://github.com/qgis/QGIS/issues/54572) | [PR #54664](https://github.com/qgis/QGIS/pull/54664) | [PR #54714](https://github.com/qgis/QGIS/pull/54714) |
| No se pueden restar o sumar ángulos ya que se ha añadido el símbolo de grados | [#54501](https://github.com/qgis/QGIS/issues/54501) | [PR #54687](https://github.com/qgis/QGIS/pull/54687) | N/D |
| WCS Mantener capas no disponibles | [#54702](https://github.com/qgis/QGIS/issues/54702) | [PR #54707](https://github.com/qgis/QGIS/pull/54707) | N/D |
| leyenda de taxones del atlas map whis | [#54654](https://github.com/qgis/QGIS/issues/54654) | [PR #54692](https://github.com/qgis/QGIS/pull/54692) | N/D |
| Spinbox para colum espacio en leyendas no permite establecer valores por encima de 99,99 unidades | [#54682](https://github.com/qgis/QGIS/issues/54682) | [PR #54709](https://github.com/qgis/QGIS/pull/54709) | N/D |
| Error de geometría Base de datos SpatiaLite | [#54662](https://github.com/qgis/QGIS/issues/54662) | [PR #54734](https://github.com/qgis/QGIS/pull/54734) | N/D |
| Dividir MultiLineStrings da resultados extraños | [#54155](https://github.com/qgis/QGIS/issues/54155) | [PR #54744](https://github.com/qgis/QGIS/pull/54744) | [PR #54851](https://github.com/qgis/QGIS/pull/54851) |
| Abrir proyecto, luego propiedades de capa, cerrar, cerrar proyecto: qgis piensa que algo ha cambiado | [#54741](https://github.com/qgis/QGIS/issues/54741) | [PR #54757](https://github.com/qgis/QGIS/pull/54757) | N/D |
| El campo Anchura de las tablas de atributos en los diseños de impresión sólo utiliza la configuración regional cuando se edita. | [#54204](https://github.com/qgis/QGIS/issues/54204) | [PR #54769](https://github.com/qgis/QGIS/pull/54769) | [PR #54781](https://github.com/qgis/QGIS/pull/54781) |
| Administrador de fuentes de datos - Navegador: Faltan los botones Cerrar y Ayuda | [#54171](https://github.com/qgis/QGIS/issues/54171) | [PR #54770](https://github.com/qgis/QGIS/pull/54770) | N/D |
| 0 puerto en OAuth2 callback URI | [#54562](https://github.com/qgis/QGIS/issues/54562) | No puede reproducir | N/D |
| QGIS falla al editar simultáneamente varias características que tienen un campo de relación de valores. | [#54164](https://github.com/qgis/QGIS/issues/54164) | [PR #54889](https://github.com/qgis/QGIS/pull/54889) | PORHACER. |
| Falla al reproducir leyendas duplicadas en el diseño | [#52268](https://github.com/qgis/QGIS/issues/52268) | [PR #54947](https://github.com/qgis/QGIS/pull/54947) |  |
| QGIS falla al solicitar más de una capa WMS | [#55042](https://github.com/qgis/QGIS/issues/55042) | [PR #55064](https://github.com/qgis/QGIS/pull/55064) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti (itOpen / qcooperative)](https://www.qcooperative.net/)
### Prestación: Corrección de errores por Even Rouault (Spatialys)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgsgeos.cpp: corrección de la advertencia -Wunused-variable | no reportado | [PR #54612](https://github.com/qgis/QGIS/pull/54612) | N/D |
| qgsvirtualpointcloudprovider.cpp: añadir una inicialización de variable que faltaba | no reportado | [PR #54613](https://github.com/qgis/QGIS/pull/54613) | N/D |
| La OAPIF no respeta el alcance de la vista | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053400.html) | [PR #54617](https://github.com/qgis/QGIS/pull/54617) | [PR #54792](https://github.com/qgis/QGIS/pull/54792) |
| Does QGIS require units \"m\" for the projection coordinate variables in a netCDF/CF file? | [QGIS user mailing list](https://lists.osgeo.org/pipermail/qgis-user/2023-September/053413.html) | [GDAL PR 8407](https://github.com/OSGeo/gdal/pull/8407) | N/D |
| Error sintáctico con el uso de == en lugar de = para la comparación en la cláusula WHERE | [#54608](https://github.com/qgis/QGIS/issues/54608) | Ya corregida | No se pueden escribir capas adicionales en una FGDB existente. |
| Añadir información SRC mínima a las exportaciones sqlite | [#54560](https://github.com/qgis/QGIS/issues/54560) | [PR #54630](https://github.com/qgis/QGIS/pull/54630) | [PR #54715](https://github.com/qgis/QGIS/pull/54715) |
| Los atributos complejos de los Feature-Items de la API OGC tienen contenido vacío | [#54275](https://github.com/qgis/QGIS/issues/54275) | [PR #54631](https://github.com/qgis/QGIS/pull/54631) | [PR #54679](https://github.com/qgis/QGIS/pull/54679) |
| Proveedor GPX: falta un elemento al importar un archivo gpx | [#54119](https://github.com/qgis/QGIS/issues/54119) | [PR #54632](https://github.com/qgis/QGIS/pull/54632) | N/D |
| Guardar ediciones en capas vectoriales grandes es lento | [#53043](https://github.com/qgis/QGIS/issues/53043) | [PR #54633](https://github.com/qgis/QGIS/pull/54633) | N/D |
| QgsVectorLayerSaveAsDialog: uncheck \'Add saved filed to map\' when selecting PGDump driver (refs #54548) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | [PR #54647](https://github.com/qgis/QGIS/pull/54647) | No merece la pena |
| Filtrado espacial de polígonos multiparte dentro de un conjunto de datos shapefile roto | [GDAL issue 8481](https://github.com/OSGeo/gdal/issues/8481) | No es un error |  |
| qgis no puede encontrar/identificar un objeto espacial poligonal haciendo clic en una parte (multi)poligonal recién creada. | [#54537](https://github.com/qgis/QGIS/issues/54537) | [PR #54761](https://github.com/qgis/QGIS/pull/54761) | [PR #54782](https://github.com/qgis/QGIS/pull/54782) |
| qgis no puede encontrar/identificar un objeto espacial poligonal haciendo clic en una parte (multi)poligonal recién creada. | [#54537](https://github.com/qgis/QGIS/issues/54537) | [GDAL PR 8483](https://github.com/OSGeo/gdal/pull/8483) | [GDAL PR 8503](https://github.com/OSGeo/gdal/pull/8503) |
| Exportar a hoja de cálculo crea un archivo xlsx con errores al exportar tablas/capas vacías | [#42945](https://github.com/qgis/QGIS/issues/42945) | [GDAL PR 8484](https://github.com/OSGeo/gdal/pull/8484) | [GDAL PR 8515](https://github.com/OSGeo/gdal/pull/8515) |
| exportar bbox mal cuando la característica cruza el anti-prime-meridion (180 grados) | [#42827](https://github.com/qgis/QGIS/issues/42827) | [GDAL PR 8485](https://github.com/OSGeo/gdal/pull/8485) | No merece la pena |
| QgsVectorDataProvider.changeAttributeValues() devuelve True incluso cuando falla | [#54816](https://github.com/qgis/QGIS/issues/54816) | [PR #54905](https://github.com/qgis/QGIS/pull/54905) | [PR #54909](https://github.com/qgis/QGIS/pull/54909) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com/)
### Prestación: Corrección de errores por Paul Blottiere (Hytech-imaging)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corrección de fallos en la transformación de coordenadas | no reportado | [PR #54609](https://github.com/qgis/QGIS/pull/54609) | N/D |
| Wrong rendering for HIGHLIGHT_LABEL_ROTATION above 89° | [#54598](https://github.com/qgis/QGIS/issues/54598) | [PR #54667](https://github.com/qgis/QGIS/pull/54667) | N/D |
| Conexión de cadena de base de datos visible en la barra de mensajes/registros de QGIS | [#54437](https://github.com/qgis/QGIS/issues/54437) | [PR #54650](https://github.com/qgis/QGIS/pull/54650) | N/D |
| PostGIS Connection\'s \"Session ROLE\" is not kept | [#54638](https://github.com/qgis/QGIS/issues/54638) | [PR #54681](https://github.com/qgis/QGIS/pull/54681) | N/D |
| Los archivos de ejemplo son instalados por la compilación del servidor, y además están en un lugar incorrecto | [#54423](https://github.com/qgis/QGIS/issues/54423) | [PR #54708](https://github.com/qgis/QGIS/pull/54708) | N/D |
| La herramienta Puntos a ruta provoca el fallo de QGIS | [#54686](https://github.com/qgis/QGIS/issues/54686) | [PR #54710](https://github.com/qgis/QGIS/pull/54710) | [PR #54784](https://github.com/qgis/QGIS/pull/54784) |
| el proyecto qgs/qgz no guarda correctamente la simbología de la malla | [#54384](https://github.com/qgis/QGIS/issues/54384) | [PR #54711](https://github.com/qgis/QGIS/pull/54711) | N/D |
| Bucle sin fin si el perfil se dibuja fuera de la extensión de la capa | [#54349](https://github.com/qgis/QGIS/issues/54349) | [PR #54745](https://github.com/qgis/QGIS/pull/54745) | N/D |
| Server: Can\'t enable WFS3 API update endpoint (PUT/PATCH) on layers without geometry | [#46119](https://github.com/qgis/QGIS/issues/46119) | [PR #54789](https://github.com/qgis/QGIS/pull/54789) | N/D |
| Añadir protección segura en torno a -of en el comando gdal para el procesamiento por lotes | [#54122](https://github.com/qgis/QGIS/issues/54122) | [PR #54800](https://github.com/qgis/QGIS/pull/54800) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Paul Blottiere (Hytech-imaging)](https://hytech-imaging.fr/)
### Prestación: Corrección de errores por Sandro Santilli (strk)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Tener QgsRectangle null rectángulo impreso como EMPTY en wkt | no reportado | [PR #54831](https://github.com/qgis/QGIS/pull/54831) | N/D |
| Corregir la relación de aspecto de cálculo en QgsLayoutItemMap::zoomToExtent | no reportado | [PR #54827](https://github.com/qgis/QGIS/pull/54827) | N/D |
| No incluir una etiqueta BoundingBox en las respuestas GetFeatureInfo, cuando es nula. | no reportado | [PR #54858](https://github.com/qgis/QGIS/pull/54858) | N/D |
| Ejecute siempre los correctores ortográficos y de shell si es posible, imprima una advertencia cuando no sea posible | no reportado | [PR #54847](https://github.com/qgis/QGIS/pull/54847) | N/D |
| Modificar el manejo del rectángulo nulo | no reportado | [PR #54872](https://github.com/qgis/QGIS/pull/54872) | N/D |
| Run spellcheck only on changed files in prepare_commit.sh | no reportado | [PR #54893](https://github.com/qgis/QGIS/pull/54893) | N/D |
| Fix prepare_commit.sh | no reportado | [PR #54918](https://github.com/qgis/QGIS/pull/54918) | N/D |
| Corregir el cálculo de la extensión en QgsSpatiaLiteProvider | no reportado | [PR #54917](https://github.com/qgis/QGIS/pull/54917) | N/D |
| No forzar verbose build en mingw build | [#54932](https://github.com/qgis/QGIS/issues/54932) | [PR #54924](https://github.com/qgis/QGIS/pull/54924) | N/D |
| Hacer QgsBookmark cadena de salida más explícita acerca de que es VACÍO | no reportado | [PR #54923](https://github.com/qgis/QGIS/pull/54923) | N/D |
| Corregir el cálculo de la extensión en QgsAFSProvider | no reportado | [PR #54944](https://github.com/qgis/QGIS/pull/54944) | N/D |
| Add `tags` make target | no reportado | [PR #54948](https://github.com/qgis/QGIS/pull/54948) | N/D |
| Manejar rectángulos nulos en QgsExtentWidget::outputExtent | no reportado | [PR #54953](https://github.com/qgis/QGIS/pull/54953) | N/D |
| Manejo de nulo en los métodos QgsRectangle grow() e include() | no reportado | [PR #54955](https://github.com/qgis/QGIS/pull/54955) | N/D |
| Añadir QgsRectangle::setNull(), obsoleto setMinimal() | no reportado | [PR #54934](https://github.com/qgis/QGIS/pull/54934) | N/D |
| Manejar rectángulo nulo en QgsRectangle::buffered | no reportado | [PR #54967](https://github.com/qgis/QGIS/pull/54967) | N/D |
| Corregir el cálculo de extensión en QgsVirtualLayerProvider | no reportado | [PR #54976](https://github.com/qgis/QGIS/pull/54976) | N/D |
| Añadir un método estático temporal QgsRectangle::createNull() | no reportado | [PR #55008](https://github.com/qgis/QGIS/pull/55008) | N/D |
| Corregir testRegisterFeatureUnprojectible - Utilizar extensión válida en testRegisterFeatureUnprojectible | no reportado | [PR #55011](https://github.com/qgis/QGIS/pull/55011) | N/D |
| Haz que QgsGeometry::boundingBox devuelva un rect nulo para una geom nula | no reportado | [PR #55012](https://github.com/qgis/QGIS/pull/55012) | N/D |
| Haz que QgsGeometry::fromRect(NULL RECT) devuelva geometría nula | no reportado | [PR #54954](https://github.com/qgis/QGIS/pull/54954) | N/D |
| Dejar de considerar Rectangle(0,0,0,0) null - while Rectangle(1,1,1,1) is not null | [#45563](https://github.com/qgis/QGIS/issues/45563) | [PR #54646](https://github.com/qgis/QGIS/pull/54646) | N/D |
| Ejecutar el verificador de diseño doxygen en el script prepare-commit, cuando sea posible. | no reportado | [PR #54936](https://github.com/qgis/QGIS/pull/54936) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](http://strk.kbt.io/)
### Prestación: Corrección de errores por Jean Felder (Oslandia)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| qgs3daxissettings: Correctamente leer relación de vista en un proyecto guardado | no reportado | [PR #54870](https://github.com/qgis/QGIS/pull/54870) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder (Oslandia)](https://oslandia.com/)
### Prestación: Corrección de errores por Nyall Dawson (North Road)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Don\'t show help for algorithms which can\'t be run in qgis_process | [#54914](https://github.com/qgis/QGIS/issues/54914) | [PR #54920](https://github.com/qgis/QGIS/pull/54920) | pendiente |
| Corrige fallos en el compositor de impresión | [#52079](https://github.com/qgis/QGIS/issues/52079) | [PR #54907](https://github.com/qgis/QGIS/pull/54907) | Demasiado intrusivo |
| Corregir etiqueta de diseño ajustar el tamaño a la lógica de texto | no reportado | [PR #54896](https://github.com/qgis/QGIS/pull/54896) | pendiente |
| Corregir la conmutación de la visibilidad de las capas de grupo restablece los modos de fusión de las máscaras de las capas hijas. | [#53088](https://github.com/qgis/QGIS/issues/53088) | [PR #54897](https://github.com/qgis/QGIS/pull/54897) | N/D |
| Garantizar que el resalte de identificación funcione con símbolos muy transparentes | [#54830](https://github.com/qgis/QGIS/issues/54830) | [PR #54864](https://github.com/qgis/QGIS/pull/54864) | [PR #54883](https://github.com/qgis/QGIS/pull/54883) |
| Arreglar mapas de diseño de rasterización de fuerza de todo el diseño cuando el elemento de mapa ha establecido la transparencia | no reportado | [PR #54882](https://github.com/qgis/QGIS/pull/54882) | Demasiado intrusivo |
| Corrección del fallo en el cuadro de diálogo de fusión de objetos espaciales cuando un campo tiene una restricción única. | [#54856](https://github.com/qgis/QGIS/issues/54856) | [PR #54862](https://github.com/qgis/QGIS/pull/54862) | [PR #54878](https://github.com/qgis/QGIS/pull/54878) |
| Corrección del nivel inicial de zoom al abrir las ventanas de diseño | [#44421](https://github.com/qgis/QGIS/issues/44421) | [PR #54849](https://github.com/qgis/QGIS/pull/54849) | [PR #54880](https://github.com/qgis/QGIS/pull/54880) |
| Corrección de un fallo al exportar mapas 3D | [#50067](https://github.com/qgis/QGIS/issues/50067) | [PR #54845](https://github.com/qgis/QGIS/pull/54845) | Demasiado arriesgado |
| Fix layout labels don\'t immediately react to changes when semi-transparent | no reportado | [PR #54839](https://github.com/qgis/QGIS/pull/54839) | [PR #54863](https://github.com/qgis/QGIS/pull/54863) |
| Corrección del fallo al abrir las propiedades de capa de una capa ráster con un origen de datos roto. | [#49176](https://github.com/qgis/QGIS/issues/49176) | [PR #54812](https://github.com/qgis/QGIS/pull/54812) | [PR #54838](https://github.com/qgis/QGIS/pull/54838) |
| Corregir el error de ejecución SQL | [#54833](https://github.com/qgis/QGIS/issues/54833) | [PR #54837](https://github.com/qgis/QGIS/pull/54837) | [PR #54842](https://github.com/qgis/QGIS/pull/54842) |
| Limpiar todo el diálogo de propiedades de capa del navegador antes de salir | [#39094](https://github.com/qgis/QGIS/issues/39094) | [PR #54808](https://github.com/qgis/QGIS/pull/54808) | [PR #54822](https://github.com/qgis/QGIS/pull/54822) |
| Evitar la pérdida de atributos al calcular los campos | [#47385](https://github.com/qgis/QGIS/issues/47385) | [PR #54815](https://github.com/qgis/QGIS/pull/54815) | [PR #54879](https://github.com/qgis/QGIS/pull/54879) |
| Arreglar fallo al cambiar capas entre editables/no editables | [#54802](https://github.com/qgis/QGIS/issues/54802) | [PR #54813](https://github.com/qgis/QGIS/pull/54813) | N/D |
| Corrección de QgsField::ConfigurationFlag::None provoca un error de sintaxis al iniciar PyQGIS | no reportado | [PR #54809](https://github.com/qgis/QGIS/pull/54809) | N/D |
| Handle sql=\'\' or sql=\"\" as empty sql strings instead of \'\' / \"\" literals | [#53736](https://github.com/qgis/QGIS/issues/53736) | [PR #54806](https://github.com/qgis/QGIS/pull/54806) | [PR #54826](https://github.com/qgis/QGIS/pull/54826) |
| Corrección de un fallo cuando determinadas páginas de símbolos están abiertas en el panel de estilos y QGIS se cierra o se abre un nuevo proyecto. | no reportado | [PR #54749](https://github.com/qgis/QGIS/pull/54749) | Demasiado intrusivo |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Prestación: Corrección de errores por Julien Cabieces (Oslandia)
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Masking with SVG symbol doesn\'t work | [#54926](https://github.com/qgis/QGIS/issues/54926) | [PR #54927](https://github.com/qgis/QGIS/pull/54927) |  |
| Error en la simbología graduada en el QGIS francés 3.28.10 | [#54549](https://github.com/qgis/QGIS/issues/54549) | [PR #54943](https://github.com/qgis/QGIS/pull/54943) | [PR #54963](https://github.com/qgis/QGIS/pull/54963) |
| QGIS se cae al deshacer el movimiento de elementos en el diseño del mapa | [#52740](https://github.com/qgis/QGIS/issues/52740) | [PR #54959](https://github.com/qgis/QGIS/pull/54959) | [PR #54969](https://github.com/qgis/QGIS/pull/54969) |
| QGIS se cae al exportar el diseño a PDF cuando se utiliza la simbología de relleno de puntos aleatorios. | [#54065](https://github.com/qgis/QGIS/issues/54065) | poly2tri issue <https://github.com/jhasse/poly2tri/issues/55> |  |
| La expresión de etiqueta con más de 32767 caracteres deja de ser válida al volver del diálogo de expresión a las propiedades de capa. | [#54141](https://github.com/qgis/QGIS/issues/54141) | [PR #55051](https://github.com/qgis/QGIS/pull/55051) | [PR #55052](https://github.com/qgis/QGIS/pull/55052) |
| La activación de la prestación notificar/escuchar hace que QGIS falle | [#54260](https://github.com/qgis/QGIS/issues/54260) | [PR #55062](https://github.com/qgis/QGIS/pull/55062) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/)

{{<content-end >}}
