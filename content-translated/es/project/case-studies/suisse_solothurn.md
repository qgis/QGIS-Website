---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: proyecto
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS en el stack gubernamental FOSSGIS del Cantón de Solothurn en Suiza
type: case-study

---
{{<content-start >}}
# QGIS en el stack gubernamental FOSSGIS del Cantón de Solothurn en Suiza
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

El cantón de Solothurn brinda servicios e infraestructura a 250,000 ciudadanos de Solothurn. En el año 2001, el Parlamento Estatal decidió migrar de Windows a Linux. Las motivaciones eran ser independientes de un proveedor en particular, alentar la libre empresa y reducir los costos en licencias. Como resultado, el departamento SO!GIS del Cantón de Solothurn comenzó a cumplir los requisitos SIG de más de 3500 empleados con una estrategia FOSSGIS.

El primer paso que tomamos fue la introducción de UMN MapServer y la creación de un cliente SOMAP que ofrece un cliente WebGIS fácil de usar para cada uno de los 3500 empleados. El segundo paso fue la migración de todos nuestros datos geoespaciales de Shapefiles al motor de base de datos espacial PostGIS. La introducción fue muy exitosa, pero faltaba un SIG de escritorio fácil de usar.

Después de una evaluación de diferentes SIG de Escritorio decidimos usar QGIS en conjunto con GRASS, reemplazando ESRI ArcInfo y ArcView3 en el 2006.

La decisión fue tomada por los siguientes aspectos:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- OSGeo Organización del Proyecto
- GUI traducido en idioma alemán
- Documentación escrita en idioma alemán
- Un desarrollador activo (Marco Hugentobler) cerca de Solothurn en Suiza.
- Contrataremos Marco Hugentoble para implementar características faltantes / pendientes como Digitalizar y DiseñoMapa
- Desarrollo de aplicación y complemento con Python
- Creciente comunidad de usuarios
- Muy activa comunidad de desarrolladores
- Independencia de un solo sistema operativo

## Dónde usamos QGIS
A diferencia de los mapas interactivos servidos por UMN MapServer, el SIG de escritorio debe ofrecer una vista flexible de los datos geoespaciales de Solothurn. QGIS Desktop GIS es usado por más de 50 usuarios en su trabajo diario. Pero muchos de ellos no son expertos en SIG. Quieren visualizar y/o capturar datos geoespaciales con una interfaz de usuario intuitiva.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SODATA contiene un inventario legible por humanos de los modelos de datos y el usuario no experto en SIG puede utilizar esta base de datos para hallar la información que necesitan.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusión
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Autor
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Este artículo fue aportado en Mayo 2009 por el Dr. Horst Düster. Él es coordinador SIG en el Departameno de Geoinformación en el Cantón de Solothurn, Suiza.

{{<content-end >}}
