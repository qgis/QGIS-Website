---
draft: 'true'

---
# Mapeo de hábitat y avifauna de la reserva forestal Amurum con QGIS en Nigeria
La reserva forestal de Amurum se encuentra cerca de la ciudad de Jos, estado de Plateau, Nigeria. Fue fundada junto al inicio del Instituto de Investigación Ornitológica Leventis A.P. (APLORI) con la utilidad de la conservación natural, educación e investigación. APLORI es alojado por el Departamento de Zoología de la Universidad de Jos. Anualmente, un grupo de aproximadamente ocho estudiantes altamente motivados de toda Nigeria obtienen formación en Biología de la Conservación, estadísticas (con R) y también GIS a partir de 2011. En diciembre de 2011 durante dos semanas, estudiamos conceptos básicos de SIG y los aplicamos con QGIS para diversos fines de conservación. En este artículo describimos la forma en que usamos QGIS para mapear los hábitats y sus determinantes en la reserva de Amurum y cómo se usaron los mapas básicos de hábitat para obtener estratos con el fin de determinar eficientemente la distribución espacial de la avifauna incluyendo la biodiversidad.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## Mapeando elevación, relieve sombreado, pendiente y hábitats.
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) GdalTools fueron utilizadas para fusionar los conjuntos de datos originales y para recortar a un área más pequeña que contiene la reserva de manera que los conjuntos de datos ráster se mantengan relativamente pequeños. A través de GPS colectamos elevaciones y varias ubicaciones en la reserva.
3) En general, las elevaciones del conjunto de datos SRTM coincideron bien con las elevaciones recolectadas por gps. Se utilizaron modelos de terreno en GdalTools para calcular buzamientos de colinas y pendientes para el área. Estas variables son importantes desde un punto de vista ecológico porque están fuertemente asociadas al tipo de hábitat.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) Ya que teníamos la intención de desarrollar un mapa atractivo, interpolamos el mapa de elevaciones original (recortado) para obtener un mapa de mayor resolución. Utilizamos la herramienta warp en GdalTools. Mediante la herramienta de contorno obtuvimos líneas de contorno suaves.
5) Las coordenadas del límite de la reserva se obtuvieron recorriendo los límites de la reserva con un GPS. Los puntos del recorrido y las rutas almacenadas en el GPS se importaron sin problemas utilizando las herramientas GPS. Los puntos del recorrido y las rutas importadas se usaron para construir un archivo de forma poligonal. Las vías dentro de la reserva fueron mapeadas de manera similar.
6) Pudimos construir de manera rápida y precisa un mapa de hábitat de Amurum usando una imagen de satélite de Google que ingresamos al espacio de trabajo con el complemento Openlayers. La reserva tiene tres tipos de hábitats distintos: Sabana, bosque en galería y afloramiento rocoso. Sobre la base de la imagen de satélite, utilizamos el editor para dibujar polígonos que delimitan los tres hábitats. El establecer las opciones de ajuste correctamente permitió la construcción de polígonos no superpuestos.

## Cartografiando las distribuciones y diversidad de aves
Los mapas de hábitat fueron usados para generar ubicaciones al azar. El área de los diversos tipos de hábitat fue usado para generar un número proporcional de localizaciones a la superficie de cada tipo de hábitat (estratificación).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Conclusión
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Autores
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
