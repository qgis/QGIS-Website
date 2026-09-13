---
HasBanner: false
draft: false
releaseDate: '2019-06-21'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.8
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.8{#changelog38 }
![image1](images/projects/403e44c7e958cff5d07a1eaf12af76ade88c564d.png)

Fecha de lanzamiento: 2019-06-21

QGIS 3.8 trae una extensa lista de nuevos cambios y mucho pulido de las funciones existentes, cuyos aspectos más destacados trataremos aquí. Como siempre, podemos recordarle que QGIS es un proyecto de código abierto y, si puede, considere apoyar nuestro trabajo a través de donaciones, patrocinios o contribuciones a la documentación del código, el sitio web, etc.

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, testers y a toda la gente ahí fuera que dedica su tiempo y esfuerzos (o financia a personas para que lo hacen). ¡Desde la comunidad de QGIS esperamos que disfrutes de este nuevo lanzamiento! Si deseas donar tiempo, dinero o participar de cualquier otra forma para hacer QGIS más impresionante, ¡por favor ve a qgis.org y echa una mano!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate/donors.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Herramientas de mapa
### Prestación: Forzar mediciones cartesianas al medir distancias / áreas
In 3.8, we added an option to the measurement tool which forces Cartesian measurements for distance or area measurements. Previously, the measurement tools always used ellipsoidal/geodesic area and distance calculations, but there\'s occasions when this is not desirable and users require pure Cartesian calculations instead.

![image2](images/entries/e912304d18194a43111a2f054b7f1dba931985d4.webp)

This feature was funded by [Oslandia](https://oslandia.com)

This feature was developed by [Loïc Bartoletti (Oslandia)](https://oslandia.com)
## Interfaz de usuario
### Función: Botón Guardar como plantilla
While QGIS has offered support for Project Templates for many years, we enhanced this in 3.8 and made it much simpler for users to create new templates. Now, users can create a new template from their current project by selecting \"Save To -\> Templates\" from the \"Project\" menu.

![image3](images/entries/8a99e041656f5d3d1fa504636aa36b0046efe532.webp)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](http://www.opengis.ch/)
### Feature: Improved \"Zoom to Native Resolution\" behavior
We\'ve improved the \"Zoom to Native\" action, so it now works correctly with tiled (e.g. WMTS/XYZ/ArcGIS MapServer) layers, by zooming to the closest native tile resolution. Additionally, we tweaked tile rendering so that pixel-perfect rendering occurs when the map is viewed at a native tile resolution. The result: super-crisp map renders when using tiled layer sources!

![image4](images/entries/61f13b52d685dcd67c7c9cc8dbb6daa269ed096a.webp)
### Prestación: Arrastrar y soltar capas a widgets de capa de mapa
Para mejorar la usabilidad de grandes proyectos QGIS, ahora admitimos arrastrar y soltar capas directamente desde la tabla de contenido del proyecto a cualquier widget que solicite una selección de capa de mapa (por ejemplo, algoritmos de procesamiento). Para proyectos complejos, localizar una capa en la tabla de contenido y arrastrarla es mucho más fácil que seleccionarla desde el cuadro combinado de widget de capa de mapa plano.

Además, para los algoritmos de procesamiento, las capas se pueden arrastrar directamente desde el panel del navegador para ingresar las opciones de capa.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Simbología
### Prestación: Cadenas de caracteres múltiples para marcadores de fuente
While QGIS has long offered support for rendering points using font-based character markers, we\'ve enhanced this functionality in 3.8 and now offer the ability to render multi-character strings! And since we\'re always aiming to make the QGIS application interface as user-friendly and pleasant to use as possible, we also took the opportunity to tweak the UI for font markers and squash a number of frustrating GUI issues which previous versions suffered from.

![image5](images/entries/a0f55caed98366ae6eaa0e413d425259aa613b9b.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Factor de distancia de etiqueta de desplazamiento de punto
Otra adición a las nuevas características de simbología agregadas en 3.8 es un nuevo control de factor de distancia de etiqueta para marcadores de desplazamiento puntual. Esta opción permite colocar etiquetas de marcador desplazadas a una distancia basada en el tamaño diagonal real del marcador en lugar de una distancia fija.

![image6](images/entries/7be374a464bde6d79745c1fedfc6075886f09b31.webp)

Esta herramienta fue desarrollada por henrik
### Prestación: Tipo de símbolo de línea Hash
QGIS loves cartography, and we know you love making pretty maps! So we\'ve added a brand-new line symbology option for \"Hashed Lines\". This line symbol type is designed to replicate the ArcGIS Hash Line symbol layer type, and allows for a repeating line segment to be drawn over the length of a feature (with a line-sub symbol used to render each individual segment).

Todas las opciones disponibles para la capa de símbolo de línea de marcador existente también están disponibles para líneas hash, p.ej. primer/último vértice, puntos medios, intervalos regulares, intervalos definidos por datos, etc. La longitud y el ángulo de la línea hash también pueden tener anulaciones definidas por datos, que se evalúan por segmento de línea, permitiendo que la línea hash cambie el tamaño y el ángulo sobre La longitud de una única característica renderizada.

![image7](images/entries/d540197d4a5088df43cac495dc1a88b931131cfe.webp)

Esta herramienta fue financiada por anónimo

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Ángulos de linea medios para marcador y simbología de línea hash
In previous QGIS versions, when a marker line was rendered using interval or center point place placement, the symbol angles were determined by taking the exact line orientation at the position of the symbol. This often leads to undesirable rendering effects, where little \"jaggies\" or corners in lines which occur right at the position of the symbol cause the marker to be oriented at a very different angle to what the eye expects to see.

Queremos que sus mapas sean lo más hermosos posible, por lo que en QGIS 3.8 el ángulo del marcador se calcula promediando sobre la línea una distancia especificada a cada lado del símbolo. P.ej. promediar el ángulo de línea de más de 4 mm significa que tomamos los puntos a lo largo de la línea de 2 mm a cada lado de la ubicación del símbolo, y los usamos para calcular el ángulo de línea de ese símbolo. Esto tiene el efecto de suavizar (o eliminar) cualquier pequeña desviación local de la dirección general de la línea, lo que da como resultado una orientación visual mucho más agradable del marcador o las líneas hash.

Al igual que todas las configuraciones de símbolos, la distancia de suavizado del ángulo promedio se puede establecer usando mm/píxeles/unidades de mapa/etc., y admite valores definidos por datos. Los anillos cerrados también consideran correctamente envolver estos ángulos promedio desde el vértice inicial/final.

Esta opción está disponible tanto para el marcador de símbolo de línea como para los nuevos tipos de símbolo de línea hash.

![image8](images/entries/4101a09e0fa63aada9acce23092bb29e16db1114.webp)

Esta herramienta fue financiada por anónimo

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Ajustes de compensación para capas de símbolos con relleno de patrón de puntos
To round out the new symbology options we\'ve added in 3.8, the Point Pattern Fill symbol type has a new setting allowing for offsetting the markers in the pattern by a preset (or data-defined!) amount. This opens the door for many styling possibilities which were not possible in earlier versions, and further increases our compatibility with converted ArcGIS symbol and layer styles.

![image9](images/entries/0cda10ddf2bac42e77b7cfc9ada813e4a26353a5.gif)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Radio de efectos de difuminado en vivo es ahora amigable con hi-dpi
QGIS 3.8 brings a highly-desired fix to layer effects\' blurring radius (aka strength). In earlier QGIS versions, these blur settings did not take into account the DPI of the map render --- resulting in inaccurate effects rendering when exporting canvases/layouts at high resolutions. In 3.8, this was fixed and high-resolution map exports now match the results shown on the map canvas and are completely resolution-independent.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Etiquetando
### Prestación: Generadores de gemotería para etiquetado
This is a huge one! During the developer\'s meeting in A Coruña, Matthias Kuhn took the opportunity to implement a frequently-asked-for feature in our labeling engine: Geometry Generator support.

Just like Geometry Generators for symbols, we now allow label paths and positions to be calculated using dynamically-evaluated geometry expressions. You can take advantage of the rich support for geometry processing which QGIS\' expression engine exposes, and use this to do ALL sorts of pre-processing to your feature geometries before they are labelled. Want to place labels around the start or end point of linestring geometries? What about dynamically smoothing and simplifying the path used for labeling river features, based on the current map scale? How about buffering polygon objects inward by a percentage of their area, and then labeling around the perimeter of this shrunken area? Now, it\'s ALL possible, thanks to the power of labeling geometry generators!

![image10](images/entries/abc08ecfe2a879424b3f8e96c26b0391e342090e.webp)

This feature was funded by [QGIS user group switzerland](https://www.qgis.ch)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Prestación: Herramientas de Etiquetado de Mapas ahora usa comportamiento click-click
Like the other QGIS digitizing and map tools, the \"Move Label\" and \"Rotate Label\" tools now use the standard left-click-to-start edit, left-click-to-end behavior. Consistency is good!
## Objetos 3D
### Prestación: Líneas anchas y resaltado de bordes poligonales
Like all recent QGIS releases, in version 3.8 we\'ve significantly boosted QGIS\' 3D rendering capabilities. New 3D rendering features include:
- Configurable line width (in screen units) for \"simple\" 3D lines (in previous versions they were always 1px wide)
- Resaltado opcional de bordes de polígonos 3D.

![image11](images/entries/6e77320c7766d11f25893f9c2de2e7de57eab488.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Prestación: Exportar animaciones 3D
Another exciting change we\'ve introduced in QGIS 3.8 is the ability to export your 3D animations! These are exported as a series of png/jpg/\... images, which can be easily merged into .avi or other standard video files (using external tools).

![image12](images/entries/f0d7bb5632bfaa9c9feafb12e7b258c312ba66a6.webp)

This feature was funded by [Northumberland National Park Authority](https://www.northumberlandnationalpark.org.uk/)

This feature was developed by [Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Prestación: Terreno desde fuentes online
Con esta nueva prestación de la versión 3.8, ahora puede buscar directamente terrenos para sus escenas 3D de fuentes en línea (por ejemplo, mosaicos alojados en AWS). ¡No más abastecimiento y preparación de rásteres con DEM, solo habilite esta opción y vea hermosas escenas 3D listas para usar!

This feature was funded by [Crowdfunding: More QGIS 3D](https://www.lutraconsulting.co.uk/crowdfunding/more-qgis-3d/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Prestación: Configuración del campo de ángulo de visión de la cámara
En QGIS 3.8, el campo de visión de la cámara a través del cual se representan las escenas 3D ha ganado un nuevo campo de configuración configurable.

![image13](images/entries/13a7660953586fea69df8afea7f75dd5d457fce8.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Diseño de impresión
### Prestación: Distribuir el espaciado entre elementos de manera uniforme
Para facilitar la creación de su diseño de impresión QGIS perfecto, agregamos nuevas herramientas para reubicar automáticamente los elementos para que el espacio horizontal o vertical entre ellos sea igual. ¡Esta adición completa las opciones existentes para alinear elementos, brindando más poder de una aplicación DTP dedicada directamente dentro del Diseñador de diseño de impresión QGIS!

Esta herramienta fue desarrollada por Matteo Nastasi
### Prestación: Creación de Flecha de Norte
We\'ve listened to user feedback which indicated that the previous approach for creating north arrows within print layouts was too difficult, and consequently have added a new button in the Print Layout Designer for direct north arrow creation. This button is a shortcut to adding a picture item, setting it to a north arrow picture, and linking it with a map. The end result is identical, but it\'s much easier for new users to understand if we expose it as an explicit \"North Arrow\" item!

Even experienced users will likely appreciate the improved workflow, including automatically linking the picture rotation to a sensible default map choice (if a map is selected, it\'s used. If not, the topmost map item under the newly drawn north arrow is used. If there\'s none, the layout\'s \'reference map\' (or biggest map) is used as a fallback).

![image14](images/entries/7a0dd68c9a38f6e4b4f0177ae53978710df89ad5.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Expresiones
### Prestación: Ordenar con soporte para funciones de agregación de expresión y concatenación
Dado que ciertas expresiones agregadas y de concatenación requieren resultados en un cierto orden, ahora permitimos el control sobre las características del orden que se agregan al agregado durante la evaluación de la expresión.

E.g. `concatenate("Station",concatenator:=',', order_by:="Station")` will give a comma-separated list of station names in alphabetical order, rather than layer feature order.

![image15](images/entries/024918bb03f4620a2b5d32926322d0644c782bb8.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Simplified variant of \"attribute\" function
This improvement brings a second variant for the existing \"attribute\" function. The \"attribute\" function in previous QGIS releases required both a target feature and attribute name to be specified. The new version is much simpler, automatically using the current feature and only requiring an attribute name.

P. ej.

Comportamiento previo:

`attribute($currentfeature, 'name' )` -\> returns value stored in \'name\' attribute for the current feature

Comportamiento mejorado:

`attribute( 'name' )` -\> returns the value stored in \'name\' attribute for the current feature

It\'s just a faster shorthand version!

![image16](images/entries/13f09f754dea12a13b9d9aeb8606e86582e87e3f.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Recuperar vértices desde el extremo de geometrías
We added negative index support to the point_n(), angle_at_vertex(), and distance_to_vertex() functions, allowing for retrieval of vertices counting backward from the end of a geometry.

![image17](images/entries/6eac3dcc7d9053f16733306878fb0cebf993737a.webp)

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
### Prestación: Nuevas funciones de expresión
As always, a new QGIS release brings a bunch of new functions for use within QGIS\' expression engine. These new functions add increased flexibility and power to the expression engine, and everywhere it\'s used throughout QGIS. This round, we\'ve added a set of new functions which make it super-easy to operate on file names and paths.

Nuevas funciones de expresión desarrolladas por Nyall Dawson of North Road:
- **base_file_name:** Returns the base name of the file without the directory or file suffix.
- **file_exists:** Returns true if a file exists
- **file_name:** Returns the file name from a full path
- **file_path:** Returns the directory/path from a full file path
- **file_size:** Returns a file size
- **file_suffix:** Returns a files suffix/extension
- **is_directory:** Returns true if a file path is a directory
- **is_file:** Returns true if a file path is a file

Nuevas funciones de expresión desarrolladas por Mathieu Pellerin of iMHere Asia:
- **array_all:** Returns true if an array contains the all values of a given array.
- **concatenate_unique:** Returns all unique strings from a field or expression joined by a delimiter.

![image18](images/entries/e83795c8c525c092fa9b68172ecdf9f713e5f15a.webp)
### Feature: New aggregation method: concatenate_unique
We added a new function `concatenate_unique()` to the expression engine (and Processing\'s \"aggregate\" algorithm) to support concatenating only unique values from a list or set of features.

![image19](images/entries/77c53d02f719feaf03e7e3d9cea8468645aa81e3.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Digitalizando
### Prestación: Widget flotante para entrada avanzada al lado del cursor del ratón
Para que las herramientas de digitalización avanzada existentes sean más fáciles de usar, agregamos una opción para mostrar los valores actuales de distancia/ángulo/x/y como una pantalla flotante junto al cursor del mouse.

![image20](images/entries/c0703ea4a49115bfb398d174aa727c7e0fc67240.gif)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [Olivier Dalang and OPENGIS.ch](https://www.opengis.ch)
### Prestación: agregar vértice encadenado en el punto final
In QGIS 3.0, we added the ability to extend an existing line feature by clicking a \"+\" indicator at the start or end of line features when using the node tool. Version 3.8 extends this functionality by allowing addition of more than one vertex using the \"+\" button.

![image21](images/entries/a58caabea738a7e34529b9aeb2bb1d4cd307cf50.gif)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [Olivier Dalang and OPENGIS.ch](https://www.opengis.ch)
### Prestación: Mejoras en el editor de vértices
Para esta versión, mejoramos el editor de vértices para que ahora vincule correctamente los *vértices seleccionados en el lienzo* con los *vértices para la edición manual de coordenadas en la tabla*.

![image22](images/entries/e518f5fc5b2decdbaba6272249cdfb3b6c2ad2fe.gif)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://www.opengis.ch)
## Widgets y Formularios
### Prestación: Permitir navegación en la lista de entidades
| arrows allow browsing the feature list in the attribute table in form view | the current edited feature can be highlighted and the map canvas automatically panned or zoomed
### Prestación: Widget de Formulario HTML
Gracias al generoso patrocinio de A.R.P.A Piemonte (una de las agencias ambientales regionales italianas) desarrollamos un nuevo widget de formulario con cuerpo HTML y acceso a valores y expresiones de entidades.

![image23](images/entries/3932162893e8bb8d20d284d7a99ead2de9dac601.gif)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: Color de fondo personalizado de widgets de formulario
Gracias al generoso patrocinio de A.R.P.A Piemonte (una de las agencias ambientales regionales italianas) finalmente lo liberamos del aburrimiento de los fondos grises.

![image24](images/entries/8627ae1acd4ed30ae116e3b79679ecb5cad3241a.gif)

This feature was funded by [A.R.P.A. Piemonte](http://www.arpa.piemonte.it)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: Navegar por las entidades de la tabla de atributos desde el visor
We\'ve added the possibility to browse through the attributes of features in a layer. This makes workflows for *asset management* a **lot** easier! You can:
1. Definir un filtro
2. Navegar por todas las funciones coincidentes
3. Revisar y ajustar

Tambien puede enfocar y ampliar a la geometría o resaltar la entidad actual mientras navega.

(Esto reemplaza el complemento anterior de ItemBrowser con una funcionalidad incorporada equivalente).

![image25](images/entries/f034aaf2a173be885b5f8fca36e3b577795ad1de.webp)

This feature was funded by [regioDATA](https://www.regiodata-gmbh.de/)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://www.opengis.ch)
## Procesado
### Feature: Add \"Save layer styles into GeoPackage\" option for Package Layers algorithm
QGIS loves GeoPackage, so it\'s likely no surprise that every new QGIS version brings improvements to GeoPackage handling! In 3.8, we enhanced the \"Package Layers\" Processing algorithm so that it now allows embedding the current layer styles directly into the packaged layers!

![image26](images/entries/ebabefc4ccc4b71dcffda0508834b709fddec635.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Análisis de superposición
Este nuevo algoritmo de procesamiento calcula el área y el porcentaje de cobertura mediante el cual las entidades de una capa de entrada se superponen con entidades de una selección de capas superpuestas. Se agregan nuevos atributos a la capa de salida que informa el área total de superposición y el porcentaje de la característica de entrada solapada por cada una de las capas de superposición seleccionadas.

This is quite a common GIS task request, yet is full of traps for inexperienced users, and the amount of manual data work usually done by users to calculate these figures can often lead to mistakes and inaccurate results. We want to make spatial analysis as easy and foolproof as possible, so we\'ve added Overlap Analysis as an inbuilt tool which allows this task to be done in a single step without risk of human error.

![image27](images/entries/d265fa2b9bab9184d25244f0cd8aececb5136e66.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Permitir valores redondeados en Extraer extensión de la capa
We\'ve added a parameter to the Processing algorithm \'Extract Layer Extent\' to round the extent bounding box coordinates to a certain interval. While rounding, the bounding box will only ever be enlarged, to ensure it will always cover the input data set. (I.e. the x and y minimum coordinates are rounded down, and x and y maximum coordinates are rounded up).

![image28](images/entries/6b783ea6f8bb83c8f45844681ed7221126be4782.webp)

Esta prestación fue desarrollada por Raymond Nijssen
### Prestación: Nuevas opciones para el procesamiento automático por lotes
In QGIS 3.8 we moved the existing \"double click column header\" to fill values down functionality to a new \"Auto fill\" button in the Processing Batch dialog, making this feature much more user-discoverable (we suspect many users had no idea this handy shortcut even existed!). In addition, we\'ve added TONS of new functionality to easily auto-populate the batch table. These include:
- File or layer parameters can now be batch populated by searching for files in a directory with a matching filename pattern (including recursive searches!). Ever needed to auto convert 100s of Shapefiles from a set of folders? Now it\'s easy to do!
- Una opción para añadir valores calculados desde una expresión QGIS, permitiendo complejos valores basados en rangos para ser añadidos al diálogo (p.Ej. valores desde 100-1000, incrementándose en 50)
- A \"Calculate by Expression\" option allows for updating existing batch table cells using the results of a QGIS expression. These expressions can freely utilise other parameter values from the input batch rows, making it easy to craft the exact output file name you desire based on the other columns values in a batch row.

![image29](images/entries/e20e687223b884d70737f09130f0e9792974eed6.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Generar teselas ráster XYZ
We\'ve added a brand-new algorithm to generate raster \"XYZ\" tiles using the current QGIS project. Tile images can be saved as individual images in directory structure, or as a single file in the \"MBTiles\" format.

![image30](images/entries/b9af6c101c6c22836c4dec3b78a6ce3d6b7e1bcd.webp)

Esta prestación fue fundada por Hansestadt Herford, SWK mbH, Datenbankgesellschaft mbH

This feature was developed by [Lutra Consulting](https://www.lutraconsulting.co.uk/)
### Prestación: Resurrección de el proveedor OTB
QGIS 3.8 recupera el proveedor de procesamiento OTB, que se eliminó en la actualización QGIS 3.0. El proveedor se actualizó para usar todas las novedades disponibles en Procesamiento en QGIS 3, y una vez más está disponible de fábrica para todos sus requisitos de análisis de imágenes.

(*Note that OTB is a third party dependency which must be manually installed by users. Instructions on installing OTB are available \`here \<https://gitlab.orfeo-toolbox.org/orfeotoolbox/qgis-otb-plugin#open-processing-settings\>\`\_\_*)

![image31](images/entries/77dfad7d869283213cfc54a96e5ced2ad69d259a.webp)

Esta prestación fue desarrollada por Rashad Kanavath
### Prestación: Variables de expresión para un modelo
We\'ve added a new \"Model Variables\" dock panel to the model editor, allowing you to create and set custom expression variables for use in your Processing models. These variables are available anywhere expressions are evaluated within the model, so you can use them as input parameter values for child algorithms, within data-defined dynamic parameters, etc.

The prime use case here is for models which use a constant value throughout multiple steps within the model (e.g. \@target_resolution: a target raster resolution, \@max_simplification: a simplification value for input features coming from different sources, etc). Previously, you\'d need to hunt down and replace these values in multiple places when you wanted to tweak them. By replacing them with variables in your model you only have a single place you need to edit these values when you want to adjust them!

Las variables del modelo se almacenan dentro de un modelo de procesamiento individual en sí mismo y no se exponen fuera del cuadro de diálogo del diseñador del modelo.

![image32](images/entries/dfd820ccdc499878a5d7c818f03cd2d586311945.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Mejorada la IU del modelador
We\'ve added numerous usability improvements to the Processing Graphical Modeler, including
- La adición de útiles informaciones emergentes al pasar el mouse sobre los componentes del modelo
- Los algoritmos y las entradas conectadas a los componentes del modelo se resaltan al pasar el mouse sobre diferentes partes del modelo, lo que hace que sea mucho más fácil visualizar el flujo del modelo y las conexiones dentro de los modelos complejos.
- Los tipos de parámetros de entrada ahora se muestran en el título del cuadro de diálogo de definición de parámetros
- Ahora se puede especificar el tipo de datos para los parámetros numéricos, lo que permite entradas de solo enteros para modelos

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Marcar algoritmos con problemas conocidos
De forma predeterminada, ahora ocultamos algoritmos de terceros con problemas conocidos de la caja de herramientas Procesamiento, lo que le ayuda a evitar la frustración (o resultados engañosos) al ejecutar estos algoritmos. Una nueva configuración en la pantalla Opciones de procesamiento permite mostrar estos algoritmos, pero se resaltarán en la caja de herramientas con un icono de advertencia. ¡Úselo bajo su propio riesgo!

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Algoritmos de lógica boleana OR / AND para ráster
In version 3.8 we\'ve added new algorithms which calculate the boolean OR or AND for a set of input rasters. For AND, if all of the input rasters have a non-zero value for a pixel, that pixel will be set to 1 in the output raster, otherwise it will be set to 0. For OR, if ANY of the input rasters have a non-zero value for a pixel, that pixel will be set to 1 in the output raster, else 0.

Un parámetro de capa de referencia le permite especificar una capa ráster existente para usar como referencia al crear el ráster de salida. El ráster de salida tendrá la misma extensión, CRS y dimensiones de píxeles que esta capa.

By default, a nodata pixel in ANY of the input layers will result in a nodata pixel in the output raster. If you check the \'Treat nodata values as false\' option, then nodata inputs will be treated the same as a 0 input value.

Estos nuevos algoritmos hacen un cálculo lógico booleano de ráster mucho más simple, sin la complejidad de usar la calculadora de ráster. También son dinámicamente escalables a cualquier cantidad de rásteres de entrada (a diferencia de la calculadora de ráster), por lo que son mucho más flexibles cuando se usan en sus modelos de Procesamiento.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Nuevos tipos de parámetros de entrada para Imprimir diseños e imprimir  elementos de diseño
By adding new parameter types for Print Layouts and Print Layout items, we\'ve opened up QGIS 3.8 to a whole new world of Processing algorithms which operate on print layouts. These new parameter types allow for creation of Processing algorithms and graphical models which prompt users to select a print layout and/or an item on the layout when run.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Nuevo tipo de parámetro para Escala de Mapa
We\'ve added a new parameter type specifically for map scales, QgsProcessingParameterScale. Scale values are evaluated using self.parameterAsDouble, which return the map scale denominator (matching the standard in other parts of the QGIS API).

Los parámetros de escala se muestran a los usuarios que utilizan el QgsScaleWidget estándar, el cuál incluye el cuadro combinado de escalas predefinidas y un botón de acceso directo para que coincida con la escala del mapa actual. La adición de este nuevo tipo de parámetro le permite crear algoritmos y modelos de procesamiento que requieren una elección de escala en tiempo de ejecución.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Improved \"point\" parameter handling
We improved the workflow for algorithms with a \"point\" input parameter. When picking the point coordinate from a map you can now take advantage of QGIS snapping tools, allowing you to exactly match the point parameter to a feature\'s boundary.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New \"Print Layout Map Extent to Layer\" algorithm
Aprovechando las nuevas facilidades para acceder a Diseños de impresión en Procesamiento, agregamos un nuevo algoritmo que crea una capa poligonal que contiene la extensión de un elemento del mapa del diseño de impresión. La capa de salida también incluye atributos útiles que especifican el tamaño del mapa (en unidades de diseño), la escala y la rotación.

If you\'ve ever wanted to create an advanced overview indicator, and the inbuilt layout tools haven\'t sufficed --- this new algorithm is for you!

![image33](images/entries/a10b7ebe75528742860a666be9de2d1365de3b73.webp)

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Añadir campos X/Y a la capa
Este nuevo algoritmo es un atajo útil para agregar campos X e Y (latitud/longitud) a una capa de puntos. Incluso puede calcular los valores X/Y utilizando un sistema de referencia de coordenadas diferente de la capa (por ejemplo, creando campos de latitud/longitud para una capa en un CRS proyectado).

![image34](images/entries/5633452beec85bb6486092463af4553c02aa6165.webp)

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \"Join attributes by nearest\" algorithm
¡Ahora puede realizar las uniones vecinas K-nearest desde la caja de herramientas Procesamiento!

QGIS 3.8 trae un nuevo algoritmo que toma una capa vectorial de entrada y crea una nueva capa vectorial con atributos adicionales en su tabla de atributos. Los atributos adicionales y sus valores se toman de una segunda capa vectorial, donde las entidades se unen al encontrar las entidades más cercanas de cada capa.

De forma predeterminada, solo se une la entidad más cercana, pero opcionalmente, la unión puede usar las n entidades vecinas más cercanas. Si se especifica una distancia máxima, solo las entidades que estén más cerca de esta distancia serán unidas.

![image35](images/entries/f78e2f7a712f8a5cc1d5e9e20b4bb378598c1180.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Algoritmo Grass r.geomorphon
The upstream GRASS team has been hard at work creating a new GRASS module for terrain analysis --- \"r.geomorphon\". In 3.8 we expose their efforts via a new Processing tool, which calculates geomorphons (terrain forms) and associated geometry using a machine learning approach.

![image36](images/entries/a0026a05eea40004dfd250cf1a2ff492fdeb1b58.webp)
### Prestación: Algoritmo de pansharpening de GDAL
Another third party tool which we\'ve added to the Processing toolbox in QGIS 3.8 is the GDAL pansharpening tool. Now it\'s easy to take advantage of this fast, powerful tool in your Processing analysis scripts and models.

![image37](images/entries/35c02288524968f8ea021f9a64fcd64b9ec328f9.webp)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Nuevo parámetro de prefijo de campos para algoritmos de superposición
We\'ve added overlay layer fields prefix parameter for the following algorithms:
- algoritmo de intersección
- algoritmo de línea de intersección
- algoritmo de diferencia simétrica
- algoritmo de unión

Esto puede ser muy útil para evitar la coincicdencia arbitraria de renombrado de campo al fusionar capas.

This feature was developed by [Mathieu Pellerin](http://imhere-asia.com/)
## Navegador
### Prestación: Acceso directo a hojas de archivos XLSX/ODS
QGIS 3.8 aporta aún más potencia al panel del navegador, y ahora muestra todas las hojas de los archivos de hoja de cálculo (por ejemplo, archivos Microsoft Excel y LibreOffice calc) en el árbol de archivos del navegador.

![image38](images/entries/f311137d05c73b9ba673d6b68669b7117589dacd.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## General
### Prestación: Proyectos QGIS dentro de archivos geopackage
Did we already say that QGIS loves GeoPackage? Need any more proof of this? Well, in QGIS 3.8, we\'ve added to ability to store QGIS projects directly inside GeoPackage files! Now you can create a totally self-contained GeoPackage which embeds a QGIS Project AND all the data used by the project. (Let\'s see Shapefiles match that one!)

![image39](images/entries/8750f1c2e3c3919926fd2cb97488da071f7efc85.webp)

This feature was funded by [QCooperative](https://www.qcooperative.net)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it)
### Prestación: Manejo de transformación de coordenadas muy mejorado
Gracias al trabajo subyacente de los incansables equipos PROJ y GDAL, ¡QGIS ahora tiene muchas mejoras enormes en las capacidades geodésicas y de transformación! Los puntos destacados incluyen:
- The PROJ CRS database is now used to populate QGIS\' CRS selection lists, removing the custom database we used in previous releases. This means that ALL responsibility for CRS definitions and updating these sit were they belong, upstream in the PROJ library \-- and consequently you can expect to see QGIS CRS definitions being a closer match to the official definitions, and newer CRS definitions will be added much faster than in previous releases.. This change also means we\'ll be an exact match for projection handling as all other open-source geospatial tools which have completed the port to the latest PROJ version, such as GDAL 3.0.
- We now rely entirely on PROJ\'s wonderful logic for generating the best coordinate operation to transform between CRS pairs. This means (amongst other stuff), we correctly support complex things like operations which require a \"pivot datum\", e.g. transformation to and from the GDA2020 coordinate systems.
- En lugar del enfoque anterior que QGIS usaba para las transformaciones de datos (llevando nuestra propia tabla de cuándo se pueden usar los archivos de cambio de cuadrícula), ahora usamos PROJ para determinarlos. Esto cambia considerablemente la interfaz de usuario que se muestra cuando un usuario ha optado por seleccionar manualmente una transformación para usar cuando existen múltiples transformaciones, y ahora mostramos una lista simplificada de rutas disponibles (y no disponibles).
- We also use PROJ\'s database to populate lists of available ellipsoids for use in distance and area calculations. This has cleaned up the ellipsoid choices considerably, and added many additional ellipsoid definitions as a result.
- La UX para notificar a los usuarios sobre problemas en las transformaciones de coordenadas se ha mejorado considerablemente, p.ej. los usuarios ahora reciben alertas cuando es posible una transformación más precisa, pero no utilizable en su sistema (debido a la falta de archivos de cambio de cuadrícula .GSB). Siempre que sea posible, presentamos a los usuarios enlaces de descarga directa para obtener estos archivos de cambio de cuadrícula necesarios/deseados. La intención aquí es garantizar que los usuarios estén informados cuando se pueden mejorar las transformaciones, en lugar de recurrir silenciosamente a opciones menos precisas.
- Users also now have the option of placing grid shift files in a \"proj\" folder under their QGIS user profile. This change means users can install grid shift files and make them available in QGIS without requiring administrative rights.
- We\'ve also completed a project which began back in the lead-up to 3.0, which ensures that project-specific transformation pathway settings are correctly respected EVERYWHERE a coordinate transform is performed. This also means we\'re ready for the next stage in handling 4d temporal based coordinate transforms (when these start to land in 2020 and beyond).

A lot of this is only possible thanks to improvements in the underlying PROJ and GDAL libraries, which landed as a result of the GDAL \"barn raising\" effort. On the QGIS side, it was ONLY possible thanks to funding from the Australian ICSM.

This feature was funded by [ICSM](https://www.icsm.gov.au/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Proveedores de datos
### Prestación: Proveedor PostGres: añadir soporte para columnas de identidad generadas
Esta herramienta fue desarrollada por jef-n
### Prestación: Soporte de Lista de cadenas para capas compatibles
QGIS 3.8 now fully supports disk-based layers with String List fields, allowing you to take advantage of QGIS\' flexible handling of list field types with these formats.

Esta prestación fue desarrollada por Mathieu Pellerin
### Prestación: Mas mejoras en el manejo del MapServer de ArcGIS
Reconstruimos el proveedor de MapServer de ArcGIS, añadiendo mejoras significativas sobre versiones previas:
- Capas teselas ahora son cargadas progresivamente, con realimentación inmediata
- Optimizamos significativamente el proveedor, desembocando en redibujados de mapas mucho mas rápidos
- Las capas de MapServer ahora respetan correctamente los ajustes de autenticación y ajustes de referencia HTTP.
- \"Nested\" services are correctly shown in the QGIS browser panel
- Los servicios de ImageServer pueden añadirse usando el proveedor

Resultado final: ¡las capas de MapServer ahora son suaves en QGIS!

Esta prestación fue desarrollada por Nyall Dawson (North Road) & Mathieu Pellerin (iMHere Asia)
### Prestación: Servidor SQL: Manejar geometrías v2, incluyendo geometrías curvas y Z/M
SQL Server users rejoice: QGIS now fully supports curved geometry types (and other \"version 2\" geometry fields)!

In past QGIS versions, the SQL Server provider would only handle version 1 type geometries, and could only show straight feature types. In 3.8, we\'ve added full support for version 2 geometries. This change also allows full support for Z or M enabled geometry types! Additionally, we fixed several known issues with geography field types.

This feature was developed by [Tamas Szekeres](https://github.com/szekerest)
### Prestación: WMS: Definir un filtro para varias capas.
A veces, debe definir el mismo filtro para cada capa seleccionada al realizar una solicitud WMS (por ejemplo, al acceder a datos específicos del usuario). En versiones anteriores de QGIS tuvimos que definir el filtro usando el formato:

`&FILTER=layer1:"column1" = 'value1';layer2:"column1" = 'value1';layer3:"column1" = 'value1'`

With QGIS 3.8, we\'ve simplified this, and now allow the filter format:

`&FILTER=layer1,layer2,layer3:"column1" = 'value1'`

Esta herramienta fue financiada por VEOLIA

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Prestación: Soporte para curvas en exportación DXF
You can now export curved geometry layers to DXF format without segmentizing the features --- no more loss of curves!

![image41](images/entries/d0543abc36459754e4e3630e3703f0f1169ba7b3.webp)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

Esta prestación fue desarrollada por Jürgen Fischer en colaboración con Matthias Kuhn
## Servidor de QGIS
### Prestación: Permitir la configuración del tamaño para GetLegendGraphics
| For this release we improved how the legend for QGIS servers handles the size of symbols which are scaled by map units. | Whenever possible, the server will determine the legend size based on the map canvas and resolution. Even more, for cases where this information is not available in the GetLegend request, it is now possible to configure a *default scale* in the project, symbols in the legend will then be drawn in the size they will have when rendered at this scale.

This feature was developed by [David Signer, OPENGIS.ch](https://www.opengis.ch)
## Plugins
### Prestación: Soporte para dependencias de complemento
In QGIS 3.8, we\'ve introduced a long-sought-after feature for QGIS plugin developers: the ability to specify dependencies for your plugins.

To add a plugin dependancy, you can use the new metadata \"plugin_dependencies\". The format is a comma-separated list of PIP-like plugin names (with optional version). E.g:

`plugin_dependencies=GeoCoding,IPyConsole==1.9`

El ejemplo superior requerirá:
- Cualquier versión de GeoCoding
- Versión 1.9 de IPyConsole

Cuando se instala un complemento, se analizan los metadatos y se le solicita al usuario un cuadro de diálogo que enumera las dependencias. El usuario puede decidir qué hacer con las dependencias:
- Instalar
- Actualizar/Desactualizar
- No hacer nada

![image40](images/entries/28da67ad96ccda7a8a64b261db17bf33be4b3f69.gif)

This feature was funded by [GISCE TI](https://gisce.net/)

This feature was developed by [Alessandro Pasotti](http://www.itopen.it/)
## Programabilidad
### Prestación: soporte de sintaxis de REGEXP SQL para el proveedor SpatiaLite y conexiones Python
We\'ve enabled REGEX to be used with the spatialite provider. (This comes in handy when setting filters!). We\'ve also added support for this syntax via any python connections made through Qgis.utils\'s \"spatialite_connection\" API - allowing you to use REGEXP in your SQL queries from within DB Manager.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Prestación: Busqueda del vecino mas cercano en QgsSpatialIndex
Agregamos API para permitir la búsqueda precisa de vecinos más cercanos basada en QgsGeometry a las búsquedas de QgsGeometry a través de QgsSpatialIndex. En versiones anteriores de QGIS solo eran posibles búsquedas de vecinos más cercanos de puntos a geometría. Pero con este cambio, puede usar QgsSpatialIndex de forma segura y precisa para determinar los vecinos más cercanos entre cualquier tipo de geometrías.

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Calculadora ráster resultados incorrectos | [#21405](https://issues.qgis.org/issues/21405) | Solucionado en maestro |  |
| El servidor QGIS ignora el orden de representación personalizado al cargar el grupo principal | [#21917](https://issues.qgis.org/issues/21917) | [PR #9878](https://github.com/qgis/QGIS/pull/9878) | Hecho |
| WMS Client: GetFeatureInfo in JSON format doesn\'t display numeric attribute values | [#21735](https://issues.qgis.org/issues/21735) | [PR #9879](https://github.com/qgis/QGIS/pull/9879) | Hecho |
| Fallo al añadir Nuevo campo a Capa Vectorial | [#22100](https://issues.qgis.org/issues/22100) |  |  |
| La prioridad en el etiquetado no aparece atenuada cuando la configuración definida por datos está habilitada | [#22077](https://issues.qgis.org/issues/22077) | No válido |  |
| \$length return bad value | [#22105](https://issues.qgis.org/issues/22105) | trabaja para mi (y para todo el mundo) |  |
| Relation reference widget wrong feature when \"on map identification\" | [#22071](https://issues.qgis.org/issues/22071) |  |  |
| Map composer: \"href\" HTML attribute issue in PDF output | [#22075](https://issues.qgis.org/issues/22075) | won\'t fix |  |
| Problema exportando capa ráster a Geopaquete | [#20848](https://issues.qgis.org/issues/20848) | [PR #10036](https://github.com/qgis/QGIS/pull/10036) | Hecho |
| Crear vector New shapefile POLYGON | [#22107](https://issues.qgis.org/issues/22107) | inválido |  |
| \"Export to PostgreSQL\" python error if rather schema has an uppercase letter in its name | [#22035](https://issues.qgis.org/issues/22035) | [PR #10063](https://github.com/qgis/QGIS/pull/10063) |  |
| Relation reference widget wrong feature when \"on map identification\" | [#22071](https://issues.qgis.org/issues/22071) | [PR #10047](https://github.com/qgis/QGIS/pull/10047) | Hecho |
| Administrador de BD importa dato erróneo | [#22033](https://issues.qgis.org/issues/22033) | [PR #10077](https://github.com/qgis/QGIS/pull/10077) | Hecho |
| QGIS falla al filtrar una capa con un campo adjunto | [#21775](https://issues.qgis.org/issues/21775) | Arreglado por Nyall |  |
| Calculadora Ráster, abs() no funciona | [#29824](https://github.com/qgis/QGIS/issues/29824) | [PR #29965](https://github.com/qgis/QGIS/pull/29965) | Hecho |
| link URL a archivo válido falla en ventana de identificación | [#29879](https://github.com/qgis/QGIS/issues/29879) | [PR #29967](https://github.com/qgis/QGIS/pull/29967) | Hecho |
| QgsProject.instance().clear() cuelga QGIS cuando la ventana LayoutDesigner está abierta | [#29821](https://github.com/qgis/QGIS/issues/29821) | [PR #29968](https://github.com/qgis/QGIS/pull/29968) | Hecho |
| QGIS Server WFS DescribeFeatureType anuncia precisión double de campos virtuales como entero | [#29767](https://github.com/qgis/QGIS/issues/29767) | [PR #29970](https://github.com/qgis/QGIS/pull/29970) | Hecho |
| QGIS falla al exportar una plantilla | [#29798](https://github.com/qgis/QGIS/issues/29798) | [PR #29981](https://github.com/qgis/QGIS/pull/29981) | Hecho |
| Exportar atlas como imagen falla cuando la expresión del nombre de archivo contiene punto | [#29980](https://github.com/qgis/QGIS/issues/29980) | [PR #29983](https://github.com/qgis/QGIS/pull/29983) | Hecho |
| Botones para ajustar el tamaño de marcador en la pestaña de digitalización del diálogo de ajustes generales no funciona | [#29987](https://github.com/qgis/QGIS/issues/29987) | [PR #29991](https://github.com/qgis/QGIS/pull/29991) |  |
| El compositor de mapa hce que QGIS falle al copiar mezclas de elementos en la página de diseño | [#29747](https://github.com/qgis/QGIS/issues/29747) | [PR #30017](https://github.com/qgis/QGIS/pull/30017) | PORHACER. |
| QGIS falla con vistas PostgreSQL | [#29673](https://github.com/qgis/QGIS/issues/29673) | no se puede reproducir y no pregunta por reintentar |  |
| Browser - \"Project home\" folder shortcut does not appear when a new project is saved | [#29919](https://github.com/qgis/QGIS/issues/29919) | [PR #30025](https://github.com/qgis/QGIS/pull/30025) | PORHACER. |
| Falla al llamar QgsRasterHistogram.histogramVector | [#29700](https://github.com/qgis/QGIS/issues/29700) | [PR #30033](https://github.com/qgis/QGIS/pull/30033) | Hecho |
| Do not offer to \"Import settings from Qgis2?\" if no such settings exist | [#30082](https://github.com/qgis/QGIS/issues/30082) | [PR #30092](https://github.com/qgis/QGIS/pull/30092) | Hecho |
| En gpkg, el constructor de consultas evita la generación automática de la entidad pegada con el mismo campo que la entidad oculta | [#30062](https://github.com/qgis/QGIS/issues/30062) | [PR #30096](https://github.com/qgis/QGIS/pull/30096) | PORHACER. |
| Arrastrar y soltar Geopaquetes desde el sistema de archivos al mapa pierde capas vectoriales, pierde nombres para capas ráster | [#30050](https://github.com/qgis/QGIS/issues/30050) | [PR #30098](https://github.com/qgis/QGIS/pull/30098) | Hecho |
| QGIS falla al intentar identificar una capa con campos duplicados | [#29937](https://github.com/qgis/QGIS/issues/29937) | [PR #30100](https://github.com/qgis/QGIS/pull/30100) | PORHACER. |
| Propiedades de etiqueta no se guardarán a los archivos de proyecto (búfer y fondo) | [#29882](https://github.com/qgis/QGIS/issues/29882) | works for me on release-3_4 and master |  |
| Guardando ediciones a una capa con campo JSON lanza un error | [#30131](https://github.com/qgis/QGIS/issues/30131) | [PR #30137](https://github.com/qgis/QGIS/pull/30137) | Riesgoso? |
| Ajustes de Widget de relación de valor perdida al importar archivo de definición de capa | [#30115](https://github.com/qgis/QGIS/issues/30115) | [PR #30151](https://github.com/qgis/QGIS/pull/30151) | Riesgoso? |
| Unable to add new features in QGIS for PostGIS table using sequence for gid. Data type serial: \'integer overflow\' | [#30041](https://github.com/qgis/QGIS/issues/30041) | [PR #30184](https://github.com/qgis/QGIS/pull/30184) | Hecho |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Prestación: Corrección de Errores por Alexander Bruy
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| v.net.distance - columna de costes de nodos | [#22013](https://issues.qgis.org/issues/22013) | [PR #10060](https://github.com/qgis/QGIS/pull/10060) | Hecho |
| Conversión de shapefile a ráster no funciona | [#21922](https://issues.qgis.org/issues/21922) |  |  |
| GRASS r.in.lidar.info, csólo puede elegir *.txt not the intended* .las | [#21910](https://issues.qgis.org/issues/21910) | [PR #10061](https://github.com/qgis/QGIS/pull/10061) | Hecho |
| SAGA OpenCV Image Analysis | [#21746](https://issues.qgis.org/issues/21746) |  |  |
| SAGA \"saga split rgb bands\" tool is not inside any (SAGA) group of tools | [#21849](https://issues.qgis.org/issues/21849) | [PR #10062](https://github.com/qgis/QGIS/pull/10062) | Hecho |
| r.sun no puede ser ejecutado porque llama a dos opciones incompatibles | [#21637](https://issues.qgis.org/issues/21637) | [PR #10074](https://github.com/qgis/QGIS/pull/10074) | Hecho |
| i.segment (GRASS 7.4.2) solo produce un Raster de buena calidad pero no Raster Segmentados | [#20646](https://issues.qgis.org/issues/20646) | funciona bien en master y 3.4 |  |
| La mayoría de filtros (SAGA) devuelven resultados erróneos si la entrada es .tif | [#22118](https://issues.qgis.org/issues/22118) | inválido |  |
| Interfaz de procesos de Procesamiento por lotes: no hay modo de regresar | [#16893](https://issues.qgis.org/issues/16893) | [PR #10080](https://github.com/qgis/QGIS/pull/10080) | Hecho |
| Error de renombrado de columna PostGIS en el administrador de BD  | [#21425](https://issues.qgis.org/issues/21425) | [PR #10082](https://github.com/qgis/QGIS/pull/10082) | no es necesario |
| El ajuste de texto no funciona en mapas | [#21388](https://issues.qgis.org/issues/21388) | [PR #10081](https://github.com/qgis/QGIS/pull/10081) | Hecho |
| Estilos almacenados en archivos QML con el mismo nombre que la capa no se autocargarán nunca más | [#21691](https://issues.qgis.org/issues/21691) | [PR #14660](https://github.com/qgis/QGIS/pull/14660) | Hecho |
| QGIS 3.4.6 se bloqueó cuando intentó clasificar una capa | [#21693](https://issues.qgis.org/issues/21693) | [PR #29951](https://github.com/qgis/QGIS/pull/29951) | Hecho |
| Solucionado que la tabla no funcione bajo filtro definido por Usuario (SAGA) | [#29999](https://github.com/qgis/QGIS/issues/29999) | [PR #30001](https://github.com/qgis/QGIS/pull/30001) | Hecho |
| Versionado del Administrador de BD:\_la vista actual carece de clave primaria | [#25888](https://github.com/qgis/QGIS/issues/25888) | [PR #30045](https://github.com/qgis/QGIS/pull/30045) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Alexander Bruy](https://bruy.me/)
### Prestación: Corrección de Errores por Victor Olaya
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Processing \"iterate\" does not work anymore | [#21524](https://issues.qgis.org/issues/21524) | [PR #10078](https://github.com/qgis/QGIS/pull/10078) |  |
| Tipo de parámetro erróneo en Filtro Gaussiano SAGA | [#21797](https://issues.qgis.org/issues/21797) | [Commit](https://github.com/qgis/QGIS/commit/83e6dd3efe302de4749d68be23217d8dd4e667d2) |  |
| La matriz de distancia no mantiene el tipo de datos y la precisión para la capa de punto de entrada lineal (N\*k x 3) | [#21501](https://issues.qgis.org/issues/21501) |  |  |
| Processing \"Build virtual vector\" now fails in certain cases | [#21519](https://issues.qgis.org/issues/21519) | [PR #10083](https://github.com/qgis/QGIS/pull/10083) |  |
| Calculadora ráster SAGA carga mas cuadrículas que las seleccionadas cuando se suministra un sdat en XGRIDS | [#22131](https://issues.qgis.org/issues/22131) | [PR #10085](https://github.com/qgis/QGIS/pull/10085) |  |
| Exportar Objetos Seleccionados para generar capa lineal no seleccionable en modelador gráfico | [#21705](https://issues.qgis.org/issues/21705) | [PR #10093](https://github.com/qgis/QGIS/pull/10093) |  |
| Error de Procesamiento por lotes en r.mapcalc.simple | [#29822](https://github.com/qgis/QGIS/issues/29822) |  |  |
| Ayuda para algoritmos no visible en el modelador | [#21536](https://issues.qgis.org/issues/21536) |  |  |
| Correcciones de errores relacionadas con la interfaz por lotes y no estaban vinculadas a informes de errores. Estas son regresiones que se introdujeron en los cambios recientes que noté mientras trabajaba en otro problema | [PR #29948](https://github.com/qgis/QGIS/pull/29948) |  |  |
|  | [PR #29950](https://github.com/qgis/QGIS/pull/29950) |  |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

Esta prestación fue desarrollada por Victor Olaya
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| ENVI driver ignores \"geo point\" (GCP) metadata on reading | [#1528](https://github.com/OSGeo/gdal/issues/1528) | [Commit](https://github.com/rouault/gdal/commit/f2f29cd3a7708a4a9553f127b2d19b3cd72f9180) |  |
| GetFeature de WFS falla en el parámetro TypeNames | [#21768](https://issues.qgis.org/issues/21768) | [PR #29946](https://github.com/qgis/QGIS/pull/29946) | Hecho |
| No puede cargar archivo GPX automáticamente despues de crearlo en QGIS 3.4.7 o QGIS 3.6.2 | [#22005](https://issues.qgis.org/issues/22005) | [PR #29947](https://github.com/qgis/QGIS/pull/29947) | Hecho |
| No se puede crear cache temporal SpatiaLite | [#29819](https://github.com/qgis/QGIS/issues/29819) | [PR #29949](https://github.com/qgis/QGIS/pull/29949) | Hecho |
| Círculo cerrado de PostGIS en Polígonos Curvos no se muestra | [#29895](https://github.com/qgis/QGIS/issues/29895) | [PR #30010](https://github.com/qgis/QGIS/pull/30010) | Hecho |
| Solucionada salida GeoJSON de Multipolígono/Multisuperficie | [PR #30012](https://github.com/qgis/QGIS/pull/30012) | [PR #30012](https://github.com/qgis/QGIS/pull/30012) | No necesitado |
| Las funciones multiparche no se mostrarán más | [#29376](https://github.com/qgis/QGIS/issues/29376) | [PR #30024](https://github.com/qgis/QGIS/pull/30024) | Hecho |
| Multiples problemas y puntos muertos con WFS | [#29258](https://github.com/qgis/QGIS/issues/29258) | [PR #30026](https://github.com/qgis/QGIS/pull/30026) | Hecho |
| Proveedor WFS: Evitar colgado del diálogo de progreso de descarga | [PR #30039](https://github.com/qgis/QGIS/pull/30039) | [PR #30039](https://github.com/qgis/QGIS/pull/30039) | Hecho |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Even Rouault](https://www.spatialys.com/)
### Prestación: Corrección de errores por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Problemas en capas embebidas | [#29678](https://github.com/qgis/QGIS/issues/29678) | [PR #9993](https://github.com/qgis/QGIS/pull/9993) and [PR #10004](https://github.com/qgis/QGIS/pull/10004) |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Prestación: Corrección de Errores por Peter Petrik
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| Editando una entidad Geopaquete con espacios en los nombres de los campos puede hacer fallar QGIS | [#29630](https://github.com/qgis/QGIS/issues/29630) | [PR #29997](https://github.com/qgis/QGIS/pull/29997) | PORHACER. |
| Fallo en la actualización de capa pg | [#29814](https://github.com/qgis/QGIS/issues/29814) | duplicar | N/D |
| Tipo de archivo XMDF desaparecido de la versión Madeira 3.4.5 | [#29381](https://github.com/qgis/QGIS/issues/29381) | inválido | N/D |
| Mesh calculator: crash when \'All Selected Dataset Times\' button clicked | [#30003](https://github.com/qgis/QGIS/issues/30003) | [PR #30005](https://github.com/qgis/QGIS/pull/30005) | N/D |
| Falla al editar campos | [#29200](https://github.com/qgis/QGIS/issues/29200) | no es posible replicar | N/D |
| Cerrando el editor de vértices la aplicación falla. | [#30028](https://github.com/qgis/QGIS/issues/30028) | [PR #30030](https://github.com/qgis/QGIS/pull/30030) | PORHACER. |
| Detached 3D view crash \[macOS\] | [#29169](https://github.com/qgis/QGIS/issues/29169) | no es posible replicar |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Loïc Bartoletti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.4 backport commit (GitHub) |
| --- | --- | --- | --- |
| No pinza al seleccionar punto de rotación | [#29706](https://github.com/qgis/QGIS/issues/29706) | duplicar / no es un bug |  |
| Falla mientras trabaja con almacen virtual de etiquetas y datos definidos | [#30078](https://github.com/qgis/QGIS/issues/30078) | no es posible replicar |  |
| Mejorada la digitalización avanzada por ángulo | [#30133](https://github.com/qgis/QGIS/issues/30133) | no es un error |  |
| Corregido reformado para puntos pinzados con Z | [PR #30108](https://github.com/qgis/QGIS/pull/30108) |  |  |

This feature was funded by [QGIS.ORG donors and sponsors](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://oslandia.com/en/)

{{<content-end >}}
