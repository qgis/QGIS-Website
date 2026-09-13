---
HasBanner: false
draft: false
releaseDate: '2023-03-04'
section: proyecto
sidebar: true
title: Registro de cambios de QGIS 3.30
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios de QGIS 3.30{#changelog330 }
![image1](images/projects/af9e5405a8329d7de8959238a3d499da780c1598.png)

Fecha de lanzamiento: 2023-03-04

The 3.30 \'s-Hertogenbosch release of the groundbreaking QGIS project introduces a wide range of changes and optimizations from the QGIS developer community.

The splash screen features a fragment of the "Gemeentekaart", or Municipality map, of \'s-Hertogenbosch from 1867. It is part of a series of 1200 maps of all the communities in The Netherlands from that time, which were published in an atlas for each of the 11 regions. All maps were drawn in the same size, although for large municipalities a double format was used and scaled to match the page. The series was internationally rewarded because of its accuracy and completeness. The map was drawn by Jacob Kuyper (1821-1908), the most famous geographer and cartographer of his time in The Netherlands. Text and splash map image provided by [atlasandmap.com](https://atlasandmap.com)

La integración nativa de GeoNode también se ha migrado a un complemento externo, aprovechando las potentes extensiones de la API de QGIS para complementos implementados en versiones recientes.

Los usuarios también pueden esperar nuevas funcionalidades y mejoras en la experiencia de usuario, como compatibilidad con tablas de atributos ráster, ordenación inteligente y configurable para la carga de capas, mejoras en las utilidades GPS, widgets de formularios más dinámicos, previsualización nativa de medios enriquecidos para archivos adjuntos, mejor integración con servicios en la nube, ampliaciones de los estándares de metadatos de QGIS y otras muchas novedades dignas de mención.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://www.youtube.com/watch?v=q7O819lFKc4>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/q7O819lFKc4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

QGIS is a community effort, and we would like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise contribute towards making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large or small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://qgis.org/en/site/about/sustaining_members.html) for more details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug-fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es software libre y no hay obligación de pagar nada por utilizarlo; de hecho, queremos animar a todo el mundo a que lo use, independientemente de su situación económica o social. Creemos que dotar a las personas de herramientas para la toma de decisiones espaciales redundará en una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Cambios que eliminan funcionalidades
### Novedad: Baja de retrocompatibilidad para simbología con QGIS 3.16 y anteriores.
Las versiones anteriores de QGIS escribían cantidades significativas de objetos de compatibilidad en la estructura XML de los archivos de proyecto para mantener la compatibilidad con simbologías anteriores y permitir que los archivos de proyecto se abrieran con QGIS 3.16 y versiones anteriores. Esta compatibilidad se ha eliminado de futuras versiones.

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
## Herramientas de mapa
### Prestación: Consejos para mapas rasterizados
en versiones anteriores, MapTips sólo estaba disponible para capas vectoriales, pero nuevos cambios en la API han hecho posible implementar MapTips para otros tipos de capas.

Las capas raster son ahora compatibles con MapTips, y se han añadido nuevas funciones de utilidad de expresión para ampliar las capacidades existentes de MapTips:
- `map_to_html_table`: converts a map (key-value pair data structure) to an HTML table
- `map_to_html_dl`: converts a map (key-value pair data structure) to an HTML definition list
- `raster_attributes`: creates a map with the fields names as keys and the raster attribute table values as values from the attribute table entry that matches the given raster value
- a new \"Map Layer Position\" expression scope that defines a variable `@layer_cursor_point` with the layer coordinates (in the layer\'s CRS) under the mouse position

![image3](images/entries/7cc33f0191d7461c103eef9eb792495d4b298dd6.webp)

Esta prestación ha sido financiada por NOAA OCS Hydrography

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestaciones: Identificar al mover el ratón, sin hacer clic
Una nueva opción permite activar la herramienta de identificación al mover el ratón, sin necesidad de hacer clic en el lienzo.

This option behaves almost identically to the default identify option, with the difference being that the user doesn\'t need to click or use a keyboard shortcut to trigger the identify action. This allows the identify tool to function similar to the MapTips utility, whilst providing users with the benefits of the identify tool such as support for multiple layer types and derived information.

El disparador por defecto es un temporizador de 300 milisegundos que ejecutará la acción de identificar, que se implementa para evitar problemas de rendimiento al mover el ratón.

![image4](images/entries/36bfbae2b85c46b304ea84c05ce819fd69a66d38.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Interfaz de usuario
### Prestación: Funcionalidad basada en restricciones para tablas de atributos
En la tabla de atributos se han expuesto nuevos filtros de prestaciones de estilo condicional basado en restricciones y restricciones que fallan.

Esta funcionalidad proporciona opciones de filtrado para ver u ocultar las prestaciones que no cumplen las restricciones (duras o blandas), e introduce un nuevo tipo de estilo condicional que funciona junto con los tipos de fila y campo preexistentes para resaltar las prestaciones que no cumplen las restricciones de capa.

![image5](images/entries/4ad89600c1e78bca863927f30581319b86afe6f1.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Panel de información GPS y campos de la barra de herramientas adicionales
El panel de información GPS incluye ahora la longitud total actual de la ruta y la distancia desde el inicio de la ruta. Estas prestaciones también están disponibles como una opción (no activada por defecto) que permite mostrarlas en la etiqueta de información de la barra de herramientas GPS.

El panel de información GPS también incluye la altitud elipsoidal en los valores de información GPS disponibles.

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: UX y refactorización del panel de información GPS
Se ha llevado a cabo una remodelación sustancial del panel de información GPS con el fin de simplificar el manejo del GPS por parte del usuario dentro de QGIS y proporcionar una experiencia GPS más ágil.

Previously, **all** application-level GPS functionality was exposed through a single GPS \"Information\" panel interface, which included GPS connection settings, digitizing from GPS, and the actual display of GPS information. This interface became cluttered and difficult to use

La funcionalidad GPS se ha dividido en distintas partes:
1. Los ajustes GPS a nivel de aplicación, que raramente se modifican, están presentes en la pestaña GPS del menú Opciones dentro de Ajustes de QGIS.
2. A new floating \"GPS Toolbar\" has been added, which contains the most commonly used GPS-related operations.
3. The final action in the GPS Toolbar opens a \"GPS settings\" popup, that contains various settings that are expected to be modified mid-session and are expected to be more readily accessible.
4. The GPS information widget has been redesigned to show only GPS **information**. Specifically, only the \"information\" and \"signal\" tabs remain. The GPS information widget still contains a shortcut to the connect/disconnect action, and also a settings button that exposes the same GPS settings menu as is used in the GPS toolbar.

La clase del widget de información del GPS es ahora responsable ÚNICAMENTE de mostrar la información del GPS en el panel, y se han creado nuevas clases dedicadas para manejar la digitalización desde el GPS, la nueva barra de herramientas del GPS, y los ajustes del GPS en consecuencia.

![image6](images/entries/206ae34a728a37cae967f60887b5a7f2bbd94c0f.webp)

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Simbología
### Prestación: Opciones de exportación de SLD mejoradas
Se ha desarrollado una nueva extensión de la API de exportación de Styled Layer Descriptor (SLD) que existe en paralelo con las opciones de exportación de SLD existentes, pero que proporciona una funcionalidad adicional para el control granular de las exportaciones de SLD.

Este desarrollo incluye la exportación de estilos de capas poligonales complejas como símbolos gráficos externos que se almacenan junto con el SLD exportado.

![image7](images/entries/cce332a4adc8cc7a24ead53acd8924431f1085f2.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Representación
### Prestación: Sombreado global del terreno del mapa
Ahora los usuarios pueden aplicar al mapa un efecto de sombreado global del terreno, basado en la elevación de *todas* las capas activas que admiten elevación, incluida :
- Raster layers (if \"Represent elevation Surface\" is checked in the layer properties)
- Capas de malla
- Capas de nubes de puntos.

Se combinan los valores de elevación en una posición determinada de todas las capas pertinentes, y la elevación considerada se elige en función de uno de los dos métodos definidos por el usuario:
- La mayor elevación se considera
- Se considera la elevación de la capa superior del árbol de capas

Actualmente, los métodos de sombreado aplicados son la iluminación Eye Dome y el efecto de sombreado de colinas.

Los ajustes de sombreado de elevación se exponen a la interfaz de usuario en los siguientes controles:
- En las propiedades del proyecto, en la misma pestaña de los ajustes de elevación del proyecto
- En el panel de estilo de capas, se ha creado una nueva pestaña para definir los ajustes globales de sombreado del terreno

![image8](images/entries/e75c69fb42f1916ceaf4b30f589154dc47881c6f.webp)

This feature was funded by [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Prestación: Añadir soporte superíndice y subíndice para el renderizador de texto
Los elementos de texto de QGIS admiten ahora superíndices y subíndices.

Esto permite:
- `<sup>superscript</sup>` / `<sub>subscript</sub>` components in text, where the text will be vertically super or subscript aligned and automatically sized to 2/3rd of the parent font size. Users can also set a fixed font size for the super/subscript by including the relevant CSS rules in their HTML, e.g. `<sup style="font-size:33pt">super</sup>`
- `vertical-align: super` or `vertical-align: sub` CSS formatting rules in any other HTML element

![image9](images/entries/24e510e32b919b373d09e5fe8536cfc0dfd0d66e.webp)

Esta prestación ha sido financiada por OSGEO UK.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Objetos 3D
### Prestación: Limitación de la extensión 2D de la escena 3D
La extensión renderizada de una escena 3D puede ahora limitarse a las prestaciones que intersecan una extensión 2D especificada por el usuario.

La forma en que se limitan los objetos espaciales renderizados depende del tipo de capa de datos de origen:
- Los terrenos planos, DEM y en línea se *recortan* en la extensión especificada
- Las capas de nubes de puntos *sólo cargan puntos dentro* de la extensión especificada
- Las capas vectoriales *sólo cargan las prestaciones que intersectan* la extensión especificada

El filtrado de objetos espaciales basado en la extensión en capas de malla está aún en fase de desarrollo.

![image10](images/entries/a8135c9cfcaa91fdc540512f36cf276a2cdb4f02.webp)

This feature was funded by [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

This feature was developed by [Stefanos Natsis](https://github.com/uclaros)
### Prestación: Control mejorado de la cámara
Hay un par de mejoras que mejoran la experiencia del usuario:
- Elevation range is taken into account when \"Zoom full\" is used (users should not end up \"behind\" their scene anymore)
- Mueva la cámara verticalmente usando Ctrl + Mayús + Botón izquierdo del ratón
- Permitir zoom con la rueda mientras se mueve el ratón
- Continuar el zoom con el botón derecho del ratón cuando el puntero sale de la ventana gráfica

This feature was funded by [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Diseño de impresión
### Prestación: Gestor de accesos directos en diseños de impresión
El gestor de atajos, accesible desde el menú de configuración de la interfaz principal de QGIS, permite a los usuarios configurar y anular los atajos de teclado existentes y admite métodos definidos por el usuario para ejecutar acciones de QGIS.

Ahora se ha añadido un cuadro de diálogo de configuración del administrador de teclado similar a la interfaz de diseño de impresión para mejorar la productividad.

![image11](images/entries/ce065abd5dfe0a678e461a12e0efef92c5acaae3.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Prestación: Uso del renderizador de texto en las leyendas de diseño
Este cambio permite utilizar las funciones del renderizador de texto completo para los títulos de las leyendas, los subtítulos y el texto de los artículos.

Permite configurar los buffers, las sombras, el control del espaciado entre fuentes y otras opciones disponibles (incluido el formato HTML mixto) que se permiten utilizar en los formatos de texto.

Esta prestación ha sido financiada por NIBIO

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Expresiones
### Feature: Add feature_id() function
A new `feature_id($feature)` expression function now allows for retrieving the feature ID of a feature object.

The function accepts one argument which must be a feature object. Accordingly, this function can be used with the results of any other function which returns feature objects, such as \"get_feature\", \"overlay\_\*\", etc.

![image12](images/entries/6536913b10d68dded9a54bc58ba003b821b100f6.webp)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New is_feature_valid() and is_attribute_valid() functions
New `is_feature_valid()` and `is_attribute_valid()` functions are provided in QGIS expressions. Both functions validate a feature or attribute, based on the constraints attached to fields for a given vector layer. This enables users to leverage the select-by-expression utility to locate features that have unmet constraints. In addition, users can now use the rule-based renderer to provide visual feedback through symbology indicating the constraint validity state of rendered features.

![image13](images/entries/f6a73012edcc84033d40e91bc6216365fd4f5ae6.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Feature: Add x_at, y_at, z_at, m_at expression functions
The available \$functions are considered deprecated (\$x_at`and`\$y_at\`), and instead of operating on the current feature geometry the functions instead support a feature geometry as arguments.

Los cambios para estas expresiones incluyen la creación de funciones similares para otras medidas geométricas. Estas nuevas funciones incluyen:
- x_at(geometry, i)
- y_at(geometry, i)
- z_at(geometry, i)
- m_at(geometry, i)

This feature was funded by [Métropole Européenne de Lille](https://www.lillemetropole.fr/)

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
## Administración de datos
### Prestación: Edición del campo DateTime: segregación del formato de visualización y del formato del valor del campo
Los esfuerzos por mejorar la gestión de la información de los campos de fecha y hora incluyen la definición explícita del formato de localización para la *visualización* de los campos de fecha y hora, al tiempo que se garantiza que la edición, captura y almacenamiento de los valores de los campos se ajusta a las normas internacionales de formato de hora.

This feature was funded by [3liz](https://3liz.com)

This feature was developed by [rldhont](https://github.com/rldhont)
### Prestación: Añadir la opción de registrar directamente puntos y trazas GPS en un Geopackage o Spatialite db
When activated in the GPS toolbar settings, the \"Log to Geopackage/Spatialite\" action will prompt the user to select an existing GPKG or SpatiaLite file, or enter a new file name. A \"gps_points\" and \"gps_tracks\" table will be created in the file with a predefined structure.

All incoming GPS messages will be logged to the gps_points layer, along with speed/bearing/altitude/accuracy information from the GPS.

When the GPS is disconnected (or QGIS is closed), the entire recorded GPS track will be added to the gps_tracks table, along with some calculated information like track length, and start and end times)

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: Add an explicit \"Offset from UTC\" option for storing GPS feature timestamps
Esta opción permite a los usuarios introducir manualmente un desfase deseado con respecto a UTC para almacenar las marcas horarias GPS. Esto permite una flexibilidad total para los usuarios que necesitan tener en cuenta las compensaciones de ahorro de luz diurna u otras cuestiones complejas de zona horaria.

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Compatibilidad con tablas de atributos ráster (RAT)
QGIS incluye ahora una amplia compatibilidad con las tablas de atributos ráster (RAT).

Estas actualizaciones proporcionan una nueva interfaz de RAT dentro de la API de QGIS, y se ofrece soporte para RAT gestionadas por proveedores de datos ráster (GDAL), así como para archivos de tabla de atributos de valor genérico (VAT), siempre que se almacenen en un archivo auxiliar sidecar DBF.

Much of the functionality from the [Python RAT Plugin](https://github.com/noaa-ocs-hydrography/qgis-raster-attribute-table-plugin) was ported into QGIS to provide native support for RATs, and a new set of GUI operations affords users the following advanced functionalities:
- **Estilización automática de raster**: Si un RAT está disponible al añadir un raster al proyecto e incluye información de estilo, QGIS aplicará los estilos relevantes a la capa raster por defecto. La carga automática funciona tanto para RATs incrustados como para VAT.DBF sidecar con el mismo nombre base del raster.
- **RAT Reclasificación**: La reclasificación de un ráster puede realizarse seleccionando una columna diferente
- **RAT Identificar**: Los valores de la fila RAT correspondientes al valor del píxel en cuestión se muestran en la herramienta Mapa de identificación.
- **RAT properties**: A new \"Attribute Table\" tab is available from the raster layers property window
- **RAT Edición**: Las RAT ofrecen funciones básicas de edición
- **RAT Creación a partir de la clasificación actual**: Las RAT pueden crearse a partir de estilos de paleta o pseudocolor de banda única existentes

A gallery of these functionalities in action is [available on GitHub](https://github.com/qgis/QGIS/pull/50687)

![image14](images/entries/4406611cee132d2bfae92d9ba01681464f333928.gif)

Esta prestación ha sido financiada por NOAA OCS Hydrography

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Metadatos y Metabúsqueda
### Prestación: Añadir fechas clave a los metadatos de capas y proyectos
Se han añadido los siguientes campos al estándar de metadatos de capas/proyectos de QGIS:
- Fecha de creación
- Fecha de publicación
- Fecha revisada
- Fecha reemplazada

En versiones anteriores, los metadatos de capa no tenían campos de fecha, mientras que los metadatos de proyecto sólo incluyen el campo de fecha de creación

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Widgets y Formularios
### Prestación: Admite adjuntar atributos multimedia audiovisuales
La nueva funcionalidad introduce soporte multimedia para el widget de recursos externos, lo que permite a los usuarios reproducir archivos multimedia de audio y vídeo en el visor de archivos adjuntos.

This change includes additional configuration options for external resources, with two new items in the integrated viewer type combo box. The video type will take into consideration the height set by the user. If it\'s left to auto, the video widget will grow to fill available space.

This functionality includes the development of the `QgsMediaWidget` object into the QGIS API for extended multimedia support.

![image15](images/entries/75fcba5750d9ce4bb1b7ad41089dd39fd11ae827.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Estado editable definido por datos para widgets de formulario
The \"Editable\" checkbox status can now be controlled through an expression, the expression supports the \"form\" context, meaning that it can use `current_value( '<field_name>' )` to dynamically change the editable status according to changes to other fields in the form.

![image16](images/entries/ce2bc7938c4c5f28d3f0d872e9045c856ef79ef1.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Widget espaciador para arrastrar y soltar formularios de atributos
Se proporciona un nuevo widget de espaciador, con la opción de dibujar una línea horizontal, que ofrece a los usuarios un mayor grado de control sobre cómo se presentan los formularios para los usuarios finales y amplía la funcionalidad para mejorar la experiencia del usuario con interrupciones temáticas y una alineación mejorada.

El widget se representa como un espacio en blanco en el formulario, lo que crea una separación manual entre otros objetos del formulario.

When the \"Draw line\" option is set in the configuration it will fill the vacant space with a line in a manner similar to the horizontal rule, or `<hr>` tag in html.

![image17](images/entries/72c262227fb339abd30833edc712ead25d943044.webp)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Dynamic text widgets with current_value support
Text widgets now support dynamic configuration based on the values of fields present in the current form context by providing a `current_value()` function which may be evaluated within a `QLabel` object.

Using the `current_value( '<field_name>' )` expression will evaluate and update the form when the form field value changes.

![image18](images/entries/6de3cc5d5a6d002fd014717e57f251ec9b0147d9.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Feature: Dynamic HTML widgets with current_value support
HTML widgets now support dynamic configuration based on the values of fields present in the current form context by providing a `current_value` function.

Using the `current_value( '<field_name>' )` expression will evaluate and update the form when the form field value changes.

![image19](images/entries/f04157ac77cf00862595f8b75707c8126e121ce4.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Múltiples selecciones con filtrado en el widget de relación de valores
The Value Relation widget previously ignored \"Use completer\" option when \"Allow multiple selections\" was enabled. Now these two options work together and there is a search box present at the top of the table, allowing filtering of values. When \"Use completer\" option is not enabled, the search box is not shown as before.

![image20](images/entries/3ec355e558ca705d17be8f21c79c613d1022630a.gif)

This feature was funded by [QGIS Norway](http://www.qgis.no/)

This feature was developed by [Stefanos Natsis (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Leyenda de capa
### Prestación: Nuevas mejoras en la ordenación de capas
Ya están disponibles en QGIS nuevas opciones para los métodos configurables de inserción de árboles de capas y la clasificación automatizada de las capas añadidas mediante las funciones de arrastrar y soltar.

El comportamiento anterior era que QGIS siempre cargaba nuevas capas por encima de la capa activa en ese momento.

Se han proporcionado nuevas opciones para permitir un mayor control de cómo se añaden nuevas capas a los proyectos:
- (Siempre) En la parte superior del árbol de capas
- Optimal index/position within the currently active layer\'s group

El índice óptimo intentará ordenar de forma inteligente las capas por tipo (por ejemplo, puntos sobre áreas, etc.) y ofrecerá una experiencia significativamente mejorada a los nuevos usuarios.

Además, las capas añadidas mediante arrastrar y soltar se añadirán al árbol de índice de capas en la ubicación del cursor cuando se suelte para garantizar que la capa se renderiza de forma predecible e intuitiva.

![image21](images/entries/a2f44bdf5df6e8b33dc71c975cbb9c01cfa4845c.webp)

This feature was funded by [Funded by the QGIS user group Switzerland](https://www.qgis.ch/)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Procesado
### Prestación: Opciones adicionales para la exportación de mosaicos XYZ cuando se utiliza la salida html de Leaflet.
Se han expuesto tres nuevos parámetros avanzados opcionales para el algoritmo de generación de teselas XYZ:
- Título de salida de Leaflet HTML
- Atribución de salida de Leaflet HTML
- Incluir mapa base de OpenStreetMap en la salida de LeafletHTML

![image22](images/entries/a96f4972c9664c8887220b0a218103c053050e71.webp)

This feature was developed by [Björn Hinkeldey](https://github.com/pathmapper)
### Feature: Support data defined parameter values when using qgis_process tool
While many processing algorithms supported data-defined parameter values, these were not possible to specify when using the qgis_process tool (or when representing algorithm settings as JSON and qgis_process commands), introducing limitations for utilizing QGIS within command line processing operations.

A new syntax is now provided to allow the specification of data-defined parameter values when running qgis_process operations, and copying the algorithm settings from QGIS will now correctly handle data-defined values.

Command line arguments are specified with the `expression:` prefix within an encapsulated string, whilst the JSON definition is implemented using an expression object with a `data_defined` type definition. Note that special characters within the expression will need to use the appropriate escape characters relevant to the context in which they are used.

Considering the expression `@variable*"field_name"*to_int('2')/100` for the following examples, the command-line syntax would be:

    --PARAMETER='expression:@variable*"field_name"*to_int('\''2'\'')/100'
    
Mientras que la representación JSON sería:

    "inputs": {
      "PARAMETER": {
        "expression": "@variable*\"field_name\"*to_int('2')/100",
        "type": "data_defined"
      },
      "OUTPUT": "TEMPORARY_OUTPUT"
    }
    
Esta prestación ha sido financiada por el Instituto de Investigación sobre la Naturaleza y los Bosques del Gobierno flamenco.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Feature: New \"load_layer\" function
A new `load_layer` expression function has been made available (exclusively for Processing expressions for the time being), which allows the loading of a map layer using a source string and provider name.

Está diseñado para permitir el uso de las funciones de expresión que hacen referencia directa a las capas del mapa (como las funciones de agregación) con una ruta de capa codificada.

This permits the usage of these functions to be used outside of a project (such as via the qgis_process tool) and perform operations such as utilizing complex aggregate functions in the refactor fields algorithm via the qgis_process utility without creating a temporary project for data manipulation.

Esta prestación ha sido financiada por el Instituto de Investigación sobre la Naturaleza y los Bosques del Gobierno flamenco.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Se añade una interfaz de usuario para la definición de la extensión en la calculadora GDAL Raster.
The GDAL Raster Calculator now includes an interface for user-specified extent definition, so that users no longer have to specify the `--extent` criteria in advanced options.

This feature was developed by [Nicolas Godet](https://github.com/nicogodet)
## Opciones de Aplicación y Proyecto
### Prestación: Añadir la opción de almacenar el componente GPS seleccionado en los valores M de la geometría
This new setting, available from the GPS settings panel, allows users to opt into creating geometries with M values from the inbuilt GPS logging tools. This applies to both features digitized from GPS logs, and from the new \"Log to GeoPackage/SpatiaLite\" functionality.

Las opciones incluyen el almacenamiento de marcas de tiempo (como milisegundos desde la época), velocidad sobre el terreno, altitudes, rumbos y componentes de precisión como valores m.

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Hacer que la capa de destino de la pista GPS sea una elección explícita del usuario, recordar en el proyecto
En versiones anteriores, la capa de destino para las prestaciones digitalizadas por GPS recién creadas siempre seguía la selección de capa actual. Esto hacía muy difícil diseñar proyectos en torno a la digitalización GPS, ya que cada vez que un usuario empezaba a interactuar con el proyecto, las prestaciones GPS capturadas se colocaban de forma impredecible dentro de las capas disponibles.

La capa de destino de los objetos espaciales GPS es ahora una elección explícita del usuario. Un usuario puede establecer esta capa, y luego seguir adelante e interactuar con el resto de las capas de su proyecto y tener la garantía de que cada vez que pulse las acciones para crear objetos espaciales GPS estos objetos espaciales se pondrán en la capa correcta. La capa de destino se almacena en el proyecto actual, por lo que al reabrir un proyecto anterior se restablecerá automáticamente la capa de destino GPS (lo que también facilita al personal o a los guionistas crear proyectos de digitalización GPS por adelantado para otros usuarios y tener la seguridad de que funcionarán correctamente sobre el terreno).

Otras mejoras son:
- Ahora, la capa de destino GPS se puede editar automáticamente cuando se crea un objeto espacial, y el usuario recibe una notificación al respecto. De este modo se sigue el enfoque que utilizamos para las herramientas de etiquetado interactivo y se evita la frustración del usuario cuando antes no se guardaban las prestaciones sin ninguna orientación sobre el motivo.
- Las acciones de la barra de herramientas GPS ahora siguen de forma más inteligente el estado del proyecto, el GPS y el seguimiento GPS actual, de modo que las acciones sólo se activan cuando tienen sentido.
- Mejoras en la interfaz de usuario y mejores consejos de herramientas

![image23](images/entries/9563911d7eeb4412cd32f237969579aa1ed6aa90.gif)

Esta prestación ha sido financiada por NIWA

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Gráficos de Perfil
### Prestación: Nuevo elemento de lienzo de perfil de elevación para QGIS Quick
A new elevation profile canvas item is available for [QGIS Quick](https://api.qgis.org/api/qgsquick.html), allowing the elevation profile tools to be used in other cross platform and mobile QGIS applications.

![image24](images/entries/f870a9112a3577742c6f8c6a98b142b23145d525.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Trazados de perfiles de elevación en diseños de impresión
It is now possible to include profile plots in print layouts! There is a new \"Add Elevation Profile\" button in the toolbar which will initially create an empty plot. A plot can be initialized by clicking \"Copy From Profile\" button in the properties of the elevation profile item - this will use the active elevation profile from the main window of QGIS.

El perfil de elevación tiene amplias opciones de configuración: puede especificar:
- qué capas incluir
- tolerancia de la curva del perfil
- rangos de las gráficas (distancia/elevación mínima y máxima)
- bordes y colores de la zona del gráfico
- propiedades de los ejes de distancia y elevación: intervalos de las etiquetas, aspecto de las líneas de la cuadrícula, fuentes, etc.

![image25](images/entries/ca6f01c1c76d7cff23ff8d27492734c74b8c3973.webp)

This feature was funded by [QGIS Community Crowdfunding Efforts](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Navegador
### Prestación: Añadir funciones de edición y creación de relaciones de conjuntos de datos en el navegador
Esta funcionalidad permite crear nuevas definiciones de relaciones incrustadas en archivos de bases de datos para ESRI FileGeodatabases, GeoPackage y bases de datos sqlite.

También es posible eliminar y modificar las relaciones existentes, aunque la funcionalidad disponible puede depender de las restricciones del formato real de la base de datos.

![image26](images/entries/2e902df01faff7f71bdfe3854c5b1a38e013e8d8.gif)

Esta prestación ha sido financiada por Provincie Zuid-Holland.

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
## Proveedores de datos
### Prestación: Eliminación del proveedor GeoNode nativo
The Native GeoNode Provider has been removed from QGIS and is now instead available as a [plugin](https://geonode.org/QGISGeoNodePlugin/).

This change is due to the extension of plugin APIs to support the necessary functionalities, such as the data source manager, and was executed in line with [QEP 262](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/262).

This feature was developed by [Giovanni Allegri](https://github.com/giohappy)
### Prestación: En el gestor de fuentes de datos, permita a los usuarios añadir directamente una capa de mosaico XYZ sin tener que crear primero una conexión.
Ahora los usuarios pueden añadir directamente una capa de mosaico XYZ en el gestor de fuentes de datos, sin tener que crear primero una nueva conexión.

Esto permite a los usuarios añadir fácilmente capas XYZ ad hoc a su mapa sin contaminar sus listas de conexiones guardadas.

![image27](images/entries/1e5a07f058db3b16265d94f6e535ac7c79664bcd.gif)

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Registro SQL para el proveedor OGR
Dado que GDAL admite ahora retrollamadas de registro de consultas para capas basadas en SQLite, QGIS aprovecha esta funcionalidad para permitir el registro de consultas en las herramientas de depuración de QGIS.

Está disponible para fuentes de datos SQLite basadas en OGR (SpatiaLite/ GPKG).

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Soporte de almacenamiento en la nube S3
Ahora se admite el almacenamiento en la nube compatible con S3, como AWS S3 y MinIO, como método de acceso y almacenamiento de archivos externos, disponible mediante la interfaz de usuario de almacenamiento externo para el almacenamiento en la nube de archivos adjuntos.

A new QGIS Auth method named \"AWS S3\" has been provided to support connecting to services using the S3 protocol.

Esta prestación ha sido financiada por Métropole Grand Lyon*\*.

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### Prestación: Capas WMTS con escalado automático que tienen en cuenta la resolución
QGIS permite ahora que las capas WMTS tengan en cuenta la resolución de la pantalla del dispositivo, o puntos por pulgada (PPP), y aumenten la resolución del mosaico en pantallas con PPP altos.

Se ha añadido un nuevo cuadro combinado en el nuevo diálogo del servidor WMS y WMTS para la configuración de la relación de píxeles del mosaico WMTS. Esto permite a QGIS manejar automáticamente la escala hacia arriba y hacia abajo de los azulejos recuperados del servicio basado en el DPI renderizado.

Tenga en cuenta que se recomienda activar la transformación suave de los mapas de píxeles cuando esté activada la ampliación automática.

![image28](images/entries/a921de87af46b4774b94bd632e704527f840ea55.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Eliminación del proveedor SAGA no mantenido de las instalaciones de QGIS
This provider has not been maintained and does not work with newer SAGA versions. Users are encouraged to use the 3rd-party \"Processing Saga NextGen\" plugin instead.

After many many years of discussion, it\'s time for the inbuilt provider to go!

This feature was developed by [Nyall Dawson](https://github.com/nyalldawson)
### Prestación: Mejora de la compatibilidad de las capas con tipo de geometría desconocido para el proveedor WFS.
The QGIS WFS provider has been improved to look in the response to the GetCapabilities request (if using WFS 2.0) if the `IsPoint`, `IsCurve`, `IsSurface` extended filter functions are present.

When such a layer is added to the project, a \"Select Items to Add\" dialog box is displayed.

This enables the user to select one or several layers among ones of `NoGeometry`, `MultiPoint`, `MultiCurve`, `MultiSurface`, `GeometryCollection` types.

![image32](images/entries/2068734219e240ca90b22435ca1381f3c8e4b9ef.webp)

This feature was funded by [QGIS-DE user group](https://qgis.de)

This feature was developed by [Even Rouault](https://github.com/rouault)
## Servidor de QGIS
### Feature: QGIS_APPLICATION_FULL_NAME environment variable
This change defines the `QgsApplication::applicationFullName()` method for use with PostgreSQL `application_name` and QGIS Server Logging.

For QGIS Server, the `QGIS_SERVER_APPLICATION_NAME` can be specified instead and will take precedence over the `QGIS_APPLICATION_FULL_NAME` setting.

The value may also be specified in the `/qgis/application_full_name` variable in the QGIS Server config file.

By default, this value will be defined by the value of `QgsApplication::applicationName()+' '+QgsApplication::platform()`.

This feature was funded by [3liz](https://3liz.com)

This feature was developed by [rldhont](https://github.com/rldhont)
### Prestación: Compatibilidad de GeoJSON con WFS DescribeFeatureType
Se ha añadido la compatibilidad con JSON como formato de salida para las solicitudes DescribeFeatureType al servidor WFS de QGIS. Aunque no es una estipulación explícita de las especificaciones WFS, esta funcionalidad permite respuestas que coinciden con otros proveedores de servicios WFS como GeoServer.

This feature was funded by [Kristianstads kommun](https://www.kristianstad.se/)

This feature was developed by [David Marteau](https://github.com/dmarteau)
## Plugins
### Prestación: Activación/desactivación y filtrado de reglas del comprobador de topología
El complemento de comprobación de topología se ha mejorado para ofrecer funciones que permitan una mejor gestión de las reglas, así como el filtrado de grandes conjuntos de errores. Otras mejoras hacen que la experiencia del usuario esté más en línea con las versiones posteriores de QGIS y permiten mejorar la productividad, como la eliminación masiva y la desactivación de reglas.

The topology checker rules dialog now features check boxes which are attached to individual rules, which allow for enabling/ disabling rules when running validity checks *without having to remove them*. This avoids scenarios when users don\'t want to lose rules but are only interested in validating a subset.

El panel del comprobador de topología también cuenta con un nuevo cuadro combinado debajo de su barra de herramientas que permite filtrar rápidamente los errores para que los usuarios puedan centrarse en un tipo de error concreto, aunque seguirá mostrando todos los tipos de error por defecto.

![image29](images/entries/52e54d9f31a12f024d3c452ecbc77fb3278c18e4.webp)

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
## Programabilidad
### Prestación: Mejoras en QgsExifTools
Se ha añadido nueva funcionalidad a la clase QgsExifTools, incluyendo:
- The `readTag()` and `readTags()` functions now support Xmp metadata tags
- A new `tagImage()` function can be used to add individual metadata tags to a given image, which can be used in addition to the pre-existing `geoTagImage()` function

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Actualizaciones del autocompletado inteligente de corchetes para editores de código
Previous releases of QGIS included an `autoCloseBracket` setting for the Python Console, which had a number of limitations in its behavior, including being limited to use within the Python Console and Script Editor interfaces.

Updates to the autocomplete settings extend this functionality to other Code Editor interfaces, such as the Expression Editor, Project Macro Editor, and Script Editor. The `autoCloseBracket` behavior has also been adjusted to better mimic the behavior of modern IDEs, and an `autoSurround` setting has been added to surround selected text when using the following character sets:
- braces/ curly brackets: `{}`
- square/ box brackets: `[]`
- parenthesis/ round brackets: `()`
- double quotation mark: `"`
- single quotation mark: `'`
- backticks: ``\`
- asterisk: `*`

A excepción de los caracteres acento grave y asterisco, la funcionalidad autoCloseBracket está disponible cuando se encapsulan nuevos datos sin una selección de texto activa.

La configuración de autocompletado está activada por defecto en las nuevas versiones, pero se proporciona una nueva interfaz de configuración para que los usuarios puedan realizar un control granular.

![image30](images/entries/2ed531d2789b12d258d1503c8fb74e396f06e63d.webp)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
### Feature: Add \"toggle comment\" action to the integrated python console
Las acciones de comentar y descomentar del Editor de Python incrustado se han sustituido por una acción de alternar comentarios, que ahora también está disponible en el Editor de scripts de procesamiento.

De este modo, la experiencia de usuario del editor está en consonancia con la de otros IDE, como VSCode, que permiten alternar los comentarios.

The default shortcut for this action is set to `Ctrl+:`

The toggle comment action is also available in **Project Macro** and **Expression Editors**, however this is only available using the `Ctrl+:` shortcut and does not include the action button on the UI.

![image31](images/entries/fb255d60095471377459f1c6907df83e6f54bea4.gif)

This feature was developed by [Yoann Quenach de Quivillic](https://github.com/YoannQDQ)
## Correcciones Notables
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Task: take into account GDT_Int8 | [#50907](https://github.com/qgis/QGIS/issues/50907) | [PR #51586](https://github.com/qgis/QGIS/pull/51586) | [PR #51602](https://github.com/qgis/QGIS/pull/51602) |
| Task: take into account GDT_Int8 | [#50907](https://github.com/qgis/QGIS/issues/50907) | [PR #51587](https://github.com/qgis/QGIS/pull/51587) | N/D |
| MultiLineString from OpenFileGDB Disappears on Zoom | [#32534](https://github.com/qgis/QGIS/issues/32534) | [GDAL PR 7137](https://github.com/OSGeo/gdal/pull/7137) |  |
| DATETIME: Zona horaria incorrecta para UTC en la tabla de atributos | [#48393](https://github.com/qgis/QGIS/issues/48393) | [PR #51625](https://github.com/qgis/QGIS/pull/51625) | [PR #51645](https://github.com/qgis/QGIS/pull/51645) |
| distutils está obsoleto pero aún se utiliza | [#51532](https://github.com/qgis/QGIS/issues/51532) | [PR #51630](https://github.com/qgis/QGIS/pull/51630) | [PR #51644](https://github.com/qgis/QGIS/pull/51644) |
| Importación de Datos a una Geodatabase Creada con Archivos de QGIS | [#51435](https://github.com/qgis/QGIS/issues/51435) | <https://github.com/nyalldawson/QGIS/pull/36> | N/D |
| Importación de Datos a una Geodatabase Creada con Archivos de QGIS | [#51435](https://github.com/qgis/QGIS/issues/51435) | [GDAL PR 7147](https://github.com/OSGeo/gdal/pull/7147) | [GDAL PR 7176](https://github.com/OSGeo/gdal/pull/7176) |
| OGCAPI Objetos Espaciales url de colección con punto | [#51663](https://github.com/qgis/QGIS/issues/51663) | [PR #51671](https://github.com/qgis/QGIS/pull/51671) | [PR #51987](https://github.com/qgis/QGIS/pull/51987) |
| CityGML Import no funciona con archivos LoD2 | [#51647](https://github.com/qgis/QGIS/issues/51647) | [GDAL PR 7168](https://github.com/OSGeo/gdal/pull/7168) | N/D |
| Capas rotas al crear una nueva tabla en GPKG creada por terceros | [#51721](https://github.com/qgis/QGIS/issues/51721) | [GDAL PR 7174](https://github.com/OSGeo/gdal/pull/7174) | N/D |
| \"Save Layer Edits\" after \"Add Polygon Feature\" deletes added polygons when the objects have no attributes | [#51247](https://github.com/qgis/QGIS/issues/51247) | [GDAL PR 7184](https://github.com/OSGeo/gdal/pull/7184) | [GDAL PR 7188](https://github.com/OSGeo/gdal/pull/7188) |
| sig transformando coordenadas incorrectamente | [#51792](https://github.com/qgis/QGIS/issues/51792) | [proj PR 3621](https://github.com/OSGeo/PROJ/pull/3621) | N/D |
| Some versions of QGIS can\'t parse mixed-dtype-columns in GeoJSON | [#51911](https://github.com/qgis/QGIS/issues/51911) | Ninguno: sólo investigación e intento de reparación preliminar |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Añadir fila no funciona con columnas de identidad postgres que tienen muchos caracteres | [#51563](https://github.com/qgis/QGIS/issues/51563) | [PR #51641](https://github.com/qgis/QGIS/pull/51641) | [PR #52059](https://github.com/qgis/QGIS/pull/52059) |
| If some layers are not identifyable, QGIS Server WMS \"GetFeatureInfo\" returns LayerNotQueryable | [#51613](https://github.com/qgis/QGIS/issues/51613) | [PR #51646](https://github.com/qgis/QGIS/pull/51646) (tests only, cannot reproduce) | N/D |
| Investigación y diagnóstico sobre: Error o nuevo comportamiento en los valores de los campos por defecto en QGIS 3.28.X | [#51543](https://github.com/qgis/QGIS/issues/51543) | Asked feedback to the original developer of the \"feature\" |  |
| \[ogr provider\] Saving big CSV edit is very slow when the whole file has to be updated (such as adding a new field) | [#51668](https://github.com/qgis/QGIS/issues/51668) | [PR #51686](https://github.com/qgis/QGIS/pull/51686) | [PR #51700](https://github.com/qgis/QGIS/pull/51700) |
| Datos vectoriales - Simbología graduada - Formato de leyenda - Utilice sólo el límite superior | [#51691](https://github.com/qgis/QGIS/issues/51691) | [PR #51692](https://github.com/qgis/QGIS/pull/51692) | [PR #51696](https://github.com/qgis/QGIS/pull/51696) |
| Extraño comportamiento de QgsDoubleSpinbox en simbología graduada con intervalo fijo | [#51687](https://github.com/qgis/QGIS/issues/51687) | [PR #51714](https://github.com/qgis/QGIS/pull/51714) | No |
| Las escalas predefinidas del proyecto se recortan en el separador de miles después de reiniciar/reabrir las propiedades del proyecto | [#51735](https://github.com/qgis/QGIS/issues/51735) | [PR #51749](https://github.com/qgis/QGIS/pull/51749) | [PR #51766](https://github.com/qgis/QGIS/pull/51766) |
| wms getLegendGraphic llama al grupo y no a la capa cuando se añaden muchas capas de estilo desde el navegador | [#51759](https://github.com/qgis/QGIS/issues/51759) | [PR #51765](https://github.com/qgis/QGIS/pull/51765) | No |
| overlay_intersects\' does not work with WFS-layer | [#51492](https://github.com/qgis/QGIS/issues/51492) | [PR #51773](https://github.com/qgis/QGIS/pull/51773) | [PR #51793](https://github.com/qgis/QGIS/pull/51793) |
| multiedit in attribute table not working properly in version \>=3.22 | [#48077](https://github.com/qgis/QGIS/issues/48077) | [PR #51801](https://github.com/qgis/QGIS/pull/51801) | Riesgoso? |
| La restricción de expresión clave/valor no se actualiza | [#51791](https://github.com/qgis/QGIS/issues/51791) | [PR #51804](https://github.com/qgis/QGIS/pull/51804) | [PR #51811](https://github.com/qgis/QGIS/pull/51811) |
| Los campos flotantes creados en ArcGIS se convierten en reales 12, 11 - La precisión es demasiado alta | [#51849](https://github.com/qgis/QGIS/issues/51849) | Won\'t Fix |  |
| La fuente de datos CSV no se convierte correctamente de 3.16 a 3.22 - los proyectos ya no se pueden utilizar. | [#48587](https://github.com/qgis/QGIS/issues/48587) | [PR #51881](https://github.com/qgis/QGIS/pull/51881) | [PR #51950](https://github.com/qgis/QGIS/pull/51950) |
| Los cambios en la geometría se descartan al guardar ediciones cuando el filtro de capa está activado (capa gpkg). | [#51934](https://github.com/qgis/QGIS/issues/51934) | Trabaja para mí |  |
| If a widget default value is setup as NULL then it\'s not working as it\'s overriden by database column default | [#51818](https://github.com/qgis/QGIS/issues/51818) | Won\'t Fix (probably: still debating) |  |
| Can\'t use raster Unique values symbolgogy for Integer rasters with a single value of 1 | [#51822](https://github.com/qgis/QGIS/issues/51822) | [PR #51975](https://github.com/qgis/QGIS/pull/51975) | [PR #51979](https://github.com/qgis/QGIS/pull/51979) |
| PyQGIS QgsPolygon creación se bloquea | [#51978](https://github.com/qgis/QGIS/issues/51978) | [PR #52004](https://github.com/qgis/QGIS/pull/52004) | PORHACER. |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Área Simplificar quita Valores Z y M | [#50742](https://github.com/qgis/QGIS/issues/50742) | [PR #51695](https://github.com/qgis/QGIS/pull/51695) | [PR #51742](https://github.com/qgis/QGIS/pull/51742) |
| El valor NULL se muestra como enlace html NULL en el widget Archivo | [#50892](https://github.com/qgis/QGIS/issues/50892) | [PR #51770](https://github.com/qgis/QGIS/pull/51770) | [PR #51775](https://github.com/qgis/QGIS/pull/51775) |
| La tabla del editor de vértices muestra columnas incorrectas en QGIS 3.28 | [#51433](https://github.com/qgis/QGIS/issues/51433) | [PR #51774](https://github.com/qgis/QGIS/pull/51774) | [PR #51986](https://github.com/qgis/QGIS/pull/51986) |
| Al copiar objetos espaciales a la capa PostgreSQL no se copia el valor del atributo del mismo nombre | [#51121](https://github.com/qgis/QGIS/issues/51121) | Won\'t Fix |  |
| Bloqueo al cambiar el estilo a desplazamiento puntual desde el generador de geometría | [#51070](https://github.com/qgis/QGIS/issues/51070) | [PR #51784](https://github.com/qgis/QGIS/pull/51784) | PORHACER. |
| Arreglar parámetro de confianza no guardado y no leído | no reportado | [PR #51854](https://github.com/qgis/QGIS/pull/51854) | PORHACER. |
| Decoración de la flecha norte: el selector de archivos para SVG personalizado no funciona correctamente | [#51850](https://github.com/qgis/QGIS/issues/51850) | [PR #51882](https://github.com/qgis/QGIS/pull/51882) | [PR #51949](https://github.com/qgis/QGIS/pull/51949) |
| El cuadro de diálogo Filtro para capas vectoriales en estado de edición puede seguir abriéndose mediante el icono de filtro del menú Capas. | [#51816](https://github.com/qgis/QGIS/issues/51816) | [PR #51884](https://github.com/qgis/QGIS/pull/51884) | [PR #51990](https://github.com/qgis/QGIS/pull/51990) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/)
### Funcionalidad: Bugs corregidos por Sandro Santilli
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| CI falla al tocar src/test/qgistest.h | [#51917](https://github.com/qgis/QGIS/issues/51917) |  |  |
| TestQgsTileDownloadManager::testIdleThread es inestable | [#48927](https://github.com/qgis/QGIS/issues/48927) | [PR #51916](https://github.com/qgis/QGIS/pull/51916) |  |
| Crash on exit with static `QgsCoordinateReferenceSystem` | [#51893](https://github.com/qgis/QGIS/issues/51893) | [PR #51891](https://github.com/qgis/QGIS/pull/51891) | [PR #51954](https://github.com/qgis/QGIS/pull/51954) |
| Permitir omitir pruebas dependientes del backend PostgreSQL en tiempo de ejecución | [Discussion in PR #51891](https://github.com/qgis/QGIS/pull/51891#discussion_r1109132667) | [PR #51910](https://github.com/qgis/QGIS/pull/51910) | N/D |
| No descartar atributos geométricos que no tengan SRID | [#49380](https://github.com/qgis/QGIS/issues/49380#issuecomment-1282913470) | [PR #51885](https://github.com/qgis/QGIS/pull/51885) | [PR #51997](https://github.com/qgis/QGIS/pull/51997) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Prestación: Corrección de errores por Jean Felder
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| wms getcapabilities se bloquea en datos dimensionales si no hay valores | no informado | [PR #51930](https://github.com/qgis/QGIS/pull/51930) | [PR #51933](https://github.com/qgis/QGIS/pull/51933) |
| \[3D\] Fix Y-Z inversion in point3dsymbolwidget | no informado | [PR #51855](https://github.com/qgis/QGIS/pull/51855) | [PR #51938](https://github.com/qgis/QGIS/pull/51938) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jean Felder](https://oslandia.com/)
### Prestación: Corrección de errores por Jacky Volpes
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Missing \"Save style\...\" icon in Layer Style Panel | [#51515](https://github.com/qgis/QGIS/issues/51515) | [PR #52037](https://github.com/qgis/QGIS/pull/52037) | Riesgoso? |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Jacky Volpes](https://oslandia.com/)
### Prestación: Corrección de errores por Stefanos Natsis
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Arrastrar y soltar nubes de puntos desde el navegador añadir la capa dos veces | no informado | [PR #51685](https://github.com/qgis/QGIS/pull/51685) |  |
| Al abrir más de 16 capas vectoriales a la vez se produce un fallo | no informado | [PR #51782](https://github.com/qgis/QGIS/pull/51782) |  |
| Bloqueo al intentar dividir línea por punto | [#51501](https://github.com/qgis/QGIS/issues/51501) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| QGIS 3.26 crashes when performing \"split with line\". | [#50948](https://github.com/qgis/QGIS/issues/50948) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| No se puede dividir una geometría lineal en un vértice si la geometría tiene dimensión Z. | [#49403](https://github.com/qgis/QGIS/issues/49403) | [PR #51797](https://github.com/qgis/QGIS/pull/51797) | [PR #51951](https://github.com/qgis/QGIS/pull/51951) |
| Current implementation of multiple-layer style paste doesn\'t work for the command menu \"Layer / Paste Style\". | [#25214](https://github.com/qgis/QGIS/issues/25214) | [PR #51799](https://github.com/qgis/QGIS/pull/51799) |  |
| Copy attribute / Copy feature attributes doesn\'t return value if value is URI | [#26899](https://github.com/qgis/QGIS/issues/26899) | [PR #51803](https://github.com/qgis/QGIS/pull/51803) |  |
| La herramienta de división intenta dividir incluso sin puntos digitalizados | no reportado | [PR #51831](https://github.com/qgis/QGIS/pull/51831) | [PR #51955](https://github.com/qgis/QGIS/pull/51955) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Stefanos Natsis](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corrección del uso de la capa de símbolos de línea interpolada para los contornos de polígonos. | No reportado | [PR #52030](https://github.com/qgis/QGIS/pull/52030) | [PR #52032](https://github.com/qgis/QGIS/pull/52032) |
| \[processing\] Don\'t raise uncaught exceptions when trying to generate GDAL commands for invalid layers | [#51958](https://github.com/qgis/QGIS/issues/51958) | [PR #51994](https://github.com/qgis/QGIS/pull/51994) | [PR #52001](https://github.com/qgis/QGIS/pull/52001) |
| Don\'t use scientific notation when generating gdal_translate command from georeferencer | [#51813](https://github.com/qgis/QGIS/issues/51813) | [PR #51993](https://github.com/qgis/QGIS/pull/51993) | [PR #52071](https://github.com/qgis/QGIS/pull/52071) |
| Aplicar inmediatamente los cambios de precisión y sufijo de la etiqueta de rampa de color cuando está marcada la opción de aplicación automática. | No reportado | [PR #51989](https://github.com/qgis/QGIS/pull/51989) | No apropiado |
| \[processing\] Fix exception when setting output files in batch processing after removing rows | [#51664](https://github.com/qgis/QGIS/issues/51664) | [PR #51988](https://github.com/qgis/QGIS/pull/51988) | [PR #51998](https://github.com/qgis/QGIS/pull/51998) |
| \[processing\] Gracefully handle algorithms with no provider set | [#51971](https://github.com/qgis/QGIS/issues/51971) | [PR #51985](https://github.com/qgis/QGIS/pull/51985) | [PR #51999](https://github.com/qgis/QGIS/pull/51999) |
| Los valores Nan z no deben recortarse de las geometrías renderizadas | [#51796](https://github.com/qgis/QGIS/issues/51796) | [PR #51984](https://github.com/qgis/QGIS/pull/51984) | [PR #51996](https://github.com/qgis/QGIS/pull/51996) |
| Don\'t try to download whole COG locally in order to determine open options | No reportado | [PR #51982](https://github.com/qgis/QGIS/pull/51982) | No apropiado |
| Corrección de la pérdida del primer color de las capas de símbolos lineburst en la interfaz gráfica de usuario. | [#51942](https://github.com/qgis/QGIS/issues/51942) | [PR #51952](https://github.com/qgis/QGIS/pull/51952) | [PR #51968](https://github.com/qgis/QGIS/pull/51968) |
| Corrección de la iteración vectorial ineficaz cuando ninguna regla basada en reglas coincide con la escala actual del mapa. | No reportado | [PR #51904](https://github.com/qgis/QGIS/pull/51904) | No apropiado |
| Corrección de la lógica para activar un restablecimiento completo del modelo en la tabla de atributos tras cambiar los atributos. | No reportado | [PR #51890](https://github.com/qgis/QGIS/pull/51890) | [PR #51892](https://github.com/qgis/QGIS/pull/51892) |
| Corrección de la colocación de etiquetas perimetrales con el formato HTML activado | [#51829](https://github.com/qgis/QGIS/issues/51829) | [PR #51840](https://github.com/qgis/QGIS/pull/51840) | [PR #51868](https://github.com/qgis/QGIS/pull/51868) |
| Corrección de la pérdida de datos en columnas de geometría secundaria al mostrarlas en forma de atributos. | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51863](https://github.com/qgis/QGIS/pull/51863) | No apropiado |
| Corrección de la pérdida de datos cuando se utilizan capas con columnas de geometría secundaria en herramientas de procesamiento. | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51846](https://github.com/qgis/QGIS/pull/51846) | No apropiado |
| Gestión correcta de la conversión de valores geométricos para campos geométricos | [#49380](https://github.com/qgis/QGIS/issues/49380) | [PR #51845](https://github.com/qgis/QGIS/pull/51845) | [PR #51859](https://github.com/qgis/QGIS/pull/51859) |
| Mostrar un icono para los campos de geometría | No reportado | [PR #51844](https://github.com/qgis/QGIS/pull/51844) | No apropiado |
| Fix geometry fields incorrectly show as \"range\" types in fields list | No reportado | [PR #51842](https://github.com/qgis/QGIS/pull/51842) | [PR #51860](https://github.com/qgis/QGIS/pull/51860) |
| Asegúrese de que el src correcto está disponible para QgsMapCanvas para ranuras conectadas a extentsChanged cuando se cambia el SRC de lienzo | [#51833](https://github.com/qgis/QGIS/issues/51833) | [PR #51841](https://github.com/qgis/QGIS/pull/51841) | [PR #51873](https://github.com/qgis/QGIS/pull/51873) |
| Fix array_remove_all behavior when removing null values from array | [#51820](https://github.com/qgis/QGIS/issues/51820) | [PR #51838](https://github.com/qgis/QGIS/pull/51838) | [PR #51869](https://github.com/qgis/QGIS/pull/51869) |
| Use a better approach to update virtual layer queries which doesn\'t lose all the layer\'s properties | [#51118](https://github.com/qgis/QGIS/issues/51118) | [PR #51780](https://github.com/qgis/QGIS/pull/51780) | [PR #51872](https://github.com/qgis/QGIS/pull/51872) |
| \[layouts\] Use nicer number formatting for dynamic map scale labels | [#51764](https://github.com/qgis/QGIS/issues/51764) | [PR #51768](https://github.com/qgis/QGIS/pull/51768) | No es posible |
| Re-permit format_number to omit group separators | No reportado | [PR #51761](https://github.com/qgis/QGIS/pull/51761) | [PR #51763](https://github.com/qgis/QGIS/pull/51763) |
| Recuerde el estado colapsado del cuadro de grupo del renderizador de capas vectoriales | No reportado | [PR #51719](https://github.com/qgis/QGIS/pull/51719) | No apropiado |
| When unchecking render layers as a group, ensure child layers don\'t have clipping blend modes | [#51358](https://github.com/qgis/QGIS/issues/51358) | [PR #51707](https://github.com/qgis/QGIS/pull/51707) | Demasiado intrusivo |
| Corrección de la georreferenciación incorrecta de las imágenes | [#51699](https://github.com/qgis/QGIS/issues/51699) | [PR #51705](https://github.com/qgis/QGIS/pull/51705) | [PR #51736](https://github.com/qgis/QGIS/pull/51736) |
| Corrección del fallo al mostrar información sobre herramientas para capas no válidas. | No reportado | [PR #51703](https://github.com/qgis/QGIS/pull/51703) | [PR #51708](https://github.com/qgis/QGIS/pull/51708) |
| Fix map tips do not show for vector layers where the HTML map tip option isn\'t used | No reportado | [PR #51702](https://github.com/qgis/QGIS/pull/51702) | No afectado |
| Corrección de la creación de GeoPDF con temas exportados que contienen barras oblicuas | [#51480](https://github.com/qgis/QGIS/issues/51480) | [PR #51633](https://github.com/qgis/QGIS/pull/51633) | [PR #51677](https://github.com/qgis/QGIS/pull/51677) |
| Avoid redo-ing the legend symbol hit test for legend edits which won\'t affect the legend symbols visible in a map | [#51455](https://github.com/qgis/QGIS/issues/51455) | [PR #51681](https://github.com/qgis/QGIS/pull/51681) | [PR #51738](https://github.com/qgis/QGIS/pull/51738) |
| Optimizar el filtro de leyendas mediante cálculos de mapas/expresiones | [#51233](https://github.com/qgis/QGIS/issues/51233) | [PR #51675](https://github.com/qgis/QGIS/pull/51675) | Demasiado arriesgado |
| \[georeferencer\] Fix warning about missing output file name doesn\'t show in all circumstances | No reportado | [PR #51673](https://github.com/qgis/QGIS/pull/51673) | [PR #51739](https://github.com/qgis/QGIS/pull/51739) |
| Ensure using \@geometry/@feature variables trigger geometry fetching in expression calculation | [#50791](https://github.com/qgis/QGIS/issues/50791) | [PR #51655](https://github.com/qgis/QGIS/pull/51655) | [PR #51678](https://github.com/qgis/QGIS/pull/51678) |
| Corrección de la generación de perfiles de elevación ráster para líneas exactamente horizontales/verticales. | [#51196](https://github.com/qgis/QGIS/issues/51196) | [PR #51637](https://github.com/qgis/QGIS/pull/51637) | [PR #52072](https://github.com/qgis/QGIS/pull/52072) |
| Porcentaje de codificación de valores de texto al crear/actualizar campos en los servicios de prestaciones de ArcGIS | [#51509](https://github.com/qgis/QGIS/issues/51509) | [PR #51636](https://github.com/qgis/QGIS/pull/51636) | [PR #51654](https://github.com/qgis/QGIS/pull/51654) |
| Corrección de los resultados de arrastrar y soltar en GDB en columnas desplazadas por on | [#51435](https://github.com/qgis/QGIS/issues/51435) | [PR #51634](https://github.com/qgis/QGIS/pull/51634) | [PR #51969](https://github.com/qgis/QGIS/pull/51969) |
| Exponer opción para pasos de tiempo irregulares al exportar animaciones de mapas. | [#51546](https://github.com/qgis/QGIS/issues/51546) | [PR #51632](https://github.com/qgis/QGIS/pull/51632) | [PR #51638](https://github.com/qgis/QGIS/pull/51638) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)
### Prestación: Corrección de errores por David Signer
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.28 backport commit (GitHub) |
| --- | --- | --- | --- |
| WMS legend symbol missing for \"Meters at Scale\" symbology and projected CRS | [#50366](https://github.com/qgis/QGIS/issues/50366) | [PR #52015](https://github.com/qgis/QGIS/pull/52015) |  |
| La vista de formulario de tabla de atributos pierde el índice cuando se cambia una capa dependiente | [#43902](https://github.com/qgis/QGIS/issues/43902) | [PR #52046](https://github.com/qgis/QGIS/pull/52046) |  |
| Attribute table form view looses index when the \"yellow\" selection is changed | no reportado | [PR #52045](https://github.com/qgis/QGIS/pull/52045) |  |
| Los objetos espaciales del Editor de relaciones ya no se pueden seleccionar | no reportado | [PR #51914](https://github.com/qgis/QGIS/pull/51914) | No afectado |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

This feature was developed by [David Signer](https://opengis.ch/)

{{<content-end >}}
