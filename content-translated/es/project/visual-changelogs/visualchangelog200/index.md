---
HasBanner: false
draft: false
releaseDate: '2013-09-09'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.0
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.0{#changelog20 }
Fecha de lanzamiento: 2013-09-09

{{<table-of-contents >}}
## Herramientas de análisis
### Característica: Comandante de Procesamiento
Para acceder rápidamente a la funcionalidad de geoprocesamiento, simplemente inicie el comando de procesamiento (Ctrl + Alt + M) y comience a escribir el nombre de la herramienta que está buscando. Commander le mostrará las opciones disponibles y las lanzará por usted. No más búsquedas en los menús para encontrar herramientas. Ahora están a tu alcance.

![image1](images/processing_commander_2.png)
### Característica: Mejoras en complemento Mapas de Calor
El complemento de mapa de calor ha visto numerosas mejoras y optimizaciones, resultando una creación mucho más rápida de mapas de calor. Además, ahora tiene la opción de elegir qué función kernel se usa para crear el mapa de calor.

![image2](images/Selection_027.png)
### Característica: Soporte de procesamiento
The SEXTANTE project has been ported to and incorporated into QGIS as core functionality. SEXTANTE has been renamed to \'Processing\' and introduces a new menu in QGIS from where you can access a rich toolbox of spatial analysis tools. The processing toolbox has incredibly rich functionality - with a python programming API allowing you to easily add new tools, and hooks to provide access to analysis capabilities of many popular open source tools such as GRASS, OTB, SAGA etc.

![image3](images/Selection_028.png)
### Característica: Modelador de Procesamiento
Una de las grandes características del nuevo marco de procesamiento es la capacidad de combinar las herramientas gráficamente. Con **Processing Modeller**, puede crear análisis complejos a partir de una serie de pequeños módulos de un solo propósito. Puede guardar estos modelos y luego usarlos como bloques de construcción en modelos aún más complejos. ¡Impresionante poder integrado en QGIS y muy fácil de usar!

![image4](images/Processing_modeler_029.png)
## Opciones de Aplicación y Proyecto
### Característica: defina el proyecto de inicio predeterminado y las plantillas de proyecto
With QGIS 2.0 you can specify what QGIS should do when it starts: `New Project` (legacy behaviour, starts with a blank project), `Most recent` (when you start QGIS it will load the last project you worked on), `Specific` (always load a specific project when QGIS starts). You can use the project template directory to specify where your template projects should be stored. Any project that you store in that directory will be available for use as a template when invoking the `Project --> New from template` menu.

![image5](images/Screen_Shot_2013-09-12_at_11.23.02_PM.png)
### Característica: Variables de ambiente del sistema
Current system environment variables can now be viewed and many configured within the application Options dialog. Useful for platforms, such as Mac, where a GUI application does not necessarily inherit the user\'s shell environment. Also useful for setting/viewing environment variables for the external tool sets controlled by the processing toolbox, e.g. SAGA, GRASS; and, for turning on debugging output for specific sections of the source code.

![image6](images/changelog-2.0_sys-env-options.png)
### Característica: Escalas de acercamiento definidas por el usuario
A listing of zoom scales can now be configured for the application and optionally overridden per project. The list will show up in the `Scale` popup combo box in the main window status bar, allowing for quick access to known scales for efficiently viewing and working with the current data sources. Defined scales can be exported to an XML file that can be imported into other projects or another QGIS application.

![image7](images/changelog-2.0_predefined-scales.png)
## Navegador
### Característica: Mejoras al panel de navegador en-aplicación
- Directorios pueden ser filtrados con expresiones * ! (wildcard) o expresiones regulares
- New `Project home` (parent directory of current project)
- View `Properties` of the selected directory in a dialog
- Choose which directories to `Fast scan`
- Choose to `Add a directory` directly to `Favourites` via filesystem browse dialog
- New `/Volumes` on Mac (hidden directory for access to external drives)
- New `OWS` group (collation of available map server connections)
- Open a second browser (`View -> Panels -> Browser (2)`) for drag-n-drop interactions between browser panels
- Íconos ahora ordenados por tipo grupo de elemento (sistema de archivo, bases de datos, servidores de mapa)
- Layer `Properties` now have better visual layout

![image8](images/changelog-2.0_browser.png)
## Proveedores de datos
### Característica: mejora del Proveedor de Datos Ráster
The raster data provider system has been completely overhauled. One of the best new features stemming from this work is the ability to \'Layer -\> Save As\...\' to save any raster layer as a new layer. In the process you can clip, resample, and reproject the layer to a new Coordinate Reference System. You can also save a raster layer as a rendered image so if you for example have single band raster that you have applied a colour palette to, you can save the rendered layer out to a georeferenced RGB layer.

![image9](images/Selection_017.png)
### Característica: Soporte para Oracle Spatial
QGIS 2.0 ahora incluye soporte para Oracle Spatial.

![image10](images/oracle.png)
### Característica: Adicionado proveedor Web Coverage Service
QGIS ahora provee soporte nativo para capas Web Coverage Service - el proceso para adicionar wCS es similar a adicionar una capa WMS o WFS.
### Característica: Corte acumulativo 2% ráster predeterminado
Muchos productos de imágenes ráster tienen una gran cantidad de valores atípicos que dan como resultado imágenes con un aspecto desvaído. QGIS 2.0 introduce un control mucho más fino sobre el comportamiento de representación de los rásteres, incluido el uso de un corte acumulativo de 2% a 98% por defecto al determinar el espacio de color para la imagen. La imagen aquí muestra QGIS 1.8 (izquierda) versus QGIS 2.0 (derecha) cuando se procesa la misma imagen con la configuración predeterminada.

![image11](images/Selection_023.png)
### Característica: Formato de identificar WMS
Ahora es posible seleccionar el formato de los resultados de la herramienta de identificación para capas WMS si múltiples formatos conocidos son admitidos por el servidor. Los formatos admitidos son HTML, elemento (GML) y texto. Si se selecciona el formato de elemento (GML), el resultado está en la misma forma que para capas vectoriales, la geometría puede estar destacada y el elemento incluyendo atributos y geometría puede copiarse al porta-papeles y pegado a otra capa.

![image12](images/wms-identify.png)
### Característica: Soporte WMTS
El cliente WMS en QGIS ahora admite WMTS (Servicios Web de Tesela de Mapas), incluida la selección de subconjuntos de datos, como segmentos de tiempo. Al agregar una capa WMS desde un servidor compatible, se le pedirá que seleccione el intervalo de tiempo para mostrar.

![image13](images/Selection_035.png)
## General
### Feature: Quantum GIS is now known only as \'QGIS\'
The \'Quantum\' in \'Quantum GIS\' never had any particular significance and the duality of referring to our project as both `Quantum GIS` and `QGIS` caused some confusion. We are streamlining our project and as part of that process we are officially dropping the use of the word `Quantum` - henceforth we will be known only as `QGIS` (spelled with all letters in upper case). We will be updating all our code and publicity material to reflect this.

![image14](images/qgis.png)
## Etiquetando
### Característica: Nuevo sistema de etiquetado
The labelling system has been totally overhauled - it now includes many new features such as drop shadows, \'highway shields\', many more data bound options, and various performance enhancements. We are slowly doing away with the \'old labels\' system, although you will still find that functionality available for this release, you should expect that it will disappear in a follow up release.

![image15](images/Layer_labeling_settings_003_1.png)
### Característica: Propiedades de etiquetas basadas en expresión
The full power of normal label and rule expressions can now be used for label properties. Nearly every property can be defined with an expression or field value giving you more control over the label result. Expressions can refer to a field (e.g. set the font size to the value of the field \'font\') or can include more complex logic.

Ejemplos de propiedades enlazables incluyen:
- Tipo de letra
- Tamaño
- Estilo
- Tamaño de la zona de influencia

![image16](images/2013-09-05_09_44_59-qgis-dev-bin.png)
### Característica: Antiguo motor de etiquetado dado de baja
Use of the older labelling engine available in QGIS \<= 1.8 is now discouraged (i.e. deprecated), but has not been removed. This is to allow users to migrate existing projects from the old to new labelling engine.

Se aplican las siguientes líneas guías para trabajar con el motor más antiguo en QGIS 2.0:
- Deprecated labelling tab is removed from vector layer properties dialog for new projects or older opened projects that don\'t use that labelling engine.
- La pestaña en desuso permanece activa para proyectos abiertos más antiguos si alguna capa los usa, y no desaparece incluso si guarda el proyecto sin capas que tengan habilitado el motor de etiquetado más antiguo.

La pestaña de etiquetado obsoleto se puede habilitar/deshabilitar para el proyecto actual, a través de los comandos de la consola Python, por ejemplo:

    >>> QgsProject.instance().writeEntry('DeprecatedLabels', '/Enabled', True | False)
    # or
    >>> QgsProject.instance().removeEntry('DeprecatedLabels', '/')
    
**NOTA**: Existe una *probabilidad muy alta* de que el motor de etiquetado en desuso se elimine por completo antes de la próxima versión estable de QGIS. Por favor, migre proyectos más antiguos.

![image17](images/changelog-2.0_labels-deprecated.png)
## Leyenda de capa
### Característica: retroalimentación visual y opciones de leyenda
- Conteo total para elementos en una capa, así como por símbolo
- Capas vector en modo edición ahora tiene un lápiz rojo para indicar ediciones no despachadas (no guardadas)
- La capa activa ahora está subrayada, para indicarla en selecciones multi-capas or cuando no existe selección
- Al hacer clic en espacios en blanco que no son elementos de la lista, ahora se borra la selección
- `Right-clicks` are now treated as `left-clicks` prior to showing the contextual menu, allowing for one click instead of two
- Grupos y capas pueden estar opcionalmente  en el estilo letra negrita.
- Los iconos de vista previa generados por la capa ráster ahora se pueden desactivar, para proyectos donde dicha representación puede ser lenta

![image18](images/changelog-2.0_visual-options.png)
### Característica: Duplicar la capa de mapa existente
Duplicar las capas vectoriales y ráster seleccionadas en la leyenda de la capa del mapa. Similar a importar nuevamente la misma fuente de datos, como una capa separada, luego copiar/pegar atributos de estilo y simbología.

![image19](images/changelog-2.0_dup-layer_1.png)
### Prestación: commandos de edición alterna de multicapas
El usuario ahora puede seleccionar varias capas en la leyenda y, si alguna de ellas es una capa vectorial en modo de edición, elija guardar, revertir o cancelar las ediciones actuales no confirmadas. El usuario también puede elegir aplicar esas acciones en todas las capas, independientemente de la selección.

![image20](images/changelog-2.0_current-edits.png)
## Compositor de Mapa
### Característica: Elementos Mapa HTML
Ahora puede colocar elementos html sobre su mapa.

![image21](images/Composer_1_006.png)
### Característica: Soporte multipágina
Una ventana única de diseñador ahora puede contener más de una página.

![image22](images/2013-09-08_22_31_33-Composer_1.png)
### Característica: Expresiones en etiquetas del diseñador
The composer label item in 1.8 was quite limited and only allowed a single token \$CURRENT_DATE to be used. In 2.0 full expression support has been added too greater power and control of the final labels.

Una etiqueta con una expresión como:

    This was printed on: [% format_date( $now, 'dd.MM.yyyy')%]
    
será evaluado al momento de impresión (y momento de despliegue) para generar:

    This was printed on: 06.09.2013
    
When atlas generation is enabled the currently active features\' attribute values will also be accessible in the expressions allowing such things as:

    Asset ID [% "ID" %] and the Tree Type is [% "TreeType" %]
    
![image23](images/2013-09-06_09_53_30-Composer_1.png)
### Característica: Auto ajustar líneas
Tener elementos de mapa bien alineados es fundamental para hacer buenos mapas impresos. Se han agregado líneas de ajuste automático para permitir una fácil alineación del objeto en el compositor simplemente arrastrando un objeto cerca de otro.

![image24](images/2013-09-05_10_05_01-Composer_1.png)
### Característica: Ajuste Manual de Líneas
A veces necesita alinear objetos a una distancia determinada en el compositor. Con las nuevas líneas de ajuste manual, puede agregar líneas de ajuste manual que permiten alinear mejor los objetos utilizando una alineación común. Simplemente arrastre desde la regla superior o lateral para agregar una nueva línea guía.

![image25](images/2013-09-05_10_09_41-Composer_1.png)
### Característica: Generación de series de mapa
¿Alguna vez has necesitado generar una serie de mapas? Por supuesto que si. El compositor ahora incluye la generación de series de mapas incorporadas utilizando la función de atlas. Las capas de cobertura pueden ser puntos, líneas, polígonos, y los datos del atributo de la característica actual están disponibles en las etiquetas para el reemplazo del valor al vuelo.

![image26](images/Picture1.png)
### Prestación: Soporte de resumen automático en el marco del mapa
Necesita mostrar el área actual del marco del mapa principal en una ventana de vista general más pequeña. Ahora usted puede. El marco del mapa ahora contiene la capacidad de mostrar las extensiones de otros y se actualizará cuando se mueva. Usar esto con la función de generación de atlas ahora núcleo en el compositor permite cierta generación de mapas rápidos. El estilo de marco general utiliza el mismo estilo que un objeto de polígono de mapa normal para que su creatividad nunca se vea restringida.

![image27](images/Picture1_1.png)
### Característica: Mezcla de capa
Layer blending makes it possible to combine layers in new and exciting ways. While in older versions, all you could do was to make the layer transparent, you can now choose between much more advanced options such as \"multiply\", \"darken only\", and many more.

Blending can be used in the normal map view as well as in print composer. For a short tutorial on how to use blending in print composer to make the most out of background images, see [\"Vintage map design using QGIS\"](http://anitagraser.com/2013/07/29/vintage-map-design-using-qgis/).

![image28](images/printcomposer_blending_1.png)
### Característica: Soporte etiqueta HTML
Se ha agregado soporte HTML para el elemento de etiqueta del compositor de mapas para darle aún más control sobre sus mapas finales. Las etiquetas HTML admiten hojas de estilos CSS completas, HTML e incluso JavaScript si así lo desea.

![image29](images/html.png)
### Característica: Leyenda multicolumna del diseñador
La leyenda del compositor ahora admite varias columnas. La división de una sola capa con muchas clases en varias columnas es opcional. Las capas de símbolos individuales ahora se agregan de forma predeterminada como elementos de una sola línea. Se pueden asignar tres estilos diferentes al título de la capa/grupo: Grupo, Subgrupo u Oculto. Los estilos de título permiten la agrupación visual arbitraria de elementos. Por ejemplo, una capa de un solo símbolo puede mostrarse como un elemento de una sola línea o con un título de capa (como en 1.8), los símbolos de las múltiples capas siguientes pueden agruparse en un solo grupo (ocultando títulos), etc. Los recuentos de entidades pueden agregarse a las etiquetas.

![image30](images/multicolumn-legend.png)
### Característica: Actualizaciones al administrador del diseñador de mapa 
Se hicieron las siguientes mejoras a la administración del diseñador de mapa:
- El nombre del compositor ahora se puede definir en el momento de la creación, optando por comenzar desde otros nombres
- Ahora los diseñadores pueden ser duplicados
- `New from Template` and from `Specific` (in Composer Manager) creates a composer from a template located anywhere on the filesystem
- El proyecto padre puede ser guardado ahora directamente desde el espacio de trabajo del diseñador
- Todas las acciones de gestión del diseñador ahora están accesibles directamente desde el espacio de trabajo del diseñador 

![image31](images/changelog-2.0_composer-mngmnt.png)
## Plugins
### Característica: Administrador de complementos renovado
En QGIS 1.x, la administración de complementos era algo confusa con dos interfaces: una para administrar complementos ya instalados y otra para obtener complementos de Python desde un único repositorio de complementos. En QGIS 2.0 presentamos **un nuevo administrador de complementos unificado **que proporciona una *ventana única* para descargar, habilitar/deshabilitar y, en general, administrar sus complementos. ¡Ah, y la interfaz de usuario también es vistosa con pestañas laterales e iconos fáciles de reconocer!

![image32](images/Plugin_Manager_024.png)
## Programabilidad
### Característica: Nueva consola Python
La nueva consola Python te da aún más potencia. Ahora con soporte de autocompletado, resaltado de sintaxis, configuración de fuente ajustable. El editor de código lateral permite una entrada más fácil de bloques de código más grandes con la capacidad de abrir y ejecutar cualquier archivo Python en la sesión QGIS.

![image33](images/pyconsole.png)
### Prestación: Aún más funciones de expresión
Con el motor de expresión cada vez más utilizado a través de QGIS para permitir cosas como etiquetas y símbolos basados en expresiones, se han agregado muchas más funciones al generador de expresiones y todas son accesibles a través del generador de expresiones. Todas las funciones incluyen ayuda integral y guías de uso para facilitar su uso.

![image34](images/2013-09-06_09_10_49-Expression_based_label.png)
### Prestación: Funciones de expresión personalizadas
If the expression engine doesn\'t have the function that you need. Not to worry. New functions can be added via a plugin using a simple Python API.

![image35](images/2013-09-06_09_14_58-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Característica: Nueva API Python más limpia
La API de Python se ha modernizado para permitir una experiencia de programación más limpia y más pythonica. La API QGIS 2.0 usa SIP V2 que elimina la lógica toString(), toInt() que era necesaria cuando se trabajaba con valores. Los tipos ahora se convierten en tipos nativos de Python para una API mucho mejor. El acceso a los atributos ahora se realiza en la propia función utilizando una simple búsqueda de claves, no más búsquedas de índice y mapas de atributos.

    >>> feature['mycolumn'] = 10
    >>> feature['mycolumn']
    10
    
La forma en que se leen las características de una capa también se ha mejorado, lo que permite el subprocesamiento múltiple en futuras versiones.

    for feature in layer.getFeatures():
           print feature['mycolumn']
    
![image36](images/2013-09-06_09_28_08-untitled__routing_-_Sublime_Text_UNREGISTERED.png)
### Característica: Compatibilidad de código con lanzamientos versión 1.x
As this is a major release, it is not completely API compatible with previous 1.x releases. In most cases porting your code should be fairly straightforward - you can use [this guide](https://github.com/qgis/QGIS/wiki/Python_plugin_API_changes_from_18_to_20) to get started. Please use the developer mailing list if you need further help.

![image37](images/Selection_021.png)
### Característica: Macros de proyecto Python
Un módulo de Python, guardado en un archivo project.qgs, se puede cargar y ejecutar funciones específicas en los siguientes eventos del proyecto:
- `openProject()`
- `saveProject()`
- `closeProject()`

Se puede configurar si los macros se ejecutarán en las opciones de aplicación.

![image38](images/changelog-2.0_project-macros_w-setttings.png)
## Simbología
### Prestación: Propiedades definidas por datos
Con las nuevas propiedades definidas de datos, es posible controlar el tipo de símbolo, tamaño, color, rotación y muchas otras propiedades a través de atributos de características.

![image39](images/datadefinedproperties2.png)
### Característica: Administración mejorada de capa símbolo
La nueva descripción general de la capa de símbolos utiliza un diseño claro y estructurado en árbol que permite un acceso fácil y rápido a todas las capas de símbolos.

![image40](images/symbollayertree.png)
### Característica: Soporte de transparencia para definiciones de color
In most places where you select colours, QGIS now allows you to specify the alpha channel (which determins how transparent the colour should be). This allows you to create great looking maps and to hide data easily that you don\'t want users to see.

![image41](images/Layer_Properties_-_nat_026_1.png)
### Característica: Control de color para capas ráster
QGIS 2.0 allows you to precisely control exactly how you\'d like raster layers to appear. You now have complete control over the brightness, contrast and saturation of raster layers. There\'s even options to allow display of rasters in grayscale or by colorising with a specified color.

![image42](images/Layer_Properties_-_blue_marble_032.png)
### Característica: Copiar simbología entre capas
Its now super easy to copy symbology from one layer to another layer. If you are working with several similar layer, you can simply `right-click` on one layer, choose `Copy Style` from the context menu and then `right-click` on another layer and choose `Paste-Style`.

![image43](images/Selection_034.png)
### Característica: Guardar estilos en su base de datos
Si está utilizando una base de datos almacén de datos vectoriales, ahora puede almacenar las definiciones de estilo de capa directamente en la base de datos. Esto facilita compartir capas con estilo en un entorno empresarial o multiusuario.

![image44](images/Selection_037.png)
### Feature: Colour ramp support
Colour ramps are now available in many places in QGIS symbology settings and QGIS ships with a rich, extensible set of colour ramps. You can also design your own and many [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) themes are included in QGIS now \'out of the box\'. Color ramps even have full support for transparency!

![image45](images/Selection_038.png)
### Característica: Defininir estilos predeterminados personalizados para todas los tipos de capas
Now QGIS lets you control how new layers will be drawn when they do not have an existing `.qml` style defined. You can also set the default transparency level for new layers and whether symbols should have random colours assigned to them.

![image46](images/Screen_Shot_2013-09-12_at_11.18.52_PM.png)
## Interfaz de usuario
### Característica: Nuevo tema de ícono
We have updated out icon theme to use the \'GIS\' theme which introduces an improved level of consistency and professionalism to the QGIS user interface.

![image47](images/Selection_001_1.png)
### Característica: Pestañas en lados, grupos que colapsan
Hemos estandarizado el diseño de las pestañas e introducido cuadros de grupo plegables en muchos de nuestros cuadros de diálogo para facilitar la navegación por las diferentes opciones y hacer un mejor uso del espacio de la pantalla.

![image48](images/Selection_005.png)
### Característica: Notificaciones moderadas
In many cases we want to tell you something, but we don\'t want to stop your work or get in your way. With the new notification system QGIS can let you know about important information via a yellow message bar that appears at the top of the map canvas but doesn\'t force you to deal with it if you are busy doing something else. Programmers can create these notification (e.g. from a plugin) too using our python API.

![image49](images/Selection_030.png)
### Característica: Fuente de letras personalizada y stylesheet Qt de la aplicación
The system font used for the application\'s user interface can now be set. Any C++ or Python plugin that is a child of the QGIS GUI application or has copied/applied the application\'s GUI stylesheet can inherit its styling, which is useful for GUI fixes across platforms and when using custom QGIS Qt widgets, like `QgsCollapsibleGroupBox`.

Se puede acceder a la hoja de estilo de la aplicación GUI QGIS generada para la plataforma actual después del lanzamiento(en PyQGIS):

    qgis.utils.iface.mainWindow().styleSheet()
    
![image50](images/changelog-2.0_app-font.png)
### Característica: Diálogos y botones del seleccionador vivo de color
Every color chooser button throughout the interface has been updated to give visual feedback on whether the current color has a transparent, or \'alpha,\' component. The color chooser opened by the new color buttons will now always be the default for the operating system. If the user has `Use live-updating color chooser dialogs` checked under `Options -> General -> Application`, any change in the color chooser will immediately be shown in the color button and for any item currently being edited, where applicable.

![image51](images/changelog-2.0_live-color-dlgs.png)
### Característica: Anotaciones SVG
Con QGIS 2.0 ahora puede agregar anotaciones SVG a su mapa, ya sea ancladas a un lugar específico o en una posición relativa sobre el canvas.

![image52](images/Screen_Shot_2013-09-14_at_9.39.11_AM.png)
### Característica: Constructor de formas con arrastrar y soltar 
QGIS 2.0 admite un gran sistema nuevo para crear formularios de entrada de datos. Con el diseñador de formularios de arrastrar y soltar, puede crear formularios de aspecto inteligente con pestañas para agrupar campos comunes. Ahora es mucho más fácil controlar la experiencia de entrada de datos para sus usuarios.

![image53](images/Screen_Shot_2013-09-14_at_2.17.27_PM.png)
### Característica: Herramienta de acción predeterminada
Si es usuario de acciones de capa vectorial (pequeñas tareas que se pueden ejecutar al hacer clic en una función), le encantará la nueva herramienta de acción en la barra de herramientas. Con él, puede seleccionar una acción activa y luego hacer clic en sus entidades para invocar esa acción.

![image54](images/Screen_Shot_2013-09-14_at_2.27.03_PM.png)

{{<content-end >}}
