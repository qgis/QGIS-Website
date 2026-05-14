---
draft: 'true'

---
# Análisis de hábitat del lince en los Cárpatos del Sur
Un caso de estudio para promover el entendimiento básico de la modelización de hábitat de vida silvestre para estudiantes basado en datos Libres.
## Introducción
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodología
Todos los datos recopilados se procesaron con QGIS 2.6 y 2.8, se proyectaron en ETRS89 / ETRS-LAEA y se almacenaron de acuerdo con la directiva INSPIRE para cumplir con las normas de la UE. Se definió un **índice discreto de ponderaciones** global y se aplicó a todos los datos de entrada.

![Figure 1: Workflow - Lynx habitat expert model](./images/europe_lynx1.png)

**Descripción de flujo de trabajo**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Nota: Las clases de cobertura terrestre se agruparon por posible ocurrencia del lince y actividad humana. Aunque técnicamente es de origen más antiguo, la información relacionada con los valores de cobertura forestal se integró para indicar la mejora del hábitat y como un ejemplo general para unir conjuntos de datos espaciales*
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
    
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```

```
    .
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
    
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
    
*Nota: El Modelo de accesibilidad de caza debe indicar la probabilidad cada vez menor de que los cazadores accedan al área por una mayor distancia a las carreteras e incrementando de la pendiente*

![Figure 2, 3 and 4](./images/europe_lynx2.png)
## Conclusión
Al observar el resultado final (Figura 3), un primer análisis de hábitat potencial plausible pareció tener éxito, pero lo que es más importante, el modelado básico en sí mismo resultó ser menos difícil de lo que se esperaba inicialmente. Nuestra opción de agregar un submodelo para la accesibilidad del cazador nos permitió implementar otra dimensión en términos de evaluación del riesgo del hábitat, que puede ser simplemente anidada en el escenario ya existente y utilizada para determinar las necesidades de protección bajo aspectos de, por ejemplo, desarrollo de infraestructura. Sin embargo, no se puede obtener cierta información crucial sobre el hábitat, como la estructura del bosque (nuestra mayor idoneidad para el hábitat) mediante los conjuntos de datos disponibles y, en combinación con el complejo comportamiento de las especies, el resultado debe entenderse como básico e incompleto. Los factores adicionales que no se implementaron en esta etapa son la mortalidad en la carretera, la rugosidad del terreno y la presencia detallada de presas.

Además de su carácter de código abierto y libre, el software QGIS ha sido objeto de importantes desarrollos en los últimos años. Hicimos una experiencia muy positiva con la integración de la caja de herramientas, permitiendo el uso de varias herramientas de GRASS y SAGA, incluso para usuarios inexpertos. No se han producido problemas de compatibilidad a pesar de los cambios frecuentes entre las diferentes versiones y la ausencia general de restricciones administrativas puede ser una ventaja poderosa cuando se trabaja de forma intuitiva con conjuntos de datos. Estamos deseando ver nuevas mejoras, especialmente en lo que respecta al creador de modelos integrado.
## Referencias
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document European Commission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. Tesis PhD.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Autores
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe and David Winger son estudiantes de cuarto semestre del programa de estudios International Forest Ecosystem Management B.Sc., Anne Gnilke respectivamente Silvicultura Alemana y Henri Hiltunen es un estudiante de intercambio de Mikkeli University of Applied Sciences, Finland. Prof. Mund imparte clases de SIG y Teledetección en HNE Eberswalde desde 2010 y brindó orientación y apoyo técnico para el proyecto.

Por favor contacte Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, o Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de para mayor información.
