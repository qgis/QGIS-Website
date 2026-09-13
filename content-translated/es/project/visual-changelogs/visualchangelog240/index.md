---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.4{#changelog24 }
Fecha de lanzamiento: 2014-06-27

Registro de cambios para la próxima versión de QGIS 2.4.0. El énfasis en esta versión se ha centrado mucho en el pulido y el rendimiento: hemos agregado muchas características nuevas, ajustes y mejoras para hacer que la interfaz de usuario sea más consistente y de aspecto profesional (y con suerte más fácil de usar). Al compositor (utilizado para crear mapas listos para imprimir) se le ha hecho mucho trabajo para que sea una plataforma más viable para crear grandes resultados cartográficos.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Nos gustaría agradecer a los desarrolladores, documentadores, probadores y a las muchas personas que ofrecen su tiempo y esfuerzo voluntario (o financian a personas que lo hacen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente nos gustaría agradecer a nuestros patrocinadores oficiales por el soporte financiero invalorable que proveen a este proyecto:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## General
### Feature: Generate band name with NetCDF EXTRA_DIM
El NetCDF proporcionó información dimensional adicional. Esta información proporciona metadatos en cada banda. Estos metadatos se pueden usar para explicar el nombre de cada banda. Por ejemplo, las bandas de un archivo NetCDF representan la temperatura a una profundidad dada. Para el usuario, es más fácil seleccionar una banda con información de profundidad, en lugar de solo el número de banda.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Característica: Aplicando escala y desplazamiento a datos ráster
En algunas fuentes de datos ráster, los datos se almacenan como números enteros con una escala y un desplazamiento en los metadatos. La escala y el desplazamiento se pueden usar para obtener los datos correctos. QGIS los aplica a datos ráster para proveer a los usuarios información correcta para leyenda, histograma e identificación.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Característica: Barra de cálculo rápido de campo en tabla de atributo
Tenemos una grandiosa nueva característica para aquellos trabajando con campos calculados en tablas de atributo vector. La nueva barra de cálculo rápido le permite rápidamente y fácilmente actualizar los valores en una columna en la tabla de atributos.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Característica: Modos de previsualización de color en el diseñador y tela del mapa
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Característica: archivos Capa QLR QGIS
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Prestación: Nuevas funciones de expresión
Tenemos algunas funciones nuevas disponibles en el contructor de expresiones.
- caja delimitadora (bordes)
- bounding box width & height (bounds_width/bounds_height)
- min/max x/y coordinates (xmin/xmax/ymin/ymax)
- nueva función wordwrap que devuelve una cadena ajustada a un número máximo/mínimo de caracteres

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Característica: Copia, pega y arrastra y larga colores
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Característica: Reproducción multipropósito
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Etiquetando
### Característica: Etiquetar elemenots múltiples veces
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Compositor de Mapa
### Característica: Mejoras a los elementos imagen del diseñador
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Característica: Modos de escala predefinidos para mapas del atlas
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Característica: Tablas de atributo mejoradas en el diseñador
Hemos hecho varias mejoras a la abilidad para mostrar tablas en sus bosquejos del diseñador:
- Se ha adicionado soporte para reordenar columnas dentro de una tabla
- Soporte adicionado para columnas basadas en expresiones
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Los contenidos de tabla pueden ser filtrados por una expresión

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Característica: Mejoras generales del diseñador
Hay varias adiciones al creador de mapas para facilitarle la vida mientras trabaja en el modo de composición de mapas:
- Botón adicionado para ver la extensión actual de elemento de mapa en  la lona principal del mapa
- Abilidad para exportar imágenes SVG desde el diseñador con capas
- Definir estilo de unión y extremo para barras de escala
- Soporte para establecer el estilo de unión de línea para marcos de elementos

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Característica: Mejoras a los marcos HTML
Se han mejorado los marcos HTML en el compositor. Hay un nuevo botón **agregar marco** que se puede usar para crear manualmente múltiples marcos vinculados. También hemos mejorado nuestra lógica de salto de página, lo que hace que sea menos probable que obtenga saltos de página que corten la mitad de las líneas de texto al paginar marcos HTML.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Plugins
### Característica: Complemento Cliente Catálogo MetaSearch
MetaSearch es un complemento QGIS para interactuar con los servicios de catálogo de metadatos, que admite el estándar OGC Catalog Service for the Web (CSW). Este complemento proporciona un enfoque fácil e intuitivo y una interfaz fácil de usar para buscar en los catálogos de metadatos dentro de QGIS y ahora se proporciona de forma predeterminada con el producto central QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Simbología
### Característica: Estilo de llenado shapeburst
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Característica: Opción para desplazar la ubicación de línea marcador
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Característica: Nuevo visualizador de polígono invertido
Se ha agregado un nuevo renderizador para las entidades de polígono, lo que le permite diseñar todo **fuera** de sus polígonos. Esto puede ser útil para resaltar áreas o para crear máscaras cartográficas. Cuando se usa con un nuevo estilo de ráfaga de forma, ahora puede producir resultados como se muestra en la imagen para esta entrada.

**Nota:** La nueva versión del complemento de máscara ayuda a crear fácilmente capas de máscara a partir de la selección actual, etiquetar entidades solo en esas áreas y generar una máscara automática en la generación de mapas Atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Característica: Guardando y recuperando estilos con capas Spatialite
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
