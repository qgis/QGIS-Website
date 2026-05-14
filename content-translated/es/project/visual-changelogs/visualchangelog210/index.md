---
HasBanner: false
draft: false
releaseDate: '2015-06-26'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.10
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.10{#changelog210 }
Fecha de lanzamiento: 2015-06-26

This is the change log for the next release of QGIS - version 2.10.0 \' Pisa\' - host city to our developer meet up in March 2010.

**Último Lanzamiento**

This is the next release in our 4-monthly release series. It gives you early access to the new features we have been working on and represents the \'cutting edge\' of QGIS development. If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.2 and is available at [download.qgis.org](http://download.qgis.org). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates). The features provided in QGIS 2.10 \'Pisa\' will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

**New Features in QGIS 2.10 \'Pisa\'**

QGIS 2.10.0 includes many great new features, tweaks and enhancements to make the most popular Free desktop GIS even more feature filled and useful. Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, probadores y a las muchas personas que ofrecen su tiempo y esfuerzo voluntario (o financian a personas que lo hacen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente nos gustaría agradecer a nuestros patrocinadores oficiales por el soporte financiero invalorable que proveen a este proyecto:
- **GOLD Sponsor:** [Asia Air Survey, Japan,](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## General
### Característica: Parámetros de unión ahora pueden ser editados
Ahora es posible editar parámetros join (tales como el prefijo join o columnas a unir/join) después que el join ha sido creado. Antes de este cambio se tenía que borrar y recrear todo el join.

![image14](images/entries/bb09241b7b997dfa07942ee5172ad466ebb777f7.webp)
### Característica: Capas con joins ahora pueden ser filtrados
Prior to version 2.10 a layer couldn\'t be filtered if it had at least one join. Now it is still filterable, but only using columns of the original master table.

![image15](images/entries/a2a93d4e621c1a2cfd976f3b0ec9673739aafda3.webp)
### Característica: Mejoras generales
Así como los numerosos elementos listados abajo, se hicieron las siguientes mejoras:
- Soporte para capas Pointcloud en PostGIS
- Barras de iconos e iconos mejorados en widgets acoplables para ocupar menos espacio en la pantalla y para mejorar la apariencia de OSX
- Mejoras al complemento / proveedor GRASS
- Soporte para escrituras no-latinas en etiquetas curveadas
- Calculadora ráster y herramientas de referenciación muy mejoradas y más robustas
- IU y flujo de trabajo mejorado para la ventana de propiedades de etiqueta definidas por datos

![image16](images/entries/db0cb94196fd524d93236131418f6e5f3bbf6f25.webp)
### Característica: Manejo mejorado de potencial sobreescritura de archivo de proyecto
QGIS 2.10 ahora le avisará cuando intente guardar su proyecto si la última fecha de modificación de un proyecto cargado ha cambiado. Esto es útil si más de un usuario o sesión tiene el mismo archivo de proyecto abierto y ambos intentan guardar ediciones en el archivo de proyecto.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

![image17](images/entries/c30c07afc9123db564b766339daefe53af3cd348.webp)
### Característica: Nuevo motor de geometría
QGIS 2.10 has a new geometry engine. In general you won\'t see many differences on the user interface yet, but this lays the foundation for a much richer set of geospatial capabilities that we will be able to support in the future. The new implementation supports curved geometry types (so for example you can represent a traffic roundabout as a circle rather than a segmented polygon made to look like a circle) and has backend support for z/m values in geometries. To use curves in QGIS you will need to use PostGIS or a similar datastore that is able to express curvilinear geometries. If you want to have a play you can try a simple exercise like this in your PostGIS database:

    -- Table: curves DROP TABLE curves;
    CREATE TABLE curves (
       id bigserial NOT NULL,
       geometry geometry(CURVEPOLYGON, 4326),
       name text,
       CONSTRAINT p_key PRIMARY KEY (id)
       );
    
    INSERT INTO curves VALUES ( 1, st_geomfromtext(
       'CURVEPOLYGON(CIRCULARSTRING(1 1,1 2, 2 2, 2 1, 1 1))', 4326), 'test');
    
Then add the layer `curves` to your project.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [KantonSolothurn, Switzerland](http://www.sogis.ch/)

![image18](images/entries/4f070e4075b4703edb40d8cb91d5fb527d1d3a93.webp)
## Herramientas de análisis
### Característica: Nuevo widget de resumen estadístico en el acople
Can display summary statistics (e.g. mean, standard deviation, \...) for a field or expression from a vector layer or selection. This is provided by means of a new dock panel that you can activate from the `View -> Panels -> Statistics` menu. Please note that you will only be able to generate statistics on **vector layers** that have a **numeric column**.

![image1](images/entries/7d52fdffac5546ea3f39ee4dac5dbe19f961703a.webp)
### Característica: Usar funciones logarítmicas en la calculadora ráster
The raster calculator (`Raster -> Raster Calculator` in the QGIS menu) is a tool that allows you to perform matrix operations on one or more raster layers. With QGIS 2.10 you can now use `LN` and `LOG10` functions in the raster calculator.

![image2](images/entries/13c65100ab57ed8f97fa23b08704ca726a7c33da.webp)
### Característica: Nuevas características de estadísticas zonales
Las estadísticas zonales proporcionan una forma de extraer valores agregados para los píxeles subyacentes a un polígono. Las siguientes nuevas funciones se han agregado a nuestra herramienta de estadísticas zonales:
- ahora puede seleccionar qué estadísticas calcular
- estadísticos extras han sido adicionados (mediana, desv estándar, mín, máx, rango, minoría, mayoría y variedad)
- habilidad para seleccionar la banda ráster para usar la extracción de estadísticos

Note that zonal stats is a \'core plugin\' (a plugin that ships with your QGIS installer), but is disabled by default. You need to enable it in the plugin manager and then a menu entry for zonal statistics will appear in the `Raster` menu.

![image3](images/entries/d86b8eb8a72d26a0fcb0bf043c9189e14a4ae125.webp)
## Navegador
### Característica: Nuevo widget de propiedades del navegador
When using the QGIS Browser dock panels (`View -> Panels -> Browser`), you and now enable a properties widget at the bottom of the file system tree. Any data source that you click on will have its properties shown in this panel. This makes it quick and convenient to see basic information about the dataset you have selected. To toggle the properties view, you should use the `i` icon at the top of the browser panel.

![image4](images/entries/2f3fed9a32d761418704da2a7da378ba172164da.webp)
### Característica: Nuevo ícono del navegador
El navegador QGIS es una aplicación independiente y separada que le permite navegar y ver los conjuntos de datos SIG disponibles (desde su sistema de archivos, conexiones de bases de datos, conexiones de servicios web, etc.) En versiones anteriores de QGIS utilizamos un icono muy similar al de la Aplicación QGIS en sí que ha sido fuente de confusión para muchos usuarios. Para reducir la probabilidad de abrir la aplicación incorrecta, hemos creado un nuevo icono para el navegador QGIS.

![image5](images/entries/e76e98dffc99404f3cad540c42baebb434a696fe.webp)
## Proveedores de datos
### Característica: Mejoras a Exportación DXF
La exportación DXF se mejoró continuamente en las últimas tres versiones de QGIS. Esta versión presenta un SVG mejorado o un marcador simple para la conversión de bloques DXF, corrige algunos errores y problemas que resultaron en archivos DXF incompletos (ilegibles). En la captura de pantalla, puede ver la vista original en QGIS a la izquierda y la representación del archivo DXF exportado en Autodesk TrueView a la derecha.

See also [this article on qgis.ch](http://www.qgis.ch/en/projects/dxf-export) explaining what is supported and what not.

**This feature was developed by:** [Jürgen Fischer (norBIT)](http://www.norbit.de/)

**Esta característica fue financiada por:** Communidades de Morges, Uster, Vevey y SIGE

![image6](images/entries/b5ee8bd7a3412e429782a5e56954dabee05c36ff.webp)
### Característica: filtros de expresión del lado de proveedor PostGIS
En QGIS 2.10 ahora puede filtrar características en el lado del servidor de la base de datos. Solo las expresiones admitidas se enviarán a la base de datos. Las expresiones que utilizan operadores o funciones no admitidas recurrirán satisfactoriamente a la evaluación local.

To make use of this feature you need to enable it in `Settings -> Options -> data sources`. If your filter expression is PostgreSQL compliant it will automatically be run on the server side. You can also make use of this feature when using the python API for example when using these calls.

`QgsFeatureRequest().setFilterExpression( expression )`

o

`QgsVectorLayer::getFeatures( expression )`

![image7](images/entries/4d4076579ecc0b5aace30fa2743f616a9b691a02.webp)
## Gestión de datos
### Característica: Campos virtuales ahora son actualizables
Prior to version 2.8 you had to delete and recreate virtual fields if you wanted to change the expression for calculating the virtual field. In 2.10 you can now go to the `Fields` tab and press the small `Expression` button to open the expression editor and update the expression used for the virtual field.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image8](images/entries/f45d5a4447f28d96a2c5c4cc6c27b84285096a02.webp)
### Prestación: Edición de línea con autocompletador para el widget de edición ValueRelation
The value relation edit widget for vector layers (`Layer -> Properties -> Fields -> Edit Widget -> Value Relation`) can now be set to autocomplete as you start typing in the input box it creates on the feature form.

![image9](images/entries/4610dc0ab64a85ae020aeb22b4cbfcc8d45d0df3.webp)
### Característica: Mejoras al Administrador BD
Existen dos nuevas características en el Administrador BD:

**Consulta como capa no necesitará una única columna de enteros nunca más**

Una columna con única columna de enteros no será necesitada más para cargar una consulta SQL como una capa QGIS. Un valor autoincrementado será usado en su lugar.

**Integración de un constructor de consulta SQL**

Una nueva ventana en DB Manager ayuda a la creación de consultas SQL por medio de widgets donde el usuario puede seleccionar nombres de tablas, columnas y funciones. Se ha portado desde el complemento QSpatialite y funciona para los proveedores de PostGIS y Spatialite.

**Estas características fueron financiadas por**: MEDDE (Ministerio Francés de Desarrollo Sustentable)

**Estas características fueron desarrolladas por**: Hugo Mercier / Oslandia

![image10](images/entries/f5ad9f81ac37ff4dcfa754f83d23c2700ad4c9f8.webp)
### Prestación: Encadenamiento de filtros para el widget de referencia de relación
To select linked entries from other tables one can use the relation reference widgets. One can either select elements graphically by selecting them in the map, if the linked feature has a geometry attached or choose an element by the linked id. To facilitate the non-spatial selection it is now possible to narrow the available options with filters (chained or unchained). If the filters are unchained their choices are combined with \"AND\" to define the available options. If chained is checked, a drill-down mode for the filters is activated so each filter only shows the entries which correspond to the previous filter. This is useful for selecting from hierarchical data like City -\> Street -\> Number.

**This feature was developed by:** [Matthias Kuhn (OpenGIS)](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)

![image11](images/entries/fd0d2e726135033e8e5a61b8a718535074a2ac0c.webp)
## Diagramas
### Característica: Mejoras de diagrama
La funcionalidad del diagrama en QGIS le permite superponer pequeños gráficos circulares o histogramas sobre las características del mapa. En esta versión, hemos realizado las siguientes mejoras en el soporte de diagramación:
- Diagramas pueden ser desabilitados sin perder la configuración
- Adicionar caja de selección para mostrar siempre diagramas para una capa
- El interfaz de usuario de diagramas ha sido actualizado para simplificar el diálogo y hacerlo más amigable al usuario
- Diagram classes are now shown in the layer\'s legend

![image12](images/entries/cc5753de0538c89e3231f18c7ce62c7bc0afa5e8.webp)
## Digitalizando
### Característica: Herramienta mejorada de rotación de geometría
The geometry rotation tool is an advanced digitising tool that allows you to arbitrarily rotate a feature\'s geometry. The following improvements have been made to the rotation tool:
- ahora puede usar entrada numérica en la herramienta de rotación de mapa
- puede usar la caja combo para definir los ángulos
- added support for snapping to angles (directly enabled when `using`shift + click\`\`)
- rotation anchor is defined on `CTRL+click` and not on mouse move

![image13](images/entries/7ff32dd8c7ead358f9ffab4576dff33503154eb2.webp)
## Etiquetando
### Feature: \"Follow point\" alignment for multiline labels
Cuando se establece este modo, la alineación del texto para las etiquetas depende de la ubicación final de la etiqueta en relación con el punto. Por ejemplo, si la etiqueta se coloca a la izquierda del punto, la etiqueta se alineará a la derecha, y si se coloca a la derecha del punto, la etiqueta se alineará a la izquierda. Esto mejora en gran medida la apariencia de las etiquetas multilínea para capas de puntos.

![image19](images/entries/851e7234a9509e2452dee69939d9de933a8bb90a.webp)
## Compositor de Mapa
### Característica: Agregar modo de tamaño a barra de escala para ajustar un ancho deseado de barra de escala
In previous QGISversions it was hard to use graphical scalebars when the range of potential scales was big. The scalebar would either be quickly too wide or too narrow and one had to manually adapt the segment sizes (units per segment) after each scale change. It also meant that graphical scalebars couldn\'t be really used in Atlas serial printing or with QGISserver when the final map scale was unknown. With QGIS2.10 one can now set min/max sizes for one segment length in mm and QGISwould automatically adapt the units per segment while still keeping round values.

Don\'t forget to also set the alignment of the scalebar, esp. if you want it to be centered or right-aligned!

**This feature was developed by:** [Sandro Mani (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [Kanton Glarus, Switzerland](http://geo.gl.ch/)

![image20](images/entries/d435d4f94cf3d70a97c8d373aa08c28f8685defd.webp)
## Programabilidad
### Característica: Mejoras para programadores
Hemos hecho varios cambios y mejoras que serán de interés a los desarrolladores:
- Hemos aumentado el requisito mínimo para Qt4 a la versión 4.8. Qt4 es uno de los principales conjuntos de herramientas/bibliotecas de C ++ que utilizamos para crear QGIS.
- New `QgsStatisticalSummary` class for calculating statistics from a list of numbers.
- Permite fuente de dato de capa vector cambiante.
- Implicit sharing of classes : `QgsField`, `QgsFields`, `QgsDataDefined`, `QgsFeature`, `QgsGeometry`.
- Plugins can now create their own entries in the browser widget with two new classes : `QgsDataItemProvider` and `QgsDataItemProviderRegistry`.

![image21](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
## Servidor de QGIS
### Característica: Soporte de parámetro tolerancia en pedidos WMS GetFeatureInfo
Al usar capas WMS atendidas por QGIS Server, ahora puede especificar la tolerancia a qué distancia del origen del clic se deben considerar las solicitudes GetFeatureInfo. Esto es importante para los dispositivos móviles donde es más difícil señalar exactamente las funciones. Antes de esta nueva característica, era prácticamente imposible identificar características de punto o línea en un dispositivo móvil con el servidor QGIS. Puede agregar los siguientes parámetros a sus solicitudes GetFeatureInfo:

FI_POINT_TOLERANCE=16&FI_LINE_TOLERANCE=8&FI_POLYGON_TOLERANCE=4

y cambiar los valores de tolerancia (en píxles) para coincidir con sus necesidades.

**This feature was developed by:** [Marco Hugentobler (Sourcepole AG)](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster, Switzerland](http://gis.uster.ch/)

![image22](images/entries/29470cc51906dffe3a96d3e17a7e8c83b4504a18.webp)
## Simbología
### Característica: Hacer coincidir categorías a estilos existentes
Agregue opciones en el menú avanzado del renderizador categorizado para establecer categorías en símbolos con un nombre coincidente de la biblioteca de estilos o un archivo de estilo XML.

![image23](images/entries/c3fe0d0389c267271cbd47b8c44f52ac079961d7.webp)
### Característica: Variar tamaños de símbolo usando el renderizador graduado
Los renderizadores son el subsistema de QGIS que le permite crear ricas representaciones cartográficas de sus datos. Un renderizador graduado varía la simbología en función de un valor que cambia continuamente en una capa vectorial. En versiones anteriores de QGIS solo podía variar el color (por ejemplo, usando un color a lo largo de una rampa de color). En QGIS 2.10, el renderizador de símbolos graduados ahora le permite variar el tamaño * o * el color. Para las capas de puntos puede variar el tamaño del punto, para las líneas puede variar el ancho de la línea. Las capas poligonales solo retienen la capacidad de variar según el color, el ancho de línea aún no es posible.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image24](images/entries/1d170efe9ca0c76e971cfe0f1d0adb7c4e14f08f.webp)
### Característica: Nueva opción para prevenir el recorte automático de rasgos a la extensión del mapa
This option (located under the symbol advanced menu) disables the automatic clipping of lines/polygons to the canvas extent. In some cases this clipping results in unfavourable symbology (eg centroid fills where the centroid must always be the actual feature\'s centroid).

![image25](images/entries/ecd30b6893fd93d65c95df8f069cc3c3e0fff7be.webp)
### Característica: Se ha eliminado tamaño, escala y rotación del menú avanzado
We have removed `SizeScale` and `Rotation` from `` `Layer -> Properties -> Symbology tab -> Advanced Menu ``. You should rather set rotation on a *per-symbol layer basis* using an expression or field. The expressions used in old projects are converted to symbol level **data defined size and angle** properties.

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image26](images/entries/2e02fb11f0f967b1ea17331d9af3d5a22a63fed1.webp)
### Característica: Propiedades definidas por datos para el marcador de fuentes de letra
Ahora se pueden ahora definir por datos la mayoría de las propiedades del marcador de fuentes, incluyendo el tamaño del marcador, rotación y caracter.

![image27](images/entries/9ffd9d3284adcc85d6434f0b97f2db8974a7f647.webp)
### Característica: Visualizar y modificar el renderizador graduado usando un histograma
Se ha agregado una nueva pestaña de histograma al renderizador graduado, que muestra un histograma interactivo de los valores del campo o expresión asignados. Los saltos de clase se pueden mover o agregar usando el histograma.

**This feature was funded by:** [ADUGA](http://www.aduga.org)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image28](images/entries/b519e61b5b50de563203adf8ef35a7c037536332.webp)
### Característica: expresiones de tamaño, rotación y ancho de trazo en el nivel de simbología
El tamaño y la rotación se pueden definir mediante una expresión para todos los niveles de símbolos que componen un marcador. El ancho se puede definir mediante una expresión para todos los símbolos que componen una línea.

Para los símbolos, se genera una leyenda para diferentes tamaños. Esto permite una leyenda de análisis multivariante en el caso de colores clasificados / graduados.

Se puede acceder a un asistente, con vista previa, a través del botón de datos definidos para ayudar al usuario a definir la expresión de tamaño. Hay tres métodos disponibles: lannery, Area y Radius

**This feature was developed by:** [Vincent Mora (Oslandia)](http://www.oslandia.com/)

**This feature was funded by:** [Agence de l\'eau Adour-Garonne](http://www.eau-adour-garonne.fr/)

![image29](images/entries/30f4392583400a0ed2fbdae3468265b91f39e675.webp)
### Característica: Efectos vivos de capa para capas y capas de símbolos
Los efectos de capa en vivo se suman a las capacidades cartográficas ya extensas de QGIS al agregar la capacidad de agregar varios efectos de renderizado en la cadena de renderizado. Con los efectos en vivo, puede hacer cosas como colocar sombras debajo de su símbolo, sesgar y cortar el símbolo representado. También puede superponer estos efectos uno encima del otro y establecer si el efecto debe ser progresivo (es decir, aplicarse al estado renderizado hasta el momento) o discreto (reinyectando la geometría de origen en la cadena de renderizado).

** Nota **: Esta es una funcionalidad para usuarios avanzados y debemos tener en cuenta que el uso excesivo de esta función puede ralentizar significativamente los tiempos de renderizado, por lo que puede considerar tener diferentes perfiles de simbología para su capa, uno para la generación de mapas de calidad de producción y uno para el modo borrador.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [a crowd-funding initiative](https://www.kickstarter.com/projects/41633306/a-christmas-gift-for-qgis-live-layer-effects-for-q)

![image30](images/entries/2ce331bd884c14764989c1bc5e3c4d1f80ec588c.webp)

{{<content-end >}}
