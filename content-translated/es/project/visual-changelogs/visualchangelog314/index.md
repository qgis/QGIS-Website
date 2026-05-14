---
HasBanner: false
draft: false
releaseDate: '2020-06-19'
section: proyecto
sidebar: true
title: Registro de Cambios para QGIS 3.14
type: visual-changelog

---
{{<content-start >}}
# Registro de Cambios para QGIS 3.14{#changelog314 }
![image1](images/splash.jpeg)

Fecha de lanzamiento: 2020-06-19

Another awesome release in the trail of great QGIS releases we have made across 18 years of development. This release is so jam-packed with new features and improvements big and small, it is hard to know where to start. Some of the marquee features include vector tile support, huge advances in mdal / mesh support, native support for temporal data in WMS-T, PG Raster, vector providers, and mesh layers. Users focussed on cartography and digitising haven\'t been left out either, with many new options for you!

**Gracias**

We would like to thank the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## General
### Funcionalidad: Nueva configuración para la fuente de las anotaciones de la decoración de la malla
Annotations for the map canvas\' grid decoration are now fully customizable including font color, buffer, etc.

![image8](images/entries/14b7cf800ef293ac3ea3f00d12a30022876e713c.webp)

Esta funcionalidad fue financiada por iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Temporal
### Funcionalidad: Configuración del rango temporal acumulativo en el controlador temporal
Añade un ajuste en el controlador temporal para establecer el rango de animación temporal a acumulativo. Esto significa que todos los fotogramas tendrán la misma fecha-hora de inicio pero diferentes fechas y horas finales.

This is useful is you wish to accumulate data in your temporal visualisation instead of showing a \'moving time window\' across your data.

