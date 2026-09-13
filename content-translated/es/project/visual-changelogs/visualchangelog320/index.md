---
HasBanner: false
draft: false
releaseDate: '2021-06-18'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.20
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.20{#changelog320 }
![image1](images/projects/712c5f48a25ce79a413e9cc34336e05100b7f0c1.png)

Fecha de lanzamiento: 2021-06-18

QGIS 3.20 Odense features a splash screen which displays a section of [the earliest map](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object80440/en/) of Denmark's third largest city, [Odense](https://en.wikipedia.org/wiki/Odense) from 1593. The map was published by [Georg Braun](https://en.wikipedia.org/wiki/Georg_Braun) (1541-1622) in the work *Civitates orbis terrarum* (Cities of the World). Georg Braun's maps are all beautiful and were, for the period, produced at a high cartographic level. *Civitates orbis terrarum* was long the main source of maps of the world's cities, such as [Paris](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62269/en/), [London](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62684/en/), [Mexico City](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62261/en/) and [Aden](http://www5.kb.dk/maps/kortsa/2012/jul/kortatlas/object62257/en/).

The name Odense literally means "Odin's temple", and the place may have originally been a shrine to the pagan god Odin. At the bottom left of the map you see the ruins of one of the large Viking-Age ring-shaped fortress, which were constructed in Denmark by the Danish Viking king [Harald Bluetooth](https://en.wikipedia.org/wiki/Harald_Bluetooth) (died c. 985/86). The ring fortress in Odense is called [Nonnebakken](https://odensebysmuseer.dk/nonnebakken-the-viking-ring-fortress-in-time-and-space/?lang=en).

Esta versión introduce una serie de cambios sutiles y actualizaciones de estabilidad, reforzando el amplio catálogo de características de vanguardia introducidas en las últimas versiones de QGIS. En esta versión se incluyen numerosas mejoras en la gestión de datos, con algunos cambios avanzados en la gestión y visualización de sistemas SRC e información de proyección. Entre estas mejoras en la gestión de SRC se encuentra el soporte básico para la época de coordenadas de los sistemas SRC dinámicos y las advertencias avanzadas de integridad de la precisión, colocando a QGIS 3.20 firmemente en la vanguardia de los SIG y de las prácticas de gestión de datos para sistemas de alta precisión.

Additionally, users can expect improved metadata management and handling for certain data and metadata types. Another key highlight is the native integration of the [nominatim](https://nominatim.org/) geocoding service, which will allow users to search locations and addresses using data from the OpenStreetMap project directly from the QGIS locator bar.

The QGIS Community has also seen an uptick in activity in the [QGIS HUB](https://plugins.qgis.org/), as well as the Virtual QGIS Open Days, with the [Cutting Edge Open Day](https://github.com/qgis/qgis/wiki/QHF-May-2021) showcasing a number of demonstrations which leverage rich QGIS functionality that was introduced in more recent releases.

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## General
### Prestación: Opciones adicionales para abrir tabla de atributos
Los atajos disponibles anteriormente para abrir tablas de atributos, utilizar filtros para mostrar sólo los elementos seleccionados o los elementos visibles dentro del lienzo, se han integrado en la barra de herramientas del menú para facilitar su uso y mejorar la experiencia del usuario, especialmente cuando se trabaja con grandes conjuntos de datos.

![image2](images/entries/571fda8da2dc36cc6032354e4249ac9f642aad02.webp)

This feature was developed by [Raymond Nijssen](https://github.com/raymondnijssen)
### Prestación: Definir tamaño para todas las columnas en la tabla de atributos
The existing ability to \"Set Width\" and \"Autosize\" for columns has been extended to apply the resizing of a field to all columns.

This includes the ability to set a fixed width or to \"Autosize\" all columns. These actions are available from the attribute table header context menu which is accessible by right-clicking a field header.

![image3](images/entries/424dea8c61279f20c7f3ca5bf3cd13c21f999987.webp)

This feature was developed by [Ben Wirf](https://github.com/benwirf)
### Prestación: Facilitada la exportación/importación de configuraciones de autenticación
Starting with QGIS 3.20, users can now easily export and import authentication configurations via a pair of actions in QGIS settings\' authentication panel. Exported configurations can be password-protected to avoid sensitive information leakage.

Esto facilita enormemente el compartir varias configuraciones de autenticación entre múltiples usuarios de QGIS, especialmente cuando se trata de métodos de configuración más complejos como oauth2.

This feature was funded by Ville d\'Yverdon-les-Bains

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Temporal
### Prestación: Pasos de navegación temporal
A temporal navigation step option for \"source timestamps\" has been added to the temporal controller. When selected, this causes the temporal navigation to step between all available time ranges from layers in the project. It\'s useful when a project contains layers with non-contiguous available times, such as a WMS-T service which provides images that are available at irregular dates. This option will allow users to only step between time ranges where the next available image is shown.

![image4](images/entries/09959743079b809c8969b49f5fbbffe774aeb644.gif)

Esta prestación fue financiada por Natural resources Canada Contrato: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Definiciones WMS-T mejoradas
Se han simplificado los ajustes de WMS-T y se han introducido controles para facilitar la selección de la hora deseada por algunos proveedores.

Se hicieron cambios para poder alcanzar los siguientes resultados:
- Hacer más claro exactamente que controla cada una de las configuraciones
- Hacer más clara la interacción y asociaciones entre varias configuraciones
- Hacer obvio qué ajustes se aplican, independientemente de si la capa está controlada por el controlador temporal o si los ajustes se refieren sólo a las capas estáticas de WMS-T
- Para los servidores que exponen un conjunto no contiguo de instancias de fecha-hora, en lugar de un rango de fechas, se proporciona un cuadro combinado que elimina la necesidad de introducir manualmente las fechas válidas

Ejemplo de configuraciones con un servidor que expone un rango de fechas disponibles:

![available](images/entries/5959d2a149797fdbd8108653dad86b4ba93d54a1.gif)

Ejemplo de configuración con un servidor que expone una lista de instancias datetime disponibles únicamente:

![datetime](images/entries/f8d2510c5cdf7241f1ed61a9bdd0211f1d6fb0f7.gif)

![image7](images/entries/f8ab8c722dde210f851f838752916bfe76147420.webp)

Esta prestación fue financiada por Natural resources Canada Contrato: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Navegación temporal con la rueda horizontal del ratón
Horizontal scrolling using the mouse wheel (where supported) with the cursor on the map canvas will allow users to navigate, or \"scrub\", the temporal navigation slider backwards and forwards

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Herramientas de mapa
### Prestación: Integración Geocodificador Nominatim
The Nominatim Geocoder is now natively integrated into QGIS out of the box! QGIS provides a Nominatim locator filter, as well as the \"Batch Nominatim Geocoder\" processing tool for batch geocoding locations.

*filtro localizador Nominatim*

The QGIS locator bar widget (by default, a search bar in the bottom left corner CTRL+K) now supports Nominatim geocode searches by using the prefix \'\>\'.

Users may now search for locations using the format `> search string` in the locator and will be provided with a selection of results. Selecting a search result will reposition the canvas extent on that location.

*Geocodificador por lotes Nominatim*

In addition, a new \"Batch Nominatim Geocoder\" algorithm has been added to the QGIS processing toolbox under Vector tools, allowing users to geocode multiple locations at once.

Nominatim es un servicio de geocodificación que utiliza datos del proyecto OpenStreetMap. Se aplican limitaciones de uso y límites de velocidad - 1 consulta por segundo - de acuerdo con las políticas de uso de la Fundación OpenStreetMap (OSMF), y los datos se proporcionan bajo los términos de la licencia ODbl. Además, las consultas al servicio Nominatim pueden incluir información de telemetría.

El envío de este gran servicio de geocodificador por defecto no habría sido posible sin la generosidad y participación de al FOSM.

![image8](images/entries/bd1b0900b9e2b2756dbc9c9aa90f8b8f34ef166e.gif)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Interfaz de usuario
### Prestación: Mejoras en diálogo de procesado de historia
The processing\'s history dialog has had a series of user interface improvements, including regrouping of algorithms in meaningful folder structures and making use of individual algorithm icons. Searching for that algorithm you ran last week has never been as easy!

![image9](images/entries/4e8fa82827363fa9b82ed5b79c1b84f12a220465.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Iconos de capa de mapa en el diálogo del constructor de expresión
The expression builder dialog now displays map layer icons next to the list of layers under the \'Map Layers\' parent group. This speeds up skipping through the list and provides additional context.

![image10](images/entries/2128b48e7c773959e0305181db1b4da9c917889d.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: filtrado del explorador SVG
La interfaz del navegador de SVG admite ahora un sencillo filtrado basado en texto, que permite a los usuarios filtrar las imágenes SVG disponibles en función de una cadena de búsqueda determinada.

![image11](images/entries/3e4dfa0a3e25db1821ae914eeec5c34d7c125ebf.gif)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
## Simbología
### Prestación: Tipo de capa de símbolo de línea interpolada para capas vectoriales
QGIS provides a new \"Interpolated Line\" symbol layer type, which results in the rendering of a color and/ or width varying line.

Este símbolo es altamente configurable y permite a los usuarios asociar atributos o expresiones a cada extremidad de la línea o curva, entre otras opciones de configuración. Los valores se interpolan a lo largo de la cadena de líneas entre las extremidades. El color se configura con un widget de sombreado de rampa de color.

![image12](images/entries/ebfd1d989cdb0d61ab56ab5a629a82a716446666.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Prestación: Recortar el símbolo línea simple
Se ha añadido una opción para recortar el inicio y el final de los símbolos de línea simples, lo que permite que la representación de la línea recorte la primera y la última sección de una línea a una distancia configurada por el usuario. Resulta útil para crear símbolos complejos en los que una capa de línea no debe superponerse a las capas de símbolos de marcador colocadas en las posiciones de inicio o final de una característica de línea, como en el caso de las rutas de transporte. La distancia de recorte admite una serie de unidades, incluido un porcentaje de la longitud total de la línea, y también puede configurarse como una propiedad definida por los datos.

Una galería de muestra de esta prestación en uso:

![image13](images/entries/f0cad8bbc2de6c44b22c4875c45ed6e24e9f4bf6.webp)

![image14](images/entries/14f48f5bcc891d1c97a8b187f53bb21c6dd6dff6.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New \"Embedded styling\" renderer with OGR feature styles support
A new \"Embedded styling\" renderer has been added which exposes OGR feature styles, allowing QGIS to automatically symbolize data from certain datatypes which have integrated style information, such as KML or TAB files.

This feature implements [QEP-209](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/209)

La compatibilidad debería extenderse automáticamente a todos los controladores GDAL que implementen la API de estilo de características OGR.

Actualmente sólo admite la conversión de símbolos de líneas, pero el soporte de símbolos de puntos y polígonos está en desarrollo.

![image15](images/entries/44767fa890705c09d9c4b21b998807c7999ddde4.gif)

Esta funcionalidad también admite la conversión directa de representadores de símbolos incrustados en representadores categorizados o basados en reglas. Esto permite a QGIS crear automáticamente categorías o reglas que definen la simbología basándose en los ID de características relevantes:

![image16](images/entries/3a408fbcff1ee8d5889c3fe30c0d9d831b050698.gif)

![image17](images/entries/be73e288ed1f46860868a6ae49e7d1f8604082b9.webp)

Esta prestación fue financiada por el grupo de usuarios QGIS Dinamarca

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Nuevas formas y estilos de extremos para los marcadores de elipse
Se han añadido varias formas nuevas -semiarcos y flechas- a la capa del símbolo del marcador de elipse, así como un ajuste para modificar el estilo de la tapa de las formas de elipse de sólo trazo.

![image18](images/entries/3b34a6b8ceb5cad5a423a10562511457c0c21396.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Establecer estilos de extremos para marcadores simples
QGIS now allows for the pen cap (or line ending) style to be set for simple marker symbol layers, which is useful for the stroke-only symbols like cross and arrowhead markers, where it\'s beneficial to allow the use of round caps instead of square caps.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Permitir que el estilo del extremo de la pluma se establezca para las capas del símbolo del marcador de elipse
Los marcadores de elipse ahora también incluyen soporte para modificar los estilos del extremo de la pluma (final de línea)

![image19](images/entries/5d01d2759751cf797586797a74beea3c9561677d.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Polygon rings \@geometry_ring_num variable
A new variable, `@geometry_ring_num`, has been added for data-defined styling when rendering polygon rings. The variable is available whenever a polygon outline is being rendered, such as a simple line or marker line. This data-defined property will be set to 0 for the exterior ring, and increment accordingly (1, 2, 3\... etc) for successive interior rings.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Etiquetando
### Prestación: Símbolos de relleno para los escudos de fondo de las etiquetas
Los escudos de las etiquetas ahora pueden utilizar símbolos de relleno para las formas de rectángulo, cuadrado, círculo y elipse.

This extends beyond the previously available ability for these shields to utilize simple fill and stroke and grants the ability to leverage the complete symbology capabilities of QGIS for shield rendering, including the utilization of \"saved styles\".

![image20](images/entries/5698488e5fae8bdd876dfe754b56bfad0c3fd950.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Configuración del modo de mezcla para las llamadas de las etiquetas
Las llamadas de etiquetas ahora pueden aprovechar los modos de mezcla avanzados de QGIS

![image21](images/entries/4dd84f1e0b5ec295da997ffd84fb15b2cae25b13.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Etiquetas de líneas de anclaje por línea completa
In previous versions, when an anchor position for a line label was calculated, QGIS would only consider the visible extent of the feature. This affected the expected label position in some cases, and a new \"Use Entire Line\" setting allows users to configure the behavior according to their needs, so that the entire feature may be considered before label placement rather than just the portion of a feature that is currently visible.

![image22](images/entries/1a1788cc98f860e53b8ba3b1b2d7ad5b0969179f.webp)

Esta prestación fue financiada por Stadt Zürich

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Radio de la esquina de la llamada del globo
Balloon callout styles now support rounded corners by introducing a \"corner radius\" option, resulting in the ability to easily produce visually pleasing designs.

![image23](images/entries/9c3d5b37de37e8db7168e68229a6bb3cd02138e6.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Llamadas con globos (burbujas de diálogo)
A new \"balloon\", or speech bubble, callout style is provided for labels.

![image24](images/entries/7dcb80eacfb6e10dc6b6b05a160421a93ee78d14.webp)

Esta prestación fue financiada por SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Estilo de llamada de líneas curvas
A new \"Curved Line\" callout style has been provided for creating cartographically pleasing curved line callouts between the labels and features

Las opciones incluyen:
- Selección de una orientación específica de la curva (en el sentido de las agujas del reloj o en sentido contrario)
- Opción de orientación automática que determina la orientación óptima para cada etiqueta individual
- Control de la cantidad de curvatura aplicada a las líneas de llamada.

![curved-callout](images/entries/fd1a05c782e4e2e487a5ed876dc6c396269b0acf.gif)

![image26](images/entries/42e4e2dd600bceda0ff426996577761d9e8b1638.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Resaltar los puntos de inicio o final de la llamada anclada
When the \"show pinned labels\" option is enabled, QGIS will now also highlight any pinned callout start or end points. This allows users to immediately see which callouts points have been manually placed in relation to those that are automatically placed.

![image27](images/entries/e1de38ee6adde2a016b8d4550111ff766211f0f7.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Creación automática de campos auxiliares de llamada
Ahora QGIS gestiona automáticamente la creación de campos auxiliares de llamada cuando se intenta mover un punto de inicio o final de llamada de forma interactiva, haciendo que la experiencia del usuario para mover una llamada siga exactamente el mismo comportamiento que el de mover una etiqueta, evitando que el sistema obligue a los usuarios a crear campos auxiliares por adelantado.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Ajuste de llamadas
Cuando se mueve interactivamente una línea de llamada, manteniendo el botón de mayúsculas, ahora la llamada se ajusta a ángulos en incrementos de 15 grados.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Acceso directo a las capas de etiquetas
Se ha añadido una acción de acceso directo para alternar el etiquetado en el menú contextual de las capas vectoriales en el panel de capas. Esto permite activar o desactivar rápidamente las etiquetas, sin perder la configuración de las mismas. Si una capa nunca ha tenido configurado el etiquetado y la acción está marcada, entonces QGIS intentará aplicar una configuración de etiquetado simple a la capa utilizando los parámetros por defecto.

![image28](images/entries/023bb952056e1d7f41e7a06590000f17b76d6d45.gif)

Esta prestación fue financiada por Natural resources Canada Contrato: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Puntos de inicio y fin de la llamada definidos por los datos
Las líneas de llamada de etiquetas ahora pueden tener puntos de inicio y finalización definidos por los datos, lo que resulta útil para el control manual de la ubicación exacta de las líneas de llamada individuales.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Permitir que las llamadas se muevan de forma interactiva mediante la herramienta Mover Etiqueta
This change allows the interactive \"Move labels\" tool to also move callout endpoints, whenever the callout has data-defined origin or destination fields set.

![image29](images/entries/8bb0e3614666059f3fe66065173f207d335d3800.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Nubes de Puntos
### Prestación: Soporte para conjuntos de datos remotos (EPT)
Point cloud datasets that have been processed to [EPT format](https://entwine.io/entwine-point-tile.html) can be loaded from remote HTTP(S) servers, similar to how raster/vector tiles work. This way, it is possible to access large point cloud datasets without first having to download them as LAS/LAZ files. The EPT format is optimized for tiling and streaming, so QGIS only downloads small amounts of data necessary for display of the current view and resolution. This works in both 2D and 3D view.

If you have point cloud datasets in LAS/LAZ format, these can be converted to EPT using [Entwine](https://github.com/connormanning/entwine) or [Untwine](https://github.com/hobu/untwine) (shipped also with QGIS).

How to use: in Data Source Manager \> Point Cloud tab \> select \"Protocol\" as the source type and enter URL of the dataset (normally ending with \"ept.json\").

You can test with [USGS LiDAR data](https://usgs.entwine.io/) - just use the link from \"EPT\" column from one of the datasets. Some example endpoints include:
- [Chicago](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_IL_4County_Cook_2017_LAS_2019/ept.json)
- [Mount Baker](https://s3-us-west-2.amazonaws.com/usgs-lidar-public/USGS_LPC_WA_MtBaker_2015_LAS_2017/ept.json)
- [Denmark](https://na-c.entwine.io/dk/ept.json)
- [Netherlands AHN2](https://na-c.entwine.io/ahn/ept.json)

By the way, every point cloud dataset that QGIS loads is first processed to EPT (look for \"ept_XXX\" sub-folder where your original data is located), so it is possible to just copy that \"ept_XXX\" folder to a HTTP(S) server and you are ready to use this feature.

![image30](images/entries/50ed450146655afb5c6ae68f0ead344cfc9eea73.webp)

This feature was funded by [Hobu](https://hobu.co/)

This feature was developed by [Belgacem Nedjima (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Diseño de impresión
### Feature: \"Convert to Static Text\" option
When using dynamic, or expression-based labels, users may now select the \"Convert to Static Text\" option which has been added to the dropdown menu next to \"Insert/Edit Expression...\", in the layout label properties widget.

This option will evaluate and replace any dynamic parts of a label\'s contents with their current values.

Esto proporciona una manera fácil de convertir las etiquetas dinámicas en estáticas, para que los usuarios puedan ajustar manualmente los resultados cuando sea necesario.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mejora de la vista previa de las capas XYZ en los elementos del mapa
Se ha mejorado la gestión de las capas XYZ previsualizadas en los elementos del mapa de diseño para garantizar que los niveles de acercamiento de las teselas coincidan con los del diseño exportado al acercar y alejar la vista en el diálogo del diseñador de diseños. Los usuarios pueden ahora afinar más fácilmente la colocación de sus elementos (etiquetas, leyendas, imágenes, etc.) en una vista previa del mapa que se ajusta mejor al resultado deseado.

Esta prestación fue financiada por Kanton Zug - Amt für Raum und Verkehr (ARV)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Expresiones
### Prestación: Función length3D
A \"length3D\" function has been added for returning the 3D length of a LineGeometry type geometry. This calculates the cartesian 3D length of a geometry line object. If the geometry is not a 3D line object, it returns its 2D length.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Funciones de expresión de matrices ampliadas
Se han añadido las siguientes expresiones de matriz:
- array_count
- array_prioritize
- array_replace

Esta prestación fue financiada por el Cantón de Lucerna

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
### Prestación: Función de expresión del tipo MIME
The new `mime_type( bytes )` expression function returns the MIME Type, or [Media type](https://en.wikipedia.org/wiki/Media_type), of an input bytes object

![image31](images/entries/c6aa4689915ec3337efac4284ed39a15e8cadddf.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Digitalizando
### Prestación: Seleccionar los atributos de la geometría más grande al fusionar
Se ha añadido un botón para seleccionar los atributos de la geometría más grande en el diálogo de confirmación cuando se utilizan las herramientas de edición de características de fusión para las capas de polígonos y líneas.

![image32](images/entries/e27a6a42f878cdfec87021d53241457aa1d8845f.webp)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Prestación: Modo de digitalización en streaming
When streaming digitizing mode is active, points are automatically added following the mouse cursor movement, providing a \"freehand drawing\" type experience.

Using the \"R\" key during digitizing operations will toggle streaming digitizing and normal (or circular string) digitizing.

Funciona con múltiples herramientas de mapa, incluyendo la creación de nuevos objetos espaciales de líneas o polígonos, añadir anillo, añadir parte, remodelar, dividir características, dividir partes, y más.

![image33](images/entries/854b65b029335216c7e37c89168389f945e62fe2.gif)

Esta prestación fue financiada por Natural resources Canada Contrato: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New \"Line Endpoints\" snapping option
Cuando está activado, este modo de ajuste se ajusta sólo al vértice inicial o final de las líneas. Cuando se ajusta a una capa de polígono, sólo se ajusta al primer vértice de los anillos.

Esta prestación fue financiada por Natural resources Canada Contrato: 3000720707

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Selección de vértices por polígono
Ahora los usuarios pueden utilizar el botón ALT para seleccionar vértices por polígono mientras digitalizan.

Esto debería mejorar la experiencia del usuario para la selección de vértices específicos utilizando la herramienta de vértices, reduciendo la necesidad de múltiples pasadas utilizando las funciones SHIFT o CTRL para añadir y eliminar vértices de la selección actual.

Esto también reduce la necesidad de rotar creativamente el lienzo del mapa con el fin de alinear los vértices para la selección, y proporciona un proceso de edición mejorado, como por ejemplo para seleccionar los vértices de una carretera curva a lo largo de un solo lado.

Esta función admite las siguientes operaciones de uso:
- Alt+clic con la herramienta de vértices para empezar a digitalizar un polígono.
- Cada clic posterior añade un nuevo vértice al polígono de la banda elástica.
- El retroceso/eliminación elimina el último vértice de la banda elástica añadido.
- Esc cancels the polygon selection mode, as does backspace/ deleting all of the rubberband\'s vertices.
- El clic derecho finaliza la digitalización del polígono y selecciona todos los vértices dentro del polígono de la banda elástica.

![image34](images/entries/d4a70011e9064862c99827f5b940805dd2d45182.gif)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
## Administración de datos
### Prestación: Icono de advertencia en el árbol de capas para las capas con imprecisiones en el SRC
A new \"Show CRS accuracy warnings for layers in project legend\" is provided which, when checked, will display a new warning icon identifying any layers with a CRS which is identified as having accuracy issues.

Ejemplos de capas de baja precisión pueden ser aquellas con un SRC dinámico sin época de coordenadas disponible, o un SRC basado en un conjunto de datos con una precisión que supera el límite establecido por el usuario.

Esta opción está desactivada por defecto, y está diseñada para su uso en ingeniería, BIM y otros sectores en los que las inexactitudes del nivel de los contadores/subcontadores son muy peligrosas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Soporte básico para la época de coordenadas SRC dinámicas
Basic support for the coordinate epoch of dynamic (not plate fixed) CRS has been added in line with relevant updates to [GDAL](https://github.com/OSGeo/gdal/pull/3810).

QGIS ha añadido soporte para respetar la época de las coordenadas de origen o destino cuando se transforma a o desde un SRC dinámico.

Si se intenta realizar una transformación de SRC dinámico a SRC dinámico en diferentes épocas, lo cual no es soportado actualmente por PROJ, se mostrará un mensaje de advertencia al usuario advirtiéndole que los resultados pueden ser engañosos y no deben ser utilizados para trabajos de alta precisión.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mejoras en la información de proyección
Se han introducido varias mejoras en el manejo y la representación de la información de proyección en QGIS, entre ellas:
- La adición de una API para recuperar los detalles de la operación PROJ para los SRC
- The ability to show extended information about a layer\'s CRS in the layer properties info tab, including accuracy warnings
- The addition of a `@map_crs_projection` variable, for retrieving a friendly name of a map\'s projection (e.g. \"Albers Equal Area\")

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Avisos SRC de conjunto de datums
QGIS now shows a warning in the projection selection widget when a CRS based on a datum ensemble is selected, warning the user that there\'s an inherent lack of accuracy in the selected CRS.

![image35](images/entries/b99e932e308d3b6d2b3868a88f3528386adb3d1f.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Persistencia de los metadatos de las capas en las exportaciones de archivos vectoriales
A \"persist layer metadata\" checkbox has been added to the export vector file dialog. When checked, any layer metadata present in the source layer will be copied and stored in the destination file.

Esta función está activada por defecto y garantiza que los metadatos se transfieran correctamente a los elementos recién creados, lo que resulta especialmente eficaz cuando se utiliza el formato GPKG.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Notas de capa
QGIS now supports \"layer notes\", which can be created via the \"Add Layer Notes\" action in the layer context menu.

Estas notas se guardan por capa, por proyecto. Pueden utilizarse como lugar para almacenar mensajes importantes para los usuarios del proyecto, como listas de tareas, instrucciones de procesamiento o gestión, o cualquier otro metadato arbitrario basado en texto.

Un icono indicador de notas en el panel de capas identifica las capas que tienen notas adjuntas. Al hacer clic en el icono del indicador de notas se abrirá la nota para su edición.

This feature was discussed in [QEP-206](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/206)

Estas notas pueden copiarse y pegarse utilizando la metodología tradicional de copiar y pegar para transferir estilos entre capas en QGIS.

Las notas de capa también son compatibles con los archivos QML (QGIS Style) y QLR (QGIS Layer Definition) y se almacenan en ellos.

![image36](images/entries/250d188c3987a1247b9e3a414d5d72c9c681b0ad.webp)

Esta prestación ha sido financiada por Alta Ehf

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Carga automática de metadatos .shp.xml
QGIS ahora cargará y convertirá automáticamente los metadatos de ESRI almacenados mediante un archivo sidecar .shp.xml. Cuando se carguen datos shapefile y estos archivos de metadatos estén presentes, se cargarán automáticamente, con los metadatos de capa disponibles rellenados en consecuencia.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Traducir automáticamente los datos de las capas de las bases de datos de archivos de ESRI a los metadatos de las capas de QGIS
When loading data from a .gdb file, QGIS will automatically attempt to translate as much as possible of the original ESRI metadata across to the QGIS metadata, so that it\'s immediately available for use.

Esta prestación ha sido financiada por North Road / SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Lectura de dominios de campo a partir de conjuntos de datos
Para los formatos que soportan la definición incrustada de dominios de campo (actualmente GPKG y GDB), QGIS convierte automáticamente el dominio de campo incrustado a la configuración equivalente del editor de QGIS para el campo.

Esto significa que GPKG/GDB con dominios de campo codificados se cargarán automáticamente en QGIS con su configuración correcta del widget de Mapa de Valores intacta, de modo que los usuarios vean las descripciones de los valores de campo en lugar de los códigos en bruto. Los campos con un dominio de tipo rango (mín/máx) se traducirán también al widget de rango para el campo.

Esta prestación ha sido financiada por North Road

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Permitir la carga de capas GPKG con el tipo GEOMETRY
GeoPackage supports layers with a generic \"geometry\" type, with the QGIS release 3.20 it is now possible to load them and specify the requested geometry type on load, just like with PostGIS.

![image37](images/entries/a37aab7ea49b4870a931206e88811ebabcff6546.webp)

This feature was developed by [Marco Bernasocchi (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Soporte de edición fuera de línea para los tipos de campo de lista de cadenas y lista de números
Usuarios de PostGIS recocíjense: la edición fuera de línea se ha vuelto un poco más inteligente y ahora puede manejar los tipos de campo de lista de cadenas y lista de números.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Widgets y Formularios
### Prestación: Utilización por campos de los últimos valores de los objetos espaciales recién creados
Se ha ampliado el control para saber si los últimos valores de campo introducidos deben reutilizarse al crear nuevos objetos espaciales, ya que esta funcionalidad puede controlarse ahora de forma independiente para cada campo de atributo individual de cada capa.

Históricamente esta funcionalidad se configuraba utilizando una opción global que hace que TODOS los valores de los campos de TODAS las capas sean recordados y reutilizados durante una sesión de QGIS al crear nuevos objetos espaciales.

Esto permite un control más fino sobre el comportamiento del formulario, donde algunos valores pueden ser deseables para reutilizar, pero otros deben ser borrados o establecidos a un valor por defecto basado en una expresión.

![image38](images/entries/73f699bdf27a1b3b35de96e7a233d12a49b585d9.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Widget de Vista JSON
Nuevo widget de vista para mostrar los datos JSON de una manera fácil de usar. Los datos pueden mostrarse como texto resaltado por la sintaxis o como un árbol.

![image39](images/entries/1061561e58e1b0807158ab415f4a13b43589d824.gif)

This feature was funded by [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/)

This feature was developed by [Damiano Lombardi](http://damiano@opengis.ch)
## Leyenda de capa
### Feature: Vector \"label\" legend entries
QGIS admite ahora la adición de entradas de leyenda para las etiquetas de las capas, que mostrarán el estilo de fuente y las clases de etiquetado para los objetos espaciales vectoriales.

Esto proporciona una entrada de leyenda que permite a los usuarios identificar explícitamente los objetos espciales por el estilo de la etiqueta, incluso cuando no se utiliza ninguna simbología de objetos espaciales.

Control of this behavior is made accessible by adding a \"show label legend\" option to the legend tab of the vector layer properties.

![image40](images/entries/89218cecca8823903e432b9cd1a38280cc5101a9.webp)

Esta prestación ha sido financiada por el Cantón de Glarus

This feature was developed by [mhugent](https://github.com/mhugent)
## Procesado
### Prestación: Añadir la opción de guardar los metadatos de las capas en el algoritmo Empaquetar Capas
Esta opción adicional enriquece el algoritmo de Empaquetar Capas y copiará los metadatos de la capa de origen en el geopackage, de modo que se utilizarán como metadatos por defecto para la capa.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Algoritmo de las Propiedades de las Capas Ráster
Este algoritmo recupera las propiedades básicas de la capa ráster, como el tamaño en píxeles, las dimensiones de los píxeles (unidades cartográficas por píxel), el número de bandas y el valor sin datos.

It is intended for use as a means of extracting these useful properties to use as the input values to other algorithms in a model, such as passing an existing raster\'s pixel sizes over to a GDAL raster algorithm.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mejora de la operación de rasterización con soporte 3D
El proceso de rasterización (de vector a ráster) de GDAL es ahora compatible con los datos 3D, ya que incluye la posibilidad de utilizar el valor Z (elevación) de una característica para extraer los valores de quemado.

The use of this option indicates that a burn value should be extracted from the "Z" values of the feature. Works with points and lines (linear interpolation along each segment). For polygons, it only works properly if the features are flat (i.e. contain the same Z value for all vertices)

This feature was developed by [talledodiego](https://github.com/talledodiego)
### Prestación: Guardar la opción seleccionada para el algoritmo de Empaquetar Capas
El algoritmo Empaquetar Capas se ha modificado para permitir guardar sólo los objetos espaciales seleccionados

This feature was developed by [Stefan Conrads](https://github.com/stefancon)
### Prestación: Niveles de registro para el procesamiento del contexto
Se ha añadido una nueva propiedad de nivel de registro a QgsProcessingContext

Esto permite que los algoritmos ajusten su salida en función del nivel de registro.

The qgis_process command line operation has been granted a \--verbose switch to enable verbose log output.

Esta prestación ha sido financiada por Natural Resources Canada Contrato: 3000720411

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: La revisión de la geometría ofrece un gran aumento de la velocidad
This development cycle saw a rework of the inner workings of QGIS\' geometry snapper algorithm, which has led to a significant speed boost. Datasets which could take over 10 minutes to process now take less than 10 seconds.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Feature: Add a last_value function to the aggregate algorithm
The aggregate processing tool now includes a `last_value` aggregation function, which is especially useful when working with input data that has meaningful ordering.

![image41](images/entries/77afe9dba20e9134db3a1c628c5eeebab275b87a.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Opciones de Aplicación y Proyecto
### Prestación: Añadir una opción global para desactivar la supervisión de los directorios
Permite a los usuarios excluirse manualmente de la monitorización de directorios en el navegador por defecto, y también proporciona un mecanismo para que las instalaciones empresariales deshabiliten este comportamiento potencialmente no deseado.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: API para la exportación e importación de configuraciones de autenticación XML
QGIS proporciona ahora funciones de exportación e importación al gestor de autenticación de QGIS. Esta funcionalidad aún no ha sido expuesta a través de la interfaz de usuario. Las configuraciones de autenticación complejas con numerosas, como OAuth2, pueden ser opcionalmente encriptadas o almacenadas en texto plano para mejorar los flujos de trabajo de gestión de la autenticación.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Navegador
### Prestación: Colores de iconos personalizados para las carpetas en el navegador
QGIS now allows users to set a custom icon color for different folders in the browser. This effectively allows users to \"tag\" folders, which aids in the rapid navigation of complex folder structures in the browser.

![image42](images/entries/5135bb429434786f87aca3d2deeb980ce874ae44.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Grupo OWS eliminado del Explorador QGIS
The non-functional and redundant \"OWS\" Group has been removed from the QGIS Browser panel.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## Proveedores de datos
### Prestación: Se ha añadido soporte para los tipos de datos de lista enteros, reales y enteros64 en OGR
Se han añadido tipos de campos de lista adicionales al controlador OGR para los tipos de datos compatibles, como Geojson.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Ampliar las capacidades de lectura de capas vectoriales a otros tipos de capas
Whilst the ability for QGIS to access a layer\'s metadata information, such as reading the extent of a layer from the metadata, was previously restricted to vector layers, this functionality has now been extended to include various other layer types including raster, point cloud, and others.

Esta prestación fue fundada por Ifremer

This feature was developed by [rldhont](https://github.com/rldhont)
## Servidor de QGIS
### Prestación: Opacidad de la capa externa
Soporte de control de opacidad para capas externas/remotas servidas por QGIS Server

This feature was developed by [mhugent](https://github.com/mhugent)
### Prestación: URL de servicio configurable
Se han añadido opciones adicionales a QGIS Server para mejorar los resultados de la respuesta GetCapabilities, especialmente sin la necesidad de completar varios campos dentro de la configuración del proyecto QGIS. Estas actualizaciones también permiten establecer muchas opciones mediante una variable de entorno, o proporcionando cabeceras desde un proxy.

Se han añadido las siguientes opciones que serán resueltas por el servidor en el siguiente orden:
- Valor definido en el proyecto por servicio.
- The `<service>_SERVICE_URL` environment variable.
- The `SERVICE_URL` environment variable.
- The custom `X-Qgis-<service>-Service-Url` header.
- The custom `X-Qgis-Service-Url` header.
- Build from the standard `Forwarded` header.
- Build from the pseudo standard `X-Forwarded-Host` and `X-Forwarded-Proto` headers.
- Build from the standard `Host` header and the server protocol.
- Construye a partir del nombre del servidor y el protocolo del servidor.

This feature was developed by [Stéphane Brunner](https://github.com/sbrunner)
## Correcciones Notables
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| advertencia del compilador en QgsMeshDatasetGroupStore::readXml() | no reportado | [PR #43304](https://github.com/qgis/QGIS/pull/43304) | N/D |
| QGIS se cae con GDAL 3.3 | [#43224](https://github.com/qgis/QGIS/issues/43224) | [PR #43306](https://github.com/qgis/QGIS/pull/43306) | [PR #43323](https://github.com/qgis/QGIS/pull/43323) |
| Los datos se corrompen al borrar un campo en una capa (específica) del geopackage | [#42768](https://github.com/qgis/QGIS/issues/42768) | [PR #43309](https://github.com/qgis/QGIS/pull/43309) | [PR #43322](https://github.com/qgis/QGIS/pull/43322) |
| PyQGIS: La uri de la capa WMS-T sin timeDimensionExtent en ella hace caer a QGIS | [#43158](https://github.com/qgis/QGIS/issues/43158) | [PR #43310](https://github.com/qgis/QGIS/pull/43310) | [PR #43324](https://github.com/qgis/QGIS/pull/43324) |
| Corrupción de datos: La sobreescritura de GPKG OID/FID fallida hace que el valor se desborde en la siguiente columna de atributos | [#42274](https://github.com/qgis/QGIS/issues/42274) | [PR #43311](https://github.com/qgis/QGIS/pull/43311) | [PR #43360](https://github.com/qgis/QGIS/pull/43360) |
| \"Split features\" causes data loss | [#41283](https://github.com/qgis/QGIS/issues/41283) | [PR #43328](https://github.com/qgis/QGIS/pull/43328) | [PR #43340](https://github.com/qgis/QGIS/pull/43340) |
| Las comprobaciones de las restricciones de llave foránea se ignoran en la GPKG | [#34728](https://github.com/qgis/QGIS/issues/34728) | [PR #43330](https://github.com/qgis/QGIS/pull/43330) | No apropiado |
| Extraño mensaje de error de Compositor de Consulta SQL en el cliente WFS | [#42985](https://github.com/qgis/QGIS/issues/42985) | [PR #43334](https://github.com/qgis/QGIS/pull/43334) | [PR #43341](https://github.com/qgis/QGIS/pull/43341) |
| WFS 1.1.0 ExceptionReport response handling : QGIS looks for \'exceptionCode\' but in specifications it\'s \'code\' attribute | [#42196](https://github.com/qgis/QGIS/issues/42196) | [PR #43335](https://github.com/qgis/QGIS/pull/43335) | [PR #43342](https://github.com/qgis/QGIS/pull/43342) |
| Falla la selección de exportación de una capa WFS grande | [#42049](https://github.com/qgis/QGIS/issues/42049) | [PR #43336](https://github.com/qgis/QGIS/pull/43336) | [PR #43343](https://github.com/qgis/QGIS/pull/43343) |
| El WKT largo (?) hace que la capa de texto delimitada falle en 3.16 y 3.18 | [#43256](https://github.com/qgis/QGIS/issues/43256) | [PR #43337](https://github.com/qgis/QGIS/pull/43337) | [PR #43339](https://github.com/qgis/QGIS/pull/43339) |
| SRS incorrecto al leer una capa de Postgis | no reportado | [PR #43338](https://github.com/qgis/QGIS/pull/43338) | No apropiado |
| Datos de malla en formato GRIB de ERA5 | [#41809](https://github.com/qgis/QGIS/issues/41809) | [GDAL PR 3875](https://github.com/OSGeo/gdal/pull/3875) | [GDAL PR 3877](https://github.com/OSGeo/gdal/pull/3877) |
| Two OGR provider filtered layers with same source dataset don\'t restore proper feature count / extent on project reload | [#43361](https://github.com/qgis/QGIS/issues/43361) | [PR #43372](https://github.com/qgis/QGIS/pull/43372) | [PR #43394](https://github.com/qgis/QGIS/pull/43394) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/en/home/)
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| El gestor de fuentes de datos no consigue derivar el tipo de geometría 3D exacta para las tablas GeometryZ PostGIS | [#43268](https://github.com/qgis/QGIS/issues/43268) | [PR #43326](https://github.com/qgis/QGIS/pull/43326) |  |
| Attribute table conditional formatting doesn\'t work when using \$geometry is NULL | [#43252](https://github.com/qgis/QGIS/issues/43252) | Trabaja para mí |  |
| Salidas incompletas QgsZonalStatistics.calculateStatistics() | [#43245](https://github.com/qgis/QGIS/issues/43245) | [PR #43332](https://github.com/qgis/QGIS/pull/43332) | [PR #43378](https://github.com/qgis/QGIS/pull/43378) |
| Mala Solicitud en feed.qgis.org | [#43232](https://github.com/qgis/QGIS/issues/43232) | [PR #43333](https://github.com/qgis/QGIS/pull/43333) | No relevante |
| Servidor: Características de WFS3/API - superposición de columnas/contenido en elementos de datos como páginas HTML | [#42269](https://github.com/qgis/QGIS/issues/42269) | [PR #43363](https://github.com/qgis/QGIS/pull/43363) | [PR #43380](https://github.com/qgis/QGIS/pull/43380) |
| La transformación de datum utilizando la cuadrícula gsb personalizada para la capa WMS en QGIS Server no funciona | [#43072](https://github.com/qgis/QGIS/issues/43072) | [PR #43365](https://github.com/qgis/QGIS/pull/43365) | No relevante |
| Server: fix unreported QGIS_OPTIONS_PATH not really working for proj | no reportado | [PR #43366](https://github.com/qgis/QGIS/pull/43366) | No apropiado |
| WFS cascade getfeatureinfo falla | [#42062](https://github.com/qgis/QGIS/issues/42062) | Trabaja para mí |  |
| Servidor autónomo: arreglar el almacenamiento de proyectos no soportado con -p | no reportado | [PR #43381](https://github.com/qgis/QGIS/pull/43381) | [PR #43464](https://github.com/qgis/QGIS/pull/43464) |
| QGIS Server GetPrint: HIGHLIGHT_GEOM is not printed if map layers are configured to follow a map theme | [#34178](https://github.com/qgis/QGIS/issues/34178) | [PR #43391](https://github.com/qgis/QGIS/pull/43391) | Arriesgado |
| El recuento de objetos espaciales es erróneo al añadir objetos espaciales de una tabla con objetos espaciales de geometrías mixtas | [#43199](https://github.com/qgis/QGIS/issues/43199) | Trabaja para mí |  |
| No todos los tipos de geometría se encuentran en la tabla PostGIS con el tipo espacial de geometría | [#43186](https://github.com/qgis/QGIS/issues/43186) | [PR #43419](https://github.com/qgis/QGIS/pull/43419) | Arriesgado |
| El icono no se actualiza al guardar una capa de rascado | no reportado | [PR #43431](https://github.com/qgis/QGIS/pull/43431) | [PR #43463](https://github.com/qgis/QGIS/pull/43463) |
| Arreglar la lista de protocolos en la configuración personalizada de ssh | no reportado | [PR #43432](https://github.com/qgis/QGIS/pull/43432) | No apropiado |
| Se bloquea con la tabla establecida en Mostrar Visible, se une, y se deja abierta al salir de QGIS | [#43287](https://github.com/qgis/QGIS/issues/43287) | [PR #43434](https://github.com/qgis/QGIS/pull/43434) | No apropiado |
| \"show label\" is disabled in widget designer but label keeps displaying in attribute form if you use tabs in the Drag and-Drop Designer and the field widget was placed in any tab | [#43103](https://github.com/qgis/QGIS/issues/43103) | [PR #43435](https://github.com/qgis/QGIS/pull/43435) | PORHACER. |
| El navegador añade capas a los proyectos con un espacio por delante | [#43129](https://github.com/qgis/QGIS/issues/43129) | [PR #43436](https://github.com/qgis/QGIS/pull/43436) | No apropiado |
| Error en saveStyleToDatabase() al guardar más de una capa en un GPKG | [#42988](https://github.com/qgis/QGIS/issues/42988) | Trabaja para mí |  |
| Los parámetros del widget no son persistentes para las relaciones en diseñador D&D | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43468](https://github.com/qgis/QGIS/pull/43468) | No apropiado |
| Rule-based rendering sometimes doesn\'t show all results | [#43181](https://github.com/qgis/QGIS/issues/43181) | [PR #43502](https://github.com/qgis/QGIS/pull/43502) | Arriesgado |
| Corregir la falta de estadísticas de bandas rasterizadas en el panel de información | no reportado | [PR #43507](https://github.com/qgis/QGIS/pull/43507) |  |
| La calculadora de rásteres no crea/almacena estadísticas para los rásteres de salida | [#42835](https://github.com/qgis/QGIS/issues/42835) | [PR #43512](https://github.com/qgis/QGIS/pull/43512) | No es una prioridad |
| Attribute Form Value Relation Doesn\'t Respect Column Default | [#41951](https://github.com/qgis/QGIS/issues/41951) | Trabaja para mí |  |
| Attribute table in form view can display \"ghost\" attributes | [#43477](https://github.com/qgis/QGIS/issues/43477) | [PR #43533](https://github.com/qgis/QGIS/pull/43533) | No es una prioridad |
| Problema de la cláusula por defecto de la identidad PG | <https://lists.osgeo.org/pipermail/qgis-user/2021-June/048983.html> | [PR #43529](https://github.com/qgis/QGIS/pull/43529) | No apropiado |
| Error Pyqgis 3.18.3 al añadir la capa WMS | [#43580](https://github.com/qgis/QGIS/issues/43580) | [PR #43581](https://github.com/qgis/QGIS/pull/43581) | PORHACER. |
| \"Reuse last entered attribute values\" slows creation of new features on large vector | [#42909](https://github.com/qgis/QGIS/issues/42909) | [PR #43584](https://github.com/qgis/QGIS/pull/43584) | PORHACER. |
| Deleting \"all other values\" breaks date based categorise symbology | [#43651](https://github.com/qgis/QGIS/issues/43651) | [GDAL PR 3978](https://github.com/OSGeo/gdal/pull/3978) |  |
| Correge la documentación de las construcciones doctest | <https://github.com/qgis/QGIS-Documentation/pull/6747> | <https://github.com/qgis/QGIS-Documentation/pull/6747> | No relevante |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Funcionalidad: Corrección de errores por Paul Blottiere
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| VERSION es ahora obligatoria en WMS 1.3.0 para las solicitudes de getmap | no reportado | [PR #43459](https://github.com/qgis/QGIS/pull/43459) | [PR #43467](https://github.com/qgis/QGIS/pull/43467) |
| WMTS GetCapabilities y orden de los ejes | [#34826](https://github.com/qgis/QGIS/issues/34826) | [PR #43280](https://github.com/qgis/QGIS/pull/43280) | [PR #43772](https://github.com/qgis/QGIS/pull/43772) |
| Utilizar la versión más baja en la negociación del wms | [#41051](https://github.com/qgis/QGIS/issues/41051) | [PR #41376](https://github.com/qgis/QGIS/pull/41376) | Arriesgado |
| QGIS crashes adding a record to a memory (\"scratch\") layer table in some circumstances | [#42578](https://github.com/qgis/QGIS/issues/42578) | Trabaja para mí |  |
| QGIS falla silenciosamente cuando no se puede crear una capa auxiliar | no reportado | [PR #43543](https://github.com/qgis/QGIS/pull/43543) | [PR #43773](https://github.com/qgis/QGIS/pull/43773) |
| No se puede guardar el almacenamiento auxiliar | [#26365](https://github.com/qgis/QGIS/issues/26365) | [PR #43560](https://github.com/qgis/QGIS/pull/43560) | Arriesgado |
| WMS GetFeatureInfo en la capa de tiempo habilitado no pasa el parámetro TIME | [#42141](https://github.com/qgis/QGIS/issues/42141) | [PR #43599](https://github.com/qgis/QGIS/pull/43599) | [PR #43774](https://github.com/qgis/QGIS/pull/43774) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://www.qcooperative.net/)
### Prestación: Corrección de errores por Denis Rouzaud
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Los parámetros del widget no son persistentes para las relaciones en diseñador D&D | [#43123](https://github.com/qgis/QGIS/issues/43123) | [PR #43479](https://github.com/qgis/QGIS/pull/43479) | irrelevante |
| Use a read-only line edit instead of combobox in relation reference doesn\'t allow to add a child from the parent | [#42813](https://github.com/qgis/QGIS/issues/42813) | [PR #43509](https://github.com/qgis/QGIS/pull/43509) | demasiado arriesgado / no merece la pena |
| no hay forma abierta en todas las capas filtro localizador de características (filtro activo tiene) + mostrar la forma en lugar de error para las capas sin geometría | no reportado | [PR #43462](https://github.com/qgis/QGIS/pull/43462) | ¿? |
| No se puede añadir una relación polimórfica | [#41959](https://github.com/qgis/QGIS/issues/41959) | [PR #43488](https://github.com/qgis/QGIS/pull/43488) | irrelevante |
| La expresión de filtro del widget de referencia de la relación en el formulario de atributos, no funciona correctamente | [#42803](https://github.com/qgis/QGIS/issues/42803) | [PR #43523](https://github.com/qgis/QGIS/pull/43523) | si |
| corregir El elemento de diseño de imagen no maneja correctamente una ruta de archivo inexistente cuando se proporciona con una expresión | [#42280](https://github.com/qgis/QGIS/issues/42280) | [PR #43119](https://github.com/qgis/QGIS/pull/43119) |  |
| error en las relaciones: desaparece el acercamiento al botón hijo | [#34477](https://github.com/qgis/QGIS/issues/34477) | Trabaja para mí |  |
| Value Relation and Relation reference widget: Entries are sorted although the option \"Order by value\" is NOT checked | [#26468](https://github.com/qgis/QGIS/issues/26468) | no estoy seguro de cómo arreglar esto por ahora |  |
| Errores al añadir una característica con una relación polimórfica | [#41962](https://github.com/qgis/QGIS/issues/41962) | corregido |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProjectionSelectionWidget::selectCrs() no se puede sobrescribir en Python | [#43019](https://github.com/qgis/QGIS/issues/43019) | Funciona para mí. |  |
| ¿Un error? en FindPyQt5.py | [#41913](https://github.com/qgis/QGIS/issues/41913) | [#41913](https://github.com/qgis/QGIS/issues/41913) | irrelevante |
| Falta icono del complemento núcleo Comprobador de Geometría | [#42708](https://github.com/qgis/QGIS/issues/42708) | [PR #43536](https://github.com/qgis/QGIS/pull/43536) | [PR #43549](https://github.com/qgis/QGIS/pull/43549) |
| Por favor, elimine el grupo OWS no funcional del navegador QGIS | [#24841](https://github.com/qgis/QGIS/issues/24841) | [PR #43559](https://github.com/qgis/QGIS/pull/43559) | No apropiado |
| La construcción falla con el qwtpolar externo | [#41910](https://github.com/qgis/QGIS/issues/41910) | [PR #43551](https://github.com/qgis/QGIS/pull/43551) | [PR #43583](https://github.com/qgis/QGIS/pull/43583) |
| La herramienta de comprobación de geometrías no guarda los cambios de acción por defecto | [#42489](https://github.com/qgis/QGIS/issues/42489) | [PR #43550](https://github.com/qgis/QGIS/pull/43550) | [PR #43568](https://github.com/qgis/QGIS/pull/43568) |
| Ubicación incorrecta de la salida del error cuando se utiliza Comprobar validez en datos con cierto tipo de error 3D | [#43582](https://github.com/qgis/QGIS/issues/43582) | [PR #43588](https://github.com/qgis/QGIS/pull/43588) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Las tablas de Postgresql con campos intarray como clave primaria causan problemas en los scripts de python | [#42778](https://github.com/qgis/QGIS/issues/42778) | [PR #43493](https://github.com/qgis/QGIS/pull/43493) | [PR #43510](https://github.com/qgis/QGIS/pull/43510) |
| No se puede instanciar QgsFeatureFilterModel usando PyQGIS | [#42488](https://github.com/qgis/QGIS/issues/42488) | [PR #43494](https://github.com/qgis/QGIS/pull/43494) | [PR #43516](https://github.com/qgis/QGIS/pull/43516) |
| QGIS se bloquea al cargar el archivo ui | [#42379](https://github.com/qgis/QGIS/issues/42379) | Funcionando |  |
| Campo QvariantList , nada en la tabla de atributos cuando hay un solo valor en la lista | [#33108](https://github.com/qgis/QGIS/issues/33108) | [PR #43508](https://github.com/qgis/QGIS/pull/43508) | [PR #43530](https://github.com/qgis/QGIS/pull/43530) |
| Copiar SRC en el portapapeles cuando se copian las características seleccionadas | [#40117](https://github.com/qgis/QGIS/issues/40117) | [PR #43527](https://github.com/qgis/QGIS/pull/43527) | [PR #43532](https://github.com/qgis/QGIS/pull/43532) |
| La tarea abierta en ejecución (conexión) hace imposible salir de QGIS | [#40001](https://github.com/qgis/QGIS/issues/40001) | [PR #43587](https://github.com/qgis/QGIS/pull/43587) |  |
| Plugin manager doesn\'t work with proxy | [#43284](https://github.com/qgis/QGIS/issues/43284) | Retroalimentación |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #43617](https://github.com/qgis/QGIS/pull/43617) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Prestación: Corrección de Errores por Peter Petrik
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Las contraseñas no se pueden guardar en el llavero en macOS con QGIS 3.16 | [#40541](https://github.com/qgis/QGIS/issues/40541) | retroalimentación |  |
| El perfil con errores da lugar a que se inicien dos instancias | [#29379](https://github.com/qgis/QGIS/issues/29379) | ya no es un problema |  |
| Error de inicio del complemento de GRASS en macOS | [#41782](https://github.com/qgis/QGIS/issues/41782) | Funciona para mí. |  |
| El Gestor de Fuentes de Datos identifica incorrectamente la extensión ráster de PostGIS en macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | investigación |  |
| Crash with point clouds when zooming into 3D viewer \[Mac\] | [#41903](https://github.com/qgis/QGIS/issues/41903) | [PR #43743](https://github.com/qgis/QGIS/pull/43743) | irrelevante |
| Crash when chcking the \"Show bounding boxes\" option in 3D view settings | [#40766](https://github.com/qgis/QGIS/issues/40766) | [PR #43755](https://github.com/qgis/QGIS/pull/43755) | backport_bot |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL (si se informa, Github) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir el escaneo del panel del navegador en ubicaciones remotas puede colgar QGIS | muchas PRs |  |  |
| \[3d\] Fix rendering of curved lines using simple line renderer | no reportado | [Commit 700390a](https://github.com/qgis/QGIS/commit/700390abff6928636de010c49746a10129c215eb) |  |
| Fijar la vista previa de las capas a través del panel del navegador | [#43303](https://github.com/qgis/QGIS/issues/43303) | [Commit 7bf85a0](https://github.com/qgis/QGIS/commit/7bf85a0cccc105208a0a9563396ad8ca10a38810) |  |
| \[expressions\] Fix evaluation of round(\...) where input value is a string containing a decimal number | [#36467](https://github.com/qgis/QGIS/issues/36467) | [Commit 42c2061](https://github.com/qgis/QGIS/commit/42c2061c5418bbcfa2fde8aac35486ac7fcb26b1) |  |
| Fix label masking settings get dropped for layers with \",\" or \";\" characters in the text | [#37473](https://github.com/qgis/QGIS/issues/37473) | [Commit 3d4e2f4](https://github.com/qgis/QGIS/commit/3d4e2f460f5ca04a469a2549c69b96dea889b174) |  |
| Corregir el enmascaramiento de símbolos huérfanos puede obligar a rasterizar los mapas | no reportado | [Commit ffc500d](https://github.com/qgis/QGIS/commit/ffc500d79de02d9f83d36a8fa40b4436079be04d) |  |
| Corregir la selección de objetos espaciales que utilizan variables en las reglas de filtrado | [#42006](https://github.com/qgis/QGIS/issues/42006) | [Commit d41c234](https://github.com/qgis/QGIS/commit/d41c2342676098e9c9991305711b9eea748bb858) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[labeling\] Default to \"from symbol bounds\" for cartographic point label placement | [#25866](https://github.com/qgis/QGIS/issues/25866) | [Commit 4ad5d36](https://github.com/qgis/QGIS/commit/4ad5d36d93df8eaf0105aed2c9918197f5bf67ef) |  |
| El constructor de PyQGIS QgsLineString sólo acepta listas de QgsPoint, no QgsPointXY como indica la documentación | [#43200](https://github.com/qgis/QGIS/issues/43200) | [Commit 2b6c3c1](https://github.com/qgis/QGIS/commit/2b6c3c1db2cc3c8214a6c019c2c044b8bae712f2) |  |
| Corregir el fallo al cambiar los niveles de los símbolos a través del muelle de estilo | [#42671](https://github.com/qgis/QGIS/issues/42671) | [Commit f3f4c17](https://github.com/qgis/QGIS/commit/f3f4c17c5fa1d71670d505a2938da2345c683909) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Permitir el borrado de los datos definidos en los botones que se establecen en campos inexistentes | no reportado | [Commit ee03ad5](https://github.com/qgis/QGIS/commit/ee03ad5991094ec975118c986075d0e830dec469) |  |
| \[processing\] Python entry in history dialog should be processing.run line, not processing.execAlgorithmDialog | no reportado | [Commit 61ac64c](https://github.com/qgis/QGIS/commit/61ac64c5a146adc72d38eaf5ab3fe35a6f51be20) |  |
| Don\'t try to render font marker symbols in massive font sizes, avoid crash | [#42270](https://github.com/qgis/QGIS/issues/42270) | [Commit 12d1078](https://github.com/qgis/QGIS/commit/12d1078a8bc11caef7002629e6315cf50522e732) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Corregir Qgis::MessageLevel::None no está disponible en PyQGIS | [#42996](https://github.com/qgis/QGIS/issues/42996) | [Commit 02266ef](https://github.com/qgis/QGIS/commit/02266ef8e66ef6613d27e7818e0e7adf0d5a3271) |  |
| Corregir que los límites de los símbolos de los marcadores incluyen incorrectamente los límites de las capas de símbolos desactivadas | no reportado | [Commit ca54e8f](https://github.com/qgis/QGIS/commit/ca54e8f8520453954e06e4d91adbd375287ddadd) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Corregir el fallo en la representación de las capas unidas | [#38551](https://github.com/qgis/QGIS/issues/38551) | [Commit ca00377](https://github.com/qgis/QGIS/commit/ca00377027dc7ae6066d8ca5fc3da35ad46dd7c2) | [Commit cdbf722](https://github.com/qgis/QGIS/commit/cdbf7224f716a7272e89239895ae254d2ee31bcd) |
| \[temporal\] Fix broken animations when a non-integer interval value is used (e.g. 1.5 hours) | no reportado | [Commit 81ec79c](https://github.com/qgis/QGIS/commit/81ec79c0e5d31f0e56413fdb01af320fbc00c564) |  |
| Corrección que permite la selección de atributos para el nombre de la capa DXF | [#42575](https://github.com/qgis/QGIS/issues/42575) | [Commit 66c6ef9](https://github.com/qgis/QGIS/commit/66c6ef96bcd4bcce4fa06cfc4ea62c87ac2898c9) |  |
| Fix papercut in rule based labeling widget where it\'s possible to uncheck BOTH the filter and else radio buttons | no reportado | [Commit 1fcb9752](https://github.com/qgis/QGIS/commit/1fcb97522c34d319c18bab13e4ccc64d6161bbef) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Fix it\'s impossible to change a rule based labeling \"else\" rule back to a normal rule | no reportado | [Commit de92ca0](https://github.com/qgis/QGIS/commit/de92ca034714452e8de139584518277092ea6c3c) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Corregir las propiedades definidas por los datos que se vinculan a un campo pueden tener valores incorrectos cuando el campo vinculado tiene un valor nulo | no reportado | [Commit 4e25c6b](https://github.com/qgis/QGIS/commit/4e25c6bcf413c8d93a09839696dbc93ae0e55f64) | [Commit 2a3bcc3](https://github.com/qgis/QGIS/commit/2a3bcc365d901c3d69270fd9c4a9a2165c2cbd31) |
| Corregir la transformación de coordenadas rota al exportar características a DXF | [#43449](https://github.com/qgis/QGIS/issues/43449) | [Commit 65c02e0](https://github.com/qgis/QGIS/commit/65c02e024a767ccc57283ec29a9c1b6d6ef8003f) | [Commit 044f6a1](https://github.com/qgis/QGIS/commit/044f6a1ec2d96314805ee9ab9be73d8d25e38597) |
| \[processing\] Don\'t show model child algorithm outputs as choices for multi-layer input parameters when running a model | [#41210](https://github.com/qgis/QGIS/issues/41210) | [Commit f4477b2](https://github.com/qgis/QGIS/commit/f4477b2cc4f29553ceb8c3d2d82139bc955ffd0c) |  |
| Ampliar la documentación de QgsPoint/QgsPointXY para aclarar cuándo debe utilizarse cada clase | [#43598](https://github.com/qgis/QGIS/issues/43598) | [Commit ae83444](https://github.com/qgis/QGIS/commit/ae83444c9f0c5ce8056ac7b282d6fb1dedc43ad4) |  |
| Corregir el fallo al cancelar la herramienta de unión | [#43553](https://github.com/qgis/QGIS/issues/43553) | [Commit b1f50bb](https://github.com/qgis/QGIS/commit/b1f50bbc2cefe593918b73af7d2b92ffac9b764d) | [Commit 1f25ba5](https://github.com/qgis/QGIS/commit/1f25ba5dbc58bc2f2efd1d930a6104110abe1569) |
| Fix \"force layer to render as raster\" setting wasn\'t correctly copied | [#43535](https://github.com/qgis/QGIS/issues/43535) | [Commit 1313786](https://github.com/qgis/QGIS/commit/131378650ff47f35588eed04162a7e2f2c728abf) | [Commit dcd016b](https://github.com/qgis/QGIS/commit/dcd016bace01506aa283aa7e6760ebe13bfa0d73) |
| Corregir un retroceso masivo de rendimiento en la tabla de atributos | no reportado | [Commit 5fdb88b](https://github.com/qgis/QGIS/commit/5fdb88bae3e40316a489d71594f17548f7a55f00) | [Commit 4970c3a](https://github.com/qgis/QGIS/commit/4970c3a9dbc66d1b2d155e3cdd07df200ee1c14a) |
| Fix performance issue when using attribute table with \"edited or new features\" filter in place | no reportado | [Commit af021f1](https://github.com/qgis/QGIS/commit/af021f10fb73d4850a0486527775e7fdc101ef47) |  |
| Corregir mensaje de error no válido cuando se crea una expresión para un elemento texto de composición | [#42884](https://github.com/qgis/QGIS/issues/42884) | [Commit db74013](https://github.com/qgis/QGIS/commit/db74013c7fc5966436fc41b3d912e93367bbec23) |  |
| Clarificar etiquetas en controlador temporal | no reportado | [Commit ed346d8](https://github.com/qgis/QGIS/commit/ed346d88fd3ebdf16839fa5b750dc92731cecfb6) |  |
| Redibujar correctamente el lienzo al aplicar cambios en las propiedades del proyecto | no reportado | [Commit 41f9842](https://github.com/qgis/QGIS/commit/41f98420e028c251cd0619242b5c1e8d01f5d41e) | [Commit 607b44b](https://github.com/qgis/QGIS/commit/607b44b1e0175a97c103eb7c04f2450c1ff924d3) |
| Make interactive labeling tools correctly work with data defined properties which aren\'t bound to fields | no reportado | [Commit c6bd366](https://github.com/qgis/QGIS/commit/c6bd366112f92e836dd071dd395f8b3dbf982d50) |  |
| Corregir el fallo en el etiquetado si la etiqueta tiene un conjunto de datos x/y definidos y se produce un error de proyección al transformar estas coordenadas | no reportado | [Commit 8943ac7](https://github.com/qgis/QGIS/commit/8943ac76d598f96c59d59a2ed530a972f07f89a1) | [Commit 2fe68cc](https://github.com/qgis/QGIS/commit/2fe68cc2f9c776f12fb94886d9c5d660a7d2a99f) |
| \[temporal\] Fix filter generation for vector temporal layers | [#38468](https://github.com/qgis/QGIS/issues/38468) | [Commit 544708f](https://github.com/qgis/QGIS/commit/544708f4aade5c4451463e045fd23c168552ab40) |  |
| Corregir el formato de los bloques de excepción en los documentos de PyQGIS | no reportado | [Commit 8359281](https://github.com/qgis/QGIS/commit/835928101213484c23f46e5c91b8329102478534) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| Corregir las estadísticas zonales no maneja correctamente las transformaciones de coordenadas | [#26858](https://github.com/qgis/QGIS/issues/26858) | [Commit e70cf8d](https://github.com/qgis/QGIS/commit/e70cf8da2747c13e02866bc940ce4dbb3af41815) | [Commit c82678d](https://github.com/qgis/QGIS/commit/c82678dd6136de79cd76206c9ca25b1f9e34abd2) |
| Don\'t assume that owslib \>= 0.20 is available | [#38074](https://github.com/qgis/QGIS/issues/38074) | [Commit 3cf9083](https://github.com/qgis/QGIS/commit/3cf9083743de2a72893d2efeddcfb29f3ea7130f) | [Commit eb1a55a](https://github.com/qgis/QGIS/commit/eb1a55a146d1dddb7ddf52da9c961e4c5a8cce96) |
| Corregir el fallo en el comprobador de geometría cuando se encuentran geometrías vacías | [#38983](https://github.com/qgis/QGIS/issues/38983) | [Commit 73a4948](https://github.com/qgis/QGIS/commit/73a49489c857ec492f62bb8ef0ec2494d93d368a) | [Commit 6938593](https://github.com/qgis/QGIS/commit/69385937d842cfa88ff65663591049ca210403b8) |
| \[temporal\] Fix incorrect frame duration in last frame in animation mode | [#40777](https://github.com/qgis/QGIS/issues/40777) | [Commit f76747b](https://github.com/qgis/QGIS/commit/f76747b8b1ffd93844767ad9b66e3601b96a98a2) |  |
| Default to a time range of the last 24 hours, in 1 hour increments, instead of a confusing \"zero length\" range | [#40868](https://github.com/qgis/QGIS/issues/40868) | [Commit 5f5a3a7](https://github.com/qgis/QGIS/commit/5f5a3a7e46fac5a4939d90f2eaf57a8b61008789) |  |
| Arreglar el restablecimiento de los campos temporales si previamente no se ha establecido ningún valor | [#43643](https://github.com/qgis/QGIS/issues/43643) | [Commit 9de5d25](https://github.com/qgis/QGIS/commit/9de5d2500bd358c1214b17434424d1c301444b03) | [PR #43235](https://github.com/qgis/QGIS/pull/43235) |
| \[processing\] Fix broken execution of models via browser/drag and drop | [#43698](https://github.com/qgis/QGIS/issues/43698) | [Commit cbe2678](https://github.com/qgis/QGIS/commit/cbe2678e34767f01dd3d2578261c4e55e40a00ba) | [Commit 9e0cdcb](https://github.com/qgis/QGIS/commit/9e0cdcba48de04a3fb3a6aa81276e68a0447a6fd) |
| Corrección QgsDistanceArea.bearing() | no reportado | [Commit 0b499d3](https://github.com/qgis/QGIS/commit/0b499d3a0058dbb234ce54f6329015818a9ccde7) |  |
| Don\'t restrict adding crs selections to list of recent CRSes to only a few select dialogs | no reportado | [Commit 870945c](https://github.com/qgis/QGIS/commit/870945c476c1a429eb410af2a793644a7b1db85f) |  |
| \[processing\] Fix use of data defined parameter values when editing features in place | [#43758](https://github.com/qgis/QGIS/issues/43758) | [Commit 3ae9625](https://github.com/qgis/QGIS/commit/3ae96253de7efc5e8921e776ae91de4b9281d90c) |  |
| \[layouts\] Fix bounding rectangle for shapes doesn\'t include stroke width after loading from xml | [#43748](https://github.com/qgis/QGIS/issues/43748) | [Commit fad1800](https://github.com/qgis/QGIS/commit/fad18003b3560e6daa1c47080f5b2fe10ddef9e6) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
