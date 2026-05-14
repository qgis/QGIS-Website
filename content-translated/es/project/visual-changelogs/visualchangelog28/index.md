---
HasBanner: false
draft: false
releaseDate: '2015-02-20'
section: proyecto
sidebar: true
title: Registro de cambios para QGIS 2.8
type: visual-changelog

---
{{<content-start >}}
# Registro de cambios para QGIS 2.8{#changelog28 }
Fecha de lanzamiento: 2015-02-20

This is the change log for the next release of QGIS - version 2.8 \' Wien\'. Wien is German for \'Vienna\' - host city to our developer meet up in November 2009 and again in March 2014.

**Lanzamiento a Largo Plazo**

This is a special release since it is designated an \'LTR\' (Long Term Release). LTR releases will be supported with backported bug fixes for one year, and will be in permanent feature freeze (i.e. no new features will be added, only bug fixes and trivial updates).

El propósito de los lanzamientos de LTR es proporcionar una plataforma estable y que cambie con menos frecuencia para empresas y organizaciones que no desean lidiar con la actualización de las habilidades de los usuarios, materiales de capacitación, etc. más de una vez al año. El éxito de la LTR depende de ustedes, nuestros queridos usuarios: necesitamos su apoyo para ayudar a financiar las correcciones de errores y asegurarnos de que en sus contratos de soporte con proveedores de soporte especifique que las correcciones de errores realizadas en su nombre se aplican a la rama LTR así como nuestra rama de desarrollo normal.

Si un LTR es importante para usted, considere también apoyar directamente el proyecto QGIS, o aliente a su proveedor comercial a usar LTR como base para su solución empresarial para que todos puedan beneficiarse de una plataforma estable que se mejora y refina continuamente. Tenga en cuenta que para los usuarios y organizaciones que les gusta vivir al límite, nuestros lanzamientos regulares de cuatrimestrales continuarán sin cesar.

**Nuevas Características**

QGIS 2.8 también es una versión especial porque incluye muchas características nuevas, ajustes y mejoras para hacer que el SIG de escritorio gratuito más popular sea aún más completo y útil.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

**Gracias**