![image2](images/entries/90da13821bfde46aa6d9d951fb9a31bf27d85656.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Feature: Add a new \"Redraw Layer Only\" mode for temporal vector layers
Cuando se establece en este modo, la capa se redibujará automáticamente cada vez que se cambie el rango temporal, pero no se aplicará un filtrado basado en el tiempo a las entidades.

Esta configuración es útil cuando la capa tiene configuraciones de simbología que varían según el rango temporal. Por ejemplo, cuando una capa está utilizando expresiones de renderizador basadas en reglas dependientes del tiempo o expresiones de simbología definidas por datos.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Añadir soporte de manejo básico temporal para capas vectoriales
Esto expone algunas capacidades temporales nativas básicas para capas vectoriales:
- Rango de tiempo estático para la capa (para que coincida con las posibilidades de la capa ráster), esto establece un rango de tiempo estático único que se aplica a toda la capa. Todas las entidades de la capa se mostrarán siempre que el tiempo del lienzo se superponga al rango de tiempo de la capa
- \"Single field with DateTime\": Allows selection of a single Date or DateTime field from the layer. Features will be shown whenever this field value is within the canvas time range
- \"Separate Fields for Start and End Date/Time\": Allows selection of start and end Date/DateTime fields from the layer. Features will be shown whenever the time interval calculated from these fields overlaps the canvas time range

We should consider extending this in future, e.g. to add modes like \"start time + fixed duration\", \"start time + duration from field\", \"start and end time via expressions\", etc.

Algunas limitaciones/ineficiencias conocidas:
- Actualmente solo se pueden usar los campos Fecha/Fecha y hora. Esto se hizo para simplificar el manejo del formato y evitar la necesidad de preocuparse por los campos de cadena con diferentes formatos de fecha y hora. En el futuro, deberíamos permitir la selección de campos de cadena y permitir a los usuarios ingresar una cadena de formato de fecha y hora personalizada
- Unlike the Time Manager plugin approach, the approach taken here is to rely completely on QGIS expressions and feature requests to do the filtering (Time Manager uses layer filter strings and attempts to set a native SQL filter syntax so that filtering is done on the backend). This is intentional because it provides a unified filter approach regardless of the provider used (i.e. we don\'t need to worry about the different SQL syntaxes used natively by the different providers). The beauty of feature request expression compilation **should** mean that the QGIS expressions are magically turned into native backend queries, BUUUUUUUUUUUT\... because we lack QGIS expression support for DateTime literals, we currently rely on the \"to_datetime\" expression function and coerce everything through strings. None of the expression compilers handle this function, so currently \*all\* filtering is done on the QGIS side. We need to add functions for optimised DateTime literal creation and then ensure that the different compilers correctly map these literals across to the backend filter syntax to allow all the filtering work to be done on the database side\...

Entonces, actualmente, el rendimiento es mucho peor con capas grandes en comparación con el Administrador de Tiempo (y el conjunto de entidades expuestas es más pequeño, por ejemplo, sin manejo de interpolación), pero la ventaja es que podemos usar el marco temporal nativo y tener capas vectoriales animadas junto con malla y ráster ¡capas!

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Soporte de API Temporal de Ráster Postgres
Añadida integración de capacidades temporales para rasters Postgres

![image3](images/entries/78421839-37e3d100-765b-11ea-83e5-e7e3e519155e.webp)

![image4](images/entries/a8347da9570ae597bc17e23236e4eb4d57efb1d1.gif)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Funcionalidad: Ajustes de proyecto temporal QGIS
Esta funcionalidad añade la funcionalidad de configuración temporal del proyecto

You will be able to set the project temporal range either by using manual input or by calculating it from the current project\'s temporal layers. The latter can be done by clicking the provided \"Calculate from Layers\" button.

Esta implementación prepara el escenario para agregar una función de animación para capas temporales en QGIS.

Here\'s an example of setting the project temporal range. ![image5](images/entries/74980472-93f2ed00-5441-11ea-8765-f35d1f69b144.gif)

Prior discussions about QGIS temporal support can be found [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/161) and [here](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/128).

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Funcionalidad: Soporte de restricciones temporales a capas WMS-T
Esta funcionalidad añade la habilidad para restringir capas WMS Temporales (WMS-T) dentro de QGIS. Será capaz de restringir el rango de FechaHora para cualquier capa temporal desde proveedores WMS-T.

Esta implementación permite al usuario especificar el rango de FechaHora requerido en la capa desde la pestaña de origen en el diálogo de propiedades de la capa.

Below is an example of the workflow. ![image6](images/entries/74638436-ee0f5c00-517c-11ea-938e-cec23c61ba29.gif)

**Nota:** *Para solicitudes de punto en el tiempo instantáneo, al especificar un rango con igual fecha de inicio y finalización, se utilizará el instante de fecha y hora especificado y no un rango.*

![image7](images/entries/b86eea9111e33e6aea345b0e0759de48eaceade9.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
### Funcionalidad: API Temporal
Esta funcionalidad proporciona una implementación API para soporte temporal en QGIS.

You can find the API for Python by searching for \'Temporal\' in the python docs ([link](https://qgis.org/pyqgis/master/search.html?q=Temporal&check_keywords=yes&area=default)).

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Kartoza / Samweli Mwakisambwe](https://kartoza.com)
## Herramientas de mapa
### Funcionalidad: Soporte de Herramienta de Identificación para capas de teselas vectoriales.
El herramienta de mapa identificar ahora es capaz de inspeccionar atributos de entidades en teselas vectoriales.

![image9](images/entries/79157425-d3501100-7dd4-11ea-8395-5c8ff1dce449.webp)

This feature was funded by [Many funders](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Mostrar un menú al lado de los botones del widget de escala, para permitir ajustar el widget directamente a una escala desde un diseño de impresión de mapa
Una captura de pantalla dice miles de palabras:

![image10](images/entries/78198825-34bada80-74cd-11ea-803a-90afea085b38.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add tool button to \"Deselect Features from the Current Active layer\"
![image11](images/entries/76692569-26616780-6661-11ea-9071-fd4c712860db.gif)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Interfaz de usuario
### Funcionalidad: Permitir el arrastre y soltado de una capa en varias instancias de QGIS
![image12](images/entries/77666018-b5834f00-6f80-11ea-971e-c6d7d996d37d.gif)

This feature was funded by [QGIS Swiss user group](https://www.qgis.ch)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Abrir tablas de Atributos como pestañas
If the option \"Open new attribute tables as dock windows\" is active, new attribute tables will be opened as tabs on top of existing attribute tables.

![image13](images/entries/80049561-d8017d00-84d8-11ea-826e-d7092ac7a5c6.gif)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## Simbología
### Funcionalidad: Representador de Contorno de Capa Ráster
Este nuevo representador dibuja líneas de contorno que se calculan sobre la marcha desde la banda ráster de origen. Es posible establecer el intervalo de las líneas de contorno y el símbolo utilizado para dibujar.

In addition there is support for \"index contours\" - contour lines with higher intervals, typically drawn with a wider line symbol.

If we generate contour lines on input raster blocks with the same size as our output raster block, the generated lines would contain too much detail. This detail can be reduced by the \"downscale\" factor - this will request lower resolution of the source raster.

![image14](images/entries/77861880-17111b00-7218-11ea-95ba-410c97830b93.webp)

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### Funcionalidad: Agregar la unidad de tamaño porcentual para la simbología de capa de Marcador de Imagen Ráster y relleno Raster
According to the [Feature Request](https://github.com/qgis/QGIS/issues/30057) this patch adds a new percentage (of original image size) value for size units of **Raster Image Marker** and **Raster fill** (by [nirvn](https://github.com/qgis/QGIS/pull/34869#issuecomment-595090465) suggestion) layers.

Por ejemplo una capa contiene imágenes ráster de varios tamaños y relaciones de aspecto:

![image15](images/entries/77845535-6e3fcd00-71d1-11ea-8760-b477e75f7a3a.webp) ![image16](images/entries/77845539-726bea80-71d1-11ea-9512-0a8e6cde7b3c.webp)

Si usamos una **unidad de tamaño** de marcador de imagen Ráster existente verá algo como esto (con un cocodrilo normal, pero una gran jirafa):

![image17](images/entries/77846711-bfec5580-71d9-11ea-9afe-a52af9b2784e.webp)

o como esto (con una jirafa normal pero un minúsculo cocodrilo):

![image18](images/entries/77846764-1eb1cf00-71da-11ea-9d6d-f468708ea726.webp)

El nuevo valor de **porcentaje** de unidades de tamaño está tratando de solucionar este problema.

Both unit tests \"qgis_rasterfilltest\" and \"qgis_rastermarkertest\" were rewritten with a set of new control images for testing the proposed **percentage** value of size units.

This feature was developed by [beketata](https://api.github.com/users/beketata)
### Funcionalidad: Añadir propiedades definados por datos a la familia/estilo de fuente para marcadores de fuente
Data-defined properties were added for the font markers\' font family and the brand new font style properties. This can come in handy for a number of scenarios, including multilingual context where a data-defined property can avoid duplicating datasets.

![image19](images/entries/1ded1a8bbec9eeebafad96b7616e963847961e14.webp)

Esta funcionalidad fue financiada por iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Funcionalidad: Configuración de Nuevo estilo de fuente  para marcadores de fuente
Con esta nueva configuración de estilo de fuente, los usuarios pueden elegir un estilo no predeterminado de familias de fuentes que antes no estaban disponibles.

![image20](images/entries/e387c3745d49a36116908dffc1126befae7d1b1f.webp)

Esta funcionalidad fue financiada por iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Etiquetando
### Funcionalidad: Respetar colores HTML en etiquetas
Habilitada, esta opción tratará el contenido de la etiqueta como HTML, y cualquier opción de formato html RELACIONADA CON COLORES DEL PRIMER PLANO se respetará en la etiqueta representada.

Note: ONLY HTML COLOR TAGS ARE RESPECTED. This is NOT a bug, rather this feature has been designed as a \"test of the waters\" with HTML formatting in labels, and accordingly only formatting options which do not alter the font shape were considered.

En el lado positivo, funciona correctamente con TODAS las demás configuraciones de etiquetas, incluidas sombras, buffers, etiquetas curvas, etc.

Ahora alguna imágenes bonitas:

![image21](images/entries/81377287-84359b80-9148-11ea-95f4-9d7917d62cf9.webp)

![image22](images/entries/81377294-88fa4f80-9148-11ea-9036-2a597b064bbc.webp)

This feature was funded by [geoProRegio AG](http://www.geoproregio.ch)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Emplazamiento automático de etiquetas fuera de polígonos
Esta funcionalidad añade la habilidad de ubicar automaticamente etiquetas fuera de entidades poligonales.

Esto se expone de varias maneras:
1. A new placement mode which always places polygon labels for the layer outside the features: ![image23](images/entries/80680381-faf7e680-8b01-11ea-8612-b0f543bfd943.webp) ![image24](images/entries/80680391-00553100-8b02-11ea-8e56-21b57964f765.webp)
2. When using other polygon placement modes, a new checkbox \"Allow placing labels outside of polygons\" can be checked to allow labels to be placed outside when it isn\'t possible to place them inside the polygon: ![image25](images/entries/80680478-30043900-8b02-11ea-8bd5-3325fc0a5021.webp) ![image26](images/entries/80680488-37c3dd80-8b02-11ea-98bb-e0882e6ab9ab.webp)

The \"allow placing labels outside\" checkbox can be data defined, allowing users to either allow outside labels, prevent outside labels, or force outside labels on a feature-by-feature basis.

The placement algorithm is based on a modification of Rylov & Reimer (2016) \"*A practical algorithm for the external annotation of area features*\". While Rylov & Reimer propose a horizontal sweep-line based approach for selection of candidate label points, in practice I found that this delivered inferior results (and was slower) then just traversing the exterior ring of the polygon and generating candidate point at regular intervals (especially for narrow, nearly horizontal polygons).

As shown in the islands screenshot above, the outside placement mode works as expected with the \"Follow label placement\" multiline alignment mode.

This feature was funded by [Swiss QGIS user group](https://www.qgis.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Capa vectorial teselada - parte 4 (etiquetando)
Continuado el trabjo en la implementación de capa vetorial teselada.

This adds labeling support for vector tile layers. So far this is just working on qgis_core\... GUI support will come next. Labeling uses the same concepts as the rendering of vector tiles: we have a list of labeling styles, each one is defined by sub-layer name, geometry type, filter expression, zoom range and of course label style configuration (QgsPalLayerSettings).

Note there is a \"chicken-and-egg problem\" with labeling: For vector tiles, we create QgsFields for a sub-layer based on fields that renderer and labeling request, but with labeling it was impossible to get required fields if they were not already available in the expression context (hence some small additions to QgsProperty, QgsPropertyCollection, QgsPalLayerSettings to be able to get required field names by not preparing internal expressions at the same time).

![image27](images/entries/78723460-bf676380-792b-11ea-9cab-a6732e20033a.webp)

An example how to set the above labeling in Python console:

    s = QgsVectorTileBasicLabelingStyle()
    s.setLayerName("place")
    s.setGeometryType(QgsWkbTypes.PointGeometry)
    s.setFilterExpression("rank = 1 AND class = 'country'")
    ls=QgsPalLayerSettings()
    ls.drawLabels=True
    ls.fieldName="name"
    ls.placement = QgsPalLayerSettings.OverPoint s.setLabelSettings(ls)
    labeling = QgsVectorTileBasicLabeling()
    labeling.setStyles([s])
    iface.activeLayer().setLabeling(labeling)
    
This feature was funded by [Many funders](https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Añadir control sobre la anchura de punto para llamada en la eetiqueta
Esto les da a los usuarios control sobre dónde debe unirse una llamada al texto de la etiqueta (anteriormente, solo tenía control sobre dónde se uniría la llamada a la geometría de entidad correspondiente).

Como elecciones se incluyen:
- Punto mas cercano (comportamiento previo)
- Etiqueta en centroide
- Fijado en esquinas: Superior izquierda / superior derecha / inferior izquierda / inferior derecha / etc.

Control definido por datos sobre la anchura de la etiqueta si es posible.

¡Ayuda a corregir la fealdad de las llamadas!

Resultado previo (modo punto mas cercano):

![image28](images/entries/76173692-5a660400-61ed-11ea-87dd-74a4db5cf0ce.webp)

With new \"centroid\" placement:

![image29](images/entries/76173706-6d78d400-61ed-11ea-89c1-ce4e2477dfef.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Malla
### Funcionalidad: Usar solo grupo de conjunto de datos especificado
Esta funcionalidad permite al usaurio elegir los grupos del conjunto de datos que son usados. Esto puede hacerse en el diálogo de propiedades de capa de malla en la pestaña fuente.

Una nueva vista de árbol muestra todos los grupos del conjunto de datos disponibles en el proveedor de datos. Los grupos del conjunto de datos pueden ser marcados/desmarcados y renombrados.

Este widget también proporciona botones para cargar conjuntos de datos extra desde archivos, para expandir/contraer el árbol, para marcar/desmarcar todos los elementos y para resetear los preestablecidos desde el proveedor (por ahora, solo el nombre original).

Solo los grupos de conjuntos de datos marcados serán mostrados en el widget de conjunto de datos activo en los ajustes del representador.

![image30](images/entries/81516813-3a46e400-9307-11ea-9621-a27d5a8c86f2.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Ajuste de color escalar basado en clasificación
Con esta característica, MDAL lee valores escalares clasificados en el conjunto de datos. Cuando os valores están clasificados, la configuración de representación escalar predeterminada tiene el sombreador de rampa de color y las etiquetas establecidas de acuerdo con los valores clasificados.

![image31](images/entries/81480226-42fbc500-91f6-11ea-91fd-3d430693d551.webp)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Ajuste de elementos en malla
Añade un método a la API para ajustar elementos en la malla.

Este método devuelve la posición del punto ajustado en el elemento de malla mas cercano:
- Para un vértice, la posición ajustada es la posición del vértice
- Para una arista, la posición ajustada es el punto proyectado en la arista, o la extremidad de la arista si es fuera de la arista
- Para una cara, la posición ajustada es el centroide de la cara

La posición devuelta es en coordenadas del mapa

![image32](images/entries/f11b278c71fecee8445ff29077bfddef543b564d.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: variando la anchura/color de malla 1D 
Esta funcionalidad proporciona una nueva forma de renderizar una malla 1D con anchos de borde que pueden variar según el valor. Entonces, el ancho y el color varían según el valor en los bordes o en los vértices.

El usuario puede definir un valor min/max y una anchura min/max para establecer la representación.

Para el color, el usuario puede definir un sombreador de rampa de color (como para la malla 2D y la trama).

Para esta nueva representación, nuevas clases genéricas son introducidas que podrían usarse fuera del marco de trabajo de la malla.

![image33](images/entries/80013358-bb475400-849c-11ea-95c8-71b04382a927.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Soporte para mallas múltiples (desde MDAL 0.5.91)
Además de actualizar a MDAL 0.5.91, esta funcionalidad permite cargar varias mallas desde un archivo.

El archivo se analiza y se inicia un diálogo de subcapa usando la misma lógica que para las capas vectoriales o ráster.

![image34](images/entries/78789841-b1413380-797b-11ea-9c7b-f31cb9756809.gif)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Característica: Conecte la capa de malla al marco temporal QGIS
![image35](images/entries/77872855-31e29000-7216-11ea-80fb-82e351dbb4a2.gif)
#### Manejo de tiempo en la capa de malla
El tiempo en una capa de malla está definida por:
- Una hora de referencia proporcionado por los datos, el proyecto o el usuario
- Cada conjunto de datos está asociado a tiempos relativos
- La extensión de tiempo está definida por la primera y última horas de todos los conjuntos de datos

```
    Reference time :          AT
    Dataset 1 time            o---RT------RT-----RT-----------RT
    Dataset 2 time            o-------RT------RT--------RT
    Dataset 3 time            o--------------------------RT-------RT------RT
    Time extent of layer      o----<---------------------------------------->

    -  AT : absolute time (QDateTime)
    -  RT : relative time (qint64)
```
La clase **QgsMeshDataprovidertemporalCapabilities** almacena el tiempo de referencia proporcionado por los datos y todos los tiempos relativos del conjunto de datos. Esta clase tiene la capacidad de devolver el índice del conjunto de datos desde el índice de un grupo de conjunto de datos y una hora relativa desde la hora de referencia. La hora de referencia (que puede ser diferente de la hora de referencia del proveedor) y la extensión de hora absoluta se almacenan en la clase **QgsMeshTemporalProperties**

The temporal settings in the properties widget are only the reference time and the provider time unit: ![image36](images/entries/77871643-bf23e580-7212-11ea-9b92-82c906c19c22.webp)

La referencia de tiempo predeterminada de la capa es establecida por (orden de prioridad):
- Desde el proveedor de datos si es definido por datos
- Desde el proyecto si es definido
- Desde la fecha actual con hora 00h00

El usuario puede cambiarlo si quiere.
#### Principios de Representación
The 2D and 3D renderers access the active dataset index from the layer with the time range stored in the `QgsContextRenderer` and in the `Qgs3DMapSettings` : Relative time is calculated as the difference between the time range of `QgsContextRenderer` and the reference time stored by `QgsMeshTemporalProperties`. The dataset index comes from the `QgsMeshDataproviderTemporalCapabilities` that maps the relative time with dataset index.

Los datos provienen del proveedor con el índice del conjunto de datos.
#### Conjunto de datos estático
There is also the option to set a static dataset, that is to choose a dataset that will be rendered independently of the QGIS time controller. To do that the user can check the check box at the bottom of the temporal page of the properties widget: ![image37](images/entries/77871772-20e44f80-7213-11ea-8988-a51ec78c1320.webp) For now, as it was simpler to implement and allows the required dataset to be chosen directly, the user can independently choose scalar dataset and vector dataset from combo boxes with the time associated for each dataset (relative time for data without reference time). If required, a unique time could be implemented but that could lead to inconsistent results with non synchronous datasets. The static dataset settings are in the temporal page but can be easily put in the source page if wanted.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Remuestreo de valores de vértice a valores nominales
El remuestreo está disponible para conjuntos de datos definidos en caras, p.ej. el valor en los vértices es calculado a partir de los valores en las caras.

Esta funcionalidad implementa el remuestreo desde valores en vértices a valores en las caras usando el método del promedio de vecinos.

The default method is set to \"none\" for resampling from vertices to faces and to \"neighbor average\" for resampling from faces to vertices. Then the default rendering is always smooth. ![image38](images/entries/77320848-acc41c00-6ce7-11ea-85af-2bff553ecbb5.gif)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Coloreando conjunto de datos vectoriales de malla con rampa de sombreado de color
Esta funcionalidad permite al usuario colorear el conjunto de datos de malla vectorial (flecha, lineas de corriente, trazos) con la rampa de sombreado de color dependiendo de la magnitud del vector.

![image39](images/entries/77156534-ed1c6380-6a75-11ea-8b97-a13d3ea27ede.webp)

![image40](images/entries/77156669-2c4ab480-6a76-11ea-9209-d0144fbfc3f0.webp)

![image41](images/entries/77156736-5bf9bc80-6a76-11ea-827b-bb55ce52b814.webp)

This feature was funded by [Deltares](https://www.deltares.nl/en/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Guardar estilo para capa de malla
Esta funcionalidad añade la opción de guardar un estilo de capa de malla en un archivo qml, como se utilizó con capas vectoriales y ráster.

The feature also refactors the raster and vector layer properties menu style. ![image42](images/entries/76421493-1fdda200-637a-11ea-9e4b-71a596b18dd9.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Representador de Malla 1D
Update to [MDAL 0.5.90](https://github.com/lutraconsulting/MDAL/releases/tag/0.5.90)

Initial implementation of [Support of 1D elements in Mesh Layers](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/164)

Las mallas 1D consisten en vértices y bordes. Un borde conecta dos vértices y puede tener datos asignados (escalares o vectoriales) en él. La red de malla 1D puede, por ejemplo, usarse para modelar un sistema de drenaje urbano.

There are new options to display 1D mesh (edges) in the mesh frame tab ![image43](images/entries/75885078-2aea7c80-5e26-11ea-8435-eef74afce7b7.webp)

También para los datos en malla 1D (bordes o vértices) hay nuevas opciones en la pestaña de contornos

![image44](images/entries/75885122-3b9af280-5e26-11ea-96a3-f4a4e48c040e.webp)

Note que no todas las funcionalidades disponibles para mallas 2D están disponibles, notáblemente
- Soporte para Calculadora de Malla para mallas 1D
- Representación 3D de mallas 1D
- Identificar y trazar en Crayfish (se agregará más adelante en el siguiente PR)

Algunas funciones no son necesarias para mallas 1D, especialmente
- Esportación de contornos de malla

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Funcionalidad: Simplificación de malla
Como una capa de malla podría tener millones de triángulos, el representado puede ser muy lento, especialmente porque todos los triángulos se muestran en la vista, incluso cuando los triángulos son demasiado pequeños para ser vistos.

Para esas situaciones, esta característica proporciona una opción para simplificar la malla. La simplificación conduce a una o más mallas simplificadas que representan niveles de detalle. Al renderizar la malla, se elige el nivel de detalle apropiado para proporcionar una representación adecuada según la vista.

Una nueva pestaña en el widget de propiedades de capa de malla le permite al usuario cambiar los ajustes :
- El factor de reducción se usa para simplificar una malla; El número de triángulos para cada nivel de detalle es aproximadamente igual al número de triángulos del nivel de detalle anterior, dividido por el factor de reducción
- Resolución de malla máxima: este es el tamaño promedio (en píxeles) de los triángulos que se pueden mostrar; Si el tamaño promedio de la malla es inferior a este valor, se muestra una malla con un nivel de detalle más bajo, es decir, una malla con un tamaño promedio apenas mayor que la resolución de malla máxima.

![image45](images/entries/74750757-9e936380-5242-11ea-98cf-a0e3e6694831.webp)

This feature allows the speeding up of rendering as shown in these tables (result in milliseconds) : ![image46](images/entries/74750903-d69aa680-5242-11ea-9be3-0af7b2beacaf.webp)

Demo GIF Before: ![image47](images/entries/74751034-0cd82600-5243-11ea-8a02-de78a337f299.gif)

After: ![image48](images/entries/74751042-12357080-5243-11ea-80cb-2a3217d03a78.gif)

This feature was funded by [BMT](https://www.bmt.org/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Objetos 3D
### Funcionalidad: Flechas para representación de conjuntos de datos de capa de malla 3D
Esta funcionalidad agrega una opción para mostrar flechas en una entidad 3D de conjunto de datos de capa de malla, dependiendo del conjunto de datos de vector.

El conjunto de datos utilizado para representar las flechas es el elegido para representar vectores en la representación 2D.

Del mismo modo, el color de las flechas se define en la configuración de representación 2D para el conjunto de datos vectoriales.

En la configuración 3D, el usuario puede definir el espaciado de las flechas y si el tamaño es fijo o escalado en magnitud.

This spacing setting also defines the maximum size of arrows because arrows can\'t overlap. ![image49](images/entries/76225819-6a80e200-61f3-11ea-88da-43e70c358530.webp)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Diseño de impresión
### Característica: Configuración temporal para elementos del mapa de diseño
Esta característica añade una sección plegable al widget del elemento del mapa de diseño que permite a los usuarios habilitar y establecer un rango temporal para usar al representar el contenido del mapa.

El valor de inicio y final de fecha y hora para ser definido por los datos, lo cual es útil cuando se usa junto con las características del atlas.

![image50](images/entries/265d07738c1cec8a398ce5503330a520f98d4526.gif)

Esta funcionalidad fue financiada por iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Funcionalidad: Posibilidad de ordenar la tabla de atributos por campo no listado en la tabla
En lugar de utilizar el mismo modelo de datos para las columnas visualizadas y de clasificación, ahora se utilizan dos modelos de datos. Usan las mismas clase API/base ya que son muy similares.

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Mostrar el control sobre el comportamiento de división de la leyenda de capas capa-por-capa
This allows users to manually override the legend\'s default setting for \"split layers\" on a layer-by-layer basis, by double clicking a layer in the layout legend panel and choosing whether that layer:
- Sigue la configuración de leyenda predeterminada para dividir
- Can ALWAYS be split over multiple columns (regardless of the legend\'s setting)

o
- Can NEVER be split over multiple columns (regardless of the legend\'s setting)

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir la personalización de los símbolos de división y subdivisión diferente al símbolo horizontal de la barra de escala
Permite diseñar símbolos de división y subdivisión de una manera diferente en comparación con el símbolo de línea horizontal en una barra de escala

Patrocinado por SLYR

Builds off the hard work done by \@agiudiceandrea!

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Característica: Permitir anular el símbolo predeterminado para un nodo de leyenda
This allows users to (optionally) customise the symbol appearance for a legend node, e.g. to tweak the colors or symbol sizes to better provide a \"representative\" patch symbol compared with how those corresponding features actually appear on the map.

It\'s useful for exaggerating symbol widths, or for manually tweaking the colors of semi-transparent symbols so that the colors represent the actual appearance of the symbols when rendered on top of the map content. Or to tweak the marker interval/offset in marker lines so that the markers are nicely spaced in the legend patch.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir el emplazamiento manual de saltos de columna en leyenda
Añade la opción al configurar un elemento de leyenda para insertar un salto de columna antes del elemento, provocando que este sea ubicado en una nueva columna.

This allows user control over the column content, for cases when the automatic column generation doesn\'t result in the desired results.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Añadir subdivisiones en segmentos en la parte derecha de la barra de escala
Añade la habilidad para crear subdivisiones en segmentos en la parte derecha de la barra de escala.

Line Ticks Up ![image51](images/entries/80860629-47116b00-8c69-11ea-83d8-61f27cb77e68.webp)

Line Ticks Middle ![image52](images/entries/80860663-6c9e7480-8c69-11ea-94a3-8d0e8544867d.webp)

Line Ticks Down ![image53](images/entries/80860675-7b852700-8c69-11ea-984d-584eff1e3c95.webp)

Scalebar item properties - Segments groupbox ![image54](images/entries/81009703-653bbe80-8e55-11ea-9286-4850b32edb23.webp)

El comportamiento referente a los segmentos del lado izquierdo de la barra de escala no cambia.

This feature was developed by [Andrea Giudiceandrea](https://api.github.com/users/agiudiceandrea)
### Característica: Permitir anular el tamaño del parche de leyenda por elemento
Permite a los usuarios inhabilitar el tamaño del parche de símbolo para nodos de leyenda individuales, haciendo doble-click en el nodo

Width and height can be individually overridden, with the node falling back to the default width or height when the override isn\'t set.

Sponsored by SLYR ![image55](images/entries/80325577-0edce780-8879-11ea-82bd-8f323a4c68ab.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir control sobre el espaciado horizontal antes de grupo/subgrupo/símbolos de leyenda
Gives flexibility to allow \"nesting\" legend groups/subgroups/symbols and much greater control over legend item placement.

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Administrar formas de parches de leyenda mediante el administrador de estilo
Esta actualización finaliza el trabajo reciente de personalización de formas de parches de leyenda, al agregar soporte para formas de parches de leyendas personalizadas al administrador de estilos.

¡Ahora solo necesitamos un buen conjunto de formas de parche predeterminadas a enviar!

![image56](images/entries/79927419-0c4a4e80-8483-11ea-9b87-7ed8b393d349.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: permite configurar formas de parches de leyenda haciendo doble clic en elementos de leyenda
Permite a los usuarios establecer formas de parches de leyenda personalizadas para los elementos al ingresar una cadena WKT que representa la geometría del parche.

Patrocinado por SLYR

![image57](images/entries/79714030-ea31be80-8312-11ea-8b6f-f40e3eea04b1.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Admite pegar imágenes directamente en diseños
Incrusta la imagen pegada en el diseño.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir que los elementos de marcador sincronicen su rotación con los mapas
Esto permite la creación de flechas de norte desde símbolos de marcador, mostrando las mismas opciones que existen para elementos de imagen actuando como flehas de norte.

Cuando un marcador actúa como una flecha hacia el norte, la rotación del mapa se AGREGA a cualquier rotación de símbolo de marcador existente (por ejemplo, si tiene que girar el marcador de triángulo un 90% para que apunte hacia arriba, ¡funcionará bien en el modo de flecha hacia el norte!)

![image58](images/entries/78468312-2c2b0400-775a-11ea-926e-2acf7ec15aa4.webp)

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Nuevo tipo de elemento para símbolos de marcador
Permite colocar símbolos de marcador directamente en diseños, p.ej. para colocar marcadores manualmente sobre un elemento del mapa o para crear leyendas personalizadas avanzadas.

Anteriormente tenía que hackear el soporte para estos, p.ej. dibujando rectángulos usando símbolos de relleno centroide. Es mucho mejor tener un tipo de elemento dedicado a él, lo que permite opciones de personalización más específicas (¡próximamente!)

Patrocinado por SLYR

![image59](images/entries/78419618-c885d580-768a-11ea-959a-8459e19e05df.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Agregar contenido de importación desde el portapapeles para elementos de tabla fijos
A new import content from clipboard feature has been added to QGIS\' table editor to enable quicker layout fixed table item editing and creation.

![image60](images/entries/e7f2b64e48b0726bc03e2d4fa9424feabde1808d.gif)

Esta funcionalidad fue financiada por iMHere Asia

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Feature: Add numeric formatter \"fraction\" style
This style represents decimal numbers as vulgar fractions, e.g. \"3/4\" instead of 0.75.

Options include using Unicode superscript and subscript characters for nicer typography, e.g. ¹⁷/₂₃ (this is the default mode, disabling this option uses the \"17/23\" format). An option also exists for using dedicated unicode characters for specific fractions (where a unicode character exists), e.g. ½ or ¾.

Ultimately this allows for creation of scalebars with fractional representations of distances, e.g. 0 \-\-\-\-- ½ \-\-\-\-- 1 km (instead of 0 \-\-\-\-\-- 0.5 \-\-\-\-\-- 1km)

Patrocinado por SLYR

![image61](images/entries/77267662-0c71f580-6cef-11ea-9956-917e1d6ef496.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"stepped line\" and \"hollow\" scalebar styles
Agrega dos nuevos estilos de barra de escala (que están disponibles en ArcMap, pero que antes eran imposibles de reproducir en QGIS)

Estilo Línea Escalonada:

![image62](images/entries/77247015-c1b59680-6c78-11ea-92a9-7bbb2ba8638a.webp)

Hollow (aka \"South African\") style:

![image63](images/entries/77247024-dc880b00-6c78-11ea-827a-344645cec248.webp)

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: permitir que el estilo de línea de la barra de escala se establezca utilizando símbolos de línea QGIS
En lugar de la configuración anterior de los colores de línea de barra de escala/ancho/estilos de tapa, ahora exponemos la opción como un símbolo de línea completa para un estilo más avanzado.

Además alguna depuración de código.

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Característica: Vuelva a trabajar la interfaz de usuario y el comportamiento del elemento
Adds an explicit choice between SVG or raster image sources, which allows us to clean up the configuration panel for layout pictures by hiding options which don\'t apply to a certain picture source. Also permits us to:
- Reutilizar el widget árbol selector estándar SVG, que carga imágenes en un hilo de fondo
- Usa el estándar SVG y la edición de la línea del selector de imagen, que permite arrastrar y soltar imágenes y expone opciones para insertar imágenes y enlazar a fuentes en linea

En última instancia esto está motivado por el deseo de permitir los usuario insertar imágenes en diseños y plantilla de diseños

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Hacer CRS controlable por una variable
Esto hace al CRS del Mapa controlable por una variable.

![image64](images/entries/74844265-348ac500-52fb-11ea-9198-78f4f9022ac1.webp)

Referente a #34547

This feature was developed by [Alex](https://api.github.com/users/roya0045)
## Expresiones
### Prestación: Nuevas expresiones
- `ascii`
- `make_interval` Allows direct construction of interval values from years/months/weeks/days/hours/minutes/second values, without having to construct a string representation of the interval first
- `maptip`
- `layer_property('distance_units')`
- `display_expression`
- `eval_template`
- `make_date`
- `make_time`
- `make_datetime`
- `close_line`
- `is_multipart`
- geometría Z y M mínima y máxima
- `@frame_number`
- `@frame_rate`
- `@frame_duration`
- `@map_start_time` Start of the map\'s temporal time range (as a datetime value)
- `@map_end_time` End of the map\'s temporal time range (as a datetime value)
- `@map_interval:` Duration of the map\'s temporal time range (as an interval value)
- `@animation_start_time`
- `@animation_end_time`

Esta funcionalidad fue desarrollada por Etienne Trimaille, Jan Caha, Julien Monticolo, Nyall Dawson
### Característica: Navegador de funciones para la vista previa en el generador de expresiones
This adds a feature browser to the expression builder so one can browse features to see the result of the expression ![image65](images/entries/80604352-e6e4b400-8a31-11ea-8f3b-8c864e124c78.webp)

A new widget is added: `QgsFeaturePickerWidget`. For the moment, it\'s a simple combobox (but inherits widget so we can add a map picker button later on). It behaves the same way than the one in the relation reference widget (an editable combobox).

It relies on the same base model (`QgsFeatureFilterModel`). A new abstract class `QgsFeaturePickerModelBase` regroups the logic of the, and the new model is called `QgsFeaturePickerModel`. Basically the `QgsFeaturePickerModel` used the feature id to identify the features while `QgsFeatureFilterModel` use a list of attributes (the foreign keys of a relation). It declutters a bit the former model which was quite\...cluttered.

As a side note, I tried to use templates for `QgsFeaturePickerModelBase`, but since templates cannot be mixed with Q_OBJECT, the alternatives sounded like the code would be less readable.

Se han añadido pruebas.

Patrocinado por **QGIS Swiss User Group**!

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Habilidad para borrar funciones personalizadas
Agrega un botón de eliminación a la pestaña Editor de funciones en el cuadro de diálogo del generador de expresiones para permitir la eliminación de funciones de usuario de QGIS sin necesidad de navegar al directorio del perfil de usuario.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Añadir la habilidad para editar, importar y exportar expresiones de usuario
A new button is added that allows editing of saved expressions. It is only active when a user expression is selected in the expressions tree. When pressed, it opens a window that allows the currently selected user expression to be edited. Changing the label of the expression makes a copy of the currently existing one. [Demo](https://imgur.com/w3UEOoR)

**Importar/Exportar**

A new button with a menu is added, that allows the import/export of user expressions to/from a JSON file. Clicking on either of the menu entries opens a file selector dialog for the expressions JSON file source/destination. In the case of label conflicts, an additional dialog asks how to proceed - either to overwrite or to skip the current expression. [Import/Export Demo](https://imgur.com/0eiaFfu)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Digitalizando
### Característica: Dedicado a evitar el modo intersección/superposición de geometría
Esta versión de QGIS viene con una nueva configuración dedicada para evitar la intersección/superposición de geometría al digitalizar entidades.

| The three available modes are:

|

Permitir intersecciones / superposiciones

|

Evite intersecciones / superposiciones en la capa activa

|

Evite intersecciones / superposiciones en la lista de capas definidas por el usuario.

|

The third mode\'s layers list is setup by the user via the advanced snapping configuration widgets.

![image66](images/entries/caa646295d6f1cf6297864810637e9f8ceddc102.webp)

This feature was funded by [OpenGIS.ch](http://www.opengis.ch/)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Funcionalidad: Nuevos modos de ajuste: Centroide y mitad de un segmento (midpoint)
This feature is aimed at improving [snapping modes in QGIS](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/107) by getting closer to the experience of CAD tools.

Agrega dos nuevos modos. Ajuste en el centro de una geometría (centroide) y en el medio de un segmento.

Para permitir la selección de estos nuevos modos, se pueden seleccionar varios modos de ajuste al mismo tiempo.

![image67](images/entries/71798125-35201280-3051-11ea-959d-a5897ca3391a.webp)

El orden de preferencia para el ajuste es el siguiente: - Vértice, Intersección - Medio - Centroide - Borde - Área

![image68](images/entries/71799417-7e726100-3055-11ea-8e07-3792dbc741c2.gif)

Sponsored by: Qwat group / Ville de Lausanne ( \@ponceta \@dsavary ) / Oslandia and some spare time

This feature was developed by [lbartoletti](https://api.github.com/users/lbartoletti)
### Funcionalidad: Ajustar a la entidad digitalizada actualmente
Ajustar ahora también admite el ajuste a la entidad que se está digitalizando actualmente. Esta opción habilita/deshabilita un nuevo botón en la barra de herramientas de ajuste.

This enables some really nice CAD-like editing abilities, such as closing features at a 90° angle or precisely aligning segments inside a feature. It\'s very efficient once one is accustomed to using the alt+a shortcut to lock the angle.

![image69](images/entries/81065380-a37bc100-8edb-11ea-8aed-6fd52d843a26.gif)

Esta funcionalidad fue financiada por Kanton Solothurn y Land Vorarlberg

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Funcionalidad: Trazado ahora soporta geometrías curvas
La herramienta trazado ahora crea geometrías curvas cuando trabaja en una capa que soporta geometrías curvas.

![image70](images/entries/79769829-e3b04080-832c-11ea-9029-981e3a3ecf1b.gif)

El soporte es todavía experimental, así que esta funcionalidad debe ser habilitada en las opciones de digitalización:

Esta prestación fue financiada por ecoptima y Planteam

This feature was developed by [Olivier Dalang (OPENGIS.ch)](https://api.github.com/users/olivierdalang)
## Widgets y Formularios
### Funcionalidad: Permitir la edición de vínculos en el widget del archivo
En un formulario, los vínculos pueden ahora ser editadas en el widget de archivo (cuando el widget no es de solo lectura).

![image71](images/entries/81038564-bcb64a80-8ea6-11ea-8289-46340dee9a88.gif)

Patrocinado por el grupo de usuarios QGIS Swiss

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Etiquetas controladas por expresión (alias)
Esta nueva funcionalidad permite etiquetas de forma (alias) a ser evaluadas en el contexto del formulario.

![image72](images/entries/78998144-46912300-7b48-11ea-9fbf-232d11fbeff6.webp)

![image73](images/entries/78904645-26486200-7a7d-11ea-84b0-b9e96c0c9797.gif)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Característica: Añadir descripción al widget de relación de valor
Agrega una opción para añadir una descripción a cada valor en el widget de relación de valor. La descripción se mostrará como información sobre herramientas

Por favor perdone los diferentes idiomas en el video de demostración.

![image74](images/entries/76538031-f195ba80-647e-11ea-9a41-271576e315bc.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Característica: Nuevo widget de nombre de tabla de base de datos
Un nuevo widget fue añadido a QGIS para seleccionar una nueva tabla de una conexión a BBDD existente:

![image75](images/entries/76504669-70233580-6448-11ea-9194-173ae0d344ce.gif)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Característica Obtener valores de formulario principal actuales en formularios secundarios
This feature adds the option of using current values from the \"parent\" form in filter expressions (for now only in value-relation widgets: to be used in drill-down filters).

A new \"parentForm\" scope was added as well as a new set of functions and variables to access the parent from within an embedded child form. The new functions and variables were modelled on the existing \"current_value\", \"current_feature\" etc.

The new functions and variables are also available when the parent form is opened from a new (unsaved, unbuffered) feature, making it easier to create drill-down filters based on the parent\'s values when adding children from an unsaved parent form.
### Ejemplo
![image76](images/entries/75692656-28f9af80-5ca6-11ea-8dd6-9a4bf454f5b7.gif)
### Nuevas funciones y variables
![image77](images/entries/75693398-2ba8d480-5ca7-11ea-8be0-9643f8841c89.webp) ![image78](images/entries/75693402-2cda0180-5ca7-11ea-9d65-f0c00e26180e.webp) ![image79](images/entries/75693404-2d729800-5ca7-11ea-889d-5aa73bc131ce.webp)

Financiada por: **ARPA Piemonte**

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Característica: Widget de relación: agrega casilla de confirmación para ocultar el botón Guardar ediciones secundarias
Esto es muy útil para formularios encastrados.

Financiada por: **ARPA Piemonte**

![image80](images/entries/75524592-82e04800-5a0e-11ea-9333-461a0d02a1c0.webp)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Característica: Widget de relación fuerza supresión de ventana emergente
Añade una opción a la configuración del widget de relación para suprimir la ventana emergente de formulario abierta cuando se agregan nuevas características en un contexto de formulario encastrado.

Esta opción anula la opción nivel de formulario (ese podría ser el comportamiento deseado cuando el formulario se usa como formulario independiente).

![image81](images/entries/75249972-9786cb00-57d7-11ea-8100-3426d32831db.webp)

Aviso: la etiqueta final el **Forzar forma oculta al agregar función**

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
## Leyenda de capa
### Funcionalidad: Se agregó el movimiento hacia abajo en el menú contextual de vista previa de capas
Moverse alrededor de las capas en grandes proyectos se hizo más fácil con *Mover hacia arriba*, pero uno aún tenía que mover manualmente los mapas base al final de la lista de capas, una tarea engorrosa en los grandes árboles de capas. Esta funcionalidad agrega una opción *Mover al fondo* al menú contextual del árbol de capas que funciona de la misma manera que Mover al principio.

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Feature: Make Add Group button act as Group Selected if selected layers \>= 2
When there is more than one layer selected and the user presses the *Add Group* button, create a new group and put the selected layers in it too! ![image82](images/entries/76710403-f624d200-670f-11ea-9a41-13420c7940e3.gif)

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Funcionalidad: Permitir renombrado del tema del mapa actual
Esto añade la opción de renombrar un tema de mapa desde el menú desplegable del tema de mapa 

![image83](images/entries/78195435-e29f9800-747f-11ea-95d2-604be58cf229-1.gif)

This feature was developed by [Harrissou Sant-anna](https://api.github.com/users/DelazJ)
### Feature: Turn on/off ALL selected layers with \"Space\" button
Toggles the visibility of the currently selected layers or groups using the space button: ![image84](images/entries/77874799-cff64a80-7256-11ea-974b-c4084d1e01ae.gif)

This feature was developed by [Ivan Ivanov](https://github.com/suricactus)
## Herramientas de análisis
### Funcionalidad: Registro de Redes - mas funcionalidad
Añade algunas herramientas mas útiles para el registro de redes:
- Copiar URL
- Copiar petición como JSON
- Guardar registro a archivo (después de una gran advertencia a los usuarios de que el registro puede contener información confidencial y debe tratarse como confidencial)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Herramienta de registro de red incorporada
This tool, which is available from the new F12 \"dev tools\" panel, is a native port of \@rduivenvoorde\'s network logger plugin.

Muestra una lista de solicitudes de red en curso y completadas, junto con una carga completa de detalles útiles como estado de solicitud y respuesta, encabezados, errores, errores de configuración SSL, tiempos de espera, estado de caché, etc.

También tiene muchas capacidades útiles y de pulido, como la capacidad de filtrar solicitudes por subcadenas de URL y estado, y puede hacer click con el botón derecho en las solicitudes para abrir la URL en un navegador o copiarlas como un comando cURL.

¿Por qué queremos esto como una herramienta nativa en lugar de un complemento? Bien:
- It\'s extremely useful, so is nice to have available out-of-the-box
- Al moverlo a c++, podemos iniciar el proceso de registro mucho antes de que un complemento tenga la oportunidad. Esto permite que el registro incluya información adicional, como solicitudes activadas por otros complementos que se producen antes de que se haya cargado el complemento del registrador de red (también otras solicitudes integradas, por ejemplo, noticias)
- El rendimiento ha sido una lucha constante con el complemento Python. Si bien esto es lo más cercano posible a un puerto 1:1, los problemas de rendimiento se han resuelto mágicamente. Las clases tienen algunas operaciones de lista muy intensivas, lo que probablemente sea la causa del bajo rendimiento en Python.

![image85](images/entries/77712469-95ef3380-701f-11ea-8fec-3eded258b4e9.gif)

This feature was funded by [Meteorological Service of Canada](https://weather.gc.ca)

This feature was developed by [Nyall Dawson (for Kartoza)](https://api.github.com/users/nyalldawson)
## Procesado
### Funcionalidad: Colección de algoritmos de generación de raster aleatorios
Con esta funcionalidad, agregamos una amplia colección de algoritmos de generación de ráster de números aleatorios. Los algoritmos son capaces de generar rásteres aleatorios siguiendo distribuciones de números aleatorios específicos. Las siguientes distribuciones están disponibles:
1. Crear una capa ráster aleatoria (distribución binomial)
2. Crear una capa ráster aleatoria (distribución exponencial)
3. Crear una capa ráster aleatoria (distribución gamma)
4. Crear una capa ráster aleatoria (distribución binomial negativa)
5. Crear una capa ráster aleatoria (distribución normal)
6. Crear una capa ráster aleatoria (distribución de poisson)
7. Crear una capa ráster aleatoria (distribución uniforme)

![image86](images/entries/6304472935d29f8292cf24c7cb0198e95a4de137.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Funcionalidad: Capa vectorial teselada - Parte 8 (escritura en Procesamiento)
Esta funcionalidad agrega integración de procesamiento para la escritura de mosaicos vectoriales. Es solo un contenedor alrededor de la clase QgsVectorTileWriter existente.

Nuevos algoritmos en la caja de herramientas Procesamiento:

![image87](images/entries/81117303-224a1b80-8f27-11ea-851d-f4271ce66ed3.webp)

Algorithm\'s parameters for XYZ:

![image88](images/entries/81117371-4279da80-8f27-11ea-9d8b-bbe1c78d9bf1.webp)

Algorithm\'s parameters for MBTiles:

![image89](images/entries/81117466-6ccb9800-8f27-11ea-85e7-9c9a1df87920.webp)

Lista de capas entrantes:

![image90](images/entries/81117708-d6e43d00-8f27-11ea-866a-0c3bdbd97291.webp)

Detalles de capas entrantes:

![image91](images/entries/81117621-ae5c4300-8f27-11ea-993b-782d7de4a10e.webp)

This feature was funded by [QGIS Community](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Nuevo algoritmo del modelador para crear ramas condicionales
Este algoritmo permite a los usuarios configurar múltiples condiciones (a través de expresiones qgis), lo que hace que su rama correspondiente del modelo se ejecute u omita dependiendo del resultado de la evaluación de la expresión.

![image92](images/entries/79409609-b6d4f400-7fe1-11ea-8f7a-f42542f3fbfe.gif)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir reordenamiento de modelos entrantes
Instead of forcing a quasi-random ordering of inputs for models, this feature exposes a new \"Reorder Model Inputs\" option in the model designer which allows users control over the exact order of inputs to show users for their model.

No more illogical ordering like showing a field choice before the layer choice it\'s based on!

Patrocinado por NaturalGIS

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: aplazar la validación del modelo
Instead of forcing all child algorithms to be immediately valid and have all parameters correctly filled, this feature defers model validation until run time or when a new \"Validate model\" action is triggered.

A common frustration with the QGIS model designer is that it constantly forces models to be valid, even work-in-progress models. This means it's impossible to add a component to a model and only partially populate its settings --- you have to fill in everything upfront. If you realise mid way through this that you need to make a change somewhere else in your model, it's impossible to do without canceling and losing all the settings you've already configured.

Este cambio ve la validación del modelo diferida hasta el tiempo de ejecución. Los modelos pueden ser temporalmente inválidos (por ejemplo, tener componentes de algoritmo que solo están configurados parcialmente). Los valores requeridos que faltan ahora se pueden completar en una etapa posterior, sin perder ninguna configuración existente. Si se ejecuta un modelo no válido, el usuario recibe una advertencia descriptiva informándole de los cambios que deben realizar para finalizar la configuración del modelo.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Se agregó soporte para diferentes tipos de datos ráster en Crear algoritmo de capa ráster constante
With this feature we added a new advanced **OUTPUT_TYPE** parameter for the *Create constant raster layer* algorithm. Via this parameter, you can now specify an output data type for your constant raster layers.
- Byte
- Integer16
- Integer16 sin signo
- Integer32
- Integer32 sin signo
- Float32
- Float64

![image93](images/entries/b7b0b73f7d48104cb49f33ed2d453a70d188cbd6.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Funcionalidad: Añadido algoritmo de Redondeo ráster
Con este nuevo algoritmo de procesamiento capacitamos a QGIS para **redondear valores Ráster**

La funcionalidad principal del algoritmo es el redondeo ascendente/cercano/descendente estándar de los valores de celda de coma flotante o el redondeo a las potencias de una base *n* especificada por el usuario. El algoritmo se puede usar con rásteres de todo tipo (incluso rásteres de bytes/enteros al redondear a potencias de n) y genera el mismo tipo de datos ráster. Un redondeo de coma flotante estándar de un ráster entero lo copiará y generará una advertencia.

El ejemplo muestra una salida ráster redondeada a múltiplos de 10

![image94](images/entries/650983141141fc954abc96f79e5255e4634c5051.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Funcionalidad: Permitir copiado/cortado/pegado de componentes del modelo
Esta funcionalidad permite a los usuarios copiar y pegar componentes del modelo, tanto dentro del mismo modelo como entre distintos modelos

![image95](images/entries/78641463-a099aa80-78f4-11ea-8c0b-c6b6b72f0e7d.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: permite agregar resultados de procesamiento a capas existentes
When appending results, users are given a field mapping panel choice to allow them to manually set how fields are mapped to the destination layer\'s fields:

![image96](images/entries/78631098-b9976100-78de-11ea-8f18-f7c7473e0945.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir la creación de cuadros de grupos en modelos
Añade las siguientes funciones al diseñador del modelo:
- La habilidad para personalizar el color de comentarios en un modelo
- Allow creation of \"Group Boxes\" in models, which are a visual indicator of logically linked model components (e.g. \'Data Preparation Steps\', \'NDVI Calculation Steps\', \... etc). Users can customise the color and title for group boxes.
- Permite la navegación directa a los cuadros de grupo desde el menú Ver, lo que ayuda a la navegación de modelos complejos.

![image97](images/entries/78090538-bba87e00-740d-11ea-9476-144163d8f1ca.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcoinalidad: Procesamiento: muestra valores de entrada y salida para hijos después de ejecutar el modelo a través del diseñador
¡Una imagen lo explica mejor! Después de ejecutar el algoritmo a través del diseñador, ahora verá los valores calculados para las entradas y salidas para cada algoritmo secundario:

![image98](images/entries/77991113-5d749000-7366-11ea-986c-652f6e2229e7.webp)

This is very useful for debugging models \-- you can see a much clearer visual picture of the flow of values through the model.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"Save Log to File\" algorithm for models
This algorithm saves the contents of the execution log (right up to the point in the model at which the \'save log\' algorithm executes) to a file.

Se puede utilizar para almacenar automáticamente el registro de depuración cuando se ejecutan modelos para su posterior consulta y transparencia.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir ejecutar algoritmos directamente en la fuente de base de datos (y otras no en disco) sin cargarlos antes en el proyecto
Este cambio permite a los usuarios navegar directamente a fuentes de capa no ubicadas en disco para cualquier entrada de fuente de entidad de procesamiento. ¡Permite que estas entradas se tomen directamente desde capas postgres, sql server, oracle, wfs, afs, etc. sin tener que cargarlas primero en un proyecto!

Aprovechamos al máximo el navegador QGIS al habilitar esto:

![image99](images/entries/77508685-fca50d80-6eb6-11ea-8190-a447847f55d9.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Mostrar opciones avanzadas para fuente de entidad para el procesamiento de entradas
Esta funcionalidad muestra opciones avanzadas para fuentes de entidad, tales como:
- La habilidad de limitar el número de entidades leidas desde la fuente. (Útil en desarrollo de modelos, puede fácilmente verificar la ejecución de modelos usando un pequeño subconjunto de una capa de entrada)
- The ability to override on a per-input basis the global processing option for how to handle invalid geometries. Now you can safely leave the default processing setting at the conservative \"Stop algorithm execution when a geometry is invalid\" setting while easily temporarily overriding this for one particular input!

![image100](images/entries/77395930-64dbec80-6dee-11ea-9590-b7fadcd242c1.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir el ajuste a la rejilla para modelos en el diseñador
This update implements two \"snapping\" features in the Processing model designer:
1. Users can enable a new \"Enable Snapping\" option from the view menu, which will cause all component moving or resizing operations to automatically snap to grids
2. After selecting some components, users can select Edit -\> Snap Selected Components to Grid to manually snap just those selected components.

Additionally, I\'ve added a helpful \"select all\" action for quickly selecting all components in a model.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: Add \"filter by geometry type\" and \"filter by layer type\" algorithms to processing
Esta actualización añade dos nuevos algorimtos a procesamiento:
- \"Filter by geometry type\": This algorithm filters features by their geometry type. Incoming features will be directed to different outputs based on whether they have a point, line or polygon geometry. It allows for model creation which responds to different input layer geometry types by applying different logic depending on the input geometry type.
- \"Filter by layer type\": This algorithm allows conditional model branching based on an input layer type. For instance, it allows a model to adapt to the actual layer type of a generic \"map layer\" parameter input, and decide which branch of the model to run as a result.

It also adds in the required API to allow algorithms to \"prune\" model branches based on their calculated results. For example, a model which returns the new *FlagPruneModelBranchesBasedOnAlgorithmResults* flag will cause any remaining parts of the model which are dependent on the outputs of that algorithm to be entirely skipped IF the algorithm does not return that particular output. (This is a prerequisite component for a future generic \"conditional branching by expression\" algorithm, and also used by \"filter by layer type\" to control the model flow based on the input layer type)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: \"Remove Null Geometries\" algorithm can also remove EMPTY geometries
Empty geometries do not contain coordinates. Thus, like *null* geometries, empty geometries are not spatial data in a strict sense. To make it easier for users to clean a vector layer, the *Remove Null Gometries* algorithm now has an \"**Also remove empty geometries**\" option.

![image101](images/entries/76703713-81b34a00-66a1-11ea-9818-ebf771885206.webp)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Funcionalidad: Añadir manejo de multiselecciones al diseñador de modelo, redimensionado interactivo
Añade:
- La habilidad para seleccionar múltiples elementos al tiempo en el diseñador de modelo
- La habilidad para redimensionar elementos individuales o múltiples
- La habilidad para borrar múltiples elementos seleccionados
- Improved model designer \"tool\" interaction, following the layout designer approach (e.g. alt + space = zoom drag mode, and selection tools follow their counterparts in layouts so shift+selection adds to selection, ctrl+selection removes, etc)
- Los elementos seleccionados se pueden mover con las teclas de cursores

Refs NRCan Contract#3000707093

Here\'s how it looks in action (with a particular ugly looking test model I use!)

![image102](images/entries/76388083-f9d4f380-63b3-11ea-8f06-97249e85ac2e.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Añadir soporte deshacer/rehacer al diseñador de modelo
¡Hace QGIS mas clemente para los usuarios!

Refs NRCan Contract#3000707093

Works just like you\'d expect:

![image103](images/entries/76176510-c8fe8e00-61fc-11ea-90e1-91cbeadcbd4f.gif)

Tenga en cuenta que guardamos toda la definición del modelo en la pila de deshacer, no solo los cambios en los componentes afectados.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Recordar los valores de los parámetros entre ejecuciones del diseñador del modelo
Al diseñar un modelo, los usuarios generalmente necesitarán ejecutar el modelo muchas veces mientras modifican su estructura.

This change causes the parameters used when running the model from the designer to be remembered and saved into the model, so that each time you run the model from the designer you don\'t have to re-set all the input parameter values to the desired test ones.

¡Hace que el diseño iterativo del modelo sea MUCHO más fácil!

Patrocinado por Alta Ehf

Also includes a partial port of the model designer dialog from Python to c++, because c++ \>\> Python.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Comentarios en modelos de procesamiento
Esto permite a los usuarios crear comentarios adjuntos a los componentes del modelo (entradas, algoritmos o salidas). Los comentarios se muestran vinculados al componente asociado y se pueden mover libremente por el modelo.

![image104](images/entries/75851342-26799000-5e35-11ea-8895-a310f01b3823.gif)

Financiada por Fisel + König

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: nueva herramienta de consola independiente para ejecutar algoritmos de procesamiento
This new qgis_process tool allows users to run processing algorithms (both built-in, and those provided by plugins) directly from the console.

Ejecutando:
- `qgis_process list` will output a complete list of all available algorithms, grouped by provider.
- `qgis_process plugins` lists available and activated plugins which advertise the hasProcessingProvider metadata option (only these plugins are loaded by the tool)
- `qgis_process help algid` outputs the help and input descriptions for the specified algorithm, e.g. `qgis_process help native:centroids`

`qgis_process run`: runs an algorithm. Parameters are specified by a `--param=value` syntax. E.g.

    qgis_process run native:centroids --INPUT="my_shapefile.shp" --OUTPUT="centroids.kml"
    
o

    qgis_process run native:buffer --INPUT=/home/me/my.shp --DISTANCE=20 --OUTPUT=/home/me/buffered.shp
    
Mientras se ejecuta un algoritmo, se muestra una barra de comentarios basada en texto y la operación se puede cancelar mediante CTRL + C

Patrocinado por el Grupo de Usuarios Sueco

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Nuevo tipo de parámetro para valores de fecha y hora (o fecha u hora)
Agrega un nuevo tipo de parámetro QgsProcessingParameterDateTime para manejar valores de fecha/fecha y hora/hora.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funconalidad: Añadir algoritmos para generar advertencias y excepciones de modelos
Estos algoritmos generan una advertencia personalizada en el registro de procesamiento O generan una excepción que hace que la ejecución del modelo finalice.

An optional condition expression can be specified to control whether or not the warning/exception is raised, allowing logic like \"if the output layer from another algorithm contains more than 10 features, then abort the model execution\".

Patrocinada por Fisel + König

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Añadir algoritmo para rellenar celdas NoData (sin datos)
En la nueva versión de QGIS, presentamos un nuevo algoritmo de procesamiento para llenar celdas NoData en un conjunto de datos ráster con una entrada numérica constante.

El algoritmo escanea un dataset ráster de entrada en busca de celdas NoData y las llena con el valor de relleno definido por el usuario. Al hacerlo, el algoritmo respeta el tipo de datos del ráster de entrada de modo que, p.ej. los números de coma flotante se tratarán adecuadamente para un ráster entero. El conjunto de datos resultante no contendrá ninguna celda NoData.

![image105](images/entries/6cbf249116a09b4d342729da1e09060b9f0ec52f.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Funcionalidad: Varias correciones para Procesamiento
- Finalizar el trabajo sobre el soporte de parámetros de rango en algoritmos GRASS;
- Arreglar algoritmo roto r.series
- Correciones menores a r.rescale y r.rescale.eq
- Correciones para herramienta rasterizado
- Limpieza de pruebas GRASS GIS

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Feature: Show \"template layer\" field constraints in the \"Refactor Fields\" algorithm interface
Cuando está migrando datos, es importante tener en cuenta las restricciones en las capas de destino (también conocido como plantilla).

The \"Refactor Fields\" algorithm now highlights constraints, and even lets you know more about them via tool-tips.

![image106](images/entries/75100644-6079a500-559e-11ea-91b6-f99fa05451de.webp)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Funcionalidad: Nuevo algoritmo convertir a curvas
Agregamos un nuevo algoritmo para convertir geometrías segmentadas en geometrías curvas.

El algoritmo considera puntos sucesivos para representar una curva si están espaciados uniformemente y dentro de una tolerancia.

![image107](images/entries/c747d86081f3862d9d4bbb2ab067103daceab724.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Opciones de Aplicación y Proyecto
### Feature: Add \@layers, \@layer_ids project scope variables
Add \@layers, \@layer_ids project scope variables which contain lists of map layers and map layers ids for all layers from the current project

This mimics the existing \@map_layers, \@map_layer_ids, but unlike the \@map variants these return ALL project layers, not just those associated with the current context\'s map settings.

Patrocinado por SLYR

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Proveedores de datos
### Funcionalidad: Permitir añadir atributos en el diálogo  New Scratch Layer
Allows the user to add attributes directly in the New Scratch Layer dialog making it more consistent with other dialogs like New Shapefile/Geopackage. ![image108](images/entries/81394331-76711d80-912a-11ea-8b86-4f2789adff08.webp)

Todavía es posible crear una capa reutilizable sin ningún atributo al no agregar ningún campo a la lista.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Premitir la creación tablas DBF sin geometrías desde el diálogo New Shapefile
Allow creating \"plain\" DBF files without associated geometries from the New Shapefile dialog.

![image109](images/entries/81068877-be553200-8ee9-11ea-9a06-a4d30e773cf6.webp)

Creating DBF tables can be useful in some cases and having to use third-party tools for this instead of doing it from within QGIS is inconvenient. This also makes the New Shapefile dialog more consistent with the New Geopackage dialog, which already allows \"geometryless\" tables to be created.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Permitir el filtrado de lista WM(T)S en diálogo fuente
Añade la habilidad para filtrar entre listas de WMS o WMTS desde el diálogo fuente

WMS ![image110](images/entries/80964825-d0fc3800-8e11-11ea-9961-34edb623458c.webp)

WMTS ![image111](images/entries/80964191-b4abcb80-8e10-11ea-8b80-395dbb37b45c.webp)

Patrocinado por el grupo de usuarios QGIS Swiss

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funcionalidad: Añadir teselas vectoriales al Administrador de Fuente de Datos y al menú Capas
Agrega una nueva pestaña al cuadro de diálogo Administrador de origen de datos que permite al usuario administrar/agregar conexiones de mosaicos vectoriales, incluida la importación/exportación. También agrega una entrada correspondiente al menú Capas.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Importar/Exportar a Mapa ArcGIS y FeatureServer
Agregue la funcionalidad de importación/exportación perdida para las conexiones ArcGIS MapServer y FeatureServer.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Añadir teselas XYZ al diálogo Administrador de Fuente de Datos y al menú Capas
Agrega una nueva pestaña al cuadro de diálogo Administrador de fuente de datos que permite administrar/agregar conexiones XYZ. Agrega también la entrada correspondiente al menú Capas.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Funcionalidad: Grupo de transacciones SpatiaLite
Implementación de Transacciones para el proveedor nativo SpatiaLite

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Funcionalidad: Permitir guardar salidas directamente a más formatos de base de datos (y otras cosas agradables)
Esta actualización permite a los usuarios guardar las salidas de procesamiento de vectores directamente en más formatos de base de datos.

Anteriormente, los resultados solo podían escribirse directamente en las bases de datos de Postgres. Con este cambio, esta funcionalidad se ha hecho más flexible y ahora admite la escritura directa a cualquier proveedor de base de datos que implemente la API de conexiones (actualmente postgres, geopackage, spaceialite y servidor sql)

En última instancia, esto expone la nueva capacidad de guardar directamente los resultados en las bases de datos de Servidor SQL o Spatialite (junto con las opciones anteriores de GPKG + Postgres que ya existían)

(As soon as oracle, db2, \... have the connections API implemented we\'ll instantly gain direct write support for those too!)

We do this via a nice inline version of the new \"new database table name\" widget.

![image112](images/entries/77608752-dab89300-6f69-11ea-9c48-eefca7a4d199.gif)

Otras cosas nuevas incluyen:
- Ahora puede arrastrar y soltar archivos o carpetas desde el explorador o el navegador qgis a los parámetros de salida para sobrescribir fácilmente estos archivos (o guardarlos en la carpeta), haciendo coincidir el comportamiento posible con las entradas
- You can actually write scripts which output direct to ANY qgis data provider (including oracle and db2)\... it\'s just that these don\'t get exposed in the UI because they don\'t yet support the connections API

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Añadir tipo de parámetro dedicado a conexiones de bases de datos
Permite la selección de las conexiones de base de datos registradas para un tipo de proveedor de base de datos específico (el proveedor debe implementar la API de conexiones).

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: PG: expone tablas foráneas
Expone tablas foráneas al navegador y diálogo de selección de base de datos.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Característica: El raster PG expone el filtro establecido a la aplicación
Este debe ser el cambio final al proveedor de datos ráster PG y expone las opciones del filtro de ajuste:
- El filtro puede ser establecido en el diálogo de la fuente de datos (como para capas vectoriales)
- Filter can be set from the legend tree\'s context menu (as for vector layers)
- El renderizador, la extensión y las estadísticas mín/max también se actualizan cuando cambia el filtro
- Nuevas pruebas para el nuevo comportamiento

![image113](images/entries/75894983-49a43f80-5e35-11ea-95a8-a86276b39bbc.gif)

This feature was funded by [ARPA Piemonte](http://www.arpa.piemonte.it/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Funcionalidad: Postgres: guardar entidades en tablas con campos generados
Permitir la actualización/inserción de entidades en tablas PostgreSQL con campos generados. Las columnas GENERADAS son una funcionalidad introducida por PostgreSQL 12, que permite generar valores de columna a partir de otras columnas en la misma tabla; esto reemplaza la creación de desencadenantes para, por ejemplo, rellenar automáticamente y mantener actualizada una columna de centroides o áreas para los polígonos en la columna de geometría principal.

This feature was developed by [José de Paula Rodrigues N. Assis](https://api.github.com/users/espinafre)
### Funcionalidad: soporte para los tipos de campo Fecha y FechaHora añadidos a proveedores SpatiaLite y Texto Delimitado
Los proveedores SpatiaLite y Texto Delimitado ahora soportan tipos de campo Fecha y FechaHora.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Servidor de QGIS
### Feature: Add QGIS_SERVER_IGNORE_BAD_LAYERS config option
Permite ignorar el comportamiento por defecto en el caso de capas malas (que puede invalidar todo el proyecto).

Establecido a VERDADERO, las capas malas son saltadas y el resto del proyecto se vuelve válido.

This feature was funded by [Geoinformatikbüro Dassau GmbH](https://www.gbd-consult.de/home.html)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Feature: Server project settings, add \'expanded\' attribute
In addition to the \'visible\' and \'mutuallyExclusive\' attribute, this update adds \'expanded\' to the GetProjectSettings response of the server. The update allows a web client to see which layer tree elements are expanded / collapsed and to then present them the same way in the web map layer list.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files.

Añade parámetros desaparecidos a petición GetDxf.

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Funcionalidad: Convalidador de proyectos WMS
El convalidador del servidor QGIS ha sido revisado. Esta herramienta es útil cuando desea publicar un proyecto QGIS utilizando el protocolo WMS.

Para programadores, el convalidador es también invocable desde PyQGIS, así que los complementos ahora también pueden usarlo.

This feature was funded by [3Liz](https://www.3liz.com)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Funcionalidad: Webp
> WebP es un formato de imagen moderno que proporciona una compresión superior sin pérdidas para las imágenes en la web. WebP crea imágenes más ligeras y fieles que hacen que la web sea más rápida.
> 
> Las imágenes sin pérdida de WebP son un 26% más pequeñas en tamaño que las PNG. Las imágenes con pérdida WebP son un 25-34% más pequeñas que las imágenes JPEG comparables con un índice de calidad SSIM equivalente.

Source: <https://developers.google.com/speed/webp>

Con webp, el servidor QGIS ahora admite un formato que proporciona tamaños de archivo más pequeños para la misma calidad e incluso proporciona transparencia.

This feature was funded by [OPENGIS.ch](https://www.opengis.ch)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Plugins
### Feature: Allow plugins to register custom \"Project Open\" handlers
These allow plugins to extend the \"Open Project\" dialog by adding in support for new file filters, which appear in the formats drop down list alongside the existing \"QGS Projects\" entry.

Los controladores abiertos de proyectos personalizados tienen la primera oportunidad de cargar archivos de proyecto.

Esto permite que los complementos amplien el soporte QGIS al agregar soporte integrado para abrir proyectos desde formatos que no sean QGS/QGZ, p.ej. permitiendo a los usuarios abrir documentos ArcGIS MXD o MapInfo WOR Workspaces directamente desde el diálogo de apertura del proyecto.

Estos proyectos no nativos también se agregan a la lista de proyectos recientes y a la pantalla de bienvenida, lo que les brinda una experiencia verdaderamente de primera clase dentro de QGIS.

Patrocinado por SLYR

![image114](images/entries/78514331-1833e080-77f4-11ea-9c8d-a5e9ead7dc1a.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Permitir a los usuarios instalar complementos estables o experimentales
Esta actualización mejora el administrador de complementos al permitir a los usuarios elegir entre instalar la versión estable o la versión experimental de un complemento.

Esto hace posible tener prelanzamientos de complementos en el repositorio para que los usuarios avanzados puedan probarlos, al tiempo que les permite volver fácilmente a versiones estables, sin tener que desmarcar la opción global *habilitar experimental*.

This change makes no difference for users who haven\'t checked the *enable experimental* option.

![image115](images/entries/75906887-b1638600-5e47-11ea-98c6-06fb664ab177.webp)

This feature was funded by [Swiss QGIS User Group](https://www.qgis.ch/)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
## Programabilidad
### Característica: Soporte para agregar widgets de muelle como pestañas: addTabifyDockWidget()
Los widgets de muelle son buenos para visualizar interfaces complejos que extienden la funcionalidad QGIS.

Ahora, tanto los desarrolladores principales como los complementos tienen la opción de tabular sus widgets de base sobre los existentes. Incluso pueden elegir sobre qué widget de muelle quieren que aparezca su propio widget de muelle.

![image116](images/entries/80051225-4b0cf280-84dd-11ea-9016-84a4303f230f.gif)

This feature was funded by [SwissTierras Colombia](https://swisstierrascolombia.com/)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Caracterísitca: Envoltorio de parámetros de salida para la nueva API
Conecta los contenedores de parámetros de salida (destinos de sumideros, vector, trama, archivos y carpetas) a la nueva c++ API para diálogo y modelador.

Esto permite una serie de nuevas posibilidades, incluyendo:
- Models with static outputs for child algorithms, e.g. always saving a child algorithm\'s output to a geopackage or postgres layer
- Models with expression based output values for child algorithms, e.g. generating an automatic file name based on today\'s date and saving outputs to that file

![image117](images/entries/78028688-bbbf6400-73a2-11ea-9b7f-a7d81133d321.gif)

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Característica: Llevar los últimos parámetros de entradas restantes a la nueva API
Esta actualización transfiere los parámetros de entrada Raster Band y Multi Layer a la nueva API C++.

Los beneficios incluyen:
- Expresión basada en las listas banda/capa en los modelos
- Listas en línea (sin bloqueo) para parámetros de selección múltiple (campos, bandas, listas de capas, enumeraciones)
- Reordenamiento de parámetros de entrada multicapa en los modelos, para establecer órdenes específicos de capa

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Parámetros de fuente de entidades de puerto, ráster, vector y capa de malla a nueva API
It\'s now possible to use expression-based layer sources in processing models.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Capa vectorial teselada - parte 1
Este es el trabajo inicial en soporte de capa vectorial teselada.

![image118](images/entries/77539757-2d2e7c80-6ea2-11ea-9098-c6c0924f9d59.webp) (The red lines are not rendering artifacts, they are drawn intentionally to show tile borders.)
### Resumen
So far this only includes changes to the qgis_core library.

Principales adiciones a la API pública:
- QgsVectorTileLayer - la clase de capa principal de mapa
- QgsVectorTileRenderer - clase base para implementaciones de la clase renderizador para mosaicos vectoriales
- QgsVectorTileBasicRenderer - implementación del renderizador por defecto

Nuevas clases privadas (se pueden agregar a la API pública si es necesario):
- QgsVectorTileLoader - maneja la búsqueda de mosaicos de la red/mbtiles
- QgsVectorTileMVTDecoder - manejar la decodificación de datos de mosaico sin procesar a las entidades
- QgsVectorTileLayerRenderer - se encarga de la representación general (buscar + decodificar + dibujar)
- QgsVectorTileUtils - algunas funciones útiles

Algunas clases nuevas que pueden compartir los mosaicos vectoriales y ráster:
- QgsTileXYZ - posición de una tesela en el conjunto de matriz de mosaico (nivel de zoom, columna, fila)
- QgsTileRange - Selección rectangular en una matriz de mosaico (columna y fila inicial / final)
- QgsTileMatrix - Descripción de una matriz de mosaico (extensión del mapa, nivel de zoom, escala, número de filas / columnas)

(también QgsTileMatrixSet se agregará más adelante cuando admitamos otros conjuntos de matriz de mosaicos que no sean solo GoogleCRS84Quad)
### Probando
You can load a vector tile layer from Python console, e.g.:

    ds = QgsDataSourceUri() ds.setParam("type","xyz")
    ds.setParam("url", "https://api.maptiler.com/tiles/v3/{z}/{x}/{y}.pbf?key=YOUR_FREE_API_KEY") 
    uri = bytes(ds.encodedUri()).decode('utf-8')
    vtl = QgsVectorTileLayer(uri, "Vector Tiles Test")
    QgsProject.instance().addMapLayer(vtl)
    
It is also possible to load vector tiles from a local MBTiles file - for \"type\" use \"mbtiles\" and for \"url\" use a local path (e.g. \"/home/martin/x.mbtiles\").

No hay actualmente soporte para etiquetado.
### Gracias
Huge thanks to all funders who have contributed to the crowdfunding and made this possible - <https://www.lutraconsulting.co.uk/blog/2020/04/02/vectortiles-donors>

This feature was funded by [QGIS Community](https://www.lutraconsulting.co.uk/crowdfunding/vectortile-qgis/)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk)
### Característica: Parámetro de extensión de procesamiento de puerto a la nueva API, otras muchas mejoras
Esta actualización finalmente transfiere el parámetro de extensión a la nueca API C++, pero a lo largo del camino:
- Refactors the existing gui widget \"QgsExtentGroupBox\" to move the guts out to \"QgsExtentWidget\" (allowing it to be used in places where a group box is inappropriate/looks bad). It also adds a new \"condensed\" mode for the widget, because the default appearance is very space heavy.
- El nuevo widget de parámetros utiliza este QgsExtentWidget común, por lo que eliminamos todo el código duplicado que anteriormente usaba el antiguo envoltorio de Python
- Permite arrastrar y soltar las capas del mapa del proyecto desde el árbol de capas a un QgsExtentWidget para configurar automáticamente la extensión de modo que coincida
- Permite QgsExtentWidget ser opcionalmente anulable
- Allows QgsGeometry values to be set for extent parameter values. This is done to aid use of extent parameters with the \"precalculated value\" mode in models \-- you can now use all the expression geometry functions to calculate a geometry and the bounding box of this is used for the parameter value in the child algorithm

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funcionalidad: Interfaz y API para herramientas unificadas de desarrollo/depuración
Adds interface hooks to allow plugins (and c++) to register \"development/debugging\" tools

Estas herramientas aparecen en un nuevo bloque de Herramientas de Desarrollo/Depuración, y proporcionan un lugar unificado y manejable para estas herramientas en la IU.

Aquí la intención es que las herramientas especializadas en desarrollo/depuración serán movidas a esta interfaz común, p.ej.
- Registro de Red
- Inspector de variables locales de Python de primeros auxilios
- Herramientas de depuración en el momento del arranque
- Layer load and rendering time debugging tools \... ?

Here\'s an example demo showing a \"Python locals\" dev tool:

![image119](images/entries/77492080-55f74780-6e8b-11ea-9141-1b96c42c29eb.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Característica: Tipo de datos soportados para QgsProcessingParameterMapLayer
Allow the definition of accepted layer types for `QgsProcessingParameterMapLayer`. This is useful when an algorithm can work with different layer types (for example, points and rasters) and avoids duplication of the same algorithm with different inputs.

Esto es una mejora de la API y no es visible para las gran mayoría de los usuarios.

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Característica: Agregar tipos de parámetros de procesamiento para el esquema de la base de datos y el nombre de la tabla
Reemplaza los anteriores contenedores widget postgis ad-hos de Python con os parámetros apropiados de primera clase C++ para esquemas y tablas, con contenedores construidos a partir de la API de conexiones principales.

Refs NRCan Contract#3000707093

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Getfeatureinfo no muestra la relación de elementos de referencia para el Servidor QGIS | [#36549](https://github.com/qgis/QGIS/issues/36549) | Resulto ser una solicitud de función | N/D |
| OGR provider QgsOgrProvider::changeAttributeValues devuelve verdadero en errores | [#36583](https://github.com/qgis/QGIS/issues/36583) | [PR #36620](https://github.com/qgis/QGIS/pull/36620) | N/D |
| Los grupos de transacciones GPKG se almacenan con el segundo par vacío de la clave | [#36525](https://github.com/qgis/QGIS/issues/36525) | [PR #36660](https://github.com/qgis/QGIS/pull/36660) | [PR #37157](https://github.com/qgis/QGIS/pull/37157) |
| Simbología usando relaciones no se propaga en el Servidor QGIS | [#36614](https://github.com/qgis/QGIS/issues/36614) | No se ejecuta | N/D |
| \"Loading PostGIS raster with QGIS 3.12.3 crashes\" | [#36689](https://github.com/qgis/QGIS/issues/36689) | [PR #36702](https://github.com/qgis/QGIS/pull/36702) | irrelevante |
| valor de GetFeatureInfo Fid es diferente entre aplicación/json y aplicación/vnd.ogc.gml | [#36262](https://github.com/qgis/QGIS/issues/36262) | [PR #36733](https://github.com/qgis/QGIS/pull/36733) | [PR #37158](https://github.com/qgis/QGIS/pull/37158) |
| GPKG (y spatialite) DB-nivel restricción única no son soportados por el proveedor OGR (y spatialite) | [#36468](https://github.com/qgis/QGIS/issues/36468) | [PR #36802](https://github.com/qgis/QGIS/pull/36802) | N/D |
| sin valor en la forma de atributo si falta valor en el mapa de valores | [#32756](https://github.com/qgis/QGIS/issues/32756) | [PR #36804](https://github.com/qgis/QGIS/pull/36804) | N/D |
| El Administrador de BBDD ya no muestra resultados de consultas | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36823](https://github.com/qgis/QGIS/pull/36823) | N/D |
| El Administrador de BBDD ya no muestra resultados de consultas | [#36205](https://github.com/qgis/QGIS/issues/36205) | [PR #36831](https://github.com/qgis/QGIS/pull/36831) | N/D |
| Coger/soltar en el navegador GPKG no funciona | no reportado | [PR #36972](https://github.com/qgis/QGIS/pull/36972) | [PR #37159](https://github.com/qgis/QGIS/pull/37159) |
| no es posible guardar un proyecto en el geopaquete | [#36832](https://github.com/qgis/QGIS/issues/36832) | [PR #36980](https://github.com/qgis/QGIS/pull/36980) | N/D |
| It is possible to store text into a numeric field, while it shouldn\'t be, using the Date/Time edit widget | [#36715](https://github.com/qgis/QGIS/issues/36715) | [#36715](https://github.com/qgis/QGIS/issues/36715) | N/D |
| Creación de entidad muy lenta al usar uniones | [#36167](https://github.com/qgis/QGIS/issues/36167) | [PR #36866](https://github.com/qgis/QGIS/pull/36866), [PR #36963](https://github.com/qgis/QGIS/pull/36963) | N/D |
| Servidor QGIS: Petición WFS no usa SrsName en la geometría | [#36398](https://github.com/qgis/QGIS/issues/36398) | [PR #36926](https://github.com/qgis/QGIS/pull/36926), [PR #37071](https://github.com/qgis/QGIS/pull/37071) | no crítico |
| Incapaz de borrar una conexión a geopaquete almacenado desde el navegador | [#36930](https://github.com/qgis/QGIS/issues/36930) | [PR #36937](https://github.com/qgis/QGIS/pull/36937) | [PR #37166](https://github.com/qgis/QGIS/pull/37166) |
| Restricciones: única restricción evaluada incorrectamente cuando es 0 | [#36962](https://github.com/qgis/QGIS/issues/36962) | [PR #36967](https://github.com/qgis/QGIS/pull/36967) | N/D |
| PyQgis: campos OriginJoin no presentes en contenedor QgsLayerVector QgsFields para capas GeoPackage | [#36977](https://github.com/qgis/QGIS/issues/36977) | no ejecutable | N/D |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | no ejecutable/en progreso | N/D |
| Removal of unused \'allowMethod\' from qgisservice/qgisserverapi | [#36163](https://github.com/qgis/QGIS/issues/36163) | [PR #36997](https://github.com/qgis/QGIS/pull/36997) | N/D |
| Homogeneizar el título de la ventana | [#35761](https://github.com/qgis/QGIS/issues/35761) | [PR #36998](https://github.com/qgis/QGIS/pull/36998) | N/D |
| Etiquetado: problema de activación de atenuación de alineación definida por datos | [#37003](https://github.com/qgis/QGIS/issues/37003) | [PR #37006](https://github.com/qgis/QGIS/pull/37006) | [PR #37167](https://github.com/qgis/QGIS/pull/37167) |
| QGIS reports \"no layers\" in GeoPackage when geopackage directory is write protected | [#36574](https://github.com/qgis/QGIS/issues/36574) | [PR #37018](https://github.com/qgis/QGIS/pull/37018) | no crítico (solo UX) |
| Joined tables cannot be edited even if the \"editable join layer\" option is checked | [#36934](https://github.com/qgis/QGIS/issues/36934) | won\'t fix | N/D |
| Las marcas de tiempo de Postgis de la consulta en el Administrador de BBDD se muestran como \`PyQT5.QTCore.QDateTime(2020, 3, 17 | [#35140](https://github.com/qgis/QGIS/issues/35140) | [PR #37042](https://github.com/qgis/QGIS/pull/37042) | N/D |
| Vista previa de imagen incorrecta y tamaño de vista previa de imagen en formulario | [#33682](https://github.com/qgis/QGIS/issues/33682) | [PR #37093](https://github.com/qgis/QGIS/pull/37093) | [PR #37168](https://github.com/qgis/QGIS/pull/37168) |
| can\'t change value in vertex editor if \"locale\" settings use commas as decimal separator | [#29682](https://github.com/qgis/QGIS/issues/29682) | [PR #37135](https://github.com/qgis/QGIS/pull/37135) | [PR #37169](https://github.com/qgis/QGIS/pull/37169) |
| Identifying a WMS layer with format \"feature\" crashes QGIS | [#29443](https://github.com/qgis/QGIS/issues/29443) | [PR #37171](https://github.com/qgis/QGIS/pull/37171) | [PR #37210](https://github.com/qgis/QGIS/pull/37210) |
| Intentar crear una nueva entidad en Spatialite con grupo de transacciones y la restricción NOT NULL falla | [#37236](https://github.com/qgis/QGIS/issues/37236) | won\'t fix | N/D |
| Using \"Add feature\" to create feature and child feature with transaction group causes foreign key error | [#37222](https://github.com/qgis/QGIS/issues/37222) | [PR #37249](https://github.com/qgis/QGIS/pull/37249) | no crítico |
| Capa vectorial de spatialite con entidades desaparecidas y recuento inconsistente de entidades | [#29264](https://github.com/qgis/QGIS/issues/29264) | [PR #37277](https://github.com/qgis/QGIS/pull/37277) | PORHACER. |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir error cuando la capa vectorial tiene Z | [#32016](https://github.com/qgis/QGIS/issues/32016) | [PR #36553](https://github.com/qgis/QGIS/pull/36553) | [PR #36595](https://github.com/qgis/QGIS/pull/36595) |
| Corregir rectángulo a partir de 3 puntos | [#35043](https://github.com/qgis/QGIS/issues/35043), [#35671](https://github.com/qgis/QGIS/issues/35671) | [PR #36523](https://github.com/qgis/QGIS/pull/36523) | [PR #36560](https://github.com/qgis/QGIS/pull/36560) |
| Permitir buscar qmlplugindump en distintas rutas | N/D | [PR #36513](https://github.com/qgis/QGIS/pull/36513) | N/D |
| Reparar la ausencia de palabras en el widget de configuración avanzada | [PR #35643](https://github.com/qgis/QGIS/pull/35643)#issuecomment-610215386 | [PR #36511](https://github.com/qgis/QGIS/pull/36511) | N/D |
| Corregir interpolación en cortar geometría | [PR #36514](https://github.com/qgis/QGIS/pull/36514) | [#33489](https://github.com/qgis/QGIS/issues/33489) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Interpretación errónea de código EPSG de un archivo PRJ en QGIS-dev (proj v7.1.0) | [#36111](https://github.com/qgis/QGIS/issues/36111) | [PROJ PR 2240](https://github.com/OSGeo/PROJ/pull/2240) | N/A: PROJ problema |
| QGIS crashes when adding file to geopackage -\> layer -\> field(BLOB) | [#30210](https://github.com/qgis/QGIS/issues/30210) | [PR #36722](https://github.com/qgis/QGIS/pull/36722) | [PR #36737](https://github.com/qgis/QGIS/pull/36737) |
| Mensaje de error malo en conexión fallida a WFS | [#29866](https://github.com/qgis/QGIS/issues/29866) | [PR #36717](https://github.com/qgis/QGIS/pull/36717) | [PR #36735](https://github.com/qgis/QGIS/pull/36735) |
| QGIS falla durante el re-renderizado de mapa tras cambiar CRS | [#29672](https://github.com/qgis/QGIS/issues/29672) | No se ejecuta | N/D |
| QGIS crashes when \"open directory\" is selected from the recent projects contextual menu | [#31630](https://github.com/qgis/QGIS/issues/31630) | [PR #36738](https://github.com/qgis/QGIS/pull/36738) | [PR #36755](https://github.com/qgis/QGIS/pull/36755) |
| Problema reproyectando rasters en CRS 54019 y 54042 | [#35512](https://github.com/qgis/QGIS/issues/35512) | [PROJ PR 2243](https://github.com/OSGeo/PROJ/pull/2243) | N/A: PROJ problema |
| Advertencia del Proveedor WFS - no se puede crear cache temporal de SpatiaLite al usar la instalación de paquete plano | [#36545](https://github.com/qgis/QGIS/issues/36545) | [PR #36745](https://github.com/qgis/QGIS/pull/36745) | N/D |
| Operación de transacción WFS usando URI GetCapabilities | [#34307](https://github.com/qgis/QGIS/issues/34307) | [PR #36746](https://github.com/qgis/QGIS/pull/36746) | N/D |
| QGis 3.10.2 falla al mostrar dos capas ráster de PostGIS | [#34456](https://github.com/qgis/QGIS/issues/34456) | - | N/D |
| QGIS 3.4.10 fallos - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | ya arreglado en máster | [PR #36751](https://github.com/qgis/QGIS/pull/36751) |
| Proveedor WMS pide contraseña SERVICE=WMTS en mayúsculas para detectar WMTS | [#36659](https://github.com/qgis/QGIS/issues/36659) | [PR #36752](https://github.com/qgis/QGIS/pull/36752) | [PR #36766](https://github.com/qgis/QGIS/pull/36766) |
| WCS DescribirCobertura responde siempre origen vacío | [#36504](https://github.com/qgis/QGIS/issues/36504) | [PR #36754](https://github.com/qgis/QGIS/pull/36754) | [PR #36781](https://github.com/qgis/QGIS/pull/36781) |
| Extensión errónea si la capa contiene punto en 0,0 | [#33823](https://github.com/qgis/QGIS/issues/33823) | No un error de QGIS. Corregido en GDAL 3.1 | N/D |
| Proyección no reconocida desde conversión Mapinfo | [#34471](https://github.com/qgis/QGIS/issues/34471) | [PR #36758](https://github.com/qgis/QGIS/pull/36758) | [PR #36783](https://github.com/qgis/QGIS/pull/36783) |
| QGIS falla(se congela al añadir un archivo CSV pesado como capa delimitada por texto | [#36392](https://github.com/qgis/QGIS/issues/36392) | [PR #36778](https://github.com/qgis/QGIS/pull/36778) | [PR #36810](https://github.com/qgis/QGIS/pull/36810) |
| QGIS 3.12 CRS desconocido o Selecciona Transformación | [#36837](https://github.com/qgis/QGIS/issues/36837) | [GDAL Commit 68133b8](https://github.com/OSGeo/gdal/commit/68133b8b6f724a581a5dcb19fbdcd657ddbd6c4c) | [GDAL Commit 6ae7f60](https://github.com/OSGeo/gdal/commit/6ae7f60a5914a2f16b8b1a94758f10e6621e4aca) |
| BIGTIFF error no es obvio en el registro de procesamiento | [#36867](https://github.com/qgis/QGIS/issues/36867) | [GDAL Commit cfc8e61](https://github.com/OSGeo/gdal/commit/cfc8e613ad86dd4b00604dd64df239916ccda135) | [GDAL Commit fb88e3c](https://github.com/OSGeo/gdal/commit/fb88e3ca5c8905fbcaab79e96a2bfc1c36f72d08) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Funcionalidad: Corrección de errores por Paul Blottiere
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir segfault al agregar una capa | [Mailing list](https://lists.osgeo.org/pipermail/qgis-developer/2020-June/061421.html) | [PR #36910](https://github.com/qgis/QGIS/pull/36910) | N/D |
| Corregir señal de conexión | Problema no reportado | [PR #35836](https://github.com/qgis/QGIS/pull/35836) | N/D |
| Actualizar la API para exportar una leyenda en JSON | Problema vinculante no reportado | [PR #36370](https://github.com/qgis/QGIS/pull/36370) | N/D |
| Volcado de núcleo si la capa de mosaico vectorial (archivo) no está disponible | [#36821](https://github.com/qgis/QGIS/issues/36821) | No se ejecuta | N/D |
| Fallo en abrir proyecto cuando la extensión del lienzo de mapa = nan | [#35899](https://github.com/qgis/QGIS/issues/35899) | No se ejecuta | N/D |
| Usando algunas funciones en la calculadora de ráster falla QGIS | [#35583](https://github.com/qgis/QGIS/issues/35583) | [PR #37273](https://github.com/qgis/QGIS/pull/37273) | N/D |
| Almacenamiento auxiliar no utilizable en capa no editable | [#30376](https://github.com/qgis/QGIS/issues/30376) | Ya corregido. Cerrado. | N/D |
| Corregir compilación con GCC 10, Qt/PyQt 5.15.0 y SIP 4.19.23 | [#37072](https://github.com/qgis/QGIS/issues/37072) | [PR #37116](https://github.com/qgis/QGIS/pull/37116) | [PR #37250](https://github.com/qgis/QGIS/pull/37250) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fallo reproducible usando QgsMapCanvas.items() con capas Oracle | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #36240](https://github.com/qgis/QGIS/pull/36240) | [PR #36246](https://github.com/qgis/QGIS/pull/36246) |
| Saltos de línea son ignorados en el panel de ayuda de expresión de usuario | [#36191](https://github.com/qgis/QGIS/issues/36191) | [PR #36249](https://github.com/qgis/QGIS/pull/36249) | [PR #36387](https://github.com/qgis/QGIS/pull/36387) |
| \"Edit user expression\" does not allow to rename the user expression | [#36192](https://github.com/qgis/QGIS/issues/36192) | [PR #36349](https://github.com/qgis/QGIS/pull/36349) | N/D |
| No puede cambiar etiquetas de clases de simbologías ráster | [#36172](https://github.com/qgis/QGIS/issues/36172) | [PR #36376](https://github.com/qgis/QGIS/pull/36376) | [PR #36533](https://github.com/qgis/QGIS/pull/36533) |
| Falla cuando la capa no está disponible | [#33300](https://github.com/qgis/QGIS/issues/33300) | No puede reproducir | N/D |
| Seleccionar por expresión devuelve resultados erróneos con enteros del campo división para archivos de forma | [#35449](https://github.com/qgis/QGIS/issues/35449) | [PR #2531](https://github.com/OSGeo/gdal/pull/2531) | N/D |
| Using concat(field1, field2) concatenates 0 instead of empty string (\'\') if any of the fields is NULL | [#36112](https://github.com/qgis/QGIS/issues/36112) | [PR #36521](https://github.com/qgis/QGIS/pull/36521) | [PR #36529](https://github.com/qgis/QGIS/pull/36529) |
| Atascado en la ventana de Proyecto reciente al abrir un archivo en blanco en 3.10.3 | [#34809](https://github.com/qgis/QGIS/issues/34809) | No puede reproducir | N/D |
| QGIS se bloquea al obtener elementos de la escena lienzzo de mapa si se identifican entidades | [#34457](https://github.com/qgis/QGIS/issues/34457) | [PR #36439](https://github.com/qgis/QGIS/pull/36439) | [PR #36450](https://github.com/qgis/QGIS/pull/36450) |
| ordenación en una columna que tiene una relación de valor es inconsistente | [#36114](https://github.com/qgis/QGIS/issues/36114) | [PR #36776](https://github.com/qgis/QGIS/pull/36776) | [PR #36887](https://github.com/qgis/QGIS/pull/36887) |
| Puntos perdidos (dependiendo de la escala en el lienzo) en la capa virtual basada en archivo sqlite | [#36054](https://github.com/qgis/QGIS/issues/36054) | [PR #36792](https://github.com/qgis/QGIS/pull/36792) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| El proyecto es modificado tan pronto como mueves el cursor en el lienzo | [#36796](https://github.com/qgis/QGIS/issues/36796) | [PR #36797](https://github.com/qgis/QGIS/pull/36797) | [PR #36718](https://github.com/qgis/QGIS/pull/36718) |
| Set filter applied to wrong \"version\" of table when multiple geometry types | [#34982](https://github.com/qgis/QGIS/issues/34982) | [PR #36801](https://github.com/qgis/QGIS/pull/36801)[PR #36718](https://github.com/qgis/QGIS/pull/36718) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Prestación: Corrección de errores por Bertrand Rix
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| La herramienta vértice inhabilita los parámetros de ajuste global | [#36229](https://github.com/qgis/QGIS/issues/36229) | [PR #36231](https://github.com/qgis/QGIS/pull/36231) | N/D |
| QGIS falla con el método QgsGeometry en colección vacía | [#36142](https://github.com/qgis/QGIS/issues/36142) | [PR #36351](https://github.com/qgis/QGIS/pull/36351) | N/D |
| Máscara selectiva: líneas fantasma sobre fondo oscuro | [#34650](https://github.com/qgis/QGIS/issues/34650) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/D |
| Máscara selectiva: lección con opacidad de la máscara | [#34947](https://github.com/qgis/QGIS/issues/34947) | [PR #36697](https://github.com/qgis/QGIS/pull/36697) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Prestación: Errores corregidos por Sebastien Peillet
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| \[Oracle\]Error on save geometries because wrong default values #34482 | [#34482](https://github.com/qgis/QGIS/issues/34482) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/D |
| Consulta inválida para valores por defecto de la columna fecha de una capa oracle | [#32401](https://github.com/qgis/QGIS/issues/32401) | [PR #36769](https://github.com/qgis/QGIS/pull/36769) | N/D |
| Campos desaparecidos  en Visibilidad por expresión para un grupo en un formulario de arrastrar/soltar | [#35196](https://github.com/qgis/QGIS/issues/35196) | [PR #36824](https://github.com/qgis/QGIS/pull/36824) | N/D |
| Escalas Personalizadas de Proyecto son mostradas con notación científica | [#36859](https://github.com/qgis/QGIS/issues/36859) | [PR #36860](https://github.com/qgis/QGIS/pull/36860) | N/D |
| Oracle: las tablas se enumeran una vez para Polígonos y una vez para MultiPolygons pero ambas muestran todas las geometrías | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) | N/D |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | [PR #37136](https://github.com/qgis/QGIS/pull/37136) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Prestación: Corrección de Errores por Alexander Bruy
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Copia de variables truncadas copia texto truncado, no original | [#30641](https://github.com/qgis/QGIS/issues/30641) | [PR #36554](https://github.com/qgis/QGIS/pull/36554) | [PR #36576](https://github.com/qgis/QGIS/pull/36576) |
| Desconectar el modo Multiedición no retorna a la vista de tabla | [#25099](https://github.com/qgis/QGIS/issues/25099) | [PR #36541](https://github.com/qgis/QGIS/pull/36541) | [PR #36630](https://github.com/qgis/QGIS/pull/36630) |
| Procesamiento GRASS: nombre de parámetro deasparecido | [#36520](https://github.com/qgis/QGIS/issues/36520) | [PR #36644](https://github.com/qgis/QGIS/pull/36644) | [PR #36690](https://github.com/qgis/QGIS/pull/36690) |
| Se corrigió la redirección de los resultados estándar a archivos temporales en algoritmos de procesamiento de GRASS | no reportado | [PR #36618](https://github.com/qgis/QGIS/pull/36618) | [PR #36684](https://github.com/qgis/QGIS/pull/36684) |
| Corregir el algortimo GRASS r.tileset | no reportado | [PR #36645](https://github.com/qgis/QGIS/pull/36645) | [PR #36695](https://github.com/qgis/QGIS/pull/36695) |
| QgsRasterTerrainAnalysisPlugin: probar el valor devuelto QgsRelief::processRaster() | [#17452](https://github.com/qgis/QGIS/issues/17452) | [PR #36731](https://github.com/qgis/QGIS/pull/36731) | [PR #36740](https://github.com/qgis/QGIS/pull/36740) |
| Histograma para estilo graduado en propiedades de capa desaparece cuando la ventana de propiedades de capa es muy pequeña | [#25197](https://github.com/qgis/QGIS/issues/25197) | [PR #36732](https://github.com/qgis/QGIS/pull/36732) | [PR #36749](https://github.com/qgis/QGIS/pull/36749) |
| Exporting image with atlas option \"Save World file\" lead to incorrect world file naming (text after dot is missing) | [#34523](https://github.com/qgis/QGIS/issues/34523) | [PR #36742](https://github.com/qgis/QGIS/pull/36742) | [PR #36748](https://github.com/qgis/QGIS/pull/36748) |
| \"Reloading QGIS\" from the crash report dialog fails to reopen the project | [#25532](https://github.com/qgis/QGIS/issues/25532) | [PR #36736](https://github.com/qgis/QGIS/pull/36736) | [PR #36750](https://github.com/qgis/QGIS/pull/36750) |
| Exportando estilo ráster a SLD solo funciona cuando el archivo saliente tiene el sufijo .sld | [#35944](https://github.com/qgis/QGIS/issues/35944) | [PR #36774](https://github.com/qgis/QGIS/pull/36774) | [PR #36795](https://github.com/qgis/QGIS/pull/36795) |
| \[Style Manager\] Missing Favorites category in the \"select by group\" dialog from \"Export symbols\" | [#27315](https://github.com/qgis/QGIS/issues/27315) | [PR #36793](https://github.com/qgis/QGIS/pull/36793) | no crítico |
| Interpolación TIN - problemas en formato y tamaño de salida ráster | [#31970](https://github.com/qgis/QGIS/issues/31970) | [PR #36822](https://github.com/qgis/QGIS/pull/36822) | [PR #36844](https://github.com/qgis/QGIS/pull/36844) |
| Layer panel: \"Edit Symbol\" does nothing if no symbol defined for a rule (in rule-based rendering) | [#23048](https://github.com/qgis/QGIS/issues/23048) | [PR #36954](https://github.com/qgis/QGIS/pull/36954) | no crítico |
| Cambio de atributos en los resultados del algoritmo del área de Servicio | no reportado | [PR #37074](https://github.com/qgis/QGIS/pull/37074), [PR #37097](https://github.com/qgis/QGIS/pull/37097) | N/D |
| El marco de prueba de procesamiento no aplica el redondeo a valores convertidos a números | no reportado | [PR #37234](https://github.com/qgis/QGIS/pull/37234) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir fuga en renderizador de malla 3D | no reportado | [Commit 4b5a63d](https://github.com/qgis/QGIS/commit/4b5a63d11b7ea5baf6931c8abf86e132c706c1be) | N/D |
| Corregir cuelgue al previsualizar representación de símbolos usando Metros en tamaño de Unidad de Mapa | [#28690](https://github.com/qgis/QGIS/issues/28690) | [Commit 7c6286f](https://github.com/qgis/QGIS/commit/7c6286f8dfb7cc24e5b06c9ab950d9dd55fac517) | No \-- too intrusive |
| Corregir fuente en editor de código CSS | no reportado | [Commit 63cb42c](https://github.com/qgis/QGIS/commit/63cb42c298ef5ab732274bce205e49171b797ae4) | no crítico |
| Se corrigió la representación de las expresiones del generador de geometría que devuelven los resultados de la colección de geometría | [#35356](https://github.com/qgis/QGIS/issues/35356) | [Commit be281c49](https://github.com/qgis/QGIS/commit/be281c49b7932a1d0d0e3cb4dce7af17f5b201a9) | No \-- too intrusive |
| \[processing\] Correctly expose date time inputs (and a bunch of others) as inputs for in-model expressions | [#37219](https://github.com/qgis/QGIS/issues/37219) | [Commit 281356a](https://github.com/qgis/QGIS/commit/281356aa4e951db5cd2782b53a7261c7343c4ca7) | N/D |
| Repara todas las advertencias de obsolescencia de Qt 5.14 | no reportado | [Commit 3717adc](https://github.com/qgis/QGIS/commit/3717adcef6315f4b9a0089bfc2393cede937b644) | No \-- too intrusive |
| \[symbology\] When rendering a multipart geometry, ensure that geometry generator symbol is only rendered once, instead of once per part | [#23730](https://github.com/qgis/QGIS/issues/23730) | [Commit d98fe9f](https://github.com/qgis/QGIS/commit/d98fe9f989f3b0677282acdf2ba99f4aa4fa08cc) | No \-- too intrusive |
| \[layout\] Make \"show feature count\" button apply to all selected indexes | [#37194](https://github.com/qgis/QGIS/issues/37194) | [Commit 671cebc](https://github.com/qgis/QGIS/commit/671cebcf817e2b6fc17ce0307edf7fa377b665d3) | No \-- too intrusive |
| Fix for container \"show as group box\" setting is lost when closing layer properties dialog | [#37205](https://github.com/qgis/QGIS/issues/37205) | [Commit 803f507](https://github.com/qgis/QGIS/commit/803f507d45f99534dbc03ab5300e6137da36cd59) | N/D |
| Uso de un lenguaje aún más contundente para disuadir a los usuarios de crear proyecciones personalizadas utilizando cadenas de Proj. | [#37204](https://github.com/qgis/QGIS/issues/37204) | [Commit 7ec4968](https://github.com/qgis/QGIS/commit/7ec4968aa9dcb2107b00c1caaeb6ae575498bc3c) | No \-- string change |
| Use \"markers\" terminology consistently in centroid fill widget | [#37106](https://github.com/qgis/QGIS/issues/37106) | [Commit 2596b6b](https://github.com/qgis/QGIS/commit/2596b6be858a17533d1e16fca8ff8afc5d222564) | No \-- string change |
| Corregir manejo de lista numerada en dox/PyQGIS API | no reportado | [Commit 74400c7](https://github.com/qgis/QGIS/commit/74400c7ff88d563dad74dad41860f9b603214973) | No |
| Corregir referencias cruzadas en documentos PyQGIS | no reportado | [Commit 81a9db9](https://github.com/qgis/QGIS/commit/81a9db9f57706cba9b11e4372dd1bf50fcd7bc6a) | No |
| \[layouts\] Fix attribute table sort order combined with feature filter results in empty tables | [#36341](https://github.com/qgis/QGIS/issues/36341) | [Commit 24897ab](https://github.com/qgis/QGIS/commit/24897ab86a7f11be196d8d705fa3307b05e0e53d) | N/D |
| Se corrigió la representación de texto destacado en etiquetas rotadas | [#36681](https://github.com/qgis/QGIS/issues/36681) | [Commit 2bb4aad](https://github.com/qgis/QGIS/commit/2bb4aad8c9b7238bd6ff6dc9a90a28c8625e859e) | N/D |
| Corregir manejo ca salida Grass en modelos de Procesamiento | [#36379](https://github.com/qgis/QGIS/issues/36379) | [Commit ef19911](https://github.com/qgis/QGIS/commit/ef19911f1132dc5720a4068f059a0322d7511e2b) |  |
| Corregir simplificación incorrecta de conjuntos de datos vectoriales a rectángulos en visualización de algunos CRS | [#36898](https://github.com/qgis/QGIS/issues/36898) | [Commit 47fba10](https://github.com/qgis/QGIS/commit/47fba106dd9d057e6691dcca392efacbe31ad9ff) | No \-- too intrusive |
| Arreglar el formato de elemento de lista en documentos de PyQGIS | no reportado | [Commit 84ec481](https://github.com/qgis/QGIS/commit/84ec481aa8f3d3bb487272122414c765e77a2ea2) | N/D |
| \[processing\] Fix manual entry of extent values in widget | [#36787](https://github.com/qgis/QGIS/issues/36787) | [Commit ccc34c7](https://github.com/qgis/QGIS/commit/ccc34c76e714e5f6f87d2a329ca048896eb4c87f) | N/D |
| \[decorations\] Use a proper ellipsoidal length calculation when calculating the size of the scalebar decoration | [#28407](https://github.com/qgis/QGIS/issues/28407) | [Commit af19cea](https://github.com/qgis/QGIS/commit/af19cea5acc90a6cc19d116dd35739059d0c5f83) | [PR 36718 Commit a91309d](https://github.com/qgis/QGIS/pull/36718/commits/a91309ddbc0a430dc3bbcf48070bc565296ac551) |
| Corregir la colección de tipos de geometrías trinagulares tras teselado | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit df46fba](https://github.com/qgis/QGIS/commit/df46fba33823415b8310c986795f8c51550a0fa6) | No \-- too intrusive |
| Corregir fallo vía QgsVectorFileWriter al escribir el tipo de geometría triangular | [#36638](https://github.com/qgis/QGIS/issues/36638) | [Commit e0c03f9](https://github.com/qgis/QGIS/commit/e0c03f9f0848490f358876ae5be6973961700bc9) | No \-- too intrusive |
| Corregir degradación en resultados de Teselado | [#37077](https://github.com/qgis/QGIS/issues/37077) | [Commit 61e7a5f](https://github.com/qgis/QGIS/commit/61e7a5fc90154bd4d35fea7d6cbd413ce61fa02e) | N/D |
| La cadena de subconjunto de capa fija se ignora cuando OGR se niega a aceptar una expresión de solicitud de entidad compilada | [#37073](https://github.com/qgis/QGIS/issues/37073) | [Commit b5b4221](https://github.com/qgis/QGIS/commit/b5b42218af5cbfca82f3b0a4d5a521e3d330f550) | [PR 36718 Commit f486cf6](https://github.com/qgis/QGIS/pull/36718/commits/f486cf6e6dadb2d0690f167620c90f4efddb3c4a) |
| \[legends\] Fix corrupted data defined legend rendering in layout designer | [#36765](https://github.com/qgis/QGIS/issues/36765) | [Commit 8d00ae8](https://github.com/qgis/QGIS/commit/8d00ae8638a09cb9a4c9ecd5d1fec3b352050cdd) | No \-- too intrusive |
| Evita algunas advertencias al inicio de QGIS | no reportado | [Commit 013f682](https://github.com/qgis/QGIS/commit/013f682bd3c6addd163a78d3776c578ae37377c6) | N/D |
| Coloca la pestaña 3D en propiedades de vector en la posición correcta | [#35010](https://github.com/qgis/QGIS/issues/35010) | [Commit ce9f5194](https://github.com/qgis/QGIS/commit/ce9f519468d46bb6fe6dd0bc68efd7d58129be68) | N/D |
| Corrige que la pestaña 3d no está activada al reabrir propiedades de capa vectorial | [#35011](https://github.com/qgis/QGIS/issues/35011) | [Commit 3c0ecbf](https://github.com/qgis/QGIS/commit/3c0ecbfd79e1924cd01143324cdc26fe4a68f748) | N/D |
| \[labeling\] Fix incorrect label placement after moving an \'unplaced\' label | no reportado | [Commit cbfb7f4](https://github.com/qgis/QGIS/commit/cbfb7f4ce25e10aab5f7b8cee147afb801042704) | [PR 36718 Commit 9189dec](https://github.com/qgis/QGIS/pull/36718/commits/9189dec7633b2eb6a1075bb35c2f90f6b90ba63a) |
| Don\'t block creation of new geopackages in vector save as dialog | no reportado | [Commit 8ccd127](https://github.com/qgis/QGIS/commit/8ccd127f4d8bf66fb04b6484147ed116acf66d91) | N/D |
| \[browser\] Refine refreshConnections method to avoid triggering a full refresh of ALL browser content | [#37007](https://github.com/qgis/QGIS/issues/37007) | [Commit a9d6b04](https://github.com/qgis/QGIS/commit/a9d6b04f776b80acd1a97f48c7ed10e3599618b6) | No \-- too intrusive |
| \[3d\] When showing edges, data defined polygon height was not accounted for | no reportado | [Commit e516231](https://github.com/qgis/QGIS/commit/e516231bb2854405ea78a0cec40ad96295e9f8c6) | N/D |
| Fixes for \"Show all\" labeling mode | no reportado | [Commit 2b91bd0](https://github.com/qgis/QGIS/commit/2b91bd0cafff66f14ceb49b104bf2f2cc6ae714d) | N/D |
| \[3d\] Fix reprojection of features shows no features | [#34824](https://github.com/qgis/QGIS/issues/34824) | [Commit 62bd026](https://github.com/qgis/QGIS/commit/62bd0267439a65f94a5cd9cb886bbb4e4780cdf0) | N/D |
| \[processing\] Add metadata setting for file destination parameters to avoid file overwrite confirmation prompt | [#37011](https://github.com/qgis/QGIS/issues/37011) | [Commit e81af2c](https://github.com/qgis/QGIS/commit/e81af2c9e10dc2a2e220c815cb9e531f7dba838d) | N/D |
| Evitar la representación antialiasing incorrecta de ciertos objetos (como las etiquetas de mapa) cuando no se desee | [#36964](https://github.com/qgis/QGIS/issues/36964) | [Commit bab83844](https://github.com/qgis/QGIS/commit/bab838444cb55fc479d2f3dfa3b19d8ce80e73af) | No \-- too intrusive |
| Asegúrese de que los campos requeridos por los fondos de símbolo de marcador para las etiquetas se obtengan al representar | [#36944](https://github.com/qgis/QGIS/issues/36944) | [Commit 8fb8e45](https://github.com/qgis/QGIS/commit/8fb8e45d516611f09bf28e3832c3c6214f16c4a2) | No \-- too intrusive |
| \"Fix \"\"zoom\"\" and \"\"flash\"\" features buttons have no effect when opening filter mode in attribute form\" | [#34506](https://github.com/qgis/QGIS/issues/34506) | [Commit 6b2795](https://github.com/qgis/QGIS/commit/6b27958948db2c88ae72b0b9ff99fc8aa8522bf2) | N/D |
| Evitar imágenes en miniatura de proyecto corrupto en algunas circunstancias | no reportado | [Commit f404e6e](https://github.com/qgis/QGIS/commit/f404e6e162df954ffb200d550b6c32375b7270c1) | N/D |
| Auto focus search box when opening \"add layer to legend\" dialog | [#36905](https://github.com/qgis/QGIS/issues/36905) | [Commit 019e494](https://github.com/qgis/QGIS/commit/019e494f1d61851ea192900a2cc9cce460d1ea73) | no crítico |
| \[processing\] Set correct output layer type for Point to Layer algorithm | [#36941](https://github.com/qgis/QGIS/issues/36941) | [Commit 7ee85cd](https://github.com/qgis/QGIS/commit/7ee85cd93cb5e0b623feaad2ef1ce9ea8f654bac) | N/D |
| \"Limit scope of Ctrl+C shortcut for copy features to canvas and for python console to console widget\" | [#27035](https://github.com/qgis/QGIS/issues/27035) (many others too) | [Commit 873716c](https://github.com/qgis/QGIS/commit/873716c6fa17298868060a6517205ad7bea78a72) | No \-- too intrusive |
| Recordar las posiciones de ventana en el diseñador de impresión | [#36907](https://github.com/qgis/QGIS/issues/36907) | [Commit 97d31d0](https://github.com/qgis/QGIS/commit/97d31d025fe2264afadcf6afcb3eb6ebcfe9e91d) | no crítico |
| Corregir fallo al ampliar demasiado las etiquetas | [#36346](https://github.com/qgis/QGIS/issues/36346) | [Commit 3aa5e56](https://github.com/qgis/QGIS/commit/3aa5e56d3c3dbb61f2a28c4874593aa401957ed3) | [Commit a22635b](https://github.com/qgis/QGIS/commit/a22635bb64ae6d2a46715bd1208463e22b6080ae) |
| \[processing\] Allow parent layer to be specified for field mapping inputs in models | [#26493](https://github.com/qgis/QGIS/issues/26493) | [Commit b8d4a39](https://github.com/qgis/QGIS/commit/b8d4a39b58465f93f45ed886e77411c194f44132) | No \-- too intrusive |
| Fix placement of message bar \'clear all\' menu arrow on hidpi screens | no reportado | [Commit 8a9975b](https://github.com/qgis/QGIS/commit/8a9975b4ff6b7a8a79bef05230db28754500fa40) | no crítico |
| Siempre refrescar la colección de complementos cuando es pulsado manualmente por el usuario | [#34351](https://github.com/qgis/QGIS/issues/34351) | [Commit 98603b7](https://github.com/qgis/QGIS/commit/98603b78660e05334c7b34ea3722533164f9553b) | [PR 36718 Commit 0fcf6dc](https://github.com/qgis/QGIS/pull/36718/commits/0fcf6dc08289fb549c9bace24a70ed4a50bdd959) |
| \[3d\] Expose 3d algorithms provider to Python | [#36661](https://github.com/qgis/QGIS/issues/36661) | [Commit 1f835df](https://github.com/qgis/QGIS/commit/1f835dfa9af51204ea1182df7bf722d84b223645) | No \-- too intrusive |
| \[symbology\] Don\'t force rasterized output when exporting point pattern fills | [#16100](https://github.com/qgis/QGIS/issues/16100) | [Commit 23396b7c](https://github.com/qgis/QGIS/commit/23396b7c864d00fc164db8c80d704a1ffc430ac1) | No \-- too intrusive |
| \[layouts\] Don\'t refresh the map canvas multiple times during atlas exports | [#30144](https://github.com/qgis/QGIS/issues/30144) | [Commit 57519e9](https://github.com/qgis/QGIS/commit/57519e9faa95fbfe6196134d9128caee48cb4b84) | no crítico |
| \[processing\] Fix double-evaluation of warp output parameter | [#30095](https://github.com/qgis/QGIS/issues/30095) | [Commit adeca2f](https://github.com/qgis/QGIS/commit/adeca2f586203913ae3702531b32579ed4c14344) |  |
| Corregir mensaje de advertencia incorrecto al apagar la previsualización del atlas | no reportado | [Commit 3b0af960](https://github.com/qgis/QGIS/commit/3b0af960dd90af15cbe32e2fd7642408031e70f5) | N/D |
| Acelerar las operaciones de la barra de mensajes cuando se muestran muchos mensajes | [#29698](https://github.com/qgis/QGIS/issues/29698) | [Commit 5dd29f0](https://github.com/qgis/QGIS/commit/5dd29f065e57fde532a21ae1bc9311aef9378455) | No \-- too intrusive |
| Corregir que el cálculo de la orientación mínima del cuadro delimitador es errónea en algunos casos | [#36632](https://github.com/qgis/QGIS/issues/36632) | [Commit 97d0988](https://github.com/qgis/QGIS/commit/97d098884a7889346739d61bd9048e9dcf942d11) | [PR 36718 Commit 68c6a0e](https://github.com/qgis/QGIS/pull/36718/commits/68c6a0e31dc58fa23621e872739df9efded6e6b7) |
| Asegurar que la opacidad del símbolo es siempre ignorada para selecciones | [#27859](https://github.com/qgis/QGIS/issues/27859) | [Commit 4de6a53](https://github.com/qgis/QGIS/commit/4de6a53235a6f7bd657c60d4f4d7160ed371d9df) | [PR 36718 Commit 99eb710](https://github.com/qgis/QGIS/pull/36718/commits/99eb710f89be0c6adc9acfdd888e366e6f2b796f) |
| Arreglar el orden aleatorio de los símbolos en el cuadro de diálogo Exportar símbolo | [#20572](https://github.com/qgis/QGIS/issues/20572) | [Commit 987310f](https://github.com/qgis/QGIS/commit/987310fe90de2b21deb5c2564eb051e1d72548b2) | [PR 36718 Commit bfa6058](https://github.com/qgis/QGIS/pull/36718/commits/bfa60586e10735a6b670cd349dd8b9efd2ab2762) |
| Permitir limpiar el campo de influencia del mapa de calor  | [#20256](https://github.com/qgis/QGIS/issues/20256) | [Commit 3961fa2](https://github.com/qgis/QGIS/commit/3961fa26f53e411c5c83b50e006df739ebda4c3e) | [PR 36718 Commit d2600d6](https://github.com/qgis/QGIS/pull/36718/commits/d2600d6d2cb765cb0641347ac342a74f663e4ba5) |
| Flag SAGA \'Merge Layers\' algorithm as having known issues | [#36375](https://github.com/qgis/QGIS/issues/36375) | [Commit f676c821](https://github.com/qgis/QGIS/commit/f676c821d9d9ff2d6e509d881ba2ea1853a34051) | N/D |
| Solución del problema extraño de Qt que viene de arriba donde un pintor con un pincel semitransparente sin un patrón sólido aplica incorrectamente la opacidad del pincel al lápiz al exportar a dispositivos de impresora | [#36580](https://github.com/qgis/QGIS/issues/36580) | [Commit 38c8218](https://github.com/qgis/QGIS/commit/38c82187a65d8b4833f2c633a69a4d937a8725eb) | [PR 36718 Commit a562b67](https://github.com/qgis/QGIS/pull/36718/commits/a562b678438d26c1f80486fdfff422d70c8c6329) |
| Mejorar el mensaje del complemento de vigilancia y Experiencia de Usuario | no reportado | [Commit 150b373](https://github.com/qgis/QGIS/commit/150b373c7ae61c0548ab0803f9b30a36b15e7ab4) | No \-- too intrusive |
| \"\[layouts\] Warn when previewing an atlas and a feature with no geometry is encountered, when one or more maps are set to be driven by atlas feature\" | [#36556](https://github.com/qgis/QGIS/issues/36556) | [Commit 6ce84d2](https://github.com/qgis/QGIS/commit/6ce84d2c347f49c9aae0c1953e2b2529228db430) | No \-- too intrusive |
| Avoid proj \'object is not a concatenated operation\' warnings | no reportado | [Commit 6baa209](https://github.com/qgis/QGIS/commit/6baa209285f452e5996537b1b0f1b5d924d5c59b) |  |
| \"Fix memory layers lose CRS definition if it does not have an authority associated with it\" | [#36241](https://github.com/qgis/QGIS/issues/36241) | [Commit e23a49a](https://github.com/qgis/QGIS/commit/e23a49a6b858cad9373c3bfb9ad66525622ce9ee) | [PR 36718 Commit c9350eb](https://github.com/qgis/QGIS/pull/36718/commits/c9350eb7439a29ac8ff3734cd7866f2403e3646e) |
| Implementar la detección de índice espacial para proveedor OGR | [#30530](https://github.com/qgis/QGIS/issues/30530) | [Commit f20801a](https://github.com/qgis/QGIS/commit/f20801a8bb3f23576e5e0d2abc6d3229e5044200) | [PR 36718 Commit 536906e](https://github.com/qgis/QGIS/pull/36718/commits/536906ec6375b70d88767e58a08550369a25d1a0) |
| Corregir título de diálogo incorrecto para propiedades de capa ráster | [#35510](https://github.com/qgis/QGIS/issues/35510) | [Commit 2099261](https://github.com/qgis/QGIS/commit/2099261230f82c5cd4439538e38754947c8f6bd6) | [PR 36718 Commit e809f48](https://github.com/qgis/QGIS/pull/36718/commits/e809f48cb9aaf03dfe8671c2d885f99b4a91922b) |
| Don\'t try to identify CRSes created just for ellipsoid definitions | no reportado | [Commit 15b318b](https://github.com/qgis/QGIS/commit/15b318b50de9131ed1dd6bbf73ae5eb7572579a7) | No \-- too intrusive |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Prestación: Corrección de errores por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Permitir ordenar tabla de atributos por campo no listado en la tabla | [#25671](https://github.com/qgis/QGIS/issues/25671) | [PR #36236](https://github.com/qgis/QGIS/pull/36236) | N/D |
| Corregir dependencias del árbol de capas (símbolos mostrar información y capa principal) | no reportado | [PR #37000](https://github.com/qgis/QGIS/pull/37000) | N/D |
| Corregir editor de Expresión: la verificación de sintaxis falla si la tabla está vacía | [#37100](https://github.com/qgis/QGIS/issues/37100) | [PR #37137](https://github.com/qgis/QGIS/pull/37137) | N/D |
| corregir ajuste de entidad en el widget de previsualización de expresión | [#37214](https://github.com/qgis/QGIS/issues/37214) | [PR #37221](https://github.com/qgis/QGIS/pull/37221) | N/D |
| Congelado al mostrar tabla de atributos de capa WFS | [#37224](https://github.com/qgis/QGIS/issues/37224) | no corregido todavía | N/D |
| Las búsquedas en tablas con más de 100 entradas muestran valores incorrectos en las partes del formulario de relación de Referencia | [#37266](https://github.com/qgis/QGIS/issues/37266) | [PR #37280](https://github.com/qgis/QGIS/pull/37280) | [PR #37286](https://github.com/qgis/QGIS/pull/37286) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Funcionalidad: Corrección de errores por Audun Ellertsen
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Soporte SpatiaLite para importar capas con campos binarios | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36744](https://github.com/qgis/QGIS/pull/36744) | N/D |
| Soporte PostGIS para importar capas con campos binarios | [#36705](https://github.com/qgis/QGIS/issues/36705) | [PR #36708](https://github.com/qgis/QGIS/pull/36708) | [PR #36720](https://github.com/qgis/QGIS/pull/36720) |

This feature was funded by [Kongsberg Digital](https://www.kongsberg.com/digital/)

This feature was developed by [Audun Ellertsen](https://github.com/audun/)

{{<content-end >}}
