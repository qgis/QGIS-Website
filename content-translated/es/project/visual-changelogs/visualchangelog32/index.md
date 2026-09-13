---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Fecha de lanzamiento: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Gracias**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Patrocinadores para la versión QGIS 3.2
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## General
### Funcionalidad: Nuevo formato de archivo comprimido de proyecto .qgz es ahora el formato predeterminado
QGZ fue añadido como un formato adicional en 3.0. Tener este formato como el predeterminado facilitará mucho el camino para ir a un contenedor capaz de abarcar recursos como SVG, datos fuera de línea en GPKG, rampas de color, complementos o scripts.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Funcionalidad: Filtrado de valores de campo en Query Builder
Cuando creamos una nueva expresión de filtro en el constructor de consultas, ahora puede filtrar los valores de campo del panel de previsualización.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Funcionalidad: Mapa a pantalla completa via Ctrl-Shift-Tab
Además de Ctrl-Tab ahora puede hacer Ctrl-Shift-Tab, que le mostrará el Mapa y SOLO el Mapa, no más barras de herramientas o botones (o incluso sin Barra de Título de Ventana, en combinación con F11). Ideal para la proyección del mapa en pantalla completa a través de Beamer o en pantallas grandes. ¡Todavía puedes hacer zoom y desplazarte! (Basado en el trabajo de Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Richard Duivenvoorde
## Herramientas de mapa
### Funcionalidad: Herramienta de mapa simplificar ahora también puede suavizar entidades
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Herramienta identificar con opciones extra
Con las nuevas mejoras, el usuario ahora puede usar herramientas similares a la Selección para identificar múltiples entidades.

Esta funcionalidad fue fundada por Leicestershire County Council y East Hampshire District Council

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Funcionalidad: Almacenar también el estado expandido/colapsado de nodos en los Temas de mapa
Cada tema de mapa también registrará qué capas, grupos y elementos de leyenda se expanden, por lo que cuando se selecciona un tema de mapa, los estados expandidos/contraídos se aplican en el árbol de capas.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
Una nueva vista de mapa fue configurada para hacer zoom automáticamente a la selección actual. Podría combinarse con diferentes temas de mapa como en este ejemplo.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Funcionalidad: Elección del método de simplificación para la herramienta de simplificación de mapa
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: agregar zoom a la entidad relatada en los formularios
Aparece un nuevo botón en el subformulario de atributo de entidad cuando se seleccionan uno o más registros en una tabla relatada. El botón acerca el mapa a estas entidades si tienen geometrías.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Esta prestación fue desarrollada por Jürgen Fischer
### Funcionalidad: Áreas/longitudes/perímetros cartesianos en resultados de identificación
En QGIS 3.2 ahora mostramos áreas, longitudes y perímetros elipsoidales y cartesianos por separado dentro del panel de resultados de identificación. Ver las dos medidas distintas les brinda a los usuarios una mejor comprensión de los problemas potenciales en los cálculos de área o distancia causados por una proyección incorrecta o por elecciones de elipsoide.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Expresiones
### Prestación: Nuevas funciones de expresión
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Nuevas variables:
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Esta funcionalidad fue desarrollada por Mathieu Pellerin, Nyall Dawson
### Funcionalidad: Expression Builder más útil
El constructor de expresiones ahora hace mas fácil construir expresiones dentro de QGIS!
- El generador ahora muestra la descripción de los valores definidos por los datos, incluido el rango de valores esperados de la expresión
- Ctrl+clic en el nombre de una función en la expresión actual abrirá automáticamente la ayuda para esa función
- Ahora muestra indicadores para partes de expresiones con errores
- Muestra una lista completa de mensajes de error obtenidos analizando la expresión

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Interfaz de usuario
### Funcionalidad: Panel de capas: Indicadores para capas de mapa filtradas
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

Esto agrega un minimarco para mostrar iconos adicionales en las vistas de árbol de capas junto a los nombres de capas y grupos. El texto de información sobre herramientas puede asociarse con indicadores para proporcionar un contexto adicional para los indicadores. Además, se emite una señal cuando el usuario hace clic en los indicadores y se pueden definir acciones personalizadas. La idea es que los indicadores se puedan usar en el futuro para un sutil informe de varios bits de información, por ejemplo:
- capa de mapa con geometrías inválidas
- capa de mapa con excepciones de reproyección al vuelo
- capa de mapa tiene fuente de datos desaparecida
- capa de mapa con CRS inválido

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### FUncionalidad: Permitir personalizar el prefijo de los filtros de localización
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Funcionalidad: Apertura de vectorial o ráster almacenados en HTTP(s), FTP, o servicios en la nube
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Calculadora rápida en la barra de búsqueda del localizador
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Accesos directos para alternar paneles
Atajo Ctrl+{no}

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Funcionalidad: Marcador de búsqueda en el localizador
Permite buscar marcadores espaciales. Doble Click en el resultado de una búsqueda hará zoom al marcador.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Esta funcionalidad fue desarrollada por Klavs Pihlkjær
### Funcionalidad: Acciones Close y Revert Project
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Esta funcionalidad fue desarrollada por Nathan Woodrow, Nyall Dawson
### Funcionalidad: Indicador de cambios sin guardar en la barra de título
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funconalidad: Demora de consejos de mapas configurables
Esta funcionalidad fue desarrollada por jdugge
### Funcionalidad: Mover capa o grupo a la parte superior del panel de capas
Mueve la(s) capa(s) seleccionada(s) o grupo(s) a la cabeza del panel de capas.

Esta funcionalidad fue desarrollada por Mie Winstrup
### Funcionalidad: Copiar contenido del panel de estadísticas al portapapeles
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Search Settings, Options, y Project Properties páginas desde el localizador
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Esta funcionalidad fue desarrollada por Klavs Pihlkjær
### Funcionalidad: Los indicadores para capas y grupos incrustados
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Simbología
### Funcionalidad: Colores mas agradables para nuevas capas
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Representación
### Funcionalidad: Decoración del Copyright del mapa mejorada
- Soporte de expresión para el texto del copyright.
- Opciones de formato de texto mejoradas, incluyendo sombras, bordes, fondos, etc.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: El tamaño y familia de fuente de la barra de escala de la Ventana principal pueden ser personalizados
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Tamaño y ruta SVG personalizados para la decoración de la flecha de norte
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Administración de datos
### Funcionalidad: Refrescar una vista materializada
Desde el navegador, con click derecho en una capa materializada, ahora puede refrescarla.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Funcionalidad: Soporte de Z y M para edición fuera de línea
La edición fuera de línea ahora también soporta capas con coordenadas Z y M.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcionalidad: Metadatos para proyectos QGIS
Continuando con el trabajo de metadatos iniciado en QGIS 3.0, 3.2 ahora admite metadatos para proyectos QGIS. Esto permite establecer metadatos detallados en las propiedades del proyecto, incluidos resúmenes, palabras clave, detalles de contacto, enlaces, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Esta funcionalidad fue fundada por Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) dentro del proyecto ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Widgets y Formularios
### Funcionalidad: Diseño de varias columnas para widget de relación de valor de selección múltiple
El widget de relación de valor con selección múltiple habilitada ahora admite varias columnas. Esto permite un mejor uso del espacio horizontal de la pantalla.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### Funcionalidad: Permitir el uso de una URL para formularios de atributos personalizados (archivo UI)
El archivo UI se descargará en cada sesión en el primer uso. Esto hace posible distribuir fácilmente los archivos actualizados de la interfaz de usuario a los clientes.

