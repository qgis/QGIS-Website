---
HasBanner: false
draft: false
releaseDate: '2018-10-26'
section: proyecto
sidebar: true
title: Changelog for QGIS 3.4
type: visual-changelog

---
{{<content-start >}}
# Changelog for QGIS 3.4{#changelog34 }
![image0](images/entries/splash34vs.webp)

Fecha de lanzamiento: 2018-10-26

The first long-term release (LTR) of QGIS 3. QGIS 3.4 just released. After five consolidation point releases (3.4.5) it will replace the previous LTR in the package repositories in February 2019 (see [release schedule]({{< ref "resources/roadmap#release-schedule" >}})). This is a giant leap forward for the project - our first Long Term Release based on the 3.x platform. For users moving over from the 2.18 LTR there is a huge list of new features and impactful changes in this new LTR version. Please bear in mind that 3.x plugins are incompatible with 2.x plugins so review your plugin usage carefully - and if possible help to migrate old plugins to the new platform. If you have not already done so, take a look at the changelogs from [Version 3.0](../visualchangelog30) and [Version 3.2](../visualchangelog32) to understand the full scope of changes in the 3.4 release.

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current supporters is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

![image1](images/projects/750d7d9b7e9dbd498202c4b1288a0cbceb1cd65b.png)

{{<table-of-contents >}}
## General
### Prestación: Flatpak
QGIS is now available as a flatpak application on [flathub](https://flathub.org/apps/search/qgis) Flatpak (formerly xdg-app) is a software utility for software deployment, package management, and application virtualization for Linux desktop computers. It allows users to install different QGIS versions on linux without having to recompile or use Docker. It is a full package with all libraries included, and it uses its own user profile locations. So you\'ll need some disk space and new habits working with flatpak, but it rocks!

[![image28](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)](images/entries/48295bdab734a17ef03ea6bacf182708618e0980.webp)

This feature was funded by [Aleix Pol](https://github.com/aleixpol)

This feature was developed by [Aleix Pol](https://github.com/aleixpol)
### Prestación: Archivos SVG pueden ser embebidos en proyectos y símbolos
Permite imágenes SVG para simbología, etiquetas, etc para ser directamente embebidas en un archivo de proyecto (o estilo QML, o plantilla impresa QPT!) mediante codificación del SVG como una cadena estádar base64.

Adicionálmente, archivos embebidos pueden ser extraidos de proyectos y símbolos y grabados de nuevo a archivos SVG basada en disco.

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Prestación: aceleración basada en OpenCL
This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Alessandro Pasotti](https://qgis.org)
## Expresiones
### Prestación: Nuevas funciones de expresión y variables
Muchas nuevas funciones de expresión han sido añadidas en QGIS 3.4. Estas incluyen muchas funciones manejables con las que trabajar y manipular matrices y objetos de mapa(diccionario).
- **json_to_map**: Converts a JSON encoded string value to a map (dictionary) type object
- **map_to_json**: Converts a map (dictionary) type object to a JSON encoded string value
- **hstore_to_map**: Converts a hstore value to a map (dictionary) type object
- **map_to_hstore**: Converts a map (dictionary) type object to a hstore value
- **array_foreach** : Loops over an array and executes an expression on each item in the array, returning a new array containing each calculated value
- **array_filter** : Filters an array according to an expression
- **raster_value**: Returns a value sampled from a raster layer at a specified point
- **to_dms**: Converts a numeric value to a Degrees, Minutes, Seconds formatted string
- **to_dm**: Converts a numeric value to a Degrees, Minutes formatted string
- **line_substring**: Returns the portion of a line (or curve) geometry which falls between the specified start and end distances (measured from the beginning of the line). Z and M values are linearly interpolated from existing values.
- **generate_series(start,stop,step)**: Creates an array containing a sequence of numbers.

Además, algunas nuevas variables también se han puesto a disposición para su uso dentro de las expresiones QGIS:
- **\@canvas_cursor_point**: Contains a point value representing the current position of the mouse cursor within the main map canvas
- **\@map_layers**: Contains an array of all layers which are visible within the map
- **\@map_layer_ids**: Contains an array of all layer IDs for layers visible within the map

[![image2](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)](images/entries/ced45b9dd1f58c80aef504344f515a28e33e9e4a.webp)

This feature was developed by [Etienne Trimaille, Matteo Ghetta, Matthias Kuhn, Mathieu Pellerin, Nyall Dawson](https://qgis.org)
### Prestación: Autocompletado de código para el generador de expresiones
Autocompletado de código en el editor de expresiones.
- Las variables, los nombres de funciones y los nombres de campo se proponen e insertan automáticamente al escribir expresiones
- Los parámetros de la función se muestran al llenarlos

[![image3](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)](images/entries/df385d837684dcb42633c66b5c566925803f3406.gif)

This feature was funded by [OPENGIS.ch](https://www.opengis.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch/)
## Herramientas de mapa
### Prestación: Identificar o seleccionar entidades basadas en un polígono existente
Often it is useful to select/identify features that are covered by an existing polygon. For this, users can use \"Select Features by Polygon\" and \"Identify Features by Polygon\" tools, but it was necessary to manually trace the polygon of interest. This new feature allows user to right click on the map and pick an existing polygon feature at that location from popup menu - that polygon will be used as input for selection or identification.

[![image4](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)](images/entries/ee07ddaa42114f923a4fae5429bd8d2f93e66ce5.webp)

Esta prestación fue fundada por Leicestershire County Council

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Interfaz de usuario
### Prestación: Auto selección de archivos exportados en el administrador de archivos
Whenever a message bar item links to a created file (e.g. after exporting a layout or map layer), the link will now directly open the folder containing this file within the operating system file browser AND pre-select the created file. It\'s a super-handy shortcut speeding up file operations after an export from QGIS!

[![image5](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)](images/entries/0ccd6bdae5b0df6d65c259ef08f38032fe4ee34f.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: New \"Open Directory\" option for disabled welcome page projects
Esta nueva opción de click-derecho en el menu contextual para entradas deshabilitadas en la página de bienvenida permite a los usuarios abrir la ruta existente cerrada a la localización del proyecto original en su administrador de archivos, para ayudar a reubicar proyectos faltantes/movidos/renombrados.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mejoras UX para Capas temporales Scratch
Temporary Scratch Layers in QGIS can be very handy when a \"throw-away\" layer is needed, such as when pre-processing data in multiple steps. However, they can be a trap for uniformed users who may not realise that the contents of the layer will be permanently lost when the current QGIS project is closed. Accordingly, a new indicator icon has been added which shows up next to any temporary scratch layers in the layer tree, making it immediately clear which layers are temporary only.

It\'s also much easier to transition these temporary layers to permanent disk-based formats. You can either click the new indicator icon or select \"Make Permanent\" from the layer context menu. QGIS will then prompt for a location to save the temporary layer to, then replaces it in place (keeping the same layer ID, style, form settings, etc).

[![image6](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)](images/entries/135600d5ba3c15dd0b4b6386cdd5cbf5a59ce3c2.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Mejoras en el administrador de tareas
The QGIS task manager widget (shown in the status bar whenever a background task is running) now shows an estimated time remaining and completion time for long-running background tasks. This Estimated Time of Arrival is calculated using a simple linear interpolation based on the task\'s elapsed time and current progress, and allows users to know whether they\'ve only got time to make an instance coffee in the office kitchen or walk round the block for a proper barista made coffee before that long processing task completes\...

Additionally, QGIS uses the standard operating system progress reporting mechanisms on more platforms and occasions in QGIS 3.4. Some long running tasks (which don\'t run in the background) such as atlas exports now show their progress via the operating system mechanism, and throw up handy completion notifications.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Hipervínculos a conjuntos locales vectoriales & ráster en el panel de información
For local vector and raster datasets, the Information tab within the layer properties dialog now features source file path hyperlinks. Upon clicking on the hyperlink, the system\'s file navigator will open and automatically highlight the dataset.

[![image7](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)](images/entries/6891c502c6506b88398e9bfb3e266598823c5765.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Prestación: Mejoras del administrador de estilos
El cuadro de diálogo Administrador de estilo QGIS (que permite a los usuarios configurar y administrar sus propias bibliotecas de símbolos y rampas de color) ahora se abre de forma no modal, por lo que ahora se puede usar junto con la ventana principal de QGIS (al igual que el cuadro de diálogo Administrador de diseño y el Diseñador de diseño de impresión ventanas).

We\'ve also improved the preview of symbols within the Layer Styling dock, adding a toggle to switch between a large icon view and a detailed list view of symbols. Hovering over symbols (and colors!) now shows a large preview of the symbol. Finally, we\'ve made symbol lists more hi-dpi friendly.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: pulido de la Interfaz y experiencia de panel de navegador
Se realizaron toneladas de trabajo para esta versión para mejorar la interfaz de usuario y la experiencia del panel del navegador, incluidas las correcciones de HiDPI, las mejoras del conjunto de datos vectoriales/ráster comprimidos y un conjunto de iconos actualizado.

También se ha agregado funcionalidad, incluida la capacidad de crear un nuevo directorio directamente desde el menú contextual del navegador. El navegador ahora también muestra una gama más completa de opciones para las conexiones de SQL Server, que coinciden con las opciones que ya estaban disponibles para otras conexiones de bases de datos.

[![image8](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)](images/entries/579042fca8a22be300449c3b55629fced75316b8.webp)

Esta prestación fue desarrollada por Mathieu Pellerin (iMHere Asia), Nyall Dawson (North Road)
### Prestación: Gráfico QML y widget de dibujos
En QGIS 3.4 se ha agregado un nuevo tipo de widget de formulario de capa vectorial para mostrar elementos gráficos atractivos e interactivos como gráficos o dibujos técnicos en el formulario de atributos. El widget tiene una configuración flexible, que incluye plantillas de ejemplo y soporte de expresión.

[![image9](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)](images/entries/1bc81f284db61667934e9a7e0969303f59fe06d2.gif)

This feature was funded by [QGIS Project](https://qgis.org/)

This feature was developed by [David Signer and Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Simbología
### Prestación: Estilizado de capa de malla
- Agregar conjuntos de datos a la capa de malla desde el panel de propiedades
- Panel de información y fuente en el panel de propiedades
- Selección del conjunto de datos activo (propiedades o panel de estilo)
- Estilo de contornos/escalares (propiedades o panel de estilo)
- Estilo del marco de malla (propiedades o panel de estilo)
- Diseño de flechas vectoriales (propiedades o panel de diseño)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)
### Prestación: Clasificado simétrico en renderizador graduado
This feature was funded by <https://github.com/pierreloicq>

This feature was developed by <https://github.com/pierreloicq>
### Prestación: Exportación e Importación parcial QML
When exporting and importing styles to and from `.qml` files it is now possible to select a subset of sections. This allows to save and restore parts of a layer configuration while omitting others. For example, it\'s possible to export only the symbology of a layer and when importing this QML style file into a layer, any configuration on the forms and widgets or other properties are unaffected. It is also possible to only handle single sections of a style when using copy/paste.

[![image10](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)](images/entries/93836361649c4b182b46e143014d7f30be674187.webp)

This feature was funded by [qwat group](http://qwat.org/)

This feature was developed by [Denis Rouzaud (OPENGIS.ch GmbH)](https://www.opengis.ch)
## Digitalizando
### Prestación: Mejoras en el rastreador GPS
QGIS 3.4 extends the inbuilt GPS tracking support, adding \"acquisition interval\" and \"distance threshold\" parameters. These options can be used to keep the cursor stationary when the receiver is in static conditions.

This feature was funded by [Andrea Rossi](https://github.com/rossia)

This feature was developed by [Andrea Rossi](https://github.com/rossia)
### Prestación: Mayor elección de ángulos en el muelle de digitalización avanzada
Se han añadido opciones para permitir pinzar a 5/10/15/18/22.5 grados en el modo de construcción.

[![image11](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)](images/entries/7c32c14544fb2f45646ea03f794e5124b4d4f9be.webp)

This feature was funded by [lbartoletti](https://github.com/lbartoletti)

This feature was developed by [lbartoletti](https://github.com/lbartoletti)
### Prestación: Herramienta vértices puede trabajar solo en la capa actual
The new vertex is a lot more productive now. It can move vertices of all editable layers at once, which is great to preserve cross layers topology. However in many cases, many of us don\'t want to modify all layers at once. We added a variation of the vertex map tool just for that.

[![image12](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)](images/entries/7c03fe883ce1558385fdc922797ab3a7342136d0.webp)

This feature was funded by [Oslandia](https://oslandia.com)

This feature was developed by [Paul Blottiere (Oslandia)](https://oslandia.com/en/home-en/)
### Prestación: Añadir herramientas de mapa  de línea inversa
A long awaited feature ! No more external plugin or algorithm to reverse a line\'s direction!

[![image13](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)](images/entries/988902221b0384cd96f880633f9d822faaad6903.webp)

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Loïc Bartoletti](https://github.com/lbartoletti)
### Prestación: Precisión geométrica
Las capas vectoriales tienen una opción de configuración de precisión. La precisión define cuán precisa se debe guardar la ubicación de los nodos. Cada nodo de geometrías nuevas o editadas se ajusta a una cuadrícula de esta resolución. Mientras se digitaliza, se muestra la cuadrícula para guiar al usuario.

[![image14](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)](images/entries/4dc31694598d9c507be8ed1110c0c4a494b997ec.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Borrar automáticamente nodos duplicados
Al agregar o editar geometrías en una capa vectorial, QGIS puede eliminar automáticamente nodos duplicados de las geometrías. Esta opción es configurable en la pestaña de digitalización de capas vectoriales.

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Verificar la validez geométrica
Se puede verificar la validez de cada geometría nueva o editada si esta opción está activada. Esto permite comunicarse de forma transparente con un usuario cuando hay geometrías erróneas producidas por la sesión de edición actual.

[![image15](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)](images/entries/f5eee0b5a59923d41b427c9acc432b4c4f86da01.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Pruebas de topología mientras se edita
Las comprobaciones de topología se pueden activar en una capa. En geometrías recién agregadas y editadas, se pueden ejecutar comprobaciones de topología. Las verificaciones se ejecutarán cuando se guarde la capa o al hacer clic en el botón de verificación de topología en el panel de validación de geometría.

Las siguientes pruebas están disponibles:
- Huecos
- Superposiciones
- Vértices perdidos en polígonos vecinos

This builds on top of the functionality of the geometry checker plugin which was implemented by [Sourcepole](https://sourcepole.ch).

[![image16](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)](images/entries/a706012a7afb489573f08133f5885fe5bc1a3660.gif)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Administración de datos
### Prestación: Traducción de proyectos QGIS
Like QGIS and the plugins, the projects are translated with the Qt translation process. Means, it makes the translation according to a Qt Compiled Translation Source File (`.qm` file). When the user opens a project, QGIS checks for a `.qm` file laying in the same folder like the `.qgs` file, having the same name like the `.qgs` file and having the language-code as postfix of the users language (the language configured in the QGIS settings). To create the translation, in the project settings, there is an option to generate the `.ts` file, that can edited by programs like Qt Linguist or Transifex.

More information in [this blog post](https://new.opengis.ch/2018/09/11/qgis-speaks-a-lot-of-languages/)

This feature was funded by [QGIS Usergroup Switzerland and QGEP Project](https://www.qgis.ch/en)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch/)
### Prestación: Cambiar el modo de acoplamiento de la tabla de atributos bajo demanda
A button has been added to the Attribute Table toolbar for switching between docked and window mode on demand. Previously users had to change an option in the settings dialog and open a new table in order to switch between docked/undocked mode, but that\'s painful if you decide *after* a table is already open that you\'d like to dock/undock it\...!

[![image17](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)](images/entries/2ed512377b90aed08dc73bb7b3ea17ae5c9f4708.gif)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Nuevo filtro de localización para buscar en todas las capas
A new locator filter has been added which allows users to search across *all* layers in their project, by the layer\'s display expression.

The filter can be activated by using the prefix \'af\', or by making it a default search via QGIS options -\> Locator -\> Features In All Layer. Display expressions are defined in the vector layer properties under the display tab. Individual layers can be marked as not searchable in the Project Properties dialog, under the Data Sources tab.

[![image18](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)](images/entries/0e99950042f20317f1974b5f2f999cbd9233b47c.webp)

This feature was funded by [Opengis.ch](https://www.opengis.ch/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Prestación: Capas no borrables(requeridas) resaltadas en el árbol de capas
A new indicator \"locked\" icon is shown for any layers marked as \"required\" within the current project. This icon gives users instant feedback that a particular layer cannot be removed from the project.

Las capas requeridas se configuran a través del cuadro de diálogo Propiedades del proyecto, pestaña Orígenes de datos.

[![image19](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)](images/entries/43cff3e927cdbacf08d61f979891030e48f9a451.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Prestación: Agregar capa ráster a un Geopackage existente
When saving a raster layer to GeoPackage database, it\'s now possible to append the layer to an existing file.

[![image20](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)](images/entries/7417555bb52774a5b522ec6d3034d6fd22077732.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
## Widgets y Formularios
### Prestación: Formularios Drill-Down(en cascada) en Widgets de Relación de Valores
New functions and logic in QGIS "Value Relation Widgets", allowing the implementation of complex, dynamic filters within QGIS attribute forms. The functionality can be used to implement "drill-down" forms within QGIS, where the values available in one field depend on the values of other fields:

[![image21](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif)

This feature was funded by [QGIS community through crowd-funding](https://north-road.com/drill-down-cascading-forms/)

Esta prestación fue desarrollada por Alessandro Pasotti (with North Road)
## Compositor de Mapa
### Prestación: Elementos de Mapa 3D
Esta prestación permite a los usuarios añadir su vista de mapa 3D a la impresora de diseño.

[![image22](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)](images/entries/413f4a9377731af02f3fe815bf3b7e70ac508d1c.webp)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
## Procesado
### Feature: New \"Edit in place\" mode
Thanks to a large number of [generous backers](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/), a crowdfunded \"edit in place\" mode was added to Processing for 3.4. When a vector layer is active and editable, this mode allows users to execute suitable algorithms directly on the features from the layer, modifying their attributes and geometries in-place. All edits are added to the layer's "edit buffer", so you can easily undo and redo the changes before saving them back to the data source.

For those power users who perform frequent data edits, this functionality is also exposed via QGIS 3.0's "Locator bar" (that "type to locate" bar which sits in the bottom-left corner). Typing 'ef' ("edit features") followed by the name of the corresponding operation allows you to perform the edits directly via the keyboard. E.g.
- Seleccione un montón de características de línea
- Presione Ctrl+K (activa la barra de localización)
- Type "ef reverse"
- Press enter -- the selected line features will be reversed immediately!

[![image23](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)](images/entries/bdfd9b4a3d367378786fd358e13c475e7fb05816.gif)

This feature was funded by [Crowdfunding campaign](https://north-road.com/edit-features-in-place-using-qgis-spatial-operations-campaign/)

This feature was developed by [North Road](https://north-road.com)
### Prestación: Almacenar modelos dentro del proyecto
Some Processing models are so intrinsically linked to the logic inside a particular project that they have no meaning (or are totally broken) outside of that project (e.g. models which rely on the presence of particular map layers, relations, etc). Accordingly, from QGIS 3.4, Processing models can be stored inside QGIS project files. Any models stored within a project are made available as soon as that project is opened. This also avoids cluttering up the \"global\" model provider with models which make no sense, and makes it easier to distribute a single project all relevant models included.

Models are stored inside projects by clicking the new \"Embed in Project\" button in the Modeler dialog toolbar. Models can be removed from a project from the model\'s right click menu in the toolbox.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Muestra de valores ráster
Un nuevo algoritmo se ha añadido para muestreo de valores de capas ráster en ubicaciones puntuales.

[![image24](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)](images/entries/835925fb7c793d7e56a8c21a49408cd2542c973c.webp)

This feature was funded by [Faunalia](https://www.faunalia.eu)

This feature was developed by [Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Feature: New \'Raster pixels to polygons\' algorithm
Este algoritmo convierte una capa ráster en una capa vectorial, con una entidad de polígono correspondiente a cada píxel del ráster y un único campo que contiene el valor de banda del ráster.

This feature was funded by [SMEC/SJ](http://smec.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Prestación: algoritmo de agrupamiento K-Means
QGIS 3.4 adds a native \"k-means clustering\" algorithm. Based on a port of PostGIS\' ST_ClusterKMeans function, this algorithm adds a new cluster ID field to a set of input features which identifies the feature\'s cluster based on a k-means clustering approach. If non-point geometries are used as input, the clustering is based off the centroid of the input geometries.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: algoritmo de agrupación espacial dbscan
Este nuevo algoritmo nativo implementa una aproximación optimizada de agrupación por barrido basado en la densidad DBSCAN para agrupar entidades puntuales 2D. 

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación:  Algoritmos mejorados
Algunas mejoras diversas a algoritmos existentes de procesamiento incluyen:
- El algoritmo "Dirección inversa de línea" ahora funciona con entradas de geometría MultiLineString
- *Extender líneas*: añadido soporte para distancias inicial y final dinámicas (definidos por datos)
- *Compensación de líneas*: soporte para compensación dinámica de distancia
- Los algoritmos *Unir por valor de campo* y *Unir por localización* ahora puede exportar opcionalmente registros no coincidentes
- "Unir por valor de campo*: tambien informa recuentos de entidades coincidentes/no coincidentes

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Algoritmos para filtrar vértices por M y filtrar vértices por Z
Se agregaron dos nuevos algoritmos para filtrar vértices de línea/polígono por sus valores M o Z. Se puede ingresar un valor M/Z mínimo y máximo, y si los vértices caen fuera de estos rangos, se descartarán de la geometría de salida. Los valores de filtro mínimo y máximo también se pueden definir con datos, por lo que pueden variar según la entidad.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of Translated Features\" algorithm
Este nuevo algoritmo crea copias de entidades en una capa, creando múltiples versiones trasladadas (desplazamiento) de una entidad. Cada copia es desplazada por una pequeña cantidad en el eje x/y/z/m.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Array of offset (parallel) lines\" algorithm
Este nuevo algoritmo crea copias de una entidad lineal en una capa, mediante la creación de múltiples versiones paralelas de cada entidad. Cada copia es desplazada en una distancia preestablecida.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Elección de unidades para distancias no graduadas/desconocidas
Cuando un algoritmo tiene un parámetro de distancia en metros/pies/etc (p.ej. distancias no geográficas), se ha añadido un combo box permitiendo elegir el tipo de unidad.

(QGIS doesn\'t (and should **never**) expose this for distances in degrees \-- it\'s up to users in this situation to choose a suitable local projection and reproject their data to match.)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson](https://north-road.com)
### Feature: \"Drape features to z/m\" algorithms
Estos dos nuevos algoritmos pueden establecer el vértice z o m de una geometría a valores  muestreados desde una banda ráster. Los valores se pueden escalar opcionalmente usando un valor de escala (definido por datos).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Raster pixels to points\" algorithm
A new \"pixels to points\" algorithm was added in QGIS 3.4, which creates a point feature at the center of every pixel. nodata pixels are skipped.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: algoritmo de subcadena de línea
Este nuevo, muy solicitado, algoritmo devuelve la porción de una línea (o curva) que cae dentro de las distancias inicial y final (medida desde el comienzo de la línea). Los valores Z y M son interpolados linealmente desde valores existentes.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Interpolate point on line\" algorithm
Este nuevo algorimto crea una geometría puntual interpolada a una distancia fija en la geometría lineal (o límite de polígono). Son completamente admitidas entradas de geometrías curvas. Valores Z o M son linealmente interpoladas a partir de valores existentes.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: casco cócavo k-vecino
This feature was funded by <https://qgis.org>

This feature was developed by [Detlev Neumann, Rudi von Staden](https://qgis.org)
### Prestación: Las secuencias de comandos de Python que implementan algoritmos ahora ejecutan el algoritmo al arrastrar y soltar y al hacer doble clic en el navegador
Cuando sea apropiado, los scripts ahora iniciarán un diálogo de algoritmo de procesamiento cuando:
- Arrastrar y soltar un script de Python en la ventana principal
- Using the browser panel\'s right-click run script action

[![image25](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)](images/entries/06f359ac4e92e415c502bc5def413563b755d8e8.webp)

This feature was funded by [iMhere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: New GDAL\'s rearrange band algorithm
A new GDAL provider \'Rearrange band\' algorithm was added to the processing toolbox. The algorithm allows to output rasters continuing a subset of a given input raster\'s bands, and offers the possibility to re-order the bands.

[![image26](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)](images/entries/989a55b259fe6fd44640151cf4e2b0f0bb34573b.webp)

This feature was funded by [iMHere Asia](https://www.imhere-asia.com/)

This feature was developed by [Mathieu Pellerin](https://www.imhere-asia.com/)
### Feature: \"Precalculated\" values for model algorithm parameters
A new option is present for all parameters of using a \"precalculated expression\". This expression is evaluated once before the child algorithm is executed and used during the execution of that algorithm.

This feature was funded by [QGIS](https://qgis.org)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: \"Categorize a layer using a style XML file\" algorithm
This new algorithm sets a vector layer\'s renderer to a categorized renderer using matching symbols from a style database.

A specified expression (or field name) is used to create categories for the renderer, with QGIS creating a category for each unique value within the layer. Each category is individually matched to the symbols which exist within the specified QGIS XML style database. Whenever a matching symbol name is found, the category\'s symbol will be set to this matched symbol.

La coincidencia no distingue entre mayúsculas y minúsculas de forma predeterminada, pero se puede distinguir entre mayúsculas y minúsculas si es necesario. Opcionalmente, los caracteres no alfanuméricos tanto en el valor de la categoría como en el nombre del símbolo se pueden ignorar mientras se realiza la coincidencia. Esto permite una mayor tolerancia al combinar categorías con símbolos.

Si lo desea, también se pueden generar tablas que contengan listas de las categorías que no pueden coincidir con los símbolos y símbolos que no coinciden con las categorías.

[![image27](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)](images/entries/dbf5d7f496eadfefae1bc300f763e991206fb694.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Nuevo algoritmo de modo para pinzar geometrías
The new mode \"Snap to anchor nodes (single layer only)\" makes sure that any two vertices of the vector layer are at least at distance given by the threshold value.

Este algoritmo es útil cuando se realizan operaciones de superposición de vectores como intersección, unión o diferencia para evitar posibles errores topológicos causados por errores numéricos si las coordenadas están muy cerca una de la otra. Después de ejecutar el algoritmo, algunas geometrías previamente válidas pueden volverse inválidas y, por lo tanto, puede ser útil ejecutar el algoritmo Fix geometries después.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Proveedores de datos
### Prestación: complemento de método de autenticación OAuth2
- Soporta código de autenticación, implícito y propietario del recurso de concesión del flujo
- Permite par conexiones preconfiguradas, lectura para localizaciones por defecto
- Ofrece almacenamiento en caché de la toma de acceso más allá de los reinicios de QGIS
- Guardar/cargar configuraciones

This feature was funded by [Monsanto Company](https://monsanto.com/)

This feature was developed by [Larry Shaffer, Alessandro Pasotti](https://qgis.org)
### Prestación: capa de malla: Nuevo soporte de formato de capa de malla
Las capas de malla representan datos en una cuadrícula de tamaño variable con componentes adicionales (por ejemplo, tiempo y vector). Con la introducción de MDAL, los usuarios pueden cargar los siguientes formatos directamente en QGIS y explorar todos los demás componentes:
- GRIB
- XMDF
- Netcdf

[![image29](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)](images/entries/767a26455fb1a8ad8cab663a52832ef575954483.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/blog/2018/10/18/mdal/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Prestación: capa de malla: añadir función para identificar valores en capas de malla
Con esta API, los desarrolladores pueden inspeccionar elementos de malla y obtener valores espacial y temporalmente. Como ejemplo, puede crear un diagrama de series de tiempo desde su capa de malla.

[![image30](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)](images/entries/45c0ea5d14157275da7153ac31cc41987319e5eb.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Prestación: capa de malla: permitir elegir diferentes dataset vectoriales y escalares
Una capa de malla a menudo contiene varias cantidades. Por ejemplo, un netcdf/grib puede contener varias cantidades meteorológicas. Cada cantidad también puede tener múltiples componentes. Por ejemplo, los datos del viento pueden contener velocidad (escalar) y valores (cuadrícula). Con esta opción, puede superponer escalares y cuadrículas de diferentes cantidades. En la imagen a continuación, puede ver la temperatura (cuadrícula) y el viento (escalar).

[![image31](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)](images/entries/74ce47f09e8644a2ce6a8daeae2e37e13615b956.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Prestación: capa de malla: permitir representar vectores/flechas en la cuadrícula definida por el usuario
Los datos escalares se generan generalmente en el centro/esquina de cada elemento de malla. Al mostrar los datos escalares, las flechas pueden verse dispersas y, a menudo, no es posible ver la tendencia general. Con esta opción, las flechas se pueden mostrar en una cuadrícula definida por el usuario. Los valores escalares adicionales se interpolarán sobre la marcha y se colocarán en la cuadrícula definida por el usuario.

[![image32](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)](images/entries/9eaa1430fee8b738a79936d7df104270e0b7f2a8.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Prestación: soporte tipos JSON/JSONB
The reading of PostgreSQL JSON types is supported. JSON Data can be displayed in the widgets as \"Key/Value\" (maps), as \"List\" (arrays) or as text.

[![image33](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)](images/entries/94f82c582268d7966bb1fa140893b63af207dca3.webp)

This feature was funded by [Kanton Solothurn](https://www.so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: soporte de autenticacion token de Esri
Support has been added to QGIS\' Authentication system for ESRI\'s temporary token based authentication. This allows for connection to ArcGIS Feature and Map Servers via an allocated temporary token.

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: SQL Server - manejo de geometrías inválidas
Recent versions of QGIS have switched to a safer approach to reading SQL Server layers, which automatically checks for geometry validity and repairs geometries when needed. This workaround is required to avoid issues with the design of SQL Server\'s geometry handling, where encountering any rows with invalid geometries can silently abort a request without returning all the features from a layer. Unfortunately, the workaround comes at a significant performance cost.

In QGIS 3.4 a new setting was added to allow users to manually turn off QGIS\' SQL Server invalid geometry handling. Turning on the \"Skip invalid geometry handling\" setting under a SQL Server connection\'s properties causes QGIS to skip all the expensive geometry validation processing, but firmly places the responsibility for ensuring that all features on the database have valid geometries back upon the user/database administrator. **This is a \"use at your own risk\" setting. Improperly enabling this option can lead to missing features and data loss.**

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Servidor de QGIS
### Prestación: La caché del servidor se puede administrar mediante complementos
De forma predeterminada, QGIS Server solo almacena en la memoria caché el documento WMS GetCapabilities. Con la implementación de WMTS, es necesario tener una forma de almacenar en caché las teselas. Pero el administrador de caché no se ha desarrollado solo para almacenar en caché teselas.

El complemento del administrador de caché se puede usar para almacenar en caché:
- WMS, WFS, WCS, WMTS GetCapabilities documentos
- WFS DescribeFeatureType documentos
- WCS DescribeCoverage documentos
- WMTS GetTile imagenes
- WMS GetLegendGraphic imagenes

Aquí hay una clase de administrador de caché de Python, que no verifica si el proyecto QGIS ha cambiado:

    class PyServerCache(QgsServerCacheFilter):
    
        """ Used to have cache control """
    
        def __init__(self, server_iface):
            super(QgsServerCacheFilter, self).__init__(server_iface)
    
            self._cache_dir = os.path.join(tempfile.gettempdir(), "qgs_server_cache")
            if not os.path.exists(self._cache_dir):
                os.mkdir(self._cache_dir)
    
            self._tile_cache_dir = os.path.join(self._cache_dir, 'tiles')
            if not os.path.exists(self._tile_cache_dir):
                os.mkdir(self._tile_cache_dir)
    
        def getCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                return QByteArray()
    
            doc = QDomDocument(m.hexdigest() + ".xml")
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "r") as f:
                statusOK, errorStr, errorLine, errorColumn = doc.setContent(f.read(), True)
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            return doc.toByteArray()
    
        def setCachedDocument(self, doc, project, request, key):
            if not doc:
                print("Could not cache None document")
                return False
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._cache_dir, m.hexdigest() + ".xml"), "w") as f:
                f.write(doc.toString())
            return os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocument(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml")):
                os.remove(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
            return not os.path.exists(os.path.join(self._cache_dir, m.hexdigest() + ".xml"))
    
        def deleteCachedDocuments(self, project):
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            for f in filelist:
                os.remove(os.path.join(self._cache_dir, f))
            filelist = [f for f in os.listdir(self._cache_dir) if f.endswith(".xml")]
            return len(filelist) == 0
    
        def getCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
    
            if not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                return QByteArray()
    
            img = QImage(m.hexdigest() + ".png")
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "rb") as f:
                statusOK = img.loadFromData(f.read())
                if not statusOK:
                    print("Could not read or find the contents document. Error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
                    return QByteArray()
    
            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            img.save(buff, 'PNG')
            return ba
    
        def setCachedImage(self, img, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            with open(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"), "wb") as f:
                f.write(img)
            return os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImage(self, project, request, key):
            m = hashlib.md5()
            paramMap = request.parameters()
            urlParam = "&".join(["%s=%s" % (k, paramMap[k]) for k in paramMap.keys()])
            m.update(urlParam.encode('utf8'))
            if os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png")):
                os.remove(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
            return not os.path.exists(os.path.join(self._tile_cache_dir, m.hexdigest() + ".png"))
    
        def deleteCachedImages(self, project):
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            for f in filelist:
                os.remove(os.path.join(self._tile_cache_dir, f))
            filelist = [f for f in os.listdir(self._tile_cache_dir) if f.endswith(".png")]
            return len(filelist) == 0
    
Y la forma de agregarlo al administrador de caché del servidor QGIS.

`servercache = PyServerCache(server_iface) server_iface.registerServerCache(servercache, 100)`

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### Prestación: soporte WMTS 1.0.0
QGIS Server 3.4 es compatible con el estándar WMTS 1.0.0 OGC.

En las propiedades del proyecto QGIS, el usuario puede definir:
- qué parte del proyecto (todos los proyectos, grupos de capas o capas) debe publicarse a través del estándar WMTS
- la escala mínima de teselas

El servidor QGIS reutiliza el CRS definido en el WMS para WMTS.

Para administrar la memoria caché de teselas, QGIS Server debe instalar y cargar un complemento QGIS Server con una clase QgsServerCacheFilter.

[![image34](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)](images/entries/d0d72b47494e231b98bf3169fcbe34ca22d0624d.webp)

This feature was funded by [Ifremer](https://wwz.ifremer.fr/)

This feature was developed by [3Liz](https://3liz.com)
### Prestación: Añadir capacidad para definir min. escala para WMTS
This feature was funded by <https://github.com/rldhont>

This feature was developed by <https://github.com/rldhont>
### Prestación: Admite registros del servidor QGIS en stderr
It\'s now possible to configure QGIS Server to make it write its logs to stderr. This is done by setting the QGIS_SERVER_LOG_FILE env var to the special value \"stderr\".

This feature was funded by [OSLANDIA](https://oslandia.com)

This feature was developed by [Eric Lemoine](https://github.com/elemoine)
## Plugins
### Prestación: Soporte para zips encriptados en el Administrador de Plugins
El Administrador de Plugins ahora es capaz de instalar plugins desde archivos locales zip incluso si están encriptados.

[![image35](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)](images/entries/1bfc11325b9afa06d3196603749e1786f7922ffd.webp)

This feature was funded by [Borys Jurgiel](https://github.com/borysiasty)

This feature was developed by [Borys Jurgiel](https://github.com/borysiasty)
### Prestación: Edición de GeoPackage fuera de línea
Con la funcionalidad de edición fuera de línea, es posible seleccionar si la exportación debe crear un archivo SpatiaLite o GeoPackage para uso fuera de línea.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
## Programabilidad
### Prestación: QgsSpatialIndexKDBush
A very fast static spatial index for 2D points based on a flat KD-tree, using <https://github.com/mourner/kdbush.hpp>

Compared to QgsSpatialIndex, this index: - supports single point features only (no multipoints) - is static (features cannot be added or removed from the index after construction) - is much faster! - supports true \"distance based\" searches, i.e. return all points within a radius from a search point

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: QgsRasterDataProvider:: método de prueba para un muestreo eficiente de rásteres en un punto dado
This is an alternative to the `QgsRasterDataProvider::identify` method, which is less efficient but more powerful

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: Nueva llamada de API de geometría para devolver una subcadena de curva
Se ha agregado la nueva API PyQGIS para facilitar la recuperación de una subcadena de una geometría LineString/Curve:

`QgsCurve::curveSubstring - Returns a new curve representing a substring of a curve, from a start distance and end distance.`

If z or m values are present, the output z and m will be interpolated using the existing vertices\' z or m values. The method also handles curved geometries without loss or segmentation.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Prestación: cambios en el Módulo sip de la API
Due to upstream changes within the PyQt/sip library, the recommended way to import this module has changed in QGIS 3.4. For maximum portability, instead of directly calling: `import sip` plugins should instead use: `from qgis.PyQt import sip` Using this newer style import will ensure that the code works correct across all platforms and remains functional in future QGIS versions.
### Prestación: Proveedores de datos vectoriales de Python
Desarrollo de la API, un proveedor de muestras y pruebas que permiten la creación de un proveedor de datos vectoriales en Python puro.

[![image36](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)](images/entries/dbae71a0ccad069280a263fabddf3452b8165ca3.webp)

Esta prestación fue financiada por Good will

Esta funcionalidad fue desarrollada por Alessandro Pasotti
## Objetos 3D
### Prestación: navegación mejorada
This will update camera\'s view center as the camera moves around. Before the view center would be always at the zero elevation, which means that with terrain further away from zero elevation tilting and rotation of camera would feel weird due to the center point being far away.

Permite mover la cámara arriba/abajo usando las teclas page up/page down

Mover cámara manteniendo la posición con Ctrl+cursores de dirección/ratón

[![image37](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)](images/entries/a1b22a29fc363ffc90be8f98a991913148164ef2.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Animación
Puede crear una animación basada en un conjunto de fotogramas clave: posiciones de la cámara en momentos particulares. QGIS 3D luego interpola las posiciones/rotaciones de la cámara entre los fotogramas clave.

Para crear los fotogramas clave, primero configure la escena para su mapa, girando, haciendo zoom o moviendo la cámara. Luego asigne un tiempo al marco. Existen varios métodos para las interpolaciones entre fotogramas clave.

[![image38](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)](images/entries/006592e0cf0245a829d451988d178c5f07ce5560.gif)

This feature was funded by [QGIS community through crowd-funding](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martian Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Renderizado Simple de cadenas lineales 3D
Este modo de representación de líneas 3D utilizará la representación de líneas OpenGL en lugar de almacenar las líneas en polígonos y representarlas como mallas.

The advantage is that the 3D lines do not loose their Z coordinate which is the case currently with \"ordinary\" 3D rendering after buffering.

The disadvantage is that the lines cannot be wide (supported in Qt3D only since 5.10, but even then their rendering won\'t have nice joins/caps) and only ambient color is used from the material.

[![image39](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)](images/entries/d28d6a8023fa5fbd306f6b31f0545ff71112009f.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
### Prestación: Herramienta de Identificación en Mapa para vistas 3D
Una nueva herramienta de Identificación fue introducida para mapas 3D. Usando esta herramienta, puede inspeccionar entidades desde la escena 3D.

[![image40](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)](images/entries/88fc4584f5ec10e1112813c133bf40f481af9e88.gif)

This feature was funded by [Department of Environment, Land and Infrastructure Engineering (DIATI)](https://www.faunalia.eu/en/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Prestación: API Experimental de Python
Algunas clases de QGIS 3D se han puesto a disposición de los desarrolladores de Python. Ahora es posible consultar o cambiar los renderizadores 3D de las capas del mapa y las propiedades de lectura/escritura de los símbolos 3D contenidos, como los colores de los materiales. Tenga en cuenta que, por ahora, la API se considera experimental, por lo que puede cambiar en futuras versiones 3.x.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
