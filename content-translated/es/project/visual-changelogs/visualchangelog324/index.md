---
HasBanner: false
draft: false
releaseDate: '2022-02-18'
section: proyecto
sidebar: true
title: Registro de cambios de QGIS 3.24
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios de QGIS 3.24{#changelog324 }
![image1](images/projects/dce49bc182a307d8b4d60cfa0ba8caede109cf69.png)

Fecha de lanzamiento: 2022-02-18

In Memorium: This release is named \'Tisler\' after a small Norwegian island that was a favourite visiting place of Håvard Tveite who passed away in May 2021. Håvard was a very active member of the QGIS community, providing valuable input to the documentation, developing numerous plugins, and taking care of the QGIS Resources Sharing Repository to name just a few of his contributions. The map on the QGIS 3.24 splash screen is an orienteering map that Håvard has created. He liked spending some time each year map-making at Tisler.

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on youtube at <https://youtu.be/gVgR4Oxqtkk>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/gVgR4Oxqtkk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## Interfaz de usuario
### Característica: Recupere extensiones de mapas directamente desde mapas de diseño y marcadores
Esto le ahorrará mucho tiempo. El widget de extensión en QGIS ahora le permite recuperar directamente y hacer coincidir la extensión de los mapas de los marcadores y diseños en su proyecto.

![image3](images/entries/2dc42086879501e4645c8f6b7bbaba0f90fa4164.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Característica: Creación más fácil de sistemas de referencia de coordenadas personalizados
We\'ve added a new option when selecting a Coordinate Reference System (CRS) which allows you to just directly enter a custom CRS definition (from proj or WKT strings), instead of requiring you to specifically add these custom CRS to the projection database first.

It\'s much friendlier when you just want to define a custom projection for a single-purpose use, e.g. an overview map with a projection designed for a particular latitude and longitude location.

![image4](images/entries/c0053c5fd55a77bc13f8e92bbf9d27ecd57535e4.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Simbología
### Feature: Marker/hash line: offsets along line by \"percent\" of line length (and negative offsets!)
Ahora puede especificar el *desplazamiento a lo largo de la línea* en porcentaje para los tipos de capa de símbolos de marcador y de línea de hash. (Estos desplazamientos se tratan como porcentajes de la longitud total de la línea).

Además, cuando el ajuste *desplazamiento a lo largo de la línea* para una capa de símbolo de marcador o línea de hash es mayor que el tamaño de un **anillo cerrado**, QGIS tratará ahora el desplazamiento como si continuara haciendo un bucle alrededor del anillo. Por ejemplo, si se establece un desfase del 150%, el desfase se tratará como el 50% de la longitud del anillo cerrado.

Por último, también hemos hecho posible especificar un *desplazamiento negativo a lo largo de la línea* para un anillo cerrado. Los desplazamientos negativos se calculan hacia atrás a lo largo del anillo.

![image5](images/entries/78402d91402744c434c0501a4fa078b686f31251.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Control de si las colocaciones del primer/último vértice aplican a cada parte de geometrías multiparte
Esta nueva opción de simbología para los tipos de símbolo Marcador y Línea de guiones permite controlar si las opciones de colocación de Primer y Último vértice deben aplicarse a cada parte de una línea (o polígono) multiparte individualmente, o sólo al primer y último vértice de toda la geometría multiparte.

![image6](images/entries/49ea4f5c6e67426b41fefcdcb38cb3625e03bd34.gif)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Marker/hash line \"on vertices\" placement option replaced by \"on inner vertices\"
El nuevo modo *En vértices interiores* coloca los símbolos sólo en todos los vértices **interiores** (es decir, todos los vértices excepto el primero o el último).

Previously, the old \"Vertex\" mode put symbols on the first and last vertex as well as all inner vertices, making it basically impossible to style a line with a **different** marker on the first or last vertex to the rest of the line\'s vertices. With the new *On Inner Vertices* option it\'s easy to create a style where a line has a different marker on the first or last vertex vs the rest of the vertices!

(This change is paired nicely with the switch to using checkboxes for the placement options \-- to get a marker to show on all vertices, just make sure the first, last and inner vertices options are checked).

![image7](images/entries/4eaf67cc6d084f5f22f2dea6bdac9b62ab0ae25a.webp)

Esta prestación ha sido financiada por North Road, gracias a SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Opciones de colocación en capas de símbolo marcador y línea hash son ahora casillas de verificación en lugar de botones mutuamente excluyentes
Esta mejora facilita considerablemente la creación de líneas de marcadores (o hash) con los marcadores en el primer **y** último vértice (entre otras combinaciones útiles).

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Controle el modelo de color usado al interpolar rampas de degradado
Al renderizar una rampa de degradado, algunas combinaciones de colores de degradado harán que la rampa atraviese tonos medios grises turbios si la interpolación se realiza utilizando los canales rojo/verde/azul de forma independiente. Un enfoque alternativo consiste en interpolar los colores a través de sus canales de tono/saturación/luminosidad o valor. Este enfoque puede evitar estos tonos medios desaturados, lo que resulta en gradientes visualmente más agradables.

We now allow the color specifcation to be set per stop in a multi-stop color gradient to give users control over which interpolation technique to use. There\'s also an option to control the direction which interpolation should follow for the Hue component of a HSL/HSV color spec interpolation,m which can help avoid unwanted interpolation through the entire rainbow hue spectrum in some circumstances!

This [video](https://user-images.githubusercontent.com/1829991/140872101-b6d7dd66-3595-4584-8e1a-0a384f5ec82d.mp4) shows the difference in mid-tones of a color ramp, where the RGB interpolation results in murky colors, while the HSL/HSV interpolation remains nice and vibrant.

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Miniaturas redimensionables en el cuadro de diálogo del administrador de estilo
We\'ve added a new slider to control the size of thumbnails shown in the style manager dialog, because sometimes these thumbnail sizes are just too small to get a good representation of a symbol!

![image8](images/entries/48ee80e3b2307562c724664ce3d59fa8ac7cf477.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: \"Lineburst\" symbols
We\'ve added a brand new \"Lineburst\" symbol layer type, which renders a gradient along the **width** of a line (as opposed to the Interpolated Line renderer, which renders a gradient along the **length** of a line). It\'s just like the Shapeburst fill symbol type, but for lines!

![image9](images/entries/e205aa8113a089b9911726a45b0c198e79af0b6b.webp)

This feature was funded by [North Road, thanks to SLYR!](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: \"Raster Line\" symbols
We\'re super-excited to bring you this brand new line symbol type, which allows you to render a raster image following a line feature\'s shape. This symbol type opens a whole new realm of possibilities for QGIS symbology, and is especially useful when creating maps in a hand drawn or painted style.

Hay opciones disponibles para controlar:
- la ruta de la imagen (incluida la ruta definida por los datos)
- ancho de línea
- opacidad
- estilos de unión de líneas y tapas

![image10](images/entries/fa66229ff4db5e654b673579cde7d58dff4cc85d.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Elección del comportamiento de recorte para rellenos de patrón de linea
Ahora puede controlar cómo se recortan las líneas de un símbolo de relleno de patrón de línea a las formas poligonales. Las opciones disponibles son:
- **Recortar sólo durante el renderizado**: se crean líneas que cubren todo el *cuadro delimitador* del objeto espacial que luego se recortan mientras se dibuja. Los extremos de la línea (principio y final) no serán visibles (es el mismo comportamiento que en versiones anteriores de QGIS).
- **Recortar Líneas Antes de Renderizar**: las líneas son recortadas a la *forma exacta* del polígono antes de renderizar. Los extremos de la línea (incluyendo estilos de final, símbolos marcadores de inicio/final de línea, etc) serán visibles y pueden en algunas ocasiones extenderse fuera del polígono (dependiendo de los ajustes de símbolos de línea).
- **Sin Recortes**: no se realiza ningún recorte - las lineas cubrirán todo el cuadro delimitador de la característica

![image11](images/entries/d6195c4a0b58fd7a1f076e7d74dc82d85f453fcc.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Renderización mejorada de los rellenos de patrón de línea
Cuando se exporta a un formato vectorial (p. ej. PDF o SVG) o o cuando un subsímbolo de línea tiene propiedades dinámicas (definidas por los datos), conmutamos ahora automáticamente a un enfoque basado en línea a línea para renderizar el relleno. (Anteriormente, siempre se utilizó un enfoque de patrón de mosaico, que a menudo resultaba en artefactos indeseables o costuras visible en el patrón).

Algunos de los muchos beneficios de este cambio son:
- Smaller PDF/SVG output file sizes \-- the line pattern fills aren\'t stored as raster images in the output so the overall file size will often be much smaller
- Los archivos exportados PDF/SVG son más fáciles de modificar en aplicaciones externas (como Inkscape o Adobe Illustrator) para su postproducción, puesto que cada linea individual en la plantilla puede ser modificada.
- Better quality PDF/SVG outputs, since the fill isn\'t DPI dependent and looks pixel perfect regardless of how far in you zoom
- Sin artefactos visibles en ciertos ángulos, distancias o con ciertos estilos de símbolo de linea

Y aún más exactamente, abre la puerta a un rango de nuevos estilos de símbolos, por ejemplo:
- patrones de línea donde cada linea cambia de color/anchura/puntuación/ etc.
- patrones de línea con símbolos marcadores de linea en el punto central/etc
- efectos de generador de geometría por línea, p. ej. patrones de línea ondulada, estilos de lñinea dibujada a mano, etc

![image12](images/entries/ddab2e2d054c9535c86e7a94c2045e9ffa2b0b48.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Ángulo de rotación por relleno de patrón de puntos
Ahora puede especificar un ángulo de rotación opcional para el relleno de patrón de puntos, lo que hace que todo el patrón de puntos tenga un ángulo. ¡Esto puede ser extremadamente útil cuando se superponen múltiples rellenos de patrón de puntos!

![image13](images/entries/f43cb7d8a69d6765a0873888cbe6cc7f17bb8c51.gif)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Característica: Desplazamientos de puntos aleatorios para relleno de patrón de puntos
This (optional) setting allows each point in a point pattern fill to be randomly shifted up to the specified maximum distance in the x or y direction. You can specify the maximum offset in millimeters, points, map units, or even \"percentage\" units (where percentage is relative to the pattern width or height).

You can set an optional random number seed to avoid the symbol patterns \"jumping\" around between map refreshes. Data defined overrides are also supported.

The main difference between this new setting and the existing *random marker fill* symbol type is that the random offset with a point pattern allows for quasi-\"regular\" placement of markers \-- because the points in the pattern are effectively constrained to a grid, this allows creation of semi-random fills which don\'t have empty areas or overlapping markers. (As opposed to the random marker fill, which will always place points completely randomly\... sometimes resulting in visual clusters of points or unwanted empty areas).

![image14](images/entries/1ccd4651fd333335c687c1195322df4b49f59b6f.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Ajuste del modo de referencia de coordenadas para las capas de símbolos de relleno de patrones de líneas y puntos
Las capas de símbolos de relleno de patrones de líneas y puntos tienen un nuevo ajuste de modo de referencia de coordenadas para ajustar el anclaje de los patrones. Desde un punto de vista práctico, esto permite que los patrones se alineen perfectamente entre elementos adyacentes y superpuestos.

![relief](https://changelog.qgis.orgimages/entries/e36d0e51676a76cf1655adc1453fd2a2e8a449b6.gif)

![image16](images/entries/afd8b9d9b32f494472a3787323764d9266f6f6ff.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Control del recorte de marcadores para rellenos de patrones de puntos
Esta nueva opción le permite controlar cómo se recortan los marcadores en un relleno de patrón de puntos. Las opciones disponibles incluyen:
- **Clip to shape**: markers will be clipped by the boundary of the shape, so \"cut off\" markers may be visible (same behaviour as previous QGIS versions)
- **Centroide del marcador dentro de la forma**: los marcadores sólo se dibujarán si su centroide se encuentra dentro de la forma, y los marcadores no se recortarán a los límites de la forma.
- **Marcador completamente dentro de la forma**: los marcadores sólo se dibujarán si encajan completamente dentro de la forma.
- **Sin recorte**: se dibujarán símbolos de marcador completos si **cualquier** parte del marcador se encuentra dentro de la forma.

![image17](images/entries/4fcff106088f49e8828b8dfcbaa0867c7735aa71.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Funciones de expresión para crear ondas triangulares/cuadradas/curvas
We\'ve added some new expression functions which produce \"wavy lines\" along geometry boundaries. Multiple wave shapes are available, including:
- Onda (sinusoidal)
- Triangular
- Cuadrado

Además, también se han añadido funciones de expresión para crear ondas de forma regular o con aleatorización.

Cuando se utilizan con generadores de geometría, estas expresiones pueden emplearse para crear efectos cartográficos muy avanzados.

![image18](images/entries/fc0f7dd38a16926620e0d1d62cce022b9d2618e5.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Etiquetando
### Feature: \"Percentage\" units for text buffer size, shadow offset and blur radius
Ahora los tamaños del búfer de texto, el desplazamiento de la sombra y el radio de desenfoque de la sombra pueden establecerse como porcentaje del tamaño de la fuente. Esto es deseable, ya que permite la creación de formatos de texto en los que los componentes se escalan de forma agradable a medida que cambia el tamaño del texto, en lugar de tener tamaños fijos de búfer/sombra que deben ajustarse de forma independiente cuando cambia el tamaño del texto.

![image19](images/entries/4e05a38133304694f05b0c70e73750436581f3ef.gif)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Posiciones de etiquetas definidas por geometrías de puntos
Ahora puede establecer la colocación definida por los datos de las etiquetas para que esté vinculada a un campo geométrico de punto o a una expresión. (Las versiones anteriores de QGIS sólo permitían definir la ubicación de los datos mediante dos campos numéricos x e y separados).

Este cambio también permite utilizar la herramienta *Mover Etiqueta* para cambiar la posición de una etiqueta que está vinculada a un campo de geometría de punto, haciendo que la nueva posición de la etiqueta se almacene como geometría de punto en ese atributo.

![image20](images/entries/0d4347d53e5b2383aab0b5207dcc9dd6317faf3f.webp)

Esta prestación ha sido financiada por el grupo suizo de usuarios de QGIS

This feature was developed by [Damiano Lombardi](http://OPENGIS.ch)
### Prestación: Texto estirado para etiquetas y formatos de texto
This improvement allows your text to be horizontally stretched or condensed by a percentage factor. It\'s often handy for tweaking the widths of fonts to fit a bit of extra text into labels (when used sparingly, that is\... you can certainly abuse font stretching with some horrendous results!)

**Note:** This improvement requires Qt 6.3+ or KDE\'s 5.15 fork. (On other builds the stretch options are hidden and can\'t be set)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Representación
### Prestación: Renderizado de capas como grupos
Se trata de otra interesante mejora cartográfica que abre un nuevo campo para la simbología y la visualización de mapas en QGIS.

Prior to this improvement, QGIS supported grouping layers within the layer tree as a means of structuring projects, but these groups had no impact on how the component layers were rendered. In QGIS 3.24 we\'ve introduced a new option allowing these layer groups to \"*Render as Group*\", which causes all the component layers to be rendered as a single flattened object during map renders.

Esta opción está disponible en el panel de estilos de capa siempre que se seleccione una capa de grupo. Este panel también le permite controlar el aspecto del grupo en su conjunto, con opciones para la opacidad general del grupo, el modo de fusión y los efectos de capa.

Additionally, when a layer is contained in a group which has the new *Render as Group* option activated, new blending modes will be available which perform \"clipping\" style operations during the render. These allow you to achieve some very powerful results, such as clipping the render of one layer\'s content by the content in a second \"mask\" layer!

![image21](images/entries/aa14990a802d70d0302c5441ea955248bc1dd40d.webp)

Esta prestación ha sido financiada por Andrew Fletcher.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Support for \"Line pattern\" when converting Mapbox GL vector tile layer styles
Haciendo uso de la nueva capa de símbolos de línea ráster, QGIS 3.24 ahora renderiza correctamente el estilo de patrón de línea Mapbox GL para las capas de mosaico vectorial recién añadidas.

![image22](images/entries/8a1550b27e8d8252b4b79267b0cef1c72ff10659.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Admite estilos de fondo para capas de mosaico vectorial con estilo Mapbox GL.
Ahora renderizamos correctamente cualquier estilo de fondo predefinido presente en las capas de mosaico vectorial con estilo GL de Mapbox. Esto mejora notablemente el aspecto de las capas de mosaico vectorial con estilos oscuros.

![image23](images/entries/38d362b08812fcb3d9129f2f8881d3bf02e77703.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Objetos 3D
### Prestación: Respeto de la ordenación Z al renderizar nubes de puntos en 2D
We\'ve added an option to render point clouds according to their Z-order in 2D map views. With the new *bottom-to-top* ordering option enabled, points with larger Z values will cover lower points \-- resulting in the appearance of a true orthographic photo. There\'s also an option for reverse sorting (*top-to-bottom*), where the scene appears as if viewed from below.

![image24](images/entries/7edd9bfb77f56b17d2c74c43a8ca1a8ab7456298.webp)

This feature was funded by [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Acoplar/desacoplar vistas 3D
We\'ve been aware that using dock widgets for 3D maps can be inconvenient, and in many situations these are frustrating to resize and move as they are prone to re-dock as you adjust their sizes! With QGIS 3.24 we added the ability to switch 3D maps from a dockable widget to a top-level window (and back to a dock widget), so that these map views can now be managed, resized and moved just like a standard application window.

![image25](images/entries/0ee88178c41fb6f57e0cc9ebe92256c58cfd9f55.gif)

This feature was funded by [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

This feature was developed by [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Gestor de vistas de mapas en 3D
Previously, if you closed a 3D map view and then saved your project, the 3D map view and all its settings would be lost when you reopen that project. So in QGIS 3.24 we\'ve added a \"*3D map view manager\"* that takes care of listing, removing, renaming and duplicating 3D map views in your projects!

We\'ve also added a new \"*3D Map Views*\" menu, which contains all your created 3D map views for easy access!

![image26](images/entries/4a38d45cc87a5068e3729f2d0091067178975164.webp)

This feature was funded by [Crowdfunding: Enhancing elevation data and point clouds in QGIS](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis/)

This feature was developed by [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Navegación por la cámara mejorada
The default navigation mode in earlier versions of QGIS would sometimes behave strangely when moving around, rotating or zooming in/out. A lot of effort went into improvements of the camera control, so since QGIS 3.24 the camera navigation\'s behavior should feel more natural and similar to other 3D mapping software.

For more details, see [Fixing terrain and camera issues in 3D](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/215)

Esta prestación ha sido financiada por una subvención de QGIS.org (2021)

This feature was developed by [Nedjima Belgacem (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Diseño de impresión
### Prestación: Capacidades completas de renderizado de texto para etiquetas de texto de diseño
En versiones anteriores de QGIS había que recurrir a trucos como el uso de HTML y CSS para añadir efectos como sombras al texto de los diseños de mapas. ¡Se acabaron los trucos! En 3.24 le permitimos utilizar las propiedades familiares de las opciones de etiquetado de texto también para el texto en los diseños. Esto significa que ahora puedes añadir sombras, topes de texto, fondos, espaciado entre letras y palabras, etc. a los elementos de texto de tus diseños.

![image27](images/entries/42e4f30b9e1adc647a7b7ef774186d8b90374a9f.gif)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Expresiones
### Feature: geometry_type function
The new `geometry_type` function returns the high-level type of a geometry (i.e. \'Point\', \'Line\' or \'Polygon\').

![image28](images/entries/503ad2cbcbf9b3ac0b46a624fe4d501dbf2db89d.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Las intersecciones superpuestas se ordenan por tamaño de intersección
We have added further enhancements to the `overlay_intersects` function. The change adds two new optional arguments to the existing function:
- **return_details**: only valid when used with an expression, set this to true to return a list of maps containing (key names in quotes) the feature \'id\', the expression \'result\' and the \'overlap\' value, the \'radius\' of the maximum inscribed circle is also returned when the target layer is a polygon.
- **sort_by_intersection_size**: only valid when used with an expression, set this to true to return the results ordered by the overlap value in descending order.

![image29](images/entries/74ef8569e9142ace7235302fd562a6729821ee7e.webp)

This feature was funded by [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Mostrar todos los nombres de campo de capa al construir expresiones
As a handy time-saver, we now make a list of all field names from all layers in your project available directly in the expression builder. If you double-click any of these field names, they\'ll be added to your expression as string values (`'field_name'`).

![image30](images/entries/e08ee30c934aa44f05b3037531e9502fd0d1feee.webp)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: represent_attributes function
Esta nueva función devuelve un mapa con todos los nombres de atributos (campos) como claves y los valores de representación configurados como valores. El valor de representación de los atributos depende del tipo de widget configurado para cada atributo.

La función puede utilizarse con cero, uno o más argumentos:
- Si se llama sin parámetros, la función devolverá la representación de los atributos de la **objeto espacial actual** en la capa actual.
- If called with a \'feature\' parameter only, the function will return the representation of the attributes of the specified feature from the current layer.
- If called with a \'layer\' and a \'feature\' parameter, the function will return the representation of the attributes of the specified feature from the specified layer.

![image31](images/entries/2d81dc010346379fa47fb7f2e301f41d0b7f42fb.webp)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Optional minimum overlap area and circle radius for overlay_intersection
We have added two optional arguments to the `overlay_intersection()` expression function:
- `min_overlap`: for polygons an optional minimum area in current feature squared units for the intersection (if the intersection results in multiple polygons the intersection will be returned if at least one of the polygons has an area greater or equal to the value), for lines an optional minimum length in current feature units (if the intersection results in multiple lines the intersection will be returned if at least one of the lines has a length greater or equal to the value)
- `min_inscribed_circle_radius`: for polygons only an optional minimum radius in current feature units for the maximum inscribed circle of the intersection (if the intersection results in multiple polygons the intersection will be returned if at least one of the polygons has a radius for the maximum inscribed circle greater or equal to the value). Read more on the underlying GEOS predicate, as described in PostGIS ST_MaximumInscribedCircle function.

![image32](images/entries/c94c8c8c3879b90c6c0a602d8d932c505a9a6868.webp)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: map_prefix_keys function
In QGIS 3.24 we\'ve added a new `map_prefix_keys` function that takes a map and a prefix, the function returns a map with all keys prefixed by the prefix.

Example: `map_prefix_keys(map('1','one','2','two'), 'prefix-')`

returns: `{ 'prefix-1': 'one', 'prefix-2': 'two' }`

![image33](images/entries/f8f2becdcaaa40fb07b3bb875928b3edcbdedcfc.webp)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: densify_by_count and densify_by_distance functions
Esta funcionalidad, que antes sólo estaba disponible a través de la caja de herramientas de Procesos, ¡ahora se puede utilizar en las expresiones!

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Rotate parts of multi-part geometries independently with \"rotate\" expression function
The new \"per_part\" option for the \"rotate\" expression function allows you to rotate each part of a multi-part geometry around the center of each part (instead of the center of the geometry as a whole). This enhancement is designed to help out symbology when the rotate function is used as a cartographic tool as part of a geometry generator symbol layer.

![image34](images/entries/c70899168f010b55fedad4b28e90aab687158a80.gif)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: apply_dash_pattern function
Esta nueva e interesante función de expresión aplica un patrón de líneas discontinuas a una geometría, devolviendo una geometría MultiLineString que es la geometría de entrada trazada a lo largo de cada línea (o anillo) utilizando un patrón de líneas discontinuas.

Rules can be set to control how the dash pattern is adjusted at line endings. If you specify a start rule or end rule, then the \"adjustment\" option defines whether both dash and gaps, or only dash or gap sizes are adjusted to apply these rules.

También puede establecer un desplazamiento de patrón opcional para especificar en qué punto del patrón debe comenzar el resultado.

![image35](images/entries/ba54e83091593860e9e61425565b085ad082f5ff.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: función de escala
This new expression function allows you to scale (resize) a geometry. Just like the \'rotate\' function, the function accepts an optional point position to apply the scaling from. If no anchor point is not specified then scaling is done from the center of the geometry\'s bounding box.

![image36](images/entries/6dd5dd5783c501d294a289cfbdabf9ce58b4c481.webp)

This feature was funded by [North Road, thanks to SLYR](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Filter by multiple attributes for get_feature function
We extended the `get_feature` function to allow multi-attribute filtering, by adding an option to pass an array of filter values to the input.

This feature was developed by [Alex](https://github.com/roya0045)
## Administración de datos
### Prestación: Soporte multiedición para el editor de relaciones
We\'ve added a new multi edit mode for the relation editor, which allows the rapid addition of child features to multiple parent features. This improves efficiency for data management operations, such as the ability to select multiple trees and adding a maintenance item to all of them in one click.

![image37](images/entries/c610c679ea1906d12ca9d4893e60796fd8a3ecab.gif)

This feature was funded by [QGIS Model Baker](https://opengisch.github.io/QgisModelBaker)

This feature was developed by [Damiano Lombardi, OPENGIS.ch](https://github.com/domi4484)
## Metadatos y Metabúsqueda
### Prestación: Compatibilidad con la API OGC - Registros en metabúsqueda
We updated the MetaSearch tool to provide support for the [OGC API - Records](https://ogcapi.ogc.org/records) (OARec) standard. As part of the OGC API evolution, OGC API - Records is the successor to OGC:CSW (like OGC API - Features is to WFS, etc.).

El estándar OGC API - Registros está actualmente en desarrollo y el plazo actual para una RFC pública por parte de OGC es el primer trimestre de 2022. Por ello, te pedimos que tomes nota del estado del borrador de la especificación para que seas consciente de que la especificación puede cambiar un poco más en los próximos meses. En los próximos meses tendremos que perfeccionar la forma en que se gestionan los enlaces accionables (lo que debería suponer una mejora significativa en comparación con el flujo de trabajo de publicación/encuentro/vinculación de CSW).

La incorporación de esta función a QGIS supone una gran ventaja para facilitar las búsquedas y ayudará tanto a usuarios como a proveedores a largo plazo".

![image38](images/entries/5422b5fd0f6fce0bff486b0268a425f7498b1efc.webp)

This feature was developed by [Tom Kralidis](https://github.com/tomkralidis)
## Widgets y Formularios
### Prestación: Acciones de envío de formularios con HTTP POST
In QGIS 3.24 we added two new HTTP POST actions, similar to the existing `Open` action which uses an HTTP GET request.

Las dos acciones difieren en la forma de codificar los datos del formulario:
1. application/x-www-form-urlencoded
2. multipart/form-data

En ambos casos, los datos se pasan a la acción en una URL codificada.

A new function `url_encode(<map>)` is provided to convert a dictionary (a map) to the encoded format.

The response from the submitted URL is opened by delegating to the operating system `QDesktopServices::openUrl()` after the payload has been stored in a temporary file.

![image39](images/entries/7d4d7ec8aa1eb9c16be7e2e8dad3af8c6fc900a1.webp)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Nuevo botón para abrir la tabla de atributos en los objetos espaciales filtrados
We\'ve added a new button to the attribute form (when in search mode) which enables you to open an attribute table filtered to only show the matching features.

![image40](images/entries/1dfb86fa1bec6a73056c703ae49504cc2b61fb7a.gif)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Herramientas de análisis
### Prestación: Añadir método de redondez al polígono curvo
We added a \"roundness\" method to `QgsCurvePolygon`, allowing the calculation of the \"roundness\" of an area feature based on the formula `Roundness = (4 * pi * Area) / Perimeter^2`.

Esto incluye la adición de una nueva expresión y una herramienta de procesamiento para calcular la redondez. La herramienta de procesamiento crea una nueva capa con la redondez de cada característica en un nuevo campo.

![image41](images/entries/0ebc31c2437a3f5595257edd778d3f2fcbca9486.webp)

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
## Procesado
### Prestación: Algoritmo de extracción de etiquetas
For 3.24 we added a new tool to QGIS\' processing toolbox: \"Extract labels\". As its name hints at, this algorithm extracts label information from a rendered map at a specific extent and scale.

La información extraída de la etiqueta incluye su posición (como geometrías de puntos), el nombre de la capa asociada y el ID de la característica, así como propiedades de apariencia de la etiqueta como rotación, texto, alineación, familia de fuentes, tamaño, peso, etc.

El algoritmo también genera un estilo predeterminado sin símbolos ni etiquetas para la capa de salida, lo que permite arrastrar y soltar esas capas guardadas en proyectos y dibujar la etiqueta exactamente como se exportaron.

If a map theme is specified when extracting labels, the exported labels will match the visibility and symbology of that theme. If left blank, the project\'s current visible layers will be used.

![image42](images/entries/b2149ac307c233bac0cfcb25166a573c8d55d200.webp)

This feature was funded by [TEKSI](https://www.teksi.ch/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Parámetro opcional de extensión de salida para el algoritmo GDAL Raster Calculator
When running against GDAL 3.3 or newer, QGIS processing toolbox\'s GDAL Raster Calculator algorithm now allows you to specify an optional \"output extent\" parameter. This can be quite useful when working with large datasets, often avoiding the need to create an intermediary clipped raster prior to running the calculator algorithm.

![image43](images/entries/7ebbfa145decc6a81678410d53e4d96709d6b2c7.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Parámetro opcional de extensión para el algoritmo GDAL de recorte de trama por máscara
We added an optional extent parameter to the GDAL \"clip raster by mask\" algorithm, which can come in handy when working with large raster datasets.

![image44](images/entries/08731bc9d93110cb048f5ac8c9256c9b7556694d.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Revisión del historial de tratamiento
QGIS 3.24 includes a partial implementation of the framework described in [QEP 130](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/130), and ports the Processing history log over to this framework.

Se trata de un enfoque mucho más flexible para almacenar el historial de procesamiento, ya que nos permite almacenar información adicional ilimitada sobre la herramienta ejecutada (incluidos todos los parámetros de entrada, los resultados de salida y el registro de texto completo). El registro del historial se almacena ahora en una base de datos sqlite en lugar del archivo de texto utilizado anteriormente, lo que permite un almacenamiento/recuperación/filtrado más eficiente.

El nuevo marco no se limita a Processing: también podría utilizarse para almacenar el historial de otras operaciones del usuario, como la edición de proyectos, la exportación de diseños, etc.

We\'ll be using this framework in future to further extend the Processing history dialog. For 3.24, we\'re using it to expose a number of helpful additions to the history dialog:
- Right clicking an entry in the log has a new option to copy the execution parameters as a \"qgis_process\" command line equivalent, giving you a super-easy way to generate qgis_process commands for execution in a CLI.
- Right clicking an entry also shows a new \"Copy as JSON\" option, which copies a JSON string of the input parameters and algorithm settings

![image45](images/entries/d20797cd802b8ecea77a8e1e1d96bf5fcc075f86.webp)

This feature was funded by the [Research Institute for Nature and Forest](https://www.inbo.be/en), Flemish Govt

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Acciones avanzadas en los cuadros de diálogo de procesamiento
We have added new actions on the processing dialog including **copy as qgis_process command**, and **copy/paste as JSON**. Together these actions:
- Permite copiar fácilmente el comando PyQGIS equivalente para ejecutar la herramienta utilizando los parámetros definidos en el diálogo
- Allow for easy generation of qgis_process commands via the QGIS GUI, including any tricky parameter values like GeoPackage outputs with specific layers
- Proporcionar una forma de copiar los ajustes definidos en el cuadro de diálogo en un formato de texto, para que pueda almacenarlos fácilmente y restaurarlos más tarde pegando los valores.
- Provides an easy way for you to copy the settings into the JSON format consumed by qgis_process, so that it is easy to see the expected format even for complex parameters (like TIN interpolation parameters).

![image46](images/entries/d372e3463624cffbf522dd16d72d17570a7c511b.webp)

This feature was funded by the [Research Institute for Nature and Forest](https://www.inbo.be/en), Flemish Govt

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Exportación de un único archivo del algoritmo Atlas a PDF
You can now export an atlas layout to a single (collated) PDF file using the \"Export atlas layout as PDF\" processing algorithm.

![image47](images/entries/ced24ad63c3ff2bf6d47b975a965e6a0b9b28466.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Los modelos de proyecto se muestran en el menú Proyecto
We added a new submenu to the \"Project\" menu, which will list any Processing models stored within the current project. This gives you a quick way to launch these project-specific models, in either a single or batch mode!

![image48](images/entries/46c8c42ecd96ab046c3e8fcf944607621f43b2f8.webp)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Añadir parámetro de destino de nube de puntos y salida a Procesos
Hemos ampliado y mejorado el soporte de nubes de puntos en Procesos, concretamente mediante:
- Fixing the filtering of point cloud layers in `QgsProcessingMapLayerComboBox`-based widget used for parameters
- Añadir un tipo de parámetro de nube de puntos de destino y tipos de salida de nube de puntos con los widgets correspondientes. (Actualmente son útiles para proveedores y plugins de terceros que crean salidas de nubes de puntos).
- Exposing the newly added point cloud output and destination parameters to the `algfactory` wrapper

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Compatibilidad con matrices de campos
In QGIS 3.24, we\'ve made array field types first-class citizen in the Processing toolbox! The following algorithms have all been updated to support array fields:
- Algoritmo Refactorizar;
- Algoritmo Agregado;
- Añadir campo al algoritmo de la tabla de atributos;
- Algoritmo calculador de campo; y
- Algoritmo avanzado (es decir, python) de calculadora de campo

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Opciones de Aplicación y Proyecto
### Feature: qgis_process \--no-python argument
This new, optional command line parameter for the qgis_process command-line tool allows you to skip launching Processing with Python support when it is not required. This can result in a significant improvement in qgis_process startup times!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Suppress \"bad layers\" handler on startup
We\'ve added support for a new command line flag for the `qgis` executable, which allows you to disable the default dialog which shows when opening a project with missing/broken layers:

    [--skipbadlayers]       don't prompt for missing layers
    
Example invocation: `./qgis --skipbadlayers` or `./qgis -B`

El caso de uso para esto es que a veces los usuarios tienen automatización u otros procesos de post-arranque y no quieren tener el proceso de arranque interrumpido si hay capas malas presentes en el proyecto. Después del arranque, QGIS ignorará las capas que falten, pero seguirán marcadas como rotas en la lista de capas.

Esta prestación fue sugerida por Giuseppe Baiamonte durante la Jornada de Puertas Abiertas de QGIS, el 17 de diciembre de 2021.

![image49](images/entries/3b60790eb1b2f970940e9280d3eccee6a6f2b8f9.webp)

This feature was developed by [Tim Sutton](https://github.com/timlinux)
### Feature: Parameter values for qgis_process can be specified as a JSON object via stdin
We now provide a mechanism to support complex input parameters for algorithms when running the qgis_process command line tool.

To indicate that parameters will be specified via stdin then the qgis_process command must follow the format
``` 
qgis_process run algid -
```
(with a trailing `-` in place of the usual arguments list).

The JSON object must contain an \"inputs\" key, which is a map of the input parameter values.
``` 
echo "{"inputs": {\"INPUT\": \"my_shape.shp\", DISTANCE: 5}}" | qgis_process run native:buffer -
```
Además, en este objeto JSON se pueden incluir ajustes adicionales como las unidades de distancia, las unidades de área, el elipsoide y la ruta del proyecto:
``` 
{
    'ellipsoid': 'EPSG:7019',
    'distance_units': 'feet',
    'area_units': 'ha',
    'project_path': 'c:/temp/my_project.qgs'
    'inputs': {'DISTANCE': 5, ..... }
}
```
(Specifying input parameters via stdin implies automatically the \--json output format for results.)

One big motivation behind this enhancement is to provide a way for the qgis_process R libraries to support parameter types such as aggregates!

This feature was funded by the [Research Institute for Nature and Forest](https://www.inbo.be/en), Flemish Govt

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Run Python script algorithms directly via qgis_process
The qgis_process command-line tool now supports running a Python script algorithm directly by specifying the path to the .py file, in place of an algorithm ID or model file path!

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Proveedores de datos
### Prestación: Errores más fáciles a partir de mosaicos ráster XYZ, WMS y vectoriales
Server errors which occur during XYZ, vector tile or WMS network requests are now shown directly in the QGIS window via the message bar. We\'ve made these error messages much more descriptive and helpful, by including the original response error text wherever possible!

![image50](images/entries/006a532d89422cfe5ddb6638ae635384e4f8b8f2.gif)

This feature was funded by [MapTiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Prestación: Conexión inmediata con las teselas de Mapzen Global Terrain
QGIS now sports built-in support for the Terrarium DEM format for WMS/XYZ layers. In addition, we now have out-of-the-box ability to add Mapzen Global Terrain Tiles hosted on AWS. You can find the new MapZen option in the XYZ section of the browser panel. Users now have an immediately accessible global DEM source for their projects!! See also <https://registry.opendata.aws/terrain-tiles/>

![image51](images/entries/68cfde8b146eb42d4e75fd089adb2fbe8e7e5012.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Método de autenticación HMAC SHA256 para MapTiler
We\'ve added a new authentication method specific for MapTiler which allows you to use a token encrypted with HMAC-SHA256.

![image52](images/entries/3f4f8ef8eef605c25bf84e0e86420c6493e02729.webp)

This feature was funded by [MapTiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Prestación: Parámetro de plantilla {usage} para mosaicos XYZ raster y vectoriales
Para las capas ráster basadas en mosaicos XYZ y para las capas de mosaicos vectoriales, ahora permitimos la posibilidad de insertar parámetros de plantilla {usage} (además de {x}, {y}, {z}). Si está presente, este parámetro será sustituido por el contexto en el que se realiza la solicitud.

Los posibles valores de contexto son:
- **vista** - cuando la solicitud procede de un lienzo de mapa 2D o 3D
- **export** - when the request comes from exporting a layer or exporting a print layout for high-quality output (map previews in print layout designer are classed as "view")
- **desconocido** - cuando procede de algún otro contexto, pero se desconoce la fuente.

Esta funcionalidad es útil para los clientes de MapTiler, que necesitan reconocer el contexto en el que se utilizan los mosaicos para facturar a los usuarios en consecuencia.

This feature was funded by [MapTiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Prestación: Conversión de mosaicos ráster WMTS/XYZ en terreno (DEM)
In QGIS 3.24 we\'ve introduced the possibility to convert WMTS/XYZ raster datasets to a raster layer of single band float type following a predefined encoding scheme.

You can activate this option and choose an encoding scheme (for now, \"MapTiler Terrain RGB\" or \"Terrarium Terrain RGB\" are available) in the source settings of the XYZ connection or in the Data Source Manager when adding a WMST layer.

El conversor seleccionado traducirá los valores fuente RGB a valores flotantes para cada píxel. Una vez cargada, la capa se presentará como una capa ráster de punto flotante de banda única, ¡lista para ser estilizada utilizando un renderizador de pseudocolor o de sombra de colina!

![image53](images/entries/6010ce9b5ad8a9d4bc3130b537c74a567be6df23.webp)

This feature was funded by [MapTiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Prestación: Tipos de campo de matriz para capas borrador
Ahora se pueden añadir tipos de campo de matriz directamente a las nuevas capas scratch creadas. (Aunque los tipos de campo de matriz ya eran compatibles con las capas scratch, no había forma de que los usuarios los añadieran al crear una nueva capa scratch).

![image54](images/entries/57bd4059d12ad5ef94acb42989824a746de92582.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Tipos de campo JSON para nuevas capas de GeoPackage
We\'ve added support for creating JSON fields directly to newly created GeoPackage layers. (While JSON field types have previously been supported by GeoPackage layers, there was no way for users to add them when creating a new layer.)

![image55](images/entries/a96a3edb24bb7e7132fdb353b77ea1a1c98ed9ef.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Anulación de tipos de texto delimitados y otras mejoras
We\'ve given some love to the delimited text data provider in 3.24, with several enhancements which include:

**Soporte de tipos booleanos y detección automática.

Los tipos de datos booleanos son ahora ciudadanos de primera clase, que se reconocen automáticamente cuando todos los registros de una columna contienen uno de los siguientes valores (sin distinguir mayúsculas de minúsculas):
- t/f
- true/false
- yes/no
- 0/1

Los campos booleanos también se detectan a partir de un archivo CSVT, un formato GDAL/GeoCSV, por ejemplo.

`Integer(Boolean)`

You can also add custom string representations for TRUE/FALSE (for example a localized \"yes\"/\"no\" value).

**Sustitución del tipo de columna

Los tipos de columna se determinan automáticamente (mediante un escaneo inicial limitado del archivo para obtener información inmediata, seguido de un escaneo completo del archivo que se realiza en un hilo independiente para no bloquear la interfaz gráfica de usuario y que el usuario puede interrumpir), los tipos se exponen a la interfaz gráfica de usuario como cuadros combinados y el usuario puede anular los tipos determinados automáticamente.

**Soporte CSVT mejorado**.

CoordX, CoordY, Point(X/Y), WKT are now recognized as specified in <https://giswiki.hsr.ch/GeoCSV>

![image56](images/entries/998275eaa241752a63c889c4c428948f6702d7ed.webp)

Este prestación ha sido financiada por la ciudad de Friburgo de Brisgovia.

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Nuevo método de autenticación basado en el encabezado HTTP
Existe un nuevo método de autenticación para las solicitudes de red que admite la autenticación de cabecera HTTP definida por el usuario. En estas solicitudes se pueden incluir varias cabeceras personalizadas.

This is useful in various scenarios, such as when a WMS requires an API key that is to be used in a HTTP header with the header key being `X-API-KEY`, which can now be included in requests from QGIS to authenticate against the WMS endpoint.

![image57](images/entries/72f6e13c97be1a5e3e4d3aafdee9eef6d77a5bfe.webp)

This feature was developed by [Tom C](https://github.com/Cumminsc9)
### Prestación: Exponer columnas secundarias de geometría PostGIS como geometrías referenciadas
As discussed in [this issue](https://github.com/qgis/QGIS/pull/45007), we have added support for exposing additional geometry columns from the Postgres provider as QgsReferencedGeometry. This allows more efficient interaction with additional geometry columns through the API. For example, in label placement, the additional geometry column can be used instead of the feature geometry. The fields will be represented as `WKT [CRS User-Friendly Identifier]` in the attribute table.

Puede utilizarse en expresiones y en la pestaña de propiedades de colocación de etiquetas, donde puede vincular la colocación de etiquetas a la segunda columna de geometría utilizando la propiedad Punto. En el caso de que la utilice para etiquetar, la segunda columna de geometría se actualizará automáticamente si utiliza la herramienta mover y el tipo de columna es Geometría. Si el tipo de columna es texto, también puede utilizarla como segunda geometría haciendo, por ejemplo

    geom_from_wkt("my wkt string field")
    
En este caso, sin embargo, la columna será sólo de lectura.

Así, por ejemplo, ahora en las expresiones si usted tiene la columna de geometría secundaria que puede hacer:

    buffer("my_second_geom_column", 10)
    
y funcionará.

{{<rich-box-start icon="⚠️" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-6" >}}
##### Atención
Esto cambia el comportamiento de los proyectos existentes.

{{<rich-content-end >}}

{{<rich-box-end >}}

![image58](images/entries/2f2169f6a9927916d3841b63333982a5417a3a0c.webp)

This feature was funded by [OPENGIS.ch](https://www.opengis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://github.com/m-kuhn)
## Servidor de QGIS
### Prestación: Permitir un mejor control de la cadena de flujo de respuesta desde los filtros del servidor
Los nuevos filtros permiten controlar la cadena de llamadas mediante la implementación de nuevas retrollamadas de filtro que permiten devolver un valor de control para detener la propagación. Esto permite un mejor control del flujo de datos y respuestas.
- Deprecate `bool QgsFilter::onRequestReady()`, `bool QgsFilter::onSendResponse()`, `bool QgsFilter::onResponseComplete()`
- Add new methods `bool QgsFilter::onRequestReady()`, `bool QgsFilter::onSendResponse()`, `bool QgsFilter::onResponseComplete()` which return boolean values for controlling data flow
- Handle flow control in `QgsFilterResponseDecorator::flush()`

This feature was developed by [David Marteau](https://github.com/dmarteau)
## Correcciones Notables
### Errores corregido por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Proyección incorrecta de ráster en pantallas HIDPI | [#46882](https://github.com/qgis/QGIS/issues/46882) | [PR #46931](https://github.com/qgis/QGIS/pull/46931) | PORHACER. |
| Título del Gestor de Fuentes de Datos no traducible | [#46929](https://github.com/qgis/QGIS/issues/46929) | [PR #46932](https://github.com/qgis/QGIS/pull/46932) | PORHACER. |
| QGIS 3.22 - Nombres de mapa idénticos en el compositor de impresión | [#46927](https://github.com/qgis/QGIS/issues/46927) | Trabaja para mí |  |
| Atributos en negrita y cursiva de las etiquetas que se reinicializan | [#46896](https://github.com/qgis/QGIS/issues/46896) | Trabaja para mí |  |
| NameError: name \'QGISAPP\' is not defined when using stop_app() | [#46883](https://github.com/qgis/QGIS/issues/46883) | Works for me on Linux/master, might be windows only |  |
| La capa virtual no se carga correctamente tras reabrir un proyecto | [#46834](https://github.com/qgis/QGIS/issues/46834) | [PR #46938](https://github.com/qgis/QGIS/pull/46938) | PORHACER. |
| QGIS se bloquea al llamar a readLayerXml() | [#46741](https://github.com/qgis/QGIS/issues/46741) | Trabaja para mí |  |
| Cae el sistema al cambiar la orientación de la página en el diseño | [#46575](https://github.com/qgis/QGIS/issues/46575) | [PR #46972](https://github.com/qgis/QGIS/pull/46972) | PORHACER. |
| \"sort\" funcionality of attributes table sort numeric fields as text | [#34935](https://github.com/qgis/QGIS/issues/34935) | [PR #47035](https://github.com/qgis/QGIS/pull/47035) | PORHACER. |
| OAPIF: api-key no incluida al solicitar el endpoint /collections | [#46535](https://github.com/qgis/QGIS/issues/46535) | [PR #47145](https://github.com/qgis/QGIS/pull/47145) | PORHACER. |
| Falta la notación XML en la información sobre herramientas del cuadro de diálogo de creación de archivos vectoriales. | [#46508](https://github.com/qgis/QGIS/issues/46508) | [PR #47148](https://github.com/qgis/QGIS/pull/47148) | PORHACER. |
| La opción Ignorar fuera de rango en el representador de símbolos interpolados crea artefactos si el valor inicial está fuera de rango. | [#46362](https://github.com/qgis/QGIS/issues/46362) | [PR #47174](https://github.com/qgis/QGIS/pull/47174) | PORHACER. |
| start width \> end width is ignored when using the \"exact\" color interpolation method | [#46371](https://github.com/qgis/QGIS/issues/46371) | [PR #47195](https://github.com/qgis/QGIS/pull/47195) | PORHACER. |
| QGIS Layouts: using \"Data defined override\" for HTML Source URL not working | [#34395](https://github.com/qgis/QGIS/issues/34395) | me funciona (cerrado - no es un error) |  |
| (Des)fuerza ocultar forma en relación widget | [#47226](https://github.com/qgis/QGIS/issues/47226) | [PR #47245](https://github.com/qgis/QGIS/pull/47245) | PORHACER. |
| El protocolo de autenticación Oauth2 no honra el número de puerto definido en la URL de redirección en QGIS 3.22.1 | [#46354](https://github.com/qgis/QGIS/issues/46354) | me funciona (dejado abierto) |  |
| HTML/String-ish QByteArray como resultado de la función de expresión rompe la vista previa de la expresión | [#46174](https://github.com/qgis/QGIS/issues/46174) | [PR #47229](https://github.com/qgis/QGIS/pull/47229) | PORHACER. |
| Raster layer exported to GeoPackage with the character \'ß\' in the name is not immediately loaded in the project | [#45965](https://github.com/qgis/QGIS/issues/45965) | me funciona (cerrado) |  |
| La ordenación de tablas de atributos de diseño no funciona en diseños de impresión cuando el nombre de la columna tiene espacios. | [#43744](https://github.com/qgis/QGIS/issues/43744) | [PR #47249](https://github.com/qgis/QGIS/pull/47249) | PORHACER. |
| Leyenda de rango de escala incorrecta tras aplicar simbología graduada logarítmica a una capa vectorial. | [#45454](https://github.com/qgis/QGIS/issues/45454) | [PR #47259](https://github.com/qgis/QGIS/pull/47259) | Riesgoso? |
| arreglar la caída del servidor | no reportado | [PR #47271](https://github.com/qgis/QGIS/pull/47271) | PORHACER. |
| Cargar proyecto QGIS desde línea de comandos a partir de un proyecto PostgreSQL | [#47270](https://github.com/qgis/QGIS/issues/47270) | [PR #47272](https://github.com/qgis/QGIS/pull/47272) | PORHACER. |
| Aggregate function with filter doesn\'t work in layout manager | [#45552](https://github.com/qgis/QGIS/issues/45552) | Funciona para mí (cerrado) |  |
| Value map widget: \"value\"/\"description\" inconsistency when table added to print layouts | [#41798](https://github.com/qgis/QGIS/issues/41798) | [PR #47300](https://github.com/qgis/QGIS/pull/47300) | PORHACER. |
| Faltan entradas en la tabla de atributos en la maquetación con atlas en el salto de página | [#44086](https://github.com/qgis/QGIS/issues/44086) | [PR #47303](https://github.com/qgis/QGIS/pull/47303) | PORHACER. |
| Server OAPIF: bbox filter isn\'t working if data source CRS is not EPSG:4326/WGS84 | [#47302](https://github.com/qgis/QGIS/issues/47302) | [PR #47318](https://github.com/qgis/QGIS/pull/47318) | PORHACER. |
| Drag & Drop designer control visibility by expression with field IS NOT NULL doesn\'t work if the field is configured with html | [#47363](https://github.com/qgis/QGIS/issues/47363) | [PR #47432](https://github.com/qgis/QGIS/pull/47432) | Riesgoso? |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Correcciones de error por Sandro Santilli
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| El algoritmo DistanceWithin falla con el proveedor PostgreSQL | [#45352](https://github.com/qgis/QGIS/issues/45352) | [PR #46971](https://github.com/qgis/QGIS/pull/46971) | [PR #47076](https://github.com/qgis/QGIS/pull/47076) |
| GH_WORKSPACE -\> QGIS_WORKSPACE | [PR #47060](https://github.com/qgis/QGIS/pull/47060) |  |  |
| Mejorar la documentación sobre la ejecución de pruebas | [PR #47057](https://github.com/qgis/QGIS/pull/47057) |  |  |
| Usar variables para configurar la conexión postgresql en authmanager test | [PR #47059](https://github.com/qgis/QGIS/pull/47059) |  |  |
| Re-use possibly cached postgis_version from pgsql description method | [PR #47393](https://github.com/qgis/QGIS/pull/47393) | [PR #47401](https://github.com/qgis/QGIS/pull/47401) |  |
| Confiar en la clave primaria de las capas configuradas por el complemento DBManager TopoViewer | [#47389](https://github.com/qgis/QGIS/issues/47389) | [PR #47390](https://github.com/qgis/QGIS/pull/47390) | [PR #47403](https://github.com/qgis/QGIS/pull/47403) |
| Mejorada la salida de depuración en la clase QgsPostgresConn | [PR #47396](https://github.com/qgis/QGIS/pull/47396) |  |  |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Error corregido por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QGIS 3.21.0: preset transform required \"nehpgn.gsb\" but downloads \"nehpgn.tif\" which does not work | [#45470](https://github.com/qgis/QGIS/issues/45470) | [PR #46918](https://github.com/qgis/QGIS/pull/46918) | [PR #46952](https://github.com/qgis/QGIS/pull/46952) |
| La capa ráster se desalinea cuando bbox es mayor que la capa de trama proyectada. | [#34518](https://github.com/qgis/QGIS/issues/34518) | [PR #46939](https://github.com/qgis/QGIS/pull/46939) | [PR #46956](https://github.com/qgis/QGIS/pull/46956) |
| Filter for WFS layer: The \"Tables\" button is missing | [#46887](https://github.com/qgis/QGIS/issues/46887) | No es un error |  |
| Algo más sencillo que SQL para filtrar una capa WFS | [#46888](https://github.com/qgis/QGIS/issues/46888) | [PR #47056](https://github.com/qgis/QGIS/pull/47056) | [PR #47132](https://github.com/qgis/QGIS/pull/47132) |
| renombrar/borrar columnas lleva mucho tiempo en vectores grandes | [#47012](https://github.com/qgis/QGIS/issues/47012) | [GDAL PR 5193](https://github.com/OSGeo/gdal/pull/5193) | [GDAL PR 5204](https://github.com/OSGeo/gdal/pull/5204) |
| Al abrir un Geopackage Vectorial en QGIS se altera su archivo aunque el usuario no realice ningún cambio | [#23991](https://github.com/qgis/QGIS/issues/23991) | [PR #47098](https://github.com/qgis/QGIS/pull/47098) | [PR #47301](https://github.com/qgis/QGIS/pull/47301) |
| El SRC MapInfo no se reconoce correctamente | [GDAL issue #5217](https://github.com/OSGeo/gdal/issues/5217) | [PR #47149](https://github.com/qgis/QGIS/pull/47149) | [PR #47157](https://github.com/qgis/QGIS/pull/47157) |
| Crash exporting dxf using \"Symbol layer symbology\" | [#46245](https://github.com/qgis/QGIS/issues/46245) | [PR #47277](https://github.com/qgis/QGIS/pull/47277) | [PR #47297](https://github.com/qgis/QGIS/pull/47297) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Error corregido por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Al intentar añadir GPKG desde el gestor de fuentes de datos se bloquea QGIS master | [#46463](https://github.com/qgis/QGIS/issues/46463) | [PR #46928](https://github.com/qgis/QGIS/pull/46928) | irrelevante |
| El nombre para mostrar en las propiedades de capa no se rellena automáticamente | [#28353](https://github.com/qgis/QGIS/issues/28353) | [PR #47016](https://github.com/qgis/QGIS/pull/47016) |  |
| Correcciones a QgsGeometry::addPart + nuevos casos de prueba | no reportado | [PR #47009](https://github.com/qgis/QGIS/pull/47009) |  |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Denis Rouzaud](http://www.opengis.ch/)
### Corrección de errores por Alex Bruy
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Imagen de diseño: los parámetros svg definidos por datos deben desactivarse para las imágenes incompatibles. | [#26524](https://github.com/qgis/QGIS/issues/26524) | [PR #46976](https://github.com/qgis/QGIS/pull/46976) |  |
| TypeError en MetaSearch al añadir datos WFS | [#46135](https://github.com/qgis/QGIS/issues/46135) | [PR #46993](https://github.com/qgis/QGIS/pull/46993) | [PR #47003](https://github.com/qgis/QGIS/pull/47003) |
| El algoritmo Dividir Capa Vectorial no exporta valores nulos y vacíos. | [#38105](https://github.com/qgis/QGIS/issues/38105) | [PR #46997](https://github.com/qgis/QGIS/pull/46997) | [PR #47030](https://github.com/qgis/QGIS/pull/47030) |
| el gestor de fuentes de datos no se abre con el submenú correcto para las fuentes de datos de nubes de puntos | [#42881](https://github.com/qgis/QGIS/issues/42881) | [PR #46998](https://github.com/qgis/QGIS/pull/46998) | [PR #47002](https://github.com/qgis/QGIS/pull/47002) |
| SLD import doesn\'t recognize html enconding in ttf font references | [#27263](https://github.com/qgis/QGIS/issues/27263) | [PR #46975](https://github.com/qgis/QGIS/pull/46975) | [PR #47040](https://github.com/qgis/QGIS/pull/47040) |
| Error al abrir el diálogo del cargador de datos desde MetaSearch | [#40490](https://github.com/qgis/QGIS/issues/40490) | Trabaja para mí |  |
| El nombre para mostrar en las propiedades de capa no se rellena automáticamente | [#28353](https://github.com/qgis/QGIS/issues/28353) | [PR #46978](https://github.com/qgis/QGIS/pull/46978) |  |
| No hay manera de añadir mbtiles basado en archivos MVT paquete excepto arrastrar y soltar | [#36449](https://github.com/qgis/QGIS/issues/36449) | [PR #47028](https://github.com/qgis/QGIS/pull/47028) | [PR #47068](https://github.com/qgis/QGIS/pull/47068) |
| \"GDAL rasterize overwrite with attribute\" does not refresh/reload output | [#45729](https://github.com/qgis/QGIS/issues/45729) | [PR #47055](https://github.com/qgis/QGIS/pull/47055) | [PR #47105](https://github.com/qgis/QGIS/pull/47105) |
| Borrar columna en parámetro de matriz en el modelador gráfico no funciona | [#45694](https://github.com/qgis/QGIS/issues/45694) | [PR #47064](https://github.com/qgis/QGIS/pull/47064) | [PR #47067](https://github.com/qgis/QGIS/pull/47067) |
| Firma incorrecta del QgsProcessingParameterMeshDatasetGroups al exportar a Python | no reportado | [PR #47152](https://github.com/qgis/QGIS/pull/47152) | [PR #47156](https://github.com/qgis/QGIS/pull/47156) |
| El mensaje de error cuando no se pueden ejecutar las herramientas de GRASS es (ahora) erróneo | [#46052](https://github.com/qgis/QGIS/issues/46052) | [PR #47163](https://github.com/qgis/QGIS/pull/47163) |  |
| \"Ignore invalid input features\" processing setting location is misleading | [#42557](https://github.com/qgis/QGIS/issues/42557) | [PR #47163](https://github.com/qgis/QGIS/pull/47163) |  |
| Número incoherente de decimales en la herramienta Identificar | [#27929](https://github.com/qgis/QGIS/issues/27929) | [PR #47173](https://github.com/qgis/QGIS/pull/47173) |  |
| qgis_process is not showing algorithm providers installed via a python plugin | [#41120](https://github.com/qgis/QGIS/issues/41120) | [PR #47258](https://github.com/qgis/QGIS/pull/47258) | [PR #47263](https://github.com/qgis/QGIS/pull/47263) |
| No se pueden eliminar archivos .shp y .dbf con código python (removeMapLayers, deleteShapeFile) | [#39428](https://github.com/qgis/QGIS/issues/39428) | Trabaja para mí |  |
| Opción de extensión QgsProcessingParameterFile | [#45633](https://github.com/qgis/QGIS/issues/45633) | No es un error |  |
| Make the labels \"edit rule\" widget a real dialog with buttons | [#36761](https://github.com/qgis/QGIS/issues/36761) | [PR #47305](https://github.com/qgis/QGIS/pull/47305) |  |
| Editar formulario python editor tabs/spaces confusion | [#46988](https://github.com/qgis/QGIS/issues/46988) | [PR #47345](https://github.com/qgis/QGIS/pull/47345) | [PR #47352](https://github.com/qgis/QGIS/pull/47352) |
| Error when making buffer from empty layer with \'Dissolve result\' option checked | [#46396](https://github.com/qgis/QGIS/issues/46396) | [PR #47348](https://github.com/qgis/QGIS/pull/47348) | [PR #47384](https://github.com/qgis/QGIS/pull/47384) |
| QGIS no sustituye las comas en los nombres de capa al exportar a DXF (por lo que es incompatible con AutoCAD) | [#47381](https://github.com/qgis/QGIS/issues/47381) | [PR #47418](https://github.com/qgis/QGIS/pull/47418) | [PR #47430](https://github.com/qgis/QGIS/pull/47430) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Errores corregidos por Alex Bruy
### Error corregido por Paul Blottiere
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fixes WFS EXP_FILTER parsing in GetFeature request | [mailing list](https://www.mail-archive.com/qgis-user@lists.osgeo.org/msg50029.html) | [PR #47029](https://github.com/qgis/QGIS/pull/47029) | Demasiado arriesgado |
| Corrección del nombre de archivo de salida cuando se guarda un ráster en un formato sin extensión. | no reportado | [PR #46992](https://github.com/qgis/QGIS/pull/46992) | PORHACER. |
| Documento WFS GetFeature y excepciones | no reportado | [PR #47198](https://github.com/qgis/QGIS/pull/47198) | PORHACER. |
| Exluding a print layout in project propteries -\> server do not avoid that a GetPrint request can be done for that layout | [#46140](https://github.com/qgis/QGIS/issues/46140) | [PR #47199](https://github.com/qgis/QGIS/pull/47199) | PORHACER. |
| Server: Can\'t enable WFS3 API update endpoint (PUT/PATCH) on layers without geometry | [#46119](https://github.com/qgis/QGIS/issues/46119) | Trabaja para mí |  |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Pau Blottiere](https://hytech-imaging.fr/)
### Corrección de errores por Matthias Kuhn
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir HTTP Post con MultiPart | [#46989](https://github.com/qgis/QGIS/issues/46989) | [PR #47006](https://github.com/qgis/QGIS/pull/47006) | no es necesario |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Matthias Kuhn](https://www.opengis.ch/)
### Error fijado por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Añadir extensión .tsv al filtro de archivos de texto delimitado compatibles | reportado en youtube screencast | [PR #47181](https://github.com/qgis/QGIS/pull/47181) | pendiente |
| Corregir la colocación de los anclajes de línea se invierte para las etiquetas que se sitúan debajo de las líneas | no reportado | [PR #47181](https://github.com/qgis/QGIS/pull/47181) | [PR #47181](https://github.com/qgis/QGIS/pull/47181) |
| Corregir código de retorno incorrecto de QgsProcessingModelAlgorithm::fromFile cuando el archivo no existe | no reportado | [PR #47161](https://github.com/qgis/QGIS/pull/47161) | [PR #47162](https://github.com/qgis/QGIS/pull/47162) |
| Corregir muchas regresiones del georreferenciador | multiple | no reportado | pendiente |
| Avoid some unwanted \"unhandled exception\" message boxes which can pop up while moving the mouse | reportado en youtube screencast | [PR #47138](https://github.com/qgis/QGIS/pull/47138) | [PR #47154](https://github.com/qgis/QGIS/pull/47154) |
| Don\'t use custom palette in crash handler dialog, this results in unreadable text on dark themes | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47110](https://github.com/qgis/QGIS/pull/47110) | [PR #47136](https://github.com/qgis/QGIS/pull/47136) |
| Don\'t slightly colorise the icons for selected items in lists | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47133](https://github.com/qgis/QGIS/pull/47133) | no apto |
| Corregir excepción python planteada después de ejecutar algoritmo in-place que no requiere parámetros | reportado en youtube screencast | [PR #47108](https://github.com/qgis/QGIS/pull/47108) | [PR #47130](https://github.com/qgis/QGIS/pull/47130) |
| Corrección del etiquetado de los elementos fuera del intervalo de fechas del controlador temporal | [#45160](https://github.com/qgis/QGIS/issues/45160) | [PR #47119](https://github.com/qgis/QGIS/pull/47119) | [PR #47126](https://github.com/qgis/QGIS/pull/47126) |
| Corrección de la orientación de las etiquetas curvas en función de la línea. | [#45051](https://github.com/qgis/QGIS/issues/45051) | [PR #47118](https://github.com/qgis/QGIS/pull/47118) | [PR #47137](https://github.com/qgis/QGIS/pull/47137) |
| Cuando el procesamiento se inicializa en scripts externos, asegúrese de que los proveedores GRASS, SAGA y OTB se incluyen por defecto | [#45935](https://github.com/qgis/QGIS/issues/45935) | [PR #47114](https://github.com/qgis/QGIS/pull/47114) | [PR #47121](https://github.com/qgis/QGIS/pull/47121) |
| Mostrar error descriptivo cuando no se puede utilizar la herramienta de rotación de etiquetas debido a expresiones no válidas. | [#47091](https://github.com/qgis/QGIS/issues/47091) | [PR #47112](https://github.com/qgis/QGIS/pull/47112) | no apto |
| QgsRasterDataProvider.block() devuelve un QgsRasterBlock inválido si el tamaño del bloque solicitado excede un cierto umbral. | [#47097](https://github.com/qgis/QGIS/issues/47097) | [PR #47106](https://github.com/qgis/QGIS/pull/47106) | [PR #47129](https://github.com/qgis/QGIS/pull/47129) |
| Corrección de la falta de iconos para los tipos de campo de matriz | [#47078](https://github.com/qgis/QGIS/issues/47078) | [PR #47086](https://github.com/qgis/QGIS/pull/47086) | no apto |
| Utilizar el enfoque correcto para desestablecer el campo definido por los datos para la posición de la etiqueta cuando se elimina la columna auxiliar. | [#46403](https://github.com/qgis/QGIS/issues/46403) | [PR #47085](https://github.com/qgis/QGIS/pull/47085) | [PR #47088](https://github.com/qgis/QGIS/pull/47088) |
| Corrección de la ordenación de atlas con nombres de campo complejos | [#40332](https://github.com/qgis/QGIS/issues/40332) | [PR #47083](https://github.com/qgis/QGIS/pull/47083) | [PR #47103](https://github.com/qgis/QGIS/pull/47103) |
| mejorar la gestión de los campos al pasar a un sistema basado en reglas | [#46459](https://github.com/qgis/QGIS/issues/46459) | [PR #47081](https://github.com/qgis/QGIS/pull/47081) | [PR #47104](https://github.com/qgis/QGIS/pull/47104) |
| Fix \'Save all Styles/Save current Style\' only appears after close/reopen the layer properties window | [#46596](https://github.com/qgis/QGIS/issues/46596) | [PR #47080](https://github.com/qgis/QGIS/pull/47080) | no apto |
| Corrección de la legibilidad del texto al utilizar temas oscuros | [#47065](https://github.com/qgis/QGIS/issues/47065) | [PR #47071](https://github.com/qgis/QGIS/pull/47071) | [PR #47074](https://github.com/qgis/QGIS/pull/47074) |
| Corrección de errores sqlite en el arranque causados por la lógica de importación de bases de datos de estilo predeterminado. | no reportado | [PR #47070](https://github.com/qgis/QGIS/pull/47070) | no apto |
| Los widgets de color cambian de color incorrectamente cuando se pasa el ratón por encima del widget. | no reportado | [PR #47069](https://github.com/qgis/QGIS/pull/47069) | [PR #47077](https://github.com/qgis/QGIS/pull/47077) |
| Evitar errores de definición de src al cerrar el diálogo de opciones | [#47014](https://github.com/qgis/QGIS/issues/47014) | [PR #47061](https://github.com/qgis/QGIS/pull/47061) | n/d |
| Arreglar la advertencia de acceso directo duplicado registrado al inicio | no reportado | [PR #46983](https://github.com/qgis/QGIS/pull/46983) | no apto |
| Fix scroll wheel events get \"stuck\" when scrolling to bottom of areas | no reportado | [PR #46958](https://github.com/qgis/QGIS/pull/46958) | [PR #46987](https://github.com/qgis/QGIS/pull/46987) |
| Señalar muchas situaciones en las que las transformaciones aproximadas son apropiadas para que no se muestren advertencias. | [#45621](https://github.com/qgis/QGIS/issues/45621) | [PR #46957](https://github.com/qgis/QGIS/pull/46957) | [PR #46961](https://github.com/qgis/QGIS/pull/46961) |
| Corregir de fallos al guardar estilos de capa | [#46954](https://github.com/qgis/QGIS/issues/46954) | [PR #46955](https://github.com/qgis/QGIS/pull/46955) | no apto |
| Arreglar las funciones de fusión dañadas | no reportado | [PR #46924](https://github.com/qgis/QGIS/pull/46924) | n/d |
| \[mssql\] Fix provider on case-sensitive database locales | [#46907](https://github.com/qgis/QGIS/issues/46907) | [PR #46923](https://github.com/qgis/QGIS/pull/46923) | [PR #46949](https://github.com/qgis/QGIS/pull/46949) |
| \[mssql\] Fix inserting features when pk attribute name contains special chars | [#42290](https://github.com/qgis/QGIS/issues/42290) | [PR #46876](https://github.com/qgis/QGIS/pull/46876) | [PR #46903](https://github.com/qgis/QGIS/pull/46903) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)
### Corrección de errores por Damiano Lombardi
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corrección #47089 punto de rotación incorrecta para rotar la vista previa de la herramienta de etiqueta | [#47089](https://github.com/qgis/QGIS/issues/47089) | [PR #47124](https://github.com/qgis/QGIS/pull/47124) |  |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Damiano Lombardi](https://www.opengis.ch/)

{{<content-end >}}