This feature was funded by [SIRS](http://www.sirs-fr.com)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Funcionalidad: Formularios Drill-down (en cascada)
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Esta funcionalidad fue fundada por Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS Danish User Group, Bo Victor Thomsen y Lene Fischer, North River Geographic

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## Leyenda de capa
### Funcionalidad: Texto opcional en la parte superior de los símbolos para capas vectoriales
Esta funcionalidad permite a los usuarios añadir información extra a los símbolos en la leyenda.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Funcionalidad: Copiar&Pegar Grupo/capas desde un proyecto QGIS a otros.
Permitiendo copiar y pegar grupos o capas entre proyectos y perfiles.

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## Compositor de Mapa
### Funcionalidad: Fuente de tabla definida por datos para elementos de tabla de atributos
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(Todos los atributos de tabla existentes (configuración de columna) se dejan intactos, por lo que establecer una tabla definida por datos en una capa con diferentes campos dará como resultado columnas vacías en la tabla).

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Metadatos del proyecto incrustados en exportaciones de diseño
Guardar un diseño de impresión en SVG, PDF o imágenes ahora incrustará cualquier metadato del proyecto en el archivo creado. La compatibilidad con diferentes elementos de metadatos depende del formato de exportación individual.

Esta funcionalidad fue fundada por Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) dentro del proyecto ERIKUS

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Mejor formato para el texto de la barra de escala
QGIS 3.2 permite utilizar la gama completa de opciones de formato de texto dentro del texto de la barra de escala, p. ej. buffers, sombras y formas de fondo.

