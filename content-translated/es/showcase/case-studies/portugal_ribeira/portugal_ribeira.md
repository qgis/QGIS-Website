---
draft: 'true'

---
# QGIS y GRASS para la modelación de corredores ecológicos de lobos en el norte de Portugal
The Iberian wolf is a sub-species of the gray wolf that exists only in north of Portugal and Spain, with small isolated groups in the south of Douro river. During the last century, it suffered a high regression, being a "vulnerable" species in Spain and "endangered" in Portugal. Nowadays, there are only around 300 wolves in Portugal, due to the high persecution, destruction and fragmentation of the habitat.

![Study area in Portugal](./images/portugal_ribeira1.png){.align-right}

Ribeira de Pena es un municipio en el distrito de Villa Real en el norte de Portugal. Es un municipio rural, caracterizado por la agricultura, el pastoreo de ganado, bosques, montañas, valles y fauna diversa, junto con la baja densidad humana proporciona refugio y comida para los lobos. Ubicada en una zona de transición entre el duro y montañoso Trás-os-Montes y el verde Minho, Ribeira de Peña es uno de los municipios que puede funcionar como un corredor ecológico entre áreas con mayor concentración de lobos en el norte con otro con menor concentración en el sur.

Comencé usando software SIG durante mi curso de biología, y más a menudo durante mi tesis de maestría. En aquel tiempo usaba principalmente software privativo. Después de terminar mi grado de maestría, perdí acceso al software privativo.

Mientras tanto, entré en el nuevo mundo de Linux. Después de eso, me contactaron para ayudar a algunos investigadores a modelar corredores ecológicos para lobos en Ribeira de Pena, usando SIG, ya que nunca trabajaron con este tipo de software. Como ya estaba usando Linux en lugar de Windows, mi primer problema fue qué software usar. Luego escuché acerca de QGIS y decidí probarlo, aunque parecía muy simplista e incompleto, en comparación con lo que ya sabía. Rápidamente me di cuenta de lo equivocado que estaba y me entusiasmé mucho con las capacidades analíticas que QGIS proporcionaba, especialmente con la integración de GRASS.

Para modelar los corredores ecológicos, utilizamos QGIS junto con el complemento GRASS. Utilizamos varios datos geográficos junto con datos de presencia de la especie para modelar los corredores ecológicos. Estas son algunas de las funciones de QGIS y GRASS utilizadas en este caso, solo por nombrar algunas:
- complemento Interpolación en QGIS: para crear un Modelo Digital de Elevación
- r.watershed en GRASS: para crear cursos de agua a partir de MDT
- r.grow.distance en GRASS: genera una capa mapa ráster de distancia a las entidades en la capa de entrada
- r.reclass en GRASS: Para reclasificar capas
- r.slope.aspect.slope en GRASS: para calcular la pendiente a partir de un MDT
- r.mapcalculator en GRASS: para calcular alguna álgebra de mapa simple
- r.cost.coord en GRASS: crea un mapa ráster que muestra el costo acumulado de moverse entre diferentes ubicaciones geográficas en un mapa ráster de entrada cuyos valores de categoría de celda representan el costo.
- r.drain in GRASS: Traces a flow through an elevation model on a raster map \---- the one used to create the corridors

Con este trabajo obtuvimos un mapa con los posibles corredores ecológicos para el lobo en el municipio de Ribeira de Pena. Estas son áreas a considerar por los técnicos del ayuntamiento cuando planifiquen medidas de conservación para la especie. Estos corredores son de extrema importancia porque permiten conectar las frágiles manadas de lobos en Vila Real, en el sur, con las del norte, que continúan con las de Peneda-Gerês y España, mucho más estables. Son de particular importancia aquellos corredores que cruzan asentamientos humanos, como pequeños pueblos, ciudades y carreteras. Estas áreas deben considerarse críticas para la conservación del lobo, y aplicar medidas para reducir el impacto humano en esta especie.

![Ecological corridors and critical conservation areas for wolves in northern Portugal.](./images/portugal_ribeira2.png){.align-right width="100.0%"}
## Conclusión
Both QGIS and plugin GRASS are very intuitive with user-friendly interface, with all essential functions to perform most analysis. For what I could see, QGIS and GRASS perform equally as well as the proprietary programs I was most familiar with from college days, with the big advantage of free open-source software, usable in every computer or notebook without licenses, constant upgrades and the ultimate advantage to contribute to it\'s improvement and/or tip the developers about some essential function.

Changing to Linux and then to QGIS and GRASS was one of my best calls, and although there can be some missing issues, easily resolved in the future with the developers, I don\'t regret my decision and advise everyone to use them.
## Autor
![Monica Almeida](./images/portugal_ribeiraaut.png){.align-left height="200px"}

Este artículo fue aportado en Julio 2012 por Monica Almeida. Ella es bióloga de la conservación y trabaja en una organización no gubernamental para la preservación del lobo en Portugal.
