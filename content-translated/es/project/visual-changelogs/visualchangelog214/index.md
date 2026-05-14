---
HasBanner: false
draft: false
releaseDate: '2016-02-26'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.14
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.14{#changelog214 }
![image1](images/projects/596e7e353771d2802f065352548e512b8d902d83.png)

Fecha de lanzamiento: 2016-02-26

This is the changelog for the next release of QGIS - version 2.14 \'Essen\'. Essen was the host city to our developer meet ups in October 2012 and 2014.

**Lanzamiento a Largo Plazo**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for **one year**, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). Note that we are in discussion to extend the term of our LTR releases to two years, but for technical reasons we will not do this until QGIS 3.2.

El propósito de los lanzamientos de LTR es proporcionar una plataforma estable y que cambie con menos frecuencia para empresas y organizaciones que no desean lidiar con la actualización de las habilidades de los usuarios, materiales de capacitación, etc. más de una vez al año. El éxito de la LTR depende de ustedes, nuestros queridos usuarios: necesitamos su apoyo para ayudar a financiar las correcciones de errores y asegurarnos de que en sus contratos de soporte con proveedores de soporte especifique que las correcciones de errores realizadas en su nombre se aplican a la sucursal de LTR así como nuestra rama de desarrollo normal.

Si un LTR es importante para usted, considere también apoyar directamente el proyecto QGIS, o aliente a su proveedor comercial a usar LTR como base para su solución empresarial para que todos puedan beneficiarse de una plataforma estable que se mejora y refina continuamente. Tenga en cuenta que para los usuarios y las organizaciones que les gusta vivir en la frontera, nuestros lanzamientos regulares cada cuatro meses continuarán sin cesar.

**New Features in QGIS 2.14 \'Essen\'**

If you are upgrading from QGIS 2.8 (our previous LTR version) you will find a great many new features in this release. We encourage you to peruse the changelogs for the intermediate non LTR [2.10](../visualchangelog210/) and [2.12](../visualchangelog212/) releases as this QGIS 2.14 includes all features published in those releases too. Note that 2.14 first enters the regular package repositories and will not immediately replace 2.8 in the LTR package repositories. That will happen when 2.16 is released.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six-monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it - in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html)

{{<table-of-contents >}}
## Patrocinadores QGIS actuales
{{<fund type="changelog" >}}
## General
### Característica: Cambiado comportamiento de función strpos
The strpos function behaviour has been altered, so that no match now results in a \"0\" value and a non-zero value means a match at the specified character position. In older QGIS versions, a \"-1\" value would mean no-match and other return values represented the character position - 1.

Los archivos de proyecto de versiones anteriores de QGIS deberán actualizarse para reflejar este cambio.