Texto de la barra de escala ilegible es cosa del pasado!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Procesado
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Funcionalidad: Cargar script desde modelo
Nueva opción para cargar scripts de Procesamiento desde un modelo personalizado

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Funcionalidad: Algoritmo de filtrado de entidades para procesar modelos
Agregar un nuevo algoritmo de filtro de entidades para el modelador de procesamiento. Permite filtrar entidades de una fuente basada en expresiones y enviar entidades coincidentes a diferentes salidas como productos finales o canalizaciones de algoritmos diferentes para su posterior procesamiento.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Funcionalidad: Histograma Zonal
Este nuevo algoritmo agrega campos que representan recuentos de cada valor único de una capa ráster contenida dentro de zonas definidas como polígonos.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: portar Union, algoritmos de diferencia e intersección a C ++
Los algoritmos de geoprocesamiento nativos de QGIS se han portado de Python a C ++. Además del aumento de rendimiento, se han resuelto varios errores con esta actualización.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
Este nuevo algoritmo de procesamiento proyecta puntos desde una capa de puntos de entrada por una distancia y rumbo especificados (acimut). Admite parámetros dinámicos para la distancia y rumbo, de modo que la distancia y la demora pueden tomarse de los valores de campo o expresiones.

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Valores de parámetros dinámicos para mas algoritmos
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

En 3.2 los siguientes algoritmos ahora soportan parámetros dinámicos:
- Borrar huecos
- Borrar Vértices duplicados
- implificar
- Suavizar
- Anclar a la malla
- Subdividir
- Transectar
- Trasladar

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funconalidad: algoritmo de Buffer multi-anillo (distancia constante)
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Esta prestación fue desarrollada por Alex Bruy
### Feature: New \"segmentize\" algorithms
En QGIS 3.2 dos nuevos algoritmos para segmentar geometrías curvas han sido añadidos a Procesamiento.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Opción de crear puntos en todas las partes poligonales
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Algoritmo para rotar entidades
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Importar fotos geoetiquetadas
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Opcionalmente, el escaneo puede ser recursivo y puede crear una tabla opcional de fotos que no se pudieron leer o que le faltaban geoetiquetas.

El algoritmo establece automáticamente la tabla de salida para usar un widget de recursos externo para mostrar las fotos vinculadas en el formulario de atributo.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: algoritmo para Intercambiar valores de coordenadas x/y
Este algoritmo intercambia los valores de coordenadas X e Y en las geometrías de entrada. Se puede usar para reparar geometrías que accidentalmente han invertido sus valores de latitud y longitud.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
Este cambio permite a los usuarios establecer opcionalmente un orden de clasificación para usar al asignar valores en el algoritmo Agregar campo incremental. Anteriormente, los valores siempre se agregaban utilizando el orden de las entidades originales. Con este cambio, los usuarios pueden controlar el orden en que se asignan los valores a las entidades.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Indicador para parámetro de unidades de distancia
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Además, si la unidad está en grados, se muestra un pequeño icono de advertencia junto al parámetro. La información de herramienta para este icono aconseja a los usuarios que vuelvan a proyectar datos en un sistema adecuado de coordenadas local proyectado.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Registro de algoritmos puede ser salvado/limpiado/copiado
En el cuadro de diálogo de ejecución del algoritmo, se han agregado nuevos botones para permitir a los usuarios guardar el registro actual (en archivos de texto o HTML), copiar el contenido del registro en el portapapeles y borrar el registro.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Algoritmo de Búfer en cuña
Este nuevo algoritmo crea bufers de formas acuñadas a partir de los puntos de entrada.

El parámetro azimut proporciona el ángulo (en grados) de la mitad de la cuña al punto. El ancho del búfer (en grados) se especifica mediante el parámetro ancho. Tenga en cuenta que la cuña se extenderá a la mitad del ancho angular a ambos lados de la dirección del acimut. El radio externo del búfer se especifica a través del radio externo, y opcionalmente también se puede especificar un radio interno.

El algoritmo soporta parámetros dinámicos para azimuth, anchura y radio.

