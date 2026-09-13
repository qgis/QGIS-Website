---
HasBanner: false
draft: false
releaseDate: '2015-10-23'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.12
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.12{#changelog212 }
![image1](images/projects/3648539707d0789903fdfedac3705584f12fa6ac.png)

Fecha de lanzamiento: 2015-10-23

This is the change log for the next release of QGIS - version 2.12.0 \'Lyon\' - host city to our developer meet up in April 2012.

**New Features in QGIS 2.12 \'Lyon\'**

This is the next release in our 4-monthly release series. It gives you access to the new features we have been working on and represents the \'cutting edge\' of QGIS development.

QGIS \'Lyon\' is jam-packed with awesome new features. Special highlights are support for rule based labelling, rule based styling of attribute tables, and advanced geometry checker, support for digitising curve based geometries, better authentication management and much, much more! QGIS 2.12 also has many bug fixes and memory leaks addressed. The features provided in QGIS 2.12 will be included in the next LTR release (slated for release in 2016), so using this release provides you with an excellent opportunity to test new features that will make their way into the next LTR.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org). If you are working in a production environment where you wish to be more conservative about rolling out new features to your users, we also provide a Long Term Release (LTR) version of QGIS. The current LTR is version 2.8.3 and is available at [download.qgis.org](http://download.qgis.org).

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, probadores y a las muchas personas que ofrecen su tiempo y esfuerzo voluntario (o financian a personas que lo hacen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente nos gustaría agradecer a nuestros patrocinadores oficiales por el soporte financiero invalorable que proveen a este proyecto:
- **GOLD Sponsor:** [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [AGH University of Science and Technology, Krakow, Poland](http://www.agh.edu.pl/en)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [WhereGroup GmbH & Co. KG, Germany](http://wheregroup.com/)
- BRONZE Sponsor: [Nicholas Pearson Associates, UK](http://www.npaconsult.co.uk/)
- BRONZE Sponsor: [QGIS Poland, Poland](http://qgis-polska.org/)
- BRONZE Sponsor: [www.terrelogiche.com, Italy](http://www.terrelogiche.com/)
- BRONZE Sponsor: [GeoSynergy, Australia](http://www.geosynergy.com.au/)
- BRONZE Sponsor: [Gaia3D, South Korea](http://www.gaia3d.com/)
- BRONZE Sponsor: [Royal Borough of Windsor and Maidenhead, UK](http://www.rbwm.gov.uk/)
- BRONZE Sponsor: [Chartwell Consultants Ltd, Canada](http://www.chartwell-consultants.com/)
- BRONZE Sponsor: [Trage Wegen vzw, Belgium](http://www.tragewegen.be/)
- BRONZE Sponsor: [GFI - Gesellschaft fr Informations technologie mbH, Germany](http://www.gfi-gis.de/)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.gkg-kassel.de/)
- BRONZE Sponsor: [GIS-Support, Poland](http://www.gis-support.com/)
- BRONZE Sponsor: [ADLARES GmbH, Germany](http://www.adlares.com/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [Customer Analytics, USA](http://www.customeranalytics.com/)
- BRONZE Sponsor: [Avioportolano Italia, Italy](http://www.avioportolano.it/)
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)
- BRONZE Sponsor: [Urbsol, Australia](http://www.urbsol.com.au/)
- BRONZE Sponsor: [MappingGIS, Spain](http://www.mappinggis.com/)
- BRONZE Sponsor: [GIS3W, italy](http://www.gis3w.it/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become and official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## General
### Característica: Nueva ventana de bienvenida
En lugar de simplemente mostrar un lienzo blanco en blanco, QGIS ahora le mostrará una lista de sus proyectos más recientes, junto con miniaturas para que sea mas rápido y fácil volver al trabajo que dejó en su última sesión.

**This feature was developed by:** Matthias Kuhn at [OPENGIS.ch](http://www.opengis.ch)

![image11](images/entries/30f2ab32f4ae0d135a26b6a6ddb6705f0f6dd74a.webp)
### Característica: mejoramiento contínuo a la calidad del código
Mediante el uso de la biblioteca de direcciones saneada, se han identificado y reparado cientos de pérdidas de memoria. Los escaneos de código automatizados que utilizan el Escaneo de cobertura se han utilizado regularmente para identificar posibles problemas, y nuestra densidad de defectos de Cobertura ahora es impresionantemente baja, con solo 0.02 defectos por 1000 líneas de código. La biblioteca de pruebas unitarias automatizadas también ha crecido significativamente durante 2.12, resultando en más regresiones identificadas y reparadas de inmediato. En 2.12 también agregamos pruebas continuas en OSX, para que cada confirmación se pruebe en el conjunto de pruebas unitarias en las plataformas Linux y OSX.

![image12](images/entries/774d1839283f357009c64811bd000e2f8ad97c7a.webp)
### Característica: Editor avanzado de configuración
Se ha agregado un nuevo panel al cuadro de diálogo de configuración que le permite editar cualquiera de las opciones ya definidas en su perfil. Esto está destinado solo a usuarios avanzados ya que podría experimentar un comportamiento inesperado en QGIS si cambia esta configuración sin comprender completamente lo que está haciendo.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

![image13](images/entries/6d59988bf11726192579915cff18f2b81e3f9c8f.webp)
### Característica: Grupos de árboles de capas mutuamente exclusivos
Con esta prestación, puede crear grupos de capas donde solo una capa del grupo sea visible en cualquier momento. La función se puede cambiar individualmente para los grupos en el menú contextual de la vista de capas en árbol.

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esta característica fue financiada por:** Región Toscana (Italia) - SITA (CIG: 63526840AE)

![image14](images/entries/5c68a4deab4d6058d05d3129fec89c6f9abb8530.webp)
### Característica: Filtrado de valores de campo en el widget de expresión
Al crear una expresión que usa valores de un campo, ahora puede filtrar los valores de campo del panel de vista previa .

**Esta característica fue desarrollada por:** Salvatore Larosa

![image15](images/entries/5d41174bdf2a059d41824590520857002a70a056.webp)
### Característica: Soporte de tema para interfaz de usuario
QGIS 2.12 now supports user interface theming support which you can use to customise the appearance of window backgrounds, buttons etc. By default we ship with two themes: **Default** and **Night mapping**. The latter is a dark theme which some people may prefer if they find that light themes cause eye strain. If you know a little CSS you can create your own custom themes fairly easily too\...

Find out more about theming support by reading [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/29/ui-theme-support-now-core-in-qgis/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image16](images/entries/2ec302b12a3b0db8e7a66465afccb227bc543a3e.webp)
### Prestación: Nuevas funciones de expresión en 2.12
A set of functions for \"fuzzy matching\" have been added. These include functions for finding the similarity of two strings and also for performing phonetic matching between strings, and allow you to perform filters for records which \"nearly match\" a specified string.

Se han agregado más funciones basadas en geometría, incluyendo:
- `num_points(geom)` for calculating the number of nodes in a geometry
- `area(geom)`, `length(geom)` and `perimeter(geom)`, for calculating the area, length and perimeter of any geometry object. Previously only calculation of the area, length and perimeter of the current feature\'s geometry was possible.
- `start_point(geom)`, `end_point(geom)`, `point_n(geom, n)`, for retrieving the first, last and numbered points from a geometry
- `make_point(x,y)`, for manual creation of a point geometry
- `x(geom)`, `y(geom)` functions which return the x and y coordinate for point geometries or the centroid x/y for non-point geometries

A new `project_color` function has been added, which allows you to retrieve a color from the project\'s color scheme by name. This lets you create \'linked colors\', where the color of symbol or labeling components can be bound to a color in the project\'s color scheme. Update the color in the scheme, and all the linked colors will be automatically refreshed to match!

Adicionalmente, algunas expresiones muy útiles han sido portadas desde el complemento expresiones+, incluyendo:
- `color_part`: allows retreival of a specific color component (eg red, hue, alpha) from a color
- `set_color_part`: allows a specific color component to be overridden, eg alter the alpha value (opacity) of a color
- `day_of_week`: returns the day of week as a number from a date

Adicionalmente, la ayuda de contexto para funciones de expresión ha sido mejorada para mejor legibilidad.

![image17](images/entries/b56f529af78b2d970f057c2c25ba89b87a85ce85.webp)
### Característica: Variables en expresiones
Ahora puede definir variables personalizadas para usar en expresiones. Las variables se pueden definir a nivel global de aplicación, nivel de proyecto, nivel de capa y nivel de composición. Al igual que las reglas en cascada CSS, las variables se pueden sobrescribir; por ejemplo, una variable de nivel de proyecto sobrescribirá cualquier conjunto de variables a nivel de aplicación. Puede usar estas variables para crear cadenas de texto u otras expresiones personalizadas. Por ejemplo, en el compositor crea una etiqueta con este contenido:

`This map was made using QGIS [% @qgis_version %].` `The project file for this map is: [% @project_path %]`

Representará la etiqueta como ésta:

`This map was made using QGIS 2.12.` `The project file for this map is: /gis/qgis-user-conference-2015.qgs`

You can manage global variables from the `Settings -> Options` menu, and project level variables from `Project properties` (including adding your own custom variables).

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image18](images/entries/19aca1d680543a4013c53ba80406bdd5ebff88c5.webp)
## Herramientas de análisis
### Característica: Se adicionó el número de vértices a campos derivados en la herramienta identificar 
El uso de la herramienta identificar sobre un elemento línea ahora mostrará el número de vértices en el elemento como un atributo derivado adicional.
### Prestación: Herramienta de alineación ráster
This new tool in qgis_analysis library is able to take several rasters as input and:
- reproyectar al mismo SRC
- remuestrea al mismo tamaño de celda y desplazamiento en la cuadrícula (grid)
- recorte a una región de interés
- reescale valores cuando sea necesario

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Kartoza](http://kartoza.com/)

**This feature was funded by:** [DFAT](http://dfat.gov.au) for the [InaSAFE project](http://inasafe.org/)

![image2](images/entries/c613bb210ba0e85eb3b479ab79cd895827c22602.webp)
### Prestación: Complementos Geometry Checker y Geometry Snapper
Hay dos complementos nuevos (que debe habilitar manualmente en el administrador de complementos) disponibles para validar y corregir geometrías. El complemento **Geometry Checker** (en la foto a la derecha) verificará y corregirá su conjunto de datos vectoriales para una variedad de diferentes tipos de errores sistemáticos e intentará resolverlos por usted. Después de resolver un error, la lista de errores se actualiza automáticamente, de modo que si, por ejemplo, corregir un error también resuelve otros errores, todos los errores se eliminan de la lista de problemas.

Con la herramienta **Geometry Snapper** puede alinear los bordes y vértices de una capa vectorial con los bordes y vértices de una segunda capa utilizando una tolerancia definida por el usuario.

**This feature was developed by:** Sandro Mani at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image3](images/entries/319136e65a51c7a8d76adac7aef89806db170c2e.webp)
## Opciones de Aplicación y Proyecto
### Característica: Gestión de contraseña encriptada
QGIS 2.12 introduces a new authentication system (see [PR 2330, QEP 14](https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/qep-14-authentication-system.rst)). Here\'s what is included:
- Contraseña-maestra-configuraciones de autentificación encriptadas almacenadas en una base de datos SQLite 
- Arquitectura del complemento del método de Autentificación(como proveedores de datos)
- Complemento método básico de autentificación
- Complemento básico integrado con conexiones PostGIS y proveedor OWS 
- En línea con la configuración actual de nombre de usuario/contraseña (todavía completamente funcional)
- Configuraciones de conexión a servidor SSL (salvo excepciones o configuraciones personalizadas para errores de conexión SSL)

Autenticación PKI relacionada:
- Importe Certificados de Autorización adicionales, emisores de certificados intermedios y paquetes de identidad personal
- Administrar componentes certificado como en Firefox
- Complementos de método de autenticación para paquetes PEM y PKCS#12 en disco, y para identidades personales almacenadas
- Integrado con conexiones de proveedor OWS (PostGIS y otras bases de datos tomarán un poco más de trabajo)

Para escenarios de proyectos compartidos, incluida la configuración de una unidad de red, puede editar la configuración de la ID de autenticación (authcfg) a algo que se comparta entre los usuarios.

Since the authcfg ID is embedded in the project file, each user just needs to make an auth config that has their specific credentials for that resource, then edit the ID (upon creation of config or after) to the same ID in the project file. Then, when the resource loads, the same configuration will be queried on everyone\'s QGIS, just with their respective credentials for the authentication method used.

Para el cuadro de diálogo Manejar capas malas, los usuarios pueden Agregar/Editar/Eliminar configuraciones de autenticación dentro del cuadro de diálogo y actualizar el URI de la fuente de datos para que coincida. Por lo tanto, en el escenario de un proyecto compartido, el usuario podría agregar inmediatamente una nueva configuración de autenticación apropiada (y ver exactamente qué ID de autenticación compartida debería usarse) al cargar el proyecto.

Currently, the master password auto-set can be set via Python, or by way of a custom C++ plugin, on launch setups using a call to `QgsAuthManager::instance()->setMasterPassword( "mypassword", true )`, or by QGIS_AUTH_PASSWORD_FILE environment variable to set the path to a file with the master password.

**Note:** for Server, you can also use QGIS_AUTH_DB_DIR_PATH to set the path to a qgis-auth.db directory and QGIS_AUTH_PASSWORD_FILE to set the path to a file with the master password on the server.

PKI example docs: <https://github.com/dakcarto/QGIS-Enhancement-Proposals/blob/auth-system/extras/auth-system/pkiuser.rst>

**Esta característica fue desarrollada por:** Larry Shaffer

**This feature was funded by:** [Boundless Spatial, Inc.](http://boundlessgeo.com/)

![image4](images/entries/d6c9305a8dcaea3a5a6c039dec40d50e0caf23ff.webp)
## Navegador
### Característica: Mejoras a conexiones PostGIS en el navegador
El navegador QGIS ahora admite funcionalidades adicionales para conexiones PostGIS, incluida la capacidad de **crear, renombrar y eliminar esquemas**, **soporte para renombrar y truncar capas** y **copiar tablas de un esquema a otro** .

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**Table copying by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image5](images/entries/00820dbcf67c97b61154e7e1f41af0397009b548.webp)
## Proveedores de datos
### Característica: Mejoras en proveedor PostGIS
Se realizaron las siguientes mejoras al proveedor PostGIS:
- Mejoras de rendimiento para el procesador basado en reglas para capas PostGIS
- soporte adicionado para teclas compuestas en vistas

**Compound keys developed by:** Jürgen Fischer at [norBIT GmbH](http://www.norbit.de/)

![image6](images/entries/bc56564581d97034137956cd27e945b3d3ceb3df.webp)
## Gestión de datos
### Característica: Mejoras DBManager
Han habido varias mejoras a la herramienta DB Manager:
- En el Administrador de bases de datos, ahora puede exportar sus datos a cualquier formato de datos compatible con OGR en lugar del Shapefile que solo estaba disponible en la versión anterior.
- Se soporta ahora Oracle Spatial en el DBManager
- Al importar datos en una tabla, puede usar la nueva opción **importar solo entidades seleccionadas** para restringir lo que se importará.
- Las nuevas ventanas de consultas son creadas ahora como pestañas para reducir el número de diálogos

![image7](images/entries/daa22cc4517b58f2457d78781d4dbab12663ce9d.webp)
### Característica: Formateo condicional para celdas de tabla de atributos
This is a major improvement to QGIS\'s attribute table rendering support. You can now style table cells according to rules. For example you can colour all cells with a population of less than 50 000 in red. The option is enabled via a new icon on the table toolbar at the top right of the attribute table window. You can read more about this feature on [Nathan Woodrow\'s blog article](http://nathanw.net/2015/08/20/mixing-a-bit-of-excel-into-qgis-conditional-formatted-table-cells/).

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image8](images/entries/ae9afefda043d31ef7718528d506d98e90e7a1f7.webp)
### Característica: Soporte para rutas relativas en widgets
Para lo siguiente edite tipos de widget:
- Nombre de archivo
- Foto
- Vista web

Si la ruta que se selecciona con el explorador de archivos se encuentra en el mismo directorio que el archivo de proyecto .qgs o inferior, las rutas se convierten en rutas relativas. Esto aumenta la portabilidad de un proyecto QGIS con información multimedia adjunta.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [Alta ehf](http://www.alta.is/)

![image9](images/entries/fcf703990b5cb743ffa5cc7778cb151022ff2d20.webp)
## Digitalizando
### Característica: Mejoras de digitalización
In QGIS 2.10 we mentioned that there is a new geometry architecture for QGIS but that not all features were supported in the digitising tools. With QGIS 2.12 we now have editing support for the **creation of curves / \'circular strings\`**. Note again that you need to be using a data provider (e.g. PostGIS, GML or WFS) that supports curves. These improvements to the digitising tools were also added in QGIS 2.12:
- herramienta para adicionar cadenas circulares con dos puntos y un radio
- herramienta para agregar cadenas circulares con punto de inicio, punto de curva y punto de final
- permite que escape cancele dibujado de nuevos elementos
- muestra una tabla de nodos al editar con la herramienta de nodos, lo que le permite ingresar manualmente las coordenadas exactas x e y para los nodos, así como los valores de z y m (según el tipo de capa)

Además, se actualizaron más herramientas de edición y modificación de geometría para que funcionen correctamente con capas que contienen dimensiones z o m.

**This feature was developed by:** Marco Hugentobler at [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [Canton of Solothurn](http://www.sogis.so.ch/)

![image10](images/entries/215ead2dd5e43e394d47169a7fd82aa5cc08b6b6.webp)
## Etiquetando
### Feature: Data defined quadrant when in \"around point\" mode
Ahora es posible especificar un cuadrante definido de datos cuando una etiqueta de punto se establece en el modo de colocar Punto de referencia. Esto le permite anular manualmente la ubicación del cuadrante para una etiqueta específica mientras permite que las etiquetas restantes vuelvan a la ubicación automática.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image19](images/entries/27a58b65cf449505c92cc6c8470a93d1f09893a1.webp)
### Característica: Dibujar solo etiquetas que caben dentro de polígonos
Se ha agregado una opción a las capas de polígono para dibujar solo etiquetas que se ajusten completamente a las entidades poligonales.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image20](images/entries/5c8461abe3aa5483c3243c0f145940b0d5fd1310.webp)
### Característica: Controlar prioridad de obstáculos de etiquetado
In 2.12 it\'s now possible to specify the priority for labeling obstacles. This allows you to make labels prefer to overlap features from certain layers rather than others. The priority can also be data defined so that certain features are more likely to be covered than others. You can also use data defined expressions or fields to control whether a specific feature in layer will act as an obstacle for labels.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image21](images/entries/f07a082bd4e62f059788c18a9de353107b8bdc44.webp)
### Característica: Nuevas opciones para controlar como actúan las capas polígonos como obstáculos
New options have been added to control how labels should be placed to avoid overlapping the features in polygon layers. The options are to either avoid placing labels over polygon interiors or avoid placing them over polygon boundaries. Avoiding placing labels over boundaries is useful for regional boundary layers, where the features cover an entire area. In this case it\'s impossible to avoid placing labels within these features and it looks much better to avoid placing them over the boundaries between features instead. The result is better cartographic placement of labels in this situation.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image22](images/entries/e37943c654080e33219acb5e519970cf748c87bf.webp)
### Prestación: Control definido por datos sobre prioridad de etiqueta
Esta característica solicitada a menudo permite a los usuarios establecer la prioridad para etiquetas individuales. En versiones anteriores, QGIS permitía establecer la prioridad de la etiqueta para una capa completa, pero no había ninguna opción para controlar la prioridad de las características dentro de una capa. ¡Ahora, puede usar una expresión o campo definido por datos para priorizar el etiquetado de ciertas características sobre otras dentro de una capa!

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image23](images/entries/bd185cde38420f50fb540d742d178768d28ac577.webp)
### Característica: Opción para capas solo obtáculo
This allows users to set a layer as just an obstacle for other layer\'s labels without rendering any labels of its own. It means that a non-labelled layer can act as an obstacle for the labels in other layers, so they will be discouraged from drawing labels over the features in the obstacle layer, and allows for improved automatic label placement by preventing overlap of labels and features from other layers.

In the screenshot you can see that the Streets have the option \"Discourage other labels from covering features in this layer\" enabled. The red labels derived from polygon geometries are thus placed to avoid intersection with the street axis. You have to enable \"Horizontal\" or \"Free\" on the polygon layer in order to achieve proper results.

Note, that it is also possible to both label a layer, but also act as obstacle layer, by enabling the checkbox \"Discourage labels from covering features\" in the \"rendering\" tab of the label settings.

See [this article](http://nyalldawson.net/2015/07/recent-labelling-improvements-in-qgis-master/) for more details.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image24](images/entries/de1eae1359ce92045d51c6fa9bc3f014a3f3ae67.webp)
### Característica: Etiquetado basado en reglas
Las etiquetas de las características ahora se pueden diseñar usando reglas para agregar aún más control sobre la colocación y el estilo de las etiquetas. Al igual que la representación cartográfica basada en reglas, las reglas de etiquetas se pueden anidar para permitir opciones de estilo extremadamente flexibles. Por ejemplo, puede renderizar etiquetas de manera diferente según el tamaño de la entidad en la que se representarán (como se ilustra en la captura de pantalla).

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esta característica fue financiada por:** Región Toscana (Italia) - SITA (CIG: 63526840AE)

![image25](images/entries/8846f57f0395e7f6b2543a92a5c55b67e8b19923.webp)
## Compositor de Mapa
### Característica: Mejoras en la navegación del atlas
You can now set a field or expression as the \"page name\" for atlas compositions. A page number combobox has been added to the atlas toolbar, which shows both a list of available page numbers and names. This allows you to jump directly to a specific page within your atlas.

El nombre de la página también se puede usar dentro de las expresiones de simbología y etiquetado para permitir un estilo avanzado de las características del atlas en función de su nombre de página.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image26](images/entries/bbf6147ef8be9d209fa188d6c524bce9d13d5ba8.webp)
### Característica: Formato personalizado para anotaciones de cuadrícula
Las anotaciones de cuadrícula del compositor de mapa ahora se pueden formatear en formatos personalizados, que se evalúan utilizando el motor de expresión. ¡Ahora utiliza cualquier formato esotérico de numeración de cuadrícula que requieran sus mapas!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image27](images/entries/a6cd03594ca802015ef4a5bf7806cc1ce291214b.webp)
### Prestación: Manejo de texto multilínea y ajuste automático de texto en tablas de atributos del compositor
Las tablas de atributos del Compossitor ahora incluyen soporte completo para cadenas de varias líneas. También se ha agregado control sobre la alineación vertical del texto dentro de una celda, junto con opciones para ajustar el texto en ciertos caracteres o calcular automáticamente el ajuste del texto para que se ajuste al tamaño de las columnas. Para aplicar el ajuste automático de texto con alturas de fila automáticas, establezca el ancho de columna en un tamaño fijo.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image28](images/entries/db66b56f79949779ea32126bd22f2f1c9d4b55e6.webp)
### Característica: Personalización avanzada del color de fondo de celda
Este cambio permite a los usuarios establecer diferentes colores para alternar filas y columnas, primera/última fila/columna y fila de encabezado dentro de las tablas de atributos del compositor.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [Ville de Morges](http://www.morges.ch/)

![image29](images/entries/68266f6b11599dfa226952455ca150448a5d082a.webp)
### Prestación: Opción Añadir ajuste de página a contenido y opciones para recortar exportaciones a contenido
Se ha agregado una nueva opción en el panel de composición para redimensionar una composición a sus contenidos, con márgenes extras opcionales si lo requiere.

Composer exports can also be cropped to their contents. If selected, this option will make the images output by composer include only the area of the composition with content. There\'s also an option for margins to add around the item bounds if required.

If the composition includes a single page, then the output will be sized to include EVERYTHING on the composition. If it\'s a multi-page composition, then each page will be cropped to only include the area of that page with items.

Se ha agregado un nuevo cuadro de diálogo de opciones de exportación de imágenes para facilitar esto, que también incluye atajos útiles para ignorar la resolución de impresión o las dimensiones de la imagen exportada.

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image30](images/entries/38572cf4aa662cc4463c2a29f3d5ca38aa382632.webp)
### Característica: Forzar capas vector a ser representadas como imágenes ráster
A new option has been added under the layer properties, rendering tab to force a vector layer to render as a raster. Extremely detailed layers (eg polygon layers with a huge number of nodes) can cause composer exports in PDF/SVG format to be huge as all nodes are included in the exported file. This can also make the resultant file very slow to work with or open in external programs. Now, you can force these layers to be rasterised on a layer-by-layer basis, so that the exported files won\'t have to include all the nodes contained in these layers. The end result is smaller file sizes and PDFs/SVGs which are faster to open.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image31](images/entries/0127fe10ecae31dbcd133492c93f33b0d569dcba.webp)
### Característica: Control definido por datos sobre capas de mapas y estilos preestablecidos
Se ha agregado un nuevo control de datos definidos para que las capas del mapa y los preajustes de estilo se muestren en el compositor de mapa. La expresión definida de datos de capas de mapa debe dar como resultado una lista delimitada de nombres de capa que se mostrarán en el mapa, o la expresión definida de datos de estilo preestablecido debe dar como resultado el nombre de un estilo preestablecido existente.

Using this control over map layers allows for \"layer-based\" atlases, where the map layers should change between atlas pages instead of or in combination with the map extent changing. An example could be an atlas looping over different administrative units and at the same time looping over several historic maps or aerial images.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image32](images/entries/a8dc3b35df4020897e39c81bd22a469ab5ea6225.webp)
### Característica: Opción para esconder páginas de ver/exportar
There\'s now an option to hide the display of pages while editing and exporting compositions. This option is useful for compositions which aren\'t intended for print and are not bound by any preset page sizes. You can hide the pages, then add and resize items in any way you desire without the visual distraction of page boundaries!

**Sponsored by:** [NIWA](https://www.niwa.co.nz/)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Plugins
### Característica: Actualización del complemento GRASS
El complemento GRASS se actualizó para permitir la compatibilidad con GRASS 7. Las capas de GRASS se pueden examinar y cargar desde el navegador QGIS o desde el panel del navegador. Los datos vectoriales de GRASS se pueden editar directamente dentro de QGIS. El proyecto contiene los siguientes paquetes de trabajo:
- Actualización de biblioteca de complemento y construcción multiversión
- Integración explorador QGIS y panel de explorador
- Soporte para conjuntos de mapas, módulos y shell para permitir análisis de datos
- edición vector

Para los usuarios de GRASS 6 y GRASS 7, descubrirá que la integración entre GRASS y QGIS es mucho más fluida. Puede crear capas de GRASS directamente en el panel del navegador QGIS, diseñar capas de vectores de GRASS utilizando herramientas de estilo QGIS estándar y utilizar herramientas de digitalización QGIS conocidas para crear nuevas geometrías de vectores en un conjunto de mapas de GRASS.

See also [QGIS GRASS Plugin Upgrade project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/) and [progress report](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/progress.html)

**This feature was developed by:** [Radim Blazek](http://www.gissula.eu/)

**This feature was funded by:** Crowd funding, see [project page](http://www.gissula.eu/qgis-grass-plugin-crowdfunding/)

![image33](images/entries/fb9ac25e9ca6c5e4030167e289435e995f5af8f5.webp)
## Programabilidad
### Feature: Map tools moved from app-\>gui
Este cambio permite reutilizar herramientas de mapa desde los scripts PyQGIS y complementos Python.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)

**This feature was funded by:** [SIGE](http://www.sige.ch/)
### Característica: Editar capas mediante \`with edit(layer):\`
Ejemplo:

    from qgis.core import edit
    
    with edit(layer):
       f=layer.getFeatures().next()
       f[0]=5
       layer.updateFeature(f)
    
Esto llamará automáticamente commitChanges() al final. Si ocurre alguna excepción, hará rollBack() de todos los cambios.

**This feature was developed by:** Matthias Kuhn at [OpenGIS](http://www.opengis.ch/)
### Característica: Nueva API para el motor de etiquetado (QgsLabelingEngineV2)
La idea es hacer un motor mas flexible comparado con la implementación QgsPalLabeling:
> - Comunicación resumida con etiquetas/diagramas de texto desde el propio motor
> - permite múltiples tipos de etiquetas por capa
> - soporte de proveedores personalizados de etiqueta (ej. implementado por complementos)
> - hacer el motor de etiquetado independiente del motor de reproducción del mapa
> - facilita la prueba automática del motor de etiquetado y sus componentes

See [blogpost](http://www.lutraconsulting.co.uk/blog/2015/10/25/rule-based-labeling/) for more details

**This feature was developed by:** Martin Dobias at [Lutra Consulting](http://www.lutraconsulting.co.uk/) on subcontract to [Gis3W](http://www.gis3w.it/)

**Esta característica fue financiada por:** Región Toscana (Italia) - SITA (CIG: 63526840AE)
### Característica: Abrir scripts en editor externo
Alégrense pythonistas - ahora pueden abrir sus scripts en un editor externo usando el nuevo botón adicionado a la consola.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image34](images/entries/78acf0058f4306bf408a58df3762dff5986633a7.webp)
### Característica: Nuevas clases para programas PyQGIS
Se ha agregado una nueva clase QgsStringUtils que permite que los scripts PyQGIS utilicen los nuevos algoritmos de coincidencia difusa agregados en 2.12. Estas incluyen funciones para encontrar la distancia de edición de Levenshtein entre dos cadenas y para calcular la representación fonética de una cadena. ¡Estos algoritmos han sido altamente optimizados para el rendimiento, por lo que están listos para que comience la coincidencia difusa en millones de cadenas!

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)
## Servidor de QGIS
### Característica: API Python del Servidor QGIS
QGIS Server ahora está empaquetado como una biblioteca con una API inicial (pero creciente) y enlaces de Python. Con la nueva API tenemos un conjunto de muestras de Python para el componente principal del servidor y para los complementos del servidor. Invocar el servidor desde Python ahora es tan fácil como:

    from qgis.server import QgsServer
    headers, body =  QgsServer().handleRequest(my_query_string)
    
For more information see [this article](http://www.itopen.it/qgis-server-binding-news/)

**This work has been developed and funded by**: Alessandro Pasotti at [ItOpen](http://www.itopen.it/)
### Característica: getMap en formato dxf
Ahora es posible recuperar el resultado de una solicitud GetMap WMS en formato DXF. Es compatible con las mismas características y opciones disponibles en el escritorio QGIS. Con las mismas limitaciones.

| Sample URL: | `http://yourserver.org/cgi-bin/qgismapserver.fcgi?` | `map=/path/to/your/projectfile.qgs&` | `SERVICE=WMS&` | `VERSION=1.3.0&` | `REQUEST=GetMAP&` | `FORMAT=application/dxf&` | `FORMAT_OPTIONS=SCALE:500;MODE:SYMBOLLAYERSYMBOLOGY&` | `FILE_NAME=youroutputfilename.dxf&` | `CRS=EPSG:EPSG:21781&` | `BBOX=695558.73070825,244430.77224034,697158.88528251,245722.25976142&` | `WIDTH=1042&` | `HEIGHT=841&` | `LAYERS=yourdxfexportlayers`

See also [QGIS as OGC data server](http://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_server_support.html#dxf-export) for all the available options.

En el pantallazo puede ver el QGIS Web Client en la izquierda con la funcionalidad de exportar DXF (usando el servidor QGIS) y la misma extensión en Autodesk TrueView a la derecha.

**This feature was developed by:** Marco Hugentobler [Sourcepole AG](http://www.sourcepole.ch/)

**This feature was funded by:** [City of Uster](http://gis.uster.ch/)

![image35](images/entries/beb2e9c00102c67ae703eac097ffba8866379609.webp)
## Simbología
### Característica: Exportar imágenes miniaturas desde el administrador de de estilo
El administrador de estilo le permite ahora exportar imágenes miniatura con estilo seleccionado como imágenes SVG o PNG.

**This feature was developed by:** [Nathan Woodrow](http://nathanw.net/)

![image36](images/entries/8861a040751804f6c2691ee4d93d410efd6d99ac.webp)
### Característica: Nueva opción para limitar el tamaño en mm cuando usa tamaños de unidades de mapa
Préviamente solo la opción de limitar el rango de escala del tamaño de la unidad del mapa estaba disponible. Ahora además puede elegir limitar el tamaño renderizado en mm.

![image37](images/entries/b822235ddb09b4184b926bf2e0acc5c892147d0b.webp)
### Característica: Mejoras al renderizador de desplazamiento
- Permitir tolerancia en mm/píxles para el renderizador de desplazamiento
- Permite establecer transparencia para colores
- Modo de colocación de anillo concéntrico (permite un despliegue más compacto que sólo con anillos)

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image38](images/entries/33b5f15429279a7ec75dd1f6a2e01b1a7df789ca.webp)
### Característica: todas las rampas de colores pueden ahora editarse
In QGIS 2.12 \"edit\" buttons have been added next to every color ramp choice. This allows you to easily edit an existing color ramp without having to create a new ramp and overwrite the existing one.

![image39](images/entries/6ca1426e6e9bfd5500b08fb2185ae50a77258892.webp)
### Característica: Manejo mejorado del borde de marcador SVG
QGIS 2.12 arregla una serie de problemas respecto al manejo de bordes dentro de símbolos de marcador SVG y relleno SVG.

Las versiones anteriores de QGIS representaban los contornos en un tamaño significativamente menor que el establecido, y el dibujo de SVG con tamaños de contorno en unidades de mapa estaba averiado.

These issues have been fixed in QGIS 2.12, but as a result you may need to update your project symbology if you\'ve previously set oversized outlines for your symbols to overcome these bugs. In the image you see QGIS 2.12 vs QGIS 2.10 SVG markers in the symbol layer dialogs.

![image40](images/entries/a678d22393345b4fcc07b5bd023babe383151b46.webp)
### Característica: Adicionar píxeles como opción para todas las elecciones de unidad de tamaño en simbología
For all size input widgets there is now a third option \"pixel\", next to \"mm\" and \"map units\". This concerns symbol sizes, stroke widths, dash sizes, offsets, etc. This may help, if you design for screens and not for print output.

**This feature was developed by:** [Nyall Dawson](http://nyalldawson.net/)

![image41](images/entries/cbc683061bcc06764361ab79874f1020ccfe8eb7.webp)

{{<content-end >}}
