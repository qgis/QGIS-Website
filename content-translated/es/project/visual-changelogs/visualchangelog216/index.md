---
HasBanner: false
draft: false
releaseDate: '2016-07-08'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.16
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.16{#changelog216 }
![image1](images/projects/b4bbe21d5002a4b73ba27f5abf4e4aaea61d161f.png)

Fecha de lanzamiento: 2016-07-08

This is the log for the next release of QGIS - version 2.16.0 \'Nødebo\'. The Department of Geoscience and Natural Resource Management Forest and Landscape College in Nødebo were hosts to the First International QGIS conference and developer meeting in May 2015.

**Esto no es un Lanzamiento de Largo Plazo**

Esta edición no está diseñada como un Lanzamiento de Largo Plazo (LTR). Los usuarios que deseen tener una versión de QGIS que no cambie y reciba corrección de errores durante al menos un año están invitados a utilizar el actual LTR 2.14 (que ahora se ha convertido en nuestro LTR oficial con el lanzamiento de QGIS 2.16).

**New Features in QGIS 2.16 \'Nødebo\'**

If you are upgrading from QGIS 2.14 you will find a great many new features in this release. We encourage you to peruse the changelogs for [previous releases](https://www.qgis.org/en/site/forusers/visualchangelogs.html) as this QGIS 2.16 release includes all features published in those releases too.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

[![Introducing Nødebo](images/pronouncingnodebo.png)](http://www.youtube.com/watch?v=GKg2SHmBExs)

Pronouncing Nødebo\...

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sponsors. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

QGIS is Free software and you are under no obligation to pay anything to use it -in fact we want to encourage people far and wide to use it regardless of what your financial or social status is - we believe empowering people with spatial decision making tools will result in a better society for all of humanity. If you are able to support QGIS, you can [![donate here](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://qgis.org/en/site/getinvolved/donations.html).

{{<table-of-contents >}}
## Patrocinadores de QGIS versión 2.16.0
Anualmente, también recibimos apoyo de varias organizaciones que aprecian el trabajo que hacemos y nos gustaría facilitar el esfuerzo de desarrollo sostenido que implica el proyecto. Estos patrocinadores se enumeran a continuación con nuestro agradecimiento.

{{<fund type="changelog" >}}
## General
### Prestación: Copiar elementos en formato GeoJSON
The previous setting for include WKT when copying features has been replaced with a choice of copying features as \"Plain text, attributes only\", \"Plain text, WKT geometry\" and a new \"GeoJSON\" option. When set to \"GeoJSON\", copying features in QGIS will place a GeoJSON text representation of the features on the clipboard for easy pasting into other applications/JavaScript code. These settings can be found in the `Settings -> Options -> Data Sources -> Copy features as`.

![image95](images/entries/826068a22b7e7d472720f2404e293fc81de32850.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Característica: Almacenar marcadores espaciales en archivos de proyecto
Si está creando un marcador espacial, ahora puede elegir almacenar el marcador en su archivo de proyecto activo. Desplácese por el panel de marcadores para encontrar la casilla de verificación que habilita esta capacidad.

![image96](images/entries/fe01b36ab39b8cc21e6ec875c4baadc890cf6519.png.400x300_q85_crop.webp)

This feature was developed by [Stéphane Brunner](http://www.camptocamp.com/)
### Prestación: Soporte de mensajes GNSS GNRMC
QGIS can now handle GLONASS satellite data (\$GN\* lines) to get a more precise Position from external GPS/GNSS Receivers.

![image97](images/entries/9d13c0c632da1e70199f035ce5a186c018da2cef.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Ondřej Fibich
### Prestación: Pegar elementos GeoJSON directamente en QGIS
El manipulador del portapapeles QGIS ahora puede analizar muchos formatos de texto adicionales, incluido el soporte nativo para las colecciones de características GeoJSON. Esto le permite copiar y pegar directamente cadenas de GeoJSON en QGIS y convertirlas automáticamente en entidades y geometrías de QGIS.

![image98](images/entries/b649df59dc031b26896e9bba2e20c8380081b741.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Mejoras en consejos de mapa
- Visibilidad de maptip (consejosmapa) se preserva entre sesiones
- Maptips ahora puede mostrar contenido HTML, incluyendo imágenes, videos y enlaces URL

![image99](images/entries/96467c2c86ede6392190f021d266ee0e7ed6cbb5.png.400x300_q85_crop.webp)

This feature was funded by [OPENGIS.ch GmbH](http://www.opengis.ch)

This feature was developed by [Marco Bernasocchi (OpenGIS.ch)](http://www.opengis.ch)
### Prestación: Íconos MIME Escritorio para tipos de archivo QGIS
It\'s now easier to recognise and differentiate QGIS\'s file types on your operating system files manager. There are now desktop MIME Icons for the following file types:
- \*.qgs - archivo Proyecto QGIS
- \*.qml - Archivo de configuración de capa
- \*.qlr - Archivo de definición de capa
- \*.qpt - Archivo plantilla del diseñador

![image100](images/entries/9161a4c36a0149b32cd18119954ac32ce42788a6.PNG.400x300_q85_crop.webp)

This feature was developed by [Alexandre Neto](https://gisunchained.wordpress.com/)
## Interfaz de usuario
### Prestación: Magnificador de la vista de mapa
Se ha añadido una herramienta de aumento a QGIS que le permite ampliar el mapa a una escala determinada. Esto le permite acercar el mapa sin alterar su escala, facilitando la modificación de las posiciones de las etiquetas y los símbolos. Además, en la configuración se puede definir un valor de aumento predeterminado, ¡lo que es muy útil para pantallas de alta resolución!.

![image41](images/entries/4991ffccebf8da94cd01acc1139f52d389731549.gif)

This feature was funded by [the QWAT project](https://github.com/qwat)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Prestación: Mejoras al acercamiento de mapa
QGIS 2.16 trae mejoras a la manera como puede acercar o alejar el lienzo del mapa.
- Holding down `Ctrl` while using the mouse wheel to zoom in or out now results in a finer zoom. This behavior brings canvas into line with composer.
- Pressing `Ctrl++` or `Ctrl+-` performs an immediate zoom in/out on the map canvas
- When certain map tools are active, you can perform a web-map style zoom by holding down `Shift` and dragging a rectangle on the map to zoom to that area. This is enabled for the map tools which are not selection tools (since they use shift for adding to selection), and edit tools.

![image42](images/entries/5817785cf3d18db78669c2eb2c2be0cf606c3783.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Rediseñado el Editor de Gradiente Interactivo 
El editor de rampa de gradiente ha sido reelaborado con controles interactivos para una manipulación más fácil de los gradientes. El cuadro de diálogo ahora también incluye un gráfico interactivo para modificar las paradas de gradiente a través de los valores HSV o RGB de color. El nuevo editor presenta:
- arrastre para mover las paradas de color
- doble click para agregar una nueva parada
- presionando borrar eliminará la parada seleccionada
- Al presionar las teclas de flecha se moverá la parada seleccionada, y mantener presionada la tecla Mayús mientras se presiona una tecla del cursor da como resultado un movimiento mayor
- arrastre y suelte un color en el widget para agregar una nueva parada

![image43](images/entries/dca557436392cf51e05a0c77fa915b5e94013d2c.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Elección de vista predeterminada para el diálogo de atributo
En versiones anteriores de QGIS, el cuadro de diálogo de atributos siempre se abría en la vista de tabla. Ahora, tiene la opción de establecer siempre el cuadro de diálogo predeterminado en la vista de tabla, vista de formulario o recordar la última vista utilizada.

![image44](images/entries/53f72a9cf1bf32d73eb5174c37e54c60002b9707.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Característica: Mejoras en calendarios emergentes
Today\'s date is now highlighted in calendar popup widgets, making it easier to select a date relative to the current day.

![image45](images/entries/83b0414698c309c7afacb9da1b01370cff94497d.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Mejora en seleccionadores de color
Los menús desplegables del botón de color ahora muestran una rueda de color, lo que permite ajustes de color muy rápidos.

![image46](images/entries/1f485fa58f218aa481acf0c118907a1cd60fd682.gif)

This feature was developed by [Nathan Woodrow](http://nathanw.net)
### Prestación: Copiar el contenido de celda desde la tabla de atributo
A new context menu item called `Copy cell content` is now available in the menu opened by a right click on a cell within the attribute table. When this button is clicked, the content of the cell is copied in the clipboard, whatever the kind of widget.

![image47](images/entries/968170742ce1d075c6ab1c462e682ea4fd8c5225.png.400x300_q85_crop.webp)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Prestación: Soporte HiDPI mejorado
Los usuarios de la pantalla HiDPI percibirán una interfaz de usuario mejorada a medida que se haya realizado más trabajo para actualizar los iconos para confiar en las imágenes SVG. A partir de QGIS 2.16, todas las barras de herramientas ahora son compatibles con HiDPI.

![image48](images/entries/e60e55de87e8d2558134f9c9552ef41295642217.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Comportamiento mejorado de herramienta de selección de mapa
El comportamiento de las herramientas de selección basadas en mapas se ha refinado, con los siguientes cambios:

Para selecciones de tipo clic-y-arrastrar:
- holding `Shift` = add to selection
- holding `Ctrl` = subtract from selection
- holding `Ctrl+Shift` = intersect with current selection
- holding `Alt` (can be used with `Shift`/`Ctrl` too) = change from \"intersects\" to \"fully contains\" selection mode

Para selecciones de tipo un-solo-clic:
- holding `Shift` or `Ctrl` = toggle whether feature is selected (i.e. either add to current selection or remove from current selection)

Este cambio alinea el comportamiento del lienzo con otras aplicaciones de diseño y también con el comportamiento del compositor.

![image49](images/entries/4688ab87c97f9c773a62e3c1d5ceaa615cab8b0e.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Actualizaciones de Documentación
### Prestación: Documentación QGIS 2.14
Teniendo ahora una forma automática de crear un reporte en el repositorio de documentación para cada nueva característica en QGIS, estamos seguros de que todas las nuevas características están ahora en la documentación.

El equipo de documentación trabajó arduamente en tres versiones de QGIS: 2.10, 2.12 y 2.14, por lo que la documentación está actualizada para la versión actual de QGIS. Hay alrededor de 180 nuevas características que se han documentado en 4 meses.

Si cree que faltan algunas características en la documentación, siéntase libre de agregar un nuevo reporte, escribir un texto pequeño para describirlo o mejor hacer una contribución.

The documentation team has also worked on improving the documentation guidelines in order to ease contribution\'s process for new doc writers and help translators.

El equipo de documentación ahora trabajará duro los siguientes meses para documentar el lanzamiento actual estable (2.16) de QGIS.

![image51](images/entries/3d6aea22a76278945fcbaebcb6e959c6f4f8790e.png.400x300_q85_crop.webp)

Revise los hitos 2.10, 2.12 y 2.14 para ver todo el trabajo de documentación que ha tenido lugar:
- <https://github.com/qgis/QGIS-Documentation/milestone/5>
- <https://github.com/qgis/QGIS-Documentation/milestone/4>
- <https://github.com/qgis/QGIS-Documentation/milestone/3>

### Feature: Authentication system\'s documentation in users manual
The authentication system features introduced in earlier versions of QGIS (2.12 and 2.14) are now fully documented in the Users manual, and will be a great contribute to the system\'s understanding and adoption.

![image50](images/entries/2408c7661583ab3114123624225f8f8422c634a3.png.400x300_q85_crop.webp)

This feature was funded by [Boundless](http://boundlessgeo.com/)

Esta prestación fue desarrollada por Larry Shaffer
## Simbología
### Característica: Capa del símbolos de flecha
The \"arrow\" symbol layer is a symbol layer allowing to draw straight or curved arrows from a line layer.

En el modo curvo, los nodos de la capa de línea a la que se aplica esta capa de símbolo se usan como puntos de control para arcos circulares. Las flechas se pueden rellenar con cualquier estilo de relleno existente que QGIS admita. Las opciones también permiten seleccionar el tipo de flecha (con una o dos cabezas, planas o divididas en dos), su ancho (que puede ser variable) y el tamaño de las cabezas.

![image52](images/entries/000cc7827fe96aa72aedb646e6497cc69a050396.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/) and Andreas Neumann

This feature was developed by [Hugo Mercier](http://oslandia.com/)
### Feature: New \"Filled marker\" symbol layer type
A \"filled marker\" is similar to the simple marker symbol layer, except that it uses a fill sub symbol to render the marker. This allows use of all the existing QGIS fill (and outline) styles for rendering markers, eg gradient or shapeburst fills.

![image53](images/entries/6107e2a6192e6d459fce2f0a1d9da99680dc53b0.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Nuevos símbolos de accesibilidad y poca visión
Additional accessibility and low visions symbols are now available in QGIS\' SVG symbols collection.

![image54](images/entries/7f6fc338b6f85fb59cd6e5e79b27899724e1c33e.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Nuevos marcadores simples de símbolos 
- semicírculo, tercer, cuarto de círculo
- marcadores medio triángulo
- marcadores cruz y hexágono rellenos
- marcador elipse diamante

![image55](images/entries/e5f7ea942c155a0a8dff05c60aca0f299907ee02.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Feature: \"No symbol\" renderer
Using the new \"No symbol\" renderer in QGIS 2.16 no symbol will be drawn for features, but labeling, diagrams and other non-symbol parts will still be shown.

Todavía se pueden hacer selecciones en el lienzo de la capa y las entidades seleccionadas se representarán con un símbolo predeterminado. Las entidades que se están editando también se mostrarán.

This is intended as a handy shortcut for layers which you only want to show labels or diagrams for, and avoids the need to render symbols with totally transparent fill/border to achieve this. It may not sound useful from the title - but it\'s quite a handy shortcut!

![image56](images/entries/4e02691b64446f5a36f4faf3cc4906726cf57aad.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Mayor control sobre la representación del relleno del punto centroide
Se ha agregado una opción para controlar si el marcador se dibuja en todas las partes o en una sola parte de las entidades múltiples.

![image57](images/entries/1a5e1daeefff5beb028c3230fffd86624974acea.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Definición de contorno para símbolos de marcadores de fuente
El símbolo de marcadores de fuente ahora puede tener un contorno, lo que puede ayudar a aumentar la visibilidad de dichos símbolos al agregar un color de búfer de contorno. Los caracteres de fuente habilitados para Emoji pueden servir como buenos marcadores cuando se usan con un contorno grueso.

![image58](images/entries/be266e3dace9cc7011bfea6bab34ee8e4ade414e.jpeg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Controlar estilo de unión de contorno para marcadores simples, elipse, y fuentes.
Los usuarios ahora pueden cambiar el estilo de combinación de contornos para marcadores simples, elipse y fuentes para ajustar su simbología.

![image59](images/entries/c6b3a2f051a8c4e3f82c5cb6a995ae150acccb4b.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Nueva herramienta de mapa para establecer interactivamente el desplazamiento del símbolo puntual
Allows for setting a point\'s offset if it is bound to a field using data defined overrides. The offset field should be a text field. The map tool to interactively set the offset is in the `Advanced digitizing` toolbar in the icon group with the `Rotate Point Symbols` tool. See the attached animation for an example. Note that when making subsequent adjustments to the offset, you should drag from the original point vertex marker, not the current position of the symbol as rendered on the map.

![image60](images/entries/56a9953a6923d6b9b481b099a5a9dfec0146ba90.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Acople de Estilo
The style dock is a new, far more efficient, way to manage layer styles in QGIS. It supports a live preview of style changes as they are made, full undo / redo support and a less distracted workflow as you prepare your map cartography. For a comprehensive overview of the style dock\'s features, please see [style dock part 1](https://nathanw.net/2016/06/25/improving-you-styling-with-the-qgis-style-dock-part-1/) and [style dock part 2](https://nathanw.net/2016/06/29/qgis-style-dock-part-2-plugin-panels/).

![image61](images/entries/92389e4750d63c3842286fa43fe5ef2214f7c6dd.gif)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Etiquetando
### Prestación: Las herramientas de etiquetado de mapa ahora trabajan con etiquetado basado en reglas
En versiones anteriores de QGIS cuando el etiquetado basado en reglas estaba en su lugar, no podía usar las herramientas de mapa de etiquetado para ubicar y rotar interactivamente las posiciones de las etiquetas. Esto ahora es compatible.

![image62](images/entries/fffc27648a04732d7d051734705ccef544b24fba.gif)

Esta prestación fue desarrollada por Martin Dobias
## Diagramas
### Prestación: Ingresos de leyenda para tamaño de diagrama
A new \"legend\" tab has been added to diagram properties, allowing both the existing attribute legend and a new size legend to be enabled/disabled. The size legend has a configurable marker symbol.

![image63](images/entries/eb51ab12f096acf0422786510fc15324060fe9e1.png.400x300_q85_crop.webp)

This feature was funded by [ADUGA](http://www.aduga.org/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Selección de unidades para ancho de contorno
La selección de unidades para ancho de contorno ya está disponible. Esto permite para un tamaño de la unidad de mapa un diagrama que crecerá y se reducirá en función de la escala del mapa mientras se mantiene un ancho de contorno milimétrico fijo.

![image64](images/entries/932c792c43a94b8236ea803ae334c1a3d9f447ef.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Comportamiento de los Diagramas como etiquetas y que pueden ser manejados desde la barra de herramientas
Originalmente, había una barra de herramientas para etiquetas que permitía:
- establecer opciones de etiquetado para etiquetas de la capa actual
- resaltar las etiquetas ancladas. El resaltado es verde en la capa editable, de lo contrario, azul.
- fijar o no fijar etiquetas
- mover, mostrar y ocultar etiquetas

Con esta nueva prestación, hay una nueva herramienta disponible en la barra de herramientas de etiquetas que permite establecer las propiedades de los diagramas para la capa actual. Además, cada herramienta mencionada anteriormente ahora también es totalmente utilizable con diagramas.

![image65](images/entries/eb337b7d02cd7ecb923134de80a63aa62c3e8bb8.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
## Representación
### Prestación: Nuevas opciones para simplificación al vuelo
El usuario puede seleccionar el algoritmo a usar cuando se ejecuta la simplificación del lado local para dibujar geometrías más rápido. Ahora, QGIS proporciona tres algoritmos:
- Distancia (algoritmo predeterminado, y la única opción disponible en lanzamientos previos QGIS)
- SnapToGrid
- Visvalingam

This change also moves the local \"on-the-fly\" simplification from the provider and iterator classes to the rendering code. This avoids cases where simplification changes the geometry fetched from vector data providers, possibly affecting rule based and other expression based symbology. This is important when you have expressions that use the feature geometry (e.g. calculation of area) - we want to be sure that these calculations are done on the original geometry, not on the simplified ones.

![image66](images/entries/9460e7d5f10a8c89697cef1f80674ca30d1c3aef.jpg.400x300_q85_crop.webp)

This feature was developed by [Alvaro Huarte](https://es.linkedin.com/in/alvarohuarte)
### Prestación: Clasificación basada en cuantiles para capas ráster
This option can be found for single band pseudocolor rasters in the classification `mode` dialog.

![image67](images/entries/844d12273c1d3d42e5f1b20367e92bc1144b77fe.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Piers Titus van der Torren
### Prestación: Renderizador vivo de relieve sombreado
QGIS 2.16 tiene un nuevo procesador de ráster que creará dinámicamente un modelo sombreado a partir de un Modelo digital de elevaciones.

![image68](images/entries/62f9492d1949677e316625b415ec732e63fcd3ec.gif)

Esta prestación fue desarrollada por Asger Skovbo Petersen y Nathan Woodrow
## Digitalización
### Feature: \"Repeating\" locking mode for constraints
When enabled, repeating locks are not automatically cleared when a new point is added. They are handy when the same constraint must be repeated for multiple points (eg adding vertices which are always 50 meters apart). This functionality is available in the `Advanced Digitizing Panel`.

![image69](images/entries/f7dced55540bf500c4d9ca5a0efa9bef617c86e5.gif)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Extender geometrías de cadenas lineales con la herramienta reformar
The reshape tool now allows you to extend linestrings, by starting a reshape at either a line\'s start or end point.

![image70](images/entries/52726f3b8cd8b62d63a32b9628dd8d3cef53172c.gif)

Esta prestación fue desarrollada por Martin Dobias
### Prestación: Tolerancia de segmentación
Support was added to set the segmentation tolerance (maximum angle or maximum difference). This setting controls the way circular arcs are rendered. The smaller maximum angle (in degrees) or maximum difference (in map units), the more straight line segments will be used during rendering. You can find this option in `Settings -> Options -> Rendering -> Curve Segmentation`.

![image71](images/entries/c86e3cd9ebab19e1581568eb5804c69ba279787d.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Marco Hugentobler
## Administración de datos
### Prestación: Nuevas opciones de configuración para tablas de atributos
- Allow reordering the attribute table columns (via right click on field name header \--\> \"Organize Columns\" dialog; drag and drop to reorder)
- Permite agregar una nueva columna a la tabla de atributos mediante botones para provocar una acción establecida en la característica elegida
- Las columnas pueden ocultarse de la tabla de atributos (mediante click derecho sobre el encabezado de nombre de campo)
- Ahora QGIS recuerda el ancho de cualquier columna redimensionada

![image72](images/entries/4ac86473163c0b1e322343de1e4013262c2492ce.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/) and [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Stéphane Brunner (Camptocamp)](http://www.camptocamp.com/) and [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Prestación: Columnas Múltiples en formulario de atributos
Al usar el diseñador de arrastrar y soltar, un usuario puede especificar en cuántas columnas deben ser distribuidos los campos.

To enable multiple columns in the \"Fields\" tab of the layer properties:
- Asegúrese que está usando el modo de arrastrar y soltar del diseñador de formularios
- Doble click sobre contenedores de grupo, como pestañas o grupos
- aparecerá un pequeño diálogo dónde puede seleccionar el número de columnas

El orden será primera columna, segunda columna, n-ésima columna, siguiente fila, etc.

![image73](images/entries/f8297ba9ee600c3d41114db96f56b00bb278ba4e.gif)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Prestación: control sobre los atributos a exportar al guardar una capa vectorial
Checkboxes have been added so that you can select which attributes you want included in the export, and you also now have the option to write \"displayed\" values rather than raw values. This option is useful for layers with relations, where you\'d like a literal value included rather than a numeric identifier.

Depending on the data format, the \"displayed value\" is enabled by default, e.g. for export to spreadsheet formats (ODF, XLSX, CSV/Text).

![image74](images/entries/1c9b2b234c1ccb7a1b92af1f5856817f65dc70f1.png.400x300_q85_crop.webp)

This feature was partially funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

Esta prestación fue desarrollada por Jürgen Fischer, Even Rouault
### Prestación: Vista de formularios: columna lateral ahora ordenable
En el modo de formularios de la tabla de atributos QGIS, hay una columna lateral que se puede usar para saltar directamente a una característica específica. Hasta este lanzamiento, esta vista lateral no se podía ordenar. Para ordenar, uno tenía que saltar al modo tabla y luego volver al modo formulario. Ahora se puede ordenar directamente la característica por la vista previa del atributo de característica en el panel lateral eligiendo la función de clasificación en el botón desplegable de expresión sobre la columna lateral.

![image75](images/entries/3d6b97523db9d4389e5dbac8f0befb10d9d8f020.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Prestación: widget de referencia de relación: acceso directo para agregar nuevos valores
The relation reference widget was enhanced to allow quicker extensions of related value lists. If the checkbox \"Allow adding new features\" is enabled in the widget properties (access through \"Fields\" tab in layer properties), a green plus button will appear to the right of the widget. After pressing the \"Plus\" button, the dialog of the related table will open in \"new record\" mode where one can add an additional entry.

![image76](images/entries/5788b370bc8535629699d8b69656335974ca6feb.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)
### Prestación: Mejoras en exportación DXF
Se ha agregado soporte para etiquetado basado en reglas y símbolos rotados, y para generar geometrías 3D.

![image77](images/entries/8a21b400f4e417df6e25f32c8b23191f1ff83628.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Jürgen Fischer
### Prestación: widgets de nivel superior en el diseñador de arrastrar y soltar
Ahora es posible poner widgets directamente en el formulario con el diseñador de arrastrar y soltar. Por lo tanto, puede existir un formulario de diseñador de arrastrar y soltar sin pestañas.

![image78](images/entries/720df275d40a2d527f2492bde7db4dcdc94fc3da.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Característica: seleccion y filtrado basado en formulario
In QGIS 2.16 a new mode was added to the attribute table dialog for searching and filtering features. When activated (using a button on the toolbar or by pressing `CTRL+F`), the dialog will switch to form view and all widgets are replaced with their search widget wrapper variant.

Alongside each widget is a tool button with options for controlling the search/filter behaviour for that field, eg \"equal to\", \"not equal to\", \"is null\", \"greater than\", etc.., with the options presented matching themselves to the corresponding field and widget type.

Aparecen nuevos botones en la parte inferior del formulario para seleccionar características coincidentes (con opciones para agregar a la selección/eliminar de la selección/seleccionar dentro de la selección actual) o filtrar características en la tabla (con opciones para agregar características a un filtro actual o restringir aún más un filtro actual). Aparecen nuevos botones en la parte inferior del formulario para seleccionar características coincidentes (con opciones para agregar a la selección/eliminar de la selección/seleccionar dentro de la selección actual) o filtrar características en la tabla (con opciones para agregar características a un filtro actual o restringir aún más un filtro actual).

You can also access this mode with the new \"Select by Value\" option, or by pressing F3 with a layer selected.

![image79](images/entries/481596921dd3e432cb4414b42e17fce6e7d9e84c.gif)

Esta prestación fue financiada por SIGE, Ciudad de Uster, Morges

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Crear capas GeoPackage
The [GeoPackage](http://www.geopackage.org) format is an open standard for geospatial data that should be on your radar as a replacement for the ESRI Shapefile format. It addresses many shortcomings with the shape file format including limitations in the number and width of fields. In QGIS 2.16 it is now easy to create a new GeoPackage as it has been integrated into the `Layer` toolbar and `Layer -> Create Layer` menu.

![image80](images/entries/34cfb4a4532464ab1983e561228a9a16d16dfd54.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Even Rouault
### Prestación: Restricciones a widgets
In previous QGIS versions there was no way to check the validity of values entered by a user for a feature\'s attributes. Now, a user can specify a constraint on each widget in a layer\'s attribute form. Constraints are created using QGIS\' expressions, eg `"min_population" > 50000`. A \"Not Null\" checkbox is also available to indicate that a value must be entered for the field. Additionally, descriptive text can be added to give the user helpful feedback when a constraint fails.

Constraints are evaluated on the fly while a user is modifying a feature. A tooltip is available on any field having a constraint, showing the constraint\'s expression, the result of the evaluation and a description of the constraint. A message bar will also displayed at the top of the form summarizing any fields which do not meet the constraint criteria.

![image81](images/entries/ab562b71015b29b17a6b86e8e3c5f71838e25d50.png.400x300_q85_crop.webp)

This feature was funded by [the QWAT project](https://github.com/qwat) and the [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch) and [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Prestación: Editar atributos de múltiples elementos simultáneamente
This change allows the attributes of multiple features to be edited simultaneously. It is enabled when the attribute table dialog is in \"form mode\", via a new \"multi edit\" button on the toolbar. There\'s also a shortcut to edit multiple selected features by using `Edit -> Modify Attributes of Selected Features`.

En este modo, los cambios en el valor de los atributos se aplicarán a todas las entidades seleccionadas. Aparecen nuevos widgets junto a cada widget del editor, lo que permite visualizar el estado actual de edición múltiple y revertir los cambios campo por campo.

Los cambios se realizan como un comando simple de edición, por lo que presionar deshacer revertirá los cambios de atributos para todas las entidades seleccionadas a la vez.

Multiedit mode is only available for auto generated and drag and drop forms -it is not supported by custom ui forms.

![image82](images/entries/d0d864bec8d2ec5bd1fa12e48ad7268a30455c82.gif)

This feature was funded by [Kanton Basel Stadt](http://www.geo.bs.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Leyenda de capa
### Feature: New option to zoom to a layer\'s visible scale range
Para las capas con una serie de rango de escala visible, al seleccionar esta opción se establecerá automáticamente la escala a la escala más cercana donde la capa es visible. Además, la interfaz se ha ajustado para que las capas que están fuera de su rango de escala y ocultas se muestren en gris en el árbol de capas.

![image83](images/entries/e15880a6d0d095c8be69eec510f8563b569e5342.gif)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
## Compositor de Mapa
### Prestación: Nuevas herramientas para dibujar polígonos y polilíneas
Dos nuevos tipos de elementos del compositor de formas, basados en nodos, ahora están disponibles en el compositor de mapas. Con estos, puede dibujar polígonos o polilíneas dentro de su composición con solo unos pocos clics.

También se han agregado nuevas herramientas para permitir la edición de nodos (es decir, mover o eliminar nodos) y también para agregar nuevos nodos a una forma existente. ¡Los elementos de polígono y polilínea del compositor también se pueden diseñar utilizando todos los estilos de símbolos disponibles para capas de línea y polígonos!

![image84](images/entries/52e5ebd093c119ee882b1c354fefc97f5e823ffc.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Paul Blottiere (Oslandia)](http://oslandia.com/)
### Prestación: links relativos en las etiquetas del compositor
Now labels and HTML boxes can contain relative URLs. If we don\'t have a base URL, the project file will be used as a base URL.

![image85](images/entries/5efabc11a312d90df04591a62cbafbb85b0ffc4d.png.400x300_q85_crop.webp)

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Patrick Valsecchi (Camptocamp)](http://www.camptocamp.com/)
### Prestación: incrusta entidades de atlas en la fuente HTML del compositor como GeoJSON
This change makes the current atlas feature (and additionally all attributes of related child features) available to the source of a composer HTML item, allowing the item to dynamically adjust its rendered HTML in response to the feature\'s properties. An example use case is dynamically populating a HTML table with all the attributes of related child features for the atlas feature.

To use this, the HTML source must implement a \"setFeature(feature)\" JavaScript function. This function is called whenever the atlas feature changes, and is passed the atlas feature (and all related attributes) as a GeoJSON Feature.

![image86](images/entries/15b7c338bb2fa76444929f3c7ae6fd6614018032.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com/)
### Prestación: Soporte de SGV Parametrizado para el compositor de imágenes SVG
This change makes it possible to change an SVG files fill and outline colors, and outline width when using parameterised SVG files such as those included with QGIS. For more details on parameterised SVG files see [this article](http://blog.sourcepole.ch/2011/06/30/svg-symbols-in-qgis-with-modifiable-colors/).

![image87](images/entries/f9766e2ad952c9a3d4a7fe2ddbdfa20d63b2aff4.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Uso más fácil de HTML en etiquetas
In QGIS 2.16, the base stylesheet of composer labels will automatically set the label font and margins to match the label\'s settings. This allows interactive choice of font, margins and colors and avoids the need to manually set these with CSS within the label HTML code.

![image88](images/entries/d078efbe63f71e8bdf28d476f9da0396f4b7dc0a.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Georeferenciar salidas (ej. PDF) desde el diseñador
En QGIS 2.16, el compositor de mapas georreferencia automáticamente las salidas (cuando el formato de salida lo hace posible, por ejemplo, TIF y PDF).

La opción existente para crear un archivo mundial se ha separado de la selección del mapa a georreferenciar. El nuevo comportamiento es siempre georreferenciar salidas, y solo crear el archivo mundial separado si esa opción está marcada.

![image89](images/entries/e05ee773025d69f028f01ffa15521578be7d3dc3.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: los mapas del Compositor ahora se actualizan automáticamente con preajustes
Cuando un mapa de compositor es configurado para seguir un estilo preestablecido, se actualizará automáticamente cada vez que se cambie el estilo.

A new option has been added in composer map properties: \"Follow visibility preset\" with a combo box to choose the active preset. This is an alternative to \"lock layers\" (and \"lock layer styles\") functionality which just copy a preset\'s configuration, while this new option creates a link to the preset.

The difference is that when a preset is updated, composer map will automatically pick the new configuration when following the preset, while there is no update if \"lock layers\" (and \"lock layer styles\") option is used.

![image90](images/entries/6ef5520185d80b38adcbba6c54e4fbdb6c2584fc.gif)

Esta prestación fue desarrollada por Martin Dobias
## Herramientas de análisis
### Prestación: Parámetros con nombre en expresiones
In QGIS 2.16 the expression engine now supports use of named parameters. This means that instead of writing the cryptic expression: `clamp(1,2,3)` you can use: `clamp( min:=1, value:=2, max:=3)`. This change also allows arguments to be switched, eg: `clamp( value:=2, max:=3, min:=1)`.

El uso de parámetros con nombre ayuda a aclarar a qué se refieren los argumentos para una función de expresión, ¡lo cual es útil cuando intentas interpretar una expresión a posteriori!

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Característica: Más unidades de distancia
La elección de las unidades de distancia se ha ampliado con nuevas opciones que incluyen kilómetros, yardas y millas. El uso de estas unidades evita la necesidad de la conversión manual de distancias (por ejemplo, pies a millas).

![image91](images/entries/a550363f123d3bf08bd53fef79dc92559ae8965d.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Cambios a expresiones
- Support `date + time` = datetime calculations
- Support for `date - date`, `time - time` and `datetime - datetime` type calculations which return an interval.
- New `char()` function for returning a matching character by unicode value

### Prestación: Estadísticas para campos cadena y fecha
El muelle de resumen estadístico ahora puede calcular estadísticas agregadas para los campos de cadena y fecha.

![image92](images/entries/819559c98282bcf044fae47ddcc00908be3adf69.png.400x300_q85_crop.webp)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Mostrar Radio de una Curva con la herramienta de información
Si hace clic en una línea curva con la herramienta de información, QGIS ahora mostrará el radio en la herramienta de información.

![image93](images/entries/70f085e8494b3f65fd801b79fe6e15fe4ec7f012.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Marco Hugentobler
### Prestación: Agregar soporte para expresiones
QGIS 2.16 agrega soporte para varios tipos de agregados al motor de expresión. Éstos incluyen:
1. Aggregates within the current layer, eg `sum("passengers")` Supports sub expressions (ie `sum("passengers"/2)` ), group by ( `sum("passengers", group_by:="line_segment")` ), and optional filters ( `sum("passengers", filter:= "station_class" > 3 )` )
2. Relational aggregates, which calculate an aggregate over all matching child features from a relation, eg `relation_aggregate( 'my_relation', 'mean', "some_child_field" )`
3. A summary aggregate function, for calculating aggregates on other layers. Eg `aggregate('rail_station_layer','sum',"passengers")`. The summary aggregate function supports an optional filter, making it possible to calculate things like: `aggregate('rail_stations','sum',"passengers", intersects(@atlas_geometry, $geometry ) )` for calculating the total number of passengers for the stations inside the current atlas feature

En todos los casos, los cálculos se almacenan en caché dentro del contexto de expresión, por lo que solo deben calcularse una vez para cada conjunto de evaluaciones de expresión.

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: complemento fTools ha sido reemplazado por algoritmos de Procesamiento
fTools is a core plugin that for many years has provided the tools found in the `Vector` menu in QGIS. With the advent of the QGIS processing framework, the fTools began to represent a duplication of effort, and many of the tools have been improved in their Processing equivalents. To address, the fTools plugin has been removed from QGIS and equivalent menu entries have been added to the vector menu, pointing to the Processing framework tools that achieve the same thing.

![image94](images/entries/99f9e994013dd63cdbba44a765ae5b5a0595d533.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Alex Bruy
## Procesado
### Prestación: Establecer ubicaciones de puntos haciendo clic en el lienzo
Los parámetros de procesamiento que esperan una ubicación de punto ahora se pueden establecer haciendo clic en una ubicación en el lienzo del mapa. Anteriormente, las coordenadas debían ingresarse manualmente.

Esta prestación fue desarrollada por Alex Bruy
### Prestación: Soporte de expresiones y variables
Las entradas y salidas en los cuadros de diálogo de algoritmos ahora admiten variables y  expresiones QGIS.

Esta prestación fue desarrollada por Victor Olaya
### Prestación: Algoritmos preconfigurados
Los algoritmos con parámetros preconfigurados ahora se pueden agregar a la caja de herramientas Procesamiento, como acceso directo para un proceso dado.

Esta prestación fue desarrollada por Victor Olaya
### Prestación: Cree un complemento con algoritmos basados en script desde la caja de herramientas
Anteriormente, la única forma de crear un complemento QGIS que agregara nuevos algoritmos a Procesamiento era desarrollar esos algoritmos manualmente y crear un nuevo proveedor de algoritmos. Ahora, los algoritmos se pueden escribir como simples secuencias de comandos de procesamiento, y se puede crear un complemento que los contenga directamente desde Processing Toolbox. Ese complemento se puede distribuir como un complemento regular y extenderá el procesamiento cuando esté activo.

Esta prestación fue desarrollada por Victor Olaya
### Prestación: Uso de administrador de autentificación en algoritmos relacionados con PostGIS
Los algoritmos relacionados con PostGIS ahora usan el administrador de autenticación QGIS para obtener credenciales para la base de datos PostGIS.
- En caso de que se haya establecido un método de autenticación en la conexión PostGIS, se le pedirá al usuario su contraseña maestra.
- En caso de que no se haya establecido un método de autenticación en la conexión, las credenciales se tomarán de la caché de credenciales o, si no se encuentran allí, se solicitarán al usuario y se almacenarán en la caché de credenciales para su uso posterior.

Con esto, ya no es necesario almacenar contraseñas dadas en la configuración de conexión para usar algoritmos relacionados con PostGIS.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Característica: Soporte para escritura de tablas sin geometría
El algoritmo OutputVector ahora admite escribir tablas sin geometría.

Por ahora, esto solo se ha aplicado en el algoritmo Refactor Fields, pero podría extenderse fácilmente a otros algoritmos relacionados con atributos.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

This feature was developed by [Arnaud Morvan (Camptocamp)](http://www.camptocamp.com/)
### Prestación: Algoritmos GRASS adicionales en procesamiento
For this release, QGIS Processing now includes every [vector](https://grass.osgeo.org/grass70/manuals/vector.html), [raster](https://grass.osgeo.org/grass70/manuals/raster.html) and [imagery](https://grass.osgeo.org/grass70/manuals/imagery.html) algorithms from GRASS7. Now, there are more than 300 algorithms for you to use directly from the QGIS interface. You have all the power of GRASS7 directly incorporated into QGIS and you can mix GRASS7 algorithms with all other Processing algorithms without having to use a GRASS7 database.

También se han incluido algunas pruebas unitarias para algunos algoritmos (principalmente para algoritmos ráster e imágenes), lo que hace que la detección de errores sea más fácil de manejar y procesar.

Tenga en cuenta que, por el momento, los algoritmos de procesamiento GRASS7 solo pueden usar y producir capas de vectores Shapefile y rásteres GeoTiff. También hay un límite para algunos algoritmos ráster GRASS7 (todos los algoritmos que manipulan tablas de colores) que duplican capas ráster en directorios temporales. Dependiendo del tamaño de los rásteres de origen, probablemente necesitará algo de espacio en disco para manejarlos.

This feature was developed by [Médéric Ribreux](https://medspx.fr)
## Proveedores de datos
### Prestación: Los conjuntos de datos OGR se abren en modo de solo lectura de forma predeterminada
Permite la edición concurrente de Shapefiles y Tabfiles en QGIS y MapInfo.

This feature was funded by [MEEM (French Ministry of Sustainable Development)](http://www.developpement-durable.gouv.fr/)

Esta prestación fue desarrollada por Even Rouault
### Prestación: manejo mejorado de los campos de tipo DOMINIO de Postgres
QGIS now shows the correct domain type as field type name, and is able to correctly determine the length and precision of domain types. See the PostgreSQL [documentation](https://www.postgresql.org/docs/9.1/static/sql-createdomain.html) to find more information about DOMAIN types.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: hace que el modo readOnly (solo lectura) de capas vectoriales sea configurable en el proyecto
Using this option, you can prevent users from inadvertently editing layers. Go to `Project properties -> Identify layers` to configure which layers should be presented as read only.

![image101](images/entries/9fce381bdf92bd039a26282a93579d5d5ef22e92.png.400x300_q85_crop.webp)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
### Prestación: Soporte de bases de datos DB2
Esta prestación fue desarrollada por David Adler
### Prestación: Actualizar vistas materializadas de Postgres en db manager
### Prestación: Atributos OGR FID mostrados
QGIS ahora muestra el OGR FID como primer atributo cuando es significativo, por ejemplo para controladores GPKG y otras bases de datos.

Esta prestación fue desarrollada por Even Rouault
### Prestación: Servicios ArcGIS Map y Feature REST
QGIS ahora puede conectarse a servicios ArcGIS REST.

Puede conectarse a los servicios de ArcGIS Feature (equivalente a WFS en el mundo de ESRI) y a los servicios de ArcGIS Map (equivalente a WMS). El proveedor le permite leer mapas y capas vectoriales de esos servicios.

Esta prestación es bastante conveniente para los usuarios que desean cambiar de una pila de SRI de ESRI sin perder nada de lo que ya han construido en servicios de mapas privados o públicos. También puede conectarse a los servicios públicos proporcionados por ESRI.

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Prestación: Guardar estilos en bases de datos MS SQL y Oracle
Esta prestación fue desarrollada por Jürgen Fischer y Christian Frugard
### Prestación: Renombrar campos en capas
En QGIS 2.16 ahora puede cambiar el nombre de los campos en Postgres, Oracle, OGR y capas de memoria haciendo doble click en el nombre del campo en la ventana de propiedades de capa.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Soporte básico de Oracle Workspace Manager
Se agregó soporte a Oracle Workspace Manager cuando se usa Oracle Provider.

See <https://github.com/qgis/QGIS/commit/d161612bd216d36dc23ab2307636cf1bc0a36192>

This feature was funded by [ENEL](https://www.enel.com)

This feature was developed by [Jürgen Fischer for Faunalia](http://faunalia.it)
### Prestación: Mejora masiva al Proveedor WFS
QGIS 2.16 trae una revisión del proveedor WFS, incluyendo
- Autodetección de versión
- Almacenamiento en el caché de disco de las funciones descargadas
- Descarga en segundo plano y representación progresiva
- soporte WFS 1.1 y 2.0
- paginación WFS 2.0 GetFeature
- Agregar pruebas de proveedor
- Soporte para uniones WFS 2.0
- Parámetros URI con SQL con cláusulas SELECT / FROM / JOIN / WHERE / ORDER BY 
- Maneja campos DateTime
- Enable \"Only request features overlapping the view extent\" by default (and memorize the settings)
- Soporte para tipos de gemoterías adicionales/mezcladas (CurvePolygon, CompoundCurve)
- Mayor tolerancia para servidores WFS que no se ajustan

![image102](images/entries/d69f2cc2fcc59b26d830bb84c82d5e6c9d89beae.png.400x300_q85_crop.webp)

This feature was funded by [Land Information New Zealand and Canton of Zug, Switzerland](http://www.linz.govt.nz/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Feature: Generation of default values on Postgres layers \"just in time\"
La expresión utilizada para generar valores predeterminados para un campo en la base de datos postgres se está imprimiendo actualmente en el formulario de características.

    nextval('serial')
    
A new option in the \"project properties\" (tab \"Data Sources\") allows evaluating the expression before opening the form and will directly print the new value in the feature form.

    23
    
La principal ventaja de esta mejora es que ahora se puede crear y vincular directamente registros de tablas relacionadas antes de tener que guardar los datos primero, porque la clave principal ya está presente antes de guardar la función.

![image103](images/entries/6d4b378f46ee1338b7aa80f15adf2ea8e510909e.png.400x300_q85_crop.webp)

This feature was funded by [Canton of Zug, Switzerland](http://geo.zg.ch/)

This feature was developed by [Matthias Kuhn](http://www.opengis.ch/)
## Servidor de QGIS
### Prestación: Soporte de remarcación en GetMap y GetPrint
Esta prestación fue financiada por el Cantón de Solothurn

This feature was developed by [Marco Hugentobler, Sourcepole](https://www.sourcepole.com/)
### Prestación: Datum predeterminado para el servidor
Will have to dig through <https://github.com/qgis/QGIS/commit/70863ecaf0ccfcb538e3892af4b528304b21a0a2> to find details

This feature was developed by [Marco Hugentobler (Sourcepole)](https://www.sourcepole.com/)
## Plugins
### Prestación: Actualizado el complemento globo
- Actualizado a OsgEarth 2.8
- Reescribir el controlador de mosaico de globo QGIS
- Reescribir la lógica de sincronización entre 2D y 3D
- Migración a un nuevo núcleo de geometría
- Soporte para múltiples capas de fondo.
- Menús incrustados en la ventana del globo
- Selección de capa independiente para globo
- Trabajo de tesis de maestría del puerto de Mathias Kuhns de QGIS 2.1 / OsgEarth 2.4

![image104](images/entries/f709cc02852b833f459f30431f38f868d69ebfad.jpg.400x300_q85_crop.webp)

This feature was funded by [Sourcepole QGIS Enterprise](http://qgisenterprise.com/)

This feature was developed by [Sandro Mani, Sourcepole](https://www.sourcepole.com/)
### Prestación: Globo: Extruir objetos
Permitir extrusionar objetos en la 3ª dimensión.

Ya sea por un valor fijo o por un atributo o expresión.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Prestación: API: Adicionar páginas a propiedades de capa vector
Permitir agregar páginas adicionales al cuadro de diálogo de propiedades de capa vectorial.

Esto permite poner la configuración para las opciones de capa afín proporcionadas directamente por un complemento donde pertenecen para una mejor experiencia de usuario.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Prestación: Globo: Soporte vector
Al mostrar capas en globo, conserva los datos vetoriales

Esta prestación fue financiada por Master Thesis UZH

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
### Prestación: Globo: Exageración vertical para MDT
Because sometimes it\'s just nice to exaggerate about the size.

This feature was developed by [Matthias Kuhn](http://www.opengis.ch)
## Programabilidad
### Prestación: Widgets incrustados en árbol de capa
Esto permite la definición de widgets incrustados en el árbol de capas para capas individuales en el cuadro de diálogo de propiedades de capa (en la nueva pestaña Leyenda). La idea es tener una forma de acceder rápidamente a algunas acciones que a menudo se usan con una capa.

La implementación viene con un widget de transparencia, en el futuro puede haber más widgets estándar, p. Ej. para configurar el filtrado, la selección, el estilo u otras cosas. La API permite que los complementos registren sus propios widgets, lo que será útil para que varios complementos específicos del dominio asignen widgets personalizados a las capas que administran.

![image105](images/entries/f6cd05f9d927a47543b0c3b1fba740d86a226076.png.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Martian Dobias
### Prestación: Los complementos pueden añadir páginas a las propiedades de capas vectoriales
This feature was developed by [Sandro Mani (Sourcepole)](https://www.sourcepole.com/)
### Prestación: Nuevas clases PyQGIS en 2.16
### Nuevas clases núcleo
- [QgsComposerNodesItem](https://qgis.org/api/classQgsComposerNodesItem.html) -an abstract base class for composer items which provides generic methods for nodes based shapes such as polygons or polylines
- [QgsComposerPolygon](https://qgis.org/api/classQgsComposerPolygon.html) - a composer item for polygon shapes
- [QgsComposerPolyline](https://qgis.org/api/classQgsComposerPolyline.html) -a composer item for polyline shapes
- [QgsGroupUngroupItemsCommand](https://qgis.org/api/classQgsGroupUngroupItemsCommand.htmll) -a composer undo command class for grouping / ungrouping composer items
- [QgsConstWkbSimplifierPtr](https://qgis.org/api/classQgsConstWkbSimplifierPtr.html) -WKB reader which simplifies geometries on the fly
- [QgsAction](https://qgis.org/api/classQgsAction.html) - a utility class that encapsulates an action based on vector attributes
- [QgsActionManager](https://qgis.org/api/classQgsActionManager.html) - stores and manages actions associated with a layer
- [QgsAggregateCalculator](https://qgis.org/api/classQgsAggregateCalculator.html) -a utility class for calculating aggregates for a field (or expression) over the features from a vector layer
- [QgsAttributeTableConfig](https://qgis.org/api/classQgsAttributeTableConfig.html) -a container for configuration of the attribute table for a vector layer
- [QgsDateTimeStatisticalSummary](https://qgis.org/api/classQgsDateTimeStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of datetimes
- [QgsInterval](https://qgis.org/api/classQgsInterval.html) - a representation of the interval between two datetime values
- [QgsJSONExporter](https://qgis.org/api/classQgsJSONExporter.html) - handles exporting QgsFeature features to GeoJSON features
- [QgsJSONUtils](https://qgis.org/api/classQgsJSONUtils.html) - helper utilities for working with JSON and GeoJSON conversions
- [QgsRuntimeProfiler](https://qgis.org/api/classQgsRuntimeProfiler.html) -simple profiler for timing code paths during execution
- [QgsSQLStatement](https://qgis.org/api/classQgsSQLStatement.html) - utility class for parsing SQL statements
- [QgsStringStatisticalSummary](https://qgis.org/api/classQgsStringStatisticalSummary.html) -calculator for summary statistics and aggregates for a list of strings
- [QgsHillshadeRenderer](https://qgis.org/api/classQgsHillshadeRenderer.html) - a renderer for generating live hillshade models
- [QgsArrowSymbolLayer](https://qgis.org/api/classQgsArrowSymbolLayer.html) -line symbol layer used for representing lines as arrows
- [QgsNullSymbolRenderer](https://qgis.org/api/classQgsNullSymbolRenderer.html) -a renderer which draws no symbols for features by default, but allows for labeling and diagrams for the layer
- [QgsSimpleMarkerSymbolLayerBase](https://qgis.org/api/classQgsSimpleMarkerSymbolLayerBase.html) -abstract base class for simple marker symbol layers. Handles creation of the symbol shapes but leaves the actual drawing of the symbols to subclasses.
- [QgsFilledMarkerSymbolLayer](https://qgis.org/api/classQgsFilledMarkerSymbolLayer.html) -filled marker symbol layer, consisting of a shape which is rendered using a QgsFillSymbolV2

### Nuevas clases GUI
#### Widgets reutilizables:
- [QgsMultiEditToolButton](https://qgis.org/api/classQgsMultiEditToolButton.html) -a tool button widget which is displayed next to editor widgets in attribute forms, and allows for controlling how the widget behaves and interacts with the form while in multi edit mode
- [QgsSearchWidgetToolButton](https://qgis.org/api/classQgsSearchWidgetToolButton.html) -a tool button widget which is displayed next to search widgets in forms, and allows for controlling how the widget behaves and how the filtering/searching operates
- [QgsLayerTreeEmbeddedConfigWidget](https://qgis.org/api/classQgsLayerTreeEmbeddedConfigWidget.html) -a widget to configure layer tree embedded widgets for a particular map layer
- [QgsLayerTreeEmbeddedWidgetProvider](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetProvider.html) -provider interface to be implemented in order to introduce new kinds of embedded widgets for use in layer tree
- [QgsLayerTreeEmbeddedWidgetRegistry](https://qgis.org/api/classQgsLayerTreeEmbeddedWidgetRegistry.html) -registry of widgets that may be embedded into layer tree view
- [QgsAttributeFormEditorWidget](https://qgis.org/api/classQgsAttributeFormEditorWidget.html) -a widget consisting of both an editor widget and additional widgets for controlling the behaviour of the editor widget depending on a number of possible modes
- [QgsComposerItemComboBox](https://qgis.org/api/classQgsComposerItemComboBox.html) -a combo box which displays items of a matching type from a composition
- [QgsCompoundColorWidget](https://qgis.org/api/classQgsCompoundColorWidget.html) -a custom QGIS widget for selecting a color, including options for selecting colors via
- rueda de tono, muestras de color y un mezclador de color
- [QgsDockWidget](https://qgis.org/api/classQgsDockWidget.html) - QDockWidget subclass with more fine-grained control over how the widget is closed or opened
- [QgsFocusWatcher](https://qgis.org/api/classQgsFocusWatcher.html) - an event filter for watching for focus events on a parent object
- [QgsGradientStopEditor](https://qgis.org/api/classQgsGradientStopEditor.html) -an interactive editor for previewing a gradient color ramp and modifying the position of color stops along the gradient
- [QgsMapLayerConfigWidget](https://qgis.org/api/classQgsMapLayerConfigWidget.html) -a panel widget that can be shown in the map style dock
- [QgsMapLayerConfigWidgetFactory](https://qgis.org/api/classQgsMapLayerConfigWidgetFactory.html) -factory class for creating custom map layer property pages
- [QgsPanelWidget](https://qgis.org/api/classQgsPanelWidget.html) - base class for any widget that can be shown as a inline panel
- [QgsPanelWidgetWrapper](https://qgis.org/api/classQgsPanelWidgetWrapper.html) -inline panel wrapper widget for existing widgets which can\'t have the inheritance tree changed, e.g dialogs
- [QgsPanelWidgetStack](https://qgis.org/api/classQgsPanelWidgetStack.html) -a stack widget to manage panels in the interface
- [QgsShortcutsManager](https://qgis.org/api/classQgsShortcutsManager.html) -a class that contains a list of QActions and QShortcuts that have been registered and allows their shortcuts to be changed
- [QgsTableWidgetItem](https://qgis.org/api/classQgsTableWidgetItem.html) -this can be used like a regular QTableWidgetItem with the difference that a specific role can be set to sort
- [QgsHillshadeRendererWidget](https://qgis.org/api/classQgsHillshadeRendererWidget.html) -renderer widget for configuring the hill shade renderer
- [QgsRasterTransparencyWidget](https://qgis.org/api/classQgsRasterTransparencyWidget.html) -widget for controlling a raster layer\'s transparency and related options
- [QgsArrowSymbolLayerWidget](https://qgis.org/api/classQgsArrowSymbolLayerWidget.html) -renderer widget for configuring arrow symbol layers

#### Diálogos reutilizables:
- [QgsOrganizeTableColumnsDialog](https://qgis.org/api/classQgsOrganizeTableColumnsDialog.html) -dialog for organising (hiding and reordering) columns in the attributes table
- [QgsConfigureShortcutsDialog](https://qgis.org/api/classQgsConfigureShortcutsDialog.html) -dialog for allowing users to configure shortcuts contained in a QgsShortcutsManager
- [QgsNewGeoPackageLayerDialog](https://qgis.org/api/classQgsNewGeoPackageLayerDialog.html) -dialog to set up parameters to create a new GeoPackage layer
- [QgsSourceSelectDialog](https://qgis.org/api/classQgsSourceSelectDialog.html) -generic widget class for listing layers available from a remote service

## Correcciones Notables
### Prestación: Programa de corrección de errores pagado de QGIS
Hicimos otra ronda de corrección de errores pagados (¡gracias a nuestros patrocinadores y donantes!). A continuación, siga los resúmenes de trabajos de los desarrolladores que participaron:
### Nyall Dawson
Here\'s the full list (sorted by priority):
- Reparar la transformación proyectiva rota en georeferenciador (#14551 - severo)
- Corregir selección de elementos por radio falla (#14748 - severo)
- Se corrigió el cálculo de área incorrecta para el polígono (# 14675 - grave, aunque es muy poco probable que ocurra. Se agregaron pruebas unitarias para cubrir este caso límite)
- Arreglar el diseño del muelle de widget (# 15011 - grave)
- Corregir caída en capa símbolo flecha (no reportado)
- Corregir caída cuando se crea unión no válida (no reportado)
- Corregir los SVG parametrizados que no se muestran para elementos de flecha del compositor (# 14997 - alto)
- Classifications on joined fields should only consider values which are matched to layer\'s features (#9051 - high)
- Utiliza siempre la comparación de cadenas en expresiones para campos de cadena (# 13204 - alto)
- Se corrigió el directorio de inicio que se agrega como svg predeterminado y ruta de plantilla (# 14662, # 14652, # 14883 - alta)
- Se corrigió el bloqueo al usar polígonos invertidos con el procesador de mapas de calor (# 14968 - alto)
- Guardar los valores de simbología ráster con total precisión (# 14950 - normal)
- Las acciones no están habilitadas al cargar la capa con el estilo predeterminado (# 13910 - normal)
- Remove \"attribute table\" text from dialog title (#14959 - normal)
- Corregir que no se puede desactivar el receptor del widget de personalización (# 9732 - normal)
- Corregir que en una capa de símbolo el ancho/alto de la cabeza de la flecha está volteado (# 15002 - normal)
- Corregir que las uniones no se recrean al cargar proyectos con capas defectuosas (# 10500 - normal)
- Invalidar caché de unión cuando se modifica la capa (# 11140 - normal)
- Admitir correctamente las uniones mediante campos virtuales (# 14820 - normal)
- Corregir que es posible que los campos virtuales que dependen de otros campos virtuales no se calculen en algunas circunstancias (# 14939 - normal)
- Se corrigieron las etiquetas basadas en reglas que no se muestran al usar funciones de expresión de python (# 14985 - normal)
- Actualización automática cuando los niveles de símbolo cambian en la base de estilo (# 14861 - normal)
- Corregir que el estilo del botón Dock no está sincronizado con el estado Dock (# 14862 - normal)
- Solucionar problemas al renderizar SVG con texto (# 14644, # 14794 - normal)
- Asegurar que los campos que se muestran en el botón de datos definidos estén siempre actualizados (# 14809 - normal)
- Corregir que no puede establecer un acceso directo para acercar (# 14958 - normal)
- Fix inverted polygons and displacement renderer don\'t allow right click on legend items (#14966 - normal)
- Fix inverted polygon & displacement renderer don\'t show colour wheel in legend menu (#14967 - normal)
- Agregar proxies faltantes para el comportamiento de verificación de leyenda a subprocesadores para polígonos invertidos y renderizadores de desplazamiento (no informados)
- Fix joined attributes can\'t be used in filter expressions (#13176 - low)
- Mostrar el tipo de WKB en los metadatos de la capa vectorial (no se informa)
- Adicionar cadenas de capacidades faltantes a capa metadatos (no reportado)
- Solucionar el ruido de depuración al usar capas de geometría 25D (no reportado)
- Corregir algunos widgets de la barra de estado que no podían ocultarse a través de la personalización (no informados)
- Hacer que el widget de estilo se aplique en vivo, recuerde la configuración (no se informa)
- Don\'t show constraint messages when form is in search mode (unreported)
- Mostrar barras de desplazamiento para atributos de formulario como identificar resultados (no informados)
- Hacer que el botón Aplicar estilo del muelle siempre esté habilitado (no se informa)
- Corregí algunas actualizaciones automáticas faltantes de la base de estilo (no se informa)

I also forward ported a bunch of fixes from Sourcepole\'s fork.
### Even Rouault
Aquí están los reportes con los que ha tratado durante su tiempo asignado para la corrección de errores QGIS 2.16

**Severo/Alto:**
- <https://issues.qgis.org/issues/15006>: Crashes in standalone browser
- <https://issues.qgis.org/issues/14876>: WFS client broken in QGIS master
- <https://issues.qgis.org/issues/13762>: Error accessing external WMS server \--WMS provider: Cannot calculate extent
- <https://issues.qgis.org/issues/14927>: Attribute table sorting problem with qgis-rel-dev (2.14.X regression)
- <https://issues.qgis.org/issues/15064>: QGIS crashes on OGR layers with wkbUnknown25D, wkbUnknownM/Z/ZM layer geometry type
- <https://issues.qgis.org/issues/14844>: Oblique Mercator projection hanging when rendering map
- <https://issues.qgis.org/issues/15047>: ASSERT failure in QVector\[HTML_REMOVED\]::at: \"index out of range\" in qgis_attributetabletest (TestQgsAttributeTable)
- <https://issues.qgis.org/issues/15087>: Crash when deleting the last segment of a compoundcurve

**Normal**
- <https://issues.qgis.org/issues/14965>: wfs provider copies features when zooming in and out
- <https://issues.qgis.org/issues/14928>: WMS request without BBOX
- <https://issues.qgis.org/issues/14999>: Spatialite provider does not support alphanumeric primary keys (backport in 2.14)
- <http://hub.qgis.org/issues/15061>: Cannot add WFS layer
- <https://issues.qgis.org/issues/15065>: Failed detection of geometry type in some conditions
- <https://issues.qgis.org/issues/15066>: OGR: Sublayers detected sometimes when not relevant (Polygon/CurvePolygon)
- <https://issues.qgis.org/issues/15067>: DXF export creates invalid file
- <https://issues.qgis.org/issues/15081>: Impossible to clear geometry of feature from a shapefile
- unreported \[Geometry\] Fix various issues related to Wkb/Wkt import

**Otro:**
- <https://issues.qgis.org/issues/14981>: Import of Shapefile to Geopackage-Database in DB-Manager fails (analysis)
- <https://issues.qgis.org/issues/15011>: Browser panel is unusable (bisection & analysis)
- <https://issues.qgis.org/issues/14909>: regression: QGIS crashes when closing docked attribute table (analysis)
- <https://issues.qgis.org/issues/13353>: QGIS and gdal 2.0.0 (closed: no further action needed)
- <https://issues.qgis.org/issues/15053>: WMS with EPSG:31255 is shifted (datum=hermannskogel) (analysis. probably outdated proj.4 version)

### Sandro Santilli
- <http://hub.qgis.org/issues/14262>: Overflow on primary key with negative values; cannot save edits
- <http://hub.qgis.org/issues/12228>: Deadlock from parallel rendering
- <http://hub.qgis.org/issues/11371>: Map Composer: group + move + ungroup + undo = crash
- <http://hub.qgis.org/issues/14976>: Repository files modified by \"make check\"
- <http://hub.qgis.org/issues/13635>: Different handling of invalid geometries between LTR and master version
- <http://hub.qgis.org/issues/13952>: QGIS node tool causes snapping another feature randomly

### Martin Dobias
- Digitizing: \"Simplify Feature\" should not open a dialog when no feature is clicked
- Digitizing: how to abort \"Simplify Feature\" or \"Rotate Feature\" tool is not that obvious
- Falta un camino sobre agregar capa vectorial.
- El autotracing falla con arcos circulares en geometrías
- WMS no funciona en master a625eeb (2.15.0-80)
- Procesando algoritmos preconfigurados error de python
- GPS don\'t record geometry point, but only attribute values\...
- muelle de estilo: el panel de transparencia (transparencia global, píxel transparente, etc.) no funciona para el renderizador de sombreado
- muelle de estilo: falta el botón de retroceso y la ruta de exploración cuando se edita una regla de etiqueta basada en reglas
- Corregir deshacer/rehacer para el renderizado/etiquetado basado en reglas en la barra de estilo
- Reparar las actualizaciones del widget de deshacer en el panel de estilo
- style dock: hillshade renderer\'s global transparency value resets after changing symbology settings
- style dock: values of raster\'s layer rendering options not properly restored

### Matthias Kuhn
- Mejorar la estabilidad de QgsMapLayerRegistry
- Processing: Difference algorithm: don\'t ignore invalid geometries by default
- Se corrigieron algunos problemas de compatibilidad de Python 3
- Trabajar para volver a habilitar las pruebas de osx (fusionadas después de la versión 2.16)
- Documentación de la API
- startup.py se ejecuta dos veces
- Correcciones UX:
  - Tabla de atributos: siempre muestra números de encabezado de columna secuenciales
  - Widget de referencia de relación: solo habilitar el botón de formulario cuando se establece una entidad
  - Mostrar ID de entidad en la herramienta de información de la tabla de atributos
  - Foco inicial del widget en el diálogo de credenciales
  - Tiempo de espera predeterminado para elementos de la barra de mensajes
  - Add button\" state in postgis source select dialog
- Instalar archivos de encabezado faltantes
- Ruptura al salir
- Directorio de caché de red
- Formulario de características oculto detrás de la ventana principal en Windows
- Edición sin conexión: respetar rutas relativas
- Edición sin conexión: los atributos modificados terminan en una entidad incorrecta
- Offline editing: Don\'t crash with raster layers
- Relation form crece infinitamente
- Corregir caída cuando se carga el estilo de una capa
- Se reparó el bloqueo al cerrar la tabla acoplada de atributos
- Corregir la ruta gpsbabel predeterminada mal configurada
- Muestra el recuento de entidades correcto con una regla que requiere geometría
- Se corrigió el bloqueo al usar el renderizador 2.5D con capa incompatible

{{<content-end >}}