La salida nativa de este algoritmo son geometrías CurvePolygon, pero pueden segmentarse automáticamente a Polígonos según el formato de salida.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Anchura variable de búfer
Se han agregado nuevos algoritmos de procesamiento para crear búferes de ancho variable, incluidos los búferes cónicos (con un diámetro inicial y final especificado) y los búferes de ancho variable a partir de los valores de la cadena de línea m.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: algoritmos de reclasificación ráster
Se han agregado dos nuevos algoritmos de reclasificación de ráster QGIS nativos al procesamiento. ¡Estos son fáciles de usar, también rápidos y estables, y funcionan para CUALQUIER tipo de capa ráster compatible con QGIS!
- Reclasificar por capa: reclasifica un ráster utilizando los rangos especificados a través de los campos min/max/valor de una tabla de vectores
- Reclasificar por tabla: reclasifica un ráster utilizando una tabla fija ingresada por los usuarios en el diálogo del algoritmo

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: algoritmo de unión con una capa simple
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Opciones de Aplicación y Proyecto
### Funcionalidad: Capas obligatorias en el proyecto
No se permite eliminar las capas requeridas del proyecto. Esto agrega seguridad adicional para proteger a los usuarios del proyecto de eliminar capas que puedan pensar que no son necesarias (por ejemplo, usadas en uniones, relaciones, expresiones)

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Funcionalidad: Guardando y cargando proyectos en la base de datos PostgreSQL
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Navegador
### Funcionalidad: Guardar/Cargar conexiones para teselas XYZ
Desde el panel del navegador, las entradas de teselas XYZ se pueden exportar/importar a /desde un archivo XML.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Funcionalidad: La ruta de inicio del proyecto se puede configurar manualmente
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Las rutas de inicio del proyecto también se pueden establecer en rutas relativas, en cuyo caso serán relativas a la ubicación guardada del proyecto.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Proveedores de datos
### Funcionalidad: Soporte para capas de malla
El trabajo inicial se ha realizado para introducir capas de malla que admitan la visualización de datos en mallas estructuradas o no estructuradas (cuadrículas) además de las capas ráster y vectoriales. Esto todavía es un trabajo en progreso, se espera que esté completamente listo en QGIS 3.4. Hasta ahora, el trabajo condujo a la creación de una nueva biblioteca MDAL para el manejo de diferentes formatos de datos basados en malla y hay nuevas API introducidas bajo cubierta, sin embargo, la interfaz de usuario aún no está implementada.

Para mas información ver:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

y

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Funcionalidad: Establecer automáticamente el estilo predeterminado para capas de ArcGIS Feature Server
Cuando las capas de un servidor de entidades se cargan en QGIS 3.2, se aplicará automáticamente el mismo estilo que el especificado para esa capa en el servidor, coincidiendo con la apariencia de la capa cuando se carga en ArcGIS.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funconalidad: Consultas de Oracle mas rápidas
Ciertas operaciones se aceleran considerablemente para las capas de Oracle, p.ej. caso de que las mayúsculas y minúsculas no coincidan para las entidades.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Restringir la lista de tablas para una conexión de base de datos Oracle a un esquema preestablecido
Este cambio permite establecer un esquema en las propiedades de conexión para una conexión de base de datos Oracle. Si está configurado, solo las tablas dentro de ese esquema serán escaneadas y listadas para la conexión.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Funcionalidad: Soporte de solo lectura para geometrías curvas de Oracle
Previamente estas geometrías eran descartadas silenciosamente.

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Plugins
### Funcionalidad: Añadiendo historial de consultas en el DB Manager
En 3.2 es posible almacenar consultas SQL. El historial de consultas está disponible en la pestaña de la ventana SQL del complemento Administrado de BD.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Funcionalidad: Ejecución DB Manager SQL en segundo plano
Esta funcionalidad fue desarrollada por Paul Blottiere
## Objetos 3D
### Funcionalidad: Polígonos 3D: Opcionalmente genera caras posteriores
A veces, los conjuntos de datos con polígonos en 3D no tienen un orden consistente de vértices (en sentido horario versus en sentido antihorario) y eso causó resultados subóptimos en la vista 3D: o bien algunos polígonos (paredes) parecen faltar si se habilita sacrificar la cara posterior - o algunos polígonos están sombreados incorrectamente si el descarte posterior está desactivado. Con la nueva opción **Agregar caras posteriores** habilitada, el teselador generará triángulos en ambas direcciones (anverso y reverso), lo que mejora en gran medida la calidad de representación para dichos conjuntos de datos.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

La imagen contiene el conjunto de datos de edificios 3D de Praga disponible gratuitamente.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
