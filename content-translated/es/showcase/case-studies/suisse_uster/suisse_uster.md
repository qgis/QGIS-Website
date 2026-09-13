---
draft: 'true'

---
# El uso de QGIS en la Infraestructura de GeoDatos de la Ciudad de Uster
La ciudad de Uster ha estado utilizando QGIS desde 2007. Animado por la decisión del Cantón de Solothurn de utilizar QGIS como el SIG de escritorio reemplazando ArcView, Uster decidió darle una oportunidad. La ciudad se unión al esfuerzo de impulsar el desarrollo de la aplicación QGIS, aconsejando y probando nuevas características y finalmente apoyando el desarrollo económicamente. Como recompensa, Uster recibe un SIG de escritorio de rápida evolución e independiente de plataformas y una solución Web SIG respaldado por un usuario internacional y una comunidad de desarrollo.

![](./images/suisse_uster1.png){.align-right}

Postgis / PostgreSQL se utiliza como un almacén central de geodatos. Otras bases de datos y fuentes de datos se reproducen en PostgreSQL a intervalos regulares, utilizando herramientas como OGR y FME. Al principio, QGIS se utilizaba principalmente como visor. El primer usuario de QGIS fue un agricultor que tenía la tarea de supervisar las declaraciones hechas por los agricultores locales para recibir subsidios agrícolas. Más tarde, QGIS también se presentó como editor de datos y plataforma de publicación de mapas, junto con las mejoras de las herramientas de edición y el compositor de impresión. Junto con otros usuarios suizos de QGIS (Solothurn, Thun y CDE (Universidad de Berna)) coordinamos y patrocinamos las mejoras de estas herramientas, junto con algunas mejoras en la simbolización basada en datos, etiquetado automatizado, manejo de atributos y formularios.

![](./images/suisse_uster2.png){.align-right}

La administración de la ciudad también utiliza software comercial SIG: Autodesk Topobase, para la captura y edición de datos de infraestructura catastral y de aguas residuales, y GE Smallworld para la gestión de redes de gas, agua y electricidad. Sin embargo, estos son sistemas especializados para uso por personal especialmente capacitado. QGIS maneja todos los demás proyectos SIG y la visualización de todos los datos.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

Hoy, QGIS es utilizado por los siguientes proyectos SIG:
- visualización de datos de aguas residuales, integración de bases de datos adicionales y acceso directo a videos de canales y protocolos de inspección
- visualización y edición para el monitoreo y la planificación ambiental y urbana de los sistemas de aguas residuales e hidrología (alemán: Genereller Entwässerungsplan)
- visualización de datos catastrales subterráneos (redes de aguas residuales, agua, gas y electricidad, más tarde también telecomunicaciones) (alemán: Leitungskataster)
- vista de datos catastrales y de inspección
- vista y edición del inventario comunal de sitios protegidos naturales
- vista y edición de datos de planificación urbana y regional
- viendo y editando datos de infraestructuras de carreteras
- viendo estadísticas generadas directamente desde la base de datos de actuales y anteriores residentes
- planificación y visualización para planificación de energía (regiones de provisión de gas, uso de calor de aguas residuales, energía geotermal cercana a la superficie, estaciones de calentamiento de bloque, etc.)

Más proyectos adicionales están actualmente en desarrollo.

![](./images/suisse_uster4.png){.align-right}

En 2007 no estaba del todo claro a qué ritmo se desarrollaría más QGIS y cómo evolucionarían tanto el soporte comunitario como el comercial. Hoy se puede afirmar que la velocidad de desarrollo y las mejoras realizadas por la comunidad QGIS excedieron nuestras expectativas. El apoyo comunitario y comercial de las empresas Sourcepole y Norbit es excelente. Existe una comunicación directa con los desarrolladores sin estar protegido por un equipo de gestión de productos o ventas. Los desarrolladores de estas dos compañías también son desarrolladores principales del proyecto QGIS y tienen un excelente conocimiento de la base del código.

Los errores a menudo se corrigen dentro de las horas o días posteriores a la presentación de informes y los nuevos desarrollos se implementan en un corto período de tiempo. Las nuevas características pueden probarse inmediatamente después del desarrollo y desplegarse para los usuarios siempre que la calidad sea lo suficientemente buena para el usuario final. No hay necesidad de esperar los lanzamientos oficiales de software. Disfrutamos de la libertad de poder influir en el proyecto e instalar el software en tantas computadoras como queramos sin tener que lidiar con la gestión de licencias. Esperamos con interés la futura colaboración con la comunidad QGIS y nuestros seguidores comerciales para el avance del proyecto QGIS.
## Autor
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Este artículo fue contribuído en Abril 2011 por Dr. Andreas Neumann. Él es coordinador SIG en la Ciudad de Uster, Suiza.
