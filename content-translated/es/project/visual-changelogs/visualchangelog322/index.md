---
HasBanner: false
draft: false
releaseDate: '2021-10-22'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.22
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.22{#changelog322 }
![image1](images/projects/badbeb89221e014ed31e7ea07919c9e734df39b2.png)

Fecha de lanzamiento: 2021-10-22

QGIS 3.22 Białowieża is aimed at celebrating the 100-year anniversary of [Białowieża National Park](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_National_Park), Poland, which was established in 1921. [Białowieża Forest](https://en.wikipedia.org/wiki/Bia%C5%82owie%C5%BCa_Forest) is one of the world's last primary woodlands, located on the border between Poland and Belarus. It is one of the few natural old-growth forests in temperate lowland Europe and has been protected for over 600 years. The outstanding value of Białowieża Forest has been acknowledged by its recognition as a [UNESCO Natural World Heritage Site](https://whc.unesco.org/en/list/33).

Białowieża Forest is named after the village Białowieża, which is located right in the middle of this woodland. It is one of the oldest settlements in the area, nowadays hosting numerous research and tourism activities. Today, there are three research institutions in the village: [Białowieża Geobotanical Station, University of Warsaw](https://bsg.bialowieza.pl/en/), [The Mammal Research Institute, Polish Academy of Sciences](https://ibs.bialowieza.pl/en/), and the [Forest Research Institute, Department of Natural Forests](https://www.ibles.pl/en/web/guest/home). Additionally, a large number of scientists from Poland and abroad travel to Białowieża in order to carry out their studies, and as such, there are also other users of QGIS in the area, as well as additional projects which contribute to the Open Data and Open Source Software ecosystems, such as the [Open Forest Data](https://openforestdata.pl/) project.

You can learn more about the project and this release of QGIS at the dedicated project website, <https://qgisbialowieza.pl>.

This feature-packed release includes a vast number of user experience enhancements and controls added to various advanced functionalities. In addition to a host of additional mesh functionality and operational improvements, QGIS Desktop now includes annotation tools and support for annotation layers, amongst much, much more. For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video at <https://youtu.be/U-RHBt6WZi8>

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official project sustaining member, please visit our [sustaining member page]({{< ref "/funding/membership.md" >}}) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es un software libre y no está obligado a pagar nada por utilizarlo. De hecho, queremos animar a la gente a utilizarlo, independientemente de su situación económica o social, ya que creemos que dotar a la gente de herramientas para la toma de decisiones espaciales dará lugar a una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Notas
### Prestación: Propiedades y efectos de la capa de anotación
Las propiedades adicionales de las capas de anotación incluyen ahora las siguientes:
- Una ventana de propiedades de la capa de anotación, que contiene información básica sobre la capa y opciones para establecer rangos de escala, opacidad, modo de fusión y efectos de dibujo para la capa
- An option to view the main annotation layer\'s properties via the annotation toolbar (the main annotation layer is the hidden layer which is always present above all other map layers, so it\'s impossible to open it\'s property window via the layer tree)
- Options to set an annotation layer\'s opacity/blend mode/paint effect in the layer styling dock for interactive changes

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Edición de nodos en un elemento de anotación
La herramienta de modificación de anotaciones puede utilizarse ahora para editar los nodos de un elemento de anotación haciendo clic sobre un nodo existente y moviéndolo. Las interacciones del usuario siguen los patrones estándar de QGIS, como se indica a continuación:
- Clic izquierdo para iniciar el movimiento
- Segundo clic izquierdo para aplicar los cambios
- Clic derecho para cancelar
- Si se selecciona un nodo y se pulsa suprimir, se eliminará el nodo
- Al hacer doble clic en un segmento se añade un nodo

![image2](images/entries/4510afc65b63bab4ab46e0408a6c4c4207aff40f.gif)

Esta prestación fue financiada por el grupo de usuarios suizo de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mover la anotación seleccionada con las teclas del cursor
Cuando se selecciona un elemento de anotación, se puede mover pulsando las teclas del cursor.

Esta funcionalidad incluye la posibilidad de utilizar los atajos de teclado de una manera que sigue el mismo patrón de interacción que se utiliza con los elementos de diseño:
- `shift + cursor`: Big movement
- `alt + cursor`: 1px movement

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Creación de herramientas de anotación de líneas y polígonos
Se han añadido a las herramientas de anotación funciones para crear nuevos elementos de anotación de líneas y polígonos.

Éstas admiten las mismas interacciones que las funciones de dibujo vectorial, como el ajuste, el trazado, el acoplamiento de cad, el retroceso para eliminar vértices, los modos de digitalización de curvas y corrientes, y otros.

Esta prestación fue financiada por el grupo suizo de usuarios de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Nueva herramienta de texto puntual
Se ha creado un marco para que las herramientas cartográficas creen nuevos elementos de anotación, incluida la posibilidad de crear nuevos elementos de anotación de texto puntual.

![image3](images/entries/4822b0a64c8a57a049ae15acb8c77a27709172d5.gif)

Esta prestación fue financiada por el grupo de usuarios suizo de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Barra de herramientas de anotaciones
Se ha añadido una nueva barra de herramientas de anotaciones que proporciona acciones para lo siguiente:
- Crea una nueva capa de anotación vacía en el proyecto actual.
- The \"Modify Annotations\" tool, which provides an interface for editing existing annotations.

Las operaciones admitidas para la función de modificación de anotaciones incluyen:
- Al hacer clic en una anotación existente para seleccionarla, se muestran sus propiedades en el muelle de estilo de la capa, incluidos el símbolo, la escala de referencia, el índice z, etc.
- Haga clic con el botón izquierdo del ratón en un elemento de anotación seleccionado para empezar a moverlo. Un clic con el botón derecho o un escape cancelan el movimiento, mientras que un segundo clic con el botón izquierdo confirmará el movimiento.
- Si se pulsa la tecla de borrado mientras se selecciona una anotación, se borrará dicha anotación

Esta prestación fue financiada por el grupo suizo de usuarios de QGIS

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Herramientas de mapa
### Feature: Add a \"measure bearing\" map tool
This tool behaves similarly to the existing \"measure angle\" map tool, but requires the user only to click two points on the map and displays the bearing between these points.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Interfaz de usuario
### Prestación: Alternar la edición en varias capas seleccionadas
The *toggle editing* action has been modified to support activation on all selected layers, making it easy to start and stop editing sessions across multiple layers simultaneously. Although the editing session status for all selected layers may not be the same, all selected layers will be toggled to an active or inactive state as the inverse of the current state of the currently active layer. This functionality is applied to the menu item *Layer \> Toggle Editing*, the *Toggle Editing* button on the digitizing toolbar, and the *Toggle Editing* entry in the layers context menu.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Prestación: Identificar grupos de capas y todas las capas seleccionadas
Whilst the identify features tool supported multiple selection modes, the \"current layer\" mode has been extended to support the selection of layer groups, and will identify features from all selected layers. Only features from visible layers within a layer group will be identified.

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Feature: Add a \'Show in Files\' action for all file items in browser
Abre una ventana del explorador de archivos y selecciona directamente el archivo

Also fixes the existing \"File Properties\" action so that it shows regardless of the file type, and doesn\'t show incorrectly in some circumstances.

![image4](images/entries/f80090adb3c2f85fa81b5689741afd936f8d5439.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Simbología
### Prestación: Unidades personalizadas para las capas de símbolos del generador de geometría
Los generadores de geometría ahora exponen una opción para que los usuarios seleccionen las unidades que deben utilizarse para devolver las geometrías, en lugar de admitir únicamente las unidades definidas en el SRC de la capa. Esto es especialmente útil en situaciones en las que el símbolo no está asociado a una capa, como cuando se utiliza en elementos de diseño.

La actualización ofrece las siguientes opciones de unidades:
- Unidades del mapa (el comportamiento anterior, por defecto)
- Milímetros
- Píxeles
- Pulgadas
- Puntos

When millimeters, pixels, inches or points are selected, then the \@map_geometry variable will be available for use within the expression, containing the feature geometry in the specified units (relative to the map frame), whilst the \$geometry variable remains available within the expression in the layer CRS map units.

![image5](images/entries/d1c6b0c69cf9dd8247d1dc0e370d0182b550f48a.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Escala de referencia simbólica para capas vectoriales
Se ha expuesto una opción que permite configurar las escalas de referencia para las simbologías de características en las capas vectoriales.

En la práctica, esto define la escala relevante del mapa en la que la simbología configurada y los tamaños de las etiquetas pueden referenciarse con unidades basadas en el papel, como milímetros o puntos. Estos tamaños de unidad se escalarán automáticamente en consecuencia, basándose en la relación de la escala de referencia pertinente y la escala de la vista del mapa actual.

Por ejemplo, cuando una capa de líneas está configurada para utilizar una línea de 2 mm de ancho utilizando una escala de referencia de 1:2000, el elemento se representaría utilizando líneas de 4 mm de ancho a una escala de mapa de 1:1000, o de 1 mm con una escala de mapa de 1:4000.

Esta prestación ha sido financiada por North Road, gracias a SLYR

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Opción de filtro de inversión de colores para la representación de trama
Ahora es posible invertir los colores de una trama que se está representado mediante una nueva opción de inversión de colores. Esto puede ser útil en varias ocasiones. Por ejemplo, un mapa base rasterizado claro puede convertirse rápidamente en un mapa base oscuro sin necesidad de volver a crear un nuevo conjunto de datos rasterizados.

![image6](images/entries/0fc6bce9e9240b7e354b84d7477439798fd64a59.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Etiquetando
### Prestación: Especificación de la unidad para la rotación de la etiqueta definida por los datos
Especificar la unidad de ángulo para la rotación de la etiqueta definida por los datos

![image](images/entries/126294292-06c91bd5-83d2-4d6f-88a2-38fa2d303c86.webp)

![Peek 2021-08-29 14-38](images/entries/131250678-52360214-31a9-4cf9-ad84-b10a4f78c431.gif)

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Malla
### Prestación: Crear nueva capa malla
QGIS soporta ahora la creación de nuevas capas de malla.

La creación de mallas admite los siguientes formatos de creación:
- Nueva capa de malla vacía
- Nuevo marco de malla basado en una malla existente dentro del proyecto
- Nuevo marco de malla basado en una malla existente de un archivo

![image9](images/entries/8ba4033bf4f8eea7e3776db420b34d6c51358859.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Edición del marco de la malla
QGIS admite ahora la edición de marcos de malla, lo que permite garantizar la coherencia de la malla y ofrece la posibilidad de deshacer y rehacer las operaciones de edición.

This introduces the `QgsMeshEditor` class to the QGIS Python API, which allows for performing edit operations, and the QgsTopologicalMesh class which is not exposed to the Python API but is used for ensuring that edited mesh elements remain topologically correct and perform data modifications.

![image10](images/entries/71bed70b1ced3fef5e3b8190cc613f3cb60f0fac.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Ciclo de vida de la edición del marco de malla
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

La edición de cuadros de malla soporta ahora un conjunto completo de funcionalidades para controlar las operaciones del ciclo de vida de la edición, incluyendo inicio, confirmación, retroceso y cancelación, de forma similar a las capas vectoriales.

![image11](images/entries/9463f4559796ff4808fcd05d1ffbec3aa6d6bae4.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Herramienta de edición del mapa de malla
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools.

La herramienta de mapa de edición de malla ahora soporta las siguientes operaciones:
- Añadir vértices/caras
- Seleccionar vértices/caras
- Eliminar vértices/caras
- Cambiar los valores Z de los vértices
- Mover vértices
- Interacción con los bordes
- Dividir caras

![image12](images/entries/ce164b754aff6438bb6db52a4d5c2eb3e103af62.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Mejoras avanzadas en la edición de mallas
This feature has been introduced in the scope of [QEP 228](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/228) which outlines the introduction of Mesh Editing tools, implements changes to the User Interface, and exposes new functionality to the API.

La interfaz de usuario de QGIS proporciona funciones de triangulación de delaunay y refinamiento de caras, a las que se puede acceder desde el menú contextual del mapa cuando se seleccionan vértices y/o caras de una capa de malla. Estas opciones pueden migrar a los botones de la barra de herramientas de la malla una vez que se hayan introducido más funciones.

![mapToolrefine](images/entries/125721486-055c4cc3-5309-4455-bc5c-e00d6f349bc4.gif)

La API de QGIS también se ha ampliado para soportar la edición avanzada de mallas, que se introduce mediante una nueva clase abstracta de interfaz QgsMeshAdvancedEditing. Las clases derivadas de esta clase pueden ser implementadas para realizar alguna edición avanzada sobre una malla: generación de caras para añadir a la malla, operación particular sobre muchas caras o vértices. La edición avanzada se realiza pasando una instancia de QgsMeshAdvancedEditing a una instancia de QgsmeshEditor, y la edición se aplica como otras operaciones de edición.

En esta función se implementan dos funciones de edición avanzada:
- Triangulación de Delaunay
- Refinamiento de las caras

![image14](images/entries/a914bfb8a85bf2ab2232e8bfad6c3af3cdd751cb.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Seleccionar elementos de malla editables por polígono
Ahora los usuarios pueden seleccionar elementos de malla dentro de un área digitalizada al realizar la edición de la malla. Cada vértice del polígono se digitaliza haciendo clic con el botón izquierdo, mientras que haciendo clic con el botón derecho se completa y valida el polígono para seleccionar los elementos de malla que se cruzan (caras y vértices). La tecla de retroceso permitirá al usuario eliminar el último vértice, y la tecla de Escape permitirá al usuario volver al modo de digitalización normal.

Esta función admite dos modos de comportamiento con diferentes predicados de selección, como se indica a continuación:
- Se seleccionarán los elementos que se toquen (por defecto), o los que se incluyan parcialmente o se crucen (banda elástica verde).
- Se seleccionarán los elementos contenidos, o completamente incluidos (goma azul).

![image15](images/entries/6a687b260a4d3a41c432360336393ee2746997c8.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Seleccionar elementos de malla por geometrías existentes
Se han añadido dos acciones para seleccionar elementos de malla a partir de geometrías presentes en capas vectoriales existentes.

Una vez seleccionadas las geometrías de las capas vectoriales, el usuario puede utilizar estas herramientas para seleccionar los elementos de la malla utilizando los predicados de tocar o contener.

![image16](images/entries/4a918fc1feabd7e3c68282b1b6d052c8504d6013.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Seleccionar elementos de malla por expresión
An interface has been created for selecting mesh elements by expression during mesh editing. In addition, a contextual expression function `$face_area` has been added that returns the area of a mesh face.

![image17](images/entries/141acf32014c3ce387ff61e39cabf3e04c6d3896.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Tranformar vértice único
Un nuevo modo de edición para la herramienta de transformación de malla permite al usuario importar las coordenadas de un solo vértice seleccionado.

El botón de la herramienta en la parte superior derecha de la ventana Transformar Vértices de Malla activa este modo, y cada vez que se selecciona un solo vértice se rellenan automáticamente los campos disponibles para que el usuario pueda ajustar las coordenadas del vértice en consecuencia.

![image18](images/entries/2148b3024a51a218bafafbbe26f74c30692222f6.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Reindizar/ renumerar la capa de malla
Ahora los usuarios pueden reindizar (o renumerar) los vértices y las caras de una capa de malla durante la edición. La renumeración es una optimización de la malla con el algoritmo Cuthill-McKee.

![image19](images/entries/5da7e6705568488c08fbf7faaf311b2eca46c9da.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Forzar la malla por polilíneas
Al editar elementos de malla, los usuarios pueden ahora transformar los elementos forzándolos a ajustarse a una superficie definida por polilíneas existentes, o líneas de ruptura. Las caras se ven obligadas a seguir las líneas de ruptura, es decir, los bordes de las caras encontradas tienen que estar en estas líneas. Los usuarios pueden seleccionar las geometrías de las líneas de ruptura y, a continuación, utilizar el botón dedicado para transformar los elementos de malla que se cruzan.

Las opciones proporcionadas para la transformación incluyen:
- Añadir nuevos vértices cuando las líneas cortan las aristas internas
- Interpolar el valor Z de los vértices recién añadidos en la malla o de las líneas
- Ajuste de la tolerancia para desplazar los vértices existentes en su lugar e impedir la creación de nuevos vértices a lo largo de la línea dentro de la distancia especificada

![forceByBreakLine](images/entries/132239197-096d733b-b519-4aab-9384-79724fd84331.gif)

Whilst the term \"break lines\" is typically used to refer to polylines that constrain a surface or TIN to the defined positions, these break lines are often components of the mesh itself, and additional operations would continue to constrain the surface to these lines. This functionality specifically transforms the surface in a static manner, so that future operations are not constrained to the lines used to transform the mesh elements.

![image21](images/entries/704c731583ce48d963fe9878177bc40639ae3078.webp)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Transformación de malla por expresión
User can perform geometrical transformations on a mesh using an expression to change the vertices\' coordinates. All coordinates (X,Y,Z) of selected vertices can be calculated with an expression, allowing transformation of the mesh while the mesh is still valid.

With a valid expression, selecting the \"Preview transform\" option will calculate the new expression based mesh coordinates and identify whether the transform is valid and may be applied.

Si la vista previa es verde, la malla transformada es válida y el usuario puede aplicar la transformación. Si la vista previa es roja, la malla transformada no es válida y el usuario no puede aplicar la transformación.

Una vez aplicada, los usuarios tienen la opción de deshacer o rehacer la operación.

![image22](images/entries/04937a2d9bba1e27712351f52e6b6f4d5fc0be4d.gif)

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
## Representación
### Prestación: Permitir el uso de PPP físicos para el lienzo del mapa
Se ha puesto a disposición un nuevo ajuste para utilizar correctamente los DPI físicos de la pantalla en lugar de los DPI lógicos, lo que permite que los símbolos se representen por igual en los distintos dispositivos conectados (con altos y bajos dpi), y en aplicaciones móviles como QField.

Este ajuste está desactivado por defecto para garantizar que los símbolos no se escalen de forma diferente a como lo hacían en versiones anteriores de QGIS.

This feature was developed by [Matthias Kuhn](https://github.com/m-kuhn)
### Prestación: Opacidad de la capa rasterizada definida por los datos
Se ha expuesto un nuevo control que permite definir la opacidad de una trama con datos. Esto permite la representación variada de una capa de trama, en varios contextos, como en diferentes páginas de un atlas, siendo dependiente de la visibilidad de otra capa, o ajustada por variables temporales, etc.

Additionally, a \"redraw layer only\" temporal mode for raster layers has been added, which causes a raster layer to be redrawn on each new animation frame as in the equivalent functionality for vector layers. This may be useful in many contexts, such as when the layer uses time-based expression values like the data defined renderer opacity to fade in or out a raster layer from an animation.

![image23](images/entries/881acd52afafba75698f1d7668794b80b594baef.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Diseño de impresión
### Prestación: Soporte de escala predefinida para atlas de puntos
Los elementos del mapa de disposición han ganado soporte para el modo de escala predefinido cuando se controla por atlas de puntos. Esto garantiza que se observe el comportamiento correcto cuando las características del atlas son geometrías multipunto con áreas envolventes variables.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Indentación de grupos y subgrupos de leyendas
Two new entries have been added to the \"Spacing\" section of the Legend properties:
- Sangría de los elementos del grupo
- Sangría de los elementos del subgrupo

Los elementos que pertenezcan a grupos o subgrupos se desplazarán a la derecha en la cantidad especificada. Cuando se añadan parches de leyenda a la izquierda de las entradas, también se sangrarán.

![image24](images/entries/3792e9ae5124b81f1b4289cab220fdbb237851a8.webp)

This feature was developed by [Jürnjakob Dugge](https://github.com/jdugge)
## Expresiones
### Feature: Mesh expression functions for vertex_as_point and vertex_z
Se han añadido expresiones para interactuar con las capas de la malla, con las siguientes funciones que devuelven el valor relacionado con el vértice actual:
- `$vertex_as_point`: returns the current vertex as a geometry point
- `$vertex_z`: returns the Z value of the current vertex.

These two functions are contextual and need to be added in a `QgsExpressionContext` with `QgsExpressionContextUtils::meshExpressionScope()` for the creation of a specific `QgsExpressionScope`.

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Feature: Expression function for \$z
The z value for the current feature in an expression context can now be retrieved using `$z`

This feature was funded by [Hydrotec](https://www.hydrotec.de/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Expresión de la transformación afín
An affine_transform function has been added to QGIS Expressions.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Prestación: Expresión de la distancia recta2d
A straight_distance2d function is now available in QGIS expressions for retrieving the direct/ Euclidean distance between the first and last vertex of a curve geometry feature.

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
### Prestación: Añadir expresión de sinuosidad
Se ha añadido una función de sinuosidad a las expresiones de QGIS.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Feature: New exif() and exif_geotag() functions
Se ha añadido un nuevo par de funciones al motor de expresión de QGIS para leer las etiquetas exif de los archivos de imagen. Las dos funciones son:
- exif(path, tag) : this function returns the value of a given tag string for the provided image file path; when the second optional parameter isn\'t provided, the function will return a map object containing *all* exif tags and their values.
- exif_geotag(path) : this function returns a point geometry from the exif geotags containing in the provided image file path.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Digitalizando
### Prestación: Optimización del algoritmo de ajuste geométrico
El ajuste de la geometría es ahora increíblemente rápido después de beneficiarse de otra ronda de trabajo de optimización. Los pequeños valores de distancia de ajuste que cuelgan a QGIS para siempre son ahora cosa del pasado.

This feature was funded by [SwissTierras Colombia](https://www.swisstierrascolombia.com/)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Convertir en curva con la herramienta de vértices
The ability to convert vertices to or from curved vertices is now supported with the Vertex tool, allowing users to convert vertices with the \"C\" and \"O\" keys.

Additionally, methods for `convertVertex()` have been introduced for the `QgsGeometry` and `QgsCompoundCurve` objects in the QGIS API.

![image25](images/entries/fcc006352c7b09e37d6d8511ecb7fe2ae6a8be50.gif)

This feature was funded by [Swiss QGIS user group](https://qgis.ch/)

This feature was developed by [Olivier Dalang](https://github.com/olivierdalang)
### Prestación: Añadir soporte Z/M en la digitalización avanzada
Las herramientas de digitalización avanzada de QGIS admiten ahora la introducción de valores Z y M definidos por el usuario, lo que mejora en gran medida el control disponible para las características recién digitalizadas, como los componentes de las redes 3D.

![image26](images/entries/287d041be909700393995e3018fba76f41e09a67.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
## Administración de datos
### Prestación: Soporte para arrastrar y soltar el widget de archivos de almacenamiento externo
Ahora los usuarios pueden utilizar la función de arrastrar y soltar en un widget de recursos externos cuando se ha definido y configurado adecuadamente un almacenamiento externo.

![image27](images/entries/038bb187a174a4c491f3f2db6ef03cec5b75e43d.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
### Prestación: Tamaño del conjunto de datos basado en el archivo y fecha de última modificación en el diálogo de propiedades de la capa
The layer properties dialog\'s information panel now shows the size and last modified date of file-based datasets, removing the need to retrieve these details from a file manager. These additional details are also visible in the browser panel\'s information section. For datasets formed of more than a single file, the size will reflect the sum of all the auxiliary/ sidecar files forming the dataset.

![image28](images/entries/10c72ab958bb1e7a59f8f81afb81d33780ed0834.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Cambiar el nombre de los archivos en el navegador QGIS
Se ha añadido una acción de cambio de nombre al submenú de gestión de archivos en el navegador QGIS. Si el archivo renombrado corresponde a un conjunto de datos espaciales con múltiples archivos auxiliares/secundarios, éstos serán renombrados en consecuencia.

Además, se advierte a los usuarios si el archivo es una capa que existe en el proyecto actual y se les pregunta si desean actualizar automáticamente todas las rutas de las capas en consecuencia.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Move GPS tools \"add gpx layer\" functionality to Data Source Manager
Functionality from the GPS tools plugin to add GPX layers has been moved to a new \"Add GPS Data\" page in the data source manager.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Cargar proyectos desde la GPKG mediante la función de arrastrar y soltar
Históricamente, al utilizar la función de arrastrar y soltar con el formato GPKG, sólo se representaban las capas de objetos espaciales para cargarlas en QGIS.

QGIS mostrará ahora los proyectos incrustados en un GPKG cuando el archivo GPKG se añada al lienzo de QGIS mediante la función de arrastrar y soltar.

![image29](images/entries/3672e8bb8d50bf1593252343da8fd8ff78a46535.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Soporte de Almacenamiento Externo
QGIS now includes an External Storage API, in line with the proposal outlined in [QEP 196](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/196).

La aplicación incluye las siguientes características:
- API de almacenamiento externo
- Registro que contiene todos los backends de almacenamiento externo
- Almacenamiento externo SimpleCopy que almacena el recurso externo seleccionado en una ubicación específica del disco
- Soporte WebDAV

Además, se ha añadido un widget que permite la configuración y visualización de los backends y componentes de almacenamiento externo. El widget de modo de almacenamiento (Archivo o Directorio) no está actualmente visible cuando se selecciona un almacenamiento externo, y los ajustes de la ruta relativa están ocultos ya que las rutas relativas no son relevantes para los datos de almacenamiento externo.

![image30](images/entries/c16663cabec529b113bb73919141bf50bf142c9e.gif)

This feature was funded by [Lille Metropole](https://www.lillemetropole.fr/)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Widgets y Formularios
### Prestación: Arrastrar y soltar las acciones del formulario de diseño
Las acciones de capa están ahora disponibles en los formularios mediante el diseñador de arrastrar y soltar

![image31](images/entries/d8af279071ac38fdc63fbd3980077155db39bd0f.gif)

This feature was funded by [Kanton Solothurn, Amt für Geoinformation](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Leyenda de capa
### Prestación: Utilizar el icono del marcador de posición en la leyenda para las capas rasterizadas
Se ha añadido una nueva función que permite seleccionar una imagen de marcador de posición que puede utilizarse en el elemento de leyenda de una capa raster o vectorial. Esto es muy útil en ciertos casos, como cuando se utilizan capas rasterizadas con el servidor de QGIS, evitando largas listas de valores paletizados de las peticiones GetLegendGraphic y devolviendo en su lugar un resultado adaptado, entre otros varios casos de uso.

![image32](images/entries/f06524b9f422ee1ced55d9d79b816cabc5ea212d.webp)

This feature was funded by [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)

This feature was developed by [mhugent](https://github.com/mhugent)
## Herramientas de análisis
### Prestación: Añadir la función if() a la calculadora de trama
Una prestación largamente esperada ha sido que QGIS soporte simples declaraciones if() en la calculadora de raster.

Aunque las sentencias condicionales han sido admitidas en la calculadora de tramas durante un tiempo, la sintaxis y la estructura de las expresiones eran a menudo verbosa y compleja.

The raster calculator will now support simple conditional statements with the common syntax of `if ( condition , option1 , option2 )` whereby if the condition evaluates to true, the first option will be used, otherwise the second option will be used.

![image33](images/entries/c5d6968380879133ddb31ab2d0f755d6d2048402.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
### Prestación: Soporte de ráster virtual en la calculadora de ráster
Se ha añadido soporte para el proveedor de datos ráster virtual a la calculadora ráster de QGIS, que ahora permite a los usuarios realizar operaciones de calculadora ráster sin especificar un archivo de salida o escribir el ráster resultante en el disco.

This option is enabled via the UI by checking the \"Create on-the-fly raster instead of writing layer to disk\" checkbox in the raster calculator, and is also supported via the PyQgis API.

Las capas ráster resultantes pueden utilizarse en otras operaciones de análisis y permiten nombres de ráster especificados por el usuario. Si no se proporciona un nombre para el ráster resultante, se nombrará según la fórmula utilizada para generarlo.

![image34](images/entries/844b2b463a26d035fe25d43d7221a24a570ac615.gif)

This feature was developed by [Francesco Bursi](https://github.com/Franc-Brs)
## Procesado
### Prestación: Tipo de parámetro de la capa de anotación para el tratamiento
Se ha añadido un tipo de parámetro de capa de anotación al marco de procesamiento de QGIS, que incluye un nuevo algoritmo para convertir los elementos de la capa de anotación principal en capas de anotación secundarias. Esto es útil para mover elementos creados en la capa principal a una capa secundaria, de modo que la colocación del elemento pueda ajustarse dentro de la pila de capas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir una opción POST al algoritmo de procesamiento de FileDownloader
Añade la posibilidad de elegir entre realizar peticiones GET o POST al descargar un archivo mediante la herramienta de procesamiento FileDownloader.

Si se especifica el parámetro POST, se pueden añadir algunos DATOS en la consulta.

Esto es útil en muchos contextos, como para enviar solicitudes más largas a la API de Overpass usando POST para descargar datos de OSM.

![image35](images/entries/89bee20177cb03e453300ae291ae879649e963ab.webp)

This feature was funded by [3Liz](https://www.3liz.com)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Feature: Add new \"Select within distance\" and \"Extract within distance\" algorithms
Se han proporcionado nuevos algoritmos que permiten a los usuarios seleccionar o extraer características de una capa que están dentro de una determinada distancia de objetos espaciales de otra capa de referencia.

La comprobación de la distancia está muy optimizada, ya que utiliza índices espaciales para restringir el número de objetos espaciales recuperados, y también gestiona automáticamente la comprobación en el servidor de base de datos para las capas que utilizan el proveedor PostGIS.

Además, el parámetro de distancia puede ser una propiedad definida por los datos.

Esta prestación fue financiada por QTIBIA Engineering

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Parámetro de la nube de puntos para el procesamiento
Se ha añadido un nuevo parámetro de nube de puntos al Marco de Procesamiento de QGIS. Esto permite filtrar las capas de nubes de puntos en la capa de mapa y los parámetros de capas múltiples. Esto abre la puerta a los algoritmos nativos de nubes de puntos y mejora el soporte de nubes de puntos para los proveedores de terceros.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Eliminar el complemento de importación de GPS
La última funcionalidad de las herramientas GPS se ha trasladado a tres nuevos algoritmos de procesamiento, a saber
- Convertir datos GPS
- Cargar datos GPS a dispositivo
- Descargar datos GPS de dispositivo

Como resultado, el complemento de importación de GPS se ha vuelto redundante y se ha eliminado completamente de QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Convertir el algoritmo de procesamiento del tipo de objeto espacial GPX
La herramienta Convertir tipo de objeto espacial GPX se ha portado desde las herramientas GPS a un nuevo algoritmo de procesamiento, que utiliza la herramienta GPSBabel para convertir las características GPX de un tipo a otro (por ejemplo, convertir todas las características de punto de vía a un objeto espacial de ruta).

Está diseñado como un sustituto de los flujos de trabajo que anteriormente utilizaban esta funcionalidad del plugin de herramientas GPS, pero con todas las ventajas y mejoras que se derivan automáticamente de formar parte del Marco de Procesamiento de QGIS.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Añadir campo incremental con opción de módulo
Este algoritmo permite al usuario añadir una columna con un número entero que se incrementará desde START hasta el límite, con la posibilidad de agrupar para reanudar en el valor de START después del grupo.

An option called \"modulo counter\" is included which will reset the counter to the starting value if the modulo value is reached. Using a value of 0 for the modulo option will disable it.

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Prestación: Parámetro de duración
Se ha añadido un nuevo parámetro de duración al marco de procesamiento para facilitar la creación de algoritmos relacionados con el tiempo.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Algoritmo de agrupación espaciotemporal ST-DBSCAN
QGIS 3.22 incluye un nuevo algoritmo de agrupación espaciotemporal ST-DBSCAN que agrupa las características de los puntos basándose en una implementación 2D del algoritmo de agrupación espaciotemporal basada en la densidad de las aplicaciones con ruido (ST-DBSCAN).

Para más detalles, consulte los siguientes documentos:
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu, \"A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise\". In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
- Birant, Derya, and Alp Kut. \"ST-DBSCAN: An algorithm for clustering spatial--temporal data.\" Data & Knowledge Engineering 60.1 (2007): 208-221.
- Peca, I., Fuchs, G., Vrotsou, K., Andrienko, N. V., & Andrienko, G. L. (2012). Scalable Cluster Analysis of Spatial Events. In EuroVA@ EuroVis.

![image36](images/entries/10136b7563df169c40e2c20a96fe75b6ed93e16f.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Trasladar los proveedores de procesamiento no nativos a complementos independientes
In line with the discussion in [QEP 226](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/226), the SAGA, GRASS, and OTB providers have been separated into independent plugins.

Esto debería evitar problemas con la carga del complemento de Procesos en los casos en que alguno de estos proveedores esté roto. También facilitará su conversión en complementos de terceros en el futuro.

Los complementos SAGA y GRASS están habilitados por defecto, dejando la UX sin cambios. El proveedor OTB puede ser habilitado en el Administrador de Complemento si es necesario, sin embargo, la habilitación o deshabilitación de cualquiera de estos proveedores se realiza ahora a través del Administrador de Complemento como con cualquier otro complemento.

Se trata de un cambio principalmente interno, siendo el único cambio visible por parte de los usuarios finales el hecho de que el Administrador de Complementos se utiliza para activar o desactivar los proveedores SAGA, GRASS y OTB.

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Opciones de Aplicación y Proyecto
### Prestación: Exportar todos los atajos de teclado a XML o PDF
Históricamente, al exportar los atajos de teclado a un archivo XML, QGIS sólo exportaba los atajos definidos por el usuario. En los casos en los que no se encontraban atajos personalizados, se creaba un archivo vacío.

Se ha proporcionado una nueva opción para exportar todos los atajos de teclado disponibles al archivo XML resultante, o para generar una salida en PDF con una lista de todos los atajos QGIS definidos.

![image37](images/entries/1822a5ace82d1e8030ed3d563c07f6b9b6fc3901.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
### Prestación: Mover el widget de configuración del dispositivo GPS Tools GPSbabel a la configuración global
Los ajustes de configuración de GPS babel se han trasladado de una página de ajustes en el obsoleto plugin GPS Tools, a una nueva página en el diálogo principal de ajustes.

![image38](images/entries/d61c12a455d85b290431d5ff461de15db0afb446.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Establecer la estructura de la ruta por defecto para los nuevos proyectos
Históricamente, QGIS Desktop permitía definir si un determinado proyecto utilizaba una estructura absoluta o relativa desde las propiedades del proyecto, sin embargo, la configuración por defecto de esta funcionalidad siempre estaba configurada para utilizar rutas relativas.

Se ha expuesto una nueva configuración que permite a los usuarios establecer la estructura de la ruta por defecto para utilizarla de forma absoluta o relativa para los nuevos proyectos en las opciones del programa. De la misma manera que el formato de proyecto por defecto puede ser configurado para usar qgz o qgs, esto está disponible como una propiedad global específica para cada perfil de usuario.

This feature was developed by [mhugent](https://github.com/mhugent)
### Prestación: Permitir la configuración del tamaño máximo de la caché desde la configuración de QGIS
In the `qgis_global_settings.ini` file, it\'s possible to set the max image cache size in bytes.

La caché se utiliza para almacenar en caché la simbología y las imágenes de diseño. Si se utilizan imágenes de alta resolución para la impresión del diseño, este valor debe aumentarse en consecuencia.

El valor predeterminado es 100mb.

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [David Marteau](https://github.com/dmarteau)
## Navegador
### Prestación: Mejora de la acción de eliminación de los archivos del navegador
La acción de eliminar utilizada desde el navegador QGIS se ha mejorado en varios aspectos, entre ellos:
- La acción es más coherente y se aplica a todos los elementos del tipo de archivo
- Ahora se puede eliminar varios archivos seleccionando varios elementos de archivo en el navegador, lo que incluye un mensaje de confirmación.
- Antes de borrar los archivos, se analiza el proyecto actual para ver si está utilizando alguno de los archivos. Si es así, se muestra un aviso preguntando a los usuarios si quieren cancelar el borrado, o borrar y eliminar capas, o borrar y conservar capas.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Widget de resultados de la API de conexiones
As a part of the ongoing efforts to port the table management functionalities from the DB Manager to the QGIS Browser, as detailed in [QEP 205](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/205), a new SQL dialog is available from the browser panel which provides the ability to execute queries and SQL statements for the following elements:
- Conexiones BD
- Elementos de esquema
- Elementos de tabla

La aplicación también admite las siguientes funcionalidades avanzadas:
- Una implementación multihilo tanto para la obtención de tokens de la API como para la obtención de filas da lugar a operaciones de la interfaz gráfica de usuario que no se bloquean
- API totalmente interrumpible
- Soporte para la carga progresiva de objetos espaciales en la vista de resultados (API fetchMore)

![image39](images/entries/a4d260146fe4267a34d9db97495df2b244f5d7ff.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Proveedores de datos
### Prestación: Transacciones en el proveedor MSSQL
Se ha añadido el soporte de transacciones al proveedor de datos MSSQL.

There are no GUI-related changes, as users can enable transactional editing as with other providers. This is done by going to the Project Properties and checking \"Automatically create transaction groups where possible\" in the Data Sources tab.

Por defecto, una transacción en ejecución en MSSQL bloqueará a otros clientes para que no puedan acceder a los mismos datos. Por ejemplo, si un cliente inicia una transacción y añade o modifica una función en una tabla, los demás clientes se bloquearán al intentar leer cualquier dato de la tabla hasta que se complete la transacción.

There is database-level configuration option, `READ_COMMITTED_SNAPSHOT`, which is `OFF` by default.

Activando esto se cambiará el comportamiento para que funcione de forma similar a otros sistemas SGBDR como PostgreSQL, en el sentido de que las transacciones no provocan bloqueos y permite que la base de datos soporte múltiples versiones de datos. Esta es una propiedad a nivel de base de datos configurada por el administrador y no puede ser establecida automáticamente por QGIS al conectarse a la base de datos, sin embargo puede ser activada usando la siguiente consulta:
``` sql
ALTER DATABASE my_db SET READ_COMMITTED_SNAPSHOT ON
```
En la mayoría de los casos en los que se desea realizar transacciones, es probable que se recomiende activar esta opción para evitar la congelación en QGIS u otros clientes.

This feature was funded by [ms.GIS](http://www.msgis.com)

This feature was developed by [Lutra Consulting (Martin Dobias)](https://www.lutraconsulting.co.uk/)
### Prestación: Mostrar el sistema y las tablas internas en la selección de subcapas
Se ha añadido una casilla de verificación al diálogo de selección de subcapas para controlar si se deben mostrar las tablas del sistema y las internas. Esto estará desactivado por defecto, pero será útil en los casos en que los usuarios tengan una necesidad particular de cargar una tabla del sistema en QGIS para su visualización o manipulación.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Leer y convertir automáticamente los metadatos de las bases de datos personales de ESRI
Anteriormente esto era compatible con las geodatabases de archivos y los metadatos shp.xml, pero ahora también es compatible con las geodatabases personales de ESRI (archivos .mdb)

Requiere GDAL 3.4+

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Crear un proveedor de elementos de datos genérico para todas las fuentes de datos basadas en archivos
Este proveedor utiliza la API QgsProviderRegistry::querySublayers para crear automáticamente los elementos de datos del navegador adecuados para todas las fuentes basadas en archivos, independientemente del proveedor subyacente, ya sea mdal, gdal, ogr, pdal o ept.

Esto permite fusionar fuentes que pueden ser manejadas por múltiples proveedores diferentes en elementos contenedores únicos en el navegador, que pueden expandirse para mostrar todos los elementos relacionados o anidados. Es habitual que muchos tipos de archivos, como los archivos GeoPDF o KML/KMZ, puedan contener capas raster y vectoriales, o archivos .nc a los que se puede acceder como malla o raster dependiendo del proveedor de datos.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Servidor de QGIS
### Prestación: Habilitar múltiples MetadataUrls
Históricamente, QGIS Server sólo admitía la provisión de una única URL de metadatos, pero ahora permitirá que se especifiquen múltiples puntos finales de metadatos en la definición del servicio.

![image40](images/entries/8e644bb4823b8da291e1e2b2dd1ca472d3d57246.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
### Prestación: Añadir versión a las herramientas CLI de QGIS Server
It\'s quite a common practice to have arguments like `-v` and `--version` for tools accessed via command line interfaces (CLIs), so new `--version` and it\'s alias `-v` have been added to identify QGIS version information for the following tools:
- qgis_process
- qgis_mapserv.fcgi
- qgis_mapserver

This feature was funded by [3Liz](https://www.3liz.com/)

This feature was developed by [Étienne Trimaille](https://github.com/Gustry)
## Programabilidad
### Prestación: Exponer el codificador de teselas vectoriales que se puede programar
An additional `writeSingleTile` method in `QgsVectorTileWriter` has been exposed to enable the encoding of a single vector tile to a memory buffer. This may support workflows for PyQgis and QGIS Server which include support for vector tiles.

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Prestación: Codificar y escribir mosaicos vectoriales en un SRC diferente al EPSG:3857
La API de QGIS ha sido ampliada para soportar la codificación y escritura de mosaicos vectoriales en un SRC diferente al EPSG:3857.

Tenga en cuenta que según la especificación de Mapbox Vector Tile, un Vector Tile representa datos basados en una extensión cuadrada dentro de una proyección. Un mosaico vectorial debe contener información sobre sus límites y su proyección. El formato de archivo asume que el decodificador conoce los límites y la proyección de un Vector Tile antes de decodificarlo.

Esta prestación fue fundada por Ifremer

This feature was developed by [rldhont](https://github.com/rldhont)
### Prestación: Filtro DistanceWithin para QgsFeatureRequest
Se ha añadido una opción a QgsFeatureRequest para solicitar objetos espaciales dentro de una determinada distancia de una geometría de referencia

Esto es posible gracias al nuevo enum Qgis::SpatialFilterType que se ha añadido para reflejar si una petición no utiliza ningún filtro espacial, un filtro BoundingBox (a través de setFilterRect), o el nuevo filtro DistanceWithin.

Por ejemplo, la siguiente solicitud recuperará todas las características en un radio de 50 unidades de mapa de la cadena de líneas proporcionada:
``` python
QgsFeatureRequest().setDistanceWithin(QgsGeometry.fromWkt('LineString(0 0, 10 0, 12 1)'), 50)
```
Los filtros de distancia interior se tratan como los filtros de caja delimitadora, en el sentido de que son independientes de cualquier filtro de atributos/identificación (como los identificadores de características o las expresiones).

Provider feature iterators can potentially delegate the distance within search to the backend. So, for example, the PostgreSQL data provider could use an `ST_DWithin` query for optimal index use.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: API para valores preestablecidos de combobox
Se ha añadido una API para permitir que un parámetro de cadena se muestre como un cuadro combinado con opciones preestablecidas en las herramientas de la GUI de procesamiento.

In some circumstances, it is desirable to restrict the values available when a user is asked to enter a string parameter that should match a list of predetermined \"valid\" values, yet these values will vary installation by installation.

For example, a \"printer name\" parameter, where it may be desired that users may pick a name value from a list of printers installed on the system, but since the printer names will vary between installations, an enum parameter is not a suitable choice.

This is now supported by setting the \"value_hints\" option in the widget wrapper metadata, as demonstrated below.

Aunque esto proporciona un mecanismo para guiar a los usuarios a seleccionar entre valores de cadena válidos cuando se ejecuta un algoritmo de Procesamiento a través de la GUI, no pone ningún límite a los valores de cadena aceptados a través de los códigos de PyQGIS o cuando se ejecuta el algoritmo a través de otros medios que no utilizan la GUI. Los algoritmos deben manejar con gracia otros valores en consecuencia.
``` python
param = QgsProcessingParameterString( 'PRINTER_NAME', 'Printer name')
# show only printers which are available on the current system as options
# for the string input.
param.setMetadata( {'widget_wrapper': { 'value_hints': ['Inkjet printer', 'Laser printer'] } })
```
This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Soporte de la clase QgsExifTools para obtener los valores de las etiquetas
La clase QgsExifTools puede ahora recuperar etiquetas exif individuales de las imágenes utilizando la función readTag.

E.g.: `QgsExifTools.readTag('/my/photo/0997.JPG'), 'Exif.Image.DateTime')`

Las etiquetas exif conocidas que representan valores de tiempo se convierten automáticamente en objetos Q{Date,Time,DateTime}. Esto hace que trabajar con esas etiquetas sea mucho más fácil y se integra bien con otras partes de la API de QGIS.

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Correcciones Notables
### Error corregido por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Problema de parseo WFS / GML, pero QGIS carga GML como archivo sin problemas? | [#45017](https://github.com/qgis/QGIS/issues/45017) | No es un error |  |  |
| La solicitud POST para modificar la marca de tiempo no respeta el formato definido | [#44990](https://github.com/qgis/QGIS/issues/44990) | No se corrige / no es un error |  |  |
| Warning message \'Cannot create temporary SpatiaLite cache\' when adding many WFS-layers | [#44971](https://github.com/qgis/QGIS/issues/44971) | Duplicado |  |  |
| QGIS crea un filtro no válido para la petición WFS GetFeature | [#43957](https://github.com/qgis/QGIS/issues/43957) | [PR #45043](https://github.com/qgis/QGIS/pull/45043) | [PR #45053](https://github.com/qgis/QGIS/pull/45053) |  |
| WFS Layer is not rendered when requested CRS is not matching project CRS and \"Only request features overlapping the view extent\" option is set | [#44054](https://github.com/qgis/QGIS/issues/44054) | [PR #45044](https://github.com/qgis/QGIS/pull/45044) | [PR #45047](https://github.com/qgis/QGIS/pull/45047) |  |
| Añadir una capa WFS con un filtro para un atributo inexistente conduce a una capa rota | [#43950](https://github.com/qgis/QGIS/issues/43950) | [PR #45045](https://github.com/qgis/QGIS/pull/45045) | [PR #45052](https://github.com/qgis/QGIS/pull/45052) |  |
| La nueva capa de archivo shape sobrescribe silenciosamente los archivos existentes | [#44299](https://github.com/qgis/QGIS/issues/44299) | [PR #45207](https://github.com/qgis/QGIS/pull/45207) | [PR #45240](https://github.com/qgis/QGIS/pull/45240) |  |
| QGIS en linux se bloquea al abrir muchos geopackages a la vez | [#43620](https://github.com/qgis/QGIS/issues/43620) | [PR #45211](https://github.com/qgis/QGIS/pull/45211) | No |  |
| Fallo en QgsPointCloudLayerRenderer al cerrar mientras el renderizado sigue activo | [#44144](https://github.com/qgis/QGIS/issues/44144) | [PR #45227](https://github.com/qgis/QGIS/pull/45227) | [PR #45241](https://github.com/qgis/QGIS/pull/45241) |  |
| Las herramientas de geoprocesamiento hacen que libgeos lance SIGBUS | [#45226](https://github.com/qgis/QGIS/issues/45226) | [geos PR 481](https://github.com/libgeos/geos/pull/481) | N/D |  |
| QGIS se bloquea después de cargar la capa WMS a través de un script y de acercarse y alejarse. | [#44095](https://github.com/qgis/QGIS/issues/44095) | [PR #45254](https://github.com/qgis/QGIS/pull/45254) | No | Principalmente es una cuestión de uso |
| Entero inesperadamente grande en GeoPackage | [#45178](https://github.com/qgis/QGIS/issues/45178) | No es un error |  |  |
| Atributos - Botón Actualizar Todo - Crea Campos Corruptos - Archivo GeoJSON | [#45139](https://github.com/qgis/QGIS/issues/45139) | [GDAL PR 4552](https://github.com/OSGeo/gdal/pull/4552) | N/D |  |
| WFS connection manager: GetCapabilities document\'s URLs not being used consistently | [#45242](https://github.com/qgis/QGIS/issues/45242) | [PR #45267](https://github.com/qgis/QGIS/pull/45267) | [PR #45273](https://github.com/qgis/QGIS/pull/45273) |  |
| QGIS se bloquea si se pierde la conexión a la red y se carga una capa rasterizada | [#45293](https://github.com/qgis/QGIS/issues/45293) | [GDAL PR 4560](https://github.com/OSGeo/gdal/pull/4560) | N/D |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Errores corregido por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Administrador de fuentes de datos - Servidor REST de ArcGIS - el diálogo/ventana se cierra al añadir una capa | [#45050](https://github.com/qgis/QGIS/issues/45050) | [PR #45059](https://github.com/qgis/QGIS/pull/45059) | n/d |  |
| \"Display no data value as\" option is not available in raster layer properties | [#44949](https://github.com/qgis/QGIS/issues/44949) | [PR #45063](https://github.com/qgis/QGIS/pull/45063) | No crítica |  |
| La capa rasterizada no se representa después de un cambio en la fuente de datos cuando se combina con cierto elemento de diseño | [#44929](https://github.com/qgis/QGIS/issues/44929) | [PR #45074](https://github.com/qgis/QGIS/pull/45074) | [PR #45083](https://github.com/qgis/QGIS/pull/45083) |  |
| Actualizar los identificadores de los objetos espaciales seleccionados antes de emitir featuresDeleted | [#44921](https://github.com/qgis/QGIS/issues/44921) | [PR #45078](https://github.com/qgis/QGIS/pull/45078) | No crítica |  |
| sample() and identify() from QgsRasterDataProvider don\'t always provide the same value | [#44902](https://github.com/qgis/QGIS/issues/44902) | [PR #45086](https://github.com/qgis/QGIS/pull/45086) | [PR #45145](https://github.com/qgis/QGIS/pull/45145) |  |
| Copiar objetos que contienen cadenas multilíneas en otro proyecto no funciona correctamente | [#44989](https://github.com/qgis/QGIS/issues/44989) | [PR #45129](https://github.com/qgis/QGIS/pull/45129) | No crítica |  |
| la proyección de coordenadas de etiquetas para la geometría multipunto hace que QGIS se caiga | [#45148](https://github.com/qgis/QGIS/issues/45148) | [PR #45150](https://github.com/qgis/QGIS/pull/45150) | No |  |
| Copy/paste style category \"Form\" is missing some settings | [#45146](https://github.com/qgis/QGIS/issues/45146) | Maybe won\'t fix, checking with m-kuhn and 3nids |  |  |
| Añadir un nuevo punto en una capa multipunto de memoria mata a QGIS | [#45152](https://github.com/qgis/QGIS/issues/45152) | [PR #45157](https://github.com/qgis/QGIS/pull/45157) |  |  |
| Atributos - Botón Actualizar Todo - Crea Campos Corruptos - Archivo GeoJSON | [#45139](https://github.com/qgis/QGIS/issues/45139) | [PR #45174](https://github.com/qgis/QGIS/pull/45174) | No |  |
| WMS parent layer added via QGIS Browser doesn\'t use default style | [#45192](https://github.com/qgis/QGIS/issues/45192) | [PR #45209](https://github.com/qgis/QGIS/pull/45209) | No |  |
| \"Display nodata as\" color widget is not automatically updated in layer styling panel | [#45132](https://github.com/qgis/QGIS/issues/45132) | [PR #45264](https://github.com/qgis/QGIS/pull/45264) | n/d |  |
| PostGIS error while changing attributes (field value and geometry): prepared statement \"updatefeature\" already exists | [#45100](https://github.com/qgis/QGIS/issues/45100) | [PR #45266](https://github.com/qgis/QGIS/pull/45266) | en cola |  |
| Attribute Table in Layout Manager Font Style Override Doesn\'t Show Fields | [#45098](https://github.com/qgis/QGIS/issues/45098) | [PR #45269](https://github.com/qgis/QGIS/pull/45269) | en cola |  |
| La capa WFS de QGIS Server no se muestra debido a un problema con el orden de los ejes de coordenadas | [#45216](https://github.com/qgis/QGIS/issues/45216) | [PR #45270](https://github.com/qgis/QGIS/pull/45270) | No crítica |  |
| No se representa con la trama de transformación de identidad creada con rasterio | [#45324](https://github.com/qgis/QGIS/issues/45324) | Comprobado, probablemente no sea un error |  |  |
| La consulta SQL del DB Manager se ejecuta dos veces | [#45318](https://github.com/qgis/QGIS/issues/45318) | [PR #45351](https://github.com/qgis/QGIS/pull/45351) | en cola |  |
| can\'t use layers where name starts with number in virtual layer | [#45347](https://github.com/qgis/QGIS/issues/45347) | [PR #45354](https://github.com/qgis/QGIS/pull/45354) | en cola |  |
| Mostrar el recuento de características cuenta nula en la categoría cero | [#45280](https://github.com/qgis/QGIS/issues/45280) | [PR #45361](https://github.com/qgis/QGIS/pull/45361) | en cola |  |
| Copying table by Drag&Drop in Browser (2) doesn\'t copy the table structure correctly | [#45286](https://github.com/qgis/QGIS/issues/45286) | [PR #45375](https://github.com/qgis/QGIS/pull/45375) | No |  |
| Gráfico de histograma erróneo si el tipo de datos raster es byte | [#45379](https://github.com/qgis/QGIS/issues/45379) | [PR #45400](https://github.com/qgis/QGIS/pull/45400) | en cola |  |
| Inconsistencia en el manejo de patrones para QgsServerOgcApiHandler | [#45439](https://github.com/qgis/QGIS/issues/45439) | [PR #45450](https://github.com/qgis/QGIS/pull/45450) | en cola |  |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | [PR #45521](https://github.com/qgis/QGIS/pull/45521) | en cola |  |
| La clave projectsInDatabase no se almacena en xml para las conexiones PostGIS | [#45508](https://github.com/qgis/QGIS/issues/45508) | [PR #45523](https://github.com/qgis/QGIS/pull/45523) | en cola |  |
| Changing values in Form mode of attribute table doesn\'t set active the Save button | [#45527](https://github.com/qgis/QGIS/issues/45527) | [PR #45532](https://github.com/qgis/QGIS/pull/45532) | en cola |  |
| Crear disparador spatialite con DBManager no funciona | [#45420](https://github.com/qgis/QGIS/issues/45420) | [PR #45553](https://github.com/qgis/QGIS/pull/45553) | No |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Error corregido por Peter Petrik
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| QGIS 3.20 en Mac se bloquea cuando se emiten ciertas señales de Qt | [#44182](https://github.com/qgis/QGIS/issues/44182) | [QGIS-Mac-Packager Commit bf925f311](https://github.com/qgis/QGIS-Mac-Packager/commit/bf925f3118a5d51080dfed46dddcb7cba3bbbc00) | n/d |  |
| No se pueden visualizar archivos LAS escritos en coordenadas WGS84 (EPSG:4326) | [#44755](https://github.com/qgis/QGIS/issues/44755) | duplicate of [#41765](https://github.com/qgis/QGIS/issues/41765) |  |  |
| macOS: Symbol not found: \_\_cg_jpeg_resync_to_restart when reprojecting raster layer with GDAL warp on macOS | [#40164](https://github.com/qgis/QGIS/issues/40164) | no | no | Ya no es un problema con la versión nocturna (qgis-deps-0.9) |
| El Gestor de Fuentes de Datos identifica incorrectamente la extensión ráster de PostGIS en macOS | [#43042](https://github.com/qgis/QGIS/issues/43042) | [PR #45322](https://github.com/qgis/QGIS/pull/45322) | en cola |  |
| iconos no visibles en las Notas de Capa | [#44425](https://github.com/qgis/QGIS/issues/44425) | [PR #45332](https://github.com/qgis/QGIS/pull/45332) | n/d |  |
| no se puede abrir ningún archivo ascii FLO-2D en Capa Malla | no reportado | [PR #45349](https://github.com/qgis/QGIS/pull/45349) | n/d |  |
| problema de codificación al utilizar la herramienta de procesamiento GRASS en macOS | [#41870](https://github.com/qgis/QGIS/issues/41870) | [PR #45399](https://github.com/qgis/QGIS/pull/45399) | No es crítico - existe una solución |  |
| Las importaciones del backend QT de Matplotlib no funcionan en MacOS | [#45398](https://github.com/qgis/QGIS/issues/45398) | investigación |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Correcciones de error por Sandro Santilli
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Haz que QgsGeos::prepareGeometry y QgsGeos::cacheGeos sean idempotent | no reportado | [PR #45147](https://github.com/qgis/QGIS/pull/45147) |  |  |
| Añadir un método distanceWithin a la clase virtual QgsGeometryEngine | no reportado | [PR #45057](https://github.com/qgis/QGIS/pull/45057) |  |  |
| Allow calling testdata_pg.sh from any directory | no reportado | [PR #45378](https://github.com/qgis/QGIS/pull/45378) |  |  |
| Hacer TestPyQgsPostgresProvider.testGeneratedColumns idempotent | no reportado | [PR #45415](https://github.com/qgis/QGIS/pull/45415) |  |  |
| Mejorar la documentación y el script de configuración de la base de datos de prueba de PostgreSQL | no reportado | [PR #45413](https://github.com/qgis/QGIS/pull/45413) |  |  |
| Añadir GEOS DistanceWithin API | [GEOS Ticket #1124](https://trac.osgeo.org/geos/ticket/1124) | [GEOS commit #ba10ba4508a](https://trac.osgeo.org/geos/changeset/ba10ba4508af887a1a78bbc632ab45d89ce3242c/git) | [GEOS Issue #472](https://github.com/libgeos/geos/issues/472) |  |
| Hacer que la prueba del proveedor de Postgres sea idempotent | [#45417](https://github.com/qgis/QGIS/issues/45417) | [PR #45418](https://github.com/qgis/QGIS/pull/45418) |  |  |
| Utilice GEOSDistanceWithin cuando esté disponible | no reportado | [PR #45340](https://github.com/qgis/QGIS/pull/45340) |  |  |
| Reducir las conversiones de GEOS y las preparaciones de las geometrías | no reportado | [PR #45195](https://github.com/qgis/QGIS/pull/45195) |  |  |
| Más heurística para determinar si hay que iterar sobre la fuente de destino | no reportado | [PR #45339](https://github.com/qgis/QGIS/pull/45339) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Sandro Santilli](https://strk.kbt.io/)
### Errores corregidos por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Más const en geometría | No se ha informado / rendimiento | [PR #45217](https://github.com/qgis/QGIS/pull/45217) |  |  |
| QgsFeature::setId mejorar la documentación con una advertencia | [#44898](https://github.com/qgis/QGIS/issues/44898) | [PR #45189](https://github.com/qgis/QGIS/pull/45189) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| Comprobación de la Geometría: Ampliar el FeatureID | [#44250](https://github.com/qgis/QGIS/issues/44250) | [PR #45191](https://github.com/qgis/QGIS/pull/45191) | [PR #45229](https://github.com/qgis/QGIS/pull/45229) |  |
| VertexTool. Corrige el movimiento de vértices en la capa Z si los SRC son diferentes (con Vincent Cloarec) | No reportado | [PR #45020](https://github.com/qgis/QGIS/pull/45020) | No se ha retrocedido. Introducir nuevos métodos. |  |
| Corregir el URI de la dimensión Z/M a través del Administrador de BD. | [#34894](https://github.com/qgis/QGIS/issues/34894) | [PR #45223](https://github.com/qgis/QGIS/pull/45223) | [PR #45304](https://github.com/qgis/QGIS/pull/45304) |  |
| \[FIX\] GeometryValidator init curve support | No reportado | [PR #45272](https://github.com/qgis/QGIS/pull/45272) |  |  |
| Compile fails, \'None\' is not a member of \'QgsField::ConfigurationFlags\' | [#44681](https://github.com/qgis/QGIS/issues/44681) | No se corrige / no es un error |  |  |
| La unión falla cuando se usa un punto y una capa de polígono | [#44801](https://github.com/qgis/QGIS/issues/44801) | Diferencia entre GEOS 3.8 y 3.9 |  |  |
| El orden de los anillos en la cadena WKT de MultiPolygon puede dejar partes superpuestas al borrar agujeros (native:deleteholes) | [#44424](https://github.com/qgis/QGIS/issues/44424) | No se corregirá por ahora. Podemos usar Geos para arreglar el problema, pero quitaremos Z/M y segmentizaremos el arco. |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Loïc Bartoletti](https://www.oslandia.com/)
### Error corregido por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Regresión: al intentar ejecutar el algoritmo de conversión de multipartes a monopartes se produce un error de python | [#45331](https://github.com/qgis/QGIS/issues/45331) | [PR #45348](https://github.com/qgis/QGIS/pull/45348) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Denis Rouzaud](https://www.opengis.ch/)
### Error corregido por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Los estilos en la base de datos no funcionan para el proveedor postgres y las capas no geométricas | [#44749](https://github.com/qgis/QGIS/issues/44749) | [PR #45075](https://github.com/qgis/QGIS/pull/45075) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| \"Layer notes\" icon is not displayed when copy-pasting a style | [#44692](https://github.com/qgis/QGIS/issues/44692) | [PR #45302](https://github.com/qgis/QGIS/pull/45302) | no hay necesidad |  |
| Errores JSON ambiguos | [#42832](https://github.com/qgis/QGIS/issues/42832) | No se ha podido reproducir |  |  |
| Tabla de atributos: faltan características al copiar/pegar desde la capa cero | [#42798](https://github.com/qgis/QGIS/issues/42798) | Can't reproduce (Closed) |  |  |
| La vista del formulario muestra imágenes adjuntas erróneas al desplazarse por las funciones | [#42705](https://github.com/qgis/QGIS/issues/42705) | Ya corregida |  |  |
| La herramienta Construir Raster Virtual crea una capa adicional al seleccionar y reordenar las capas | [#44270](https://github.com/qgis/QGIS/issues/44270) | [PR #45092](https://github.com/qgis/QGIS/pull/45092) | [PR #45102](https://github.com/qgis/QGIS/pull/45102) |  |
| Las opciones del widget de adjuntos se restablecen cuando se vuelven a abrir las propiedades del widget de campo | [#45089](https://github.com/qgis/QGIS/issues/45089) | Duplicado |  |  |
| Los atributos de objetos espaciales borrados no actúan como si hubieran sido borrados, e impiden guardar la capa | [#39146](https://github.com/qgis/QGIS/issues/39146) | [PR #45176](https://github.com/qgis/QGIS/pull/45176) | [PR #45292](https://github.com/qgis/QGIS/pull/45292) |  |
| \[Postgres\] default value displayed instead of NULL | [#45198](https://github.com/qgis/QGIS/issues/45198) | [PR #45199](https://github.com/qgis/QGIS/pull/45199) | [PR #45291](https://github.com/qgis/QGIS/pull/45291) |  |
| a feature copy/paste sets a NULL field to its \"default value\" in a geopackage | [#44544](https://github.com/qgis/QGIS/issues/44544) | Pregunta: ¿Evaluamos el valor por defecto del campo NULL al copiar y pegar? |  |  |
| El constructor de expresiones de QGIS no puede resolver correctamente las matrices de texto de PostgreSQL | [#45290](https://github.com/qgis/QGIS/issues/45290) | [PR #45321](https://github.com/qgis/QGIS/pull/45321) |  |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Julien Cabieces](https://www.oslandia.com/)
### Error fijado por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) | Observaciones |
| --- | --- | --- | --- | --- |
| Don\'t reset mesh layer styling when changing data source for layer | [#45391](https://github.com/qgis/QGIS/issues/45391) | [PR #45392](https://github.com/qgis/QGIS/pull/45392) | N/D |  |
| Se ha corregido un fallo al representar objetos espaciales recortados y resultados de formas recortadas | [#45190](https://github.com/qgis/QGIS/issues/45190) | [Commit 6a4cdb36](https://github.com/qgis/QGIS/commit/6a4cdb36c91085c5bb1544fb02da1f83467a29d7) | [PR #45422](https://github.com/qgis/QGIS/pull/45422) |  |
| Se ha corregido un fallo al utilizar las herramientas de etiquetas de mapas con proyectos que contienen capas de azulejos vectoriales. | [#44486](https://github.com/qgis/QGIS/issues/44486) | [PR #45311](https://github.com/qgis/QGIS/pull/45311) | [PR #45390](https://github.com/qgis/QGIS/pull/45390) |  |
| Corregir el tamaño de los símbolos en Metros a Escala no puede ser negativo | [#45298](https://github.com/qgis/QGIS/issues/45298) | [Commit 360351a](https://github.com/qgis/QGIS/commit/360351a02704c370545fb8f92c0bdafbdfa35b2e) | No es adecuado para el backport |  |
| Corregir la sobreescritura del estilo por defecto de las capas del geopackage | [#42811](https://github.com/qgis/QGIS/issues/42811) | [Commit eef6939b96](https://github.com/qgis/QGIS/commit/eef6939b96407b3d050988be4a0eeb692ffc5b68) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Corregir el cuelgue al renderizar líneas con patrones de guiones con todos los valores 0 | [#41994](https://github.com/qgis/QGIS/issues/41994) | [Commit f4e2e900](https://github.com/qgis/QGIS/commit/f4e2e900eed16633ef0198f7b9a9152f395e173a) | [PR #45107](https://github.com/qgis/QGIS/pull/45107) |  |
| Actualizar las ubicaciones de las barras de herramientas por defecto | no reportado | [Commit 77be95feac](https://github.com/qgis/QGIS/commit/77be95feac7391e58f6bd487f30e09ed8ed63651) | N/D |  |
| Don\'t overwrite existing data defined property expressions when an interactive map tool is used to move/rotate/edit labels | [PR #45279](https://github.com/qgis/QGIS/pull/45279) | [Commit b30c17f0](https://github.com/qgis/QGIS/commit/b30c17f07d00850597d8bb1b2cfb1f454498b391) | N/D |  |
| Corregir el fallo al salir con el dock CAD abierto | no reportado | [Commit 1fb21f69f](https://github.com/qgis/QGIS/commit/1fb21f69fede05cabb8f1d27a8ad24564ae16f3d) | N/D |  |
| Fix rule based symbology doesn\'t work for columns with \'-\' in name | [#44379](https://github.com/qgis/QGIS/issues/44379) | [Commit 51fa9840](https://github.com/qgis/QGIS/commit/51fa9840248135a7fe7ee181b7d645f3c591c9cc) | [Commit 797367dde](https://github.com/qgis/QGIS/commit/797367dde65d6ab06f39f5c4636c2127c67aa9d1) |  |
| Evitar los cuelgues al dibujar los iconos de los símbolos utilizando tamaños inapropiados en las unidades del mapa | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45233](https://github.com/qgis/QGIS/pull/45233) | No es adecuado para el backport |  |
| Corregir la visualización inapropiada de los valores z/m en el cad dock cuando se selecciona una capa no z/m | no reportado | [Commit 55a76d1d](https://github.com/qgis/QGIS/commit/55a76d1d867c32f52ae4bd38ed671d44aa3ae92e) | N/D |  |
| Implementar una cancelación más sensible del renderizado de mapas para los mapas que utilizan efectos complejos | [#41149](https://github.com/qgis/QGIS/issues/41149) | [PR #45212](https://github.com/qgis/QGIS/pull/45212) | No es adecuado para el backport |  |
| Permitir el uso del muelle CAD para el SRC geográfico, pero sólo permitir el establecimiento de las restricciones x/y/z/m | no reportado | [PR #45185](https://github.com/qgis/QGIS/pull/45185) | No es adecuado para el backport |  |
| Corregir el fallo al abrir las propiedades de simbología de una capa configurada como renderizador incrustado que no es compatible con los representadores incrustados | [#45159](https://github.com/qgis/QGIS/issues/45159) | [PR #45193](https://github.com/qgis/QGIS/pull/45193) | N/D |  |
| Corregir las coordenadas de QgsMapToolCapture cuando se asocia con una capa no vectorial donde el CRS de la capa != CRS del lienzo | no reportado | [PR #45183](https://github.com/qgis/QGIS/pull/45183) | N/D |  |
| Corregir el representado del generador de geometría fuera de las capas vectoriales | [#39159](https://github.com/qgis/QGIS/issues/39159) | [PR #45165](https://github.com/qgis/QGIS/pull/45165) | No es adecuado para el backport |  |
| Corregir la personalización del color se pierde al configurar los representadores utilizando generadores de geometría | [#38377](https://github.com/qgis/QGIS/issues/38377) | [PR #45166](https://github.com/qgis/QGIS/pull/45166) | No es adecuado para el backport |  |
| Corregir la representación de la capa de símbolos de líneas interpoladas fuera de las capas vectoriales | [#45028](https://github.com/qgis/QGIS/issues/45028) | [PR #45164](https://github.com/qgis/QGIS/pull/45164) | N/D |  |
| Corregir la documentación de QgsGeometry.fromPolygonXY | [#45099](https://github.com/qgis/QGIS/issues/45099) | [Commit 3d599fe4](https://github.com/qgis/QGIS/commit/3d599fe4b5574e7c916133171e097163cae51e32) | N/D |  |
| Corregir la digitalización de rasgos usando el dock CAD cuando el CRS de la capa != el CRS del lienzo | no reportado | [PR #45108](https://github.com/qgis/QGIS/pull/45108) | N/D |  |
| Corregir el desplazamiento del fondo al dibujar un texto girado | [#44907](https://github.com/qgis/QGIS/issues/44907) | [PR #45425](https://github.com/qgis/QGIS/pull/45425) | pendiente |  |
| Escapar correctamente las cadenas de origen complejas en el registro del historial de procesamiento | [#45403](https://github.com/qgis/QGIS/issues/45403) | [PR #45426](https://github.com/qgis/QGIS/pull/45426) | pendiente |  |
| Corregir el manejo de los archivos ADF en el navegador | no reportado | [PR #45393](https://github.com/qgis/QGIS/pull/45393) | No es adecuado para el backport |  |

These bug fixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
