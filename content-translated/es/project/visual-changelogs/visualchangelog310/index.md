---
HasBanner: false
draft: false
releaseDate: '2019-10-25'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 3.10
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 3.10{#changelog310 }
![image1](images/projects/ce6ba8fc893e51ec721c9dded4dd98d11806a223.png)

Fecha de lanzamiento: 2019-10-25

QGIS 3.10 contiene una gran cantidad de cambios nuevos y mejoras en algunas de las herramientas existentes - intentaremos cubrir aquí lo más destacado. Como siempre queremos recordarte que QGIS es un proyecto de código abierto y si te es posible, considera apoyar nuestro trabajo con donaciones o contribuciones a la documentación del código, sitio web y demás. 

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, testers y a toda la gente ahí fuera que dedica su tiempo y esfuerzos (o financia a personas para que lo hacen). ¡Desde la comunidad de QGIS esperamos que disfrutes de este nuevo lanzamiento! Si deseas donar tiempo, dinero o participar de cualquier otra forma para hacer QGIS más impresionante, ¡por favor ve a qgis.org y echa una mano!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

{{<fund type="active" >}}

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## Herramientas de mapa
### Prestación: Las longitudes 3D de lineas ahora se muestran en los resultados de la herramienta de identificación.
Al usar la herramienta de identificación de objetos espaciales en una linea 3D ahora se incluye la longitud 3d cartesiana de la linea en los resultados (junto a las longitudes cartesiana 2d y elipsoidal 2d ya existentes).

![image2](images/entries/b1aba6e9334ee1d862bde8f66f9ae4d30d945703.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Simbología
### Funcionalidad: Configuración de remuestreo por defecto para capas ráster.
In QGIS 3.10 we\'ve added a new setting for the default resampling mode to use when for newly-added raster datasets. (This setting can be found in the rendering panel of the options dialog).

![image3](images/entries/07ae51e244cc5b1d6a971e386ea98f1314a3dfb1.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Mejorado el copiado y pegado de símbolos
We\'re passionate about making QGIS a user-friendly cartographic tool which is a joy to work with, so we\'ve added a bunch of new shortcuts throughout the interface which allow you to copy and paste symbols from one part of QGIS to another. E.g, you can copy a symbol from a category and paste it directly onto another category, or a layout shape item, or inside the style manager dialog!

![image4](images/entries/79f8365571da7b6c60f001f388d9c02d9e8920b2.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \"Center of segment\" placement mode for marker and hash line symbol layers
We\'ve added a brand new \"Center of segment\" mode for placement of marker line or hashed lines symbols. This allows you to place markers or hash lines over the center point of individual line segments, exposing cartographic effects which were not possible before (and improving the quality of layers converted from ArcMap using the [SLYR](https://north-road.com/slyr/) tool).

![image5](images/entries/c1f50067d50b909e38b7333ad5d8d415e763801d.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Desplazamientos definidos mediante expresiones más flexibles
In previous QGIS releases, only string values of the format \'x,y\' would be permitted for data-defined symbol and label offsets. We\'ve listened to user feedback that this was confusing, and in QGIS 3.10 we now allow arrays of numbers as a valid expression result for offsets. E.g. \"array(3,5)\".

![image6](images/entries/1ccab8f4328238f5275e41c3d466bf27a5d097a2.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Etiquetando
### Funcionalidad: Crear y gestionar formatos de texto y opciones de etiquetado en los estilos de QGIS
In QGIS 3.10 we\'ve finally implemented a long-awaited feature, allowing users to manage their own libraries of custom text formats and label settings alongside their existing symbol libraries!

Now, the Style Manager dialog can be used to manage text formats (which store the font, color, buffers, shadows, and backgrounds of text formats) and layer-wide label settings. (A \"text format\" includes just font settings and other appearance related settings, while a \"labe setting\" also includes layer-type specific settings such as label placement, priority, and rendering settings).

Text Formats and Label Settings offer all the same functionality as you\'re used to for managing symbols and color ramps within styles, including import and export to XML files, tagging, smart groups, favoriting etc\...

![image7](images/entries/bf657c21ba6deaff10ff80611a77b435e12155e5.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [North Road](http://north-road.com)
### Funcionalidad: Símbolos de tipo marcador para fondos de etiquetas
Alongside all the other exciting labeling improvements which we\'ve landed in 3.10, we now allow use of marker symbols as a background for labels. This allows you to use all the rich functionality available for marker symbols as a background to labels, and complements the existing shapes and SVG background choices!

![image8](images/entries/3a9fd11192cdbdaa2f139a28d63cc33e1d10c3bc.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [North Road](http://north-road.com)
### Funcionalidad: "Llamadas" para etiquetas
A common practice when placing labels on a crowded map is to use \'callouts\' - labels which are placed outside (or displaced from) their associated feature, with a line connecting the label and the feature. In QGIS 3.10, we\'ve added native support for quickly and easily creating beautiful label callouts (no more expression mangling or drawing by hand!).

We\'ve added many settings for controlling exactly how these label callouts are drawn, and naturally, you can take full advantage of the richness of QGIS line symbol support within your callouts! This includes all the existing line symbol styles, layer effects, and even support for data-defined settings!

In 3.10, we expose options for either a \"simple\" (direct line) or \"Manhattan\" (straight lines) callout styles. If you\'re interested in sponsoring additional callout styles in a future release, get in contact with the QGIS team to find out how you can make this happen!

![image9](images/entries/7bcc02d06eb7030a289e129b9bed2656d6c6fefb.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Cambiar la alineación para etiquetas con múltiples lineas para etiquetas individuales
We\'ve added an additional option to allow you to control multi-line alignment on a label-by-label basis. Just active the Label Properties tool and click on your map labels, and a new setting for the text alignment is now available.

![image10](images/entries/14b307efef5de1085e4c402d3e06e5dd10a64ae2.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Mostrar etiquetas no colocadas
If you\'ve ever been concerned about automatic label placement hiding away important labels on your map \-- this feature is for you! In QGIS 3.10 we\'ve added an option to show \"Unplaced labels\" on your map, so you can see immediately exactly what\'s been hidden from view (AKA \"see what others can\'t\")!

This new setting (which is accessed through the Labeling toolbar) will render these Unplaced Labels in a red color (but the color can be changed from the project Label Settings dialog). After identifying any missing labels in your map, we suggest you use the existing Labeling tools such as the \"move label\" or \"show/hide label\" tool to rearrange your map and make these labels visible again.

![image11](images/entries/4e53a6482dacb6e2d6d1ff2a8c4592d98f82430a.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Exceder la distancia para etiquetas de lineas
We understand that making a cartographic masterpiece is a demanding task, so in QGIS 3.10 we\'ve extended the capabilities of curved labels by adding a new \"overrun distance\" setting. This setting allows you to control exactly how far a curved label is allowed to extend past to ends of a line feature. Bumping up the distance will result in giving the labeling engine more flexibility in placing your labels, resulting in more labels being placed in better locations on your map! Win! The setting works for both curved and parallel label modes, and supports distances in mm/map units/pixels/etc, and data-defined distances.

![image12](images/entries/0b830e5ea769aacfd9c5bf9d8028ed278590d803.gif)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Data defined control for \"label every part of multipart features\" setting
The \"label every part\" option was one of the very few settings which couldn\'t be previously data-definable for labels. We\'ve remedied this omission in QGIS 3.10, and you can now control whether you want all parts labelled on a feature-by-feature basis!

![image13](images/entries/9db2c54c0d65bc61da8c0c46cfefcbab96c833df.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: Control \"label all parts\" via the label properties tool
We aren\'t lying when we say that QGIS 3.10 is a love-letter to map labelling! Another new option we\'ve added in this version is interactive control over whether all parts of a feature should be labeled via the Label Properties tool.

![image14](images/entries/737cd2f8bc569ee9ad7df9aee02eec83b4e6facd.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Orientación vertical para texto
A partir de la versión 3.10, QGIS está completamente equipado para dibujar etiquetas orientadas verticalmente. Para nuestros usuarios chinos, japoneses y coreanos: ¡corre la voz! :)

Puedes elegir dos modos de orientación vertical: uno que siempre dibuja las etiquetas verticalmente, o un modo alternativo, que dinámicamente selecciona la orientación basándose en la rotación de la etiqueta.

![image15](images/entries/e49baccdb83da1b88433e2c7718642ae4a78810d.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Control sobre el interletraje de la fuente
Another option we\'ve added for improving the conversion of ArcMap symbology to QGIS (via [SLYR](https://north-road.com/slyr/)) is a new setting for controlling whether label fonts are kerned (or not).

![image16](images/entries/b2a650a874e263173a56d93b046df7f031eb8d6e.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Representación
### Funcionalidad: Dibujado de capas ráster fuera de la extensión reportada
Depending on the server technology used, sometimes the map extent reported by raster layers may be smaller than the actual area which can be rendered (especially notably for WMS servers with symbology which takes more space than the data extent). Previous version of QGIS would crop raster layers to the reported extents, resulting in truncated symbols on the borders of these layers. Now, there\'s a new option to allow you to override this behaviour and ignore the reported extent for affected servers.

Esta funcionalidad fue desarrollada por Matthias Kuhn (Opengis.ch) 
### Funcionalidad: Georreferenciar PDFs y TIFs cuando se guarda el lienzo del mapa como imagen o PDF
In QGIS 3.10 we\'ve implemented support for embedded georeferencing within PDFs and TIFs when using the save \[map canvas\] as image or PDF.

![image17](images/entries/1030adf0c9c0c46ff5a38a09ae16a735bdff3684.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Nueva ilustración con imagen para el lienzo.
We\'ve added a brand new decoration for the QGIS main canvas, allowing you to add a bitmap and SVG image overlay (logo, legend, etc.) to your map window.

Como en otras partes de QGIS, la decoración permite utilizar relleno personalizado y color del borde para SVGs con parámetros habilitados.

![image18](images/entries/41ab256b477b0baf0971b398f882a6633cd12615.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Clasificación mediante escala logarítmica
Ahora puedes utilizar una escala logarítmica cuando crees rangos para el estilo graduado.

![image19](images/entries/bb6303d9589972781988549283ef150700ba5863.webp)

This feature was developed by [OPENGIS.ch](https://www.opengis.ch)
## Objetos 3D
### Funcionalidad: Herramienta de medición en vistas del mapa 3D
Now you can measure distances in 3D map views! This new tool is available in the 3D map view toolbar, and has the same workflow as the 2D measurement tool (with the same configuration settings of rubber band color, units, decimal place, etc). It also has the same behavior (left-click to add a new point, middle-click to delete the last point, and right-click to restart the measurement). This allows you to measure distances in 3d, e.g. the distance between two building's roofs or the length of a river running down a mountain. See the 3D measurement tool in action:

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
### Funcionalidad: Estilo tipo cartel para puntos
Hemos añadido un nuevo tipo de estilo para capas de puntos. Permite mostrar un punto con un símbolo de QGIS (e.g. marcador, SVG, etc) que siempre mira hacia el usuario y siempre tiene el mismo tamaño. Puedes ver un ejemplo de uso en el video.

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
### Funcionalidad: Navegación 3D en pantalla
En anteriores versiones de QGIS, ya podías navegar el mundo 3D usando el teclado y el ratón. Desafortunadamente, para nuevos usuarios, no es fácil empezar a utilizarlos. La navegación 3D en pantalla ayudar a movernos por el mundo 3D. Hay botones para alejar y acerca el zum, movernos arriba/abajo/izquierda/derecha, y rotar la vista 3D del mapa. Esta funcionalidad puede ser activada desde la barra de herramientas de la vista de mapa 3D. Observa como se usa en este video:

![image20](images/entries/570ff6f8c365a78d05bb56cfdbd8647f83aac331.webp)

This feature was funded by [Google Summer of Code Program](https://summerofcode.withgoogle.com/projects/#5265985207009280)

This feature was developed by [Ismail Sunni](http://ismailsunni.id)
## Diseño de impresión
### Funcionalidad: Ordenado de elementos de la leyenda de derecha a izquierda
Thanks to funding from our right-to-left locale users, we\'ve added a new choice for arrangement of legend elements. These include symbols to the left OR symbols to the right of the legend text, and alignment options for groups, subgroups and item text.

Esta funcionalidad permite la creación de leyendas en idiomas con escritura de derecha a izquierda. Para hacer las cosas más sencillas para el usuario, hemos hecho que este estilo de alineación sea por defecto para idiomas con escritura de derecha a izquierda. 

![image21](images/entries/420b784c4fc79a09358201c8814cfe48b82dbbca.webp)

This feature was funded by [Kaplan Open Source](https://kaplanopensource.co.il/)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Controlar el margen bajo los encabezados de grupo y subgrupo en leyendas.
If you\'re after pixel-perfect control over your legend appearance \-- this one\'s for you! QGIS 3.10 now allows you to tweak the spacing applied under group or subgroup headings.

![image22](images/entries/78263d3350afd05147928378f81dddba13961acc.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Opciones definidas mediante datos en formatos de texto
Since so much of QGIS\' cartographic power comes from the flexibility of data-defined symbol settings, we\'ve now allowed them to be used for text formats too! This means you can now use data defined properties wherever text formats are used, e.g. within layout scalebar text.

![image23](images/entries/69961f6faa732b683ccfb1ab539250b21ea5bd26.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: \@scale_value variable
To complement the new support for data-defined settings within text formats, we added a new \@scale_value expression variable. This can be used when evaluating data defined text format properties while rendering scale bar text, and ultimately allows you to have per-label customisation of the text format inside scale bars (e.g. showing certain distance labels in bold).

![image24](images/entries/ec2940b4222b8172403b20b0f70af0588c38f0cc.gif)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Opciones para la colocación de escalas gráficas
We\'ve extended layout scale bars with additional styling options, adding a pair of settings to refine the placement of scalebar labels. Now you can define whether labels are shown above or below the scalebar itself, as well as setting whether labels are centered in the middle of a segment or placed at its end.

![image25](images/entries/e571fc1811ccf58e007a7913600b65377e31ed41.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Simplificar PDF o SVG exportados
En versiones anteriores de QGIS se generaban PDFs ( o SVG) gigantes,  ya que estos archivos contenían muchos vértices redundantes que no eran distinguibles a los DPI definidos en la exportación. Ahora, por defecto, aplicamos una simplificación cuando se escriben los archivos PDF o SVG, lo que causará que se simplifiquen las geometrías y eliminando automáticamente vértices redundantes (e.g. si tenemos 300 dpi, vértices estén a menos de 0.004 cm serán eliminados). 

This new setting, \"Simplify geometries to reduce output file size\", is exposed in the SVG or PDF export settings dialogs shown when exporting a layout/atlas/report to PDF or SVG.

No more ridiculously complex and large export file size for your QGIS print layouts! Aside from the file size issues, these also cause problems when trying to load into other applications, e.g. Inkscape, which chokes on the huge number of vertices and grinds to a crawl\.... ouch!

![image26](images/entries/7eea84e316a148c6872369d3df5fb63a6bc2f043.webp)

Esta funcionalidad fue financiada por el GeoPDF export group: Land Vorarlberg; Cantones de Zug, Thurgovia yNeuchâtel; Ciudades de Viena y Dornbirn; Biodiversity Information Service for Powys y Brecon Beacons National Park

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Mejora de la exportación de SVG por capas
User feedback told us that the way we created layered SVG files in past releases was frustrating to work with. So, in QGIS 3.10, we\'ve revamped this feature and now SVG layer names will match the layer names from QGIS, making it much easier for designers to understand the contents of the document! Read more about this are related features [here](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/).

![image27](images/entries/dac35ad47f56dd24456df6d318359a0d70efeb15.webp)

Está funcionalidad fue financiada por el GeoPDF export group 

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Indicador de re-dibujado en el diseñador de impresión
In earlier QGIS releases, there was no way to tell whether a map refresh had finished inside a QGIS print layout designer window. So, we\'ve added a new indicator in the status bar which shows whenever there\'s a redraw is humming away in the background. No more user confusion!

![image28](images/entries/8c6426a723b9fdc1cead1949f3304db4763ecb9c.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Exportación a GeoPDF
If you export PDF\'s from QGIS now, there is an option to export it as GeoPDF. If you open this PDF with a compatible PDF viewer, you will then be able to toggle layers on and off, pan and zoom around the PDF and interactively interrogate features! Futhermore, you can re-import these GeoPDF documents back into QGIS as vector layers, and see all the features in their original locations and with their original attribute values.

GeoPDF export is available for either print layouts or map canvas exports. We\'ve added lots of flexibility to this new option, e.g. with options for controlling which layers will be exported as interactive layers. You can even choose to export multiple map themes into a single GeoPDF document, so that your readers can interactive switch between these themes! (Wow!)

Nota, la exportación a GeoPDF requiere que QGIS haya sido compilado con GDAL 3.0 o posterior.

Read more at [QGIS 3.10 Loves GeoPdf](https://north-road.com/2019/09/03/qgis-3-10-loves-geopdf/)

![image29](images/entries/9f73cce9c3f3ff81c6b66adab654ff4e23524ae1.webp)

Esta funcionalidad fue financiada por el GeoPDF export group: Land Vorarlberg; Cantones de Zug, Thurgovia yNeuchâtel; Ciudades de Viena y Dornbirn; Biodiversity Information Service for Powys y Brecon Beacons National Park

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Prestación: Control de propiedades de cuadrículas mediante datos
We\'ve added data defined control over layout map grids, to give you extra flexibility in the appearance and behaviour of these grids, and to allow you to create layout templates and atlases with grids which dynamically respond to map scale changes.

Now, you\'re able to set data-defined control for:
- Estado de activación de la cuadrícula
- Intervalos x/y de la cuadrícula
- Desplazamientos en x/y de la cuadrícula
- Tamaño de marco y margen de la cuadrícula
- Distancia de las anotaciones al marco de la cuadrícula
- Tamaño de las cruces de la cuadrícula
- Grosor de la linea del marco de la cuadrícula

![image30](images/entries/e219a18e997a6506314c1777c94050bf4a69cf9b.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: tamaño de los segmentos de la cuadrícula dinámicos
Just like the existing scalebar setting of the same name, this new setting allows you to set a page-size-based range for map grid intervals. The grid interval will be dynamically calculated based on the map extent and scale to pick the largest possible \"pretty\" interval which results in grid sizes inside the desired range.

Este cambio hace posible que puedas generar composiciones y plantillas para el diseñador de impresión con cuadrículas que responden elegantemente a una amplio rango de escalas del mapa.

![image31](images/entries/245ada907ba2e14ad291dae54b93adb327b64225.webp)

Esta funcionalidad fue financiada por Andreas Neumann

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Marcadores espaciales para composiciones de mapas
Another long-requested feature we\'ve implemented for QGIS 3.10 is a new button in the layout map item properties toolbar, which allows you to directly set a map item to the extent of a spatial bookmark!

![image32](images/entries/4b8ed681a38435a2f0bf299fd28f299e2873848c.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## Expresiones
### Prestación: Nuevas funciones de expresión
- **attributes()**: returns a map containing all attributes from a feature, with field names as map keys. We\'ve got flexible, robust support for working with map values in expressions now, so this allows rapid conversion of all feature attributes to a map to use with these handy functions!
- New optional \"format\" parameters were added to the **to_date**, **to_datetime**, and **to_time** functions
- | **collect_geometries**: this new function collects a set of geometries into a multi-part geometry object. Geometry parts can either be specified as separate arguments to the function or (more flexibly), as an array of geometry parts. This function allows geometries to be generated using iterator based approaches, such as transforming an array generated using generate_series, e.g: | `collect_geometries( array_foreach( generate_series( 0, 330, 30), project($geometry, .2, radians(@element)) ) )` | Gives a nice radial effect of points surrounding the central feature point when used as a MultiPoint geometry generator
- A new **make_line** expression function variant which accepts an array of points. This allows creation of lines from variable numbers of points, and from sequences from aggregates/dynamically generated sequences.

## Digitalizando
### Funcionalidad: Soporte para tiempo GPS
We\'ve overhauled the existing GPS based functionality in QGIS 3.10, adding new options for automatically retrieving and storing GPS timestamps alongside GPS based features.

This feature was funded by [NIWA](https://niwa.co.nz/)

This feature was developed by [Alessandro Pasotti (North Road)](http://north-road.com)
### Funcionalidad: Excepciones permitidas en huecos
In QGIS 3.4 we introduced the ability to configure QGIS layers to run topological checks on every save operation. For 3.10, we have now added a new option to the check for \"gaps\" which allows you to actively mark some gaps as allowed. These exceptions will be saved on a separate, configurable layer. Whenever a gap is detected, you either have the possibility to fix it or to add it to the allowed exceptions with the press of a button.

![image33](images/entries/4a7b306942755ac96cfa9bc97abbfd7815d17ad4.webp)

This feature was funded by [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Administración de datos
### Funcionalidad: Claves foráneas compuestas
In QGIS 3.10, we added the possibility to create layer relationships which utilise composite foreign keys. QGIS now fully supports editing parent and child features which are linked with more than one attribute. This functionality is accessed in the Project Properties -\> Relations tab.

![image34](images/entries/6b2177a5781bc2d5cdfb63f121501a734897e4a1.webp)

This feature was funded by [California Geological Survey](https://www.conservation.ca.gov/cgs)

This feature was developed by [OPENGIS.ch](https://www.opengis.ch)
### Funcionalidad: Añadir dependencias circulares de datos
¿Alguna vez has tenido problemas con el autoensamblado al editar un objeto que es modificado por alguien más (o un molesto trigger de la base de datos)? Las dependencias de datos permiten actualizar el contenido de las capas dependientes cuando se modifican los datos. Hemos mejorado el soporte para dependencias en QGIS permitiendo actualizar la propia capa modificada, lo que es como una dependencia circular (una capa de puntos y una capa de lineas que dependen una de la otra por ejemplo). No más autoensamblado en objetos "fantasma".

More info in the [pull request](https://github.com/qgis/QGIS/pull/30947)

![image35](images/entries/3b93e7b25eef3e3f149ba8db022e467258a74116.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Widgets y Formularios
### Funcionalidad: Actualizar widgets dependientes en tiempo real
Actualiza valores un widget en tiempo real al editar los campos referenciados. Cuando un widget A contiene un valor por defecto que depende de un widget B, se actualiza en cuanto el widget B es editado.

![image36](images/entries/0f24e8e2746cb4b7890d015c2ae476f1f1bf96ef.webp)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
## Herramientas de análisis
### Funcionalidad: Expresiones de filtrado almacenadas para tablas de atributos.
While previous versions of QGIS allowed you to filter attribute tables using a custom expression, these expressions were lost whenever the attribute table was closed. Now, we\'ve added the ability to store and manage your custom expression filters to the attribute table dialog. You can now build up your own personal collection of useful filters, which will always be available for re-use with a few simple mouse clicks!

![image37](images/entries/d6791d32d649fdc3b2e86aa257a33796391e13e0.webp)

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-3854-DE.html)

This feature was developed by [David Signer (OPENGIS.ch)](https://www.opengis.ch)
### Funcionalidad: Nuevos operadores para la calculadora ráster
You ask, we listen: `abs` , `min` and `max` are now available in the Raster Calculator user interface!

![image38](images/entries/8a0081e087a6f9ff9180615f34bb56ea6dccc649.webp)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Procesado
### Feature: New algorithm \"Point to layer\"
Este algoritmo crea una nueva capa vectorial que contiene un única geometría coincidente con un parámetro puntual. Puede ser utilizada en modelos para convertir una entrada de tipo punto en una capa, que puede ser utilizada por otros algoritmos que requieran una entrada de tipo capa.

![image39](images/entries/9f61759f0b8d6a61ea070a5328c4f641c582778e.webp)

Esta funcionalidad fue desarrollada por Olivier Dalang
### Funcionalidad: Parámetros avanzados de modelos 
When creating inputs for a Processing model, you can now mark these input parameters as \"Advanced\" options. (Advanced parameters are hidden by default when users run your model through the Processing toolbox)

![image40](images/entries/d9224e26da62b092d56fd091195942d4142e9bd7.webp)

Esta prestación fue desarrollada por Alex Bruy
### Feature: All GDAL based algorithms now support free-form \"additional parameters\"
We added an optional \"Additional command-line parameters\" parameter to all GDAL algorithms , useful for cases when you need to pass a specific command-line argument(s) which is not exposed in the algorithm UI.

![image41](images/entries/18f42d184246ed167be10dee72f5000671d7ac01.webp)

Esta prestación fue desarrollada por Alex Bruy
### Funcionalidad: Tamaño del "Metatile" para teselas XYZ
Ahora puedes especificar un tamaño de metatile personalizado cuando generes teselas XYZ. Valores más grandes permiten acelerar el dibujado de las teselas y proveen mejor etiquetado (menos huecos sin etiquetas) a expensas de utilizar más memoria.

![image42](images/entries/471f15d2616ffc1531c8eef95d4d8ed87d161998.webp)

Esta prestación fue desarrollada por Martin Dobias
### Funcionalidad: Nuevo tipo de parámetro para colores
QGIS 3.10 incluye un nuevo tipo de parámetro para usar en modelos de Procesos y scripts, que permite a lo usuarios seleccionar un color. ¡Útil para cualquier modelo y algoritmo que requiera un color como entrada!

![image43](images/entries/87cae0401b93aa308c156a615e63a71e98d25980.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Create style database from project\"
Este algoritmo extrae todos los objetos de estilo (símbolos, rampas de color, formatos de texto y opciones de etiquetas) de un proyecto de QGIS y los almacena en una nueva base de datos de estilos en formato XML, que puede ser posteriormente gestionado e importado a través del menú de Gestión de estilos.

![image44](images/entries/8d6075eb1c4fc38b76f9761836048e940be408f8.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Filtro para archivos y valores por defecto para entradas de tipo archivo o carpeta en modelos
For file or folder inputs in Processing models we\'ve added a new file filter setting (with some standard file formats available as an optional preset), and now allow you to set a default value for these inputs.

![image45](images/entries/94fe90f54308a81c5f031066c132e1ad5e8e6ac2.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Combine style databases\"
The new \"Combine style databases\" algorithm combines multiple QGIS style databases into a single output style database. If any symbols exist with duplicate names between the different source databases these will be renamed to have unique names in the output combined database. It\'s designed to give users an easy way to condense multiple separate style databases into a single unified database.

It works brilliantly with results generated by running the \"Create style database from project\" in a batch mode!

![image46](images/entries/479f2a711f8c4b254e72348eda3c79187d4117f2.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Generar teselas XYZ usando múltiples hilos
El algoritmo para generar teselas XYZ ha sido optimizado y ahora puede generar las teselas usando múltiples hilos de procesamiento.

![image47](images/entries/60aac076d447f244dd232a8e8766a109032a9540.webp)

Esta funcionalidad fue desarrollada por Isghj5
### Funcionalidad: Nuevos algoritmos para exportar e importar marcadores desde/a capas del mapa.
To complement the spatial bookmark overhaul in QGIS 3.10, we\'ve added new Processing algorithms which allow you to create a bunch of new bookmarks corresponding to the features from a layer, or to export existing spatial bookmark extents to a new polygon layer.

![image48](images/entries/d0471bc7ea65e476537c8828a7850a64ca9120ef.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Feature: New algorithm \"Split features by character\"
Este nuevo algoritmo separa objetos en múltiples objetos, dividiendo el valor de un campo con el carácter especificado.

Por ejemplo, si una capa contiene múltiples valores separados por comas en un campo, este algoritmo puede usarse para separar estos valores entre varios objetos. Las geometrías y otros atributos permanecen sin cambios en el resultado.

Opcionalmente, para mayor flexibilidad la cadena de texto utilizada para separar puede ser una expresión regular.

This algorithm was designed for use in models which need to process input files with multiple concatenated values in a single attribute, e.g. geocoding a table with \"address1,address2,address3\" format strings.

![image49](images/entries/a0adf902641c8ace142d9749e632e114262342cd.webp)

This feature was funded by [SMEC/SJ](https://www.smec.com/en_au)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Nuevo algoritmo "Subir por una linea"
Previously available as a plugin, the \"Climb Along Line\" algorithm has been added to the out-of-the-box QGIS toolset. This algorithm calculates the accumulated height differences for lines in an input line layer, calculated using the Z values of the line vertices. A copy of the input line layer is returned with additional attributes for accumulated climb and descent, as well as the minimum and maximum Z values for each line.

![image50](images/entries/1b68212fa4a991c79f7d352b5ee3798d0e9a10a3.webp)

This feature was developed by [Håvard Tveite (NMBU) and Matteo Ghetta (Faunalia)](https://www.faunalia.eu)
### Funcionalidad: Portar el algoritmo Crear cuadrícula a C++
Hemos portado el algoritmo Crear Cuadrícula de Python a C++ con el objetivo de acelerarlo. El algoritmo ahora funciona mucho más rápido y además es capaz de crear retículas regulares con puntos/lineas/rectángulos/rombos/hexágonos en alta resolución en enormes extensiones (e.g. países enteros) en un tiempo razonable.

![image51](images/entries/6ef35bc88e69aaf92f5f223249bf792ffd4d28d5.webp)

This feature was funded by [Clemens Raffler](https://twitter.com/root676)

This feature was developed by [Clemens Raffler](https://github.com/root676)
## Navegador
### Funcionalidad: Extraer símbolos de proyectos de QGIS directamente desde el navegador
QGIS\' Browser panel just keeps getting more and more powerful! In 3.10, we\'ve added a new option when right-clicking a QGIS project within the browser: \"Extract Symbols\". Selecting this option opens a style manager dialog showing all symbols, color ramps, text formats and label settings from the selected project, allowing you to easily export the browse these symbols.

![image52](images/entries/4c9dd54203cbce44f91e85ed1ff01f1cbb4a40c5.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
## General
### Funcionalidad: Mostrar noticias en la página de bienvenida
Un feed de noticias curadas de QGIS ahora se muestra en la página de bienvenida. ¡Esto al fin nos proporciona un canal directo para enviar noticias del proyecto a TODOS nuestros usuarios! Espera ver muchas noticias, consejos, y eventos interesantes de QGIS.

![image53](images/entries/d3822539302bcd15ae05ef697abafaa1aa5c3ae4.webp)

Esta funcionalidad fue financiada por QGIS.org

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Miliradianes (definición SI) y unidades mil (OTAN)
QGIS 3.10 te permite medir ángulos en dos nuevas unidades, miliradianes (definición SI) y unidades mil (OTAN).

![image54](images/entries/f208b7c32bfe608a448dc2e9359de20e3e4397dd.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Personalización del interfaz filtrado de dialogos
We\'ve added a new \"search\" box to the Interface Customization dialog, which allows you to filter through the widgets and easily find the widget you are trying to customize\...

![image55](images/entries/57f395b303ba963e67242e0f2cfe7104e61f2ad0.webp)

Esta funcionalidad fue desarrollada por DelazJ
### Funcionalidad: Auto-reparar mejorado para capas no disponibles
Cuando la ruta de un archivo esta fijada en un proyecto, QGIS 3.10 intentará escanear automáticamente todas las rutas rotas e intentará reparar automáticamente cualquier otra que estén apuntando a la misma ruta original rota. ¡Cualquier cambio que permita arreglar capas rotas más rápidamente es un cambio bienvenido en nuestra opinión!

![image56](images/entries/0119e6f0b3d950d613d224d7bbd53a38575b3579.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: ¡Marcadores espaciales sobrealimentados!
We\'ve totally revamped how spatial bookmarks are exposed and managed in QGIS 3.10. Spatial Bookmarks are now shown in the browser panel, and can be regrouped into custom, categorized folders. This offers a much easier way to navigate and manage your bookmarks.

También hemos añadido un nuevo menú de edición de marcadores, que contiene un editor de extensiones que facilita en gran manera la edición de los marcadores.

Los marcadores ahora pueden ser arrastrados y soltados en lienzos, permitiendo que lienzos secundarios se centren en un marcador en particular. Esto permite que los marcadores funcionen bien en proyectos con múltiples lienzos., ya que pueden ser soltados en un lienzo específico para hacer zum.

![image57](images/entries/8329961bfa04631c5a970888f9a21bad66ddc6fa.webp)

Esta funcionalidad fue desarrollada por Mathieu Pellerin, Nyall Dawson
### Feature: \"Reselect Features\" action in Edit -\> Select menu
Ever spend 10 minutes painstakingly creating an interactive selection of features, only to accidentally deselect them all through an errant mouse click? If so, this feature is designed just for you! Now, you can restore a layer\'s selection following a selection clear operation via the new \"Reselect Features\" option in the Edit menu.

![image58](images/entries/e1234a3ca30866b91f64f97b83fdf0fb90838cb6.webp)

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Paralelizar la creación de índices de autoensamblado
La idea era para cada capa el cálculo del caché de autoensamblado (secuencial en aquel momento) y hacerlo no bloqueante. Como consecuencia de esto es posible seguir usando QGIS incluso si el caché de autoensamblado se está generando al mismo tiempo. El usuario puede, por ejemplo, empezar a editar un nodo mientras la creación del caché está en proceso.

Esta funcionalidad fue desarrollada por Oslandia
### Funcionalidad: Plantillas para proyectos de QGIS
QGIS 3.10 incluye la posibilidad de usar plantillas de proyectos directamente desde la página de bienvenida. Además ahora puedes enviar plantillas de proyectos a toda tu organización colocándolas en una carpeta de sistema, junto con la posibilidad ya existente de colocarlas en la carpeta de tu perfil de usuario.

![image59](images/entries/5adaa5a973e0b232bae3a8dbab8739c8887ac70e.webp)

This feature was funded by [The QGIS Project](https://www.qgis.org)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Proveedores de datos
### Funcionalidad: Soporte de lectura-escritura para formatos .shz y .shp.zip
For QGIS builds based on GDAL 3.1, you can now open and edit single-layer ZIP compressed shapefiles (.shz), or multi-layer ones (.shp.zip). Regardless of where you sit on the Shapefile vs Geopackage battle, you\'ll welcome this ability to de-clutter your folders and store shapefiles as a single file!

Esta prestación fue desarrollada por Even Rouault
### Funciones: autenticación para bases de datos Oracle
We\'ve updated the Oracle database provider to add full support for QGIS built-in authentication system.

Esta prestación fue desarrollada por Jürgen Fischer
### Funcionalidad: Mejorado el soporte para ráster de PostGIS
Las capas ráster de PostGIS ahora se muestran en el panel del Navegador y el menú del Administrador de fuentes de datos, permitiendo que gestiones y añadas fácilmente estás capas a tus proyectos. Actualmente solo soporta la lectura desde el Navegador - no puedes arrastrar rásters a una base de datos PostGIS desde el Navegador.

Esta funcionalidad fue desarrollada por Alessandro Pasotti
### Funcionalidad: Oracle - soporte para transacciones con bases de datos
For version 3.10, we\'ve enhanced the Oracle database provider and added support for editing layers via transactions.

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Dimensiones Z/M en capas de texto delimitado
We\'ve added optional support for Z and M fields to QGIS\' delimited text provider, allowing you to create Z or M enabled layers directly from CSV files.

![image60](images/entries/bfaa5fc4c03d27e5345475172f5e7bdb20a4f6ff.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Funcionalidad: Proveedores de datos estáticos
Una enorme trabajo, tras bambalinas, que hemos completado en QGIS 3.10 es refactorizar la infraestructura de proveedores de datos. Ahora, los proveedores permiten enlaces tanto estáticos como dinámicos. Esto era un prerequisito para poder construir librerías de QGIS en plataformas que no soportan enlaces dinámicos (iOS), ¡y permite a herramientas basadas en QGIS, por ejemplo la app de recolección de datos Input, que sea distribuida en dispositivos basados en iOS!

This feature was funded by [Lutra Consulting Ltd.](http://www.lutraconsulting.co.uk)

This feature was developed by [Peter Petrik, Martin Dobias](http://www.lutraconsulting.co.uk/about)
## Servidor de QGIS
### Funcionalidad: Uso de SVG en QGIS Server
Earlier QGIS server versions had rendering issues when remote SVG files were used in a project (e.g. those hosted via external http servers). We\'ve improved how QGIS Server fetches these resources, and it\'s now possible to use remote SVG paths in your layers and publish them as WMS without rendering issues in QGIS Server.

![image61](images/entries/71d731c71f864fcb542f2f7ec52c68e4c03068d3.webp)

This feature was funded by [Ifremer](https://sextant.ifremer.fr/)

This feature was developed by [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Funcionalidad: Dimensiones en WMS
En QGIS 3.10 un servidor WMS puede proveer soporte para varios tipos de dimensiones, tales como, tiempo, elevación o otro tipo de dimensiones. La dimensión tiene que ser definida a nivel de la capa y puede ser usada por el cliente WMS para filtrar la información solicitada. WMS tiempo es parte de WMS dimensión.

![image62](images/entries/45744c5a4a4c94e1c71a91bcfa7b672333002e75.webp)

This feature was funded by [Ifremer](https://sextant.ifremer.fr/)

This feature was developed by [René-Luc D\'Hont (3Liz)](https://www.3liz.com/)
### Funcionalidad: Soporte para Servidor OAPIF (aka WFS3) 
QGIS 3.10 Server is one of the very first geospatial servers which supports the new [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) standard (also known as WFS3)!

Esta es una implementación completamente nueva que provee un servicio basado en HTML y JSON para tus desarrollos de cartografía web, incluyendo un simple interfaz WebGIS que está disponible listo para usarse y es fácilmente personalizable a través de un sistema de plantillas HTML.

More information is available in the [documentation](https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/services.html#wfs3-ogc-api-features)

![image63](images/entries/81af9beefcd8522ecc0f953b2a6b9b4895e35675.webp)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Programabilidad
### Funcionalidad: Nueva clase QgsBookmarkManager
Junto con QgsProject y QgsApplication, esta nueva clase provee un método estable y soportado para gestionar marcadores de proyecto y globales (en comparación con el antiguo y no documentado enfoque de manipular directamente claves de proyectos o una base de datos sqlite). ¡Ahora tus complementos son capaces de leer, modificar y gestionar marcadores espaciales!

This feature was funded by [North Road](http://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](http://north-road.com)
### Funcionalidad: Nueva API para el proveedor de conexiones a bases de datos
Thanks to funding from the QGIS grant program, you can now use a [new API](https://github.com/qgis/QGIS/pull/31190) aimed to manage DB connections in a unified way. The new connection API also provides a set of useful methods that can be used by plugin authors to access information about tables, schemas etc. and to run SQL arbitrary queries and get the results back into a handy Python array.

Esta funcionalidad fue financiada por QGIS

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net)
## Correcciones Notables
### Prestación: Corrección de errores por Alessandro Pasotti
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Cuelgue cuando se eliminan elementos del diseñador de impresión | [#31549](https://github.com/qgis/QGIS/issues/31549) |  |  |
| Error python en el administrador de BD | [#31457](https://github.com/qgis/QGIS/issues/31457) |  |  |
| QGIS 3.4.11: Clickando en la URL de un PDF en la respuesta GetFeatureInfo genera un error | [#31542](https://github.com/qgis/QGIS/issues/31542) | Ya arreglado (por mí) en 3.8 y Master |  |
| Watch file no añade nuevas columnas | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| Perdida de fondo de etiquetas de antigüo proyecto/estilo | [#31427](https://github.com/qgis/QGIS/issues/31427) | [PR #3164](https://github.com/qgis/QGIS/pull/31647) |  |
| \"Text formats\" dialog shows modifiable buffer properties while the \"draw text buffer\" is unchecked | [#31428](https://github.com/qgis/QGIS/issues/31428) | [PR #3173](https://github.com/qgis/QGIS/pull/31734) |  |
| El widget de pestaña Simbología no se expande horizontalmente en la extensión del diálogo de propiedades de capa | [#31449](https://github.com/qgis/QGIS/issues/31449) | [PR #3166](https://github.com/qgis/QGIS/pull/31665) |  |
| Watch file no añade nuevas columnas | [#31452](https://github.com/qgis/QGIS/issues/31452) |  |  |
| no reportado pero relacionado con #31452 | [PR #3168](https://github.com/qgis/QGIS/pull/31688) |  |  |
| Imposible añadir servicio WMS en QGIS, la misma URL funciona en otros clientes | [#31661](https://github.com/qgis/QGIS/issues/31661) |  |  |
| Servidor QGIS - Descarga de capacidades fallida: El protocolo de enlace SSL falló | [#31675](https://github.com/qgis/QGIS/issues/31675) |  |  |
| regresión aparente en la calculadora ráster multiplicando condicionales | [#31193](https://github.com/qgis/QGIS/issues/31193) | [PR #3169](https://github.com/qgis/QGIS/pull/31690) |  |
| Acciones de navegador GPKG rotas | [#31730](https://github.com/qgis/QGIS/issues/31730) | [PR #3173](https://github.com/qgis/QGIS/pull/31731) |  |
| Cambiando el tamaño del cuadro de diálogo del administrador de fuente de datos falla el redimensionado de los paneles sin enfoque | [#31732](https://github.com/qgis/QGIS/issues/31732) | [PR #3174](https://github.com/qgis/QGIS/pull/31741) |  |
| El procesamiento de partes múltiples a partes individuales no maneja restricciones únicas | [#31634](https://github.com/qgis/QGIS/issues/31634) | [PR #3175](https://github.com/qgis/QGIS/pull/31750) | [PR #3181](https://github.com/qgis/QGIS/pull/31810) |
| Quiebra al añadir leyenda via python | [#31713](https://github.com/qgis/QGIS/issues/31713) |  |  |
| UI: La leyenda no se refresca después de actualizar límites de clases | [#31643](https://github.com/qgis/QGIS/issues/31643) | No afectado | [PR #3183](https://github.com/qgis/QGIS/pull/31834) |
| UI: PostGIS layer error message not helpful, disappears and shouldn\'t happen | [#31799](https://github.com/qgis/QGIS/issues/31799) | [PR #3184](https://github.com/qgis/QGIS/pull/31841) |  |
| El servidor contextual GetLegendGraphics (BBOX) falla si no se suministra WIDTH y HEIGHT | [#31846](https://github.com/qgis/QGIS/issues/31846) | [PR #3186](https://github.com/qgis/QGIS/pull/31865) | [PR #3188](https://github.com/qgis/QGIS/pull/31882) |
| extender/recortar falla | [#31864](https://github.com/qgis/QGIS/issues/31864) |  |  |
| UI: cualquier click para subir/bajar el número de clases se dispara dos veces | [#31635](https://github.com/qgis/QGIS/issues/31635) | [PR #3187](https://github.com/qgis/QGIS/pull/31871) |  |
| El proyecto GPKG no se marca manchado despues de borrarlo del almacén | [#30550](https://github.com/qgis/QGIS/issues/30550) | [PR #3187](https://github.com/qgis/QGIS/pull/31876) |  |
| Solucionado un problema no informado con la conversión de QVariantList a JSON en QgsJsonUtils | no reportado | [PR #3192](https://github.com/qgis/QGIS/pull/31920) |  |
| Fallo al añadir WMS | [#31927](https://github.com/qgis/QGIS/issues/31927) | [#31927](https://github.com/qgis/QGIS/issues/31927) | [PR #3197](https://github.com/qgis/QGIS/pull/31979) |
| El cambio de signo de la calculadora de ráster no funciona cuando OpenCL está activo | [#32023](https://github.com/qgis/QGIS/issues/32023) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Snapping map units always show \"meters even when the project is in different units | [#31961](https://github.com/qgis/QGIS/issues/31961) | [PR #3201](https://github.com/qgis/QGIS/pull/32018) |  |
| QGIS Raster Calculator no genera datos, solo rásteres | [#32025](https://github.com/qgis/QGIS/issues/32025) | [PR #3202](https://github.com/qgis/QGIS/pull/32026) |  |
| Problema abriendo proyectos desde PostgreSQL | [#32050](https://github.com/qgis/QGIS/issues/32050) | [PR #3206](https://github.com/qgis/QGIS/pull/32062) |  |
| GetLegendGraphic muestra todos los símbolos idénticos para leyendas basadas en contenido | [#32020](https://github.com/qgis/QGIS/issues/32020) |  |  |
| WFS doesn\'t recognize advertised GeoJSON outputFormat string | [#32065](https://github.com/qgis/QGIS/issues/32065) | [PR #3210](https://github.com/qgis/QGIS/pull/32106) |  |
| Fallos creando índices en geopaquetes (QGIS 3.8.3) | [#32094](https://github.com/qgis/QGIS/issues/32094) |  |  |
| DB manager import option \"Create single-part geometries instead of multi-part\" is broken | [#32089](https://github.com/qgis/QGIS/issues/32089) | [PR #3210](https://github.com/qgis/QGIS/pull/32108) |  |
| GetLegendGraphic muestra todos los símbolos idénticos para leyendas basadas en contenido | [#32020](https://github.com/qgis/QGIS/issues/32020) | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| WFS contextual legend issue when canvas CRS is different than layer\'s CRS | no reportado | [PR #3212](https://github.com/qgis/QGIS/pull/32120) |  |
| PostGIS/geojson: No se pueden ingresar números negativos en campos int | [#32149](https://github.com/qgis/QGIS/issues/32149) | [PR #3216](https://github.com/qgis/QGIS/pull/32161) |  |
| La pestaña de información en las propiedades de la capa WMS no responde si un servicio WMS contiene muchas capas | [#32213](https://github.com/qgis/QGIS/issues/32213) | [PR #3226](https://github.com/qgis/QGIS/pull/32269) |  |
| Fuente de datos UI - Comentarios de tabla mutilínea PostgreSQL hace la malla de la tabla difícil de leer | [#32257](https://github.com/qgis/QGIS/issues/32257) | [PR #3233](https://github.com/qgis/QGIS/pull/32336) |  |
| Más desreferencia de puntero nulo cuando los complementos están desactivados | [#32347](https://github.com/qgis/QGIS/issues/32347) | [PR #3235](https://github.com/qgis/QGIS/pull/32351) |  |
| Desreferencia de puntero nulo cuando los complementos están desactivados | [#32338](https://github.com/qgis/QGIS/issues/32338) | [PR #3234](https://github.com/qgis/QGIS/pull/32345) |  |
| \"Merge features\" and \"merge feature attributes\" have broken numerical functions | [PR #3236](https://github.com/qgis/QGIS/pull/32360) | [PR #3236](https://github.com/qgis/QGIS/pull/32360) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Prestación: Corrección de Errores por Alexander Bruy
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Los scripts GDAL en Processing necesitan ser citadas en los nombres de los atributos | [#30878](https://github.com/qgis/QGIS/issues/30878) | [PR #3171](https://github.com/qgis/QGIS/pull/31712) | [PR #3171](https://github.com/qgis/QGIS/pull/31717) |
| Los algortimos GDAL no manejan correctamente capas de entrada WFS | [#29663](https://github.com/qgis/QGIS/issues/29663) | [PR #3173](https://github.com/qgis/QGIS/pull/31735) |  |
| shp files in zip files files cannot be used in Processing with 3rd party providers (SAGA, GRASS\...) | [#29001](https://github.com/qgis/QGIS/issues/29001) | [PR #3174](https://github.com/qgis/QGIS/pull/31744) | [PR #3178](https://github.com/qgis/QGIS/pull/31787) |
| No es posible el uso de alternar entidades seleccionadas en el cuadro combinado capa de Processing | [#30636](https://github.com/qgis/QGIS/issues/30636) | [PR #3173](https://github.com/qgis/QGIS/pull/31739) |  |
| Connect to postgis database fails in \"Layer - Add Postgis layer\" on databases with weird table names | [#27040](https://github.com/qgis/QGIS/issues/27040) | [PR #3176](https://github.com/qgis/QGIS/pull/31763) |  |
| GRASS v.build.polylines dosn\'t work in Qgis 3.4.10 | [#31037](https://github.com/qgis/QGIS/issues/31037) |  |  |
| Processing Algorithms written with the \@alg decorator don\'t get the gear icon | [#31252](https://github.com/qgis/QGIS/issues/31252) | [PR #3188](https://github.com/qgis/QGIS/pull/31887) |  |
| v.drape - no hay exportacion 25D con formato SpatiaLite | [#30066](https://github.com/qgis/QGIS/issues/30066) |  |  |
| Servicio url no puede incluir parámetros de consulta personalizados | [#26761](https://github.com/qgis/QGIS/issues/26761) |  |  |
| Processing: error python al arrancar | [#29535](https://github.com/qgis/QGIS/issues/29535) |  |  |
| Saving Processing\'s Package Layers algorithm\'s output to default temporary output leaves no result | [#30535](https://github.com/qgis/QGIS/issues/30535) |  |  |
| \[Georeferencer\] GDAL script does not set target SR | [#31353](https://github.com/qgis/QGIS/issues/31353) | [PR #3189](https://github.com/qgis/QGIS/pull/31898) |  |
| Processing \"Build virtual vector\" now fails in certain cases | [#29336](https://github.com/qgis/QGIS/issues/29336) | [PR #3190](https://github.com/qgis/QGIS/pull/31901) |  |
| Problema no reportado con importación perdida en el diálogo de algortimos Processing | no reportado | [PR #3190](https://github.com/qgis/QGIS/pull/31902) |  |
| db manager: python error when clicking \"edit table\" if the table is a postgis raster | [#30214](https://github.com/qgis/QGIS/issues/30214) | [PR #3190](https://github.com/qgis/QGIS/pull/31904) |  |
| Administrador BD: Renombbrando una columna de geometría PostGis provoca la pérdida de su tipo de gemetría y SRS | [#27613](https://github.com/qgis/QGIS/issues/27613) | [PR #3192](https://github.com/qgis/QGIS/pull/31929) |  |
| El georeferenciador muestra incorrectamente la última imagen cuando es reabierta | [#26700](https://github.com/qgis/QGIS/issues/26700) | [PR #3193](https://github.com/qgis/QGIS/pull/31932) |  |
| Administrador BD: Diálogo Crear capa debe cerrarse o limpiado una vez que la nueva capa es generada | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #3195](https://github.com/qgis/QGIS/pull/31956) |  |
| \[Vector Save As\...\] Extension is not replaced in filename when switching format | [#26054](https://github.com/qgis/QGIS/issues/26054) | [PR #3196](https://github.com/qgis/QGIS/pull/31960) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Esta funcionalidad fue desarrollada por Alexander Bruy
### Prestación: Corrección de Errores por Peter Petrik
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Fallo reproducible: Recuperando instancia QgsHighlight almacenada como una propiedad de widget | [#30766](https://github.com/qgis/QGIS/issues/30766) | [PR #3173](https://github.com/qgis/QGIS/pull/31733) | [PR #3197](https://github.com/qgis/QGIS/pull/31977) |
| Estilo de capa malla de capa no responde al cambio de Rampa de color (primera vez) | [#29188](https://github.com/qgis/QGIS/issues/29188) | [PR #3198](https://github.com/qgis/QGIS/pull/31981) |  |
| QGIS falla al cerrar en QSortFilterProxyModel | [#31721](https://github.com/qgis/QGIS/issues/31721) |  |  |
| QGIS se cuelga | [#29742](https://github.com/qgis/QGIS/issues/29742) |  |  |
| Fallo al intentar salvar un proyecto | [#29896](https://github.com/qgis/QGIS/issues/29896) |  |  |
| Fallo al salir con digitalización avanzada activa | [#29143](https://github.com/qgis/QGIS/issues/29143) |  |  |
| Renombrado de la app macOS provoca error de autenticación | [#32163](https://github.com/qgis/QGIS/issues/32163) |  |  |
| QGIS no puede abrirse después de actualizar a Mac OS Catalina | [#32167](https://github.com/qgis/QGIS/issues/32167) |  |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Prestación: Corrección de Errores por Even Rouault
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Accidente maestro de QGIS al salir @ QgsCoordinateTransformPrivate::freeProj en la plataforma Windows | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3176](https://github.com/qgis/QGIS/pull/31764) | [Commit 08bb3fe](https://github.com/qgis/QGIS/commit/08bb3fea3fc3f574755ecc0a7dc8381a9822e4cd) |
| Accidente maestro de QGIS al salir @ QgsCoordinateTransformPrivate::freeProj en la plataforma Windows | [#31762](https://github.com/qgis/QGIS/issues/31762) | [PR #3184](https://github.com/qgis/QGIS/pull/31848) | [PR #3185](https://github.com/qgis/QGIS/pull/31850) |
| QGIS WFS despojado del viewparam KVP de solicitudes de características de WFS | [#31026](https://github.com/qgis/QGIS/issues/31026) | [PR #3176](https://github.com/qgis/QGIS/pull/31765) | [PR #3188](https://github.com/qgis/QGIS/pull/31883) |
| Crash: right click on image -\>export -\>save as-\>\"save raster layer as\" | [#30937](https://github.com/qgis/QGIS/issues/30937) | [PR #3176](https://github.com/qgis/QGIS/pull/31766) | [PR #3178](https://github.com/qgis/QGIS/pull/31780) |
| Fallo al descubrir relaciones para capas postgresql | [#31213](https://github.com/qgis/QGIS/issues/31213) | [PR #3176](https://github.com/qgis/QGIS/pull/31768) | [PR #3177](https://github.com/qgis/QGIS/pull/31779) |
| Exportando ráster como datos en bruto a GeoPackage falla silenciosamente | [#30644](https://github.com/qgis/QGIS/issues/30644) | [PR #3177](https://github.com/qgis/QGIS/pull/31771) | [PR #3178](https://github.com/qgis/QGIS/pull/31781) |
| QGIS falla después de desactivar un driver GDAL en uso en el proyecto | [#29212](https://github.com/qgis/QGIS/issues/29212) | [PR #3177](https://github.com/qgis/QGIS/pull/31772) | [PR #3180](https://github.com/qgis/QGIS/pull/31802) |
| Fallo exportando a formato GS7BG | [#31775](https://github.com/qgis/QGIS/issues/31775) | [PR #3178](https://github.com/qgis/QGIS/pull/31785) | [PR #3183](https://github.com/qgis/QGIS/pull/31836) |
| pgdump no será ya mas un formato reconocido para el algoritmo de conversión de formato GDAL/OGR | [#31421](https://github.com/qgis/QGIS/issues/31421) | [PR #3181](https://github.com/qgis/QGIS/pull/31811) | no vale la pena |
| Archivos PBF no cargan correctamente | [#31062](https://github.com/qgis/QGIS/issues/31062) | [PR #3181](https://github.com/qgis/QGIS/pull/31812) | [PR #31835](https://github.com/qgis/QGIS/pull/31835) |
| Error importando cobertura de un servicio Geoservidor WFS | [#29844](https://github.com/qgis/QGIS/issues/29844) | [PR #31813](https://github.com/qgis/QGIS/pull/31813) | [PR #31867](https://github.com/qgis/QGIS/pull/31867) |
| El recuento de entidades de Geojson en línea no se actualiza al refrescar | [#30518](https://github.com/qgis/QGIS/issues/30518) | [PR #31860](https://github.com/qgis/QGIS/pull/31860) | no vale la pena |
| Ediciones en fuentes de datos GeoJson no se grabarán mas | [#28580](https://github.com/qgis/QGIS/issues/28580) | GDAL <https://github.com/OSGeo/gdal/pull/1846> | Compatible con las ramas de mantenimiento GDAL 3.0 y 2.4 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Funcionalidad: Bugs corregidos por Sandro Santilli
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Añadiendo rasters Postgis desde Administrador de BD pregunta por contraseña para cada añadido | [#31162](https://github.com/qgis/QGIS/issues/31162) |  |  |
| \[processing\] segmentizebymaxdistance puts qgis in endless CPU loop | [#31832](https://github.com/qgis/QGIS/issues/31832) | [Commit 6942b4b9](https://github.com/qgis/QGIS/commit/6942b4b93d252bc3a031db08a34f378d8d3c726d) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) |
| El archivo INSTALL no encuentra doc/api/html | [#31842](https://github.com/qgis/QGIS/issues/31842) | [Commit 3225f491](https://github.com/qgis/QGIS/commit/3225f4911a1199fc217aeca9fa63d9bf3d1b82c0) | n/d |
| QGIS died on signal 11 \# at start up | [#31350](https://github.com/qgis/QGIS/issues/31350) |  |  |
| repository files modified by `make check` | [#25830](https://github.com/qgis/QGIS/issues/25830) | [PR #31980](https://github.com/qgis/QGIS/pull/31980) |  |
| Error CMake en cmake/FindGEOS.cmake:162 | [#32170](https://github.com/qgis/QGIS/issues/32170) | [Commit bc9bb888](https://github.com/qgis/QGIS/commit/bc9bb8880a3db5a05c697f5d56708757a2ce999d) | [Commit 27f13936](https://github.com/qgis/QGIS/commit/27f13936afd970d766f398584a1ea509dc15b907) |
| False success from ogr provider\'s committChanges | [#32144](https://github.com/qgis/QGIS/issues/32144) | [Commit f421dc4f](https://github.com/qgis/QGIS/commit/f421dc4f92cfc019eec9823556d3c8f3e9589d95) | [Commit 136cec24](https://github.com/qgis/QGIS/commit/136cec244111748627c59db151002fddfc5f1708) |
| TestSagaAlgorithms: line 139, in check_algorithm: \'NoneType\' object has no attribute \'checkParameterValues\' | [#32143](https://github.com/qgis/QGIS/issues/32143) | [Commit 76b39de1](https://github.com/qgis/QGIS/commit/76b39de1b85375f48d7a5d35ebe39a52224d1809) | n/d |
| Los datos PostGIS cargan extremádamente lento | [#26186](https://github.com/qgis/QGIS/issues/26186) | [PR #31858](https://github.com/qgis/QGIS/pull/31858) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sandro Santilli](http://strk.kbt.io/)
### Funcionalidad: Bugs corregidos por Matthias Kuhn
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Fallo al abrir la pestaña de simbología de capa inválida | [#32041](https://github.com/qgis/QGIS/issues/32041) | [#32041](https://github.com/qgis/QGIS/issues/32041) | n/d |
| Revisión PR | Muchas :D |  |  |
| qgz son marcados como temporales en windows | [#32118](https://github.com/qgis/QGIS/issues/32118) |  |  |
| Permite seleccionar tipo de geometría en contexto | [#32121](https://github.com/qgis/QGIS/issues/32121) | [PR #32125](https://github.com/qgis/QGIS/pull/32125) | n/d |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Matthias Kuhn](https://www.opengis.ch/)
### Funcionalidad: Corrección de errores por Paul Blottiere
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Soluciona schemaLocation  inválido en GetCapabilities doc | [#32085](https://github.com/qgis/QGIS/issues/32085) | [PR #32352](https://github.com/qgis/QGIS/pull/32352) |  |
| Invalid WMS GetFeatureInfo response with json info_format | [#32326](https://github.com/qgis/QGIS/issues/32326) | [PR #32386](https://github.com/qgis/QGIS/pull/32386)/files |  |
| QGIS Server SELECTION doesn\'t work with Postgres ids of type bigint or text | [#29779](https://github.com/qgis/QGIS/issues/29779) |  |  |
| Regresión con opacidades para la solicitud  GetPrint de WMS | [#29317](https://github.com/qgis/QGIS/issues/29317) |  |  |
| Regresión no reportada: tipo inválido de renderizador tras cargar un archivo de estilo QML | regresión no reportada | [PR #32388](https://github.com/qgis/QGIS/pull/32388) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Esta funcionalidad fue desarrollada por Paul Blottiere
### Prestación: Corrección de Errores por Nyall Dawson
| Título del Error | URL del issue (si se reportó) | URL del PR o commit | 3.4 backport PR o commit |
| --- | --- | --- | --- |
| Solucionar fallo al borrar diseños de la ventana del diseñador | [#32465](https://github.com/qgis/QGIS/issues/32465) | [Commit e643e7f6](https://github.com/qgis/QGIS/commit/e643e7f6abe63aff123e07a0137afdda3987d4e6) | n/d |
| Solucionar modelo a pythin cuando el modelo no tiene parámetros de entrada | [Commit 6f1c42e7](https://github.com/qgis/QGIS/commit/6f1c42e7bc9fa6ddfae3bbc1304ebeb53fe6a014) | n/d |  |
| Solucionar escape de cadena al convertir modelos al código python | [#32451](https://github.com/qgis/QGIS/issues/32451) | [Commit e3eb4f54](https://github.com/qgis/QGIS/commit/e3eb4f54abdd8c6d4f4de443e3517775e9e565e1) | n/d |
| Arreglar la pérdida de memoria | [Commit 5be31915](https://github.com/qgis/QGIS/commit/5be319157f112a2fdbab7f03d0010d69f1e79157) | n/d |  |
| Solucionar el desbordamiento potencial en el procesador ráster | [Commit 1ba8db41](https://github.com/qgis/QGIS/commit/1ba8db41b67c7c481affd5271864cc2318ce06e4) | n/d |  |
| Restaurar las variables del proyecto pronto en el ciclo de lectura del proyecto | [#32382](https://github.com/qgis/QGIS/issues/32382) | [Commit d76835fe](https://github.com/qgis/QGIS/commit/d76835fec5a9217a5ea1996374d142f7319f8d08) | n/d |
| Mejorar documentos para "unir por el mas cercano", subir advertencia al registro | [#32317](https://github.com/qgis/QGIS/issues/32317) | [Commit 670c81f9](https://github.com/qgis/QGIS/commit/670c81f9212ada60f56c1c70ee9d37280052622c) | n/d |
| Capturar algunas excepciones de reproyección durante la representación ráster | [#32301](https://github.com/qgis/QGIS/issues/32301) | [Commit 1dfc0c1e](https://github.com/qgis/QGIS/commit/1dfc0c1e4eb8be26bb7214e3978aa6d80974c221) | n/d |
| \[labeling\] Fix broken numeric formatting settings, add tests | [#32393](https://github.com/qgis/QGIS/issues/32393) | [Commit b58dd674](https://github.com/qgis/QGIS/commit/b58dd6745fabf8bccd6dbeb684b37393d5953cb7) | n/d |
| Corregir la excepción de transformación no capturada al determinar los límites de la capa AFS | no reportado | [Commit 857697dd](https://github.com/qgis/QGIS/commit/857697dd9919e80fc03e0c2059e56ce7311e9b49) | n/d |
| Solucionar lanzamiento de advertencia qt al convertir un proyecto 2.18 | no reportado | [Commit 12ad9fca](https://github.com/qgis/QGIS/commit/12ad9fca1ed5027129161ee5b5c764b8374d0b51) | n/d |
| Add option to take no action (\"Leave as an unknown CRS\") when a layer is loaded which has no CRS | #19762, #27634, #24815 (y probablemente otros) | [Commit ffe66bff](https://github.com/qgis/QGIS/commit/ffe66bff82be16dd90cd95f13331e5be7ca2c628) | n/d |
| Don\'t force fallback to WGS84 for unknown layer CRSes | no reportado | [Commit 93741566](https://github.com/qgis/QGIS/commit/937415663f609fa7e41056aeb1176a0a145accc1) | n/d |
| Solucionar que las capas de memoria no pueden usar códigos CRS no-EPSG | No reportado, pero probablemente una causa de muchos errores | [Commit 2dad68f7](https://github.com/qgis/QGIS/commit/2dad68f76396a419b25fa8dad2b7b16552086740) | n/d |
| Solucionar fallo tras borrar secciones del informe | [#31302](https://github.com/qgis/QGIS/issues/31302) | [Commit 3356460c](https://github.com/qgis/QGIS/commit/3356460ce70af15105880d135271595dccfc397c) | [Commit d3230ac0](https://github.com/qgis/QGIS/commit/d3230ac0c545604a97fa3028ca3e846bff65004c) |
| Asegurar que los anillos de polígono generados para la representación estén siempre cerrados | no reportado | [Commit a69e38d9](https://github.com/qgis/QGIS/commit/a69e38d9c358faea5ae4a8628add1e6721cc23e8) | n/d |
| Don\'t crash QgsTessellator when an empty polygon is added | no reportado | [Commit 761b2e77](https://github.com/qgis/QGIS/commit/761b2e778594f4051a72d02b898354f501e336fe) | n/d |
| Solucionar fallo en complemento comprobador de topología cuando se cancela un chequeo | no reportado | [Commit 606bcd35](https://github.com/qgis/QGIS/commit/606bcd35143d09cca5b1ec45bdb5b13236e4376b) | n/d |
| Solucionar comprobador de topología comprobador multiparte | [#28361](https://github.com/qgis/QGIS/issues/28361) | [Commit 5101386b](https://github.com/qgis/QGIS/commit/5101386b37fb4d180d32d31663404e3bcc647cec) | n/d |
| Solucionar fallo al salir cuando el muelle del comprobador de topología está abierto con resultados visibles | no reportado | [Commit 64375ad4](https://github.com/qgis/QGIS/commit/64375ad4d28597eb97808f64e1481915df7a676c) | n/d |
| Don\'t load print layouts when opening project browser items | vía email | [Commit 9f1ce084](https://github.com/qgis/QGIS/commit/9f1ce08418db9545ed18d6711c472833f9889e1d) | n/d |
| Agregar el indicador QgsProject para evitar cargar diseños de impresión al leer un archivo de proyecto, evita bloqueos cuando el proyecto se carga en segundo plano | vía email | [Commit d0ed3746](https://github.com/qgis/QGIS/commit/d0ed3746629ae9c9349fe2e9c75550679120026d) | n/d |
| Don\'t try to load HTML content when a layout is created in a background thread | vía email | [Commit 53252496](https://github.com/qgis/QGIS/commit/532524961c0880b33e1d7ed4a3ce0805d7f0bc71) | [Commit 5fcab0e7](https://github.com/qgis/QGIS/commit/5fcab0e713a1e9ffde8b049f620d4a5cd6a81ff3) |
| Enorme aumento de velocidad a QgsTessellator | [Commit 577e1e96](https://github.com/qgis/QGIS/commit/577e1e962d4004f9cd11a169860e0b099216c963) | n/d |  |
| \[processing\] Ensure all objects used by the model are correctly imported | [#32004](https://github.com/qgis/QGIS/issues/32004) | [Commit e5e3fe47](https://github.com/qgis/QGIS/commit/e5e3fe473e8e6764f528b4a40095a7a047e9c357) | n/d |
| \[processing\] Avoid confusing use of expression parameter type in Random Points in Polygon algorithm | [#27640](https://github.com/qgis/QGIS/issues/27640) | [Commit 196e15a0](https://github.com/qgis/QGIS/commit/196e15a0ff974622bfa1e7dfdeb9fe8567a7f3b7) | n/d |
| \[layouts\] Update map settings variables in UI when map extent/rotation changes | [#24136](https://github.com/qgis/QGIS/issues/24136) | [Commit 86c83537](https://github.com/qgis/QGIS/commit/86c83537f9b03816ba5b8f90c8cf8a2820077441) | n/d |
| \[layouts\] Fix layout variables set programmatically do not show in GUI | [#28837](https://github.com/qgis/QGIS/issues/28837) | [Commit 1afdd935](https://github.com/qgis/QGIS/commit/1afdd935cf84cbd702093935a676672d1e349da1) | n/d |
| \[layouts\] Ensure variable panels are updated when layout or atlas properties change | [#26402](https://github.com/qgis/QGIS/issues/26402) | [Commit 2b31e03a](https://github.com/qgis/QGIS/commit/2b31e03ad0659500a733d71c10c54e17e6817c10) | n/d |
| \[layouts\] Move page background setting to a per-page option | [#25695](https://github.com/qgis/QGIS/issues/25695) | [Commit 45e847ef](https://github.com/qgis/QGIS/commit/45e847ef69b56b4c12774363e20a7a05f49e8618) | n/d |
| Optimizar QgsContrastEnhancementFunction | [Commit f5c21a0f](https://github.com/qgis/QGIS/commit/f5c21a0fbd72fe840900e0ad35c4af285fbd8a79) | n/d |  |
| \[layouts\] Prevent removal of the last remaining page in a layout | vía email | [Commit e6ecfdd3](https://github.com/qgis/QGIS/commit/e6ecfdd39bc2ae842c437700508899a9e1aa9dcd) | [Commit b65f23f8](https://github.com/qgis/QGIS/commit/b65f23f86b4630b4b5157400a713c36081bd56b9) |
| \[layouts\] Fix crash when exporting layout with no pages | vía email | [Commit b784d698](https://github.com/qgis/QGIS/commit/b784d6982826039bd9fa35b7ecd1a362e29c0b04) | [Commit f8355cbb](https://github.com/qgis/QGIS/commit/f8355cbbbe4bdbbae9c3f1b135ed59bbc51226a2) |
| Solucionar problemas de altos dpi del panel de formato condicional | [Commit 1f033fe8](https://github.com/qgis/QGIS/commit/1f033fe83d63a2edb6ddc2b6d90169e3b814764e) | n/d |  |
| Solucionar pérdida de ajuste de fuente al editar formato condicional | [Commit 72efc1ed](https://github.com/qgis/QGIS/commit/72efc1edde693800b6604e8ec3afcc892ea5239e) | n/d |  |
| Evitar desbordamiento en QgsImageOperation | [Commit aefbf662](https://github.com/qgis/QGIS/commit/aefbf6627256637cf455b2df409b3a4bf8171b33) | [Commit 9f4d3a87](https://github.com/qgis/QGIS/commit/9f4d3a8745b2d89faeb6a9272369eaa772e3638c) |  |
| \[processing\] Extend api for retrieving a layer in a compatible format | Plugin de rastreador de errores por parte de terceros | [Commit 651c5071](https://github.com/qgis/QGIS/commit/651c5071806d6f4f4dafc800e6b0d67f043a9ef0) | n/d |
| Fix conditional styles in feature list view do not update when the layer\'s conditional styles are changed | [Commit bccd5a46](https://github.com/qgis/QGIS/commit/bccd5a46106d7c5a63b3bd8c64ad1491a60205af) | n/d |  |
| Solucionar visor roto de estilos condicionales en el visor de lista de entidades | [Commit 5f7264d4](https://github.com/qgis/QGIS/commit/5f7264d4d18d6894c4d33017439dc517a932fd75) | n/d |  |
| Solucionar estilizado condicional incorrecto aplicado a filas en algunos casos | [Commit c15c7271](https://github.com/qgis/QGIS/commit/c15c72718909f4bce2d172b819c74ec7d8d4d9b3) | n/d |  |
| Uso inválido de colores, colores no transparentes, para indicar que no se configuran colores en formatos condicionales, se corrigen los colores incorrectos utilizados para las filas con estilo condicional | [Commit bc82cffd](https://github.com/qgis/QGIS/commit/bc82cffd85342d92435600547c220eb1eaf90257) | n/d |  |
| \"\[labeling\] When an extreme number of features are being labeled from a single layer, place additional limits on the maximum number of |  |  |  |
| labeling candidates to generate for features in this layer\" | [Commit 61bfced6](https://github.com/qgis/QGIS/commit/61bfced6a7ae109bc97a0924eae108c0e51916d5) | n/d |  |
| \[layouts\] Fix incorrect alignment of items when the align or distribute tools are used with items with a non-top-left reference point | [#31900](https://github.com/qgis/QGIS/issues/31900) | [Commit b4550dc4](https://github.com/qgis/QGIS/commit/b4550dc4c06eec23ace4cbc5c6f1f8b23c8ee14f) | n/d |
| \[processing\] Respect user set default vector output format in vector split algorithm | [Commit 90bac82f](https://github.com/qgis/QGIS/commit/90bac82f124ccb53e43bb99f5d483105bea1c967) | n/d |  |
| Solucionar que el GUI no se actualiza cuando el diseño del atlas se establece para usar la expresión de nombre de archivo predeterminada | [#20786](https://github.com/qgis/QGIS/issues/20786) | [Commit a4da849e](https://github.com/qgis/QGIS/commit/a4da849e9d190ece1b748303cc8f68333f1e0e78) | n/d |
| \[reports\] Remove useless extra set of export actions | [#26384](https://github.com/qgis/QGIS/issues/26384) | [Commit d6b41813](https://github.com/qgis/QGIS/commit/d6b4181349a274e8d34196a340f4b806403af06b) | n/d |
| \[reports\] Fix crash when print button clicked before a report section is opened | no reportado | [Commit c93fd0a4](https://github.com/qgis/QGIS/commit/c93fd0a4350ea14db9728ad17ada06e70eb9ffd6) | n/d |
| \[reports\] Reduce minimum width of report organiser dock | [#25916](https://github.com/qgis/QGIS/issues/25916) | [Commit 7c490848](https://github.com/qgis/QGIS/commit/7c4908481269f38e1b96c730542d5299903963fb) | n/d |
| \[layouts\] Add a page number selection combo box at the top of the guide manager dock | [#25700](https://github.com/qgis/QGIS/issues/25700) | [Commit 2f22aeaf](https://github.com/qgis/QGIS/commit/2f22aeaf276785867ed850f54c691a0a5b7c0aeb) | n/d |
| Show color button style \"Pick color\" and \"Chooe Color\" and symbol button menu | [#25696](https://github.com/qgis/QGIS/issues/25696) | [Commit 39cfd0f9](https://github.com/qgis/QGIS/commit/39cfd0f935bb8c6669237bc7abe6ca89c6a82a32) | n/d |
| Solucionar que los límites del diseño no sincronizados después de borrar página | [#26665](https://github.com/qgis/QGIS/issues/26665) | [Commit d498eed0](https://github.com/qgis/QGIS/commit/d498eed0a5caf01b914a2c25f0c1d255d955b4a9) | n/d |
| \[layouts\] Fix odd selection behavior when keyboard modifiers are pressed when rectangular selection ends | [Commit 37b5af54](https://github.com/qgis/QGIS/commit/37b5af54d9423563d17422f5b90d6a7dbdfe0299) | n/d |  |
| Corregir la interacción con los miembros del grupo en el panel de elementos | [#26674](https://github.com/qgis/QGIS/issues/26674) | [Commit 5154240f](https://github.com/qgis/QGIS/commit/5154240fa94401952329138300dd2035e5519d5e) | n/d |
| \[layout\] Fix invalid svg exports when including metadata | [#28130](https://github.com/qgis/QGIS/issues/28130) | [Commit cc94aebc](https://github.com/qgis/QGIS/commit/cc94aebc6fa2e53adc99902b7f7ac4f87e0361db) | n/d |
| \[legends\] Fix missing symbols for inverted polygon layers when using filter by map content | [#22718](https://github.com/qgis/QGIS/issues/22718) | [Commit abc9f47c](https://github.com/qgis/QGIS/commit/abc9f47ca471540c9b0f9dd6159d3ac7f9791a3c) | n/d |
| Utilizar un tamaño de fuente ligeramente mayor en los detalles de CRS en Windows | [#31297](https://github.com/qgis/QGIS/issues/31297) | [Commit 757017c2](https://github.com/qgis/QGIS/commit/757017c2c29a0ea4b72527e4cd98e700c720022c) | n/d |
| \[processing\] Add warning when packaging a geopackage with no layers | [#31888](https://github.com/qgis/QGIS/issues/31888) | [Commit f11e6603](https://github.com/qgis/QGIS/commit/f11e6603957f69a34ad7aa9893aa144cc5020ca4) | n/d |
| \[layouts\] Fix crash when opening layout with dynamic image in html label | [#28996](https://github.com/qgis/QGIS/issues/28996) | [Commit 5db6165f](https://github.com/qgis/QGIS/commit/5db6165fb597c2db278e678953578992789fa38b) | [Commit e29865cd](https://github.com/qgis/QGIS/commit/e29865cd485c3576db27aab4cad86614f3eff2f3) |
| Exponer informe de la configuración de entidad cuando una tabla de atributos es usada en un atlas | [#28441](https://github.com/qgis/QGIS/issues/28441) | [Commit 9fd17c8f](https://github.com/qgis/QGIS/commit/9fd17c8f3cce8fb5864db137da71c3cb61b44510) | n/d |
| \[layouts\] Fix attribute table ignores cell margin for top/bottom aligned text | [#31259](https://github.com/qgis/QGIS/issues/31259) | [Commit 7b356fe4](https://github.com/qgis/QGIS/commit/7b356fe4cde1b030ddfb589a22cb59229311074e) | n/d |
| Solucionar bordes de símbolo de leyenda truncados cuando se establece opacidad a la capa | [Commit 30e14938](https://github.com/qgis/QGIS/commit/30e149387bcccbd14f057a16cb27729c57c9a210) | n/d |  |
| Solucionar que añadir/mover leyenda es muy lento en proyectos amplios | [#29058](https://github.com/qgis/QGIS/issues/29058) | [Commit 758ac909](https://github.com/qgis/QGIS/commit/758ac9092f9fac3f7533766f329f17832b2dcd35) | n/d |
| \[reports\] Fix predefined scale mode is incompatible with report outputs | [#29196](https://github.com/qgis/QGIS/issues/29196) | [Commit fcd21e48](https://github.com/qgis/QGIS/commit/fcd21e485068d8082bdef0a5a7393b57fe5bf3c1) | n/d |
| Asegurar que la evaluación de expresión en atlas tenga acceso al alcance de la cobertura de capa | [#31807](https://github.com/qgis/QGIS/issues/31807) | [Commit 3de05939](https://github.com/qgis/QGIS/commit/3de059395706a225ca137b3d4a7a34b27d3cc9ae) | n/d |
| Redimensionando páginas al contenido no debe crear tamaño de página vacía si no se presentan elementos | [#29034](https://github.com/qgis/QGIS/issues/29034) | [Commit 421e68cf](https://github.com/qgis/QGIS/commit/421e68cf5ae5637001765842e257caf6becdb876) | n/d |
| Solucionar que la rotación del mapa no se restaura inmediatamente en los informes | [#31217](https://github.com/qgis/QGIS/issues/31217) | [Commit f5afebe5](https://github.com/qgis/QGIS/commit/f5afebe5dd0228ceb612a9823a80c77ccd51a1e6) | n/d |
| No devuelve valores nan cuando se utiliza un asistente con min val == max val | [#31242](https://github.com/qgis/QGIS/issues/31242) | [Commit 97923751](https://github.com/qgis/QGIS/commit/979237515ce2921b9552a99eda071e9e9a14297a) | n/d |
| \[layouts\] Fix label items don\'t update when their opacity \< 100 | [#29079](https://github.com/qgis/QGIS/issues/29079) | [Commit f9a47738](https://github.com/qgis/QGIS/commit/f9a47738aaaec7504f912b2442195662a216b9e3) | n/d |
| Fix project load status indicator can get \"stuck\" after project load | no reportado | [Commit 40d95b69](https://github.com/qgis/QGIS/commit/40d95b69d91ade71473f5ea0182040d8398cc668) | n/d |
| Corregir expresiones corruptas en ventana emergente del indicador de filtro | [Commit 393e623b](https://github.com/qgis/QGIS/commit/393e623ba7d278eabc4f09aeaabb92f56fa269c9) | [Commit 8e0e368f](https://github.com/qgis/QGIS/commit/8e0e368f255ba10c530afd445ecd1ab53bf266bb) |  |
| Solucionar que no se pueda usar el panel GPS para dibujar entidades en multi polígono/línea | [#29144](https://github.com/qgis/QGIS/issues/29144) | [Commit dc2b209d](https://github.com/qgis/QGIS/commit/dc2b209da3609a47b1457c0cb12417afbcb36344) | n/d |
| Solucionar pérdida del ajuste del fondo de la etiqueta al restaurar proyectos | [#31427](https://github.com/qgis/QGIS/issues/31427) | [Commit aa4a8da3](https://github.com/qgis/QGIS/commit/aa4a8da3a713b6961fccce019c5e9b5778f68b23) | n/d |
| Solucionar fallo en renderizador de desplazamiento de punto | [Commit 7043933f](https://github.com/qgis/QGIS/commit/7043933ff2bed42df5ae3439867330e39fe60f53) | n/d |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