Nos gustaría agradecer a los desarrolladores, documentadores, probadores y a las muchas personas que ofrecen su tiempo y esfuerzo voluntario (o financian a personas que lo hacen).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Finalmente nos gustaría agradecer a nuestros patrocinadores oficiales por el soporte financiero invalorable que proveen a este proyecto:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- SILVER Sponsor: [Office of Public Works, Ireland, Ireland](http://www.opw.ie/)
- BRONZE Sponsor: [GIS3W, Italy](http://www.gis3w.it/)
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
- BRONZE Sponsor: [Faculty of Geology, Geophysics and Environmental Protection, AGH, ​University of Science and Technology, Poland](http://www.wggios.agh.edu.pl/en)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS es software gratuito y no tiene la obligación de pagar nada por usarlo; de hecho, queremos alentar a las personas a utilizarlo independientemente de su estado financiero o social, creemos que empoderar a las personas con herramientas de toma de decisiones espaciales dar como resultado una sociedad mejor para toda la humanidad.

{{<table-of-contents >}}
## General
### Característica: Ingrese expresiones en las cajas de girado
When editing attributes in the **attribute table or forms**, you can now enter expressions directly into spin boxes, e.g. `5 * 2.5` and they will be automatically evaluated.

![](images/entries/e094287244ee1fe161c8ca95951c2d11ca1e6cdd.webp)
### Característica: Pueden importarse/exportarse marcadores
Ahora es posible guardar / cargar sus marcadores en un archivo. Esto facilita compartir ubicaciones marcadas o transferirlas entre computadoras.

**Esta característica fue desarrollada por:** Salvatore Larosa

![](images/entries/e3d35c32da659821bc0c657b8e7ba40587a1bfb2.webp)
### Característica: Mejoras a expresiones
- **Integer division produces a double when required**: Previously dividing two integers in an expression would always result in an integer value, i.e. `5 / 2 = 2`. Now the result will always be double when required, so `5 / 2 = 2.5`, which is much more expected for users. A new integer divide operator - `//` has been added to mimic the old behaviour, i.e. `5 // 2 = 2`.
- **New \'if()\' function**: There is now a new `if(cond, true, false)` expression
- **Evaluación floja para expresiones**
- **Added get and transform geometry**: These new keywords can be used with `getFeature` for some geometry tests like intersects, crosses, contains, etc.
- `geometry` - returns the feature\'s geometry
- `transform` - returns the transformed geometry

![](images/entries/ec56f9b8331e619ad1a44970fde655b68125f9d8.webp)
### Característica: marco de prueba continua y mejoras de QA
In our ongoing quest to improve the stability and quality of QGIS, every commit is now tested against a growing test suite to identify regressions automatically. In the image on the right you can see the list of incoming pull requests on our GitHub page are now automatically annotated with a check or cross based on whether our test suite successfully ran on [Travis.ci](https://travis-ci.org/qgis/QGIS) when the pull request is made or updated.

Ahora también realizamos regularmente análisis de Coverity de la base de código QGIS. Como resultado de esto, hemos identificado y solucionado más de 1000 problemas marcados, incluidas pérdidas de memoria y posibles bloqueos. QGIS tiene una densidad de defectos de 0.01, mientras que el promedio para programas de tamaño similar es de aproximadamente 1.0.

![](images/entries/4ec86080ff150743f1bdc88d3ac7881a6cd405de.webp)
## Herramientas de análisis
### Característica: Mejoras al diálogo de medición
La herramienta de medida se ha mejorado para que ahora pueda seleccionar qué unidades se deben usar en el cuadro de diálogo de medida. También hay una nueva sección de información en el cuadro de diálogo que muestra qué configuraciones se están utilizando durante los cálculos de medición.

![](images/entries/67a001d3d800feec8805de698ed364e91d00daab.webp)
## Navegador
### Navegador más responsivo
In the QGIS Browser items are now expanded in their own threads, speeding up the load time of the browser and making the browser more responsive. Navigating PostGIS sources is now much faster in the browser. The animated snapshot to the right (click image to see the animation) shows the loading of two slow WMS servers in parallel . The browser\'s state (tree expansion) is restored on startup.

**Esta característica fue desarrollada por:** Radim Blazek

![](images/entries/c8df646572084b8f12027fd54c1210f14c80c8e1.gif)
## Proveedores de datos
### Característica: Soporte para gráficos leyenda WMS contextuales
If your WMS server supports contextual legends, you can make use of them in QGIS now too. Contextual legends are getLegendGraphic requests which return only the relevant legend for your current view extent, and thus do not include legend items for things you can\'t see in the current map.

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/e516a25492b547113c487d00475cfe07bc7b131e.webp)
## Gestión de datos
### Característica: Prefijos personalizados para uniones
Ahora puede definir un prefijo personalizado en el administrador de combinaciones en el cuadro de diálogo de propiedades de capa. Al usar un prefijo, la tabla de atributos mostrará nombres de atributos junto con su prefijo preferido.

![](images/entries/372e6561a4db3ed3ca3d418c946f81bce0d0d134.webp)
### Característica: Soporte para la creación de capas temporales de memoria
This release add support for creating new temporary scratch layers within QGIS core. Scratch layers can be created in the `Layer --> Create layer --> New Temporary Scratch Layer` menu option.

![](images/entries/bddbbd6cb55e9a19441ea564275dd480661e61de.webp)
### Característica: Soporte para cálculos en filas seleccionadas
En la tabla de atributo ahora puede hacer cálculos en las filas seleccionadas solo gracias al nuevo botón adicionado a la barra de la calculadora de campo.

![](images/entries/1b7ead001901ed4242d26556abac055834e367b2.webp)
## Digitalizando
### Característica: Herramientas avanzadas de digitalización
Si alguna vez deseó poder digitalizar líneas exactamente paralelas o en ángulos rectos, bloquear líneas en ángulos específicos, etc. en QGIS, ¡ahora puede hacerlo! Las herramientas de digitalización avanzadas son un puerto del complemento CADinput y agrega un nuevo panel a QGIS. El panel se activa al capturar nuevas geometrías o partes de geometría

![](images/entries/50f726e5899eb72dcec76e4bed1936bcf957e75f.webp)
### Característica: Herramienta simplificar mejorada
La herramienta simplificar ha sido revisada, adicionando:
- Soporte reproyección al vuelo
- el usuario puede especificar la tolerancia exacta (no sólo un valor relativo disparatado)
- tolerancia puede ser especificada tanto en unidades de mapas, unidades de capa o píxeles
- definiciones de tolerancia se almacenan en configuración
- simplificar múltiples entidades a la vez (arrastre un rectángulo en vez de solamente pinchar)
- soporte para entidades multipartes
- estadística sobre la reducción del número de vértices

**This feature was funded by:** [Tracks for Africa](http://tracks4africa.com/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/20b7f96ffc7d37b8c2ae09189d7957a929a716e5.webp)
### Característica: Mejoras del alineado
There is a new snapping mode : **snap to all layers** which makes it quick to enable snapping between all layers. Also the underlying snapping architecture of QGIS has been overhauled making snapping much faster on large projects and improving the precision with which snapping takes place. ​There's also less confusion with snapping tolerances being to map units or layer units, so those anticipated 1 metre tolerances don't become 1 degree tolerances without you knowing.

**This feature was funded by:** [Ville de Vevey, SITNyon](http://www.vevey.ch/) and [QGIS Usergroup Switzerland](http://www.qgis.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/8454af2743154585eb82325ab2694e50e7d9efcd.webp)
## Leyenda de capa
### Feature: Show rule-based renderer\'s legend as a tree
Advanced users who leverage QGIS\'s rule based renderer system will be pleased to see that the rules are now presented as a tree in the legend. Better still, each node in the **tree** can be **toggled on/off** individually providing for great flexibility in which sublayers get rendered in your map.

**This feature was funded by:** [SIGE](http://www.sige.ch/)

**This feature was developed by:** [Lutra Consulting](http://www.lutraconsulting.co.uk/) in cooperation with [Kartoza](http://kartoza.com/)

![](images/entries/0d39448aa0893d7a71c5241aa2181750535e62c3.webp)
## Compositor de Mapa
### Característica: Mejoras del IGU del Diseñador
- View menu option to **hide bounding boxes**. This allows users to hide the bounding boxes for selected items within a composition. It\'s a handy feature for allowing interaction with items while previewing exactly how they will look when the composition is exported, without large boxes blocking the view.
- **Modo pantalla completa para diseñador**
- Option to **toggle display of panels** in composer, available by both the `view menu`, using the shortcut `F10` and by pressing `Tab` when the composer canvas is selected. It\'s useful for maximising the space when planning a map layout.

![](images/entries/10677c6e1612a4392e8bca0a9cbe31126426becf.webp)
### Característica: Mejoras grid
En el compositor ahora tiene un control más fino de la visualización de cuadros y anotaciones. Anteriormente, para mapas rotados o cuadrículas reproyectadas, el compositor dibujaría todas las coordenadas para cada lado del mapa. Esto dio como resultado una combinación de coordenadas de latitud/y y longitud/x que se muestran en un lado. Ahora puede controlar si desea todas las coordenadas, solo latitud o longitud solo para cada lado del marco del mapa. También se han agregado opciones similares para controlar cómo se divide la cuadrícula de un marco del mapa.

Nueva dirección descendente vertical para anotaciones. Este cambio agrega un nuevo modo de dirección vertical descendente para las anotaciones de cuadrícula del mapa. Anteriormente, solo se admitía texto ascendente para las anotaciones verticales.

![](images/entries/288d533cbed1f6beeef17004897060c8639bbbb4.webp)
### Característica: Márgenes de elementos etiqueta
- Ahora puede controlar los márgenes **horizontales y verticales para elementos de etiqueta**. Anteriormente, solo se aplicaba una configuración de margen único a los márgenes horizontales y verticales. Este cambio permite a los usuarios especificar diferentes márgenes horizontales y verticales.
- You can now specify negative margins for label items, **allowing text to be drawn slightly outside of a label item\'s bounds**. This is desirable for aligning label items with other items while allowing for optical margin alignment for the label type.

![](images/entries/7f4905d74ca140ed369bea8866357b9d952ee212.webp)
## Plugins
### Característica: mejoras a consola Python
You can now drag and drop python scripts into QGIS window and they will be executed automatically. We also added a toolbar icon to the plugins toolbar and a shortcut ( `Ctrl-Alt-P` ) for quick access to the python console.

![](images/entries/03be8f30ce341816bd3bcd1a58f3b913ddcea07c.webp)
## Procesado
### Característica: Nuevo tipo de parámetro del predicado geométrico
Con este nuevo tipo de parámetro, utilizado en los algoritmos **Seleccionar por ubicación, Extraer por ubicación** y **Atributos por ubicación**, el usuario puede seleccionar con precisión el operador espacial a utilizar.

**This feature was funded by:** [French Ministry of Ecology, Sustainable Development and Energy](http://www.developpement-durable.gouv.fr/)

**This feature was developed by:** [Camptocamp](http://www.camptocamp.com)

![](images/entries/cd198b98cf28e611f5c2e3be93bc5ec90dd0a5b4.webp)
### Característica: Nuevos algoritmos
Varios nuevos algoritmos han sido adicionados al marco de procesamiento:
- Algoritmo **puntos regulares** (atiende #5953)
- Algoritmo **diferencia simétrica** (atiende #5953)
- Algoritmo **división vector** (atiende #5953)
- Algoritmo **cuadrícula vector** (atiende #5953)
- Algoritmo de cálculo de **curvas hipsométricas**
- **Dividir líneas con líneas**
- **Campos de refactorización** algoritmo de manipulación de atributos

![](images/entries/b2403fae20cd24cfb1883d24e97de6fc51e40c88.webp)
## Programabilidad
### Característica: Adicionar funcionalidad comentario a expresiones
Comments can now be added to expressions using an SQL style `--` prefix.

![](images/entries/e1579eec6d8ab74330fb2f784c68ed16c83bb79d.webp)
### Prestación: Editor de función de expresión personalizado
You can now define custom expression functions in the expression widget. See [this blog post](http://nathanw.net/2015/01/19/function-editor-for-qgis-expressions/) for more details.

![](images/entries/503dd9dadec4fb85ee5ab6335e4f03979a8e7d77.webp)
### Característica: Soporte Qt5
QGIS ahora puede construirse usando bibliotecas Qt5. Note que actualmente la mayoría de los binarios aún estarán con Qt4 por defecto.

![](images/entries/c702d89260cbab35323c052a15ab5c5728fc7115.webp)
### Característica: Carga en masa de índice espacial
En la API, hemos agregado soporte para la carga masiva de índice espacial. Esta es una forma mucho más rápida de inicializar un índice espacial. Desde python es tan simple como:

`index = QgsSpatialIndex( layer.getFeatures() )`

De una simple prueba con 50K puntos en una capa memoria:

**bulk loading \~ 100 ms**

inserting features \~ 600 ms

El árbol índice también debería en teoría estar mejor construido y podría resultar en vistas más rápidas.

![](images/entries/80cea18c68b7885cb71c1682ca3777caa048ff9e.webp)
### Característica: Ejecutar solo la parte seleccionada de una consulta SQL
In the DB Manager SQL editor, it is now possible to highlight a portion of the SQL and only that portion will be executed when you press `F5` or click the `run` button

![](images/entries/0d1343e84aa0946becab1e37880a58ceeffbd491.webp)
## Servidor de QGIS
### Característica: Complementos servidor python
El soporte de complementos de Python para el servidor QGIS acerca el poder de python al lado del servidor, permitiendo un desarrollo y despliegue rápido y eficiente de nuevas características.

**This feature was developed by:** [Alessandro Pasotti (ItOpen)](http://www.itopen.it/)
### Característica: Soporte para estilos de capa
- Servidor QGIS ahora soporta estilos predefinidos de capa en pedidos GetMap
- QGIS Server ahora soporta múltiples estilos en pedido GetStyles (vea sección simbología abajo)

### Característica: Adiciona Método DescribeLayer a WMS
**Perfil de descriptor de capa estilizada del servicio de mapas web: DescribeLayer**

<http://www.opengeospatial.org/standards/sld>

La definición de un estilo definido por el usuario requiere información sobre las características que se simbolizan, o al menos su característica/tipo de cobertura. Dado que los estilos definidos por el usuario se pueden aplicar a una capa con nombre, debe existir un mecanismo por el cual un cliente pueda obtener información de tipo de característica/cobertura para una capa con nombre. Este es otro ejemplo de cerrar la brecha entre los conceptos de capas y estilos de WMS y los conceptos de WFS/WCS, como el tipo de característica y la capa de cobertura. Para permitir esto, un WMS puede admitir opcionalmente la solicitud **DescribeLayer**.

Se ha pensado que el método DescribeLayer es mas acertado que sobrecargar aún más el documento de capacidades WMS.

Para cada capa nombrada, la descripción debe indicar si realmente se basa en datos de entidades y, de ser así, debe indicar el WFS/WCS (mediante un prefijo de URL) y los tipos de entidades/cobertura. Tenga en cuenta que es perfectamente válido que una capa con nombre no se pueda describir de esta manera.
## Simbología
### Prestación: Tipo de llenado de imagen ráster
Este nuevo tipo de símbolo de capa permite rellenar polígonos con un (mosaico) de imagen ráster.

Las opciones incluyen nombre de archivo (datos definidos), opacidad, tamaño de imagen (en píxeles, mm o unidades de mapa), modo de coordenadas (función o vista) y rotación.

![](images/entries/3c372b247f1f5583768532c2be96f169dcff1e8f.webp)
### Característica: Renderizador vivo de mapa de calor
El nuevo visualizador mapa de calor de capa vector permite mapas de calor vivos, dinámicos para capas puntos.

Las opciones incluyen la especificación del radio del mapa de calor en píxeles, mm o unidades de mapa, la elección de la rampa de color, los puntos de ponderación por campo y un control deslizante para seleccionar un ratio entre la velocidad de renderización y la calidad.

![](images/entries/a13862e4cf8707ec70ddb37a8e3e824db6af883d.webp)
### Característica: Múltiples estilos por capa
It is now possible to set multiple styles for a layer and then easily toggle between them. This functionality is available in the `legend context menu --> styles sub-menu` where it is possible to add/remove styles and quickly switch between them. Layer sets remember styles, and different styles can also be applied to individual composer map items. The multiple styles defined are also available when the project is served via QGIS Server as a WMS layer. For more information on this see also this [blog post](http://www.lutraconsulting.co.uk/blog/2015/02/19/towering-qgis-release/).

**This feature was funded by:** [Regione Toscana](http://www.regione.toscana.it/)

**This feature was developed by:** [Gis3W](http://www.gis3w.it/), [Lutra Consulting](http://www.lutraconsulting.co.uk/)

![](images/entries/e6d0058bbae51c52fb9fffc79d4cc459fbaf853b.webp)
### Característica: Más configuración de simbología definida por datos
Se ha mejorado la interfaz de usuario para la configuración de simbología definida por datos: moviendo la opción definida por datos junto a cada propiedad definible de datos (de acuerdo con otras partes de QGIS como las propiedades de etiquetado). Además, se han hecho muchas propiedades nuevas como datos definibles para simbología. Esta mejora de la interfaz de usuario también proporciona una forma de ver de inmediato si se define una anulación definida por datos así como un acceso más fácil a las configuraciones definidas por datos.

![](images/entries/1af9b133ea80a4469e9be81107449b0e22df442b.webp)
### Característica: Exportación DXF: mejora exportación símbolo marcador
Se ha mejorado la funcionalidad del exportador de archivos DXF, con mayor fidelidad de los símbolos de marcador exportados a la simbología original QGIS.
### Característica: Rotación de mapa en tela, rotación mejorada en diseñador
Esta versión incluye soporte preliminar para la rotación del lienzo del mapa. Puede rotar el lienzo utilizando el nuevo widget de rotación en la barra de estado. El soporte de rotación también se ha extendido al compositor de mapas para que maneje correctamente el etiquetado, la simbología, etc.

**This feature was funded by:** [Japan Space Imaging Corporation (JSI)](http://www.spaceimaging.co.jp/)

**This feature was developed by:** [Faunalia](http://www.faunalia.eu/)

![](images/entries/b655549a3336c2fb16eef87f6f30fe50f5abe9f9.webp)
## Interfaz de usuario
### Característica: Selección de proyección mejorada/consistente
Todos los cuadros de diálogo ahora usan un widget de selección de proyección consistente, que permite seleccionar rápidamente entre proyecciones estándar/QGIS de proyectos recientemente utilizados.

![](images/entries/7a9b103d6b537f8fd6d2c53b81dc4f9a2e3f736c.webp)

.

{{<content-end >}}
