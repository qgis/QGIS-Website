---
HasBanner: false
draft: false
releaseDate: '2020-10-23'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.16
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.16{#changelog316 }
![image1](images/projects/dbc0cef663f2f652e0961ac2ed168eb45ed2e182.png)

Fecha de lanzamiento: 2020-10-23

¡Otro gran día para el proyecto QGIS! La nueva versión de soporte a largo plazo trae una amplia gama de características tanto para QGIS Desktop como para QGIS Server. Esta versión trae una gran cantidad de nuevas opciones para mapeo 3D, generación de mallas a partir de otros tipos de datos, herramientas adicionales de análisis espacial, simbología y mejoras en la interfaz de usuario, ¡por nombrar solo algunas! Se ha incorporado una gran cantidad de herramientas en el marco de procesamiento en constante expansión, y el navegador QGIS ahora admite la funcionalidad avanzada de interacción con la base de datos que antes estaba reservada para el complemento DB Manager. Estas son algunas de las mejoras que se han introducido a partir de esta versión, y los usuarios del LTS anterior encontrarán una gran cantidad de nuevas funciones disponibles desde 3.10. Nos complace detallar algunos de los aspectos más destacados de esta nueva versión a continuación.

**Gracias**

We would like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## General
### Añadido "easter egg" de los grupos de usuarios
Type the words \"user groups\" into the current coordinates window and watch the magic happen.

![image2](images/entries/079434bceb5004b0ee2c4ad5d62edd1290c28575.webp)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
## Temporal
### Hailidad para exportar fotogramas de animación temporal
Permite exportar fotogramas de animación temporal a imágenes sucesivas, para luego unirlas en una aplicación externa. Los usuarios tienen un control preciso sobre el tamaño de la imagen y la extensión del mapa.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Herramientas de mapa
### Localizador Ir-A
Hemos añadido un nuevo filtro de localizador Ir-A

El indicador Ir-A tiene las siguientes cadenas:
- Un par de coordenadas x e y (separadas por una coma o un espacio).
- Una URL con formato OSM, Leaflet u OpenLayers.
- Una URL de Google Maps

La lógica de la cadena XY es como sigue:
- If the canvas CRS isn\'t WGS84:
  - Si la coordenada encaja dentro de los límites WGS84, agrega un resultado WGS84 (esto se pondera para tener una prioridad más alta que el resultado SRC del lienzo de abajo).
  - Si la coordenada encaja dentro de los límites del SRC del lienzo, agrega un resultado del SRC del lienzo.
- Si el SRC del lienzo es WGS84:
  - Si la coordenada encaja dentro de los límites WGS84, añade un resultado WGS84.

![image3](images/entries/acb9e856ac744d0e40d8de33c025deb075385856.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Interfaz de usuario
### Añadir menú contextual al lienzo del mapa
The map canvas now has a right-click context menu. By default, it creates the \"Copy Coordinate\" menu that was introduced with QGIS 3.14, however, it is expected that this functionality will be extended to allow many more functionalities to be accessed with spatial context in the future.

![image4](images/entries/f6e3ce9dca04583c9fa791204fe7e1a3c49c61d0.webp)

This feature was developed by [jakimowb](https://api.github.com/users/jakimowb)
## Simbología
### Mejoras de estilizado de tesela vectorial
Se introdujeron múltiples mejoras para la edición de estilos de teselas vectoriales complejas:
- Muestra consejos en listas, para que las reglas y los nombres de filtro completos se puedan ver sin cambiar el tamaño de las columnas
- Muestra el nivel de zoom del lienzo actual en los widgets
- Permitir a los usuarios filtrar la lista de estilos para mostrar solo aquellos que están visibles actualmente
- Establece el nivel de zoom del lienzo correcto al editar símbolos, para que las vistas previas de las expresiones funcionen bien

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Permite a los usuarios especificar opcionálmente la  URL para el estilo predeterminado en las conexiones de tesela vectorial
When setting up a vector tile source connection, there\'s a new option to enter a URL to a MapBox GL JSON style configuration. If one has been entered, then that style will be applied whenever the layers from the connection are added to QGIS.

Esto también funciona con las conexiones de Sercivio de Tesela Vectorial de ArcGIS, que tendrán la configuración de estilo predeterminada especificada en la configuración del servidor.

![image5](images/entries/f93d5dca726eb94be82cc47479424b8fe42f5920.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Permite desplazamiento definido por datos para capas de símbolo de relleno
Cualquier capa de símbolo de relleno que admita polígonos de compensación, incluidos rellenos simples, rellenos de imágenes ráster, rellenos de forma y degradado, ahora permite desplazamientos definidos por datos

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Importar estilos de GL JSON MapBox para capas de tesela vectorial
Los usuarios ahora pueden cargar archivos de configuración de estilo MapBox GL JSON al importar archivos de estilo en capas de tesela vectorial

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Exponer la opción para compensar los patrones de trazos de líneas simples por una cantidad preestablecida
Allows for tweaking the positioning of dashes/spaces in the line, so that the dashes/spaces can be placed at nicer positions to account for corners in the line (also can be used potentially to \"align\" adjacent dash pattern borders).

El desplazamiento puede ser establecido en varias unidades, incluyendo unidades de mapa, y también pueden ser definido por datos.

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agrega opciones para ajustar dinámicamente el patrón de trazos en capas de símbolo de línea simple
Se han agregado opciones para permitir el ajuste de los patrones de guiones para permitir un mayor control para mejorar la calidad renderizada de los símbolos de línea. Estas opciones incluyen:
- Alinear el patrón de trazos con la longitud de la línea: si está marcada, las longitudes del patrón de trazos se ajustarán sutilmente para garantizar que cuando se represente una línea terminará con un elemento de trazo completo, en lugar de un elemento de espacio o un elemento de trazo parcial.
- Tweak dash pattern at sharp corners: If checked, this option dynamically adjusts the dash pattern placement so that sharp corners are represented by a full dash element coming into and out of the sharp corner. It\'s designed to better represent the underlying geometry while rendering dashed lines, especially for jagged lines.

The following images illustrate the \"Align dash pattern to line length\" change in action, with yellow lines indicating the true start and end position of the line features being symbolised.

Antes:

![image6](images/entries/87635346-39f11c00-c782-11ea-88bc-369866d7f57a.webp)

Después:

![image7](images/entries/87635368-44131a80-c782-11ea-95d9-07fb7d00ffcf.webp)

![image8](images/entries/e1a4d82c248cdd0f04f236443897178c12574885.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Administrar símbolos 3D mediante el administrador de estilo
Se ha agregado soporte para administrar símbolos 3D a través del administrador de estilo QGIS, incluido el soporte para importar y exportar bibliotecas de símbolos 3D, y completa el trabajo reciente de abstraer completamente los símbolos 3D y sus controladores de widgets.

Desafortunadamente, no hay miniaturas generadas para los símbolos 3D en la biblioteca y, por el momento, se utiliza un icono genérico para todos los símbolos 3D. La generación de miniaturas no es un asunto trivial, por lo que se ha pospuesto por el momento.

This feature addresses the issue raised in [31479](https://github.com/qgis/QGIS/issues/31479).

![image9](images/entries/7e4ee802abba7dfd7ec61cdd8b3db333b7a30fae.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Etiquetando
### Agrega la opción de permitir a los usuarios controlar la ubicación de las etiquetas a lo largo de las entidades de línea
A new \"Label Anchoring\" section in the line placement settings for labels allows users to specify whether labels should be placed at the center, start or end of lines. In addition, it allows offsets of these positions (based on the percentage of the feature length), which may be defined statically or by using a data-defined definition.

![image10](images/entries/f5cc643fc4eafe75053c134b245e91d2e72e33d0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Controlar anchura de punto para etiquetas de línea
Se presenta una nueva opción que permite a los usuarios controlar si el punto de anclaje para el etiquetado de entidades de línea es una sugerencia o un requisito estricto. Las modificaciones de comportamiento resultante incluyen las siguientes:
- Estricto: las etiquetas se colocan exactamente en el anclaje de la etiqueta únicamente y no se permiten otras ubicaciones alternativas.
- Sugerido: el ancla de la etiqueta se trata como una sugerencia para la ubicación preferida de la etiqueta, pero se permiten otras ubicaciones cercanas al punto de anclaje.

![image11](images/entries/a6c67225ee3b55a021a395ffbf58bd05352ef6fb.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Diagramas
### Representación del eje para diagrama de barras apiladas
Esto agrega soporte para representar el eje en diagramas de barras apiladas si se ha establecido un eje. La implementación se basa en la representación de ejes para el diagrama de histogramas.

Los valores negativos no se manejan correctamente mediante diagramas de barras apiladas con o sin el eje mostrado.

Addresses [Issue 34915](https://github.com/qgis/QGIS/issues/34915)

![image12](images/entries/09739c5bed021a99baec41c98b87f5335a4bf8ec.webp)

This feature was developed by [Dan Minor](https://api.github.com/users/dminor)
## Malla
### Conjuntos de datos de malla en memoria con persistencia
Esta funcionalidad introduce la capacidad de crear grupos de conjuntos de datos en memoria para capas de malla. Estos grupos de conjuntos de datos son temporales y no se guardan una vez que se cierra el proyecto.

Se ha agregado una nueva opción a la calculadora de malla que permite la creación de grupos de conjuntos de datos en memoria.

Esta funcionalidad también presenta la capacidad de eliminar o guardar estos grupos de conjuntos de datos de memoria en un archivo con el controlador especificado.

![image13](images/entries/85622744-4d9edc00-b635-11ea-91db-a02fa28e6bea.gif)

![image14](images/entries/b27519025102be3b07fc8241f0ff8f8f2f9b31c6.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Identificación múltiple para capa de malla
La herramienta de identificación se ha adaptado para el caso de ser usada en capas de malla y ahora muestra el valor del conjunto de datos correspondiente a la hora actual del controlador temporal para todos los grupos de conjuntos de datos. Primero se muestran los grupos de conjuntos de datos activos (escalares y eventualmente vectoriales), luego los otros grupos de conjuntos de datos. También se muestra otra información, que incluye:
- Fuente donde se almacena el conjunto de datos
- Intervalo de tiempo del conjunto de datos que se muestra (puede ser diferente al tiempo del controlador temporal). No muestra nada si el grupo de conjuntos de datos no es temporal
- Centroide de la cara correspondiente
- Coordenada del vértice pinzado (si hay alguno pinzado)
- Centro de la arista pinzada (si hay alguna pinzada)

Cuando el mapa del lienzo no tiene la navegación temporal habilitada, los resultados de identificación contienen solo información sobre los grupos de conjuntos de datos activos que tienen conjuntos de datos estáticos definidos en el diálogo de propiedades de la malla.

![image15](images/entries/c4974747f5bc0dcba02f30a97e68bb5edacc5f48.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Grupos del conjunto de datos virtula para capa de malla
The ability to use \"virtual\" data set groups has been introduced for mesh layers. This replaces the \"memory\" dataset group used in [37389](https://github.com/qgis/QGIS/pull/37389).

With the mesh calculator, users may choose to create those \"virtual\" dataset groups that will be added to the layer. Values are not stored in memory but each dataset is rather calculated when needed with the formula entered in the mesh calculator.

Esos grupos de conjuntos de datos virtuales se guardan dentro del proyecto y se eliminan o guardan en un archivo para su persistencia.

Los grupos de conjuntos de datos persistentes y virtuales se distinguen en la pestaña de origen de las propiedades de la capa de malla por cambios en el color del fondo de cada elemento, indicados como sigue:

Persistente: amarillo

Virtual: púrpura

![image16](images/entries/86540129-a8a3bf00-bed0-11ea-94b8-bf29b5818cb8.gif)

![image17](images/entries/803983acbaec38e8df0fb4fd12d28beef7399520.webp)

This feature was funded by [Artelia Group](https://www.arteliagroup.com/en)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Añadir exportar al método QgsMesh
Se ha agregado un método para exportar una triangulación a una instancia de QgsMesh, con la posibilidad de construir una capa de malla con triangulación a partir de puntos y líneas existentes. Este es el primer paso para posibilitar obtener un QgsMesh de otras capas de mapa.

Las clases Triangulation y DualEdgeTriangulation también fueron renombradas y refactorizadas para hacerlas más consistentes con el código QGIS.
- Agregue un método para exportar la triangulación a una instancia de QgsMesh.

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
### Creación de una malla TIN
Las capas de malla TIN se pueden crear a partir de datos de capas vectoriales (vértices y/o líneas de ruptura). La malla resultante se construye con una triangulación de Delaunay restringida. Esta capa de malla se puede crear usando la API de Python o mediante un algoritmo en la caja de herramientas de procesamiento.

![image18](images/entries/fc8a9633b87b29bba052dacd166c0735b4449c90.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Representación
### Filtro de corrección gamma para capas ráster
Agregar un conducto de filtro de corrección gamma para las capas ráster, además de los filtros de brillo, contraste, tono y saturación existentes. Los usuarios pueden ajustar el valor de gamma desde el cuadro de diálogo de propiedades de la capa, utilizando el panel de estilo y / o nuevos botones en la barra de herramientas Ráster. El valor de gamma predeterminado es 1.0 y se puede ajustar dentro del rango de 0.1 a 10.

Addresses [Issue 13512](https://github.com/qgis/QGIS/issues/34915)

Also adds a rendering test for brightness and contrast filter which has no test at all and fixes some deprecation warnings in the Python test for `QgsRasterLayer`.

![image19](images/entries/bf6076062db63bc4c789bc18d3b029c14b2ddc8e.gif)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## Objetos 3D
### Permitir que los archivos de textura de material 3D se incrusten en el estilo/proyecto
Se realizaron algunas limpiezas menores de API y código, así como también se introdujo el uso de QgsImageCache para archivos de textura 3D con el fin de permitir que se incrusten en proyectos.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Renderizado de sombras
Las sombras pueden ahora ser renderizadas en vistas 3D.

![image20](images/entries/ef724bf261c7740d3cc92238d71d5ecb32a190c3.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Exportar escenas 3D
Las escenas 3D ahora se pueden exportar para su uso en otro software 3D, como Blender. Esta función de exportación admite múltiples funciones adicionales, incluida la simplificación del modelo de salida al especificar la resolución de salida, el suavizado de modelo opcional y la exportación de capas vectoriales 3D.

![image21](images/entries/91c112ba42358124faec9c3427542524d6b593f9.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Soporte de iluminación direccional para QGIS 3D
Añadidas luces direccionales a QGIS 3D
- Ahora el usaurio puede añadir luces direccionales a las vistas 3D.
- Añadí una pestaña de widget bajo la sección de luces del diálogo de configuración 3D.
- El usuario puede especificar la dirección de la luz, su color e intensidad.
- Esto es solo un duplicado de la ya existente implementación de luces puntuales con algunos cambios.
- Later it may be useful to add a way to visualize the light direction by displaying a mesh that is positioned at camera\'s view point like an arrow that displays how the sun lights the scene for example.

![image22](images/entries/4dcd7d7f4bcfb71d765656bfe734ec32ddcaca9c.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Soporte de texturizado para capa vectorial
Se ha agregado soporte de texturizado para QGIS 3D con las siguientes nuevas funcionalidades:
- Los usuarios ahora pueden seleccionar una imagen para que se muestre en las superficies de los edificios como mapa difuso de las propiedades del símbolo.
- El usuario también puede cambiar la escala de texturas desde las propiedades del símbolo.

Some visual issues may appear when using textures. These issues relate to the normals of surfaces that you may be able to fix by checking \"add back faces\" and playing around with the invert normals and culling mode in the symbol properties.

![image23](images/entries/1c4fc6ffc1b7a28aeff9c625fb6238998dd30b67.webp)

This feature was developed by [Nedjima Belgacem](https://api.github.com/users/NEDJIMAbelgacem)
### Habilitar modelos 3D integrados y remotos para símbolos de puntos 3D
Los usuarios ahora pueden utilizar e incrustar modelos 3D remotos para símbolos de puntos 3D.

![image24](images/entries/d4deaabbeddcf5f4784f602f19dabfac22b2d100.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Agregar opción para mostrar los orígenes de la fuente de luz
Una función que permite a los usuarios alternar una esfera visible en los orígenes de la fuente de luz en una escena 3D.

Esto permite reposicionar y colocar más fácilmente las fuentes de luz en relación con el contenido de la escena.

Addresses [Issue #37726](https://github.com/qgis/QGIS/issues/37726).

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mejoras en el manejo de materiales
Se introdujeron más mejoras para el manejo de materiales y se agregó un modelo de sombreado Gooch. Esto mejora la API QgsAbstractMaterialSettings, al:
- Adición de soporte de iconos para los tipos de materiales registrados (para usar en el cuadro combinado del selector de materiales).
- Adds support for handling different rendering techniques to QgsAbstractMaterialSettings. Now material classes can indicate which rendering techniques they support (e.g. Triangles, Lines, InstancedPoints, etc.), and the material is only offered when it\'s compatible with the required technique.
- El manejo de la técnica en el widget de material de gooch se mejoró para evitar mostrar configuraciones que no tienen ningún efecto en un contexto particular (por ejemplo, ocultar todo excepto la elección de color ambiental para símbolos de línea 2D simples).
- A new material, \"Gooch\", was added. This material gives a CAD style 3D render, where the shading is not dependent on appropriate lighting setup in a scene and where the 3D details are always visible, regardless of the lighting choice.

![image25](images/entries/b6df518d57147bfdfd207d4499363c9d4653721b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Diseño de impresión
### Presenta el control sobre el formato de texto y la alineación de celdas individuales en tablas de texto manuales
Agrega control sobre la configuración del formato de texto (por ejemplo, negrita / cursiva / búfer / sombra, etc.) y la alineación del texto (horizontal y vertical) para el contenido de celdas individuales en una tabla de texto manual.

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Use QgsTextRenderer para representar el texto de la tabla de atributos
Permite la gama completa de opciones de formato de texto en tablas de atributos de diseño, incluidos búferes, sombras, espaciado de palabras, etc.

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Use QgsTextRenderer para dibujar el texto de la cuadrícula del mapa en composiciones
Permite anotaciones de cuadrícula que utilizan búferes, sombras, formas de fondo, etc.

![image26](images/entries/86863750-26550e00-c10f-11ea-8dd4-1b740017949e.gif)

![image27](images/entries/349efbc988ccbf3499e18ec4453b637abf893c38.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Presentar la opción para controlar el método de compresión de imágenes PDF al exportar diseños a PDF
Las opciones son para la compresión Lossy, que es la compresión JPEG predeterminada utilizada, y la compresión Lossless (que crea archivos más grandes en la mayoría de los casos, pero es mucho más adecuada para impresiones profesionales o para postproducción en otros productos como Illustrator, etc.)

La mala noticia es que esta opción solo está disponible en compilaciones basadas en Qt 5.13 o posterior.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agregar configuración de recorte automático para mapas de atlas
Esta función permite a los usuarios habilitar el recorte de mapas para los elementos del mapa de diseño, de modo que los mapas se recorten al límite de la función del área del atlas actual.

La opciones existentes son:
- Habilitar o deshabilitar el recorte por base de mapa
- Especificar el tipo de recorte:
  - "Clip During Render Only": applies a painter based clip, so that portions of vector features which sit outside the atlas feature become invisible
  - "Clip Feature Before Render": applies the clip before rendering features, so borders of features which fall partially outside the atlas feature will still be visible on the boundary of the atlas feature
  - "Render Intersecting Features Unchanged": just renders all features which intersect the current atlas feature, but without clipping their geometry
- Controlar si las etiquetas deben colocarse a la fuerza dentro de la entidad del atlas o si pueden colocarse fuera de la entidad
- Restringir el corte a un subconjunto de las capas del proyecto, de modo que solo se recorten algunas

![image28](images/entries/86433831-191ad680-bd3f-11ea-9289-cc6d2b3e2e11.gif)

![image29](images/entries/1f1343d09c75b0e1d131c25a79b905d7aaadbc35.webp)

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agrega una API a QgsMapSettings para especificar regiones de recorte a aplicar mientras se renderizan mapas
Actualmente, esta es una funcionalidad solo de API, pero se ha agregado una funcionalidad que proporciona las capacidades de backend para especificar las regiones de recorte que se pueden usar durante las operaciones de representación de mapas.

Although primarily introduced in order to provide functionality which allows the automatic clipping of map elements to the current atlas feature geometry in print layouts, the API has been deliberately implemented in a manner that\'s very flexible to allow various use cases which require the clipping of regions during map render operations.

Para las capas no vectoriales, el recorte se aplica mediante un trazado de recorte QPainter. Para capas vectoriales, la API expone varias opciones sobre cómo se debe aplicar el recorte:
1. As an \"intersects\" style test only: All vector features which intersect the path are rendered, without actually clipping the feature\'s geometry
2. By modifying the feature\'s geometry and clipping the geometry to the region: Any stroke or outline settings for the symbol will be rendered along the boundary of the clipping region, even if the feature actually partially falls outside this region.

o
1. Uso de una ruta de recorte de pintor: las entidades se recortan en la región, pero solo en el momento del pintor. Los límites de la función que quedan fuera de la región de recorte no serán visibles.

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Tamaño máximo de marcador de leyenda de diseño
Agrega la posibilidad de ingresar el tamaño máximo del marcador (en mm) al widget de leyenda de diseño.

En algunos casos, como cuando las capas de puntos usan un tamaño de símbolo que se basa en unidades de mapa, los marcadores de puntos en la leyenda del diseño pueden volverse bastante grandes. Esta función agrega una configuración al widget de leyenda de diseño que permite la restricción del tamaño máximo del símbolo de marcador mientras la actualización automática de la leyenda aún está activa.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
### Permitir que las celdas de las tablas de texto manual tengan contenido basado en expresiones
Permite que las celdas individuales de una tabla de texto manual tomen su contenido de una expresión preestablecida. Las expresiones tienen acceso al contexto de expresión del elemento de diseño completo, lo que permite que las celdas calculen y muestren valores de estilo de metadatos o cálculos basados en agregados.

Esta funcionalidad fue financiada por City of Canning

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Recortar mapas de diseño para darles forma
Se introdujo una nueva funcionalidad que permite a los usuarios recortar un elemento de mapa a una forma o elemento poligonal desde su diseño, lo que permite mapas no rectangulares dentro del diseño.

![image30](images/entries/88761088-c1428480-d1b1-11ea-90c0-a391d00b084d.gif)

![image31](images/entries/7179282b09e8d196251f543a9c5f059f89c701e2.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Soporte para marcas/anotaciones rotados
Tick marks and annotations on a map frame in the print composer can now be rotated, allowing them to align with a rotated map frame as described in [issue 36904](https://github.com/qgis/QGIS/issues/36904). It works for both rotated maps and reprojected grids.

Las sisguientes opciones se han añadido:
- Marcas:
  - Rotar marcas (si no se marca, las marcas se dibujan como antes, sin tener en cuenta el ángulo)
  - Alineación de marcas rotadas (si las marcas deben tener una longitud constante o estar alineadas ortogonalmente)
  - Skip low angled ticks (an angle threshold below which ticks aren\'t drawn, so you can skip ticks for grid lines that are, for example, too close to being parallel with the map edge)
- Anotaciones:
  - Paralelo a la marca (junto a/ horizontal/ vertical ascendente/ vertical descendente)
  - Dibuje un ángulo bajo (si está marcado, las marcas omitidas arriba aún recibirán una anotación)

![image32](images/entries/0da542215cefcd2e3ca120dd0381b47611734dce.gif)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
### Agregar expresión de desplazamiento de página para posiciones Y
A `layout_pageoffsets` expression was added for print layouts which returns an array of Y coordinates for the top of each page in the layout. this allows users to dynamically position items on pages in a context where page sizes may change.

For example, to set an item at 2.5mm from the top of page 2 (for the data-defined position Y of a map item) : `@layout_pageoffsets[1] + 2.5`

This constitutes a workaround for [Issue 37567](https://github.com/qgis/QGIS/issues/37567).

This feature was funded by [BikePlan](https://www.bikeplan.swiss/)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Expresiones
### Add to_decimal() function to convert DMS to DD
A new `QgsCoordinateUtils::dmsToDecimal` function has been added which exposes the `to_decimal` function in expressions. This allows the conversion of DMS (degree/minute/second) strings into DD (decimal degree) format.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Add \"main_angle\" function to return the estimated main angle of a geometry
Devuelve el ángulo del cuadro delimitador mínimo orientado que cubre el valor de la geometría.

Useful for data defined overrides in the symbology of label expressions, e.g. to rotate labels to match the overall angle of a polygon, and similar for line pattern fill. ![image33](images/entries/87367553-aae7d680-c5be-11ea-923a-e81200f2b90c.gif)

![image34](images/entries/03463ac0a8303444d94806fb2ff66d6a73c56ccb.webp)

This feature was funded by [Kanton Solothurn](https://geo.so.ch/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funciones de referencia del puerto al núcleo
Se han agregado varias operaciones de superposición al motor de expresión. Esto cubre la funcionalidad del complemento refFunctions.

![image35](images/entries/90797864-7bd92900-e311-11ea-945f-0c2ade14e801.gif)

The following new expression functions are implemented:

    * overlay_intersects(layer[,expression][,filter][,limit][,cache])
    * overlay_contains(layer[,expression][,filter][,limit][,cache])
    * overlay_crosses(layer[,expression][,filter][,limit][,cache])
    * overlay_equals(layer[,expression][,filter][,limit][,cache])
    * overlay_touches(layer[,expression][,filter][,limit][,cache])
    * overlay_disjoint(layer[,expression][,filter][,limit][,cache])
    * overlay_within(layer[,expression][,filter][,limit][,cache])
    * overlay_nearest(layer[,expression][,filter][,limit][,max_distance][,cache])
    
En todos los casos, el operador espacial se evalúa frente a la otra capa. Si se proporciona una expresión, devuelve una matriz de resultados. Si no se proporciona ninguna expresión, devuelve un valor booleano que indica si hay una coincidencia o no para al menos una característica. Las entidades se pueden filtrar opcionalmente por una expresión y, opcionalmente, limitarse a un cierto recuento.

The `overlay_nearest` function has an additional max_distance filter.

![image36](images/entries/d4bb059729eecfc689e001f731d59fff25225615.webp)

This feature was developed by [Olivier Dalang, OPENGIS.ch](https://www.opengis.ch)
## Digitalizando
### Agregue la opción para calcular el rumbo según la dirección del viaje
En el caso de dispositivos que notifican mediciones de rumbo incorrectas, esta opción se puede utilizar para calcular el rumbo del GPS en función de las dos ubicaciones registradas anteriormente.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Digitalización y división de entidades  curvas
Se introdujo una nueva funcionalidad que agrega la posibilidad de cambiar entre cadenas lineales o circulares al digitalizar o dividir entidades de capas vectoriales.

El usuario puede utilizar el método abreviado de teclado **Ctrl+Shift+G** para cambiar entre lineal/circular.

For splitting features, new overloading methods have been added to the API. When splitting, curves are preserved. For this, the curve is segmentized before splitting, and all the split features are \"de-segmentized\" after splitting.

A toolbar button was added to enable switching between linear/circular: ![image37](images/entries/88101713-6505b200-cb6c-11ea-9feb-68a4130d6f52.gif)

![image38](images/entries/86938423-6a93de80-c10e-11ea-8511-489d8b4f006f.gif)

![image39](images/entries/86938444-7089bf80-c10e-11ea-8fd0-0f419f71b52e.gif)

![image40](images/entries/8145ccfa4e659f7d8315830cecfe2b2f391b9aa4.webp)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
## Administración de datos
### Algoritmo de reescalar ráster para procesamiento
Adds a rescale raster algorithm to change raster value range, whilst preserving the shape of the raster\'s histogram. Useful for when rasters from different sources should be compared or processed together and their pixel values should be in the same range. By default, the algorithm preserves the NODATA value of the input raster but there is an option to override it.

The following image displays a histogram of a DEM (value range is 85-243) ![image41](images/entries/86897604-53ee8700-c110-11ea-99ae-540d38f88154.webp) And the next image displays a histogram of same DEM rescaled to the range 100-1000 ![image42](images/entries/86897671-67015700-c110-11ea-8183-e0d6bd013dbb.webp)

Addresses [Issue 26099](https://github.com/qgis/QGIS/issues/26099).

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
## Widgets y Formularios
### Múltiples widgets para una sola relación
Ahora se pueden crear varios widgets de relación para una sola relación, cada uno con su propia configuración distinta.

This feature changes the behavior of relation widgets created in the drag and drop interface and provides resolution for [Issue 37675](https://github.com/qgis/QGIS/issues/37675).

Al leer un proyecto configurado con versiones anteriores de QGIS, la configuración se toma y se escribe en la nueva configuración del widget. Los formularios autogenerados ya no permiten la configuración de los widgets del editor de relaciones, pero si se ha configurado en un QGIS anterior, el formulario de atributo seguirá leyendo esta configuración.

![image44](images/entries/d3a51f9b7ea6ffa3c8c8c457e3d6278d57bcf125.gif)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Mostrar entidades relacionadas en el árbol de resultados de identificación
Los usuarios ahora podrán ver entidades relacionadas (secundarias) en la ventana de resultados cuando usen la herramienta de identificación. Debajo de cada entidad principal identificada, se mostrarán nuevos grupos que contienen cualquier entidad secundaria relacionada, mostrando sus atributos, acciones y permitiendo al usuario abrir directamente el formulario de entidad para la entidad secundaria.

This feature addresses issue [18634](https://github.com/qgis/QGIS/issues/18634).

![image45](images/entries/863b80851b995421b6f2ea455faf6b1c41211cd5.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Filtrar expresiones en el widget de relación de referencia
Se ha agregado una opción para que la expresión de filtro estática se use en el widget de relación de referencia.

![image46](images/entries/8048bb8df64e31bb733eea239c527f8be631ce6f.gif)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Herramientas de análisis
### Agregar tiempos de carga del proyecto de perfil a la base de herramientas de depuración
Modification of the QgsRuntimeProfiler class which performs the following functions: 1. Make the profiling thread-safe, so that it\'s possible to record times across multiple threads 2. Allows different profiling \"groups\"

The new groups API is used here to expose a breakdown of project load times in the debugging dock, alongside the existing QGIS startup profiling. It\'s possible now to get a breakdown of the various stages of project load, in order to identify the causes of slow project load times.

TODO: In the majority of cases, performance problems will be caused by one or more layers, so it would be nice to further break down the individual layer load times. For example, for an individual WFS layer, we may see the time taken for the initial \"server capabilities\" or other queries. Add a group with profile times for map rendering, so you can see exactly which layers in your project are causing slow map redraw times.

En su forma actual, solo se muestra el tiempo de carga total de cada capa individual.

![image47](images/entries/85852208-7bca1a80-b7f3-11ea-8882-b3253622b1b6.webp)

![image48](images/entries/943a79db68aee3458cb88cacd7a69b66fda3caea.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Procesado
### añadir cadena de ayuda para parámetros
Las cadenas de ayuda ahora pueden ser especificadas a nivel de parámetro.

Esto puede ser visible en la herramienta de consejo, en la CLI y API de Procesos de Python.

![image55](images/entries/2196bcb0123ced5e180ffb2b9469a65a38dcc41b.webp)

This feature was developed by [Étienne Trimaille](https://api.github.com/users/Gustry)
### New \"Align points to features\" algorithm
Este algoritmo calcula la rotación necesaria para alinear entidades puntuales con su entidad más cercana de otra capa de referencia. Se agrega un nuevo campo a la capa de salida que se rellena con el ángulo (en grados, en el sentido de las agujas del reloj) hasta la entidad de referencia más cercana.

Optionally, the output layer\'s symbology can be set to automatically use the calculated rotation field to rotate marker symbols.

Si lo desea, se puede establecer una distancia máxima para usar al alinear puntos para evitar alinear puntos aislados con entidades distantes.

Un caso de uso de ejemplo para esto es la alineación de símbolos de puntos de construcción para seguir la dirección de la carretera más cercana mediante el uso de un valor de rotación definido por datos generado por este algoritmo.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agregue un algoritmo modelador para crear directorios
Este algoritmo permite a los modelos crear nuevos directorios de archivos. Útil para modelos que tienen que generar resultados en ciertas rutas creadas dinámicamente (por ejemplo, una carpeta que contiene la fecha actual).

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agregue un algoritmo de modelador para establecer una variable de expresión de proyecto
Allows a model to set Project-level expression variables during execution. Especially useful with the new [Export Print Layout algorithms](https://github.com/qgis/QGIS/pull/36916) to allow models which dynamically set variables used in a layout prior to export.

This functionality was ported from <https://gis.stackexchange.com/questions/359386>

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agregar algoritmos de procesamiento para exportar un diseño de impresión como PDF/imagen
Los modelos pueden exportar diseños de impresión del proyecto actual. Un caso de uso para esto es permitir a los usuarios crear un modelo en el proyecto que exporta un conjunto particular de diseños del proyecto a ciertas carpetas, de modo que puedan reexportar fácilmente el proyecto actual en una sola operación en lugar de tener que abrir manualmente múltiples diseños y exportar uno por uno.

Además, con las nuevas capacidades para tener archivos de salida basados en expresiones dentro de los modelos, puede exportar automáticamente los diseños a una carpeta con la etiqueta de fecha actual e incluirla en los nombres de los archivos exportados.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Agregar funciones de guardado al algoritmo de archivo
Ahora existe un algoritmo de procesamiento nativo para guardar entidades vectoriales en un conjunto de datos de archivo dentro de un modelo. Viene con un par de funciones avanzadas para pasar opciones de capas y conjuntos de datos a GDAL.

![image56](images/entries/b238631365830b019300700cf59c3a8dd3d05a4f.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Exportar atlas de diseño como algoritmo PDF
Se agregó un nuevo algoritmo de procesamiento QGIS que permite la exportación de un atlas de mapas a PDF. Esta es la contraparte en PDF del reciente algoritmo de diseño de atlas de exportación a imagen.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### New \"Flatten Relationship\" algorithm
Este algoritmo aplana todas las relaciones para una capa vectorial, exportando una sola capa que contiene una entidad maestra por entidad relacionada. Esta entidad maestra contiene todos los atributos de las entidades relacionadas.

It\'s designed as a quick way to de-normalize a relation from a project, e.g. to allow exporting to CSV.

Esta prestación fue financiada por SMEC/SJ

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Exportar diseño de atlas como algoritmo de imagen
Un nuevo algoritmo nativo de procesos fue añadido a exportar diseño de atlas como imagenes.

Esto es útil en modelos en los que se procesan conjuntos de datos remotos con el objetivo de utilizarlos como capas de cobertura de atlas.

![image57](images/entries/e4f315e60743577c9f45ad44643fd5ba9778c040.webp)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Nuevo algoritmo de estadísticas de celda
Agregamos un algoritmo de análisis ráster **Estadísticas de celda**. Realiza estadísticas por celda en una pila de capas ráster mientras tiene en cuenta NoData. Las funciones disponibles en la implementación actual son:

|
- Suma
- Media
- Mediana
- Desviación estandar
- Varianza
- Máximo
- Mínimo
- Mayoría (valor mas frecuente)
- Minoría (valor menos frecuente)
- Rango (max - min)
- Variedad (recuento de valores únicos)

![image49](images/entries/fca13f48b118ed13ebe84191a226ca0e20c37bfa.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Nuevo algorimto Igual a frecuencia
Hemos agregado algunos algoritmos de ráster nuevos que operan celda por celda local en una pila de ráster. El algoritmo Igual a frecuencia evalúa celda por celda la frecuencia (número de veces) que los valores de una pila de rásteres de entrada son iguales al valor de un ráster de valor.

![image50](images/entries/e368e10cfa5e19992176930121e0cb846c3d1ca8.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Nuevo algoritmo mayor que la frecuencia
Hemos agregado algunos algoritmos de ráster nuevos que operan celda por celda local en una pila de ráster. El algoritmo Mayor que la frecuencia evalúa celda por celda la frecuencia (número de veces) que los valores de una pila de rásteres de entrada son mayores que el valor de un ráster de valor.

![image51](images/entries/97228db861367c2875dab0533ab616bb2ac2432c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nuevo algoritmo de menor frecuencia
Hemos agregado algunos algoritmos de ráster nuevos que operan celda por celda local en una pila de ráster. El algoritmo Menor a frecuencia evalúa, celda por celda, la frecuencia (número de veces) que los valores de una pila de rásteres de entrada son menores que el valor de un ráster de valor.

![image52](images/entries/114853cd3d7c245b56edea0024704c853997275c.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nueva posición más baja en el algoritmo de pila de ráster
Agregamos algunas herramientas de análisis de posición de valor de ráster con esta nueva versión de QGIS: El algoritmo *Posición más baja en la pila de ráster* evalúa celda por celda la posición del ráster con el valor más bajo en una pila de rásteres. Los recuentos de posiciones comienzan con 1 y van hasta el número total de rásteres de entrada. El orden de los rásteres de entrada es relevante para el algoritmo.

![image53](images/entries/f3383f5583c9096b1b8d1873679e1a495fac0485.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Nuevo algoritmo posición más alta en la pila de ráster
Agregamos algunas herramientas de análisis de posición de valor de ráster con esta nueva versión de QGIS: El algoritmo *Posición más alta en la pila de ráster* evalúa celda por celda la posición del ráster con el valor más alto en una pila de rásteres. Los recuentos de posiciones comienzan con 1 y van hasta el número total de rásteres de entrada. El orden de los rásteres de entrada es relevante para el algoritmo.

![image54](images/entries/a730b8c1566c99bdebff09c783ae320b0c138d76.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Cargar los resultados del procesamiento en el grupo de capas
Users can now optionally set a group name which ensures that the resulting output layers added to the project when using the *Open output file after running algorithm* option are grouped together. This allows all outputs from several processing algorithms to be grouped so that they may be easily located in the layer tree and be removed, exported, or have their visibility toggled easily. ![image58](images/entries/414c68839518d5b658d6e6f1565f6c27e1f4336f.gif)

This feature was developed by [Germán Carrillo](https://github.com/gacarrillor)
### Agregar un algoritmo de estadísticas zonales que cree una nueva salida
Previously, when calculating zonal statistics, the algorithm always updated the original data source, adding additional fields. A new zonal statistics algorithm has been added which creates a new output instead. This functionality is an implementation of the [29504 feature request](https://github.com/qgis/QGIS/issues/29504).

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Agregar parámetro de procesamiento de geometría
Added a new `QgisProcessingParameterGeometry` for passing geometries as a parameter to processing alogrithms.

Esto proporciona una forma de pasar geometrías simples a algoritmos sin requerir una capa de entrada.

Los casos de uso inmediatos son:
- Algoritmos que podrían necesitar manipular geometrías de forma atómica.
- Delegación desde algoritmos parentales.
- Úselo con procesamiento qgis sin cabeza en herramientas de procesamiento independientes.

Prestaciones:
- El parámetro es compatible con los parámetros de cadena, ya que puede pasar Well-Known-Text como valor.
- La interacción del widget actual es minimalista, ya que solo usa el widget de texto de entrada para ingresar el valor como WKT.

This feature was developed by [David Marteau](https://api.github.com/users/dmarteau)
### Agrega una interfaz para determinar si es seguro que la aplicación salga
Se agregó una interfaz para complementos y scripts para registrar lógica personalizada para evitar que la aplicación QGIS salga. Esto permite que los complementos determinen si es seguro que la aplicación salga. Esto ha hecho posible permitir que los complementos determinen si hay cambios no guardados que deben guardarse o descartarse antes de permitir la salida de QGIS, funcionalidad que ya se implementó en el editor de scripts de la consola, evitando la pérdida de datos al avisar a los usuarios cuando hay cambios no guardados. en lugar de cerrar silenciosamente la aplicación.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Opciones de Aplicación y Proyecto
### Lista de controladores vectoriales GDAL disponibles
A *Vector Drivers* tab is now available within the QGIS GDAL Settings window, which lists all the available GDAL vector drivers and allows users to toggle their active state. Where several drivers may be used to open data of a specific type, users may now modify these settings to ensure that the intended driver is used when importing specific vector data types. For example, the FileGDB and OpenFileGDB drivers are both capable of being used to import .gdb files, but if the data file has a version of 9.x, the FileGDB won\'t be able to open it. In this instance, a user may disable the FileGDB driver and ensure that the data is loaded using the OpenFileGDB driver instead.

This functionality directly addresses the limitations outlined in [Issue 18738](https://github.com/qgis/QGIS/issues/18738).

![image59](images/entries/5cc48d8ea8bc276446f8eae4a1c838e0d1f91a40.webp)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Detectar la carpeta de instalación de GRASS en MacOS
MacOS previously had a platform-specific custom parameter setting Grass7Utils.GRASS_FOLDER. This caused crashes for many users with multiple QGIS installations or who had some invalid folder settings. The parameter has been removed and a GISBASE environment variable has been introduced instead, which is commonly used in GRASS scripts as the \"root\" installation directory, emulating the behavior used for GRASS detection in Windows environments. If GISBASE is not present (default), a search is performed for grass folders in `QgsApplication.prefixPath()` (when packaged in bundle format). If not found, the standalone GRASS instance is searched for. The new behaviour for GRASS is in-line with the methodology used for the GDAL and SAGA processing tools.

This resolves [Issue 38595](https://github.com/qgis/QGIS/issues/38595).

![image60](images/entries/e59bb83513293830df8ec4dcf825247b14dacc98.webp)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://api.github.com/users/PeterPetrik)
## Navegador
### Exponer campos en el navegador
First part of QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/171>

Expone columnas de campo en el navegador para proveedores que implementan conexiones API:
- PG
- GPKG
- Spatialite
- MSSQL

Las siguientes operaciones con soportadas en campos:
- añadir nuevo campo
- borrar campo

![image61](images/entries/87223743-a4b7e700-c37f-11ea-88a3-4b371bfadf89.gif)

![image62](images/entries/d4e761ad977a712aa1fc1fbc65d61c886e6e79fb.webp)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
## Proveedores de datos
### Conexiones de Servicios de Tesela Vectorial de ArcGIS
Se agregó una opción para crear conexiones para ArcGIS Vector Tile Services para permitir a los usuarios cargar fácilmente capas de mosaicos vectoriales desde los servicios de mosaicos vectoriales de ArcGIS Server. También agregó soporte para autenticación, configuración y cadena de referencia personalizada para conexiones de mosaicos vectoriales.

Este cambio agrega opciones de IU explícitas para agregar y configurar conexiones a los servicios de teselas vectoriales de ESRI. Si bien estos servicios utilizan el marco de mosaico vectorial estándar para la recuperación de datos, se pueden agregar directamente creando una conexión mediante el punto final de la API VectorTileService en el servidor ArcGIS.

After a user adds a layer from a VectorTileService, the server\'s default styling and labeling for the layer is automatically loaded.

![image63](images/entries/e31c882fa9552ed6bd247f0092305ae8c153948a.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Propagación de metadatos de la capa de confianza
La bandera de confianza a nivel de proyecto solo se usa para leer la extensión de la capa vectorial desde xml, no desde el proveedor.

This flag was not available at the vector layer and data provider level. A new QgsMapLayer reading flag to propagate the trust layer metadata for the project\'s read flag and a new provider flag to trust the datasource config.

Confiar en la configuración de la fuente de datos permite al proveedor usar metadatos estimados, asegura que la clave principal sea única y que el tipo de geometría detectable y el SRID sean los mismos que los solicitados.

This feature was developed by [rldhont](https://api.github.com/users/rldhont)
### Añadir soporte para columnas virtuales en Oracle
Soporte para columnas virtuales (generadas) de Oracle ha sido añadido y se define de este modo:

`sql CREATE TABLE QGIS.GENERATED_COLUMNS ( "pk" INTEGER PRIMARY KEY, "generated_field" GENERATED ALWAYS AS ('test:' || "pk") VIRTUAL);`

**Note:** It\'s not possible to define a generated column on an SDO_GEOMETRY field in Oracle.

For now, when creating a new feature, the generated field is editable and should not be. A new API method needs to be added to retrieve readonly field from the provider as discussed in [Issue 35995](https://github.com/qgis/QGIS/pull/35995#issuecomment-633055700).

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Añadir opciones avanzadas para importar datos
Se ha introducido una nueva funcionalidad que permite especificar parámetros avanzados al importar capas utilizando el proveedor de datos OGR, lo que abre una amplia gama de nuevas posibilidades, especialmente cuando se trabaja con problemas esperados del conjunto de datos.

![image64](images/entries/e1c7474d19828b39f5872b289a1e8ba994556a10-1.webp)

![image65](images/entries/4a2d99c6ef6ec12e5f63a29ad00d9ebc3cd534e2.webp)

This feature was developed by [Even Rouault](https://api.github.com/users/rouault)
## Servidor de QGIS
### Ordenar mediante API WFS3 del servidor QGIS
Añade ordenado funcional a la API del Servidor de QGIS WFS3

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Complemento de la página de destino del servidor QGIS
A Landing Page Plugin for QGIS Server was created, which is a C++ port of <https://github.com/elpaso/qgis-server-landing-page-plugin>

![image66](images/entries/a2254bbef892835317a9f608afd8bd3722ee4b38.gif)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### variable de entorno para deshabilitar GetPrint y no cargar diseños
A new `QGIS_SERVER_DISABLE_GETPRINT` environment variable was added to QGIS Server which prevents the loading of layouts when projects are read and disables the WMS GetPrint request, improving the read time of projects.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
### variable de entorno para confiar en los metadatos de la capa con la configuración del servidor
Los metadatos de la capa de confianza se pueden definir a nivel de proyecto. Se agregó una nueva marca de lectura del proyecto que permite forzar los metadatos de la capa de confianza.

For QGIS server, the trust layer metadata option can be overridden with `QGIS_SERVER_TRUST_LAYER_METADATA` environment variable.

This feature was funded by [Ifremer](https://wwz.ifremer.fr)

This feature was developed by [3Liz](https://www.3liz.com)
## Correcciones Notables
### Error corregido por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Scrolling attribute table of a layer added with the \"delimted text provider\" is almost impossible | [#38068](https://github.com/qgis/QGIS/issues/38068) | [PR #38735](https://github.com/qgis/QGIS/pull/38735) | [PR #38745](https://github.com/qgis/QGIS/pull/38745) |
| soporte para claves API a través de una consulta para la implementación API de funciones API OGC | [#38436](https://github.com/qgis/QGIS/issues/38436) | [PR #38738](https://github.com/qgis/QGIS/pull/38738) | N/D |
| El SRC personalizado no siempre cambia los parámetros correctamente de wkt a proj string | [#38689](https://github.com/qgis/QGIS/issues/38689) | No se ejecuta |  |
| El cliente de funciones de la API de OGC siempre usa el límite=1000 | [#38666](https://github.com/qgis/QGIS/issues/38666) | No se ejecuta |  |
| La exportación a geopaquete cambia el tipo de campo de DATE a DATETIME | [#37857](https://github.com/qgis/QGIS/issues/37857) | no es un error |  |
| El campo de fecha CSV se interpreta como tipo de hora | [#38091](https://github.com/qgis/QGIS/issues/38091) | [PR #38741](https://github.com/qgis/QGIS/pull/38741) | N/D |
| Diferencia de transformación de coordenadas entre QGIS y Proj | [#38190](https://github.com/qgis/QGIS/issues/38190) | problema de uso |  |
| gdal_rasterize not working when file has \'&\' symbol in name | [#38674](https://github.com/qgis/QGIS/issues/38674) | [PR #38743](https://github.com/qgis/QGIS/pull/38743) | [PR #38747](https://github.com/qgis/QGIS/pull/38747) |
| Volcado de núcleo cuando se usa la función de identificación en un polígono vectorial | [#36213](https://github.com/qgis/QGIS/issues/36213) | ya corregido |  |
| Error del histograma ráster de QGIS 3.10.8(LTR) | [#38298](https://github.com/qgis/QGIS/issues/38298) | [PR #38769](https://github.com/qgis/QGIS/pull/38769) | PORHACER. |
| \[Postgres\] Cannot edit attribute when there is no primary key | [#37917](https://github.com/qgis/QGIS/issues/37917) | no un error IMHO |  |
| El cambio entre formatos de salida de información de WMS arroja: CRITICAL QTableWidget: no se puede insertar un elemento que ya es propiedad de otro QTableWidget | [#37215](https://github.com/qgis/QGIS/issues/37215) | [PR #38770](https://github.com/qgis/QGIS/pull/38770) | [PR #38783](https://github.com/qgis/QGIS/pull/38783) |
| Guardar como Geopackage: campos de TEXT convertidos a TEXT(255) | [#25405](https://github.com/qgis/QGIS/issues/25405) | ya corregido |  |
| \"Join attributes by nearest\" tool defaults to \"None\" when using Max distance of 0 | [#38761](https://github.com/qgis/QGIS/issues/38761) | [PR #38773](https://github.com/qgis/QGIS/pull/38773) | No, not appropriate (see [PR #38778](https://github.com/qgis/QGIS/pull/38778)) |
| Ediciones perdidas en capa del mismo grupo de transacción | [#38697](https://github.com/qgis/QGIS/issues/38697) | [PR #38779](https://github.com/qgis/QGIS/pull/38779) + [PR #38780](https://github.com/qgis/QGIS/pull/38780) | [PR #38824](https://github.com/qgis/QGIS/pull/38824) |
| Preview of Expression String Builder \'freezes\' if Feature id higher then available | [#38646](https://github.com/qgis/QGIS/issues/38646) | [PR #38797](https://github.com/qgis/QGIS/pull/38797) | N/D |
| Proveedor VectorFileWriter/OGR: solución alternativa de error GDAL 3.1.x con respecto a la creación de XLSX y ODS | no reportado | [PR #38837](https://github.com/qgis/QGIS/pull/38837) | [PR #38853](https://github.com/qgis/QGIS/pull/38853) |
| Widget de operación coordinada: evite repetir el alcance y las observaciones | no reportado | [PR #38847](https://github.com/qgis/QGIS/pull/38847) | N/D |
| Congelado al mostrar tabla de atributos de capa WFS | [#37224](https://github.com/qgis/QGIS/issues/37224) | [PR #38952](https://github.com/qgis/QGIS/pull/38952) | [PR #38956](https://github.com/qgis/QGIS/pull/38956) |
| OGR Error al editar un archivo kml | [#39087](https://github.com/qgis/QGIS/issues/39087) | [GDAL Commit 72e1a4d7c96e0381d2d335857697b5f8e1668450](https://github.com/OSGeo/gdal/commit/72e1a4d7c96e0381d2d335857697b5f8e1668450) | Retroportado a la rama GDAL 3.1 también |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Errores corregido por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| La carga de capas de PostGIS sin geometría especificada carga todas las entidades en la tabla de atributos. | [PR #35367](https://github.com/qgis/QGIS/pull/35367) [#38565](https://github.com/qgis/QGIS/issues/38565) | Retroportar solamente | [PR #38736](https://github.com/qgis/QGIS/pull/38736) |
| Servidor API: el proyecto actual ya no se puede configurar | [#38755](https://github.com/qgis/QGIS/issues/38755) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) | [PR #38758](https://github.com/qgis/QGIS/pull/38758) |
| La capa PostGIS guardada en el proyecto 3.10 no se carga correctamente en 3.14 | [#38567](https://github.com/qgis/QGIS/issues/38567) | [PR #38763](https://github.com/qgis/QGIS/pull/38763) | N/D |
| Servidor WFS-T 1.1.0 caso incorrecto para totalUpdated, totalInserted, totalDeleted | [#38558](https://github.com/qgis/QGIS/issues/38558) | [PR #38764](https://github.com/qgis/QGIS/pull/38764) | PORHACER. |
| El servidor se bloquea en GetLegendGraphics cuando RULE no existe. | [#38766](https://github.com/qgis/QGIS/issues/38766) | [PR #38775](https://github.com/qgis/QGIS/pull/38775) | [PR #38794](https://github.com/qgis/QGIS/pull/38794) |
| La vista de formulario se atasca en el último valor no NULL mostrado para algunos atributos al navegar por los datos | [#38552](https://github.com/qgis/QGIS/issues/38552) | [PR #38801](https://github.com/qgis/QGIS/pull/38801) | PORHACER. |
| Línea de marcador Anulación de rotación de marcador simple que no respeta la configuración de dirección de línea de seguimiento | [#38716](https://github.com/qgis/QGIS/issues/38716) | [PR #38815](https://github.com/qgis/QGIS/pull/38815) |  |
| Unable to dock the \"snapping options\" widget | [#38604](https://github.com/qgis/QGIS/issues/38604) | trabaja para mi |  |
| Can\'t read PG data sources when saved in version 3.10 and using service / auth combo | [#38809](https://github.com/qgis/QGIS/issues/38809) | [PR #38833](https://github.com/qgis/QGIS/pull/38833) | N/D |
| DB Manager \"cancel\" button to stop a query is not working | [#38092](https://github.com/qgis/QGIS/issues/38092) | [PR #38870](https://github.com/qgis/QGIS/pull/38870) | N/D |
| GDAL enhancement related to [#38092](https://github.com/qgis/QGIS/issues/38092) | [#38092](https://github.com/qgis/QGIS/issues/38092)2 | <https://github.com/OSGeo/gdal/pull/2953#event-3788638320> | N/D |
| Problema de cambio de valores al crear un nuevo campo en Administrador de BBDD | [#38800](https://github.com/qgis/QGIS/issues/38800) | trabaja para mi |  |
| Problema con VUV wms | [#38924](https://github.com/qgis/QGIS/issues/38924) | trabaja para mi |  |
| Administrador de fuente de datos: Ventana WMS/WMTS no redimensionable | [#38903](https://github.com/qgis/QGIS/issues/38903) | trabaja para mi, retroalimentación pendiente |  |
| Form tab option \"Show as group box\" won\'t save or apply | [#38539](https://github.com/qgis/QGIS/issues/38539) | trabaja para mi |  |
| El bloqueo de escala se ignora al realizar una panorámica del mapa | [#38953](https://github.com/qgis/QGIS/issues/38953) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/D |
| Zoom a capa sobrescribe error de escala bloqueado | [#38417](https://github.com/qgis/QGIS/issues/38417) | [PR #38954](https://github.com/qgis/QGIS/pull/38954) | N/D |
| Nombres de columnas repetidos causan problemas de visualización en el Administrador de Bases de Datos. | [#38976](https://github.com/qgis/QGIS/issues/38976) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/D |
| \"show search_path\" returns 0 rows | [#38975](https://github.com/qgis/QGIS/issues/38975) | [PR #38981](https://github.com/qgis/QGIS/pull/38981) | N/D |
| PG NOTIFY no accesible | [#38986](https://github.com/qgis/QGIS/issues/38986) | trabaja para mi |  |
| Corregir PG administrador de BBDD al renombrar esquema | [#38998](https://github.com/qgis/QGIS/issues/38998) | [PR #39000](https://github.com/qgis/QGIS/pull/39000) | N/D |
| Varios problemas de UX de elementos del navegador PG | [#39001](https://github.com/qgis/QGIS/issues/39001) | [PR #39006](https://github.com/qgis/QGIS/pull/39006) | N/D |
| Vectorial virtual no carga correctamente en Windows | [#35016](https://github.com/qgis/QGIS/issues/35016) | trabaja para mi en windows/actual maestro |  |
| Administrador de BBDD: los comentarios de campo de PostgreSQL no se muestran correctamente | [#38394](https://github.com/qgis/QGIS/issues/38394) | [PR #39026](https://github.com/qgis/QGIS/pull/39026) |  |
| Solo la primera fila de la tabla de ráster PostGis en la vista previa del Administrador de BBDD al añadir capa a lienzo de mapa | [#39017](https://github.com/qgis/QGIS/issues/39017) | [PR #39039](https://github.com/qgis/QGIS/pull/39039) | N/D |
| Consulta PostGIS errónea al intentar descubrir relaciones | [#39036](https://github.com/qgis/QGIS/issues/39036) |  |  |
| muchas tablas adicionales que ya están cargadas en el proyecto se cargan en la carga del proyecto debido a las dependencias de la capa | [#39025](https://github.com/qgis/QGIS/issues/39025) | [PR #39043](https://github.com/qgis/QGIS/pull/39043) | N/D |
| Corrección parcial para: asignaciones incorrectas de valores ráster a la simbología Valores únicos/paletizados o pseudocolor monobanda | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39071](https://github.com/qgis/QGIS/pull/39071) | N/D |
| Permite establecer la precisión para clasificar un ráster pseudocolor monobanda | no reportado | [PR #39079](https://github.com/qgis/QGIS/pull/39079) |  |
| Corrección completa para: asignaciones incorrectas de valores de ráster a la simbología Valores paletizados/únicos o pseudocolor monobanda | [#39058](https://github.com/qgis/QGIS/issues/39058) | [PR #39088](https://github.com/qgis/QGIS/pull/39088) | Arriesgado |
| Fallo con secuencia identificadora al añadir entidad | [#39093](https://github.com/qgis/QGIS/issues/39093) | trabaja para mi |  |
| Exportar informe a PDF quiebra QGIS si no hay diseño en modo de edición | [#39086](https://github.com/qgis/QGIS/issues/39086) | [PR #39135](https://github.com/qgis/QGIS/pull/39135) | PORHACER. |
| Ráster PG: los rásteres flotantes no muestran los valores de nodata correctamente en master/3.14 | [#39142](https://github.com/qgis/QGIS/issues/39142) | [#39142](https://github.com/qgis/QGIS/issues/39142) |  |
| Llamada de Python API QgsAbstractDatabaseProviderConnection::Excepciones de TableProperty no convertidas a QgsProviderConnectionException | [#39151](https://github.com/qgis/QGIS/issues/39151) | [PR #39152](https://github.com/qgis/QGIS/pull/39152) | N/D |
| Administrador de BBDD incapaz de mostrar columna geografía de PosGIS | [#37666](https://github.com/qgis/QGIS/issues/37666) | [PR #39154](https://github.com/qgis/QGIS/pull/39154) | N/D |
| Establecer un campo a NULL vía calculadora de campo congela QGIS | [#39178](https://github.com/qgis/QGIS/issues/39178) | [PR #39257](https://github.com/qgis/QGIS/pull/39257) | PORHACER. |
| Layer X: Feature has too many attributes (expecting 5, received 7) when \"Automatic Creation of Transaction Group\" is enabled | [#39230](https://github.com/qgis/QGIS/issues/39230) | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | [PR #39278](https://github.com/qgis/QGIS/pull/39278) |
| unreported crash when calling data provider\'s lastError on no errors | no reportado | [PR #39267](https://github.com/qgis/QGIS/pull/39267) | N/D |
| Quiebra al digitalizar una entidad cuando el grupo de transacción está habilitado (tras guardar) | [#39265](https://github.com/qgis/QGIS/issues/39265) | [PR #39283](https://github.com/qgis/QGIS/pull/39283) |  |
| Grupos de transacciones: capas no actuales un conjunto no editable después de guardar | [#39282](https://github.com/qgis/QGIS/issues/39282) | [PR #39286](https://github.com/qgis/QGIS/pull/39286) | no crítico |
| OGR decodeUri: ser tolerante en el caso de layerName | No reportado pero afecta a la documentación QGIS | [PR #39328](https://github.com/qgis/QGIS/pull/39328) | N/D |
| Manejo incorrecto de extensiones en enlaces cuando el nombre de la capa tiene puntos | no reportado | [PR #39346](https://github.com/qgis/QGIS/pull/39346) | N/D |
| Las contraseñas están codificadas en URL antes de la codificación base64 para la autenticación básica HTTP | [#39243](https://github.com/qgis/QGIS/issues/39243) | [PR #39347](https://github.com/qgis/QGIS/pull/39347) | [PR #39382](https://github.com/qgis/QGIS/pull/39382) |
| QGIS se bloquea en el menú Configuración si NO está en inglés | [#39430](https://github.com/qgis/QGIS/issues/39430) | [PR #39434](https://github.com/qgis/QGIS/pull/39434) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Error corregido por Peter Petrik
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Problema al mostrar malla y rotación de lienzo | [#35147](https://github.com/qgis/QGIS/issues/35147) | [PR #38795](https://github.com/qgis/QGIS/pull/38795)/files | no, no crítico |
| Quiebra al intentar usar malla | [#31773](https://github.com/qgis/QGIS/issues/31773) | No se ejecuta |  |
| Mal comportamiento del Administrador de Marcadores Espaciales y Quiebra de la App | [#35348](https://github.com/qgis/QGIS/issues/35348) | No se ejecuta |  |
| Fallo de segmentación 11 en el apagado de QGIS en MacOS | no reportado | [PR #38806](https://github.com/qgis/QGIS/pull/38806) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| Quiebra al crear Nueva conexión MSSQL en macOS | [#35026](https://github.com/qgis/QGIS/issues/35026) | [PR #39084](https://github.com/qgis/QGIS/pull/39084) | different packaging system\... |
| qgis_process is installed in the wrong place on MacOS | [#38447](https://github.com/qgis/QGIS/issues/38447) | [Mac Packager Commit 97b0ec974e2309e447ebb69c4117580db27af6f0](https://github.com/qgis/QGIS-Mac-Packager/commit/97b0ec974e2309e447ebb69c4117580db27af6f0) | N/D |
| Incapaz de cargar el complemento de GRASS en MacOS | [#32511](https://github.com/qgis/QGIS/issues/32511) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| Processing: GRASS r.drain fails on macOS: \"No module named site\", \"Raster not found\" | [#36126](https://github.com/qgis/QGIS/issues/36126) | [Mac Packager Commit 218a571f6f268dcc4490ebe1a00068bfe363b2ae](https://github.com/qgis/QGIS-Mac-Packager/commit/218a571f6f268dcc4490ebe1a00068bfe363b2ae) | different packaging system\... |
| El cuadro de diálogo de opciones de la caja de herramientas de procesamiento de Grass7 debe incluir una forma de especificar una ruta al binario de GRASS, anulando Grass7Utils.command | [#29454](https://github.com/qgis/QGIS/issues/29454) | No se ejecuta |  |
| Ruta errónea del complemento GRASS en QGIS 3.14 | [#38595](https://github.com/qgis/QGIS/issues/38595) | [PR #38840](https://github.com/qgis/QGIS/pull/38840) | different packaging system\... |
| Sin diálogo de Impresión o Configuración de Página en macOS | [#30791](https://github.com/qgis/QGIS/issues/30791) | No se ejecuta |  |
| Splash Screen Persists While \'Handle Bad Layers\' Dialog is Open | [#34784](https://github.com/qgis/QGIS/issues/34784) | [PR #38842](https://github.com/qgis/QGIS/pull/38842) | no apropiado |
| error al emerger los términos de licencia de qgis | [#38588](https://github.com/qgis/QGIS/issues/38588) | No se ejecuta |  |
| Ya no se pueden cargar imágenes en formularios personalizados | [#30833](https://github.com/qgis/QGIS/issues/30833) | already fixed by [Mac Packager Issue #3](https://github.com/qgis/QGIS-Mac-Packager/issues/3) | no apropiado |
|  | [Mac Packager Issue #83](https://github.com/qgis/QGIS-Mac-Packager/issues/83) | [Mac Packager Commit 36f86759649abc4cb8f6875f6ad934070c13d56e](https://github.com/qgis/QGIS-Mac-Packager/commit/36f86759649abc4cb8f6875f6ad934070c13d56e) | different packaging system\... |
| Proyecciones que no se leen en MacOS Nightly Build | [#38919](https://github.com/qgis/QGIS/issues/38919) | [PR #38922](https://github.com/qgis/QGIS/pull/38922) | different packaging system\... |
| capas en formato .osm no son cargadas | [Mac Packager Issue #84](https://github.com/qgis/QGIS-Mac-Packager/issues/84) | No se ejecuta | funciona en 3.10 |
| Falta el paquete Python de metadatos | [Mac Packager Issue #87](https://github.com/qgis/QGIS-Mac-Packager/issues/87) | [Mac Packager Commit 7c94749579acaf059e9b6c5094c7a2cb74d17f7a](https://github.com/qgis/QGIS-Mac-Packager/commit/7c94749579acaf059e9b6c5094c7a2cb74d17f7a) | different packaging system\... |
| La exportación de GeoPDF falla | [Mac Packager Issue #75](https://github.com/qgis/QGIS-Mac-Packager/issues/75) | funciona ahora con qgis-deps-0.5.5 | different packaging system\... |
| La consola de GRASS no funciona en Mac | [#38961](https://github.com/qgis/QGIS/issues/38961) | [Mac Packager Commit bfc4ca0717de0e496d98f91e7a28e85216763ab1](https://github.com/qgis/QGIS-Mac-Packager/commit/bfc4ca0717de0e496d98f91e7a28e85216763ab1) | different packaging system\... |
| EL complemento de Procesamiento quiebra QGIS en MacOS Nightly Build | [#38960](https://github.com/qgis/QGIS/issues/38960) | [PR #38973](https://github.com/qgis/QGIS/pull/38973) | different packaging system\... |
| El programa quiebra al pegar nombre de archivo | [#38939](https://github.com/qgis/QGIS/issues/38939) | No se ejecuta |  |
| Ruta predeterminada de Python errónea en servidor QGIS en macOS | [#29843](https://github.com/qgis/QGIS/issues/29843) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| qgis_map.fcgi on macOS doesn\'t find libraries | [#29399](https://github.com/qgis/QGIS/issues/29399) | [Mac Packager Commit 1a6ccb6e60adbfbbe05839e0c507e675a71c2491](https://github.com/qgis/QGIS-Mac-Packager/commit/1a6ccb6e60adbfbbe05839e0c507e675a71c2491) | different packaging system\... |
| Proveedor de GRASS no puede obtener proyección | [#31397](https://github.com/qgis/QGIS/issues/31397) | [Mac Packager Commit bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95](https://github.com/qgis/QGIS-Mac-Packager/commit/bfdeab3f5c2ae9465efd1a55a29c0bbc9a88cd95) | different packaging system\... |
| QGIS quiebra al inicio en Mac | [#38858](https://github.com/qgis/QGIS/issues/38858) | perfil de usuario corrupto | N/D |
| El Navegador no puede abrir Volúmenes en macOS | [#29702](https://github.com/qgis/QGIS/issues/29702) | [PR #39096](https://github.com/qgis/QGIS/pull/39096) | no, no crítico |
| MetaSearch unexpected keyword argument \'auth\' | [#38074](https://github.com/qgis/QGIS/issues/38074) | no se puede reproducir en maestro | different packaging system\... |
| No hay complementos encontrados en /Applications/QGIS3.10.app/Contents/MacOS/../PlugIns/qgis | [#39044](https://github.com/qgis/QGIS/issues/39044) | no se puede reproducir en maestro | different packaging system\... |
| Panel Navegador: incapaz de encontrar todas las unidades conectadas | [#24641](https://github.com/qgis/QGIS/issues/24641) | duplicate of [#29702](https://github.com/qgis/QGIS/issues/29702) for MacOS |  |
| Configuración del Proveedor para GRASS evita activar OTB | [#39112](https://github.com/qgis/QGIS/issues/39112) | no se puede reproducir en maestro |  |
| Can\'t open GeoJSON vector via HTTP protocol on Windows and macOS | [#37107](https://github.com/qgis/QGIS/issues/37107) | \"[Mac Packager Commit d06bc3ac933c75071f36937aaf8189920dccc503](https://github.com/qgis/QGIS-Mac-Packager/commit/d06bc3ac933c75071f36937aaf8189920dccc503) | different packaging system\... |
| QGIS 3.0.1 Quiebra - Al hacer Zoom mientras se mueve un nodo quiebra QGIS | [#26509](https://github.com/qgis/QGIS/issues/26509) | No se ejecuta |  |
| Quiebra al conectar perfiles de usuario (¿demasiado pronto?) | [#26993](https://github.com/qgis/QGIS/issues/26993) | No se ejecuta |  |
| Abortado al depurar complemento python con pdb | [#27201](https://github.com/qgis/QGIS/issues/27201) | no se puede reproducir/no válido |  |
| Customization: the widget catcher can\'t select icon from a toolbar when it\'s under a group of icons | [#22967](https://github.com/qgis/QGIS/issues/22967) | [PR #39209](https://github.com/qgis/QGIS/pull/39209) | no crítico |
| QGIS on macOS can save file in qgz-format, but won\'t open files in qgz format | [#39204](https://github.com/qgis/QGIS/issues/39204) | No se ejecuta |  |
| El puntero del mouse sigue cambiando de tipo | [#32947](https://github.com/qgis/QGIS/issues/32947) | probablemente función deseada, no  un error |  |
| Error de función agregar en la versión macOS | \"[#32932](https://github.com/qgis/QGIS/issues/32932) | no se puede reproducir en maestro | different packaging system\... |
| Clear filter in Snapping Toolbar \> Edit advanced configuration causes crash | [#29750](https://github.com/qgis/QGIS/issues/29750) | no se puede reproducir en maestro |  |
| Ventana de ajustes de pinzado con mapas nocturnos, baja legibilidad | [#29751](https://github.com/qgis/QGIS/issues/29751) | ya corregido |  |
| Fusionar ráster falla en macOS | [#39213](https://github.com/qgis/QGIS/issues/39213) | no se puede reproducir en maestro | different packaging system\... |
| Can\'t get info on WFS feature in MacOS nightly build | [#39223](https://github.com/qgis/QGIS/issues/39223) | [Mac Packager Commit 54872e06a43ef61bf6dae8242e121bd5cec8be11](https://github.com/qgis/QGIS-Mac-Packager/commit/54872e06a43ef61bf6dae8242e121bd5cec8be11) | different packaging system\... |
| QGIS 3.4.10 fallos - Python | [#31304](https://github.com/qgis/QGIS/issues/31304) | ya corregido | ya corregido |
| Exporting GRASS vector (save as\...) crashes QGIS | [#37508](https://github.com/qgis/QGIS/issues/37508) | [PR #39284](https://github.com/qgis/QGIS/pull/39284) | PORHACER. |
| Bloqueo al cargar un proyecto 3D con MDE de terreno y símbolos que usan el valor de altura sobre el terreno | [#35483](https://github.com/qgis/QGIS/issues/35483) | [PR #39287](https://github.com/qgis/QGIS/pull/39287) | PORHACER. |
| Crear Vista 3D desde ráster | [#37163](https://github.com/qgis/QGIS/issues/37163) | duplicate of [#35483](https://github.com/qgis/QGIS/issues/35483) | N/D |
| Quiebra al mover cámara en 3D | \"[#37881](https://github.com/qgis/QGIS/issues/37881) | no se puede reproducir en maestro |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Error corregido por Paul Blottiere
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Linebreak issue with editing expression of \"Title Label Decoration\" | [#37803](https://github.com/qgis/QGIS/issues/37803) | [PR #38817](https://github.com/qgis/QGIS/pull/38817) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| QGIS Server GetPrint: EXTERNAL_WMS layer on top of QGIS layer | [#35873](https://github.com/qgis/QGIS/issues/35873) | [PR #38548](https://github.com/qgis/QGIS/pull/38548) | N/D |
| Corrige certificación de OGC API Features | no reportado | [PR #37622](https://github.com/qgis/QGIS/pull/37622) | N/D |
| Outdated help for labels \"data-defined\" placement group options | [#36680](https://github.com/qgis/QGIS/issues/36680) | [PR #37344](https://github.com/qgis/QGIS/pull/37344) |  |
| Server GetFeatureInfo devuelve 0 donde debe devolver NULL | [#37781](https://github.com/qgis/QGIS/issues/37781) | [PR #38807](https://github.com/qgis/QGIS/pull/38807) |  |
| La función z devuelve Nan cuando se usa con una geometría de punto 2d | [#37772](https://github.com/qgis/QGIS/issues/37772) | [PR #38831](https://github.com/qgis/QGIS/pull/38831) |  |
| La función m devuelve Nan cuando se usa con una geometría de punto 2d | no reportado | [PR #38831](https://github.com/qgis/QGIS/pull/38831)/commits/829ee25d431b2b3d1ea08fa8a930bb519ab2dd2f |  |
| processing.algorithmHelp desde terminal (fuera del escritorio QGIS) | [#37524](https://github.com/qgis/QGIS/issues/37524) | No se ejecuta |  |
| Cache join layer in memory\" not toggling when editing join properties | [#37326](https://github.com/qgis/QGIS/issues/37326) | [PR #38838](https://github.com/qgis/QGIS/pull/38838) |  |
| Las sugerencias de mapas no deberían aparecer para entidades invisibles | [#37066](https://github.com/qgis/QGIS/issues/37066) | [PR #38861](https://github.com/qgis/QGIS/pull/38861) |  |
| Funciones de fusión: no se respeta el valor manual | [#37659](https://github.com/qgis/QGIS/issues/37659) | [PR #39083](https://github.com/qgis/QGIS/pull/39083) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Corrección de errores por Matthias Kuhn
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Los nodos de leyenda se superponen entre sí después de insertar | [#38881](https://github.com/qgis/QGIS/issues/38881) | [PR #38882](https://github.com/qgis/QGIS/pull/38882) | no crítico |
| Rendimiento deficiente de la leyenda con leyendas complejas | [#38890](https://github.com/qgis/QGIS/issues/38890) | [PR #38891](https://github.com/qgis/QGIS/pull/38891) | no crítico |
| Las capas AMS no se pueden agregar cuando no se establece ningún SRC del proyecto | [#38892](https://github.com/qgis/QGIS/issues/38892) | [PR #38893](https://github.com/qgis/QGIS/pull/38893) | sin intención |
| Problemas de funcionamiento de la leyenda | [#38978](https://github.com/qgis/QGIS/issues/38978) | [PR #39066](https://github.com/qgis/QGIS/pull/39066) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Matthias Kuhn](https://www.opengis.ch/)
### Error corregido por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| QgsProcessingAlgRunnerTask iniciado dentro de función quiebra QGIS | [#38583](https://github.com/qgis/QGIS/issues/38583) | No se arreglará |  |
| El símbolo del generador de geometría no se representa si la entidad en sí no está en el lienzo del mapa | [#38579](https://github.com/qgis/QGIS/issues/38579) | Retroalimentación |  |
| Widget de relación en las pestañas del formulario de entrada: valor NULL relleno con datos en el formulario | [#38549](https://github.com/qgis/QGIS/issues/38549) | Won't backport (too risky) | (Closed) [#38549](https://github.com/qgis/QGIS/issues/38549) |
| Warning message: Missing layer form dependency : layer \'layerX\' requires layer \'layerY\' to be loaded | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | [PR #38802](https://github.com/qgis/QGIS/pull/38802) | N/D |
| Al incrustar una capa, la expresión de visualización de una relación de referencia no se hace cargo | [#38422](https://github.com/qgis/QGIS/issues/38422) | Cerrado (Solicitud de objeto) |  |
| el atajo de teclado CTRL+C copia solo la primera celda, no toda la línea | [#37503](https://github.com/qgis/QGIS/issues/37503) | [PR #38810](https://github.com/qgis/QGIS/pull/38810) |  |
| si el acceso directo está configurado para las funciones de copia, Ctrl+C ya no funciona | [#37401](https://github.com/qgis/QGIS/issues/37401) | Duplicado #37503 |  |
| Organizar columnas no funciona si la tabla está vacía | [#38653](https://github.com/qgis/QGIS/issues/38653) | Upstream (Qt) |  |
| Copiar y pegar estilo para formularios ignora el tipo de widget de edición | [#37702](https://github.com/qgis/QGIS/issues/37702) | [PR #38836](https://github.com/qgis/QGIS/pull/38836) |  |
| Mantenga el orden al arrastrar y soltar varios widgets | [#37038](https://github.com/qgis/QGIS/issues/37038) | [PR #38844](https://github.com/qgis/QGIS/pull/38844) | [PR #39239](https://github.com/qgis/QGIS/pull/39239) |
| Bloqueo de QGIS al eliminar QgsAnnotation en Python | [#36098](https://github.com/qgis/QGIS/issues/36098) | Retroalimentación |  |
| El error en la declaración SQL para las capas virtuales puede bloquear capas en el lienzo del mapa | [#34378](https://github.com/qgis/QGIS/issues/34378) | [PR #38949](https://github.com/qgis/QGIS/pull/38949) | [PR #39023](https://github.com/qgis/QGIS/pull/39023) |
| No se encontró el campo virtual en la capa virtual | [#38523](https://github.com/qgis/QGIS/issues/38523) | Retroalimentación |  |
| La columna de ID cerrada para la capa temporal no se detecta al crear capas virtuales usando el administrador de fuente de datos | [#34830](https://github.com/qgis/QGIS/issues/34830) | No se arreglará |  |
| Campo virtual booleano inutilizable en capas virtuales | [#31798](https://github.com/qgis/QGIS/issues/31798) | [PR #38957](https://github.com/qgis/QGIS/pull/38957) | [PR #38748](https://github.com/qgis/QGIS/pull/38748) |
| no genera una capa de geometría virtual basada en el campo de trabajo virtual | [#28265](https://github.com/qgis/QGIS/issues/28265) | Retroalimentación |  |
| Closed virtual fields can\'t be filtered | [#28072](https://github.com/qgis/QGIS/issues/28072) | No reproducido |  |
| Qgis craqueado después de eliminar el campo calculado | [#26486](https://github.com/qgis/QGIS/issues/26486) | No reproducido |  |
| sql \"order by\" does not work with the \"Add/Edit Virtual Layer\" feature | [#29043](https://github.com/qgis/QGIS/issues/29043) | No se arreglará |  |
| Form fails to initialize \$geometry | [#34791](https://github.com/qgis/QGIS/issues/34791) | [PR #39041](https://github.com/qgis/QGIS/pull/39041) |  |
| Oracle - can\'t create or a modify a connection | [#38979](https://github.com/qgis/QGIS/issues/38979) | [PR #39131](https://github.com/qgis/QGIS/pull/39131) |  |
| Conexión de prueba lista para Oracle DB - ¡OK en gris! | [#39116](https://github.com/qgis/QGIS/issues/39116) | Duplicado #38979 |  |
| Scale dependent snapping does not activate as long as it displays the scale as \"1:xxxxxx\" | [#39031](https://github.com/qgis/QGIS/issues/39031) | [PR #39133](https://github.com/qgis/QGIS/pull/39133) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Error corregido por Denis Rouzaud
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| correctly determine if variables are static in aggregate expression and filter, give \@parent in generic aggregates | [#33382](https://github.com/qgis/QGIS/issues/33382) | [PR #39391](https://github.com/qgis/QGIS/pull/39391) | no |
| Congelación al usar agregar en un campo virtual | [#39366](https://github.com/qgis/QGIS/issues/39366) | No se arreglará |  |
| Corregir el cálculo del ancla del marcador SVG y mejorar los límites | [PR #39336](https://github.com/qgis/QGIS/pull/39336) |  |  |
| Mejorar SVG IU + borrar código duplicado | [PR #39421](https://github.com/qgis/QGIS/pull/39421) |  |  |
| Mejorar SVG IU + borrar código duplicado | [PR #39519](https://github.com/qgis/QGIS/pull/39519) |  |  |
| Mejorar SVG IU + borrar código duplicado | [PR #39524](https://github.com/qgis/QGIS/pull/39524) |  |  |
| Corregir entidades duplicadas | [PR #39548](https://github.com/qgis/QGIS/pull/39548) |  |  |
| Corregir duplicado de entidad siendo parada a 1 nivel de profundidad | [PR #39550](https://github.com/qgis/QGIS/pull/39550) |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Error corregido por Olivier Dalang
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Problemas del núcleo del solucionador de topología  | no reportado | [PR #39392](https://github.com/qgis/QGIS/pull/39392) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Olivier Dalang](https://www.opengis.ch/)
### Error fijado por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.10 backport commit (GitHub) |
| --- | --- | --- | --- |
| Corregir quiebra en dbmanager | [#38393](https://github.com/qgis/QGIS/issues/38393) | [Commit 8c623b268ed94ef65aa19e2271be10b75e1ef36a](https://github.com/qgis/QGIS/commit/8c623b268ed94ef65aa19e2271be10b75e1ef36a) | N/D |
| Solucionar problemas de tamaño de página de GeoPDF cuando se abre en Acrobat Reader | [#33465](https://github.com/qgis/QGIS/issues/33465) | [Commit 460bf8e534eb32ccba665918a615b55a8cbccadd](https://github.com/qgis/QGIS/commit/460bf8e534eb32ccba665918a615b55a8cbccadd) | Retrasado hasta pruebas de usuario más generalizadas |
| Mejorar la iluminación predeterminada de las escenas 3d | no reportado | [Commit 350bc602e0ecd0f93dc2cc90ab34ce09993a687b](https://github.com/qgis/QGIS/commit/350bc602e0ecd0f93dc2cc90ab34ce09993a687b) | N/D |
| Permitir conversión de resultados de QgsFeatureStoreList a objetos Python | [#39479](https://github.com/qgis/QGIS/issues/39479) | [Commit 49c508921d7ccb59b1f1abaff4f890456cca1455](https://github.com/qgis/QGIS/commit/49c508921d7ccb59b1f1abaff4f890456cca1455) | Demasiado arriesgado |
| Fix preview symbol when offsetting point symbols isn\'t shown correctly | no reportado | [Commit 62409b92ce20a84dd92188cf42a98d7cdc0b08c3](https://github.com/qgis/QGIS/commit/62409b92ce20a84dd92188cf42a98d7cdc0b08c3) | N/D |
| Usar herramientas de comportamiento click-click para rotar y desplazar marcador | no reportado | [Commit 00a3a6b8057f96dfa6c37943427a276cd3a5065d](https://github.com/qgis/QGIS/commit/00a3a6b8057f96dfa6c37943427a276cd3a5065d) | N/D |
| Evitar bloqueos masivos de IU cuando una capa tiene acciones complicadas definidas | no reportado | [Commit 9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668](https://github.com/qgis/QGIS/commit/9aa805c15bb2cf8f9ba33fd2905f5784d6eb4668) | Demasiado arriesgado |
| Asegurar que la expresión de visualización se use para la herramienta de acción del mapa, no los ID de entidades sin procesar | no reportado | [Commit e304d4d7e3eae0f48f336c7eb34542be6055df5d](https://github.com/qgis/QGIS/commit/e304d4d7e3eae0f48f336c7eb34542be6055df5d) | Baja prioridad |
| Mejorar la experiencia de usuario al configurar luces en una escena 3d, corregir la interfaz confusa | no reportado | [Commit 3019b82100d4fc405f64cebcddf9aaae253c4293](https://github.com/qgis/QGIS/commit/3019b82100d4fc405f64cebcddf9aaae253c4293) | N/D |
| Corregir entidades con geometrías inválidas no puede ser seleccionado | [#38460](https://github.com/qgis/QGIS/issues/38460) | [Commit 22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d](https://github.com/qgis/QGIS/commit/22c2c5a41c7ca25cb1fdbb0e121578a2d9386d4d) | N/D |
| Exponer pestaña metadatos para capas de malla | no reportado | [Commit 9482b1be70f36f778f6a409847244c5ff8a6a739](https://github.com/qgis/QGIS/commit/9482b1be70f36f778f6a409847244c5ff8a6a739) | N/D |
| Corregir códigos de texto desaparecidos en instalación Windows | [#36871](https://github.com/qgis/QGIS/issues/36871) | [Commit c3ca85e60bec73056bd87c426fd71c8f578363cb](https://github.com/qgis/QGIS/commit/c3ca85e60bec73056bd87c426fd71c8f578363cb) | Demasiado arriesgado |
| Don\'t force a whole layout map to be rasterised just because one vector layer has non 100% opacity | no reportado | [Commit 2d15a4cfad6c732cf640fbb0eabd625856b643ca](https://github.com/qgis/QGIS/commit/2d15a4cfad6c732cf640fbb0eabd625856b643ca) | Demasiado arriesgado |
| Asegurar que las propiedades de la capa de malla tengan la misma apariencia que otros tipos de capas | no reportado | [Commit 3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac](https://github.com/qgis/QGIS/commit/3c67e1acde24a49bcb0356c2ef5ed6cb8102fdac) | N/D |
| Acelerar el algoritmo de triangulación de malla evitando un montón de desprendimientos innecesarios de QVector | no reportado | [Commit 46ef391a7acf10515a11c19b69fafa4548046448](https://github.com/qgis/QGIS/commit/46ef391a7acf10515a11c19b69fafa4548046448) | N/D |
| Don\'t allow users to set 3d terrain to mesh or DEM without selecting an elevation layer, instead show friendly warning | no reportado | [Commit 0d9f1da846c70764fa6840309b5460f713b30e1f](https://github.com/qgis/QGIS/commit/0d9f1da846c70764fa6840309b5460f713b30e1f) | N/D |
| Evitar la apertura del cuadro de diálogo de configuración del mapa 3D con el panel seleccionado inicialmente fuera de sincronización | no reportado | [Commit 8b6477208f3c34e228734f7c04d32625965c48ed](https://github.com/qgis/QGIS/commit/8b6477208f3c34e228734f7c04d32625965c48ed) | N/D |
| Fix menu not shown when clicking \'add\' item in style manager dialog and color ramp tab is active | no reportado | [Commit a085ce84b81a46896c9f00ee64eccaea63dad29a](https://github.com/qgis/QGIS/commit/a085ce84b81a46896c9f00ee64eccaea63dad29a) | N/D |
| Corregir intentar crear una nueva rampa de color desde la primera página en el cuadro de diálogo del administrador de estilo. | no reportado | [Commit 34fb646f7ab69f20072b4d74ebec0595054089d7](https://github.com/qgis/QGIS/commit/34fb646f7ab69f20072b4d74ebec0595054089d7) | N/D |
| \[processing\] Fix generated layers stored in geopackage always report a feature count of 0 | no reportado | [Commit 0675d99b34ee209a09857dfcba47cb5a92f55154](https://github.com/qgis/QGIS/commit/0675d99b34ee209a09857dfcba47cb5a92f55154) | Demasiado arriesgado |
| El algoritmo Fix Import Geotagged photos asigna incorrectamente widgets de formulario al guardar los resultados en GPKG | no reportado | [Commit ff336ade18f4d6b307e4ed0e98fee77ee11a157c](https://github.com/qgis/QGIS/commit/ff336ade18f4d6b307e4ed0e98fee77ee11a157c) | [PR #39563](https://github.com/qgis/QGIS/pull/39563) |
| \[processing\] Ensure driverName is passed to QgsVectorLayerExporter so that GPKG specific optimisations can be applied when saving outputs to geopackage | no reportado | [Commit 501c63feb3887e18da35188062546186d8a767ac](https://github.com/qgis/QGIS/commit/501c63feb3887e18da35188062546186d8a767ac) | Demasiado arriesgado |
| Actualizar las cadenas y la interfaz de usuario con respecto a la configuración de suplantación de SRC de capa | [#32101](https://github.com/qgis/QGIS/issues/32101) | [Commit 06cfdd9563b15d8fbb27aee94b83d1b15773df77](https://github.com/qgis/QGIS/commit/06cfdd9563b15d8fbb27aee94b83d1b15773df77) | N/D |
| Use proper SQL code editor in filter preview widget in vector layer properties, don\'t show filter as disabled | no reportado | [Commit 0f4270cfe600e77f09db7727bd3ba965be7acb0e](https://github.com/qgis/QGIS/commit/0f4270cfe600e77f09db7727bd3ba965be7acb0e) | N/D |
| Corregir la presentación literal booleana en dox/PyQGIS docs | no reportado | [Commit 746ee315bd0a4140f6e84617d547cc89103f79aa](https://github.com/qgis/QGIS/commit/746ee315bd0a4140f6e84617d547cc89103f79aa) | N/D |
| Acelerar la validación de la geometría de QGIS | no reportado | [Commit 2a15c3b0a4a631db1b55ac7e46256fdbd89949f9](https://github.com/qgis/QGIS/commit/2a15c3b0a4a631db1b55ac7e46256fdbd89949f9) | Demasiado arriesgado |
| \[processing\] Correctly discard fid field values when running algorithms with the RegeneratePrimaryKey flag in in-place mode | [#37761](https://github.com/qgis/QGIS/issues/37761), [#33816](https://github.com/qgis/QGIS/issues/33816) | [Commit db7b97705967041d4eaca7e7f69cbf49f5692aef](https://github.com/qgis/QGIS/commit/db7b97705967041d4eaca7e7f69cbf49f5692aef) | Demasiado arriesgado |
| \[processing\] When reporting that a feature is invalid, also mention the layer name | [#26664](https://github.com/qgis/QGIS/issues/26664) | [Commit a53bb3d49b59a3f814d862f30202ff156f74d6bc](https://github.com/qgis/QGIS/commit/a53bb3d49b59a3f814d862f30202ff156f74d6bc) | Demasiado arriesgado |
| Permitir expandir archivos xls, ods, gpx, pdf en el navegador para que las fuentes de capa se puedan reparar para estos tipos de archivos | no reportado | [Commit 252976b739527e213f5d1c8c98a345911dfeab32](https://github.com/qgis/QGIS/commit/252976b739527e213f5d1c8c98a345911dfeab32) | N/D |
| \[processing\] Fix \"Split with lines\" algorithm can get stuck in an endless loop | no reportado | [Commit 05645b320d8547f50a308843e961e343c383036d](https://github.com/qgis/QGIS/commit/05645b320d8547f50a308843e961e343c383036d) | Demasiado arriesgado |
| Don\'t show cascaded feature deletion warnings and feedback if joined deleted features came from an auxilary layer | no reportado | [Commit 8c79b94fcc14e41d4442a018554e889f81b8e080](https://github.com/qgis/QGIS/commit/8c79b94fcc14e41d4442a018554e889f81b8e080) | N/D |
| Se corrigió el bloqueo en el dock de deshacer al borrar el proyecto/cerrar QGIS | [#38157](https://github.com/qgis/QGIS/issues/38157) | [Commit d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8](https://github.com/qgis/QGIS/commit/d87d230bb4bcbe091fe35bb047d54f7d9fcaabb8) | [Commit 5c97ff66dd90d450a1ec60583da9626c14c9c08c](https://github.com/qgis/QGIS/commit/5c97ff66dd90d450a1ec60583da9626c14c9c08c) |
| Fix copy/paste/select all shortcuts don\'t work when layer tree is selected | [#38849](https://github.com/qgis/QGIS/issues/38849) | [Commit 02d7afae3f8699e83efacc781d3266700397d8b8](https://github.com/qgis/QGIS/commit/02d7afae3f8699e83efacc781d3266700397d8b8) | N/D |
| Las funciones nuevas y editadas ya no muestran correctamente su sombreado de color correspondiente en la vista de lista de funciones | no reportado | [Commit a195b056624c2fabe231be7c0e96c3d63e052e5b](https://github.com/qgis/QGIS/commit/a195b056624c2fabe231be7c0e96c3d63e052e5b) | Demasiado arriesgado/baja prioridad |
| ALWAYS load processing plugin in qgis_process tool | [#37989](https://github.com/qgis/QGIS/issues/37989) | [Commit bc0df6d25e929a575d0821208f7d187737d80709](https://github.com/qgis/QGIS/commit/bc0df6d25e929a575d0821208f7d187737d80709) | N/D |
| Add \--json option to qgis_process tool | <https://github.com/paleolimbot/qgisprocess/issues/21> | [Commit fc8d916b8dd444b3edaee3c18ec308e74a9bb91e](https://github.com/qgis/QGIS/commit/fc8d916b8dd444b3edaee3c18ec308e74a9bb91e) | N/D |
| Asegúrese de que todos los editores de código en QGIS sigan la misma apariencia y comportamiento | no reportado | (mucho) | N/D |
| Al crear un SRC a partir de WKT y el WKT tiene un nombre de SRC incrustado, utilícelo correctamente para configurar la descripción de QgsCoordinateReferenceSystem | no reportado | [Commit 9a35b27630982d63101c57c3e3440dcbf1a7786f](https://github.com/qgis/QGIS/commit/9a35b27630982d63101c57c3e3440dcbf1a7786f) | Posible después de más pruebas de usuario |
| Gran velocidad para scripts que disparan muchas solicitudes de funciones individuales a una capa de proveedor de memoria | no reportado | [Commit 1d2bb41752c51e6c9b84124a1ce1599d3d42b41c](https://github.com/qgis/QGIS/commit/1d2bb41752c51e6c9b84124a1ce1599d3d42b41c) | Demasiado arriesgado |
| \[console\] Fix exception when running scripts | no reportado | [Commit 5c8013df6129a2bc06d25a98ff20dbf27621bff5](https://github.com/qgis/QGIS/commit/5c8013df6129a2bc06d25a98ff20dbf27621bff5) | N/D |
| \[layouts\] Fix resizing multiline label items to adjust to the size of their text | no reportado | [Commit 6829e6351e1dab18f1fa0c0443107eb7617794c7](https://github.com/qgis/QGIS/commit/6829e6351e1dab18f1fa0c0443107eb7617794c7) | Demasiado arriesgado |
| Mejorar la apariencia de la documentación de PyQGIS para funciones que devuelven múltiples valores | no reportado | [Commit 0001ec27a43cbf4c99d1525c3c5f75183e96f5c3](https://github.com/qgis/QGIS/commit/0001ec27a43cbf4c99d1525c3c5f75183e96f5c3) | N/D |
| \[processing\] Don\'t raise a generic \"something went wrong\" exception when calling processing.run(), instead use proper descriptive exception | no reportado | [Commit 2207c30a247e5907a12185165b4bd220e255bbdc](https://github.com/qgis/QGIS/commit/2207c30a247e5907a12185165b4bd220e255bbdc) | Demasiado arriesgado |
| \[processing\] Fix execution of \"Eliminate selection\" through Python | [#38808](https://github.com/qgis/QGIS/issues/38808) | [Commit ee7bea2305253fd276a69c25bb5d308942dcb190](https://github.com/qgis/QGIS/commit/ee7bea2305253fd276a69c25bb5d308942dcb190) | Demasiado arriesgado |
| \[3d\] Fix crash when line feature cannot be buffered | no reportado | [Commit f6eed85729a8cbf913155ae16df7499f688ba0fa](https://github.com/qgis/QGIS/commit/f6eed85729a8cbf913155ae16df7499f688ba0fa) | [Commit d4c963e1c2fdc497dba038896caf2b3f975240ff](https://github.com/qgis/QGIS/commit/d4c963e1c2fdc497dba038896caf2b3f975240ff) |
| Corregir los patrones de trazo personalizados escalan incorrectamente cuando se establece el ancho de trazo definido por datos | [#39201](https://github.com/qgis/QGIS/issues/39201) | [Commit 03fdc0cd7992a7883183704cd68506f32afe9ca3](https://github.com/qgis/QGIS/commit/03fdc0cd7992a7883183704cd68506f32afe9ca3) | Demasiado arriesgado |
| Permitir cambiar el tamaño de las columnas en la tabla de transformación de datum | [#39169](https://github.com/qgis/QGIS/issues/39169) | [Commit 1cd5a3358b235f67b6b4d95331ce561e9f8cb715](https://github.com/qgis/QGIS/commit/1cd5a3358b235f67b6b4d95331ce561e9f8cb715) | N/D |
| La configuración de corrección se muestra incorrectamente para tipos de capa incorrectos en el cuadro de diálogo de etiquetado | [#39168](https://github.com/qgis/QGIS/issues/39168) | [Commit 2e948884c029c9f79639201943ec4bc36dba3573](https://github.com/qgis/QGIS/commit/2e948884c029c9f79639201943ec4bc36dba3573) | N/D |
| \[processing\] Fix error reporting from batch dialog | [#39197](https://github.com/qgis/QGIS/issues/39197) | [Commit 5243a8594cc39540f2c01201415633801a22ff43](https://github.com/qgis/QGIS/commit/5243a8594cc39540f2c01201415633801a22ff43) | N/D |
| \[processing\] Fix crash when renaming conditional branch in modeler | [#39053](https://github.com/qgis/QGIS/issues/39053) | [Commit ddae53b7b789467bf17b21d6f4b884e827fbd3c5](https://github.com/qgis/QGIS/commit/ddae53b7b789467bf17b21d6f4b884e827fbd3c5) | N/D |
| \[processing\] Fix crash in model designer when a child algorithm contains hidden parameters | no reportado | [Commit f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0](https://github.com/qgis/QGIS/commit/f3c9f9bfbc2fc456c77965be4c1e65cc692bc0d0) | N/D |
| Asegúrese de que True/False se traten como palabras clave de Python en el editor de código de Python | no reportado | [Commit 5f661045c078b7938550c2c9d0798664c6f65f5a](https://github.com/qgis/QGIS/commit/5f661045c078b7938550c2c9d0798664c6f65f5a) | N/D |
| Don\'t silently close QGIS with unsaved changes in the console script editors | [#38529](https://github.com/qgis/QGIS/issues/38529) | [Commit 9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9](https://github.com/qgis/QGIS/commit/9093bdfd1e46ba65af78c5fc01bcb4df1ed6a0e9) | Demasiado arriesgado |
| Corregir la caída del archivo .py del algoritmo de secuencia de comandos de procesamiento en QGIS ya no activa el algoritmo para ejecutar | no reportado | [Commit 64bf347d7e1d664fc674c5ca602ce6c4bedecdf9](https://github.com/qgis/QGIS/commit/64bf347d7e1d664fc674c5ca602ce6c4bedecdf9) | N/D |
| Arreglar el muelle de registro de mensajes causa estragos con otros muelles ubicados en la misma área | [#31955](https://github.com/qgis/QGIS/issues/31955) | [Commit 384f6a1d9257a05eaa58942921c94f1dd4941cd3](https://github.com/qgis/QGIS/commit/384f6a1d9257a05eaa58942921c94f1dd4941cd3) | Demasiado arriesgado |
| When restoring a custom CRS from XML, if the CRS does NOT match any of the existing user defined CRS\'s on the QGIS profile then still restore the previously saved name of the custom CRS | no reportado | [Commit e6d316ace7031821e04ca625e35f7c2c4d57f639](https://github.com/qgis/QGIS/commit/e6d316ace7031821e04ca625e35f7c2c4d57f639) | Posible después de más pruebas de usuario |
| Don\'t refer to valid but custom CRSes as \"Unknown CRS\" and instead use \"Custom CRS\" phrasing | no reportado | [Commit d3833fd8d6c4b4f0673c4c2337044c224675185f](https://github.com/qgis/QGIS/commit/d3833fd8d6c4b4f0673c4c2337044c224675185f) | Posible después de más pruebas de usuario |
| Mejorar el rendimiento del diálogo de proceso de procesamiento por lotes con una gran cantidad de archivos | [#38987](https://github.com/qgis/QGIS/issues/38987) | [Commit 776768eb9f4ee2a8d13909b4ced5c175a0d05b3d](https://github.com/qgis/QGIS/commit/776768eb9f4ee2a8d13909b4ced5c175a0d05b3d) | Demasiado arriesgado |
| Mejorar el comportamiento de los widgets de transformación y selector de SRC | no reportado | mucho | N/D |
| \[layouts\] Use standard CRS selector widget for map grid CRS choice | [#26548](https://github.com/qgis/QGIS/issues/26548) | [Commit 4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70](https://github.com/qgis/QGIS/commit/4c7fbc0260ef95f7dd6dd4b6954ee2086ad3da70) | Demasiado arriesgado |
| \[layouts\] When selecting a CRS for a map item, don\'t show misleading no crs option at the top of the dialog | no reportado | [Commit c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad](https://github.com/qgis/QGIS/commit/c3a26db4babbef46ae1b7904bb9d1f0ee9e273ad) | Demasiado arriesgado |
| Fix \"layer has no CRS\" message incorrectly show at the top of many projection selection dialog boxes | no reportado | [Commit c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c](https://github.com/qgis/QGIS/commit/c68d05cc40f8f2c828e5204e6e4f5f11e68b4a7c) | Demasiado arriesgado |
| Solucionar el bloqueo al editar el estilo y abrir un proyecto | [#38920](https://github.com/qgis/QGIS/issues/38920) | [Commit 67ec244864ca6f9290e1f35a1a0c60b4888fe686](https://github.com/qgis/QGIS/commit/67ec244864ca6f9290e1f35a1a0c60b4888fe686) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/ecf96231aefa5628539f0b63ca313ea8b20c9548 |
| Evitar la advertencia qt al arrastrar un objeto que no es de color sobre los botones de color | no reportado | [Commit fd771bba68da84b1ce8023898b9662b5dc619693](https://github.com/qgis/QGIS/commit/fd771bba68da84b1ce8023898b9662b5dc619693) | N/D |
| Corregir el cambio en las posiciones de los objetos de geopdf cuando se usa SRC geográfico a gran escala | [#37755](https://github.com/qgis/QGIS/issues/37755) | [Commit 0b77f187ec5a14651457fd07f306cba2511fb854](https://github.com/qgis/QGIS/commit/0b77f187ec5a14651457fd07f306cba2511fb854) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/b705d29c73e81fe87e2e301c7028e5e659d80364 |
| Los metadatos de restricción de corrección se duplican después de abrir las propiedades de la capa | [#38916](https://github.com/qgis/QGIS/issues/38916) | [Commit 6a002573c00a8a8e11443eaca28b57a8ad6de4c0](https://github.com/qgis/QGIS/commit/6a002573c00a8a8e11443eaca28b57a8ad6de4c0) | [PR #38748](https://github.com/qgis/QGIS/pull/38748)/commits/49260b8f1f4b1ddd9a25c7160f32570221f3989e |
| Corregir la exportación de PDF incluye información vectorial fuera del área de interés | [#38878](https://github.com/qgis/QGIS/issues/38878) | [Commit f3f226aa69a19b31dd8a1b83c82319528e061cfe](https://github.com/qgis/QGIS/commit/f3f226aa69a19b31dd8a1b83c82319528e061cfe) | Demasiado arriesgado |
| \[layouts\] Fix legend symbol rendering doesn\'t respect linked map scale when symbol uses map unit based sizes | [#38326](https://github.com/qgis/QGIS/issues/38326) | [Commit 426ee2120b33a8613f3e476da3c2eba0a00f65d7](https://github.com/qgis/QGIS/commit/426ee2120b33a8613f3e476da3c2eba0a00f65d7) | N/D |
| Don\'t try to write empty rendered rings/geometries to GeoPDF outputs | no reportado | [Commit 96753cfd1b9e986841158675bda365e585c48c27](https://github.com/qgis/QGIS/commit/96753cfd1b9e986841158675bda365e585c48c27) | Posible después de más pruebas de usuario |
| Aplicar correctamente la configuración de mayúsculas siempre que se use QgsTextRenderer, no solo en el etiquetado | [#38898](https://github.com/qgis/QGIS/issues/38898) | [Commit e1ca83b2c24c51e7ff67a53278ffd2601c0459be](https://github.com/qgis/QGIS/commit/e1ca83b2c24c51e7ff67a53278ffd2601c0459be) | Demasiado arriesgado |
| Fix qgis_process list raises exception if processing algorithm provider is activated | [#38862](https://github.com/qgis/QGIS/issues/38862) | [Commit 772181bc16820d7dd5ee8d967355dbdfde5a8efe](https://github.com/qgis/QGIS/commit/772181bc16820d7dd5ee8d967355dbdfde5a8efe) | N/D |
| Aceleración dramática para llamar a algunos métodos de uso frecuente desde PyQGIS | no reportado | [Commit d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca](https://github.com/qgis/QGIS/commit/d4a2dddac5a2fd4fcf901cc3d50f70a6119ca1ca) | Demasiado arriesgado |
| \[processing\] Fix certain characters show as HTML escaped in processing log | [#37934](https://github.com/qgis/QGIS/issues/37934) | [Commit 965595d25bd0a69875ba8a405d3b365bedfe2a12](https://github.com/qgis/QGIS/commit/965595d25bd0a69875ba8a405d3b365bedfe2a12) | N/D |
| Se corrigió el uso incorrecto de mayúsculas en el título del cuadro de diálogo del nombre del nuevo diseño | no reportado | [Commit 92d0ec59a1c26c4ac33d35b9e6c93344845eddca](https://github.com/qgis/QGIS/commit/92d0ec59a1c26c4ac33d35b9e6c93344845eddca) | N/D |
| Add a new capitalization option for \"Title Case\", and rename the confusing \"Capitalize First Letter\" option to Force First Letter to Capital | [#16539](https://github.com/qgis/QGIS/issues/16539) | [Commit 484ba6f979cdcaabffe823c72b35b57d1b1c7aad](https://github.com/qgis/QGIS/commit/484ba6f979cdcaabffe823c72b35b57d1b1c7aad) | N/D |
| Agregue una categoría de leyenda a los widgets de selección de estilo y permita que la configuración de la leyenda se almacene y restaure en QML | [#37683](https://github.com/qgis/QGIS/issues/37683) | [Commit f018252023275f95c167d7f308d05c8819d6db0b](https://github.com/qgis/QGIS/commit/f018252023275f95c167d7f308d05c8819d6db0b) | Demasiado arriesgado |
| Fix \[Style\] Export \--\> Save as QGIS Layer style File should allow to select style categories (and output format) | [#29145](https://github.com/qgis/QGIS/issues/29145) | [Commit 1ad2e78735e57cef218a7470d7eec645c2f45263](https://github.com/qgis/QGIS/commit/1ad2e78735e57cef218a7470d7eec645c2f45263) | Demasiado arriesgado |
| \[browser\] Correctly save expanded node state when closing QGIS | no reportado | [Commit 2eff061bf3cdcb3f36956e43098adfcb0359b5eb](https://github.com/qgis/QGIS/commit/2eff061bf3cdcb3f36956e43098adfcb0359b5eb) | Demasiado arriesgado |
| \[browser\] Gpkg and other container types can be dragged to the map to allow layers to be added from them | no reportado | [Commit 0234d4e9e10f3fbb5732f66e00eebd038f502ab0](https://github.com/qgis/QGIS/commit/0234d4e9e10f3fbb5732f66e00eebd038f502ab0) | Demasiado arriesgado |
| Don\'t prompt for CRS for annotation layers | [#38739](https://github.com/qgis/QGIS/issues/38739) | [Commit 15975c1d5191933311d81a494d87806f4e73ce57](https://github.com/qgis/QGIS/commit/15975c1d5191933311d81a494d87806f4e73ce57) | N/D |
| Fix reading saved color map file when an item\'s label contains a comma character | [#24112](https://github.com/qgis/QGIS/issues/24112) | [Commit 252149375c750d6a8f1ee281c1cc9d03de272170](https://github.com/qgis/QGIS/commit/252149375c750d6a8f1ee281c1cc9d03de272170) | Demasiado arriesgado |
| Corregir que la configuración del diagrama no se restaura correctamente al cargar un archivo QML | [#35343](https://github.com/qgis/QGIS/issues/35343) | [Commit 4668927ce432b198b3c572535ff234343c5042f5](https://github.com/qgis/QGIS/commit/4668927ce432b198b3c572535ff234343c5042f5) | Demasiado arriesgado |
| Corregir ya no puede pegar colores de cadenas de texto | no reportado | [PR #39561](https://github.com/qgis/QGIS/pull/39561) | N/D |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
