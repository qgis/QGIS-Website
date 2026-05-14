---
HasBanner: false
draft: false
releaseDate: '2022-10-21'
section: proyecto
sidebar: true
title: Registro de cambios de QGIS 3.28
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios de QGIS 3.28{#changelog328 }
![image1](images/projects/19a3cf4af4fcad7ecec62560b72067b903097054.png)

Fecha de lanzamiento: 2022-10-21

QGIS 3.28 Firenze introduces various feature updates, UX modifications, usability enhancements, and improved integration with various proprietary services and data backends. It is also set to introduce the long-awaited features provided by previous releases into the long-term support release, as outlined in the [QGIS Roadmap](https://www.qgis.org/en/site/getinvolved/development/roadmap.html).

La pantalla de inicio muestra un raro y extraordinario mapa de Florencia de 1847, obra de Giuseppe Molini. Este mapa, magníficamente grabado, fue dibujado originalmente en 1731 por el arquitecto florentino Ferdinando Ruggieri. Orientado hacia el sur, el mapa abarca el antiguo centro amurallado de Florencia, que se extiende a ambos lados del río Arno. En el cuadrante superior derecho aparece el símbolo del lirio de Florencia. Aunque se imprimió en 1847, este mapa se ha elaborado al estilo del siglo XVII mediante grabado en cobre sobre papel grueso. En 1847, Florencia estaba en plena transformación política. Un año después de la producción de este raro mapa, el Gran Duque de Toscana, en respuesta a las manifestaciones políticas en toda Florencia, concedió a Toscana su primera constitución.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://youtu.be/IEkOhQezQMk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/IEkOhQezQMk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es software libre y no hay obligación de pagar nada por utilizarlo; de hecho, queremos animar a todo el mundo a que lo use, independientemente de su situación económica o social. Creemos que dotar a las personas de herramientas para la toma de decisiones espaciales redundará en una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Cambios que eliminan funcionalidades
### Novedad: Baja de retrocompatibilidad para simbología con QGIS 3.16 y anteriores.
Previos lanzamientos de QGIS tenían escrito una cantidad significativa de objetos de compatibilidad en la estructura XML de los archivos de proyecto para mantener la retrocompatibilidad para que los archivos de projecto pudieran ser abiertos con QGIS 3.16 o anteriores. Esta compatibilidad fue eliminada para lanzamientos futuros, proviendo significativas optimizaciones para la estructura de archivos de proyectos.
## Temporal
### Prestación: Añadir soporte de gestor temporal para capas WMTS con dimensión TIME
This enhancement exposes any WMTS \"time\" dimensions for use in the temporal framework, including allowing these layers to be animated and controlled via the temporal controller.

When we do detect a time dimension on a WMTS layer, we no longer expose this in the same way as other non-time dimensions. The browser panel does not show the dimension values, and adding the layer via Data Source Manager no longer prompts the user to pick from the available time values. Instead, these layers are indicated with a new \"time capable raster layer\" icon, and are added to a project without the user specifying a time value.

Just like a WMS(T) layer, when a time-dimension enabled WMTS layer is added to the project, it will default to the \"automatic\" temporal mode, meaning that the layer will follow the temporal controller\'s current time range by default. A user can then opt to show a specific static time value for the layer through the layer\'s Temporal properties page, by unchecking \"Dynamic Temporal Control\" and picking a specific available time range from the \"Predefined date\" option.

Esto debería unificar la experiencia del usuario, de modo que el uso de las capas habilitadas para tiempo WMTS sea esencialmente idéntico al uso de las capas WMS(T).

![image3](images/entries/8f0a6c8e4850886732633ab76d5873dffd7746c4.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Herramientas de mapa
### Prestación: Permitir la selección de objetos espaciales en capas de teselas vectoriales
Se ha añadido soporte para seleccionar objetos espaciales de capas de mosaico vectorial, lo que permite a los usuarios utilizar las herramientas de selección estándar basadas en mapas para seleccionar interactivamente características de estas fuentes.

Cuando una capa de mosaico vectorial tiene una selección, un usuario puede:
- Copie los objetos espaciales y péguelos en otras capas, o péguelos en una capa cero
- Use other (non-editing) tools which operate on selections, such as \"zoom to selected features\"/\"pan to selected features\"

Las selecciones pueden realizarse utilizando cualquiera de las herramientas de selección basadas en mapas interactivos, por ejemplo, selección por rectángulo, a mano alzada, polígono o radio. También se aplican todos los métodos abreviados que se aplican a las selecciones vectoriales para añadir/restar/interseccionar selecciones.

La selección de elementos se realiza utilizando el nivel de zoom del lienzo, y los elementos seleccionados en este nivel de zoom persisten, aunque el usuario cambie la escala del mapa a otro nivel de zoom vectorial. Esto significa que un usuario puede acercarse y seleccionar una característica pequeña o detallada, y luego alejarse y seguir viendo la característica seleccionada en el mapa.

Esta prestación ha sido financiada por Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Interfaz de usuario
### Prestación: UX exclusiva basada en ventanas para el gestor de fuentes de datos
The data source manager dialog is now ALWAYS non modal, and options to set it as such have been removed. The dialog now functions just like other \"manager\" type windows in QGIS, such as the style manager or layout manager.

En su lugar, el gestor de fuentes de datos se tratará como una ventana propia, que pasa a primer plano cada vez que se pulsa el botón Gestor de fuentes de datos.

![image4](images/entries/9bbc312e9b1362ae660a9719c910ab209d3e8a55.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir una acción Mostrar en tabla de atributos al menú del botón derecho del ratón de los símbolos de clase de leyenda.
A new \"Show in Attribute Table\" action has been added to the right-click context menu of legend class symbols in the table of contents. This allows users to open the attribute table with a filter applied to match only the features relevant to a particular symbol group. This provides a significant performance improvement for certain datasets, such as large vector layers loaded from a remote source.

![image5](images/entries/8b43481bcab479b040b0a5ac5400ddc89c77dd0a.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Añadir la opción de ocultar los valores NULL en los resultados de identificación
The \"Identify Features\" utility now provides the capability to hide NULL values from the returned results

![image6](images/entries/f0c7217db5f0104999a3d87c2229010dcc62cb50.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Simbología
### Prestación: Permite controlar el marcador de localización GPS
Se ha introducido una nueva página de opciones generales de GPS que incluye nuevos ajustes para controlar el símbolo del marcador utilizado para la ubicación GPS actual, y si este símbolo debe girar para coincidir con la dirección GPS.

![image7](images/entries/411b2d3b0f1b180857eda6d4e0c73144f1aeee57.gif)

Esta prestación ha sido financiada por Tiwi Resources, Bush Heritage, Australian Wildlife Conservancy

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadidas nuevas formas de marcador de elipse
Los estilos de símbolo para el tipo de marcador elipse incluyen ahora tipos de forma adicionales para:
- Pentágono
- Hexágono
- Octágono
- Tercer Círculo
- Cuarto de Círculo
- Estrella

![image8](images/entries/3e749b405f10a24f95665cd0ad3e1ea0f199811b.webp)

Esta prestación ha sido financiada por North Road

This feature was developed by [ZayneTomlins](https://github.com/ZayneTomlins)
## Etiquetando
### Prestación: Añade soporte para negrita/cursiva/tamaño de fuente y familia de fuente HTML al etiquetado.
Se ha añadido soporte para etiquetas de formato HTML adicionales para su uso dentro del etiquetado (y en cualquier otro lugar donde se utilice el renderizador de texto).

Entre las etiquetas compatibles se incluyen:
- familia tipográfica
- tamaño de la letra
- negrita
- cursiva

![image9](images/entries/b49f780e98b4276b76cf3022b34da26dd4ed9d1f.webp)

Esta prestación fue financiada por el grupo de usuarios suizo de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir la opción de utilizar unidades absolutas para la altura de línea
Anteriormente, la altura de línea siempre se establecía en múltiplos del interlineado del texto; sin embargo, ahora es posible utilizar unidades absolutas para la altura de línea (útil en contextos en los que se utilizan tamaños de texto mixtos dentro de un mismo documento).

![image10](images/entries/b413c593933bc197886a97919ae015880e119aa7.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Malla
### Prestación: Añadir la opción de recargar las propiedades temporales de la capa de malla
An \"Always take reference time from data source\" option has been added for mesh layers that when checked, will ensure that the reference time is reloaded from the data source, and each time the layer is reloaded or the project reopened the time properties will be updated from the file automatically.

In previous releases, when a mesh layer file had a reference time and time extent that changed, the time layer properties would not be updated when the projector layer are reloaded, and the user would be required to manually navigate to the \"Reload from provider\" feature in the temporal tab of the layer properties.

![image11](images/entries/8bf480abed6701e5535110f8069ba1f63ecf2de4.gif)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
## Objetos 3D
### Prestación: Efecto 3D de oclusión ambiental
Existe un nuevo efecto de oclusión ambiental para la representación de datos en vistas 3D que resulta útil para mejorar la percepción de profundidad de los datos en 3D. Se trata de un efecto de posprocesamiento que puede combinarse incluso con la iluminación de cúpula ocular (EDL) para obtener resultados bastante interesantes. Una simplificación excesiva del efecto es que las características que no son visibles para la cámara se utilizan para texturizar y oscurecer los elementos vecinos, con la ventaja de mejorar el contraste, la definición de las características y la diferenciación.

Hay un nuevo elemento para controlar el estado de la oclusión ambiental en el menú de configuración de las vistas 3D, así como parámetros adicionales en la sección avanzada del cuadro de diálogo de configuración para un control más preciso:
- Radio: El umbral de distancia para calcular la oclusión ambiental.
- Intensidad: La fuerza del efecto debe ser (valores más altos hacen las cosas más oscuras)
- Umbral de oclusión: Número de puntos vecinos que deben estar ocluidos para que aparezca el efecto (valores inferiores al 50% harán que la salida sea más oscura, pero posiblemente proporcionen un mayor rango de oclusión).

![image12](images/entries/996b020346252bc10d87279d9e0cac766802c1d4.webp)

This feature was developed by [Martin Dobias & Belgacem Nedjima](https://github.com/wonder-sk)
## Nubes de Puntos
### Prestación: Exportación de capas de nubes de puntos
Las capas de nubes de puntos ahora se pueden exportar a formatos de datos vectoriales o de nubes de puntos, con filtrado opcional.

Los formatos compatibles son:
- Capa scratch temporal (capa de memoria)
- GeoPackage
- Archivos shape
- DXF
- LAZ (requires build WITH_PDAL)
- Archivos LAS sin comprimir

Las operaciones de exportación admiten el filtrado por:
- Extensión
- Filtrado por rango Z
- Limitar el número de puntos exportados
- Filtrado espacial por capa de polígonos

Además, también admite la definición y reproyección de SRC de salida.

![image13](images/entries/9b7102f1bbd9286c16285a43158904395e56c4bc.webp)

Esta prestación ha sido financiada por el Estado de Vorarlberg y el grupo suizo de usuarios de QGIS.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Prestación: Iluminación Eye Dome para nubes de puntos en lienzos de mapas 2D
El efecto de iluminación de cúpula ocular ya está disponible para nubes de puntos en renderizadores 2D

![image14](images/entries/99c16bf2efe3bdcf020a41ad088e29ec7437573e.webp)

This feature was developed by [Nedjima Belgacem](https://github.com/NEDJIMAbelgacem)
## Diseño de impresión
### Feature: Add FORCE_RASTER and IMAGE_COMPRESSION parameters to PDF algorithms
The `FORCE_RASTER` and `IMAGE_COMPRESSION` parameters have been added to the various \"Export print layout as PDF\" algorithms, including support for Atlas and multifile exports.

`FORCE_RASTER` is mutually exclusive with and takes precedence over the `FORCE_VECTOR` parameter.

![image15](images/entries/06cc045f6a69f9caaacde8f8b3ead9e89f02af22.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Expresiones
### Prestación: Añadir una nueva forma variable de las funciones actuales de expresión de objetos espaciales
Se ha añadido la nueva forma de variable de estilo para hacer referencia a la característica actual y sus atributos en las expresiones.

Las nuevas variables introducidas son:
- `@feature`: a replacement for \$currentfeature, contains the current feature
- `@id`: a replacement for \$id, contains the current feature id
- `@geometry`: a replacement for \$geometry, contains the current feature geometry

This is a step towards eventually deprecating the older `$` style functions, and providing a more consistent approach to expressions instead of an unpredictable mix of `@`/`$`.

Las funciones antiguas y las referencias a variables seguirán funcionando (y probablemente seguirán funcionando indefinidamente en aras de la compatibilidad con proyectos antiguos). También seguirán (de momento) expuestas en la interfaz de usuario para evitar confusiones al usuario.

![image16](images/entries/b9666dee9322ba767162310e6958503e639d1148.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add new shared_paths function
A new `shared_paths` function has been added which returns a collection containing paths shared by the two input geometries. Those going in the same direction are in the first element of the collection, and those going in the opposite direction are in the second element. The paths themselves are given in the direction of the first geometry.

![image17](images/entries/f02946a8f1e45527366c30e6d0ea5a4947c7f86a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Make_valid and geom_to_array functions
Se han añadido funciones adicionales para:
- `make_valid`: Repair broken input geometries and returns the corrected geometries
- `geometries_to_array`: This converts a geometry collection into an array for easier handling and iteration

![image18](images/entries/bc2bbd8d26e2ebb4fd7dc02f0ce7ec6460f3a3bc.webp)

This feature was developed by [Alex](https://github.com/roya0045)
### Prestación: Función de casco cóncavo
A new `concave_hull` function is now available in QGIS expressions (GEOS 3.11+)

![image19](images/entries/e434b7356dc93f9c43fa3142c7f8f914a4aa5615.webp)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Prestación: Pedir confirmación al descartar cambios de expresión
A new confirmation dialog is now safeguarding users against accidentally discarding their unapplied changes in expression editor dialogs. This safeguard is used in the Expression String Builder, the Expression Dialog (Epsilon icon, e. g. for Geometry Generators or for Pre-calculated Values in the model builder) and the Expression Based Filter (Attribute Table -\> Advanced filter expression).

![image36](images/entries/cebe844ae2c28045a8b6e2e89cb2b40cdbbd38c6.webp)

This feature was funded by [WhereGroup GmbH](https://wheregroup.com/)

This feature was developed by [Johannes Kröger](https://github.com/kannes)
## Administración de datos
### Prestación: Pedir confirmación al eliminar funciones
Aparece por defecto un nuevo diálogo de confirmación cuando los usuarios realizan una acción que borraría registros, como utilizar la tecla DEL o acciones de la barra de herramientas, para reducir aún más los riesgos de borrado accidental de características. Además, el recuento de objetos espaciales se incluye ahora en el propio mensaje del cuadro de diálogo (y también se sigue mostrando en la barra de título), con lo que el número total de objetos espaciales eliminados queda más claro para los usuarios.

In previous releases, similar confirmation prompts would only be displayed when some features fell out of the extent of the map canvas, or the deletion triggered the removal of child relation features. The new behavior is for the prompt to be enabled by default and disabled by using the \"Don\'t show this message again\" checkbox.

![image20](images/entries/677952561ec24d417a74cf46842a6c52aec49587.webp)

This feature was funded by [QGIS user group Switzerland](https://www.qgis.ch/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Metadatos y Metabúsqueda
### Prestación: Búsqueda y almacenamiento de proveedores de datos de metadatos por capas
Implementation of elements from the [QEP #250 \"Database metadata storage\"](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/250) initiative have been completed and this functionality includes the creation of a new layer metadata API and GUI components.

Los siguientes proveedores de datos/formatos son compatibles para almacenar y gestionar metadatos de capas en QGIS:
- GPKG (ya estaba implementado, sólo lo incluí en la nueva API)
- Postgres
- Postgres Ráster

Además, hay disponible una nueva pestaña de búsqueda de metadatos de capas en el gestor de fuentes de datos, y una búsqueda interactiva de metadatos de capas mediante el localizador de QGIS.

![image21](images/entries/17fc26636b3c1fe423ec8f715e69365495519add.webp)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Procesado
### Prestación: Soporte de precisión fija para determinadas herramientas de procesamiento
A new advanced parameter is available for some processing tools which allows the use of the [fixed precision](https://blog.cleverelephant.ca/2020/12/waiting-postgis-31-3.html#fixed-precision-overlay) parameter provided by GEOS \>= 3.9.0. This parameter is listed under advanced parameters as \"Grid Size\" and is currently supported in the following tools:
- Solapa
- Intersección
- Diferencia
- Diferencia Simétrica
- Unión

![image22](images/entries/b2ef315dc1013852d3316023c62af5ff06626e93.webp)

Esta prestación ha sido financiada por Orange Telecom FR

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: Improved \"Make Valid\" Algorithms
QGIS puede utilizar ahora los nuevos métodos refinados de GEOS 3.10+ para validar y reparar características geométricas.

![image23](images/entries/4b320e5bad078f1a0eb23fe958d86e330b08c10e.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Opción predeterminada para mostrar el recuento de objetos espaciales para las salidas vectoriales del procesamiento.
A new `Show feature count for output vector layers` setting is available (but disabled by default for performance reasons), which will automatically enable the \"show feature count\" option on output layers loaded from QGIS processing. This is able to give users a first glimpse of what to expect as an output from a Processing algorithm.

![image24](images/entries/e804b2accbcf155f4db2ea4024bd89ed5883097f.webp)

This feature was developed by [Germap](https://github.com/gacarrillor)
### Prestación: Añadir la opción de exportación de relaciones al algoritmo de capas de paquetes
The \"Package Layers\" processing tool now supports optionally following project relations and exporting related tables following the hierarchy both upstream and downstream, whilst also taking selected features into account.

![image25](images/entries/26076b13de92a8ac2a1fea1511e03776c1aeae13.webp)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Add \"Offset\" parameter to \"Drape\" algorithms
Adds the \"Offset\" parameter to the \"Drape (set Z value from raster)\" and \"Set M value from raster\" algorithms. The \"Offset\" value is algebraically added to the band values after applying the \"Scale factor\".

![image26](images/entries/78e9cb5b82c872604fc3616c2c7b3772e7d26bef.webp)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
## Opciones de Aplicación y Proyecto
### Prestación: Modificados los ajustes de visualización de coordenadas y marcación del proyecto
Las opciones de visualización de coordenadas y rumbos en los ajustes del proyecto se han actualizado de acuerdo con lo siguiente:
- Unidades de mapa (el comportamiento es el mismo que en versiones anteriores)
- Mapa Geográfico (comportamiento modificado)
- Unidades de proyección personalizadas (nuevo tipo)

La antigua opción Geográfica (Latitud/Longitud) mostraba los valores en las coordenadas CRS del mapa *si* el SRC era geográfico; de lo contrario, transformaba las coordenadas a un valor SRC WGS84 codificado.

The updated Map Geographic (degrees) option, which supersedes the legacy approach, will display values in the map CRS coordinates *if* the CRS is geographic, however in instances where it is not, the internal `QgsCoordinateReferenceSystem::toGeographicCrs()` API will be used to transform the coordinates into the map CRS\' associated geographic CRS. This is helpful in various contexts, such as when analyzing non-earth celestial bodies.

El tipo de Unidades de Proyección Personalizadas es una nueva adición que por defecto es WGS84 y permite a los usuarios establecer cualquier SRC que deseen como coordenadas de visualización.

![image27](images/entries/7af6704f72373fec3c1e9c212366fd3d8cfa0218.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add support for \"user\" fonts, and automatic downloading of freely licensed fonts
A new \"Fonts\" panel has been added to the settings dialog, which provides support for the following functionalities:
- The ability for users to populate a list of automatic font replacements to apply when loading projects or styles, allowing better support for projects and styles to be used across different operating systems (e.g. replace \"Arial\" with \"Helvetica\").
- Users can now place TTF or OTF fonts in the \"fonts\" subfolder of their user profile. These fonts will automatically be loaded at QGIS startup time. This provides a way for users to use fonts without requiring them to be installed on an operating system level, which is often blocked in enterprise environments. The Fonts setting panel lists all installed user fonts and allows users to manage (i.e. remove) previously installed user fonts
- Se proporciona una API para que otras herramientas, como complementos y otros clientes, especifiquen carpetas de fuentes de usuario adicionales que deben analizarse durante el inicio de QGIS.
- Automatic downloading of missing fonts is now supported in certain circumstances. If a user opens a project or style, or they try to load a vector tile layer that references fonts that aren\'t currently available, then a hard-coded list of freely licensed fonts to download via URL is consulted to determine whether it\'s possible to automatically download the font to the user font directory (and notify the user of the font license). A setting to opt out of this behavior is provided in the Fonts panel if so desired.

![image28](images/entries/77e17395ccb70e466ad4c5a80675ad0ff8ec070e.gif)

Esta prestación ha sido financiada por Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Navegador
### Prestación: Implementación del descubrimiento de relaciones para capas OGR, y mostrar las relaciones en el navegador.
La función Propiedades del proyecto → Relaciones → Descubrir relaciones ahora es capaz de admitir capas OGR que admiten relaciones, como GeoPackage (a través de la extensión de tablas relacionadas) y ESRI FileGeodatabases.

El panel de navegación de QGIS incluye ahora la posibilidad de mostrar información detallada sobre las relaciones entre estas fuentes de datos.

![image29](images/entries/11c3f493eff806b4eccbf9af27c96894ea3223a3.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Modificación de la interfaz de usuario para la creación de geopackage y ESRI File Geodatabase
A \"New ESRI File Geodatabase\" action has been added to the QGIS Browser right-click context menu on directories, and a new \"vacuum\" action is available for GDB files. (requires GDAL 3.6+)

Además, al crear un nuevo Geopackage desde el mismo menú, ahora se creará inmediatamente un GPKG vacío, en lugar del comportamiento heredado de abrir un cuadro de diálogo de creación de tablas por defecto (y requerir la creación de tablas o que los usuarios introduzcan datos ficticios).

<https://user-images.githubusercontent.com/1829991/178902332-0e112e73-0140-45b9-84bf-fc7875cb7b98.gif>

![image30](images/entries/7a0e8f73e24aa061244e30d6bf1b8154e5eebce4.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Permitir arrastrar y soltar capas vectoriales en conjuntos de datos de la base de datos OGR que no sean GPKG.
QGIS permite ahora arrastrar y soltar capas vectoriales entre conjuntos de datos de bases de datos OGR que no estén almacenados en formato GPKG, por ejemplo, el arrastre de una capa a una GDB para importar ese conjunto de datos a la geodatabase.

![image31](images/entries/c1c17d31db79a4beaab864daf13257e6e7ed0ba0.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Exponer la gestión de dominios de campo para fuentes OGR no gpkg
El navegador QGIS soporta ahora funcionalidades más avanzadas para bases de datos OGR que no están en formato GPKG, incluyendo capacidades de gestión de dominios de campo (creación y listado de dominios) y creación de tablas. Esto significa que los usuarios pueden gestionar dominios de campo y crear nuevas tablas en una base de datos ESRI FileGeodatabase existente desde la interfaz del navegador QGIS.

![image32](images/entries/cc1f815593c28352dffaad020061004db91f8ded.webp)

Esta prestación ha sido financiada por Provincie Gelderland

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Proveedores de datos
### Prestación: Definir rol de sesión para conexiones PostgreSQL
A `session_role` setting can now be specified for PostgreSQL connections to set the user identifier of the active SQL session. Permissions checking for SQL commands are then carried out with the associated named role.

This is highly useful in instances where it is desirable to automatically give ownership of new objects (Tables/ Views/ Functions etc.) to the `session_role` group, and share ownership and the associated rights with all members of the `session_role` group.

The specified `session_role` must be a role that the current session user is a member of, or if the session user is a superuser, any role can be selected.

This feature was funded by [3liz](https://3liz.com/)

This feature was developed by [rldhont](https://github.com/rldhont)
### Prestación: Añadir automáticamente tablas relacionadas al añadir capas desde conjuntos de datos GDAL con información de relación incrustada.
For GDAL data formats with embedded relationship information, whenever a table is added QGIS is now able to discover relationships and immediately add all the related tables to the current project (if they don\'t already exist). Additionally, when adding these related layers QGIS will automatically configure the corresponding QGIS relationships.

Esto funciona para todos los formatos que admiten la API de relaciones GDAL, entre los que se incluyen:
- Geopackage (a través de la extensión de tablas relacionadas)
- ESRI FileGDB/ OpenFileGDB
- ESRI Personal Geodatabase
- Formatos SQLite/ Spatialite.

Esta prestación ha sido financiada por la Universidad de Uppsala.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añade compatibilidad con cadenas de subconjuntos (filtros) para las capas REST de arcgis
Esto puede **mejorar enormemente** el rendimiento en capas grandes.

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Proveedor abstracto de bases de datos para renombrar campos
A `QgsAbstractDatabaseProviderConnection` interface has been added for supporting renaming fields, and implemented for OGR connections along with the ability to rename existing fields for supported database connections via the QGIS Browser interface.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: WFS realiza operaciones espaciales binarias en expresiones en el servidor
QGIS solía ser capaz de realizar los filtros de expresión de operaciones espaciales binarias en el servidor cuando la geometría se proporcionaba como WKT o en el formato GML. Este cambio convierte la geometría de ser una variable estática en la expresión a un filtro OGC. La URL WFS se crea entonces combinando un rectángulo de cuadro delimitador, un filtro de capa y la expresión de filtrado.

A feature request computes the expression in advance to find out if it can be performed on the server, then it\'s stored in `QgsBackgroundCachedSharedData` where a new download is triggered.

Cuando una solicitud de filtro no es una operación espacial binaria pura, no se evaluará en el servidor.

Esta prestación ha sido financiado por el cantón de Schaffhausen.

This feature was developed by [signedav](https://github.com/signedav)
### Prestación: Edición de capas REST de ArcGIS
QGIS admite ahora la edición de capas del servidor de objetos espaciales de ArcGIS, como las alojadas en ArcGIS online. Suponiendo que el usuario tenga concedidos los permisos apropiados para editar una capa, desbloqueará la capacidad de utilizar las herramientas nativas de QGIS para editar esa capa. Estos cambios incluyen soporte para las siguientes operaciones:
- Borrar objetos espaciales
- Añadir nuevos objetos espaciales
- Curved geometries (only supported for enterprise ArcGIS server, as [ArcGIS online currently has no support for curves](https://support.esri.com/en/technical-article/000014684))
- Modificación de objetos espaciales existentes
- Modificación de atributos (creación de campos, supresión de campos, creación de índices de atributos)

This feature was funded by [Naturstyrelsen and Miljøstyrelsen, Danish Ministry of Environment](https://eng.naturstyrelsen.dk/)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Carga automática de subcapas de trama a partir de estilos de mosaico vectoriales
Al cargar un nuevo origen de mosaico vectorial en un proyecto, si el estilo MapBox GL asociado incluye alguna subcapa ráster, cárguela también en el proyecto con los estilos convertidos.

Fixes <https://github.com/qgis/QGIS/issues/46593>

![Peek 2022-06-20 12-31](https://user-images.githubusercontent.com/1829991/174514930-77887a1d-4679-49a2-9ff0-7c360bc0fc01.gif)

Esta prestación ha sido financiada por Toitū Te Whenua Land Information New Zealand

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir capas WMS individualmente
En versiones anteriores, la selección de capas de los servidores WMS se cargaba en QGIS como una única capa de proyecto. Esta nueva funcionalidad proporciona una casilla de verificación opcional para cargar cada una de las capas WMS seleccionadas en QGIS como capas de proyecto distintas.

![image34](images/entries/2685710315d58fc03e1557e3381a41fdd8eb5a02.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Prestación: Guardar proyectos en el proveedor de bases de datos Oracle
QGIS ahora permite guardar proyectos en bases de datos Oracle.

![image35](images/entries/6a575714dfc905211f3518a4f5f3803c32e8afa9.webp)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Servidor de QGIS
### Feature: QGIS_SERVER_ALLOWED_EXTRA_SQL_TOKENS settings variable
Esta nueva función permite especificar tokens adicionales que pueden utilizarse en la definición de un FILTRO WMS. La lista actual de tokens aceptados es bastante reducida y este ajuste permitirá a los administradores del sistema ampliar fácilmente la lista de tokens permitidos.

Esta prestación ha sido financiada por Zweckverband Grevesmühlen

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Abrir capas en modo de sólo lectura con QGIS Servidor
A new `QGIS_SERVER_FORCE_READONLY_LAYERS` environment variable to force QGIS Server to open layers in read-only mode.

Esto incluye varios cambios en la API subyacente para admitir la configuración de sólo lectura para la construcción del proveedor de datos, la estructura del proyecto y las propiedades de las capas.

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [rldhont](https://github.com/rldhont)
## Plugins
### Prestación: Cambios en el comportamiento de las actualizaciones automáticas de complementos
This change moves the old `app/plugin_installer/checkOnStart` setting key to a new `plugins/automatically-check-for-updates` key, and switches the default value to enable automatic checks.

Esto está diseñado para cambiar a todos los usuarios existentes de QGIS al nuevo comportamiento por defecto de buscar actualizaciones de plugins al inicio (a un máximo de una vez cada 3 días).

Su objetivo es ofrecer una mejor experiencia QGIS a nuestros usuarios, informando proactivamente a todos los usuarios cuando los plugins deben ser actualizados, asegurando que TODOS los usuarios son más propensos a actualizar los plugins y obtener las correcciones de errores para los plugins con prontitud.

**Los usuarios de Enterprise que hayan personalizado esta configuración en sus implantaciones tendrán que adaptar sus guiones a la nueva clave de configuración.

Además, se ha eliminado la opción de controlar el número de días entre las comprobaciones de inicio de los plugins, que ahora es de 3 días.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Programabilidad
### Prestación: Añadir tratamiento temporal a los mapas en QGIS Quick
A new implementation has been added to allow the Canvas and Map Settings in [QGIS Quick](https://api.qgis.org/api/qgsquick.html) to handle temporal functionality.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Adición del parámetro de línea de comandos py-args
When running QGIS from the command line with the `--code` parameter, a new `--py-args` utility allows the passing of arguments to the python interpreter.

Arguments between `--py-args` and `--` are passed to the python interpreter and ignored by QGIS, so for example, when using the following command:

    qgis --code /home/user/example.py --py-args --specialScriptArguments "arg1" 'arg2' -- layer1 layer2
    
The `example.py` script will have `--specialScriptArguments`, `arg1`, and `arg2` passed as system arguments to the python interpreter, whilst `layer1` and `layer2` will be handled by QGIS normally and loaded as map layers

Esta prestación ha sido financiada por el Landesamt für Vermessung und Geoinformation Vorarlberg.

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| GetPrint request of Atlas Template doesn\'t respect Project scales | [#49900](https://github.com/qgis/QGIS/issues/49900) | [PR #50199](https://github.com/qgis/QGIS/pull/50199) | [PR #50214](https://github.com/qgis/QGIS/pull/50214) |
| Las entradas enteras de la tabla de atributos no se muestran debido al tamaño de la ventana | [#50181](https://github.com/qgis/QGIS/issues/50181) | [PR #50201](https://github.com/qgis/QGIS/pull/50201) | No recomendado |
| Mezcla de nombre de campo/displayName de colecciones WFS3 en solicitud/respuesta | [#49399](https://github.com/qgis/QGIS/issues/49399) | [PR #50203](https://github.com/qgis/QGIS/pull/50203) | No recomendado |
| QGIS Server WMS GetFeatureInfo does not evaluate represent_value expression in maptip | [#30719](https://github.com/qgis/QGIS/issues/30719) | [PR #50216](https://github.com/qgis/QGIS/pull/50216) | [PR #50223](https://github.com/qgis/QGIS/pull/50223) |
| \"evaluate default value on providers side\" block insert on table in the schema with autoincrement | [#50168](https://github.com/qgis/QGIS/issues/50168) | [PR #50230](https://github.com/qgis/QGIS/pull/50230) | [PR #50333](https://github.com/qgis/QGIS/pull/50333) |
| QGIS no responde al introducir el tamaño de la página utilizando campos personalizados de anchura o altura | [#50104](https://github.com/qgis/QGIS/issues/50104) | No puede reproducir |  |
| \"Add Directory\...\" inputs files from previous selected directory at first instance, then the corret. | [#50055](https://github.com/qgis/QGIS/issues/50055) | [PR #50232](https://github.com/qgis/QGIS/pull/50232) | [PR #50241](https://github.com/qgis/QGIS/pull/50241) |
| El panel Estilo de capa y el panel Capa no muestran la misma configuración de visibilidad para el estilo de capa. | [#49998](https://github.com/qgis/QGIS/issues/49998) | No puede reproducir |  |
| Bloqueo al abrir el cuadro de diálogo Opciones después de cambiar la configuración regional | [#50239](https://github.com/qgis/QGIS/issues/50239)9 | [PR #50263](https://github.com/qgis/QGIS/pull/50263) | No necesitado |
| error de API de conexiones MSSQL no notificado | No reportado | [PR #50194](https://github.com/qgis/QGIS/pull/50194) | [PR #50454](https://github.com/qgis/QGIS/pull/50454) |
| Identify and select tools don\'t work with geometry-based query layers | [#50242](https://github.com/qgis/QGIS/issues/50242) | No puede reproducir |  |
| Problema con la recarga de archivos SLD en QGIS | [#50152](https://github.com/qgis/QGIS/issues/50152) | [PR #50266](https://github.com/qgis/QGIS/pull/50266) | en cola |
| Sin fin alg splitwithlines no comunicado | No reportado | [PR #50279](https://github.com/qgis/QGIS/pull/50279) | No recomendado |
| Processing algorithm \"Split with lines\" does not split polygon | [#50227](https://github.com/qgis/QGIS/issues/50227) | No es un error |  |
| La expresión no divide la cadena en varias líneas | [#49666](https://github.com/qgis/QGIS/issues/49666) | [PR #50295](https://github.com/qgis/QGIS/pull/50295) | [PR #50455](https://github.com/qgis/QGIS/pull/50455) |
| Problema con la exportación de SLD complejos | [#42348](https://github.com/qgis/QGIS/issues/42348) | [PR #50342](https://github.com/qgis/QGIS/pull/50342) | [PR #50354](https://github.com/qgis/QGIS/pull/50354) |
| Interpretación errónea de la opacidad del color SLD | [#44657](https://github.com/qgis/QGIS/issues/44657) | No es un error |  |
| Tamaño de etiqueta incorrecto para la exportación/importación de SLD | [#35561](https://github.com/qgis/QGIS/issues/35561) | [PR #50347](https://github.com/qgis/QGIS/pull/50347) | No necesitado |
| La exportación de SLD no incluye la opacidad de relleno | [#33376](https://github.com/qgis/QGIS/issues/33376) | [PR #50349](https://github.com/qgis/QGIS/pull/50349) | [PR #50436](https://github.com/qgis/QGIS/pull/50436) |
| SpatiaLite - La función añadida desaparece, el diálogo de atributos no muestra los campos obligatorios | [#50523](https://github.com/qgis/QGIS/issues/50523) | [PR #50573](https://github.com/qgis/QGIS/pull/50573) | en cola |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| En la importación GML falta un obejto espacial sin geometría | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | No apropiado |
| WFS/QgsOapifProvider no tiene en cuenta el pageSize del diálogo | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | No necesitado |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: falta el prefijo del espacio de nombres en los elementos de geometría y atributos en FILTER para las solicitudes WFS GetFeature | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | No reportado | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| El cliente WFS muestra un SRC erróneo | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignora el campo heredado del tipo de característica padre en los servicios WFS 2.0 | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | No apropiado |
| La carga y visualización de los datos CADRG/NITF es más lenta que antes. | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | No reportado | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | No necesitado |
| QGIS 3.24.1 (Windows) destruye mi mosaico ráster VRT | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328)Bug Title |
| \-- | \-- | \-- | \-- |
| En la importación GML falta un obejto espacial sin geometría | [#50215](https://github.com/qgis/QGIS/issues/50215) | [PR #50231](https://github.com/qgis/QGIS/pull/50231) | No apropiado |
| WFS/QgsOapifProvider no tiene en cuenta el pageSize del diálogo | [#49404](https://github.com/qgis/QGIS/issues/49404) | [PR #50236](https://github.com/qgis/QGIS/pull/50236) | No necesitado |
| \[WFS\] Layer is added incorrectly as mixed geometry collection | [#49335](https://github.com/qgis/QGIS/issues/49335) | [PR #50237](https://github.com/qgis/QGIS/pull/50237) | [PR #50353](https://github.com/qgis/QGIS/pull/50353) |
| WFS: falta el prefijo del espacio de nombres en los elementos de geometría y atributos en FILTER para las solicitudes WFS GetFeature | [#49121](https://github.com/qgis/QGIS/issues/49121) | [PR #50249](https://github.com/qgis/QGIS/pull/50249) | [PR #50351](https://github.com/qgis/QGIS/pull/50351) |
| \[Processing\] Fix typo in smoothing parameter name of gdal_grid algorithms | No reportado | [PR #50261](https://github.com/qgis/QGIS/pull/50261) | [PR #50331](https://github.com/qgis/QGIS/pull/50331) |
| El cliente WFS muestra un SRC erróneo | [#42627](https://github.com/qgis/QGIS/issues/42627) | [PR #50272](https://github.com/qgis/QGIS/pull/50272) | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |
| QGIS doesn\'t work properly with WFS 2.0.0 combined with OGC HTTP URI srsName style (e.g. <http://www.opengis.net/def/crs/EPSG/0/xxxx>) | [#29391](https://github.com/qgis/QGIS/issues/29391) | [PR #50281](https://github.com/qgis/QGIS/pull/50281) | [PR #50386](https://github.com/qgis/QGIS/pull/50386) |
| QGIS ignora el campo heredado del tipo de característica padre en los servicios WFS 2.0 | [#42660](https://github.com/qgis/QGIS/issues/42660) | [PR #50300](https://github.com/qgis/QGIS/pull/50300) | No apropiado |
| La carga y visualización de los datos CADRG/NITF es más lenta que antes. | [#49439](https://github.com/qgis/QGIS/issues/49439) | [PR #50302](https://github.com/qgis/QGIS/pull/50302) | [PR #50352](https://github.com/qgis/QGIS/pull/50352) |
| world_map.gpkg: little fix to avoid warning with recent GDAL versions | No reportado | [PR #50304](https://github.com/qgis/QGIS/pull/50304) | No necesitado |
| QGIS 3.24.1 (Windows) destruye mi mosaico ráster VRT | [#48052](https://github.com/qgis/QGIS/issues/48052) | <https://github.com/OSGeo/gdal/pull/6426> | [PR #50328](https://github.com/qgis/QGIS/pull/50328) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS no recupera la secuencia de postgis en 3.26 | [#49463](https://github.com/qgis/QGIS/issues/49463) | [PR #50247](https://github.com/qgis/QGIS/pull/50247) | no hay necesidad de bp |
| SVG no se renderiza para el símbolo Marcador SVG | [#50208](https://github.com/qgis/QGIS/issues/50208) | No se puede arreglar, problema con Qt |  |
| If \"estimated metadata\" option is checked, feature count for tables/postgis do not work | [#46790](https://github.com/qgis/QGIS/issues/46790) | [PR #50256](https://github.com/qgis/QGIS/pull/50256) | [PR #50425](https://github.com/qgis/QGIS/pull/50425) |
| Fuente de imagen raster variable en compositor no funciona | [#47981](https://github.com/qgis/QGIS/issues/47981) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Cuadro de imagen de diseño de impresión que vuelve a SVG | [#38031](https://github.com/qgis/QGIS/issues/38031) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| Imagen de diseño no puede cambiar imagen SVG a imagen Raster | [#37804](https://github.com/qgis/QGIS/issues/37804) | [PR #50277](https://github.com/qgis/QGIS/pull/50277) | [PR #50332](https://github.com/qgis/QGIS/pull/50332) |
| QgsOptionsPageWidget - helpKey y helpSearchPath no funcionan | [#49421](https://github.com/qgis/QGIS/issues/49421) | [PR #50282](https://github.com/qgis/QGIS/pull/50282) | [PR #50330](https://github.com/qgis/QGIS/pull/50330) |
| Congelación al abrir la tabla de atributos WFS desde un servidor HTTPS con excepción SSL | [#42615](https://github.com/qgis/QGIS/issues/42615) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | sin bp |
| El feed de noticias no se carga al utilizar el instalador MSI | [#49097](https://github.com/qgis/QGIS/issues/49097) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) | sin bp |
| .ci/run_tests.sh: test_core_networkaccessmanager (Timeout) | [#50234](https://github.com/qgis/QGIS/issues/50234) | [PR #50443](https://github.com/qgis/QGIS/pull/50443) |  |
| Símbolo SVG en la versión más reciente de QGIS (3.22.7/8/10 probado) hacer que el software de retraso mucho (y no en la versión 3.4). | [#49818](https://github.com/qgis/QGIS/issues/49818) | Feedback, not sure it's a bug |  |
| Menú desplegable Opciones vacías en la pestaña Registrador de consultas | [#50403](https://github.com/qgis/QGIS/issues/50403) | [PR #50527](https://github.com/qgis/QGIS/pull/50527) | sin bp |
| Build fails with WITH_POSTGRESQL=OFF | [#50075](https://github.com/qgis/QGIS/issues/50075) | Retroalimentación |  |
| Build fails with WITH_GSL=OFF | [#50076](https://github.com/qgis/QGIS/issues/50076) | [PR #50555](https://github.com/qgis/QGIS/pull/50555) |  |
| QGIS master exporta fuera de los límites del diseño | [#48624](https://github.com/qgis/QGIS/issues/48624) | No se puede arreglar, problema con Qt |  |
| Sangrado del trazado hasta el borde fuera de la ventana del mapa | [#49638](https://github.com/qgis/QGIS/issues/49638) | No se puede arreglar, problema con Qt |  |
| Freeze with virtual field on \$area used as parameter in sum | [#49589](https://github.com/qgis/QGIS/issues/49589) | [PR #50533](https://github.com/qgis/QGIS/pull/50533) | [PR #50565](https://github.com/qgis/QGIS/pull/50565) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Funcionalidad: Corrección de errores por Paul Blottiere
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS Server WFS 1.1.0 GetFeature response - properties with xsi:nil=\"true\" | [#45243](https://github.com/qgis/QGIS/issues/45243) | [PR #50495](https://github.com/qgis/QGIS/pull/50495) |  |
| No se pueden mover las etiquetas | [#47542](https://github.com/qgis/QGIS/issues/47542) | No puede reproducir |  |
| Almacenamiento auxiliar y capas eliminadas | [#44667](https://github.com/qgis/QGIS/issues/44667) | [PR #50479](https://github.com/qgis/QGIS/pull/50479) | No recomendado |
| El parámetro OPACITIES no se maneja con la capa Vector Tile en GetMap/GetPrint | [#50364](https://github.com/qgis/QGIS/issues/50364) | [PR #50374](https://github.com/qgis/QGIS/pull/50374) | [PR #50539](https://github.com/qgis/QGIS/pull/50539) |
| Se corrigen los mensajes de registro cuando un error de trabajo no está relacionado con una capa específica. | No reportado | [PR #50372](https://github.com/qgis/QGIS/pull/50372) | No necesitado |
| Labels: Data defined override of \"Show Label\" always wants the auxiliary storage option | [#47993](https://github.com/qgis/QGIS/issues/47993) | [PR #50496](https://github.com/qgis/QGIS/pull/50496) | [PR #50538](https://github.com/qgis/QGIS/pull/50538) |
| Los campos de rotación o desplazamiento del almacenamiento auxiliar para símbolos son visibles por defecto, mientras que las etiquetas no lo son | [#28548](https://github.com/qgis/QGIS/issues/28548) | [PR #50498](https://github.com/qgis/QGIS/pull/50498) |  |
| Mejora de la selección de panoramas ráster PostGIS | No reportado | [PR #50554](https://github.com/qgis/QGIS/pull/50554) | [PR #50575](https://github.com/qgis/QGIS/pull/50575) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Funcionalidad: Bugs corregidos por Sandro Santilli
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Caída del sistema con offline-editing-core-plugin convirtiendo a capa de proyecto offline con polígono vacío | [#50466](https://github.com/qgis/QGIS/issues/50466) | [PR #50577](https://github.com/qgis/QGIS/pull/50577) |  |
| Limpieza temporal de la ruta de configuración de la prueba de python cuando se solicite | [#48884](https://github.com/qgis/QGIS/issues/48884) | [PR #50608](https://github.com/qgis/QGIS/pull/50608) |  |
| Incluir nombre de tipo en mensaje sobre validaciones qfield no soportadas | No reportado | [PR #50589](https://github.com/qgis/QGIS/pull/50589) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir la regresión en los cálculos de saltos de columna en las leyendas | [#42672](https://github.com/qgis/QGIS/issues/42672) | [PR #50597](https://github.com/qgis/QGIS/pull/50597) | Not suitable \-- too risky |
| Corregir error de trazado cuando el src de la capa difiere del src del mapa | [#49247](https://github.com/qgis/QGIS/issues/49247) | [PR #50612](https://github.com/qgis/QGIS/pull/50612) | No requerido |
| Mostrar sólo los SRC disponibles en el widget de selección de capas del WMS | [#45918](https://github.com/qgis/QGIS/issues/45918) | [PR #50572](https://github.com/qgis/QGIS/pull/50572) | No requerido |
| Corregir algunos algoritmos de superposición que generan geometrías multipunto pero la capa de salida es de un solo punto, lo que provoca errores de inserción. | [#49456](https://github.com/qgis/QGIS/issues/49456) | [PR #50567](https://github.com/qgis/QGIS/pull/50567) | [PR #50641](https://github.com/qgis/QGIS/pull/50641) |
| Corregir información que falta en los informes de caídas del sistema en Windows | [#50472](https://github.com/qgis/QGIS/issues/50472) | [PR #50595](https://github.com/qgis/QGIS/pull/50595) | No requerido |
| Corregir la regresión por la que los cuadros de diálogo de la tabla de atributos no se abrían como ventanas de nivel superior con sus propias entradas en la barra de tareas. | [#49286](https://github.com/qgis/QGIS/issues/49286) | [PR #50594](https://github.com/qgis/QGIS/pull/50594) | No requerido |
| \[georeferencer\] Fix options ignored when \"create world file only\" is active | [#49331](https://github.com/qgis/QGIS/issues/49331) | [PR #50566](https://github.com/qgis/QGIS/pull/50566) | No requerido |
| Asegurar que la herramienta de identificación utiliza etiquetas correctas para los valores x/y cuando el orden de los ejes de coordenadas del proyecto es y/x. | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | No requerido |
| Garantizar que la visualización de coordenadas en la barra de estado se actualice inmediatamente cuando cambien los ajustes relacionados, y actualizar la información sobre herramientas para que coincida con los valores reales mostrados en el widget. | [#50540](https://github.com/qgis/QGIS/issues/50540) | [PR #50548](https://github.com/qgis/QGIS/pull/50548) | No requerido |
| Corregir la representación de líneas con valores nan z | [#50510](https://github.com/qgis/QGIS/issues/50510) | [PR #50549](https://github.com/qgis/QGIS/pull/50549) | No requerido |
| Corregir la lógica rota en la limpieza de la historia de la consola de Python | No reportado | [PR #50504](https://github.com/qgis/QGIS/pull/50504) | [PR #50515](https://github.com/qgis/QGIS/pull/50515) |
| Fix QgsFileWidget does not reactivate widget\'s window after selecting a file/folder via the browse button on mac | No reportado | [PR #50501](https://github.com/qgis/QGIS/pull/50501) | [PR #50502](https://github.com/qgis/QGIS/pull/50502) |
| Corregir el plegado de código que no se muestra para las clases de editor de código que no son de python. | No reportado | [PR #50492](https://github.com/qgis/QGIS/pull/50492) |  |
| Corregir una fuga en el uso de la biblioteca de geometría GEOS | No reportado | [PR #50379](https://github.com/qgis/QGIS/pull/50379) |  |
| Corregir el renderizador de contornos de trama que ignora la opacidad. | [#41663](https://github.com/qgis/QGIS/issues/41663) | [PR #50382](https://github.com/qgis/QGIS/pull/50382) | Not suitable \-- too risky |
| Corregir el truncamiento de la lista de proyectos recientes elimina demasiados elementos, plantea una advertencia | No reportado | [PR #50394](https://github.com/qgis/QGIS/pull/50394) | [PR #50397](https://github.com/qgis/QGIS/pull/50397) |
| Corregir huevo de pascua mareado | [#50345](https://github.com/qgis/QGIS/issues/50345) | [PR #50380](https://github.com/qgis/QGIS/pull/50380) | No requerido |
| Corregir el relleno de puntos fijos a veces ignora la opacidad de los símbolos. | [#48031](https://github.com/qgis/QGIS/issues/48031) | [PR #50384](https://github.com/qgis/QGIS/pull/50384) | Not suitable \-- too risky |
| Corregir ruta rota en svg plantea advertencias Qt durante la representación | No reportado | [PR #50383](https://github.com/qgis/QGIS/pull/50383) |  |
| Garantizar que se utiliza el contexto de expresión correcto al generar iconos de vista previa de símbolos. | [#49106](https://github.com/qgis/QGIS/issues/49106) | [PR #50393](https://github.com/qgis/QGIS/pull/50393) | Not suitable \-- too risky |
| \[spatialite\] Fix corrupted default attribute values when fields are loaded using gaiaVectorLayer | Informado privadamente | [PR #50360](https://github.com/qgis/QGIS/pull/50360) | [PR #50361](https://github.com/qgis/QGIS/pull/50361) |
| Corregir el manejo de teselas vectoriales cuando el nivel de acercamiento 0 no está disponible. | [#47934](https://github.com/qgis/QGIS/issues/47934) | [PR #50337](https://github.com/qgis/QGIS/pull/50337) | No requerido |
| Arreglar la función de arrastrar y soltar archivos en la ventana del georreferenciador | [#49175](https://github.com/qgis/QGIS/issues/49175) | [PR #50338](https://github.com/qgis/QGIS/pull/50338) | No requerido |
| Nunca intente manejar valores de tipo parámetro base como capas de mapa en métodos QgsProcessingParameterDefinition::valueAs\*. | [#48598](https://github.com/qgis/QGIS/issues/48598) | [PR #50327](https://github.com/qgis/QGIS/pull/50327) | No requerido |
| Evitar un cálculo redundante de la extensión de la capa visible en el lienzo de vista general. | No reportado | [PR #50329](https://github.com/qgis/QGIS/pull/50329) | [PR #50336](https://github.com/qgis/QGIS/pull/50336) |
| Mostrar pestaña Renderizado estándar en propiedades de capa de nube de puntos, añadir widget de rango de escala faltante a propiedades de capa de malla. | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | No apto |
| Mostrar pestaña Renderizado estándar en propiedades de capa de nube de puntos, añadir widget de rango de escala faltante a propiedades de capa de malla. | [#50268](https://github.com/qgis/QGIS/issues/50268) | [PR #50326](https://github.com/qgis/QGIS/pull/50326) | No apto |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix \"Add Ring\" tool doesn\'t consider all the overlapping features | [#23113](https://github.com/qgis/QGIS/issues/23113) | [#50447](https://github.com/qgis/QGIS/pull/50447) | No apto - añadir nuevos métodos |
| Corregir wkbType a partir de OGR 25D Type | [#50218](https://github.com/qgis/QGIS/issues/50218) | [#50233](https://github.com/qgis/QGIS/pull/50233) | [#50251](https://github.com/qgis/QGIS/pull/50251) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/)

{{<content-end >}}