![image47](images/entries/74ddb567a30e840405ca83656e76dd6476d00226.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Jürgen Fischer
### Característica: Acercamiento a elemento con click-derecho en tabla de atributos
Ahora puede acercarse a cualquier elemento dentro de la tabla de atributos (sin tener que seleccionarlo primero) haciendo click derecho y seleccionado acercar a elemento.

![image48](images/entries/7a400f577a7d554f309297f8a1af05a61e448a27.png.400x300_q85_crop.webp)
### Característica: Mejoras en velocidad y memoria
- **Guardando un conjunto de los elementos seleccionados** de una capa grande ahora es mucho más rápido
- Ahora es más rápida la actualización sólo en elementos seleccionados usando la **calculadora de campo**
- **Acercamiento más rápido** a seleccionado en capas grandes
- Much faster `get_feature` expression function (especially when an indexed column in the referenced layer is used)
- `SelectByAttribute` and `ExtractByAttribute` processing algorithms are orders of magnitude faster, and can take advantage of database indices created on an attribute
- `PointsInPolygon` processing algorithm is many magnitudes faster
- **Filtrar las categorías en un renderizador categorizado** (por ejemplo, solo mostrar algunas categorías y desmarcar otras) es mucho más rápido, ya que ahora solo se obtienen las características coincidentes del proveedor de datos
- Significativa **reducción en memoria** requerida para la apertura de capas vector grandes

### Característica: Más variables de expresión
Durante la representación, estarán disponibles nuevas variables:
- `@geometry_part_count`: The part count of the currently rendered geometry (interesting for multi-part features)
- `@geometry_part_num`: 1-based index of the currently rendered geometry part

Estos son útil para aplicar estilos diferentes a partes diferentes de elementos multiparte:
- `@map_extent_width`: The width of the currently rendered map in map units
- `@map_extent_height`: The height of the currently rendered map in map units
- `@map_extent_center`: The center point of the currently rendered map in map units

También se han agregado variables relacionadas con el ambiente del sistema operativo:
- `@qgis_os_name`: eg \'Linux\',\'Windows\' or \'OSX\'
- `@qgis_platform`: eg \'Desktop\' or \'Server\'
- `@user_account_name`: current user\'s operating system account name
- `@user_full_name`: current user\'s name from operating system account (if available)

![image49](images/entries/b2e29d9df21795416961b8b548f98078386eeecf.png.400x300_q85_crop.webp)

Esta característica fue financiada por Andreas Neumann (el SO y las variables relacionadas con usuario)

Esta característica fue desarrollada por Nyall Dawson, Matthias Kuhn
### Característica: Mejor control sobre la ubicación de elementos de mapa
QGIS 2.14 ha obtenido un control más preciso sobre la colocación de flechas del norte, barras de escala y avisos de derechos de autor en el canvas del mapa principal. Ahora puede establecer con precisión la posición de estos elementos utilizando variedad de unidades (incluidos milímetros, píxeles y porcentajes).

![image50](images/entries/e2390ce8f4bc93ebf00228e1545b192315d2cb57.png.400x300_q85_crop.webp)
### Característica: Programa pagado de arrego de fallos
Antes de cada lanzamiento, tenemos un programa de pago de corrección de errores donde financiamos a los desarrolladores para que eliminen la mayor cantidad de errores posible. Hemos decidido comenzar a incluir un informe sobre el programa de corrección de errores de pago como parte de nuestro informe de registro de cambios. Tenga en cuenta que esta lista es **no exhaustiva**.
- Sandro Santilli: [Postgis Connection freeze if you press \"Set filter\" during loading of data](http://hub.qgis.org/issues/13141)
- Sandro Santilli: [db_manager is unable to load rasters from connections with no dbname specified](http://hub.qgis.org/issues/10600)
- Sandro Santilli: [Plugin layers do not work correctly with rotation](http://hub.qgis.org/issues/11900)
- Sandro Santilli: Crash in QgsGeomColumnTypeThread stopping connection scan [#14140](http://hub.qgis.org/issues/14140) [#13806](http://hub.qgis.org/issues/13806)
- Sandro Santilli: [Crash after bulk change of attribute value in shapefile](http://hub.qgis.org/issues/11422)
- Sandro Santilli: [KMZ causes QGIS application crash (Mac)](http://hub.qgis.org/issues/13865)
- Sandro Santilli: [QGIS 2.8.1 crash opening FileGDB (openGDB-Driver)](http://hub.qgis.org/issues/12416)
- Sandro Santilli: [QGIS crashes when removing vertex of a multipart geometry](http://hub.qgis.org/issues/14188)
- Sandro Santilli: [test -V -R qgis_analyzertest segfaults](http://hub.qgis.org/issues/14176)
- Sandro Santilli: [output/bin/qgis_diagramtest segfaults](http://hub.qgis.org/issues/14212)
- Sandro Santilli: Overflow on primary key with negative values; crashes QGIS when editing [#13958](http://hub.qgis.org/issues/13958) [#14262](http://hub.qgis.org/issues/14262)
- Sandro Santilli: [PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Sandro Santilli: [TestVectorLayerJoinBuffer hangs if database is not available](http://hub.qgis.org/issues/14308)
- Nyall Dawson: [BLOCKER: Crash when opening layer properties dialog for geometryless vector layer](http://hub.qgis.org/issues/14116)
- Nyall Dawson: Ruptura del lado del servidor filtrando para OGR, Oracle y capas Spatialite
- Nyall Dawson: [BLOCKER: Bad polygon digitizing in master](http://hub.qgis.org/issues/14117)
- Nyall Dawson: [BLOCKER: Heatmap with expression triggers segfault](http://hub.qgis.org/issues/14127)
- Nyall Dawson: [BLOCKER: unchecking one sub-layer of a categorized symbology leads to no features being drawn](http://hub.qgis.org/issues/14118)
- Nyall Dawson: [HIGH: A Multiband image(e.g. landsat5,7,8) cannot be displayed in windows8](http://hub.qgis.org/issues/13155)
- Nyall Dawson: [BLOCKER: CurvePolygons not drawn](http://hub.qgis.org/issues/14028)
- Nyall Dawson: [BLOCKER: \"Merge Attributes\" tool doesn\'t change values when they are typed](http://hub.qgis.org/issues/14146)
- Nyall Dawson: [HIGH: Filter legend by content is broken when renderer contains duplicate symbols](http://hub.qgis.org/issues/14131)
- Nyall Dawson: Solucion de problemas con la conversión de renderizadores a renderizadores basados en reglas que resultan en un renderizador roto
- Nyall Dawson: Reparar el renderizador categorizado que no almacena cambios en el símbolo de origen
- Nyall Dawson: [HIGH: Avoid crash with raster calculator and huge raster inputs](http://hub.qgis.org/issues/13336)
- Nyall Dawson: [HIGH: \@value variable of simple symbol fill color wrongly gets modified in data-defined expression](http://hub.qgis.org/issues/14148)
- Nyall Dawson: [HIGH: Editing Composer legend while filtered does not work](http://hub.qgis.org/issues/11459)
- Nyall Dawson: [NORMAL: Deleting nodes - inconsistent behaviour](http://hub.qgis.org/issues/14168)
- Nyall Dawson: Arreglar manejo de valores de tiempo en atributos
- Nyall Dawson: arreglos en orden de pestañas de Diálogo
- Nyall Dawson: [BLOCKER: crash when adding multiple files from browser panel](http://hub.qgis.org/issues/14223)
- Nyall Dawson: [HIGH: Merge selected features tool corrupts data when columns are defined as \"hidden\"](http://hub.qgis.org/issues/14235)
- Nyall Dawson: Manejar correctamente los campos LongLong en el diálogo de combinación de atributos
- Nyall Dawson: Se corrigió la visualización engañosa de los detalles de cálculo en el cuadro de diálogo de la herramienta de medición (era engañoso e inexacto para muchas combinaciones de CRS/unidad)
- Nyall Dawson: [NORMAL: max value for option \"increase size of small diagrams\" not sufficient](http://hub.qgis.org/issues/14282)
- Nyall Dawson: [BLOCKER: Area not calculated correctly with OTF on](http://hub.qgis.org/issues/13209)
- Nyall Dawson: [NORMAL: Incoherent lat/lon coordinates in a projected coordinate system project](http://hub.qgis.org/issues/9730)
- Nyall Dawson: NORMAL: make the field calculator compute areas and lengths in units other than map units [#12939](http://hub.qgis.org/issues/12939) [#2402](http://hub.qgis.org/issues/2402) [#4857](http://hub.qgis.org/issues/4857)
- Nyall Dawson: [NORMAL: different built-in tools calculate inconsistent polygon areas](http://hub.qgis.org/issues/4252)
- Nyall Dawson: [NORMAL: In virtual fields \$area function computes always values using \"None/planimetric\" ellipsoid](http://hub.qgis.org/issues/12622)
- Martin Dobias: capa ráster dibujada como basura
- Martin Dobias: HIGH: Multi-threaded rendering and OTF reprojection issues [#11441](http://hub.qgis.org/issues/11441) [#11746](http://hub.qgis.org/issues/11746)
- Martin Dobias: [BLOCKER: Regression in \"save as\" dialog for shapefiles](http://hub.qgis.org/issues/14158)
- Martin Dobias: Carga lenta de tabla de atributos en modo depuración
- Martin Dobias: [BLOCKER: Crash when changing renderer type](http://hub.qgis.org/issues/14164)
- Martin Dobias: [HIGH: Custom python renderer issues #1](http://hub.qgis.org/issues/14025)
- Martin Dobias: [HIGH: Custom python renderer issues #2](http://hub.qgis.org/issues/13973)
- Martin Dobias: arreglos visualizador 2.5d
- Martin Dobias: [HIGH: Long freeze when initializing snapping](http://hub.qgis.org/issues/12578)
- Martin Dobias: [NORMAL: Loading of data-defined from xml](http://hub.qgis.org/issues/14177)
- Martin Dobias: Fix DB manager to work with SpatiaLite \< 4.2
- Martin Dobias: [NORMAL: Crash while rendering in debug mode](http://hub.qgis.org/issues/14369)
- Martin Dobias: BLOCKER: Fix selection / identification in spatialite views [#14232](http://hub.qgis.org/issues/14232) [#14233](http://hub.qgis.org/issues/14233)
- Martin Dobias: [BLOCKER: Fix drag&drop of spatialite tables](http://hub.qgis.org/issues/14237)
- Jürgen Fischer:[Zoom to layer works incorrectly while layer editing](http://hub.qgis.org/issues/3155)
- Jürgen Fischer:[Help viewer process running in the background with no help viewer (or even QGIS) open](http://hub.qgis.org/issues/8305)
- Jürgen Fischer:[Spatialindex include path missing in some components](http://hub.qgis.org/issues/13197)
- Jürgen Fischer:[compile fails attempting to generate qgsversion.h](http://hub.qgis.org/issues/13680)
- Jürgen Fischer:[Edit widget configuration is stored twice](http://hub.qgis.org/issues/13960)
- Jürgen Fischer:[Extra space in \"IS NOT\" operator makes the expression return wrong selection](http://hub.qgis.org/issues/13938)
- Jürgen Fischer:[QGIS greadily allocates memory and crashes when editing moderately large shapefiles with the node tool](http://hub.qgis.org/issues/13963)
- Jürgen Fischer:[French reprojection use ntf_r93.gsb (IGNF:LAMBE etc ..)](http://hub.qgis.org/issues/14101)
- Jürgen Fischer:[Digitizing: \"Reuse last entered attribute values\" should not overwrite primary key column](http://hub.qgis.org/issues/14154)
- Jürgen Fischer:[Issues in Case expression description](http://hub.qgis.org/issues/14189)
- Jürgen Fischer:[shapefile vector writer: datetime field saved as date resulting in data loss of time](http://hub.qgis.org/issues/14190)
- Jürgen Fischer:[Add help for some variable functions](http://hub.qgis.org/issues/14259)
- Jürgen Fischer:[Virtual layers not working in Processing](http://hub.qgis.org/issues/14313)
- Jürgen Fischer:[layer definition file load error](http://hub.qgis.org/issues/14340)
- Jürgen Fischer:[QgsGeometry::fromWkb fails if WKB is different endian representation](http://hub.qgis.org/issues/14204)
- Jürgen Fischer:[Debian build failure.](http://hub.qgis.org/issues/14248)
- Jürgen Fischer:[PyQgsPostgresProvider test hangs in absence of test database](http://hub.qgis.org/issues/14269)
- Jürgen Fischer:[wkb access out of bounds](http://hub.qgis.org/issues/14315)
- Jürgen Fischer:[QGIS under Windows netCDF import reverses Y axis, Linux doesn\'t](http://hub.qgis.org/issues/14316) [OSGeo4W #483](https://trac.osgeo.org/osgeo4w/ticket/483)
- Jürgen Fischer:[OSGEO4W: Running offline install crashes installer](https://trac.osgeo.org/osgeo4w/ticket/105)
- Jürgen Fischer:[OSGEO4W: Dependencies are not tracking on Windows Server 2003 x64](https://trac.osgeo.org/osgeo4w/ticket/117)
- Jürgen Fischer:[OSGEO4W: installation from local package don\'t check the dependencies](https://trac.osgeo.org/osgeo4w/ticket/151)
- Jürgen Fischer:[OSGEO4W: Setup starts downloading and installing packages before showing you a list to choose from](https://trac.osgeo.org/osgeo4w/ticket/262)
- Jürgen Fischer:[OSGEO4W: Using -a for Advanced selects two options (command line install)](https://trac.osgeo.org/osgeo4w/ticket/351)
- Jürgen Fischer:[OSGEO4W: Infinite license download during quite installation of szip](https://trac.osgeo.org/osgeo4w/ticket/486)
- Jürgen Fischer: atasco en proveedor Oracle
- Jürgen Fischer: arreglar definición de ruta para Saga

### Feature: Field calculator can be used to update feature\'s geometry
La calculadora de campo ahora se puede usar para actualizar geometrías de entidades usando el resultado de una expresión geométrica. Este es un atajo útil para realizar operaciones como aplicar un búfer a un grupo de entidades seleccionadas, y junto con todas las funciones de geometría recientemente agregadas en 2.14, ¡es una forma muy práctica de manipular sus geometrías!

![image51](images/entries/ba37e2e778a2349c7099e09fcf648238090d8af4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Prestación: Nuevas funciones de expresión en 2.14
Se han agregado muchas nuevas expresiones para la versión 2.14:
- `relate`: performs a DE-9IM geometry relation by either returning the DE-9IM representation of the relationship between two geometries, or by testing whether the DE-9IM relationship matches a specified pattern.
- the `make_point` function now accepts optional z and m values, and a new `make_point_m` function has been added for creation of PointM geometries.
- `m` and `z` functions for retrieving the m and z values from a point geometry
- new `make_line` and `make_polygon` functions, for creation of line and polygon geometries from a set of points
- `reverse`, for reversing linestrings
- `eval` function, which can evaluate a string as though it is an expression of its own
- `translate` function, for translating geometries by an x/y offset
- `darker` and `lighter` functions, which take a color argument and make it darker or lighter by a specified amount
- `radians` and `degrees`: for converting angles between radians and degrees
- `point_on_surface`: returns a point on the surface of a geometry
- `exterior_ring`: returns the exterior ring for a polygon geometry
- `is_closed`: returns true if a linestring is closed
- new geometry accessor functions: `geometry_n` (returns a specific geometry from within a collection), `interior_ring_n` (returns an interior ring from within a polygon)
- `num_geometries`: returns number of geometries inside a collection
- `num_rings`: returns number of rings in a polygon geometry object
- `num_interior_rings`: returns number of interior rings in a polygon
- `nodes_to_points`, for converting every node in a geometry to a multipoint geometry
- `segments_to_lines`, for converting every segment in a geometry to a multiline geometry
- `closest_point`: returns closest point in a geometry to a second geometry
- `shortest_line`: returns the shortest possible line joining two geometries

`nodes_to_points` and `segments_to_lines` are intended for use with geometry generator symbology, eg to allow use of m and z values for nodes/lines with data defined symbology.

Otras mejoras:
- geometries and features can now be used in conditional functions. For instance, this allows expressions like `case when $geometry then ... else ...` and `case when get_feature(...) then ... else ...`

![image52](images/entries/98616590f44281e09aa24f6c30d7f668c8665c31.png.400x300_q85_crop.webp)
## Herramientas de análisis
### Característica: Más estadísticas están disponibles en la herramienta fusionar atributos
Cuando se usan los valores de atributo de fusión o la herramienta de características de fusión, hay disponibles resumenes adicionales de estadísticas que se pueden usar para establecer los valores de atributo resultantes. Estos incluyen Q1, Q3, rangos intercuartiles, valores mayoritarios y minoritarios, y número de valores únicos, entre otros.

![image27](images/entries/3820507f3bffdaab2bafe7285a8c51791f0b1fdb.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: valores z/m son mostrados cuando se usa la herramienta identificar
La herramienta de identificación ahora puede mostrar cualquier valor z o m presente en las características identificadas. Si la entidad es una línea o polígono, la herramienta mostrará el número de vértice y x/y/z/m para el vértice más cercano al punto identificado. La herramienta de identificación ahora también muestra el número de partes y el número de parte para colecciones.

![image28](images/entries/c9813d351340f46e28e6a0cb576a4b2ca72466a9.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Manejo unificado de unidades de distancia y área y formatos de coordenada
En QGIS 2.14, el manejo de varias opciones con respecto a unidades de distancia, unidades de área y visualización de coordenadas se ha unificado, simplificado y trasladado a Propiedades del proyecto. Este cambio trae numerosos beneficios, que incluyen:
- El formato de coordenadas especificado en las Propiedades del proyecto se usa de manera consistente cada vez que se muestra una coordenada al usuario, incluidos los resultados de la herramienta de identificación y la visualización de la barra de estado.
- The setting for distance and area units in Project Properties is respected for all distance and area calculations, including the measure tool, identify results, and use of the `$area`, `$length` and `$perimeter` functions.
- Se han agregado unidades de área adicionales, que incluyen yardas cuadradas, acres, hectáreas y más.
- Se han agregado unidades angulares adicionales a la herramienta de medición de ángulo, incluyendo rotaciones, minutos de arco y segundos de arco.
- It\'s now possible to show the coordinates in latitude and longitude in the status bar even when using a projected CRS.

![image29](images/entries/b086f236720ecb5cac0aa8bb7383275799affff4.png.400x300_q85_crop.webp)

Esta característica fue financiada por el programa de corrección de fallos patrocinado por QGIS

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Navegador
### Característica: Mejoras al Navegador
El navegador QGIS es un sistema de archivos, servicios web OGC y un panel de conexión de base de datos que le permite arrastrar y soltar fácilmente cualquier capa de las fuentes mencionadas en el lienzo del mapa (o en la ventana del Administrador de base de datos). Se agregaron dos nuevas mejoras útiles para esta versión:
- **Se pueden esconder selectivamente las rutas en el panel de navegación** -esto es útil para hacer menos cargada su lista de fuentes y enfocar únicamente en directorios relevantes.
- **Cargue proyectos directamente desde el navegador**: ahora puede arrastrar y soltar un proyecto completo en el lienzo del mapa QGIS y se cargará.

![image30](images/entries/8479ec7c4077c9602d6eacdb11d518bd55922074.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Nathan Woodrow
## Proveedores de datos
### Característica: Capacidades caché WMS
QGIS will now cache WMS `GetCapabilities` requests so that on subsequent use response times will be quicker when using that service. By default the cache period is 24 hours, but you can adjust this in the `Network` tab of the QGIS Settings dialog.

![image31](images/entries/743840449ddf09f45251e9710e9666cf4da86081.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Jürgen Fischer
### Característica: Expandido soporte de geometría curveada
The delimited text provider now supports curved WKT strings, and the memory provider (eg \"temporary scratch\" layers) has gained full support for curved geometries. Additionally, if QGIS has been built using GDAL versions 2.0 and up then QGIS will fully support curved geometries in supported file types (eg GML files).

![image32](images/entries/79f4b8256ab3507b192277c4f14d3bb04423dc52.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Mejor manejo de campos hora y fechahora
QGIS 2.14 ha mejorado el manejo de tipos de campo tiempo y fechatiempo, incluyendo:
- Campos marca de tiempo (timestamp) PostgreSQL se manejan correctamente
- El motor de expresión ahora dispone de soporte completo para campos hora
- El generador de expresiones ahora muestra resultados de cálculo de vista previa para fecha, hora, fecha, hora e intervalos
- Los campos de tiempo son totalmente compatibles con las capas de archivos vectoriales (según el formato del archivo), PostgreSQL, MS SQL Server y capas temporales temporales
- Guardar capas a archivos vector preservará los campos de    tiempo si existe soporte por el formato de capa vector (ej. archivos .tab Mapinfo)

![image33](images/entries/2511118cd31ca53892ef5764cf8e80d9491d131a.png.400x300_q85_crop.webp)

Esta característica fue desarrollada por Jürgen Fischer, Nyall Dawson
### Característica: Soport Z/M en proveedor de texto delimitado
The delimited text provider has gained support for WKT strings containing Z and M coordinates. For example you can express a point with z and measure elements like this : `POINT ZM (1 1 5 60)`.

![image34](images/entries/41d5c223ac43b4f8f392894109414e9d053c9136.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Grupos de transacción para edición postgres
Se ha introducido una nueva opción para activar edición transaccional.

Cuando esta opción está activada
- Todas las capas de la misma base de datos se colocan en el grupo de transacción
- Cuando la primera capa de un grupo pasa al modo edición, todas las otras son automáticamente pasadas a edición
- Cuando se edita una capa, los cambios se envían a la base de datos inmediatamente, lo que permite que los desencadenantes y las restricciones se apliquen de inmediato.
- Cuando se confirma una capa en un grupo de transacciones, se confirman todas las capas (transacción de base de datos)
- Cuando una capa de un grupo de transacciones se revierte, todas las capas se revierten (transacción de la base de datos)

This feature is currently **Experimental**. If you find any problems, please [report them](https://www.qgis.org/en/site/getinvolved/development/bugreporting.html).

Por ahora esto está implementado solamente para bases de datos postgres.

![image35](images/entries/bb8a03f09c9675985409cf4360308509830d38d4.png.400x300_q85_crop.webp)

This feature was funded by [SIGE](http://www.sige.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch, based on work by Sourcepole](https://opengis.ch)
### Característica: Autentificación PKI para proveedor Postgres
La capacidad de utilizar el Administrador de autenticación QGIS introducido en 2.12 se ha extendido al proveedor de PostGIS. Esto permite conectarse a Postgres mediante autenticación básica o PKI, con las credenciales almacenadas en la configuración de QGIS. La nueva autenticación del proveedor de Postgres también se puede usar en el administrador de bases de datos.

![image36](images/entries/6e8f65042bd5981e585812ce2d957d0c6055ba3f.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Esta característica fue desarrollada por Luigi Pirelli
### Característica: Capas virtuales
Las consultas SQL dinámicas ahora se pueden usar en cualquier tipo de capas vectoriales que QGIS pueda cargar, ¡incluso si el formato de capa en sí no tiene soporte para consultas SQL!

A new kind of vector layer called \"virtual layer\" is now available for that purpose. These allow you to create a virtual layer by defining a query (including support for aggregates and joins) from other layers in your project. The resultant layer will be a live, dynamic view of the query result, so any changes to the source layers will be automatically and immediately reflected in the virtual layer!

El dialecto SQL admitido es SQLite con funciones Spatialite. Las funciones de expresión QGIS también se pueden usar en consultas. Se puede acceder a cualquier tipo de capas vectoriales en la consulta, incluidas varias capas de diferentes proveedores de datos para hacer uniones.

Support for virtual layers has also been added to DB Manager as well as to the Processing toolbox where a new \'Execute SQL\' tool is available.

![image37](images/entries/58bc1a2fea31fe8d6ab70ff33c763c9ddac40ade.png.400x300_q85_crop.webp)

This feature was funded by [MEDDE (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
### Característica: Más extensiones de archivo para selectores de archivo de proveedores GDAL y OGR
Para archivos vectoriales y ráster, QGIS se basa en la biblioteca GDAL/OGR. Significa que casi cualquier formato de archivo que GDAL u OGR se puede abrir directamente en QGIS. Hasta ahora, algunas extensiones de archivo no se agregaron en el selector de archivos GDAL u OGR, lo que hace que los usuarios crean que QGIS no puede abrir o manejar esos formatos de archivo. Para minimizar este problema, se han agregado algunas extensiones nuevas a los filtros de selección de archivos GDAL y OGR:

**Para archivos vector:**
- .thf para el formato francés de catastro EDIGEO
- .ods para el formato OpenDocument Spreadsheet de LibreOffice
- .xls para formato Microsoft Excel
- .xlsx para formato Microsoft Excel OpenXML
- .xml para formato NAS - ALKIS
- .map para formato WAsP
- .pix para formato PCIDSK
- .gtm y .gtz para formato GPSTrackMaker
- .vfk para formato VFK
- .osm y .pbf para formato OpenStreetMap
- .sua para formato SUA
- .txt para formato OpenAir
- .xml para formato TABLE Planetary Data Systems
- .htf para Hydrographic Transfer Format
- .svg para formato SVG
- .gen para ARCGEN
- .sxf para Storage and eXchange
- .pdf para formato vector Geospatial PDF
- .sgy y .segy para formato SEG-Y
- .seg, .seg1, .sp1, .uko, .ukooa para formato SEGUKOOA
- .ovf para formato de archivo vector VRT
- .kmz para formato comprimido KML (KMZ)
- .db3, .s3db, .sqlite3, .db3, .s3db, .sqlite3 para formato SQLite/Spatialite
- .sl3 para formato SQLite Spatial (FDO)
- CouchDB Spatial (vía URL)

**Para archivos ráster:**
- .ovr para formato de archivo ráster vrt

![image38](images/entries/7a628a66f2f63454bd65fbedda309ff5a7d25f1e.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
### Feature: Use ST_RemoveRepeatedPoints for server-side simplification with PostGIS 2.2 (or newer) layers
When using a PostGIS 2.2 instance, QGIS now uses the ST_RemoveRepeatedPoints function instead of the ST_SnapToGrid function to process server-side simplification, as described by [Paul Ramsey](http://blog.cartodb.com/smaller-faster/).

Este método disminuirá el número de vértices de las geometrías que QGIS necesita descargar del servidor, lo que aumentará la velocidad de renderizado y ahorrará ancho de banda entre QGIS y el servidor PostgreSQL.

![image39](images/entries/bea701efeedd257314f507dfb2689fbf95403095.png.400x300_q85_crop.webp)

This feature was developed by [Michaël Douchin \@kimaidou](http://3liz.com)
## Gestión de datos
### Característica: Eliminación del complemento SPIT
The \"SPIT\" plugin is no longer bundled with QGIS, as the plugin was unmaintained and has been surpassed by DB Manager and the processing database import algorithms.

![image40](images/entries/b496fc25b098575ece2a38ea5a601caf75bb51dc.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Nathan Woodrow
### Característica: exportar DXF: opción para usar título en vez de nombre como nombre de capa DXF en la aplicación y servidor
![image41](images/entries/e09652676e15a883821ca9b269c03ab0239aacb3.png.400x300_q85_crop.webp)

This feature was funded by [City of Uster](http://gis.uster.ch/)

Esta prestación fue desarrollada por Jürgen Fischer
### Característica: El tipo de geometría puede ser redefinida en el diálogo de guardar vector
Esto hace posible hacer cosas como guardar una tabla sin geometría CON un tipo de geometría, de modo que las geometrías se puedan agregar manualmente a las filas. Anteriormente, esto solo era posible en QGIS recurriendo a combinaciones ficticias u otras soluciones.

Además, se han agregado opciones para forzar que el archivo de salida sea de tipo múltiple o que incluya una dimensión z.

![image42](images/entries/886630cb835b72865c5442a73a79b46cc5a7b60f.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Prestación: Las uniones vectoriales ahora se guardan dentro de los archivos de definición de capa QLR
### Característica: Widget de Recurso Externo
A new form widget is now available. It is named \"External resource\" and it allows a more complete handling of attributes assigned to file paths storing. Here is a complete summary of the widget features:
- You can set an **extension filter** to force the storing of fixed file formats. If a filter is set, the file selector will only show file names that are relevant to the filter (it is still possible to select any file by using \'\*\' character in the search field). Filter syntax is the same than [Qt widget QFileDialog::getOpenFileName](https://doc.qt.io/qt-4.8/qfiledialog.html#getOpenFileName).
- You can set a **default path**. Each time a user triggers the widget, a file selector will open at the default path (if set). If no default path has been set, the file selector will use the last path selected from an \"External resource\" widget. If the widget has never been used, the file selector defaults to opening on the project path.
- Puede definir y establecer **almacenamiento de ruta relativa**. El almacenamiento de la ruta relativa le permitirá guardar solo la parte de la ruta que está después de la ruta predeterminada (si la ruta predeterminada está configurada) o la ruta actual del proyecto. Esto es particularmente útil cuando desea guardar rutas largas en atributos de tamaño limitado (como los atributos de texto para Shapefiles que están limitados a 254 caracteres), o para crear archivos de proyectos y archivos de datos independientes para su distribución.
- Otra nueva característica para hacer que el widget sea más fácil de usar es que **las rutas de archivos ahora se pueden mostrar como hipervínculos**. Al hacer clic en el hipervínculo se abrirá directamente el archivo vinculado desde QGIS. Puede configurar esta opción para mostrar la ruta completa del archivo o solo su nombre de archivo. El archivo se abrirá utilizando el controlador predeterminado para ese formato de archivo de su sistema operativo.
- También puede ** usar una URL en lugar de una ruta de archivo **. El widget lo interpretará como una URL y podrá abrir la página web vinculada directamente en su navegador web predeterminado.
- Puede elegir **almacenar rutas de directorio en vez de rutas de archivo**.
- Hay un ** visor de documentos integrado ** en este widget. Puede usarlo para mostrar imágenes o páginas web directamente en QGIS. El selector de archivos para el visor integrado se beneficiará de todas las opciones mencionadas anteriormente.

Para obtener más información sobre las opciones de configuración, puede utilizar la información sobre herramientas del cuadro de diálogo de configuración.

The main aim of this new widget is to fix and improve the two existing \'File name\' and \'Photo\' widgets, and replace them with a single unified widget. For the moment, you can still use the old widgets but they will be deprecated and removed for QGIS 3.0. We recommend to switch your projects to use the new \'External Resource\' widget now.

**Esta característica fue desarrollada por**:
- [Denis Rouzaud](https://github.com/3nids)
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)
- [Médéric Ribreux](https://medspx.fr)

![image43](images/entries/d20edab2103d774f548a55552ca2dbe20ac39e67.png.400x300_q85_crop.webp)
### Característica: Edición de relación N:M
Esto agrega la posibilidad de administrar datos en una base de datos relacional normalizada en relaciones N: M (muchas a muchas). En el editor de relaciones en un formulario, las herramientas para agregar, eliminar, vincular y desvincular también funcionan en la tabla de vinculación si una relación se visualiza como una relación N: M.

La configuración se realiza a través de la pestaña de campos donde en la relación se puede elegir una segunda relación (si hay una relación adecuada en términos de una segunda relación en la tabla de enlace).

**Limitaciones:**

QGIS no es un sistema de gestión de base de datos.

Está basado en supuestos sobre el sistema de base de datos subyacente, En particular:
- it expects an `ON DELETE CASCADE` or similar measure on the second relation
- it does not take care of setting the primary key when adding features. Either users need to be instructed to set them manually or - if it\'s a database derived value - the layers need to be in transaction mode

![image44](images/entries/9f033883617b01432aae23c35be54070c1a9f5b3.png.400x300_q85_crop.webp)

Esta característica está financiada por République et canton de Neuchâtel, Ville de Pully, Ville de Vevey

This feature was developed by [Matthias Kuhn](http://opengis.ch)
## Digitalizando
### Característica: Color configurable de la banda elástica
Ahora puede establecer el ancho y el color de la banda elástica utilizados para la digitalización.

![image45](images/entries/40ef6c2f93c7697133ebede324fe9dafe40f42f0.png.400x300_q85_crop.webp)
### Característica: Herramienta de ditilización de trazo
La nueva herramienta de digitalización con rastreo es una herramienta de digitalización avanzada que le permite digitalizar entidades en una capa rastreando entidades en otra capa.

La herramienta de trazado:
- uses Dijkstra's shortest path algorithm to find traceable routes
- puede trazar rutas sobre múltiples elementos distintos
- puede ser usado con herramientas Digitalización Avanzada (ej.: remodelado)
- puede ser habilitado y desabilitado presionando **T** en su teclado mientras digitaliza
- es rápido y fácil de usar

You can read more about this feature [here](http://www.lutraconsulting.co.uk/blog/2016/02/16/qgis-trace-digitising/) and with [this tutorial](http://www.lutraconsulting.co.uk/products/autotrace/TraceDigitising).

Esta prestación fue fundada por: The Royal Borough of Windsor and Maidenhead, Neath Port Talbot County Borough Council, Ujaval Gandhi, Surrey Heath Borough Council, Matias Arnold, Northumberland National Park Authority, Buccleuch Estates Limited, Countryscape

![image46](images/entries/357ff84cf7685a2686a019ebe42f0012b495f79a.png.400x300_q85_crop.webp)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
## Etiquetando
### Feature: \"Cartographic\" placement mode for point labels
En este lugar de emplazamiento, los candidatos de etiqueta de punto se generan siguiendo reglas de colocación ideal cartográfica, por ejemplo, las ubicaciones de etiqueta se priorizan en el orden:
- arriba derecha
- arriba izquierda
- abajo derecha
- abajo izquierda
- al medio derecha
- al medio izquierda
- arriba, ligeramente derecha
- abajo, ligeramente izquierda

(respetando las guías de Krygier y Wood (2011) y otros trabajos maestros cartográficos)

La prioridad de ubicación también se puede establecer para una característica individual utilizando una lista definida de datos de posiciones priorizadas. Esto también permite que solo se usen ciertas ubicaciones, por lo que, por ejemplo, para las características costeras, podría evitar que se coloquen etiquetas sobre la tierra.

![image53](images/entries/23cdbb38f45b05ea930fbeec8ad461e2616ef2a9.png.400x300_q85_crop.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Aplicar distancia de etiqueta a partir del borde del símbolo
Cuando esta configuración está activa, la distancia de la etiqueta se aplica desde los límites del símbolo representado a un punto en lugar del punto en sí. Es especialmente útil cuando el tamaño del símbolo no es fijo, por ejemplo, si está establecido por un tamaño definido por datos o cuando se usan símbolos diferentes en una representación categorizada.

Note que esta configuración sólo está disponible con el nuevo modo Cartográfico de ubicación de etiqueta de punto.

![image54](images/entries/9469a985c317ec310e8506e27da5148cedbb93c0.png.400x300_q85_crop.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Control sobre el orden de representación de etiqueta
A new control for setting a label\'s \"z-index\" has been added to the labeling properties dialog. This control (which also accepts data-defined overrides for individual features) determines the order in which labels are rendered. Label layers with a higher z-index are rendered on top of labels from a layer with a lower z-index.

Además, la lógica se ha modificado de modo que si 2 etiquetas tienen índices z coincidentes, entonces:
- si son de la misma casa, una etiqueta más pequeña se dibujará siempre sobre la etiqueta más grande
- si son de capas diferentes, las etiquetas se dibujarán en el mismo orden que las capas en cuestión (es decir, respetando el orden establecido en la leyenda)

Los diagramas también pueden tener su conjunto de índices z (pero no datos definidos) para que se pueda controlar el orden de las etiquetas y los diagramas.

Tenga en cuenta que esto * NO * permite que las etiquetas se dibujen debajo de las entidades de otras capas, solo controla el orden en que se dibujan las etiquetas en la parte superior del mapa.

![image55](images/entries/52f3e941b047714fbaf81adc7a226e4808a82d09.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: El símbolo reproducido actual es ahora considerado un obstáculo para las etiquetas de elementos punto
Anteriormente, solo la característica de punto en sí misma se trataba como un obstáculo para los candidatos a la etiqueta. Si se utilizó un símbolo grande o desplazado para el punto, se permitió que las etiquetas se superpusieran a este símbolo sin incurrir en el valor del obstáculo.

Ahora, el tamaño real y el desplazamiento del símbolo representado se consideran al detectar si una etiqueta colisiona con una entidad de punto. El resultado es que QGIS ahora evita dibujar etiquetas sobre símbolos de puntos en más circunstancias.

![image56](images/entries/7d4d3117427f938ec3a5a4a1ed013e8e4445db60.png.400x300_q85_crop.webp)

Esta prestación fue financiada por la Ciudad de Uster

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
## Leyenda de capa
### Prestación: Pegar un estilo a múltiples capas seleccionadas o a todas las capas en un grupo de la leyenda
Esta prestación añade la posibilidad de pegar el estilo de una capa a un grupo de capas o capas seleccionadas.

![image57](images/entries/63fd1bfff18a108796c400edf127367f30f93c4b.png.400x300_q85_crop.webp)

Esta característica fue desarrollada por Salvatore Larosa
### Característica: Filtra leyenda por expresión
Ahora es posible filtrar elementos de la leyenda por una expresión. Se ha diseñado teniendo en cuenta el filtrado de la simbología categorizada o basada en reglas.

El filtro de leyenda está disponible en la leyenda de la aplicación principal, así como en los componentes de leyenda del compositor QGIS.

![image59](images/entries/8c957ae820bc98f0a23a7d660abd40264af6e31d.png.400x300_q85_crop.webp)

This feature was funded by [Agence de l\'Eau Adour-Garonne (Adour-Garonne Water Agency)](http://www.eau-adour-garonne.fr)

This feature was developed by [Hugo Mercier / Oslandia](http://oslandia.com)
## Compositor de Mapa
### Característica: Nuevas opciones para filtrar elementos de leyenda
Esto introduce dos nuevas opciones para filtrar elementos de la leyenda.

El primero, filtro por expresión, permite a los usuarios establecer una expresión para filtrar qué características deben mostrarse en la leyenda. Solo los símbolos con una función coincidente se mostrarán en la leyenda.

La segunda opción de filtro permite que una leyenda del compositor se filtre para incluir solo los elementos contenidos en el polígono de atlas actual.

![image58](images/entries/cf32cc889370df205de51af684c4e683c3ec2dc4.png.400x300_q85_crop.webp)

This feature was developed by [Hugo Mercier (Oslandia)](http://oslandia.com/)
### Característica: Rutas adicionales para plantillas del diseñador
You can now define custom paths that should be used for QGIS to find composer templates. This means that you can for example put a bunch of templates in a network share and give your users access to that folder in addition to the local ones that exist on their own system. To manage the composer template search paths, look in `Settings -> Options -> Composer`

![image60](images/entries/bd36891d76ee01ee79e516b0167f403a89fa49de.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Nathan Woodrow
### Característica: Selección múltiple de composiciones en el administrador
Composer Manager ha obtenido soporte para administrar múltiples composiciones al mismo tiempo. Ahora puede abrir o eliminar varias composiciones a la vez utilizando la tecla Ctrl y seleccionando varias composiciones de la lista.

![image61](images/entries/2603b37c6a6ccec10f56f37951d9494cb44c8d0a.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Plugins
### Característica: Soporte de istema de autentificación para el administrador de complemento
El soporte para el nuevo sistema de autenticación se ha agregado al administrador de complementos. Esto permite a los usuarios aplicar configuraciones de autenticación para las conexiones a los repositorios de complementos y a los administradores del sistema crear acceso autenticado a los repositorios de complementos y/o descargar paquetes de complementos.

![image62](images/entries/7b66e68eb37b27b0ecabcab7d0656985e222e8c0.png.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com)

Esta prestación fue desarrollada por Larry Shaffer
## Procesado
### Característica: Nuevos algoritmos en 2.14
#### Geoalgoritmos QGIS:
- Smooth: para suavizar capas línea o polígono.
- Revertir dirección de línea.

#### geoalgoritmos GDAL/OGR:
- gdal2tiles: construye un directorio con tejas TMS, KMLs y visores simples de web.
- gdal_retile: retiles a set of tiles and/or build tiled pyramid levels.

### Característica: Pruebas S/C de Unidad
Para garantizar la estabilidad de largo plazo del módulo de procesamiento, se ha introducido un nuevo marco de prueba.

Los geo-algoritmos de procesamiento se ejecutan después de cada cambio que llega al código fuente QGIS y el resultado se compara con un conjunto de datos de control para garantizar un comportamiento correcto. Esto proporciona una retroalimentación inmediata sobre posibles regresiones.

It is possible - and desired - that more tests are added. You can read more about [how to participate](https://www.opengis.ch/2016/02/04/increasing-the-stability-of-processing-algorithms/).

![image63](images/entries/4121e58bd51cfe5c8b2c0cd14d1420eaeb1f4473.png.400x300_q85_crop.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Característica: Caja de herramientas mejorada
Se ha eliminado la interfaz simplificada y se ha agregado un nuevo sistema de proveedores de gestión más fácil de usar. La funcionalidad de búsqueda de algoritmos ahora también busca en proveedores que no están activos, y sugiere activarlos.

![image64](images/entries/2a135d5384f592e77938c59c0563cc2d0f6c3ebf.jpg.400x300_q85_crop.webp)

This feature was funded by [Boundless Spatial](http://boundlessgeo.com/)

Esta característica fue desarrollada por Víctor Olaya
### Prestación: Los procesos por lotes se pueden guardar y luego recuperar desde la interfaz de procesamiento por lotes
![image65](images/entries/f8dec7fbc9e74dc3f4078f9710984d44b26c4fa3.jpg.400x300_q85_crop.webp)
### Característica: Diálogo de algoritmo más informativo
Ahora se muestra una breve descripción junto con los parámetros del algoritmo, lo que facilita la comprensión del propósito del algoritmo.

Also, batch processes can be now started from the algorithm dialog, using the "Run as batch process..." button

![image66](images/entries/c4039a87ddc906921e5e3ce47f8c7aadc7ab2263.jpg.400x300_q85_crop.webp)
### Característica: módulos v.net GRASS7
QGIS 2.14 Processing now incorporates v.net GRASS modules (only for GRASS7). Those modules are a set of algorithms that perform on graph line vector layers (networks). [A graph](https://en.wikipedia.org/wiki/Graph_theory#Graph) is a set of vertices (or nodes or points) linked together with a set of edges (or arcs or lines). The set of edges is often called a network.

Thanks to v.net modules, you can easily calculate the shortest path between a set of nodes on the network or even compute the [isochrone map](https://en.wikipedia.org/wiki/Isochrone_map) from a set of central points. you can also easily solve [the complex travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a network and a set of travel nodes.

Los algoritmos de v.net a menudo usan una capa de vector de línea (para la red) y una capa de puntos que representa los nodos que desea usar para el cálculo. Asegúrese de utilizar una capa de vector de línea de gráfico real para la capa de red (los bordes deben estar conectados en el vértice sin intersección entre los bordes) para evitar problemas. También puede usar cualquier atributo de capa de red para el cálculo de costos (el contenido del atributo se usa para calcular el costo de viaje del borde).

Aquí hay un resumen rápido de los diferentes algoritmos que se han incluido en el procesamiento:
- v.net.alloc: Asigna subredes desde los centros más cercanos.
- v.net.allpairs: Computa la ruta más corta entre todos los pares de nodos en la red.
- v.net.arcs: Crea arcos de un archivo de puntos.
- v.net.articulation: Computes the [articulation points](https://en.wikipedia.org/wiki/Biconnected_component) in the network.
- v.net.bridge: Computes [bridges](https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29) of the network.
- v.net.centrality: Calcula el grado, centralidad, intermediación, cercanía y centralidad de vector propio de cada nodo de la red.
- v.net.components: Computa componentes de la red conectados de manera fuerte o débil.
- v.net.connect: Conecta puntos (nodos) a los arcos más cercanos en la red (y adiciona bordes si es necesario).
- v.net.connectivity: Procesa la conectividad de vértices entre dos conjuntos de nodos de una red.
- v.net.distance: Calcula la ruta más corta mediante la red entre dos conjuntos de nodos.
- v.net.flow: Computa el flujo máximo entre dos conjuntos de nodos en la red.
- v.net.iso: Calcula el mapa isócrono de la red a partir de un conjunto de nodos.
- v.net.nodes: Extrae nodos de una capa red/gráfico.
- v.net.nreports: Reporta información acerca de los nodos.
- v.net.path: Encuentra la ruta más corta en la red entre dos nodos.
- v.net.report: Reporta información acerca de los bordes de la red.
- v.net.salesman: Computes the [travelling salesman path](https://en.wikipedia.org/wiki/Travelling_salesman_problem) from a set of nodes on the network.
- v.net.spanningtree: Computes the [Spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) of the network.
- v.net.steiner: Creates [a Steiner tree](https://en.wikipedia.org/wiki/Steiner_tree_problem) for the network and given nodes.
- v.net.visibility: Realiza construcción de gráficos de visibilidad.

Use the \"Help\" tab on each of the v.net Processing algorithm to read [the official GRASS7 documentation](https://grass.osgeo.org/grass70/manuals/topic_network.html) directly for more information.

![image67](images/entries/655bbfccc4997a5a3e3d1f5c709da5277eef6000.png.400x300_q85_crop.webp)

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Programabilidad
### Prestación: Rediseño del editor de función de expresión
Con auto guardar

![image68](images/entries/b42e959476310932713777f75f5eced4826df20a.png.400x300_q85_crop.webp)
### Característica: Almacenar el código init de python en el proyecto
Adds an option and code editor to store python form init code into the project (and the DB, since it\'s in the style section)

![image69](images/entries/67bad1306d40aa9b32b64f4d025b77649ae2f775.png.400x300_q85_crop.webp)
### Característica: Nuevas opciones de filtrado y ordenado para QgsFeatureRequest
QgsFeatureRequest ahora admite establecer un límite máximo para el número de entidades devueltas. En muchos casos, este límite se pasa al proveedor, lo que resulta en ganancias de rendimiento significativas cuando solo se requiere un número determinado de entidades.

Additionally, QgsFeatureRequest now supports setting ordering for returned features. Again, in many cases this ordering is delegated to the provider so that it is performed \"server side\" for optimal performance.

![image70](images/entries/6e136c8a4bdf4361b9307f88175369b62d4648d6.png.400x300_q85_crop.webp)
### Prestación: Opciones de código de Python de características personalizadas
Esta característica agrega más opciones al formulario de característica personalizada del código Python:
- carga desde archivo (con el widget seleccionador de archivo)
- carga desde el entorno (es decir, un complemento o una función de inicio de Python)
- ingresar el código directamente en el widget de entrada (nueva opción)

Las opciones de configuración, incluido el código personalizado de Python ingresado en el cuadro de diálogo, se almacenan en el proyecto y en la configuración QML de estilo y se pueden exportar/restaurar desde una base de datos.

![image71](images/entries/65e82ab529ee1287c631712127e1ac75f78d05c6.png.400x300_q85_crop.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.gov.it/)

This feature was developed by [Alessandro Pasotti (ItOpen)](http://www.itopen.it)
### Característica: Nuevas clases PyQGIS en 2.14
### Nuevas clases núcleo
- [QgsAttributeEditorElement](https://qgis.org/api/classQgsAttributeEditorElement.html)
  - abstract base class for any elements of a drag and drop form
- [QgsAttributeEditorContainer](https://qgis.org/api/classQgsAttributeEditorContainer.html)
  
  \- container for attribute editors, used to group them visually in an attribute form
- [QgsAttributeEditorField](https://qgis.org/api/classQgsAttributeEditorField.html)
  - element for loading a field\'s widget onto a form
- [QgsAttributeEditorRelation](https://qgis.org/api/classQgsAttributeEditorRelation.html)
  - element for loading a relation editor widget onto a form
- [QgsEditFormConfig](https://qgis.org/api/classQgsEditFormConfig.html)
  - stores and sets configuration parameters for attribute editor forms
- [QgsFeatureFilterProvider](https://qgis.org/api/classQgsFeatureFilterProvider.html)
  
  \- provides an interface for modifying a QgsFeatureRequest in place to apply additional filters to the request
- [QgsTracer](https://qgis.org/api/classQgsTracer.html) - provides graph creation and shortest path search for vector layers
- [QgsTransactionGroup](https://qgis.org/api/classQgsTransactionGroup.html)
  - interface for grouping layers into single edit transactions
- [QgsUnitTypes](https://qgis.org/api/classQgsUnitTypes.html) -helper functions for various unit types and conversions between units (eg distance and area units)
- [QgsVirtualLayerDefinition](https://qgis.org/api/classQgsVirtualLayerDefinition.html)
  - class for manipulating the definitions of virtual layers
- [QgsVirtualLayerDefinitionUtils](https://qgis.org/api/classQgsVirtualLayerDefinitionUtils.html)
  - helper utilities for working with QgsVirtualLayerDefinition objects
- [Qgs25DRenderer](https://qgis.org/api/classQgs25DRenderer.html) -2.5D symbol renderer
- [QgsGeometryGeneratorSymbolLayerV2](https://qgis.org/api/classQgsGeometryGeneratorSymbolLayerV2.html)
  - geometry generator symbol layer
- [QgsFeatureRequest.OrderByClause](https://qgis.org/api/classQgsFeatureRequest_1_1OrderByClause.html)
  - class for specifying a field sort order for feature requests
- [QgsFeatureRequest.OrderBy](https://qgis.org/api/classQgsFeatureRequest_1_1OrderBy.html)
  - a prioritized list of order by clauses for sorting

### Nuevas clases GUI
#### Widgets reutilizables:
- [QgsExternalResourceWidget](https://qgis.org/api/classQgsExternalResourceWidget.html)
  
  \- widget for displaying a file path with a push button for an \"open file\" dialog, and optional display of pictures or HTML files
- [QgsFileWidget](https://qgis.org/api/classQgsFileWidget.html) -widget for selecting a file or a folder
- [QgsLegendFilterButton](https://qgis.org/api/classQgsLegendFilterButton.html)
  
  \- tool button widget that allows enabling or disabling legend filter by contents of the map
- [QgsMapCanvasTracer](https://qgis.org/api/classQgsMapCanvasTracer.html)
  
  \- an extension of QgsTracer that provides extra functionality for interacting with map canvases
- [Qgs25DRendererWidget](https://qgis.org/api/classQgs25DRendererWidget.html)
  - widget for setting properties for a 2.5D renderer
- [QgsColorWidgetAction](https://qgis.org/api/classQgsColorWidgetAction.html)
  - widget action for embedding a color picker inside a menu

#### Diálogos reutilizables:
- [QgsStyleV2GroupSelectionDialog](https://qgis.org/api/classQgsStyleV2GroupSelectionDialog.html)
  - dialog for grouping selections in a style
- [QgsGroupWMSDataDialog](https://qgis.org/api/classQgsGroupWMSDataDialog.html)
  - dialog for setting properties for a WMS group
- [QgsOrderByDialog](https://qgis.org/api/classQgsOrderByDialog.html)
  - dialog for specifying sort ordering of fields

## Servidor de QGIS
### Característica: parámetro STARTINDEX en Pedido WFS GetFeature
`` `STARTINDEX `` is standard in WFS 2.0, but it\'s an extension for WFS 1.0 implemented in QGIS Server.

`STARTINDEX` can be used to skip some features in the result set and in combination with `MAXFEATURES` provides for the ability to use WFS GetFeature to page through results. Note that `STARTINDEX=0` means start with the first feature, skipping none.

This feature was developed by [3Liz](http://3liz.com)
### Característica: showFeatureCount en GetLegendGraphic
Add non-standard parameter **showFeatureCount** to add feature count in the legend. To activate it,**showFeatureCount** can be set to *TRUE* or *1*.

Esta característica necesita un servidor X falso.

![image72](images/entries/95f13aa3a1f4cb4ca8cbf7ce30e6bb278e6b9cd8.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Prestación: Opción para evitar renderizar artefactos en los bordes de las teselas
![image73](images/entries/1ded32aa2bb962fde1b9f00b891b2a04406be621.png.400x300_q85_crop.webp)
### Característica: Revisor de configuración en propiedades del proyecto
Para ayudar a configurar un proyecto para QGIS Server, se ha agregado un nuevo verificador de configuración a las propiedades del proyecto.

Los test de prueba de errores como:
- nombres duplicados o cortos usados como nombres OWS
- nombres OWS no válidos
- codificación faltante de capa vector

![image74](images/entries/c548fc562785f400d3000e7ae1f61705c333026c.png.400x300_q85_crop.webp)

This feature was funded by [Ifremer](http://wwz.ifremer.fr/institut_eng/)

This feature was developed by [3Liz](http://3liz.com)
### Característica: Capacidades WMS INSPIRE
En las propiedades del proyecto, el usuario puede:
- activa capacidades INSPIRE
- seleccione el idioma para el servicio, de 24 idiomas oficiales UE + 5 idiomas regionales
- Elija el escenario para el servicio de metadatos y especifique sus parámetros

Las capacidades WMS 1.3.0 reflejan la configuración INSPIRE.

![image75](images/entries/4ee445bcb5e9eab3fb9bf2eda8f9b1b81bbe21c0.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
### Característica: Adiciona nombre corto a capas, grupos y proyecto
Varios elementos tienen un **Nombre** y un **Título**. El Nombre es una cadena de texto utilizada para la comunicación de máquina a máquina, mientras que el Título es para el beneficio de los humanos. Por ejemplo, un conjunto de datos podría tener el Título descriptivo *Temperatura atmosférica máxima* y solicitarse utilizando el Nombre abreviado *ATMAX*.

Los usuarios ya pueden establecer un título para capas y proyectos. OpenGeospatial Web Services, OWS (WMS, WFS, WCS), el nombre se basa en el nombre utilizado en el árbol de capas. Este nombre es más una etiqueta para humanos que un nombre para la comunicación de máquina a máquina.

Para agregar la capacidad para que los usuarios definan Nombre como una cadena de texto para la comunicación de máquina a máquina, esta prestación añade:
- ediciones de línea de nombre corto a propiedades de capa
- WMS diálogo de datos al árbol de grupos de capas(nombre corto, título, resumen)
- ediciones de línea de nombre corto a las propiedades del proyecto
- add a regexp validator \"\^\[A-Za-z\]\[A-Za-z0-9.\_-\]\*\" to short name line edit accessible through a static method
- adicionar un elemento TreeName en el fullProjectSettings

Si se ha establecido un nombre corto para capas, grupos y proyectos, QGIS Sever lo utilizará como nombre de capa.

![image76](images/entries/e2345455bda9f0ed3da5e1c2750d6e2239ab8a86.png.400x300_q85_crop.webp)

This feature was developed by [3Liz](http://3liz.com)
## Simbología
### Prestación: asistente de tamaño para variar el grosor de línea
![image77](images/entries/1d891425b0e1b9927ced6aab3e0353aed92608de.png.400x300_q85_crop.webp)
### Característica: Soporte de transparencia en parámetros de color SVG
SVG no agrupados se deben añadir:

`fill-opacity="param(fill-opacity)"`

y

`stroke-opacity="param(outline-opacity)"`

para permitir soporte de transparencia.

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Duplicación fácil de capas de símbolo
A new \"duplicate\" button has been added to the symbol properties dialog, which allows symbol layers to be easily duplicated.

![image78](images/entries/a6e2ad682852a2fb8b635395ec75f83ef584621d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Característica: Representador 2,5D
Esto añade una interfaz de configuración y renderizador que hace mas fácil unir todas las piezas requeridas para obtener un efecto 2.5D.

Permite configurar algunos estilos y está destinado a crear una configuración fácil de usar.

Since every part of the system is built around QGIS\' internal rendering and symbology engine, there is much to fine tune. To get all the possibilities, just change the renderer to a graduated, categorized or single symbol renderer upon creation and you will find full access to improve the style to your needs.

**Esta característica fue desarrollada por**:
- Matthias Kuhn at [OPENGIS.ch](https://opengis.ch)

**Esta característica fue financiada por**:
- Consejo Regional de Picardía
- ADUGA
- Ville de Nyon
- Wetu GIT cc

![image79](images/entries/8d66f8838011e7bc8fae540d56bf9ef6db20db68.jpg.400x300_q85_crop.webp)
### Característica: Permite la definición del orden de representación para los elementos
Cuando se requiere que las características se representen en un orden particular, esto puede especificarse mediante el uso de una expresión arbitraria.

This can be configured in the layer\'s symbology configuration dialog and can be a simple field or a complex expression.

También proporciona control sobre orden ascendente o descendente así como si los NULL son primeros o últimos.

Si es posible, la solicitud se enviará a la base de datos (esto depende de la complejidad de la expresión y del proveedor de la capa). Si no es posible enviar la solicitud a la base de datos, el pedido se realizará en la máquina local.

This is used by the 2.5D renderer to render features based on their distance from the \"camera\".

Esto está también disponible para complementos:

    layer.getFeatures( QgsFeatureRequest().setOrderBy( 'name' ) ) -- alphabetical by name
    
**This feature was developed by**: Matthias Kuhn at [OPENGIS.ch](https://opengis.ch) **This feature was funded by**: Regional Council of Picardy, ADUGA, Ville de Nyon, Wetu GIT cc

![image80](images/entries/e06cf21a35e070a28ce5b3b98c92f2fb1c1b881d.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Prestación: Generador de símbolos de geometría.
El Generador de símbolos de geometría permite usar el motor de expresión para modificar la geometría antes del renderizado o incluso crear nuevas geometrías mientras representamos basándonos en atributos de entidad.

Esto puede usar todo tipo de operadores espaciales como el búfer, la traducción, la intersección o la extrusión con parámetros basados en atributos solo para la representación sin modificar realmente los datos en la fuente.
### Ejemplos
#### Traducir una geometría
Utilizado para la cubierta del renderizador 2.5D

    translate( $geometry, 10, 10 )
    
#### Estilo de llenadao para borde de polígono
Esto genera un polígono que representa la frontera del polígono original (Ejemplo de la imagen)

    difference( buffer( $geometry , 250 ), buffer( $geometry, -250 ) )
    
Capas de diferentes símbolos pueden contener diferentes generadores de geometrías, esto permite mostrar diferentes versiones de una geometría al mismo tiempo. El renderizador 2.5D sirve de ejemplo.

![image81](images/entries/b06b6bc93644c051c13de162b45d9486b7af769a.png.400x300_q85_crop.webp)

Esta característica fue financiada por el Consejo Regional de Picardía, ADUGA, Ville de Nyon, Wetu GIT cc

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
## Interfaz de usuario
### Característica: La tabla de atributo puede ser actualizada
Ahora está disponible una opción para recargar atributos dentro de la tabla de atributos.

![image82](images/entries/4623399cb1f63e2c6fa80c72a6aea17b6c63bb3e.png.400x300_q85_crop.webp)
### Prestación: establece directamente la representación y los colores del símbolo de clase desde el menú contextual en la leyenda
Muestra un widget de rueda de color en el menu, el cuál le permite editar el color de un símbolo interactivamente, ¡sin tener que abrir tan siquiera un sólo diálogo!

![image83](images/entries/3159457a414ea61f8f40659af5c9561882a44fe1.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Prestación: Editar símbolos de leyenda diréctamente desde el árbol de capas.
This adds a new \"edit symbol\" item to the right-click menu for a renderer child legend item (eg categories for the categorised renderer). Selecting it opens a symbol editor dialog which allows for directly editing the class\'s symbol. It\'s much faster than opening the layer properties and going through the style tab. You can also double-click on a child item to open the symbol editor immediately.

![image84](images/entries/e7b2447e329507f0b27e855111ffa038b1ccc353.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)
### Prestación: Mostrar/Esconder todos los elementos de la leyenda mediante el menú contextual
Allows toggling on/off all the symbol items for categorized/graduated/rule-based layers via the right click menu on an item. Previously you\'d have to toggle each item manually one-by-one.

![image85](images/entries/c526cf9c28c92dde193490a2707c1fe2e0a58ea6.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson](http://nyalldawson.net)

{{<content-end >}}
