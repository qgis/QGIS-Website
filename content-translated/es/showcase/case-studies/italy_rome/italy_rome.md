---
draft: 'true'

---
# Modelo de geoprocesamiento QGIS para simplificar el análisis de microzonificación sísmica de primer nivel
The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Geoquímica ambiental y remediación de suelos y aguas contaminados;
- Depósitos minerales y procesamiento mineral, incluyendo el tratamiento de desechos;
- Geoingeniería y seguridad de las excavaciones de roca;
- Evolución geológica reciente;
- Mitigación de desastres naturales;
- Geoarqueología y arqueometría.
- Geología Marina
- Geomática, análisis y desarrollo SIG.

El nivel 1 del estudio de microzonificación sísmica del área de Pitramontecorvino (Apulia, Sur de Italia, ubicado a lo largo de la cadena Centro-Sur de los Apeninos) es parte de un proyecto, en colaboración con la Autoridad de Cuencas de Apulia (Puglia AdB) y el Departamento de Geología y Geofísica (DGG) de la Universidad de Bari, aspira a la microzonificación sísmica de 63 Municipios del área de Foggia. La actividad fue promovida por el Departamento italiano de Protección Civil (DPC) y financiado por el Comité Interministerial de Planeamiento Económico (CIPE n. 20/2004).
## Herramienta de geoprocesamiento QGIS para estudios sísmicos de microzonificación de primer nivel
La microzonificación sísmica evalúa el riesgo sísmico a escala local con el propósito de identificar areas del territorio caracterizados por un comportamiento sísmico homogéneo. El primer nivel de la microzonificación tiene el propósito de definir las propiedades litológicas y la geometría de las unidades geológicas que caracterizan estas porciones del territorio (microzonas).

La observación del daño causado por un terremoto a menudo muestra variaciones a escala local causada no solo por las estructuras geológicas sino también por la diferente calidad y tipo de estructuras de construcción, dando lugar a diferentes riesgos sísmicos.

La microzonificación sísmica evalúa el riesgo sísmico local, mediante la identificación de áreas del territorio que se caracterizan por comportamientos sísmicos homogéneos.

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

El primer nivel de microzonificación sísmica consiste en la creación de tres mapas temáticos:
1. Mapa de inspección conteniendo las inspecciones para estudios de microzonificación sísmica;
2. Mapa geolitológico, obtenido a partir de mapas geológicos y geomorfológicos a escala detallada que integran datos litológicos, estratigráficos y geotécnicos existentes relacionados con levantamientos;
3. Mapa de microzonificación de nivel 1 (el principal producto de microzonificación de nivel 1), identificando las microzonas en tres categorías de riesgos locales.
   - Zonas estables;
   - Zonas estables susceptibles a amplificación del suelo;
   - Zonas inestables.

El objetivo del trabajo es contribuir a la creación de una metodología para procesar los datos topográficos, geológicos, geofísicos y geotécnicos con el fin de elaborar mapas de nivel 1 de microzonificación sísmica, mediante el uso de herramientas de código abierto.

La herramienta de Modelado Gráfico integrada en la última versión de QGIS (2.8.1 en el momento de escribir esto) ha sido usada para la ceación de un modelo de geoprocesamiento simple. Esta herramienta es útil para automatizar uno de los análisis comúnmente realizado para la creación mapas de nivel 1 de microzonificación sísmica, en particular para identificar zonas inestables como entidades poligonales.

El modelo hace uso de diferentes software y bibliotecas de código abierto (GRASS, GDAL, QGIS), demonstrando la utilidad de QGIS como un interfaz simplificado y unificado para herramientas SGLCA (Software Geoespacial Libre y Código Abierto) (Fig. 1).

![(Fig. 1) Screenshot from the geoprocessing model.](./images/italy_igag1.png){.align-right}

El modelo toma como entrada (Fig. 2):
- Un shapefile de líneas contorno que contiene un campo con valores de elevación;
- The name of the field containing elevation values;
- La resolución deseable del ráster en metros para el MDT y Pendiente (predeterminada 10);
- Se extraerá un shapefile polígono con elementos que intersectan áreas con pendiente mayor a 15 grados;
- El nombre de la capa polígono resultante.

![(Fig. 2) Model input form (left) and execution log (right).](./images/italy_igag2.png){.align-right}

Cuando se lanza, el modelo realiza las siguientes operaciones:
- La herramienta de GRASS v.to.rast.attribute convierte las lineas de contorno de elevaciones a raster, tomando el contorno del shapefile, el nombre del campo Z y la resolución del raster como entradas;
- La herramienta de GRASS r.surf.contour genera un modelo de elevaciones tomando como entradas un raster temporal que es la salida obtenida del paso anterior y la resolución del raster;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- La herramienta GRASS r.mapcalculator es usada para generar un ráster de 1 bit que identifica áreas con pendiente mayor que 15 grados (este valor está codificado en las guías de microzonificación, de manera que es fijo), usando la expresión:

if(A\>15,1,null())

donde A es el ráster temporal generado por gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

El resultado es una capa poligonal con zonas propensas a la inestabilidad debido a un valor de pendiente mayor de 15 grados, automáticamente extraidos de un mapa temático como una capa poligonal de deslizamientos de tierra (Fig. 3) o un mapa litológico.

![(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).](./images/italy_igag3.png){.align-right}
## Conclusiones
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Referencias
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autores
Este artículo fue contribuído en Marzo 2015 por Giuseppe Cosentino y Francesco Pennica (www.igag.cnr.it).

![Giuseppe Cosentino](./images/guiseppe_cosentino.png){.align-left height="200px"}

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

![Francesco Pennica](./images/francesco_pennica.png){.align-left height="200px"}

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.
