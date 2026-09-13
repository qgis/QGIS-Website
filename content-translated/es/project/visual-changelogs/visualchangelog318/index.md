---
HasBanner: false
draft: false
releaseDate: '2021-02-19'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.18
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.18{#changelog318 }
![image1](images/projects/606afcefcc3f5fd4ff00db9b4cb04b22485044db.png)

Fecha de lanzamiento: 2021-02-19

Following on from the feature-filled releases of [QGIS 3.14](https://qgis.org/en/site/forusers/visualchangelog314/) and [QGIS 3.16](https://qgis.org/en/site/forusers/visualchangelog316/), QGIS 3.18 introduces a host of enhancements and new features, along with a long-awaited feature - Native Point Cloud support in QGIS! Thanks to the efforts of [Lutra](https://www.lutraconsulting.co.uk/), [North Road](https://north-road.com/), and [Hobu](https://hobu.co/), QGIS is now able to import and render point cloud data in various formats by leveraging the Open Source PDAL library. This functionality has been introduced due to the success of a [crowd-funding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/) and would not have been possible without the support of the QGIS community and contributors. Thank you to all those involved in realizing this incredible milestone!

Mientras QGIS Desktop 3.18 se despide del proveedor de bases de datos DB2, introduce la compatibilidad con los usuarios del sistema de bases de datos SAP HANA.

The QGIS ecosystem has also seen some exciting changes in the form of the [QGIS HUB](https://plugins.qgis.org/) which is an extension of the plugin site which now supports the distribution of community developed [styles](https://plugins.qgis.org/styles/), [projects](https://plugins.qgis.org/geopackages/), and even [processing models](https://plugins.qgis.org/models/).

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/Yeo6sXVpXvA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS es Software Libre y no estás obligado a pagar nada por utilizarlo - de hecho queremos motivar a personas de todos lados independientemente de cuál sea tu estatus social o económico - creemos que empoderar a las personas con herramientas espaciales para la toma de decisiones resultará en una mejor sociedad para toda la humanidad.

{{<table-of-contents >}}
## Interfaz de usuario
### Prestación: Ocultar los atributos derivados de los resultados Identificar
Anteriormente, la utilidad *Identificar* de QGIS Desktop exponía un gran número de atributos derivados, como la información sobre la geometría. Aunque es increíblemente valiosa, para muchos casos de uso esta información es verbosa. Los usuarios tendrán ahora la opción de alternar la visualización de los atributos derivados para crear una vista más concisa de los resultados de la identificación.

![image2](images/entries/96178054-1aa78d80-0f2f-11eb-8d75-299bfd6aa73e.webp)

![image3](images/entries/c9eea14d2c01670795967bd1e42fcb8777330718.webp)

This feature was developed by [Richard Duivenvoorde](https://api.github.com/users/rduivenvoorde)
### Prestación: Cierre de todas las pestañas a la vez desde la interfaz de los registros de mensajes
The QgsMessageLogViewer now includes an **\"Empty tab and close others\"** to the log viewer panel context menu, supporting a quicker action to a clean interface when debugging.

![image4](images/entries/5adbd9ce0bfeb73ec308ed003603aacceab728d4.webp)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Prestación: API para widgets de origen de capas
An API has been added in the provider GUI to allow a provider to create a custom widget, which exposes options to customize and change the layer\'s source. For example, a file-based layer provider could expose a widget for selecting a new file path, or an online provider could expose widgets for changing the host or authentication information.

Dos implementaciones han sido añadidas para esto:
1. Un widget de selección de archivos para las capas basadas en archivos GDAL.
2. Un widget para personalizar las propiedades de la capa XYZ.

![image5](images/entries/24c8af6d1314e7a22f8f70a7628f3aeae9b3ce1a-1.webp)

![image6](images/entries/14df1b85a3e3ada3024a39499a245bbdd7e2ca64-1.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: GUI para SVGs dinámicas
QGIS now supports dynamic standard vector graphic elements, as outlined in [QEP #199](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/199). This allows QGIS to dynamically replace attributes or node values in the XML of the SVG and apply data-driven values to SVG elements. QGIS Desktop has additionally added a GUI editor to ensure that users are able to properly leverage this new functionality.

![image7](images/entries/c6d55ffc6be5f0e4962d9b971cac6e54ab316717.webp)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Prestación: Acercamiento a múltiples capas
The \"Zoom to Layer\" function available from the context menu, the View menu and the Map Navigation toolbar can now zoom to the extent of all the selected layers in the layer tree.

![image8](images/entries/101234295-f1cc8a80-368b-11eb-9b52-8f42a4f994a2.gif)

This feature was developed by [Patrice Pineault](https://api.github.com/users/TurboGraphxBeige)
### Prestación: Acercamiento y desplazamiento a una selección de múltiples capas
The \"Zoom to Selection\" and \"Pan Map to Selection\" functions available from the context menu, the View menu or the Map Navigation toolbox now offer the ability to navigate to the extent of the selection from the selected layers in the layer tree.

![image9](images/entries/a76fca5cfc367779584da0655cd18474e4518329-1.gif)

This feature was developed by [Patrice Pineault](https://api.github.com/users/TurboGraphxBeige)
### Prestación: Acercamiento/alejamiento mediante el desplazamiento de la rueda del ratón sobre el panel de visión general del mapa
Ahora los usuarios pueden acercarse y alejarse desde el panel de vista general del mapa utilizando el desplazamiento del ratón.

![image10](images/entries/77b55b4c85c9c4f5076b1a735f7971819cc2a2ee.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Accesibilidad
### Prestación: Simulación mejorada de deficiencia de visión color
Esto modifica el soporte anterior para la simulación en escala de grises y basada en LMS para la protanopía y la deuteranopía, alineándolo con la metodología utilizada actualmente en Chromium y Firefox. QGIS utiliza ahora cálculos actualizados de luminancia en escala de grises (rebautizados como acromatopsia), una matriz de protanopía precalculada (rebautizada como protanope), una matriz de deuteranopía precalculada (rebautizada como deuteranope) y un modo adicional para la tritanopía que utiliza una matriz precalculada similar.

This feature was developed by [Will Cohen](https://api.github.com/users/willcohen)
### Prestación: Widget de rotación para el georreferenciador
El lienzo del georreferenciador puede ahora girarse para facilitar la colocación de los puntos de referencia. Esto es especialmente útil para las imágenes escaneadas que pueden no tener orientaciones uniformes.

![image11](images/entries/aba35ba4bb5ff0f2a8c1afcb55673e496efea18a.gif)

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
## Simbología
### Prestación: Opacidad general de símbolo definida por datos
Mientras que antes era posible establecer la opacidad de los colores individuales de las capas de símbolos mediante expresiones definidas por datos, ahora es posible establecer una expresión definida por datos para controlar la opacidad general de los símbolos.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Abrir la galería de estilos desde el gestor de estilos
The Style Manager interface now includes a button to open the [styles gallery](https://plugins.qgis.org/styles/) from the QGIS HUB.

![image12](images/entries/0d6dd72f8089ee52196001751451d42c7107fbe8.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Malla
### Prestación: Nuevos algoritmos de exportación de mallas
Se han añadido nuevas opciones de exportación para las capas de malla. Estas permiten las siguientes opciones al exportar una malla a una capa vectorial:
- Exportas caras
- Exportar bordes (malla 1D)
- Exportar como grid

![image13](images/entries/4738ffe8180f8fc320cf464121ec10fc27bd4c33.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
### Prestación: Exportación nativa para capas malla
Las versiones anteriores de QGIS requerían la utilización del complemento crayfish, sin embargo, esta funcionalidad se ha incorporado ahora al núcleo de QGIS y permite a los usuarios exportar capas de malla a vectores y añadir el valor del conjunto de datos como un atributo.

![image14](images/entries/41bdfc3d3c6afabc0e3e23986e42dbc22eb794df.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
### Prestación: Simplificación malla para 3D
Los datos mallas pueden ahora simplificarse definiendo un nivel de detalle para la representación 3D. Esto ayuda al rendimiento de los conjuntos de datos complejos y garantiza una experiencia más fluida cuando se requiere la navegación en 3D.

![image15](images/entries/6461d329ef7d4936ddbc932b0bf96edcb071b398.gif)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
### Prestación: Múltiples algoritmos de procesamiento nativo malla
Se han portado varios algoritmos de procesamiento nuevos desde el complemento crayfish, entre ellos:
- Rasterizar capa malla
- Exportar contorno a capas vector
- Exportar sección transversal a archivo texto (csv)
- Exportar series de tiempo a archivo texto (csv)

![image16](images/entries/3acf2cfe05dc7550f16e183026350914d028a6da.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
## Representación
### Feature: \"Merged feature\" renderer for polygon and line layers
A new rendering option allows area and line features to be \"dissolved\" into a single object prior to rendering to ensure that complex symbols or overlapping features are represented by a uniform and contiguous cartographic symbol.

![image17](images/entries/4f1a29b4c0552c362d0bd87f3034af0ef07b642c.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Redibujado Más Inteligente de Mapa
Previously, map redraws would attempt to redraw all elements in the frame. The map rendering has been significantly improved and now the existing map frame elements are used during the redraw process. This work was completed as a part of [QEP #181](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/181) and was funded by the QGIS Grant program for 2020.

La siguiente pantalla muestra el comportamiento del redibujado antes de la mejora:

![image18](images/entries/7d0a503ab9ae05427e42e2987335ef569c761a3e-1.gif)

This feature was funded by [QGIS grant 2020](https://qgis.org/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
## Objetos 3D
### Prestación: Iluminación de la cúpula del ojo
La iluminación de cúpula (EDL) es un efecto de posprocesamiento que compara la profundidad de cada píxel (distancia desde la cámara) con las profundidades de los píxeles vecinos y resalta los bordes según las diferencias calculadas.

Se ha añadido un elemento de configuración EDL a la pestaña de ajustes avanzados del diálogo de configuración de la vista 3D. La intensidad de la EDL tiene el efecto de aumentar el contraste, lo que permite una mejor percepción de la profundidad (que puede ser necesario ajustar al hacer zoom). La distancia EDL es la distancia de los píxeles utilizados desde el píxel central y tiene el efecto de hacer los bordes más gruesos.

The eye dome lighting is, by principle, an image-based rendering solution similar to SSAO (screen space ambient occlusion), and therefore works on the whole scene and doesn\'t differ between point clouds or regular 3D objects.

![image19](images/entries/4e7b365e9e991bf06f15a3ad15ff50a0ac9692e2.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](https://www.lutraconsulting.co.uk)
### Prestación: Colores material 3D definidos por datos
Los colores de los materiales 3D ahora pueden ser definidos por los datos, permitiendo que los colores de las características sean determinados usando el valor de un atributo o expresión.

La representación de los polígonos puede realizarse actualmente con múltiples tipos de materiales, cada uno de los cuales tiene una apariencia y una configuración de colores distinta:
- Material realista (Phong) - calculado usando 3 colores (difuso, ambiente, especular), que utiliza la configuración de iluminación de la vista 3D
- Material CAD (Gooch) - calculado usando 4 colores (difuso, cálido, frío, especular), que ignora la configuración de iluminación de la vista 3D

Los materiales con textura no son compatibles en este momento.

![image20](images/entries/97449982-9da1ee00-1908-11eb-9276-32c863c3f6e1.webp)

![image21](images/entries/504010202dcff6a9b78450fedfa493b6e726b5c0.webp)

This feature was funded by [Kristianstad](https://www.kristianstad.se)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Prestación: Apoyo a la proyección ortográfica en 3D
QGIS ofrece ahora soporte de proyección ortográfica para escenas 3D, una característica a menudo deseada en el contexto de la arquitectura, la arqueología, etc.

![image22](images/entries/7e43323cea578f6f50e83de6307c22bdef948f8d.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Nubes de Puntos
### Prestación: Soporte de nubes de puntos
Following the successful [crowdfunding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/) for point cloud support in QGIS, the engineers at Lutra, North Road, and Hobu have been able to introduce the ability for QGIS to import and render point cloud data.

Esto incluye la posibilidad de añadir capas de nubes de puntos a los proyectos de QGIS, con soporte para el formato EPT, y representarlas en contextos 2D y 3D.

![image23](images/entries/3d87d5647d363b53b1a19ffd67de7406632df572.webp)

This feature was funded by [Point Cloud data support in QGIS](https://www.lutraconsulting.co.uk/blog/2021/02/18/qgis-3-18-point-cloud/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk)
### Prestación: Añadir nubes de punto a navegador
El Explorador QGIS y la interfaz de gestión de fuentes de datos ahora soportan la estructura básica de las capas de nubes de puntos compatibles con PDAL.

![image24](images/entries/96aca5c2d2f428f0aa7fee0d11b5c8600c5c523c.webp)

This feature was funded by [Point Cloud data support in QGIS crowd funding campaign](https://www.lutraconsulting.co.uk/blog/2021/02/18/qgis-3-18-point-cloud/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Prestación: Integración del proveedor de PDAL de Untwine
Ability to generate EPT index for (smaller) laz files directly in QGIS via the [untwine](https://github.com/hobu/untwine) library

This feature was funded by [Point Cloud data support in QGIS crowd funding campaign](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk)
## Diseño de impresión
### Prestación: Leyendas basadas en rampa gradiente
A new QgsColorRampLegendNode class was added which allows for the creation of color ramp-based legend nodes. It\'s now used for raster layers when using a pseudocolor renderer with the linear interpolation type or for the single-band gray renderer, as well as for point clouds using a ramp based renderer.

En una leyenda de diseño, el elemento de la rampa hereda la anchura y la altura del símbolo de la leyenda por defecto, pero es posible anular opcionalmente este comportamiento.

Se incluyen etiquetas para el valor mínimo y máximo de la rampa, que se representan utilizando la misma configuración de fuente que el resto del texto de los elementos de la leyenda:

![image25](images/entries/86e6d57200857c701d9438eabe246289e74f5194-1.gif)

La alineación de etiqueta seguirá los ajustes de leyenda:

![image26](images/entries/7c80cc107b0e3fb1098d416834463478367b555e-1.gif)

Y, naturalmente, los artículos funcionarán bien con leyendas de varias columnas:

![image27](images/entries/145e2d7f00d3a2b33f383e3cbd808a6b21a792c4-1.gif)

![image28](images/entries/0dad8d8307a3c3fe1f5b28aa56790b307c090f33-1.gif)

This feature was funded by [Hans van der Kwast](https://www.youtube.com/c/HansvanderKwast)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Mejoras en la leyenda de la rampa de color
Los elementos de la leyenda de la rampa de color ahora admiten las siguientes opciones configurables:
- Un prefijo y sufijo para el texto de rampa
- Formateo numérico
- Dirección de rampa
- Personalización de formateo de texto
- La habilidad para crear barras horizontales.

Los usuarios también pueden optar por refinar estos ajustes para un elemento de leyenda de diseño en particular. Esta funcionalidad está disponible para todos los elementos de la rampa, incluidas las capas de trama, nube de puntos o malla.

![image29](images/entries/9a48f9d2970e50c7d4f70358b6cfd870033427a5-1.gif)

![image30](images/entries/fb52826e81fd08763c269aaab50ea0c25b7af9b8-1.gif)

This feature was funded by [Hans van der Kwast](https://www.youtube.com/c/HansvanderKwast)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Preajustes de texto dinámico
The new *Add Item -\> Dynamic Text* menu contains preset dynamic text expressions that users can use to insert a label automatically containing the corresponding expression.

For example, using the dynamic text element **Layout Name** will insert a label containing the expression \[% \@layout_name %\]. This improves the feature awareness, discoverability, and provides an easy method for users to access dynamic attributes.

![image31](images/entries/c41a7d2a5ec018bfba237429aa5d125d11ad9310.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Expresiones
### Prestación: Formateo opcional de resultados UUID
There is now a string format parameter available for the `uuid()` function in QGIS expressions. Users now have various options that they can use to stipulate the format of the returned UUID value, including the following options:
- `uuid()`: **{0bd2f60f-f157-4a6d-96af-d4ba4cb366a1}**
- `uuid('WithoutBraces')`: **0bd2f60f-f157-4a6d-96af-d4ba4cb366a1**
- `uuid('Id128')`: **0bd2f60ff1574a6d96afd4ba4cb366a1**

![image32](images/entries/3f0471353b72cffc4b69defb87cea2d7a1c44017.webp)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Prestación: Variable CRS de capa para expresiones
QGIS expressions now support a *layer_crs* variable which will return the AuthID for a particular layer\'s coordinate reference system. This allows expressions to identify the layer CRS dynamically and perform transformations without needing to manually specify the CRS.

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Prestación: Compatibilidad con las funciones de mínimo, máximo, mayoría, suma, media y mediana en matrices numéricas
Las expresiones de QGIS incluyen ahora funciones de agregación para colecciones, que permiten recuperar fácilmente valores específicos de una colección que pueden utilizarse en elementos de QGIS como las simbologías. Se han introducido las siguientes funciones:
- array_min
- array_max
- array_majority
- array_sum
- array_mean
- array_median

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Feature: Negative index for array_get function
The function array_get now supports the use of negative index positions.

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Feature: Add map_credits function
A *map_credits* function was added that collates a list of all the layer metadata attribution strings for the layers shown inside a specified map item.

Por ejemplo:

    array_to_string( map_credits( 'Main Map' ) )
    
Returns a comma-separated list of layer credits for layers shown in the \'Main Map\' layout item, e.g \'CC-BY-NC, CC-BY-SA\'

There\'s an optional *include_layer_names* argument you can use to include layer names before their attribution:

    array_to_string( map_credits( 'Main Map',
       include_layer_names := true,
       layer_name_separator := ': ' ) )
    
This would return a comma-separated list of layer names and their credits for layers shown in the \'Main Map\' layout item, e.g. \'Railway lines: CC-BY-NC, Basemap: CC-BY-SA\'

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Digitalizando
### Prestación: Menú contextual de Seleccionar objetos espaciales
Ahora es posible seleccionar características mediante un menú contextual en el lienzo del mapa. Al hacer clic con el botón derecho del ratón en el mapa, se identificarán de forma inteligente las características que se encuentran bajo el cursor del ratón y se podrán añadir o eliminar las características disponibles de la selección actual. Cuando hay varias características disponibles, puede persistir un breve retraso mientras el sistema intenta buscar las características disponibles que estarán disponibles en un elemento de menú anidado para su selección, o los usuarios pueden simplemente utilizar la función *seleccionar todo* para seleccionar todas las características disponibles en la posición dada.

![image33](images/entries/edec99086412445b929c0926f69600279e56d4fb.gif)

This feature was funded by [Kristianstad](https://www.kristianstad.se)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Prestación: Se ha añadido la configuración del trazado de curvas a la interfaz de usuario
Existing curve tracing settings [were introduced previously](https://github.com/qgis/QGIS/pull/37826) and have now been exposed in the user interface to enable users to incrementally modify settings to optimize their results when capturing curve data.

![image34](images/entries/29b75d5574181d5b7570090b9801ede92bec2fcd.webp)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Prestación: Herramienta de escalado de objetos espaciales
A new digitizing tool allows for selected features to be scaled when in editing mode. This implementation was based on the work of [\@roya0045](https://github.com/roya0045) with [#40650](https://github.com/qgis/QGIS/pull/40650).

![image35](images/entries/16ac8bca1e78da740dc8ea8b6b46a916f8f0b83d.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Administración de datos
### Prestación: Nuevo algoritmo exportar a hoja de cálculo
Los usuarios pueden exportar una selección de capas vectoriales como hojas en una nueva hoja de cálculo o añadirlas como hojas adicionales a una hoja de cálculo existente

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Reproyectar coordenadas en el Georeferenciador
El georreferenciador ahora reproyecta los puntos de datos en una proyección de salida deseada, en lugar de utilizar el SRC del lienzo del mapa para determinar las posiciones de los puntos de datos. Esto permite a los usuarios una mayor flexibilidad y control al capturar los puntos de control.

![image36](images/entries/50d4d1d6353ebfa251c53ea29c28821bf4c5ac18.gif)

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Prestación: Relaciones polimórficas/ Sistema de gestión de documentos
A new GUI is available to manage polymorphic relations, implemented as a part of the dynamic relations described in [QEP #79](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/79).

The \"Add relation\" button in the relation manager screen now has additional options for adding and editing polymorphic relations:

The \"Add polymorphic relation\" and \"Edit polymorphic relation\" open the same dialog, although in the latter case it will automatically be populated with existing values.

Una vez guardada, la lista de relaciones aparece como un widget de árbol, donde los objetos de relación generados para una relación polimórfica aparecen como hijos. Los nombres de las relaciones generadas no se pueden modificar.

Las relaciones polimórficas se almacenan dentro de un proyecto y actualmente no se pueden exportar.

![image37](images/entries/6628cd483a00a52f51cd963febd883d2756eb299.webp)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Widgets y Formularios
### Prestación: Restricciones blandas y duras en las formas
Historically, required fields would prevent a form from being saved entirely. Using soft constraints allow forms to notify users that expected information has been omitted, without preventing the form submission. Hard constraints, by contrast, function identically to the previous \"required fields\" functionality and will prevent form submissions unless data is correctly captured for the field.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Viktor Sklencar)](https://www.lutraconsulting.co.uk)
## Herramientas de análisis
### Prestación: API de geocodificación de Nominatim
Although not exposed through the locator or as an algorithm, QGIS now includes a Nominatim API geocoder class. The geocoder class\' implementation insures that it respects the OpenStreetMap Foundation Terms of Use by caching results and throttling requests by default.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Procesado
### Prestación: Permitir la expresión de campos de orden en el algoritmo PointsToPath
`$id` may be used as an expression for a csv with ordered values, and the `ORDER_EXPRESSION` parameter has been added to the PointsToPath algorithm.

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Prestación: Anulación del SRC para la salida de Cortar Ráster por extensión
In some instances, the **Clip raster by extent** algorithm may output features without a CRS specified, which can now be modified by explicitly enforcing the output to inherit it\'s CRS from the input layer.

This feature was developed by [rldhont](https://api.github.com/users/rldhont)
### Feature: Add \"retain fields\" algorithm
Allows users to select a list of fields to keep, and all other fields will be dropped from the layer. Helps with making flexible models where input datasets may have a range of different fields and only a certain subset of them need to be retained. This work was inspired by [#39114](https://github.com/qgis/QGIS/pull/39114)

![image38](images/entries/c02ae93517a537925c870d3a9d477cc26af5f9e7.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Parámetro de campo común de referencia para múltiples capas
Los parámetros de campo de las herramientas de procesamiento pueden soportar el procesamiento de un campo común para múltiples capas vectoriales, en una implementación inspirada en el comportamiento de algunos algoritmos de procesamiento en Orfeo ToolBox.

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Feature: Extend import geotagged photos to include exif_orientation
The \"Import geotagged photos\" tool has been updated so that the exif_orientation parameter value is extracted to the output table. This ensures that maptips and other HTML widgets can be configured to correctly transform the photos to be correctly displayed based on the orientation value.

This feature was developed by [Pelle Rosenbeck Gøeg](https://api.github.com/users/pellegoeg)
### Prestación: Algoritmo de exportación de información de capas
Se ha añadido un nuevo algoritmo en la caja de herramientas de procesamiento llamado exportar información de capas para apoyar la creación de una capa de polígonos correspondiente a la extensión de la(s) capa(s) definida(s) por el usuario con detalles adicionales de la capa que se adjuntan como atributos a cada característica de polígono. La información recogida soporta actualmente los siguientes elementos:
- SRC
- Nombre del proveedor
- Ruta del archivo
- Nombre de la capa
- Filtro de subconjunto
- Resumen
- Atribución

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Prestación: Algoritmos de percentiles y rangos de celdas
Las características de la herramienta de procesamiento **Estadística de Celdas** han sido replicadas y modificadas para permitir tres nuevos algoritmos de procesamiento, que permiten a QGIS calcular las estadísticas de las celdas de manera similar a las funciones de porcentaje comunes utilizadas en los programas de hojas de cálculo. Los nuevos algoritmos de procesamiento son:
- **Percentil de la pila de celdas**
- **Porcentaje de la pila de celdas desde el valor**
- **Porcentaje de la pila de celdas a partir de la capa rasterizada**

Mientras que el algoritmo de percentiles sólo ofrece la posibilidad de calcular percentiles basados en un valor de fracción de entrada (que oscila entre 0 y 1), también se puede calcular un ráster de rango porcentual basado en un ráster de valor de entrada. Esto ofrece al usuario la posibilidad de calcular los percentiles por celda basándose en la entrada de valores del conjunto de datos (por ejemplo, capas de muestra).

Todos los algoritmos proporcionan diferentes métodos para calcular los percentiles y los rangos porcentuales:

**Percentile:** - Nearest Rank - Inclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTILE.INC* function) - Exclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTILE.EXC* function)

**Percentrank:** - Inclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTRANK.INC* function) - Exclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTRANK.EXC* function)

![image39](images/entries/febde74bab33bb165971509e90fb112c4b643001.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Prestación: Algoritmo de procesamiento de puntos a líneas
Se ha añadido un algoritmo de procesamiento nativo en c++ que crea capas de líneas a partir de capas de puntos, similar al existente en python *Points to path* pero con funcionalidad ampliada:
- Added support for *natural sorting* ( \'10\' \> \'9\' )
- Evitar crear líneas no válidas con un solo vértice
- Evitar crear líneas cerradas con dos vértices

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
## Opciones de Aplicación y Proyecto
### Prestación: Capas ocultas
Los proyectos de QGIS ahora admiten la inclusión de capas ocultas, que pueden incluirse en un proyecto pero no son visibles en el índice.

La propiedad de la capa es configurable desde la pestaña **Fuentes de datos** de las propiedades del proyecto e incluye soporte de la API para el filtrado de texto.

![image40](images/entries/95af3e621abc52bc04d94eca629279df2b987961.gif)

Esta prestación fue financiada por **ARPA Piemonte**.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Custom \"Full Extent\" definition
A new \"View Settings\" tab has been added to the project properties, with the option to manually defined the full extent of a project. The extent defined here will be the extent used when zooming to the full map extent, instead of the calculated or maximum extent of all layers. This is useful for defining a particular area of interest for a project and does not limit user\'s ability to \"zoom out\" further than the defined extent.

![image41](images/entries/d0109e9db23e15765f201c3b292f23fa4230b608.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Alternar la caché de red a QgsNetworkAccessManager
Una casilla de verificación en el panel del registrador de red permite ahora a los usuarios desactivar temporalmente la caché de red, lo que resulta útil cuando se depura la actividad de red de QGIS, o cuando se utiliza QGIS para probar los cambios del lado del servidor.

Esta es una configuración transitoria por diseño y se olvida tan pronto como se cierra QGIS.

![image42](images/entries/0115a38666f35166fa9e6fd53791a7bc8f73b6dc.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Navegador
### Prestación: Unificar las conexiones de ArcGis Feature Service y ArcGIS Map Service en el navegador
The separate \"ArcGis Feature Service\" and \"ArcGIS Map Service\" browser connections have been replaced with a single, unified, **\"ArcGIS Rest Servers\"** connection and browser node, which shows a definitive view of the server and exposes both service types.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: Permitir la navegación de ArcGIS REST por grupos de contenido
Las conexiones de ArcGIS Feature Service que tienen sus correspondientes URLs de punto final del Portal pueden ser exploradas por grupos de contenido en el panel del navegador.

If a connection has the Portal endpoints set, then expanding out the connection in the browser will show a \"Groups\" and \"Services\" folder, instead of the full list of services usually shown. Expanding out the groups folder will show a list of all content groups that the user is a member of, each of which can be expanded to show the service items belonging to that group.

This feature was funded by [SRK Consulting](https://www.srk.com)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Proveedores de datos
### Prestación: Algoritmo de exportación DXF nativo
Permite exportar capas individuales o múltiples en un único archivo DXF. Para cada capa de entrada, los usuarios pueden seleccionar qué atributo utilizar para dividir una sola capa en múltiples capas de salida.

Implements a native DXF export algorithm using `QgsDxfExport` functionality, which is also used by `Project -> Import/Export -> Export Project to DXF`.

![image43](images/entries/7800af6d2597ad04650532f201c8d4ee005c8e53.gif)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Prestación: Tipos de geometría adicionales para la exportación de PostGIS
Some available geometry types from the GDAL ogr2ogr operation used for exporting data to PostGIS databases have been added to the tool interface. This functionality also includes the option to specify vector dimensions for exported data and resolves issue [39003](https://github.com/qgis/QGIS/issues/39003).

![image44](images/entries/48415fefe669fa93d5c7e13959c4a35e6dab60e2.gif)

This feature was developed by [mazano](https://api.github.com/users/NyakudyaA)
### Prestación: Mejora de las solicitudes de red con GDAL
A QgsCPLHTTPFetchOverrider utility class was added and used in the OGR provider which redirects GDAL\'s CPL HTTP calls through QgsBlockingNetworkRequest. This ensures that GDAL can use the QGIS network provider rather than redirecting requests through cURL. Additional head(), put() and deleteResource() methods were added to QgsBlockingNetworkRequest.

This feature was developed by [Even Rouault](https://api.github.com/users/rouault)
### Prestación: Campos generados de sólo lectura
Se ha añadido un método de la API para garantizar que las columnas generadas de sólo lectura no se expongan en los editores.

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Prestación: Mejora de la carga de MSSQL con parámetros predefinidos
Para reducir los tiempos de carga de las capas, la extensión de la capa del mapa puede ser precalculada, y las claves primarias pueden ser especificadas, eliminando la necesidad de que QGIS calcule estas características y mejorando el rendimiento.

This is done by extending dbo.geometry_columns tables and adding the following extra columns, which may be populated accordingly by database administrators:
- Extent : qgis_xmin, qgis_xmax, qgis_ymin, qgis_ymax
- Primary key : qgis_pkey

En el widget de configuración de la conexión a la base de datos, hay ahora dos casillas de verificación adicionales que hacen uso de estos parámetros:
- Utilizar la extensión de la capa de las columnas adicionales
- Utilizar la clave primaria de la columna extra

![image45](images/entries/3d77459436d542190afa88f6d927be7f8245dbf0.gif)

This feature was funded by [ms.GIS](http://msgis.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Filtro de esquemas para MS SQL
Los usuarios pueden ahora filtrar los esquemas disponibles para las conexiones MS SQL. El widget de conexión a la base de datos contiene ahora opciones para filtrar los esquemas disponibles, de modo que sólo los esquemas esperados estén disponibles en el navegador de QGIS.

![image46](images/entries/1e2fe1a94747c9aa2fbbaab3053bfc6631cfbb22.gif)

This feature was funded by [ms.GIS](http://msgis.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Prestación: Compatibilidad con la base de datos SAP HANA
QGIS es ahora compatible con las bases de datos SAP HANA. SAP HANA es una base de datos en memoria con un motor espacial compatible con OGC con una edición express gratuita disponible en www.sap.com

This feature was developed by [Maxim Rylov](https://api.github.com/users/mrylov)
### Prestación: Se deja de dar soporte a DB2
**El proveedor de datos DB2 ha sido marcado como obsoleto**, y está oculto de la interfaz de usuario de QGIS por defecto.

QGIS has adopted a gentle approach to removing unmaintained core providers, and users of deprecated providers may enable support for them by setting the hidden \"providers/showDeprecated\" settings key to *true*.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Prestación: API de conexión de Oracle
La API de QGIS incluye ahora *QgsAbstractDatabaseProviderConnection* para el proveedor de Oracle.

Esta prestación fue financiada por Metropole de Lille

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Prestación: Añadir opciones avanzadas para la importación de datos rasterizados
Se ha introducido una nueva funcionalidad que permite especificar parámetros avanzados al importar capas utilizando el proveedor de datos GDAL, lo que abre un amplio abanico de nuevas posibilidades, sobre todo a la hora de trabajar en torno a los problemas y deficiencias esperados del conjunto de datos.

![image47](images/entries/5d7ccf71a162d927706fd6e6517a67452ec653e1.webp)

Esta prestación fue desarrollada por Mathieu Pellerin
## Servidor de QGIS
### Prestación: Escala de símbolos GetLegendGraphics
La solicitud GetLegendGraphics de QGIS Server WMS ahora admite la inclusión de denominadores de escala mínima/máxima en las exportaciones de símbolos json

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Prestación: Arrastrar y soltar para la respuesta GetFeatureInfo de WMS
Con el formulario de edición de arrastrar y soltar, es posible reordenar los atributos y añadir grupos o subgrupos desde el formulario de edición. Esta funcionalidad se ha ampliado para que la respuesta GetFeatureInfo de WMS pueda modificarse para incluir grupos y subgrupos, así como para permitir que el contenido de la respuesta se modifique y reordene utilizando el formulario de edición, con soporte para la funcionalidad de arrastrar y soltar.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
## Programabilidad
### Prestación: Ejecutar varios elementos desde el diálogo del historial de comandos
La consola de QGIS Python admite ahora la ejecución de múltiples comandos seleccionados desde el diálogo del historial, añadiendo un nuevo botón **Pegar**.

![image48](images/entries/1de42c7dc35c2b73dce1605a3c36b97166d81850.webp)

This feature was developed by [Salvatore Larosa](https://api.github.com/users/slarosa)
### Prestación: Activar o desactivar complementos desde la línea de comandos
The qgis_process command line tool has had new commands added which allow users to enable or disable plugins using the commands as outlined below:
- `qgis_process plugins enable plugin_name`: enables the named plugin
- `qgis_process plugins disable plugin_name`: disables the named plugin

This improves the automation capabilities of QGIS and allows the use of plugins on headless environments with the qgis_process tool.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Se cae con las capas de VRT usando las funciones de píxel de Python | [#41048](https://github.com/qgis/QGIS/issues/41048) | Trabaja para mí |  |
| No se pueden introducir atributos y guardar ediciones en la tabla PostGIS cuando el usuario sólo tiene el privilegio de INSERTAR | [#40922](https://github.com/qgis/QGIS/issues/40922) | [PR #41059](https://github.com/qgis/QGIS/pull/41059) | no |
| El nombre de la capa de GeoPackage se trunca cuando el nombre del archivo contiene más de un punto | [#40864](https://github.com/qgis/QGIS/issues/40864) | [PR #41061](https://github.com/qgis/QGIS/pull/41061) | no |
| No se puede hacer clic con el botón derecho en la tabla GeoPackage desde el navegador | [#40856](https://github.com/qgis/QGIS/issues/40856) | Trabaja para mí |  |
| Vacío La capa de rascado temporal convertida en permanente no es editable | [#38834](https://github.com/qgis/QGIS/issues/38834) | [PR #41075](https://github.com/qgis/QGIS/pull/41075) | no |
| Actualización de la compilación de MXE, varios problemas | varios problemas | [Commit afff8ba7be2794fe521a462feaf83b1a5d7cce63](https://github.com/qgis/QGIS/commit/afff8ba7be2794fe521a462feaf83b1a5d7cce63) [PR #40923](https://github.com/qgis/QGIS/pull/40923) | si (CI) |
| can\'t change value in vertex editor if \"locale\" settings use commas as decimal separator | [#29682](https://github.com/qgis/QGIS/issues/29682) | [PR #41082](https://github.com/qgis/QGIS/pull/41082) | [PR #41607](https://github.com/qgis/QGIS/pull/41607) |
| Empty String \'\' is shown as NULL with a spatialite layer using OGR provider | [#41076](https://github.com/qgis/QGIS/issues/41076) | [PR #41109](https://github.com/qgis/QGIS/pull/41109) | [PR #41123](https://github.com/qgis/QGIS/pull/41123) |
| La solicitud errónea de WFS 2.0.0 devuelve objetos espaciales duplicados | [#41087](https://github.com/qgis/QGIS/issues/41087) | [PR #41169](https://github.com/qgis/QGIS/pull/41169) | no |
| Servidor WMS GetFeatureInfo inconsistencias de ID de características | [#41124](https://github.com/qgis/QGIS/issues/41124) | [PR #41137](https://github.com/qgis/QGIS/pull/41137) | [PR #41148](https://github.com/qgis/QGIS/pull/41148) |
| WMS lanza LayerNotDefined cuando el nombre de la capa contiene el signo más (+) | [#41116](https://github.com/qgis/QGIS/issues/41116) | [PR #41211](https://github.com/qgis/QGIS/pull/41211) | [PR #41331](https://github.com/qgis/QGIS/pull/41331) |
| QGIS Server WFS 1.1: problema con el orden de los ejes | [#36584](https://github.com/qgis/QGIS/issues/36584) | [PR #41242](https://github.com/qgis/QGIS/pull/41242) | [PR #41608](https://github.com/qgis/QGIS/pull/41608) |
| raster export (save as\...) not working if QGIS locale uses commas as decimal separator | [#41284](https://github.com/qgis/QGIS/issues/41284) | [PR #41316](https://github.com/qgis/QGIS/pull/41316) | [PR #41330](https://github.com/qgis/QGIS/pull/41330) |
| WFS de QGISserver devuelve un GML no válido en caso de WFS en cascada | [#41292](https://github.com/qgis/QGIS/issues/41292) | [PR #41335](https://github.com/qgis/QGIS/pull/41335) | [PR #41387](https://github.com/qgis/QGIS/pull/41387) |
| Mejor gestión de los FID duplicados en los GPKG | [#41156](https://github.com/qgis/QGIS/issues/41156) | Trabaja para mí |  |
| No se pueden crear nuevas tablas en un geopackage (navegador) | [#41342](https://github.com/qgis/QGIS/issues/41342) | [PR #41355](https://github.com/qgis/QGIS/pull/41355) | [PR #41403](https://github.com/qgis/QGIS/pull/41403) |
| QGIS se cae al cancelar el formulario de añadir hijos | [#41295](https://github.com/qgis/QGIS/issues/41295) | [PR #41375](https://github.com/qgis/QGIS/pull/41375) | N/D |
| El grupo no tiene nombre al importar subcapas desde el panel del navegador | [#41343](https://github.com/qgis/QGIS/issues/41343) | [PR #41379](https://github.com/qgis/QGIS/pull/41379) | [PR #41402](https://github.com/qgis/QGIS/pull/41402) |
| La herramienta Identificar ya no funciona en las capas de arcgis map services | [#41311](https://github.com/qgis/QGIS/issues/41311) | [PR #41427](https://github.com/qgis/QGIS/pull/41427) | [PR #41430](https://github.com/qgis/QGIS/pull/41430) |
| La señal committedAttributeValuesChanges no se emite cuando el proyecto está en modo de transacción automática | [#41477](https://github.com/qgis/QGIS/issues/41477) | [PR #41539](https://github.com/qgis/QGIS/pull/41539) | arriesgado |
| El archivo de proyecto no almacena variables con texto formateado | [#41541](https://github.com/qgis/QGIS/issues/41541) | Fallo en la fase previa de QT |  |
| Una nueva tabla espacial en un geopackage con índice siempre lanza una advertencia | [#41436](https://github.com/qgis/QGIS/issues/41436) | [PR #41556](https://github.com/qgis/QGIS/pull/41556) | [PR #41609](https://github.com/qgis/QGIS/pull/41609) |
| Empty \"Exclude layers\" selection list in Server settings dialog when using projects saved in GPKG files or PGSQL databases | [#40552](https://github.com/qgis/QGIS/issues/40552) | [PR #41605](https://github.com/qgis/QGIS/pull/41605) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Prestación: Corrección de Errores por Peter Petrik
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Omitir el círculo de tipo de capa desconocida en las teselas vectoriales | [#41529](https://github.com/qgis/QGIS/issues/41529) | [PR #41584](https://github.com/qgis/QGIS/pull/41584) | por hacer |
| Las contraseñas no se pueden guardar en el llavero en macOS con QGIS 3.16 | [#40541](https://github.com/qgis/QGIS/issues/40541) | [QGIS-Mac-Packager PR #112](https://github.com/qgis/QGIS-Mac-Packager/pull/112) | automático |
| Symbol not found: \_curl_mime_addpart with GDAL merge | [QGIS-Mac-Packager Issue #111](https://github.com/qgis/QGIS-Mac-Packager/issues/111) | [QGIS-Mac-Packager PR #112](https://github.com/qgis/QGIS-Mac-Packager/pull/112) | automático |
| initGUI() da lugar a un fallo de segmentación en macOS en PyQgis independiente | [#40378](https://github.com/qgis/QGIS/issues/40378) | respondido con el arreglo del script |  |
| La instancia QgsCompoundColorWidget se cae cuando QgsApplication::colorSchemeRegistry() está vacío \\ | [#28208](https://github.com/qgis/QGIS/issues/28208) | inválido |  |
| Incluir las fuentes que faltan en la compilación | [QGIS-Mac-Packager Issue #105](https://github.com/qgis/QGIS-Mac-Packager/issues/105) | [PR #41412](https://github.com/qgis/QGIS/pull/41412) | no necesitado? |
| Manejo incorrecto de los valores de los datos Grib | [#37504](https://github.com/qgis/QGIS/issues/37504) | no se puede replicar en qgis 3.16 macos |  |
| Error al abrir datos de malla .2dm y .xmdf | [#40385](https://github.com/qgis/QGIS/issues/40385) | [PR libspatialindex #221](https://github.com/libspatialindex/libspatialindex/pull/221) | automático |
| error r.watershed en macOS | [#40996](https://github.com/qgis/QGIS/issues/40996) | [QGIS-Mac-Packager Commit 7238782](https://github.com/qgis/QGIS-Mac-Packager/commit/7238782f4b3408f1d69b2adbafe52d9698c4f20c) | [QGIS-Mac-Packager Commit 7238782](https://github.com/qgis/QGIS-Mac-Packager/commit/7238782f4b3408f1d69b2adbafe52d9698c4f20c) |
| La aceleración OpenCL no se encuentra en macOS | [#41182](https://github.com/qgis/QGIS/issues/41182) | [PR #41374](https://github.com/qgis/QGIS/pull/41374) | [Github commit](https://github.com/nyalldawson/QGIS/commit/997d3c1ab8386a5035b70a65e9843ec64feaa377) |
| Proj.db no se encuentra para las herramientas SAGA en QGIS 3.17 Mac nightly | [#41606](https://github.com/qgis/QGIS/issues/41606) | [QGIS-Mac-Packager Commit 7a71390](https://github.com/qgis/QGIS-Mac-Packager/commit/7a713903cf001a9e156eac60e25e84789e1e534a) | automático |
| \[mesh\]\[ui\] Changing settings for 2D Contour color ramp shader shows confusing widgets | \"[#39571](https://github.com/qgis/QGIS/issues/39571) | [PR #41442](https://github.com/qgis/QGIS/pull/41442) | no necesitado? |
| QGIS crashes when \"open directory\" is selected from the recent projects contextual menu | [PR #41591](https://github.com/qgis/QGIS/pull/41591) | [PR #41591](https://github.com/qgis/QGIS/pull/41591) | por hacer |
| La configuración definida por los datos en el marco html no funciona | [#41590](https://github.com/qgis/QGIS/issues/41590) | investigación realizada |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| PostgreSQL provider doesn\'t support special characters for authentication on Windows | [#41132](https://github.com/qgis/QGIS/issues/41132) | [PR #41144](https://github.com/qgis/QGIS/pull/41144) | [PR #41179](https://github.com/qgis/QGIS/pull/41179) |
| Conexiones WMS/WFS La importación XML falla silenciosamente si hay dos conexiones con el mismo nombre | [#39758](https://github.com/qgis/QGIS/issues/39758) | [PR #41145](https://github.com/qgis/QGIS/pull/41145) | [PR #41195](https://github.com/qgis/QGIS/pull/41195) |
| QgsAttributeWidgetRelationEditWidget::setRelationEditorConfiguration(): evitar el bloqueo en una relación corrupta | [#40495](https://github.com/qgis/QGIS/issues/40495) | [PR #41147](https://github.com/qgis/QGIS/pull/41147) | [PR #41175](https://github.com/qgis/QGIS/pull/41175) |
| \[Processing\] Rescale Raster gives bad results | [#41084](https://github.com/qgis/QGIS/issues/41084) | [PR #41155](https://github.com/qgis/QGIS/pull/41155) | [PR #41194](https://github.com/qgis/QGIS/pull/41194) |
| QGIS no utiliza el índice espacial PostGIS en la columna de geografía | [#39453](https://github.com/qgis/QGIS/issues/39453) | [PR #41296](https://github.com/qgis/QGIS/pull/41296) | [PR #41301](https://github.com/qgis/QGIS/pull/41301) |
| El Geopackage con el campo DateTime (selección temporal) se comporta de forma diferente para la pintura y la tabla de atributos | [#41074](https://github.com/qgis/QGIS/issues/41074) | Análisis del problema |  |
| Se cae con las capas de VRT usando las funciones de píxel de Python | [#41048](https://github.com/qgis/QGIS/issues/41048) | [GDAL PR 3424](https://github.com/OSGeo/gdal/pull/3424) | [GDAL Commit a2ed089](https://github.com/OSGeo/gdal/commit/a2ed0894b83e023e21a6dfa19fa399d0784b339a) |
| Nombres de capa vacíos al añadir una capa Raster desde el controlador GDAL / OGCAPI | [#41428](https://github.com/qgis/QGIS/issues/41428) | [PR #41452](https://github.com/qgis/QGIS/pull/41452) | no apropiado |
| El GeoTIFF importado no utiliza la extensión de los datos para seleccionar el CRS - NAD83 vs NAD83(CSRS) | [#41456](https://github.com/qgis/QGIS/issues/41456) | inválido |  |
| Georreferenciador: se corrige el fallo en los archivos .points generados por versiones antiguas de QGIS | no reportado | [PR #41480](https://github.com/qgis/QGIS/pull/41480) | N/D |
| Crash al intentar cargar las teselas vectoriales de los mapas de la comunidad de ArcGis | [#41401](https://github.com/qgis/QGIS/issues/41401) | [PR #41481](https://github.com/qgis/QGIS/pull/41481) | [PR #41516](https://github.com/qgis/QGIS/pull/41516) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Prestación: Corrección de errores por Julien Cabieces
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Regresión del recuento de registros en las vistas | [#41188](https://github.com/qgis/QGIS/issues/41188) | No se arreglará |  |
| Errores de desbordamiento de enteros al crear y guardar capas virtuales | [#40503](https://github.com/qgis/QGIS/issues/40503) | [PR #41332](https://github.com/qgis/QGIS/pull/41332) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| La Herramienta de Vértices utiliza datos antiguos almacenados en caché, lo que da lugar a datos corruptos en la base de datos. | [#40720](https://github.com/qgis/QGIS/issues/40720) | [PR #41357](https://github.com/qgis/QGIS/pull/41357) | [PR #41509](https://github.com/qgis/QGIS/pull/41509) |
| Metadatos de la capa WMS - el recuento de SRC disponibles no es correcto | [#40318](https://github.com/qgis/QGIS/issues/40318) | [PR #41363](https://github.com/qgis/QGIS/pull/41363) |  |
| Faltan variables de capa en el algoritmo de la calculadora de campo en QGIS 3.16.1 | [#40255](https://github.com/qgis/QGIS/issues/40255) | [PR #41417](https://github.com/qgis/QGIS/pull/41417) | [PR #41510](https://github.com/qgis/QGIS/pull/41510)/ |
| El filtro no se aplica en las capas duplicadas | [#40349](https://github.com/qgis/QGIS/issues/40349) | Retroalimentación |  |
| No se pueden guardar los resultados en la base de datos PostgreSQL al iterar características en los algoritmos de procesamiento | [#39620](https://github.com/qgis/QGIS/issues/39620) | [PR #41446](https://github.com/qgis/QGIS/pull/41446) |  |
| Closed Python call to \--processing.run(\'qgis:fieldcalculator\'\-- fails to catch divide by zero | [#37737](https://github.com/qgis/QGIS/issues/37737) | Ya Corregido |  |
| El widget de expresión no muestra los campos cuando se marca la opción "Sólo objetos espaciales seleccionados". | [#40055](https://github.com/qgis/QGIS/issues/40055) | [PR #41457](https://github.com/qgis/QGIS/pull/41457) | [PR #41511](https://github.com/qgis/QGIS/pull/41511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/en/)
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL issues.qgis.org (if reported) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix text edit widget wrapper incorrectly shows \"NULL\" string for indeterminate state | no reportado | [Commit fa91357](https://github.com/qgis/QGIS/commit/fa9135792574ff5dbbd1ab53d15faec3d190e3db) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| \[layouts\] Expose the correct expression context for attribute and manual table text format widgets | no reportado | [Commit f337271](https://github.com/qgis/QGIS/commit/f3372716060f2c1eecff46c99c999b66505504fc) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir un error incorrecto al guardar modificaciones de atributos en capas con uniones | no reportado | [Commit 01889d9](https://github.com/qgis/QGIS/commit/01889d96b22757028e62c156a945ae8b86e69a68) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir el mensaje de error JSON engañoso cuando un formulario de atributos no guarda los cambios | no reportado | [Commit fd657be](https://github.com/qgis/QGIS/commit/fd657bee96c2b58c035a69a71fd58d1cb409770e) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix project \"avoid tile artifacts\" setting has no effect on server | [#37679](https://github.com/qgis/QGIS/issues/37679) | [Commit 04d6ea9](https://github.com/qgis/QGIS/commit/04d6ea99b43fb8e426dc1cb31b2b7e913aca203c) | No apropiado |
| Don\'t crash when a relation is created where the field names defined in the relation differ in case from the layer\'s field names | no reportado | [Commit 0f49cb9](https://github.com/qgis/QGIS/commit/0f49cb909732882e4c0b3ba26a6987fff95e29ea) | [Commit c708ca58](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Arreglar los botones de añadir/eliminar no tienen iconos en los diálogos de creación de relaciones | no reportado | [Commit 2e81dbc](https://github.com/qgis/QGIS/commit/2e81dbcc50e510afc9033be9a99bfcb2512f6fd9) | N/D |
| Se ha corregido la restauración de las opciones de creación de rásteres de GDAL anteriores cuando se ejecuta un algoritmo desde el historial de procesamiento. | no reportado | [Commit 645397e](https://github.com/qgis/QGIS/commit/645397e83d88c124e8ca8faa46b304c2e74ec3e9) | [Commit c708ca5](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Arreglar la configuración de las opciones del perfil GDAL actual sobrescribe temporalmente la definición de uno de los perfiles GDAL almacenados | [#41378](https://github.com/qgis/QGIS/issues/41378) | [Commit 7ff0187](https://github.com/qgis/QGIS/commit/7ff01871d0c72b92070aed3b66f95f7f268ce6e0) | [Commit c708ca58e](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Fix crash when running model from file through qgis_process with the \--json switch | no reportado | [Commit ccd4fb6](https://github.com/qgis/QGIS/commit/ccd4fb67eb309a077e959df60c0d3556321453da) | [Commit 8bda37c](https://github.com/qgis/QGIS/commit/8bda37ca0f2b914fa5fe9916398a2d08c1ef774d) |
| When labelling job takes a long time to render, don\'t clear the map canvas between the finished layer render state and final state | no reportado | [Commit 1beb1bd](https://github.com/qgis/QGIS/commit/1beb1bdc788ba64f826c54d3ab587fcc5289afb4) | N/D |
| Don\'t loop through all selected features multiple times (once per field) when the attribute form is opened | [#41366](https://github.com/qgis/QGIS/issues/41366) | [Commit c661359](https://github.com/qgis/QGIS/commit/c6613593c72ac0411417d5a9aacf0335d52c4e66) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir la expresión incorrecta del filtro de solicitud de características generada cuando el representados basado en reglas utiliza una regla NOT IN | no reportado | [Commit a895598](https://github.com/qgis/QGIS/commit/a89559879743242d2b7138c2d3d73179c380af97) | [Commit 5eec9e4](https://github.com/qgis/QGIS/commit/5eec9e42f3e4ddeb17f63a194df7a1f9ccb2e5e5) |
| Preguntar a los usuarios por los campos de destino existentes para los campos de resultado Suma de la longitud de la línea y Recuento de puntos en los polígonos cuando se ejecuta en modo in situ. | [#39807](https://github.com/qgis/QGIS/issues/39807) | [Commit 12e8130](https://github.com/qgis/QGIS/commit/12e8130beb0836fe18bf741f5ad26bf599feb84f) | No apropiado |
| Corregir el fallo cuando no existen capas en el proyecto | no reportado | [Commit 039bc20](https://github.com/qgis/QGIS/commit/039bc202733d57e5daaa13d417eb78b2c072851d) | N/D |
| \[processing\] Fix exception in algorithm locator filter if an algorithm has no group set | no reportado | [Commit 46dbd8b](https://github.com/qgis/QGIS/commit/46dbd8b2d6275256779c14938de7424ab1053d7a) | [Commit 7ef7b17](https://github.com/qgis/QGIS/commit/7ef7b17f2601bd8ee8f31dc5be7a69b90c89550f) |
| Expose additional GDAL supported resampling methods as options for \"early\" raster resampling | [#40746](https://github.com/qgis/QGIS/issues/40746) | [Commit 13fbcd1c](https://github.com/qgis/QGIS/commit/13fbcd1cff3dfa31a7c592566de9d2f5be1cf965) | No apropiado |
| \[processing\] Add commands to qgis_process tool to enable or disable plugins from the command line | [#41218](https://github.com/qgis/QGIS/issues/41218) | [Commit d140970](https://github.com/qgis/QGIS/commit/d1409703fbc1eff1c80cc0895e53e2764f332e92) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir la transparencia de las capas de ImageServer añadidas a través del navegador | [#41126](https://github.com/qgis/QGIS/issues/41126) | [Commit 9fb554f](https://github.com/qgis/QGIS/commit/9fb554fde0348c3a78aad6070c6c83986e5470ab) | No apropiado |
| \[server\] Just skip any broken projects on the landing page, instead of blocking the whole landing pag | no reportado | [Commit e4a4b83](https://github.com/qgis/QGIS/commit/e4a4b832dff47e552271c8b024eb8105b88483cb) | No apropiado |
| Actualizar automáticamente el lienzo del mapa y los diseños si se establece en un src de usuario y el usuario cambia esa definición de src | no reportado | [Commit ea57cfe](https://github.com/qgis/QGIS/commit/ea57cfea1ff4320b2bd6b7e6be5aea699bdeabe3) | No apropiado |
| Don\'t show duplicate \"source\"/\"path\" rows for local files | no reportado | [Commit 8aa9c6a](https://github.com/qgis/QGIS/commit/8aa9c6a142523aed85ce74d70b93c04553e13dc0) | N/D |
| Corregir la recuperación de los resultados de sql de los geopackages | [#40856](https://github.com/qgis/QGIS/issues/40856) | [Commit f65fe3d](https://github.com/qgis/QGIS/commit/f65fe3dbc95a7f38b24271e9fb979eed68823cff) |  |
| Don\'t default to input field for optional expression parameters | [#41063](https://github.com/qgis/QGIS/issues/41063) | [Commit 1fed902](https://github.com/qgis/QGIS/commit/1fed9020a21a3f3deb9cece03ebb533aeae8c6a2) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| \[layouts\] Always update label after text changes | [#40203](https://github.com/qgis/QGIS/issues/40203) | [Commit 5d14c61](https://github.com/qgis/QGIS/commit/5d14c61f224e0f3621f701f96aa499ab355e1888) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Arreglar las propiedades relacionadas con el símbolo de relleno (como los filtros de anillo) que se muestran para los símbolos de línea en algunos contextos. | [#33398](https://github.com/qgis/QGIS/issues/33398) | [Commit 9cba248](https://github.com/qgis/QGIS/commit/9cba2489bcde55ee6e072dc7690ff2401928c507) | No apropiado |
| Asegurar de que el dock de estilo de capa se actualiza al cambiar los elementos de la leyenda a través del menú del árbol de capas | [#40630](https://github.com/qgis/QGIS/issues/40630) | [Commit 457d661](https://github.com/qgis/QGIS/commit/457d6618ad6e9843b785854cf85ab5a0b815cd8c) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Se corrige la representación de la capa de símbolos del marcador de campo vectorial cuando se gira el mapa. | [#40916](https://github.com/qgis/QGIS/issues/40916) | [Commit 157bdca](https://github.com/qgis/QGIS/commit/157bdcab884dde6523e78897ec1a8618a26b6d06) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir la capa de símbolos de líneas de marcadores que representa los vértices de las versiones segmentadas de las geometrías curvas en lugar de los vértices reales | [#39750](https://github.com/qgis/QGIS/issues/39750) | [Commit 71090b0](https://github.com/qgis/QGIS/commit/71090b077f6968eef2c428d2de74c63c78f3f3a1) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Corregir la decoración de la barra de escala utiliza la extensión incorrecta del mapa al restaurar un proyecto | [#40748](https://github.com/qgis/QGIS/issues/40748) | [Commit f1ea5a9](https://github.com/qgis/QGIS/commit/f1ea5a9c560eaba6f3947cc8447d6f25226c2b5d) | [Commit 6b1e67d](https://github.com/qgis/QGIS/commit/6b1e67dd947e41359a7ad3d1a8f44ef1ec20b442) |
| Corregir la falta de identificación de los resultados de los elementos del menú del botón derecho para los tipos de capas no vectoriales | no reportado | [Commit 176e972](https://github.com/qgis/QGIS/commit/176e9728c5ebb24f309369878664c2c49dc6eb16) | No apropiado |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
