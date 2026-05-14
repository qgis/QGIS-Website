---
HasBanner: false
draft: false
releaseDate: '2022-06-17'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.26
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.26{#changelog326 }
![image1](images/projects/916ce336f8f5939eb158506ea38290af6f1ce0f0.png)

Fecha de lanzamiento: 2022-06-17

QGIS 3.26 Buenos Aires viene con muchísimas funcionalidades e incluye una vasto número de mejoras en un conjunto de funcionalidades avanzadas. Esto incluye numerosas mejoras en las capacidades 3D, mejoras en las herramientas para nubes de puntos, y la introducción de un nuevo sistema de visualización de perfiles para la creación de secciones transversales y perfiles de elevación. Lo mejor es que este nuevo sistema de ploteo usa las capacidades nativas de QGIS para el renderizado en incluye toda la simbología, estilos y propiedades controladas por datos que todos ya conocemos.

For a whirlwind tour of all the new functionalities introduced, you can view the highlight reel video on YouTube at <https://youtu.be/pZmrw_zR7sA>

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/pZmrw_zR7sA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

The QGIS Community has also been active in various crowd-funding campaigns, [Open Day events](https://github.com/qgis/QGIS/wiki#qgis-open-day), and the growth of the [STAC Ecosystem](https://medium.com/radiant-earth-insights/stac-updates-february-2022-e02a194861e) has led to inter-agency collaboration initiatives which include outcomes such as the [STAC Browser QGIS Plugin](https://stac-utils.github.io/qgis-stac-plugin/), which make it nearly trivial to produce [Raster Mosaics](https://www.youtube.com/watch?v=se2Xd7CKhHg) from Earth Observation data using Open Source and Open Data. There is also a new [online analytics dashboard](https://blog.qgis.org/2022/06/16/qgis-userbase-analytics/) which collects information from the QGIS Feed in an attempt to show how and where QGIS is being used, providing valuable insight to developers and the QGIS community.

We would also like to extend a big thank you to the developers, documenters, testers, and the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [list of donors](https://qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our sustaining member page for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es un software libre y no estás obligado a pagar nada por utilizarlo. De hecho, queremos animar a la gente a utilizarlo, independientemente de su situación económica o social, ya que creemos que dotar a la gente de herramientas para la toma de decisiones espaciales dará lugar a una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Cambios que eliminan funcionalidades
### Funcionalidad: Eliminado el soporte para DB2
El proveedor para DB2 ha sido marcado como obsoleto y eliminado de la interfaz de QGIS desde hace unas cuantas versiones. Como no se ha presentado ningún desarrollador para mantener el soporte a este proveedor de datos, ha sido eliminado y ya no estará disponible en QGIS.
## Herramientas de mapa
### Funcionalidad: Seleccionar todos los objetos según el valor de un atributo desde el panel de resultados de indentificación
Las herramientas de resultados de identificación ahora tienen disponible una opción desde el menú contextual del valor de un campo que permite seleccionar rápidamente todos los objetos de una capa que tenga el mismo valor.

![image3](images/entries/d2f2d4bf5b05b7e21aa6ff0957ad8be8ccda082f.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Interfaz de usuario
### Funcionalidad: Orden de coordenadas dependiente del SRC
QGIS ahora usará el orden de coordenadas correspondiente al SRC del proyecto cuando se muestren las coordenadas en la barra de de estado (y en los resultados de identificación). Se ha añadido una opción en las propiedades del proyecto para anular esto si se desea un orden de coordenadas en específico.

Específicamente, esto significa que de ahora en adelante, los proyectos con SRC geográficos (como EPSG:4326), mostraran primero la latitud y en segundo lugar la longitud (a no ser que SRC tenga definido un orden diferente).

![image4](images/entries/7dada94231069c7f647d9a4a239d57506ad14bfd.gif)

Está funcionalidad fue financiada por SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Seleccionar objetos mediante símbolos basados en expresiones
A \"Select Features\" action has been added to the right click context menu on legend class symbols. This allows you to rapidly select all features within a layer that match the associated symbol class in categorized, graduated, and rule based renderers.

![image5](images/entries/965a5e626ced053fd00fc33288c17330b7f920a0.gif)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Copia el valor de previsualización de una expresión al portapapeles.
Se ha añadido un nuevo botón a la interfaz del constructor de expresiones que permite copiar en el portapapeles el valor del campo de vista previa de la expresión.

![image6](images/entries/0ecfdc2b0f6dae82ab5650f4d1d97d37df33aee4.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com/)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
### Funcionalidad: Opción para sincronizar el panel de estadísticas con selección capa
A \"Keep synchronized with TOC\" checkbox has been added to the statistics panel, which allows the statistics panel to automatically synchronize with the table of contents layer list, ensuring that the active layer is selected for the computed statistics displayed in the statistics panel.

La última expresión usada para definir las estadísticas de una capa se guardará para cada capa.

![image7](images/entries/0075fa6cc3b8410072eeec8bb43ac4cef4c38e61.webp)

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
### Funcionalidad: Implementada la acción de "scroll" para botones de símbolos y colores.
Realizar una acción con la rueda del ratón cuando estemos sobre un capa con símbolos ahora ajustará automáticamente uno de los atributos del estilo. Esta funcionalidad afecta a diferente estilos de diferentes formas, dependiendo de qué control de la interfaz se seleccione.
- Para símbolos con marcadores, el tamaño del marcador aumenta/disminuye.
- Para símbolos de líneas, el ancho de la línea crece/decrece.

Además, cuando usemos la rueda del ratón sobre un símbolo de color, la opacidad del color aumenta/disminuye.

![image8](images/entries/ab668355973259b389bd2623c4b1ba01b5e8f237.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Accesibilidad
### Funcionalidad: Desplazamiento horizontal en tablas con mayúsculas+rueda del ratón
Ahora en las tablas de atributo podemos desplazarnos horizontalmente usando la combinación de teclas mayúsculas + rueda del ratón, alternando el desplazamiento vertical que ocurre por defecto.

This matches the behavior exposed by LibreOffice, and provides a convenient way to quickly horizontally scroll tables when a mouse doesn\'t have a dedicated horizontal scroll wheel.

![image9](images/entries/7bf2a8d0d0500149ed7b1cb5edb22b8cd6258c86.gif)

Esta funcionalidad fue financiada por the City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Simbología
### Feature: New \"Animated Marker\" symbol type
Un nuevo tipo de símbolo para marcadores permite que los puntos sean dibujados usando un marcador animado, usando un gif, webp, o mng animado. Hay opciones para el archivo que se va a usar, el tamaño, el ángulo y la tasa de cuadros por segundo (fps).

Hay dos formas en las que se manejan los símbolos animados.
- Si el mapa NO es considerado una animación (i.e. un proyecto normal de QGIS), entonces el cuadro a dibujar será definido unicamente por la marca de tiempo actual (la hora).
- Si el mapa en si mismo es considerado una animación, entonces el cuadro dibujado para el marcador animado está basado en el cuadro de la animación y la tasa de cuadros por segundo del mapa. Este es el caso cuando el controlador temporal está configurado en modo Animación. En este caso, los marcadores animados seguirán la animación de controlador temporal, e.g. pausando cuando la animación sea pausada, avanzando cuadros con la animación, etc. Este modo también aplica cuando estemos exportando una animación desde el controlador temporal y es usado cuando un complemento especifica la tasa de cuadros y las propiedades del cuadro actual.

![image10](images/entries/e5330839c8c13220ccbbb2ea1c5fc556548a21be.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Permitir que cualquier símbolo sea un símbolo animado
Users can now indicate that a symbol should be treated as an animated symbol, through the new \"Animation Settings\" option in the symbol widget\'s Advanced menu.

This settings panel allows users to enable animation for the symbol and set a specific frame rate at which the symbol should be redrawn. When enabled, the \@symbol_frame variable can be used in any symbol data defined property in order to animate that property.

For instance, setting the symbol\'s rotation to the following data defined expression will cause the symbol to rotate over time, with rotation speed dictated by the symbol\'s refresh rate.

    @symbol_frame % 360
    
![image11](images/entries/c5c8938147137d9264d57a56c00548cc535cdaa2.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Add a new classification method for \"Fixed interval\"
Permite a los usuarios crear intervalos graduados usando una anchura de intervalo especifica para clases (en lugar del número total de clases).

![image13](images/entries/5f4efe2866e8ba166c3948fb22946ec1ed3fa02b.gif)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: El panel de patrones para líneas muestra la longitud total del patrón
El panel de patrones de línea personalizados ahora muestra la longitud total del patrón, mejorando la habilidad de los usuarios para emparejar la longitud en conjunto del patrón con tamaños de otras partes de un símbolo.

![image14](images/entries/201cc3be8689d55102c675c4af0ffdf4204c2a2b.webp)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Seleccionar la categoría de un estilo cuando se almacenen estilos en base de datos
QGIS soport el almacenamiento de estilos de capa en base de datos de origen, o en la base de datos de estilos local. QGIS luego proporciona la habilidad de usar esos estilos como el estilo por defecto de una capa, o proporciona acceso al estilo a través del gestor de estilos.

En anteriores versiones de QGIS, este proceso almacenaba todos los estilos disponibles en la base de datos, sin embargo la nueva funcionalidad permite a los usuarios qué categoría en especifico deben almacenarse, proporcionando un nivel de flexibilidad para guardar estilos en bases de datos similar a la que previamente estaba disponible solo para los formatos de estilo QML y SLD.

![image15](images/entries/0bd238b2326485fe91d8dd6f2aa8956e5534a5e3.webp)

This feature was developed by [Jacky Volpes](https://github.com/Djedouas)
## Etiquetando
### Funcionalidad: Permitir el control mediante datos sobre el tipo de anclaje para lineas
Allows data-defined control over whether the \'hint\' or \'strict\' anchoring type is used.

Esta funcionalidad fue financiada por City of Freiburg im Breisgau

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Control la ubicación del anclaje para etiquetas relativa a la posición del texto
Se proporciona un control para definir que parte del texto (inicio, mitad, o final) de las etiquetas para lineas corresponde a la posición del anclaje en la colocación de etiquetas. Este permite mayor precisión en la colocación de etiquetas de acuerdo a requerimientos específicos, como, por ejemplo, alinear el final del texto de una etiqueta con una punto en específico de un objeto de tipo línea.

En anteriores versiones de QGIS, las etiquetas siempre estaban centradas sobre la posición del anclaje en líneas, a no ser que fuera una etiqueta curva, en las que se usaba el principio de la etiqueta para determinar la orientación del anclaje.

A new option for \"Follow placement\" has also been added, which means that the text anchor will depend on the placement along line setting. This control attempts to determine the appropriate alignment option automatically according to the label placement on the feature and exhibits the following behaviors:
- Para etiquetas ancladas cerca del inicio de la línea (0-25%), la ubicación del anclaje será el **inicio** del texto de la etiqueta.
- Para etiquetas ancladas cerca del final de la línea (0-75%), la ubicación del anclaje será el **final** del texto de la etiqueta.
- Para ubicaciones de anclaje entre 25 y 75%, la ubicación del anclaje será el **centro** del texto de la etiqueta.

Esta funcionalidad fue financiada por City of Freiburg im Breisgau

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com/slyr/)
### Funcionalidad: Mover de forma interactiva las etiquetas de líneas curvas a lo largo de la línea
Placement of curved label text can now be manipulated by using the interactive \"Move Labels\" tool.

![image16](images/entries/31ad531d280be178c752850a8860a95f2b8c3bf2.gif)

Esta funcionalidad fue financiada por City of Freiburg im Breisgau

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Representación
### Funcionalidad: Remuestreo  en proveedores WMS
Siguiendo la habilidad de QGIS 3.24 para convertir teselas ráster WMS en datos de elevación, QGIS ha sido consecuentemente mejorado para incluir varios métodos de remuestreo para reducir los artefactos de renderizado en fuentes de datos DEM WMS, tales como el pixelado encontrado en durante el renderizado de sombreados.

![image17](images/entries/60b9ae3354e9c6e2086986aee3b0828dc738187f.gif)

This feature was funded by [Maptiler](https://www.maptiler.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](http://www.lutraconsulting.co.uk)
### Funcionalidad: Vectorización con enmascaramiento selectivo
QGIS introduced a selective masking feature in [version 3.12](https://changelog.qgis.org/en/qgis/version/3.12/#selective-masking), however the implementation relied on the rasterization of the map products and made it unsuitable for some cartographic work.

Esta funcionalidad, largamente esperada, implementa el enmascaramiento selectivo de manera que vectoriza objetos enmascarados o recortados siempre que sea posible, permitiendo resultados de alta calidad en formatos vectoriales tales como SVG o PDF cuando se usa la funcionalidad de enmascaramiento de QGIS.

This is implemented in line with [QEP 186](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/186).

![image18](images/entries/c717fac5bdd68a9f803738c77a5637fc070823e0.webp)

This feature was developed by [Julien Cabieces](https://github.com/troopa81)
## Objetos 3D
### Funcionalidad: Soporte para transparencia en materiales 3D Phong
Proporciona soporte para renderizar objetos semi-transparentes en 3D. Presenta un control de opacidad para el menú de materiales phong, que por defecto está al 100% (totalmente opaco).

![image19](images/entries/38a2c9b60971a3056d2749373b2153e59eb0b3e1.webp)

This feature was funded by [Swedish QGIS user group.](https://www.qgis.se/)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](http://www.lutraconsulting.co.uk)
### Funcionalidad: Los mapas 3D heredan la configuración del proyecto
Cuando se crea un nuevo mapa 3D en un proyecto, el mapa usará la misma configuración del terreno definida en el proyecto. Esto hace que sea más sencillo crear y destruir mapas 3D, sin tener que volver a configurar las opciones del terreno cada vez.

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Sincronizar la navegación 2D y 3D
A new \"Navigation sync\" setting for 3D map frames provides the ability to automatically synchronize the 2D main map canvas extent and the 3D viewport based on various navigation options.
- Opción 1: Siempre que la cámara es desplazada en la vista 3D, la extensión del lienzo del mapa principal (2D) se colocará en el mismo área.
- Opción 2: Cualquier cambio en la posición del lienzo del mapa principal (2D) resultará en un cambio en la orientación de la cámara 3D para ver aproximadamente la misma extensión desde arriba (posición NADIR - perpendicular al terreno).
- Opción 3: Un área trapezoidal representando el campo de visión del mapa 3D se dibujará sobre el lienzo del mapa principal (2D).

Hay acciones disponibles para rápidamente activar o desactivar estas opciones.

![image20](images/entries/9438a5861c6891d7123bdba4918fd4cd9da82343.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](http://www.lutraconsulting.co.uk)
### Funcionalidad: Eje tridimensional en la vista del mapa 3D
Una eje tridimensional ha sido añadido a la vista del mapa 3D para mejorar la orientación de los usuarios.

Esto incluye opciones para:
- Mostrar el eje para X/Y/Z o usar Norte/Este/Sur/Oeste en función del sistema de referencia de coordenadas (SRC).
- Visualización de un cubo etiquetado con caras en lugar de las típicas flechas de eje

![image21](images/entries/bc7d732eed29aa4c9cd5a3888d2b80262960f41a.gif)

This feature was developed by [benoitdm-oslandia](https://github.com/benoitdm-oslandia)
## Nubes de Puntos
### Funcionalidad: Triangulación de nubes de puntos en vistas 3D
QGIS ahora puede renderizar capas de nubes de puntos como superficies solidas en vistas 3D , lo cual se obtiene mediante triangulación 2.5D.

La triangulación se configura mediante un checkbox en las opciones de estilizado en 3D, y las opciones de configuración permiten la exclusión de triángulos que superen, umbrales definidos por el usuario, de anchura y altura.

Esta triangulación esta disponible para todos los estilos de renderizado de nubes de puntos 3D, incluido color único, rampa de color, clasificación, y RGB.

![image22](images/entries/4b103066398ae065f4e3eb1e898356fceda8ef1d.webp)

This feature was developed by [Vincent Cloarec](https://github.com/vcloarec)
### Funcionalidad: Soporte para nubes de puntos optimizadas para la nube (COPC).
QGIS ahora soporta la lectura de nubes de puntos optimizadas para la nube desde fuentes de datos locales o remotas.

For more information on the COPC format, visit <https://copc.io/>.

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](https://www.lutraconsulting.co.uk/)
### Funcionalidad: Filtrado de nubes de puntos
Se ha añadido soporte para filtrado de nubes de puntos, incluyendo la herramienta gráfica para consultas. Usando expresiones de filtrado sobre xyz y/o atributos LAS, se puede observar las nubes de punto filtradas tanto en el mapa 2D como vistas 3D.

![image23](images/entries/a86ac2e8e5f5f1dbdc9630e2b71d4e62686362d9.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
### Funcionalidad: Sincronización de estilos de nubes de puntos
A new \"Follow 2d renderer\" style for 3D point cloud symbology allows for a point cloud layer\'s 3D symbol to be kept in sync with its 2D counterpart. Any changes to the 2D symbology will be automatically applied to the 3D symbology.

![image12](images/entries/9fde94a418b67018b72ad7d0e71c01cf9bc19afa.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
### Funcionalidad: Mejoras en la simbología por clases
La simbología por clases para las nubes de puntos ha sido mejorada para:
- Mostrar unicamente clases que estén presentes en el conjunto de datos (en lugar de una lista pre-definida) y mostrar clases no estándar.
- Mostrar el porcentaje de puntos en cada clase
- Funcionar también con otros atributos (número de retorno, número de retornos, origen de puntos y algunas otras clases).

![image55](images/entries/74d4c97f9c4d402e928893c88f331e9.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Lutra Consulting (Stefanos Natsis)](http://www.lutraconsulting.co.uk)
## Diseño de impresión
### Funcionalidad: Aplicar las opciones para fuentes en estilos condicionales para capas en las tablas de atributos del diseñador de impresión.
Anteriormente, solo las opciones de color de fuente y color de fondo era aplicadas a las tablas en el diseñador de impresión. Opciones adicionales de configuración tales como familia de la fuente, negrita, itálica, tachado y subrayado son aplicadas desde reglas condicionales.

![image24](images/entries/a15e95f80ef5f86dd2de37e4e1642984db89f8a9.gif)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Opciones definidas por datos para la barra de escalas.
Añade opciones definidas por datos para el objeto barra de escala del diseñador de impresión. Está opción es útil cuando se esté generando un atlas con la barra de escala definida en un campo de la capa que define el atlas. El mapa actualmente puede configurarse con estas opciones pero no la barra de escala. Esta funcionalidad implementa #48084, que permite que las propiedades de la barra de escala sean definidas mediante datos.

![image56](images/entries/d3e680f3e4facc9078e4755045152d57f7dc680f.webp)

This feature was developed by [Ethan Snyder](https://github.com/esnyder-rve)
## Expresiones
### Funcionalidad: Operadores Between/Not between
QGIS now includes support for SQL-like `BETWEEN` and `NOT BETWEEN` operators in expression clauses.

![image25](images/entries/01fbc5c6454d48b126daa9597332ca8e94811608.gif)

Esta funcionalidad fue financiada por Kanton Solothurn

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Funcionalidad: Variable padre estática en funciones de agregación
En anteriores versiones de QGIS, las expresiones de agregación no pasaban los parámetros del objeto padre como variables estáticas, lo que imposibilitaba que fueran ejecutadas por el proveedor de datos (e.g. PostgreSQL). Este cambio tiene como resultado la mejora de rendimiento en muchas de las funciones de agregación. Por ejemplo, en la expresión aggregate.

`IF(aggregate(layer:='parks',aggregate:='count', expression:= 't_id', filter:=intersects( $geometry, geometry(@parent))) < 1, 'FALSE', 'TRUE')`

The execution of the `intersects( $geometry, geometry(@parent))` filter will be performed on the data provider directly.

This feature was funded by [Amt für Geoinformation Kanton Schaffhausen](https://agi.sh.ch)

This feature was developed by [David Signer](https://github.com/signedav)
## Digitalizando
### Funcionalidad: Añadir una opción para evitar que se abra automáticamente la herramienta de edición de vértices
The vertex tool dock now has a new checkbox for \"Auto-open table\", which is checked by default and retains the existing behavior.

Si un usuario opta por desmarcar esta opción, entonces se desactivará la auto-apertura de este menú.

Esto es deseable cuando:
- The user is editing in a full screen session with docks hidden, and doesn\'t want the vertex editor dock to keep opening itself
- The user has a heavily customized setup of stacked/tabbed/rearranged docks, and doesn\'t want the vertex editor dock to keep appearing and disappearing and causing other docks to be rearranged

If a user has opted out of the auto-open table behavior, then the dock can be closed and won\'t show immediately when switching to the vertex tool. The dock can then be re-opened either through the standard Views - Panels menu (or by right clicking a toolbar), OR through a new \"Show Vertex Editor\" action which has been added to the dropdown menu for the vertex editor toolbar button.

![image26](images/entries/b8569c513e1dffa0fabb253e8074588d44cce5eb.gif)

Está funcionalidad fue financiada por SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Funcionalidad: Integrar herramientas de formas en la digitalización de objetos
Las herramientas de formas han sido aumentadas e integradas con las funciones de las herramientas de digitalización, de manera que éstas pueden ser utilizadas durante la digitalización

Este incluye el soporte en la digitalización de objetos tales como:
- StraightSegments
- CircularStrings
- Streaming
- Formas

Esto tiene como resultado la habilidad de poder usar las herramientas de añadir parte, añadir anillo, o cualquier otra operación de digitalización para operaciones de digitalización híbridas, por ejemplo, usar la herramienta de arcos circulares o formas rectangulares para crear anillos en polígonos.

This required significant refactoring and the porting of code from `QgsMapToolDigitizeFeature` to `QgsMapToolCapture`.

![image27](images/entries/c0a8faef50107305ea8a04e92f68f9d7518507ff.gif)

This feature was developed by [Denis Rouzaud](https://github.com/3nids)
### Funcionalidad: Nuevas restricciones para el panel de digitalización avanzanda
El panel de digitalización avanzada ahora incluye dos restricciones suaves (guías de autoensamblado) para permitir a los usuarios capturar posiciones relativas a objetos existentes. Estas restricciones se pueden activar e incluyen: 
- **Extensión de línea**: QGIS proveerá una restricción que traza la extensión de una línea, basado en la orientación de un segmento definido por el segmento seleccionado.
- **Vértice xy**: QGIS provee una restricción que corre perpendicular a un vértice existente en orientación vertical u horizontal.

![image28](images/entries/4a68cb3c6e9a4f55c5f95ca4b827405ce0aed526.gif)

This feature was funded by Métropole Européenne de Lille \@Jean-Roc

This feature was developed by [Antoine Facchini](https://github.com/Koyaani)
## Administración de datos
### Feature: Add a \"filter rules\" search box to vector tile renderer and labeling widgets
Ahora los usuarios pueden filtrar las reglas visibles por una parte de su etiqueta, capa o cadenas de filtro. Esto puede ayudar mucho a encontrar reglas en estilos de mosaico vectorial complejos.

![image29](images/entries/1cb1d1557bac8d4552a3ef617a27e0fcf9c082ff.gif)

This feature was funded by [North Road Consulting](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Nombres de campo definidos por el usuario en la exportación
Al exportar capas, ahora los usuarios pueden anular los nombres de los campos en las capas resultantes.

La interfaz de los campos de diálogo de exportación incluye los siguientes cambios:
- A new \"Export names\" column has been introduced to the fields table
- Existe una cómoda casilla de verificación para generar automáticamente alias o volver a los nombres de campo originales.
- When field names are modified by the user, the checkbox will display a \"PartiallyChecked\" state indicator

![image30](images/entries/77669a9cc8355f9fae0e331a28de7ace46e730d6.gif)

Esta funcionalidad fue financiada por el Grupo de Usuarios de QGIS de Suiza

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
### Prestación: Georreferenciación de capas vectoriales en el georreferenciador
QGIS soporta ahora la georreferenciación de capas vectoriales en la herramienta de georreferenciación. Esto permite georreferenciar interactivamente capas vectoriales sin referenciación espacial, o volver a referenciar capas con referenciación, de forma similar a los datos ráster. La georreferenciación se produce en una tarea, por lo que QGIS debería seguir respondiendo, incluso con grandes conjuntos de datos.

Based on [#41386](https://github.com/qgis/QGIS/pull/41386)

![image31](images/entries/b6e89fcd31aec118497af05f94586d2bbf6f4491.gif)

Esta función ha sido financiada por el grupo de usuarios danés de QGIS.

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Añadir capacidades de gestión de dominios de campo al navegador
Se ha añadido una nueva API para gestionar dominios de campo a través de conexiones a bases de datos, y QGIS expone ahora esta funcionalidad a través del panel del navegador.

En la actualidad, esta función sólo está disponible para GeoPackages, pero en el futuro podría estar disponible para otros proveedores.

Esta funcionalidad incluye la posibilidad de crear nuevos dominios de campo, así como establecer el dominio de campo para los campos de la tabla GeoPackage.

![image32](images/entries/e5f0feb4e3c4d925c98336d8938170ac9bb9fc1c.gif)

Esta prestación ha sido financiada por Provincie Gelderland

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Edición transaccional en búfer
Con este modo de edición, todas las capas editables se conmutan de forma sincrónica y todas las ediciones se guardan en un búfer de edición local. El guardado de los cambios se ejecuta dentro de una única transacción en todas las capas (por proveedor).

This new edit mode attempts to provide a hybrid alternative for managing the data editing approaches used in the current editing modes, local edit buffers and transactional editing, and is implemented in line with [QEP 203](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/203)

![image33](images/entries/c7c3eea32a0cf34a07a9325fd87fdefcf8afb280.webp)

Esta prestación ha sido financiada por Kanton Glarus

This feature was developed by [Damiano Lombardi](https://github.com/domi4484)
## Widgets y Formularios
### Prestación: Acceso a referencia de formulario en acciones de formulario python
The form instance, or `QgsAttributeForm` object, has now been exposed to the Python API for Drag and drop form actions.

Esto significa que los usuarios de QGIS pueden ahora hacer referencia al formulario actual y producir acciones que cambien los valores dentro del propio formulario, como restablecer los valores por defecto o acciones rápidas para aplicar otros preajustes definidos por el usuario.

This implementation has been done in line with [QEP 251](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/251)

![image34](images/entries/8f71244038218dae15182ee507699de0050b405d.gif)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Permitir la personalización de la fuente y el color de las etiquetas de los formularios mediante arrastrar y soltar
Ahora es posible personalizar el tipo de letra y el color de las etiquetas de los formularios y los títulos de los grupos o pestañas en la interfaz Arrastrar y soltar desde el diseñador.

![image35](images/entries/df03bff457eac65712cad54d0acee177526a3f13.webp)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
### Prestación: Contraer grupo de formularios por expresión
Ahora hay nuevas opciones de configuración disponibles para los cuadros de grupo de formularios de arrastrar y soltar que permiten especificar una expresión para definir si un grupo de formularios debe colapsarse.

![image36](images/entries/d601af9dff97189a63c0c9d7125ad9d50de3ff66.webp)

Esta funcionalidad fue financiada por ARPA Piemonte

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Herramientas de análisis
### Feature: \"Keep disjoint features separate\" option for dissolve algorithm
A \"Keep disjoint features separate\" option has been added for the dissolve algorithm which will cause features and parts that do not overlap or touch to be exported as separate features instead of parts of a single multipart feature. This makes it much simpler to perform simple aggregation based dissolves on a single class.

![image37](images/entries/350b223b3d7b647643338f57158c2b139df11f87.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Procesado
### Prestación: Herramienta de modelo de mensaje elevado
Se ha añadido un algoritmo de aumento de mensajes a las herramientas de modelos que permite a los usuarios incluir información adicional en los registros de los modelos. De este modo se evita el abuso de los algoritmos de aumento de errores/avisos y se proporciona un control más detallado de los niveles de registro de los modelos.

![image38](images/entries/e2433bb4fe23b076129ea4accd516e3b7939d64f.gif)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
### Prestación: Ejecutar pasos de procesamiento por lotes en tareas
Los pasos individuales del diálogo de procesamiento por lotes ahora se ejecutan como una tarea separada siempre que sea posible. Aunque los pasos individuales se siguen ejecutando secuencialmente en lugar de en paralelo, esto mantiene la capacidad de respuesta de la interfaz de usuario, y permite la cancelación sensible y la presentación de informes de progreso.

Esta prestación fue financada por NRCan Contrato#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Procesamiento en segundo plano de algoritmos modelo
Anteriormente, cualquier modelo gráfico diseñado en Procesos era forzado a ejecutarse en el hilo principal, y no soportaba la ejecución en segundo plano. QGIS ahora soporta la ejecución de algoritmos de modelos fuera del hilo principal para que puedan ejecutarse con seguridad en tareas en segundo plano.

Esta prestación fue financada por NRCan Contrato#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Permitir la configuración de Ejemplos en la ayuda del modelo gráfico
A new \'Examples\' section has been added to the graphical model help editor dialog, allowing users to enter their own custom examples to help explain usage of the model.

More instructive help is now shown for models in the qgis_process tool, including outputting any example help which has been set.

![image39](images/entries/64e788f716481fbb085a0ba70e8cc4f2333ad744.gif)

Esta prestación fue financada por NRCan Contrato#3000739399

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Herramientas de superposición con soporte para múltiples capas superpuestas
Adds new Intersect, Union and Difference tools which support multiple \"overlay\" inputs instead of a single overlay layer. The current workflow includes selecting the order of overlay layers used in the operation, which are used in an iterative process by using the output of an operation between two layers as an input for the same operation with the next layer.

Se trata de una abstracción útil que puede utilizarse en diversos escenarios, como los modelos de procesamiento en los que los procesos iterativos o los bucles pueden estar limitados.

![image40](images/entries/419403e295be2748e89100cb31117685b151e409.webp)

This feature was developed by [Alexander Bruy](https://github.com/alexbruy)
## Opciones de Aplicación y Proyecto
### Prestación: Marco de propiedades de elevación del proyecto
Elevation/terrain settings are now project-level settings, which are defined through the Project Properties, Terrain tab, in line with [QEP 246](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/246) and in order to support the new elevation profile tools.

Este marco proporciona opciones de configuración para:
- **Terreno llano** con altura del terreno configurable
- **DEM (Capa Ráster)** con ajustes para definir la capa ráster de origen, la escala vertical y el desplazamiento.
- **Malla** con ajustes para definir la capa de la malla de origen, la escala vertical y el desplazamiento.

![image41](images/entries/c58fa193b00b77b743b17b9ef50336f1b13d1b9f.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Almacenamiento opcional de la configuración de la interfaz de usuario en los proyectos
An opt-in setting for projects has been added for \"Remember attribute table windows and docks between sessions\". If checked for a project, then any opened attribute tables will be saved into the project and immediately restored when loading that project.

Esto se ha diseñado para mejorar los flujos de trabajo cuando un usuario ha construido un proyecto con un conjunto particular de configuraciones de tablas de atributos para sus requisitos, y volver a configurar estas tablas de atributos es una molestia.

![image42](images/entries/a9b8aad7c60417bb1d7a811da40af7a1b763efbe.gif)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Almacenamiento opcional del estado de edición de las capas en los proyectos
An opt-in setting has been added to project properties for \"Remember editable layer status between sessions\". If checked, then any layers which are editable will be remembered when saving that project and immediately made editable whenever the project is restored to make it simpler for users who are making complex, data-editing focused projects to store their configurations on a project by project basis.

![image43](images/entries/04bf91d7cd37549d0949e2d3c67be6e7a809a3a5.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Soporte de bases de datos estilo proyecto
Una nueva función permite a los usuarios establecer una lista de bases de datos de estilos QGIS para un proyecto. Esto permite que los proyectos se vinculen a varias bases de datos de estilos y, a continuación, muestren todos los símbolos y entidades de esas bases de datos en la interfaz de estilo de capas.

Las rutas de estilo pueden apuntar a bases de datos de estilos .db o a exportaciones .xml. Cuando se carga un proyecto, los selectores de estilo de símbolos y etiquetas mostrarán TODOS los símbolos de TODOS los estilos vinculados al proyecto. Además, cada proyecto dispone ahora de una base de datos de estilos específica del proyecto (que se almacena junto con el proyecto), para almacenar símbolos, formatos de texto, etc. específicos del proyecto.

**Esta funcionalidad requiere una versión de QGIS basada en Qt 5.13 o posterior, y está oculta en versiones anteriores (por ejemplo, en Ubuntu 20.04)**.

![image44](images/entries/6172a0a8196db373e0eac8edbcbf790ae9532ba8.webp)

Esta prestación ha sido financiada por el grupo de usuarios suizos de QGIS.

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Se ha añadido la opción de mostrar el recuento de objetos espaciales por defecto en las capas recién añadidas.
Si está activada, esta opción hará que el recuento de objetos espaciales se active para cualquier capa de mapa recién añadida/creada. Esta opción permanecerá desactivada por defecto.

![image45](images/entries/3706248ef1ca50af9877d04df93d6f3455bce9ca.webp)

Está funcionalidad fue financiada por SevenCs GmbH

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Feature: Add a \"Skip\" option for custom environmental variables
The QGIS settings allow a particular user profile to modify the system environment variables for enhanced flexibility, in Settings \--\> Options \--\> Environment.

This functionality included options for \"Overwrite\", \"If Undefined\", \"Unset\", \"Prepend\", and \"Append\", which allowed users to perform various functions from configuring credentials to extending their PATH variables.

A new \"Skip\" option is now provided which allows users to ignore values from an existing field, without losing the stored values or having to remove them from the settings to disable them.

![image46](images/entries/31251db3a673149dcd900737dd9aada0fafb93ff.gif)

This feature was developed by [Andrea Giudiceandrea](https://github.com/agiudiceandrea)
### Feature: Revamped projects\' default symbols, color ramp, and text format
Esta nueva versión de QGIS ha renovado la forma en que se manejan los símbolos de los proyectos por defecto, con el objetivo de mejorar su UI/UX así como su correcto comportamiento en entornos multiusuario. Los cambios incluyen:
- Projects\' default symbols and color ramps are now stored as symbology XML rather than references, improving portability and integration with external applications and services
- Se ha añadido un nuevo ajuste de formato de texto predeterminado a nivel de proyecto para permitir la configuración definida por el usuario de la fuente predeterminada del proyecto para las capas vectoriales recién añadidas.
- The user interface has been upgraded to make use of QGIS\' symbol and color ramp buttons

![image47](images/entries/5fca0da47e4af53c46a12dcd5b68a1982afff16b.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Gráficos de Perfil
### Prestación: Herramienta de trazado de perfiles de elevación
QGIS incluye ahora una herramienta nativa de trazado de perfiles de elevación.

La herramienta incluye las siguientes prestaciones:
- Support for vector, raster, mesh, and point cloud layers, based on the corresponding layer\'s elevation settings.
- Dibujar líneas de perfil de forma interactiva mediante una herramienta cartográfica, que admite ajuste, trazado, digitalización de arroyos y curvas.
- Selección de una línea existente para utilizarla como línea de perfil. Cuando esta herramienta está activa, los usuarios pueden hacer clic en cualquier objeto espacial lineal del mapa para generar una curva de perfil a lo largo de esa línea. Si en el punto sobre el que se ha hecho clic hay varias características, aparecerá un menú emergente que permitirá a los usuarios seleccionar una de las características disponibles.
- Los gráficos pueden exportarse a PDF (como objetos vectoriales de alta calidad) o a varios formatos de imagen.
- Los perfiles se representan utilizando símbolos de línea estándar de QGIS, por lo que incluyen soporte para diseño y configuración avanzados, incluyendo soporte para generadores de geometría y efectos de pintura.
- Medición de distancias en los gráficos
- Identificación de objetos espaciales en el gráfico mediante un solo clic o haciendo clic y arrastrando el rectángulo. Los resultados se muestran en la ventana de resultados de identificación estándar y admiten capas vectoriales, ráster, de malla y de nube de puntos.

La navegación interactiva por el lienzo del gráfico se realiza mediante los métodos abreviados estándar de QGIS, como:
- Botón central del ratón: Paneo
- Espacio: Paneo
- Ctrl + Espacio: Zoom (acercamiento)
- Ctrl + rueda Ratón: Acercamiento fino

Shortcuts are available for nudging the elevation profile curve left and right, which allows users to \"scrub\" the curve across the map frame and find the optimal profile line. The step distance is set to match the chart\'s tolerance distance, so that a single step will result in a different set of point and point cloud features shown in the chart.

Los atajos de teclado para dar un codazo son:
- Ctrl+Alt+,: Scrub izquierda
- Ctrl+Alt+.: Scrub derecha

For more information on this awesome feature and framework, be sure to watch the [QGIS Elevation Profiles Deep Dive](https://www.youtube.com/watch?v=AknJjNPystU) presentation on YouTube.

![image48](images/entries/6c530f4bfd565313f515ae9f6a79662d1682bfc7.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Simbología flexible de capas vectoriales en perfiles de elevación
Las capas vectoriales añadidas a las cartas de perfil respetarán por defecto su simbología de capa. Se ha añadido una casilla de verificación para desactivar esta opción en las propiedades de elevación de la capa.

Esto significa que los resultados vectoriales en los gráficos de perfil de elevación mostrarán por defecto las características utilizando su correspondiente representador 2D, por lo que los estilos personalizados como las clases categorizadas serán visibles en el gráfico de perfil por defecto.

There\'s also options to change the interpretation of the elevation profile for vector layers. By default, the elevation profile tool will use an \"individual features\" option, which samples discrete positions where the cross section profile line intersects the vector features. There\'s also a \"continuous surface\" option which will generate an interpretation of the surface by interpolating across the sample positions for enhanced visualization, such as the production of a continuous surface line from contour lines or surveyed elevation points.

Additional rendering capabilities are provided for the \"continuous surface\" interpretation option, such as a \"fill below\" symbol style. This can be easier to interpret in some cases, and helps match expected symbology conventions in certain disciplines.

![image49](images/entries/50ff18ed7962a0fbc09ca17f3b0688db6ed33bd3.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Simbología flexible para el trazado de perfiles de nubes de puntos
Las capas de nubes de puntos en las cartas de perfil incluyen las siguientes características de simbología:
- Visualización de puntos en un solo color o un ajuste para heredar la clasificación y la coloración de la simbología 2D (por ejemplo, colores RGB).
- Respetar el ajuste de tolerancia de distancia de la curva del perfil
- Opción para reducir la opacidad de los puntos que están más alejados de la curva del perfil.
- Refinamiento automático basado en el área visible y la escala del gráfico, con un error máximo de pantalla controlable por el usuario.
- Control de la apariencia de los puntos (color, tamaño y forma)

![image50](images/entries/c8cf49088468d798190f56a32c0e6c6d1cefe72f.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Extrusión de rasgos vectoriales para gráficos de perfiles
La herramienta de perfil de elevación proporciona soporte para la extrusión de objetos espaciales vectoriales y alturas de desplazamiento para la incorporación de vectores 2D en gráficos de perfil. Estas propiedades pueden definirse en los datos y también se utilizarán como ajustes predeterminados de desplazamiento/extrusión para cualquier nuevo símbolo de polígono 3D creado para esa capa.

![image51](images/entries/3bfe2bcf8051167fd7729ef3c5a2a4f5249f823b.webp)

This feature was funded by [Crowdfunding for raster and point clouds improvements](https://www.lutraconsulting.co.uk/crowdfunding/elevation-pointcloud-enhancements-qgis)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
## Navegador
### Prestación: Control del menú contextual para cambiar el nombre de los grupos de marcadores
Creating new spatial bookmarks from the browser will now default to the \"project bookmark\" category, and a new context menu option has been added for renaming of bookmark groups. The existing behavior of renaming bookmark groups using the F2 key remains unchanged.

![image52](images/entries/79d5021866775b2eb429eb60c96f697ac0c6af49.gif)

This feature was funded by [Camptocamp](https://www.camptocamp.com)

This feature was developed by [Ismail Sunni](https://github.com/ismailsunni)
## Proveedores de datos
### Prestación: Admite la lectura directa de paquetes de mosaicos vectoriales ESRI (.vtpk)
Los paquetes de mosaicos vectoriales ESRI (archivos VTPK) pueden abrirse ahora directamente como capas de mosaicos vectoriales mediante arrastrar y soltar, incluyendo soporte para la traducción de estilos.

This feature was funded by [North Road Consulting, thanks to SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road Consulting)](https://north-road.com)
### Prestación: Registro SQL en el panel Depuración/Desarrollo
El panel de depuración/desarrollo incluye ahora soporte para el registro de las consultas SQL realizadas por QGIS a los proveedores de datos backend.

Esto proporciona un método eficaz para depurar algoritmos y proveedores de datos, así como para capturar las sentencias SQL realizadas para ejecutar acciones específicas contra proveedores concretos.

Tenga en cuenta que esto está diseñado específicamente para ser utilizado como una herramienta de depuración y desarrollo y no está diseñado para ser un reemplazo para cualquier capacidad de registro en los sistemas de bases de datos backend.

This has been implemented in line with [QEP 242](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/242).

![image53](images/entries/62594ee3295e3276fe9510f42e2ba54d05153ebd.webp)

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Servidor de QGIS
### Prestación: Estrategia alternativa de comprobación periódica para detectar actualizaciones de proyectos
QGIS Server ahora proporciona una estrategia alternativa lastModified() para invalidar la caché interna del proyecto, abordando las preocupaciones sobre la capacidad del servidor QGIS para invalidar la caché cuando un archivo de proyecto se actualiza en sistemas de archivos atípicos, como NFS, o cuando el archivo de proyecto se almacena en un sistema de base de datos como PostgreSQL.

Ahora se proporciona una estrategia de comprobación periódica asíncrona que utiliza el último valor modificado de un proyecto para comprobar si se han producido cambios en la configuración del proyecto.

The `QGIS_SERVER_PROJECT_CACHE_STRATEGY` environment variable may be used to configure the server caching strategy using the following values:
- `periodic` for the alternative strategy
- `filesystem` to use the file system watcher strategy
- `off` to disable internal caching completely.

`QGIS_SERVER_PROJECT_CACHE_CHECK_INTERVAL` is used for controlling the periodic strategy interval.

The `QFileSystemWatcher` strategy remains the default configuration.

This feature was funded by [3Liz](https://3liz.com)

This feature was developed by [David Marteau](https://github.com/dmarteau)
### Prestación: Añadir más parámetros de etiqueta de resaltado del servidor
Se han añadido nuevos parámetros para controlar mejor la colocación de las etiquetas de resaltado en el servidor WMS, entre los que se incluyen:
- `HIGHLIGHT_LABELDISTANCE`: Distance between the feature and the label, defined in mm
- `HIGHLIGHT_LABELROTATION`: Label rotation, defined in degrees
- `HIGHLIGHT_LABELVALI`: Vertical alignment for placing the label directly on a point
- `HIGHLIGHT_LABELHALI`: Horizontal alignment for placing the label directly on a point

This feature was developed by [mhugent](https://github.com/mhugent)
### Prestación: Soporte de propiedades temporales para Servidor WMS
Las versiones anteriores de QGIS Server sólo ofrecían soporte para las dimensiones de tiempo y elevación para capas vectoriales y no proporcionaban integración con la API actualizada de propiedades temporales proporcionada por QGIS.

QGIS Server has now been extended to support the time dimension in the `GetCapabilities` response for WMS services, and accept a `TIME` query string parameter which provides capacity for temporal data filtering.

El análisis sintáctico de los valores de tiempo se realizará con la especificación de implementación proporcionada por OGC API - Features (OAPIF) y utilizará la siguiente estructura:

\| interval\| syntax \| \|\-\--\|\-\--\| \| interval-closed \| date-time \"/\" date-time \| \| interval-open-start \| \[\"..\"\] \"/\" date-time \| \| interval-open-end \| date-time \"/\" \[\"..\"\] \| \| interval \| interval-closed / interval-open-start / interval-open-end \| \| datetime \| date-time / interval \|

Tenga en cuenta que este filtrado sólo se aplica a valores individuales, y que actualmente no se admite una lista de instantes o rangos.

To prevent conflict with existing TIME dimension stipulations on legacy projects, if a `TIME` dimension was explicitly defined for a vector layer, the temporal properties for that layer will not be activated and the explicitly set `TIME` dimension will be considered instead.

Esta prestación fue financiada por Gis3W

This feature was developed by [Alessandro Pasotti](https://github.com/elpaso)
## Programabilidad
### Prestación: Añadir una función QgsScaleCalculator para calcular el ancho del lienzo a partir de una extensión, escala y ppp dados.
A new `calculateCanvasWidth( extent, scale )` was added to the `QgsScaleCalculator` class to derive canvas width in pixel unit when providing an extent, a scale, and a DPI.

This feature was developed by [Mathieu Pellerin](https://github.com/nirvn)
### Prestación: Borrar la acción de símbolo actual en el widget de botón de símbolo
Se ha añadido una acción Establecer en null / Borrar símbolo actual para borrar el símbolo actual adjunto a un widget de botón de símbolo.

![image54](images/entries/e7c6ed595485dd51c3bccb87f2a31f9691ad4aae.webp)

This feature was developed by [Mathieu Pellerin](https://www.opengis.ch/)
## Correcciones Notables
### Error corregido por Even Rouault
| Título del Error | URL Incidencias (si se ha informado, Github) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| WFS provider doesn\'t recognize CRS strings other than OGC URNs | [#46485](https://github.com/qgis/QGIS/issues/46485) | [PR #48550](https://github.com/qgis/QGIS/pull/48550) | N/D |
| QgsMapCanvas::showEvent access violation / QGIS crash | [#48438](https://github.com/qgis/QGIS/issues/48438) | [PR #48551](https://github.com/qgis/QGIS/pull/48551) | [PR #48558](https://github.com/qgis/QGIS/pull/48558) |
| \[GDAL provider\] Minimal support for GDT_Int64/GDT_UInt64 of GDAL 3.5.0 | (no reportado) | [PR #48553](https://github.com/qgis/QGIS/pull/48553) |  |
| el acceso a QgsRubberBand-methods se bloquea QGis | [#48471](https://github.com/qgis/QGIS/issues/48471) | [PR #48554](https://github.com/qgis/QGIS/pull/48554) | [PR #48561](https://github.com/qgis/QGIS/pull/48561) |
| annotationManager con acceso a canvas-items se bloquea QGis | [#48436](https://github.com/qgis/QGIS/issues/48436) | [PR #48554](https://github.com/qgis/QGIS/pull/48554) | [PR #48561](https://github.com/qgis/QGIS/pull/48561) |
| No se puede importar archivos excel con la nueva versión de QGIS | [#47838](https://github.com/qgis/QGIS/issues/47838) | N/A - error freexl. Parche enviado a upstream | N/D |
| Las capas añadidas por QGIS no son correctas si la fuente de datos es una colección. | [#47610](https://github.com/qgis/QGIS/issues/47610) | [PR #48556](https://github.com/qgis/QGIS/pull/48556) | [PR #48572](https://github.com/qgis/QGIS/pull/48572) |
| SQLite: No hay creación de índice espacial aunque QGIS informa engañosamente de éxito | [#44513](https://github.com/qgis/QGIS/issues/44513) | [PR #48557](https://github.com/qgis/QGIS/pull/48557) | [PR #48565](https://github.com/qgis/QGIS/pull/48565) |
| Guardar una capa de puntos editada de gran tamaño lleva demasiado tiempo | [#46355](https://github.com/qgis/QGIS/issues/46355) | [GDAL PR 5730](https://github.com/OSGeo/gdal/pull/5730) | [GDAL PR 5753](https://github.com/OSGeo/gdal/pull/5753) |
| Tabla de atributos no existente pero registrada en GPKG se añade como tabla vacía | [#30670](https://github.com/qgis/QGIS/issues/30670) | [GDAL PR 5752](https://github.com/OSGeo/gdal/pull/5752) | No apropiado |
| Los acentos se muestran incorrectamente al guardar metadatos en el geopackage | [#47435](https://github.com/qgis/QGIS/issues/47435) | [PR #48625](https://github.com/qgis/QGIS/pull/48625) | [PR #48631](https://github.com/qgis/QGIS/pull/48631) |
| Raster tiles are clipped based on the gpkg_contents bounding box of a GeoPackage | [#45530](https://github.com/qgis/QGIS/issues/45530) | No es un error |  |
| Pan-action freeze after use of middle mouse button and \'copy coordinate\' | [#48645](https://github.com/qgis/QGIS/issues/48645) | [PR #48666](https://github.com/qgis/QGIS/pull/48666) | [PR #48684](https://github.com/qgis/QGIS/pull/48684) |
| New GeoPackage layer cannot be loaded (QGIS thinks it\'s invalid but it isn\'t really) | [#48671](https://github.com/qgis/QGIS/issues/48671) | [PR #48692](https://github.com/qgis/QGIS/pull/48692) | [PR #48774](https://github.com/qgis/QGIS/pull/48774) |
| \[regression\] New filter for duplicated WFS layer is also applied on source layer | [#48465](https://github.com/qgis/QGIS/issues/48465) | [PR #48998](https://github.com/qgis/QGIS/pull/48998) | N/D |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Even Rouault](https://www.spatialys.com/)
### Errores corregido por Alessandro Pasotti
| Título del Error | URL Incidencias (si se ha informado, Github) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| \@project_keywords are no longer tested on Rule based filters | [#48480](https://github.com/qgis/QGIS/issues/48480) | No es un error |  |
| No más estilos después de duplicar capa y cambiar filtro en query builder en 3.22.6 | [#48467](https://github.com/qgis/QGIS/issues/48467) | A mi me funciona en 3.24.2 y master |  |
| MSSQL Add Connection Dialog nunca activa el botón OK | [#48462](https://github.com/qgis/QGIS/issues/48462) | A mí me funciona en master |  |
| Highlight of identified feature not displaying correctly on \"geometry generator\" marker from different CRS | [#48439](https://github.com/qgis/QGIS/issues/48439) | [PR #48579](https://github.com/qgis/QGIS/pull/48579) | PORHACER. |
| No se pueden pegar rasgos copiados como capa de rascado temporal | [#48401](https://github.com/qgis/QGIS/issues/48401) | [PR #48611](https://github.com/qgis/QGIS/pull/48611) | PORHACER. |
| QGIS se bloquea al abrir un formulario con contenido de relación | [#48443](https://github.com/qgis/QGIS/issues/48443) | [PR #48616](https://github.com/qgis/QGIS/pull/48616) | PORHACER. |
| Widget de referencia de relación: la expresión de filtro no funciona con variables | [#48190](https://github.com/qgis/QGIS/issues/48190) | [PR #48619](https://github.com/qgis/QGIS/pull/48619) | PORHACER. |
| Orden aleatorio de atributos en la consulta de objeto espacial de oracle | [#35309](https://github.com/qgis/QGIS/issues/35309) | [PR #48668](https://github.com/qgis/QGIS/pull/48668) | no |
| La fuente de datos CSV no se convierte correctamente de 3.16 a 3.22 - los proyectos ya no se pueden utilizar. | [#48587](https://github.com/qgis/QGIS/issues/48587) | Me funciona en 3.24 y master |  |
| Fallo en la prueba de documentación | [QGIS developer mail list](https://lists.osgeo.org/pipermail/qgis-developer/2022-May/064720.html) | [QGIS Documentation PR 7581](https://github.com/qgis/QGIS-Documentation/pull/7581) | no |
| \"Add to group\" option in sub layer window always add at top of layer tree | [#48694](https://github.com/qgis/QGIS/issues/48694) | [PR #48696](https://github.com/qgis/QGIS/pull/48696) | no |
| El nombre/id de los objetos de mapa en GetProjectSettings sigue un orden inverso al utilizado para añadir los objetos de mapa en un diseño | [#46143](https://github.com/qgis/QGIS/issues/46143) | [PR #48728](https://github.com/qgis/QGIS/pull/48728) | no |
| Las inserciones abortadas en tablas sin geometría de Postgis se guardan de todos modos | [#48171](https://github.com/qgis/QGIS/issues/48171) | [PR #48741](https://github.com/qgis/QGIS/pull/48741) | no |
| Inconsistent coordinate rounding in Raster \"Layer Properties\" | [#48767](https://github.com/qgis/QGIS/issues/48767) | [PR #48790](https://github.com/qgis/QGIS/pull/48790) | PORHACER. |
| Arrastrar y Soltar Tabla-Postgis en el Navegador QGIS altera el nombre de la Geometría-Columna | [#48748](https://github.com/qgis/QGIS/issues/48748) | [PR #48796](https://github.com/qgis/QGIS/pull/48796) | no |
| El filtro de capas no funciona en valores de cadenas multilínea con saltos de línea | [#47530](https://github.com/qgis/QGIS/issues/47530) | [PR #48818](https://github.com/qgis/QGIS/pull/48818) | no hay necesidad |
| QGIS se bloquea al buscar en el constructor de expresiones | [#48189](https://github.com/qgis/QGIS/issues/48189) | [PR #48856](https://github.com/qgis/QGIS/pull/48856) | [PR #48864](https://github.com/qgis/QGIS/pull/48864) |
| Servidor GetPrint con varios mapas siguientes temas de mapas aplicar el prefijo LAYERS (map0:LAYERS) a todos los mapas | [PR #48923](https://github.com/qgis/QGIS/pull/48923) | [PR #48923](https://github.com/qgis/QGIS/pull/48923) | PORHACER. |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Corrección de errores por Alex Bruy
| Título del Error | URL Incidencias (si se ha informado, Github) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingParameterMultipleLayers añade un elemento de lista extra al reordenar las entradas | [#45634](https://github.com/qgis/QGIS/issues/45634) | Me funciona en 3.24 y master |  |
| GDAL Vector to Raster (gdal_rasterize) fail to produce ESRI ASCII as output | [#39140](https://github.com/qgis/QGIS/issues/39140) | No es un error |  |
| Procesamiento: Drape / qgis:setzfromraster comportamiento NODATA inconsistente | [#43650](https://github.com/qgis/QGIS/issues/43650) | A mí me funciona en master |  |
| El nodo de salida del algoritmo se coloca en la mitad del lienzo del modelo. | [#48132](https://github.com/qgis/QGIS/issues/48132) | [PR #48600](https://github.com/qgis/QGIS/pull/48600) | [PR #48661](https://github.com/qgis/QGIS/pull/48661) |
| Inconsequence in CRS-names/id\'s in Copy Coordinate in MapCanvas | [#37226](https://github.com/qgis/QGIS/issues/37226) | [PR #48599](https://github.com/qgis/QGIS/pull/48599) |  |
| QGIS Formulario de rellenado por lotes están produciendo espacios entre filas | [#43869](https://github.com/qgis/QGIS/issues/43869) | [PR #48601](https://github.com/qgis/QGIS/pull/48601) | [PR #48636](https://github.com/qgis/QGIS/pull/48636) |
| El cuadro de diálogo de ajustes de procesamiento se borra después de realizar una búsqueda en el cuadro de diálogo Ajustes. | [#34543](https://github.com/qgis/QGIS/issues/34543) | [PR #48602](https://github.com/qgis/QGIS/pull/48602) | [PR #48633](https://github.com/qgis/QGIS/pull/48633) |
| QgsProcessingAlgorithm con FlagHideFromModeler bandera sigue siendo visible en el Diseñador de Modelos | [#48586](https://github.com/qgis/QGIS/issues/48586) | [PR #48603](https://github.com/qgis/QGIS/pull/48603) | [PR #48632](https://github.com/qgis/QGIS/pull/48632) |
| La salida de Nominatim Geocoder por lotes guardada directamente en un archivo no tiene SRC | [#48385](https://github.com/qgis/QGIS/issues/48385) | [PR #48618](https://github.com/qgis/QGIS/pull/48618) | [PR #48708](https://github.com/qgis/QGIS/pull/48708) |
| La iteración sobre objetos espaciales en el algoritmo de procesamiento no crea la carpeta de destino correcta | [#48383](https://github.com/qgis/QGIS/issues/48383) | [PR #48646](https://github.com/qgis/QGIS/pull/48646) | [PR #48657](https://github.com/qgis/QGIS/pull/48657) |
| Al arrastrar varias capas en el widget de selección de capas del algoritmo de procesamiento se bloquea QGIS | [#47728](https://github.com/qgis/QGIS/issues/47728) | [PR #48649](https://github.com/qgis/QGIS/pull/48649) | [PR #48656](https://github.com/qgis/QGIS/pull/48656) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Alex Bruy](https://www.qcooperative.net/)
### Correcciones de error por Sandro Santilli
| Título del Error | URL Incidencias (si se ha informado, Github) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| Añadir un simple script bash para ejecutar pruebas como lo hace CI | [QGIS QEP #244](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/244) | [PR #48617](https://github.com/qgis/QGIS/pull/48617) | No apropiado |
| test_provider_eptprovider occasionally aborts | [#48778](https://github.com/qgis/QGIS/issues/48778) | [PR #48793](https://github.com/qgis/QGIS/pull/48793) | no es necesario |
| Problema con la clase QgsVectorLayerUndoCommand (QGIS se bloquea) | [#23243](https://github.com/qgis/QGIS/issues/23243) | [PR #48700](https://github.com/qgis/QGIS/pull/48700) | [PR #48934](https://github.com/qgis/QGIS/pull/48934) |
| Comprobar que los archivos de origen no se sobrescriben | [#25830](https://github.com/qgis/QGIS/issues/25830) | [PR #48654](https://github.com/qgis/QGIS/pull/48654) | No apropiado |
| TestQgsGdalProvider falla en ausencia de soporte netcdf | [#48906](https://github.com/qgis/QGIS/issues/48906) | [PR #48907](https://github.com/qgis/QGIS/pull/48907) | [PR #48926](https://github.com/qgis/QGIS/pull/48926) |
| test_core_gdalprovider modifies tests/testdata/zip/landsat_b1.zip source file | [#48846](https://github.com/qgis/QGIS/issues/48846) | [PR #48917](https://github.com/qgis/QGIS/pull/48917) | [PR #48926](https://github.com/qgis/QGIS/pull/48926) |
| Drop gpkg_metadata_reference_column_name_update trigger generated by GDAL \< 2.4.0 | N/D | [PR #48953](https://github.com/qgis/QGIS/pull/48953) | [PR #48957](https://github.com/qgis/QGIS/pull/48957) |
| Corrección del análisis de pruebas que procesa la modificación de archivos fuente | [#48937](https://github.com/qgis/QGIS/issues/48937) | [PR #48959](https://github.com/qgis/QGIS/pull/48959) | [PR #48961](https://github.com/qgis/QGIS/pull/48961) |
| ctest: No module named \'qgis.server\' | [#48958](https://github.com/qgis/QGIS/issues/48958) | [PR #48993](https://github.com/qgis/QGIS/pull/48993) | [PR #48999](https://github.com/qgis/QGIS/pull/48999) |
| PyQgsLocalServer test fails: AttributeError: module \'platform\' has no attribute \'dist\' | [#48962](https://github.com/qgis/QGIS/issues/48962) | [PR #48976](https://github.com/qgis/QGIS/pull/48976) | [PR #49028](https://github.com/qgis/QGIS/pull/49028) |
| Corrección de activadores GDAL antiguos en archivos de paquetes geográficos | N/D | [PR #49037](https://github.com/qgis/QGIS/pull/49037) | [PR #49039](https://github.com/qgis/QGIS/pull/49039) |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Sandro Santilli (strk)](https://strk.kbt.io/)
### Error fijado por Nyall Dawson
| Título del Error | URL Incidencias (si se ha informado, Github) | URL Commit (Github) | 3.22 backport commit (GitHub) |
| --- | --- | --- | --- |
| layer_property(\..., \'path\') should work for all layer types | [#49011](https://github.com/qgis/QGIS/issues/49011) | [PR #49042](https://github.com/qgis/QGIS/pull/49042) | [PR #49046](https://github.com/qgis/QGIS/pull/49046) |
| Mejora del diálogo de creación de capas virtuales | no reportado | [PR #49015](https://github.com/qgis/QGIS/pull/49015) | No apropiado |
| \[db manager\] Don\'t load preview layers into project | [#47159](https://github.com/qgis/QGIS/issues/47159) | [PR #49016](https://github.com/qgis/QGIS/pull/49016) | [PR #49019](https://github.com/qgis/QGIS/pull/49019) |
| Don\'t hang when an error occurs while trying to build a virtual layer | [#48908](https://github.com/qgis/QGIS/issues/48908) | [Commit 988edc8700](https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5) | Demasiado intrusivo |
| Don\'t offer non-vector layer providers as options for virtual layer | [#48908](https://github.com/qgis/QGIS/issues/48908) | [Commit 988edc8700](https://github.com/qgis/QGIS/commit/988edc8700bd8d6363ebc4e4379963924bfa02b5) | Demasiado intrusivo |
| Corregir la selección/deselección de todo en el diálogo de edición fuera de línea cuando algunas capas están en grupos no seleccionados. | [#48971](https://github.com/qgis/QGIS/issues/48971) | [PR #48985](https://github.com/qgis/QGIS/pull/48985) | [PR #49002](https://github.com/qgis/QGIS/pull/49002) |
| Corregir flotar objetos espaciales en la tabla de atributos en temas oscuros los selecciona | [#48914](https://github.com/qgis/QGIS/issues/48914) | [PR #48986](https://github.com/qgis/QGIS/pull/48986) | [PR #49001](https://github.com/qgis/QGIS/pull/49001) |
| Corregir el contexto de expresión del atlas no está disponible cuando la representación de los marcos de visión general del elemento | [#48963](https://github.com/qgis/QGIS/issues/48963) | [PR #48967](https://github.com/qgis/QGIS/pull/48967) | [PR #48984](https://github.com/qgis/QGIS/pull/48984) |
| Fix regression where layout attribute table conditional styles don\'t apply | [#48965](https://github.com/qgis/QGIS/issues/48965) | [PR #48968](https://github.com/qgis/QGIS/pull/48968) | [PR #48973](https://github.com/qgis/QGIS/pull/48973) |
| Review and finish open PR [PR #48314](https://github.com/qgis/QGIS/pull/48314) |  |  |  |
| Corregir atributos de expresión basados en la geometría para diagramas | [#47800](https://github.com/qgis/QGIS/issues/47800) | [PR #48893](https://github.com/qgis/QGIS/pull/48893) | [PR #48911](https://github.com/qgis/QGIS/pull/48911) |
| Corregir la pérdida de precisión al introducir manualmente una extensión en los widgets de procesamiento de extensiones. | [#48887](https://github.com/qgis/QGIS/issues/48887) | [PR #48895](https://github.com/qgis/QGIS/pull/48895) | [PR #48910](https://github.com/qgis/QGIS/pull/48910) |
| Corregir algunos iconos de tamaño reducido en pantallas hidpi | no reportado | [PR #48875](https://github.com/qgis/QGIS/pull/48875) | No apropiado |
| Poner la capa de cobertura del atlas a disposición del generador de expresiones para un formato de cuadrícula personalizado. | [#48833](https://github.com/qgis/QGIS/issues/48833) | [PR #48839](https://github.com/qgis/QGIS/pull/48839) | [PR #48894](https://github.com/qgis/QGIS/pull/48894) |
| Fix regression where user defined default style doesn\'t apply to MapInfo TAB files | [#48667](https://github.com/qgis/QGIS/issues/48667) | [PR #48840](https://github.com/qgis/QGIS/pull/48840) | [PR #48892](https://github.com/qgis/QGIS/pull/48892) |
| Corregir la recogida de valores de QgsFeatureListComboBox | [#48459](https://github.com/qgis/QGIS/issues/48459) | [PR #48841](https://github.com/qgis/QGIS/pull/48841) | [PR #48881](https://github.com/qgis/QGIS/pull/48881) |
| Corregir los valores claros para el desplazamiento a lo largo de las cajas de giro de línea | no reportado | [PR #48872](https://github.com/qgis/QGIS/pull/48872) | [PR #48878](https://github.com/qgis/QGIS/pull/48878) |
| Fix ambiguous \"show all labels\" setting and address regressions in label when this setting is misinterpreted | [#41043](https://github.com/qgis/QGIS/issues/41043) | [PR #48771](https://github.com/qgis/QGIS/pull/48771) | Demasiado intrusivo |
| La capa de anotación principal debe seguir las src del proyecto a menos que tenga elementos añadidos | [#42378](https://github.com/qgis/QGIS/issues/42378) | [PR #48815](https://github.com/qgis/QGIS/pull/48815) | Demasiado intrusivo |
| Corregir algunas advertencias engañosas sobre las transformaciones para src no terrestres. | [#42378](https://github.com/qgis/QGIS/issues/42378) | [PR #48815](https://github.com/qgis/QGIS/pull/48815) | Demasiado intrusivo |
| No mostrar nunca el cuadro de diálogo de selección de transformación para la primera capa añadida a un proyecto | no reportado | [PR #48811](https://github.com/qgis/QGIS/pull/48811) | [PR #48814](https://github.com/qgis/QGIS/pull/48814) |
| Garantizar que las expresiones de nivel de capa funcionen correctamente en los diagramas | [#47800](https://github.com/qgis/QGIS/issues/47800)0 | [PR #48803](https://github.com/qgis/QGIS/pull/48803) | [PR #48813](https://github.com/qgis/QGIS/pull/48813) |
| Corrección del tratamiento de fuentes WMTS con dimensiones en el navegador | [#36264](https://github.com/qgis/QGIS/issues/36264) | [PR #48800](https://github.com/qgis/QGIS/pull/48800) | [PR #48812](https://github.com/qgis/QGIS/pull/48812) |
| Asegúrese de que se cambian todas las unidades al ajustar la unidad de salida de un símbolo | [#45961](https://github.com/qgis/QGIS/issues/45961) | [PR #48786](https://github.com/qgis/QGIS/pull/48786) |  |
| Corregir la pérdida de estilo de capa de malla al fijar una ruta rota a una capa de malla. | no reportado | [PR #48765](https://github.com/qgis/QGIS/pull/48765) | [PR #48768](https://github.com/qgis/QGIS/pull/48768) |
| Mostrar lo más destacado de las etiquetas ancladas también para las etiquetas curvas ancladas | [#48753](https://github.com/qgis/QGIS/issues/48753) | [PR #48764](https://github.com/qgis/QGIS/pull/48764) | N/D |
| Don\'t hide parts of the mesh renderer widget if the layer is invalid | no reportado | [PR #48757](https://github.com/qgis/QGIS/pull/48757) |  |
| Añadir widget de opacidad de capa en el widget de propiedades del renderizador de capas de malla. | no reportado | [PR #48756](https://github.com/qgis/QGIS/pull/48756) |  |
| Review and finish open PR [PR #44941](https://github.com/qgis/QGIS/pull/44941) |  |  |  |
| Corregir una caída del sistema cuando QgsProject::instance() se accede cuando no existe QgsApplication | no reportado | [PR #48721](https://github.com/qgis/QGIS/pull/48721) | N/D |
| Mejor enfoque para filtrar listas por etiquetas que funciona en diferentes estilos. | [#48659](https://github.com/qgis/QGIS/issues/48659) | [PR #48689](https://github.com/qgis/QGIS/pull/48689) | N/D |
| Corregir la lentitud de la vista de diseño cuando se activa el atlas con el filtro de leyenda activado. | [#47033](https://github.com/qgis/QGIS/issues/47033) | [PR #48686](https://github.com/qgis/QGIS/pull/48686) | [PR #48704](https://github.com/qgis/QGIS/pull/48704) |
| Corregir la caída del sistema tras ejecutar el modelo desde el cuadro de diálogo de historial | [#40258](https://github.com/qgis/QGIS/issues/40258) | [PR #48687](https://github.com/qgis/QGIS/pull/48687) | [PR #48709](https://github.com/qgis/QGIS/pull/48709) |
| Corregir la caída del sistema al salir de QGIS | probablemente resuelva una serie de tickets abiertos, pero necesita la confirmación del usuario final | [Commit 5b052730b5](https://github.com/qgis/QGIS/commit/5b052730b5c10f12570dd5e68fca1962f113b3f3) | Demasiado intrusivo |
| Añadir soporte para tipos de campo de mapa a proveedor de memoria, evitar la pérdida de datos en los modelos / procesamiento. | no reportado | [PR #48638](https://github.com/qgis/QGIS/pull/48638) | Demasiado intrusivo |
| Corregir fallo al convertir una geometría curva a curvas | [#48045](https://github.com/qgis/QGIS/issues/48045) | [#48045](https://github.com/qgis/QGIS/issues/48045) | [PR #49024](https://github.com/qgis/QGIS/pull/49024) |
| Corregir muchas fugas de memoria | no reportado | [PR #48590](https://github.com/qgis/QGIS/pull/48590) | N/D |
| Corregir modificador ctrl desplazamiento en los botones de símbolo | no reportado | [PR #48581](https://github.com/qgis/QGIS/pull/48581) | N/D |

These bugfixes were funded by [QGIS.ORG (through donations and sustaining memberships)](https://qgis.org/)

Bugs fixed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
