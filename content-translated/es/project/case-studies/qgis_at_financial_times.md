---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: proyecto
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: Uso de QGIS en el Equipo Gráfico de Financial Times
type: case-study

---
{{<content-start >}}
# Uso de QGIS en el Equipo Gráfico de Financial Times
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2016</span>
</p>

## Entrevista con Steven Bernard (Editor de diseño interactivo)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Steven, ¿Cual es el nombre de tu equipo de trabajo en FT? ¿Puede darnos una pequeña noción de lo que su equipo del FT está haciendo?

**Steve**: Nuestro equipo está en período de transición en este momento, tenemos un nuevo editor de visualización de datos, Alan Smith OBE (anteriormente de la ONS) que está sacudiendo las cosas y creando un solo equipo de gráficos. Tradicionalmente teníamos un equipo de gráficos web y un equipo de gráficos impresos. El equipo de impresión se encargaría de todos los gráficos de los periódicos, así como de crear versiones para ellos de la web. Mi equipo fue responsable de todo el contenido exclusivo de la web, además de trabajar estrechamente con los productores/desarrolladores interactivos en el diseño de gráficos interactivos.

El equipo recién formado permitirá un mayor intercambio de habilidades entre los diferentes medios.

Alan ha introducido un único flujo de trabajo digital para nuestro equipo, que incluye el uso de d3 para ayudar a crear un vocabulario gráfico más amplio y reducir el tiempo que lleva crear las imágenes.

![](../images/ft_europe_migration_balkan-route.png)

*Ejemplo: Flujos de migrantes. Ruto de los Balcanes Occidentales.*

**QGIS**: Cuántos colegas existen en su equipo?

**Steven**: Incluyendo todos los diseñadores, desarrolladores y estadísticos tenemos un equipo de 24

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](../images/ft_nigeria-migration_animation.gif)

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](../images/ft_gotthard-tunnel.png)

*Ejemplo: túnel ferroviario y caminero Gotardo en los Alpes Suizos.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: ¿Cómo descubrió QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](../images/ft_blm-federal-land-map.png)

*Example: Tierras públicas en los EE.UU*

**QGIS**: Qué otras herramientas utiliza aparte de QGIS y cómo las combina?

**Steven**: Si se trata simplemente de un mapa de localización sencillo, el 95% del trabajo se realiza en QGIS, y el pulido final se realiza en Adobe Illustrator.

Si estoy haciendo un mapa en relieve, entonces el proceso es mucho más complejo. Recuperaré archivos DEM de Nasa Earth Explorer y los traeré a QGIS para recortarlos a medida. Luego tomaré el DEM recortado en Blender para crear un render 3D. Si estoy usando una capa de satélite en el sombreado, descargaré una imagen de BlueMarble de la NASA y la llevaré a Blender también. El render exportado de Blender se vuelve a poner en QGIS para usarlo como capa de fondo. Puedo modificarlo en Photoshop de antemano si es necesario.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Otra herramienta útil es Google My Maps, que permite a los reporteros de todo el mundo marcar ubicaciones en un mapa y luego podemos descargarlas como un archivo kmz e importarlas directamente a QGIS.

La herramienta final que uso es Adobe After Effects, ya que recientemente me puse a animar mis mapas para llevar al usuario a viajar. Como se usó en la serie Land Rush recientemente:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Usa otras herramientas espaciales o SIG aparte de QGIS, y si así es, cuáles?

**Steven**: QGIS todo el tiempo para mi, pero como mencioné arriba algunos de mis colegas usan también Map Publisher.

![](../images/ft_isis-air-strikes_febupdate.png)

*Ejemplo: Ataques en Siria en Febrero 2016.*

**QGIS**: Puedes describir las fortalezas y debilidades de QGIS respecto a las tareas que tienes que hacer?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

En unas dos semanas estaba convencido de que sería viable. El principal punto de venta fue la capacidad de configurar guías de estilo para todo, incluido el estilo de nivel de zoom para mapas a nivel de calle.

Tengo un sistema configurado donde tenemos conjuntos de hojas de Google con columnas para nombre, latitud, longitud, icono de marcador, ancho de funete, tamaño de fuente y si desea que el marcador sea visible o no.

El icono del marcador es un menú desplegable conectado a una tabla vLookUp que contiene todos los detalles de ese marcador.

Así, todo lo que tengo que hacer es descargar el csv, importarlo en QGIS, aplicar un estilo y tengo un mapa que está 95% listo para entregar.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](../images/ft_chinaMigration.png)

*Ejemplo: Atracción y Migración Urbana dentro de China.*

**QGIS**: Cuáles son los conceptos o características que gustas más de QGIS?

**Steven**: ¡Hay numerosas características que clasificaría como salvavidas! Pero principalmente Quick OSM y Georeferencer me han ahorrado mucho tiempo, esto es absolutamente esencial cuando los plazos son ajustados. Lo cual, cuando se trabaja para una organización de noticias, suele ser el 90% del tiempo.

![](../images/ft_china_henanGuangdong.png)

*Ejemplo: Atracción y Migración Urbana dentro de China. Vistas detalle.*

**QGIS**: ¿Qué características o funcionalidades en QGIS extrañas más? ¿Tiene una lista de características faltantes que lo ayudarían mucho si se implementaran?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Ser capaz de guardar como imagen en archivos de mayor tamaño. Actualmente, esta es la única forma en que puedo crear un recorte georreferenciado de un archivo DEM para llevarlo a Blender. Pero está limitado al tamaño de su pantalla. Si tuviera un archivo DEM de 8,000 píxeles cargado en QGIS, me gustaría poder exportar el recorte a un tamaño mayor que mi pantalla para usarlo en video HD, por ejemplo.

**QGIS**: Si extraña ciertas característica que lo ayudaríans en QGIS, ¿consideraría mejorar QGIS usted mismo (con la codificación en QGIS core o los complementos de Python), o consideraría contratar a un desarrollador de QGIS para implementar la característica que falta para usted? ¿O buscarías otras herramientas para llenar ese vacío?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](../images/ft_us_broadband_internet_subscription.png)

*Ejemplo: Porcentaje de hogares con una suscripción internet en los EE.UU.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Gracias por su tiempo y el trabajo que hace para promover y documentar los flujos de trabajo en QGIS!

![](../images/ft_potrait_steve_bernard.jpg)

*Retrato de Steve Bernard. Editor de Diseño Interactivo del Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Preguntas de entrevista por A. Neumann y T. Sutton. Abril 2016.

{{<content-end >}}
