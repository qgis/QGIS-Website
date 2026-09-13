---
HasBanner: false
draft: false
releaseDate: '2016-10-21'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.18
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.18{#changelog218 }
![image1](images/projects/ac3b0a08203e87505a823b0d8a0895d44489f916.png)

Fecha de lanzamiento: 2016-10-21

Esta es la última versión de la serie 2.x. La versión actual a largo plazo (LTR) sigue siendo la versión 2.14.x. Esta versión proporciona mejoras incrementales sobre nuestra versión anterior. La mayor parte de la actividad se centra actualmente en el desarrollo de QGIS 3.0, que es nuestra versión de próxima generación prevista para finales del primer trimestre de 2017.

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Patrocinadores de QGIS versión 2.18.0
Anualmente, también recibimos apoyo de varias organizaciones que aprecian el trabajo que hacemos y nos gustaría facilitar el esfuerzo de desarrollo sostenido que implica el proyecto. Estos patrocinadores se enumeran a continuación con nuestro agradecimiento.

{{<fund type="changelog" relativeImgPath=true >}}
## General
### Prestación: Enlaces automáticos en identificar resultados
Any `http` or `mailto` links within attribute values will now automatically be converted to clickable links within the identify results panel.

![image58](images/entries/eab95eb0acb92a68edeee71a13ea23d77b88d307.png.400x300_q85_crop.webp)

This feature was developed by [Sandro Mani (Sourcepole)](https://sourcepole.ch/)
### Prestación: Rueda del mouse sobre controles deslizantes del diálogo de color
En QGIS 2.18 ahora puede desplazar la rueda del mouse sobre cualquiera de los controles deslizantes dentro del cuadro de diálogo del selector de color para incrementar el valor en pequeñas cantidades. Este es un atajo útil para pequeños ajustes en los componentes de color.

![image59](images/entries/ab472e2c8270ba64bee64bbbf8c9f5104edc79de.gif)

This feature was funded by [Nyall Dawson (North Road)](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Agregue esquemas de color personalizados al menú desplegable del botón de color
QGIS 2.18 adds the ability for users to set whether a user created color scheme should show up in the color button drop-down menus. This setting is controlled through the color picker dialog, on the lists tab. Just add a new color scheme, then from the scheme menu tick the new \"show in buttons\" option. It\'s a handy shortcut if you have sets of common palettes and want them to be instantly available through the color menu.

![image60](images/entries/9453954d199c4950d7aecf153b6d5e53f820ff19.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Simbología
### Prestación: el selector de color ahora está incrustado en el panel de estilo de capa
En QGIS 2.18, al hacer clic en un botón de color dentro del panel de estilo de capa, se abre el cuadro de diálogo del selector de color dentro del panel de estilo en lugar de hacerlo como un cuadro de diálogo separado. Esto permite la modificación interactiva de colores con una vista previa inmediata del resultado.

![image42](images/entries/3af7533f5148810d0c26a221d7acdccaf1d7a835.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Etiquetando
### Prestación: Soporte de lista de sustitución para etiquetado
Agrega la capacidad de especificar una lista de sustitutos de texto para hacer que se apliquen al texto de la etiqueta. Por ejemplo, abreviando tipos de calles.

Los usuarios pueden exportar e importar listas de sustitutos para facilitar la reutilización y el intercambio.

![image43](images/entries/a73aec5fad4c5e39800e462bbac6dd2597f98cba.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Algoritmo de colocación de etiquetas de línea mejorado
El modo de etiquetado paralelo para capas de línea se ha mejorado considerablemente, con un nuevo algoritmo que evita colocar etiquetas sobre partes irregulares de las geometrías de entidades.

![image44](images/entries/5b77d12263e0dabfb0649f27d92188613796f409.png.400x300_q85_crop.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: etiquetar polígonos usando etiquetas curvas a lo largo del perímetro
Esto agrega un nuevo modo para etiquetar polígonos donde el perímetro del polígono se etiqueta usando etiquetado curvo.

![image45](images/entries/c7a28cf09a0f1646210faaae85a56c2209ee15e9.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Representación
### Prestación: Vista previa de mosaicos ráster (capas WMTS y XYZ)
En versiones anteriores de QGIS, los usuarios tenían que esperar hasta que finalizara la descarga de todos los mosaicos de una capa para ver el mapa resultante. Esto ahora se ha solucionado y los mosaicos se muestran en el lienzo del mapa inmediatamente a medida que se descargan, lo que mejora la experiencia del usuario al reducir considerablemente el tiempo hasta que se muestra algo. Además, los mosaicos descargados previamente de resoluciones más bajas o más altas pueden usarse para la funcionalidad de vista previa en las áreas donde los mosaicos con la resolución correcta aún no se han descargado.

![image46](images/entries/007bf6d09a1f67e0c0c4ee71d48081185c0c5c84.gif)

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
### Prestación: representación cancelable de rásteres (capas WMS, WMTS, WCS y XYZ)
Esta realce mejora la experiencia del usuario cuando se trabaja con capas ráster que provienen de servidores remotos. Anteriormente, habría que esperar hasta que las descargas se hayan completado por completo para poder hacer zoom o desplazar el mapa nuevamente, porque la interfaz de usuario permanecería congelada mientras tanto. Esto se soluciona ahora por el hecho de que la representación de las capas ráster se puede cancelar en cualquier momento.

This feature was funded by [Land Information New Zealand](http://www.linz.govt.nz/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Administración de datos
### Prestación: agregue una bandera para copiar solo las características seleccionadas
Los complementos de edición sin conexión son complementos predeterminados que se proporcionan con QGIS y le permite desconectar un conjunto de datos remoto (por ejemplo, desde una base de datos), editarlo en el campo y luego resincronizarlo cuando regrese a su oficina. Esto extiende las posibilidades de edición fuera de línea para trabajar solo en subconjuntos de capas grandes.

![image47](images/entries/ec977674f356d5376d19be49534818a4cc830c64.png.400x300_q85_crop.webp)

Esta prestación fue fundada por DB Fahrwegdienste GmbH

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
## Widgets y Formularios
### Característica: Permitir controlar etiquetas para widgets de edición individual
Permite el control de etiquetas para widgets de edición individuales en un formulario. En el diseñador de arrastrar y soltar, un doble clic en un elemento permitirá controlar si la etiqueta debe mostrarse para cada elemento individualmente.

In addition it is possible to configure if the link/unlink buttons are shown in relation reference widget, which is useful to hide in 1:n relations where a child can\'t exist without its parents.

![image48](images/entries/6d827c6b286f137ec9de1d97a15c745764494d0a.png.400x300_q85_crop.webp)

This feature was funded by [Kanton Zug, GIS-Fachstelle](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Prestación: visibilidad condicional para pestañas y cuadros de grupo
Esto agrega una nueva opción de configuración para mostrar u ocultar condicionalmente pestañas y cuadros de grupo en formularios de diseñador de arrastrar y soltar.

La configuración se realiza mediante un doble clic en el árbol del diseñador en la interfaz de configuración de campos.

Se puede ingresar una expresión para controlar la visibilidad. La expresión se volverá a evaluar cada vez que los valores en el formulario cambien y la pestaña o el cuadro de grupo se muestra/oculta en consecuencia.

![image49](images/entries/8adda1d639ba9b46b15f8a70b38c6cfd407d2515.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Prestación: valores de campo predeterminados del lado del cliente
Allows an expression to be set for a vector layer field which is used to evaluate a default value for this field. Default value expressions can utilise properties of the feature which exist at the time of calling, such as digitized geometries. Expression variables can also be used in default value expressions, making it easy to eg insert a user\'s name, the current datetime, project path, etc.

![image50](images/entries/49a9d8a5c38f04d96cf37ad190a97dd4dc4b5025.png.400x300_q85_crop.webp)

Esta prestación fue fundada por DB Fahrwegdienste GmbH

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Compositor de Mapa
### Prestación: Flechas de Norte verdaderas
QGIS 2.18 adds support for orienting north arrows in the composer to True North. Previously all arrows were aligned to grid north, which is unsuitable for polar regions or non-north up projections (such as some South African projection systems). Now, you can choose to orient arrows to either grid north or true north. There\'s also an optional offset angle, which can be used to specify a grid convergence to make your arrows orient to magnetic north!

![image51](images/entries/b36b83066c2361e4a9647ee830b55b01a04ce4c5.png.400x300_q85_crop.webp)

This feature was funded by [Norwegian Polar Institute\'s Quantarctica project](http://quantarctica.npolar.no)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Procesado
### Prestación: algoritmo de punto en superficie
This new algorithm is similar to the centroids algorithm, but where a centroid may fall outside its corresponding feature the \'Point on surface\' algorithm is guaranteed to create a point which is inside the corresponding polygon feature (or touching the corresponding line feature for line layers).

![image52](images/entries/133a854441e2ade7bec91a48e9a1f1d4b1d012ac.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: el algoritmo de procesamiento de disolución acepta múltiples campos
El algoritmo de disolución ahora le permite disolver en función de más de un valor de campo. En versiones anteriores de QGIS, una disolución solo podía agrupar entidades por un solo valor de campo.

![image53](images/entries/a75b372f431c98592bdaccbc0bf4e90654969fa2.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: algoritmo de clip de procesamiento optimizado
El algoritmo de recorte de procesamiento se ha optimizado para escenarios de uso común, lo que resulta en aceleraciones dramáticas para las operaciones de anclado. Por ejemplo:

** Recortando una capa de carreteras con 1 millón de líneas contra 2 polígonos **

| **Earlier versions:** 5 mins 30 seconds | **QGIS 2.18:** 10 seconds

** Recortando una capa de dirección de 5 millones de puntos a 2 polígonos **

| **Earlier versions:** 50 minutes | **QGIS 2.18:** 30 seconds

![image54](images/entries/f975cb641b319e952264dc1e706deafdfd2b7496.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: algoritmo de cajas delimitadoras
Este nuevo algoritmo calcula el cuadro delimitador (envolvente) de cada entidad en la capa de entrada.

![image55](images/entries/398557f0cfe897a227fea70ceef700f9ab048e2d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: algoritmo de mezclado de lineas conectadas
Este algoritmo une todas las partes conectadas de las geometrías MultiLineString en geometrías LineString individuales. Si alguna parte de las geometrías MultiLineString de entrada no está conectada, la geometría resultante será una MultiLineString que contiene las líneas que podrían fusionarse y las partes de la línea no conectadas.

![image56](images/entries/7ebf10a71a1c3f28d48a2c19f7ad1f08ca75bf80.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: algoritmo de límite de geometría
Este nuevo algoritmo devuelve el cierre del límite combinatorio de las geometrías de entrada (es decir, el límite topológico de la geometría). Por ejemplo, una geometría de polígono tendrá un límite que consiste en las cadenas de líneas para cada anillo en el polígono, y una geometría de línea tendrá un límite que consiste en los puntos inicial y final de la línea. Este algoritmo solo es válido para capas de polígonos o líneas.

![image57](images/entries/907b7b5c36af36547f10f33f65e9655a5cbe5a67.png.400x300_q85_crop.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Proveedores de datos
### Prestación: soporte nativo de capas de mosaico XYZ
Los mosaicos ráster en formato XYZ ahora son compatibles de forma nativa con los proveedores de datos WMS, lo que permite a los usuarios mostrar mapas base de otras fuentes sin necesidad de complementos de terceros como QuickMapServices o OpenLayers.

To add connections to XYZ layers, just open browser dock widget, look for item called \"Tile Server (XYZ)\" and right click it to get a popup menu with \"New connection\" action. You will be asked for URL, in which `{x}`, `{y}`, `{z}` will be replaced by the actual tile numbers according to the current map view. For example, to add OpenStreetMap base map, one may use this URL: `http://c.tile.openstreetmap.org/{z}/{x}/{y}.png`

The data provider also supports encoding of XYZ tile numbers into \"quadkeys\" used by Bing. Simply use `{q}` instead of `{x}`, `{y}` and `{z}` in the URL.

![image61](images/entries/f69a3601e9201e38f9a561d40807512035da2298.gif)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](http://www.lutraconsulting.co.uk/)
## Servidor de QGIS
### Prestación: Posibilidad de segmentar información de geometría en el servidor
Necessary for geometries that contain curves (CircularArc, CompoundCurve, CurvePolygon), but the web client (e.g. QGIS Web Client) can\'t handle the display of these geometry types.

This feature can be enabled in the \"OWS server\" tab in the \"Project Properties\" dialogue.

![image62](images/entries/f4b9cf3ba10669b933eb3f3a5c401f675ad76533.png.400x300_q85_crop.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Marco Hugentobler (Sourcepole)](http://www.sourcepole.ch/)
## Plugins
### Prestación: Administrador de base de datos: agregar la capacidad de actualizar la capa SQL
With this feature the user can update the layer datasource if it\'s based on an SQL request.

This feature was funded by [Ifremer](http://wwz.ifremer.fr)

This feature was developed by [3Liz](http://3liz.com)
## Programabilidad
### Prestación: Exponer la función de referencia lineal GEOS a QgsGeometry
A new function `QgsGeometry::lineLocatePoint()` has been added for retrieving the distance along a linestring to the nearest position on the linestring to a given point.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Característica: Nuevas clases PyQGIS en 2.18
### Nuevas clases núcleo
- [QgsAnnotation](https://qgis.org/api/classQgsAnnotation.html) - an interface for annotation items which are drawn over a map
- [QgsFeedback](https://qgis.org/api/classQgsFeedback.html) - a base class for feedback objects to be used for cancellation of something running in a worker thread
- [QgsOptionalExpression](https://qgis.org/api/classQgsOptionalExpression.html) - an expression with an additional enabled flag

### Nuevas clases IGU, Widgets reutilizables
- [QgsExpressionLineEdit](https://qgis.org/api/classQgsExpressionLineEdit.html) - includes a line edit for entering expressions together with a button to open the expression creation dialog. This widget is designed for use in contexts where no layer fields are available for use in an expression and space is constrained.
- [QgsTabWidget](https://qgis.org/api/classQgsTabWidget.html) - similar to QTabWidget but with additional methods to temporarily hide/show tabs

## Prestación: Nuevas funciones de expresión
QGIS 2.18 agrega varias funciones de expresión nuevas, incluidas funciones para la interpolación de ángulo/distancia.
- `line_merge`: merges a MultiLineString geometry into connected LineStrings
- `boundary`: returns a geometry\'s topological boundary, ie for polygons this is a MultiLineString representing the polygon\'s rings
- `angle_at_vertex`: returns the average (bisector) angle to a geometry at a specified vertex index
- `distance_to_vertex`: returns distance along geometry to a specified vertex index
- `line_interpolate_angle`: calculates the angle parallel to a geometry at the specified distance along the geometry
- `line_interpolate_point`: returns a point on line at distance
- `line_locate_point`: returns distance along line to nearest line location closest to specified point

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)

{{<content-end >}}
